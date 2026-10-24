import sys
from PIL import Image, ImageFilter
import numpy as np
from collections import deque
V, M = sys.argv[1], sys.argv[2]
src = Image.open(V + '/last.png').convert('RGB')

def flood(mask, seeds):
    H, W = mask.shape; seen = np.zeros_like(mask); q = deque()
    for y, x in seeds:
        if mask[y, x] and not seen[y, x]: seen[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True; q.append((ny, nx))
    return seen

def coeffs(dst, srcq):
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,srcq):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);B.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]);B.append(v)
    return np.linalg.solve(np.array(A,float),np.array(B,float)).tolist()

quads = np.load(V + '/quads.npy')
jobs = [('moderninha-smart-2', 'bebidas'), ('stone', 'comidas'), ('cielo', 'combos')]
SS = 2
for (name, scr), q in zip(jobs, quads):
    # ângulo da borda de cima da tela
    ang = np.degrees(np.arctan2(q[1][1]-q[0][1], q[1][0]-q[0][0]))
    big = src.resize((src.width*SS, src.height*SS), Image.LANCZOS)
    c = q.mean(0) * SS
    rot = big.rotate(ang, Image.BICUBIC, center=tuple(c), fillcolor=(255,255,255))
    # mesma rotação aplicada aos cantos da tela
    t = np.radians(-ang); R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    qr = (q*SS - c) @ R.T + c
    a = np.asarray(rot).astype(int); H, W, _ = a.shape
    white = a.min(axis=2) > 232
    seeds = [(0, x) for x in range(W)] + [(H-1, x) for x in range(W)] + [(y, 0) for y in range(H)] + [(y, W-1) for y in range(H)]
    bg = flood(white, seeds)
    # o aparelho é o pedaço que não é fundo e encosta no centro da tela
    fg = ~bg
    cy, cx = int(c[1]), int(c[0])
    dev = flood(fg, [(cy, cx)])
    alpha = Image.fromarray((dev*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2))
    img = rot.copy()
    # tela do Evolua Ticket por cima
    s = Image.open(f'{M}/scr-{scr}.png').convert('RGBA')
    k = qr.mean(0); qd = k + (qr - k) * 1.012
    warped = s.transform((W, H), Image.PERSPECTIVE, coeffs(qd.tolist(), [(0,0),(s.width,0),(s.width,s.height),(0,s.height)]), Image.BICUBIC)
    img = img.convert('RGBA'); img.alpha_composite(warped)
    img.putalpha(alpha)
    img = img.crop(alpha.getbbox())
    img = img.resize((img.width//SS, img.height//SS), Image.LANCZOS)
    img.save(f'{V}/up-{name}.png')
    print(name, round(ang, 2), img.size)
