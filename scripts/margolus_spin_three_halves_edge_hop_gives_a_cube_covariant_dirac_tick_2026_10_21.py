#!/usr/bin/env python3
"""Supplied two-partition spin-3/2 edge hop: finite checks of unitarity,
cubic covariance, the Bloch band identity, and its small-momentum spectrum.
The geometry, rotation action and mass parameter are supplied model choices.
No physical identification or classification of other ticks is asserted.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300

import os, sys, signal, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

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
def Dj(j, n, a): J = Jm(j); return expm(-1j * a * sum(n[k] * J[k] for k in range(3)))
def coh(j):
    J = Jm(j); out = []
    for i in range(8):
        n = (2 * C[i] - 1.0) / np.sqrt(3); w, v = np.linalg.eigh(sum(n[k] * J[k] for k in range(3))); out.append(v[:, -1])
    return out
def rep(j, R, n=None, a=None):
    xi = coh(j); n, a = axang(R) if n is None else (n, a); D = Dj(j, n, a); L = np.zeros((8, 8), complex)
    for i in range(8):
        k = img(R, i); L[k, i] = xi[k].conj() @ D @ xi[i]
    return L
def tickK(Ks, X, W):
    Dg = np.exp(1j * (np.atleast_2d(Ks) @ C.T)); return (Dg.conj()[:, :, None] * X[None] * Dg[:, None, :]) @ W[None]
def om(Ks, X, W, cen=0.0): return np.angle(np.exp(1j * (-np.angle(np.linalg.eigvals(tickK(Ks, X, W))) - cen)))
rng = np.random.default_rng(7); dirs = rng.normal(size=(200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
N = 6; sites = np.array(list(itertools.product(range(N), repeat=3))); idx = {tuple(s): i for i, s in enumerate(sites)}
n = 20; g = (np.arange(n) + .5 - n / 2) * 2 * np.pi / n; KZ = np.vstack([np.array(list(itertools.product(g, g, g))), np.zeros((1, 3))])
def half(off):
    M = np.zeros((N**3, N**3), complex)
    for b in itertools.product(range(0, N, 2), repeat=3):
        xs = [(np.array(b) + off + s) % N for s in C]; ids = [idx[tuple(x)] for x in xs]; rs = [int((x % 2) @ [4, 2, 1]) for x in xs]
        for a in range(8):
            for e in range(8): M[ids[a], ids[e]] = W[rs[a], rs[e]]
    return M
print('== supplied spin-3/2 edge hop and finite band diagnostics')
x3 = coh(1.5); Gm = np.array([[x3[a].conj() @ x3[b] for b in range(8)] for a in range(8)])
edges = [(a, b) for a in range(8) for b in range(8) if np.sum(abs(C[a] - C[b])) == 1]
Wa = [np.zeros((8, 8), complex) for _ in range(3)]
for a, b_ in edges:
    ax = int(np.argmax(abs(C[a] - C[b_]))); Wa[ax][a, b_] = -Gm[a, b_] / abs(Gm[a, b_]) / np.sqrt(3)
W3 = sum(Wa)
def face_hol(j):
    xs = coh(j); cyc = [0, 1, 3, 2]   # face x=0: corners 000,001,011,010
    return np.prod([xs[cyc[(i + 1) % 4]].conj() @ xs[cyc[i]] for i in range(4)])
hol = {1.5: face_hol(1.5)}
print('   face holonomy phase / pi:', {j: round(np.angle(h) / np.pi, 4) for j, h in hol.items()})
check('spin-3/2 reference-face holonomy is -1 (pi flux)', abs(hol[1.5] + abs(hol[1.5])) < 1e-12)
L3 = [rep(1.5, R) for R in rots]
acomm = max(np.abs(Wa[a] @ Wa[b_] + Wa[b_] @ Wa[a] - (2 / 3) * (a == b_) * np.eye(8)).max() for a in range(3) for b_ in range(3))
check('W = Wx+Wy+Wz with {Wa,Wb} = (2/3) delta_ab: W Hermitian and W^2 = 1', acomm < 1e-12 and np.allclose(W3, W3.conj().T) and np.allclose(W3 @ W3, np.eye(8)), f'{acomm:.1e}')
check('W commutes with the 24 spin-3/2 corner actions', max(np.abs(L @ W3 - W3 @ L).max() for L in L3) < 1e-12)
W, xi = W3, x3
Uf = half(np.ones(3, int)) @ half(np.zeros(3, int))
def glob3(R, cen):
    Gl = np.zeros((N**3, N**3), complex); S = Dj(1.5, *axang(R))
    for i, x in enumerate(sites):
        y = np.rint(R @ (x - cen) + cen).astype(int) % N
        Gl[idx[tuple(y)], i] = xi[int((y % 2) @ [4, 2, 1])].conj() @ S @ xi[int((x % 2) @ [4, 2, 1])]
    return Gl
err = max(np.abs(glob3(R, cn) @ Uf - Uf @ glob3(R, cn)).max() for R in rots for cn in (np.full(3, .5), np.full(3, 1.5)))
check('lattice tick (6^3 sites) commutes with all 24 spin-3/2 rotations about both block centres', err < 1e-12, f'{err:.1e}')
def W3m(mu): return np.cos(mu / 2) * W3 + 1j * np.sin(mu / 2) * np.eye(8)
KR = rng.uniform(-np.pi, np.pi, size=(2000, 3)); emax = 0; quart = 0
for mu in (0.0, 0.1, 0.3):
    Wq = W3m(mu); ev = np.linalg.eigvals(tickK(KR, Wq, Wq)); w_ = np.sort(np.abs(np.angle(ev)), 1)
    cw = np.cos(mu / 2)**2 * np.cos(KR).sum(1) / 3 - np.sin(mu / 2)**2
    emax = max(emax, np.abs(np.cos(w_) - cw[:, None]).max()); quart = max(quart, np.ptp(w_, 1).max())
check('all 8 bands obey cos w = cos^2(mu/2) S(K) - sin^2(mu/2), S = (cos Kx+cos Ky+cos Kz)/3 (2000 K, three mu)', emax < 1e-10, f'{emax:.1e}')
check('all eight sampled absolute quasienergies agree', quart < 1e-8)
for mu in (0.0, 0.1):
    Wq = W3m(mu)
    for kk in (0.1, 0.4):
        o = np.abs(om(kk * dirs, Wq, Wq)); ref = np.sqrt(mu**2 + kk**2 / 3)
        dev = abs(o.mean() / ref - 1); spr = np.ptp(o.mean(1)) / o.mean()
        check(f'mu={mu}, |k|={kk}: |w| = sqrt(mu^2 + k^2/3) within 0.25%, direction spread < 0.5%', dev < 2.5e-3 and spr < 5e-3, f'dev {dev:.1e}, spread {spr:.1e}')
Wq = W3m(0.1); dz = np.min(np.abs(om(KZ, Wq, Wq)), 1); w0 = np.abs(om(np.zeros((1, 3)), Wq, Wq))
check('mu=0.1: global gap = mu, reached at K=0 (zone grid min)', np.allclose(w0, 0.1) and dz.min() >= 0.1 - 1e-12, f'grid min {dz.min():.4f}')
wpi = np.abs(om(np.full((1, 3), np.pi), Wq, Wq))
check('mu=0.1: quasienergy magnitude pi at K=pi(1,1,1)', np.allclose(wpi, np.pi))
Ux = lambda K: tickK(K, W3, W3)[0]
def flux(sel, r=0.02, nt=20, nph=40):
    th_ = np.linspace(0, np.pi, nt + 1); ph_ = np.linspace(0, 2 * np.pi, nph + 1)[:-1]; V = {}
    for i, t in enumerate(th_):
        for k_, p in enumerate(ph_):
            K = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]); w_, v = np.linalg.eig(Ux(K)); o_ = -np.angle(w_)
            V[i, k_] = np.linalg.qr(v[:, [q for q in range(8) if sel(o_[q])]])[0]
    F = 0
    for i in range(nt):
        for k_ in range(nph):
            a, b2, c2, d2 = V[i, k_], V[i + 1, k_], V[i + 1, (k_ + 1) % nph], V[i, (k_ + 1) % nph]
            F += np.angle(np.linalg.det(a.conj().T @ b2) * np.linalg.det(b2.conj().T @ c2) * np.linalg.det(c2.conj().T @ d2) * np.linalg.det(d2.conj().T @ a))
    return F / (2 * np.pi)
fu = flux(lambda o: o > 0)
check('finite mesh Berry-flux diagnostic near K=0 agrees with zero', abs(fu) < 1e-6, f'{fu:+.2e}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

sys.exit(bool(FAIL))
