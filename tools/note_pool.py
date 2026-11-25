# Daniel K.'s sticky note for the OASIS posters: "Where is the pool?"
# Usage: python3 note_pool.py [out.png]   (run from the working folder that contains fonts/)
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
S = 1024
W, H = 760, 700
note = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(note)
for y in range(H):
    t = y / H; d.line([(0, y), (W, y)], fill=(int(252 - 8*t), int(226 - 18*t), int(92 - 24*t), 255))
d.rectangle([0, 0, W, 80], fill=(240, 212, 80, 255))          # sticky strip
d.polygon([(W, H-110), (W, H), (W-110, H)], fill=(0, 0, 0, 0))  # curled corner
d.polygon([(W, H-110), (W-110, H), (W-96, H-86)], fill=(214, 186, 70, 255))
mk = lambda s: ImageFont.truetype('fonts/PermanentMarker-Regular.ttf', s)
ink, red = (28, 36, 70, 255), (170, 30, 24, 255)
d.text((60, 130), "WHERE IS", font=mk(118), fill=ink)
d.text((60, 290), "THE POOL?", font=mk(118), fill=ink)
d.line([(70, 450), (640, 438)], fill=red, width=12)
d.text((330, 500), "- Daniel K.", font=mk(64), fill=ink)
note = note.rotate(4, resample=Image.BICUBIC, expand=True)
out = Image.new('RGBA', (S, S), (0, 0, 0, 0))
x, y = (S - note.width)//2, (S - note.height)//2
shadow = Image.new('RGBA', (S, S), (0, 0, 0, 0))
shadow.paste((0, 0, 0, 110), (x + 14, y + 20), note.getchannel('A'))
out = Image.alpha_composite(out, shadow.filter(ImageFilter.GaussianBlur(14)))
out.alpha_composite(note, (x, y))
out.save(sys.argv[1] if len(sys.argv) > 1 else 'note_where-is-the-pool_1024.png', optimize=True)
