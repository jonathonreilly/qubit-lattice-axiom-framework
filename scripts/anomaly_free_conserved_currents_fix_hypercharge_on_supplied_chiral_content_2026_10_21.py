#!/usr/bin/env python3
"""Which value currents may links respond to?  Supplied-model, finite diagnostic; no physical identification.

A. The measured conflict: a link field coupled to relay value (fermion number F), to baryon number B or to
   B-L with strength e, against the neutron-charge, atom-neutrality and MICROSCOPE bounds.
B. Lattice facts: the eps symmetry of the massless CL-2 tick survives arbitrary link phases exactly, and its
   anomaly weight vanishes; the 2D Wilson index equals the flux for one light species and cancels between
   doublers (on-site lattice symmetries carry no net anomaly).
C. Spectral-flow rederivation of the abelian anomaly weight sum_i chi_i X_i q_i^2 (exact counting).
D. Supplied SM chiral content, 3 generations, generic Yukawa textures: classically conserved U(1)s, then the
   subspace that stays conserved when SU(3), SU(2) and the U(1) links themselves act (all trilinear weights 0).
E. Electric charges that follow; B and L under the rule; instanton numbers.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import os, sys, signal, itertools
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
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))

# ===================== A. measured conflict =====================
print('== A. measured bounds')
G, u, hbar, c = 6.67430e-11, 1.66053906660e-27, 1.054571817e-34, 2.99792458e8
aG = G * u * u / (hbar * c); alpha = 1 / 137.035999
# (Z, A, atomic mass in u) dominant isotopes; alloys by mass fraction (MICROSCOPE TA6V and PtRh10)
iso = {'Ti': (22, 48, 47.947947), 'Al': (13, 27, 26.981538), 'V': (23, 51, 50.943960), 'Pt': (78, 195, 194.964791),
       'Rh': (45, 103, 102.905504), 'Fe': (26, 56, 55.934942), 'O': (8, 16, 15.994915), 'Si': (14, 28, 27.976927),
       'Mg': (12, 24, 23.985042), 'S': (16, 32, 31.972071), 'Ni': (28, 58, 57.935343), 'Ca': (20, 40, 39.962591)}
def per_mass(mix, X):   # charge per atomic mass unit for a mass-fraction mix
    return sum(w / iso[e][2] * X(*iso[e][:2]) for e, w in mix.items()) / sum(mix.values())
TA6V = {'Ti': .90, 'Al': .06, 'V': .04}; PtRh = {'Pt': .90, 'Rh': .10}
Earth = {'Fe': .32, 'O': .30, 'Si': .15, 'Mg': .14, 'S': .03, 'Ni': .018, 'Ca': .015, 'Al': .014}
charges = {'F=3A+Z': lambda Z, A: 3 * A + Z, 'B=A': lambda Z, A: A, 'B-L=A-Z': lambda Z, A: A - Z}
eta_max = 1.5e-15 + 2.7e-15     # MICROSCOPE 2022: eta(Ti,Pt) = (-1.5 +- 2.3 stat +- 1.5 syst) e-15
print(f'   alpha_G(u) = {aG:.3e};  eta bound used |eta| < {eta_max:.1e}')
gb = {}
for k, X in charges.items():
    xE = per_mass(Earth, X); dx = per_mass(TA6V, X) - per_mass(PtRh, X)
    eta_e = alpha / aG * xE * abs(dx); g = np.sqrt(4 * np.pi * aG * eta_max / (xE * abs(dx))); gb[k] = g
    print(f'   {k:8s}: (X/mu)_Earth={xE:.4f}  Delta(X/mu)_TiPt={dx:+.3e}  eta(coupling e)={eta_e:.1e}  g_max={g:.1e}')
check('MICROSCOPE: a massless B or B-L link needs g < 1e-24 (e = 0.303 is excluded by > 45 orders in eta)',
      gb['B=A'] < 1e-24 and gb['B-L=A-Z'] < 1e-24, f"g_B<{gb['B=A']:.1e}, g_B-L<{gb['B-L=A-Z']:.1e}")
qn_meas, qn_err = -0.4e-21, 1.1e-21   # Baumann et al. 1988; atom neutrality Bressi et al. 2011: (-0.1+-1.1)e-21
qF = {'e': 1, 'u': 1, 'd': 1}
check('photon on relay value F: q_n = q_p = 3, q_H = +4 (e and p repel; atoms unbound); measured |q_n| < 1.5e-21',
      qF['u'] + 2 * qF['d'] == 3 and 2 * qF['u'] + qF['d'] + qF['e'] == 4, f'excluded by a factor {3/(abs(qn_meas)+qn_err):.0e}')

# ===================== B. lattice facts =====================
print('== B. lattice: on-site symmetries survive links and carry no net anomaly')
Cc = np.array(list(itertools.product((0, 1), repeat=3))); cc = Cc - 0.5
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for i in range(8):
    n = (2 * Cc[i] - 1.0) / np.sqrt(3); w, v = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v[:, -1])
Gm = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(Cc[a] - Cc[b])) == 1: W[a, b] = -Gm[a, b] / abs(Gm[a, b]) / np.sqrt(3)
check('CL-2 block hop W: Hermitian, W^2 = 1', np.abs(W - W.conj().T).max() < 1e-12 and np.abs(W @ W - np.eye(8)).max() < 1e-12)
N = 4; sites = list(itertools.product(range(N), repeat=3)); idx = {s: i for i, s in enumerate(sites)}; V = N ** 3
rng = np.random.default_rng(7)
theta = {}
def link(s, t):   # antisymmetric random link phase
    key = (s, t) if (s, t) < (t, s) else (t, s); sg = 1 if key == (s, t) else -1
    if key not in theta: theta[key] = rng.uniform(-np.pi, np.pi)
    return sg * theta[key]
def sgnm(H):
    w, v = np.linalg.eigh(H); return (v * np.sign(w)) @ v.conj().T
def half(off, mu, q):
    M = np.zeros((V, V), complex)
    for b in itertools.product(range(0, N, 2), repeat=3):
        ss = [tuple((b[k] + off + Cc[i][k]) % N for k in range(3)) for i in range(8)]
        Wt = np.array([[W[a, bb] * np.exp(1j * q * link(ss[a], ss[bb])) if W[a, bb] != 0 else 0 for bb in range(8)] for a in range(8)])
        S = sgnm(Wt)                                   # supplied covariant extension: sign(W_theta), = W at theta = 0
        Bk = np.cos(mu / 2) * S + 1j * np.sin(mu / 2) * np.eye(8)
        ix = [idx[s] for s in ss]; M[np.ix_(ix, ix)] = Bk
    return M
epsL = np.diag([(-1.0) ** sum(s) for s in sites])
for mu in (0.0, 0.4):
    Ut = half(1, mu, 1.0) @ half(0, mu, 1.0)
    un = np.abs(Ut.conj().T @ Ut - np.eye(V)).max(); cm = np.abs(epsL @ Ut - Ut @ epsL).max()
    if mu == 0.0:
        check('random link phases, mu = 0: tick unitary and eps = (-1)^(x+y+z) commutes exactly (survives links)', un < 1e-10 and cm < 1e-10, f'{un:.1e}, {cm:.1e}')
    else:
        check('mu = 0.4: eps broken by the mass (|[eps,U]| > 0.1)', cm > 0.1, f'{cm:.2f}')
print('   eps = gamma5 x sigma3 (margolus-doublet): anomaly weight tr(gamma5 sigma3 Q^2) over the copy doublet ∝ tr sigma3 = 0')

# 2D Wilson-Dirac index on an L x L torus with n flux quanta: index = -(1/2) tr sign(sigma3 (D_W - m0))
L = 14
def wilson_index(nflux, m0, r):
    s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1.]).astype(complex)
    Vt = L * L; D = np.zeros((2 * Vt, 2 * Vt), complex); f = 2 * np.pi * nflux / (L * L)
    def ix(x, y): return (x % L) + L * (y % L)
    for x in range(L):
        for y in range(L):
            i = ix(x, y)
            Ux = np.exp(-1j * f * L * y) if x == L - 1 else 1.0      # Landau gauge A_y = f x, twist on x boundary
            Uy = np.exp(1j * f * x)
            for (j, U_, s) in ((ix(x + 1, y), Ux, s1), (ix(x, y + 1), Uy, s2)):
                blk_f = 0.5 * (s - r * np.eye(2)) * U_; blk_b = 0.5 * (-s - r * np.eye(2)) * np.conj(U_)
                D[2*i:2*i+2, 2*j:2*j+2] += blk_f; D[2*j:2*j+2, 2*i:2*i+2] += blk_b
            D[2*i:2*i+2, 2*i:2*i+2] += (2 * r - m0) * np.eye(2)
    H = np.kron(np.eye(Vt), s3) @ D
    w = np.linalg.eigvalsh((H + H.conj().T) / 2); return -0.5 * np.sum(np.sign(w))
res = {(n, m0, r): wilson_index(n, m0, r) for (n, m0, r) in [(1, 1, 1), (2, 1, 1), (3, 1, 1), (2, 3, 1), (2, 5, 1), (2, 1, 0)]}
print('   index (flux, m0, r):', {k: int(round(float(v))) for k, v in res.items()})
check('Wilson, one light species (m0 = 1): |index| = flux for flux 1, 2, 3 (zero modes = flux quanta)',
      all(abs(abs(res[(n, 1, 1)]) - n) < 1e-9 for n in (1, 2, 3)))
check('two doublers (m0 = 3) give -index of one; all four (m0 = 5) or naive (r = 0) give 0: doublers cancel the anomaly',
      abs(res[(2, 3, 1)] + res[(2, 1, 1)]) < 1e-9 and abs(res[(2, 5, 1)]) < 1e-9 and abs(res[(2, 1, 0)]) < 1e-9)

# ===================== C. spectral flow =====================
print('== C. spectral flow of a chiral branch (exact count)')
def flow(chi, q, cut=50):   # levels k = (2 pi/L)(n + 1/2 + q Phi/2 pi), E = chi k, Phi: 0 -> 2 pi; count zero crossings
    n = np.arange(-cut, cut); E0 = chi * (n + 0.5); E1 = chi * (n + 0.5 + q)
    return int(np.sum((E0 >= 0) & (E1 < 0)) - np.sum((E0 < 0) & (E1 >= 0)))   # change of the filled count
fl = {(chi, q): flow(chi, q) for chi in (1, -1) for q in (1, 2, -1, 3)}
check('one flux quantum moves chi*q levels of a branch of charge q; times LLL degeneracy q n_B  -> weight sum chi X q^2',
      all(fl[(chi, q)] == -chi * q for chi, q in fl), str({f'{k}': v for k, v in list(fl.items())[:4]}))

# ===================== D. SM content: which U(1)s may be gauged =====================
print('== D. supplied chiral content (left-handed Weyl), 3 generations')
# fields: (name, colour dim, SU(2) dim, T(SU3) per comp, T(SU2) per comp)
FLD = [('Q', 3, 2), ('u', 3, 1), ('d', 3, 1), ('L', 1, 2), ('e', 1, 1), ('n', 1, 1)]
def traces(ch, with_n=True):
    """ch: dict (field, gen) -> charge.  Returns weights SU3^2 X, SU2^2 X, X^3, grav X (left-handed Weyl sums)."""
    s3 = s2 = cub = gr = Fr(0)
    for g in range(3):
        for f, nc, nw in FLD:
            if f == 'n' and not with_n: continue
            x = ch[(f, g)]
            if nc == 3: s3 += Fr(1, 2) * nw * x
            if nw == 2: s2 += Fr(1, 2) * nc * x
            cub += nc * nw * x ** 3; gr += nc * nw * x
    return s3, s2, cub, gr
def tri(a, b, c3, with_n=True):
    return sum(nc * nw * a[(f, g)] * b[(f, g)] * c3[(f, g)] for g in range(3) for f, nc, nw in FLD if (f != 'n' or with_n))
def univ(q, u_, d, l, e, n): return {(f, g): Fr(v) for g in range(3) for f, v in zip('QudLen', (q, u_, d, l, e, n))}
Y = univ(Fr(1, 6), Fr(-2, 3), Fr(1, 3), Fr(-1, 2), Fr(1), Fr(0))
B = univ(Fr(1, 3), Fr(-1, 3), Fr(-1, 3), 0, 0, 0); Lp = univ(0, 0, 0, 1, -1, -1)
Fn = univ(1, -1, -1, 1, -1, -1)
BmL = {k: B[k] - Lp[k] for k in B}; BpL = {k: B[k] + Lp[k] for k in B}
LmuLtau = {(f, g): Fr((g == 1) - (g == 2)) * Lp[(f, g)] for f, g in Lp}
rows = {}
for name, X in [('F (relay value)', Fn), ('B', B), ('L', Lp), ('B+L', BpL), ('B-L', BmL), ('Lmu-Ltau', LmuLtau), ('Y', Y)]:
    s3, s2, cub, gr = traces(X); yyx = tri(Y, Y, X); rows[name] = (s3, s2, cub, gr, yyx)
    print(f'   {name:16s} SU3^2X={str(s3):5s} SU2^2X={str(s2):5s} X^3={str(cub):5s} grav={str(gr):4s} Y^2X={yyx}')
check('relay value F, B, L, B+L have SU(2)^2 weights 6, 3/2, 3/2, 3 (nonzero): links acting break them',
      [rows[k][1] for k in ('F (relay value)', 'B', 'L', 'B+L')] == [6, Fr(3, 2), Fr(3, 2), 3])
check('Y and B-L (with nu^c): all weights 0; without nu^c B-L has X^3 = grav = -3',
      all(v == 0 for v in rows['Y']) and all(v == 0 for v in rows['B-L']) and traces(BmL, False)[2:] == (-3, -3))
check('Lmu-Ltau: all weights 0 (anomaly alone does not remove it)', all(v == 0 for v in rows['Lmu-Ltau']))

# classical conservation with generic (all i,j) Yukawas: unknowns X(f,g) and X(H)
def nullspace(with_nuc):
    fl_ = [f for f, _, _ in FLD if (f != 'n' or with_nuc)]
    var = {(f, g): sp.Symbol(f'{f}{g}') for g in range(3) for f in fl_}; h = sp.Symbol('h')
    eqs = []
    for i in range(3):
        for j in range(3):
            eqs += [var[('Q', i)] + h + var[('u', j)], var[('Q', i)] - h + var[('d', j)], var[('L', i)] - h + var[('e', j)]]
            eqs += [var[('L', i)] + h + var[('n', j)]] if with_nuc else [var[('L', i)] + var[('L', j)] + 2 * h]   # Dirac or Weinberg
    allv = list(var.values()) + [h]
    A = sp.Matrix([[sp.diff(e_, v) for v in allv] for e_ in eqs]); ns = A.nullspace()
    return var, h, allv, ns
for with_nuc in (True, False):
    var, h, allv, ns = nullspace(with_nuc)
    # impose SU(3)^2 X and SU(2)^2 X (linear)
    a = sp.symbols(f'a0:{len(ns)}'); gen = sum((ai * v for ai, v in zip(a, ns)), sp.zeros(len(allv), 1))
    val = dict(zip(allv, gen))
    s3 = sum(sp.Rational(1, 2) * (2 * val[var[('Q', g)]] + val[var[('u', g)]] + val[var[('d', g)]]) for g in range(3))
    s2 = sum(sp.Rational(1, 2) * (3 * val[var[('Q', g)]] + val[var[('L', g)]]) for g in range(3))
    sol = sp.solve([s3, s2], a, dict=True)
    gen2 = gen.subs(sol[0]) if sol else gen; free = sorted(gen2.free_symbols, key=str)
    basis = [gen2.diff(fs) for fs in free]
    def asdict(vec): return {k: Fr(str(sp.nsimplify(vec[allv.index(var[k])]))) for k in var}
    bd = [asdict(bv) for bv in basis]
    for dct in bd:
        if not with_nuc:
            for g in range(3): dct[('n', g)] = Fr(0)
    trilin = [tri(x1, x2, x3, with_nuc) for x1 in bd for x2 in bd for x3 in bd]
    grav = [traces(x1, with_nuc)[3] for x1 in bd]
    lab = 'Dirac nu^c' if with_nuc else 'no nu^c, Weinberg'
    print(f'   {lab}: classical U(1)s dim {len(ns)}; after SU(3)^2, SU(2)^2 dim {len(basis)}; trilinears {set(trilin)}, grav {set(grav)}')
    if with_nuc:
        check('Dirac nu^c: classical conserved U(1)s = span{Y,B,L} (dim 3); stays-conserved subspace = span{Y, B-L} (dim 2), all trilinears 0',
              len(ns) == 3 and len(basis) == 2 and set(trilin) == {0} and set(grav) == {0})
    else:
        ok = len(ns) == 2 and len(basis) == 1 and set(trilin) == {0}
        yv = bd[0]; rat = {f: yv[(f, 0)] / yv[('Q', 0)] for f in 'QudLe'}
        check('Weinberg (no nu^c): classical = span{Y,B}; stays-conserved = span{Y} with ratios Q:u:d:L:e = 1:-4:2:-3:6 (the SM Y)',
              ok and [rat[f] for f in 'QudLe'] == [1, -4, 2, -3, 6], str([str(rat[f]) for f in 'QudLe']))
# generation-universal derivation without the gravitational weight: Y^3 = (h-3q)^3 up to sign
q_, h_ = sp.symbols('q h'); l_ = -3 * q_
cubic = 6 * q_**3 + 3 * (-q_ - h_)**3 + 3 * (-q_ + h_)**3 + 2 * l_**3 + (-l_ + h_)**3
check('with Yukawas and SU(2)^2: X^3 per generation = (h - 3q)^3, so h = 3q (Y fixed up to scale; no gravity input)',
      sp.expand(cubic - (h_ - 3 * q_)**3) == 0)

# ===================== E. charges, B and L =====================
print('== E. electric charge = unbroken T3 + lambda Y (+ eps (B-L) if B-L is gauged)')
lam, epsv = sp.symbols('lambda epsilon')
qY = {'Q': sp.Rational(1, 6), 'L': sp.Rational(-1, 2), 'uR': sp.Rational(2, 3), 'dR': sp.Rational(-1, 3), 'eR': -1}
BL = {'Q': sp.Rational(1, 3), 'L': -1}
def qch(f, t3): return t3 + lam * qY[f] + epsv * BL[f]
qu, qd = qch('Q', sp.Rational(1, 2)), qch('Q', -sp.Rational(1, 2)); qnu, qe = qch('L', sp.Rational(1, 2)), qch('L', -sp.Rational(1, 2))
qp, qn, qH = 2 * qu + qd, qu + 2 * qd, 2 * qu + qd + qe
check('q_e + q_p = 0 identically in lambda and epsilon (hydrogen neutral from the consistency rule alone)', sp.simplify(qH) == 0)
check('q_n = -q_nu identically: neutron neutral iff neutrino neutral', sp.simplify(qn + qnu) == 0, f'q_n = {sp.simplify(qn)}')
vac = {lam: 1, epsv: 0}    # vacuum component of H: T3 = -1/2, Y = +1/2 neutral  <=> lambda = 1
vals = [qe.subs(vac), qp.subs(vac), qn.subs(vac), qu.subs(vac), qd.subs(vac), qnu.subs(vac)]
check('neutral vacuum (H: T3=-1/2, Y=1/2): e, p, n, u, d, nu = -1, 1, 0, 2/3, -1/3, 0 (measured values)',
      vals == [-1, 1, 0, sp.Rational(2, 3), sp.Rational(-1, 3), 0], str(vals))
print(f'   with a gauged B-L admixture: q_n = epsilon; measured |q_n| < 1.5e-21 bounds |epsilon| < 1.5e-21')
aW = (1 / 127.95) / 0.23122; supp = 4 * np.pi / aW
dB = sum(Fr(1, 3) for g in range(3) for col in range(3)); dL = 3; dF = 3 * 3 + 3
check('SU(2) instanton: one zero mode per doublet -> Delta B = Delta L = 3, Delta(B-L) = 0, Delta F = 12',
      dB == 3 and dL == 3 and dF == 12 and dF == 2 * rows['F (relay value)'][1])
print(f'   rate ~ exp(-4 pi/alpha_W) = exp(-{supp:.1f}) = 10^{-supp/np.log(10):.1f}; needs 3 baryons (one proton cannot decay this way)')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
