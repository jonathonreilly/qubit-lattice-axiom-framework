#!/usr/bin/env python3
"""Global zero / pi quasienergy touching set of the massless-normalised two-qubit
Clifford cubic walk family (b, G(b) PSD rank <= 3).

Self-contained: numpy, scipy-free, sympy, mpmath only.  Exact algebra (sympy
Groebner bases, ideal membership, exact radicals) for every finite claim; one
labelled numerical scan (disjoint method) at the end.
"""
import itertools
import sys
import time

import numpy as np
import sympy as sp
import mpmath as mp

T_START = time.time()
mp.mp.dps = 60

PASSED = 0
FAILED = 0


def check(name, ok):
    global PASSED, FAILED
    if ok:
        PASSED += 1
        print("PASS " + name)
    else:
        FAILED += 1
        print("FAIL " + name)


def info(msg):
    print("INFO " + msg)


# ----------------------------------------------------------------------------
# Setup: Gram matrix G(b) of (f, h1, h2) over phi = (1, e1, e2, e3)
# ----------------------------------------------------------------------------
b0, b1, b2 = sp.symbols('b0 b1 b2', real=True)
G = sp.Matrix([
    [1 - 3 * b0**2, -2 * b0 * b1, b1**2 - b0**2 - b0 * b2, -3 * b1 * (b0 - b2)],
    [-2 * b0 * b1, b0**2 - 2 * b1**2, b1 * (b0 - b2), b0 * b2 - b1**2 + b2**2],
    [b1**2 - b0**2 - b0 * b2, b1 * (b0 - b2), 2 * b1**2 - b2**2, 2 * b1 * b2],
    [-3 * b1 * (b0 - b2), b0 * b2 - b1**2 + b2**2, 2 * b1 * b2, 3 * b2**2]])


def phi(c):
    return sp.Matrix([1, c[0] + c[1] + c[2], c[0] * c[1] + c[0] * c[2] + c[1] * c[2], c[0] * c[1] * c[2]])


P0 = phi((1, 1, 1))
TRIM = {'0': (1, 1, 1), 'X': (-1, 1, 1), 'M': (-1, -1, 1), 'R': (-1, -1, -1)}


def GB(eqs, gens, order='lex'):
    return sp.groebner([sp.expand(e) for e in eqs], *gens, order=order)


def in_rad(gb, p, mmax=8):
    p = sp.expand(p)
    return any(gb.contains(sp.expand(p**m)) for m in range(1, mmax + 1))


def covers(gb, branches):
    """V(I) is contained in the union of V(J_i) (over C): every product of one
    generator per branch lies in sqrt(I)."""
    return all(in_rad(gb, sp.Mul(*combo)) for combo in itertools.product(*branches))


def psd_eigs(bv, dps=60):
    mp.mp.dps = dps
    Gn = mp.matrix(G.subs({b0: bv[0], b1: bv[1], b2: bv[2]}).evalf(dps).tolist())
    return sorted(mp.eigsy(Gn, eigvals_only=True))


def is_admissible(bv, tol_zero=mp.mpf(10)**-40, tol_pos=mp.mpf(10)**-6):
    """G PSD of rank <= 3 (smallest eigenvalue 0 to 40 digits, rest >= 0)."""
    ev = psd_eigs(bv)
    return abs(ev[0]) < tol_zero and all(e > -tol_zero for e in ev)


# ----------------------------------------------------------------------------
# Part 0: algebraic identities used (exact)
# ----------------------------------------------------------------------------
c1, c2, c3, s1, s2, s3 = sp.symbols('c1 c2 c3 s1 s2 s3', real=True)
C = (c1, c2, c3)
Sn = (s1, s2, s3)
PH = phi(C)
VEC = [[s1, s2, s3],
       [s1 * (c2 + c3), s2 * (c1 + c3), s3 * (c1 + c2)],
       [s1 * c2 * c3, s2 * c1 * c3, s3 * c1 * c2]]
gvec = [sum(bb * VEC[j][a] for j, bb in enumerate((b0, b1, b2))) for a in range(3)]
trig_rels = [s**2 + c**2 - 1 for s, c in zip(Sn, C)]


def trig_zero(expr):
    rem = sp.reduced(sp.expand(expr), trig_rels, *Sn, *C, order='lex')[1]
    return sp.expand(rem) == 0


quad = (PH.T * G * PH)[0]
gsq = sum(x**2 for x in gvec)
check("0.1 Gram identity phi^T G phi + |g|^2 = 1 identically in k (s_a^2 = 1 - c_a^2)",
      trig_zero(quad + gsq - 1))
check("0.2 phi0^T G phi0 = 1 exactly (g(0)=0)", sp.expand((P0.T * G * P0)[0] - 1) == 0)
Ba = [b0 + b1 * (c2 + c3) + b2 * c2 * c3, b0 + b1 * (c1 + c3) + b2 * c1 * c3, b0 + b1 * (c1 + c2) + b2 * c1 * c2]
check("0.3 g_a = sin(k_a) * B_a(c) with B_a = b0 + b1 (c_b + c_c) + b2 c_b c_c",
      all(sp.expand(gvec[a] - Sn[a] * Ba[a]) == 0 for a in range(3)))
check("0.4 B_1 - B_2 = (c2 - c1)(b1 + b2 c3)  (and cyclic)",
      sp.expand(Ba[0] - Ba[1] - (c2 - c1) * (b1 + b2 * c3)) == 0
      and sp.expand(Ba[1] - Ba[2] - (c3 - c2) * (b1 + b2 * c1)) == 0)
f_expr = (P0.T * G * PH)[0]
for eps in (1, -1):
    psi = PH - eps * P0
    check("0.5 identity (phi - %d phi0)^T G (phi - %d phi0) + |g|^2 = 2 - 2 (%d) f, f = phi0^T G phi" % (eps, eps, eps),
          trig_zero((psi.T * G * psi)[0] + gsq - 2 + 2 * eps * f_expr))
check("0.6 G(-b) = G(b) (spectrum symmetric under b -> -b)",
      sp.expand(G.subs({b0: -b0, b1: -b1, b2: -b2}, simultaneous=True) - G) == sp.zeros(4))
Dm = sp.diag(1, -1, 1, -1)
check("0.7 G(b0,-b1,b2) = D G(b) D, D = diag(1,-1,1,-1) (the Q=(pi,pi,pi) shift, phi(k+Q) = D phi(k))",
      sp.expand(G.subs(b1, -b1) - Dm * G * Dm) == sp.zeros(4))

# ----------------------------------------------------------------------------
# Part 1: Reduction (Lemma 1) -- logic stated in ATTEMPT.md; here the PSD part
# ----------------------------------------------------------------------------
# The logical reduction (PSD => f = +-1 iff G(phi -+ phi0) = 0, and then g = 0) uses 0.5.
# Non-PSD exclusions used below:
tt = sp.symbols('tt', real=True)
line1 = {b0: tt, b1: -tt, b2: tt}
G_l1 = G.subs(line1).applyfunc(sp.expand)
check("1.1 b = t(1,-1,1): G11 = -t^2 < 0 for t != 0, so not PSD", sp.expand(G_l1[1, 1] + tt**2) == 0)
line2 = {b0: tt, b1: tt, b2: tt}
G_l2 = G.subs(line2).applyfunc(sp.expand)
lam = sp.symbols('lam')
cp2 = sp.Poly(sp.expand((G_l2 - lam * sp.eye(4)).det()), lam).all_coeffs()
# char poly = lam^4 - e1 lam^3 + e2 lam^2 - e3 lam + e4, PSD needs all e_i >= 0
check("1.2 b = t(1,1,1): e3 = -6 t^4 < 0 (char-poly coefficient), so not PSD for t != 0",
      sp.expand(-cp2[3] + 6 * tt**4) == 0 and sp.expand(cp2[4]) == 0)
G_l3 = G.subs({b0: 0, b2: 0}).applyfunc(sp.expand)
check("1.3 b = (0,b1,0): G11 = -2 b1^2 < 0 for b1 != 0, so not PSD", sp.expand(G_l3[1, 1] + 2 * b1**2) == 0)
check("1.4 PSD forces |b2| <= 1/3 (minors: G11>=0, G00>=0, 2x2 minor of G22,G33 => b0^2>=2b1^2>=3b2^2, 3b0^2<=1)",
      sp.expand((G[2, 2] * G[3, 3] - G[2, 3]**2) - (2 * b1**2 * b2**2 - 3 * b2**4)) == 0)

# ----------------------------------------------------------------------------
# Part 2: TRIM points (all c_a = +-1)
# ----------------------------------------------------------------------------
gens3 = [b0, b1, b2]
line_b = [b0 - b2, b1 + b2]   # b = t(1,-1,1)
zero_b = [b0, b1, b2]
for name in ('X', 'M', 'R'):
    psi = phi(TRIM[name]) - P0
    gb = GB(list(G * psi), gens3)
    br = [zero_b, line_b] if name == 'X' else [zero_b]
    check("2.%s0 TRIM class %s, f = +1 (G(phi_T - phi0) = 0): complex solutions of the 4 equations lie in %s"
          % (name, name, "{b=0} u {b = t(1,-1,1)}" if name == 'X' else "{b=0}"), covers(gb, br))

# pi at TRIM: finite sets
xp_gb = GB(list(G * (phi(TRIM['X']) + P0)), gens3)
mp_gb = GB(list(G * (phi(TRIM['M']) + P0)), gens3)
rp_gb = GB(list(G * (phi(TRIM['R']) + P0)), gens3)


def shape_lemma(gb):
    """expects [b0 - p0(b2), b1 - p1(b2), r(b2)] up to scaling"""
    ex = gb.exprs
    lin0 = [e for e in ex if sp.Poly(e, b0).degree() == 1 and sp.Poly(e, b1).degree() == 0 and sp.Poly(e, b0).LC() == sp.Poly(e, b0).LC().as_independent(b2)[0]]
    lin1 = [e for e in ex if sp.Poly(e, b1).degree() == 1 and sp.Poly(e, b0).degree() == 0 and sp.Poly(e, b1).LC().free_symbols == set()]
    uni = [e for e in ex if e.free_symbols == {b2}]
    if len(lin0) != 1 or len(lin1) != 1 or len(uni) != 1 or len(ex) != 3:
        return None
    sol0 = sp.solve(lin0[0], b0)[0]
    sol1 = sp.solve(lin1[0], b1)[0]
    return sol0, sol1, sp.Poly(uni[0], b2)


members = []   # (label, (b0,b1,b2) mp tuple, trim class)
shX = shape_lemma(xp_gb)
check("2.X1 TRIM X, f = -1: Groebner basis has shape b0 = p(b2), b1 = q(b2), r(b2) = 0 (zero-dimensional)", shX is not None)
shM = shape_lemma(mp_gb)
check("2.M1 TRIM M, f = -1: Groebner basis has shape b0 = p(b2), b1 = q(b2), r(b2) = 0 (zero-dimensional)", shM is not None)

for lab, sh in (('X', shX), ('M', shM)):
    p0e, p1e, rp = sh
    roots = [r for r in rp.real_roots()]
    nreal = len(roots)
    psd_list = []
    for r in roots:
        rv = sp.N(r, 60)
        bv = (sp.N(p0e.subs(b2, rv), 60), sp.N(p1e.subs(b2, rv), 60), rv)
        res = G.subs({b0: bv[0], b1: bv[1], b2: bv[2]}) * (phi(TRIM[lab]) + P0)
        resn = max(abs(sp.N(x, 50)) for x in res)
        ev = psd_eigs(bv)
        adm = is_admissible(bv)
        info("class %s pi-root b = (%s, %s, %s), residual %s, eigs %s admissible=%s" %
             (lab, sp.N(bv[0], 10), sp.N(bv[1], 10), sp.N(bv[2], 10), sp.N(resn, 3),
              [mp.nstr(e, 5) for e in ev], adm))
        if adm:
            psd_list.append(bv)
    check("2.%s2 real solutions of G(phi_%s + phi0) = 0: %d real points, %d of them with G PSD rank 3 (a +- pair)"
          % (lab, lab, nreal, len(psd_list)), nreal == 4 and len(psd_list) == 2)
    for bv in psd_list:
        members.append((lab, bv))

# R class: explicit
check("2.R1 TRIM R, f = -1: ideal equals <59 b0 - 177 b2, 177 b1^2 - 1188 b2^4 - 132 b2^2 - 4, b1 (396 b2^2 - 7), (396 b2^2 - 7)(297 b2^4 + 33 b2^2 + 1)>",
      all(rp_gb.contains(sp.expand(p)) for p in [59 * b0 + 39204 * b2**5 - 1485 * b2**3 - 163 * b2,
                                                  177 * b1**2 - 1188 * b2**4 - 132 * b2**2 - 4,
                                                  b1 * (396 * b2**2 - 7),
                                                  (396 * b2**2 - 7) * (297 * b2**4 + 33 * b2**2 + 1)])
      and len(rp_gb.exprs) == 4)
quadR = sp.Poly(297 * sp.Symbol('y')**2 + 33 * sp.Symbol('y') + 1, sp.Symbol('y'))
check("2.R2 297 y^2 + 33 y + 1 has negative discriminant (no real b2^2), so b2^2 = 7/396, hence b1^2 = 5/132 and b0 = 3 b2",
      33**2 - 4 * 297 < 0 and sp.simplify(177 * sp.Rational(5, 132) - (1188 * sp.Rational(7, 396)**2 + 132 * sp.Rational(7, 396) + 4)) == 0
      and sp.simplify(-(39204 * sp.Rational(7, 396)**2 - 1485 * sp.Rational(7, 396) - 163) / 59 - 3) == 0)
r77, r165 = sp.sqrt(77), sp.sqrt(165)
for sg2, sg1 in itertools.product((1, -1), (1, -1)):
    bR = (sg2 * r77 / 22, sg1 * sg2 * r165 / 66, sg2 * r77 / 66)   # product sign: b1 sign relative to b2
    # sign relation classes: (b2>0,b1>0),(b2>0,b1<0),(b2<0,b1<0)=-(first),(b2<0,b1>0)=-(second)
    resR = sp.simplify(sp.expand(G.subs({b0: bR[0], b1: bR[1], b2: bR[2]}) * (phi(TRIM['R']) + P0)))
    bv = tuple(sp.N(x, 60) for x in bR)
    check("2.R3 exact: b_R = (%s, %s, %s) solves G(phi_R + phi0) = 0 and is PSD rank 3"
          % (sp.nsimplify(bR[0]), sp.nsimplify(bR[1]), sp.nsimplify(bR[2])),
          resR == sp.zeros(4, 1) and is_admissible(bv))
    members.append(('R', bv))

# gold exact check (X)
r5 = sp.sqrt(5)
bgold = (((9 * r5 - 5) / 38), ((5 * r5 - 7) / 19), ((71 - 29 * r5) / 38))
resg = sp.simplify(sp.expand(G.subs({b0: bgold[0], b1: bgold[1], b2: bgold[2]}) * (phi(TRIM['X']) + P0)))
check("2.X3 exact: b_gold solves G(phi_X + phi0) = 0 (source Theorem 5), so it is one of the PSD real points above",
      resg == sp.zeros(4, 1) and any(abs(m[1][0] - sp.N(bgold[0], 40)) < 1e-30 for m in members if m[0] == 'X'))

# M-class exact residual: reduce modulo minimal polynomial of b2
p0e, p1e, rpM = shM
polyM = rpM.as_expr()
resM = [sp.simplify(sp.rem(sp.numer(sp.together(x)), polyM, b2)) for x in
        (G.subs({b0: p0e, b1: p1e}) * (phi(TRIM['M']) + P0))]
check("2.M3 exact: G(b0(b2), b1(b2), b2)(phi_M + phi0) reduces to 0 modulo the degree-8 minimal relation r(b2)",
      all(x == 0 for x in resM))

# ----------------------------------------------------------------------------
# Part 3: Z(b) strata with at least one interior axis (g=0 but not a TRIM point)
# ----------------------------------------------------------------------------
x, gm, t = sp.symbols('x gm t')


def psi_of(c, sgn):
    return phi(c) + sgn * P0


# |A|=1 : c = (x, e2, e3) with e2,e3 = +-1, x in (-1,1); B_1 = b0 + b1(e2+e3) + b2 e2 e3 = 0
S1 = {(1, 1): (b0 + 2 * b1 + b2), (1, -1): (b0 - b2), (-1, -1): (b0 - 2 * b1 + b2)}
for (e2, e3), rel in S1.items():
    # zero (f=+1): psi = phi - phi0, saturate x != 1
    eqs = list(G * psi_of((x, e2, e3), -1)) + [rel, t * (x - 1) - 1]
    gb = GB(eqs, [t, x] + gens3)
    br = [zero_b, line_b] if (e2, e3) == (1, 1) else [zero_b]
    check("3.1 axis-line stratum c=(x,%d,%d), x in (-1,1), f=+1: solutions in %s" %
          (e2, e3, "{0} u {t(1,-1,1)}" if (e2, e3) == (1, 1) else "{b=0}"), covers(gb, br))
    # pi (f=-1)
    eqs = list(G * psi_of((x, e2, e3), 1)) + [rel]
    gb = GB(eqs, [x] + gens3)
    if (e2, e3) == (-1, -1):
        ok = gb.contains(sp.expand(8 * x - 31)) and not bool(-1 <= sp.Rational(31, 8) <= 1)
        check("3.2 axis-line stratum c=(x,-1,-1), f=-1: forces x = 31/8, outside [-1,1]", ok)
    else:
        check("3.2 axis-line stratum c=(x,%d,%d), f=-1: ideal is the unit ideal (no complex solution at all)" % (e2, e3),
              list(gb.exprs) == [1])

# |A|=2 : c = (g,g,eps) with g(b1 + eps b2) + (b0 + eps b1) = 0   (from B_1 = B_2 = 0)
for eps in (1, -1):
    rel = gm * (b1 + eps * b2) + (b0 + eps * b1)
    eqs = list(G * psi_of((gm, gm, eps), -1)) + [rel, t * (gm - 1) - 1]
    gb = GB(eqs, [t, gm] + gens3)
    check("3.3 diagonal stratum c=(g,g,%d), g != 1, f=+1: solutions in {b=0}" % eps, covers(gb, [zero_b]))
    eqs = list(G * psi_of((gm, gm, eps), 1)) + [rel]
    gb = GB(eqs, [gm] + gens3)
    if eps == 1:
        check("3.4 diagonal stratum c=(g,g,+1), f=-1: forces g = -2, outside [-1,1]", gb.contains(sp.expand(gm + 2)))
    else:
        cub = sp.Poly((gm + 4) * (gm**3 + 10 * gm**2 + 17 * gm - 44), gm)
        check("3.4 diagonal stratum c=(g,g,-1), f=-1: g is a root of (g+4)(g^3+10g^2+17g-44), none in [-1,1]",
              gb.contains(cub.as_expr()) and cub.count_roots(-1, 1) == 0)

# face degeneracy of the |A|=2 relation (b1 + eps b2 = 0 and b0 + eps b1 = 0): b = t(1,-1,1) (eps=1) or t(1,1,1) (eps=-1)
check("3.5 relation b1+eps b2 = 0 = b0+eps b1 gives exactly the lines t(1,-1,1) (eps=+1), t(1,1,1) (eps=-1); both non-PSD (1.1, 1.2)",
      sp.solve([b1 + b2, b0 + b1], [b0, b1], dict=True) == [{b0: b2, b1: -b2}]
      and sp.solve([b1 - b2, b0 - b1], [b0, b1], dict=True) == [{b0: b2, b1: b2}])

# |A|=3, all three c equal: c = (g,g,g) with B(g) = b0 + 2 b1 g + b2 g^2 = 0
Bd = b0 + 2 * b1 * gm + b2 * gm**2
eqs = list(G * psi_of((gm, gm, gm), -1)) + [Bd, t * (gm - 1) - 1]
gb = GB(eqs, [t, gm] + gens3)
check("3.6 body-diagonal stratum c=(g,g,g), g != 1, f=+1: forces b0 = b2 = 0, then b = (0,b1,0) which is non-PSD unless b1=0 (1.3)",
      covers(gb, [[b0, b2]]))
eqs = list(G * psi_of((gm, gm, gm), 1)) + [Bd]
gb = GB(eqs, gens3 + [gm])
quart = sp.Poly(8 * gm**4 + 47 * gm**3 + 138 * gm**2 + 201 * gm + 141, gm)
check("3.7 body-diagonal stratum c=(g,g,g), f=-1: g is a root of 8g^4+47g^3+138g^2+201g+141, which has no real root",
      gb.contains(quart.as_expr()) and quart.count_roots() == 0)

# |A|=3, exactly two equal: c = (g,g,x), b = B2 (g^2, -g, 1)
B2s = sp.Symbol('B2s')
Gs = G.subs({b0: B2s * gm**2, b1: -B2s * gm, b2: B2s}).applyfunc(sp.expand)
eqs = [sp.expand(q) for q in Gs * psi_of((gm, gm, x), -1)] + [t * (x - 1) - 1]
gb = GB(eqs, [t, B2s, gm, x])
check("3.8 two-equal stratum c=(g,g,x) (b0 b2 = b1^2, g = -b1/b2), x != 1, f=+1: B2^2 (g-1) = 0 so b = 0 or b = B2 (1,-1,1) (non-PSD)",
      gb.contains(sp.expand(B2s**2 * (gm - 1))) and in_rad(gb, B2s * (gm - 1)))
eqs = [sp.expand(q) for q in Gs * psi_of((gm, gm, x), 1)]
gb = GB(eqs, [B2s, gm, x])
check("3.9 two-equal stratum c=(g,g,x), f=-1: unit ideal (no solution)", list(gb.exprs) == [1])

# all distinct interior with all B_a = 0 forces b1 = b2 = 0 hence b0 = 0 (from 0.4 and B_a)
d1, d2, d3 = sp.symbols('d1 d2 d3')
gbd = GB([Ba[0], Ba[1], Ba[2], (c1 - c2) * d1 - 1, (c2 - c3) * d2 - 1, (c3 - c1) * d3 - 1], [d1, d2, d3, c1, c2, c3, b0, b1, b2])
check("3.10 three pairwise-distinct interior c_a with B_1 = B_2 = B_3 = 0 forces b = 0", covers(gbd, [zero_b]))

# s = 0 corollary: w^T G w = s^2, so s=0 & PSD => G w = 0
wv = sp.Matrix([0, 1, 2, 1])
vv = sp.Matrix([1, 2, 1, 0])
sc = b0 + 2 * b1 + b2
check("3.11 identities v^T G v = 1 - s^2, w^T G w = s^2, v^T G w = 0 (source Theorem 4)",
      sp.expand((vv.T * G * vv)[0] - (1 - sc**2)) == 0 and sp.expand((wv.T * G * wv)[0] - sc**2) == 0
      and sp.expand((vv.T * G * wv)[0]) == 0)
gbw = GB(list(G * wv), gens3)
check("3.12 G w = 0 has complex solutions only in {b=0} u {b = t(1,-1,1)}; the line is non-PSD, so an admissible b with s = 0 is b = 0",
      covers(gbw, [zero_b, line_b]))

# TRIM-TRIM pairs (normalising the member at another TRIM class instead of k=0): F(T1) = -+F(T2), T1,T2 in {X,M,R}
def pair_gb(a, bcl, sgn):
    return GB(list(G * (phi(TRIM[a]) - sgn * phi(TRIM[bcl]))), gens3)


def same_ideal(g1, g2):
    return all(g1.contains(e) for e in g2.exprs) and all(g2.contains(e) for e in g1.exprs)


for a, bcl, brs in (('X', 'M', [zero_b]), ('X', 'R', [zero_b]), ('M', 'R', [zero_b, [b0 - b2, b1 - b2]])):
    check("3.13 pair (%s,%s) with F(%s) = +F(%s): complex solutions in %s (t(1,1,1) is non-PSD)" %
          (a, bcl, a, bcl, "{b=0}" if len(brs) == 1 else "{b=0} u {t(1,1,1)}"), covers(pair_gb(a, bcl, 1), brs))
gb_xm = pair_gb('X', 'M', -1)
last = [e for e in gb_xm.exprs if e.free_symbols == {b2}][0]
rr = [r for r in sp.Poly(last, b2).real_roots()]
check("3.14 pair (X,M) with F(X) = -F(M): b2 is a root of (4b2^2-9)(b2^4-7b2^2+1); every real root has |b2| > 1/3, violating PSD (1.4)",
      len(rr) > 0 and all(abs(float(sp.N(r))) > 1 / 3 for r in rr))
flip = lambda gbx: GB([e.subs(b1, -b1) for e in gbx.exprs], gens3)
check("3.15 pair (X,R) with F(X) = -F(R) is the b1 -> -b1 image of the (M,0) pi system; pair (M,R) with F(M) = -F(R) is the image of the (X,0) pi system",
      same_ideal(pair_gb('X', 'R', -1), flip(mp_gb)) and same_ideal(pair_gb('M', 'R', -1), flip(xp_gb)))

# ----------------------------------------------------------------------------
# Part 4: the members of P, their nodes, and the Dirac cones
# ----------------------------------------------------------------------------
members_sorted = sorted(members, key=lambda m: (m[0], float(m[1][2])))
info("P has %d members (lists below)" % len(members_sorted))
cnt = {k: sum(1 for m in members_sorted if m[0] == k) for k in 'XMR'}
check("4.1 P = 2 (X: +-b_gold) + 2 (M: +-b_M) + 4 (R) = 8 admissible members with a pi-touching TRIM node",
      cnt == {'X': 2, 'M': 2, 'R': 4})

f_fun = sp.lambdify((b0, b1, b2) + C, f_expr, 'mpmath')
cos_th = {k: sp.lambdify((b0, b1, b2), (P0.T * G * phi(TRIM[k]))[0], 'mpmath') for k in 'XMR'}
ok_all = True
for lab, bv in members_sorted:
    vals = {k: cos_th[k](*bv) for k in 'XMR'}
    pi_set = [k for k in 'XMR' if abs(vals[k] + 1) < mp.mpf(10)**-40]
    zero_set = [k for k in 'XMR' if abs(vals[k] - 1) < mp.mpf(10)**-40]
    info("member %s b=(%s,%s,%s): cos theta_X,M,R = %s" %
         (lab, mp.nstr(bv[0], 8), mp.nstr(bv[1], 8), mp.nstr(bv[2], 8), [mp.nstr(vals[k], 8) for k in 'XMR']))
    ok_all &= (pi_set == [lab]) and zero_set == []
check("4.2 at each member of P exactly one TRIM class is a pi node, and it is the predicted class; no TRIM class touches 0", ok_all)

# distinctness of the members (cone speed s separates classes)
spd = sorted(float(abs(m[1][0] + 2 * m[1][1] + m[1][2])) for m in members_sorted)
info("cone speeds |s| of the P members: " + ", ".join("%.4f" % z for z in spd))

# nodes: Jacobian of g, and the local cone (pi - omega)^2 = |J q|^2 + ...
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
ck = [sp.cos(k1), sp.cos(k2), sp.cos(k3)]
sk = [sp.sin(k1), sp.sin(k2), sp.sin(k3)]
gfun = [sk[a] * (b0 + b1 * (ck[(a + 1) % 3] + ck[(a + 2) % 3]) + b2 * ck[(a + 1) % 3] * ck[(a + 2) % 3]) for a in range(3)]
Jac = sp.Matrix(3, 3, lambda i, j: sp.diff(gfun[i], (k1, k2, k3)[j]))
nodes = {'X': (sp.pi, 0, 0), 'M': (sp.pi, sp.pi, 0), 'R': (sp.pi, sp.pi, sp.pi)}
Jn = {k: Jac.subs(dict(zip((k1, k2, k3), nodes[k]))).applyfunc(sp.simplify) for k in 'XMR'}
check("4.3 Jacobian of g at the nodes: X: diag(-s, b0-b2, b0-b2); M(pi,pi,0): diag(-(b0-b2), -(b0-b2), b0-2b1+b2); R: -(b0-2b1+b2) 1",
      Jn['X'] == sp.diag(-(b0 + 2 * b1 + b2), b0 - b2, b0 - b2)
      and Jn['M'] == sp.diag(-(b0 - b2), -(b0 - b2), b0 - 2 * b1 + b2)
      and Jn['R'] == -(b0 - 2 * b1 + b2) * sp.eye(3))
Jlam = {k: sp.lambdify((b0, b1, b2), Jn[k], 'mpmath') for k in 'XMR'}
ok_cone = True
rng = np.random.default_rng(7)
for lab, bv in members_sorted:
    J = Jlam[lab](*bv)
    detJ = mp.det(J)
    nondeg = abs(detJ) > mp.mpf(10)**-6
    # numerical dispersion near the node
    ndp = nodes[lab]
    worst = 0.0
    for _ in range(4):
        d = rng.normal(size=3)
        d /= np.linalg.norm(d)
        q = mp.mpf('1e-3')
        kk = [mp.mpf(sp.N(ndp[i], 60)) + q * mp.mpf(float(d[i])) for i in range(3)]
        fv = f_fun(*bv, *[mp.cos(z) for z in kk])
        omega = mp.acos(fv)
        lhs = mp.pi - omega
        qv = mp.matrix([q * mp.mpf(float(d[i])) for i in range(3)])
        rhs = mp.norm(J * qv)
        worst = max(worst, float(abs(lhs / rhs - 1)))
    info("node %s of member b=(%s,...): det J = %s, max |(pi-omega)/|Jq| - 1| = %.2e" % (lab, mp.nstr(bv[0], 6), mp.nstr(detJ, 5), worst))
    ok_cone &= nondeg and worst < 5e-3
check("4.4 every pi node of P is a massless Dirac cone: det J != 0 and (pi - omega) = |J q| (1 + O(q)) numerically at |q| = 1e-3", ok_cone)

# R members come in pairs (b0,b1,b2), (b0,-b1,b2) that are the same spectrum relabelled: f_B(k) = -f_A(k+Q)
Rm = [m[1] for m in members_sorted if m[0] == 'R']
ok_pair = True
rng2 = np.random.default_rng(3)
for A in Rm:
    B = (A[0], -A[1], A[2])
    assert any(all(abs(B[i] - Z[i]) < mp.mpf(10)**-40 for i in range(3)) for Z in Rm)
    for _ in range(5):
        kk = [mp.mpf(float(z)) for z in rng2.uniform(0, 2 * np.pi, 3)]
        fA = f_fun(*A, *[mp.cos(z + mp.pi) for z in kk])
        fB = f_fun(*B, *[mp.cos(z) for z in kk])
        ok_pair &= abs(fB + fA) < mp.mpf(10)**-40
check("4.5 the four R members form two pairs (b0,b1,b2) <-> (b0,-b1,b2) with f_B(k) = -f_A(k+Q): one spectrum, relabelled by the shift k -> k+(pi,pi,pi) and omega -> omega+pi", ok_pair)

Mm = [m[1] for m in members_sorted if m[0] == 'M']
check("4.6 (numerical, 60 digits) the M members have cone speed s = +-(sqrt2 + sqrt6)/4 = +-cos(pi/12), i.e. cos theta_X = -sqrt3/2 at the axis points",
      all(abs(abs(B[0] + 2 * B[1] + B[2]) - (mp.sqrt(2) + mp.sqrt(6)) / 4) < mp.mpf(10)**-45 for B in Mm) and len(Mm) == 2)

# ----------------------------------------------------------------------------
# Part 5: consequences for the named explicit members and the source's b*, b_iso
# ----------------------------------------------------------------------------
uu = sp.Symbol('uu')
detG = sp.expand(G.det())
quartic_u = sp.Poly(sp.expand(detG.subs({b0: sp.Rational(11, 30), b2: sp.Rational(3, 20)}).subs(b1, sp.sqrt(uu))), uu)
rts = [r for r in quartic_u.nroots(n=60) if abs(sp.im(r)) < 1e-40 and sp.re(r) > 0]
ustar = min(sp.re(r) for r in rts)
bstar = (sp.N(sp.Rational(11, 30), 60), sp.sqrt(sp.N(ustar, 60)), sp.N(sp.Rational(3, 20), 60))
ev = psd_eigs(bstar)
check("5.1 source's b* = (11/30, sqrt(u*), 3/20): det G = 0 and G PSD of rank 3 (eigs %s)" % [mp.nstr(e, 4) for e in ev],
      is_admissible(bstar) and ev[1] > 1e-3)
r6, r15 = sp.sqrt(6), sp.sqrt(15)
biso = tuple(sp.N(z, 60) for z in ((r6 + 2 * r15) / 27, (5 * r6 - 2 * r15) / 27, (2 * r15 - 2 * r6) / 27))
check("5.2 source's b_iso: G PSD of rank 3", is_admissible(biso) and psd_eigs(biso)[1] > 1e-5)


def dist_to_P(bv):
    return min(float(mp.norm(mp.matrix([bv[i] - m[1][i] for i in range(3)]))) for m in members_sorted)


for nm, bv in (('b*', bstar), ('b_iso', biso)):
    vals = {k: cos_th[k](*bv) for k in 'XMR'}
    margin = min(float(v + 1) for v in vals.values())
    check("5.3 %s: not in P (distance %.4f), b != 0, so by the theorem T_0 = {k=0}, T_pi = empty; TRIM cos values %s"
          % (nm, dist_to_P(bv), [mp.nstr(vals[k], 6) for k in 'XMR']),
          dist_to_P(bv) > 1e-3 and margin > 0.05)

# ----------------------------------------------------------------------------
# Part 6: disjoint numerical scan (labelled numerical)
# ----------------------------------------------------------------------------
Gfun = sp.lambdify((b0, b1, b2), G, 'numpy')
du = sp.Poly(sp.expand(detG).subs(b1, sp.sqrt(uu)), uu)
coef_f = [sp.lambdify((b0, b2), cf, 'numpy') for cf in du.all_coeffs()]
n = 24
ks = np.linspace(0, np.pi, n + 1)
K = np.array(np.meshgrid(ks, ks, ks, indexing='ij')).reshape(3, -1)
cK = np.cos(K)
PHI = np.vstack([np.ones(cK.shape[1]), cK.sum(0), cK[0] * cK[1] + cK[0] * cK[2] + cK[1] * cK[2], cK[0] * cK[1] * cK[2]])
p0n = np.array([1., 3., 3., 1.])
w2 = (np.sin(K / 2)**2).sum(0)
Pnum = np.array([[float(z) for z in m[1]] for m in members_sorted])

rng = np.random.default_rng(11)
samples = []
for _ in range(25000):
    B0 = rng.uniform(-0.58, 0.58)
    B2 = rng.uniform(-0.34, 0.34)
    cs = [float(fn(B0, B2)) for fn in coef_f]
    if cs[0] == 0:
        continue
    for r in np.roots(cs):
        if abs(r.imag) < 1e-12 and r.real >= 0:
            for sg in (1, -1):
                bv = np.array([B0, sg * np.sqrt(r.real), B2])
                if np.linalg.eigvalsh(np.array(Gfun(*bv), dtype=float))[0] > -1e-10:
                    samples.append(bv)
# add perturbations of P members (so the scan probes the neighbourhoods)
for pm in Pnum:
    for _ in range(40):
        samples.append(pm + rng.normal(scale=0.01, size=3))   # not necessarily admissible; filtered below
admissible = []
for bv in samples:
    Gn = np.array(Gfun(*bv), dtype=float)
    ev = np.linalg.eigvalsh(Gn)
    if ev[0] > -1e-9 and abs(np.linalg.det(Gn)) < 1e-9:
        admissible.append(bv)
info("scan: %d admissible samples (G PSD, det G ~ 0) from the quartic-in-b1^2 parametrisation + perturbations" % len(admissible))
min_pi = []
min_zero_ratio = []
dist = []
for bv in admissible:
    Gn = np.array(Gfun(*bv), dtype=float)
    fvals = p0n @ Gn @ PHI
    min_pi.append((1 + fvals).min())
    sc_ = bv[0] + 2 * bv[1] + bv[2]
    ratio = (1 - fvals)[1:] / w2[1:]
    min_zero_ratio.append(ratio.min() / max(sc_**2, 1e-12))
    dist.append(np.min(np.linalg.norm(Pnum - bv, axis=1)) if len(Pnum) else 9.9)
min_pi = np.array(min_pi)
dist = np.array(dist)
min_zero_ratio = np.array(min_zero_ratio)
near = min_pi < 0.02
info("scan: %d samples have min_k (1+f) < 0.02; their max distance to P = %.4f" % (near.sum(), dist[near].max() if near.any() else 0.0))
check("6.1 (numerical) every scanned admissible b with a grid point of 1+f < 0.02 lies within 0.06 of a member of P",
      (not near.any()) or dist[near].max() < 0.06)
far = dist > 0.1
check("6.2 (numerical) away from P (distance > 0.1; %d samples) min_k (1+f) stays >= 0.02 (smallest %.4f): no pi touching" %
      (far.sum(), min_pi[far].min() if far.any() else 1.0), far.any() and min_pi[far].min() >= 0.02)
check("6.3 (numerical) 1 - f > 0 off k=0 for all scanned b with s != 0 (smallest (1-f)/(s^2 sum sin^2(k/2)) = %.3f)" % min_zero_ratio.min(),
      min_zero_ratio.min() > 0.05)
# direct: at members of P the grid minimum of 1+f is at the predicted TRIM class
ok_loc = True
for lab, bv in members_sorted:
    Gn = np.array(Gfun(*[float(z) for z in bv]), dtype=float)
    fv = p0n @ Gn @ PHI
    idx = np.where(1 + fv < 1e-8)[0]
    ks_hit = {tuple(np.round(K[:, i] / np.pi).astype(int)) for i in idx}
    want = {'X': {(1, 0, 0), (0, 1, 0), (0, 0, 1)}, 'M': {(1, 1, 0), (1, 0, 1), (0, 1, 1)}, 'R': {(1, 1, 1)}}[lab]
    ok_loc &= ks_hit == want
check("6.4 (numerical, k-grid) at every member of P the set {f = -1} on the grid is exactly the predicted TRIM orbit "
      "(X: three axis points, M: three face points, R: the corner)", ok_loc)
# the thirteen: also confirm T_0 = {0} on grid for P members
okz = True
for lab, bv in members_sorted:
    Gn = np.array(Gfun(*[float(z) for z in bv]), dtype=float)
    fv = p0n @ Gn @ PHI
    okz &= (np.where(1 - fv < 1e-8)[0].tolist() == [0])
check("6.5 (numerical, k-grid) at every member of P the set {f = +1} on the grid is {k = 0} only", okz)

# ----------------------------------------------------------------------------
# Verdict lines
# ----------------------------------------------------------------------------
elapsed = time.time() - T_START
info("runtime %.1f s" % elapsed)
if FAILED == 0:
    print("HIT: for the massless-normalised family (G(b) PSD rank<=3, b != 0) the zero-touching set is exactly {k=0}; the pi-touching set is empty "
          "except for 8 explicit members: +-b_gold (3 axis cones), +-b_M (3 face cones, s ~ 0.966) and 4 members b_R = (3b2, b1, b2) with b2^2 = 7/396, "
          "b1^2 = 5/132 (1 corner cone) -- the face and corner pi members are new; the source's b* and b_iso are globally gapped except k=0")
print("TOTAL: PASS=%d FAIL=%d" % (PASSED, FAILED))
print("SUMMARY: exact Groebner stratification of the zero set of g plus PSD exclusions classifies all zero/pi quasienergy touchings of the massless Clifford walk family and finds 6 new admissible members with face/corner pi Dirac cones.")
sys.exit(0 if FAILED == 0 else 1)
