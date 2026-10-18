#!/usr/bin/env python3
"""B15 continuum / gradient-expansion part (exact sympy, generic smooth functions N, M, psi).

Conventions (match B14): every relabelling generator G[xi] acts as {field, G[xi]} = Lie derivative L_xi field
(scalar: G_m = int pi xi.grad phi;  metric: delta h = 2 d xi). For the fermion, with {psi, psibar} = -i,
G_f[xi] = int psibar (i L_xi) psi and {H_f(N), H_f(M)} = -i int psibar [h_N, h_M] psi  (T0 of the lattice script).
So closure with a relabelling of shift u requires [h_N, h_M] = -L_u (one-particle operators).

 C1  spin part of L_xi fixed INDEPENDENTLY of the bracket: L_xi = xi.grad + (1/2) div xi + b (curl xi).sigma with
     [L_xi, sigma.grad] = 0 for every rigid rotation xi = w x x  =>  b = i/4  (Kosmann/Belinfante value).
     (density weight 1/2 is what makes i L_xi Hermitian.)
 C2  continuum Weyl operator h_N = -i v (N sigma.grad + (1/2) grad N.sigma): [h_N, h_M] = -v^2 L_w, w = N grad M - M grad N,
     EXACTLY (all orders), 3D.
 C3  lattice naive Weyl operator with bond timing (t, 1-t), Taylor-expanded in the spacing a, 3D:
     O(a^0): [h_N,h_M] = -v^2 L_w for every t;  O(a^1): proportional to (2t-1), nonzero for t != 1/2.
 C4  1D, t = 1/2, O(a^2): is the remainder absorbable by ANY O(a^2)-corrected relabelling
     L_u + a^2 (c1 u d^3 + c2 u' d^2 + c3 u'' d + c4 u'''), u = -xi~/a the bond bilinear the gravity sector fixes?
 C5  1D naive Dirac + Wilson term: O(a) bracket component along sigma^2 (= -i alpha beta), not of relabelling type;
     and a position-dependent mass m(x) N beta drops out exactly in the continuum.
 C6  closure arithmetic: gravity supplies u_g = -(sK/(4 alpha)) w at leading order (xi~ ~ -w); C2/C3 give
     [h_N,h_M] = -v^2 L_w; closure <=> v^2 = -sK/(4 alpha). Hermiticity (v real) => s = -1 and v^2 = K/(4 alpha).
"""
from __future__ import annotations

import sympy as sp

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


I = sp.I
X = sp.symbols("x y z", real=True)
a, v, t = sp.symbols("a v t", real=True)
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
Nf = sp.Function("N")(*X)
Mf = sp.Function("M")(*X)
PSI = sp.Matrix([sp.Function("psi1")(*X), sp.Function("psi2")(*X)])


def grad(f):
    return [sp.diff(f, xx) for xx in X]


def lie(u, psi, b=I / 4):
    """L_u psi = u.grad psi + (1/2) div u psi + b (curl u).sigma psi"""
    div = sum(sp.diff(u[k], X[k]) for k in range(3))
    curl = [sp.diff(u[2], X[1]) - sp.diff(u[1], X[2]), sp.diff(u[0], X[2]) - sp.diff(u[2], X[0]), sp.diff(u[1], X[0]) - sp.diff(u[0], X[1])]
    out = sp.zeros(2, 1)
    for k in range(3):
        out += u[k] * psi.diff(X[k])
    out += div / 2 * psi
    for k in range(3):
        out += b * curl[k] * (SIG[k] * psi)
    return out


def zero(m):
    return all(sp.simplify(sp.expand(e)) == 0 for e in m)


# ------------------------------------------------------------------ C1 Kosmann coefficient
def c1():
    b = sp.Symbol("b")
    om = sp.symbols("o1 o2 o3")
    xi = [om[1] * X[2] - om[2] * X[1], om[2] * X[0] - om[0] * X[2], om[0] * X[1] - om[1] * X[0]]

    def weyl(psi):
        out = sp.zeros(2, 1)
        for k in range(3):
            out += SIG[k] * psi.diff(X[k])
        return out
    commu = lie(xi, weyl(PSI), b) - weyl(lie(xi, PSI, b))
    sol = sp.solve(sp.expand(commu[0].subs({om[0]: 0, om[1]: 0, om[2]: 1}).subs(PSI[0], 0)), b)
    ok = sol == [I / 4] and zero(lie(xi, weyl(PSI), I / 4) - weyl(lie(xi, PSI, I / 4)))
    check("C1", ok, f"rotation invariance of sigma.grad fixes the spin coefficient of the spinor Lie derivative: b = {sol} (Kosmann: L_xi = xi.grad + div xi/2 + (i/4) curl xi.sigma)")


# ------------------------------------------------------------------ C2 continuum exact identity
def hcont(n, psi):
    out = sp.zeros(2, 1)
    for k in range(3):
        out += SIG[k] * (n * psi.diff(X[k]) + sp.diff(n, X[k]) / 2 * psi)
    return -I * v * out


def c2():
    br = hcont(Nf, hcont(Mf, PSI)) - hcont(Mf, hcont(Nf, PSI))
    w = [Nf * sp.diff(Mf, xx) - Mf * sp.diff(Nf, xx) for xx in X]
    ok = zero(br + v ** 2 * lie(w, PSI))
    check("C2", ok, "continuum symmetrized Weyl operator: [h_N, h_M] = -v^2 L_w exactly, w = N grad M - M grad N, L_w Kosmann (spin term produced automatically with b = i/4)")


# ------------------------------------------------------------------ lattice Taylor machinery
def shift(expr, k, s, K):
    return sum(((s * a) ** n / sp.factorial(n)) * sp.diff(expr, X[k], n) for n in range(K + 1))


def trunc(expr, p):
    expr = sp.expand(expr)
    return sum(expr.coeff(a, q) * a ** q for q in range(-2, p + 1))


def hlat(n, psi, p, dims=(0, 1, 2), tt=t, mats=None):
    """naive lattice Weyl operator, bond weight tt*N_x + (1-tt) N_(x+e), Taylor-expanded, truncated at a^p"""
    mats = SIG if mats is None else mats
    K = p + 2
    out = sp.zeros(psi.shape[0], 1)
    for k in dims:
        wb = tt * n + (1 - tt) * shift(n, k, 1, K)           # bond (x, x+e)
        wbm = tt * shift(n, k, -1, K) + (1 - tt) * n         # bond (x-e, x)
        fwd = psi.applyfunc(lambda e: shift(e, k, 1, K))
        bwd = psi.applyfunc(lambda e: shift(e, k, -1, K))
        out += (mats[k] * (wb * fwd - wbm * bwd)) * (-I * v / (2 * a))
    return out.applyfunc(lambda e: trunc(e, p))


def c3():
    p = 1
    hm = hlat(Mf, PSI, p)
    hn = hlat(Nf, PSI, p)
    br = (hlat(Nf, hm, p) - hlat(Mf, hn, p)).applyfunc(lambda e: trunc(e, p))
    w = [Nf * sp.diff(Mf, xx) - Mf * sp.diff(Nf, xx) for xx in X]
    lead = br.applyfunc(lambda e: sp.expand(e).coeff(a, 0))
    neg = br.applyfunc(lambda e: sp.expand(e).coeff(a, -1))
    first = br.applyfunc(lambda e: sp.expand(e).coeff(a, 1))
    ok0 = zero(neg) and zero(lead + v ** 2 * lie(w, PSI))
    check("C3a", ok0, "lattice naive Weyl (3D), any bond timing t: O(a^-1) part 0 and O(a^0) part of [h_N,h_M] = -v^2 L_w (Kosmann, same v^2 coefficient as the continuum)")
    f_half = first.applyfunc(lambda e: sp.expand(e.subs(t, sp.Rational(1, 2))))
    f_other = first.applyfunc(lambda e: sp.expand(e.subs(t, 1)))
    lin_in = all(sp.expand(sp.diff(e, t, 2)) == 0 for e in first)
    fac = all(sp.expand(e.subs(t, sp.Rational(1, 2))) == 0 for e in first)
    check("C3b", zero(f_half) and not zero(f_other) and lin_in and fac,
          "O(a^1) part of the bracket is affine in t, vanishes at t = 1/2 (endpoint mean) and is nonzero at t = 1 (one-endpoint timing)")
    # describe the O(a) term at t=1: derivative order acting on psi
    print("   O(a) term (t=1), first component, number of terms:", len(sp.Add.make_args(sp.expand(f_other[0]))))


# ------------------------------------------------------------------ C4 1D O(a^2) absorbability
def c4():
    x = X[0]
    n = sp.Function("N")(x)
    m = sp.Function("M")(x)
    ps = sp.Function("psi")(x)
    p = 2
    K = p + 2

    def sh1(e, s):
        return sum(((s * a) ** k / sp.factorial(k)) * sp.diff(e, x, k) for k in range(K + 1))

    def D(nn, f):  # 1D lattice operator  (1/2a)[wbar+ f(x+a) - wbar- f(x-a)], endpoint mean; h = -i v sigma^1 D
        wp = (nn + sh1(nn, 1)) / 2
        wm = (sh1(nn, -1) + nn) / 2
        return trunc((wp * sh1(f, 1) - wm * sh1(f, -1)) / (2 * a), p)
    br = trunc(D(n, D(m, ps)) - D(m, D(n, ps)), p)       # [D_N, D_M] ; [h_N,h_M] = -v^2 [D_N, D_M]
    w = n * sp.diff(m, x) - m * sp.diff(n, x)

    def ell(u, f):
        return u * sp.diff(f, x) + sp.diff(u, x) * f / 2
    lead_ok = sp.simplify(br.coeff(a, 0) - ell(w, ps)) == 0
    # u = -xi~/a with xi~ at the bond midpoint y: xi~(y) = N(y+a/2) M(y-a/2) - N(y-a/2) M(y+a/2)
    def shh(e, s):
        return sum(((s * a / 2) ** k / sp.factorial(k)) * sp.diff(e, x, k) for k in range(K + 2))
    u = trunc(-(shh(n, 1) * shh(m, -1) - shh(n, -1) * shh(m, 1)) / a, p)
    u_ok = sp.simplify(u.coeff(a, 0) - w) == 0 and u.coeff(a, 1) == 0
    u2 = u.coeff(a, 2)
    R = sp.expand(br.coeff(a, 2) - ell(u2, ps))
    c = sp.symbols("c1:5")
    Xw = c[0] * w * sp.diff(ps, x, 3) + c[1] * sp.diff(w, x) * sp.diff(ps, x, 2) + c[2] * sp.diff(w, x, 2) * sp.diff(ps, x) + c[3] * sp.diff(w, x, 3) * ps
    resid = sp.expand(R - Xw)
    # coefficient extraction: treat derivatives as independent symbols
    reps = {}
    for f, nm in ((n, "n"), (m, "m"), (ps, "p")):
        for k in range(8, -1, -1):
            reps[sp.diff(f, x, k) if k else f] = sp.Symbol(f"{nm}{k}")
    rs = sp.expand(resid.subs(reps))
    syms = [s for s in rs.free_symbols if s.name[0] in "nmp"]
    eqs = sp.Poly(rs, *syms).coeffs()
    sol = sp.solve(eqs, c, dict=True)
    Rs = sp.expand(R.subs(reps))
    print("   1D O(a^2) remainder R (after subtracting L_{u2}):", sp.factor(Rs))
    check("C4a", lead_ok and u_ok, "1D endpoint mean: O(a^0) of [D_N,D_M] = L_w; gravity's bond bilinear u = -xi~/a = w + O(a^2) (midpoint expansion)")
    check("C4b", sol == [], f"1D endpoint mean, O(a^2): the remainder is NOT absorbable by any O(a^2)-corrected relabelling L_u + a^2(c1 u d^3 + c2 u' d^2 + c3 u'' d + c4 u''') (sympy.solve -> {sol}): the fermion bracket closes only up to an O(a^2) lattice artefact")
    # contrast: is it absorbable if u is allowed to be ANY bilinear (i.e. the gravity shift were free)? -> shows the obstruction is the shift, not the operator
    q = sp.symbols("q1:3")
    alt = q[0] * (n * sp.diff(m, x, 3) - m * sp.diff(n, x, 3)) + q[1] * (sp.diff(n, x) * sp.diff(m, x, 2) - sp.diff(m, x) * sp.diff(n, x, 2))
    resid2 = sp.expand(br.coeff(a, 2) - ell(alt, ps) - Xw)
    rs2 = sp.expand(resid2.subs(reps))
    syms2 = [s for s in rs2.free_symbols if s.name[0] in "nmp"]
    sol2 = sp.solve(sp.Poly(rs2, *syms2).coeffs(), list(c) + list(q), dict=True)
    check("C4c", sol2 != [], f"control: if the O(a^2) part of the shift were a FREE bilinear, the remainder would be absorbable (solution {sol2}); so the obstruction is the mismatch between the fermion's range-2 shift and the gravity sector's nearest-neighbour xi~")


# ------------------------------------------------------------------ C5 Wilson / position-dependent mass
def c5():
    x = X[0]
    n = sp.Function("N")(x)
    m = sp.Function("M")(x)
    mu = sp.Function("mu")(x)
    r = sp.Symbol("r", real=True)
    psi = sp.Matrix([sp.Function("psi1")(x), sp.Function("psi2")(x)])
    s1, s2, s3 = SIG
    p = 1
    K = p + 3

    def sh1(e, s):
        return sum(((s * a) ** k / sp.factorial(k)) * sp.diff(e, x, k) for k in range(K + 1))

    def h(nn, f, rr=r):
        wp = (nn + sh1(nn, 1)) / 2
        wm = (sh1(nn, -1) + nn) / 2
        fp, fm = f.applyfunc(lambda e: sh1(e, 1)), f.applyfunc(lambda e: sh1(e, -1))
        hop = s1 * (wp * fp - wm * fm) * (-I * v / (2 * a))
        wil = s3 * (wp * (f - fp) + wm * (f - fm)) * (rr / (2 * a))
        return (hop + wil).applyfunc(lambda e: trunc(e, p + 1))
    # apply to psi = (f, 0) and (0, f) to read the 2x2 operator; sigma^2 component = (B21 - B12)/(2i)
    f = sp.Function("f")(x)
    b_col1 = (h(n, h(m, sp.Matrix([f, 0]))) - h(m, h(n, sp.Matrix([f, 0])))).applyfunc(lambda e: trunc(e, p))
    b_col2 = (h(n, h(m, sp.Matrix([0, f]))) - h(m, h(n, sp.Matrix([0, f])))).applyfunc(lambda e: trunc(e, p))
    # operator entries B_ij acting on f: B11 = col1[0], B21 = col1[1], B12 = col2[0], B22 = col2[1]
    sig2 = sp.expand((b_col1[1] - b_col2[0]) / (2 * I))
    sig2_a1 = sp.expand(sig2.coeff(a, 1))
    sig2_a0 = sp.expand(sig2.coeff(a, 0))
    w = n * sp.diff(m, x) - m * sp.diff(n, x)
    wp = sp.diff(w, x)
    target = sp.expand(-(r * v / 2) * (wp * sp.diff(f, x) + sp.diff(wp, x) * f / 2))   # -(r v/2) l_{w'} f
    ratio_ok = sp.simplify(sig2_a1 - target) == 0
    print("   sigma^2 component, O(a):", sp.factor(sig2_a1))
    check("C5a", sig2_a0 == 0 and sig2_a1 != 0 and ratio_ok,
          "1D naive Dirac + Wilson (endpoint mean): the bracket acquires a sigma^2 (= i alpha beta) component at O(a) (zero at O(a^0)), equal to -(r v/2) a sigma^2 (w' d + w''/2) = -(r v a/2) sigma^2 l_{w'} - Clifford-odd, not a spinor relabelling; Wilson fermions close only at leading order, O(a) obstruction")
    # position-dependent mass drops out in the continuum
    def hc(nn, g):
        return -I * v * s1 * (nn * g.diff(x) + sp.diff(nn, x) / 2 * g) + s3 * mu * nn * g
    brm = hc(n, hc(m, psi)) - hc(m, hc(n, psi))
    brk = (-I * v) ** 2 * (s1 * s1) * ((n * (m * psi.diff(x) + sp.diff(m, x) / 2 * psi).diff(x) + sp.diff(n, x) / 2 * (m * psi.diff(x) + sp.diff(m, x) / 2 * psi))
                                       - (m * (n * psi.diff(x) + sp.diff(n, x) / 2 * psi).diff(x) + sp.diff(m, x) / 2 * (n * psi.diff(x) + sp.diff(n, x) / 2 * psi)))
    check("C5b", zero(brm - brk), "continuum: an arbitrary position-dependent mass mu(x) N beta drops out of [h_N,h_M] exactly (alpha beta = -beta alpha)")


def c6():
    s, K, al = sp.symbols("s K alpha", real=True)
    v2 = sp.Symbol("v2")
    # closure: [h_N,h_M] = -v^2 L_w must equal -L_{u_g}, u_g = -(sK/(4alpha)) * xi~/(-1) ... in lattice units xi_g = (sK/4alpha) xi~, xi~ ~ -w
    # => u_g = (sK/(4alpha)) * (-w) and -v^2 L_w = -L_{u_g} = (sK/(4alpha)) L_w
    sol = sp.solve(sp.Eq(-v2, s * K / (4 * al)), v2)
    ok = sol == [-s * K / (4 * al)]
    check("C6", ok, f"closure condition v^2 = {sol[0]}; with K, alpha > 0 and v real (Hermitian h) only s = -1 is possible and then v^2 = K/(4 alpha): the same value B14 found for the scalar gradient coefficient c")


if __name__ == "__main__":
    c1()
    c2()
    c3()
    c4()
    c5()
    c6()
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
