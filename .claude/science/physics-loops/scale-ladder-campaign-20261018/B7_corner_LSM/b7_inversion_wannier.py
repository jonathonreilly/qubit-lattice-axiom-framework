#!/usr/bin/env python3
"""B7 (5): with the site inversion kept (class Gh), Slater band insulators at nu = 2, 6, 10.

On-site Slater insulators under Gh exist only at nu = 0 mod 4 (the dressed O_h class has only 4-dim irreps on a
site). Here: a symmetric Wannier doublet centred on the cube centre (1b), built from the corner modes of the 8
surrounding sites, and its union with an on-site quartet.  Certificate: lambda_min of the Gram matrix of the Bloch
sums on an N-grid minus a Lipschitz bound (entrywise Frobenius bound on dG/dk) is > 0, so the Loewdin projector
P(k) is analytic and of constant rank; H = -P (nu = rank) and H = +P (nu = 12 - rank) are then gapped (gap 1),
local, number-conserving, and symmetric (checked: P(g k + pi s_g) = U_g P(k) U_g^T at random k).
"""
import itertools, sys, time
from fractions import Fraction as Fr
import numpy as np
import b7_model as m

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)
def mults(ev, tol=1e-7):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    return out

t0 = time.time()
D = m.build(); OH = D['OH']; U = D['U']; lam = D['lam']; sh = D['shift']
ALL = list(range(48)); rng = np.random.default_rng(31)

def wannier_blocks(w, idx, want_dim, radius=1.0, seed=0):
    """Irrep block (dimension want_dim) of the dressed site group of w acting on corner modes of sites within
    `radius` of w, copied to the orbit of w.  Returns ({site D: 12 x r block}, centres (r x 3))."""
    S = m.site_group(D, w, idx)
    wv = np.array([float(c) for c in w])
    sites = [d for d in itertools.product(range(-2, 3), repeat=3) if np.linalg.norm(np.array(d) - wv) <= radius + 1e-9]
    modes = [(d, c) for d in sites for c in range(12)]; mi = {q: i for i, q in enumerate(modes)}
    def img(g, t, d, c):
        dd = tuple(int(x) for x in OH[g] @ np.array(d) + np.array(t))
        col = U[g][:, c]; r_ = int(np.nonzero(col)[0][0])
        return dd, r_, (-1.0) ** int(np.dot(lam[g], d)) * col[r_]
    ops = []
    for g, t in S:
        Mx = np.zeros((len(modes), len(modes)), complex)
        for (d, c) in modes:
            dd, r_, a = img(g, t, d, c); Mx[mi[(dd, r_)], mi[(d, c)]] = a
        ops.append(Mx)
    Rr = np.random.default_rng(seed); X = Rr.normal(size=(len(modes),) * 2) + 1j * Rr.normal(size=(len(modes),) * 2); X = X + X.conj().T
    Y = sum(Q @ X @ Q.conj().T for Q in ops) / len(ops); ev, V = np.linalg.eigh(Y)
    i = 0; blk = None
    for d in mults(ev):
        if d == want_dim and blk is None: blk = V[:, i:i + d]
        i += d
    if blk is None: return None
    orb = []
    for g in idx:
        gw = tuple(sum(int(OH[g][i, j]) * w[j] for j in range(3)) for i in range(3))
        red = tuple(x - (x.numerator // x.denominator) for x in gw)
        if red not in [o[0] for o in orb]: orb.append((red, g))
    r = len(orb) * want_dim; out = {}; centres = []; col0 = 0
    for red, g in orb:
        gw = [sum(int(OH[g][i, j]) * w[j] for j in range(3)) for i in range(3)]
        tt = [int(red[i] - gw[i]) for i in range(3)]
        for a in range(want_dim):
            for (d, c), amp in zip(modes, blk[:, a]):
                if abs(amp) < 1e-14: continue
                dd, r_, s_ = img(g, tt, d, c)
                out.setdefault(dd, np.zeros((12, r), complex))[r_, col0 + a] += amp * s_
            centres.append([float(x) for x in red])
        col0 += want_dim
    return out, np.array(centres)

def W_of_k(blocks, centres, ks):
    W = np.zeros((len(ks), 12, centres.shape[0]), complex)
    for Dd, A in blocks.items():
        W += A[None] * np.exp(1j * (ks @ np.array(Dd, float))[:, None] - 1j * (ks @ centres.T))[:, None, :]
    return W
def gram_certificate(blocks, centres, N):
    ks = m.kgrid(N); lmin = np.inf
    for ch in range(0, len(ks), 50000):
        W = W_of_k(blocks, centres, ks[ch:ch + 50000])
        lmin = min(lmin, np.linalg.eigvalsh(np.conj(np.transpose(W, (0, 2, 1))) @ W)[:, 0].min())
    # G_ij(k) = sum_{D,D'} conj(A_D)_{.i} A_D'_{.j} e^{i k.((D'-c_j)-(D-c_i))};  |dG/dk| <= ||(sum |..| |..|)||_F
    r = centres.shape[0]; Bd = np.zeros((r, r))
    items = list(blocks.items())
    for Dd, A in items:
        for Dd2, A2 in items:
            M_ = np.abs(A.conj().T @ A2)
            dist = np.linalg.norm((np.array(Dd2)[None, :] - centres)[None, :, :] - (np.array(Dd)[None, :] - centres)[:, None, :], axis=2)
            Bd += M_ * dist
    lip = np.linalg.norm(Bd)
    return lmin, lmin - lip * np.sqrt(3) * np.pi / N, lip
def projector(blocks, centres, ks):
    W = W_of_k(blocks, centres, ks); G = np.conj(np.transpose(W, (0, 2, 1))) @ W
    ev, V = np.linalg.eigh(G); Gm = V @ (V.conj().transpose(0, 2, 1) / ev[:, :, None])   # G^{-1}
    return W @ Gm @ np.conj(np.transpose(W, (0, 2, 1)))
def merge(b1, c1, b2, c2):
    r1, r2 = c1.shape[0], c2.shape[0]; out = {}
    for Dd, A in b1.items(): out.setdefault(Dd, np.zeros((12, r1 + r2), complex))[:, :r1] += A
    for Dd, A in b2.items(): out.setdefault(Dd, np.zeros((12, r1 + r2), complex))[:, r1:] += A
    return out, np.vstack([c1, c2])

h_ = Fr(1, 2)
X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)); X = X + X.conj().T
ev, V = np.linalg.eigh(sum(U[g] @ X @ U[g].T for g in ALL) / 48); assert mults(ev) == [4, 4, 4]
quartets = [V[:, 4 * i:4 * i + 4] for i in range(3)]
best = None
for seed in range(6):
    bd, cd = wannier_blocks((h_, h_, h_), ALL, 2, seed=seed)
    for qi, q in enumerate(quartets):
        bm, cm = merge(bd, cd, {(0, 0, 0): q.astype(complex)}, np.zeros((4, 3)))
        lm = gram_certificate(bm, cm, 16)[0]
        if best is None or lm > best[0]: best = (lm, seed, qi, bd, cd, bm, cm)
print(f"   search: best rank-6 combination doublet seed {best[1]}, on-site quartet {best[2]}, Gram lambda_min (N = 16) {best[0]:.4f}")
b2, c2 = wannier_blocks((h_, h_, h_), ALL, 2)
b6, c6 = best[5], best[6]
ok = True; info = {}
for lab, (bl, ce), NG in (('rank 2 (cube-centre doublet)', (b2, c2), 96), ('rank 6 (doublet + on-site quartet)', (b6, c6), 144)):
    lmin, cert, lip = gram_certificate(bl, ce, NG)
    ks = rng.uniform(-np.pi, np.pi, size=(30, 3)); P = projector(bl, ce, ks); oks = True
    for g in ALL:
        Pg = projector(bl, ce, (OH[g] @ ks.T).T + np.pi * sh[g])
        oks &= np.allclose(Pg, U[g][None] @ P @ U[g].T[None], atol=1e-9)
    rank_ok = np.allclose(np.trace(P, axis1=1, axis2=2).real, ce.shape[0])
    info[lab] = (round(float(lmin), 4), round(float(lip), 3), round(float(cert), 4), oks, rank_ok)
    ok &= cert > 0 and oks and rank_ok
    print(f"   {lab}: Gram lambda_min (N = {NG}) {lmin:.4f}, Lipschitz bound {lip:.3f}, certified {cert:.4f}, "
          f"P symmetric under all 48 dressed O_h: {oks}, rank ok: {rank_ok}")
check("Gh: symmetric Wannier bands of rank 2 and 6 with certified nonsingular Gram matrix; H = -P gives gapped symmetric "
      "Slater insulators at nu = 2 and 6, H = +P at nu = 10 and 6 (complements); with the on-site quartets (nu = 4, 8) "
      "every even nu is realised under Gh", ok)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time() - t0:.0f} s)")
sys.exit(1 if FAIL else 0)
