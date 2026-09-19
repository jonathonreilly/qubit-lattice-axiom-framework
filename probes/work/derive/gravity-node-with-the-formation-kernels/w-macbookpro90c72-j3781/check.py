#!/usr/bin/env python3
"""Exact checks for J:derive:gravity-node-with-the-formation-kernels:a2.

Route: take the node's OWN normalisation row on main (NEWTON_LAW_DERIVED_NOTE.md
-> LATTICE_GREENS_FUNCTION_MARADUDIN_..._2026-05-18.md) as the contract, and ask
what the formation kernels deliver into that slot.  Everything symbolic/exact;
the two transcendental roots are enclosed with rigorous interval arithmetic.
"""
import sympy as sp
from mpmath import iv

iv.dps = 60

P = F = 0


def chk(tag, ok, msg):
    global P, F
    if ok:
        P += 1
        print("PASS %-5s %s" % (tag, msg))
    else:
        F += 1
        print("FAIL %-5s %s" % (tag, msg))


k1, k2, k3, t = sp.symbols("k1 k2 k3 t", real=True)
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
K = (k1, k2, k3)
X = (x1, x2, x3)

# ---------------------------------------------------------------- N: the node
# N1  the two spellings of the node's symbol on main are one function
E = sum(2 - 2 * sp.cos(k) for k in K)                    # Maradudin row L28/L50
Delta = sum((2 * sp.sin(k / 2)) ** 2 for k in K)         # Regge spelling
chk("N1", sp.simplify(sp.expand_trig(E - Delta)) == 0,
    "E(k) = sum(2-2cos k_a) = sum (2 sin(k_a/2))^2")

# N2  small-k form: |k|^2 - (1/12) sum k^4 + O(k^6), quadratic part = identity
ser = sp.series(E.subs({k1: t * x1, k2: t * x2, k3: t * x3}), t, 0, 6).removeO()
q2 = sp.expand(ser.coeff(t, 2))
q4 = sp.expand(ser.coeff(t, 4))
chk("N2a", sp.simplify(q2 - (x1 ** 2 + x2 ** 2 + x3 ** 2)) == 0,
    "Hessian of E at k=0 is the identity: E = |k|^2 + O(k^4)")
chk("N2b", sp.simplify(q4 + sp.Rational(1, 12) * sum(x ** 4 for x in X)) == 0,
    "first anisotropy of E is the quartic -(1/12) sum k_a^4 (order r^-3 tail)")

# N3  single zero in the Brillouin zone, and the exact maximum
chk("N3", sp.solveset(2 - 2 * sp.cos(k1), k1, sp.Interval(-sp.pi, sp.pi)) == sp.FiniteSet(0),
    "E >= 0 on the BZ with the only zero at k = 0")
Emax = E.subs({k1: sp.pi, k2: sp.pi, k3: sp.pi})
chk("N4", Emax == 12 and sp.simplify(sp.Max(*[E.subs(dict(zip(K, c)))
                                              for c in [(0, 0, 0), (sp.pi, 0, 0),
                                                        (sp.pi, sp.pi, 0), (sp.pi, sp.pi, sp.pi)]]) - 12) == 0,
    "max E = 12 at the zone corner")

# ------------------------------------------- L: candidate (iii), light-cone 3+1
phi7 = (1 + 2 * sum(sp.cos(k) for k in K)) / 7
chk("L1a", sp.simplify(7 * (1 - phi7) - E) == 0, "7(1 - phi_7) = E exactly")
chk("L1b", sp.simplify(7 * (1 + phi7) - (14 - E)) == 0, "7(1 + phi_7) = 14 - E exactly")

s2, Es = sp.symbols("sigma2 E", positive=True)
phiE = 1 - Es / 7
chi = sp.simplify(1 / (1 - phiE))
C = sp.simplify(s2 / (1 - phiE ** 2))
chk("L2a", sp.simplify(chi - 7 / Es) == 0, "static response chi = 1/(1-phi) = 7/E")
chk("L2b", sp.simplify(C - 49 * s2 / (Es * (14 - Es))) == 0,
    "equal-time covariance C = 49 sigma^2/(E(14-E))")
chk("L2c", sp.simplify(C - sp.Rational(7, 2) * s2 * (1 / Es + 1 / (14 - Es))) == 0,
    "C = (7/2) sigma^2 (1/E + 1/(14-E))")
chk("L2d", sp.simplify(C / (s2 * chi) - 7 / (14 - Es)) == 0,
    "C/(sigma^2 chi) = 7/(14-E): 1/2 at k->0, 7/2 at the corner")
chk("L3", sp.simplify((14 - Emax) - 2) == 0,
    "14 - E >= 2 > 0 on the whole BZ: C is positive, its second term short-range")

# ---------------------------------- S: the normalisation, and its bookkeeping
kap, bet = sp.symbols("kappa beta", positive=True)
A = sp.Function("A")
sig_sc = A(kap) / kap                       # single-site transverse variance
bet_sc = kap / (7 * A(kap))                 # from kappa = 7 beta m, m = A(kappa)
chk("S1", sp.simplify(7 * bet_sc * sig_sc - 1) == 0,
    "SELF-CONSISTENT bookkeeping: sigma^2 = 1/(7 beta) identically, for EVERY A")
out_resp = sp.simplify(sig_sc * 7 / Es)
out_cov = sp.simplify(sp.Rational(7, 2) * sig_sc / Es)
chk("S2a", sp.simplify(out_resp - 1 / (bet_sc * Es)) == 0,
    "node input sigma^2 chi = G/beta exactly (G = 1/E), A-independent")
chk("S2b", sp.simplify(out_cov - 1 / (2 * bet_sc * Es)) == 0,
    "two-point tail coefficient = G/(2 beta) exactly, A-independent")
b = sp.symbols("b", positive=True)            # beta, via its defining relation A(kappa)=kappa/(7b)
coeff_resp = sp.simplify((out_resp * Es).subs(A(kap), kap / (7 * b)))
coeff_cov = sp.simplify((out_cov * Es).subs(A(kap), kap / (7 * b)))
chk("S3a", sp.simplify(coeff_resp - 1 / b) == 0 and sp.solve(sp.Eq(coeff_resp, 1), b) == [1],
    "unit Newtonian coefficient, response slot  <=>  beta = 1 EXACTLY")
chk("S3b", sp.simplify(coeff_cov - 1 / (2 * b)) == 0
    and sp.solve(sp.Eq(coeff_cov, 1), b) == [sp.Rational(1, 2)],
    "unit Newtonian coefficient, two-point slot <=>  beta = 1/2 EXACTLY")

# S4  what is scheme-independent: the concentration kappa*, not beta
#     sigma^2 = A(kappa)/kappa = Sum_n 2/(kappa^2 + n^2 pi^2)   (Mittag-Leffler)
n = sp.symbols("n", positive=True, integer=True)
term = 2 / (kap ** 2 + n ** 2 * sp.pi ** 2)
langevin = sp.coth(kap) - 1 / kap
chk("S4a", sp.simplify(sp.summation(term.subs(kap, 0), (n, 1, sp.oo)) - sp.Rational(1, 3)) == 0,
    "sum_n 2/(n^2 pi^2) = 1/3 exactly: A(kappa)/kappa -> 1/3 as kappa -> 0")
chk("S4a2", sp.simplify(sp.diff(term, kap) + 4 * kap / (kap ** 2 + n ** 2 * sp.pi ** 2) ** 2) == 0,
    "every term falls as -4kappa/(...)^2 < 0: A(kappa)/kappa strictly decreasing, root unique")
chk("S4b", sp.series(langevin, kap, 0, 4).removeO() == kap / 3 - kap ** 3 / 45,
    "A(kappa) = coth kappa - 1/kappa = kappa/3 - kappa^3/45 + ...  (A'(0) = 1/3)")
for c, tag in ((sp.Rational(1, 7), "S4c"), (sp.Rational(2, 7), "S4d")):
    chk(tag, c < sp.Rational(1, 3),
        "sigma^2 = %s < 1/3: the root kappa* of A(kappa)/kappa = %s exists and is unique"
        % (c, c))


def A_over_k(kv):
    """A(kappa)/kappa as a rigorous interval."""
    e = iv.exp(2 * kv)
    return ((e + 1) / (e - 1) - 1 / kv) / kv


def enclose(target, lo, hi):
    """monotone decreasing A/k: sign change over [lo,hi] encloses the root."""
    return A_over_k(iv.mpf(lo)) - target > 0 and A_over_k(iv.mpf(hi)) - target < 0


t_resp, t_cov = iv.mpf(1) / 7, iv.mpf(2) / 7
chk("S5a", enclose(t_resp, "5.79145", "5.79146"),
    "response slot: kappa* in [5.79145, 5.79146]   (A(kappa*)/kappa* = 1/7)")
chk("S5b", enclose(t_cov, "1.63831", "1.63832"),
    "two-point slot: kappa* in [1.63831, 1.63832]  (A(kappa*)/kappa* = 2/7)")
# the prior attempt's two numbers are exactly kappa*/7 in the ALIGNED bookkeeping,
# which by the defining equation equals m* resp. m*/2 -- a magnetisation, not a coupling
chk("S5c", enclose(t_resp, "5.7911", "5.7918"),
    "aligned bookkeeping (kappa = 7 beta): beta = kappa*/7 in [0.8273, 0.8274] = m* = A(kappa*)")
chk("S5d", enclose(t_cov, "1.6380", "1.6387"),
    "aligned bookkeeping, two-point slot: beta = kappa*/7 in [0.2340, 0.2341] = m*/2")


def ml_bracket(kv, N=1000):
    """rigorous bracket for sum_n 2/(kappa^2+n^2 pi^2), tail bounded by 1/(1+u) >= 1-u."""
    k, pi2 = iv.mpf(kv), iv.pi ** 2
    s = iv.mpf(0)
    for j in range(1, N + 1):
        s = s + 2 / (k ** 2 + iv.mpf(j) ** 2 * pi2)
    hi = s + (2 / pi2) / iv.mpf(N)
    lo = s + (2 / pi2) / iv.mpf(N + 1) - (2 * k ** 2 / pi2 ** 2) / (3 * iv.mpf(N) ** 3)
    return lo, hi


lo, hi = ml_bracket("1")
chk("S5e", (lo - A_over_k(iv.mpf(1)) < 0) and (hi - A_over_k(iv.mpf(1)) > 0),
    "the partial-fraction form brackets A(1)/1 to ~2e-7: the Mittag-Leffler route checks out")
chk("S6a", sp.simplify(sp.Rational(3, 7) - 3 * sp.Rational(1, 7)) == 0 and
    sp.Rational(3, 7) < 1 and sp.Rational(3, 7) < sp.Rational(1, 2),
    "aligned-state threshold beta > 3/7 (from A'(0)=1/3): beta=1 and beta=1/2 clear it")
chk("S6b", sp.Rational(2341, 10000) < sp.Rational(3, 7),
    "the aligned bookkeeping's two-point root 0.2341 < 3/7: no aligned state there")
# S8  the two bookkeepings impose the SAME equation on the state: only the label beta moves
for lab, bval, targ in (("S8a", 1, sp.Rational(1, 7)), ("S8b", sp.Rational(1, 2), sp.Rational(2, 7))):
    self_c = sp.solve(sp.Eq(kap, 7 * bval * A(kap)), A(kap))[0]     # kappa = 7 beta m, m = A(kappa)
    chk(lab, sp.simplify(self_c / kap - targ) == 0,
        "self-consistent beta = %s and aligned beta = kappa*/7 impose the same A(kappa)/kappa"
        " = %s: same kappa*, same sigma^2, different label" % (bval, targ))

gap_lo, gap_hi = 1 / sp.Rational(8274, 10000), 1 / sp.Rational(8273, 10000)
chk("S7", sp.Rational(12, 10) < gap_lo and gap_hi < sp.Rational(122, 100),
    "the two exact bookkeepings differ by the factor 1/m* = 1.2087: a 21% spread in beta,"
    " against a quoted bracket width of 1.5e-4")

# ------------------------------------------- B: candidate (ii), backward 3+1
phi4 = (1 + sum(sp.exp(sp.I * k) for k in K)) / 4
S = sp.simplify(sp.expand(1 - sp.Abs(phi4) ** 2).rewrite(sp.cos))
S = sp.simplify(sp.re(sp.expand(1 - phi4 * sp.conjugate(phi4))))
fcc = (sum(1 - sp.cos(k) for k in K)
       + sum(1 - sp.cos(a - b) for a, b in ((k1, k2), (k1, k3), (k2, k3)))) / 8
chk("B1", sp.simplify(sp.expand_trig(sp.expand(S - fcc))) == 0,
    "1-|phi_4|^2 = (1/8)[sum(1-cos k_j) + sum_{i<j}(1-cos(k_i-k_j))]: the FCC Laplacian")
serB = sp.series(fcc.subs({k1: t * x1, k2: t * x2, k3: t * x3}), t, 0, 4).removeO()
xv = sp.Matrix(X)
M = (4 * sp.eye(3) - sp.ones(3, 3)) / 16
chk("B2", sp.simplify(sp.expand(serB.coeff(t, 2)) - sp.expand((xv.T * M * xv)[0, 0])) == 0,
    "its Hessian is k^T(4I - J)k/16, NOT a multiple of |k|^2")
ev = M.eigenvals()
chk("B3a", ev == {sp.Rational(1, 4): 2, sp.Rational(1, 16): 1},
    "eigenvalues {1/4, 1/4, 1/16}: ratio 4, two distinct values -> no rotation fixes it")
chk("B3b", M.det() == sp.Rational(1, 256) and sp.simplify(M.inv() - 4 * (sp.eye(3) + sp.ones(3, 3))) == sp.zeros(3, 3),
    "det = 1/256, inverse = 4(I + J) exactly")
# unique zero of the symbol in the BZ: a sum of six nonnegative terms vanishes iff each does,
# and 1 - cos vanishes only at 0 on [-pi, pi]
chk("B4", sp.solveset(sp.Eq(1 - sp.cos(k1), 0), k1, sp.Interval(-sp.pi, sp.pi)) == sp.FiniteSet(0)
    and sp.minimum(1 - sp.cos(k1), k1, sp.Interval(-sp.pi, sp.pi)) == 0
    and sp.simplify(fcc.subs({k2: 0, k3: 0}) - sp.Rational(3, 8) * (1 - sp.cos(k1))) == 0,
    "six nonnegative terms: the symbol vanishes only at k = 0 in the BZ, as the node's does")


def amp(nvec):
    """1/r amplitude of the kernel 1/(k^T M k) along the unit direction nvec."""
    nv = sp.Matrix(nvec)
    nv = nv / sp.sqrt((nv.T * nv)[0, 0])
    return sp.simplify(1 / (4 * sp.pi * sp.sqrt(M.det()) * sp.sqrt((nv.T * M.inv() * nv)[0, 0])))


a_perp, a_diag = amp([1, -1, 0]), amp([1, 1, 1])
chk("B5a", sp.simplify(a_perp / a_diag - 2) == 0,
    "1/r amplitude in the level plane is EXACTLY TWICE the amplitude along [111]")
psi = sp.symbols("psi", real=True)
prof = sp.simplify(amp([1, -1, 0]) * sp.sqrt(1) / sp.sqrt(1 + 3 * sp.cos(psi) ** 2))
chk("B5b", sp.simplify(prof.subs(psi, 0) - a_diag) == 0 and
    sp.simplify(prof.subs(psi, sp.pi / 2) - a_perp) == 0,
    "angular profile amplitude(psi) = (2/pi) / sqrt(1 + 3 cos^2 psi), psi = angle to [111]")
chk("B6", sp.simplify(a_perp / a_diag - 1) != 0,
    "so NO sigma^2 normalises (ii) to 1/(4 pi r): the needed factor varies by 2 with"
    " direction -- an order r^-1 failure, where main's own anisotropy is order r^-3")

# -------------------------------------------- I: candidate (i), backward 2+1
w = sp.symbols("w", real=True)
for nn in range(4):
    val = sp.integrate(sp.exp(sp.I * w * nn) / (2 * sp.pi), (w, -sp.pi, sp.pi))
    chk("I1.%d" % nn, sp.simplify(val - (1 if nn == 0 else 0)) == 0,
        "a symbol independent of the level-time momentum w transforms to delta_{n,0}"
        if nn == 0 else "  ... so the equal-level kernel vanishes off its own level (n=%d)" % nn)

print()
print("TOTAL: PASS=%d FAIL=%d" % (P, F))
print("HIT: the node's slot on main is the RESOLVENT (NEWTON_LAW_DERIVED_NOTE.md L44-47,"
      " L61-64 @ abb98a122e), so the light-cone input is sigma^2 chi; in the"
      " self-consistent bookkeeping kappa = 7 beta m, m = A(kappa), sigma^2 = A(kappa)/kappa"
      " the output is EXACTLY G/beta for every A, so the node's unit Newtonian"
      " normalisation is exactly beta = 1 (and beta = 1/2 for the two-point reading).")
print("HIT: the node's normalisation fixes the STATE, not the coupling: the prescribed"
      " sigma^2 = A(7beta)/(7beta) and the self-consistent sigma^2 = A(kappa)/kappa with"
      " kappa = 7 beta m, m = A(kappa) impose the SAME equation A(kappa*)/kappa* = 1/7"
      " (kappa* in [5.79145, 5.79146], sigma^2 = 1/7), and differ only in the label beta:"
      " kappa*/7 = 0.82735... = A(kappa*) = m* versus exactly 1. So beta carries a 21%"
      " bookkeeping spread, against a quoted bracket width of 1.5e-4.")
print("HIT: candidate (ii) backward 3+1 fails the node at leading order, exactly: its symbol's"
      " Hessian k^T(4I-J)k/16 has eigenvalues {1/4,1/4,1/16}, so the 1/r amplitude is"
      " (2/pi)/sqrt(1+3cos^2 psi) -- twice as large in the level plane as along [111] -- and no"
      " sigma^2 can normalise it, where main's own lattice anisotropy enters only at r^-3.")
print("SUMMARY: PARTIAL the node's slot is the resolvent (so sigma^2 chi, not the AR(1)"
      " equal-time covariance); sigma^2 chi = G/beta and C_tail = G/(2beta) hold identically"
      " in the self-consistent bookkeeping, making the node's normalisation beta = 1 resp."
      " 1/2 exactly and A-independent; the scheme-independent content is kappa*, and beta"
      " carries a 21% bookkeeping spread; A(kappa)/kappa = sum_n 2/(kappa^2+n^2 pi^2) re-proves"
      " the monotonicity lemma in one line; candidate (ii) fails isotropy at order r^-1 with"
      " the exact profile 1/sqrt(1+3cos^2 psi) (ratio 2), candidate (i) is confined to one level.")
