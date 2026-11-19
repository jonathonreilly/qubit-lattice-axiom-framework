#!/usr/bin/env python3
"""Mass from a rule on the supplied covariant Margolus spin-3/2 tick (CL-2 draft).
Checks: (1) the mass term is the block hop itself, W(mu) = W exp(i mu/2 W) = e^{i mu/2} exp(i(pi-mu)P_-);
(2) the staggered sign eps anticommutes with both partitions' hops, so eps U(mu) eps = U(-mu) and mu = 0 is
protected; (3) Floquet Hellmann-Feynman: the filled-sea value of the block hop B = psi^dag W psi is
<B> = 4 s I(s), s = sin(mu/2), I(s) = int sqrt((1+S)/(1-S+s^2(1+S))), the same on even and odd blocks,
checked against eigenvectors and a 6^3 real-space lattice; (4) a supplied NJL-type block rule
exp(i pi N_-) exp(i g B^2/2) in the Hartree (large-N) mean field: gap equation theta = g <B>, critical
coupling g_c = 1/(4 I0), unique nonzero root for g > g_c, attractor of the mean-field iteration;
(5) small-mass law g/g_c - 1 = (3 sqrt3/(2 pi^2 I0)) mu^2 ln(1/mu) + O(mu^2): power-law, not exponential.
Supplied model; Hartree mean field; filled negative-quasi-energy sea; no physical identification.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss

T0 = time.monotonic()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ---- the supplied CL-2 block hop (same construction as the covariant-tick runner)
C = np.array(list(itertools.product((0, 1), repeat=3))); c = C - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def img(R, i): return int(np.argmin(np.sum(abs(c - R @ c[i]), 1)))
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
J3 = Jm(1.5)
xi = []
for i in range(8):
    n = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v_[:, -1])
def Lrot(R):
    n, a = axang(R); D = expm(-1j * a * sum(n[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8):
        k = img(R, i); L[k, i] = xi[k].conj() @ D @ xi[i]
    return L
Ls = [Lrot(R) for R in rots]
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1:
            g_ = xi[a].conj() @ xi[b]; W[a, b] = -g_ / abs(g_) / np.sqrt(3)
I8 = np.eye(8); Pm = (I8 - W) / 2
def Wm(mu): return np.cos(mu / 2) * W + 1j * np.sin(mu / 2) * I8
def Dk(Ks): return np.exp(1j * (np.atleast_2d(Ks) @ C.T))
def U(Ks, mu):
    Dg = Dk(Ks); X = Wm(mu); Wodd = Dg.conj()[:, :, None] * X[None] * Dg[:, None, :]
    return Wodd @ X[None], Wodd
def Sof(Ks): return np.cos(np.atleast_2d(Ks)).sum(1) / 3
def sea_proj(Uk):
    lam, V = np.linalg.eig(Uk); Vi = np.linalg.inv(V); sel = (np.angle(lam) > 0)[:, None, :]   # w = -arg(lam) < 0
    return np.einsum('kai,kib->kab', V * sel, Vi), sel.sum(2)[:, 0]
eps = np.diag((-1.0) ** C.sum(1))
rng = np.random.default_rng(3)

print('== 1. the mass term is the block hop itself')
check('W Hermitian, W^2 = 1, commutes with the 24 spin-3/2 corner actions',
      np.allclose(W, W.conj().T) and np.allclose(W @ W, I8) and max(abs(L @ W - W @ L).max() for L in Ls) < 1e-12)
mu = 0.37
check('W(mu) = W exp(i mu/2 W) = e^{i mu/2} exp(i (pi - mu) P_-): mass = hop angle short of pi',
      np.allclose(Wm(mu), W @ expm(0.5j * mu * W)) and np.allclose(Wm(mu), np.exp(0.5j * mu) * expm(1j * (np.pi - mu) * Pm)))

print('== 2. staggered sign eps = (-1)^(x+y+z)')
Ks = rng.uniform(-np.pi, np.pi, (50, 3)); Up, Wo = U(Ks, mu); Un, _ = U(Ks, -mu)
check('eps W eps = -W; eps commutes with D(K); eps W_odd(K) eps = -W_odd(K)', np.allclose(eps @ W @ eps, -W) and np.allclose(eps @ U(Ks, 0)[1] @ eps, -U(Ks, 0)[1]))
check('eps U(mu) eps = U(-mu) at 50 random K (mu = 0 is an eps-symmetric point; mu is eps-odd)', np.allclose(eps @ Up @ eps, Un))
rot_par = [np.allclose(L @ eps @ L.conj().T, eps) or np.allclose(L @ eps @ L.conj().T, -eps) for L in Ls]
check('every rotation maps eps to +-eps (90-degree turns swap the sublattices), and B = psi^dag W psi is invariant', all(rot_par))

print('== 3. filled-sea value of the block hop (Floquet Hellmann-Feynman)')
def I_closed(Ks, s):
    S1m = (2 * np.sin(np.atleast_2d(Ks) / 2) ** 2).sum(1) / 3; S1p = 2 - S1m
    return np.sqrt(S1p / (S1m + s * s * S1p))
errs = []; erro = []
for mu in (0.05, 0.37, 1.1):
    Ks = rng.uniform(-np.pi, np.pi, (400, 3)); Uk, Wo = U(Ks, mu); P, nsea = sea_proj(Uk)
    Be = np.einsum('ab,kba->k', W, P).real
    Wme = Wm(mu); Pphi = Wme[None] @ P @ Wme.conj().T[None]                     # sea after the even half-tick
    Dg = Dk(Ks); Wodd0 = Dg.conj()[:, :, None] * W[None] * Dg[:, None, :]
    Bo = np.einsum('kab,kba->k', Wodd0, Pphi).real
    ref = 4 * np.sin(mu / 2) * I_closed(Ks, np.sin(mu / 2))
    errs.append(abs(Be - ref).max()); erro.append(abs(Bo - ref).max()); assert np.all(nsea == 4)
check('per K: Tr(P_sea W) = 2 sin(mu)(1+S)/sin|w| = 4 s sqrt((1+S)/(1-S+s^2(1+S))), 3 mu x 400 K', max(errs) < 1e-9, f'max {max(errs):.1e}')
check('odd blocks (state after the even half-tick) carry the same value', max(erro) < 1e-9, f'max {max(erro):.1e}')
N = 6; sites = np.array(list(itertools.product(range(N), repeat=3))); idx = {tuple(s): i for i, s in enumerate(sites)}
def half(off, X):
    M = np.zeros((N ** 3, N ** 3), complex)
    for b in itertools.product(range(0, N, 2), repeat=3):
        xs = [(np.array(b) + off + s) % N for s in C]; ids = [idx[tuple(x)] for x in xs]; rs = [int((x % 2) @ [4, 2, 1]) for x in xs]
        for a in range(8):
            for e in range(8): M[ids[a], ids[e]] = X[rs[a], rs[e]]
    return M
mu = 0.37; He, Ho = half(np.zeros(3, int), Wm(mu)), half(np.ones(3, int), Wm(mu)); Uf = Ho @ He
lam, V = np.linalg.eig(Uf); Vi = np.linalg.inv(V); sel = np.angle(lam) > 0; Pr = (V[:, sel]) @ Vi[sel]
Be_rs = np.trace(half(np.zeros(3, int), W) @ Pr).real / 27; Bo_rs = np.trace(half(np.ones(3, int), W) @ (He @ Pr @ He.conj().T)).real / 27
Kg = np.array([2 * np.pi * np.array(k) / 3 for k in itertools.product(range(3), repeat=3)])
Bb = (4 * np.sin(mu / 2) * I_closed(Kg, np.sin(mu / 2))).mean()
check('6^3 real-space lattice, filled sea (108 of 216 modes): per-block <B> on even and odd blocks = Bloch value',
      sel.sum() == 108 and abs(Be_rs - Bb) < 1e-9 and abs(Bo_rs - Bb) < 1e-9, f'{Be_rs:.10f} {Bo_rs:.10f} vs {Bb:.10f}')
eps_g = np.diag((-1.0) ** sites.sum(1))
check('real space: eps anticommutes with both half-tick hops (any edge hop on the bipartite lattice)',
      np.allclose(eps_g @ half(np.zeros(3, int), W) @ eps_g, -half(np.zeros(3, int), W)) and np.allclose(eps_g @ half(np.ones(3, int), W) @ eps_g, -half(np.ones(3, int), W)))

print('== 4. supplied NJL block rule exp(i pi N_-) exp(i g B^2/2), Hartree mean field')
# exact zone integral: six pyramids K = pi t (1,u,v) (and images); Jacobian pi^3 t^2; cube volume (2pi)^3
gu, wu = leggauss(48); edges_t = np.concatenate([[0.0], np.geomspace(1e-12, 1.0, 60)]); gt, wt = leggauss(14)
tn = np.concatenate([(a + b) / 2 + (b - a) / 2 * gt for a, b in zip(edges_t[:-1], edges_t[1:])])
tw = np.concatenate([(b - a) / 2 * wt for a, b in zip(edges_t[:-1], edges_t[1:])])
UU, VV = np.meshgrid(gu, gu, indexing='ij'); WUV = np.outer(wu, wu)
hx = (np.sin(np.pi * tn / 2) ** 2)[:, None, None]
hy = np.sin(np.pi * tn[:, None, None] * UU[None] / 2) ** 2; hz = np.sin(np.pi * tn[:, None, None] * VV[None] / 2) ** 2
S1m = 2 * (hx + hy + hz) / 3; S1p = 2 - S1m; WT = (tw * tn ** 2)[:, None, None] * WUV[None] * 6 * np.pi ** 3 / (2 * np.pi) ** 3
def I_of(s): return float(np.sum(WT * np.sqrt(S1p / (S1m + s * s * S1p))))
def dI_of(s): return float(np.sum(WT * (np.sqrt(S1p / S1m) - np.sqrt(S1p / (S1m + s * s * S1p)))))
I0 = I_of(0.0); g_c = 1 / (4 * I0)
Kgrid = (np.arange(160) + 0.5) / 160 * 2 * np.pi - np.pi
I0_grid = 0.0
for kx in Kgrid:
    KK = np.stack(np.meshgrid([kx], Kgrid, Kgrid, indexing='ij'), -1).reshape(-1, 3); I0_grid += I_closed(KK, 0.0).sum()
I0_grid /= 160 ** 3
print(f'   I0 = {I0:.10f}  (160^3 midpoint grid: {I0_grid:.6f});  g_c = 1/(4 I0) = {g_c:.10f}')
check('I0 by pyramid quadrature agrees with an independent midpoint grid to 2e-4', abs(I0 - I0_grid) < 2e-4, f'diff {I0 - I0_grid:.1e}')
ths = np.linspace(1e-3, np.pi / 2 - 1e-3, 120); Fv = np.array([np.sin(t) / t * I_of(np.sin(t)) for t in ths])
check('gap function F(theta) = (sin theta/theta) I(sin theta) strictly decreases on (0, pi/2): one root for each g in (g_c, g_max)',
      np.all(np.diff(Fv) < 0), f'F(0+) = {Fv[0]:.6f}, F(pi/2) = {Fv[-1]:.6f}; g_max = {1 / (4 * Fv[-1]):.6f}')
def mu_of_g(g):
    lo, hi = 1e-12, np.pi / 2 - 1e-12
    for _ in range(80):
        md = (lo + hi) / 2
        if 4 * g * np.sin(md) / md * I_of(np.sin(md)) > 1: lo = md
        else: hi = md
    return 2 * lo
rows = [(r, mu_of_g(r * g_c)) for r in (1.0001, 1.001, 1.01, 1.1, 1.5)]
print('   g/g_c -> mu:', '; '.join(f'{r}: {m:.4g}' for r, m in rows))
# direct Floquet mean-field iteration with eigenvectors on a K grid (no closed form used)
Kq = (np.arange(14) + 0.5) / 14 * 2 * np.pi - np.pi; KQ = np.array(list(itertools.product(Kq, Kq, Kq)))
def B_grid(th):
    P, _ = sea_proj(U(KQ, 2 * th)[0]); return np.einsum('ab,kba->k', W, P).real.mean()
g = 1.5 * g_c; th = 0.02; hist = []
for it in range(40):
    th = g * B_grid(th); hist.append(th)
Ig = lambda s: I_closed(KQ, s).mean()
lo, hi = 1e-6, np.pi / 2 - 1e-6
for _ in range(60):
    md = (lo + hi) / 2
    if 4 * g * np.sin(md) * Ig(np.sin(md)) > md: lo = md
    else: hi = md
check('mean-field iteration theta -> g <B>(theta) from eigenvectors (14^3 K, g = 1.5 g_c) converges from theta = 0.02 to the nonzero root',
      abs(hist[-1] - lo) < 1e-6 and abs(hist[-1] - hist[-2]) < 1e-8, f'theta_40 = {hist[-1]:.8f}, root {lo:.8f}')
check('theta = 0 is a repeller there (slope 4 g I0 > 1) and the root an attractor', 4 * g * Ig(0) > 1 and abs(hist[-1] - hist[-2]) < abs(hist[1] - hist[0]))
m_sc = 2 * lo; dirs = rng.normal(size=(100, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
o = np.abs(np.angle(np.linalg.eigvals(U(0.05 * dirs, m_sc)[0]))).min(1)
check('self-consistent band is the CL-2 band: isotropic within 1e-4 at |k| = 0.05 and gap = mu', np.ptp(o) / o.mean() < 1e-4 and abs(np.abs(np.angle(np.linalg.eigvals(U(np.zeros(3), m_sc)[0]))).min() - m_sc) < 1e-10, f'mu = {m_sc:.6f}, spread {np.ptp(o) / o.mean():.1e}')

print('== 5. small-mass law: power law, no exponential hierarchy')
a_th = 3 * np.sqrt(3) / (2 * np.pi ** 2)
res = []
for mu in (1e-2, 1e-3, 1e-4, 1e-5):
    s = np.sin(mu / 2); res.append((mu, dI_of(s) / mu ** 2))
xs = np.log(1 / np.array([r[0] for r in res])); ys = np.array([r[1] for r in res]); A, Bc = np.polyfit(xs, ys, 1)
print('   (I0 - I)/mu^2 at mu = 1e-2..1e-5:', ' '.join(f'{y:.6f}' for y in ys))
check('I0 - I(sin(mu/2)) = a mu^2 ln(1/mu) + b mu^2 with a = 3 sqrt3/(2 pi^2) (rederived from the K=0 cone)', abs(A / a_th - 1) < 1e-3, f'fit a = {A:.6f}, theory {a_th:.6f}, b = {Bc:.4f}')
mu_e = 2 / np.sqrt(3) * np.sqrt(8 * np.pi) * 0.51099895e-3 / 1.220890e19
tune = (a_th * np.log(1 / mu_e) + Bc) * mu_e ** 2 / I0 + mu_e ** 2 / 24
print(f'   electron-scale mu ~ {mu_e:.3e} (supplied units: a = sqrt(8 pi) l_P, c = 1/sqrt3 block/tick) needs g/g_c - 1 = {tune:.2e}')
check('a mass of order 1e-22 needs g tuned to g_c to about 1e-42 (no natural hierarchy from the contact rule)', 1e-44 < tune < 1e-40)
print('supplied: the B^2 block rule and its coupling g, the Hartree (large-N) decoupling, the negative-quasi-energy sea.')
print('not established: any species mass value or ratio; Fock/fluctuation corrections; physical identification.')
print('elapsed_seconds', round(time.monotonic() - T0, 1))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
