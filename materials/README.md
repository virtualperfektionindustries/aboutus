# Material-ready textures

Every image from [`../assets/`](../assets/), made square for the CS2 Material Editor:

- The canvas is the next power of two that fits the image (512, 1024 or 2048), and the image is centred on it.
- **`<name>_color.png`**: the image. Where the original is not square (or has its own transparency, such as the stickers and pictograms), the rest of the canvas is transparent.
- **`<name>_trans.png`**: only for images with transparent parts. White where the image is, black where it is transparent. Use it as the **Translucency** (or Alpha Test) mask in the material.
- Images that are square and fully opaque only have a `_color.png`.

The folders match `assets/`: `logos/`, `screens/`, `plates/`, `signs/`, `stickers/`, `posters/`, `newspapers/`.

Because the image sits in the middle of a larger canvas, scale the texture on the face in Hammer so that only the image part is visible, or use the mask so the empty part is cut away.

Generated with [`tools/square.py`](../tools/square.py): `python3 tools/square.py assets materials`.
