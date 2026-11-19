#!/usr/bin/env python3
"""link-selection: which CL-3 link-selection rule removes the species-number and B-L links?

Supplied-model, finite diagnostics and exact linear algebra; no physical identification beyond the
labels stated.  Candidates:
 (a) links only on charges anomaly-free on the light content;
 (b) links only on non-abelian symmetries, or on charges acting on more than one species;
 (c) links only on symmetries of every term of the update (CL-3 as written);
 (d) one dressed unit per link group.
A. measured bounds (estimates).  B. CL-1's vector-like content with species in parallel.
C. chiral SM content, three families, cumulative term sets.  D. Pati-Salam route: stabiliser of a
nu^c-number-changing term.  E. estimates against measurement.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, signal, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.linalg import expm

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

rng = np.random.default_rng(11)

# ============ A. measured bounds (estimates) ============
print('== A. MICROSCOPE (Ti vs Pt) on a massless link of coupling g to charge X')
G, u, hbar, c = 6.67430e-11, 1.66053906660e-27, 1.054571817e-34, 2.99792458e8
aG = G * u * u / (hbar * c)
iso = {'Ti': (22, 48, 47.948), 'Al': (13, 27, 26.982), 'V': (23, 51, 50.944), 'Pt': (78, 195, 194.965),
       'Rh': (45, 103, 102.906), 'Fe': (26, 56, 55.935), 'O': (8, 16, 15.995), 'Si': (14, 28, 27.977),
       'Mg': (12, 24, 23.985), 'S': (16, 32, 31.972), 'Ni': (28, 58, 57.935), 'Ca': (20, 40, 39.963)}
def per_mass(mix, X):
    tot = sum(mix.values())
    return sum(w / iso[e][2] * X(*iso[e][:2]) for e, w in mix.items()) / tot
TA6V = {'Ti': .90, 'Al': .06, 'V': .04}; PtRh = {'Pt': .90, 'Rh': .10}
Earth = {'Fe': .32, 'O': .30, 'Si': .15, 'Mg': .14, 'S': .03, 'Ni': .018, 'Ca': .015, 'Al': .014}
eta_max = 1.5e-15 + 2.7e-15      # MICROSCOPE 2022 final: (-1.5 +- 2.7) e-15
charges = {'B=A': lambda Z, A: A, 'L=Z': lambda Z, A: Z, 'B-L': lambda Z, A: A - Z,
           'N_u=A+Z': lambda Z, A: A + Z, 'N_d=2A-Z': lambda Z, A: 2 * A - Z}
gb = {}
for k, X in charges.items():
    xE = per_mass(Earth, X); dx = abs(per_mass(TA6V, X) - per_mass(PtRh, X))
    gb[k] = np.sqrt(4 * np.pi * aG * eta_max / (xE * dx))
print('   g_max: ' + ', '.join(f'{k} {v:.1e}' for k, v in gb.items()))
check('[E] every species number, B, L and B-L needs g < 1e-23 as a massless link (e = 0.30)',
      max(gb.values()) < 1e-23 and gb['B-L'] < 2e-24, f"B-L {gb['B-L']:.1e}")

# ============ B. CL-1 vector-like content, species in parallel ============
print('== B. vector-like species in parallel (CL-1 as written)')
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
def tick(K, E, M):
    n = np.array([np.sin(K[0]), np.sin(K[1]), np.sin(K[2]) + 0.3 * np.cos(K[0])]); n /= np.linalg.norm(n)
    R = n[0] * sx + n[1] * sy + n[2] * sz                     # a reflection, R^2 = 1
    return expm(-1j * np.kron(E - M / 2, R)) @ expm(1j * np.kron(E + M / 2, R))
def species_commutant(E, M, nK=5):
    ns = M.shape[0]; rows = []
    basis = [np.kron(np.eye(ns)[:, [i]] @ np.eye(ns)[[j], :], np.eye(2)) for i in range(ns) for j in range(ns)]
    for _ in range(nK):
        U = tick(rng.uniform(-np.pi, np.pi, 3), E, M)
        rows.append(np.array([(U @ b - b @ U).ravel() for b in basis]).T)
    A = np.vstack(rows)
    return ns * ns - np.linalg.matrix_rank(A, tol=1e-9)
def herm_with(eigs):
    Q, _ = np.linalg.qr(rng.normal(size=(len(eigs),) * 2) + 1j * rng.normal(size=(len(eigs),) * 2))
    return Q @ np.diag(eigs) @ Q.conj().T
res = {}
res['4 distinct'] = species_commutant(np.diag([.04, .041, .042, .043]), np.diag([.001, .002, .003, .004]).astype(complex))
res['4 mixed'] = species_commutant(0.04 * np.eye(4), herm_with([.001, .002, .003, .004]))
eig8 = [.003] * 3 + [.005] * 3 + [.001, .002]
res['(3,3,1,1)'] = species_commutant(0.04 * np.eye(8), herm_with(eig8))
check('[T] any quadratic species-parallel tick: on-site commutant = commutant of the mass matrix; dims = sum of '
      'multiplicities^2, so >= one exact U(1) per distinct mass, whatever mixing the mass matrix holds',
      res == {'4 distinct': 4, '4 mixed': 4, '(3,3,1,1)': 20}, str(res))
fam = 3 * (9 + 9 + 1 + 1)
print(f'   one family u(3)+u(3)+u(1)+u(1) = 20 generators, 4 abelian; three families {fam}, 12 abelian, no su(2)')
# (a) on vector-like content: L and R of each species carry the same X and link charge
Xs, qs = rng.normal(size=8), rng.normal(size=8)
w = sum(Xs * qs ** 2) - sum(Xs * qs ** 2)
check('[T] (a) is void on vector-like content: every on-site U(1) has anomaly weight sum chi X q^2 = 0', w == 0)
# (b) multi-species charges span everything
n = 4; multi = [v for v in itertools.product([-1, 0, 1], repeat=n) if sum(x != 0 for x in v) >= 2]
check('[T] (b, "acts on >1 species") is not a selection: its charges span all n species numbers (n = 4), '
      'and links must be valued in a Lie algebra', np.linalg.matrix_rank(np.array(multi, float)) == n)
check('[T] (b, non-abelian only) on (3,3,1,1): derived algebra su(3)+su(3) = 16, centre 4: no abelian link, so no photon',
      res['(3,3,1,1)'] - 4 == 16)

# ============ C. chiral SM content, 3 families ============
print('== C. chiral SM 16 x 3, SU(3) x SU(2) linked; exact U(1)s after each term set')
FLD = [('Q', 3, 2, Fr(1, 6)), ('u', 3, 1, Fr(-2, 3)), ('d', 3, 1, Fr(1, 3)), ('L', 1, 2, Fr(-1, 2)), ('e', 1, 1, Fr(1)), ('n', 1, 1, Fr(0))]
V = {(f, g): sp.Symbol(f'{f}{g}') for g in range(3) for f, *_ in FLD}; h = sp.Symbol('h')
allv = list(V.values()) + [h]; allv_noh = list(V.values())
yuk = [V['Q', i] + V['u', j] + h for i in range(3) for j in range(3)] + \
      [V['Q', i] + V['d', j] - h for i in range(3) for j in range(3)] + \
      [V['L', i] + V['e', j] - h for i in range(3) for j in range(3)] + \
      [V['L', i] + V['n', j] + h for i in range(3) for j in range(3)]
dB = [V['u', i] + V['d', j] + V['d', k] + V['n', l] for i, j, k, l in itertools.product(range(3), repeat=4)]   # uddn class
nc4 = [V['n', i] + V['n', j] + V['n', k] + V['n', l] for i, j, k, l in itertools.product(range(3), repeat=4)]  # (nu^c)^4
nc2 = [V['n', i] + V['n', j] for i in range(3) for j in range(3)]                                              # nu^c nu^c
def ns_of(eqs, vars_=allv):
    if not eqs: return [sp.Matrix([1 if v == x else 0 for v in vars_]) for x in vars_]
    A = sp.Matrix([[sp.diff(e, v) for v in vars_] for e in eqs]); return A.nullspace()
def todict(vec, vars_=allv): return {k: Fr(str(vec[vars_.index(V[k])])) for k in V}
def tri(a, b, c_):
    return sum(nc * nw * a[f, g] * b[f, g] * c_[f, g] for g in range(3) for f, nc, nw, _ in FLD)
def lin(x):  # SU3^2 X, SU2^2 X, grav X
    s3 = sum(Fr(1, 2) * nw * x[f, g] for g in range(3) for f, nc, nw, _ in FLD if nc == 3)
    s2 = sum(Fr(1, 2) * nc * x[f, g] for g in range(3) for f, nc, nw, _ in FLD if nw == 2)
    gr = sum(nc * nw * x[f, g] for g in range(3) for f, nc, nw, _ in FLD)
    return s3, s2, gr
Y = {(f, g): yv for g in range(3) for f, _, _, yv in FLD}
def anomaly_free_dim(basis):
    """largest subspace of span(basis) containing Y on which all linear and mixed cubic anomalies vanish:
    impose the linear ones and Y^2 X; then check the remaining cubic forms vanish identically."""
    a = sp.symbols(f'a0:{len(basis)}')
    x = {k: sum(ai * sp.Rational(b[k].numerator, b[k].denominator) for ai, b in zip(a, basis)) for k in V}
    Ys = {k: sp.Rational(Y[k].numerator, Y[k].denominator) for k in V}
    eqs = list(lin(x)) + [sum(nc * nw * Ys[f, g] ** 2 * x[f, g] for g in range(3) for f, nc, nw, _ in FLD)]
    eqs = [sp.expand(e) for e in eqs if sp.expand(e) != 0]
    sol = sp.linsolve(eqs, a) if eqs else None
    gen = [x[k] for k in V]
    if sol:
        s = list(sol)[0]; gen = [sp.expand(gk.subs(dict(zip(a, s)))) for gk in gen]
    free = sorted(set().union(*[gk.free_symbols for gk in gen]), key=str)
    B_ = [{k: Fr(str(sp.expand(gk).coeff(fs))) for k, gk in zip(V, gen)} for fs in free]
    cub = {tri(p, q, r) for p in B_ for q in B_ for r in B_} | {tri(Y, p, q) for p in B_ for q in B_}
    return len(B_), cub == {0}, B_
sets = [('T0 links only', []), ('T1 +Yukawa-type, generic', yuk), ('T2 T1 + uddn class', yuk + dB),
        ('T3 T2 + (nu^c)^4', yuk + dB + nc4), ("T3' T1 + (nu^c)^4", yuk + nc4), ("T3'' T1 + nu^c nu^c", yuk + nc2),
        ('T4 no Yukawa, uddn + (nu^c)^4', dB + nc4)]
out = {}
for lab, eqs in sets:
    vv = allv_noh if lab.startswith('T4') else allv
    ns = ns_of(eqs, vv); ds = [todict(v, vv) for v in ns]
    if lab.startswith('T0'):
        out[lab] = (18, None); print(f'   {lab}: exact U(1)s 18 (u(3)^6 flavour, 54 generators)'); continue
    dA, okc, BA = anomaly_free_dim(ds)
    out[lab] = (len(ns), dA, okc, BA, ds)
    tag = f'with (a) {dA}' if okc else f'linear anomalies leave {dA}, cubics not identically 0'
    print(f'   {lab}: exact U(1)s {len(ns)}; {tag}')
B_ = {(f, g): v for g in range(3) for f, v in zip('QudLen', (Fr(1, 3), Fr(-1, 3), Fr(-1, 3), 0, 0, 0))}
L_ = {(f, g): Fr(v) for g in range(3) for f, v in zip('QudLen', (0, 0, 0, 1, -1, -1))}
BmL = {k: B_[k] - L_[k] for k in V}
def in_span(vecs, basis):
    M = np.array([[float(b[k]) for k in V] for b in basis]); T = np.array([[float(v[k]) for k in V] for v in vecs])
    return np.linalg.matrix_rank(np.vstack([M, T])) == np.linalg.matrix_rank(M) == len(basis)
c1 = out['T1 +Yukawa-type, generic']; c2 = out['T2 T1 + uddn class']; c3 = out['T3 T2 + (nu^c)^4']
check('[T] T1: exact = span{Y, B, L} (3); with (a) span{Y, B-L} (2), all mixed cubics 0: (a) leaves B-L',
      c1[0] == 3 and in_span([Y, B_, L_], c1[4]) and c1[1] == 2 and c1[2] and in_span([Y, BmL], c1[3]))
check("[T] T2: the register's uddn-class terms conserve B-L: span{Y, B-L} survives even under (c)",
      c2[0] == 2 and c2[1] == 2 and in_span([Y, BmL], c2[3]))
yb = c3[3][0]; rat = [yb[f, 0] / yb['Q', 0] for f in 'QudLen']
check('[T] T3: one added nu^c-number term leaves exactly span{Y} (1), ratios Q:u:d:L:e:n = 1:-4:2:-3:6:0; '
      "same with (nu^c)^4 or nu^c nu^c and no uddn once (a) removes B",
      c3[0] == 1 and rat == [1, -4, 2, -3, 6, 0] and out["T3' T1 + (nu^c)^4"][:2] == (2, 1)
      and out["T3'' T1 + nu^c nu^c"][:2] == (2, 1), str([str(r) for r in rat]))
t4 = out['T4 no Yukawa, uddn + (nu^c)^4']
Xf = {k: Fr(0) for k in V}
for k, v in ((('Q', 0), 1), (('Q', 1), -1), (('L', 0), 1), (('L', 1), -1)): Xf[k] = Fr(v)
okX = all(t == 0 for t in lin(Xf)) and tri(Xf, Xf, Xf) == 0 and tri(Y, Y, Xf) == 0 and tri(Y, Xf, Xf) == 0
check('[T] T4 (masses only from the vacuum): 10 exact U(1)s; X = Q1 - Q2 + L1 - L2 is anomaly-free with Y, '
      'so flavour links survive (a)+(c) and are Higgsed only by the mass condensates', t4[0] == 10 and okX and in_span([Y, Xf], t4[4]))

# ============ D. Pati-Salam route: stabiliser of a nu^c-number term ============
print('== D. su(4)+su(2)L+su(2)R (the mirror-term group) on one 16; stabiliser of (nu^c)^k')
def su(nn):
    g = []
    for i in range(nn):
        for j in range(i + 1, nn):
            m = np.zeros((nn, nn), complex); m[i, j] = m[j, i] = 1; g.append(m)
            m = np.zeros((nn, nn), complex); m[i, j] = -1j; m[j, i] = 1j; g.append(m)
    for k in range(1, nn):
        m = np.zeros((nn, nn), complex); m[:k, :k] = np.eye(k); m[k, k] = -k; g.append(m / np.sqrt(k * (k + 1) / 2))
    return g
I2, I4 = np.eye(2), np.eye(4); Z8 = np.zeros((8, 8))
def blk(A, Bm): return np.block([[A, Z8], [Z8, Bm]])
gens = [blk(np.kron(t, I2), np.kron(-t.conj(), I2)) for t in su(4)] + \
       [blk(np.kron(I4, s), Z8) for s in su(2)] + [blk(Z8, np.kron(I4, -s.conj())) for s in su(2)]
BL4 = np.diag([1 / 3, 1 / 3, 1 / 3, -1]); T3R = blk(Z8, np.kron(I4, -sz.real / 2)); BLm = blk(np.kron(BL4, I2), np.kron(-BL4, I2))
Ym = T3R + BLm / 2
nuc = np.zeros(16, complex); nuc[8 + 2 * 3 + 0] = 1          # (4bar, lepton, beta = 0): B-L = +1, T3R = -1/2, Y = 0
def null_real(Gm):
    ev, U_ = np.linalg.eigh(Gm); return U_[:, ev < 1e-10 * max(1.0, ev.max())]
def gram_explicit(k):   # A_{.,j} = generator j acting on every slot of nu^c^(x k); Gram = Re A^H A
    vk = nuc
    for _ in range(k - 1): vk = np.kron(vk, nuc)
    cols = []
    for g_ in gens:
        acc = np.zeros(16 ** k, complex)
        for slot in range(k):
            t = vk.reshape([16] * k); acc += np.moveaxis(np.tensordot(g_, t, axes=([1], [slot])), 0, slot).ravel()
        cols.append(acc)
    A = np.array(cols).T; return (A.conj().T @ A).real
def gram_product(k):    # same Gram for a product state, in closed form: k <gv,g'v> + k(k-1) <gv,v><v,g'v>
    gv = np.array([g_ @ nuc for g_ in gens])
    return (k * gv.conj() @ gv.T + k * (k - 1) * np.outer((gv.conj() @ nuc), (nuc.conj() @ gv.T))).real
gerr = max(np.abs(gram_explicit(k) - gram_product(k)).max() for k in (1, 2, 3))
S1, S2, S4 = null_real(gram_product(1)), null_real(gram_explicit(2)), null_real(gram_product(4))
St = [sum(cf * g_ for cf, g_ in zip(col, gens)) for col in S4.T]
der = np.array([(a @ b - b @ a).ravel() for a in St for b in St]); dder = np.linalg.matrix_rank(der, tol=1e-9)
# centre: elements z = sum c_i St_i with [z, St_j] = 0 for all j
Cm = np.array([[ (St[i] @ St[j] - St[j] @ St[i]).ravel() for i in range(len(St))] for j in range(len(St))])  # j, i, entries
Cm = Cm.transpose(0, 2, 1).reshape(-1, len(St)); cz = null_real((Cm.conj().T @ Cm).real)
z = sum(cz[i, 0] * St[i] for i in range(len(St))) if cz.shape[1] == 1 else None
yok = z is not None and np.linalg.matrix_rank(np.array([z.ravel(), Ym.ravel()]), tol=1e-8) == 1
check('[T] dim su(4)+su(2)+su(2) = 21; stabiliser of nu^c, nu^c nu^c and (nu^c)^4 (point-split) = 12 each',
      len(gens) == 21 and S1.shape[1] == S2.shape[1] == S4.shape[1] == 12 and gerr < 1e-12, f'{S1.shape[1]}, {S2.shape[1]}, {S4.shape[1]}; closed-form Gram vs explicit k<=3: {gerr:.0e}')
check('[T] that stabiliser = su(3)+su(2)L+u(1)_Y exactly: derived algebra 11, centre 1, centre = Y = T3R + (B-L)/2',
      dder == 11 and cz.shape[1] == 1 and yok, f'derived {dder}, centre {cz.shape[1]}')
print('   so the term that removes the B-L link also breaks the mirror-term group to exactly SU(3) x SU(2) x U(1)_Y')

# ============ E. estimates against measurement ============
print('== E. estimates')
L = np.log(2.44e18 / 91.1876); b1, b2 = 41 / 10, -19 / 6; ai = 127.95
s2w = 3 / 8 - (5 / 8) * (b1 - b2) * L / (2 * np.pi) / ai
print(f'   (d) per-mode equal unit, explicit breaking at the cell: sin^2 thW(MZ) = {s2w:.3f} vs 0.2312 (one loop, SM)')
inv = 50 + (4 / 3) / (2 * np.pi) * np.log(2.44e18 / 0.000511)
print(f'   (d) universal unit on a species link (N_e, 1/alpha_cell ~ 50): alpha_IR = {1/inv:.3f} vs < {gb["L=Z"]**2/(4*np.pi):.0e}')
check('[E] (d) neither selects nor meets measurement: a universal unit gives alpha ~ 1e-2 on species links, '
      'per-link constants need tuning to < 1e-48', 1 / inv > 1e-3 and gb['L=Z'] ** 2 / (4 * np.pi) < 1e-48)
qn = 2 * (Fr(1, 6) - Fr(1, 2)) + (Fr(1, 6) + Fr(1, 2))   # T3 + Y on u, d
check('[T] with B-L unlinked, Q = T3 + Y: q_n = 0 exactly (measured (-0.2 +- 0.8)e-21); a linked B-L admixture leaves q_n free',
      qn == 0)
print('   (nu^c)^4 keeps Z4 of B-L: no Majorana mass, Dirac neutrinos, no 0nubb (KamLAND-Zen T1/2 > 3.8e26 yr; LEGEND-1000 tests)')
print('   nu^c nu^c instead: seesaw, needs M < 6e14 GeV (nuc-dark-matter D4), a scale no law supplies')
print('theorems: B1-B4, C1-C4, D1-D2, E2.  estimates: A1, E1.')
print('supplied: chiral content and SM/PS links (chirality wall open); Yukawa-type flavour-generic terms; the nu^c term;')
print('  vacuum-field charge h; toy reflection R(K); MICROSCOPE 2022, composition, SM one-loop b, alpha(MZ).')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
