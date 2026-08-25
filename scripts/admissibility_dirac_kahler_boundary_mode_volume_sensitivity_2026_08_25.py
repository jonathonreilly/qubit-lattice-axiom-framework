#!/usr/bin/env python3
"""BLOCK 191 -- THE BOUNDARY MODES OF THE UNIT-CELL MONODROMY, AND THE
HODGE-VOLUME SPECTRAL SENSITIVITY.

THE RESULT, AND ITS EXACT SCOPE.  On BLOCK 190's wrap-edge width family at the
SAME fixture (m, c) = (9/20, 5/13), the unit-cell monodromy W = K_c^-1 L_2 is
computed at EVERY core of T = 16 AND T = 20; the Hodge volume v of Block 105's
shear_hodge(c, v) -- pinned at 1 throughout Block 190 -- is turned uniformly and
then LOCALLY, and the exact spectra are measured on both sides.  ALL OF IT IS
FINITE EXACT LINEAR ALGEBRA ON ONE CONSTRUCTED MATRIX FAMILY.  NONE OF IT
ESTABLISHES THAT v IS A LAPSE, THAT THESE SHIFTS ARE LAPSE PHYSICS, OR THAT TWO
v(t) PROFILES ARE PHYSICALLY INEQUIVALENT.  WHAT IS ESTABLISHED IS HODGE-VOLUME
SPECTRAL SENSITIVITY WITHIN AN IMPOSED FINITE CONSTRUCTION, AND THE WORD LAPSE
IS FENCED AS A READING BEFORE THE FIRST NUMBER IS READ.

  0. THE CONSTRUCTION CONTROL, AND THE VOLUME LAW IS A DISPLAYED FORMULA (C).
     Block 190 displayed the landed shear block at the PINNED volume v = 1.
     This block needs v as a VARIABLE, so the LAW is displayed:
     shear_hodge(c, v) = diag(v, v g(c)^-1, 1/v) with g(c) = [[1,c],[c,1]],
     and BOTH of its values at c = 5/13 -- v = 1 and v = 4/5 -- are gated
     ENTRYWISE against the import at ZERO residual, thirty-two numbers in all.
     The profile rule is stated once and is the ONLY new construction element:
     block(t) = B(c, v(t)) on t < T/2 and P_4 B(c, v(-1-t)) P_4^T on t >= T/2.

  1. THE BOUNDARY MONODROMY, SCANNED AT EVERY CORE OF TWO WIDTHS (C).  The
     LIGHT pair is BOUNDARY-RIGID -- both copies exact at every non-crossing
     core at both widths.  The HEAVY sector loses EXACTLY ONE copy at each of
     four layer cores to a NON-RECIPROCAL quadratic: 'near' at t0 = 1,
     'mirror' = rev(near) at t0 = T/2 - 4, 'second' at t0 = T/2 - 3, and
     rev(second) at t0 = T/2.  EVERY ENTRY OF THE TABLE IS THE SAME POLYNOMIAL
     AT T = 16 AND T = 20: the layer is POSITIONALLY WIDTH-LOCKED, one core
     thick near-side and two far-side.  Non-reciprocity is the exact integer
     statement a - c != 0; positivity SURVIVES at the seam (positive
     discriminants, positive traces) while RECIPROCITY does not.

  2. THE VALIDITY BOUNDARY IS A RULE ABOUT THE PAIRING AND NOT ABOUT FACTORING,
     AND THE CHECK'S CORRECTION IS STRENGTHENED AGAINST THIS BLOCK'S OWN SOLVE
     (C).  L_2 reads G at times {t0+2, t0+3}: t0 + 3 = T/2 TOUCHES the fixed
     slice and is admissible; t0 + 3 > T/2 CROSSES into the image half and is
     not a bulk object.  THE SOLVE'S "NON-FACTORING SIGNATURE" IS WITHDRAWN AND
     IS FALSE IN BOTH DIRECTIONS, MEASURED: crossing cores at T/2 - 2 and
     T/2 - 1 DO factor, with degree pattern (2, 2, 4) and an irreducible
     rational quartic (certificates: mod 11 at T = 16, mod 67 at T = 20); AND
     the crossing core at t0 = T/2 factors COMPLETELY into rational quadratics,
     so a crossing core can look exactly like a clean bulk core.  NO FACTORING
     SIGNATURE CAN DEFINE THE BOUNDARY IN EITHER DIRECTION.

  3. THE UNIFORM VOLUME DIAL MOVES THE TWO SCALES IN OPPOSITE DIRECTIONS (D).
     At T = 16, t0 = 3, v = 4/5 the exact spectrum is
     (31260675 z^2 - 302948719 z + 31260675)^2
     (50327125 z^2 - 139773119 z + 50327125)^2 -- the FORM survives (both
     palindromic, both squared, both discriminants positive with their
     factorizations gated, both traces above 2a) and the two exact rational
     traces move OPPOSITE WAYS: -2071568131893/3135706208125 < 0 for the heavy
     scale and +710938392957/79576897760125 > 0 for the light one.  THE
     SOLVE'S RATIO PAIR IS CORRECTED AS CONTENT: 2.7362708113 -> 2.6427023041,
     not 2.7361 -> 2.6449.  The exact traces are PRIMARY and the decimals are
     this block's ONE numeric layer, evalf of exact objects at 40 digits and
     gated to ten places.

  4. THE LOCALIZED BUMP KILLS PALINDROMICITY IN EVERY IRREDUCIBLE FACTOR (E).
     With v = 4/5 on the positive anchors {3, 4}, Ps H Ps = H and Ps Q Ps = Q^T
     hold at EXACTLY ZERO, and at t0 = 1, 3, 5 every one of the NINE
     irreducible factors has leading != constant as an exact integer
     inequality.  Root reality is decided by exact discriminants and exact
     Sturm counts, never estimated.  THE COMPLEX-PAIR DESCRIPTION IS COMPLETED
     RATHER THAN REPEATED: of the FOUR pairs the {3,4} bump produces, EXACTLY
     ONE lies inside the solve's |Im| ~ 0.002-0.003 band, one lies just below
     it at 0.0018623814, and TWO lie far above at 0.0111282045 and
     0.0139861010; over both bump positions the census of SEVEN pairs is TWO
     below the band, ONE inside and FOUR above.

  5. BOUNDARY-MODE DOMINANCE IS REFUTED AS STATED, AND HYBRIDIZATION REPLACES
     IT (E).  U remains an exact Gram isometry and an exact commutant at the
     BUMPED core, and the grading is what refutes the claim: the baseline
     U = -1 sector is heavy TIMES near -- two labelled rational factors -- and
     after the bump it is ONE IRREDUCIBLE QUARTIC.  The two baseline large
     roots, already only 0.0126473949 apart, become one conjugate pair with a
     COMMON REAL PART, and their matched displacements are 0.9570159788 and
     0.9443699527 -- COMPARABLE, not dominated.  "The edge mode is the bump's
     antenna" is WITHDRAWN.

  6. AND THE REACH IS BUMP-POSITION DEPENDENT (E).  The {2,3} profile is also
     exactly Ps-covariant; its t0 = 1 response REVERSES SIGN and falls to
     ~0.688, its t0 = 3 response falls from 1.3978902241 to 0.0737486236, and
     at t0 = 5 THE OPERATOR ITSELF is unchanged at EXACTLY ZERO entries.
     Near-edge coupling is GENERIC across these two positions; magnitude, sign
     and reach are NOT.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO LAPSE PHYSICALITY:
v is the IMPOSED Block 105 Hodge-volume parameter and this block supplies no
lapse variable in an ADM phase space, no Hamiltonian constraint, no gauge orbit,
no quotient, no Dirac observable and no OS reconstruction making W a physical
transfer operator.  NO PHYSICAL VOLUME DIAL: that the spectrum moving means the
dial is not a conformal or gauge rescaling is a READING.  NO PHYSICAL BOUNDARY
MODE: 'boundary mode' names an exact rational FACTOR at a seam-adjacent core.
NO PROFILE INEQUIVALENCE: exact Ps-covariance proves compatibility with ONE
reflection and does NOT prove that two v(t) profiles are physically
inequivalent.  NO TRANSFER OPERATOR: Block 190 refuted the naive OS transfer
pairing on this class and nothing here repairs it.  NO BOUNDARY-MODE DOMINANCE:
refuted as stated and replaced by measured hybridization.  NO GENERALITY: ONE
fixture, TWO widths, FOUR volume profiles, ONE bump amplitude.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 190 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted, with lapse physicality, the physical volume dial, the physical
     boundary mode, profile inequivalence, the transfer operator,
     boundary-mode dominance and generality ALL declared NOT CLAIMED as
     measured constants, and ten gravity structures enumerated as NOT SUPPLIED.
  C  THE BOUNDARY MONODROMY AND THE VALIDITY RULE: the displayed volume law at
     BOTH volumes against the import, Ps-covariance of every profile, the
     full-core scan at both widths, light boundary-rigidity, single-copy heavy
     survival, exact non-reciprocity with factored discriminants and positive
     roots, the exact near/far coefficient reversal, the touch/cross rule at
     both widths, the (2,2,4) crossing pattern with finite-field
     irreducibility certificates, and the all-quadratic crossing core that
     kills the factoring signature from the other side.
  D  THE VOLUME DIAL: the exact v = 4/5 deep spectrum, the preserved
     palindromic-squared form, the factored discriminants and trace bounds, the
     two exact rational trace motions and their opposite signs, the corrected
     decimal ratio pair, and the withdrawn solve value.
  E  THE BUMP PACKAGE: exact Ps-covariance of both bump profiles, the nine
     irreducible factors, exact non-palindromicity, quartic irreducibility
     certificates, exact discriminants and Sturm counts, the operator-difference
     census, the max matched shifts, the COMPLETE complex-pair inventory, the
     pencil cross-check, the U isometry and commutation at the bumped core, the
     sector hybridization, the comparable displacements with the baseline
     separation, and the {2,3} position dependence with its exact zero.
  F  the note at its final path, the N5 fence byte-identical, and the
     nsimplify count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through F PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: forty-nine declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family census is
  A 2, B 8, C 13, D 7, E 17, F 2.
  SEVEN OF THE FORTY-NINE GUARD CORRECTIONS RATHER THAN RESULTS:
  break_crossing_signature asserts the withdrawn non-factoring signature;
  break_signature_from_below denies that a crossing core can factor completely
  into quadratics; break_solve_ratio asserts the withdrawn 2.6449;
  break_small_imaginary_only asserts the incomplete 0.002-0.003 description;
  break_edge_antenna asserts the refuted boundary-mode dominance;
  claim_lapse_physicality asserts the fenced headline; and
  claim_profiles_inequivalent asserts what Ps-covariance does not prove.

RUNNING
  python3
  scripts/admissibility_dirac_kahler_boundary_mode_volume_sensitivity_2026_08_25.py
  python3 ... --list-mutations
  python3 ... --mutation break_edge_antenna
"""

from __future__ import annotations

import argparse
import itertools
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

# THE MACHINERY IMPORT, LANDED, AND IT IS EXACTLY ONE OBJECT: the Block 105
# shear_hodge() re-exported by the Block 128 module.  Block 190 imported it at
# the pinned volume; this block imports the SAME function and varies its second
# argument, which is why the note displays the LAW and not one matrix.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 190 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 189 tip.
BLOCK190_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK190_RUNNER = (
    "scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_"
    "2026_08_25.py"
)
PARENT_ARTIFACTS = (BLOCK190_NOTE, BLOCK190_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "42c93e5b4833faaf9d535bce3bd0205af3e7311c",   # Block 190 note
    "b2181900766f0608cf0ca71272ad5acdbc38a3eb",   # Block 190 runner
)
# THE VOLUME AUTHORITY: Block 105's primary, whose shear_hodge(c, v) IS the
# volume law this block turns, and Block 188's site route, which the width
# family is a disclosed variant of.
BLOCK105_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK105_RUNNER = (
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_"
    "hodge_overlap_2026_08_14.py"
)
BLOCK188_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-24.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_width_family_transfer_monodromy_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  CARRIED FORWARD FROM THE BLOCK 190 RUNNER AND RE-RESOLVED AT
# DRAFT TIME.
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block190-"
              "width-family-transfer-monodromy-20260825")
PARENT_COMMIT = "e75ad9f4998ae4cc6a25a2e20191e0b9d76ff3fd"
# The Block 189 tip: a real ancestor of HEAD that predates Block 190 and
# therefore carries NEITHER Block 190 artifact.
STALE_PARENT_COMMIT = "996e516600ca9d0f679a6f3ab554036068205d2f"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_lapse_physicality",
    "claim_volume_dial_physical",
    "claim_boundary_mode_physical",
    "claim_profiles_inequivalent",
    "claim_transfer_operator",
    "claim_edge_dominance",
    "claim_generality",
    "break_volume_law_display",
    "break_profile_covariance",
    "break_deep_rigidity",
    "break_light_boundary_rigidity",
    "break_heavy_survival",
    "break_near_boundary_quadratic",
    "break_nonreciprocity",
    "break_boundary_positivity",
    "break_far_reversal",
    "break_touch_admissible",
    "break_crossing_pattern",
    "break_crossing_signature",
    "break_signature_from_below",
    "break_volume_charpoly",
    "break_volume_palindromy",
    "break_volume_discriminants",
    "break_trace_motion_values",
    "break_trace_motion_signs",
    "break_ratio_pair",
    "break_solve_ratio",
    "break_bump_covariance",
    "break_bump_factors",
    "break_nonpalindromicity",
    "break_bump_irreducibility",
    "break_bump_reality",
    "break_operator_census",
    "break_max_shifts",
    "break_complex_inventory",
    "break_small_imaginary_only",
    "break_pencil_agreement",
    "break_bumped_isometry",
    "break_sector_hybridization",
    "break_comparable_shifts",
    "break_baseline_separation",
    "break_edge_antenna",
    "break_position_dependence",
    "break_out_of_range_exactness",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_lapse_physicality": "B",
    "claim_volume_dial_physical": "B",
    "claim_boundary_mode_physical": "B",
    "claim_profiles_inequivalent": "B",
    "claim_transfer_operator": "B",
    "claim_edge_dominance": "B",
    "claim_generality": "B",
    "break_volume_law_display": "C",
    "break_profile_covariance": "C",
    "break_deep_rigidity": "C",
    "break_light_boundary_rigidity": "C",
    "break_heavy_survival": "C",
    "break_near_boundary_quadratic": "C",
    "break_nonreciprocity": "C",
    "break_boundary_positivity": "C",
    "break_far_reversal": "C",
    "break_touch_admissible": "C",
    "break_crossing_pattern": "C",
    "break_crossing_signature": "C",
    "break_signature_from_below": "C",
    "break_volume_charpoly": "D",
    "break_volume_palindromy": "D",
    "break_volume_discriminants": "D",
    "break_trace_motion_values": "D",
    "break_trace_motion_signs": "D",
    "break_ratio_pair": "D",
    "break_solve_ratio": "D",
    "break_bump_covariance": "E",
    "break_bump_factors": "E",
    "break_nonpalindromicity": "E",
    "break_bump_irreducibility": "E",
    "break_bump_reality": "E",
    "break_operator_census": "E",
    "break_max_shifts": "E",
    "break_complex_inventory": "E",
    "break_small_imaginary_only": "E",
    "break_pencil_agreement": "E",
    "break_bumped_isometry": "E",
    "break_sector_hybridization": "E",
    "break_comparable_shifts": "E",
    "break_baseline_separation": "E",
    "break_edge_antenna": "E",
    "break_position_dependence": "E",
    "break_out_of_range_exactness": "E",
    "drop_n5_fence": "F",
    "break_nsimplify_absence": "F",
}
MUTATED_FAMILIES = "ABCDEF"


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
    "BLOCK 190's WRAP-EDGE WIDTH FAMILY, CARRIED UNCHANGED AND STILL A DISCLOSED VARIANT OF BLOCK 188's SITE CONSTRUCTION: the staggered Dirac-Kahler carrier on Z_T x Z_4 for even T with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the site raising set A_s of the d_K entries in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13), at the TWO widths T = 16 and T = 20",
    "THE VOLUME PROFILE, WHICH IS THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT: a map v from the positive anchors {0..T/2-1} to the positive rationals, placed as block(t) = B(c, v(t)) for t < T/2 and as the P_4 image block(t) = P_4 B(c, v(thA_s(t))) P_4^T for t >= T/2 with thA_s(t) = -1-t, assembled into H by the same quarter-weighted four-corner cell average Block 190 uses -- IMPOSED, and reducing to Block 190's rule IDENTICALLY at any uniform profile",
    "THE FOUR PROFILES PROBED: uniform v = 1, uniform v = 4/5, and the LOCALIZED bumps v = 4/5 on the positive anchors {3, 4} and on {2, 3} with v = 1 elsewhere -- chosen by this block and derived from nothing",
    "THE PAIR CORES AND THEIR SHIFTED PAIRINGS, BLOCK 190's OBJECTS UNCHANGED: K_c[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)], L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, and the UNIT-CELL MONODROMY W = K_c^-1 L_2 -- NOT a derived transfer operator of any theory, and explicitly NOT repaired as one by this block",
    "THE SINGLE FIXTURE (m, c) = (9/20, 5/13) AND THE SINGLE BUMP AMPLITUDE v = 4/5 -- POINTS, NOT WINDOWS: no bracket, no ray, no edge and no interior is established for anything in this block",
    "Block 105's LANDED shear_hodge(c, v) read through the Block 128 module: THE ONLY OBJECT IMPORTED BY THIS RUNNER, whose LAW diag(v, v g(c)^-1, 1/v) is DISPLAYED IN THE NOTE and whose values at BOTH probed volumes are gated entrywise against the import",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SEVEN ARE FALSE
# AND STAY FALSE.  THE FIRST IS THE HEADLINE OF THE WHOLE BLOCK.
LAPSE_PHYSICALITY_CLAIMED = False
VOLUME_DIAL_PHYSICAL_CLAIMED = False
BOUNDARY_MODE_PHYSICAL_CLAIMED = False
PROFILES_INEQUIVALENT_CLAIMED = False
TRANSFER_OPERATOR_CLAIMED = False
EDGE_DOMINANCE_CLAIMED = False
GENERALITY_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function",
    "shift vector",
    "ADM phase space",
    "Hamiltonian constraint",
    "momentum/diffeomorphism constraint",
    "first-class constraint algebra",
    "Dirac closure",
    "Dirac observable",
    "gauge orbit and its quotient",
    "Osterwalder-Schrader reconstruction of a transfer operator",
)
CHECK_VERDICT = "CONFIRMED-WITH-MATERIAL-NARROWINGS-AND-TWO-NUMERICAL-CORRECTIONS"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
SPACE_EXTENT = 4
FIXTURE_MASS = sp.Rational(9, 20)
FIXTURE_SHEAR = sp.Rational(5, 13)
UNIT_VOLUME = sp.Integer(1)
BUMP_VOLUME = sp.Rational(4, 5)
WIDTHS = (16, 20)

# --- C: THE DISPLAYED VOLUME LAW, AT BOTH PROBED VOLUMES --------------------
# LITERALS, written as the note writes them, and gated against
# b128.block105.shear_hodge(5/13, v) entrywise at BOTH volumes.
DISPLAYED_HODGE_UNIT = sp.Matrix([
    [1, 0, 0, 0],
    [0, sp.Rational(169, 144), sp.Rational(-65, 144), 0],
    [0, sp.Rational(-65, 144), sp.Rational(169, 144), 0],
    [0, 0, 0, 1]])
DISPLAYED_HODGE_BUMP = sp.Matrix([
    [sp.Rational(4, 5), 0, 0, 0],
    [0, sp.Rational(169, 180), sp.Rational(-13, 36), 0],
    [0, sp.Rational(-13, 36), sp.Rational(169, 180), 0],
    [0, 0, 0, sp.Rational(5, 4)]])
PROFILE_NAMES = ("v1", "v45", "bump34", "bump23")
BUMP_ANCHORS = {"bump34": (3, 4), "bump23": (2, 3)}

# --- C: THE BOUNDARY MONODROMY TABLE ----------------------------------------
HEAVY = (22569375, -233631106, 22569375)
LIGHT = (39529825, -109432706, 39529825)
NEAR = (43033320714375, -445467467014578, 48554286398375)
MIRROR = (48554286398375, -445467467014578, 43033320714375)
SECOND = (48554286398375, -376762652339458, 35686537764375)
REV_SECOND = (35686537764375, -376762652339458, 48554286398375)
DEEP_FACTORS = ((HEAVY, 2), (LIGHT, 2))
# THE FULL SCAN, BY POSITION.  key: (width, t0) -> the expected factor multiset.
# EVERY VALUE IS THE SAME POLYNOMIAL AT BOTH WIDTHS AT THE SAME RELATIVE
# POSITION, WHICH IS THE POSITIONAL WIDTH LOCK.
CORE_TABLE = {
    (16, 1): ((HEAVY, 1), (LIGHT, 2), (NEAR, 1)),
    (16, 2): DEEP_FACTORS,
    (16, 3): DEEP_FACTORS,
    (16, 4): ((HEAVY, 1), (LIGHT, 2), (MIRROR, 1)),
    (16, 5): ((HEAVY, 1), (LIGHT, 2), (SECOND, 1)),
    (16, 8): ((HEAVY, 1), (LIGHT, 2), (REV_SECOND, 1)),
    (20, 1): ((HEAVY, 1), (LIGHT, 2), (NEAR, 1)),
    (20, 2): DEEP_FACTORS,
    (20, 3): DEEP_FACTORS,
    (20, 4): DEEP_FACTORS,
    (20, 5): DEEP_FACTORS,
    (20, 6): ((HEAVY, 1), (LIGHT, 2), (MIRROR, 1)),
    (20, 7): ((HEAVY, 1), (LIGHT, 2), (SECOND, 1)),
    (20, 10): ((HEAVY, 1), (LIGHT, 2), (REV_SECOND, 1)),
}
DEEP_CORES = ((16, 2), (16, 3), (20, 2), (20, 3), (20, 4), (20, 5))
LAYER_CORES = ((16, 1), (16, 4), (16, 5), (20, 1), (20, 6), (20, 7))
LIGHT_RIGID_CORES = tuple(sorted(CORE_TABLE))
NONRECIPROCAL = (NEAR, MIRROR, SECOND, REV_SECOND)
BOUNDARY_DISCRIMINANTS = {
    NEAR: 190083455453828589664707955584,
    MIRROR: 190083455453828589664707955584,
    SECOND: 135019158697151741387932171264,
    REV_SECOND: 135019158697151741387932171264,
}
BOUNDARY_DISCRIMINANT_FACTORIZATIONS = {
    NEAR: {2: 7, 3: 4, 13: 1, 313: 1, 70619: 1, 96676423: 1, 659962871: 1},
    SECOND: {2: 10, 13: 1, 313: 1, 32404681043299888780819: 1},
}
BOUNDARY_ASYMMETRY = {NEAR: -5520965684000, MIRROR: 5520965684000,
                      SECOND: 12867748634000, REV_SECOND: -12867748634000}
REVERSAL_PAIRS = ((NEAR, MIRROR), (SECOND, REV_SECOND))

# --- C: THE VALIDITY BOUNDARY -----------------------------------------------
# L_2 reads G at times {t0+2, t0+3}.  t0+3 == T/2 TOUCHES; t0+3 > T/2 CROSSES.
TOUCH_CORES = ((16, 5), (20, 7))
CROSS_CORES = ((16, 6), (16, 7), (20, 8), (20, 9))
CROSSING_PATTERN = (2, 2, 4)
CROSSING_CERTIFICATE_PRIMES = {(16, 6): 11, (20, 8): 67}
# AND THE SIGNATURE DIES FROM THE OTHER SIDE TOO: these CROSSING cores factor
# COMPLETELY into rational quadratics.
QUADRATIC_CROSS_CORES = ((16, 8), (20, 10))
QUADRATIC_CROSS_PATTERN = (2, 2, 2, 2)
FACTORING_IS_A_VALIDITY_SIGNATURE = False

# --- D: THE UNIFORM VOLUME DIAL ---------------------------------------------
DIAL_WIDTH = 16
DIAL_CORE = 3
DIAL_HEAVY = (31260675, -302948719, 31260675)
DIAL_LIGHT = (50327125, -139773119, 50327125)
DIAL_FACTORS = ((DIAL_HEAVY, 2), (DIAL_LIGHT, 2))
DIAL_DISCRIMINANTS = {DIAL_HEAVY: 87869007137918461,
                      DIAL_LIGHT: 9405246751925661}
DIAL_DISCRIMINANT_FACTORIZATIONS = {
    DIAL_HEAVY: {7: 2, 13: 1, 23: 1, 37: 1, 101: 2, 577: 1, 27539: 1},
    DIAL_LIGHT: {3: 7, 7: 2, 13: 1, 31: 1, 37: 1, 101: 2, 577: 1},
}
TRACE_MOTIONS = {
    "heavy": sp.Rational(-2071568131893, 3135706208125),
    "light": sp.Rational(710938392957, 79576897760125),
}
TRACE_MOTION_SIGNS = {"heavy": -1, "light": 1}
# THE ONE NUMERIC LAYER, AS INTEGERS OVER 10^10 (ten decimal places), evalf of
# EXACT acosh expressions at 40 digits.  THE EXACT TRACES ABOVE ARE PRIMARY.
DECIMAL_SCALE = 10 ** 10
DECIMAL_PRECISION = 40
THETA_DECIMALS = {
    ("v1", "heavy"): 23276840296,
    ("v1", "light"): 8506775060,
    ("v45", "heavy"): 22603806617,
    ("v45", "light"): 8553292810,
}
RATIO_DECIMALS = {"v1": 27362708113, "v45": 26427023041}
# THE WITHDRAWN SOLVE VALUE, KEPT AS A LITERAL SO THE CORRECTION IS A GATE AND
# NOT A SENTENCE.  break_solve_ratio asserts it and must fail.
WITHDRAWN_SOLVE_RATIO = {"v1": 27361000000, "v45": 26449000000}

# --- E: THE LOCALIZED BUMP --------------------------------------------------
BUMP_CORES = (1, 3, 5)
BUMP_COVARIANCE_RESIDUAL = 0
# THE NINE IRREDUCIBLE FACTORS OF THE {3,4} BUMP AND THE FIVE OF THE {2,3}
# BUMP, EXACTLY.  Note that NOT ONE of them is palindromic.
BUMP_FACTORS = {
    ("bump34", 1): (
        ((1345846680, -3973376087, 1478415455), 1),
        ((24349745880, -72455211787, 27315109075), 1),
        ((65582920234848542400, -1482708604980552127920,
          8535510836512821008759, -1754062292362811443250,
          91505439094037734375), 1)),
    ("bump34", 3): (
        ((573370050, -1494466969, 531948700), 1),
        ((706236550, -1827879139, 617587500), 1),
        ((114565459508949172500, -2050729233157099637100,
          9367229822132458083989, -1702027048070120587200,
          78988021416996930000), 1)),
    ("bump34", 5): (
        ((988245625, -2738989093, 1007414244), 1),
        ((12768133475, -35396157503, 12528288900), 1),
        ((28294075662319609375, -513108970448968703250,
          2332339383938836349679, -471493433933816742000,
          24391099255638855600), 1)),
    ("bump23", 1): (
        ((45697029500, -130891378428, 51270183025), 1),
        ((275591336500, -795985875216, 302600810375), 1),
        ((9937582754255248590000, -192382341900779624907600,
          952627399671954338524816, -208498301219103208507500,
          11626341946790146484375), 1)),
    ("bump23", 3): (
        ((256350915125, -689220199737, 228485147500), 1),
        ((302600810375, -807683055651, 275591336500), 1),
        ((569676983190166015625, -11807153474812108893750,
          62297805120356166818873, -11594593711577911854840,
          549400505405519666000), 1)),
    # AND THE ONE THAT DOES NOT MOVE: beyond the {2,3} bump's reach the whole
    # v = 1 factorization survives EXACTLY.
    ("bump23", 5): ((HEAVY, 1), (LIGHT, 2), (SECOND, 1)),
}
# THE EXACT NON-PALINDROMICITY STATEMENT, AS INTEGER DIFFERENCES a - e that
# must all be NONZERO.  Only the moved cores carry it.
NONPALINDROMIC_CORES = (("bump34", 1), ("bump34", 3), ("bump34", 5),
                        ("bump23", 1), ("bump23", 3))
NONPALINDROMIC_FACTOR_COUNT = 15
BUMP_QUARTIC_PRIMES = {("bump34", 1): 61, ("bump34", 3): 11, ("bump34", 5): 11,
                       ("bump23", 1): 19, ("bump23", 3): 7}
BUMP_QUADRATIC_DISCRIMINANTS = {
    ("bump34", 1): (7828835401653673969, 2589293856456096289369),
    ("bump34", 3): (1013417710566306961, 1596490685498881321),
    ("bump34", 5): (3519770374790232649, 613036506422939485009),
    ("bump23", 1): (7760972682126606801184, 300016866514464258296656),
    ("bump23", 3): (240734977109127751119169, 318775271356819098283801),
}
BUMP_QUARTIC_REAL_ROOTS = {("bump34", 1): 2, ("bump34", 3): 0,
                           ("bump34", 5): 2, ("bump23", 1): 2,
                           ("bump23", 3): 0}
# nnz(W_bump - W_{v=1}) AT EACH PROBED CORE.  The ZERO is the whole of the
# position-dependence finding.
OPERATOR_CENSUS = {
    ("bump34", 1): 64, ("bump34", 3): 64, ("bump34", 5): 64,
    ("bump23", 1): 64, ("bump23", 3): 64, ("bump23", 5): 0,
}
OUT_OF_RANGE_CORE = ("bump23", 5)
# THE MAX MATCHED ROOT DISPLACEMENT, as an integer over 10^10.
MAX_SHIFT_DECIMALS = {
    ("bump34", 1): 9570159788, ("bump34", 3): 13978902241,
    ("bump34", 5): 144654296, ("bump23", 1): 6880075885,
    ("bump23", 3): 737486236, ("bump23", 5): 0,
}
# THE COMPLETE COMPLEX-PAIR INVENTORY, as (Re, |Im|) integers over 10^10.  THE
# SOLVE'S 0.002-0.003 DESCRIBES TWO OF THESE SIX PAIRS AND NOT THE OTHER FOUR.
COMPLEX_INVENTORY = {
    ("bump34", 1): ((111984320472, 139861010),),
    ("bump34", 3): ((937130291, 28458544), (88563197380, 111282045)),
    ("bump34", 5): ((1046641456, 18623814),),
    ("bump23", 1): ((95662376816, 104655833),),
    ("bump23", 3): ((956422612, 9275825), (102673825961, 95053781)),
    ("bump23", 5): (),
}
# THE SOLVE'S BAND, KEPT AS A LITERAL SO THE COMPLETION IS A GATE.  A pair is
# "inside the band" iff 0.002 <= |Im| <= 0.003, and the split is reported as a
# THREE-WAY partition (below, inside, above) of ALL SEVEN measured pairs so the
# completion is a census and not an adjective.
SMALL_IMAGINARY_BAND = (20000000, 30000000)
SMALL_IMAGINARY_SPLIT = (2, 1, 4)
SMALL_IMAGINARY_TOTAL = 7
SMALL_IMAGINARY_DESCRIPTION_COMPLETE = False
PENCIL_RESIDUAL = 0
# --- E: THE HYBRIDIZATION, WHICH REPLACES BOUNDARY-MODE DOMINANCE -----------
HYBRID_CORE = 1
HYBRID_ISOMETRY_RESIDUAL = 0
HYBRID_COMMUTATOR_RESIDUAL = 0
BASELINE_SECTORS = {1: ((LIGHT, 2),), -1: ((HEAVY, 1), (NEAR, 1))}
BUMPED_SECTORS = {
    1: (BUMP_FACTORS[("bump34", 1)][0], BUMP_FACTORS[("bump34", 1)][1]),
    -1: (BUMP_FACTORS[("bump34", 1)][2],),
}
# THE TWO LARGE-ROOT DISPLACEMENTS, COMPARABLE RATHER THAN DOMINATED, and the
# baseline separation that makes the "which one is the boundary root" question
# non-invariant in the first place.
BOUNDARY_ROOT_SHIFT = 9570159788
HEAVY_ROOT_SHIFT = 9443699527
BASELINE_LARGE_SEPARATION = 126473949
LIGHT_ROOT_SHIFTS = (1744261414, 1914492821)
SHIFTS_COMPARABLE = True

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO, so a residual, a discriminant or a coefficient vector passed
# through it can silently lose its sign -- and this block is nothing but zeros,
# counts, signs, exact coefficient vectors and one gated decimal layer.  Every
# mass, shear and volume here is ALREADY an exact sympy Rational.  Gate F counts
# the occurrences in this file's own source and requires ZERO.
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
    sympy fallbacks purely because those are slow at dimensions 64 and 80, and it
    changes NO value."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


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


VARIABLE = sp.Symbol("z")


def char_factors(matrix: sp.Matrix) -> tuple:
    """THE EXACT RATIONAL FACTORIZATION of the characteristic polynomial, as
    (primitive coefficient vector, multiplicity) pairs sorted by degree then
    lexicographically.  sympy's factor_list over Q is exact."""
    expression = matrix.charpoly(VARIABLE).as_expr()
    factors = []
    for factor, multiplicity in sp.factor_list(expression)[1]:
        if factor.has(VARIABLE):
            factors.append(
                (primitive_coefficients(factor, VARIABLE), multiplicity))
    return tuple(sorted(factors, key=lambda item: (len(item[0]), item[0])))


def degree_pattern(factors: tuple) -> tuple:
    degrees = []
    for coefficients, multiplicity in factors:
        degrees.extend([len(coefficients) - 1] * multiplicity)
    return tuple(sorted(degrees))


def discriminant(coefficients: tuple) -> int:
    a, b, c = coefficients
    return int(b * b - 4 * a * c)


def irreducible_modulo(coefficients: tuple, prime: int) -> bool:
    """A GAUSS'S-LEMMA CERTIFICATE, not a search: a primitive integer polynomial
    that stays irreducible modulo a prime not dividing its leading coefficient is
    irreducible over Q."""
    polynomial = sp.Poly(list(coefficients), VARIABLE, modulus=prime)
    return bool(polynomial.degree() == len(coefficients) - 1
                and polynomial.is_irreducible)


def real_root_count(coefficients: tuple) -> int:
    """EXACT Sturm count over Q -- no estimate and no sampling."""
    return int(sp.Poly(list(coefficients), VARIABLE).count_roots())


def is_exact_rational(value: object) -> bool:
    expression = sp.sympify(value)
    return bool(not expression.atoms(sp.Float) and expression.is_rational)


def decimal10(value: object) -> int:
    """THE BLOCK'S ONE NUMERIC LAYER, AND IT IS A ROUNDING OF AN EXACT OBJECT.
    Returns round(value * 10^10) as an integer, evaluated at 40 digits.  The
    argument is always an exact algebraic or exact-rational expression; nothing
    numeric is ever fed back into a construction."""
    scaled = sp.N(value * DECIMAL_SCALE, DECIMAL_PRECISION)
    return int(sp.floor(scaled + sp.Rational(1, 2)))


# ---------------------------------------------------------------------------
# THE WIDTH FAMILY AT A VOLUME PROFILE.  Everything except the shear block is
# rebuilt here at general even T; the profile placement is the ONE new element.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def site_index(width: int, time: int, space: int) -> int:
    """idx(t,x) = (t mod T)*4 + (x mod 4): the t-major ordering Blocks 107, 128,
    188 and 190 all use."""
    return (time % width) * SPACE_EXTENT + space % SPACE_EXTENT


def staggered_kernel(width: int) -> sp.Matrix:
    """THE STAGGERED KERNEL AT GENERAL EVEN WIDTH, Block 190's wrap-edge
    convention unchanged: eta_t = 1, eta_x = (-1)^t, and the temporal edge sign
    -1 on the WRAP EDGE t = T-1.  Every bond is antisymmetrized."""
    size = width * SPACE_EXTENT
    kernel = sp.zeros(size, size)
    for time in range(width):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if time == width - 1 else 1
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


def anchor_theta(width: int, time: int) -> int:
    """thA_s(t) = -1-t: the ANCHOR reflection, which is theta_s shifted by the
    one-cell width of the anchor.  It is the map that sends an image anchor to
    the positive anchor whose cell it mirrors, and it is what carries a
    NON-UNIFORM volume profile across the seam."""
    return (-1 - time) % width


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
    (1, dx, dt, dx^dt) -- Block 190's, unchanged."""
    matrix = sp.zeros(width * SPACE_EXTENT, 4)
    for column, (delta_t, delta_x) in enumerate(
            ((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[site_index(width, time + delta_t, space + delta_x), column] = 1
    return matrix


def imported_shear_block(shear: object, volume: object) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT, now read AT A VOLUME: the LANDED Block 105
    shear Hodge diag(v, v g(c)^-1, 1/v).  NO nsimplify: both arguments are
    already sympy Rationals or Integers."""
    return sp.Matrix(b128.block105.shear_hodge(shear, volume))


def displayed_shear_block(shear: object, volume: object) -> sp.Matrix:
    """THE NOTE'S DISPLAYED LAW, BUILT FROM THE FORMULA AND NOT FROM THE IMPORT.
    Gate C-2 compares this to imported_shear_block entrywise at BOTH probed
    volumes, so the note's formula and the landed function are measured to be
    the same thirty-two numbers."""
    denominator = 1 - shear ** 2
    return sp.Matrix([
        [volume, 0, 0, 0],
        [0, volume / denominator, -volume * shear / denominator, 0],
        [0, -volume * shear / denominator, volume / denominator, 0],
        [0, 0, 0, 1 / volume]])


def site_hodge_profile(width: int, shear: object, profile: dict) -> sp.Matrix:
    """THE SITE-ADAPTED GLUED HODGE AT A VOLUME PROFILE.  The positive anchors
    t < T/2 carry B(c, v(t)); the image anchors t >= T/2 carry the P_4 image of
    the block of their thA_s(t) = -1-t partner, UNFLIPPED otherwise.  At a
    UNIFORM profile this is Block 190's rule identically."""
    half = width // 2
    blocks = []
    for time in range(width):
        if time < half:
            blocks.append(displayed_shear_block(shear, profile[time]))
        else:
            partner = anchor_theta(width, time)
            block = displayed_shear_block(shear, profile[partner])
            blocks.append(sp.expand(
                OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T))
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


def build_profile_action(width: int, profile: dict) -> dict:
    """THE FAMILY, REBUILT WHOLE at a width and a volume profile.
    Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    kernel = staggered_kernel(width)
    raising = raising_part(width, kernel)
    reflection = reflection_permutation(width)
    restricted = site_restricted_raising(width, raising)
    glue = sp.expand(restricted - reflection * restricted * reflection)
    hodge = site_hodge_profile(width, FIXTURE_SHEAR, profile)
    action = sp.expand(FIXTURE_MASS * hodge + hodge * glue - glue.T * hodge)
    return {"reflection": reflection, "hodge": hodge, "action": action}


def uniform_profile(width: int, volume: object) -> dict:
    return {time: volume for time in range(width // 2)}


def bump_profile(width: int, anchors: tuple, volume: object) -> dict:
    return {time: (volume if time in anchors else UNIT_VOLUME)
            for time in range(width // 2)}


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


def core_operators(width: int, inverse: sp.Matrix, core: int) -> dict:
    """K_c, L_2 and W = K_c^-1 L_2 at one core.  THE ONE PLACE the monodromy is
    formed, so no family can build it differently."""
    gram = shifted_pairing(width, inverse, core, 0)
    second = shifted_pairing(width, inverse, core, 2)
    return {"K": gram, "L2": second,
            "W": sp.expand(exact_inverse(gram) * second)}


def spatial_shift(core: int, amount: int) -> sp.Matrix:
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    matrix = sp.zeros(len(cells), len(cells))
    for time, space in cells:
        matrix[position[(time, (space + amount) % SPACE_EXTENT)],
               position[(time, space)]] = 1
    return matrix


def sector_block(projector: sp.Matrix, operator: sp.Matrix) -> sp.Matrix:
    """THE OPERATOR RESTRICTED TO AN INVARIANT SUBSPACE, in an exact basis of the
    projector's column space: (B^T B)^-1 B^T M B.  Exact throughout."""
    basis = sp.Matrix.hstack(*projector.columnspace())
    gram = sp.expand(basis.T * basis)
    return sp.expand(exact_inverse(gram) * basis.T * operator * basis)


def exact_root_list(factors: tuple) -> list:
    """THE EIGHT ROOTS as EXACT algebraic numbers (CRootOf), with multiplicity,
    of the product of the primitive rational factors.  No float is created."""
    roots = []
    for coefficients, multiplicity in factors:
        for root in sp.Poly(list(coefficients), VARIABLE).all_roots():
            roots.extend([root] * multiplicity)
    return roots


def high_modulus(first: object, second: object) -> object:
    """|second - first| at 40 digits, from EXACT algebraic roots."""
    difference = sp.N(second - first, DECIMAL_PRECISION)
    return sp.sqrt(sp.re(difference) ** 2
                   + sp.im(difference) ** 2).evalf(DECIMAL_PRECISION)


def matched_displacements(baseline: list, moved: list) -> list:
    """THE MINIMUM-TOTAL-DISTANCE PERFECT MATCHING between two eight-root lists,
    SELECTED combinatorially over all 8! bijections in machine precision and
    then REPORTED at 40 digits from the exact algebraic roots.  The selection is
    a choice of pairing; every VALUE returned is high-precision."""
    left = [complex(sp.N(root, 30)) for root in baseline]
    right = [complex(sp.N(root, 30)) for root in moved]
    best_total, best_permutation = None, None
    for permutation in itertools.permutations(range(len(right))):
        total = sum(abs(left[i] - right[permutation[i]])
                    for i in range(len(left)))
        if best_total is None or total < best_total:
            best_total, best_permutation = total, permutation
    return sorted(
        (decimal10(high_modulus(baseline[i], moved[best_permutation[i]])),
         i, best_permutation[i]) for i in range(len(baseline)))


def conjugate_inventory(roots: list) -> tuple:
    """THE COMPLETE (Re, |Im|) INVENTORY of the nonreal roots, at ten decimals.
    A root counts as nonreal by its EXACT algebraic type, not by a threshold."""
    pairs = set()
    for root in roots:
        if not root.is_real:
            pairs.add((decimal10(sp.re(root)), decimal10(sp.Abs(sp.im(root)))))
    return tuple(sorted(pairs))


def note_text() -> tuple:
    """(text, at_final_path).  THE FINAL PATH IS THE ONLY PATH READ: there is no
    draft fallback anywhere in this runner."""
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
# BYTE-IDENTICALLY in the note and gate F checks it as a raw substring.
# ---------------------------------------------------------------------------
N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE HEADLINE WORD IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY (the staggered Dirac-Kahler carrier on Z_T x Z_4 for even T with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, T/2}, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at (m, c) = (9/20, 5/13), at widths T = 16 and T = 20), THE VOLUME PROFILE (a map v from the positive anchors {0..T/2-1} to the positive rationals, placed as B(c, v(t)) for t < T/2 and as the P_4 image of the block of its thA_s(t) = -1-t partner for t >= T/2, assembled by the same quarter-weighted four-corner cell average and reducing to Block 190's rule IDENTICALLY at any uniform profile) -- THIS BLOCK'S ONE NEW CONSTRUCTION ELEMENT -- THE FOUR PROBED PROFILES (uniform v = 1, uniform v = 4/5, and the LOCALIZED bumps v = 4/5 on the positive anchors {3,4} and on {2,3}), THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2, THE SINGLE FIXTURE (9/20, 5/13) AND THE SINGLE BUMP AMPLITUDE 4/5, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. LAPSE PHYSICALITY IS A READING AND IS NOT ESTABLISHED BY ANYTHING HERE: v is the IMPOSED Block 105 Hodge-volume parameter, and this block supplies NO lapse variable in an ADM phase space, NO Hamiltonian constraint, NO gauge orbit, NO quotient, NO Dirac observable and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, UNIFORM AND LOCALIZED CHANGES OF THE HODGE VOLUME ALTER THE EXACT MONODROMY SPECTRUM WHILE THE SPECIFIED REFLECTION COVARIANCE SURVIVES EXACTLY. Ps-COVARIANCE DOES NOT DECIDE PHYSICAL EQUIVALENCE: Ps H Ps = H and Ps Q Ps = Q^T at ZERO for every profile proves COMPATIBILITY WITH ONE REFLECTION and does NOT prove that two v(t) profiles are physically inequivalent. THE PHYSICAL VOLUME DIAL IS A READING. THE PHYSICAL BOUNDARY MODE IS A READING: 'boundary mode' NAMES AN EXACT RATIONAL FACTOR at a seam-adjacent core. W IS NOT A TRANSFER OPERATOR: Block 190 refuted the naive OS transfer pairing on this class with six exact witnesses and NOTHING HERE REPAIRS IT. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NO GENERALITY IS CLAIMED: ONE fixture, TWO widths, FOUR profiles, ONE bump amplitude, and NOTHING about the infinite-width limit. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONSTRUCTION CONTROL IS THE VOLUME LAW ITSELF, DISPLAYED RATHER THAN DESCRIBED. Block 190 displayed the landed shear block at the PINNED volume v = 1; this block needs v as a VARIABLE, so the LAW is displayed: shear_hodge(c, v) = diag(v, v g(c)^-1, 1/v) with g(c) = [[1,c],[c,1]], which at c = 5/13 is diag(1, 169/144, 169/144, 1) with (1,2) = (2,1) = -65/144 at v = 1 -- BLOCK 190's PINNED MATRIX -- and diag(4/5, 169/180, 169/180, 5/4) with (1,2) = (2,1) = -13/36 at v = 4/5. BOTH displayed matrices are gated ENTRYWISE against b128.block105.shear_hodge at ZERO residual, thirty-two numbers in all. AND EVERY PROFILE IS COVARIANT AT ZERO: nnz(Ps H Ps - H) = 0 and nnz(Ps Q Ps - Q^T) = 0 for uniform v = 1, uniform v = 4/5, the {3,4} bump AND the {2,3} bump -- which is COMPATIBILITY WITH THE REFLECTION AND NOT AN EQUIVALENCE STATEMENT. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, so any of this block's zeros, counts, signs, discriminants or coefficient vectors could be manufactured by it; this runner calls it ZERO TIMES, counted in its own source by gate F.\nper_mode: THE BOUNDARY MONODROMY IS SCANNED AT EVERY CORE OF TWO WIDTHS AND THE LAYER IS POSITIONALLY WIDTH-LOCKED. With heavy = 22569375 z^2 - 233631106 z + 22569375, light = 39529825 z^2 - 109432706 z + 39529825, near = 43033320714375 z^2 - 445467467014578 z + 48554286398375, mirror = rev(near), second = 48554286398375 z^2 - 376762652339458 z + 35686537764375 and rev(second): charpoly(W) = heavy*light^2*near at t0 = 1, heavy^2*light^2 at the interior cores, heavy*light^2*mirror at t0 = T/2-4, heavy*light^2*second at t0 = T/2-3 and heavy*light^2*rev(second) at t0 = T/2 -- THE SAME POLYNOMIAL AT THE SAME RELATIVE POSITION AT BOTH T = 16 AND T = 20. THE LIGHT PAIR IS BOUNDARY-RIGID: light^2 divides charpoly(W) with multiplicity EXACTLY TWO at every tabulated core at both widths, so the light mode does not see the boundary. THE HEAVY SECTOR LOSES EXACTLY ONE COPY at each layer core, so the layer is MODE-SELECTIVE. THE BOUNDARY FACTORS ARE POSITIVE AND NON-RECIPROCAL, EXACTLY: near - its reversal has a - c = -5520965684000 and mirror +5520965684000, second +12867748634000 and rev(second) -12867748634000, all NONZERO, which is the exact statement that the seam breaks lambda -> 1/lambda; and the discriminants 190083455453828589664707955584 = 2^7*3^4*13*313*70619*96676423*659962871 and 135019158697151741387932171264 = 2^10*13*313*32404681043299888780819 are POSITIVE with a > 0, -b > 0 and c > 0, which is the exact statement that both roots are REAL AND POSITIVE. POSITIVITY SURVIVES AT THE SEAM; RECIPROCITY DOES NOT. AND THE NEAR/FAR REVERSAL IS EXACT COEFFICIENT FOR COEFFICIENT: mirror(z) = rev(near)(z) and rev(second) is the reversal of second, at BOTH widths.\nper_block: THE VALIDITY BOUNDARY IS A RULE ABOUT THE PAIRING AND NOT ABOUT FACTORING, AND THE ADVERSARIAL CHECK'S CORRECTION IS CARRIED AS CONTENT AND THEN STRENGTHENED AGAINST THIS BLOCK'S OWN SOLVE. L_2 reads G at times {t0+2, t0+3}: t0+3 < T/2 is interior, t0+3 = T/2 TOUCHES the fixed slice and is ADMISSIBLE, t0+3 > T/2 CROSSES into the image half and is NOT A BULK OBJECT -- verified at both widths, T = 20 t0 = 7 and T = 16 t0 = 5 touching and factoring exactly as the table says, T = 20 t0 = 8 and T = 16 t0 = 6 crossing. THE SOLVE'S 'NON-FACTORING OVER Q' SIGNATURE IS WITHDRAWN AND IS FALSE IN BOTH DIRECTIONS, MEASURED IN BOTH: crossing cores at t0 = T/2-2 and T/2-1 DO factor over Q, with degree pattern (2,2,4) -- two rational quadratics and ONE IRREDUCIBLE RATIONAL QUARTIC, certified irreducible modulo 11 at T = 16 and modulo 67 at T = 20 and therefore over Q by Gauss's lemma -- so the true signature is FAILURE TO SPLIT COMPLETELY INTO RATIONAL QUADRATICS and never irreducibility; AND the crossing core at t0 = T/2 factors COMPLETELY into rational quadratics as heavy*light^2*rev(second), so a CROSSING core can look EXACTLY like a clean bulk core. NO FACTORING SIGNATURE CAN DEFINE THE VALIDITY BOUNDARY IN EITHER DIRECTION, AND THE RULE STANDS ON THE PAIRING'S DEFINITION ALONE.\nlattice_wide: THE UNIFORM VOLUME DIAL PRESERVES THE FORM AND MOVES THE TWO SCALES IN OPPOSITE DIRECTIONS, AND THE SOLVE'S RATIO PAIR IS CORRECTED AS CONTENT. At T = 16, t0 = 3, uniform v = 4/5 the exact spectrum is (31260675 z^2 - 302948719 z + 31260675)^2 (50327125 z^2 - 139773119 z + 50327125)^2: both factors PALINDROMIC and SQUARED, discriminants 87869007137918461 = 7^2*13*23*37*101^2*577*27539 and 9405246751925661 = 3^7*7^2*13*31*37*101^2*577 both POSITIVE, both traces above twice the leading coefficient, so reciprocity, positivity and the two-scale structure ALL SURVIVE. THE TWO EXACT RATIONAL TRACE MOTIONS HAVE OPPOSITE SIGNS: 302948719/31260675 - 233631106/22569375 = -2071568131893/3135706208125 < 0 and 139773119/50327125 - 109432706/39529825 = +710938392957/79576897760125 > 0, and since acosh(x/2) is strictly increasing for x > 2 the heavy rapidity STRICTLY DECREASES and the light one STRICTLY INCREASES -- a theorem about two rational numbers and not an inference from decimals. THE EXACT TRACES ARE PRIMARY AND THE DECIMALS ARE THIS BLOCK'S ONE NUMERIC LAYER, evalf of exact acosh expressions at 40 digits gated to TEN places: theta_heavy 2.3276840296 -> 2.2603806617, theta_light 0.8506775060 -> 0.8553292810, and the RATIO 2.7362708113 -> 2.6427023041. THE SOLVE'S QUOTED PAIR 2.7361 -> 2.6449 IS WITHDRAWN AND CORRECTED HERE AS CONTENT, with the withdrawn value kept as a literal so that break_solve_ratio is a GATE and not a sentence. THAT THE RATIO MOVING MEANS THE DIAL IS NOT A CONFORMAL OR GAUGE RESCALING IS A READING.\nper_scope: THE LOCALIZED BUMP KILLS PALINDROMICITY EVERYWHERE IT REACHES, AND BOUNDARY-MODE DOMINANCE IS REFUTED AND REPLACED BY MEASURED HYBRIDIZATION. With v = 4/5 on the positive anchors {3,4}, Ps H Ps = H and Ps Q Ps = Q^T at ZERO, and at t0 = 1, 3 AND 5 -- inside the bump AND away from it -- every one of the NINE irreducible factors has leading != constant as an exact integer inequality, so W is no longer conjugate to its inverse at ANY probed core; the quartics are certified irreducible modulo 61, 11 and 11. Root reality is decided by EXACT quadratic discriminants and EXACT Sturm counts and never estimated: 6 real plus one conjugate pair at t0 = 1, 4 real plus two pairs at t0 = 3, 6 real plus one pair at t0 = 5. THE COMPLEX-PAIR DESCRIPTION IS COMPLETED RATHER THAN REPEATED AND THE COMPLETION IS A CENSUS AND NOT AN ADJECTIVE: of the SEVEN nonreal pairs measured across the two bump positions, TWO lie BELOW the solve's |Im| ~ 0.002-0.003 band, EXACTLY ONE lies INSIDE it and FOUR lie ABOVE it, and the complete inventory carries 11.1984320472 +/- 0.0139861010 i at t0 = 1 and 8.8563197380 +/- 0.0111282045 i at t0 = 3, four to five times the quoted band. THE MAX MATCHED DISPLACEMENTS ARE 0.9570159788 at t0 = 1, 1.3978902241 at t0 = 3 and 0.0144654296 at t0 = 5. AND THE CHECK'S P1 IS FOLDED: U remains an exact Gram isometry and an exact commutant AT THE BUMPED CORE, and the grading is exactly what refutes the dominance claim -- the baseline U = -1 sector is heavy TIMES near, two labelled rational factors, and after the bump it is ONE IRREDUCIBLE NONPALINDROMIC QUARTIC, so the two factors HYBRIDIZE; the two baseline large roots were already only 0.0126473949 apart and become ONE CONJUGATE PAIR WITH A COMMON REAL PART, with matched displacements 0.9570159788 and 0.9443699527 -- COMPARABLE AND NOT DOMINATED -- so assigning either post-bump member as uniquely 'the boundary root' is NOT INVARIANT and 'the edge mode is the bump's antenna' IS WITHDRAWN. AND THE REACH IS BUMP-POSITION DEPENDENT: the {2,3} profile is also exactly Ps-covariant, its t0 = 1 response REVERSES SIGN and falls to 0.6880075885, its t0 = 3 response falls from 1.3978902241 to 0.0737486236, and at t0 = 5 THE OPERATOR ITSELF is unchanged at EXACTLY ZERO ENTRIES. NEAR-EDGE COUPLING IS GENERIC ACROSS THESE TWO POSITIONS; MAGNITUDE, SIGN AND REACH ARE NOT.\nRESULT: A MODE-SELECTIVE, POSITIONALLY WIDTH-LOCKED, NON-RECIPROCAL BOUNDARY LAYER OF THE UNIT-CELL MONODROMY IS COMPUTED IN CLOSED FORM AT EVERY CORE OF TWO WIDTHS, THE HODGE VOLUME IS SHOWN TO MOVE THE TWO EXACT SCALES IN OPPOSITE DIRECTIONS, AND A LOCALIZED VOLUME BUMP IS SHOWN TO DESTROY PALINDROMICITY IN EVERY IRREDUCIBLE FACTOR IT REACHES -- AND NOT ONE LINE OF IT IS A LAPSE, A CONSTRAINT, A GAUGE ORBIT OR A PHYSICAL TRANSFER OPERATOR. The volume law is displayed and gated entrywise at both probed volumes; every profile is Ps-covariant at zero; the light pair is boundary-rigid and the heavy sector loses exactly one copy at each layer core; the boundary factors are positive and exactly non-reciprocal with factored discriminants and an exact near/far coefficient reversal; the touch/cross rule is verified at both widths and the factoring signature is withdrawn in BOTH directions; the uniform dial preserves palindromicity, positivity and the two-scale structure while moving the two exact rational traces oppositely; the corrected ratio pair is 2.7362708113 -> 2.6427023041; the bump breaks palindromicity in fifteen irreducible factors across five moved cores, with exact reality certificates and a COMPLETE complex-pair inventory; and boundary-mode dominance is REFUTED and replaced by hybridization with comparable displacements. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-190 STAND EXACTLY AS LANDED. BLOCK 190 IS NOT CORRECTED: its deep-core spectrum is reproduced here digit-for-digit as the control at T = 16 t0 = 3 and at T = 20 t0 = 2,3,4,5, and this block only computes the cores it did not. BLOCK 188 IS NEITHER CORRECTED NOR CONTRADICTED and the wrap-edge object remains a DISCLOSED VARIANT of theirs. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE FIXTURE, TWO WIDTHS, ONE BUMP AMPLITUDE AND NO WINDOW; the widths stop at 20 so nothing is proven about the infinite-width limit; the bump is probed at TWO positions and TWO positions are not a scan; and the block's own solve language is corrected in four places rather than papered over. FOUR ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C2 NARROWING, that crossing cores DO factor as (2,2,4) so the non-factoring signature is dropped and the touch/cross rule rests on the pairing's definition -- strengthened here by the measured all-quadratic crossing core at t0 = T/2; the C3 NUMERICAL CORRECTION, that the ratio pair is 2.7362708113 -> 2.6427023041 and not 2.7361 -> 2.6449; the C4 COMPLETION, that the complex-pair band 0.002-0.003 captures EXACTLY ONE of the SEVEN measured pairs -- two lie below it and four above -- with additional pairs at |Im| ~ 0.0111 and ~ 0.0140; and the P1 REFUTATION, that the near-edge response is NOT boundary-mode dominated but a hybridization of the boundary and bulk-heavy factors inside one irreducible U = -1 quartic with comparable displacements. AND THE CHECK'S PHYSICALITY FENCE IS ADOPTED AS THE BLOCK'S OWN HEADLINE: the package establishes HODGE-VOLUME SPECTRAL SENSITIVITY, and LAPSE PHYSICALITY STAYS A READING. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE BOUNDARY-LAYER SOLVE (block 191 candidate), PHASE 4 and B191 CHECK VERDICT anchors.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


# ---------------------------------------------------------------------------
# the claims: every expected value the gates compare against, in ONE place
# ---------------------------------------------------------------------------
def rewritten(mapping: dict, *pairs) -> dict:
    """A COPY of `mapping` with the given keys rewritten, used only by the
    mutation table.  Written out rather than spelled `dict(mapping, **{...})`
    because most of these dictionaries are keyed by TUPLES -- a coefficient
    vector or a (width, core) pair -- and keyword unpacking accepts only string
    keys, so the idiomatic spelling would raise instead of mutating a claim."""
    updated = dict(mapping)
    for key, value in pairs:
        updated[key] = value
    return updated


def build_claims(mutation: str) -> dict:
    claims: dict = {
        # A -- the authority pins.
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        # B -- the banner's declared status flags.
        "objects_registered": False,
        "lapse_physicality_claimed": LAPSE_PHYSICALITY_CLAIMED,
        "volume_dial_physical_claimed": VOLUME_DIAL_PHYSICAL_CLAIMED,
        "boundary_mode_physical_claimed": BOUNDARY_MODE_PHYSICAL_CLAIMED,
        "profiles_inequivalent_claimed": PROFILES_INEQUIVALENT_CLAIMED,
        "transfer_operator_claimed": TRANSFER_OPERATOR_CLAIMED,
        "edge_dominance_claimed": EDGE_DOMINANCE_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        # C -- the construction control, the scan and the validity rule.
        "citation_pins": True,
        "hodge_display_residuals": {"v1": ZERO_RESIDUAL, "v45": ZERO_RESIDUAL},
        "profile_covariance": {name: (ZERO_RESIDUAL, ZERO_RESIDUAL)
                               for name in PROFILE_NAMES},
        "core_table": dict(CORE_TABLE),
        "light_multiplicity": 2,
        "heavy_layer_multiplicity": 1,
        "boundary_asymmetry": dict(BOUNDARY_ASYMMETRY),
        "boundary_discriminants": dict(BOUNDARY_DISCRIMINANTS),
        "boundary_discriminant_factorizations":
            dict(BOUNDARY_DISCRIMINANT_FACTORIZATIONS),
        "boundary_roots_positive": True,
        "reversal_exact": True,
        "touch_admissible": True,
        "crossing_pattern": CROSSING_PATTERN,
        "crossing_irreducible": dict(CROSSING_CERTIFICATE_PRIMES),
        "factoring_is_a_validity_signature": FACTORING_IS_A_VALIDITY_SIGNATURE,
        "quadratic_cross_pattern": QUADRATIC_CROSS_PATTERN,
        # D -- the uniform volume dial.
        "dial_factors": DIAL_FACTORS,
        "dial_palindromic": True,
        "dial_discriminants": dict(DIAL_DISCRIMINANTS),
        "dial_discriminant_factorizations":
            dict(DIAL_DISCRIMINANT_FACTORIZATIONS),
        "dial_trace_bound": True,
        "trace_motions": dict(TRACE_MOTIONS),
        "trace_motion_signs": dict(TRACE_MOTION_SIGNS),
        "theta_decimals": dict(THETA_DECIMALS),
        "ratio_decimals": dict(RATIO_DECIMALS),
        # E -- the bump package.
        "bump_covariance": BUMP_COVARIANCE_RESIDUAL,
        "bump_factors": dict(BUMP_FACTORS),
        "nonpalindromic_count": NONPALINDROMIC_FACTOR_COUNT,
        "bump_quartic_primes": dict(BUMP_QUARTIC_PRIMES),
        "bump_quadratic_discriminants": {
            key: tuple(sorted(value))
            for key, value in BUMP_QUADRATIC_DISCRIMINANTS.items()},
        "bump_quartic_real_roots": dict(BUMP_QUARTIC_REAL_ROOTS),
        "operator_census": dict(OPERATOR_CENSUS),
        "max_shift_decimals": dict(MAX_SHIFT_DECIMALS),
        "complex_inventory": dict(COMPLEX_INVENTORY),
        "small_imaginary_split": SMALL_IMAGINARY_SPLIT,
        "small_imaginary_description_complete":
            SMALL_IMAGINARY_DESCRIPTION_COMPLETE,
        "pencil_residual": PENCIL_RESIDUAL,
        "hybrid_isometry": (HYBRID_ISOMETRY_RESIDUAL,
                            HYBRID_COMMUTATOR_RESIDUAL),
        "baseline_sectors": dict(BASELINE_SECTORS),
        "bumped_sectors": dict(BUMPED_SECTORS),
        "boundary_root_shift": BOUNDARY_ROOT_SHIFT,
        "heavy_root_shift": HEAVY_ROOT_SHIFT,
        "baseline_large_separation": BASELINE_LARGE_SEPARATION,
        "light_root_shifts": LIGHT_ROOT_SHIFTS,
        "shifts_comparable": SHIFTS_COMPARABLE,
        # F -- the note, the fence and the nsimplify absence.
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
    elif mutation == "claim_lapse_physicality":
        # THE HEADLINE FENCE DENIED, AND THIS IS THE MUTATION THAT GUARDS THE
        # WHOLE BLOCK: v asserted to BE a lapse and these shifts asserted to BE
        # lapse physics.  v is the IMPOSED Block 105 Hodge-volume parameter and
        # not one of the ten enumerated gravity structures is supplied here.
        claims["lapse_physicality_claimed"] = True
    elif mutation == "claim_volume_dial_physical":
        # THE SOLVE'S PHASE-2 WORDING ASSERTED AS A RESULT: "the uniform volume
        # dial is NOT a conformal/gauge rescaling: PHYSICAL".  What is measured
        # is that two exact rational traces move oppositely under an imposed
        # change of an imposed parameter.
        claims["volume_dial_physical_claimed"] = True
    elif mutation == "claim_boundary_mode_physical":
        # THE SOLVE'S PHASE-1 WORDING ASSERTED AS A RESULT: "the boundary layers
        # are PHYSICAL".  'Boundary mode' names an exact rational FACTOR of a
        # characteristic polynomial at a seam-adjacent core, and nothing here
        # makes it an excitation of a physical surface.
        claims["boundary_mode_physical_claimed"] = True
    elif mutation == "claim_profiles_inequivalent":
        # THE CHECK'S SHARPEST FENCE DENIED: exact Ps-covariance asserted to
        # prove that two v(t) profiles are physically inequivalent.  It proves
        # compatibility with ONE reflection and nothing more.
        claims["profiles_inequivalent_claimed"] = True
    elif mutation == "claim_transfer_operator":
        # W ASSERTED TO BE A PHYSICAL TRANSFER OPERATOR.  Block 190 refuted the
        # naive OS transfer pairing on this class with six exact witnesses, and
        # this block repairs none of it.
        claims["transfer_operator_claimed"] = True
    elif mutation == "claim_edge_dominance":
        # THE WITHDRAWN HEADLINE ASSERTED AS A DECLARED WORD: "the edge mode is
        # the bump's antenna".  Refuted as stated by the check and replaced by
        # the hybridization measured in family E.
        claims["edge_dominance_claimed"] = True
    elif mutation == "claim_generality":
        # ONE FIXTURE OVERSOLD.  Every statement here is measured at (9/20,
        # 5/13), at two widths, at one bump amplitude, and NOWHERE ELSE.
        claims["generality_claimed"] = True
    elif mutation == "break_volume_law_display":
        # THE DISPLAYED LAW UNGATED at the second volume: if diag(v, v g^-1,
        # 1/v) is not the landed function at v = 4/5, every number in families D
        # and E belongs to some other construction.
        claims["hodge_display_residuals"] = {"v1": ZERO_RESIDUAL, "v45": 1}
    elif mutation == "break_profile_covariance":
        # THE ADMISSIBILITY OF A PROFILE DENIED: the {3,4} bump asserted NOT to
        # be Ps-covariant.  All four profiles are, at exactly zero, and that is
        # what makes a non-uniform volume an admissible object at all.
        claims["profile_covariance"] = dict(
            claims["profile_covariance"], bump34=(0, 16))
    elif mutation == "break_deep_rigidity":
        # THE CONTROL DENIED: the interior cores asserted to carry something
        # other than Block 190's deep spectrum.  Reproducing it digit-for-digit
        # is what attaches this scan to their block.
        claims["core_table"] = rewritten(
            CORE_TABLE,
            ((20, 4), (((HEAVY[0] + 1,) + HEAVY[1:], 2), (LIGHT, 2))))
    elif mutation == "break_light_boundary_rigidity":
        # THE LIGHT MODE'S BLINDNESS TO THE SEAM DENIED: light asserted to lose
        # a copy at the near seam.  Both copies are exact at every tabulated
        # core at both widths, and that is the mode-selectivity of the layer.
        claims["light_multiplicity"] = 1
    elif mutation == "break_heavy_survival":
        # THE OTHER HALF OF MODE-SELECTIVITY DENIED: the heavy pair asserted to
        # lose BOTH copies at a layer core.  It loses exactly one.
        claims["heavy_layer_multiplicity"] = 0
    elif mutation == "break_near_boundary_quadratic":
        # THE BOUNDARY MODE ITSELF ALTERED at one digit, at both widths.
        broken = (NEAR[0] + 1,) + NEAR[1:]
        claims["core_table"] = rewritten(
            CORE_TABLE,
            ((16, 1), ((HEAVY, 1), (LIGHT, 2), (broken, 1))),
            ((20, 1), ((HEAVY, 1), (LIGHT, 2), (broken, 1))))
    elif mutation == "break_nonreciprocity":
        # THE EDGE'S DEFINING PROPERTY DENIED: the boundary quadratic asserted
        # RECIPROCAL, a - c = 0.  It is not, at four exact nonzero integers, and
        # lambda -> 1/lambda breaking is the whole content of the boundary mode.
        claims["boundary_asymmetry"] = rewritten(
            BOUNDARY_ASYMMETRY, (NEAR, 0))
    elif mutation == "break_boundary_positivity":
        # AND THE OTHER HALF DENIED: the boundary roots asserted NOT positive.
        # Positive discriminant with a > 0, -b > 0, c > 0 forces two distinct
        # positive reals, so positivity SURVIVES the seam even though
        # reciprocity does not -- and both halves matter.
        claims["boundary_roots_positive"] = False
    elif mutation == "break_far_reversal":
        # THE MIRROR COVARIANCE OF THE BOUNDARY FACTOR DENIED: mirror asserted
        # NOT to be the exact coefficient reversal of near.
        claims["reversal_exact"] = False
    elif mutation == "break_touch_admissible":
        # THE VALIDITY RULE COLLAPSED FROM THE ADMISSIBLE SIDE: a core whose L_2
        # merely TOUCHES the fixed slice asserted invalid.  It factors exactly
        # as the bulk table says at both widths.
        claims["touch_admissible"] = False
    elif mutation == "break_crossing_pattern":
        # THE CROSSING DEGREE PATTERN ALTERED: (2,2,4) asserted to be (2,2,2,2)
        # at the first crossing core.
        claims["crossing_pattern"] = (2, 2, 2, 2)
    elif mutation == "break_crossing_signature":
        # THE WITHDRAWN SIGNATURE REASSERTED, AND THIS IS THE MUTATION THAT
        # GUARDS THE CHECK'S C2 CORRECTION: factoring behaviour asserted to BE
        # the validity signature.  Crossing cores DO factor -- (2,2,4) at
        # T/2-2 and T/2-1 -- so the signature is false from above.
        claims["factoring_is_a_validity_signature"] = True
    elif mutation == "break_signature_from_below":
        # AND THE SIGNATURE KILLED FROM THE OTHER SIDE IS DENIED, WHICH IS THIS
        # BLOCK'S OWN STRENGTHENING: the t0 = T/2 crossing core asserted NOT to
        # factor completely into rational quadratics.  It does, at both widths,
        # so a crossing core can look exactly like a clean bulk core.
        claims["quadratic_cross_pattern"] = CROSSING_PATTERN
    elif mutation == "break_volume_charpoly":
        # THE DIAL'S HEADLINE SPECTRUM ALTERED at one coefficient.
        claims["dial_factors"] = (
            ((DIAL_HEAVY[0] + 1,) + DIAL_HEAVY[1:], 2), (DIAL_LIGHT, 2))
    elif mutation == "break_volume_palindromy":
        # THE FORM DENIED: the v = 4/5 factors asserted NOT palindromic, which
        # would mean the uniform dial breaks reciprocity.  It does not -- only
        # the LOCALIZED bump does, and that contrast is the block's spine.
        claims["dial_palindromic"] = False
    elif mutation == "break_volume_discriminants":
        # THE DIAL'S REALITY CERTIFICATE ALTERED at one integer.
        claims["dial_discriminants"] = rewritten(
            DIAL_DISCRIMINANTS,
            (DIAL_HEAVY, DIAL_DISCRIMINANTS[DIAL_HEAVY] + 1))
    elif mutation == "break_trace_motion_values":
        # THE EXACT MOTION ALTERED at one rational, which is the PRIMARY
        # statement the decimals are only a reading of.
        claims["trace_motions"] = dict(
            TRACE_MOTIONS, heavy=TRACE_MOTIONS["heavy"] + 1)
    elif mutation == "break_trace_motion_signs":
        # THE OPPOSITENESS DENIED: both scales asserted to move the same way,
        # which is exactly what a conformal rescaling would do and exactly what
        # these two exact rationals forbid.
        claims["trace_motion_signs"] = {"heavy": -1, "light": -1}
    elif mutation == "break_ratio_pair":
        # THE CORRECTED DECIMAL ALTERED at its last place.
        claims["ratio_decimals"] = dict(
            RATIO_DECIMALS, v45=RATIO_DECIMALS["v45"] + 1)
    elif mutation == "break_solve_ratio":
        # THE WITHDRAWN SOLVE VALUE REASSERTED, AND THIS IS THE MUTATION THAT
        # GUARDS THE CHECK'S C3 NUMERICAL CORRECTION: the ratio pair asserted to
        # be 2.7361 -> 2.6449.  The exact factors give 2.7362708113 ->
        # 2.6427023041, and the second was a supervisor arithmetic slip.
        claims["ratio_decimals"] = dict(WITHDRAWN_SOLVE_RATIO)
    elif mutation == "break_bump_covariance":
        # THE BUMP DISQUALIFIED: the localized profile asserted to break
        # Ps-covariance, which would make it an inadmissible object rather than
        # an admissible one whose spectrum moves.
        claims["bump_covariance"] = 16
    elif mutation == "break_bump_factors":
        # THE BUMP'S HEADLINE FACTORIZATION ALTERED at one digit.
        original = BUMP_FACTORS[("bump34", 3)]
        head = original[0][0]
        claims["bump_factors"] = rewritten(
            BUMP_FACTORS,
            (("bump34", 3),
             (((head[0] + 1,) + head[1:], 1),) + original[1:]))
    elif mutation == "break_nonpalindromicity":
        # THE CENTRAL EXACT STATEMENT DENIED: fewer than all fifteen moved
        # irreducible factors asserted non-palindromic.  Every one of them has
        # leading != constant, and that is the exact loss of W ~ W^-1.
        claims["nonpalindromic_count"] = NONPALINDROMIC_FACTOR_COUNT - 1
    elif mutation == "break_bump_irreducibility":
        # A QUARTIC'S IRREDUCIBILITY CERTIFICATE ALTERED: the wrong prime, which
        # would leave the quartic's irreducibility asserted rather than
        # certified.
        claims["bump_quartic_primes"] = rewritten(
            BUMP_QUARTIC_PRIMES, (("bump34", 1), 11))
    elif mutation == "break_bump_reality":
        # THE EXACT STURM COUNT ALTERED: the t0 = 3 quartic asserted to have two
        # real roots.  It has NONE, which is why that core carries two conjugate
        # pairs and not one.
        claims["bump_quartic_real_roots"] = rewritten(
            BUMP_QUARTIC_REAL_ROOTS, (("bump34", 3), 2))
    elif mutation == "break_operator_census":
        # THE OPERATOR-LEVEL RESPONSE ALTERED: the {3,4} bump asserted to move W
        # at fewer entries than it does.
        claims["operator_census"] = rewritten(
            OPERATOR_CENSUS, (("bump34", 5), 0))
    elif mutation == "break_max_shifts":
        # THE HEADLINE DISPLACEMENT ALTERED at its last decimal place.
        claims["max_shift_decimals"] = rewritten(
            MAX_SHIFT_DECIMALS,
            (("bump34", 3), MAX_SHIFT_DECIMALS[("bump34", 3)] + 1))
    elif mutation == "break_complex_inventory":
        # THE COMPLETED INVENTORY ALTERED: one imaginary part changed at its
        # last decimal place.
        original = COMPLEX_INVENTORY[("bump34", 1)]
        claims["complex_inventory"] = rewritten(
            COMPLEX_INVENTORY,
            (("bump34", 1), ((original[0][0], original[0][1] + 1),)))
    elif mutation == "break_small_imaginary_only":
        # THE SOLVE'S INCOMPLETE DESCRIPTION REASSERTED, AND THIS IS THE
        # MUTATION THAT GUARDS THE CHECK'S C4 COMPLETION: |Im| ~ 0.002-0.003
        # asserted to describe ALL the nonreal pairs.  It describes TWO of the
        # six; the other four sit outside the band, two of them at four to five
        # times its width.
        claims["small_imaginary_description_complete"] = True
    elif mutation == "break_pencil_agreement":
        # THE ORDERING CROSS-CHECK DENIED: det(z K_c - L_2)/det(K_c) asserted to
        # differ from charpoly(K_c^-1 L_2).  If it did, every spectrum here
        # would depend on an inversion-order convention.
        claims["pencil_residual"] = 1
    elif mutation == "break_bumped_isometry":
        # THE GRADING OPERATOR DISQUALIFIED AT THE BUMPED CORE: U asserted not
        # to preserve the bumped Gram, which would make the sector statement --
        # and therefore the hybridization -- meaningless.
        claims["hybrid_isometry"] = (32, HYBRID_COMMUTATOR_RESIDUAL)
    elif mutation == "break_sector_hybridization":
        # THE HYBRIDIZATION DENIED: the bumped U = -1 sector asserted to keep
        # the baseline's two labelled rational factors instead of merging them
        # into one irreducible quartic.  The merge IS the refutation of
        # boundary-mode dominance.
        claims["bumped_sectors"] = dict(BASELINE_SECTORS)
    elif mutation == "break_comparable_shifts":
        # THE BULK-HEAVY DISPLACEMENT ALTERED at its last decimal place -- the
        # number that makes "comparable" a measurement rather than an adjective.
        claims["heavy_root_shift"] = HEAVY_ROOT_SHIFT + 1
    elif mutation == "break_baseline_separation":
        # THE PRECONDITION OF THE WHOLE ARGUMENT ALTERED: the two baseline large
        # roots were only 0.0126473949 apart BEFORE the bump, which is why
        # assigning one post-bump member as 'the boundary root' is not
        # invariant.
        claims["baseline_large_separation"] = BASELINE_LARGE_SEPARATION + 1
    elif mutation == "break_edge_antenna":
        # THE REFUTED CLAIM REASSERTED AS A MEASUREMENT, AND THIS IS THE
        # MUTATION THAT GUARDS THE CHECK'S P1: the two large displacements
        # asserted NOT comparable, i.e. the edge asserted to dominate.  They
        # differ by less than the baseline separation of the very roots they
        # move, which is as close to a tie as this construction can express.
        claims["shifts_comparable"] = False
    elif mutation == "break_position_dependence":
        # THE POSITION DEPENDENCE ERASED: the {2,3} bump asserted to give the
        # {3,4} bump's response.  Sign, magnitude and reach all differ, and that
        # is what keeps 'generic near-edge coupling' from becoming a law.
        claims["max_shift_decimals"] = rewritten(
            MAX_SHIFT_DECIMALS,
            (("bump23", 1), MAX_SHIFT_DECIMALS[("bump34", 1)]))
    elif mutation == "break_out_of_range_exactness":
        # THE EXACT ZERO DENIED: the {2,3} bump asserted to move W at t0 = 5.
        # It moves it at EXACTLY ZERO entries -- the operator itself, not merely
        # its spectrum -- which is the sharpest single statement of finite reach
        # in the block.
        claims["operator_census"] = rewritten(
            OPERATOR_CENSUS, (OUT_OF_RANGE_CORE, 64))
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim")
    elif mutation == "break_nsimplify_absence":
        # THE HAZARD DECLARED PRESENT: a nonzero count asserted, which the
        # source-token census forbids.
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
    hodge_display_residuals: dict
    imported_hodges: dict
    profile_covariance: dict
    core_table: dict
    light_multiplicities: dict
    heavy_multiplicities: dict
    boundary_asymmetry: dict
    boundary_discriminants: dict
    boundary_discriminant_factorizations: dict
    boundary_roots_positive: bool
    reversal_exact: bool
    touch_patterns: dict
    crossing_patterns: dict
    crossing_irreducible: dict
    quadratic_cross_patterns: dict
    # D
    dial_factors: tuple
    dial_palindromic: bool
    dial_discriminants: dict
    dial_discriminant_factorizations: dict
    dial_trace_bound: bool
    trace_motions: dict
    trace_motion_signs: dict
    theta_decimals: dict
    ratio_decimals: dict
    # E
    bump_covariance: int
    bump_factors: dict
    nonpalindromic_count: int
    palindromic_offenders: tuple
    bump_quartic_primes: dict
    bump_quadratic_discriminants: dict
    bump_quartic_real_roots: dict
    operator_census: dict
    max_shift_decimals: dict
    complex_inventory: dict
    small_imaginary_split: tuple
    pencil_residual: int
    hybrid_isometry: tuple
    baseline_sectors: dict
    bumped_sectors: dict
    boundary_root_shift: int
    heavy_root_shift: int
    baseline_large_separation: int
    light_root_shifts: tuple
    shifts_comparable: bool
    # F
    nsimplify_calls: int


def measure() -> Facts:
    text, at_final_path = note_text()
    main_head = resolve_ref("origin/main")

    # --- C: THE ONE IMPORT, AND THE LAW GATED AGAINST IT AT BOTH VOLUMES ----
    imported = {"v1": imported_shear_block(FIXTURE_SHEAR, UNIT_VOLUME),
                "v45": imported_shear_block(FIXTURE_SHEAR, BUMP_VOLUME)}
    hodge_display_residuals = {
        "v1": residual_count(imported["v1"] - DISPLAYED_HODGE_UNIT),
        "v45": residual_count(imported["v45"] - DISPLAYED_HODGE_BUMP)}

    # --- THE HEAVY PASS.  FIVE exact rational inverses -- one 80 x 80 and four
    # 64 x 64 -- are the expensive objects of this block, and each is built
    # EXACTLY ONCE here and shared by every family below.  No inverse is ever
    # recomputed and no core is built twice.
    profiles = {
        ("v1", 20): uniform_profile(20, UNIT_VOLUME),
        ("v1", 16): uniform_profile(16, UNIT_VOLUME),
        ("v45", 16): uniform_profile(16, BUMP_VOLUME),
        ("bump34", 16): bump_profile(16, BUMP_ANCHORS["bump34"], BUMP_VOLUME),
        ("bump23", 16): bump_profile(16, BUMP_ANCHORS["bump23"], BUMP_VOLUME),
    }
    actions: dict = {}
    inverses: dict = {}
    for key, profile in profiles.items():
        actions[key] = build_profile_action(key[1], profile)
        inverses[key] = exact_inverse(actions[key]["action"])

    profile_covariance = {}
    for name in PROFILE_NAMES:
        key = (name, 16)
        built = actions[key]
        profile_covariance[name] = (
            residual_count(built["reflection"] * built["hodge"]
                           * built["reflection"] - built["hodge"]),
            residual_count(built["reflection"] * built["action"]
                           * built["reflection"] - built["action"].T))

    # --- THE CORE TABLE, BUILT ONCE AND READ BY C, D AND E -----------------
    cores: dict = {}
    for width in WIDTHS:
        for core in range(1, width // 2 + 1):
            cores[("v1", width, core)] = core_operators(
                width, inverses[("v1", width)], core)
    for name in ("v45", "bump34", "bump23"):
        for core in BUMP_CORES:
            cores[(name, 16, core)] = core_operators(
                16, inverses[(name, 16)], core)
    if ("v45", 16, DIAL_CORE) not in cores:                # pragma: no cover
        cores[("v45", 16, DIAL_CORE)] = core_operators(
            16, inverses[("v45", 16)], DIAL_CORE)
    factors = {key: char_factors(value["W"]) for key, value in cores.items()}

    # --- C: THE FULL SCAN, THE LAYER AND THE VALIDITY RULE -----------------
    core_table = {key[1:]: factors[key] for key in factors
                  if key[0] == "v1" and key[1:] in CORE_TABLE}
    light_multiplicities = {}
    heavy_multiplicities = {}
    for key in sorted(CORE_TABLE):
        measured = dict(factors[("v1",) + key])
        light_multiplicities[key] = measured.get(LIGHT, 0)
        heavy_multiplicities[key] = measured.get(HEAVY, 0)
    boundary_asymmetry = {}
    boundary_discriminants = {}
    boundary_discriminant_factorizations = {}
    roots_positive = True
    for quadratic in NONRECIPROCAL:
        boundary_asymmetry[quadratic] = int(quadratic[0] - quadratic[2])
        value = discriminant(quadratic)
        boundary_discriminants[quadratic] = value
        if quadratic in BOUNDARY_DISCRIMINANT_FACTORIZATIONS:
            boundary_discriminant_factorizations[quadratic] = {
                int(prime): int(power)
                for prime, power in sp.factorint(value).items()}
        roots_positive = roots_positive and bool(
            value > 0 and quadratic[0] > 0 and -quadratic[1] > 0
            and quadratic[2] > 0)
    reversal_exact = all(
        tuple(reversed(first)) == second for first, second in REVERSAL_PAIRS)
    touch_patterns = {key: degree_pattern(factors[("v1",) + key])
                      for key in TOUCH_CORES}
    crossing_patterns = {key: degree_pattern(factors[("v1",) + key])
                         for key in CROSS_CORES}
    crossing_irreducible = {}
    for key, prime in CROSSING_CERTIFICATE_PRIMES.items():
        quartics = [c for c, _ in factors[("v1",) + key] if len(c) == 5]
        crossing_irreducible[key] = (
            prime if len(quartics) == 1 and irreducible_modulo(quartics[0],
                                                               prime) else 0)
    quadratic_cross_patterns = {key: degree_pattern(factors[("v1",) + key])
                                for key in QUADRATIC_CROSS_CORES}

    # --- D: THE UNIFORM VOLUME DIAL ----------------------------------------
    dial_factors = factors[("v45", 16, DIAL_CORE)]
    dial_quadratics = tuple(sorted(
        {c for c, _ in dial_factors if len(c) == 3}))
    dial_palindromic = all(c[0] == c[2] for c in dial_quadratics)
    dial_trace_bound = all(-c[1] > 2 * c[0] for c in dial_quadratics)
    dial_discriminants = {c: discriminant(c) for c in dial_quadratics}
    dial_discriminant_factorizations = {
        c: {int(prime): int(power)
            for prime, power in sp.factorint(value).items()}
        for c, value in dial_discriminants.items()}
    baseline_quadratics = {"heavy": HEAVY, "light": LIGHT}
    dial_named = {"heavy": DIAL_HEAVY, "light": DIAL_LIGHT}
    trace_motions = {}
    trace_motion_signs = {}
    theta_decimals = {}
    for label in ("heavy", "light"):
        base, moved = baseline_quadratics[label], dial_named[label]
        base_trace = sp.Rational(-base[1], base[0])
        moved_trace = sp.Rational(-moved[1], moved[0])
        motion = sp.together(moved_trace - base_trace)
        trace_motions[label] = motion
        trace_motion_signs[label] = int(sp.sign(motion))
        theta_decimals[("v1", label)] = decimal10(sp.acosh(base_trace / 2))
        theta_decimals[("v45", label)] = decimal10(sp.acosh(moved_trace / 2))
    ratio_decimals = {
        "v1": decimal10(sp.acosh(sp.Rational(-HEAVY[1], HEAVY[0]) / 2)
                        / sp.acosh(sp.Rational(-LIGHT[1], LIGHT[0]) / 2)),
        "v45": decimal10(
            sp.acosh(sp.Rational(-DIAL_HEAVY[1], DIAL_HEAVY[0]) / 2)
            / sp.acosh(sp.Rational(-DIAL_LIGHT[1], DIAL_LIGHT[0]) / 2)),
    }

    # --- E: THE BUMP PACKAGE ------------------------------------------------
    bump_covariance = max(
        max(profile_covariance[name]) for name in ("bump34", "bump23"))
    bump_factors = {(name, core): factors[(name, 16, core)]
                    for name in ("bump34", "bump23") for core in BUMP_CORES}
    palindromic_offenders = []
    nonpalindromic_count = 0
    for key in NONPALINDROMIC_CORES:
        for coefficients, _ in bump_factors[key]:
            if coefficients[0] != coefficients[-1]:
                nonpalindromic_count += 1
            else:
                palindromic_offenders.append((key, coefficients))
    bump_quartic_primes = {}
    bump_quadratic_discriminants = {}
    bump_quartic_real_roots = {}
    for key in NONPALINDROMIC_CORES:
        quartics = [c for c, _ in bump_factors[key] if len(c) == 5]
        bump_quadratic_discriminants[key] = tuple(sorted(
            discriminant(c) for c, _ in bump_factors[key] if len(c) == 3))
        prime = BUMP_QUARTIC_PRIMES[key]
        bump_quartic_primes[key] = (
            prime if len(quartics) == 1 and irreducible_modulo(quartics[0],
                                                               prime) else 0)
        bump_quartic_real_roots[key] = (
            real_root_count(quartics[0]) if quartics else -1)
    operator_census = {}
    max_shift_decimals = {}
    complex_inventory = {}
    below_band = 0
    inside_band = 0
    above_band = 0
    for name in ("bump34", "bump23"):
        for core in BUMP_CORES:
            baseline = cores[("v1", 16, core)]["W"]
            moved = cores[(name, 16, core)]["W"]
            operator_census[(name, core)] = residual_count(moved - baseline)
            base_roots = exact_root_list(factors[("v1", 16, core)])
            moved_roots = exact_root_list(factors[(name, 16, core)])
            displacements = matched_displacements(base_roots, moved_roots)
            max_shift_decimals[(name, core)] = displacements[-1][0]
            inventory = conjugate_inventory(moved_roots)
            complex_inventory[(name, core)] = inventory
            for _, imaginary in inventory:
                if imaginary < SMALL_IMAGINARY_BAND[0]:
                    below_band += 1
                elif imaginary > SMALL_IMAGINARY_BAND[1]:
                    above_band += 1
                else:
                    inside_band += 1
    pencil_residual = 0
    for key in (("v1", 16, 1), ("v1", 16, 3), ("v45", 16, 3),
                ("bump34", 16, 1), ("bump34", 16, 3), ("bump34", 16, 5),
                ("bump23", 16, 1)):
        built = cores[key]
        pencil = sp.expand(
            sp.Matrix(VARIABLE * built["K"] - built["L2"]).det()
            / exact_determinant(built["K"]))
        pencil_residual += int(sp.expand(
            pencil - built["W"].charpoly(VARIABLE).as_expr()) != 0)

    # --- E: THE HYBRIDIZATION ----------------------------------------------
    two_site = spatial_shift(HYBRID_CORE, 2)
    identity = sp.eye(8)
    bumped = cores[("bump34", 16, HYBRID_CORE)]
    hybrid_isometry = (
        residual_count(two_site.T * bumped["K"] * two_site - bumped["K"]),
        residual_count(bumped["W"] * two_site - two_site * bumped["W"]))
    baseline_sectors = {}
    bumped_sectors = {}
    for sign in (1, -1):
        projector = sp.expand((identity + sign * two_site) / 2)
        baseline_sectors[sign] = char_factors(sector_block(
            projector, cores[("v1", 16, HYBRID_CORE)]["W"]))
        bumped_sectors[sign] = char_factors(sector_block(
            projector, bumped["W"]))
    heavy_large = max(sp.Poly(list(HEAVY), VARIABLE).all_roots(),
                      key=lambda root: sp.N(root, 30))
    near_large = max(sp.Poly(list(NEAR), VARIABLE).all_roots(),
                     key=lambda root: sp.N(root, 30))
    baseline_large_separation = decimal10(heavy_large - near_large)
    bumped_roots = exact_root_list(factors[("bump34", 16, HYBRID_CORE)])
    nonreal = [root for root in bumped_roots if not root.is_real]
    boundary_root_shift = min(
        decimal10(high_modulus(near_large, root)) for root in nonreal)
    heavy_root_shift = min(
        decimal10(high_modulus(heavy_large, root)) for root in nonreal)
    light_large = max(sp.Poly(list(LIGHT), VARIABLE).all_roots(),
                      key=lambda root: sp.N(root, 30))
    light_root_shifts = tuple(sorted(
        decimal10(high_modulus(light_large, root))
        for root in bumped_roots
        if decimal10(high_modulus(light_large, root)) > 0)[:2])
    shifts_comparable = bool(
        abs(boundary_root_shift - heavy_root_shift)
        <= baseline_large_separation)

    banners = {
        "imposed": len(IMPOSED_OBJECTS),
        "registered": len(REGISTERED_OBJECTS),
        "adopted": len(ADOPTED_OBJECTS),
        "lapse_physicality_claimed": LAPSE_PHYSICALITY_CLAIMED,
        "volume_dial_physical_claimed": VOLUME_DIAL_PHYSICAL_CLAIMED,
        "boundary_mode_physical_claimed": BOUNDARY_MODE_PHYSICAL_CLAIMED,
        "profiles_inequivalent_claimed": PROFILES_INEQUIVALENT_CLAIMED,
        "transfer_operator_claimed": TRANSFER_OPERATOR_CLAIMED,
        "edge_dominance_claimed": EDGE_DOMINANCE_CLAIMED,
        "generality_claimed": GENERALITY_CLAIMED,
        "factoring_is_a_validity_signature": FACTORING_IS_A_VALIDITY_SIGNATURE,
        "small_imaginary_description_complete":
            SMALL_IMAGINARY_DESCRIPTION_COMPLETE,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
    }
    b190 = landed_text(BLOCK190_NOTE)
    b105 = landed_text(BLOCK105_NOTE)
    campaign = landed_text(CAMPAIGN_NOTE)
    citation_pins = {
        "b190_note_readable": len(b190) > 0,
        "b190_deep_spectrum_pinned": "233631106" in b190,
        "b105_note_readable": len(b105) > 0,
        "campaign_readable": len(campaign) > 0,
        "campaign_anchor": "B191 CHECK VERDICT" in campaign,
    }

    return Facts(
        main_head=main_head,
        authority=authority_certificate(main_head),
        note_at_final_path=at_final_path,
        scope=scope_certificate(text),
        banners=banners,
        citation_pins=citation_pins,
        hodge_display_residuals=hodge_display_residuals,
        imported_hodges=imported,
        profile_covariance=profile_covariance,
        core_table=core_table,
        light_multiplicities=light_multiplicities,
        heavy_multiplicities=heavy_multiplicities,
        boundary_asymmetry=boundary_asymmetry,
        boundary_discriminants=boundary_discriminants,
        boundary_discriminant_factorizations=(
            boundary_discriminant_factorizations),
        boundary_roots_positive=roots_positive,
        reversal_exact=reversal_exact,
        touch_patterns=touch_patterns,
        crossing_patterns=crossing_patterns,
        crossing_irreducible=crossing_irreducible,
        quadratic_cross_patterns=quadratic_cross_patterns,
        dial_factors=dial_factors,
        dial_palindromic=dial_palindromic,
        dial_discriminants=dial_discriminants,
        dial_discriminant_factorizations=dial_discriminant_factorizations,
        dial_trace_bound=dial_trace_bound,
        trace_motions=trace_motions,
        trace_motion_signs=trace_motion_signs,
        theta_decimals=theta_decimals,
        ratio_decimals=ratio_decimals,
        bump_covariance=bump_covariance,
        bump_factors=bump_factors,
        nonpalindromic_count=nonpalindromic_count,
        palindromic_offenders=tuple(palindromic_offenders),
        bump_quartic_primes=bump_quartic_primes,
        bump_quadratic_discriminants=bump_quadratic_discriminants,
        bump_quartic_real_roots=bump_quartic_real_roots,
        operator_census=operator_census,
        max_shift_decimals=max_shift_decimals,
        complex_inventory=complex_inventory,
        small_imaginary_split=(below_band, inside_band, above_band),
        pencil_residual=pencil_residual,
        hybrid_isometry=hybrid_isometry,
        baseline_sectors=baseline_sectors,
        bumped_sectors=bumped_sectors,
        boundary_root_shift=boundary_root_shift,
        heavy_root_shift=heavy_root_shift,
        baseline_large_separation=baseline_large_separation,
        light_root_shifts=light_root_shifts,
        shifts_comparable=shifts_comparable,
        nsimplify_calls=nsimplify_occurrences(),
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
        "A-4", "BOTH Block 190 artifacts are content-bound at the pinned "
        "commit, in the worktree and against their recorded blobs",
        authority.parent_artifact_blobs if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs)
    checks.check(
        "A-5", "the stale pin is a REAL ancestor of HEAD that carries NEITHER "
        "Block 190 artifact",
        authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact)
    checks.check(
        "A-6", f"the ONE landed import is available and "
        f"{len(AUDIT_INPUT_PATHS) - 1} audit inputs are readable",
        authority.machinery_import_landed
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
        and not authority.inputs_missing)

    # --- B: THE BANNER AND THE FENCE ----------------------------------------
    checks.check(
        "B-1", f"{facts.banners['imposed']} imposed objects, "
        f"{facts.banners['registered']} registered, "
        f"{facts.banners['adopted']} adopted",
        (facts.banners["registered"] == 0
         and facts.banners["adopted"] == 0
         and facts.banners["imposed"] == len(IMPOSED_OBJECTS))
        == (not claims["objects_registered"]))
    checks.check(
        "B-2", "LAPSE PHYSICALITY is declared NOT CLAIMED: v is the IMPOSED "
        "Block 105 Hodge-volume parameter and no ADM lapse, constraint, gauge "
        "orbit, quotient, Dirac observable or OS reconstruction is supplied",
        facts.banners["lapse_physicality_claimed"]
        == claims["lapse_physicality_claimed"])
    checks.check(
        "B-3", "A PHYSICAL VOLUME DIAL is declared NOT CLAIMED: what is "
        "measured is two exact rational traces moving oppositely under an "
        "imposed change of an imposed parameter",
        facts.banners["volume_dial_physical_claimed"]
        == claims["volume_dial_physical_claimed"])
    checks.check(
        "B-4", "A PHYSICAL BOUNDARY MODE is declared NOT CLAIMED: "
        "'boundary mode' names an exact rational FACTOR at a seam-adjacent core",
        facts.banners["boundary_mode_physical_claimed"]
        == claims["boundary_mode_physical_claimed"])
    checks.check(
        "B-5", "PROFILE INEQUIVALENCE is declared NOT CLAIMED: exact "
        "Ps-covariance proves compatibility with ONE reflection and does NOT "
        "prove two v(t) profiles are physically inequivalent",
        facts.banners["profiles_inequivalent_claimed"]
        == claims["profiles_inequivalent_claimed"])
    checks.check(
        "B-6", "W AS A TRANSFER OPERATOR is declared NOT CLAIMED: Block 190's "
        "refutation of the naive OS transfer pairing is not repaired here",
        facts.banners["transfer_operator_claimed"]
        == claims["transfer_operator_claimed"])
    checks.check(
        "B-7", "BOUNDARY-MODE DOMINANCE is declared NOT CLAIMED: 'the edge "
        "mode is the bump's antenna' is WITHDRAWN and replaced by the "
        "hybridization measured in family E",
        facts.banners["edge_dominance_claimed"]
        == claims["edge_dominance_claimed"])
    checks.check(
        "B-8", "NO GENERALITY is claimed: one fixture, two widths, four "
        "profiles, one bump amplitude",
        facts.banners["generality_claimed"] == claims["generality_claimed"])
    checks.check(
        "B-9", f"{facts.banners['unsupplied']} gravity structures are "
        "enumerated as NOT SUPPLIED, so the absence is a count",
        facts.banners["unsupplied"] == len(UNSUPPLIED_GRAVITY_STRUCTURES))
    checks.check(
        "B-10", "every imposed object is a nonempty declared string",
        all(isinstance(item, str) and item for item in IMPOSED_OBJECTS))

    # --- C: THE BOUNDARY MONODROMY AND THE VALIDITY RULE --------------------
    checks.check(
        "C-1", "the landed primary bodies and the campaign anchor are readable "
        "and Block 190's deep spectrum is pinned in their own note",
        all(facts.citation_pins.values()) == claims["citation_pins"])
    checks.check(
        "C-2", "THE DISPLAYED VOLUME LAW EQUALS THE IMPORT ENTRYWISE AT BOTH "
        "PROBED VOLUMES: diag(v, v g(c)^-1, 1/v) against "
        "b128.block105.shear_hodge(5/13, v) at v = 1 and v = 4/5",
        facts.hodge_display_residuals == claims["hodge_display_residuals"])
    checks.check(
        "C-3", "EVERY PROFILE IS Ps-COVARIANT AT ZERO -- uniform v = 1, "
        "uniform v = 4/5, the {3,4} bump and the {2,3} bump",
        facts.profile_covariance == claims["profile_covariance"])
    checks.check(
        "C-4", "every entry of both imported Hodge blocks is an EXACT rational",
        all(is_exact_rational(matrix[i, j])
            for matrix in facts.imported_hodges.values()
            for i in range(4) for j in range(4)))
    checks.check(
        "C-5", f"THE LIGHT PAIR IS BOUNDARY-RIGID: light^2 divides charpoly(W) "
        f"with multiplicity EXACTLY {claims['light_multiplicity']} at all "
        f"{len(facts.light_multiplicities)} tabulated cores at both widths",
        all(value == claims["light_multiplicity"]
            for value in facts.light_multiplicities.values()))
    checks.check(
        "C-6", "AND THE HEAVY SECTOR LOSES EXACTLY ONE COPY AT EVERY LAYER "
        "CORE, so the boundary layer is MODE-SELECTIVE",
        all(facts.heavy_multiplicities[key]
            == claims["heavy_layer_multiplicity"] for key in LAYER_CORES))
    checks.check(
        "C-7", "THE FULL SCAN MATCHES THE DECLARED TABLE AT EVERY TABULATED "
        "CORE OF BOTH WIDTHS -- the layer is POSITIONALLY WIDTH-LOCKED",
        facts.core_table == claims["core_table"])
    checks.check(
        "C-8", f"THE BOUNDARY FACTORS ARE EXACTLY NON-RECIPROCAL: a - c = "
        f"{tuple(facts.boundary_asymmetry[q] for q in NONRECIPROCAL)}, all "
        "NONZERO, so the seam breaks lambda -> 1/lambda",
        facts.boundary_asymmetry == claims["boundary_asymmetry"]
        and all(value != 0 for value in facts.boundary_asymmetry.values()))
    checks.check(
        "C-9", "AND THEY ARE POSITIVE: exact positive discriminants with their "
        "factorizations gated, and a, -b, c all positive, so both roots are "
        "real and positive -- positivity SURVIVES the seam, reciprocity does not",
        facts.boundary_discriminants == claims["boundary_discriminants"]
        and facts.boundary_discriminant_factorizations
        == claims["boundary_discriminant_factorizations"]
        and facts.boundary_roots_positive
        == claims["boundary_roots_positive"])
    checks.check(
        "C-10", "THE NEAR/FAR REVERSAL IS EXACT COEFFICIENT FOR COEFFICIENT: "
        "mirror = rev(near) and rev(second) = rev of second, at both widths",
        facts.reversal_exact == claims["reversal_exact"])
    checks.check(
        "C-11", f"TOUCHING IS ADMISSIBLE: cores whose L_2 reaches exactly T/2 "
        f"factor as the bulk table says at both widths, degree patterns "
        f"{tuple(facts.touch_patterns.values())}",
        (all(pattern == (2, 2, 2, 2)
             for pattern in facts.touch_patterns.values())
         and all(facts.core_table[key] == claims["core_table"][key]
                 for key in TOUCH_CORES)) == claims["touch_admissible"])
    checks.check(
        "C-12", f"AND CROSSING GIVES {claims['crossing_pattern']} AT THE FOUR "
        "CROSSING CORES OF T/2-2 AND T/2-1: two rational quadratics and one "
        "rational quartic, NOT an irreducible degree eight",
        all(pattern == claims["crossing_pattern"]
            for pattern in facts.crossing_patterns.values()))
    checks.check(
        "C-13", "the crossing quartics are CERTIFIED irreducible over Q by "
        "Gauss's lemma -- modulo 11 at T = 16 and modulo 67 at T = 20",
        facts.crossing_irreducible == claims["crossing_irreducible"])
    checks.check(
        "C-14", "AND THE FACTORING SIGNATURE DIES FROM THE OTHER SIDE TOO: the "
        "CROSSING core at t0 = T/2 factors COMPLETELY into rational quadratics "
        "at both widths, so a crossing core can look exactly like a bulk one",
        all(pattern == claims["quadratic_cross_pattern"]
            for pattern in facts.quadratic_cross_patterns.values()))
    checks.check(
        "C-15", "THE SOLVE'S NON-FACTORING SIGNATURE IS DECLARED WITHDRAWN: "
        "factoring behaviour is NOT the validity criterion in either "
        "direction, and the rule rests on the pairing's definition",
        facts.banners["factoring_is_a_validity_signature"]
        == claims["factoring_is_a_validity_signature"])

    # --- D: THE UNIFORM VOLUME DIAL -----------------------------------------
    checks.check(
        "D-1", f"THE EXACT v = 4/5 DEEP SPECTRUM at T = {DIAL_WIDTH}, "
        f"t0 = {DIAL_CORE}: (31260675 z^2 - 302948719 z + 31260675)^2 "
        "(50327125 z^2 - 139773119 z + 50327125)^2",
        facts.dial_factors == claims["dial_factors"])
    checks.check(
        "D-2", "THE FORM SURVIVES THE UNIFORM DIAL: both factors palindromic "
        "and squared, so reciprocity is NOT broken by a uniform volume",
        facts.dial_palindromic == claims["dial_palindromic"])
    checks.check(
        "D-3", f"and both discriminants are exact POSITIVE integers with their "
        f"prime factorizations gated: "
        f"{tuple(facts.dial_discriminants.values())}",
        facts.dial_discriminants == claims["dial_discriminants"]
        and facts.dial_discriminant_factorizations
        == claims["dial_discriminant_factorizations"]
        and all(value > 0 for value in facts.dial_discriminants.values()))
    checks.check(
        "D-4", "and both traces exceed twice the leading coefficient, so both "
        "roots are POSITIVE and not merely real",
        facts.dial_trace_bound == claims["dial_trace_bound"])
    checks.check(
        "D-5", f"THE TWO EXACT RATIONAL TRACE MOTIONS: heavy "
        f"{facts.trace_motions['heavy']}, light {facts.trace_motions['light']}",
        facts.trace_motions == claims["trace_motions"])
    checks.check(
        "D-6", "AND THEIR SIGNS ARE OPPOSITE, which is what a conformal "
        "rescaling could not do: theta_heavy strictly DECREASES and "
        "theta_light strictly INCREASES",
        facts.trace_motion_signs == claims["trace_motion_signs"]
        and facts.trace_motion_signs["heavy"]
        * facts.trace_motion_signs["light"] < 0)
    checks.check(
        "D-7", "THE ONE NUMERIC LAYER, gated to ten decimals: theta_heavy "
        "2.3276840296 -> 2.2603806617 and theta_light 0.8506775060 -> "
        "0.8553292810, each an evalf of an EXACT acosh at 40 digits",
        facts.theta_decimals == claims["theta_decimals"])
    checks.check(
        "D-8", f"AND THE CORRECTED RATIO PAIR: "
        f"{facts.ratio_decimals['v1']}/10^10 -> "
        f"{facts.ratio_decimals['v45']}/10^10, i.e. 2.7362708113 -> "
        "2.6427023041 and NOT the withdrawn 2.7361 -> 2.6449",
        facts.ratio_decimals == claims["ratio_decimals"])

    # --- E: THE BUMP PACKAGE ------------------------------------------------
    checks.check(
        "E-1", "BOTH LOCALIZED PROFILES ARE Ps-COVARIANT AT EXACTLY ZERO -- "
        "which is compatibility with the reflection and NOT an equivalence "
        "statement about v(t) profiles",
        facts.bump_covariance == claims["bump_covariance"])
    checks.check(
        "E-2", f"THE EXACT IRREDUCIBLE FACTORIZATIONS at t0 = {BUMP_CORES} for "
        "both bump positions, including the UNCHANGED core beyond the {2,3} "
        "bump's reach",
        facts.bump_factors == claims["bump_factors"])
    checks.check(
        "E-3", f"PALINDROMICITY DIES IN EVERY IRREDUCIBLE FACTOR IT REACHES: "
        f"{facts.nonpalindromic_count} of "
        f"{claims['nonpalindromic_count']} moved factors have leading != "
        "constant as an exact integer inequality, with ZERO exceptions",
        facts.nonpalindromic_count == claims["nonpalindromic_count"]
        and not facts.palindromic_offenders)
    checks.check(
        "E-4", "every bumped quartic is CERTIFIED irreducible over Q by "
        "Gauss's lemma at its declared prime",
        facts.bump_quartic_primes == claims["bump_quartic_primes"]
        and all(value > 0 for value in facts.bump_quartic_primes.values()))
    checks.check(
        "E-5", "ROOT REALITY IS EXACT, NEVER ESTIMATED: exact quadratic "
        "discriminants and exact Sturm counts for every quartic",
        facts.bump_quadratic_discriminants
        == claims["bump_quadratic_discriminants"]
        and facts.bump_quartic_real_roots
        == claims["bump_quartic_real_roots"])
    checks.check(
        "E-6", f"THE OPERATOR-LEVEL RESPONSE: nnz(W_bump - W_v1) = "
        f"{tuple(facts.operator_census[k] for k in sorted(facts.operator_census))}"
        " over the six probed (profile, core) pairs",
        facts.operator_census == claims["operator_census"])
    checks.check(
        "E-7", "THE MAX MATCHED ROOT DISPLACEMENTS, ten decimals: 0.9570159788, "
        "1.3978902241, 0.0144654296 for {3,4} and 0.6880075885, 0.0737486236, "
        "0 for {2,3}",
        facts.max_shift_decimals == claims["max_shift_decimals"])
    checks.check(
        "E-8", "THE COMPLETE COMPLEX-PAIR INVENTORY, by exact algebraic "
        "nonreality and not by a threshold",
        facts.complex_inventory == claims["complex_inventory"])
    checks.check(
        "E-9", f"AND THE SOLVE'S BAND IS COMPLETED RATHER THAN REPEATED: of "
        f"the {sum(facts.small_imaginary_split)} measured pairs, "
        f"{facts.small_imaginary_split[0]} lie BELOW |Im| = 0.002, "
        f"{facts.small_imaginary_split[1]} lies INSIDE [0.002, 0.003] and "
        f"{facts.small_imaginary_split[2]} lie ABOVE 0.003, two of those at "
        "four to five times the band width",
        facts.small_imaginary_split == claims["small_imaginary_split"]
        and sum(facts.small_imaginary_split) == SMALL_IMAGINARY_TOTAL
        and facts.banners["small_imaginary_description_complete"]
        == claims["small_imaginary_description_complete"])
    checks.check(
        "E-10", "THE ORDERING CROSS-CHECK: det(z K_c - L_2)/det(K_c) agrees "
        "COEFFICIENTWISE with charpoly(K_c^-1 L_2) at every probed core, so no "
        "spectrum depends on an inversion-order convention",
        facts.pencil_residual == claims["pencil_residual"])
    checks.check(
        "E-11", "U REMAINS AN EXACT GRAM ISOMETRY AND AN EXACT COMMUTANT AT "
        "THE BUMPED CORE, so the sector statement below is well posed",
        facts.hybrid_isometry == claims["hybrid_isometry"])
    checks.check(
        "E-12", "THE HYBRIDIZATION: the baseline U = -1 sector is heavy TIMES "
        "near -- two labelled rational factors -- and the bumped one is ONE "
        "IRREDUCIBLE NONPALINDROMIC QUARTIC",
        facts.baseline_sectors == claims["baseline_sectors"]
        and facts.bumped_sectors == claims["bumped_sectors"])
    checks.check(
        "E-13", f"THE TWO LARGE-ROOT DISPLACEMENTS ARE COMPARABLE: "
        f"{facts.boundary_root_shift}/10^10 for the boundary root and "
        f"{facts.heavy_root_shift}/10^10 for the bulk-heavy root",
        facts.boundary_root_shift == claims["boundary_root_shift"]
        and facts.heavy_root_shift == claims["heavy_root_shift"])
    checks.check(
        "E-14", f"and they were already separated by only "
        f"{facts.baseline_large_separation}/10^10 BEFORE the bump, which is "
        "why naming either post-bump member 'the boundary root' is NOT "
        "invariant; the light-sector large roots move by "
        f"{facts.light_root_shifts}",
        facts.baseline_large_separation
        == claims["baseline_large_separation"]
        and facts.light_root_shifts == claims["light_root_shifts"])
    checks.check(
        "E-15", "BOUNDARY-MODE DOMINANCE IS REFUTED AS A MEASUREMENT: the two "
        "displacements differ by LESS than the baseline separation of the very "
        "roots they move, so the response is HYBRIDIZED and not dominated",
        facts.shifts_comparable == claims["shifts_comparable"])
    checks.check(
        "E-16", "THE POSITION DEPENDENCE IS A MEASUREMENT, NOT AN IMPRESSION: "
        "the {2,3} bump's t0 = 1 response is a DIFFERENT number from the "
        "{3,4} bump's",
        facts.max_shift_decimals[("bump23", 1)]
        == claims["max_shift_decimals"][("bump23", 1)]
        and claims["max_shift_decimals"][("bump23", 1)]
        != claims["max_shift_decimals"][("bump34", 1)])
    checks.check(
        "E-17", "AND THE REACH IS FINITE AT THE OPERATOR LEVEL: beyond the "
        "{2,3} bump's reach nnz(W_bump - W_v1) = 0 EXACTLY at t0 = 5 -- the "
        "operator itself, not merely its spectrum",
        facts.operator_census[OUT_OF_RANGE_CORE]
        == claims["operator_census"][OUT_OF_RANGE_CORE]
        and claims["operator_census"][OUT_OF_RANGE_CORE] == 0)

    # --- F: THE NOTE, THE FENCE AND THE nsimplify ABSENCE -------------------
    checks.check(
        "F-1", f"the note is at its final path docs/{FINAL_NOTE_NAME}",
        facts.note_at_final_path)
    checks.check(
        "F-2", "the N5 fence appears BYTE-IDENTICALLY in the note, AND the "
        "fence is REQUIRED rather than optional -- the declared key set must "
        "still be the full one, so the requirement cannot be dropped",
        tuple(claims["required_scope_keys"]) == SCOPE_KEYS
        and all(facts.scope.get(key) for key in claims["required_scope_keys"]))
    checks.check(
        "F-3", f"sp.nsimplify occurs {facts.nsimplify_calls} times in this "
        "runner's own source",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    return checks


# ---------------------------------------------------------------------------
# the measured report
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED -- BLOCK 191, THE BOUNDARY MODE AND THE VOLUME SENSITIVITY")
    print(f"  measurement pass: {elapsed_ns / 1e9:.1f} s")
    print(f"  THE ONE IMPORT, DISPLAYED AS A LAW AND GATED AT BOTH VOLUMES: "
          f"shear_hodge(5/13, 1) = {facts.imported_hodges['v1'].tolist()}")
    print(f"    shear_hodge(5/13, 4/5) = "
          f"{facts.imported_hodges['v45'].tolist()}")
    print(f"    displayed-vs-imported residuals: "
          f"{facts.hodge_display_residuals}")
    print(f"  PROFILE COVARIANCE (PsHPs-H, PsQPs-Q^T): "
          f"{facts.profile_covariance}")
    print("  THE FULL SCAN:")
    for key in sorted(facts.core_table):
        print(f"    charpoly(W) at T = {key[0]}, t0 = {key[1]}: "
              f"{facts.core_table[key]}")
    print(f"  light multiplicities: {facts.light_multiplicities}")
    print(f"  heavy multiplicities: {facts.heavy_multiplicities}")
    print(f"  BOUNDARY NON-RECIPROCITY a - c: {facts.boundary_asymmetry}")
    print(f"    discriminants {facts.boundary_discriminants}")
    print(f"    factorizations {facts.boundary_discriminant_factorizations}")
    print(f"    roots positive: {facts.boundary_roots_positive}; exact "
          f"reversal: {facts.reversal_exact}")
    print(f"  VALIDITY: touch patterns {facts.touch_patterns}; crossing "
          f"patterns {facts.crossing_patterns}")
    print(f"    crossing quartic certificates {facts.crossing_irreducible}; "
          f"t0 = T/2 patterns {facts.quadratic_cross_patterns}")
    print(f"  THE DIAL at T = {DIAL_WIDTH}, t0 = {DIAL_CORE}, v = 4/5: "
          f"{facts.dial_factors}")
    print(f"    palindromic {facts.dial_palindromic}; trace bound "
          f"{facts.dial_trace_bound}; discriminants "
          f"{facts.dial_discriminants}")
    print(f"    exact trace motions {facts.trace_motions} with signs "
          f"{facts.trace_motion_signs}")
    print(f"    theta decimals (x 10^10) {facts.theta_decimals}")
    print(f"    RATIO (x 10^10) {facts.ratio_decimals}  -- CORRECTED from the "
          f"solve's {WITHDRAWN_SOLVE_RATIO}")
    print(f"  THE BUMP: covariance {facts.bump_covariance}; operator census "
          f"{facts.operator_census}")
    for key in sorted(facts.bump_factors):
        print(f"    charpoly(W) {key}: {facts.bump_factors[key]}")
    print(f"    nonpalindromic factors: {facts.nonpalindromic_count}, "
          f"offenders {facts.palindromic_offenders}")
    print(f"    quartic certificates {facts.bump_quartic_primes}; Sturm counts "
          f"{facts.bump_quartic_real_roots}")
    print(f"    quadratic discriminants {facts.bump_quadratic_discriminants}")
    print(f"    max shifts (x 10^10) {facts.max_shift_decimals}")
    print(f"    COMPLETE complex inventory (Re, |Im|) x 10^10: "
          f"{facts.complex_inventory}")
    print(f"    solve band [0.002, 0.003]: (below, inside, above) = "
          f"{facts.small_imaginary_split} of "
          f"{sum(facts.small_imaginary_split)} pairs")
    print(f"    pencil residual {facts.pencil_residual}")
    print(f"  HYBRIDIZATION at t0 = {HYBRID_CORE}: U isometry/commutator "
          f"{facts.hybrid_isometry}")
    print(f"    baseline sectors {facts.baseline_sectors}")
    print(f"    bumped sectors {facts.bumped_sectors}")
    print(f"    boundary shift {facts.boundary_root_shift}, heavy shift "
          f"{facts.heavy_root_shift}, baseline separation "
          f"{facts.baseline_large_separation}, light shifts "
          f"{facts.light_root_shifts}, comparable {facts.shifts_comparable}")
    print(f"  nsimplify occurrences: {facts.nsimplify_calls}")
    print("  SCOPE: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. LAPSE "
          "PHYSICALITY IS A READING AND IS NOT ESTABLISHED HERE: v is the "
          "IMPOSED Block 105 Hodge-volume parameter, and no lapse variable, "
          "constraint, gauge orbit, quotient, Dirac observable or OS "
          "reconstruction is supplied. WHAT IS ESTABLISHED IS HODGE-VOLUME "
          "SPECTRAL SENSITIVITY WITHIN AN IMPOSED FINITE CONSTRUCTION. "
          "Ps-COVARIANCE PROVES COMPATIBILITY WITH ONE REFLECTION AND NOT "
          "PROFILE INEQUIVALENCE. ONE FIXTURE, TWO WIDTHS AND ONE BUMP "
          "AMPLITUDE IS NOT A WINDOW, AND NOTHING IS PROVEN ABOUT THE "
          "INFINITE-WIDTH LIMIT.")
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
