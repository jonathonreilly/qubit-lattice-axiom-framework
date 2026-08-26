#!/usr/bin/env python3
"""BLOCK 194 -- THE SPLIT GENERALITY THEOREM OF THE TRANSFER PACKAGE: THE
STRUCTURAL LEGS ARE (m, c)-UNIVERSAL ON THE SEARCHED SET AND POSITIVITY IS NOT.

THE RESULT, AND ITS EXACT SCOPE.  Block 190's wrap-edge width family is carried
at T = 16 and its mass/shear pair (m, c) -- FIXED at (9/20, 5/13) through Blocks
190 to 193 -- is turned into a VARIABLE.  The transfer package that those blocks
established at the one fixture SPLITS IN TWO under that variation, and the split
is the block's whole content:

  (i) THE STRUCTURAL LEGS ARE UNIVERSAL ON THE SEARCHED SET.  Ps-covariance,
      palindromicity of the deep monodromy characteristic polynomial, its being
      a PERFECT SQUARE of a degree-four palindromic polynomial, the commutation
      [W, U] = 0 with the momentum shift, the parity independence
      charpoly(W, t0=2) = charpoly(W, t0=3), and the bump-{2,3} window-cell
      invariance at t0 = 5 hold at EVERY admissible point of the searched
      rational set -- 192 of 192, with ZERO exceptions.

 (ii) POSITIVITY IS WINDOWED, NOT GENERIC.  The positive two-scale reading --
      that the four reciprocal root pairs are e^{+/-theta} with theta real --
      FAILS at 98 of those same 192 points.  The exact witness (m, c) =
      (1/100, 3/4) carries a NEGATIVE real reciprocal pair, and this block
      exhibits a SECOND failure mode the check did not separate: at
      (5, 101/100) and (1/10, 3/2) the failing pairs are COMPLEX and
      UNIMODULAR, carrying no negative pair at all.

THAT SPLIT IS THE THEOREM.  ALL OF IT IS FINITE EXACT LINEAR ALGEBRA OVER QQ ON
ONE CONSTRUCTED MATRIX FAMILY.  NONE OF IT SUPPLIES GRAVITY, A MASS SPECTRUM, A
TRANSFER OPERATOR, A CONTINUUM LIMIT OR A BOUNDARY CURVE IN THE (m, c) PLANE.
'MASS', 'SCALE', 'POSITIVITY', 'WINDOW' AND 'GENERIC' NAME PROPERTIES OF EXACT
RATIONAL MATRICES AND OF NOTHING ELSE, AND THEY ARE FENCED BEFORE THE FIRST
NUMBER IS READ.

  0. THE FIVE-POINT DEEP-ODD PACKAGE (C).  At the control (9/20, 5/13), at
     Block 188's two known-positive fixtures (1, 5/13) and (9/20, 3/5), and at
     the two FRESH points (1/2, 1/3) and (2/3, 1/5), the deep odd core t0 = 3
     gives charpoly(W) equal to a product of two palindromic integer quadratics
     each of multiplicity two, DIVIDED BY AN EXACT INTEGER: the polynomial
     SymPy returns is MONIC, so the displayed integer product is the polynomial
     only up to that scalar, which is DECLARED per point and gated at exactly
     zero residual.  THAT NORMALIZATION IS THE ADVERSARIAL CHECK'S C1
     CORRECTION AND IT IS CARRIED HERE AS CONTENT, NOT AS AN ERRATUM.

  1. PARITY INDEPENDENCE AND THE WINDOW CELL (D).  At all five points the
     even-deep core t0 = 2 and the odd-deep core t0 = 3 have the SAME
     characteristic polynomial, and the {2, 3} volume bump at v = 4/5 leaves
     the t0 = 5 monodromy MATRIX-EXACTLY unchanged while moving the core Gram
     in 64 of 64 entries (48 of 64 at zero shear) -- a nontrivial quotient
     cancellation and not a trivial invariance.

  2. THE BOUNDARY-LAYER STRUCTURE IS GENERIC TOO (E).  At T = 16 the core
     t0 = 4 = T/2 - 4 is a FAR BOUNDARY-LAYER core, not an even-deep one, and
     at every one of the five points its factorization is
     (heavy)^1 (light)^2 (boundary)^1 with a NON-RECIPROCAL boundary quadratic.
     Block 191's boundary-mode structure is (m, c)-generic on this grid.

  3. THE SPLIT, ON THE CHECK'S CENSUS (F).  The searched set is
     M x C with |M| = 12 and |C| = 17, 204 candidates, of which the 12 points
     with c = 2 have EXACTLY SINGULAR baseline Q and are excluded, leaving 192
     admissible.  THIS RUNNER RE-MEASURES A TWELVE-POINT SUBSET spanning the
     census -- SIX positive and SIX failing, including the witness -- and
     CITES the full 192-point census, which is measured OFFLINE and is NOT
     re-run here.  The positivity WINDOW is reported as MEASURED POINTS ONLY:
     no boundary curve is fitted and nothing is interpolated between points.

  4. THE MONOTONICITY CHAIN (G).  At fixed m = 1/2 over
     c in {1/5, 1/4, 1/3, 2/5, 9/20}, the exact traces T = 2 cosh(theta) obey
     T_heavy strictly INCREASING and T_light strictly DECREASING at every step,
     with every trace exceeding 2.  Since acosh(T/2) is positive and strictly
     increasing for T > 2, theta_heavy / theta_light strictly increases ON THIS
     FIVE-POINT DISCRETE GRID -- and that is all: no continuous monotonicity
     between grid points and no dispersion theorem.

WHAT IS NOT CLAIMED, STATED ONCE AND GATED AS CONSTANTS.  NO GRAVITY.  NO
GENERIC POSITIVITY: it fails at 98 of 192 searched points and the failure is
the block's own headline.  NO WINDOW BOUNDARY CURVE: the census is a finite set
of POINTS and no region, edge or interpolation is supplied.  NO EXHAUSTIVE
CENSUS: 'generic' is scoped to the searched rational sets and to nothing wider.
NO PHYSICAL MASS: theta is a logarithm of an algebraic number attached to a
rational matrix.  NO TRANSFER OPERATOR.  NO CONTINUUM.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 193 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin verified to be a REAL ancestor of HEAD that
     carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: seven imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, GENERIC POSITIVITY, a window boundary curve,
     an exhaustive census, a physical mass, the transfer operator and the
     continuum limit ALL declared NOT CLAIMED as measured constants, and ten
     gravity structures enumerated as NOT SUPPLIED.
  C  THE FIVE-POINT DEEP-ODD PACKAGE: the carrier controls and ranks; the five
     primitive factor pairs; the five EXACT MONIC NORMALIZATION scalars at zero
     residual; the perfect-square palindromic form; positivity by TWO
     independent exact routes with two distinct scales; and [W, U] = 0.
  D  PARITY AND THE WINDOW CELL: t0 = 2 against t0 = 3 at all five; the
     bump-{2,3} t0 = 5 matrix-exact zero at all five; and the core-Gram motion
     that makes it nontrivial.
  E  THE BOUNDARY LAYER: the (heavy)^1 (light)^2 (boundary)^1 shape, the five
     declared boundary quadratics, and their non-reciprocity with positive
     discriminant.
  F  THE SPLIT: the census frame with the c = 2 singularity re-measured; the
     universal legs on the twelve-point subset; the subset's six-six span; the
     exact (1/100, 3/4) witness with its negative reciprocal pair; the SECOND
     complex-unimodular failure mode; the cited full-census counts; and the
     measured-only discipline on the window.
  G  THE MONOTONICITY CHAIN: the five exact trace pairs; the five cross-product
     certificates; the four adjacent differences; and the ratio conclusion,
     discrete and fenced.
  H  the note at its final path, the N5 fence byte-identical, and the
     nsimplify count measured ZERO in this file's own source.

BASELINE EXPECTATION: A through H PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-six declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family census is
  A 2, B 8, C 6, D 3, E 3, F 8, G 4, H 2.
  SIX OF THE THIRTY-SIX GUARD CORRECTIONS RATHER THAN RESULTS:
  claim_positivity_generic asserts the refuted generic positivity;
  break_monic_normalization asserts the unnormalized integer product IS the
  characteristic polynomial; claim_window_boundary_curve asserts a boundary
  curve the census cannot supply; claim_census_exhaustive asserts the searched
  set is all of admissible (m, c) space; and break_failure_modes asserts that
  every positivity failure is a negative reciprocal pair.

RUNNING
  python3 scripts/admissibility_dirac_kahler_transfer_package_mc_generality_2026_08_25.py
  python3 ... --list-mutations
  python3 ... --mutation claim_positivity_generic
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

# THE MACHINERY IMPORT, LANDED, AND IT IS EXACTLY ONE OBJECT: the Block 105
# shear_hodge() re-exported by the Block 128 module, read here at a RATIONAL
# SHEAR that this block VARIES, which is precisely the freedom Blocks 190-193
# never exercised.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    MACHINERY_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    MACHINERY_IMPORT_LANDED = False

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 193 is the commit this block's branch
# is cut from; its note and its runner both exist at PARENT_COMMIT and NEITHER
# exists at STALE_PARENT_COMMIT, which is the Block 192 tip.
BLOCK193_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PARITY_WINDOW_INTERTWINING_LAW_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK193_RUNNER = (
    "scripts/admissibility_dirac_kahler_parity_window_intertwining_law_"
    "2026_08_25.py"
)
PARENT_ARTIFACTS = (BLOCK193_NOTE, BLOCK193_RUNNER)
# Refreshed by anchored sed at landing, exactly as the five pins are.
PARENT_ARTIFACT_BLOBS = (
    "310022e30f02ae9219384c71806ff2582b6f273a",   # Block 193 note
    "7ca31a2438c84cc67e207b7d7cd4daae64286d12",   # Block 193 runner
)
# THE CONSTRUCTION AUTHORITY: Block 190's width family, whose carrier, cores and
# monodromy are carried unchanged; Block 191's volume profile and boundary-mode
# structure; Block 105's primary, whose shear_hodge(c, v) is the one imported
# object; and Block 188's site route, which the width family is a disclosed
# variant of and whose two known-positive fixtures are two of the five points.
BLOCK192_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HYBRIDIZATION_MECHANISM_SUPPORT_CUTOFF_"
    "BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
BLOCK191_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK190_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_"
    "THEOREM_NOTE_2026-08-25.md"
)
BLOCK105_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
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
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_PACKAGE_MC_GENERALITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_PARITY_WINDOW_INTERTWINING_LAW_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_dirac_kahler_parity_window_intertwining_law_2026_08_25.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_HYBRIDIZATION_MECHANISM_SUPPORT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_OS_POSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  RE-RESOLVED LIVE AT DRAFT TIME: origin/main had MOVED past
# the Block 193 runner's recorded b11811704e, and the axiom and registry blobs
# were unchanged across that move.
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block193-"
              "parity-window-intertwining-law-20260825")
PARENT_COMMIT = "37a5f926c9e15745faaffda66b308f0d04e76e47"
# The Block 192 tip: a real ancestor of HEAD that predates Block 193 and
# therefore carries NEITHER Block 193 artifact.
STALE_PARENT_COMMIT = "afb66fc43c8858cc6a1d4cf943a14085e45be3f1"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_positivity_generic",
    "claim_window_boundary_curve",
    "claim_census_exhaustive",
    "claim_physical_mass",
    "claim_transfer_operator",
    "claim_continuum_limit",
    "break_carrier_controls",
    "break_grid_factors",
    "break_monic_normalization",
    "break_palindromic_square",
    "break_grid_positivity",
    "break_commutant",
    "break_parity_independence",
    "break_window_cell",
    "break_gram_motion",
    "break_boundary_shape",
    "break_boundary_factors",
    "break_boundary_nonreciprocal",
    "break_census_frame",
    "break_universal_subset",
    "break_subset_span",
    "break_witness",
    "break_failure_modes",
    "break_census_counts",
    "break_census_columns",
    "break_window_measured_only",
    "break_trace_table",
    "break_cross_products",
    "break_adjacent_differences",
    "break_ratio_monotonicity",
    "drop_n5_fence",
    "break_nsimplify_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_positivity_generic": "B",
    "claim_window_boundary_curve": "B",
    "claim_census_exhaustive": "B",
    "claim_physical_mass": "B",
    "claim_transfer_operator": "B",
    "claim_continuum_limit": "B",
    "break_carrier_controls": "C",
    "break_grid_factors": "C",
    "break_monic_normalization": "C",
    "break_palindromic_square": "C",
    "break_grid_positivity": "C",
    "break_commutant": "C",
    "break_parity_independence": "D",
    "break_window_cell": "D",
    "break_gram_motion": "D",
    "break_boundary_shape": "E",
    "break_boundary_factors": "E",
    "break_boundary_nonreciprocal": "E",
    "break_census_frame": "F",
    "break_universal_subset": "F",
    "break_subset_span": "F",
    "break_witness": "F",
    "break_failure_modes": "F",
    "break_census_counts": "F",
    "break_census_columns": "F",
    "break_window_measured_only": "F",
    "break_trace_table": "G",
    "break_cross_products": "G",
    "break_adjacent_differences": "G",
    "break_ratio_monotonicity": "G",
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
    "BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16, CARRIED UNCHANGED THROUGH BLOCKS 191, 192 AND 193 AND STILL A DISCLOSED VARIANT OF BLOCK 188's SITE CONSTRUCTION, BUT WITH ITS MASS/SHEAR PAIR (m, c) PROMOTED FROM A FIXTURE TO A VARIABLE: the staggered Dirac-Kahler carrier on Z_16 x Z_4 with eta_t = 1 and eta_x = (-1)^t, the temporal edge sign w = -1 on the WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, 8}, the site raising set A_s of the d_K entries in the CLOSED half {0..8} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H read at EVERY (m, c) probed here",
    "THE FIVE-POINT GRID, CHOSEN BY THE SOLVE AND DERIVED FROM NOTHING: the control (9/20, 5/13) that Blocks 190 to 193 all used, Block 188's two known-positive fixtures (1, 5/13) and (9/20, 3/5), and the two FRESH points (1/2, 1/3) and (2/3, 1/5) that the adversarial check rebuilt independently -- FIVE POINTS ARE NOT A SCAN AND A GRID IS NOT A PARAMETER SPACE",
    "THE ADVERSARIAL CHECK'S SEARCHED RATIONAL SET, IMPOSED HERE AS THE CENSUS FRAME AND NOT AS A DOMAIN: M = {1/100, 1/50, 1/20, 1/10, 1/5, 1/3, 1/2, 2/3, 1, 2, 5, 10} and C = {-99/100, -9/10, -3/4, -1/2, -1/5, 0, 1/5, 1/3, 1/2, 3/4, 9/10, 19/20, 99/100, 101/100, 6/5, 3/2, 2}, the full Cartesian product of 204 candidates of which the TWELVE with c = 2 have exactly singular baseline Q -- A FINITE SET OF RATIONAL POINTS AND NOT A REGION OF THE PLANE",
    "THE TWELVE-POINT RE-MEASURED SUBSET, CHOSEN BY THIS BLOCK TO SPAN THE SPLIT AND FOR NO OTHER REASON: six points where positivity holds and six where it fails, including the check's exact witness (1/100, 3/4), both fresh fixtures, both signs of c, both extremes of m, the zero-shear point and three points beyond the Hodge edge |c| > 1",
    "BLOCK 191's UNIT VOLUME PROFILE AND ITS {2, 3} BUMP AT v = 4/5, BOTH CARRIED UNCHANGED: a map v from the positive anchors {0..7} to the positive rationals, placed as B(c, v(t)) for t < 8 and as the P_4 image of the block of its thA_s(t) = -1-t partner for t >= 8, assembled by the quarter-weighted four-corner cell average",
    "THE PAIR CORES AND THEIR SHIFTED PAIRINGS, BLOCK 190's OBJECTS UNCHANGED: K_c[a,b] = G[idx(t_b, x_b), idx(theta_s t_a, x_a)], L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)] on G = Q^-1, the UNIT-CELL MONODROMY W = K_c^-1 L_2 and the momentum shift U -- NOT a derived transfer operator of any theory, and explicitly NOT repaired as one by this block",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE AT A VARYING RATIONAL SHEAR -- THE ONLY OBJECT IMPORTED, and the freedom in its first argument is exactly the freedom this block exercises",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL SEVEN ARE FALSE
# AND STAY FALSE.  THE SECOND IS THE ONE THE ADVERSARIAL CHECK REFUTED.
GRAVITY_SUPPLIED_CLAIMED = False
POSITIVITY_GENERIC_CLAIMED = False
WINDOW_BOUNDARY_CURVE_CLAIMED = False
CENSUS_EXHAUSTIVE_CLAIMED = False
PHYSICAL_MASS_CLAIMED = False
TRANSFER_OPERATOR_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
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
CHECK_VERDICT = "STRUCTURE-UNIVERSAL-POSITIVITY-WINDOWED-AND-THE-SPLIT-IS-THE-THEOREM"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
WIDTH = 16
SPACE_EXTENT = 4
CARRIER_SIZE = WIDTH * SPACE_EXTENT
CORE_SIZE = 8
UNIT_VOLUME = sp.Integer(1)
BUMP_VOLUME = sp.Rational(4, 5)
BUMP_ANCHORS = (2, 3)
DEEP_ODD_CORE = 3
DEEP_EVEN_CORE = 2
BOUNDARY_CORE = 4
WINDOW_CORE = 5


def rat(text: str) -> sp.Rational:
    """A rational from a plain string literal.  NOT nsimplify: sp.Rational on a
    decimal-free ratio of integers is exact by construction."""
    return sp.Rational(text)


# --- C: THE FIVE-POINT DEEP-ODD PACKAGE -------------------------------------
GRID = (("9/20", "5/13"), ("1", "5/13"), ("9/20", "3/5"),
        ("1/2", "1/3"), ("2/3", "1/5"))
# nnz(Q G - I), nnz(Ps Q Ps - Q^T), rank(Q), and the four core Gram ranks.
GRID_CONTROLS = (0, 0, CARRIER_SIZE, (8, 8, 8, 8))
# THE DEEP ODD CORE t0 = 3: the two PRIMITIVE palindromic integer quadratics,
# each of MULTIPLICITY TWO, as (a, b, a) coefficient triples.
GRID_FACTORS = {
    ("9/20", "5/13"): ((22569375, -233631106, 22569375),
                       (39529825, -109432706, 39529825)),
    ("1", "5/13"): ((26527, -444930, 26527), (51097, -289682, 51097)),
    ("9/20", "3/5"): ((12475, -273738, 12475), (53125, -142538, 53125)),
    ("1/2", "1/3"): ((233, -690, 233), (739, -7258, 739)),
    ("2/3", "1/5"): ((17099, -159050, 17099), (21709, -81434, 21709)),
}
GRID_MULTIPLICITY = 2
# THE ADVERSARIAL CHECK'S C1 CORRECTION, CARRIED AS CONTENT: SymPy's
# characteristic polynomial is MONIC, so the displayed integer product equals it
# only after division by THIS EXACT INTEGER.  The correction is a formula, not a
# hedge: charpoly_monic(W) = (a1 z^2 + b1 z + a1)^2 (a2 z^2 + b2 z + a2)^2 / s,
# and s = (a1 a2)^2 exactly, which is gated below as an identity and not merely
# as a table lookup.
GRID_MONIC_SCALARS = {
    ("9/20", "5/13"): 795955611005101889386962890625,
    ("1", "5/13"): 1837245025097114161,
    ("9/20", "3/5"): 439216851806640625,
    ("1/2", "1/3"): 29648362969,
    ("2/3", "1/5"): 137791066603200481,
}
MONIC_SCALAR_IS_LEADING_SQUARED = True
MONIC_RESIDUAL = 0
# THE PERFECT-SQUARE PALINDROMIC FORM: charpoly_monic(W) = p(z)^2 with
# p(z) = z^4 + alpha z^3 + beta z^2 + alpha z + 1, so all four reciprocal pairs
# are governed by the TRACE POLYNOMIAL q(T) = T^2 + alpha T + (beta - 2) whose
# roots are the two scales T = z + 1/z.
PALINDROMIC_SQUARE = True
# POSITIVITY BY TWO INDEPENDENT EXACT ROUTES.  Route one is the per-factor
# discriminant/trace/constant test on the primitive quadratics; route two is the
# scale census (# scales > 2, # in (-2,2), # < -2) read off q(T) with NO radical
# ever evaluated.  Positivity is (2, 0, 0) and the two routes must agree.
GRID_SCALE_CENSUS = (2, 0, 0)
GRID_POSITIVE = True
GRID_TWO_SCALES = True
ROUTES_AGREE = True
GRID_COMMUTATOR = 0

# --- D: PARITY INDEPENDENCE AND THE WINDOW CELL ------------------------------
PARITY_INDEPENDENT = True
WINDOW_CELL_RESIDUAL = 0
# nnz(K_bump - K_1) at t0 = 5: the core Gram DOES move, so the window-cell
# invariance is a quotient cancellation and not a trivial identity.
GRID_GRAM_MOTION = 64

# --- E: THE BOUNDARY-LAYER GENERICITY ---------------------------------------
# At T = 16 the core t0 = 4 = T/2 - 4 is a FAR BOUNDARY-LAYER core, not the
# even-deep representative (that is t0 = 2).  The solve read it as a parity test
# and it is not one; that mis-aim is carried as a correction.
BOUNDARY_SHAPE = (1, 2, 1)                 # (heavy)^1 (light)^2 (boundary)^1
BOUNDARY_FACTORS = {
    ("9/20", "5/13"): (48554286398375, -445467467014578, 43033320714375),
    ("1", "5/13"): (3750468703, -54521277270, 3250592053),
    ("9/20", "3/5"): (173474375, -2051118834, 93475175),
    ("1/2", "1/3"): (1098595, -9936202, 1011691),
    ("2/3", "1/5"): (209535268, -1901760850, 204452743),
}
BOUNDARY_NON_RECIPROCAL = True

# --- F: THE SPLIT -----------------------------------------------------------
CENSUS_MASSES = ("1/100", "1/50", "1/20", "1/10", "1/5", "1/3",
                 "1/2", "2/3", "1", "2", "5", "10")
CENSUS_SHEARS = ("-99/100", "-9/10", "-3/4", "-1/2", "-1/5", "0", "1/5",
                 "1/3", "1/2", "3/4", "9/10", "19/20", "99/100", "101/100",
                 "6/5", "3/2", "2")
CENSUS_CANDIDATES = 204
CENSUS_SINGULAR_SHEAR = "2"
CENSUS_SINGULAR_POINTS = 12
CENSUS_ADMISSIBLE = 192
# THE CITED FULL CENSUS, MEASURED OFFLINE AND NOT RE-RUN BY THIS RUNNER.  The
# runner gates the TWELVE-POINT SUBSET below; these four numbers are the
# offline totals and are declared as citations, gated only for internal
# consistency (universal legs total to the admissible count; positive plus
# failing total to it as well).
CENSUS_UNIVERSAL = 192
CENSUS_POSITIVE = 94
CENSUS_POSITIVITY_FAILURES = 98
# THE TWELVE-POINT SUBSET, RE-MEASURED HERE IN FULL.
CENSUS_SUBSET = (
    ("1/100", "3/4"), ("1/20", "9/10"), ("10", "3/4"),
    ("1/2", "1/3"), ("2/3", "1/5"),
    ("1/100", "-99/100"), ("10", "99/100"),
    ("1/2", "1/2"), ("2", "-1/2"),
    ("1/3", "0"), ("5", "101/100"), ("1/10", "3/2"),
)
SUBSET_SIZE = 12
SUBSET_POSITIVE = (("1/2", "1/3"), ("2/3", "1/5"), ("1/100", "-99/100"),
                   ("1/2", "1/2"), ("2", "-1/2"), ("1/3", "0"))
SUBSET_FAILING = (("1/100", "3/4"), ("1/20", "9/10"), ("10", "3/4"),
                  ("10", "99/100"), ("5", "101/100"), ("1/10", "3/2"))
SUBSET_SPAN = (6, 6)
# THE UNIVERSAL LEGS ON THE SUBSET: palindromic, perfect square, [W,U] = 0,
# parity independence, and the bump-{2,3} window cell -- 12 of 12 each.
SUBSET_UNIVERSAL_LEGS = 12
# The core Gram motion is 64 at every subset point EXCEPT the zero-shear point,
# where the {2,3} bump moves 48 of 64 entries.  It is nonzero everywhere, which
# is the only thing the nontriviality argument needs.
SUBSET_GRAM_MOTION = {("1/3", "0"): 48}
SUBSET_GRAM_MOTION_DEFAULT = 64
# THE EXACT WITNESS, digit for digit as the adversarial check recorded it.
WITNESS_POINT = ("1/100", "3/4")
WITNESS_FACTORS = ((57536, 5175457, 57536), (1322536, -2645457, 1322536))
WITNESS_MONIC_SCALAR = 5790210286399072239616
WITNESS_NEGATIVE_FACTOR = (57536, 5175457, 57536)
WITNESS_NEGATIVE_DISCRIMINANT = 26772113593665
WITNESS_ROOT_PRODUCT = 1
WITNESS_ROOT_SUM_NEGATIVE = True
WITNESS_POSITIVE_FACTOR = (1322536, -2645457, 1322536)
WITNESS_POSITIVE_DISCRIMINANT = 2036853665
# THE SECOND FAILURE MODE, WHICH IS THIS BLOCK'S OWN REFINEMENT OF THE CHECK.
# The check reported its failures as NEGATIVE reciprocal pairs.  Measured here:
# the failing set also contains points whose failing pairs are COMPLEX and
# UNIMODULAR, carrying NO negative pair at all.  The scale census separates the
# modes exactly: (2,0,0) positive, (1,0,1) one negative pair, (1,1,0) one
# complex pair, (0,2,0) both pairs complex.
FAILURE_MODES = {
    ("1/100", "3/4"): (1, 0, 1),
    ("1/20", "9/10"): (1, 0, 1),
    ("10", "3/4"): (1, 0, 1),
    ("10", "99/100"): (1, 0, 1),
    ("5", "101/100"): (0, 2, 0),
    ("1/10", "3/2"): (1, 1, 0),
}
NEGATIVE_PAIR_POINTS = 4
COMPLEX_PAIR_POINTS = 2
ALL_FAILURES_ARE_NEGATIVE_PAIRS = False
# THE HODGE EDGE, WHICH IS WHERE THE TWO MODES SEPARATE.  The displayed shear
# metric is g(c) = [[1, c], [c, 1]] with det g = 1 - c^2, so |c| > 1 is exactly
# where g is INDEFINITE.  Measured on the subset and cited from the full census:
# every searched point with c > 1 fails, and fails by the COMPLEX mode with no
# negative pair; every NEGATIVE-pair failure sits at |c| < 1.
HODGE_EDGE_SEPARATES_MODES = True
# THE CITED FULL-CENSUS COLUMN TABLE, MEASURED OFFLINE AND NOT RE-RUN HERE:
# per shear column, (positive, negative-pair, complex-pair) over the twelve
# searched masses.  Two whole-column facts live in it -- the four columns
# c = 3/4, 9/10, 19/20, 99/100 fail at EVERY searched mass by a negative pair,
# which extends the check's single c = 3/4 observation; and the three columns
# beyond the Hodge edge fail at every searched mass by the complex mode.
CENSUS_COLUMNS = {
    "-99/100": (9, 3, 0),
    "-9/10": (10, 2, 0),
    "-3/4": (10, 2, 0),
    "-1/2": (10, 2, 0),
    "-1/5": (12, 0, 0),
    "0": (12, 0, 0),
    "1/5": (11, 1, 0),
    "1/3": (10, 2, 0),
    "1/2": (10, 2, 0),
    "3/4": (0, 12, 0),
    "9/10": (0, 12, 0),
    "19/20": (0, 12, 0),
    "99/100": (0, 12, 0),
    "101/100": (0, 0, 12),
    "6/5": (0, 0, 12),
    "3/2": (0, 0, 12),
}
CENSUS_NEGATIVE_PAIR_TOTAL = 62
CENSUS_COMPLEX_PAIR_TOTAL = 36
MASS_UNIFORM_NEGATIVE_COLUMNS = ("3/4", "9/10", "19/20", "99/100")
BEYOND_EDGE_COLUMNS = ("101/100", "6/5", "3/2")
# MEASURED-ONLY DISCIPLINE: the census is a finite set of POINTS.  No boundary
# curve is fitted, nothing is interpolated between points, and no point outside
# the searched set is asserted either way.
WINDOW_IS_MEASURED_POINTS_ONLY = True
WINDOW_BOUNDARY_POINTS_CLAIMED = 0

# --- G: THE MONOTONICITY CHAIN ----------------------------------------------
MONOTONICITY_MASS = "1/2"
MONOTONICITY_SHEARS = ("1/5", "1/4", "1/3", "2/5", "9/20")
# THE EXACT TRACES T = 2 cosh(theta) = -b/a per primitive palindromic factor,
# as (heavy, light) pairs of (numerator, denominator).
MONOTONICITY_TRACES = {
    "1/5": ((63258, 7619), (28762, 9629)),
    "1/4": ((6223, 709), (575, 193)),
    "1/3": ((7258, 739), (690, 233)),
    "2/5": ((12922, 1171), (6298, 2141)),
    "9/20": ((3084847, 250021), (1534683, 525061)),
}
# THE CROSS-PRODUCT CERTIFICATES for T_heavy - T_light > 0: the exact integer
# num(heavy) den(light) - num(light) den(heavy), all five strictly positive.
MONOTONICITY_CROSS = {
    "1/5": 389973604,
    "1/4": 793364,
    "1/3": 1181204,
    "2/5": 20291044,
    "9/20": 1236029872324,
}
# THE FOUR ADJACENT EXACT DIFFERENCES as c increases.
MONOTONICITY_HEAVY_STEPS = (
    ("1/5", "1/4", 2563115, 5401871),
    ("1/4", "1/3", 547125, 523951),
    ("1/3", "2/5", 1050240, 865369),
    ("2/5", "9/20", 381584475, 292774591),
)
MONOTONICITY_LIGHT_STEPS = (
    ("1/5", "1/4", -14391, 1858397),
    ("1/4", "1/3", -805, 44969),
    ("1/3", "2/5", -9856, 498853),
    ("2/5", "9/20", -21077875, 1124155601),
)
ALL_TRACES_EXCEED_TWO = True
HEAVY_STRICTLY_INCREASING = True
LIGHT_STRICTLY_DECREASING = True
# AND THEREFORE the ratio increases -- ON THE FIVE-POINT DISCRETE GRID ONLY.
RATIO_STRICTLY_INCREASING_ON_GRID = True
CONTINUOUS_MONOTONICITY_CLAIMED = False

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO, so a discriminant, a trace difference or a residual passed
# through it can silently turn a POSITIVITY FAILURE into a PASS -- and this
# block is a block whose entire content is a sign census over 192 points.  The
# thinnest margin in the gated subset is at (1/100, -99/100), a POSITIVE point
# whose light scale T = 520153019601/260073505000 exceeds 2 by 6009601/
# 260073505000, about 2.3e-5.
# Every mass, shear, volume and amplitude here is ALREADY an exact sympy
# Rational.  Gate H counts the occurrences in this file's own source and
# requires ZERO.
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
    QQ^(n x n) exactly; DomainMatrix carries out the inverse and the rank by
    exact fraction-free arithmetic over that field.  No float is created at any
    point and no tolerance exists to be tuned.  It is used in place of the dense
    sympy fallback purely because that is slow at dimension 64, and it changes
    NO value."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return rational_matrix(matrix).inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    return rational_matrix(matrix).rank()


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is
    involved."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


Z = sp.Symbol("z")
T_SYMBOL = sp.Symbol("T")


# ---------------------------------------------------------------------------
# THE WIDTH FAMILY AT AN ARBITRARY (m, c).  Everything except the shear block is
# rebuilt here; the shear block is the ONE import, and its first argument is the
# variable this block introduces.
# ---------------------------------------------------------------------------
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def site_index(time: int, space: int) -> int:
    return (time % WIDTH) * SPACE_EXTENT + space % SPACE_EXTENT


def site_theta(time: int) -> int:
    """theta_s(t) = -t, fixing the slices {0, T/2}."""
    return (-time) % WIDTH


def anchor_theta(time: int) -> int:
    """thA_s(t) = -1-t: the ANCHOR reflection that carries a NON-UNIFORM volume
    profile across the seam."""
    return (-1 - time) % WIDTH


def staggered_kernel() -> sp.Matrix:
    kernel = sp.zeros(CARRIER_SIZE, CARRIER_SIZE)
    for time in range(WIDTH):
        for space in range(SPACE_EXTENT):
            temporal_sign = -1 if time == WIDTH - 1 else 1
            here = site_index(time, space)
            ahead = site_index(time + 1, space)
            kernel[here, ahead] += sp.Rational(temporal_sign, 2)
            kernel[ahead, here] -= sp.Rational(temporal_sign, 2)
            spatial_sign = (-1) ** time
            right = site_index(time, space + 1)
            kernel[here, right] += sp.Rational(spatial_sign, 2)
            kernel[right, here] -= sp.Rational(spatial_sign, 2)
    return kernel


def grade_projector(grade: int) -> sp.Matrix:
    return sp.diag(*[1 if (time % 2 + space % 2) == grade else 0
                     for time in range(WIDTH) for space in range(SPACE_EXTENT)])


def raising_part(kernel: sp.Matrix) -> sp.Matrix:
    p0, p1, p2 = (grade_projector(g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def reflection_permutation() -> sp.Matrix:
    matrix = sp.zeros(CARRIER_SIZE, CARRIER_SIZE)
    for time in range(WIDTH):
        for space in range(SPACE_EXTENT):
            matrix[site_index(site_theta(time), space),
                   site_index(time, space)] = 1
    return matrix


def site_restricted_raising(raising: sp.Matrix) -> sp.Matrix:
    half = WIDTH // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(CARRIER_SIZE, CARRIER_SIZE)
    for row in range(CARRIER_SIZE):
        for column in range(CARRIER_SIZE):
            if raising[row, column] == 0:
                continue
            row_time = row // SPACE_EXTENT
            column_time = column // SPACE_EXTENT
            if row_time not in closed or column_time not in closed:
                continue
            if row_time == column_time and row_time in fixed:
                continue
            matrix[row, column] = raising[row, column]
    return matrix


def cell_embedding(time: int, space: int) -> sp.Matrix:
    matrix = sp.zeros(CARRIER_SIZE, 4)
    for column, (delta_t, delta_x) in enumerate(
            ((0, 0), (0, 1), (1, 0), (1, 1))):
        matrix[site_index(time + delta_t, space + delta_x), column] = 1
    return matrix


KERNEL = staggered_kernel()
REFLECTION = reflection_permutation()
RAISING_SET = site_restricted_raising(raising_part(KERNEL))
GLUE = sp.expand(RAISING_SET - REFLECTION * RAISING_SET * REFLECTION)
EMBEDDINGS = {(time, space): cell_embedding(time, space)
              for time in range(WIDTH) for space in range(SPACE_EXTENT)}


def imported_shear_block(shear: sp.Rational, volume: object) -> sp.Matrix:
    """THE ONE IMPORTED OBJECT: the LANDED Block 105 shear Hodge
    diag(v, v g(c)^-1, 1/v) with g(c) = [[1, c], [c, 1]].  NO nsimplify: both
    arguments are already exact sympy Rationals."""
    return sp.Matrix(b128.block105.shear_hodge(shear, volume))


def volume_profile(anchors: tuple = (), volume: object = UNIT_VOLUME) -> dict:
    return {time: (volume if time in anchors else UNIT_VOLUME)
            for time in range(WIDTH // 2)}


def site_hodge(shear: sp.Rational, profile: dict) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule
    at Block 190's seam convention."""
    half = WIDTH // 2
    blocks = {}
    for time in range(WIDTH):
        if time < half:
            blocks[time] = imported_shear_block(shear, profile[time])
        else:
            block = imported_shear_block(shear, profile[anchor_theta(time)])
            blocks[time] = sp.expand(
                OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    result = sp.zeros(CARRIER_SIZE, CARRIER_SIZE)
    for time, block in blocks.items():
        for space in range(SPACE_EXTENT):
            embedding = EMBEDDINGS[time, space]
            result += embedding * block * embedding.T / 4
    return sp.expand(result)


def completion(mass: sp.Rational, hodge: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    return sp.expand(mass * hodge + hodge * GLUE - GLUE.T * hodge)


def core_cells(core: int) -> tuple:
    return tuple((time, space) for time in (core, core + 1)
                 for space in range(SPACE_EXTENT))


def shifted_pairing(inverse: sp.Matrix, core: int, step: int) -> sp.Matrix:
    """L_k[a,b] = G[idx(t_b + k, x_b), idx(theta_s t_a, x_a)]; k = 0 is K_c."""
    cells = core_cells(core)
    matrix = sp.zeros(CORE_SIZE, CORE_SIZE)
    for row, (row_time, row_space) in enumerate(cells):
        partner = site_index(site_theta(row_time), row_space)
        for column, (column_time, column_space) in enumerate(cells):
            matrix[row, column] = inverse[
                site_index(column_time + step, column_space), partner]
    return matrix


def momentum_shift(core: int) -> sp.Matrix:
    """U: the two-site spatial shift on the core's eight cells, whose commutant
    with W is the U-grading Block 190 recorded."""
    cells = core_cells(core)
    position = {cell: index for index, cell in enumerate(cells)}
    matrix = sp.zeros(CORE_SIZE, CORE_SIZE)
    for time, space in cells:
        matrix[position[time, (space + 2) % SPACE_EXTENT],
               position[time, space]] = 1
    return matrix


# ---------------------------------------------------------------------------
# THE HEAVY WORK, DONE ONCE PER (m, c, profile) AND SHARED.  The 64 x 64 exact
# inverse is the only expensive step in this runner and nothing recomputes one.
# ---------------------------------------------------------------------------
_CARRIER_CACHE: dict = {}


def carrier(mass_text: str, shear_text: str, anchors: tuple = ()) -> dict:
    key = (mass_text, shear_text, anchors)
    if key in _CARRIER_CACHE:
        return _CARRIER_CACHE[key]
    mass, shear = rat(mass_text), rat(shear_text)
    profile = volume_profile(anchors, BUMP_VOLUME if anchors else UNIT_VOLUME)
    hodge = site_hodge(shear, profile)
    action = completion(mass, hodge)
    domain = rational_matrix(action)
    rank = domain.rank()
    record = {"mass": mass, "shear": shear, "action": action, "rank": rank,
              "inverse": None}
    if rank == CARRIER_SIZE:
        record["inverse"] = domain.inv().to_Matrix()
    _CARRIER_CACHE[key] = record
    return record


def monodromy(inverse: sp.Matrix, core: int) -> tuple:
    gram = shifted_pairing(inverse, core, 0)
    two_step = shifted_pairing(inverse, core, 2)
    return gram, sp.expand(exact_inverse(gram) * two_step)


# ---------------------------------------------------------------------------
# THE EXACT SPECTRAL READ.  Everything below is polynomial arithmetic over QQ:
# no root is ever evaluated, no radical is taken and no float exists.
# ---------------------------------------------------------------------------
def primitive_coefficients(expression: sp.Expr) -> tuple:
    """The integer PRIMITIVE form of a rational polynomial: clear denominators
    by their lcm, divide by the integer content, and fix a positive leader."""
    coefficients = [sp.Rational(value)
                    for value in sp.Poly(sp.expand(expression), Z).all_coeffs()]
    multiplier = 1
    for value in coefficients:
        multiplier = sp.ilcm(multiplier, value.q)
    integers = [sp.Integer(value * multiplier) for value in coefficients]
    content = 0
    for value in integers:
        content = sp.igcd(content, int(value))
    integers = [value // content for value in integers]
    if integers[0] < 0:
        integers = [-value for value in integers]
    return tuple(int(value) for value in integers)


def primitive_factors(monodromy_matrix: sp.Matrix) -> tuple:
    """The primitive irreducible QQ factors of charpoly(W) with multiplicity."""
    factors = []
    for factor, multiplicity in sp.factor_list(
            monodromy_matrix.charpoly(Z).as_expr())[1]:
        if factor.has(Z):
            factors.append((primitive_coefficients(factor), int(multiplicity)))
    return tuple(sorted(factors, key=lambda item: (len(item[0]), item[0])))


def monic_charpoly(monodromy_matrix: sp.Matrix) -> sp.Poly:
    return sp.Poly(monodromy_matrix.charpoly(Z).as_expr(), Z).monic()


def factor_expression(coefficients: tuple) -> sp.Expr:
    degree = len(coefficients) - 1
    return sum(sp.Integer(coefficients[i]) * Z ** (degree - i)
               for i in range(len(coefficients)))


def monic_scalar(monodromy_matrix: sp.Matrix, factors: tuple) -> tuple:
    """THE CHECK'S C1 CORRECTION AS AN EXACT MEASUREMENT.  Returns the scalar s
    and the polynomial residual of

        prod_i (primitive factor_i)^(multiplicity_i)  =  s * charpoly_monic(W).

    A zero residual with an integer s is the whole content of the correction:
    the displayed integer product is the characteristic polynomial only after
    division by s."""
    product = sp.Integer(1)
    for coefficients, multiplicity in factors:
        product *= factor_expression(coefficients) ** multiplicity
    monic = monic_charpoly(monodromy_matrix).as_expr()
    quotient, remainder = sp.div(sp.expand(product), sp.expand(monic), Z)
    return sp.Rational(quotient), sp.expand(remainder)


def palindromic(coefficients: tuple) -> bool:
    return tuple(coefficients) == tuple(reversed(coefficients))


def palindromic_square_root(monodromy_matrix: sp.Matrix):
    """THE DEGREE-FOUR PALINDROMIC SQUARE ROOT p of the deep monic charpoly,
    returned as (alpha, beta) with p(z) = z^4 + alpha z^3 + beta z^2 + alpha z
    + 1, or None when the charpoly is not such a perfect square.  The square is
    verified by exact expansion, not assumed from the multiplicities."""
    monic = monic_charpoly(monodromy_matrix)
    if monic.degree() != 8:
        return None
    root = sp.Poly(1, Z, domain=QQ)
    for factor, multiplicity in sp.factor_list(monic.as_expr())[1]:
        if not factor.has(Z):
            continue
        if multiplicity % 2:
            return None
        root *= sp.Poly(factor, Z).monic() ** (multiplicity // 2)
    if root.degree() != 4:
        return None
    if sp.expand(root.as_expr() ** 2 - monic.as_expr()) != 0:
        return None
    coefficients = [sp.Rational(value) for value in root.all_coeffs()]
    if coefficients[0] != 1 or coefficients[4] != 1:
        return None
    if coefficients[1] != coefficients[3]:
        return None
    return coefficients[1], coefficients[2]


def trace_polynomial(monodromy_matrix: sp.Matrix):
    """q(T) = T^2 + alpha T + (beta - 2), the polynomial whose two roots are the
    SCALES T = z + 1/z of the deep monic charpoly.  Substituting z + 1/z into
    z^-2 p(z) gives (T^2 - 2) + alpha T + beta, which is q exactly."""
    root = palindromic_square_root(monodromy_matrix)
    if root is None:
        return None
    alpha, beta = root
    return sp.Integer(1), alpha, beta - 2


def scale_census(trace_poly) -> tuple:
    """THE EXACT SCALE CENSUS, WITH NO RADICAL EVER EVALUATED.  For
    q(T) = T^2 + alpha T + gamma the count of roots above 2, strictly inside
    (-2, 2) and below -2 is read off the sign of q(2), the sign of q(-2) and the
    position of the vertex -alpha/2.  T > 2 is the hyperbolic branch
    T = 2 cosh(theta), hence a POSITIVE reciprocal pair e^{+/-theta}; T < -2 is
    a NEGATIVE real reciprocal pair; |T| < 2 gives a COMPLEX pair on the unit
    circle."""
    if trace_poly is None:
        return None
    _, alpha, gamma = trace_poly
    discriminant = alpha * alpha - 4 * gamma
    if discriminant < 0:
        return (0, 0, 0, discriminant)
    at_two = 4 + 2 * alpha + gamma
    at_minus_two = 4 - 2 * alpha + gamma
    vertex = -alpha / 2
    above = 2 if (at_two > 0 and vertex > 2) else (1 if at_two < 0 else 0)
    below = 2 if (at_minus_two > 0 and vertex < -2) else (
        1 if at_minus_two < 0 else 0)
    return (above, 2 - above - below, below, discriminant)


def factor_roots_positive(coefficients: tuple) -> bool:
    """ROUTE ONE, INDEPENDENT OF THE SCALE CENSUS: an exact per-factor sign test
    on one primitive irreducible QQ factor of the characteristic polynomial.
    A linear factor a z + b has the single root -b/a; a quadratic
    a z^2 + b z + c has two real positive roots exactly when its discriminant is
    positive and both -b/a and c/a are positive."""
    if len(coefficients) == 2:
        return sp.Rational(-coefficients[1], coefficients[0]) > 0
    if len(coefficients) == 3:
        a, b, c = coefficients
        return (b * b - 4 * a * c > 0
                and sp.Rational(-b, a) > 0 and sp.Rational(c, a) > 0)
    return False


def all_roots_positive(factors: tuple) -> bool:
    return all(factor_roots_positive(coefficients)
               for coefficients, _ in factors)


def reciprocal_quadratics(factors: tuple) -> tuple:
    return tuple((coefficients, multiplicity)
                 for coefficients, multiplicity in factors
                 if len(coefficients) == 3
                 and coefficients[0] == coefficients[2])


def factor_trace(coefficients: tuple) -> sp.Rational:
    """T = 2 cosh(theta) = -b/a for a primitive palindromic factor a z^2+b z+a."""
    return sp.Rational(-coefficients[1], coefficients[0])


def boundary_shape(deep_factors: tuple, boundary_factors: tuple) -> tuple:
    """THE FAR BOUNDARY-LAYER SHAPE at t0 = 4: the two deep quadratics reappear
    with multiplicities (heavy)^1 (light)^2 and exactly one NEW quadratic
    appears with multiplicity one, and that new factor is NON-reciprocal."""
    deep = {coefficients: multiplicity
            for coefficients, multiplicity in deep_factors}
    seen, extra = {}, []
    for coefficients, multiplicity in boundary_factors:
        if coefficients in deep:
            seen[coefficients] = multiplicity
        else:
            extra.append((coefficients, multiplicity))
    quadratics = sorted(((factor_trace(coefficients), coefficients)
                         for coefficients in deep if len(coefficients) == 3),
                        reverse=True)
    if len(quadratics) != 2 or len(extra) != 1:
        return (0, 0, 0), None
    heavy, light = quadratics[0][1], quadratics[1][1]
    coefficients, multiplicity = extra[0]
    shape = (seen.get(heavy, 0), seen.get(light, 0), multiplicity)
    return shape, coefficients


def non_reciprocal(coefficients: tuple) -> bool:
    """The boundary quadratic is NOT palindromic -- its roots do not come in a
    reciprocal pair -- and it still has two real roots."""
    if len(coefficients) != 3:
        return False
    a, b, c = coefficients
    return a != c and b * b - 4 * a * c > 0


# ---------------------------------------------------------------------------
# THE MEASUREMENT PASS.  Every number this runner reports is produced here, once
# and before any mutation flag is read, and every heavy inverse is shared.
# ---------------------------------------------------------------------------
@dataclass
class PointFacts:
    rank: int
    inverse_residual: int
    covariance_residual: int
    gram_ranks: tuple
    factors: tuple
    monic_scalar: object
    monic_residual: object
    monic_scalar_is_leading_squared: bool
    charpoly_palindromic: bool
    perfect_square: bool
    trace_poly: object
    scale_census: object
    positive_by_census: bool
    positive_by_factors: bool
    two_scales: bool
    traces: tuple
    commutator_residual: int
    parity_equal: bool
    window_residual: object
    gram_motion: object
    boundary_shape: object
    boundary_factor: object


def measure_point(mass_text: str, shear_text: str, want_bump: bool,
                  want_boundary: bool) -> PointFacts:
    base = carrier(mass_text, shear_text)
    rank = base["rank"]
    if rank != CARRIER_SIZE:
        return PointFacts(rank, -1, -1, (), (), None, None, False, False,
                          False, None, None, False, False, False, (), -1,
                          False, None, None, None, None)
    inverse, action = base["inverse"], base["action"]
    inverse_residual = residual_count(action * inverse - sp.eye(CARRIER_SIZE))
    covariance_residual = residual_count(
        REFLECTION * action * REFLECTION - action.T)

    cores = (DEEP_EVEN_CORE, DEEP_ODD_CORE, WINDOW_CORE)
    if want_boundary:
        cores = cores + (BOUNDARY_CORE,)
    frames = {core: monodromy(inverse, core) for core in cores}
    gram_ranks = tuple(exact_rank(frames[core][0]) for core in sorted(frames))

    deep = frames[DEEP_ODD_CORE][1]
    factors = primitive_factors(deep)
    scalar, remainder = monic_scalar(deep, factors)
    quadratics = reciprocal_quadratics(factors)
    leading_product = sp.Integer(1)
    for coefficients, multiplicity in factors:
        leading_product *= sp.Integer(coefficients[0]) ** multiplicity
    monic_charpoly_coefficients = primitive_coefficients(
        deep.charpoly(Z).as_expr())
    trace_poly = trace_polynomial(deep)
    census = scale_census(trace_poly)
    shift = momentum_shift(DEEP_ODD_CORE)

    even = frames[DEEP_EVEN_CORE][1]
    parity_equal = (primitive_coefficients(even.charpoly(Z).as_expr())
                    == monic_charpoly_coefficients)

    window_residual, gram_motion = None, None
    if want_bump:
        bumped = carrier(mass_text, shear_text, BUMP_ANCHORS)
        if bumped["rank"] == CARRIER_SIZE:
            bump_gram, bump_monodromy = monodromy(bumped["inverse"],
                                                  WINDOW_CORE)
            window_residual = residual_count(
                bump_monodromy - frames[WINDOW_CORE][1])
            gram_motion = residual_count(bump_gram - frames[WINDOW_CORE][0])

    shape, boundary_factor = (None, None)
    if want_boundary:
        shape, boundary_factor = boundary_shape(
            factors, primitive_factors(frames[BOUNDARY_CORE][1]))

    return PointFacts(
        rank=rank,
        inverse_residual=inverse_residual,
        covariance_residual=covariance_residual,
        gram_ranks=gram_ranks,
        factors=factors,
        monic_scalar=scalar,
        monic_residual=remainder,
        monic_scalar_is_leading_squared=(scalar == leading_product),
        charpoly_palindromic=palindromic(monic_charpoly_coefficients),
        perfect_square=trace_poly is not None,
        trace_poly=trace_poly,
        scale_census=census,
        positive_by_census=bool(census and census[:3] == (2, 0, 0)),
        positive_by_factors=all_roots_positive(factors),
        two_scales=bool(census and census[3] != 0),
        traces=tuple(sorted((factor_trace(coefficients)
                             for coefficients, _ in quadratics), reverse=True)),
        commutator_residual=residual_count(deep * shift - shift * deep),
        parity_equal=parity_equal,
        window_residual=window_residual,
        gram_motion=gram_motion,
        boundary_shape=shape,
        boundary_factor=boundary_factor)


@dataclass
class Facts:
    main_head: str
    authority: AuthorityCertificate
    scope: dict
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    grid: dict
    subset: dict
    singular_ranks: dict
    census_frame: tuple
    monotonicity: dict
    monotonicity_cross: dict
    heavy_steps: dict
    light_steps: dict
    heavy_increasing: bool
    light_decreasing: bool
    traces_exceed_two: bool
    inverse_count: int
    nsimplify_calls: int


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    authority = authority_certificate(main_head)
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""

    # ---- C, D, E: the five-point grid, full package ------------------------
    grid = {point: measure_point(point[0], point[1], True, True)
            for point in GRID}

    # ---- F: the twelve-point census subset ---------------------------------
    subset = {}
    for point in CENSUS_SUBSET:
        subset[point] = (grid[point] if point in grid
                         else measure_point(point[0], point[1], True, False))

    # ---- F: the c = 2 exclusion, RE-MEASURED rather than taken on report ----
    # The census frame says the twelve c = 2 candidates have exactly singular
    # baseline Q.  Two of them are rebuilt here at opposite ends of M; the
    # displayed shear Hodge has denominator 1 - c^2 = -3 there, so the
    # singularity is a property of Q and not of the Hodge block.
    singular_ranks = {}
    for mass_text in (CENSUS_MASSES[0], CENSUS_MASSES[-1]):
        singular_ranks[(mass_text, CENSUS_SINGULAR_SHEAR)] = carrier(
            mass_text, CENSUS_SINGULAR_SHEAR)["rank"]
    census_frame = (len(CENSUS_MASSES), len(CENSUS_SHEARS),
                    len(CENSUS_MASSES) * len(CENSUS_SHEARS),
                    len(CENSUS_MASSES) * len(CENSUS_SHEARS)
                    - len(CENSUS_MASSES))

    # ---- G: the monotonicity chain at fixed m = 1/2 ------------------------
    monotonicity, monotonicity_cross = {}, {}
    for shear_text in MONOTONICITY_SHEARS:
        facts = measure_point(MONOTONICITY_MASS, shear_text, False, False)
        monotonicity[shear_text] = facts
        if len(facts.traces) == 2:
            heavy, light = facts.traces
            monotonicity_cross[shear_text] = sp.Integer(
                heavy.p * light.q - light.p * heavy.q)
    heavy_steps, light_steps = {}, {}
    for index in range(len(MONOTONICITY_SHEARS) - 1):
        low, high = MONOTONICITY_SHEARS[index], MONOTONICITY_SHEARS[index + 1]
        if len(monotonicity[low].traces) != 2:
            continue
        if len(monotonicity[high].traces) != 2:
            continue
        heavy_steps[(low, high)] = (monotonicity[high].traces[0]
                                    - monotonicity[low].traces[0])
        light_steps[(low, high)] = (monotonicity[high].traces[1]
                                    - monotonicity[low].traces[1])

    return Facts(
        main_head=main_head,
        authority=authority,
        scope=scope_certificate(note_text),
        imposed=len(IMPOSED_OBJECTS),
        registered=len(REGISTERED_OBJECTS),
        adopted=len(ADOPTED_OBJECTS),
        unsupplied=len(UNSUPPLIED_GRAVITY_STRUCTURES),
        grid=grid,
        subset=subset,
        singular_ranks=singular_ranks,
        census_frame=census_frame,
        monotonicity=monotonicity,
        monotonicity_cross=monotonicity_cross,
        heavy_steps=heavy_steps,
        light_steps=light_steps,
        heavy_increasing=all(value > 0 for value in heavy_steps.values()),
        light_decreasing=all(value < 0 for value in light_steps.values()),
        traces_exceed_two=all(
            trace > 2
            for facts in monotonicity.values() for trace in facts.traces),
        inverse_count=len(_CARRIER_CACHE),
        nsimplify_calls=nsimplify_occurrences())


# ---------------------------------------------------------------------------
# THE CLAIMS, and the thirty-six mutations that each rewrite exactly one
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims = {
        # A -- authority.
        "main_head": CURRENT_MAIN,
        "parent_commit": PARENT_COMMIT,
        "stale_parent": STALE_PARENT_COMMIT,
        # B -- the banner.
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "positivity_generic": POSITIVITY_GENERIC_CLAIMED,
        "window_boundary_curve": WINDOW_BOUNDARY_CURVE_CLAIMED,
        "census_exhaustive": CENSUS_EXHAUSTIVE_CLAIMED,
        "physical_mass": PHYSICAL_MASS_CLAIMED,
        "transfer_operator": TRANSFER_OPERATOR_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        # C -- the five-point deep-odd package.
        "grid_controls": GRID_CONTROLS,
        "grid_factors": dict(GRID_FACTORS),
        "grid_multiplicity": GRID_MULTIPLICITY,
        "grid_monic_scalars": dict(GRID_MONIC_SCALARS),
        "monic_scalar_is_leading_squared": MONIC_SCALAR_IS_LEADING_SQUARED,
        "monic_residual": MONIC_RESIDUAL,
        "palindromic_square": PALINDROMIC_SQUARE,
        "grid_scale_census": GRID_SCALE_CENSUS,
        "grid_positive": GRID_POSITIVE,
        "grid_two_scales": GRID_TWO_SCALES,
        "routes_agree": ROUTES_AGREE,
        "grid_commutator": GRID_COMMUTATOR,
        # D -- parity and the window cell.
        "parity_independent": PARITY_INDEPENDENT,
        "window_cell_residual": WINDOW_CELL_RESIDUAL,
        "grid_gram_motion": GRID_GRAM_MOTION,
        # E -- the boundary layer.
        "boundary_shape": BOUNDARY_SHAPE,
        "boundary_factors": dict(BOUNDARY_FACTORS),
        "boundary_non_reciprocal": BOUNDARY_NON_RECIPROCAL,
        # F -- the split.
        "census_frame": (len(CENSUS_MASSES), len(CENSUS_SHEARS),
                         CENSUS_CANDIDATES, CENSUS_ADMISSIBLE),
        "census_singular_points": CENSUS_SINGULAR_POINTS,
        "census_universal": CENSUS_UNIVERSAL,
        "census_positive": CENSUS_POSITIVE,
        "census_failures": CENSUS_POSITIVITY_FAILURES,
        "subset_universal_legs": SUBSET_UNIVERSAL_LEGS,
        "subset_span": SUBSET_SPAN,
        "subset_positive": SUBSET_POSITIVE,
        "subset_failing": SUBSET_FAILING,
        "subset_gram_motion": dict(SUBSET_GRAM_MOTION),
        "witness_factors": WITNESS_FACTORS,
        "witness_monic_scalar": WITNESS_MONIC_SCALAR,
        "witness_negative_discriminant": WITNESS_NEGATIVE_DISCRIMINANT,
        "witness_positive_discriminant": WITNESS_POSITIVE_DISCRIMINANT,
        "failure_modes": dict(FAILURE_MODES),
        "negative_pair_points": NEGATIVE_PAIR_POINTS,
        "complex_pair_points": COMPLEX_PAIR_POINTS,
        "all_failures_negative": ALL_FAILURES_ARE_NEGATIVE_PAIRS,
        "hodge_edge_separates": HODGE_EDGE_SEPARATES_MODES,
        "census_columns": dict(CENSUS_COLUMNS),
        "census_negative_total": CENSUS_NEGATIVE_PAIR_TOTAL,
        "census_complex_total": CENSUS_COMPLEX_PAIR_TOTAL,
        "window_measured_only": WINDOW_IS_MEASURED_POINTS_ONLY,
        "boundary_points_claimed": WINDOW_BOUNDARY_POINTS_CLAIMED,
        # G -- the monotonicity chain.
        "traces": dict(MONOTONICITY_TRACES),
        "cross": dict(MONOTONICITY_CROSS),
        "heavy_steps": MONOTONICITY_HEAVY_STEPS,
        "light_steps": MONOTONICITY_LIGHT_STEPS,
        "traces_exceed_two": ALL_TRACES_EXCEED_TWO,
        "heavy_increasing": HEAVY_STRICTLY_INCREASING,
        "light_decreasing": LIGHT_STRICTLY_DECREASING,
        "ratio_increasing": RATIO_STRICTLY_INCREASING_ON_GRID,
        "continuous_monotonicity": CONTINUOUS_MONOTONICITY_CLAIMED,
        # H -- the note, the fence and the nsimplify absence.
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
    }

    # --- A ----------------------------------------------------------------
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_commit"] = STALE_PARENT_COMMIT
    # --- B ----------------------------------------------------------------
    elif mutation == "claim_objects_registered":
        claims["registered"] = 1
        claims["adopted"] = 1
    elif mutation == "claim_gravity_supplied":
        claims["gravity_supplied"] = True
        claims["unsupplied"] = 0
    elif mutation == "claim_positivity_generic":
        # THE REFUTED HALF REASSERTED, AND THIS IS THE MUTATION THAT GUARDS THE
        # CHECK'S BOUNDARY HUNT: positivity is asserted to be as generic as the
        # structural legs.  It is not -- it fails at 98 of 192 searched points.
        claims["positivity_generic"] = True
    elif mutation == "claim_window_boundary_curve":
        # A CURVE ASSERTED WHERE ONLY POINTS WERE MEASURED.
        claims["window_boundary_curve"] = True
        claims["boundary_points_claimed"] = 1
    elif mutation == "claim_census_exhaustive":
        # 'GENERIC' UNSCOPED: the searched rational set asserted to be all of
        # admissible (m, c) space.
        claims["census_exhaustive"] = True
    elif mutation == "claim_physical_mass":
        claims["physical_mass"] = True
    elif mutation == "claim_transfer_operator":
        claims["transfer_operator"] = True
    elif mutation == "claim_continuum_limit":
        claims["continuum_limit"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_carrier_controls":
        claims["grid_controls"] = (0, 0, CARRIER_SIZE, (8, 8, 8, 7))
    elif mutation == "break_grid_factors":
        broken = dict(GRID_FACTORS)
        broken[("1/2", "1/3")] = ((233, -690, 233), (739, -7259, 739))
        claims["grid_factors"] = broken
    elif mutation == "break_monic_normalization":
        # THE CORRECTION DENIED: the unnormalized integer product is asserted to
        # BE the characteristic polynomial, i.e. the scalar is asserted to be 1.
        claims["grid_monic_scalars"] = {point: 1 for point in GRID}
        claims["monic_scalar_is_leading_squared"] = False
    elif mutation == "break_palindromic_square":
        claims["palindromic_square"] = False
    elif mutation == "break_grid_positivity":
        claims["grid_scale_census"] = (1, 0, 1)
    elif mutation == "break_commutant":
        claims["grid_commutator"] = 1
    # --- D ----------------------------------------------------------------
    elif mutation == "break_parity_independence":
        claims["parity_independent"] = False
    elif mutation == "break_window_cell":
        claims["window_cell_residual"] = 1
    elif mutation == "break_gram_motion":
        claims["grid_gram_motion"] = 0
    # --- E ----------------------------------------------------------------
    elif mutation == "break_boundary_shape":
        claims["boundary_shape"] = (2, 1, 1)
    elif mutation == "break_boundary_factors":
        broken = dict(BOUNDARY_FACTORS)
        broken[("1/2", "1/3")] = (1098595, -9936202, 1011692)
        claims["boundary_factors"] = broken
    elif mutation == "break_boundary_nonreciprocal":
        claims["boundary_non_reciprocal"] = False
    # --- F ----------------------------------------------------------------
    elif mutation == "break_census_frame":
        claims["census_frame"] = (len(CENSUS_MASSES), len(CENSUS_SHEARS),
                                  CENSUS_CANDIDATES, CENSUS_CANDIDATES)
    elif mutation == "break_universal_subset":
        claims["subset_universal_legs"] = SUBSET_SIZE - 1
    elif mutation == "break_subset_span":
        claims["subset_span"] = (12, 0)
    elif mutation == "break_witness":
        claims["witness_negative_discriminant"] = (
            WITNESS_NEGATIVE_DISCRIMINANT + 1)
    elif mutation == "break_failure_modes":
        # THIS BLOCK'S OWN REFINEMENT DENIED: every positivity failure is
        # asserted to be a negative reciprocal pair.  Two of the six subset
        # failures carry complex unimodular pairs instead.
        claims["all_failures_negative"] = True
        claims["failure_modes"] = {point: (1, 0, 1) for point in SUBSET_FAILING}
        claims["negative_pair_points"] = 6
        claims["complex_pair_points"] = 0
    elif mutation == "break_census_counts":
        claims["census_positive"] = CENSUS_POSITIVE + 1
    elif mutation == "break_census_columns":
        # THE COLUMN STRUCTURE FLATTENED: c = 3/4 is asserted to carry two
        # survivors rather than failing at every one of the twelve masses.
        broken = dict(CENSUS_COLUMNS)
        broken["3/4"] = (2, 10, 0)
        claims["census_columns"] = broken
    elif mutation == "break_window_measured_only":
        claims["window_measured_only"] = False
    # --- G ----------------------------------------------------------------
    elif mutation == "break_trace_table":
        broken = dict(MONOTONICITY_TRACES)
        broken["1/3"] = ((7258, 739), (691, 233))
        claims["traces"] = broken
    elif mutation == "break_cross_products":
        broken = dict(MONOTONICITY_CROSS)
        broken["1/4"] = 793365
        claims["cross"] = broken
    elif mutation == "break_adjacent_differences":
        claims["light_steps"] = tuple(
            (low, high, -numerator, denominator)
            for low, high, numerator, denominator in MONOTONICITY_LIGHT_STEPS)
    elif mutation == "break_ratio_monotonicity":
        # THE DISCRETE FENCE DROPPED: the ratio is asserted to be monotone as a
        # function of c rather than along the five measured points.
        claims["ratio_increasing"] = False
        claims["continuous_monotonicity"] = True
    # --- H ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    grid = facts.grid
    subset = facts.subset

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 193 artifacts are "
        f"content-identical at it and in the worktree, the stale pin "
        f"{STALE_PARENT_COMMIT[:12]} is a real ancestor carrying NEITHER, the "
        f"machinery import is landed, and {authority.inputs_readable} of "
        f"{len(AUDIT_INPUT_PATHS) - 1} audit inputs are readable",
        authority.parent_pin_is_commit
        and claims["parent_commit"] == PARENT_COMMIT
        and claims["stale_parent"] == STALE_PARENT_COMMIT
        and authority.parent_ref_and_ancestry
        and authority.parent_artifact_blobs
        and not authority.stale_parent_artifact_blobs
        and authority.stale_is_real_ancestor
        and authority.stale_carries_neither_artifact
        and authority.machinery_import_landed
        and authority.inputs_readable == len(AUDIT_INPUT_PATHS) - 1
        and not authority.inputs_missing)

    # --- B: THE BANNER AND THE FENCE ---------------------------------------
    checks.check(
        "B-1", f"{facts.imposed} imposed objects, {claims['registered']} "
        f"registered, {claims['adopted']} adopted",
        facts.imposed == claims["imposed"]
        and facts.registered == claims["registered"]
        and facts.adopted == claims["adopted"])
    checks.check(
        "B-2", f"NO GRAVITY IS SUPPLIED: gravity_supplied = "
        f"{claims['gravity_supplied']} and {claims['unsupplied']} gravity "
        f"structures are enumerated as NOT SUPPLIED",
        claims["gravity_supplied"] is False
        and facts.unsupplied == claims["unsupplied"])
    checks.check(
        "B-3", "POSITIVITY IS NOT GENERIC AND THIS BLOCK SAYS SO FIRST: the "
        "structural legs hold at all 192 admissible searched points and "
        "positivity fails at 98 of them, so the package SPLITS and the split "
        "is the result",
        claims["positivity_generic"] is False)
    checks.check(
        "B-4", "NO WINDOW BOUNDARY CURVE: the census is a finite set of exact "
        "rational POINTS, no edge is fitted, nothing is interpolated between "
        "points, and no point outside the searched set is asserted either way",
        claims["window_boundary_curve"] is False
        and claims["boundary_points_claimed"] == 0)
    checks.check(
        "B-5", "THE CENSUS IS NOT EXHAUSTIVE: 'generic' here is scoped to the "
        "searched rational sets M and C and to nothing wider, and a finite "
        "search is not a statement about admissible (m, c) space",
        claims["census_exhaustive"] is False)
    checks.check(
        "B-6", "NO PHYSICAL MASS: theta is a logarithm of an algebraic number "
        "attached to an exact rational matrix, 'heavy' and 'light' order two "
        "such numbers, and no particle, dispersion relation or energy is "
        "supplied",
        claims["physical_mass"] is False)
    checks.check(
        "B-7", "W IS NOT A TRANSFER OPERATOR: Block 190 refuted the naive OS "
        "transfer pairing on this class and nothing here repairs it",
        claims["transfer_operator"] is False)
    checks.check(
        "B-8", "NO CONTINUUM AND NO LIMIT: one width, one profile family, one "
        "bump and a finite grid of exact rationals",
        claims["continuum_limit"] is False)

    # --- C: THE FIVE-POINT DEEP-ODD PACKAGE --------------------------------
    inverse_residuals = {point: grid[point].inverse_residual for point in GRID}
    covariance_residuals = {point: grid[point].covariance_residual
                            for point in GRID}
    ranks = {point: grid[point].rank for point in GRID}
    gram_ranks = {point: grid[point].gram_ranks for point in GRID}
    checks.check(
        "C-1", f"the carrier closes at all {len(GRID)} grid points: "
        f"rank(Q) = {claims['grid_controls'][2]}, nnz(Q G - I) = "
        f"{claims['grid_controls'][0]}, nnz(Ps Q Ps - Q^T) = "
        f"{claims['grid_controls'][1]}, and the four core Gram ranks are "
        f"{claims['grid_controls'][3]}",
        all(ranks[point] == claims["grid_controls"][2] for point in GRID)
        and all(inverse_residuals[point] == claims["grid_controls"][0]
                for point in GRID)
        and all(covariance_residuals[point] == claims["grid_controls"][1]
                for point in GRID)
        and all(gram_ranks[point] == claims["grid_controls"][3]
                for point in GRID))
    checks.check(
        "C-2", f"at the deep odd core t0 = {DEEP_ODD_CORE} every grid point "
        f"gives EXACTLY TWO primitive palindromic integer quadratics, each of "
        f"multiplicity {claims['grid_multiplicity']}, and all five pairs are "
        f"the declared coefficient triples",
        all(tuple(coefficients for coefficients, _ in grid[point].factors)
            == tuple(sorted(claims["grid_factors"][point]))
            and all(multiplicity == claims["grid_multiplicity"]
                    and palindromic(coefficients)
                    for coefficients, multiplicity in grid[point].factors)
            for point in GRID))
    checks.check(
        "C-3", f"THE CHECK'S C1 CORRECTION, AS A FORMULA: charpoly(W) is MONIC, "
        f"so the displayed integer product equals it only after division by an "
        f"exact scalar -- the five scalars are the declared integers, each is "
        f"EXACTLY the squared product of the two leading coefficients, and the "
        f"polynomial residual is {claims['monic_residual']} at every point",
        all(grid[point].monic_scalar == claims["grid_monic_scalars"][point]
            for point in GRID)
        and all(grid[point].monic_residual == claims["monic_residual"]
                for point in GRID)
        and all(grid[point].monic_scalar_is_leading_squared
                == claims["monic_scalar_is_leading_squared"]
                for point in GRID))
    checks.check(
        "C-4", f"the monic characteristic polynomial is PALINDROMIC and is the "
        f"exact SQUARE of a degree-four palindromic polynomial at all "
        f"{len(GRID)} grid points, verified by expansion and not inferred from "
        f"the multiplicities",
        all(grid[point].charpoly_palindromic for point in GRID)
        and all(grid[point].perfect_square == claims["palindromic_square"]
                for point in GRID))
    checks.check(
        "C-5", f"positivity holds at all {len(GRID)} grid points by TWO "
        f"independent exact routes -- the per-factor discriminant/trace/"
        f"constant test and the scale census {claims['grid_scale_census']} on "
        f"q(T) -- the two routes AGREE at every point, and the two scales are "
        f"DISTINCT",
        all(grid[point].scale_census[:3] == claims["grid_scale_census"]
            for point in GRID)
        and all(grid[point].positive_by_factors == claims["grid_positive"]
                for point in GRID)
        and all((grid[point].positive_by_census
                 == grid[point].positive_by_factors) == claims["routes_agree"]
                for point in GRID)
        and all(grid[point].two_scales == claims["grid_two_scales"]
                for point in GRID))
    checks.check(
        "C-6", f"the deep monodromy COMMUTES with the momentum shift U at all "
        f"{len(GRID)} grid points: nnz([W, U]) = {claims['grid_commutator']}",
        all(grid[point].commutator_residual == claims["grid_commutator"]
            for point in GRID))

    # --- D: PARITY INDEPENDENCE AND THE WINDOW CELL ------------------------
    checks.check(
        "D-1", f"parity independence at all {len(GRID)} grid points: "
        f"charpoly(W, t0 = {DEEP_EVEN_CORE}) equals "
        f"charpoly(W, t0 = {DEEP_ODD_CORE}) exactly",
        all(grid[point].parity_equal == claims["parity_independent"]
            for point in GRID))
    checks.check(
        "D-2", f"the window-law cell closes at all {len(GRID)} grid points: "
        f"the {BUMP_ANCHORS} bump at v = {BUMP_VOLUME} leaves the "
        f"t0 = {WINDOW_CORE} monodromy MATRIX-EXACTLY unchanged, residual "
        f"{claims['window_cell_residual']}",
        all(grid[point].window_residual == claims["window_cell_residual"]
            for point in GRID))
    checks.check(
        "D-3", f"and that invariance is a NONTRIVIAL quotient cancellation: "
        f"the core Gram K_c itself moves in {claims['grid_gram_motion']} of "
        f"{CORE_SIZE * CORE_SIZE} entries at every grid point",
        all(grid[point].gram_motion == claims["grid_gram_motion"]
            for point in GRID))

    # --- E: THE BOUNDARY-LAYER GENERICITY ----------------------------------
    checks.check(
        "E-1", f"at the far boundary-layer core t0 = {BOUNDARY_CORE} the "
        f"factorization has shape (heavy)^{claims['boundary_shape'][0]} "
        f"(light)^{claims['boundary_shape'][1]} "
        f"(boundary)^{claims['boundary_shape'][2]} at all {len(GRID)} grid "
        f"points",
        all(grid[point].boundary_shape == claims["boundary_shape"]
            for point in GRID))
    checks.check(
        "E-2", f"the five boundary quadratics are the declared integer "
        f"triples, digit for digit",
        all(grid[point].boundary_factor == claims["boundary_factors"][point]
            for point in GRID))
    checks.check(
        "E-3", f"every boundary quadratic is NON-RECIPROCAL -- leading and "
        f"constant differ, so its roots are not a reciprocal pair -- and each "
        f"has a strictly positive discriminant",
        all(non_reciprocal(grid[point].boundary_factor)
            == claims["boundary_non_reciprocal"] for point in GRID))

    # --- F: THE SPLIT ------------------------------------------------------
    universal_legs = sum(
        1 for point in CENSUS_SUBSET
        if subset[point].charpoly_palindromic
        and subset[point].perfect_square
        and subset[point].commutator_residual == 0
        and subset[point].parity_equal
        and subset[point].window_residual == 0)
    measured_positive = tuple(
        point for point in CENSUS_SUBSET if subset[point].positive_by_census)
    measured_failing = tuple(
        point for point in CENSUS_SUBSET
        if not subset[point].positive_by_census)
    witness = subset[WITNESS_POINT]
    negative_points = tuple(
        point for point in measured_failing
        if subset[point].scale_census[2] > 0)
    complex_points = tuple(
        point for point in measured_failing
        if subset[point].scale_census[2] == 0
        and subset[point].scale_census[1] > 0)
    checks.check(
        "F-1", f"the census frame is {claims['census_frame'][0]} masses by "
        f"{claims['census_frame'][1]} shears = {claims['census_frame'][2]} "
        f"candidates, and the {claims['census_singular_points']} with "
        f"c = {CENSUS_SINGULAR_SHEAR} are excluded because baseline Q is "
        f"EXACTLY SINGULAR there -- RE-MEASURED at both ends of M, ranks "
        f"{sorted(facts.singular_ranks.values())} against {CARRIER_SIZE} -- "
        f"leaving {claims['census_frame'][3]} admissible",
        facts.census_frame == claims["census_frame"]
        and len(CENSUS_MASSES) == claims["census_singular_points"]
        and bool(facts.singular_ranks)
        and all(rank < CARRIER_SIZE
                for rank in facts.singular_ranks.values()))
    checks.check(
        "F-2", f"THE UNIVERSAL HALF OF THE SPLIT, RE-MEASURED: palindromicity, "
        f"the perfect-square form, [W, U] = 0, parity independence and the "
        f"{BUMP_ANCHORS} window cell all hold at "
        f"{claims['subset_universal_legs']} of {SUBSET_SIZE} subset points, "
        f"including at every point where positivity FAILS",
        universal_legs == claims["subset_universal_legs"]
        and universal_legs == SUBSET_SIZE
        and all(subset[point].gram_motion
                == claims["subset_gram_motion"].get(
                    point, SUBSET_GRAM_MOTION_DEFAULT)
                for point in CENSUS_SUBSET))
    checks.check(
        "F-3", f"THE WINDOWED HALF, RE-MEASURED: the twelve-point subset SPANS "
        f"the split exactly {claims['subset_span'][0]} positive to "
        f"{claims['subset_span'][1]} failing, and both lists are the declared "
        f"points",
        (len(measured_positive), len(measured_failing)) == claims["subset_span"]
        and measured_positive == claims["subset_positive"]
        and measured_failing == claims["subset_failing"])
    checks.check(
        "F-4", f"THE EXACT WITNESS {WITNESS_POINT}: the two primitive factors "
        f"are the declared triples over the monic scalar "
        f"{claims['witness_monic_scalar']}; the failing factor has "
        f"discriminant {claims['witness_negative_discriminant']} > 0, root "
        f"product exactly {WITNESS_ROOT_PRODUCT} and root sum strictly "
        f"NEGATIVE, so its two roots are real, reciprocal and both negative; "
        f"and the surviving factor has discriminant "
        f"{claims['witness_positive_discriminant']} > 0 with a positive "
        f"reciprocal pair",
        tuple(coefficients for coefficients, _ in witness.factors)
        == tuple(sorted(claims["witness_factors"]))
        and witness.monic_scalar == claims["witness_monic_scalar"]
        and (WITNESS_NEGATIVE_FACTOR[1] ** 2
             - 4 * WITNESS_NEGATIVE_FACTOR[0] * WITNESS_NEGATIVE_FACTOR[2]
             == claims["witness_negative_discriminant"])
        and (WITNESS_POSITIVE_FACTOR[1] ** 2
             - 4 * WITNESS_POSITIVE_FACTOR[0] * WITNESS_POSITIVE_FACTOR[2]
             == claims["witness_positive_discriminant"])
        and WITNESS_NEGATIVE_FACTOR[2] == WITNESS_NEGATIVE_FACTOR[0]
        and (factor_trace(WITNESS_NEGATIVE_FACTOR) < 0)
        == WITNESS_ROOT_SUM_NEGATIVE
        and factor_trace(WITNESS_NEGATIVE_FACTOR) < -2
        and factor_trace(WITNESS_POSITIVE_FACTOR) > 2
        and witness.scale_census[:3] == claims["failure_modes"][WITNESS_POINT])
    checks.check(
        "F-5", f"AND THE FAILURE SET IS NOT ONE MODE: the scale census "
        f"separates {claims['negative_pair_points']} subset failures carrying "
        f"a NEGATIVE real reciprocal pair from {claims['complex_pair_points']} "
        f"carrying COMPLEX unimodular pairs and NO negative pair at all, so "
        f"'every failure is a negative pair' is "
        f"{claims['all_failures_negative']}; and the two modes are separated "
        f"by the HODGE EDGE det g(c) = 1 - c^2, every subset point with c > 1 "
        f"failing in the complex mode and every negative-pair failure sitting "
        f"at |c| < 1",
        all(subset[point].scale_census[:3] == claims["failure_modes"][point]
            for point in SUBSET_FAILING)
        and len(negative_points) == claims["negative_pair_points"]
        and len(complex_points) == claims["complex_pair_points"]
        and (len(complex_points) == 0) == claims["all_failures_negative"]
        and (all(rat(point[1]) > 1 for point in complex_points)
             and all(abs(rat(point[1])) < 1 for point in negative_points)
             and all(abs(rat(point[1])) < 1 for point in measured_positive))
        == claims["hodge_edge_separates"])
    checks.check(
        "F-6", f"THE FULL CENSUS IS CITED, NOT RE-RUN: {claims['census_universal']} "
        f"of {claims['census_frame'][3]} admissible points carry the universal "
        f"legs and {claims['census_positive']} carry positivity against "
        f"{claims['census_failures']} that do not -- the two halves total the "
        f"admissible count exactly, and this runner gates the {SUBSET_SIZE}-"
        f"point subset above rather than the full sweep",
        claims["census_universal"] == claims["census_frame"][3]
        and claims["census_positive"] + claims["census_failures"]
        == claims["census_frame"][3]
        and claims["census_failures"] > 0
        and len(CENSUS_SUBSET) == SUBSET_SIZE)
    checks.check(
        "F-7", f"MEASURED-ONLY DISCIPLINE ON THE WINDOW: "
        f"{claims['window_measured_only']} -- the positivity window is "
        f"reported as the {SUBSET_SIZE} re-measured points plus the cited "
        f"census and nothing else, with no fitted edge, no interpolation "
        f"between points and no extrapolation off the searched set",
        claims["window_measured_only"] is True)
    subset_columns = {}
    for point in CENSUS_SUBSET:
        census = subset[point].scale_census[:3]
        slot = 0 if census == (2, 0, 0) else (1 if census[2] > 0 else 2)
        subset_columns.setdefault(point[1], [0, 0, 0])[slot] += 1
    checks.check(
        "F-8", f"THE CITED COLUMN TABLE, AND ITS TWO WHOLE-COLUMN FACTS: the "
        f"{len(claims['census_columns'])} admissible shear columns each carry "
        f"{len(CENSUS_MASSES)} searched masses and total "
        f"({claims['census_positive']}, {claims['census_negative_total']}, "
        f"{claims['census_complex_total']}); the four columns "
        f"{MASS_UNIFORM_NEGATIVE_COLUMNS} fail at EVERY searched mass by a "
        f"NEGATIVE pair, which extends the check's single c = 3/4 observation "
        f"to four columns; the three columns {BEYOND_EDGE_COLUMNS} beyond the "
        f"Hodge edge fail at every searched mass by the COMPLEX mode; and "
        f"every subset point agrees with its own column's mode",
        all(sum(entry) == len(CENSUS_MASSES)
            for entry in claims["census_columns"].values())
        and sum(entry[0] for entry in claims["census_columns"].values())
        == claims["census_positive"]
        and sum(entry[1] for entry in claims["census_columns"].values())
        == claims["census_negative_total"]
        and sum(entry[2] for entry in claims["census_columns"].values())
        == claims["census_complex_total"]
        and claims["census_negative_total"] + claims["census_complex_total"]
        == claims["census_failures"]
        and all(claims["census_columns"][column]
                == (0, len(CENSUS_MASSES), 0)
                for column in MASS_UNIFORM_NEGATIVE_COLUMNS)
        and all(claims["census_columns"][column]
                == (0, 0, len(CENSUS_MASSES))
                for column in BEYOND_EDGE_COLUMNS)
        and all(all(measured == 0 or claims["census_columns"][column][slot] > 0
                    for slot, measured in enumerate(counts))
                for column, counts in subset_columns.items()))

    # --- G: THE MONOTONICITY CHAIN -----------------------------------------
    measured_traces = {
        shear: tuple((trace.p, trace.q)
                     for trace in facts.monotonicity[shear].traces)
        for shear in MONOTONICITY_SHEARS}
    checks.check(
        "G-1", f"at fixed m = {MONOTONICITY_MASS} over c in "
        f"{MONOTONICITY_SHEARS} the exact traces T = 2 cosh(theta) = -b/a are "
        f"the declared (heavy, light) pairs, and every one of the ten exceeds "
        f"2 so acosh(T/2) is real and strictly positive",
        all(measured_traces[shear] == claims["traces"][shear]
            for shear in MONOTONICITY_SHEARS)
        and facts.traces_exceed_two == claims["traces_exceed_two"])
    checks.check(
        "G-2", f"T_heavy > T_light at every grid point, certified by the exact "
        f"integer cross-products {tuple(claims['cross'][s] for s in MONOTONICITY_SHEARS)}, "
        f"all strictly positive",
        all(facts.monotonicity_cross[shear] == claims["cross"][shear]
            for shear in MONOTONICITY_SHEARS)
        and all(value > 0 for value in claims["cross"].values()))
    checks.check(
        "G-3", f"the four adjacent exact differences are the declared "
        f"rationals: T_heavy strictly INCREASES and T_light strictly DECREASES "
        f"at every step of the chain",
        all(facts.heavy_steps[(low, high)] == sp.Rational(numerator,
                                                          denominator)
            for low, high, numerator, denominator in claims["heavy_steps"])
        and all(facts.light_steps[(low, high)] == sp.Rational(numerator,
                                                              denominator)
                for low, high, numerator, denominator in claims["light_steps"])
        and facts.heavy_increasing == claims["heavy_increasing"]
        and facts.light_decreasing == claims["light_decreasing"])
    checks.check(
        "G-4", f"THEREFORE theta_heavy / theta_light is strictly increasing ON "
        f"THIS FIVE-POINT DISCRETE GRID -- acosh(T/2) is positive and strictly "
        f"increasing for T > 2, theta_heavy rises and theta_light falls, and "
        f"both stay positive -- and continuous monotonicity between grid "
        f"points is {claims['continuous_monotonicity']}",
        claims["ratio_increasing"] is True
        and facts.heavy_increasing and facts.light_decreasing
        and facts.traces_exceed_two
        and claims["continuous_monotonicity"] is False)

    # --- H: THE NOTE, THE FENCE AND THE NSIMPLIFY ABSENCE ------------------
    checks.check(
        "H-1", f"the note is present at {NOTE_PATH.name} and the N5 fence is "
        f"byte-identical there and in this runner",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "H-2", f"sp.nsimplify appears {facts.nsimplify_calls} times in this "
        f"runner's own source, MEASURED and not promised -- the hazard is a "
        f"rational TOLERANCE that maps a small nonzero rational to exactly "
        f"zero, which on a sign census whose thinnest gated margin is "
        f"T - 2 = 6009601/260073505000 at (1/100, -99/100) would flip a "
        f"passing sign test either way",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED")
    print(f"  elapsed: {elapsed_ns / 1e9:.1f}s")
    print(f"  origin/main {facts.main_head}")
    print(f"  authority {facts.authority}")
    print(f"  imposed {facts.imposed}, registered {facts.registered}, "
          f"adopted {facts.adopted}, gravity structures NOT SUPPLIED "
          f"{facts.unsupplied}")
    print(f"  check verdict carried: {CHECK_VERDICT}")
    print(f"  exact 64x64 inverses built and shared: {facts.inverse_count}")
    print("  THE FIVE-POINT GRID")
    for point in GRID:
        item = facts.grid[point]
        print(f"    (m, c) = ({point[0]}, {point[1]})")
        print(f"      rank(Q) {item.rank}, nnz(QG-I) {item.inverse_residual}, "
              f"nnz(PsQPs-Q^T) {item.covariance_residual}, Gram ranks "
              f"{item.gram_ranks}")
        print(f"      t0=3 factors {item.factors}")
        print(f"      monic scalar {item.monic_scalar} "
              f"(= (a1 a2)^2: {item.monic_scalar_is_leading_squared}), "
              f"residual {item.monic_residual}")
        print(f"      palindromic {item.charpoly_palindromic}, perfect square "
              f"{item.perfect_square}, scale census {item.scale_census[:3]}, "
              f"two scales {item.two_scales}")
        print(f"      positive by census {item.positive_by_census}, by factors "
              f"{item.positive_by_factors}, traces {item.traces}")
        print(f"      nnz([W,U]) {item.commutator_residual}, parity equal "
              f"{item.parity_equal}")
        print(f"      window cell residual {item.window_residual}, core Gram "
              f"motion {item.gram_motion}")
        print(f"      t0=4 shape {item.boundary_shape}, boundary factor "
              f"{item.boundary_factor}")
    print("  THE CENSUS SUBSET, RE-MEASURED")
    print(f"    c = {CENSUS_SINGULAR_SHEAR} baseline ranks (singular): "
          f"{facts.singular_ranks}")
    for point in CENSUS_SUBSET:
        item = facts.subset[point]
        verdict = "POSITIVE" if item.positive_by_census else "FAILS POSITIVITY"
        print(f"    ({point[0]}, {point[1]}): {verdict}; census "
              f"{item.scale_census[:3]}; palindromic "
              f"{item.charpoly_palindromic}; square {item.perfect_square}; "
              f"[W,U] {item.commutator_residual}; parity {item.parity_equal}; "
              f"window {item.window_residual}; Gram motion {item.gram_motion}")
        print(f"        factors {item.factors} over {item.monic_scalar}")
    print(f"    CITED, NOT RE-RUN: {CENSUS_UNIVERSAL}/{CENSUS_ADMISSIBLE} "
          f"universal, {CENSUS_POSITIVE}/{CENSUS_ADMISSIBLE} positive, "
          f"{CENSUS_POSITIVITY_FAILURES}/{CENSUS_ADMISSIBLE} failing")
    print(f"  THE MONOTONICITY CHAIN at m = {MONOTONICITY_MASS}")
    for shear in MONOTONICITY_SHEARS:
        item = facts.monotonicity[shear]
        print(f"    c = {shear}: traces {item.traces}, cross "
              f"{facts.monotonicity_cross[shear]}")
    print(f"    heavy steps {facts.heavy_steps}")
    print(f"    light steps {facts.light_steps}")
    print(f"    heavy increasing {facts.heavy_increasing}, light decreasing "
          f"{facts.light_decreasing}, all traces > 2 "
          f"{facts.traces_exceed_two}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}")
    print("  NOT CLAIMED: NO GRAVITY. POSITIVITY IS NOT GENERIC. NO WINDOW "
          "BOUNDARY CURVE. THE CENSUS IS NOT EXHAUSTIVE. NO PHYSICAL MASS. "
          "W IS NOT A TRANSFER OPERATOR. NO CONTINUUM. A FIVE-POINT GRID AND "
          "A 192-POINT RATIONAL SEARCH ARE NOT A PARAMETER SPACE.")
    print()


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE GENERALITY LANGUAGE IS FENCED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- BLOCK 190's WRAP-EDGE WIDTH FAMILY AT T = 16 WITH ITS MASS/SHEAR PAIR (m, c) PROMOTED FROM A FIXTURE TO A VARIABLE (the staggered Dirac-Kahler carrier on Z_16 x Z_4 with eta_t = 1, eta_x = (-1)^t and the temporal sign w = -1 ON THE WRAP EDGE t = T-1, the grade-raising d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t with fixed slices {0, 8}, the raising set A_s in the CLOSED half {0..8} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H), THE FIVE-POINT GRID of the control (9/20, 5/13), Block 188's two known-positive fixtures (1, 5/13) and (9/20, 3/5) and the two FRESH points (1/2, 1/3) and (2/3, 1/5), THE ADVERSARIAL CHECK's SEARCHED RATIONAL SET M x C of 204 candidates imposed as a CENSUS FRAME AND NOT AS A DOMAIN, THE TWELVE-POINT RE-MEASURED SUBSET chosen to span the split, BLOCK 191's UNIT VOLUME PROFILE AND ITS {2, 3} BUMP AT v = 4/5, THE PAIR CORES with K_c[a,b] = G[idx(t_b,x_b), idx(theta_s t_a, x_a)] and L_k[a,b] = G[idx(t_b+k,x_b), idx(theta_s t_a, x_a)] on G = Q^-1, THE UNIT-CELL MONODROMY W = K_c^-1 L_2 with its momentum shift U, and the LANDED Block 105 shear_hodge(c, v) read through the Block 128 module AT A VARYING RATIONAL SHEAR -- THE ONLY OBJECT IMPORTED -- are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit, NO quotient and NO Osterwalder-Schrader reconstruction that would make W a physical transfer operator. WHAT IS ESTABLISHED IS NARROWER AND IS SAID IN THOSE WORDS: WITHIN THIS IMPOSED FINITE MATRIX CONSTRUCTION, THE TRANSFER PACKAGE SPLITS -- ITS STRUCTURAL LEGS HOLD AT EVERY ADMISSIBLE POINT OF A 192-POINT RATIONAL SEARCH AND ITS POSITIVITY LEG FAILS AT 98 OF THEM. 'MASS', 'SCALE', 'HEAVY', 'LIGHT', 'POSITIVITY', 'WINDOW' AND 'GENERIC' NAME PROPERTIES OF EXACT RATIONAL MATRICES: 'scale' NAMES a root T = z + 1/z of a rational quadratic, 'theta' NAMES acosh(T/2) for T > 2 and therefore a LOGARITHM OF AN ALGEBRAIC NUMBER, 'heavy' and 'light' ORDER two such numbers, 'positivity' NAMES the statement that eight roots of one rational polynomial are real and positive, and 'generic' NAMES a count over a FINITE SEARCHED SET. NO PHYSICAL MASS IS SUPPLIED AND NO DISPERSION RELATION IS SUPPLIED. NO WINDOW BOUNDARY CURVE IS SUPPLIED: the census is a FINITE SET OF EXACT RATIONAL POINTS, no edge is fitted, nothing is interpolated between points and no point outside the searched set is asserted either way. THE CENSUS IS NOT EXHAUSTIVE AND 'GENERIC' IS SCOPED TO M AND C AND TO NOTHING WIDER. NO CONTINUUM. TEN GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient, OS reconstruction of a transfer operator. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE FIVE-POINT DEEP-ODD PACKAGE IS EXACT AT EVERY POINT, AND THE CHECK'S C1 CORRECTION IS CARRIED AS A FORMULA RATHER THAN AS A HEDGE. At the deep odd core t0 = 3 each of the five grid points gives charpoly(W) with EXACTLY TWO primitive palindromic integer quadratics, each of MULTIPLICITY TWO: (22569375 z^2 - 233631106 z + 22569375) and (39529825 z^2 - 109432706 z + 39529825) at the control; (26527, -444930) and (51097, -289682) at (1, 5/13); (12475, -273738) and (53125, -142538) at (9/20, 3/5); (233 z^2 - 690 z + 233) and (739 z^2 - 7258 z + 739) at (1/2, 1/3); and (17099 z^2 - 159050 z + 17099) and (21709 z^2 - 81434 z + 21709) at (2/3, 1/5). THE POLYNOMIAL SymPy RETURNS IS MONIC, SO THOSE DISPLAYED INTEGER PRODUCTS ARE THE CHARACTERISTIC POLYNOMIAL ONLY AFTER DIVISION BY AN EXACT SCALAR, AND THE SCALAR IS EXACTLY THE SQUARED PRODUCT OF THE TWO LEADING COEFFICIENTS: 795955611005101889386962890625, 1837245025097114161, 439216851806640625, 29648362969 and 137791066603200481, each gated at ZERO polynomial residual. THE CARRIER CLOSES AT EVERY POINT: rank(Q) = 64, nnz(Q G - I) = 0, nnz(Ps Q Ps - Q^T) = 0 and all four core Gram ranks are 8. THE SPECTRAL FORM IS GATED TWICE OVER: the monic charpoly is PALINDROMIC and is the EXACT SQUARE of a degree-four palindromic polynomial p(z) = z^4 + alpha z^3 + beta z^2 + alpha z + 1 verified by expansion and NOT inferred from the multiplicities, and positivity is established by TWO INDEPENDENT EXACT ROUTES that AGREE at every point -- a per-factor discriminant/trace/constant test, and a SCALE CENSUS on the trace polynomial q(T) = T^2 + alpha T + (beta - 2) that counts roots above 2, inside (-2, 2) and below -2 from the signs of q(2), q(-2) and the vertex, WITH NO RADICAL EVER EVALUATED. THE HAZARD INHERITED FROM BLOCK 186 IS HONOURED BY ABSENCE AND MEASURED RATHER THAN PROMISED: the nsimplify call carries a rational TOLERANCE and maps a small nonzero rational to EXACTLY ZERO, and this block's margins are as thin as T - 2 = 6009601/260073505000 at the census point (1/100, -99/100), which is INSIDE the gated subset and is POSITIVE, so a single such call could manufacture or destroy positivity; this runner calls it ZERO TIMES, counted in its own source by gate H.\\nper_mode: PARITY INDEPENDENCE, THE WINDOW CELL AND THE BOUNDARY LAYER ARE ALL (m, c)-GENERIC ON THE GRID. At all five points charpoly(W, t0 = 2) equals charpoly(W, t0 = 3) EXACTLY, which is the TRUE parity test; and the {2, 3} volume bump at v = 4/5 leaves the t0 = 5 monodromy MATRIX-EXACTLY unchanged at residual 0 while the core Gram K_c itself moves in 64 of its 64 entries, so the window-cell invariance is a NONTRIVIAL QUOTIENT CANCELLATION and not a trivial identity. THE SOLVE'S OWN t0 = 4 LEG WAS MIS-AIMED AND THE MIS-AIM IS CARRIED AS A CORRECTION: at T = 16 the core t0 = 4 = T/2 - 4 is a FAR BOUNDARY-LAYER core and NOT the even-deep representative -- that is t0 = 2 -- so the parityW comparisons the solve read at t0 = 4 compared deep against boundary and were MEANINGLESS AS PARITY TESTS. What t0 = 4 does carry is Block 191's BOUNDARY-MODE STRUCTURE, and that structure REPLICATES AT ALL FIVE POINTS: the factorization is (heavy)^1 (light)^2 (boundary)^1 with exactly one NEW quadratic of multiplicity one, and that quadratic is NON-RECIPROCAL -- leading and constant differ -- with a strictly positive discriminant, at (9/20, 5/13), (1, 5/13), (9/20, 3/5), (1/2, 1/3) and (2/3, 1/5) alike.\\nper_block: THE SPLIT, AND IT IS THE BLOCK. The adversarial check searched the full Cartesian set M = {1/100, 1/50, 1/20, 1/10, 1/5, 1/3, 1/2, 2/3, 1, 2, 5, 10} against C = {-99/100, -9/10, -3/4, -1/2, -1/5, 0, 1/5, 1/3, 1/2, 3/4, 9/10, 19/20, 99/100, 101/100, 6/5, 3/2, 2} -- 204 exact rational candidates. THE TWELVE WITH c = 2 ARE EXCLUDED BECAUSE BASELINE Q IS EXACTLY SINGULAR THERE, RE-MEASURED HERE AT BOTH ENDS OF M AT RANK 62 OF 64, leaving 192 admissible. ON THOSE 192: palindromicity, the perfect-square form, [W, U] = 0, parity independence and the {2, 3} window cell hold at 192 OF 192 WITH ZERO EXCEPTIONS, while POSITIVITY HOLDS AT ONLY 94 AND FAILS AT 98. THE STRUCTURAL LEGS ARE UNIVERSAL ON THE SEARCHED SET AND POSITIVITY IS NOT, AND THAT IS THE THEOREM. THE RUNNER GATES A TWELVE-POINT SUBSET RE-MEASURED IN FULL -- SIX POSITIVE AND SIX FAILING, spanning both fresh fixtures, both signs of c, both extremes of m, the zero-shear point and three points beyond the Hodge edge -- AND CITES THE FULL 192-POINT CENSUS, WHICH IS MEASURED OFFLINE AND IS NOT RE-RUN BY THE RUNNER; that citation boundary is stated here so no reader mistakes a cited count for a gated one. THE EXACT WITNESS IS (m, c) = (1/100, 3/4), where charpoly(W) = (57536 z^2 + 5175457 z + 57536)^2 (1322536 z^2 - 2645457 z + 1322536)^2 / 5790210286399072239616: the first factor has discriminant 26772113593665 > 0, root product exactly 1 and root sum -5175457/57536 < 0, so its two roots are real, reciprocal and BOTH STRICTLY NEGATIVE, while the second retains a positive reciprocal pair with discriminant 2036853665.\\nlattice_wide: THE FAILURE SET IS NOT ONE MODE, AND THE HODGE EDGE SEPARATES THE TWO. The adversarial check reported its positivity failures as NEGATIVE reciprocal pairs. Measured here, the failing set contains a SECOND MODE the check did not separate: at (5, 101/100) and (1/10, 3/2) the failing pairs are COMPLEX AND UNIMODULAR, carrying NO negative pair at all, and the scale census distinguishes the modes exactly -- (2,0,0) positive, (1,0,1) one negative real pair, (1,1,0) one complex pair, (0,2,0) both pairs complex. THE SEPARATION IS THE HODGE EDGE ITSELF: the displayed shear metric is g(c) = [[1, c], [c, 1]] with det g = 1 - c^2, so |c| > 1 is exactly where g is INDEFINITE, and on the searched set EVERY point with c > 1 fails in the COMPLEX mode while EVERY negative-pair failure and EVERY positive point sits at |c| < 1. THE CITED COLUMN TABLE MAKES IT ARITHMETIC: over the sixteen admissible shear columns at twelve searched masses each, (positive, negative-pair, complex-pair) is (9,3,0) at c = -99/100, (10,2,0) at -9/10, -3/4 and -1/2, (12,0,0) at -1/5 and 0, (11,1,0) at 1/5, (10,2,0) at 1/3 and 1/2, (0,12,0) at 3/4, 9/10, 19/20 and 99/100, and (0,0,12) at 101/100, 6/5 and 3/2 -- totalling 94, 62 and 36. TWO WHOLE-COLUMN FACTS FOLLOW AND BOTH ARE COUNTS OVER A FINITE SEARCH AND NOTHING MORE: the FOUR columns c = 3/4, 9/10, 19/20 and 99/100 fail at EVERY ONE of the twelve searched masses by a negative pair, which EXTENDS the check's single c = 3/4 observation to four columns; and the THREE columns beyond the Hodge edge fail at every searched mass by the complex mode. NO CURVE IS FITTED THROUGH THESE COLUMNS AND NO POINT BETWEEN THEM IS ASSERTED EITHER WAY.\\nper_scope: THE MONOTONICITY CHAIN IS EXACT, DISCRETE AND FENCED AS DISCRETE. At fixed m = 1/2 over c in {1/5, 1/4, 1/3, 2/5, 9/20} the exact traces T = 2 cosh(theta) = -b/a are T_heavy = 63258/7619, 6223/709, 7258/739, 12922/1171 and 3084847/250021 against T_light = 28762/9629, 575/193, 690/233, 6298/2141 and 1534683/525061. Every one of the ten exceeds 2, so acosh(T/2) is real and strictly positive at every point; T_heavy > T_light is certified by the exact integer cross-products 389973604, 793364, 1181204, 20291044 and 1236029872324, all strictly positive; and the four adjacent differences are 2563115/5401871, 547125/523951, 1050240/865369 and 381584475/292774591 for the heavy trace against -14391/1858397, -805/44969, -9856/498853 and -21077875/1124155601 for the light one. SINCE acosh(T/2) IS POSITIVE AND STRICTLY INCREASING FOR T > 2, theta_heavy STRICTLY INCREASES AND theta_light STRICTLY DECREASES ALONG THE CHAIN AND BOTH STAY POSITIVE, SO theta_heavy / theta_light STRICTLY INCREASES -- ON THIS FIVE-POINT DISCRETE GRID AND NOWHERE ELSE. THIS IS NOT A THEOREM OF CONTINUOUS MONOTONICITY BETWEEN GRID POINTS, IT IS NOT A DISPERSION RELATION, AND IT IS NOT A STATEMENT ABOUT ANY MASS RATIO IN NATURE. WHAT REMAINS OPEN IS NAMED: WHY the structural legs are universal is NOT derived -- they are COUNTED over a finite search and no proof from the staggered recurrence is offered; the positivity window's boundary is NOT located, because a finite set of points cannot locate one; and the coincidence between the Hodge edge |c| = 1 and the complex-mode boundary is MEASURED at the searched columns and NOT proved.\\nRESULT: THE TRANSFER PACKAGE OF BLOCKS 190 TO 193 SPLITS UNDER VARIATION OF (m, c): ITS STRUCTURAL LEGS -- Ps-COVARIANCE, PALINDROMICITY, THE PERFECT-SQUARE FORM, [W, U] = 0, PARITY INDEPENDENCE AND THE WINDOW-CELL INVARIANCE -- HOLD AT ALL 192 ADMISSIBLE POINTS OF THE SEARCHED RATIONAL SET WITH ZERO EXCEPTIONS, WHILE ITS POSITIVITY LEG FAILS AT 98 OF THEM IN TWO EXACTLY SEPARATED MODES DIVIDED BY THE HODGE EDGE -- AND NOT ONE LINE OF IT IS A MASS SPECTRUM, A DISPERSION RELATION, A TRANSFER OPERATOR, A BOUNDARY CURVE IN THE (m, c) PLANE OR A CONTINUUM LIMIT. The five-point deep-odd package, the parity independence, the window cell and Block 191's boundary-mode structure are exact at every grid point; the check's C1 monic-normalization correction is carried as a FORMULA with the scalar identified as the squared product of the leading coefficients; the check's positivity witness is reproduced digit for digit; the check's single-column c = 3/4 observation is extended to four whole columns; a SECOND failure mode the check did not separate is exhibited and located at the Hodge edge; and the theta-ratio monotonicity is proved exactly and fenced as discrete. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128 and 181-193 STAND EXACTLY AS LANDED. BLOCK 193 IS NOT CORRECTED: its parity-resolved window law is carried here unchanged as the source of this block's window-cell leg, and the {2, 3} cell at t0 = 5 is gated as an INSTANCE of it at five new (m, c) points. THIS BLOCK'S OWN DEFECTS ARE DISCLOSED: ONE width, ONE profile family, ONE bump, a FIVE-POINT grid and a 192-POINT rational search -- a finite search is not a parameter space; the runner GATES twelve points and CITES the other 180, so the full-census counts are CITATIONS and not gated measurements; the universality of the structural legs is COUNTED and not DERIVED; the positivity window's boundary is NOT located and no curve is fitted; and the coincidence of the complex-mode boundary with the Hodge edge |c| = 1 is MEASURED at the searched columns and NOT proved. SIX ITEMS ARE FOLDED FROM THE ADVERSARIAL CHECK AS CONTENT AND NOT AS ERRATA: the C1 MONIC-NORMALIZATION correction, carried as a formula with its scalar identified; the C2, C3 and C4 CONFIRMATIONS at both fresh points, extended here to all five; the P1 EXTREME-POINT failures, folded as the first half of the split; the P2 BOUNDARY HUNT and its 192-point census, folded as the block's centre; the P2 WARNING that irreducible-factor degree alone is not a valid positivity checker, which is why this block gates the perfect-square form and the scale census instead; and the P3 MONOTONICITY chain, reproduced exactly and fenced as discrete. PROVENANCE: CAMPAIGN_20260824_GRAVITY_MAINLINE.md, at its THE (m,c) GENERALITY SOLVE (block 194 candidate), GEN PHASE 1 MEASURED, GEN PHASE 2 MEASURED and B194 CHECK VERDICT anchors.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
