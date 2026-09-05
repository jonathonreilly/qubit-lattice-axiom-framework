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


# ---------------------------------------------------------------------------
# the witnesses: one rational positive-definite point (Block 214's W1 moduli,
# positive definite in every sign cell) and Block 213's two curve points
# ---------------------------------------------------------------------------
W1_MODULI = b211.W1_MODULI                                   # (v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4)
FLAT_MODULI = (sp.Integer(1), sp.Integer(0), sp.Integer(1), sp.Integer(0))
ALL_PLUS_CELL = (1,) * 6


def curve_moduli(pi0: int) -> tuple:
    """Block 213's rule-A curve point g0 = g1/(1 + pi0 g1) with the family's
    ties, over QQ(sqrt 6): L+-'s moduli for pi0 = +1, L-+'s for pi0 = -1."""
    name = "L+-" if pi0 == 1 else "L-+"
    return b213.locus_witness_table()[name][0]


def moduli_as_g(moduli: tuple) -> tuple:
    v0, g0, v1, g1 = moduli
    return (g0, g1, v0, v1)


def star_cells(census: dict) -> tuple:
    return tuple(sorted((v for v, c in census["cells"].items() if c["star"]), key=lambda v: census["cells"][v]["mask"]))


def class_representatives(census: dict) -> dict:
    out = {}
    for values in star_cells(census):
        out.setdefault(census["cells"][values]["class"], values)
    return out


# ---------------------------------------------------------------------------
# C. THE COVARIANCE AT THE 16 CELLS, re-measured on Block 215's machinery
# ---------------------------------------------------------------------------
def measure_covariance(group: dict, census: dict) -> dict:
    """At every star-pattern cell (and the all-plus control) at symbolic
    moduli: the shear-alive twisted-O line under two generators, and the
    strict (E = 1) locus under every S3_body -- Block 215's G-3/G-4/G-5."""
    lifts, table, orders = group["lifts"], group["table"], group["orders"]
    g3 = orders.index(3)
    g4 = next(i for i in range(24) if orders[i] == 4
              and len(b215.closure(table, frozenset((g3, i)), group["identity_index"])) == 24)
    star_line = b215.canonical_subspace([[0, 1, 0, -1], [0, 0, 1, 1]], PARAMETER_SYMBOLS)
    facts: dict = {"generators_generate_o": len(b215.closure(table, frozenset((g3, g4)), group["identity_index"])) == 24}
    twisted, strict = {}, {}
    for values in star_cells(census) + (ALL_PLUS_CELL,):
        cell = formal(values, MODULI, PARAMETER_SYMBOLS)
        per = tuple(b215.irredundant([b215.constraints(cell, lifts[g], e, PARAMETER_SYMBOLS) for e in b215.sign_vectors()])
                    for g in (g3, g4))
        locus = b215.intersect(per[0], per[1], PARAMETER_SYMBOLS)
        alive = tuple(v for f, v in locus if not f)
        twisted[values] = (len(alive), alive == (star_line,), b215.describe(tuple((frozenset(), v) for v in alive), PARAMETER_SYMBOLS))
        strict_per = tuple(b215.irredundant([b215.constraints(cell, lifts[g], (1,) * 8, PARAMETER_SYMBOLS)]) for g in range(24))
        members = []
        for member in group["classes"]["S3_body"]:
            alive_s3 = tuple(v for f, v in b215.subgroup_locus(strict_per, member, PARAMETER_SYMBOLS) if not f)
            members.append((tuple(sorted(member)), alive_s3 == (star_line,), len(alive_s3)))
        strict[values] = tuple(members)
    facts["twisted"] = twisted
    facts["strict_s3"] = strict
    star = star_cells(census)
    facts["twisted_line_is_star_line_at_every_star_cell"] = all(twisted[v][0] == 1 and twisted[v][1] for v in star)
    facts["all_plus_twisted_line"] = twisted[ALL_PLUS_CELL][2]
    facts["strict_s3_alive_count_per_star_cell"] = tuple(sorted(set(sum(1 for _, ok, _ in strict[v] if ok) for v in star)))
    facts["strict_s3_star_line_at_every_star_cell"] = all(any(ok for _, ok, _ in strict[v]) for v in star)
    facts["strict_s3_alive_at_all_plus"] = any(n > 0 for _, _, n in strict[ALL_PLUS_CELL])
    facts["strict_s3_member_per_star_cell"] = {census["cells"][v]["mask"]: next(m for m, ok, _ in strict[v] if ok) for v in star}
    facts["star_line"] = star_line
    facts["generator_indices"] = (g3, g4)
    return facts


# ---------------------------------------------------------------------------
# D. THE UNION LOCUS AT THE CELLS: the M_oo lemma, the block identity, the
# necessity half by the coefficient ideal at every witness
# ---------------------------------------------------------------------------
def union_locus(cell: sp.Matrix, gaussian: bool) -> tuple:
    """(radical generators of the coefficient ideal of det M - det B^2 in
    (D16, D25, D34); det M is D07-free; det M on the plane equals det B^2 with
    the plane multiple symbolic) -- Block 214's F-4 machinery at one cell."""
    params = (B16, C25, D34)
    even, odd = b213.even_odd(3)
    h0, m, _ = b214.principal_part(cell, "onsite")
    det_m = sp.expand(b214.ff_det(m, params + KAPPA, algebraic=gaussian))
    det_b = sp.expand(sp.radsimp(m.extract(even, odd).det(method="berkowitz")))
    difference = sp.expand(sp.radsimp(det_m - det_b ** 2))
    if gaussian:
        r = sp.Symbol("r")
        coefficients = sp.Poly(difference.subs(sp.sqrt(6), r), *KAPPA).coeffs() + [r ** 2 - 6]
        basis = sp.groebner(coefficients, *params, r, order="lex")
        generators = b214.reduced_generators(basis.exprs, params, r)
    else:
        generators = b214.radical_generators(b214.coefficient_ideal(difference, KAPPA, params), params)
    on_plane = {B16: LAM_LINE, C25: -LAM_LINE, D34: LAM_LINE}
    det_m_plane = sp.expand(b214.ff_det(m.subs(on_plane), (LAM_LINE,) + KAPPA, algebraic=gaussian))
    det_b_plane = sp.expand(sp.radsimp(det_b.subs(on_plane)))
    sufficiency = is_zero_alg(det_m_plane - det_b_plane ** 2)
    return generators, sufficiency, det_m_plane


def measure_union(census: dict) -> dict:
    facts: dict = {}
    even, odd = b213.even_odd(3)
    # THE M_oo LEMMA AT SYMBOLIC FACE SIGNS: the odd-odd block of the onsite
    # principal part carries no shear, no volume and no sign -- only the three
    # parameter combinations of Block 214 -- so its vanishing locus is the
    # star line at EVERY cell.
    sign_symbols = sp.symbols("s_tx0 s_ty0 s_xy0 s_tx1 s_ty1 s_xy1")
    generic = b214.formal_cell(dict(zip(FACE_ORDER, sign_symbols)), G0, G1, V0, V1, PARAMETER_SYMBOLS)
    h0, m, _ = b214.principal_part(generic, "onsite")
    facts["onsite_h0_is_the_cell"] = residual_count((h0 - generic).applyfunc(sp.cancel)) == 0
    m_oo = m.extract(odd, odd)
    facts["m_oo_free_symbols"] = tuple(sorted(str(s) for s in m_oo.free_symbols))
    facts["m_oo_entries"] = (str(sp.factor(m_oo[0, 1])), str(sp.factor(m_oo[0, 2])), str(sp.factor(m_oo[1, 2])))
    facts["m_oo_row7_zero"] = residual_count(m_oo[3, :]) == 0 and residual_count(m_oo[:, 3]) == 0
    facts["m_oo_zero_on_star_line"] = residual_count(m_oo.subs({C25: -B16, D34: B16})) == 0
    facts["m_oo_ideal_is_star_line"] = tuple(sorted(str(g) for g in b214.radical_generators(
        b214.coefficient_ideal(sum((m_oo[i, j] * sp.Symbol(f"w{i}{j}") for i in range(4) for j in range(4)), 0),
                               KAPPA + tuple(sp.Symbol(f"w{i}{j}") for i in range(4) for j in range(4)),
                               (B16, C25, D34)), (B16, C25, D34)))) == tuple(sorted(b214.PLANE))
    # THE BLOCK IDENTITY det [[A, B], [B^T, 0]] = det(B)^2 at generic symbolic blocks
    a = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"a{min(i, j)}{max(i, j)}"))
    b = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"b{i}{j}"))
    block = sp.BlockMatrix([[a, b], [b.T, sp.zeros(4, 4)]]).as_explicit()
    facts["block_identity_generic"] = sp.expand(
        b214.ff_det(block, tuple(sorted(block.free_symbols, key=str))) - b.det(method="berkowitz") ** 2) == 0
    # THE NECESSITY HALF at every witness: W1's moduli at the 16 star cells,
    # the all-plus control and the flat cell (rational); the curve moduli at
    # the 8 rule-A cells (QQ(sqrt 6)).
    table: dict = {}
    for values in star_cells(census) + (ALL_PLUS_CELL,):
        mask = census["cells"][values]["mask"]
        cell = formal(values, moduli_as_g(W1_MODULI), (sp.Integer(0), B16, C25, D34))
        minors = b211.leading_minors(cell.subs({p: 0 for p in PARAMETER_SYMBOLS}))
        print(f"[union] W1 moduli at cell {mask}", file=sys.stderr)
        generators, sufficiency, _ = union_locus(cell, False)
        table[("W1", mask)] = (tuple(sorted(str(g) for g in generators)), sufficiency, all(x > 0 for x in minors))
    flat = formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), (sp.Integer(0), B16, C25, D34))
    generators, sufficiency, _ = union_locus(flat, False)
    table[("flat", 0)] = (tuple(sorted(str(g) for g in generators)), sufficiency, True)
    for values in star_cells(census):
        c = census["cells"][values]
        if not c["rule_a"]:
            continue
        print(f"[union] curve moduli at cell {c['mask']}", file=sys.stderr)
        cell = formal(values, moduli_as_g(curve_moduli(c["class"][0])), (sp.Integer(0), B16, C25, D34))
        minors = b211.leading_minors(cell.subs({p: 0 for p in PARAMETER_SYMBOLS}))
        generators, sufficiency, _ = union_locus(cell, True)
        table[("curve", c["mask"])] = (tuple(sorted(str(g) for g in generators)), sufficiency, all(sp.radsimp(x) > 0 for x in minors))
    facts["table"] = table
    facts["necessity_is_plane_everywhere"] = all(entry[0] == tuple(sorted(b214.PLANE)) for entry in table.values())
    facts["sufficiency_everywhere"] = all(entry[1] for entry in table.values())
    facts["witnesses_positive_definite"] = all(entry[2] for entry in table.values())
    facts["witness_count"] = len(table)
    facts["rational_witness_count"] = sum(1 for key in table if key[0] in ("W1", "flat"))
    facts["curve_witness_count"] = sum(1 for key in table if key[0] == "curve")
    reps = class_representatives(census)
    facts["class_representative_masks"] = {key: census["cells"][v]["mask"] for key, v in reps.items()}
    facts["one_witness_per_class"] = all(("W1", census["cells"][v]["mask"]) in table for v in reps.values())
    return facts


# ---------------------------------------------------------------------------
# F. THE COVARIANT WITNESS WITH ONE METRIC'S CONE, at every common positive cell
# ---------------------------------------------------------------------------
def strict_stabiliser(cell: sp.Matrix, lifts: tuple) -> tuple:
    """The rotations whose lift preserves the cell with E = 1, exactly."""
    return tuple(g for g in range(24) if residual_count((lifts[g] * cell * lifts[g].T - cell).applyfunc(sp.radsimp)) == 0)


def block211_solve(values: tuple, moduli: tuple) -> tuple:
    """Block 211's six-face system solved with the parameters free (Block
    214's cell_with_parameters route) at a transported witness."""
    v0, g0, v1, g1 = moduli
    _, matrix, rhs = b211.face_system(b211.branch_moduli(v0, g0, v1, g1, sign_dict(values)))
    cell, free = b211.solve_pinned(matrix, rhs, at_zero=False)
    cell = cell.applyfunc(sp.radsimp)
    names = dict(zip(PARAMETER_NAMES, PARAMETER_SYMBOLS))
    renamed = cell.subs({s: names[str(s)] for s in cell.free_symbols if str(s) in PARAMETER_NAMES})
    return renamed, tuple(str(s) for s in free)


def measure_witness(group: dict, census: dict) -> dict:
    """At each of the 8 rule-A star cells: Block 213's curve point over
    QQ(sqrt 6) transported to the cell -- positive definite, on the curve, on
    the ties, Block 211's own solve; strictly S3-covariant with both shears
    alive, the star line its parameter locus, and preserved on the line; the
    two Hodge readings proportional; the graded cone one quadric squared, and
    one metric's cone with the parameters on the star line."""
    lifts, orders = group["lifts"], group["orders"]
    even, odd = b213.even_odd(3)
    facts: dict = {}
    table: dict = {}
    star_line = b215.canonical_subspace([[0, 1, 0, -1], [0, 0, 1, 1]], PARAMETER_SYMBOLS)
    for values in star_cells(census):
        c = census["cells"][values]
        if not c["rule_a"]:
            continue
        pi0 = c["class"][0]
        moduli = curve_moduli(pi0)
        v0, g0, v1, g1 = moduli
        entry: dict = {"class": c["class"], "moduli": moduli}
        entry["on_curve"] = sp.radsimp(g0 - g1 / (1 + pi0 * g1)) == 0
        entry["on_ties"] = (sp.radsimp(v0 ** 2 - (1 - g0 ** 2) * (1 - g1 ** 2)) == 0
                            and sp.radsimp(v1 ** 2 - (1 - g1 ** 2) / (1 - g0 ** 2)) == 0)
        entry["shears_nonzero"] = g0 != 0 and g1 != 0
        cell = formal(values, moduli_as_g(moduli), PARAMETER_SYMBOLS)
        solved, free = block211_solve(values, moduli)
        entry["is_block211_solve"] = residual_count((solved - cell).applyfunc(sp.radsimp)) == 0 and free == PARAMETER_NAMES
        zero = cell.subs({p: 0 for p in PARAMETER_SYMBOLS})
        entry["positive_definite"] = all(sp.radsimp(x) > 0 for x in b211.leading_minors(zero))
        stabiliser = strict_stabiliser(zero, lifts)
        entry["stabiliser"] = stabiliser
        entry["stabiliser_orders"] = tuple(sorted(orders[g] for g in stabiliser))
        entry["stabiliser_is_s3_body"] = any(frozenset(stabiliser) == member for member in group["classes"]["S3_body"])
        # (indexed by rotation, as Block 215's subgroup_locus expects: all 24)
        strict_per = tuple(b215.irredundant([b215.constraints(cell, lifts[g], (1,) * 8, PARAMETER_SYMBOLS)]) for g in range(24))
        locus = b215.subgroup_locus(strict_per, frozenset(stabiliser), PARAMETER_SYMBOLS)
        entry["strict_locus"] = b215.describe(locus, PARAMETER_SYMBOLS)
        entry["strict_locus_is_star_line_alive"] = locus == ((frozenset(), star_line),)
        on_line = cell.subs({B16: LAM_LINE, C25: -LAM_LINE, D34: LAM_LINE, A07: 0})
        entry["preserved_on_line"] = all(residual_count((lifts[g] * on_line * lifts[g].T - on_line).applyfunc(sp.radsimp)) == 0
                                         for g in stabiliser)
        g1_m, g2_m, _, _, _, _ = b213.metric_candidates(zero)
        g1_m, g2_m = g1_m.applyfunc(sp.radsimp), g2_m.applyfunc(sp.radsimp)
        mu = sp.radsimp(g2_m[0, 0] / g1_m[0, 0])
        entry["mu"] = mu
        entry["readings_proportional"] = residual_count((g2_m - mu * g1_m).applyfunc(sp.radsimp)) == 0
        form = b213.quadratic_form(g1_m, KAPPA)
        h0, m, _ = b214.principal_part(zero, "onsite")
        det_b = sp.expand(sp.radsimp(m.extract(even, odd).det(method="berkowitz")))
        entry["graded_cone_is_one_quadric_squared"] = b213.proportional(det_b, form ** 2, KAPPA)
        _, m_line, _ = b214.principal_part(on_line, "onsite")
        det_m_line = sp.expand(b214.ff_det(m_line, (LAM_LINE,) + KAPPA, algebraic=True))
        entry["cone_on_line_is_one_metric_cone"] = b213.proportional(det_m_line, form ** 4, KAPPA + (LAM_LINE,))
        entry["cone_on_line_constant"] = sp.factor(sp.radsimp(sp.cancel(det_m_line / form ** 4)))
        table[c["mask"]] = entry
    facts["table"] = table
    facts["witness_count"] = len(table)
    keys = ("on_curve", "on_ties", "shears_nonzero", "is_block211_solve", "positive_definite", "stabiliser_is_s3_body",
            "strict_locus_is_star_line_alive", "preserved_on_line", "readings_proportional",
            "graded_cone_is_one_quadric_squared", "cone_on_line_is_one_metric_cone")
    facts["all_witnesses"] = {key: all(entry[key] for entry in table.values()) for key in keys}
    facts["mu_per_class"] = {key: tuple(sorted(set(entry["mu"] for entry in table.values() if entry["class"] == key)))
                             for key in ((1, -1), (-1, 1))}
    facts["stabiliser_orders"] = tuple(sorted(set(entry["stabiliser_orders"] for entry in table.values())))
    facts["cone_on_line_constants"] = tuple(sorted(set(str(entry["cone_on_line_constant"]) for entry in table.values())))
    return facts


# ---------------------------------------------------------------------------
# G. THE BRANCHES ON THE COVARIANT LINE, THE D07 CONGRUENCE, THE SYMBOL UNDER S3
# ---------------------------------------------------------------------------
def line_branches(cell_on_line: sp.Matrix, form) -> tuple:
    """The H-pencil charpoly of (H0^-1 M)^2 over QQ(sqrt 6)(lam_line)[kappa],
    factored: every factor linear in LAM gives a branch, reported as its
    k-free ratio to k^T G1 k (a rational function of the line multiple)."""
    from sympy import QQ
    from sympy.polys.matrices import DomainMatrix
    h0, m, _ = b214.principal_part(cell_on_line, "onsite")
    operator = (h0.inv() * m).applyfunc(sp.radsimp)
    squared = (operator * operator).applyfunc(sp.radsimp)
    gens = tuple(sorted(squared.free_symbols - {sp.sqrt(6)}, key=str))
    domain = QQ.algebraic_field(sp.sqrt(6)).frac_field(*gens)
    coefficients = DomainMatrix.from_Matrix(squared).convert_to(domain).charpoly()
    lam = b213.LAM
    charpoly = sum(domain.to_sympy(cf) * lam ** (len(coefficients) - 1 - k) for k, cf in enumerate(coefficients))
    numerator, _ = sp.fraction(sp.factor(charpoly))
    _, factors = sp.factor_list(numerator, lam)
    branches, remainder = [], []
    for base, power in factors:
        poly = sp.Poly(base, lam)
        if poly.degree() == 1:
            root = sp.cancel(-poly.coeff_monomial(1) / poly.coeff_monomial(lam))
            ratio = sp.factor(sp.radsimp(sp.cancel(root / form)))
            branches.append((str(ratio), power, not (ratio.free_symbols & set(KAPPA))))
        elif poly.degree() > 0:
            remainder.append((poly.degree(), power))
    return tuple(sorted(branches)), tuple(sorted(remainder))


def measure_branches(census: dict) -> dict:
    facts: dict = {}
    even, odd = b213.even_odd(3)
    # THE D07 CONGRUENCE AT SYMBOLIC FACE SIGNS AND SYMBOLIC MODULI: U = I - (D07/D3) E_70
    sign_symbols = sp.symbols("s_tx0 s_ty0 s_xy0 s_tx1 s_ty1 s_xy1")
    generic = b214.formal_cell(dict(zip(FACE_ORDER, sign_symbols)), G0, G1, V0, V1, PARAMETER_SYMBOLS)
    h0, m, _ = b214.principal_part(generic, "onsite")
    unipotent = sp.eye(8)
    unipotent[7, 0] = -A07 / generic[7, 7]
    facts["d07_congruence_M_symbolic_signs"] = residual_count((unipotent.T * m * unipotent - m.subs(A07, 0)).applyfunc(sp.cancel)) == 0
    shifted = (unipotent.T * h0 * unipotent - h0.subs(A07, 0)).applyfunc(sp.cancel)
    facts["d07_shift"] = str(sp.factor(shifted[0, 0]))
    facts["d07_shift_rest_zero"] = residual_count(shifted) == 1
    facts["d07_congruence_holds_at_star_cells"] = all(
        residual_count((unipotent.T * m * unipotent - m.subs(A07, 0)).subs(dict(zip(sign_symbols, values))).applyfunc(sp.cancel)) == 0
        for values in star_cells(census))
    # THE BRANCHES ON THE COVARIANT LINE at the two named curve witnesses (their own cells)
    table: dict = {}
    for name, pi0 in (("L+-", 1), ("L-+", -1)):
        values = next(v for v, c in census["cells"].items() if c["rule_a"] and c["class"][0] == pi0
                      and sign_dict(v) == b213.locus_witness_table()[name][1])
        moduli = curve_moduli(pi0)
        v0, g0, v1, g1 = moduli
        cell = formal(values, moduli_as_g(moduli), PARAMETER_SYMBOLS)
        zero = cell.subs({p: 0 for p in PARAMETER_SYMBOLS})
        g1_m = b213.metric_candidates(zero)[0].applyfunc(sp.radsimp)
        form = b213.quadratic_form(g1_m, KAPPA)
        print(f"[branches] {name} symbolic line multiple", file=sys.stderr)
        on_line = cell.subs({B16: LAM_LINE, C25: -LAM_LINE, D34: LAM_LINE, A07: 0})
        symbolic, remainder = line_branches(on_line, form)
        table[(name, "line symbolic")] = (symbolic, remainder)
        for label, point in (("line 1/4", {B16: QUARTER, C25: -QUARTER, D34: QUARTER, A07: 0}),
                             ("line 1/4 + D07 1/4", {B16: QUARTER, C25: -QUARTER, D34: QUARTER, A07: QUARTER})):
            print(f"[branches] {name} {label}", file=sys.stderr)
            branches, remainder = line_branches(cell.subs(point), form)
            table[(name, label)] = (branches, remainder)
        table[(name, "v0 v1")] = sp.radsimp(v0 * v1)
        table[(name, "v1 / v0")] = sp.radsimp(v1 / v0)
        table[(name, "d07 rescale 1/4")] = sp.radsimp(1 / (1 - QUARTER ** 2 * v1 / v0))
        table[(name, "line rescale 1/4")] = sp.radsimp(1 / (1 - QUARTER ** 2 / (v0 * v1)))
    facts["table"] = table
    facts["all_branches_k_free"] = all(all(kf for _, _, kf in entry[0]) and entry[1] == ()
                                       for key, entry in table.items() if isinstance(entry, tuple))
    return facts


def invariant_quadric_dimension(rotations: tuple, members: tuple) -> int:
    """dim { G symmetric 3 x 3 : R^T G R = G for every R in the members }."""
    g = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"q{min(i, j)}{max(i, j)}"))
    unknowns = tuple(g[i, j] for i in range(3) for j in range(i, 3))
    rows = []
    for index in members:
        r = rotations[index]
        residual = (r.T * g * r - g).applyfunc(sp.expand)
        for i in range(3):
            for j in range(i, 3):
                rows.append([sp.Poly(residual[i, j], *unknowns).coeff_monomial(u) for u in unknowns])
    return 6 - sp.Matrix(rows).rank()


def measure_symbol(group: dict, census: dict) -> dict:
    """(e): at each rule-A witness the two quadrics of Block 213's symbol
    identity det B = D3 (k^T D1 k)(k^T E adj(D2) E k) and det B itself are
    invariant under kappa -> R kappa EXACTLY for the strict stabiliser (an
    S3_body), each quadric lies in the two-dimensional S3-invariant space
    span(|k|^2, (n . k)^2) with n the 3-fold axis; the full group would leave
    only |k|^2 (the flat cell); a twisted rotation maps the symbol to the
    symbol of the GAUGED raising part E' D E', not to itself."""
    lifts, rots, orders = group["lifts"], group["rotations"], group["orders"]
    even, odd = b213.even_odd(3)
    facts: dict = {}
    table: dict = {}
    k2 = KT ** 2 + KX ** 2 + KY ** 2
    a, b = sp.symbols("a_inv b_inv")
    for values in star_cells(census):
        c = census["cells"][values]
        if not c["rule_a"]:
            continue
        zero = formal(values, moduli_as_g(curve_moduli(c["class"][0])), (0, 0, 0, 0))
        _, _, _, d1, d2, d3 = b213.metric_candidates(zero)
        q1 = b213.quadratic_form(d1, KAPPA)
        q2 = b213.quadratic_form(SIGNATURE * d2.adjugate() * SIGNATURE, KAPPA)
        _, m, _ = b214.principal_part(zero, "onsite")
        det_b = sp.expand(sp.radsimp(m.extract(even, odd).det(method="berkowitz")))
        entry: dict = {"identity": is_zero_alg(det_b - d3 * q1 * q2)}
        stabiliser = strict_stabiliser(zero, lifts)
        entry["stabiliser"] = stabiliser
        for label, expression in (("q1", q1), ("q2", q2), ("detB", det_b)):
            entry[label + "_invariance_set"] = tuple(g for g in range(24) if is_zero_alg(rotate_kappa(expression, rots[g]) - expression))
        entry["invariance_sets_are_the_stabiliser"] = all(entry[label + "_invariance_set"] == stabiliser for label in ("q1", "q2", "detB"))
        three_cycle = next(g for g in stabiliser if orders[g] == 3)
        axis = (rots[three_cycle] - sp.eye(3)).nullspace()[0]
        axis = axis / sp.gcd(list(axis))
        entry["axis"] = tuple(axis)
        nk = (axis.T * sp.Matrix(KAPPA))[0, 0]
        spans = []
        for expression in (q1, q2):
            equations = sp.Poly(sp.expand(sp.radsimp(expression - a * k2 - b * nk ** 2)), *KAPPA).coeffs()
            solution = sp.linsolve(equations, (a, b))
            spans.append(tuple(sp.radsimp(x) for x in next(iter(solution))) if solution else None)
        entry["span_coefficients"] = tuple(spans)
        entry["in_invariant_span"] = all(s is not None for s in spans)
        entry["invariant_quadric_dimension_s3"] = invariant_quadric_dimension(rots, stabiliser)
        entry["invariant_quadric_dimension_o"] = invariant_quadric_dimension(rots, tuple(range(24)))
        table[c["mask"]] = entry
    facts["table"] = table
    facts["identity_everywhere"] = all(e["identity"] for e in table.values())
    facts["invariance_is_exactly_s3_everywhere"] = all(e["invariance_sets_are_the_stabiliser"] and len(e["stabiliser"]) == 6
                                                       for e in table.values())
    facts["quadrics_in_s3_span_everywhere"] = all(e["in_invariant_span"] for e in table.values())
    facts["invariant_dimensions"] = tuple(sorted(set((e["invariant_quadric_dimension_s3"], e["invariant_quadric_dimension_o"])
                                                     for e in table.values())))
    facts["axes"] = tuple(sorted(set(e["axis"] for e in table.values())))
    # THE FLAT CELL: both quadrics are |k|^2, invariant under all 24
    flat = formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), (0, 0, 0, 0))
    _, _, _, d1f, d2f, _ = b213.metric_candidates(flat)
    facts["flat_quadrics_are_k2"] = (sp.expand(b213.quadratic_form(d1f, KAPPA) - k2) == 0
                                     and sp.expand(b213.quadratic_form(SIGNATURE * d2f.adjugate() * SIGNATURE, KAPPA) - k2) == 0)
    # THE TWISTED IDENTITY at L+-'s own cell for the order-4 generator: with
    # T = E L preserving H (E != 1), T^T M(kappa) T = M_{E'}(R^-1 kappa) where
    # E' = L^T E L and M_{E'} is the principal part of the gauged raising part
    # E' D E' -- so det B(R kappa) = det B_{E'}(kappa), and det B itself moves.
    lpm = b213.locus_witness_table()["L+-"]
    zero = b214.formal_cell(lpm[1], lpm[0][1], lpm[0][3], lpm[0][0], lpm[0][2], (0, 0, 0, 0))
    _, m0, _ = b214.principal_part(zero, "onsite")
    det_b0 = sp.expand(sp.radsimp(m0.extract(even, odd).det(method="berkowitz")))
    det_m0 = sp.expand(b214.ff_det(m0, KAPPA, algebraic=True))
    dk = b214.raising_matrix()
    g4 = next(g for g in range(24) if orders[g] == 4)
    lift = lifts[g4]
    twists = [e for e in b215.sign_vectors()
              if residual_count((sp.diag(*e) * lift * zero * lift.T * sp.diag(*e) - zero).applyfunc(sp.radsimp)) == 0]
    facts["twist_count_order4"] = len(twists)
    gauged_identity, gauged_block, moves, conjugation = [], [], [], []
    for e in twists:
        twisted_lift = sp.diag(*e) * lift
        e_prime = (lift.T * sp.diag(*e) * lift).applyfunc(sp.expand)
        dk_gauged = (e_prime * dk * e_prime).applyfunc(sp.expand)
        m_gauged = (zero * dk_gauged + dk_gauged.T * zero).applyfunc(sp.expand)
        # T^T M(kappa) T = M_{E'}(R^-1 kappa) entry by entry, hence det M(R kappa) = det M_{E'}(kappa)
        conjugation.append(residual_count(((twisted_lift.T * m0 * twisted_lift) - m_gauged.subs(
            {k: sum(rots[g4].T[i, j] * KAPPA[j] for j in range(3)) for i, k in enumerate(KAPPA)}, simultaneous=True)
        ).applyfunc(sp.radsimp)) == 0)
        det_m_gauged = sp.expand(b214.ff_det(m_gauged, KAPPA, algebraic=True))
        gauged_identity.append(is_zero_alg(rotate_kappa(det_m0, rots[g4]) - det_m_gauged))
        # the even-odd block picks up the sign det(T_e) det(T_o) = +-1 of the twisted lift
        sign = twisted_lift.extract(even, even).det() * twisted_lift.extract(odd, odd).det()
        det_b_gauged = sp.expand(sp.radsimp(m_gauged.extract(even, odd).det(method="berkowitz")))
        gauged_block.append(is_zero_alg(rotate_kappa(det_b0, rots[g4]) - sign * det_b_gauged))
        moves.append(not is_zero_alg(rotate_kappa(det_m0, rots[g4]) - det_m0))
    facts["twisted_conjugation_identity"] = bool(twists) and all(conjugation)
    facts["twisted_symbol_is_gauged_symbol"] = bool(twists) and all(gauged_identity)
    facts["twisted_block_is_gauged_block_up_to_sign"] = bool(twists) and all(gauged_block)
    facts["twisted_symbol_moves"] = bool(twists) and all(moves)
    facts["gauged_raising_differs"] = bool(twists) and all(
        residual_count(((lift.T * sp.diag(*e) * lift) * dk * (lift.T * sp.diag(*e) * lift) - dk).applyfunc(sp.expand)) > 0 for e in twists)
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    group: dict
    census: dict
    covariance: dict
    union: dict
    witness: dict
    branches: dict
    symbol: dict
    axiom_text: str
    note_text: str
    timings: dict


def measure() -> Facts:
    timings: dict = {}
    started = time.monotonic_ns()

    def lap(label: str) -> None:
        nonlocal started
        now = time.monotonic_ns()
        timings[label] = (now - started) // 1_000_000
        started = now
        print(f"[phase] {label}: {timings[label]} ms", file=sys.stderr)

    git_maybe("fetch", "origin", "main", "--quiet")
    authority = authority_certificate(git_maybe("rev-parse", "origin/main"))
    lap("authority")
    group = b215.measure_group()
    lap("group")
    census = measure_census()
    lap("census")
    covariance = measure_covariance(group, census)
    lap("covariance")
    union = measure_union(census)
    lap("union")
    witness = measure_witness(group, census)
    lap("witness")
    branches = measure_branches(census)
    lap("branches")
    symbol = measure_symbol(group, census)
    lap("symbol")
    axiom_text = (ROOT / AXIOM_PATH).read_text(encoding="utf-8") if (ROOT / AXIOM_PATH).is_file() else ""
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, group, census, covariance, union, witness, branches, symbol, axiom_text, note_text, timings)


# ---------------------------------------------------------------------------
# THE DECLARED LITERALS -- every claim is a constant compared against a
# measurement; a mutation rewrites exactly one claim.
# ---------------------------------------------------------------------------
FACE_ORDER_LITERAL = (("tx", 0), ("ty", 0), ("xy", 0), ("tx", 1), ("ty", 1), ("xy", 1))
STAR_MASKS = (2, 5, 11, 12, 16, 23, 25, 30, 33, 38, 40, 47, 51, 52, 58, 61)     # = the refuting checker's CK-11 list
RULE_A_MASKS = (2, 11, 16, 25, 38, 47, 52, 61)
RULE_B_MASKS = (5, 12, 23, 30, 33, 40, 51, 58)
COINCIDENCE_CENSUS = (                    # Block 213's literal, re-declared here and compared to both
    ("(g0*g1 + g0 + g1,)", 4, ((-1, -1),)),
    ("(g0*g1 + g0 - g1,)", 4, ((1, -1),)),
    ("(g0*g1 - g0 + g1,)", 4, ((-1, 1),)),
    ("(g0*g1 - g0 - g1,)", 4, ((1, 1),)),
    ("(g0, g1)", 48, ((-1, -1), (-1, 1), (1, -1), (1, 1))),
)
STAR_PER_CLASS = {(1, 1): (5, 30, 40, 51), (1, -1): (2, 25, 47, 52), (-1, 1): (11, 16, 38, 61), (-1, -1): (12, 23, 33, 58)}
CLASS_REPRESENTATIVE_MASKS = {(1, 1): 5, (1, -1): 2, (-1, 1): 11, (-1, -1): 12}
INTERSECTION_COUNT = 16
POSITIVE_SUBSET_COUNT = 8
RULE_A_CLASSES = ((-1, 1), (1, -1))
RULE_B_CLASSES = ((-1, -1), (1, 1))
STAR_TO_RULE_A_DISTANCES = ((0, 8), (3, 8))       # (face flips to the nearest rule-A cell, number of star cells)
STAR_LINE = ("D16 - D34", "D25 + D34")            # = Block 214's PLANE = Block 215's STAR_LINE
DIAGONAL_LINE = ("D16 - D34", "D25 - D34")
M_OO_ENTRIES = ("kt*(D16 + D25)", "-kx*(D16 - D34)", "-ky*(D25 + D34)")   # = Block 214's ONSITE_M_OO_ENTRIES
M_OO_FREE_SYMBOLS = ("D16", "D25", "D34", "kt", "kx", "ky")
UNION_WITNESS_COUNTS = (26, 18, 8)                 # (all, rational, on the curve over QQ(sqrt 6))
COVARIANT_WITNESS_COUNT = 8
MU_PER_CLASS = {(1, -1): (sp.Rational(32, 27),), (-1, 1): (sp.Rational(27, 32),)}
STABILISER_ORDERS = ((1, 2, 2, 2, 3, 3),)
CONE_ON_LINE_CONSTANTS = ("64/81", "9/16")         # det M = c (k^T G1 k)^4 on the star line, per class of pi0
BRANCH_TABLE = {
    ("L+-", "line symbolic"): ((("-32/(9*(4*lam_line**2 - 3))", 2, True), ("-4/(4*lam_line**2 - 3)", 4, True), ("1", 2, True)), ()),
    ("L+-", "line 1/4"): ((("1", 2, True), ("128/99", 2, True), ("16/11", 4, True)), ()),
    ("L+-", "line 1/4 + D07 1/4"): ((("128/119", 2, True), ("128/99", 2, True), ("16/11", 4, True)), ()),
    ("L-+", "line symbolic"): ((("-27/(4*(9*lam_line**2 - 8))", 2, True), ("-9/(9*lam_line**2 - 8)", 4, True), ("1", 2, True)), ()),
    ("L-+", "line 1/4"): ((("1", 2, True), ("108/119", 2, True), ("144/119", 4, True)), ()),
    ("L-+", "line 1/4 + D07 1/4"): ((("108/119", 2, True), ("12/11", 2, True), ("144/119", 4, True)), ()),
}
VOLUME_PRODUCTS = {"L+-": sp.Rational(3, 4), "L-+": sp.Rational(8, 9)}          # v0 v1
VOLUME_RATIOS = {"L+-": sp.Rational(9, 8), "L-+": sp.Rational(4, 3)}            # v1 / v0
D07_RESCALE = {"L+-": sp.Rational(128, 119), "L-+": sp.Rational(12, 11)}       # 1/(1 - D07^2 v1/v0) at D07 = 1/4
LINE_RESCALE = {"L+-": sp.Rational(12, 11), "L-+": sp.Rational(128, 119)}      # 1/(1 - lam^2/(v0 v1)) at lam = 1/4
D07_SHIFT = "-D07**2*v1"                                                        # = Block 214's D07_SHIFT
INVARIANT_DIMENSIONS = ((2, 1),)                   # (dim of S3-invariant quadrics, dim of O-invariant quadrics)
AXES = ((-1, -1, 1), (-1, 1, 1), (1, -1, 1), (1, 1, 1))
TWIST_COUNT_ORDER4 = 4
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
INSTANCE_SCOPE = (
    "one cell form: Block 211's family at the 16 star-pattern cells, with the all-plus and flat cells as controls; no other cell's necessity half is run",
    "one assembly measured (onsite); the overlap assembly at the 16 cells is not computed; neither assembly decided",
    "the witnesses: W1's moduli, the flat moduli and Block 213's two curve points transported by class; the parameters symbolic, the line multiple symbolic, D07 at 1/4",
    "the pencil factored with the multiple symbolic at the two named curve witnesses only; the cone on the line at all eight",
    "the covariance notion: Block 215's (E_R R) H (E_R R)^T = H, twisted over its 64 sign vectors or strict; its lift, its generators; no other twist",
    "no bench, no dispersion, no continuum, no metric of anything physical; 'one metric's cone' names Block 213's statement only",
)
INSTANCE_SCOPE_COUNT = 6

N5_FENCE = "N5: per_element: THE IMPOSED-OBJECT BANNER FIRST, AND THE WORDS COVARIANCE, CONE, CELL, LOCUS AND METRIC ARE EACH SCOPED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- the cube complex and its wedge, Block 211's family with its 64 face-sign cells and its four free parameters, Block 213's coincidence census and curve witnesses, Block 214's principal part and plane, Block 215's lift and star-pattern cells, and Block 105's assemblies are IMPOSED MEASURED OBJECTS. NO GRAVITY IS SUPPLIED. 'COVARIANCE' NAMES THE MATRIX IDENTITY (E_R R) H (E_R R)^T = H AND WHETHER THE CELL FORM INHERITS THE AXIOM'S COVARIANCE IS A READING ASSERTED NOWHERE; 'ONE METRIC'S CONE' NAMES BLOCK 213'S EXACT STATEMENT det B = c (k^T G1 k)^2 AND NOTHING PHYSICAL; NO CELL, NO SUBGROUP, NO ASSEMBLY, NO PARAMETER VALUE IS SELECTED.\\nper_site: The two 64-cell indexings (Block 213's FACES, Block 211's GAUGE_FACE_ORDER) are the same tuple (tx0, ty0, xy0, tx1, ty1, xy1) and both predicates are re-evaluated from the sign dictionary; Block 213's Groebner census reproduces literal for literal; Block 215's twisted-O line is the star line and exactly one S3_body keeps both shears alive strictly at every one of the 16 star-pattern cells, the diagonal and no alive S3 at the all-plus control; every witness used is Block 211's own solve and positive definite.\\nper_mode: THE M_oo LEMMA: at SYMBOLIC face signs the odd-odd block of the onsite principal part is (D16 + D25) kt, (D34 - D16) kx, -(D25 + D34) ky with no shear, no volume, no face sign and no D07, so its coefficient ideal is the star line at every cell and det M = det B^2 there by the block identity det [[A, B], [B^T, 0]] = det(B)^2 (verified at generic symbolic blocks); THE NECESSITY HALF: the radical of the coefficient ideal of det M - det B^2 in (D16, D25, D34) is exactly (D16 - D34, D25 + D34) at all 26 positive-definite witnesses -- W1's moduli at the 16 star cells, at the all-plus control and at the flat cell, and Block 213's curve moduli over QQ(sqrt 6) at the 8 rule-A cells; at least one witness in each of the four gauge classes among the 16.\\nper_block: THE CENSUS: Block 213's 16 coincidence-curve cells ARE Block 215's 16 star-pattern cells -- rule A (S1 = -E S0 E) iff (P_tx, P_ty, P_xy) = (+, -, +), rule B iff (-, +, -), because P_f = -+E_i E_j = +-E_k and Block 213's E = diag(1, -1, 1) is the star's pair-sign pattern; the intersection is all 16, the positive subset all 8 rule-A cells (four in each mixed class), the 8 rule-B star cells 3 face flips from the nearest rule-A cell. THE COVARIANT WITNESS: at each of the 8 rule-A cells Block 213's curve point transported to the cell is positive definite, strictly S3-covariant with both shears alive (its strict stabiliser IS an S3_body, the star line its parameter locus, preserved on the line), the readings proportional with mu = 32/27 or 27/32, the graded cone one quadric squared, and det M = c (k^T G1 k)^4 on the star line with the multiple symbolic (c = 64/81, 9/16): ONE METRIC'S CONE FOR EVERY LINE MULTIPLE AND EVERY D07.\\nlattice_wide: THE BRANCHES ON THE COVARIANT LINE at L+- and L-+: all four pencil branches are k-free constants times k^T G1 k -- {1, (32/27)/(1 - lam^2/(v0 v1)), (4/3)/(1 - lam^2/(v0 v1)) twice} at L+- with v0 v1 = 3/4 and {1, (27/32)/(1 - lam^2/(v0 v1)), (9/8)/(1 - lam^2/(v0 v1)) twice} at L-+ with v0 v1 = 8/9, the line multiple rescaling the top-form and transverse constants and D07 the 0-form constant alone (128/119 at L+-, 12/11 at L-+ at D07 = 1/4); the D07 congruence U^T M U = M|_{D07 = 0} holds at symbolic face signs with the H0 shift -D07^2 v1. THE SYMBOL: Block 213's identity det B = D3 (k^T D1 k)(k^T E adj(D2) E k) holds at every witness; both quadrics and det B are invariant under kappa -> R kappa for EXACTLY the strict S3, each quadric lies in the two-dimensional S3-invariant space span(|k|^2, (n . k)^2), the O-invariant space is one-dimensional (the flat cell's |k|^2), and a twisted rotation maps det M to the symbol of the GAUGED raising part E' D E' (det B up to the twisted lift's sign), never to itself.\\nper_scope: THE THEOREM IS THE CONDITIONAL: IF the cell form is (twisted-)covariant under the group THEN at the 16 cells the parameters lie on the star line and the cone is the union of the readings' cones there; the antecedent is a reading. OPEN: the overlap assembly at the 16 cells; the necessity half symbolically in the moduli; the pencil at the other six rule-A cells; the bench; no dynamics, continuum or gravity is supplied.\\nRESULT: AT EVERY ONE OF THE 16 STAR-PATTERN CELLS THE UNION LOCUS OF THE CONE IS THE STAR LINE, THE LINE COVARIANCE SELECTS THERE WITH THE SHEARS ALIVE; THE 16 CELLS ARE EXACTLY BLOCK 213'S 16 COINCIDENCE CELLS AND EACH OF THE 8 POSITIVE ONES CARRIES A STRICTLY S3-COVARIANT POSITIVE-DEFINITE WITNESS WITH ONE METRIC'S CONE FOR EVERY LINE MULTIPLE AND EVERY D07; THE SYMBOL IS EXACTLY S3-INVARIANT. SCOUT-GRADE FINITE EXACT LINEAR ALGEBRA ON ONE CELL FORM, NOT A SPACETIME AND NOT A DYNAMICS. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER NECESSITY -- the CYCLE913 CAUTION.\\nDECISION_CUT: NOTHING IS REGISTERED OR ADOPTED; no landed note is EDITED, no landed number touched; Blocks 105-215 STAND; Block 215's REOPEN item 2 is ANSWERED at the 16 cells as a conditional, in the affirmative: covariance and the cone agree there with the shears alive. Fable primary seat; refuting checker PENDING.\\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; retained-positive theory count remains zero."


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


def build_claims(mutation: str) -> dict:
    wrong_census = COINCIDENCE_CENSUS[:-1] + (("(g0, g1)", 64, ((-1, -1), (-1, 1), (1, -1), (1, 1))),)
    wrong_branches = dict(BRANCH_TABLE)
    wrong_branches[("L+-", "line 1/4")] = ((("1", 2, True), ("32/27", 2, True), ("4/3", 4, True)), ())
    claims = {
        "current_main": CURRENT_MAIN, "parent_commit": PARENT_COMMIT,
        "registered": (), "gravity_supplied": False, "covariance_inherited": False,
        "assembly_decided": False, "cell_selected": False, "metric_supplied": False,
        "face_order": FACE_ORDER_LITERAL, "star_masks": STAR_MASKS, "coincidence_census": COINCIDENCE_CENSUS,
        "witness_solves": True,
        "m_oo_entries": M_OO_ENTRIES, "union_necessity_plane": True, "union_necessity_measured": True,
        "intersection_count": INTERSECTION_COUNT, "positive_subset_count": POSITIVE_SUBSET_COUNT,
        "covariant_witness_count": COVARIANT_WITNESS_COUNT, "covariant_cell_exists": True,
        "cone_on_line_constants": CONE_ON_LINE_CONSTANTS,
        "branch_table": BRANCH_TABLE, "d07_rescale": D07_RESCALE, "d07_shift": D07_SHIFT,
        "invariant_dimensions": INVARIANT_DIMENSIONS,
        "scout_grade": SCOUT_GRADE_FENCE, "instance_scope_count": INSTANCE_SCOPE_COUNT,
        "n5_verbatim": True, "float_absent": True,
    }
    flips = {
        "stale_main_authority": ("current_main", STALE_MAIN),
        "stale_parent_authority": ("parent_commit", STALE_PARENT_COMMIT),
        "claim_objects_registered": ("registered", ("the covariant witness",)),
        "claim_gravity_supplied": ("gravity_supplied", True),
        "claim_covariance_inherited": ("covariance_inherited", True),
        "claim_assembly_decided": ("assembly_decided", True),
        "claim_cell_selected": ("cell_selected", True),
        "claim_metric_supplied": ("metric_supplied", True),
        "break_indexing_agreement": ("face_order", FACE_ORDER_LITERAL[3:] + FACE_ORDER_LITERAL[:3]),
        "break_star_pattern_masks": ("star_masks", STAR_MASKS[:8]),
        "break_coincidence_census": ("coincidence_census", wrong_census),
        "break_witness_solves": ("witness_solves", False),
        "break_m_oo_lemma": ("m_oo_entries", ("kt*(D16 + D25)", "-kx*(D16 - D34)", "-ky*(D25 - D34)")),
        "break_union_necessity": ("union_necessity_plane", False),
        "claim_union_from_identity_alone": ("union_necessity_measured", False),
        "break_intersection": ("intersection_count", 0),
        "break_positive_subset": ("positive_subset_count", 4),
        "break_covariant_witness": ("covariant_witness_count", 2),
        "claim_covariant_cell_empty": ("covariant_cell_exists", False),
        "break_one_metric_cone": ("cone_on_line_constants", ("1", "1")),
        "break_branch_table": ("branch_table", wrong_branches),
        "break_d07_rescale": ("d07_rescale", {"L+-": sp.Integer(1), "L-+": sp.Integer(1)}),
        "break_d07_congruence": ("d07_shift", "0"),
        "break_symbol_invariance": ("invariant_dimensions", ((1, 1),)),
        "break_scout_grade_fence": ("scout_grade", "a spacetime and a dynamics"),
        "break_instance_scope": ("instance_scope_count", 2),
        "drop_n5_fence": ("n5_verbatim", False),
        "break_float_absence": ("float_absent", False),
    }
    if mutation:
        key, value = flips[mutation]
        claims[key] = value
    return claims


def build_checks(facts: Facts, claims: dict) -> Checks:
    checks = Checks()
    au = facts.authority
    checks.check("A-1", "FIVE PINS RE-RESOLVED LIVE: origin/main, axiom and registry blobs on origin/main and in the worktree",
                 au.fixed_authority and claims["current_main"] == CURRENT_MAIN)
    checks.check("A-2", "PARENT PIN IS THE BLOCK 215 TIP, an ancestor of HEAD, with its note and runner content-bound by blob",
                 au.parent_pin_is_commit and au.parent_is_ancestor and au.parent_artifact_blobs
                 and claims["parent_commit"] == PARENT_COMMIT)
    checks.check("A-3", "STALE PARENT (the Block 214 tip) is a real ancestor carrying NEITHER Block 215 artifact; machinery imported; inputs readable",
                 au.stale_is_real_ancestor and au.stale_carries_neither_artifact
                 and au.machinery_import_landed and au.inputs_readable == len(AUDIT_INPUT_PATHS) - 1)
    checks.check("B-1", "NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted",
                 len(IMPOSED_OBJECTS) == 6 and claims["registered"] == REGISTERED_OBJECTS == () and ADOPTED_OBJECTS == ())
    checks.check("B-2", "NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied",
                 not claims["gravity_supplied"] and not GRAVITY_SUPPLIED_CLAIMED and len(UNSUPPLIED_GRAVITY_STRUCTURES) == 9)
    checks.check("B-3", "THE AXIOM CLAUSE IS QUOTED VERBATIM AND GOVERNS THE RULE; that the cell form inherits it is a READING, asserted nowhere (the theorem is the conditional)",
                 AXIOM_COVARIANCE_CLAUSE in facts.axiom_text and not claims["covariance_inherited"] and not COVARIANCE_INHERITED_CLAIMED)
    checks.check("B-4", "NO CELL, NO SUBGROUP, NO ASSEMBLY, NO PARAMETER VALUE IS SELECTED, AND NO METRIC IS SUPPLIED: 'one metric's cone' names Block 213's statement only",
                 not claims["cell_selected"] and not CELL_SELECTED_CLAIMED and not claims["assembly_decided"] and not ASSEMBLY_DECIDED_CLAIMED
                 and not claims["metric_supplied"] and not METRIC_SUPPLIED_CLAIMED and not SUBGROUP_SELECTED_CLAIMED
                 and not PARAMETER_VALUE_SELECTED_CLAIMED)
    checks.check("B-5", "THE WORDS COVARIANCE, CONE, CELL, LOCUS AND METRIC ARE SCOPED; six readings enumerated, none licensed; no continuum, no spacetime cone",
                 len(SCOPED_HEADLINE_WORDS) == 5 and len(READINGS) == 6 and not READINGS_LICENSED_CLAIMED
                 and not CONTINUUM_LIMIT_CLAIMED and not CONE_IS_SPACETIME_CONE_CLAIMED)
    ce, cv, un, wi, br, sy = facts.census, facts.covariance, facts.union, facts.witness, facts.branches, facts.symbol
    checks.check("C-1", "THE TWO 64-CELL INDEXINGS AGREE: Block 213's FACES and Block 211's GAUGE_FACE_ORDER are the same declared tuple (tx0, ty0, xy0, tx1, ty1, xy1); both predicates are evaluated from the sign dictionary",
                 ce["indexing_agrees"] and ce["face_order"] == claims["face_order"] == FACE_ORDER_LITERAL)
    checks.check("C-2", "THE 16 STAR-PATTERN CELLS REPRODUCE BLOCK 215's G-5 RULE (the declared masks, four per gauge class, the checker's list) AND BLOCK 213's COINCIDENCE CENSUS REPRODUCES LITERAL FOR LITERAL (48 + 4 x 4 cells; rule A and rule B masks declared)",
                 ce["star_masks"] == claims["star_masks"] == STAR_MASKS and len(STAR_MASKS) == 16
                 and ce["star_per_class"] == STAR_PER_CLASS and ce["census"] == tuple(sorted(claims["coincidence_census"]))
                 and ce["census_matches_block213"] and ce["rule_a_masks"] == RULE_A_MASKS and ce["rule_b_masks"] == RULE_B_MASKS
                 and ce["curve_is_rule_a_or_b"])
    checks.check("C-3", "THE COVARIANCE AT THE 16 CELLS, RE-MEASURED: the shear-alive twisted-O line is the star line at every star cell (one component), exactly one S3_body keeps both shears alive strictly there with the star line; at the all-plus control the line is the diagonal and no S3 keeps the shears alive",
                 cv["generators_generate_o"] and cv["twisted_line_is_star_line_at_every_star_cell"]
                 and cv["strict_s3_alive_count_per_star_cell"] == (1,) and cv["strict_s3_star_line_at_every_star_cell"]
                 and cv["all_plus_twisted_line"] == (((), DIAGONAL_LINE),) and not cv["strict_s3_alive_at_all_plus"])
    checks.check("C-4", "THE WITNESSES ARE BLOCK 211's OWN SOLVES: at every rule-A cell the transported curve point solves Block 211's six-face system with the four parameters free, is on the curve and on both ties, has both shears nonzero and is positive definite; every union witness is positive definite",
                 claims["witness_solves"] and wi["all_witnesses"]["is_block211_solve"] and wi["all_witnesses"]["on_curve"]
                 and wi["all_witnesses"]["on_ties"] and wi["all_witnesses"]["shears_nonzero"]
                 and wi["all_witnesses"]["positive_definite"] and un["witnesses_positive_definite"])
    checks.check("D-1", "THE M_oo LEMMA AT SYMBOLIC FACE SIGNS: the onsite H0 is the cell; the odd-odd block of M carries exactly Block 214's three entries, no shear, no volume, no face sign, no D07; its coefficient ideal is the star line; the block identity holds at generic symbolic blocks; det M = det B^2 on the line with the multiple symbolic at every witness",
                 un["onsite_h0_is_the_cell"] and un["m_oo_entries"] == claims["m_oo_entries"] == b214.ONSITE_M_OO_ENTRIES
                 and un["m_oo_free_symbols"] == M_OO_FREE_SYMBOLS and un["m_oo_row7_zero"] and un["m_oo_zero_on_star_line"]
                 and un["m_oo_ideal_is_star_line"] and un["block_identity_generic"] and un["sufficiency_everywhere"])
    checks.check("D-2", "THE NECESSITY HALF IS MEASURED, NOT ASSERTED FROM THE IDENTITY: at all 26 positive-definite witnesses (W1's moduli at the 16 star cells, the all-plus control and the flat cell; the curve moduli over QQ(sqrt 6) at the 8 rule-A cells) the radical of the coefficient ideal of det M - det B^2 is exactly the star line",
                 claims["union_necessity_measured"] and un["necessity_is_plane_everywhere"] == claims["union_necessity_plane"]
                 and claims["union_necessity_plane"]
                 and (un["witness_count"], un["rational_witness_count"], un["curve_witness_count"]) == UNION_WITNESS_COUNTS
                 and all(entry[0] == tuple(sorted(STAR_LINE)) for entry in un["table"].values()))
    checks.check("D-3", "ONE WITNESS IN EVERY GAUGE CLASS AMONG THE 16: the class representatives are the declared masks and each carries a rational union witness",
                 un["one_witness_per_class"] and un["class_representative_masks"] == CLASS_REPRESENTATIVE_MASKS)
    checks.check("E-1", "THE INTERSECTION WITH BLOCK 213's COINCIDENCE CELLS IS ALL 16: the star-pattern cells ARE the coincidence-curve cells; rule A iff (P_tx, P_ty, P_xy) = (+, -, +), rule B iff (-, +, -), and that pattern is -E_i E_j = E_k, the star's pair signs",
                 ce["intersection_count"] == claims["intersection_count"] == INTERSECTION_COUNT and ce["star_equals_curve"]
                 and ce["intersection_masks"] == STAR_MASKS and ce["rule_a_iff_star_pattern_plus"] and ce["rule_b_iff_star_pattern_minus"]
                 and ce["star_pattern_is_minus_e_i_e_j"] and ce["star_pair_signs_block215"] == STAR_PATTERN[0])
    checks.check("E-2", "THE POSITIVE SUBSET IS ALL 8 RULE-A CELLS, four in each mixed gauge class; the 8 rule-B star cells lie in the (+,+) and (-,-) classes, 3 face flips from the nearest rule-A cell",
                 ce["positive_subset_count"] == claims["positive_subset_count"] == POSITIVE_SUBSET_COUNT
                 and ce["positive_subset_masks"] == RULE_A_MASKS and ce["rule_a_classes"] == RULE_A_CLASSES and ce["rule_b_classes"] == RULE_B_CLASSES
                 and tuple(sorted((d, sum(1 for _, x in ce["star_to_rule_a_distance"] if x == d)) for d in {x for _, x in ce["star_to_rule_a_distance"]})) == STAR_TO_RULE_A_DISTANCES)
    checks.check("F-1", "THE COVARIANT WITNESS EXISTS AT EVERY ONE OF THE 8 RULE-A CELLS: positive definite, its strict stabiliser IS an S3_body (orders 1,2,2,2,3,3) so both shears are alive without any gauge, the star line is its parameter locus with no forced condition, and the cell with the parameters on the line is preserved",
                 claims["covariant_cell_exists"] and wi["witness_count"] == claims["covariant_witness_count"] == COVARIANT_WITNESS_COUNT
                 and wi["all_witnesses"]["positive_definite"] and wi["all_witnesses"]["stabiliser_is_s3_body"]
                 and wi["stabiliser_orders"] == STABILISER_ORDERS and wi["all_witnesses"]["strict_locus_is_star_line_alive"]
                 and wi["all_witnesses"]["preserved_on_line"])
    checks.check("F-2", "ONE METRIC'S CONE AT THE COVARIANT WITNESS: the two readings are proportional (mu = 32/27 in class (+,-), 27/32 in class (-,+)), the graded cone is one quadric squared, and det M = c (k^T G1 k)^4 on the star line with the multiple symbolic, c = 64/81 and 9/16 -- for every line multiple, and by the D07 congruence for every D07",
                 wi["all_witnesses"]["readings_proportional"] and wi["mu_per_class"] == MU_PER_CLASS
                 and wi["all_witnesses"]["graded_cone_is_one_quadric_squared"] and wi["all_witnesses"]["cone_on_line_is_one_metric_cone"]
                 and wi["cone_on_line_constants"] == claims["cone_on_line_constants"] == CONE_ON_LINE_CONSTANTS
                 and br["d07_congruence_M_symbolic_signs"])
    checks.check("G-1", "THE BRANCHES ON THE COVARIANT LINE at L+- and L-+ are the declared table: with the multiple symbolic all four pencil branches are k-free constants times k^T G1 k; at lam = 1/4 the constants {1, 128/99, 16/11 x2} and {1, 108/119, 144/119 x2}; with D07 = 1/4 the 0-form constant alone moves (128/119, 12/11)",
                 br["all_branches_k_free"] and all(br["table"][key] == value for key, value in claims["branch_table"].items()))
    checks.check("G-2", "THE TWO RESCALINGS: the line multiple rescales the top-form and transverse constants by 1/(1 - lam^2/(v0 v1)) (v0 v1 = 3/4, 8/9; 12/11 and 128/119 at lam = 1/4) and D07 rescales the 0-form constant by 1/(1 - D07^2 v1/v0) (v1/v0 = 9/8, 4/3; 128/119 and 12/11 at D07 = 1/4) -- Block 214's 128/119 re-measured on the covariant line",
                 all(br["table"][(name, "v0 v1")] == VOLUME_PRODUCTS[name] and br["table"][(name, "v1 / v0")] == VOLUME_RATIOS[name]
                     and br["table"][(name, "d07 rescale 1/4")] == claims["d07_rescale"][name] == D07_RESCALE[name]
                     and br["table"][(name, "line rescale 1/4")] == LINE_RESCALE[name] for name in ("L+-", "L-+"))
                 and sp.Rational(128, 119) == D07_RESCALE["L+-"] == b214.LOCUS_D07_RESCALE)
    checks.check("G-3", "THE D07 CONGRUENCE AT SYMBOLIC FACE SIGNS AND SYMBOLIC MODULI: U^T M U = M|_{D07 = 0} with U = I - (D07/D3) E_70, the H0 shift is -D07^2 v1 on the (0,0) entry and nothing else; holds at every star cell",
                 br["d07_congruence_M_symbolic_signs"] and br["d07_shift"] == claims["d07_shift"] == D07_SHIFT == b214.D07_SHIFT
                 and br["d07_shift_rest_zero"] and br["d07_congruence_holds_at_star_cells"])
    checks.check("G-4", "THE SYMBOL UNDER S3 AND UNDER A TWISTED ROTATION: Block 213's identity holds at every witness; the two quadrics and det B are invariant under kappa -> R kappa for exactly the strict S3; each quadric lies in the 2-dimensional S3-invariant space (the O-invariant space is 1-dimensional; the flat quadrics are |k|^2); the four body-diagonal axes occur; a twisted rotation maps det M to the gauged raising part's symbol (det B up to the twisted lift's sign) and det M moves",
                 sy["identity_everywhere"] and sy["invariance_is_exactly_s3_everywhere"] and sy["quadrics_in_s3_span_everywhere"]
                 and sy["invariant_dimensions"] == claims["invariant_dimensions"] == INVARIANT_DIMENSIONS and sy["axes"] == AXES
                 and sy["flat_quadrics_are_k2"] and sy["twist_count_order4"] == TWIST_COUNT_ORDER4 and sy["twisted_conjugation_identity"]
                 and sy["twisted_symbol_is_gauged_symbol"] and sy["twisted_block_is_gauged_block_up_to_sign"]
                 and sy["twisted_symbol_moves"] and sy["gauged_raising_differs"])
    checks.check("H-1", "SCOUT-GRADE FENCE, inherited verbatim from Blocks 211, 213, 214 and 215",
                 claims["scout_grade"] == SCOUT_GRADE_FENCE == b215.SCOUT_GRADE_FENCE and SCOUT_GRADE_ONLY)
    checks.check("H-2", "THE INSTANCE SCOPE IS ENUMERATED: six restrictions",
                 claims["instance_scope_count"] == len(INSTANCE_SCOPE) == 6)
    sc = scope_certificate(facts.note_text)
    checks.check("I-1", "THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY",
                 bool(facts.note_text) and sc["n5_verbatim"] == claims["n5_verbatim"] and claims["n5_verbatim"])
    checks.check("I-2", "NO nsimplify, NO float literal, NO float call in this runner's source",
                 nsimplify_occurrences() == 0 and float_literal_occurrences() == 0 and float_call_sites() == 0
                 and claims["float_absent"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("== BLOCK 216: the covariant curved cell and its cone -- measured facts ==")
    print(f"authority: {facts.authority}")
    for name in ("census", "covariance", "union", "witness", "branches", "symbol"):
        section = getattr(facts, name)
        for key in sorted(section, key=str):
            if key == "cells":
                continue
            value = section[key]
            if isinstance(value, dict):
                for inner in sorted(value, key=str):
                    print(f"{name} {key} {inner}: {value[inner]}")
            else:
                print(f"{name} {key}: {value}")
    print(f"timings_ms: {facts.timings}  elapsed_ms: {elapsed_ns // 1_000_000}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        for name in MUTATIONS:
            print(name)
        return 0
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()
    # Every measurement happens once, before any mutation flag is consulted.
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
