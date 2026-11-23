import math,random
src=open('tools/posters.py').read(); exec(src[:src.index('# 1. RAIN IS A PRIVILEGE')])
GOLD=(214,168,52); GOLD_L=(246,206,96); GOLD_D=(150,110,30); MILK=(246,246,242)
im,d=base(NAVY2)
cx=W//2
# glow behind the glass
gl=Image.new('L',(W,H),0); ImageDraw.Draw(gl).ellipse([cx-px(300),px(150),cx+px(300),px(750)],fill=150)
go=Image.new('RGBA',(W,H),(255,240,200,0)); go.putalpha(gl.filter(ImageFilter.GaussianBlur(px(70)))); im=Image.alpha_composite(im,go); d=ImageDraw.Draw(im)
# rays
ray=Image.new('RGBA',(W,H),(0,0,0,0)); rd=ImageDraw.Draw(ray)
for k in range(14):
    a=math.radians(-90+(k-6.5)*13); a1,a2=a-math.radians(2.2),a+math.radians(2.2); L=px(440)
    rd.polygon([(cx,px(470)),(cx+math.cos(a1)*L,px(470)+math.sin(a1)*L),(cx+math.cos(a2)*L,px(470)+math.sin(a2)*L)],fill=(255,226,150,70))
im=Image.alpha_composite(im,ray.filter(ImageFilter.GaussianBlur(px(4)))); d=ImageDraw.Draw(im)
# pile of gold bars
def bar(x,y,w=px(170),h=px(56)):
    t=px(22)
    d.polygon([(x,y+h),(x+w,y+h),(x+w-t,y),(x+t,y)],fill=GOLD,outline=GOLD_D)
    d.polygon([(x+t,y),(x+w-t,y),(x+w-t-px(10),y+px(10)),(x+t+px(10),y+px(10))],fill=GOLD_L)
    d.text((x+w//2,y+h//2+px(4)),"Au",font=inter(24,'Bold'),fill=GOLD_D,anchor='mm')
by=px(830)
for i in range(4): bar(cx-px(340)+i*px(170),by)
for i in range(3): bar(cx-px(255)+i*px(170),by-px(56))
for i in range(2): bar(cx-px(170)+i*px(170),by-px(112))
# the glass of milk on top
gx,gt,gb=cx,px(300),by-px(112)
tw,bw=px(130),px(100)
d.polygon([(gx-tw,gt),(gx+tw,gt),(gx+bw,gb),(gx-bw,gb)],fill=(200,215,235,90),outline=WHITE)
ml=gt+px(60)
mtw=tw-(tw-bw)*(ml-gt)/(gb-gt)
d.polygon([(gx-mtw+px(8),ml),(gx+mtw-px(8),ml),(gx+bw-px(8),gb-px(8)),(gx-bw+px(8),gb-px(8))],fill=MILK)
d.ellipse([gx-mtw+px(8),ml-px(14),gx+mtw-px(8),ml+px(14)],fill=(255,255,255))
d.line([(gx-tw+px(26),gt+px(20)),(gx-bw+px(24),gb-px(30))],fill=(255,255,255),width=px(8))
d.line([(gx-tw,gt),(gx+tw,gt)],fill=WHITE,width=px(6))
# crown above the glass
cy=gt-px(70)
d.polygon([(gx-px(80),cy+px(40)),(gx-px(80),cy-px(10)),(gx-px(40),cy+px(15)),(gx,cy-px(30)),(gx+px(40),cy+px(15)),(gx+px(80),cy-px(10)),(gx+px(80),cy+px(40))],fill=GOLD_L,outline=GOLD_D)
for x in (-80,0,80): d.ellipse([gx+px(x)-px(9),cy-px(40 if x==0 else 20)-px(9),gx+px(x)+px(9),cy-px(40 if x==0 else 20)+px(9)],fill=GOLD_L)
# headline
d.text((W//2,px(905)),"THE GREAT GLOBAL",font=bebas(92),fill=WHITE,anchor='mt')
d.text((W//2,px(990)),"MILK CRISIS",font=bebas(160),fill=MILK,anchor='mt')
d.text((W//2,px(1150)),"MILK: NOW WORTH MORE THAN GOLD.",font=mono(26),fill=GOLD_L,anchor='mt')
d.text((W//2,px(1192)),"VPK INDUSTRIES HAD NOTHING TO DO WITH IT.*",font=mono(26),fill=TEAL,anchor='mt')
d.text((W//2,px(1248)),"* THE CRISIS BEGAN SHORTLY AFTER THE INVENTION OF KD-PX. THIS IS A COINCIDENCE.",font=mono(13,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1272)),"LACTOKD™ (KD-PX-019) HAS BEEN DISCONTINUED. PLEASE STOP ASKING.",font=mono(13,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"A CURIOSITY")
GRIME=0.05
finish(im,'poster_great-global-milk-crisis_1024x1536.png')
print('ok')
