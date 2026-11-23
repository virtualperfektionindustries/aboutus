import math,random,textwrap
from PIL import Image,ImageDraw,ImageFilter,ImageFont,ImageChops
S=2; W,H=1024*S,1448*S
PAPER=(232,226,208); INK=(28,26,24); GREYI=(120,114,104); RED=(150,30,24)
def px(v): return int(v*S)
def serif(sz,bold=False): return ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-'+('Bold' if bold else 'Regular')+'.ttf',int(sz*S))
def cond(sz): return ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf',int(sz*S))
def bebas(sz): return ImageFont.truetype('fonts/BebasNeue-Regular.ttf',int(sz*S))
def inter(sz,w='ExtraBold'): return ImageFont.truetype('/usr/share/fonts/opentype/inter/Inter-'+w+'.otf',int(sz*S))
M=px(60)
def wraptext(d,text,font,x,y,w,lh,col=INK):
    words=text.split(); line=""
    for wd in words:
        t=(line+" "+wd).strip()
        if d.textlength(t,font=font)<=w: line=t
        else: d.text((x,y),line,font=font,fill=col); y+=lh; line=wd
    if line: d.text((x,y),line,font=font,fill=col); y+=lh
    return y
def filler(d,x,y,w,y_end,seed):
    r=random.Random(seed)
    while y<y_end:
        lw=w if r.random()>0.12 else int(w*r.uniform(0.3,0.8))
        d.line([(x,y+px(7)),(x+lw,y+px(7))],fill=(150,144,132),width=px(5)); y+=px(17)
        if r.random()<0.08: y+=px(14)
def headline(d,text,y,size):
    f=cond(size)
    while d.textlength(text,font=f)>W-2*M: size-=2; f=cond(size)
    d.text((W//2,y),text,font=f,fill=INK,anchor='mt')
def masthead(d,name,motto,price):
    d.text((W//2,px(40)),name,font=serif(92,True),fill=INK,anchor='mt')
    d.line([(M,px(160)),(W-M,px(160))],fill=INK,width=px(5)); d.line([(M,px(168)),(W-M,px(168))],fill=INK,width=px(2))
    d.text((M,px(180)),"VOL. 404 · NO. 1",font=serif(17),fill=INK)
    d.text((W//2,px(180)),motto,font=serif(17),fill=INK,anchor='mt')
    d.text((W-M,px(180)),price,font=serif(17),fill=INK,anchor='ra')
    d.line([(M,px(212)),(W-M,px(212))],fill=INK,width=px(2))
def halftone_old(img,box):
    # printed photo: greyscale, slightly soft, with a fine dot screen
    x0,y0,x1,y1=box; g=img.crop(box).convert('L').filter(ImageFilter.GaussianBlur(px(1)))
    w,h=x1-x0,y1-y0; scr=Image.new('L',(w,h),255); sd=ImageDraw.Draw(scr); st=px(5)
    for y in range(0,h,st):
        for x in range(0,w,st): sd.ellipse([x+px(1),y+px(1),x+st-px(1),y+st-px(1)],fill=225)
    g=ImageChops.multiply(g,scr)
    tint=Image.merge('RGB',[g.point(lambda v,c=c:int(c*v/255)) for c in PAPER]).convert('RGBA')
    img.alpha_composite(tint,(x0,y0))
    ImageDraw.Draw(img).rectangle(box,outline=INK,width=px(3))
def finish(im,name):
    n=Image.effect_noise((W//2,H//2),20).resize((W,H),Image.BICUBIC)
    g=Image.new('RGBA',(W,H),(255,255,255,0)); g.putalpha(n.point(lambda v:max(0,v-128)//3)); im=Image.alpha_composite(im,g)
    gr=Image.effect_noise((W//64,H//64),70).resize((W,H),Image.BICUBIC).filter(ImageFilter.GaussianBlur(px(24))).point(lambda v:max(0,v-140)*3)
    go=Image.new('RGBA',(W,H),(120,90,40,0)); go.putalpha(gr.point(lambda v:int(v*0.18))); im=Image.alpha_composite(im,go)
    # a fold line in the middle
    fl=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(fl).line([(0,H//2),(W,H//2)],fill=(0,0,0,40),width=px(3)); im=Image.alpha_composite(im,fl.filter(ImageFilter.GaussianBlur(px(3))))
    im.resize((1024,1448),Image.LANCZOS).convert('RGB').save('papers/'+name,optimize=True)
def body_columns(d,y,lead,seed,y_end=None):
    y_end=y_end or H-px(70); cw=(W-2*M-px(40))//3
    for c in range(3):
        x=M+c*(cw+px(20))
        yy=y
        if c==0: yy=wraptext(d,lead,serif(17),x,yy,cw,px(24))+px(10)
        filler(d,x,yy,cw,y_end,seed+c)
        if c<2: d.line([(x+cw+px(10),y),(x+cw+px(10),y_end)],fill=GREYI,width=px(1))


def photo_box(img,box,path,top=False):
    x0,y0,x1,y1=box; w,h=x1-x0,y1-y0
    p=Image.open(path).convert('L'); r=max(w/p.width,h/p.height)
    p=p.resize((int(p.width*r)+1,int(p.height*r)+1),Image.LANCZOS)
    l=(p.width-w)//2; t=(p.height-h) if top=='bottom' else (0 if top else (p.height-h)//2); p=p.crop((l,t,l+w,t+h))
    p=p.filter(ImageFilter.UnsharpMask(px(2),80,2))
    # newspaper print: lower contrast, lifted blacks, fine dot screen
    p=p.point(lambda v:int(28+v*0.80))
    scr=Image.new('L',(w,h),255); sd=ImageDraw.Draw(scr); st=px(4)
    for yy in range(0,h,st):
        for xx in range(0,w,st): sd.ellipse([xx+px(0.6),yy+px(0.6),xx+st-px(0.6),yy+st-px(0.6)],fill=232)
    p=ImageChops.multiply(p,scr)
    tint=Image.merge('RGB',[p.point(lambda v,c=c:int(c*v/255)) for c in PAPER]).convert('RGBA')
    img.alpha_composite(tint,(x0,y0)); ImageDraw.Draw(img).rectangle(box,outline=INK,width=px(2))

def paper(fname,name,motto,price,no,head_,sub,photo,caption,lead,seed,side=None,top=False):
    im=Image.new('RGBA',(W,H),PAPER+(255,)); d=ImageDraw.Draw(im)
    masthead(d,name,motto,price)
    d.rectangle([M,px(180),M+px(240),px(205)],fill=PAPER)
    d.text((M,px(180)),f"VOL. 404 \u00b7 NO. {no}",font=serif(17),fill=INK)
    headline(d,head_,px(232),84)
    sz=20
    while d.textlength(sub,font=serif(sz))>W-2*M: sz-=1
    d.text((W//2,px(340)),sub,font=serif(sz),fill=INK,anchor='mt')
    box=(M,px(400),px(640) if side else W-M,px(860))
    photo_box(im,box,photo,top); d=ImageDraw.Draw(im)
    if side:
        sx0,sy0,sx1,sy1=px(670),px(400),W-M,px(860)
        d.rectangle([sx0,sy0,sx1,sy1],outline=INK,width=px(4)); d.rectangle([sx0,sy0,sx1,sy0+px(50)],fill=INK)
        d.text(((sx0+sx1)//2,sy0+px(25)),"ALSO TODAY",font=serif(20,True),fill=PAPER,anchor='mm')
        d.text((sx0+px(20),sy0+px(70)),side[0],font=cond(44),fill=INK)
        d.text((sx0+px(20),sy0+px(122)),side[1],font=cond(44),fill=RED)
        wraptext(d,side[2],serif(16),sx0+px(20),sy0+px(190),sx1-sx0-px(40),px(23))
    wraptext(d,caption,serif(15),M,px(872),W-2*M,px(20),GREYI)
    body_columns(d,px(925),lead,seed)
    finish(im,fname)

P='photos/photo_{}.png'
paper('newspaper_daily-pint_milk-overtakes-gold_1024x1448.png',"The Daily Pint","\u201cALL THE NEWS THAT'S FIT TO DRINK\u201d","PRICE: 1 GLASS",1,
 "MILK OVERTAKES GOLD","Central banks sell reserves \u00b7 currencies re-pegged to the pint \u00b7 \u201cGold is just shiny milk now,\u201d says analyst",P.format(1),
 "A glass of milk rests on a national gold reserve. Bank staff say the gold is now \u201cmostly decorative.\u201d",
 "THE BOVINE RESERVE \u2014 In a historic move, central banks around the world sold their gold to buy milk on Tuesday. The Bovine Reserve raised its base rate to 3.5 percent cream. Asked about the cause of the shortage, a VPK Industries spokesperson described the timing of the crisis as \u201ca curiosity\u201d and declined to comment further.",1)
paper('newspaper_dairy-herald_soft-drinks-go-flat_1024x1448.png',"The Dairy Herald","EST. BEFORE THE CRISIS","2 PINTS",1,
 "SOFT DRINKS GO FLAT","Fizzy giants file for bankruptcy \u00b7 survivors rebrand as dairies \u00b7 \u201cFizzy milk\u201d trial ends in tears",P.format(2),
 "Empty soft drink shelves, as shoppers queue for the dairy section. The last bottles were left where they fell.",
 "BUSINESS \u2014 Demand for soft drinks fell to zero this week as consumers worldwide switched to milk. Most manufacturers have closed their factories. One brand attempted a carbonated milk drink; its launch event was described by guests as \u201cmemorable, in a bad way.\u201d VPK Industries said it was \u201csorry for their loss\u201d and \u201cnot involved.\u201d",2)
paper('newspaper_udder-times_great-fridge-heist_1024x1448.png',"The Udder Times","LATE EDITION","1/2 PINT",1,
 "GREAT FRIDGE HEIST","Largest milk robbery in history \u00b7 no suspects \u00b7 single crate marked \u201cKD-PX\u201d found at scene",P.format(3),
 "The national milk reserve after the robbery. The crate in the foreground was \u201calmost certainly placed there by someone else.\u201d",
 "CRIME \u2014 Thieves emptied the national milk reserve overnight and escaped in an unmarked refrigerated truck. Police have no suspects. The only evidence is a single crate labelled \u201cKD-PX\u201d. A VPK Industries spokesperson called this \u201ca coincidence\u201d and asked reporters to \u201cplease stop asking about the crate.\u201d",3)
paper('newspaper_evening-moo_long-may-she-reign_1024x1448.png',"The Evening Moo","SPECIAL CORONATION ISSUE","FREE (WITH PURCHASE OF MILK)",1,
 "LONG MAY SHE REIGN","Bessie IV crowned in historic ceremony \u00b7 pastures declared sacred \u00b7 crowds weep, then drink milk",P.format(4),
 "Her Majesty Bessie IV on the sacred pasture, moments after the coronation.",
 "ROYAL NEWS \u2014 Thousands gathered on the sacred pasture as Bessie IV was crowned the first bovine monarch in history. The coronation was attended by every signatory of the Lactose Accords and by VPK Industries, \u201cas an observer.\u201d Her first decree raised the national milk ration to two glasses a day. Long may she reign.",4,
 side=("LACTOKD\u2122","RECALLED","VPK Industries has discontinued its synthetic milk after every glass sold created demand for two more. The company calls it \u201ca success the world was not ready for.\u201d A \u201creduced craving\u201d formula made things worse."))
paper('newspaper_daily-pint_lactose-accords-signed_1024x1448.png',"The Daily Pint","\u201cALL THE NEWS THAT'S FIT TO DRINK\u201d","PRICE: 1 GLASS",2,
 "LACTOSE ACCORDS SIGNED","Historic treaty on milk distribution \u00b7 every signatory receives one cow \u00b7 VPK attends \u201cas an observer\u201d",P.format(5),
 "Delegates sign the Lactose Accords, each accompanied by the cow their country received under the treaty.",
 "DIPLOMACY \u2014 After eleven days of negotiations, world leaders signed the Lactose Accords, the first international treaty on the fair distribution of milk. Each signatory country received one cow. VPK Industries attended as an observer and, according to delegates, \u201cobserved very carefully\u201d.",5)
paper('newspaper_udder-times_oat-milk-rebellion_1024x1448.png',"The Udder Times","MORNING EDITION","1/2 PINT",2,
 "OAT MILK REBELLION ENDS","Plant-based protesters disperse peacefully \u00b7 \u201cIt just isn't the same,\u201d admits leader",P.format(6),
 "Oat milk supporters face police on the high street. The spilled milk was later found to be real milk.",
 "CITY \u2014 The so-called Oat Milk Rebellion came to a quiet end on Saturday, after protesters admitted that plant-based milk does not satisfy the cravings. \u201cWe tried,\u201d said one, holding an empty carton. Asked about the cravings, VPK Industries said it \u201cdoes not know where they come from\u201d.",6)
paper('newspaper_dairy-herald_bovine-reserve-raises-rate_1024x1448.png',"The Dairy Herald","FINANCE SPECIAL","2 PINTS",2,
 "RATE RAISED TO 4% CREAM","Bovine Reserve acts on milk inflation \u00b7 cream futures \u201conly go up\u201d \u00b7 markets stay calm, then drink milk",P.format(7),
 "The governor of the Bovine Reserve announces the new base rate. The portrait behind him has hung in the building since the crisis began.",
 "MARKETS \u2014 The Bovine Reserve raised its base rate to four percent cream on Thursday, citing \u201cpersistent milk inflation\u201d. A litre now costs more than a month's rent in most capitals. Analysts expect cream futures to keep rising, as they have every day since the start of the crisis.",7)
paper('newspaper_evening-moo_milk-rationed_1024x1448.png',"The Evening Moo","EVENING EDITION","FREE (WITH PURCHASE OF MILK)",2,
 "MILK RATIONED","One glass per person per day \u00b7 queues stretch for blocks \u00b7 officials warn against \u201cdisguises\u201d",P.format(8),
 "Citizens queue for their daily glass. Several were later found to be the same person in different hats.",
 "NATIONAL \u2014 From Monday, every citizen is entitled to one glass of milk per day. Shops report queues stretching for several blocks, and officials have warned against returning in disguise. VPK Industries welcomed the measure and said it \u201cfully supports a normal amount of milk\u201d.",8)
paper('newspaper_daily-pint_vpk-denies-everything_1024x1448.png',"The Daily Pint","\u201cALL THE NEWS THAT'S FIT TO DRINK\u201d","PRICE: 1 GLASS",3,
 "VPK DENIES EVERYTHING","\u201cA coincidence,\u201d says spokesperson \u00b7 refuses questions on KD-PX \u00b7 glass of milk seen on podium",P.format(9),
 "A VPK Industries spokesperson ends the press conference after the first question. The glass on the podium was empty by the end.",
 "BUSINESS \u2014 VPK Industries today denied any connection between its KD-PX products and the global milk crisis. \u201cThe crisis began shortly after the invention of KD-PX. This is a coincidence,\u201d said a spokesperson, who then refused all further questions. Asked about the glass of milk on the podium, the company said it was \u201cfor research purposes\u201d.",9)
print('ok')
