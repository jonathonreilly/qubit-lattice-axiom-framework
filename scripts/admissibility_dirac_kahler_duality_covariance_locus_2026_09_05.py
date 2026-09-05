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
