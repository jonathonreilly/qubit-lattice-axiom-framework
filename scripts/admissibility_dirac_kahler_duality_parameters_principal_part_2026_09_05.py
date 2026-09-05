#!/usr/bin/env python3
"""BLOCK 214 -- THE DUALITY PARAMETERS AND THE PRINCIPAL PART.

Block 211 solves the six-face system at every compatible moduli point with
exactly four free duality parameters D07, D16, D25, D34 (each pairing a corner
with its Hodge complement).  Block 213 proved its graded-cone theorem at the
degree-diagonal representative D07 = D16 = D25 = D34 = 0 and its refuting
checker showed that W1 with D16 = 1/4 breaks grade parity of the folded H0 and
replaces the union of the two Hodge cones by an irreducible quartic squared.
This runner determines EXACTLY, on the four-parameter cell form imported
through Block 213's machinery (read-only), what the parameters do to the
principal part M = H0 D + D^T H0 of the period-2 Bloch expansion:

  the parity-breaking mechanism (which corner pairs each parameter couples and
  why D07 is congruent to zero while D16, D25, D34 are not), the exact locus in
  the parameters where det M stops being det B^2 (the union of the two Hodge
  cones), the factorization type off it, the fate of Block 213's coincidence
  locus, the pencil branches with a parameter on, the deformed flat cell, and
  the shear/volume registration under the parameters.

Gate families: A authority, B banner and fences, C construction fidelity,
D the control, E the bench witnesses, F the lemmas, G registration, H scope
fences, I note and hygiene.  Every measurement is taken once before any
mutation flag is read; exact arithmetic only -- no float, no nsimplify.
Scout-grade finite exact linear algebra on one cell form, not a spacetime and
not a dynamics.  Nothing is registered and nothing is adopted.
"""
from __future__ import annotations

import argparse
import ast
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

# THE MACHINERY IMPORT, LANDED IN THIS BRANCH AND READ-ONLY: Block 213's runner
# carries the period-2 operator machinery, the two assemblies, the metric
# candidates, the witness tables and, through it, Blocks 201, 211, 209 and 105.
try:
    import admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05 as b213
    B213_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b213 = None
    B213_IMPORT_LANDED = False
b211 = b213.b211 if b213 is not None else None
b209 = b213.b209 if b213 is not None else None
MACHINERY_IMPORT_LANDED = bool(B213_IMPORT_LANDED and b213 is not None
                               and b213.MACHINERY_IMPORT_LANDED
                               and b211 is not None and b209 is not None)

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_"
    "THEOREM_NOTE_2026-09-05.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 213 is the commit this block is cut
# from AND its scientific parent; its note and runner exist at PARENT_COMMIT
# and NEITHER exists at STALE_PARENT_COMMIT, the Block 212 tip.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_"
    "THEOREM_NOTE_2026-09-05.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_"
    "2026_09_05.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "07acf91561b76946587787b58918e1b8dd03575e",
    "e708803abd3539187dd00f5c088abc96f838dc59",
)

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS (the cache parser AST-reads it).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SIX_FACE_POSITIVITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-27.md",
    "scripts/admissibility_dirac_kahler_six_face_positivity_classification_2026_08_27.py",
    "scripts/admissibility_dirac_kahler_covariant_rule_identification_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_three_direction_rule_geometry_2026_08_26.py",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py",
)
SELF_NOTE_INPUT = AUDIT_INPUT_PATHS[0]

AUDIT_TIMEOUT_SEC = 600
# THE FIVE-PIN AUTHORITY BLOCK, re-resolved live against the REMOTE origin/main.
CURRENT_MAIN = "e249016f759f224d9b429932cd0d1db4d452dc1a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block213-"
              "weighted-kernel-dispersion-20260905")
PARENT_COMMIT = "851aff9b3f950e5f08b0bd0878df2e1992bbe15b"
# The Block 212 tip: a real ancestor of HEAD carrying NEITHER Block 213 artifact.
STALE_PARENT_COMMIT = "4e9931a970ded94f769553da9e6d77770d612f64"
# A real but superseded authority head, carried forward from Block 213's record.
STALE_MAIN = "66e478505e055faf4a5b9e6f4883211e44304718"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_parameter_value_selected",
    "claim_readings_licensed",
    "break_parameter_carriers",
    "break_degree_diagonal_reconciliation",
    "break_overlap_folded_structure",
    "break_flat_control",
    "break_flat_deformation",
    "break_bloch_bench_agreement",
    "break_parity_mechanism",
    "break_d07_congruence",
    "break_union_locus",
    "break_factorization_type",
    "claim_single_metric_cone_restored",
    "break_coincidence_fate",
    "break_pencil_branches",
    "break_shear_registration",
    "claim_volume_blind_under_parameters",
    "break_scout_grade_fence",
    "claim_assembly_decided",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_parameter_value_selected": "B", "claim_readings_licensed": "B",
    "break_parameter_carriers": "C", "break_degree_diagonal_reconciliation": "C",
    "break_overlap_folded_structure": "C",
    "break_flat_control": "D", "break_flat_deformation": "D",
    "break_bloch_bench_agreement": "E",
    "break_parity_mechanism": "F", "break_d07_congruence": "F",
    "break_union_locus": "F", "break_factorization_type": "F",
    "claim_single_metric_cone_restored": "F", "break_coincidence_fate": "F",
    "break_pencil_branches": "F",
    "break_shear_registration": "G", "claim_volume_blind_under_parameters": "G",
    "break_scout_grade_fence": "H", "claim_assembly_decided": "H",
    "break_instance_scope": "H",
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
def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC).strip()


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
    "weighted kernel K_H = H d - d^T H (Block 201's completion at m = 0)",
    "Block 105's onsite and overlap assemblies (Block 213's rules)",
    "the period-2 Bloch principal part M = H0 D(kappa) + D(kappa)^T H0",
    "Block 211's four-parameter cell form with D07, D16, D25, D34 free",
    "the two Hodge readings G1 = D1/D0 and G2 = D3 E D2^-1 E (Block 213)",
    "Block 211's witnesses W1, W2, W3, mixed, honest_face, L+-, L-+ and flat",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
PARAMETER_VALUE_SELECTED_CLAIMED = False
SYMBOL_IS_DYNAMICS_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("PARAMETER", "PARITY", "CONE", "LOCUS", "BRANCH")
READINGS = (
    "R1 the parameters are a gauge-like freedom of the cell form (not established)",
    "R2 the plane D16 = D34 = -D25 is preferred (not established)",
    "R3 D07 is a 0-form normalisation (a congruence fact, not a physical reading)",
    "R4 the deformed flat cell is a physical vacuum deformation (not established)",
    "R5 the irreducible quartic is a birefringence (not established, no dynamics)",
    "R6 the volume registration through the parameters resolves #7970 (not established)",
)
CHECK_VERDICT = "FABLE-PRIMARY-RELAUNCHED-REFUTING-CHECKER-PENDING"

# THE DECLARED PARAMETER POINTS (exact rationals, all inside Block 211's bound
# D07^2 < v0/v1, D16^2, D25^2, D34^2 < v1/v0 at every rational witness used).
QUARTER = sp.Rational(1, 4)
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = sp.symbols(" ".join(PARAMETER_NAMES))
A07, B16, C25, D34 = PARAMETER_SYMBOLS
KT, KX, KY = b213.KT, b213.KX, b213.KY
KAPPA = (KT, KX, KY)
LAM = b213.LAM
SIGN_ASSEMBLIES = ("onsite", "overlap")
RATIONAL_WITNESSES = ("W1", "W2", "W3", "mixed", "honest_face")
LOCUS_WITNESSES = ("L+-", "L-+")
CONE_WITNESSES = RATIONAL_WITNESSES + LOCUS_WITNESSES
BENCH_EXTENT = (4, 2, 2)

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


def ff_det(matrix: sp.Matrix, gens: tuple, field: bool = False):
    """THE FRACTION-FREE DETERMINANT over QQ[gens] (or its fraction field):
    Bareiss on a DomainMatrix, exact, no float and no tolerance."""
    domain = QQ.frac_field(*gens) if field else QQ[list(gens)]
    return domain.to_sympy(DomainMatrix.from_Matrix(matrix).convert_to(domain).det())


def factor_shape(expression, variables: tuple) -> tuple:
    """The (total degree in the variables, multiplicity) of every irreducible
    factor over QQ that carries a variable -- the factorization TYPE."""
    return tuple((sp.Poly(base, *variables).total_degree(), power)
                 for base, power in b213.primitive_factors(expression, variables))


def square_root_factor(expression, variables: tuple):
    """The unique irreducible factor of a perfect square det M = Q^2 (fails
    closed if the factorization is not one irreducible factor squared)."""
    factors = b213.primitive_factors(expression, variables)
    if len(factors) != 1 or factors[0][1] != 2:
        return None
    return factors[0][0]


def coefficient_ideal(expression, variables: tuple, unknowns: tuple) -> tuple:
    """The lex Groebner basis, in the unknowns, of the ideal generated by the
    coefficients of `expression` as a polynomial in `variables`: its zero set
    is EXACTLY where the expression vanishes identically in the variables."""
    coefficients = sp.Poly(sp.expand(expression), *variables).coeffs()
    basis = sp.groebner([sp.expand(cf) for cf in coefficients], *unknowns, order="lex")
    return tuple(sp.expand(g) for g in basis.exprs)


def radical_generators(basis: tuple, unknowns: tuple) -> tuple:
    """The square-free parts of the basis elements, factored -- read as the
    reduced generators of the locus when every element is a power product of
    linear forms (measured, not assumed: the gate compares the literal)."""
    out = []
    for element in basis:
        _, factors = sp.factor_list(element)
        for base, _ in factors:
            if base.free_symbols & set(unknowns):
                out.append(sp.expand(base))
    return tuple(sorted(set(out), key=str))


# THE FOUR-PARAMETER CELL, SOLVED THROUGH BLOCK 211 WITH THE PARAMETERS KEPT
# SYMBOLIC (solve_pinned at_zero=False) -- and reconciled with Block 213's
# degree-diagonal cell (at_zero=True) by substitution at zero.
def full_witness_table() -> dict:
    table = dict(b213.witness_table())
    table.update(b213.locus_witness_table())
    return table


def cell_with_parameters(name: str) -> tuple:
    moduli, signs = full_witness_table()[name]
    volume0, gamma0, volume1, gamma1 = moduli
    _, matrix, rhs = b211.face_system(b211.branch_moduli(volume0, gamma0, volume1, gamma1, signs))
    cell, free = b211.solve_pinned(matrix, rhs, at_zero=False)
    diagonal, _ = b211.solve_pinned(matrix, rhs, at_zero=True)
    return cell.applyfunc(sp.radsimp), tuple(str(s) for s in free), diagonal.applyfunc(sp.radsimp)


def raising_matrix() -> sp.Matrix:
    return b213.first_order_matrix(b213.raising_rules(b213.lane_rules(3)), 3, KAPPA)


def principal_part(cell: sp.Matrix, assembly: str) -> tuple:
    """H0 (the folded H at zero momentum) and M = H0 D + D^T H0 for one cell
    under one assembly, from Block 213's rules."""
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    h0 = b213.folded_matrix(rules, 3)
    dk = raising_matrix()
    return h0, (h0 * dk + dk.T * h0).applyfunc(sp.expand), rules


def hodge_complement_permutation() -> sp.Matrix:
    return sp.Matrix(8, 8, lambda i, j: 1 if b209.CORNERS[j] == tuple(1 - x for x in b209.CORNERS[i]) else 0)


def formal_cell(signs: dict, g0, g1, v0, v1, params: tuple) -> sp.Matrix:
    """Block 213's formal block-diagonal family with the four duality entries
    placed on their corner pairs (0,7), (1,6), (2,5), (3,4)."""
    cell = b213.formal_family(signs, g0, g1, v0, v1)
    for (i, j), value in zip(((0, 7), (1, 6), (2, 5), (3, 4)), params):
        cell[i, j] = cell[j, i] = value
    return cell


# ---------------------------------------------------------------------------
# THE MEASUREMENTS -- every fact once, before any mutation flag is read
# ---------------------------------------------------------------------------
GQ = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"G{min(i, j)}{max(i, j)}"))
HQ = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"H{min(i, j)}{max(i, j)}"))
GQ_UNKNOWNS = (GQ[0, 1], GQ[0, 2], GQ[1, 1], GQ[1, 2], GQ[2, 2])
HQ_UNKNOWNS = (HQ[0, 1], HQ[0, 2], HQ[1, 1], HQ[1, 2], HQ[2, 2])


def single_quadric_locus(quartic, params: tuple) -> tuple:
    """Q = (k^T G k)^2 with G a general symmetric 3 x 3: the lex Groebner basis
    eliminated to the parameters -- () with basis (1,) means NO solution over
    the algebraic closure, i.e. no parameter point makes Q one quadric squared."""
    q = b213.quadratic_form(GQ, KAPPA)
    equations = sp.Poly(sp.expand(quartic - q ** 2), *KAPPA).coeffs()
    unknowns = tuple(GQ[i, j] for i in range(3) for j in range(i, 3))
    basis = sp.groebner(equations, *unknowns, *params, order="lex")
    return tuple(sp.expand(g) for g in basis.exprs if not any(g.has(u) for u in unknowns))


def two_quadric_locus(quartic, params: tuple) -> tuple:
    """Q = q1 q2 with two general quadrics, normalised by the kt^4 coefficient
    (nonzero at every witness, measured): the eliminant in the parameters is
    EXACTLY the locus where Q is a product of two quadrics over the closure."""
    lead = sp.Poly(quartic, *KAPPA).coeff_monomial(KT ** 4)
    if lead == 0:
        return ("LEAD-COEFFICIENT-ZERO",)
    q1, q2 = b213.quadratic_form(GQ, KAPPA), b213.quadratic_form(HQ, KAPPA)
    equations = [sp.expand(e.subs({GQ[0, 0]: 1, HQ[0, 0]: lead}))
                 for e in sp.Poly(sp.expand(quartic - q1 * q2), *KAPPA).coeffs()]
    basis = sp.groebner(equations, *GQ_UNKNOWNS, *HQ_UNKNOWNS, *params, order="lex")
    return tuple(sp.factor(g) for g in basis.exprs
                 if not any(g.has(u) for u in GQ_UNKNOWNS + HQ_UNKNOWNS))


def line_factor_locus(quartic, params: tuple) -> tuple:
    """Q vanishes on a projective line: the three affine charts of the dual
    plane, kt = -(l1 kx + l2 ky), kx = -l2 ky, ky = 0 -- exhaustive."""
    l1, l2 = sp.symbols("l1 l2")
    out = []
    for substitution in ({KT: -(l1 * KX + l2 * KY)}, {KX: -l2 * KY}, {KY: 0}):
        equations = sp.Poly(sp.expand(quartic.subs(substitution)), *KAPPA).coeffs()
        basis = sp.groebner(equations, l1, l2, *params, order="lex")
        out.append(tuple(sp.factor(g) for g in basis.exprs if not g.has(l1, l2)))
    return tuple(out)


def pencil_branches(h0: sp.Matrix, m: sp.Matrix) -> tuple:
    """The charpoly of (H0^-1 M)^2 (the H-pencil principal symbol) factored in
    lam: the linear factors are the algebraic branches, the rest the degree
    structure of the irreducible remainder."""
    operator = (h0.inv() * m).applyfunc(sp.radsimp)
    return b213.linear_branches(sp.expand((operator * operator).charpoly(LAM).as_expr()), KAPPA)


def form_branches(m: sp.Matrix) -> tuple:
    return b213.linear_branches(sp.expand((m * m).charpoly(LAM).as_expr()), KAPPA)


def measure_cells() -> dict:
    facts: dict = {}
    for name in ("flat",) + CONE_WITNESSES:
        cell, free, diagonal = cell_with_parameters(name)
        carriers = tuple((i, j) for i in range(8) for j in range(8)
                         if cell[i, j].free_symbols & set(PARAMETER_SYMBOLS))
        zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
        facts[name] = {
            "cell": cell, "free": free, "carriers": carriers,
            "entries": tuple(str(cell[i, j]) for i, j in ((0, 7), (1, 6), (2, 5), (3, 4))),
            "reconciled": residual_count(cell.subs(zero) - diagonal) == 0,
            "reconciled_b213": residual_count(diagonal - b213.solve_witness(name, *full_witness_table()[name])[1]) == 0,
        }
    return facts


def measure_construction(cells: dict) -> dict:
    """C: the four-parameter cell, its carriers, reconciliation with Block 213's
    degree-diagonal cell, onsite H0 = cell, overlap H0 = H0(0) + (s/4) P111."""
    g0, g1, v0, v1 = sp.symbols("g0 g1 v0 v1")
    formal = formal_cell(b211.ALL_PLUS, g0, g1, v0, v1, PARAMETER_SYMBOLS)
    zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
    h_on, _, _ = principal_part(formal, "onsite")
    h_ov, _, _ = principal_part(formal, "overlap")
    total = sum(PARAMETER_SYMBOLS)
    even, odd = b213.even_odd(3)
    h_eo_on = h_on.extract(even, odd)
    return {
        "free_names": tuple(cells[n]["free"] for n in ("flat",) + CONE_WITNESSES),
        "carriers": tuple(cells[n]["carriers"] for n in ("flat",) + CONE_WITNESSES),
        "entries": tuple(cells[n]["entries"] for n in ("flat",) + CONE_WITNESSES),
        "reconciled": all(cells[n]["reconciled"] and cells[n]["reconciled_b213"] for n in ("flat",) + CONE_WITNESSES),
        "onsite_h0_is_cell": residual_count(h_on - formal) == 0,
        "onsite_h_eo": tuple(tuple(str(h_eo_on[i, j]) for j in range(4)) for i in range(4)),
        "overlap_h0_structure": residual_count(h_ov - h_ov.subs(zero) - total / 4 * hodge_complement_permutation()) == 0,
        "overlap_parity_preserved_iff_sum_zero": residual_count(h_ov.extract(even, odd).subs(zero)) == 0
        and residual_count(h_ov.extract(even, odd) - total / 4 * hodge_complement_permutation().extract(even, odd)) == 0,
    }


def bench_charpolys(cell: sp.Matrix, assembly: str, reading: str) -> tuple:
    rules = (b213.onsite_rules if assembly == "onsite" else b213.overlap_rules)(cell, b209.CORNERS, 3)
    raising = b213.raising_rules(b213.lane_rules(3))
    hodge = b213.bench_matrix(rules, BENCH_EXTENT)
    lifted = b213.bench_matrix(raising, BENCH_EXTENT)
    direct = b213.direct_bench_charpoly(hodge, lifted, reading)
    union = b213.bloch_spectrum_charpoly(rules, raising, BENCH_EXTENT, 3, reading)
    return direct, union, hodge


def measure_control(cells: dict) -> dict:
    """D: the flat cell at zero parameters is the identity and gives R5's
    symbol; the flat cell with a parameter on is NOT the identity -- the
    deformed flat symbol is measured exactly."""
    flat = cells["flat"]["cell"]
    zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
    facts: dict = {"flat_zero_is_identity": residual_count(flat.subs(zero) - sp.eye(8)) == 0}
    h0, m, _ = principal_part(flat, "onsite")
    det_m = sp.expand(ff_det(m, PARAMETER_SYMBOLS + KAPPA))
    quartic = square_root_factor(det_m, KAPPA)
    norm = (KT ** 2 + KX ** 2 + KY ** 2) ** 2
    facts["flat_det_shape"] = factor_shape(det_m, KAPPA)
    facts["flat_quartic"] = str(sp.expand(quartic)) if quartic is not None else None
    facts["flat_quartic_zero_is_norm4"] = quartic is not None and sp.expand(quartic.subs(zero) - norm) == 0
    facts["flat_quartic_minus_norm4"] = str(sp.factor(sp.expand(quartic - norm))) if quartic is not None else None
    facts["flat_plane_restores_norm4"] = quartic is not None and sp.expand(
        quartic.subs({C25: -B16, D34: B16}) - norm) == 0
    facts["flat_d07_absent"] = quartic is not None and not quartic.has(A07)
    for label, point in (("D16", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
                         ("D07", {A07: QUARTER, B16: 0, C25: 0, D34: 0}),
                         ("zero", zero)):
        cellp = flat.subs(point)
        for reading in ("form", "pencil"):
            direct, union, hodge = bench_charpolys(cellp, "onsite", reading)
            facts[f"flat_{label}_{reading}_multiset"] = b213.multiset_of(direct)
            facts[f"flat_{label}_{reading}_agree"] = sp.expand(direct - union) == 0
        facts[f"flat_{label}_h_is_identity"] = residual_count(hodge - sp.eye(hodge.rows)) == 0
    return facts


def measure_bench(cells: dict) -> dict:
    """E: Bloch union = direct bench on (4,2,2) at W1 with D16 = 1/4 and with
    D07 = 1/4, both assemblies, both readings; the multisets recorded."""
    facts: dict = {}
    for label, point in (("D16", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
                         ("D07", {A07: QUARTER, B16: 0, C25: 0, D34: 0})):
        cellp = cells["W1"]["cell"].subs(point)
        for assembly in SIGN_ASSEMBLIES:
            for reading in ("form", "pencil"):
                direct, union, _ = bench_charpolys(cellp, assembly, reading)
                facts[(label, assembly, reading)] = (sp.expand(direct - union) == 0, b213.multiset_of(direct))
    return facts


def measure_mechanism() -> dict:
    """F-1/F-2: the parity-breaking mechanism at the FORMAL family with symbolic
    moduli AND symbolic parameters -- M_ee, M_oo, the D07 unipotent congruence."""
    g0, g1, v0, v1 = sp.symbols("g0 g1 v0 v1")
    formal = formal_cell(b211.ALL_PLUS, g0, g1, v0, v1, PARAMETER_SYMBOLS)
    facts: dict = {}
    even, odd = b213.even_odd(3)
    for assembly in SIGN_ASSEMBLIES:
        h0, m, _ = principal_part(formal, assembly)
        m_ee, m_oo = m.extract(even, even), m.extract(odd, odd)
        facts[(assembly, "M_ee")] = tuple(tuple(str(sp.factor(m_ee[i, j])) for j in range(4)) for i in range(4))
        facts[(assembly, "M_oo")] = tuple(tuple(str(sp.factor(m_oo[i, j])) for j in range(4)) for i in range(4))
        zero = {s: sp.Integer(0) for s in PARAMETER_SYMBOLS}
        facts[(assembly, "M_eo_parameter_free")] = not (m.extract(even, odd).free_symbols & set(PARAMETER_SYMBOLS))
        facts[(assembly, "diagonal_blocks_vanish_at_zero")] = residual_count(m_ee.subs(zero)) == 0 and residual_count(m_oo.subs(zero)) == 0
    # the onsite M_oo vanishes identically iff D16 = D34 = -D25 (any D07): its
    # three entries are (D16 + D25) kt, (D34 - D16) kx, -(D25 + D34) ky
    h0, m, _ = principal_part(formal, "onsite")
    m_oo = m.extract(odd, odd)
    facts["onsite_M_oo_entries"] = (str(sp.factor(m_oo[0, 1])), str(sp.factor(m_oo[0, 2])), str(sp.factor(m_oo[1, 2])))
    facts["onsite_M_oo_zero_on_plane"] = residual_count(m_oo.subs({C25: -B16, D34: B16})) == 0
    facts["onsite_M_oo_row7_zero"] = residual_count(m_oo[3, :]) == 0 and residual_count(m_oo[:, 3]) == 0
    m_ee = m.extract(even, even)
    facts["onsite_M_ee_vector"] = (str(sp.factor(m_ee[0, 1])), str(sp.factor(m_ee[0, 2])), str(sp.factor(m_ee[0, 3])))
    facts["onsite_M_ee_2form_block_zero"] = residual_count(m_ee[1:, 1:]) == 0
    # THE D07 CONGRUENCE: U = I - (D07/D3) E_70 with D3 = 1/v1
    unipotent = sp.eye(8)
    unipotent[7, 0] = -A07 / formal[7, 7]
    m_zero, h_zero = m.subs(A07, 0), h0.subs(A07, 0)
    facts["d07_congruence_M"] = residual_count((unipotent.T * m * unipotent - m_zero).applyfunc(sp.cancel)) == 0
    shifted = (unipotent.T * h0 * unipotent - h_zero).applyfunc(sp.cancel)
    facts["d07_congruence_H0_shift"] = str(sp.factor(shifted[0, 0]))
    facts["d07_congruence_H0_rest_zero"] = residual_count(shifted) == (1 if shifted[0, 0] != 0 else 0)
    facts["d07_shift_is_minus_a2_over_D3"] = sp.cancel(shifted[0, 0] + A07 ** 2 / formal[7, 7]) == 0
    # THE OVERLAP M SEES ONLY THE SUM s = D07 + D16 + D25 + D34: moving the
    # whole value from one parameter to another leaves M unchanged.
    _, m_overlap, _ = principal_part(formal, "overlap")
    total = sp.Symbol("s")
    reference = m_overlap.subs({A07: total, B16: 0, C25: 0, D34: 0})
    facts["overlap_sum_only"] = all(
        residual_count(m_overlap.subs({A07: 0, B16: 0, C25: 0, D34: 0, parameter: total}) - reference) == 0
        for parameter in (B16, C25, D34))
    return facts


def measure_cone(cells: dict) -> dict:
    """F-3..F-6 at every cone witness: det M with the parameters symbolic, the
    union locus (det M = det B^2 as an identity in kappa), the factorization
    type, the single-quadric and two-quadric loci, the line-factor locus."""
    facts: dict = {}
    even, odd = b213.even_odd(3)
    plane_generators = (sp.expand(B16 - D34), sp.expand(C25 + D34))
    for name in CONE_WITNESSES:
        cell = cells[name]["cell"]
        for assembly in SIGN_ASSEMBLIES:
            params = (B16, C25, D34) if assembly == "onsite" else (A07,)
            point = {A07: 0} if assembly == "onsite" else {B16: 0, C25: 0, D34: 0}
            h0, m, _ = principal_part(cell.subs(point), assembly)
            gaussian = m.has(sp.sqrt(6))
            if gaussian:
                det_m = sp.expand(sp.radsimp(m.det(method="berkowitz")))
            else:
                det_m = sp.expand(ff_det(m, params + KAPPA))
            det_b = sp.expand(m.extract(even, odd).det(method="berkowitz"))
            difference = sp.expand(sp.radsimp(det_m - det_b ** 2))
            basis = coefficient_ideal(difference, KAPPA, params)
            entry: dict = {
                "union_basis_radical": radical_generators(basis, params),
                "union_iff_plane": (radical_generators(basis, params) == plane_generators) if assembly == "onsite"
                else (radical_generators(basis, params) == (A07,)),
            }
            if gaussian:
                _, factors = sp.factor_list(det_m, extension=sp.sqrt(6))
                shape = tuple((sp.Poly(f, *KAPPA).total_degree(), p) for f, p in factors
                              if f.free_symbols & set(KAPPA))
                quartic = None
                if len(shape) == 1 and shape[0] == (4, 2):
                    quartic = [f for f, p in factors if f.free_symbols & set(KAPPA)][0]
            else:
                shape = factor_shape(det_m, KAPPA)
                quartic = square_root_factor(det_m, KAPPA)
            entry["shape"] = shape
            entry["is_square_of_quartic"] = quartic is not None
            if quartic is not None:
                quartic = sp.expand(quartic)
                entry["quartic_parameter_degree"] = sp.Poly(quartic, *params).total_degree()
                entry["quartic_even_in_parameters"] = sp.expand(quartic.subs({p: -p for p in params}, simultaneous=True) - quartic) == 0
                entry["single_quadric_locus"] = single_quadric_locus(quartic, params)
                entry["line_factor_locus"] = line_factor_locus(quartic, params) if not gaussian else ("NOT-RUN-OVER-QQ(sqrt6)",)
            facts[(name, assembly)] = entry
        # THE TWO-QUADRIC ELIMINANT on the one-parameter slices at every
        # rational witness (onsite: D16, D25, D34 alone and the diagonal
        # D16 = D25 = D34; overlap: the sum s) -- exact, over the closure.
        entry = facts[(name, "onsite")]
        if entry["is_square_of_quartic"] and name in RATIONAL_WITNESSES:
            h0, m, _ = principal_part(cell.subs({A07: 0}), "onsite")
            det_m = sp.expand(ff_det(m, (B16, C25, D34) + KAPPA))
            quartic = sp.expand(square_root_factor(det_m, KAPPA))
            s = sp.Symbol("s")
            slices = {"D16": {B16: s, C25: 0, D34: 0}, "D25": {B16: 0, C25: s, D34: 0},
                      "D34": {B16: 0, C25: 0, D34: s}, "diag": {B16: s, C25: s, D34: s}}
            entry["two_quadric_slices"] = tuple(
                (label, two_quadric_locus(sp.expand(quartic.subs(sub)), (s,))) for label, sub in slices.items())
    return facts


def measure_branches(cells: dict) -> dict:
    """F-7: the pencil and form branches with a parameter on, at W1 and at the
    locus witness L+-, and the exact D07 rescaling of the 0-form branch."""
    facts: dict = {}
    points = {
        "W1 D16": ("W1", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
        "W1 D07": ("W1", {A07: QUARTER, B16: 0, C25: 0, D34: 0}),
        "W1 plane": ("W1", {A07: 0, B16: QUARTER, C25: -QUARTER, D34: QUARTER}),
        "W1 zero": ("W1", {A07: 0, B16: 0, C25: 0, D34: 0}),
        "L+- D07": ("L+-", {A07: QUARTER, B16: 0, C25: 0, D34: 0}),
        "L+- D16": ("L+-", {A07: 0, B16: QUARTER, C25: 0, D34: 0}),
    }
    for label, (name, point) in points.items():
        cell = cells[name]["cell"].subs(point)
        h0, m, _ = principal_part(cell, "onsite")
        branches, remainder = pencil_branches(h0, m)
        facts[(label, "pencil")] = (tuple((str(sp.factor(root)), power) for root, power in branches), remainder)
        if name == "W1":
            branches_f, remainder_f = form_branches(m)
            facts[(label, "form")] = (tuple((str(sp.factor(root)), power) for root, power in branches_f), remainder_f)
    # THE D07 RESCALING, EXACT: at W1 the 0-form branch k^T D1 k / D0 becomes
    # k^T D1 k / (D0 - D07^2 / D3), the other branches unchanged.
    cell = cells["W1"]["cell"]
    g1, _, d0, d1, _, d3 = b213.metric_candidates(cell.subs({A07: 0, B16: 0, C25: 0, D34: 0}))
    facts["d07_rescaled_zero_form"] = str(sp.factor(b213.quadratic_form(d1, KAPPA) / (d0 - QUARTER ** 2 / d3)))
    facts["zero_form_branch"] = str(sp.factor(b213.quadratic_form(g1, KAPPA)))
    cellL = cells["L+-"]["cell"]
    g1L, _, d0L, d1L, _, d3L = b213.metric_candidates(cellL.subs({A07: 0, B16: 0, C25: 0, D34: 0}))
    facts["locus_d07_rescale_constant"] = sp.radsimp(sp.cancel(d0L / (d0L - QUARTER ** 2 / d3L)))
    facts["locus_tuning_a2"] = sp.radsimp(sp.cancel(d0L * d3L * (1 - sp.Rational(27, 32))))
    return facts


def measure_registration() -> dict:
    """G: the shears register with the parameters on and no parameter cancels
    that (Groebner (1)); the volumes now enter the cone through the parameters."""
    g0, g1, v0, v1 = sp.symbols("g0 g1 v0 v1")
    facts: dict = {}
    # shear: volumes at W1, shears symbolic, three parameters symbolic
    formal = formal_cell(b211.ALL_PLUS, g0, g1, sp.Rational(15, 16), sp.Integer(1), (0, B16, C25, D34))
    _, m, _ = principal_part(formal, "onsite")
    det_m = sp.expand(ff_det(m, (B16, C25, D34, g0, g1) + KAPPA))
    for shear in (g0, g1):
        derivative = sp.expand(sp.diff(det_m, shear))
        facts[f"shear_{shear}_registers"] = derivative != 0
        basis = coefficient_ideal(derivative, KAPPA + (g0, g1), (B16, C25, D34))
        facts[f"shear_{shear}_cancelling_parameters"] = basis
    # volume: shears at W1, volumes symbolic, three parameters symbolic
    formal = formal_cell(b211.ALL_PLUS, QUARTER, QUARTER, v0, v1, (0, B16, C25, D34))
    _, m, _ = principal_part(formal, "onsite")
    numerator, _ = sp.fraction(sp.together(sp.cancel(ff_det(m, (B16, C25, D34, v0, v1) + KAPPA, field=True))))
    numerator = sp.expand(numerator)
    unit = numerator.subs({v0: 1, v1: 1})
    zero = {B16: 0, C25: 0, D34: 0}
    facts["volume_blind_with_parameters"] = b213.proportional(numerator, unit, KAPPA + (B16, C25, D34))
    facts["volume_blind_at_zero_parameters"] = b213.proportional(numerator.subs(zero), unit.subs(zero), KAPPA)
    facts["volume_derivative_with_parameters"] = sp.expand(sp.diff(sp.cancel(numerator / unit), v0)) != 0
    return facts


@dataclass(frozen=True)
class Facts:
    authority: AuthorityCertificate
    construction: dict
    control: dict
    bench: dict
    mechanism: dict
    cone: dict
    branches: dict
    registration: dict
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

    git_maybe("fetch", "origin", "main", "--quiet")
    authority = authority_certificate(git_maybe("rev-parse", "origin/main"))
    lap("authority")
    cells = measure_cells()
    construction = measure_construction(cells)
    lap("construction")
    control = measure_control(cells)
    lap("control")
    bench = measure_bench(cells)
    lap("bench")
    mechanism = measure_mechanism()
    lap("mechanism")
    cone = measure_cone(cells)
    lap("cone")
    branches = measure_branches(cells)
    lap("branches")
    registration = measure_registration()
    lap("registration")
    note_text = NOTE_PATH.read_text(encoding="utf-8") if NOTE_PATH.is_file() else ""
    return Facts(authority, construction, control, bench, mechanism, cone,
                 branches, registration, note_text, timings)


# ---------------------------------------------------------------------------
# THE DECLARED LITERALS -- every claim is a constant compared against a
# measurement; a mutation rewrites exactly one claim.
# ---------------------------------------------------------------------------
PLANE = ("D16 - D34", "D25 + D34")
ONSITE_M_OO_ENTRIES = ("kt*(D16 + D25)", "-kx*(D16 - D34)", "-ky*(D25 + D34)")
ONSITE_M_EE_VECTOR = ("kt*(D07 + D34)", "-kx*(D07 - D25)", "ky*(D07 + D16)")
D07_SHIFT = "-D07**2*v1"
FLAT_QUARTIC_MINUS_NORM4 = None      # filled from the measured flat cell
FLAT_MULTISETS = None                # filled from the measured flat bench
W1_BENCH_MULTISETS = None            # filled from the measured W1 bench
LINE_LOCUS = {"onsite": None, "overlap": None}
BRANCH_TABLE = None                  # filled from the measured branches
CONE_SHAPES = {"onsite": ((4, 2),), "overlap": ((4, 2),)}
TWO_QUADRIC_SLICE_ELIMINANT = "s**2"
LOCUS_D07_RESCALE = sp.Rational(128, 119)
LOCUS_TUNING_A2 = sp.Rational(5, 48)
SCOUT_GRADE_FENCE = ("scout-grade finite exact linear algebra on one cell form, "
                     "not a spacetime and not a dynamics")
SCOUT_GRADE_ONLY = True
ASSEMBLY_DECIDED = False
HODGE_READING_SELECTED = False
INSTANCE_SCOPE = (
    "one bench (4,2,2) for the exact spectra; the principal part at one degenerate zero",
    "one cell family (Block 211's), seven cone witnesses, the flat cell, four declared parameter points",
    "two assemblies, two readings, neither selected; no parameter value selected",
    "symbolic parameters at the witnesses; symbolic moduli only for the mechanism and the registration",
    "factorization loci exact at the witnesses and on the declared slices; no generic-parameter theorem off them",
    "m = 0 and periodic closure, this block's choices as in Block 213",
)
INSTANCE_SCOPE_COUNT = 6
SCOPE_KEYS = ("n5_verbatim",)


def scope_certificate(text: str) -> dict:
    return {"n5_verbatim": N5_FENCE in text}


def build_claims(mutation: str) -> dict:
    claims = {
        "current_main": CURRENT_MAIN, "parent_commit": PARENT_COMMIT,
        "registered": (), "adopted": (), "gravity_supplied": False,
        "parameter_value_selected": False, "readings_licensed": False,
        "carriers": ((0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)),
        "reconciled": True, "overlap_structure": True,
        "flat_zero_identity": True, "flat_deformation_absent": False,
        "bench_agreement": True,
        "m_oo_entries": ONSITE_M_OO_ENTRIES, "m_ee_vector": ONSITE_M_EE_VECTOR,
        "d07_congruence": True, "d07_shift": D07_SHIFT,
        "union_iff_plane": True, "cone_shapes": CONE_SHAPES,
        "single_quadric_restored": False, "coincidence_persists_on_plane": True,
        "pencil_zero_form_rescaled": True,
        "shear_registers": True, "volume_blind_with_parameters": False,
        "scout_grade": SCOUT_GRADE_FENCE, "assembly_decided": False,
        "instance_scope_count": INSTANCE_SCOPE_COUNT,
        "n5_verbatim": True, "float_absent": True,
    }
    flips = {
        "stale_main_authority": ("current_main", STALE_MAIN),
        "stale_parent_authority": ("parent_commit", STALE_PARENT_COMMIT),
        "claim_objects_registered": ("registered", ("the four duality parameters",)),
        "claim_gravity_supplied": ("gravity_supplied", True),
        "claim_parameter_value_selected": ("parameter_value_selected", True),
        "claim_readings_licensed": ("readings_licensed", True),
        "break_parameter_carriers": ("carriers", ((0, 7), (7, 0))),
        "break_degree_diagonal_reconciliation": ("reconciled", False),
        "break_overlap_folded_structure": ("overlap_structure", False),
        "break_flat_control": ("flat_zero_identity", False),
        "break_flat_deformation": ("flat_deformation_absent", True),
        "break_bloch_bench_agreement": ("bench_agreement", False),
        "break_parity_mechanism": ("m_oo_entries", ("kt*(D16 - D25)", "-kx*(D16 - D34)", "-ky*(D25 + D34)")),
        "break_d07_congruence": ("d07_shift", "-D07**2*v0"),
        "break_union_locus": ("union_iff_plane", False),
        "break_factorization_type": ("cone_shapes", {"onsite": ((2, 2), (2, 2)), "overlap": ((4, 2),)}),
        "claim_single_metric_cone_restored": ("single_quadric_restored", True),
        "break_coincidence_fate": ("coincidence_persists_on_plane", False),
        "break_pencil_branches": ("pencil_zero_form_rescaled", False),
        "break_shear_registration": ("shear_registers", False),
        "claim_volume_blind_under_parameters": ("volume_blind_with_parameters", True),
        "break_scout_grade_fence": ("scout_grade", "a spacetime and a dynamics"),
        "claim_assembly_decided": ("assembly_decided", True),
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
    checks.check("A-2", "PARENT PIN IS THE BLOCK 213 TIP, an ancestor of HEAD, with its note and runner content-bound by blob",
                 au.parent_pin_is_commit and au.parent_is_ancestor and au.parent_artifact_blobs
                 and claims["parent_commit"] == PARENT_COMMIT)
    checks.check("A-3", "STALE PARENT (the Block 212 tip) is a real ancestor carrying NEITHER Block 213 artifact; machinery imported; inputs readable",
                 au.stale_is_real_ancestor and au.stale_carries_neither_artifact
                 and au.machinery_import_landed and au.inputs_readable == len(AUDIT_INPUT_PATHS) - 1)
    checks.check("B-1", "NOTHING REGISTERED, NOTHING ADOPTED: six imposed objects, zero registered, zero adopted",
                 len(IMPOSED_OBJECTS) == 6 and claims["registered"] == REGISTERED_OBJECTS == () and claims["adopted"] == ADOPTED_OBJECTS == ())
    checks.check("B-2", "NO GRAVITY IS SUPPLIED: nine structures enumerated as not supplied",
                 not claims["gravity_supplied"] and not GRAVITY_SUPPLIED_CLAIMED and len(UNSUPPLIED_GRAVITY_STRUCTURES) == 9)
    checks.check("B-3", "NO PARAMETER VALUE IS SELECTED: the four parameter points are declared probes, not a choice",
                 not claims["parameter_value_selected"] and not PARAMETER_VALUE_SELECTED_CLAIMED)
    checks.check("B-4", "THE WORDS PARAMETER, PARITY, CONE, LOCUS AND BRANCH ARE SCOPED; SYMBOL NAMES NO DYNAMICS, CONE NO SPACETIME CONE",
                 len(SCOPED_HEADLINE_WORDS) == 5 and not SYMBOL_IS_DYNAMICS_CLAIMED and not CONE_IS_SPACETIME_CONE_CLAIMED
                 and not CONTINUUM_LIMIT_CLAIMED)
    checks.check("B-5", "THE READINGS ARE READINGS: six enumerated, none licensed",
                 len(READINGS) == 6 and not claims["readings_licensed"] and not READINGS_LICENSED_CLAIMED)
    co = facts.construction
    checks.check("C-1", "THE FREE PARAMETERS ARE EXACTLY D07, D16, D25, D34 at all eight cells and they carry exactly the eight antidiagonal entries",
                 all(f == PARAMETER_NAMES for f in co["free_names"]) and all(c == claims["carriers"] for c in co["carriers"])
                 and all(e == PARAMETER_NAMES for e in co["entries"]))
    checks.check("C-2", "THE CELL AT ZERO PARAMETERS IS BLOCK 213's DEGREE-DIAGONAL CELL (solve_witness) at every witness",
                 co["reconciled"] == claims["reconciled"] and claims["reconciled"])
    checks.check("C-3", "ONSITE: the folded H0 IS the cell, so H_eo carries the four parameters on the antidiagonal; OVERLAP: H0 = H0(0) + (s/4) P111",
                 co["onsite_h0_is_cell"] and co["overlap_h0_structure"] == claims["overlap_structure"]
                 and co["overlap_parity_preserved_iff_sum_zero"] and claims["overlap_structure"])
    ct = facts.control
    checks.check("D-1", "THE CONTROL IS R5's: the flat cell at zero parameters is the identity, H = I on (4,2,2), multisets {0x8, 1x8} form and pencil, Bloch = direct",
                 ct["flat_zero_is_identity"] == claims["flat_zero_identity"] and claims["flat_zero_identity"]
                 and ct["flat_zero_h_is_identity"] and ct["flat_zero_form_multiset"] == ct["flat_zero_pencil_multiset"] == ((0, 8), (1, 8))
                 and ct["flat_zero_form_agree"] and ct["flat_zero_pencil_agree"] and ct["flat_quartic_zero_is_norm4"])
    checks.check("D-2", "THE FLAT CELL WITH A PARAMETER ON IS NOT THE IDENTITY: det M = Q^2 with Q = |k|^4 + (measured quartic), D07 absent, restored on the plane D16 = D34 = -D25",
                 (not ct["flat_D16_h_is_identity"]) and (not ct["flat_D07_h_is_identity"]) and ct["flat_det_shape"] == ((4, 2),)
                 and ct["flat_quartic_minus_norm4"] == FLAT_QUARTIC_MINUS_NORM4 and ct["flat_d07_absent"] and ct["flat_plane_restores_norm4"]
                 and not claims["flat_deformation_absent"])
    checks.check("D-3", "THE DEFORMED FLAT BENCH: the (4,2,2) multisets with D16 = 1/4 and with D07 = 1/4 are the declared literals, Bloch = direct",
                 tuple(ct[f"flat_{l}_{r}_multiset"] for l in ("D16", "D07") for r in ("form", "pencil")) == FLAT_MULTISETS
                 and all(ct[f"flat_{l}_{r}_agree"] for l in ("D16", "D07") for r in ("form", "pencil")))
    be = facts.bench
    checks.check("E-1", "BLOCH UNION = DIRECT BENCH on (4,2,2) at W1 with D16 = 1/4 and with D07 = 1/4, both assemblies, both readings",
                 all(v[0] for v in be.values()) == claims["bench_agreement"] and claims["bench_agreement"] and len(be) == 8)
    checks.check("E-2", "THE W1 BENCH MULTISETS WITH A PARAMETER ON are the declared literals",
                 tuple(be[k][1] for k in sorted(be)) == W1_BENCH_MULTISETS)
    me = facts.mechanism
    checks.check("F-1", "THE PARITY MECHANISM (onsite, symbolic moduli and parameters): M_eo is parameter-free; M_ee couples corner 0 to the 2-forms by u = ((D07+D34)kt, (D25-D07)kx, (D07+D16)ky); M_oo is the zero-diagonal 3x3 [(D16+D25)kt, (D34-D16)kx, -(D25+D34)ky] on the 1-forms with corner 7 empty",
                 me[("onsite", "M_eo_parameter_free")] and me["onsite_M_ee_vector"] == claims["m_ee_vector"]
                 and me["onsite_M_oo_entries"] == claims["m_oo_entries"] and me["onsite_M_oo_row7_zero"]
                 and me["onsite_M_ee_2form_block_zero"] and me[("onsite", "diagonal_blocks_vanish_at_zero")]
                 and me["onsite_M_oo_zero_on_plane"])
    checks.check("F-2", "THE D07 CONGRUENCE: U = I - (D07/D3) E_70 gives U^T M U = M|D07=0 and U^T H0 U = H0|D07=0 with D0 -> D0 - D07^2/D3 (= D0 - D07^2 v1), so D07 leaves the cone and rescales the 0-form pencil branch",
                 me["d07_congruence_M"] == claims["d07_congruence"] and claims["d07_congruence"]
                 and me["d07_congruence_H0_shift"] == claims["d07_shift"] and me["d07_congruence_H0_rest_zero"]
                 and me["d07_shift_is_minus_a2_over_D3"])
    checks.check("F-3", "OVERLAP: M sees only the sum s = D07 + D16 + D25 + D34 and its M_eo is parameter-free",
                 me["overlap_sum_only"] and me[("overlap", "M_eo_parameter_free")])
    cn = facts.cone
    checks.check("F-4", "THE UNION LOCUS: det M = det B^2 identically in kappa IFF D16 = D34 = -D25 (onsite, any D07) and IFF s = 0 (overlap), at all seven cone witnesses",
                 all(cn[(n, a)]["union_iff_plane"] for n in CONE_WITNESSES for a in SIGN_ASSEMBLIES) == claims["union_iff_plane"]
                 and claims["union_iff_plane"])
    checks.check("F-5", "THE FACTORIZATION TYPE: at symbolic parameters det M is one irreducible quartic squared under both assemblies at all seven witnesses, the quartic of degree exactly 2 and even in the parameters",
                 all(cn[(n, a)]["shape"] == claims["cone_shapes"][a] and cn[(n, a)]["is_square_of_quartic"]
                     and cn[(n, a)]["quartic_parameter_degree"] == 2 and cn[(n, a)]["quartic_even_in_parameters"]
                     for n in CONE_WITNESSES for a in SIGN_ASSEMBLIES))
    checks.check("F-6", "NO PARAMETER POINT RESTORES A SINGLE METRIC'S CONE off the locus: the single-quadric system is inconsistent (basis (1,)) at the five rational witnesses under both assemblies and at the locus witnesses under overlap",
                 all(cn[(n, a)]["single_quadric_locus"] == (sp.Integer(1),) for n in RATIONAL_WITNESSES for a in SIGN_ASSEMBLIES)
                 and all(cn[(n, "overlap")]["single_quadric_locus"] == (sp.Integer(1),) for n in LOCUS_WITNESSES)
                 == (not claims["single_quadric_restored"]))
    checks.check("F-7", "THE FATE OF THE COINCIDENCE LOCUS: at L+- and L-+ (onsite) the single-quadric locus in (D16, D25, D34) is EXACTLY the plane D16 = D34 = -D25 -- persists there for every D07, destroyed off it",
                 all(radical_generators(cn[(n, "onsite")]["single_quadric_locus"], (B16, C25, D34)) == tuple(sp.sympify(p) for p in PLANE)
                     for n in LOCUS_WITNESSES) == claims["coincidence_persists_on_plane"] and claims["coincidence_persists_on_plane"])
    checks.check("F-8", "OFF THE PLANE THE QUARTIC IS ABSOLUTELY IRREDUCIBLE ON THE DECLARED SLICES: the two-quadric eliminant is s^2 on D16, D25, D34 alone and on D16 = D25 = D34 at every rational witness, and no line factor exists at any rational witness under either assembly",
                 all(all(str(e[1]) == f"({TWO_QUADRIC_SLICE_ELIMINANT},)" for e in cn[(n, "onsite")]["two_quadric_slices"]) for n in RATIONAL_WITNESSES)
                 and all(all(str(chart) == LINE_LOCUS[a] for chart in cn[(n, a)]["line_factor_locus"]) for n in RATIONAL_WITNESSES for a in SIGN_ASSEMBLIES))
    br = facts.branches
    checks.check("F-9", "THE PENCIL WITH A PARAMETER ON at W1: the branch structures are the declared literals; with D07 = 1/4 the 0-form branch is k^T D1 k / (D0 - D07^2/D3) and the other branches are Block 213's",
                 tuple((k, br[k]) for k in sorted(br) if isinstance(k, tuple)) == BRANCH_TABLE
                 and claims["pencil_zero_form_rescaled"])
    checks.check("F-10", "ON THE LOCUS WITH D07 ON: at L+- with D07 = 1/4 the 0-form constant becomes 128/119 (the others 32/27, 4/3, 4/3 unchanged); D07^2 = (v0/v1)(1 - 1/mu) = 5/48 would tie the 0-form to the top-form constant, the transverse pair stays -- still not scalar",
                 br["locus_d07_rescale_constant"] == LOCUS_D07_RESCALE and br["locus_tuning_a2"] == LOCUS_TUNING_A2)
    rg = facts.registration
    checks.check("G-1", "THE SHEARS REGISTER WITH THE PARAMETERS ON and NO parameter point cancels either shear's registration (coefficient ideal (1))",
                 rg["shear_g0_registers"] and rg["shear_g1_registers"] and rg["shear_g0_cancelling_parameters"] == (sp.Integer(1),)
                 and rg["shear_g1_cancelling_parameters"] == (sp.Integer(1),) and claims["shear_registers"])
    checks.check("G-2", "THE VOLUMES ENTER THE CONE THROUGH THE PARAMETERS: det M is proportional to its unit-volume value at zero parameters (Block 213) and NOT with the parameters on",
                 rg["volume_blind_at_zero_parameters"] and rg["volume_blind_with_parameters"] == claims["volume_blind_with_parameters"]
                 and not claims["volume_blind_with_parameters"] and rg["volume_derivative_with_parameters"])
    checks.check("H-1", "SCOUT-GRADE FENCE, inherited verbatim from Blocks 211 and 213",
                 claims["scout_grade"] == SCOUT_GRADE_FENCE and SCOUT_GRADE_ONLY)
    checks.check("H-2", "THE ASSEMBLY IS NOT DECIDED AND NO HODGE READING IS SELECTED",
                 not claims["assembly_decided"] and not ASSEMBLY_DECIDED and not HODGE_READING_SELECTED)
    checks.check("H-3", "THE INSTANCE SCOPE IS ENUMERATED: six restrictions",
                 claims["instance_scope_count"] == len(INSTANCE_SCOPE) == 6)
    sc = scope_certificate(facts.note_text)
    checks.check("I-1", "THE NOTE IS PRESENT AND CARRIES THE N5 FENCE BYTE-IDENTICALLY",
                 bool(facts.note_text) and sc["n5_verbatim"] == claims["n5_verbatim"] and claims["n5_verbatim"])
    checks.check("I-2", "NO nsimplify, NO float literal, NO float call in this runner's source",
                 nsimplify_occurrences() == 0 and float_literal_occurrences() == 0 and float_call_sites() == 0
                 and claims["float_absent"])
    return checks


def report_measured(facts: Facts, elapsed_ns: int) -> None:
    print("== BLOCK 214: the duality parameters and the principal part -- measured facts ==")
    print(f"authority: {facts.authority}")
    co = facts.construction
    print(f"construction: free={co['free_names'][0]} carriers={co['carriers'][0]} reconciled={co['reconciled']} "
          f"onsite_h0_is_cell={co['onsite_h0_is_cell']} overlap_h0_structure={co['overlap_h0_structure']}")
    print(f"onsite H_eo (rows even 0,3,5,6; cols odd 1,2,4,7): {co['onsite_h_eo']}")
    ct = facts.control
    for key in sorted(ct):
        print(f"control {key}: {ct[key]}")
    for key in sorted(facts.bench):
        print(f"bench {key}: {facts.bench[key]}")
    me = facts.mechanism
    for key in me:
        print(f"mechanism {key}: {me[key]}")
    for key in facts.cone:
        entry = facts.cone[key]
        print(f"cone {key}: " + " ".join(f"{k}={entry[k]}" for k in entry))
    for key in facts.branches:
        print(f"branches {key}: {facts.branches[key]}")
    for key in facts.registration:
        print(f"registration {key}: {facts.registration[key]}")
    print(f"timings_ms: {facts.timings}  elapsed_ms: {elapsed_ns // 1_000_000}")


N5_FENCE = "N5-FENCE-PLACEHOLDER"


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
