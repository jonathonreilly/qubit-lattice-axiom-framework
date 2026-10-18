#!/usr/bin/env python3
"""Fresh-context reviewer's independent check of C4b D1 (walker cone from {C,C}) and D4 (alpha = K2/4).

Written from scratch; shares no code with the runner's kernel engine (K) or the C4b checker's engine (V).
Route: operator level for the fermion (bilinear brackets {int chibar A chi, int chibar B chi} = -i int chibar [A,B] chi,
which follows from {chi, chibar} = -i), explicit commutators of differential operators acting on a test spinor of
sympy Functions; gravity by explicit functional derivatives (own Euler operator) with symmetric-tensor bracket
{h_ij, P_kl} = (d_ik d_jl + d_il d_jk)/2.  The frame of the metric route E = (delta + a h)^(-1/2) is expanded to first
order by hand: E = delta - a h/2.

Checks:
 R1  {C_f[N], C_f[M]} (flat walker, speed v) = v^2 K[z], z = N grad M - M grad N, K[xi] = int chibar i(L_xi + kap curl xi.sigma) chi,
     with L_xi = xi.d + div(xi)/2 (half-density), kap solved.
 R2  gravity {C[N], C[M]} at order P, C = kin0 - K1 R1, kin0 = (trP^2 + b trP^2)/(4 alpha), R1 = d_i d_j h_ij - lap trh:
     closes on c0 lam1 G1[z], G1[xi] = int P.(d xi + d xi^T), iff b = -1/2, with c0 lam1 = K1/(4 alpha).
 R3  {C_f[N; E(h)], lam1 G1[xi]} + {C_f[N], lam_f K[xi]} = C_f[s1 xi.dN + s2 N div xi] at order chi chibar iff
     a lam1 = lam_f, s1 = -lam_f, s2 = 0, kap = same as R1.
 R4  closure of the lapse bracket on ONE generator G = lam1 G1 + lam_f K with one c0: v^2 = c0 lam_f; with R2, R3:
     v^2 = a K1/(4 alpha).  With B2's K2 = a K1 (taken from the note; two engines), v^2 = K2/(4 alpha); v = 1 => alpha = K2/4.
 R5  analytic cross-check of B2 by covariance (no bracket code): gravity potential K1 R1 + K2 R2 is (K1^2/K2) [sqrt g R]_(1,2)
     on delta + (K2/K1) h (checked symbolically with my own sqrt(g) R from Christoffels), G = lam1 G1 + nu G2 drags
     (lam1/nu) delta + h, so nu = lam1 K2/K1; the walker on delta + a h needs lam_f = a lam1 (R3) and lam_f = nu ({G,G}):
     a = K2/K1.  Only the scaling identity is checked here; B2 itself is not re-derived.
"""
import itertools
import sympy as sp

X = sp.symbols("x0:3", real=True)
R3_ = range(3)
I = sp.I
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
N = sp.Function("N")(*X)
M = sp.Function("M")(*X)
XI = [sp.Function(f"xi{k}")(*X) for k in R3_]
psi = sp.Matrix([sp.Function("p1")(*X), sp.Function("p2")(*X)])
d = lambda f, k: sp.diff(f, X[k])
PASS = []


def check(tag, ok, msg):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {msg}")


def Hop(Nf, E, v=1):
    """H = (v/2){N E_a^j sigma_a, p_j}, p = -i d, acting on a 2-spinor of functions."""
    def act(f):
        out = sp.zeros(2, 1)
        for a in R3_:
            for j in R3_:
                c = Nf * E[a, j]
                out += (-I / 2) * (c * sig[a] * f.applyfunc(lambda t: d(t, j)) + (sig[a] * (c * f)).applyfunc(lambda t: d(t, j)))
        return (v * out).applyfunc(sp.expand)
    return act


def Lhalf(xi, kap):
    """K_xi = xi.d + div(xi)/2 + kap curl(xi).sigma  (generator K[xi] = int chibar i K_xi chi)."""
    div = sum(d(xi[k], k) for k in R3_)
    curl = [d(xi[(c + 2) % 3], (c + 1) % 3) - d(xi[(c + 1) % 3], (c + 2) % 3) for c in R3_]
    def act(f):
        out = sum((xi[k] * f.applyfunc(lambda t: d(t, k)) for k in R3_), sp.zeros(2, 1)) + div / 2 * f
        out += kap * sum((curl[c] * sig[c] * f for c in R3_), sp.zeros(2, 1))
        return out.applyfunc(sp.expand)
    return act


def zero_coeffs(expr_list):
    """all coefficients (in the jet of psi, N, M, xi) of a list of expressions -> list of equations."""
    eqs = []
    for e in expr_list:
        e = sp.expand(e)
        if e == 0:
            continue
        atoms = sorted(e.atoms(sp.Derivative) | {f for f in e.atoms(sp.Function) if isinstance(f, sp.core.function.AppliedUndef)}, key=str)
        syms = [sp.Dummy() for _ in atoms]
        ee = e.xreplace(dict(zip(atoms, syms)))     # top-down: derivatives are replaced whole
        assert not ee.free_symbols & set(X), ee.free_symbols
        P = sp.Poly(ee, *syms)
        eqs += [c for c in P.coeffs()]
    return eqs


E0 = sp.eye(3)
# ------------------------------------------------------------------------------------------------- R1 walker lapse bracket
v, kap, V2 = sp.symbols("v kap V2")


def asolve(eqs, unk):
    """sympy.solve with back-substitution audit (solve can drop parameter-only equations)."""
    sols = sp.solve(eqs, unk, dict=True)
    good = [so for so in sols if all(sp.simplify(sp.sympify(e).subs(so)) == 0 for e in eqs)]
    if not eqs:
        return [{}]
    return good


HN, HM = Hop(N, E0, 1), Hop(M, E0, 1)
comm = (HN(HM(psi)) - HM(HN(psi))).applyfunc(sp.expand)
# {C_f[N], C_f[M]} = -i int chibar [H_N, H_M] chi  ==  V2 K[z] = int chibar i V2 K_z chi   <=>  -i[H_N,H_M] = i V2 K_z
# (walker at speed 1 here; a walker of speed v has bracket v^2 times this)
z = [N * d(M, k) - M * d(N, k) for k in R3_]
res = (-I * comm - I * V2 * Lhalf(z, kap)(psi)).applyfunc(sp.expand)
sk = asolve(zero_coeffs(list(res)), [kap, V2])
res_m = (-I * comm - I * V2 * Lhalf([-t for t in z], kap)(psi)).applyfunc(sp.expand)
sk_m = asolve(zero_coeffs(list(res_m)), [kap, V2])
check("R1", sk == [{kap: I / 4, V2: 1}] and sk_m == [{kap: I / 4, V2: -1}],
      f"flat unit-speed walker {{C_f[N],C_f[M]}} = +1 x K[z], z = N grad M - M grad N, K_xi = L_xi + (i/4) curl xi.sigma: {sk} "
      f"(against -z the coefficient is -1: {sk_m}); a walker of speed v gives v^2 K[z]")
KAP = I / 4

# ------------------------------------------------------------------------------------------------- R2 gravity lapse bracket at order P
pairs = [(i, j) for i in R3_ for j in R3_ if i <= j]
hs = {p: sp.Function(f"h{p[0]}{p[1]}")(*X) for p in pairs}
Ps = {p: sp.Function(f"P{p[0]}{p[1]}")(*X) for p in pairs}
hm = sp.Matrix(3, 3, lambda i, j: hs[(min(i, j), max(i, j))])
Pm = sp.Matrix(3, 3, lambda i, j: Ps[(min(i, j), max(i, j))])
al, K1, K2, b, lam1, lamf, c0, a, s1, s2, nu = sp.symbols("alpha K1 K2 b lam1 lam_f c0 a s1 s2 nu")


def euler(L, u, maxo=3):
    """Euler-Lagrange derivative of int L wrt function u (derivatives up to order maxo)."""
    out = sp.diff(L, u)
    for o in range(1, maxo + 1):
        for al_ in itertools.combinations_with_replacement(R3_, o):
            D = sp.Derivative(u, *[X[k] for k in al_])
            c = sp.diff(L, D)
            if c != 0:
                cc = c
                for k in al_:
                    cc = d(cc, k)
                out += (-1) ** o * cc
    return sp.expand(out)


def dsym(L, field, p):
    """derivative wrt the symmetric component (i,j): off-diagonal components counted twice in tr(.), so divide by 2."""
    i, j = p
    return euler(L, field[p]) / (1 if i == j else 2)


def pb_grav(L1, L2):
    """{int L1, int L2} = int sum_ij (dL1/dh_ij dL2/dP_ij - dL1/dP_ij dL2/dh_ij), symmetric-tensor convention."""
    tot = 0
    for p in pairs:
        mult = 1 if p[0] == p[1] else 2
        tot += mult * (dsym(L1, hs, p) * dsym(L2, Ps, p) - dsym(L1, Ps, p) * dsym(L2, hs, p))
    return sp.expand(tot)


trP = Pm.trace()
kin0 = (sum(Pm[i, j] ** 2 for i in R3_ for j in R3_) + b * trP ** 2) / (4 * al)
trh = hm.trace()
R1 = sum(d(d(hm[i, j], i), j) for i in R3_ for j in R3_) - sum(d(d(trh, k), k) for k in R3_)
CgN = N * (kin0 - K1 * R1)
CgM = M * (kin0 - K1 * R1)
lhsP = pb_grav(CgN, CgM)
G1 = lambda xi: sum(Pm[i, j] * (d(xi[j], i) + d(xi[i], j)) for i in R3_ for j in R3_)
resP = sp.expand(lhsP - c0 * lam1 * G1(z))
# local functional vanishes iff its Euler derivative wrt every P component vanishes
eqP = []
for p in pairs:
    eqP += zero_coeffs([euler(resP, Ps[p])])
sP = asolve(eqP, [b, c0])
check("R2", sP == [{b: -sp.Rational(1, 2), c0: K1 / (4 * al * lam1)}],
      f"gravity {{C[N],C[M]}} at order P = c0 lam1 G1[z] (same z) iff {sP}: b = -1/2, c0 lam1 = K1/(4 alpha)")

# ------------------------------------------------------------------------------------------------- R3 {C,G} at chi chibar with E = delta - a h/2
# {C_f[N; E(h)], lam1 G1[xi]}: G1 moves h_ij by lam1 (d_i xi_j + d_j xi_i); so C_f's frame moves by -a lam1 S_xi (S = sym grad)
S = sp.Matrix(3, 3, lambda i, j: (d(XI[j], i) + d(XI[i], j)) / 2)
dE = -a * lam1 * S
HdE = Hop(N, dE)   # linear in E: the frame variation of the operator
# {C_f[N], lam_f K[xi]} = -i int chibar [H_N, i lam_f K_xi] chi = int chibar lam_f [H_N, K_xi] chi
H0 = Hop(N, E0)
Kx = Lhalf(XI, KAP)
op_lhs = (HdE(psi) + lamf * (H0(Kx(psi)) - Kx(H0(psi)))).applyfunc(sp.expand)
Np = s1 * sum(XI[k] * d(N, k) for k in R3_) + s2 * N * sum(d(XI[k], k) for k in R3_)
op_rhs = Hop(Np, E0)(psi)
e3 = zero_coeffs(list((op_lhs - op_rhs).applyfunc(sp.expand)))
s3 = asolve(e3, [a, s1, s2])
check("R3", s3 == [{a: lamf / lam1, s1: -lamf, s2: 0}],
      f"{{C,G}} at order chi chibar with E = (delta + a h)^(-1/2), Kosmann kap = i/4 (from R1): {s3}  => a lam1 = lam_f, s1 = -lam_f")
# control: the opposite Kosmann spin sign fails
op_lhs_b = (HdE(psi) + lamf * (H0(Lhalf(XI, -KAP)(psi)) - Lhalf(XI, -KAP)(H0(psi)))).applyfunc(sp.expand)
s3b = asolve(zero_coeffs(list((op_lhs_b - op_rhs).applyfunc(sp.expand))), [a, s1, s2])
check("R3c", s3b == [], f"control: Kosmann spin coefficient -i/4 does not close: {s3b}")

# ------------------------------------------------------------------------------------------------- R4 the cone and alpha
# closure on one G = lam1 G1 + lam_f K with one c0: gravity part c0 lam1 = K1/(4 alpha) (R2), walker part v^2 = c0 lam_f (R1)
v2 = sp.simplify(sP[0][c0] * lamf)                         # walker part: v^2 x (R1's unit coefficient) = c0 lam_f
v2a = sp.simplify(v2.subs(lamf, sp.solve(sp.Eq(a, s3[0][a]), lamf)[0]))   # lam_f = a lam1 (R3)
check("R4a", sp.simplify(v2a - a * K1 / (4 * al)) == 0, f"walker speed^2 v^2 = c0 lam_f = {v2} = a K1/(4 alpha) using lam_f = a lam1 (R3)")
v2B = sp.simplify(v2a.subs(K1, K2 / a))     # B2 (from the note, two engines): K2 = a K1
sal = asolve([v2B - 1], [al])
check("R4b", sp.simplify(v2B - K2 / (4 * al)) == 0 and sal == [{al: K2 / 4}],
      f"with B2's K2 = a K1: v^2 = {v2B} (= TT cone K2/(4 alpha)); v = 1 => {sal}; at a = 1, alpha = K1/4 = K2/4")
# sign sanity: v^2 > 0 for K1, alpha, a > 0 (Lorentzian), and v^2 is Phi_rho invariant (a->rho a, K1->rho K1, alpha->rho^2 alpha)
rho = sp.symbols("rho", positive=True)
check("R4c", sp.simplify(v2a.subs({a: rho * a, K1: rho * K1, al: rho ** 2 * al}, simultaneous=True) - v2a) == 0,
      "v^2 = a K1/(4 alpha) is Phi_rho invariant (a -> rho a, K1 -> rho K1, alpha -> rho^2 alpha), as an observable must be")

# ------------------------------------------------------------------------------------------------- R5 scaling identity behind B2
# own sqrt(g) R to second order from Christoffels, plane-wave free: use generic h; check K1 R1 + K2 R2 = (K1^2/K2) sqrtgR_(1,2)[(K2/K1) h]
t = sp.Symbol("t")


def sqrtgR_upto2(hmat):
    g = sp.eye(3) + t * hmat
    gi = sp.eye(3) - t * hmat + t ** 2 * hmat * hmat
    Gam = [[[sum(gi[l, m] * (d(g[m, i], j) + d(g[m, j], i) - d(g[i, j], m)) for m in R3_) / 2 for j in R3_] for i in R3_] for l in R3_]
    Ric = sp.zeros(3, 3)
    for i in R3_:
        for j in R3_:
            Ric[i, j] = sum(d(Gam[l][i][j], l) - d(Gam[l][i][l], j) + sum(Gam[l][l][m] * Gam[m][i][j] - Gam[l][j][m] * Gam[m][i][l]
                                                                         for m in R3_) for l in R3_)
    Rs = sum(gi[i, j] * Ric[i, j] for i in R3_ for j in R3_)
    trh_, trh2 = hmat.trace(), (hmat * hmat).trace()
    sg = 1 + t * trh_ / 2 + t ** 2 * (trh_ ** 2 / 8 - trh2 / 4)
    ser = sp.expand(sp.series(sp.expand(sg * Rs), t, 0, 3).removeO())
    return ser.coeff(t, 1), ser.coeff(t, 2)


# 2-component h restricted (x0, x1 dependence, h00, h01, h11 only) to keep it cheap; the scaling identity is exact anyway
Y = X[:2]
hr = sp.zeros(3, 3)
hr[0, 0] = sp.Function("u")(*Y); hr[1, 1] = sp.Function("w")(*Y); hr[0, 1] = hr[1, 0] = sp.Function("q")(*Y)
r1, r2 = sqrtgR_upto2(hr)
R1lin = sum(d(d(hr[i, j], i), j) for i in R3_ for j in R3_) - sum(d(d(hr.trace(), k), k) for k in R3_)
check("R5a", sp.expand(r1 - R1lin) == 0, "own Christoffel sqrt(g)R: first-order part equals d_i d_j h_ij - lap trh (the R1 used in R2)")
eps_ = K2 / K1
lhs5 = K1 * r1 + K2 * r2
rhs5 = (K1 ** 2 / K2) * (eps_ * r1 + eps_ ** 2 * r2)
check("R5b", sp.simplify(lhs5 - rhs5) == 0, "K1 R1 + K2 R2 = (K1^2/K2)[sqrt g R]^(1,2) on delta + (K2/K1) h: gravity sees delta + (K2/K1) h, "
      "the walker sees delta + a h, so one relabelling generator for both needs a = K2/K1 (gamma = 1) -- consistent with B2")

print(f"TOTAL: PASS={sum(PASS)} FAIL={len(PASS) - sum(PASS)}")
