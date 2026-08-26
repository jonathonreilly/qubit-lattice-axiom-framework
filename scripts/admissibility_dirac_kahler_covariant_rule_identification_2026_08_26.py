#!/usr/bin/env python3
"""BLOCK 201 -- FINITE COVARIANT-ENCODING EXHIBITS AND SELECTION BOUNDARIES.

This runner preserves four exact calculations while separating them from a
physical-rule identification that the available premises do not select:

* the chosen pair A=sx, B=-sz spin-diagonalises the finite Z_6 x Z_4 kernel at
  four twists, with a twelve-verdict dictionary measured on Z_6 x Z_4 only;
* after a target 4 x 4 scalar form is declared, the sixteen-word cell ansatz
  has a unique preimage at every anchor parity.  Two unrelated replacement
  targets have the same rank certificate, so this is encodability, not target
  selection;
* a real Cl(3,0) triple has no 2 x 2 or odd-dimensional representation and an
  exact 4 x 4 exhibit carries all 24 proper cubic rotations;
* Block 171's independent finite bench satisfies exact Schur and support
  identities.  No equation here identifies its Q with the chosen matrix pair.

The six ordered generator pairs in the declared census all reproduce the lane
signs.  Consequently neither that census, the target-preimage rank, nor the
imported Schur identity chooses a unique covariant rule.  All positive results
are finite or algebraic proposal-grade evidence; nothing is registered,
adopted, or asserted as a continuum or Nature-level result.

There are thirty-four claim-only mutations.  Each must fail exactly its mapped
gate after all exact measurements have been made once.
"""

from __future__ import annotations

import argparse
import ast
import itertools
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import sympy as sp
from sympy import QQ
from sympy.polys.domains import QQ_I
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED, AND THEY ARE EXACTLY TWO OBJECTS: the Block 105
# shear_hodge() re-exported by the Block 128 module, read here at UNIT VOLUME;
# and Block 171's committed bench, read through ITS OWN Site and Env classes so
# that the landed W9 profile is the landed one and not a rebuild of it.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    HODGE_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    HODGE_IMPORT_LANDED = False
try:
    import admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21 as b171
    BENCH_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b171 = None
    BENCH_IMPORT_LANDED = False
MACHINERY_IMPORT_LANDED = HODGE_IMPORT_LANDED and BENCH_IMPORT_LANDED

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 200 is the commit this block's
# branch is cut from; its note and its runner both exist at PARENT_COMMIT and
# NEITHER exists at STALE_PARENT_COMMIT, which is the Block 199 tip.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_"
    "BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_transfer_robustness_boundary_package_"
    "2026_08_26.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "50f3f6658e82ea81c1e958d50ce1d12c29c74ef1",
    "f05266ad469a44758e2bc11d5c17d7101d7e0463",
)
# THE CONSTRUCTION AUTHORITY.  Block 171 supplies the committed 12x4 bench and
# the landed W9 profile this block identifies; Block 190 supplies the lane
# kernel conventions and the seam/wrap fork; Block 105 supplies the imported
# shear Hodge, read through the Block 128 module.
BLOCK171_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_"
    "THEOREM_NOTE_2026-08-21.md"
)
BLOCK171_RUNNER = (
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py"
)
BLOCK105_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_"
    "HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_ROBUSTNESS_BOUNDARY_PACKAGE_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_transfer_robustness_boundary_package_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERATOR_TRILEMMA_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md",
    "scripts/admissibility_dirac_kahler_generator_trilemma_kernel_2026_08_21.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  RE-RESOLVED LIVE AT DRAFT TIME against the REMOTE origin/main
# of the real repository -- never against a local main ref, which sits behind it.
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block200-"
              "transfer-robustness-boundary-package-20260826")
PARENT_COMMIT = "4a21fefcce3f161dca9e13b64212add7db003349"
# The repaired Block 199 tip: a real ancestor of HEAD that predates Block 200
# and therefore carries NEITHER parent artifact.
STALE_PARENT_COMMIT = "725269c6057deed9b7ac1f72a315297a9f99f35a"
# A real but superseded authority head, carried from Block 199's own record.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_rule_is_dynamics",
    "claim_naive_uniqueness",
    "claim_probabilistic_marginal_derived",
    "claim_generic_parameter_theorem",
    "claim_readings_licensed",
    "break_spin_diagonalisation",
    "break_twist_dictionary",
    "break_seam_wrap_fork",
    "break_gauge_hodge_defect",
    "break_lane_pair_census",
    "break_odd_extent_obstruction",
    "break_cell_uniqueness",
    "break_cell_sign_location",
    "claim_target_rank_selects_hodge",
    "break_no_real_triple",
    "break_four_by_four_triple",
    "break_cubic_covariance",
    "break_bench_metadata",
    "break_conditional_locality",
    "break_schur_identity",
    "break_local_block_invariance",
    "break_end_to_end_profile",
    "break_far_dependence_location",
    "break_instance_scope",
    "claim_marginal_is_local",
    "claim_selection_bridges_supplied",
    "break_finite_instance_scope",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_rule_is_dynamics": "B",
    "claim_naive_uniqueness": "B",
    "claim_probabilistic_marginal_derived": "B",
    "claim_generic_parameter_theorem": "B",
    "claim_readings_licensed": "B",
    "break_spin_diagonalisation": "C",
    "break_twist_dictionary": "C",
    "break_seam_wrap_fork": "C",
    "break_gauge_hodge_defect": "C",
    "break_lane_pair_census": "C",
    "break_odd_extent_obstruction": "C",
    "break_cell_uniqueness": "D",
    "break_cell_sign_location": "D",
    "claim_target_rank_selects_hodge": "D",
    "break_no_real_triple": "E",
    "break_four_by_four_triple": "E",
    "break_cubic_covariance": "E",
    "break_bench_metadata": "F",
    "break_conditional_locality": "F",
    "break_schur_identity": "F",
    "break_local_block_invariance": "F",
    "break_end_to_end_profile": "F",
    "break_far_dependence_location": "F",
    "break_instance_scope": "G",
    "claim_marginal_is_local": "G",
    "claim_selection_bridges_supplied": "G",
    "break_finite_instance_scope": "G",
    "drop_n5_fence": "H",
    "break_nsimplify_absence": "H",
    "break_float_absence": "H",
}
MUTATED_FAMILIES = "ABCDEFGH"


class Checks:
    def __init__(self) -> None:
        self.results: list = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def families(self) -> dict:
        summary: dict = {}
        for key, _, value in self.results:
            family = key.split("-", 1)[0]
            summary[family] = summary.get(family, True) and value
        return summary

    def report(self) -> None:
        for key, _, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}")
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
    "A FINITE MATRIX-PAIR EXHIBIT, NOT A SELECTED PHYSICAL RULE: A = sx, B = -sz and Omega(t,x) = sx^t sz^x on the declared finite extents",
    "A TARGET-CONDITIONAL CELL ENCODING: the sixteen Clifford-word coefficients solving Psi_cell^T CP Psi_cell = L tensor I_2 after L is declared",
    "AN INDEPENDENT REAL Cl(3,0) EXHIBIT: a minimal 4 x 4 triple and its 24 proper cubic rotations, with no bridge asserting that the lane signs select this lift",
    "BLOCK 190's LANE KERNEL CONVENTIONS AND BLOCK 107's COMPLETION, CARRIED UNCHANGED AS THE COMPARISON TARGET: the eta-staggered scalar kernel with eta_t = 1 and eta_x = (-1)^t at the periodic, wrap-edge and one-edge-seam closures, the grade deg(t, x) = t mod 2 + x mod 2, d_K = P1 K P0 + P2 K P1, the site reflection theta_s(t) = -t, the raising set A_s in the CLOSED half {0..T/2} EXCLUDING fixed-slice spatial edges, the glue D_s = A_s - Ps A_s Ps and the completion Q = m H + H D_s - D_s^T H at m = 9/20 and c = 5/13",
    "BLOCK 171's COMMITTED 12x4 BENCH READ THROUGH ITS OWN Site AND Env CLASSES AND NOT REBUILT: Site('12x4', 12, 4) with N = 24, T = 6, c = 1, tstar = 5 and lx = 4, the xgraded carrier substitution, the record dictionary, and the landed weight profile Env.profile('W9', tstar)",
    "THE LANDED BLOCK 105 shear_hodge(c, v) READ THROUGH THE BLOCK 128 MODULE AT UNIT VOLUME -- THE ONLY GEOMETRIC OBJECT IMPORTED -- at the symbolic shear c and at the rational shear 5/13",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL EIGHT ARE FALSE
# AND STAY FALSE.  THE SECOND, THIRD AND FOURTH ARE THE THREE THIS BLOCK'S
# RESULT MOST INVITES A READER TO ASSUME.
GRAVITY_SUPPLIED_CLAIMED = False
RULE_IS_DYNAMICS_CLAIMED = False
NAIVE_UNIQUENESS_CLAIMED = False
PROBABILISTIC_MARGINAL_DERIVED_CLAIMED = False
MARGINAL_IS_LOCALLY_COMPUTABLE_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
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
)
READINGS = (
    "Two fixed matrices and a finite congruence do not supply dynamics, evolution, or a continuum field equation.",
    "Six admitted ordered generator pairs reproduce the lane signs, so those signs do not uniquely select the displayed pair.",
    "A unique preimage after a target is declared does not select that target; unrelated replacement targets have the same certificate.",
    "The exact Block 171 Schur identity is independent imported evidence and is not derived from A, B, or Omega here.",
    "Four finite extents and one finite bench do not constitute a generic-parameter or continuum theorem.",
)
CHECK_VERDICT = "FINITE-EXHIBITS-CONFIRMED-SELECTION-NOT-SUPPLIED"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
UNIT_VOLUME = sp.Integer(1)

# --- C: S2, THE KERNEL IDENTIFICATION ---------------------------------------
TEMPORAL_COUPLING = ((0, 1), (1, 0))          # A  = sx
SPATIAL_COUPLING = ((-1, 0), (0, 1))          # B  = -sz
BENCH_EXTENT = (6, 4)                          # Z_6 x Z_4, the committed extent
FORK_EXTENT = (8, 4)
ODD_EXTENTS = ((8, 3), (7, 4))
EVEN_EXTENTS = ((6, 4), (8, 4))
TWISTS = ((1, 1), (1, -1), (-1, 1), (-1, -1))
LANE_CONVENTIONS = ("periodic", "wrap", "seam")
SPIN_NONSCALAR_BLOCKS = 0
SCALAR_KERNEL_NNZ = 96                         # 4 directed links at 24 sites
# THE TWIST DICTIONARY, TWELVE VERDICTS, IN THE ORDER (periodic, wrap, seam).
TWIST_DICTIONARY = {
    (1, 1): (True, False, False),
    (1, -1): (False, False, False),
    (-1, 1): (False, True, True),
    (-1, -1): (False, False, False),
}
DICTIONARY_VERDICTS = 12
# THE LANDED BLOCK 190 FORK, REPRODUCED AND NOT CITED.
FORK_MASS = sp.Rational(9, 20)
FORK_SHEAR = sp.Rational(5, 13)
FORK_ASYMMETRY = {"seam": 144, "wrap": 160}
# THE GAUGE THAT MOVES THE KERNEL DOES NOT MOVE THE REFLECTION OR THE HODGE.
SEAM_EQUIVALENCE_RESIDUAL = 0          # nnz(E K_wrap E - K_seam)
REFLECTION_COMMUTATOR_NNZ = 24
REFLECTION_COMMUTATOR_CELLS = ((7, 0), (1, 0))
REFLECTION_COMMUTATOR_ENTRY = sp.Integer(-2)
HODGE_COMMUTATOR_NNZ = 16
HODGE_COMMUTATOR_CELLS = ((3, 1), (4, 0))
HODGE_COMMUTATOR_ENTRY = sp.Rational(-65, 288)
GAUGE_LINK_RESIDUAL = 0
GAUGE_HODGE_RESIDUAL_SCALAR = 48
GAUGE_HODGE_RESIDUAL_COVARIANT = 96
GAUGE_RESIDUAL_DISPLACEMENTS = ((1, 1), (1, 3), (7, 1), (7, 3))
GAUGE_RESIDUAL_UNIFORM_VALUE = True            # every entry exactly b/2
GAUGE_RESIDUAL_ENDPOINT_PRODUCT = -1
# THE CENSUS, AND SIX IS THE STATED-POWER ANSWER.
LANE_PAIR_CENSUS = {
    ("stated", "lane"): 6,
    ("stated", "scout"): 6,
    ("parity", "lane"): 2,
    ("parity", "scout"): 4,
}
LANE_PAIRS = (("sx", "sz"), ("sx", "isy"), ("sz", "sx"),
              ("sz", "isy"), ("isy", "sx"), ("isy", "sz"))
# THE PARITY OBSTRUCTION.
ODD_EXTENT_NONSCALAR = {(8, 3): 16, (7, 4): 8}
EVEN_EXTENT_NONSCALAR = {(6, 4): 0, (8, 4): 0}
ODD_WRAP_BLOCK = ((sp.Rational(-1, 2), 0), (0, sp.Rational(1, 2)))

# --- D: S3, THE UNIQUE CELL FORM ---------------------------------------------
CELL_CORNERS = ((0, 0), (0, 1), (1, 0), (1, 1))
CELL_EQUATIONS = 64
CELL_UNKNOWNS = 16
CELL_COEFFICIENT_RANK = 16
CELL_AUGMENTED_RANK = 16
CELL_AFFINE_DIMENSION = 0
CELL_SOLUTION_COUNT = 1
ANCHOR_PARITIES = ((0, 0), (0, 1), (1, 0), (1, 1))
ANCHOR_PARITY_RANKS = {
    (0, 0): (16, 16, 0), (0, 1): (16, 16, 0),
    (1, 0): (16, 16, 0), (1, 1): (16, 16, 0),
}
TARGET_REPLACEMENT_CERTIFICATE = (16, 16, 0, 0)
TARGET_REPLACEMENT_CASES = 8
CELL_MISMATCH_COUNT = 1
CELL_SIGN_POSITION = (1, 2)
CELL_SIGN_IS_OPPOSITE = True                   # F[1,2] + L[1,2] = 0 exactly
DIRECTED_REPAIR_RESIDUAL = 0                   # nnz(F' - L) with W'_12 = -sx sz
DIRECTED_REPAIR_CP_RESIDUAL = 0                # f'_12 W'_12 - f_12 W_12
GENERAL_RANK = 64
GENERAL_AFFINE_DIMENSION = 0
GENERAL_WORD_RESIDUAL = 0                      # CP_word - Psi (L (x) I2) Psi^T

# --- E: S4, THE Cl(3,0) LIFT --------------------------------------------------
ANTIDIAGONAL_FORCED = True                     # m0 = m3 = 0 against diag(1,-1)
SQUARE_CONDITIONS = ("b*c_ - 1", "d*e - 1")
ANTICOMMUTATOR_CONDITION = "b*e + c_*d"
REDUCED_CONDITION = "b**2 + d**2"
REAL_TRIPLE_SOLUTIONS = 0
REAL_TRIPLE_EXISTS = False
ODD_DIMENSION_DETERMINANT_SIGN = -1
ODD_DIMENSION_OBSTRUCTION = True
ISY_SQUARE = ((-1, 0), (0, -1))
LIFT_DIMENSION = 4
LIFT_SQUARE_RESIDUALS = (0, 0, 0)
LIFT_ANTICOMMUTATORS = (0, 0, 0)
PROPER_ROTATIONS = 24
INTERTWINER_NULLITY = 2
SPIN_DETERMINANTS = (1, 4)
SPIN_GRAM_SCALARS = (1, 2)
SPIN_CONJUGATION_RESIDUAL = 0
CHECK_SPIN_DETERMINANTS = (64, 256)            # the independent check's own picks
CHECK_SPIN_GRAM_SCALARS = (8, 16)

# --- F: S5, THE DISTRIBUTION IDENTIFICATION -----------------------------------
BENCH_TAG = "12x4"
BENCH_COVER = 12
BENCH_LX = 4
BENCH_N = 24
BENCH_T = 6
BENCH_CORE = 1
BENCH_TSTAR = 5
BENCH_SITE_ROWS = (20, 21, 22, 23)
BENCH_GRAM = "W9"
BASE_RECORD_CELL = (4, 1)                      # (tstar - 1, 1)
FAR_CELLS = ((2, 0), (2, 1), (2, 2), (2, 3))
FAR_MOVED_COMPONENTS = (4, 4, 4, 4)
CONDITIONAL_LOCALITY_HOLDS = False
SCHUR_RESIDUALS = (0, 0, 0)     # Q Q^-1 - I, Q_rr Q_rr^-1 - I, marginal - Schur^-1
ENVIRONMENT_SIZE = 20
LOCAL_BLOCK_RESIDUALS = ((0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0))
COUPLING_SUPPORT_SLOTS = (0, 4)                # {(tstar+1) mod T, tstar - 1}
PROFILE_RESIDUAL = (0, 0, 0, 0)
BASE_PROFILE = (
    sp.Rational(
        99491964565273401802184764096700720144873011550590119008125660,
        332104416501168344774479973392962443860642497838366698864680759),
    sp.Rational(
        91080721824530247656123193767966591345766405303415704520142860,
        332104416501168344774479973392962443860642497838366698864680759),
    sp.Rational(
        1219997211440630957997585843315269123255292746675951695815488087,
        5313670664018693516391679574287399101770279965413867181834892144),
    sp.Rational(
        1044510470341204167061166405137452994664756549073822309567107737,
        5313670664018693516391679574287399101770279965413867181834892144),
)
ENVIRONMENT_CORRECTION_NNZ = (1, 4, 5, 1)

# --- G: THE SCOPE QUALIFICATIONS ---------------------------------------------
INSTANCE_SCOPE = (
    "the committed 12x4 bench, which is Z_6 x Z_4",
    "the xgraded carrier",
    "the stated base record {(tstar - 1, 1): 0}",
    "four class-0 record changes at slot 2",
)
FINITE_INSTANCES = ((6, 4), (8, 4), (8, 3), (7, 4))
FINITE_INSTANCE_COUNT = 5                      # the four extents and the bench
RATIONAL_SHEARS = (sp.Rational(5, 13),)
GAUSSIAN_INTERPRETATION_DERIVED = False
MARGINAL_LOCAL_ONLY_DEFECT = 8                 # nnz(Schur^-1 - Q[ss,ss]^-1)
ENVIRONMENT_CORRECTION_SUPPORT = 8             # nnz(Q_sr Q_rr^-1 Q_rs)
LOCAL_ONLY_MOVED_COMPONENTS = 4
NON_CLIFFORD_FRAME = ((1, 1), (0, 1))
NON_CLIFFORD_TEMPORAL = ((0, 1), (1, -2))
NON_CLIFFORD_SPATIAL = ((-1, 1), (1, 0))
NON_CLIFFORD_TEMPORAL_SQUARE = ((1, -2), (-2, 5))
NON_CLIFFORD_SPATIAL_SQUARE = ((2, -1), (-1, 1))
NON_CLIFFORD_ANTICOMMUTATOR = ((2, -3), (-3, 2))
NON_CLIFFORD_LANE_SIGNS_MATCH = True
NON_CLIFFORD_IS_CLIFFORD = False
GENERATOR_PAIR_SELECTED = False
HODGE_TARGET_SELECTED = False
SAME_RULE_BRIDGE_SUPPLIED = False

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  This block's whole content is a set of EXACT ZERO/NONZERO
# statements -- zero non-scalar spin blocks against 96 nonzero kernel entries,
# an affine solution dimension of 0, a conjugation residual of 0 against a
# nonzero determinant, and four record movements whose numerators run past a
# hundred digits and whose ONLY claim is that they are not zero.  A single such
# call could turn the conditional-locality FAILURE into a spurious success.
# Every mass, shear and volume here is ALREADY an exact sympy Rational.  Gate H
# counts the occurrences in this file's own source and requires ZERO, and gate
# H also requires ZERO float literals by an AST scan of the same source.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_literal_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many float literals this runner's own source
    contains, by an AST walk rather than by a text search.  A float literal is
    the one way an inexact number could enter a file whose every comparison is
    an exact rational one."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def imported_float_atoms() -> int:
    """BLOCK 200's CORRECTION #99, HONOURED BY MEASUREMENT RATHER THAN BY CARE.
    The landed Block 105 shear_hodge(c, v) forms its last corner as 1 / v by
    Python division, so a plain int volume returns a sympy Float there while an
    exact Rational does not -- and the two compare EQUAL, which is exactly why
    the contamination is silent.  Every volume this runner passes is an exact
    sympy Integer or Rational; this counts the Float atoms that actually come
    back, at the unit volume and at both the symbolic and the rational shear."""
    if b128 is None:                                   # pragma: no cover
        return -1
    shear, volume = sp.symbols("c v", positive=True)
    total = 0
    for arguments in ((FORK_SHEAR, UNIT_VOLUME), (shear, volume),
                      (shear, UNIT_VOLUME)):
        block = sp.Matrix(b128.block105.shear_hodge(*arguments))
        total += sum(len(block[i, j].atoms(sp.Float))
                     for i in range(block.rows) for j in range(block.cols))
    return total


def rational_matrix(matrix: sp.MatrixBase) -> DomainMatrix:
    """THE EXACT RATIONAL DOMAIN, AND IT IS NOT A NUMERICAL METHOD.  Every entry
    of every matrix passed here is a sympy Rational, so the matrix lies in
    QQ^(m x n) exactly; DomainMatrix carries out the inverse, the rank and the
    determinant by exact fraction-free arithmetic over that field.  No float is
    created at any point and no tolerance exists to be tuned."""
    return DomainMatrix.from_Matrix(sp.Matrix(matrix)).convert_to(QQ)


def gaussian_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    """THE EXACT INVERSE OVER QQ_I, used for the bench's two big inverses.  The
    committed carrier carries an imaginary unit, so the field is QQ_I and not
    QQ; the arithmetic is exact in both."""
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix)).convert_to(QQ_I).to_field().inv().to_Matrix()


def exact_rank(matrix: sp.MatrixBase) -> int:
    return rational_matrix(matrix).rank()


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    matrix = sp.Matrix(matrix)
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if matrix[i, j] != 0)


def residual_count(matrix: sp.MatrixBase) -> int:
    """THE RESIDUAL, COUNTED: exact nonzero entries after exact expansion.  A
    count of 0 is the exact zero-matrix statement and no tolerance is
    involved."""
    return nonzero_entries(sp.Matrix(matrix).applyfunc(sp.expand))


def rational_residual_count(matrix: sp.MatrixBase) -> int:
    """The same count over a rational-function field, where a nonzero entry may
    only be visible after a common denominator is taken."""
    matrix = sp.Matrix(matrix)
    return sum(1 for i in range(matrix.rows) for j in range(matrix.cols)
               if sp.cancel(sp.together(matrix[i, j])) != 0)


def tuple_of(matrix: sp.MatrixBase) -> tuple:
    matrix = sp.Matrix(matrix)
    return tuple(tuple(matrix[i, j] for j in range(matrix.cols))
                 for i in range(matrix.rows))


def matrix_of(rows) -> sp.Matrix:
    return sp.Matrix([[sp.sympify(entry) for entry in row] for row in rows])


# ---------------------------------------------------------------------------
# THE RULE, REBUILT FROM FORMULAS.  Two fixed real 2 x 2 matrices and one
# staggering; everything in family C, D and E comes from these four lines.
# ---------------------------------------------------------------------------
SX = sp.Matrix([[0, 1], [1, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
ISY = sp.Matrix([[0, 1], [-1, 0]])
I2 = sp.eye(2)
GENERATORS = (("sx", SX), ("sz", SZ), ("isy", ISY))
A_COUPLING = SX
B_COUPLING = -SZ


def staggering(time: int, space: int) -> sp.Matrix:
    """Omega(t, x) = gamma_t^t gamma_x^x, which for the period-two pair (sx, sz)
    is sx^(t mod 2) sz^(x mod 2)."""
    return (SX ** (time % 2)) * (SZ ** (space % 2))


def covariant_kernel(width: int, extent: int, twist: tuple) -> tuple:
    """The covariant nearest-neighbour kernel and its spin-diagonalisation.
    Returns (scalar kernel, number of NON-SCALAR 2 x 2 blocks)."""
    size = width * extent

    def index(time, space):
        return (time % width) * extent + space % extent

    kernel = sp.zeros(2 * size, 2 * size)

    def place(i, j, block):
        for row in range(2):
            for column in range(2):
                kernel[2 * i + row, 2 * j + column] += block[row, column]

    for time in range(width):
        for space in range(extent):
            temporal = twist[0] if time == width - 1 else 1
            spatial = twist[1] if space == extent - 1 else 1
            place(index(time, space), index(time + 1, space),
                  temporal * A_COUPLING / 2)
            place(index(time + 1, space), index(time, space),
                  -temporal * A_COUPLING.T / 2)
            place(index(time, space), index(time, space + 1),
                  spatial * B_COUPLING / 2)
            place(index(time, space + 1), index(time, space),
                  -spatial * B_COUPLING.T / 2)
    frame = sp.zeros(2 * size, 2 * size)
    for time in range(width):
        for space in range(extent):
            block = staggering(time, space)
            for row in range(2):
                for column in range(2):
                    frame[2 * index(time, space) + row,
                          2 * index(time, space) + column] = block[row, column]
    diagonalised = sp.expand(frame.T * kernel * frame)
    nonscalar = 0
    for i in range(size):
        for j in range(size):
            block = diagonalised[2 * i:2 * i + 2, 2 * j:2 * j + 2]
            if (sp.expand(block[0, 1]) != 0 or sp.expand(block[1, 0]) != 0
                    or sp.expand(block[0, 0] - block[1, 1]) != 0):
                nonscalar += 1
    scalar = sp.Matrix(size, size, lambda i, j: diagonalised[2 * i, 2 * j])
    return scalar, nonscalar


def lane_kernel(width: int, extent: int, convention: str) -> sp.Matrix:
    """Block 190's eta-staggered scalar kernel at one of its three closures."""
    size = width * extent

    def index(time, space):
        return (time % width) * extent + space % extent

    kernel = sp.zeros(size, size)
    seam = width // 2 - 1
    for time in range(width):
        for space in range(extent):
            if convention == "wrap":
                sign = -1 if time == width - 1 else 1
            elif convention == "seam":
                sign = -1 if time == seam else 1
            else:
                sign = 1
            kernel[index(time, space), index(time + 1, space)] += \
                sp.Rational(sign, 2)
            kernel[index(time + 1, space), index(time, space)] -= \
                sp.Rational(sign, 2)
            stagger = (-1) ** time
            kernel[index(time, space), index(time, space + 1)] += \
                sp.Rational(stagger, 2)
            kernel[index(time, space + 1), index(time, space)] -= \
                sp.Rational(stagger, 2)
    return kernel


def site_sign_equivalent(scalar: sp.Matrix, lane: sp.Matrix, size: int) -> bool:
    """THE GAUGE IS PROPAGATED, NOT SEARCHED.  Fix eps at one site and push the
    exact link ratio outward by breadth-first traversal; a contradiction, a
    ratio outside {+1, -1} or a missing lane link refutes equivalence at once.
    The verdict is then re-checked as an exact matrix identity."""
    signs = {0: 1}
    frontier = [0]
    links: dict = {}
    for i in range(size):
        for j in range(size):
            if scalar[i, j] != 0:
                links.setdefault(i, []).append(j)
    while frontier:
        i = frontier.pop()
        for j in links.get(i, []):
            if lane[i, j] == 0:
                return False
            ratio = sp.Rational(lane[i, j]) / sp.Rational(scalar[i, j])
            if ratio not in (1, -1):
                return False
            value = signs[i] * ratio
            if j in signs:
                if signs[j] != value:
                    return False
            else:
                signs[j] = value
                frontier.append(j)
    gauge = sp.diag(*[signs.get(k, 1) for k in range(size)])
    return residual_count(gauge * scalar * gauge - lane) == 0


# --- the Block 190 carrier at the fork extent, rebuilt from the same formulas -
OFFSET_PERMUTATION = sp.Matrix([[0, 0, 1, 0],
                                [0, 0, 0, 1],
                                [1, 0, 0, 0],
                                [0, 1, 0, 0]])


def fork_index(time: int, space: int) -> int:
    width, extent = FORK_EXTENT
    return (time % width) * extent + space % extent


def grade_projector(grade: int) -> sp.Matrix:
    width, extent = FORK_EXTENT
    return sp.diag(*[1 if (time % 2 + space % 2) == grade else 0
                     for time in range(width) for space in range(extent)])


def raising_part(kernel: sp.Matrix) -> sp.Matrix:
    """d_K = P1 K P0 + P2 K P1."""
    p0, p1, p2 = (grade_projector(g) for g in (0, 1, 2))
    return sp.expand(p1 * kernel * p0 + p2 * kernel * p1)


def fork_reflection() -> sp.Matrix:
    width, extent = FORK_EXTENT
    size = width * extent
    matrix = sp.zeros(size, size)
    for time in range(width):
        for space in range(extent):
            matrix[fork_index(-time, space), fork_index(time, space)] = 1
    return matrix


def fork_restricted(raising: sp.Matrix) -> sp.Matrix:
    """A_s: the d_K entries inside the CLOSED half {0..T/2}, with the two fixed
    slices' own spatial edges removed."""
    width, extent = FORK_EXTENT
    size = width * extent
    half = width // 2
    closed, fixed = set(range(half + 1)), {0, half}
    matrix = sp.zeros(size, size)
    for row in range(size):
        for column in range(size):
            if raising[row, column] == 0:
                continue
            row_time, column_time = row // extent, column // extent
            if row_time not in closed or column_time not in closed:
                continue
            if row_time == column_time and row_time in fixed:
                continue
            matrix[row, column] = raising[row, column]
    return matrix


def fork_embedding(time: int, space: int) -> sp.Matrix:
    width, extent = FORK_EXTENT
    matrix = sp.zeros(width * extent, 4)
    for column, (delta_t, delta_x) in enumerate(CELL_CORNERS):
        matrix[fork_index(time + delta_t, space + delta_x), column] = 1
    return matrix


def imported_shear_block(shear) -> sp.Matrix:
    """THE ONE IMPORTED GEOMETRIC OBJECT: the LANDED Block 105 shear Hodge
    diag(v, v g(c)^-1, 1/v) with g(c) = [[1, c], [c, 1]], read at UNIT volume.
    NO nsimplify: both arguments are already exact."""
    return sp.expand(sp.Matrix(b128.block105.shear_hodge(shear, UNIT_VOLUME)))


def fork_hodge(shear) -> sp.Matrix:
    """THE QUARTER-WEIGHTED FOUR-CORNER CELL AVERAGE, Block 191's assembly rule
    at Block 190's seam convention and at unit volume."""
    width, extent = FORK_EXTENT
    half = width // 2
    block = imported_shear_block(shear)
    reflected = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    result = sp.zeros(width * extent, width * extent)
    for time in range(width):
        chosen = block if time < half else reflected
        for space in range(extent):
            embedding = fork_embedding(time, space)
            result += embedding * chosen * embedding.T / 4
    return sp.expand(result)


def fork_completion(convention: str, hodge: sp.Matrix,
                    reflection: sp.Matrix) -> sp.Matrix:
    """Q = m H + H D_s - D_s^T H, Block 107's completion used UNCHANGED."""
    width, extent = FORK_EXTENT
    raising = fork_restricted(raising_part(lane_kernel(width, extent, convention)))
    glue = sp.expand(raising - reflection * raising * reflection)
    return sp.expand(FORK_MASS * hodge + hodge * glue - glue.T * hodge)


# ---------------------------------------------------------------------------
# THE MEASUREMENT PASS.  Every number this runner reports is produced here, once
# and before any mutation flag is read.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class KernelFacts:
    nonscalar: dict
    scalar_nnz: int
    dictionary: dict
    verdicts: int
    fork_asymmetry: dict
    seam_equivalence: int
    reflection_commutator: tuple
    hodge_commutator: tuple
    gauge_link_residual: int
    gauge_scalar_residual: int
    gauge_covariant_residual: int
    gauge_displacements: tuple
    gauge_uniform: bool
    gauge_endpoints: bool
    census: dict
    pairs: tuple
    odd_nonscalar: dict
    even_nonscalar: dict
    odd_block: tuple


@dataclass(frozen=True)
class CellFacts:
    equations: int
    unknowns: int
    coefficient_rank: int
    augmented_rank: int
    affine_dimension: int
    solution_count: int
    parity_ranks: dict
    replacement_certificates: tuple
    mismatch_count: int
    mismatch_positions: tuple
    sign_opposite: bool
    coefficients: tuple
    target: tuple
    repair_residual: int
    repair_cp_residual: int
    general_rank: int
    general_affine_dimension: int
    general_word_residual: int


@dataclass(frozen=True)
class LiftFacts:
    antidiagonal_forced: bool
    square_conditions: tuple
    anticommutator_condition: str
    reduced_condition: str
    real_solutions: int
    isy_square: tuple
    odd_dimension_det_sign: int
    odd_dimension_obstruction: bool
    square_residuals: tuple
    anticommutators: tuple
    rotations: int
    nullities: tuple
    determinants: tuple
    gram_scalars: tuple
    conjugation_residual: int


@dataclass(frozen=True)
class BenchFacts:
    tag: str
    size: int
    width: int
    core: int
    tstar: int
    extent: int
    site_rows: tuple
    moved_components: tuple
    all_moves_nonzero: bool
    schur_residuals: tuple
    environment_size: int
    local_residuals: tuple
    support_slots: tuple
    inward_support_slots: tuple
    profile: tuple
    profile_residual: tuple
    correction_nnz: tuple
    correction_support: int
    local_only_defect: int
    local_only_moved: int


@dataclass(frozen=True)
class CounterexampleFacts:
    frame: tuple
    temporal: tuple
    spatial: tuple
    temporal_square: tuple
    spatial_square: tuple
    anticommutator: tuple
    lane_signs_match: bool
    is_clifford: bool
    period_two: bool


@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    kernel: KernelFacts
    cell: CellFacts
    lift: LiftFacts
    bench: BenchFacts
    counterexample: CounterexampleFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    imported_floats: int


def measure_kernel() -> KernelFacts:
    """S2, AND EVERY LINE OF IT IS A FORMULA.  The covariant kernel, its
    staggering, the twist dictionary by exact sign propagation, the landed fork
    rebuilt from d_K/A_s/D_s/Q, the gauge's non-commutation, the census and the
    parity obstruction."""
    width, extent = BENCH_EXTENT
    size = width * extent
    nonscalar = {}
    dictionary = {}
    scalar_nnz = None
    for twist in TWISTS:
        scalar, bad = covariant_kernel(width, extent, twist)
        nonscalar[twist] = bad
        if twist == (1, 1):
            scalar_nnz = nonzero_entries(scalar)
        dictionary[twist] = tuple(
            site_sign_equivalent(scalar, lane_kernel(width, extent, c), size)
            for c in LANE_CONVENTIONS)
    verdicts = sum(len(row) for row in dictionary.values())

    # THE LANDED FORK, REBUILT AND NOT CITED.
    hodge = fork_hodge(FORK_SHEAR)
    reflection = fork_reflection()
    asymmetry = {}
    for convention in ("seam", "wrap"):
        action = fork_completion(convention, hodge, reflection)
        asymmetry[convention] = residual_count(action - action.T)

    # THE GAUGE, AND WHAT IT DOES NOT COMMUTE WITH.
    fwidth, fextent = FORK_EXTENT
    fsize = fwidth * fextent
    seam_sign = sp.diag(*[1 if (i // fextent) < fwidth // 2 else -1
                          for i in range(fsize)])
    # E IS A GENUINE KERNEL EQUIVALENCE -- E K_wrap E = K_seam EXACTLY -- which
    # is what makes its FAILURE to commute with the reflection and the Hodge a
    # statement rather than a coincidence of a badly chosen sign.
    seam_equivalence = residual_count(
        seam_sign * lane_kernel(fwidth, fextent, "wrap") * seam_sign
        - lane_kernel(fwidth, fextent, "seam"))
    reflection_commutator = sp.expand(seam_sign * reflection
                                      - reflection * seam_sign)
    hodge_commutator = sp.expand(seam_sign * hodge - hodge * seam_sign)
    (rt, rx), (rt2, rx2) = REFLECTION_COMMUTATOR_CELLS
    (ht, hx), (ht2, hx2) = HODGE_COMMUTATOR_CELLS
    reflection_pair = (residual_count(reflection_commutator),
                       reflection_commutator[fork_index(rt, rx),
                                             fork_index(rt2, rx2)])
    hodge_pair = (residual_count(hodge_commutator),
                  hodge_commutator[fork_index(ht, hx), fork_index(ht2, hx2)])

    # THE LITERAL STAGE-2 GAUGE: zero on the LINKS, 96 covariant entries on the
    # HODGE, every one of them exactly b/2 on a cell diagonal.
    shear, volume = sp.symbols("c v", positive=True)
    symbolic_hodge = sp.zeros(fsize, fsize)
    block = sp.expand(sp.Matrix(b128.block105.shear_hodge(shear, volume)))
    reflected = sp.expand(OFFSET_PERMUTATION * block * OFFSET_PERMUTATION.T)
    for time in range(fwidth):
        chosen = block if time < fwidth // 2 else reflected
        for space in range(fextent):
            embedding = fork_embedding(time, space)
            symbolic_hodge += embedding * chosen * embedding.T / 4
    symbolic_hodge = sp.expand(symbolic_hodge)
    gauge_signs = [((-1) ** (i % fextent))
                   * (1 if (i // fextent) < fwidth // 2 else -1)
                   for i in range(fsize)]
    gauge = sp.diag(*gauge_signs)
    # ZERO ON THE LINKS: the literal stage-2 representative under the temporal
    # wrap twist reaches the landed one-edge seam kernel EXACTLY under g.
    twisted_scalar, _ = covariant_kernel(fwidth, fextent, (-1, 1))
    link_residual = residual_count(
        gauge * twisted_scalar * gauge
        - lane_kernel(fwidth, fextent, "seam"))
    hodge_residual = sp.expand(gauge * symbolic_hodge * gauge - symbolic_hodge)
    support = [(i, j) for i in range(fsize) for j in range(fsize)
               if sp.expand(hodge_residual[i, j]) != 0]
    half_shear = sp.cancel(volume * shear / (1 - shear ** 2) / 2)
    uniform = all(sp.cancel(hodge_residual[i, j] - half_shear) == 0
                  for i, j in support)
    endpoints = all(gauge_signs[i] * gauge_signs[j]
                    == GAUGE_RESIDUAL_ENDPOINT_PRODUCT for i, j in support)
    displacements = tuple(sorted({
        (((j // fextent) - (i // fextent)) % fwidth,
         ((j % fextent) - (i % fextent)) % fextent) for i, j in support}))
    # THE COVARIANT PRESENTATION, FORMED AND COUNTED RATHER THAN DOUBLED ON
    # PAPER: the Hodge is spin-trivial, so its residual in the 2N x 2N frame is
    # the scalar residual tensored with I_2, and the count is taken there.
    covariant_hodge_residual = sp.Matrix(
        sp.kronecker_product(hodge_residual, I2))
    covariant_residual = sum(
        1 for i in range(2 * fsize) for j in range(2 * fsize)
        if sp.expand(covariant_hodge_residual[i, j]) != 0)

    # THE CENSUS, FOUR WAYS.
    census = {}
    pairs = ()
    for powers in ("stated", "parity"):
        for predicate in ("lane", "scout"):
            hits = lane_pair_census(powers, predicate)
            census[(powers, predicate)] = len(hits)
            if (powers, predicate) == ("stated", "lane"):
                pairs = hits

    # THE PARITY OBSTRUCTION.
    odd = {ext: covariant_kernel(ext[0], ext[1], (1, 1))[1]
           for ext in ODD_EXTENTS}
    even = {ext: covariant_kernel(ext[0], ext[1], (1, 1))[1]
            for ext in EVEN_EXTENTS}
    odd_block = tuple_of(sp.expand(
        staggering(0, 2).T * (B_COUPLING / 2) * staggering(0, 0)))
    return KernelFacts(
        nonscalar, scalar_nnz, dictionary, verdicts, asymmetry,
        seam_equivalence, reflection_pair, hodge_pair, link_residual,
        len(support), covariant_residual, displacements, uniform, endpoints,
        census, pairs, odd, even, odd_block)


def lane_pair_census(powers: str, predicate: str) -> tuple:
    """THE FOUR CENSUSES, MEASURED SIDE BY SIDE.  'stated' uses the actual
    integer powers Omega = G1^t G2^x that the rule declares; 'parity' resets
    them modulo two, which is NOT the stated frame when i sy occurs because
    (i sy)^2 = -I.  'lane' is the true lane test c_t = 1 and c_x = (-1)^t;
    'scout' is the weaker t-alternation predicate that does not require the
    spatial sign to be uniform in x."""
    hits = []
    for (name_a, first), (name_b, second) in itertools.permutations(
            GENERATORS, 2):
        if residual_count(first * second + second * first) != 0:
            continue
        sign_a = sp.expand(first * first)[0, 0]
        sign_b = sp.expand(second * second)[0, 0]
        temporal, spatial = sign_a * first, sign_b * second
        temporal_values, spatial_values, scalarity = {}, {}, True
        for time in range(4):
            for space in range(4):
                if powers == "stated":
                    here = (first ** time) * (second ** space)
                    ahead = (first ** (time + 1)) * (second ** space)
                    right = (first ** time) * (second ** (space + 1))
                else:
                    here = (first ** (time % 2)) * (second ** (space % 2))
                    ahead = (first ** ((time + 1) % 2)) * (second ** (space % 2))
                    right = (first ** (time % 2)) * (second ** ((space + 1) % 2))
                first_block = sp.expand(here.T * temporal * ahead)
                second_block = sp.expand(here.T * spatial * right)
                for block in (first_block, second_block):
                    if (block[0, 1] != 0 or block[1, 0] != 0
                            or sp.expand(block[0, 0] - block[1, 1]) != 0):
                        scalarity = False
                temporal_values[(time, space)] = first_block[0, 0]
                spatial_values[(time, space)] = second_block[0, 0]
        if not scalarity:
            continue
        temporal_ok = all(temporal_values[(t, x)] == 1
                          for t in range(4) for x in range(4))
        if predicate == "lane":
            spatial_ok = all(spatial_values[(t, x)] == (-1) ** t
                             for t in range(4) for x in range(4))
        else:
            spatial_ok = all(spatial_values[(t, x)] == -spatial_values[(t + 1, x)]
                             for t in range(3) for x in range(4))
        if temporal_ok and spatial_ok:
            hits.append((name_a, name_b))
    return tuple(hits)


def cell_system(anchor: tuple, words: dict, unknowns: tuple,
                target: sp.Matrix) -> tuple:
    """The covariant cell equation Psi_cell^T CP Psi_cell = L (x) I_2, written
    out as 64 exact equations in the 16 scalar word coefficients."""
    form = sp.zeros(8, 8)
    for i in range(4):
        for j in range(4):
            block = unknowns[4 * i + j] * words[(i, j)]
            for row in range(2):
                for column in range(2):
                    form[2 * i + row, 2 * j + column] = block[row, column]
    frame = sp.zeros(8, 8)
    for i, (delta_t, delta_x) in enumerate(CELL_CORNERS):
        block = staggering(anchor[0] + delta_t, anchor[1] + delta_x)
        for row in range(2):
            for column in range(2):
                frame[2 * i + row, 2 * i + column] = block[row, column]
    diagonalised = sp.expand(frame.T * form * frame)
    equations = []
    for i in range(4):
        for j in range(4):
            block = diagonalised[2 * i:2 * i + 2, 2 * j:2 * j + 2]
            equations += [sp.expand(block[0, 0] - target[i, j]),
                          sp.expand(block[1, 1] - target[i, j]),
                          sp.expand(block[0, 1]), sp.expand(block[1, 0])]
    return equations, frame


def measure_cell() -> CellFacts:
    """Measure target-conditional encodability, not target selection."""
    shear, volume = sp.symbols("c v", positive=True)
    target = sp.expand(sp.Matrix(b128.block105.shear_hodge(shear, volume)))
    words = {}
    for i, (time_i, space_i) in enumerate(CELL_CORNERS):
        for j, (time_j, space_j) in enumerate(CELL_CORNERS):
            delta_t, delta_x = (time_j - time_i) % 2, (space_j - space_i) % 2
            words[(i, j)] = (SX ** delta_t) * (SZ ** delta_x)
    unknowns = sp.symbols("f0:16")

    equations, frame = cell_system((0, 0), words, unknowns, target)
    coefficients, constants = sp.linear_eq_to_matrix(equations, unknowns)
    rank = coefficients.rank()
    augmented = coefficients.row_join(constants).rank()
    solutions = list(sp.linsolve((coefficients, constants), unknowns))
    solved = sp.Matrix(4, 4, lambda i, j: sp.cancel(solutions[0][4 * i + j]))
    difference = sp.Matrix(4, 4,
                           lambda i, j: sp.cancel(solved[i, j] - target[i, j]))
    positions = tuple((i, j) for i in range(4) for j in range(4)
                      if difference[i, j] != 0)
    sign_opposite = all(
        sp.cancel(solved[i, j] + target[i, j]) == 0 for i, j in positions)

    parity_ranks = {}
    for parity in ANCHOR_PARITIES:
        other, _ = cell_system(parity, words, unknowns, target)
        matrix, vector = sp.linear_eq_to_matrix(other, unknowns)
        other_rank = matrix.rank()
        other_augmented = matrix.row_join(vector).rank()
        parity_ranks[parity] = (
            other_rank, other_augmented, len(unknowns) - other_rank)

    # Rank-16 inversion is not a selector for the imported Hodge target.  Two
    # unrelated declared targets receive the same certificate at all four
    # anchors, including exact substitution residual zero.
    replacement_targets = (
        sp.diag(1, 2, 3, 4),
        sp.Matrix([[0, 1, 2, 3], [5, 0, 7, 11],
                   [13, 17, 0, 19], [23, 29, 31, 0]]),
    )
    replacement_certificates = []
    for replacement in replacement_targets:
        for parity in ANCHOR_PARITIES:
            other, _ = cell_system(parity, words, unknowns, replacement)
            matrix, vector = sp.linear_eq_to_matrix(other, unknowns)
            other_rank = matrix.rank()
            other_augmented = matrix.row_join(vector).rank()
            other_solutions = list(sp.linsolve((matrix, vector), unknowns))
            substitution = {
                unknown: other_solutions[0][index]
                for index, unknown in enumerate(unknowns)
            }
            replacement_certificates.append((
                other_rank,
                other_augmented,
                len(unknowns) - other_rank,
                sum(1 for equation in other
                    if sp.cancel(equation.subs(substitution)) != 0),
            ))

    # THE LONE SIGN IS A DIRECTED WORD LABEL: replace W_12 by -sx sz = sz sx.
    repaired_words = dict(words)
    repaired_words[CELL_SIGN_POSITION] = sp.expand(-words[CELL_SIGN_POSITION])
    repaired, _ = cell_system((0, 0), repaired_words, unknowns, target)
    matrix, vector = sp.linear_eq_to_matrix(repaired, unknowns)
    repaired_solutions = list(sp.linsolve((matrix, vector), unknowns))
    repaired_solved = sp.Matrix(
        4, 4, lambda i, j: sp.cancel(repaired_solutions[0][4 * i + j]))
    repair_residual = rational_residual_count(
        sp.Matrix(4, 4, lambda i, j: repaired_solved[i, j] - target[i, j]))
    i, j = CELL_SIGN_POSITION
    repair_cp_residual = rational_residual_count(
        repaired_solved[i, j] * repaired_words[(i, j)]
        - solved[i, j] * words[(i, j)])

    # NO NON-WORD FAMILY: the general 8 x 8 congruence, solved outright.
    general_unknowns = sp.symbols("g0:64")
    general_form = sp.Matrix(8, 8, lambda i, j: general_unknowns[8 * i + j])
    general_target = sp.zeros(8, 8)
    for i in range(4):
        for j in range(4):
            general_target[2 * i, 2 * j] = target[i, j]
            general_target[2 * i + 1, 2 * j + 1] = target[i, j]
    general_equations = [
        sp.expand((frame.T * general_form * frame)[i, j] - general_target[i, j])
        for i in range(8) for j in range(8)]
    general_matrix, general_vector = sp.linear_eq_to_matrix(
        general_equations, general_unknowns)
    general_rank = general_matrix.rank()
    unique_form = sp.expand(frame * general_target * frame.T)
    word_form = sp.zeros(8, 8)
    for i in range(4):
        for j in range(4):
            block = solved[i, j] * words[(i, j)]
            for row in range(2):
                for column in range(2):
                    word_form[2 * i + row, 2 * j + column] = block[row, column]
    return CellFacts(
        len(equations), len(unknowns), rank, augmented,
        len(unknowns) - rank,
        int(rank == augmented == len(unknowns)), parity_ranks,
        tuple(replacement_certificates),
        len(positions), positions, sign_opposite, tuple_of(solved),
        tuple_of(target), repair_residual, repair_cp_residual,
        general_rank, len(general_unknowns) - general_rank,
        rational_residual_count(word_form - unique_form))


def kronecker(first: sp.Matrix, second: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(sp.BlockMatrix(
        [[first[0, 0] * second, first[0, 1] * second],
         [first[1, 0] * second, first[1, 1] * second]]).as_explicit())


def signed_permutations() -> tuple:
    result = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            matrix = sp.zeros(3, 3)
            for i in range(3):
                matrix[i, permutation[i]] = signs[i]
            if matrix.det() == 1:
                result.append(matrix)
    return tuple(result)


def measure_lift() -> LiftFacts:
    """S4, AND THE 2 x 2 IMPOSSIBILITY IS A REDUCTION RATHER THAN A SEARCH."""
    # (1) anticommutation with diag(1, -1) forces the ANTIDIAGONAL shape.
    entries = sp.symbols("m0:4", real=True)
    general = sp.Matrix(2, 2, entries)
    forced = sp.solve(
        [sp.expand(sp.diag(1, -1) * general + general * sp.diag(1, -1))[i, j]
         for i in range(2) for j in range(2)], list(entries), dict=True)
    antidiagonal_forced = bool(
        forced and forced[0].get(entries[0]) == 0
        and forced[0].get(entries[3]) == 0)
    # (2) the square and anticommutator conditions, written out.
    b, c_, d, e = sp.symbols("b c_ d e", real=True)
    first = sp.Matrix([[0, b], [c_, 0]])
    second = sp.Matrix([[0, d], [e, 0]])
    square_first = sp.expand(first * first - I2)[0, 0]
    square_second = sp.expand(second * second - I2)[0, 0]
    anticommutator = sp.expand(first * second + second * first)[0, 0]
    # (3) the substitution, and the reduction to b^2 + d^2 = 0.
    reduced = sp.expand(
        anticommutator.subs({c_: 1 / b, e: 1 / d}) * b * d)
    # (4) the real solution set of the FULL system is empty.
    real_solutions = sp.solve(
        [square_first, square_second, anticommutator], [b, c_, d, e], dict=True)
    # (5) the near miss.
    isy_square = tuple_of(sp.expand(ISY * ISY))

    lift = (kronecker(SX, I2), kronecker(SZ, SX), kronecker(SZ, SZ))
    squares = tuple(residual_count(g * g - sp.eye(4)) for g in lift)
    anticommutators = tuple(
        residual_count(lift[i] * lift[j] + lift[j] * lift[i])
        for i in range(3) for j in range(i + 1, 3))

    rotations = signed_permutations()
    unknowns = sp.symbols("s0:16")
    template = sp.Matrix(4, 4, lambda i, j: unknowns[4 * i + j])
    nullities, determinants, grams, residual = set(), set(), set(), 0
    for rotation in rotations:
        target = [sp.expand(sum((rotation[i, j] * lift[j] for j in range(3)),
                                sp.zeros(4, 4))) for i in range(3)]
        equations = []
        for i in range(3):
            block = sp.expand(template * lift[i] - target[i] * template)
            equations += [block[a, b_] for a in range(4) for b_ in range(4)]
        matrix, _ = sp.linear_eq_to_matrix(equations, unknowns)
        basis = matrix.nullspace()
        nullities.add(len(basis))
        chosen = None
        for vector in basis:
            candidate = sp.Matrix(4, 4, lambda a, b_: vector[4 * a + b_])
            scale = sp.ilcm(*[sp.Rational(candidate[a, b_]).q
                              for a in range(4) for b_ in range(4)])
            candidate = sp.expand(candidate * scale)
            divisor = sp.igcd(*[int(candidate[a, b_])
                                for a in range(4) for b_ in range(4)])
            if divisor:
                candidate = candidate / divisor
            candidate = sp.Matrix(4, 4,
                                  lambda a, b_: sp.Integer(candidate[a, b_]))
            # INVERTIBILITY IS CERTIFIED BY AN EXACT DETERMINANT, NEVER BY A
            # NUMERICAL RANK OR A CONDITION NUMBER.
            if candidate.det() != 0:
                chosen = candidate
                break
        determinants.add(chosen.det())
        gram = sp.expand(chosen.T * chosen)
        if residual_count(gram - gram[0, 0] * sp.eye(4)) == 0:
            grams.add(gram[0, 0])
        inverse = chosen.inv()
        for i in range(3):
            residual += residual_count(
                chosen * lift[i] * inverse - target[i])
    odd_dimension_det_sign = (-1) ** 3
    odd_dimension_obstruction = odd_dimension_det_sign == -1
    return LiftFacts(
        antidiagonal_forced, (str(square_first), str(square_second)),
        str(anticommutator), str(reduced), len(real_solutions), isy_square,
        odd_dimension_det_sign, odd_dimension_obstruction,
        squares, anticommutators, len(rotations), tuple(sorted(nullities)),
        tuple(sorted(determinants)), tuple(sorted(grams)), residual)


def measure_bench() -> BenchFacts:
    """S5, AND THE OBJECT IS CORRECTED BEFORE IT IS IDENTIFIED.  Block 171's
    bench is read through ITS OWN Site and Env classes, so the landed W9
    profile compared against here is the LANDED one and not a rebuild."""
    zero = sp.Integer(0)
    site = b171.Site(BENCH_TAG, BENCH_COVER, BENCH_LX)
    base = {BASE_RECORD_CELL: zero}
    rows = tuple(site.rows(site.tstar))
    rest = [i for i in range(site.N) if i not in rows]

    def action(records):
        return sp.Matrix(site.bench.Q.subs(site.sub(records=dict(records))))

    def profile(records):
        environment = b171.Env(
            site, site.bench.Q.subs(site.sub(records=dict(records))), "e")
        return tuple(environment.profile(BENCH_GRAM, site.tstar))

    # (1) CONDITIONAL LOCALITY FAILS, AND THE FAILURE IS EXACT.
    landed = profile(base)
    moved, all_nonzero = [], True
    for cell in FAR_CELLS:
        shifted = profile({**base, cell: zero})
        deltas = [sp.cancel(a - b) for a, b in zip(shifted, landed)]
        count = sum(1 for value in deltas if value != 0)
        moved.append(count)
        if count == 0:
            all_nonzero = False

    # (2) THE SCHUR IDENTITY, WITH BOTH INVERSES CERTIFIED.
    base_action = action(base)
    inverse = gaussian_inverse(base_action)
    environment = base_action[rest, rest]
    environment_inverse = gaussian_inverse(environment)
    schur = sp.expand(
        base_action[rows, rows]
        - base_action[rows, rest] * environment_inverse
        * base_action[rest, rows])
    schur_residuals = (
        residual_count(base_action * inverse - sp.eye(site.N)),
        residual_count(environment * environment_inverse
                       - sp.eye(len(rest))),
        residual_count(inverse[rows, rows] - gaussian_inverse(schur)))

    # (3) THE LOCAL DATA ARE EXACTLY LOCAL, AND THEIR SUPPORT IS TWO SLOTS.
    outward = base_action[rows, rest]
    inward = base_action[rest, rows]
    support = tuple(sorted({rest[j] // site.lx for j in range(len(rest))
                            if any(outward[i, j] != 0
                                   for i in range(site.lx))}))
    inward_support = tuple(sorted({rest[i] // site.lx
                                   for i in range(len(rest))
                                   if any(inward[i, j] != 0
                                          for j in range(site.lx))}))
    local_residuals, correction_nnz = [], []
    base_correction = sp.expand(outward * environment_inverse * inward)
    for cell in FAR_CELLS:
        far_action = action({**base, cell: zero})
        local_residuals.append((
            residual_count(base_action[rows, rows] - far_action[rows, rows]),
            residual_count(outward - far_action[rows, rest]),
            residual_count(inward - far_action[rest, rows])))
        far_correction = sp.expand(
            far_action[rows, rest]
            * gaussian_inverse(far_action[rest, rest])
            * far_action[rest, rows])
        correction_nnz.append(residual_count(base_correction - far_correction))

    # (4) END TO END.
    def normalised(matrix):
        hermitian = sp.expand((matrix + matrix.H) / 2)
        total = sum(hermitian[i, i] for i in range(site.lx))
        return tuple(sp.cancel(hermitian[i, i] / total)
                     for i in range(site.lx))

    marginal = gaussian_inverse(schur)
    rebuilt = normalised(marginal)
    profile_residual = tuple(sp.expand(a - b)
                             for a, b in zip(landed, rebuilt))

    # (5) THE MARGINAL IS NOT LOCALLY COMPUTABLE, AND THE DEFECT IS MEASURED.
    local_only = gaussian_inverse(base_action[rows, rows])
    local_only_defect = residual_count(marginal - local_only)
    local_only_moved = sum(
        1 for a, b in zip(rebuilt, normalised(local_only))
        if sp.expand(a - b) != 0)
    return BenchFacts(
        site.tag, site.N, site.T, site.c, site.tstar, site.lx, rows,
        tuple(moved), all_nonzero, schur_residuals, len(rest),
        tuple(local_residuals), support, inward_support, landed,
        profile_residual, tuple(correction_nnz),
        residual_count(base_correction), local_only_defect, local_only_moved)


def measure_counterexample() -> CounterexampleFacts:
    """THE EXACT RATIONAL NON-CLIFFORD PERIOD-TWO FRAME, WHICH IS WHY THE S2
    UNIQUENESS STATEMENT IS QUALIFIED AND NOT NAIVE."""
    frame = matrix_of(NON_CLIFFORD_FRAME)
    inverse = frame.inv()
    temporal = sp.expand(inverse.T * SX * inverse)
    spatial = sp.expand(inverse.T * (-SZ) * inverse)
    matches = True
    for time in range(4):
        for space in range(4):
            here = sp.expand(frame * (SX ** time) * (SZ ** space))
            ahead = sp.expand(frame * (SX ** (time + 1)) * (SZ ** space))
            right = sp.expand(frame * (SX ** time) * (SZ ** (space + 1)))
            if residual_count(here.T * temporal * ahead - I2) != 0:
                matches = False
            if residual_count(here.T * spatial * right
                              + ((-1) ** time) * I2) != 0:
                matches = False
    temporal_square = sp.expand(temporal * temporal)
    spatial_square = sp.expand(spatial * spatial)
    anticommutator = sp.expand(temporal * spatial + spatial * temporal)
    is_clifford = bool(
        residual_count(temporal_square - temporal_square[0, 0] * I2) == 0
        and residual_count(spatial_square - spatial_square[0, 0] * I2) == 0
        and residual_count(anticommutator) == 0)
    return CounterexampleFacts(
        tuple_of(frame), tuple_of(temporal), tuple_of(spatial),
        tuple_of(temporal_square), tuple_of(spatial_square),
        tuple_of(anticommutator), matches, is_clifford,
        residual_count(frame * (SX ** 2) * (SZ ** 2) - frame) == 0)


def measure() -> Facts:
    main_head = resolve_ref("origin/main")
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() \
        else ""
    return Facts(
        main_head,
        authority_certificate(main_head),
        len(IMPOSED_OBJECTS),
        len(REGISTERED_OBJECTS),
        len(ADOPTED_OBJECTS),
        len(UNSUPPLIED_GRAVITY_STRUCTURES),
        len(READINGS),
        measure_kernel(),
        measure_cell(),
        measure_lift(),
        measure_bench(),
        measure_counterexample(),
        scope_certificate(note_text),
        nsimplify_occurrences(),
        float_literal_occurrences(),
        imported_float_atoms())


# ---------------------------------------------------------------------------
# THE CLAIMS.  Every one of them is a literal, and a mutation rewrites exactly
# one of them.  No measurement is taken here.
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict:
    claims = {
        # A
        "main_head": CURRENT_MAIN,
        "parent_commit": PARENT_COMMIT,
        "stale_parent": STALE_PARENT_COMMIT,
        # B
        "imposed": len(IMPOSED_OBJECTS),
        "registered": 0,
        "adopted": 0,
        "gravity_supplied": GRAVITY_SUPPLIED_CLAIMED,
        "unsupplied": len(UNSUPPLIED_GRAVITY_STRUCTURES),
        "rule_is_dynamics": RULE_IS_DYNAMICS_CLAIMED,
        "naive_uniqueness": NAIVE_UNIQUENESS_CLAIMED,
        "generator_pair_selected": GENERATOR_PAIR_SELECTED,
        "hodge_target_selected": HODGE_TARGET_SELECTED,
        "same_rule_bridge": SAME_RULE_BRIDGE_SUPPLIED,
        "probabilistic_marginal": PROBABILISTIC_MARGINAL_DERIVED_CLAIMED,
        "marginal_is_local": MARGINAL_IS_LOCALLY_COMPUTABLE_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "nonscalar": {twist: SPIN_NONSCALAR_BLOCKS for twist in TWISTS},
        "scalar_nnz": SCALAR_KERNEL_NNZ,
        "dictionary": dict(TWIST_DICTIONARY),
        "verdicts": DICTIONARY_VERDICTS,
        "fork_asymmetry": dict(FORK_ASYMMETRY),
        "seam_equivalence": SEAM_EQUIVALENCE_RESIDUAL,
        "reflection_commutator": (REFLECTION_COMMUTATOR_NNZ,
                                  REFLECTION_COMMUTATOR_ENTRY),
        "hodge_commutator": (HODGE_COMMUTATOR_NNZ, HODGE_COMMUTATOR_ENTRY),
        "gauge_link_residual": GAUGE_LINK_RESIDUAL,
        "gauge_scalar_residual": GAUGE_HODGE_RESIDUAL_SCALAR,
        "gauge_covariant_residual": GAUGE_HODGE_RESIDUAL_COVARIANT,
        "gauge_displacements": GAUGE_RESIDUAL_DISPLACEMENTS,
        "census": dict(LANE_PAIR_CENSUS),
        "pairs": LANE_PAIRS,
        "odd_nonscalar": dict(ODD_EXTENT_NONSCALAR),
        "even_nonscalar": dict(EVEN_EXTENT_NONSCALAR),
        "odd_block": ODD_WRAP_BLOCK,
        # D
        "cell_rank": CELL_COEFFICIENT_RANK,
        "cell_augmented": CELL_AUGMENTED_RANK,
        "cell_dimension": CELL_AFFINE_DIMENSION,
        "cell_count": CELL_SOLUTION_COUNT,
        "parity_ranks": dict(ANCHOR_PARITY_RANKS),
        "replacement_certificate": TARGET_REPLACEMENT_CERTIFICATE,
        "replacement_cases": TARGET_REPLACEMENT_CASES,
        "mismatch_count": CELL_MISMATCH_COUNT,
        "mismatch_positions": (CELL_SIGN_POSITION,),
        "sign_opposite": CELL_SIGN_IS_OPPOSITE,
        "repair_residual": DIRECTED_REPAIR_RESIDUAL,
        "repair_cp_residual": DIRECTED_REPAIR_CP_RESIDUAL,
        "general_rank": GENERAL_RANK,
        "general_dimension": GENERAL_AFFINE_DIMENSION,
        "general_word_residual": GENERAL_WORD_RESIDUAL,
        # E
        "antidiagonal_forced": ANTIDIAGONAL_FORCED,
        "reduced_condition": REDUCED_CONDITION,
        "real_solutions": REAL_TRIPLE_SOLUTIONS,
        "real_triple_exists": REAL_TRIPLE_EXISTS,
        "isy_square": ISY_SQUARE,
        "odd_dimension_det_sign": ODD_DIMENSION_DETERMINANT_SIGN,
        "odd_dimension_obstruction": ODD_DIMENSION_OBSTRUCTION,
        "lift_squares": LIFT_SQUARE_RESIDUALS,
        "lift_anticommutators": LIFT_ANTICOMMUTATORS,
        "rotations": PROPER_ROTATIONS,
        "nullities": (INTERTWINER_NULLITY,),
        "determinants": SPIN_DETERMINANTS,
        "gram_scalars": SPIN_GRAM_SCALARS,
        "conjugation_residual": SPIN_CONJUGATION_RESIDUAL,
        # F
        "bench_metadata": (BENCH_TAG, BENCH_N, BENCH_T, BENCH_CORE,
                           BENCH_TSTAR, BENCH_LX),
        "site_rows": BENCH_SITE_ROWS,
        "moved_components": FAR_MOVED_COMPONENTS,
        "conditional_locality": CONDITIONAL_LOCALITY_HOLDS,
        "schur_residuals": SCHUR_RESIDUALS,
        "environment_size": ENVIRONMENT_SIZE,
        "local_residuals": LOCAL_BLOCK_RESIDUALS,
        "support_slots": COUPLING_SUPPORT_SLOTS,
        "profile": BASE_PROFILE,
        "profile_residual": PROFILE_RESIDUAL,
        "correction_nnz": ENVIRONMENT_CORRECTION_NNZ,
        # G
        "instance_scope": len(INSTANCE_SCOPE),
        "gaussian_derived": GAUSSIAN_INTERPRETATION_DERIVED,
        "local_only_defect": MARGINAL_LOCAL_ONLY_DEFECT,
        "local_only_moved": LOCAL_ONLY_MOVED_COMPONENTS,
        "correction_support": ENVIRONMENT_CORRECTION_SUPPORT,
        "counterexample_matches": NON_CLIFFORD_LANE_SIGNS_MATCH,
        "counterexample_is_clifford": NON_CLIFFORD_IS_CLIFFORD,
        "counterexample_temporal": NON_CLIFFORD_TEMPORAL,
        "counterexample_spatial": NON_CLIFFORD_SPATIAL,
        "finite_instances": FINITE_INSTANCE_COUNT,
        "rational_shears": len(RATIONAL_SHEARS),
        # H
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
        "float_literals": 0,
        "imported_floats": 0,
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
    elif mutation == "claim_rule_is_dynamics":
        # THE FIRST MISREAD: a site-independent Clifford RULE is asserted to be
        # a dynamical law.  It is two fixed real 2 x 2 matrices.
        claims["rule_is_dynamics"] = True
    elif mutation == "claim_naive_uniqueness":
        claims["naive_uniqueness"] = True
    elif mutation == "claim_probabilistic_marginal_derived":
        # THE BLOCK IDENTITY PROMOTED TO A PROBABILITY STATEMENT: the Gaussian
        # reading is asserted to be re-derived here.  No gate touches it.
        claims["probabilistic_marginal"] = True
    elif mutation == "claim_generic_parameter_theorem":
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_spin_diagonalisation":
        # THE SHADOW DENIED: the covariant kernel is asserted NOT to
        # spin-diagonalise on the committed extent, which would make the whole
        # identification a coincidence of one twist.
        claims["nonscalar"] = {twist: (1 if twist == (-1, 1) else 0)
                               for twist in TWISTS}
    elif mutation == "break_twist_dictionary":
        claims["dictionary"] = dict(TWIST_DICTIONARY)
        claims["dictionary"][(-1, 1)] = (False, True, False)
    elif mutation == "break_seam_wrap_fork":
        claims["fork_asymmetry"] = {"seam": 160, "wrap": 160}
    elif mutation == "break_gauge_hodge_defect":
        # THE FENCE REMOVED: the kernel gauge is asserted to be a gauge of the
        # WHOLE construction.  It moves the Hodge at 96 covariant entries.
        claims["gauge_covariant_residual"] = 0
        claims["gauge_scalar_residual"] = 0
    elif mutation == "break_lane_pair_census":
        # THE SUPERSEDED COUNT: the stated-power census is asserted to be four.
        # It is six; four is the parity-reset count under the weaker predicate.
        claims["census"] = dict(LANE_PAIR_CENSUS)
        claims["census"][("stated", "lane")] = 4
    elif mutation == "break_odd_extent_obstruction":
        claims["odd_nonscalar"] = {(8, 3): 0, (7, 4): 0}
    # --- D ----------------------------------------------------------------
    elif mutation == "break_cell_uniqueness":
        claims["cell_rank"] = 15
        claims["cell_dimension"] = 1
        claims["cell_count"] = 0
    elif mutation == "break_cell_sign_location":
        # THE LOCATED SIGN MOVED: the lone disagreement is asserted to sit at
        # (2, 1).  It sits at (1, 2), and the direction is the content.
        claims["mismatch_positions"] = ((2, 1),)
    elif mutation == "claim_target_rank_selects_hodge":
        claims["replacement_cases"] = 0
    # --- E ----------------------------------------------------------------
    elif mutation == "break_no_real_triple":
        # THE OBSTRUCTION DELETED: a real 2 x 2 triple is asserted to exist,
        # which would put the whole rule on M2(R) and make the 4 x 4 lift
        # unnecessary.  The reduced condition b^2 + d^2 = 0 refutes it.
        claims["real_triple_exists"] = True
        claims["real_solutions"] = 1
    elif mutation == "break_four_by_four_triple":
        claims["lift_anticommutators"] = (0, 0, 4)
    elif mutation == "break_cubic_covariance":
        # THE COVARIANCE OVERSTATED IN ITS ARITHMETIC FORM: the intertwiner
        # systems are asserted to have nullity 1, which would leave no room for
        # the rational rescaling that makes the determinant certificate work.
        claims["nullities"] = (1,)
        claims["rotations"] = 12
    # --- F ----------------------------------------------------------------
    elif mutation == "break_bench_metadata":
        claims["bench_metadata"] = (BENCH_TAG, BENCH_N, BENCH_T, BENCH_CORE,
                                    4, BENCH_LX)
    elif mutation == "break_conditional_locality":
        # THE PREMISE INVERTED: W9 is asserted to be conditionally local, which
        # is the claim this stage refutes.  All four far records move all four
        # weights by exact nonzero rationals.
        claims["conditional_locality"] = True
        claims["moved_components"] = (0, 0, 0, 0)
    elif mutation == "break_schur_identity":
        claims["schur_residuals"] = (0, 0, 4)
    elif mutation == "break_local_block_invariance":
        # THE LOCALITY OF THE LAW DENIED: the far records are asserted to move
        # the local blocks too, which would leave nothing local to identify.
        claims["local_residuals"] = ((0, 0, 0), (0, 1, 0),
                                     (0, 0, 0), (0, 0, 0))
    elif mutation == "break_end_to_end_profile":
        claims["profile_residual"] = (0, 0, 0, 1)
    elif mutation == "break_far_dependence_location":
        claims["correction_nnz"] = (1, 4, 5, 0)
    # --- G ----------------------------------------------------------------
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 1
    elif mutation == "claim_marginal_is_local":
        # THE TWO HALVES CONFLATED: the marginal is asserted computable from the
        # local blocks alone.  Dropping the environment correction changes the
        # site block at 8 entries and moves all four weights.
        claims["marginal_is_local"] = True
        claims["local_only_defect"] = 0
    elif mutation == "claim_selection_bridges_supplied":
        claims["hodge_target_selected"] = True
        claims["same_rule_bridge"] = True
    elif mutation == "break_finite_instance_scope":
        claims["finite_instances"] = 0
    # --- H ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    elif mutation == "break_float_absence":
        claims["float_literals"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    kernel = facts.kernel
    cell = facts.cell
    lift = facts.lift
    bench = facts.bench
    other = facts.counterexample

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both parent artifacts are "
        f"content-identical at it and in the worktree, the stale pin "
        f"{STALE_PARENT_COMMIT[:12]} is a real ancestor carrying NEITHER, both "
        f"machinery imports are landed, and {authority.inputs_readable} of "
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
        "B-3", "THE WORD *RULE* IS SCOPED BEFORE THE FIRST NUMERAL: it names "
        "a pair of fixed real 2 x 2 matrices attached to the two lattice "
        "directions -- A = sx and B = -sz -- and names NO dynamics, NO "
        "semigroup, NO generator, NO evolution and NO continuum field equation",
        claims["rule_is_dynamics"] is False)
    checks.check(
        "B-4", f"NO GENERATOR PAIR IS SELECTED: the exact admitted-pair "
        f"census contains {len(kernel.pairs)} ordered pairs, all reproduce the "
        f"lane signs, and an additional rational period-two frame also "
        f"reproduces them ({other.lane_signs_match}) while being non-Clifford "
        f"({not other.is_clifford})",
        claims["naive_uniqueness"] is False
        and claims["generator_pair_selected"] is False
        and len(kernel.pairs) == 6)
    checks.check(
        "B-5", "THE WORD *MARGINAL* IS SCOPED: it names an exact "
        "block/covariance identity between the site block of Q^-1 and the "
        "inverse Schur complement.  The PROBABILISTIC reading uses the "
        "surrounding Gaussian interpretation, which NO gate here re-derives -- "
        "and the separate fence that the marginal is not LOCALLY COMPUTABLE is "
        "measured in gate G-3, so neither statement leans on the other",
        claims["probabilistic_marginal"] is False)
    checks.check(
        "B-6", "NO GENERIC-PARAMETER THEOREM AND NO CONTINUUM LIMIT: what is "
        "established is a set of exact finite-instance results together with "
        "generic linear algebra over QQ and QQ(c, v), and five finite "
        "instances are not a parameter space and not a limit",
        claims["generic_parameter_theorem"] is False
        and claims["continuum_limit"] is False)
    checks.check(
        "B-7", f"THE READINGS ARE READINGS: {claims['readings']} of them are "
        f"enumerated as readings, readings_licensed = "
        f"{claims['readings_licensed']}, and EVERY NEGATIVE HERE IS NON-SUPPLY "
        f"WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the "
        f"cycle-913 caution, carried verbatim, with nothing registered and "
        f"nothing adopted",
        facts.readings == claims["readings"]
        and claims["readings_licensed"] is False
        and not REGISTERED_OBJECTS and not ADOPTED_OBJECTS
        and claims["registered"] == 0 and claims["adopted"] == 0)

    # --- C: S2, THE KERNEL IDENTIFICATION -----------------------------------
    checks.check(
        "C-1", f"THE LANE KERNEL IS A SPIN-DIAGONALISED SHADOW: on "
        f"Z_{BENCH_EXTENT[0]} x Z_{BENCH_EXTENT[1]}, the committed extent, the "
        f"covariant kernel built from the SITE-INDEPENDENT couplings A = sx and "
        f"B = -sz is exactly spin-diagonalised by "
        f"Omega(t, x) = gamma_t^t gamma_x^x, with "
        f"{claims['nonscalar'][(1, 1)]} non-scalar 2 x 2 blocks at ALL FOUR "
        f"wrap twists and {claims['scalar_nnz']} nonzero scalar entries -- "
        f"four directed links at each of the {BENCH_EXTENT[0] * BENCH_EXTENT[1]}"
        f" sites",
        kernel.nonscalar == claims["nonscalar"]
        and kernel.scalar_nnz == claims["scalar_nnz"])
    checks.check(
        "C-2", f"THE TEMPORAL-TWIST DICTIONARY IS EXACT IN "
        f"{claims['verdicts']} VERDICTS, BY SIGN PROPAGATION AND NOT BY "
        f"SEARCH: diag(eps) Sc diag(eps) = KL exactly, the (+, +) twist "
        f"reaching the PERIODIC lane kernel alone, the (-, +) twist reaching "
        f"BOTH the wrap AND the one-edge seam convention, and the two "
        f"spatially twisted kernels reaching none of the three",
        kernel.dictionary == claims["dictionary"]
        and kernel.verdicts == claims["verdicts"]
        and kernel.dictionary[(-1, 1)] == (False, True, True))
    checks.check(
        "C-3", f"AND THE LANDED SEAM/WRAP FORK COMES BACK DIGIT FOR DIGIT: on "
        f"Z_{FORK_EXTENT[0]} x Z_{FORK_EXTENT[1]} at m = {FORK_MASS}, "
        f"c = {FORK_SHEAR} and unit volume, with d_K = P1 K P0 + P2 K P1, "
        f"D_s = A_s - Ps A_s Ps and Q = m H + H D_s - D_s^T H, "
        f"nnz(Q_seam - Q_seam^T) = {claims['fork_asymmetry']['seam']} and "
        f"nnz(Q_wrap - Q_wrap^T) = {claims['fork_asymmetry']['wrap']}",
        kernel.fork_asymmetry == claims["fork_asymmetry"])
    checks.check(
        "C-4", f"THE KERNEL GAUGE IS NOT A GAUGE OF THE WHOLE CONSTRUCTION: "
        f"the wrap-to-seam sign E is a genuine kernel equivalence at "
        f"nnz(E K_wrap E - K_seam) = {claims['seam_equivalence']}, and yet "
        f"it has nnz([E, Ps]) = "
        f"{claims['reflection_commutator'][0]} with the entry "
        f"{claims['reflection_commutator'][1]} at "
        f"{REFLECTION_COMMUTATOR_CELLS}, nnz([E, H]) = "
        f"{claims['hodge_commutator'][0]} with the entry "
        f"{claims['hodge_commutator'][1]} at {HODGE_COMMUTATOR_CELLS}, and the "
        f"literal stage-2 gauge leaves the LINK residual "
        f"{claims['gauge_link_residual']} while leaving a HODGE residual of "
        f"EXACTLY {claims['gauge_covariant_residual']} covariant entries "
        f"({claims['gauge_scalar_residual']} scalar), each exactly b/2 on a "
        f"cell diagonal {claims['gauge_displacements']} whose endpoint gauge "
        f"product is -1",
        kernel.seam_equivalence == claims["seam_equivalence"]
        and kernel.reflection_commutator == claims["reflection_commutator"]
        and kernel.hodge_commutator == claims["hodge_commutator"]
        and kernel.gauge_link_residual == claims["gauge_link_residual"]
        and kernel.gauge_scalar_residual == claims["gauge_scalar_residual"]
        and kernel.gauge_covariant_residual
        == claims["gauge_covariant_residual"]
        and kernel.gauge_displacements == claims["gauge_displacements"]
        and kernel.gauge_uniform and kernel.gauge_endpoints)
    checks.check(
        "C-5", f"THE LANE-PAIR CENSUS IS "
        f"{claims['census'][('stated', 'lane')]} AND NOT FOUR: with the STATED "
        f"integer powers Omega = G1^t G2^x and the true lane test c_t = 1, "
        f"c_x = (-1)^t, exactly {claims['census'][('stated', 'lane')]} ordered "
        f"pairs drawn from sx, sz and i sy work; the parity-reset powers give "
        f"{claims['census'][('parity', 'lane')]} under the same test and "
        f"{claims['census'][('parity', 'scout')]} under the weaker "
        f"t-alternation predicate, so four is the signature of two independent "
        f"defects and not a count of solutions",
        kernel.census == claims["census"] and kernel.pairs == claims["pairs"])
    checks.check(
        "C-6", f"THE FOUR DECLARED EXTENTS HAVE AN EXACT PARITY CONTRAST: the "
        f"two odd extents leave {claims['odd_nonscalar']} non-scalar blocks "
        f"while the two even extents leave {claims['even_nonscalar']}, with "
        f"the exhibited "
        f"wrap block Omega(0, 2)^T (B/2) Omega(0, 0) = {claims['odd_block']} "
        f"not scalar",
        kernel.odd_nonscalar == claims["odd_nonscalar"]
        and kernel.even_nonscalar == claims["even_nonscalar"]
        and kernel.odd_block == tuple(
            tuple(sp.sympify(v) for v in row) for row in claims["odd_block"])
        and all(v > 0 for v in claims["odd_nonscalar"].values()))

    # --- D: S3, TARGET-CONDITIONAL CELL ENCODING -----------------------------
    checks.check(
        "D-1", f"THE PREIMAGE OF A DECLARED TARGET IS UNIQUE: the cell "
        f"equation Psi_cell^T CP Psi_cell = shear_hodge(c, v) tensor I_2 "
        f"with the declared words W_ab = sx^dt sz^dx is "
        f"{cell.equations} exact equations in {cell.unknowns} unknowns over "
        f"QQ(c, v), of coefficient rank {claims['cell_rank']}, augmented rank "
        f"{claims['cell_augmented']}, affine solution dimension "
        f"{claims['cell_dimension']} -- with the rank/augmented/dimension "
        f"triple checked at every anchor parity",
        cell.equations == CELL_EQUATIONS and cell.unknowns == CELL_UNKNOWNS
        and cell.coefficient_rank == claims["cell_rank"]
        and cell.augmented_rank == claims["cell_augmented"]
        and cell.affine_dimension == claims["cell_dimension"]
        and cell.solution_count == claims["cell_count"]
        and cell.parity_ranks == claims["parity_ranks"])
    checks.check(
        "D-2", f"AND IT IS THE LANDED SHEAR HODGE UP TO EXACTLY ONE LOCATED "
        f"SIGN: nnz(F - L) = {claims['mismatch_count']} at the position "
        f"{claims['mismatch_positions']}, where F is the NEGATIVE of L, and "
        f"that sign is a DIRECTED WORD-LABEL convention -- replacing the single "
        f"word W_12 by -sx sz gives F' = L at residual "
        f"{claims['repair_residual']} with the CP matrix itself unchanged at "
        f"residual {claims['repair_cp_residual']}",
        cell.mismatch_count == claims["mismatch_count"]
        and cell.mismatch_positions == claims["mismatch_positions"]
        and cell.sign_opposite is claims["sign_opposite"]
        and cell.repair_residual == claims["repair_residual"]
        and cell.repair_cp_residual == claims["repair_cp_residual"])
    checks.check(
        "D-3", f"THE RANK DOES NOT SELECT THE TARGET: two unrelated target "
        f"matrices across four anchors give {claims['replacement_cases']} "
        f"certificates equal to {claims['replacement_certificate']}; the "
        f"general 8 x 8 congruence also has automatic rank "
        f"{claims['general_rank']} and affine dimension "
        f"{claims['general_dimension']}.  These are invertible changes of "
        f"coordinates, not a physical target-selection theorem",
        len(cell.replacement_certificates) == claims["replacement_cases"]
        and all(value == claims["replacement_certificate"]
                for value in cell.replacement_certificates)
        and cell.general_rank == claims["general_rank"]
        and cell.general_affine_dimension == claims["general_dimension"]
        and cell.general_word_residual == claims["general_word_residual"])

    # --- E: S4, THE Cl(3,0) LIFT --------------------------------------------
    checks.check(
        "E-1", f"THERE IS NO REAL 2 x 2 TRIPLE, AND THE PROOF IS A REDUCTION "
        f"AND NOT A SEARCH: after the first involution is diagonalised to "
        f"diag(1, -1), anticommutation forces the other two ANTIDIAGONAL "
        f"({claims['antidiagonal_forced']}); the squares give b c = 1 and "
        f"d e = 1; the anticommutator gives b e + c d = 0; substituting "
        f"c = 1/b, e = 1/d and multiplying by b d yields EXACTLY "
        f"{claims['reduced_condition']} = 0, which over R forces b = d = 0 and "
        f"contradicts b c = d e = 1 -- the real solution set of the full system "
        f"has {claims['real_solutions']} members.  The near miss is exhibited: "
        f"(i sy)^2 = {claims['isy_square']}, NOT +I_2",
        lift.antidiagonal_forced is claims["antidiagonal_forced"]
        and lift.reduced_condition == claims["reduced_condition"]
        and lift.real_solutions == claims["real_solutions"]
        and claims["real_triple_exists"] is False
        and lift.isy_square == tuple(
            tuple(sp.Integer(v) for v in row) for row in claims["isy_square"])
        and lift.square_conditions == SQUARE_CONDITIONS
        and lift.anticommutator_condition == ANTICOMMUTATOR_CONDITION)
    checks.check(
        "E-2", f"THE MINIMAL REAL HOME IS {LIFT_DIMENSION} x "
        f"{LIFT_DIMENSION}: the 2 x 2 obstruction is supplemented by the "
        f"odd-dimensional determinant sign {claims['odd_dimension_det_sign']} "
        f"for AB=-BA with invertible A,B, excluding dimension 3; the exhibit "
        f"G1 = sx (x) I_2, G2 = sz (x) sx and G3 = sz (x) sz have square "
        f"residuals {claims['lift_squares']} and pairwise anticommutators "
        f"{claims['lift_anticommutators']}",
        lift.odd_dimension_det_sign == claims["odd_dimension_det_sign"]
        and lift.odd_dimension_obstruction
        is claims["odd_dimension_obstruction"]
        and lift.square_residuals == claims["lift_squares"]
        and lift.anticommutators == claims["lift_anticommutators"])
    checks.check(
        "E-3", f"AND ALL {claims['rotations']} PROPER CUBIC ROTATIONS ARE "
        f"SPIN-IMPLEMENTED, WITH INVERTIBILITY CERTIFIED BY AN EXACT "
        f"DETERMINANT AND NEVER BY A NUMERICAL RANK: the det = +1 signed "
        f"permutations number {claims['rotations']}, each intertwiner system "
        f"S G_i - (sum_j R_ij G_j) S = 0 has nullity {claims['nullities']}, "
        f"the primitive integer member selected in each nullspace has "
        f"S^T S = lambda I_4 for lambda in {claims['gram_scalars']} and "
        f"det S = lambda^2 in {claims['determinants']} -- both nonzero as "
        f"exact integers -- and the total residual of "
        f"S G_i S^-1 - sum_j R_ij G_j over all rotations and generators is "
        f"{claims['conjugation_residual']}",
        lift.rotations == claims["rotations"]
        and lift.nullities == claims["nullities"]
        and lift.determinants == tuple(
            sp.Integer(v) for v in claims["determinants"])
        and lift.gram_scalars == tuple(
            sp.Integer(v) for v in claims["gram_scalars"])
        and lift.conjugation_residual == claims["conjugation_residual"]
        and all(v != 0 for v in claims["determinants"])
        and all(sp.Integer(d) == sp.Integer(g) ** 2
                for d, g in zip(claims["determinants"],
                                claims["gram_scalars"])))

    # --- F: IMPORTED BLOCK 171 FINITE IDENTITIES -----------------------------
    checks.check(
        "F-1", f"THE BENCH IS BLOCK 171's OWN AND IS READ THROUGH ITS OWN Site "
        f"AND Env CLASSES RATHER THAN REBUILT: "
        f"Site('{claims['bench_metadata'][0]}', {BENCH_COVER}, {BENCH_LX}) "
        f"gives N = {claims['bench_metadata'][1]}, T = "
        f"{claims['bench_metadata'][2]}, c = {claims['bench_metadata'][3]}, "
        f"tstar = {claims['bench_metadata'][4]}, lx = "
        f"{claims['bench_metadata'][5]} and site rows {claims['site_rows']}",
        (bench.tag, bench.size, bench.width, bench.core, bench.tstar,
         bench.extent) == claims["bench_metadata"]
        and bench.site_rows == claims["site_rows"])
    checks.check(
        "F-2", f"AND ITS LANDED W9 PROFILE IS NOT CONDITIONALLY LOCAL: with the "
        f"base record {{{BASE_RECORD_CELL}: 0}} held fixed, EACH of the four "
        f"far additions {FAR_CELLS} moves {claims['moved_components']} of the "
        f"four normalised weights by EXACT NONZERO rationals, so "
        f"conditional_locality = {claims['conditional_locality']} is a MEASURED "
        f"refutation and not a floating-point artifact",
        bench.moved_components == claims["moved_components"]
        and bench.all_moves_nonzero
        and claims["conditional_locality"] is False
        and all(v == bench.extent for v in claims["moved_components"]))
    checks.check(
        "F-3", f"THE MARGINALISATION IDENTITY IS EXACT AND BOTH INVERSES ARE "
        f"CERTIFIED RATHER THAN ASSUMED: over QQ_I, nnz(Q Q^-1 - I_{BENCH_N}) "
        f"= {claims['schur_residuals'][0]}, nnz(Q[rr,rr] Q[rr,rr]^-1 - "
        f"I_{claims['environment_size']}) = {claims['schur_residuals'][1]}, and "
        f"(Q^-1)[ss,ss] = (Q[ss,ss] - Q[ss,rr] Q[rr,rr]^-1 Q[rr,ss])^-1 ENTRY "
        f"FOR ENTRY at {claims['schur_residuals'][2]}",
        bench.schur_residuals == claims["schur_residuals"]
        and bench.environment_size == claims["environment_size"])
    checks.check(
        "F-4", f"THE LOCAL DATA ARE EXACTLY LOCAL, AND THEIR DIRECT SUPPORT IS "
        f"TWO SLOTS: under ALL FOUR far additions the triple "
        f"(nnz(dQ[ss,ss]), nnz(dQ[ss,rr]), nnz(dQ[rr,ss])) is "
        f"{claims['local_residuals']}, and the direct support of Q[ss,rr] and "
        f"of Q[rr,ss] is exactly the slots {claims['support_slots']} = "
        f"{{tstar - 1, (tstar + 1) mod T}}",
        bench.local_residuals == claims["local_residuals"]
        and bench.support_slots == claims["support_slots"]
        and bench.inward_support_slots == claims["support_slots"])
    checks.check(
        "F-5", f"WITHIN BLOCK 171'S OWN BENCH THE RECONSTRUCTION IS END TO "
        f"END: Block 171's own "
        f"Env.profile('{BENCH_GRAM}', tstar) equals the normalised diagonal of "
        f"herm(Schur^-1) at componentwise residual "
        f"{claims['profile_residual']} on the base-record instance, and the "
        f"landed profile is the declared exact 4-tuple",
        bench.profile_residual == tuple(
            sp.Integer(v) for v in claims["profile_residual"])
        and bench.profile == claims["profile"])
    checks.check(
        "F-6", f"AND THE FAR DEPENDENCE IS LOCATED RATHER THAN NAMED: the "
        f"environment correction Q[ss,rr] Q[rr,rr]^-1 Q[rr,ss] changes under "
        f"the four far cells at EXACT nonzero-entry counts "
        f"{claims['correction_nnz']}, so every bit of the movement in F-2 sits "
        f"in that one term",
        bench.correction_nnz == claims["correction_nnz"]
        and all(v > 0 for v in claims["correction_nnz"]))

    # --- G: THE SCOPE QUALIFICATIONS ----------------------------------------
    checks.check(
        "G-1", f"THE FAR-DEPENDENCE PATTERN IS INSTANCE-SCOPED, AND THE SCOPE "
        f"IS ENUMERATED RATHER THAN IMPLIED: {claims['instance_scope']} "
        f"declared restrictions -- the committed {BENCH_TAG} bench, the "
        f"xgraded carrier, the stated base record and four class-0 changes at "
        f"slot 2 -- and NOT every extent, NOT every carrier, NOT every far "
        f"slot and NOT every record value",
        len(INSTANCE_SCOPE) == claims["instance_scope"]
        and len(FAR_CELLS) == 4
        and all(cell_index[0] == 2 for cell_index in FAR_CELLS))
    checks.check(
        "G-2", f"'EXACT MARGINAL' IS AN EXACT BLOCK/COVARIANCE IDENTITY AND "
        f"NOT A RE-DERIVED PROBABILISTIC MARGINAL: what is gated is the site "
        f"block of Q^-1, herm and diagonal normalisation, at residuals "
        f"{claims['schur_residuals']} and {claims['profile_residual']}; the "
        f"Gaussian interpretation that turns it into a probability statement "
        f"is NOT re-derived here (gaussian_derived = "
        f"{claims['gaussian_derived']})",
        claims["gaussian_derived"] is False
        and bench.schur_residuals == SCHUR_RESIDUALS
        and bench.profile_residual == tuple(
            sp.Integer(v) for v in PROFILE_RESIDUAL))
    checks.check(
        "G-3", f"THE LAW IS LOCAL AND THE OBSERVED STATISTICS ARE NOT, AND THE "
        f"NOTE NEVER CONFLATES THEM: the marginal uses the GLOBAL environment "
        f"inverse -- the environment correction itself has "
        f"{claims['correction_support']} nonzero entries, dropping it changes "
        f"the site block of the marginal at {claims['local_only_defect']} "
        f"entries and moves {claims['local_only_moved']} of the four weights -- "
        f"so marginal_is_local = {claims['marginal_is_local']}",
        claims["marginal_is_local"] is False
        and bench.local_only_defect == claims["local_only_defect"]
        and bench.local_only_moved == claims["local_only_moved"]
        and bench.correction_support == claims["correction_support"]
        and claims["local_only_defect"] > 0)
    checks.check(
        "G-4", f"THE THREE SELECTION BRIDGES ARE NOT SUPPLIED: generator-pair "
        f"selection = {claims['generator_pair_selected']}, imported-Hodge "
        f"target selection = {claims['hodge_target_selected']}, and a bridge "
        f"from A/B/Omega to Block 171's Q = {claims['same_rule_bridge']}.  The "
        f"additional rational "
        f"period-two frame S = {NON_CLIFFORD_FRAME} gives A' = "
        f"{claims['counterexample_temporal']} and B' = "
        f"{claims['counterexample_spatial']} reproducing the same lane signs "
        f"({claims['counterexample_matches']}) with (A')^2 = "
        f"{NON_CLIFFORD_TEMPORAL_SQUARE}, (B')^2 = "
        f"{NON_CLIFFORD_SPATIAL_SQUARE} and A'B' + B'A' = "
        f"{NON_CLIFFORD_ANTICOMMUTATOR}, so is_clifford = "
        f"{claims['counterexample_is_clifford']}; and every word here names an "
        f"exact result on {claims['finite_instances']} finite instances and "
        f"{claims['rational_shears']} rational shear, never a continuum",
        claims["generator_pair_selected"] is False
        and claims["hodge_target_selected"] is False
        and claims["same_rule_bridge"] is False
        and other.lane_signs_match is claims["counterexample_matches"]
        and other.is_clifford is claims["counterexample_is_clifford"]
        and claims["counterexample_is_clifford"] is False
        and other.period_two
        and other.temporal == tuple(
            tuple(sp.Integer(v) for v in row)
            for row in claims["counterexample_temporal"])
        and other.spatial == tuple(
            tuple(sp.Integer(v) for v in row)
            for row in claims["counterexample_spatial"])
        and other.temporal_square == tuple(
            tuple(sp.Integer(v) for v in row)
            for row in NON_CLIFFORD_TEMPORAL_SQUARE)
        and other.spatial_square == tuple(
            tuple(sp.Integer(v) for v in row)
            for row in NON_CLIFFORD_SPATIAL_SQUARE)
        and other.anticommutator == tuple(
            tuple(sp.Integer(v) for v in row)
            for row in NON_CLIFFORD_ANTICOMMUTATOR)
        and claims["finite_instances"] == len(FINITE_INSTANCES) + 1
        and claims["rational_shears"] == len(RATIONAL_SHEARS))

    # --- H: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE -------------------
    checks.check(
        "H-1", f"the note is present at {NOTE_PATH.name} and all five N5 "
        f"resolution lines appear there byte-for-byte",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "H-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn a hundred-digit nonzero record movement into a "
        f"spurious zero and reinstate the refuted conditional locality",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "H-3", f"and {claims['float_literals']} float literals appear in that "
        f"same source, MEASURED by an AST walk rather than by a text search, "
        f"while the LANDED shear_hodge returns {claims['imported_floats']} "
        f"sympy Float atoms at every argument pair this runner passes -- Block "
        f"200's correction #99 honoured by measurement rather than by care, "
        f"since 1 / v is a Python division there and a Float compares EQUAL to "
        f"its exact partner",
        facts.float_literals == claims["float_literals"]
        and facts.imported_floats == claims["imported_floats"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    """Keep machine stdout below the repository runner-output ceiling."""
    print("MEASURED")
    print(f"elapsed_ns={elapsed_ns} main={facts.main_head}")
    print(f"authority={facts.authority}")
    print(f"objects=imposed:{facts.imposed},registered:{facts.registered},"
          f"adopted:{facts.adopted}")
    print(f"kernel=nonscalar:{facts.kernel.nonscalar},nnz:"
          f"{facts.kernel.scalar_nnz},dictionary:{facts.kernel.dictionary},"
          f"pairs:{facts.kernel.pairs},finite_parity:"
          f"{facts.kernel.odd_nonscalar}/{facts.kernel.even_nonscalar}")
    print(f"cell=rank:{facts.cell.coefficient_rank}/"
          f"{facts.cell.augmented_rank},dim:{facts.cell.affine_dimension},"
          f"anchors:{facts.cell.parity_ranks},replacements:"
          f"{facts.cell.replacement_certificates},sign:"
          f"{facts.cell.mismatch_positions},general:{facts.cell.general_rank}")
    print(f"lift=odd_sign:{facts.lift.odd_dimension_det_sign},"
          f"squares:{facts.lift.square_residuals},anti:"
          f"{facts.lift.anticommutators},rotations:{facts.lift.rotations},"
          f"residual:{facts.lift.conjugation_residual}")
    print(f"block171=schur:{facts.bench.schur_residuals},local:"
          f"{facts.bench.local_residuals},profile:"
          f"{facts.bench.profile_residual},far:{facts.bench.correction_nnz}")
    print(f"selection=generator:false,target:false,same_rule_bridge:false; "
          f"counterexample=lane:{facts.counterexample.lane_signs_match},"
          f"clifford:{facts.counterexample.is_clifford}")
    print(f"hygiene=nsimplify:{facts.nsimplify_calls},float_literals:"
          f"{facts.float_literals},imported_float_atoms:{facts.imported_floats}")


N5_FENCE = (
    "N5: per_element: The declared matrix pair is an exact finite exhibit, not a selected dynamical or physical rule; zero objects are registered or adopted.\n"
    "N5: per_site: The twist dictionary is gated only on Z_6 x Z_4, and the even/odd contrast is reported only for the four measured extents.\n"
    "N5: per_mode: Rank-16 cell inversion is target-conditional encodability; two unrelated replacement targets receive the same exact certificate, so no Hodge target is selected.\n"
    "N5: per_block: The real Cl(3,0) exhibit and the imported Block 171 Schur identities remain separate exact results because no same-rule bridge is supplied.\n"
    "N5: lattice_wide: The six-pair census and rational counterexample defeat uniqueness from lane signs alone; no generic-parameter, continuum, gravity, or Nature claim is made."
)


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
