#!/usr/bin/env python3
"""A one-dimensional lattice Hamiltonian constraint without local degrees of freedom is first class, but lattice
parametrised field theory is anomalous, and first-classness is local zero curvature.

Companion runner of
docs/A_ONE_DIMENSIONAL_LATTICE_HAMILTONIAN_CONSTRAINT_WITHOUT_LOCAL_DEGREES_OF_FREEDOM_IS_FIRST_CLASS_BUT_LATTICE_PARAMETRISED_FIELD_THEORY_IS_ANOMALOUS_AND_FIRST_CLASSNESS_IS_LOCAL_ZERO_CURVATURE_BOUNDED_THEOREM_NOTE_2026-10-18.md

Self-contained (Python 3, sympy). Consolidates the scale-ladder campaign block C10 runner (c10_runner.py,
c10_staggered_check.py) and parts of its same-family check (chk_A.py, chk_P.py, chk_P4.py, chk_stag.py). It imports
nothing from the campaign directory. Same model family throughout: re-running this runner is not an independent check.

Every test is exact: sympy over QQ and QQ(symbols), cyclotomic reduction in QQ[w]/Phi_L, Groebner bases over QQ
(a basis [1] certifies inconsistency over C), exact linear algebra.

Supplied models only (nothing adopted, no physical identification). Z_L periodic, circulant Delta_xy = d(y - x),
symbol lam_n = sum_r d(r) w^(n r), w = exp(2 pi i/L); A = Delta - Delta^T, S = Delta + Delta^T.
  Model A : (phi, pi; X, P), 4L-dim.  H_x = (pi^2 + (Dphi)^2)/2 - (P^2 + (DX)^2)/2,  D_x = pi Dphi + P DX.
            l, m = a -+ beta; n, k = b -+ gamma; a, b = pi +- Dphi; beta, gamma = P -+ DX;  C+ = l m/4, C- = n k/4.
  Model P : (phi, pi; u+, Pi+; u-, Pi-), 6L-dim.  g+- = 1 + Delta u+-,
            C+ = Pi+ g+ + a^2/4,  C- = Pi- g- - b^2/4,  H = C+ - C-, D = C+ + C-.
  Kuchar  : K_x = Pi_x + h_x(u, a), chiral bracket {a_x, a_y} = 2 Delta_xy (antisymmetric Delta);
            curvature F_xy = d_{u_y} h_x - d_{u_x} h_y + {h_x, h_y}.

Parts
  L   frame/counting lemmas, Kuchar form, recombination C = g K and its zeroth-order constants (Lambda_n = lam_n).
  A   Model A: exact brackets, Theorem A1 (symbolic antisymmetric Delta), Sigma cap U, Dirac algebra, A3 kinks.
  P   Model P: exact brackets, on-shell anomaly, hand-proof witness for every antisymmetric Delta, rational points
      (3/784 forward), P4a curvature and anomaly = g_x g_y F_xy.
  J   finite-range Kuchar densities at the ruler: rational class, jet certificates (Groebner) with controls.
  G   staggered flat density (2Z-covariant only).
  K   deparametrised clocks (P6): no finite-range quadratic density with sum = H0 and {h_0, H0} = 0.
Default: TOTAL PASS=59 FAIL=0 in about 2 min (single-threaded); --slow: TOTAL PASS=68 FAIL=0 in about 10 min.  --slow adds the full A3 census at L = 4, 5
(central, forward), the shift-invariant (1,2) N = 2 consistency, the staggered example at L = 8, and the P6 windows
(8,1) central and (9,2) central/forward.
"""
from __future__ import annotations

import itertools
import sys
import time

import sympy as sp
from sympy import QQ

SLOW = "--slow" in sys.argv
PASS = FAIL = 0
T0 = time.time()


def check(name, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""), flush=True)


def section(title):
    print(f"\n=== {title}  [{time.time() - T0:.0f}s]", flush=True)


# ------------------------------------------------------------------ difference operators and brackets
def circ(L, d):
    """circulant Delta_xy = d(y - x); keys of d are offsets (negative allowed)."""
    D = sp.zeros(L, L)
    for x in range(L):
        for r, v in d.items():
            D[x, (x + r) % L] += v
    return D


HALF = sp.Rational(1, 2)
FWD = {1: 1, 0: -1}
CEN = {1: HALF, -1: -HALF}
d1, d2 = sp.symbols("d1 d2")
AS2 = {1: d1, -1: -d1, 2: d2, -2: -d2}          # general antisymmetric range-2 circulant (all antisymmetric at L = 5, 6)
w = sp.Symbol("w")


def pb_canon(F, G, Q, P):
    return sp.expand(sum(sp.diff(F, q) * sp.diff(G, p) - sp.diff(F, p) * sp.diff(G, q) for q, p in zip(Q, P)))


def cyclo_zero(e, L):
    return sp.rem(sp.expand(e), sp.cyclotomic_poly(L, w), w) == 0


def lam(n, d, L):
    return sp.expand(sum(v * w**((n * r) % L) for r, v in d.items()))


# ================================================================== Part L
section("Part L: frame and counting lemmas (L1, L2), Kuchar form (L3), recombination (L4)")
x, y, z, px, py, pz = sp.symbols("x y z px py pz")
Q3, P3 = [x, y, z], [px, py, pz]
br = pb_canon(px, py + x * pz, Q3, P3)                        # V1 = d_x, V2 = d_y + x d_z: [V1, V2] = d_z, not involutive
on = br.subs({px: 0, py: -x * pz})
check("L1a non-involutive momentum-linear pair <p,V_a>: {C1,C2} on Sigma = -p_z != 0 (not first class)",
      sp.expand(on + pz) == 0, f"{{C1,C2}}|Sigma = {on}")
br = pb_canon(px, py + x * px, Q3, P3)                        # V2 = d_y + x d_x: involutive
check("L1b involutive pair: {C1,C2} = -C1 (structure function times constraint)", sp.expand(br + px) == 0)
q3 = sp.symbols("q0:3")
k3 = sp.symbols("k0:3")
V = [[1, q3[2], q3[0]**2], [0, 1, q3[1]], [0, 0, 1]]          # unit upper triangular: a frame everywhere
Cs = [sum(V[a_][i] * k3[i] for i in range(3)) for a_ in range(3)]
check("L1c frame (n momentum-linear constraints on an n-dim base): Sigma = zero section, first class automatically",
      all(pb_canon(Cs[a_], Cs[b_], q3, k3).subs({kk: 0 for kk in k3}) == 0 for a_ in range(3) for b_ in range(3)))

# L2: Model A Sigma cap U = {l = k = 0}: {l,l} = {k,k} = 0, {l_x, k_y} = 2 S_xy (general circulant), rank 2L
L = 5
ds = sp.symbols(f"c0:{L}")
Dg = circ(L, {r: ds[r] for r in range(L)})


def modelA(L, D):
    f = sp.symbols(f"f0:{L}"); p_ = sp.symbols(f"p0:{L}"); X = sp.symbols(f"X0:{L}"); P = sp.symbols(f"P0:{L}")
    Df = [sum(D[i, j] * f[j] for j in range(L)) for i in range(L)]
    DX = [sum(D[i, j] * X[j] for j in range(L)) for i in range(L)]
    a = [p_[i] + Df[i] for i in range(L)]; b = [p_[i] - Df[i] for i in range(L)]
    be = [P[i] - DX[i] for i in range(L)]; ga = [P[i] + DX[i] for i in range(L)]
    l = [sp.expand(a[i] - be[i]) for i in range(L)]; m = [sp.expand(a[i] + be[i]) for i in range(L)]
    n = [sp.expand(b[i] - ga[i]) for i in range(L)]; k = [sp.expand(b[i] + ga[i]) for i in range(L)]
    Cp = [sp.expand(l[i] * m[i] / 4) for i in range(L)]; Cm = [sp.expand(n[i] * k[i] / 4) for i in range(L)]
    H = [sp.expand((p_[i]**2 + Df[i]**2 - P[i]**2 - DX[i]**2) / 2) for i in range(L)]
    Dd = [sp.expand(p_[i] * Df[i] + P[i] * DX[i]) for i in range(L)]
    return dict(f=f, p=p_, X=X, P=P, l=l, m=m, n=n, k=k, Cp=Cp, Cm=Cm, H=H, D=Dd,
                Q=list(f) + list(X), Pm=list(p_) + list(P))


def modelA_ring(L, d):
    """Model A in the sparse polynomial ring QQ[params, phi, pi, X, P] (fast exact arithmetic); d as in circ()."""
    params = sorted({s for v in d.values() for s in sp.sympify(v).free_symbols}, key=str)
    names = [str(s) for s in params] + [f"f{i}" for i in range(L)] + [f"p{i}" for i in range(L)] + \
            [f"X{i}" for i in range(L)] + [f"P{i}" for i in range(L)]
    R, *gens = sp.ring(names, QQ)
    npar = len(params)
    f, p_, X, P = (gens[npar + s * L: npar + (s + 1) * L] for s in range(4))
    Dm = [[R.from_expr(sp.sympify(circ(L, d)[i, j])) if circ(L, d)[i, j] != 0 else R(0) for j in range(L)] for i in range(L)]
    Df = [sum((Dm[i][j] * f[j] for j in range(L)), R(0)) for i in range(L)]
    DX = [sum((Dm[i][j] * X[j] for j in range(L)), R(0)) for i in range(L)]
    a = [p_[i] + Df[i] for i in range(L)]; b = [p_[i] - Df[i] for i in range(L)]
    be = [P[i] - DX[i] for i in range(L)]; ga = [P[i] + DX[i] for i in range(L)]
    l = [a[i] - be[i] for i in range(L)]; m = [a[i] + be[i] for i in range(L)]
    n = [b[i] - ga[i] for i in range(L)]; k = [b[i] + ga[i] for i in range(L)]
    Cp = [l[i] * m[i] / 4 for i in range(L)]; Cm = [n[i] * k[i] / 4 for i in range(L)]
    H = [(p_[i]**2 + Df[i]**2 - P[i]**2 - DX[i]**2) / 2 for i in range(L)]
    Dd = [p_[i] * Df[i] + P[i] * DX[i] for i in range(L)]
    return dict(D=Dm, l=l, m=m, n=n, k=k, Cp=Cp, Cm=Cm, H=H, Dd=Dd, Q=list(f) + list(X), Pm=list(p_) + list(P))


def pb_ring(F, G, Q, P):
    return sum((F.diff(q) * G.diff(p) - F.diff(p) * G.diff(q) for q, p in zip(Q, P)), F.ring(0))


M = modelA(L, Dg)
pbA = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
S = Dg + Dg.T
ok = all(pbA(M["l"][i], M["l"][j]) == 0 and pbA(M["k"][i], M["k"][j]) == 0
         and sp.expand(pbA(M["l"][i], M["k"][j]) - 2 * S[i, j]) == 0 for i in range(L) for j in range(L))
allv = M["Q"] + M["Pm"]
rk = sp.Matrix([[sp.diff(e, v) for v in allv] for e in M["l"] + M["k"]]).rank()
check("L2 Model A L=5 general circulant: {l,l} = {k,k} = 0, {l_x,k_y} = 2 S_xy, rank(l,k) = 2L: "
      "{l=k=0} is Lagrangian (2L constraints on 4L dims, reduced space 0-dim) iff S = 0", ok and rk == 2 * L, f"rank {rk}")

# L3: Kuchar form K_x = P_x + h_x(X, matter): brackets independent of the clock momenta; curvature formula
Xs = sp.symbols("X0:3"); Ps = sp.symbols("P0:3"); fz, pz_ = sp.symbols("fz pz_")
hs = [Xs[0] * fz**2 + pz_ * Xs[1], Xs[1]**2 * pz_ + fz * Xs[2], fz * pz_ * Xs[0] * Xs[2]]
Ks = [Ps[i] + hs[i] for i in range(3)]
Qa, Pa = list(Xs) + [fz], list(Ps) + [pz_]
ok = True
for i in range(3):
    for j in range(3):
        br = pb_canon(Ks[i], Ks[j], Qa, Pa)
        ok &= not any(br.has(pp) for pp in Ps)
        Fij = sp.diff(hs[i], Xs[j]) - sp.diff(hs[j], Xs[i]) + pb_canon(hs[i], hs[j], [fz], [pz_])
        ok &= sp.expand(br - Fij) == 0
check("L3 Kuchar form: {K_x,K_y} = d_{X_y} h_x - d_{X_x} h_y + {h_x,h_y} is clock-momentum free "
      "(weak = strong vanishing; first class <=> zero curvature)", ok)

# L4a: recombination with the ruler, C_x = g_x K_x, K abelian (matter plus u-gradient):
#      {C_x, C_y} = Delta_xy (g_y/g_x) C_x - Delta_yx (g_x/g_y) C_y, written polynomially as D_xy g_y K_x - D_yx g_x K_y
for L, dname, d in [(5, "central", CEN), (5, "forward", FWD), (4, "generic circulant", {r: sp.Symbol(f"e{r}") for r in range(4)})]:
    D = circ(L, d)
    u = sp.symbols(f"u0:{L}"); Pi = sp.symbols(f"Pi0:{L}"); f = sp.symbols(f"f0:{L}"); pf = sp.symbols(f"pf0:{L}")
    g = [1 + sum(D[i, j] * u[j] for j in range(L)) for i in range(L)]
    W = sum(u[i]**2 * u[(i + 1) % L] for i in range(L))
    K = [Pi[i] + pf[i]**2 / 2 + f[i]**2 + sp.diff(W, u[i]) for i in range(L)]
    Qv, Pv = list(u) + list(f), list(Pi) + list(pf)
    okab = all(pb_canon(K[i], K[j], Qv, Pv) == 0 for i in range(L) for j in range(L))
    C = [sp.expand(g[i] * K[i]) for i in range(L)]
    ok = all(sp.expand(pb_canon(C[i], C[j], Qv, Pv) - (D[i, j] * g[j] * K[i] - D[j, i] * g[i] * K[j])) == 0
             for i in range(L) for j in range(L))
    check(f"L4a L={L} {dname}: K abelian and {{g_x K_x, g_y K_y}} = D_xy (g_y/g_x) C_x - D_yx (g_x/g_y) C_y strongly", okab and ok)

# L4b: zeroth-order constants at g = 1: cbar(m,n) = lam_n - lam_m, Lambda_n = lam_n; (S) holds; central Lam2/Lam1 = w + 1/w
for L in range(4, 10):
    okS = True
    for d in (CEN, FWD):
        Dm = circ(L, d)
        for m_ in range(L):
            for n_ in range(L):
                # coefficient of C_z in {C_m, C_n}, C_m = sum_x w^(m x) C_x, computed from the matrix entries of the L4
                # Poisson form at g = 1, {C_x, C_y} = D_xy C_x - D_yx C_y; it must equal cbar(m,n) w^((m+n) z)
                for z_ in (0, 1):
                    cz = sum(w**((m_ * z_ + n_ * y_) % L) * Dm[z_, y_] for y_ in range(L)) - \
                         sum(w**((m_ * x_ + n_ * z_) % L) * Dm[z_, x_] for x_ in range(L))
                    okS &= cyclo_zero(cz - (lam(n_, d, L) - lam(m_, d, L)) * w**(((m_ + n_) * z_) % L), L)
        okS &= (not cyclo_zero(lam(1, d, L), L)) and (not cyclo_zero(lam(1, d, L) - lam(L - 1, d, L), L))
    okS &= cyclo_zero(lam(2, CEN, L) - (w + w**(L - 1)) * lam(1, CEN, L), L)
    check(f"L4b L={L}: cbar(m,n) = lam_n - lam_m, Lambda_n = +lam_n, (S) holds (central, forward); central Lam2/Lam1 = 2cos(2pi/L)", okS)

# ================================================================== Part A
section("Part A: Model A (one clock pair, no local degrees of freedom)")
for L in (4, 5):
    t = time.time()
    M = modelA_ring(L, {r: sp.Symbol(f"c{r}") for r in range(L)})       # fully general circulant
    Dg = M["D"]
    pbA = lambda F, G: pb_ring(F, G, M["Q"], M["Pm"])
    okHD = all(M["H"][i] - M["Cp"][i] - M["Cm"][i] == 0 and M["Dd"][i] - M["Cp"][i] + M["Cm"][i] == 0 for i in range(L))
    ok = True
    for i in range(L):
        for j in range(L):
            A_ij = Dg[i][j] - Dg[j][i]; S_ij = Dg[i][j] + Dg[j][i]
            ok &= pbA(M["Cp"][i], M["Cp"][j]) - A_ij * (M["l"][i] * M["m"][j] + M["m"][i] * M["l"][j]) / 8 == 0
            ok &= pbA(M["Cm"][i], M["Cm"][j]) + A_ij * (M["n"][i] * M["k"][j] + M["k"][i] * M["n"][j]) / 8 == 0
            ok &= pbA(M["Cp"][i], M["Cm"][j]) - S_ij * (M["l"][i] * M["k"][j] + M["m"][i] * M["n"][j]) / 8 == 0
    check(f"A-br L={L} general circulant: H = C+ + C-, D = C+ - C-; {{C+,C+}} = A(lm'+ml')/8, {{C-,C-}} = -A(nk'+kn')/8, "
          f"{{C+x,C-y}} = S_xy(l_x k_y + m_x n_y)/8", okHD and ok, f"({time.time() - t:.0f}s)")



def antisym(L):
    """fully general antisymmetric circulant on Z_L (d(L/2) = 0 is forced at even L)."""
    dd = {}
    for r in range(1, (L - 1) // 2 + 1):
        s_ = sp.Symbol(f"s{r}")
        dd[r] = s_; dd[-r] = -s_
    return dd


for L in range(4, 9):
    dd = antisym(L)
    lab = f"general antisymmetric circulant ({(L - 1) // 2} parameters" + ("; includes SLAC)" if L % 2 else ")")
    t = time.time()
    M = modelA_ring(L, dd)
    D = M["D"]
    pbA = lambda F, G: pb_ring(F, G, M["Q"], M["Pm"])
    ok = True
    for i in range(L):
        for j in range(L):
            ok &= pbA(M["Cp"][i], M["Cm"][j]) == 0
            lhs = pbA(M["Cp"][i], M["Cp"][j]) * M["m"][i] * M["m"][j]
            ok &= lhs - D[i][j] * (M["m"][j]**2 * M["Cp"][i] + M["m"][i]**2 * M["Cp"][j]) == 0
            lhs = pbA(M["Cm"][i], M["Cm"][j]) * M["n"][i] * M["n"][j]
            ok &= lhs + D[i][j] * (M["n"][j]**2 * M["Cm"][i] + M["n"][i]**2 * M["Cm"][j]) == 0
    check(f"A1 L={L} {lab}: {{C+,C-}} = 0, {{C+x,C+y}} = D_xy((m_y/m_x)C+x + (m_x/m_y)C+y), "
          f"{{C-x,C-y}} = -D_xy((n_y/n_x)C-x + (n_x/n_y)C-y) strongly on U", ok, f"({time.time() - t:.0f}s)")
M = modelA_ring(5, FWD)
okc = any(pb_ring(M["Cp"][i], M["Cm"][j], M["Q"], M["Pm"]) != 0 for i in range(5) for j in range(5))
check("A1-control L=5 forward (not antisymmetric): {C+,C-} != 0, so A1 needs S = 0", okc)

# Sigma cap U is non-empty in the periodic sector, but there sum m = sum n = 0 (uniform m, n need winding)
L = 5
M = modelA(L, circ(L, CEN))
sol = sp.solve(M["l"] + M["k"], M["p"] + M["P"], dict=True)[0]
vals = {v: r for v, r in zip(M["f"] + M["X"], [3, -1, 4, 1, -5, 9, 2, -6, 5, 8])}
mv = [sp.expand(M["m"][i].subs(sol).subs(vals)) for i in range(L)]
nv = [sp.expand(M["n"][i].subs(sol).subs(vals)) for i in range(L)]
summ = sp.expand(sum(M["m"]).subs(sol)); sumn = sp.expand(sum(M["n"]).subs(sol))
check("A1-U L=5 central: Sigma cap U non-empty (explicit point with all m_x, n_x != 0); on {l=k=0} in the periodic "
      "sector sum m = sum n = 0, so a uniform background needs winding of phi -/+ X",
      all(v != 0 for v in mv + nv) and summ == 0 and sumn == 0, f"m={mv}, n={nv}")

# A5: uniform background m = mb, n = nb: Dirac algebra with delta' -> Delta, on shell
mb, nb = sp.symbols("mb nb")
D = circ(L, AS2)
cp = sp.symbols(f"cp0:{L}"); cm = sp.symbols(f"cm0:{L}")
sfp = lambda i, j: D[i, j] * (cp[i] + cp[j])          # m uniform: m_y/m_x = 1
sfm = lambda i, j: -D[i, j] * (cm[i] + cm[j])
Hs = [cp[i] + cm[i] for i in range(L)]; Ds = [cp[i] - cm[i] for i in range(L)]
ok = True
for i in range(L):
    for j in range(L):
        HH = sfp(i, j) + sfm(i, j)                      # {C+ + C-, C+ + C-}
        DH = sfp(i, j) - sfm(i, j)                      # {C+ - C-, C+ + C-}
        DD = sfp(i, j) + sfm(i, j)
        ok &= sp.expand(HH - D[i, j] * (Ds[i] + Ds[j])) == 0 and sp.expand(DH - D[i, j] * (Hs[i] + Hs[j])) == 0
        ok &= sp.expand(DD - D[i, j] * (Ds[i] + Ds[j])) == 0
check("A5 L=5 any antisymmetric Delta, uniform background: {H_x,H_y} ~ D_xy(D_x+D_y), {D_x,H_y} ~ D_xy(H_x+H_y), "
      "{D_x,D_y} ~ D_xy(D_x+D_y) (Dirac algebra with delta' -> Delta)", ok)
# Fourier: {D_0, H_n} ~ lam_n H_n and {H_1, H_-1} ~ (lam_-1 - lam_1) D_0, from the A5 structure functions
okF = True
for L in range(5, 9):
    Dm = circ(L, CEN)
    for m_ in range(L):
        for z_ in (0, 1):
            # coefficient of H_z in {D_0, H_m} = sum_{x,y} w^(m y) Delta_xy (H_x + H_y), from the matrix entries;
            # it must equal lam_m w^(m z)
            c = sum(w**((m_ * y_) % L) * Dm[z_, y_] for y_ in range(L)) + w**((m_ * z_) % L) * sum(Dm[x_, z_] for x_ in range(L))
            okF &= cyclo_zero(c - lam(m_, CEN, L) * w**((m_ * z_) % L), L)
    for z_ in (0, 1):
        # coefficient of D_z in {H_1, H_-1} = sum_{x,y} w^(x - y) Delta_xy (D_x + D_y); it must be z-independent (D_0 only)
        c11 = w**z_ * sum(w**((-y_) % L) * Dm[z_, y_] for y_ in range(L)) + \
              w**((-z_) % L) * sum(w**x_ * Dm[x_, z_] for x_ in range(L))
        okF &= cyclo_zero(c11 - (lam(L - 1, CEN, L) - lam(1, CEN, L)), L)
    okF &= not cyclo_zero(lam(L - 1, CEN, L) - lam(1, CEN, L), L)
    okF &= cyclo_zero(lam(2, CEN, L) - (w + w**(L - 1)) * lam(1, CEN, L), L)
check("A5-F central L=5-8: Lambda_n = lam_n, {H_1,H_-1} ~ (lam_-1 - lam_1) D_0 != 0, Lam2/Lam1 = 2cos(2pi/L)", okF)


# A3: kink rule on the components of Sigma
def component(M, sp_, sm):
    eqs = [(M["l"][i] if sp_[i] == 0 else M["m"][i]) for i in range(len(sp_))] + \
          [(M["n"][i] if sm[i] == 0 else M["k"][i]) for i in range(len(sm))]
    others = [(M["m"][i] if sp_[i] == 0 else M["l"][i]) for i in range(len(sp_))] + \
             [(M["k"][i] if sm[i] == 0 else M["n"][i]) for i in range(len(sm))]
    sol = sp.solve(eqs, M["Q"] + M["Pm"], dict=True)[0]
    return eqs, others, sol


L = 4
D = circ(L, CEN); A_ = D - D.T
M = modelA(L, D)
pbA = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
eqs, others, sol = component(M, (0, 1, 0, 0), (1, 1, 1, 1))    # (l, m, l, l | k, k, k, k): C+ kinks at bonds 01, 12
b01 = sp.expand(pbA(M["Cp"][0], M["Cp"][1]).subs(sol))
pred = sp.expand((A_[0, 1] * M["m"][0] * M["l"][1] / 8).subs(sol))
bad = sorted({(i, j) for i in range(2 * L) for j in range(i + 1, 2 * L)
              if sp.expand(pbA((M["Cp"] + M["Cm"])[i], (M["Cp"] + M["Cm"])[j]).subs(sol)) != 0})
check("A3-kink central L=4, component (l,m,l,l | k,k,k,k): {C+_0,C+_1} = A_01 m_0 l_1/8, not identically 0; "
      "the only non-vanishing brackets are C+ at the kink bonds", b01 == pred and b01 != 0 and bad == [(0, 1), (1, 2)],
      f"{{C+_0,C+_1}}|comp = {sp.factor(b01)}; non-zero pairs {bad}")
L = 5
D = circ(L, CEN); A_ = D - D.T
M = modelA(L, D)
pbA = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
eqs, others, sol = component(M, (0,) * 5, (1, 1, 0, 1, 1))     # C- kink: k,k,n,k,k
b12 = sp.expand(pbA(M["Cm"][1], M["Cm"][2]).subs(sol))
check("A3-kink central L=5, C- kink (k,k,n,k,k): {C-_1,C-_2} = -A_12 n_1 k_2/8 != 0 (mirrored kink form)",
      b12 != 0 and sp.expand(b12 + (A_[1, 2] * M["n"][1] * M["k"][2] / 8).subs(sol)) == 0)
D = circ(L, FWD); S_ = D + D.T
M = modelA(L, D)
pbA = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
eqs, others, sol = component(M, (0,) * 5, (1,) * 5)             # forward regular (l,k) branch
b01 = sp.expand(pbA(M["Cp"][0], M["Cm"][1]).subs(sol))
check("A3-fwd L=5 forward, regular uniform (l,k) branch: {C+_0,C-_1} = S_01 m_0 n_1/8 != 0 (anomalous)",
      b01 != 0 and sp.expand(b01 - (S_[0, 1] * M["m"][0] * M["n"][1] / 8).subs(sol)) == 0)


def branch_scan(L, D):
    M = modelA(L, D)
    pbA = lambda F, G: pb_canon(F, G, M["Q"], M["Pm"])
    allC = M["Cp"] + M["Cm"]
    BR = [[pbA(allC[i], allC[j]) for j in range(2 * L)] for i in range(2 * L)]
    A_ = D - D.T; S_ = D + D.T
    allv = M["Q"] + M["Pm"]
    out, agree = [], True
    for sp_ in itertools.product([0, 1], repeat=L):
        for sm in itertools.product([0, 1], repeat=L):
            eqs, others, sol = component(M, sp_, sm)
            Jr = sp.Matrix([[sp.diff(e, v) for v in allv] for e in eqs]).rank()
            nondeg = all(sp.expand(o.subs(sol)) != 0 for o in others)
            fc = all(sp.expand(BR[i][j].subs(sol)) == 0 for i in range(2 * L) for j in range(i + 1, 2 * L))
            pred = True
            for i in range(L):
                for j in range(L):
                    if A_[i, j] != 0 and (sp_[i] != sp_[j] or sm[i] != sm[j]): pred = False
                    if S_[i, j] != 0 and sp_[i] != sm[j]: pred = False
            if nondeg: agree &= (pred == fc)
            tag = ("l" if all(v == 0 for v in sp_) else "m" if all(v == 1 for v in sp_) else "mix") + \
                  ("n" if all(v == 0 for v in sm) else "k" if all(v == 1 for v in sm) else "mix")
            out.append((tag, fc, nondeg, Jr))
    return out, agree


if SLOW:
    for L, dn, d in [(4, "central", CEN), (4, "forward", FWD), (5, "central", CEN), (5, "forward", FWD)]:
        t = time.time()
        out, agree = branch_scan(L, circ(L, d))
        fc_nd = sorted({f"{tg}(rank {r})" for tg, fc, nd, r in out if fc and nd})
        ndeg = sum(1 for o in out if o[2]); nfc_deg = sum(1 for o in out if o[1] and not o[2])
        rkr = 2 * L - (2 if (dn == "central" and L % 2 == 0) else 1)
        expect = ({f"ln(rank {rkr})", f"mk(rank {rkr})", f"lk(rank {2 * L})", f"mn(rank {2 * L})"} if dn == "central"
                  else {f"ln(rank {rkr})", f"mk(rank {rkr})"})
        check(f"A3-census L={L} {dn}: kink rule decides all {ndeg} non-degenerate components; first-class ones = {fc_nd}",
              agree and set(fc_nd) == expect, f"degenerate first-class pieces: {nfc_deg} ({time.time() - t:.0f}s)")

# ================================================================== Part P
section("Part P: Model P (lattice parametrised field theory, two embedding pairs)")


def modelP(L, D):
    f = sp.symbols(f"f0:{L}"); p_ = sp.symbols(f"p0:{L}")
    up = sp.symbols(f"up0:{L}"); Pp = sp.symbols(f"Pp0:{L}"); um = sp.symbols(f"um0:{L}"); Pm = sp.symbols(f"Pm0:{L}")
    Df = [sum(D[i, j] * f[j] for j in range(L)) for i in range(L)]
    gp = [1 + sum(D[i, j] * up[j] for j in range(L)) for i in range(L)]
    gm = [1 + sum(D[i, j] * um[j] for j in range(L)) for i in range(L)]
    a = [sp.expand(p_[i] + Df[i]) for i in range(L)]; b = [sp.expand(p_[i] - Df[i]) for i in range(L)]
    Cp = [sp.expand(Pp[i] * gp[i] + a[i]**2 / 4) for i in range(L)]
    Cm = [sp.expand(Pm[i] * gm[i] - b[i]**2 / 4) for i in range(L)]
    return dict(f=f, p=p_, up=up, Pp=Pp, um=um, Pm=Pm, a=a, b=b, gp=gp, gm=gm, Cp=Cp, Cm=Cm,
                Q=list(f) + list(up) + list(um), P=list(p_) + list(Pp) + list(Pm))


for L, dn, d in [(5, "central", CEN), (5, "forward", FWD), (5, "antisymmetric range 2", AS2)]:
    D = circ(L, d)
    M = modelP(L, D)
    pbP = lambda F, G: pb_canon(F, G, M["Q"], M["P"])
    A_ = D - D.T; S_ = D + D.T
    ok = True
    for i in range(L):
        for j in range(L):
            e = pbP(M["Cp"][i], M["Cp"][j]) - (D[i, j] * M["Pp"][i] * M["gp"][j] - D[j, i] * M["gp"][i] * M["Pp"][j]
                                               + A_[i, j] * M["a"][i] * M["a"][j] / 4)
            ok &= sp.expand(e) == 0
            ok &= sp.expand(pbP(M["Cp"][i], M["Cm"][j]) + S_[i, j] * M["a"][i] * M["b"][j] / 4) == 0
    check(f"P1 L={L} {dn}: {{C+x,C+y}} = D_xy Pi+_x g_y - D_yx g_x Pi+_y + A_xy a_x a_y/4, {{C+x,C-y}} = -S_xy a_x b_y/4 (strong)", ok)
    if dn != "forward":
        onsh = {M["Pp"][i]: -M["a"][i]**2 / (4 * M["gp"][i]) for i in range(L)}
        ok = True
        for i in range(L):
            for j in range(i + 1, L):
                wk = pbP(M["Cp"][i], M["Cp"][j]).subs(onsh)
                pr = -D[i, j] * (M["a"][i] * M["gp"][j] - M["a"][j] * M["gp"][i])**2 / (4 * M["gp"][i] * M["gp"][j])
                ok &= sp.cancel(sp.together(wk - pr)) == 0
        check(f"P2 L={L} {dn}: on shell {{C+x,C+y}} = -D_xy (a_x g_y - a_y g_x)^2/(4 g_x g_y) (perfect-square anomaly)", ok)
    # rational point of Sigma: values r/7, r cycling 1,-2,3,5,-1,4,2 over (phi, pi, u+, u-) in that order; Pi+- on shell
    cyc = itertools.cycle([1, -2, 3, 5, -1, 4, 2])
    vals = {s: sp.Rational(next(cyc), 7) for s in list(M["f"]) + list(M["p"]) + list(M["up"]) + list(M["um"])}
    if dn.startswith("antisymmetric"):
        vals.update({d1: sp.Rational(2, 3), d2: -sp.Rational(1, 12)})
    gpv = [sp.sympify(gg).subs(vals) for gg in M["gp"]]; gmv = [sp.sympify(gg).subs(vals) for gg in M["gm"]]
    av = [t.subs(vals) for t in M["a"]]; bv = [t.subs(vals) for t in M["b"]]
    vals.update({M["Pp"][i]: -av[i]**2 / (4 * gpv[i]) for i in range(L)})
    vals.update({M["Pm"][i]: bv[i]**2 / (4 * gmv[i]) for i in range(L)})
    onS = all(c.subs(vals) == 0 for c in M["Cp"] + M["Cm"]) and all(gg != 0 for gg in gpv + gmv)
    H = [M["Cp"][i] - M["Cm"][i] for i in range(L)]
    hb = pbP(H[0], H[1]).subs(vals)
    expect = {"central": sp.Rational(34583, 570752), "forward": sp.Rational(3, 784),
              "antisymmetric range 2": sp.Rational(2591839, 24618825)}[dn]
    extra = " (d1 = 2/3, d2 = -1/12)" if dn.startswith("antisymmetric") else ""
    check(f"P3 L={L} {dn}{extra}: rational point of Sigma (all g != 0) with {{H_0,H_1}} = {hb} != 0: not first class",
          onS and hb == expect and hb != 0, f"expected {expect}")

# Hand proof, witnessed: for every antisymmetric Delta != 0, at u+- = 0, phi = 0, pi = e_0 (on shell),
# {C+_0, C+_y} = -Delta_0y/4 and {C+, C-} = 0. Symbolic general antisymmetric circulant at L = 5, 6, 7.
for L in (5, 6, 7):
    dsy = sp.symbols(f"s1:{L // 2 + 1}")
    dd = {}
    for r in range(1, L // 2 + 1):
        if 2 * r == L: continue                          # antisymmetry forces d(L/2) = 0
        dd[r] = dsy[r - 1]; dd[-r] = -dsy[r - 1]
    D = circ(L, dd)
    M = modelP(L, D)
    pbP = lambda F, G: pb_canon(F, G, M["Q"], M["P"])
    vals = {s: 0 for s in list(M["f"]) + list(M["up"]) + list(M["um"])}
    vals.update({M["p"][i]: (1 if i == 0 else 0) for i in range(L)})
    av = [t.subs(vals) for t in M["a"]]; bv = [t.subs(vals) for t in M["b"]]
    vals.update({M["Pp"][i]: -av[i]**2 / 4 for i in range(L)}); vals.update({M["Pm"][i]: bv[i]**2 / 4 for i in range(L)})
    onS = all(sp.expand(c.subs(vals)) == 0 for c in M["Cp"] + M["Cm"])
    ok = all(sp.expand(pbP(M["Cp"][0], M["Cp"][j]).subs(vals) + D[0, j] / 4) == 0 for j in range(1, L))
    ok &= all(pbP(M["Cp"][i], M["Cm"][j]) == 0 for i in range(L) for j in range(L))
    check(f"P-hand L={L} general antisymmetric circulant: at u = phi = 0, pi = e_0 on Sigma, {{C+_0,C+_y}} = -Delta_0y/4 "
          f"and {{C+,C-}} = 0: anomalous whenever Delta != 0", onS and ok)

# P4a: Kuchar density of the naive C+ (diagonal coefficient alpha = g): h = a^2/(4g); curvature and anomaly relation
for L, dd, lab in [(5, CEN, "central"), (5, AS2, "general antisymmetric"), (6, CEN, "central")]:
    D = circ(L, dd)
    a = sp.symbols(f"a0:{L}"); G = sp.symbols(f"G0:{L}")       # G_x = g_x as symbols; d/du_y = sum_z Delta_zy d/dG_z
    pa = lambda F, H_: sp.expand(sum(2 * D[i, j] * sp.diff(F, a[i]) * sp.diff(H_, a[j]) for i in range(L) for j in range(L) if D[i, j] != 0))
    du = lambda F, yy: sum(D[zz, yy] * sp.diff(F, G[zz]) for zz in range(L) if D[zz, yy] != 0)
    h = [a[i]**2 / (4 * G[i]) for i in range(L)]
    ok = okrel = True
    for i in range(L):
        for j in range(i + 1, L):
            F = du(h[i], j) - du(h[j], i) + pa(h[i], h[j])
            v_i, v_j = a[i] / G[i], a[j] / G[j]
            ok &= sp.expand((F + D[i, j] * (v_i - v_j)**2 / 4) * 4 * G[i]**2 * G[j]**2) == 0
            anom = -D[i, j] * (a[i] * G[j] - a[j] * G[i])**2 / (4 * G[i] * G[j])
            okrel &= sp.cancel(sp.together(anom - G[i] * G[j] * F)) == 0
    check(f"P4a L={L} {lab}: h = a^2/(4g) has F_xy = -D_xy (v_x - v_y)^2/4, v = a/g; on-shell anomaly = g_x g_y F_xy", ok and okrel)

# ================================================================== Part J
section("Part J: finite-range Kuchar densities at the ruler (central Delta, chiral bracket {a_x,a_y} = 2 Delta_xy)")


def Dl_factory(L, d):
    def Dl(i, j):
        r = (j - i) % L
        if r > L // 2: r -= L
        return d.get(r, 0)
    return Dl


def class1(Ra, Rg, d=CEN):
    """h_x = sum k_rst a_{x+r} a_{x+s}/g_{x+t}: exact flatness; returns True iff only h = 0 is flat."""
    rd = max(abs(k) for k in d)
    span = 2 * Ra + Rg + 2 * rd + 2
    L = 2 * span + 3
    Dl = Dl_factory(L, d)
    a = sp.symbols(f"a0:{L}"); g = sp.symbols(f"g0:{L}")
    pairs = [(r, s) for r in range(-Ra, Ra + 1) for s in range(r, Ra + 1)]
    kap = {(r, s, t): sp.Symbol(f"k{r}_{s}_{t}".replace("-", "m")) for (r, s) in pairs for t in range(-Rg, Rg + 1)}
    h = lambda xx: sum(v * a[(xx + r) % L] * a[(xx + s) % L] / g[(xx + t) % L] for (r, s, t), v in kap.items())
    pba = lambda F, G: sum(2 * Dl(i, j) * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L) if Dl(i, j) != 0)
    du = lambda F, yy: sum(Dl(zz, yy) * sp.diff(F, g[zz]) for zz in range(L) if Dl(zz, yy) != 0)
    eqs = set(); h0 = h(0)
    for yy in range(1, span + 1):
        num = sp.expand(sp.fraction(sp.together(du(h0, yy) - du(h(yy), 0) + pba(h0, h(yy))))[0])
        if num == 0: continue
        eqs.update(sp.expand(c) for c in sp.Poly(num, *[v for v in list(a) + list(g) if num.has(v)]).coeffs())
    sol = sp.solve(list(eqs), list(kap.values()), dict=True)
    return (len(sol) >= 1 and all(all(v == 0 for v in s.values()) for s in sol)), len(kap), L


def jet_cert(Ra, Rw, N, mode, d=CEN):
    """h_x = sum_{r<=s in a-window} c_rs(w) a_{x+r} a_{x+s}, c_rs a Taylor polynomial of degree N in the window variables.
    mode 'g'    : variables e_t = g_{x+t} - 1 (X+ enters only via g = 1 + Delta u); d/du_y by the chain rule
    mode 'shift': variables u_{x+t}, with shift invariance sum_t d/du_{x+t} h_x = 0 imposed
    mode 'u'    : variables u_{x+t}, no shift invariance (control)
    Flatness F_0y = 0 through order N-1 at the ruler u = 0 (complete for C^N coefficient germs);
    normalisation h(a = 1, u = 0) = sum c_rs(0) != 0 (Rabinowitsch variable tt). Returns True iff Groebner basis = [1]."""
    rd = max(abs(k) for k in d)
    A0, A1 = (-Ra, Ra) if isinstance(Ra, int) else Ra
    W0, W1 = (-Rw, Rw) if isinstance(Rw, int) else Rw
    span = 2 * (A1 - A0) + (W1 - W0) + 2 * rd + 4 + max(abs(A0), abs(A1), abs(W0), abs(W1))
    L = 2 * span + 3                                   # ring large enough that no bracket wraps: equivalent to Z
    Dl = Dl_factory(L, d)
    a = sp.symbols(f"a0:{L}"); e = sp.symbols(f"e0:{L}")
    pairs = [(r, s) for r in range(A0, A1 + 1) for s in range(r, A1 + 1)]
    ts = list(range(W0, W1 + 1))
    mons = [c for k in range(N + 1) for c in itertools.combinations_with_replacement(ts, k)]
    kap = {(r, s, c): sp.Symbol("k_%d_%d_" % (r, s) + "_".join(map(str, c)) + "_%d" % len(c)) for (r, s) in pairs for c in mons}
    unk = list(kap.values()); tt = sp.Symbol("tt")

    def h(xx):
        return sp.expand(sum(v * sp.prod([e[(xx + t) % L] for t in c]) * a[(xx + r) % L] * a[(xx + s) % L]
                             for (r, s, c), v in kap.items()))

    def pba(F, G):
        return sp.expand(sum(2 * Dl(i, j) * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L) if Dl(i, j) != 0))

    def du(F, yy):
        if mode == "g":
            return sp.expand(sum(Dl(zz, yy) * sp.diff(F, e[zz]) for zz in range(L) if Dl(zz, yy) != 0))
        return sp.expand(sp.diff(F, e[yy]))

    def trunc(F, nmax):
        if F == 0: return F
        pP = sp.Poly(F, *e)
        return sp.expand(sum(cf * sp.prod([v**kk for v, kk in zip(e, mon)]) for mon, cf in pP.terms() if sum(mon) <= nmax))

    eqs = set()
    h0 = h(0)
    for yy in range(1, span + 1):
        F = trunc(du(h0, yy) - du(h(yy), 0) + pba(h0, h(yy)), N - 1)
        if F == 0: continue
        gens = [v for v in list(a) + list(e) if F.has(v)]
        eqs.update(sp.expand(cf) for cf in sp.Poly(F, *gens).coeffs())
    if mode == "shift":
        sh = sp.expand(sum(sp.diff(h0, e[yy % L]) for yy in ts))
        if sh != 0:
            eqs.update(sp.Poly(sh, *[v for v in list(a) + list(e) if sh.has(v)]).coeffs())
    eqs.discard(0)
    norm = tt * sum(v for (r, s, c), v in kap.items() if len(c) == 0) - 1
    G = sp.groebner(list(eqs) + [norm], *(unk + [tt]), order="grevlex", domain=QQ)
    return list(G.exprs) == [1], len(unk), len(eqs), L


def run_jet(label, Ra, Rw, N, mode, expect_empty):
    t = time.time()
    empty, nu, ne, L = jet_cert(Ra, Rw, N, mode)
    what = "no flat C^N germ with h(1,0) != 0" if expect_empty else "flat jets exist (consistent over C)"
    check(f"{label} mode={mode} a-window={Ra} var-window={Rw} N={N}: {what}", empty == expect_empty,
          f"(ring L={L}, {nu} unknowns, {ne} eqs, Groebner {'[1]' if empty else 'non-trivial'}, {time.time() - t:.0f}s)")


for Ra, Rg in [(1, 0), (1, 1)]:
    t = time.time()
    ok, nk, Lr = class1(Ra, Rg)
    check(f"P4b rational class h = sum k a a/g_(x+t), Ra={Ra} Rg={Rg}: the only flat member is h = 0", ok,
          f"(ring L={Lr}, {nk} unknowns, {time.time() - t:.0f}s)")
run_jet("P5a obstruction", 0, 0, 2, "g", True)
run_jet("P5b obstruction", 1, 0, 2, "g", True)
run_jet("P5c control (order 0 only)", 1, 1, 1, "g", False)
run_jet("P5e control (order 0 only)", 1, 1, 1, "shift", False)
run_jet("P5f obstruction", 1, 1, 2, "shift", True)
run_jet("P5h obstruction (one-sided u-window, through order 2)", (0, 0), (-2, 0), 3, "shift", True)
run_jet("P5i obstruction", (0, 0), (-2, 2), 2, "shift", True)
run_jet("P5j obstruction", (0, 1), (-2, 0), 2, "shift", True)
run_jet("P5d obstruction", 1, 1, 2, "g", True)
run_jet("P5g control (no shift invariance)", 1, 1, 2, "u", False)
if SLOW:
    run_jet("P5m (1,2) shift-invariant, consistent", 1, 2, 2, "shift", False)

# ================================================================== Part G
section("Part G: staggered flat density (range 1, 2Z-covariant only)")
for L in ([4, 6, 8] if SLOW else [4, 6]):
    a = sp.symbols(f"a0:{L}"); u = sp.symbols(f"u0:{L}")
    Dl = Dl_factory(L, CEN)
    pa = lambda F, G: sp.expand(sum(2 * Dl(i, j) * sp.diff(F, a[i]) * sp.diff(G, a[j]) for i in range(L) for j in range(L) if Dl(i, j) != 0))

    def stag(eps):
        return [a[xx]**2 / 4 if xx % 2 else
                (a[xx] + eps * (u[(xx + 1) % L] * a[(xx + 1) % L] - u[(xx - 1) % L] * a[(xx - 1) % L]) / 2)**2 / 4 for xx in range(L)]

    res = {}
    for eps in (-1, 1):
        h = stag(eps)
        res[eps] = all(sp.expand(sp.diff(h[i], u[j]) - sp.diff(h[j], u[i]) + pa(h[i], h[j])) == 0
                       for i in range(L) for j in range(i + 1, L))
    h = stag(-1)
    c = sp.Symbol("c")
    shift_inv = all(sp.expand(h[i].subs({u[j]: u[j] + c for j in range(L)}, simultaneous=True) - h[i]) == 0 for i in range(L))
    A = sp.Symbol("A")
    sub = {a[j]: A for j in range(L)}
    lin = [sp.expand(sum(sp.diff(h[i].subs(sub), u[j]).subs({uu: 0 for uu in u}) * u[j] for j in range(L))) for i in (0, 1)]
    e0 = (u[1] - u[L - 1]) / 2
    check(f"G L={L}: staggered h flat exactly (eps = -1), opposite sign not flat (control), not shift invariant; "
          f"uniform-a linear u-response -A^2 e/2 (even), 0 (odd) against continuum -A^2 e/4",
          res[-1] and not res[1] and not shift_inv and sp.expand(lin[0] + A**2 * e0 / 2) == 0 and lin[1] == 0,
          f"even={lin[0]}, odd={lin[1]}")

# ================================================================== Part K
section("Part K: deparametrised clocks (P6)")


def lemD(L, R, d):
    D = circ(L, d)
    f = sp.symbols(f"f0:{L}"); p_ = sp.symbols(f"p0:{L}")
    Df = [sum(D[i, j] * f[j] for j in range(L)) for i in range(L)]
    H0 = sp.expand(sum(p_[i]**2 + Df[i]**2 for i in range(L)) / 2)
    win = list(range(-R, R + 1))
    zz = lambda xx: [f[(xx + i) % L] for i in win] + [p_[(xx + i) % L] for i in win]
    n = 2 * len(win)
    c = {(i, j): sp.Symbol(f"c{i}_{j}") for i in range(n) for j in range(i, n)}
    h = lambda xx: sum(v * zz(xx)[i] * zz(xx)[j] for (i, j), v in c.items())
    allv = list(f) + list(p_)
    eqs = sp.Poly(sp.expand(sum(h(xx) for xx in range(L)) - H0), *allv).coeffs()
    eqs += sp.Poly(pb_canon(h(0), H0, f, p_), *allv).coeffs()
    return sp.linsolve(eqs, list(c.values())) == sp.EmptySet, len(c)


cases = [(7, 1, "central", CEN), (7, 1, "forward", FWD)]
if SLOW:
    cases += [(8, 1, "central", CEN), (9, 2, "central", CEN), (9, 2, "forward", FWD)]
for L, R, dn, d in cases:
    t = time.time()
    ok, nc = lemD(L, R, d)
    check(f"P6 L={L} R={R} {dn}: no translation-covariant range-R quadratic h with sum_x h_x = H0 and {{h_0,H0}} = 0",
          ok, f"({nc} unknowns, {time.time() - t:.0f}s)")
# control: dropping {h_0, H0} = 0, the density h = (pi^2 + (Dphi)^2)/2 itself solves sum h = H0
L, R = 7, 1
D = circ(L, CEN)
f = sp.symbols(f"f0:{L}"); p_ = sp.symbols(f"p0:{L}")
Df = [sum(D[i, j] * f[j] for j in range(L)) for i in range(L)]
h0 = sp.expand((p_[0]**2 + Df[0]**2) / 2)
H0 = sp.expand(sum(p_[i]**2 + Df[i]**2 for i in range(L)) / 2)
check("P6-control L=7 central: the naive density h_0 = (pi_0^2 + (Dphi)_0^2)/2 has range 1 and sums to H0, but {h_0,H0} != 0",
      pb_canon(h0, H0, f, p_) != 0)

print(f"\n[runtime {time.time() - T0:.1f}s{'; --slow' if SLOW else ''}]")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
