import math,random
src=open('tools/posters.py').read(); exec(src[:src.index('# 1. RAIN IS A PRIVILEGE')])
s2=open('tools/posters2.py').read(); exec(s2[s2.index('def stamp('):s2.index('# 7. DO NOT KICK')])
PAPER=(226,222,210); INK=NAVY
def paper_footer(im,d):
    y=H-px(150); d.line([(px(70),y),(W-px(70),y)],fill=INK,width=px(2))
    im.alpha_composite(vpk_icon(1024,NAVY).resize((px(84),px(84)),Image.LANCZOS),(px(70),y+px(26))); d=ImageDraw.Draw(im)
    d.text((px(172),y+px(30)),"VPK INDUSTRIES",font=bebas(44),fill=INK); d.text((px(172),y+px(78)),"WE OWN THE WORLD. LITERALLY.",font=mono(17),fill=RED)
    return d
def diamond(d,cx,cy,r,sym):
    d.polygon([(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)],fill=WHITE,outline=RED)
    for k in range(px(10)): d.polygon([(cx,cy-r+k),(cx+r-k,cy),(cx,cy+r-k),(cx-r+k,cy)],outline=RED)
    if sym=='Kd': d.text((cx,cy+px(2)),sym,font=inter(int(r/S*0.55)),fill=(20,20,20),anchor='mm')
    elif sym: d.text((cx,cy+px(4)),sym,font=bebas(int(r/S*0.95)),fill=(20,20,20),anchor='mm')

# 19. KDANIUM SAFETY DATA SHEET
im,d=base(PAPER); d.rectangle([px(28),px(28),W-px(28),H-px(28)],outline=INK,width=px(4))
d.text((px(90),px(80)),"VPK INDUSTRIES · NONVIS DIVISION · KD-PX SERIES",font=mono(18),fill=INK)
d.text((px(90),px(115)),"SAFETY DATA SHEET",font=bebas(104),fill=INK)
d.rectangle([W-px(260),px(80),W-px(90),px(250)],fill=WHITE,outline=YEL,width=px(8))
d.text((W-px(245),px(92)),"404",font=mono(22),fill=INK)
d.text((W-px(175),px(175)),"Kd",font=inter(84),fill=INK,anchor='mm')
d.text((px(90),px(225)),"KDANIUM (Kd) · SYNTHETIC ELEMENT · REV. 404",font=mono(20,'SemiBold'),fill=RED)
d.line([(px(90),px(275)),(W-px(90),px(275))],fill=INK,width=px(3))
for i,sym in enumerate(["!","","Kd","?"]): diamond(d,px(190)+i*px(215),px(375),px(80),sym)
dx,dy,dr=px(190)+px(215),px(395),px(26)
d.ellipse([dx-dr,dy-dr,dx+dr,dy+dr],fill=(20,20,20)); d.polygon([(dx-dr*0.92,dy-dr*0.38),(dx,dy-dr*2.4),(dx+dr*0.92,dy-dr*0.38)],fill=(20,20,20))
sections=[("1. IDENTIFICATION","Product: Kdanium. Use: rain, snow, fire, smoke, anything. Supplier: VPK Industries."),
          ("2. HAZARDS","None.* Perfection is non-hazardous by definition."),
          ("3. COMPOSITION","Kdanium 100%. Perfection 100%. Other: classified."),
          ("4. FIRST AID","Skin: rinse with plain water (not Kd₂O). Inhalation: move to the playable area. Ingestion: you were told."),
          ("5. HANDLING","Wear gloves. Do not touch, inhale, lick or drink. Do not look at it for too long."),
          ("6. EXPOSURE EFFECTS*","Skin irritation, teal glow, headache, slowed reflexes, phantom footsteps, crosshair drift, deranking."),
          ("7. DISPOSAL","Noclip it into the void. Do not dispose of in the playable area.")]
y=px(490); bf=mono(17,'SemiBold'); tf=mono(17,'Regular')
def wrap(text,font,maxw):
    words=text.split(); lines=[]; cur=""
    for w_ in words:
        t=(cur+" "+w_).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w_
    lines.append(cur); return lines
for head,body in sections:
    d.text((px(90),y),head,font=bf,fill=RED if '*' in head or head.startswith('2') else INK); y+=px(30)
    for l in wrap(body,tf,W-px(200)): d.text((px(110),y),l,font=tf,fill=INK); y+=px(27)
    y+=px(16)
d.text((px(90),y+px(6)),"* Side effects are rare, mild and entirely your fault.",font=mono(16,'SemiBold'),fill=RED)
im=stamp(im,"APPROVED",W-px(260),px(1275),80,-12,(40,110,60)); d=ImageDraw.Draw(im)
d=paper_footer(im,d)
GRIME=0.05
finish(im,'poster_kdanium-safety-data-sheet_1024x1536.png')
GRIME=0.14

# 20. MISSED THAT SHOT?
im,d=base(NAVY2)
cx,cy=W//2,px(470)
# target dummy silhouette, crosshair a little behind it
d.ellipse([cx+px(40),cy-px(210),cx+px(160),cy-px(90)],fill=(90,104,134))
d.rounded_rectangle([cx+px(10),cy-px(85),cx+px(190),cy+px(200)],radius=px(40),fill=(90,104,134))
ox=cx-px(120); oy=cy-px(150)
for a_,b_ in (((ox-px(70),oy),(ox-px(18),oy)),((ox+px(18),oy),(ox+px(70),oy)),((ox,oy-px(70)),(ox,oy-px(18))),((ox,oy+px(18)),(ox,oy+px(70)))):
    d.line([a_,b_],fill=TEAL,width=px(10))
d.line([(ox+px(80),oy),(cx+px(40),cy-px(150))],fill=YEL,width=px(3))
d.text((ox-px(80),oy+px(115)),"+20 ms",font=mono(34),fill=YEL,anchor='lm')
headline(d,["MISSED THAT","SHOT?"],px(800),WHITE,150)
d.text((W//2,px(1070)),"IT WASN'T YOUR FAULT.",font=mono(30),fill=TEAL,anchor='mt')
d.text((W//2,px(1115)),"IT WASN'T OURS EITHER.*",font=mono(30),fill=YEL,anchor='mt')
d.text((W//2,px(1190)),"* NO LINK HAS BEEN PROVEN BETWEEN KD-PX PRODUCTS AND SLOWED REFLEXES.",font=mono(14,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1215)),"VPK INDUSTRIES IS NOT RESPONSIBLE FOR LOST AIM DUELS.",font=mono(14,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"PUBLIC NOTICE")
finish(im,'poster_missed-that-shot_1024x1536.png')

# 21. FEELING THE URGE? (AWP on an eco round)
im,d=base(NAVY2)
# a buy menu tile instead of a drawing of the rifle
PANEL=(30,40,64); PANEL_L=(44,58,90)
d.rounded_rectangle([px(140),px(170),W-px(140),px(740)],radius=px(18),fill=PANEL,outline=GREY,width=px(3))
d.text((px(180),px(200)),"BUY MENU · SNIPER RIFLES",font=mono(20,'SemiBold'),fill=GREY)
d.text((W-px(180),px(200)),"ROUND 2 · ECO",font=mono(20,'SemiBold'),fill=RED,anchor='ra')
tx0,ty0,tx1,ty1=px(200),px(260),W-px(200),px(560)
d.rounded_rectangle([tx0,ty0,tx1,ty1],radius=px(14),fill=PANEL_L,outline=YEL,width=px(6))
# scope reticle as the rifle's icon
sx,sy,sr=tx0+px(150),(ty0+ty1)//2,px(95)
d.ellipse([sx-sr,sy-sr,sx+sr,sy+sr],outline=WHITE,width=px(8))
d.line([(sx-sr,sy),(sx+sr,sy)],fill=WHITE,width=px(4)); d.line([(sx,sy-sr),(sx,sy+sr)],fill=WHITE,width=px(4))
d.ellipse([sx-px(8),sy-px(8),sx+px(8),sy+px(8)],fill=RED)
d.text((tx0+px(300),ty0+px(60)),"AWP",font=bebas(150),fill=WHITE)
d.text((tx0+px(306),ty0+px(220)),"$4,750",font=mono(40),fill=YEL)
d.text((px(200),px(600)),"YOUR MONEY:",font=mono(26),fill=GREY); d.text((W-px(200),px(600)),"$1,400",font=mono(34),fill=RED,anchor='ra')
d.text((W//2,px(680)),"INSUFFICIENT FUNDS. BUY ANYWAY?",font=mono(24),fill=RED,anchor='mm')
# mouse cursor clicking the tile
cx_,cy_=tx1-px(110),ty1-px(80)
d.polygon([(cx_,cy_),(cx_,cy_+px(110)),(cx_+px(28),cy_+px(84)),(cx_+px(48),cy_+px(128)),(cx_+px(66),cy_+px(120)),(cx_+px(46),cy_+px(76)),(cx_+px(82),cy_+px(76))],fill=WHITE,outline=NAVY2)
for a_ in (200,235,270):
    r_=math.radians(a_); d.line([(cx_+math.cos(r_)*px(22),cy_+math.sin(r_)*px(22)),(cx_+math.cos(r_)*px(50),cy_+math.sin(r_)*px(50))],fill=YEL,width=px(5))
headline(d,["FEELING","THE URGE?"],px(800),WHITE,150)
d.text((W//2,px(1070)),"BUYING AN AWP ON AN ECO ROUND",font=mono(26),fill=TEAL,anchor='mt')
d.text((W//2,px(1110)),"IS A COMPLETELY NORMAL DECISION.*",font=mono(26),fill=TEAL,anchor='mt')
d.text((W//2,px(1190)),"* THIS URGE IS NOT RELATED TO DYNASNOW™ CONSUMPTION. PROBABLY.",font=mono(14,'SemiBold'),fill=GREY,anchor='mt')
d.text((W//2,px(1215)),"IF THE URGE PERSISTS, ASK YOUR TEAMMATES. THEY WILL HAVE OPINIONS.",font=mono(14,'SemiBold'),fill=GREY,anchor='mt')
d=footer(im,d,"PUBLIC NOTICE")
finish(im,'poster_feeling-the-urge_1024x1536.png')
print('ok')
