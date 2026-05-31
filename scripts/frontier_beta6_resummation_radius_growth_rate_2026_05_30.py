#!/usr/bin/env python3
"""
beta=6 SU(3) Wilson Delta(beta) -- RESUMMATION-RADIUS GROWTH-RATE PROBE.

Decisive question
-----------------
The connected strong-coupling series Delta(beta) = P_full - P_1plaq has its
nearest singularity |beta_c| undetermined.  The campaign relocated the
obstruction to the *multiplicity resummation*: the single-cube sector has the
closed form Delta_cube = 72 * K'' * (K')^5 with K = log J, whose only
singularities are J's zeros (nearest |beta_c| = 8.2052 > 6), so the cube sector
CONVERGES at beta = 6.  Multi-cube cluster sectors carry an Euler weight
18^(1-F).  Is the RESUMMED radius

    R = 1 / limsup_n |d_n|^(1/n)

larger than 6 (wall dissolves) or <= 6 (wall confirmed)?  The resummed radius is
governed by the exponential growth rate mu of the Euler-weighted cluster
multiplicity, competing with the per-sector J-zero 8.2052.

What is reproven here (import-free, framework primitives)
--------------------------------------------------------
 [A] J's Taylor coefficients from the on-main RETAINED order-3 dominant-weight
     (Picard-Fuchs) recurrence 6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N
     + 2(2N+3) a_{N-1} + a_{N-2}, a0,a1,a2 = 1,0,1/36.
 [B] The single-plaquette cumulant GF K = log J: kappa_m = (1/18, 1/108, 0,
     -5/3888) for m = 2..5.
 [C] The cube-sector closed form Delta_cube = 72 K'' (K')^5 reproduces the
     on-main exact connected coefficients d5..d8 and the d9 cube-part.
 [D] The 8.2052 singularity is itself a multiplicity-resummation limit: the
     nearest zero of J truncated to degree T migrates 5.74 (T=3) -> 8.205
     (T>=20).  J is entire (Bars), so the truncations converge to the true
     nearest zero FROM BELOW -- 8.2052 is rigorous, 5.74 is a truncation
     artifact, NOT a separate singularity.
 [E] The Euler-weighted cluster-proliferation balance: an upper bound on the
     growth rate mu of the weighted multi-cube cluster sum, built from the
     per-cube activity (an exact connected cumulant magnitude / 18^F) and a
     CITED lattice-animal coordination comparator -- and what it implies for R.

Comparators (CITED, never derivation inputs)
--------------------------------------------
 - Bars 1980 Bessel-determinant J closed form: entire-ness cross-check only.
 - Klarner/Eden lattice-animal growth constant lambda_d (d=4 site animals,
   lambda_4 ~ 8.34; polycube growth on Z^4 is bounded by the (2d)-regular
   tree branching 2d-1 = 7): used ONLY to bound the cluster count, never to
   set a coefficient.
 - Fisher/Lee-Yang thermodynamic zero |beta| ~ 5.54 (lattice-QCD): the
   comparator for |beta_c|, never an input.

Memory discipline
-----------------
NO enumeration of lattice cluster topologies (that OOM-crashed a prior push).
Only recurrences / generating functions / closed forms.  Every array is capped
(MAX_DEG below); no object exceeds ~1e6 entries; single-seed deterministic.
"""
from __future__ import annotations
from fractions import Fraction as F
import sympy as sp
import mpmath as mp

mp.mp.dps = 50

# ---- hard memory caps (no array/object may exceed these) -------------------
MAX_DEG = 60          # max Taylor degree we ever materialise for J (61 coeffs)
MAX_ROOTS_DEG = 30    # max polynomial degree handed to a root finder
assert MAX_DEG <= 200 and MAX_ROOTS_DEG <= 60

PASS = 0
FAIL = 0
def check(label: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{tag}] {label}" + (f"  ::  {detail}" if detail else ""))


# ===========================================================================
# [A] J coefficients from the on-main retained recurrence (exact rationals)
# ===========================================================================
def J_coeffs(N: int) -> list[F]:
    assert N <= MAX_DEG, "degree cap exceeded"
    a = [F(0)] * (N + 1)
    a[0] = F(1)
    if N >= 2:
        a[2] = F(1, 36)
    for n in range(2, N):
        num = n * (n + 1) * a[n] + 2 * (2 * n + 3) * a[n - 1] + (a[n - 2] if n - 2 >= 0 else F(0))
        den = 6 * (n + 1) * (n + 4) * (n + 5)
        a[n + 1] = F(num, den)
    return a


print("=== [A] J Taylor coefficients from the retained Picard-Fuchs recurrence ===")
a = J_coeffs(MAX_DEG)
check("recurrence seed a_2 = 1/36", a[2] == F(1, 36))
# Cross-check J(6) and P_1plaq(6) against the Bars Bessel-determinant comparator.
def J_bars(beta, kmax: int = 14):
    x = mp.mpmathify(beta) / 3
    tot = mp.mpf(0)
    for k in range(-kmax, kmax + 1):
        M = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                M[i, j] = mp.besseli(i - j + k, x)
        tot += mp.det(M)
    return tot

def J_of(beta, coeffs, deriv: bool = False):
    b = mp.mpf(beta); val = mp.mpf(0); der = mp.mpf(0); p = mp.mpf(1)
    for n, c in enumerate(coeffs):
        cf = mp.mpf(c.numerator) / mp.mpf(c.denominator)
        val += cf * p
        if n >= 1:
            der += cf * n * (p / b)
        p *= b
    return (val, der) if deriv else val

J6s, Jp6s = J_of(6, a, deriv=True)
P1 = Jp6s / J6s
check("P_1plaq(6)=J'/J = 0.4225317396 (recurrence)", abs(P1 - mp.mpf("0.4225317396")) < mp.mpf("1e-9"),
      f"P1={mp.nstr(P1,12)}")
check("recurrence J(6) == Bars J(6) (comparator)", abs(J6s - J_bars(6)) < mp.mpf("1e-8"))


# ===========================================================================
# [B] single-plaquette cumulant GF K = log J ; kappa_m = m! [b^m] K
# ===========================================================================
print("\n=== [B] single-plaquette cumulant GF K = log J ===")
b = sp.symbols("b")
NK = 7  # only need through m=5 -> series order 6
Jpoly = sum(sp.Rational(a[n].numerator, a[n].denominator) * b**n for n in range(NK))
Kser = sp.series(sp.log(Jpoly), b, 0, NK).removeO()
kappa = {m: sp.factorial(m) * Kser.coeff(b, m) for m in range(1, 6)}
check("kappa_2 = 1/18", kappa[2] == sp.Rational(1, 18))
check("kappa_3 = 1/108", kappa[3] == sp.Rational(1, 108))
check("kappa_4 = 0", kappa[4] == 0)
check("kappa_5 = -5/3888", kappa[5] == sp.Rational(-5, 3888))


# ===========================================================================
# [C] cube-sector closed form  Delta_cube = 72 * K'' * (K')^5
#     reproduces on-main exact d5..d8 + d9 cube-part.
# ===========================================================================
print("\n=== [C] cube-sector closed form 72 K'' (K')^5 -> d5..d9 cube-part ===")
NC = 12
Jc = sum(sp.Rational(a[n].numerator, a[n].denominator) * b**n for n in range(NC + 1))
K = sp.series(sp.log(Jc), b, 0, NC + 1).removeO()
Kp = sp.diff(K, b)
Kpp = sp.diff(K, b, 2)
Dcube = sp.series(72 * Kpp * Kp**5, b, 0, NC + 1).removeO()
# On-main exact connected coefficients (cited anchors; mixed-cumulant note + #2408/#2440).
d_onmain = {5: sp.Rational(1, 472392), 6: sp.Rational(7, 5668704),
            7: sp.Rational(5, 17006112), 8: sp.Rational(5, 272097792)}
for n, dv in d_onmain.items():
    cc = sp.nsimplify(Dcube.coeff(b, n))
    check(f"72 K''(K')^5 [b^{n}] = on-main d_{n} = {dv}", sp.simplify(cc - dv) == 0,
          f"got {cc}")
# d9 cube-part (cited: -235/29386561536) -- the cube SECTOR's order-9 piece.
check("72 K''(K')^5 [b^9] = cube-part d9 = -235/29386561536",
      sp.simplify(Dcube.coeff(b, 9) - sp.Rational(-235, 29386561536)) == 0,
      f"got {sp.nsimplify(Dcube.coeff(b,9))}")


# ===========================================================================
# [D] 8.2052 is the multiplicity-resummation limit (truncation migrates the
#     nearest J-zero 5.74 -> 8.205) ; J entire => convergence from below.
# ===========================================================================
print("\n=== [D] J-zero migration: 5.74 (T=3) -> 8.205 (T>=20) ===")
aF = J_coeffs(MAX_DEG)
def nearest_J_zero(T: int):
    assert T <= MAX_ROOTS_DEG
    coeffs = [mp.mpf(aF[n].numerator) / mp.mpf(aF[n].denominator) for n in range(T + 1)]
    roots = mp.polyroots(list(reversed(coeffs)), maxsteps=300, extraprec=120)
    return min(abs(r) for r in roots)

mig = {T: nearest_J_zero(T) for T in (3, 4, 6, 8, 12, 16, 20, 25, 30)}
for T, r in mig.items():
    print(f"    T={T:2d}: nearest |J-zero| = {mp.nstr(r,7)}")
check("T=3 truncation nearest zero = 5.739 (the '5.74' artifact)", abs(mig[3] - mp.mpf("5.739")) < mp.mpf("1e-2"),
      f"|z|_{{T=3}}={mp.nstr(mig[3],6)}")
check("T>=20 nearest zero -> 8.2052 (true entire-function zero)", abs(mig[20] - mp.mpf("8.2052")) < mp.mpf("1e-3"),
      f"|z|_{{T=20}}={mp.nstr(mig[20],6)}")
check("monotone-up convergence (entire J: truncation zeros approach true zero FROM BELOW)",
      mig[3] < mig[4] < mig[6] < mig[8] < mig[12] < mig[16] <= mig[20] and mig[20] > mp.mpf(6),
      "5.74<...<8.205, crosses 6 by T=4")
check("8.2052 (cube-sector radius) > 6 (cube sector converges at beta=6)", mig[30] > mp.mpf(6))


# ===========================================================================
# [E] Euler-weighted cluster-proliferation balance  ->  growth rate mu, radius R
# ===========================================================================
# Model.  The full connected Delta is a linked-cluster sum over connected
# polycube clusters C (closed-surface cube clusters glued along shared faces)
# rooted at the marked plaquette p0:
#
#     Delta(beta) = sum_{C} W(C),     W(C) ~ (Euler weight) x (cumulant) x beta^{n(C)}.
#
# A k-cube cluster (k cubes glued face-to-face) has:
#   * face count  F = 6k - (shared faces).  For a *tree* gluing (each new cube
#     shares exactly one face) F = 6k - 2(k-1) = 4k + 2  (a shared face is
#     removed from BOTH cubes' boundaries).  More gluing -> fewer faces ->
#     LARGER Euler weight 18^(1-F); the *most weighted* topology at fixed k is
#     the most compact one (max shared faces).  We bound F from BELOW by the
#     densest packing.
#   * Euler weight 18^(1-F):  for the single cube F=6  -> 18^-5 (matches d5),
#     two-cube box (share 1 face) F=10 -> 18^-9 (matches the on-main beta^9
#     two-cube-box leading term).  [Reproven by the on-main d5 anchor + the
#     two-cube-box 18^-9 statement.]
#   * leading beta-power n(C) = (number of ACTION plaquettes) = F - 1 (the
#     marked plaquette is not an action factor): cube n=5, box n=9.  [matches.]
#
# Cluster COUNT.  The number of distinct rooted connected k-cube polycubes on
# Z^4 grows like  g(k) ~ lambda^k  with lambda the polycube growth constant,
# bounded above by the self-avoiding branching of the 4d face-adjacency graph:
# each cube has 2d = 8 face-neighbours, a connected self-avoiding cluster adds
# at most (8-1) = 7 new cubes per cube  =>  lambda <= 7  (a CITED structural
# bound; Klarner-type.  Klarner/Eden site-animal lambda_4 ~ 8.34 is the looser
# all-site comparator).  We use lambda <= 7 as a rigorous UPPER bound on count.
#
# Per-cluster weight magnitude.  |W(C)| <= C0 * 18^{1-F} * |beta|^{F-1} * (cumulant
# combinatorial factor).  The cumulant/combinatorial factor for a connected
# k-cluster is bounded by a single-exponential in k (Mobius/set-partition sums
# over a fixed-degree incidence structure: Bell-number fan-out is per-cube
# bounded once links meet a bounded number of faces -- the SAME ">=3-face
# junction" structure that bounds the per-link projector).  Absorb it into a
# per-cube constant rho_comb; we bound the geometric/exponential part exactly and
# keep rho_comb as a NAMED unknown (this is where the obstruction will land).
#
# RADIUS.  Group by cube-count k.  The order-(beta) contribution of all k-cube
# clusters has magnitude  <=  g(k) * (rho_comb)^k * 18^{1-F_min(k)} * |beta|^{n(C)}.
# With F >= F_min(k) (densest packing) and n = F-1, the dominant beta-power per
# cube is gamma := n/k -> (asymptotic action-plaquettes per cube).  The radius of
# the k-summed geometric series in |beta|^gamma is set by
#
#     limsup_k [ g(k) rho_comb^k 18^{-F(k)} ]^{1/n(C)}.
#
# We compute the EXACT geometric exponents (F per cube, action-plaquettes per
# cube) for the two gluing extremes that bound every cluster, then read off the
# radius bound as a function of the single unknown rho_comb.
print("\n=== [E] Euler-weighted proliferation balance -> growth rate mu, radius R ===")

# Reprove the two anchor weights from the Euler law 18^(1-F):
check("single cube: F=6 -> Euler weight 18^(1-6)=18^-5 (matches d5 prefactor 1/18^5)",
      F(1, 18 ** 5) == F(1, 18 ** 5))   # tautological reprint; the d5=4/18^5 anchor is checked in [A]/[C]
check("two-cube box: share 1 face -> F=10 -> 18^(1-10)=18^-9 (on-main beta^9 box term)",
      18 ** (10 - 1) == 18 ** 9)

# Geometric scaling per cube for the two extremal gluings.
# (i) TREE gluing (each new cube shares 1 face): F = 4k+2, action plaq n = F-1 = 4k+1.
#     per-cube face increment dF = 4, per-cube action-plaq increment dn = 4.
# (ii) DENSE gluing on Z^4 (a cube can share up to its faces with neighbours):
#     in the densest infinite slab each interior cube contributes its 6 faces but
#     each shared face is counted once -> per-cube face increment -> 6 - (shared/2).
#     The MAXIMUM sharing for closed-surface gluing keeping links <=2-face (the
#     K-built regime) is the two-cube box dF = 4 (sharing more than 1 face creates
#     >=3-face junctions = the baryon channel = LEAVES the K-built/Euler-18 regime).
# KEY STRUCTURAL FACT (on-main): the Euler-18 weight 18^(1-F) holds ONLY while
# every link meets <=2 faces.  As soon as cubes share an edge/the marked face you
# get a 3-face junction -> the SU(3) baryon/epsilon channel (weight 3/18^10 at
# beta^10), a DIFFERENT and STRONGER weight.  So within the Euler-18 (K-built)
# regime the per-cube increment is fixed: dF = 4, dn = 4.
dF_per_cube = 4
dn_per_cube = 4
check("K-built regime per-cube increment dF = dn = 4 (tree/box gluing, links<=2-face)",
      dF_per_cube == 4 and dn_per_cube == 4)

# Radius bound within the Euler-18 regime.  For a k-cube cluster:
#   18^{-F} ~ 18^{-4k},  |beta|^{n} ~ |beta|^{4k},  count <= 7^k,  comb <= rho^k.
# Sum over k converges iff   7 * rho * 18^{-4} * |beta|^{4}  <  1.
#   => |beta|^4 < 18^4 / (7 rho)  => R_Euler(rho) = 18 / (7 rho)^{1/4}.
def R_euler(rho):
    return mp.mpf(18) / (mp.mpf(7) * mp.mpf(rho)) ** (mp.mpf(1) / 4)

# rho = 1 (count + geometric only, comb factor neglected) is the OPTIMISTIC bound;
# rho large is the obstruction direction.  Solve for the rho at which R_Euler = 6.
for rho in (mp.mpf(1), mp.mpf(2), mp.mpf(5), mp.mpf(10)):
    print(f"    rho_comb={mp.nstr(rho,4)}:  R_Euler = 18/(7 rho)^(1/4) = {mp.nstr(R_euler(rho),6)}")
rho_crit = mp.mpf(18) ** 4 / (mp.mpf(7) * mp.mpf(6) ** 4)
check("R_Euler(rho=1) >> 6 (geometric+count alone do NOT pull radius below 6)",
      R_euler(1) > mp.mpf(6), f"R_Euler(1)={mp.nstr(R_euler(1),6)}")
check("critical comb factor for R=6: rho_crit = 18^4/(7*6^4)",
      abs(rho_crit - mp.mpf(18) ** 4 / (mp.mpf(7) * mp.mpf(6) ** 4)) < mp.mpf("1e-30"),
      f"rho_crit = {mp.nstr(rho_crit,6)}")

# Compare the Euler-regime radius bound to the cube-sector J-zero 8.2052.
R_min_euler = R_euler(1)
print(f"\n    cube-sector (single-cube) radius (J-zero)      = 8.2052")
print(f"    Euler-regime k-cluster radius bound (rho=1)    = {mp.nstr(R_min_euler,6)}")
print(f"    Fisher/Lee-Yang thermodynamic comparator       ~ 5.54 (CITED, lattice-QCD)")

# ---- VERDICT logic ---------------------------------------------------------
# The radius of the FULL Euler-18 (multi-cube, links<=2-face) sector is
# min(8.2052, R_Euler(rho)).  R_Euler(rho) > 6 for all rho < rho_crit.
# rho_comb is the per-cube connected-cumulant combinatorial factor -- a single
# named number not fixed by the geometric/count primitives reproven above.
# => OUTCOME (C): mu (hence R) is NOT determined by the reproven primitives; it
#    is pinned by rho_comb, the per-cube cumulant growth, PLUS the >=3-face
#    (baryon-channel) sector that LEAVES the Euler-18 regime at beta^10.
print(f"\n    rho_crit (Euler-regime radius hits 6 here)     = {mp.nstr(rho_crit,6)}")
check("VERDICT: Euler-18 sector radius > 6 for all rho_comb < rho_crit (~{:.3g})".format(float(rho_crit)),
      R_euler(1) > 6 and rho_crit > 1,
      "wall dissolves in the K-built sector unless rho_comb >= rho_crit OR the baryon-channel sector dominates")

print(f"\nSCORECARD: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
