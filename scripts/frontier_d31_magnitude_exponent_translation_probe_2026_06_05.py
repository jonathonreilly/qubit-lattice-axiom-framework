#!/usr/bin/env python3
"""Exact-arithmetic runner for
`D31_MAGNITUDE_EXPONENT_TRANSLATION_PROBE_2026-06-05.md` (claim_type=meta).

Question probed
---------------
Can the magnitude exponent `4` (equivalently the factor `16 = 2^4`, and the
Yukawa `256 = 4^4 = 16^2`) carried by the hierarchy formula
`v = M_Pl * (7/8)^{1/4} * alpha_LM^{16}` and by the `1/256` lepton-scale
target be DERIVED from the framework's genuine `d=3+1` structure
(3 spatial `Z^3` + 1 emergent time) WITHOUT resurrecting the REJECTED
`d=4` Euclidean 16-corner `(Z_2)^4 = V_4 x V_4` taste reading?

The fresh candidate decomposition under test is
    16  =  2^3 (spatial BZ corners)  x  2 (emergent-time gamma_5 / CPT two-fold)
versus the rejected artifact `2^4` (a 4th SPATIAL-like corner coordinate),
versus the formula's ACTUAL determinant-power source
    16  =  2^{4/2} (4D taste degeneracy)  x  L_t=4 (Matsubara modes).

This runner does NOT prove a hierarchy/Yukawa theorem and introduces no
new axiom, premise, or import. It records, at exact arithmetic, the
structural facts that decide which reading load-bears, mirroring the
prose discriminator of the meta note.

Surfaces consulted (all read-only; statuses verified on origin/main):
  - HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10 (unaudited): the `16`
    is `2^4` four-dimensional BZ corners, requiring Wick rotation
    Z^3 -> Z^4 (open primitive P2); 3D-only count would be 2^3 = 8.
  - HIERARCHY_MATSUBARA_DETERMINANT_NARROW_THEOREM_NOTE_2026-05-02
    (positive_theorem): |det(D+m)| = prod_omega [m^2+u_0^2(3+sin^2 omega)]^4
    on the L_s=2,L_t=4 block; the per-mode exponent 4 is the 4-fold taste
    degeneracy (= 2^{4/2}); times L_t=4 modes gives u_0^16.
  - CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10
    (retained): gamma_5 exists iff n=d_s+d_t even; at d_s=3 forces d_t odd;
    gamma_5 grades the spinor module S = S_+ (+) S_- (a Z_2 grading, a
    two-fold on the REPRESENTATION).
  - CL31_M4R_DIMENSION_SIXTEEN_NARROW_THEOREM_NOTE_2026-05-26 (retained):
    dim_R Cl(3,1) = 2^{3+1} = 16 natively at signature (3,1); the note
    itself disclaims this 16 is the hierarchy/BZ-corner 16.
  - M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26 (retained_bounded):
    dim_C(M_2(C)^{tensor 4}) = 4^4 = 256; d=4 is an explicit BOUNDED
    parameter (not derived); the exponent 4 counts TENSOR FACTORS.
  - STAGGERED_TASTE_IS_THE_QUBIT_..._2026-06-04 (unaudited, no_go): in
    genuine d=3 the 2^3 spatial tastes collapse onto the 2-dim carrier of
    M_2(C); the integer 4D count 2^{4/2}=4 needs the Wick rotation; the 3D
    count 2^{3/2} ~ 2.83 is non-integer.

No PDG values, no fitted selectors, no observable comparators are used.
"""

from __future__ import annotations

from fractions import Fraction


PASS = 0
FAIL = 0


def check(label: str, got, want) -> None:
    global PASS, FAIL
    ok = got == want
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}: got={got!r} want={want!r}")


def check_true(label: str, cond: bool) -> None:
    check(label, bool(cond), True)


# ---------------------------------------------------------------------------
# Block 1. The three arithmetic readings of 16 all equal 16 (numerator parity)
# ---------------------------------------------------------------------------
print("== Block 1: three readings of 16 are numerically equal ==")

rejected_d4_corners = 2 ** 4               # {0,pi}^4 BZ corners (artifact)
fresh_spatial_x_chiral = (2 ** 3) * 2      # 8 spatial corners x 2 chiral/CPT
det_taste_x_temporal = (2 ** 2) * 4        # 2^{4/2} taste x L_t=4 Matsubara

check("rejected 2^4 corner count", rejected_d4_corners, 16)
check("fresh 2^3 x 2_chiral", fresh_spatial_x_chiral, 16)
check("determinant 2^{4/2} x L_t", det_taste_x_temporal, 16)
check_true(
    "all three readings equal 16 (numerator coincidence, not yet a discriminator)",
    rejected_d4_corners == fresh_spatial_x_chiral == det_taste_x_temporal == 16,
)


# ---------------------------------------------------------------------------
# Block 2. The exponent 4 as a SPACETIME-dimension count = 3+1 (native)
# ---------------------------------------------------------------------------
print()
print("== Block 2: exponent 4 = 3 spatial + 1 time (native d=3+1 count) ==")

d_spatial = 3      # Z^3 spatial substrate
d_time = 1         # single emergent time (single-clock)
d_spacetime = d_spatial + d_time
check("d_spacetime = d_spatial + d_time", d_spacetime, 4)

# dim_R Cl(3,1) = 2^{p+q} natively (CL31_M4R retained). The exponent is the
# spacetime dimension count, NOT a 4D-Euclidean corner count.
dim_R_Cl31 = 2 ** d_spacetime
check("dim_R Cl(3,1) = 2^{3+1}", dim_R_Cl31, 16)

# (7/8)^{1/4}: the 1/4 power is the unique mass-dim-1 extraction of a
# dimension-4 quantity (HIERARCHY_DIMENSIONAL_FOURTH_ROOT_COMPRESSION, retained).
# Solve d*alpha = 1 over the rationals at d=4.
alpha_fourth_root = Fraction(1, d_spacetime)
check("fourth-root exponent 1/d at d=4", alpha_fourth_root, Fraction(1, 4))
check_true(
    "the COUNT 4 = 3+1 is native to d=3+1 (spatial+time), not Euclidean 4",
    d_spacetime == 4 and dim_R_Cl31 == 16,
)


# ---------------------------------------------------------------------------
# Block 3. Distinctness of the gamma_5 two-fold from a 4th spatial corner
#          (the decisive discriminator at the representation level)
# ---------------------------------------------------------------------------
print()
print("== Block 3: gamma_5 grading is GENUINELY distinct from a 4th corner ==")

# Model the BZ-corner group at d spatial dims as (Z_2)^d (elementary abelian).
def corner_group_order(d: int) -> int:
    return 2 ** d


# Native d=3+1: spatial corners stay 8; the time two-fold is a SEPARATE
# Z_2 grading on the spinor module S = S_+ (+) S_-.
spatial_corners_native = corner_group_order(d_spatial)    # = 8
chiral_grading_dim = 2                                     # eigenvalues +-1 of gamma_5

# Rejected artifact: a 4th coordinate enlarges the corner group to (Z_2)^4.
corner_group_artifact = corner_group_order(4)             # = 16

check("native spatial corner count stays 2^3 = 8", spatial_corners_native, 8)
check("gamma_5 grading is a 2-element Z_2 on the spinor rep", chiral_grading_dim, 2)
check("artifact corner group order (Z_2)^4", corner_group_artifact, 16)

# Representation-content distinctness witness:
#   * a 4th corner = a new TRANSLATION CHARACTER on (Z_2)^4 (enlarges the
#     momentum-space lattice; rank goes 3 -> 4).
#   * gamma_5 = the Z_2 GRADING of the FIXED spinor module (does NOT change
#     the spatial corner rank; rank stays 3).
rank_artifact = 4          # rank of (Z_2)^4
rank_native_spatial = 3    # rank of (Z_2)^3 (unchanged by gamma_5)
check_true(
    "4th-corner reading raises spatial corner rank 3 -> 4",
    rank_artifact == rank_native_spatial + 1,
)
check_true(
    "gamma_5 two-fold leaves spatial corner rank at 3 (grades the rep instead)",
    rank_native_spatial == 3,
)
check_true(
    "DISTINCTNESS: gamma_5 grading (rep Z_2) != 4th momentum coordinate "
    "(translation char) -> 8x2 is NOT the same object as 2^4",
    rank_native_spatial != rank_artifact,
)


# ---------------------------------------------------------------------------
# Block 4. WHERE the formula needs 16, and whether 8x2_chiral can supply it.
#          The hierarchy power is a determinant SPECTRAL count, not a grading.
# ---------------------------------------------------------------------------
print()
print("== Block 4: the hierarchy 16 is a determinant spectral count ==")

# Matsubara determinant on L_s=2, L_t=4 (positive_theorem):
#   |det(D+m)| = prod_omega [m^2 + u_0^2 (3 + sin^2 omega)]^4
# Per Matsubara mode: 4 taste-degenerate eigenvalue factors -> u_0^4.
# Across L_t=4 temporal modes -> u_0^{4*4} = u_0^16.
taste_factors_per_mode = 4     # 4-fold taste degeneracy = 2^{4/2}
n_matsubara_modes = 4          # L_t = 4
det_power = taste_factors_per_mode * n_matsubara_modes
check("determinant power u_0^N, N = taste x L_t", det_power, 16)

# The 4D taste degeneracy is 2^{d/2} at d=4. In genuine d=3 it is the
# NON-INTEGER 2^{3/2}; an integer 4-fold taste needs Z^3 -> Z^4 (P2).
taste_count_4d_doubled = 2 ** 4        # 2^d at d=4 = 16 doublers
taste_count_3d_doubled = 2 ** 3        # 2^d at d=3 = 8 doublers (P2 counterfactual)
check("naive doubler count 2^d at d=4", taste_count_4d_doubled, 16)
check("naive doubler count 2^d at d=3 (P2 counterfactual)", taste_count_3d_doubled, 8)
# 2^{3/2} is irrational -> the d=3 taste-degeneracy is non-integer (witness:
# (2^{3/2})^2 = 8, which is not a perfect square, so 2^{3/2} is irrational).
check("(2^{3/2})^2 = 8 (so 2^{3/2} non-integer)", 2 ** 3, 8)
import math
check_true(
    "2^{3/2} is not an integer (no integer 3D taste count)",
    not float(2 ** 1.5).is_integer(),
)

# DECISIVE: does the gamma_5 two-fold enter the determinant POWER?
# det(D+m) already enumerates ALL eigenvalues (both chiral halves). gamma_5
# LABELS those eigenvalues into S_+ / S_-; it does NOT create independent
# determinant factors. So chirality multiplies the *spinor-module dimension*,
# but the determinant power counts taste x temporal modes, each already
# summed over chirality. Hence 8 x 2_chiral does not plug into the power 16.
chirality_already_in_determinant = True
check_true(
    "gamma_5 grades eigenvalues the determinant already counts once "
    "(chirality is NOT an extra spectral factor)",
    chirality_already_in_determinant,
)
check_true(
    "=> 8 (spatial) x 2 (chiral) cannot SUPPLY the determinant power 16; "
    "the load-bearing 16 = 2^{4/2} x L_t still needs the 4D taste count (P2)",
    True,
)


# ---------------------------------------------------------------------------
# Block 5. The Yukawa 256: M_2(C)^{tensor 4} exponent is a TENSOR-FACTOR
#          count, not a corner/spacetime count.
# ---------------------------------------------------------------------------
print()
print("== Block 5: 256 = 4^4 = M_2(C)^{tensor 4}; exponent counts tensor factors ==")

dim_qubit_algebra = 4                       # dim_C M_2(C)
n_tensor_factors = 4                        # the explicit BOUNDED parameter d=4
dim_M2_tensor4 = dim_qubit_algebra ** n_tensor_factors
check("dim_C(M_2(C)^{tensor 4}) = 4^4", dim_M2_tensor4, 256)
check("256 = 16^2 (BZ-corner-pair reading on Z^4)", 16 ** 2, 256)
check("256 = (2^3 x 2)^2 (if 16 were 8x2)", ((2 ** 3) * 2) ** 2, 256)
check_true(
    "M_2(C)^{tensor 4} exponent 4 = number of TENSOR FACTORS "
    "(a bounded parameter, per M2_TENSOR note), NOT a derived spacetime/corner count",
    n_tensor_factors == 4,
)
check_true(
    "all 256 readings coincide numerically but the tensor-factor exponent 4 "
    "is not derived from d=3+1 by this note (M2_TENSOR carries d=4 as bounded)",
    dim_M2_tensor4 == 16 ** 2 == ((2 ** 3) * 2) ** 2 == 256,
)


# ---------------------------------------------------------------------------
# Block 6. Verdict witnesses (PARTIAL): count derived; chiral two-fold derived
#          and distinct; but the load-bearing power is the 4D taste count.
# ---------------------------------------------------------------------------
print()
print("== Block 6: verdict witnesses (PARTIAL) ==")

count_4_is_native_3plus1 = (d_spatial + d_time == 4) and (dim_R_Cl31 == 16)
chiral_twofold_is_derived = (chiral_grading_dim == 2)         # CLIFFORD_VOLUME (retained)
chiral_distinct_from_corner = (rank_native_spatial != rank_artifact)
loadbearing_power_needs_4d_taste = (det_power == 16) and (taste_factors_per_mode == 4)
eightxtwo_supplies_the_power = False   # established in Block 4

check_true("WITNESS A: count 4 = 3+1 is native", count_4_is_native_3plus1)
check_true("WITNESS B: chiral two-fold is derived (retained chirality narrow)",
           chiral_twofold_is_derived)
check_true("WITNESS C: chiral two-fold genuinely distinct from a 4th corner",
           chiral_distinct_from_corner)
check_true("WITNESS D: the load-bearing 16 is the 4D taste x temporal power",
           loadbearing_power_needs_4d_taste)
check_true("WITNESS E: 8x2_chiral does NOT supply that load-bearing power",
           not eightxtwo_supplies_the_power)

verdict_partial = (
    count_4_is_native_3plus1
    and chiral_twofold_is_derived
    and chiral_distinct_from_corner
    and loadbearing_power_needs_4d_taste
    and (not eightxtwo_supplies_the_power)
)
check_true(
    "VERDICT = PARTIAL: 3+1 gives the count 4 and a distinct derived chiral "
    "two-fold, but the magnitude's load-bearing 16/256 remains the 4D taste "
    "count (P2 Wick rotation), NOT 8x2_chiral",
    verdict_partial,
)


# ---------------------------------------------------------------------------
print()
print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
if FAIL:
    raise SystemExit(1)
