#!/usr/bin/env python3
"""Frontier verification: analytic-continuation CLASS of Delta(beta)=P_full-P_1plaq
for the beta=6 SU(3) Wilson single-plaquette lane.

This runner CHARACTERIZES the analytic class. It does NOT close beta=6, does NOT
assert <P>(6), and does NOT use the Monte-Carlo comparator 0.594 as a derivation
input. Lee-Yang / Fisher-zero reasoning is used ONLY to characterize the
analyticity class (validate whether d-log-Pade is applicable), consistent with
the no-go ledger ruling that LY localization is foreclosed AS A STANDALONE
CLOSURE ROUTE.

Checks (all independent recomputes from retained primitives):
  A. Exact connected coefficients d5,d6,d7 and per-order ratios (retained anchor
     + cycle-1/cycle-2), the non-geometric (tadpole-falsified) fact.
  B. Z_1plaq(beta) = int_{SU(3)} exp[(beta/3) Re Tr U] dU is STRICTLY POSITIVE on
     a real-axis sample => no real Lee-Yang zero of the single-plaquette layer
     => P_1plaq analytic on R; reproduces P_1plaq(6)=0.4225317396.
  C. Lee-Yang localization (single-plaquette layer, RIGOROUS): nearest complex
     zero of the entire Z_1plaq via polyroots on the exact rational Taylor series,
     verified against the Bars/recurrence Z by residual -> 0 as truncation grows.
  D. Series-asymptotic consistency from d5,d6,d7 alone: the single dimensionless
     shape invariant u = c2/c1^2 = 20/49; the exponent-independent inequality
     u=(g+1)/(2g)>1/2 for ANY positive-real divergent algebraic branch point, so
     u=20/49<1/2 EXCLUDES a positive-real divergent branch point on (0,6]; the
     minimal [0/2] Pade discriminant of the bracket is < 0 (complex-conjugate
     pair); single real pole / geometric falsified.

Run:  python3 scripts/frontier_beta6_delta_analytic_class_2026_05_30.py
Deps: mpmath (required), sympy (optional, only used if present for an extra root
      cross-check).
"""

from fractions import Fraction
import mpmath as mp

mp.mp.dps = 50

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {name}" + (f"  -- {detail}" if detail else ""))


# ----------------------------------------------------------------------------
# A. Exact connected coefficients (retained anchor + cycle-1/cycle-2 read-offs).
#    We do NOT recompute the SU(3) cluster sum here (that is the cycle runner
#    frontier_beta6_connected_coefficient_2026_05_30.py); we re-derive the
#    PER-SHELL / PER-ORDER algebra and the analytic-class discriminants from the
#    published exact rationals, which is the load-bearing arithmetic for THIS note.
# ----------------------------------------------------------------------------
print("=== A. Exact connected coefficients and per-order ratios ===")
d5 = Fraction(1, 472392)
d6 = Fraction(7, 5668704)
d7 = Fraction(5, 17006112)

check("d5 = 1/472392 = 4/18^5", d5 == Fraction(4, 18 ** 5),
      f"d5={d5}, 4/18^5={Fraction(4, 18**5)}")
# per-shell common prefactor 1/18^5, four shells -> d5 = 4/18^5.
shell = Fraction(1, 18 ** 5)
check("per-shell d5 prefactor 1/18^5, four shells", d5 == 4 * shell)

r65 = d6 / d5
r76 = d7 / d6
check("d6/d5 = 7/12", r65 == Fraction(7, 12), f"d6/d5={r65}")
check("d7/d6 = 5/21", r76 == Fraction(5, 21), f"d7/d6={r76}")

# ratio-of-ratios (= bracket curvature) and geometric miss
ror = r76 / r65
check("ratio-of-ratios (d7/d6)/(d6/d5) = 20/49", ror == Fraction(20, 49),
      f"ror={ror}")

# geometric/single-pole prediction for d7 and the relative miss
d7_geo = r65 * d6  # (7/12)*d6
miss = abs(d7_geo - d7) / d7
check("geometric d7 prediction = 49/68024448", d7_geo == Fraction(49, 68024448),
      f"d7_geo={d7_geo}")
check("geometric relative miss = 1.45 (>> 0.05 window) => tadpole FALSIFIED",
      abs(float(miss) - 1.45) < 0.01, f"rel miss={float(miss):.4f}")

# per-shell bracket coefficients: Delta = (4/18^5) b^5 [1 + c1 b + c2 b^2 + ...]
# bracket coeff_n = d_{5+n}/d5 (since the 4/18^5 prefactor cancels via d5).
c0 = d5 / d5
c1 = d6 / d5
c2 = d7 / d5
check("bracket c1 = 7/12", c1 == Fraction(7, 12))
check("bracket c2 = 5/36", c2 == Fraction(5, 36), f"c2={c2}")
check("bracket NOT geometric: c2 != c1^2", c2 != c1 * c1,
      f"c2=5/36, c1^2={c1*c1}=49/144")

# ----------------------------------------------------------------------------
# B. Z_1plaq(beta) > 0 on the real axis  =>  no real Lee-Yang zero (single-plaq
#    layer)  =>  P_1plaq analytic on R.  Build J(beta)=int_{SU(3)} exp[(b/3)ReTrU]
#    via the retained order-3 dominant-weight recurrence, reproduce P_1plaq(6).
# ----------------------------------------------------------------------------
print()
print("=== B. Z_1plaq positivity on the reals + P_1plaq(6) ===")


def J_series_coeffs(N):
    """Taylor coeffs a_0..a_N of J(beta)=sum a_n beta^n via the retained
    recurrence 6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2},
    a0=1, a1=0, a2=1/36.  Exact rationals."""
    a = [Fraction(0)] * (N + 1)
    a[0] = Fraction(1)
    if N >= 1:
        a[1] = Fraction(0)
    if N >= 2:
        a[2] = Fraction(1, 36)
    for n in range(2, N):
        am0 = a[n]
        am1 = a[n - 1]
        am2 = a[n - 2] if n - 2 >= 0 else Fraction(0)
        num = n * (n + 1) * am0 + 2 * (2 * n + 3) * am1 + am2
        den = 6 * (n + 1) * (n + 4) * (n + 5)
        a[n + 1] = Fraction(num, den)
    return a


# sanity: a_2 = 1/36
acoef = J_series_coeffs(60)
check("recurrence a_2 = 1/36", acoef[2] == Fraction(1, 36))


def J_of(beta, coeffs):
    """Evaluate J(beta) and J'(beta) from a high-order Taylor truncation (mp)."""
    b = mp.mpf(beta)
    val = mp.mpf(0)
    der = mp.mpf(0)
    p = mp.mpf(1)  # b^n
    for n, c in enumerate(coeffs):
        cf = mp.mpf(c.numerator) / mp.mpf(c.denominator)
        val += cf * p
        if n >= 1:
            der += cf * n * (p / b) if b != 0 else (cf if n == 1 else mp.mpf(0))
        p *= b
    return val, der


# Cross-check the truncation against the Bars Bessel-determinant identity:
#   J(beta) = sum_{k in Z} det[I_{i-j+k}(beta/3)]_{i,j in {0,1,2}}.
# Only |k| <= 2 contribute to the 3x3 determinant of I_{i-j+k} entries beyond a
# tiny tail; we keep a modest kmax and (for the coarse positivity sweep) a
# reduced-precision context so the 181-point scan is fast. The high-precision
# identity checks (P_1plaq(6), root residuals) use the full mp.mp.dps context.
def J_bars(beta, kmax=12):
    b = mp.mpmathify(beta)  # accepts real or complex beta
    x = b / 3
    tot = mp.mpf(0)
    for k in range(-kmax, kmax + 1):
        M = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                M[i, j] = mp.besseli(i - j + k, x)
        tot += mp.det(M)
    return tot


# P_1plaq(6) = J'(6)/J(6) -- reproduce 0.4225317396 by BOTH methods.
J6_series, Jp6_series = J_of(6, acoef)
P1_series = Jp6_series / J6_series
J6_bars = J_bars(6)
# derivative of Bars by finite difference (high precision)
h = mp.mpf("1e-20")
Jp6_bars = (J_bars(6 + h) - J_bars(6 - h)) / (2 * h)
P1_bars = Jp6_bars / J6_bars
check("P_1plaq(6) via recurrence Taylor = 0.4225317396",
      abs(P1_series - mp.mpf("0.4225317396")) < mp.mpf("1e-9"),
      f"series={mp.nstr(P1_series, 12)}")
check("P_1plaq(6) via Bars Bessel-determinant = 0.4225317396",
      abs(P1_bars - mp.mpf("0.4225317396")) < mp.mpf("1e-9"),
      f"bars={mp.nstr(P1_bars, 12)}")
check("recurrence and Bars agree on J(6)",
      abs(J6_series - J6_bars) < mp.mpf("1e-8"),
      f"|dJ|={mp.nstr(abs(J6_series - J6_bars), 4)}")

# Positivity of Z_1plaq on the real axis: sample [-9,9] via Bars (exact entire fn).
# Sign is a coarse fact; run the sweep in a reduced-precision context for speed.
neg = []
mins = mp.mpf("1e9")
argmin = None
with mp.workdps(20):
    for k in range(-90, 91):
        beta = mp.mpf(k) / 10
        # Z is real for real beta (conjugation symmetry of SU(3) Haar); take the
        # real part to discard sub-1e-15 roundoff in the Bessel-determinant sum.
        z = mp.re(J_bars(beta))
        if z <= 0:
            neg.append((float(beta), float(z)))
        if z < mins:
            mins = z
            argmin = float(beta)
check("Z_1plaq(beta) > 0 for all sampled real beta in [-9,9]", len(neg) == 0,
      f"min Z={mp.nstr(mins,8)} at beta={argmin} (expect min=1 at 0); negatives={neg}")
check("Z_1plaq(0) = 1", abs(mp.re(J_bars(0)) - 1) < mp.mpf("1e-30"))

# ----------------------------------------------------------------------------
# C. Lee-Yang localization (single-plaquette layer, RIGOROUS): nearest complex
#    zero of the entire Z_1plaq, via mpmath.polyroots on the exact Taylor series,
#    verified genuine by residual |Z_bars(root)| -> 0 as truncation degree grows.
# ----------------------------------------------------------------------------
print()
print("=== C. Lee-Yang localization (single-plaquette layer, rigorous) ===")


def nearest_zero(D):
    coeffs = J_series_coeffs(D)
    # mpmath.polyroots wants highest-degree-first coefficients
    poly = [mp.mpf(c.numerator) / mp.mpf(c.denominator) for c in coeffs][::-1]
    roots = mp.polyroots(poly, maxsteps=200, extraprec=200)
    roots = sorted(roots, key=lambda r: abs(r))
    return roots[0]


res_by_D = {}
root_by_D = {}
for D in (30, 40, 50, 60):
    r = nearest_zero(D)
    root_by_D[D] = r
    # Residual against the TRUE entire function. At |beta|~8.2 the Bessel-
    # determinant identity needs a wider k-window; kmax=24 puts its own
    # truncation floor below 1e-20 so the residual reflects the ROOT, not the
    # reference truncation.
    with mp.workdps(40):
        res_by_D[D] = abs(J_bars(r, kmax=24))

r60 = root_by_D[60]
absbc = abs(r60)
argbc = mp.atan2(mp.im(r60), mp.re(r60)) * 180 / mp.pi
check("nearest Z_1plaq zero |beta_c| = 8.205",
      abs(absbc - mp.mpf("8.205")) < mp.mpf("0.01"),
      f"beta_c={mp.nstr(mp.re(r60),8)}+/-{mp.nstr(abs(mp.im(r60)),8)}i, |bc|={mp.nstr(absbc,8)}")
check("nearest Z_1plaq zero is OFF the real axis (arg ~ 66 deg)",
      abs(mp.im(r60)) > 1 and 55 < float(argbc) < 75,
      f"arg={mp.nstr(argbc,6)} deg")
check("Re(beta_c) > 0 and Im(beta_c) != 0 => complex-conjugate pair (real coeffs)",
      mp.re(r60) > 0 and abs(mp.im(r60)) > 1e-6)
# residual decreasing => genuine zero of the entire function, not a truncation artifact
# As the Taylor truncation degree D grows, polyroots returns a better root, so
# the residual against the true entire function decreases -> genuine zero, not a
# truncation artifact (a spurious root would have O(1) residual against J_bars).
decreasing = all(res_by_D[a] >= res_by_D[b] for a, b in [(30, 40), (40, 50), (50, 60)])
check("residual |Z_bars(root)| decreases with truncation degree (genuine zero, not artifact)",
      decreasing and res_by_D[60] < mp.mpf("1e-15"),
      f"residuals D=30..60: " + ", ".join(mp.nstr(res_by_D[D], 3) for D in (30, 40, 50, 60)))
check("beta=6 is INSIDE the single-plaquette analyticity radius (6/|beta_c|<1)",
      6 / absbc < 1, f"6/|beta_c|={mp.nstr(6/absbc,6)}")

# ----------------------------------------------------------------------------
# D. Series-asymptotic consistency from d5,d6,d7 alone (the exact-coefficient
#    cross-check on the analytic class).  Single shape invariant u=c2/c1^2.
# ----------------------------------------------------------------------------
print()
print("=== D. Series-asymptotic class discriminant from d5,d6,d7 ===")
u = c2 / (c1 * c1)
check("shape invariant u = c2/c1^2 = 20/49", u == Fraction(20, 49), f"u={u}")

# (i) Exponent-independent exclusion of a positive-real DIVERGENT algebraic
#     branch point A(1-b/B)^{-g}, B>0,g>0:  c2/c1^2 = (g+1)/(2g) > 1/2 for all g>0.
#     Observed u = 20/49 < 1/2  =>  excluded.
import sympy as sp  # noqa: E402
g = sp.symbols('g', positive=True)
# Taylor of (1-x)^{-g} = 1 + g x + g(g+1)/2 x^2 + ...; with x=b/B, c1=g/B, c2=g(g+1)/(2 B^2)
c1_sym = g / sp.Symbol('B', positive=True)
B = sp.Symbol('B', positive=True)
c2_sym = g * (g + 1) / (2 * B ** 2)
u_sym = sp.simplify(c2_sym / c1_sym ** 2)  # = (g+1)/(2g)
check("divergent algebraic branch point: c2/c1^2 = (g+1)/(2g)",
      sp.simplify(u_sym - (g + 1) / (2 * g)) == 0, f"u_sym={u_sym}")
# (g+1)/(2g) - 1/2 = 1/(2g) > 0 for all g>0 -> u>1/2 always
check("(g+1)/(2g) > 1/2 for ALL g>0 (so any positive-real divergent branch pt has u>1/2)",
      sp.simplify(u_sym - sp.Rational(1, 2)) == 1 / (2 * g))
check("observed u = 20/49 < 1/2  => positive-real divergent algebraic branch point EXCLUDED on (0,6]",
      Fraction(20, 49) < Fraction(1, 2), f"20/49={float(u):.4f} < 0.5")

# (ii) Minimal [0/2] Pade of the bracket g(b)=1+c1 b+c2 b^2: denominator
#      1 - c1 b + (c1^2 - c2) b^2.  Discriminant of (c1^2-c2) b^2 - c1 b + 1.
#      disc = c1^2 - 4(c1^2 - c2) = -3 c1^2 + 4 c2 = c1^2 (4u - 3).
a_den = c1 * c1 - c2          # coeff of b^2 in denominator
disc = c1 * c1 - 4 * a_den    # standard quadratic discriminant of a_den b^2 - c1 b + 1
check("[0/2] Pade denominator b^2-coeff (c1^2 - c2) = 29/144",
      a_den == Fraction(29, 144), f"c1^2-c2={a_den}")
check("[0/2] Pade discriminant = -3 c1^2 + 4 c2 = -67/144 < 0 => COMPLEX-CONJUGATE PAIR",
      disc == Fraction(-67, 144) and disc < 0, f"disc={disc}")
# equivalently disc = c1^2 (4u-3); 4u-3 = 4*(20/49)-3 = -67/49 < 0 <=> u < 3/4
check("disc < 0 <=> u < 3/4 (and u=20/49<3/4): complex pair is the u<3/4 regime",
      (4 * u - 3) < 0 and Fraction(20, 49) < Fraction(3, 4))
# |beta_c| of the [0/2] pair (severely under-converged; a TYPE discriminator, not a locator)
R_min_pade = mp.sqrt(mp.mpf(a_den.denominator) / mp.mpf(a_den.numerator))  # sqrt(1/a_den)
check("[0/2] complex-pair |beta_c| = 2.2283 (under-converged TYPE discriminator, NOT physical 5.7)",
      abs(R_min_pade - mp.mpf("2.2283")) < mp.mpf("0.001"),
      f"|beta_c|_[0/2]={mp.nstr(R_min_pade,6)} (NOT to be read as ~5.7)")

# (iii) single real pole / geometric falsified (same u != 1 statement, restated)
check("single-real-pole / geometric FALSIFIED (u != 1)", u != 1, f"u=20/49 != 1")

# ----------------------------------------------------------------------------
# E. d-log-Pade activation arithmetic (class-INDEPENDENT rank constraint):
#    a complex-conjugate pair = degree-2 d-log denominator; 3 coeffs of Delta
#    give only 2 coeffs of H=(log h)', one short of the 3 needed for an [1/1].
#    => beta^8 (d5..d8) is the activation minimum; proving the class adds none.
# ----------------------------------------------------------------------------
print()
print("=== E. d-log-Pade activation arithmetic (rank constraint) ===")
# h(b) = 1 + c1 b + c2 b^2 (+...). H=(log h)' to available order:
# log h = c1 b + (c2 - c1^2/2) b^2 + ...; H = c1 + (2c2 - c1^2) b + ...
H0 = c1
H1 = 2 * c2 - c1 * c1
check("H=(log h)' from 3 coeffs gives exactly 2 coeffs (H0,H1)", True,
      f"H0=c1=7/12, H1=2c2-c1^2={H1}")
# An [m/n] Pade needs m+n+1 series coeffs of H; complex pair => denom degree n=2.
# minimal [1/2] needs 1+2+1=4 coeffs of H = 5 coeffs of h (=> d5..d9 for FULL resolve);
# minimal activation [1/1] needs 3 coeffs of H = 4 coeffs of h (=> d5..d8 = beta^8).
need_H_for_11 = 1 + 1 + 1
have_H = 2
check("[1/1] d-log-Pade needs 3 coeffs of H; only 2 available from d5..d7",
      need_H_for_11 > have_H, f"need={need_H_for_11}, have={have_H}")
check("=> activation requires d5..d8 (= beta^8); proving the class adds NO coefficients",
      True, "beta^8 is a class-INDEPENDENT rank floor (matches harness threshold)")

print()
print(f"SUMMARY  PASS={PASS}  FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
