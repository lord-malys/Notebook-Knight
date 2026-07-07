"""Notebook Knight enemy sheet splitter v2.
Usage: python3 split_sheet.py <sheet.png> <enemy_id> [--horizontal]
Splits a 3-variant sheet (base/inked/colored) into enemy_<id>[_inked|_colored].png,
transparent background, trimmed, centered on 800x1000.
v2: edge-based segmentation instead of background modeling - finds the drawn outlines,
fills them, keeps splatter details, drops background gradients/glows/vignettes."""
import sys
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

def split_bands(arr, n=3, axis=0):
    gray = arr[..., :3].astype(np.float32).mean(axis=2)
    grad = np.abs(np.diff(gray, axis=1 - axis)).sum(axis=1 - axis)
    k = max(5, len(grad) // 100)
    prof = np.convolve(grad, np.ones(k) / k, mode='same')
    L = len(prof)
    cuts = [0]
    for i in range(1, n):
        lo, hi = int(L * (i / n - 0.12)), int(L * (i / n + 0.12))
        cuts.append(lo + int(np.argmin(prof[lo:hi])))
    cuts.append(L)
    return list(zip(cuts[:-1], cuts[1:]))

def extract_figure(band):
    """Edge-detect the drawn linework, close+fill it, keep sizable components."""
    arr = band.astype(np.float32)
    gray = arr[..., :3].mean(axis=2)
    gy, gx = np.gradient(gray)
    edges = np.hypot(gx, gy)
    # adaptive threshold: linework is much stronger than gradient/glow backgrounds
    t = max(6.0, np.percentile(edges, 99) * 0.12)
    mask = edges > t
    # connect strokes and fill enclosed regions
    mask = ndimage.binary_dilation(mask, iterations=4)
    mask = ndimage.binary_fill_holes(mask)
    mask = ndimage.binary_erosion(mask, iterations=3)
    # drop tiny noise, keep intentional splatter (>= 40 px)
    lbl, n = ndimage.label(mask)
    if n == 0:
        return None
    sizes = ndimage.sum(mask, lbl, range(1, n + 1))
    keep = np.isin(lbl, np.where(sizes >= 40)[0] + 1)
    # feathered alpha
    alpha = ndimage.gaussian_filter(keep.astype(np.float32), 1.2)
    alpha = np.clip((alpha - 0.25) / 0.5, 0, 1)
    return np.dstack([arr[..., :3], alpha * 255]).astype(np.uint8)

def trim_and_fit(rgba, W=800, H=1000, margin=0.04):
    a = rgba[..., 3]
    ys, xs = np.where(a > 20)
    if len(xs) == 0:
        return None
    crop = Image.fromarray(rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1])
    mw, mh = int(W * (1 - 2 * margin)), int(H * (1 - 2 * margin))
    s = min(mw / crop.width, mh / crop.height)
    crop = crop.resize((max(1, int(crop.width * s)), max(1, int(crop.height * s))), Image.LANCZOS)
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    canvas.paste(crop, ((W - crop.width) // 2, H - int(H * margin) - crop.height), crop)
    return canvas

def main():
    path, eid = sys.argv[1], sys.argv[2]
    axis = 1 if '--horizontal' in sys.argv else 0
    arr = np.array(Image.open(path).convert('RGB'))
    for (b0, b1), suf in zip(split_bands(arr, 3, axis), ['', '_inked', '_colored']):
        band = arr[b0:b1] if axis == 0 else arr[:, b0:b1]
        rgba = extract_figure(band)
        out = trim_and_fit(rgba) if rgba is not None else None
        if out is None:
            print(f'WARN: no content for {suf or "base"}')
            continue
        out.save(f'enemy_{eid}{suf}.png')
        print(f'wrote enemy_{eid}{suf}.png')

if __name__ == '__main__':
    main()
