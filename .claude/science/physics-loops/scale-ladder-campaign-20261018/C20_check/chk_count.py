"""Independent count of the O_h x translation invariant Hermitian range-1 one-fermion terms (C20 claim C0) by the
character formula dim = (1/|G|) sum_g tr(g | V_pm), V_pm = conjugation-even/odd Hermitian block spaces."""
import itertools
import numpy as np
from chk_common import load
Mdl, X, Mm, seeds = load()
L = Mdl['L']; VERTS = Mdl['VERTS']; VID = Mdl['C']['VID']; CORN = Mdl['CORN']; CI = Mdl['CI']
shifts = list(itertools.product((-1, 0, 1), repeat=3)); SI = {s: i for i, s in enumerate(shifts)}
def dm(x): return ((x + 1) % L) - 1
idx = {}
for s in shifts:
    for a in range(12):
        for b in range(12): idx[(s, a, b)] = len(idx)
n = len(idx)
def vid(s, a): return VID[(tuple(x % L for x in s), CORN[a])]
def action(g):
    P, sg = g; img = np.zeros(n, int); sgn = np.zeros(n)
    for (s, a, b), k in idx.items():
        i, j = vid(s, a), vid((0, 0, 0), b); i2, j2 = P[i], P[j]
        sh = tuple(dm(x - y) for x, y in zip(VERTS[i2][0], VERTS[j2][0]))
        img[k] = idx[(sh, CI[VERTS[i2][1]], CI[VERTS[j2][1]])]; sgn[k] = (-1.0) ** (int(sg[i]) + int(sg[j]))
    return img, sgn
tau = np.zeros(n, int)
for (s, a, b), k in idx.items(): tau[k] = idx[(tuple(-x for x in s), b, a)]
G = [action(g) for g in Mdl['rots'] + Mdl['invs']]
for img, sgn in G: assert np.array_equal(img[tau], tau[img]) and np.allclose(sgn[tau], sgn)
ar = np.arange(n)
trg = [np.sum(sgn[img == ar]) for img, sgn in G]
trgt = [np.sum(sgn[tau][img[tau] == ar]) for img, sgn in G]   # (g tau) e_k = sgn[tau k] e_{img[tau k]}
even = (sum(trg) + sum(trgt)) / 2 / len(G)
odd = (sum(trg) - sum(trgt)) / 2 / len(G)
print(f'conjugation-even (real, B_-s = B_s^T): {even:.6f}; conjugation-odd (imaginary, B_-s = -B_s^T): {odd:.6f}; total {even+odd:.6f}')
