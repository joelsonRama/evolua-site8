import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from collections import deque
F, S = sys.argv[1], sys.argv[2]
im = Image.open(F + '/impressora-bluetooth.webp').convert('RGB'); W, H = im.size
a = np.asarray(im).astype(int)
# contorno do papel (não deixa o "fundo branco" entrar no papel)
paper_poly = [(378,335),(572,0),(700,0),(800,40),(905,92),(955,135),(984,195),(988,265),(975,320),(945,355),(900,372),(850,372),(660,500)]
guard = Image.new('L', (W, H), 0); ImageDraw.Draw(guard).polygon(paper_poly, fill=255); guard = np.asarray(guard) > 0
white = (a.min(axis=2) > 236) & ~guard
seen = np.zeros((H, W), bool); q = deque()
for x in range(W):
    for y in (0, H-1):
        if white[y, x]: seen[y, x] = True; q.append((y, x))
for y in range(H):
    for x in (0, W-1):
        if white[y, x] and not seen[y, x]: seen[y, x] = True; q.append((y, x))
while q:
    y, x = q.popleft()
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < H and 0 <= nx < W and white[ny, nx] and not seen[ny, nx]: seen[ny, nx] = True; q.append((ny, nx))
alpha = Image.fromarray(((~seen) * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(1))

# ficha do Evolua Ticket na face do papel
def coeffs(dst, src):
    A=[];B=[]
    for (x,y),(u,v) in zip(dst,src):
        A.append([x,y,1,0,0,0,-u*x,-u*y]);B.append(u)
        A.append([0,0,0,x,y,1,-v*x,-v*y]);B.append(v)
    return np.linalg.solve(np.array(A,float),np.array(B,float)).tolist()
tk = Image.open(S + '/ticket/ficha-quermesse.png').convert('RGBA')
tw, th = tk.size
crop = tk.crop((0, int(th*0.0), tw, th))   # ficha inteira
cw, ch = crop.size
face = [(588,6),(872,128),(652,494),(380,334)]   # TL, TR, BR, BL
warp = crop.transform((W, H), Image.PERSPECTIVE, coeffs(face, [(0,0),(cw,0),(cw,ch),(0,ch)]), Image.BICUBIC)
# luz do papel da foto (sem o texto antigo) para manter a sombra natural
lum = im.convert('L').filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(12))
facemask = Image.new('L', (W, H), 0); ImageDraw.Draw(facemask).polygon([(364,338),(559,-2),(706,-2),(800,38),(905,92),(872,128),(652,494)], fill=255)
# apaga o texto antigo: pinta a face com o branco do papel
base = im.copy()
paper_white = Image.merge('RGB', (lum, lum, lum))
base.paste(paper_white, (0,0), facemask.filter(ImageFilter.GaussianBlur(1)))
w = np.asarray(warp).astype(float)
shade = (np.asarray(lum).astype(float) / 250.0).clip(0.7, 1.05)[..., None]
w[..., :3] = w[..., :3] * shade
warp = Image.fromarray(w.clip(0,255).astype('uint8'), 'RGBA')
out = base.convert('RGBA'); out.alpha_composite(warp)
out.putalpha(alpha)
out = out.crop(alpha.getbbox())
out.save(S + '/phone/impressora-real.png'); print(out.size)
bg = Image.new('RGBA', out.size, (230,236,246,255)); bg.alpha_composite(out); bg.convert('RGB').save(S + '/phone/impressora-prev.png')
