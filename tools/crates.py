import math,random,sys
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
sys.path.insert(0,'tools')
from brand_logos import vpk_icon
S=2
BLK=(20,20,22); RED=(190,30,26); PAPER=(244,240,230); GREY=(110,112,118)
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def inter(sz,w='ExtraBold'): return ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-'+w+'.otf',int(sz*S))
def px(v): return int(v*S)

# ---------- pictograms: red diamond, black symbol, caption ----------
def pictogram(name,caption,draw_symbol):
    W=H=px(512); im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    cx,cy,r=W//2,px(220),px(200)
    d.polygon([(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)],fill=(255,255,255,255))
    for k in range(px(22)): d.polygon([(cx,cy-r+k),(cx+r-k,cy),(cx,cy+r-k),(cx-r+k,cy)],outline=RED+(255,))
    draw_symbol(d,cx,cy)
    d.rounded_rectangle([px(40),px(436),W-px(40),px(496)],radius=px(8),fill=PAPER+(255,),outline=BLK+(255,),width=px(3))
    d.text((W//2,px(466)),caption,font=mono(24),fill=BLK,anchor='mm')
    im.resize((512,512),Image.LANCZOS).save(f'crates/kdpx_pictogram_{name}_512.png',optimize=True)
    return im
def sym_kd(d,cx,cy): d.text((cx,cy+px(4)),"Kd",font=inter(110),fill=BLK,anchor='mm'); d.text((cx-px(70),cy-px(78)),"404",font=mono(24),fill=BLK,anchor='mm')
def sym_drop(d,cx,cy):
    rr=px(62); y=cy+px(30)
    d.ellipse([cx-rr,y-rr,cx+rr,y+rr],fill=BLK); d.polygon([(cx-rr*0.92,y-rr*0.38),(cx,y-rr*2.5),(cx+rr*0.92,y-rr*0.38)],fill=BLK)
    d.ellipse([cx-rr*0.5,y-rr*0.35,cx-rr*0.15,y+rr*0.05],fill=(255,255,255))
def sym_lick(d,cx,cy):
    # a face sticking its tongue out, crossed out
    W_=(255,255,255)
    R=px(100); y=cy-px(10)
    d.ellipse([cx-R,y-R,cx+R,y+R],outline=BLK,width=px(14))
    for ex in (-38,38): d.ellipse([cx+px(ex)-px(13),y-px(45),cx+px(ex)+px(13),y-px(19)],fill=BLK)
    d.arc([cx-px(52),y-px(20),cx+px(52),y+px(44)],20,160,fill=BLK,width=px(12))
    d.rounded_rectangle([cx-px(26),y+px(30),cx+px(26),y+px(98)],radius=px(26),fill=BLK)
    d.line([(cx,y+px(40)),(cx,y+px(80))],fill=W_,width=px(5))
    d.line([(cx-px(115),cy+px(115)),(cx+px(115),cy-px(115))],fill=RED,width=px(18))
def sym_radio(d,cx,cy):
    R=px(105); r=px(24)
    for a in (90,210,330):
        d.pieslice([cx-R,cy-R,cx+R,cy+R],-a-30,-a+30,fill=BLK)
    d.ellipse([cx-px(38),cy-px(38),cx+px(38),cy+px(38)],fill=(255,255,255))
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=BLK)
def sym_explode(d,cx,cy):
    # GHS "exploding bomb": a small bomb, many thin spikes, small fragments flying out
    rnd=random.Random(21); bx,by=cx-px(8),cy+px(6)
    for k in range(34):
        a=rnd.uniform(0,2*math.pi); r0=px(30); r1=px(rnd.randint(70,128))
        w=rnd.choice((px(3),px(4),px(5)))
        d.line([(bx+math.cos(a)*r0,by+math.sin(a)*r0),(bx+math.cos(a)*r1,by+math.sin(a)*r1)],fill=BLK,width=w)
    for k in range(14):
        a=rnd.uniform(-0.6*math.pi,0.5*math.pi); r=px(rnd.randint(70,125)); x,y=bx+math.cos(a)*r,by+math.sin(a)*r; sz=px(rnd.randint(6,11))
        t=rnd.uniform(0,6.28)
        d.polygon([(x+math.cos(t)*sz,y+math.sin(t)*sz),(x+math.cos(t+2.3)*sz,y+math.sin(t+2.3)*sz),(x+math.cos(t+4.0)*sz*0.6,y+math.sin(t+4.0)*sz*0.6)],fill=BLK)
    R=px(34); d.ellipse([bx-R,by-R,bx+R,by+R],fill=BLK)
    d.ellipse([bx-px(20),by-px(22),bx-px(6),by-px(8)],fill=(255,255,255))
def sym_health(d,cx,cy):
    # GHS "health hazard": a bust with a burst on the chest
    W_=(255,255,255); y=cy-px(14)
    d.ellipse([cx-px(30),y-px(96),cx+px(30),y-px(36)],fill=BLK)
    d.rectangle([cx-px(16),y-px(44),cx+px(16),y-px(20)],fill=BLK)
    d.pieslice([cx-px(78),y-px(28),cx+px(78),y+px(140)],180,360,fill=BLK)
    d.rectangle([cx-px(78),y+px(55),cx+px(78),y+px(96)],fill=BLK)
    pts=[]
    for k in range(16):
        a=math.radians(k*22.5); r=px(34) if k%2==0 else px(12)
        pts.append((cx+math.cos(a)*r,y+px(48)+math.sin(a)*r))
    d.polygon(pts,fill=W_)
def sym_reflex(d,cx,cy):
    for a,b in (((cx-px(95),cy),(cx-px(25),cy)),((cx+px(25),cy),(cx+px(95),cy)),((cx,cy-px(95)),(cx,cy-px(25))),((cx,cy+px(25)),(cx,cy+px(95)))):
        d.line([a,b],fill=BLK,width=px(16))
    d.ellipse([cx+px(35),cy+px(35),cx+px(105),cy+px(105)],outline=BLK,width=px(9))
    d.line([(cx+px(70),cy+px(70)),(cx+px(70),cy+px(48))],fill=BLK,width=px(7)); d.line([(cx+px(70),cy+px(70)),(cx+px(88),cy+px(70))],fill=BLK,width=px(7))
def sym_snow(d,cx,cy):
    R=px(100)
    for k in range(6):
        a=math.radians(k*60-90); d.line([(cx,cy),(cx+math.cos(a)*R,cy+math.sin(a)*R)],fill=BLK,width=px(14))
        for t,l in ((0.55,0.35),):
            bx,by=cx+math.cos(a)*R*t,cy+math.sin(a)*R*t
            for s_ in (-1,1):
                b=a+s_*math.radians(45); d.line([(bx,by),(bx+math.cos(b)*R*l,by+math.sin(b)*R*l)],fill=BLK,width=px(10))
def sym_boot(d,cx,cy):
    bx,by=cx-px(70),cy+px(40)
    d.polygon([(bx,by-px(110)),(bx+px(70),by-px(110)),(bx+px(80),by-px(30)),(bx+px(160),by-px(12)),(bx+px(168),by+px(36)),(bx,by+px(36))],fill=BLK)
    d.ellipse([cx-px(120),cy-px(120),cx+px(120),cy+px(120)],outline=RED,width=px(16))
    d.line([(cx-px(85),cy+px(85)),(cx+px(85),cy-px(85))],fill=RED,width=px(16))
picts=[('kdanium',"KDANIUM",sym_kd),('weather',"CONTAINS WEATHER",sym_drop),('health-hazard',"MAY CAUSE DERANKING",sym_health),
       ('radioactive',"HIGHLY RADIOACTIVE",sym_radio),('cryogenic',"KEEP BELOW 0 °K",sym_snow),('explosive',"EXPLOSIVE",sym_explode)]
ims=[pictogram(n,c,f) for n,c,f in picts]
sheet=Image.new('RGBA',(px(512)*3,px(512)*2),(60,50,38,255))
for i,im in enumerate(ims): sheet.alpha_composite(im,((i%3)*px(512),(i//3)*px(512)))
sheet.resize((1536,1024),Image.LANCZOS).convert('RGB').save('crates/_pictogram_preview.png')

# ---------- shipping label ----------
W,H=px(1024),px(768)
im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
d.rectangle([px(10),px(10),W-px(10),H-px(10)],outline=BLK,width=px(5))
d.rectangle([px(10),px(10),W-px(10),px(110)],fill=BLK)
im.alpha_composite(vpk_icon(1024,BLK).resize((px(74),px(74)),Image.LANCZOS),(px(28),px(23))); d=ImageDraw.Draw(im)
d.text((px(120),px(60)),"VPK INDUSTRIES · KD-PX SHIPMENT",font=bebas(62),fill=PAPER,anchor='lm')
d.text((W-px(28),px(60)),"WAYBILL",font=mono(26),fill=(224,176,48),anchor='rm')
def box(x0,y0,x1,y1,label,lines,big=None):
    d.rectangle([x0,y0,x1,y1],outline=BLK,width=px(3))
    d.text((x0+px(14),y0+px(10)),label,font=mono(15,'SemiBold'),fill=GREY)
    y=y0+px(36)
    if big: d.text((x0+px(14),y),big,font=bebas(56),fill=BLK); y+=px(60)
    for l in lines: d.text((x0+px(14),y),l,font=mono(19),fill=BLK); y+=px(26)
box(px(30),px(130),px(500),px(300),"FROM",["SECTOR: [CLASSIFIED]","ADDRESS: [CLASSIFIED]"],"[CLASSIFIED]")
box(px(520),px(130),W-px(30),px(300),"TO",["SECTOR: DUST II","ATTN: DANIEL K."],"NONVIS-001 OASIS")
box(px(30),px(318),px(500),px(520),"CONTENTS",["KD-PX-001  DynaRain™        x 22","KD-PX-002  DynaRain™ Splash x 22","KD-PX-004  Cigarette Smoke   x 1","KD-PX-012  SmokeScreen Pro™ x 1"])
box(px(520),px(318),W-px(30),px(520),"DETAILS",["WEIGHT:   [?] (NOT FOUND)","CARRIER:  [REDACTED]","DELIVERY: BEFORE THE ROUND","SIGNED:   Daniel K."])
# handling icons row
d.text((px(40),px(540)),"HANDLING",font=mono(15,'SemiBold'),fill=GREY)
x=px(40)
for t in ("THIS SIDE UP","KEEP DRY (IRONIC)","DO NOT LICK","KEEP BELOW 0 °K... WAIT, NO."):
    w=d.textlength(t,font=mono(17))+px(24); d.rectangle([x,px(565),x+w,px(600)],outline=BLK,width=px(3)); d.text((x+px(12),px(582)),t,font=mono(17),fill=BLK,anchor='lm'); x+=w+px(12)
# barcode + tracking
r=random.Random(404); bx=px(40); y0b,y1b=px(625),px(715)
while bx<px(560):
    w=r.choice((px(2),px(3),px(5),px(7))); d.rectangle([bx,y0b,bx+w,y1b],fill=BLK); bx+=w+r.choice((px(2),px(3),px(5)))
d.text((px(40),px(735)),"KDPX-404-0001-OASIS",font=mono(18),fill=BLK,anchor='lm')
# priority stamp area
d.rectangle([px(600),px(625),W-px(30),px(745)],fill=RED)
d.text(((px(600)+W-px(30))//2,px(670)),"PRIORITY: WEATHER",font=bebas(54),fill=PAPER,anchor='mm')
d.text(((px(600)+W-px(30))//2,px(718)),"CLASSIFIED · NONVIS CLEARANCE REQUIRED",font=mono(14,'SemiBold'),fill=PAPER,anchor='mm')
# wear
n=Image.effect_noise((W//2,H//2),14).resize((W,H),Image.BICUBIC)
g=Image.new('RGBA',(W,H),(0,0,0,0)); g.putalpha(n.point(lambda v:max(0,v-128)//3)); im=Image.alpha_composite(im,g)
gr=Image.effect_noise((W//64,H//64),70).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(px(18))).point(lambda v:max(0,v-140)*3)
go=Image.new('RGBA',(W,H),(90,70,40,0)); go.putalpha(gr.point(lambda v:int(v*0.12))); im=Image.alpha_composite(im,go)
im.resize((1024,768),Image.LANCZOS).convert('RGB').save('crates/kdpx_shipping_label_1024x768.png',optimize=True)
print('ok')
