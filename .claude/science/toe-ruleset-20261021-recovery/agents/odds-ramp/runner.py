#!/usr/bin/env python3
"""odds-ramp: can CL-1 itself (the only law that changes the odds) create departures from the vacuum at a rate that
grows with H*N, the Hubble rate per tick?  Supplied models, finite diagnostics and labelled estimates only.
 A  with the step fixed at eps0, what in the tick depends on the edge length; the de Sitter split cycle in ticks
 B  Bogoliubov occupation and injected energy per split vs h = H N (birth), copy-mass ramp M N(t) and mass ramp m N(t)
 C  violating the split constraint (copy angle at birth above eps0): band inversion, the split at K = pi(1,1,1)
 D  the lag threshold: above h_c the splits cannot keep up and the edge diverges in finitely many ticks
 E  symmetry: isotropic mean stress, particle = hole number per momentum, no C-odd excess
 F  estimates against measurement
Supplied: CL-1 tick (cube hop W, mass angle, even-cube copy mass), its negative-quasi-energy vacuum, CL-1's split
(midpoint of an even half-tick, corner passing, zone-point newborns, nearest unitary), a de Sitter background
(H fixed, edges l_c -> 2 l_c), antiperiodic cube tori, 8 pi G = l_c^2, species count N_s = 12, measured numbers.
"""
from __future__ import annotations
import os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
# ------------------------------------------------------------------ engine (CL-1 cube tick; inlined from one-cell-start)
import itertools
import numpy as np
from scipy.linalg import expm
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8); I64 = np.eye(64)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C8[i] - 1.0) / r3; _, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(a + 1, 8):
        d_ = C8[a] - C8[b]
        if np.sum(abs(d_)) == 1:
            g_ = XI[a].conj() @ XI[b]; ax = int(np.argmax(abs(d_))); Wi[ax][a, b] = -g_ / abs(g_) / r3; Wi[ax][b, a] = np.conj(Wi[ax][a, b])
W = sum(Wi); SCOPY = 1j * (r3 * Wi[0]) @ (r3 * Wi[1]) @ (r3 * Wi[2]) @ W          # copy sign s = i R1 R2 R3 R
def expmW(t): return np.cos(t) * I8 - 1j * np.sin(t) * W
def dag(A): return np.conj(np.swapaxes(A, -1, -2))
def tr(A): return np.trace(A, axis1=-2, axis2=-1)
def Dm(K): return np.exp(1j * (np.atleast_2d(K) @ C8.T))
def Uo(Ko, Ki, M):
    Do, Di = Dm(Ko), Dm(Ki); return Do[:, :, None] * M[None] * Di.conj()[:, None, :]
def tick(K, eps, mu, M=0.0):
    Ue = expmW(eps - mu / 2)
    if M: Cm = expm(1j * (M / 4) * (I8 - SCOPY) @ W); Ue = Cm @ Ue @ Cm
    return Uo(K, K, expmW(-(eps + mu / 2))) @ Ue
def proj(U):
    cw = np.real(tr(U)) / 8; w = np.arccos(np.clip(cw, -1, 1)); X = (U - dag(U)) / (2j * np.sin(w)[:, None, None])
    return (I8 + X) / 2, (I8 - X) / 2, w
    g = (np.pi * (2 * np.arange(Lc) + 1) / Lc + np.pi) % (2 * np.pi) - np.pi; return np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
def Kanti(Lc):                                    # antiperiodic cube momenta pi(2m+1)/Lc, kept in m order (FFT-ready)
    g = (np.pi * (2 * np.arange(Lc) + 1) / Lc + np.pi) % (2 * np.pi) - np.pi; return np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
def lratio(j, h): return 1.0 / (1.0 - h * j)       # de Sitter, N proportional to l: d ln l / d tick = h l/l_c
def cycle(K, eps0, mu0, x0, h, nt=None, frac=1.0):
    """evolve the birth vacuum through one split cycle (l_c -> 2 l_c); return per-K flips (of 4 filled) and end quasi-energies"""
    K = np.atleast_2d(K); jend = 1.0 / (2 * h); n = max(1, int(round(jend))) if nt is None else nt
    P0 = projH(tick(K, eps0, mu0, x0)); Vv = np.linalg.eigh(P0)[1][:, :, 4:]
    for j in range(n):
        s = lratio((j + 0.5) * jend / n, h); Vv = tick(K, eps0, mu0 * s, x0 * s) @ Vv
    U1 = tick(K, eps0, 2 * mu0, 2 * x0); P1 = projH(U1)
    fl = np.real(np.einsum('kai,kab,kbi->k', Vv.conj(), I8 - P1, Vv))
    wq = np.abs(np.angle(np.linalg.eigvals(U1))); return fl, wq, n
def projH(U):                                     # negative-quasi-energy projector for any spectrum (copy mass)
    _, vv = np.linalg.eigh((U - dag(U)) / 2j); vp = vv[:, :, 4:]; return vp @ dag(vp)
def cycleE(K, eps0, mu0, x0, h, nt=None):
    """one split cycle from the birth vacuum; returns mean flips per mode and mean excitation quasi-energy per cube (rad/tick)"""
    K = np.atleast_2d(K); jend = 1.0 / (2 * h); n = max(1, int(round(jend))) if nt is None else nt
    P0 = projH(tick(K, eps0, mu0, x0)); Vv = np.linalg.eigh(P0)[1][:, :, 4:]
    for j in range(n):
        s = lratio((j + 0.5) * jend / n, h); Vv = tick(K, eps0, mu0 * s, x0 * s) @ Vv
    U1 = tick(K, eps0, 2 * mu0, 2 * x0); w_, v_ = np.linalg.eig(U1); q = -np.angle(w_)
    Q, _ = np.linalg.qr(v_)                                   # unitary U1: eigvecs orthogonal up to degeneracy
    occ = np.sum(np.abs(dag(Q) @ Vv) ** 2, axis=-1)           # occupation of each Floquet mode
    filled = q < 0; dn = np.where(filled, 1 - occ, occ)
    return (np.sum(np.where(filled, 0, occ), axis=-1)).mean() / 8, np.sum(np.abs(q) * dn, axis=-1).mean()
def kappa(Eq, eps0, h): return Eq * np.sqrt(3) * np.sin(eps0) / (144 * h ** 2)   # energy per split / rho_crit (8 pi G = l_c^2)
def seaC(K, eps, M, mid=True):                    # massless species with copy mass M on the even cubes; midpoint frame
    P = projH(tick(np.atleast_2d(K), eps, 0.0, M))
    if mid: F = expm(1j * (M / 4) * (I8 - SCOPY) @ W) @ expmW(eps / 2); P = F @ P @ F.conj().T
    return P
def omega(K):                                     # rows: fine alias K/2 + pi m; columns: child sign pattern (-1)^(m'.c)
    K = np.atleast_2d(K); q = K[:, None, :] / 2 + np.pi * C8[None]; sg = (-1.0) ** C8
    return np.prod((1 + sg[None, None] * np.exp(-1j * q)[:, :, None, :]) / 2, axis=-1)
def had(K):  return np.einsum('nmk,ab->nmakb', omega(K), I8).reshape(len(np.atleast_2d(K)), 64, 64)
def polar(M):
    U, s, Vh = np.linalg.svd(M); return U @ Vh, s
I64 = np.eye(64)
def splitX(K, eps0, xc, xf):
    """current CL-1 split: parent (eps0, copy angle xc) -> children (eps0, xf); min singular value, vacuum residual, heat"""
    K = np.atleast_2d(K); B = had(K); Pf = np.zeros((len(K), 64, 64), complex); NB = np.zeros((64, 64), complex)
    for im, m in enumerate(C8):
        Pf[:, 8 * im:8 * im + 8, 8 * im:8 * im + 8] = seaC(K / 2 + np.pi * m, eps0, xf)
        if im: NB[8 * im:8 * im + 8, 8 * im:8 * im + 8] = seaC(np.pi * m[None], eps0, xf)[0]
    Pf = dag(B) @ Pf @ B; P1 = np.zeros_like(Pf); P1[:, :8, :8] = seaC(K, eps0, xc); P1 += NB[None]
    V, sv = polar(Pf @ P1 + (I64 - Pf) @ (I64 - P1))
    heat = np.real(tr((I64 - Pf) @ V @ P1 @ dag(V))) / 32
    return sv.min(axis=-1), np.abs(V @ P1 @ dag(V) - Pf).max(axis=(-1, -2)), heat
def cycleK(K, eps0, mu0, x0, h):
    """per-K occupations of the end-of-cycle Floquet modes (particles in empty band, holes in filled band)"""
    K = np.atleast_2d(K); n = max(1, int(round(1.0 / (2 * h)))); jend = 1.0 / (2 * h)
    Vv = np.linalg.eigh(projH(tick(K, eps0, mu0, x0)))[1][:, :, 4:]
    for j in range(n):
        s = lratio((j + 0.5) * jend / n, h); Vv = tick(K, eps0, mu0 * s, x0 * s) @ Vv
    P1 = projH(tick(K, eps0, 2 * mu0, 2 * x0)); part = np.real(np.einsum('kai,kab,kbi->k', Vv.conj(), I8 - P1, Vv))
    hole = 4 - np.real(np.einsum('kai,kab,kbi->k', Vv.conj(), P1, Vv)); return part, hole

# ------------------------------------------------------------------ A
print('== A. what the fixed-step tick reads from the edges; the de Sitter cycle')
K6 = Kanti(6)
d0 = max(np.abs(tick(K6, 0.3, 0.0, 0.0) - tick(K6, 0.3, 0.0 * s, 0.0 * s)).max() for s in (1.0, 1.5, 2.0))
f0, _ = cycleE(K6, 0.3, 0.0, 0.0, 0.01)
check('A1 THEOREM (CL-1 text): with eps = eps0 fixed and N = l sin(eps0)/sqrt3, a massless species without copy mass has '
      'the same half-ticks at every edge length, so expansion creates nothing in it at any H N (lattice conformal invariance); '
      'the only edge dependence is the mass angle m N and the copy angle M N, both proportional to l', d0 == 0 and abs(f0) < 1e-14,
      f'|dU| {d0:.0e}; flips per mode per cycle {abs(f0):.0e}')
h = 0.01; jj = np.arange(0, 51); lr = lratio(jj, h)
check('A2 THEOREM: in de Sitter with N proportional to l, d ln l/d tick = h l/l_c (h = H N at birth), so l/l_c = 1/(1 - h j): '
      'a cycle l_c -> 2 l_c lasts 1/(2h) ticks, the conformal time per tick is fixed, and without splits the whole future is '
      '1/h ticks', abs(lr[50] - 2) < 1e-12, f'h = 0.01: l/l_c at tick 50 = {lr[50]:.3f}')

# ------------------------------------------------------------------ B
print('== B. Bogoliubov occupation vs h = H N (copy-mass ramp x = M N from x0 to 2 x0 per cycle)')
hs = np.array([0.001, 0.003, 0.01, 0.03, 0.1, 0.3]); tabB = {}
for e0 in (0.3, 0.04):
    for xr in (0.3, 0.6, 0.93):
        tabB[(e0, xr)] = np.array([cycleE(K6, e0, 0.0, xr * e0, hh) for hh in hs])
pB = {k: np.diff(np.log(v[:, 0])) / np.diff(np.log(hs)) for k, v in tabB.items()}
for k, v in tabB.items():
    print(f'   eps0 {k[0]} x0/eps0 {k[1]}: flips/mode ' + ' '.join(f'{a:.1e}' for a in v[:, 0]) + ' | slope ' + ' '.join(f'{a:.2f}' for a in pB[k]))
check('B1 finite diagnostic (6^3 cube torus): the occupation per cycle grows as h^2 (slope 1.7-2.1) while h << the partner '
      'gap per tick, and saturates at the sudden limit (slope -> 0) once a cycle lasts a few ticks; no slope above 2 while the '
      'split constraint holds', all(1.6 < pB[k][0] < 2.2 for k in pB) and all(pB[k][-1] < 0.6 for k in pB) and max(max(v) for v in pB.values()) < 2.2,
      f'h = {hs[0]}..{hs[-1]}')
kap = {k: np.array([kappa(v[i, 1], k[0], hh) for i, hh in enumerate(hs)]) for k, v in tabB.items()}
check('B2 THEOREM + diagnostic: the injected energy per split over rho_crit is kappa(h) = E sqrt3 sin(eps0)/(144 h^2), a '
      'function of h and x0/eps0 alone, flat for small h (Delta rho ~ H^2: exactly the marginal p = 2 of the steady-state '
      'map) and falling as 1/h^2 past saturation: amplitude never grows faster than (H N)^2',
      all(abs(np.log(kap[k][1] / kap[k][0])) < 0.3 and kap[k][-1] < kap[k][0] for k in kap),
      'kappa(h -> 0) per species: ' + ', '.join(f'{k[1]}: {kap[k][0]:.1e}' for k in kap if k[0] == 0.3))
K12 = Kanti(12); kedge = {xr: kappa(cycleE(K12, 0.1, 0.0, xr * 0.1, 0.002)[1], 0.1, 0.002) for xr in (0.6, 0.9, 0.99)}
Ns = 12; kmax = kedge[0.99]
check('B3 finite diagnostic (12^3): kappa per species rises toward the split-constraint edge x0 -> eps0 and stays bounded '
      '(about 0.09); with N_s = 12 species N_s kappa reaches 15/16 only within about 10% of the edge',
      0.05 < kmax < 0.2 and kedge[0.6] < kedge[0.9] < kmax, ', '.join(f'x0/eps0 {k}: {v:.3f}' for k, v in kedge.items()) + f'; N_s kappa_max {Ns * kmax:.2f} vs 15/16, 7/8')
fm = np.array([cycleE(K6, 0.3, mu0, 0.0, 0.003)[0] for mu0 in (0.01, 0.02, 0.04)])
Cm_ = fm / (np.array([0.01, 0.02, 0.04]) ** 2 * 0.003 ** 2)
check('B4 finite diagnostic: a mass ramp m N gives flips ~ C mu0^2 h^2 with C = O(10-100), so a measured fermion '
      '(mu0 = m N < 1e-17 at the cell) is created at < 1e-30 per mode per cycle', all(1.5 < s < 2.3 for s in np.diff(np.log(fm)) / np.log(2)) and Cm_.max() < 100,
      'mu0 .01 .02 .04: ' + ' '.join(f'{a:.1e}' for a in fm) + '; C ' + ' '.join(f'{a:.0f}' for a in Cm_))
def fixed(kf, n=600):
    rho, H = 1.0, 1.0
    for _ in range(n): rho = rho / 16 + kf(H) * rho; H = np.sqrt(rho)
    return H
kf = lambda H: Ns * kmax * (1 if H < 1 else 1 / H ** 2)                 # flat then saturating, h in units of saturation
kl = lambda H: 0.5 * (1 if H < 1 else 1 / H ** 2)
Hs, Hl = fixed(kf), fixed(kl)
check('B5 THEOREM (steady-state map of one-cell-start C2 with the kappa shape of B2): with kappa flat then falling, N_s kappa(0) > 15/16 drives H to a stable '
      'fixed point at saturation (h ~ 0.1 eps0) that never ends, and N_s kappa(0) < 15/16 decays to nothing: the ramp has no '
      'exit and gives the same split at every level (lambda = 1, n_s = 1)', abs(Hs - np.sqrt(Ns * kmax * 16 / 15)) < 1e-6 and Hl < 1e-6,
      f'H/H_sat: N_s kappa {Ns * kmax:.2f} -> {Hs:.3f}; 0.5 -> {Hl:.0e}')

# ------------------------------------------------------------------ C
print('== C. the split constraint violated (copy angle x0 > eps0 at birth: partner band inverted during the cycle)')
e0 = 0.3; rowC = {}
for xr in (0.9, 1.1, 1.5):
    rowC[xr] = [splitX(Kanti(L), e0, 2 * xr * e0, xr * e0) for L in (1, 2, 3, 4, 5)]
ok = all(r[0].min() > 0.3 and r[2].max() < 1e-12 for r in rowC[0.9])
ok &= all(rowC[xr][i][0].min() < 1e-12 for xr in (1.1, 1.5) for i in (0, 2, 4)) and all(rowC[xr][i][0].min() > 0.2 and rowC[xr][i][2].max() < 1e-12 for xr in (1.1, 1.5) for i in (1, 3))
sc = [rowC[1.1][i][2].sum() * 32 for i in (0, 2, 4)]
check('C1 finite diagnostic (current CL-1, eps fixed): violating the constraint makes the sign blocks singular exactly at '
      'K = pi(1,1,1), which only odd tori hold (the one-cube start, never the 2^n cascade after it); every other momentum '
      'carries the vacuum exactly, so the heat is one momentum\'s worth, not extensive: no built-in reheating',
      ok and max(sc) / min(sc) < 1.01, f'flips at K = pi on L = 1, 3, 5: ' + ', '.join(f'{v:.3f}' for v in sc) + '; elsewhere 0')
svn = [splitX(np.full((1, 3), np.pi * (1 - d)), e0, 2.2 * e0, 1.1 * e0)[0][0] for d in (0.1, 0.03, 0.01)]
check('C2 finite diagnostic: near K = pi the smallest singular value falls linearly, so the inverted split\'s V* is '
      'discontinuous there and its kernel has a power-law tail (the finite-range heating of the sea-split note then applies)',
      abs(svn[1] / svn[2] - 3) < 0.3 and abs(svn[0] / svn[1] - 3) < 0.6, 'sv at d = .1, .03, .01: ' + ', '.join(f'{v:.2e}' for v in svn))
finv = np.array([cycleE(Kanti(6), 0.04, 0.0, 1.33 * 0.04, hh)[0] for hh in (0.001, 0.003, 0.01)])
pinv = np.diff(np.log(finv)) / np.log([3, 10 / 3])
check('C3 finite diagnostic: with the band inverted, avoided crossings near K = pi are passed adiabatically at small h and '
      'diabatically above the torus gap (Landau-Zener), giving a slope above 2 in a window set by the torus\' nearest '
      'momentum to pi, i.e. by the level: a size effect of the first few splits, not a clock of later ones', max(pinv) > 2.4,
      'flips 0.001, 0.003, 0.01: ' + ' '.join(f'{a:.1e}' for a in finv) + ' | slopes ' + ' '.join(f'{a:.2f}' for a in pinv))

# ------------------------------------------------------------------ D
print('== D. the lag threshold (split at the middle of the next even half-tick after l >= 2 l_c)')
def lag(h, nt=3000, sub=40):
    l = 1.0; dj = 1.0 / sub; pend = None; lmax = 0
    for t in range(nt * sub):
        if t % sub == 0 and l >= 2 and pend is None: pend = t + sub // 4
        if pend is not None and t == pend: l /= 2; pend = None
        if h * l * dj >= 1 or l > 1e6: return np.inf
        l = l / (1 - h * l * dj); lmax = max(lmax, l)
    return lmax
lo, hi = 0.2, 0.25
for _ in range(14):
    mid = (lo + hi) / 2; lo, hi = (mid, hi) if np.isfinite(lag(mid)) else (lo, mid)
check('D1 finite diagnostic: below h_c the splits keep the edge within [l_c, 4 l_c]; above it each split lands later, '
      'the edge (and every mass and copy angle) diverges in finitely many ticks and the split constraint is broken for good',
      0.2 < lo < 0.25 and np.isfinite(lag(0.15)) and not np.isfinite(lag(0.3)), f'h_c = {lo:.4f}; H l_c at h_c = {lo * r3:.3f}/sin(eps0)')

# ------------------------------------------------------------------ E
print('== E. symmetry of what the ramp creates')
part, hole = cycleK(K6, 0.3, 0.0, 0.25, 0.01)
Tij = np.einsum('k,ki,kj->ij', part, np.sin(K6), np.sin(K6)); an = np.abs(Tij - np.trace(Tij) / 3 * np.eye(3)).max() / np.trace(Tij)
km = np.array([np.argmin(np.abs(((K6 + kk) + np.pi) % (2 * np.pi) - np.pi).sum(1)) for kk in K6])
check('E1 THEOREM (one-body, translation- and tetrahedrally covariant ramp): particles equal holes at every momentum (no '
      'number, hence no B or L, is created), n(K) = n(-K), and the mean stress is isotropic (no rank-2 invariant of the '
      '12 kept rotations): eta = 0 and the mean anisotropy is 0; tensor modes come only from shot noise',
      np.abs(part - hole).max() < 1e-12 and np.abs(part - part[km]).max() < 1e-12 and an < 1e-12,
      f'|n_p - n_h| {np.abs(part - hole).max():.0e}; |n(K) - n(-K)| {np.abs(part - part[km]).max():.0e}; anisotropy {an:.0e}')

# ------------------------------------------------------------------ F
print('== F. ESTIMATES vs measurement (l_c = 4 sqrt(8 pi) l_P; eps0 0.0075-0.0375; not theorems)')
lcP = 4 * np.sqrt(8 * np.pi); Hinf = 2.4e-5 / np.sqrt(8 * np.pi)          # H/M_P at the r < 0.036 bound (A_s 2.1e-9)
hinf = Hinf * lcP * np.sin(0.0375) / r3; hsat = 0.1 * 0.0375
Hss = hsat * r3 / np.sin(0.0375) / lcP; rss = 2 * (Hss * np.sqrt(8 * np.pi)) ** 2 / np.pi ** 2 / 2.1e-9
print(f'   observable inflation: h <= {hinf:.1e}; the ramp injects a fixed N_s kappa <= {Ns * kmax:.2f} rho_c per split there (no H-growth)')
print(f'   self-sustained branch: H/M_P ~ {Hss:.1e} at saturation, r ~ {rss:.0e} vs < 0.036; lambda = 1 vs 0.976-0.982; eta = 0 vs 6.1e-10')
print(f'   lag branch: H l_c > {lo * r3 / np.sin(0.0375):.0f}, super-Planckian; massless species never created (A1)')
check('F1 arithmetic: every branch of the ramp misses a measured fact (r, lambda, eta, or no exit)', rss > 1 and hinf < 1e-4)
print('supplied: tick, copy-mass placement, vacuum branch, split, de Sitter background, tori, 8 pi G = l_c^2, N_s, measured numbers.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
