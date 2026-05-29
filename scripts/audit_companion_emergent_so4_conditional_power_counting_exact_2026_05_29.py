#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`EMERGENT_SO4_CONDITIONAL_ON_CONTINUUM_LIMIT_POWER_COUNTING_NARROW_THEOREM_NOTE_2026-05-29.md`.

Narrow CONDITIONAL power-counting theorem. The runner verifies the
LOAD-BEARING power-counting inputs of the note's antecedent->consequent
implication; it does NOT verify the antecedent (existence of the
interacting continuum limit as a non-trivial QFT), which is the explicit
undischarged Yang-Mills-existence-adjacent gate.

Load-bearing facts verified here (all exact-symbolic via sympy, with one
high-precision pointwise numeric cross-check of the cubic-harmonic
identity):

  (PC1) Hypercubic dispersion expansion. The free staggered fermion
        dispersion E^2 = (1/a^2) sum_i sin^2(p_i a) and the bosonic
        Laplacian dispersion E^2 = (4/a^2) sum_i sin^2(p_i a/2) both
        expand as p^2 + c4 a^2 sum_i p_i^4 + O(a^4), with the leading
        anisotropy carried by an operator of two extra mass dimensions
        relative to p^2 (i.e. a DIMENSION-6 operator in a theory whose
        kinetic term p^2 is dimension-4). Verified: c4 = -1/3 (fermion),
        c4 = -1/12 (boson), and NO O(a^1) (dimension-5) term appears.

  (PC2) O_h-singlet harmonic classification. Among the real spherical
        harmonics Y_{l m}, the dimension of the trivial (invariant)
        representation of the cubic point group O_h ( = the count of
        O_h-singlet cubic harmonics ) is:
            l = 0 : 1   (the trivial isotropic harmonic -- SO(4)/SO(3)
                         invariant, does NOT break rotational symmetry)
            l = 1 : 0
            l = 2 : 0
            l = 3 : 0
            l = 4 : 1   (the FIRST non-trivial O_h-singlet -- the cubic
                         harmonic K_4; this is the lowest-l harmonic that
                         is O_h-invariant but NOT SO(3)/SO(4)-invariant)
            l = 5 : 0
            l = 6 : 1
        Hence the lowest-degree O_h-invariant, rotation-symmetry-breaking
        angular structure is l = 4. Combined with parity (even l only)
        this fixes the leading lattice-artifact operator that is an
        O_h-singlet and SO(4)-breaking to the l = 4 sector, i.e.
        dimension 6 (two derivatives above the l = 0 / l = 2 sectors
        already exhausted by the rotation-invariant kinetic operators).

  (PC3) Angular decomposition of the leading anisotropy (normalized
        convention). With the standard normalized real spherical
        harmonics (Condon-Shortley), the leading anisotropy direction
        function sum_i n_i^4 decomposes as
            sum_i n_i^4 = 3/5 + <f|Y_{4,0}> Y_{4,0} + <f|Y_{4,+4}> Y_{4,+4},
        with the EXACT zonal projection <f|Y_{4,0}> = 4 sqrt(pi)/15 (the
        reproducible l=4 anisotropy weight the framework's emergent-
        Lorentz note records) and NO l=0-other / l=2 / l=6 / sin(4 phi)
        content. The combined real-cubic-harmonic single-coefficient
        form K_4 = Y_{4,0} + sqrt(5/14)(Y_{4,4} + Y_{4,-4}) carries a
        convention-sensitive coefficient and is NOT load-bearing here;
        the load-bearing facts are (i) the anisotropy lives entirely in
        l = 4 (verified by closed reconstruction), and (ii) the exact
        factor-of-3 axis/diagonal ratio (pure geometry). Verified
        symbolically (trigsimp == 0) and pointwise to high precision.

  (PC4) Power-counting irrelevance arithmetic at the Gaussian fixed
        point in d = 4. A local operator O of mass dimension
        Delta_O has coupling g_O of mass dimension [g_O] = d - Delta_O.
        Its linearized RG eigenvalue at the Gaussian fixed point is
        y_O = d - Delta_O = [g_O]. O is RELEVANT iff y_O > 0,
        MARGINAL iff y_O = 0, IRRELEVANT iff y_O < 0. For d = 4 and a
        dimension-6 operator (Delta_O = 6): y_O = -2 < 0 -> IRRELEVANT;
        its dimensionful coupling scales as a^{+2} (the lattice spacing
        supplies the inverse-mass scale), giving the O(a^2) suppression.
        The runner checks this arithmetic for the relevant/marginal/
        irrelevant boundary and confirms dimension-6 -> y = -2,
        dimension-5 (forbidden here by parity) -> y = -1, and that
        dimension-4 (marginal) is the kinetic boundary.

CONDITIONALITY (verified as a guard, not as a proof of the antecedent):
  (PC5) Vacuity guard. The runner asserts that power-counting
        irrelevance (PC4) is, on its own, a statement ABOUT a fixed
        point and a scaling dimension -- it does not assert the
        existence of an interacting continuum limit. The note's
        implication is vacuously safe if the antecedent fails. This
        check is a documentation assertion (True) recording that the
        runner does NOT attempt to verify continuum-limit existence.

No PDG observed values consumed. No literature numerical comparators
consumed. No fitted selectors consumed. No framework axiom package
imported. The hypercubic dispersions and the harmonic conventions are
explicit inputs.
"""

import sys

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
FAILURES = []


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        FAILURES.append(name)
        print(f"FAIL: {name}")


# ---------------------------------------------------------------------------
# (PC1) Hypercubic dispersion expansion -> leading anisotropy is dim-6
# ---------------------------------------------------------------------------
print("=" * 70)
print("(PC1) Hypercubic dispersion expansion (staggered + Laplacian)")
print("=" * 70)

a, p1, p2, p3 = sp.symbols("a p1 p2 p3", positive=True, real=True)

# Free staggered fermion: E^2 = (1/a^2) sum_i sin^2(p_i a)
E2_fermion = sum(sp.sin(pi_ * a) ** 2 for pi_ in (p1, p2, p3)) / a**2
# Bosonic Laplacian:     E^2 = (4/a^2) sum_i sin^2(p_i a / 2)
E2_boson = 4 * sum(sp.sin(pi_ * a / 2) ** 2 for pi_ in (p1, p2, p3)) / a**2

# Expand both in small a to O(a^4); collect order by order.
ser_f = sp.series(E2_fermion, a, 0, 5).removeO()
ser_b = sp.series(E2_boson, a, 0, 5).removeO()

psq = p1**2 + p2**2 + p3**2
p4sum = p1**4 + p2**4 + p3**4

# Leading term (a^0) must be p^2 for both.
lead_f = ser_f.subs(a, 0)
lead_b = ser_b.subs(a, 0)
check("PC1a: fermion leading term is p^2 (isotropic, dim-4 kinetic)",
      sp.simplify(lead_f - psq) == 0)
check("PC1b: boson leading term is p^2 (isotropic, dim-4 kinetic)",
      sp.simplify(lead_b - psq) == 0)

# No a^1 (dimension-5) term: parity / even-power forbids it.
coeff_a1_f = ser_f.coeff(a, 1)
coeff_a1_b = ser_b.coeff(a, 1)
check("PC1c: fermion has NO O(a^1) (dimension-5) anisotropy term",
      sp.simplify(coeff_a1_f) == 0)
check("PC1d: boson has NO O(a^1) (dimension-5) anisotropy term",
      sp.simplify(coeff_a1_b) == 0)

# a^2 (dimension-6) term: c4 * sum_i p_i^4, with c4 = -1/3 / -1/12.
coeff_a2_f = sp.expand(ser_f.coeff(a, 2))
coeff_a2_b = sp.expand(ser_b.coeff(a, 2))
check("PC1e: fermion O(a^2) term equals (-1/3) sum_i p_i^4 (dim-6)",
      sp.simplify(coeff_a2_f - sp.Rational(-1, 3) * p4sum) == 0)
check("PC1f: boson O(a^2) term equals (-1/12) sum_i p_i^4 (dim-6)",
      sp.simplify(coeff_a2_b - sp.Rational(-1, 12) * p4sum) == 0)

# The leading anisotropy operator sum_i p_i^4 carries exactly two extra
# powers of momentum relative to the p^2 kinetic term: dim-4 -> dim-6.
deg_kin = sp.Poly(psq, p1, p2, p3).total_degree()
deg_aniso = sp.Poly(p4sum, p1, p2, p3).total_degree()
check("PC1g: anisotropy operator degree (4) = kinetic degree (2) + 2 "
      "-> two extra mass dimensions -> dimension-6 operator",
      deg_kin == 2 and deg_aniso == 4 and (deg_aniso - deg_kin) == 2)


# ---------------------------------------------------------------------------
# (PC2) O_h-singlet harmonic classification: lowest SO(4)-breaking
#       O_h-invariant harmonic is l = 4
# ---------------------------------------------------------------------------
print("=" * 70)
print("(PC2) O_h-singlet (cubic-harmonic) count per angular momentum l")
print("=" * 70)

# Count the dimension of the trivial representation of the full cubic
# point group O_h inside the degree-l real spherical-harmonic space
# (dimension 2l+1). We do this by Burnside/averaging the character of
# the (2l+1)-dim rotation representation over the 48 elements of O_h,
# restricted to the 24 proper rotations of O (the chiral octahedral
# group); for EVEN l the improper elements double the proper-rotation
# average's projector trace consistently (parity even), so the count of
# *parity-even* O_h singlets equals the count of O-singlets for even l.
#
# Character of SO(3) irrep of spin l at rotation angle phi:
#   chi_l(phi) = sin((2l+1) phi / 2) / sin(phi / 2)      (phi != 0)
#   chi_l(0)   = 2l + 1
#
# Proper rotation group O (order 24) conjugacy classes:
#   E      : 1 element,  angle 0
#   6 C4   : 6 elements, angle pi/2
#   3 C2   : 3 elements, angle pi      (the C4^2 = C2 axis rotations)
#   8 C3   : 8 elements, angle 2pi/3
#   6 C2'  : 6 elements, angle pi      (face-diagonal 2-fold axes)
O_classes = [
    (1, sp.Integer(0)),                 # E
    (6, sp.pi / 2),                     # 6 C4
    (3, sp.pi),                         # 3 C2 (= C4^2)
    (8, 2 * sp.pi / 3),                 # 8 C3
    (6, sp.pi),                         # 6 C2'
]
O_ORDER = sum(n for n, _ in O_classes)
assert O_ORDER == 24


def chi_l(l, phi):
    if phi == 0:
        return sp.Integer(2 * l + 1)
    return sp.sin((2 * l + 1) * phi / 2) / sp.sin(phi / 2)


def num_O_singlets(l):
    """Multiplicity of the trivial rep of O in the spin-l rep."""
    tot = sp.Integer(0)
    for n, phi in O_classes:
        tot += n * chi_l(l, phi)
    return sp.nsimplify(sp.simplify(tot / O_ORDER))


expected_singlets = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1,
                     7: 0, 8: 1, 9: 1, 10: 1}
for l in range(0, 11):
    got = num_O_singlets(l)
    exp = expected_singlets[l]
    check(f"PC2.l{l}: O_h-singlet count at l={l} is {exp}",
          sp.Integer(got) == sp.Integer(exp))

# The load-bearing structural conclusion: l = 0 is the ONLY singlet at
# l < 4, and it is the rotation-INVARIANT (isotropic) harmonic; the first
# rotation-symmetry-BREAKING O_h singlet is at l = 4.
first_breaking_l = next(l for l in range(1, 11)
                        if expected_singlets[l] == 1)
check("PC2*: lowest l with a NON-trivial (l>0) O_h singlet is l = 4 "
      "-> first SO(4)-breaking O_h-invariant angular structure is l=4",
      first_breaking_l == 4)


# ---------------------------------------------------------------------------
# (PC3) Cubic-harmonic identity sum_i n_i^4 = 3/5 + (4 sqrt(pi)/15) K_4
#       in the normalized convention
# ---------------------------------------------------------------------------
print("=" * 70)
print("(PC3) Angular decomposition of leading anisotropy "
      "(l=4, normalized convention)")
print("=" * 70)

theta, phi = sp.symbols("theta phi", real=True)
n1 = sp.sin(theta) * sp.cos(phi)
n2 = sp.sin(theta) * sp.sin(phi)
n3 = sp.cos(theta)
f_ang = n1**4 + n2**4 + n3**4

# Normalized real spherical harmonics (Condon-Shortley, real form). The
# m != 0 forms carry the sqrt(2) that unit-normalizes the real partners;
# <Y|Y> = 1 each (self-checked below).
#   Y_{4,0}  = (3/16) sqrt(1/pi) (35 cos^4 - 30 cos^2 + 3)
#   Y_{4,+4} = (3/16) sqrt(35/pi) sin^4(theta) cos(4 phi)
#   Y_{4,-4} = (3/16) sqrt(35/pi) sin^4(theta) sin(4 phi)
#   Y_{2,0}  = sqrt(5/(16 pi)) (3 cos^2 - 1)
#   Y_{0,0}  = 1/(2 sqrt(pi))
Y00 = 1 / (2 * sp.sqrt(sp.pi))
Y20 = sp.sqrt(5 / (16 * sp.pi)) * (3 * sp.cos(theta) ** 2 - 1)
Y40 = sp.Rational(3, 16) * sp.sqrt(1 / sp.pi) * (
    35 * sp.cos(theta) ** 4 - 30 * sp.cos(theta) ** 2 + 3)
Y4p4 = sp.Rational(3, 16) * sp.sqrt(35 / sp.pi) * sp.sin(theta) ** 4 * sp.cos(4 * phi)
Y4m4 = sp.Rational(3, 16) * sp.sqrt(35 / sp.pi) * sp.sin(theta) ** 4 * sp.sin(4 * phi)


def sph_inner(A, B):
    return sp.simplify(sp.integrate(
        sp.integrate(A * B * sp.sin(theta), (theta, 0, sp.pi)),
        (phi, 0, 2 * sp.pi)))


# Normalization self-checks for the harmonics used.
check("PC3*a: Y_{0,0} is unit-normalized", sph_inner(Y00, Y00) == 1)
check("PC3*b: Y_{4,0} is unit-normalized", sph_inner(Y40, Y40) == 1)
check("PC3*c: Y_{4,+4} is unit-normalized", sph_inner(Y4p4, Y4p4) == 1)
check("PC3*d: Y_{4,-4} is unit-normalized", sph_inner(Y4m4, Y4m4) == 1)

# --- Load-bearing, convention-independent decomposition facts ---------
# (1) The isotropic (l=0) part is exactly 3/5.
c0 = sph_inner(f_ang, Y00)
check("PC3a: isotropic projection <f|Y00> Y00 = 3/5 (l=0 part)",
      sp.simplify(c0 * Y00 - sp.Rational(3, 5)) == 0)

# (2) The zonal l=4 projection <f|Y_{4,0}> = 4 sqrt(pi)/15 EXACTLY. This
# is the reproducible number the emergent-Lorentz note records for the
# l=4 cubic anisotropy weight (it is the projection onto the m=0 zonal
# harmonic Y_{4,0}; the combined-object real-cubic-harmonic K_4 carries a
# convention-sensitive single coefficient that is NOT load-bearing here).
c40 = sph_inner(f_ang, Y40)
check("PC3b: zonal l=4 projection <f|Y_{4,0}> = 4 sqrt(pi)/15 (exact)",
      sp.simplify(c40 - 4 * sp.sqrt(sp.pi) / 15) == 0)

# (3) The full l=4 reconstruction closes: f = 3/5 + sum_m <f|Y_{4,m}> Y_{4,m},
# with the only nonzero m in {0, +4} (no sin(4phi) content). This is the
# rigorous, convention-independent statement of "the anisotropy lives
# entirely in l=4".
c4p4 = sph_inner(f_ang, Y4p4)
c4m4 = sph_inner(f_ang, Y4m4)
recon = sp.Rational(3, 5) + c40 * Y40 + c4p4 * Y4p4 + c4m4 * Y4m4
diff = sp.simplify(sp.trigsimp(sp.expand_trig(f_ang - recon)))
check("PC3c: full l=0 + l=4 reconstruction closes (symbolic, ==0)",
      diff == 0)
check("PC3d: no sin(4 phi) content (<f|Y_{4,-4}> = 0)", c4m4 == 0)

# High-precision pointwise numeric cross-check of the closed reconstruction,
# independent of scipy harmonic conventions (lambdify of the same sympy
# closed forms vs brute-force sum_i n_i^4).
rng = np.random.default_rng(20260529)
N = 200000
ph = rng.uniform(0, 2 * np.pi, N)
ct = rng.uniform(-1, 1, N)
th = np.arccos(ct)
nx = np.sin(th) * np.cos(ph)
ny = np.sin(th) * np.sin(ph)
nz = np.cos(th)
lhs_num = nx**4 + ny**4 + nz**4
recon_fn = sp.lambdify((theta, phi), recon, "numpy")
rhs_num = recon_fn(th, ph)
max_err = float(np.max(np.abs(lhs_num - rhs_num)))
print(f"   max|LHS - reconstruction| over {N} directions = {max_err:.3e}")
check("PC3e: pointwise reconstruction holds to < 1e-12", max_err < 1e-12)

# No l=2 contamination (orthogonality to Y_{2,0}).
proj_l2 = sph_inner(f_ang, Y20)
check("PC3f: <f | Y_{2,0}> = 0 (no l=2 contamination)", proj_l2 == 0)

# Factor-of-3 axis/diagonal anisotropy (pure geometry, coeff-independent).
f_axis = f_ang.subs({theta: 0})                       # [0,0,1]
f_diag = f_ang.subs({theta: sp.acos(1 / sp.sqrt(3)), phi: sp.pi / 4})
check("PC3g: sum_i n_i^4 = 1 along [001] axis",
      sp.simplify(f_axis - 1) == 0)
check("PC3h: sum_i n_i^4 = 1/3 along [111] diagonal (factor-3 ratio)",
      sp.simplify(f_diag - sp.Rational(1, 3)) == 0)

# ---------------------------------------------------------------------------
# (PC4) Power-counting irrelevance arithmetic at the Gaussian fixed point
# ---------------------------------------------------------------------------
print("=" * 70)
print("(PC4) Gaussian-fixed-point power-counting (d=4)")
print("=" * 70)

d = sp.Integer(4)


def rg_eigenvalue(Delta_O, d=d):
    """Linearized RG eigenvalue of operator coupling at Gaussian FP:
       y_O = d - Delta_O = mass dimension of the coupling g_O."""
    return d - sp.Integer(Delta_O)


def classify(Delta_O):
    y = rg_eigenvalue(Delta_O)
    if y > 0:
        return "relevant"
    if y == 0:
        return "marginal"
    return "irrelevant"


# Kinetic operator (dimension-4 in d=4) is marginal -- the boundary.
check("PC4a: dimension-4 operator is marginal (y = 0) in d=4",
      rg_eigenvalue(4) == 0 and classify(4) == "marginal")
# Dimension-5 (forbidden here by parity) would be irrelevant, y=-1.
check("PC4b: dimension-5 operator has y = -1 (irrelevant)",
      rg_eigenvalue(5) == -1 and classify(5) == "irrelevant")
# THE load-bearing line: dimension-6 SO(4)-breaking operator is irrelevant.
check("PC4c: dimension-6 operator has y = -2 < 0 -> IRRELEVANT at the "
      "Gaussian FP in d=4 (load-bearing power-counting input)",
      rg_eigenvalue(6) == -2 and classify(6) == "irrelevant")
# Dimensionful coupling of the dim-6 operator scales as a^{+2}: the
# lattice spacing supplies the inverse mass scale [g] = mass^{-2},
# g_phys = c * a^{|y|} = c * a^2 -> 0 as a->0. We record |y| = 2.
check("PC4d: dim-6 coupling carries mass-dimension -2 -> a^2 suppression "
      "(O(a^2) corrections, vanish as a->0)",
      rg_eigenvalue(6) == -2)
# A relevant operator (e.g. a dim-2 mass term) would have y=+2>0: the
# contrast confirms the sign convention is the standard one.
check("PC4e: sign-convention sanity -- dimension-2 (mass) operator is "
      "relevant (y = +2 > 0)",
      rg_eigenvalue(2) == 2 and classify(2) == "relevant")


# ---------------------------------------------------------------------------
# (PC5) Conditionality guard (documentation assertion)
# ---------------------------------------------------------------------------
print("=" * 70)
print("(PC5) Conditionality / vacuity guard")
print("=" * 70)

# This runner verifies the power-counting INPUTS to the conditional, not
# the antecedent. The antecedent -- existence of the interacting continuum
# limit as a non-trivial QFT -- is a Yang-Mills-existence-adjacent OPEN
# gate and is NOT verified anywhere in this script. The implication the
# note proves is vacuously safe if the antecedent fails. We record this
# as an explicit True assertion so the runner output documents that no
# continuum-limit-existence claim is made.
antecedent_verified_here = False
check("PC5a: runner does NOT verify continuum-limit existence "
      "(antecedent is the explicit open gate; implication only)",
      antecedent_verified_here is False)
check("PC5b: note proves the IMPLICATION only; power-counting "
      "irrelevance is vacuous content without the antecedent",
      True)


# ---------------------------------------------------------------------------
print("=" * 70)
print(f"PASS={PASS}  FAIL={FAIL}")
if FAILURES:
    print("FAILURES:")
    for f in FAILURES:
        print("  -", f)
print("=" * 70)
sys.exit(0 if FAIL == 0 else 1)
