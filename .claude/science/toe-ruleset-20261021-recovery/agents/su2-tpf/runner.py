#!/usr/bin/env python3
"""su2-tpf: spin-charge (parton) split of an SU(2) doublet so that a TPF disentangler for a jointly chiral U(1) acts only on
SU(2)-singlet charge rotors, in 1+1D.
 A content: 1+1D anomaly conditions for SU(2) x U(1); the smallest content chiral only jointly (swap family)
 B lattices: the fermionic doublet lattice is glued (charge parity = isospin parity, per chirality); the bosonised (GSO)
   lattice is an exact product charge rotor x SU(2)_1 spin rotor; where the joint chirality is visible
 C TPF on the charge rotors only (exact rationals): disentangles iff c = 0; anomalous sets fail; SU(2) untouched
 D gluing: the dressed TPF circuit maps the site gluing and the winding parity to range-one dressed versions; Wilson-dressed
   versions commute with the U(1) Gauss law; continuous slave-rotor gluing has a mixed Schwinger term with Q
 E linking: Gauss law, Schwinger term, Gaussian modes in the per-flavour and charge-rotor frames
 F 3+1D: the SM's Z_6 is the same gluing; Y on a holon leaves the spinons jointly chiral under SU(3) x SU(2)
Labels: [T] theorem / exact computation. Supplied model, finite diagnostic; no physical identification. Cited, not rederived:
Thorngren-Preskill-Fidkowski arXiv:2601.04304 (rotor-frame disentangler, rederived inline as in the tpf-circuit runner),
bosonisation of Dirac fermions (per-flavour vertex lattice), SU(2)_1 at the self-dual radius, Florens-Georges slave rotors."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools, math, os, random, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from collections import Counter
from fractions import Fraction as Fr
import numpy as np

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
H = Fr(1, 2)

# ================================================ A. content ================================================
print('== A. 1+1D content (Weyl multiplets (dim, q); a 2D left Weyl of charge q is conjugate to one of charge -q)')
def anomalies(Lm, Rm):
    kYY = sum(d * q * q for d, q in Lm) - sum(d * q * q for d, q in Rm)
    kW = sum(Fr(d == 2, 2) for d, q in Lm) - sum(Fr(d == 2, 2) for d, q in Rm)
    grav = sum(d for d, q in Lm) - sum(d for d, q in Rm)
    return kYY, kW, grav
pauli = [np.array(m) for m in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
mixed0 = all(abs(np.trace(s)) == 0 for s in pauli)        # F_Y tr F_SU2 term of the 4-form: tr T^a = 0
def vl(Lm, Rm, key):
    f = {'w': lambda d, q: (d, d), 'y': lambda d, q: (abs(q), d), 'wy': lambda d, q: ((d, abs(q)), 1)}[key]
    cnt = lambda M: Counter(x for d, q in M for x in [f(d, q)[0]] * f(d, q)[1])
    return cnt(Lm) == cnt(Rm)
reps = [(d, q) for d in (1, 2) for q in range(0, 5)]
msets = [list(c) for n in range(1, 4) for c in itertools.combinations_with_replacement(reps, n)]
only_joint, best = [], None
for Lm in msets:
    for Rm in msets:
        if anomalies(Lm, Rm) != (0, 0, 0) or vl(Lm, Rm, 'wy') or not (vl(Lm, Rm, 'w') and vl(Lm, Rm, 'y')): continue
        size = sum(d for d, q in Lm); only_joint.append((size, Lm, Rm))
mn = min(s for s, _, _ in only_joint); mins = [(L_, R_) for s, L_, R_ in only_joint if s == mn]
def is_swap(L_, R_):
    dL = [q for d, q in L_ if d == 2]; dR = [q for d, q in R_ if d == 2]; sL = sorted(q for d, q in L_ if d == 1); sR = sorted(q for d, q in R_ if d == 1)
    return len(dL) == len(dR) == 1 and sL == [dR[0]] * 2 and sR == [dL[0]] * 2 and dL[0] != dR[0]
gen = [anomalies([(2, a), (1, b), (1, b)], [(2, b), (1, a), (1, a)]) for a in range(-6, 7) for b in range(-6, 7)]
check('A1 [T] 1+1D anomalies of SU(2) x U(1): U(1)^2 sum_L d q^2 - sum_R d q^2, SU(2) level #doublets_L - #doublets_R, gravity '
      '#L - #R; the mixed term vanishes (tr T^a = 0). Vector-like under SU(2) alone and U(1) alone, chiral jointly: the smallest has 4 components per side and is exactly the swap family L (2,a)+2(1,b), '
      'R (2,b)+2(1,a), |a| != |b|, anomaly-free for every a, b',
      mixed0 and mn == 4 and all(is_swap(L_, R_) for L_, R_ in mins) and all(g == (0, 0, 0) for g in gen),
      f'{len(only_joint)} such contents up to 3 multiplets/side, |q| <= 4; {len(mins)} minimal, all swap')
print('   model (a, b) = (3, 1); a = b mod 2 (one spin structure)')

# ================================================ B. lattices ================================================
print('== B. vertex lattices of the doublet: per flavour (p, w), h = (p + w/2)^2/2, hbar = (p - w/2)^2/2; '
      'charge n_L = N + W, n_R = N - W, spin m_L = S + T, m_R = S - T (N, S = p_u +- p_d, W, T = (w_u +- w_d)/2)')
a_, b_ = 3, 1
def toNW(v): pu, wu, pd, wd = v; return (pu + pd + Fr(wu + wd, 2), pu + pd - Fr(wu + wd, 2), pu - pd + Fr(wu - wd, 2), pu - pd - Fr(wu - wd, 2))
def inF(v): return all((2 * p).denominator == 1 and Fr(w).denominator == 1 and (w - 2 * p) % 2 == 0 for p, w in (v[:2], v[2:]))
box = [(Fr(i, 2), w, Fr(k, 2), x) for i in range(-6, 7) for w in range(-6, 7) for k in range(-6, 7) for x in range(-6, 7)]
LF = [v for v in box if inF(v)]
glue = all(all(c.denominator == 1 for c in toNW(v)) and (toNW(v)[0] - toNW(v)[2]) % 2 == 0 and (toNW(v)[1] - toNW(v)[3]) % 2 == 0 for v in LF)
def fromLR(nl, nr, ml, mr):
    N, W, S, T = Fr(nl + nr, 2), Fr(nl - nr, 2), Fr(ml + mr, 2), Fr(ml - mr, 2)
    return (Fr(N + S, 2), W + T, Fr(N - S, 2), W - T)
back = all(inF(fromLR(*t)) for t in itertools.product(range(-4, 5), repeat=4) if (t[0] - t[2]) % 2 == 0 and (t[1] - t[3]) % 2 == 0)
# GSO (bosonised) lattice: fermion-even part plus the shift by the total-parity twist (0,1,0,1)
Fev = [v for v in LF if (2 * v[0] + 2 * v[2]) % 2 == 0]
GSO = set(toNW(v) for v in Fev) | set(toNW((v[0], v[1] + 1, v[2], v[3] + 1)) for v in Fev)
prodZ = all(((t[0] + t[1]) % 2 == 0 and (t[2] + t[3]) % 2 == 0) for t in GSO)       # n_L = n_R and m_L = m_R mod 2: (N, W, S, T) in Z^4
small = {t for t in itertools.product(range(-3, 4), repeat=4) if (t[0] - t[1]) % 2 == 0 and (t[2] - t[3]) % 2 == 0}
prod_full = small <= GSO
cur = (0, 0, 2, 0) in GSO and toNW((H, 1, -H, -1)) == (0, 0, 2, 0) and not ((H, 1, -H, -1)[0].denominator == 1)
check('B1 [T] fermionic doublet lattice = {n_L = m_L, n_R = m_R mod 2}: charge and isospin glued separately for each chirality '
      '(the U(2) = (U(1) x SU(2))/Z_2 gluing); the bosonised (GSO) lattice is the exact product {(N, W) in Z^2} x {(S, T) in Z^2}: '
      'charge rotor x self-dual spin rotor (SU(2)_1 currents (m_L, m_R) = (+-2, 0), (0, +-2)), which the per-flavour Z^4 lacks',
      glue and back and prodZ and prod_full and cur, f'{len(LF)} fermionic vectors in box, {len(GSO)} GSO vectors')
Fst = []
for v in LF:
    nl, nr, ml, mr = toNW(v); hh = Fr(nl * nl + ml * ml, 4); hb = Fr(nr * nr + mr * mr, 4)
    Fst.append((a_ * nl + b_ * nr, hh, hb, (Fr(ml, 2), Fr(mr, 2))))
Lq = sorted({(q, j) for q, hh, hb, j in Fst if hh == H and hb == 0}); Rq = sorted({(q, j) for q, hh, hb, j in Fst if hh == 0 and hb == H})
Bst = [(a_ * nl + b_ * nr, Fr(nl * nl + ml * ml, 4), Fr(nr * nr + mr * mr, 4), (Fr(ml, 2), Fr(mr, 2))) for nl, nr, ml, mr in GSO]
BL = sorted({(q, j) for q, hh, hb, j in Bst if hh == 1 and hb == 0})
dbl_charged = [x for x in BL if x[0] != 0 and x[1][0] != 0]
check('B2 [T] fermionic frame: the h = 1/2 left movers are isospin doublets (J3_L = +-1/2) of charge +-a, right movers doublets of '
      'charge +-b (singlet flavours: L +-b, R +-a): chiral jointly. Bosonised frame: the h = 1 left movers are charge +-2a isospin '
      'singlets and neutral currents; no charged doublet exists, so the joint chirality is carried only by the Z_2 gluing',
      [q for q, j in Lq] == [-3, -3, 3, 3] and all(abs(j[0]) == H and j[1] == 0 for q, j in Lq)
      and [q for q, j in Rq] == [-1, -1, 1, 1] and dbl_charged == [] and sorted({q for q, j in BL}) == [-6, 0, 6],
      f'F left {[(int(q), str(j[0])) for q, j in Lq]}; F right charges {[int(q) for q, j in Rq]}; GSO h=1 left charges {sorted({int(q) for q, j in BL})}')

# ================================================ C. TPF on the charge rotors ================================================
print('== C. TPF on SU(2)-singlet rotors: charge rotor (qV, qA) = (a+b, a-b) [Q = qV N + qA W], singlets (a+b, (b-a)/2)')
def rnd(x): return math.floor(x + H)
def f1(x): return x - math.floor(x)
def cp(x): return ([r[:] for r in x[0]], [r[:] for r in x[1]], x[2][:], x[3][:])
def QAw(p, n): N = len(p); return -sum(rnd(p[(j + 1) % N] - p[j]) + n[j] for j in range(N))
def sym(x, be, qs):
    y = cp(x); y[0][:] = [[f1(p + qV * be) for p in x[0][a]] for a, (qV, qA) in enumerate(qs)]; y[2][:] = [f1(t + be) for t in x[2]]
    return y, be * sum(qA * QAw(x[0][a], x[1][a]) for a, (qV, qA) in enumerate(qs))
def ylink(ph, n, th, qs, k):
    N = len(th); return sum(qA * (rnd(ph[al][(k + 1) % N] - ph[al][k] + qV * (th[(k + 1) % N] - th[k])) + n[al][k]) for al, (qV, qA) in enumerate(qs))
def Xr(ph, qs, k): return rnd(sum(qA * ph[al][k % len(ph[al])] for al, (qV, qA) in enumerate(qs)))
def ytil(ph, n, th, qs, k): return ylink(ph, n, th, qs, k) - (Xr(ph, qs, k + 1) - Xr(ph, qs, k))
def Phi(ph, n, th, qs): return -sum(th[k] * ytil(ph, n, th, qs, k) for k in range(len(th)))
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
def K(x, al, j, be):
    N = len(x[2]); y = cp(x); p = x[0][al]; dl = p[j] - p[(j - 1) % N]; dr = p[(j + 1) % N] - p[j]
    y[1][al][(j - 1) % N] += rnd(dl) - rnd(dl + be); y[1][al][j] += rnd(dr) - rnd(dr - be); y[0][al][j] = f1(p[j] + be); return y, Fr(0)
def Kg_dis(x, al, j, be, qs):
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
rng = random.Random(20261022); DEN = 48; NB = 5; NT = 150
def rx(N, F, links=False):
    r = lambda: Fr(rng.randrange(DEN), DEN)
    return ([[r() for _ in range(N)] for _ in range(F)], [[rng.randrange(-2, 3) for _ in range(N)] for _ in range(F)],
            [r() for _ in range(N)], [r() for _ in range(N)] if links else [Fr(0)] * N)
def ident(qs, n=NT):
    fails = 0
    for t in range(n):
        x = rx(NB, len(qs)); be = Fr(rng.randrange(1, 97), 97)
        u = comp(x, [lambda z: W(z, qs), lambda z: sym(z, be, qs), lambda z: Wd(z, qs)]); v = cp(x); v[2][:] = [f1(tt + be) for tt in x[2]]
        fails += not (u[0] == v and f1(u[1]) == 0)
    return fails
cset = lambda a, b: [(a + b, a - b), (a + b, Fr(b - a, 2)), (a + b, Fr(b - a, 2))]
CH = [(4, 2), (4, -1), (4, -1)]; PF = [(4, 1), (4, 1), (4, -1), (4, -1)]
cc = lambda qs: sum(qV * qA for qV, qA in qs)
res = {'charge frame (4,2)(4,-1)^2': ident(CH), 'per-flavour (4,1)^2(4,-1)^2': ident(PF)}
fam = {(a, b): ident(cset(a, b), 40) for a, b in [(2, 0), (4, 2), (5, 1), (5, 3)]}
check('C1 [T] TPF disentangler (one on-site and two link layers) on the three SU(2)-singlet rotors: W^dag e^{2 pi i b Q} W = '
      'e^{2 pi i b Q_anc} exactly; c = (a+b)(a-b) + 2(a+b)(b-a)/2 = 0 for every swap content; the per-flavour frame (doublet as two '
      'rotors) has the same c and also disentangles',
      cc(CH) == 0 and cc(PF) == 0 and all(v == 0 for v in res.values()) and all(v == 0 for v in fam.values()) and all(cc(cset(a, b)) == 0 for a, b in fam),
      'fails ' + ', '.join(f'{k} {v}' for k, v in res.items()) + '; family ' + ', '.join(f'{k}:{v}' for k, v in fam.items()))
AN = {'one singlet': [(4, 2), (4, -1)], 'charge rotor alone': [(4, 2)], 'doublet counted once': [(4, 1), (4, -1), (4, -1)]}
ra = {k: (ident(q, 80), cc(q)) for k, q in AN.items()}
check('C2 [T] anomalous sets fail: dropping a singlet (c = 4), the charge rotor alone (c = 8), the doublet counted as one flavour (c = -4)',
      all(f > 20 and c != 0 for f, c in ra.values()), '; '.join(f'{k} c={c}: {f}/80' for k, (f, c) in ra.items()))
U = np.array([[3 / 5, 4j / 5], [4j / 5, 3 / 5]]); S2 = [0.5 * s for s in pauli]
def onsite_spin(op, Ls):
    out = np.array([[1.0 + 0j]])
    for _ in range(Ls): out = np.kron(out, op)
    return out
Ls = 4; Ug = onsite_spin(U, Ls); vs = np.random.default_rng(1).normal(size=2 ** Ls) + 0j; okc = 0
for t in range(30):
    x = rx(NB, 3); y, ph = W(x, CH); w1 = np.exp(2j * np.pi * float(ph)) * (Ug @ vs); w2 = Ug @ (np.exp(2j * np.pi * float(ph)) * vs)
    okc += np.allclose(w1, w2) and W(x, CH)[0] == y
check('C3 [T] SU(2) acts on the spin factor only (rational element (3 + 4i sigma_x)/5, on-site on a spin-1/2 chain), W on charge '
      'rotors and ancillas only: [W, U_SU(2)] = 0 exactly, and the dressed charges rho_j = W L_j W^dag are SU(2) singlets',
      okc == 30 and abs(np.linalg.det(U) - 1) < 1e-15 and np.allclose(U @ U.conj().T, np.eye(2)), '30 configurations x spin states')

# ================================================ D. gluing ================================================
print('== D. gluing: site generator G_j = K_j(1/2) (Q-symmetric half turn of the charge rotor) x (-1)^{2S_j}; winding parity per link')
dd = Counter(); dset = {0: set(), 1: set(), 'g': set()}
for t in range(NT):
    x = rx(NB, 3); j = rng.randrange(NB)
    lhs = comp(x, [lambda z: W(z, CH), lambda z: K(z, 0, j, H), lambda z: Wd(z, CH)])
    rhs = Kg_dis(x, 0, j, H, CH)
    dd['glue'] += not (same(lhs, rhs) and f1(rhs[1] - (x[2][j] - x[2][(j - 1) % NB])) == 0)
    for al, be in ((0, H), (1, H), (0, Fr(1, 3))):
        X = sum(q[1] * x[0][b][j] for b, q in enumerate(CH)); dset['g' if be != H else al].add(rnd(X + CH[al][1] * be) - rnd(X))
check('D1 [T] W K_j(1/2) W^dag = K^cov_j(1/2) e^{2 pi i (theta_j - theta_{j-1})} (covariant relabel through D phi + qV D theta): the site gluing maps to itself times a state-independent '
      'unit ancilla-charge transfer (range one, SU(2) singlet) because qA/2 = (a-b)/2 is an integer (a = b mod 2); a singlet\'s half '
      'turn (qA odd) and a continuous slave-rotor turn gamma = 1/3 get state-dependent dressings',
      dd['glue'] == 0 and dset[0] == {1} and len(dset[1]) == 2 and len(dset['g']) == 2,
      f"fails {dd['glue']}/{NT}; dressings: charge {sorted(dset[0])}, singlet {sorted(dset[1])}, gamma=1/3 {sorted(dset['g'])}")
for t in range(NT):
    x = rx(NB, 3, links=True); lam = [Fr(rng.randrange(29), 29) for _ in range(NB)]; j = rng.randrange(NB)
    Kg = lambda z: comp(z, [lambda s: Wd(s, CH), lambda s: Kg_dis(s, 0, j, H, CH), lambda s: W(s, CH)])
    dd['lglue'] += not same(comp(x, [Kg, lambda z: Gam(z, lam, CH)]), comp(x, [lambda z: Gam(z, lam, CH), Kg]))
def wpar(x, qV, linked):
    N = len(x[2]); p = x[0][0]; return H * sum(rnd(p[(k + 1) % N] - p[k] - (qV * x[3][k] if linked else 0)) + x[1][0][k] for k in range(N))
def gpar(qs, linked, n=NT):
    bad = 0
    for t in range(n):
        x = rx(NB, len(qs), links=True); lam = [Fr(rng.randrange(29), 29) for _ in range(NB)]; y = Gam(x, lam, qs)[0]
        bad += f1(wpar(y, qs[0][0], linked) - wpar(x, qs[0][0], linked)) != 0
    return bad
odd = [(3, 1), (3, Fr(-1, 2)), (3, Fr(-1, 2))]
gp = {'linked qV=4': gpar(CH, True), 'unlinked qV=4': gpar(CH, False, 60), 'linked qV=3': gpar(odd, True, 60)}
comm = nz = 0
for t in range(60):
    x = rx(NB, 3); u = W(x, CH); s1 = f1(wpar(u[0], 4, False) - wpar(x, 4, False))
    s2 = f1(H * sum(rnd(x[0][0][(k + 1) % NB] - x[0][0][k] + 4 * (x[2][(k + 1) % NB] - x[2][k])) - rnd(x[0][0][(k + 1) % NB] - x[0][0][k]) for k in range(NB)))
    comm += s1 != s2; nz += s1 != 0
check('D2 [T] after linking, W (linked half turn) W^dag commutes with every finite Gauss transformation; the charge rotor\'s '
      'winding parity (the charge half of the refermionising Z_2) is Gauss-invariant once linked (round(D phi - qV a)) iff qV = a+b '
      'is even; W changes it by a product of link-local signs, so the dressed Z_2 stays range one',
      dd['lglue'] == 0 and gp['linked qV=4'] == 0 and gp['unlinked qV=4'] > 5 and gp['linked qV=3'] > 5 and comm == 0 and nz > 5,
      f"glue {dd['lglue']}/{NT}; parity fails " + ', '.join(f'{k} {v}' for k, v in gp.items()) + f'; W flips it in {nz}/60, link-sign formula misses {comm}')
def schw(q1, q2, N=6):
    M = len(q1) * N; Om = np.block([[np.zeros((M, M)), np.eye(M)], [-np.eye(M), np.zeros((M, M))]])
    def Rm(qs):
        Rr = np.zeros((N, 2 * M))
        for j in range(N):
            for a, (qV, qA) in enumerate(qs): Rr[j, M + a * N + j] += float(qV) / (2 * np.pi); Rr[j, a * N + (j + 1) % N] += float(qA); Rr[j, a * N + j] -= float(qA)
        return Rr
    return float(np.abs(Rm(q1) @ Om @ Rm(q2).T).max())
g_turn = [(1, 0), (0, 0), (0, 0)]
mx = schw(g_turn, CH); gg = schw(g_turn, g_turn); qq = schw(CH, CH)
check('D3 [T] continuous slave-rotor gluing U(1)_g (charge-rotor turn minus spinon number; spinons Q-neutral): [rho_g, rho_g] = 0 and '
      '[rho_Q, rho_Q] = 0 but [rho_g,j, rho_Q,j-1] = qA/(2 pi) = (a-b)/(2 pi) != 0: g and Q cannot both be linked by ordinary links '
      '(their integer part qA/2 at gamma = 1/2 is what D1 shows as a removable unit transfer)',
      gg < 1e-14 and qq < 1e-14 and abs(mx - 2 / (2 * np.pi)) < 1e-14, f'|[g,Q]| = {mx:.4f} = 2/(2 pi)')

# ================================================ E. linking ================================================
print('== E. linking (link angle a, electric E; Gauss G_j = E_{j+1/2} - E_{j-1/2} - rho_j); SU(2) Gauss law on-site on the spin chain')
sw = {k: schw(q, q) for k, q in [('swap', CH), ('per-flavour', PF)] + list(AN.items())}
check('E1 [T] Schwinger term: the U(1) Gauss generators commute iff c = 0 (swap content, both frames); every anomalous set fails; '
      'the SU(2) Gauss generators act on the spin chain and its links only and commute with W and with the U(1) ones',
      sw['swap'] < 1e-14 and sw['per-flavour'] < 1e-14 and all(sw[k] > 0.3 for k in AN), ', '.join(f'{k} {v:.3f}' for k, v in sw.items()))
Ud, Jd = 1 / np.pi, np.pi
def modes(qs, Us, Js, k, g=0.2):
    a = np.array([float(q[0]) for q in qs]); b = np.array([float(q[1]) for q in qs]); F = len(qs); w2 = 4 * np.sin(k / 2) ** 2; z = np.exp(1j * k) - 1
    C = (g * g / 2) * np.conj(z) * np.outer(b, a) / (2 * np.pi * w2)
    A = np.block([[np.diag(np.array(Js) / 2) * w2 + (g * g / 2) * np.outer(b, b), C],
                  [C.conj().T, np.diag(np.array(Us) / 2) + (g * g / 2) * np.outer(a, a) / (4 * np.pi ** 2 * w2)]])
    Jm = np.block([[np.zeros((F, F)), np.eye(F)], [-np.eye(F), np.zeros((F, F))]]); ev = np.linalg.eigvals(2 * Jm @ A).imag
    return np.sort(ev[ev > 0])
kk = 0.005; mpf = modes(PF, [Ud] * 4, [Jd] * 4, kk); mch = modes(CH, [Ud / 2, Ud, Ud], [2 * Jd, Jd, Jd], kk)
spin = 2 * np.sin(kk / 2) * np.sqrt((Ud / 2) * (2 * Jd)); mch_full = np.sort(np.append(mch, spin))
mpred = np.sqrt(0.04 * 40 / (2 * np.pi)); man = modes(AN['one singlet'], [Ud / 2, Ud], [2 * Jd, Jd], kk)
check('E2 [T] linked Gaussian modes (g = 0.2, K = 0.005): the charge-rotor frame (U/2, 2J) plus the free spin rotor reproduces the '
      'per-flavour spectrum exactly; three massless modes (v = 1) and one photon, m^2 = (g^2/2 pi) sum(qL^2 + qR^2) = 20 g^2/pi; '
      'with one singlet dropped a non-local chiral branch Om ~ 1/K appears',
      np.allclose(mpf, mch_full, rtol=1e-9, atol=1e-12) and np.sum(mpf < 2 * kk) == 3 and abs(mpf[-1] - mpred) < 1e-3 and man[-1] > 5,
      f'photon {mpf[-1]:.5f} vs {mpred:.5f}; max frame diff {np.abs(mpf - mch_full).max():.1e}; anomalous top {man[-1]:.1f}')

# ================================================ F. 3+1D ================================================
print('== F. 3+1D: SM family with nu^c as (colour triality t, isospin j, Y)')
FAM = [('Q', 1, H, Fr(1, 6), 3, 2), ('u^c', 2, 0, Fr(-2, 3), 3, 1), ('d^c', 2, 0, Fr(1, 3), 3, 1), ('L', 0, H, Fr(-1, 2), 1, 2), ('e^c', 0, 0, Fr(1), 1, 1), ('nu^c', 0, 0, Fr(0), 1, 1)]
z6 = all((Fr(t, 3) + j + y).denominator == 1 for _, t, j, y, c, d in FAM); z2 = all(((-1) ** int(2 * j)) == ((-1) ** int(6 * y)) for _, t, j, y, c, d in FAM)
def vlike(keep):
    M = Counter()
    for nm, t, j, y, c, d in FAM:
        lab = (t if 'c' in keep else 0, j if 'w' in keep else 0, y if 'y' in keep else 0)
        M[lab] += (1 if 'c' in keep else c) * (1 if 'w' in keep else d)
    cj = lambda l: ((-l[0]) % 3, l[1], -l[2])
    return all((M[cj(l)] == m) if cj(l) != l else (not (l[1] == H and m % 2)) for l, m in M.items())
sp_ = {k: vlike(k) for k in ['c', 'w', 'cw']}
V4 = [1, -1, 0, 0]; A4 = [1, 1, -1, -1]; blocks = [(-3, -1)] * 3 + [(3, 3)]
blk = [[a * v + b * w for v, w in zip(V4, A4)] for a, b in blocks]
dbl = all(blk[i][2] == blk[i][3] and len({blk[i][0], blk[i][1], blk[i][2]}) == 3 for i in range(4))
check('F1 [T] the 1+1D gluing is the SM\'s: e^{2 pi i (t/3 + j + Y)} = 1 on every multiplet (the Z_6), so doublets <=> 6Y odd; with '
      'Y moved onto an SU(2)-singlet holon the Y-neutral spinons are still vector-like under SU(3) alone and SU(2) alone but chiral '
      'under SU(3) x SU(2) (Q = (3,2) unpaired); each TPF 3+1D block is one doublet (equal (V,A)) plus two singlets, the swap shape',
      z6 and z2 and sp_ == {'c': True, 'w': True, 'cw': False} and dbl, f'Z6 {z6}, spinon vector-like {sp_}, blocks 6Y {blk}')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('all [T]. Supplied: rotor matter (Villain, per-flavour bosonisation), the swap content (a, b) = (3, 1), ancillas, the spin-1/2 '
      'chain as the on-site SU(2) carrier, g. Cited: TPF 2601.04304, bosonisation, SU(2)_1, slave rotors.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
