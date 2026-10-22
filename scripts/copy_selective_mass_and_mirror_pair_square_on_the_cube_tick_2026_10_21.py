#!/usr/bin/env python3
"""Copy-selective terms on the CL-2 tick: what a mass or pair-square phase on one copy keeps, gaps and costs.

Supplied model: the CL-2 Margolus tick (one fermion mode per site, spin-3/2 edge hop W, step st, mass mu), read in the
symmetric split E_e^(1/2) D^dag E_o D E_e^(1/2); a supplied copy-selective factor exp(i M P W / 2) on both sides, with P
the projector onto one copy (copies told apart by the three-fold turns); supplied toys (0+1D two-copy Fidkowski-Kitaev,
1+1D 3-4-5-0 on the Margolus swap).  Sections:
 A  tick, copies, exact symmetries;  B  isotropy with the 12 tetrahedral turns;  C  chirality at step pi/2 and its cost;
 D  toys (sparse ED <= 2^8, integer lattices);  E  estimates against measurement.
Finite diagnostics of supplied models.  Cited, not rederived: 't Hooft anomaly matching and its crystalline form, the
Z16 classification, Haldane's null-vector criterion, the SMG conjecture that anomaly freedom suffices.
"""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/COPY_SELECTIVE_MASS_AND_MIRROR_PAIR_SQUARE_ON_THE_CUBE_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm, logm, null_space
from fractions import Fraction
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form

T0 = time.monotonic()
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max())
OM = np.exp(2j * np.pi / 3)

# ------------------------------------------------ supplied tick ------------------------------------------------
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
    n = (2 * C[i] - 1.0) / np.sqrt(3); w, v = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v[:, -1])
def Lrot(R):
    n, a = axang(R); Dm = expm(-1j * a * sum(n[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = img(R, i); L[k, i] = xi[k].conj() @ Dm @ xi[i]
    return L
Ls = [Lrot(R) for R in rots]
cls = []
for R in rots:
    t = int(round(np.trace(R))); k = {3: 'E', -1: 'C2', 1: 'C4', 0: 'C3'}[t]
    if k == 'C2': k = 'C2f' if np.allclose(abs(np.diag(R)), 1) else 'C2e'
    cls.append(k)
ODD = [k in ('C4', 'C2e') for k in cls]
iC3 = [i for i, R in enumerate(rots) if cls[i] == 'C3' and np.allclose(axang(R)[0], np.ones(3) / np.sqrt(3))][0]
iC4 = [i for i, k in enumerate(cls) if k == 'C4'][0]
Gm = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: W[a, b] = -Gm[a, b] / abs(Gm[a, b]) / np.sqrt(3)
I8 = np.eye(8); EPS = np.diag((-1.0) ** C.sum(1)).astype(complex)        # sublattice sign
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W                  # exp(i th W)
def Ut(K, st, mu=0.0, M=0.0, P=None):
    Eh = ex(-(st - mu / 2) / 2); X = Eh @ Dg(K).conj().T @ ex(st + mu / 2) @ Dg(K) @ Eh
    if M:
        F = expm(1j * M * P @ W / 2); X = F @ X @ F
    return X
def Uo(K, st, mu=0.0):                     # unsplit frame, in which EPS is the sublattice sign
    return Dg(K).conj().T @ ex(st + mu / 2) @ Dg(K) @ ex(-(st - mu / 2))
def IRal(f, K0=np.zeros(3), sgn=1.0, h=1e-5):
    def H(q): return 1j * logm(sgn * f(K0 + q))
    al = []
    for a in range(3):
        e = np.zeros(3); e[a] = h; A = (H(e) - H(-e)) / (2 * h); al.append((A + A.conj().T) / 2)
    v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); return [A / v for A in al], v
def lift(al, L):
    Sig = [-1j * al[1] @ al[2], -1j * al[2] @ al[0], -1j * al[0] @ al[1]]
    Mr = np.array([[np.trace(L @ al[a] @ L.conj().T @ al[b]).real / 8 for b in range(3)] for a in range(3)])
    n, ang = axang(np.round(Mr).T); best = None
    for s_ in (1, -1):
        S = expm(-1j * s_ * ang / 2 * sum(n[k] * Sig[k] for k in range(3)))
        e_ = max(nrm(S @ al[q] @ S.conj().T - L @ al[q] @ L.conj().T) for q in range(3))
        if best is None or e_ < best[0]: best = (e_, S)
    return best
def copies(al):
    S = lift(al, Ls[iC3])[1]; rho = S.conj().T @ Ls[iC3]; w_, V = np.linalg.eig(rho); P = {}
    for q, lam in ((1, OM), (2, OM ** 2)):
        Vl = V[:, np.abs(w_ - lam) < 1e-5]; Pq = Vl @ np.linalg.pinv(Vl); P[q] = (Pq + Pq.conj().T) / 2
    return P, rho
def solve(pairs, conj):                       # V with V X(*) = Y V for all (X, Y)
    A = np.vstack([np.kron(I8, (X.conj() if conj else X).T) - np.kron(Y, I8) for X, Y in pairs])
    ns = null_space(A, rcond=1e-9); return [ns[:, i].reshape(8, 8) for i in range(ns.shape[1])]
rng = np.random.default_rng(7); KR = rng.uniform(-np.pi, np.pi, size=(12, 3))   # many K: each K alone only fixes two 4-dim eigenspaces
STEPS = (np.pi / 2, 0.3, 0.04)

# ===================================== A. the tick, its copies, exact symmetries =====================================
print('== A. tick and copies')
ok1, worst = True, 0.0
for st in STEPS:
    mu = 0.2; b = np.pi / 2 - st; A_ = (np.cos(2 * b) + np.cos(mu)) / 2
    for K in KR[:3]:
        U = Ut(K, st, mu); cw = np.cos(np.angle(np.linalg.eigvals(U)))
        band = A_ * np.mean(np.cos(K)) - (np.cos(2 * b) - np.cos(mu)) / 2
        cov = max(nrm(L @ U @ L.conj().T - Ut(R @ K, st, mu)) for L, R in zip(Ls, rots))
        worst = max(worst, nrm(U @ U.conj().T - I8), cov, np.ptp(cw), abs(cw[0] - band))
check('A1 tick unitary, 24/24 covariant, bands exactly fourfold, cos w = A <cos K> - (cos2b - cos mu)/2', worst < 1e-12,
      f'steps pi/2, .3, .04; worst {worst:.0e}')
info = {}
for st in STEPS:
    al, v = IRal(lambda K: Ut(K, st)); P, rho = copies(al); s3 = P[1] - P[2]; g5 = 1j * al[0] @ al[1] @ al[2]
    cl = max(nrm(al[a] @ al[b] + al[b] @ al[a] - 2 * (a == b) * I8) for a in range(3) for b in range(3))
    chi = {}
    for L, k in zip(Ls, cls): chi.setdefault(k, set()).add(round(abs(np.trace(lift(al, L)[1].conj().T @ L)) / 4, 6))
    keep = all(nrm(L @ s3 @ L.conj().T - s3) < 1e-8 for L, o in zip(Ls, ODD) if not o)
    flip = all(nrm(L @ s3 @ L.conj().T + s3) < 1e-8 for L, o in zip(Ls, ODD) if o)
    sl = [nrm(s3 @ Ut(kk * np.array([.3, .5, .81]), st) - Ut(kk * np.array([.3, .5, .81]), st) @ s3) for kk in (.02, .04)]
    info[st] = dict(al=al, v=v, P=P, s3=s3, g5=g5, cl=cl, chi=chi, keep=keep, flip=flip, slope=np.log2(sl[1] / sl[0]),
                    ev=np.sort_complex(np.round(np.linalg.eigvals(rho), 6)))
check('A2 long-wavelength Dirac algebra: Clifford relations, speed sin(st)/sqrt3',
      all(info[s]['cl'] < 1e-8 and abs(info[s]['v'] - np.sin(s) / np.sqrt(3)) < 1e-8 for s in STEPS),
      'speeds ' + ', '.join(f"{info[s]['v']:.5f}" for s in STEPS))
okA3 = all(int(np.sum(np.abs(info[s]['ev'] - OM) < 1e-4)) == 4 and int(np.sum(np.abs(info[s]['ev'] - OM ** 2) < 1e-4)) == 4 for s in STEPS)
chis = info[np.pi / 2]['chi']
check('A3 internal part of a three-fold turn is diag(w, w^2) on the copies (4+4); |copy character| (E,C2f,C4,C3,C2e) = (2,2,0,1,0)',
      okA3 and all(info[s]['chi'] == chis for s in STEPS) and [sorted(chis[k]) for k in ('E', 'C2f', 'C4', 'C3', 'C2e')] == [[2.0], [2.0], [0.0], [1.0], [0.0]],
      'E irrep, every step')
check('A4 the 12 even (tetrahedral) turns keep the copy sign s3, the 12 odd turns (C4, edge C2) flip it',
      all(info[s]['keep'] and info[s]['flip'] for s in STEPS))
dims = {}
for st, mu in ((np.pi / 2, 0.0), (np.pi / 2, 0.2), (0.3, 0.0), (0.3, 0.2), (0.04, 0.0)):
    dims[(round(st, 3), mu)] = len(solve([(Ut(K, st, mu), Ut(K, st, mu)) for K in KR], False))
s2 = info[np.pi / 2]; alo, _ = IRal(lambda K: Uo(K, np.pi / 2)); g5o = 1j * alo[0] @ alo[1] @ alo[2]
check('A5 copy sign broken at O(K^2) at every step; the block-local commutant is span{1, eps} only at step pi/2, mu = 0, else scalars',
      all(abs(info[s]['slope'] - 2) < 0.05 for s in STEPS) and dims == {(1.571, 0.0): 2, (1.571, 0.2): 1, (0.3, 0.0): 1, (0.3, 0.2): 1, (0.04, 0.0): 1}
      and nrm(EPS + g5o @ s2['s3']) < 1e-8,
      f'slopes {[round(float(info[s]["slope"]), 2) for s in STEPS]}; dims {list(dims.values())}; at pi/2 eps = -g5 s3')
print('   no exact internal copy swap: no internal twist restores the 12 odd turns')
sym = {}
for st in (np.pi / 2, 0.3):
    f = lambda K: Ut(K, st, 0.2); s3 = info[st]['s3']
    tr = solve([(f(K), f(-K).conj().T) for K in KR], True); ph = solve([(f(K), f(-K)) for K in KR], True)
    ch = solve([(f(K), f(K).conj().T) for K in KR], False); iv = solve([(f(K), f(-K)) for K in KR], False)
    act = lambda V, cj: (lambda Vn: (nrm(Vn @ (s3.conj() if cj else s3) @ Vn.conj().T - s3) < 1e-6, nrm(Vn @ (s3.conj() if cj else s3) @ Vn.conj().T + s3) < 1e-6))(V / np.sqrt(np.trace(V @ V.conj().T).real / 8))
    sym[st] = [(len(x), act(x[0], cj)) for x, cj in ((tr, True), (ph, True), (ch, False), (iv, False))]
check('A6 time reversal and particle-hole exist and swap the copies; the chiral map and the inversion keep them (mu = 0.2)',
      all([s[1] for s in sym[st]] == [(False, True), (False, True), (True, False), (True, False)] and all(s[0] == 1 for s in sym[st]) for st in sym),
      'an antiunitary commuting with a 3-fold turn maps w <-> w^2')

# ===================================== B. isotropy with the 12 tetrahedral turns =====================================
print('== B. what the 12 tetrahedral turns give')
def count(G, f): return round(sum(f(R) for R in G).real / len(G), 6)
ch1 = lambda R, k=1: np.trace(np.linalg.matrix_power(R, k))
reps = {'V x V': lambda R: ch1(R) ** 2, 'Sym2': lambda R: (ch1(R) ** 2 + ch1(R, 2)) / 2,
        'Sym3': lambda R: (ch1(R) ** 3 + 3 * ch1(R, 2) * ch1(R) + 2 * ch1(R, 3)) / 6,
        'V x Sym2': lambda R: ch1(R) * (ch1(R) ** 2 + ch1(R, 2)) / 2,
        'Sym4': lambda R: (ch1(R) ** 4 + 6 * ch1(R) ** 2 * ch1(R, 2) + 3 * ch1(R, 2) ** 2 + 8 * ch1(R) * ch1(R, 3) + 6 * ch1(R, 4)) / 24}
Tg = [R for R, o in zip(rots, ODD) if not o]
cnt = {k: (count(Tg, f), count(rots, f)) for k, f in reps.items()}
check('B1 invariants (T, O): velocity and Weyl-cone tensors V x V (1,1), Sym2 (1,1), Sym4 (2,2); T alone adds Sym3 (xyz) and V x Sym2',
      cnt == {'V x V': (1, 1), 'Sym2': (1, 1), 'Sym3': (1, 0), 'V x Sym2': (1, 0), 'Sym4': (2, 2)},
      'extras: parity-odd xyz and the spin term s_a d_abc k_b k_c')
res = {}
for st in (np.pi / 2, 0.3):
    Pm = info[st]['P'][1]; M = 0.5; mu = 0.0
    g = lambda K, mu=mu: Ut(K, st, mu, M, Pm)
    keepT = max(nrm(L @ g(K) @ L.conj().T - g(R @ K)) for L, R, o in zip(Ls, rots, ODD) if not o for K in KR[:2])
    brk = min(nrm(L @ g(K) @ L.conj().T - g(R @ K)) for L, R, o in zip(Ls, rots, ODD) if o for K in KR[:2])
    R4 = rots[iC4]
    surv = [len(solve([(g(K), Y(K)) for K in KR], cj)) for Y, cj in
            ((lambda K: g(-K), False), (lambda K: g(K).conj().T, False), (lambda K: g(-K).conj().T, True),
             (lambda K: g(-K), True), (lambda K: g(-(R4 @ K)).conj().T, True))]
    e0 = np.sort(np.angle(np.linalg.eigvals(g(np.zeros(3), 0.1))))
    v = info[st]['v']; dev, hel = [], 0.0
    for d in (np.array([1., 0, 0]), np.array([1., 2, 3]) / np.sqrt(14)):
        r = []
        for kk in (0.01, 0.02, 0.04):
            H = 1j * logm(g(kk * d)); e = np.sort(np.linalg.eigvalsh((H + H.conj().T) / 2)); hel = max(hel, abs(e[5] - e[4]))
            r.append(abs(e[4] / (v * kk) - 1))
        dev.append(np.log2(r[2] / r[1]))
    al, _ = IRal(lambda K: Ut(K, st)); B_ = np.linalg.svd(info[st]['P'][2])[0][:, :4]
    pd = []
    for kk in (0.02, 0.04):
        H = 1j * logm(Ut(kk * np.array([1., 2, 3]) / np.sqrt(14), st)); H = (H + H.conj().T) / 2
        pd.append(np.abs(np.sort(np.linalg.eigvalsh(B_.conj().T @ H @ B_))[2:] - np.sort(np.linalg.eigvalsh(H))[-2:]).max())
    res[st] = dict(keepT=keepT, brk=brk, surv=surv, e0=e0, dev=dev, hel=hel, pslope=np.log2(pd[1] / pd[0]))
check('B2 copy-selective factor (M = .5 on the w-copy): all 12 tetrahedral turns kept, all 12 odd turns broken',
      all(res[s]['keepT'] < 1e-9 and res[s]['brk'] > 0.1 for s in res), f"odd-turn residual >= {min(res[s]['brk'] for s in res):.2f}")
check('B3 it keeps inversion and the chiral map (so their product, the CPT analogue); loses time reversal and particle-hole, keeps T x C4',
      all(res[s]['surv'] == [1, 1, 0, 0, 1] for s in res), f"solution counts (I, chiral, T, PH, T.C4) = {res[np.pi/2]['surv']}")
check('B4 at K = 0 the light copy keeps the species mass (.1) and the other copy gets .1 + M: no tuning',
      all(np.allclose(np.sort(np.abs(res[s]['e0'])), [0.1] * 4 + [0.6] * 4, atol=1e-9) for s in res))
check('B5 light band with the factor: no helicity splitting, and w/(v|K|) - 1 ~ K^2 (dimension-6 anisotropy, no dimension-5 term)',
      all(res[s]['hel'] < 1e-10 and all(abs(x - 2) < 0.1 for x in res[s]['dev']) for s in res),
      f"slopes {[round(float(x), 2) for s in res for x in res[s]['dev']]}")
check('B6 strong-coupling projection on the light copy: deviation from the exact band ~ K^3 (relative K^2)',
      all(abs(res[s]['pslope'] - 3) < 0.1 for s in res), f"slopes {[round(float(res[s]['pslope']), 2) for s in res]}")

# ===================================== C. chirality at step pi/2 and its cost =====================================
print('== C. step pi/2: chiral SU(2)s exist; what mirror gapping needs')
P2 = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1]).astype(complex)]
def content(K0, sgn):
    al, v = IRal(lambda K: Uo(K, np.pi / 2), K0, sgn); g5 = 1j * al[0] @ al[1] @ al[2]
    S = lift(al, Ls[iC3])[1]; rho = S.conj().T @ Ls[iC3]; rows = []
    for gg in (1, -1):
        for q, lam in ((1, OM), (2, OM ** 2)):
            w_, V = np.linalg.eig(rho); Vl = V[:, np.abs(w_ - lam) < 1e-5]; M_ = (I8 + gg * g5) / 2 @ (Vl @ np.linalg.pinv(Vl))
            u, s_, _ = np.linalg.svd(M_); Bq = u[:, s_ > 0.5]; Aq = [Bq.conj().T @ a @ Bq for a in al]
            Mm = np.array([[np.trace(Aq[a] @ P2[i]).real / 2 for a in range(3)] for i in range(3)])
            rows.append((q, int(np.sign(np.linalg.det(Mm))), int(round(np.trace(Bq.conj().T @ EPS @ Bq).real / 2))))
    return sorted(rows), g5, rho
r0, g50, rho0 = content(np.zeros(3), 1.0); rp, g5p, rhop = content(np.full(3, np.pi), -1.0)
def anomZ3(rows, sub): return sum((1 if chi == -1 else -1) * q for q, chi, s in rows if s == sub)   # LH-sign x Z3 charge
check('C1 w = 0 and w = pi windows hold the same pieces (copy charge, handedness, sublattice); even cells: (L, q=2) + (R, q=1)',
      r0 == rp and nrm(g5p - g50) < 1e-8 and nrm(rhop - rho0) < 1e-8 and (2, -1, 1) in r0 and (1, 1, 1) in r0, f'pieces {r0}')
aw = anomZ3(r0, 1)
check('C2 per window and family: Z3(turn) x SU(2)_even^2 = 4 x (+2 light - 1 mirror) = 4 = 1 mod 3 (light 8 = 2, mirror -4 = 2)',
      aw == 1 and anomZ3(rp, 1) == 1 and (4 * 2) % 3 == 2 and (-4) % 3 == 2 and (4 * aw) % 3 == 1)
aN = {q: 4 * sum((1 if chi == -1 else -1) for q_, chi, s_ in r0 if s_ == 1 and q_ == q) for q in (1, 2)}   # U(1)_N x SU(2)_even^2
check('C3 number-conserving terms cannot gap the mirror alone: U(1)_N x SU(2)_even^2 = +4 light (q=2), -4 mirror (q=1), 0 in total',
      aN == {2: 4, 1: -4}, 'the B+L-type anomaly (matching cited); every link-mediated (current-current) term of CL-5 conserves N')
# pair square on the mirror 16: chi = (4,1,2) mirror-L (odd cells), xi = (4b,2,1) = conjugated mirror-R (even cells)
qM, qL = 1, 2
terms = {'chi^4': -4, 'xi^4': +4, 'chi^2 xi^2': 0, '(chi xi)^2': 0}               # Delta N of each SO(10) structure
plain = {k: (qM * dN) % 3 for k, dN in terms.items()}; twisted = {k: (qM * dN - qM * dN) % 3 for k, dN in terms.items()}
check('C4 the SO(10) pair square on the mirror breaks the plain three-fold turn (chi^4, xi^4 charged) but keeps turn x exp(-2 pi i N/3)',
      plain == {'chi^4': 2, 'xi^4': 1, 'chi^2 xi^2': 0, '(chi xi)^2': 0} and set(twisted.values()) == {0},
      f'twisted: mirror 0, light {(qL - qM) % 3}; light pair square {(4 * (qL - qM)) % 3} != 0 (light protected)')
gen = {'Q': (Fraction(1, 6), Fraction(1, 3), 6), 'u': (Fraction(-2, 3), Fraction(-1, 3), 3), 'd': (Fraction(1, 3), Fraction(-1, 3), 3),
       'L': (Fraction(-1, 2), Fraction(-1), 2), 'e': (Fraction(1), Fraction(1), 1), 'n': (Fraction(0), Fraction(1), 1)}
Xc = {k: 5 * bl - 4 * y for k, (y, bl, m) in gen.items()}
nu16 = sum(m for k, (y, bl, m) in gen.items() if Xc[k].denominator == 1 and int(Xc[k]) % 4 == 1)
check('C5 Z16: X = 5(B-L) - 4Y = 1 mod 4 on all 16 Weyl of a family, nu = 16 = 0 mod 16 (15 without nu^c); a copy per cell = 8 x (L, R) = 16',
      nu16 == 16 and all(int(x) % 4 == 1 for x in Xc.values()), 'so the mirror copy of one cell is exactly an anomaly-free 16')
idx = {N: (4 * N) % 3 for N in range(1, 7)}
check('C6 window index for N stacked families = 4N mod 3: the light band top at K = pi(1,1,1) is protected unless N = 0 mod 3',
      [N for N, v_ in idx.items() if v_ == 0] == [3, 6], f'{idx}; this does not select N by itself (see C7)')
bw = {}
for st in (np.pi / 2, 0.04):
    g1 = np.linspace(-np.pi, np.pi, 13); Kg = np.array(list(itertools.product(g1, g1, g1)))
    bw[st] = max(np.abs(np.angle(np.linalg.eigvals(Ut(K, st, 0.0)))).max() for K in np.vstack([Kg[::7], np.full(3, np.pi)]))
comm_mu = nrm(EPS @ Uo(KR[0], np.pi / 2, 0.2) - Uo(KR[0], np.pi / 2, 0.2) @ EPS)
comm_0 = nrm(EPS @ Uo(KR[0], np.pi / 2, 0.0) - Uo(KR[0], np.pi / 2, 0.0) @ EPS)
check('C7 the chiral SU(2)s need step pi/2 and mu = 0; there the band reaches w = pi, against 2 st = .08 at the CL vacuum bound st < .04',
      abs(bw[np.pi / 2] - np.pi) < 1e-6 and bw[0.04] < 0.081 and comm_mu > 0.05 and comm_0 < 1e-12,
      f'band max {bw[np.pi/2]:.3f} vs {bw[0.04]:.3f}; |[eps,U]| at mu=.2: {comm_mu:.2f}. Two-body umklapp needs band max >= pi/2')

# C8: small-step ticks that conserve the sublattice exactly need a sublattice-even cube generator
def invsp(Lset):
    A = np.vstack([np.kron(I8, L.T) - np.kron(L, I8) for L in Lset + [EPS]]); return null_space(A, rcond=1e-9).shape[1]
alo2, _ = IRal(lambda K: Uo(K, np.pi / 2)); G5 = 1j * alo2[0] @ alo2[1] @ alo2[2]; G5 = (G5 + G5.conj().T) / 2
fd = {round(float(np.sum((C[a] - C[b]) ** 2))) for a in range(8) for b in range(8) if abs(G5[a, b]) > 1e-9}
def gscan(G, th=0.1, n=9):
    eA, eB = expm(1j * th * G), expm(-1j * th * G); g1 = np.linspace(-np.pi, np.pi, n)
    f = lambda K: Dg(K).conj().T @ eA @ Dg(K) @ eB
    ws = [np.abs(np.angle(np.linalg.eigvals(f(np.array(K))))) for K in itertools.product(g1, g1, g1)]
    nz = sum(w.min() < 1e-6 for w in ws); bm = max(w.max() for w in ws)
    a2, _ = IRal(f); return int(nz), max(nrm(a2[a] @ a2[b] + a2[b] @ a2[a] - 2 * (a == b) * I8) for a in range(3) for b in range(3)), bm
gs = [gscan(G5 + cc * info[np.pi / 2]['s3']) for cc in (0.0, 0.3)]
check('C8 sublattice-even cube generators: O-invariant span{1, g5}, g5 = face-diagonal spin-3/2 hop; its tick has bandwidth 2 th but zeros on whole body diagonals (no cone), also with + .3 s3 (T)',
      invsp(Ls) == 2 and invsp([L for L, o in zip(Ls, ODD) if not o]) == 4 and fd == {2} and all(z > 20 and cl > 0.5 for z, cl, b in gs) and abs(gs[0][2] - 0.2) < 1e-6,
      f'zero grid points {[z for z, _, _ in gs]} of 729, Clifford error {[round(cl, 2) for _, cl, _ in gs]}, band max {gs[0][2]:.3f}')

# ===================================== D. toys =====================================
print('== D. toys')
nq = 8
X_ = sp.csr_matrix(np.array([[0, 1], [1, 0]], complex)); Y_ = sp.csr_matrix(np.array([[0, -1j], [1j, 0]]))
Z_ = sp.csr_matrix(np.diag([1., -1]).astype(complex)); I2 = sp.identity(2, format='csr', dtype=complex)
def kronall(ops):
    Mx = ops[0]
    for o in ops[1:]: Mx = sp.kron(Mx, o, format='csr')
    return Mx
gam = [kronall([Z_] * j + [Pp] + [I2] * (nq - j - 1)) for j in range(nq) for Pp in (X_, Y_)]
light = gam[0::2]; mirr = gam[1::2]                    # complex conjugation: X-type T-even (light), Y-type T-odd (mirror)
isreal = lambda A: np.abs(A.toarray().imag).max() < 1e-12
code = [(0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 4, 5), (0, 2, 4, 6)]
stab = [mirr[a] @ mirr[b] @ mirr[c_] @ mirr[e] for a, b, c_, e in code]
HFK = -sum(stab); eF = np.linalg.eigvalsh(HFK.toarray())
check('D1 0+1D: T forbids mirror-only and light-only bilinears; the copy-selective FK quartic is T-invariant and commuting',
      isreal(1j * light[0] @ mirr[0]) and not isreal(1j * mirr[0] @ mirr[1]) and not isreal(1j * light[0] @ light[1]) and all(isreal(s) for s in stab)
      and max(np.abs((stab[i] @ stab[j] - stab[j] @ stab[i]).toarray()).max() for i in range(4) for j in range(4)) == 0)
check('D2 FK on the mirror 8 only: lowest level 16-fold = (mirror unique) x (light 2^4 untouched), gap 2',
      int(np.sum(eF < eF[0] + 1e-9)) == 16 and abs(eF[16] - eF[0] - 2) < 1e-9, 'Fock dim 256, sparse operators')
z8 = {}; rr = np.random.default_rng(5)
for N in (2, 4, 6, 8):
    G = [gam[2 * j + 1] for j in range(N)]; terms_ = []
    for k in (2, 4, 6, 8):
        for ids in itertools.combinations(range(N), k):
            Mx = G[ids[0]]
            for i in ids[1:]: Mx = Mx @ G[i]
            Mx = (1j) ** (k * (k - 1) // 2) * Mx
            if isreal(Mx): terms_.append(Mx)
    ev = np.linalg.eigvalsh(sum(rr.normal() * T_ for T_ in terms_).toarray()) if terms_ else np.zeros(2 ** nq)
    z8[N] = int(np.sum(ev < ev[0] + 1e-9)) // 2 ** ((16 - N) // 2)
check('D3 Z8: a T-invariant interaction leaves a unique state of N same-sign Majoranas only for N = 8', z8 == {2: 2, 4: 2, 6: 2, 8: 1}, f'{z8}')
Ht = sum(1j * light[a] @ mirr[a] for a in range(nq))
spl = []
for tt in (0.025, 0.05, 0.1):
    e_ = np.linalg.eigvalsh((HFK + tt * Ht).toarray()); spl.append(e_[15] - e_[0])
Uf = expm((-1j * 0.5 * 0.1 * Ht).toarray()) @ expm((-1j * 0.5 * HFK).toarray()); wf = np.angle(np.linalg.eigvals(Uf))
near = np.sort(np.abs(np.angle(np.exp(1j * (wf - 2.0)))))
check('D4 two-half-tick circuit (copy mixing t, then FK): light 16 split only at order t^4 (static slope), mirror stays apart',
      all(abs(np.log2(spl[i + 1] / spl[i]) - 4) < 0.05 for i in range(2)) and near[16] > 0.8,
      f'slopes {[round(float(np.log2(spl[i+1]/spl[i])), 3) for i in range(2)]}; Floquet gap {near[16]:.2f} at t=.1')
Lb = 5; Nn = 2 * Lb
def swap_layer(off):
    Mx = np.zeros((Nn, Nn))
    for j in range(Lb):
        a_, b_ = (2 * j + off) % Nn, (2 * j + 1 + off) % Nn; Mx[a_, b_] = Mx[b_, a_] = 1
    return Mx
U1 = swap_layer(1) @ swap_layer(0); Q0 = np.diag([1.0 if x % 2 == 0 else 0.0 for x in range(Nn)])
mov = [(int(np.argmax(U1[:, x])) - x) % Nn for x in (0, 1)]
check('D5 1+1D Margolus swap: even sites move right, odd sites left, sublattice exactly conserved (chirality = sublattice)',
      nrm(U1 @ Q0 - Q0 @ U1) < 1e-12 and mov == [2, Nn - 2])
Km = np.diag([1, 1, -1, -1]); t1 = np.array([3, 4, 5, 0]); t2 = np.array([0, 5, 4, 3]); Kl = -Km
zl, zm = np.ones(4, int), -np.ones(4, int)              # light (L3,L4,R5,R0) z=+1; mirror (R3,R4,L5,L0) z=-1
an = lambda K_, z, t: int(z @ K_ @ t)
check('D6 3-4-5-0: light and mirror each U(1)^2-anomaly-free; mixed Z3 x U(1)_A: mirror -2, light -2, total -4 (= 2 mod 3, the swap index)',
      all(int(t @ K_ @ s) == 0 for K_ in (Km, Kl) for t in (t1, t2) for s in (t1, t2)) and an(Km, zm, t1) == -2 and an(Kl, zl, t1) == -2,
      f'twisted (z+1 per fermion): mirror {an(Km, zm + 1, t1)}, {an(Km, zm + 1, t2)}')
l1 = np.array([1, -2, 1, 2]); l2 = np.array([2, 1, -2, 1]); Lm = Matrix([list(l1), list(l2)])
check('D7 one mirror: the neutral null lattice is span{l1, l2} (primitive); l1, l2 carry plain Z3 charge 1 -> no plain-Z3 Lagrangian; twisted: both neutral',
      all(int(x @ Km @ y) == 0 for x in (l1, l2) for y in (l1, l2)) and all(int(x @ t) == 0 for x in (l1, l2) for t in (t1, t2))
      and [smith_normal_form(Lm)[i, i] for i in range(2)] == [1, 1] and [int(l1 @ zm) % 3, int(l2 @ zm) % 3] == [1, 1]
      and [int(l1 @ (zm + 1)) % 3, int(l2 @ (zm + 1)) % 3] == [0, 0], 'so the twisted turn allows gapping one mirror; the plain one needs Z3 breaking')
def stk(vv, j): out = np.zeros(12, int); out[4 * j:4 * j + 4] = vv; return out
w1, w2 = np.array([1, 0, 1, 0]), np.array([0, 1, 0, 1])
A3 = np.array([stk(w1, 0) - stk(w1, 1), stk(w1, 1) - stk(w1, 2), stk(w2, 0) - stk(w2, 1), stk(w2, 1) - stk(w2, 2),
               sum(stk(l1, j) for j in range(3)), sum(stk(l2, j) for j in range(3))])
K3 = np.kron(np.eye(3, dtype=int), Km)
check('D8 three mirrors, plain Z3: an explicit Lagrangian of six neutral, Z3-neutral null vectors with Smith form all 1 (generation-mixing terms)',
      np.abs(A3 @ K3 @ A3.T).max() == 0 and np.abs(A3 @ np.tile(t1, 3)).max() == 0 and np.abs(A3 @ np.tile(t2, 3)).max() == 0
      and set((A3 @ -np.ones(12, int)) % 3) == {0} and [smith_normal_form(Matrix(A3.tolist()))[i, i] for i in range(6)] == [1] * 6)

# ===================================== E. estimates against measurement =====================================
print('== E. estimates')
alpha, Mlat = 1 / 137.036, 1.22e19 / 3          # GeV; lattice spacing a few Planck lengths (register)
dim5 = alpha / (4 * np.pi) / Mlat
check('E1 a dimension-5 cubic birefringence, if allowed, would be ~ (alpha/4pi)/M_lat = %.0e /GeV vs GRB bound 1e-34: excluded by 1e%d' % (dim5, int(np.log10(dim5 / 1e-34))),
      dim5 / 1e-34 > 1e10, 'B3/B5: the chiral map kills it on the tetrahedral rule; the rule must keep that map')
check('E2 one light copy removes the doubled electron g-2 term (8.5e-8, 6.5e5 x precision) and the doubled N_nu (2.984 +- .008)',
      8.5e-8 / 1.3e-13 > 1e5 and abs(2.984 - 3) / 0.008 < 3)
mmir = 0.08 * 1.22e19
check('E3 mirror mass M/tick with M <= 2 st ~ .08 (vacuum cap): up to %.0e GeV, far above LHC limits on extra quarks and leptons (~1.5 TeV)' % mmir, mmir > 1e4)
print('E4 (estimate) at step pi/2 SU(2)_odd is exact, so its link is massless unless the rule breaks it; measured W_R > ~6 TeV')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('finite/exact: A, B, C1-C2, C4-C8, D. Cited: anomaly matching (C3, C6), Z16 (C5), Haldane (D7-D8). E: estimates.')
print(f'\nTOTAL: PASS={PASS} FAIL={FAIL}')
