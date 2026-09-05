#!/usr/bin/env python3
"""BLOCK 215 -- THE COVARIANCE LOCUS OF THE FOUR DUALITY PARAMETERS.

Block 214 exhibited the plane D16 = D34 = -D25 (onsite) and the sum s = 0
(overlap) as the loci where the cone is the union of the two Hodge cones, and
recorded that no premise prefers them.  The Admissibility axiom names one
symmetry: "covariant under lattice translations and proper cubic rotations".
This runner computes EXACTLY what that symmetry does to the four parameters
of Block 211's six-face-compatible cell form, at symbolic moduli, in every
corner-sign gauge class, for EVERY conjugacy class of subgroups of the proper
cubic group O (the classes are computed from the group, not recalled):

  the corner action of O on the eight-corner cell, BUILT HERE from the 3 x 3
  signed permutations (Block 201) as the multiplicative extension through the
  lane's own wedge (the raising part D(kappa) of Block 213/214), verified as a
  representation and as an intertwiner L D(kappa) L^-1 = D(R kappa);
  the star lemma (the Hodge star derived from the lane's wedge; the plane IS
  the star line); the twisted-covariance census (E_R R) H (E_R R)^T = H over
  Block 211's 64 sign vectors, strict and twisted, with the fate of the shears
  reported first; the overlap sum; the controls (positivity, onsite parity,
  the flat cell).  The block's theorem is a CONDITIONAL: IF the cell form is
  twisted-covariant under G THEN the parameters lie on L(G).  Whether the cell
  form inherits the axiom's covariance is a reading, enumerated and not
  licensed.  Nothing is registered and nothing is adopted; no subgroup, no
  assembly, no reading and no parameter value is selected.

Gate families: A authority, B banner and fences, C construction fidelity,
D the star lemma, E the census, F the overlap sum, G the controls, H scope
fences, I note and hygiene.  Every measurement is taken once before any
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

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

# THE MACHINERY IMPORTS, LANDED IN THIS BRANCH AND READ-ONLY.
try:
    import admissibility_dirac_kahler_duality_parameters_principal_part_2026_09_05 as b214
    B214_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b214 = None
    B214_IMPORT_LANDED = False
try:
    import admissibility_dirac_kahler_covariant_rule_identification_2026_08_26 as b201
    B201_IMPORT_LANDED = True
except ModuleNotFoundError:                            # pragma: no cover
    b201 = None
    B201_IMPORT_LANDED = False
b213 = b214.b213 if b214 is not None else None
b211 = b214.b211 if b214 is not None else None
b209 = b214.b209 if b214 is not None else None
MACHINERY_IMPORT_LANDED = bool(B214_IMPORT_LANDED and B201_IMPORT_LANDED and b214 is not None
                               and b214.MACHINERY_IMPORT_LANDED and b213 is not None
                               and b211 is not None and b209 is not None)

FINAL_NOTE_NAME = (
    "ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_"
    "NOTE_2026-09-05.md"
)
NOTE_PATH = ROOT / "docs" / FINAL_NOTE_NAME
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

# THE STACK PARENT'S TWO ARTIFACTS.  Block 214 is the commit this block is cut
# from AND its scientific parent; its note and runner exist at PARENT_COMMIT
# and NEITHER exists at STALE_PARENT_COMMIT, the Block 213 tip.
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_"
    "THEOREM_NOTE_2026-09-05.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_duality_parameters_principal_part_"
    "2026_09_05.py"
)
PARENT_ARTIFACTS = (PARENT_NOTE, PARENT_RUNNER)
PARENT_ARTIFACT_BLOBS = (
    "467b2c2eea9bdaca3fb8baa6855a33b8386211a3",
    "7cbd27e40d101a383cfb651fc8144bd94762023b",
)

# A LITERAL TUPLE OF PLAIN STRING CONSTANTS (the cache parser AST-reads it).
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_COVARIANCE_LOCUS_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUALITY_PARAMETERS_PRINCIPAL_PART_BOUNDED_THEOREM_NOTE_2026-09-05.md",
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
PARENT_REF = ("origin/physics-loop/toe-axiom-closure-block214-"
              "duality-parameters-principal-part-20260905")
PARENT_COMMIT = "1dc2ae2557a22ef188f344665bc00edc2593d113"
# The Block 213 tip: a real ancestor of HEAD carrying NEITHER Block 214 artifact.
STALE_PARENT_COMMIT = "851aff9b3f950e5f08b0bd0878df2e1992bbe15b"
# A real but superseded authority head, carried forward from Block 214's record.
STALE_MAIN = "e249016f759f224d9b429932cd0d1db4d452dc1a"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "claim_objects_registered",
    "claim_gravity_supplied",
    "claim_covariance_inherited",
    "claim_subgroup_selected",
    "claim_assembly_decided",
    "break_representation_orders",
    "break_intertwining",
    "break_subgroup_class_count",
    "break_gauge_congruence",
    "break_star_signs",
    "break_star_line",
    "break_twisted_census",
    "break_strict_census",
    "claim_shears_killed_by_twisted_covariance",
    "break_p111_commutation",
    "break_overlap_locus",
    "claim_positivity_selects_plane",
    "claim_parity_selects_plane",
    "break_flat_cell_loci",
    "break_scout_grade_fence",
    "break_instance_scope",
    "drop_n5_fence",
    "break_float_absence",
)
MUTATION_GATE = {
    "stale_main_authority": "A", "stale_parent_authority": "A",
    "claim_objects_registered": "B", "claim_gravity_supplied": "B",
    "claim_covariance_inherited": "B", "claim_subgroup_selected": "B",
    "claim_assembly_decided": "B",
    "break_representation_orders": "C", "break_intertwining": "C",
    "break_subgroup_class_count": "C", "break_gauge_congruence": "C",
    "break_star_signs": "D", "break_star_line": "D",
    "break_twisted_census": "E", "break_strict_census": "E",
    "claim_shears_killed_by_twisted_covariance": "E",
    "break_p111_commutation": "F", "break_overlap_locus": "F",
    "claim_positivity_selects_plane": "G", "claim_parity_selects_plane": "G",
    "break_flat_cell_loci": "G",
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
    "Block 211's six-face-compatible cell-form family with its ties, four gauge classes and four free duality parameters",
    "Block 211's corner-sign gauge D -> E D E (64 sign vectors, four classes)",
    "the 24 proper cubic rotations (Block 201's signed permutations, det = +1) and the corner action BUILT HERE",
    "Block 105's two assemblies (onsite, overlap) through Block 213/214's rules",
    "Block 214's plane D16 = D34 = -D25 and its facts F-1..F-4 (the loci whose name is sought)",
)
REGISTERED_OBJECTS = ()
ADOPTED_OBJECTS = ()
GRAVITY_SUPPLIED_CLAIMED = False
COVARIANCE_INHERITED_CLAIMED = False
SUBGROUP_SELECTED_CLAIMED = False
ASSEMBLY_DECIDED_CLAIMED = False
PARAMETER_VALUE_SELECTED_CLAIMED = False
READINGS_LICENSED_CLAIMED = False
CONTINUUM_LIMIT_CLAIMED = False
CONE_IS_SPACETIME_CONE_CLAIMED = False
UNSUPPLIED_GRAVITY_STRUCTURES = (
    "lapse function", "shift vector", "ADM phase space", "Hamiltonian constraint",
    "momentum/diffeomorphism constraint", "first-class constraint algebra",
    "Dirac closure", "Dirac observable", "gauge orbit and its quotient",
)
SCOPED_HEADLINE_WORDS = ("COVARIANCE", "LOCUS", "STAR", "GAUGE", "PLANE")
AXIOM_COVARIANCE_CLAUSE = ("There is one fixed nearest-neighbor admissibility rule, covariant under lattice\n"
                           "translations and proper cubic rotations.")
READINGS = (
    "R1 the cell form inherits the Admissibility axiom's proper-cubic-rotation covariance (the antecedent; not established, not asserted)",
    "R2 the plane D16 = D34 = -D25 is preferred because it is the star line (not established: only the conditional is claimed)",
    "R3 the full group O is 'the' symmetry of the cell form (not established: no subgroup is selected)",
    "R4 the sign gauge is a physical gauge symmetry (not established: it is Block 211's congruence of one solved system)",
    "R5 the star line is a light-cone or a metric statement (not established: the cone is a polynomial identity)",
    "R6 strict covariance killing the shears means the curved family is unphysical (not established: no dynamics, no selection)",
)
CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"

# the parameters, the corners and the moduli
PARAMETER_NAMES = ("D07", "D16", "D25", "D34")
PARAMETER_SYMBOLS = sp.symbols(" ".join(PARAMETER_NAMES))
A07, B16, C25, D34 = PARAMETER_SYMBOLS
G0, G1, V0, V1 = sp.symbols("g0 g1 v0 v1")
MODULI = (G0, G1, V0, V1)
SUM = sp.Symbol("s")
KT, KX, KY = b213.KT, b213.KX, b213.KY
KAPPA = (KT, KX, KY)
CORNERS = b209.CORNERS
DEGREE_INDICES = b209.DEGREE_INDICES
PAIRS = ((0, 7), (1, 6), (2, 5), (4, 3))
DIRECTION_NAMES = ("t", "x", "y")
GAUGE_CLASSES = ((1, 1), (1, -1), (-1, 1), (-1, -1))
QUARTER = sp.Rational(1, 4)

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


def corner_index(corner: tuple) -> int:
    return CORNERS.index(tuple(corner))


# ---------------------------------------------------------------------------
# C. THE ROTATIONS, THE WEDGE, THE CORNER ACTION -- built here, then verified
# ---------------------------------------------------------------------------
def rotations() -> tuple:
    """Block 201's signed 3 x 3 permutation matrices with det = +1: the
    proper cubic rotations of the direction space (t, x, y)."""
    return tuple(sp.ImmutableMatrix(m) for m in b201.signed_permutations())


def raising_matrix() -> sp.Matrix:
    return b214.raising_matrix()


def unit_raising(direction: int) -> sp.Matrix:
    """D(e_mu): the raising part at the unit vector kappa = e_mu -- left
    multiplication by the basis 1-form of that direction, read off the lane's
    own D(kappa) and nothing else."""
    point = {k: (1 if i == direction else 0) for i, k in enumerate(KAPPA)}
    return raising_matrix().subs(point)


def wedge_rule() -> dict:
    """THE LANE'S WEDGE SIGNATURE, MEASURED FROM D: for each direction mu and
    each corner c without mu, the sign of D(e_mu)[c + e_mu, c]."""
    rule = {}
    for mu in range(3):
        d = unit_raising(mu)
        for c in CORNERS:
            if c[mu] == 1:
                continue
            target = tuple(c[k] + (1 if k == mu else 0) for k in range(3))
            rule[(mu, c)] = d[corner_index(target), corner_index(c)]
    return rule


def ordered_monomial_sign(mu: int, c: tuple) -> int:
    """The sign of e_mu ^ e_c in the ORDERED monomial basis t < x < y: minus
    one for every occupied direction of c before mu."""
    return (-1) ** sum(c[:mu])


def corner_action(rotation: sp.Matrix) -> sp.Matrix:
    """L(R) e_c = (R e_mu1) ^ (R e_mu2) ^ ... for c = {mu1 < mu2 < ...}: the
    multiplicative extension of the direction action THROUGH THE LANE'S WEDGE
    (products of D(e_mu) applied to the empty corner), so every sign is the
    lane's own."""
    unit = [unit_raising(mu) for mu in range(3)]
    images = [sum((rotation[nu, mu] * unit[nu] for nu in range(3)), sp.zeros(8, 8)) for mu in range(3)]
    lifted = sp.zeros(8, 8)
    vacuum = sp.zeros(8, 1)
    vacuum[0, 0] = 1
    for c in CORNERS:
        vector = vacuum
        for mu in reversed([mu for mu in range(3) if c[mu] == 1]):
            vector = images[mu] * vector
        lifted[:, corner_index(c)] = vector
    return sp.ImmutableMatrix(lifted)


def direction_map(rotation: sp.Matrix) -> tuple:
    """(pi, s): column mu of R has its nonzero at row pi(mu) with sign s_mu."""
    pi, signs = [], []
    for mu in range(3):
        nu = [n for n in range(3) if rotation[n, mu] != 0][0]
        pi.append(nu)
        signs.append(int(rotation[nu, mu]))
    return tuple(pi), tuple(signs)


def orientation_lift(rotation: sp.Matrix) -> sp.Matrix:
    """THE SIGN RULE, STATED: L(R) e_c = (prod of the direction signs on c) x
    (sign of the permutation sorting the image directions) e_{R c}.  Compared
    against the wedge construction at gate C-2."""
    pi, signs = direction_map(rotation)
    lifted = sp.zeros(8, 8)
    for c in CORNERS:
        occupied = [mu for mu in range(3) if c[mu] == 1]
        image = [pi[mu] for mu in occupied]
        sign = 1
        for mu in occupied:
            sign *= signs[mu]
        for i in range(len(image)):
            for j in range(i + 1, len(image)):
                if image[i] > image[j]:
                    sign = -sign
        target = tuple(1 if nu in image else 0 for nu in range(3))
        lifted[corner_index(target), corner_index(c)] = sign
    return sp.ImmutableMatrix(lifted)


def monomial_intertwiners(rotation: sp.Matrix) -> tuple:
    """MEASURE the sign rule instead of guessing it: among the 256 signed
    versions of the corner permutation of R, exactly those satisfying
    T D(kappa) T^-1 = D(R kappa) -- expected to be +-L(R) and nothing else."""
    lifted = corner_action(rotation)
    permutation = lifted.applyfunc(abs)
    dk = raising_matrix()
    rotated = dk.subs({k: sum(rotation[i, j] * KAPPA[j] for j in range(3)) for i, k in enumerate(KAPPA)},
                      simultaneous=True)
    found = []
    for signs in itertools.product((1, -1), repeat=8):
        t = sp.diag(*signs) * permutation
        if residual_count((t * dk * t.T - rotated).applyfunc(sp.expand)) == 0:
            found.append(sp.ImmutableMatrix(t))
    return tuple(found)


def matrix_order(matrix: sp.Matrix) -> int:
    power = matrix
    for n in range(1, 25):
        if power == sp.eye(8):
            return n
        power = power * matrix
    return 0


def axis_type(rotation: sp.Matrix) -> str:
    """The rotation axis from the +1 eigenspace: face (a coordinate axis),
    edge (two nonzero coordinates) or body (the diagonal)."""
    space = (rotation - sp.eye(3)).nullspace()
    if len(space) == 3:
        return "identity"
    vector = space[0]
    return {1: "face", 2: "edge", 3: "body"}[sum(1 for x in vector if x != 0)]


# ---------------------------------------------------------------------------
# the group: multiplication table, subgroups, conjugacy classes -- COMPUTED
# ---------------------------------------------------------------------------
def group_table(lifts: tuple) -> tuple:
    """The 24 x 24 multiplication table of the lifted matrices (closure and
    the identity are measured, not assumed)."""
    index = {m: i for i, m in enumerate(lifts)}
    table = []
    for a in lifts:
        row = []
        for b in lifts:
            product = sp.ImmutableMatrix(a * b)
            row.append(index.get(product, -1))
        table.append(tuple(row))
    return tuple(table)


def closure(table: tuple, generators: frozenset, identity: int) -> frozenset:
    elements = {identity} | set(generators)
    frontier = list(elements)
    while frontier:
        g = frontier.pop()
        for h in list(elements):
            for product in (table[g][h], table[h][g]):
                if product not in elements:
                    elements.add(product)
                    frontier.append(product)
    return frozenset(elements)


def all_subgroups(table: tuple, identity: int) -> tuple:
    """Closures of every pair of elements, deduplicated; then the completeness
    certificate: adjoining any element to any listed subgroup and closing gives
    a listed subgroup (so every subgroup, generated element by element, is
    listed)."""
    n = len(table)
    found = set()
    for i in range(n):
        for j in range(n):
            found.add(closure(table, frozenset((i, j)), identity))
    complete = all(closure(table, s | {g}, identity) in found for s in found for g in range(n))
    return tuple(sorted(found, key=lambda s: (len(s), sorted(s)))), complete


def inverse_of(table: tuple, g: int, identity: int) -> int:
    return [h for h in range(len(table)) if table[g][h] == identity][0]


def conjugacy_classes(table: tuple, subgroups: tuple, identity: int) -> tuple:
    n = len(table)
    classes, seen = [], set()
    for s in subgroups:
        if s in seen:
            continue
        orbit = set()
        for g in range(n):
            ginv = inverse_of(table, g, identity)
            orbit.add(frozenset(table[table[g][h]][ginv] for h in s))
        seen |= orbit
        classes.append(tuple(sorted(orbit, key=sorted)))
    return tuple(classes)


def class_signature(subgroup: frozenset, orders: tuple, axes: tuple) -> tuple:
    """The multiset of (element order, axis type) -- the geometric label of a
    subgroup class, computed from its elements."""
    return tuple(sorted((orders[g], axes[g]) for g in subgroup))


SIGNATURE_NAMES = {
    ((1, "identity"),): "1",
    ((1, "identity"), (2, "face")): "C2_face",
    ((1, "identity"), (2, "edge")): "C2_edge",
    ((1, "identity"), (3, "body"), (3, "body")): "C3_body",
    ((1, "identity"), (2, "face"), (4, "face"), (4, "face")): "C4_face",
    ((1, "identity"), (2, "face"), (2, "face"), (2, "face")): "V4_faces",
    ((1, "identity"), (2, "edge"), (2, "edge"), (2, "face")): "V4_face_edges",
    ((1, "identity"), (2, "edge"), (2, "edge"), (2, "edge"), (3, "body"), (3, "body")): "S3_body",
    ((1, "identity"), (2, "edge"), (2, "edge"), (2, "face"), (2, "face"), (2, "face"), (4, "face"), (4, "face")): "D4_face",
    tuple(sorted([(1, "identity")] + [(2, "face")] * 3 + [(3, "body")] * 8)): "T",
    tuple(sorted([(1, "identity")] + [(2, "face")] * 3 + [(3, "body")] * 8 + [(2, "edge")] * 6 + [(4, "face")] * 6)): "O",
}


# ---------------------------------------------------------------------------
# D. THE STAR, derived from the lane's wedge
# ---------------------------------------------------------------------------
def hodge_star() -> sp.Matrix:
    """* e_c = sign e_{c-bar} with the sign fixed by e_c ^ (* e_c) = e_{txy}
    (the volume form = the full corner with coefficient +1), the wedge being
    the products of the lane's D(e_mu) -- no sign is assumed."""
    unit = [unit_raising(mu) for mu in range(3)]
    star = sp.zeros(8, 8)
    for c in CORNERS:
        complement = tuple(1 - x for x in c)
        vector = sp.zeros(8, 1)
        vector[corner_index(complement), 0] = 1
        for mu in reversed([mu for mu in range(3) if c[mu] == 1]):
            vector = unit[mu] * vector
        star[corner_index(complement), corner_index(c)] = vector[7, 0]
    return sp.ImmutableMatrix(star)


def degree_projector(degree: int) -> sp.Matrix:
    p = sp.zeros(8, 8)
    for i in DEGREE_INDICES[degree]:
        p[i, i] = 1
    return p


def star_facts(lifts: tuple) -> dict:
    star = hodge_star()
    dk = raising_matrix()
    facts: dict = {"star_signs": tuple(int(star[corner_index(tuple(1 - x for x in c)), corner_index(c)]) for c in CORNERS)}
    facts["star_squares"] = tuple(int((star * star * degree_projector(k))[DEGREE_INDICES[k][0], DEGREE_INDICES[k][0]]) for k in range(4))
    facts["star_square_is_scalar"] = residual_count(star * star - sp.diag(*[facts["star_squares"][b209.CORNER_DEGREE[i]] for i in range(8)])) == 0
    # * D(kappa) = eps_k D(kappa)^T * on k-forms, the sign measured per degree
    adjoint_signs = []
    for k in range(3):
        left = (star * dk * degree_projector(k)).applyfunc(sp.expand)
        right = (dk.T * star * degree_projector(k)).applyfunc(sp.expand)
        sign = [e for e in (1, -1) if residual_count((left - e * right).applyfunc(sp.expand)) == 0]
        adjoint_signs.append(sign[0] if sign else 0)
    facts["star_adjoint_signs"] = tuple(adjoint_signs)
    facts["star_commutes_with_every_lift"] = all(residual_count(L * star - star * L) == 0 for L in lifts)
    p111 = b214.hodge_complement_permutation()
    facts["p111_is_unsigned_star"] = residual_count(p111 - star.applyfunc(abs)) == 0
    twists = []
    for L in lifts:
        twist = L * p111 * L.T
        diagonal = (twist * p111).applyfunc(sp.expand)
        twists.append(tuple(int(diagonal[i, i]) for i in range(8)) if residual_count(twist.applyfunc(abs) - p111) == 0 else None)
    facts["p111_twists"] = tuple(twists)
    facts["p111_commutes_with_lift_count"] = sum(1 for t in twists if t == (1,) * 8)
    facts["p111_commutes_with_unsigned_permutation"] = all(
        residual_count(P * p111 - p111 * P) == 0 for P in (L.applyfunc(abs) for L in lifts))
    # the 1 <-> 2 block of the star on the duality pairs (1,6), (2,5), (4,3)
    facts["star_pair_signs"] = tuple(int(star[j, i]) for i, j in PAIRS)
    return facts


# ---------------------------------------------------------------------------
# the family, the gauge, the locus machinery
# ---------------------------------------------------------------------------
def family(class_key: tuple, params: tuple, moduli: tuple = MODULI) -> sp.Matrix:
    g0, g1, v0, v1 = moduli
    return b214.formal_cell(b211.REPRESENTATIVES[class_key], g0, g1, v0, v1, params)


def sign_vectors() -> tuple:
    """Block 211's 64 corner-sign vectors: the six middle corners free, the
    empty and the full corner fixed at +1."""
    out = []
    for signs in itertools.product((1, -1), repeat=6):
        e = [1] * 8
        for k, i in enumerate((1, 2, 4, 3, 5, 6)):
            e[i] = signs[k]
        out.append(tuple(e))
    return tuple(out)


def canonical_subspace(rows: list, unknowns: tuple):
    """The linear ideal generated by the rows, as the RREF of the coefficient
    matrix -- a canonical form, so equal subspaces compare equal."""
    if not rows:
        return ()
    matrix = sp.Matrix(rows)
    reduced, pivots = matrix.rref()
    return tuple(tuple(reduced[i, j] for j in range(len(unknowns))) for i in range(len(pivots)))


def subspace_contains(inner, outer) -> bool:
    """V(inner) is a subset of V(outer): every generator of `outer` lies in the
    row space of `inner`."""
    if not outer:
        return True
    if not inner:
        return False
    a = sp.Matrix(list(inner))
    b = sp.Matrix(list(inner) + list(outer))
    return a.rank() == b.rank()


def constraints(h: sp.Matrix, lift: sp.Matrix, e: tuple, unknowns: tuple) -> tuple:
    """(forced moduli conditions, parameter subspace) for T = E L: the entries
    of T H T^T - H, each either a parameter-linear form (collected) or a
    moduli-only expression (which forces a condition on the moduli)."""
    # T = E L is a signed permutation: T e_i = eps_i e_{p(i)} with eps_i the
    # lift's sign at column i times e at the target, so (T H T^T)[p(i), p(j)]
    # = eps_i eps_j H[i, j] -- the congruence entry by entry, no products.
    p = [next(r for r in range(8) if lift[r, i] != 0) for i in range(8)]
    eps = [int(lift[p[i], i]) * e[p[i]] for i in range(8)]
    rows, forced = [], set()
    for i in range(8):
        for j in range(i, 8):
            if h[i, j] == 0 and h[p[i], p[j]] == 0:
                continue
            entry = sp.expand(eps[i] * eps[j] * h[i, j] - h[p[i], p[j]])
            if entry == 0:
                continue
            if not (entry.free_symbols & set(unknowns)):
                forced.add(str(sp.factor(entry)))
                continue
            poly = sp.Poly(entry, *unknowns)
            if poly.total_degree() != 1 or (poly.free_symbols - set(unknowns)):
                forced.add("NONLINEAR:" + str(entry))
                continue
            rows.append([poly.coeff_monomial(u) for u in unknowns])
    return frozenset(forced), canonical_subspace(rows, unknowns)


def irredundant(components: list) -> tuple:
    """Drop every component contained in another: (F, V) is inside (F', V')
    when F' is a subset of F and V is a subset of V'."""
    kept = []
    for f, v in components:
        dominated = any((f2 <= f and subspace_contains(v, v2)) and (f2, v2) != (f, v)
                        for f2, v2 in components)
        if not dominated and (f, v) not in kept:
            kept.append((f, v))
    return tuple(sorted(kept, key=lambda fv: (sorted(fv[0]), fv[1])))


def intersect(left: tuple, right: tuple, unknowns: tuple) -> tuple:
    out = []
    for f1, v1 in left:
        for f2, v2 in right:
            out.append((f1 | f2, canonical_subspace([list(r) for r in v1 + v2], unknowns)))
    return irredundant(out)


def per_rotation_loci(h: sp.Matrix, lifts: tuple, unknowns: tuple, twisted: bool) -> tuple:
    """For every rotation, the union of components over the admissible sign
    vectors (twisted) or over E = 1 alone (strict)."""
    vectors = sign_vectors() if twisted else ((1,) * 8,)
    return tuple(irredundant([constraints(h, L, e, unknowns) for e in vectors]) for L in lifts)


def subgroup_locus(per_rotation: tuple, subgroup: frozenset, unknowns: tuple) -> tuple:
    result = ((frozenset(), ()),)
    for g in sorted(subgroup):
        result = intersect(result, per_rotation[g], unknowns)
    return result


def describe(components: tuple, unknowns: tuple) -> tuple:
    """A printable literal: each component as (forced conditions, generators)."""
    out = []
    for f, v in components:
        generators = tuple(str(sp.expand(sum(coefficient * u for coefficient, u in zip(row, unknowns)))) for row in v)
        out.append((tuple(sorted(f)), generators))
    return tuple(out)


# ---------------------------------------------------------------------------
# THE MEASUREMENTS -- every fact once, before any mutation flag is read
# ---------------------------------------------------------------------------
def measure_group() -> dict:
    """C: the 24 rotations, the corner action as a representation, the sign
    rule measured, the intertwining, the subgroup classes computed."""
    rots = rotations()
    lifts = tuple(corner_action(R) for R in rots)
    facts: dict = {"rotation_count": len(rots), "all_det_one": all(R.det() == 1 for R in rots)}
    facts["distinct_lifts"] = len(set(lifts))
    table = group_table(lifts)
    facts["closed"] = all(x >= 0 for row in table for x in row)
    identity = lifts.index(sp.ImmutableMatrix(sp.eye(8)))
    facts["identity_index"] = identity
    orders = tuple(matrix_order(L) for L in lifts)
    facts["order_counts"] = tuple((n, orders.count(n)) for n in (1, 2, 3, 4))
    facts["homomorphism"] = all(
        table[i][j] == lifts.index(sp.ImmutableMatrix(corner_action(rots[i] * rots[j])))
        for i in range(24) for j in range(24))
    facts["sign_rule_matches_wedge"] = all(orientation_lift(R) == L for R, L in zip(rots, lifts))
    facts["lift_on_empty_and_full_corner"] = tuple(sorted(set((int(L[0, 0]), int(L[7, 7])) for L in lifts)))
    dk = raising_matrix()
    facts["intertwines"] = all(
        residual_count((L * dk * L.T - dk.subs(
            {k: sum(R[i, j] * KAPPA[j] for j in range(3)) for i, k in enumerate(KAPPA)}, simultaneous=True)
        ).applyfunc(sp.expand)) == 0 for R, L in zip(rots, lifts))
    facts["lift_orthogonal"] = all(residual_count(L * L.T - sp.eye(8)) == 0 for L in lifts)
    # the sign rule MEASURED: the intertwining monomial lifts are exactly +-L(R)
    measured = tuple(monomial_intertwiners(R) for R in rots)
    facts["monomial_intertwiner_count"] = tuple(sorted(set(len(m) for m in measured)))
    facts["monomial_intertwiners_are_plus_minus_lift"] = all(
        set(m) == {L, sp.ImmutableMatrix(-L)} for m, L in zip(measured, lifts))
    # the wedge rule read off D versus the ordered-monomial sign
    rule = wedge_rule()
    facts["wedge_is_ordered_monomial"] = all(v == ordered_monomial_sign(mu, c) for (mu, c), v in rule.items())
    facts["wedge_rule_count"] = len(rule)
    # subgroups and their conjugacy classes, from the table
    subgroups, complete = all_subgroups(table, identity)
    classes = conjugacy_classes(table, subgroups, identity)
    axes = tuple(axis_type(R) for R in rots)
    labelled = []
    for cls in classes:
        signature = class_signature(cls[0], orders, axes)
        labelled.append((SIGNATURE_NAMES.get(signature, "UNNAMED:" + str(signature)), len(cls[0]), len(cls), cls[0]))
    labelled.sort(key=lambda x: (x[1], x[0]))
    facts["subgroup_count"] = len(subgroups)
    facts["subgroups_complete"] = complete
    facts["class_table"] = tuple((name, order, size) for name, order, size, _ in labelled)
    facts["representatives"] = {name: rep for name, _, _, rep in labelled}
    facts["lifts"] = lifts
    facts["rotations"] = rots
    facts["table"] = table
    facts["axes"] = axes
    facts["orders"] = orders
    return facts


def measure_star(group: dict) -> dict:
    facts = star_facts(group["lifts"])
    # THE STAR LINE: the 1 <-> 2 cross block of the family is proportional to
    # the star exactly when (D16, D25, D34) is proportional to the star's pair
    # signs; the linear ideal of that line, canonical.
    sy, sx, st = facts["star_pair_signs"][1:]
    lam = sp.Symbol("lam")
    line = canonical_subspace([[0, 1, 0, -sy * st], [0, 0, 1, -sx * st]], PARAMETER_SYMBOLS)
    facts["star_line_generators"] = describe(((frozenset(), line),), PARAMETER_SYMBOLS)[0][1]
    facts["star_line_is_block214_plane"] = tuple(sorted(facts["star_line_generators"])) == tuple(sorted(b214.PLANE))
    # the cross block on the line IS lam * star (1 -> 2) with D07 the free 0 <-> 3 multiple
    star = hodge_star()
    h = family((1, 1), (A07, lam * sy, lam * sx, lam * st))
    even, odd = b213.even_odd(3)
    ones, twos = DEGREE_INDICES[1], DEGREE_INDICES[2]
    cross = h.extract(list(twos), list(ones))
    facts["cross_block_is_lam_star_on_line"] = residual_count(cross - lam * star.extract(list(twos), list(ones))) == 0
    facts["d07_is_zero_three_star_multiple"] = h[7, 0] == A07 * star[7, 0]
    # the mechanism: the onsite M_oo vanishes on the star line and not off it
    hs = family((1, 1), PARAMETER_SYMBOLS)
    _, m, _ = b214.principal_part(hs, "onsite")
    m_oo = m.extract(odd, odd)
    on_line = m_oo.subs({B16: lam * sy, C25: lam * sx, D34: lam * st})
    facts["m_oo_zero_on_star_line"] = residual_count(on_line.applyfunc(sp.expand)) == 0
    facts["m_oo_nonzero_off_line"] = residual_count(m_oo.subs({B16: lam, C25: lam, D34: lam}).applyfunc(sp.expand)) > 0
    # the star-line ideal equals the coefficient ideal of M_oo in the parameters
    entries = [sp.expand(m_oo[i, j]) for i in range(4) for j in range(4) if sp.expand(m_oo[i, j]) != 0]
    rows = []
    for entry in entries:
        for coefficient in sp.Poly(entry, *KAPPA).coeffs():
            rows.append([sp.Poly(coefficient, *PARAMETER_SYMBOLS).coeff_monomial(u) for u in PARAMETER_SYMBOLS])
    facts["m_oo_ideal_is_star_line"] = canonical_subspace(rows, PARAMETER_SYMBOLS) == line
    return facts


def measure_census(group: dict) -> dict:
    """E: per gauge class, per subgroup class: the twisted and the strict
    loci with the fate of the shears, from the per-rotation data."""
    lifts = group["lifts"]
    facts: dict = {"twisted": {}, "strict": {}, "per_rotation_twisted_shears_survive": {},
                   "per_rotation_strict_shears_survive": {}}
    for key in GAUGE_CLASSES:
        h = family(key, PARAMETER_SYMBOLS)
        print(f"[census] gauge class {key}", file=sys.stderr)
        twisted = per_rotation_loci(h, lifts, PARAMETER_SYMBOLS, True)
        strict = per_rotation_loci(h, lifts, PARAMETER_SYMBOLS, False)
        facts["per_rotation_twisted_shears_survive"][key] = tuple(any(not f for f, _ in comps) for comps in twisted)
        facts["per_rotation_strict_shears_survive"][key] = tuple(any(not f for f, _ in comps) for comps in strict)
        for name, rep in group["representatives"].items():
            facts["twisted"][(key, name)] = describe(subgroup_locus(twisted, rep, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS)
            facts["strict"][(key, name)] = describe(subgroup_locus(strict, rep, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS)
    return facts


def measure_overlap(group: dict) -> dict:
    """F: the overlap fold sees the sum only; its parity; its loci in s."""
    lifts = group["lifts"]
    h_full, _, _ = b214.principal_part(family((1, 1), PARAMETER_SYMBOLS), "overlap")
    h_sum, _, _ = b214.principal_part(family((1, 1), (SUM, 0, 0, 0)), "overlap")
    facts: dict = {"overlap_sees_sum_only": residual_count(
        (h_full - h_sum.subs(SUM, sum(PARAMETER_SYMBOLS))).applyfunc(sp.expand)) == 0}
    even, odd = b213.even_odd(3)
    p111 = b214.hodge_complement_permutation()
    facts["overlap_parity_block_is_sum_over_four_p111"] = residual_count(
        (h_sum.extract(even, odd) - SUM / 4 * p111.extract(even, odd)).applyfunc(sp.expand)) == 0
    facts["twisted"], facts["strict"] = {}, {}
    for key in GAUGE_CLASSES:
        h, _, _ = b214.principal_part(family(key, (SUM, 0, 0, 0)), "overlap")
        print(f"[overlap] gauge class {key}", file=sys.stderr)
        twisted = per_rotation_loci(h, lifts, (SUM,), True)
        strict = per_rotation_loci(h, lifts, (SUM,), False)
        for name, rep in group["representatives"].items():
            facts["twisted"][(key, name)] = describe(subgroup_locus(twisted, rep, (SUM,)), (SUM,))
            facts["strict"][(key, name)] = describe(subgroup_locus(strict, rep, (SUM,)), (SUM,))
    return facts


def measure_controls(group: dict) -> dict:
    """G: positivity off the plane, onsite parity, the flat cell, the gauge
    congruence in the field, the reconciliation with Block 214's cell."""
    lifts = group["lifts"]
    facts: dict = {}
    w1 = (sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(15, 16), sp.Integer(1))   # (g0, g1, v0, v1) at W1
    witness = family((1, 1), (0, QUARTER, 0, 0), w1)
    minors = tuple(witness[:k, :k].det() for k in range(1, 9))
    facts["positivity_witness_minors"] = minors
    facts["positivity_witness_is_pd"] = all(m > 0 for m in minors)
    plane = [sp.sympify(g) for g in b214.PLANE]
    facts["positivity_witness_off_plane"] = any(
        g.subs({B16: QUARTER, C25: 0, D34: 0}) != 0 for g in plane)
    h = family((1, 1), PARAMETER_SYMBOLS)
    even, odd = b213.even_odd(3)
    h_eo = h.extract(even, odd)
    facts["onsite_parity_block_entries"] = tuple(sorted(str(x) for x in h_eo if x != 0))
    facts["onsite_parity_preserved_iff_all_zero"] = set(h_eo.free_symbols) == set(PARAMETER_SYMBOLS) and all(
        residual_count(h_eo.subs({p: 0 for p in PARAMETER_SYMBOLS if p != q})) == 1 for q in PARAMETER_SYMBOLS)
    flat = family((1, 1), PARAMETER_SYMBOLS, (sp.Integer(0), sp.Integer(0), sp.Integer(1), sp.Integer(1)))
    facts["flat_zero_is_identity"] = residual_count(flat.subs({p: 0 for p in PARAMETER_SYMBOLS}) - sp.eye(8)) == 0
    twisted = per_rotation_loci(flat, lifts, PARAMETER_SYMBOLS, True)
    strict = per_rotation_loci(flat, lifts, PARAMETER_SYMBOLS, False)
    facts["flat_twisted"] = {name: describe(subgroup_locus(twisted, rep, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS)
                             for name, rep in group["representatives"].items()}
    facts["flat_strict"] = {name: describe(subgroup_locus(strict, rep, PARAMETER_SYMBOLS), PARAMETER_SYMBOLS)
                            for name, rep in group["representatives"].items()}
    zero = {p: 0 for p in PARAMETER_SYMBOLS}
    base = family((1, 1), PARAMETER_SYMBOLS).subs(zero)
    facts["gauge_congruence_in_field"] = all(
        any(residual_count((sp.diag(*e) * base * sp.diag(*e) - family(key, PARAMETER_SYMBOLS).subs(zero)).applyfunc(sp.expand)) == 0
            for e in sign_vectors()) for key in GAUGE_CLASSES)
    cell, free, _ = b214.cell_with_parameters("W1")
    renamed = cell.subs({s: dict(zip(PARAMETER_NAMES, PARAMETER_SYMBOLS))[str(s)] for s in cell.free_symbols
                         if str(s) in PARAMETER_NAMES})
    facts["family_is_block214_cell_at_w1"] = residual_count((renamed - family((1, 1), PARAMETER_SYMBOLS, w1)).applyfunc(sp.cancel)) == 0 \
        and free == PARAMETER_NAMES
    return facts
