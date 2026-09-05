#!/usr/bin/env python3
"""BLOCK 217 -- THE OTHER ASSEMBLY AT THE COVARIANT CELLS, AND THE BENCH.

Block 216 found that at each of the 8 rule-A star-pattern cells Block 213's
curve point is a positive-definite cell that is strictly S3-covariant with
both shears alive, the star line its parameter locus, and carries one
metric's cone -- under the ONSITE assembly.  Block 215 found that the overlap
fold sees the four parameters only through s = D07 + D16 + D25 + D34 and that
strict covariance forces s = 0 only together with a shear relation
(g0 v0 v1 + g1 = 0 at all-plus) -- at the four class representatives.  Block
213 found the overlap cone a non-Hodge pair of cones at all-plus witnesses.
This runner computes EXACTLY, at the 8 rule-A cells with Block 216's curve
witnesses and at the all-plus and flat controls, under the OVERLAP assembly:

  (a) the fold's parameter dependence at SYMBOLIC face signs and moduli (a
      lemma at every cell: only s, parity block (s/4) P111, the two-flip
      couplings -(s_f0 g0 v0 v1 + s_f1 g1)/(4 v0)); the union locus in s;
      the strict and twisted stabilisers of the fold at s = 0 and at
      symbolic s; the strict shear relation at symbolic face signs under each
      cell's own S3_body, evaluated on the curve;
  (b) the overlap cone at the witnesses at s = 0 and at symbolic s -- its
      factorization type and its relation to the onsite cone;
  (c) Block 213's (4,2,2) bench at one covariant witness (L+-'s cell) and at
      the all-plus W1 control with the parameters on the star line at the
      numeric point 1/4, both assemblies, both readings, every multiset with
      Block 213's own consistency check (Bloch union = direct bench), exact
      over QQ(sqrt 6) and QQ(sqrt 6, i);
  (d) the small-k structure: the bench's nonzero Bloch point against the
      principal part at kappa = e_t, exactly, with no continuum reading.

  Nothing registered or adopted; no assembly, cell, subgroup, reading or
  parameter value selected; the covariance antecedent stays a reading; 'one
  metric's cone' names Block 213's exact statement and nothing physical; no
  continuum or light-cone reading of the bench.

Gate families: A authority, B banner/fences, C construction fidelity, D the
overlap loci, E the overlap cone, F the bench, G the small-k structure, H
scope, I note and hygiene.  Every measurement is taken once before any
mutation flag is read; exact arithmetic only -- no float, no nsimplify.
Scout-grade finite exact linear algebra on one cell form, not a spacetime and
not a dynamics.
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
from sympy.polys.matrices import DomainMatrix

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY: Block 216 (the
# census, the witnesses, the strict stabiliser) and through it Blocks 215,
# 214, 213, 211, 209.
try:
    import admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05 as b216
    B216_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b216 = None
    B216_IMPORT_LANDED = False
b215 = b216.b215 if b216 is not None else None
b214 = b216.b214 if b216 is not None else None
b213 = b216.b213 if b216 is not None else None
b211 = b216.b211 if b216 is not None else None
b209 = b216.b209 if b216 is not None else None
MACHINERY_IMPORT_LANDED = bool(B216_IMPORT_LANDED and b216 is not None and b216.MACHINERY_IMPORT_LANDED
                               and b215 is not None and b214 is not None and b213 is not None
                               and b211 is not None and b209 is not None)
# THE STACK PARENT'S TWO ARTIFACTS.  Block 216 is the commit this block is cut
# from AND its scientific parent; its note and runner exist at PARENT_COMMIT
# and NEITHER exists at STALE_PARENT_COMMIT, the Block 215 tip.
PARENT_NOTE = "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md"
PARENT_RUNNER = "scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py"
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "7b55a41befe0a90ba06c15122fee2f9ad07ed2d5",
    "a9429465498b23d06da568f7f7ed7a9d9bb0dddd",
)
FINAL_NOTE_NAME = "ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md"
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS (the cache parser AST-reads it).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_OVERLAP_ASSEMBLY_COVARIANT_CELLS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_COVARIANT_CURVED_CELL_CONE_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_covariant_curved_cell_cone_2026_09_05.py",
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
PARENT_REF = "origin/physics-loop/toe-axiom-closure-block216-covariant-curved-cell-cone-20260905"
PARENT_COMMIT = "fa610e595f47792beec65d246fda1c8993155fcc"
# The Block 215 tip: a real ancestor of HEAD carrying NEITHER Block 216 artifact.
STALE_PARENT_COMMIT = "d386a1be41ab8a26e9a4a2e5258f841bf1dbc2cc"
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
    "break_cell_census",
    "break_witness_reproduction",
    "break_fold_sees_sum",
    "break_flat_control",
    "break_union_locus_s",
    "break_strict_stabiliser",
    "break_twisted_stabiliser",
    "break_shear_relation",
    "claim_curve_satisfies_shear_relation",
    "break_overlap_cone_pair",
    "claim_overlap_cone_is_onsite_cone",
    "break_overlap_cone_symbolic_s",
    "break_bench_multisets",
    "break_bloch_equals_direct",
    "break_bench_control",
    "break_bench_reads_principal_part",
    "break_bloch_fold_sees_parameters",
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
    "break_cell_census": "C", "break_witness_reproduction": "C",
    "break_fold_sees_sum": "C", "break_flat_control": "C",
    "break_union_locus_s": "D", "break_strict_stabiliser": "D", "break_twisted_stabiliser": "D",
    "break_shear_relation": "D", "claim_curve_satisfies_shear_relation": "D",
    "break_overlap_cone_pair": "E", "claim_overlap_cone_is_onsite_cone": "E", "break_overlap_cone_symbolic_s": "E",
    "break_bench_multisets": "F", "break_bloch_equals_direct": "F", "break_bench_control": "F",
    "break_bench_reads_principal_part": "G", "break_bloch_fold_sees_parameters": "G",
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
    "Block 213's coincidence census, its curve witnesses L+- and L-+ over QQ(sqrt 6), its (4,2,2) bench and its Bloch reduction",
    "Block 214's principal part M = H0 D + D^T H0 under both assemblies, its plane and its union-locus statement in s at all-plus witnesses",
    "Block 215's corner action of the 24 proper rotations, its sign vectors and its overlap statements at the four class representatives",
    "Block 216's 16 star-pattern cells, its 8 rule-A covariant witnesses and their strict S3_body stabilisers under the onsite assembly",
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
READING_SELECTED_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
LIGHT_CONE_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("COVARIANCE", "CONE", "CELL", "ASSEMBLY", "BENCH")
AXIOM_COVARIANCE_CLAUSE = ("There is one fixed nearest-neighbor admissibility rule, covariant under lattice\n"
                           "translations and proper cubic rotations.")
READINGS = (
    "R1 the cell form inherits the Admissibility axiom's proper-cubic-rotation covariance (the antecedent; not established, not asserted)",
    "R2 the difference in covariance between the two assemblies at the covariant cells decides the assembly (not established: both are measured, neither is selected)",
    "R3 'one metric's cone' or 'a non-Hodge pair of cones' is a metric or a cone of anything physical (not established: Block 213's polynomial statements)",
    "R4 the (4,2,2) bench multisets are a dispersion law, a light cone or a continuum limit (not established: sixteen exact eigenvalues of one finite matrix at two Bloch points)",
    "R5 the overlap fold's twisted D4_face stabiliser is a symmetry of anything physical (not established: a matrix identity on one folded 8 x 8 matrix)",
    "R6 the covariant witness is a vacuum, a background or a spacetime (not established: a positive-definite point on one cell form)",
)
CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"

# the parameters, the moduli, the directions, the cells, the witnesses
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = b216.PARAMETER_SYMBOLS
A07, B16, C25, D34 = PARAMETER_SYMBOLS
G0, G1, V0, V1 = b216.MODULI
MODULI = (G0, G1, V0, V1)
KT, KX, KY = b216.KAPPA
KAPPA = (KT, KX, KY)
SUM = sp.Symbol("s")                      # Block 215's overlap sum s = D07 + D16 + D25 + D34
LAM = b213.LAM
FACE_ORDER = b211.GAUGE_FACE_ORDER        # (tx0, ty0, xy0, tx1, ty1, xy1)
FACE_NAMES = ("tx", "ty", "xy")
SIGNATURE = sp.diag(1, -1, 1)             # Block 213's E on (t, x, y)
QUARTER = sp.Rational(1, 4)
BENCH_EXTENT = (4, 2, 2)                  # Block 213's three-direction bench
LINE_POINT = (sp.Integer(0), QUARTER, -QUARTER, QUARTER)   # (D07, D16, D25, D34) on the star line at 1/4
ALL_PLUS_CELL = b216.ALL_PLUS_CELL
W1_MODULI = b216.W1_MODULI                # (v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4)
FLAT_MODULI = b216.FLAT_MODULI
GAUGE_CLASSES = b216.GAUGE_CLASSES

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
    return b216.sign_dict(values)


def formal(values: tuple, moduli: tuple, params: tuple) -> sp.Matrix:
    """Block 214's formal_cell at a face-sign cell (moduli as (g0, g1, v0, v1))."""
    return b216.formal(values, moduli, params)


def curve_moduli(pi0: int) -> tuple:
    """Block 213's curve point (v0, g0, v1, g1): L+-'s for pi0 = +1, L-+'s for pi0 = -1."""
    return b216.curve_moduli(pi0)


def moduli_as_g(moduli: tuple) -> tuple:
    return b216.moduli_as_g(moduli)


def rule_a_cells(census: dict) -> tuple:
    return tuple(v for v in b216.star_cells(census) if census["cells"][v]["rule_a"])


def overlap_fold(cell_s: sp.Matrix) -> tuple:
    """(H0(s), M(s)) of the overlap assembly for a cell carrying (s, 0, 0, 0)."""
    h0, m, _ = b214.principal_part(cell_s, "overlap")
    return h0, m


# ---------------------------------------------------------------------------
# C. THE FOLD AT SYMBOLIC FACE SIGNS AND SYMBOLIC MODULI (a lemma at every cell)
# ---------------------------------------------------------------------------
SIGN_SYMBOLS = sp.symbols("s_tx0 s_ty0 s_xy0 s_tx1 s_ty1 s_xy1")


def generic_cell(params: tuple) -> sp.Matrix:
    return b214.formal_cell(dict(zip(FACE_ORDER, SIGN_SYMBOLS)), G0, G1, V0, V1, params)


def measure_fold() -> dict:
    """The overlap fold H0 at symbolic face signs, moduli and parameters: it
    depends on the parameters only through s (Block 215's F-1, now a lemma at
    every cell), its parity block is (s/4) P111, and at s = 0 it is h0 I plus
    the two-flip couplings; the flat cell gives H = I at zero parameters under
    both assemblies; the overlap Bloch fold at z = (i, 1, 1) is parameter-free."""
    facts: dict = {}
    h_full, _ = overlap_fold(generic_cell(PARAMETER_SYMBOLS))
    h_s, _ = overlap_fold(generic_cell((SUM, 0, 0, 0)))
    facts["fold_sees_sum_only_symbolic_signs"] = residual_count(
        (h_full - h_s.subs(SUM, sum(PARAMETER_SYMBOLS))).applyfunc(sp.expand)) == 0
    even, odd = b213.even_odd(3)
    p111 = b214.hodge_complement_permutation()
    facts["parity_block_is_sum_over_four_p111"] = residual_count(
        (h_s.extract(even, odd) - SUM / 4 * p111.extract(even, odd)).applyfunc(sp.expand)) == 0
    facts["fold_linear_in_s"] = all(sp.Poly(sp.expand(x), SUM).degree() <= 1 for x in h_s if x != 0)
    h_zero = h_s.subs(SUM, 0)
    facts["fold_zero_free_symbols"] = tuple(sorted(str(x) for x in h_zero.free_symbols))
    facts["fold_diagonal"] = str(sp.factor(h_zero[0, 0]))
    facts["fold_diagonal_scalar"] = all(sp.cancel(h_zero[i, i] - h_zero[0, 0]) == 0 for i in range(8))
    couplings: dict = {}
    for i in range(8):
        for j in range(i + 1, 8):
            if h_zero[i, j] != 0:
                couplings[(i, j)] = str(sp.factor(h_zero[i, j]))
    facts["couplings"] = couplings
    facts["coupling_count"] = len(couplings)
    facts["coupling_literals"] = tuple(sorted(set(couplings.values())))
    # every coupling joins a two-flip pair (corners differing in exactly two coordinates)
    facts["couplings_are_two_flip_pairs"] = all(
        sum(1 for a, b in zip(b209.CORNERS[i], b209.CORNERS[j]) if a != b) == 2 for (i, j) in couplings)
    # the flat control: both assemblies give the identity at zero parameters; the flat fold is I + (s/4) P111
    flat = formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), (0, 0, 0, 0))
    h_on, _, _ = b214.principal_part(flat, "onsite")
    h_ov, _, _ = b214.principal_part(flat, "overlap")
    facts["flat_both_assemblies_identity"] = residual_count(h_on - sp.eye(8)) == 0 and residual_count(h_ov - sp.eye(8)) == 0
    flat_s, _ = overlap_fold(formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), (SUM, 0, 0, 0)))
    facts["flat_fold_is_identity_plus_sum_p111"] = residual_count((flat_s - sp.eye(8) - SUM / 4 * p111).applyfunc(sp.expand)) == 0
    # the overlap Bloch fold at the bench's nonzero point z = (i, 1, 1), symbolic everything: parameter-free
    rules = b213.overlap_rules(generic_cell(PARAMETER_SYMBOLS), b209.CORNERS, 3)
    bloch_i = b213.bloch_matrix(rules, (sp.I, 1, 1), 3)
    facts["bloch_fold_at_i_parameter_free"] = not (bloch_i.free_symbols & set(PARAMETER_SYMBOLS))
    facts["bloch_momenta"] = tuple(tuple(str(x) for x in z) for z in b213.bench_momenta(BENCH_EXTENT))
    return facts


# ---------------------------------------------------------------------------
# D. THE LOCI: stabilisers of the fold at s = 0 and at symbolic s, the shear
# relation at symbolic signs, the union locus in s
# ---------------------------------------------------------------------------
def s_locus(h_sym: sp.Matrix, lift: sp.Matrix, e: tuple) -> tuple:
    """(feasible, forced) for T = E L on a fold linear in s: infeasible when an
    entry of T H T^T - H is a nonzero constant, else the forced locus in s."""
    t = sp.diag(*e) * lift
    residual = (t * h_sym * t.T - h_sym).applyfunc(sp.radsimp)
    forced = set()
    for i in range(8):
        for j in range(i, 8):
            x = sp.expand(residual[i, j])
            if x == 0:
                continue
            if sp.Poly(x, SUM).degree() == 0:
                return (False, None)
            forced.add("s")
    return (True, tuple(sorted(forced)))


def stabilisers_in_s(h_sym: sp.Matrix, lifts: tuple) -> tuple:
    """(strict, twisted): rotation -> forced loci in s, over E = 1 and over all 64 sign vectors."""
    strict, twisted = {}, {}
    for g in range(24):
        ok, forced = s_locus(h_sym, lifts[g], (1,) * 8)
        if ok:
            strict[g] = forced
        loci = set()
        for e in b215.sign_vectors():
            ok, forced = s_locus(h_sym, lifts[g], e)
            if ok:
                loci.add(forced)
        if loci:
            twisted[g] = tuple(sorted(loci))
    return strict, twisted


def forced_conditions(h: sp.Matrix, lift: sp.Matrix) -> tuple:
    """The moduli conditions forced by L H L^T = H at symbolic moduli: the
    non-volume factors of every nonzero entry's numerator (the volumes are
    nonzero on Block 211's domain)."""
    out = set()
    residual = (lift * h * lift.T - h).applyfunc(sp.cancel)
    for i in range(8):
        for j in range(i, 8):
            entry = residual[i, j]
            if entry == 0:
                continue
            numerator, _ = sp.fraction(sp.factor(entry))
            _, factors = sp.factor_list(numerator)
            out.add(tuple(sorted(str(base) for base, _ in factors if base.free_symbols and base not in (V0, V1))))
    return tuple(sorted(out))


def union_locus_s(m_s: sp.Matrix, gaussian: bool) -> tuple:
    """(radical generators in s of the coefficient ideal of det M - det B^2,
    deg_s det M, deg_s det B, det M, det B) for the overlap principal part."""
    even, odd = b213.even_odd(3)
    det_m = sp.expand(b214.ff_det(m_s, (SUM,) + KAPPA, algebraic=gaussian))
    det_b = sp.expand(sp.radsimp(m_s.extract(even, odd).det(method="berkowitz")))
    difference = sp.expand(sp.radsimp(det_m - det_b ** 2))
    if gaussian:
        r = sp.Symbol("r")
        coefficients = sp.Poly(difference.subs(sp.sqrt(6), r), *KAPPA).coeffs() + [r ** 2 - 6]
        basis = sp.groebner(coefficients, SUM, r, order="lex")
        generators = b214.reduced_generators(basis.exprs, (SUM,), r)
    else:
        generators = b214.radical_generators(b214.coefficient_ideal(difference, KAPPA, (SUM,)), (SUM,))
    return (tuple(str(g) for g in generators), sp.Poly(det_m, SUM).degree(), sp.Poly(det_b, SUM).degree(), det_m, det_b)


def class_name_of(group: dict, members: tuple) -> str:
    target = frozenset(members)
    for name, cls in group["classes"].items():
        if any(frozenset(member) == target for member in cls):
            return name
    return "NONE"


def rotation_axis(rotation: sp.Matrix) -> tuple:
    space = (rotation - sp.eye(3)).nullspace()
    if len(space) != 1:
        return ()
    axis = space[0] / sp.gcd(list(space[0]))
    return tuple(axis)


def measure_loci(group: dict, census: dict) -> dict:
    """D: at each rule-A cell with Block 216's curve witness, and at the all-plus
    W1 and flat controls: the onsite strict stabiliser (Block 216's S3_body),
    the overlap fold's strict and twisted stabilisers at symbolic s (feasible
    rotations and the locus in s each forces), the shear relation at symbolic
    moduli under the cell's own S3_body, its value on the curve, the union
    locus in s and the degrees of det M and det B in s."""
    lifts, rots, orders = group["lifts"], group["rotations"], group["orders"]
    fold_generic_zero, _ = overlap_fold(generic_cell((0, 0, 0, 0)))
    table: dict = {}
    witnesses = [(census["cells"][v]["mask"], v, curve_moduli(census["cells"][v]["class"][0]), True)
                 for v in rule_a_cells(census)]
    witnesses += [("W1", ALL_PLUS_CELL, W1_MODULI, False), ("flat", ALL_PLUS_CELL, FLAT_MODULI, False)]
    for key, values, moduli, gaussian in witnesses:
        print(f"[loci] witness {key}", file=sys.stderr)
        v0, g0, v1, g1 = moduli
        entry: dict = {"class": census["cells"][values]["class"], "moduli": moduli}
        onsite_zero = formal(values, moduli_as_g(moduli), (0, 0, 0, 0))
        onsite_stab = b216.strict_stabiliser(onsite_zero, lifts)
        entry["onsite_stabiliser"] = onsite_stab
        entry["onsite_stabiliser_class"] = class_name_of(group, onsite_stab)
        h_s, m_s = overlap_fold(formal(values, moduli_as_g(moduli), (SUM, 0, 0, 0)))
        entry["fold_linear_in_s"] = all(sp.Poly(sp.expand(x), SUM).degree() <= 1 for x in h_s if x != 0)
        strict, twisted = stabilisers_in_s(h_s, lifts)
        entry["strict_feasible"] = tuple(sorted(strict))
        entry["strict_all_s"] = tuple(sorted(g for g, f in strict.items() if f == ()))
        entry["strict_only_at_zero"] = tuple(sorted(g for g, f in strict.items() if f == ("s",)))
        entry["twisted_feasible"] = tuple(sorted(twisted))
        entry["twisted_all_s"] = tuple(sorted(g for g, loci in twisted.items() if () in loci))
        entry["twisted_class"] = class_name_of(group, entry["twisted_all_s"])
        entry["twisted_axes"] = tuple(sorted(set(rotation_axis(rots[g]) for g in entry["twisted_all_s"] if orders[g] == 4)))
        common = tuple(sorted(set(onsite_stab) & set(entry["twisted_all_s"])))
        entry["common_with_onsite"] = common
        entry["common_class"] = class_name_of(group, common)
        entry["s3_in_twisted"] = set(onsite_stab) <= set(entry["twisted_all_s"])
        # the shear relation at SYMBOLIC moduli at this cell's signs, under the onsite stabiliser
        fold_cell = fold_generic_zero.subs(dict(zip(SIGN_SYMBOLS, values)))
        forced = {g: forced_conditions(fold_cell, lifts[g]) for g in onsite_stab if orders[g] > 1}
        entry["forced_by_order"] = tuple(sorted(set((orders[g], f) for g, f in forced.items())))
        entry["forced_union"] = tuple(sorted(set(itertools.chain.from_iterable(
            itertools.chain.from_iterable(f) for f in forced.values()))))
        entry["shear_relation_plus"] = sp.radsimp(g0 * v0 * v1 + g1)
        entry["shear_relation_minus"] = sp.radsimp(g0 * v0 * v1 - g1)
        entry["volume_product"] = sp.radsimp(v0 * v1)
        entry["shears_nonzero"] = g0 != 0 and g1 != 0
        generators, deg_m, deg_b, _, _ = union_locus_s(m_s, gaussian)
        entry["union_locus"], entry["det_m_degree_s"], entry["det_b_degree_s"] = generators, deg_m, deg_b
        table[key] = entry
    facts: dict = {"table": table}
    rule_keys = [k for k in table if isinstance(k, int)]
    facts["rule_a_count"] = len(rule_keys)
    facts["onsite_stabiliser_is_s3_everywhere"] = all(table[k]["onsite_stabiliser_class"] == "S3_body" for k in rule_keys)
    facts["overlap_strict_trivial_everywhere"] = all(table[k]["strict_feasible"] == (0,) for k in rule_keys)
    facts["overlap_twisted_classes"] = tuple(sorted(set(table[k]["twisted_class"] for k in rule_keys)))
    facts["overlap_twisted_is_all_s"] = all(table[k]["twisted_feasible"] == table[k]["twisted_all_s"] for k in rule_keys)
    facts["overlap_twisted_orders"] = tuple(sorted(set(len(table[k]["twisted_all_s"]) for k in rule_keys)))
    facts["overlap_twisted_axes"] = tuple(sorted(set(table[k]["twisted_axes"] for k in rule_keys)))
    facts["common_classes"] = tuple(sorted(set(table[k]["common_class"] for k in rule_keys)))
    facts["s3_in_twisted_anywhere"] = any(table[k]["s3_in_twisted"] for k in rule_keys)
    facts["forced_by_order"] = tuple(sorted(set(table[k]["forced_by_order"] for k in rule_keys)))
    facts["forced_union"] = tuple(sorted(set(table[k]["forced_union"] for k in rule_keys)))
    facts["shear_relations_on_curve"] = {key: tuple(sorted(set((table[k]["shear_relation_plus"], table[k]["shear_relation_minus"])
                                                              for k in rule_keys if table[k]["class"] == key)))
                                         for key in ((1, -1), (-1, 1))}
    facts["curve_violates_every_relation"] = all(table[k]["shear_relation_plus"] != 0 and table[k]["shear_relation_minus"] != 0
                                                 and table[k]["shears_nonzero"] for k in rule_keys)
    facts["union_locus_everywhere"] = tuple(sorted(set(table[k]["union_locus"] for k in table)))
    facts["det_degrees_s"] = tuple(sorted(set((table[k]["det_m_degree_s"], table[k]["det_b_degree_s"]) for k in table)))
    facts["witness_count"] = len(table)
    facts["w1_twisted_class"] = table["W1"]["twisted_class"]
    facts["w1_strict_feasible"] = table["W1"]["strict_feasible"]
    facts["flat_strict_all_s_class"] = class_name_of(group, table["flat"]["strict_all_s"])
    facts["flat_strict_only_at_zero_count"] = len(table["flat"]["strict_only_at_zero"])
    facts["flat_twisted_class"] = table["flat"]["twisted_class"]
    return facts


# ---------------------------------------------------------------------------
# E. THE OVERLAP CONE at the witnesses: s = 0 and symbolic s, against the onsite cone
# ---------------------------------------------------------------------------
def quadric_coefficients(quadric) -> tuple:
    """(c_xx, |c_tx|, |c_ty|, |c_xy|) of a quadric normalised to kt^2 + ... + ky^2."""
    poly = sp.Poly(sp.expand(quadric), *KAPPA)
    lead = poly.coeff_monomial(KT ** 2)
    norm = lambda m: sp.radsimp(poly.coeff_monomial(m) / lead)
    return (norm(KX ** 2), sp.Abs(norm(KT * KX)), sp.Abs(norm(KT * KY)), sp.Abs(norm(KX * KY)), norm(KY ** 2))


def measure_cone(census: dict) -> dict:
    facts: dict = {}
    table: dict = {}
    even, odd = b213.even_odd(3)
    witnesses = [(census["cells"][v]["mask"], v, curve_moduli(census["cells"][v]["class"][0]), True)
                 for v in rule_a_cells(census)]
    witnesses += [("W1", ALL_PLUS_CELL, W1_MODULI, False), ("flat", ALL_PLUS_CELL, FLAT_MODULI, False)]
    for key, values, moduli, gaussian in witnesses:
        print(f"[cone] witness {key}", file=sys.stderr)
        entry: dict = {"class": census["cells"][values]["class"]}
        _, m_s = overlap_fold(formal(values, moduli_as_g(moduli), (SUM, 0, 0, 0)))
        det_m = sp.expand(b214.ff_det(m_s, (SUM,) + KAPPA, algebraic=gaussian))
        det_b0 = sp.expand(sp.radsimp(m_s.extract(even, odd).det(method="berkowitz")))
        entry["det_m_zero_is_det_b_squared"] = is_zero_alg(det_m.subs(SUM, 0) - det_b0 ** 2)
        extension = {"extension": sp.sqrt(6)} if gaussian else {}
        _, factors = sp.factor_list(det_m, SUM, *KAPPA, **extension)
        entry["det_m_shape"] = tuple(sorted((sp.Poly(b, SUM, *KAPPA).degree_list(), p) for b, p in factors
                                            if b.free_symbols & set(KAPPA)))
        _, factors0 = sp.factor_list(det_b0, *KAPPA, **extension)
        quadrics = [sp.expand(b) for b, p in factors0 if b.free_symbols & set(KAPPA)]
        entry["det_b_zero_shape"] = tuple(sorted((sp.Poly(b, *KAPPA).total_degree(), p) for b, p in factors0
                                                 if b.free_symbols & set(KAPPA)))
        onsite_zero = formal(values, moduli_as_g(moduli), (0, 0, 0, 0))
        g1_m = b213.metric_candidates(onsite_zero)[0].applyfunc(sp.radsimp)
        form = b213.quadratic_form(g1_m, KAPPA)
        entry["det_b_zero_is_onsite_cone"] = b213.proportional(det_b0, form ** 2, KAPPA)
        entry["quadrics_proportional_to_onsite"] = tuple(b213.proportional(q, form, KAPPA) for q in quadrics)
        entry["quadrics_rational"] = all(not q.has(sp.sqrt(6)) for q in quadrics)
        if len(quadrics) == 2:
            entry["pair_proportional"] = b213.proportional(quadrics[0], quadrics[1], KAPPA)
            entry["pair_related_by_ky_flip"] = (is_zero_alg(quadrics[0].subs(KY, -KY) - quadrics[1])
                                                or is_zero_alg(quadrics[0].subs(KY, -KY) + quadrics[1]))
            entry["coefficients"] = quadric_coefficients(quadrics[0])
        table[key] = entry
    facts["table"] = table
    rule_keys = [k for k in table if isinstance(k, int)]
    facts["det_m_zero_is_det_b_squared_everywhere"] = all(e["det_m_zero_is_det_b_squared"] for e in table.values())
    facts["det_m_shapes"] = tuple(sorted(set(e["det_m_shape"] for e in table.values())))
    facts["det_b_zero_shapes_rule_a"] = tuple(sorted(set(table[k]["det_b_zero_shape"] for k in rule_keys)))
    facts["det_b_zero_shape_w1"] = table["W1"]["det_b_zero_shape"]
    facts["det_b_zero_shape_flat"] = table["flat"]["det_b_zero_shape"]
    facts["overlap_cone_is_onsite_cone_anywhere"] = any(table[k]["det_b_zero_is_onsite_cone"] for k in rule_keys)
    facts["quadric_proportional_to_onsite_anywhere"] = any(any(table[k]["quadrics_proportional_to_onsite"]) for k in rule_keys)
    facts["pair_distinct_everywhere"] = all(not table[k]["pair_proportional"] for k in rule_keys)
    facts["pair_ky_flip_everywhere"] = all(table[k]["pair_related_by_ky_flip"] for k in rule_keys)
    facts["quadrics_rational_everywhere"] = all(table[k]["quadrics_rational"] for k in rule_keys)
    facts["coefficients_per_class"] = {key: tuple(sorted(set(table[k]["coefficients"] for k in rule_keys if table[k]["class"] == key)))
                                       for key in ((1, -1), (-1, 1))}
    return facts


# ---------------------------------------------------------------------------
# F/G. THE BENCH over QQ(sqrt 6) and QQ(sqrt 6, i): Block 213's (4,2,2), both
# assemblies, both readings, Bloch union = direct, and the principal part at e_t
# ---------------------------------------------------------------------------
def alg_charpoly(matrix: DomainMatrix, domain):
    coefficients = matrix.charpoly()
    return sp.expand(sum(domain.to_sympy(c) * LAM ** (len(coefficients) - 1 - k) for k, c in enumerate(coefficients)))


def symbol_matrix(hodge: DomainMatrix, raising: DomainMatrix, raising_t: DomainMatrix, reading: str) -> DomainMatrix:
    """Block 213's domain_symbol: -K^2 (form) or -(d - H^-1 d^T H)^2 (pencil)."""
    if reading == "form":
        kernel = hodge * raising - raising_t * hodge
        return -(kernel * kernel)
    operator = raising - hodge.inv() * raising_t * hodge
    return -(operator * operator)


def bench_charpolys(cell: sp.Matrix, assembly: str, reading: str) -> tuple:
    """(direct 16 x 16 bench charpoly over QQ(sqrt 6), Bloch union over
    QQ(sqrt 6, i) at Block 213's bench momenta, seconds direct, seconds union)."""
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    raising = b213.raising_rules(b213.lane_rules(3))
    real_field = QQ.algebraic_field(sp.sqrt(6))
    complex_field = QQ.algebraic_field(sp.sqrt(6), sp.I)
    started = time.monotonic_ns()
    hodge = DomainMatrix.from_Matrix(b213.bench_matrix(rules, BENCH_EXTENT)).convert_to(real_field)
    lifted = DomainMatrix.from_Matrix(b213.bench_matrix(raising, BENCH_EXTENT)).convert_to(real_field)
    direct = alg_charpoly(symbol_matrix(hodge, lifted, lifted.transpose(), reading), real_field)
    direct_ms = (time.monotonic_ns() - started) // 1_000_000
    started = time.monotonic_ns()
    product = sp.Integer(1)
    transposed = b213.transpose_rules(raising)
    for z in b213.bench_momenta(BENCH_EXTENT):
        h_b = DomainMatrix.from_Matrix(b213.bloch_matrix(rules, z, 3)).convert_to(complex_field)
        d_b = DomainMatrix.from_Matrix(b213.bloch_matrix(raising, z, 3)).convert_to(complex_field)
        dt_b = DomainMatrix.from_Matrix(b213.bloch_matrix(transposed, z, 3)).convert_to(complex_field)
        product *= alg_charpoly(symbol_matrix(h_b, d_b, dt_b, reading), complex_field)
    union = sp.expand(product)
    return direct, union, direct_ms, (time.monotonic_ns() - started) // 1_000_000


def charpoly_shape(charpoly) -> tuple:
    """Every irreducible factor over QQ as (degree, multiplicity, primitive integer coefficients)."""
    _, factors = sp.factor_list(sp.expand(charpoly), LAM)
    out = []
    for base, power in factors:
        poly = sp.Poly(base, LAM)
        coefficients = tuple(poly.all_coeffs())
        if coefficients[0] < 0:
            coefficients = tuple(-c for c in coefficients)
        out.append((poly.degree(), power, coefficients))
    return tuple(sorted(out))


def bench_cells(census: dict) -> dict:
    """The bench cells: L+-'s own cell (mask 2) at the curve moduli, the all-plus
    W1 control and the flat cell, each with the parameters at the line point;
    the first two also at zero parameters (for the overlap comparison)."""
    witness = next(v for v in rule_a_cells(census) if census["cells"][v]["mask"] == 2)
    return {
        "witness line": formal(witness, moduli_as_g(curve_moduli(1)), LINE_POINT),
        "W1 line": formal(ALL_PLUS_CELL, moduli_as_g(W1_MODULI), LINE_POINT),
        "flat line": formal(ALL_PLUS_CELL, moduli_as_g(FLAT_MODULI), LINE_POINT),
        "witness zero": formal(witness, moduli_as_g(curve_moduli(1)), (0, 0, 0, 0)),
        "W1 zero": formal(ALL_PLUS_CELL, moduli_as_g(W1_MODULI), (0, 0, 0, 0)),
    }


def measure_bench(cells: dict) -> dict:
    """F: every (cell, assembly, reading) charpoly of degree 16 on (4,2,2):
    Bloch union = direct bench, the multiset (or the factor shape when a root
    is irrational), the two timings."""
    facts: dict = {}
    table: dict = {}
    for label, cell in cells.items():
        assemblies = ("onsite", "overlap") if label.endswith("line") else ("overlap",)
        for assembly in assemblies:
            for reading in ("form", "pencil"):
                print(f"[bench] {label} {assembly} {reading}", file=sys.stderr)
                direct, union, direct_ms, union_ms = bench_charpolys(cell, assembly, reading)
                table[(label, assembly, reading)] = {
                    "agree": sp.expand(direct - union) == 0, "multiset": b213.multiset_of(direct),
                    "shape": charpoly_shape(direct), "degree": sp.Poly(direct, LAM).degree(),
                    "direct_ms": direct_ms, "union_ms": union_ms, "charpoly": direct,
                }
    facts["table"] = table
    facts["charpoly_count"] = len(table)
    facts["all_agree"] = all(e["agree"] for e in table.values())
    facts["all_degree_16"] = all(e["degree"] == 16 for e in table.values())
    facts["multisets"] = {key: e["multiset"] for key, e in table.items()}
    facts["shapes"] = {key: e["shape"] for key, e in table.items()}
    facts["overlap_line_equals_zero"] = all(
        table[(f"{c} line", "overlap", r)]["charpoly"] == table[(f"{c} zero", "overlap", r)]["charpoly"]
        for c in ("witness", "W1") for r in ("form", "pencil"))
    facts["overlap_pencil_is_r5_everywhere"] = all(
        e["multiset"] == ((0, 8), (1, 8)) for key, e in table.items() if key[1] == "overlap" and key[2] == "pencil")
    facts["timings_ms"] = {key: (e["direct_ms"], e["union_ms"]) for key, e in table.items()}
    return facts


def principal_charpoly_at_et(cell: sp.Matrix, assembly: str, reading: str):
    """The charpoly of the principal symbol at kappa = e_t: (H0^-1 M)^2 (pencil) or M^2 (form)."""
    h0, m, _ = b214.principal_part(cell, assembly)
    if reading == "pencil":
        operator = (h0.inv() * m).applyfunc(sp.radsimp)
        squared = (operator * operator).applyfunc(sp.radsimp)
    else:
        squared = (m * m).applyfunc(sp.expand)
    at_et = squared.subs({KT: 1, KX: 0, KY: 0})
    field = QQ.algebraic_field(sp.sqrt(6))
    return alg_charpoly(DomainMatrix.from_Matrix(at_et).convert_to(field), field)


def measure_smallk(cells: dict, bench: dict) -> dict:
    """G: the bench against the principal part at kappa = e_t -- the pencil
    bench charpoly equals lam^8 times the charpoly of (H0^-1 M(e_t))^2 under
    the onsite assembly (an exact identity, not a limit), the witness reading
    G1_tt times Block 216's four branch constants on the line; the identity
    fails for the form reading and for the overlap assembly, whose Bloch fold
    at z = (i, 1, 1) is parameter-free and differs from H0."""
    facts: dict = {}
    table: dict = {}
    for label in ("witness line", "W1 line", "flat line"):
        for assembly in ("onsite", "overlap"):
            for reading in ("form", "pencil"):
                principal = principal_charpoly_at_et(cells[label], assembly, reading)
                table[(label, assembly, reading)] = sp.expand(bench["table"][(label, assembly, reading)]["charpoly"] - LAM ** 8 * principal) == 0
    facts["identity_table"] = table
    facts["onsite_pencil_identity_everywhere"] = all(table[(l, "onsite", "pencil")] for l in ("witness line", "W1 line", "flat line"))
    facts["identity_fails_form_and_overlap"] = not any(v for key, v in table.items() if key[1] == "overlap" or key[2] == "form")
    # the witness reads G1_tt times the four branch constants of Block 216's line-1/4 table
    g1_m = b213.metric_candidates(cells["witness zero"])[0].applyfunc(sp.radsimp)
    g1_tt = sp.radsimp(g1_m[0, 0])
    facts["g1_tt_witness"] = g1_tt
    constants = []
    for ratio, power, _ in b216.BRANCH_TABLE[("L+-", "line 1/4")][0]:
        constants += [sp.Rational(ratio)] * power
    predicted = tuple(sorted(((sp.radsimp(g1_tt * c), 2 * constants.count(c) // 1) for c in set(constants)), key=lambda t: t[0]))
    predicted = tuple((value, sum(2 for c in constants if sp.radsimp(g1_tt * c) == value) // 2) for value, _ in predicted)
    bench_multiset = bench["table"][("witness line", "onsite", "pencil")]["multiset"]
    facts["witness_multiset_is_g1tt_times_constants"] = bench_multiset == ((0, 8),) + tuple((v, 2 * n // 2 * 2 // 2) for v, n in predicted) \
        and bench_multiset is not None
    facts["predicted_nonzero"] = predicted
    # the overlap Bloch fold at the bench's nonzero point versus the fold at s = 0, at the witness
    rules = b213.overlap_rules(cells["witness line"], b209.CORNERS, 3)
    bloch_i = b213.bloch_matrix(rules, (sp.I, 1, 1), 3)
    h_zero, _, _ = b214.principal_part(cells["witness zero"], "overlap")
    facts["bloch_fold_differs_from_h0_entries"] = residual_count((bloch_i - h_zero).applyfunc(sp.expand))
    facts["bloch_fold_parameter_free_at_witness"] = residual_count((bloch_i - b213.bloch_matrix(
        b213.overlap_rules(cells["witness zero"], b209.CORNERS, 3), (sp.I, 1, 1), 3)).applyfunc(sp.expand)) == 0
    # the onsite cone at kappa = e_t is a number: det M(e_t) = c G1_tt^4 (Block 216's constant), no zero
    h0, m, _ = b214.principal_part(cells["witness line"], "onsite")
    det_et = sp.radsimp(b214.ff_det(m.subs({KT: 1, KX: 0, KY: 0}), (), algebraic=True))
    facts["onsite_cone_at_et"] = sp.radsimp(det_et / g1_tt ** 4)
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    group: dict
    census: dict
    fold: dict
    loci: dict
    cone: dict
    bench: dict
    smallk: dict
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
    census = b216.measure_census()
    lap("census")
    fold = measure_fold()
    lap("fold")
    loci = measure_loci(group, census)
    lap("loci")
    cone = measure_cone(census)
    lap("cone")
    cells = bench_cells(census)
    bench = measure_bench(cells)
    lap("bench")
    smallk = measure_smallk(cells, bench)
    lap("smallk")
    axiom_text = (ROOT / AXIOM_PATH).read_text(encoding="utf-8") if (ROOT / AXIOM_PATH).is_file() else ""
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, group, census, fold, loci, cone, bench, smallk, axiom_text, note_text, timings)
