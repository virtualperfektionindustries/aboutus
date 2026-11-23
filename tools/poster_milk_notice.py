src=open('tools/posters.py').read(); exec(src[:src.index('# 1. RAIN IS A PRIVILEGE')])
PAPER=(232,226,208); INK=NAVY
im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
d.rectangle([px(28),px(28),W-px(28),H-px(28)],outline=INK,width=px(6))
d.rectangle([px(28),px(28),W-px(28),px(130)],fill=RED)
d.text((W//2,px(80)),"PUBLIC NOTICE",font=bebas(84),fill=PAPER,anchor='mm')
d.text((W//2,px(160)),"THE GREAT GLOBAL",font=bebas(110),fill=INK,anchor='mt')
d.text((W//2,px(262)),"MILK CRISIS",font=bebas(170),fill=INK,anchor='mt')
# photo of the first day of the rush
ph=Image.open('photos2/photo_1.png').convert('L'); bx0,by0,bx1,by1=px(70),px(440),W-px(70),px(820)
w,h=bx1-bx0,by1-by0; r=max(w/ph.width,h/ph.height); ph=ph.resize((int(ph.width*r)+1,int(ph.height*r)+1),Image.LANCZOS)
l=(ph.width-w)//2; t=(ph.height-h)//2; ph=ph.crop((l,t,l+w,t+h)).point(lambda v:int(30+v*0.8))
scr=Image.new('L',(w,h),255); sd=ImageDraw.Draw(scr)
for yy in range(0,h,px(4)):
    for xx in range(0,w,px(4)): sd.ellipse([xx+1,yy+1,xx+px(4)-1,yy+px(4)-1],fill=232)
ph=ImageChops.multiply(ph,scr)
im.alpha_composite(Image.merge('RGB',[ph.point(lambda v,c=c:int(c*v/255)) for c in PAPER]).convert('RGBA'),(bx0,by0)); d=ImageDraw.Draw(im)
d.rectangle([bx0,by0,bx1,by1],outline=INK,width=px(4))
# two columns
def col(x,title,items,y=px(850)):
    d.text((x,y),title,font=bebas(46),fill=RED); y+=px(56)
    for it in items:
        d.text((x,y),"•",font=mono(18),fill=INK)
        lines=[];cur=""
        for wd in it.split():
            tt=(cur+" "+wd).strip()
            if d.textlength(tt,font=mono(17,'SemiBold'))<=px(380): cur=tt
            else: lines.append(cur); cur=wd
        lines.append(cur)
        for ln in lines: d.text((x+px(24),y),ln,font=mono(17,'SemiBold'),fill=INK); y+=px(25)
        y+=px(8)
col(px(80),"WHAT IS HAPPENING",["Demand for milk has doubled. Then doubled again.","Shops are out of milk. Shelves are restocked every hour.","Nobody knows why everyone wants milk.","Experts are looking into it."])
col(px(530),"WHAT YOU CAN DO",["Take one glass per person per day.","Do not hoard milk. Do not return in disguise.","Report all milk hoarding.","Stay calm. Drink slowly."])
# VPK statement box
sx0,sy0,sx1,sy1=px(80),px(1160),W-px(80),px(1340)
d.rectangle([sx0,sy0,sx1,sy1],fill=INK)
d.text((sx0+px(24),sy0+px(20)),"A STATEMENT FROM VPK INDUSTRIES",font=bebas(40),fill=YEL)
d.text((sx0+px(24),sy0+px(72)),"The crisis began shortly after the invention of KD-PX.",font=mono(19),fill=PAPER)
d.text((sx0+px(24),sy0+px(102)),"This is a coincidence.",font=mono(19),fill=PAPER)
d.text((sx0+px(24),sy0+px(138)),"VPK INDUSTRIES HAD NOTHING TO DO WITH IT.",font=mono(21),fill=YEL)
# footer
y=H-px(150); d.line([(px(70),y),(W-px(70),y)],fill=INK,width=px(2))
im.alpha_composite(vpk_icon(1024,NAVY).resize((px(84),px(84)),Image.LANCZOS),(px(70),y+px(26))); d=ImageDraw.Draw(im)
d.text((px(172),y+px(30)),"VPK INDUSTRIES",font=bebas(44),fill=INK); d.text((px(172),y+px(78)),"WE OWN THE WORLD. LITERALLY.",font=mono(17),fill=RED)
d.text((W-px(70),y+px(52)),"ISSUED IN THE PUBLIC INTEREST",font=mono(15,'SemiBold'),fill=INK,anchor='rm')
GRIME=0.08
finish(im,'poster_milk-crisis-public-notice_1024x1536.png')
print('ok')
