#!/usr/bin/env python3
"""Probe: is the X-point isotropy in S2.H20.S2.L202 explained by an on-site intertwiner for k -> M k + (pi/2) e_x?"""
from chk_model import *
def UHw(lbl): a,b=int(lbl[1]),int(lbl[2]); return UHc(a,b)
def ULw(lbl): return ULc(*map(int,lbl[1:]))
S2 = lambda k: SKc(k) @ SKc(k)
WA = lambda k: S2(k) @ UHw("H20") @ S2(k) @ ULw("L202")
rng = np.random.default_rng(4); ks = rng.uniform(-np.pi, np.pi, (4, 3)); I = np.eye(12)
OH = [np.array(P) * np.array(s)[:, None] for P in [np.eye(3, dtype=int)[list(p)] for p in itertools.permutations(range(3))] for s in itertools.product((1, -1), repeat=3)]
hits = []
for M in OH:
    for th in [np.pi / 2 * np.eye(3)[0], np.pi / 2 * np.array([1, 1, 0])]:
        for om in (1, -1, 1j, -1j):
            for inv in (False, True):
                A = np.vstack([np.kron(WA(k).T, I) - om * np.kron(I, (WA(M @ k + th).conj().T if inv else WA(M @ k + th))) for k in ks])
                _, s, Vh = np.linalg.svd(A, full_matrices=False); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))]); nb = Vh[s < 1e-9]
                if len(nb):
                    X = sum((rng.normal() + 1j * rng.normal()) * v.conj().reshape(12, 12, order='F') for v in nb)
                    if np.linalg.svd(X, compute_uv=False).min() > 1e-6: hits.append((M.tolist(), np.round(th / np.pi, 2).tolist(), om, inv, len(nb)))
print("invertible on-site intertwiners W(k) -> w W(Mk + theta)^{+-1}, theta in {(pi/2)e_x, (pi/2)(1,1,0)}:", len(hits))
for h in hits[:6]: print("  ", h)
# antiunitary: V W(k)^* V^-1 = w W(Mk+theta)^{+-1}
hitsA = []
for M in OH:
    th = np.pi / 2 * np.eye(3)[0]
    for om in (1, -1, 1j, -1j):
        for inv in (False, True):
            A = np.vstack([np.kron(WA(k).conj().T, I) - om * np.kron(I, (WA(M @ k + th).conj().T if inv else WA(M @ k + th))) for k in ks])
            _, s, Vh = np.linalg.svd(A, full_matrices=False); s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))]); nb = Vh[s < 1e-9]
            if len(nb):
                X = sum((rng.normal() + 1j * rng.normal()) * v.conj().reshape(12, 12, order='F') for v in nb)
                if np.linalg.svd(X, compute_uv=False).min() > 1e-6: hitsA.append((M.tolist(), om, inv))
print("antiunitary versions:", len(hitsA), hitsA[:4])
