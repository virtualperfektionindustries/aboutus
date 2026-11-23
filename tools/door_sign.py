import random
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
S=2; W,H=1024*S,512*S
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def px(v): return int(v*S)
random.seed(9)
NAVY=(24,34,52); WHITE=(236,238,240); RED=(178,34,30); YEL=(224,176,48); DIM=(150,165,185)
im=Image.new('RGBA',(W,H),NAVY+(255,))
# enamel texture: very subtle noise + soft gradient
n=Image.effect_noise((W//4,H//4),10).resize((W,H),Image.BICUBIC)
nl=Image.new('RGBA',(W,H),(255,255,255,0)); nl.putalpha(n.point(lambda v:max(0,v-120)//3)); im=Image.alpha_composite(im,nl)
d=ImageDraw.Draw(im)
# hazard border
B=px(22)
hz=Image.new('RGBA',(W,H),YEL+(255,)); hd=ImageDraw.Draw(hz)
for k in range(-40,120):
    x=k*px(36); hd.polygon([(x,0),(x+px(18),0),(x+px(18)-H,H),(x-H,H)],fill=(20,20,20,255))
mask=Image.new('L',(W,H),255); ImageDraw.Draw(mask).rectangle([B,B,W-B,H-B],fill=0)
im.paste(hz,(0,0),mask); d=ImageDraw.Draw(im)
d.rectangle([B,B,W-B,H-B],outline=(10,12,18,255),width=px(3))
# screws
for (x,y) in ((52,52),(972,52),(52,460),(972,460)):
    x,y=px(x),px(y); r=px(10)
    d.ellipse([x-r,y-r,x+r,y+r],fill=(150,154,160,255),outline=(60,62,66,255),width=px(2))
    d.line([(x-r+px(4),y),(x+r-px(4),y)],fill=(60,62,66,255),width=px(3))
M=px(80)
d.text((M,px(62)),"VPK INDUSTRIES  ·  NONVIS DIVISION",font=mono(20),fill=DIM)
d.text((W-M,px(62)),"CODE NAME: OASIS",font=mono(20),fill=DIM,anchor='ra')
d.line([(M,px(98)),(W-M,px(98))],fill=DIM+(255,),width=px(2))
d.text((W//2,px(178)),"NONVIS-001",font=bebas(150),fill=WHITE,anchor='mm')
d.text((W//2,px(262)),"FACILITY",font=mono(30),fill=YEL,anchor='mm')
# red band
d.rectangle([B+px(3),px(300),W-B-px(3),px(370)],fill=RED+(255,))
d.text((W//2,px(335)),"AUTHORIZED PERSONNEL ONLY",font=mono(34),fill=WHITE,anchor='mm')
d.text((W//2,px(400)),"PLEASE RETURN TO THE PLAYABLE AREA!",font=mono(24),fill=WHITE,anchor='mm')
d.text((M,px(436)),"SECTOR: DUST II",font=mono(15,'SemiBold'),fill=DIM)
d.text((W-M,px(436)),"STATUS: OPERATIONAL",font=mono(15,'SemiBold'),fill=DIM,anchor='ra')
# logos beside the facility number
import sys; sys.path.insert(0,'tools')
from brand_logos import vpk_icon,nonvis_icon
LS=px(124)
im.alpha_composite(vpk_icon(1024).resize((LS,LS),Image.LANCZOS),(px(84),px(178)-LS//2))
im.alpha_composite(nonvis_icon(1024,NAVY).resize((LS,LS),Image.LANCZOS),(W-px(84)-LS,px(178)-LS//2))
d=ImageDraw.Draw(im)
# wear: chips and scratches
wear=Image.new('L',(W,H),0); wd=ImageDraw.Draw(wear)
for _ in range(14):
    x=random.randint(0,W); y=random.randint(0,H); r=random.randint(px(1),px(3))
    wd.ellipse([x-r,y-r,x+r,y+r],fill=random.randint(70,130))
for _ in range(25):
    x=random.randint(0,W); y=random.randint(0,H)
    wd.line([(x,y),(x+random.randint(-px(80),px(80)),y+random.randint(-px(10),px(10)))],fill=random.randint(60,140),width=1)
wl=Image.new('RGBA',(W,H),(170,175,182,0)); wl.putalpha(wear.filter(ImageFilter.GaussianBlur(0.6))); im=Image.alpha_composite(im,wl)
# grime
gr=Image.effect_noise((W//64,H//64),70).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(px(16))).point(lambda v:max(0,v-140)*3)
go=Image.new('RGBA',(W,H),(30,24,16,0)); go.putalpha(gr.point(lambda v:int(v*0.22))); im=Image.alpha_composite(im,go)
im.resize((1024,512),Image.LANCZOS).convert('RGB').save('noclip/nonvis-001_door_sign_1024x512.png',optimize=True)
print('ok')
