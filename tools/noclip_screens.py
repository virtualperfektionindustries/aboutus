from PIL import Image,ImageDraw,ImageFilter,ImageFont
S=2; W,H=1024*S,512*S; M=int(36*S)
JB='/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-'
def mono(sz,w='Bold'): return ImageFont.truetype(JB+w+'.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
BG=(12,17,20); STEEL_L=(60,71,82)
YELLOW=(224,176,48); TEAL=(150,212,199); PINK=(236,162,187); WHITE=(232,240,238); RED=(255,92,72); DIM=(92,122,118); BLUE=(140,185,255)
def px(v): return int(v*S)
def tag(t,x,y,word,c,f=None):
    # "[ OK ]" style tag: the brackets stay in place, the word is centred between them
    f=f or mono(18); cw=t.textlength("[",font=f)
    t.text((x,y),"[",font=f,fill=c); t.text((x+5*cw,y),"]",font=f,fill=c)
    w=t.textlength(word,font=f); t.text((x+cw+(4*cw-w)/2,y),word,font=f,fill=c)
COMPANY="VPK INDUSTRIES · NONVIS DIVISION"

def screen(code,program,title,subtitle,right,section,body,footer,joke,out):
    im=Image.new('RGBA',(W,H),BG+(255,)); d=ImageDraw.Draw(im)
    for x in range(0,W,px(32)): d.line([(x,0),(x,H)],fill=(18,26,29,255),width=1)
    for y in range(0,H,px(32)): d.line([(0,y),(W,y)],fill=(18,26,29,255),width=1)
    txt=Image.new('RGBA',(W,H),(0,0,0,0)); t=ImageDraw.Draw(txt)
    t.text((M,px(22)),code,font=mono(22),fill=YELLOW)
    cw=t.textlength(code+"  ",font=mono(22))
    t.text((M+cw,px(27)),program,font=mono(15,'SemiBold'),fill=DIM)
    t.text((M,px(48)),title,font=bebas(78),fill=TEAL)
    t.text((M,px(128)),subtitle,font=mono(15 if len(subtitle)<=50 else 13,'SemiBold'),fill=WHITE)
    def rtext(y,s_,f,c):
        w=t.textlength(s_,font=f); t.text((W-M-w,y),s_,font=f,fill=c)
    rtext(px(26),COMPANY,mono(13,'SemiBold'),DIM)
    for i,(s_,c) in enumerate(right): rtext(px(56+30*i),s_,mono(20 if i==0 else 16),c)
    t.line([(M,px(160)),(W-M,px(160))],fill=TEAL+(160,),width=px(2))
    t.text((M,px(170)),section,font=mono(15),fill=YELLOW)
    body(t)
    t.line([(M,px(372)),(W-M,px(372))],fill=STEEL_L+(255,),width=px(1))
    for i,f in enumerate(footer): t.text((M,px(382+22*i)),f,font=mono(14),fill=DIM)
    rtext(px(404),"CLASSIFIED · NONVIS CLEARANCE REQUIRED",mono(12,'SemiBold'),PINK)
    t.text((M,px(440)),joke,font=mono(20),fill=PINK)
    jw=t.textlength(joke,font=mono(20))
    t.rectangle([M+jw+px(14),px(442),M+jw+px(26),px(464)],fill=PINK+(255,))
    im=Image.alpha_composite(im,txt.filter(ImageFilter.GaussianBlur(5*S))); im=Image.alpha_composite(im,txt)
    sl=Image.new('L',(W,H),0); sd=ImageDraw.Draw(sl)
    for y in range(0,H,px(3)): sd.line([(0,y),(W,y)],fill=60,width=S)
    dk=Image.new('RGBA',(W,H),(0,0,0,0)); dk.putalpha(sl); im=Image.alpha_composite(im,dk)
    vg=Image.new('L',(W,H),255); ImageDraw.Draw(vg).rounded_rectangle([px(-40),px(-40),W+px(40),H+px(40)],radius=px(220),fill=0)
    vo=Image.new('RGBA',(W,H),(0,0,0,0)); vo.putalpha(vg.filter(ImageFilter.GaussianBlur(70*S)).point(lambda v:int(v*0.8))); im=Image.alpha_composite(im,vo)
    im.resize((1024,512),Image.LANCZOS).convert('RGB').save(out,optimize=True)

# ---------- KD-WX-001 A.T.M.O.S. ----------
def atmos_body(t):
    # POST_PROCESSING: N/A, the prefabs only hold an empty mesh with the post-process texture, no post_processing_volume entity
    items=[("OK","LIGHT_ENVIRONMENT","SUN / MOON"),("OK","ENV_SKY","SKYBOX"),("OK","ENV_CUBEMAP_FOG","FOG"),
           ("OK","ENV_WIND","WIND"),("N/A","POST_PROCESSING","NOT LINKED"),("OK","INFO_MAP_PARAMS","MAP PARAMETERS")]
    for i,(st,n,v) in enumerate(items):
        x=M+(0 if i<3 else px(480)); y=px(204+(i%3)*40)
        tag(t,x,y,st,TEAL if st=="OK" else YELLOW); t.text((x+px(84),y),n,font=mono(18),fill=WHITE); t.text((x+px(300),y),v,font=mono(18),fill=DIM)
for summer in (False,True):
    screen("KD-WX-001","WEATHER PROGRAM","A.T.M.O.S.","ATMOSPHERIC TUNING & MOOD OVERRIDE STATION",
           [("ACTIVE PROFILE  ENV_SUMMER",YELLOW),("STANDBY: ENV_NIGHT",DIM)] if summer else
           [("ACTIVE PROFILE  ENV_NIGHT",BLUE),("STANDBY: ENV_SUMMER",DIM)],
           "MAP ENVIRONMENT: 5 / 6 ENTITIES LINKED",atmos_body,
           ["ENVIRONMENT SYNC: COMPLETE","PROFILE SWITCH REQUIRES FULL REBUILD"],
           "NATURE IS A SETTING.","noclip/kd-wx-001_atmos%s_1024x512.png"%("_summer" if summer else ""))

# ---------- KD-WX-002 F.O.R.E.C.A.S.T. ----------
# Current state of the night prefab: rain every round, lightning at variable intervals, the storm state under maintenance.
def forecast_body(t):
    y=px(204); bx=M+px(150); bw=px(300); bh=px(18)
    for name,pct,col,active,note,nc in (("RAIN",100,BLUE,True,None,None),("STORM",None,YELLOW,False,"UNDER MAINTENANCE",YELLOW),
                                         ("CLEAR",None,DIM,False,"REMOVED - SEE INCIDENT #003",RED)):
        t.text((M,y),("> " if active else "  ")+name,font=mono(18),fill=WHITE if active else DIM)
        t.rectangle([bx,y+px(4),bx+bw,y+px(4)+bh],outline=STEEL_L+(255,),width=px(1))
        if pct is None:
            t.text((bx+px(10),y+px(3)),note,font=mono(13,'SemiBold'),fill=nc)
            t.text((bx+bw+px(14),y),"  -",font=mono(18),fill=DIM)
        else:
            t.rectangle([bx+px(2),y+px(6),bx+px(2)+int((bw-px(4))*pct/100),y+px(2)+bh],fill=col+(255,))
            t.text((bx+bw+px(14),y),f"{pct:>3}%",font=mono(18),fill=col)
        y+=px(40)
    t.text((M,y+px(6)),"ROLL METHOD: SINGLE STATE UNTIL STORM RETURNS",font=mono(14),fill=DIM)
    x2=W//2+px(80); y=px(204)
    for k,v,c in (("CURRENT STATE","RAIN",BLUE),("PRECIP CELLS","ALL ONLINE",TEAL),("LIGHTNING","VARIABLE INTERVAL",TEAL),("STORM MODULE","UNDER MAINTENANCE",YELLOW)):
        t.text((x2,y),k,font=mono(14,'SemiBold'),fill=DIM); t.text((x2,y+px(17)),v,font=mono(18),fill=c); y+=px(40)
screen("KD-WX-002","WEATHER PROGRAM","F.O.R.E.C.A.S.T.","FULLY OVERRIDDEN RANDOM EVENT & CLIMATE ACTIVATION SCHEDULING TERMINAL",
       [("FORECAST  RAIN",BLUE),("CONFIDENCE: 100%",TEAL)],
       "WEATHER STATE PROBABILITIES (PER ROUND)",forecast_body,
       ["STATES: RAIN (STORM UNDER MAINTENANCE)","SURFACE STATUS: WET"],
       "FORECAST ACCURACY: 100%. WE MAKE IT!","noclip/kd-wx-002_forecast_1024x512.png")

# For the env_summer prefab F.O.R.E.C.A.S.T. is simply switched off: a dark, powered-off screen.
def screen_off(out):
    im=Image.new('RGBA',(W,H),(7,9,10,255)); d=ImageDraw.Draw(im)
    gl=Image.new('L',(W,H),0); g=ImageDraw.Draw(gl)
    g.polygon([(px(120),0),(px(430),0),(px(140),H),(px(-170),H)],fill=22)   # soft glass reflection
    g.polygon([(px(470),0),(px(540),0),(px(250),H),(px(180),H)],fill=12)
    gl=gl.filter(ImageFilter.GaussianBlur(30*S))
    ref=Image.new('RGBA',(W,H),(180,200,205,0)); ref.putalpha(gl); im=Image.alpha_composite(im,ref)
    vg=Image.new('L',(W,H),255); ImageDraw.Draw(vg).rounded_rectangle([px(-40),px(-40),W+px(40),H+px(40)],radius=px(220),fill=0)
    vo=Image.new('RGBA',(W,H),(0,0,0,0)); vo.putalpha(vg.filter(ImageFilter.GaussianBlur(70*S)).point(lambda v:int(v*0.8))); im=Image.alpha_composite(im,vo)
    im.resize((1024,512),Image.LANCZOS).convert('RGB').save(out,optimize=True)
screen_off("noclip/kd-wx-002_forecast_summer_1024x512.png")

# ---------- KD-WX-003 S.T.R.A.T.O.S. ----------
def stratos_body_for(summer=False):
    # summer: S.T.R.A.T.O.S. is not broadcasting (env_summer prefab), the emitter is idle
    def body(t):
        y=px(204)
        rows=(("OK",TEAL,"SEASON: SUMMER","DEFAULT",TEAL) if summer else ("OK",TEAL,"SEASON: SUMMER","LOADED",DIM),
              ("OK",TEAL,"SEASON: NIGHT","LOADED",DIM) if summer else ("LIVE",BLUE,"SEASON: NIGHT","TRANSMITTING",BLUE),
              ("--",DIM,"SEASON: WINTER","NOT INSTALLED",YELLOW),("OK",TEAL,"ROOF ARRAY","2 ANT. + 2 DISHES",DIM),
              ("OFF",DIM,"EMITTER ANTENNA","IDLE",DIM) if summer else ("ON",TEAL,"EMITTER ANTENNA","ACTIVE",TEAL))
        for tg,tc,name,val,vc in rows:
            tag(t,M,y,tg,tc); t.text((M+px(84),y),name,font=mono(18),fill=WHITE); t.text((M+px(300),y),val,font=mono(18),fill=vc); y+=px(33)
        x2=W//2+px(110)
        t.text((x2,px(204)),"EMITTER OUTPUT",font=mono(14,'SemiBold'),fill=DIM)
        for i in range(12):
            h=px(10+i*7); xx=x2+i*px(26); col=TEAL if i<8 else (YELLOW if i<10 else RED)
            t.rectangle([xx,px(330)-h,xx+px(18),px(330)],fill=(STEEL_L if summer or i>=9 else col)+(255,))
        t.text((x2,px(340)),"SIDE EMITTER  |  0.0 GW  |  22 C" if summer else "SIDE EMITTER  |  2.4 GW  |  41 C",font=mono(14),fill=DIM if summer else TEAL)
    return body
screen("KD-WX-003","WEATHER PROGRAM","S.T.R.A.T.O.S.","SEASONAL TRANSMISSION & REGIONAL ATMOSPHERE TAKEOVER SYSTEM",
       [("CORE STATUS  ONLINE",TEAL),("UPLINK: KD-WX-001 / 002",DIM)],
       "SEASON MODULES",stratos_body_for(False),
       ['FORMERLY "RAINMAKER Mk II"'],
       "KD-PX DYNARAIN IS LOADED, EMITTING...","noclip/kd-wx-003_stratos_1024x512.png")
# the same screen for the env_summer prefab: no broadcast, emitter idle
screen("KD-WX-003","WEATHER PROGRAM","S.T.R.A.T.O.S.","SEASONAL TRANSMISSION & REGIONAL ATMOSPHERE TAKEOVER SYSTEM",
       [("CORE STATUS  STANDBY",YELLOW),("UPLINK: KD-WX-001 / 002",DIM)],
       "SEASON MODULES",stratos_body_for(True),
       ['FORMERLY "RAINMAKER Mk II"'],
       "EMITTER IDLE. WAITING FOR NIGHTFALL...","noclip/kd-wx-003_stratos_summer_1024x512.png")

# ---------- KD-MCS-001 V.I.G.I.L. ----------
ASSETS=[f"LMP-{i:03d}" for i in range(1,7)]
def vigil_body(fail=(),frame=False,summer=False):
    # summer (env_summer prefab): daylight, the street lights are on standby
    def body(t):
        y0=px(200); dy=px(27)
        if frame:
            for r in range(6):
                y=y0+r*dy; t.rectangle([M,y-px(3),M+px(560),y+px(22)],outline=STEEL_L+(255,),width=1)
        else:
            for r,a in enumerate(ASSETS):
                y=y0+r*dy; bad=a in fail
                t.text((M,y),"[FAIL]" if bad else "[ OK ]",font=mono(16),fill=RED if bad else TEAL)
                t.text((M+px(72),y),a,font=mono(16),fill=WHITE)
                t.text((M+px(160),y),"STREET LIGHT",font=mono(16),fill=DIM)
                t.text((M+px(300),y),"OFFLINE - VANDALISM REPORTED" if bad else ("STANDBY - DAYLIGHT" if summer else "ONLINE"),font=mono(16),fill=RED if bad else DIM)
        # event log on the right
        x2=M+px(620); x3=W-M
        t.text((x2,y0-px(28)),"EVENT LOG",font=mono(14,'SemiBold'),fill=YELLOW)
        t.rectangle([x2,y0-px(4),x3,y0+px(160)],outline=STEEL_L+(255,),width=1)
        if not frame:
            lines=[("R01 00:00","SYSTEM ONLINE",DIM),("R01 00:00","ASSET SCAN 6/6 OK",DIM)]
            if fail: lines+= [("R03 01:24",f"{fail[0]} VANDALISM",RED),("R03 01:24","REPAIR QUEUED",YELLOW)]
            if summer: lines+= [("R01 00:00","DAYLIGHT: LIGHTS ON STANDBY",TEAL),("R01 00:00","SUN: NOT A MONITORED ASSET",DIM)]
            for i,(ts,msg,c) in enumerate(lines):
                yy=y0+px(6)+i*px(24); t.text((x2+px(10),yy),ts,font=mono(13,'SemiBold'),fill=DIM); t.text((x2+px(100),yy),msg,font=mono(13),fill=c)
    return body
for name,fail,frame,summer in (("",(),False,False),("_incident",("LMP-002",),False,False),("_frame",(),True,False),("_summer",(),False,True)):
    nf=len(fail)
    right=[("LIVE FEED",TEAL)] if frame else [(f"ASSETS ONLINE  {6-nf:02d}/06",TEAL if not nf else YELLOW),("SYSTEM STATUS: "+("NOMINAL" if not nf else "INCIDENT"),TEAL if not nf else RED)]
    screen("KD-MCS-001","MAP CONTROL PROGRAM","V.I.G.I.L.","VANDALISM INCIDENT & GENERAL INFRASTRUCTURE LOG",
           right,"MONITORED ASSETS",vigil_body(fail,frame,summer),
           ["AUTO-REPAIR SCHEDULED: NEXT ROUND","REPORT ID FORMAT: KD-MCS-001/<TYPE>-<NO>"],
           "EVERYTHING IS LOGGED. EVERYTHING!",f"noclip/kd-mcs-001_vigil{name}_1024x512.png")
print('ok')

# ---------- KD-MCS-001 V.I.G.I.L. screensaver ----------
# The Nonvis eye bounces around the idle screen (DVD style), with a fading trail.
# Needs logos/nonvis-division_logo_icon_1024.png in the working folder.
def vigil_screensaver(out):
    im=Image.new('RGBA',(W,H),(6,9,11,255))
    logo=Image.open('logos/nonvis-division_logo_icon_1024.png').convert('RGBA')
    logo=logo.crop(logo.getchannel('A').getbbox())
    L=px(190); logo=logo.resize((round(logo.width*L/logo.height),L),Image.LANCZOS)
    lum=logo.convert('L'); a=logo.getchannel('A')
    from PIL import ImageChops
    mask=ImageChops.multiply(a,lum.point(lambda v:min(255,60+v)))       # bright lines strong, dark fill faint
    def stamp(layer,x,y,alpha,col):
        sol=Image.new('RGBA',logo.size,col+(255,)); m=mask.point(lambda v:int(v*alpha))
        layer.paste(sol,(x,y),m)
    txt=Image.new('RGBA',(W,H),(0,0,0,0)); t=ImageDraw.Draw(txt)
    # path: drifting from the top-left towards the bottom-right corner
    trail=[(px(250),px(40)),(px(360),px(85)),(px(470),px(130)),(px(580),px(175))]
    for i,(x,y) in enumerate(trail): stamp(txt,x,y,0.10+0.08*i,TEAL)
    stamp(txt,px(690),px(220),1.0,TEAL)
    t.text((M,px(26)),"KD-MCS-001",font=mono(18),fill=YELLOW)
    t.text((M+t.textlength("KD-MCS-001  ",font=mono(18)),px(30)),"V.I.G.I.L.",font=mono(13,'SemiBold'),fill=DIM)
    s_="IDLE 04:04:04"; t.text((W-M-t.textlength(s_,font=mono(13,'SemiBold')),px(30)),s_,font=mono(13,'SemiBold'),fill=DIM)
    t.text((M,px(424)),"SCREEN IDLE. MONITORING IS NOT.",font=mono(20),fill=PINK)
    jw=t.textlength("SCREEN IDLE. MONITORING IS NOT.",font=mono(20))
    t.rectangle([M+jw+px(14),px(426),M+jw+px(26),px(448)],fill=PINK+(255,))
    t.text((M,px(458)),"PRESS ANY KEY TO RESUME.",font=mono(13,'SemiBold'),fill=DIM)
    im=Image.alpha_composite(im,txt.filter(ImageFilter.GaussianBlur(6*S))); im=Image.alpha_composite(im,txt)
    sl=Image.new('L',(W,H),0); sd=ImageDraw.Draw(sl)
    for y in range(0,H,px(3)): sd.line([(0,y),(W,y)],fill=60,width=S)
    dk=Image.new('RGBA',(W,H),(0,0,0,0)); dk.putalpha(sl); im=Image.alpha_composite(im,dk)
    vg=Image.new('L',(W,H),255); ImageDraw.Draw(vg).rounded_rectangle([px(-40),px(-40),W+px(40),H+px(40)],radius=px(220),fill=0)
    vo=Image.new('RGBA',(W,H),(0,0,0,0)); vo.putalpha(vg.filter(ImageFilter.GaussianBlur(70*S)).point(lambda v:int(v*0.8))); im=Image.alpha_composite(im,vo)
    im.resize((1024,512),Image.LANCZOS).convert('RGB').save(out,optimize=True)
vigil_screensaver("noclip/kd-mcs-001_vigil_screensaver_1024x512.png")
