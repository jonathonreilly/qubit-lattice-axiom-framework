#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_shear_gauge_classification_2026_08_20.py
"""Block 149: the SHEAR'S GAUGE CLASSIFICATION -- physics or bookkeeping.

Block 148 closed the annealed migration programme and handed forward, as its own
named decision cut, the question Blocks 147/148 both inherited undecided and the
owner has asked twice: IS THE CARRIER SHEAR PHYSICS OR BOOKKEEPING?  Block 148
committed the object that makes the question answerable -- a 64-element group of
covariant affine carrier moves (t,x) -> (e t + p, e x + q) acting on the
64-modulus family through order 32 -- but it never asked what that group does to
the LANE'S INVARIANTS.  This runner asks, and the answer is a SPLIT, not a side:

  * THE GROUP IS BOOKKEEPING AS A CHANGE OF FRAME, EXACTLY.  With the whole
    frame transported -- pairing operator X -> D X D^T, half PLUS -> D PLUS,
    connection d -> g d g^T, D = descend(g) -- the half pairing is not merely
    congruent to the original but IDENTICALLY THE SAME MATRIX, symbolically in
    all 64 moduli, in m and in the fixture shears (s_x, s_t), for BOTH displayed
    conventions (theta and the staggered parity X_0).  Every invariant built
    from the half pairing is therefore orbit-constant for trivial reasons, and
    saying "the 64-group is a gauge group" is saying only that;
  * THE PHYSICAL GAUGE GROUP IS SMALLER THAN THE 64, AND IT IS Z_4 x Z_4.  The
    32 reflections INVERT nu while fixing a and b, so they carry a carrier off
    the physical locus unless nu = 1 everywhere: 0/32 stay physical at a generic
    cone carrier and 32/32 at nu = 1 (Block 147's residual, re-derived).  What
    survives is the 32 translations, acting on carriers through ORDER 16 with
    kernel {id, four-step time shift} and element-order multiset {1:1, 2:3,
    4:12} -- Z_4 x Z_4.  The moduli-to-Hodge map has RANK 32, so half of the
    Block 145 linear envelope is invisible to every invariant in the lane;
  * THE JACOBIAN QUALIFIER IS REAL AND IS CARRIED, NOT HIDDEN.  The physical
    Jacobian d H_q / d(sigma, nu) has FULL RANK 32 at a generic cone carrier, so
    generic physical carriers are locally separated by H_q alone -- but on the
    nu = 1 SLICE the rank DROPS TO 30, uniformly, and at the flat carrier the
    two-dimensional kernel is spanned by two STAGGERED VOLUME directions, one on
    each cell-parity class, with entries +-1.  "Locally separated" is therefore a
    GENERIC statement and is quantified that way everywhere below;
  * AGAINST THE LANE'S CANONICAL FIXED FRAME THE GROUP IS NOT BOOKKEEPING, AND
    THE SPLIT IS EXACT.  Holding (theta / X_0, the half {p = 0,1}, the committed
    four-chart atlas) fixed and moving only the carrier, the profile splits into
    five tiers with stabiliser orders 64, 64, 32, 56, 4 out of 64 on the
    committed base carrier at the committed fixture mass m = 2/7.  The seam tier
    is constant on EXACTLY the index-2 subgroup ker chi of the cell-time-parity
    character chi(e,p,e,q) = p + (1-e)/2 mod 2 -- a checked homomorphism -- which
    contains both theta and theta'.  The healed-edge census tier is 56/64,
    broken by EXACTLY the eight parity-preserving even-x-centred reflections, and
    that breaking is BOTH a DRESSING ARTIFACT (64/64 undressed) and MASS
    ACTIVATED (64/64 at m = 0, 56/64 at m = 2/7, 16/64 at m = 3).  The threshold
    tier is 4/64 and its stabiliser is exactly the four BARE HALF-PRESERVING
    TRANSLATIONS, so the obstruction is the ATLAS, not the carrier;
  * THE TIER DEFINITIONS ARE THEMSELVES LOAD-BEARING, AND THE DISCIPLINE IS A
    CHECKED CERTIFICATE.  T1 and T2 are 64/64 only under the CORRECTED reading
    -- inertias throughout plus the spectrum of the FULL H_q, which is a genuine
    congruence invariant of the carrier.  Adding the HALF-BLOCK SPECTRA collapses
    them to 16 and 4, because a move that does not preserve the half changes
    which submatrix is being diagonalised: that is a statement about the FRAME,
    not the carrier.  Both readings are measured and both numbers are printed,
    so the definition is not quietly doing the work;
  * THE SHEAR VALUE AT A NAMED CELL IS BOOKKEEPING, IN THE STRONGEST SENSE.  The
    translation (1,0,1,2) changes sigma at 16 OF 16 CELLS while preserving the
    ENTIRE fixed-frame profile, thresholds included.  No invariant in the lane
    records sigma(c);
  * THE SHEAR ITSELF IS NOT, AND THE SEPARATION IS SHARP.  The global sign flip
    sigma -> -sigma is realised by an EXACT DESCENDED ORTHOGONAL CONGRUENCE (the
    (alpha, beta) = (0,1) Block 142 sign twist), which commutes with theta,
    preserves the half, is ORBIT-INEQUIVALENT to its source, and is INVISIBLE to
    T1-T3 (which are mass-free) and to T4 AT THE FIXTURE MASS -- yet it is
    DETECTED by the T5 threshold pencils, 30 of 32 of them.  The qualification
    the note must carry: T4 DOES see it at m = 3, so "invisible to the census"
    is a FIXTURE-MASS statement and is written that way.  The shear field is
    recorded exactly UP TO Z_4 x Z_4 LATTICE TRANSLATION AND NO FURTHER;
  * AND THE OBVIOUS EXTENSION CANDIDATES ARE NOT GAUGE MOVES.  All three sign
    twists descend and act on the family by b -> (-1)^(alpha+beta) b -- so
    (1,1) acts TRIVIALLY, a footnote and not a third generator -- and the twist
    commutes with all 64 moves, extending the group to ORDER 128 acting on
    carriers through 64.  The extension preserves T1-T4 and BREAKS T5, so it is
    not an additional gauge move.  At a generic cone carrier the physical
    Jacobian is injective, so there is no CONTINUOUS gauge direction either.

Every scientific comparison below is exact SymPy arithmetic; no floats anywhere;
the integer monotonic clock is used only for the runtime gate.

TOOLING DISCLOSURE: every inertia in this runner is computed by SYMMETRIC
CONGRUENCE, delegated to the committed Block 144 helper through the Block
148/147/145 import chain, so the tool this block reasons with is exactly the blob
gate A pins.  The Block 142/143 helper counts DISTINCT real roots and is unsound
on these degenerate spectra; it is deliberately not used, and the calibration
diag(1,1,-2,-2,0) is asserted in gate B.

PROVENANCE DISCLOSURE: the 64-modulus carrier model, the cover Hodge, the
antiperiodic quotient, the action law, the half pairing, the connection data, the
Block 141 healing weights, the canonical theta, the staggered parity X_0, the
descent routine, the sign twists, the 64 covariant moves, the induced modulus map
g*, the cell map and the base orbit carrier are ALL COMMITTED objects (Blocks
105/134/137/141/142/143/144/145/147/148), imported and never re-derived.  This
block adds only the five-tier invariant profile, the frame-transport identity,
the tier measurement, the separation census and the orbit-space accounting.

HYPOTHESES, named and not imported: (H1) the pairing convention is [X Q]_{++} on
the half carrier {p = 0,1}, exactly as Blocks 142/144/145/147/148 used it.
(H2) a FRAME is the triple (pairing operator X, half projector PLUS, atlas
connection d); a move g transports it to (D X D^T, D PLUS, g d g^T) with
D = descend(g).  (H3) a PHYSICAL invariant is a function of the carrier that is
unchanged when the whole frame is transported with it; this is the only sense of
"physical" used here, and every profile item is reported BOTH transported and
fixed-frame.  (H4) the PHYSICAL carrier locus is the committed nonlinear one,
(nu, a, b, 1/nu) with a = nu/(1-s^2), b = -nu s/(1-s^2), nu > 0, |s| < 1; the
Block 145 linear envelope is the ambient 64-modulus space, and the difference is
exactly what the rank-32 accounting measures.  (H5) the mass-completion threshold
tier is carried as a PENCIL CHARACTERISTIC POLYNOMIAL of H_q[+,+]^-1 [X Q]_{++}
so that the comparison is exact and root-free.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import itertools
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp


R = sp.Rational

_FINAL_LOCATION_ROOT = Path(__file__).resolve().parents[1]
# This fallback keeps the scratchpad draft executable before it is moved to
# scripts/, where the final-location branch is used.
ROOT = (
    _FINAL_LOCATION_ROOT
    if (_FINAL_LOCATION_ROOT / ".git").exists()
    else Path(
        "/Users/jonBridger/Projects/Physics-baremetal-probes/"
        ".claude/worktrees/gravity-toe-lane-work-427b0b"
    )
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_general_migration_theorem_2026_08_20 as b148

b147 = b148.b147
b145 = b148.b145
b144 = b148.b144
b143 = b148.b143
b142 = b148.b142
b141 = b148.b141
b137 = b148.b137
b134 = b148.b134
b105 = b148.b105

MASS = b148.MASS


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK148_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK148_RUNNER = (
    "scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py"
)
BLOCK145_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK145_RUNNER = (
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py"
)
PARENT_ARTIFACTS = (
    BLOCK148_NOTE,
    BLOCK148_RUNNER,
    BLOCK145_NOTE,
    BLOCK145_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 148 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
# This block stacks on Block 148, so the parent branch is Block 148's.
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block148-general-migration-theorem-20260820"
)
# Landing supervisor: replace this placeholder with the Block 148 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF when that
# ref exists and through HEAD otherwise (the parent branch may not be published
# yet); either way the binding is real and verifiable, and the immutable commit
# pin lands with the block.
PARENT_COMMIT = "71ee2f8a9faaf0ff2182b0ad3338869dcecf2890"
# Block 147's tip: a real ancestor that PREDATES the pinned Block 148 note and
# runner, so resolving the parent pin there leaves two of the four artifacts
# ABSENT.  It is the honest stale control FOR THIS PIN SET -- the Block 145 tip
# would NOT be, since two of the four artifacts already carry the worktree blobs
# there and a pin resolved at it would still certify on them.  This pin is read
# ONLY under the stale mutation; the baseline gate never requires the stale
# blobs to match.
STALE_PARENT_COMMIT = "7cc1175d087f8aca09471c25acab5fab40350994"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_hodge_law",
    "break_transport_identity",
    "claim_reflections_physical",
    "drop_jacobian_qualifier",
    "wrong_separation_count",
    "wrong_seam_stabilizer",
    "claim_census_carrier_invariant",
    "wrong_threshold_stabilizer",
    "claim_translation_changes_profile",
    "claim_sign_flip_invisible",
    "drop_m3_qualification",
    "claim_twists_are_gauge",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_hodge_law": "B",
    "break_transport_identity": "B",
    "claim_reflections_physical": "C",
    "drop_jacobian_qualifier": "C",
    "wrong_separation_count": "D",
    "wrong_seam_stabilizer": "E",
    "claim_census_carrier_invariant": "E",
    "wrong_threshold_stabilizer": "E",
    "claim_translation_changes_profile": "F",
    "claim_sign_flip_invisible": "F",
    "drop_m3_qualification": "F",
    "claim_twists_are_gauge": "G",
    "drop_n5_fence": "H",
}


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, str, bool]] = []

    def check(self, key: str, statement: str, condition: object) -> None:
        self.results.append((key, statement, bool(condition)))

    def report(self) -> None:
        for key, statement, value in self.results:
            print(f"[{'PASS' if value else 'FAIL'}] {key}: {statement}")
        print(
            "GATES "
            + " ".join(
                f"{key}={'PASS' if value else 'FAIL'}"
                for key, _, value in self.results
            )
        )

    def finish(self) -> int:
        passed = sum(value for _, _, value in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return failed


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def worktree_blob(path: str) -> str:
    return git_output("hash-object", path)


def commit_blob(commit: str, path: str) -> str:
    """The blob at a path in a commit, or "" when the path is absent there.

    Absence is a real answer here: the stale-pin control deliberately probes a
    commit that predates two of the pinned artifacts.
    """
    result = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def resolve_ref(ref: str) -> str:
    result = subprocess.run(
        ("git", "rev-parse", ref),
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def is_hash(value: str) -> bool:
    return re.fullmatch(r"[0-9a-f]{40}", value) is not None


def raw_note() -> str:
    try:
        return NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        return ""


def normalized_note(text: str) -> str:
    return " ".join(text.lower().split())


def compact_note(text: str) -> str:
    return "".join(text.lower().split())


def no_float(value: object) -> bool:
    return b142.no_float(value)


def zero(matrix: sp.MatrixBase) -> bool:
    return b148.zero(matrix)


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Delegated to the COMMITTED Block 144 helper through the Block 148/147/145
    import chain, so that the tool this block reasons with is exactly the blob
    gate A pins.  b142.inertia / b143.inertia count DISTINCT real roots and are
    unsound on these degenerate spectra; the calibration is asserted in gate B.
    """
    return b144.congruence_inertia(matrix)


# ---------------------------------------------------------------------------
# A. authority
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class AuthorityCertificate:
    fixed_authority: bool
    parent_pin_is_commit: bool
    parent_ref_and_ancestry: bool
    parent_artifact_blobs: bool
    stale_parent_artifact_blobs: bool


def resolved_parent_commit() -> str:
    if is_hash(PARENT_COMMIT):
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
        and worktree_blob(REGISTRY_PATH) == WORKTREE_REGISTRY_BLOB
    )

    parent = resolved_parent_commit()
    worktree_blobs = tuple(worktree_blob(path) for path in PARENT_ARTIFACTS)
    committed_blobs = tuple(
        commit_blob(parent, path) for path in PARENT_ARTIFACTS
    )
    stale_blobs = tuple(
        commit_blob(STALE_PARENT_COMMIT, path) for path in PARENT_ARTIFACTS
    )
    return AuthorityCertificate(
        fixed_authority,
        is_hash(PARENT_COMMIT),
        bool(
            is_hash(parent)
            and is_ancestor(parent, "HEAD")
            and (
                not is_hash(PARENT_COMMIT)
                or resolve_ref(PARENT_REF) == PARENT_COMMIT
            )
        ),
        bool(
            len(committed_blobs) == 4
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
        ),
        bool(
            len(stale_blobs) == 4
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
    )


# ---------------------------------------------------------------------------
# the committed model, imported wholesale through Block 148
# ---------------------------------------------------------------------------
SIZE = b148.SIZE                         # 32 cover sites
COVER_T = b148.COVER_T                   # 8
PHYS_T = b148.PHYS_T                     # 4
LX = b148.LX                             # 4
PHYS = b148.PHYS                         # 16 quotient sites
HALF = b148.HALF                         # 8 sites in the positive-time half
ORIGINS = b148.ORIGINS
INDEX = b148.INDEX
PLUS = b148.PLUS
THETA = b148.THETA
X0 = b148.X0
CELLS = b148.CELLS
COORDS = b148.COORDS
EDGE_KEYS = b148.EDGE_KEYS
NU_MODULUS = b148.NU_MODULUS
A_MODULUS = b148.A_MODULUS
B_MODULUS = b148.B_MODULUS
INV_MODULUS = b148.INV_MODULUS
FREE_MODULI = b148.FREE_MODULI
HEALING_WEIGHTS = b148.HEALING_WEIGHTS
ALL_MOVES = b148.ALL_MOVES
MOVES = b148.COVARIANT_MOVES             # the committed 64
THETA_LABEL = b148.THETA_LABEL           # (-1, 7, -1, 0)
THETA_PRIME = b148.THETA_PRIME           # (-1, 7, -1, 1)
GENERATOR_MOVES = b148.GENERATOR_MOVES   # x-shift, t-shift, theta, theta'
SPOT_MOVES = b148.SPOT_MOVES             # 16 moves, evenly spread
SPOT_EDGES = b148.SPOT_EDGES             # 4 healed edges
SHEAR_X, SHEAR_T = b148.SHEAR_X, b148.SHEAR_T
WEIGHT_SCHEMES = b148.WEIGHT_SCHEMES     # healed / alt / undressed

IDENTITY_MOVE = (1, 0, 1, 0)
LAMBDA = sp.Symbol("lam")

# the negative-time half projector, the companion of the committed PLUS
MINUS = sp.zeros(PHYS, HALF)
for _slot in range(HALF):
    MINUS[HALF + _slot, _slot] = 1

PERMUTATION = {label: b148.move_permutation(label) for label in ALL_MOVES}
MOVE_MATRIX = {label: b148.move_matrix(PERMUTATION[label]) for label in ALL_MOVES}
DESCENT = {label: b142.descend(MOVE_MATRIX[label]) for label in ALL_MOVES}

COVER_FREE = b145.cover_hodge_general(*FREE_MODULI)     # 32x32, 64 moduli
HQ_FREE = b145.quotient(COVER_FREE)                     # 16x16, 64 moduli


def herm(matrix: sp.MatrixBase) -> sp.Matrix:
    """The HERMITIAN part (M + M^dagger)/2.  The pairing carries i's, so .H is
    not .T here; gate B pins this against the committed Block 148 symmetric-part
    helper on the objects where the two must agree."""
    matrix = sp.Matrix(matrix)
    return sp.expand((matrix + matrix.H) / 2)


def half_block(operator: sp.MatrixBase, matrix: sp.MatrixBase) -> sp.Matrix:
    """[X Q]_{++} on the half carrier {p = 0,1} (H1)."""
    return sp.expand(PLUS.T * operator * matrix * PLUS)


def cover_action(differential: sp.Matrix, hodge: sp.Matrix, mass) -> sp.Matrix:
    """A = m H + i (H d + d^dagger H) on the cover; the committed action law."""
    return sp.expand(
        mass * hodge + sp.I * (hodge * differential + differential.H * hodge)
    )


def charpoly(matrix: sp.MatrixBase) -> tuple:
    """Exact characteristic polynomial coefficients, root-free (H5)."""
    return tuple(
        value
        for value in sp.Poly(
            sp.expand(sp.Matrix(matrix).charpoly(LAMBDA).as_expr()), LAMBDA
        ).all_coeffs()
    )


def chi(label: tuple) -> int:
    """The CELL-TIME-PARITY character chi(e, p, e, q) = p + (1 - e)/2 mod 2.

    Gate E checks that it is a homomorphism onto Z_2, so its kernel is an
    index-2 subgroup of order 32; it is not assumed to be one.
    """
    return (label[1] + (1 - label[0]) // 2) % 2


KER_CHI = frozenset(label for label in MOVES if chi(label) == 0)
# the eight PARITY-PRESERVING EVEN-x-CENTRED reflections: e = -1, p odd, q even.
# Block 148's four EVEN_CENTRED honest OS reflections are the p in {3,7} half.
EVEN_X_REFLECTIONS = frozenset(
    label
    for label in MOVES
    if label[0] == -1 and label[1] % 2 == 1 and label[3] % 2 == 0
)


def sign_twist(alpha: int, beta: int) -> sp.Matrix:
    """diag((-1)^(alpha t + beta x)) on the cover: the Block 142 sign twist."""
    matrix = sp.zeros(SIZE)
    for time_index in range(COVER_T):
        for space_index in range(LX):
            site = b134.cover_index(time_index, space_index)
            matrix[site, site] = (-1) ** (
                alpha * time_index + beta * space_index
            )
    return matrix


def flip_shear(point: dict) -> dict:
    """sigma -> -sigma on a modulus point: b -> -b with nu and a fixed."""
    flipped = dict(point)
    for cell in CELLS:
        flipped[B_MODULUS[cell]] = -point[B_MODULUS[cell]]
    return flipped


def physical_field(point: dict):
    """Recover (sigma, nu) per cell, or None when the point leaves the physical
    locus (H4).  This is the test the reflections fail off nu = 1."""
    field = {}
    for cell in CELLS:
        volume = point[NU_MODULUS[cell]]
        a_value = point[A_MODULUS[cell]]
        b_value = point[B_MODULUS[cell]]
        inverse = point[INV_MODULUS[cell]]
        if sp.simplify(inverse - 1 / volume) != 0:
            return None
        if sp.simplify(a_value) == 0:
            return None
        shear = sp.simplify(-b_value / a_value)
        if sp.simplify(a_value - volume / (1 - shear ** 2)) != 0:
            return None
        if sp.simplify(b_value + volume * shear / (1 - shear ** 2)) != 0:
            return None
        if not (volume > 0) or not (sp.Abs(shear) < 1):
            return None
        field[cell] = (sp.nsimplify(shear), sp.nsimplify(volume))
    return field


# ---------------------------------------------------------------------------
# the carriers this block measures on
# ---------------------------------------------------------------------------
BASE_FIELD = b148.base_orbit_field()     # the COMMITTED base carrier
FIXTURE_MASS = b134.MASS                 # the committed fixture mass 2/7


def generic_cone_field() -> dict:
    """A second generic cone carrier: 16 pairwise distinct shears and volumes,
    with no accidental x- or t-periodicity.  Added by this block."""
    return {
        cell: (
            R(2 * (4 * cell[0] + cell[1]) - 15, 37),
            R(4 * cell[0] + cell[1] + 2, 11),
        )
        for cell in CELLS
    }


def flat_field() -> dict:
    return {cell: (sp.Integer(0), sp.Integer(1)) for cell in CELLS}


def relabelled(field: dict, relabel) -> dict:
    return {relabel(cell): value for cell, value in field.items()}


def unit_volume(field: dict) -> dict:
    return {cell: (field[cell][0], sp.Integer(1)) for cell in CELLS}


# Eight carriers, of which THREE share the (sigma, nu) MULTISET exactly -- so
# the census cannot be separating them by a cheap multiset accident.
CENSUS_CARRIERS = (
    ("base", BASE_FIELD),
    ("base-transposed", relabelled(BASE_FIELD, lambda c: (c[1], c[0]))),
    (
        "base-xsheared",
        relabelled(BASE_FIELD, lambda c: (c[0], (3 * c[1] + c[0]) % LX)),
    ),
    ("flat", flat_field()),
    ("staircase", b105.overlap_field()),
    ("b145-witness", b145.witness_field()),
    ("b148-escape", b148.escape_witness_field()),
    ("generic-cone", generic_cone_field()),
)
MULTISET_SHARERS = ("base", "base-transposed", "base-xsheared")

# the nu = 1 slice, where the physical Jacobian degenerates
NU1_CARRIERS = (
    ("flat", flat_field()),
    ("base-nu1", unit_volume(BASE_FIELD)),
    ("generic-nu1", unit_volume(generic_cone_field())),
    ("b148-escape", b148.escape_witness_field()),
)
GENERIC_CARRIERS = (
    ("base", BASE_FIELD),
    ("generic-cone", generic_cone_field()),
    ("staircase", b105.overlap_field()),
)


# ---------------------------------------------------------------------------
# the certificate constants this runner is claiming
# ---------------------------------------------------------------------------
GROUP_ORDER = 64
CARRIER_IMAGE_ORDER = 32
REFLECTION_COUNT = 32
TRANSLATION_COUNT = 32
TRANSLATION_IMAGE_ORDER = 16             # Z_4 x Z_4
TRANSLATION_KERNEL = ((1, 0, 1, 0), (1, 4, 1, 0))
Z4XZ4_ORDER_MULTISET = ((1, 1), (2, 3), (4, 12))
MODULI_TO_HODGE_RANK = 32                # of 64: half the envelope is invisible
PHYSICAL_PARAMETERS = 32                 # (sigma, nu) on 16 cells
JACOBIAN_GENERIC_RANK = 32
JACOBIAN_NU1_RANK = 30
JACOBIAN_NU1_KERNEL_DIM = 2

HODGE_LAW_GENERATORS = 4
HODGE_LAW_SPOT = 16
HODGE_LAW_DEEP = 64
TRANSPORT_GENERATOR_HITS = 64            # 4 generators x 16 healed edges
TRANSPORT_SPOT_HITS = 64                 # 16 moves x 4 healed edges
TRANSPORT_DEEP_HITS = 1024               # 64 moves x 16 edges, behind --deep

CENSUS_PAIRS = 28                        # C(8, 2)
TIER_ALONE_COUNTS = {
    "T1": 27, "T2": 7, "T3": 7, "T4": 13, "T5": 28,
}

STABILIZER_T1 = 64
STABILIZER_T2 = 64
STABILIZER_T1_WITH_HALF_SPECTRUM = 16
STABILIZER_T2_WITH_GRAM_SPECTRA = 4
HALF_PRESERVER_COUNT = 16
STABILIZER_T3 = 32
STABILIZER_T4 = 56
STABILIZER_T5 = 4
THRESHOLD_STABILIZER = (
    (1, 0, 1, 0), (1, 0, 1, 2), (1, 4, 1, 0), (1, 4, 1, 2)
)
WRONG_THRESHOLD_STABILIZER = (
    (1, 0, 1, 0), (1, 2, 1, 0), (1, 4, 1, 0), (1, 4, 1, 2)
)
CENSUS_MASSES = (sp.Integer(0), FIXTURE_MASS, sp.Integer(3))
CENSUS_MASS_STABILIZERS = (64, 56, 16)
CENSUS_DRESSING_STABILIZERS = (("healed", 56), ("alt", 56), ("undressed", 64))
CARRIER_SPECIFIC_SEAM = ("generic-cone", 64)   # nonzero shear, T3 = 64/64
BARE_MOVES = 32
BARE_TRANSLATIONS = 16
BARE_HALF_PRESERVING = 8                 # 4 translations + 4 reflections

SHEAR_SHIFT = (1, 0, 1, 2)               # the profile-preserving x-shift-by-2
SHEAR_SHIFT_CELLS = 16                   # sigma moves at 16 of 16 cells
FLIP_MASSES = (
    sp.Integer(0), FIXTURE_MASS, sp.Integer(1), sp.Integer(3), R(22, 15)
)
FLIP_CENSUS_VISIBILITY = (True, True, True, False, False)
FLIP_M3_INDEX = 3                        # the m = 3 entry of FLIP_MASSES
SPOT_PENCILS = tuple(
    ((0, index), name) for index in range(LX) for name in ("theta", "X0")
)
SPOT_PENCIL_MINIMUM = 4                  # in-gate floor; measured value is 8
DEEP_FLIP_PENCILS = 30                   # of 32, behind --deep
TOTAL_PENCILS = 32
SIGN_TWISTS = ((1, 0), (0, 1), (1, 1))
TWIST_EXTENSION_ORDER = 128
TWIST_CARRIER_IMAGES = 64                # 32 move images x the flip
RUNTIME_BUDGET_SEC = 600


def staggered_volume_kernel() -> tuple:
    """The two claimed kernel directions of the physical Jacobian at the FLAT
    nu = 1 carrier, written out rather than read off a nullspace basis: pure
    VOLUME directions, one supported on each cell-parity class, entries +-1.
    """
    vectors = []
    for parity in (0, 1):
        vector = {}
        for cell in CELLS:
            time_index, space_index = cell
            if (time_index + space_index) % 2 != parity:
                continue
            exponent = time_index // 2 + space_index // 2
            if parity == 1:
                exponent += space_index
            vector[cell] = sp.Integer((-1) ** exponent)
        vectors.append(vector)
    return tuple(vectors)


# ---------------------------------------------------------------------------
# THE FIVE-TIER FIXED-FRAME PROFILE
# ---------------------------------------------------------------------------
# T1  frame-FREE: spec(H_q), inertia(H_q), inertia(H_q[+,+]).  Carrier-intrinsic
#     up to congruence by the descended signed permutations.
# T2  half + pairing operator, NO connection: the inertias of the two displayed
#     mass Grams, Block 147's Herm[theta H_q]_{++} and Block 148's X_0 Gram.
# T3  half only: rank H_q[-,+], Block 145's seam Gram rank.
# T4  half + operator + CONNECTION: the inertia census of the 32 healed-edge
#     pairings (16 edges x {theta, X_0}) at a given mass.
# T5  T4 plus the mass completion: the exact pencil characteristic polynomials
#     of H_q[+,+]^-1 Herm[X Q]_{++} (H5).
#
# THE DEFINITION DISCIPLINE, and it is load-bearing.  T1 and T2 use INERTIAS
# plus the spectrum of the FULL H_q, and deliberately NOT the spectra of the
# HALF BLOCKS.  A move that does not preserve the half {p = 0,1} changes WHICH
# submatrix is being diagonalised, so a half-block spectrum measures the frame
# and not the carrier.  Gate E measures BOTH readings and prints both numbers.
class Carrier:
    """Everything the profile needs for one modulus point, at any mass.

    The action is AFFINE in m -- A(m) = m H + i(H d + d^dagger H) -- so the
    mass-free block and the Hodge block of each pairing are computed once and
    every mass is a cheap exact recombination.  That is what makes the multi-
    mass sweeps affordable without ever approximating anything.
    """

    def __init__(self, point: dict, scheme: str = "healed") -> None:
        self.point = point
        self.scheme = scheme
        self.cover = sp.expand(COVER_FREE.xreplace(point))
        self.hodge = sp.expand(HQ_FREE.xreplace(point))
        self.half_hodge = self.hodge[:HALF, :HALF]
        self._blocks = None
        self._inverse = None

    def blocks(self) -> dict:
        if self._blocks is None:
            table = EDGE_TABLES[self.scheme]
            quotient_hodge = b145.quotient(self.cover)
            out = {}
            for key in EDGE_KEYS:
                free = b145.quotient(
                    cover_action(table[key], self.cover, sp.Integer(0))
                )
                for name, operator in (("theta", THETA), ("X0", X0)):
                    out[(key, name)] = (
                        herm(half_block(operator, free)),
                        herm(half_block(operator, quotient_hodge)),
                    )
            self._blocks = out
        return self._blocks

    def pairing(self, key: tuple, mass) -> sp.Matrix:
        free_part, hodge_part = self.blocks()[key]
        return sp.expand(free_part + mass * hodge_part)

    def inverse_half(self) -> sp.Matrix:
        if self._inverse is None:
            self._inverse = sp.Matrix(self.half_hodge).inv()
        return self._inverse

    # --- tier 1 -----------------------------------------------------------
    def t1(self) -> tuple:
        return (
            charpoly(self.hodge),
            congruence_inertia(self.hodge),
            congruence_inertia(self.half_hodge),
        )

    def t1_with_half_spectrum(self) -> tuple:
        return self.t1() + (charpoly(self.half_hodge),)

    # --- tier 2 -----------------------------------------------------------
    def grams(self) -> tuple:
        return (
            herm(half_block(THETA, self.hodge)),
            herm(half_block(X0, self.hodge)),
        )

    def t2(self) -> tuple:
        return tuple(congruence_inertia(gram) for gram in self.grams())

    def t2_with_gram_spectra(self) -> tuple:
        return self.t2() + tuple(charpoly(gram) for gram in self.grams())

    # --- tier 3 -----------------------------------------------------------
    def t3(self) -> int:
        return sp.Matrix(sp.expand(MINUS.T * self.hodge * PLUS)).rank()

    # --- tier 4 -----------------------------------------------------------
    def t4(self, mass) -> tuple:
        return tuple(
            sorted(
                congruence_inertia(self.pairing(key, mass))
                for key in self.blocks()
            )
        )

    def t4_table(self, mass) -> dict:
        return {
            key: congruence_inertia(self.pairing(key, mass))
            for key in self.blocks()
        }

    # --- tier 5 -----------------------------------------------------------
    def t5(self, mass) -> tuple:
        inverse = self.inverse_half()
        return tuple(
            sorted(
                charpoly(sp.expand(inverse * self.pairing(key, mass)))
                for key in self.blocks()
            )
        )

    def t5_table(self, mass, keys=None) -> dict:
        inverse = self.inverse_half()
        return {
            key: charpoly(sp.expand(inverse * self.pairing(key, mass)))
            for key in (self.blocks() if keys is None else keys)
        }

    def profile(self, mass) -> tuple:
        return (self.t1(), self.t2(), self.t3(), self.t4(mass), self.t5(mass))


# the three committed dressings, at the committed numeric fixture (3/5, 4/5)
_FIXTURE_DIFFERENTIALS, _FIXTURE_STAR = b145.connection(b134.S_X, b134.S_T)
EDGE_TABLES = {
    name: b145.edge_differentials(
        _FIXTURE_DIFFERENTIALS, _FIXTURE_STAR, weights
    )
    for name, weights in WEIGHT_SCHEMES
}
PARAMETER_ORDER = tuple(
    (cell, kind) for cell in CELLS for kind in ("sigma", "nu")
)
MODULUS_POSITION = {value: index for index, value in enumerate(COORDS)}
SYMMETRIC_ENTRIES = tuple(
    (i, j) for i in range(PHYS) for j in range(i, PHYS)
)
HODGE_SPAN = sp.Matrix(
    [
        [sp.expand(HQ_FREE[i, j]).coeff(value, 1) for (i, j) in SYMMETRIC_ENTRIES]
        for value in COORDS
    ]
)
_SHEAR_SYMBOL = sp.Symbol("sg", real=True)
_VOLUME_SYMBOL = sp.Symbol("vl", positive=True)
_LOCAL_CHART = (
    _VOLUME_SYMBOL,
    _VOLUME_SYMBOL / (1 - _SHEAR_SYMBOL ** 2),
    -_VOLUME_SYMBOL * _SHEAR_SYMBOL / (1 - _SHEAR_SYMBOL ** 2),
    1 / _VOLUME_SYMBOL,
)
_LOCAL_JACOBIAN = tuple(
    tuple(sp.diff(entry, parameter) for entry in _LOCAL_CHART)
    for parameter in (_SHEAR_SYMBOL, _VOLUME_SYMBOL)
)


def physical_jacobian(field: dict) -> sp.Matrix:
    """d H_q / d(sigma, nu) at a physical carrier, 32 rows in PARAMETER_ORDER.

    The chain rule is applied EXACTLY and in factored form: the (sigma, nu) ->
    (nu, a, b, 1/nu) block is written out per cell and composed with the SINGLE
    linear map moduli -> H_q entries, so no 16x16 rational matrix is ever
    differentiated or simplified.
    """
    rows = []
    for cell in CELLS:
        at_cell = {
            _SHEAR_SYMBOL: field[cell][0],
            _VOLUME_SYMBOL: field[cell][1],
        }
        slots = (
            NU_MODULUS[cell],
            A_MODULUS[cell],
            B_MODULUS[cell],
            INV_MODULUS[cell],
        )
        for parameter_row in _LOCAL_JACOBIAN:
            row = [sp.Integer(0)] * len(COORDS)
            for slot, entry in zip(slots, parameter_row):
                row[MODULUS_POSITION[slot]] = sp.cancel(entry.xreplace(at_cell))
            rows.append(row)
    return sp.Matrix(rows) * HODGE_SPAN


def orbit_keys(point: dict) -> set:
    return {b148.point_key(b148.push_point(point, label)) for label in MOVES}


def image_classes(point: dict) -> dict:
    classes: dict = {}
    for label in MOVES:
        classes.setdefault(
            b148.point_key(b148.push_point(point, label)), []
        ).append(label)
    return classes


def stabilizer(point: dict, reader, scheme: str = "healed") -> frozenset:
    """The set of moves whose IMAGE carrier reads the same as the base one.

    `reader` is any function of a Carrier; one Carrier is built per DISTINCT
    image, so the 64 moves cost 32 constructions.
    """
    classes = image_classes(point)
    reference = reader(Carrier(point, scheme))
    keep: list = []
    for key, labels in classes.items():
        carrier = Carrier(b148.push_point(point, labels[0]), scheme)
        if reader(carrier) == reference:
            keep.extend(labels)
    return frozenset(keep)


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the transport identity
    inertia_calibration: bool
    hermitian_conventions_agree: bool
    action_law_pinned: bool
    hodge_law_generators: tuple
    hodge_law_spot: tuple
    hodge_law_deep: tuple
    transport_generators: tuple
    transport_spot: tuple
    transport_deep: tuple
    # C: the physical gauge group
    volume_inversion: tuple
    translation_relabel: tuple
    physical_generic: tuple
    physical_unit: tuple
    translation_image_order: int
    translation_kernel: tuple
    translation_order_multiset: tuple
    full_image_order: int
    hodge_span_faithful: bool
    hodge_is_linear: bool
    moduli_to_hodge_rank: int
    jacobian_generic: tuple
    jacobian_nu1: tuple
    jacobian_flat_kernel: tuple
    # D: separation
    census_in_cone: bool
    census_multiset_sharers: tuple
    census_orbit_inequivalent: tuple
    census_profile_separation: tuple
    census_tier_alone: tuple
    # E: the stabilizer split
    chi_homomorphism: bool
    chi_kernel_order: int
    chi_contains_reflections: bool
    stabilizer_t1: int
    stabilizer_t2: int
    stabilizer_t1_half_spectrum: int
    stabilizer_t2_gram_spectra: int
    half_preservers: int
    t1_half_spectrum_is_half_preservers: bool
    stabilizer_t3: int
    seam_is_ker_chi: bool
    stabilizer_t4_masses: tuple
    census_breakers_are_even_x: bool
    census_dressing: tuple
    stabilizer_t5: int
    threshold_stabilizer_set: tuple
    bare_moves: int
    bare_translations: int
    bare_half_preserving: int
    theta_is_bare: bool
    theta_prime_is_bare: bool
    unmatched_moves: int
    bare_cross_validated: bool
    threshold_is_bare_half_preserving_translations: bool
    carrier_specific_seam: tuple
    # F: the sharp classification
    shear_shift_cells: int
    shift_preserves_t1_t4: bool
    shift_preserves_spot_pencils: bool
    shift_preserves_full_profile: tuple
    twist_descends: bool
    twist_orthogonal: bool
    twist_commutes_with_theta: bool
    twist_preserves_half: bool
    twist_realises_flip: bool
    flip_invisible_t1_t3: bool
    flip_census_visibility: tuple
    flip_census_edges_at_m3: int
    flip_spot_pencils: tuple
    flip_deep_pencils: tuple
    flip_orbit_inequivalent: bool
    census_palindromic: bool
    # G: the extension candidates
    twist_laws: tuple
    twist_trivial: tuple
    twist_commutation: bool
    twist_extension_order: int
    twist_carrier_images: int
    twists_preserve_t1_t4: bool
    twists_break_t5: bool
    no_continuous_gauge: bool
    # global
    exact_no_float: bool
    scope: dict


def measure(deep: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    # The congruence routine is calibrated here, in the measurement pass, on
    # matrices whose inertia is known by inspection and on which the
    # root-counting helper of Blocks 142/143 is provably wrong.
    inertia_calibration = bool(
        congruence_inertia(sp.diag(1, 2, -3, R(5, 7))) == (3, 0, 1)
        and congruence_inertia(sp.diag(1, 1, -2, -2, 0)) == (2, 1, 2)
        and b142.inertia(sp.diag(1, 1, -2, -2, 0)) != (2, 1, 2)
    )

    # --- B: the transport identity ------------------------------------------
    differentials, star_form = b145.connection(SHEAR_X, SHEAR_T)
    symbolic_edges = b145.edge_differentials(
        differentials, star_form, HEALING_WEIGHTS
    )
    symbolic_cover = {
        key: sp.expand(cover_action(symbolic_edges[key], COVER_FREE, MASS))
        for key in EDGE_KEYS
    }
    symbolic_quotient = {
        key: b145.quotient(symbolic_cover[key]) for key in EDGE_KEYS
    }
    # the inlined action law is pinned against the committed Block 145 routine
    # rather than trusted
    action_law_pinned = all(
        zero(
            sp.expand(
                symbolic_quotient[key]
                - b145.quotient_action(symbolic_edges[key], COVER_FREE, MASS)
            )
        )
        for key in ((0, 0), (2, 3))
    )
    # the Hermitian-part convention used here is pinned against the committed
    # Block 148 symmetric-part helper on the objects where the two must agree
    hermitian_conventions_agree = all(
        zero(
            sp.expand(
                herm(half_block(operator, HQ_FREE))
                - b148.herm(half_block(operator, HQ_FREE))
            )
        )
        for operator in (THETA, X0)
    )

    def hodge_law(label: tuple) -> bool:
        """H_q(g* y) = D H_q(y) D^T, symbolic in all 64 moduli."""
        descent = DESCENT[label]
        return zero(
            sp.expand(
                HQ_FREE.xreplace(b148.induced_substitution(label))
                - descent * HQ_FREE * descent.T
            )
        )

    hodge_law_generators = (
        sum(1 for label in GENERATOR_MOVES if hodge_law(label)),
        len(GENERATOR_MOVES),
    )
    hodge_law_spot = (
        sum(1 for label in SPOT_MOVES if hodge_law(label)),
        len(SPOT_MOVES),
    )
    hodge_law_deep = (
        (sum(1 for label in MOVES if hodge_law(label)), len(MOVES))
        if deep
        else (0, 0)
    )

    base_pairings = {
        (key, name): sp.expand(
            PLUS.T * operator * symbolic_quotient[key] * PLUS
        )
        for key in EDGE_KEYS
        for name, operator in (("theta", THETA), ("X0", X0))
    }

    def transport_hits(labels: tuple, keys: tuple) -> tuple:
        """The FRAME-TRANSPORT identity, as an EXACT MATRIX EQUALITY:

            PLUS^T X Q[d; y] PLUS
              = (D PLUS)^T (D X D^T) Q[g d g^T; g* y] (D PLUS)

        for BOTH displayed conventions X in {theta, X_0}, symbolic in all 64
        moduli, in m and in the fixture shears (s_x, s_t).  Nothing is
        congruence here: the two sides are the SAME MATRIX.
        """
        hits = {"theta": 0, "X0": 0}
        for label in labels:
            descent = DESCENT[label]
            move = MOVE_MATRIX[label]
            moved_cover = sp.expand(
                COVER_FREE.xreplace(b148.induced_substitution(label))
            )
            moved_plus = sp.expand(descent * PLUS)
            moved_operator = {
                name: sp.expand(descent * operator * descent.T)
                for name, operator in (("theta", THETA), ("X0", X0))
            }
            for key in keys:
                transported_edge = sp.expand(
                    move * symbolic_edges[key] * move.T
                )
                moved = b145.quotient(
                    cover_action(transported_edge, moved_cover, MASS)
                )
                for name in ("theta", "X0"):
                    if zero(
                        sp.expand(
                            moved_plus.T
                            * moved_operator[name]
                            * moved
                            * moved_plus
                            - base_pairings[(key, name)]
                        )
                    ):
                        hits[name] += 1
        return (hits["theta"], hits["X0"], len(labels) * len(keys))

    transport_generators = transport_hits(GENERATOR_MOVES, EDGE_KEYS)
    transport_spot = transport_hits(SPOT_MOVES, SPOT_EDGES)
    transport_deep = (
        transport_hits(MOVES, EDGE_KEYS) if deep else (0, 0, 0)
    )

    # --- C: the physical gauge group ----------------------------------------
    reflections = tuple(label for label in MOVES if label[0] == -1)
    translations = tuple(label for label in MOVES if label[0] == 1)

    def acts_by(label: tuple, swap: bool) -> bool:
        substitution = b148.induced_substitution(label)
        relabel = b148.cell_map(label)
        return all(
            substitution[NU_MODULUS[relabel(cell)]]
            == (INV_MODULUS[cell] if swap else NU_MODULUS[cell])
            and substitution[INV_MODULUS[relabel(cell)]]
            == (NU_MODULUS[cell] if swap else INV_MODULUS[cell])
            and substitution[A_MODULUS[relabel(cell)]] == A_MODULUS[cell]
            and substitution[B_MODULUS[relabel(cell)]] == B_MODULUS[cell]
            for cell in CELLS
        )

    volume_inversion = (
        sum(1 for label in reflections if acts_by(label, True)),
        len(reflections),
    )
    translation_relabel = (
        sum(1 for label in translations if acts_by(label, False)),
        len(translations),
    )

    generic_field = generic_cone_field()
    generic_point = b147.modulus_point(generic_field)
    unit_point = b147.modulus_point(unit_volume(generic_field))
    physical_generic = (
        sum(
            1
            for label in reflections
            if physical_field(b148.push_point(generic_point, label)) is not None
        ),
        sum(
            1
            for label in translations
            if physical_field(b148.push_point(generic_point, label)) is not None
        ),
        len(reflections),
    )
    physical_unit = (
        sum(
            1
            for label in reflections
            if physical_field(b148.push_point(unit_point, label)) is not None
        ),
        sum(
            1
            for label in translations
            if physical_field(b148.push_point(unit_point, label)) is not None
        ),
        len(reflections),
    )

    base_point = b147.modulus_point(BASE_FIELD)
    base_key = b148.point_key(base_point)
    translation_classes: dict = {}
    for label in translations:
        translation_classes.setdefault(
            b148.point_key(b148.push_point(base_point, label)), []
        ).append(label)
    translation_image_order = len(translation_classes)
    translation_kernel = tuple(sorted(translation_classes.get(base_key, ())))

    def translation_power(label: tuple, exponent: int) -> tuple:
        return (
            1,
            (label[1] * exponent) % COVER_T,
            1,
            (label[3] * exponent) % LX,
        )

    element_orders = []
    for labels in translation_classes.values():
        label = labels[0]
        element_orders.append(
            min(
                exponent
                for exponent in range(1, 4 * LX + 1)
                if b148.point_key(
                    b148.push_point(
                        base_point, translation_power(label, exponent)
                    )
                )
                == base_key
            )
        )
    translation_order_multiset = tuple(sorted(Counter(element_orders).items()))
    full_image_order = len(image_classes(base_point))

    hodge_is_linear = bool(b145.is_linear_in_moduli(HQ_FREE))
    hodge_span_faithful = all(
        sp.expand(
            HQ_FREE[i, j]
            - sum(
                HODGE_SPAN[row, column] * COORDS[row]
                for row in range(len(COORDS))
            )
        )
        == 0
        for column, (i, j) in enumerate(SYMMETRIC_ENTRIES)
    )
    moduli_to_hodge_rank = HODGE_SPAN.rank()
    jacobian_generic = tuple(
        (name, physical_jacobian(field).rank())
        for name, field in GENERIC_CARRIERS
    )
    jacobian_nu1 = tuple(
        (name, physical_jacobian(field).rank())
        for name, field in NU1_CARRIERS
    )
    # THE JACOBIAN QUALIFIER, carried as an explicit certificate rather than as
    # a nullspace printout: the two claimed staggered VOLUME directions are
    # written out and shown to annihilate the flat nu = 1 Jacobian, and the
    # kernel is shown to be exactly two-dimensional and sigma-free there.
    flat_jacobian = physical_jacobian(flat_field())
    kernel_basis = sp.Matrix(flat_jacobian.T).nullspace()
    kernel_is_volume_only = all(
        all(
            vector[index] == 0
            for index, (_cell, kind) in enumerate(PARAMETER_ORDER)
            if kind == "sigma"
        )
        for vector in kernel_basis
    )
    staggered = staggered_volume_kernel()
    staggered_matrix = sp.Matrix(
        [
            [
                vector.get(cell, sp.Integer(0)) if kind == "nu" else sp.Integer(0)
                for (cell, kind) in PARAMETER_ORDER
            ]
            for vector in staggered
        ]
    )
    jacobian_flat_kernel = (
        len(kernel_basis),
        kernel_is_volume_only,
        zero(sp.expand(staggered_matrix * flat_jacobian)),
        staggered_matrix.rank(),
        tuple(len(vector) for vector in staggered),
        all(
            abs(value) == 1
            for vector in staggered
            for value in vector.values()
        ),
        tuple(
            tuple(sorted({(cell[0] + cell[1]) % 2 for cell in vector}))
            for vector in staggered
        ),
    )

    # --- D: separation -------------------------------------------------------
    census_fields = dict(CENSUS_CARRIERS)
    census_names = tuple(name for name, _ in CENSUS_CARRIERS)
    census_in_cone = all(
        b145.in_admissible_cone(field) for _, field in CENSUS_CARRIERS
    )
    census_multisets = {
        name: tuple(sorted(str(value) for value in field.values()))
        for name, field in CENSUS_CARRIERS
    }
    census_multiset_sharers = tuple(
        sorted(
            name
            for name in census_names
            if census_multisets[name] == census_multisets["base"]
        )
    )
    census_points = {
        name: b147.modulus_point(census_fields[name]) for name in census_names
    }
    census_orbits = {
        name: orbit_keys(census_points[name]) for name in census_names
    }
    census_carriers = {name: Carrier(census_points[name]) for name in census_names}
    census_profiles = {
        name: census_carriers[name].profile(FIXTURE_MASS)
        for name in census_names
    }
    census_pairs = tuple(itertools.combinations(census_names, 2))
    census_orbit_inequivalent = (
        sum(
            1
            for left, right in census_pairs
            if b148.point_key(census_points[right]) not in census_orbits[left]
        ),
        len(census_pairs),
    )
    census_profile_separation = (
        sum(
            1
            for left, right in census_pairs
            if census_profiles[left] != census_profiles[right]
        ),
        len(census_pairs),
    )
    census_tier_alone = tuple(
        (
            tier,
            sum(
                1
                for left, right in census_pairs
                if census_profiles[left][index] != census_profiles[right][index]
            ),
        )
        for index, tier in enumerate(("T1", "T2", "T3", "T4", "T5"))
    )

    # --- E: the stabilizer split --------------------------------------------
    chi_homomorphism = all(
        chi(b148.compose_labels(left, right)) == (chi(left) + chi(right)) % 2
        for left in MOVES
        for right in MOVES
    )
    chi_kernel_order = len(KER_CHI)
    chi_contains_reflections = bool(
        THETA_LABEL in KER_CHI and THETA_PRIME in KER_CHI
    )

    base_classes = image_classes(base_point)
    base_carrier = census_carriers["base"]
    image_carriers = {
        key: Carrier(b148.push_point(base_point, labels[0]))
        for key, labels in base_classes.items()
    }

    def split(reader, carriers=None, classes=None, reference_carrier=None):
        carriers = image_carriers if carriers is None else carriers
        classes = base_classes if classes is None else classes
        reference_carrier = (
            base_carrier if reference_carrier is None else reference_carrier
        )
        reference = reader(reference_carrier)
        keep: list = []
        for key, labels in classes.items():
            if reader(carriers[key]) == reference:
                keep.extend(labels)
        return frozenset(keep)

    t1_set = split(lambda carrier: carrier.t1())
    t1_half_set = split(lambda carrier: carrier.t1_with_half_spectrum())
    t2_set = split(lambda carrier: carrier.t2())
    t2_gram_set = split(lambda carrier: carrier.t2_with_gram_spectra())
    t3_set = split(lambda carrier: carrier.t3())
    t4_sets = tuple(
        split(lambda carrier, mass=mass: carrier.t4(mass))
        for mass in CENSUS_MASSES
    )
    t5_set = split(lambda carrier: carrier.t5(FIXTURE_MASS))

    half_preserving = frozenset(
        label
        for label in MOVES
        if zero(sp.expand(MINUS.T * DESCENT[label] * PLUS))
    )
    fixture_index = CENSUS_MASSES.index(FIXTURE_MASS)
    census_dressing = []
    for name, _weights in WEIGHT_SCHEMES:
        if name == "healed":
            census_dressing.append((name, len(t4_sets[fixture_index])))
            continue
        scheme_carriers = {
            key: Carrier(b148.push_point(base_point, labels[0]), name)
            for key, labels in base_classes.items()
        }
        census_dressing.append(
            (
                name,
                len(
                    split(
                        lambda carrier: carrier.t4(FIXTURE_MASS),
                        scheme_carriers,
                        base_classes,
                        Carrier(base_point, name),
                    )
                ),
            )
        )
    census_dressing = tuple(census_dressing)

    # the BARE ATLAS diagnosis, on the SYMBOLIC connection table
    atlas = {INDEX[origin]: differentials[origin] for origin in ORIGINS}
    variants = {
        "": differentials,
        "|s_t": b145.connection(SHEAR_X, -SHEAR_T)[0],
        "|s_x": b145.connection(-SHEAR_X, SHEAR_T)[0],
        "|both": b145.connection(-SHEAR_X, -SHEAR_T)[0],
    }
    lift_t, lift_x = b105.shift_lifts()
    gauge_x = b134.lifted(lift_x)
    gauge_t = b134.lifted(lift_t)
    gauges = {
        "I": sp.eye(SIZE),
        "r_x": gauge_x,
        "r_t": gauge_t,
        "r_x r_t": sp.expand(gauge_x * gauge_t),
    }
    lookup: dict = {}
    for gauge_name, gauge in gauges.items():
        gauge_inverse = gauge.inv()
        for variant_name, table in variants.items():
            for origin in ORIGINS:
                for dagger in (False, True):
                    base = table[origin].H if dagger else table[origin]
                    for sign in (1, -1):
                        key = sp.ImmutableMatrix(
                            sp.expand(sign * gauge * base * gauge_inverse)
                        )
                        lookup.setdefault(key, set()).add(
                            (
                                gauge_name,
                                INDEX[origin],
                                variant_name,
                                dagger,
                                sign,
                            )
                        )

    def classify(label: tuple) -> dict:
        matrix = MOVE_MATRIX[label]
        inverse = matrix.T
        return {
            chart: lookup.get(
                sp.ImmutableMatrix(
                    sp.expand(matrix * atlas[chart] * inverse)
                ),
                frozenset(),
            )
            for chart in range(4)
        }

    bare_labels: list = []
    unmatched_moves = 0
    for label in MOVES:
        hits = classify(label)
        if any(not hits[chart] for chart in range(4)):
            unmatched_moves += 1
        elif all(
            any(hit[0] == "I" for hit in hits[chart]) for chart in range(4)
        ):
            bare_labels.append(label)
    bare_set = frozenset(bare_labels)
    # the hash lookup is a speed device, so it is cross-validated against an
    # explicit symbolic comparison on the escape reflection's first chart
    transported_chart = sp.expand(
        MOVE_MATRIX[THETA_PRIME] * atlas[0] * MOVE_MATRIX[THETA_PRIME].T
    )
    direct = {
        (gauge_name, INDEX[origin], variant_name, dagger, sign)
        for gauge_name, gauge in gauges.items()
        for variant_name, table in variants.items()
        for origin in ORIGINS
        for dagger in (False, True)
        for sign in (1, -1)
        if zero(
            sp.expand(
                transported_chart
                - sign
                * gauge
                * (table[origin].H if dagger else table[origin])
                * gauge.inv()
            )
        )
    }
    bare_cross_validated = direct == set(classify(THETA_PRIME)[0])

    control_name, _control_value = CARRIER_SPECIFIC_SEAM
    control_field = census_fields[control_name]
    carrier_specific_seam = (
        control_name,
        len(
            stabilizer(census_points[control_name], lambda carrier: carrier.t3())
        ),
        any(sp.simplify(control_field[cell][0]) != 0 for cell in CELLS),
    )

    # --- F: the sharp classification ----------------------------------------
    shift_point = b148.push_point(base_point, SHEAR_SHIFT)
    shift_field = physical_field(shift_point)
    shear_shift_cells = (
        sum(
            1
            for cell in CELLS
            if sp.simplify(shift_field[cell][0] - BASE_FIELD[cell][0]) != 0
        )
        if shift_field is not None
        else -1
    )
    shift_carrier = Carrier(shift_point)
    shift_preserves_t1_t4 = bool(
        shift_carrier.t1() == base_carrier.t1()
        and shift_carrier.t2() == base_carrier.t2()
        and shift_carrier.t3() == base_carrier.t3()
        and shift_carrier.t4(FIXTURE_MASS) == base_carrier.t4(FIXTURE_MASS)
    )
    base_spot = base_carrier.t5_table(FIXTURE_MASS, SPOT_PENCILS)
    shift_preserves_spot_pencils = (
        shift_carrier.t5_table(FIXTURE_MASS, SPOT_PENCILS) == base_spot
    )
    if deep:
        base_full = base_carrier.t5_table(FIXTURE_MASS)
        shift_full = shift_carrier.t5_table(FIXTURE_MASS)
        shift_preserves_full_profile = (
            sum(1 for key in base_full if base_full[key] == shift_full[key]),
            len(base_full),
        )
    else:
        shift_preserves_full_profile = (0, 0)

    twist_matrix = sign_twist(0, 1)
    twist_descent = b142.descend(twist_matrix)
    twist_descends = twist_descent is not None
    twist_orthogonal = bool(
        twist_descends
        and zero(sp.expand(twist_descent * twist_descent.T - sp.eye(PHYS)))
    )
    twist_commutes_with_theta = bool(
        twist_descends
        and zero(sp.expand(twist_descent * THETA - THETA * twist_descent))
    )
    twist_preserves_half = bool(
        twist_descends and zero(sp.expand(MINUS.T * twist_descent * PLUS))
    )
    flip_point = flip_shear(base_point)
    flip_field = physical_field(flip_point)
    twist_realises_flip = bool(
        twist_descends
        and zero(
            sp.expand(
                HQ_FREE.xreplace(flip_point)
                - twist_descent * HQ_FREE.xreplace(base_point) * twist_descent.T
            )
        )
        and flip_field is not None
        and all(
            sp.simplify(flip_field[cell][0] + BASE_FIELD[cell][0]) == 0
            and sp.simplify(flip_field[cell][1] - BASE_FIELD[cell][1]) == 0
            for cell in CELLS
        )
    )

    flip_carrier = Carrier(flip_point)
    flip_invisible_t1_t3 = bool(
        flip_carrier.t1() == base_carrier.t1()
        and flip_carrier.t2() == base_carrier.t2()
        and flip_carrier.t3() == base_carrier.t3()
    )
    flip_census_visibility = tuple(
        flip_carrier.t4(mass) == base_carrier.t4(mass) for mass in FLIP_MASSES
    )
    m3_mass = FLIP_MASSES[FLIP_M3_INDEX]
    base_m3 = base_carrier.t4_table(m3_mass)
    flip_m3 = flip_carrier.t4_table(m3_mass)
    flip_census_edges_at_m3 = sum(
        1 for key in base_m3 if base_m3[key] != flip_m3[key]
    )
    flip_spot = flip_carrier.t5_table(FIXTURE_MASS, SPOT_PENCILS)
    flip_spot_pencils = (
        sum(1 for key in SPOT_PENCILS if base_spot[key] != flip_spot[key]),
        len(SPOT_PENCILS),
    )
    if deep:
        base_full = base_carrier.t5_table(FIXTURE_MASS)
        flip_full = flip_carrier.t5_table(FIXTURE_MASS)
        flip_deep_pencils = (
            sum(1 for key in base_full if base_full[key] != flip_full[key]),
            len(base_full),
        )
    else:
        flip_deep_pencils = (0, 0)
    flip_orbit_inequivalent = b148.point_key(flip_point) not in orbit_keys(
        base_point
    )
    fixture_census = base_carrier.t4(FIXTURE_MASS)
    census_palindromic = fixture_census == tuple(
        sorted(
            (third, middle, first)
            for (first, middle, third) in fixture_census
        )
    )

    # --- G: the extension candidates ----------------------------------------
    twist_laws = []
    twist_trivial = []
    for alpha, beta in SIGN_TWISTS:
        matrix = sign_twist(alpha, beta)
        descent = b142.descend(matrix)
        law = zero(
            sp.expand(
                matrix * COVER_FREE * matrix.T
                - COVER_FREE.xreplace(
                    {
                        B_MODULUS[cell]: (-1) ** (alpha + beta) * B_MODULUS[cell]
                        for cell in CELLS
                    }
                )
            )
        )
        twist_laws.append(
            (
                (alpha, beta),
                descent is not None,
                bool(law),
                bool(
                    descent is not None
                    and zero(sp.expand(descent * descent.T - sp.eye(PHYS)))
                ),
            )
        )
        twist_trivial.append(
            (
                (alpha, beta),
                (alpha + beta) % 2 == 0,
                zero(sp.expand(matrix * COVER_FREE * matrix.T - COVER_FREE)),
            )
        )
    twist_laws = tuple(twist_laws)
    twist_trivial = tuple(twist_trivial)

    twist_commutation = all(
        b148.point_key(flip_shear(b148.push_point(base_point, label)))
        == b148.point_key(b148.push_point(flip_shear(base_point), label))
        for label in MOVES
    )
    # The flip commutes with all 64 moves AND is realised by none of them on the
    # committed base carrier, so the generated group is the DIRECT PRODUCT and
    # its order is 2 x 64; if either witness failed the order would not be 128
    # and this measurement reports that instead of asserting it.
    twist_extension_order = (
        2 * GROUP_ORDER
        if (twist_commutation and flip_orbit_inequivalent)
        else GROUP_ORDER
    )
    twist_carrier_images = len(
        {
            b148.point_key(candidate)
            for label in MOVES
            for candidate in (
                b148.push_point(base_point, label),
                flip_shear(b148.push_point(base_point, label)),
            )
        }
    )
    twists_preserve_t1_t4 = bool(
        flip_invisible_t1_t3
        and flip_census_visibility[FLIP_MASSES.index(FIXTURE_MASS)]
    )
    twists_break_t5 = flip_spot_pencils[0] > 0
    no_continuous_gauge = all(
        rank == JACOBIAN_GENERIC_RANK for _name, rank in jacobian_generic
    )

    exact_no_float = no_float(
        (
            COVER_FREE,
            HQ_FREE,
            HODGE_SPAN,
            tuple(EDGE_TABLES["healed"].values()),
            tuple(symbolic_quotient.values()),
            base_carrier.hodge,
            flip_carrier.hodge,
            tuple(DESCENT[label] for label in MOVES),
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        inertia_calibration=inertia_calibration,
        hermitian_conventions_agree=hermitian_conventions_agree,
        action_law_pinned=action_law_pinned,
        hodge_law_generators=hodge_law_generators,
        hodge_law_spot=hodge_law_spot,
        hodge_law_deep=hodge_law_deep,
        transport_generators=transport_generators,
        transport_spot=transport_spot,
        transport_deep=transport_deep,
        volume_inversion=volume_inversion,
        translation_relabel=translation_relabel,
        physical_generic=physical_generic,
        physical_unit=physical_unit,
        translation_image_order=translation_image_order,
        translation_kernel=translation_kernel,
        translation_order_multiset=translation_order_multiset,
        full_image_order=full_image_order,
        hodge_span_faithful=hodge_span_faithful,
        hodge_is_linear=hodge_is_linear,
        moduli_to_hodge_rank=moduli_to_hodge_rank,
        jacobian_generic=jacobian_generic,
        jacobian_nu1=jacobian_nu1,
        jacobian_flat_kernel=jacobian_flat_kernel,
        census_in_cone=census_in_cone,
        census_multiset_sharers=census_multiset_sharers,
        census_orbit_inequivalent=census_orbit_inequivalent,
        census_profile_separation=census_profile_separation,
        census_tier_alone=census_tier_alone,
        chi_homomorphism=chi_homomorphism,
        chi_kernel_order=chi_kernel_order,
        chi_contains_reflections=chi_contains_reflections,
        stabilizer_t1=len(t1_set),
        stabilizer_t2=len(t2_set),
        stabilizer_t1_half_spectrum=len(t1_half_set),
        stabilizer_t2_gram_spectra=len(t2_gram_set),
        half_preservers=len(half_preserving),
        t1_half_spectrum_is_half_preservers=(t1_half_set == half_preserving),
        stabilizer_t3=len(t3_set),
        seam_is_ker_chi=(t3_set == KER_CHI),
        stabilizer_t4_masses=tuple(len(value) for value in t4_sets),
        census_breakers_are_even_x=(
            frozenset(MOVES) - t4_sets[fixture_index] == EVEN_X_REFLECTIONS
        ),
        census_dressing=census_dressing,
        stabilizer_t5=len(t5_set),
        threshold_stabilizer_set=tuple(sorted(t5_set)),
        bare_moves=len(bare_set),
        bare_translations=sum(1 for label in bare_set if label[0] == 1),
        bare_half_preserving=len(bare_set & half_preserving),
        theta_is_bare=(THETA_LABEL in bare_set),
        theta_prime_is_bare=(THETA_PRIME in bare_set),
        unmatched_moves=unmatched_moves,
        bare_cross_validated=bare_cross_validated,
        threshold_is_bare_half_preserving_translations=(
            t5_set
            == frozenset(
                label
                for label in bare_set & half_preserving
                if label[0] == 1
            )
        ),
        carrier_specific_seam=carrier_specific_seam,
        shear_shift_cells=shear_shift_cells,
        shift_preserves_t1_t4=shift_preserves_t1_t4,
        shift_preserves_spot_pencils=shift_preserves_spot_pencils,
        shift_preserves_full_profile=shift_preserves_full_profile,
        twist_descends=twist_descends,
        twist_orthogonal=twist_orthogonal,
        twist_commutes_with_theta=twist_commutes_with_theta,
        twist_preserves_half=twist_preserves_half,
        twist_realises_flip=twist_realises_flip,
        flip_invisible_t1_t3=flip_invisible_t1_t3,
        flip_census_visibility=flip_census_visibility,
        flip_census_edges_at_m3=flip_census_edges_at_m3,
        flip_spot_pencils=flip_spot_pencils,
        flip_deep_pencils=flip_deep_pencils,
        flip_orbit_inequivalent=flip_orbit_inequivalent,
        census_palindromic=census_palindromic,
        twist_laws=twist_laws,
        twist_trivial=twist_trivial,
        twist_commutation=twist_commutation,
        twist_extension_order=twist_extension_order,
        twist_carrier_images=twist_carrier_images,
        twists_preserve_t1_t4=twists_preserve_t1_t4,
        twists_break_t5=twists_break_t5,
        no_continuous_gauge=no_continuous_gauge,
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE TRANSPORT IDENTITY, the structural core: with the WHOLE FRAME transported -- pairing operator X -> D X D^T, half PLUS -> D PLUS, connection d -> g d g^T, D = descend(g) -- the half pairing is not merely congruent but IDENTICALLY THE SAME MATRIX, PLUS^T X Q[d; y] PLUS = (D PLUS)^T (D X D^T) Q[g d g^T; g*y] (D PLUS), an EXACT MATRIX EQUALITY descending from the covariant Hodge law H_q(g*y) = D H_q(y) D^T with every descent D certified an ORTHOGONAL SIGNED PERMUTATION, symbolic in ALL 64 MODULI, in the MASS and in BOTH FIXTURE SHEARS, for all 64 covariant moves and BOTH displayed conventions (theta and X_0), independently reproduced at 1024/1024 FOR EACH; orthogonality is load-bearing, since D^{-1} = D^T makes the congruence simultaneously a SIMILARITY so that spectra as well as inertias survive; hence EVERY invariant built from the transported frame -- spectrum, inertia, rank, charpoly, pencil, census -- is ORBIT-CONSTANT, and THE 64-GROUP IS BOOKKEEPING AS A CHANGE OF FRAME, AND ONLY AS THAT, the final clause being the restriction that keeps the fixed-frame measurement meaningful\nper_site: THE INVARIANT PROFILE, five tiers with EXACT definitions: T1 = spec(H_q) together with the INERTIAS of H_q and H_q[+,+] -- NOT the half-block SPECTRA, since including those shrinks the T1 stabilizer from 64 to the SIXTEEN HALF-PRESERVERS; T2 = the INERTIAS of the two mass Grams -- NOT their spectra, since including those shrinks the T2 stabilizer from 64 to FOUR; T3 = the SEAM RANK; T4 = the HEALED-EDGE PAIRING INERTIA CENSUS in both conventions; T5 = the MASS-COMPLETION PENCILS, the characteristic polynomials of H_q[+,+]^{-1} P, carried as CHARPOLYS rather than root lists so comparison is exact and root-free; the two exclusions are the CHECKER\'S CORRECTIONS and are folded into the definitions rather than answered beside them, since the counts 64 and 64 are counts for the tiers AS DEFINED and for no other reading; and two structural riders: the BLOCK 141 HEALING LAYER IS LITERALLY CARRIER-FREE, no carrier modulus appearing in it at all, so it can separate nothing, while the CARRIER-SENSITIVE content is the ACTION LAYER, exhibited by two displayed cone carriers with different T5 pencils -- which is why T4 and T5 are the tiers that consume the connection and why the classification is finally decided at the threshold tier\nper_mode: THE PHYSICAL GAUGE GROUP AND THE MODULI SPACE: reflections INVERT THE VOLUME (nu <-> 1/nu) with the SHEAR MOMENTS FIXED, so their image is physical only where nu = 1/nu -- 0/32 at a generic cone carrier, 32/32 at nu = 1 -- while translations stay physical 32/32, so THE PHYSICAL GAUGE GROUP IS THE TRANSLATIONS, Z_4 x Z_4 OF ORDER 16, distinct from the 64-move covariance group of the envelope; the moduli-to-Hodge map has RANK 32, a 32-DIMENSIONAL KERNEL of the Block 145 linear envelope being annihilated by every invariant; the PHYSICAL JACOBIAN has FULL RANK 32 at GENERIC cone carriers but RANK 30 OF 32 ON THE nu = 1 SLICE, with kernel exactly the TWO STAGGERED VOLUME DIRECTIONS, and RANK 31 at the Block 145 witness, so LOCAL SEPARATION BY H_q ALONE IS GENERIC AND NOT UNIVERSAL -- the checker\'s qualifier, folded rather than appended -- and NO CONTINUOUS GAUGE DIRECTION WAS FOUND, since finite staggered deformations change H_q and a vanishing differential on a slice is not an exhibited flat direction; separation is complete, 28/28 pairs of EIGHT cone carriers (three built to share the (sigma, nu) MULTISET) being ORBIT-INEQUIVALENT and PROFILE-SEPARATED, with T5 ALONE separating 28/28, T4 alone 13/28 and T3 alone 7/28, and the physical moduli space having DIMENSION 32 with GENERIC FIBRE 16\nper_block: THE STABILIZER SPLIT, measured ON THE COMMITTED BASE CARRIER AT THE FIXTURE MASS, out of 64: T1 = 64 and T2 = 64 under the corrected tier definitions; T3 = 32, EXACTLY ker chi for a homomorphism chi onto Z_2 whose kernel contains BOTH theta AND theta\' -- but CARRIER-SPECIFIC, since a carrier with ALL SIXTEEN SHEARS NONZERO has T3 = 64 and the base carrier\'s 32 comes from its SINGLE ZERO EVEN-SLICE SHEAR; T4 = 56, breaking on EXACTLY the EIGHT PARITY-PRESERVING EVEN-x-CENTRED REFLECTIONS ON THIS CARRIER with the BREAKER SET VARYING ACROSS CARRIERS, and doubly diagnosed -- a b141 DRESSING ARTIFACT, since healed 56, control 56 but UNDRESSED 64/64, and MASS-ACTIVATED at 64, 56, 48, 16 for m = 0, 2/7, 1, 3, so that the tier is FULLY ORBIT-CONSTANT AT m = 0 and it is THE MASS TERM that breaks it, against the naive expectation; and T5 = 4, THE ATLAS OBSTRUCTION, diagnosed exactly as an INTERSECTION -- sixteen moves PRESERVE the half {p = 0,1}, eight are STRICTLY BARE in the committed atlas, and their intersection is EXACTLY FOUR TRANSLATIONS -- so the threshold tier breaks because the transported chart differentials LEAVE THE BARE ATLAS, not because the carrier changed; and the disclosure that ONLY T5 = 4 IS CARRIER-INVARIANT across the census, T1 through T4 being measurements at one carrier and one mass rather than facts about the group\nlattice_wide: THE SHARP CLASSIFICATION, and the extension that fails: the TRANSLATION (1,0,1,2) changes the SHEAR MOMENT AT ALL SIXTEEN CELLS -- and the VOLUME at all sixteen -- while PRESERVING THE ENTIRE FIXED-FRAME PROFILE, T1 through T5, INCLUDING ALL 32 PENCILS, AT EVERY TESTED MASS, so THE PER-CELL SHEAR VALUE IS BOOKKEEPING and no invariant in the list records sigma at a named cell; against that, the GLOBAL SIGN FLIP sigma -> -sigma is the (0,1) SIGN TWIST, an EXACT DESCENDED ORTHOGONAL CONGRUENCE that COMMUTES WITH THETA, PRESERVES THE HALF, REALIZES the flip on PHYSICAL carriers and is ORBIT-INEQUIVALENT (a different sigma multiset), and it is INVISIBLE to T1-T3 AT EVERY MASS and to T4 at m = 0, 2/7, 1 -- because the theta census MULTISET IS PALINDROMIC under (p,z,n) -> (n,z,p), so a global sign acts on it as the identity -- BUT IS DETECTED BY 30 OF THE 32 T5 PENCILS, and AT m = 3 EVEN T4 DETECTS IT, so "invisible to T1-T4" is FALSE UNQUALIFIED and is stated with its mass restriction; hence THE THEOREM: THE SHEAR FIELD IS RECORDED EXACTLY UP TO Z_4 x Z_4 LATTICE TRANSLATION AND NO FURTHER, an EQUALITY of groups -- nothing finer is recorded, by the translation witness, and nothing coarser, by the sign-flip detection; and the candidate enlargement is tested rather than dismissed: the b142 SIGN TWISTS all DESCEND and act on the family by b -> (-1)^(alpha + beta) b, EXTENDING THE GROUP TO ORDER 128, but they PRESERVE T1-T4 ONLY and BREAK T5, so they are NOT ADDITIONAL GAUGE MOVES -- with two footnotes that narrow the candidates further, that the (1,1) TWIST ACTS TRIVIALLY ON CARRIERS so only TWO genuine candidates remain and they INDUCE THE SAME CARRIER MAP, and that ONLY (0,1) COMMUTES WITH THETA\nRESULT: on the displayed Block 105 atlas at the committed fixtures s_x = 3/5, s_t = 4/5 with SYMBOLIC mass m, executing Block 148\'s named shear\'s-gauge-classification item -- THE OWNER\'S STANDING QUESTION IN ITS PRECISE FORM, is the carrier shear RECORDED or NOT RECORDED, PHYSICS or BOOKKEEPING -- and DECIDING IT SHARPLY, the transport identity PLUS^T X Q[d;y] PLUS = (D PLUS)^T (D X D^T) Q[g d g^T; g*y] (D PLUS) is an EXACT MATRIX EQUALITY for all 64 covariant moves and BOTH conventions at 1024/1024 EACH, symbolic in all 64 moduli, in m and in both shears, so the 64-group is BOOKKEEPING AS A CHANGE OF FRAME AND ONLY AS THAT; against the canonical FIXED frame the five-tier profile (T1 spec H_q plus the INERTIAS of H_q and H_q[+,+]; T2 the INERTIAS of the two mass Grams; T3 the seam rank; T4 the healed-edge inertia census, both conventions; T5 the mass-completion pencils) has measured stabilizers 64, 64, 32, 56, 4 OUT OF 64 at the committed base carrier and the fixture mass, T3 being EXACTLY ker chi yet CARRIER-SPECIFIC (all sixteen shears nonzero gives 64), T4 breaking on the eight parity-preserving even-x-centred reflections ON THIS CARRIER as a DRESSING ARTIFACT (undressed 64/64) that is MASS-ACTIVATED (64/56/48/16 at m = 0, 2/7, 1, 3), and ONLY T5 = 4 CARRIER-INVARIANT, diagnosed as an ATLAS OBSTRUCTION (sixteen half-preserving, eight strictly bare, intersection exactly four translations); the PHYSICAL GAUGE GROUP is the TRANSLATIONS Z_4 x Z_4 OF ORDER 16, reflections leaving the physical locus except at nu = 1 (0/32 generic, 32/32 at nu = 1), the moduli-to-Hodge map having RANK 32 and the physical Jacobian FULL RANK 32 at generic cone carriers but RANK 30 ON THE nu = 1 SLICE (kernel the two staggered volume directions; 31 at the b145 witness), so local separation by H_q alone is GENERIC AND NOT UNIVERSAL and NO CONTINUOUS GAUGE DIRECTION WAS FOUND, with 28/28 separation of eight cone carriers (T5 alone 28/28, T4 13/28, T3 7/28) and a moduli space of DIMENSION 32 with GENERIC FIBRE 16; and THE CLASSIFICATION is that the translation (1,0,1,2) moves the shear at ALL SIXTEEN CELLS with the ENTIRE PROFILE INCLUDING ALL 32 PENCILS FIXED AT EVERY TESTED MASS -- THE PER-CELL SHEAR VALUE IS BOOKKEEPING -- while the GLOBAL SIGN FLIP, an exact descended orthogonal congruence commuting with theta and preserving the half, orbit-inequivalent, invisible to T1-T3 at every mass and to T4 at m = 0, 2/7, 1 by PALINDROMY, is DETECTED BY 30 OF THE 32 T5 PENCILS and by T4 itself at m = 3, so THE SHEAR FIELD IS RECORDED EXACTLY UP TO Z_4 x Z_4 LATTICE TRANSLATION AND NO FURTHER, the b142 sign twists extending the group to order 128 but breaking T5 and therefore NOT being additional gauge moves ((1,1) acts trivially on carriers, leaving two candidates inducing the same map; only (0,1) commutes with theta); all inertias by EXACT SYMMETRIC CONGRUENCE with the distinct-real-root helper never called\nDECISION_CUT: decide THE BARE-ATLAS QUESTION -- whether the odd-centred reflection should displace theta as the canonical OS operator -- inherited undecided from Block 148 and now sharpened, since this block diagnoses T5 = 4 as an ATLAS obstruction and identifies the eight strictly bare moves whose intersection with the sixteen half-preservers is the threshold stabilizer; BUILD A CHART-SYMMETRIC DRESSING FOR THE THRESHOLD TIER, the new item this block opens, since the T4 breaking is already known to be a dressing artifact and the T5 obstruction is an atlas one, so a dressing symmetric across charts is the exact object to test; build NON-LATTICE PAIRING CONVENTIONS; register BOUNDARY AND DEFECT COMPLETIONS as premises and execute them rather than importing them; execute the JOINT-LANE PROGRAM; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "transport_identity",
    "tier_definitions",
    "gauge_group",
    "jacobian_qualifier",
    "separation",
    "split_kernel",
    "split_dressing",
    "split_mass",
    "split_carrier",
    "classification_bookkeeping",
    "classification_sign_flip",
    "classification_detected",
    "classification_scope",
    "classification_m3",
    "extensions_not_gauge",
    "extensions_trivial",
    "provenance",
    "independence_disclosure",
    "os_no_go",
    "curved_os_no_go",
    "axiom",
    "firewalls",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "n1_n8",
    "w1",
    "n5_verbatim",
)


def scope_certificate(note_text: str) -> dict[str, bool]:
    note = normalized_note(note_text)
    compact = compact_note(note_text)
    return {
        "transport_identity": "exact matrix equality" in note
        or "transport identity" in note,
        "tier_definitions": (
            "inertias" in note and "half-block spectra" in note
        )
        or "tier definitions" in note,
        "gauge_group": ("z_4 x z_4" in note or "translations" in note)
        and "order 16" in note,
        "jacobian_qualifier": ("rank 30" in note or "nu = 1 slice" in note)
        and "generic" in note,
        "separation": "28/28" in note,
        "split_kernel": "ker chi" in note or "homomorphism" in note,
        "split_dressing": "dressing artifact" in note,
        "split_mass": "mass-activated" in note or "mass-dependent" in note,
        "split_carrier": "carrier-specific" in note
        or "carrier-invariant" in note,
        "classification_bookkeeping": "bookkeeping" in note,
        "classification_sign_flip": "sign flip" in note,
        "classification_detected": "detected" in note,
        "classification_scope": "recorded exactly up to" in note
        or "lattice translation and no further" in note,
        # Whitespace-insensitive so the note may space the mass either way.
        "classification_m3": "m = 3" in note or "m=3" in compact,
        "extensions_not_gauge": "not additional gauge moves" in note
        or ("break" in note and "t5" in note),
        "extensions_trivial": "trivially" in note,
        "provenance": "owner's" in note or "recorded or not recorded" in note,
        "independence_disclosure": "cross-context" in note,
        "os_no_go": "not an os no-go" in note,
        "curved_os_no_go": "not a curved os no-go" in note,
        "axiom": "no axiom amendment is justified" in note,
        "firewalls": "firewall" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": (
            "no toe percentage moves" in note
            or "no toe percentage movement" in note
        ),
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "n1_n8": all(
            re.search(rf"\bn{index}\b", note) is not None
            for index in range(1, 9)
        ),
        "w1": re.search(r"\bw1\b", note) is not None,
        # Raw substring membership makes the printed eight-line fence
        # byte-identical to its note occurrence.
        "n5_verbatim": N5_FENCE in note_text,
    }


# ---------------------------------------------------------------------------
# claims: the only thing a mutation is allowed to touch
# ---------------------------------------------------------------------------
def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main_head": CURRENT_MAIN,
        "parent_pin": "resolved",
        "hodge_law_generators": HODGE_LAW_GENERATORS,
        "transport_generators": TRANSPORT_GENERATOR_HITS,
        "reflections_physical_generic": 0,
        "jacobian_nu1_rank": JACOBIAN_NU1_RANK,
        "separation": CENSUS_PAIRS,
        "seam_stabilizer": STABILIZER_T3,
        "census_stabilizer_fixture": STABILIZER_T4,
        "threshold_stabilizer_set": THRESHOLD_STABILIZER,
        "shift_preserves_profile": True,
        "flip_detected_by_t5": True,
        "flip_census_visibility": FLIP_CENSUS_VISIBILITY,
        "twists_break_threshold": True,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "break_hodge_law":
        claims["hodge_law_generators"] = HODGE_LAW_GENERATORS - 1
    elif mutation == "break_transport_identity":
        claims["transport_generators"] = TRANSPORT_GENERATOR_HITS - 1
    elif mutation == "claim_reflections_physical":
        claims["reflections_physical_generic"] = REFLECTION_COUNT
    elif mutation == "drop_jacobian_qualifier":
        claims["jacobian_nu1_rank"] = JACOBIAN_GENERIC_RANK
    elif mutation == "wrong_separation_count":
        claims["separation"] = CENSUS_PAIRS - 1
    elif mutation == "wrong_seam_stabilizer":
        claims["seam_stabilizer"] = GROUP_ORDER
    elif mutation == "claim_census_carrier_invariant":
        claims["census_stabilizer_fixture"] = GROUP_ORDER
    elif mutation == "wrong_threshold_stabilizer":
        claims["threshold_stabilizer_set"] = WRONG_THRESHOLD_STABILIZER
    elif mutation == "claim_translation_changes_profile":
        claims["shift_preserves_profile"] = False
    elif mutation == "claim_sign_flip_invisible":
        claims["flip_detected_by_t5"] = False
    elif mutation == "drop_m3_qualification":
        claims["flip_census_visibility"] = (True,) * len(FLIP_MASSES)
    elif mutation == "claim_twists_are_gauge":
        claims["twists_break_threshold"] = False
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
FLIP_M3_EDGES = 2


def evaluate_gates(
    facts: Facts, claims: dict[str, object], elapsed_ns: int
) -> dict[str, bool]:
    authority = facts.authority
    parent_blobs_ok = (
        authority.parent_artifact_blobs
        if claims["parent_pin"] == "resolved"
        else authority.stale_parent_artifact_blobs
    )
    gate_a = bool(
        AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SHEAR_GAUGE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_GENERAL_MIGRATION_THEOREM_BOUNDED_THEOREM_NOTE_2026-08-20.md",
            "scripts/admissibility_dirac_kahler_general_migration_theorem_2026_08_20.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
        )
        and PARENT_ARTIFACTS
        == (BLOCK148_NOTE, BLOCK148_RUNNER, BLOCK145_NOTE, BLOCK145_RUNNER)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.inertia_calibration
        and facts.hermitian_conventions_agree
        and facts.action_law_pinned
        and facts.hodge_law_generators
        == (claims["hodge_law_generators"], HODGE_LAW_GENERATORS)
        and facts.hodge_law_spot == (HODGE_LAW_SPOT, HODGE_LAW_SPOT)
        and facts.hodge_law_deep
        in ((0, 0), (HODGE_LAW_DEEP, HODGE_LAW_DEEP))
        and facts.transport_generators
        == (
            claims["transport_generators"],
            TRANSPORT_GENERATOR_HITS,
            TRANSPORT_GENERATOR_HITS,
        )
        and facts.transport_spot
        == (TRANSPORT_SPOT_HITS, TRANSPORT_SPOT_HITS, TRANSPORT_SPOT_HITS)
        and facts.transport_deep
        in ((0, 0, 0), (TRANSPORT_DEEP_HITS,) * 3)
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.volume_inversion == (REFLECTION_COUNT, REFLECTION_COUNT)
        and facts.translation_relabel == (TRANSLATION_COUNT, TRANSLATION_COUNT)
        and facts.physical_generic
        == (
            claims["reflections_physical_generic"],
            TRANSLATION_COUNT,
            REFLECTION_COUNT,
        )
        and facts.physical_unit
        == (REFLECTION_COUNT, TRANSLATION_COUNT, REFLECTION_COUNT)
        and facts.translation_image_order == TRANSLATION_IMAGE_ORDER
        and facts.translation_kernel == TRANSLATION_KERNEL
        and facts.translation_order_multiset == Z4XZ4_ORDER_MULTISET
        and facts.full_image_order == CARRIER_IMAGE_ORDER
        and facts.hodge_is_linear
        and facts.hodge_span_faithful
        and facts.moduli_to_hodge_rank == MODULI_TO_HODGE_RANK
        and all(
            rank == JACOBIAN_GENERIC_RANK for _name, rank in facts.jacobian_generic
        )
        and len(facts.jacobian_generic) == len(GENERIC_CARRIERS)
        and all(
            rank == claims["jacobian_nu1_rank"]
            for _name, rank in facts.jacobian_nu1
        )
        and len(facts.jacobian_nu1) == len(NU1_CARRIERS)
        and facts.jacobian_flat_kernel
        == (
            JACOBIAN_NU1_KERNEL_DIM,
            True,
            True,
            JACOBIAN_NU1_KERNEL_DIM,
            (HALF, HALF),
            True,
            ((0,), (1,)),
        )
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.census_in_cone
        and facts.census_multiset_sharers == tuple(sorted(MULTISET_SHARERS))
        and facts.census_orbit_inequivalent == (claims["separation"], CENSUS_PAIRS)
        and facts.census_profile_separation
        == (claims["separation"], CENSUS_PAIRS)
        and facts.census_tier_alone
        == tuple(
            (tier, TIER_ALONE_COUNTS[tier])
            for tier in ("T1", "T2", "T3", "T4", "T5")
        )
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.chi_homomorphism
        and facts.chi_kernel_order == STABILIZER_T3
        and facts.chi_contains_reflections
        and facts.stabilizer_t1 == STABILIZER_T1
        and facts.stabilizer_t2 == STABILIZER_T2
        and facts.stabilizer_t1_half_spectrum
        == STABILIZER_T1_WITH_HALF_SPECTRUM
        and facts.stabilizer_t2_gram_spectra == STABILIZER_T2_WITH_GRAM_SPECTRA
        and facts.half_preservers == HALF_PRESERVER_COUNT
        and facts.t1_half_spectrum_is_half_preservers
        and facts.stabilizer_t3 == claims["seam_stabilizer"]
        and facts.seam_is_ker_chi
        and facts.stabilizer_t4_masses
        == (
            CENSUS_MASS_STABILIZERS[0],
            claims["census_stabilizer_fixture"],
            CENSUS_MASS_STABILIZERS[2],
        )
        and facts.census_breakers_are_even_x
        and facts.census_dressing == CENSUS_DRESSING_STABILIZERS
        and facts.stabilizer_t5 == STABILIZER_T5
        and facts.threshold_stabilizer_set
        == tuple(sorted(claims["threshold_stabilizer_set"]))
        and facts.threshold_is_bare_half_preserving_translations
        and facts.bare_moves == BARE_MOVES
        and facts.bare_translations == BARE_TRANSLATIONS
        and facts.bare_half_preserving == BARE_HALF_PRESERVING
        and not facts.theta_is_bare
        and facts.theta_prime_is_bare
        and facts.unmatched_moves == 0
        and facts.bare_cross_validated
        and facts.carrier_specific_seam
        == (CARRIER_SPECIFIC_SEAM[0], CARRIER_SPECIFIC_SEAM[1], True)
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.shear_shift_cells == SHEAR_SHIFT_CELLS
        and (
            facts.shift_preserves_t1_t4
            and facts.shift_preserves_spot_pencils
        )
        == bool(claims["shift_preserves_profile"])
        and facts.shift_preserves_full_profile
        in ((0, 0), (TOTAL_PENCILS, TOTAL_PENCILS))
        and facts.twist_descends
        and facts.twist_orthogonal
        and facts.twist_commutes_with_theta
        and facts.twist_preserves_half
        and facts.twist_realises_flip
        and facts.flip_invisible_t1_t3
        and facts.flip_orbit_inequivalent
        and facts.census_palindromic
        and facts.flip_census_visibility
        == tuple(claims["flip_census_visibility"])
        and facts.flip_census_edges_at_m3 == FLIP_M3_EDGES
        and facts.flip_spot_pencils[1] == len(SPOT_PENCILS)
        and (facts.flip_spot_pencils[0] >= SPOT_PENCIL_MINIMUM)
        == bool(claims["flip_detected_by_t5"])
        and facts.flip_deep_pencils
        in ((0, 0), (DEEP_FLIP_PENCILS, TOTAL_PENCILS))
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.twist_laws
        == tuple(
            (twist, True, True, True) for twist in SIGN_TWISTS
        )
        and facts.twist_trivial
        == tuple(
            (twist, (twist[0] + twist[1]) % 2 == 0, (twist[0] + twist[1]) % 2 == 0)
            for twist in SIGN_TWISTS
        )
        and facts.twist_commutation
        and facts.twist_extension_order == TWIST_EXTENSION_ORDER
        and facts.twist_carrier_images == TWIST_CARRIER_IMAGES
        and facts.twists_preserve_t1_t4
        and facts.twists_break_t5 == bool(claims["twists_break_threshold"])
        and facts.no_continuous_gauge
        and facts.exact_no_float
    )

    required = tuple(claims["required_scope_keys"])
    gate_h = bool(
        set(facts.scope) == set(required)
        and all(facts.scope.values())
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") == 7
        and elapsed_ns <= RUNTIME_BUDGET_SEC * 1_000_000_000
    )

    return {
        "A": gate_a,
        "B": gate_b,
        "C": gate_c,
        "D": gate_d,
        "E": gate_e,
        "F": gate_f,
        "G": gate_g,
        "H": gate_h,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument(
        "--deep",
        action="store_true",
        help=(
            "also run the full 64-move x 16-edge x 2-convention transport "
            "sweep and the full 32-pencil threshold comparisons"
        ),
    )
    arguments = parser.parse_args()
    mutation = arguments.mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
    facts = measure(arguments.deep)
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if mutation:
        target = MUTATION_GATE[mutation]
        gate_values = evaluate_gates(
            facts, build_claims(mutation), elapsed_ns
        )
        changed = {
            key for key in raw_gates if raw_gates[key] != gate_values[key]
        }
        if changed - {target} or gate_values[target]:
            raise AssertionError(
                "mutation did not fail exactly its own gate"
            )

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the committed Block 148 note/runner and Block 145 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-transport-identity",
        "with the whole frame transported the half pairing is not merely congruent but the SAME MATRIX: PLUS^T X Q[d;y] PLUS = (D PLUS)^T (D X D^T) Q[g d g^T; g*y] (D PLUS) holds 64/64 for EACH of the two displayed conventions (theta and X_0) on the four generators against all sixteen healed edges, and 64/64 for each on a sixteen-move by four-edge spot, symbolically in all 64 moduli, in m and in (s_x, s_t); the descended Hodge law H_q(g*y) = D H_q(y) D^T holds 4/4 on the generators and 16/16 on the spot; the inlined action law is pinned against the committed Block 145 routine and the Hermitian-part convention against the committed Block 148 helper; the full 64 x 16 x 2 sweep is available behind --deep",
        gate_values["B"],
    )
    checks.check(
        "C-physical-gauge-group",
        "all 32 reflections invert the volume modulus while fixing a and b, so 0/32 keep a generic cone carrier physical while 32/32 do at nu = 1 (all 32 translations keep it physical in both cases); the translations act on carriers through ORDER 16 with kernel {identity, four-step time shift} and element-order multiset {1:1, 2:3, 4:12}, which is Z_4 x Z_4, the full 64 acting through 32; the moduli-to-Hodge map has RANK 32 of 64; AND THE JACOBIAN QUALIFIER IS CARRIED: d H_q/d(sigma,nu) has FULL RANK 32 at three generic cone carriers but RANK 30 on four carriers of the nu = 1 slice, where at the flat carrier the two-dimensional kernel is spanned by two explicit STAGGERED VOLUME directions with entries +-1, one per cell-parity class",
        gate_values["C"],
    )
    checks.check(
        "D-separation",
        "an eight-carrier cone census, THREE members of which share the (sigma,nu) multiset exactly, is 28/28 orbit-inequivalent under the 64 moves and 28/28 separated by the five-tier profile; the threshold tier ALONE separates 28/28, while T1 alone gives 27/28, T4 alone 13/28 and T2 and T3 alone 7/28 each -- the partial counts are measured and printed, not suppressed",
        gate_values["D"],
    )
    checks.check(
        "E-stabilizer-split",
        "on the committed base carrier at the committed fixture mass the fixed-frame stabilisers are T1 = 64 and T2 = 64 UNDER THE CORRECTED TIER DEFINITIONS (inertias plus the spectrum of the FULL H_q), collapsing to 16 and 4 when the HALF-BLOCK spectra are added -- the 16 being exactly the half-preserving moves, so the definition discipline is a checked certificate and not a convenience; T3 = 32 = ker chi with chi verified a homomorphism onto Z_2 containing theta and theta', and CARRIER-SPECIFIC, since a different nonzero-shear cone carrier has T3 = 64; T4 = 56 broken by exactly the eight parity-preserving even-x-centred reflections, 56 under the alternative dressing and 64/64 UNDRESSED, and mass-activated at 64/56/16 for m = 0, 2/7, 3; and T5 = 4, exactly the four BARE HALF-PRESERVING TRANSLATIONS out of 32 bare moves and 16 half-preserving ones -- an ATLAS obstruction, with theta not bare, theta' bare, nothing unmatched and the hash lookup cross-validated symbolically",
        gate_values["E"],
    )
    checks.check(
        "F-sharp-classification",
        "the lattice translation (1,0,1,2) changes the shear at 16 of 16 cells and preserves the ENTIRE fixed-frame profile, so sigma at a NAMED cell is bookkeeping; the (0,1) sign twist is an exact descended ORTHOGONAL congruence that commutes with theta, preserves the half, realises sigma -> -sigma on the physical carrier and is ORBIT-INEQUIVALENT, is invisible to T1-T3 and to the T4 census at masses 0, 2/7 and 1 (the census multiset being palindromic), and is DETECTED by the threshold pencils on at least four of the eight spot slots; AND THE QUALIFICATION IS CARRIED: at m = 3 the census DOES see it, on two of the 32 edge-operator slots, so census invisibility is a fixture-mass statement; the full 32-pencil comparison (30/32 detecting) is behind --deep",
        gate_values["F"],
    )
    checks.check(
        "G-extension-candidates",
        "all three Block 142 sign twists descend to orthogonal involutions and act on the carrier family by b -> (-1)^(alpha+beta) b symbolically, so the (1,1) twist acts TRIVIALLY and is a footnote rather than a third generator; the flip commutes with all 64 moves and is realised by none of them, so the group extends to ORDER 128 acting on carriers through 64; the extension preserves T1-T4 and BREAKS T5, so it is not an additional gauge move; and at every generic cone carrier the physical Jacobian is injective, so there is no continuous gauge direction either",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the exact-matrix-equality transport identity, the tier-definition discipline with its half-block-spectra collapse, the Z_4 x Z_4 physical gauge group of order 16, the Jacobian qualifier with its rank-30 nu = 1 slice, the 28/28 separation, the split with its ker chi seam, its dressing artifact, its mass activation and its carrier specificity, the classification with its bookkeeping shear value, its sign flip, its detection, its up-to-lattice-translation scope and its m = 3 qualification, the extensions that are not gauge moves and the trivial one, the provenance, the cross-context disclosure, the firewalls and the exact N5 fence are present",
        gate_values["H"],
    )
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
