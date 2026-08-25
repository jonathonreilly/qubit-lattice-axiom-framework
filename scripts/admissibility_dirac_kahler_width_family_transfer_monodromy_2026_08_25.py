#!/usr/bin/env python3
"""BLOCK 190 -- THE WIDTH FAMILY, ITS TRANSFER LOCALITY, AND THE UNIT-CELL
MONODROMY.

THE RESULT, AND ITS EXACT SCOPE.  On a DISCLOSED VARIANT of Block 188's site
construction -- the SAME staggered Dirac-Kahler carrier on Z_T x Z_4 at the
SAME fixture (m, c) = (9/20, 5/13), but with the antiperiodic temporal sign
carried on the WRAP EDGE t = T-1 instead of at t = 3 -- the naive OS transfer
pairing is REFUTED with exact core witnesses, the step operator V = K_c^-1 L_1
is measured to be a LOCAL object (width-invariant, parity-rigid, with a
finite-range boundary layer at BOTH seams), and the primitive UNIT-CELL
MONODROMY W = K_c^-1 L_2 is computed exactly and PROVEN spectrally positive.
ALL OF IT IS FINITE EXACT LINEAR ALGEBRA ON ONE CONSTRUCTED MATRIX FAMILY.
NONE OF IT IS GRAVITY, AND THE WORDS DISPERSION, MASS SCALE, PHYSICAL TIME STEP
AND TRANSFER POSITIVITY ARE FENCED AS READINGS THROUGHOUT.

  0. THE CONSTRUCTION CONTROL COMES FIRST, AND IT IS TWO-SIDED (C).  FIRST, the
     HODGE: the ONLY object imported from the landed chain is Block 105's
     shear_hodge() through the Block 128 module, and its value at (c, v) =
     (5/13, 1) is DISPLAYED INLINE IN THE NOTE ENTRYWISE as I + (25/144)(E11 +
     E22) - (65/144)(E12 + E21) -- gated here against the import at ZERO
     entrywise residual, so the note's displayed matrix and the landed function
     are measured to be the same sixteen numbers.  SECOND, the SIGN LAYER: the
     wrap-edge convention is a VARIANT and the fork is gated AS A PAIR OF
     NUMBERS.  At T = 8 the LANDED placement w(3) gives nnz(Q - Q^T) = 144 --
     BLOCK 188'S OWN LANDED NUMBER -- and reproduces THEIR landed core minors
     DIGIT-FOR-DIGIT; the wrap placement w(T-1) gives 160 and a DIFFERENT first
     minor.  BOTH are Ps-covariant at ZERO.  THE VARIANT IS NOT THE LANDED
     OBJECT AND THIS RUNNER MEASURES THE DIFFERENCE RATHER THAN ASSERTING THE
     SAMENESS.  AND THE HODGE FORK IS RESOLVED ON BOTH SIDES, WHICH SETTLES THE
     ADVERSARIAL CHECK'S C3/C6/C8: the check's FORENSIC variant block gives the
     IDENTICAL spectra at every bulk core -- which is why it reproduced every
     headline coefficient -- while the Block 105 note's own displayed block is
     measured here to be THE SAME LANDED FUNCTION AT VOLUME 12/13, and at that
     volume the spectra MOVE.  The discrepancy was a VOLUME CONVENTION and
     never a disputed measurement, and both of the check's failing rebuilds are
     reproduced here DIGIT-FOR-DIGIT.

  1. THE NAIVE TRANSFER PAIRING IS REFUTED ON THE CORES, AND THE CHECK'S C2
     CORRECTION IS CARRIED AS CONTENT (D).  At T = 12 the one-step and two-step
     core pairings L_1 and L_2 are ASYMMETRIC at every bulk core t0 = 1, 2, 3,
     with the exact census (48, 40), (48, 40), (48, 48) and SIX EXACT WITNESSES
     recorded entry by entry.  The GLOBAL mechanism is [tau^k, G] != 0,
     measured at T = 8 in BOTH sign layers.  BUT THE ADVERSARIAL CHECK'S
     CORRECTION IS TAKEN: global commutator nonvanishing is NOT by itself a
     proof that a RESTRICTED core pairing is asymmetric -- symmetry after
     restriction needs only the PROJECTED block to vanish.  THE SIX CORE
     WITNESSES ARE THE PROOF, and the mechanism is stated as a mechanism and
     not as a derivation.

  2. THE STEP OPERATOR IS LOCAL, AND LOCALITY IS A MATRIX STATEMENT (E).  V2 at
     T = 12, V2 at T = 16 and V4 at T = 16 are EQUAL ENTRYWISE at ZERO
     residual, and so are V1 at T = 12 and V1 at T = 16 -- the step DYNAMICS is
     both width-invariant and position-homogeneous.  THE GRAM IS NOT: K_c(2)
     and K_c(4) at T = 16 differ at EXACTLY 56 ENTRIES.  The boundary layer
     lives in the metric data and in one quartic, never in the even step
     matrix.

  3. THE BOUNDARY LAYER HAS TWO SEAMS AND THE SECOND ONE IS THIS BLOCK'S OWN
     FINDING (E).  Every probed core factors (2, 2, 4) over Q.  The even
     quadratics and the odd quadratics are position- and width-invariant
     throughout.  The odd quartic carries a NEAR-seam value at t0 = 1 locked
     across all three widths, its exact coefficient MIRROR at t0 = half - 3,
     and a DEEP value at t0 = 3 (T = 16) and t0 = 3, 5 (T = 20).  AND THE EVEN
     QUARTIC IS NOT RIGID EVERYWHERE, WHICH IS A CORRECTION TO THE SOLVE'S OWN
     WORDING: at the FAR-seam core t0 = half - 2 it takes a DIFFERENT value,
     (47667825, 63213480, 101294706, -55889280, 39529825), and that value is
     itself LOCKED across T = 12, 16 and 20.  The even sector is rigid in the
     INTERIOR and has its own one-core far-seam layer.

  4. THE MIRROR COVARIANCE IS EXACT (E).  At T = 12 (V1 against V3) and at
     T = 16 (V1 against V5) the primitive degree-8 coefficient vectors satisfy
     q_j = (-1)^j p_(8-j) for all nine j at ZERO residual, which is exactly
     q(z) proportional to z^8 p(-1/z) and therefore spec(V_mirror) =
     {-1/lambda} with multiplicity.

  5. THE UNIT-CELL MONODROMY IS PRIMITIVE, PARITY-INDEPENDENT AND POSITIVE (F).
     W != V^2 at EXACTLY 32 entries at every T = 20 deep core t0 = 3, 4, 5,
     with exact witnesses; charpoly(W) is IDENTICAL at all three, (22569375 z^2
     - 233631106 z + 22569375)^2 (39529825 z^2 - 109432706 z + 39529825)^2.
     POSITIVITY IS PROVEN AND NOT ESTIMATED: both discriminants are exact
     positive integers with their prime factorizations gated, both traces
     exceed twice the leading coefficient, both constant/leading ratios are 1
     so the roots are reciprocal, and the two trace ratios are DISTINCT because
     233631106*39529825 - 109432706*22569375 = 6765568955757700 != 0.  Four
     distinct real positive roots in two reciprocal pairs.  AND THE COEFFICIENT
     IDENTITY IS EXACT: the second monodromy quadratic is a z^2 - c z + a built
     from the even V-quartic's (a, b, c), with the odd coefficient b DROPPING
     OUT.

  6. THE COMMUTANT IS COMPUTED EXHAUSTIVELY, NOT GUESSED (G).  U (the two-site
     shift) is a Gram isometry AND commutes with W, and it GRADES the spectrum:
     U = +1 carries both copies of the 39529825 pair and U = -1 both copies of
     the 22569375 pair, with the off-sector block EXACTLY zero.  S (the
     ONE-site shift) also commutes with W, with S^2 = U and S^4 = I, but is NOT
     a Gram isometry -- a 64-entry defect with an exact witness, which is the
     check's own P2 finding rebuilt here.  Its momentum blocks give p = 0 and p
     = 2 the SAME polynomial, and THAT EQUALITY IS NOT FORCED BY THE GROUP: it
     is gated as an ADDITIONAL exact isospectrality.  THE CENSUS IS EXHAUSTIVE
     AND MEASURED IN THIS RUNNER RATHER THAN CITED: all 2048 signed monomial
     candidates are swept and the W-commutants are EXACTLY {I, S, U, S^3} with
     EXACTLY {I, U} among them Gram isometries.  AND THE P1 FORK IS RESOLVED
     THE OTHER WAY, WHICH IS THIS BLOCK'S SECOND CORRECTION TO THE CHECK: K_c
     is EXACTLY SYMMETRIC at the deep core, so the K-ONLY transposition is a
     measured NO-OP and CANNOT change any spectrum; the consistent
     transposition moves W at 48 entries yet preserves charpoly(W), because W'
     = K_c^-1 W^T K_c is a SIMILARITY.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO DISPERSION
RELATION: what is measured is the characteristic polynomial of a finite matrix
in two momentum sectors, and that E(0) and E(pi) are energies of a propagating
mode is NOT DERIVED.  NO MASS SCALES: theta_1 and theta_2 are logarithms of
exact rational-trace eigenvalues, and no mass, no continuum limit and no unit
is supplied.  NO PHYSICAL TIME STEP: that the two-slice unit cell is THE time
step of a theory is a reading about a staggered carrier, not a theorem.  NO
REFLECTION-POSITIVE TRANSFER: positivity of this 8 x 8 spectrum is proven, and
the Osterwalder-Schrader reconstruction that would make it mean transfer
positivity IS NOT PERFORMED.  NO GRAVITY: no lapse, no shift, no constraint, no
algebra, no closure and no ADM phase space.  NO GENERALITY: ONE fixture, ONE
carrier family, FOUR widths.  AND THE OBJECT ITSELF IS A DISCLOSED VARIANT:
BLOCK 188 IS NOT CORRECTED and its landed T = 8 object is reproduced here
digit-for-digit under ITS OWN sign placement.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 189 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE IMPOSED-OBJECT BANNER AND THE NOT-CLAIMED KEYS: the imposed objects,
     ZERO registered and ZERO adopted, with dispersion, mass scales, physical
     time step, transfer positivity, the landed-object identification and
     generality all declared NOT CLAIMED as measured constants.
  C  THE TWO-SIDED CONSTRUCTION CONTROL: the displayed Hodge against the import
     entrywise, the 144/160 sign-layer fork with Ps-covariance on BOTH sides,
     the landed core minors reproduced under w(3) and measurably different
     under w(T-1), and the T = 12 structure -- d_K^2, Ps H Ps, Ps Q Ps, the
     empty cross block, four PD adjacent cores and the rank-8 full span with a
     zero Schur complement -- plus the two-sided Hodge fork: ROBUSTNESS under
     the check's forensic variant, SENSITIVITY to the volume, and both of the
     check's own rebuilds reproduced digit-for-digit.
  D  THE REFUTATION AND ITS MECHANISM: six exact core witnesses with their
  exact
     positions and values, the two-layer commutator census at T = 8, and the
     check's C2 correction carried as a declared constant.
  E  LOCALITY, RIGIDITY AND THE TWO BOUNDARY LAYERS: the entrywise step
     equalities, the 56-entry Gram inhomogeneity, the (2,2,4) factor pattern,
     the shared quadratics, the near/mirror/deep odd quartics, the far-seam
     even quartic locked across three widths, and the exact mirror covariance.
  F  THE MONODROMY: primitivity at 32 entries with exact witnesses, parity
     independence across three deep cores, the exact spectrum, the four
     positivity facts with factored discriminants, and the coefficient
     identity.
  G  THE COMMUTANT: the U isometry and grading, the S relations and its
     non-isometry, the momentum blocks with the additional isospectrality
     declared, the EXHAUSTIVE 2048-candidate census, the refuted reflection,
     and the P1 resolution with the K-only no-op measured.
  H  the note at its final path, the N5 fence byte-identical, and the nsimplify
     count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through G PASS, with H failing on note-at-final-path
alone until the note is landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: fifty-eight declared mutations, each of which rewrites
  ONE CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement
  happens once, before any mutation flag is consulted, so a mutation can only
  rewrite a CLAIM and no gate can cascade into another.  The per-family census
  is A 2, B 7, C 13, D 5, E 10, F 9, G 10, H 2.
    A  stale_main_authority, stale_parent_authority
    B  claim_objects_registered, claim_dispersion_derived,
       claim_mass_scales_derived, claim_physical_time_step,
       claim_transfer_positivity_derived, claim_variant_is_landed,
       claim_generality
    C  break_hodge_display, break_fork_pair, break_fork_covariance,
       break_landed_control, break_variant_difference, break_dk_square,
       break_cross_block, break_core_positivity, break_span_rank,
       break_schur_complement, break_hodge_robustness,
       break_volume_sensitivity, break_check_reproduction
    D  break_l1_asymmetry, break_l2_asymmetry, break_core_witness,
       break_commutator_support, break_mechanism_sufficiency
    E  break_matrix_locality, break_width_invariance, break_gram_inhomogeneity,
       break_factor_pattern, break_even_quadratics, break_even_rigidity,
       break_far_boundary_layer, break_odd_near_layer, break_odd_deep_lock,
       break_mirror_covariance
    F  break_monodromy_primitive, break_monodromy_witness,
       break_parity_independence, break_monodromy_spectrum,
       break_discriminant_positivity, break_trace_bound, break_reciprocal_form,
       break_trace_ratio_distinct, break_coefficient_identity
    G  break_u_isometry, break_sector_assignment, break_s_relations,
       break_s_isometry, break_momentum_degeneracy, break_census_commutants,
       break_census_isometries, break_reflection_refutation,
       break_transpose_robustness, break_konly_vacuity
    H  drop_n5_fence, break_nsimplify_absence
  SEVEN OF THE FIFTY-EIGHT GUARD CORRECTIONS RATHER THAN RESULTS:
  break_mechanism_sufficiency asserts that [tau^k, G] != 0 alone proves the
  restricted asymmetry, which is exactly the check's C2 correction;
  break_konly_vacuity asserts that the K-only transposition changes the
  spectrum, which this construction's exactly symmetric K_c forbids and which
  corrects the check's P1; break_far_boundary_layer asserts the even quartic is
  rigid at the far seam, which corrects the solve's own wording;
  break_momentum_degeneracy asserts the p = 0 / p = 2 equality is group-forced;
  claim_variant_is_landed asserts the wrap-edge object IS Block 188's; and
  break_landed_control denies the digit-for-digit reproduction that makes the
  variant disclosure honest.

RUNNING
  python3
  scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py
  python3 ... --list-mutations
  python3 ... --mutation break_konly_vacuity
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT, LANDED, AND THINNER THAN BLOCK 189's -- EXACTLY ONE
# OBJECT: the Block 105 shear_hodge() re-exported by the Block 128 module.  The
# cover embedding is NOT imported, because it is fixed to a single time extent
# and this block varies the width; it is rebuilt here for general even T and its
# corner order (1, dx, dt, dx^dt) is the same one.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 189 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 188 tip.
BLOCK189_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_GAUGE_QUOTIENT_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK189_RUNNER = (
    "scripts/admissibility_dirac_kahler_site_gauge_quotient_2026_08_24.py"
)
PARENT_ARTIFACTS = (BLOCK189_NOTE, BLOCK189_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "d4b0edb7e34225397b86b0dc5ca466b673bd677d",   # Block 189 note
    "b4bd04e747d234dfe9f78563202d66d0101d4122",   # Block 189 runner
)
# THE CONSTRUCTION AUTHORITY: Block 188's site route is the object this block
# VARIES, and its landed core minors are the control of gate C.
BLOCK188_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK188_RUNNER = (
    "scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py"
)
# THE LADDER AUTHORITY: Block 107's note, whose transfer step this block probes
# and REFUTES in its naive form.
BLOCK107_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_"
    "THEOREM_NOTE_2026-08-15.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_GAUGE_QUOTIENT_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_site_gauge_quotient_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_ADM_SEAM_TWO_HISTORY_GRAM_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 189 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block189-"
              "site-gauge-quotient-20260824")
PARENT_COMMIT = "996e516600ca9d0f679a6f3ab554036068205d2f"
# The Block 188 tip: a real ancestor of HEAD that predates Block 189 and
# therefore carries NEITHER Block 189 artifact.
STALE_PARENT_COMMIT = "094200a75208b6c8d153c1b91df32a3913729ed0"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_dispersion_derived",
    "claim_mass_scales_derived",
    "claim_physical_time_step",
    "claim_transfer_positivity_derived",
    "claim_variant_is_landed",
    "claim_generality",
    "break_hodge_display",
    "break_fork_pair",
    "break_fork_covariance",
    "break_landed_control",
    "break_variant_difference",
    "break_dk_square",
    "break_cross_block",
    "break_core_positivity",
    "break_span_rank",
    "break_schur_complement",
    "break_hodge_robustness",
    "break_volume_sensitivity",
    "break_check_reproduction",
    "break_l1_asymmetry",
    "break_l2_asymmetry",
    "break_core_witness",
    "break_commutator_support",
    "break_mechanism_sufficiency",
    "break_matrix_locality",
    "break_width_invariance",
    "break_gram_inhomogeneity",
    "break_factor_pattern",
    "break_even_quadratics",
    "break_even_rigidity",
    "break_far_boundary_layer",
    "break_odd_near_layer",
    "break_odd_deep_lock",
    "break_mirror_covariance",
    "break_monodromy_primitive",
    "break_monodromy_witness",
    "break_parity_independence",
    "break_monodromy_spectrum",
    "break_discriminant_positivity",
    "break_trace_bound",
    "break_reciprocal_form",
    "break_trace_ratio_distinct",
    "break_coefficient_identity",
    "break_u_isometry",
    "break_sector_assignment",
    "break_s_relations",
    "break_s_isometry",
    "break_momentum_degeneracy",
    "break_census_commutants",
    "break_census_isometries",
    "break_reflection_refutation",
    "break_transpose_robustness",
    "break_konly_vacuity",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_dispersion_derived": "B",
    "claim_mass_scales_derived": "B",
    "claim_physical_time_step": "B",
    "claim_transfer_positivity_derived": "B",
    "claim_variant_is_landed": "B",
    "claim_generality": "B",
    "break_hodge_display": "C",
    "break_fork_pair": "C",
    "break_fork_covariance": "C",
    "break_landed_control": "C",
    "break_variant_difference": "C",
    "break_dk_square": "C",
    "break_cross_block": "C",
    "break_core_positivity": "C",
    "break_span_rank": "C",
    "break_schur_complement": "C",
    "break_hodge_robustness": "C",
    "break_volume_sensitivity": "C",
    "break_check_reproduction": "C",
    "break_l1_asymmetry": "D",
    "break_l2_asymmetry": "D",
    "break_core_witness": "D",
    "break_commutator_support": "D",
    "break_mechanism_sufficiency": "D",
    "break_matrix_locality": "E",
    "break_width_invariance": "E",
    "break_gram_inhomogeneity": "E",
    "break_factor_pattern": "E",
    "break_even_quadratics": "E",
    "break_even_rigidity": "E",
    "break_far_boundary_layer": "E",
    "break_odd_near_layer": "E",
    "break_odd_deep_lock": "E",
    "break_mirror_covariance": "E",
    "break_monodromy_primitive": "F",
    "break_monodromy_witness": "F",
    "break_parity_independence": "F",
    "break_monodromy_spectrum": "F",
    "break_discriminant_positivity": "F",
    "break_trace_bound": "F",
    "break_reciprocal_form": "F",
    "break_trace_ratio_distinct": "F",
    "break_coefficient_identity": "F",
    "break_u_isometry": "G",
    "break_sector_assignment": "G",
    "break_s_relations": "G",
    "break_s_isometry": "G",
    "break_momentum_degeneracy": "G",
    "break_census_commutants": "G",
    "break_census_isometries": "G",
    "break_reflection_refutation": "G",
    "break_transpose_robustness": "G",
    "break_konly_vacuity": "G",
    "drop_n5_fence": "H",
    "break_nsimplify_absence": "H",
}
MUTATED_FAMILIES = "ABCDEFGH"


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict[str, bool] = {}
        for key, _, value in self.results:
            family = key.split("-", 1)[0]
            summary[family] = summary.get(family, True) and value
        return summary

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print("GATES " + " ".join(
            f"{family}={'PASS' if value else 'FAIL'}"
            for family, value in self.families().items()))

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC).strip()


def worktree_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", path), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def commit_blob(commit: str, path: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC).returncode == 0


def is_hash(value: str) -> bool:
    import re as _re
    return _re.fullmatch(r"[0-9a-f]{40}", value) is not None


def is_placeholder(value: str) -> bool:
    return is_hash(value) and value.startswith("0" * 30)


def audit_inputs_readable() -> tuple:
    missing = tuple(
        path for path in AUDIT_INPUT_PATHS
        if path != SELF_NOTE_INPUT and not (ROOT / path).is_file())
    return len(AUDIT_INPUT_PATHS) - 1 - len(missing), missing


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    machinery_import_landed: bool
    inputs_readable: int
    inputs_missing: tuple


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT):
        return PARENT_COMMIT
    resolved = resolve_ref(PARENT_REF)
    return resolved if is_hash(resolved) else git_output("rev-parse", "HEAD")


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and commit_blob("origin/main", AXIOM_PATH) == CURRENT_AXIOM_BLOB
        and commit_blob("origin/main", REGISTRY_PATH) == CURRENT_REGISTRY_BLOB
        and worktree_blob(AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB)
    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(commit_blob(parent, p) for p in PARENT_ARTIFACTS)
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, p) for p in PARENT_ARTIFACTS)
    readable, missing = audit_inputs_readable()
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT) and not is_placeholder(PARENT_COMMIT),
        bool(is_hash(parent) and is_ancestor(parent, "HEAD")
             and (is_placeholder(PARENT_COMMIT)
                  or resolve_ref(PARENT_REF) == PARENT_COMMIT)),
        bool(len(committed_blobs) == len(PARENT_ARTIFACTS) == 2
             and all(is_hash(v) for v in committed_blobs)
             and committed_blobs == worktree_blobs
             and committed_blobs == PARENT_ARTIFACT_BLOBS),
        bool(all(is_hash(v) for v in stale_blobs)
             and stale_blobs == worktree_blobs),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        MACHINERY_IMPORT_LANDED,
        readable,
        missing)


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
IMPOSED_OBJECTS = (
    "THE WIDTH FAMILY, A DISCLOSED VARIANT OF BLOCK 188's SITE CONSTRUCTION AND NOT THAT CONSTRUCTION: the staggered Dirac-Kahler carrier on Z_T x Z_4 for EVEN T with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 carried ON THE WRAP EDGE t = T-1 (Block 188's landed T = 8 object carries it at t = 3 instead, and the fork is MEASURED here as a pair), the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site Hodge with block B(c) on t < T/2 and P_4 B P_4^T on the far half assembled by the local cell average, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13), at the FOUR widths T = 8, 12, 16, 20",
    "THE PAIR CORES AND THEIR SHIFTED PAIRINGS: for a core t0 the eight cells {(t,x) : t in {t0, t0+1}} in t-major order, the Gram K_c[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)] and the shifted pairings L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE STEP OPERATOR V = K_c^-1 L_1 AND THE UNIT-CELL MONODROMY W = K_c^-1 L_2 -- THIS BLOCK'S OWN CHOSEN OBJECTS, not derived transfer operators of any theory",
    "THE CORE SYMMETRY CANDIDATES: U (the two-site spatial shift), S (the ONE-site spatial shift), R (the spatial reflection x -> -x) and the FULL 2048-element signed-monomial candidate set (optional layer swap x every spatial dihedral action x all relative sign choices up to overall sign), swept EXHAUSTIVELY here",
    "THE SINGLE FIXTURE (m, c) = (9/20, 5/13) at unit volume -- ONE POINT, NOT A WINDOW: no bracket, no ray, no edge and no interior is established for anything in this block",
    "Block 105's LANDED shear_hodge() read through the Block 128 module: THE ONLY OBJECT IMPORTED BY THIS RUNNER, and its value at (5/13, 1) is DISPLAYED ENTRYWISE IN THE NOTE and gated against the import",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SIX ARE FALSE
# AND STAY FALSE.
DISPERSION_CLAIMED = False
MASS_SCALES_CLAIMED = False
PHYSICAL_TIME_STEP_CLAIMED = False
TRANSFER_POSITIVITY_CLAIMED = False
VARIANT_IS_LANDED_CLAIMED = False
GENERALITY_CLAIMED = False
# AND THE SEVENTH DECLARED CONSTANT IS A CORRECTION RATHER THAN A DENIAL: the
# global commutator mechanism does NOT by itself prove the restricted core
# asymmetry.  Family D gates it so break_mechanism_sufficiency has something to
# deny.
GLOBAL_MECHANISM_IS_SUFFICIENT = False
# AND THE EIGHTH: the p = 0 / p = 2 equality is NOT forced by the group.
MOMENTUM_EQUALITY_IS_GROUP_FORCED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function",
    "shift vector",
    "Hamiltonian constraint",
    "momentum/diffeomorphism constraint",
    "first-class constraint algebra",
    "Dirac closure",
    "ADM phase space / history transporter",
    "Osterwalder-Schrader reconstruction of a transfer operator",
    "any continuum limit, any unit and any mass",
)
CHECK_VERDICT = "CONFIRMED-WITH-TWO-CORRECTIONS"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
SPACE_EXTENT = 4
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)
WIDTHS = (8, 12, 16, 20)

# --- C: THE TWO-SIDED CONSTRUCTION CONTROL ----------------------------------
# THE DISPLAYED HODGE, WRITTEN OUT AS THE NOTE WRITES IT.  This is a LITERAL,
# built from the note's formula and NOT from the import; gate C compares it to
# b128.block105.shear_hodge(5/13, 1) entrywise.
DISPLAYED_HODGE = sp.Matrix([
    [1, 0, 0, 0],
    [0, sp.Rational(169, 144), sp.Rational(-65, 144), 0],
    [0, sp.Rational(-65, 144), sp.Rational(169, 144), 0],
    [0, 0, 0, 1]])
# THE SIGN-LAYER FORK, AS A PAIR.  144 is Block 188's landed number at the
# landed placement; 160 is this block's variant at the wrap edge.
LANDED_SIGN_TIME = 3
FORK_ASYMMETRY = {"landed_w3": 144, "wrap_wTm1": 160}
FORK_COVARIANCE = {"landed_w3": 0, "wrap_wTm1": 0}
# THE LANDED CONTROL: Block 188's own core minors, reproduced under w(3).
B188_CORE_MINOR_1 = sp.Rational(
    250811603701251182926764176363850176714557920003089965221914456500,
    666495028860293624372300921944800123265476111209829299156533225479)
B188_CORE_MINOR_2 = sp.Rational(
    9699265179160355495171233606378759680576921193642386633764164130236400111062250000,
    65542091681979044701359795584266761562795513633598145522262137753727157320281821073)
# AND THE VARIANT'S OWN NUMBER AT THE SAME CORE, WHICH IS DIFFERENT.  This is
# what makes the disclosure a measurement instead of a disclaimer.
VARIANT_CORE_MINOR_1 = sp.Rational(
    6874991398831399275340647912337474750,
    18307834037130787420472860378633197921)
# --- C: THE T = 12 STRUCTURE ------------------------------------------------
STRUCTURE_WIDTH = 12
STRUCTURE_HALF = 6
DK_SQUARE_RESIDUAL = 0
HODGE_COVARIANCE_RESIDUAL = 0
ACTION_COVARIANCE_RESIDUAL = 0
CROSS_BLOCK_NONZEROS = 0
ADJACENT_CORES = (1, 2, 3, 4)
CORE_SIGNS = (1,) * 8
FULL_SPAN_SLICES = (1, 2, 3, 4, 5)
FULL_SPAN_RANK = 8
SCHUR_NONZEROS = 0
SCHUR_SHAPE = (12, 12)
# --- C: THE HODGE FORK, RESOLVED ON BOTH SIDES ------------------------------
# THE ADVERSARIAL CHECK REBUILT THIS BLOCK FROM THREE DIFFERENT SHEAR BLOCKS AND
# GOT THREE DIFFERENT ANSWERS.  All three are rebuilt here as declared controls,
# none of them is claimed to be anything, and the result settles the check's
# C3/C6/C8 completely.
# (i) THE FORENSIC VARIANT the check reverse-engineered, I - 2c^2 E11 -
#     c(E12+E21).  It is NOT a landed object.  It is measured here to give the
#     IDENTICAL V and W spectra at every T = 12 core -- which is exactly why the
#     check reproduced this block's headline coefficients digit-for-digit under
#     it.  THE SPECTRA ARE ROBUST IN THIS DIRECTION.
FORENSIC_HODGE = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1 - 2 * FIXTURE_SHEAR ** 2, -FIXTURE_SHEAR, 0],
    [0, -FIXTURE_SHEAR, 1, 0],
    [0, 0, 0, 1]])
HODGE_ROBUST_UNDER_FORENSIC = True
# (ii) THE BLOCK 105 NOTE'S OWN DISPLAYED BLOCK, which is measured here to be the
#     SAME LANDED FUNCTION AT VOLUME 12/13 rather than a different formula:
#     shear_hodge(5/13, 12/13) = diag(12/13, 13/12, 13/12, 13/12) with the
#     (1,2) and (2,1) entries -5/12.  THE SPECTRA ARE NOT ROBUST IN THIS
#     DIRECTION, and this is the whole of the check's C3 discrepancy: a VOLUME
#     convention, not a Hodge formula.  Its T = 12 even-core factors are
#     reproduced here DIGIT-FOR-DIGIT against the check's own displayed rebuild.
CONTROL_VOLUME = sp.Rational(12, 13)
CHECK_B105_FACTORS = ((1975, 1953, -2365), (2365, 1953, -1975),
                      (4746925, 6783420, 13155959, -6783420, 4746925))
# (iii) THE CHECK'S UNIT-VOLUME FALLBACK, I_4 with the (1,2) and (2,1) entries
#     -c.  It is NOT the landed function at any volume.  Its T = 12 even-core
#     factors are likewise reproduced here digit-for-digit.
FALLBACK_HODGE = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, -FIXTURE_SHEAR, 0],
    [0, -FIXTURE_SHEAR, 1, 0],
    [0, 0, 0, 1]])
CHECK_FALLBACK_FACTORS = ((475, 468, -565), (565, 468, -475),
                          (272425, 393120, 755774, -393120, 272425))
VOLUME_SENSITIVE = True
CONTROL_CORES = (1, 2, 3)

# --- D: THE REFUTATION AND ITS MECHANISM ------------------------------------
REFUTATION_CORES = (1, 2, 3)
L1_ASYMMETRY = {1: 48, 2: 48, 3: 48}
L2_ASYMMETRY = {1: 40, 2: 40, 3: 48}
# THE SIX EXACT WITNESSES: (core, k) -> (row, column, exact value).  Positions
# are core-order indices; index 0 is (t0, 0) and index 4 is (t0+1, 0).
CORE_WITNESSES = {
    (1, 1): (0, 1, sp.Rational(
        839039300251161817029323017210249139894300640625,
        10790888393902301609279309496845869518844858077209)),
    (1, 2): (0, 1, sp.Rational(-476073000000, 512915117048537)),
    (2, 1): (0, 1, sp.Rational(
        -906698597244659770526025093421484375,
        120809412487309579386522672090695208353)),
    (2, 2): (0, 4, sp.Rational(
        -128538968276917302214042968750000000,
        7914929056239059806431509242611057315467)),
    (3, 1): (0, 1, sp.Rational(
        -906698597244659770526025093421484375,
        120809412487309579386522672090695208353)),
    (3, 2): (0, 1, sp.Rational(476073000000, 512915117048537)),
}
# THE GLOBAL MECHANISM, MEASURED IN BOTH SIGN LAYERS AT T = 8.
MECHANISM_WIDTH = 8
TAU2_ACTION_NONZEROS = {"landed_w3": 224, "wrap_wTm1": 208}
TAU2_ACTION_PAIRS = {"landed_w3": 28, "wrap_wTm1": 26}
TAU2_ACTION_WITNESS = sp.Rational(-65, 576)
TAU2_INVERSE_NONZERO = {"landed_w3": 944, "wrap_wTm1": 864}

# --- E: LOCALITY, RIGIDITY AND THE TWO BOUNDARY LAYERS ----------------------
STEP_EQUALITIES = {
    "V2@T16 - V4@T16": 0,
    "V2@T12 - V2@T16": 0,
    "V1@T12 - V1@T16": 0,
}
GRAM_INHOMOGENEITY = 56
GRAM_WITNESS = sp.Rational(
    400377448540516729912267326589982089768750145494702722472706914791871900000,
    6123616489153094576092155984273690994586709553556143546606984965959685926729)
FACTOR_PATTERN = (2, 2, 4)
EVEN_QUADRATICS = ((5675, 5634, -6845), (6845, 5634, -5675))
ODD_QUADRATICS = ((1794654055, 1598495382, -2164653217),
                  (2164653217, 1598495382, -1794654055))
EVEN_DEEP_QUARTIC = (39529825, 55889280, 109432706, -55889280, 39529825)
# THIS BLOCK'S OWN CORRECTION TO THE SOLVE'S WORDING: the even quartic is NOT
# rigid at the FAR seam.  At t0 = half - 2 it takes this value instead, and that
# value is locked across all three widths.
EVEN_FAR_QUARTIC = (47667825, 63213480, 101294706, -55889280, 39529825)
ODD_NEAR_QUARTIC = (38849406107919890625, 96204052429420176000,
                    476869355306538239554, -108546564308758876800,
                    43833595903292990625)
ODD_MIRROR_QUARTIC = (43833595903292990625, 108546564308758876800,
                      476869355306538239554, -96204052429420176000,
                      38849406107919890625)
ODD_DEEP_QUARTIC = (20375067515625, 50455444752000, 257292658829458,
                    -50455444752000, 20375067515625)
# THE PROBED CORE TABLE: (width, t0) -> the expected quartic key.
EVEN_DEEP_CORES = ((12, 2), (16, 2), (16, 4), (20, 2), (20, 4), (20, 6))
EVEN_FAR_CORES = ((12, 4), (16, 6), (20, 8))
ODD_NEAR_CORES = ((12, 1), (16, 1), (20, 1))
ODD_MIRROR_CORES = ((12, 3), (16, 5), (20, 7))
ODD_DEEP_CORES = ((16, 3), (20, 3), (20, 5))
ALL_PROBED_CORES = (EVEN_DEEP_CORES + EVEN_FAR_CORES + ODD_NEAR_CORES
                    + ODD_MIRROR_CORES + ODD_DEEP_CORES)
MIRROR_PAIRS = ((12, 1, 3), (16, 1, 5))
MIRROR_RESIDUAL = 0

# --- F: THE UNIT-CELL MONODROMY ---------------------------------------------
MONODROMY_WIDTH = 20
DEEP_CORES = (3, 4, 5)
PRIMITIVITY_NONZEROS = 32
PRIMITIVITY_WITNESSES = {
    3: sp.Rational(53601896033238042551256, 229758595220483765728625),
    4: sp.Rational(-46628656073521939366872, 229758595220483765728625),
    5: sp.Rational(53601896033238042551256, 229758595220483765728625),
}
MONODROMY_HEAVY = (22569375, -233631106, 22569375)
MONODROMY_LIGHT = (39529825, -109432706, 39529825)
MONODROMY_FACTORS = ((MONODROMY_HEAVY, 2), (MONODROMY_LIGHT, 2))
DISCRIMINANTS = {
    MONODROMY_HEAVY: 52545986939220736,
    MONODROMY_LIGHT: 5725088884359936,
}
DISCRIMINANT_FACTORIZATIONS = {
    MONODROMY_HEAVY: {2: 8, 13: 1, 31: 1, 37: 1, 71: 1, 313: 2, 1979: 1},
    MONODROMY_LIGHT: {2: 8, 3: 7, 7: 1, 13: 1, 31: 1, 37: 1, 313: 2},
}
TRACE_RATIO_GAP = 6765568955757700
TWO_COSH = {MONODROMY_HEAVY: sp.Rational(233631106, 22569375),
            MONODROMY_LIGHT: sp.Rational(109432706, 39529825)}
# THE COEFFICIENT IDENTITY: the second monodromy quadratic is a z^2 - c z + a
# from the even V-quartic (a, b, c, -b, a); b DROPS OUT.
COEFFICIENT_IDENTITY_SOURCE = EVEN_DEEP_QUARTIC

# --- G: THE COMMUTANT --------------------------------------------------------
COMMUTANT_CORE = 3
U_ISOMETRY_RESIDUAL = 0
U_COMMUTATOR_RESIDUAL = 0
U_OFF_SECTOR_NONZEROS = 0
U_SECTOR_FACTORS = {1: (MONODROMY_LIGHT, 2), -1: (MONODROMY_HEAVY, 2)}
S_COMMUTATOR_RESIDUAL = 0
S_SQUARE_RESIDUAL = 0
S_FOURTH_RESIDUAL = 0
S_GRAM_DEFECT = 64
S_GRAM_WITNESS = sp.Rational(
    2196923328476037505923247454222973532938493206039747366330235451412004291015625,
    2814140416367857864535548440193722522538862625515710221151046656087532099673561724)
MOMENTUM_FACTORS = {"p0": MONODROMY_LIGHT, "p2": MONODROMY_LIGHT,
                    "p13": MONODROMY_HEAVY}
CENSUS_SIZE = 2048
CENSUS_COMMUTANTS = ("I", "S", "S^3", "U")
CENSUS_ISOMETRIES = ("I", "U")
REFLECTION_COMMUTATOR_NONZEROS = 16
REFLECTION_WITNESS = sp.Rational(16334218, 7905965)
# THE P1 RESOLUTION.  K_c is EXACTLY SYMMETRIC at the deep core, so the K-only
# transposition is a NO-OP; the consistent transposition moves W at 48 entries
# and preserves charpoly because W' = K_c^-1 W^T K_c is a similarity.
CORE_GRAM_SYMMETRY_RESIDUAL = 0
KONLY_DIFFERENCE = 0
CONSISTENT_DIFFERENCE = 48
SIMILARITY_RESIDUAL = 0

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO, so a residual, a minor or a polynomial coefficient passed through
# it can silently lose its sign -- and this block is nothing but zeros, counts,
# signs and exact coefficient vectors.  Every mass and shear here is ALREADY an
# exact sympy Rational.  Gate H counts the occurrences in this file's own source
# and requires ZERO.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def rational_matrix(matrix: sp.MatrixBase) -> DomainMatrix:
    """THE EXACT RATIONAL DOMAIN, AND IT IS NOT A NUMERICAL METHOD.  Every entry
    of every matrix in this runner is a sympy Rational, so the matrix lies in
    QQ^(n x n) exactly; DomainMatrix carries out rank, inverse and determinant by
    exact fraction-free arithmetic over that field.  No float is created at any
    point and no tolerance exists to be tuned.  It is used in place of the dense
    sympy fallbacks purely because those are slow at dimensions 48, 64 and 80,
    and it changes NO value."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


def exact_rank(matrix: sp.MatrixBase) -> int:
    return rational_matrix(matrix).rank()


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return rational_matrix(matrix).inv().to_Matrix()


def exact_determinant(matrix: sp.MatrixBase) -> object:
    return QQ.to_sympy(rational_matrix(matrix).det())


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is involved."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


def first_nonzero(matrix: sp.MatrixBase) -> tuple:
    """(row, column, exact value) of the first nonzero entry in row-major order,
    or (-1, -1, 0) if the matrix is exactly zero.  THE WITNESS IS AN ENTRY AND A
    POSITION, never a norm."""
    for row in range(matrix.rows):
        for column in range(matrix.cols):
            if matrix[row, column] != 0:
                return (row, column, matrix[row, column])
    return (-1, -1, sp.Integer(0))


def slice_pair_support(matrix: sp.MatrixBase) -> tuple:
    """THE EXACT ORDERED TIME-SLICE-PAIR SUPPORT of a cover-sized matrix."""
    return tuple(sorted({
        (row // SPACE_EXTENT, column // SPACE_EXTENT)
        for row in range(matrix.rows) for column in range(matrix.cols)
        if matrix[row, column] != 0}))


def leading_minors(matrix: sp.Matrix) -> tuple:
    return tuple(exact_determinant(matrix[:size, :size])
                 for size in range(1, matrix.rows + 1))


def minor_signs(minors: tuple) -> tuple:
    return tuple(int(sp.sign(value)) for value in minors)


def primitive_coefficients(expression: object, variable: sp.Symbol) -> tuple:
    """THE PRIMITIVE INTEGER COEFFICIENT VECTOR of a rational polynomial, high
    degree first, normalized to a POSITIVE leading coefficient and to content 1.
    This is the canonical form every polynomial claim in this block is stated in,
    so that no claim depends on an incidental rational scaling."""
    polynomial = sp.Poly(sp.expand(expression), variable)
    coefficients = [sp.Rational(c) for c in polynomial.all_coeffs()]
    multiplier = 1
    for value in coefficients:
        multiplier = sp.ilcm(multiplier, value.q)
    integers = [sp.Integer(value * multiplier) for value in coefficients]
    content = 0
    for value in integers:
        content = sp.igcd(content, int(value))
    integers = [value / content for value in integers]
    if integers[0] < 0:
        integers = [-value for value in integers]
    return tuple(int(value) for value in integers)


def char_factors(matrix: sp.Matrix) -> tuple:
    """THE EXACT RATIONAL FACTORIZATION of the characteristic polynomial, as
    (primitive coefficient vector, multiplicity) pairs sorted by degree then
    lexicographically.  sympy's factor_list over Q is exact."""
    variable = sp.Symbol("z")
    expression = matrix.charpoly(variable).as_expr()
    factors = []
    for factor, multiplicity in sp.factor_list(expression)[1]:
        if factor.has(variable):
            factors.append(
                (primitive_coefficients(factor, variable), multiplicity))
    return tuple(sorted(factors, key=lambda item: (len(item[0]), item[0])))


def degree_pattern(factors: tuple) -> tuple:
    """THE FACTOR-DEGREE PATTERN, with multiplicity expanded."""
    degrees = []
    for coefficients, multiplicity in factors:
        degrees.extend([len(coefficients) - 1] * multiplicity)
    return tuple(sorted(degrees))


def quartic_of(factors: tuple) -> tuple:
    quartics = [c for c, _ in factors if len(c) == 5]
    return quartics[0] if len(quartics) == 1 else ()


def quadratics_of(factors: tuple) -> tuple:
    return tuple(sorted(c for c, _ in factors if len(c) == 3))


def is_exact_rational(value: object) -> bool:
    expression = sp.sympify(value)
    return bool(not expression.atoms(sp.Float) and expression.is_rational)


# ---------------------------------------------------------------------------
# THE WIDTH FAMILY, BUILT DIRECTLY.  Nothing here is imported except the Block
# 105 shear block; the cell embedding, the kernel, the grading, the reflection,
# the raising set, the glue and the completion are all built at general even T.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def site_index(width: int, time: int, space: int) -> int:
    """idx(t,x) = (t mod T)*4 + (x mod 4): time first, the same t-major ordering
    Blocks 107, 128 and 188 use."""
    return (time % width) * SPACE_EXTENT + space % SPACE_EXTENT


def staggered_kernel(width: int, sign_time: int) -> sp.Matrix:
    """THE STAGGERED KERNEL AT GENERAL EVEN WIDTH.  eta_t = 1 and
    eta_x = (-1)^t; the temporal edge sign is -1 at t = sign_time and +1
    elsewhere, and every bond is antisymmetrized.  THE SIGN PLACEMENT IS THE
    FORK: sign_time = T-1 is THIS BLOCK'S WRAP-EDGE convention and
    sign_time = 3 is Block 188's LANDED placement at T = 8."""
    size = width * SPACE_EXTENT
    kernel = sp.zeros(size, size)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if time == sign_time else 1
            here = site_index(width, time, space)
            ahead = site_index(width, time + 1, space)
            kernel[here, ahead] += sp.Rational(temporal_sign, 2)
            kernel[ahead, here] -= sp.Rational(temporal_sign, 2)
            spatial_sign = (-1) ** time
            right = site_index(width, time, space + 1)
            kernel[here, right] += sp.Rational(spatial_sign, 2)
            kernel[right, here] -= sp.Rational(spatial_sign, 2)
    return kernel


def site_degree(time: int, space: int) -> int:
    return time % 2 + space % 2


def grade_projector(width: int, grade: int) -> sp.Matrix:
    return sp.diag(*[1 if site_degree(t, x) == grade else 0
                     for t in range(width) for x in range(SPACE_EXTENT)])


def raising_part(width: int, kernel: sp.Matrix) -> sp.Matrix:
    """d_K = P1 K P0 + P2 K P1, the grade-raising part."""
    p0, p1, p2 = (grade_projector(width, g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def site_theta(width: int, time: int) -> int:
    """theta_s(t) = -t, fixing the slices {0, T/2}."""
    return (-time) % width


def reflection_permutation(width: int) -> sp.Matrix:
    size = width * SPACE_EXTENT
    matrix = sp.zeros(size, size)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            matrix[site_index(width, site_theta(width, time), space),
                   site_index(width, time, space)] = 1
    return matrix


def cell_embedding(width: int, time: int, space: int) -> sp.Matrix:
    """THE UNIT-CELL EMBEDDING at general width, corner order
    (1, dx, dt, dx^dt) -- the same corner order the landed Block 128
    cover_embedding() uses, rebuilt here because that function is fixed to a
    single time extent and this block varies the width."""
    matrix = sp.zeros(width * SPACE_EXTENT, 4)
    for column, (delta_t, delta_x) in enumerate(
            ((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[site_index(width, time + delta_t, space + delta_x), column] = 1
    return matrix


def imported_shear_block(shear: object) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT: the LANDED Block 105 shear Hodge at an EXACT
    rational shear and unit volume.  NO nsimplify: both arguments are already
    sympy Rationals or Integers."""
    return b128.block105.shear_hodge(shear, UNIT_VOLUME)


def site_hodge(width: int, block: sp.Matrix) -> sp.Matrix:
    """THE SITE-ADAPTED GLUED HODGE at general width.  The physical anchors
    t < T/2 carry the block; the image anchors t >= T/2 carry its P_4 image,
    UNFLIPPED; the cover assembly is the local cell average."""
    half = width // 2
    blocks = [block if time < half
              else sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
              for time in range(width)]
    result = sp.zeros(width * SPACE_EXTENT, width * SPACE_EXTENT)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            embedding = cell_embedding(width, time, space)
            result += embedding * blocks[time] * embedding.T / 4
    return sp.expand(result)


def site_restricted_raising(width: int, raising: sp.Matrix) -> sp.Matrix:
    """A_s: the d_K entries with BOTH endpoint times in the CLOSED half
    {0..T/2}, EXCLUDING the spatial edges that live INSIDE a fixed slice."""
    half = width // 2
    closed = set(range(half + 1))
    fixed = {0, half}
    size = width * SPACE_EXTENT
    result = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            if row_time not in closed or column_time not in closed:
                continue
            if row_time == column_time and row_time in fixed:
                continue
            result[row, column] = raising[row, column]
    return result


def build_width_action(width: int, mass: object, block: sp.Matrix,
                       sign_time: int) -> dict:
    """THE WIDTH FAMILY, REBUILT WHOLE at a given width, mass, shear block and
    sign placement.  Q = m H + H D_s - D_s^T H, Block 107's completion used
    UNCHANGED."""
    kernel = staggered_kernel(width, sign_time)
    raising = raising_part(width, kernel)
    reflection = reflection_permutation(width)
    restricted = site_restricted_raising(width, raising)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    hodge = site_hodge(width, block)
    action = sp.expand(mass * hodge + hodge * glue - glue.T * hodge)
    return {"kernel": kernel, "raising": raising, "reflection": reflection,
            "glue": glue, "hodge": hodge, "action": action}


def core_cells(core: int) -> tuple:
    """THE PAIR CORE {(t,x) : t in {t0, t0+1}} in t-major order."""
    return tuple((time, space) for time in (core, core + 1)
                 for space in range(SPACE_EXTENT))


def shifted_pairing(width: int, inverse: sp.Matrix, core: int,
                    step: int) -> sp.Matrix:
    """L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]; k = 0 is the core
    Gram K_c itself.  THE INDEX ORDER IS t-MAJOR."""
    cells = core_cells(core)
    size = len(cells)
    matrix = sp.zeros(size, size)
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(width, site_theta(width, row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(width, column_time + step, column_space), partner]
    return sp.expand(matrix)


def span_gram(width: int, inverse: sp.Matrix, slices: tuple) -> sp.Matrix:
    """THE FULL-SPAN GRAM over several adjacent slices, same pairing."""
    cells = tuple((time, space) for time in slices
                  for space in range(SPACE_EXTENT))
    size = len(cells)
    matrix = sp.zeros(size, size)
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(width, site_theta(width, row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(width, column_time, column_space), partner]
    return sp.expand(matrix)


def time_shift(width: int, step: int) -> sp.Matrix:
    """tau^k: e_(t,x) -> e_(t+k,x), the time translation whose failure to commute
    with the action is the global mechanism of family D."""
    size = width * SPACE_EXTENT
    matrix = sp.zeros(size, size)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            matrix[site_index(width, time + step, space),
                   site_index(width, time, space)] = 1
    return matrix


# ---------------------------------------------------------------------------
# THE CORE SYMMETRY CANDIDATES, as 8 x 8 matrices in the core order
# ---------------------------------------------------------------------------
def core_permutation(core: int, action) -> sp.Matrix:
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    matrix = sp.zeros(len(cells), len(cells))
    for cell in cells:
        matrix[position[action(cell)], position[cell]] = 1
    return matrix


def spatial_shift(core: int, amount: int) -> sp.Matrix:
    return core_permutation(
        core, lambda cell: (cell[0], (cell[1] + amount) % SPACE_EXTENT))


def spatial_reflection(core: int) -> sp.Matrix:
    return core_permutation(
        core, lambda cell: (cell[0], (-cell[1]) % SPACE_EXTENT))


def candidate_monomials(core: int) -> tuple:
    """THE EXHAUSTIVE SIGNED-MONOMIAL CANDIDATE SET: an optional swap of the two
    time layers, times every spatial dihedral action (4 rotations x 2
    reflections), times every relative sign pattern up to an overall sign.  That
    is 2 * 8 * 2^7 = 2048 matrices, and family G sweeps all of them."""
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    candidates = []
    for swap in (False, True):
        for reflect in (False, True):
            for shift in range(SPACE_EXTENT):
                permutation = sp.zeros(8, 8)
                for time, space in cells:
                    image_time = (2 * core + 1 - time) if swap else time
                    image_space = ((-space) % SPACE_EXTENT if reflect
                                   else (space + shift) % SPACE_EXTENT)
                    permutation[position[(image_time, image_space)],
                                position[(time, space)]] = 1
                for bits in range(2 ** 7):
                    signs = [1] + [1 if not (bits >> k) & 1 else -1
                                   for k in range(7)]
                    candidates.append(sp.diag(*signs) * permutation)
    return tuple(candidates)


def sector_block(projector: sp.Matrix, operator: sp.Matrix) -> sp.Matrix:
    """THE OPERATOR RESTRICTED TO AN INVARIANT SUBSPACE, in an exact basis of the
    projector's column space: (B^T B)^-1 B^T M B.  Exact throughout."""
    basis = sp.Matrix.hstack(*projector.columnspace())
    gram = sp.expand(basis.T * basis)
    return sp.expand(exact_inverse(gram) * basis.T * operator * basis)


def nullspace_block(matrix: sp.Matrix, operator: sp.Matrix) -> sp.Matrix:
    basis = sp.Matrix.hstack(*sp.expand(matrix).nullspace())
    gram = sp.expand(basis.T * basis)
    return sp.expand(exact_inverse(gram) * basis.T * operator * basis)


def note_text() -> tuple:
    """(text, at_final_path).  THE FINAL PATH IS THE ONLY PATH READ: there is no
    draft fallback anywhere in this runner, so before landing the text is empty
    and gate H fails on note-at-final-path alone."""
    try:
        return NOTE_PATH.read_text(encoding="utf-8"), True
    except OSError:
        return "", False


def landed_text(path: str) -> str:
    try:
        return (ROOT / path).read_text(encoding="utf-8")
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# THE N5 FENCE.  Single-line literal with \n separators; it appears
# BYTE-IDENTICALLY in the note and gate H checks it as a raw substring.
# ---------------------------------------------------------------------------
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH. NOTHING HERE IS REGISTERED OR ADOPTED -- THE WIDTH FAMILY (the staggered Dirac-Kahler carrier on Z_T x Z_4 for even T with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 carried ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site Hodge with block B(c) on t < T/2 and P_4 B P_4^T on the far half, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13), at widths T = 8, 12, 16, 20), THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE STEP OPERATOR V = K_c^-1 L_1 AND THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE CORE SYMMETRY CANDIDATES U, S, R and the full 2048-element signed-monomial set, THE SINGLE FIXTURE (9/20, 5/13), and the LANDED Block 105 shear_hodge() read through the Block 128 module -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. AND THE OBJECT IS A DISCLOSED VARIANT AND SAYS SO BEFORE IT SAYS ANYTHING ELSE: BLOCK 188's LANDED T = 8 OBJECT CARRIES THE ANTIPERIODIC SIGN AT t = 3 AND THIS FAMILY CARRIES IT AT t = T-1, AND THE FORK IS MEASURED AS A PAIR -- nnz(Q - Q^T) = 144 at the landed placement, which is BLOCK 188's OWN LANDED NUMBER, and 160 at the wrap edge, with Ps Q Ps = Q^T at ZERO on BOTH SIDES. AND THE WORDS ARE FENCED BEFORE THE NUMBERS ARE READ. DISPERSION IS A READING: what is measured is the characteristic polynomial of a finite matrix in two momentum sectors, and that E(0) and E(pi) are energies of a propagating mode is NOT DERIVED. MASS SCALES ARE A READING: theta_1 and theta_2 are logarithms of exact rational-trace eigenvalues, with no mass, no continuum limit and no unit supplied. THE PHYSICAL TIME STEP IS A READING: that the two-slice unit cell is THE time step of a theory is a statement about a staggered carrier and not a theorem. TRANSFER POSITIVITY IS A READING: the positivity of this 8 x 8 spectrum is PROVEN, and the Osterwalder-Schrader reconstruction that would make it mean transfer positivity IS NOT PERFORMED. NO GRAVITY STRUCTURE IS SUPPLIED -- no lapse function, no shift vector, no Hamiltonian constraint, no momentum or diffeomorphism constraint, no first-class algebra, no Dirac closure and no ADM phase space. NO GENERALITY IS CLAIMED: ONE fixture, ONE carrier family, FOUR widths. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONSTRUCTION CONTROL IS TWO-SIDED AND IT COMES FIRST. THE HODGE: the ONLY imported object is Block 105's shear_hodge() through the Block 128 module, its value at (c, v) = (5/13, 1) is DISPLAYED INLINE ENTRYWISE as I + (25/144)(E11 + E22) - (65/144)(E12 + E21) -- that is diag(1, 169/144, 169/144, 1) with the (1,2) and (2,1) entries -65/144 in zero-based corner order (1, dx, dt, dx^dt) -- and the displayed matrix is gated against the import at ZERO entrywise residual. THE SIGN LAYER: at T = 8 the LANDED placement reproduces BLOCK 188's core minors DIGIT-FOR-DIGIT, first minor 250811603701251182926764176363850176714557920003089965221914456500/666495028860293624372300921944800123265476111209829299156533225479 and second minor 9699265179160355495171233606378759680576921193642386633764164130236400111062250000/65542091681979044701359795584266761562795513633598145522262137753727157320281821073, while the WRAP placement gives 6874991398831399275340647912337474750/18307834037130787420472860378633197921 at the same core -- A DIFFERENT NUMBER, MEASURED, WHICH IS EXACTLY WHY THE VARIANT IS DISCLOSED AND NOT ASSERTED TO BE THEIR OBJECT. AND THE HODGE FORK IS RESOLVED ON BOTH SIDES, WHICH SETTLES THE ADVERSARIAL CHECK'S C3/C6/C8 RATHER THAN ARGUING WITH IT: the check's FORENSIC variant block I - 2c^2 E11 - c(E12+E21) gives the IDENTICAL V and W factorizations at all three T = 12 bulk cores -- which is exactly why the check reproduced every headline coefficient digit-for-digit under it -- while the BLOCK 105 NOTE'S OWN DISPLAYED BLOCK is measured here to be THE SAME LANDED FUNCTION AT VOLUME 12/13, diag(12/13, 13/12, 13/12, 13/12) with the (1,2) and (2,1) entries -5/12, and at that volume every bulk core MOVES: the even core gives (1975, 1953, -2365), (2365, 1953, -1975) and 4746925 z^4 + 6783420 z^3 + 13155959 z^2 - 6783420 z + 4746925, which is THE CHECK'S OWN DISPLAYED REBUILD REPRODUCED DIGIT-FOR-DIGIT, as is their unit-shear fallback's (475, 468, -565), (565, 468, -475) and 272425 z^4 + 393120 z^3 + 755774 z^2 - 393120 z + 272425. THE DISCREPANCY WAS A VOLUME CONVENTION AND NEVER A DISPUTED MEASUREMENT, and that is why this note DISPLAYS the block entrywise at a PINNED volume instead of describing it. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's zeros, counts, signs or coefficient vectors could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate H.\nper_mode: THE NAIVE TRANSFER PAIRING IS REFUTED ON THE CORES THEMSELVES, AND THE CHECK'S C2 CORRECTION IS CARRIED AS CONTENT AND NOT AS AN ERRATUM. At T = 12 the one-step and two-step core pairings are ASYMMETRIC at every bulk core: nnz(L_1 - L_1^T) = 48 at t0 = 1, 2, 3 and nnz(L_2 - L_2^T) = 40, 40, 48, with SIX EXACT WITNESSES recorded by position and value. THE GLOBAL MECHANISM IS [tau^k, G] != 0, measured at T = 8 IN BOTH SIGN LAYERS: [tau^2, Q] has 224 nonzeros on 28 ordered slice pairs at the landed placement and 208 on 26 at the wrap edge, with the COMMON exact witness [tau^2, Q]_(0,1) = -65/576, and [tau^2, G] is nonzero in both at 944 and 864 entries. BUT THE CORRECTION IS TAKEN AND IT IS DECLARED AS A CONSTANT: global commutator nonvanishing is NOT BY ITSELF a proof that a RESTRICTED core pairing is asymmetric, because symmetry after restriction to one 8-vector core requires only the PROJECTED commutator block to vanish. THE SIX CORE WITNESSES ARE THE PROOF AND THE COMMUTATOR IS THE MECHANISM.\nper_block: THE STEP OPERATOR IS A LOCAL OBJECT, AND LOCALITY IS A MATRIX STATEMENT AND NOT A SPECTRAL ONE. V2@T12, V2@T16 and V4@T16 are EQUAL ENTRYWISE at ZERO residual, and so are V1@T12 and V1@T16: the step dynamics is width-invariant AND position-homogeneous. THE GRAM IS NOT: K_c(2) and K_c(4) at T = 16 differ at EXACTLY 56 ENTRIES, so the boundary layer lives in the metric data. Every probed core factors (2,2,4) over Q with the even quadratics (5675, 5634, -6845), (6845, 5634, -5675) and the odd quadratics (1794654055, 1598495382, -2164653217), (2164653217, 1598495382, -1794654055) invariant throughout. THE ODD QUARTIC CARRIES A NEAR-SEAM LAYER: value 38849406107919890625 z^4 + 96204052429420176000 z^3 + 476869355306538239554 z^2 - 108546564308758876800 z + 43833595903292990625 at t0 = 1 locked at ALL THREE widths, its exact coefficient MIRROR at t0 = T/2 - 3, and the DEEP value 20375067515625 z^4 + 50455444752000 z^3 + 257292658829458 z^2 - 50455444752000 z + 20375067515625 at T = 16 t0 = 3 and T = 20 t0 = 3, 5. AND THE EVEN QUARTIC IS NOT RIGID EVERYWHERE, WHICH CORRECTS THIS BLOCK'S OWN EARLIER WORDING: at the FAR-seam core t0 = T/2 - 2 it is 47667825 z^4 + 63213480 z^3 + 101294706 z^2 - 55889280 z + 39529825 rather than the deep 39529825-family value, and THAT far-seam value is itself LOCKED across T = 12, 16 and 20. The even sector is rigid in the INTERIOR and carries its own one-core far-seam layer. AND THE MIRROR COVARIANCE IS EXACT: q_j = (-1)^j p_(8-j) for all nine coefficients at T = 12 (V1 against V3) and T = 16 (V1 against V5), which is q(z) proportional to z^8 p(-1/z) and therefore spec(V_mirror) = {-1/lambda} with multiplicity.\nlattice_wide: THE UNIT-CELL MONODROMY IS PRIMITIVE, PARITY-INDEPENDENT AND POSITIVE, AND THE POSITIVITY IS PROVEN AND NOT ESTIMATED. W != V^2 at EXACTLY 32 entries at every T = 20 deep core t0 = 3, 4, 5, with exact witnesses (W - V^2)_(0,4) = 53601896033238042551256/229758595220483765728625, -46628656073521939366872/229758595220483765728625 and 53601896033238042551256/229758595220483765728625; the monodromy cannot be built by squaring the step and W is the primitive object. charpoly(W) is IDENTICAL at all three deep cores and equals (22569375 z^2 - 233631106 z + 22569375)^2 (39529825 z^2 - 109432706 z + 39529825)^2. THE FOUR POSITIVITY FACTS ARE EXACT INTEGERS: the discriminants are 52545986939220736 = 2^8 * 13 * 31 * 37 * 71 * 313^2 * 1979 and 5725088884359936 = 2^8 * 3^7 * 7 * 13 * 31 * 37 * 313^2, both POSITIVE with their factorizations gated; both traces exceed twice the leading coefficient; both constant/leading ratios are EXACTLY 1 so each pair is reciprocal; and the two trace ratios are DISTINCT because 233631106 * 39529825 - 109432706 * 22569375 = 6765568955757700 != 0. Four distinct real positive roots in two reciprocal pairs, with 2 cosh(theta_1) = 233631106/22569375 and 2 cosh(theta_2) = 109432706/39529825 EXACTLY. AND THE COEFFICIENT IDENTITY IS EXACT: the second monodromy quadratic is a z^2 - c z + a built from the even V-quartic's (a, b, c) = (39529825, 55889280, 109432706), with the odd coefficient b DROPPING OUT.\nper_scope: THE COMMUTANT IS COMPUTED EXHAUSTIVELY AND NOT GUESSED, AND THE CHECK'S P1 FORK IS RESOLVED THE OTHER WAY. U (the two-site spatial shift) satisfies U^T K_c U = K_c and [W, U] = 0 at ZERO, with the off-sector block EXACTLY zero, and it GRADES the spectrum: U = +1 carries both copies of 39529825 z^2 - 109432706 z + 39529825 and U = -1 both copies of 22569375 z^2 - 233631106 z + 22569375. S (the ONE-site spatial shift) also commutes with W at ZERO, with S^2 = U and S^4 = I at ZERO, but is NOT a Gram isometry -- S^T K_c S - K_c has EXACTLY 64 nonzero entries with an exact witness -- which is the check's P2 finding rebuilt here on this construction. Its momentum blocks give p = 0 and p = 2 the SAME polynomial and p = 1, 3 the other one, AND THE p = 0 / p = 2 EQUALITY IS DECLARED NOT GROUP-FORCED: it is an ADDITIONAL exact isospectrality. THE CENSUS IS EXHAUSTIVE AND MEASURED IN THIS RUNNER RATHER THAN CITED: all 2048 signed monomial candidates are swept, the W-commutants are EXACTLY {I, S, U, S^3} and EXACTLY {I, U} of them are Gram isometries; the unsigned spatial reflection is refuted with a 16-entry commutator and the exact witness [W, R]_(0,5) = 16334218/7905965. AND THE P1 CORRECTION RUNS THE OTHER WAY ON THIS CONSTRUCTION, WHICH IS THIS BLOCK'S SECOND CORRECTION TO THE CHECK: K_c is EXACTLY SYMMETRIC at the deep core, so the K-ONLY transposition is a MEASURED NO-OP at 0 entries and CANNOT change any spectrum, while the CONSISTENT transposition moves W at EXACTLY 48 entries and still preserves charpoly(W) -- because W' = K_c^-1 W^T K_c is a SIMILARITY, which is a two-line proof and not a coincidence of these numbers.\nRESULT: A NAIVE TRANSFER IS REFUTED WITH SIX EXACT WITNESSES, A LOCAL STEP OPERATOR WITH TWO FINITE-RANGE BOUNDARY LAYERS IS EXHIBITED, AND A PRIMITIVE UNIT-CELL MONODROMY WITH A PROVEN POSITIVE RECIPROCAL SPECTRUM AND AN EXHAUSTIVELY COMPUTED COMMUTANT IS COMPUTED IN CLOSED FORM -- AND NOT ONE LINE OF IT IS GRAVITY. The construction control is two-sided and both sides are measured; the displayed Hodge equals the import entrywise; the sign-layer fork is 144 against 160 with Ps-covariance on both sides and the landed minors reproduced digit-for-digit at the landed placement; L_1 and L_2 are asymmetric at every bulk core with six exact witnesses and the global commutator is the MECHANISM and not the proof; the step matrices are width- and position-invariant while the Grams are not, at 56 entries; the odd quartic has a near-seam value, its exact mirror and a deep value, and the even quartic has its own far-seam value locked across three widths; the mirror covariance is exact at nine coefficients; the monodromy is primitive at 32 entries, parity-independent across three deep cores, and positive with factored discriminants and distinct trace ratios; and the commutant is EXACTLY {I, S, U, S^3} with EXACTLY {I, U} isometries out of 2048 candidates. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-189 STAND EXACTLY AS LANDED. BLOCK 188 IS NEITHER CORRECTED NOR CONTRADICTED: their T = 8 object is reproduced here DIGIT-FOR-DIGIT under THEIR OWN sign placement, and this block's family is a DISCLOSED VARIANT at a different placement, measured to be a different matrix. BLOCK 189 IS NOT CORRECTED: its stabilizer element U reappears here as the exact mass-scale grading of the monodromy, which extends their result and changes none of it. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE FIXTURE AND NO WINDOW; the four headline words are READINGS and the OS reconstruction that would license them IS NOT PERFORMED; the even quartic's rigidity is NOT global and its far-seam exception is measured here rather than papered over; and the deep-core probes reach T = 20 and no further, so nothing is proven about the infinite-width limit. TWO ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C2 CORRECTION, that the global commutator is a mechanism and the six core witnesses are the proof, which is now a declared constant and a gate; and the P2 S-COMMUTANT, which is now rebuilt, gated and extended by an exhaustive 2048-candidate census. AND TWO CORRECTIONS RUN THE OTHER WAY AND ARE STATED AS SUCH: the check's P1 K-only spectrum change does NOT occur on this construction, because K_c is exactly symmetric and the K-only transposition is a no-op; and the check's C3/C6/C8 coefficient refutations do NOT apply to this construction, because they were computed at a DIFFERENT VOLUME -- the landed shear_hodge() at v = 1 reproduces every stated coefficient, their own two rebuilds are reproduced here digit-for-digit at v = 12/13 and at unit shear, and their forensic variant is measured to be spectrally IDENTICAL to the landed block, which is why the display is now gated entrywise against the import at a PINNED volume. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE PROPER OS TRANSFER -- THE WIDTH RESOLUTION, THE LOCALITY THEOREM SHAPE, THE ODD-SECTOR LOCK, THE UNIT-CELL MONODROMY, THE DEGENERACY MECHANISM and THE B190 CHECK VERDICT AND THE TWO-FORK RESOLUTION anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


# ---------------------------------------------------------------------------
# the claims: every expected value the gates compare against, in ONE place
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims: dict = {
        # A -- the authority pins.
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        # B -- the banner's declared status flags.
        "objects_registered": False,
        "dispersion_claimed": DISPERSION_CLAIMED,
        "mass_scales_claimed": MASS_SCALES_CLAIMED,
        "physical_time_step_claimed": PHYSICAL_TIME_STEP_CLAIMED,
        "transfer_positivity_claimed": TRANSFER_POSITIVITY_CLAIMED,
        "variant_is_landed_claimed": VARIANT_IS_LANDED_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        # C -- the two-sided construction control and the T = 12 structure.
        "citation_pins": True,
        "hodge_display_residual": ZERO_RESIDUAL,
        "fork_asymmetry": dict(FORK_ASYMMETRY),
        "fork_covariance": dict(FORK_COVARIANCE),
        "landed_minor_1": B188_CORE_MINOR_1,
        "landed_minor_2": B188_CORE_MINOR_2,
        "variant_minor_1": VARIANT_CORE_MINOR_1,
        "dk_square": DK_SQUARE_RESIDUAL,
        "hodge_covariance": HODGE_COVARIANCE_RESIDUAL,
        "action_covariance": ACTION_COVARIANCE_RESIDUAL,
        "cross_block": CROSS_BLOCK_NONZEROS,
        "core_signs": CORE_SIGNS,
        "span_rank": FULL_SPAN_RANK,
        "schur_nonzeros": SCHUR_NONZEROS,
        "hodge_robust_under_forensic": HODGE_ROBUST_UNDER_FORENSIC,
        "volume_sensitive": VOLUME_SENSITIVE,
        "check_b105_factors": CHECK_B105_FACTORS,
        "check_fallback_factors": CHECK_FALLBACK_FACTORS,
        # D -- the refutation and its mechanism.
        "l1_asymmetry": dict(L1_ASYMMETRY),
        "l2_asymmetry": dict(L2_ASYMMETRY),
        "core_witnesses": dict(CORE_WITNESSES),
        "tau2_nonzeros": dict(TAU2_ACTION_NONZEROS),
        "tau2_pairs": dict(TAU2_ACTION_PAIRS),
        "tau2_witness": TAU2_ACTION_WITNESS,
        "tau2_inverse_nonzero": dict(TAU2_INVERSE_NONZERO),
        "global_mechanism_is_sufficient": GLOBAL_MECHANISM_IS_SUFFICIENT,
        # E -- locality, rigidity and the two boundary layers.
        "step_equalities": dict(STEP_EQUALITIES),
        "gram_inhomogeneity": GRAM_INHOMOGENEITY,
        "gram_witness": GRAM_WITNESS,
        "factor_pattern": FACTOR_PATTERN,
        "even_quadratics": EVEN_QUADRATICS,
        "odd_quadratics": ODD_QUADRATICS,
        "even_deep_quartic": EVEN_DEEP_QUARTIC,
        "even_far_quartic": EVEN_FAR_QUARTIC,
        "odd_layer_quartics": (ODD_NEAR_QUARTIC, ODD_MIRROR_QUARTIC),
        "odd_deep_quartic": ODD_DEEP_QUARTIC,
        "mirror_residual": MIRROR_RESIDUAL,
        # F -- the unit-cell monodromy.
        "primitivity_nonzeros": PRIMITIVITY_NONZEROS,
        "primitivity_witnesses": dict(PRIMITIVITY_WITNESSES),
        "parity_independent": True,
        "monodromy_factors": MONODROMY_FACTORS,
        "discriminants": dict(DISCRIMINANTS),
        "discriminant_factorizations": dict(DISCRIMINANT_FACTORIZATIONS),
        "trace_exceeds_twice_leading": True,
        "reciprocal_form": True,
        "trace_ratio_gap": TRACE_RATIO_GAP,
        "two_cosh": dict(TWO_COSH),
        "coefficient_identity": True,
        # G -- the commutant.
        "u_isometry": U_ISOMETRY_RESIDUAL,
        "u_commutator": U_COMMUTATOR_RESIDUAL,
        "u_off_sector": U_OFF_SECTOR_NONZEROS,
        "u_sector_factors": dict(U_SECTOR_FACTORS),
        "s_relations": (S_COMMUTATOR_RESIDUAL, S_SQUARE_RESIDUAL,
                        S_FOURTH_RESIDUAL),
        "s_gram_defect": S_GRAM_DEFECT,
        "s_gram_witness": S_GRAM_WITNESS,
        "momentum_factors": dict(MOMENTUM_FACTORS),
        "momentum_equality_is_group_forced": MOMENTUM_EQUALITY_IS_GROUP_FORCED,
        "census_size": CENSUS_SIZE,
        "census_commutants": CENSUS_COMMUTANTS,
        "census_isometries": CENSUS_ISOMETRIES,
        "reflection_commutator": REFLECTION_COMMUTATOR_NONZEROS,
        "reflection_witness": REFLECTION_WITNESS,
        "core_gram_symmetry": CORE_GRAM_SYMMETRY_RESIDUAL,
        "konly_difference": KONLY_DIFFERENCE,
        "consistent_difference": CONSISTENT_DIFFERENCE,
        "consistent_charpoly_same": True,
        "similarity_residual": SIMILARITY_RESIDUAL,
        # H -- the note, the fence and the nsimplify absence.
        "required_scope_keys": SCOPE_KEYS,
        "nsimplify_calls": 0,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "claim_objects_registered":
        # THE BANNER DENIED: the imposed objects asserted REGISTERED, which zero
        # registered and zero adopted objects forbid.
        claims["objects_registered"] = True
    elif mutation == "claim_dispersion_derived":
        # THE FIRST HEADLINE READING ASSERTED.  E(0) = theta_2 and E(pi) =
        # theta_1 is a way of TALKING about two momentum sectors of an 8 x 8
        # matrix; no propagating mode and no lattice dispersion relation is
        # derived anywhere in this block.
        claims["dispersion_claimed"] = True
    elif mutation == "claim_mass_scales_derived":
        # THE SECOND: theta_1 and theta_2 called MASSES.  They are logarithms of
        # eigenvalues of a constructed matrix, with no continuum limit, no unit
        # and no mass anywhere in the block.
        claims["mass_scales_claimed"] = True
    elif mutation == "claim_physical_time_step":
        # THE THIRD: the two-slice unit cell asserted to BE the physical time
        # step of a theory.  It is the period of the staggering of THIS carrier.
        claims["physical_time_step_claimed"] = True
    elif mutation == "claim_transfer_positivity_derived":
        # THE FOURTH, AND THE BIGGEST OVERREAD RISK IN THE BLOCK: the proven
        # spectral positivity asserted to BE reflection-positive transfer.  The
        # OS reconstruction that would license the word IS NOT PERFORMED.
        claims["transfer_positivity_claimed"] = True
    elif mutation == "claim_variant_is_landed":
        # THE DISCLOSURE DENIED: the wrap-edge family asserted to be Block 188's
        # landed object.  It is measured to be a different matrix at the same
        # core, and 144 against 160 is the fork.
        claims["variant_is_landed_claimed"] = True
    elif mutation == "claim_generality":
        # ONE FIXTURE OVERSOLD.  Every statement here is measured at (9/20,
        # 5/13) and NOWHERE ELSE; there is no bracket, no ray and no edge.
        claims["generality_claimed"] = True
    elif mutation == "break_hodge_display":
        # THE DISPLAY UNGATED: the note's inline matrix asserted to differ from
        # the import.  If those sixteen numbers are not the landed ones, every
        # coefficient below belongs to some other construction -- which is
        # exactly the failure mode the adversarial check fell into.
        claims["hodge_display_residual"] = 1
    elif mutation == "break_fork_pair":
        # THE FORK COLLAPSED: the wrap placement asserted to give Block 188's
        # 144.  It gives 160, and the whole variant disclosure rests on that.
        claims["fork_asymmetry"] = dict(FORK_ASYMMETRY, wrap_wTm1=144)
    elif mutation == "break_fork_covariance":
        # THE VARIANT DISQUALIFIED: the wrap placement asserted NOT to be
        # Ps-covariant.  Both placements satisfy Ps Q Ps = Q^T at zero, which is
        # what makes the variant admissible rather than broken.
        claims["fork_covariance"] = dict(FORK_COVARIANCE, wrap_wTm1=16)
    elif mutation == "break_landed_control":
        # THE CONTROL DENIED AT ITS LAST DIGIT: if the landed placement does not
        # reproduce Block 188's core minor exactly, this rebuild is not a variant
        # of their object at all and nothing here attaches to theirs.
        claims["landed_minor_1"] = B188_CORE_MINOR_1 + 1
    elif mutation == "break_variant_difference":
        # THE DISCLOSURE MADE VACUOUS FROM THE OTHER SIDE: the wrap placement
        # asserted to give the SAME core minor as the landed one.  It does not,
        # and a disclosure that no measurement could detect is not a disclosure.
        claims["variant_minor_1"] = B188_CORE_MINOR_1
    elif mutation == "break_dk_square":
        # THE COMPLEX PROPERTY DENIED: d_K^2 asserted nonzero, which would mean
        # the grade-raising part is not a differential and the whole
        # Dirac-Kahler structure is absent at this width.
        claims["dk_square"] = 8
    elif mutation == "break_cross_block":
        # THE HALF-SPLIT DENIED: the cross block between the physical span and
        # its image asserted nonempty, which would mean the two halves are
        # coupled and the reflection pairing is not block-diagonal.
        claims["cross_block"] = 16
    elif mutation == "break_core_positivity":
        # THE CORE GRAM DENIED AT ITS THIRD MINOR: asserted NEGATIVE, which the
        # exact determinants over QQ forbid at every adjacent core.
        claims["core_signs"] = (1, 1, -1, 1, 1, 1, 1, 1)
    elif mutation == "break_span_rank":
        # THE STATE SPACE INFLATED: the five-slice span asserted to have full
        # rank 20.  It has rank EXACTLY 8 -- the OS space does not grow with the
        # span, and every core is a frame for the same eight directions.
        claims["span_rank"] = 20
    elif mutation == "break_schur_complement":
        # THE FRAME STATEMENT DENIED: the Schur complement of one core inside the
        # full span asserted nonzero, which would mean the span carries
        # directions the core does not.
        claims["schur_nonzeros"] = 8
    elif mutation == "break_hodge_robustness":
        # THE CHECK'S OWN REPRODUCTION EXPLAINED AWAY: the forensic variant
        # asserted NOT to give this block's spectra.  It gives them exactly, and
        # that is the reason the check could reproduce every headline
        # coefficient while believing it had refuted them.
        claims["hodge_robust_under_forensic"] = False
    elif mutation == "break_volume_sensitivity":
        # THE DISPLAY MADE DECORATIVE: the spectra asserted INVARIANT under the
        # volume too, which would mean the note need not pin v = 1.  The landed
        # function at v = 12/13 gives different polynomials at every core, and
        # that is the entire C3 discrepancy.
        claims["volume_sensitive"] = False
    elif mutation == "break_check_reproduction":
        # THE DIAGNOSIS DENIED AT ITS LAST DIGIT: the check's own displayed
        # rebuild asserted to be a different polynomial from the one this
        # runner gets at v = 12/13.  Reproducing THEIR numbers is what proves
        # the discrepancy is a volume convention and not a disputed measurement.
        claims["check_b105_factors"] = (
            (CHECK_B105_FACTORS[0][0] + 1,) + CHECK_B105_FACTORS[0][1:],
        ) + CHECK_B105_FACTORS[1:]
    elif mutation == "break_l1_asymmetry":
        # THE ONE-STEP REFUTATION ERASED: L_1 asserted symmetric at t0 = 1, which
        # would mean the naive one-step transfer pairing is fine after all.
        claims["l1_asymmetry"] = {**L1_ASYMMETRY, 1: 0}
    elif mutation == "break_l2_asymmetry":
        # THE TWO-STEP REFUTATION FLATTENED: the t0 = 3 count asserted to be the
        # generic 40, which would erase the measured inhomogeneity of the cores.
        claims["l2_asymmetry"] = {**L2_ASYMMETRY, 3: 40}
    elif mutation == "break_core_witness":
        # THE PROOF ITSELF DENIED AT ONE DIGIT: one of the six exact core
        # witnesses altered.  They ARE the proof of the refutation, so a wrong
        # witness is a wrong theorem.
        row, column, value = CORE_WITNESSES[(2, 2)]
        claims["core_witnesses"] = {
            **CORE_WITNESSES, (2, 2): (row, column, value + 1)}
    elif mutation == "break_commutator_support":
        # THE TWO-LAYER MECHANISM CENSUS FLATTENED: the landed placement asserted
        # to carry the wrap placement's 26 slice pairs.  It carries 28, and the
        # sign layer is visible in the mechanism as well as in the asymmetry.
        claims["tau2_pairs"] = dict(TAU2_ACTION_PAIRS, landed_w3=26)
    elif mutation == "break_mechanism_sufficiency":
        # THE ADVERSARIAL CHECK'S C2 CORRECTION DENIED, AND THIS IS THE MUTATION
        # THAT GUARDS IT: the global commutator asserted to PROVE the restricted
        # core asymmetry by itself.  Symmetry after restriction to one 8-vector
        # core requires only the PROJECTED block to vanish, so the global
        # statement is a mechanism and the six core witnesses are the proof.
        claims["global_mechanism_is_sufficient"] = True
    elif mutation == "break_matrix_locality":
        # POSITION HOMOGENEITY DENIED: V2 and V4 at T = 16 asserted to differ as
        # matrices.  They are equal entrywise, and that equality -- not a
        # spectral coincidence -- is what makes the step operator local.
        claims["step_equalities"] = dict(
            STEP_EQUALITIES, **{"V2@T16 - V4@T16": 32})
    elif mutation == "break_width_invariance":
        # WIDTH INVARIANCE DENIED: V2 at T = 12 asserted to differ from V2 at
        # T = 16.  If the step matrix moved with the carrier width there would be
        # no bulk object to speak of.
        claims["step_equalities"] = dict(
            STEP_EQUALITIES, **{"V2@T12 - V2@T16": 32})
    elif mutation == "break_gram_inhomogeneity":
        # THE OTHER HALF OF LOCALITY ERASED: the Grams asserted EQUAL as well.
        # They differ at 56 entries, and the whole point is that the boundary
        # layer lives in the metric data while the dynamics is homogeneous.
        claims["gram_inhomogeneity"] = 0
    elif mutation == "break_factor_pattern":
        # THE RATIONAL STRUCTURE DENIED: the characteristic polynomial asserted
        # irreducible of degree 8 at every core, which would remove the parity
        # split the entire E family is about.
        claims["factor_pattern"] = (8,)
    elif mutation == "break_even_quadratics":
        # THE EVEN QUADRATIC RIGIDITY DENIED at its first coefficient.
        claims["even_quadratics"] = ((5676, 5634, -6845), EVEN_QUADRATICS[1])
    elif mutation == "break_even_rigidity":
        # THE INTERIOR EVEN QUARTIC DENIED: the deep even value altered, which
        # would break the position- and width-invariance of the even sector.
        claims["even_deep_quartic"] = tuple(
            [EVEN_DEEP_QUARTIC[0] + 1] + list(EVEN_DEEP_QUARTIC[1:]))
    elif mutation == "break_far_boundary_layer":
        # THIS BLOCK'S OWN WORDING CORRECTION DENIED, AND THIS IS THE MUTATION
        # THAT GUARDS IT: the even quartic asserted RIGID at the far seam too.
        # At t0 = T/2 - 2 it takes a DIFFERENT value at all three widths, and the
        # earlier claim that the even sector is rigid everywhere was too strong.
        claims["even_far_quartic"] = EVEN_DEEP_QUARTIC
    elif mutation == "break_odd_near_layer":
        # THE NEAR-SEAM ODD VALUE DENIED, which is the layer's near end.
        near, mirror = ODD_NEAR_QUARTIC, ODD_MIRROR_QUARTIC
        claims["odd_layer_quartics"] = (
            tuple([near[0] + 1] + list(near[1:])), mirror)
    elif mutation == "break_odd_deep_lock":
        # THE ODD BULK LIMIT DENIED: the deep value asserted different, which
        # would mean the odd sector never converges and there is no bulk
        # transfer content at all.
        claims["odd_deep_quartic"] = tuple(
            [ODD_DEEP_QUARTIC[0] + 1] + list(ODD_DEEP_QUARTIC[1:]))
    elif mutation == "break_mirror_covariance":
        # THE REFLECTION RELATION DENIED: q_j = (-1)^j p_(8-j) asserted to fail.
        # It holds at all nine coefficients at both widths, and it is the exact
        # statement that spec(V_mirror) = {-1/lambda}.
        claims["mirror_residual"] = 1
    elif mutation == "break_monodromy_primitive":
        # THE PRIMITIVITY DENIED: W asserted EQUAL to V^2, which would make the
        # monodromy a derived object and this family redundant.
        claims["primitivity_nonzeros"] = 0
    elif mutation == "break_monodromy_witness":
        # THE PRIMITIVITY WITNESS ALTERED at one digit.
        claims["primitivity_witnesses"] = {
            **PRIMITIVITY_WITNESSES, 4: PRIMITIVITY_WITNESSES[4] + 1}
    elif mutation == "break_parity_independence":
        # THE PARITY RESULT DENIED: the odd and even deep cores asserted to carry
        # different monodromy spectra.  They carry the same one, and that is what
        # makes the monodromy a bulk invariant rather than a core-local number.
        claims["parity_independent"] = False
    elif mutation == "break_monodromy_spectrum":
        # THE HEADLINE SPECTRUM ALTERED at one coefficient.
        claims["monodromy_factors"] = (
            ((MONODROMY_HEAVY[0] + 1,) + MONODROMY_HEAVY[1:], 2),
            (MONODROMY_LIGHT, 2))
    elif mutation == "break_discriminant_positivity":
        # THE POSITIVITY PROOF'S FIRST LEG DENIED: a discriminant asserted to be
        # a different integer.  These are exact integers with exact
        # factorizations, and the reality of the roots is decided by them.
        claims["discriminants"] = {
            **DISCRIMINANTS,
            MONODROMY_HEAVY: DISCRIMINANTS[MONODROMY_HEAVY] + 1}
    elif mutation == "break_trace_bound":
        # THE SECOND LEG DENIED: the traces asserted NOT to exceed twice the
        # leading coefficient, which is what forces both roots POSITIVE rather
        # than merely real.
        claims["trace_exceeds_twice_leading"] = False
    elif mutation == "break_reciprocal_form":
        # THE THIRD LEG DENIED: the constant/leading ratio asserted not to be 1,
        # which is what makes the roots reciprocal pairs and licenses the cosh
        # parametrization at all.
        claims["reciprocal_form"] = False
    elif mutation == "break_trace_ratio_distinct":
        # THE FOURTH LEG DENIED: the two trace ratios asserted EQUAL, which would
        # collapse the four roots to two and destroy the two-scale statement.
        claims["trace_ratio_gap"] = 0
    elif mutation == "break_coefficient_identity":
        # THE STRUCTURAL IDENTITY DENIED: the second monodromy quadratic asserted
        # NOT to be a z^2 - c z + a from the even V-quartic.  It is, exactly, and
        # the odd coefficient b dropping out is the content.
        claims["coefficient_identity"] = False
    elif mutation == "break_u_isometry":
        # THE GRADING OPERATOR DISQUALIFIED: U asserted NOT to preserve the core
        # Gram, which would make the sector split meaningless on the pairing.
        claims["u_isometry"] = 32
    elif mutation == "break_sector_assignment":
        # THE MASS-SCALE GRADING SWAPPED: the heavy and light sectors exchanged.
        # The assignment is the whole content of the degeneracy mechanism.
        claims["u_sector_factors"] = {1: (MONODROMY_HEAVY, 2),
                                      -1: (MONODROMY_LIGHT, 2)}
    elif mutation == "break_s_relations":
        # THE SECOND COMMUTANT DENIED: [W, S] asserted nonzero, which would erase
        # the check's own P2 finding and the momentum resolution with it.
        claims["s_relations"] = (32, S_SQUARE_RESIDUAL, S_FOURTH_RESIDUAL)
    elif mutation == "break_s_isometry":
        # THE CHECK'S P2 QUALIFIER ERASED: S asserted to BE a Gram isometry.  It
        # is not -- 64 entries -- and that is exactly why it organizes the
        # spectrum without being a symmetry of the OS pairing.
        claims["s_gram_defect"] = 0
    elif mutation == "break_momentum_degeneracy":
        # THE ADDITIONAL ISOSPECTRALITY DOWNGRADED TO A GROUP FACT, AND THIS IS
        # THE MUTATION THAT GUARDS THE CHECK'S OWN QUALIFIER: the p = 0 / p = 2
        # equality asserted FORCED by the symmetry.  It is not; it is a measured
        # coincidence of this construction and is declared as one.
        claims["momentum_equality_is_group_forced"] = True
    elif mutation == "break_census_commutants":
        # THE EXHAUSTIVE SWEEP'S RESULT SHRUNK: the commutant asserted to be
        # {I, U} only, which would drop S and with it the momentum resolution.
        claims["census_commutants"] = ("I", "U")
    elif mutation == "break_census_isometries":
        # AND INFLATED FROM THE OTHER SIDE: every W-commutant asserted to be a
        # Gram isometry.  Exactly two of the four are, and the gap between 4 and
        # 2 is the useful part of the census.
        claims["census_isometries"] = CENSUS_COMMUTANTS
    elif mutation == "break_reflection_refutation":
        # THE REFUTED CANDIDATE REVIVED: the spatial reflection asserted to
        # commute with W.  It does not, at 16 entries with an exact witness, and
        # the campaign's own P2 refutation depends on that.
        claims["reflection_commutator"] = 0
    elif mutation == "break_transpose_robustness":
        # CONVENTION ROBUSTNESS DENIED: the consistently transposed pairing
        # asserted to change charpoly(W).  It cannot, because the transposed
        # operator is K_c^-1 W^T K_c, a similarity.
        claims["consistent_charpoly_same"] = False
    elif mutation == "break_konly_vacuity":
        # THE CHECK'S P1 CARRIED UNCORRECTED, AND THIS IS THE MUTATION THAT
        # GUARDS THIS BLOCK'S SECOND CORRECTION: the K-only transposition
        # asserted to change the operator.  K_c is EXACTLY SYMMETRIC here, so the
        # K-only transposition is the identity operation and changes nothing --
        # the check's 64-entry spectrum change does not occur on this
        # construction.
        claims["konly_difference"] = 64
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    elif mutation == "break_nsimplify_absence":
        # THE HAZARD DECLARED PRESENT: a nonzero nsimplify count asserted, which
        # the source-token census forbids.
        claims["nsimplify_calls"] = 1
    return claims


# ---------------------------------------------------------------------------
# the measurement pass: every gate reads it, no gate feeds it
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    note_at_final_path: bool
    scope: dict
    banners: dict
    citation_pins: dict
    # C
    hodge_display_residual: int
    imported_hodge: sp.Matrix
    fork_asymmetry: dict
    fork_covariance: dict
    landed_minors: tuple
    variant_minor_1: object
    dk_square: int
    hodge_covariance: int
    action_covariance: int
    cross_block: int
    core_signs: dict
    span_rank: int
    schur_nonzeros: int
    schur_shape: tuple
    hodge_robust_under_forensic: bool
    volume_sensitive: bool
    check_b105_factors: tuple
    check_fallback_factors: tuple
    # D
    l1_asymmetry: dict
    l2_asymmetry: dict
    core_witnesses: dict
    tau2_nonzeros: dict
    tau2_pairs: dict
    tau2_witness: object
    tau2_inverse_nonzero: dict
    # E
    step_equalities: dict
    gram_inhomogeneity: int
    gram_witness: object
    core_factors: dict
    mirror_residuals: dict
    # F
    primitivity_nonzeros: dict
    primitivity_witnesses: dict
    monodromy_factors: dict
    discriminants: dict
    discriminant_factorizations: dict
    trace_exceeds_twice_leading: bool
    reciprocal_form: bool
    trace_ratio_gap: int
    two_cosh: dict
    coefficient_identity: bool
    # G
    u_isometry: int
    u_commutator: int
    u_off_sector: int
    u_sector_factors: dict
    s_relations: tuple
    s_gram_defect: int
    s_gram_witness: object
    momentum_factors: dict
    census_size: int
    census_commutants: tuple
    census_isometries: tuple
    reflection_commutator: int
    reflection_witness: object
    core_gram_symmetry: int
    konly_difference: int
    consistent_difference: int
    consistent_charpoly_same: bool
    similarity_residual: int
    # H
    nsimplify_calls: int
    elapsed_note: str


def core_operators(width: int, inverse: sp.Matrix, core: int) -> dict:
    """K_c, its exact inverse, L_1, L_2, V and W at one core.  THE ONE PLACE the
    step and the monodromy are formed, so no family can build them differently."""
    gram = shifted_pairing(width, inverse, core, 0)
    gram_inverse = exact_inverse(gram)
    first = shifted_pairing(width, inverse, core, 1)
    second = shifted_pairing(width, inverse, core, 2)
    return {"K": gram, "Kinv": gram_inverse, "L1": first, "L2": second,
            "V": sp.expand(gram_inverse * first),
            "W": sp.expand(gram_inverse * second)}


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    # --- THE ONE IMPORT, AND THE DISPLAY GATED AGAINST IT ------------------
    imported = imported_shear_block(FIXTURE_SHEAR)
    hodge_display_residual = residual_count(imported - DISPLAYED_HODGE)

    # --- THE HEAVY PASS.  Every action and every inverse in this block is
    # built EXACTLY ONCE here and shared by every family below.  The T = 16
    # (64 x 64) and T = 20 (80 x 80) exact rational inverses are the expensive
    # objects and neither is ever recomputed.
    actions: dict = {}
    inverses: dict = {}
    for width in WIDTHS:
        actions[width] = build_width_action(
            width, FIXTURE_MASS, imported, width - 1)
        inverses[width] = exact_inverse(actions[width]["action"])
    landed8 = build_width_action(
        MECHANISM_WIDTH, FIXTURE_MASS, imported, LANDED_SIGN_TIME)
    landed8_inverse = exact_inverse(landed8["action"])

    # --- C: THE SIGN-LAYER FORK, MEASURED AS A PAIR ------------------------
    fork_asymmetry = {
        "landed_w3": residual_count(
            landed8["action"] - landed8["action"].T),
        "wrap_wTm1": residual_count(
            actions[8]["action"] - actions[8]["action"].T)}
    fork_covariance = {
        "landed_w3": residual_count(
            landed8["reflection"] * landed8["action"] * landed8["reflection"]
            - landed8["action"].T),
        "wrap_wTm1": residual_count(
            actions[8]["reflection"] * actions[8]["action"]
            * actions[8]["reflection"] - actions[8]["action"].T)}
    landed_core = shifted_pairing(8, landed8_inverse, 1, 0)
    landed_minors = leading_minors(landed_core[:2, :2])
    variant_core = shifted_pairing(8, inverses[8], 1, 0)
    variant_minor_1 = exact_determinant(variant_core[:1, :1])

    # --- C: THE T = 12 STRUCTURE -------------------------------------------
    structure = actions[STRUCTURE_WIDTH]
    dk_square = residual_count(structure["raising"] * structure["raising"])
    hodge_covariance = residual_count(
        structure["reflection"] * structure["hodge"] * structure["reflection"]
        - structure["hodge"])
    action_covariance = residual_count(
        structure["reflection"] * structure["action"] * structure["reflection"]
        - structure["action"].T)
    physical = tuple(site_index(STRUCTURE_WIDTH, t, x)
                     for t in FULL_SPAN_SLICES for x in range(SPACE_EXTENT))
    image = tuple(site_index(STRUCTURE_WIDTH, t + STRUCTURE_HALF + 1, x)
                  for t in range(len(FULL_SPAN_SLICES))
                  for x in range(SPACE_EXTENT))
    cross_block = sum(
        1 for row in physical for column in image
        if structure["action"][row, column] != 0)
    core_signs = {}
    for core in ADJACENT_CORES:
        gram = shifted_pairing(STRUCTURE_WIDTH, inverses[STRUCTURE_WIDTH],
                               core, 0)
        core_signs[core] = (residual_count(gram - gram.T),
                            exact_rank(gram),
                            minor_signs(leading_minors(gram)))
    span = span_gram(STRUCTURE_WIDTH, inverses[STRUCTURE_WIDTH],
                     FULL_SPAN_SLICES)
    span_rank = exact_rank(span)
    corner = span[:8, :8]
    schur = sp.expand(span[8:, 8:]
                      - span[8:, :8] * exact_inverse(corner) * span[:8, 8:])
    schur_nonzeros = residual_count(schur)

    # --- C: THE HODGE FORK, RESOLVED ON BOTH SIDES -------------------------
    def control_spectra(block: sp.Matrix) -> dict:
        """A whole T = 12 rebuild at a DECLARED CONTROL shear block, returning
        the V and W factorizations at the three bulk cores.  Nothing is claimed
        of any control block; they exist to locate the check's rebuilds."""
        built = build_width_action(
            STRUCTURE_WIDTH, FIXTURE_MASS, block, STRUCTURE_WIDTH - 1)
        inverse = exact_inverse(built["action"])
        return {core: (char_factors(
            core_operators(STRUCTURE_WIDTH, inverse, core)["V"]),
            char_factors(core_operators(STRUCTURE_WIDTH, inverse, core)["W"]))
            for core in CONTROL_CORES}

    landed_spectra = control_spectra(imported)
    forensic_spectra = control_spectra(FORENSIC_HODGE)
    volume_spectra = control_spectra(
        b128.block105.shear_hodge(FIXTURE_SHEAR, CONTROL_VOLUME))
    fallback_spectra = control_spectra(FALLBACK_HODGE)
    hodge_robust = bool(forensic_spectra == landed_spectra)
    volume_sensitive = bool(all(
        volume_spectra[core] != landed_spectra[core] for core in CONTROL_CORES))

    # --- THE CORE TABLE, BUILT ONCE AND READ BY D, E, F AND G --------------
    cores: dict = {}
    for width, core in ALL_PROBED_CORES:
        cores[(width, core)] = core_operators(width, inverses[width], core)
    for core in REFUTATION_CORES:
        key = (STRUCTURE_WIDTH, core)
        if key not in cores:
            cores[key] = core_operators(
                STRUCTURE_WIDTH, inverses[STRUCTURE_WIDTH], core)
    for core in DEEP_CORES:
        key = (MONODROMY_WIDTH, core)
        if key not in cores:
            cores[key] = core_operators(
                MONODROMY_WIDTH, inverses[MONODROMY_WIDTH], core)

    # --- D: THE REFUTATION AND ITS MECHANISM -------------------------------
    l1_asymmetry: dict = {}
    l2_asymmetry: dict = {}
    core_witnesses: dict = {}
    for core in REFUTATION_CORES:
        built = cores[(STRUCTURE_WIDTH, core)]
        for step, target in ((1, l1_asymmetry), (2, l2_asymmetry)):
            pairing = built[f"L{step}"]
            defect = sp.expand(pairing - pairing.T)
            target[core] = nonzero_entries(defect)
            core_witnesses[(core, step)] = first_nonzero(defect)
    tau2_nonzeros: dict = {}
    tau2_pairs: dict = {}
    tau2_inverse_nonzero: dict = {}
    tau2_witnesses: dict = {}
    shift = time_shift(MECHANISM_WIDTH, 2)
    for label, built, inverse in (
            ("landed_w3", landed8, landed8_inverse),
            ("wrap_wTm1", actions[8], inverses[8])):
        commutator = sp.expand(shift * built["action"]
                               - built["action"] * shift)
        tau2_nonzeros[label] = nonzero_entries(commutator)
        tau2_pairs[label] = len(slice_pair_support(commutator))
        tau2_witnesses[label] = commutator[0, 1]
        tau2_inverse_nonzero[label] = residual_count(
            sp.expand(shift * inverse - inverse * shift))
    tau2_witness = (tau2_witnesses["landed_w3"]
                    if tau2_witnesses["landed_w3"] == tau2_witnesses["wrap_wTm1"]
                    else sp.Integer(0))

    # --- E: LOCALITY, RIGIDITY AND THE TWO BOUNDARY LAYERS -----------------
    step_equalities = {
        "V2@T16 - V4@T16": residual_count(
            cores[(16, 2)]["V"] - cores[(16, 4)]["V"]),
        "V2@T12 - V2@T16": residual_count(
            cores[(12, 2)]["V"] - cores[(16, 2)]["V"]),
        "V1@T12 - V1@T16": residual_count(
            cores[(12, 1)]["V"] - cores[(16, 1)]["V"]),
    }
    gram_defect = sp.expand(cores[(16, 2)]["K"] - cores[(16, 4)]["K"])
    gram_inhomogeneity = nonzero_entries(gram_defect)
    gram_witness = first_nonzero(gram_defect)[2]
    core_factors = {key: char_factors(value["V"])
                    for key, value in cores.items()}
    variable = sp.Symbol("z")
    mirror_residuals = {}
    for width, first, second in MIRROR_PAIRS:
        low = primitive_coefficients(
            cores[(width, first)]["V"].charpoly(variable).as_expr(),
            variable)[::-1]
        high = primitive_coefficients(
            cores[(width, second)]["V"].charpoly(variable).as_expr(),
            variable)[::-1]
        mirror_residuals[(width, first, second)] = sum(
            1 for j in range(9) if high[j] != (-1) ** j * low[8 - j])

    # --- F: THE UNIT-CELL MONODROMY ----------------------------------------
    primitivity_nonzeros: dict = {}
    primitivity_witnesses: dict = {}
    monodromy_factors: dict = {}
    for core in DEEP_CORES:
        built = cores[(MONODROMY_WIDTH, core)]
        defect = sp.expand(built["W"] - built["V"] * built["V"])
        primitivity_nonzeros[core] = nonzero_entries(defect)
        primitivity_witnesses[core] = defect[0, 4]
        monodromy_factors[core] = char_factors(built["W"])
    quadratics = tuple(sorted(
        {coefficients
         for coefficients, _ in monodromy_factors[DEEP_CORES[0]]
         if len(coefficients) == 3}))
    discriminants = {
        coefficients: int(coefficients[1] ** 2
                          - 4 * coefficients[0] * coefficients[2])
        for coefficients in quadratics}
    discriminant_factorizations = {
        coefficients: {int(prime): int(power) for prime, power
                       in sp.factorint(value).items()}
        for coefficients, value in discriminants.items()}
    trace_exceeds = all(-coefficients[1] > 2 * coefficients[0]
                        for coefficients in quadratics)
    reciprocal_form = all(coefficients[2] == coefficients[0]
                          for coefficients in quadratics)
    ordered = sorted(quadratics)
    trace_ratio_gap = int(
        -ordered[0][1] * ordered[1][0] + ordered[1][1] * ordered[0][0])
    two_cosh = {coefficients: sp.Rational(-coefficients[1], coefficients[0])
                for coefficients in quadratics}
    even_quartic = quartic_of(core_factors[(MONODROMY_WIDTH, 4)])
    coefficient_identity = bool(
        len(even_quartic) == 5
        and (even_quartic[0], -even_quartic[2], even_quartic[4]) in quadratics)

    # --- G: THE COMMUTANT ---------------------------------------------------
    commutant = cores[(MONODROMY_WIDTH, COMMUTANT_CORE)]
    gram, monodromy = commutant["K"], commutant["W"]
    identity = sp.eye(8)
    two_site = spatial_shift(COMMUTANT_CORE, 2)
    one_site = spatial_shift(COMMUTANT_CORE, 1)
    reflection = spatial_reflection(COMMUTANT_CORE)
    u_isometry = residual_count(two_site.T * gram * two_site - gram)
    u_commutator = residual_count(monodromy * two_site - two_site * monodromy)
    u_off_sector = residual_count(
        (identity - two_site) / 2 * monodromy * (identity + two_site) / 2)
    u_sector_factors = {
        sign: char_factors(sector_block(
            sp.expand((identity + sign * two_site) / 2), monodromy))
        for sign in (1, -1)}
    s_relations = (
        residual_count(monodromy * one_site - one_site * monodromy),
        residual_count(one_site * one_site - two_site),
        residual_count(one_site ** 4 - identity))
    s_defect = sp.expand(one_site.T * gram * one_site - gram)
    s_gram_defect = nonzero_entries(s_defect)
    s_gram_witness = first_nonzero(s_defect)[2]
    momentum_factors = {
        "p0": char_factors(nullspace_block(one_site - identity, monodromy)),
        "p2": char_factors(nullspace_block(one_site + identity, monodromy)),
        "p13": char_factors(
            nullspace_block(one_site * one_site + identity, monodromy)),
    }
    named = {"I": identity, "S": one_site, "U": two_site,
             "S^3": sp.expand(one_site ** 3)}
    candidates = candidate_monomials(COMMUTANT_CORE)
    commutant_names: set = set()
    isometry_names: set = set()
    for candidate in candidates:
        if residual_count(monodromy * candidate - candidate * monodromy):
            continue
        label = next(
            (name for name, matrix in named.items()
             if residual_count(candidate - matrix) == 0), "OTHER")
        commutant_names.add(label)
        if residual_count(candidate.T * gram * candidate - gram) == 0:
            isometry_names.add(label)
    reflection_defect = sp.expand(
        monodromy * reflection - reflection * monodromy)
    reflection_commutator = nonzero_entries(reflection_defect)
    reflection_witness = reflection_defect[0, 5]
    core_gram_symmetry = residual_count(gram - gram.T)
    konly = sp.expand(exact_inverse(gram.T) * commutant["L2"])
    consistent = sp.expand(exact_inverse(gram.T) * commutant["L2"].T)
    konly_difference = residual_count(konly - monodromy)
    consistent_difference = residual_count(consistent - monodromy)
    consistent_charpoly_same = bool(
        char_factors(consistent) == monodromy_factors[COMMUTANT_CORE])
    similarity_residual = residual_count(
        consistent - exact_inverse(gram) * monodromy.T * gram)

    banners = {
        "imposed": len(IMPOSED_OBJECTS),
        "registered": len(REGISTERED_OBJECTS),
        "adopted": len(ADOPTED_OBJECTS),
        "dispersion_claimed": DISPERSION_CLAIMED,
        "mass_scales_claimed": MASS_SCALES_CLAIMED,
        "physical_time_step_claimed": PHYSICAL_TIME_STEP_CLAIMED,
        "transfer_positivity_claimed": TRANSFER_POSITIVITY_CLAIMED,
        "variant_is_landed_claimed": VARIANT_IS_LANDED_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        "global_mechanism_is_sufficient": GLOBAL_MECHANISM_IS_SUFFICIENT,
        "momentum_equality_is_group_forced": MOMENTUM_EQUALITY_IS_GROUP_FORCED,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
    }
    b189 = landed_text(BLOCK189_NOTE)
    b188 = landed_text(BLOCK188_NOTE)
    campaign = landed_text(CAMPAIGN_NOTE)
    citation_pins = {
        "b189_note_readable": len(b189) > 0,
        "b188_note_readable": len(b188) > 0,
        "b188_asymmetry_pinned": "144" in b188,
        "campaign_readable": len(campaign) > 0,
        "campaign_anchor": "THE B190 CHECK VERDICT" in campaign,
    }

    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        hodge_display_residual=hodge_display_residual,
        imported_hodge=imported,
        fork_asymmetry=fork_asymmetry,
        fork_covariance=fork_covariance,
        landed_minors=landed_minors,
        variant_minor_1=variant_minor_1,
        dk_square=dk_square,
        hodge_covariance=hodge_covariance,
        action_covariance=action_covariance,
        cross_block=cross_block,
        core_signs=core_signs,
        span_rank=span_rank,
        schur_nonzeros=schur_nonzeros,
        schur_shape=(schur.rows, schur.cols),
        hodge_robust_under_forensic=hodge_robust,
        volume_sensitive=volume_sensitive,
        check_b105_factors=tuple(c for c, _ in volume_spectra[2][0]),
        check_fallback_factors=tuple(c for c, _ in fallback_spectra[2][0]),
        l1_asymmetry=l1_asymmetry,
        l2_asymmetry=l2_asymmetry,
        core_witnesses=core_witnesses,
        tau2_nonzeros=tau2_nonzeros,
        tau2_pairs=tau2_pairs,
        tau2_witness=tau2_witness,
        tau2_inverse_nonzero=tau2_inverse_nonzero,
        step_equalities=step_equalities,
        gram_inhomogeneity=gram_inhomogeneity,
        gram_witness=gram_witness,
        core_factors=core_factors,
        mirror_residuals=mirror_residuals,
        primitivity_nonzeros=primitivity_nonzeros,
        primitivity_witnesses=primitivity_witnesses,
        monodromy_factors=monodromy_factors,
        discriminants=discriminants,
        discriminant_factorizations=discriminant_factorizations,
        trace_exceeds_twice_leading=trace_exceeds,
        reciprocal_form=reciprocal_form,
        trace_ratio_gap=trace_ratio_gap,
        two_cosh=two_cosh,
        coefficient_identity=coefficient_identity,
        u_isometry=u_isometry,
        u_commutator=u_commutator,
        u_off_sector=u_off_sector,
        u_sector_factors=u_sector_factors,
        s_relations=s_relations,
        s_gram_defect=s_gram_defect,
        s_gram_witness=s_gram_witness,
        momentum_factors=momentum_factors,
        census_size=len(candidates),
        census_commutants=tuple(sorted(commutant_names)),
        census_isometries=tuple(sorted(isometry_names)),
        reflection_commutator=reflection_commutator,
        reflection_witness=reflection_witness,
        core_gram_symmetry=core_gram_symmetry,
        konly_difference=konly_difference,
        consistent_difference=consistent_difference,
        consistent_charpoly_same=consistent_charpoly_same,
        similarity_residual=similarity_residual,
        nsimplify_calls=nsimplify_occurrences(),
        elapsed_note="",
    )


# ---------------------------------------------------------------------------
# the gates: each reads facts and claims, and NOTHING else
# ---------------------------------------------------------------------------
def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", "the five-pin authority block resolves against origin/main",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", "PARENT_COMMIT is a real 40-hex commit and not a placeholder",
        authority.parent_pin_is_commit)
    checks.check(
        "A-3", f"PARENT_REF {PARENT_REF} resolves to PARENT_COMMIT and it is "
        "an ancestor of HEAD",
        authority.parent_ref_and_ancestry)
    checks.check(
        "A-4", "BOTH Block 189 artifacts are content-bound at the pinned "
        "commit, in the worktree and against their recorded blobs",
        authority.parent_artifact_blobs if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs)
    checks.check(
        "A-5", "the stale pin is a REAL ancestor of HEAD that carries NEITHER "
        "Block 189 artifact",
        authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact)
    checks.check(
        "A-6", f"the ONE landed import is available and "
        f"{len(AUDIT_INPUT_PATHS) - 1} audit inputs are readable",
        authority.machinery_import_landed
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
        and not authority.inputs_missing)

    # --- B: THE BANNER AND THE NOT-CLAIMED KEYS -----------------------------
    checks.check(
        "B-1", f"{facts.banners['imposed']} imposed objects, "
        f"{facts.banners['registered']} registered, "
        f"{facts.banners['adopted']} adopted",
        (facts.banners["registered"] == 0
         and facts.banners["adopted"] == 0
         and facts.banners["imposed"] == len(IMPOSED_OBJECTS))
        == (not claims["objects_registered"]))
    checks.check(
        "B-2", "DISPERSION is declared NOT CLAIMED",
        facts.banners["dispersion_claimed"] == claims["dispersion_claimed"])
    checks.check(
        "B-3", "MASS SCALES are declared NOT CLAIMED",
        facts.banners["mass_scales_claimed"] == claims["mass_scales_claimed"])
    checks.check(
        "B-4", "A PHYSICAL TIME STEP is declared NOT CLAIMED",
        facts.banners["physical_time_step_claimed"]
        == claims["physical_time_step_claimed"])
    checks.check(
        "B-5", "TRANSFER POSITIVITY is declared NOT CLAIMED: the spectral "
        "positivity is proven and the OS reconstruction is NOT performed",
        facts.banners["transfer_positivity_claimed"]
        == claims["transfer_positivity_claimed"])
    checks.check(
        "B-6", "THE WIDTH FAMILY IS DECLARED A VARIANT and is NOT claimed to "
        "be Block 188's landed object",
        facts.banners["variant_is_landed_claimed"]
        == claims["variant_is_landed_claimed"])
    checks.check(
        "B-7", "NO GENERALITY is claimed: one fixture, one carrier family",
        facts.banners["generality_claimed"] == claims["generality_claimed"])
    checks.check(
        "B-8", f"{facts.banners['unsupplied']} gravity structures are "
        "enumerated as NOT SUPPLIED, so the absence is a count",
        facts.banners["unsupplied"] == len(UNSUPPLIED_GRAVITY_STRUCTURES))
    checks.check(
        "B-9", "every imposed object is a nonempty declared string",
        all(isinstance(item, str) and item for item in IMPOSED_OBJECTS))

    # --- C: THE TWO-SIDED CONSTRUCTION CONTROL ------------------------------
    checks.check(
        "C-1", "the landed primary bodies and the campaign anchor are readable "
        "and Block 188's 144 is pinned in their own note",
        all(facts.citation_pins.values()) == claims["citation_pins"])
    checks.check(
        "C-2", "THE DISPLAYED HODGE EQUALS THE IMPORT ENTRYWISE: "
        "I + (25/144)(E11+E22) - (65/144)(E12+E21) against "
        "b128.block105.shear_hodge(5/13, 1)",
        facts.hodge_display_residual == claims["hodge_display_residual"])
    checks.check(
        "C-3", "every entry of the imported Hodge is an EXACT rational",
        all(is_exact_rational(facts.imported_hodge[i, j])
            for i in range(4) for j in range(4)))
    checks.check(
        "C-4", f"THE SIGN-LAYER FORK AS A PAIR: nnz(Q - Q^T) = "
        f"{facts.fork_asymmetry['landed_w3']} at the LANDED w(3) placement and "
        f"{facts.fork_asymmetry['wrap_wTm1']} at the WRAP w(T-1) placement",
        facts.fork_asymmetry == claims["fork_asymmetry"])
    checks.check(
        "C-5", "BOTH placements are Ps-covariant: Ps Q Ps - Q^T = 0 on each",
        facts.fork_covariance == claims["fork_covariance"])
    checks.check(
        "C-6", "THE LANDED CONTROL: at w(3) the {1,2}-core minors reproduce "
        "Block 188's landed pair DIGIT-FOR-DIGIT",
        facts.landed_minors[0] == claims["landed_minor_1"]
        and facts.landed_minors[1] == claims["landed_minor_2"])
    checks.check(
        "C-7", "AND THE VARIANT IS MEASURABLY DIFFERENT: at w(T-1) the same "
        "core's first minor is a DIFFERENT exact rational",
        facts.variant_minor_1 == claims["variant_minor_1"]
        and facts.variant_minor_1 != claims["landed_minor_1"])
    checks.check(
        "C-8", "d_K^2 = 0 at T = 12: the grade-raising part is a differential",
        facts.dk_square == claims["dk_square"])
    checks.check(
        "C-9", "Ps H Ps = H and Ps Q Ps = Q^T at T = 12, both at ZERO",
        facts.hodge_covariance == claims["hodge_covariance"]
        and facts.action_covariance == claims["action_covariance"])
    checks.check(
        "C-10", "the cross block between the physical span and its image is "
        "EMPTY at T = 12",
        facts.cross_block == claims["cross_block"])
    checks.check(
        "C-11", "every adjacent core t0 = 1..4 at T = 12 is symmetric at ZERO, "
        "of rank 8, with all eight leading minors POSITIVE",
        all(value == (0, 8, claims["core_signs"])
            for value in facts.core_signs.values()))
    checks.check(
        "C-12", f"the full {{1..5}} span Gram has EXACT RANK "
        f"{facts.span_rank}: the OS space does NOT grow with the span",
        facts.span_rank == claims["span_rank"])
    checks.check(
        "C-13", f"the {facts.schur_shape[0]} x {facts.schur_shape[1]} Schur "
        "complement of the {1,2} core inside that span is EXACTLY ZERO, so the "
        "core is a FRAME for the whole span",
        facts.schur_nonzeros == claims["schur_nonzeros"]
        and facts.schur_shape == SCHUR_SHAPE)
    checks.check(
        "C-14", "HODGE ROBUSTNESS ONE WAY: the check's FORENSIC variant block "
        "gives the IDENTICAL V and W factorizations at all three T = 12 bulk "
        "cores -- which is WHY the check reproduced these coefficients",
        facts.hodge_robust_under_forensic
        == claims["hodge_robust_under_forensic"])
    checks.check(
        "C-15", "AND SENSITIVITY THE OTHER WAY, WHICH IS WHY THE DISPLAY PINS "
        "v = 1: the SAME landed function at volume 12/13 gives a DIFFERENT "
        "polynomial at every bulk core",
        facts.volume_sensitive == claims["volume_sensitive"])
    checks.check(
        "C-16", "AND THE CHECK'S TWO FAILING REBUILDS ARE REPRODUCED HERE "
        "DIGIT-FOR-DIGIT, so the C3 discrepancy is located as a VOLUME "
        "convention and not a disputed measurement",
        facts.check_b105_factors == claims["check_b105_factors"]
        and facts.check_fallback_factors == claims["check_fallback_factors"])

    # --- D: THE REFUTATION AND ITS MECHANISM --------------------------------
    checks.check(
        "D-1", f"nnz(L_1 - L_1^T) at T = 12 cores 1,2,3 = "
        f"{tuple(facts.l1_asymmetry[c] for c in REFUTATION_CORES)}: the "
        "one-step transfer pairing is REFUTED at every bulk core",
        facts.l1_asymmetry == claims["l1_asymmetry"])
    checks.check(
        "D-2", f"nnz(L_2 - L_2^T) at the same cores = "
        f"{tuple(facts.l2_asymmetry[c] for c in REFUTATION_CORES)}: the "
        "two-step pairing is REFUTED as well",
        facts.l2_asymmetry == claims["l2_asymmetry"])
    checks.check(
        "D-3", "SIX EXACT CORE WITNESSES, each a position and an exact "
        "rational value, and they are the PROOF of the refutation",
        facts.core_witnesses == claims["core_witnesses"])
    checks.check(
        "D-4", "every witness is an EXACT rational and none is zero",
        all(is_exact_rational(value) and value != 0
            for _, _, value in facts.core_witnesses.values()))
    checks.check(
        "D-5", f"THE MECHANISM IN BOTH SIGN LAYERS: nnz([tau^2, Q]) = "
        f"{facts.tau2_nonzeros['landed_w3']} at w(3) and "
        f"{facts.tau2_nonzeros['wrap_wTm1']} at w(T-1)",
        facts.tau2_nonzeros == claims["tau2_nonzeros"])
    checks.check(
        "D-6", f"and the ordered slice-pair supports are "
        f"{facts.tau2_pairs['landed_w3']} and {facts.tau2_pairs['wrap_wTm1']} "
        "respectively -- the sign layer is visible in the mechanism too",
        facts.tau2_pairs == claims["tau2_pairs"])
    checks.check(
        "D-7", "the COMMON exact witness [tau^2, Q]_(0,1) = -65/576 in BOTH "
        "layers, and [tau^2, G] is nonzero in both",
        facts.tau2_witness == claims["tau2_witness"]
        and facts.tau2_inverse_nonzero == claims["tau2_inverse_nonzero"])
    checks.check(
        "D-8", "THE CHECK'S C2 CORRECTION, DECLARED: the global commutator is "
        "the MECHANISM and is NOT by itself a proof of the restricted core "
        "asymmetry -- the six core witnesses are",
        facts.banners["global_mechanism_is_sufficient"]
        == claims["global_mechanism_is_sufficient"])

    # --- E: LOCALITY, RIGIDITY AND THE TWO BOUNDARY LAYERS ------------------
    checks.check(
        "E-1", "V2@T16 == V4@T16 ENTRYWISE at zero residual: the step dynamics "
        "is POSITION-homogeneous",
        facts.step_equalities["V2@T16 - V4@T16"]
        == claims["step_equalities"]["V2@T16 - V4@T16"])
    checks.check(
        "E-2", "V2@T12 == V2@T16 and V1@T12 == V1@T16 ENTRYWISE: the step "
        "dynamics is WIDTH-invariant",
        facts.step_equalities["V2@T12 - V2@T16"]
        == claims["step_equalities"]["V2@T12 - V2@T16"]
        and facts.step_equalities["V1@T12 - V1@T16"]
        == claims["step_equalities"]["V1@T12 - V1@T16"])
    checks.check(
        "E-3", f"BUT THE GRAM IS NOT: K_c(2) - K_c(4) at T = 16 has EXACTLY "
        f"{facts.gram_inhomogeneity} nonzero entries, with an exact witness",
        facts.gram_inhomogeneity == claims["gram_inhomogeneity"]
        and facts.gram_witness == claims["gram_witness"])
    checks.check(
        "E-4", f"every one of the {len(facts.core_factors)} probed cores "
        "factors (2,2,4) over Q",
        all(degree_pattern(value) == claims["factor_pattern"]
            for value in facts.core_factors.values()))
    checks.check(
        "E-5", "the EVEN quadratic pair is identical at every even core and "
        "width probed",
        all(quadratics_of(facts.core_factors[key])
            == tuple(sorted(claims["even_quadratics"]))
            for key in EVEN_DEEP_CORES + EVEN_FAR_CORES))
    checks.check(
        "E-6", "the ODD quadratic pair is identical at every odd core and "
        "width probed",
        all(quadratics_of(facts.core_factors[key])
            == tuple(sorted(claims["odd_quadratics"]))
            for key in ODD_NEAR_CORES + ODD_MIRROR_CORES + ODD_DEEP_CORES))
    checks.check(
        "E-7", f"the DEEP even quartic is identical at the "
        f"{len(EVEN_DEEP_CORES)} interior even cores across all three widths",
        all(quartic_of(facts.core_factors[key]) == claims["even_deep_quartic"]
            for key in EVEN_DEEP_CORES))
    checks.check(
        "E-8", "AND THE EVEN SECTOR IS NOT RIGID AT THE FAR SEAM, WHICH IS "
        "THIS BLOCK'S OWN WORDING CORRECTION: at t0 = T/2 - 2 the quartic is a "
        "DIFFERENT value, itself locked across T = 12, 16 and 20",
        all(quartic_of(facts.core_factors[key]) == claims["even_far_quartic"]
            for key in EVEN_FAR_CORES)
        and claims["even_far_quartic"] != claims["even_deep_quartic"])
    checks.check(
        "E-9", "the ODD near-seam quartic is locked at t0 = 1 across all three "
        "widths, and its exact coefficient MIRROR at t0 = T/2 - 3",
        all(quartic_of(facts.core_factors[key]) == claims["odd_layer_quartics"][0]
            for key in ODD_NEAR_CORES)
        and all(quartic_of(facts.core_factors[key])
                == claims["odd_layer_quartics"][1] for key in ODD_MIRROR_CORES))
    checks.check(
        "E-10", "the ODD DEEP quartic is locked at T = 16 t0 = 3 and T = 20 "
        "t0 = 3, 5 -- the odd bulk value",
        all(quartic_of(facts.core_factors[key]) == claims["odd_deep_quartic"]
            for key in ODD_DEEP_CORES)
        and claims["odd_deep_quartic"] != claims["odd_layer_quartics"][0])
    checks.check(
        "E-11", "THE MIRROR COVARIANCE q_j = (-1)^j p_(8-j) holds at all NINE "
        "coefficients at T = 12 (V1/V3) and T = 16 (V1/V5)",
        all(value == claims["mirror_residual"]
            for value in facts.mirror_residuals.values()))
    checks.check(
        "E-12", "every polynomial coefficient measured is an integer in the "
        "primitive normalization",
        all(isinstance(coefficient, int)
            for value in facts.core_factors.values()
            for coefficients, _ in value for coefficient in coefficients))

    # --- F: THE UNIT-CELL MONODROMY -----------------------------------------
    checks.check(
        "F-1", f"W != V^2 at EXACTLY {PRIMITIVITY_NONZEROS} entries at every "
        "T = 20 deep core t0 = 3, 4, 5: the monodromy is PRIMITIVE",
        all(value == claims["primitivity_nonzeros"]
            for value in facts.primitivity_nonzeros.values()))
    checks.check(
        "F-2", "the three exact (W - V^2)_(0,4) witnesses",
        facts.primitivity_witnesses == claims["primitivity_witnesses"])
    checks.check(
        "F-3", "charpoly(W) is IDENTICAL at all three deep cores: the "
        "monodromy is PARITY-INDEPENDENT",
        (len({tuple(value) for value in facts.monodromy_factors.values()}) == 1)
        == claims["parity_independent"])
    checks.check(
        "F-4", "charpoly(W) = (22569375 z^2 - 233631106 z + 22569375)^2 "
        "(39529825 z^2 - 109432706 z + 39529825)^2",
        all(tuple(value) == claims["monodromy_factors"]
            for value in facts.monodromy_factors.values()))
    checks.check(
        "F-5", "both discriminants are the claimed exact POSITIVE integers",
        facts.discriminants == claims["discriminants"]
        and all(value > 0 for value in facts.discriminants.values()))
    checks.check(
        "F-6", "and both prime factorizations are exactly as displayed",
        facts.discriminant_factorizations
        == claims["discriminant_factorizations"])
    checks.check(
        "F-7", "both traces EXCEED twice the leading coefficient, which forces "
        "both roots POSITIVE and not merely real",
        facts.trace_exceeds_twice_leading
        == claims["trace_exceeds_twice_leading"])
    checks.check(
        "F-8", "both constant/leading ratios are EXACTLY 1, so each pair is "
        "RECIPROCAL",
        facts.reciprocal_form == claims["reciprocal_form"])
    checks.check(
        "F-9", "the two trace ratios are DISTINCT: 233631106*39529825 - "
        "109432706*22569375 = 6765568955757700 != 0, so four DISTINCT real "
        "positive roots in two reciprocal pairs",
        facts.trace_ratio_gap == claims["trace_ratio_gap"]
        and facts.trace_ratio_gap != 0)
    checks.check(
        "F-10", "2 cosh(theta_1) = 233631106/22569375 and 2 cosh(theta_2) = "
        "109432706/39529825, both EXACT rationals",
        facts.two_cosh == claims["two_cosh"]
        and all(is_exact_rational(value) for value in facts.two_cosh.values()))
    checks.check(
        "F-11", "THE COEFFICIENT IDENTITY: the second monodromy quadratic is "
        "a z^2 - c z + a from the even V-quartic (a, b, c) and b DROPS OUT",
        facts.coefficient_identity == claims["coefficient_identity"])

    # --- G: THE COMMUTANT ----------------------------------------------------
    checks.check(
        "G-1", "U^T K_c U = K_c and [W, U] = 0 at the T = 20 deep core, both "
        "at ZERO residual",
        facts.u_isometry == claims["u_isometry"]
        and facts.u_commutator == claims["u_commutator"])
    checks.check(
        "G-2", "the U off-sector block of W is EXACTLY zero, so the grading is "
        "a genuine block decomposition",
        facts.u_off_sector == claims["u_off_sector"])
    checks.check(
        "G-3", "U = +1 carries BOTH copies of the 39529825 quadratic and "
        "U = -1 BOTH copies of the 22569375 quadratic",
        all(facts.u_sector_factors[sign] == (claims["u_sector_factors"][sign],)
            for sign in (1, -1)))
    checks.check(
        "G-4", "[W, S] = 0, S^2 = U and S^4 = I, all at ZERO: S is a genuine "
        "SECOND commuting symmetry of the monodromy",
        facts.s_relations == claims["s_relations"])
    checks.check(
        "G-5", f"BUT S IS NOT A GRAM ISOMETRY: S^T K_c S - K_c has EXACTLY "
        f"{facts.s_gram_defect} nonzero entries, with an exact witness",
        facts.s_gram_defect == claims["s_gram_defect"]
        and facts.s_gram_witness == claims["s_gram_witness"])
    checks.check(
        "G-6", "the S-momentum blocks: p = 0 and p = 2 both carry the "
        "39529825 quadratic and p = 1, 3 the 22569375 one",
        facts.momentum_factors["p0"] == ((claims["momentum_factors"]["p0"], 1),)
        and facts.momentum_factors["p2"]
        == ((claims["momentum_factors"]["p2"], 1),)
        and facts.momentum_factors["p13"]
        == ((claims["momentum_factors"]["p13"], 2),))
    checks.check(
        "G-7", "AND THE p = 0 / p = 2 EQUALITY IS DECLARED NOT GROUP-FORCED: "
        "it is an ADDITIONAL exact isospectrality of this construction",
        facts.banners["momentum_equality_is_group_forced"]
        == claims["momentum_equality_is_group_forced"])
    checks.check(
        "G-8", f"THE CENSUS IS EXHAUSTIVE AND MEASURED HERE: "
        f"{facts.census_size} signed monomial candidates swept",
        facts.census_size == claims["census_size"])
    checks.check(
        "G-9", "the W-commutants among them are EXACTLY {I, S, S^3, U}",
        facts.census_commutants == tuple(sorted(claims["census_commutants"])))
    checks.check(
        "G-10", "and EXACTLY {I, U} of those are Gram isometries -- 2 of 4",
        facts.census_isometries == tuple(sorted(claims["census_isometries"])))
    checks.check(
        "G-11", f"the unsigned spatial reflection is REFUTED: [W, R] has "
        f"{facts.reflection_commutator} nonzero entries with the exact witness "
        "[W, R]_(0,5) = 16334218/7905965",
        facts.reflection_commutator == claims["reflection_commutator"]
        and facts.reflection_witness == claims["reflection_witness"])
    checks.check(
        "G-12", "K_c is EXACTLY SYMMETRIC at the deep core, which is the "
        "hypothesis the whole P1 resolution turns on",
        facts.core_gram_symmetry == claims["core_gram_symmetry"])
    checks.check(
        "G-13", "THEREFORE THE K-ONLY TRANSPOSITION IS A MEASURED NO-OP -- "
        "this block's CORRECTION to the check's P1, whose 64-entry spectrum "
        "change does NOT occur on this construction",
        facts.konly_difference == claims["konly_difference"])
    checks.check(
        "G-14", f"the CONSISTENT transposition moves W at EXACTLY "
        f"{facts.consistent_difference} entries",
        facts.consistent_difference == claims["consistent_difference"])
    checks.check(
        "G-15", "and yet preserves charpoly(W) exactly",
        facts.consistent_charpoly_same == claims["consistent_charpoly_same"])
    checks.check(
        "G-16", "because the transposed operator IS K_c^-1 W^T K_c, a "
        "SIMILARITY -- measured at ZERO residual, not argued",
        facts.similarity_residual == claims["similarity_residual"])
    checks.check(
        "G-17", "every commutant witness measured is an EXACT rational",
        is_exact_rational(facts.s_gram_witness)
        and is_exact_rational(facts.reflection_witness))

    # --- H: THE NOTE, THE FENCE AND THE nsimplify ABSENCE -------------------
    checks.check(
        "H-1", f"the note is at its final path docs/{FINAL_NOTE_NAME}",
        facts.note_at_final_path)
    checks.check(
        "H-2", "the N5 fence appears BYTE-IDENTICALLY in the note, AND the "
        "fence is REQUIRED rather than optional -- the declared key set must "
        "still be the full one, so the requirement cannot be dropped",
        tuple(claims["required_scope_keys"]) == SCOPE_KEYS
        and all(facts.scope.get(key) for key in claims["required_scope_keys"]))
    checks.check(
        "H-3", f"sp.nsimplify occurs {facts.nsimplify_calls} times in this "
        "runner's own source",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    return checks


# ---------------------------------------------------------------------------
# the measured report
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED -- BLOCK 190, THE WIDTH FAMILY TRANSFER AND MONODROMY")
    print(f"  measurement pass: {elapsed_ns / 1e9:.1f} s")
    print(f"  THE ONE IMPORT, DISPLAYED AND GATED: shear_hodge(5/13, 1) = "
          f"{facts.imported_hodge.tolist()}")
    print(f"  displayed-vs-imported residual: {facts.hodge_display_residual}")
    print(f"  SIGN-LAYER FORK at T = 8: nnz(Q - Q^T) = "
          f"{facts.fork_asymmetry['landed_w3']} at the LANDED w(3), "
          f"{facts.fork_asymmetry['wrap_wTm1']} at the WRAP w(T-1); "
          f"Ps-covariance {facts.fork_covariance}")
    print(f"  LANDED CONTROL minor 1: {facts.landed_minors[0]}")
    print(f"  VARIANT minor 1 (different, and that is the disclosure): "
          f"{facts.variant_minor_1}")
    print(f"  T = 12 structure: d_K^2 = {facts.dk_square}, Ps H Ps - H = "
          f"{facts.hodge_covariance}, Ps Q Ps - Q^T = "
          f"{facts.action_covariance}, cross block = {facts.cross_block}, "
          f"span rank = {facts.span_rank}, Schur "
          f"{facts.schur_shape} = {facts.schur_nonzeros}")
    print(f"  Hodge fork: robust under the forensic variant = "
          f"{facts.hodge_robust_under_forensic}; sensitive to the volume = "
          f"{facts.volume_sensitive}")
    print(f"    check's v = 12/13 rebuild reproduced: "
          f"{facts.check_b105_factors}")
    print(f"    check's unit-shear fallback reproduced: "
          f"{facts.check_fallback_factors}")
    print(f"  REFUTATION: nnz(L_1 - L_1^T) = {facts.l1_asymmetry}, "
          f"nnz(L_2 - L_2^T) = {facts.l2_asymmetry}")
    for key in sorted(facts.core_witnesses):
        row, column, value = facts.core_witnesses[key]
        print(f"    witness core {key[0]} k = {key[1]} at ({row},{column}) = "
              f"{value}")
    print(f"  MECHANISM: nnz([tau^2, Q]) = {facts.tau2_nonzeros}, slice pairs "
          f"= {facts.tau2_pairs}, common witness = {facts.tau2_witness}, "
          f"nnz([tau^2, G]) = {facts.tau2_inverse_nonzero}")
    print(f"  LOCALITY: {facts.step_equalities}; K_c(2) - K_c(4) at T = 16 = "
          f"{facts.gram_inhomogeneity} entries")
    for key in sorted(facts.core_factors):
        print(f"    V charfactors {key}: {facts.core_factors[key]}")
    print(f"  MIRROR residuals: {facts.mirror_residuals}")
    print(f"  MONODROMY: nnz(W - V^2) = {facts.primitivity_nonzeros}")
    for core in sorted(facts.monodromy_factors):
        print(f"    charpoly(W) at t0 = {core}: {facts.monodromy_factors[core]}")
    print(f"  POSITIVITY: discriminants {facts.discriminants}")
    print(f"    factorizations {facts.discriminant_factorizations}")
    print(f"    traces exceed 2a: {facts.trace_exceeds_twice_leading}; "
          f"reciprocal: {facts.reciprocal_form}; trace-ratio gap: "
          f"{facts.trace_ratio_gap}")
    print(f"    2 cosh: {facts.two_cosh}; coefficient identity: "
          f"{facts.coefficient_identity}")
    print(f"  COMMUTANT: U isometry {facts.u_isometry}, [W,U] "
          f"{facts.u_commutator}, off-sector {facts.u_off_sector}, S relations "
          f"{facts.s_relations}, S Gram defect {facts.s_gram_defect}")
    print(f"    census {facts.census_size}: commutants "
          f"{facts.census_commutants}, isometries {facts.census_isometries}")
    print(f"    reflection [W,R] = {facts.reflection_commutator} entries, "
          f"witness {facts.reflection_witness}")
    print(f"    P1: K_c symmetry {facts.core_gram_symmetry}, K-only "
          f"{facts.konly_difference}, consistent "
          f"{facts.consistent_difference}, charpoly preserved "
          f"{facts.consistent_charpoly_same}, similarity residual "
          f"{facts.similarity_residual}")
    print(f"  nsimplify occurrences: {facts.nsimplify_calls}")
    print("  SCOPE: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. THE OBJECT "
          "IS A DISCLOSED VARIANT of Block 188's landed construction and their "
          "own T = 8 numbers are reproduced here under THEIR sign placement. "
          "DISPERSION, MASS SCALES, THE PHYSICAL TIME STEP and TRANSFER "
          "POSITIVITY are READINGS: what is proven is the positivity of an "
          "8 x 8 rational spectrum, and the OS reconstruction that would "
          "license the words IS NOT PERFORMED. ONE FIXTURE AND FOUR WIDTHS IS "
          "NOT A WINDOW AND NOTHING IS PROVEN ABOUT THE INFINITE-WIDTH LIMIT.")
    print()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--list-mutations", action="store_true",
        help="print the declared mutation names, one per line, and exit")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted, so
    # a mutation can only rewrite a CLAIM.  No family can cascade into another
    # because no gate feeds a measurement.
    facts = measure()
    elapsed_ns = time.monotonic_ns() - started_ns

    checks = build_checks(facts, build_claims(""))
    if mutation:
        raw = checks.families()
        checks = build_checks(facts, build_claims(mutation))
        mutated = checks.families()
        target = MUTATION_GATE[mutation]
        changed = {family for family in raw if raw[family] != mutated[family]}
        if changed - {target} or mutated[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    report_measured(facts, elapsed_ns)
    checks.report()
    print(N5_FENCE)
    return checks.finish()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as error:
        print(f"[FAIL] INTERNAL-EXCEPTION: {type(error).__name__}: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise
