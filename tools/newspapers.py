import math,random,textwrap
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
S=2; W,H=1024*S,1448*S
PAPER=(232,226,208); INK=(28,26,24); GREYI=(120,114,104); RED=(150,30,24)
def px(v): return int(v*S)
def serif(sz,bold=False): return ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-'+('Bold' if bold else 'Regular')+'.ttf',int(sz*S))
def cond(sz): return ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def inter(sz,w='ExtraBold'): return ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-'+w+'.otf',int(sz*S))
M=px(60)
def wraptext(d,text,font,x,y,w,lh,col=INK):
    words=text.split(); line=""
    for wd in words:
        t=(line+" "+wd).strip()
        if d.textlength(t,font=font)<=w: line=t
        else: d.text((x,y),line,font=font,fill=col); y+=lh; line=wd
    if line: d.text((x,y),line,font=font,fill=col); y+=lh
    return y
def filler(d,x,y,w,y_end,seed):
    r=random.Random(seed)
    while y<y_end:
        lw=w if r.random()>0.12 else int(w*r.uniform(0.3,0.8))
        d.line([(x,y+px(7)),(x+lw,y+px(7))],fill=(150,144,132),width=px(5)); y+=px(17)
        if r.random()<0.08: y+=px(14)
def headline(d,text,y,size):
    f=cond(size)
    while d.textlength(text,font=f)>W-2*M: size-=2; f=cond(size)
    d.text((W//2,y),text,font=f,fill=INK,anchor='mt')
def masthead(d,name,motto,price):
    d.text((W//2,px(40)),name,font=serif(92,True),fill=INK,anchor='mt')
    d.line([(M,px(160)),(W-M,px(160))],fill=INK,width=px(5)); d.line([(M,px(168)),(W-M,px(168))],fill=INK,width=px(2))
    d.text((M,px(180)),"VOL. 404 · NO. 1",font=serif(17),fill=INK)
    d.text((W//2,px(180)),motto,font=serif(17),fill=INK,anchor='mt')
    d.text((W-M,px(180)),price,font=serif(17),fill=INK,anchor='ra')
    d.line([(M,px(212)),(W-M,px(212))],fill=INK,width=px(2))
def halftone(img,box):
    # printed photo: greyscale, slightly soft, with a fine dot screen
    x0,y0,x1,y1=box; g=img.crop(box).convert('L').filter(ImageFilter.GaussianBlur(px(1)))
    w,h=x1-x0,y1-y0; scr=Image.new('L',(w,h),255); sd=ImageDraw.Draw(scr); st=px(5)
    for y in range(0,h,st):
        for x in range(0,w,st): sd.ellipse([x+px(1),y+px(1),x+st-px(1),y+st-px(1)],fill=225)
    g=ImageChops.multiply(g,scr)
    tint=Image.merge('RGB',[g.point(lambda v,c=c:int(c*v/255)) for c in PAPER]).convert('RGBA')
    img.alpha_composite(tint,(x0,y0))
    ImageDraw.Draw(img).rectangle(box,outline=INK,width=px(3))
def finish(im,name):
    n=Image.effect_noise((W//2,H//2),20).resize((W,H),Image.BICUBIC)
    g=Image.new('RGBA',(W,H),(255,255,255,0)); g.putalpha(n.point(lambda v:max(0,v-128)//3)); im=Image.alpha_composite(im,g)
    gr=Image.effect_noise((W//64,H//64),70).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(px(24))).point(lambda v:max(0,v-140)*3)
    go=Image.new('RGBA',(W,H),(120,90,40,0)); go.putalpha(gr.point(lambda v:int(v*0.18))); im=Image.alpha_composite(im,go)
    # a fold line in the middle
    fl=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(fl).line([(0,H//2),(W,H//2)],fill=(0,0,0,40),width=px(3)); im=Image.alpha_composite(im,fl.filter(ImageFilter.GaussianBlur(px(3))))
    im.resize((1024,1448),Image.LANCZOS).convert('RGB').save('papers/'+name,optimize=True)
def body_columns(d,y,lead,seed,y_end=None):
    y_end=y_end or H-px(70); cw=(W-2*M-px(40))//3
    for c in range(3):
        x=M+c*(cw+px(20))
        yy=y
        if c==0: yy=wraptext(d,lead,serif(17),x,yy,cw,px(24))+px(10)
        filler(d,x,yy,cw,y_end,seed+c)
        if c<2: d.line([(x+cw+px(10),y),(x+cw+px(10),y_end)],fill=GREYI,width=px(1))

# ---------- 1. THE DAILY PINT: milk overtakes gold ----------
im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
masthead(d,"The Daily Pint","“ALL THE NEWS THAT'S FIT TO DRINK”","PRICE: 1 GLASS")
headline(d,"MILK OVERTAKES GOLD",px(232),84)
d.text((W//2,px(340)),"Central banks sell reserves · currencies re-pegged to the pint · “Gold is just shiny milk now,” says analyst",font=serif(20),fill=INK,anchor='mt')
# chart image
ch=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(ch)
bx0,by0,bx1,by1=M,px(400),W-M,px(860)
cd.rectangle([bx0,by0,bx1,by1],fill=(230,230,230,255))
for k in range(6): cd.line([(bx0,by0+k*(by1-by0)//6),(bx1,by0+k*(by1-by0)//6)],fill=(190,190,190,255),width=px(2))
g=[(0,0.62),(0.2,0.6),(0.4,0.63),(0.6,0.58),(0.8,0.6),(1,0.57)]; m=[(0,0.92),(0.2,0.9),(0.4,0.8),(0.55,0.6),(0.7,0.35),(0.85,0.18),(1,0.06)]
P=lambda t:(bx0+px(40)+t[0]*(bx1-bx0-px(80)),by0+t[1]*(by1-by0))
cd.line([P(t) for t in g],fill=(110,110,110,255),width=px(10),joint='curve'); cd.line([P(t) for t in m],fill=(20,20,20,255),width=px(14),joint='curve')
cd.text((P(g[-1])[0]-px(10),P(g[-1])[1]+px(14)),"GOLD",font=bebas(48),fill=(110,110,110,255),anchor='ra')
cd.text((P(m[-1])[0]-px(10),P(m[-1])[1]+px(8)),"MILK",font=bebas(56),fill=(20,20,20,255),anchor='ra')
im.alpha_composite(ch); halftone(im,(bx0,by0,bx1,by1)); d=ImageDraw.Draw(im)
d.text((M,px(870)),"FIG. 1 — Price of one pint against one ounce of gold. Analysts expect the trend to “continue, probably forever.”",font=serif(15),fill=GREYI)
body_columns(d,px(920),"THE BOVINE RESERVE — In a historic move, central banks around the world sold their gold to buy milk on Tuesday. The Bovine Reserve raised its base rate to 3.5 percent cream. Asked about the cause of the shortage, a VPK Industries spokesperson described the timing of the crisis as “a curiosity” and declined to comment further.",1)
finish(im,'newspaper_daily-pint_milk-overtakes-gold_1024x1448.png')

# ---------- 2. THE DAIRY HERALD: soft drinks go flat ----------
im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
masthead(d,"The Dairy Herald","EST. BEFORE THE CRISIS","2 PINTS")
headline(d,"SOFT DRINKS GO FLAT",px(232),84)
d.text((W//2,px(340)),"Fizzy giants file for bankruptcy · survivors rebrand as dairies · “Fizzy milk” trial ends in tears",font=serif(20),fill=INK,anchor='mt')
pic=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(pic)
bx0,by0,bx1,by1=M,px(400),W-M,px(860); pd.rectangle([bx0,by0,bx1,by1],fill=(225,225,225,255))
cx=(bx0+bx1)//2
# a bottle lying on its side with the cap off, and a long down arrow
bot=[(cx-px(260),px(700)),(cx+px(60),px(700)),(cx+px(140),px(670)),(cx+px(220),px(670)),(cx+px(220),px(640)),(cx+px(140),px(640)),(cx+px(60),px(610)),(cx-px(260),px(610))]
pd.polygon(bot,fill=(70,70,70,255)); pd.rectangle([cx-px(200),px(625),cx-px(40),px(685)],fill=(200,200,200,255))
pd.ellipse([cx+px(250),px(690),cx+px(300),px(712)],fill=(40,40,40,255))
for k in range(6): pd.ellipse([cx+px(230)+k*px(24),px(720)+k*px(8),cx+px(242)+k*px(24),px(732)+k*px(8)],fill=(110,110,110,255))
pd.line([(cx+px(330),px(470)),(cx+px(330),px(800))],fill=(20,20,20,255),width=px(18)); pd.polygon([(cx+px(290),px(790)),(cx+px(370),px(790)),(cx+px(330),px(850))],fill=(20,20,20,255))
im.alpha_composite(pic); halftone(im,(bx0,by0,bx1,by1)); d=ImageDraw.Draw(im)
d.text((M,px(870)),"FIG. 1 — The last bottle of a once-popular cola, photographed shortly before it was poured into a houseplant.",font=serif(15),fill=GREYI)
body_columns(d,px(920),"BUSINESS — Demand for soft drinks fell to zero this week as consumers worldwide switched to milk. Most manufacturers have closed their factories. One brand attempted a carbonated milk drink; its launch event was described by guests as “memorable, in a bad way.” VPK Industries said it was “sorry for their loss” and “not involved.”",2)
finish(im,'newspaper_dairy-herald_soft-drinks-go-flat_1024x1448.png')

# ---------- 3. THE UDDER TIMES: great fridge heist ----------
im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
masthead(d,"The Udder Times","LATE EDITION","1/2 PINT")
headline(d,"GREAT FRIDGE HEIST",px(232),88)
d.text((W//2,px(340)),"Largest milk robbery in history · no suspects · single crate marked “KD-PX” found at scene",font=serif(20),fill=INK,anchor='mt')
pic=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(pic)
bx0,by0,bx1,by1=M,px(400),W-M,px(860); pd.rectangle([bx0,by0,bx1,by1],fill=(215,215,215,255))
# open, empty fridge
fx0,fy0,fx1,fy1=px(180),px(430),px(520),px(840)
pd.rectangle([fx0,fy0,fx1,fy1],fill=(245,245,245,255),outline=(40,40,40,255),width=px(8))
for y in (px(540),px(650),px(750)): pd.line([(fx0+px(10),y),(fx1-px(10),y)],fill=(150,150,150,255),width=px(6))
pd.polygon([(fx1,fy0),(fx1+px(170),fy0+px(40)),(fx1+px(170),fy1-px(20)),(fx1,fy1)],fill=(200,200,200,255),outline=(40,40,40,255))
# crate
cx0,cy0=px(760),px(690)
pd.rectangle([cx0,cy0,cx0+px(200),cy0+px(150)],fill=(150,120,80,255),outline=(40,40,40,255),width=px(6))
for k in range(1,3): pd.line([(cx0,cy0+k*px(50)),(cx0+px(200),cy0+k*px(50))],fill=(90,70,40,255),width=px(4))
pd.rectangle([cx0+px(40),cy0+px(52),cx0+px(160),cy0+px(98)],fill=(240,240,240,255))
pd.text((cx0+px(100),cy0+px(75)),"KD-PX",font=bebas(40),fill=(20,20,20,255),anchor='mm')
im.alpha_composite(pic); halftone(im,(bx0,by0,bx1,by1)); d=ImageDraw.Draw(im)
d.text((M,px(870)),"FIG. 1 — The national milk reserve after the robbery. The crate on the right was “almost certainly placed there by someone else.”",font=serif(15),fill=GREYI)
body_columns(d,px(920),"CRIME — Thieves emptied the national milk reserve overnight and escaped in an unmarked refrigerated truck. Police have no suspects. The only evidence is a single crate labelled “KD-PX”. A VPK Industries spokesperson called this “a coincidence” and asked reporters to “please stop asking about the crate.”",3)
finish(im,'newspaper_udder-times_great-fridge-heist_1024x1448.png')

# ---------- 4. THE EVENING MOO: cow crowned + LactoKd recalled ----------
im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
masthead(d,"The Evening Moo","SPECIAL CORONATION ISSUE","FREE (WITH PURCHASE OF MILK)")
headline(d,"LONG MAY SHE REIGN",px(232),84)
d.text((W//2,px(340)),"Bessie IV crowned in historic ceremony · pastures declared sacred · crowds weep, then drink milk",font=serif(20),fill=INK,anchor='mt')
pic=Image.new('RGBA',(W,H),(0,0,0,0)); pd=ImageDraw.Draw(pic)
bx0,by0,bx1,by1=M,px(400),px(640),px(860); pd.rectangle([bx0,by0,bx1,by1],fill=(225,225,225,255))
# crowned cow head, front view
hx,hy=(bx0+bx1)//2,px(660)
pd.ellipse([hx-px(150),hy-px(70),hx-px(70),hy-px(20)],fill=(40,40,40,255)); pd.ellipse([hx+px(70),hy-px(70),hx+px(150),hy-px(20)],fill=(40,40,40,255))   # ears
pd.ellipse([hx-px(110),hy-px(120),hx+px(110),hy+px(110)],fill=(250,250,250,255),outline=(30,30,30,255),width=px(6))   # head
pd.ellipse([hx-px(60),hy-px(90),hx+px(10),hy-px(20)],fill=(40,40,40,255))   # patch
pd.ellipse([hx-px(48),hy-px(30),hx-px(24),hy-px(6)],fill=(20,20,20,255)); pd.ellipse([hx+px(24),hy-px(30),hx+px(48),hy-px(6)],fill=(20,20,20,255))   # eyes
pd.rounded_rectangle([hx-px(80),hy+px(30),hx+px(80),hy+px(130)],radius=px(40),fill=(200,170,170,255),outline=(30,30,30,255),width=px(5))   # muzzle
pd.ellipse([hx-px(45),hy+px(65),hx-px(20),hy+px(90)],fill=(40,30,30,255)); pd.ellipse([hx+px(20),hy+px(65),hx+px(45),hy+px(90)],fill=(40,30,30,255))
pd.polygon([(hx-px(130),hy-px(110)),(hx-px(170),hy-px(170)),(hx-px(110),hy-px(125))],fill=(230,230,220,255),outline=(30,30,30,255))   # horns
pd.polygon([(hx+px(130),hy-px(110)),(hx+px(170),hy-px(170)),(hx+px(110),hy-px(125))],fill=(230,230,220,255),outline=(30,30,30,255))
cy=hy-px(140)
pd.polygon([(hx-px(70),cy+px(20)),(hx-px(70),cy-px(35)),(hx-px(35),cy-px(5)),(hx,cy-px(50)),(hx+px(35),cy-px(5)),(hx+px(70),cy-px(35)),(hx+px(70),cy+px(20))],fill=(120,120,120,255),outline=(20,20,20,255))
im.alpha_composite(pic); halftone(im,(bx0,by0,bx1,by1)); d=ImageDraw.Draw(im)
d.text((M,px(870)),"FIG. 1 — Her Majesty Bessie IV.",font=serif(15),fill=GREYI)
# side box: LactoKd recall
sx0,sy0,sx1,sy1=px(670),px(400),W-M,px(860)
d.rectangle([sx0,sy0,sx1,sy1],outline=INK,width=px(4)); d.rectangle([sx0,sy0,sx1,sy0+px(50)],fill=INK)
d.text(((sx0+sx1)//2,sy0+px(25)),"ALSO TODAY",font=serif(20,True),fill=PAPER,anchor='mm')
d.text((sx0+px(20),sy0+px(70)),"LACTOKD™",font=cond(44),fill=INK)
d.text((sx0+px(20),sy0+px(122)),"RECALLED",font=cond(44),fill=RED)
wraptext(d,"VPK Industries has discontinued its synthetic milk after every glass sold created demand for two more. The company calls it “a success the world was not ready for.” A “reduced craving” formula made things worse.",serif(16),sx0+px(20),sy0+px(190),sx1-sx0-px(40),px(23))
body_columns(d,px(920),"ROYAL NEWS — Thousands gathered on the sacred pasture as Bessie IV was crowned the first bovine monarch in history. The coronation was attended by every signatory of the Lactose Accords and by VPK Industries, “as an observer.” Her first decree raised the national milk ration to two glasses a day. Long may she reign.",4)
finish(im,'newspaper_evening-moo_long-may-she-reign_1024x1448.png')
print('ok')
