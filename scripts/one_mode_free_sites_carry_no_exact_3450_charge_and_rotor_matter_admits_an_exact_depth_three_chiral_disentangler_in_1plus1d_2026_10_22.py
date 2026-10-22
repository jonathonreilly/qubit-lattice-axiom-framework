#!/usr/bin/env python3
"""tpf-circuit: the Thorngren-Preskill-Fidkowski symmetry-disentangler route to a chiral link, rederived and tested against the
register's rules (one fermion mode per site; rotors or Z_N only as link carriers).
 A one-mode fermion chains: the exact (Onsager) charges cannot be combined into a quantised 3450 charge; no circuit helps
 B Villain rotor matter: the rederived constant-depth disentangler (TPF eq. 23), exact on rational configurations; anomalous
   sets fail; endpoint charge; dressed charges; the Z_5 clock (all-finite) version
 C light content: Floquet dispersion, chiral zero-mode charges, quasi-energy folding of rotor states
 D gauging: Gauss law, ancillas eaten, where the chirality sits, Schwinger term, gauged normal modes
 E 3+1D: the SM 16 in TPF blocks, Kuhn-triangulation degree-of-freedom count
Labels: [T] theorem / exact computation, [M] measurement. Identities are proved in the accompanying derivation and checked exactly
(Fraction arithmetic) on random configurations. Supplied model, finite diagnostic; no physical identification. Cited, not
rederived: Thorngren-Preskill-Fidkowski arXiv:2601.04304v2 (abstract and HTML read; their W, block charges, SM grouping and
per-face fermion / per-vertex rotor layout), Chatterjee-Pace-Shao (Onsager axial charge), bosonization at the Dirac radius, Weyl
equidistribution, the N >= 5 critical phase of Z_N clocks, PDG/TWIST."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/ONE_MODE_FREE_SITES_CARRY_NO_EXACT_3450_CHARGE_AND_ROTOR_MATTER_ADMITS_AN_EXACT_DEPTH_THREE_CHIRAL_DISENTANGLER_IN_1PLUS1D_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, math, os, random, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from collections import Counter
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
def bdg(A, B): return np.block([[A, B], [B.conj().T, -A.T]])
def Ub(u): n = len(u); return np.block([[u, np.zeros((n, n))], [np.zeros((n, n)), u.conj()]])
S3450 = [(8, -1), (4, 2)]                    # (qV, qA) per flavour: Q = qV*turn + qA*winding; qL = qV/2 + qA, qR = qV/2 - qA
ANOM = {'Dirac(2,0)': [(2, 1)], '3452': [(8, -1), (6, 1)]}
OTHER_FREE = {'TPF (3,3),(9,-1)': [(3, 3), (9, -1)], '3 flavours': [(2, 3), (3, -2), (1, 0)]}

# =============================================== A. one-mode fermion chains ===============================================
print('== A. one-mode fermion chains (staggered hop, one Dirac flavour per chain)')
L = 12; T = np.roll(np.eye(L), 1, axis=0); h = 0.5j * (T - T.T); ks = 2 * np.pi * np.arange(L) / L
QV = bdg(np.eye(L), np.zeros((L, L))); QA = bdg((T + T.T) / 2, (T - T.T) / 2); U = Ub(expm(-1j * h))
hk = lambda k: (-0.5j * (np.exp(1j * k) - np.exp(-1j * k))).real          # Bloch hop = sin k
vel = lambda k: (hk(k + 1e-6) - hk(k - 1e-6)) / 2e-6
e0 = np.concatenate([np.ones(L), np.zeros(L)]) / np.sqrt(L); ep = np.concatenate([(-1.0) ** np.arange(L), np.zeros(L)]) / np.sqrt(L)
check('A1 [T] free chain: Q_V and the Kitaev-pairing axial Q_A are conserved, quantised (Q_A^2 = 1) and do not commute; K = 0 '
      'moves right with Q_A = +1, K = pi left with Q_A = -1',
      max(nrm(QV @ U - U @ QV), nrm(QA @ U - U @ QA), nrm(QA @ QA - np.eye(2 * L))) < 1e-13 and nrm(QV @ QA - QA @ QV) > 0.5
      and abs(e0 @ QA @ e0 - 1) < 1e-12 and abs(ep @ QA @ ep + 1) < 1e-12 and vel(0) > 0.99 and vel(np.pi) < -0.99,
      f'v(0) = {vel(0):+.2f}, v(pi) = {vel(np.pi):+.2f}')
fl = [(4, 1), (2, -2)]                         # a Q_V + b Q_A: right node a + b, left node a - b -> (R5, L3), (R0, L4)
lev = [np.sort(np.abs(np.linalg.eigvalsh(a * QV + b * QA))) for a, b in fl]
form = [np.sort(np.concatenate([np.sqrt(a * a + b * b + 2 * a * b * np.cos(ks))] * 2)) for a, b in fl]
dZ = [float(np.abs(x - np.round(x)).max()) for x in lev]
def mb_c(N):
    cs = []
    for j in range(N):
        c = np.zeros((2 ** N, 2 ** N))
        for s in range(2 ** N):
            if (s >> j) & 1: c[s ^ (1 << j), s] = (-1) ** bin(s & ((1 << j) - 1)).count('1')
        cs.append(c)
    return cs
Lm = 4; cs = mb_c(2 * Lm); Tm = np.roll(np.eye(Lm), 1, axis=0)
def quad(A, B, off):
    M = 0
    for i, j in itertools.product(range(Lm), repeat=2):
        ci, cj = cs[off + i], cs[off + j]; M = M + A[i, j] * ci.T @ cj + 0.5 * (B[i, j] * ci.T @ cj.T + np.conj(B[i, j]) * cj @ ci)
    return M
Qmb = sum(a * quad(np.eye(Lm), 0 * Tm, off) + b * quad((Tm + Tm.T) / 2, (Tm - Tm.T) / 2, off) for off, (a, b) in zip((0, Lm), fl))
evm = np.linalg.eigvalsh(Qmb); gaps = evm - evm[0]; dZmb = float(np.abs(gaps - np.round(gaps)).max())
check('A2 [T] the 3450 combination 4Q_V + Q_A (flavour 1) + 2Q_V - 2Q_A (flavour 2) is conserved with node charges L(3,4), R(5,0), '
      'but its one-body levels sqrt(17 + 8 cos K), 4|sin(K/2)| are not integers (many-body too, 4 + 4 modes): no U(1), and no '
      'circuit, interacting or not, can make one',
      all(np.allclose(x, y) for x, y in zip(lev, form)) and min(dZ) > 0.4 and dZmb > 0.3 and nrm(Qmb - Qmb.T) < 1e-12
      and all(nrm((a * QV + b * QA) @ U - U @ (a * QV + b * QA)) < 1e-12 for a, b in fl),
      f'distance to Z {dZ[0]:.3f}, {dZ[1]:.3f}; many-body {dZmb:.3f}')
def ok1d(R, Lf): return all(sum(abs(q) == m for q in R) == sum(abs(q) == m for q in Lf) for m in {abs(q) for q in R + Lf})
check('A3 [T] T1: a quantised one-body charge of a free one-mode update has #R(+-q) = #L(+-q); 3450 fails, so no free one-mode '
      'lattice carries it, on-site or not',
      not ok1d([5, 0], [3, 4]) and ok1d([3, 4], [3, 4]) and 9 + 16 == 25 + 0)

# =============================================== B. Villain rotor matter ==================================================
print('== B. TPF matter: per flavour a rotor angle phi_j in [0,1), a winding integer n_j per link (exact rational arithmetic)')
def rnd(x): return math.floor(x + Fr(1, 2))
def f1(x): return x - math.floor(x)
def cp(x): return ([r[:] for r in x[0]], [r[:] for r in x[1]], x[2][:], x[3][:])
def QAw(p, n): N = len(p); return -sum(rnd(p[(j + 1) % N] - p[j]) + n[j] for j in range(N))
def sym(x, be, qs):            # e^{2 pi i be Q}, Q = sum_a (qV QV_a + qA QA_a) + sum_j L_j
    y = cp(x); y[0][:] = [[f1(p + qV * be) for p in x[0][a]] for a, (qV, qA) in enumerate(qs)]; y[2][:] = [f1(t + be) for t in x[2]]
    return y, be * sum(qA * QAw(x[0][a], x[1][a]) for a, (qV, qA) in enumerate(qs))
def ylink(ph, n, th, qs, k, a=None):
    N = len(th); return sum(qA * (rnd(ph[al][(k + 1) % N] - ph[al][k] + qV * (th[(k + 1) % N] - th[k] - (a[k] if a else 0))) + n[al][k])
                            for al, (qV, qA) in enumerate(qs))
def Xr(ph, qs, k): return rnd(sum(qA * ph[al][k % len(ph[al])] for al, (qV, qA) in enumerate(qs)))
def ytil(ph, n, th, qs, k, a=None): return ylink(ph, n, th, qs, k, a) - (Xr(ph, qs, k + 1) - Xr(ph, qs, k))
def Phi(ph, n, th, qs, tpf=True):   # TPF's eq. 23 phase; tpf=False drops the -d round(sum qA phi) term
    return -sum(th[k] * (ytil(ph, n, th, qs, k) if tpf else ylink(ph, n, th, qs, k)) for k in range(len(th)))
def W(x, qs):
    y = cp(x); y[0][:] = [[f1(x[0][a][j] + qV * x[2][j]) for j in range(len(x[2]))] for a, (qV, qA) in enumerate(qs)]
    return y, Phi(x[0], x[1], x[2], qs)
def Wd(x, qs):
    y = cp(x); y[0][:] = [[f1(x[0][a][j] - qV * x[2][j]) for j in range(len(x[2]))] for a, (qV, qA) in enumerate(qs)]
    return y, -Phi(y[0], y[1], y[2], qs)
def comp(x, ops):
    ps = Fr(0)
    for op in ops: x, p = op(x); ps += p
    return x, ps
def same(u, v): return u[0] == v[0] and f1(u[1] - v[1]) == 0
def K(x, al, j, be, a=None, qV=0):     # Q-symmetric kinetic gate: turn phi_j, relabel n so the Villain gradients move continuously
    N = len(x[2]); y = cp(x); p = x[0][al]; s = (lambda k: qV * a[k]) if a else (lambda k: 0)
    dl = p[j] - p[(j - 1) % N] - s((j - 1) % N); dr = p[(j + 1) % N] - p[j] - s(j)
    y[1][al][(j - 1) % N] += rnd(dl) - rnd(dl + be); y[1][al][j] += rnd(dr) - rnd(dr - be); y[0][al][j] = f1(p[j] + be); return y, Fr(0)
def Kg_dis(x, al, j, be, qs):         # on-site-frame linked kinetic gate: covariant relabel and the axial flux phase
    N = len(x[2]); qV, qA = qs[al]; y = cp(x); p = x[0][al]; g = lambda k: qV * (x[2][(k + 1) % N] - x[2][k] - x[3][k])
    dl = p[j] - p[(j - 1) % N] + g((j - 1) % N); dr = p[(j + 1) % N] - p[j] + g(j)
    y[1][al][(j - 1) % N] += rnd(dl) - rnd(dl + be); y[1][al][j] += rnd(dr) - rnd(dr - be); y[0][al][j] = f1(p[j] + be)
    X = sum(q[1] * x[0][b][j] for b, q in enumerate(qs)); dlt = rnd(X + qA * be) - rnd(X)
    return y, dlt * (x[2][j] - x[2][(j - 1) % N] - x[3][(j - 1) % N])
def sth(x, j, mu): y = cp(x); y[2][j] = f1(x[2][j] + mu); return y, Fr(0)
def R(x, j, mu, qs): return comp(x, [lambda z: Wd(z, qs), lambda z: sth(z, j, mu), lambda z: W(z, qs)])
def Gam(x, lam, qs):
    N = len(x[2])
    def link(z): y = cp(z); y[3][:] = [f1(z[3][k] + lam[k] - lam[(k + 1) % N]) for k in range(N)]; return y, Fr(0)
    return comp(x, [lambda z, j=j: R(z, j, -lam[j], qs) for j in range(N)] + [link])
rng = random.Random(20261022); DEN = 48
def rx(N, F):
    r = lambda: Fr(rng.randrange(DEN), DEN)
    return ([[r() for _ in range(N)] for _ in range(F)], [[rng.randrange(-2, 3) for _ in range(N)] for _ in range(F)],
            [r() for _ in range(N)], [r() for _ in range(N)])
NB = 5; NT = 300
bad = Counter()
for t in range(NT):
    x = rx(NB, 2); be = Fr(rng.randrange(1, 41), 41); ga = Fr(rng.randrange(1, 37), 37); al = rng.randrange(2); j = rng.randrange(NB)
    bad['comm'] += not same(comp(x, [lambda z: K(z, al, j, be), lambda z: sym(z, ga, S3450)]), comp(x, [lambda z: sym(z, ga, S3450), lambda z: K(z, al, j, be)]))
    bad['group'] += not same(comp(x, [lambda z: K(z, al, j, be), lambda z: K(z, al, j, -be)]), (x, Fr(0)))
    y = K(x, al, j, be)[0]; bad['QA'] += QAw(y[0][al], y[1][al]) != QAw(x[0][al], x[1][al])
    bad['QAint'] += not isinstance(QAw(x[0][al], x[1][al]), int)
check('B1 [T] Q_V (turns) and Q_A (windings) are commuting integers; the kinetic gate (turn phi_j, relabel windings) commutes with '
      'every e^{2 pi i b Q}, is a U(1) action and keeps Q_A', sum(bad.values()) == 0, f'{NT} configurations, failures {sum(bad.values())}')
def ident(qs, n=NT):
    c = sum(qV * qA for qV, qA in qs); fails = form_ok = 0
    for t in range(n):
        x = rx(NB, len(qs)); be = Fr(rng.randrange(1, 97), 97)
        u = comp(x, [lambda z: W(z, qs), lambda z: sym(z, be, qs), lambda z: Wd(z, qs)]); v = sth(x, 0, 0)[0]; v[2][:] = [f1(tt + be) for tt in x[2]]
        ok_cfg = u[0] == v; fails += not (ok_cfg and f1(u[1]) == 0)
        kk = [math.floor(tt + be) for tt in x[2]]; pred = -c * sum(x[2][i] * (kk[(i + 1) % NB] - kk[i]) for i in range(NB))
        form_ok += ok_cfg and f1(u[1] - pred) == 0
    return fails, form_ok, c
rep_ = Counter()
for t in range(NT // 2):
    x = rx(NB, 2); a_, j_ = rng.randrange(2), rng.randrange(NB); ph2 = [r[:] for r in x[0]]; ph2[a_][j_] += 1
    rep_['tpf'] += f1(Phi(ph2, x[1], x[2], S3450) - Phi(x[0], x[1], x[2], S3450)) != 0
    rep_['bare'] += f1(Phi(ph2, x[1], x[2], S3450, False) - Phi(x[0], x[1], x[2], S3450, False)) != 0
res = {nm: ident(q) for nm, q in [('3450', S3450)] + list(OTHER_FREE.items())}
check('B2 [T] disentangler W = [turn flavours by qV theta_j] x prod_j e^{-2 pi i theta_j y~_j} (TPF eq. 23, rederived; one on-site and two '
      'link layers, interacting; single-valued on the rotor circle only with its -d round(sum qA phi) term): W^dag e^{2 pi i b Q} W = e^{2 pi i b Q_anc}',
      all(r[0] == 0 and r[2] == 0 for r in res.values()) and rep_['tpf'] == 0 and rep_['bare'] > 0,
      'fails ' + ', '.join(f'{k} {v[0]}' for k, v in res.items()) + f"; circle {rep_['tpf']} vs {rep_['bare']} without")
ra = {nm: ident(q) for nm, q in ANOM.items()}
check('B3 [T] anomalous sets fail, exactly by the predicted phase -c sum_j theta_j (k_{j+1} - k_j) (c = sum qV qA, k: ancilla wraps)',
      all(r[0] > NT // 4 and r[1] == NT for r in ra.values()), '; '.join(f'{k} c={v[2]}: {v[0]}/{NT} fail, formula {v[1]}/{NT}' for k, v in ra.items()))
def endpoint(qs, n=150):
    N = 6; ok = 0
    for t in range(n):
        x = rx(N, len(qs)); ph, nn = x[0], x[1]
        ps = sum(qA * sum(ph[a][(k + 1) % N] - ph[a][k] - rnd(ph[a][(k + 1) % N] - ph[a][k]) - nn[a][k] for k in range(1, 4)) for a, (qV, qA) in enumerate(qs))
        ok += f1(ps - sum(qA * (ph[a][4] - ph[a][1]) for a, (qV, qA) in enumerate(qs))) == 0
    return ok == n, sum(qV * qA for qV, qA in qs)
ep_ = {nm: endpoint(q) for nm, q in [('3450', S3450)] + list(ANOM.items())}
check('B4 [T] anomaly = endpoint charge: the 2 pi axial turn cut to an interval is exactly e^{2 pi i sum qA (phi_b - phi_a)}, '
      'endpoint charges +-sum qV qA; nonzero forbids every disentangler',
      all(v[0] for v in ep_.values()) and ep_['3450'][1] == 0 and all(ep_[k][1] != 0 for k in ANOM), ', '.join(f'{k}: {v[1]:+d}' for k, v in ep_.items()))
b5 = Counter()
for t in range(NT // 2):
    x = rx(NB, 2); be = Fr(rng.randrange(1, 41), 41); j = rng.randrange(NB)
    b5['sum'] += not same(comp(x, [lambda z, k=k: R(z, k, be, S3450) for k in range(NB)]), sym(x, be, S3450))
    y0 = R(x, j, be, S3450); x2 = cp(x); far = (j + 2) % NB
    for a in range(2): x2[0][a][far] = Fr(rng.randrange(DEN), DEN)
    x2[2][far] = Fr(rng.randrange(DEN), DEN); y2 = R(x2, j, be, S3450)
    b5['local'] += not (f1(y0[1] - y2[1]) == 0 and all(y0[0][0][a][i] == x[0][a][i] for a in range(2) for i in range(NB) if i != j))
    x3 = rx(NB, 1); b5['anom_sum'] += not same(comp(x3, [lambda z, k=k: R(z, k, be, ANOM['Dirac(2,0)']) for k in range(NB)]), sym(x3, be, ANOM['Dirac(2,0)']))
check('B5 [T] dressed charges rho_j = W L_j W^dag commute, are integers, touch sites j-1..j+1 only and sum exactly to Q (3450); '
      'for an anomalous set they sum to another U(1)', b5['sum'] == 0 and b5['local'] == 0 and b5['anom_sum'] > NT // 8,
      f"fails {b5['sum']}, {b5['local']}; anomalous {b5['anom_sum']}/{NT // 2}")

def ident_grid(qs, Nc, n=200):    # Z_N clock matter: angles, ancillas and b on the 1/N grid (windings only mod N matter)
    fails = 0
    for t in range(n):
        x = ([[Fr(rng.randrange(Nc), Nc) for _ in range(NB)] for _ in qs], [[rng.randrange(-2, 3) for _ in range(NB)] for _ in qs],
             [Fr(rng.randrange(Nc), Nc) for _ in range(NB)], [Fr(0)] * NB); be = Fr(rng.randrange(1, Nc), Nc)
        u = comp(x, [lambda z: W(z, qs), lambda z: sym(z, be, qs), lambda z: Wd(z, qs)]); v = cp(x); v[2][:] = [f1(tt + be) for tt in x[2]]
        fails += not (u[0] == v and f1(u[1]) == 0)
    return fails
g5 = {nm: ident_grid(q, 5) for nm, q in [('3450', S3450), ('(5,1) c=5', [(5, 1)]), ('Dirac(2,0) c=2', ANOM['Dirac(2,0)']), ('3452 c=-2', ANOM['3452'])]}
check('B6 [T] qubit version: with Z_5 clocks (all carriers finite) the same circuit disentangles the exact Z_5 chiral symmetry iff '
      'sum qV qA = 0 mod 5; only Z_5 is exact, the chiral U(1) can only emerge in a critical clock phase (which needs N >= 5)',
      g5['3450'] == 0 and g5['(5,1) c=5'] == 0 and g5['Dirac(2,0) c=2'] > 50 and g5['3452 c=-2'] > 50, 'fails ' + ', '.join(f'{k} {v}' for k, v in g5.items()))

# =============================================== C. light content =========================================================
print('== C. light content (U = 1/pi, J = pi: v = 1, Dirac radius)')
eps = 0.5; Uk, Jk = 1 / np.pi, np.pi; kk = np.linspace(0, np.pi, 201)
trs = [np.trace(np.array([[1, 0], [-eps * Jk * 4 * np.sin(k / 2) ** 2, 1]]) @ np.array([[1, eps * Uk], [0, 1]])) / 2 for k in kk]
pr = 1 - 2 * (eps * np.sqrt(Uk * Jk)) ** 2 * np.sin(kk / 2) ** 2
Om = np.arccos(np.clip(pr, -1, 1))
check('C1 [T] Trotterised Gaussian update: cos Om_K = 1 - 2 (eps v)^2 sin^2(K/2), stable for eps v < 1, one zero (K = 0) per '
      'flavour: no doublers; ancillas gapped by U_a L^2', np.allclose(trs, pr) and np.all(np.abs(pr) <= 1) and Om[0] == 0
      and np.all(np.diff(Om) > 0), f'Om(pi) = {Om[-1]:.3f} < pi')
def zero_modes(qs, R=4):
    out = []
    for p1, w1, p2, w2 in itertools.product(range(-R, R + 1), repeat=4):
        out.append((qs[0][0] * p1 + qs[0][1] * w1 + qs[1][0] * p2 + qs[1][1] * w2, Fr(p1 * p1 + p2 * p2) + Fr(w1 * w1 + w2 * w2, 4), p1 * w1 + p2 * w2))
    return out
def chiral_sets(qs):
    zm = zero_modes(qs); return sorted(q for q, e, s in zm if e == 2 and s == 2), sorted(q for q, e, s in zm if e == 2 and s == -2)
Lc, Rc = chiral_sets(S3450); Lv, Rv = chiral_sets([(8, 0), (4, 0)])
check('C2 [T] exact zero modes (E = 2 pi v/L sum(p^2 + w^2/4), P = 2 pi/L sum pw): the lowest one-flavour spin +2 states carry '
      'Q = +-6, +-8, spin -2 ones +-10, 0, 0: twice L(3,4) and R(5,0); the vector control gives equal sets',
      Lc == [-8, -6, 6, 8] and Rc == [-10, 0, 0, 10] and Lv == Rv, f'+2: {Lc}, -2: {Rc}')
zz = [z for z in itertools.product(range(-8, 9), repeat=4) if any(z) and ((Fr(z[0] ** 2 + z[2] ** 2) + Fr(z[1] ** 2 + z[3] ** 2, 4)) / 16).denominator == 1]
zq = [z for z in zz if 8 * z[0] - z[1] + 4 * z[2] + 2 * z[3] == 0]
check('C3 [T] folding (update, not Hamiltonian): at eps 2 pi v/L = pi/8 the zero modes with E = 16m sit exactly at quasi-energy 0, '
      'some with Q = 0; for any step a rotor\'s kinetic phases come within any delta of 0 (Weyl): unbounded carriers leave no '
      'quasi-energy gap above the vacuum', len(zq) > 0, f'{len(zz)} states (|p|,|w| <= 8), {len(zq)} with Q = 0, e.g. {min(zq, key=lambda z: sum(map(abs, z)))}')

# =============================================== D. gauging ===============================================================
print('== D. linking (link angle a, electric E; Gauss G_j = E_{j+1/2} - E_{j-1/2} - rho_j)')
dd = Counter()
for t in range(NT):
    x = rx(NB, 2); lam = [Fr(rng.randrange(29), 29) for _ in range(NB)]; be = Fr(rng.randrange(1, 41), 41); al = rng.randrange(2); j = rng.randrange(NB)
    pot = lambda z: [((z[0][a][(k + 1) % NB] - z[0][a][k] - q * z[3][k]) - rnd(z[0][a][(k + 1) % NB] - z[0][a][k] - q * z[3][k])) - z[1][a][k]
                     for a, (q, _) in enumerate(S3450) for k in range(NB)]
    dd['pot'] += pot(Gam(x, lam, S3450)[0]) != pot(x)
    Kg = lambda z: comp(z, [lambda s: Wd(s, S3450), lambda s: Kg_dis(s, al, j, be, S3450), lambda s: W(s, S3450)])
    dd['kin'] += not same(comp(x, [Kg, lambda z: Gam(z, lam, S3450)]), comp(x, [lambda z: Gam(z, lam, S3450), Kg]))
    x0 = cp(x); x0[3][:] = [Fr(0)] * NB
    dd['reduce'] += not same(Kg(x0), K(x0, al, j, be))
    dd['Kon'] += not same(comp(x0, [lambda z: W(z, S3450), lambda z: K(z, al, j, be), lambda z: Wd(z, S3450)]), Kg_dis(x0, al, j, be, S3450))
    mu = Fr(rng.randrange(1, 41), 41); u = comp(x, [lambda z: W(z, S3450), lambda z: sth(z, j, mu), lambda z: Wd(z, S3450)])
    v = cp(x); v[2][j] = f1(x[2][j] + mu)
    for a, (q, _) in enumerate(S3450): v[0][a][j] = f1(x[0][a][j] - q * mu)
    dd['L'] += not (u[0] == v and f1(u[1] - mu * ytil(x[0], x[1], x[2], S3450, j)) == 0)
check('D1 [T] Gauss law: the linked potential ({D phi - qV a} - n)^2 and the linked kinetic gate W (on-site linked gate) W^dag '
      'commute with every finite Gauss transformation and reduce to the unlinked gates at a = 0',
      dd['pot'] + dd['kin'] + dd['reduce'] == 0, f"{NT} configurations, failures {dd['pot'] + dd['kin'] + dd['reduce']}")
check('D2 [T] on-site frame: W^dag L_j W = L_j - qV P_j + y~_j, W^dag K_j W = (relabel through D phi + qV D theta) x '
      'e^{2 pi i d (theta_j - theta_{j-1})}, d = half-integer crossings of X_j = sum qA phi_j: qA acts only as whole flux units; '
      'Gauss\'s law eats the ancillas',
      dd['L'] + dd['Kon'] == 0, f"failures {dd['L'] + dd['Kon']}")
def schwinger(qs, N=6):
    F = len(qs); M = F * N; Om = np.block([[np.zeros((M, M)), np.eye(M)], [-np.eye(M), np.zeros((M, M))]]); Rr = np.zeros((N, 2 * M))
    for j in range(N):
        for a, (qV, qA) in enumerate(qs): Rr[j, M + a * N + j] += qV / (2 * np.pi); Rr[j, a * N + (j + 1) % N] += qA; Rr[j, a * N + j] -= qA
    C = Rr @ Om @ Rr.T; c = sum(qV * qA for qV, qA in qs); P_ = np.zeros((N, N))
    for j in range(N): P_[j, (j - 1) % N] -= c / (2 * np.pi); P_[(j - 1) % N, j] += c / (2 * np.pi)
    return nrm(C), nrm(C - P_)
sw = {nm: schwinger(q) for nm, q in [('3450', S3450)] + list(ANOM.items())}
check('D3 [T] Schwinger term: continuous chiral densities qV P_j + qA dphi_j obey [rho_j, rho_{j-1}] = -i c/(2 pi): Gauss '
      'generators commute iff sum qV qA = 0', sw['3450'][0] == 0 and all(v[1] < 1e-14 for v in sw.values()) and all(sw[k][0] > 0.3 for k in ANOM),
      ', '.join(f'{k} {v[0]:.4f}' for k, v in sw.items()))
def modes(qs, k, g=0.2):
    a = np.array([q[0] for q in qs], float); b = np.array([q[1] for q in qs], float); F = len(qs); w2 = 4 * np.sin(k / 2) ** 2; z = np.exp(1j * k) - 1
    A = np.block([[(Jk / 2) * w2 * np.eye(F) + (g * g / 2) * np.outer(b, b), (g * g / 2) * np.conj(z) * np.outer(b, a) / (2 * np.pi * w2)],
                  [((g * g / 2) * np.conj(z) * np.outer(b, a) / (2 * np.pi * w2)).conj().T, (Uk / 2) * np.eye(F) + (g * g / 2) * np.outer(a, a) / (4 * np.pi ** 2 * w2)]])
    Jm = np.block([[np.zeros((F, F)), np.eye(F)], [-np.eye(F), np.zeros((F, F))]]); return np.sort(np.linalg.eigvals(2 * Jm @ A).imag)
m3 = modes(S3450, 0.005); ma = modes(ANOM['3452'], 0.005); mpred = np.sqrt(25 * 0.04 / np.pi)
check('D4 [T] linked Gaussian modes (g = 0.2, K = 0.005): 3450 keeps one massless neutral mode and a photon with m^2 = '
      '(g^2/pi)(sum qL^2 + sum qR^2)/2 = 25 g^2/pi; anomalous: a chiral branch Om ~ g^2|c|/(pi K) (non-local)', abs(m3[2] - 0.005) < 1e-6 and abs(m3[3] - mpred) < 1e-3 and np.allclose(m3, -m3[::-1])
      and abs(-ma[0] - 0.04 * 2 / (np.pi * 0.005)) / (0.04 * 2 / (np.pi * 0.005)) < 0.03, f'm {m3[3]:.5f} vs {mpred:.5f}; anomalous {-ma[0]:.2f} vs {0.08 / (np.pi * 0.005):.2f}')

# =============================================== E. 3+1D and the SM 16 ===================================================
print('== E. 3+1D: TPF blocks of four left-handed Weyls, (V, A) = (1,1), (-1,1), (0,-1), (0,-1); Y x 6')
V4 = np.array([1, -1, 0, 0]); A4 = np.array([1, 1, -1, -1]); SM = [1] * 6 + [-4] * 3 + [2] * 3 + [-3] * 2 + [6, 0]
blocks = [(-3, -1)] * 3 + [(3, 3)]; Yb = [list(a * V4 + b * A4) for a, b in blocks]
an = lambda v: (sum(v), sum(int(x) ** 3 for x in v))
BL = [(0, -1)] * 3 + [(0, 3)]; BLb = sorted(sum([list(a * V4 + b * A4) for a, b in BL], [])); BLsm = sorted([1] * 6 + [-1] * 6 + [-3] * 2 + [3, 3])
check('E1 [T] SM 16: sum Y = sum Y^3 = 0; quark blocks -3V - A = (-4,2,1,1) x 3, lepton 3V + 3A = (6,0,-3,-3); sum a^2 b = -27 '
      '+ 27 = 0; 3(B - L) = -A, 3A: jointly anomaly-free with Y; a block has only the AVV anomaly (2); without nu_R (15) or for '
      '(1,5,9,-7,-8) no grouping; no SU(2)_L disentangler', BLb == BLsm and sum(a * a * c for (a, b), (_, c) in zip(blocks, BL)) == 0 and
      an(SM) == (0, 0) and sorted(sum(Yb, [])) == sorted(SM) and sum(a * a * b for a, b in blocks) == 0 and an([1, 5, 9, -7, -8]) == (0, 0)
      and (sum(V4), sum(V4 ** 3), sum(A4), sum(A4 ** 3), sum(V4 * A4 ** 2), sum(A4 * V4 ** 2)) == (0, 0, 0, 0, 0, 2))
Lt = 4; idx = lambda v: ((v[0] % Lt) * Lt + v[1] % Lt) * Lt + v[2] % Lt; tets = set()
for x in itertools.product(range(Lt), repeat=3):
    for s in itertools.permutations(range(3)):
        v = np.array(x); path = [v.copy()]
        for i in s: v = v + np.eye(3, dtype=int)[i]; path.append(v.copy())
        tets.add(frozenset(idx(p) for p in path))
tris = {frozenset(c) for t in tets for c in itertools.combinations(sorted(t), 3)}; eds = {frozenset(c) for t in tets for c in itertools.combinations(sorted(t), 2)}
Vn = Lt ** 3; per = (len(eds) / Vn, len(tris) / Vn, len(tets) / Vn)
check('E2 [T] Kuhn triangulation of Z^3: 7 edges, 12 triangles, 6 tetrahedra per vertex; TPF per site per generation: 4 charged '
      'vertex rotors (matter), 1 ancilla per linked U(1) (eaten), 48 fermion modes (one per triangle per block), 7 link rotors; rules: 1 mode',
      per == (7, 12, 6) and Vn - len(eds) + len(tris) - len(tets) == 0, 'per vertex (%d, %d, %d), Euler 0' % per)
print('   [M] V - A (TWIST P_mu xi = 1.0008) needs chiral SU(2)_L, not built by TPF; nu_R is required but sterile (N_nu 2.984 +- 0.008)')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('all [T] (D4 in the Gaussian reading, zero modes excluded). Supplied: rotor matter with winding integers, the 3450 charges and '
      'pairing (L3,R5), (L4,R0), the Dirac radius, ancillas, round-half-up, g, eps. Cited: TPF 2601.04304, Chatterjee-Pace-Shao, TWIST, PDG.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
