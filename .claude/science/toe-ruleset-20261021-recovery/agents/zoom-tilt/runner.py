#!/usr/bin/env python3
"""Zoom fixed points, scaling dimensions and the primordial tilt for the supplied CL-2 tick
(supplied model; finite diagnostic; no physical identification).
 A  rung map (x2 zoom, 2 ticks per rung tick): exact intertwiner at rungs 1 and 2, so the light-sector map is
    w'(Q) = 2 w(Q/2) on bands and C'(Q) = C(Q/2) on quasi-free odds; band spectrum 4^(1-p) on degree-2p terms of w^2
 B  fixed points on quasi-free odds = degree-0 homogeneous one-body correlations C(K^); exact density index:
    smooth (incl. the massless half-filled sea) 2, direction jumps ('Fermi cones' through Gamma) 1, mixed 0
 C  the tilt: integer dimensions; positive mixtures of integer indices force running >= {n}(1-{n});
    slow-roll analogue -2/N against the rung ladder; natural-number scan with a look-elsewhere count
 D  A_s: tensor bound in cell units (CL-5 G = a^2/8pi gives M_P = 1/a); single-clock bookkeeping; look-elsewhere
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np

T0 = time.monotonic(); PASS = FAIL = 0
rng = np.random.default_rng(20261021)
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---------------- supplied tick (CL-2): spin-3/2 edge hop on 2^3 cubes, two tilings offset by (1,1,1) ----------------
C = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J32 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); XI.append(np.linalg.eigh(sum(n_[k] * J32[k] for k in range(3)))[1][:, -1])
W = np.zeros((8, 8), complex)
for a, b in itertools.product(range(8), repeat=2):
    if np.sum(abs(C[a] - C[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3)
def Wm(a): return np.cos(a) * W + 1j * np.sin(a) * np.eye(8)
def AB(mu, b): return (np.cos(2 * b) + np.cos(mu)) / 2, (np.cos(2 * b) - np.cos(mu)) / 2
def Ublo(K, mu, b):   # one tick at cell momentum K (twist per 2 sites): U = D Wo D^+ We, D = diag exp(i C.K)
    D = np.exp(1j * np.asarray(K, float) @ C.T); return (D[..., :, None] * Wm(mu / 2 - b) * D.conj()[..., None, :]) @ Wm(mu / 2 + b)
def res(x): return int((np.asarray(x) % 2) @ [4, 2, 1])
class Cell:   # L^3 sites with Bloch twist Q per period L, built block by block from the half-tick rule
    def __init__(self, L):
        self.L = L; self.sites = np.array(list(itertools.product(range(L), repeat=3))); self.N = L ** 3
        idx = {tuple(s): i for i, s in enumerate(self.sites)}; self.blocks = {}
        for off in (0, 1):
            self.blocks[off] = [([idx[tuple(v)] for v in (np.array(b0) + off + C) % L], [res(v) for v in np.array(b0) + off + C],
                                 np.floor_divide(np.array(b0) + off + C, L)) for b0 in itertools.product(range(0, L, 2), repeat=3)]
    def half(self, off, Wb, Q):
        M = np.zeros((self.N, self.N), complex)
        for ids, rs, wr in self.blocks[off]:
            ph = np.exp(1j * wr @ Q); M[np.ix_(ids, ids)] += Wb[np.ix_(rs, rs)] * np.outer(ph.conj(), ph)
        return M
    def tick(self, Q, mu, b): return self.half(1, Wm(mu / 2 - b), Q) @ self.half(0, Wm(mu / 2 + b), Q)

print('== A. the rung map')
Ks = rng.uniform(-np.pi, np.pi, (40, 3)); c2 = Cell(2); e1 = e2 = 0
for mu, b in ((0.4, 0.3), (0.0, 0.3), (0.07, np.pi / 2 - 0.035)):
    A, B = AB(mu, b); e1 = max(e1, max(np.abs(c2.tick(K, mu, b) - Ublo(K, mu, b)).max() for K in Ks[:10]))
    e2 = max(e2, np.abs(np.real(np.linalg.eigvals(Ublo(Ks, mu, b))) - (A * np.cos(Ks).mean(1) - B)[:, None]).max())
check('A1 vectorised Bloch tick = block-built CL-2 tick; every band obeys cos w = A S(K) - B', e1 < 1e-12 and e2 < 1e-12, f'{e1:.0e}, {e2:.0e}')
def embed(L, Q, n):   # fine Bloch states at K = (Q + 2 pi n)/(L/2) embedded in the L^3 supercell
    h = L // 2; K = (Q + 2 * np.pi * np.array(n)) / h; E = np.zeros((L ** 3, 8), complex)
    for i, x in enumerate(itertools.product(range(L), repeat=3)):
        X, c = np.array(x) // 2, np.array(x) % 2; E[i, res(c)] = np.exp(1j * K @ X) / h ** 1.5
    return E, K
eI = eU = 0
for L in (4, 8):
    cl = Cell(L)
    for Q in rng.uniform(-np.pi, np.pi, (2, 3)):
        for mu, b in ((0.0, 0.3), (0.2, 0.5)):
            Uc = cl.tick(Q, mu, b); Es = [embed(L, Q, n) for n in itertools.product(range(L // 2), repeat=3)]
            eI = max(eI, max(np.abs(Uc @ E - E @ Ublo(K, mu, b)).max() for E, K in Es))
            Eall = np.hstack([E for E, _ in Es]); eU = max(eU, np.abs(Eall.conj().T @ Eall - np.eye(L ** 3)).max())
check('A2 rungs 1, 2: U_cell(Q) E_n = E_n U(K_n), K_n = (Q+2pi n)/2^r, {E_n} unitary: the rung-r tick (2^r ticks) is the direct '
      'sum of U(K_n)^(2^r); light alias n=0 gives w_r(Q) = 2^r w(Q/2^r) and C_r(Q) = C(Q/2^r) exactly', eI < 1e-12 and eU < 1e-12, f'{eI:.0e}, {eU:.0e}')
def wband(K, mu, b): A, B = AB(mu, b); return np.arccos(np.clip(A * np.cos(K).mean(-1) - B, -1, 1))
mu, b, q = 0.01, 0.3, 2e-2; ex, e111 = np.array([1., 0, 0]), np.ones(3) / np.sqrt(3); rows = []
for r in range(5):
    w2 = lambda Q: (2 ** r * wband(Q / 2 ** r, mu, b)) ** 2
    m2 = w2(np.zeros(3)); c2r = (w2(q * ex) - m2) / q ** 2; an = (w2(q * ex) - w2(q * e111)) / q ** 4; rows.append((m2, c2r, an))
rows = np.array(rows); rat = rows[1:] / rows[:-1]
check('A3 band spectrum: mass^2 x4, c^2 x1, cubic quartic x1/4 per rung (eigenvalues 4^(1-p), scaling dims 1-p, integers)',
      np.allclose(rat[:, 0], 4, rtol=1e-9) and np.allclose(rat[:, 1], 1, rtol=2e-3) and np.allclose(rat[:, 2], 0.25, rtol=2e-2),
      'ratios ' + ' '.join(f'{x:.4f}' for x in rat[-1]))

print('== B. fixed points on quasi-free odds (C(2K)=C(K): degree 0 in K) and their exact density index')
def wrap(k): return (k + np.pi) % (2 * np.pi) - np.pi
def bands(K, mu, b): U = Ublo(K, mu, b); return np.linalg.eigh((np.swapaxes(U.conj(), -1, -2) - U) / 2j)   # eigvals sin(omega)
def S_line(state, d, Ls=192, Lt=16, noff=2, ms=(1, 2, 3, 4, 6, 8, 12), mu=0.0, b=0.3):
    """S(q), q = (pi m/Ls) d: exact fine grid along d, K = a e_y + c e_z + s d (unimodular), transverse grid + random offsets.
       S(q) = rho - (1/8) <tr[D_q P(K) D_q^+ P(K - 2q)]>_K, D_q = diag exp(-i q.c)  (quasi-free Wick formula)."""
    d = np.array(d, float); acc = np.zeros(len(ms)); rho = 0.0
    for _ in range(noff):
        o = rng.uniform(0, 1, 3); s = 2 * np.pi * (np.arange(Ls) + o[0]) / Ls; t = 2 * np.pi * (np.arange(Lt) + o[1:, None]) / Lt
        for ia in range(Lt):
            K = wrap(t[0, ia] * np.array([0, 1, 0]) + t[1][None, :, None] * np.array([0, 0, 1]) + s[:, None, None] * d)
            lam, V = bands(K, mu, b); P = np.einsum('...ak,...k,...bk->...ab', V, state(K, lam), V.conj())
            rho += np.real(np.trace(P, axis1=-2, axis2=-1)).sum()
            for i, m in enumerate(ms):
                ph = np.exp(-1j * C @ (np.pi * m / Ls * d))
                acc[i] += np.real(np.einsum('a,xzab,b,xzba->', ph, P, ph.conj(), np.roll(P, m, axis=0)))
    N = noff * Ls * Lt * Lt; ms = np.array(ms); qn = np.pi * ms * np.linalg.norm(d) / Ls; S = (rho - acc) / (8 * N)
    sl = np.log(S[1:] / S[:-1]) / np.log(ms[1:] / ms[:-1]); qm = np.sqrt(qn[1:] * qn[:-1])
    return np.polyval(np.polyfit(qm[:5], sl[:5], 2), 0.0), np.polyval(np.polyfit(qn[:5], S[:5] / qn[:5], 2), 0.0), qn
sea = lambda K, lam: (lam < 0).astype(float)
Lb = 4; Kg4 = wrap(2 * np.pi * (np.stack(np.meshgrid(*[np.arange(Lb) + .5] * 3, indexing='ij'), -1)) / Lb)   # antiperiodic 8^3 torus
lam4, V4 = bands(Kg4, 0.4, 0.3); P4 = np.einsum('...ak,...k,...bk->...ab', V4, sea(Kg4, lam4), V4.conj())
Xs = np.array(list(itertools.product(range(Lb), repeat=3))); dX = (Xs[:, None, :] - Xs[None, :, :]).reshape(-1, 3)
Cc = np.einsum('kr,kab->rab', np.exp(1j * Kg4.reshape(-1, 3) @ dX.T), P4.reshape(-1, 8, 8)).reshape(len(Xs), len(Xs), 8, 8) / Lb ** 3
Cx = Cc.transpose(0, 2, 1, 3).reshape(8 * len(Xs), -1); pos = (2 * Xs[:, None, :] + C[None]).reshape(-1, 3)
perm = [int(np.ravel_multi_index(tuple(x), (8, 8, 8))) for x in pos]; Ur = Cell(8).tick(np.full(3, np.pi), 0.4, 0.3)[np.ix_(perm, perm)]
eS = 0
for m, d in ((1, (1, 0, 0)), (1, (1, 1, 0)), (2, (1, 1, 1))):
    qv = np.pi * m * np.array(d) / Lb; ph = np.exp(-1j * pos @ qv); Sr = np.real(np.trace(Cx) - ph @ np.abs(Cx) ** 2 @ ph.conj()) / len(Cx)
    ph8 = np.exp(-1j * C @ qv); Sb = np.real(np.trace(P4, axis1=-2, axis2=-1).sum() - np.einsum('a,xyzab,b,xyzba->', ph8, P4, ph8.conj(),
          np.roll(P4, tuple(m * np.array(d)), axis=(0, 1, 2)))) / (8 * Lb ** 3); eS = max(eS, abs(Sr - Sb))
check('B0 Wick formula S(q) = rho - <tr[D C(K) D^+ C(K-2q)]>/8 equals the real-space S(q) of the 512-site sea, which commutes with '
      'the block-built real-space tick', eS < 1e-12 and np.abs(Ur @ Cx - Cx @ Ur).max() < 1e-12, f'{eS:.0e}, [U,C] {np.abs(Ur @ Cx - Cx @ Ur).max():.0e}')
def cone(test):
    def st(K, lam):
        inD = test(K / np.linalg.norm(K, axis=-1, keepdims=True))[..., None]; return np.where(inD, lam < 0, lam > 0).astype(float)
    return st
faces, diags = cone(lambda n: np.abs(n).max(-1) > 0.8), cone(lambda n: np.abs(n.prod(-1)) > 0.15)
n0, _, _ = S_line(sea, (1, 0, 0)); n1, _, _ = S_line(sea, (1, 0, 0), mu=0.4)
check('B1 the massless half-filled sea (mu = 0 fixed point, smooth C(K^)) and the massive sea: index 2 (analytic q^2)',
      abs(n0 - 2) < 0.02 and abs(n1 - 2) < 0.02, f'n -> {n0:.4f}, {n1:.4f}')
res_ = {}
for nm, st in (('faces', faces), ('diags', diags)):
    res_[nm] = [S_line(st, d) for d in ((1, 0, 0), (1, 1, 0), (1, 1, 1))]
ns = [x[0] for v in res_.values() for x in v]
check('B2 pure fixed points with direction jumps (Fermi cones through Gamma, cube-symmetric, half filling): index 1 in all '
      '3 directions, not 0.965', max(abs(np.array(ns) - 1)) < 0.02, 'n -> ' + ' '.join(f'{x:.3f}' for x in ns))
an = {k: [x[1] for x in v] for k, v in res_.items()}; aniso = {k: max(v) / min(v) - 1 for k, v in an.items()}
check('B3 S/|q| at q->0 along 100,110,111 (precision ~3%%): face cones anisotropic by %.0f%%, diagonal cones %.0f%% (exact isotropy '
      'is impossible for finitely many smooth jump curves; near-isotropy is not)' % (100 * aniso['faces'], 100 * aniso['diags']),
      aniso['faces'] > 0.08, '; '.join(f"{k}: " + ' '.join(f'{x:.3f}' for x in v) for k, v in an.items()))
Kg = wrap(2 * np.pi * (np.stack(np.meshgrid(*[np.arange(16) + .5] * 3, indexing='ij'), -1)) / 16)
lam, V = bands(Kg, 0.4, 0.3); A, B = AB(0.4, 0.3); om = np.sign(lam) * wband(Kg, 0.4, 0.3)[..., None]
Pth = np.einsum('...ak,...k,...bk->...ab', V, 1 / (np.exp(om / 0.5) + 1), V.conj()); S0 = np.real(np.trace(Pth - Pth @ Pth, axis1=-2, axis2=-1)).mean() / 8
U = Ublo(Kg, 0.0, 0.3); lam0, V0 = bands(Kg, 0.0, 0.3); Pf = np.einsum('...ak,...k,...bk->...ab', V0, faces(Kg, lam0), V0.conj())
stat = np.abs(U @ Pf - Pf @ U).max()
check('B4 mixed fixed points (Gibbs, white) have S(0) = <tr C(1-C)>/8 > 0: index 0; T, Fermi level, mass double per rung '
      '(relevant, eigenvalue 2); band-diagonal fixed points commute with the tick, so CL-4 freezes them (stay mass 1)',
      S0 > 1e-3 and stat < 1e-12, f'S(0) Gibbs T=0.5: {S0:.4f}; white 1/4; [U,C] {stat:.0e}')

print('== C. the tilt against measurement')
ns_, dns, al, dal = 0.9649, 0.0042, -0.0045, 0.0067
check('C1 n_s - 1 = -(scaling dim) needs y = 0.0351 +- 0.0042 (per-rung power ratio 2^(n_s-1) = %.4f); free-tick dims are integers, nearest (0, exactly marginal c) is ' % 2 ** (ns_ - 1) + 
      f'{(1 - ns_) / dns:.1f} sigma off; irrelevant terms from the cell scale reach the pivot as 4^-192 = 1e{-192.3 * np.log10(4):.0f}',
      (1 - ns_) / dns > 5)
bound = (ns_ - np.floor(ns_)) * (np.ceil(ns_) - ns_); amin, gap = 9, 9
for _ in range(400):
    s = rng.exponential(1, 4) * 10.0 ** rng.uniform(-3, 3, 4); lq = np.linspace(-12, 6, 4000); wts = s[None] * np.exp(np.outer(lq, np.arange(4)))
    p = wts / wts.sum(1, keepdims=True); ne = p @ np.arange(4); va = p @ np.arange(4) ** 2 - ne ** 2
    fr = ne - np.floor(ne); gap = min(gap, (va - fr * (1 - fr)).min())
    if ne[0] < ns_ < ne[-1]: amin = min(amin, np.interp(ns_, ne, va))
check('C2 a positive mixture of integer-index parts has running = Var(index) >= {n}(1-{n}) = %.4f at n = 0.9649 (400 random '
      'mixtures: min %.4f, bound never violated); measured -0.0045 +- 0.0067 excludes it at %.1f sigma' % (bound, amin, (bound - al) / dal),
      gap > -1e-12 and amin >= bound - 1e-6 and (bound - al) / dal > 5)
cands = [(p * p * ((ns_ - a_) / p) * (1 - (ns_ - a_) / p), a_, p) for a_ in (0, 1, 2, 3) for p in (1, 2, 3, 4)]
best = min(cands, key=lambda t: abs(t[0] - al)); alb = best[0]
check('C2b an integer index a with one correction, S = q^a(1 + c q^p): running = p^2 f(1-f), n - a = p f; closest to data is '
      '(a,p) = (%d,%d) with running %+.4f, %.1f sigma; lattice corrections at the pivot are (qa)^p ~ 1e-58p' % (best[1], best[2], alb, abs(alb - al) / dal),
      abs(alb - al) / dal > 4)
lP, Mpc, H0 = 1.616255e-35, 3.0857e22, 67.4; RH = 2.99792458e5 / H0 * Mpc; lpiv = Mpc / 0.05; asite = np.sqrt(8 * np.pi) * lP
lad = {f'{nm} {lab}': np.log2(L / a_) for nm, a_ in (('a', asite), ('lP', lP)) for lab, L in (('c/H0', RH), ('1/k*', lpiv))}
Nl = lad['a c/H0'] * np.log(2); nsl = 1 - 2 / Nl; nsr = 1 - 2 / lad['a c/H0']; Nh = np.log(1e183) / 3
print('   rungs: ' + ', '.join(f'{k} {v:.1f}' for k, v in lad.items()) + f'; N = 57 e-folds = {57 / np.log(2):.1f} rungs')
check('C3 slow-roll analogue -2/N with the ladder: N = %.1f e-folds gives n_s = %.4f (%.1f sigma), N = rungs gives %.4f (%.1f sigma); '
      'N = 57 is a fit' % (Nl, nsl, (nsl - ns_) / dns, nsr, (nsr - ns_) / dns), (nsl - ns_) / dns > 4)
check('C4 historic graph-growth note: N_e = (1/3) ln N_cells with its own 1e183 Planck volumes gives N_e = %.1f, n_s = %.4f '
      '(%.1f sigma); its 0.9667 used N_obs = 1e78' % (Nh, 1 - 2 / Nh, (1 - 2 / Nh - ns_) / dns), (1 - 2 / Nh - ns_) / dns > 4)
base = {'1/8pi': 1 / (8 * np.pi), '1/rt3': 3 ** -.5, '1/2': .5, '1/3': 1 / 3, '1/8': .125, '1/24': 1 / 24, 'ln2': np.log(2),
        '1/pi': 1 / np.pi, '1/Nrung': 1 / lad['a c/H0'], '1/Nefold': 1 / Nl}
pre = [1, 2, 3, 4, 1 / 2, 1 / 3, 1 / 4, 2 / 3, 3 / 2, 3 / 4, 4 / 3]
vals = {}
for (k1, v1), (k2, v2) in itertools.combinations_with_replacement(list(base.items()) + [('1', 1.0)], 2):
    for e1_ in (1, 2, 3):
        for r_ in pre: vals.setdefault(round(r_ * v1 ** e1_ * v2, 12), f'{r_:.3g}*({k1})^{e1_}*{k2}')
lo, hi = 1 - ns_ - dns, 1 - ns_ + dns; inr = [v for v in vals if 0.01 <= v <= 0.1]; hits = sorted(v for v in inr if lo <= v <= hi)
exp_ = len(inr) * np.log(hi / lo) / np.log(10)
check('C5 simple ruleset numbers r*c1^e*c2 within 1 sigma of 1-n_s: %d hits vs %.0f expected by chance, so a match is not evidence; '
      'e.g. 1/8pi = %.4f (%.1f sigma) is G per cell, irrelevant (x1/4 per rung)' % (len(hits), exp_, 1 / (8 * np.pi), (1 / (8 * np.pi) - (1 - ns_)) / dns),
      exp_ >= 1 and len(hits) <= 3 * exp_ + 3, 'hits e.g. ' + ', '.join(vals[h] for h in hits[::max(1, len(hits) // 3)][:3]))

print('== D. the amplitude A_s')
As, dlnA, rmax = np.exp(3.044) * 1e-10, 0.014, 0.036
aH = np.sqrt(rmax * As * np.pi ** 2 / 2); rho4 = 3 * aH ** 2; MP = 2.4353e18; V14 = rho4 ** .25 * MP
check('D1 with M_P = 1/a (CL-5: G = a^2/8pi), Delta_t^2 = 2(aH)^2/pi^2 and r < 0.036 force aH < %.2e: formation horizon > %.2e cells '
      '(%.1f rungs), energy density < %.1e per cell^4 (V^1/4 < %.1e GeV); the tick\'s own scale (aH ~ 1) gives r ~ 1e8'
      % (aH, 1 / aH, np.log2(1 / aH), rho4, V14), np.log2(1 / aH) > 15)
gs0, gst, T0K, kst = 43 / 11, 106.75, 2.7255 * 8.617333e-14, 0.05 / Mpc * 1.97327e-16
Hs = aH * MP; TRH = (30 * 3 * Hs ** 2 * MP ** 2 / (np.pi ** 2 * gst)) ** .25; aend = (gs0 / gst) ** (1 / 3) * T0K / TRH; Ns = np.log(aend * Hs / kst)
check('D2 supplied single-clock bookkeeping at that H (instant thermalisation, T = %.1e GeV): N* = %.1f e-folds = %.1f rungs, -2/N* gives '
      'n_s = %.4f; rung budget %.1f + %.1f + %.1f = %.1f = pivot ladder (an identity: the split is not a ruleset number)'
      % (TRH, Ns, Ns / np.log(2), 1 - 2 / Ns, Ns / np.log(2), np.log2(1 / aH), np.log2(1 / aend), Ns / np.log(2) + np.log2(1 / aH) + np.log2(1 / aend)),
      abs(Ns / np.log(2) + np.log2(1 / aH) + np.log2(1 / aend) - lad['a 1/k*']) < 0.05)
av = {}
for k, v in list(base.items()) + [('1/6', 1 / 6), ('1/4', .25)]:
    if v < 1:
        for e_ in range(1, 61):
            for r_ in pre + [1 / (8 * np.pi ** 2), 1 / (2 * np.pi ** 2), 2 / np.pi ** 2]: av.setdefault(round(np.log(r_ * v ** e_), 9), f'{r_:.3g}*({k})^{e_}')
inA = [x for x in av if np.log(1e-10) <= x <= np.log(1e-8)]; hA = sorted((abs(x - np.log(As)), av[x]) for x in inA if abs(x - np.log(As)) < dlnA)
eA = len(inA) * 2 * dlnA / np.log(100); cl = min((abs(x - np.log(As)), av[x], x) for x in inA)
check('D3 A_s = 2.10e-9 from ruleset ratios r*c^e: %d hits within 1 sigma (1.4%%) vs %.1f expected by chance; nearest %s = %.3e (%.1f sigma)'
      % (len(hA), eA, cl[1], np.exp(cl[2]), cl[0] / dlnA), eA >= 1 and len(hA) <= 3 * eA + 3)
print('supplied: CL-2 tick at (mu,b) in {(0,.3),(.4,.3)}; Wilsonian light projection as the rung map on odds; the band choice of the')
print('  cone states; P_delta ~ k^n_s at fixed time; a = sqrt(8pi) l_P; tensor amplitude 2H^2/(pi^2 M_P^2), -2/N, thermal history (D2,')
print('  C3 comparators only); Planck 2018 n_s, running, A_s; BICEP/Keck r < 0.036; H0 = 67.4.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
