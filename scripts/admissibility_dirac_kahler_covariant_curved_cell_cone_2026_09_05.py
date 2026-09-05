#!/usr/bin/env python3
"""BLOCK 216 -- THE COVARIANT CURVED CELL AND ITS CONE.

Block 215 found that at exactly 16 of Block 211's 64 face-sign cells -- the
cells whose two-offset face-sign products (P_tx, P_ty, P_xy) carry the lane's
star pattern (+, -, +) up to a global sign -- a curved cell is strictly
S3-covariant with both shears alive, and the covariant line there is Block
214's plane D16 = D34 = -D25 (the star line).  Block 214 proved that the cone
is the union of the two Hodge readings' cones exactly on that plane, at
all-plus witnesses only.  Block 213 found 16 coincidence-curve cells (8 of them
positive, rule A: S1 = -E S0 E, g0 = g1/(1 + pi0 g1)) on which the graded cone
is one metric's cone.  This runner computes EXACTLY, at those 16 cells:

  (a) the union locus, both halves: sufficiency by the shear-free M_oo lemma
      (measured at SYMBOLIC face signs, so it is a lemma at every cell) and
      the block identity; necessity by the coefficient ideal of det M - det B^2
      at one positive-definite witness per gauge class among the 16, at the
      all-plus control and at the flat cell, and over QQ(sqrt 6) at the two
      rule-A curve witnesses;
  (b) the intersection with Block 213's coincidence cells by the face-sign
      masks, with the two runners' 64-cell indexings gated against each other
      and the census reproduced on Block 213's own machinery;
  (c) the covariant witness: at every common positive cell a positive-definite
      point on the rule-A curve over QQ(sqrt 6) at which the cell is strictly
      S3-covariant with both shears alive, the parameters on the star line keep
      it so, and the graded cone is one metric's cone;
  (d) the pencil branches with the parameters on the covariant line, the D07
      congruence at the 16 cells and the D07 rescaling re-measured there;
  (e) what strict S3 covariance imposes on Block 213's symbol identity, and
      what only the full group would impose.

  Nothing registered or adopted; no cell, subgroup, assembly, reading or
  parameter value selected; 'one metric's cone' names Block 213's exact
  statement and nothing physical; the covariance antecedent stays a reading.

Gate families: A authority, B banner/fences, C construction fidelity, D the
union locus, E the intersection, F the covariant witness, G the branches and
the symbol, H scope, I note and hygiene.  Every measurement is taken once
before any mutation flag is read; exact arithmetic only -- no float, no
nsimplify.  Scout-grade finite exact linear algebra on one cell form, not a
spacetime and not a dynamics.
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

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY: Block 215 (the
# lift, the star, the locus machinery) and through it Blocks 214, 213, 211, 209.
try:
    import admissibility_dirac_kahler_duality_covariance_locus_2026_09_05 as b215
    B215_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b215 = None
    B215_IMPORT_LANDED = False
b214 = b215.b214 if b215 is not None else None
b213 = b215.b213 if b215 is not None else None
b211 = b215.b211 if b215 is not None else None
b209 = b215.b209 if b215 is not None else None
MACHINERY_IMPORT_LANDED = bool(B215_IMPORT_LANDED and b215 is not None and b215.MACHINERY_IMPORT_LANDED
                               and b214 is not None and b213 is not None and b211 is not None and b209 is not None)
# THE STACK PARENT'S TWO ARTIFACTS.  Block 215 is the commit this block is cut
# from AND its scientific parent; its note and runner exist at PARENT_COMMIT
# and NEITHER exists at STALE_PARENT_COMMIT, the Block 214 tip.
PARENT_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
PARENT_RUNNER = "scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py"
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "4131aab00624434be10dbd798aea193ecd9cfc37",
    "99715185762fa254ec7a26d752b366f7e6e0fb98",
)
FINAL_NOTE_NAME = "ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md"
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS (the cache parser AST-reads it).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_duality_covariance_locus_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py",
    "scripts/admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27.py",
    "scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, re-resolved live against the REMOTE origin/main.
CURRENT_MAIN = "4407b6a0e0a38074d9b38710da6ed3a83c9e5e56"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = "origin/physics-loop/toe-axiom-closure-block215-duality-covariance-locus-20260905"
PARENT_COMMIT = "d386a1be41ab8a26e9a4a2e5258f841bf1dbc2cc"
# The Block 214 tip: a real ancestor of HEAD carrying NEITHER Block 215 artifact.
STALE_PARENT_COMMIT = "1dc2ae2557a22ef188f344665bc00edc2593d113"
# A real but superseded authority head, carried forward from Block 214's record.
STALE_MAIN = "e249016f759f224d9b429932cd0d1db4d452dc1a"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_covariance_inherited",
    "claim_assembly_decided",
    "claim_cell_selected",
    "claim_metric_supplied",
    "break_indexing_agreement",
    "break_star_pattern_masks",
    "break_coincidence_census",
    "break_witness_solves",
    "break_m_oo_lemma",
    "break_union_necessity",
    "claim_union_from_identity_alone",
    "break_intersection",
    "break_positive_subset",
    "break_covariant_witness",
    "claim_covariant_cell_empty",
    "break_one_metric_cone",
    "break_branch_table",
    "break_d07_rescale",
    "break_d07_congruence",
    "break_symbol_invariance",
    "break_scout_grade_fence",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_covariance_inherited": "B", "claim_assembly_decided": "B",
    "claim_cell_selected": "B", "claim_metric_supplied": "B",
    "break_indexing_agreement": "C", "break_star_pattern_masks": "C",
    "break_coincidence_census": "C", "break_witness_solves": "C",
    "break_m_oo_lemma": "D", "break_union_necessity": "D", "claim_union_from_identity_alone": "D",
    "break_intersection": "E", "break_positive_subset": "E",
    "break_covariant_witness": "F", "claim_covariant_cell_empty": "F", "break_one_metric_cone": "F",
    "break_branch_table": "G", "break_d07_rescale": "G", "break_d07_congruence": "G",
    "break_symbol_invariance": "G",
    "break_scout_grade_fence": "H", "break_instance_scope": "H",
    "drop_n5_fence": "I", "break_float_absence": "I",
}
MUTATED_FAMILIES = "ABCDEFGHI"


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
def git_maybe(*args: str) -> str:
    result = subprocess.run(
        ("git",) + args, cwd=ROOT, text=True, capture_output=True,
        check=False, timeout=AUDIT_TIMEOUT_SEC)
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, capture_output=True,
        timeout=AUDIT_TIMEOUT_SEC).returncode == 0


def is_hash(value: str) -> bool:
    return len(value) == 40 and all(ch in "0123456789abcdef" for ch in value)


@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_is_ancestor: bool
    parent_artifact_blobs: bool
    stale_is_real_ancestor: bool
    stale_carries_neither_artifact: bool
    machinery_import_landed: bool
    inputs_readable: int


def authority_certificate(main_head: str) -> AuthorityCertificate:
    fixed_authority = bool(
        AUDIT_TIMEOUT_SEC == 600
        and main_head == CURRENT_MAIN
        and git_maybe("rev-parse", f"origin/main:{AXIOM_PATH}") == CURRENT_AXIOM_BLOB
        and git_maybe("rev-parse", f"origin/main:{REGISTRY_PATH}") == CURRENT_REGISTRY_BLOB
        and git_maybe("hash-object", AXIOM_PATH) == WORKTREE_AXIOM_BLOB
        and git_maybe("hash-object", REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB)
    worktree_blobs = tuple(git_maybe("hash-object", p) for p in PARENT_ARTIFACTS)
    committed_blobs = tuple(git_maybe("rev-parse", f"{PARENT_COMMIT}:{p}") for p in PARENT_ARTIFACTS)
    stale_blobs = tuple(git_maybe("rev-parse", f"{STALE_PARENT_COMMIT}:{p}") for p in PARENT_ARTIFACTS)
    readable = sum(1 for p in AUDIT_INPUT_PATHS if p != SELF_NOTE_INPUT and (ROOT / p).is_file())
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT),
        is_ancestor(PARENT_COMMIT, "HEAD"),
        bool(all(is_hash(v) for v in committed_blobs)
             and committed_blobs == worktree_blobs == PARENT_ARTIFACT_BLOBS),
        is_ancestor(STALE_PARENT_COMMIT, "HEAD"),
        not any(is_hash(v) for v in stale_blobs),
        MACHINERY_IMPORT_LANDED,
        readable)


# ---------------------------------------------------------------------------
# B. the imposed objects and the NOT-CLAIMED keys, as measured literals
# ---------------------------------------------------------------------------
IMPOSED_OBJECTS = (
    "the cube complex, corners, degree indices and wedge signature (Block 209; Block 213's eta/lane_rules/raising_rules)",
    "Block 211's six-face-compatible cell-form family with its ties, 64 face-sign cells, four gauge classes and four free duality parameters",
    "Block 213's coincidence census (16 curve cells, rule A / rule B, the locus witnesses L+- and L-+ over QQ(sqrt 6)) and its symbol identity",
    "Block 214's principal part M = H0 D + D^T H0, its plane D16 = D34 = -D25 and the union-locus statement at all-plus witnesses",
    "Block 215's corner action of the 24 proper rotations, the star, the twisted/strict loci and the 16 star-pattern cells (rule G-5)",
    "Block 105's two assemblies (onsite, overlap) through Block 213/214's rules -- the onsite one measured here, neither decided",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
COVARIANCE_INHERITED_CLAIMED = False
CELL_SELECTED_CLAIMED = False
SUBGROUP_SELECTED_CLAIMED = False
ASSEMBLY_DECIDED_CLAIMED = False
METRIC_SUPPLIED_CLAIMED = False
PARAMETER_VALUE_SELECTED_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("COVARIANCE", "CONE", "CELL", "LOCUS", "METRIC")
AXIOM_COVARIANCE_CLAUSE = ("There is one fixed nearest-neighbor admissibility rule, covariant under lattice\n"
                           "translations and proper cubic rotations.")
READINGS = (
    "R1 the cell form inherits the Admissibility axiom's proper-cubic-rotation covariance (the antecedent; not established, not asserted)",
    "R2 the 16 covariant cells are preferred, physical or selected (not established: no cell is selected; the census counts them)",
    "R3 'one metric's cone' is a metric of anything physical (not established: it names Block 213's exact statement det B = c (k^T G1 k)^2)",
    "R4 the coincidence of the star pattern with the coincidence-cell rule is a dynamical or geometric principle (not established: a sign identity P_f = +-E_k)",
    "R5 the covariant witness is a vacuum, a background or a spacetime (not established: a positive-definite point on one cell form)",
    "R6 the S3-invariance of the symbol is a dispersion law or a light cone (not established: a polynomial identity in kappa on one cell)",
)
CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"

# the parameters, the corners, the moduli, the directions
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = b215.PARAMETER_SYMBOLS
A07, B16, C25, D34 = PARAMETER_SYMBOLS
G0, G1, V0, V1 = b215.MODULI
MODULI = (G0, G1, V0, V1)
KT, KX, KY = b215.KAPPA
KAPPA = (KT, KX, KY)
LAM_LINE = sp.Symbol("lam_line")          # the star-line multiple (D16, D25, D34) = (lam, -lam, lam)
CORNERS = b209.CORNERS
FACE_ORDER = b211.GAUGE_FACE_ORDER        # (tx0, ty0, xy0, tx1, ty1, xy1)
SIGNATURE = sp.diag(1, -1, 1)             # Block 213's E on (t, x, y)
STAR_PATTERN = ((1, -1, 1), (-1, 1, -1))  # (P_tx, P_ty, P_xy) up to a global sign (Block 215 G-5)
QUARTER = sp.Rational(1, 4)
HALF = sp.Rational(1, 2)
GAUGE_CLASSES = ((1, 1), (1, -1), (-1, 1), (-1, -1))

# ---------------------------------------------------------------------------
# exact helpers -- no float, no tolerance and NO nsimplify anywhere
# ---------------------------------------------------------------------------
NSIMPLIFY_TOKEN = "sp." + "nsimplify("


def nsimplify_occurrences() -> int:
    return Path(__file__).read_text(encoding="utf-8").count(NSIMPLIFY_TOKEN)


def float_literal_occurrences() -> int:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Constant) and type(node.value) is float)


def float_call_sites() -> int:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    return sum(1 for node in ast.walk(tree)
               if isinstance(node, ast.Call)
               and isinstance(node.func, ast.Name) and node.func.id == "float")


def residual_count(matrix) -> int:
    return b213.residual_count(matrix)


def is_zero_alg(expression) -> bool:
    return sp.expand(sp.radsimp(expression)) == 0


def sign_dict(values: tuple) -> dict:
    return dict(zip(FACE_ORDER, (sp.Integer(v) for v in values)))


def cell_mask(values: tuple) -> int:
    """The enumeration index of itertools.product((1, -1), repeat=6) over
    FACE_ORDER: bit (5 - k) set when face k carries -1 -- the checker's masks."""
    return sum(2 ** (5 - k) for k, v in enumerate(values) if v == -1)


def face_products(values: tuple) -> tuple:
    return (values[0] * values[3], values[1] * values[4], values[2] * values[5])


def gauge_class(values: tuple) -> tuple:
    return (values[0] * values[1] * values[2], values[3] * values[4] * values[5])


def formal(values: tuple, moduli: tuple, params: tuple) -> sp.Matrix:
    """Block 214's formal_cell at a face-sign cell: (g0, g1, v0, v1) with the
    four parameter entries on (0,7), (1,6), (2,5), (3,4)."""
    g0, g1, v0, v1 = moduli
    return b214.formal_cell(sign_dict(values), g0, g1, v0, v1, params)


def rotate_kappa(expression, rotation: sp.Matrix):
    return sp.expand(sp.radsimp(expression.subs(
        {k: sum(rotation[i, j] * KAPPA[j] for j in range(3)) for i, k in enumerate(KAPPA)}, simultaneous=True)))


# ---------------------------------------------------------------------------
# C/E. THE CENSUS: the 64 cells under both runners' rules, and the masks
# ---------------------------------------------------------------------------
def measure_census() -> dict:
    """The 64 face-sign cells indexed by Block 211's GAUGE_FACE_ORDER: Block
    215's star-pattern rule (G-5) and Block 213's coincidence rules (rule A:
    S1 = -E S0 E, rule B: S1 = +E S0 E, read off the degree blocks of Block
    213's own formal_family) and its Groebner census, cell by cell; then the
    intersection by masks."""
    facts: dict = {"indexing_agrees": tuple(b213.FACES) == tuple(FACE_ORDER),
                   "face_order": tuple(FACE_ORDER)}
    g0s, g1s, v0s, v1s = sp.symbols("g0 g1 v0 v1", positive=True)
    cells: dict = {}
    census: dict = {}
    for values in itertools.product((1, -1), repeat=6):
        signs = sign_dict(values)
        fam = b213.formal_family(signs, g0s, g1s, v0s, v1s)
        g1_f, g2_f, _, d1_f, d2_f, _ = b213.metric_candidates(fam)
        m1 = (d1_f / v1s).applyfunc(sp.cancel)
        m2 = (d2_f * v0s).applyfunc(sp.cancel)
        s0 = ((sp.eye(3) - m1) / g0s).applyfunc(sp.cancel)
        s1 = ((sp.eye(3) - m2) / g1s).applyfunc(sp.cancel)
        rule_a = residual_count(s1 + SIGNATURE * s0 * SIGNATURE) == 0
        rule_b = residual_count(s1 - SIGNATURE * s0 * SIGNATURE) == 0
        basis = sp.groebner(b213.proportionality_minors(g1_f, g2_f), g0s, g1s, order="lex")
        elements = [str(sp.factor(g)) for g in basis.exprs]
        key = "(" + ", ".join(elements) + (",)" if len(elements) == 1 else ")")
        entry = census.setdefault(key, [0, set()])
        entry[0] += 1
        entry[1].add(gauge_class(values))
        cells[values] = {
            "mask": cell_mask(values), "P": face_products(values), "class": gauge_class(values),
            "star": face_products(values) in STAR_PATTERN, "rule_a": rule_a, "rule_b": rule_b,
            "curve": key != "(g0, g1)", "groebner": key,
        }
    facts["cells"] = cells
    facts["census"] = tuple(sorted((key, count, tuple(sorted(cls))) for key, (count, cls) in census.items()))
    facts["census_matches_block213"] = facts["census"] == tuple(sorted(b213.COINCIDENCE_CENSUS))
    star = tuple(sorted(c["mask"] for c in cells.values() if c["star"]))
    rule_a = tuple(sorted(c["mask"] for c in cells.values() if c["rule_a"]))
    rule_b = tuple(sorted(c["mask"] for c in cells.values() if c["rule_b"]))
    curve = tuple(sorted(c["mask"] for c in cells.values() if c["curve"]))
    facts["star_masks"], facts["rule_a_masks"], facts["rule_b_masks"], facts["curve_masks"] = star, rule_a, rule_b, curve
    facts["curve_is_rule_a_or_b"] = set(curve) == set(rule_a) | set(rule_b) and not (set(rule_a) & set(rule_b))
    facts["intersection_masks"] = tuple(sorted(set(star) & set(curve)))
    facts["intersection_count"] = len(facts["intersection_masks"])
    facts["positive_subset_masks"] = tuple(sorted(set(star) & set(rule_a)))
    facts["positive_subset_count"] = len(facts["positive_subset_masks"])
    facts["star_equals_curve"] = set(star) == set(curve)
    # THE SIGN IDENTITY behind the coincidence of the two rules: rule A iff the
    # two-offset products are the star's pair signs (+, -, +) themselves, rule B
    # iff their global negative; and P_f = -E_i E_j = E_k for f = {i, j}, k its complement.
    facts["rule_a_iff_star_pattern_plus"] = all(c["rule_a"] == (c["P"] == STAR_PATTERN[0]) for c in cells.values())
    facts["rule_b_iff_star_pattern_minus"] = all(c["rule_b"] == (c["P"] == STAR_PATTERN[1]) for c in cells.values())
    e_t, e_x, e_y = SIGNATURE[0, 0], SIGNATURE[1, 1], SIGNATURE[2, 2]
    facts["star_pattern_is_minus_e_i_e_j"] = (-e_t * e_x, -e_t * e_y, -e_x * e_y) == STAR_PATTERN[0] == (e_y, e_x, e_t)
    facts["star_pair_signs_block215"] = tuple(b215.STAR_PAIR_SIGNS[1:])   # (y -> tx, x -> ty, t -> xy)
    facts["star_per_class"] = {key: tuple(sorted(c["mask"] for c in cells.values() if c["star"] and c["class"] == key))
                               for key in GAUGE_CLASSES}
    facts["rule_a_classes"] = tuple(sorted(set(c["class"] for c in cells.values() if c["rule_a"])))
    facts["rule_b_classes"] = tuple(sorted(set(c["class"] for c in cells.values() if c["rule_b"])))
    # the distance (face flips) from every star cell to the nearest rule-A cell
    rule_a_cells = [v for v, c in cells.items() if c["rule_a"]]
    facts["star_to_rule_a_distance"] = tuple(sorted(
        (c["mask"], min(sum(1 for a, b in zip(v, w) if a != b) for w in rule_a_cells))
        for v, c in cells.items() if c["star"]))
    return facts
