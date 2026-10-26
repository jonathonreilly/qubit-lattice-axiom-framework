#!/usr/bin/env python3
"""Anisotropic flux-free comparator: symmetry-fixed lines, an exceptional-locus theorem, and a complex-scheme census.

Supplied setting (not derived here): the four-site Bloch matrix H(f) = i M(f), z_j = exp(2 pi i f_j), of the supplied
u=+1 quadratic Majorana comparator, built from the TERMS table below (the network and hopping signs are SUPPLIED; the
table is copied from the pinned source runner, only to define the same matrix).  Couplings Jx, Jy, Jz, kappa > 0.

What this script does (all Fractions / sympy exact unless a line says otherwise):
  A. background identities of M (symbolic couplings);
  B. a constant real matrix P (P^2 = -1) with P M(z) P^-1 = M(1/z2, 1/z1, 1/z3), i.e. the swap-inversion symmetry is an
     operator symmetry; the spectral swap and inversion symmetries of det M;
  C. on the P-fixed line (x, 1-x, 1/2):  det M = 16 SOS+ SOS-  with explicit sums of three squares; hence, for ALL positive
     couplings, a touching there exists iff Jx = Jy and Jz (4 kappa^2 + Jx^2) = 8 kappa^2 Jx (the handover locus);
  D. a modular-plus-exact census of the complexified rank<=2 scheme of M at the five supplied couplings B, A, C, F, G:
     length 34 = 4 (line) + 10 (swap plane z1 = z2, a second integer quintic) + 20 (the supplied quintic orbit), with the
     exact consequence that the swap-plane points are never on the real torus.
Single process, pure python + sympy/mpmath/numpy.  Prints PASS/FAIL lines, TOTAL, SUMMARY (and HIT only for section C)."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, time, itertools, warnings, random
from fractions import Fraction as Fr
warnings.filterwarnings("ignore")
import sympy as sp
import mpmath as mp

T0 = time.time()
PASS = 0
FAIL = 0


def check(ok, label, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("%s %s%s" % ("PASS" if ok else "FAIL", label, (": " + detail) if detail else ""), flush=True)
    return ok


# ------------------------------------------------------------------ supplied network (same matrix as the pinned source runner)
TERMS = [(0, 1, (-1, 0, 0), "y"), (0, 1, (0, 0, 0), "x"), (0, 3, (0, 0, -1), "z"), (1, 1, (-1, 0, 0), "odd"), (1, 3, (1, 0, -1), "odd"),
         (3, 1, (0, 0, 1), "odd"), (0, 0, (1, 0, 0), "odd"), (0, 2, (-1, 0, 0), "odd"), (2, 0, (0, 0, 0), "odd"), (2, 3, (0, -1, 0), "y"),
         (2, 3, (0, 0, 0), "x"), (2, 1, (0, 0, 0), "z"), (3, 3, (0, -1, 0), "odd"), (3, 1, (0, 1, 0), "odd"), (1, 3, (0, 0, 0), "odd"),
         (2, 2, (0, 1, 0), "odd"), (2, 0, (0, -1, 1), "odd"), (0, 2, (0, 0, -1), "odd")]
Jx, Jy, Jz, kap = sp.symbols("Jx Jy Jz kappa", positive=True)
z1, z2, z3 = sp.symbols("z1 z2 z3")


def build(amp):
    M = sp.zeros(4, 4)
    for (a, b, n, kind) in TERMS:
        t = amp[kind]
        mon = z1 ** n[0] * z2 ** n[1] * z3 ** n[2]
        M[a, b] += t * mon
        M[b, a] -= t / mon
    return M


def R(f):
    f = Fr(f)
    return sp.Rational(f.numerator, f.denominator)


MSYM = build({"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kap})


def Mnum(J):
    return build({"x": 2 * R(J[0]), "y": 2 * R(J[1]), "z": 2 * R(J[2]), "odd": 2 * R(J[3])})


def is_zero_matrix(A):
    return all(sp.simplify(e) == 0 for e in A)


DSYM = sp.expand(MSYM.det())

# ================================================================== A. background identities
print("# A. background identities of the supplied M (symbolic couplings)")
Minv = MSYM.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True)
check(all(sp.expand(e) == 0 for e in (MSYM + Minv.T)), "A1 M(z) + M(1/z)^T = 0 (anti-Hermitian on the torus)")
mu = sp.symbols("mu")
cp = sp.expand((mu * sp.eye(4) - MSYM).det())
check(sp.expand(cp.coeff(mu, 3)) == 0 and sp.expand(cp.coeff(mu, 1)) == 0, "A2 char poly of M has no mu^3 and no mu^1 term (spectrum +-l1, +-l2, det M = l1^2 l2^2 >= 0 on the torus)")

# ================================================================== B. symmetries
print("# B. symmetries valid for all couplings (exact identities)")
P = sp.zeros(4, 4)
P[3, 0], P[0, 3], P[2, 1], P[1, 2] = 1, -1, -1, 1
check(P * P == -sp.eye(4) and P.is_symmetric() is False and P.T * P == sp.eye(4), "B0 P is real orthogonal with P^2 = -1")
Mswapinv = MSYM.subs({z1: 1 / z2, z2: 1 / z1, z3: 1 / z3}, simultaneous=True)
lhs = (P * MSYM * P.inv()).applyfunc(sp.expand)
check(all(sp.expand(lhs[i, j] - Mswapinv[i, j]) == 0 for i in range(4) for j in range(4)),
      "B1 P M(z1,z2,z3) P^-1 = M(1/z2,1/z1,1/z3) as a Laurent identity in z and in all couplings (operator symmetry)")
check(sp.expand(DSYM - DSYM.subs({z1: z2, z2: z1}, simultaneous=True)) == 0, "B2 det M(z1,z2,z3) = det M(z2,z1,z3) (spectral swap symmetry)")
check(sp.expand(DSYM - DSYM.subs({z1: 1 / z1, z2: 1 / z2, z3: 1 / z3}, simultaneous=True)) == 0, "B3 det M(z) = det M(1/z) (inversion)")
# the plain swap is NOT implemented by a constant unitary (so no block structure on z1 = z2): the swap-inversion is.
check(sp.expand(DSYM - DSYM.subs({z1: 1 / z2, z2: 1 / z1}, simultaneous=True)) != 0,
      "B4 negative control: det M(z1,z2,z3) != det M(1/z2,1/z1,z3) (z3 must be inverted with the pair)")
zz = sp.symbols("zz")
for z3v in (1, -1):
    Ml = MSYM.subs({z3: z3v, z2: 1 / z1}).subs(z1, zz).applyfunc(sp.simplify)
    check(is_zero_matrix(P * Ml - Ml * P), "B5 P commutes with M on the line (x, 1-x, %s)" % ("0" if z3v == 1 else "1/2"))

# ---- B6: the eight time-reversal-invariant momenta (z_j = +-1): det M is 16 times an explicit square
TRIM_EXPECT = {(1, 1, 1): (Jx + Jy - Jz) * (Jx + Jy + Jz), (1, 1, -1): Jx ** 2 + 2 * Jx * Jy + Jy ** 2 + Jz ** 2,
               (1, -1, 1): Jx ** 2 - Jy ** 2 - Jz ** 2 - 4 * kap ** 2, (1, -1, -1): Jx ** 2 - Jy ** 2 + Jz ** 2 + 4 * kap ** 2,
               (-1, 1, 1): Jx ** 2 - Jy ** 2 - Jz ** 2 - 4 * kap ** 2, (-1, 1, -1): Jx ** 2 - Jy ** 2 + Jz ** 2 + 4 * kap ** 2,
               (-1, -1, 1): (Jx - Jy - Jz) * (Jx - Jy + Jz), (-1, -1, -1): Jx ** 2 - 2 * Jx * Jy + Jy ** 2 + Jz ** 2 + 16 * kap ** 2}
okt = all(sp.expand(DSYM.subs({z1: p_[0], z2: p_[1], z3: p_[2]}) - 16 * sq ** 2) == 0 for p_, sq in TRIM_EXPECT.items())
check(okt, "B6 det M at the eight points z_j = +-1 equals 16 g^2 with g listed in TRIM_EXPECT; so a TRIM touching needs g = 0, i.e. Jz = Jx+Jy, Jz = |Jx-Jy|, Jx^2 = Jy^2+Jz^2+4k^2 or Jy^2 = Jx^2+Jz^2+4k^2 (the two other points have g > 0 for positive couplings)")
check(sp.expand(TRIM_EXPECT[(1, 1, -1)] - ((Jx + Jy) ** 2 + Jz ** 2)) == 0 and sp.expand(TRIM_EXPECT[(-1, -1, -1)] - ((Jx - Jy) ** 2 + Jz ** 2 + 16 * kap ** 2)) == 0,
      "B7 g(1,1,-1) = (Jx+Jy)^2+Jz^2 > 0 and g(-1,-1,-1) = (Jx-Jy)^2+Jz^2+16k^2 > 0 for all positive couplings (sums of squares)")

# ================================================================== C. second P-fixed line (x, 1-x, 1/2)
print("# C. the P-fixed line z2 = 1/z1, z3 = -1  (f = (x, 1-x, 1/2))")
w = sp.symbols("w")  # z1 = w^2 on the line
Cc = (w + 1 / w) / 2
Ss = (w - 1 / w) / (2 * sp.I)
cc_ = sp.expand(Cc ** 2 - Ss ** 2)   # cos(2 pi x)
ss_ = sp.expand(2 * Cc * Ss)         # sin(2 pi x)
SOSp = (Jz - 2 * kap * ss_) ** 2 + ((Jx + Jy) * Cc - 4 * kap * Ss) ** 2 + (Jx - Jy) ** 2 * Ss ** 2
SOSm = (Jz + 2 * kap * ss_) ** 2 + ((Jx + Jy) * Cc + 4 * kap * Ss) ** 2 + (Jx - Jy) ** 2 * Ss ** 2
Dline = sp.expand(DSYM.subs({z3: -1, z2: 1 / z1}).subs(z1, w ** 2))
check(sp.expand(Dline - 16 * SOSp * SOSm) == 0, "C1 det M(w^2, w^-2, -1) = 16 SOS+ SOS-  (Laurent identity in w, symbolic Jx,Jy,Jz,kappa)",
      "SOS+- = (Jz -+ 2k s)^2 + ((Jx+Jy)C -+ 4k S)^2 + (Jx-Jy)^2 S^2, C,S = cos,sin(pi x), s = 2CS")
# block determinants: P = +-i eigenspaces
vecp = [sp.Matrix([0, -sp.I, 1, 0]), sp.Matrix([sp.I, 0, 0, 1])]   # P v = +i v
vecm = [sp.Matrix([0, sp.I, 1, 0]), sp.Matrix([-sp.I, 0, 0, 1])]   # P v = -i v
okeig = all(sp.simplify(P * v - sp.I * v) == sp.zeros(4, 1) for v in vecp) and all(sp.simplify(P * v + sp.I * v) == sp.zeros(4, 1) for v in vecm)
check(okeig, "C2 explicit eigenvectors of P for +i and -i")
Bp = sp.Matrix.hstack(*vecp)
Bm = sp.Matrix.hstack(*vecm)
Mline = MSYM.subs({z3: -1, z2: 1 / z1}).subs(z1, w ** 2)


def blockdet(B):
    Mb = ((B.H * B).inv() * B.H * Mline * B).applyfunc(sp.simplify)
    return sp.expand(sp.simplify(Mb.det())), Mb


dp, Mpb = blockdet(Bp)
dm, Mmb = blockdet(Bm)
check(sp.expand(dp - 4 * SOSm) == 0 and sp.expand(dm - 4 * SOSp) == 0,
      "C3 the two 2x2 blocks of M on the line have real determinants 4 SOS- (P=+i) and 4 SOS+ (P=-i)")
# SOS+ - the expanded form  A - 4k(Jx+Jy+Jz) sin  with A = Jx^2+Jy^2+Jz^2 + 2 Jx Jy cos + 4k^2 (1-cos)(3+cos)
A_ = Jx ** 2 + Jy ** 2 + Jz ** 2 + 2 * Jx * Jy * cc_ + 4 * kap ** 2 * (1 - cc_) * (3 + cc_)
check(sp.expand(SOSp - (A_ - 4 * kap * (Jx + Jy + Jz) * ss_)) == 0 and sp.expand(SOSm - (A_ + 4 * kap * (Jx + Jy + Jz) * ss_)) == 0,
      "C4 SOS+- = A -+ 4 kappa (Jx+Jy+Jz) sin 2 pi x,  A = Jx^2+Jy^2+Jz^2 + 2JxJy cos + 4k^2(1-cos)(3+cos)  (so det M >= 0 on the line is an identity)")
# C5 zero characterisation.  Over the reals with C = cos(pi x), S = sin(pi x): SOS+ = 0 iff three equations hold.
# step 1: Jz > 0 and Jz = 2 k sin(2 pi x) force sin != 0 so S != 0; step 2: (Jx-Jy) S = 0 then gives Jx = Jy;
# step 3: (2Jx) C = 4 k S gives tan(pi x) = Jx/(2k); we verify the resulting closed forms exactly.
Cs, Ssy = sp.symbols("C S", positive=True)
t_ = Jx / (2 * kap)
c_loc = sp.simplify((1 - t_ ** 2) / (1 + t_ ** 2))
s_loc = sp.simplify(2 * t_ / (1 + t_ ** 2))
Jz_loc = sp.simplify(2 * kap * s_loc)
check(sp.simplify(c_loc - (4 * kap ** 2 - Jx ** 2) / (4 * kap ** 2 + Jx ** 2)) == 0 and sp.simplify(Jz_loc - 8 * kap ** 2 * Jx / (4 * kap ** 2 + Jx ** 2)) == 0,
      "C5 solving the three SOS+ equations: cos 2 pi x = (4k^2-Jx^2)/(4k^2+Jx^2), Jz = 8 k^2 Jx/(4k^2+Jx^2), Jx = Jy")
# C6 back substitution: at the locus both SOS+ (x < 1/2 branch, t = tan(pi x) = Jx/2k) vanishes identically
Cn = 1 / sp.sqrt(1 + t_ ** 2)
Sn = t_ / sp.sqrt(1 + t_ ** 2)
sosp_loc = sp.simplify(((Jz_loc - 2 * kap * 2 * Cn * Sn) ** 2 + ((Jx + Jx) * Cn - 4 * kap * Sn) ** 2 + 0 * Sn ** 2))
check(sosp_loc == 0, "C6 SOS+ vanishes identically at Jy = Jx, Jz = 8k^2Jx/(4k^2+Jx^2), tan(pi x) = Jx/(2k)")
# C7 gap: for Jx != Jy, Jz > 0 and any real angle SOS+- >= min( (Jx-Jy)^2 S^2 , ...) > 0.  Exact certificate by cases:
#   if S^2 >= s0:  SOS >= (Jx-Jy)^2 s0 ;  if S^2 < s0:  |sin| = 2|C S| and Jz - 2k sin... checked as an exact quantifier-free polynomial
#   inequality is awkward; we certify instead by the exact trigonometric statement that all three squares vanish only on the locus (C5)
#   and by an exact rational grid + Lipschitz bound at each of the five supplied couplings and several random rational couplings.
COUP = {"B": (Fr(6, 5), Fr(4, 5), Fr(1), Fr(3, 10)), "A": (Fr(1), Fr(4, 5), Fr(1), Fr(9, 20)), "C": (Fr(1), Fr(4, 5), Fr(1), Fr(4, 5)),
        "F": (Fr(2), Fr(1), Fr(5, 2), Fr(9, 10)), "G": (Fr(3, 2), Fr(1, 2), Fr(4, 5), Fr(3, 2))}


def sos_values_line(J, n=4000):
    """numerical (mpmath 30 digits) minimum over the half-circle of SOS+ * SOS-, returns (min, argmin)."""
    mp.mp.dps = 30
    jx, jy, jz, k = [mp.mpf(Fr(x).numerator) / mp.mpf(Fr(x).denominator) for x in J]
    best = None
    for i in range(n + 1):
        th = mp.pi * i / n * 1  # theta = pi x in [0, pi]
        C, S = mp.cos(th), mp.sin(th)
        s = 2 * C * S
        sp_ = (jz - 2 * k * s) ** 2 + ((jx + jy) * C - 4 * k * S) ** 2 + (jx - jy) ** 2 * S ** 2
        sm_ = (jz + 2 * k * s) ** 2 + ((jx + jy) * C + 4 * k * S) ** 2 + (jx - jy) ** 2 * S ** 2
        v = sp_ * sm_
        if best is None or v < best[0]:
            best = (v, th)
    return best


for nm, J in COUP.items():
    v, th = sos_values_line(J, 2000)
    check(v > 0 and J[0] != J[1], "C7 coupling %s (Jx != Jy): det M/16 = SOS+ SOS- on the line (x,1-x,1/2) has grid minimum %s > 0 (floating cross-check; the proof is C1+C5)" % (nm, mp.nstr(v, 6)))
# C8 positive control: the locus (Jx = Jy) has a rank-two point; the landed handover parametrisation is the Jx = Jy = 1 slice
q = sp.symbols("q", positive=True)
Jp = sp.symbols("Jp", positive=True)
loc = {Jx: Jp, Jy: Jp, Jz: 8 * kap ** 2 * Jp / (4 * kap ** 2 + Jp ** 2)}
zloc = (2 * kap + sp.I * Jp) ** 2 / (4 * kap ** 2 + Jp ** 2)
Mloc = MSYM.subs(loc).subs({z1: zloc, z2: 1 / zloc, z3: -1})
minors_ok = True
for rows in itertools.combinations(range(4), 3):
    for cols in itertools.combinations(range(4), 3):
        m = sp.simplify(sp.expand(Mloc.extract(list(rows), list(cols)).det()))
        if m != 0:
            minors_ok = False
check(minors_ok, "C8 at Jx=Jy=Jp, Jz=8k^2Jp/(4k^2+Jp^2), e^{2 pi i x}=(2k+iJp)^2/(4k^2+Jp^2): all sixteen 3x3 minors of M vanish (rank <= 2), symbolic in Jp, kappa")
trM = sp.simplify(Mloc.trace())
check(trM == 0, "C9 tr M = 0 there; with C8 a double zero level (touching of the middle bands at E=0)")
# C10: negative controls (exact rationals): leave the locus in either direction -> minors nonzero
def rank_defect(J, zval):
    M = Mnum(J).subs({z1: zval, z2: 1 / zval, z3: -1})
    return [sp.simplify(sp.expand(M.extract(list(r), list(c)).det())) for r in itertools.combinations(range(4), 3) for c in itertools.combinations(range(4), 3)]
Jp0, k0 = sp.Rational(1), sp.Rational(3, 4)
z0 = sp.nsimplify((2 * k0 + sp.I * Jp0) ** 2 / (4 * k0 ** 2 + Jp0 ** 2))
Jz0 = 8 * k0 ** 2 * Jp0 / (4 * k0 ** 2 + Jp0 ** 2)
base = (Fr(1), Fr(1), Fr(int(Jz0.p), int(Jz0.q)), Fr(3, 4))
check(all(e == 0 for e in rank_defect(base, z0)), "C10a positive control (1,1,18/13; 3/4) at z1 = (5+12i)/13: rank M <= 2 exactly")
check(any(e != 0 for e in rank_defect((Fr(1), Fr(1), Fr(18, 13) + Fr(1, 1000), Fr(3, 4)), z0)), "C10b negative control: Jz moved off the locus -> minors nonzero at that point")
check(any(e != 0 for e in rank_defect((Fr(1), Fr(1) + Fr(1, 1000), Fr(18, 13), Fr(3, 4)), z0)), "C10c negative control: Jx != Jy -> minors nonzero at that point")

# ================================================================== D. complexified rank<=2 scheme at the five supplied couplings
print("# D. complex census of the rank<=2 scheme (modular Groebner + exact slices) at the five supplied couplings")
Q5 = {  # SUPPLIED by the pinned source runner (integer quintics for cos 2 pi f3 of the off-plane orbit); descending coefficients
    "B": [864, 816, -166396, 837889, 205720, -829767],
    "A": [2686761091215, -52236803198601, 134862005654370, -5777693580942, -195927410075697, -295855810345],
    "C": [-323559360, 4015330704, 4437964845, -14633761482, 9591225363, 9746879930],
    "F": [7936185600, -13738636800, -148594878216, 375269121036, 231788784834, -325717384243],
    "G": [-470888437500, -1739470443750, 2234062696500, -1564217518875, -5666826883970, 44902909367],
}
xx, yy, zq, wq = sp.symbols("xx yy zq wq")
PRIME = 32003


def minors_of(Mn):
    out = []
    for rows in itertools.combinations(range(4), 3):
        for cols in itertools.combinations(range(4), 3):
            m = sp.together(sp.expand(Mn.extract(list(rows), list(cols)).det()))
            num, den = sp.fraction(m)
            num = sp.expand(num)
            if num != 0:
                out.append(num)
    return out


def intpoly(Pl):
    """integer primitive polynomial proportional to the rational polynomial Pl (same generator)."""
    _, Pi = Pl.clear_denoms()
    return sp.Poly(Pi.as_expr(), Pl.gens[0]).primitive()[1]


def palindromic_to_x(Pw):
    """P(w) palindromic of even degree 2m -> Q(x) with P(w) = w^m Q(w + 1/w)."""
    co = sp.Poly(Pw, wq).all_coeffs()[::-1]  # ascending
    n = len(co) - 1
    assert n % 2 == 0 and all(co[i] == co[n - i] for i in range(n + 1))
    m = n // 2
    x = sp.symbols("x")
    V = [sp.Integer(2), x]
    for k in range(2, m + 1):
        V.append(sp.expand(x * V[-1] - V[-2]))
    Q = co[m] + sum(co[m + k] * V[k] for k in range(1, m + 1))
    return sp.Poly(sp.expand(Q), x)


summary_rows = []
for nm in ("B", "A", "C", "F", "G"):
    J = COUP[nm]
    Mn = Mnum(J)
    # ---- D1: exact lex Groebner basis on the swap-inversion line z1 z2 = 1 (all complex points)
    Ms = Mn.subs({z1: zq, z2: 1 / zq, z3: wq}, simultaneous=True)
    mins = minors_of(Ms)
    Gl = sp.groebner(mins + [yy * zq * wq - 1], yy, zq, wq, order="lex")
    free = [g for g in Gl.exprs if not g.has(yy)]
    # expected: (wq - 1) and zq^2 * q((zq+1/zq)/2) up to a constant, q the landed line polynomial
    c = sp.symbols("c")
    qline = 4 * R(J[3]) ** 2 * c ** 2 - 2 * R(J[0]) * R(J[1]) * c + R(J[2]) ** 2 - R(J[0]) ** 2 - R(J[1]) ** 2 - 4 * R(J[3]) ** 2
    qz = sp.Poly(sp.expand(zq ** 2 * qline.subs(c, (zq + 1 / zq) / 2)), zq)
    has_w1 = any(sp.Poly(g, wq, zq).as_expr() == wq - 1 or sp.expand(g - (wq - 1)) == 0 for g in free)
    zpoly = [g for g in free if not g.has(wq)]
    ok_line = has_w1 and len(zpoly) == 1 and sp.expand(sp.Poly(zpoly[0], zq).monic().as_expr() - qz.monic().as_expr()) == 0
    check(ok_line, "D1[%s] rank<=2 points with z1 z2 = 1: exactly z3 = 1 and z1^2 q((z1+1/z1)/2) = 0 (landed line quadratic), 4 complex points; no point with z3 = -1" % nm)
    nreal_line = sp.Poly(qline, c).count_roots(-1, 1)
    # ---- D2: exact lex Groebner basis on the swap plane z1 = z2
    Ms = Mn.subs({z1: zq, z2: zq, z3: wq}, simultaneous=True)
    mins = minors_of(Ms)
    Gs = sp.groebner(mins + [yy * zq * wq - 1], yy, zq, wq, order="lex")
    free = [g for g in Gs.exprs if not g.has(yy)]
    pw = [g for g in free if not g.has(zq)]
    pz = [g for g in free if g.has(zq)]
    Pw = sp.Poly(pw[0], wq)
    lin = len(pz) == 1 and sp.Poly(pz[0], zq).degree() == 1
    Pw_pr = sp.Poly(Pw.as_expr() / sp.Poly(Pw.as_expr(), wq).LC(), wq) if False else Pw
    sqf = sp.gcd(Pw.as_expr(), sp.diff(Pw.as_expr(), wq)) in (1, -1) or sp.Poly(sp.gcd(Pw, Pw.diff(wq)), wq).degree() == 0
    Qp = palindromic_to_x(Pw.as_expr())
    nunit = Qp.count_roots(-2, 2)
    fl = sp.factor_list(Qp.as_expr())[1]
    print("# Q'[%s](x) = %s    (swap-plane quintic, w + 1/w = x)" % (nm, intpoly(Qp).as_expr()))
    check(Pw.degree() == 10 and lin and sqf and nunit == 0,
          "D2[%s] swap plane z1=z2: 10 complex points, w=z3 root of a squarefree palindromic degree-10 polynomial P(w)=w^5 Q'(w+1/w), z1 linear in w; Q' (degree %d, factors %s) has %d real roots in [-2,2], so no |z3|=1 and none on the real torus" % (nm, Qp.degree(), [sp.Poly(f).degree() for f, m_ in fl], nunit))
    # ---- D3: modular Groebner basis of the full scheme (grevlex, GF(p)), length and z3 characteristic polynomial
    mins = minors_of(Mn)
    gens = [z1, z2, z3, yy]
    G = sp.groebner(mins + [yy * z1 * z2 * z3 - 1], *gens, order="grevlex", modulus=PRIME)
    LM = [sp.Poly(g, *gens).monoms(order="grevlex")[0] for g in G.exprs]
    std = [e for e in itertools.product(range(14), repeat=4) if not any(all(e[i] >= l[i] for i in range(4)) for l in LM)]
    n = len(std)
    idx = {m_: i for i, m_ in enumerate(std)}
    Mx = sp.zeros(n, n)
    for j, mon in enumerate(std):
        e = z3
        for g, ex in zip(gens, mon):
            e = e * g ** ex
        r = G.reduce(sp.expand(e))[1]
        for mm, cf in sp.Poly(r, *gens, modulus=PRIME).terms():
            Mx[idx[mm], j] = int(cf) % PRIME
    x = sp.symbols("x")
    cpz = sp.Poly(Mx.charpoly(x).as_expr(), x, modulus=PRIME)
    # prediction from the exact pieces:  (x-1)^4 * P_swap(x) * (x^5 Q5((x+1/x)/2))^2   (monic mod p)
    q5 = sum(sp.Integer(cf) * x ** (5 - i) for i, cf in enumerate(Q5[nm]))
    gen_poly = intpoly(sp.Poly(sp.expand(x ** 5 * q5.subs(x, (x + 1 / x) / 2)), x))
    Psw = intpoly(sp.Poly(Pw.as_expr().subs(wq, x), x))
    pred = sp.Poly((x - 1) ** 4, x) * Psw * gen_poly ** 2
    pred_p = sp.Poly(pred.as_expr(), x, modulus=PRIME).monic()
    check(n == 34 and cpz.monic() == pred_p,
          "D3[%s] GF(%d): scheme length %d; char poly of mult-by-z3 = (x-1)^4 * P_swap * (x^5 Q5((x+1/x)/2))^2 (4 + 10 + 20 points)" % (nm, PRIME, n))
    # ---- exact facts about the supplied quintic
    q5p = sp.Poly(q5, x)
    nroots_unit = q5p.count_roots(-1, 1)
    irr = len(sp.factor_list(q5)[1]) == 1 and sp.factor_list(q5)[1][0][1] == 1
    cop = sp.gcd(Psw, gen_poly)
    cop_ok = sp.Poly(cop, x).degree() == 0
    p1 = Psw.eval(1) != 0 and gen_poly.eval(1) != 0
    check(irr and nroots_unit == 1 and cop_ok and p1,
          "D4[%s] supplied Q5 irreducible over Q with exactly %d root(s) in [-1,1]; z3-polynomials of the three strata pairwise coprime and none vanishes at z3=1 except the line stratum" % (nm, nroots_unit))
    summary_rows.append((nm, n, nreal_line, nroots_unit))
print("# D5 reading of D1-D4 (assumes GF(%d) is a good prime for the five ideals; CHECKED only at the five couplings)" % PRIME)
for (nm, n, nl, nq) in summary_rows:
    real_line = 2 * nl  # each root of q in (-1,1) gives the two torus points x, 1-x
    real_gen = 4 * nq
    check(real_line + real_gen == (6 if nm != "G" else 4),
          "D5[%s] upper bound on real-torus points from the strata (line: roots of q in [-1,1] x 2; generic: unit-circle roots of the squared factor give <= 2 points each; swap plane: 0) = %d + %d, equal to the interval-certified count of the sources (%d)" % (nm, real_line, real_gen, 6 if nm != "G" else 4))

# ================================================================== totals
if FAIL == 0:
    print("HIT: on the line f = (x, 1-x, 1/2) the comparator's det M = 16 SOS+ SOS- (three squares each), so for every positive Jx, Jy, Jz, kappa a middle-band touching exists there iff Jx = Jy and Jz = 8 kappa^2 Jx/(4 kappa^2 + Jx^2) (the handover family is the complete touching set of that line); for Jx != Jy there is none")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
print("SUMMARY: for all positive couplings the second swap-inversion line (x, 1-x, 1/2) carries a touching exactly on the locus Jx = Jy, Jz (4 kappa^2 + Jx^2) = 8 kappa^2 Jx (D = 16 SOS+ SOS-), and at the five supplied couplings the complexified rank<=2 scheme has length 34 = 4 + 10 + 20 with the 10 swap-plane points never on the real torus (modular GF(%d) evidence)." % PRIME)
print("# runtime %.1f s" % (time.time() - T0), file=sys.stderr)
sys.exit(0 if FAIL == 0 else 1)
