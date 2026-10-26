#!/usr/bin/env python3
"""
check.py -- the-inertia-of-a-static-binding, derivation attempt a1.

Model (supplied, see ATTEMPT.md): two massive records on the line, each with
single-record generator  h = s*S + m*eps  (S=(T-T^-1)/(2i), eps=(-1)^x, coin s=+-1 conserved),
one record per site (exclusion), coin-blind static term V acting when |x1-x2| = d.

Everything below is exact (sympy / Fractions / rigorous mpmath interval arithmetic) EXCEPT the
blocks explicitly marked NUMERIC (mpmath, 40-60 digits), which are cross-checks by an
independent method, and the one float diagonalisation marked FLOAT.
Prints one line per check, then TOTAL, SUMMARY, and HIT only for the new scoped result.
"""
import sys, time
import sympy as sp
import mpmath as mp

T0 = time.time()
PASS = 0
FAIL = 0


def chk(name, cond, note=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + (("  [" + note + "]") if note else ""))
    sys.stdout.flush()


# ----------------------------------------------------------------------------------------
# P1  EXACT: the lift identity  H_pair(psi) = Phi_K (H(K) u)  on the infinite line.
#     psi(x1,x2) = i^(x1+x2) q^(x1+x2) u(x1-x2, x1 mod 2),  q = e^{iK/2}.
# ----------------------------------------------------------------------------------------
m, V = sp.symbols("m V")
q = sp.symbols("q", nonzero=True)
R = 8
u = {}
for r in range(0, R + 1):
    for p in (0, 1):
        u[(r, p)] = sp.Integer(0) if r == 0 else sp.Symbol(f"u_{r}_{p}")


def uu(r, p):
    return u[(r, p % 2)]


def psi(x1, x2):
    r = x1 - x2
    if r < 1 or r > R:
        raise ValueError
    return sp.I ** (x1 + x2) * q ** (x1 + x2) * uu(r, x1)


def h_pair(x1, x2, d):
    """(H psi)(x1,x2): gauge-psi walkers h = S + m eps on each record, V at separation d.
    psi at r=0 is the excluded (zero) amplitude, via u(0,.)=0."""
    r = x1 - x2

    def ps(a, b):
        if a - b == 0:
            return sp.Integer(0)
        return psi(a, b)

    t1 = (ps(x1 - 1, x2) - ps(x1 + 1, x2)) / (2 * sp.I) + m * (-1) ** x1 * ps(x1, x2)
    t2 = (ps(x1, x2 - 1) - ps(x1, x2 + 1)) / (2 * sp.I) + m * (-1) ** x2 * ps(x1, x2)
    return t1 + t2 + (V * ps(x1, x2) if r == d else 0)


def fiber_apply(r, p, d):
    """(H(K)u)(r,p) in the phi gauge (hop -1/2 per record), q = e^{iK/2}."""
    hop = -sp.Rational(1, 2) * (q * uu(r + 1, p + 1) + uu(r - 1, p + 1) / q + q * uu(r - 1, p) + uu(r + 1, p) / q)
    mass = m * (-1) ** p * (1 + (-1) ** r) * uu(r, p)
    return hop + mass + (V * uu(r, p) if r == d else 0)


ok_lift = True
for d in (1, 2):
    for x2 in (-2, -1, 0, 1):
        for r in range(1, R):
            x1 = x2 + r
            lhs = h_pair(x1, x2, d)
            rhs = sp.I ** (x1 + x2) * q ** (x1 + x2) * fiber_apply(r, x1, d)
            if sp.simplify(sp.expand(lhs - rhs)) != 0:
                ok_lift = False
chk("P1 lift identity: pair generator on psi == gauge*e^{iK(x1+x2)/2} * fiber(K) u  (d=1,2; windows x2=-2..1, r=1..7; symbolic u,q,m,V)", ok_lift,
    "EXACT sympy")

# P1b: opposite coins (s1=+1, s2=-1): gauge i^{x1} (-i)^{x2} lifts to the SAME fiber operator (the factor i^{x1-x2} depends on r only).
def psi_opp(x1, x2):
    r = x1 - x2
    return sp.I ** x1 * (-sp.I) ** x2 * q ** (x1 + x2) * uu(r, x1)


def h_pair_opp(x1, x2, d):
    r = x1 - x2

    def ps(a, b):
        return sp.Integer(0) if a == b else psi_opp(a, b)
    t1 = (ps(x1 - 1, x2) - ps(x1 + 1, x2)) / (2 * sp.I) + m * (-1) ** x1 * ps(x1, x2)
    t2 = -(ps(x1, x2 - 1) - ps(x1, x2 + 1)) / (2 * sp.I) + m * (-1) ** x2 * ps(x1, x2)
    return t1 + t2 + (V * ps(x1, x2) if r == d else 0)


ok_opp = True
for d in (1, 2):
    for x2 in (-2, -1, 0, 1):
        for r in range(1, R):
            x1 = x2 + r
            lhs = h_pair_opp(x1, x2, d)
            rhs = sp.I ** x1 * (-sp.I) ** x2 * q ** (x1 + x2) * fiber_apply(r, x1, d)
            if sp.simplify(sp.expand(lhs - rhs)) != 0:
                ok_opp = False
chk("P1b opposite coins (s1=+1, s2=-1) lift to the same fiber operator H(K) with gauge i^{x1}(-i)^{x2}: the coin pattern does not change the spectrum or W for a coin-blind term", ok_opp, "EXACT sympy")

# ----------------------------------------------------------------------------------------
# P2  EXACT: w-basis.  w_+- = u0 +- u1  gives chain A (hop -cos(K/2)), chain B (hop i sin(K/2)),
#     coupled by m(1+(-1)^r).  c0=cos(K/2), s0=sin(K/2), q=c0+i s0.
# ----------------------------------------------------------------------------------------
c0, s0 = sp.symbols("c0 s0", real=True)
ok_w = True
for r in range(1, R - 1):
    for d in (1, 2):
        Hu0 = fiber_apply(r, 0, d)
        Hu1 = fiber_apply(r, 1, d)
        sub = {q: c0 + sp.I * s0}
        wp = sp.expand((Hu0 + Hu1).subs(sub))
        wm = sp.expand((Hu0 - Hu1).subs(sub))

        def Wp(rr): return uu(rr, 0) + uu(rr, 1)

        def Wm(rr): return uu(rr, 0) - uu(rr, 1)
        # 1/q = c0 - i s0 on the unit circle (c0^2+s0^2=1): replace via explicit conj
        wp = sp.expand((Hu0 + Hu1).subs(1 / q, c0 - sp.I * s0).subs(q, c0 + sp.I * s0))
        wm = sp.expand((Hu0 - Hu1).subs(1 / q, c0 - sp.I * s0).subs(q, c0 + sp.I * s0))
        exp_p = -c0 * (Wp(r + 1) + Wp(r - 1)) + m * (1 + (-1) ** r) * Wm(r) + (V * Wp(r) if r == d else 0)
        exp_m = sp.I * s0 * (Wm(r + 1) - Wm(r - 1)) + m * (1 + (-1) ** r) * Wp(r) + (V * Wm(r) if r == d else 0)
        dp = sp.expand(wp - exp_p)
        dm = sp.expand(wm - exp_m)
        # reduce c0^2+s0^2=1 (they enter only through q q^-1 = 1; the expansions above are linear in c0,s0)
        for dd in (dp, dm):
            nm_ = sp.numer(sp.together(dd))
            nm_ = sp.rem(sp.Poly(sp.expand(nm_), s0), sp.Poly(s0 ** 2 + c0 ** 2 - 1, s0))   # impose c0^2+s0^2=1
            if sp.expand(nm_.as_expr()) != 0:
                ok_w = False
chk("P2 w-basis form: A-chain hop -cos(K/2), B-chain hop +i sin(K/2) (forward) / -i sin(K/2) (back), mass coupling m(1+(-1)^r), V on both", ok_w, "EXACT sympy")

# ----------------------------------------------------------------------------------------
# P3  EXACT: K = 0 bound state of the line, d = 2.  Unknown parameters z,E,t,m with the relations
#       R1: (1+z)^2 = z (E^2 - 4 m^2)          (bulk decay factor)
#       R2: E t^2 - (2+z) t - 4 m^2 E = 0       (boundary condition, t = E - V)
#     psi0:  w+(1) = -1/E, w+(2) = 1, w+(2j) = z^(j-1), w+(2j+1) = c z^(j-1), c = -(1+z)/E,
#            w-(2) = 2m/t,  w-(2j) = 2m z^(j-1)/E (j>=2),  w-(odd)=0.
#     All eigen-equations of the K=0 fiber, r=1..8 and generic j, vanish modulo (R1,R2).
# ----------------------------------------------------------------------------------------
z, E, t, mm = sp.symbols("z E t mm")
R1 = (1 + z) ** 2 - z * (E ** 2 - 4 * mm ** 2)
R2 = E * t ** 2 - (2 + z) * t - 4 * mm ** 2 * E
Zj = sp.symbols("Zj")
G = sp.groebner([R1, R2], t, E, z, mm, Zj, order="lex")
Vv = E - t
cc = -(1 + z) / E


def wplus(r):
    if r == 0: return sp.Integer(0)
    if r == 1: return -1 / E
    j = r // 2
    return z ** (j - 1) if r % 2 == 0 else cc * z ** (j - 1)


def wminus(r):
    if r % 2 == 1: return sp.Integer(0)
    j = r // 2
    return 2 * mm / t if j == 1 else 2 * mm * z ** (j - 1) / E


def resid_K0(r, d=2):
    """residuals of the K=0 fiber equations in the w basis (A and B rows) at site r."""
    rA = E * wplus(r) - (-(wplus(r + 1) + wplus(r - 1)) + mm * (1 + (-1) ** r) * wminus(r) + (Vv * wplus(r) if r == d else 0))
    rB = E * wminus(r) - (mm * (1 + (-1) ** r) * wplus(r) + (Vv * wminus(r) if r == d else 0))
    return rA, rB


def in_ideal(expr):
    num, den = sp.fraction(sp.together(expr))
    num = sp.expand(num)
    rem = G.reduce(num)[1]
    return sp.expand(rem) == 0


ok_psi = True
for r in range(1, 9):
    for e in resid_K0(r):
        if not in_ideal(e):
            ok_psi = False
chk("P3a psi0 satisfies all K=0 fiber equations at sites r=1..8 modulo (R1,R2)  [bound-state condition (2+z)/E = t - 4m^2/t, t=E-V]", ok_psi, "EXACT sympy Groebner")

# generic site 2j, 2j+1 (j>=3): z^j =: Zj symbol


def wp_g(kind):
    # kind: ('e',0) means w+(2j+0)... build the needed neighbours of 2j and 2j+1 with generic j>=3
    pass


# even r = 2j: w+(2j)=Zj/z, w+(2j+1)=c Zj/z, w+(2j-1)=c Zj/z^2 ; w-(2j)=2m Zj/(z E)
rA = E * (Zj / z) - (-(cc * Zj / z + cc * Zj / z ** 2) + mm * 2 * (2 * mm * Zj / (z * E)))
rB = E * (2 * mm * Zj / (z * E)) - (2 * mm * (Zj / z))
# odd r = 2j+1: w+(2j+1)=c Zj/z, w+(2j+2)=Zj, w+(2j)=Zj/z ; w-=0
rAo = E * (cc * Zj / z) - (-(Zj + Zj / z))
chk("P3b generic bulk sites r=2j and r=2j+1 (j>=3) vanish modulo R1", all(
    sp.expand(G.reduce(sp.expand(sp.fraction(sp.together(e))[0]))[1]) == 0 for e in (rA, rB, rAo)), "EXACT sympy")

# ----------------------------------------------------------------------------------------
# P4  EXACT: threshold z = -1, E = 2m: critical coupling  V_c = (8m^2 - 1 - sqrt(1+64 m^4))/(4m);
#     E_thr(K) = 2 sqrt(m^2 + sin^2(K/2)) from the bulk quadratic at x = z + 1/z = -2.
# ----------------------------------------------------------------------------------------
M = sp.symbols("M", positive=True)
tc = sp.symbols("tc", positive=True)
# R2 at E = 2M: 2M t^2 - t - 8 M^3 = 0 (z=-1)
tc_val = (1 + sp.sqrt(1 + 64 * M ** 4)) / (4 * M)
chk("P4a threshold: root of 2M t^2 - t - 8M^3 = 0 is t = (1+sqrt(1+64M^4))/(4M)", sp.simplify((2 * M * tc_val ** 2 - tc_val - 8 * M ** 3)) == 0, "EXACT")
Vc = 2 * M - tc_val
chk("P4b V_c(m) = (8m^2-1-sqrt(1+64m^4))/(4m) = 2m - t", sp.simplify(Vc - (8 * M ** 2 - 1 - sp.sqrt(1 + 64 * M ** 4)) / (4 * M)) == 0, "EXACT")
# bounded (non-growing) threshold solution <=> w(3)=0 <=> t solves the same quadratic (derivation of P4a)
tt = sp.symbols("tt")
w3 = -1 + 4 * M ** 2 - 2 * M * (Vc + 4 * M ** 2 / (2 * M - Vc))
chk("P4c bounded threshold solution (w(3)=0) at V=V_c", sp.simplify(w3) == 0, "EXACT")
x = sp.symbols("x")
c0s, s0s, Es = sp.symbols("c0s s0s Es", positive=True)
quad = (Es ** 2 - c0s ** 2 * (x + 2)) * (Es ** 2 + s0s ** 2 * (x - 2)) - 4 * M ** 2 * Es ** 2
at_m2 = sp.factor(quad.subs(x, -2))
chk("P4d bulk quadratic at x=-2 has E^2 = 4m^2 + 4 sin^2(K/2): lower edge E_thr(K)=2 sqrt(m^2+sin^2(K/2)), E_thr''(0)=1/(2m)",
    sp.simplify(at_m2.subs(Es, 2 * sp.sqrt(M ** 2 + s0s ** 2))) == 0 and
    sp.simplify(sp.diff(2 * sp.sqrt(M ** 2 + sp.sin(sp.Symbol('K') / 2) ** 2), sp.Symbol('K'), 2).subs(sp.Symbol('K'), 0) - 1 / (2 * M)) == 0, "EXACT")

# ----------------------------------------------------------------------------------------
# P5  EXACT: the second-order (Hellmann-Feynman) identity on a finite chain with the same structure.
#     H(K) = H0 + K H1 + K^2 H2 (truncated, exact to the order needed).  Claim:
#        E''(0) = 2[ <psi|H2|psi> + <H1 psi|H1 psi>/E0 ]/<psi|psi>   at every simple eigenvalue E0 != 0
#     of H0 (psi normalised arbitrarily; H1 psi lives on B-chain odd sites which H0 does not couple).
#     Compared with the implicit derivative -P_KK/P_E of the characteristic polynomial,
#     as elements of Q(i)[E]/(g(E)).
# ----------------------------------------------------------------------------------------
def chain_matrices(N, mval, Vval, d=2):
    n = 2 * N
    H0 = sp.zeros(n, n); H1 = sp.zeros(n, n); H2 = sp.zeros(n, n)
    for r in range(1, N + 1):
        i = 2 * (r - 1)             # index of w+(r); i+1 is w-(r)
        if r % 2 == 0:
            H0[i, i + 1] += 2 * mval; H0[i + 1, i] += 2 * mval
        if r == d:
            H0[i, i] += Vval; H0[i + 1, i + 1] += Vval
        if r < N:
            j = 2 * r
            # forward hop r -> r+1 : H[(r),(r+1)]; A: -cos(K/2) = -1 + K^2/8 ; B: +i sin(K/2) = i K/2
            H0[i, j] += -1; H0[j, i] += -1
            H2[i, j] += sp.Rational(1, 8); H2[j, i] += sp.Rational(1, 8)
            H1[i + 1, j + 1] += sp.I / 2; H1[j + 1, i + 1] += -sp.I / 2
    return H0, H1, H2


Es_, Ks_ = sp.symbols("E_ K_")


def hf_identity_check(Nn, mval, Vval):
    H0, H1, H2 = chain_matrices(Nn, mval, Vval)
    Hfull = H0 + Ks_ * H1 + Ks_ ** 2 * H2
    P = sp.expand((Es_ * sp.eye(2 * Nn) - Hfull).det(method="berkowitz"))
    P0 = sp.expand(P.subs(Ks_, 0))
    no_lin = sp.expand(sp.diff(P, Ks_).subs(Ks_, 0)) == 0
    PE = sp.diff(P, Es_).subs(Ks_, 0)
    PKK = sp.diff(P, Ks_, 2).subs(Ks_, 0)
    adj = (Es_ * sp.eye(2 * Nn) - H0).adjugate()
    tested = 0
    ok = True
    for g_, mult in sp.factor_list(P0)[1]:
        g = sp.Poly(g_, Es_)
        if g.degree() < 1 or mult != 1 or g_ == Es_:
            continue
        tested += 1
        col = None
        for c_ in range(2 * Nn):
            vec = [sp.Poly(sp.expand(adj[rw, c_]), Es_).rem(g).as_expr() for rw in range(2 * Nn)]
            if any(sp.expand(v) != 0 for v in vec):
                col = sp.Matrix(vec); break
        if col is None:
            ok = False; continue
        nrm = sp.expand((col.T * col)[0, 0])
        h1v = H1 * col
        num = sp.expand((col.T * H2 * col)[0, 0] + sum(h1v[a_].subs(sp.I, -sp.I) * h1v[a_] for a_ in range(2 * Nn)) / Es_)
        lhs = sp.together(-PKK * nrm - 2 * num * PE)
        nm, dn = sp.fraction(lhs)
        if sp.Poly(sp.expand(nm), Es_).rem(g).as_expr() != 0:
            ok = False
    return no_lin, ok, tested


for (Nn, mval, Vval) in [(4, sp.Rational(3, 2), sp.Rational(-9, 5)), (5, sp.Rational(1, 3), sp.Rational(-7, 2)), (6, sp.Rational(5, 4), sp.Rational(-1))]:
    no_lin, ok, tested = hf_identity_check(Nn, mval, Vval)
    chk(f"P5 finite chain N={Nn}, m={mval}, V={Vval}: no K-linear term, and E''(0) = 2[<H2> + |H1 psi|^2/E0]/<psi|psi> equals the implicit derivative -P_KK/P_E for all {tested} simple nonzero eigenvalue factors",
        no_lin and ok and tested >= 1, "EXACT sympy, algebraic numbers mod minimal polynomial")

# ----------------------------------------------------------------------------------------
# P6  EXACT closed forms along the bound-state branch (parameters z in (-1,0), m>0).
# ----------------------------------------------------------------------------------------
zS, mS, sS = sp.symbols("zS mS sS", positive=True)


def closed_forms(zv, mv, Ev, tv):
    """return N, S1, Q, W as expressions (E, t treated as given numbers/symbols)."""
    c = -(1 + zv) / Ev
    w1 = -1 / Ev
    # sums, a = w+(2) = 1 normalisation
    Nsum = w1 ** 2 + (1 + c ** 2) / (1 - zv ** 2) + 4 * mv ** 2 * (1 / tv ** 2 + zv ** 2 / (Ev ** 2 * (1 - zv ** 2)))
    S1 = -1 / Ev + c / (1 - zv)
    Qs = (2 * mv / tv) ** 2 + (2 * mv) ** 2 * (zv / Ev - 1 / tv) ** 2 + (2 * mv / Ev) ** 2 * zv ** 2 * (1 - zv) / (1 + zv)
    Wv = (Ev * S1 + Qs) / (2 * Nsum)
    return Nsum, S1, Qs, Wv


# verify the geometric sums of N, S1, Q against explicit term lists (generic z, E, t, m, symbolic tail)
zz, EE, tt_, mmm = sp.symbols("zz EE tt_ mmm")
J = sp.symbols("J", integer=True, positive=True)
cz = -(1 + zz) / EE
j = sp.symbols("j", integer=True, positive=True)
# w+: odd/even
Nsym = (1 / EE ** 2 + sp.Sum(zz ** (2 * (j - 1)), (j, 1, sp.oo)) + sp.Sum(cz ** 2 * zz ** (2 * (j - 1)), (j, 1, sp.oo))
        + (2 * mmm / tt_) ** 2 + sp.Sum((2 * mmm / EE) ** 2 * zz ** (2 * (j - 1)), (j, 2, sp.oo)))
geo = lambda expr, lo: sp.simplify(sp.summation(expr, (j, lo, sp.oo)).args[0][0]) if isinstance(sp.summation(expr, (j, lo, sp.oo)), sp.Piecewise) else sp.summation(expr, (j, lo, sp.oo))
Ngeo = 1 / EE ** 2 + geo(zz ** (2 * (j - 1)), 1) + cz ** 2 * geo(zz ** (2 * (j - 1)), 1) + (2 * mmm / tt_) ** 2 + (2 * mmm / EE) ** 2 * geo(zz ** (2 * (j - 1)), 2)
Nclosed = closed_forms(zz, mmm, EE, tt_)[0]
chk("P6a norm N: geometric sums of psi0 equal the closed form", sp.simplify(Ngeo - Nclosed) == 0, "EXACT")
# S1 = sum_r w+(r) w+(r+1):  pairs (1,2): -1/E ; (2j,2j+1): c z^(2j-2) ; (2j+1,2j+2): c z^(2j-1)
S1geo = -1 / EE + cz * geo(zz ** (2 * (j - 1)), 1) + cz * geo(zz ** (2 * j - 1), 1)
chk("P6b S1 = sum_r w+(r)w+(r+1): closed form", sp.simplify(S1geo - closed_forms(zz, mmm, EE, tt_)[1]) == 0, "EXACT")
# Q = sum_{j>=1} (w-(2j) - w-(2j-2))^2 , w-(0)=0:  j=1 -> w-(2)^2 ; j=2 -> (2m)^2 (z/E - 1/t)^2 ; j>=3 -> (2m/E)^2 z^(2(j-2)) (1-z)^2
Qgeo = (2 * mmm / tt_) ** 2 + (2 * mmm) ** 2 * (zz / EE - 1 / tt_) ** 2 + (2 * mmm / EE) ** 2 * (1 - zz) ** 2 * geo(zz ** (2 * (j - 2)), 3)
chk("P6c Q = sum (w-(2j)-w-(2j-2))^2 closed form", sp.simplify(Qgeo - closed_forms(zz, mmm, EE, tt_)[2]) == 0, "EXACT")


# ----------------------------------------------------------------------------------------
# P7  EXACT threshold expansion by implicit differentiation along the branch (z = -1 + delta).
#     Branch: R1(z,E)=0, R2(z,E,t)=0, V = E - t.  W(z,m) = (E S1 + Q)/(2N) with N,Q multiplied by (1+z) (analytic at z=-1).
# ----------------------------------------------------------------------------------------
zb, Eb, tb, mb, sb = sp.symbols("zb Eb tb mb sb", positive=True)
cb = -(1 + zb) / Eb
Np = (1 + zb) / Eb ** 2 + (1 + cb ** 2) / (1 - zb) + 4 * mb ** 2 * ((1 + zb) / tb ** 2 + zb ** 2 / (Eb ** 2 * (1 - zb)))      # (1+z) N
S1b = -1 / Eb + cb / (1 - zb)
Qp = (1 + zb) * ((2 * mb / tb) ** 2 + (2 * mb) ** 2 * (zb / Eb - 1 / tb) ** 2) + (2 * mb / Eb) ** 2 * zb ** 2 * (1 - zb)         # (1+z) Q
Wb = (Eb * (1 + zb) * S1b + Qp) / (2 * Np)
F1 = (1 + zb) ** 2 - zb * (Eb ** 2 - 4 * mb ** 2)
F2 = Eb * tb ** 2 - (2 + zb) * tb - 4 * mb ** 2 * Eb
Ep_ = -sp.diff(F1, zb) / sp.diff(F1, Eb)
tp_ = -(sp.diff(F2, zb) + sp.diff(F2, Eb) * Ep_) / sp.diff(F2, tb)


def Dz(f): return sp.diff(f, zb) + sp.diff(f, Eb) * Ep_ + sp.diff(f, tb) * tp_


tcb = (1 + sb) / (4 * mb)
pt = {zb: -1, Eb: 2 * mb, tb: tcb}


def reds(e):
    """reduce a rational function of m and s=sqrt(1+64 m^4) to canonical form (s^2 -> 1+64m^4)."""
    e = sp.together(e)
    num, den = sp.fraction(e)

    def rr(pp):
        Pp = sp.Poly(sp.expand(pp), sb); out = 0
        for (k,), co in Pp.terms():
            out += co * (64 * mb ** 4 + 1) ** (k // 2) * sb ** (k % 2)
        return sp.expand(out)
    num = rr(num); den = rr(den)
    Pd = sp.Poly(den, sb); B_ = Pd.coeff_monomial(sb); A_ = Pd.coeff_monomial(1)
    if B_ == 0:
        return sp.factor(num / den)
    num2 = rr(sp.expand(num * (A_ - B_ * sb))); den2 = sp.expand(A_ ** 2 - B_ ** 2 * (64 * mb ** 4 + 1))
    return sp.factor(sp.simplify(num2 / den2))


def eq(a, b): return sp.simplify(reds(a) - reds(b)) == 0


chk("P7a on the branch at z=-1: E=2m, t=t_c, V=V_c, and W(-1) = 1  (the pair is two free records at threshold)",
    sp.simplify(F1.subs(pt)) == 0 and sp.simplify(F2.subs(pt).subs(sb, sp.sqrt(64 * mb ** 4 + 1))) == 0 and reds(Wb.subs(pt)) == 1, "EXACT")
alpha = reds(-Dz(Wb).subs(pt))
alpha_claim = (16 * mb ** 2 + 3 - sb) / (8 * mb ** 2)
chk("P7b  1 - W = alpha(m) delta + O(delta^2),  alpha(m) = (16 m^2 + 3 - sqrt(1+64 m^4))/(8 m^2)", sp.simplify(alpha - alpha_claim) == 0, "EXACT")
xx = sp.symbols("xx", positive=True)
chk("P7c alpha(m) > 1 for every m>0  [(8m^2+3)^2 - (1+64m^4) = 48m^2+8 > 0]", sp.expand((8 * xx + 3) ** 2 - (64 * xx ** 2 + 1) - (48 * xx + 8)) == 0, "EXACT")
chk("P7d limits: alpha -> 1 as m -> infinity (lattice value);  alpha = 1/(4m^2) + 2 + O(m^2) as m -> 0",
    sp.limit(alpha_claim.subs(sb, sp.sqrt(64 * mb ** 4 + 1)), mb, sp.oo) == 1 and
    sp.simplify(sp.series(alpha_claim.subs(sb, sp.sqrt(64 * mb ** 4 + 1)), mb, 0, 1).removeO() - (1 / (4 * mb ** 2) + 2)) == 0, "EXACT")
chk("P7e binding energy: dE/dz = 0 and d2E/dz2 = -1/(2m) at z=-1, so 2m - E0 = delta^2/(4m) + O(delta^3), binding fraction (2m-E0)/(2m) = delta^2/(8m^2)",
    sp.simplify(Ep_.subs(pt)) == 0 and eq(Dz(Ep_).subs(pt), -1 / (2 * mb)), "EXACT")
Vc_ = 2 * mb - tcb
dVdz = reds((Ep_ - tp_).subs(pt))
chk("P7f V(delta) = V_c + (dV/dz) delta, dV/dz < 0 (numerator 64m^4+s+1 > 0; 8m^2-+4m+1 > 0): the pair is bound for |V| > |V_c| and delta -> 0+ as V -> V_c^-",
    sp.simplify(dVdz + (64 * mb ** 4 + sb + 1) / (4 * mb * (8 * mb ** 2 - 4 * mb + 1) * (8 * mb ** 2 + 4 * mb + 1))) == 0 and
    sp.discriminant(8 * xx ** 2 - 4 * xx + 1, xx) < 0 and sp.discriminant(8 * xx ** 2 + 4 * xx + 1, xx) < 0, "EXACT")
# potential energy U = V * (w+(2)^2 + w-(2)^2)/N = delta * G(z),  G = V (1+(2m/t)^2)/Np
wr2 = 1 + (2 * mb / tb) ** 2
Gb = (Eb - tb) * wr2 / Np
u1 = reds(Gb.subs(pt))
u1_claim = -(-64 * mb ** 4 + 8 * mb ** 2 * sb + sb - 1) / (16 * mb ** 3)
chk("P7g <U> = u1(m) delta + O(delta^2),  u1 = V_c (1+4m^2/t_c^2) = -(-64m^4+8m^2 s+s-1)/(16 m^3) < 0", sp.simplify(u1 - u1_claim) == 0, "EXACT")
Xs = sp.symbols("Xs", positive=True)
chk("P7h u1 < 0 for all m>0   [(8m^2+1)s > 64m^4+1  <=>  (8m^2+1)^2(64m^4+1) - (64m^4+1)^2 = (64m^4+1)(16m^2) > 0]",
    sp.expand((8 * Xs ** 2 + 1) ** 2 * (64 * Xs ** 4 + 1) - (64 * Xs ** 4 + 1) ** 2 - (64 * Xs ** 4 + 1) * 16 * Xs ** 2) == 0, "EXACT")
# static (non-relativistic) formula W = 1 + <U>/(2m) - <T>/m, with <T> = <U>-virial: T = E0-2m-U = -U + O(delta^2)
static_coeff = sp.simplify(-sp.Rational(3, 2) * u1_claim / mb)       # 1 - W_static = static_coeff * delta
Rm = sp.simplify(alpha_claim / static_coeff)
chk("P7i exact deficit / static-formula deficit, R(m) = alpha m/(-(3/2)u1): R -> 1/3 as m -> 0 and R/m^2 -> 4/3 as m -> infinity",
    sp.simplify(sp.limit(Rm.subs(sb, sp.sqrt(64 * mb ** 4 + 1)), mb, 0) - sp.Rational(1, 3)) == 0 and
    sp.simplify(sp.limit((Rm / mb ** 2).subs(sb, sp.sqrt(64 * mb ** 4 + 1)), mb, sp.oo) - sp.Rational(4, 3)) == 0, "EXACT limits")
lam0 = reds(alpha_claim / (2 * mb * u1_claim))
chk("P7j lambda*(m) = alpha/(2 m u1) < 0, -> -1 as m->inf: V(K) = V0 (1 + lambda* K^2/2) removes the O(delta) deficit",
    sp.limit(lam0.subs(sb, sp.sqrt(64 * mb ** 4 + 1)), mb, sp.oo) == -1, "EXACT limit")
# second order: tuned residual
d2W = Dz(Dz(Wb))
G1 = Dz(Gb)
U2 = reds(G1.subs(pt))
W2 = reds((d2W / 2).subs(pt))
c2 = reds(W2 + lam0 * 2 * mb * U2)
c2_claim = -(-512 * mb ** 6 + 32 * mb ** 4 * sb - 128 * mb ** 4 - 4 * mb ** 2 * sb - 24 * mb ** 2 + 3 * sb - 5) / (8 * mb ** 2 * (8 * mb ** 2 - 4 * mb + 1) * (8 * mb ** 2 + 4 * mb + 1))
chk("P7k fixed-lambda residual: W_tuned - 1 = c2(m) delta^2 + O(delta^3), c2 closed form", sp.simplify(c2 - c2_claim) == 0, "EXACT")
Aq = 512 * Xs ** 3 + 128 * Xs ** 2 + 24 * Xs + 5
Bq = 32 * Xs ** 2 - 4 * Xs + 3
dpoly = sp.Poly(sp.expand(Aq ** 2 - Bq ** 2 * (64 * Xs ** 2 + 1)), Xs)
chk("P7l c2(m) > 0 for all m>0   [A = 512x^3+128x^2+24x+5 > B s with B=32x^2-4x+3>0, x=m^2: A^2 - B^2(64x^2+1) has all coefficients positive]",
    all(co > 0 for co in dpoly.all_coeffs()) and sp.discriminant(Bq, Xs) < 0, "EXACT")
# compare c2 with binding-fraction coefficient 1/(8m^2): ratio c2 * 8 m^2 is not 1 and not small
ratio_c2 = sp.simplify(c2_claim * 8 * mb ** 2)
vals = [sp.N(ratio_c2.subs(sb, sp.sqrt(64 * mb ** 4 + 1)).subs(mb, v), 8) for v in (4, sp.Rational(4, 5), sp.Rational(1, 10))]
chk(f"P7m residual / (binding fraction coefficient 1/(8m^2)) = {[float(v) for v in vals]} at m=4, 4/5, 1/10: the fixed-lambda residual is NOT the mass defect (it exceeds it by a factor 2.3 to 66)",
    all(v > 2 for v in vals), "EXACT closed form evaluated")

# P7n  independence of two core operators: weights p_2 = (w+(2)^2+w-(2)^2)/N and p_4 at r=4 along the branch.
#      A K^2 term X = (rho_2 P_2 + rho_4 P_4) K^2/2 shifts W by E0 (rho_2 <P_2> + rho_4 <P_4>); <P_r> = p_r(delta).
p2b = 1 + (2 * mb / tb) ** 2
p4b = zb ** 2 * (1 + (2 * mb / Eb) ** 2)
rat = p4b / p2b
r_thr = reds(rat.subs(pt)); r_der = reds(Dz(rat).subs(pt))
r_der_claim = -2 * (4096 * mb ** 8 + 32 * mb ** 4 * sb + 128 * mb ** 4 + sb + 1) / ((8 * mb ** 2 - 4 * mb + 1) ** 2 * (8 * mb ** 2 + 4 * mb + 1) ** 2)
chk("P7n p_4/p_2 has a nonzero z-derivative at threshold (closed form, negative for all m>0): the core weights at r=2 and r=4 are independent at O(delta^2), so a two-parameter core K^2 term can cancel the O(delta) and O(delta^2) deficits (suggested; independence is the checked part)",
    sp.simplify(r_der - r_der_claim) == 0, "EXACT")

# ----------------------------------------------------------------------------------------
# P8  NEIGHBOUR TERM (d=1), K=0, EXACT: bound-state condition V = E/(1+z)  =>  no V<0 pair below 2m.
# ----------------------------------------------------------------------------------------
z1, E1 = sp.symbols("z1 E1")
Vsym = sp.symbols("Vsym")
c1 = -(1 + z1) / E1
w1_ = -1 / (E1 - Vsym)                      # from the r=1 equation (E-V) w+(1) = -w+(2)
eq_match = sp.simplify(w1_ - c1 / z1)       # bulk form of the r=2 equation needs w+(1) = c/z
sol = sp.solve(sp.numer(sp.together(eq_match)), Vsym)
chk("P8a neighbour (d=1) at K=0: matching condition has the unique solution V = E/(1+z)", len(sol) == 1 and sp.simplify(sol[0] - E1 / (1 + z1)) == 0, "EXACT")
# also: the w-(1) amplitude vanishes unless E = V ; the r=2 equation uses only w+(1)
chk("P8b hence a decaying solution (|z|<1, real) with E>0 has V = E/(1+z) > 0: an attractive neighbour term (V<0) gives no K=0 level with 0<E<2m, any strength, any m (levels with E<0 are not rest pairs of positive-energy records and are not claimed)",
    sp.simplify((E1 / (1 + z1)).subs({E1: 1, z1: sp.Rational(-99, 100)})) > 0, "EXACT sign argument (1+z>0 for |z|<1)")

# ----------------------------------------------------------------------------------------
# P9..  NUMERIC / FLOAT cross-checks (independent method: exact decaying-mode matching determinant F(E,K)).
# ----------------------------------------------------------------------------------------
mp.mp.dps = 40


def branch_mp(zv, mv):
    zv = mp.mpf(zv); mv = mp.mpf(mv)
    Ev = mp.sqrt(4 * mv ** 2 + (1 + zv) ** 2 / zv)
    qv = (2 + zv) / Ev
    tv = (qv + mp.sqrt(qv ** 2 + 16 * mv ** 2)) / 2
    cv = -(1 + zv) / Ev
    w1v = -1 / Ev
    Nv = w1v ** 2 + (1 + cv ** 2) / (1 - zv ** 2) + 4 * mv ** 2 * (1 / tv ** 2 + zv ** 2 / (Ev ** 2 * (1 - zv ** 2)))
    S1v = -1 / Ev + cv / (1 - zv)
    Qv = (2 * mv / tv) ** 2 + (2 * mv) ** 2 * (zv / Ev - 1 / tv) ** 2 + (2 * mv / Ev) ** 2 * zv ** 2 * (1 - zv) / (1 + zv)
    Wv = (Ev * S1v + Qv) / (2 * Nv)
    Vv = Ev - tv
    Uv = Vv * (1 + (2 * mv / tv) ** 2) / Nv
    return dict(E=Ev, t=tv, V=Vv, W=Wv, U=Uv, N=Nv)


def z_of_V(Vtarget, mv):
    """invert V(z) on the branch z in (-1, r_+), r_+ = the root in (-1,0) of z^2+(2+4m^2)z+1 (where E -> 0); V is monotone there."""
    mv = mp.mpf(mv)
    rplus = (-(2 + 4 * mv ** 2) + mp.sqrt((2 + 4 * mv ** 2) ** 2 - 4)) / 2
    lo = mp.mpf(-1) + mp.mpf("1e-15"); hi = rplus - mp.mpf("1e-12")
    flo = branch_mp(lo, mv)["V"] - mp.mpf(Vtarget); fhi = branch_mp(hi, mv)["V"] - mp.mpf(Vtarget)
    assert flo * fhi < 0
    for _ in range(140):
        mid = (lo + hi) / 2
        fm = branch_mp(mid, mv)["V"] - mp.mpf(Vtarget)
        if fm * flo > 0: lo, flo = mid, fm
        else: hi = mid
    return (lo + hi) / 2


def modes_mp(Ev, Kv, mv):
    c0v, s0v = mp.cos(Kv / 2), mp.sin(Kv / 2)
    pp = Ev ** 2 - 2 * c0v ** 2; qq = Ev ** 2 - 2 * s0v ** 2
    a2 = -c0v ** 2 * s0v ** 2; a1 = pp * s0v ** 2 - c0v ** 2 * qq; a0 = pp * qq - 4 * mv ** 2 * Ev ** 2
    disc = mp.sqrt(a1 ** 2 - 4 * a2 * a0)
    xs = [(-a1 + disc) / (2 * a2), (-a1 - disc) / (2 * a2)]
    Bm = mp.matrix([[-c0v, 0], [0, 1j * s0v]]); Bd = Bm.H
    sx = mp.matrix([[0, 1], [1, 0]])
    out = []
    for xv in xs:
        r1 = (xv + mp.sqrt(xv * xv - 4)) / 2; r2 = (xv - mp.sqrt(xv * xv - 4)) / 2
        zv = r1 if abs(r1) < abs(r2) else r2
        Mm = Ev * (Ev * mp.eye(2) - 2 * mv * sx) - mp.matrix([[c0v ** 2 * (xv + 2), 0], [0, -s0v ** 2 * (xv - 2)]])
        av = mp.matrix([-Mm[0, 1], Mm[0, 0]]); a2v = mp.matrix([-Mm[1, 1], Mm[1, 0]])
        if mp.norm(a2v) > mp.norm(av): av = a2v
        cvv = (Bm * zv + Bd) * av / Ev
        out.append((zv, av, cvv))
    return out, Bm, Bd, sx


def Fdet(Ev, Kv, mv, Vv):
    ms_, Bm, Bd, sx = modes_mp(Ev, Kv, mv)
    cols = []
    for zv, av, cvv in ms_:
        cols.append((Ev * mp.eye(2) - 2 * mv * sx - Vv * mp.eye(2) - Bd * Bm / Ev) * av - Bm * cvv)
    return mp.det(mp.matrix([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]])).real


def W_det(mv, Vv, E_start, h=mp.mpf("0.01"), n=6):
    mv = mp.mpf(mv); Vv = mp.mpf(Vv)
    Ks = [h * jj for jj in range(1, n + 1)]
    Es = []; cur = E_start
    for kk in Ks:
        cur = mp.findroot(lambda Ee: Fdet(Ee, kk, mv, Vv), cur); Es.append(cur)
    Am = mp.matrix(n, n); bm = mp.matrix(n, 1)
    for ii, kk in enumerate(Ks):
        for jj in range(n): Am[ii, jj] = kk ** (2 * jj)
        bm[ii] = Es[ii]
    cfit = mp.lu_solve(Am, bm)
    return cfit[0], 2 * cfit[1], cfit[0] * 2 * cfit[1]


worst = mp.mpf(0)
sup_vals = {-0.5: 0.117, -0.3: 0.201, -0.15: 0.411, -0.115: 0.539}
sup_ok = True
for Vt, wsup in sup_vals.items():
    zv = z_of_V(Vt, 4)
    br = branch_mp(zv, 4)
    E0d, Epp, Wd = W_det(4, Vt, br["E"] * (1 - mp.mpf("1e-9")))
    worst = max(worst, abs(Wd - br["W"]), abs(E0d - br["E"]))
    sup_ok &= abs(br["W"] - wsup) < 6e-4
chk(f"P9a NUMERIC: closed-form W (Hellmann-Feynman, K=0 states) equals W from the independent decaying-mode determinant F(E,K) (E(K) fitted, 40 digits) at m=4, V=-0.5,-0.3,-0.15,-0.115; max |diff| = {mp.nstr(worst, 3)}",
    worst < mp.mpf("1e-12"), "NUMERIC mpmath")
chk("P9b NUMERIC: reproduces the supervisor's exploration W = 0.117, 0.201, 0.411, 0.539 (m=4, V=-0.5,-0.3,-0.15,-0.115) to 3 digits", sup_ok, "NUMERIC")
worst2 = mp.mpf(0)
for (mv, Vt) in [(0.8, -0.9), (0.8, -0.5)]:
    zv = z_of_V(Vt, mv); br = branch_mp(zv, mv)
    E0d, Epp, Wd = W_det(mv, Vt, br["E"] * (1 - mp.mpf("1e-9")))
    worst2 = max(worst2, abs(Wd - br["W"]))
chk(f"P9c NUMERIC: same agreement at m=0.8 (V=-0.9,-0.5); max |diff| = {mp.nstr(worst2, 3)}", worst2 < mp.mpf("1e-12"), "NUMERIC")

# m -> infinity: effective half-line model W = 1/(4 m |V|)
mbig = 40
Vbig = -mp.mpf(1) / (4 * mbig) * mp.mpf("1.5")
zb_ = z_of_V(Vbig, mbig)
bb_ = branch_mp(zb_, mbig)
chk(f"P9d NUMERIC: at m=40, V=1.5 V_c: W = {mp.nstr(bb_['W'], 8)} vs the large-m half-line law 1/(4m|V|) = {mp.nstr(1 / (4 * mbig * abs(Vbig)), 8)} (relative difference {mp.nstr(abs(bb_['W'] * 4 * mbig * abs(Vbig) - 1), 3)} = O(1/m^2))",
    abs(bb_["W"] * 4 * mbig * abs(Vbig) - 1) < 2e-3, "NUMERIC")

# static-formula comparison with the actual lattice <T>, <U>
Rnum = []
for mv in (4, 0.8, 0.1):
    zv = mp.mpf(-1) + mp.mpf("1e-6")
    br = branch_mp(zv, mv)
    T = br["E"] - 2 * mp.mpf(mv) - br["U"]
    stat = -(T - br["U"] / 2) / mv
    Rnum.append((1 - br["W"]) / (-stat))
Rcl = [float(sp.N(Rm.subs(sb, sp.sqrt(64 * mb ** 4 + 1)).subs(mb, v), 12)) for v in (4, sp.Rational(4, 5), sp.Rational(1, 10))]
chk(f"P9e NUMERIC: exact deficit / static-formula deficit (actual lattice <T>,<U>): numeric {[float(mp.nstr(r_, 6)) for r_ in Rnum]} vs closed R(m) {[round(r_, 6) for r_ in Rcl]} at m=4, 0.8, 0.1",
    all(abs(float(a_) - b_) < 2e-4 * max(1, b_) for a_, b_ in zip(Rnum, Rcl)), "NUMERIC")

# mechanism: the leading deficit is the K-dependence of the critical coupling:  alpha = V_c''(0) / |dV/dδ|
def Fthr(Kv, mv, Vv):
    Ev = 2 * mp.sqrt(mv * mv + mp.sin(Kv / 2) ** 2)
    c0v, s0v = mp.cos(Kv / 2), mp.sin(Kv / 2)
    sx = mp.matrix([[0, 1], [1, 0]]); Bm = mp.matrix([[-c0v, 0], [0, 1j * s0v]]); Bd = Bm.H
    pp = Ev ** 2 - 2 * c0v ** 2; qq = Ev ** 2 - 2 * s0v ** 2
    a2 = -c0v ** 2 * s0v ** 2; a1 = pp * s0v ** 2 - c0v ** 2 * qq; a0 = pp * qq - 4 * mv ** 2 * Ev ** 2
    disc = mp.sqrt(a1 ** 2 - 4 * a2 * a0)
    xs = sorted([(-a1 + disc) / (2 * a2), (-a1 - disc) / (2 * a2)], key=lambda xv: abs(xv + 2))
    cols = []
    for jj, xv in enumerate(xs):
        if jj == 0: zv = mp.mpf(-1)
        else:
            r1 = (xv + mp.sqrt(xv * xv - 4)) / 2; r2 = (xv - mp.sqrt(xv * xv - 4)) / 2
            zv = r1 if abs(r1) < abs(r2) else r2
        Mm = Ev * (Ev * mp.eye(2) - 2 * mv * sx) - mp.matrix([[c0v ** 2 * (xv + 2), 0], [0, -s0v ** 2 * (xv - 2)]])
        av = mp.matrix([-Mm[0, 1], Mm[0, 0]]); a2v = mp.matrix([-Mm[1, 1], Mm[1, 0]])
        if mp.norm(a2v) > mp.norm(av): av = a2v
        cvv = (Bm * zv + Bd) * av / Ev
        cols.append((Ev * mp.eye(2) - 2 * mv * sx - Vv * mp.eye(2) - Bd * Bm / Ev) * av - Bm * cvv)
    return mp.det(mp.matrix([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]])).real


mech_ok = True; mech_txt = []
for mv in (4, 0.8):
    mvv = mp.mpf(mv)
    sval = mp.sqrt(64 * mvv ** 4 + 1)
    Vc0 = (8 * mvv ** 2 - 1 - sval) / (4 * mvv)
    Ks = [mp.mpf("0.02") * jj for jj in range(1, 6)]
    vals = []; g = Vc0
    for kk in Ks:
        g = mp.findroot(lambda Vv: Fthr(kk, mvv, Vv), g); vals.append(g)
    Am = mp.matrix(5, 5); bm = mp.matrix(5, 1)
    for ii, kk in enumerate(Ks):
        for jj in range(5): Am[ii, jj] = kk ** (2 * jj)
        bm[ii] = vals[ii]
    cfit = mp.lu_solve(Am, bm)
    Vcpp = 2 * cfit[1]
    dVdz_num = -(64 * mvv ** 4 + sval + 1) / (4 * mvv * (8 * mvv ** 2 - 4 * mvv + 1) * (8 * mvv ** 2 + 4 * mvv + 1))
    alpha_num = (16 * mvv ** 2 + 3 - sval) / (8 * mvv ** 2)
    mech_ok &= abs(cfit[0] - Vc0) < mp.mpf("1e-12") and abs(Vcpp / abs(dVdz_num) - alpha_num) < mp.mpf("1e-8")
    mech_txt.append(f"(fit errors {mp.nstr(abs(cfit[0] - Vc0), 2)}, {mp.nstr(abs(Vcpp / abs(dVdz_num) - alpha_num), 2)})")
    mech_txt.append(f"m={mv}: V_c''(0)={mp.nstr(Vcpp, 8)}, |dV/ddelta|={mp.nstr(abs(dVdz_num), 8)}, ratio {mp.nstr(Vcpp / abs(dVdz_num), 10)} vs alpha {mp.nstr(alpha_num, 10)}")
chk("P9f NUMERIC mechanism: V_c(K) (critical coupling at total momentum K, from the determinant at E=E_thr(K)) has V_c(0) as in P4b and  alpha(m) = V_c''(0)/|dV/ddelta|  -- " + "; ".join(mech_txt), mech_ok, "NUMERIC")

# FLOAT: finite-chain diagonalisation picks the same bound state (K=0) and shows no neighbour-term bound state
try:
    import numpy as np

    def fiber_np(N, K, mv, Vv, d):
        n = 2 * N; H = np.zeros((n, n), complex)
        c0v, s0v = np.cos(K / 2), np.sin(K / 2); Bm = np.diag([-c0v, 1j * s0v])
        for r in range(1, N + 1):
            i = 2 * (r - 1)
            if r % 2 == 0:
                H[i, i + 1] += 2 * mv; H[i + 1, i] += 2 * mv
            if r == d:
                H[i, i] += Vv; H[i + 1, i + 1] += Vv
            if r < N:
                j2 = 2 * r
                H[i:i + 2, j2:j2 + 2] += Bm; H[j2:j2 + 2, i:i + 2] += Bm.conj().T
        return np.linalg.eigvalsh(H)
    ev = fiber_np(1200, 0.0, 0.8, -0.9, 2)
    cand = [x for x in ev if 1e-6 < x < 1.6 - 1e-7]
    br = branch_mp(z_of_V(-0.9, 0.8), 0.8)
    chk(f"P10a FLOAT: finite chain (1200 sites) m=0.8, V=-0.9 has exactly one level in (0, 2m): {cand[-1]:.10f} vs branch E0 {mp.nstr(br['E'], 10)}",
        len(cand) == 1 and abs(cand[-1] - float(br["E"])) < 1e-8, "FLOAT numpy")
    none_ok = True
    for mv in (0.3, 0.8, 4):
        for Vv in (-0.5, -1.0, -3.0, -10.0):
            ev = fiber_np(900, 0.0, mv, Vv, 1)
            if any(1e-6 < x < 2 * mv - 1e-7 for x in ev): none_ok = False
    chk("P10b FLOAT: neighbour term (d=1), m=0.3,0.8,4 and V=-0.5,-1,-3,-10: no K=0 level in (0,2m) (consistent with P8)", none_ok, "FLOAT numpy")
except Exception as exc:                                    # numpy missing would be a failure of a check, not silently skipped
    chk("P10 FLOAT block ran", False, str(exc))

# ----------------------------------------------------------------------------------------
# P11  RIGOROUS INTERVALS: a fixed K^2-coefficient lambda cannot give W=1 beyond leading order.
#      W(lambda) = W0 + lambda E0 U exactly (Hellmann-Feynman in V).  lambda*(z) = (1-W0)/(E0 U) varies along the branch.
# ----------------------------------------------------------------------------------------
iv = mp.iv
iv.dps = 40


def branch_iv(zv, mv):
    Ev = iv.sqrt(4 * mv ** 2 + (1 + zv) ** 2 / zv)
    qv = (2 + zv) / Ev
    tv = (qv + iv.sqrt(qv ** 2 + 16 * mv ** 2)) / 2
    cv = -(1 + zv) / Ev; w1v = -1 / Ev
    Nv = w1v ** 2 + (1 + cv ** 2) / (1 - zv ** 2) + 4 * mv ** 2 * (1 / tv ** 2 + zv ** 2 / (Ev ** 2 * (1 - zv ** 2)))
    S1v = -1 / Ev + cv / (1 - zv)
    Qv = (2 * mv / tv) ** 2 + (2 * mv) ** 2 * (zv / Ev - 1 / tv) ** 2 + (2 * mv / Ev) ** 2 * zv ** 2 * (1 - zv) / (1 + zv)
    Wv = (Ev * S1v + Qv) / (2 * Nv)
    Uv = (Ev - tv) * (1 + (2 * mv / tv) ** 2) / Nv
    return Ev, Wv, Uv


iv_ok = True; iv_txt = []
for mtxt in ("4", "0.8", "0.1"):
    mv = iv.mpf(mtxt)
    sv = iv.sqrt(64 * mv ** 4 + 1)
    lam_0 = (-16 * mv ** 2 + sv - 3) / (-64 * mv ** 4 + 8 * mv ** 2 * sv + sv - 1)       # lambda*(m) from P7j (closed form)
    vals = []
    for dtxt in ("0.01", "0.001"):
        zv = -1 + iv.mpf(dtxt)
        Ev, Wv, Uv = branch_iv(zv, mv)
        lam_star = (1 - Wv) / (Ev * Uv)
        Wt = Wv + lam_0 * Ev * Uv
        bfrac = (2 * mv - Ev) / (2 * mv)
        vals.append((lam_star, Wt - 1, bfrac, iv.mpf(dtxt)))
    (l1, r1, b1, d1), (l2, r2, b2, d2) = vals
    disjoint = (l1.b < l2.a) or (l2.b < l1.a)
    pos = (r1.a > 0) and (r2.a > 0)
    big = (r2 / b2).a > 2
    iv_ok &= disjoint and pos and big
    iv_txt.append(f"m={mtxt}: lambda*(delta=.01)={mp.nstr(l1.mid, 8)}, (delta=.001)={mp.nstr(l2.mid, 8)}, tuned residual/binding-fraction at delta=.001: {mp.nstr((r2 / b2).mid, 6)}")
chk("P11 RIGOROUS (interval arithmetic): lambda*(delta) takes disjoint values at delta=0.01 and 0.001, so no single fixed K^2 coefficient makes W=1 at both; tuning lambda=lambda*(m) leaves W-1>0 and more than 2 times the binding fraction at delta=0.001 -- " + "; ".join(iv_txt),
    iv_ok, "mpmath.iv enclosures")

# ----------------------------------------------------------------------------------------
if FAIL == 0:
    print("HIT: Scoped, line only (coin-blind term at separation 2, one record per site, staggered mass m>0, K=0 bound branch): W = E0 E''(0) = (E0 S1 + Q)/(2N) in closed form; 1 - W = alpha(m) delta + O(delta^2), alpha(m) = (16 m^2 + 3 - sqrt(1+64 m^4))/(8 m^2) > 1, delta = 1+z the inverse size, while the binding fraction is delta^2/(8 m^2); the exact/static-formula deficit ratio is R(m) (21.9, 1.45, 0.373 at m=4, 0.8, 0.1); V(K)=V0(1+lambda K^2/2) shifts W by exactly lambda E0 <U>, needs lambda*(m)=O(1) to cancel the O(delta) deficit and a fixed lambda* leaves c2(m) delta^2 > 0; an attractive separation-1 term gives no K=0 level in (0,2m). Z^3 not treated.")
print(f"# runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("SUMMARY: exact closed-form pair weight for two massive staggered records on the line shows the inertia shortfall at the binding threshold is first order in the inverse pair size with coefficient alpha(m) > 1 (not the binding fraction, not the static formula), arising from the momentum dependence of the critical coupling, and that fixing it needs an O(1) momentum-dependent binding strength.")
sys.exit(0 if FAIL == 0 else 1)
