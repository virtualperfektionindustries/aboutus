import math
from PIL import Image,ImageDraw,ImageFont
NAVY=(24,34,58); WHITE=(236,238,240); YEL=(224,176,48); GREY=(150,165,190); TEAL=(150,212,199)
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz))

def vpk_icon(N=2048,bg=None):
    """VPK Industries: a square partitioned like a BSP tree; the first two splits draw a V."""
    im=Image.new('RGBA',(N,N),(bg+(255,)) if bg else (0,0,0,0)); d=ImageDraw.Draw(im)
    m=N*0.06; x0,y0,x1,y1=m,m,N-m,N-m
    L=lambda u,v:(x0+u*(x1-x0),y0+v*(y1-y0))
    ow=N*0.045; w=N*0.028; tw=N*0.018
    # V: outer and inner split lines meet the bottom tips
    VO=[L(0.10,0),L(0.50,0.90),L(0.90,0)]; VI=[L(0.33,0),L(0.50,0.50),L(0.67,0)]
    d.polygon([VO[0],VO[1],VO[2],VI[2],VI[1],VI[0]],fill=YEL)
    d.rectangle([0,0,N,y0],fill=(bg+(255,)) if bg else (0,0,0,0))
    # x on the outer V lines at height v
    lx=lambda v:0.10+0.40*v/0.90; rx=lambda v:0.90-0.40*v/0.90
    lines=[(VO[0],VO[1],w),(VO[1],VO[2],w),(VI[0],VI[1],w),(VI[1],VI[2],w),
           (L(0.5,0.90),L(0.5,1),tw),
           (L(0,0.56),L(lx(0.56),0.56),tw),(L(0.17,0.56),L(0.17,1),tw),(L(0,0.80),L(0.17,0.80),tw),
           (L(1,0.30),L(rx(0.30),0.30),tw),(L(0.83,0.30),L(0.83,1),tw),(L(0.83,0.70),L(1,0.70),tw),
           (L(0.17,0.80),L(lx(0.80),0.80),tw)]
    lay=Image.new('RGBA',(N,N),(0,0,0,0)); ld=ImageDraw.Draw(lay)
    for a,b,ww in lines: ld.line([a,b],fill=WHITE,width=int(ww))
    for p_ in (VO[1],VI[1]): r=w*0.5; ld.ellipse([p_[0]-r,p_[1]-r,p_[0]+r,p_[1]+r],fill=WHITE)
    clip=Image.new('L',(N,N),0); ImageDraw.Draw(clip).rectangle([x0,y0,x1,y1],fill=255)
    lay.putalpha(Image.composite(lay.getchannel('A'),Image.new('L',(N,N),0),clip))
    im.alpha_composite(lay); d=ImageDraw.Draw(im)
    d.rectangle([x0,y0,x1,y1],outline=WHITE,width=int(ow))
    return im

def dashed(d,p0,p1,col,w,dash,gap):
    x0,y0=p0; x1,y1=p1; L=math.hypot(x1-x0,y1-y0); s=0
    while s<L:
        e=min(L,s+dash); d.line([(x0+(x1-x0)*s/L,y0+(y1-y0)*s/L),(x0+(x1-x0)*e/L,y0+(y1-y0)*e/L)],fill=col,width=int(w)); s+=dash+gap

def nonvis_icon(N=2048,bg=None):
    """Nonvis Division: a wireframe cube, hidden edges dashed, an eye in the middle."""
    im=Image.new('RGBA',(N,N),(bg+(255,)) if bg else (0,0,0,0)); d=ImageDraw.Draw(im)
    cx,cy,a=N/2,N/2,N*0.44; c=math.cos(math.radians(30))*a
    P=dict(T=(cx,cy-a),UL=(cx-c,cy-a/2),UR=(cx+c,cy-a/2),C=(cx,cy),LL=(cx-c,cy+a/2),LR=(cx+c,cy+a/2),B=(cx,cy+a))
    w=N*0.022
    for e in (('C','T'),('C','LL'),('C','LR')): dashed(d,P[e[0]],P[e[1]],GREY,N*0.016,N*0.05,N*0.035)
    for e in (('T','UL'),('T','UR'),('UL','LL'),('UR','LR'),('LL','B'),('LR','B'),('UL','C'),('UR','C'),('C','B')):
        d.line([P[e[0]],P[e[1]]],fill=WHITE,width=int(w))
    for k in P.values(): r=w*0.5; d.ellipse([k[0]-r,k[1]-r,k[0]+r,k[1]+r],fill=WHITE)
    ew,eh=a*0.64,a*0.31; pts=[]
    for i in range(61): t=i/60; pts.append((cx-ew+2*ew*t,cy-eh*math.sin(math.pi*t)))
    for i in range(61): t=i/60; pts.append((cx+ew-2*ew*t,cy+eh*math.sin(math.pi*t)))
    d.polygon(pts,fill=(bg if bg else NAVY)+(255,)); d.line(pts+[pts[0]],fill=WHITE,width=int(N*0.026),joint='curve')
    r=eh*0.80; d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=YEL)
    r2=r*0.45; d.ellipse([cx-r2,cy-r2,cx+r2,cy+r2],fill=bg if bg else NAVY)
    r3=r*0.15; d.ellipse([cx+r*0.25-r3,cy-r*0.35-r3,cx+r*0.25+r3,cy-r*0.35+r3],fill=WHITE)
    return im

def lockup(icon,title,line2,slogan,out,slogan_col):
    S=2; W,H=2048*S,640*S
    im=Image.new('RGBA',(W,H),NAVY+(255,)); d=ImageDraw.Draw(im)
    ic=icon.resize((int(H*0.72),int(H*0.72)),Image.LANCZOS); im.alpha_composite(ic,(int(H*0.16),int(H*0.14)))
    x=int(H*1.02); f=bebas(210*S); xx=x; y=int(H*0.22)
    for ch in title: d.text((xx,y),ch,font=f,fill=WHITE); xx+=d.textlength(ch,font=f)+6*S
    d.text((x+8*S,y+235*S),line2,font=mono(34*S,'SemiBold'),fill=GREY)
    d.line([(x+8*S,y+300*S),(xx-6*S,y+300*S)],fill=YEL,width=6*S)
    d.text((x+8*S,y+322*S),slogan,font=mono(38*S),fill=slogan_col)
    im.resize((2048,640),Image.LANCZOS).convert('RGB').save(out,optimize=True)

if __name__=='__main__':
    O='vpk_brand/'
    v=vpk_icon(); v.save(O+'vpk-industries_logo_icon_1024.png'.replace('1024','2048'))
    v.resize((1024,1024),Image.LANCZOS).save(O+'vpk-industries_logo_icon_1024.png',optimize=True)
    vpk_icon(1024,NAVY).save(O+'vpk-industries_logo_icon_navy_1024.png',optimize=True)
    n=nonvis_icon(); n.resize((1024,1024),Image.LANCZOS).save(O+'nonvis-division_logo_icon_1024.png',optimize=True)
    nonvis_icon(1024,NAVY).save(O+'nonvis-division_logo_icon_navy_1024.png',optimize=True)
    lockup(v,"VPK INDUSTRIES","VIRTUAL PERFEKTION INDUSTRIES","WE OWN THE WORLD. LITERALLY.",O+'vpk-industries_logo_2048x640.png',YEL)
    lockup(n,"NONVIS DIVISION","A VPK INDUSTRIES DIVISION","NEVER RENDERED. ALWAYS RUNNING.",O+'nonvis-division_logo_2048x640.png',TEAL)
    print('ok')
