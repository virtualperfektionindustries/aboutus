# Material-ready textures

Every image from [`../assets/`](../assets/), made square for the CS2 Material Editor:

- The canvas is the next power of two that fits the image (512, 1024 or 2048). The image is scaled so that its longer side fills the canvas, and centred along the shorter side.
- **`<name>_color.png`**: the image. Where the original is not square (or has its own transparency, such as the stickers and pictograms), the rest of the canvas is transparent.
- **Masks** (white where the image is, black where it is transparent): use them as the **Translucency** (or Alpha Test) mask in the material. They are shared, so the addon needs as few image files as possible:
  - Every image of the same size is placed on the canvas the same way, so it has the same mask. These masks are in [`masks/`](./masks/), named after the original size and the canvas: `mask_1024x1536_2048.png` is for every 1024×1536 image on a 2048 canvas.
  - The six hazard pictograms have the same shape, so they share `masks/mask_kdpx_pictogram_512.png`.
  - Only the images with a shape of their own (stickers, the sticky note, the logo icons) have their own **`<name>_trans.png`** next to their `_color.png`.
  - Images that are square and fully opaque need no mask.

## Shared masks

| Mask | Used by | Images |
| :--- | ---: | :--- |
| [`masks/mask_1024x1448_2048.png`](./masks/mask_1024x1448_2048.png) | 36 | newspapers (`newspapers/`) |
| [`masks/mask_1024x1536_2048.png`](./masks/mask_1024x1536_2048.png) | 29 | portrait posters (`posters/`) |
| [`masks/mask_1024x512_1024.png`](./masks/mask_1024x512_1024.png) | 11 | plates, screens and the door sign (`plates/`, `screens/`, `signs/`) |
| [`masks/mask_1024x1400_2048.png`](./masks/mask_1024x1400_2048.png) | 8 | out-of-bounds posters (`posters/`) |
| [`masks/mask_kdpx_pictogram_512.png`](./masks/mask_kdpx_pictogram_512.png) | 6 | the six hazard pictograms (`signs/`) |
| [`masks/mask_2048x640_2048.png`](./masks/mask_2048x640_2048.png) | 2 | wide logos (`logos/`) |
| [`masks/mask_1536x1024_2048.png`](./masks/mask_1536x1024_2048.png) | 2 | LactoKd ads (`posters/`) |
| [`masks/mask_1536x971_2048.png`](./masks/mask_1536x971_2048.png) | 2 | landscape OASIS posters (`posters/`) |
| [`masks/mask_873x1536_2048.png`](./masks/mask_873x1536_2048.png) | 2 | portrait OASIS posters (`posters/`) |
| [`masks/mask_1024x768_1024.png`](./masks/mask_1024x768_1024.png) | 1 | shipping label (`signs/`) |

To find the mask of an image: take the size from its file name (`poster_kdanium_1024x1536_color.png` → `masks/mask_1024x1536_2048.png`). If there is a `<name>_trans.png` next to it, use that instead.

## Own masks

- `logos/nonvis-division_logo_icon_1024_trans.png`
- `logos/vpk-industries_logo_icon_1024_trans.png`
- `stickers/kd-mcs-001_vigil_sticker_trans.png`
- `stickers/kd-wx-001_atmos_sticker_trans.png`
- `stickers/kd-wx-002_forecast_sticker_trans.png`
- `stickers/kd-wx-003_stratos_sticker_trans.png`
- `stickers/note_where-is-the-pool_1024_trans.png`

## Notes

The folders match `assets/`: `logos/`, `screens/`, `plates/`, `signs/`, `stickers/`, `posters/`, `newspapers/`.

Along the shorter side the image does not reach the edge: scale the texture on the face in Hammer so that only the image part is visible, or use the mask so the empty strips are cut away.

The pictogram sheets (`signs/kdpx_pictograms_row_4096x512` and `signs/kdpx_pictograms_grid_2048x1024`) are already power-of-two, so they keep their own size and have their own `_trans.png`; they are written by [`tools/pictogram_sheets.py`](../tools/pictogram_sheets.py).

Generated with [`tools/square.py`](../tools/square.py): `python3 tools/square.py assets materials`. It prints which mask each image uses.
