#!/usr/bin/env python3
"""Independent referee of the walker's sea in the member, attempt a2.

Worker w-macbookpro90c72-jbf3c. Does not import the attempt. Exact sympy
only: the uniform second-order energy, the sqrt(det g) mismatch, the
adiabatic kinetic form, and the two-level matrix element.
"""
import sys

import sympy as sp

FAILS = []


def ok(tag, cond, msg=""):
    if not cond:
        FAILS.append(tag)
    print(f"{tag} {'ok' if cond else 'FAIL'} {msg}".rstrip())


I, A, B, J, Ap, Bp = sp.symbols("I A B J Ap Bp", real=True)
h11, h22, h33, h12, h13, h23 = sp.symbols("h11 h22 h33 h12 h13 h23")
h = sp.Matrix([[h11, h12, h13], [h12, h22, h23], [h13, h23, h33]])
s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
s = sp.Matrix([s1, s2, s3])
r2 = s1**2 + s2**2 + s3**2

# ---------------------------------------------------------------- expansion of |(1 - h/2) s|
eps = sp.symbols("eps")
M = sp.eye(3) - eps * h / 2
quad = sp.expand((M * s).dot(M * s))
series = sp.series(sp.sqrt(quad), eps, 0, 3).removeO()
# compare with r - eps (s.h.s)/(2r) + eps^2 (s.h^2.s)/(8r) - eps^2 (s.h.s)^2/(8 r^3)
r = sp.sqrt(r2)
shs = sp.expand((s.T * h * s)[0])
sh2s = sp.expand((s.T * h * h * s)[0])
manual = r - eps * shs / (2 * r) + eps**2 * sh2s / (8 * r) - eps**2 * shs**2 / (8 * r**3)
diff = sp.simplify(sp.together(series - manual) * r**3)
ok("E1", diff == 0, "|(1-h/2)s| = r - (s.h.s)/(2r) + (s.h^2.s)/(8r) - (s.h.s)^2/(8 r^3) + O(h^3)")

# pointwise moment identities
ok(
    "E2",
    sp.simplify(r2**2 / r**3 - r) == 0 and sp.simplify(r2**2 / r**5 - 1 / r) == 0,
    "sum_ij s_i^2 s_j^2/r^3 = r and /r^5 = 1/r, so 3B+6A = I and 3B'+6A' = J",
)

# cubic contraction of the second-order piece
# <s_i s_j / r> = delta_ij I/3
# <s_a s_b s_c s_d / r^3> = A (three pairings) + (B-3A) if all four indices equal
tr = h.trace()
tr2 = (h * h).trace()
sq = h11**2 + h22**2 + h33**2
# (s.h.s)^2 average / r^3 from the isotropic tensor, contracted
# A (tr)^2 + 2 A tr(h^2) + (B-3A) sum h_ii^2
fourth = A * tr**2 + 2 * A * tr2 + (B - 3 * A) * sq
second = -((I / 3) * tr2) / 8 + fourth / 8
second = sp.expand(second.subs(I, 3 * B + 6 * A))
claim2 = sp.expand(-B / 8 * tr2 + A / 8 * tr**2 + (B - 3 * A) / 8 * sq)
ok("E3", sp.expand(second - claim2) == 0, "second order is -(B/8)tr h^2 + (A/8)(tr h)^2 + ((B-3A)/8) sum h_ii^2")

# first order
ok("E4", sp.simplify((I / 3) * tr / 2 - I / 6 * tr) == 0, "first order is (I/6) tr h")

# dilation: h = lam * 1, |v| = |1 - lam/2| r. For 1-lam/2 > 0 set u = 1-lam/2.
u = sp.symbols("u", positive=True)
det_g = u ** (-6)                        # det(g^{ij}) = u^6, det g = u^{-6}
root = sp.simplify(det_g ** (sp.Rational(-1, 6)) - u)
sqrt_det = sp.simplify(sp.sqrt(det_g) - u ** (-3))
ok(
    "E5",
    root == 0 and sqrt_det == 0,
    "for h = lam*1 and 1-lam/2 > 0, (det g)^(-1/6) = 1-lam/2 and sqrt(det g) = (1-lam/2)^(-3)",
)

# no multiple of sqrt(det g) through order lam^2
lam = sp.symbols("lam")
C, c0 = sp.symbols("C c0")
sea = -I * (1 - lam / 2)
trial = c0 + C * (1 - lam / 2) ** (-3)
ser = sp.series(trial - sea, lam, 0, 3).removeO()
sol = sp.solve([ser.coeff(lam, 0), ser.coeff(lam, 1)], [c0, C], dict=True)[0]
order2 = sp.simplify(ser.coeff(lam, 2).subs(sol))
ok(
    "E6",
    sol[C] == I / 3 and sol[c0] == -sp.Rational(4, 3) * I and order2 == I / 2,
    "matching orders 0 and 1 forces C = I/3, c0 = -4I/3, and order 2 fails by I/2",
)

# traceless form and no trace cross term
mu = sp.symbols("mu")
# set h33 = -h11-h22 so tr h = 0, off-diagonals free
E2 = claim2
E2_tl = sp.expand(E2.subs(h33, -h11 - h22))
target = sp.expand(
    -(3 * A / 8) * (h11**2 + h22**2 + (h11 + h22) ** 2)
    - (B / 4) * (h12**2 + h13**2 + h23**2)
)
# pure dilation second order vanishes
dil2 = sp.expand(claim2.subs({h11: lam, h22: lam, h33: lam, h12: 0, h13: 0, h23: 0}))
# cross: quadratic form of traceless plus mu*1 minus traceless piece is independent of traceless entries
hm = sp.Matrix([[h11 + mu, h12, h13], [h12, h22 + mu, h23], [h13, h23, -h11 - h22 + mu]])
mix = sp.expand(
    -B / 8 * (hm * hm).trace()
    + A / 8 * hm.trace() ** 2
    + (B - 3 * A) / 8 * sum(hm[i, i] ** 2 for i in range(3))
)
cross = sp.expand(mix - E2_tl)
cross2 = sp.expand(cross)
ok(
    "E7",
    sp.expand(E2_tl - target) == 0 and dil2 == 0 and cross2.free_symbols <= {A, B, mu},
    "traceless second order is -(3A/8) sum h_ii^2 - (B/4) sum_{i<j} h_ij^2; a dilation has no second order; no trace cross term",
)

# positivity witnesses: integrands nonnegative and positive at one momentum
def at(k1, k2, k3):
    ss = (sp.sin(k1), sp.sin(k2), sp.sin(k3))
    rr = sp.sqrt(sum(x**2 for x in ss))
    return ss, rr

ss, rr = at(sp.pi / 2, sp.pi / 2, 0)
A_pt = sp.simplify(ss[0] ** 2 * ss[1] ** 2 / rr**3)
Ap_pt = sp.simplify(ss[0] ** 2 * ss[1] ** 2 / rr**5)
ssb, rrb = at(sp.pi / 2, 0, 0)
B_pt = sp.simplify(ssb[0] ** 4 / rrb**3)
Bdiff = sp.simplify((ssb[0] ** 2 - ssb[1] ** 2) ** 2 / rrb**5)
ok(
    "E8",
    A_pt > 0 and B_pt > 0 and Ap_pt > 0 and Bdiff > 0,
    f"A={A_pt}, A'={Ap_pt} at (pi/2,pi/2,0); B={B_pt} and (s1^2-s2^2)^2/r^5={Bdiff} at (pi/2,0,0)",
)

# B' - A' algebra
ident_ba = sp.expand((s1**4 + s2**4) / 2 - s1**2 * s2**2 - (s1**2 - s2**2) ** 2 / 2)
ok("K1", ident_ba == 0, "B' - A' = (1/2)<(s1^2 - s2^2)^2 / r^5>")

# kinetic average
# T = < [s.hd^2.s - (s.hd.s)^2/r^2] / (32 r^3) >
# = (1/32) [ (J/3) tr(hd^2) - (Ap (tr)^2 + 2 Ap tr(hd^2) + (Bp-3Ap) sum hd_ii^2) ]
num_tr2 = sp.together((J / 3) - 2 * Ap)
num_tr2 = sp.simplify(num_tr2.subs(J, 3 * Bp + 6 * Ap))
claimT_coeff_tr2 = Bp
ok("K2", sp.simplify(num_tr2 - claimT_coeff_tr2) == 0, "kinetic coefficient of tr hd^2 is B', so T = (1/32)[B' tr hd^2 - A'(tr hd)^2 - (B'-3A') sum hd_ii^2]")

# cubic M1, M2, M3
claimT = (Bp * tr2 - Ap * tr**2 - (Bp - 3 * Ap) * sq) / 32
cub = sp.expand(claimT)
M1 = cub.coeff(h11, 2)
M2 = sp.expand(cub).coeff(h11).coeff(h22)
M3 = cub.coeff(h12, 2)
ok(
    "K3",
    sp.simplify(M1 - Ap / 16) == 0
    and sp.simplify(M2 + Ap / 16) == 0
    and sp.simplify(M3 - Bp / 16) == 0,
    "M1 = A'/16, M2 = -A'/16, M3 = B'/16",
)
dilT = sp.expand(claimT.subs({h11: 1, h22: 1, h33: 1, h12: 0, h13: 0, h23: 0}))
ok("K4", dilT == 0, "a dilation has zero second-order inertia")

# two-level matrix element, symbolic unit vectors via projectors
# use the Pauli trace identity directly and check on a general w and two explicit ON frames
sig = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]


def sdot(v):
    return sum((v[i] * sig[i] for i in range(3)), sp.zeros(2))


def me(n, n2, w):
    Pp = (sp.eye(2) + sdot(n2)) / 2
    Pm = (sp.eye(2) - sdot(n)) / 2
    return sp.simplify((Pp * sdot(w) * Pm * sdot(w)).trace())


n = (sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3))
n2 = (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7))
w = (sp.Integer(1), sp.Integer(-1), sp.Integer(2))
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
pred = (dot(w, w) * (1 + dot(n, n2)) - 2 * dot(n, w) * dot(n2, w)) / 2
same = dot(w, w) - dot(n, w) ** 2
ok(
    "K5",
    sp.simplify(me(n, n2, w) - pred) == 0
    and sp.simplify(me(n, n, w) - same) == 0
    and dot(n, n) == 1
    and dot(n2, n2) == 1,
    "trace formula |<+,n'|sigma.w|-,n>|^2 matches [|w|^2(1+n.n') - 2(n.w)(n'.w)]/2 at unit vectors",
)

# adiabatic prefactor: |w|^2 - (n.w)^2 with w = -hd s/2, Delta = 2r, excess / Delta^3
# gives [s.hd^2.s - (s.hd.s)^2/r^2] / (32 r^3)
hd = h  # placeholder symmetric
ww = [-hd.row(i).dot(s) / 2 for i in range(3)]
# |w|^2 - (n.w)^2 = |hd s|^2/4 - (s.hd.s)^2/(4 r^2)
gap = 2 * r
excess = (sh2s / 4 - shs**2 / (4 * r2)) / gap**3
excess_s = sp.simplify(excess * r**3 * 32 / (sh2s - shs**2 / r2))
ok("K6", excess_s == 1, "two-level excess |<+|Hdot|->|^2/Delta^3 equals [s.hd^2.s - (s.hd.s)^2/r^2]/(32 r^3)")

print(f"checks: {'all passed' if not FAILS else 'FAILED ' + ' '.join(FAILS)}")
if FAILS:
    print("SUMMARY: fails at step " + FAILS[0] + " - an independent exact check of that family failed")
    sys.exit(1)
print(
    "SUMMARY: confirmed exact partial - uniform sea energy -I + (I/6)tr h - (B/8)tr h^2 + (A/8)(tr h)^2 "
    "+ ((B-3A)/8) sum h_ii^2, dilation -I (det g)^(-1/6), no multiple of sqrt(det g); kinetic "
    "M1=-M2=A'/16, M3=B'/16, zero on a dilation, so not beta=-alpha. Float q^2 and alpha/K were not confirmed."
)
print(
    "HIT: confirmed - the exact claim survives. Independently, the second-order sea energy is the stated "
    "cubic form with 3B+6A=I, a dilation is exactly -I(det g)^(-1/6) so no multiple of sqrt(det g) matches "
    "through order two (the mismatch is I/2), and shear is negative definite because A and B are averages of "
    "nonnegative integrands that are positive on an open set. The adiabatic kinetic term is M1=-M2=A'/16, "
    "M3=B'/16, vanishes on a dilation, and cannot have beta=-alpha because A'>0 and B'>A'. "
    "The floating-point q^2 kernel and alpha/K>1/4 were not re-established."
)
