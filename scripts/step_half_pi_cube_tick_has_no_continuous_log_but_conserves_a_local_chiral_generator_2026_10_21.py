#!/usr/bin/env python3
"""chiral-step: exact sublattice chirality against the vacuum bound on the CL-2 cube tick.

Supplied model: the CL-2 Margolus tick on Z^3 (one fermion mode per site, spin-3/2 edge hop W on 2x2x2 cubes, two
tilings offset by (1,1,1)), Bloch form U(K) = [D(K)^+ X D(K)] Y for odd-tiling X after even-tiling Y; eps = sublattice
sign, R = pi(1,1,1).  Sections:
 A  Floquet reading: the vacuum bound rederived (band max, wrap count, two-pair resonance at step pi/2, cosmic cap).
 B  exact-energy reading: continuous logarithm for eps < pi/2, none at step pi/2; the commutator generator
    H' = (i/2)[W_o, W_e] = (i/2)(U - U^+) of the step-pi/2 tick (local, chiral, cones at Gamma and R).
 C  cube-layer ticks with exact chirality: charge uniqueness, zero on-site return, R-image, velocity span at Gamma.
 D  estimates against measurement.
Finite diagnostics of supplied models unless a line says theorem.  Cited, not rederived: Floquet Nielsen-Ninomiya
(net chirality at 0 = at pi = -W3, W3 = 0 for finite-range walks), the SMG conjecture, chiral-smg C6 (Z3 window index).
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/STEP_HALF_PI_CUBE_TICK_HAS_NO_CONTINUOUS_LOG_BUT_CONSERVES_A_LOCAL_CHIRAL_GENERATOR_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
from scipy.linalg import expm, null_space

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
rng = np.random.default_rng(20261021)

# ------------------------------------------------ the CL-2 cube objects ------------------------------------------------
C = np.array(list(itertools.product((0, 1), repeat=3))); cc = C - 0.5; I8 = np.eye(8)
EPS = np.diag((-1.0) ** C.sum(1)).astype(complex)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: g_ = XI[a].conj() @ XI[b]; W[a, b] = -g_ / abs(g_) / np.sqrt(3)
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1): rots.append(R)
def axang(R):
    a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(a)), a
def img(R, i): return int(np.argmin(np.sum(abs(cc - R @ cc[i]), 1)))
def Lrot(R):
    n_, a = axang(R); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
Ls = [Lrot(R) for R in rots]
ODD = [abs(np.trace(L @ EPS @ L.conj().T @ EPS).real / 8 + 1) < 1e-9 for L in Ls]
TL = [L for L, o in zip(Ls, ODD) if not o]
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def odd(X, K): D = Dg(K); return D.conj().T @ X @ D
def qe(U): return -np.angle(np.linalg.eigvals(U))
Rv = np.full(3, np.pi); Cd = [np.diag(C[:, a].astype(complex)) for a in range(3)]
ALPHA = [Cd[a] - W @ Cd[a] @ W for a in range(3)]                       # step-pi/2 velocities (block-local)
VA = np.sqrt(np.trace(ALPHA[0] @ ALPHA[0]).real / 8)
G5 = 1j * ALPHA[0] @ ALPHA[1] @ ALPHA[2] / VA ** 3; G5 = (G5 + G5.conj().T) / 2
Q = [-1j * (Cd[a] @ G5 - G5 @ Cd[a]) for a in range(3)]
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W
def Ucl(K, e, mu=0.0):                                                   # CL-2 tick, symmetric frame
    Eh = ex(-(e - mu / 2) / 2); return Eh @ odd(ex(e + mu / 2), K) @ Eh
def Upi(K): return odd(W, K) @ W                                         # step pi/2, mu = 0 (unsplit frame)
def Hp(K): Wo = odd(W, K); return 0.5j * (Wo @ W - W @ Wo)              # H' = (i/2)[W_o, W_e]
Smean = lambda K: np.mean(np.cos(K), -1)
KR = rng.uniform(-np.pi, np.pi, (24, 3))
g6 = np.linspace(-np.pi, np.pi, 6, endpoint=False); KG = np.array(list(itertools.product(g6, g6, g6)))

# ===================================== A. Floquet reading: the vacuum bound =====================================
print('== A. Floquet reading')
bm = {e: max(np.abs(qe(Ucl(K, e))).max() for K in np.vstack([KG, Rv])) for e in (0.04, 0.3, 1.0, np.pi / 2)}
yee = {e: 2 * np.arcsin(min(1.0, np.sqrt(3) * np.sin(e) / np.sqrt(3))) for e in bm}
npair = {e: int(np.ceil(2 * np.pi / (4 * e) - 1e-12)) for e in (0.04, 0.3, np.pi / 4, np.pi / 2)}
check('A1 theorem: band max of the CL-2 tick and of its Courant-matched photon is 2 eps; a pair carries <= 4 eps, so a wrap'
      ' to 2pi needs >= ceil(pi/(2 eps)) pairs', all(abs(bm[e] - 2 * e) < 1e-9 and abs(yee[e] - 2 * e) < 1e-12 for e in bm)
      and npair == {0.04: 40, 0.3: 6, np.pi / 4: 2, np.pi / 2: 1}, f'pairs needed at eps .04/.3/(pi/4)/(pi/2): {list(npair.values())}')
def wband(K, e):
    b = np.pi / 2 - e; A = (np.cos(2 * b) + 1) / 2
    return np.arccos(np.clip(A * Smean(K) - (np.cos(2 * b) - 1) / 2, -1, 1))
Ns = 60000; K1, K2, K3 = rng.uniform(-np.pi, np.pi, (3, Ns, 3)); K4 = K1 + K3 - K2      # p1 + p2 = h1 + h2
Fpi = wband(K1, np.pi / 2) + wband(K2, np.pi / 2) + wband(K3, np.pi / 2) + wband(K4, np.pi / 2) - 2 * np.pi
F04 = wband(K1, .04) + wband(K2, .04) + wband(K3, .04) + wband(K4, .04) - 2 * np.pi
check('A2 two particle-hole pairs at total momentum 0: at step pi/2 the mismatch to 2pi changes sign over the sample (open'
      ' resonance, rate ~ alpha^2 per cell-tick); at eps .04 it stays below 8 eps - 2pi', 0.3 < np.mean(Fpi > 0) < 0.7
      and F04.max() <= 8 * .04 - 2 * np.pi + 1e-9, f'step pi/2 fraction >0: {np.mean(Fpi > 0):.3f}; eps .04 max {F04.max():+.3f}')
rcap = 4.8e-6 / (2 * np.pi * 2.109e18 * (4.35e17 / 3.12e-43) / 1.62e-32 ** 3)
emax = {k: k * np.pi / np.log(1 / rcap) for k in (1.0, 2.0, np.log(137.036))}
print(f'   estimate: wraps inject 2pi hbar/tau each; rho_crit over the age caps the rate at {rcap:.1e} per cell-tick;'
      f' rate ~ exp(-kappa pi/eps) gives eps_max = {emax[1.0]:.4f}, {emax[2.0]:.4f}, {emax[np.log(137.036)]:.4f}'
      f' for kappa = 1, 2, ln(1/alpha); step pi/2 (alpha^2) misses by 1e{int(np.log10((1 / 137.036) ** 2 / rcap))}')
print('   cited (onecopy-verify tick S, e = pi/3): Gamma levels +-2pi/3, zone band max 2.618 (scratch scan) -> two pairs reach'
      ' 10.5 > 2pi, same bound; scaled S (e .04, phases .06/.02): band max 0.100, 4 light states kept (scratch explore_S.py)')

# ===================================== B. exact-energy reading =====================================
print('== B. exact-energy reading')
N = 12; gN = 2 * np.pi * np.arange(N) / N; KN = np.array(list(itertools.product(gN, gN, gN)))
def shells(Hfun):
    Hk = np.array([Hfun(K) for K in KN]).reshape(N, N, N, 8, 8); hr = np.fft.ifftn(Hk, axes=(0, 1, 2))
    d = np.minimum(np.arange(N), N - np.arange(N)); Dm = np.maximum.reduce(np.meshgrid(d, d, d, indexing='ij'))
    return [float(np.abs(hr[Dm == s]).max()) for s in range(1, 6)]
def plog(U): w, V = np.linalg.eig(U); return V @ np.diag(1j * np.log(w)) @ np.linalg.inv(V)
sh03 = shells(lambda K: plog(Ucl(K, 0.3))); shpi = shells(lambda K: plog(Upi(K)))
jR = [nrm(plog(Ucl(Rv + q * np.eye(3)[0], 0.3)) - plog(Ucl(Rv + q * np.eye(3)[1], 0.3))) for q in (1e-2, 1e-4)]
anti = max(nrm(EPS @ plog(Ucl(K, e, mu)) @ EPS + plog(Ucl(K, e, mu))) for K in KR[:6] for e, mu in ((0.3, 0.0), (1.0, 0.2), (0.04, 0.01)))
check('B1 eps < pi/2: the principal log H_F of the tick is continuous at R and its hops fall off fast; eps H_F eps = -H_F at'
      ' every eps and mass, so this reading has no conserved chiral charge', jR[1] < 1e-4
      and sh03[4] / sh03[0] < 1e-3 and anti < 1e-9,
      f'eps .3 shells 1..5: ' + ' '.join(f'{x:.0e}' for x in sh03) + f'; anti {anti:.0e}')
jpi = [nrm(plog(Upi(Rv + q * np.eye(3)[0])) - plog(Upi(Rv + q * np.eye(3)[1]))) for q in (1e-2, 1e-4)]
jG = [nrm(plog(Upi(q * np.eye(3)[0])) - plog(Upi(q * np.eye(3)[1]))) for q in (1e-2, 1e-4)]
hyp = nrm(Upi(np.zeros(3)) - I8) + nrm(Upi(Rv) + I8)
rpi = min(shpi[s + 1] / shpi[s] for s in (1, 2, 3)); r03 = max(sh03[s + 1] / sh03[s] for s in (1, 2, 3))
check('B2 theorem (rank lemma, proof in report): at step pi/2, U(0) = 1 and U(R) = -1 with conical bands, and no continuous'
      ' log exists; the principal log jumps at R by a q-independent amount and its hops fall off only as a power',
      hyp < 1e-14 and abs(jpi[0] - jpi[1]) < 1e-2 and jpi[1] > 1 and jG[1] < 1e-3 and rpi > 0.2 and r03 < 0.02,
      f'jump at R {jpi[1]:.3f} (q 1e-4), at Gamma {jG[1]:.0e}; shells ' + ' '.join(f'{x:.0e}' for x in shpi) + f'; shell ratios >= {rpi:.2f} (eps .3: <= {r03:.0e})')
idn = max(nrm(Hp(K) - 0.5j * (Upi(K) - Upi(K).conj().T)) for K in KR)
cm = max(nrm(Hp(K) @ Upi(K) - Upi(K) @ Hp(K)) for K in KR)
ce = max(nrm(EPS @ Hp(K) - Hp(K) @ EPS) for K in KR)
cov = max(nrm(L @ Hp(K) @ L.conj().T - Hp(R @ K)) for L, R in zip(Ls, rots) for K in KR[:3])
spec = max(np.abs(np.linalg.eigvalsh(Hp(K)) - np.repeat([-1, 1], 4) * np.sqrt(1 - Smean(K) ** 2)).max() for K in KR)
rim = max(nrm(Hp(K + Rv) + Hp(K)) for K in KR)
check('B3 theorem: H\' = (i/2)[W_o,W_e] = (i/2)(U - U^+) commutes with the step-pi/2 tick, with eps and with the 24 turns;'
      ' its bands are +-sqrt(1 - S^2), fourfold, zero only at Gamma and R; H\'(K+R) = -H\'(K)',
      max(idn, cm, ce, cov, spec, rim) < 1e-12, f'max residual {max(idn, cm, ce, cov, spec, rim):.0e}')
h = 1e-6
vG = [(Hp(np.eye(3)[a] * h) - Hp(-np.eye(3)[a] * h)) / (2 * h) for a in range(3)]
vR = [(Hp(Rv + np.eye(3)[a] * h) - Hp(Rv - np.eye(3)[a] * h)) / (2 * h) for a in range(3)]
clif = max(nrm(ALPHA[a] @ ALPHA[b] + ALPHA[b] @ ALPHA[a] - 2 * (a == b) * I8 / 3) for a in range(3) for b in range(3))
g5R = 1j * vR[0] @ vR[1] @ vR[2] / VA ** 3
sect = [sorted(np.round(np.linalg.eigvalsh(((I8 + s * EPS) / 2) @ g @ ((I8 + s * EPS) / 2)), 6)[np.abs(np.linalg.eigvalsh(((I8 + s * EPS) / 2) @ g @ ((I8 + s * EPS) / 2))) > .5])
        for g in (G5, (g5R + g5R.conj().T) / 2) for s in (1, -1)]
check('B4 cones: velocity at Gamma is the step-pi/2 Clifford triple alpha_a = C_a - W C_a W (speed 1/sqrt3 block), at R it'
      ' is -alpha, so gamma5 flips; each eps-sector holds one L and one R Weyl at each node',
      max(nrm(x - y) for x, y in zip(vG, ALPHA)) < 1e-8 and max(nrm(x + y) for x, y in zip(vR, ALPHA)) < 1e-8 and clif < 1e-12
      and nrm(g5R + G5) < 1e-6 and all(s_ == [-1.0, -1.0, 1.0, 1.0] for s_ in sect), f'speed {VA:.6f}')
Lt = 6; sites = np.array(list(itertools.product(range(Lt), repeat=3))); idx = {tuple(s_): i for i, s_ in enumerate(sites)}
def layer(off):
    M = np.zeros((Lt ** 3, Lt ** 3), complex)
    for b0 in itertools.product(range(0, Lt, 2), repeat=3):
        X = np.array(b0) + off + C; ids = [idx[tuple(v_ % Lt)] for v_ in X]; rs = [int(((v_ - off) % 2) @ [4, 2, 1]) for v_ in X]
        M[np.ix_(ids, ids)] = W[np.ix_(rs, rs)]
    return M
We_, Wo_ = layer(np.zeros(3, int)), layer(np.ones(3, int)); Hr = 0.5j * (Wo_ @ We_ - We_ @ Wo_)
disp = {}
for i, j in zip(*np.nonzero(np.abs(Hr) > 1e-12)):
    d_ = tuple(int(v_) for v_ in sorted(np.abs(((sites[j] - sites[i] + 3) % Lt) - 3))); disp[d_] = round(float(max(disp.get(d_, 0), abs(Hr[i, j]))), 4)
incube = sum(any(all(((sites[i] - o) % Lt) // 2 == ((sites[j] - o) % Lt) // 2) for o in (np.zeros(3, int), np.ones(3, int)))
             for i, j in zip(*np.nonzero(np.abs(Hr) > 1e-12)))
check('B5 real space (6^3 torus): H\' has no on-site term; each site s carries one term moving a mode from the 3 neighbours of s'
      ' in its even cube to the 3 in its odd cube: straight 2-steps (|amp| 1/6) and face diagonals (1/3, two mediators), never'
      ' inside one cube', np.abs(np.diag(Hr)).max() < 1e-14 and disp == {(0, 0, 2): 0.1667, (0, 1, 1): 0.3333} and incube == 0,
      f'hops {disp}, intra-cube {incube}')
tau = 0.04; Ek = lambda K: expm(-1j * tau * Hp(K))
shf = shells(Ek); bmf = max(np.abs(qe(Ek(K))).max() for K in KG)
check('B6 the flow exp(-i tau H\') keeps eps exactly at every tau and has band max <= tau; its strict cone becomes a'
      ' Lieb-Robinson cone (tau = .04: shells beyond the range of H\' are nonzero, each <= 5 tau x the previous)', max(nrm(EPS @ Ek(K) - Ek(K) @ EPS) for K in KR[:6]) < 1e-12
      and bmf <= tau + 1e-12 and shf[2] > 0 and max(shf[1] / shf[0], shf[2] / shf[1]) < 5 * tau, f'band max {bmf:.4f}; shells 1..4 ' + ' '.join(f'{x:.0e}' for x in shf[:4]))

# ===================================== C. cube-layer ticks with exact chirality =====================================
print('== C. cube layers with exact chirality')
diagT = null_space(np.vstack([np.kron(I8, L.T)[:, ::9] - np.kron(L, I8)[:, ::9] for L in TL]), rcond=1e-9)
check('C1 theorem: the site-local charges covariant under the 12 even turns are span{1, eps} (orbits T+, T-)', diagT.shape[1] == 2
      and np.linalg.matrix_rank(np.column_stack([diagT, np.ones(8), np.diag(EPS).real]), tol=1e-8) == 2)
iE = np.where(np.diag(EPS).real > 0)[0]; iO = np.where(np.diag(EPS).real < 0)[0]
def ru(n): Qm, _ = np.linalg.qr(rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))); return Qm
def r_even(): M = np.zeros((8, 8), complex); M[np.ix_(iE, iE)] = ru(4); M[np.ix_(iO, iO)] = ru(4); return M
def r_odd(): M = np.zeros((8, 8), complex); M[np.ix_(iO, iE)] = ru(4); M[np.ix_(iE, iO)] = ru(4); return M
ret = 0
for t in range(4):
    Re, Ro, A_, B_ = r_odd(), r_odd(), r_even(), r_even()
    ret = max(ret, np.abs(np.diag(sum(odd(A_ @ Ro, K) @ B_ @ Re for K in KG) / len(KG))).max())
avgc = np.mean([np.cos(qe(Upi(K))).mean() for K in KG])
check('C2 theorem: in a two-layer tick whose layers are both sublattice-odd no mode returns to its site (every bond lies in'
      ' one cube only), so the zone average of tr U is 0 and some quasi-energy reaches |w| >= pi/2', ret < 1e-14 and abs(avgc) < 1e-14,
      f'on-site amplitude {ret:.0e}; CL-2 step pi/2 <cos w> = {avgc:.0e}')
devs = []
while len(devs) < 60:
    L = 2 * rng.integers(1, 4); par = rng.random(L) < 0.5
    if par.sum() % 2: continue
    word = [('e' if k % 2 == 0 else 'o', r_odd() if par[k] else r_even()) for k in range(L)]
    sig = (-1) ** int(sum(par[0::2])); K = rng.uniform(-np.pi, np.pi, 3)
    def U_w(K):
        M = I8
        for til, X in word: M = (odd(X, K) if til == 'o' else X) @ M
        return M
    devs.append(max(nrm(EPS @ U_w(K) - U_w(K) @ EPS), nrm(U_w(K + Rv) - sig * U_w(K))))
check('C3 theorem: an eps-conserving word of definite-parity layers obeys U(K+R) = sigma U(K), sigma = product of the even-'
      'tiling parities: the Gamma content recurs at R at quasi-energy 0 (sigma = +1) or pi (sigma = -1, so the band reaches pi/2)', max(devs) < 1e-12,
      f'60 random words, residual {max(devs):.0e}')
print('   with the cited Floquet Nielsen-Ninomiya per eps-sector (net chirality 0 at w = 0), C3 gives >= 4 Dirac tastes:'
      ' 2 at 0 + 2 at pi (step-pi/2 type) or 4 at 0')
def comm(gens):
    A_ = np.vstack([np.kron(I8, g.T) - np.kron(g, I8) for g in gens]); ns = null_space(A_, rcond=1e-9); return [ns[:, i].reshape(8, 8) for i in range(ns.shape[1])]
def hbasis(lst):
    M = np.array([np.concatenate([x.real.ravel(), x.imag.ravel()]) for x in lst]); _, s_, vh = np.linalg.svd(M, full_matrices=False)
    return [(v[:64] + 1j * v[64:]).reshape(8, 8) for v in vh[:int(np.sum(s_ > 1e-9))]]
def span_test(grp, nw=160):
    cm_ = comm(grp); H = [Y for X in cm_ for Y in (X + X.conj().T, 1j * (X - X.conj().T)) if nrm(Y) > 1e-9]
    ev = hbasis([(Y + EPS @ Y @ EPS) / 2 for Y in H]); od = hbasis([(Y - EPS @ Y @ EPS) / 2 for Y in H])
    def big():
        if rng.random() < 0.5: return expm(1j * sum(rng.normal() * Y for Y in ev))
        Z = sum(rng.normal() * Y for Y in od); w2, V2 = np.linalg.eigh(Z); return V2 @ np.diag(np.sign(w2)) @ V2.conj().T @ expm(1j * sum(rng.normal() * Y for Y in ev))
    trips = []
    for n in range(nw):
        word = [('e' if rng.random() < .5 else 'o', big()) for k in range(rng.integers(0, 7))]
        tau_ = 'e' if rng.random() < .5 else 'o'; X = sum(rng.normal() * Y for Y in ev)
        def f(K):
            M = I8
            for til, Y in word: M = (odd(Y, K) if til == 'o' else Y) @ M
            return M @ (odd(X, K) if tau_ == 'o' else X) @ M.conj().T
        trips.append([(f(np.eye(3)[a] * h) - f(-np.eye(3)[a] * h)) / (2 * h) for a in range(3)])
    A_ = np.array([np.concatenate([np.concatenate([t.real.ravel(), t.imag.ravel()]) for t in T]) for T in trips])
    _, s_, vh = np.linalg.svd(A_, full_matrices=False); r = int(np.sum(s_ > 1e-7 * s_[0])); return r, vh[:r], trips, len(ev)
vec = lambda T: np.concatenate([np.concatenate([t.real.ravel(), t.imag.ravel()]) for t in T])
res = lambda B, T: np.linalg.norm(vec(T) - (B @ vec(T)) @ B) / np.linalg.norm(vec(T))
kerQ = null_space(sum(Q), rcond=1e-9); kdim = [int(round(np.trace(kerQ.conj().T @ ((I8 + s * EPS) / 2) @ kerQ).real)) for s in (1, -1)]
rO, BO, trO, neO = span_test(Ls); rT, BT, trT, neT = span_test(TL)
killO = max(nrm(sum(T) @ kerQ) for T in trO); killT = max(nrm(sum(T) @ kerQ) for T in trT)
check('C4 small-band eps-exact ticks (all big layers cancel): every K-linear term at Gamma, at every order, is M Q_a with'
      ' Q_a = -i[C_a, G5] (O: real span {Q, iG5 Q}; T: adds eps Q, i eps G5 Q); sum_a Q_a has a 2-dim kernel in each eps-sector'
      ' that every sampled term kills: zero modes along the body diagonals, no isotropic cone; alpha is orthogonal',
      (neO, rO, neT, rT) == (2, 2, 4, 4) and res(BO, Q) < 1e-8 and res(BO, [1j * G5 @ q for q in Q]) < 1e-8
      and res(BT, [EPS @ q for q in Q]) < 1e-8 and kdim == [2, 2] and max(killO, killT) < 1e-7 and res(BT, ALPHA) > 0.999,
      f'ranks O {rO}, T {rT}; kernel per sector {kdim}; kill {max(killO, killT):.0e}')
def U4(K, d): return odd(expm(1j * d * G5), K) @ W @ odd(expm(1j * d * G5), K) @ W
r4 = {d: (max(nrm(EPS @ U4(K, d) - U4(K, d) @ EPS) for K in KR[:6]), max(np.abs(qe(U4(K, d))).max() for K in KG) / d) for d in (0.01, 0.04, 0.3)}
v4 = max(nrm((U4(np.eye(3)[a] * h, 0.04) - U4(-np.eye(3)[a] * h, 0.04)) / (2 * h)) for a in range(3))
check('C5 example: U = e^{i d G5}_o W_e e^{i d G5}_o W_e keeps eps exactly at every d with band max ~ 1.8 d, but its Gamma node'
      ' has zero velocity (quadratic)', all(c_ < 1e-12 for c_, _ in r4.values()) and all(1.7 < x < 1.9 for _, x in r4.values()) and v4 < 1e-8,
      'band max / d: ' + ', '.join(f'{x:.3f}' for _, x in r4.values()) + f'; |dU/dK| at Gamma {v4:.0e}')

# ===================================== D. estimates against measurement =====================================
print('== D. estimates (H\' as the chiral generator)')
mR = nrm(W + odd(W, Rv)); hel = max(np.ptp(np.linalg.eigvalsh(Hp(K))[4:]) for K in KR)
Am = np.vstack([np.kron(I8, a.T) + np.kron(a, I8) for a in ALPHA] + [np.kron(I8, EPS.T) - np.kron(EPS, I8)])
nmass = null_space(Am, rcond=1e-9).shape[1]; ncov = null_space(np.vstack([Am] + [np.kron(I8, L.T) - np.kron(L, I8) for L in TL]), rcond=1e-9).shape[1]
check('D1 masses {X, +-alpha} = 0 that keep eps span 4 dims with none invariant under the 12 even turns, so no covariant'
      ' chiral mass gaps the R doubler; the CL-2 mass (W_e + W_o) vanishes at R; bands fourfold (no helicity splitting), c = 0',
      mR < 1e-15 and hel < 1e-12 and (nmass, ncov) == (4, 0), f'chiral masses {nmass}, T-invariant {ncov}')
Pi = np.zeros((8, 8))
for i in range(8): Pi[int((1 - C[i]) @ [4, 2, 1]), i] = 1
php = {0: 1.0 + 0j}
while len(php) < 8:
    for a in list(php):
        for b in range(8):
            if b not in php and abs(W[a, b]) > 0:
                ia, ib = int(np.argmax(Pi[:, a])), int(np.argmax(Pi[:, b])); php[b] = np.conj(W[ia, ib] / (php[a] * W[a, b]))
Pinv = Pi @ np.diag([php[i] for i in range(8)])
PW = Pinv @ W
pres = max(nrm(Pinv @ W @ Pinv.conj().T - W), nrm(Pinv @ EPS @ Pinv.conj().T + EPS), nrm(Pinv @ G5 @ Pinv.conj().T + G5),
           max(nrm(Pinv @ Hp(K) @ Pinv.conj().T - Hp(-K)) for K in KR[:6]), nrm(PW @ EPS @ PW.conj().T - EPS),
           nrm(PW @ G5 @ PW.conj().T - G5), max(nrm(PW @ Hp(K) @ PW.conj().T + Hp(-K)) for K in KR[:6]))
g5ok = max(nrm(L @ G5 @ L.conj().T - G5) for L in Ls) + nrm(G5 @ W + W @ G5) + nrm(G5 @ EPS - EPS @ G5)
check('D2 the gamma5 term b G5 (a CPT-odd b_0 coefficient at Gamma) is eps-even and O-invariant; the inversion P flips eps and'
      ' G5, while PW keeps eps (so SU(2)_even), maps H\'(K) to -H\'(-K) and G5 to +G5: PW (the CPT analogue) forbids b',
      pres < 1e-12 and g5ok < 1e-12, 'a mirror-gapping rule must keep PW; lattice-scale b vs electron b-bounds << 1e-20 GeV')
fam = {'Q': 6, 'u': 3, 'd': 3, 'L': 2, 'e': 1, 'n': 1}
print(f'   N_nu: 4 tastes per species -> 2 light tastes per family after mirror gapping -> N_nu = 6 vs 2.984 +- 0.008'
      f' ({(6 - 2.984) / 0.008:.0f} sigma) unless the R doubler is gapped (no covariant eps-even mass at R; needs N = 0 mod 3, chiral-smg C6)')
print(f'   W_R: SU(2)_odd is as exact as SU(2)_even, so CL-5 allows a massless W_R; M_WR > 5-6.4 TeV needs v_R >~'
      f' {5e3 / (0.65 / np.sqrt(2)) / 1e3:.0f}-{6.4e3 / (0.65 / np.sqrt(2)) / 1e3:.0f} TeV from a breaking no law supplies')
print('   V-A: SU(2)_even acts on light-L + mirror-R at Gamma (L doublet after mirror gapping); at R the copies swap roles')
print(f'   light cone: speed 1/sqrt3 block for every species built on H\'; anisotropy is O(K^2): (E/M_lat)^2 ~'
      f' {(1e4 / (1.22e19 / 3)) ** 2:.0e} at 10 TeV; the photon must ride C = lambda/sqrt3 (symmetric-stress clause)')
print(f'   masses: every fermion mass is sublattice-odd, so it breaks eps; a mass needs an SU(2)_even x SU(2)_odd-charged field')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('theorems: A1, B2 (rank lemma), B3, C1-C3, D1-D2; finite: A2, B1, B4-B6, C4, C5; estimates: A3, D text. Supplied: tick, W, filling,'
      ' quantised links, rate model, unit map, covariance group, the continuous-time reading of B.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
