#!/usr/bin/env python3
"""BLOCK 209 -- FINITE THREE-DIRECTION RULE AND CELL-GLUING DIAGNOSTICS.

This runner preserves exact parity scalarization, finite literal and shape-only
gluing ranks, the uniform flat solution, one reciprocal curved counterexample,
and a declared exterior-algebra matrix candidate D3(g,V).  D3 is a standard
metric-induced construction conditional on the chosen grading, wedge basis, and
normalization split; the framework does not select it uniquely.

The Schur-complement restriction identity is measured only on the three origin
faces.  At the opposite faces the global degree grading changes and the same
target fails in five exact entries per face.  The counterexample is explicit,
and no unbuilt local regrading or transport map is assumed.

All claims are finite exact algebra, proposed_retained only, with no spacetime,
dynamics, gravity, continuum, or physical-selection conclusion.  Thirty-six
claim-only mutations each fail exactly their mapped family.
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

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORT, LANDED, AND IT IS EXACTLY ONE OBJECT: Block 105's
# shear_hodge(c, v), reached through Block 128's own import of it, so that each
# specified literal plane target in this block is the LANDED one and never a
# rebuild.  The independent checkers deliberately
# reimplemented the same four-by-four form from its printed definition and
# agreed entry for entry; this runner takes the landed route and the note
# records both.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    LANDED_SHEAR_HODGE = b128.block105.shear_hodge
    BENCH_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    LANDED_SHEAR_HODGE = None
    BENCH_IMPORT_LANDED = False
MACHINERY_IMPORT_LANDED = BENCH_IMPORT_LANDED

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 202 is the commit this block's
# branch is cut from; its note and its runner both exist at PARENT_COMMIT and
# NEITHER exists at STALE_PARENT_COMMIT, which is the Block 201 tip.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_"
    "BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_record_pinning_mixture_diagnostics_"
    "2026_08_26.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "eb9b58aa1cf91985f82f82d7f1b912ed2eff1b41",
    "c1af544037305a8b9d8455bca7d8254cdcbad670",
)
# THE CONSTRUCTION AUTHORITY.  Block 128 supplies the import path to Block
# 105's landed shear_hodge, which is the only landed object this block reads.
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
BLOCK128_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_RECORD_PINNING_MIXTURE_DIAGNOSTICS_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_record_pinning_mixture_diagnostics_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_RULE_IDENTIFICATION_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
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
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block202-"
              "record-pinning-mixture-diagnostics-20260826")
PARENT_COMMIT = "141b9e8da04319eb2f31c53389de6edd0cf723bf"
# The Block 201 tip: a real ancestor of HEAD that predates Block 202 and
# therefore carries NEITHER parent artifact.
STALE_PARENT_COMMIT = "d460d14f89c38c4c2a8774fc62cc103d0ae706a1"
# A real but superseded authority head, carried forward from Block 202's record.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_geometry_is_spacetime",
    "claim_gluing_is_dynamics",
    "claim_rigidity_is_universal",
    "claim_continuum_theorem",
    "claim_readings_licensed",
    "break_covariant_rule_algebra",
    "break_even_scalarization",
    "break_parity_obstruction",
    "break_sign_matrix",
    "break_three_face_literal",
    "break_convention_invariance",
    "break_shape_cross_degree",
    "break_six_face_shape",
    "break_six_face_literal",
    "break_uniform_flat_point",
    "break_reciprocal_solvable",
    "break_positivity_verdict",
    "break_two_form_block",
    "break_gluing_law",
    "break_schur_residual",
    "break_shape_membership",
    "break_three_d_couplings",
    "break_orientation_split",
    "break_scout_grade_fence",
    "claim_schur_equivalence",
    "claim_principle_binds_nature",
    "claim_signs_invariant",
    "claim_landed_corrected",
    "break_instance_scope",
    "drop_n5_fence",
    "break_nsimplify_absence",
    "break_float_absence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "claim_objects_registered": "B",
    "claim_gravity_supplied": "B",
    "claim_geometry_is_spacetime": "B",
    "claim_gluing_is_dynamics": "B",
    "claim_rigidity_is_universal": "B",
    "claim_continuum_theorem": "B",
    "claim_readings_licensed": "B",
    "break_covariant_rule_algebra": "C",
    "break_even_scalarization": "C",
    "break_parity_obstruction": "C",
    "break_sign_matrix": "C",
    "break_three_face_literal": "D",
    "break_convention_invariance": "D",
    "break_shape_cross_degree": "D",
    "break_six_face_shape": "D",
    "break_six_face_literal": "E",
    "break_uniform_flat_point": "E",
    "break_reciprocal_solvable": "E",
    "break_positivity_verdict": "E",
    "break_two_form_block": "F",
    "break_gluing_law": "F",
    "break_schur_residual": "F",
    "break_shape_membership": "F",
    "break_three_d_couplings": "F",
    "break_orientation_split": "F",
    "break_scout_grade_fence": "G",
    "claim_schur_equivalence": "G",
    "claim_principle_binds_nature": "G",
    "claim_signs_invariant": "G",
    "claim_landed_corrected": "G",
    "break_instance_scope": "G",
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
    "THE THREE-DIRECTION COVARIANT RULE, WHICH IS THIS BLOCK's FIRST NEW OBJECT: the couplings A_t = G1/2, A_x = G2/2, A_y = G3/2 built from the pairwise-anticommuting involutions G1 = sx (x) I2, G2 = sz (x) sx, G3 = sz (x) sz, with the staggering Omega(t, x, y) = G1^t G2^x G3^y and the per-link scalarization test Omega(s)^T (G_d/2) Omega(s + e_d), run on the four extents (4,2,2), (4,4,2), (4,4,4) and (4,3,2)",
    "THE CELL SIGN MATRIX AND ITS WORD FORM: the 8 x 8 matrix sigma(a, b) defined by Omega_a Omega_b^T = sigma(a,b) W_ab with W_ab the canonical displacement word G1^dt G2^dx G3^dy, measured at all 64 corner pairs and at all 8 anchor parities, together with the block congruence Psi (T (x) I4) Psi^T for a general symmetric 8 x 8 target",
    "THE LITERAL GLUING SYSTEMS: the three-origin-face and six-origin-plus-opposite-face linear systems that impose on a general symmetric 8 x 8 corner matrix D that each specified face restriction, in the sub-corner order [origin, i2, i1, i1 + i2], equal the LANDED shear_hodge(c_p, v_p) at that face's own moduli -- run at generic independent moduli, at all four order-and-flip convention variants, on the uniform locus, and at the one exhibited reciprocal point (c = 3/5, v0 = 12/25, v1 = 3/4, c1 = 4/5)",
    "THE SHAPE-ONLY GLUING SYSTEMS: the three-face and six-face systems that impose only the shear-Hodge SHAPE on each plane restriction -- the five-entry zero pattern and the equal 1-form diagonals -- and whose solution manifolds are read for their forced-zero and free cross-degree pairings",
    "THE DECLARED STANDARD EXTERIOR-ALGEBRA CANDIDATE D3(g, V): the 8 x 8 symmetric matrix diag(V, V g^-1, E g E / V, 1/V) on the corner-degree sectors with E = diag(1, -1, 1) in the wedge basis beta = (dx^dy, dt^dy, dt^dx), conditional on that grading, wedge basis, and normalization split; the block measures its origin- and opposite-face restrictions separately, its Schur complements, its shape residuals, and its isotropic-locus orientation split without claiming framework selection",
    "BLOCK 105's LANDED 2D CELL FORM shear_hodge(c, v) = diag(v, v g2(c)^-1, 1/v), READ THROUGH BLOCK 128's OWN IMPORT OF IT AND NOT REBUILT: it is the target every literal gluing equation in this block is written against, and no line of this block edits it",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL TWELVE ARE
# FALSE AND STAY FALSE.  FOUR OF THEM CARRY THE TWO INDEPENDENT CHECKERS' OWN
# CORRECTIONS AS CONTENT RATHER THAN AS ERRATA.
GRAVITY_SUPPLIED_CLAIMED = False
GEOMETRY_IS_SPACETIME_CLAIMED = False
GLUING_IS_DYNAMICS_CLAIMED = False
RIGIDITY_IS_UNIVERSAL_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
EQUATIONS_OF_MOTION_CLAIMED = False
SCHUR_EQUIVALENCE_CLAIMED = False
PRINCIPLE_BINDS_NATURE_CLAIMED = False
SIGNED_SHEAR_INVARIANCE_CLAIMED = False
LANDED_CORRECTION_CLAIMED = False
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
# THE THREE WORDS THAT NAME NOTHING ESTABLISHED HERE, DECLARED SO THE NOTE'S
# ABSENCE OF THEM IS A MEASUREMENT AND NOT A PROMISE.
UNNAMED_PHYSICS_WORDS = ("SPACETIME", "CURVATURE", "EINSTEIN")
# THE ONE PHRASE THE SCHUR COMPARISON LICENSES, VERBATIM.
LICENSED_ECHO_PHRASE = "identity-type echo, not a proven equivalence"
READINGS = (
    "Physical-dimensionality reading withdrawn: on four finite extents, every directed link scalarizes when all three extents are even, while exactly eight wrap links in the single odd direction fail. This is an extent-parity fact about one declared staggering on a torus.",
    "Spatial-flatness reading withdrawn: one specified linear system, on the uniform positive-volume locus, has the single solution (c,v)=(0,1). No metric field, curvature, or spacetime is constructed.",
    "Universal positivity no-go withdrawn: at one exhibited nonuniform reciprocal point the degree-1 and degree-2 principal blocks are parameter-free and indefinite. Positivity on the other nonuniform six-face-compatible branches is unclassified.",
    "Record-marginal equivalence withdrawn: the origin-face Schur calculation and the S5 record marginal instantiate an algebraic template, but no carrier map, object identification, or commuting statement is constructed; opposite faces fail the same target.",
    "Nature-level shape verdict withdrawn: relative to the declared positive D3(g,V) candidate family, the equal-diagonal rule rejects generic shears. This block gives no reason those rejected members must be physically admissible.",
    "Generalisation withdrawn: the measurements cover four extents, three origin and three opposite coordinate faces, one reciprocal point, one isotropic-locus analysis, and one landed 2D target—not every extent, convention, branch, or moduli point.",
)

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
CORNERS = tuple((dt, dx, dy) for dt in (0, 1) for dx in (0, 1) for dy in (0, 1))
CORNER_COUNT = 8
CELL_UNKNOWNS = 36

# --- C: THE 2+1D EXTENSION ---------------------------------------------------
DIRECTION_NAMES = ("t", "x", "y")
COUPLING_FORM = ("G1/2", "G2/2", "G3/2")
STAGGERING_FORM = "Omega(t, x, y) = G1^t G2^x G3^y"
GENERATOR_SQUARES_IDENTITY = (True, True, True)
GENERATOR_ANTICOMMUTE = (True, True, True)
ETA_PATTERN = ("1", "(-1)^t", "(-1)^(t+x)")
EVEN_EXTENTS = ((4, 2, 2), (4, 4, 2), (4, 4, 4))
EVEN_SITE_COUNTS = (16, 32, 64)
EVEN_LINK_COUNTS = (48, 96, 192)
EVEN_BAD_COUNTS = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
EVEN_BAD_WRAP_COUNTS = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
EVEN_ETA_HOLDS = (True, True, True)
ODD_EXTENT = (4, 3, 2)
ODD_SITE_COUNT = 24
ODD_BAD_COUNTS = (0, 8, 0)
ODD_BAD_WRAP_COUNTS = (0, 8, 0)
ODD_BAD_TOTAL = 8
ODD_BAD_DIRECTION = 1
ODD_ETA_HOLDS = True
OBSTRUCTION_IS_DIRECTION_LOCAL = True
SIGMA_PAIRS = 64
SIGMA_ANCHORS = 8
SIGMA_WELL_DEFINED = (True,) * 8
SIGMA_VALUES = (-1, 1)
SIGMA_ROWS = (
    (1, 1, 1, -1, 1, -1, -1, -1),
    (1, 1, -1, 1, -1, 1, -1, -1),
    (1, 1, 1, -1, -1, 1, 1, 1),
    (1, 1, -1, 1, 1, -1, 1, 1),
    (1, 1, 1, -1, 1, -1, -1, -1),
    (1, 1, -1, 1, -1, 1, -1, -1),
    (1, 1, 1, -1, -1, 1, 1, 1),
    (1, 1, -1, 1, 1, -1, 1, 1),
)
WORD_FORM_EXACT = True
PSI_ORTHOGONAL = True
PSI_SIZE = 32

# --- D: THE GLUING SYSTEMS ---------------------------------------------------
THREE_FACE_EQUATIONS = 48
THREE_FACE_RANKS = (22, 23)
THREE_FACE_RELATION_COUNT = 5
# THE FIVE FORCED RELATIONS, IN CANONICAL FORM -- numerator, primitive part,
# sign-normalised.  The first two are the EQUAL-VOLUME relations and the last
# three are the EQUAL-SHEAR-SQUARE relations: on the nonsingular domain
# (v_p != 0, c_p^2 != 1) their common zero locus is exactly v_tx = v_ty = v_xy
# together with c_tx^2 = c_ty^2 = c_xy^2.  IT IS A LOCUS AND NOT A POINT, AND
# THE THREE SHEAR SIGNS ARE UNGLUED ALONG IT.
THREE_FACE_RELATIONS = (
    "c_tx**2*v_ty - c_ty**2*v_tx + v_tx - v_ty",
    "c_tx**2*v_xy - c_xy**2*v_tx + v_tx - v_xy",
    "c_ty**2*v_xy - c_xy**2*v_ty + v_ty - v_xy",
    "v_tx - v_ty",
    "v_tx - v_xy",
)
CONVENTION_VARIANTS = 4
CONVENTION_RANKS_IDENTICAL = True
CONVENTION_RELATIONS_IDENTICAL = True
SHAPE3_RANK = 14
SHAPE3_MANIFOLD = 22
SHAPE3_SURVIVOR_COUNT = 24
SHAPE3_CROSS_DEGREE_PAIRS = 22
SHAPE3_CROSS_FORCED_ZERO = 12
SHAPE3_CROSS_FREE = 10
SHAPE3_ONE_FORM_DIAGONALS_EQUAL = True
SHAPE3_TWO_FORM_DIAGONALS_EQUAL = False
SHAPE6_RANK = 22
SHAPE6_MANIFOLD = 14
SHAPE6_SURVIVOR_COUNT = 18
SHAPE6_CROSS_FORCED_ZERO = 18
SHAPE6_CROSS_FREE = 4
SHAPE6_CROSS_FREE_PAIRS = (
    ((0, 0, 0), (1, 1, 1)),
    ((0, 0, 1), (1, 1, 0)),
    ((0, 1, 0), (1, 0, 1)),
    ((0, 1, 1), (1, 0, 0)),
)
SHAPE6_CROSS_FREE_ARE_COMPLEMENTARY = True
SHAPE6_ONE_FORM_DIAGONALS_EQUAL = True
SHAPE6_TWO_FORM_DIAGONALS_EQUAL = True
SHAPE6_WITHIN_DEGREE_FREE = (3, 3)
SHAPE6_PARAMETER_CENSUS = (4, 6, 4)

# --- E: THE RIGIDITY CHAIN ---------------------------------------------------
SIX_FACE_EQUATIONS = 96
SIX_FACE_RANKS = (32, 33)
SIX_FACE_RELATION_COUNT = 16
# THE SIXTEEN, IN CANONICAL FORM.  Four are PER-OFFSET equal-volume relations,
# four are PER-OFFSET equal-shear-square relations, and EIGHT are the
# RECIPROCAL CROSS-OFFSET couplings that tie the two faces of a direction
# together -- the third entry below reads v_tx1 v_ty0 = 1 - c_tx1^2, and it is
# that reciprocity, not the per-offset half, that makes the uniform locus
# collapse.
SIX_FACE_RELATIONS = (
    "c_tx0**2*v_ty0 - c_ty0**2*v_tx0 + v_tx0 - v_ty0",
    "c_tx0**2*v_ty1 + v_tx0 - v_ty1",
    "c_tx0**2*v_xy0 - c_xy0**2*v_tx0 + v_tx0 - v_xy0",
    "c_tx0**2*v_xy1 + v_tx0 - v_xy1",
    "c_tx1**2 + v_tx1*v_ty0 - 1",
    "c_tx1**2 + v_tx1*v_xy0 - 1",
    "c_tx1**2*v_ty1 - c_ty1**2*v_tx1 + v_tx1 - v_ty1",
    "c_tx1**2*v_xy1 - c_xy1**2*v_tx1 + v_tx1 - v_xy1",
    "c_ty0**2*v_tx1 - v_tx1 + v_ty0",
    "c_ty1**2 + v_tx0*v_ty1 - 1",
    "c_xy0**2*v_tx1 - v_tx1 + v_xy0",
    "c_xy1**2 + v_tx0*v_xy1 - 1",
    "v_tx0 - v_ty0",
    "v_tx0 - v_xy0",
    "v_tx1 - v_ty1",
    "v_tx1 - v_xy1",
)
UNIFORM_CONSTRAINT_COUNT = 2
# THE TWO SURVIVING NUMERATORS ON THE UNIFORM LOCUS.  THE QUICK READING SAW
# ONLY THE FIRST.  The second is the one that forbids every curved uniform
# cell, and together they force the flat point.
UNIFORM_CONSTRAINTS = ("c**2 + v**2 - 1", "c**2*v")
UNIFORM_SOLUTION = (0, 1)
UNIFORM_ADMITS_ONLY_FLAT = True
RECIPROCAL_SHEAR = sp.Rational(3, 5)
RECIPROCAL_VOLUME_ZERO = sp.Rational(12, 25)
RECIPROCAL_VOLUME_ONE = sp.Rational(3, 4)
RECIPROCAL_SHEAR_ONE = sp.Rational(4, 5)
RECIPROCAL_RANKS = (32, 32)
RECIPROCAL_FREE_COUNT = 4
RECIPROCAL_FREE_NAMES = ("D07", "D16", "D25", "D34")
DEGREE_ONE_SPECTRUM = ((sp.Rational(-3, 20), 1), (sp.Rational(6, 5), 2))
DEGREE_TWO_SPECTRUM = ((sp.Rational(-5, 4), 1), (sp.Rational(15, 4), 2))
PRINCIPAL_BLOCKS_PARAMETER_FREE = True
CURVED_CELL_EVER_POSITIVE_DEFINITE = False
RIGIDITY_ON_CHECKED_BRANCHES = True

# --- F: THE HONEST CONSTRUCTION AND ITS GLUING LAW ---------------------------
WEDGE_SIGNATURE = (1, -1, 1)
JACOBI_IDENTITY_EXACT = True
TWO_FORM_BLOCK_FORM = "det(g) * Lambda^2(g^-1) / V = J W1^-1 J^T = E g E / V"
TWO_FORM_DIVISION_IS_LOAD_BEARING = True
TWO_FORM_UNDIVIDED_MATCHES_GENERICALLY = False
TWO_FORM_UNDIVIDED_MATCHES_AT_UNIT_VOLUME = True
TOP_IS_DUAL_OF_BOTTOM = True
ORIGIN_RESTRICTION_LAW_EXACT = True
OPPOSITE_RESTRICTION_LAW_EXACT = False
OPPOSITE_RESTRICTION_RESIDUAL_NNZ = (5, 5, 5)
OPPOSITE_REPRESENTATIVE_DEFECTS = (
    sp.Rational(1310, 23159), sp.Rational(2282, 23159),
    sp.Rational(2682, 23159),
)
PLANE_SCALE_FORCED = 1
PLANE_VOLUME_IS_CELL_VOLUME = True
SCHUR_DETERMINANT_IDENTITY = True
PARTIAL_CORRELATION_EXACT_ON_LOCUS = True
PARTIAL_CORRELATION_NEEDS_NORMALISATION = True
LANDED_MATCH_IFF_DECOUPLED = True
ONE_FORM_RESIDUAL_FORM = "kappa_p^2 * V * S_p^-1"
SHAPE_MEMBERSHIP_IFF_EQUAL_MAGNITUDES = True
SHAPE_ZERO_PATTERN_IDENTICAL = 15
EQUAL_DIAGONAL_RESIDUAL_FORM = "V * (c_opp^2 - c_opp'^2) / det g"
THREE_D_COUPLING_COUNT = 3
THREE_D_COUPLING_SIGNS = ("-", "+", "-")
THREE_D_COUPLINGS_INVISIBLE_ON_ORIGIN_FACES = True
THREE_D_COUPLINGS_VISIBLE_ON_OPPOSITE_FACES = True
CROSS_DEGREE_PAIRINGS_ZERO = True
ISOTROPIC_SIGN_PATTERNS = 8
ISOTROPIC_RELATIONS_HOLD = True
ORIENTATION_CLASSES = 2
DETERMINANT_AT_POSITIVE_ORIENTATION = "(1 - kappa)^2 * (1 + 2*kappa)"
DETERMINANT_AT_NEGATIVE_ORIENTATION = "(1 + kappa)^2 * (1 - 2*kappa)"
KAPPA_BOUND_POSITIVE = sp.Integer(1)
KAPPA_BOUND_NEGATIVE = sp.Rational(1, 2)
POSITIVITY_DOMAIN_SPLITS = True

# --- G: THE SIX SCOPE FENCES -------------------------------------------------
SCOUT_GRADE_ONLY = True
FINITE_EXACT_LINEAR_ALGEBRA = True
PHYSICAL_CONTENT_CLAIMED = False
SCHUR_TEMPLATE_ONLY = True
CARRIER_MAP_CONSTRUCTED = False
SAME_OPERATION_CLAIMED = False
OVER_CONSTRAINS_THE_PRINCIPLE = True
CONVENTION_TIED_OBJECTS = (
    "E = diag(1, -1, 1), which is the signed-complement convention tied to the wedge basis beta = (dx^dy, dt^dy, dt^dx)",
    "the sign of every individual effective plane shear c_p, which a reorientation or a coordinate reversal conjugates",
    "the sign convention g_ij = +c_ij, under which the normalised Schur shear is +rho while the 1-form Hodge block carries a NEGATIVE off-diagonal entry",
)
SQUARED_SHEAR_IS_THE_INVARIANT = True
EFFECTIVE_SHEARS_MAY_DIFFER_IN_SIGN = True
LANDED_2D_IS_NO_THIRD_DIRECTION_CASE = True
LANDED_NUMBERS_CORRECTED = 0
POSITIVITY_CLASSIFIED_ON_ALL_BRANCHES = False
INSTANCE_SCOPE = (
    "four extents, (4,2,2), (4,4,2), (4,4,4) and (4,3,2), and no other",
    "three origin and three opposite coordinate faces, and no oblique face; the Schur target holds only on the origin faces",
    "one landed 2D target, shear_hodge(c, v), and no other cell form",
    "one exhibited nonuniform reciprocal point, (c, v0, v1, c1) = (3/5, 12/25, 3/4, 4/5)",
    "one isotropic-locus analysis, over the eight sign patterns of a single magnitude kappa",
    "positivity NOT classified over every nonuniform six-face-compatible branch",
)
INSTANCE_SCOPE_COUNT = 6
SCOPE_GENERALISATION_CLAIMED = False

# THE ONE-FAMILY CONTRACT IS ENFORCED BY DISJOINT CLAIM KEYS AND NOT ONLY BY THE
# ASSERTION IN main().  Every claim key below is read by EXACTLY ONE gate.  The
# G fences therefore carry their own constants -- SCOUT_GRADE_ONLY,
# SCHUR_TEMPLATE_ONLY, OVER_CONSTRAINS_THE_PRINCIPLE, SQUARED_SHEAR_IS_THE
# INVARIANT, LANDED_NUMBERS_CORRECTED and the rest -- rather than re-reading the
# B, E and F keys that state the same thing from the other side.  Where a G gate
# depends on a fact measured elsewhere, the gate NAMES the family that measures
# it in its statement and does not consume that family's claim, so neither leans
# on the other and no mutation can flip two families at once.

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 AND HONOURED HERE BY ABSENCE.
# That call carries a rational TOLERANCE and maps a small nonzero rational to
# EXACTLY ZERO.  One of this block's source probes reached for it while
# radsimp-ing a determinant, and the whole of family E is a set of exact
# SIGN statements about rationals as small as -3/20: a single
# tolerance-carrying call could turn the negative eigenvalue that kills the
# curved cell's positivity into a zero, and the headline negative would
# evaporate.  Gate H counts the occurrences in this file's own source and
# requires ZERO, requires ZERO float literals by an AST scan of the same
# source, and -- TIGHTER THAN BLOCK 202, which had decimal displays to print
# and therefore allowed exactly one -- requires ZERO float CALL SITES, because
# every number this block reports is an exact rational short enough to print
# in full and NOTHING here is ever converted to a decimal.
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
    one way an inexact number could enter a file whose every comparison is an
    exact rational one."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    """THE SECOND HALF OF THE SAME HYGIENE, AND THIS BLOCK CAN AFFORD THE
    STRICT FORM.  Block 202 carried decimal DISPLAYS beside two-hundred-digit
    rationals and therefore allowed exactly one float call site.  Every number
    in THIS block is a short exact rational -- ranks, counts, eigenvalues like
    -3/20, moduli like 12/25 -- so no decimal is ever needed and gate H-3
    requires EXACTLY ZERO float call sites.  Nothing in this file can consume
    anything but an exact rational, by measurement rather than by promise."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def kron(left: sp.MatrixBase, right: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(sp.kronecker_product(left, right))


SIGMA_X = sp.Matrix([[0, 1], [1, 0]])
SIGMA_Z = sp.Matrix([[1, 0], [0, -1]])
IDENTITY_2 = sp.eye(2)
IDENTITY_4 = sp.eye(4)
GENERATORS = (kron(SIGMA_X, IDENTITY_2), kron(SIGMA_Z, SIGMA_X),
              kron(SIGMA_Z, SIGMA_Z))


def omega(site: tuple) -> sp.Matrix:
    """THE STAGGERING, AND IT IS A WORD AND NOT A PHASE.  Omega(t, x, y) =
    G1^t G2^x G3^y, with each exponent read modulo two because each generator
    is an involution."""
    result = IDENTITY_4
    for index, coordinate in enumerate(site):
        if coordinate % 2:
            result = result * GENERATORS[index]
    return sp.Matrix(sp.expand(result))


def canonical_word(displacement: tuple) -> sp.Matrix:
    result = IDENTITY_4
    for index, coordinate in enumerate(displacement):
        if coordinate % 2:
            result = result * GENERATORS[index]
    return sp.Matrix(sp.expand(result))


def canonical_relation(expression, symbols: tuple) -> str:
    """A FORCED RELATION, WRITTEN IN A CANONICAL FORM SO TWO ROUTES CAN BE
    COMPARED.  A cokernel vector applied to the right-hand side returns a
    rational function whose denominator is a product of nonvanishing Hodge
    factors; the CONTENT of the statement is the numerator, up to an integer
    factor and up to an overall sign.  This strips exactly those three
    freedoms and nothing else, and the SAME function is applied to the measured
    relation and to the expected literal, so no version drift can separate
    them."""
    numerator = sp.expand(sp.numer(sp.cancel(sp.expand(expression))))
    if numerator == 0:
        return "0"
    primitive = sp.Poly(numerator, *symbols).primitive()[1].as_expr()
    positive = str(sp.expand(primitive))
    negative = str(sp.expand(-primitive))
    if positive.startswith("-") != negative.startswith("-"):
        return negative if positive.startswith("-") else positive
    return min(positive, negative)


def relation_expressions(matrix: sp.Matrix, rhs: sp.Matrix,
                         symbols: tuple) -> dict:
    """THE FORCED RELATIONS OF AN INCONSISTENT SYSTEM, EXACTLY.  Every vector
    in the cokernel of the coefficient matrix annihilates the columns, so its
    pairing with the right-hand side must vanish on any solvable moduli point.
    The set of those pairings IS the compatibility locus, and it is computed
    here rather than guessed.  Returned keyed by canonical form so the caller
    can compare NAMES against a literal and still hold the EXPRESSIONS."""
    relations: dict = {}
    for vector in matrix.T.nullspace():
        expression = sp.expand(sp.numer(sp.cancel(sp.expand(
            (vector.T * rhs)[0, 0]))))
        name = canonical_relation(expression, symbols)
        if name != "0":
            relations.setdefault(name, expression)
    return relations


def relation_set(matrix: sp.Matrix, rhs: sp.Matrix, symbols: tuple) -> tuple:
    return tuple(sorted(relation_expressions(matrix, rhs, symbols)))


def sub_corner_indices(first: tuple, second: tuple, offset: tuple) -> list:
    """THE SUB-CORNER CONVENTION, DECLARED AND NOT ASSUMED: a plane restriction
    reads the four corners [origin, i2, i1, i1 + i2] of the face at the given
    offset.  Gate D-2 measures that every claim of family D survives swapping
    the two 1-form rows and flipping the plane orientation."""
    def add(left: tuple, right: tuple) -> tuple:
        return tuple((left[k] + right[k]) % 2 for k in range(3))
    return [CORNERS.index(offset), CORNERS.index(add(offset, second)),
            CORNERS.index(add(offset, first)), CORNERS.index(add(offset, add(
                first, second)))]


CELL = sp.Matrix(8, 8, lambda i, j: sp.Symbol(f"D{min(i, j)}{max(i, j)}"))
CELL_SYMBOLS = tuple(sorted({CELL[i, j] for i in range(8) for j in range(8)},
                            key=str))
CORNER_DEGREE = tuple(sum(corner) for corner in CORNERS)
DEGREE_INDICES = tuple(
    tuple(k for k in range(8) if CORNER_DEGREE[k] == degree)
    for degree in range(4))
# The three coordinate planes, each with the direction it is MISSING.
PLANE_FRAMES = (
    ((1, 0, 0), (0, 1, 0), (0, 0, 1), "tx"),
    ((1, 0, 0), (0, 0, 1), (0, 1, 0), "ty"),
    ((0, 1, 0), (0, 0, 1), (1, 0, 0), "xy"),
)
SHAPE_ZERO_POSITIONS = ((0, 1), (0, 2), (0, 3), (1, 3), (2, 3))


# ---------------------------------------------------------------------------
# THE MEASURED FACTS
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class RuleFacts:
    squares_identity: tuple
    anticommute: tuple
    even_bad: tuple
    even_bad_wrap: tuple
    even_eta: tuple
    even_links: tuple
    odd_bad: tuple
    odd_bad_wrap: tuple
    odd_eta: bool
    odd_bad_total: int
    odd_bad_directions: tuple
    sigma_rows: tuple
    sigma_values: tuple
    sigma_well_defined: tuple
    word_form_exact: bool
    psi_orthogonal: bool


@dataclass(frozen=True)
class GluingFacts:
    three_face_equations: int
    three_face_ranks: tuple
    three_face_relations: tuple
    variant_ranks: tuple
    variant_relations: tuple
    shape3_rank: int
    shape3_manifold: int
    shape3_survivors: int
    shape3_cross_zero: int
    shape3_cross_free: int
    shape3_one_form_equal: bool
    shape3_two_form_equal: bool
    shape6_rank: int
    shape6_manifold: int
    shape6_survivors: int
    shape6_cross_zero: int
    shape6_cross_free: int
    shape6_cross_free_pairs: tuple
    shape6_cross_free_complementary: bool
    shape6_one_form_equal: bool
    shape6_two_form_equal: bool
    shape6_within_degree_free: tuple
    shape6_parameter_census: tuple


@dataclass(frozen=True)
class RigidityFacts:
    six_face_equations: int
    six_face_ranks: tuple
    six_face_relations: tuple
    uniform_constraints: tuple
    uniform_solutions: tuple
    reciprocal_moduli: tuple
    reciprocal_ranks: tuple
    reciprocal_free_names: tuple
    degree_spectra: tuple
    blocks_parameter_free: tuple
    negative_eigenvalue_blocks: tuple


@dataclass(frozen=True)
class LiftFacts:
    jacobi_exact: bool
    two_form_matches_duality: bool
    two_form_matches_compound: bool
    undivided_matches_generically: bool
    undivided_matches_at_unit_volume: bool
    top_is_dual: bool
    origin_restriction_law_exact: bool
    opposite_restriction_law_exact: bool
    opposite_restriction_residual_nnz: tuple
    opposite_representative_defects: tuple
    plane_scale: object
    plane_volume: object
    schur_determinant_identity: bool
    partial_correlation_on_locus: bool
    schur_diagonal_is_unit: bool
    landed_match_at_decoupled: bool
    landed_match_residual_exact: bool
    zero_pattern_identical: int
    equal_diagonal_residuals: tuple
    membership_iff_equal: bool
    membership_generic: bool
    three_d_couplings: tuple
    origin_two_form_pair_counts: tuple
    opposite_two_form_pair_counts: tuple
    cross_degree_zero: bool
    isotropic_relations: bool
    orientation_determinants: dict
    orientation_leading_minors: dict
    kappa_bounds: tuple


@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    imposed: int
    registered: int
    adopted: int
    unsupplied: int
    readings: int
    unnamed_words: int
    rule: RuleFacts
    gluing: GluingFacts
    rigidity: RigidityFacts
    lift: LiftFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    float_calls: int


def scan_extent(extent: tuple) -> tuple:
    """THE PER-LINK SCALARIZATION TEST, RUN ON EVERY DIRECTED LINK OF A TORUS.
    A link is SCALAR when Omega(s)^T (G_d/2) Omega(s + e_d) is a multiple of
    I4; the wrap flag records whether the link crosses the periodic boundary,
    so the obstruction can be located rather than merely counted.  The eta
    check compares the surviving scalar against the re-derived staggered phase
    eta_d / 2 and never against a borrowed one."""
    bad = [0, 0, 0]
    bad_wrap = [0, 0, 0]
    eta_holds = True
    for site in itertools.product(*(range(e) for e in extent)):
        for direction in range(3):
            stepped = list(site)
            stepped[direction] += 1
            wraps = stepped[direction] == extent[direction]
            neighbour = tuple(c % e for c, e in zip(stepped, extent))
            block = sp.Matrix(sp.expand(
                omega(site).T * (GENERATORS[direction] / 2) * omega(neighbour)))
            off_diagonal = any(block[i, j] != 0 for i in range(4)
                               for j in range(4) if i != j)
            diagonal_equal = (block[0, 0] == block[1, 1] == block[2, 2]
                              == block[3, 3])
            if off_diagonal or not diagonal_equal:
                bad[direction] += 1
                if wraps:
                    bad_wrap[direction] += 1
                continue
            eta = (sp.Integer(1), sp.Integer(-1) ** site[0],
                   sp.Integer(-1) ** (site[0] + site[1]))[direction]
            if sp.expand(block[0, 0] - eta / 2) != 0:
                eta_holds = False
    return tuple(bad), tuple(bad_wrap), eta_holds


def measure_rule() -> RuleFacts:
    """FAMILY C, MEASURED ONCE.  The generator algebra, the four extent scans,
    the sign matrix at all eight anchor parities, the general-target word form
    and the orthogonality of the block staggering."""
    squares = tuple(sp.expand(g * g - IDENTITY_4).is_zero_matrix
                    for g in GENERATORS)
    anticommute = tuple(
        sp.expand(GENERATORS[i] * GENERATORS[j]
                  + GENERATORS[j] * GENERATORS[i]).is_zero_matrix
        for i, j in ((0, 1), (0, 2), (1, 2)))

    even_bad, even_wrap, even_eta, even_links = [], [], [], []
    for extent in EVEN_EXTENTS:
        bad, wrap, eta = scan_extent(extent)
        even_bad.append(bad)
        even_wrap.append(wrap)
        even_eta.append(eta)
        even_links.append(3 * extent[0] * extent[1] * extent[2])
    odd_bad, odd_wrap, odd_eta = scan_extent(ODD_EXTENT)

    sigma = sp.zeros(8, 8)
    well_defined = []
    for anchor in CORNERS:
        anchor_ok = True
        for a, corner_a in enumerate(CORNERS):
            for b, corner_b in enumerate(CORNERS):
                shifted_a = tuple(anchor[k] + corner_a[k] for k in range(3))
                shifted_b = tuple(anchor[k] + corner_b[k] for k in range(3))
                product = sp.Matrix(sp.expand(
                    omega(shifted_a) * omega(shifted_b).T))
                word = canonical_word(
                    tuple((corner_a[k] + corner_b[k]) % 2 for k in range(3)))
                if sp.expand(product - word).is_zero_matrix:
                    value = sp.Integer(1)
                elif sp.expand(product + word).is_zero_matrix:
                    value = sp.Integer(-1)
                else:
                    value = sp.nan
                    anchor_ok = False
                if anchor == (0, 0, 0):
                    sigma[a, b] = value
        well_defined.append(anchor_ok)

    target = sp.Matrix(8, 8, lambda i, j: sp.Symbol(
        f"T{min(i, j)}{max(i, j)}"))
    word_form = True
    for a, corner_a in enumerate(CORNERS):
        for b, corner_b in enumerate(CORNERS):
            word = canonical_word(
                tuple((corner_a[k] + corner_b[k]) % 2 for k in range(3)))
            residual = sp.expand(
                target[a, b] * omega(corner_a) * omega(corner_b).T
                - sigma[a, b] * target[a, b] * word)
            if not residual.is_zero_matrix:
                word_form = False

    psi = sp.diag(*[omega(corner) for corner in CORNERS])
    orthogonal = sp.expand(psi * psi.T - sp.eye(PSI_SIZE)).is_zero_matrix
    return RuleFacts(
        squares, anticommute, tuple(even_bad), tuple(even_wrap),
        tuple(even_eta), tuple(even_links), odd_bad, odd_wrap, odd_eta,
        sum(odd_bad), tuple(d for d in range(3) if odd_bad[d]),
        tuple(tuple(int(sigma[i, j]) if sigma[i, j].is_Integer else 0
                    for j in range(8)) for i in range(8)),
        tuple(sorted({int(sigma[i, j]) for i in range(8) for j in range(8)
                      if sigma[i, j].is_Integer})),
        tuple(well_defined), word_form, orthogonal)


def literal_system(offsets: tuple, order_swap: bool, flip: bool,
                   moduli=None) -> tuple:
    """THE LITERAL GLUING SYSTEM, BUILT ONCE PER CONVENTION AND PER FACE SET.
    Every equation says one entry of the general symmetric corner matrix equals
    the corresponding entry of the LANDED shear_hodge at that face's own
    moduli.  `moduli` supplies the per-face (volume, shear); when it is None
    each face carries its own independent symbol pair."""
    equations, symbols = [], []
    for first, second, normal, name in PLANE_FRAMES:
        if flip:
            first, second = second, first
        for offset_index in offsets:
            offset = tuple(offset_index * k for k in normal)
            if moduli is None:
                tag = name if offsets == (0,) else f"{name}{offset_index}"
                volume = sp.Symbol(f"v_{tag}", positive=True)
                shear = sp.Symbol(f"c_{tag}")
                symbols.extend((volume, shear))
            else:
                volume, shear = moduli[offset_index]
            landed = sp.Matrix(LANDED_SHEAR_HODGE(shear, volume))
            ordered = (first, second) if order_swap else (second, first)
            indices = [CORNERS.index(offset),
                       CORNERS.index(tuple(
                           (offset[k] + ordered[0][k]) % 2 for k in range(3))),
                       CORNERS.index(tuple(
                           (offset[k] + ordered[1][k]) % 2 for k in range(3))),
                       CORNERS.index(tuple(
                           (offset[k] + first[k] + second[k]) % 2
                           for k in range(3)))]
            for row in range(4):
                for column in range(4):
                    equations.append(sp.expand(
                        CELL[indices[row], indices[column]]
                        - landed[row, column]))
    matrix, rhs = sp.linear_eq_to_matrix(equations, CELL_SYMBOLS)
    return equations, matrix, rhs, tuple(symbols)


def shape_system(offsets: tuple) -> tuple:
    """THE SHAPE-ONLY SYSTEM: the five-entry zero pattern of the landed form
    plus the equality of its two 1-form diagonals, imposed on each face.  It
    carries NO moduli at all -- it asks only that each shadow LOOK like a
    shear-Hodge cell, and its solution manifold is the space of corner
    matrices whose plane shadows do."""
    rows = []
    for first, second, normal, _ in PLANE_FRAMES:
        for offset_index in offsets:
            offset = tuple(offset_index * k for k in normal)
            indices = sub_corner_indices(first, second, offset)
            for row, column in SHAPE_ZERO_POSITIONS:
                rows.append(CELL[indices[row], indices[column]])
            rows.append(CELL[indices[1], indices[1]]
                        - CELL[indices[2], indices[2]])
    matrix, rhs = sp.linear_eq_to_matrix(rows, CELL_SYMBOLS)
    return matrix, rhs


def shape_report(offsets: tuple) -> dict:
    matrix, rhs = shape_system(offsets)
    rank = matrix.rank()
    solution = list(sp.linsolve((matrix, rhs), CELL_SYMBOLS))[0]
    solved = sp.Matrix(8, 8, lambda i, j: solution[
        CELL_SYMBOLS.index(CELL[min(i, j), max(i, j)])])
    cross_zero, cross_free = [], []
    for i in range(8):
        for j in range(i + 1, 8):
            if CORNER_DEGREE[i] == CORNER_DEGREE[j]:
                continue
            if solved[i, j] == 0:
                cross_zero.append((CORNERS[i], CORNERS[j]))
            else:
                cross_free.append((CORNERS[i], CORNERS[j]))
    ones, twos = DEGREE_INDICES[1], DEGREE_INDICES[2]
    within = (
        sum(1 for i in ones for j in ones if i < j and solved[i, j] != 0),
        sum(1 for i in twos for j in twos if i < j and solved[i, j] != 0))
    survivors = sum(1 for i in range(8) for j in range(i, 8)
                    if solved[i, j] != 0)
    diagonals = len({solved[k, k] for k in range(8)})
    return {
        "rank": rank,
        "manifold": len(CELL_SYMBOLS) - rank,
        "survivors": survivors,
        "cross_zero": tuple(cross_zero),
        "cross_free": tuple(cross_free),
        "one_form_equal": bool(solved[ones[0], ones[0]]
                               == solved[ones[1], ones[1]]
                               == solved[ones[2], ones[2]]),
        "two_form_equal": bool(solved[twos[0], twos[0]]
                               == solved[twos[1], twos[1]]
                               == solved[twos[2], twos[2]]),
        "within": within,
        "distinct_diagonals": diagonals,
    }


def measure_gluing() -> GluingFacts:
    """FAMILY D, MEASURED ONCE.  The three-face literal system at generic
    independent moduli, the four convention variants, and the two shape-only
    manifolds."""
    variant_ranks, variant_relations = [], []
    base_relations, base_ranks, base_equations = (), (0, 0), 0
    for order_swap, flip in ((False, False), (True, False),
                             (False, True), (True, True)):
        equations, matrix, rhs, symbols = literal_system(
            (0,), order_swap, flip)
        ranks = (matrix.rank(), matrix.row_join(rhs).rank())
        relations = relation_set(matrix, rhs, symbols)
        variant_ranks.append(ranks)
        variant_relations.append(relations)
        if not order_swap and not flip:
            base_relations, base_ranks = relations, ranks
            base_equations = len(equations)

    three = shape_report((0,))
    six = shape_report((0, 1))
    return GluingFacts(
        base_equations, base_ranks, base_relations,
        tuple(variant_ranks), tuple(variant_relations),
        three["rank"], three["manifold"], three["survivors"],
        len(three["cross_zero"]), len(three["cross_free"]),
        three["one_form_equal"], three["two_form_equal"],
        six["rank"], six["manifold"], six["survivors"],
        len(six["cross_zero"]), len(six["cross_free"]),
        six["cross_free"],
        all(CORNERS.index(a) ^ CORNERS.index(b) == 7
            for a, b in six["cross_free"]),
        six["one_form_equal"], six["two_form_equal"], six["within"],
        (six["distinct_diagonals"], sum(six["within"]),
         len(six["cross_free"])))


def measure_rigidity() -> RigidityFacts:
    """FAMILY E, MEASURED ONCE, AND IT IS THE HEADLINE NEGATIVE.  The six-face
    literal system at generic independent per-face moduli; the same system on
    the UNIFORM locus, where the surviving numerators are read and SOLVED
    rather than eyeballed; and the one exhibited nonuniform reciprocal point,
    where the solution's degree blocks are extracted with their free-symbol
    content and their exact spectra."""
    equations, matrix, rhs, symbols = literal_system((0, 1), False, False)
    six_ranks = (matrix.rank(), matrix.row_join(rhs).rank())
    six_relations = relation_set(matrix, rhs, symbols)

    # THE UNIFORM LOCUS.  All twelve face moduli are collapsed to one pair.
    # THE QUICK READING SAW ONLY c^2 + v^2 - 1 AND MISSED c^2 v, WHICH IS THE
    # CLAUSE THAT KILLS THE CURVED UNIFORM CELL; both numerators are measured
    # here and the pair is SOLVED over the positive branch.
    # THE VOLUME IS POSITIVE AND THE SHEAR IS ONLY REAL.  Declaring the shear
    # positive would EXCLUDE c = 0 by assumption and hand this block its own
    # headline for free; the flat point has to be a consequence of the two
    # numerators, so the sign restriction is applied AFTER the solve and only
    # to the volume's branch.
    volume = sp.Symbol("v", positive=True)
    shear = sp.Symbol("c", real=True)
    _, uniform_matrix, uniform_rhs, _ = literal_system(
        (0, 1), False, False, moduli={0: (volume, shear), 1: (volume, shear)})
    uniform_map = relation_expressions(
        uniform_matrix, uniform_rhs, (shear, volume))
    uniform = tuple(sorted(uniform_map))
    solutions = sp.solve(list(uniform_map.values()), [shear, volume],
                         dict=True)
    uniform_solutions = tuple(sorted(
        ((candidate[shear], candidate[volume])
         for candidate in solutions
         if shear in candidate and volume in candidate
         and candidate[shear] >= 0 and candidate[volume] > 0),
        key=str))

    # THE ONE EXHIBITED NONUNIFORM POINT.  v1 and c1 are DERIVED from the
    # cross-offset reciprocal relation rather than chosen, so the point is a
    # consequence of family E's own sixteen relations and not a lucky guess.
    shear_zero = RECIPROCAL_SHEAR
    volume_zero = RECIPROCAL_VOLUME_ZERO
    volume_one = sp.cancel(volume_zero / (1 - shear_zero ** 2))
    shear_one = sp.cancel(sp.sqrt(sp.cancel(1 - volume_zero * volume_one)))
    _, point_matrix, point_rhs, _ = literal_system(
        (0, 1), False, False,
        moduli={0: (volume_zero, shear_zero), 1: (volume_one, shear_one)})
    point_ranks = (point_matrix.rank(),
                   point_matrix.row_join(point_rhs).rank())
    solution = list(sp.linsolve((point_matrix, point_rhs), CELL_SYMBOLS))[0]
    free = tuple(sorted(
        {symbol for entry in solution for symbol in entry.free_symbols
         if str(symbol).startswith("D")}, key=str))
    solved = sp.Matrix(8, 8, lambda i, j: solution[
        CELL_SYMBOLS.index(CELL[min(i, j), max(i, j)])])

    spectra, parameter_free, negative = [], [], []
    for degree in range(4):
        indices = DEGREE_INDICES[degree]
        block = sp.Matrix(len(indices), len(indices),
                          lambda i, j: solved[indices[i], indices[j]])
        content = set()
        for i in range(block.rows):
            for j in range(block.cols):
                content |= block[i, j].free_symbols
        parameter_free.append(not (content & set(free)))
        eigenvalues = tuple(sorted(
            ((value, multiplicity)
             for value, multiplicity in block.eigenvals().items()),
            key=str))
        spectra.append(eigenvalues)
        negative.append(any(value < 0 for value, _ in eigenvalues))
    return RigidityFacts(
        len(equations), six_ranks, six_relations, uniform,
        uniform_solutions,
        (shear_zero, volume_zero, volume_one, shear_one),
        point_ranks, tuple(str(symbol) for symbol in free),
        tuple(spectra), tuple(parameter_free), tuple(negative))


def measure_lift() -> LiftFacts:
    """FAMILY F, MEASURED ONCE, OVER THE RATIONAL FUNCTION FIELD IN THE THREE
    SHEARS AND THE VOLUME.  Nothing here is evaluated at a point except where
    the statement is explicitly a point statement; every identity below is an
    identity of rational functions."""
    shear_tx, shear_ty, shear_xy = sp.symbols("c_tx c_ty c_xy")
    volume = sp.Symbol("V", positive=True)
    metric = sp.Matrix([[1, shear_tx, shear_ty],
                        [shear_tx, 1, shear_xy],
                        [shear_ty, shear_xy, 1]])
    determinant = sp.expand(metric.det())
    inverse = sp.together(metric.inv())
    signature = sp.diag(*WEDGE_SIGNATURE)

    # THE SECOND COMPOUND GRAM, BUILT FROM ITS DEFINITION AND NOT ASSERTED.
    pairs = ((1, 2), (0, 2), (0, 1))
    compound = sp.zeros(3, 3)
    for i, (p1, q1) in enumerate(pairs):
        for j, (p2, q2) in enumerate(pairs):
            compound[i, j] = sp.cancel(
                inverse[p1, p2] * inverse[q1, q2]
                - inverse[p1, q2] * inverse[q1, p2])
    jacobi = sp.simplify(
        compound - signature * metric * signature / determinant
    ) == sp.zeros(3, 3)

    weight_zero = volume
    weight_one = volume * inverse
    weight_two = signature * metric * signature / volume
    weight_three = 1 / volume
    matches_duality = sp.simplify(
        weight_two - signature * weight_one.inv() * signature.T
    ) == sp.zeros(3, 3)
    matches_compound = sp.simplify(
        weight_two - determinant / volume * compound) == sp.zeros(3, 3)
    # THE LOAD-BEARING DIVISION.  The un-divided paraphrase det(g) Lambda^2 is
    # E g E, which is weight_two ONLY at V = 1.  Both halves are measured.
    undivided = determinant * compound
    undivided_generic = sp.simplify(undivided - weight_two) == sp.zeros(3, 3)
    undivided_at_one = sp.simplify(
        (undivided - weight_two).subs({volume: sp.Integer(1)})
    ) == sp.zeros(3, 3)
    top_is_dual = sp.cancel(weight_three - 1 / weight_zero) == 0

    lift = sp.zeros(8, 8)
    lift[0, 0] = weight_zero
    ones, twos = DEGREE_INDICES[1], DEGREE_INDICES[2]
    # The 1-form sector is ordered (dt, dx, dy) and the 2-form sector is
    # ordered beta = (dx^dy, dt^dy, dt^dx), each paired with its complementary
    # direction; both orders are declared here and gate G-4 fences them.
    one_order = (CORNERS.index((1, 0, 0)), CORNERS.index((0, 1, 0)),
                 CORNERS.index((0, 0, 1)))
    two_order = (CORNERS.index((0, 1, 1)), CORNERS.index((1, 0, 1)),
                 CORNERS.index((1, 1, 0)))
    for i in range(3):
        for j in range(3):
            lift[one_order[i], one_order[j]] = weight_one[i, j]
            lift[two_order[i], two_order[j]] = weight_two[i, j]
    lift[7, 7] = weight_three
    cross_zero = all(
        lift[i, j] == 0 for i in range(8) for j in range(8)
        if CORNER_DEGREE[i] != CORNER_DEGREE[j])

    # THE ORIGIN-FACE SCHUR IDENTITY, AND THE OPPOSITE-FACE COUNTERCHECK.
    # The global degree grading makes the two offsets different objects: an
    # origin face has degrees (0,1,1,2), whereas its opposite face has
    # degrees (1,2,2,3).  The Schur target below is therefore measured at both
    # offsets rather than silently transported between them.
    swap = sp.Matrix([[0, 1], [1, 0]])
    directions = {"tx": (0, 1, 2), "ty": (0, 2, 1), "xy": (1, 2, 0)}
    schur, origin_exact, opposite_exact = {}, True, True
    opposite_nnz, opposite_defects = [], []
    origin_two_pairs, opposite_two_pairs = [], []
    counter_point = {
        shear_tx: sp.Rational(1, 5), shear_ty: sp.Rational(1, 7),
        shear_xy: sp.Rational(1, 9), volume: sp.Integer(2),
    }
    for first, second, normal, name in PLANE_FRAMES:
        d1, d2, missing = directions[name]
        origin_indices = sub_corner_indices(first, second, (0, 0, 0))
        opposite_indices = sub_corner_indices(first, second, normal)
        origin_restriction = sp.Matrix(
            4, 4, lambda r, c: lift[origin_indices[r], origin_indices[c]])
        opposite_restriction = sp.Matrix(
            4, 4, lambda r, c: lift[opposite_indices[r], opposite_indices[c]])
        in_plane = sp.Matrix([[metric[d1, d1], metric[d1, d2]],
                              [metric[d2, d1], metric[d2, d2]]])
        to_missing = sp.Matrix([[metric[d1, missing]], [metric[d2, missing]]])
        complement = in_plane - to_missing * to_missing.T
        schur[name] = complement
        target = sp.diag(volume, swap * (volume * complement.inv()) * swap.T,
                         1 / volume)
        origin_exact = origin_exact and sp.simplify(
            origin_restriction - target) == sp.zeros(4, 4)
        opposite_residual = sp.Matrix(
            opposite_restriction - target).applyfunc(sp.cancel)
        opposite_exact = opposite_exact and (
            opposite_residual == sp.zeros(4, 4))
        evaluated = opposite_residual.subs(counter_point).applyfunc(sp.cancel)
        opposite_nnz.append(sum(
            evaluated[i, j] != 0 for i in range(4) for j in range(4)))
        opposite_defects.append(evaluated[0, 0])
        origin_two_pairs.append(sum(
            1 for i in range(4) for j in range(i + 1, 4)
            if CORNER_DEGREE[origin_indices[i]] == 2
            and CORNER_DEGREE[origin_indices[j]] == 2))
        opposite_two_pairs.append(sum(
            1 for i in range(4) for j in range(i + 1, 4)
            if CORNER_DEGREE[opposite_indices[i]] == 2
            and CORNER_DEGREE[opposite_indices[j]] == 2))
    schur_determinant = all(
        sp.cancel(schur[name].det() - determinant) == 0
        for _, _, _, name in PLANE_FRAMES)

    # THE 0/2 SECTORS FORCE THE PLANE SCALE AND THE PLANE VOLUME.
    scale, plane_volume = sp.symbols("lam vpos", positive=True)
    forced = sp.solve([sp.Eq(scale * plane_volume, volume),
                       sp.Eq(scale / plane_volume, 1 / volume)],
                      [scale, plane_volume], dict=True)
    plane_scale = forced[0][scale] if len(forced) == 1 else sp.nan
    plane_volume_value = forced[0][plane_volume] if len(forced) == 1 \
        else sp.nan

    # THE EFFECTIVE PLANE SHEAR IS THE PARTIAL CORRELATION, ON THE PER-PLANE
    # ISOTROPY LOCUS -- AND ITS DIAGONAL NORMALISATION IS MEASURED, NOT
    # ASSUMED: off that locus the Schur diagonal is NOT unity, which is the
    # whole reason the phrase needs its qualification.
    magnitude = sp.Symbol("kappa")
    names = {(0, 1): shear_tx, (0, 2): shear_ty, (1, 2): shear_xy}
    on_locus, residual_exact = True, True
    for first, second, _, name in PLANE_FRAMES:
        _, _, missing = directions[name]
        outer = [names[pair] for pair in ((0, 1), (0, 2), (1, 2))
                 if missing in pair]
        for orientation in (1, -1):
            reduced = schur[name].subs({outer[0]: magnitude,
                                        outer[1]: orientation * magnitude})
            effective = sp.cancel(reduced[0, 1] / (1 - magnitude ** 2))
            plane_metric = sp.Matrix([[1, effective], [effective, 1]])
            on_locus = on_locus and sp.simplify(
                volume * reduced.inv()
                - volume * plane_metric.inv() / (1 - magnitude ** 2)
            ) == sp.zeros(2, 2)
            residual_exact = residual_exact and sp.simplify(
                volume * reduced.inv() - volume * plane_metric.inv()
                - magnitude ** 2 * volume * reduced.inv()) == sp.zeros(2, 2)
    schur_diagonal_unit = sp.cancel(schur["tx"][0, 0] - 1) == 0
    decoupled = sp.simplify(
        sp.Matrix(4, 4, lambda r, c: lift[
            sub_corner_indices((1, 0, 0), (0, 1, 0), (0, 0, 0))[r],
            sub_corner_indices((1, 0, 0), (0, 1, 0), (0, 0, 0))[c]]
        ).subs({shear_ty: 0, shear_xy: 0})
        - sp.Matrix(LANDED_SHEAR_HODGE(shear_tx, volume))) == sp.zeros(4, 4)

    # SHAPE-MANIFOLD MEMBERSHIP.
    zero_pattern, equal_diagonal = 0, []
    for first, second, _, _ in PLANE_FRAMES:
        indices = sub_corner_indices(first, second, (0, 0, 0))
        for row, column in SHAPE_ZERO_POSITIONS:
            if sp.cancel(lift[indices[row], indices[column]]) == 0:
                zero_pattern += 1
        equal_diagonal.append(sp.cancel(
            lift[indices[1], indices[1]] - lift[indices[2], indices[2]]))
    expected_residuals = (
        volume * (shear_xy ** 2 - shear_ty ** 2) / determinant,
        volume * (shear_xy ** 2 - shear_tx ** 2) / determinant,
        volume * (shear_ty ** 2 - shear_tx ** 2) / determinant)
    residual_form = all(
        sp.cancel(a - b) == 0
        for a, b in zip(equal_diagonal, expected_residuals))
    generic_point = {shear_tx: sp.Rational(1, 3), shear_ty: sp.Rational(1, 5),
                     shear_xy: sp.Rational(1, 7), volume: sp.Integer(2)}
    membership_generic = any(
        residual.subs(generic_point) != 0 for residual in equal_diagonal)
    membership_iff = all(
        sp.cancel(residual.subs({shear_ty: shear_tx, shear_xy: -shear_tx}))
        == 0 for residual in equal_diagonal) and all(
        sp.cancel(residual.subs({shear_ty: -shear_tx, shear_xy: shear_tx}))
        == 0 for residual in equal_diagonal)

    couplings = (
        sp.cancel(lift[two_order[0], two_order[1]] + shear_tx / volume),
        sp.cancel(lift[two_order[0], two_order[2]] - shear_ty / volume),
        sp.cancel(lift[two_order[1], two_order[2]] + shear_xy / volume))

    # THE ISOTROPIC LOCUS AND ITS ORIENTATION SPLIT.
    isotropic_ok, determinants, leading_minors = True, {}, {}
    for e1, e2, e3 in itertools.product((1, -1), repeat=3):
        substitution = {shear_tx: e1 * magnitude, shear_ty: e2 * magnitude,
                        shear_xy: e3 * magnitude}
        orientation = e1 * e2 * e3
        determinants[(e1, e2, e3)] = (
            orientation,
            sp.factor(sp.expand(metric.subs(substitution).det())))
        reduced_metric = metric.subs(substitution)
        leading_minors[(e1, e2, e3)] = tuple(
            sp.factor(sp.expand(reduced_metric[:size, :size].det()))
            for size in (1, 2, 3))
        scales, squares = [], []
        for _, _, _, name in PLANE_FRAMES:
            reduced = schur[name].subs(substitution)
            isotropic_ok = isotropic_ok and sp.cancel(
                reduced[0, 0] - reduced[1, 1]) == 0
            scales.append(sp.cancel(volume / reduced[0, 0]))
            squares.append(sp.cancel((reduced[0, 1] / reduced[0, 0]) ** 2))
        isotropic_ok = isotropic_ok and all(
            sp.cancel(value - volume / (1 - magnitude ** 2)) == 0
            for value in scales)
        isotropic_ok = isotropic_ok and all(
            sp.cancel(value - magnitude ** 2 * (1 - orientation * magnitude)
                      ** 2 / (1 - magnitude ** 2) ** 2) == 0
            for value in squares)
    # THE BOUND IS READ OFF THE MEASURED DETERMINANT AND NOT ASSERTED: within
    # each orientation class every sign pattern returns the SAME polynomial,
    # and the class's admissible kappa range ends at that polynomial's
    # smallest positive root, which is where det g first reaches zero.
    bounds = []
    for orientation in (1, -1):
        polynomials = {sp.expand(value) for sign, value
                       in determinants.values() if sign == orientation}
        if len(polynomials) != 1:
            bounds.append(sp.nan)
            continue
        polynomial = polynomials.pop()
        roots = sorted(
            (root for root in sp.roots(sp.Poly(polynomial, magnitude))
             if root.is_real and root > 0), key=str)
        bounds.append(roots[0] if roots else sp.nan)
    return LiftFacts(
        jacobi, matches_duality, matches_compound, undivided_generic,
        undivided_at_one, top_is_dual, origin_exact, opposite_exact,
        tuple(opposite_nnz), tuple(opposite_defects), plane_scale,
        plane_volume_value, schur_determinant, on_locus, schur_diagonal_unit,
        decoupled, residual_exact, zero_pattern, tuple(equal_diagonal),
        bool(membership_iff and residual_form), bool(membership_generic),
        couplings, tuple(origin_two_pairs), tuple(opposite_two_pairs),
        cross_zero, isotropic_ok, determinants, leading_minors, tuple(bounds))


def measure() -> Facts:
    """THE ONE MEASUREMENT PASS.  Four independent packages -- the rule scans,
    the gluing systems, the rigidity chain and the declared D3 candidate -- are built
    here and NOTHING below is recomputed.  The expensive items are the two
    cokernel bases (a 48 x 36 and a 96 x 36 integer coefficient matrix), the
    four convention repeats of the first, and the symbolic inverse of the
    three-by-three metric over QQ(c_tx, c_ty, c_xy); every other operation is a
    rank or a substitution."""
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
        len(UNNAMED_PHYSICS_WORDS),
        measure_rule(),
        measure_gluing(),
        measure_rigidity(),
        measure_lift(),
        scope_certificate(note_text),
        nsimplify_occurrences(),
        float_literal_occurrences(),
        float_call_sites())


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
        "geometry_is_spacetime": GEOMETRY_IS_SPACETIME_CLAIMED,
        "unnamed_words": len(UNNAMED_PHYSICS_WORDS),
        "gluing_is_dynamics": GLUING_IS_DYNAMICS_CLAIMED,
        "rigidity_is_universal": RIGIDITY_IS_UNIVERSAL_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "equations_of_motion": EQUATIONS_OF_MOTION_CLAIMED,
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "generator_squares": GENERATOR_SQUARES_IDENTITY,
        "generator_anticommute": GENERATOR_ANTICOMMUTE,
        "even_bad": EVEN_BAD_COUNTS,
        "even_bad_wrap": EVEN_BAD_WRAP_COUNTS,
        "even_eta": EVEN_ETA_HOLDS,
        "even_links": EVEN_LINK_COUNTS,
        "odd_bad": ODD_BAD_COUNTS,
        "odd_bad_wrap": ODD_BAD_WRAP_COUNTS,
        "odd_bad_total": ODD_BAD_TOTAL,
        "odd_bad_direction": ODD_BAD_DIRECTION,
        "odd_eta": ODD_ETA_HOLDS,
        "sigma_rows": SIGMA_ROWS,
        "sigma_values": SIGMA_VALUES,
        "sigma_well_defined": SIGMA_WELL_DEFINED,
        "word_form_exact": WORD_FORM_EXACT,
        "psi_orthogonal": PSI_ORTHOGONAL,
        # D
        "three_face_equations": THREE_FACE_EQUATIONS,
        "three_face_ranks": THREE_FACE_RANKS,
        "three_face_relation_count": THREE_FACE_RELATION_COUNT,
        "three_face_relations": THREE_FACE_RELATIONS,
        "variant_count": CONVENTION_VARIANTS,
        "variant_ranks_identical": CONVENTION_RANKS_IDENTICAL,
        "variant_relations_identical": CONVENTION_RELATIONS_IDENTICAL,
        "shape3_rank": SHAPE3_RANK,
        "shape3_manifold": SHAPE3_MANIFOLD,
        "shape3_survivors": SHAPE3_SURVIVOR_COUNT,
        "shape3_cross_zero": SHAPE3_CROSS_FORCED_ZERO,
        "shape3_cross_free": SHAPE3_CROSS_FREE,
        "shape3_one_form_equal": SHAPE3_ONE_FORM_DIAGONALS_EQUAL,
        "shape6_rank": SHAPE6_RANK,
        "shape6_manifold": SHAPE6_MANIFOLD,
        "shape6_survivors": SHAPE6_SURVIVOR_COUNT,
        "shape6_cross_free_pairs": SHAPE6_CROSS_FREE_PAIRS,
        "shape6_cross_free_complementary":
            SHAPE6_CROSS_FREE_ARE_COMPLEMENTARY,
        "shape6_one_form_equal": SHAPE6_ONE_FORM_DIAGONALS_EQUAL,
        "shape6_two_form_equal": SHAPE6_TWO_FORM_DIAGONALS_EQUAL,
        "shape6_within_degree_free": SHAPE6_WITHIN_DEGREE_FREE,
        "shape6_parameter_census": SHAPE6_PARAMETER_CENSUS,
        # E
        "six_face_equations": SIX_FACE_EQUATIONS,
        "six_face_ranks": SIX_FACE_RANKS,
        "six_face_relation_count": SIX_FACE_RELATION_COUNT,
        "six_face_relations": SIX_FACE_RELATIONS,
        "uniform_constraint_count": UNIFORM_CONSTRAINT_COUNT,
        "uniform_constraints": UNIFORM_CONSTRAINTS,
        "uniform_solution": UNIFORM_SOLUTION,
        "uniform_admits_only_flat": UNIFORM_ADMITS_ONLY_FLAT,
        "reciprocal_moduli": (RECIPROCAL_SHEAR, RECIPROCAL_VOLUME_ZERO,
                              RECIPROCAL_VOLUME_ONE, RECIPROCAL_SHEAR_ONE),
        "reciprocal_ranks": RECIPROCAL_RANKS,
        "reciprocal_free_names": RECIPROCAL_FREE_NAMES,
        "degree_one_spectrum": DEGREE_ONE_SPECTRUM,
        "degree_two_spectrum": DEGREE_TWO_SPECTRUM,
        "blocks_parameter_free": PRINCIPAL_BLOCKS_PARAMETER_FREE,
        "curved_cell_pd": CURVED_CELL_EVER_POSITIVE_DEFINITE,
        "rigidity_on_checked_branches": RIGIDITY_ON_CHECKED_BRANCHES,
        # F
        "jacobi_exact": JACOBI_IDENTITY_EXACT,
        "two_form_duality": TOP_IS_DUAL_OF_BOTTOM,
        "two_form_division_load_bearing": TWO_FORM_DIVISION_IS_LOAD_BEARING,
        "undivided_generic": TWO_FORM_UNDIVIDED_MATCHES_GENERICALLY,
        "undivided_at_unit_volume": TWO_FORM_UNDIVIDED_MATCHES_AT_UNIT_VOLUME,
        "origin_restriction_law": ORIGIN_RESTRICTION_LAW_EXACT,
        "opposite_restriction_law": OPPOSITE_RESTRICTION_LAW_EXACT,
        "opposite_restriction_nnz": OPPOSITE_RESTRICTION_RESIDUAL_NNZ,
        "opposite_representative_defects": OPPOSITE_REPRESENTATIVE_DEFECTS,
        "plane_scale": PLANE_SCALE_FORCED,
        "plane_volume_is_cell_volume": PLANE_VOLUME_IS_CELL_VOLUME,
        "schur_determinant": SCHUR_DETERMINANT_IDENTITY,
        "partial_correlation": PARTIAL_CORRELATION_EXACT_ON_LOCUS,
        "partial_correlation_normalisation":
            PARTIAL_CORRELATION_NEEDS_NORMALISATION,
        "landed_match_iff_decoupled": LANDED_MATCH_IFF_DECOUPLED,
        "shape_zero_pattern": SHAPE_ZERO_PATTERN_IDENTICAL,
        "membership_iff_equal": SHAPE_MEMBERSHIP_IFF_EQUAL_MAGNITUDES,
        "three_d_coupling_count": THREE_D_COUPLING_COUNT,
        "three_d_invisible_origin":
            THREE_D_COUPLINGS_INVISIBLE_ON_ORIGIN_FACES,
        "three_d_visible_opposite":
            THREE_D_COUPLINGS_VISIBLE_ON_OPPOSITE_FACES,
        "cross_degree_zero": CROSS_DEGREE_PAIRINGS_ZERO,
        "isotropic_relations": ISOTROPIC_RELATIONS_HOLD,
        "orientation_classes": ORIENTATION_CLASSES,
        "kappa_bounds": (KAPPA_BOUND_POSITIVE, KAPPA_BOUND_NEGATIVE),
        "positivity_domain_splits": POSITIVITY_DOMAIN_SPLITS,
        # G
        "scout_grade_only": SCOUT_GRADE_ONLY,
        "finite_linear_algebra": FINITE_EXACT_LINEAR_ALGEBRA,
        "physical_content": PHYSICAL_CONTENT_CLAIMED,
        "schur_template_only": SCHUR_TEMPLATE_ONLY,
        "schur_equivalence": SCHUR_EQUIVALENCE_CLAIMED,
        "carrier_map": CARRIER_MAP_CONSTRUCTED,
        "same_operation": SAME_OPERATION_CLAIMED,
        "over_constrains_principle": OVER_CONSTRAINS_THE_PRINCIPLE,
        "principle_binds_nature": PRINCIPLE_BINDS_NATURE_CLAIMED,
        "convention_tied": len(CONVENTION_TIED_OBJECTS),
        "squared_shear_invariant": SQUARED_SHEAR_IS_THE_INVARIANT,
        "signed_shear_invariance": SIGNED_SHEAR_INVARIANCE_CLAIMED,
        "landed_special_case": LANDED_2D_IS_NO_THIRD_DIRECTION_CASE,
        "landed_numbers_corrected": LANDED_NUMBERS_CORRECTED,
        "landed_correction": LANDED_CORRECTION_CLAIMED,
        "instance_scope": INSTANCE_SCOPE_COUNT,
        "positivity_all_branches": POSITIVITY_CLASSIFIED_ON_ALL_BRANCHES,
        "scope_generalisation": SCOPE_GENERALISATION_CLAIMED,
        # H
        "note_present": True,
        "scope": {key: True for key in SCOPE_KEYS},
        "nsimplify_calls": 0,
        "float_literals": 0,
        "float_calls": 0,
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
    elif mutation == "claim_geometry_is_spacetime":
        # THE FIRST MISREAD: an 8 x 8 rational weight matrix on the corners of
        # one cube is asserted to BE a spacetime geometry.  It is a matrix.
        claims["geometry_is_spacetime"] = True
        claims["unnamed_words"] = 0
    elif mutation == "claim_gluing_is_dynamics":
        # THE SECOND MISREAD: a linear consistency system among the shadows of
        # one symmetric matrix is asserted to BE a dynamics.
        claims["gluing_is_dynamics"] = True
    elif mutation == "claim_rigidity_is_universal":
        # THE THIRD MISREAD: the exact solution count of ONE gluing principle
        # on the CHECKED branches is asserted to be a universal uniqueness
        # theorem.
        claims["rigidity_is_universal"] = True
    elif mutation == "claim_continuum_theorem":
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
        claims["equations_of_motion"] = True
    elif mutation == "claim_readings_licensed":
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_covariant_rule_algebra":
        claims["generator_anticommute"] = (True, True, False)
    elif mutation == "break_even_scalarization":
        # THE EXTENSION DENIED: the all-even extents are asserted to carry
        # non-scalar links, which would mean the rule does not extend at all.
        claims["even_bad"] = ((0, 0, 0), (0, 0, 0), (0, 1, 0))
        claims["even_eta"] = (True, True, False)
    elif mutation == "break_parity_obstruction":
        # THE OBSTRUCTION DELOCALISED: the odd-extent failures are asserted to
        # spread across directions, which would destroy the direction-local
        # reading entirely.
        claims["odd_bad"] = (4, 0, 4)
        claims["odd_bad_wrap"] = (4, 0, 4)
        claims["odd_bad_direction"] = 0
    elif mutation == "break_sign_matrix":
        claims["sigma_rows"] = tuple(
            (0,) + row[1:] if index == 0 else row
            for index, row in enumerate(SIGMA_ROWS))
        claims["word_form_exact"] = False
    # --- D ----------------------------------------------------------------
    elif mutation == "break_three_face_literal":
        # THE CHECKERS' C6 CORRECTION DELETED: the literal three-face gluing is
        # asserted to select an isolated ISOTROPIC POINT.  It selects the
        # continuous common-v common-c^2 LOCUS, with the three shear SIGNS
        # unglued -- correction 109.
        claims["three_face_ranks"] = (22, 22)
        claims["three_face_relation_count"] = 0
        claims["three_face_relations"] = ()
    elif mutation == "break_convention_invariance":
        claims["variant_relations_identical"] = False
        claims["variant_count"] = 1
    elif mutation == "break_shape_cross_degree":
        # THE CHECKER'S C5 CORRECTION DELETED: ALL cross-degree pairings are
        # asserted to be unconstrained.  Twelve of the twenty-two are forced
        # to zero by the three origin-plane shadows -- correction 108.
        claims["shape3_cross_zero"] = 0
        claims["shape3_cross_free"] = 22
    elif mutation == "break_six_face_shape":
        claims["shape6_rank"] = 14
        claims["shape6_manifold"] = 22
        claims["shape6_cross_free_complementary"] = False
    # --- E ----------------------------------------------------------------
    elif mutation == "break_six_face_literal":
        claims["six_face_ranks"] = (32, 32)
        claims["six_face_relation_count"] = 0
        claims["six_face_relations"] = ()
    elif mutation == "break_uniform_flat_point":
        # THE SUPERVISOR'S QUICK READING, UN-CORRECTED: only c^2 + v^2 = 1 is
        # asserted to survive on the uniform locus, so the curved point
        # (3/5, 4/5) would lie on it.  The companion numerator c^2 v was
        # missed, and it is the clause that forces the FLAT cell -- correction
        # 106, disclosed as a dead end rather than smoothed.
        claims["uniform_constraint_count"] = 1
        claims["uniform_constraints"] = (UNIFORM_CONSTRAINTS[0],)
        claims["uniform_solution"] = (sp.Rational(3, 5), sp.Rational(4, 5))
        claims["uniform_admits_only_flat"] = False
    elif mutation == "break_reciprocal_solvable":
        claims["reciprocal_ranks"] = (32, 33)
        claims["reciprocal_free_names"] = ()
    elif mutation == "break_positivity_verdict":
        # THE HEADLINE NEGATIVE DENIED: the indefinite principal blocks are
        # asserted to depend on the four free duality parameters, so that some
        # choice could rescue positivity.  They contain none of them.
        claims["blocks_parameter_free"] = False
        claims["curved_cell_pd"] = True
    # --- F ----------------------------------------------------------------
    elif mutation == "break_two_form_block":
        # THE SPEC'S PARAPHRASE, UN-CORRECTED: the 2-form block is asserted to
        # be det(g) Lambda^2(g^-1) with NO division by V.  That is E g E, which
        # equals the true block only on the slice V = 1 -- correction 107,
        # caught by the overnight batch check.
        claims["undivided_generic"] = True
        claims["two_form_division_load_bearing"] = False
    elif mutation == "break_gluing_law":
        claims["origin_restriction_law"] = False
        claims["opposite_restriction_law"] = True
        claims["plane_scale"] = 2
    elif mutation == "break_schur_residual":
        claims["landed_match_iff_decoupled"] = False
        claims["partial_correlation"] = False
    elif mutation == "break_shape_membership":
        # THE OVER-CONSTRAINT ERASED: D3 is asserted to lie in the shape
        # manifold at generic shears, which would remove the measured mismatch
        # between this declared candidate and the scout shape constraint.
        claims["membership_iff_equal"] = False
        claims["shape_zero_pattern"] = 0
    elif mutation == "break_three_d_couplings":
        claims["three_d_coupling_count"] = 0
        claims["three_d_invisible_origin"] = False
        claims["three_d_visible_opposite"] = False
        claims["cross_degree_zero"] = False
    elif mutation == "break_orientation_split":
        # THE ORIENTATION SPLIT COLLAPSED: both orientation classes are
        # asserted to admit the same kappa range.  The negative class stops at
        # one half and the positive class runs to one.
        claims["kappa_bounds"] = (sp.Integer(1), sp.Integer(1))
        claims["positivity_domain_splits"] = False
    # --- G ----------------------------------------------------------------
    elif mutation == "break_scout_grade_fence":
        claims["scout_grade_only"] = False
        claims["physical_content"] = True
    elif mutation == "claim_schur_equivalence":
        # THE CHECKER'S C5 QUALIFICATION DELETED: the Schur restriction and the
        # S5 record marginal are asserted to be THE SAME OPERATION.  Both
        # instantiate one algebraic template; no carrier map exists.
        claims["schur_equivalence"] = True
        claims["schur_template_only"] = False
        claims["same_operation"] = True
    elif mutation == "claim_principle_binds_nature":
        claims["principle_binds_nature"] = True
    elif mutation == "claim_signs_invariant":
        claims["signed_shear_invariance"] = True
        claims["convention_tied"] = 0
    elif mutation == "claim_landed_corrected":
        claims["landed_correction"] = True
        claims["landed_numbers_corrected"] = 1
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 0
        claims["positivity_all_branches"] = True
    # --- H ----------------------------------------------------------------
    elif mutation == "drop_n5_fence":
        claims["scope"] = {key: False for key in SCOPE_KEYS}
    elif mutation == "break_nsimplify_absence":
        claims["nsimplify_calls"] = 1
    elif mutation == "break_float_absence":
        claims["float_literals"] = 1
        claims["float_calls"] = 1
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    authority = facts.authority
    rule = facts.rule
    gluing = facts.gluing
    rigidity = facts.rigidity
    lift = facts.lift

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 202 artifacts are "
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
        "B-3", f"THE WORD *GEOMETRY* IS SCOPED BEFORE THE FIRST NUMERAL: it "
        f"names an 8 x 8 rational weight matrix on the corners of ONE cube, "
        f"required only to be symmetric and -- where positivity is at issue -- "
        f"positive definite; it names NO spacetime, NO metric field, NO "
        f"curvature and NO gravitational geometry, and the "
        f"{claims['unnamed_words']} words {UNNAMED_PHYSICS_WORDS} name "
        f"NOTHING established here",
        claims["geometry_is_spacetime"] is False
        and facts.unnamed_words == claims["unnamed_words"])
    checks.check(
        "B-4", "THE WORD *GLUING* IS SCOPED: it names a finite LINEAR "
        "consistency system among the plane restrictions of one symmetric "
        "matrix -- each equation an entry equality against the landed 2D cell "
        "form -- and it names NO evolution, NO propagation, NO field equation "
        "and NO dynamics of any kind",
        claims["gluing_is_dynamics"] is False)
    checks.check(
        "B-5", "THE WORD *RIGIDITY* IS SCOPED: it names the exact solution "
        "count of ONE specified gluing principle on the CHECKED branches -- "
        "the uniform locus, solved exactly, and one exhibited nonuniform "
        "point -- and it names NO uniqueness theorem about nature, NO no-go "
        "and NO classification of every branch",
        claims["rigidity_is_universal"] is False)
    checks.check(
        "B-6", "NO GENERIC-PARAMETER THEOREM, NO CONTINUUM LIMIT AND NO "
        "EQUATIONS OF MOTION: what is established is a set of exact "
        "finite-instance predicates over rational function fields in the "
        "moduli, and four extents with six faces are not a parameter space, "
        "not a limit and not a dynamics",
        claims["generic_parameter_theorem"] is False
        and claims["continuum_limit"] is False
        and claims["equations_of_motion"] is False)
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

    # --- C: THE 2+1D EXTENSION ----------------------------------------------
    checks.check(
        "C-1", f"THE COVARIANT RULE IN THREE DIRECTIONS IS AN ALGEBRA AND NOT "
        f"A CHOICE: the couplings are {COUPLING_FORM} with the staggering "
        f"{STAGGERING_FORM}; each of the three generators squares to I4 "
        f"({claims['generator_squares']}) and every one of the three distinct "
        f"pairs anticommutes exactly ({claims['generator_anticommute']}) -- "
        f"this is the first regime where the SPATIAL generators genuinely "
        f"refuse to commute with each other",
        rule.squares_identity == claims["generator_squares"]
        and all(claims["generator_squares"])
        and rule.anticommute == claims["generator_anticommute"]
        and all(claims["generator_anticommute"]))
    checks.check(
        "C-2", f"EVERY LINK SCALARIZES ON EVERY ALL-EVEN EXTENT, WITH THE "
        f"RE-DERIVED ETA PATTERN: on {EVEN_EXTENTS} the non-scalar counts per "
        f"direction are {claims['even_bad']} of {claims['even_links']} "
        f"directed links, none of them at a wrap {claims['even_bad_wrap']}, "
        f"and every surviving scalar equals eta_d / 2 for the pattern "
        f"{ETA_PATTERN} ({claims['even_eta']}) -- re-derived in-framework and "
        f"never borrowed",
        rule.even_bad == claims["even_bad"]
        and all(count == ZERO_RESIDUAL for row in claims["even_bad"]
                for count in row)
        and rule.even_bad_wrap == claims["even_bad_wrap"]
        and rule.even_links == claims["even_links"]
        and rule.even_eta == claims["even_eta"]
        and all(claims["even_eta"]))
    checks.check(
        "C-3", f"AND THE ODD-EXTENT OBSTRUCTION IS DIRECTION-LOCAL: on "
        f"{ODD_EXTENT} the non-scalar counts are {claims['odd_bad']} -- "
        f"EXACTLY {claims['odd_bad_total']} links, ALL of them in direction "
        f"{claims['odd_bad_direction']} which is the ONE odd extent, and ALL "
        f"of them at a wrap {claims['odd_bad_wrap']} -- while the eta pattern "
        f"still holds on every scalar link ({claims['odd_eta']})",
        rule.odd_bad == claims["odd_bad"]
        and rule.odd_bad_wrap == claims["odd_bad_wrap"]
        and rule.odd_bad == rule.odd_bad_wrap
        and rule.odd_bad_total == claims["odd_bad_total"]
        and claims["odd_bad_total"] > 0
        and rule.odd_bad_directions == (claims["odd_bad_direction"],)
        and rule.odd_eta is claims["odd_eta"])
    checks.check(
        "C-4", f"THE CELL SIGN MATRIX IS WELL-DEFINED AND THE WORD FORM IS "
        f"UNIQUE: sigma(a, b) takes values in {claims['sigma_values']} at all "
        f"{SIGMA_PAIRS} corner pairs and is well-defined at all "
        f"{SIGMA_ANCHORS} anchor parities ({claims['sigma_well_defined']}); "
        f"the word form f_ab = sigma_ab T_ab holds exactly for a GENERAL "
        f"symmetric target ({claims['word_form_exact']}); and the block "
        f"staggering Psi is orthogonal at size {PSI_SIZE} "
        f"({claims['psi_orthogonal']}), which is what makes the congruence "
        f"invertible and the coefficient unique",
        rule.sigma_rows == claims["sigma_rows"]
        and rule.sigma_values == claims["sigma_values"]
        and rule.sigma_well_defined == claims["sigma_well_defined"]
        and all(claims["sigma_well_defined"])
        and rule.word_form_exact is claims["word_form_exact"]
        and claims["word_form_exact"] is True
        and rule.psi_orthogonal is claims["psi_orthogonal"]
        and claims["psi_orthogonal"] is True)

    # --- D: THE GLUING SYSTEMS ----------------------------------------------
    checks.check(
        "D-1", f"THE LITERAL THREE-FACE GLUING IS OVER-DETERMINED, AND WHAT IT "
        f"FORCES IS A LOCUS AND NOT A POINT: {claims['three_face_equations']} "
        f"entry equations on {CELL_UNKNOWNS} unknowns have ranks "
        f"{claims['three_face_ranks']} at generic INDEPENDENT plane moduli, "
        f"and the cokernel returns EXACTLY "
        f"{claims['three_face_relation_count']} forced relations -- two "
        f"equal-volume and three equal-shear-square -- whose common zero locus "
        f"on the nonsingular domain is v_tx = v_ty = v_xy together with "
        f"c_tx^2 = c_ty^2 = c_xy^2, WITH THE THREE SHEAR SIGNS UNGLUED",
        gluing.three_face_equations == claims["three_face_equations"]
        and gluing.three_face_ranks == claims["three_face_ranks"]
        and claims["three_face_ranks"][0] != claims["three_face_ranks"][1]
        and len(gluing.three_face_relations)
        == claims["three_face_relation_count"]
        and claims["three_face_relation_count"] > 0
        and gluing.three_face_relations == tuple(
            sorted(claims["three_face_relations"])))
    checks.check(
        "D-2", f"AND EVERY ONE OF THOSE STATEMENTS IS CONVENTION-INVARIANT: "
        f"all {claims['variant_count']} order-swap by plane-flip variants "
        f"return the SAME ranks ({claims['variant_ranks_identical']}) and the "
        f"SAME forced relations ({claims['variant_relations_identical']}), "
        f"against a sign matrix already measured well-defined at all "
        f"{SIGMA_ANCHORS} anchor parities by family C",
        len(gluing.variant_ranks) == claims["variant_count"]
        and claims["variant_count"] == CONVENTION_VARIANTS
        and (len(set(gluing.variant_ranks)) == 1)
        is claims["variant_ranks_identical"]
        and claims["variant_ranks_identical"] is True
        and (len(set(gluing.variant_relations)) == 1)
        is claims["variant_relations_identical"]
        and claims["variant_relations_identical"] is True)
    checks.check(
        "D-3", f"THE THREE-FACE SHAPE-ONLY MANIFOLD, AND THE CROSS-DEGREE "
        f"COUNT IS NOT A BLANKET: rank {claims['shape3_rank']} leaves a "
        f"{claims['shape3_manifold']}-dimensional manifold with "
        f"{claims['shape3_survivors']} nonzero entries; of the "
        f"{SHAPE3_CROSS_DEGREE_PAIRS} cross-degree pairs EXACTLY "
        f"{claims['shape3_cross_zero']} are FORCED ZERO by the three "
        f"origin-plane shadows and only {claims['shape3_cross_free']} are "
        f"free, and the three 1-form diagonals are ONE shared parameter "
        f"({claims['shape3_one_form_equal']})",
        gluing.shape3_rank == claims["shape3_rank"]
        and gluing.shape3_manifold == claims["shape3_manifold"]
        and gluing.shape3_manifold == CELL_UNKNOWNS - claims["shape3_rank"]
        and gluing.shape3_survivors == claims["shape3_survivors"]
        and gluing.shape3_cross_zero == claims["shape3_cross_zero"]
        and claims["shape3_cross_zero"] > 0
        and gluing.shape3_cross_free == claims["shape3_cross_free"]
        and claims["shape3_cross_zero"] + claims["shape3_cross_free"]
        == SHAPE3_CROSS_DEGREE_PAIRS
        and gluing.shape3_one_form_equal is claims["shape3_one_form_equal"])
    checks.check(
        "D-4", f"AND THE SIX-FACE SHAPE-ONLY MANIFOLD IS EXACTLY THE "
        f"DIRAC-KAHLER DEGREE STRUCTURE: rank {claims['shape6_rank']} leaves "
        f"{claims['shape6_manifold']} dimensions and "
        f"{claims['shape6_survivors']} nonzero entries, censused as "
        f"{claims['shape6_parameter_census']} for (shared degree diagonals, "
        f"within-degree couplings, cross-degree survivors); the three 1-form "
        f"diagonals are equal ({claims['shape6_one_form_equal']}) and so are "
        f"the three 2-form diagonals ({claims['shape6_two_form_equal']}); "
        f"within-degree freedom is {claims['shape6_within_degree_free']}; and "
        f"the ONLY surviving cross-degree couplings are the four "
        f"HODGE-COMPLEMENTARY pairs {claims['shape6_cross_free_pairs']} -- the "
        f"0-3 duality pairing and the three 1-2s "
        f"({claims['shape6_cross_free_complementary']})",
        gluing.shape6_rank == claims["shape6_rank"]
        and gluing.shape6_manifold == claims["shape6_manifold"]
        and gluing.shape6_manifold == CELL_UNKNOWNS - claims["shape6_rank"]
        and gluing.shape6_survivors == claims["shape6_survivors"]
        and gluing.shape6_cross_free_pairs
        == claims["shape6_cross_free_pairs"]
        and gluing.shape6_cross_free_complementary
        is claims["shape6_cross_free_complementary"]
        and claims["shape6_cross_free_complementary"] is True
        and gluing.shape6_one_form_equal is claims["shape6_one_form_equal"]
        and gluing.shape6_two_form_equal is claims["shape6_two_form_equal"]
        and gluing.shape6_within_degree_free
        == claims["shape6_within_degree_free"]
        and gluing.shape6_parameter_census
        == claims["shape6_parameter_census"]
        and sum(claims["shape6_parameter_census"])
        == claims["shape6_manifold"])

    # --- E: THE RIGIDITY CHAIN ----------------------------------------------
    checks.check(
        "E-1", f"THE SIX-FACE LITERAL SYSTEM ADDS RECIPROCAL CROSS-OFFSET "
        f"COUPLINGS: {claims['six_face_equations']} entry equations have ranks "
        f"{claims['six_face_ranks']} at generic independent PER-FACE moduli, "
        f"with EXACTLY {claims['six_face_relation_count']} forced relations -- "
        f"four per-offset equal-volume, four per-offset equal-shear-square, "
        f"and EIGHT reciprocal cross-offset couplings, of which "
        f"'c_tx1**2 + v_tx1*v_ty0 - 1' is one: opposite faces of a direction "
        f"are tied by v_tx1 v_ty0 = 1 - c_tx1^2 and not merely by equality",
        rigidity.six_face_equations == claims["six_face_equations"]
        and rigidity.six_face_ranks == claims["six_face_ranks"]
        and claims["six_face_ranks"][0] != claims["six_face_ranks"][1]
        and len(rigidity.six_face_relations)
        == claims["six_face_relation_count"]
        and claims["six_face_relation_count"] > 0
        and rigidity.six_face_relations == tuple(
            sorted(claims["six_face_relations"])))
    checks.check(
        "E-2", f"ON THE UNIFORM LOCUS THE ONLY SOLUTION IS THE FLAT CELL: the "
        f"twelve face moduli collapsed to one pair leave EXACTLY "
        f"{claims['uniform_constraint_count']} surviving numerators "
        f"{claims['uniform_constraints']} -- BOTH of them, and the second is "
        f"the one a quick reading misses -- and their joint solution over "
        f"v > 0 with c real is the SINGLE point (c, v) = "
        f"{claims['uniform_solution']}, so uniform literal gluing admits ONLY "
        f"the flat cell ({claims['uniform_admits_only_flat']})",
        rigidity.uniform_constraints == tuple(
            sorted(claims["uniform_constraints"]))
        and len(rigidity.uniform_constraints)
        == claims["uniform_constraint_count"]
        and claims["uniform_constraint_count"] == 2
        and rigidity.uniform_solutions == (claims["uniform_solution"],)
        and claims["uniform_admits_only_flat"] is True)
    checks.check(
        "E-3", f"THE ONE EXHIBITED NONUNIFORM POINT IS SOLVABLE, AND ITS "
        f"FREEDOM IS EXACTLY THE DUALITY PAIRINGS: at (c, v0, v1, c1) = "
        f"{claims['reciprocal_moduli']} -- with v1 and c1 DERIVED from the "
        f"reciprocal relation of E-1 rather than chosen -- the six-face "
        f"literal system has ranks {claims['reciprocal_ranks']} and is "
        f"CONSISTENT, leaving exactly {RECIPROCAL_FREE_COUNT} free parameters "
        f"{claims['reciprocal_free_names']}, which are the four "
        f"Hodge-complementary corner pairs and nothing else",
        rigidity.reciprocal_moduli == claims["reciprocal_moduli"]
        and rigidity.reciprocal_ranks == claims["reciprocal_ranks"]
        and claims["reciprocal_ranks"][0] == claims["reciprocal_ranks"][1]
        and rigidity.reciprocal_free_names
        == claims["reciprocal_free_names"]
        and len(claims["reciprocal_free_names"]) == RECIPROCAL_FREE_COUNT)
    checks.check(
        "E-4", f"AND THAT CURVED CELL IS NEVER A GEOMETRY, BY NECESSITY AND "
        f"NOT BY SEARCH: its degree-1 and degree-2 PRINCIPAL blocks carry the "
        f"exact spectra {claims['degree_one_spectrum']} and "
        f"{claims['degree_two_spectrum']}, each contains a NEGATIVE "
        f"eigenvalue, and neither contains ANY of the four free symbols "
        f"({claims['blocks_parameter_free']}); a principal submatrix of a "
        f"positive definite matrix must be positive definite, so NO choice of "
        f"the four duality pairings can rescue it "
        f"({claims['curved_cell_pd']}) -- and the rigidity statement therefore "
        f"stands ON THE CHECKED BRANCHES "
        f"({claims['rigidity_on_checked_branches']})",
        rigidity.degree_spectra[1] == claims["degree_one_spectrum"]
        and rigidity.degree_spectra[2] == claims["degree_two_spectrum"]
        and rigidity.negative_eigenvalue_blocks[1]
        and rigidity.negative_eigenvalue_blocks[2]
        and all(rigidity.blocks_parameter_free)
        is claims["blocks_parameter_free"]
        and claims["blocks_parameter_free"] is True
        and claims["curved_cell_pd"] is False
        and claims["rigidity_on_checked_branches"] is True)

    # --- F: THE DECLARED STANDARD CANDIDATE AND ITS RESTRICTION LAW ---------
    checks.check(
        "F-1", f"THE DECLARED D3 CANDIDATE IS CONSTRUCTED AND ITS VOLUME DIVISION IS "
        f"LOAD-BEARING: D3(g, V) = diag(V, V g^-1, E g E / V, 1/V) with "
        f"E = diag{WEDGE_SIGNATURE}; the Jacobi complementary-minor identity "
        f"Lambda^2(g^-1) = E g E / det g holds exactly "
        f"({claims['jacobi_exact']}); the 2-form block equals BOTH the duality "
        f"image J W1^-1 J^T and det(g) Lambda^2(g^-1) / V; the top weight is "
        f"1/W0 ({claims['two_form_duality']}); and the UN-DIVIDED paraphrase "
        f"det(g) Lambda^2(g^-1) does NOT match generically "
        f"({claims['undivided_generic']}) while it DOES match on the slice "
        f"V = 1 ({claims['undivided_at_unit_volume']}), which is exactly why "
        f"the division is load-bearing "
        f"({claims['two_form_division_load_bearing']})",
        lift.jacobi_exact is claims["jacobi_exact"]
        and claims["jacobi_exact"] is True
        and lift.two_form_matches_duality and lift.two_form_matches_compound
        and lift.top_is_dual is claims["two_form_duality"]
        and lift.undivided_matches_generically is claims["undivided_generic"]
        and claims["undivided_generic"] is False
        and lift.undivided_matches_at_unit_volume
        is claims["undivided_at_unit_volume"]
        and claims["undivided_at_unit_volume"] is True
        and claims["two_form_division_load_bearing"] is True)
    checks.check(
        "F-2", f"THE ORIGIN-FACE SCHUR IDENTITY AND ITS OPPOSITE-FACE "
        f"BOUNDARY: each of the three degree-(0,1,1,2) origin faces equals "
        f"diag(V, V S_p^-1, 1/V) ({claims['origin_restriction_law']}), while "
        f"the degree-(1,2,2,3) opposite faces do not "
        f"({claims['opposite_restriction_law']}); at the exact rational "
        f"counterpoint their residual nnz counts are "
        f"{claims['opposite_restriction_nnz']} with representative (0,0) "
        f"defects {claims['opposite_representative_defects']}.  No unbuilt "
        f"local regrading or transport map is assumed.  On the origin faces, "
        f"matching lambda_p * shear_hodge(c_p, v_p) against the 0- and 2-form "
        f"sectors alone FORCES lambda_p = {claims['plane_scale']} and v_p = V "
        f"({claims['plane_volume_is_cell_volume']}), so no per-plane scale "
        f"survives; and det S_p = det g for every plane "
        f"({claims['schur_determinant']}), each plane's conditioned metric "
        f"carrying the FULL 3D volume distortion",
        lift.origin_restriction_law_exact
        is claims["origin_restriction_law"]
        and claims["origin_restriction_law"] is True
        and lift.opposite_restriction_law_exact
        is claims["opposite_restriction_law"]
        and claims["opposite_restriction_law"] is False
        and lift.opposite_restriction_residual_nnz
        == claims["opposite_restriction_nnz"]
        and all(value > 0 for value in claims["opposite_restriction_nnz"])
        and lift.opposite_representative_defects
        == claims["opposite_representative_defects"]
        and lift.plane_scale == claims["plane_scale"]
        and claims["plane_scale"] == 1
        and (lift.plane_volume == sp.Symbol("V", positive=True))
        is claims["plane_volume_is_cell_volume"]
        and lift.schur_determinant_identity is claims["schur_determinant"]
        and claims["schur_determinant"] is True)
    checks.check(
        "F-3", f"THE EFFECTIVE PLANE SHEAR IS THE PARTIAL CORRELATION, AND THE "
        f"LANDED MATCH IS AN IFF: on the per-plane isotropy locus the 1-form "
        f"block is [1/(1 - kappa_p^2)] V g2(c_p)^-1 with c_p the conditioned "
        f"off-diagonal ({claims['partial_correlation']}), the residual against "
        f"a landed shear_hodge(c_p, V) is EXACTLY "
        f"{ONE_FORM_RESIDUAL_FORM} so it vanishes iff kappa_p = 0, and at "
        f"c_ty = c_xy = 0 the tx restriction equals the landed form entry for "
        f"entry ({claims['landed_match_iff_decoupled']}); the phrase 'the "
        f"shear IS the partial correlation' needs its DIAGONAL NORMALISATION "
        f"stated ({claims['partial_correlation_normalisation']}), because the "
        f"Schur diagonal is not unity off that locus",
        lift.partial_correlation_on_locus is claims["partial_correlation"]
        and claims["partial_correlation"] is True
        and lift.landed_match_residual_exact
        and lift.landed_match_at_decoupled
        is claims["landed_match_iff_decoupled"]
        and claims["landed_match_iff_decoupled"] is True
        and (not lift.schur_diagonal_is_unit)
        is claims["partial_correlation_normalisation"]
        and claims["partial_correlation_normalisation"] is True)
    checks.check(
        "F-4", f"THE DECLARED D3 CANDIDATE MEETS THE SCOUT SHAPE ONLY ON THE "
        f"EQUAL-MAGNITUDE LOCUS: all {claims['shape_zero_pattern']} zero-"
        f"pattern constraints hold IDENTICALLY, the equal-1-form-diagonal "
        f"residuals are exactly {EQUAL_DIAGONAL_RESIDUAL_FORM} per plane, "
        f"they are NONZERO at a generic moduli point, and they all vanish iff "
        f"c_tx^2 = c_ty^2 = c_xy^2 ({claims['membership_iff_equal']}) -- so "
        f"D3 is in the shape manifold on that locus and NOT generically",
        lift.zero_pattern_identical == claims["shape_zero_pattern"]
        and claims["shape_zero_pattern"] == len(SHAPE_ZERO_POSITIONS) * 3
        and lift.membership_iff_equal is claims["membership_iff_equal"]
        and claims["membership_iff_equal"] is True
        and lift.membership_generic is True)
    checks.check(
        "F-5", f"THE GENUINELY 3D COUPLINGS ARE THE THREE 2-FORM/2-FORM "
        f"CROSSES AND NOTHING ELSE: <dx^dy, dt^dy> = -c_tx/V, "
        f"<dx^dy, dt^dx> = +c_ty/V and <dt^dy, dt^dx> = -c_xy/V, signs "
        f"{THREE_D_COUPLING_SIGNS}, {claims['three_d_coupling_count']} of them. "
        f"Each origin face contains only one 2-form and therefore hides these "
        f"pairings ({claims['three_d_invisible_origin']}), but each opposite "
        f"face contains a 2-form pair and exposes one generically "
        f"({claims['three_d_visible_opposite']}); every "
        f"cross-degree pairing of D3 is exactly zero "
        f"({claims['cross_degree_zero']}), so the declared candidate turns "
        f"on nothing off-degree at all",
        all(value == ZERO_RESIDUAL for value in lift.three_d_couplings)
        and len(lift.three_d_couplings) == claims["three_d_coupling_count"]
        and claims["three_d_coupling_count"] == THREE_D_COUPLING_COUNT
        and lift.origin_two_form_pair_counts == (0, 0, 0)
        and claims["three_d_invisible_origin"] is True
        and lift.opposite_two_form_pair_counts == (1, 1, 1)
        and claims["three_d_visible_opposite"] is True
        and lift.cross_degree_zero is claims["cross_degree_zero"]
        and claims["cross_degree_zero"] is True)
    checks.check(
        "F-6", f"ON THE ISOTROPIC LOCUS THE POSITIVITY DOMAIN SPLITS BY "
        f"ORIENTATION CLASS: all {ISOTROPIC_SIGN_PATTERNS} sign patterns "
        f"satisfy the equal-scale and equal-shear-square relations "
        f"({claims['isotropic_relations']}), and they fall into exactly "
        f"{claims['orientation_classes']} classes by "
        f"eps = sign(c_tx c_ty c_xy) -- det g = "
        f"{DETERMINANT_AT_POSITIVE_ORIENTATION} at eps = +1 against "
        f"{DETERMINANT_AT_NEGATIVE_ORIENTATION} at eps = -1 -- whose "
        f"admissible ranges end at kappa = {claims['kappa_bounds'][0]} and "
        f"kappa = {claims['kappa_bounds'][1]} respectively "
        f"({claims['positivity_domain_splits']}): the negative-class interval "
        f"endpoint is one half of the positive-class endpoint.  Sylvester's "
        f"other leading minors are exactly 1 and 1-kappa^2 in every sign "
        f"pattern, so the determinant root is not used in isolation",
        lift.isotropic_relations is claims["isotropic_relations"]
        and claims["isotropic_relations"] is True
        and len(lift.orientation_determinants) == ISOTROPIC_SIGN_PATTERNS
        and len({sign for sign, _ in lift.orientation_determinants.values()})
        == claims["orientation_classes"]
        and all(minors[0] == 1 and sp.expand(
            minors[1] - (1 - sp.Symbol("kappa") ** 2)) == 0
                for minors in lift.orientation_leading_minors.values())
        and lift.kappa_bounds == claims["kappa_bounds"]
        and (claims["kappa_bounds"][0] != claims["kappa_bounds"][1])
        is claims["positivity_domain_splits"]
        and claims["positivity_domain_splits"] is True)

    # --- G: THE SIX SCOPE FENCES -------------------------------------------
    checks.check(
        "G-1", f"FENCE ONE -- ALL OF IT IS SCOUT-GRADE FINITE EXACT LINEAR "
        f"ALGEBRA: scout_grade_only = {claims['scout_grade_only']}, "
        f"finite_linear_algebra = {claims['finite_linear_algebra']}, and "
        f"physical_content = {claims['physical_content']}; no continuum, no "
        f"dynamics and no gravity is supplied by any line of this block, and "
        f"the nine unsupplied gravity structures are enumerated separately at "
        f"B-2, so neither leans on the other",
        claims["scout_grade_only"] is True
        and claims["finite_linear_algebra"] is True
        and claims["physical_content"] is False)
    checks.check(
        "G-2", f"FENCE TWO -- THE SCHUR STATEMENT IS AN ALGEBRAIC TEMPLATE "
        f"INSTANTIATION AND NEVER AN OBJECT-LEVEL EQUIVALENCE: "
        f"schur_template_only = {claims['schur_template_only']}, "
        f"schur_equivalence = {claims['schur_equivalence']}, "
        f"carrier_map_constructed = {claims['carrier_map']} and "
        f"same_operation = {claims['same_operation']}; the ONLY licensed "
        f"phrase for the comparison with the S5 record marginal is "
        f"'{LICENSED_ECHO_PHRASE}', because no map between carriers is built "
        f"and no commuting statement is proved by any line here",
        claims["schur_template_only"] is True
        and claims["schur_equivalence"] is False
        and claims["carrier_map"] is False
        and claims["same_operation"] is False)
    checks.check(
        "G-3", f"FENCE THREE -- 'THE SHAPE PRINCIPLE OVER-CONSTRAINS' IS ABOUT "
        f"THE PRINCIPLE AND NEVER ABOUT NATURE: "
        f"over_constrains_principle = {claims['over_constrains_principle']} "
        f"relative to the full positive D3(g, V) family, whose generic members "
        f"its equal-diagonal rule rejects; principle_binds_nature = "
        f"{claims['principle_binds_nature']}, since establishing that would "
        f"need an independent reason the rejected geometries MUST be "
        f"admissible, and this block supplies none",
        claims["over_constrains_principle"] is True
        and claims["principle_binds_nature"] is False)
    checks.check(
        "G-4", f"FENCE FOUR -- E AND THE SHEAR SIGNS ARE CONVENTION-TIED AND "
        f"THE SQUARES ARE THE INVARIANTS: {claims['convention_tied']} "
        f"convention-tied objects are enumerated ({CONVENTION_TIED_OBJECTS}); "
        f"squared_shear_invariant = {claims['squared_shear_invariant']} and "
        f"signed_shear_invariance = {claims['signed_shear_invariance']}, so "
        f"reorienting or reordering the wedge basis CONJUGATES the displayed "
        f"signs and individual effective shears can differ in sign while their "
        f"squares agree; the one place a sign is nevertheless invariant "
        f"content -- the orientation class of F-6 -- is gated there and not "
        f"here",
        claims["convention_tied"] == len(CONVENTION_TIED_OBJECTS)
        and claims["convention_tied"] > 0
        and claims["squared_shear_invariant"] is True
        and claims["signed_shear_invariance"] is False
        and EFFECTIVE_SHEARS_MAY_DIFFER_IN_SIGN is True)
    checks.check(
        "G-5", f"FENCE FIVE -- THE LANDED 2D FORM IS THE NO-THIRD-DIRECTION "
        f"SPECIAL CASE AND NOTHING HERE CORRECTS IT: landed_special_case = "
        f"{claims['landed_special_case']}, its within-plane isotropy being the "
        f"statement that a 2D cell has no third direction to condition on; "
        f"landed_numbers_corrected = {claims['landed_numbers_corrected']} and "
        f"landed_correction = {claims['landed_correction']}, so Block 105's "
        f"shear_hodge and every number built on it STAND EXACTLY AS LANDED and "
        f"this block only reads them",
        claims["landed_special_case"] is True
        and claims["landed_numbers_corrected"] == ZERO_RESIDUAL
        and claims["landed_correction"] is False)
    checks.check(
        "G-6", f"FENCE SIX -- THE INSTANCE SCOPE, ENUMERATED RATHER THAN "
        f"GESTURED AT: {claims['instance_scope']} restrictions "
        f"({INSTANCE_SCOPE}), scope_generalisation = "
        f"{claims['scope_generalisation']}, and -- the sharpest of them -- "
        f"positivity_all_branches = {claims['positivity_all_branches']}: this "
        f"block solves the UNIFORM locus exactly and exhibits ONE nonuniform "
        f"point, and it does NOT classify positivity over every nonuniform "
        f"six-face-compatible branch, so 'literal gluing plus positivity gives "
        f"the flat cell' is true ON THE CHECKED BRANCHES and is not asserted "
        f"wider; the checked-branch qualifier itself is gated at E-4 and the "
        f"scoped word RIGIDITY at B-5, so no two of them lean on each other",
        claims["instance_scope"] == len(INSTANCE_SCOPE)
        and claims["instance_scope"] == INSTANCE_SCOPE_COUNT
        and claims["instance_scope"] > 0
        and claims["scope_generalisation"] is False
        and claims["positivity_all_branches"] is False)

    # --- H: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE -------------------
    checks.check(
        "H-1", f"the note is present at {NOTE_PATH.name} and all five "
        f"substantive N5 resolution lines appear in it verbatim",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "H-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn the -3/20 eigenvalue that kills the curved cell's "
        f"positivity into a zero and reinstate the geometry this block reports "
        f"as IMPOSSIBLE",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "H-3", f"and {claims['float_literals']} float literals appear in that "
        f"same source with EXACTLY {claims['float_calls']} float call sites, "
        f"both MEASURED by an AST walk rather than by a text search -- this is "
        f"TIGHTER than Block 202's 'exactly one', because every number this "
        f"block reports is a short exact rational and NOTHING here is ever "
        f"converted to a decimal",
        facts.float_literals == claims["float_literals"]
        and facts.float_calls == claims["float_calls"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    rule, gluing, rigidity, lift = (
        facts.rule, facts.gluing, facts.rigidity, facts.lift)
    print(f"MEASURED elapsed={elapsed_ns // 1000000000}s main={facts.main_head}")
    print(f"C even_bad={rule.even_bad} odd_bad={rule.odd_bad} "
          f"sigma={rule.sigma_well_defined} word={rule.word_form_exact}")
    print(f"D three_literal={gluing.three_face_ranks} "
          f"shape3={gluing.shape3_rank}/{gluing.shape3_manifold} "
          f"shape6={gluing.shape6_rank}/{gluing.shape6_manifold}")
    print(f"E six_literal={rigidity.six_face_ranks} "
          f"uniform={rigidity.uniform_solutions} reciprocal="
          f"{rigidity.reciprocal_ranks} spectra={rigidity.degree_spectra}")
    print(f"F origin_schur={lift.origin_restriction_law_exact} "
          f"opposite_schur={lift.opposite_restriction_law_exact} "
          f"opposite_nnz={lift.opposite_restriction_residual_nnz} "
          f"defects={lift.opposite_representative_defects} "
          f"bounds={lift.kappa_bounds}")
    print("SCOPE D3 is a declared finite exterior-algebra candidate; origin and "
          "opposite faces are distinct; no physical selection or continuum is adopted")


N5_FENCE = "\n".join((
    "N5: per_element: The three generator matrices, corner grading, plane targets, and D3(g,V) are declared finite algebraic objects. Their exact identities do not select a physical rule, metric field, spacetime, dynamics, gravity law, or continuum limit; nothing is registered or adopted.",
    "per_site: On the three tested all-even extents every directed link scalarizes with the stated eta pattern, while (4,3,2) has exactly eight non-scalar x-wrap links. This is a finite parity count for the declared generators, not an all-extent theorem.",
    "per_mode: The three-origin-face literal system has ranks (22,23) with five overlap relations; the six-face system has ranks (32,33) with sixteen. On the uniform positive-volume locus the two exact constraints give only (c,v)=(0,1); one reciprocal curved point is solvable but has parameter-free indefinite principal blocks. Other nonuniform branches remain unclassified.",
    "per_block: The standard exterior-algebra candidate D3=diag(V,V g^-1,E g E/V,1/V) obeys the compound identities and the Schur target on the three origin faces only. The same target fails on the three opposite faces with exact residual counts (5,5,5) because the global degree pattern changes; no local regrading or transport is supplied.",
    "lattice_wide: On the tested isotropic metric locus, Sylvester minors give positivity endpoints kappa=1 and kappa=1/2 for the two product-sign classes. This does not classify all compatible cells, choose D3 over other lifts, or establish physical geometry; all content remains finite-instance proposed_retained and TOE movement is zero.",
))


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
