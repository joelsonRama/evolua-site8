import sys
from PIL import Image, ImageFilter, ImageDraw
import numpy as np
S = sys.argv[1]; V = S + '/video'; T = S + '/ticket'
SS = 3

def retouch(img, boxes):
    """Apaga logos: cada caixa é preenchida linha a linha com a cor das bordas (esquerda/direita) da própria linha."""
    a = np.asarray(img).astype(float)
    for x0, y0, x1, y1 in boxes:
        for y in range(y0, y1):
            l = a[y, x0-3:x0].mean(0); r = a[y, x1:x1+3].mean(0)
            for x in range(x0, x1):
                t = (x - x0) / max(1, x1 - x0)
                a[y, x] = l * (1 - t) + r * t
    out = Image.fromarray(a.clip(0, 255).astype('uint8'), 'RGBA')
    # suaviza só dentro das caixas
    blur = out.filter(ImageFilter.GaussianBlur(1.5 * SS))
    m = Image.new('L', out.size, 0); d = ImageDraw.Draw(m)
    for b in boxes: d.rectangle(b, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(2 * SS))
    out.paste(blur, (0, 0), m)
    a2 = np.asarray(out).copy(); a2[..., 3] = np.asarray(img)[..., 3]
    return Image.fromarray(a2, 'RGBA')

def curl(tk, straight=0.70, max_ang=86):
    """Papel saindo da impressora: parte de baixo reta, ponta de cima curvando para trás."""
    t = np.asarray(tk).astype(float); H, W, _ = t.shape
    s0 = H * straight; L = H - s0
    r = L / np.radians(max_ang)
    top_h = r * np.sin(np.radians(max_ang))
    outH = int(np.ceil(s0 + top_h)) + 2
    out = np.zeros((outH, W, 4))
    for oy in range(outH):
        h = outH - 1 - oy                         # altura acima da boca da impressora
        if h <= s0:
            s = h; phi = 0.0
        else:
            v = min(1.0, (h - s0) / r); phi = np.arcsin(v); s = s0 + r * phi
        sy = H - 1 - s
        if sy < 0: continue
        scale = 1 - 0.10 * (1 - np.cos(phi))     # afina um pouco ao ir para trás
        shade = (0.74 + 0.26 * np.cos(phi) + 0.07 * np.exp(-((phi - 0.30) / 0.16) ** 2)) if phi > 0 else 1.0
        xs = (np.arange(W) - W / 2) / scale + W / 2
        valid = (xs >= 0) & (xs <= W - 1)
        x0 = np.clip(xs.astype(int), 0, W - 1)
        row = t[int(sy)][x0]
        row[~valid] = 0
        row[..., :3] *= shade
        out[oy] = row
    # sombra suave perto da boca (papel saindo de dentro)
    g = np.linspace(0, 1, 18 * SS)
    out[-len(g):, :, :3] *= (1 - 0.35 * g[:, None, None])
    return Image.fromarray(out.clip(0, 255).astype('uint8'), 'RGBA')

jobs = [
    # aparelho, ficha, boca da impressora (y), x central, largura do papel, caixas de retoque (coords 1x)
    ('moderninha-smart-2', 'festa', 156, 133, 150, [(56, 24, 190, 52), (180, 102, 218, 128)]),
    ('stone', 'quermesse', 155, 128, 150, [(100, 579, 154, 599)]),
    ('cielo', 'show', 51, 130, 150, [(44, 10, 196, 34), (98, 60, 150, 76)]),
]
for dev, tk, slot, cx, pw, boxes in jobs:
    d = Image.open(f'{V}/up-{dev}.png').convert('RGBA')
    D = d.resize((d.width * SS, d.height * SS), Image.LANCZOS)
    D = retouch(D, [tuple(v * SS for v in b) for b in boxes])
    t = Image.open(f'{T}/ficha-{tk}.png').convert('RGBA')
    tw = pw * SS; th = int(t.height * tw / t.width)
    paper = curl(t.resize((tw, th), Image.LANCZOS))
    top = max(0, paper.height - slot * SS + 6 * SS)
    canvas = Image.new('RGBA', (D.width, D.height + top), (0, 0, 0, 0))
    canvas.alpha_composite(D, (0, top))
    x = cx * SS - paper.width // 2; y = top + slot * SS - paper.height
    a = paper.split()[3]
    sh = Image.merge('RGBA', (*Image.new('RGB', paper.size, (8, 12, 28)).split(), a.point(lambda v: int(v * .35)))).filter(ImageFilter.GaussianBlur(4 * SS))
    canvas.alpha_composite(sh, (x + 2 * SS, y + 4 * SS))
    canvas.alpha_composite(paper, (x, y))
    out = canvas.resize((canvas.width // SS, canvas.height // SS), Image.LANCZOS)
    out.save(f'{V}/curl-{dev}.png'); print(dev, out.size)

ims = [Image.open(f'{V}/curl-{j[0]}.png') for j in jobs]
W = sum(i.width for i in ims) + 80; H = max(i.height for i in ims) + 40
bg = Image.new('RGBA', (W, H), (240, 244, 250, 255)); x = 20
for i in ims: bg.alpha_composite(i, (x, H - 20 - i.height)); x += i.width + 20
bg.convert('RGB').save(f'{V}/curl-preview.png')
