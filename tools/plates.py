import random
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
S=2; W,H=1024*S,512*S
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def px(v): return int(v*S)
random.seed(4)
def plate(code,program,name,longname,serial,spec,note,scratch,sticker,out):
    random.seed(4)
    # ---- brushed steel: fine horizontal grain ----
    n=Image.effect_noise((W//90,H),14).resize((W,H),Image.BILINEAR)
    n2=Image.effect_noise((W//30,H//2),8).resize((W,H),Image.BILINEAR)
    g=ImageChops.add(Image.new('L',(W,H),168),n,scale=1.0,offset=-128)
    g=ImageChops.add(g,n2,scale=1.0,offset=-128)
    grad=Image.new('L',(W,H)); gd=ImageDraw.Draw(grad)
    for y in range(H): gd.line([(0,y),(W,y)],fill=int(128+22*(1-y/H)))
    g=ImageChops.add(g,grad,scale=1.0,offset=-128)
    plate=Image.merge('RGB',(g.point(lambda v:int(v*0.92)),g.point(lambda v:int(v*0.97)),g)).convert('RGBA')
    d=ImageDraw.Draw(plate)
    # bevel
    for i in range(px(6)):
        a=int(90*(1-i/px(6)))
        d.line([(i,i),(W-1-i,i)],fill=(255,255,255,a)); d.line([(i,i),(i,H-1-i)],fill=(255,255,255,a))
        d.line([(i,H-1-i),(W-1-i,H-1-i)],fill=(0,0,0,a)); d.line([(W-1-i,i),(W-1-i,H-1-i)],fill=(0,0,0,a))
    # rivets
    for (x,y) in ((28,28),(996,28),(28,484),(996,484)):
        x,y=px(x),px(y); r=px(11)
        d.ellipse([x-r+px(2),y-r+px(3),x+r+px(2),y+r+px(3)],fill=(30,30,30,150))
        d.ellipse([x-r,y-r,x+r,y+r],fill=(120,124,130,255))
        d.ellipse([x-r+px(2),y-r+px(2),x+r-px(4),y+r-px(4)],fill=(190,194,200,255))
        d.ellipse([x-px(3),y-px(3),x+px(1),y+px(1)],fill=(240,240,245,255))
    def engrave(xy,text,font,ink=(34,38,44),hl=(235,238,242),anchor='la'):
        x,y=xy
        d.text((x+px(0.6),y+px(1)),text,font=font,fill=hl+(110,),anchor=anchor)
        d.text((x,y),text,font=font,fill=ink+(255,),anchor=anchor)
    M=px(60)
    engrave((M,px(52)),"VPK INDUSTRIES  ·  NONVIS DIVISION",mono(20))
    engrave((W-M,px(52)),program,mono(20,'SemiBold'),anchor='ra')
    d.line([(M,px(86)),(W-M,px(86))],fill=(40,44,50,255),width=px(2)); d.line([(M,px(88)),(W-M,px(88))],fill=(230,232,236,140),width=px(1))
    engrave((M,px(100)),code,bebas(54),ink=(150,40,30))
    engrave((M,px(150)),name,bebas(118))
    engrave((M,px(268)),longname,mono(15 if len(longname)<=60 else 13,'SemiBold'))
    # spec table
    rows=[("MODEL",code),("SERIAL",serial)]+spec+[("DESIGNED BY","KDANY"),("OPERATED BY","NONVIS DIVISION")]
    y=px(306)
    for i,(k,v) in enumerate(rows):
        x=M+(0 if i<3 else px(430)); yy=y+(i%3)*px(30)
        engrave((x,yy),k,mono(16,'SemiBold'),ink=(70,76,84)); engrave((x+px(150),yy),v,mono(16))
    # old name, scratched
    ox,oy=px(640),px(108)
    engrave((ox,oy),note,mono(16,'SemiBold'),ink=(60,66,74))
    for _ in range(5 if scratch else 0):
        x0=ox+random.randint(0,px(260)); y0=oy+random.randint(px(2),px(18))
        d.line([(x0,y0),(x0+random.randint(px(40),px(120)),y0+random.randint(-px(6),px(6)))],fill=(205,208,214,180),width=px(1))
    if sticker[0]=="NOTE":
        # handwritten sticky note, stuck on by someone
        NW,NH=px(186),px(160)
        note_=Image.new('RGBA',(NW,NH),(0,0,0,0)); nd=ImageDraw.Draw(note_)
        for yy in range(NH):
            t_=yy/NH; nd.line([(0,yy),(NW,yy)],fill=(int(252-6*t_),int(226-14*t_),int(92-20*t_),255))
        nd.rectangle([0,0,NW,px(20)],fill=(240,212,80,255))
        # curled bottom-right corner
        nd.polygon([(NW,NH-px(26)),(NW,NH),(NW-px(26),NH)],fill=(0,0,0,0))
        nd.polygon([(NW,NH-px(26)),(NW-px(26),NH),(NW-px(23),NH-px(20))],fill=(214,186,70,255))
        mk=ImageFont.truetype('fonts/PermanentMarker-Regular.ttf',px(22))
        ink=(28,36,70,255)
        nd.text((px(16),px(30)),"DO NOT KICK",font=mk,fill=ink)
        nd.text((px(16),px(62)),"THE SERVER.",font=mk,fill=ink)
        mk2=ImageFont.truetype('fonts/PermanentMarker-Regular.ttf',px(28))
        nd.text((px(44),px(96)),"AGAIN.",font=mk2,fill=(170,30,24,255))
        nd.line([(px(42),px(136)),(px(148),px(133))],fill=(170,30,24,255),width=px(3))
        nd.line([(px(48),px(142)),(px(140),px(140))],fill=(170,30,24,255),width=px(2))
        note_=note_.rotate(-6,resample=Image.BICUBIC,expand=True)
        nx,ny=px(735),px(132)
        sh_=Image.new('RGBA',(W,H),(0,0,0,0)); sh_.paste((0,0,0,120),(nx+px(5),ny+px(7)),note_.getchannel('A'))
        plate=Image.alpha_composite(plate,sh_.filter(ImageFilter.GaussianBlur(px(5))))
        plate.alpha_composite(note_,(nx,ny))
    else:
        # the machine's motto, engraved quietly like the rest of the plate
        engrave((px(640),px(170)),"MOTTO",mono(13,'SemiBold'),ink=(80,86,94))
        mf=mono(17,'MediumItalic'); full='"'+sticker[0]+(' '+sticker[1] if sticker[1] else '')+'"'
        if d.textlength(full,font=mf)<=px(324):
            engrave((px(640),px(192)),full,mf,ink=(44,48,56))
        else:
            engrave((px(640),px(192)),'"'+sticker[0],mf,ink=(44,48,56))
            engrave((px(640),px(216)),' '+sticker[1]+'"',mf,ink=(44,48,56))
    d=ImageDraw.Draw(plate)
    # footer
    d.line([(M,px(408)),(W-M,px(408))],fill=(40,44,50,255),width=px(2)); d.line([(M,px(410)),(W-M,px(410))],fill=(230,232,236,140),width=px(1))
    def engrave2(xy,text,font,ink=(34,38,44),anchor='la'):
        d.text((xy[0]+px(0.6),xy[1]+px(1)),text,font=font,fill=(235,238,242,110),anchor=anchor); d.text(xy,text,font=font,fill=ink+(255,),anchor=anchor)
    engrave2((M,px(424)),'"WE OWN THE WORLD. LITERALLY."',mono(16,'SemiBold'),ink=(60,66,74))
    engrave2((W-M,px(424)),"CLASSIFIED · NONVIS CLEARANCE REQUIRED",mono(16,'SemiBold'),ink=(150,40,30),anchor='ra')
    # grime
    gr=Image.effect_noise((W//64,H//64),70).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(px(18))).point(lambda v:max(0,v-140)*3)
    go=Image.new('RGBA',(W,H),(40,34,26,0)); go.putalpha(gr.point(lambda v:int(v*0.18))); plate=Image.alpha_composite(plate,go)
    plate.resize((1024,512),Image.LANCZOS).convert('RGB').save(out,optimize=True)


plate("KD-WX-001","WEATHER PROGRAM","A.T.M.O.S.","ATMOSPHERIC TUNING & MOOD OVERRIDE STATION","001-0000-0001",
      [("LINKED","6 ENV. ENTITIES"),("PROFILES","SUMMER / NIGHT")],"UPLINK: KD-WX-003 S.T.R.A.T.O.S.",False,
      ("NATURE IS A SETTING.",""),"noclip/kd-wx-001_atmos_plate_1024x512.png")
plate("KD-WX-002","WEATHER PROGRAM","F.O.R.E.C.A.S.T.","FULLY OVERRIDDEN RANDOM EVENT & CLIMATE ACTIVATION SCHEDULING TERMINAL","002-0000-0001",
      [("ROLL","WEIGHTED RANDOM"),("CYCLE","EVERY ROUND")],"UPLINK: KD-WX-003 S.T.R.A.T.O.S.",False,
      ("FORECAST ACCURACY: 100%.","WE MAKE IT!"),"noclip/kd-wx-002_forecast_plate_1024x512.png")
plate("KD-WX-003","WEATHER PROGRAM","S.T.R.A.T.O.S.","SEASONAL TRANSMISSION & REGIONAL ATMOSPHERE TAKEOVER SYSTEM","003-0000-0001",
      [("ROOF ARRAY","2 ANT. + 2 DISHES"),("EMITTER","SIDE MODULE")],'FORMERLY "RAINMAKER Mk II"',True,
      ("NOTE",""),"noclip/kd-wx-003_stratos_plate_1024x512.png")
plate("KD-MCS-001","MAP CONTROL PROGRAM","V.I.G.I.L.","VANDALISM INCIDENT & GENERAL INFRASTRUCTURE LOG","MCS-0000-0001",
      [("MONITORING","ALL MAP ASSETS"),("LOG","PERMANENT")],"STANDALONE UNIT",False,
      ("EVERYTHING IS LOGGED.","EVERYTHING!"),"noclip/kd-mcs-001_vigil_plate_1024x512.png")
print('ok')
