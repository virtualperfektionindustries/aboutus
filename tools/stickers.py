import math,random,sys
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageChops
sys.path.insert(0,'tools')
from brand_logos import vpk_icon,nonvis_icon
S=2; W,H=1600*S,760*S
BG=(26,26,28); LIGHT=(226,226,222); GREY=(120,120,124); DARK2=(70,70,74); RED=(214,40,40)
def px(v): return int(v*S)
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def inter(sz,w='Bold'): return ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-'+w+'.otf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def spaced(d,xy,text,font,fill,sp):
    x,y=xy
    for ch in text: d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+sp
    return x
def rounded_mask(poly,r):
    m=Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon([(px(x),px(y)) for x,y in poly],fill=255)
    m=m.filter(ImageFilter.MinFilter(r*2+1 if r*2+1<60 else 59)) if False else m
    b=m.filter(ImageFilter.GaussianBlur(px(r)))
    return b.point(lambda v:255 if v>128 else 0).filter(ImageFilter.GaussianBlur(1))
def matrix(d,x0,y0,x1,y1,seed,cell):
    r=random.Random(seed); w=x1-x0
    # vertical bars at the edges, a pixel field in the middle
    x=x0
    for _ in range(6):
        bw=r.choice((cell,cell*2,cell*3)); d.rectangle([x,y0,x+bw-1,y1],fill=LIGHT); x+=bw+r.choice((cell,cell*2))
    mx0=x+cell*2; mx1=x1-cell*14
    for yy in range(y0,y1,cell):
        for xx in range(mx0,mx1,cell):
            v=r.random()+0.25*math.sin(xx*0.013+seed)+0.2*math.cos(yy*0.05)
            if v<0.55: d.rectangle([xx,yy,xx+cell-1,yy+cell-1],fill=LIGHT)
    x=mx1+cell*2
    while x<x1:
        bw=r.choice((cell,cell*2,cell*4)); d.rectangle([x,y0,min(x1,x+bw-1),y1],fill=LIGHT); x+=bw+r.choice((cell,cell*2))
def barcode(d,x0,y0,x1,y1,seed,col):
    r=random.Random(seed); x=x0
    while x<x1:
        bw=r.choice((px(2),px(3),px(5),px(7))); d.rectangle([x,y0,min(x1,x+bw),y1],fill=col); x+=bw+r.choice((px(2),px(3),px(4)))
def xbox(d,x0,y0,x1,y1,col,w=2):
    d.rectangle([x0,y0,x1,y1],outline=col,width=px(w)); d.line([(x0,y0),(x1,y1)],fill=col,width=px(w)); d.line([(x0,y1),(x1,y0)],fill=col,width=px(w))
def brackets(d,x0,y0,x1,y1,col,l=18,w=3):
    for (cx,cy,sx,sy) in ((x0,y0,1,1),(x1,y0,-1,1),(x0,y1,1,-1),(x1,y1,-1,-1)):
        d.line([(cx,cy),(cx+sx*px(l),cy)],fill=col,width=px(w)); d.line([(cx,cy),(cx,cy+sy*px(l))],fill=col,width=px(w))

def hazard(d,cx,cy,r,kind):
    d.ellipse([cx-r,cy-r,cx+r,cy+r],outline=RED,width=px(6))
    if kind=='hand':
        d.rounded_rectangle([cx-px(16),cy-px(4),cx+px(16),cy+px(26)],radius=px(8),fill=RED)
        for i,h in enumerate((30,38,36,28)): d.rounded_rectangle([cx-px(16)+i*px(9),cy-px(h),cx-px(10)+i*px(9),cy],radius=px(3),fill=RED)
    elif kind=='bolt':
        pts=[(0,-34),(14,-34),(4,-4),(18,-4),(-10,34),(-4,6),(-18,6)]
        d.polygon([(cx+px(x),cy+px(y)) for x,y in pts],fill=RED)
    elif kind=='eye':
        d.ellipse([cx-px(28),cy-px(14),cx+px(28),cy+px(14)],outline=RED,width=px(5)); d.ellipse([cx-px(8),cy-px(8),cx+px(8),cy+px(8)],fill=RED)
    elif kind=='drop':
        rr=px(16); y=cy+px(10); d.ellipse([cx-rr,y-rr,cx+rr,y+rr],fill=RED); d.polygon([(cx-rr*0.92,y-rr*0.38),(cx,y-rr*2.5),(cx+rr*0.92,y-rr*0.38)],fill=RED)
    d.line([(cx-r*0.7,cy+r*0.7),(cx+r*0.7,cy-r*0.7)],fill=RED,width=px(6))

def sticker(fname,shape,accent,code,name,sub,warning,badge,partno,proto,serial,seed,haz,icon):
    im=Image.new('RGBA',(W,H),(0,0,0,0))
    mask=rounded_mask(shape,14)
    base=Image.new('RGBA',(W,H),BG+(255,)); base.putalpha(mask); im.alpha_composite(base)
    d=ImageDraw.Draw(im)
    # top line: PROTOTYPE + serial, right-aligned, sized to fit
    hy=px(HY.get(fname,80)); xr=px(XR.get(fname,1556))
    xbox(d,xr-px(44),hy,xr,hy+px(44),DARK2,2)
    sf=inter(40,'ExtraBold'); sx=xr-px(60)
    d.text((sx,hy),serial,font=sf,fill=LIGHT,anchor='ra')
    sw=d.textlength(serial,font=sf); pf=mono(22,'Regular')
    pw=sum(d.textlength(c,font=pf)+px(5) for c in proto)
    px0=sx-sw-px(30)-pw
    spaced(d,(px0,hy+px(8)),proto,pf,GREY,px(5))
    xbox(d,px0-px(60),hy,px0-px(16),hy+px(44),DARK2,2)
    # chevrons in the accent colour
    for i in range(2): d.text((px(108),px(205)+i*px(70)),"<",font=mono(40),fill=accent)
    # the data block
    matrix(d,px(170),px(170),px(1150),px(342),seed,px(12))
    # circles + hazard
    for (cx,cy) in ((210,420),(300,420),(210,510)): d.ellipse([px(cx-36),px(cy-36),px(cx+36),px(cy+36)],outline=DARK2,width=px(4))
    d.ellipse([px(204),px(414),px(216),px(426)],fill=GREY)
    d.line([(px(274),px(394)),(px(326),px(446))],fill=DARK2,width=px(4)); d.line([(px(326),px(394)),(px(274),px(446))],fill=DARK2,width=px(4))
    hazard(d,px(300),px(510),px(38),haz)
    # big code + name
    x=spaced(d,(px(380),px(372)),code,inter(78,'SemiBold'),LIGHT,px(6))
    spaced(d,(px(380),px(470)),name,inter(40,'Regular'),LIGHT,px(10))
    d.text((px(382),px(522)),sub,font=mono(15,'SemiBold'),fill=GREY)
    y=px(556)
    for ln in warning: d.text((px(382),y),ln,font=inter(17,'Bold'),fill=LIGHT); y+=px(26)
    # right column: type box, badge, x box
    brackets(d,px(1180),px(190),px(1340),px(350),DARK2)
    cx,cy=px(1260),px(270); d.polygon([(cx,cy-px(64)),(cx+px(64),cy),(cx,cy+px(64)),(cx-px(64),cy)],outline=GREY,width=px(2))
    d.line([(cx,cy-px(74)),(cx,cy+px(74))],fill=GREY,width=px(2)); d.line([(cx-px(74),cy),(cx+px(74),cy)],fill=GREY,width=px(2))
    spaced(d,(px(1190),px(372)),"TYPE-"+icon,mono(26,'Regular'),GREY,px(6))
    brackets(d,px(1370),px(190),px(1550),px(350),LIGHT)
    bx,by,br=px(1460),px(270),px(62); d.ellipse([bx-br,by-br,bx+br,by+br],outline=LIGHT,width=px(4))
    d.text((bx,by-px(8)),badge,font=bebas(64),fill=LIGHT,anchor='mm'); d.line([(bx-px(36),by+px(32)),(bx+px(36),by+px(32))],fill=LIGHT,width=px(5))
    brackets(d,px(1370),px(380),px(1550),px(560),DARK2)
    logo=(vpk_icon(1024,BG) if icon!='N' else nonvis_icon(1024,BG)).resize((px(130),px(130)),Image.LANCZOS)
    im.alpha_composite(logo,(px(1395),px(405))); d=ImageDraw.Draw(im)
    # part number strip
    sx0,sy0,sx1,sy1=px(430),px(640),px(1120),px(700)
    d.rounded_rectangle([sx0,sy0,sx1,sy1],radius=px(14),fill=(78,78,80))
    d.text((sx0+px(24),(sy0+sy1)//2),"PART N",font=inter(26,'Regular'),fill=(30,30,32),anchor='lm')
    barcode(d,sx0+px(140),sy0+px(10),sx1-px(330),sy1-px(10),seed+1,(30,30,32))
    d.rectangle([sx1-px(320),sy0+px(10),sx1-px(20),sy1-px(10)],fill=(78,78,80))
    barcode(d,sx1-px(320),sy0+px(10),sx1-px(20),sy0+px(24),seed+2,(30,30,32))
    d.text((sx1-px(170),sy0+px(42)),partno,font=inter(26,'Regular'),fill=(30,30,32),anchor='mm')
    # slight wear: tiny scratches inside the sticker
    r=random.Random(seed); wl=Image.new('L',(W,H),0); wd=ImageDraw.Draw(wl)
    for _ in range(18):
        x=r.randint(0,W); y=r.randint(0,H); wd.line([(x,y),(x+r.randint(-px(60),px(60)),y+r.randint(-px(4),px(4)))],fill=r.randint(30,70),width=1)
    wl=ImageChops.multiply(wl,mask); sc=Image.new('RGBA',(W,H),(255,255,255,0)); sc.putalpha(wl); im=Image.alpha_composite(im,sc)
    im=im.resize((1600,760),Image.LANCZOS); bbox=im.getbbox(); im=im.crop((max(0,bbox[0]-8),max(0,bbox[1]-8),bbox[2]+8,bbox[3]+8))
    im.save('stickers/'+fname,optimize=True); return im

# notched shapes, in 1600x760 units
A=[(80,170),(110,140),(110,60),(1560,60),(1590,90),(1590,560),(1560,590),(1180,590),(1140,730),(420,730),(380,600),(90,600),(80,590)]
F=[(60,140),(140,60),(900,60),(940,100),(1590,100),(1590,620),(1500,710),(1150,710),(1120,730),(400,730),(380,620),(60,620)]
T=[(90,200),(120,170),(120,80),(940,80),(990,40),(1560,40),(1590,70),(1590,600),(1240,600),(1180,730),(430,730),(380,610),(120,610),(90,580)]
V=[(70,60),(1520,60),(1590,130),(1590,450),(1550,490),(1550,600),(1590,640),(1590,730),(420,730),(380,690),(70,690),(70,420),(100,390),(100,260),(70,230)]
items=[
 ('kd-wx-001_atmos_sticker.png',A,(150,212,199),"KD-WX-001","A.T.M.O.S.","ATMOSPHERIC TUNING & MOOD OVERRIDE STATION",
  ["DO NOT ADJUST THE SUN WITHOUT","AUTHORIZATION. NATURE IS A SETTING."],"AT1","1.61803398875","PROTOTYPE","VPK/WX 001-1",11,'hand','A'),
 ('kd-wx-002_forecast_sticker.png',F,(140,185,255),"KD-WX-002","F.O.R.E.C.A.S.T.","RANDOM EVENT & CLIMATE ACTIVATION SCHEDULING",
  ["KEEP COFFEE AWAY FROM THE","PROBABILITY CORE. SEE INCIDENT #003."],"FC2","0.90 / 0.10","CALIBRATED","VPK/WX 002-3",22,'drop','B'),
 ('kd-wx-003_stratos_sticker.png',T,(224,176,48),"KD-WX-003","S.T.R.A.T.O.S.","SEASONAL TRANSMISSION & ATMOSPHERE TAKEOVER",
  ["HIGH OUTPUT EMITTER. 2.4 GW.","DO NOT KICK THE CABINET. AGAIN."],"ST3","2.71828182845","MK II","VPK/WX 003-2",33,'bolt','C'),
 ('kd-mcs-001_vigil_sticker.png',V,(236,162,187),"KD-MCS-001","V.I.G.I.L.","VANDALISM INCIDENT & GENERAL INFRASTRUCTURE LOG",
  ["THIS STICKER IS BEING MONITORED.","EVERYTHING IS LOGGED. EVERYTHING!"],"VG1","4.04040404040","ALWAYS ON","VPK/MCS 001-9",44,'eye','N'),
]
HY={'kd-wx-002_forecast_sticker.png':112,'kd-wx-003_stratos_sticker.png':62,'kd-mcs-001_vigil_sticker.png':78}
XR={'kd-mcs-001_vigil_sticker.png':1500}
ims=[sticker(*it) for it in items]
sh=Image.new('RGBA',(1640,4*800),(220,220,216,255))
for i,im in enumerate(ims): sh.alpha_composite(im,(20,20+i*800))
sh.convert('RGB').resize((820,1600)).save('_sheet.png')
print('ok')
