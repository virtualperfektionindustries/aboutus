src=open('tools/posters.py').read(); exec(src[:src.index('# 1. RAIN IS A PRIVILEGE')])
PAPER=(232,226,208); INK=NAVY
def wrapl(d,text,font,maxw):
    lines=[];cur=""
    for wd in text.split():
        tt=(cur+" "+wd).strip()
        if d.textlength(tt,font=font)<=maxw: cur=tt
        else: lines.append(cur); cur=wd
    lines.append(cur); return lines
def notice(fname,t1,t2,photo,left,right,statement,punch,no,top=None):
    global GRIME
    im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
    d.rectangle([px(28),px(28),W-px(28),H-px(28)],outline=INK,width=px(6))
    d.rectangle([px(28),px(28),W-px(28),px(130)],fill=RED)
    d.text((W//2,px(80)),"PUBLIC NOTICE",font=bebas(84),fill=PAPER,anchor='mm')
    d.text((W-px(60),px(80)),f"NO. {no} OF 404",font=mono(16,'SemiBold'),fill=PAPER,anchor='rm')
    d.text((W//2,px(160)),t1,font=bebas(110),fill=INK,anchor='mt')
    sz=170
    while d.textlength(t2,font=bebas(sz))>W-px(140): sz-=4
    d.text((W//2,px(262)),t2,font=bebas(sz),fill=INK,anchor='mt')
    ph=Image.open(photo).convert('L'); bx0,by0,bx1,by1=px(70),px(440),W-px(70),px(820)
    w,h=bx1-bx0,by1-by0; r=max(w/ph.width,h/ph.height); ph=ph.resize((int(ph.width*r)+1,int(ph.height*r)+1),Image.LANCZOS)
    l=(ph.width-w)//2; t=0 if top=='top' else ((ph.height-h) if top=='bottom' else (ph.height-h)//2)
    ph=ph.crop((l,t,l+w,t+h)).point(lambda v:int(30+v*0.8))
    scr=Image.new('L',(w,h),255); sd=ImageDraw.Draw(scr)
    for yy in range(0,h,px(4)):
        for xx in range(0,w,px(4)): sd.ellipse([xx+1,yy+1,xx+px(4)-1,yy+px(4)-1],fill=232)
    ph=ImageChops.multiply(ph,scr)
    im.alpha_composite(Image.merge('RGB',[ph.point(lambda v,c=c:int(c*v/255)) for c in PAPER]).convert('RGBA'),(bx0,by0)); d=ImageDraw.Draw(im)
    d.rectangle([bx0,by0,bx1,by1],outline=INK,width=px(4))
    def col(x,title,items,y=px(850)):
        d.text((x,y),title,font=bebas(46),fill=RED); y+=px(56)
        for it in items:
            d.text((x,y),"•",font=mono(18),fill=INK)
            for ln in wrapl(d,it,mono(17,'SemiBold'),px(380)): d.text((x+px(24),y),ln,font=mono(17,'SemiBold'),fill=INK); y+=px(25)
            y+=px(8)
    col(px(80),left[0],left[1]); col(px(530),right[0],right[1])
    sx0,sy0,sx1,sy1=px(80),px(1160),W-px(80),px(1340)
    d.rectangle([sx0,sy0,sx1,sy1],fill=INK)
    d.text((sx0+px(24),sy0+px(20)),"A STATEMENT FROM VPK INDUSTRIES",font=bebas(40),fill=YEL)
    y=sy0+px(72)
    for ln in wrapl(d,statement,mono(19),sx1-sx0-px(48)): d.text((sx0+px(24),y),ln,font=mono(19),fill=PAPER); y+=px(30)
    d.text((sx0+px(24),sy1-px(44)),punch,font=mono(21),fill=YEL)
    y=H-px(150); d.line([(px(70),y),(W-px(70),y)],fill=INK,width=px(2))
    im.alpha_composite(vpk_icon(1024,NAVY).resize((px(84),px(84)),Image.LANCZOS),(px(70),y+px(26))); d=ImageDraw.Draw(im)
    d.text((px(172),y+px(30)),"VPK INDUSTRIES",font=bebas(44),fill=INK); d.text((px(172),y+px(78)),"WE OWN THE WORLD. LITERALLY.",font=mono(17),fill=RED)
    d.text((W-px(70),y+px(52)),"ISSUED IN THE PUBLIC INTEREST",font=mono(15,'SemiBold'),fill=INK,anchor='rm')
    GRIME=0.08
    finish(im,fname)

notice('poster_notice_milk-rationing_1024x1536.png',"NOTICE:","MILK RATIONING",'photos/photo_8.png',
 ("WHAT IS HAPPENING",["Milk is now rationed nationwide.","Every citizen may collect one glass per day.","Queues may stretch for several blocks."]),
 ("WHAT YOU CAN DO",["Bring your own glass.","Queue once. Hats do not count as a new person.","Be patient. Milk is worth the wait."]),
 "VPK Industries did not cause the rationing. VPK Industries has never caused anything.","WE ARE SIMPLY HERE TO HELP.",2)
notice('poster_notice_beware-counterfeit-milk_1024x1536.png',"BEWARE OF","COUNTERFEIT MILK",'photos2/photo_6.png',
 ("HOW TO SPOT IT",["It smells of paint.","It is suspiciously cheap.","It was sold to you from inside a coat."]),
 ("WHAT YOU CAN DO",["Buy only from licensed dairies.","Never taste-test unknown milk.","Report suspicious white liquids."]),
 "VPK Industries does not make counterfeit milk. All VPK milk is 100% synthetic.","THAT IS A COMPLETELY DIFFERENT THING.",7,top='top')
notice('poster_notice_respect-the-cow_1024x1536.png',"PLEASE","RESPECT THE COW",'photos2/photo_3.png',
 ("REMEMBER",["Cows are now sacred in most regions.","Walking in front of a cow is considered rude.","Licensed cows travel with bodyguards."]),
 ("WHAT YOU CAN DO",["Step aside when a cow passes.","Do not touch, pet or milk without a licence.","Bow slightly. It is appreciated."]),
 "VPK Industries did not make cows sacred. They were always sacred. We checked.","WE HAVE THE UTMOST RESPECT FOR COWS.",19,top='top')
notice('poster_notice_soft-drinks-farewell_1024x1536.png',"A FAREWELL TO","SOFT DRINKS",'photos2/photo_5.png',
 ("WHAT HAPPENED",["Nobody wants soft drinks any more.","The last soda plant has closed.","Fizzy milk was attempted. It is not discussed."]),
 ("WHAT YOU CAN DO",["Recycle your last bottles responsibly.","Take a moment to remember the fizz.","Then drink a glass of milk."]),
 "We are sorry for their loss. We were not involved. We were somewhere else at the time.","OUR THOUGHTS ARE WITH THE BUBBLES.",42)
notice('poster_notice_moolah-update_1024x1536.png',"AN UPDATE ON","YOUR MOOLAH",'photos4/photo_5.png',
 ("WHAT HAPPENED",["Moolah took a short break overnight.","Its value is currently zero.","The Udder Ledger is resting: 404, cow not found."]),
 ("WHAT YOU CAN DO",["Do not panic.","Do not try to drink your screen.","Keep your commemorative Non-Fungible Cow."]),
 "VPK Industries did not lose a single pint. Technically, neither did you: you never had any.","NO USE CRYING OVER SPILLED MILK.",128,top='bottom')
notice('poster_notice_frozen-milk-advisory_1024x1536.png',"WINTER","FROZEN MILK ADVISORY",'photos4/photo_9.png',
 ("WHAT IS HAPPENING",["Milk reserves are freezing solid.","Some thermostats show “below 0 °K”.","Experts fear a Second Milk Crisis."]),
 ("WHAT YOU CAN DO",["Keep your milk above freezing.","Use an ice pick only as a last resort.","Do not lick frozen milk. Or DynaSnow™."]),
 "The timing of the freeze and our new winter product is purely seasonal. Winter happens every year.","WE HAD NOTHING TO DO WITH THE WEATHER.",403)
print('ok')
