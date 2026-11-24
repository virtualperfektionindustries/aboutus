# Tools

The Python scripts that generate every image in [`../assets/`](../assets/). They need Python 3 and Pillow (`pip install pillow`; the newspaper scripts also use NumPy).

> These scripts grew out of an interactive session, not a build system: they expect to be run from one working folder that contains `fonts/`, the cut photos in `photos/`, `photos2/` … `photos4/`, and empty output folders (`posters/`, `papers/`, `noclip/`, `crates/`, `vpk_brand/`). Paths are relative and some scripts import or `exec` the previous one. Treat them as a working reference rather than a polished tool.

| Script | Output |
| :--- | :--- |
| `brand_logos.py` | the VPK Industries and Nonvis Division logos (`vpk_logos.py`: the three early concepts) |
| `noclip_screens.py` | the monitor screens of A.T.M.O.S., F.O.R.E.C.A.S.T., S.T.R.A.T.O.S. and V.I.G.I.L. |
| `plates.py` | the machine plates |
| `stickers.py` | the die-cut machine stickers |
| `square.py` | the square, material-ready copies in `materials/` (`python3 tools/square.py assets materials`) |
| `door_sign.py`, `emitter_sign.py`, `crates.py` | the NONVIS-001 door sign, the emitter warning, the KD-PX waybill and pictograms |
| `posters.py` … `posters4.py`, `poster_milk.py`, `poster_milk_notice.py`, `poster_notices.py` | the posters and public notices |
| `newspapers.py` … `newspapers5.py` | the newspaper front pages (`newspapers.py` holds the shared layout; `newspapers2.py` adds the photo version) |

**Fonts:** Bebas Neue (SIL OFL, included), Permanent Marker (Apache 2.0, included), JetBrains Mono (SIL OFL), Inter (SIL OFL) and Liberation Serif (SIL OFL). The last three are loaded from the system font folders; install them or change the paths at the top of the scripts.
**Cutting a photo grid:** split the grid image along its white gaps (rows and columns that are almost entirely white) into nine images named `photo_1.png` … `photo_9.png`, left to right, top to bottom.
