#!/usr/bin/env python3
"""Supplied Margolus tick, one fermion mode per site: block unitary W on even 2^3 blocks, then on odd blocks
shifted by (1,1,1). Rotations act on the site modes as corner permutations times phases (spin-j coherent
states along the body diagonals, j = 0, 1/2, 1, 3/2). Main check: for j = 3/2 the edge hop with the phases of
the neighbouring sites' spin-3/2 overlaps is unitary (pi flux per cube face), exactly covariant, and gives
cos(omega) = cos^2(mu/2) (cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2): two exactly degenerate isotropic Dirac
fermions at K = 0 and nothing else near omega = 0. Also: the j = 1/2 cone (E1/2 + G3/2) with its pinned
branch, the first-order selection rule, and the step-direction structure. Supplied model, finite diagnostic;
no physical identification and no classification of all ticks.
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
def commutant(Ls):
    A = np.vstack([np.kron(L, np.eye(8)) - np.kron(np.eye(8), L.T) for L in Ls])
    _, s, Vh = np.linalg.svd(A); nd = int(np.sum(s < 1e-9)); return nd, [b.reshape(8, 8) for b in Vh[-nd:].conj()]
def isotypic(Ls, B):
    rng = np.random.default_rng(1); M = sum(rng.normal() * b for b in B); M = M + M.conj().T
    w, V = np.linalg.eigh(M); out = []
    for val in np.unique(np.round(w, 6)):
        v = V[:, np.isclose(w, val, atol=1e-5)]; out.append(v @ v.conj().T)
    return out
def tickK(Ks, X, W):
    Dg = np.exp(1j * (np.atleast_2d(Ks) @ C.T)); return (Dg.conj()[:, :, None] * X[None] * Dg[:, None, :]) @ W[None]
def om(Ks, X, W, cen=0.0): return np.angle(np.exp(1j * (-np.angle(np.linalg.eigvals(tickK(Ks, X, W))) - cen)))
rng = np.random.default_rng(7); dirs = rng.normal(size=(200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
Rk = lambda d: np.diag(c @ d).astype(complex)

print('== 1. the four monomial rotation actions on the 8 corners')
fam = {}
for j in (0, 0.5, 1, 1.5):
    Ls = [rep(j, R) for R in rots]; nd, B = commutant(Ls); P = isotypic(Ls, B)
    fam[j] = (Ls, B, P)
    mono = all(np.allclose(abs(L), abs(L).round()) and np.allclose(L.conj().T @ L, np.eye(8)) for L in Ls)
    full = rep(j, rots[0], np.array([0, 0, 1.0]), 2 * np.pi)
    print(f'   j={j}: commutant dim {nd}, isotypic dims {sorted(round(np.trace(p).real) for p in P)}, 2pi rotation = {np.round(full[0,0].real,6)}')
    check(f'j={j} action is monomial unitary; 2pi rotation acts as (-1)^(2j)', mono and np.allclose(full, (-1) ** int(2 * j) * np.eye(8)))
Ls, B, P = fam[0.5]
st = [np.trace(Dj(0.5, *axang(R))).real for R in rots]
lab = {}
for p in P:
    d = round(np.trace(p).real); ch = [np.trace(p @ L).real for L in Ls]
    lab['G3/2' if d == 4 else ('E1/2' if np.allclose(ch, st, atol=1e-8) else 'E5/2')] = p
check('j=1/2 corner space = E1/2 + E5/2 + G3/2, multiplicity free', sorted(lab) == ['E1/2', 'E5/2', 'G3/2'])
P1, P5, PG = lab['E1/2'], lab['E5/2'], lab['G3/2']
Inv = np.eye(8)[::-1]
check('the corner inversion (pure mover) is NOT j=1/2 covariant', not all(np.allclose(Inv @ L, L @ Inv) for L in Ls))

print('== 2. canonical j=1/2 tick: W = P_E1/2 - exp(-i mu) P_G3/2 + exp(-i theta) P_E5/2 on both partitions')
th = -np.pi / 2
def Wc(mu): return P1 - np.exp(-1j * mu) * PG + np.exp(-1j * th) * P5
W = Wc(0.1); N = 6; sites = np.array(list(itertools.product(range(N), repeat=3))); idx = {tuple(s): i for i, s in enumerate(sites)}
def half(off):
    M = np.zeros((N**3, N**3), complex)
    for b in itertools.product(range(0, N, 2), repeat=3):
        xs = [(np.array(b) + off + s) % N for s in C]; ids = [idx[tuple(x)] for x in xs]; rs = [int((x % 2) @ [4, 2, 1]) for x in xs]
        for a in range(8):
            for e in range(8): M[ids[a], ids[e]] = W[rs[a], rs[e]]
    return M
Uf = half(np.ones(3, int)) @ half(np.zeros(3, int))
xi = coh(0.5)
def glob(R, cen):
    G = np.zeros((N**3, N**3), complex); S = Dj(0.5, *axang(R))
    for i, x in enumerate(sites):
        y = np.rint(R @ (x - cen) + cen).astype(int) % N
        G[idx[tuple(y)], i] = xi[int((y % 2) @ [4, 2, 1])].conj() @ S @ xi[int((x % 2) @ [4, 2, 1])]
    return G
err = max(np.abs(glob(R, cn) @ Uf - Uf @ glob(R, cn)).max() for R in rots for cn in (np.full(3, .5), np.full(3, 1.5)))
check('lattice tick (6^3 sites) commutes with all 24 spinor rotations about even and odd block centres', err < 1e-12, f'max {err:.1e}')
Ks = [2 * np.pi * np.array(k) / (N // 2) for k in itertools.product(range(N // 2), repeat=3)]
bl = np.sort(np.concatenate([np.angle(np.linalg.eigvals(tickK(K, W, W)[0])) for K in Ks])); la = np.sort(np.angle(np.linalg.eigvals(Uf)))
check('Bloch form U(K) = D(K)^dag W D(K) W reproduces the lattice spectrum', np.abs(bl - la).max() < 1e-10, f'{np.abs(bl-la).max():.1e}')

print('== 3. first-order selection rule at K = 0 (any X, W in the commutant)')
v0 = 0
for j in (0, 0.5, 1):
    Lj, Bj, Pj = fam[j]; Hs = [b + b.conj().T for b in Bj] + [1j * (b - b.conj().T) for b in Bj]
    for t in range(5):
        X = expm(-1j * sum(rng.normal() * h for h in Hs))
        Wx = expm(-1j * sum(rng.normal() * h for h in Hs)); Q = X @ Wx; ev, EV = np.linalg.eig(Q)
        pr = EV[:, np.isclose(ev, ev[0], atol=1e-6)]; Pq = pr @ np.linalg.pinv(pr)
        for d in dirs[:5]: v0 = max(v0, np.abs(Pq @ (Rk(d) - X @ Rk(d) @ X.conj().T) @ Pq).max())
check('multiplicity-free actions (j=0,1/2,1): linear K-term vanishes inside every eigenspace of U(0)', v0 < 1e-10, f'max {v0:.1e}')
b = lambda p: np.linalg.eigh(p)[1][:, np.linalg.eigh(p)[0] > .5]
e15 = max(np.abs(b(P1).conj().T @ Rk(d) @ b(P5)).max() for d in dirs)
s1 = np.array([np.linalg.svd(b(P1).conj().T @ Rk(d) @ b(PG), compute_uv=False) for d in dirs])
s5 = np.array([np.linalg.svd(b(P5).conj().T @ Rk(d) @ b(PG), compute_uv=False) for d in dirs])
sb = np.array([np.linalg.svd(np.vstack([b(P1).conj().T @ Rk(d) @ b(PG), b(P5).conj().T @ Rk(d) @ b(PG)]), compute_uv=False) for d in dirs])
check('E1/2-E5/2 position coupling vanishes; E1/2-G3/2 and E5/2-G3/2 are rank 2, isotropic, 1/sqrt6',
      e15 < 1e-12 and np.allclose(s1, 1 / np.sqrt(6)) and np.allclose(s5, 1 / np.sqrt(6)), f'{s1.mean():.6f}')
check('E1/2 and E5/2 both coupled to G3/2 is anisotropic (no double Dirac cone)', np.ptp(sb, 0).max() > 0.1, f'singular-value range {sb.min():.3f}..{sb.max():.3f}')

print('== 4. massless cone (mu = 0)')
W0 = Wc(0.0); k = 1e-3; o = om(k * dirs, W0, W0); o = np.sort(np.take_along_axis(o, np.argsort(abs(o), 1), 1)[:, :6], 1) / k
print('   six K=0 states, velocities (min/max over 200 directions):', np.round(o.min(0), 4), np.round(o.max(0), 4))
check('cone: +-c twofold each, c = sqrt(2/3) block per tick, isotropic to 1e-3; two zero-velocity states',
      np.allclose(o[:, [0, 1]], -np.sqrt(2 / 3), atol=1e-3) and np.allclose(o[:, [4, 5]], np.sqrt(2 / 3), atol=1e-3) and np.abs(o[:, 2:4]).max() < 1e-2)

print('== 5. massive version (mu = m = 0.1, theta = -pi/2)')
m = 0.1; Wm = Wc(m); n = 20; g = (np.arange(n) + .5 - n / 2) * 2 * np.pi / n; KZ = np.vstack([np.array(list(itertools.product(g, g, g))), np.zeros((1, 3))])
dz = np.min(abs(om(KZ, Wm, Wm, m)), 1)
check('global quasi-energy gap around the centre equals m (20^3 zone grid + K=0)', abs(dz.min() - m) < 1e-6, f'{dz.min():.6f}')
for kk, tol, iso in ((0.1, 0.01, 0.015), (0.2, 0.02, 0.03), (0.4, 0.03, 0.05)):
    o = om(kk * dirs, Wm, Wm, m); o = np.sort(np.take_along_axis(o, np.argsort(abs(o), 1), 1)[:, :6], 1); up, dn = o[:, -1], -o[:, 0]
    ref = np.sqrt(m**2 + (2 / 3) * kk**2); dev = max(abs(up.mean() / ref - 1), abs(dn.mean() / ref - 1)); spr = max(np.ptp(up) / up.mean(), np.ptp(dn) / dn.mean())
    check(f'|k|={kk}: light bands follow sqrt(m^2 + (2/3)k^2) within {tol:.0%}, direction spread < {iso:.1%}', dev < tol and spr < iso, f'dev {dev:.4f}, spread {spr:.4f}')
deg = np.sort(-np.angle(np.linalg.eigvals(tickK(KZ[::97], Wm, Wm))), 1)
check('every band is twofold degenerate at every sampled K', np.abs(deg[:, ::2] - deg[:, 1::2]).max() < 1e-8)

print('== 6. pinned spin-3/2 branch on the four body-diagonal lines')
pin = 0; off = 9
for t in range(6):
    a = rng.uniform(0, 2 * np.pi, 3); X = P1 + np.exp(-1j * a[0]) * PG + np.exp(-1j * a[1]) * P5; Wr = P1 + np.exp(1j * (a[0] - .3)) * PG + np.exp(1j * a[2]) * P5
    for ax in [(1, 1, 1), (1, -1, 1), (-1, 1, 1), (1, 1, -1)]:
        s = np.linspace(.05, np.pi, 30)[:, None] * np.array(ax); pin = max(pin, np.min(abs(om(s, X, Wr, .3)), 1).max())
    s = np.linspace(.3, np.pi, 30)[:, None] * np.array([1, 0, 0]); off = min(off, np.min(abs(om(s, X, Wr, .3)), 1).max())
check('a twofold level sits exactly at the G3/2 energy along every body-diagonal line (random X, W)', pin < 1e-12, f'max dev {pin:.1e}')
check('it is not pinned along (1,0,0)', off > 1e-2, f'{off:.3f}')

print('== 7. corner = step direction (mover)')
P0 = fam[0][2]; Wmv = Inv; mv = True
for s_i, s in enumerate(C):
    e = np.zeros(8); e[s_i] = 1; out = Wmv @ e; mv &= int(np.argmax(out)) == 7 - s_i
check('pure mover (corner inversion, permutation-covariant) sends corner s to 1-s: step d = 1-2s per half-tick', mv)
U1 = tickK(np.array([0.3, -0.2, 0.5]), Inv, Inv)[0]; vv = np.sort(np.angle(np.linalg.eigvals(U1))); ex = np.sort(np.angle(np.exp(-1j * (1 - 2 * C) @ np.array([0.3, -0.2, 0.5]))))
check('mover tick has bands exp(-i K.d), d in {+-1}^3 (one block-lattice diagonal step per tick)', np.allclose(vv, ex))
print('== 8. j=3/2: edge hop with spin-3/2 overlap phases (the Dirac tick)')
x3 = coh(1.5); Gm = np.array([[x3[a].conj() @ x3[b] for b in range(8)] for a in range(8)])
edges = [(a, b) for a in range(8) for b in range(8) if np.sum(abs(C[a] - C[b])) == 1]
Wa = [np.zeros((8, 8), complex) for _ in range(3)]
for a, b_ in edges:
    ax = int(np.argmax(abs(C[a] - C[b_]))); Wa[ax][a, b_] = -Gm[a, b_] / abs(Gm[a, b_]) / np.sqrt(3)
W3 = sum(Wa)
def face_hol(j):
    xs = coh(j); cyc = [0, 1, 3, 2]   # face x=0: corners 000,001,011,010
    return np.prod([xs[cyc[(i + 1) % 4]].conj() @ xs[cyc[i]] for i in range(4)])
hol = {j: face_hol(j) for j in (0.5, 1, 1.5)}
print('   face holonomy phase / pi:', {j: round(np.angle(h) / np.pi, 4) for j, h in hol.items()})
check('spin-3/2 transport around every cube face is -1 (pi flux); not so for j=1/2, 1', abs(hol[1.5] + abs(hol[1.5])) < 1e-12 and abs(np.angle(hol[0.5])) > .1 and abs(np.angle(hol[1])) > .1)
L3 = fam[1.5][0]
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
check('so the bands are +-w(K), each exactly fourfold', quart < 1e-8)
for mu in (0.0, 0.1):
    Wq = W3m(mu)
    for kk in (0.1, 0.4):
        o = np.abs(om(kk * dirs, Wq, Wq)); ref = np.sqrt(mu**2 + kk**2 / 3)
        dev = abs(o.mean() / ref - 1); spr = np.ptp(o.mean(1)) / o.mean()
        check(f'mu={mu}, |k|={kk}: |w| = sqrt(mu^2 + k^2/3) within 0.25%, direction spread < 0.5%', dev < 2.5e-3 and spr < 5e-3, f'dev {dev:.1e}, spread {spr:.1e}')
Wq = W3m(0.1); dz = np.min(np.abs(om(KZ, Wq, Wq)), 1); w0 = np.abs(om(np.zeros((1, 3)), Wq, Wq))
check('mu=0.1: global gap = mu, reached at K=0 (zone grid min)', np.allclose(w0, 0.1) and dz.min() >= 0.1 - 1e-12, f'grid min {dz.min():.4f}')
wpi = np.abs(om(np.full((1, 3), np.pi), Wq, Wq))
check('time-doubler: w = pi at K = pi(1,1,1) for every mu (not gapped by mu)', np.allclose(wpi, np.pi))
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
check('massless node at K=0 has zero net Berry flux (Dirac pair, not net-chiral)', abs(fu) < 1e-6, f'{fu:+.2e}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
