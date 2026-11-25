"""Square, power-of-two copies of every asset for the CS2 Material Editor.

Usage: python3 tools/square.py assets materials

For each <src>/<folder>/<name>.png it writes <dst>/<folder>/<name>_color.png:
the image scaled so its longer side fills a power-of-two square, centred,
with the rest of the canvas transparent.

Transparency masks (white = image, black = transparent) are shared where possible,
in <dst>/masks/:
- An opaque image that only needed padding gets the mask of its size:
  masks/mask_<w>x<h>_<side>.png (every 1024x1536 poster uses the same one).
- An image with its own transparency (stickers, pictograms) gets
  <dst>/<folder>/<name>_trans.png, unless several of them have exactly the same
  mask: then they share masks/mask_<common name prefix>_<side>.png.
- A square, fully opaque image needs no mask.
The script prints which mask each image uses; materials/README.md lists them.
"""
import sys, os, glob, re, hashlib
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
mask_dir = os.path.join(dst, 'masks')
os.makedirs(mask_dir, exist_ok=True)

def pow2(n):
    p = 1
    while p < n: p *= 2
    return p

def mask_img(alpha):
    return Image.merge('RGB', (alpha, alpha, alpha))

# already material-ready at their own power-of-two size, written by tools/pictogram_sheets.py
SKIP = ('kdpx_pictograms_',)

rows = []          # (folder, name, mask path or None)
own = {}           # hash -> [(folder, name, side, alpha)]
for f in sorted(glob.glob(os.path.join(src, '*', '*.png'))):
    sub = os.path.basename(os.path.dirname(f)); name = os.path.splitext(os.path.basename(f))[0]
    if name.startswith(SKIP): continue
    im = Image.open(f).convert('RGBA'); w0, h0 = im.size
    own_alpha = im.getchannel('A').getextrema()[0] < 255
    side = pow2(max(w0, h0)); k = side / max(w0, h0)
    w, h = w0, h0
    if k != 1: im = im.resize((round(w0*k), round(h0*k)), Image.LANCZOS); w, h = im.size
    canvas = Image.new('RGBA', (side, side), (0, 0, 0, 0))
    canvas.alpha_composite(im, ((side - w)//2, (side - h)//2))
    out = os.path.join(dst, sub); os.makedirs(out, exist_ok=True)
    alpha = canvas.getchannel('A')
    padded = alpha.getextrema()[0] < 255
    if not padded:
        canvas.convert('RGB').save(os.path.join(out, name + '_color.png'), optimize=True)
        rows.append((sub, name, None)); continue
    canvas.save(os.path.join(out, name + '_color.png'), optimize=True)
    if not own_alpha:
        m = os.path.join(mask_dir, f'mask_{w0}x{h0}_{side}.png')
        if not os.path.exists(m): mask_img(alpha).save(m, optimize=True)
        rows.append((sub, name, m))
    else:
        own.setdefault(hashlib.md5(alpha.tobytes()).hexdigest(), []).append((sub, name, side, alpha))

for group in own.values():
    if len(group) == 1:
        sub, name, side, alpha = group[0]
        m = os.path.join(dst, sub, name + '_trans.png')
    else:
        prefix = os.path.commonprefix([g[1] for g in group]).rstrip('_-')
        prefix = re.sub(r'_\d+$', '', prefix) or 'shared'
        sub, name, side, alpha = group[0]
        m = os.path.join(mask_dir, f'mask_{prefix}_{side}.png')
    mask_img(alpha).save(m, optimize=True)
    for sub, name, side, alpha in group:
        old = os.path.join(dst, sub, name + '_trans.png')
        if len(group) > 1 and os.path.exists(old): os.remove(old)
        rows.append((sub, name, m))

for sub, name, m in sorted(rows):
    print(f'{sub}/{name}_color.png', '->', os.path.relpath(m, dst) if m else '(no mask)')
