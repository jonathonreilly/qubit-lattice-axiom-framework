#!/usr/bin/env python3
"""C4 check: fresh-context, independent code paths for C4's load-bearing steps.

Routes differ from c4_h_normalisation.py:
  A   species couplings by the Jacobian of the coin vector at each corner (no series), plus a
      floating-point torus build of the anticommutator couplings from position-space matrices;
      homogeneity of block 120's compatibility in R (so the normalisation is a stipulation).
  B   lapse identity by the closed-form DeWitt inverse (tensor equation, no component Hessian /
      LUsolve), at generic beta; TT cone; static pull with K1 != K2; single-light-cone equivalence.
  C   R2 against the variational identity [sqrt(g)R]^(2) ~ -(1/2) h:G^(1)(h) (linearised Einstein
      tensor), not a brute expansion of sqrt(g)R.
Expected constants come from the cited definitions, not from C4's runner.
"""
import itertools
import sys
import time

import numpy as np
import sympy as sp

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}", flush=True)


def symm(n):
    a = sp.symbols(f'{n}11 {n}22 {n}33 {n}12 {n}13 {n}23', real=True)
    return sp.Matrix([[a[0], a[3], a[4]], [a[3], a[1], a[5]], [a[4], a[5], a[2]]]), list(a)


h, hv = symm('h')
I3 = sp.eye(3)

# ---------------------------------------------------------------- A: Jacobian at species corners
print("== A: walker coupling strength and species (Jacobian route)")
B = -h / 2  # block 120 realisation at q = 0 (phi_j = 1), Lambda(B) = -(B + B^T) = h
assert sp.simplify(-(B + B.T) - h) == sp.zeros(3, 3)
counts = {}
ok_forms = True
for name in ['site', 'one', 'two']:
    n_unit = 0
    for K in itertools.product([0, 1], repeat=3):
        eta = sp.diag(*[(-1) ** c for c in K])
        # d s_a/dk_b = eta_a delta_ab ; c_a -> eta_a ; d(sin k_j)/dk = eta_j ; d(sin 2k_j /2)/dk = 1
        if name == 'site':      # v_a = s_a + sum_j B_aj s_j
            J = eta + B * eta
        elif name == 'one':     # v_a = s_a + sum_j B_aj c_a s_j
            J = eta + eta * B * eta
        else:                   # v_a = s_a + sum_j B_aj c_a P_j
            J = eta + eta * B
        form = (J.T * J).applyfunc(sp.expand)
        lin = (form - I3).applyfunc(lambda z: sum(t for t in sp.Add.make_args(sp.expand(z))
                                                   if sp.Poly(t, *hv).total_degree() == 1))
        expect = {'site': -(eta * h * eta), 'one': -(h * eta + eta * h) / 2, 'two': -h}[name]
        ok_forms &= sp.simplify(lin - expect) == sp.zeros(3, 3)
        n_unit += int(sp.simplify(lin + h) == sp.zeros(3, 3))
    counts[name] = n_unit
check("A1", ok_forms and counts == {'site': 2, 'one': 1, 'two': 8},
      f"first-order cone at the 8 corners: site -eta h eta, one-step -sym(h eta), two-step -h; corners seeing delta+h: {counts}")

# A2 floating torus build of the couplings from position-space operators (L = 6, uniform random B)
L = 6
N = L ** 3
idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
Tm = []
for a in range(3):
    M = np.zeros((N, N))
    for x, y, z in itertools.product(range(L), repeat=3):
        e = [0, 0, 0]; e[a] = 1
        M[idx(x, y, z), idx(x + e[0], y + e[1], z + e[2])] = 1.0
    Tm.append(M)
S = [(T - T.T) / 2j for T in Tm]
C = [(T + T.T) / 2 for T in Tm]
Pop = [S[j] @ C[j] for j in range(3)]
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
rng = np.random.default_rng(7)
Bn = rng.normal(size=(3, 3)) * 0.05
H0 = sum(np.kron(S[a], sig[a]) for a in range(3))
Hone = H0 + sum(np.kron(0.5 * (Bn[a, j] * C[a] @ S[j] + S[j] @ (Bn[a, j] * C[a])), sig[a]) for a in range(3) for j in range(3))
Htwo = H0 + sum(np.kron(0.5 * (Bn[a, j] * C[a] @ Pop[j] + Pop[j] @ (Bn[a, j] * C[a])), sig[a]) for a in range(3) for j in range(3))
okA2 = np.allclose(Hone, Hone.conj().T) and np.allclose(Htwo, Htwo.conj().T)
# compare spectra with the symbol formula on the grid
ev_two = np.sort(np.linalg.eigvalsh(Htwo))
ev_one = np.sort(np.linalg.eigvalsh(Hone))
sym_two, sym_one = [], []
for n in itertools.product(range(L), repeat=3):
    k = 2 * np.pi * np.array(n) / L
    s, c = np.sin(k), np.cos(k)
    P = s * c
    v2 = s + np.array([sum(Bn[a, j] * c[a] * P[j] for j in range(3)) for a in range(3)])
    v1 = s + np.array([sum(Bn[a, j] * c[a] * s[j] for j in range(3)) for a in range(3)])
    sym_two += [np.linalg.norm(v2), -np.linalg.norm(v2)]
    sym_one += [np.linalg.norm(v1), -np.linalg.norm(v1)]
okA2 &= np.allclose(ev_two, np.sort(sym_two), atol=1e-9) and np.allclose(ev_one, np.sort(sym_one), atol=1e-9)
check("A2", okA2, "6^3 torus, position-space anticommutator couplings (blocks 64/73) with a uniform strain: hermitian, "
      "spectra equal the symbol |s + B c P| (two-step) and |s + B c s| (one-step) used in A1 (floating point, atol 1e-9)")

# A3 block 120's compatibility <K, R G xi> = 0 is linear in R: c*R is compatible iff R is; so a_R is a stipulation
print("[NOTE] A3 (not a computed check): compatibility <K, R G xi> is homogeneous of degree 1 in R (definition, block 120 line 67): "
      "rescaling R -> cR preserves it for every c != 0; 'Lambda R(0) = 1' (line 66) is a normalisation clause, not a consequence")

# A4 uniform frame second order: walker cone E^T E vs matter on delta + a h with h := (E^T E)^{-1} - delta
t = sp.Symbol('t')
eps = sp.Matrix(3, 3, lambda i, j: sp.Rational((3 * i + 5 * j) % 7 - 3, 5))  # a fixed rational tilt
E = I3 + t * eps
hE = ((E.T * E).inv() - I3).applyfunc(lambda z: sp.series(z, t, 0, 3).removeO())
asym = sp.Symbol('a')
match = ((I3 + asym * hE).applyfunc(sp.expand) * (E.T * E)).applyfunc(lambda z: sp.expand(z))
c1 = [sp.expand(z).coeff(t, 1) for z in match]
sol = sp.solve([z for z in c1 if z != 0], asym, dict=True)
check("A4", sol == [{asym: 1}] and sp.simplify(hE.applyfunc(lambda z: z.coeff(t, 1)) + eps + eps.T) == sp.zeros(3, 3),
      f"rational tilt: h = -(eps+eps^T)t + O(t^2) and unit matter coupling a = {sol}")

# ---------------------------------------------------------------- B: lapse identity by DeWitt inverse
print("== B: member's lapse identity with K1, K2, a_s (closed-form DeWitt inverse)")
p = sp.Matrix(sp.symbols('p1 p2 p3', real=True))
pp = (p.T * p)[0, 0]
K1, K2, al, be, a_s, u = sp.symbols('K1 K2 alpha beta a_s u', real=True)
Th, _ = symm('Th')


def R1(M):
    return pp * M.trace() - (p.T * M * p)[0, 0]


def R2(M):
    return (-(pp / 4) * (M * M).trace() + sp.Rational(1, 2) * ((M * p).T * (M * p))[0, 0]
            - sp.Rational(1, 2) * (p.T * M * p)[0, 0] * M.trace() + (pp / 4) * M.trace() ** 2)


def tgrad(f):
    # symmetric tensor derivative: (d f/d h_ij) with off-diagonals split equally
    m = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (0, 1): 3, (0, 2): 4, (1, 2): 5}
    G = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            key = (min(i, j), max(i, j))
            G[i, j] = sp.diff(f, hv[m[key]]) * (1 if i == j else sp.Rational(1, 2))
    return G


# EL for L = alpha hdot:hdot + beta (tr hdot)^2 + pot: 2 alpha hdd + 2 beta delta tr hdd = F, F = tgrad(pot)
pot = K1 * u * R1(h) + K2 * R2(h) + (a_s / 2) * (Th * h).trace()
F = tgrad(pot)
trhdd = F.trace() / (2 * al + 6 * be)
hdd = (F - 2 * be * I3 * trhdd) / (2 * al)
dem = sp.simplify(K1 * R1(hdd))
dem_closing = sp.simplify(dem.subs(be, -al))
tgt = -(K1 * a_s / (4 * al)) * (p.T * Th * p)[0, 0]
check("B1", sp.simplify(dem_closing - tgt) == 0 and not dem_closing.has(K2),
      "beta = -alpha: e_u'' = K1 R1(hdd) = -(K1 a_s/(4 alpha)) p.Theta.p; K2, u, h drop (transversality of dR2, p.(p^2-pp).p = 0)")
check("B2", sp.simplify(dem - tgt) != 0,
      "generic beta: extra trace terms (1 + beta/alpha) p^2 tr(hdd) survive; identity is special to the closing ratio")
# B3 consistency with the source notes: walker gives e'' = -wbar^2 p.Theta.p (wbar = 1) => K1 a_s = 4 alpha
sol = sp.solve(sp.Eq(K1 * a_s / (4 * al), 1), K1)
check("B3", sol == [4 * al / a_s],
      "matching the walker's exact identity (09-25 exact-lattice T1, block 134 T2) fixes K1 a_s = 4 alpha; "
      "the notes' 'alpha = K/4' is this with a_s = 1 and K := K1")
# B4 TT cone: p = (0,0,P), h = A(e1e1 - e2e2) + Bx(e1e2 + e2e1)
P_, A_, Bx = sp.symbols('P A Bx', real=True)
hTT = sp.Matrix([[A_, Bx, 0], [Bx, -A_, 0], [0, 0, 0]])
subs_p = {p[0]: 0, p[1]: 0, p[2]: P_}
FTT = tgrad(K2 * R2(h)).subs(subs_p).subs(dict(zip(hv, [A_, -A_, 0, Bx, 0, 0])))
# 2 alpha hdd = F (tr hdd = 0 on TT) ; F = -omega^2-independent: F = -(K2 P^2/2) h
okTT = sp.simplify(FTT + (K2 * P_ ** 2 / 2) * hTT) == sp.zeros(3, 3)
om2 = K2 * P_ ** 2 / (4 * al)
okR1 = sp.simplify(R1(hTT).subs(subs_p)) == 0
check("B4", okTT and okR1, f"TT pair: 2 alpha hdd = -(K2 P^2/2) h, omega^2 = {om2}; R1 = 0 on TT so K1 is absent")
# B5 single light cone: with K1 a_s = 4 alpha (B3), TT speed^2 = K2/(4 alpha) = K2/(K1 a_s) -> 1 iff K2 = K1 a_s
v2 = sp.simplify((K2 / (4 * al)).subs(al, K1 * a_s / 4))
check("B5", sp.simplify(v2 - K2 / (K1 * a_s)) == 0,
      f"after lapse matching the TT speed^2 is {v2}: '= walker top speed' holds iff K2 = a_s K1 (gamma = 1); "
      "the notes' sentence 'at alpha = K/4 the disturbances move at the walker's top speed' uses the single-K member")
# B6 static pull with K1 != K2: isotropic gauge h = 2 lam delta, Theta = 0, source e on the clock
lam, e = sp.symbols('lam e', real=True)
iso = dict(zip(hv, [2 * lam, 2 * lam, 2 * lam, 0, 0, 0]))
potS = K1 * u * R1(h) + K2 * R2(h) - e * u
Fs = tgrad(potS).subs(iso)
cons = sp.diff(potS, u).subs(iso)
sol6 = sp.solve([cons] + list(Fs), [lam, u], dict=True)
gam = sp.simplify(a_s * sol6[0][lam] / (-sol6[0][u])) if len(sol6) == 1 else None
check("B6", gam is not None and sp.simplify(gam - a_s * K1 / K2) == 0,
      f"static pull: lam = {sol6[0][lam] if sol6 else None}, u = {sol6[0][u] if sol6 else None}; gamma = {gam}")

# ---------------------------------------------------------------- C: R1, R2 vs linearised Einstein tensor
print("== C: R1, R2 against the variational identity")
# Fourier convention d -> i p. Linearised Ricci and scalar for g = delta + h:
Ric = sp.zeros(3, 3)
trh = h.trace()
for i in range(3):
    for j in range(3):
        Ric[i, j] = sp.Rational(1, 2) * (-sum(p[k] * p[i] * h[k, j] for k in range(3))
                                          - sum(p[k] * p[j] * h[k, i] for k in range(3))
                                          + pp * h[i, j] + p[i] * p[j] * trh)
Rs = sp.expand(sum(Ric[i, i] for i in range(3)))
check("C1", sp.expand(Rs - R1(h)) == 0, "linearised scalar curvature of delta + h is R1(h) = p^2 tr h - p.h.p (unit coefficient)")
G1 = Ric - I3 * Rs / 2
# int [sqrt g R]^(2) = -(1/2) int h_ij G^(1)ij(h) (from d/de int sqrt g R = -int sqrt g G^ij dg_ij; the first-order
# term of sqrt g R is a total derivative). For a real Fourier mode the quadratic symbol is -(1/2) h:G1(h).
Q = sp.expand(-sp.Rational(1, 2) * sum(h[i, j] * G1[i, j] for i in range(3) for j in range(3)))
check("C2", sp.expand(Q - R2(h)) == 0,
      "block 62's R2(h) = -(1/2) h:G^(1)(h): R2 is the second-order part of sqrt(g)R[delta + h] (modulo divergences) with unit coefficient")
# C3 consequence: GR on delta + h/r gives (R1/r, R2/r^2): K1 = K r, K2 = K, K2/K1 = 1/r (B21 family), single K iff r = 1
r, Kc = sp.symbols('r K', positive=True)
check("C3", sp.simplify((Kc * r * R2(h / r)) / (Kc * R2(h)) - 1 / r) == 0 and sp.simplify(Kc * r * R1(h / r) - Kc * R1(h)) == 0,
      "K r sqrt(g)R[delta + h/r] = K R1 + (K/r) R2 at quadratic order: B21's one-parameter family, matter on delta + h/r has a_s = 1/r")

print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES) - sum(RES)}  ({time.time() - T0:.1f} s)")
sys.exit(0 if all(RES) else 1)
