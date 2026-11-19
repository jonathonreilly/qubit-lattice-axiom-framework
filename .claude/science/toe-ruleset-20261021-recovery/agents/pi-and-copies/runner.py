#!/usr/bin/env python3
"""The pi-cone and the two copies of the supplied spin-3/2 Margolus Dirac tick (one fermion mode per site; block
unitary on even 2^3 blocks, then on odd blocks shifted by (1,1,1); rotations act on site modes as spin-3/2 coherent
states along the body diagonals).  Convention: half-tick block unitary V(a) = cos a W + i sin a = W e^{iaW}
(a = mu/2 of the covariant-tick runner).  Sections:
 1  the auditor's K = pi(1,1,1) formula;
 2  the covariant block algebra: commutant = span{1, W (edge), F (face diagonal), B (body diagonal)} = 1_4 x M_2;
 3  the partition exchangers of the lattice (translation by (1,1,1), inversion through a site; site-local gauges;
    unitary or antiunitary) and the automorphisms they induce;
 4  theorem A (any single covariant tick): partition-neutral + nonzero pure Dirac mass at K = 0 => U(R) scalar;
 5  theorem B (W-mass family, any schedule): K=0 mass = sum m_t, R offset = sum (-1)^t m_t;
 6  the Wilson-type staggered tick (b, -b): partition-neutral, gaps R by 2b; adding the mass mu breaks neutrality;
 7  the two copies: K = 0 Bloch space = 2 G3/2, every covariant tick has fourfold rest levels;
    Dirac masses = 2A1 + 2A2 + 2E, the invariant ones give both copies the same mass.
Supplied model, finite diagnostic; no physical identification; no classification of multi-step schedules
beyond the W-mass family.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools, os, signal, sys
from math import comb
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

rng = np.random.default_rng(20261021)
CORN = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * CORN - 1).astype(float); INV = np.eye(8)[7 - np.arange(8)]
def Jm(j):
    m = j - np.arange(int(round(2 * j)) + 1); Jp = np.diag(np.sqrt(j * (j + 1) - m[1:] * (m[1:] + 1)), 1).astype(complex)
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def coherent(j, n):
    n = n / np.linalg.norm(n); th, ph, d = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0]), int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * np.sin(th / 2) ** k * np.exp(1j * (k - j) * ph) for k in range(d + 1)])
XI = [coherent(1.5, v) for v in NV]
ROTS = [R for R in (np.array(p) * np.array(s)[:, None] for p in itertools.permutations(np.eye(3)) for s in itertools.product((1, -1), repeat=3)) if np.isclose(np.linalg.det(R), 1)]
def spin_rot(R):
    w, V = np.linalg.eig(R); a = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)); ax = np.real(V[:, np.argmin(abs(w - 1))]); ax /= np.linalg.norm(ax)
    if 1e-9 < a < np.pi - 1e-9 and np.dot(ax, [R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) < 0: ax = -ax
    return expm(-1j * a * sum(ax[k] * Jm(1.5)[k] for k in range(3)))
def cidx(v): return int(np.argmin(abs(NV - v).sum(1)))
def corner_action(R):
    S = spin_rot(R); L = np.zeros((8, 8), complex)
    for i in range(8): k = cidx(R @ NV[i]); L[k, i] = XI[k].conj() @ S @ XI[i]
    return L
LS = [corner_action(R) for R in ROTS]
W = np.zeros((8, 8), complex)
for s, t in itertools.product(range(8), repeat=2):
    if abs(CORN[s] - CORN[t]).sum() == 1: g = XI[s].conj() @ XI[t]; W[s, t] = -g / abs(g) / np.sqrt(3)
GAM = np.diag((-1.0) ** CORN.sum(1)).astype(complex); I8 = np.eye(8, dtype=complex)
def Dk(K): return np.exp(1j * (CORN @ np.asarray(K, float)))
def bloch(K, seq):
    """half-steps on alternating partitions, even first: U(K) = ... (D V_odd D^dag) V_even."""
    D = Dk(K); U = I8.copy()
    for t, V in enumerate(seq): U = (V if t % 2 == 0 else D[:, None] * V * D.conj()[None, :]) @ U
    return U
def bloch_many(Ks, ve, vo):
    D = np.exp(1j * (np.atleast_2d(Ks) @ CORN.T)); return (D[:, :, None] * vo[None] * D.conj()[:, None, :]) @ ve[None]
def wrap(x): return (x + np.pi) % (2 * np.pi) - np.pi
def Va(a): return np.cos(a) * W + 1j * np.sin(a) * I8
KR, K0 = np.full(3, np.pi), np.zeros(3)
dirs = rng.normal(size=(60, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]

print('== 1. the auditor formula at K = R = pi(1,1,1)')
e1 = e0 = 0
for a, b in rng.uniform(-3, 3, (40, 2)):
    e1 = max(e1, abs(bloch(KR, [Va(a), Va(b)]) - (-np.cos(a - b) * I8 + 1j * np.sin(b - a) * W)).max())
    e0 = max(e0, abs(bloch(K0, [Va(a), Va(b)]) - (np.cos(a + b) * I8 + 1j * np.sin(a + b) * W)).max())
check('U(R) = -cos(a-b) + i sin(b-a) W exactly (even mass a, odd mass b): R sits at pi +- (a-b)', e1 < 1e-13, f'{e1:.1e}')
check('U(0) = cos(a+b) + i sin(a+b) W: K=0 mass a+b (both identities: D(R) = Gamma, Gamma W Gamma = -W)', e0 < 1e-13, f'{e0:.1e}')

print('== 2. covariant block algebra')
A = np.vstack([np.kron(L, I8) - np.kron(I8, L.T) for L in LS]); _, sv, Vh = np.linalg.svd(A); ncomm = int(np.sum(sv < 1e-9))
Bc = [b.reshape(8, 8) for b in Vh[-ncomm:].conj()]
cand = [(h - W @ h @ W) / 2 for b in Bc for h in (b + b.conj().T, 1j * (b - b.conj().T))]
cand = [(c + GAM @ c @ GAM) / 2 for c in cand]; F = max(cand, key=lambda c: abs(c).max()); F /= np.sqrt(np.trace(F @ F).real / 8)
B = 1j * F @ W
def shell(X): return sorted({int(abs(CORN[s] - CORN[t]).sum()) for s, t in itertools.product(range(8), repeat=2) if abs(X[s, t]) > 1e-12})
inc = max(abs(L @ X - X @ L).max() for L in LS for X in (W, F, B))
pauli = all(np.allclose(X @ X, I8) and np.allclose(X, X.conj().T) for X in (W, F, B)) and np.allclose(F @ B, 1j * W) and np.allclose(B @ W, 1j * F)
check('commutant of the 24 spin-3/2 corner actions has dim 4 = span{1, W, F, B}, a Pauli algebra (F,B,W) = (tau1,tau2,tau3)',
      ncomm == 4 and inc < 1e-12 and pauli, f'hop shells W {shell(W)}, F {shell(F)}, B {shell(B)}')
check('corner parity Gamma = D(R) acts on it as Ad F: W -> -W, B -> -B, F -> F',
      np.allclose(GAM @ W @ GAM, -W) and np.allclose(GAM @ B @ GAM, -B) and np.allclose(GAM @ F @ GAM, F))
eps = 1e-6; al = []
for a in range(3):
    e = np.zeros(3); e[a] = eps; x = (bloch(e, [W, W]) - bloch(-e, [W, W])) / (2j * eps); al.append((x + x.conj().T) / 2)
cl = max(abs(al[a] @ al[b] + al[b] @ al[a] - (2 / 3) * (a == b) * I8).max() for a in range(3) for b in range(3))
anti = {nm: max(abs(X @ a + a @ X).max() for a in al) < 1e-8 for nm, X in (('W', W), ('F', F), ('B', B))}
comm = max(abs(F @ a - a @ F).max() for a in al) < 1e-8
check('massless node: alpha_a Clifford (speed 1/sqrt3); W and B anticommute with all alpha_a (Dirac masses), F commutes (not a mass)',
      cl < 1e-9 and anti['W'] and anti['B'] and not anti['F'] and comm, f'Clifford err {cl:.0e}')

print('== 3. partition exchangers (6^3 lattice)')
N = 6; sites = np.array(list(itertools.product(range(N), repeat=3))); idx = {tuple(s): i for i, s in enumerate(sites)}; par = (sites % 2) @ [4, 2, 1]
def half(V, odd):
    M = np.zeros((N**3, N**3), complex); off = np.ones(3, int) if odd else np.zeros(3, int)
    for b in itertools.product(range(0, N, 2), repeat=3):
        ids = [idx[tuple((np.array(b) + off + s) % N)] for s in CORN]; M[np.ix_(ids, ids)] = V[np.ix_(par[ids], par[ids])]
    return M
def glob(R, cen):
    G = np.zeros((N**3, N**3), complex); S = spin_rot(R)
    for i, x in enumerate(sites):
        y = np.rint(R @ (x - cen) + cen).astype(int) % N; G[idx[tuple(y)], i] = XI[par[idx[tuple(y)]]].conj() @ S @ XI[par[i]]
    return G
def gauge(M, X):
    g = np.zeros(8, complex); g[0] = 1; todo = [0]
    while todo:
        s = todo.pop()
        for t in range(8):
            if abs(X[s, t]) > 1e-12 and g[t] == 0: g[t] = np.conj(X[s, t] / (g[s] * M[s, t])); todo.append(t)
    return g
Tr = np.zeros((N**3, N**3)); Is = np.zeros((N**3, N**3))
for i, x in enumerate(sites): Tr[idx[tuple((x + 1) % N)], i] = 1; Is[idx[tuple((-x) % N)], i] = 1
gT = gauge(INV @ W @ INV, W); gTa = gauge(INV @ W.conj() @ INV, W); gIa = gauge(W.conj(), W)
GL = lambda g: np.diag(g[par]); GamL = GL(np.diag(GAM))
EX = {}   # name -> (lattice operator, antiunitary?)
for base, gb, an in (('T', gT, False), ('T*', gTa, True), ('I', np.ones(8), False), ('I*', gIa, True)):
    Op = (Tr if base.startswith('T') else Is) @ GL(gb)
    EX[base] = (Op, an); EX[base + 'G'] = (GamL @ Op, an)
X = expm(1j * sum(rng.normal() * (b + b.conj().T) for b in Bc))
def induced(op, an, X): return op @ (half(X, False).conj() if an else half(X, False)) @ op.conj().T
ok = True; amap = {}
for nm, (op, an) in EX.items():
    img = induced(op, an, X)
    # read the odd-block matrix of the image (parity labels)
    Y = np.zeros((8, 8), complex); ids = [idx[tuple((np.ones(3, int) + s) % N)] for s in CORN]; Y[np.ix_(par[ids], par[ids])] = img[np.ix_(ids, ids)]
    ok &= abs(img - half(Y, True)).max() < 1e-12 and max(abs(L @ Y - Y @ L).max() for L in LS) < 1e-10
    sgn = []
    for Z in (W, F, B):
        Zi = induced(op, an, Z); Zy = np.zeros((8, 8), complex); Zy[np.ix_(par[ids], par[ids])] = Zi[np.ix_(ids, ids)]
        sgn.append(int(np.sign(np.trace(Zy @ Z).real)))
    amap[nm] = (tuple(sgn), an)
check('each of the 8 exchangers maps even-block covariant unitaries onto odd-block covariant unitaries', ok)
Ge, Go = [glob(R, np.full(3, .5)) for R in ROTS], [glob(R, np.full(3, 5.5)) for R in ROTS]
G15 = [glob(R, np.full(3, 1.5)) for R in ROTS]; OpT = Tr @ GL(gT)
okr = all(min(abs(Is @ g @ Is.T - h).max() for h in Go) < 1e-12 for g in Ge) and all(min(min(abs(OpT @ g @ OpT.conj().T - sg * h).max() for sg in (1, -1)) for h in G15) < 1e-12 for g in Ge)
check('site inversion maps the 24 even-centre rotations onto the odd-centre ones; gauged (1,1,1) translation does so up to the sign (-1)^(2j)', okr)
print('   induced signs on (W,F,B), antiunitary flag:', {k: v for k, v in amap.items()})
klein = {(1, 1, 1): 'id', (-1, 1, -1): 'AdF', (-1, -1, 1): 'AdB', (1, -1, -1): 'AdW'}
def eff(sgn, an):   # action on the SU(2) part q = c + i s m.tau; antiunitary flips i, i.e. all m signs
    s = tuple(-x for x in sgn) if an else sgn; return klein.get(s)
effs = {k: eff(*v) for k, v in amap.items()}
check('on q = cos th + i sin th m.tau every exchanger acts as Ad of 1, F, B or W (antiunitary ones too)', all(effs.values()) and set(effs.values()) == {'id', 'AdF', 'AdB', 'AdW'}, str(effs))

print('== 4. theorem A: single ticks (v, phase x alpha(v))')
def alpha(nm, X):
    op, an = EX[nm]; ids = [idx[tuple((np.ones(3, int) + s) % N)] for s in CORN]; img = induced(op, an, X)
    Y = np.zeros((8, 8), complex); Y[np.ix_(par[ids], par[ids])] = img[np.ix_(ids, ids)]; return Y
def rand_v():
    x = rng.normal(size=4); x /= np.linalg.norm(x); return np.exp(1j * rng.uniform(0, 2 * np.pi)) * (x[0] * I8 + 1j * (x[1] * F + x[2] * B + x[3] * W))
def comp(U):
    t = np.trace(U) / 8; return t, np.array([np.trace(Z @ U) / 8 for Z in (F, B, W)])
cos_ok = True; scal_ok = True; nfree = 0; nonvac = 0
for nm in EX:
    k = {'id': None, 'AdF': 0, 'AdB': 1, 'AdW': 2}[effs[nm]]; kR = {'id': 0, 'AdF': None, 'AdB': 2, 'AdW': 1}[effs[nm]]
    for _ in range(25):
        v = rand_v(); vo = alpha(nm, v); U0, UR = bloch(K0, [v, vo]), bloch(KR, [v, vo])
        x = v / np.sqrt(np.linalg.det(v[:2, :2]) if False else 1); t0, m0 = comp(U0); tR, mR = comp(UR)
        if np.linalg.norm(mR) > 1e-3: nonvac += 1
    # F-free massive samples by root finding along random great circles of SU(2)
    for _ in range(12):
        x0, x1 = rng.normal(size=4), rng.normal(size=4); x1 -= x0 * (x0 @ x1) / (x0 @ x0); x0 /= np.linalg.norm(x0); x1 /= np.linalg.norm(x1)
        mk = lambda t: (lambda y: y[0] * I8 + 1j * (y[1] * F + y[2] * B + y[3] * W))(np.cos(t) * x0 + np.sin(t) * x1)
        def f(t):
            U0 = bloch(K0, [mk(t), alpha(nm, mk(t))]); t0, m0 = comp(U0); return (m0[0] / t0).imag if abs(t0) > 1e-6 else (m0[0] / m0[1:].sum()).real
        ts = np.linspace(0, np.pi, 41); fv = [f(t) for t in ts]
        for i in range(40):
            if fv[i] * fv[i + 1] < 0 and abs(fv[i] - fv[i + 1]) < 5:
                r = brentq(f, ts[i], ts[i + 1], xtol=1e-14); v = mk(r); U0, UR = bloch(K0, [v, alpha(nm, v)]), bloch(KR, [v, alpha(nm, v)])
                t0, m0 = comp(U0); mass = np.linalg.norm(m0[1:])
                if abs(m0[0]) < 1e-9 and mass > 1e-3:
                    nfree += 1; ev = np.linalg.eigvals(U0); lam = UR[0, 0]
                    scal_ok &= abs(UR - lam * I8).max() < 1e-9 and min(abs(lam**2 - ev[i_] * ev[j_]) for i_ in range(8) for j_ in range(8) if abs(ev[i_] - ev[j_]) > 1e-6) < 1e-9
                break
check('generic single ticks: U(R) is not scalar (the statement below is not vacuous)', nonvac > 150, f'{nonvac}/200 non-scalar')
check('every partition-neutral single tick whose K=0 term is a nonzero pure Dirac mass (no F part) has U(R) = lambda*1, lambda^2 = product of the two K=0 levels: R sits exactly at the light centre or at its pi-point',
      scal_ok and nfree >= 40, f'{nfree} root-found samples over the 8 exchangers')
# bound for the AdW (translation) class: pi-gap <= mu in the branch containing the base tick
worst = -np.inf; rat = 0; cnt = 0
def Pphase(v): c = [np.trace(Z @ v) / 8 for Z in (I8, F, B, W)]; return c[0]**2 - c[1]**2 - c[2]**2 - c[3]**2
for _ in range(3000):
    hh = rng.normal(size=4) * rng.uniform(0, 0.4); v = np.exp(1j * rng.uniform(0, 6.3)) * 1j * W @ expm(1j * (hh[0] * I8 + hh[1] * F + hh[2] * B + hh[3] * W)); vo = W @ v @ W; P_ = Pphase(v)**2      # U(0) = P Ad_W(q) q with P = e^{2 i phi}; base branch: light pair near -P
    l0 = np.angle(np.linalg.eigvals(bloch(K0, [v, vo])) / (-P_)); mu = np.abs(l0).max()
    if mu > 0.3: continue
    gap = np.abs(np.angle(np.linalg.eigvals(bloch(KR, [v, vo])) / P_)).min(); cnt += 1; worst = max(worst, gap - mu); rat = max(rat, gap / max(mu, 1e-15))
check('translation class (v, W v W), base branch: pi-gap <= K=0 half-splitting mu for every sample (exact: cos aR >= cos mu)', cnt > 500 and worst < 1e-9, f'{cnt} light samples, max(gap - mu) {worst:.1e}, max gap/mu {rat:.6f}')
for h in (0.02, 0.01):
    v = 1j * (np.cos(h) * W + np.sin(h) * F); cc = bloch(K0, [v, v])[0, 0]
    gap = np.min(np.pi - abs(np.angle(np.linalg.eigvals(bloch(KR, [v, v])) / cc)))
    lam = np.abs(np.array([np.angle(np.linalg.eigvals(bloch(1e-5 * n, [v, v])) / cc) / 1e-5 for n in dirs])); an = (lam.max() - lam.min()) / lam.mean()
    if h == 0.02: a2 = an / h
check('F-rotated involution (v,v), v = cos h W + sin h F (site-inversion neutral): pi-gap 2h but first-order cone anisotropy ~ 1.42 h',
      abs(gap - 2 * h) < 1e-9 and abs(an / h - a2) / a2 < 0.02, f'gap {gap:.4f}, anisotropy/h {an / h:.3f}')

print('== 5. theorem B: W-mass schedules')
eB = 0
for _ in range(30):
    n = 2 * rng.integers(1, 5); m = rng.uniform(-2, 2, n); seq = [Va(x) for x in m]; s0, sR = m.sum(), (m * (-1.0) ** np.arange(n)).sum()
    eB = max(eB, abs(bloch(K0, seq) - expm(1j * s0 * W)).max(), abs(bloch(KR, seq) - (-1) ** (n // 2) * expm(1j * sR * W)).max())
check('any schedule of V(m_t): U(0) = exp(i W sum m_t), U(R) = (-1)^(n/2) exp(i W sum (-1)^t m_t)', eB < 1e-12, f'{eB:.1e}')
m = 0.3; seq1 = [Va(m), Va(m), Va(-m), Va(-m)]; seq2 = [Va(m), Va(-m), Va(-m), Va(m)]
check('mass sign alternating every tick (m,m,-m,-m) or (m,-m,-m,m): two-tick U(0) = U(R) = 1, i.e. massless AND ungapped',
      all(abs(bloch(K, s) - I8).max() < 1e-12 for K in (K0, KR) for s in (seq1, seq2)))

print('== 6. Wilson-type staggered tick: half-tick masses (mu/2 + b, mu/2 - b)')
def sym_under(ve, vo):
    out = []
    for nm in EX:
        a_, b_ = alpha(nm, vo), alpha(nm, ve)       # swapped tick: even gets alpha(v_odd), odd gets alpha(v_even)
        out.append(nm) if any(min(abs(a_ - p * ve).max(), 9) < 1e-9 and abs(b_ - p * vo).max() < 1e-9 for p in (1, -1, 1j, -1j)) else None
    return out
b = 0.6
s_w = sym_under(Va(b), Va(-b)); s_m = sym_under(Va(0.05), Va(0.05)); s_both = sym_under(Va(0.025 + b), Va(0.025 - b))
check('(b,-b) is invariant under exchangers (gauged translation x Gamma, site inversion x Gamma, ...); (a,a) under others; (mu/2+b, mu/2-b) under none',
      len(s_w) >= 2 and len(s_m) >= 2 and len(s_both) == 0, f'(b,-b): {s_w}; (a,a): {s_m}; both: {s_both}')
Ue, Uo = Va(0.025 + b), Va(0.025 - b); Ue2, Uo2 = Va(-0.025 + b), Va(-0.025 - b)
sw = alpha('I', Uo), alpha('I', Ue)
check('the site-inversion image of (mu/2+b, mu/2-b) is (mu/2-b, mu/2+b), Gamma-equivalent to mu -> -mu, with identical spectrum',
      np.allclose(sw[0], Uo) and np.allclose(GAM @ Uo @ GAM, -Ue2) and np.allclose(GAM @ Ue @ GAM, -Uo2) and
      np.allclose(np.sort(np.angle(np.linalg.eigvals(bloch(KR * 0.37, [Ue, Uo])))), np.sort(np.angle(np.linalg.eigvals(bloch(KR * 0.37, [Ue2, Uo2]))))))
KZ = rng.uniform(-np.pi, np.pi, (3000, 3)); errf = 0; ok4 = True
for mu, bb in ((0.05, 0.6), (0.0, 0.4), (0.1, 1.0)):
    U = bloch_many(KZ, Va(mu / 2 + bb), Va(mu / 2 - bb)); w = np.sort(np.abs(np.angle(np.linalg.eigvals(U))), 1)
    S = np.cos(KZ).sum(1) / 3; cw = (np.cos(2 * bb) + np.cos(mu)) / 2 * S - (np.cos(2 * bb) - np.cos(mu)) / 2
    errf = max(errf, np.abs(np.cos(w) - cw[:, None]).max()); ok4 &= np.ptp(w, 1).max() < 1e-8
check('bands: cos w = (cos2b + cos mu)/2 S - (cos2b - cos mu)/2, S = mean cos K_a; all eight |w| equal (copies fourfold)', errf < 1e-12 and ok4, f'{errf:.1e}')
mu, bb = 0.05, 0.6; U = bloch_many(KZ, Va(mu / 2 + bb), Va(mu / 2 - bb)); w = np.abs(np.angle(np.linalg.eigvals(U)))
wR = np.abs(np.angle(np.linalg.eigvals(bloch(KR, [Va(mu / 2 + bb), Va(mu / 2 - bb)]))))
check('quasi-energy band is [mu, pi - 2b]: light gap mu at K=0 only, pi-gap 2b at R only (mu=0.05, b=0.6)',
      w.min() >= mu - 1e-12 and w.max() <= np.pi - 2 * bb + 1e-12 and np.allclose(wR, np.pi - 2 * bb), f'sampled range {w.min():.4f}..{w.max():.4f}; pi-2b = {np.pi - 2 * bb:.4f}')
c2 = (np.cos(2 * bb) + np.cos(mu)) / 6
for kk in (0.1, 0.3):
    o = np.abs(np.angle(np.linalg.eigvals(bloch_many(kk * dirs, Va(mu / 2 + bb), Va(mu / 2 - bb))))); ref = np.sqrt(mu**2 + c2 * kk**2)
    dev = abs(o.mean() / ref - 1); spr = np.ptp(o.mean(1)) / o.mean()
    check(f'|k|={kk}: light band = sqrt(mu^2 + c^2 k^2), c^2 = (cos2b + cos mu)/6, within 0.6%; direction spread < 0.6%', dev < 6e-3 and spr < 6e-3, f'dev {dev:.1e}, spread {spr:.1e}')
Uf = half(Va(mu / 2 - bb), True) @ half(Va(mu / 2 + bb), False)
err = max(abs(g @ Uf - Uf @ g).max() for g in Ge + Go)
check('lattice tick (6^3) commutes with all 24 rotations about even and odd block centres', err < 1e-12, f'{err:.1e}')
bt = (np.pi - 0.5) / 2; o = np.abs(np.angle(np.linalg.eigvals(bloch_many(KZ, Va(mu / 2 + bt), Va(mu / 2 - bt)))))
check('b = (pi - 1/2)/2 puts every mode within the CL-6 domain |w| <= 1/2 rad per tick (speed c = %.3f)' % np.sqrt((np.cos(2 * bt) + np.cos(mu)) / 6), o.max() <= 0.5 + 1e-12, f'max |w| {o.max():.4f}')

print('== 7. the two copies')
chi = {}
for R, L in zip(ROTS, LS):
    a_ = round(np.degrees(np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)))); chi.setdefault(a_, set()).add(round(np.trace(L).real, 6))
n2 = np.mean([abs(np.trace(L))**2 for L in LS])
check('K=0 Bloch space under the 24 rotations = 2 x G3/2: character 8, -+2 (120 deg), 0 (90, 180 deg); mean |chi|^2 = 4 = 2^2; commutant 1_4 x M_2',
      ncomm == 4 and chi[0] == {8.0} and chi[120] <= {-2.0, 2.0} and chi[90] == {0.0} and chi[180] == {0.0} and abs(n2 - 4) < 1e-9, str({k: sorted(v) for k, v in chi.items()}))
worst = 0
for _ in range(30):
    seq = [expm(1j * sum(rng.normal() * (z + z.conj().T) + rng.normal() * 1j * (z - z.conj().T) for z in Bc)) for _ in range(2 * rng.integers(1, 5))]
    for K in (K0, KR):
        z = np.exp(1j * np.angle(np.linalg.eigvals(bloch(K, seq)))); cnt = [int(np.sum(abs(z - y) < 1e-8)) for y in z]; worst = max(worst, max(c % 4 for c in cnt))
check('every covariant multi-step tick (30 random, 2-8 half-steps): K=0 and R levels have multiplicity 4k, so the two copies have equal rest mass', worst == 0)
basis = []
for i in range(8):
    for j in range(i, 8):
        E = np.zeros((8, 8), complex); E[i, j] = E[j, i] = 1; basis.append(E)
        if i != j: E = np.zeros((8, 8), complex); E[i, j], E[j, i] = 1j, -1j; basis.append(E)
Am = np.array([np.concatenate([(a @ M + M @ a).ravel() for a in al]) for M in basis]).T; Am = np.vstack([Am.real, Am.imag])
_, sv, Vh = np.linalg.svd(Am); Ms = [sum(c * bm for c, bm in zip(v, basis)) for v in Vh[np.sum(sv > 1e-8):]]
Mv = np.array([x.ravel() for x in Ms]).T; P = np.linalg.pinv(Mv)
chM = {}
for R, L in zip(ROTS, LS):
    a_ = round(np.degrees(np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)))); typ = a_ if a_ != 180 else (180 if np.sum(np.isclose(abs(np.diag(R)), 1)) == 3 else 181)
    chM.setdefault(typ, set()).add(round(np.trace(P @ np.array([(L @ x @ L.conj().T).ravel() for x in Ms]).T).real, 6))
ch = [chM[t].pop() for t in (0, 120, 180, 90, 181)]; sz = (1, 8, 3, 6, 6)
irr = {'A1': (1, 1, 1, 1, 1), 'A2': (1, 1, 1, -1, -1), 'E': (2, -1, 2, 0, 0), 'T1': (3, 0, -1, 1, -1), 'T2': (3, 0, -1, -1, 1)}
dec = {k: round(sum(s * c * x for s, c, x in zip(sz, ch, v)) / 24, 6) for k, v in irr.items()}
check('Dirac masses ({M, alpha_a} = 0) form an 8-dim space = 2 A1 + 2 A2 + 2 E; the invariant pair is span{W, B}',
      len(Ms) == 8 and dec == {'A1': 2, 'A2': 2, 'E': 2, 'T1': 0, 'T2': 0}, str(dec))
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
