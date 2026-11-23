import math,random,sys
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
sys.path.insert(0,'tools')
from brand_logos import vpk_icon,nonvis_icon
S=2; W,H=1024*S,1536*S
NAVY=(24,34,58); NAVY2=(16,23,40); WHITE=(236,238,240); YEL=(224,176,48); RED=(178,34,30); TEAL=(150,212,199); GREY=(150,165,190)
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def px(v): return int(v*S)
def inter(sz,w='ExtraBold'): return ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-'+w+'.otf',int(sz*S))
VPK=vpk_icon(1024); EYE=nonvis_icon(1024)

def base(bg=NAVY):
    im=Image.new('RGBA',(W,H),bg+(255,)); d=ImageDraw.Draw(im)
    # frame
    d.rectangle([px(28),px(28),W-px(28),H-px(28)],outline=WHITE+(255,),width=px(4))
    return im,d
def headline(d,lines,y,col=WHITE,size=150,gap=0.86):
    for i,l in enumerate(lines):
        d.text((W//2,y+i*px(size*gap)),l,font=bebas(size),fill=col,anchor='mt')
def footer(im,d,extra=None):
    y=H-px(150)
    d.line([(px(70),y),(W-px(70),y)],fill=GREY+(255,),width=px(2))
    im.alpha_composite(VPK.resize((px(84),px(84)),Image.LANCZOS),(px(70),y+px(26)))
    d=ImageDraw.Draw(im)
    d.text((px(172),y+px(30)),"VPK INDUSTRIES",font=bebas(44),fill=WHITE)
    d.text((px(172),y+px(78)),"WE OWN THE WORLD. LITERALLY.",font=mono(17),fill=YEL)
    if extra: d.text((W-px(70),y+px(52)),extra,font=mono(15,'SemiBold'),fill=GREY,anchor='rm')
    return d
GRIME=0.14
def finish(im,name):
    # paper grain + grime + worn edges
    n=Image.effect_noise((W//2,H//2),18).resize((W,H),Image.BICUBIC)
    g=Image.new('RGBA',(W,H),(255,255,255,0)); g.putalpha(n.point(lambda v:max(0,v-128)//4)); im=Image.alpha_composite(im,g)
    gr=Image.effect_noise((W//64,H//64),70).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(px(20))).point(lambda v:max(0,v-140)*3)
    go=Image.new('RGBA',(W,H),(40,30,18,0)); go.putalpha(gr.point(lambda v:int(v*GRIME))); im=Image.alpha_composite(im,go)
    vg=Image.new('L',(W,H),255); ImageDraw.Draw(vg).rectangle([px(40),px(40),W-px(40),H-px(40)],fill=0)
    vo=Image.new('RGBA',(W,H),(0,0,0,0)); vo.putalpha(vg.filter(ImageFilter.GaussianBlur(px(50))).point(lambda v:int(v*0.5))); im=Image.alpha_composite(im,vo)
    im.resize((1024,1536),Image.LANCZOS).convert('RGB').save('posters/'+name,optimize=True)

def rain(d,box,n,seed,col=(200,215,240,90)):
    r=random.Random(seed); x0,y0,x1,y1=box
    for _ in range(n):
        x=r.uniform(x0,x1); y=r.uniform(y0,y1); l=r.uniform(px(30),px(70))
        d.line([(x,y),(x+l*0.18,y+l)],fill=col,width=px(2))

# 1. RAIN IS A PRIVILEGE
im,d=base(); lay=Image.new('RGBA',(W,H),(0,0,0,0)); rain(ImageDraw.Draw(lay),(px(40),px(40),W-px(40),H-px(200)),260,1); im=Image.alpha_composite(im,lay); d=ImageDraw.Draw(im)
cx,cy,R=W//2,px(620),px(190)
d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=YEL)
d.polygon([(cx-R*0.93,cy-R*0.36),(cx,cy-R*2.25),(cx+R*0.93,cy-R*0.36)],fill=YEL)
d.ellipse([cx-R*0.55,cy-R*0.45,cx-R*0.2,cy-R*0.0],fill=(245,215,120))
d.text((cx-px(18),cy+px(10)),"Kd",font=inter(108),fill=NAVY,anchor='rm')
d.text((cx-px(16),cy+px(44)),"2",font=inter(56),fill=NAVY,anchor='lm')
d.text((cx+px(22),cy+px(10)),"O",font=inter(108),fill=NAVY,anchor='lm')
headline(d,["RAIN IS A","PRIVILEGE."],px(860),WHITE,160)
d.text((W//2,px(1160)),"DynaRain™ · KD-PX-001",font=mono(26),fill=TEAL,anchor='mt')
d.text((W//2,px(1205)),"WEATHER PASS™ SEASON 1: NIGHTFALL · NOW AVAILABLE",font=mono(19,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"WETTER THAN NATURE.")
finish(im,'poster_rain-is-a-privilege_1024x1536.png')

# 2. REPORT ALL VANDALISM
im,d=base(NAVY2)
e=nonvis_icon(1024,NAVY2).resize((px(620),px(620)),Image.LANCZOS); im.alpha_composite(e,(W//2-px(310),px(110))); d=ImageDraw.Draw(im)
headline(d,["REPORT ALL","VANDALISM."],px(780),WHITE,150)
d.rectangle([px(90),px(1060),W-px(90),px(1160)],fill=RED)
d.text((W//2,px(1110)),"V.I.G.I.L. ALREADY DID.",font=bebas(84),fill=WHITE,anchor='mm')
d.text((W//2,px(1200)),"KD-MCS-001 · EVERYTHING IS LOGGED. EVERYTHING!",font=mono(19,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"NONVIS DIVISION")
finish(im,'poster_report-all-vandalism_1024x1536.png')

# 3. EMPLOYEE OF THE MONTH
im,d=base()
headline(d,["EMPLOYEE","OF THE MONTH"],px(90),YEL,140)
fx0,fy0,fx1,fy1=px(262),px(370),W-px(262),px(900)
d.rectangle([fx0-px(14),fy0-px(14),fx1+px(14),fy1+px(14)],fill=(200,170,90))
d.rectangle([fx0,fy0,fx1,fy1],fill=(60,72,96))
hx=(fx0+fx1)//2; d.ellipse([hx-px(95),fy0+px(110),hx+px(95),fy0+px(300)],fill=(36,46,70))
d.pieslice([hx-px(210),fy0+px(320),hx+px(210),fy1+px(220)],180,360,fill=(36,46,70))
d.rectangle([fx0,fy0+px(225),fx1,fy0+px(285)],fill=RED)
d.text((hx,fy0+px(255)),"PHOTO UNAVAILABLE",font=mono(26),fill=WHITE,anchor='mm')
d.text((W//2,px(950)),"DANIEL K.",font=bebas(150),fill=WHITE,anchor='mt')
d.text((W//2,px(1100)),"CONGRATULATIONS, DANIEL! AGAIN.",font=mono(24),fill=TEAL,anchor='mt')
months="JAN · FEB · MAR · APR · MAY · JUN · JUL · AUG · SEP · OCT · NOV · DEC"
d.text((W//2,px(1160)),months,font=mono(15,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1190)),"DANIEL K. (EVERY MONTH) · EMP-0001",font=mono(15,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"HUMAN RESOURCES")
finish(im,'poster_employee-of-the-month_1024x1536.png')

# 4. THE DARKNESS IS FREE
im,d=base(NAVY2)
# street lamp with a light cone
lay=Image.new('RGBA',(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lay)
ld.polygon([(px(560),px(330)),(px(250),px(980)),(px(870),px(980))],fill=(255,214,120,70))
im=Image.alpha_composite(im,lay.filter(ImageFilter.GaussianBlur(px(18)))); d=ImageDraw.Draw(im)
d.rectangle([px(300),px(220),px(330),px(980)],fill=(120,130,150))
d.arc([px(300),px(160),px(600),px(400)],180,270,fill=(120,130,150),width=px(30))
d.chord([px(460),px(250),px(660),px(360)],180,360,fill=(90,100,120))
d.ellipse([px(500),px(318),px(620),px(352)],fill=(255,226,140))
# price tag
tx,ty=px(640),px(470)
d.polygon([(tx,ty),(tx+px(230),ty),(tx+px(230),ty+px(120)),(tx,ty+px(120)),(tx-px(50),ty+px(60))],fill=YEL)
d.ellipse([tx-px(22),ty+px(50),tx-px(2),ty+px(70)],fill=NAVY2)
d.text((tx+px(118),ty+px(42)),"4.99",font=bebas(70),fill=NAVY2,anchor='mm')
d.text((tx+px(118),ty+px(92)),"/ MONTH",font=mono(18),fill=NAVY2,anchor='mm')
headline(d,["THE DARKNESS","IS FREE."],px(1000),WHITE,128)
d.text((W//2,px(1225)),"THE LIGHT COSTS EXTRA.",font=bebas(64),fill=YEL,anchor='mt')
d=footer(im,d,"LIGHT SUBSCRIPTION™")
finish(im,'poster_the-darkness-is-free_1024x1536.png')

# 5. KDANIUM
im,d=base()
tx0,ty0,tx1,ty1=px(212),px(130),W-px(212),px(730)
d.rectangle([tx0,ty0,tx1,ty1],fill=WHITE); d.rectangle([tx0,ty0,tx1,ty1],outline=YEL,width=px(14))
d.text((tx0+px(40),ty0+px(30)),"404",font=mono(60),fill=NAVY)
d.text((tx1-px(40),ty0+px(42)),"[?]",font=mono(40),fill=RED,anchor='ra')
d.text(((tx0+tx1)//2,ty0+px(320)),"Kd",font=inter(290),fill=NAVY,anchor='mm')
d.text(((tx0+tx1)//2,ty1-px(80)),"KDANIUM",font=bebas(76),fill=NAVY,anchor='mm')
headline(d,["THE ELEMENT","OF PERFECTION."],px(800),WHITE,136)
d.text((W//2,px(1080)),"RAIN · SNOW · FIRE · SMOKE · ANYTHING",font=mono(22),fill=TEAL,anchor='mt')
d.text((W//2,px(1125)),"YOU WILL NOT FIND IT IN ANY PERIODIC TABLE.",font=mono(19,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1158)),"THAT IS NOT A MISTAKE.",font=mono(19,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1205)),"DO NOT DRINK · DO NOT LICK · DO NOT INHALE",font=mono(19),fill=RED,anchor='mt')
d=footer(im,d,"KD-PX SERIES")
finish(im,'poster_kdanium_1024x1536.png')

# 6. DAYS WITHOUT AN INCIDENT
im,d=base(NAVY2)
d.rectangle([px(60),px(60),W-px(60),px(150)],fill=YEL)
for k in range(-2,40):
    x=px(60)+k*px(60); d.polygon([(x,px(60)),(x+px(30),px(60)),(x+px(30)-px(90),px(150)),(x-px(90),px(150))],fill=(20,20,20))
d.rectangle([0,0,px(60),px(160)],fill=NAVY2); d.rectangle([W-px(60),0,W,px(160)],fill=NAVY2)
d.rectangle([px(28),px(28),W-px(28),H-px(28)],outline=WHITE,width=px(4))
headline(d,["DAYS WITHOUT","AN INCIDENT"],px(210),WHITE,130)
bx0,by0,bx1,by1=px(312),px(460),W-px(312),px(900)
d.rounded_rectangle([bx0,by0,bx1,by1],radius=px(24),fill=(10,12,18),outline=GREY,width=px(6))
d.line([(bx0,(by0+by1)//2),(bx1,(by0+by1)//2)],fill=(40,44,52),width=px(6))
d.text(((bx0+bx1)//2,(by0+by1)//2),"0",font=bebas(420),fill=RED,anchor='mm')
rows=[("#001","RAINMAKER Mk I","EXPLODED"),("#002","S.T.R.A.T.O.S.","KICKED"),("#003","F.O.R.E.C.A.S.T.","COFFEE"),("#004","CLASSIFIED AREA","MILK"),("#005","UDDER LEDGER","SPILLED")]
y=px(930)
d.text((W//2,y),"RECENT INCIDENTS",font=mono(22),fill=YEL,anchor='mt'); y+=px(50)
for a,b,c in rows:
    d.text((px(200),y),a,font=mono(22),fill=GREY); d.text((px(320),y),b,font=mono(22),fill=WHITE); d.text((W-px(200),y),c,font=mono(22),fill=RED,anchor='ra'); y+=px(40)
d.text((W//2,y+px(16)),"SAFETY IS OUR NUMBER TWO PRIORITY.",font=mono(20,'SemiBold'),fill=TEAL,anchor='mt')
d=footer(im,d,"FACILITY SAFETY")
finish(im,'poster_days-without-an-incident_1024x1536.png')
print('ok')
