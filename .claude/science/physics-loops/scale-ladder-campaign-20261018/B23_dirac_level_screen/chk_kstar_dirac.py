#!/usr/bin/env python3
"""B23: structure of the k* Dirac node for every survivor (and the -k* node when it is a 4-fold level at E).
In the D+ / D- basis (Lambda = -2sqrt2 / +2sqrt2 inside the H_on = 2 space) the DPT velocity matrices h_j should be
block-diagonal (E1/2 x T1 does not contain E5/2), each 2x2 block an untilted isotropic Weyl cone at |n_S| sqrt2/3,
with opposite chiralities sign det M."""
import sys, os, glob, pickle, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b23lib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
lw, lv = np.linalg.eigh(Dpm.conj().T @ Lam @ Dpm); Bp = Dpm @ lv[:, lw < 0]; Bm = Dpm @ lv[:, lw > 0]; B = np.hstack([Bp, Bm])
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
def blocks(w, k, E):
    W0, G = W_grad(w, k); h = [-1j * np.exp(-1j * E) * B.conj().T @ G[j] @ B for j in range(3)]; h = [(x + x.conj().T) / 2 for x in h]
    off = max(np.abs(x[:2, 2:]).max() for x in h); res = []
    for s in (slice(0, 2), slice(2, 4)):
        M = np.array([[np.trace(x[s, s] @ p).real / 2 for p in (sx, sy, sz)] for x in h]); a = np.array([np.trace(x[s, s]).real / 2 for x in h])
        sv = np.linalg.svd(M, compute_uv=False); res.append((sv.min(), sv.max(), np.abs(a).max(), int(np.sign(np.linalg.det(M)))))
    return off, res, float(np.linalg.norm(W0 @ B - np.exp(1j * E) * B))
S = [r for fn in sorted(glob.glob(os.path.join(HERE, 'screen_*.pkl'))) for r in pickle.load(open(fn, 'rb'))['recs'] if not r['fermi']]
worst = dict(eig=0, off=0, speed=0, tilt=0); chis = collections.Counter(); minus = collections.Counter()
for r in S:
    w = build(r['sk'], r['names']); vs = r['vs']
    off, res, ee = blocks(w, kst, r['E'])
    worst['eig'] = max(worst['eig'], ee); worst['off'] = max(worst['off'], off)
    worst['speed'] = max(worst['speed'], max(max(abs(x[0] - vs), abs(x[1] - vs)) for x in res)); worst['tilt'] = max(worst['tilt'], max(x[2] for x in res))
    chis[(res[0][3], res[1][3])] += 1
    mk = [x for x in r['nodes'] if np.allclose(np.array(x[0]), [-0.5, 0.5, -0.5], atol=1e-4)]
    minus[(mk[0][2], mk[0][3]) if mk else 'not at E'] += 1
print("worst deviations:", worst)
print("(chi_D+, chi_D-) at +k*:", dict(chis))
print("-k* node (multiplicity, verdict):", dict(minus))
check("D+ (+) D- is the k* eigenspace at E for every survivor", worst['eig'] < 1e-10, f"{worst['eig']:.1e}")
check("h_j block-diagonal in D+ / D- (no cross terms)", worst['off'] < 1e-10, f"{worst['off']:.1e}")
check("each block an untilted isotropic Weyl cone at |n_S| sqrt2/3", worst['speed'] < 1e-10 and worst['tilt'] < 1e-10)
check("the two cones have opposite chirality", set(chis) <= {(1, -1), (-1, 1)}, str(dict(chis)))
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
