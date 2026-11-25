# The six KD-PX hazard pictograms as one texture: a row (6x1) and a grid (3x2).
# Usage: python3 tools/pictogram_sheets.py   (run from the repo root)
# Writes the sheets to assets/signs/ and the material-ready _color/_trans pair to materials/signs/.
# Both sheets are already power-of-two (4096x512 and 2048x1024), so they are not squared.
import os
from PIL import Image
ORDER = ['kdanium', 'weather', 'health-hazard', 'radioactive', 'cryogenic', 'explosive']
icons = []
for n in ORDER:
    im = Image.open(f'assets/signs/kdpx_pictogram_{n}_512.png').convert('RGBA')
    icons.append(im.crop(im.getchannel('A').getbbox()))

def sheet(cols, rows, W, H, name):
    out = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    cw, ch = W / cols, H / rows
    for i, ic in enumerate(icons):
        c, r = i % cols, i // cols
        out.alpha_composite(ic, (round(c*cw + (cw - ic.width)/2), round(r*ch + (ch - ic.height)/2)))
    out.save(f'assets/signs/{name}.png', optimize=True)
    os.makedirs('materials/signs', exist_ok=True)
    out.save(f'materials/signs/{name}_color.png', optimize=True)
    a = out.getchannel('A')
    Image.merge('RGB', (a, a, a)).save(f'materials/signs/{name}_trans.png', optimize=True)

sheet(6, 1, 4096, 512, 'kdpx_pictograms_row_4096x512')
sheet(3, 2, 2048, 1024, 'kdpx_pictograms_grid_2048x1024')
