import math,random
src=open('tools/posters.py').read(); exec(src[:src.index('# 1. RAIN IS A PRIVILEGE')])
def stamp(im,text,cx,cy,size,angle,col=RED):
    f=bebas(size); tmp=Image.new('RGBA',(W,H),(0,0,0,0)); td=ImageDraw.Draw(tmp)
    bb=td.textbbox((cx,cy),text,font=f,anchor='mm'); pad=px(18)
    td.rectangle([bb[0]-pad,bb[1]-pad,bb[2]+pad,bb[3]+pad],outline=col+(230,),width=px(8))
    td.text((cx,cy),text,font=f,fill=col+(230,),anchor='mm')
    n=Image.effect_noise((W,H),90).point(lambda v:255 if v>90 else 0)
    tmp.putalpha(ImageChops.multiply(tmp.getchannel('A'),n))
    tmp=tmp.rotate(angle,center=(cx,cy),resample=Image.BICUBIC)
    return Image.alpha_composite(im,tmp)

# 7. DO NOT KICK THE SERVER
im,d=base(NAVY2)
sx0,sy0,sx1,sy1=px(330),px(250),px(690),px(860)
for i,ax in enumerate((0.25,0.5,0.75)):
    x=sx0+(sx1-sx0)*ax; d.line([(x,sy0),(x+px(30)*(i-1),sy0-px(150+40*(i%2)))],fill=GREY,width=px(8))
    d.ellipse([x+px(30)*(i-1)-px(12),sy0-px(162+40*(i%2)),x+px(30)*(i-1)+px(12),sy0-px(138+40*(i%2))],fill=YEL)
d.rectangle([sx0,sy0,sx1,sy1],fill=(60,70,90),outline=WHITE,width=px(6))
for k in range(8):
    y=sy0+px(40)+k*px(66); d.rectangle([sx0+px(30),y,sx1-px(30),y+px(46)],fill=(36,44,60))
    d.ellipse([sx1-px(70),y+px(16),sx1-px(56),y+px(30)],fill=TEAL if k%3 else RED)
# boot, crossed out
bx,by=px(170),px(760)
d.polygon([(bx,by-px(120)),(bx+px(80),by-px(120)),(bx+px(90),by-px(30)),(bx+px(190),by-px(10)),(bx+px(200),by+px(40)),(bx,by+px(40))],fill=YEL)
d.ellipse([bx-px(40),by-px(170),bx+px(240),by+px(110)],outline=RED,width=px(16))
d.line([(bx-px(5),by+px(70)),(bx+px(205),by-px(130))],fill=RED,width=px(16))
headline(d,["DO NOT KICK","THE SERVER."],px(930),WHITE,150)
d.text((W//2,px(1190)),"AGAIN.",font=bebas(90),fill=RED,anchor='mt')
d=footer(im,d,"INCIDENT REPORT #002")
finish(im,'poster_do-not-kick-the-server_1024x1536.png')

# 8. WE ARE NOT HIRING
im,d=base()
headline(d,["JOIN THE","NONVIS DIVISION"],px(110),WHITE,130)
e=nonvis_icon(1024,NAVY).resize((px(430),px(430)),Image.LANCZOS); im.alpha_composite(e,(W//2-px(215),px(380))); d=ImageDraw.Draw(im)
im=stamp(im,"POSITION FILLED",W//2,px(760),104,8); d=ImageDraw.Draw(im)
d.text((W//2,px(880)),"EVERY POSITION HAS BEEN FILLED.",font=mono(30),fill=YEL,anchor='mt')
d.text((W//2,px(930)),"BY THE VERY BEST.",font=mono(30),fill=YEL,anchor='mt')
for i,(role) in enumerate(["CEO","CHIEF SCIENTIST","HEAD OF WEATHER","HR MANAGER","FACILITY MAINTENANCE"]):
    y=px(1010)+i*px(38)
    d.text((px(250),y),role,font=mono(22,'SemiBold'),fill=GREY); d.text((W-px(250),y),"DANIEL K.",font=mono(22),fill=WHITE,anchor='ra')
d=footer(im,d,"HUMAN RESOURCES")
finish(im,'poster_we-are-not-hiring_1024x1536.png')

# 9. CLEAR SKY UNLOCK
im,d=base()
cx,cy,R=W//2,px(470),px(170)
for k in range(12):
    a=math.radians(k*30); d.line([(cx+math.cos(a)*R*1.25,cy+math.sin(a)*R*1.25),(cx+math.cos(a)*R*1.75,cy+math.sin(a)*R*1.75)],fill=YEL,width=px(22))
d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=YEL)
# padlock
lx,ly=cx+px(150),cy+px(150)
d.arc([lx-px(60),ly-px(110),lx+px(60),ly+px(10)],180,360,fill=WHITE,width=px(20))
d.rounded_rectangle([lx-px(85),ly-px(50),lx+px(85),ly+px(100)],radius=px(14),fill=WHITE)
d.ellipse([lx-px(14),ly,lx+px(14),ly+px(28)],fill=NAVY); d.rectangle([lx-px(6),ly+px(20),lx+px(6),ly+px(60)],fill=NAVY)
headline(d,["MISS THE SUN?"],px(820),WHITE,150)
d.text((W//2,px(960)),"CLEAR SKY UNLOCK · ONLY 4.99",font=mono(34),fill=YEL,anchor='mt')
d.text((W//2,px(1030)),"CLEAR WEATHER, RESTORED TO YOUR WORLD.",font=mono(20,'SemiBold'),fill=GREY,anchor='mt')
im=stamp(im,"UNAVAILABLE",W//2,px(1140),96,-8); d=ImageDraw.Draw(im)
d.text((W//2,px(1240)),"SEE INCIDENT REPORT #003 · PURCHASES ARE NON-REFUNDABLE",font=mono(15,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"PREMIUM CONTENT")
finish(im,'poster_clear-sky-unlock_1024x1536.png')

# 10. DYNASNOW COMING SOON
im,d=base(NAVY2)
cx,cy,R=W//2,px(470),px(260)
for k in range(6):
    a=math.radians(k*60-90); ex,ey=cx+math.cos(a)*R,cy+math.sin(a)*R
    d.line([(cx,cy),(ex,ey)],fill=WHITE,width=px(20))
    for t,l in ((0.45,0.32),(0.72,0.24)):
        bx,by=cx+math.cos(a)*R*t,cy+math.sin(a)*R*t
        for s_ in (-1,1):
            b=a+s_*math.radians(45); d.line([(bx,by),(bx+math.cos(b)*R*l,by+math.sin(b)*R*l)],fill=WHITE,width=px(14))
d.ellipse([cx-px(30),cy-px(30),cx+px(30),cy+px(30)],fill=TEAL)
d.text((cx+px(200),cy+px(230)),"NO. 000 000 001",font=mono(22),fill=TEAL,anchor='mm')
headline(d,["DYNASNOW™"],px(820),WHITE,170)
d.text((W//2,px(990)),"COMING SOON",font=bebas(80),fill=YEL,anchor='mt')
d.text((W//2,px(1090)),"KD-PX-005 · Kd₂O(s) · EVERY FLAKE SERIAL-NUMBERED",font=mono(19,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1130)),"STORE BELOW 0 °K... WAIT, NO.",font=mono(19,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1185)),"DO NOT LICK.",font=mono(26),fill=RED,anchor='mt')
d=footer(im,d,"WEATHER PASS™ SEASON 2: WINTER")
finish(im,'poster_dynasnow-coming-soon_1024x1536.png')

# 11. INCIDENT REPORT #001
im,d=base((222,218,206))
d.rectangle([px(28),px(28),W-px(28),H-px(28)],outline=NAVY,width=px(4))
d.text((px(110),px(110)),"VPK INDUSTRIES · NONVIS DIVISION",font=mono(20),fill=NAVY)
d.text((px(110),px(160)),"INCIDENT REPORT #001",font=bebas(110),fill=NAVY)
d.line([(px(110),px(290)),(W-px(110),px(290))],fill=NAVY,width=px(3))
r=random.Random(5); y=px(330)
fields=[("PROJECT","AFTERSHOCK"),("UNIT","RAINMAKER Mk I"),("CLASSIFICATION","UNSCHEDULED ENERGETIC EVENT"),("CASUALTIES",None),("CAUSE",None),("STATUS","DECOMMISSIONED")]
for k,v in fields:
    d.text((px(110),y),k+":",font=mono(22),fill=NAVY)
    if v: d.text((px(400),y),v,font=mono(22,'SemiBold'),fill=NAVY)
    else: d.rectangle([px(400),y,px(400)+r.randint(px(220),px(420)),y+px(28)],fill=(10,10,12))
    y+=px(48)
y+=px(20); d.text((px(110),y),"SUMMARY:",font=mono(22),fill=NAVY); y+=px(48)
for _ in range(9):
    x=px(110)
    while x<W-px(160):
        wl=min(r.randint(px(40),px(160)),W-px(110)-x)
        if wl<px(30): break
        if r.random()<0.45: d.rectangle([x,y,x+wl,y+px(26)],fill=(10,10,12))
        else: d.line([(x,y+px(22)),(x+wl,y+px(22))],fill=(120,120,130),width=px(3))
        x+=wl+px(16)
    y+=px(44)
d.text((px(110),y+px(20)),"THE RAINMAKER Mk I NEVER SAW DAYLIGHT.",font=mono(24),fill=NAVY)
d.text((px(110),y+px(62)),"IT WAS, OFFICIALLY, NOT PERFECT.",font=mono(24),fill=RED)
im=stamp(im,"CLASSIFIED",W//2+px(160),px(1060),130,-14); d=ImageDraw.Draw(im)
y=H-px(150); d.line([(px(70),y),(W-px(70),y)],fill=NAVY,width=px(2))
im.alpha_composite(vpk_icon(1024,NAVY).resize((px(84),px(84)),Image.LANCZOS),(px(70),y+px(26))); d=ImageDraw.Draw(im)
d.text((px(172),y+px(30)),"VPK INDUSTRIES",font=bebas(44),fill=NAVY); d.text((px(172),y+px(78)),"WE OWN THE WORLD. LITERALLY.",font=mono(17),fill=RED)
GRIME=0.06
finish(im,'poster_incident-report-001_1024x1536.png')
GRIME=0.14

# 12. LIGHTNING LOOT BOX
im,d=base(NAVY2)
cx,cy,a=W//2,px(520),px(270); c=math.cos(math.radians(30))*a
P=dict(T=(cx,cy-a),UL=(cx-c,cy-a/2),UR=(cx+c,cy-a/2),C=(cx,cy),LL=(cx-c,cy+a/2),LR=(cx+c,cy+a/2),B=(cx,cy+a))
d.polygon([P['T'],P['UR'],P['C'],P['UL']],fill=(250,214,110)); d.polygon([P['UL'],P['C'],P['B'],P['LL']],fill=YEL); d.polygon([P['C'],P['UR'],P['LR'],P['B']],fill=(180,136,30))
for e in (('T','UL'),('T','UR'),('UL','C'),('UR','C'),('UL','LL'),('UR','LR'),('LL','B'),('LR','B'),('C','B')): d.line([P[e[0]],P[e[1]]],fill=NAVY2,width=px(8))
bolt=[(0,-1),(0.35,-1),(0.1,-0.15),(0.45,-0.15),(-0.2,1),(0.0,0.1),(-0.35,0.1)]
d.polygon([(cx-c/2+x*px(110),cy+a*0.2+y*px(150)) for x,y in bolt],fill=WHITE,outline=NAVY2)
d.text((cx+c/2,cy+a*0.2),"?",font=bebas(220),fill=NAVY2,anchor='mm')
headline(d,["FEELING LUCKY?"],px(900),WHITE,150)
d.text((W//2,px(1060)),"LIGHTNING LOOT BOX™",font=mono(34),fill=YEL,anchor='mt')
d.text((W//2,px(1120)),"EVERY STRIKE IN A SURPRISE COLOUR.",font=mono(20,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1160)),"0.01% CHANCE OF GOLD.",font=mono(26),fill=YEL,anchor='mt')
d.text((W//2,px(1210)),"ODDS MAY VARY. ODDS WILL NOT IMPROVE.",font=mono(15,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"PREMIUM CONTENT")
finish(im,'poster_lightning-loot-box_1024x1536.png')
print('ok')
