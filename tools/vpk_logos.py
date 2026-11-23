import math
from PIL import Image,ImageDraw,ImageFont,ImageFilter
S=4; W,H=1024*S,512*S
NAVY=(24,34,58); WHITE=(236,238,240); YEL=(224,176,48); RED=(178,34,30); TEAL=(150,212,199)
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def px(v): return int(v*S)
def canvas():
    im=Image.new('RGB',(W,H),NAVY); return im,ImageDraw.Draw(im)
def iso(cx,cy,a):
    c=math.cos(math.radians(30))*a
    return dict(T=(cx,cy-a),UL=(cx-c,cy-a/2),UR=(cx+c,cy-a/2),C=(cx,cy),LL=(cx-c,cy+a/2),LR=(cx+c,cy+a/2),B=(cx,cy+a))
def wordmark(d,x,y):
    f=bebas(100); t="VPK INDUSTRIES"; xx=x
    for ch in t:
        d.text((xx,y),ch,font=f,fill=WHITE); xx+=d.textlength(ch,font=f)+px(3)
    d.text((x+px(4),y+px(114)),"VIRTUAL PERFECTION KERNEL INDUSTRIES",font=mono(17,'SemiBold'),fill=(150,165,190))
    d.line([(x+px(4),y+px(146)),(xx-px(3),y+px(146))],fill=YEL,width=px(3))
    d.text((x+px(4),y+px(160)),"WE OWN THE WORLD. LITERALLY.",font=mono(19),fill=YEL)
def dashed(d,p0,p1,col,w,dash,gap):
    x0,y0=p0; x1,y1=p1; L=math.hypot(x1-x0,y1-y0); n=int(L/(dash+gap))+1
    for i in range(n):
        a=i*(dash+gap)/L; b=min(1,(i*(dash+gap)+dash)/L)
        if a>=1: break
        d.line([(x0+(x1-x0)*a,y0+(y1-y0)*a),(x0+(x1-x0)*b,y0+(y1-y0)*b)],fill=col,width=w)

# ---------- 1. the package: cube with a missing top face, a small world inside ----------
def logo1(d,cx,cy,a):
    p=iso(cx,cy,a)
    d.polygon([p['T'],p['UL'],p['C']],fill=(14,20,36))            # inner back-left wall
    d.polygon([p['T'],p['UR'],p['C']],fill=(30,42,70))            # inner back-right wall
    # the world inside
    r=a*0.42; wx,wy=cx,cy-a*0.30
    d.ellipse([wx-r,wy-r,wx+r,wy+r],fill=TEAL)
    for k in (-0.5,0,0.5):
        yy=wy+k*r; hw=math.sqrt(max(0,r*r-(k*r)**2))
        d.line([(wx-hw,yy),(wx+hw,yy)],fill=NAVY,width=px(4))
    d.ellipse([wx-r*0.45,wy-r,wx+r*0.45,wy+r],outline=NAVY,width=px(4))
    d.line([(wx,wy-r),(wx,wy+r)],fill=NAVY,width=px(4))
    # front faces hide the lower half of the world
    d.polygon([p['UL'],p['C'],p['B'],p['LL']],fill=WHITE)
    d.polygon([p['C'],p['UR'],p['LR'],p['B']],fill=(190,198,210))
    w=px(5)
    for e in (('T','UL'),('T','UR'),('UL','C'),('UR','C'),('UL','LL'),('UR','LR'),('LL','B'),('LR','B'),('C','B')):
        d.line([p[e[0]],p[e[1]]],fill=WHITE,width=w)
    # missing top face: dashed outline where it would be
    for e in (('T','UL'),('T','UR')):
        pass

# ---------- 2. the partition: a square split like a BSP tree, the splits draw a V ----------
def logo2(d,cx,cy,a):
    x0,y0,x1,y1=cx-a,cy-a,cx+a,cy+a
    L=lambda u,v:(x0+u*(x1-x0),y0+v*(y1-y0))
    # the V region filled
    d.polygon([L(0.12,0),L(0.5,0.92),L(0.88,0),L(0.66,0),L(0.5,0.52),L(0.34,0)],fill=YEL)
    w=px(6); col=WHITE
    d.rectangle([x0,y0,x1,y1],outline=col,width=px(8))
    # first split: the two V lines
    d.line([L(0.12,0),L(0.5,0.92)],fill=col,width=w); d.line([L(0.88,0),L(0.5,0.92)],fill=col,width=w)
    d.line([L(0.34,0),L(0.5,0.52)],fill=col,width=w); d.line([L(0.66,0),L(0.5,0.52)],fill=col,width=w)
    # further splits of the remaining space
    d.line([L(0,0.55),L(0.12+0.38*0.55/0.92,0.55)],fill=col,width=px(4))
    d.line([L(0.18,0.55),L(0.18,1)],fill=col,width=px(4))
    d.line([L(1,0.30),L(0.88-0.38*0.30/0.92,0.30)],fill=col,width=px(4))
    d.line([L(0.82,0.30),L(0.82,1)],fill=col,width=px(4))
    d.line([L(0.82,0.72),L(1,0.72)],fill=col,width=px(4))
    d.line([L(0.5,0.92),L(0.5,1)],fill=col,width=px(4))
    d.line([L(0,0.80),L(0.18,0.80)],fill=col,width=px(4))

# ---------- 3. the eye in the box: wireframe cube, hidden edges dashed, an eye at the centre ----------
def logo3(d,cx,cy,a):
    p=iso(cx,cy,a); w=px(5)
    for e in (('C','T'),('C','LL'),('C','LR')):
        dashed(d,p[e[0]],p[e[1]],(150,165,190),px(4),px(16),px(12))
    for e in (('T','UL'),('T','UR'),('UL','LL'),('UR','LR'),('LL','B'),('LR','B'),('UL','C'),('UR','C'),('C','B')):
        d.line([p[e[0]],p[e[1]]],fill=WHITE,width=w)
    # the eye
    ew,eh=a*0.62,a*0.30
    pts=[]
    for i in range(41):
        t=i/40; x=cx-ew+2*ew*t; y=cy-eh*math.sin(math.pi*t); pts.append((x,y))
    for i in range(41):
        t=i/40; x=cx+ew-2*ew*t; y=cy+eh*math.sin(math.pi*t); pts.append((x,y))
    d.polygon(pts,fill=NAVY,outline=WHITE); d.line(pts+[pts[0]],fill=WHITE,width=px(6))
    r=eh*0.82; d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=YEL)
    r2=r*0.45; d.ellipse([cx-r2,cy-r2,cx+r2,cy+r2],fill=NAVY)
    r3=r*0.16; d.ellipse([cx+r*0.25-r3,cy-r*0.35-r3,cx+r*0.25+r3,cy-r*0.35+r3],fill=WHITE)

out=[]
for i,fn in enumerate((logo1,logo2,logo3),1):
    im,d=canvas()
    fn(d,px(220),px(256),px(150 if i!=2 else 140))
    wordmark(d,px(420),px(158))
    im=im.resize((1024,512),Image.LANCZOS); name=f'vpk_logo/vpk_logo_concept{i}_1024x512.png'; im.save(name,optimize=True); out.append(im)
sheet=Image.new('RGB',(1024,1536+40),(10,14,24))
for i,im in enumerate(out): sheet.paste(im,(0,i*(512+20)))
sheet.save('vpk_logo/vpk_logo_concepts_sheet.png',optimize=True)
print('ok')
