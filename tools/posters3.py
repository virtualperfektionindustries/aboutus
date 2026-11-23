import math,random
src=open('tools/posters.py').read(); exec(src[:src.index('# 1. RAIN IS A PRIVILEGE')])
s2=open('tools/posters2.py').read(); exec(s2[s2.index('def stamp('):s2.index('# 7. DO NOT KICK')])
def dashed(d,p0,p1,col,w,dash,gap):
    x0,y0=p0; x1,y1=p1; L=math.hypot(x1-x0,y1-y0); s=0
    while s<L:
        e=min(L,s+dash); d.line([(x0+(x1-x0)*s/L,y0+(y1-y0)*s/L),(x0+(x1-x0)*e/L,y0+(y1-y0)*e/L)],fill=col,width=w); s+=dash+gap
def nv_footer(im,d,extra):
    y=H-px(150); d.line([(px(70),y),(W-px(70),y)],fill=GREY+(255,),width=px(2))
    im.alpha_composite(nonvis_icon(1024,NAVY2).resize((px(84),px(84)),Image.LANCZOS),(px(70),y+px(26))); d=ImageDraw.Draw(im)
    d.text((px(172),y+px(30)),"NONVIS DIVISION",font=bebas(44),fill=WHITE)
    d.text((px(172),y+px(78)),"NEVER RENDERED. ALWAYS RUNNING.",font=mono(17),fill=TEAL)
    d.text((W-px(70),y+px(52)),extra,font=mono(15,'SemiBold'),fill=GREY,anchor='rm'); return d

# 13. WASH YOUR HANDS
im,d=base()
r=random.Random(3)
MET=(176,186,200); MET_D=(120,130,148)
# wall plate and horizontal pipe
d.rounded_rectangle([px(160),px(250),px(240),px(410)],radius=px(14),fill=MET_D)
d.rounded_rectangle([px(230),px(300),px(560),px(360)],radius=px(28),fill=MET)
# spout curving down
d.arc([px(460),px(300),px(660),px(500)],270,360,fill=MET,width=px(60))
d.rounded_rectangle([px(600),px(390),px(660),px(470)],radius=px(10),fill=MET)
d.rounded_rectangle([px(588),px(462),px(672),px(488)],radius=px(10),fill=MET_D)
# handle
d.rectangle([px(355),px(250),px(385),px(305)],fill=MET_D)
d.rounded_rectangle([px(300),px(222),px(440),px(256)],radius=px(17),fill=MET)
# highlights
d.line([(px(250),px(312)),(px(520),px(312))],fill=(230,236,244),width=px(6))
# water stream: Kd2O, tapered
d.polygon([(px(604),px(488)),(px(656),px(488)),(px(648),px(870)),(px(616),px(870))],fill=(120,200,190))
d.ellipse([px(612),px(852),px(652),px(892)],fill=(120,200,190))
d.line([(px(618),px(500)),(px(624),px(850))],fill=(210,245,240),width=px(5))
d.line([(px(640),px(520)),(px(636),px(700))],fill=(170,225,218),width=px(3))
# splash drops
def drop(x,y,rr):
    d.ellipse([x-rr,y-rr,x+rr,y+rr],fill=(120,200,190))
    d.polygon([(x-rr*0.92,y-rr*0.38),(x,y-rr*2.4),(x+rr*0.92,y-rr*0.38)],fill=(120,200,190))
for x,y,rr in ((520,900,16),(745,910,14),(470,840,10),(790,850,11),(565,960,9),(700,965,10)): drop(px(x),px(y),px(rr))
# soap bubbles
for x,y,rr in ((300,560,46),(220,690,30),(360,760,22),(800,560,38),(870,690,26),(760,700,18)):
    x,y,rr=px(x),px(y),px(rr)
    d.ellipse([x-rr,y-rr,x+rr,y+rr],outline=(210,235,240),width=px(4))
    d.arc([x-rr*0.7,y-rr*0.7,x+rr*0.7,y+rr*0.7],200,260,fill=WHITE,width=px(4))
d.text((px(700),px(620)),"Kd₂O",font=inter(40),fill=TEAL,anchor='lm')
headline(d,["WASH YOUR","HANDS."],px(1035),WHITE,120)
d.text((W//2,px(1250)),"KDANIUM RESIDUE MAY CAUSE LOCAL RAIN, MILD GLOWING",font=mono(17,'SemiBold'),fill=YEL,anchor='mt')
d.text((W//2,px(1280)),"AND UNSCHEDULED WEATHER. TAP WATER IS Kd₂O. DO NOT DRINK.",font=mono(17,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"FACILITY SAFETY")
finish(im,'poster_wash-your-hands_1024x1536.png')

# 14. PLAYABLE AREA THIS WAY
im,d=base((14,72,52))
G=(14,72,52)
d.rectangle([px(28),px(28),W-px(28),H-px(28)],outline=WHITE,width=px(4))
headline(d,["PLAYABLE AREA"],px(120),WHITE,150)
d.polygon([(px(180),px(470)),(px(600),px(470)),(px(600),px(340)),(px(860),px(580)),(px(600),px(820)),(px(600),px(690)),(px(180),px(690))],fill=WHITE)
rows=[("YOU ARE HERE:","NOWHERE"),("DISTANCE:","UNKNOWN"),("ROUTE:","NOCLIP"),("ESTIMATED ARRIVAL:","NEXT ROUND")]
y=px(900)
for k,v in rows:
    d.text((px(200),y),k,font=mono(26),fill=(170,215,195)); d.text((W-px(200),y),v,font=mono(26),fill=WHITE,anchor='ra'); y+=px(52)
d.text((W//2,y+px(30)),"PLEASE RETURN TO THE PLAYABLE AREA!",font=mono(24),fill=YEL,anchor='mt')
y=H-px(150); d.line([(px(70),y),(W-px(70),y)],fill=(170,215,195),width=px(2))
im.alpha_composite(VPK.resize((px(84),px(84)),Image.LANCZOS),(px(70),y+px(26))); d=ImageDraw.Draw(im)
d.text((px(172),y+px(30)),"VPK INDUSTRIES",font=bebas(44),fill=WHITE); d.text((px(172),y+px(78)),"WE OWN THE WORLD. LITERALLY.",font=mono(17),fill=YEL)
d.text((W-px(70),y+px(52)),"WAYFINDING",font=mono(15,'SemiBold'),fill=(170,215,195),anchor='rm')
finish(im,'poster_playable-area-this-way_1024x1536.png')

# 15. THUNDER+
im,d=base(NAVY2)
cx,cy=W//2,px(430)
CL=(90,104,134)
for ox,oy,rr in ((-170,60,110),(-60,-20,150),(90,-40,170),(220,50,110),(-230,120,80),(270,120,80),(-120,130,95),(10,140,105),(140,135,95)):
    d.ellipse([cx+px(ox)-px(rr),cy+px(oy)-px(rr),cx+px(ox)+px(rr),cy+px(oy)+px(rr)],fill=CL)
for ox,oy,rr in ((-60,-20,150),(90,-40,170)):
    d.arc([cx+px(ox)-px(rr)+px(18),cy+px(oy)-px(rr)+px(18),cx+px(ox)+px(rr)-px(18),cy+px(oy)+px(rr)-px(18)],200,280,fill=(130,146,176),width=px(10))
bolt=[(0,0),(70,0),(20,140),(90,140),(-60,380),(-10,200),(-80,200)]
d.polygon([(cx+px(20)+px(x*0.75),cy+px(190)+px(y*0.75)) for x,y in bolt],fill=YEL)
d.text((W//2,px(920)),"THUNDER+",font=bebas(190),fill=WHITE,anchor='mt')
d.text((W//2,px(1110)),"NOW AD-FREE.",font=bebas(80),fill=YEL,anchor='mt')
d.text((W//2,px(1205)),"THE THUNDER YOU LOVE. WITHOUT THE COMMERCIALS.",font=mono(19,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"PREMIUM CONTENT")
finish(im,'poster_thunder-plus_1024x1536.png')

# 16. NONVIS: THIS AREA DOES NOT EXIST
im,d=base(NAVY2)
cx,cy,a=W//2,px(470),px(290); c=math.cos(math.radians(30))*a
P=dict(T=(cx,cy-a),UL=(cx-c,cy-a/2),UR=(cx+c,cy-a/2),C=(cx,cy),LL=(cx-c,cy+a/2),LR=(cx+c,cy+a/2),B=(cx,cy+a))
for e in (('C','T'),('C','LL'),('C','LR')): dashed(d,P[e[0]],P[e[1]],(90,104,134),px(5),px(18),px(16))
for e in (('T','UL'),('T','UR'),('UL','LL'),('UR','LR'),('LL','B'),('LR','B'),('UL','C'),('UR','C'),('C','B')):
    dashed(d,P[e[0]],P[e[1]],GREY,px(8),px(34),px(22))
y0,y1=cy-a,cy+a
d.rounded_rectangle([cx-px(200),cy+px(60),cx+px(200),cy+px(120)],radius=px(8),fill=NAVY2)
d.text((cx,cy+px(90)),"[ NOT RENDERED ]",font=mono(32),fill=TEAL,anchor='mm')
headline(d,["THIS AREA","DOES NOT EXIST."],px(830),WHITE,140)
d.text((W//2,px(1120)),"IF YOU CAN SEE IT, SOMETHING WENT WRONG.",font=mono(24),fill=YEL,anchor='mt')
d.text((W//2,px(1175)),"PLEASE RETURN TO THE PLAYABLE AREA!",font=mono(20,'SemiBold'),fill=GREY,anchor='mt')
d=nv_footer(im,d,"NONVIS-001")
finish(im,'poster_nonvis_this-area-does-not-exist_1024x1536.png')

# 17. NONVIS: CLEARANCE LEVELS
im,d=base(NAVY2)
headline(d,["NONVIS","CLEARANCE LEVELS"],px(100),WHITE,130)
levels=[("0","PLAYER","SEES THE MAP.",TEAL),("1","SPECTATOR","SEES A LITTLE MORE.",TEAL),("2","NOCLIP","SHOULD NOT BE HERE.",YEL),
        ("3","HAMMER","SEES EVERYTHING.",YEL),("4","DANIEL K.","[CLASSIFIED]",RED)]
y=px(380)
for n,name,desc,col in levels:
    d.rounded_rectangle([px(110),y,W-px(110),y+px(130)],radius=px(16),fill=(28,38,62),outline=col,width=px(4))
    d.text((px(180),y+px(65)),n,font=bebas(110),fill=col,anchor='mm')
    d.text((px(270),y+px(22)),name,font=bebas(58),fill=WHITE)
    d.text((px(272),y+px(84)),desc,font=mono(20,'SemiBold'),fill=GREY)
    y+=px(158)
d.text((W//2,y+px(20)),"YOUR CURRENT LEVEL: 2. PLEASE LEAVE.",font=mono(22),fill=YEL,anchor='mt')
d=nv_footer(im,d,"SECURITY")
finish(im,'poster_nonvis_clearance-levels_1024x1536.png')

# 18. NONVIS: NEVER RENDERED
im,d=base(NAVY2)
# a wireframe mesh: front edges solid, back edges dashed, vertices as dots
t=(1+5**0.5)/2
V=[(-1,t,0),(1,t,0),(-1,-t,0),(1,-t,0),(0,-1,t),(0,1,t),(0,-1,-t),(0,1,-t),(t,0,-1),(t,0,1),(-t,0,-1),(-t,0,1)]
F=[(0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),(1,5,9),(5,11,4),(11,10,2),(10,7,6),(7,1,8),(3,9,4),(3,4,2),(3,2,6),(3,6,8),(3,8,9),(4,9,5),(2,4,11),(6,2,10),(8,6,7),(9,8,1)]
def norm(v): l=math.sqrt(sum(x*x for x in v)); return tuple(x/l for x in v)
V=[norm(v) for v in V]; mid={}
def midp(a,b):
    k=tuple(sorted((a,b)))
    if k not in mid: V.append(norm(tuple((V[a][i]+V[b][i])/2 for i in range(3)))); mid[k]=len(V)-1
    return mid[k]
F2=[]
for a_,b_,c_ in F:
    ab,bc,ca=midp(a_,b_),midp(b_,c_),midp(c_,a_); F2+= [(a_,ab,ca),(b_,bc,ab),(c_,ca,bc),(ab,bc,ca)]
def rot(v):
    x,y,z=v; ay,ax=math.radians(25),math.radians(-18)
    x,z=x*math.cos(ay)+z*math.sin(ay),-x*math.sin(ay)+z*math.cos(ay)
    y,z=y*math.cos(ax)-z*math.sin(ax),y*math.sin(ax)+z*math.cos(ax)
    return x,y,z
RV=[rot(v) for v in V]; cx,cy,R=W//2,px(520),px(330)
P2=[(cx+v[0]*R,cy-v[1]*R) for v in RV]
edges={}
for f in F2:
    for a_,b_ in ((f[0],f[1]),(f[1],f[2]),(f[2],f[0])):
        k=tuple(sorted((a_,b_))); edges[k]=max(edges.get(k,-9),(RV[a_][2]+RV[b_][2])/2)
for (a_,b_),z in sorted(edges.items(),key=lambda e:e[1]):
    if z<0: dashed(d,P2[a_],P2[b_],(80,94,124),px(4),px(14),px(12))
for (a_,b_),z in edges.items():
    if z>=0: d.line([P2[a_],P2[b_]],fill=WHITE,width=px(5))
for i_,v in enumerate(RV):
    if v[2]>=0: rr=px(9); d.ellipse([P2[i_][0]-rr,P2[i_][1]-rr,P2[i_][0]+rr,P2[i_][1]+rr],fill=YEL)
headline(d,["NEVER RENDERED."],px(930),WHITE,140)
d.text((W//2,px(1080)),"ALWAYS RUNNING.",font=bebas(100),fill=TEAL,anchor='mt')
d.text((W//2,px(1210)),"WE DO OUR BEST WORK WHERE YOU NEVER LOOK.",font=mono(22),fill=GREY,anchor='mt')
d=nv_footer(im,d,"EMPLOYEE MORALE")
finish(im,'poster_nonvis_never-rendered_1024x1536.png')
print('ok')
