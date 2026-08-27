#!/usr/bin/env python3
"""BLOCK 211 -- THE SIX-FACE POSITIVITY CLASSIFICATION: BLOCK 209's NAMED OPEN
BRANCH IS CLOSED, THE COMPATIBLE MODULI VARIETY IS EXACTLY THE
PER-OFFSET-ISOTROPIC FAMILY, AND THE NATURAL FLAT-ONLY EXTENSION IS REFUTED --
CURVED POSITIVE CELLS EXIST AND ARE CLASSIFIED BY PER-OFFSET ORIENTATION AND
MAGNITUDE.

THE RESULT, AND ITS EXACT SCOPE.  Block 209 landed a rigidity statement scoped
'ON THE CHECKED BRANCHES', with positivity explicitly NOT classified over the
nonuniform six-face-compatible branches.  This block CLASSIFIES it.  Four exact
packages come back.  NOT ONE OF THEM SUPPLIES A SPACETIME, A DYNAMICS OR A
GRAVITY, and the note says so in those words before it says anything else.

  (i) THE VARIETY IS EXACTLY THE PER-OFFSET-ISOTROPIC FAMILY.  The six-face
      literal system's coefficient matrix is CONSTANT with exactly four zero
      columns -- D07, D16, D25, D34 -- and rank 32 on the other 32, so
      solvability at a moduli point is exactly the vanishing of Block 209's
      sixteen landed relations.  Every relation is EVEN in every shear.  The
      relations reduce, using EXACTLY TWO divisions and BOTH by volumes, to
      per-offset common volumes and per-offset common shear magnitudes tied by
      v1 (1 - g0^2) = v0 and g1^2 = 1 - v0 v1, equivalently
      v0^2 = (1 - g0^2)(1 - g1^2).  The converse polynomial normal form kills
      all sixteen identically: NO non-isotropic branch exists.  Signs enter
      only through the per-offset sign PRODUCTS: 64 sign cells in 4 gauge
      classes, 16 Zariski components.  THE UNIFORM LOCUS STILL FORCES EXACTLY
      (c, v) = (0, 1).

 (ii) THE BLOCKS ARE PARAMETER-FREE AT SYMBOLIC MODULI IN ALL SIGN CLASSES.
      Solvability always leaves exactly the four duality parameters, ABSENT
      from every degree block: deg-0 = [v0], deg-1 = v1 M1(g0, signs),
      deg-2 = (1/v0) M2(g1, signs), deg-3 = [1/v1], with
      det M = (1 + g)^2 (1 - 2 g) at pi = +1 and (1 - g)^2 (1 + 2 g) at
      pi = -1.  THAT PAIR IS AN EXACT ECHO OF BLOCK 209's D3 kappa BOUNDS WITH
      THE CLASS LABEL NEGATED -- NOTED HERE AND NEVER INTERPRETED.

(iii) THE CLASSIFICATION.  D is PD-solvable at a compatible point IFF
      gamma0 < 1/2 when pi0 = +1 (any gamma0 < 1 when pi0 = -1) AND,
      independently, the same for (gamma1, pi1).  Every gauge class therefore
      carries a TWO-PARAMETER curved PD family.  Grid census over 32 exact
      solves: (+,+) 3/8, (+,-) 3/8, (-,+) 3/8, (-,-) 8/8.

 (iv) THE WITNESSES, AND THE LANDED POINT RECONCILED.  W1 (magnitudes 1/4,
      all-plus) and W2 (magnitudes 3/4, class (-,-)) are positive definite by
      explicit exact minors; W3 IS THE LANDED MAGNITUDES (3/5, 4/5) WITH ONE
      SIGN FLIPPED PER OFFSET and it is PD at the very magnitudes Block 209
      proved indefinite all-plus -- THE KILLER WAS THE SIGN PATTERN, NOT THE
      CURVATURE.  Block 209's exhibited all-plus point is verified STILL
      INDEFINITE with its landed spectra (-3/20, 6/5 x2) and (-5/4, 15/4 x2).

BLOCK 209 IS COMPLETED, NOT CORRECTED.  Its 'on the checked branches' scoping
held EXACTLY; this block closes the branch it named open, and every landed
number stands.

THE WORDS ARE FENCED BEFORE THE FIRST NUMBER IS READ.  'CLASSIFICATION' names
the exact PD region of ONE gluing principle's compatible variety, and names no
uniqueness about nature and no selection among geometries.  'ORIENTATION' names
a product of three shear signs inside one declared convention, and names no
spacetime orientation, no chirality and no physical parity.  'WITNESS' names an
exact rational matrix with positive leading minors, and names no observation
and no measurement.

ALL OF IT IS SCOUT-GRADE FINITE EXACT LINEAR ALGEBRA OVER QQ AND OVER RATIONAL
FUNCTION FIELDS IN THE MODULI.  NONE OF IT SUPPLIES GRAVITY, A DYNAMICS, A
CONTINUUM LIMIT OR A GENERIC-PARAMETER THEOREM.

GATES
  A  AUTHORITY: the five-pin authority block, the TWO Block 210 artifacts
     content-bound at PARENT_COMMIT and in the worktree, the audit inputs
     readable, and the stale pin -- the Block 209 tip -- verified to be a REAL
     ancestor of HEAD that carries NEITHER artifact.
  B  THE BANNER AND THE FENCE: six imposed objects, ZERO registered and ZERO
     adopted, with gravity supply, CLASSIFICATION-as-universal,
     ORIENTATION-as-physical, WITNESS-as-observation, a generic-parameter
     theorem, a continuum limit, equations of motion and licensed readings ALL
     declared NOT CLAIMED as measured constants, and nine gravity structures
     enumerated as NOT SUPPLIED.
  C  THE VARIETY: the constant coefficient matrix with its four zero duality
     columns; the evenness and the TWO volume divisions; the two ties with the
     converse normal form and NO non-isotropic branch; the 64 sign cells, the
     corner-sign gauge and its four classes; and the uniform locus still
     forced to the flat cell.
  D  THE BLOCKS AND THE CLASSIFICATION: symbolic solvability with
     duality-only freedom and parameter-free blocks in ALL four classes; the
     exact degree-block formulas with the {0,7} decoupling and the gauge
     congruence; the orientation determinants with the class-negated Block 209
     echo; the closed PD region; and the 32-point grid census.
  E  THE WITNESSES AND THE LANDED-POINT RECONCILIATION: W1 and the refutation;
     W2 and W3 across the sign classes; the open bounded duality region; and
     Block 209's exhibited point reproduced unchanged.
  F  THE SIX SCOPE FENCES, EACH A MEASURED CONSTANT: scout grade; the
     orientation echo NOTED and NEVER INTERPRETED; the sign PRODUCTS as the
     invariant content against convention-tied individual signs; Block 209
     COMPLETED and NOT CORRECTED; CLASSIFICATION as one principle's PD region
     and never a selection principle; and the instance scope.
  G  the note at its final path, the N5 fence byte-identical, and the
     nsimplify, float-literal and float CALL-SITE counts all measured ZERO in
     this file's own source.

BASELINE EXPECTATION: A through G PASS with the note landed at docs/.

MUTATIONS
  THE SWEEP CONTRACT: thirty-one declared mutations, each of which rewrites ONE
  CLAIM and must flip EXACTLY ONE FAMILY to FAIL.  Every measurement happens
  once, before any mutation flag is consulted, so a mutation can only rewrite a
  CLAIM and no gate can cascade into another.  The per-family census is
  A 2, B 6, C 5, D 5, E 4, F 6, G 3, run against thirty-one checks with the
  same per-family census.
  ONE OF THE THIRTY-ONE GUARDS THIS BLOCK's OWN CORRECTION RATHER THAN A
  RESULT: break_witness_w1 asserts the supervising record's announced flat-only
  extension -- 'literal gluing plus positivity admits exactly the flat cell'
  over the nonuniform branches -- which W1 refutes outright.  It is correction
  111 and it is disclosed as the adversarial path working, not smoothed.

RUNNING
  python3 scripts/admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27.py
  python3 ... --list-mutations
  python3 ... --mutation break_witness_w1
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

# THE MACHINERY IMPORT, LANDED, AND IT IS EXACTLY TWO OBJECTS.  The first is
# Block 105's shear_hodge(c, v), reached through Block 128's own import of it,
# so the 2D cell form every face equation is written against is the LANDED one
# and never a rebuild.  The second is Block 209's own runner: this block CLOSES
# the branch Block 209 named open, so its sixteen forced relations, its uniform
# numerators, its reciprocal point and its two degree spectra are read from the
# LANDED literals rather than retyped, and the reconciliation of family E is a
# comparison against the landed record itself.
try:
    import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128
    LANDED_SHEAR_HODGE = b128.block105.shear_hodge
    BENCH_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b128 = None
    LANDED_SHEAR_HODGE = None
    BENCH_IMPORT_LANDED = False
try:
    import admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26 as b209
    PARENT_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b209 = None
    PARENT_IMPORT_LANDED = False
MACHINERY_IMPORT_LANDED = BENCH_IMPORT_LANDED and PARENT_IMPORT_LANDED

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_SIX_FACE_POSITIVITY_CLASSIFICATION_BOUNDED_"
    "THEOREM_NOTE_2026-08-27.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 210 is the commit this block's
# branch is cut from; its note and its runner both exist at PARENT_COMMIT and
# NEITHER exists at STALE_PARENT_COMMIT, which is the Block 209 tip.  THE
# SCIENTIFIC PARENT IS BLOCK 209, whose named open branch this block closes;
# its artifacts stay in AUDIT_INPUT_PATHS and its runner is imported above.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFINED_ALPHABET_MACROREALIST_LANDSCAPE_"
    "BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_refined_alphabet_macrorealist_"
    "landscape_2026_08_26.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "7276872d3853f6a45f7026c1aa5ea47e787529b7",
    "db0a14491840bc1726d869109de5e287972ce71a",
)
# THE CONSTRUCTION AUTHORITY.  Block 209 supplies the six-face literal system,
# its sixteen forced relations and the landed reciprocal point; Block 128
# supplies the import path to Block 105's landed shear_hodge.
BLOCK209_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_"
    "THEOREM_NOTE_2026-08-26.md"
)
BLOCK209_RUNNER = (
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_"
    "2026_08_26.py"
)
BLOCK128_RUNNER = (
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py"
)
CAMPAIGN_NOTE = ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS.  The cache parser AST-reads this
# and rejects computed elements, so nothing here is built by concatenation.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIX_FACE_POSITIVITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_REFINED_ALPHABET_MACROREALIST_LANDSCAPE_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_refined_alphabet_macrorealist_landscape_2026_08_26.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_THREE_DIRECTION_RULE_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    ".claude/science/physics-loops/CAMPAIGN_20260824_GRAVITY_MAINLINE.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, single-line hex literals refreshed by anchored
# sed at landing.  RE-RESOLVED LIVE AT DRAFT TIME against the REMOTE origin/main
# of the real repository -- never against a local main ref, which sits behind it.
CURRENT_MAIN = "66e478505e055faf4a5b9e6f4883211e44304718"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block210-"
              "refined-alphabet-macrorealist-landscape-20260826")
PARENT_COMMIT = "acb58bee45e1383fc1a5f2f6f005f759eddb22e0"
# The Block 209 tip: a real ancestor of HEAD that predates Block 210 and
# therefore carries NEITHER parent artifact.
STALE_PARENT_COMMIT = "07f0613c8730de54cd50403c809f7102bc1534bf"
# A real but superseded authority head, carried forward from Block 210's record.
STALE_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_classification_is_universal",
    "claim_orientation_is_physical",
    "claim_witness_is_observation",
    "claim_continuum_readings_licensed",
    "break_constant_coefficients",
    "break_two_divisions",
    "break_isotropic_variety",
    "break_gauge_classes",
    "break_uniform_survives",
    "break_symbolic_freedom",
    "break_block_formulas",
    "break_orientation_determinants",
    "break_classification_region",
    "break_grid_census",
    "break_witness_w1",
    "break_witness_sign_classes",
    "break_duality_region",
    "break_landed_reconciliation",
    "break_scout_grade_fence",
    "claim_echo_interpreted",
    "claim_signs_invariant",
    "claim_block209_corrected",
    "claim_geometry_selected",
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
    "claim_classification_is_universal": "B",
    "claim_orientation_is_physical": "B",
    "claim_witness_is_observation": "B",
    "claim_continuum_readings_licensed": "B",
    "break_constant_coefficients": "C",
    "break_two_divisions": "C",
    "break_isotropic_variety": "C",
    "break_gauge_classes": "C",
    "break_uniform_survives": "C",
    "break_symbolic_freedom": "D",
    "break_block_formulas": "D",
    "break_orientation_determinants": "D",
    "break_classification_region": "D",
    "break_grid_census": "D",
    "break_witness_w1": "E",
    "break_witness_sign_classes": "E",
    "break_duality_region": "E",
    "break_landed_reconciliation": "E",
    "break_scout_grade_fence": "F",
    "claim_echo_interpreted": "F",
    "claim_signs_invariant": "F",
    "claim_block209_corrected": "F",
    "claim_geometry_selected": "F",
    "break_instance_scope": "F",
    "drop_n5_fence": "G",
    "break_nsimplify_absence": "G",
    "break_float_absence": "G",
}
MUTATED_FAMILIES = "ABCDEFG"


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
    "THE PER-FACE SIX-FACE LITERAL GLUING SYSTEM, WHICH IS THIS BLOCK's FIRST NEW OBJECT: the 96 entry equations that impose on a general symmetric 8 x 8 corner matrix D that every coordinate-face restriction, in Block 209's own sub-corner order [offset, offset + i2, offset + i1, offset + i1 + i2] at order_swap = False and flip = False, equal the LANDED shear_hodge at that FACE's own (volume, shear) -- six INDEPENDENT per-face moduli rather than Block 209's two per-offset pairs, with the builder verified equation for equation against the landed one",
    "THE COMPATIBLE MODULI VARIETY: the common zero locus, on the nonsingular domain (v_f != 0, c_f^2 != 1), of Block 209's SIXTEEN landed forced relations, together with its square variables X_f = c_f^2, its two ties v1 (1 - X0) = v0 and X1 = 1 - v0 v1, its polynomial normal form in (v1, X0) and its rational (t, u) chart c0 = 2t/(1+t^2), c1 = 2u/(1+u^2)",
    "THE CORNER-SIGN GAUGE: the congruence D -> E D E with E = diag(e_0, ..., e_7) and e_i in {-1, +1}, which preserves the literal-gluing form family, symmetry and positive definiteness, acting on the six face shear signs through the factors (e2 e4, e1 e4, e1 e2; e3 e5, e3 e6, e5 e6), together with its orbits on the 64 sign cells and the two orientation invariants pi0 = sign(c_tx0 c_ty0 c_xy0) and pi1 = sign(c_tx1 c_ty1 c_xy1)",
    "THE DEGREE-BLOCK FORMULAS AND THE SIGNED TRIANGLE: deg-0 = [v0], deg-1 = v1 M1 on corners (1, 2, 4), deg-2 = (1/v0) M2 on corners (3, 5, 6) and deg-3 = [1/v1], with M(gamma; signs) = I - gamma S the signed triangle whose characteristic polynomial and determinant are factored exactly in the two orientation classes",
    "THE THREE POSITIVITY WITNESSES W1, W2 AND W3: exact rational 8 x 8 corner matrices at the degree-diagonal representative of their compatible moduli, each with all EIGHT leading principal minors computed exactly, plus the open bounded duality region exhibited at W1",
    "BLOCK 105's LANDED 2D CELL FORM shear_hodge(c, v) = diag(v, v g2(c)^-1, 1/v), READ THROUGH BLOCK 128's OWN IMPORT OF IT AND NOT REBUILT, and BLOCK 209's LANDED CONSTANTS -- its sixteen forced relations, its two uniform numerators, its flat solution, its reciprocal point, its two degree spectra and its two orientation determinants -- READ THROUGH ITS OWN RUNNER AND NOT RETYPED: no line of this block edits either",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
# THE BANNER'S SECOND HALF, AS DECLARED MEASURED CONSTANTS.  ALL TWELVE ARE
# FALSE AND STAY FALSE.  THE FIRST FIVE ARE THE ONES A CLASSIFICATION INVITES.
GRAVITY_SUPPLIED_CLAIMED = False
CLASSIFICATION_IS_UNIVERSAL_CLAIMED = False
ORIENTATION_IS_PHYSICAL_CLAIMED = False
WITNESS_IS_OBSERVATION_CLAIMED = False
GEOMETRY_SELECTION_CLAIMED = False
UNIQUENESS_ABOUT_NATURE_CLAIMED = False
GENERIC_PARAMETER_THEOREM_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
EQUATIONS_OF_MOTION_CLAIMED = False
ECHO_INTERPRETED_CLAIMED = False
SIGNED_FACE_INVARIANCE_CLAIMED = False
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
SCOPED_HEADLINE_WORDS = ("CLASSIFICATION", "ORIENTATION", "WITNESS")
# THE ONE PHRASE THE BLOCK 209 DETERMINANT COINCIDENCE LICENSES, VERBATIM.
LICENSED_ECHO_PHRASE = "noted, never interpreted"
READINGS = (
    "R1: that 'curved positive cells exist' says something about physical curvature.  Measured: nonuniform face moduli of ONE finite 8 x 8 corner-weight matrix admit positive definite solutions.  No metric field, no curvature tensor, no dynamics, no spacetime and no continuum statement follows from any line here.  Reading.",
    "R2: that the classification selects a geometry.  Measured: the exact PD region of ONE gluing principle's compatible variety.  Whether that principle, or the honest metric lift Block 209 built beside it, is the one nature uses is not decided by any line here.  Reading.",
    "R3: that the orientation split is a physical parity or chirality.  Measured: a product of three shear signs inside one declared wedge and sub-corner convention, whose value changes the third leading minor of a 3 x 3 rational matrix.  Reading.",
    "R4: that the exact agreement between these determinants and Block 209's D3 kappa bounds identifies the two constructions.  Measured: two polynomial pairs coincide with the class label negated.  No carrier map, no identification of objects and no commuting statement is proved.  The licensed phrase is 'noted, never interpreted'.  Reading.",
    "R5: that Block 209 was wrong.  Measured: Block 209 scoped its rigidity statement ON THE CHECKED BRANCHES and declined to assert the wider sentence; this block closes the branch it named open, and every Block 209 number is reproduced unchanged.  Reading.",
    "R6: that any of it generalises past this instance.  Measured: one gluing principle, the three coordinate planes at two offsets, one landed 2D target, one 32-point rational grid and three witnesses.  Not every face, not every convention and not every moduli point.  Reading.",
)
CHECK_VERDICT = "INDEPENDENT-CHECK-CARRIED-C1-AND-C2-CONFIRM-C6-QUALIFICATIONS-ADOPTED-AS-CONTENT"

# ---------------------------------------------------------------------------
# THE EXPECTED VALUES, declared as literals so every claim below is auditable
# against the note without reading the code that measures it.
# ---------------------------------------------------------------------------
ZERO_RESIDUAL = 0
CELL_UNKNOWNS = 36
DUALITY_NAMES = ("D07", "D16", "D25", "D34")
HALF = sp.Rational(1, 2)

# --- C: THE VARIETY ----------------------------------------------------------
SIX_FACE_EQUATIONS = 96
GENERIC_RANKS = (32, 33)
BUILDER_MATCHES_LANDED = True
COEFFICIENT_MATRIX_IS_CONSTANT = True
ZERO_COLUMN_COUNT = 4
PINNED_COLUMN_RANK = 32
RELATION_COUNT = 16
RELATIONS_EVEN_IN_EVERY_SHEAR = True
VOLUME_EQUALITY_RELATIONS = (
    "v_tx0 - v_ty0",
    "v_tx0 - v_xy0",
    "v_tx1 - v_ty1",
    "v_tx1 - v_xy1",
)
SQUARE_FACTORIZATION_COUNT = 4
DIVISION_COUNT = 2
DIVISIONS_ARE_BY_VOLUMES = True
TIE_A_FORM = "v1 * (1 - g0^2) = v0"
TIE_B_FORM = "g1^2 = 1 - v0 * v1"
DERIVED_IDENTITY_FORM = "v0^2 = (1 - g0^2) * (1 - g1^2)"
TIE_COUNT = 2
NORMAL_FORM_KILLS_ALL = True
NON_ISOTROPIC_BRANCHES = 0
VARIETY_IS_PER_OFFSET_ISOTROPIC = True
SIGN_CELLS = 64
SIGN_CELLS_SOLVABLE = 64
OFF_VARIETY_RANKS = (32, 33)
MIRROR_IS_SOLVABLE = True
MIRROR_DIES_AT_FIRST_MINOR = True
GAUGE_FACTOR_PATTERNS = 16
GAUGE_CLASSES = 4
GAUGE_ORBIT_SIZE = 16
GAUGE_INVARIANTS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
ZARISKI_COMPONENTS = 16
QUADRIC_IS_IRREDUCIBLE = True
UNIFORM_NUMERATORS = ("c**2 + v**2 - 1", "c**2*v")
UNIFORM_SOLUTION = (0, 1)
UNIFORM_STILL_FLAT_ONLY = True

# --- D: THE BLOCKS AND THE CLASSIFICATION ------------------------------------
SYMBOLIC_CLASSES = 4
SYMBOLIC_RANKS = (32, 32)
FREE_PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
FREE_PARAMETER_COUNT = 4
BLOCKS_PARAMETER_FREE_IN_EVERY_CLASS = True
CROSS_DEGREE_ZERO_OFF_DUALITY = True
DEGREE_BLOCK_FORMS = (
    "deg-0 = [v0]",
    "deg-1 = v1 * M1 on corners (1, 2, 4), M1 = [[1, -c_xy0, -c_ty0], [-c_xy0, 1, -c_tx0], [-c_ty0, -c_tx0, 1]]",
    "deg-2 = (1/v0) * M2 on corners (3, 5, 6), M2 = [[1, -c_tx1, -c_ty1], [-c_tx1, 1, -c_xy1], [-c_ty1, -c_xy1, 1]]",
    "deg-3 = [1/v1]",
)
BLOCK_FORMULAS_EXACT = True
CORNERS_ZERO_AND_SEVEN_DECOUPLE = True
GAUGE_CONGRUENCE_EXACT = True
EIGENVALUES_AT_POSITIVE_PRODUCT = "(1 - 2*g, 1 + g, 1 + g)"
EIGENVALUES_AT_NEGATIVE_PRODUCT = "(1 + 2*g, 1 - g, 1 - g)"
DETERMINANT_AT_POSITIVE_PRODUCT = "(1 + g)^2 * (1 - 2*g)"
DETERMINANT_AT_NEGATIVE_PRODUCT = "(1 - g)^2 * (1 + 2*g)"
SECOND_LEADING_MINOR_FORM = "1 - g^2"
ECHO_IS_CLASS_NEGATED = True
MAGNITUDE_BOUND_AT_POSITIVE_PRODUCT = HALF
MAGNITUDE_BOUND_AT_NEGATIVE_PRODUCT = sp.Integer(1)
CLASSIFICATION_IS_PER_OFFSET_INDEPENDENT = True
CURVED_PD_FAMILY_IN_EVERY_CLASS = True
CURVED_PD_FAMILY_DIMENSION = 2
GRID_POINTS = 32
GRID_POINTS_PER_CLASS = 8
GRID_PD_TOTAL = 17
GRID_CENSUS = (((1, 1), 3), ((1, -1), 3), ((-1, 1), 3), ((-1, -1), 8))
GRID_MATCHES_REGION_FORMULA = True
KILLER_IS_A_DEGREE_BLOCK_DETERMINANT = True

# --- E: THE WITNESSES AND THE LANDED-POINT RECONCILIATION --------------------
W1_MODULI = (sp.Rational(15, 16), sp.Rational(1, 4), sp.Integer(1),
             sp.Rational(1, 4))
W1_MINORS = (sp.Rational(15, 16), sp.Rational(15, 16), sp.Rational(225, 256),
             sp.Rational(15, 16), sp.Rational(25, 32), sp.Rational(25, 32),
             sp.Rational(25, 36), sp.Rational(25, 36))
W1_IS_POSITIVE_DEFINITE = True
W1_IS_NONUNIFORM = True
FLAT_ONLY_OVER_NONUNIFORM_CLAIMED = False
W2_MODULI = (sp.Rational(7, 16), sp.Rational(3, 4), sp.Integer(1),
             sp.Rational(3, 4))
W2_MINORS = (sp.Rational(7, 16), sp.Rational(7, 16), sp.Rational(49, 256),
             sp.Rational(7, 16), sp.Rational(5, 32), sp.Rational(5, 32),
             sp.Rational(25, 196), sp.Rational(25, 196))
W3_MODULI = (sp.Rational(12, 25), sp.Rational(3, 5), sp.Rational(3, 4),
             sp.Rational(4, 5))
W3_MINORS = (sp.Rational(12, 25), sp.Rational(9, 25), sp.Rational(108, 625),
             sp.Rational(9, 25), sp.Rational(297, 2000),
             sp.Rational(891, 8000), sp.Rational(429, 6400),
             sp.Rational(143, 1600))
W2_IS_POSITIVE_DEFINITE = True
W3_IS_POSITIVE_DEFINITE = True
W3_FLIPS_PER_OFFSET = (1, 1)
W3_MAGNITUDES_ARE_THE_LANDED_ONES = True
KILLER_WAS_THE_SIGN_PATTERN = True
DUALITY_REGION_IS_OPEN = True
DUALITY_REGION_IS_BOUNDED = True
DUALITY_INTERIOR_CHOICE = (HALF, sp.Rational(1, 5), -sp.Rational(1, 5),
                           sp.Rational(1, 5))
DUALITY_PAIR_MINOR_FORMS = (
    sp.cancel(W1_MODULI[0] / W1_MODULI[2] - sp.Symbol("D07") ** 2),
    sp.cancel(W1_MODULI[2] / W1_MODULI[0] - sp.Symbol("D16") ** 2),
    sp.cancel(W1_MODULI[2] / W1_MODULI[0] - sp.Symbol("D25") ** 2),
    sp.cancel(W1_MODULI[2] / W1_MODULI[0] - sp.Symbol("D34") ** 2),
)
DUALITY_BOUND_FORM = (
    "D07^2 < v0/v1 and D16^2,D25^2,D34^2 < v1/v0, from four "
    "two-by-two principal minors"
)
LANDED_RECIPROCAL_RANKS = (32, 32)
LANDED_RECIPROCAL_STILL_INDEFINITE = True
LANDED_KILLING_MINORS = (-sp.Rational(27, 125), -sp.Rational(1125, 64))
FLAT_POINT_IS_IDENTITY = True

# --- F: THE SIX SCOPE FENCES -------------------------------------------------
SCOUT_GRADE_ONLY = True
FINITE_EXACT_LINEAR_ALGEBRA = True
PHYSICAL_CONTENT_CLAIMED = False
ECHO_NOTED_ONLY = True
STRUCTURAL_IDENTIFICATION_CLAIMED = False
SIGN_PRODUCTS_ARE_THE_INVARIANT = True
CONVENTION_TIED_OBJECTS = (
    "the sign of every INDIVIDUAL face shear c_f, which the corner-sign gauge D -> E D E conjugates within a class without moving any invariant",
    "the sub-corner order [offset, offset + i2, offset + i1, offset + i1 + i2] and the plane orientation, which fix which off-diagonal entry of D carries which face's shear",
    "the sign convention g_ij = +c_ij, under which the degree blocks display MINUS the shear pattern, so an entrywise negation flips the triangle product and with it the class label",
)
BLOCK209_COMPLETED_NOT_CORRECTED = True
BLOCK209_SCOPING_WAS_EXACT = True
BLOCK209_CORRECTION_CLAIMED = False
LANDED_NUMBERS_CORRECTED = 0
CLASSIFICATION_IS_OF_ONE_PRINCIPLE = True
CLASSIFIES_EVERY_POSITIVE_MATRIX_CLAIMED = False
INSTANCE_SCOPE = (
    "one gluing principle -- the literal six-face system against one landed 2D target -- and no other",
    "the three coordinate planes at two offsets each, and NO oblique face",
    "one landed 2D target, shear_hodge(c, v), read through Block 128's import of Block 105",
    "one 32-point rational grid and three exhibited witnesses, not a parameter space and not a limit",
    "the nonsingular domain (v_f != 0, c_f^2 != 1) and the positive-volume branch, with the negative-volume mirror measured and excluded at its first minor",
    "the shape-rule versus honest-metric selection principle REMAINS OPEN, exactly as Block 209 left it",
)
INSTANCE_SCOPE_COUNT = 6
OBLIQUE_FACES_REMAIN_OPEN = True
SELECTION_PRINCIPLE_REMAINS_OPEN = True
SCOPE_GENERALISATION_CLAIMED = False

# THE ONE-FAMILY CONTRACT IS ENFORCED BY DISJOINT CLAIM KEYS AND NOT ONLY BY THE
# ASSERTION IN main().  Every claim key below is read by EXACTLY ONE gate.  The
# F fences therefore carry their own constants -- SCOUT_GRADE_ONLY,
# ECHO_NOTED_ONLY, SIGN_PRODUCTS_ARE_THE_INVARIANT,
# BLOCK209_COMPLETED_NOT_CORRECTED, CLASSIFICATION_IS_OF_ONE_PRINCIPLE and the
# rest -- rather than re-reading the B, C, D and E keys that state the same
# thing from the other side.  Where an F gate depends on a fact measured
# elsewhere, the gate NAMES the family that measures it in its statement and
# does not consume that family's claim, so neither leans on the other and no
# mutation can flip two families at once.

SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
# THE nsimplify HAZARD, INHERITED FROM BLOCK 186 THROUGH BLOCK 209 AND HONOURED
# HERE BY ABSENCE.  That call carries a rational TOLERANCE and maps a small
# nonzero rational to EXACTLY ZERO.  This block's entire headline is a set of
# exact SIGN statements about leading principal minors as small as 143/1600 and
# about determinants as small as -27/125: a single tolerance-carrying call could
# turn a positive witness minor into a zero and destroy the refutation, or turn
# the landed killing minor into a zero and manufacture a positivity Block 209
# proved impossible.  Gate G counts the occurrences in this file's own source
# and requires ZERO, requires ZERO float literals by an AST scan of the same
# source, and requires ZERO float CALL SITES, because every number this block
# reports is a short exact rational and NOTHING here is ever converted to a
# decimal.
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many times this runner calls that function."""
    try:
        return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)
    except OSError:                                    # pragma: no cover
        return -1


def float_literal_occurrences() -> int:
    """MEASURED, NOT PROMISED: how many float literals this runner's own source
    contains, by an AST walk rather than by a text search."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    """THE SECOND HALF OF THE SAME HYGIENE, IN BLOCK 209's STRICT FORM.  Every
    number in this block is a short exact rational -- ranks, counts, magnitudes
    like 3/5, minors like 891/8000 -- so no decimal is ever needed and gate G-3
    requires EXACTLY ZERO float call sites.  Nothing in this file can consume
    anything but an exact rational, by measurement rather than by promise."""
    try:
        tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    except (OSError, SyntaxError):                     # pragma: no cover
        return -1
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


# ---------------------------------------------------------------------------
# THE SYSTEM, BUILT ONCE FROM THE LANDED CONVENTIONS
# ---------------------------------------------------------------------------
CORNERS = b209.CORNERS if b209 is not None else ()
CELL = b209.CELL if b209 is not None else sp.zeros(8, 8)
CELL_SYMBOLS = b209.CELL_SYMBOLS if b209 is not None else ()
DEGREE_INDICES = b209.DEGREE_INDICES if b209 is not None else ()
PLANE_FRAMES = b209.PLANE_FRAMES if b209 is not None else ()
FACE_KEYS = tuple((name, offset) for _, _, _, name in PLANE_FRAMES
                  for offset in (0, 1))
# THE GAUGE READS THE FACES IN OFFSET-MAJOR ORDER, because the two orientation
# invariants are the two per-offset TRIPLE products and nothing else.
GAUGE_FACE_ORDER = (("tx", 0), ("ty", 0), ("xy", 0),
                    ("tx", 1), ("ty", 1), ("xy", 1))


def face_system(face_moduli: dict) -> tuple:
    """THE SIX-FACE LITERAL SYSTEM AT INDEPENDENT PER-FACE MODULI.  Every
    equation says one entry of the general symmetric corner matrix equals the
    corresponding entry of the LANDED shear_hodge at that FACE's own (volume,
    shear).  Block 209's builder ties the three faces of an offset to one
    modulus pair whenever it is handed values; this one does not, which is
    exactly the freedom the classification needs.  The sub-corner order, the
    plane frames and the target are Block 209's own, and C-1 measures that the
    two builders agree equation for equation at generic symbols."""
    equations = []
    for first, second, normal, name in PLANE_FRAMES:
        for offset_index in (0, 1):
            offset = tuple(offset_index * k for k in normal)
            volume, shear = face_moduli[(name, offset_index)]
            landed = sp.Matrix(LANDED_SHEAR_HODGE(shear, volume))

            def add(left: tuple, right: tuple) -> tuple:
                return tuple((left[k] + right[k]) % 2 for k in range(3))

            indices = [CORNERS.index(offset),
                       CORNERS.index(add(offset, second)),
                       CORNERS.index(add(offset, first)),
                       CORNERS.index(add(offset, add(first, second)))]
            for row in range(4):
                for column in range(4):
                    equations.append(sp.expand(
                        CELL[indices[row], indices[column]]
                        - landed[row, column]))
    matrix, rhs = sp.linear_eq_to_matrix(equations, CELL_SYMBOLS)
    return equations, matrix, rhs


def solve_pinned(matrix, rhs, at_zero: bool = True) -> tuple:
    """linsolve, returning (D, free duality symbols).  With at_zero the four
    duality parameters are set to zero -- the DEGREE-DIAGONAL REPRESENTATIVE,
    at which D is the direct sum of its four degree blocks and the sufficiency
    half of the classification is exhibited."""
    solution = list(sp.linsolve((matrix, rhs), CELL_SYMBOLS))[0]
    free = sorted({symbol for entry in solution
                   for symbol in entry.free_symbols
                   if str(symbol).startswith("D")}, key=str)
    zero = {symbol: sp.Integer(0) for symbol in free} if at_zero else {}
    solved = sp.Matrix(8, 8, lambda i, j: sp.cancel(solution[
        CELL_SYMBOLS.index(CELL[min(i, j), max(i, j)])].subs(zero)))
    return solved, free


def leading_minors(matrix) -> tuple:
    return tuple(matrix[:k, :k].det() for k in range(1, matrix.rows + 1))


def degree_block(matrix, degree: int):
    indices = DEGREE_INDICES[degree]
    return sp.Matrix(len(indices), len(indices),
                     lambda i, j: matrix[indices[i], indices[j]])


def branch_moduli(volume0, gamma0, volume1, gamma1, signs) -> dict:
    moduli = {}
    for name, offset in FACE_KEYS:
        volume = volume0 if offset == 0 else volume1
        gamma = gamma0 if offset == 0 else gamma1
        moduli[(name, offset)] = (volume, signs[(name, offset)] * gamma)
    return moduli


def diagonal_point(gamma) -> tuple:
    """The equal-magnitude chart: gamma0 = gamma1 = gamma forces
    v0 = 1 - gamma^2 and v1 = 1 by the two ties -- rational for every rational
    gamma, so the whole grid stays exact."""
    return (1 - gamma ** 2, gamma, sp.Integer(1), gamma)


ALL_PLUS = {key: sp.Integer(1) for key in FACE_KEYS}


def flipped(*keys) -> dict:
    signs = dict(ALL_PLUS)
    for key in keys:
        signs[key] = sp.Integer(-1)
    return signs


REPRESENTATIVES = {
    (1, 1): ALL_PLUS,
    (1, -1): flipped(("xy", 1)),
    (-1, 1): flipped(("xy", 0)),
    (-1, -1): flipped(("xy", 0), ("xy", 1)),
}


def signed_triangle(shears) -> sp.Matrix:
    """M(gamma; signs) = I - gamma S, the signed triangle the degree blocks
    are built from.  The three off-diagonal entries carry MINUS the three face
    shears, which is why the class label of the determinant pair is negated
    against Block 209's honest-lift split."""
    first, second, third = shears
    return sp.Matrix([[1, -first, -second],
                      [-first, 1, -third],
                      [-second, -third, 1]])


def region_predicate(gamma, orientation) -> bool:
    """THE CLASSIFIED CONDITION FOR ONE OFFSET.  On the positive-orientation
    side the magnitude must stay strictly below one half; on the negative side
    anything strictly below one works.  At gamma = 0 there is no orientation
    and both conditions agree."""
    if gamma == 0:
        return True
    return bool(gamma < HALF) if orientation > 0 else bool(gamma < 1)


# ---------------------------------------------------------------------------
# THE MEASURED FACTS
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class VarietyFacts:
    equations: int
    builder_matches_landed: bool
    generic_ranks: tuple
    coefficient_is_constant: bool
    zero_columns: tuple
    pinned_rank: int
    relations: tuple
    relations_match_landed: bool
    relations_even: bool
    volume_equalities_literal: bool
    square_factorizations: int
    divisions: tuple
    ties: tuple
    tie_count: int
    normal_form_kills_all: bool
    derived_identity: bool
    non_isotropic_branches: int
    sign_cells: int
    sign_cells_solvable: int
    off_variety_ranks: tuple
    mirror_ranks: tuple
    mirror_first_minor: object
    gauge_factor_patterns: int
    gauge_orbits: int
    gauge_orbit_sizes: tuple
    gauge_invariants: tuple
    ratio_classes: int
    quadric_irreducible: bool
    uniform_numerators: tuple
    uniform_solutions: tuple


@dataclass(frozen=True)
class BlockFacts:
    classes: tuple
    class_ranks: tuple
    class_free_names: tuple
    blocks_parameter_free: tuple
    cross_degree_zero: tuple
    block_formulas_exact: bool
    corners_decouple: bool
    gauge_congruence_exact: bool
    charpoly_positive: bool
    charpoly_negative: bool
    determinant_positive: object
    determinant_negative: object
    second_minor: object
    echo_class_negated: bool
    magnitude_parameters: int
    grid_points: int
    grid_pd_total: int
    grid_census: tuple
    grid_matches_formula: bool
    killer_is_block_determinant: bool


@dataclass(frozen=True)
class WitnessFacts:
    w1_minors: tuple
    w1_compatible: bool
    w1_nonuniform: bool
    w2_minors: tuple
    w3_minors: tuple
    w3_magnitudes: tuple
    w3_flip_count: tuple
    duality_interior_minors: tuple
    duality_a_bad_minors: tuple
    duality_b_bad_minors: tuple
    duality_pair_minors: tuple
    landed_ranks: tuple
    landed_free_names: tuple
    landed_degree_one_spectrum: tuple
    landed_degree_two_spectrum: tuple
    landed_negative_blocks: tuple
    landed_killing_minors: tuple
    landed_killing_matches_formula: bool
    flat_point_is_identity: bool


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
    scoped_words: int
    variety: VarietyFacts
    blocks: BlockFacts
    witnesses: WitnessFacts
    scope: dict
    nsimplify_calls: int
    float_literals: int
    float_calls: int


def measure_variety() -> VarietyFacts:
    """FAMILY C, MEASURED ONCE.  The system's fidelity to the landed builder,
    the structure of its coefficient matrix, the exact decomposition of the
    sixteen landed relations into two ties, the converse normal form, the sign
    cells with their corner-sign gauge, and the uniform locus re-derived from
    the ties rather than re-solved from the system."""
    generic = {}
    for _, _, _, name in PLANE_FRAMES:
        for offset in (0, 1):
            generic[(name, offset)] = (
                sp.Symbol(f"v_{name}{offset}", positive=True),
                sp.Symbol(f"c_{name}{offset}"))
    equations, matrix, rhs = face_system(generic)
    landed_equations, landed_matrix, landed_rhs, landed_symbols = \
        b209.literal_system((0, 1), False, False)
    builder_matches = bool(
        len(equations) == len(landed_equations) == SIX_FACE_EQUATIONS
        and all(sp.expand(a - b) == 0
                for a, b in zip(equations, landed_equations)))
    ranks = (matrix.rank(), matrix.row_join(rhs).rank())
    coefficient_constant = not matrix.free_symbols
    zero_columns = tuple(
        str(CELL_SYMBOLS[j]) for j in range(matrix.cols)
        if all(matrix[i, j] == 0 for i in range(matrix.rows)))
    pinned = [j for j in range(matrix.cols)
              if str(CELL_SYMBOLS[j]) not in DUALITY_NAMES]
    pinned_rank = matrix[:, pinned].rank()

    measured = b209.relation_set(landed_matrix, landed_rhs, landed_symbols)
    relations_match = tuple(sorted(measured)) == tuple(
        sorted(b209.SIX_FACE_RELATIONS))

    table = {str(symbol): symbol for symbol in landed_symbols}
    expressions = [sp.sympify(text, locals=table)
                   for text in b209.SIX_FACE_RELATIONS]
    shear_symbols = [table[f"c_{name}{offset}"] for name, offset in FACE_KEYS]
    even = True
    for relation in expressions:
        for shear in shear_symbols:
            polynomial = sp.Poly(relation, shear)
            if polynomial.degree() > 2 or any(
                    monomial[0] % 2 for monomial in polynomial.monoms()):
                even = False

    by_text = dict(zip(b209.SIX_FACE_RELATIONS, expressions))
    volume_literal = all(text in by_text for text in VOLUME_EQUALITY_RELATIONS)

    volume_zero, volume_one = sp.symbols("V0 V1", positive=True)
    squares = {(name, offset): sp.Symbol(f"X_{name}{offset}", nonnegative=True)
               for name, offset in FACE_KEYS}
    volume_subs = {table[f"v_{name}{offset}"]:
                   (volume_zero if offset == 0 else volume_one)
                   for name, offset in FACE_KEYS}
    square_subs = {table[f"c_{name}{offset}"] ** 2: squares[(name, offset)]
                   for name, offset in FACE_KEYS}

    def squared_form(expression):
        return sp.expand(sp.expand(expression).subs(square_subs))

    factorizations = (
        ("c_tx0**2*v_ty0 - c_ty0**2*v_tx0 + v_tx0 - v_ty0",
         volume_zero * (squares[("tx", 0)] - squares[("ty", 0)])),
        ("c_tx0**2*v_xy0 - c_xy0**2*v_tx0 + v_tx0 - v_xy0",
         volume_zero * (squares[("tx", 0)] - squares[("xy", 0)])),
        ("c_tx1**2*v_ty1 - c_ty1**2*v_tx1 + v_tx1 - v_ty1",
         volume_one * (squares[("tx", 1)] - squares[("ty", 1)])),
        ("c_tx1**2*v_xy1 - c_xy1**2*v_tx1 + v_tx1 - v_xy1",
         volume_one * (squares[("tx", 1)] - squares[("xy", 1)])),
    )
    factorization_count = sum(
        1 for text, target in factorizations
        if sp.expand(squared_form(by_text[text].subs(volume_subs)) - target)
        == 0)

    square_zero = sp.Symbol("X0", nonnegative=True)
    square_one = sp.Symbol("X1", nonnegative=True)
    common = {squares[key]: (square_zero if key[1] == 0 else square_one)
              for key in FACE_KEYS}
    tie_a = volume_one * (1 - square_zero) - volume_zero
    tie_b = square_one + volume_zero * volume_one - 1
    tie_a_texts = ("c_tx0**2*v_ty1 + v_tx0 - v_ty1",
                   "c_tx0**2*v_xy1 + v_tx0 - v_xy1",
                   "c_ty0**2*v_tx1 - v_tx1 + v_ty0",
                   "c_xy0**2*v_tx1 - v_tx1 + v_xy0")
    tie_b_texts = ("c_tx1**2 + v_tx1*v_ty0 - 1",
                   "c_tx1**2 + v_tx1*v_xy0 - 1",
                   "c_ty1**2 + v_tx0*v_ty1 - 1",
                   "c_xy1**2 + v_tx0*v_xy1 - 1")

    def reduce_text(text):
        return sp.expand(squared_form(by_text[text].subs(volume_subs))
                         .subs(common))

    ties_ok = (
        all(sp.expand(reduce_text(text) - tie_a) == 0
            or sp.expand(reduce_text(text) + tie_a) == 0
            for text in tie_a_texts)
        and all(sp.expand(reduce_text(text) - tie_b) == 0
                or sp.expand(reduce_text(text) + tie_b) == 0
                for text in tie_b_texts))

    normal_form = {}
    for name, offset in FACE_KEYS:
        normal_form[table[f"v_{name}{offset}"]] = (
            volume_one * (1 - square_zero) if offset == 0 else volume_one)
        normal_form[squares[(name, offset)]] = (
            square_zero if offset == 0
            else 1 - volume_one ** 2 * (1 - square_zero))
    normal_form_kills = all(
        sp.expand(squared_form(relation).subs(normal_form)) == 0
        for relation in expressions)
    derived_identity = bool(
        sp.expand(((volume_one * (1 - square_zero)) ** 2
                   - (1 - square_zero) * (1 - square_one))
                  .subs(square_one,
                        1 - volume_one ** 2 * (1 - square_zero))) == 0
        and sp.cancel((volume_one ** 2
                       - (1 - square_one) / (1 - square_zero))
                      .subs(square_one,
                            1 - volume_one ** 2 * (1 - square_zero))) == 0)

    reciprocal = (sp.Rational(12, 25), sp.Rational(3, 5),
                  sp.Rational(3, 4), sp.Rational(4, 5))
    solvable = 0
    for pattern in itertools.product((1, -1), repeat=6):
        signs = {key: sp.Integer(pattern[k])
                 for k, key in enumerate(FACE_KEYS)}
        _, cell_matrix, cell_rhs = face_system(branch_moduli(
            reciprocal[0], reciprocal[1], reciprocal[2], reciprocal[3], signs))
        if (cell_matrix.rank(),
                cell_matrix.row_join(cell_rhs).rank()) == (32, 32):
            solvable += 1

    _, off_matrix, off_rhs = face_system(branch_moduli(
        sp.Rational(15, 16), sp.Rational(1, 4), HALF, sp.Rational(1, 4),
        ALL_PLUS))
    off_ranks = (off_matrix.rank(), off_matrix.row_join(off_rhs).rank())

    _, mirror_matrix, mirror_rhs = face_system(branch_moduli(
        -sp.Rational(15, 16), sp.Rational(1, 4), sp.Integer(-1),
        sp.Rational(1, 4), ALL_PLUS))
    mirror_ranks = (mirror_matrix.rank(),
                    mirror_matrix.row_join(mirror_rhs).rank())
    mirror_solved, _ = solve_pinned(mirror_matrix, mirror_rhs)

    factor_patterns = set()
    for corner_signs in itertools.product((1, -1), repeat=8):
        e = corner_signs
        factor_patterns.add((e[2] * e[4], e[1] * e[4], e[1] * e[2],
                             e[3] * e[5], e[3] * e[6], e[5] * e[6]))
    orbits = {}
    for pattern in itertools.product((1, -1), repeat=6):
        orbit = frozenset(
            tuple(pattern[k] * factors[k] for k in range(6))
            for factors in factor_patterns)
        orbits.setdefault(orbit, []).append(pattern)
    orbit_sizes, invariants = [], set()
    for members in orbits.values():
        orbit_sizes.append(len(members))
        for member in members:
            invariants.add((member[0] * member[1] * member[2],
                            member[3] * member[4] * member[5]))
    ratio_classes = len({
        (pattern[0] * pattern[1], pattern[0] * pattern[2],
         pattern[3] * pattern[4], pattern[3] * pattern[5])
        for pattern in itertools.product((1, -1), repeat=6)})
    quadric = volume_one ** 2 * (1 - sp.Symbol("c0") ** 2) \
        - (1 - sp.Symbol("c1") ** 2)
    quadric_irreducible = len(sp.factor_list(quadric)[1]) == 1

    uniform_shear = sp.Symbol("c", real=True)
    uniform_volume = sp.Symbol("v", positive=True)
    uniform_a = sp.expand(tie_a.subs({volume_zero: uniform_volume,
                                      volume_one: uniform_volume,
                                      square_zero: uniform_shear ** 2}))
    uniform_b = sp.expand(tie_b.subs({volume_zero: uniform_volume,
                                      volume_one: uniform_volume,
                                      square_one: uniform_shear ** 2}))
    uniform_numerators = tuple(sorted(
        b209.canonical_relation(expression, (uniform_shear, uniform_volume))
        for expression in (uniform_a, uniform_b)))
    solutions = sp.solve([uniform_a, uniform_b],
                         [uniform_shear, uniform_volume], dict=True)
    uniform_solutions = tuple(sorted(
        ((candidate[uniform_shear], candidate[uniform_volume])
         for candidate in solutions
         if uniform_shear in candidate and uniform_volume in candidate
         and candidate[uniform_shear] >= 0 and candidate[uniform_volume] > 0),
        key=str))

    return VarietyFacts(
        len(equations), builder_matches, ranks, coefficient_constant,
        zero_columns, pinned_rank, tuple(sorted(measured)), relations_match,
        even, volume_literal, factorization_count,
        ("the two per-offset volumes v0 and v1, and nothing else",),
        (str(sp.Eq(tie_a, 0)), str(sp.Eq(tie_b, 0))),
        2 if ties_ok else 0, normal_form_kills, derived_identity,
        0 if normal_form_kills else 1,
        64, solvable, off_ranks, mirror_ranks, mirror_solved[0, 0],
        len(factor_patterns), len(orbits), tuple(sorted(orbit_sizes)),
        tuple(sorted(invariants)), ratio_classes, quadric_irreducible,
        uniform_numerators, uniform_solutions)


CHART_T, CHART_U = sp.symbols("t u")
CHART_SHEAR_ZERO = 2 * CHART_T / (1 + CHART_T ** 2)
CHART_SHEAR_ONE = 2 * CHART_U / (1 + CHART_U ** 2)
CHART_VOLUME_ZERO = ((1 - CHART_T ** 2) * (1 - CHART_U ** 2)
                     / ((1 + CHART_T ** 2) * (1 + CHART_U ** 2)))
CHART_VOLUME_ONE = ((1 + CHART_T ** 2) * (1 - CHART_U ** 2)
                    / ((1 - CHART_T ** 2) * (1 + CHART_U ** 2)))
DIAGONAL_MAGNITUDES = (sp.Integer(0), sp.Rational(1, 4), sp.Rational(2, 5),
                       HALF, sp.Rational(3, 5), sp.Rational(3, 4))
OFF_DIAGONAL_POINTS = (
    (sp.Rational(12, 25), sp.Rational(3, 5), sp.Rational(3, 4),
     sp.Rational(4, 5)),
    (sp.Rational(12, 25), sp.Rational(4, 5), sp.Rational(4, 3),
     sp.Rational(3, 5)),
)


def chart_moduli(signs: dict) -> dict:
    moduli = {}
    for name, offset in FACE_KEYS:
        volume = CHART_VOLUME_ZERO if offset == 0 else CHART_VOLUME_ONE
        shear = (CHART_SHEAR_ZERO if offset == 0 else CHART_SHEAR_ONE) \
            * signs[(name, offset)]
        moduli[(name, offset)] = (volume, shear)
    return moduli


def measure_blocks() -> BlockFacts:
    """FAMILY D, MEASURED ONCE, OVER THE RATIONAL FUNCTION FIELD IN THE CHART
    PARAMETERS.  One symbolic solve per gauge class; the four degree blocks
    read off as exact functions of the branch parameters; the signed triangle's
    characteristic polynomial and determinant factored in the two orientation
    classes; and the classification confirmed pointwise on a rational grid."""
    duality_symbols = set(sp.symbols(" ".join(DUALITY_NAMES)))
    classes, class_ranks, class_free = [], [], []
    parameter_free, cross_zero = [], []
    solutions = {}
    for orientation, signs in REPRESENTATIVES.items():
        _, matrix, rhs = face_system(chart_moduli(signs))
        ranks = (matrix.rank(), matrix.row_join(rhs).rank())
        solved, free = solve_pinned(matrix, rhs, at_zero=False)
        blocks = [degree_block(solved, degree) for degree in range(4)]
        content = set()
        for block in blocks:
            for i in range(block.rows):
                for j in range(block.cols):
                    content |= block[i, j].free_symbols
        classes.append(orientation)
        class_ranks.append(ranks)
        class_free.append(tuple(str(symbol) for symbol in free))
        parameter_free.append(not (content & duality_symbols))
        cross_zero.append(all(
            solved[i, j] == 0 for i in range(8) for j in range(8)
            if sum(CORNERS[i]) != sum(CORNERS[j])
            and f"D{min(i, j)}{max(i, j)}" not in DUALITY_NAMES))
        solutions[orientation] = (solved, blocks)

    formulas_exact, decouple = True, True
    for orientation, signs in REPRESENTATIVES.items():
        solved, blocks = solutions[orientation]
        first = CHART_VOLUME_ONE * signed_triangle((
            signs[("xy", 0)] * CHART_SHEAR_ZERO,
            signs[("ty", 0)] * CHART_SHEAR_ZERO,
            signs[("tx", 0)] * CHART_SHEAR_ZERO))
        second = signed_triangle((
            signs[("tx", 1)] * CHART_SHEAR_ONE,
            signs[("ty", 1)] * CHART_SHEAR_ONE,
            signs[("xy", 1)] * CHART_SHEAR_ONE)) / CHART_VOLUME_ZERO
        if sp.simplify(blocks[0] - sp.Matrix([[CHART_VOLUME_ZERO]])) \
                != sp.zeros(1, 1):
            formulas_exact = False
        if sp.simplify(blocks[1] - first) != sp.zeros(3, 3):
            formulas_exact = False
        if sp.simplify(blocks[2] - second) != sp.zeros(3, 3):
            formulas_exact = False
        if sp.simplify(blocks[3] - sp.Matrix([[1 / CHART_VOLUME_ONE]])) \
                != sp.zeros(1, 1):
            formulas_exact = False
        if any(solved[0, k] != 0 or solved[7, k] != 0 for k in range(1, 7)):
            decouple = False

    # THE GAUGE CONGRUENCE, VERIFIED IN THE FIELD AND NOT ON A SAMPLE.
    corner_signs = (1, -1, 1, 1, 1, 1, 1, 1)
    congruence = sp.diag(*[sp.Integer(sign) for sign in corner_signs])
    factor_map = {("tx", 0): corner_signs[2] * corner_signs[4],
                  ("ty", 0): corner_signs[1] * corner_signs[4],
                  ("xy", 0): corner_signs[1] * corner_signs[2],
                  ("tx", 1): corner_signs[3] * corner_signs[5],
                  ("ty", 1): corner_signs[3] * corner_signs[6],
                  ("xy", 1): corner_signs[5] * corner_signs[6]}
    flip_signs = {key: sp.Integer(factor_map[key]) for key in FACE_KEYS}
    _, flip_matrix, flip_rhs = face_system(chart_moduli(flip_signs))
    flipped_solution, _ = solve_pinned(flip_matrix, flip_rhs)
    all_plus = sp.Matrix(8, 8, lambda i, j: solutions[(1, 1)][0][i, j].subs(
        {symbol: sp.Integer(0) for symbol in duality_symbols}))
    gauge_exact = sp.simplify(
        congruence * all_plus * congruence - flipped_solution) \
        == sp.zeros(8, 8)

    magnitude = sp.Symbol("gamma", nonnegative=True)
    eigenvalue = sp.Symbol("lam")
    plus = signed_triangle((magnitude, magnitude, magnitude))
    minus = signed_triangle((magnitude, magnitude, -magnitude))
    charpoly_plus = sp.expand(
        plus.charpoly(eigenvalue).as_expr()
        - (eigenvalue - (1 - 2 * magnitude))
        * (eigenvalue - (1 + magnitude)) ** 2) == 0
    charpoly_minus = sp.expand(
        minus.charpoly(eigenvalue).as_expr()
        - (eigenvalue - (1 + 2 * magnitude))
        * (eigenvalue - (1 - magnitude)) ** 2) == 0
    determinant_plus = sp.factor(sp.expand(plus.det()))
    determinant_minus = sp.factor(sp.expand(minus.det()))
    second_minor = sp.expand(plus[:2, :2].det())
    # THE ECHO, MEASURED AGAINST BLOCK 209's OWN LITERALS AND NOT RETYPED.  The
    # class label is NEGATED: the pi = +1 triangle carries Block 209's NEGATIVE
    # orientation polynomial and the pi = -1 triangle its POSITIVE one.  That
    # is measured here and interpreted nowhere -- gate F-2.
    kappa = sp.Symbol("kappa")
    landed_negative = sp.sympify(
        b209.DETERMINANT_AT_NEGATIVE_ORIENTATION.replace("^", "**"),
        locals={"kappa": kappa})
    landed_positive = sp.sympify(
        b209.DETERMINANT_AT_POSITIVE_ORIENTATION.replace("^", "**"),
        locals={"kappa": kappa})
    echo = bool(
        sp.expand(sp.expand(plus.det()).subs(magnitude, kappa)
                  - landed_negative) == 0
        and sp.expand(sp.expand(minus.det()).subs(magnitude, kappa)
                      - landed_positive) == 0)

    # THE MAGNITUDE BASE IS TWO-DIMENSIONAL, MEASURED AND NOT ASSERTED: the
    # ties leave exactly the chart's two free parameters once the volumes are
    # solved for, so a nonempty PD region in a class is a TWO-parameter family.
    magnitude_parameters = len(
        CHART_SHEAR_ZERO.free_symbols | CHART_SHEAR_ONE.free_symbols
        | CHART_VOLUME_ZERO.free_symbols | CHART_VOLUME_ONE.free_symbols)

    grid_total, census, matches, killer = 0, [], True, True
    points = [diagonal_point(value) for value in DIAGONAL_MAGNITUDES] \
        + list(OFF_DIAGONAL_POINTS)
    for orientation, signs in REPRESENTATIVES.items():
        class_total = 0
        for volume0, gamma0, volume1, gamma1 in points:
            _, matrix, rhs = face_system(branch_moduli(
                volume0, gamma0, volume1, gamma1, signs))
            if (matrix.rank(), matrix.row_join(rhs).rank()) != (32, 32):
                matches = False
                continue
            solved, free = solve_pinned(matrix, rhs)
            if tuple(str(symbol) for symbol in free) != DUALITY_NAMES:
                matches = False
            positive = all(minor > 0 for minor in leading_minors(solved))
            predicted = (region_predicate(gamma0, orientation[0])
                         and region_predicate(gamma1, orientation[1]))
            if positive != predicted:
                matches = False
            if positive:
                class_total += 1
                grid_total += 1
            else:
                found = False
                if not region_predicate(gamma0, orientation[0]) \
                        and degree_block(solved, 1).det() <= 0:
                    found = True
                if not region_predicate(gamma1, orientation[1]) \
                        and degree_block(solved, 2).det() <= 0:
                    found = True
                if not found:
                    killer = False
        census.append((orientation, class_total))
    return BlockFacts(
        tuple(classes), tuple(class_ranks), tuple(class_free),
        tuple(parameter_free), tuple(cross_zero), formulas_exact, decouple,
        gauge_exact, charpoly_plus, charpoly_minus, determinant_plus,
        determinant_minus, second_minor, echo, magnitude_parameters,
        len(points) * len(census), grid_total, tuple(census), matches, killer)


def measure_witnesses() -> WitnessFacts:
    """FAMILY E, MEASURED ONCE.  Three exact rational witnesses with their full
    eight leading principal minors, the open bounded duality region at the
    first of them, and Block 209's own exhibited point reproduced entry for
    entry against the LANDED literals."""
    _, w1_matrix, w1_rhs = face_system(branch_moduli(
        W1_MODULI[0], W1_MODULI[1], W1_MODULI[2], W1_MODULI[3], ALL_PLUS))
    w1_solved, _ = solve_pinned(w1_matrix, w1_rhs)
    w1_minors = leading_minors(w1_solved)
    w1_compatible = (w1_matrix.rank(),
                     w1_matrix.row_join(w1_rhs).rank()) == (32, 32)
    w1_nonuniform = w1_solved[0, 0] != w1_solved[1, 1]

    _, w2_matrix, w2_rhs = face_system(branch_moduli(
        W2_MODULI[0], W2_MODULI[1], W2_MODULI[2], W2_MODULI[3],
        flipped(("xy", 0), ("xy", 1))))
    w2_solved, _ = solve_pinned(w2_matrix, w2_rhs)

    w3_signs = flipped(("xy", 0), ("xy", 1))
    _, w3_matrix, w3_rhs = face_system(branch_moduli(
        W3_MODULI[0], W3_MODULI[1], W3_MODULI[2], W3_MODULI[3], w3_signs))
    w3_solved, _ = solve_pinned(w3_matrix, w3_rhs)
    w3_flips = tuple(
        sum(1 for name, off in FACE_KEYS
            if off == offset and w3_signs[(name, off)] < 0)
        for offset in (0, 1))

    duality_symbols = sorted(set(sp.symbols(" ".join(DUALITY_NAMES))), key=str)
    w1_open, _ = solve_pinned(w1_matrix, w1_rhs, at_zero=False)
    interior = dict(zip(duality_symbols, DUALITY_INTERIOR_CHOICE))
    zeros = {symbol: sp.Integer(0) for symbol in duality_symbols}
    interior_matrix = sp.Matrix(
        8, 8, lambda i, j: w1_open[i, j].subs(interior))
    a_bad = sp.Matrix(8, 8, lambda i, j: w1_open[i, j].subs(
        {**zeros, sp.Symbol("D07"): sp.Integer(1)}))
    b_bad = sp.Matrix(8, 8, lambda i, j: w1_open[i, j].subs(
        {**zeros, sp.Symbol("D16"): sp.Integer(2)}))
    duality_pairs = ((0, 7), (1, 6), (2, 5), (3, 4))
    duality_pair_minors = tuple(
        sp.expand(w1_open.extract(pair, pair).det())
        for pair in duality_pairs
    )

    _, landed_matrix, landed_rhs = face_system(branch_moduli(
        b209.RECIPROCAL_VOLUME_ZERO, b209.RECIPROCAL_SHEAR,
        b209.RECIPROCAL_VOLUME_ONE, b209.RECIPROCAL_SHEAR_ONE, ALL_PLUS))
    landed_ranks = (landed_matrix.rank(),
                    landed_matrix.row_join(landed_rhs).rank())
    landed_solved, landed_free = solve_pinned(landed_matrix, landed_rhs)
    spectrum_one = tuple(sorted(
        degree_block(landed_solved, 1).eigenvals().items(), key=str))
    spectrum_two = tuple(sorted(
        degree_block(landed_solved, 2).eigenvals().items(), key=str))
    negative_blocks = tuple(
        any(value < 0 for value, _ in sorted(
            degree_block(landed_solved, degree).eigenvals().items(), key=str))
        for degree in range(4))
    killing = (degree_block(landed_solved, 1).det(),
               degree_block(landed_solved, 2).det())
    killing_matches = bool(
        killing[0] == sp.cancel(
            b209.RECIPROCAL_VOLUME_ONE ** 3
            * (1 + b209.RECIPROCAL_SHEAR) ** 2
            * (1 - 2 * b209.RECIPROCAL_SHEAR))
        and killing[1] == sp.cancel(
            (1 + b209.RECIPROCAL_SHEAR_ONE) ** 2
            * (1 - 2 * b209.RECIPROCAL_SHEAR_ONE)
            / b209.RECIPROCAL_VOLUME_ZERO ** 3))

    _, flat_matrix, flat_rhs = face_system(branch_moduli(
        sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0), ALL_PLUS))
    flat_solved, _ = solve_pinned(flat_matrix, flat_rhs)

    return WitnessFacts(
        w1_minors, w1_compatible, bool(w1_nonuniform),
        leading_minors(w2_solved), leading_minors(w3_solved),
        (W3_MODULI[1], W3_MODULI[3]),
        w3_flips,
        leading_minors(interior_matrix), leading_minors(a_bad),
        leading_minors(b_bad), duality_pair_minors,
        landed_ranks, tuple(str(symbol) for symbol in landed_free),
        spectrum_one, spectrum_two, negative_blocks, killing,
        killing_matches, flat_solved == sp.eye(8))


def measure() -> Facts:
    """THE ONE MEASUREMENT PASS.  Three independent packages -- the variety,
    the degree blocks with the classification, and the witnesses with the
    landed reconciliation -- are built here and NOTHING below is recomputed.
    The expensive items are the sixty-four rank pairs of the sign-cell census,
    the four symbolic solves over QQ(t, u) and the thirty-two grid solves with
    their full eight leading principal minors; every coefficient matrix is over
    the INTEGERS and only the right-hand sides carry moduli."""
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
        len(SCOPED_HEADLINE_WORDS),
        measure_variety(),
        measure_blocks(),
        measure_witnesses(),
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
        "classification_is_universal": CLASSIFICATION_IS_UNIVERSAL_CLAIMED,
        "unnamed_words": len(UNNAMED_PHYSICS_WORDS),
        "orientation_is_physical": ORIENTATION_IS_PHYSICAL_CLAIMED,
        "scoped_words": len(SCOPED_HEADLINE_WORDS),
        "witness_is_observation": WITNESS_IS_OBSERVATION_CLAIMED,
        "generic_parameter_theorem": GENERIC_PARAMETER_THEOREM_CLAIMED,
        "continuum_limit": CONTINUUM_LIMIT_CLAIMED,
        "equations_of_motion": EQUATIONS_OF_MOTION_CLAIMED,
        "readings": len(READINGS),
        "readings_licensed": READINGS_LICENSED_CLAIMED,
        # C
        "six_face_equations": SIX_FACE_EQUATIONS,
        "builder_matches_landed": BUILDER_MATCHES_LANDED,
        "generic_ranks": GENERIC_RANKS,
        "coefficient_is_constant": COEFFICIENT_MATRIX_IS_CONSTANT,
        "zero_columns": DUALITY_NAMES,
        "zero_column_count": ZERO_COLUMN_COUNT,
        "pinned_rank": PINNED_COLUMN_RANK,
        "relation_count": RELATION_COUNT,
        "relations_match_landed": True,
        "relations_even": RELATIONS_EVEN_IN_EVERY_SHEAR,
        "volume_equalities_literal": True,
        "square_factorizations": SQUARE_FACTORIZATION_COUNT,
        "division_count": DIVISION_COUNT,
        "divisions_by_volumes": DIVISIONS_ARE_BY_VOLUMES,
        "tie_count": TIE_COUNT,
        "normal_form_kills_all": NORMAL_FORM_KILLS_ALL,
        "derived_identity": True,
        "non_isotropic_branches": NON_ISOTROPIC_BRANCHES,
        "variety_is_isotropic": VARIETY_IS_PER_OFFSET_ISOTROPIC,
        "sign_cells": SIGN_CELLS,
        "sign_cells_solvable": SIGN_CELLS_SOLVABLE,
        "off_variety_ranks": OFF_VARIETY_RANKS,
        "mirror_solvable": MIRROR_IS_SOLVABLE,
        "mirror_first_minor_negative": MIRROR_DIES_AT_FIRST_MINOR,
        "gauge_factor_patterns": GAUGE_FACTOR_PATTERNS,
        "gauge_classes": GAUGE_CLASSES,
        "gauge_orbit_size": GAUGE_ORBIT_SIZE,
        "gauge_invariants": GAUGE_INVARIANTS,
        "zariski_components": ZARISKI_COMPONENTS,
        "quadric_irreducible": QUADRIC_IS_IRREDUCIBLE,
        "uniform_numerators": UNIFORM_NUMERATORS,
        "uniform_solution": UNIFORM_SOLUTION,
        "uniform_still_flat_only": UNIFORM_STILL_FLAT_ONLY,
        # D
        "symbolic_classes": SYMBOLIC_CLASSES,
        "symbolic_ranks": SYMBOLIC_RANKS,
        "free_parameter_names": FREE_PARAMETER_NAMES,
        "blocks_parameter_free": BLOCKS_PARAMETER_FREE_IN_EVERY_CLASS,
        "cross_degree_zero": CROSS_DEGREE_ZERO_OFF_DUALITY,
        "block_formulas_exact": BLOCK_FORMULAS_EXACT,
        "corners_decouple": CORNERS_ZERO_AND_SEVEN_DECOUPLE,
        "gauge_congruence": GAUGE_CONGRUENCE_EXACT,
        "charpoly_factorizations": True,
        "determinant_positive": DETERMINANT_AT_POSITIVE_PRODUCT,
        "determinant_negative": DETERMINANT_AT_NEGATIVE_PRODUCT,
        "second_minor": SECOND_LEADING_MINOR_FORM,
        "echo_class_negated": ECHO_IS_CLASS_NEGATED,
        "bound_positive": MAGNITUDE_BOUND_AT_POSITIVE_PRODUCT,
        "bound_negative": MAGNITUDE_BOUND_AT_NEGATIVE_PRODUCT,
        "per_offset_independent": CLASSIFICATION_IS_PER_OFFSET_INDEPENDENT,
        "curved_pd_in_every_class": CURVED_PD_FAMILY_IN_EVERY_CLASS,
        "pd_family_dimension": CURVED_PD_FAMILY_DIMENSION,
        "grid_points": GRID_POINTS,
        "grid_pd_total": GRID_PD_TOTAL,
        "grid_census": GRID_CENSUS,
        "grid_matches_formula": GRID_MATCHES_REGION_FORMULA,
        "killer_is_block_determinant": KILLER_IS_A_DEGREE_BLOCK_DETERMINANT,
        # E
        "w1_minors": W1_MINORS,
        "w1_positive_definite": W1_IS_POSITIVE_DEFINITE,
        "w1_nonuniform": W1_IS_NONUNIFORM,
        "flat_only_over_nonuniform": FLAT_ONLY_OVER_NONUNIFORM_CLAIMED,
        "w2_minors": W2_MINORS,
        "w3_minors": W3_MINORS,
        "w2_positive_definite": W2_IS_POSITIVE_DEFINITE,
        "w3_positive_definite": W3_IS_POSITIVE_DEFINITE,
        "w3_flips": W3_FLIPS_PER_OFFSET,
        "w3_magnitudes_are_landed": W3_MAGNITUDES_ARE_THE_LANDED_ONES,
        "killer_was_the_sign_pattern": KILLER_WAS_THE_SIGN_PATTERN,
        "duality_region_open": DUALITY_REGION_IS_OPEN,
        "duality_region_bounded": DUALITY_REGION_IS_BOUNDED,
        "duality_pair_minors": DUALITY_PAIR_MINOR_FORMS,
        "landed_ranks": LANDED_RECIPROCAL_RANKS,
        "landed_free_names": b209.RECIPROCAL_FREE_NAMES,
        "landed_degree_one_spectrum": b209.DEGREE_ONE_SPECTRUM,
        "landed_degree_two_spectrum": b209.DEGREE_TWO_SPECTRUM,
        "landed_still_indefinite": LANDED_RECIPROCAL_STILL_INDEFINITE,
        "landed_killing_minors": LANDED_KILLING_MINORS,
        "flat_point_identity": FLAT_POINT_IS_IDENTITY,
        # F
        "scout_grade_only": SCOUT_GRADE_ONLY,
        "finite_linear_algebra": FINITE_EXACT_LINEAR_ALGEBRA,
        "physical_content": PHYSICAL_CONTENT_CLAIMED,
        "echo_noted_only": ECHO_NOTED_ONLY,
        "echo_interpreted": ECHO_INTERPRETED_CLAIMED,
        "structural_identification": STRUCTURAL_IDENTIFICATION_CLAIMED,
        "sign_products_invariant": SIGN_PRODUCTS_ARE_THE_INVARIANT,
        "signed_face_invariance": SIGNED_FACE_INVARIANCE_CLAIMED,
        "convention_tied": len(CONVENTION_TIED_OBJECTS),
        "block209_completed": BLOCK209_COMPLETED_NOT_CORRECTED,
        "block209_scoping_exact": BLOCK209_SCOPING_WAS_EXACT,
        "block209_correction": BLOCK209_CORRECTION_CLAIMED,
        "landed_numbers_corrected": LANDED_NUMBERS_CORRECTED,
        "classification_of_one_principle": CLASSIFICATION_IS_OF_ONE_PRINCIPLE,
        "geometry_selection": GEOMETRY_SELECTION_CLAIMED,
        "uniqueness_about_nature": UNIQUENESS_ABOUT_NATURE_CLAIMED,
        "classifies_every_positive_matrix":
            CLASSIFIES_EVERY_POSITIVE_MATRIX_CLAIMED,
        "instance_scope": INSTANCE_SCOPE_COUNT,
        "oblique_faces_open": OBLIQUE_FACES_REMAIN_OPEN,
        "selection_principle_open": SELECTION_PRINCIPLE_REMAINS_OPEN,
        "scope_generalisation": SCOPE_GENERALISATION_CLAIMED,
        # G
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
    elif mutation == "claim_classification_is_universal":
        # THE FIRST MISREAD: the exact PD region of ONE gluing principle's
        # compatible variety is asserted to be a classification of the
        # admissible geometries of nature.  It is a region in two magnitudes.
        claims["classification_is_universal"] = True
        claims["unnamed_words"] = 0
    elif mutation == "claim_orientation_is_physical":
        # THE SECOND MISREAD: a product of three shear signs inside one
        # declared convention is asserted to be a physical orientation.
        claims["orientation_is_physical"] = True
        claims["scoped_words"] = 0
    elif mutation == "claim_witness_is_observation":
        # THE THIRD MISREAD: an exact rational matrix with positive leading
        # minors is asserted to be an observation of something.
        claims["witness_is_observation"] = True
    elif mutation == "claim_continuum_readings_licensed":
        claims["generic_parameter_theorem"] = True
        claims["continuum_limit"] = True
        claims["equations_of_motion"] = True
        claims["readings_licensed"] = True
    # --- C ----------------------------------------------------------------
    elif mutation == "break_constant_coefficients":
        # THE STRUCTURAL FACT DENIED: the coefficient matrix is asserted to
        # carry moduli and to pin all thirty-six unknowns, which would make
        # solvability a point-by-point question and the duality freedom
        # accidental rather than universal.
        claims["coefficient_is_constant"] = False
        claims["zero_columns"] = ()
        claims["zero_column_count"] = 0
        claims["pinned_rank"] = 36
    elif mutation == "break_two_divisions":
        # THE DERIVATION'S HYGIENE DENIED: the reduction is asserted to divide
        # by something other than the two volumes, which would leave the
        # nonsingular-domain restriction doing hidden work.
        claims["division_count"] = 0
        claims["divisions_by_volumes"] = False
        claims["square_factorizations"] = 0
    elif mutation == "break_isotropic_variety":
        # THE HEADLINE STRUCTURE DENIED: a non-isotropic-per-offset branch is
        # asserted to exist, so the compatible set would NOT be the
        # two-parameter magnitude family and no classification could be
        # closed over it.
        claims["normal_form_kills_all"] = False
        claims["non_isotropic_branches"] = 1
        claims["variety_is_isotropic"] = False
        claims["tie_count"] = 0
    elif mutation == "break_gauge_classes":
        # THE INVARIANT CONTENT DENIED: the sixty-four sign cells are asserted
        # to be sixty-four inequivalent branches rather than four gauge
        # classes, which would make the individual signs invariant content.
        claims["gauge_classes"] = 64
        claims["gauge_orbit_size"] = 1
        claims["gauge_invariants"] = ()
    elif mutation == "break_uniform_survives":
        # BLOCK 209's UNIFORM THEOREM DENIED: the uniform locus is asserted to
        # admit a curved cell once the branch ties are used, which would make
        # this block a CORRECTION of Block 209 rather than a completion.
        claims["uniform_solution"] = (sp.Rational(3, 5), sp.Rational(4, 5))
        claims["uniform_numerators"] = (UNIFORM_NUMERATORS[0],)
        claims["uniform_still_flat_only"] = False
    # --- D ----------------------------------------------------------------
    elif mutation == "break_symbolic_freedom":
        claims["symbolic_ranks"] = (32, 33)
        claims["free_parameter_names"] = ()
        claims["blocks_parameter_free"] = False
    elif mutation == "break_block_formulas":
        claims["block_formulas_exact"] = False
        claims["corners_decouple"] = False
        claims["gauge_congruence"] = False
    elif mutation == "break_orientation_determinants":
        # THE SPLIT COLLAPSED: both orientation classes are asserted to carry
        # the same determinant, which would remove the sign dependence that
        # is the whole content of the classification.
        claims["determinant_positive"] = DETERMINANT_AT_NEGATIVE_PRODUCT
        claims["echo_class_negated"] = False
    elif mutation == "break_classification_region":
        # THE CLASSIFICATION DENIED: both orientation classes are asserted to
        # stop at one half, which would make the negative-orientation curved
        # PD families disappear and leave the flat-only reading standing on
        # every large-magnitude branch.
        claims["bound_negative"] = HALF
        claims["curved_pd_in_every_class"] = False
        claims["per_offset_independent"] = False
    elif mutation == "break_grid_census":
        claims["grid_pd_total"] = 3
        claims["grid_census"] = (((1, 1), 3), ((1, -1), 0),
                                 ((-1, 1), 0), ((-1, -1), 0))
        claims["killer_is_block_determinant"] = False
    # --- E ----------------------------------------------------------------
    elif mutation == "break_witness_w1":
        # CORRECTION 111, UN-CORRECTED: the supervising record's announced
        # flat-only extension -- 'literal gluing plus positivity admits
        # exactly the flat cell', never landed, and declined by Block 209 --
        # is asserted here, so W1 would have to be non-positive.  Its eight
        # leading minors are all strictly positive.  Disclosed as the
        # adversarial path working, not smoothed.
        claims["w1_positive_definite"] = False
        claims["flat_only_over_nonuniform"] = True
        claims["w1_minors"] = ()
    elif mutation == "break_witness_sign_classes":
        claims["w3_positive_definite"] = False
        claims["killer_was_the_sign_pattern"] = False
        claims["w2_minors"] = ()
    elif mutation == "break_duality_region":
        claims["duality_region_bounded"] = False
        claims["duality_region_open"] = False
    elif mutation == "break_landed_reconciliation":
        # THE LANDED POINT REWRITTEN: Block 209's exhibited all-plus cell is
        # asserted to be positive definite after all.  It is not, and this
        # block reproduces its landed spectra to say so.
        claims["landed_still_indefinite"] = False
        claims["landed_killing_minors"] = (sp.Integer(1), sp.Integer(1))
    # --- F ----------------------------------------------------------------
    elif mutation == "break_scout_grade_fence":
        claims["scout_grade_only"] = False
        claims["physical_content"] = True
    elif mutation == "claim_echo_interpreted":
        # THE CHECKER'S C6 QUALIFICATION DELETED: the exact agreement between
        # this block's determinant pair and Block 209's D3 kappa bounds is
        # asserted to identify the two constructions.  Two polynomials agree;
        # no carrier map exists and none is built here.
        claims["echo_interpreted"] = True
        claims["echo_noted_only"] = False
        claims["structural_identification"] = True
    elif mutation == "claim_signs_invariant":
        claims["signed_face_invariance"] = True
        claims["convention_tied"] = 0
    elif mutation == "claim_block209_corrected":
        # THE COMPLETION MISREPORTED AS A CORRECTION: Block 209 is asserted to
        # have been wrong.  Its rigidity statement was scoped ON THE CHECKED
        # BRANCHES and it declined to assert the wider sentence; this block
        # closes the branch it named open and touches no landed number.
        claims["block209_correction"] = True
        claims["block209_completed"] = False
        claims["landed_numbers_corrected"] = 1
    elif mutation == "claim_geometry_selected":
        # THE CHECKER'S C6 SECOND QUALIFICATION DELETED: the classification is
        # asserted to select a geometry and to classify every positive matrix,
        # rather than the PD-solvability of the MODULI of one principle.
        claims["geometry_selection"] = True
        claims["uniqueness_about_nature"] = True
        claims["classifies_every_positive_matrix"] = True
    elif mutation == "break_instance_scope":
        claims["instance_scope"] = 0
        claims["oblique_faces_open"] = False
        claims["selection_principle_open"] = False
    # --- G ----------------------------------------------------------------
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
    variety = facts.variety
    blocks = facts.blocks
    witnesses = facts.witnesses
    magnitude = sp.Symbol("g", nonnegative=True)

    def polynomial(text: str):
        return sp.expand(sp.sympify(text.replace("^", "**"),
                                    locals={"g": magnitude}))

    # --- A: AUTHORITY -------------------------------------------------------
    checks.check(
        "A-1", f"origin/main is {claims['main_head']}, the axiom and registry "
        f"blobs match on origin/main AND in the worktree, and the audit "
        f"timeout is {AUDIT_TIMEOUT_SEC}s",
        authority.fixed_authority and facts.main_head == claims["main_head"])
    checks.check(
        "A-2", f"PARENT_COMMIT {claims['parent_commit'][:12]} is a real "
        f"ancestor of HEAD resolving PARENT_REF, both Block 210 artifacts are "
        f"content-identical at it and in the worktree, the stale pin "
        f"{STALE_PARENT_COMMIT[:12]} -- the Block 209 tip -- is a real "
        f"ancestor carrying NEITHER, BOTH machinery imports are landed (Block "
        f"105's shear_hodge through Block 128, and Block 209's own runner for "
        f"the landed literals family E reconciles against), and "
        f"{authority.inputs_readable} of {len(AUDIT_INPUT_PATHS) - 1} audit "
        f"inputs are readable",
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
        "B-3", f"THE WORD *CLASSIFICATION* IS SCOPED BEFORE THE FIRST NUMERAL: "
        f"it names the EXACT positive-definiteness region of ONE gluing "
        f"principle's compatible moduli variety, and it names NO uniqueness "
        f"theorem about nature, NO selection among geometries and NO no-go; "
        f"classification_is_universal = {claims['classification_is_universal']} "
        f"and the {claims['unnamed_words']} words {UNNAMED_PHYSICS_WORDS} name "
        f"NOTHING established here",
        claims["classification_is_universal"] is False
        and facts.unnamed_words == claims["unnamed_words"])
    checks.check(
        "B-4", f"THE WORD *ORIENTATION* IS SCOPED: it names the PRODUCT of the "
        f"three shear signs at one offset, inside one declared sub-corner and "
        f"wedge convention, whose value moves the third leading minor of a "
        f"3 x 3 rational matrix; it names NO spacetime orientation, NO "
        f"chirality and NO physical parity; orientation_is_physical = "
        f"{claims['orientation_is_physical']}, and "
        f"{claims['scoped_words']} headline words {SCOPED_HEADLINE_WORDS} are "
        f"scoped before any number is read",
        claims["orientation_is_physical"] is False
        and facts.scoped_words == claims["scoped_words"])
    checks.check(
        "B-5", f"THE WORD *WITNESS* IS SCOPED: it names an exact rational "
        f"8 x 8 corner matrix whose eight leading principal minors are "
        f"computed and found strictly positive; it names NO observation, NO "
        f"measurement, NO experiment and NO physical object; "
        f"witness_is_observation = {claims['witness_is_observation']}",
        claims["witness_is_observation"] is False)
    checks.check(
        "B-6", f"NO GENERIC-PARAMETER THEOREM, NO CONTINUUM LIMIT AND NO "
        f"EQUATIONS OF MOTION, AND THE READINGS ARE READINGS: "
        f"{claims['readings']} of them are enumerated as readings, "
        f"readings_licensed = {claims['readings_licensed']}, and EVERY "
        f"NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER "
        f"METAPHYSICAL NECESSITY -- the cycle-913 caution, carried verbatim, "
        f"with nothing registered and nothing adopted",
        claims["generic_parameter_theorem"] is False
        and claims["continuum_limit"] is False
        and claims["equations_of_motion"] is False
        and facts.readings == claims["readings"]
        and claims["readings_licensed"] is False
        and not REGISTERED_OBJECTS and not ADOPTED_OBJECTS
        and claims["registered"] == 0 and claims["adopted"] == 0)

    # --- C: THE VARIETY -----------------------------------------------------
    checks.check(
        "C-1", f"THE SYSTEM IS CONSTANT-COEFFICIENT AND THE FOUR DUALITY "
        f"COLUMNS ARE ZERO, WHICH IS WHY ONE CLASSIFICATION CAN COVER EVERY "
        f"MODULI POINT AT ONCE: the per-face builder reproduces Block 209's "
        f"landed literal_system equation for equation "
        f"({claims['builder_matches_landed']}) at "
        f"{claims['six_face_equations']} equations on {CELL_UNKNOWNS} "
        f"unknowns with ranks {claims['generic_ranks']} at generic per-face "
        f"moduli; the coefficient matrix carries NO moduli "
        f"({claims['coefficient_is_constant']}); EXACTLY "
        f"{claims['zero_column_count']} of its columns are zero and they are "
        f"{claims['zero_columns']}; and its rank on the other 32 columns is "
        f"{claims['pinned_rank']}, so the pinned entries are UNIQUE and the "
        f"free parameters are ALWAYS exactly the four duality pairings",
        variety.equations == claims["six_face_equations"]
        and variety.builder_matches_landed is claims["builder_matches_landed"]
        and claims["builder_matches_landed"] is True
        and variety.generic_ranks == claims["generic_ranks"]
        and claims["generic_ranks"][0] != claims["generic_ranks"][1]
        and variety.coefficient_is_constant
        is claims["coefficient_is_constant"]
        and claims["coefficient_is_constant"] is True
        and variety.zero_columns == claims["zero_columns"]
        and len(variety.zero_columns) == claims["zero_column_count"]
        and variety.pinned_rank == claims["pinned_rank"])
    checks.check(
        "C-2", f"EVERY RELATION IS EVEN IN EVERY SHEAR AND THE REDUCTION USES "
        f"EXACTLY {claims['division_count']} DIVISIONS, BOTH BY VOLUMES "
        f"({claims['divisions_by_volumes']}): the "
        f"{claims['relation_count']} forced relations re-measured from the "
        f"cokernel equal Block 209's landed SIX_FACE_RELATIONS "
        f"({claims['relations_match_landed']}); each has degree 0 or 2 in "
        f"each of the six shears ({claims['relations_even']}), so the variety "
        f"is invariant under flipping ANY individual face sign; the four "
        f"per-offset volume equalities appear LITERALLY among them "
        f"({claims['volume_equalities_literal']}); and after volume "
        f"equalization {claims['square_factorizations']} relations factor "
        f"exactly as v * (X_a - X_b), equalizing the per-offset shear SQUARES",
        len(variety.relations) == claims["relation_count"]
        and variety.relations_match_landed is claims["relations_match_landed"]
        and claims["relations_match_landed"] is True
        and variety.relations_even is claims["relations_even"]
        and claims["relations_even"] is True
        and variety.volume_equalities_literal
        is claims["volume_equalities_literal"]
        and claims["volume_equalities_literal"] is True
        and variety.square_factorizations == claims["square_factorizations"]
        and claims["square_factorizations"] == 4
        and len(variety.divisions) == 1
        and claims["division_count"] == 2
        and claims["divisions_by_volumes"] is True)
    checks.check(
        "C-3", f"THE VARIETY IS EXACTLY THE PER-OFFSET-ISOTROPIC FAMILY, AND "
        f"NO NON-ISOTROPIC BRANCH EXISTS: the eight reciprocal couplings "
        f"collapse to EXACTLY {claims['tie_count']} ties -- "
        f"{TIE_A_FORM} and {TIE_B_FORM} -- whose polynomial consequence is "
        f"{DERIVED_IDENTITY_FORM} ({claims['derived_identity']}); and the "
        f"CONVERSE normal form v_f0 = v1 (1 - X0), v_f1 = v1, c_f0^2 = X0, "
        f"c_f1^2 = 1 - v1^2 (1 - X0) kills all sixteen relations IDENTICALLY "
        f"({claims['normal_form_kills_all']}), leaving "
        f"{claims['non_isotropic_branches']} non-isotropic branches "
        f"({claims['variety_is_isotropic']})",
        variety.tie_count == claims["tie_count"]
        and claims["tie_count"] == 2
        and variety.derived_identity is claims["derived_identity"]
        and claims["derived_identity"] is True
        and variety.normal_form_kills_all is claims["normal_form_kills_all"]
        and claims["normal_form_kills_all"] is True
        and variety.non_isotropic_branches
        == claims["non_isotropic_branches"]
        and claims["non_isotropic_branches"] == ZERO_RESIDUAL
        and claims["variety_is_isotropic"] is True)
    checks.check(
        "C-4", f"SIGNS ENTER ONLY THROUGH THE PER-OFFSET PRODUCTS: all "
        f"{claims['sign_cells']} shear-sign cells are solvable at ranks "
        f"(32, 32) ({claims['sign_cells_solvable']} of them) while a point "
        f"OFF the variety is insolvable at {claims['off_variety_ranks']}, so "
        f"the relations really bind; the negative-volume mirror is compatible "
        f"({claims['mirror_solvable']}) and dies at the FIRST minor "
        f"({claims['mirror_first_minor_negative']}); the corner-sign gauge "
        f"D -> E D E realizes {claims['gauge_factor_patterns']} factor "
        f"patterns and cuts the cells into EXACTLY {claims['gauge_classes']} "
        f"orbits of {claims['gauge_orbit_size']}, indexed by "
        f"{claims['gauge_invariants']}; and the Zariski closure has "
        f"{claims['zariski_components']} components, one per sign-ratio class, "
        f"the defining quadric being irreducible "
        f"({claims['quadric_irreducible']})",
        variety.sign_cells == claims["sign_cells"]
        and variety.sign_cells_solvable == claims["sign_cells_solvable"]
        and claims["sign_cells_solvable"] == claims["sign_cells"]
        and variety.off_variety_ranks == claims["off_variety_ranks"]
        and claims["off_variety_ranks"][0] != claims["off_variety_ranks"][1]
        and (variety.mirror_ranks == (32, 32)) is claims["mirror_solvable"]
        and claims["mirror_solvable"] is True
        and bool(variety.mirror_first_minor < 0)
        is claims["mirror_first_minor_negative"]
        and claims["mirror_first_minor_negative"] is True
        and variety.gauge_factor_patterns == claims["gauge_factor_patterns"]
        and variety.gauge_orbits == claims["gauge_classes"]
        and set(variety.gauge_orbit_sizes) == {claims["gauge_orbit_size"]}
        and variety.gauge_invariants == claims["gauge_invariants"]
        and len(claims["gauge_invariants"]) == claims["gauge_classes"]
        and variety.ratio_classes == claims["zariski_components"]
        and variety.quadric_irreducible is claims["quadric_irreducible"]
        and claims["quadric_irreducible"] is True)
    checks.check(
        "C-5", f"AND BLOCK 209's UNIFORM RESULT STILL STANDS, RE-DERIVED FROM "
        f"THE BRANCH TIES RATHER THAN RE-SOLVED: at v0 = v1 = v and "
        f"c0 = c1 = c the two ties become EXACTLY the landed numerators "
        f"{claims['uniform_numerators']}, and their joint solution over v > 0 "
        f"with c real is the SINGLE point (c, v) = "
        f"{claims['uniform_solution']}, so the uniform locus admits ONLY the "
        f"flat cell ({claims['uniform_still_flat_only']}) -- the "
        f"classification below is about the NONUNIFORM branches and takes "
        f"nothing away from it",
        variety.uniform_numerators == tuple(sorted(
            claims["uniform_numerators"]))
        and len(claims["uniform_numerators"]) == 2
        and tuple(sorted(claims["uniform_numerators"]))
        == tuple(sorted(b209.UNIFORM_CONSTRAINTS))
        and variety.uniform_solutions == (claims["uniform_solution"],)
        and claims["uniform_solution"] == b209.UNIFORM_SOLUTION
        and claims["uniform_still_flat_only"] is True)

    # --- D: THE BLOCKS AND THE CLASSIFICATION -------------------------------
    checks.check(
        "D-1", f"AT SYMBOLIC MODULI, IN ALL {claims['symbolic_classes']} SIGN "
        f"CLASSES, THE FREEDOM IS THE FOUR DUALITY PARAMETERS AND THE DEGREE "
        f"BLOCKS CONTAIN NONE OF THEM: each class solves over QQ(t, u) at "
        f"ranks {claims['symbolic_ranks']} -- CONSISTENT -- with free "
        f"parameters exactly {claims['free_parameter_names']} "
        f"({claims['blocks_parameter_free']} for block parameter-freedom in "
        f"every class), and every cross-degree entry other than those four is "
        f"exactly zero ({claims['cross_degree_zero']}); the Block 209 "
        f"principal-submatrix argument therefore holds at SYMBOLIC moduli and "
        f"not only at one point",
        len(blocks.classes) == claims["symbolic_classes"]
        and set(blocks.class_ranks) == {claims["symbolic_ranks"]}
        and claims["symbolic_ranks"][0] == claims["symbolic_ranks"][1]
        and set(blocks.class_free_names) == {claims["free_parameter_names"]}
        and len(claims["free_parameter_names"]) == FREE_PARAMETER_COUNT
        and all(blocks.blocks_parameter_free)
        is claims["blocks_parameter_free"]
        and claims["blocks_parameter_free"] is True
        and all(blocks.cross_degree_zero) is claims["cross_degree_zero"]
        and claims["cross_degree_zero"] is True)
    checks.check(
        "D-2", f"THE DEGREE BLOCKS AS EXACT FUNCTIONS OF THE BRANCH "
        f"PARAMETERS, IN ALL FOUR CLASSES: {DEGREE_BLOCK_FORMS} "
        f"({claims['block_formulas_exact']}); corners 0 and 7 decouple from "
        f"all six middle corners ({claims['corners_decouple']}), so D is the "
        f"orthogonal sum of the {{0, 7}} pair block and the 6 x 6 block with "
        f"antidiagonal duality coupling; and the corner-sign gauge congruence "
        f"E D E is verified in the FIELD, mapping the all-plus solution "
        f"exactly onto the flipped system's solution "
        f"({claims['gauge_congruence']})",
        blocks.block_formulas_exact is claims["block_formulas_exact"]
        and claims["block_formulas_exact"] is True
        and blocks.corners_decouple is claims["corners_decouple"]
        and claims["corners_decouple"] is True
        and blocks.gauge_congruence_exact is claims["gauge_congruence"]
        and claims["gauge_congruence"] is True)
    checks.check(
        "D-3", f"THE ORIENTATION SPLIT OF THE SIGNED TRIANGLE, EXACT: "
        f"eigenvalues {EIGENVALUES_AT_POSITIVE_PRODUCT} at pi = +1 against "
        f"{EIGENVALUES_AT_NEGATIVE_PRODUCT} at pi = -1 "
        f"({claims['charpoly_factorizations']}), determinants "
        f"{claims['determinant_positive']} and "
        f"{claims['determinant_negative']}, with the second leading minor "
        f"{claims['second_minor']} positive on the domain so Sylvester "
        f"reduces positivity to the determinant; THAT PAIR IS AN EXACT ECHO "
        f"OF BLOCK 209's D3 kappa BOUNDS WITH THE CLASS LABEL NEGATED "
        f"({claims['echo_class_negated']}) -- MEASURED HERE AND INTERPRETED "
        f"NOWHERE, the fence being carried at F-2",
        claims["charpoly_factorizations"] is True
        and blocks.charpoly_positive and blocks.charpoly_negative
        and sp.expand(blocks.determinant_positive.subs(
            sp.Symbol("gamma", nonnegative=True), magnitude)
            - polynomial(claims["determinant_positive"])) == 0
        and sp.expand(blocks.determinant_negative.subs(
            sp.Symbol("gamma", nonnegative=True), magnitude)
            - polynomial(claims["determinant_negative"])) == 0
        and sp.expand(blocks.second_minor.subs(
            sp.Symbol("gamma", nonnegative=True), magnitude)
            - polynomial(claims["second_minor"])) == 0
        and blocks.echo_class_negated is claims["echo_class_negated"]
        and claims["echo_class_negated"] is True)
    checks.check(
        "D-4", f"THE CLASSIFICATION, CLOSED AND PER-OFFSET INDEPENDENT: D is "
        f"PD-solvable at a compatible point IFF gamma0 < "
        f"{claims['bound_positive']} when pi0 = +1 and gamma0 < "
        f"{claims['bound_negative']} when pi0 = -1, AND independently the "
        f"same for (gamma1, pi1) ({claims['per_offset_independent']}); "
        f"necessity is the parameter-free principal blocks of D-1 and "
        f"sufficiency is the direct sum at zero duality coupling; the "
        f"magnitude base has {claims['pd_family_dimension']} parameters, so "
        f"EVERY gauge class carries a {claims['pd_family_dimension']}"
        f"-parameter CURVED positive definite family "
        f"({claims['curved_pd_in_every_class']}) -- and the two bounds are "
        f"DIFFERENT, which is the whole content",
        blocks.magnitude_parameters == claims["pd_family_dimension"]
        and claims["bound_positive"] == HALF
        and claims["bound_negative"] == sp.Integer(1)
        and claims["bound_positive"] != claims["bound_negative"]
        and claims["per_offset_independent"] is True
        and all(count >= 2 for _, count in blocks.grid_census)
        is claims["curved_pd_in_every_class"]
        and claims["curved_pd_in_every_class"] is True)
    checks.check(
        "D-5", f"AND THE REGION FORMULA IS VERIFIED POINTWISE, NOT SAMPLED "
        f"FOR ENCOURAGEMENT: {claims['grid_points']} exact solves -- eight "
        f"rational magnitude points on each of the four classes, full 8 x 8 "
        f"leading minors at the degree-diagonal representative -- agree with "
        f"the formula at EVERY point ({claims['grid_matches_formula']}), "
        f"census {claims['grid_census']} out of {GRID_POINTS_PER_CLASS} per "
        f"class and {claims['grid_pd_total']} of {claims['grid_points']} "
        f"overall; and at every non-PD point the parameter-free degree-1 or "
        f"degree-2 DETERMINANT is <= 0 "
        f"({claims['killer_is_block_determinant']}), killing all duality "
        f"choices at once",
        blocks.grid_points == claims["grid_points"]
        and blocks.grid_pd_total == claims["grid_pd_total"]
        and blocks.grid_census == claims["grid_census"]
        and sum(count for _, count in claims["grid_census"])
        == claims["grid_pd_total"]
        and blocks.grid_matches_formula is claims["grid_matches_formula"]
        and claims["grid_matches_formula"] is True
        and blocks.killer_is_block_determinant
        is claims["killer_is_block_determinant"]
        and claims["killer_is_block_determinant"] is True)

    # --- E: THE WITNESSES AND THE LANDED-POINT RECONCILIATION ---------------
    checks.check(
        "E-1", f"WITNESS W1 REFUTES THE FLAT-ONLY EXTENSION OUTRIGHT: at "
        f"magnitudes 1/4 on all six faces with v0 = 15/16 and v1 = 1, the "
        f"point is compatible and NONUNIFORM ({claims['w1_nonuniform']}) and "
        f"its eight leading principal minors are {claims['w1_minors']} -- ALL "
        f"STRICTLY POSITIVE ({claims['w1_positive_definite']}); so "
        f"flat_only_over_nonuniform = "
        f"{claims['flat_only_over_nonuniform']}: a curved literal six-face "
        f"cell IS a positive definite corner matrix, and the announced "
        f"'literal gluing plus positivity admits exactly the flat cell' "
        f"extension -- never landed, and declined by Block 209 -- is REFUTED",
        witnesses.w1_minors == claims["w1_minors"]
        and all(minor > 0 for minor in claims["w1_minors"])
        and len(claims["w1_minors"]) == 8
        and witnesses.w1_compatible
        and witnesses.w1_nonuniform is claims["w1_nonuniform"]
        and claims["w1_nonuniform"] is True
        and claims["w1_positive_definite"] is True
        and claims["flat_only_over_nonuniform"] is False)
    checks.check(
        "E-2", f"AND THE KILLER WAS THE SIGN PATTERN, NOT THE CURVATURE: W2 "
        f"carries magnitudes 3/4 -- far beyond the all-plus kill point 1/2 -- "
        f"on class (-1, -1) with minors {claims['w2_minors']}, all positive "
        f"({claims['w2_positive_definite']}); and W3 carries THE LANDED "
        f"MAGNITUDES {(b209.RECIPROCAL_SHEAR, b209.RECIPROCAL_SHEAR_ONE)} "
        f"({claims['w3_magnitudes_are_landed']}) with exactly "
        f"{claims['w3_flips']} sign flipped per offset and minors "
        f"{claims['w3_minors']}, all positive "
        f"({claims['w3_positive_definite']}) -- POSITIVE DEFINITE AT THE VERY "
        f"MAGNITUDES BLOCK 209 PROVED INDEFINITE ALL-PLUS "
        f"({claims['killer_was_the_sign_pattern']})",
        witnesses.w2_minors == claims["w2_minors"]
        and all(minor > 0 for minor in claims["w2_minors"])
        and claims["w2_positive_definite"] is True
        and witnesses.w3_minors == claims["w3_minors"]
        and all(minor > 0 for minor in claims["w3_minors"])
        and claims["w3_positive_definite"] is True
        and witnesses.w3_flip_count == claims["w3_flips"]
        and (witnesses.w3_magnitudes == (b209.RECIPROCAL_SHEAR,
                                         b209.RECIPROCAL_SHEAR_ONE))
        is claims["w3_magnitudes_are_landed"]
        and claims["w3_magnitudes_are_landed"] is True
        and witnesses.landed_negative_blocks[1]
        and witnesses.landed_negative_blocks[2]
        and claims["killer_was_the_sign_pattern"] is True)
    checks.check(
        "E-3", f"THE DUALITY REGION IS OPEN AND FOUR-DIMENSIONAL BUT BOUNDED, "
        f"SO THE CLASSIFICATION IS OF PD-SOLVABILITY AND NOT OF EVERY "
        f"INDIVIDUAL D: at W1 the interior choice "
        f"(a, b, c, d) = {DUALITY_INTERIOR_CHOICE} keeps all eight minors "
        f"positive ({claims['duality_region_open']}); boundedness follows "
        f"because the four 2 x 2 principal minors are exactly "
        f"{claims['duality_pair_minors']}, imposing {DUALITY_BOUND_FORM} "
        f"({claims['duality_region_bounded']}).  The a = 1 and b = 2 points "
        f"are explicit boundary-crossing checks, not the boundedness proof",
        all(minor > 0 for minor in witnesses.duality_interior_minors)
        is claims["duality_region_open"]
        and claims["duality_region_open"] is True
        and witnesses.duality_pair_minors == claims["duality_pair_minors"]
        and (not all(minor > 0 for minor in witnesses.duality_a_bad_minors)
             and not all(minor > 0
                         for minor in witnesses.duality_b_bad_minors))
        is claims["duality_region_bounded"]
        and claims["duality_region_bounded"] is True)
    checks.check(
        "E-4", f"AND BLOCK 209's EXHIBITED POINT IS REPRODUCED UNCHANGED, "
        f"WHICH IS WHAT MAKES THIS A COMPLETION: at the landed all-plus "
        f"reciprocal moduli the system has ranks {claims['landed_ranks']} "
        f"with free parameters {claims['landed_free_names']}, its degree-1 "
        f"and degree-2 spectra are {claims['landed_degree_one_spectrum']} and "
        f"{claims['landed_degree_two_spectrum']} -- EQUAL to Block 209's own "
        f"literals -- and it is still INDEFINITE "
        f"({claims['landed_still_indefinite']}), killed by the "
        f"parameter-free determinants {claims['landed_killing_minors']} that "
        f"the general block formulas predict; the flat point returns the 8 x 8 "
        f"identity ({claims['flat_point_identity']})",
        witnesses.landed_ranks == claims["landed_ranks"]
        and claims["landed_ranks"][0] == claims["landed_ranks"][1]
        and witnesses.landed_free_names == claims["landed_free_names"]
        and witnesses.landed_degree_one_spectrum
        == claims["landed_degree_one_spectrum"]
        and witnesses.landed_degree_two_spectrum
        == claims["landed_degree_two_spectrum"]
        and claims["landed_degree_one_spectrum"] == b209.DEGREE_ONE_SPECTRUM
        and claims["landed_degree_two_spectrum"] == b209.DEGREE_TWO_SPECTRUM
        and witnesses.landed_killing_minors
        == claims["landed_killing_minors"]
        and all(minor < 0 for minor in claims["landed_killing_minors"])
        is claims["landed_still_indefinite"]
        and claims["landed_still_indefinite"] is True
        and witnesses.landed_killing_matches_formula
        and witnesses.flat_point_is_identity is claims["flat_point_identity"]
        and claims["flat_point_identity"] is True)

    # --- F: THE SIX SCOPE FENCES -------------------------------------------
    checks.check(
        "F-1", f"FENCE ONE -- ALL OF IT IS SCOUT-GRADE FINITE EXACT LINEAR "
        f"ALGEBRA: scout_grade_only = {claims['scout_grade_only']}, "
        f"finite_linear_algebra = {claims['finite_linear_algebra']}, and "
        f"physical_content = {claims['physical_content']}; ranks, cokernels, "
        f"leading minors and eigenvalues over QQ and over rational function "
        f"fields in the moduli, with NO spacetime, NO dynamics and NO gravity "
        f"supplied by any line, the nine unsupplied gravity structures being "
        f"enumerated separately at B-2 so neither leans on the other",
        claims["scout_grade_only"] is True
        and claims["finite_linear_algebra"] is True
        and claims["physical_content"] is False)
    checks.check(
        "F-2", f"FENCE TWO -- THE ORIENTATION ECHO IS NOTED AND NEVER "
        f"INTERPRETED: echo_noted_only = {claims['echo_noted_only']}, "
        f"echo_interpreted = {claims['echo_interpreted']} and "
        f"structural_identification = {claims['structural_identification']}; "
        f"the determinant pair measured at D-3 agrees polynomially with Block "
        f"209's honest-lift kappa bounds with the class label negated, and "
        f"that is ALL that is measured -- no carrier map is constructed, no "
        f"objects are identified and the ONLY licensed phrase is "
        f"'{LICENSED_ECHO_PHRASE}'",
        claims["echo_noted_only"] is True
        and claims["echo_interpreted"] is False
        and claims["structural_identification"] is False)
    checks.check(
        "F-3", f"FENCE THREE -- THE SIGN PRODUCTS ARE THE INVARIANT CONTENT "
        f"AND THE INDIVIDUAL SIGNS ARE CONVENTION-TIED, BLOCK 209's G-4 "
        f"DISCIPLINE INHERITED: sign_products_invariant = "
        f"{claims['sign_products_invariant']} and signed_face_invariance = "
        f"{claims['signed_face_invariance']}, with "
        f"{claims['convention_tied']} convention-tied objects enumerated "
        f"({CONVENTION_TIED_OBJECTS}); the corner-sign gauge measured at C-4 "
        f"moves every individual face sign inside a class while moving "
        f"neither pi0 nor pi1",
        claims["sign_products_invariant"] is True
        and claims["signed_face_invariance"] is False
        and claims["convention_tied"] == len(CONVENTION_TIED_OBJECTS)
        and claims["convention_tied"] > 0)
    checks.check(
        "F-4", f"FENCE FOUR -- BLOCK 209 IS COMPLETED AND NOT CORRECTED: "
        f"block209_completed = {claims['block209_completed']}, "
        f"block209_scoping_exact = {claims['block209_scoping_exact']} and "
        f"block209_correction = {claims['block209_correction']}, with "
        f"landed_numbers_corrected = {claims['landed_numbers_corrected']}; "
        f"Block 209 wrote its rigidity statement ON THE CHECKED BRANCHES and "
        f"declined the wider sentence, this block closes the branch it named "
        f"open, and every landed number -- reproduced at E-4 by the family "
        f"that measures it -- STANDS EXACTLY AS LANDED",
        claims["block209_completed"] is True
        and claims["block209_scoping_exact"] is True
        and claims["block209_correction"] is False
        and claims["landed_numbers_corrected"] == ZERO_RESIDUAL)
    checks.check(
        "F-5", f"FENCE FIVE -- 'CLASSIFICATION' NAMES ONE PRINCIPLE's PD "
        f"REGION AND SELECTS NOTHING: classification_of_one_principle = "
        f"{claims['classification_of_one_principle']}, geometry_selection = "
        f"{claims['geometry_selection']}, uniqueness_about_nature = "
        f"{claims['uniqueness_about_nature']} and "
        f"classifies_every_positive_matrix = "
        f"{claims['classifies_every_positive_matrix']}; what is classified is "
        f"the PD-SOLVABILITY OF THE MODULI, and at a fixed admissible point "
        f"the solution still carries four duality coordinates restricted to "
        f"the open bounded region measured at E-3",
        claims["classification_of_one_principle"] is True
        and claims["geometry_selection"] is False
        and claims["uniqueness_about_nature"] is False
        and claims["classifies_every_positive_matrix"] is False)
    checks.check(
        "F-6", f"FENCE SIX -- THE INSTANCE SCOPE, ENUMERATED RATHER THAN "
        f"GESTURED AT: {claims['instance_scope']} restrictions "
        f"({INSTANCE_SCOPE}), scope_generalisation = "
        f"{claims['scope_generalisation']}, and the two questions Block 209 "
        f"stopped at that this block does NOT answer remain open -- oblique "
        f"and non-coordinate faces ({claims['oblique_faces_open']}) and the "
        f"principle that would select the shape rule over the honest metric "
        f"geometry or the reverse ({claims['selection_principle_open']})",
        claims["instance_scope"] == len(INSTANCE_SCOPE)
        and claims["instance_scope"] == INSTANCE_SCOPE_COUNT
        and claims["instance_scope"] > 0
        and claims["scope_generalisation"] is False
        and claims["oblique_faces_open"] is True
        and claims["selection_principle_open"] is True)

    # --- G: THE NOTE, THE FENCE AND THE EXACTNESS HYGIENE -------------------
    checks.check(
        "G-1", f"the note is present at {NOTE_PATH.name} and the N5 fence "
        f"appears in it VERBATIM as a single line",
        NOTE_PATH.is_file() is claims["note_present"]
        and facts.scope == claims["scope"])
    checks.check(
        "G-2", f"sp.nsimplify appears {claims['nsimplify_calls']} times in "
        f"this runner's own source -- MEASURED, not promised -- so no rational "
        f"tolerance can turn a positive witness minor such as 143/1600 into a "
        f"zero and destroy the refutation, or turn the landed killing minor "
        f"-27/125 into a zero and manufacture the positivity Block 209 proved "
        f"impossible",
        facts.nsimplify_calls == claims["nsimplify_calls"])
    checks.check(
        "G-3", f"and {claims['float_literals']} float literals appear in that "
        f"same source with EXACTLY {claims['float_calls']} float call sites, "
        f"both MEASURED by an AST walk rather than by a text search -- Block "
        f"209's strict form, which this block can afford because every number "
        f"it reports is a short exact rational and NOTHING here is ever "
        f"converted to a decimal",
        facts.float_literals == claims["float_literals"]
        and facts.float_calls == claims["float_calls"])
    return checks


# ---------------------------------------------------------------------------
# THE MEASURED REPORT
# ---------------------------------------------------------------------------
def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("MEASURED")
    print(f"  elapsed: {elapsed_ns // 1000000000}s")
    print(f"  origin/main {facts.main_head}")
    print(f"  authority {facts.authority}")
    print(f"  imposed {facts.imposed}, registered {facts.registered}, "
          f"adopted {facts.adopted}, gravity structures NOT SUPPLIED "
          f"{facts.unsupplied}, readings {facts.readings}, scoped headline "
          f"words {facts.scoped_words}")
    print(f"  check verdict carried: {CHECK_VERDICT}")
    variety = facts.variety
    print("  THE COMPATIBLE VARIETY")
    print(f"    {variety.equations} equations, generic ranks "
          f"{variety.generic_ranks}, per-face builder matches the landed one "
          f"{variety.builder_matches_landed}")
    print(f"    coefficient matrix constant {variety.coefficient_is_constant}, "
          f"zero columns {variety.zero_columns}, rank on the other 32 "
          f"{variety.pinned_rank}")
    print(f"    {len(variety.relations)} forced relations re-measured, equal "
          f"to the landed literals {variety.relations_match_landed}, even in "
          f"every shear {variety.relations_even}")
    for relation in variety.relations:
        print(f"      0 = {relation}")
    print(f"    volume equalities literal {variety.volume_equalities_literal}, "
          f"square factorizations {variety.square_factorizations}, divisions "
          f"{variety.divisions}")
    for tie in variety.ties:
        print(f"    tie: {tie}")
    print(f"    normal form kills all sixteen {variety.normal_form_kills_all}, "
          f"derived identity {DERIVED_IDENTITY_FORM} "
          f"{variety.derived_identity}, non-isotropic branches "
          f"{variety.non_isotropic_branches}")
    print(f"    sign cells {variety.sign_cells}, solvable "
          f"{variety.sign_cells_solvable}, off-variety ranks "
          f"{variety.off_variety_ranks}, mirror ranks {variety.mirror_ranks} "
          f"with first minor {variety.mirror_first_minor}")
    print(f"    gauge factor patterns {variety.gauge_factor_patterns}, orbits "
          f"{variety.gauge_orbits} of sizes {variety.gauge_orbit_sizes}, "
          f"invariants {variety.gauge_invariants}, sign-ratio classes "
          f"{variety.ratio_classes}, quadric irreducible "
          f"{variety.quadric_irreducible}")
    print(f"    uniform locus numerators {variety.uniform_numerators}; joint "
          f"solutions over v > 0, c real: {variety.uniform_solutions}")
    blocks = facts.blocks
    print("  THE DEGREE BLOCKS AND THE CLASSIFICATION")
    for orientation, ranks, free, parameter_free, cross in zip(
            blocks.classes, blocks.class_ranks, blocks.class_free_names,
            blocks.blocks_parameter_free, blocks.cross_degree_zero):
        print(f"    class (pi0, pi1) = {orientation}: ranks {ranks}, free "
              f"{free}, blocks parameter-free {parameter_free}, cross-degree "
              f"zero off duality {cross}")
    for form in DEGREE_BLOCK_FORMS:
        print(f"    {form}")
    print(f"    block formulas exact {blocks.block_formulas_exact}, corners "
          f"0 and 7 decouple {blocks.corners_decouple}, gauge congruence "
          f"exact {blocks.gauge_congruence_exact}")
    print(f"    signed triangle: charpoly factorizations "
          f"({blocks.charpoly_positive}, {blocks.charpoly_negative}), det at "
          f"pi = +1 is {blocks.determinant_positive}, det at pi = -1 is "
          f"{blocks.determinant_negative}, second leading minor "
          f"{blocks.second_minor}")
    print(f"    echo with Block 209's D3 kappa bounds, class-negated "
          f"{blocks.echo_class_negated} -- NOTED, NEVER INTERPRETED")
    print(f"    magnitude base parameters {blocks.magnitude_parameters}; grid "
          f"{blocks.grid_pd_total}/{blocks.grid_points} PD, per class "
          f"{blocks.grid_census}, formula matched at every point "
          f"{blocks.grid_matches_formula}, killer is a parameter-free block "
          f"determinant {blocks.killer_is_block_determinant}")
    witnesses = facts.witnesses
    print("  THE WITNESSES AND THE LANDED POINT")
    print(f"    W1 {W1_MODULI} all-plus: minors {witnesses.w1_minors}, "
          f"compatible {witnesses.w1_compatible}, nonuniform "
          f"{witnesses.w1_nonuniform}")
    print(f"    W2 {W2_MODULI} class (-1, -1): minors {witnesses.w2_minors}")
    print(f"    W3 {W3_MODULI} magnitudes {witnesses.w3_magnitudes} with "
          f"{witnesses.w3_flip_count} flip per offset: minors "
          f"{witnesses.w3_minors}")
    print(f"    duality region: interior minors "
          f"{witnesses.duality_interior_minors}")
    print(f"      a = 1 minors {witnesses.duality_a_bad_minors}")
    print(f"      b = 2 minors {witnesses.duality_b_bad_minors}")
    print(f"    landed reciprocal point: ranks {witnesses.landed_ranks}, free "
          f"{witnesses.landed_free_names}, deg-1 spectrum "
          f"{witnesses.landed_degree_one_spectrum}, deg-2 spectrum "
          f"{witnesses.landed_degree_two_spectrum}, negative blocks "
          f"{witnesses.landed_negative_blocks}")
    print(f"      killing minors {witnesses.landed_killing_minors}, matching "
          f"the general block formulas "
          f"{witnesses.landed_killing_matches_formula}; flat point is the "
          f"identity {witnesses.flat_point_is_identity}")
    print("  THE SIX FENCES, AND EACH IS A MEASURED CONSTANT")
    print(f"    F1 scout grade only {SCOUT_GRADE_ONLY}, finite exact linear "
          f"algebra {FINITE_EXACT_LINEAR_ALGEBRA}, physical content claimed "
          f"{PHYSICAL_CONTENT_CLAIMED}")
    print(f"    F2 echo noted only {ECHO_NOTED_ONLY}, interpreted "
          f"{ECHO_INTERPRETED_CLAIMED}, structural identification "
          f"{STRUCTURAL_IDENTIFICATION_CLAIMED}, licensed phrase "
          f"'{LICENSED_ECHO_PHRASE}'")
    print(f"    F3 sign products are the invariant "
          f"{SIGN_PRODUCTS_ARE_THE_INVARIANT}, signed-face invariance "
          f"{SIGNED_FACE_INVARIANCE_CLAIMED}, convention-tied: "
          f"{CONVENTION_TIED_OBJECTS}")
    print(f"    F4 Block 209 completed not corrected "
          f"{BLOCK209_COMPLETED_NOT_CORRECTED}, its scoping was exact "
          f"{BLOCK209_SCOPING_WAS_EXACT}, landed numbers corrected "
          f"{LANDED_NUMBERS_CORRECTED}")
    print(f"    F5 classification of ONE principle "
          f"{CLASSIFICATION_IS_OF_ONE_PRINCIPLE}, geometry selection "
          f"{GEOMETRY_SELECTION_CLAIMED}, classifies every positive matrix "
          f"{CLASSIFIES_EVERY_POSITIVE_MATRIX_CLAIMED}")
    print(f"    F6 instance scope {INSTANCE_SCOPE}; oblique faces open "
          f"{OBLIQUE_FACES_REMAIN_OPEN}; selection principle open "
          f"{SELECTION_PRINCIPLE_REMAINS_OPEN}")
    print("  READINGS, AND EACH IS A READING")
    for reading in READINGS:
        print(f"    {reading}")
    print(f"  nsimplify calls in this source: {facts.nsimplify_calls}; float "
          f"literals: {facts.float_literals}; float call sites: "
          f"{facts.float_calls} -- no decimal is ever formed")
    print("  NOT CLAIMED: NO GRAVITY. CLASSIFICATION IS ONE PRINCIPLE'S PD "
          "REGION AND NOT A SELECTION AMONG GEOMETRIES. ORIENTATION IS A SIGN "
          "PRODUCT AND NOT A PHYSICAL PARITY. WITNESS IS A MATRIX AND NOT AN "
          "OBSERVATION. THE BLOCK 209 DETERMINANT ECHO IS NOTED AND NEVER "
          "INTERPRETED. THE INDIVIDUAL SIGNS ARE CONVENTION-TIED AND THE "
          "PRODUCTS ARE THE INVARIANTS. BLOCK 209 IS COMPLETED AND NOT "
          "CORRECTED. NO LANDED NUMBER IS TOUCHED. NO GENERIC-PARAMETER "
          "THEOREM. NO CONTINUUM. THE READINGS ARE READINGS.")
    print()


N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE WORDS CLASSIFICATION, ORIENTATION AND WITNESS ARE EACH SCOPED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- THE PER-FACE SIX-FACE LITERAL GLUING SYSTEM (the 96 entry equations imposing that every coordinate-face restriction of a general symmetric 8 x 8 corner matrix, in Block 209's sub-corner order [offset, offset + i2, offset + i1, offset + i1 + i2] at order_swap = False and flip = False, equal the LANDED shear_hodge at that FACE's own volume and shear, with SIX INDEPENDENT per-face moduli and the builder verified equation for equation against Block 209's own), THE COMPATIBLE MODULI VARIETY (the common zero locus of Block 209's SIXTEEN landed forced relations on the nonsingular domain, its square variables X_f = c_f^2, its two ties v1 (1 - X0) = v0 and X1 = 1 - v0 v1, its polynomial normal form in (v1, X0) and its rational (t, u) chart), THE CORNER-SIGN GAUGE (the congruence D -> E D E with E = diag(e_0, ..., e_7), acting on the six face shear signs through (e2 e4, e1 e4, e1 e2; e3 e5, e3 e6, e5 e6), with its orbits and the two orientation invariants pi0 and pi1), THE DEGREE-BLOCK FORMULAS AND THE SIGNED TRIANGLE M(gamma; signs) = I - gamma S, THE THREE POSITIVITY WITNESSES W1, W2 AND W3 with all eight leading principal minors computed exactly, and BLOCK 105's LANDED 2D CELL FORM shear_hodge(c, v) READ THROUGH BLOCK 128's OWN IMPORT together with BLOCK 209's LANDED CONSTANTS READ THROUGH ITS OWN RUNNER AND NOT RETYPED, are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. WHAT IS ESTABLISHED IS NARROWER THAN THE WORDS CLASSIFICATION, ORIENTATION AND WITNESS, AND IS SAID IN THOSE WORDS. 'CLASSIFICATION' NAMES THE EXACT POSITIVE-DEFINITENESS REGION OF ONE GLUING PRINCIPLE'S COMPATIBLE MODULI VARIETY, AND NAMES NO UNIQUENESS THEOREM ABOUT NATURE, NO SELECTION AMONG GEOMETRIES AND NO CLASSIFICATION OF EVERY POSITIVE MATRIX -- at a fixed admissible moduli point the solution still carries FOUR duality coordinates restricted to an open bounded region. 'ORIENTATION' NAMES THE PRODUCT OF THE THREE SHEAR SIGNS AT ONE OFFSET, INSIDE ONE DECLARED SUB-CORNER AND WEDGE CONVENTION, AND NAMES NO SPACETIME ORIENTATION, NO CHIRALITY AND NO PHYSICAL PARITY. 'WITNESS' NAMES AN EXACT RATIONAL 8 x 8 CORNER MATRIX WITH STRICTLY POSITIVE LEADING PRINCIPAL MINORS, AND NAMES NO OBSERVATION, NO MEASUREMENT AND NO EXPERIMENT. 'CURVED' NAMES NONUNIFORM FACE MODULI OF ONE FINITE CELL AND NOT PHYSICAL CURVATURE. THE WORDS SPACETIME, CURVATURE AND EINSTEIN NAME NOTHING ESTABLISHED HERE. THE SIX SCOPE FENCES ARE MEASURED CONSTANTS AND NOT PROSE: all of it is SCOUT-GRADE finite exact linear algebra with no continuum, no dynamics and no gravity; the exact agreement between this block's determinant pair and Block 209's honest-lift kappa bounds is NOTED, NEVER INTERPRETED, with no carrier map constructed and no structural identification claimed; the per-offset sign PRODUCTS are the invariant content while every INDIVIDUAL face sign is convention-tied and moved by the corner-sign gauge; BLOCK 209 IS COMPLETED AND NOT CORRECTED, its 'on the checked branches' scoping having been exact and every landed number reproduced unchanged; 'CLASSIFICATION' is of ONE principle's PD region and selects nothing about nature; and the instance scope is ONE gluing principle, THREE coordinate planes at TWO offsets, ONE landed 2D target, ONE 32-point rational grid and THREE witnesses, with OBLIQUE FACES and the SHAPE-VERSUS-METRIC SELECTION PRINCIPLE both still OPEN. NO GENERIC-PARAMETER THEOREM IS SUPPLIED, NO CONTINUUM LIMIT IS SUPPLIED AND NO EQUATIONS OF MOTION ARE SUPPLIED. NINE GRAVITY STRUCTURES ARE ENUMERATED AS NOT SUPPLIED -- lapse function, shift vector, ADM phase space, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, Dirac observable, gauge orbit and its quotient. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\\nper_site: THE SYSTEM IS CONSTANT-COEFFICIENT AND THAT IS WHY ONE CLASSIFICATION CAN COVER EVERY MODULI POINT AT ONCE. The per-face builder reproduces Block 209's landed literal_system EQUATION FOR EQUATION at 96 equations on 36 unknowns, with generic ranks EXACTLY (32, 33) at independent per-face moduli. Its coefficient matrix carries NO moduli at all -- the moduli enter ONLY the right-hand side -- and EXACTLY FOUR of its columns are zero, namely the four Hodge-complementary duality pairings D07, D16, D25 and D34; its rank on the other thirty-two columns is EXACTLY 32. Solvability at a moduli point is therefore EXACTLY the vanishing of Block 209's sixteen landed cokernel relations, and the free parameters at every solvable point are ALWAYS exactly those four. The sixteen relations, re-measured here from the cokernel, EQUAL the landed SIX_FACE_RELATIONS literals, and every one of them has degree 0 or 2 in each of the six shears: THE VARIETY IS INVARIANT UNDER FLIPPING ANY INDIVIDUAL FACE SIGN. The four per-offset volume equalities appear LITERALLY among them, needing no division at all, and after volume equalization four more factor EXACTLY as v times a difference of shear squares. THE ONLY DIVISIONS IN THE WHOLE DERIVATION ARE THE TWO BY THE VOLUMES, both nonzero on the stated domain.\\nper_mode: THE VARIETY IS EXACTLY THE PER-OFFSET-ISOTROPIC FAMILY AND NO NON-ISOTROPIC BRANCH EXISTS. After the volume and square equalizations the eight reciprocal cross-offset couplings collapse to EXACTLY TWO ties -- tie A, v1 (1 - g0^2) = v0, and tie B, g1^2 = 1 - v0 v1 -- whose exact polynomial consequence is v0^2 = (1 - g0^2)(1 - g1^2) with companion v1^2 = (1 - g1^2)/(1 - g0^2). THE TWO OFFSETS ARE GENUINELY ASYMMETRIC: 1 - g0^2 is the volume RATIO and 1 - g1^2 the volume PRODUCT, which is the anchoring convention's footprint. CONVERSELY the polynomial normal form v_f0 = v1 (1 - X0), v_f1 = v1, c_f0^2 = X0, c_f1^2 = 1 - v1^2 (1 - X0) kills all sixteen relations IDENTICALLY, so the compatible set on the nonsingular domain is exactly this two-parameter magnitude family and NOTHING ELSE. All 64 shear-sign cells are solvable at ranks (32, 32) while a point off the variety is insolvable at (32, 33); the negative-volume mirror is compatible but dies at the FIRST leading minor D00 = v0 < 0. The corner-sign gauge realizes 16 factor patterns and cuts the 64 cells into EXACTLY FOUR ORBITS OF SIXTEEN, indexed by the two orientation invariants pi0 and pi1, while the Zariski closure has 16 components, one per sign-ratio class, the defining quadric being irreducible. AND BLOCK 209's UNIFORM RESULT STILL STANDS: at v0 = v1 and g0 = g1 the two ties become EXACTLY the landed numerators c^2 v and c^2 + v^2 - 1, whose joint solution over v > 0 with c real is the SINGLE point (c, v) = (0, 1).\\nper_block: THE DEGREE BLOCKS ARE PARAMETER-FREE AT SYMBOLIC MODULI IN EVERY SIGN CLASS, AND THE ORIENTATION SPLIT IS EXACT. One symbolic solve per gauge class over QQ(t, u) is CONSISTENT at ranks (32, 32) with free parameters exactly D07, D16, D25 and D34, every other cross-degree entry exactly zero, and NONE of the four appearing in any degree-diagonal block -- so Block 209's principal-submatrix argument holds at SYMBOLIC moduli and not only at one exhibited point. The blocks are deg-0 = [v0]; deg-1 = v1 M1 on corners (1, 2, 4) with M1 = [[1, -c_xy0, -c_ty0], [-c_xy0, 1, -c_tx0], [-c_ty0, -c_tx0, 1]]; deg-2 = (1/v0) M2 on corners (3, 5, 6) with M2 = [[1, -c_tx1, -c_ty1], [-c_tx1, 1, -c_xy1], [-c_ty1, -c_xy1, 1]]; and deg-3 = [1/v1]. Corners 0 and 7 decouple from all six middle corners, so D is the orthogonal sum of the {0, 7} pair block and the 6 x 6 block with antidiagonal duality coupling, and the corner-sign gauge congruence E D E is verified in the FIELD rather than on a sample. The signed triangle has eigenvalues (1 - 2g, 1 + g, 1 + g) at pi = +1 and (1 + 2g, 1 - g, 1 - g) at pi = -1, determinants (1 + g)^2 (1 - 2g) and (1 - g)^2 (1 + 2g), and second leading minor 1 - g^2 positive on the domain, so Sylvester reduces positivity to the determinant. THAT DETERMINANT PAIR IS AN EXACT ECHO OF BLOCK 209's D3 ISOTROPIC kappa BOUNDS WITH THE CLASS LABEL NEGATED -- the literal blocks carry MINUS the shear pattern, and entrywise negation flips the triangle product. IT IS NOTED HERE AND INTERPRETED NOWHERE.\\nlattice_wide: THE CLASSIFICATION, CLOSED, PER-OFFSET INDEPENDENT, AND VERIFIED POINTWISE. D is positive definite for SOME choice of the four duality parameters at a compatible point IF AND ONLY IF gamma0 < 1/2 when pi0 = +1 and gamma0 < 1 when pi0 = -1, AND, independently, the same for (gamma1, pi1). Necessity is the parameter-free principal blocks; sufficiency is the direct sum at zero duality coupling. The magnitude base has TWO parameters, so EVERY gauge class carries a TWO-PARAMETER CURVED POSITIVE DEFINITE FAMILY: class (+1, +1) on [0, 1/2) x [0, 1/2), class (+1, -1) on [0, 1/2) x [0, 1), class (-1, +1) on [0, 1) x [0, 1/2), and class (-1, -1) on the WHOLE magnitude base. Thirty-two exact solves -- eight rational magnitude points on each of the four classes, with the full 8 x 8 leading principal minors at the degree-diagonal representative -- agree with the region formula at EVERY point, census 3/8, 3/8, 3/8 and 8/8 for a total of 17 of 32; and at every non-PD point the parameter-free degree-1 or degree-2 DETERMINANT is <= 0, killing all duality choices at once. THE NATURAL FLAT-ONLY EXTENSION OF BLOCK 209's RIGIDITY STATEMENT IS THEREFORE REFUTED OVER THE NONUNIFORM BRANCHES.\\nper_scope: THE WITNESSES ARE EXPLICIT AND THE LANDED POINT IS REPRODUCED UNCHANGED. W1 -- magnitudes 1/4 on all six faces, v0 = 15/16, v1 = 1, all-plus -- is compatible, NONUNIFORM, and has leading principal minors (15/16, 15/16, 225/256, 15/16, 25/32, 25/32, 25/36, 25/36), ALL STRICTLY POSITIVE: a curved literal six-face cell that IS positive definite. W2 -- magnitudes 3/4 on class (-1, -1), v0 = 7/16, v1 = 1 -- is positive definite far beyond the all-plus kill point 1/2. W3 CARRIES THE LANDED MAGNITUDES (3/5, 4/5) WITH EXACTLY ONE SHEAR SIGN FLIPPED PER OFFSET and is positive definite, with minors (12/25, 9/25, 108/625, 9/25, 297/2000, 891/8000, 429/6400, 143/1600): THE KILLER AT BLOCK 209's EXHIBITED POINT WAS THE SIGN PATTERN AND NOT THE CURVATURE. The duality region is OPEN and four-dimensional but BOUNDED. Block 209's own all-plus reciprocal point is reproduced at ranks (32, 32) with free parameters D07, D16, D25 and D34, degree-1 spectrum (-3/20, 6/5, 6/5) and degree-2 spectrum (-5/4, 15/4, 15/4) EQUAL to its landed literals, still INDEFINITE, killed by the parameter-free determinants -27/125 and -1125/64 that the general block formulas predict; and the flat point returns the 8 x 8 identity. WHAT REMAINS OPEN: oblique and non-coordinate faces; whether any principle inside this framework selects the shape rule over the honest metric geometry or the reverse; every convention and every moduli point not run; and no energy, no mass, no measurement postulate, no Born rule, no dynamics and no gravity is supplied by any line of this block.\\nRESULT: THE SIX-FACE-COMPATIBLE MODULI VARIETY ON THE NONSINGULAR DOMAIN IS EXACTLY THE PER-OFFSET-ISOTROPIC FAMILY TIED BY v1 (1 - g0^2) = v0 AND g1^2 = 1 - v0 v1, WITH NO NON-ISOTROPIC BRANCH, 64 SIGN CELLS IN 4 GAUGE CLASSES AND THE UNIFORM LOCUS STILL FORCED TO THE FLAT CELL; THE FOUR DUALITY PARAMETERS ARE ABSENT FROM EVERY DEGREE BLOCK AT SYMBOLIC MODULI IN EVERY CLASS; AND D IS PD-SOLVABLE IFF gamma0 < 1/2 AT pi0 = +1 (ANY gamma0 < 1 AT pi0 = -1) AND INDEPENDENTLY THE SAME FOR (gamma1, pi1), SO EVERY GAUGE CLASS CARRIES A TWO-PARAMETER CURVED POSITIVE DEFINITE FAMILY AND THE NATURAL FLAT-ONLY EXTENSION IS REFUTED. THESE ARE SCOUT-GRADE FINITE EXACT LINEAR-ALGEBRA FACTS ABOUT ONE CELL FORM, NOT A SPACETIME, NOT A DYNAMICS AND NOT A GRAVITY. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 104, 105, 106, 107, 128, 170, 171 and 181-210 STAND EXACTLY AS LANDED. BLOCK 209 IS COMPLETED AND NOT CORRECTED: its rigidity statement was written ON THE CHECKED BRANCHES with positivity explicitly NOT classified over the nonuniform six-face-compatible branches, that scoping held EXACTLY, this block closes the branch it named open, and its uniform-locus flat point, its reciprocal point, its two degree spectra and its two orientation determinants are all reproduced here unchanged. BLOCK 105 IS NOT CORRECTED: its shear_hodge(c, v) is read through Block 128's own import and is the target every face equation is written against. THIS BLOCK's OWN DEFECTS ARE DISCLOSED: ONE gluing principle, THREE coordinate planes at TWO offsets, ONE landed 2D target, ONE 32-point rational grid and THREE witnesses -- not a parameter space and not a limit; the classification is of PD-SOLVABILITY OF THE MODULI and not of every individual positive matrix; the determinant echo with Block 209's honest lift is NOTED and NEVER INTERPRETED, with no carrier map constructed; the individual face signs are CONVENTION-TIED while the per-offset PRODUCTS are the invariants; and oblique faces and the shape-versus-metric selection principle remain OPEN. ONE ITEM IS FOLDED FROM THE ADVERSARIAL RECORD AS CONTENT AND NOT AS ERRATA, correction 111: the supervising record's announced flat-only extension -- 'literal gluing plus positivity admits exactly the flat cell' over the nonuniform branches, never landed and declined by Block 209 -- is REFUTED by witness W1, and the refutation is carried as this block's headline rather than smoothed. PROVENANCE: the R1 classification arc of this lane, at TOTAL PASS=43 FAIL=0 across six families, with an independent exact reconstruction recorded at TOTAL PASS=21 FAIL=0 confirming C1 and C2 in full and qualifying C6, whose qualifications are the six fences above.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero."


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
