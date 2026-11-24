import sys,os,glob
from PIL import Image
src,dst=sys.argv[1],sys.argv[2]
def pow2(n):
    p=1
    while p<n: p*=2
    return p
rows=[]
for f in sorted(glob.glob(os.path.join(src,'*','*.png'))):
    sub=os.path.basename(os.path.dirname(f)); name=os.path.splitext(os.path.basename(f))[0]
    im=Image.open(f).convert('RGBA'); w,h=im.size; side=pow2(max(w,h))
    out=os.path.join(dst,sub); os.makedirs(out,exist_ok=True)
    k=side/max(w,h)
    if k!=1: im=im.resize((round(w*k),round(h*k)),Image.LANCZOS); w,h=im.size
    canvas=Image.new('RGBA',(side,side),(0,0,0,0)); canvas.alpha_composite(im,((side-w)//2,(side-h)//2))
    alpha=canvas.getchannel('A'); has_trans=alpha.getextrema()[0]<255
    if has_trans:
        # colour: fill transparent pixels with the nearest edge colour would be ideal; plain black keeps it simple
        canvas.save(os.path.join(out,name+'_color.png'),optimize=True)
        mask=alpha.point(lambda v:255 if v>127 else 0) if False else alpha
        Image.merge('RGB',(mask,mask,mask)).save(os.path.join(out,name+'_trans.png'),optimize=True)
    else:
        canvas.convert('RGB').save(os.path.join(out,name+'_color.png'),optimize=True)
    rows.append((sub,name,w,h,side,has_trans))
for r in rows: print(*r)
