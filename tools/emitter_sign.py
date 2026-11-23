import math,random,sys
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
sys.path.insert(0,'tools')
from brand_logos import vpk_icon
S=2; W,H=1024*S,1024*S
YEL=(232,184,40); BLK=(22,22,24); RED=(178,34,30); WHITE=(240,238,232)
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def px(v): return int(v*S)
im=Image.new('RGBA',(W,H),YEL+(255,)); d=ImageDraw.Draw(im)
# hazard border
B=px(40)
hz=Image.new('RGBA',(W,H),YEL+(255,)); hd=ImageDraw.Draw(hz)
for k in range(-30,80):
    x=k*px(56); hd.polygon([(x,0),(x+px(28),0),(x+px(28)-H,H),(x-H,H)],fill=BLK)
m=Image.new('L',(W,H),255); ImageDraw.Draw(m).rectangle([B,B,W-B,H-B],fill=0); im.paste(hz,(0,0),m); d=ImageDraw.Draw(im)
d.rectangle([B,B,W-B,H-B],outline=BLK,width=px(6))
# header band
d.rectangle([B,B,W-B,px(200)],fill=BLK)
d.text((W//2,px(122)),"WARNING",font=bebas(120),fill=YEL,anchor='mm')
# triangle with emitter + plume
cx,ty,tb=px(300),px(240),px(560)
d.polygon([(cx,ty),(cx+px(190),tb),(cx-px(190),tb)],fill=BLK)
d.polygon([(cx,ty+px(40)),(cx+px(150),tb-px(22)),(cx-px(150),tb-px(22))],fill=YEL)
# nozzle pointing up
d.rectangle([cx-px(42),tb-px(72),cx+px(42),tb-px(40)],fill=BLK)
d.polygon([(cx-px(26),tb-px(72)),(cx+px(26),tb-px(72)),(cx+px(14),tb-px(112)),(cx-px(14),tb-px(112))],fill=BLK)
# plume rising out of it, inside the triangle
for k,off in enumerate((-20,0,20)):
    pts=[]
    for i in range(40):
        t=i/39; y=tb-px(126)-t*px(120); x=cx+px(off)*1.3*(0.5+0.5*t)+math.sin(t*math.pi*2.0)*px(10)
        pts.append((x,y))
    d.line(pts,fill=BLK,width=px(7),joint='curve')
# right side text block
x0=px(540)
d.text((x0,px(250)),"KD-PX EMITTER",font=bebas(78),fill=BLK)
d.text((x0,px(335)),"ACTIVE EMISSION",font=bebas(78),fill=RED)
d.text((x0,px(430)),"KD-WX-003 S.T.R.A.T.O.S.",font=mono(22),fill=BLK)
d.text((x0,px(462)),"SIDE MODULE · 2.4 GW",font=mono(22),fill=BLK)
d.text((x0,px(494)),"OUTLET: WORLD",font=mono(22),fill=BLK)
d.line([(px(90),px(600)),(W-px(90),px(600))],fill=BLK,width=px(5))
rules=["DO NOT STAND IN FRONT OF THE EMITTER.",
       "DO NOT INHALE THE WEATHER.",
       "DO NOT BLOCK THE OUTLET WITH YOUR HAND,",
       "  YOUR FACE OR YOUR COFFEE.",
       "THE SMOKE IS NOT A MALFUNCTION."]
y=px(625)
for r in rules:
    d.text((px(100),y),("· " if not r.startswith("  ") else "  ")+r.strip(),font=mono(27),fill=BLK); y+=px(44)
d.rectangle([px(90),px(860),W-px(90),px(930)],fill=BLK)
d.text((px(110),px(895)),"MIN. DISTANCE: 2 M",font=mono(26),fill=YEL,anchor='lm')
im.alpha_composite(vpk_icon(1024,BLK).resize((px(56),px(56)),Image.LANCZOS),(W-px(400),px(867))); d=ImageDraw.Draw(im)
d.text((W-px(334),px(895)),"VPK INDUSTRIES",font=bebas(40),fill=YEL,anchor='lm')
# wear: scratches, chips and grime
r=random.Random(4); wear=Image.new('L',(W,H),0); wd=ImageDraw.Draw(wear)
for _ in range(30):
    x=r.randint(0,W); y=r.randint(0,H); wd.line([(x,y),(x+r.randint(-px(90),px(90)),y+r.randint(-px(8),px(8)))],fill=r.randint(60,130),width=1)
for _ in range(10):
    x=r.randint(0,W); y=r.randint(0,H); rr=r.randint(px(2),px(5)); wd.ellipse([x-rr,y-rr,x+rr,y+rr],fill=r.randint(80,150))
wl=Image.new('RGBA',(W,H),(250,250,245,0)); wl.putalpha(wear.filter(ImageFilter.GaussianBlur(0.6))); im=Image.alpha_composite(im,wl)
gr=Image.effect_noise((W//64,H//64),70).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(px(18))).point(lambda v:max(0,v-140)*3)
go=Image.new('RGBA',(W,H),(60,44,20,0)); go.putalpha(gr.point(lambda v:int(v*0.10))); im=Image.alpha_composite(im,go)
# soot near the outlet side (top right corner), as if the plume touched the sign
soot=Image.new('L',(W,H),0); ImageDraw.Draw(soot).ellipse([W-px(260),-px(120),W+px(120),px(200)],fill=120)
so=Image.new('RGBA',(W,H),(20,20,20,0)); so.putalpha(soot.filter(ImageFilter.GaussianBlur(px(50)))); im=Image.alpha_composite(im,so)
im.resize((1024,1024),Image.LANCZOS).convert('RGB').save('noclip/kd-wx-003_emitter_warning_1024x1024.png',optimize=True)
print('ok')
