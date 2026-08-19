#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_massless_seam_verdict_2026_08_19.py
"""Block 144: the massless-seam verdict on the shear-free carrier.

Block 142's gate D built a control carrier with overlap profile (0, nu(t)) --
shear switched off, the non-constant time profile kept -- and reported that all
sixteen healed edge pairings [theta Q]_{++} are Hermitian there with the
CANONICAL LATTICE theta, even though theta is not a Hodge symmetry on that
carrier.  Block 143 then bought Hermiticity on the committed staircase carrier
with the staggered site parity and showed positivity still fails.  The obvious
remaining hope was that the shear-free carrier -- where Hermiticity is free --
would also be the one where positivity finally works.  It does not, and the
reason is sharper and more damaging than a numerical failure:

  * THE HODGE CARRIER GOES DIAGONAL, and with an exact law.  On (0, nu(t)) the
    quotient Hodge H_q is DIAGONAL, x-independent, and
    h(p) = (2 nu_p + nu_{p-1} + 1/nu_{p-1})/4 symbolically in a positive
    profile nu, taking the four values (256/255, 9/10, 1013/1040, 10001/10608)
    at the committed fixture nu = (1, 4/5, 12/13, 15/17).  It is positive
    definite by congruence.  Diagonality has an immediate and fatal
    consequence: the REFLECTION SEAM GRAM H_q[-,+] vanishes IDENTICALLY in nu,
    and so does the mass block [theta H_q]_{++};
  * THE MASS LEAVES THE PAIRING.  Because theta exchanges the halves, the
    half-pairing is P_ij = theta[+,-] Q_ij[-,+], and Q_ij[-,+] = beta(m I + R)
    with beta = H_q[-,+] = 0.  So every P_ij is m-FREE: this carrier's OS block
    is pure skew, with no mass Gram to be positive at all.  Where Block 143's
    staircase had det H_q[+,-] = 1/26542080 != 0, here the seam is massless;
  * POSITIVITY FAILS WITH AN EXACT CERTIFICATE.  Four of the sixteen edges --
    exactly the ZERO-DRESSING COVER-TIME-EVEN-LEFT ones -- have P == 0
    identically; the other twelve have rank 8 and congruence inertia census
    {(2,0,6) x6, (6,0,2) x6}.  The mechanism is entrywise: P[j,j] = 0
    identically for every odd j on every edge and every nu, so the (1,3)
    principal minor is exactly -|P[1,3]|^2 < 0, with
    P[1,3] = (lambda_ij + c_l)(nu_2^2 + 2 nu_2 nu_3 + 1)/(5 nu_2),
    lambda_ij = x_j - x_i the dressing weight difference and c_l = (0,0,-1,+1)
    a CHART OFFSET carried by the left chart alone.  The offset is what makes
    the two forced self-edges (2,2) and (3,3) indefinite at lambda = 0, where
    the naive weight-proportional reading would have predicted zero;
  * THE REFLECTION BLOCKER SURVIVES, BY A DIFFERENT MECHANISM.  0/256 signed
    lattice reflections preserve H_q here as well, but Block 142's fingerprint
    argument is gone -- the absolute-value fingerprint count collapses from 15
    to 4.  The replacement is a SLICE-FIXING certificate: h takes four distinct
    values, so any signed permutation preserving H_q must fix every time slice,
    while every lattice reflection acts on slices as p -> b - p, and no shift b
    has h(b - p) = h(p) for all p.  The flat profile nu = 1 makes H_q = I and
    256/256 reflections preserve it, which is exactly the contrast that shows
    the blocker is carried by the profile and not by the reflection family; and
  * THE OS VERDICT IS CURVATURE-BLIND.  The flat profile nu = (1,1,1,1)
    reproduces the IDENTICAL null locus and the IDENTICAL inertia census while
    the pairing entries themselves differ, so nothing in the verdict is reading
    the remaining curvature.  The Block 134 connection residual still has its
    closed form in the signed frame at rank 16 while the Block 141 healing
    generator Omega* has rank 12: the two are NOT identified, and no frame can
    identify them.  Completions do not rescue anything either: every swap-type
    Gram is identically zero here, so the swap completion is VACUOUS, and the
    mass completion is a hand-inserted repair with per-edge thresholds
    {0, 4/15, 2/5, 4/5, 16/15, 6/5, 22/15}, global threshold 22/15, PSD exactly
    at 22/15 and failing at 22/15 - 1/1000, and a PROFILE-DEPENDENT threshold
    (220/81 at nu = (1,2,3,5)).

Every scientific comparison below is exact SymPy arithmetic -- concrete at the
committed shear-free fixture nu = (1, 4/5, 12/13, 15/17) and symbolic in a
positive profile wherever the certificate is claimed to be profile-uniform.
No floats anywhere; the integer monotonic clock is used only for the runtime
gate.

TOOLING DISCLOSURE: every inertia in this runner is computed by SYMMETRIC
CONGRUENCE (Sylvester's law, with the 2x2 hyperbolic pivot for a zero
diagonal), not by root counting.  The Block 142/143 helper counts DISTINCT
real roots, which undercounts on the degenerate spectra this carrier produces;
it is unsound here and is deliberately not used.

HYPOTHESES, named and not imported: (H1) the OS pairing convention is
P_ij = [theta Q_ij]_{++} on the half carrier {p = 0,1} with theta the canonical
lattice reflection, exactly as Block 142's gate E used it.  (H2) the swap
completion is P^sw = (P_ij + P_ji)/2 and its Gram is any of the four natural
seam transports of H_q; both are tested, neither is assumed to be the flat
program's completion.  (H3) the mass completion P + m H_q[+,+] is a
data-dependent boundary term, tested and reported, not derived.  (H4) the
atlas, the healing weights and the connection fixture are the committed
Block 105/137/141 ones; only the Hodge carrier moves.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys
import time

import sympy as sp


R = sp.Rational
MASS = sp.symbols("m", real=True)
WEIGHT = sp.symbols("w", real=True)
LAM = sp.Symbol("lambda")

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

import admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19 as b143

b142 = b143.b142
b141 = b143.b141
b137 = b143.b137
b134 = b143.b134
b105 = b134.block105


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_MASSLESS_SEAM_VERDICT_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK143_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK143_RUNNER = (
    "scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_"
    "2026_08_19.py"
)
BLOCK143_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_staggered_hermitian_pairing_"
    "2026_08_19.txt"
)
BLOCK142_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK142_RUNNER = (
    "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_"
    "2026_08_19.py"
)
PARENT_ARTIFACTS = (
    BLOCK143_NOTE,
    BLOCK143_RUNNER,
    BLOCK143_CACHE,
    BLOCK142_NOTE,
    BLOCK142_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_MASSLESS_SEAM_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.py",
    "logs/runner-cache/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 143 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block143-staggered-hermitian-pairing-20260819"
)
# Landing supervisor: replace this placeholder with the Block 143 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF, which is
# a real and verifiable binding; the immutable commit pin lands with the block.
PARENT_COMMIT = "275f1bd78201b0d9f440099536d3f602106caf29"
# Block 141's tip: a real ancestor that predates the Block 142/143 artifacts and
# is therefore the honest "stale pin" control for the authority mutation.  It is
# read ONLY under the stale mutation; the baseline gate never requires the stale
# blobs to match the worktree.
STALE_PARENT_COMMIT = "2d92a7252bb85ed4090e0fc76032f674e51c6236"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "break_hodge_law",
    "claim_seam_gram_nonzero",
    "break_edge_nilpotency",
    "wrong_leftover_rank",
    "claim_pairing_mass_dependent",
    "wrong_null_count",
    "wrong_census",
    "wrong_formula_offset",
    "claim_positive_semidefinite_edge",
    "claim_preserver_exists",
    "break_flat_contrast",
    "wrong_mass_threshold",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "break_hodge_law": "B",
    "claim_seam_gram_nonzero": "B",
    "break_edge_nilpotency": "C",
    "wrong_leftover_rank": "C",
    "claim_pairing_mass_dependent": "D",
    "wrong_null_count": "D",
    "wrong_census": "E",
    "wrong_formula_offset": "E",
    "claim_positive_semidefinite_edge": "E",
    "claim_preserver_exists": "F",
    "break_flat_contrast": "F",
    "wrong_mass_threshold": "G",
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
    commit that predates some of the pinned artifacts.
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
    return all(sp.expand(value) == 0 for value in matrix)


def zero_simplified(matrix: sp.MatrixBase) -> bool:
    """Symbolic-profile twin of `zero`: needed because a symbolic nu leaves
    entries as unexpanded rational functions that only cancel under simplify."""
    return all(sp.simplify(value) == 0 for value in matrix)


def is_diagonal(matrix: sp.MatrixBase) -> bool:
    return zero_simplified(
        matrix - sp.diag(*[matrix[k, k] for k in range(matrix.rows)])
    )


def congruence_inertia(matrix: sp.MatrixBase) -> tuple[int, int, int]:
    """Exact (n_positive, n_zero, n_negative) WITH multiplicity, by congruence.

    Ported from the independent Block 144 checker.  Sylvester's law of inertia
    is applied directly: pivot on a nonzero diagonal entry and clear its row and
    column, and when the diagonal entry vanishes but an off-diagonal partner
    does not, split off the 2x2 block [[0, a], [conj(a), b]] whose determinant
    is -|a|^2 < 0 and which therefore contributes exactly (1, 0, 1).

    This replaces b142.inertia / b143.inertia, which count DISTINCT real roots
    via count_roots and so undercount on the degenerate spectra this carrier
    produces: on diag(1, 1, -2, -2, 0) the root count returns (1, 1, 1) where
    the true inertia is (2, 1, 2).  The calibration is asserted in gate B.
    """
    work = sp.Matrix(matrix).as_mutable()
    active = list(range(work.rows))
    positive = negative = null = 0
    while active:
        head = active[0]
        pivot = sp.simplify(work[head, head])
        if pivot != 0:
            if pivot.is_positive:
                positive += 1
            elif pivot.is_negative:
                negative += 1
            else:
                raise ValueError(f"non-real pivot {pivot}")
            rest = active[1:]
            for row in rest:
                factor = work[row, head] / pivot
                if factor == 0:
                    continue
                for column in rest:
                    work[row, column] = sp.expand(
                        work[row, column] - factor * work[head, column]
                    )
            active = rest
            continue
        partner = next(
            (k for k in active[1:] if sp.simplify(work[head, k]) != 0), None
        )
        if partner is None:
            null += 1
            active = active[1:]
            continue
        # the 2x2 block [[0, a], [conj(a), b]] has determinant -|a|^2 < 0
        positive += 1
        negative += 1
        block = sp.Matrix(
            [
                [work[head, head], work[head, partner]],
                [work[partner, head], work[partner, partner]],
            ]
        )
        block_inverse = block.inv()
        rest = [j for j in active if j not in (head, partner)]
        for row in rest:
            left = sp.Matrix([[work[row, head], work[row, partner]]])
            coefficients = sp.expand(left * block_inverse)
            for column in rest:
                work[row, column] = sp.expand(
                    work[row, column]
                    - coefficients[0, 0] * work[head, column]
                    - coefficients[0, 1] * work[partner, column]
                )
        active = rest
    return (positive, null, negative)


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
    return PARENT_COMMIT if is_hash(PARENT_COMMIT) else git_output(
        "rev-parse", PARENT_REF
    )


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
                or git_output("rev-parse", PARENT_REF) == PARENT_COMMIT
            )
        ),
        bool(
            len(committed_blobs) == 5
            and all(is_hash(value) for value in committed_blobs)
            and committed_blobs == worktree_blobs
        ),
        bool(
            len(stale_blobs) == 5
            and all(is_hash(value) for value in stale_blobs)
            and stale_blobs == worktree_blobs
        ),
    )


# ---------------------------------------------------------------------------
# carrier machinery, imported wholesale from the committed Blocks 143/142/141/137/134
# ---------------------------------------------------------------------------
SIZE = b134.SIZE                         # 32 cover sites
COVER_T = b134.COVER_TIME_EXTENT         # 8
PHYS_T = b134.PHYSICAL_TIME_EXTENT       # 4
LX = b134.SPACE_EXTENT                   # 4
PHYS = b142.PHYS                         # 16 quotient sites
HALF = b142.HALF                         # 8 sites in the positive-time half
ORIGINS = b142.ORIGINS                   # ((0,0),(0,1),(1,0),(1,1))
INDEX = b142.INDEX
DISPLAYED = b142.DISPLAYED               # ((1,0),(1,1))
PLUS = b142.PLUS
IDENTITY = b142.IDENTITY
HEALING_WEIGHTS = b141.HEALING_WEIGHTS   # x = (0, 0, 1/2, -1/3)
PLUS_SITES = list(range(HALF))           # the carrier half p = 0,1
MINUS_SITES = list(range(HALF, PHYS))    # p = 2,3
COVER_TIME_EVEN = tuple(
    origin for origin in ORIGINS if origin[0] % 2 == 0
)
COVER_TIME_ODD = tuple(
    origin for origin in ORIGINS if origin[0] % 2 == 1
)
THETA = b142.canonical_theta()

# the concrete shear-free profile Block 142's gate D control used
NU_FIXTURE = tuple(b105.OVERLAP_SHEARS[t][1] for t in range(PHYS_T))
NU_SYMBOLIC = sp.symbols("nu0 nu1 nu2 nu3", positive=True)
NU_FLAT = (sp.Integer(1),) * PHYS_T
NU_OTHER = (sp.Integer(1), sp.Integer(2), sp.Integer(3), sp.Integer(5))

# the certificate constants this runner is claiming
HODGE_SLICE_VALUES = (
    R(256, 255),
    R(9, 10),
    R(1013, 1040),
    R(10001, 10608),
)
HODGE_INERTIA = (PHYS, 0, 0)
GRAM_INERTIA = (HALF, 0, 0)
NULL_EDGES = ((0, 0), (0, 1), (1, 0), (1, 1))
LIVE_RANK = 8
CENSUS_COUNTS = frozenset({((2, 0, 6), 6), ((6, 0, 2), 6)})
ODD_DIAGONAL_SITES = (1, 3, 5, 7)
MINOR_SITES = (1, 3)
# P[1,3] = (lambda_ij + c_l) * (nu_2^2 + 2 nu_2 nu_3 + 1) / (5 nu_2)
CHART_OFFSETS = (0, 0, -1, 1)
FIXTURE_PAIRING_UNIT = R(10001, 13260)
SELF_EDGE_22_ENTRY = -R(10001, 13260)
LEFTOVER_COMPANION_EDGES = ((2, 2), (3, 3))
LEFTOVER_COMPANION_RANK = 0
COMPANION_RANK4_EDGES = 14
SIGNED_REFLECTION_FAMILY = 256
FINGERPRINT_COUNT = 4
RESIDUAL_RANK = 16
HEALING_GENERATOR_RANK = 12
THRESHOLD_SET = (
    sp.Integer(0),
    R(4, 15),
    R(2, 5),
    R(4, 5),
    R(16, 15),
    R(6, 5),
    R(22, 15),
)
GLOBAL_THRESHOLD = R(22, 15)
THRESHOLD_MARGIN = R(1, 1000)
OTHER_PROFILE_THRESHOLD = R(220, 81)


def shear_free_field(nu) -> dict:
    """Block 142 gate D's control carrier: overlap profile (0, nu(t))."""
    return {
        (t, x): (sp.Integer(0), nu[t])
        for t in range(PHYS_T)
        for x in range(LX)
    }


def carrier(nu) -> sp.Matrix:
    """The antiperiodic quotient Hodge H_q of one shear-free profile."""
    return sp.expand(
        b134.antiperiodic_quotient(b142.hodge_from_field(shear_free_field(nu)))
    )


def cover_hodge(nu) -> sp.Matrix:
    return b142.hodge_from_field(shear_free_field(nu))


def half_pairings(hodge, differentials, star, weights) -> tuple[dict, dict]:
    """The 16 healed edge actions and their half-pairings P = [theta Q]_{++}."""
    weight = {origin: weights[INDEX[origin]] for origin in ORIGINS}
    edges: dict[tuple[int, int], sp.Matrix] = {}
    blocks: dict[tuple[int, int], sp.Matrix] = {}
    for left in ORIGINS:
        for right in ORIGINS:
            dressing = sp.expand((weight[right] - weight[left]) * star)
            action = sp.expand(
                b137.quotient_action(
                    sp.expand(differentials[left] + dressing), hodge, MASS
                )
            )
            key = (INDEX[left], INDEX[right])
            edges[key] = action
            blocks[key] = sp.expand(b142.pairing(THETA, action))
    return edges, blocks


def chart_pairings(hodge, differentials, star) -> dict[int, sp.Matrix]:
    """P of the four left charts at a SYMBOLIC dressing weight w.

    Every edge (i,j) is this object at w = lambda_ij = x_j - x_i, so the four
    chart pairings carry the whole 16-edge family with the weight left free.
    """
    return {
        INDEX[left]: sp.expand(
            b142.pairing(
                THETA,
                sp.expand(
                    b137.quotient_action(
                        sp.expand(differentials[left] + WEIGHT * star),
                        hodge,
                        MASS,
                    )
                ),
            )
        )
        for left in ORIGINS
    }


def zero_dressing_cover_time_even(weights) -> tuple:
    """The predicted null locus: zero dressing and a cover-time-EVEN left."""
    weight = {origin: weights[INDEX[origin]] for origin in ORIGINS}
    return tuple(
        sorted(
            (INDEX[left], INDEX[right])
            for left in COVER_TIME_EVEN
            for right in ORIGINS
            if weight[right] == weight[left]
        )
    )


def census_of(blocks: dict) -> dict:
    return {
        key: congruence_inertia(block)
        for key, block in blocks.items()
        if not zero(block)
    }


def census_counts(blocks: dict) -> frozenset:
    counts: dict[tuple[int, int, int], int] = {}
    for value in census_of(blocks).values():
        counts[value] = counts.get(value, 0) + 1
    return frozenset(counts.items())


def psd_threshold(block: sp.Matrix, gram: sp.Matrix):
    """The least m >= 0 with block + m*gram positive semidefinite.

    gram is positive definite, so the pencil gram^{-1} block is diagonalisable
    with real spectrum and the threshold is max(0, -min eigenvalue), computed
    from the exact rational characteristic polynomial.
    """
    pencil = sp.expand(gram.inv() * block)
    poly = sp.Poly(sp.expand(pencil.charpoly(LAM).as_expr()), LAM)
    roots = sp.polys.polytools.real_roots(poly)
    if len(roots) != block.rows:
        return None
    return sp.simplify(sp.Max(0, -min(roots)))


# ---------------------------------------------------------------------------
# F. the replaced blocker mechanism: slice fixing
# ---------------------------------------------------------------------------
def signed_permutation_image(matrix: sp.Matrix):
    """(sigma, True) when the matrix is a signed permutation, else (None, False).

    sigma[i] is the row carrying column i's single nonzero entry.
    """
    image: list[int] = []
    for column in range(matrix.rows):
        rows = [
            row for row in range(matrix.rows)
            if sp.expand(matrix[row, column]) != 0
        ]
        if len(rows) != 1 or sp.expand(matrix[rows[0], column]) not in (1, -1):
            return (None, False)
        image.append(rows[0])
    return (tuple(image), len(set(image)) == matrix.rows)


def reflection_family():
    """The 256 signed cover reflections of Block 142, descended to the quotient."""
    for shift_t in range(COVER_T):
        for shift_x in range(LX):
            for overall in (1, -1):
                for alpha in (0, 1):
                    for beta in (0, 1):
                        yield (
                            (shift_t, shift_x, overall, alpha, beta),
                            b142.descend(
                                b142.signed_cover_reflection(
                                    shift_t, shift_x, overall, alpha, beta
                                )
                            ),
                        )


def slice_certificate(hodge_quotient: sp.Matrix) -> dict:
    """The exact replacement for Block 142's fingerprint blocker.

    H_q is diagonal with h depending only on the time slice p, so for a signed
    permutation S with image sigma, (S^dagger H_q S)[i,i] = h(slice(sigma(i))).
    Preserving H_q therefore FORCES h(slice(sigma(i))) = h(slice(i)) for every
    site i; with four DISTINCT slice values that means sigma must fix every time
    slice setwise.  Every descended lattice reflection acts on slices as
    p -> (b - p) mod 4 for some shift b, and no b has h(b - p) = h(p) for all p,
    so no reflection can fix the slices and none can preserve H_q.  The direct
    256-member scan is run alongside as an independent confirmation.
    """
    values = tuple(
        sp.expand(hodge_quotient[p * LX, p * LX]) for p in range(PHYS_T)
    )
    slice_shifts_with_symmetry = tuple(
        shift
        for shift in range(PHYS_T)
        if all(values[(shift - p) % PHYS_T] == values[p] for p in range(PHYS_T))
    )
    total = 0
    descending = 0
    signed_permutations = 0
    preserving = 0
    diagonal_matching = 0
    realised_shifts: set[int] = set()
    slice_action_is_reflection = True
    for _, descended in reflection_family():
        total += 1
        if descended is None:
            continue
        descending += 1
        image, is_signed_permutation = signed_permutation_image(descended)
        if not is_signed_permutation:
            slice_action_is_reflection = False
            continue
        signed_permutations += 1
        shifts = {
            (image[index] // LX + index // LX) % PHYS_T
            for index in range(PHYS)
        }
        if len(shifts) == 1:
            realised_shifts |= shifts
        else:
            slice_action_is_reflection = False
        if all(
            values[image[index] // LX] == values[index // LX]
            for index in range(PHYS)
        ):
            diagonal_matching += 1
        if zero(
            sp.expand(descended.H * hodge_quotient * descended - hodge_quotient)
        ):
            preserving += 1
    return {
        "slice_values": values,
        "distinct_slice_values": len(set(values)),
        "slice_shifts_with_symmetry": slice_shifts_with_symmetry,
        "family_size": total,
        "descending": descending,
        "signed_permutations": signed_permutations,
        "preserving": preserving,
        "diagonal_matching": diagonal_matching,
        "realised_shifts": tuple(sorted(realised_shifts)),
        "slice_action_is_reflection": slice_action_is_reflection,
    }


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    # B: the diagonal-Hodge law
    inertia_calibration: bool
    hodge_is_diagonal: bool
    hodge_symbolic_diagonal: bool
    hodge_x_independent: bool
    hodge_symbolic_x_independent: bool
    hodge_slice_values: tuple
    hodge_law_symbolic: bool
    hodge_inertia: tuple
    gram_inertia: tuple
    seam_gram_zero: bool
    seam_gram_symbolic_zero: bool
    theta_mass_block_zero: bool
    theta_mass_block_symbolic_zero: bool
    # C: the Block 141 carryover on this carrier
    edge_nilpotent_count: int
    atlas_curvature_nonzero: int
    self_dressings_zero: bool
    companion_rank4_edges: int
    leftover_companion_edges: tuple
    leftover_companion_ranks: frozenset
    # D: the pairing
    hermitian_edges: int
    symbolic_hermitian_charts: int
    pairing_mass_free: bool
    symbolic_pairing_mass_free: bool
    null_edges: tuple
    predicted_null_edges: tuple
    even_left_charts_null_at_zero_weight: int
    odd_left_charts_live_at_zero_weight: int
    # E: the verdict
    live_edge_count: int
    live_edge_ranks: frozenset
    census_counts: frozenset
    psd_live_edges: int
    odd_diagonal_zero_symbolic: bool
    minor_is_negative_modulus: bool
    minor_negative_edges: int
    chart_offsets_measured: tuple
    pairing_formula_edges: int
    fixture_pairing_unit: sp.Expr
    self_edge_22_entry: sp.Expr
    # F: the blocker with the replaced mechanism
    distinct_slice_values: int
    slice_shifts_with_symmetry: tuple
    reflection_family_size: int
    reflections_descending: int
    reflections_signed_permutations: int
    reflections_preserving: int
    reflections_matching_diagonal: int
    slice_action_is_reflection: bool
    realised_slice_shifts: tuple
    fingerprint_count: int
    flat_hodge_is_identity: bool
    flat_reflections_preserving: int
    # G: curvature blindness and the completions
    flat_null_edges: tuple
    flat_census_counts: frozenset
    carriers_differ: bool
    pairing_entries_differ_edges: int
    residual_frame_exact: bool
    residual_rank: int
    residual_formula_rank: int
    healing_generator_rank: int
    residual_identified: bool
    healing_generator_square_zero: bool
    threshold_set: tuple
    global_threshold: sp.Expr
    psd_at_threshold: bool
    fails_below_threshold: bool
    other_profile_threshold: sp.Expr
    swap_grams_zero: bool
    swap_grams_symbolic_zero: bool
    # global
    exact_no_float: bool
    scope: dict


def measure() -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    # The congruence routine is calibrated here, in the measurement pass, on a
    # matrix whose inertia is known by inspection and on which the root-counting
    # helper of Blocks 142/143 is provably wrong.
    inertia_calibration = bool(
        congruence_inertia(sp.diag(1, 2, -3, R(5, 7))) == (3, 0, 1)
        and congruence_inertia(sp.diag(1, 1, -2, -2, 0)) == (2, 1, 2)
        and b142.inertia(sp.diag(1, 1, -2, -2, 0)) != (2, 1, 2)
    )

    # --- the four carriers.  Nothing else builds a Hodge. ------------------
    hodge = cover_hodge(NU_FIXTURE)
    hodge_quotient = carrier(NU_FIXTURE)
    symbolic_hodge = cover_hodge(NU_SYMBOLIC)
    symbolic_quotient = carrier(NU_SYMBOLIC)
    flat_hodge = cover_hodge(NU_FLAT)
    flat_quotient = carrier(NU_FLAT)
    other_hodge = cover_hodge(NU_OTHER)
    other_quotient = carrier(NU_OTHER)

    fixture = b137.connection_data(b134.S_X, b134.S_T)
    differentials = fixture["d"]
    star = sp.expand(differentials[(0, 0)] - differentials[(1, 0)])

    # --- B: the diagonal-Hodge law -----------------------------------------
    hodge_slice_values = tuple(
        sp.expand(hodge_quotient[p * LX, p * LX]) for p in range(PHYS_T)
    )
    hodge_x_independent = all(
        sp.expand(hodge_quotient[p * LX + x, p * LX + x])
        == hodge_slice_values[p]
        for p in range(PHYS_T)
        for x in range(LX)
    )
    hodge_symbolic_x_independent = all(
        sp.simplify(
            symbolic_quotient[p * LX + x, p * LX + x]
            - symbolic_quotient[p * LX, p * LX]
        )
        == 0
        for p in range(PHYS_T)
        for x in range(LX)
    )
    hodge_law_symbolic = all(
        sp.simplify(
            symbolic_quotient[p * LX + x, p * LX + x]
            - (
                2 * NU_SYMBOLIC[p]
                + NU_SYMBOLIC[(p - 1) % PHYS_T]
                + 1 / NU_SYMBOLIC[(p - 1) % PHYS_T]
            )
            / 4
        )
        == 0
        for p in range(PHYS_T)
        for x in range(LX)
    )
    seam_gram = hodge_quotient[MINUS_SITES, PLUS_SITES]
    symbolic_seam_gram = symbolic_quotient[MINUS_SITES, PLUS_SITES]
    theta_mass_block = sp.expand(PLUS.T * THETA * hodge_quotient * PLUS)
    symbolic_theta_mass_block = sp.expand(
        PLUS.T * THETA * symbolic_quotient * PLUS
    )

    # --- C: the Block 141 carryover ----------------------------------------
    weight = {origin: HEALING_WEIGHTS[INDEX[origin]] for origin in ORIGINS}
    dressing = {
        (INDEX[left], INDEX[right]): sp.expand(
            (weight[right] - weight[left]) * star
        )
        for left in ORIGINS
        for right in ORIGINS
    }
    keys = sorted(dressing)
    edge_nilpotent_count = sum(
        1
        for key in keys
        if zero(
            sp.expand(
                (differentials[ORIGINS[key[0]]] + dressing[key])
                * (differentials[ORIGINS[key[0]]] + dressing[key])
            )
        )
    )
    atlas_curvature_nonzero = sum(
        1
        for i in range(len(ORIGINS))
        for j in range(len(ORIGINS))
        for k in range(len(ORIGINS))
        if not zero(
            sp.expand(dressing[(i, k)] - dressing[(j, k)] - dressing[(i, j)])
        )
    )
    self_dressings_zero = all(
        zero(dressing[(i, i)]) for i in range(len(ORIGINS))
    )
    companion_ranks = {
        key: sp.expand(
            b137.quotient_action(
                sp.expand(differentials[ORIGINS[key[0]]] + dressing[key]),
                hodge,
                MASS,
            )[HALF // 2:HALF, 0:HALF // 2]
        ).rank()
        for key in keys
    }
    companion_rank4_edges = sum(
        1 for value in companion_ranks.values() if value == 4
    )
    leftover_companion_edges = tuple(
        sorted(key for key in keys if companion_ranks[key] != 4)
    )
    leftover_companion_ranks = frozenset(
        companion_ranks[key] for key in leftover_companion_edges
    )

    # --- D: the pairing -----------------------------------------------------
    edges, blocks = half_pairings(hodge, differentials, star, HEALING_WEIGHTS)
    symbolic_charts = chart_pairings(symbolic_hodge, differentials, star)
    hermitian_edges = sum(
        1 for block in blocks.values() if zero(sp.expand(block - block.H))
    )
    symbolic_hermitian_charts = sum(
        1
        for block in symbolic_charts.values()
        if zero_simplified(sp.expand(block - block.H))
    )
    pairing_mass_free = all(
        MASS not in sp.expand(block).free_symbols for block in blocks.values()
    )
    symbolic_pairing_mass_free = all(
        MASS not in sp.expand(block).free_symbols
        for block in symbolic_charts.values()
    )
    null_edges = tuple(sorted(key for key in keys if zero(blocks[key])))
    even_left_charts_null_at_zero_weight = sum(
        1
        for origin in COVER_TIME_EVEN
        if zero_simplified(symbolic_charts[INDEX[origin]].subs(WEIGHT, 0))
    )
    odd_left_charts_live_at_zero_weight = sum(
        1
        for origin in COVER_TIME_ODD
        if not zero_simplified(symbolic_charts[INDEX[origin]].subs(WEIGHT, 0))
    )

    # --- E: the verdict -----------------------------------------------------
    live_keys = [key for key in keys if key not in null_edges]
    live_edge_ranks = frozenset(blocks[key].rank() for key in live_keys)
    census = {key: congruence_inertia(blocks[key]) for key in live_keys}
    counts: dict[tuple[int, int, int], int] = {}
    for value in census.values():
        counts[value] = counts.get(value, 0) + 1
    psd_live_edges = sum(1 for value in census.values() if value[2] == 0)

    row, column = MINOR_SITES
    odd_diagonal_zero_symbolic = all(
        sp.simplify(block[j, j]) == 0
        for block in symbolic_charts.values()
        for j in ODD_DIAGONAL_SITES
    )
    minors = {
        key: sp.expand(
            blocks[key][row, row] * blocks[key][column, column]
            - blocks[key][row, column] * blocks[key][column, row]
        )
        for key in keys
    }
    minor_is_negative_modulus = all(
        sp.simplify(
            minors[key] + sp.Abs(blocks[key][row, column]) ** 2
        )
        == 0
        for key in keys
    )
    minor_negative_edges = sum(1 for key in keys if minors[key] < 0)

    # the CORRECTED closed form: the chart offset c_l is carried by the LEFT
    # chart alone and is NOT the weight difference, so the two forced self-edges
    # (2,2) and (3,3) are nonzero at lambda = 0.
    unit = (
        NU_SYMBOLIC[2] ** 2
        + 2 * NU_SYMBOLIC[2] * NU_SYMBOLIC[3]
        + 1
    ) / (5 * NU_SYMBOLIC[2])
    chart_offsets_measured = tuple(
        sp.simplify(
            sp.simplify(symbolic_charts[left][row, column] / unit) - WEIGHT
        )
        for left in range(len(ORIGINS))
    )
    fixture_unit = sp.simplify(
        unit.subs(dict(zip(NU_SYMBOLIC, NU_FIXTURE)))
    )
    pairing_formula_edges = sum(
        1
        for key in keys
        if sp.simplify(
            blocks[key][row, column]
            - (
                HEALING_WEIGHTS[key[1]]
                - HEALING_WEIGHTS[key[0]]
                + CHART_OFFSETS[key[0]]
            )
            * fixture_unit
        )
        == 0
    )

    # --- F: the blocker with the replaced mechanism -------------------------
    slice_facts = slice_certificate(hodge_quotient)
    flat_slice_facts = slice_certificate(flat_quotient)
    absolute = [
        tuple(
            sorted(
                sp.Abs(hodge_quotient[r, c]) for c in range(PHYS)
            )
        )
        for r in range(PHYS)
    ]
    fingerprint_count = len(set(absolute))

    # --- G: curvature blindness and the completions -------------------------
    flat_edges, flat_blocks = half_pairings(
        flat_hodge, differentials, star, HEALING_WEIGHTS
    )
    other_edges, other_blocks = half_pairings(
        other_hodge, differentials, star, HEALING_WEIGHTS
    )
    flat_null_edges = tuple(sorted(key for key in keys if zero(flat_blocks[key])))
    pairing_entries_differ_edges = sum(
        1 for key in keys if not zero(sp.expand(blocks[key] - flat_blocks[key]))
    )

    shear_x, shear_t = sp.symbols("s_x s_t", real=True, nonzero=True)
    selector = b134.selector_system(
        tuple(
            (origin, b134.chart_gauge(origin)) for origin in b134.DISPLAYED
        ),
        b134.local_differential(shear_x, shear_t),
    )
    certificate = b134.residual_operator_certificate(selector, shear_t)
    at_fixture = {shear_x: b134.S_X, shear_t: b134.S_T}
    residual_rank = sp.simplify(certificate.omega.subs(at_fixture)).rank()
    residual_formula_rank = sp.simplify(
        certificate.formula.subs(at_fixture)
    ).rank()
    healing_generator_rank = star.rank()

    gram = hodge_quotient[PLUS_SITES, PLUS_SITES]
    thresholds = {key: psd_threshold(blocks[key], gram) for key in keys}
    global_threshold = max(thresholds.values())
    psd_at_threshold = all(
        congruence_inertia(
            sp.expand(blocks[key] + global_threshold * gram)
        )[2]
        == 0
        for key in keys
    )
    fails_below_threshold = any(
        congruence_inertia(
            sp.expand(
                blocks[key] + (global_threshold - THRESHOLD_MARGIN) * gram
            )
        )[2]
        > 0
        for key in keys
    )
    other_gram = other_quotient[PLUS_SITES, PLUS_SITES]
    other_profile_threshold = max(
        psd_threshold(other_blocks[key], other_gram) for key in keys
    )

    # every natural seam transport of the Gram, all of them zero here
    swap = sp.expand(-THETA)
    swap_grams = (
        theta_mass_block,
        sp.expand(PLUS.T * hodge_quotient * swap * PLUS),
        sp.expand(PLUS.T * swap * hodge_quotient * PLUS),
        sp.expand(
            hodge_quotient[PLUS_SITES, MINUS_SITES]
            * swap[MINUS_SITES, PLUS_SITES]
        ),
    )
    symbolic_swap_grams = (
        symbolic_theta_mass_block,
        sp.expand(PLUS.T * symbolic_quotient * swap * PLUS),
        sp.expand(PLUS.T * swap * symbolic_quotient * PLUS),
        sp.expand(
            symbolic_quotient[PLUS_SITES, MINUS_SITES]
            * swap[MINUS_SITES, PLUS_SITES]
        ),
    )

    exact_no_float = no_float(
        (
            hodge_quotient,
            flat_quotient,
            other_quotient,
            THETA,
            star,
            tuple(edges.values()),
            tuple(blocks.values()),
            tuple(flat_blocks.values()),
            tuple(other_blocks.values()),
            tuple(thresholds.values()),
            hodge_slice_values,
            fixture_unit,
            global_threshold,
            other_profile_threshold,
        )
    )

    return Facts(
        main_head=main_head,
        authority=authority,
        inertia_calibration=inertia_calibration,
        hodge_is_diagonal=is_diagonal(hodge_quotient),
        hodge_symbolic_diagonal=is_diagonal(symbolic_quotient),
        hodge_x_independent=hodge_x_independent,
        hodge_symbolic_x_independent=hodge_symbolic_x_independent,
        hodge_slice_values=hodge_slice_values,
        hodge_law_symbolic=hodge_law_symbolic,
        hodge_inertia=congruence_inertia(hodge_quotient),
        gram_inertia=congruence_inertia(gram),
        seam_gram_zero=zero(seam_gram),
        seam_gram_symbolic_zero=zero_simplified(symbolic_seam_gram),
        theta_mass_block_zero=zero(theta_mass_block),
        theta_mass_block_symbolic_zero=zero_simplified(
            symbolic_theta_mass_block
        ),
        edge_nilpotent_count=edge_nilpotent_count,
        atlas_curvature_nonzero=atlas_curvature_nonzero,
        self_dressings_zero=self_dressings_zero,
        companion_rank4_edges=companion_rank4_edges,
        leftover_companion_edges=leftover_companion_edges,
        leftover_companion_ranks=leftover_companion_ranks,
        hermitian_edges=hermitian_edges,
        symbolic_hermitian_charts=symbolic_hermitian_charts,
        pairing_mass_free=pairing_mass_free,
        symbolic_pairing_mass_free=symbolic_pairing_mass_free,
        null_edges=null_edges,
        predicted_null_edges=zero_dressing_cover_time_even(HEALING_WEIGHTS),
        even_left_charts_null_at_zero_weight=(
            even_left_charts_null_at_zero_weight
        ),
        odd_left_charts_live_at_zero_weight=(
            odd_left_charts_live_at_zero_weight
        ),
        live_edge_count=len(live_keys),
        live_edge_ranks=live_edge_ranks,
        census_counts=frozenset(counts.items()),
        psd_live_edges=psd_live_edges,
        odd_diagonal_zero_symbolic=odd_diagonal_zero_symbolic,
        minor_is_negative_modulus=minor_is_negative_modulus,
        minor_negative_edges=minor_negative_edges,
        chart_offsets_measured=chart_offsets_measured,
        pairing_formula_edges=pairing_formula_edges,
        fixture_pairing_unit=fixture_unit,
        self_edge_22_entry=sp.expand(blocks[(2, 2)][row, column]),
        distinct_slice_values=slice_facts["distinct_slice_values"],
        slice_shifts_with_symmetry=slice_facts["slice_shifts_with_symmetry"],
        reflection_family_size=slice_facts["family_size"],
        reflections_descending=slice_facts["descending"],
        reflections_signed_permutations=slice_facts["signed_permutations"],
        reflections_preserving=slice_facts["preserving"],
        reflections_matching_diagonal=slice_facts["diagonal_matching"],
        slice_action_is_reflection=slice_facts["slice_action_is_reflection"],
        realised_slice_shifts=slice_facts["realised_shifts"],
        fingerprint_count=fingerprint_count,
        flat_hodge_is_identity=zero(sp.expand(flat_quotient - IDENTITY)),
        flat_reflections_preserving=flat_slice_facts["preserving"],
        flat_null_edges=flat_null_edges,
        flat_census_counts=census_counts(flat_blocks),
        carriers_differ=not zero(sp.expand(hodge_quotient - flat_quotient)),
        pairing_entries_differ_edges=pairing_entries_differ_edges,
        residual_frame_exact=certificate.signed_frame_exact,
        residual_rank=residual_rank,
        residual_formula_rank=residual_formula_rank,
        healing_generator_rank=healing_generator_rank,
        residual_identified=healing_generator_rank == residual_formula_rank,
        healing_generator_square_zero=zero(sp.expand(star * star)),
        threshold_set=tuple(sorted(set(thresholds.values()))),
        global_threshold=global_threshold,
        psd_at_threshold=psd_at_threshold,
        fails_below_threshold=fails_below_threshold,
        other_profile_threshold=other_profile_threshold,
        swap_grams_zero=all(zero(gram_matrix) for gram_matrix in swap_grams),
        swap_grams_symbolic_zero=all(
            zero_simplified(gram_matrix)
            for gram_matrix in symbolic_swap_grams
        ),
        exact_no_float=exact_no_float,
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = "N5: per_element: on Block 142's gate-D SHEAR-FREE carrier with overlap profile (0, nu(p)) the quotiented Hodge H_q is DIAGONAL, x-INDEPENDENT and POSITIVE DEFINITE on all 16 sites with the exact law h(p) = (2 nu_p + nu_{p-1} + 1/nu_{p-1})/4, symbolic in EVERY positive profile nu, taking the four distinct fixture values 256/255, 9/10, 1013/1040, 10001/10608; and THE SEAM GRAM VANISHES, H_q[-,+] = 0 and [theta H_q]_{++} = 0 IDENTICALLY IN nu, so every half-pairing P is m-FREE and the mass leaves the pairing entirely -- this is the mechanism naming the block\nper_site: the odd diagonal P[1,1] = P[3,3] = P[5,5] = P[7,7] = 0 IDENTICALLY, so the (1,3) principal minor is exactly -|P[1,3]|^2 < 0 on all 12 live edges, with the CORRECTED entry formula P[1,3] = (lambda_ij + c_l)(nu_2^2 + 2 nu_2 nu_3 + 1)/(5 nu_2) where c_l = (0, 0, -1, +1) is indexed by the LEFT CHART and the coefficient is NOT the bare weight difference -- edge (2,2) has lambda = 0 yet P[1,3] = -10001/13260\nper_mode: the healing family's CARRIER-FREE half survives VERBATIM (16/16 edge nilpotency, 0/64 atlas curvature, Omega_ii = 0) while its CARRIER-DEPENDENT half re-derives to companion rank 4 on 14/16 edges, with the refinement that the two leftover self-edges (2,2),(3,3) sit at companion rank 0 here, NOT the staircase's rank 3\nper_block: all 16 healed pairings are HERMITIAN with the canonical lattice theta, symbolic in nu and in the weights; exactly 4 edges have P IDENTICALLY ZERO -- the zero-dressing cover-time-even-left locus, where Block 143's nilpotent locus goes TOTALLY NULL, with P(w=0) = 0 for even-left and nonzero for odd-left identically in nu -- and the other 12 have rank 8 with census {(2,0,6) x6, (6,0,2) x6}, so NO healed pairing is positive semidefinite: the verdict is NEVER PSD, m-FREE and PROFILE-UNIFORM\nlattice_wide: 0/256 signed lattice reflections preserve the shear-free H_q, but Block 142's FINGERPRINT ARGUMENT COLLAPSES here -- fingerprints 15 -> 4, the absolute-value preserver group jumping to 24^4 -- and is REPLACED by a strictly stronger certificate: with four distinct slice values any signed permutation preserving H_q must FIX EVERY TIME SLICE, so NO half-exchanging isometry exists at all and NO shift b satisfies h(b-p) = h(p); by CONTRAST the flat profile gives H_q = I with 256/256 reflections preserving it, so the blocker is genuinely CARRIER-DRIVEN\nRESULT: on the displayed Block 105 atlas at s_x = 3/5, s_t = 4/5 with symbolic m, the shear-free carrier makes the pairing MASSLESS and positivity still FAILS for every positive profile; the fixture IS genuinely curved -- Block 134's selector-conflict residual, whose closed form 2 i s_t T_t^{-1} P_even P_x holds in the signed frame W and has rank 16, and Block 137's rank-16 C_ijk are untouched by the carrier change, but that closed form must NOT be identified with the healing generator Omega* = d_(0,0) - d_(1,0), which has rank 12 and which NO FRAME identifies with it -- while the FLAT profile nu = (1,1,1,1) reproduces the ENTIRE INERTIA CENSUS VERBATIM, the same 4 null edges and the same {(2,0,6),(6,0,2)}, though the pairing entries DIFFER, so THE CENSUS, NOT THE PAIRING, IS CURVATURE-BLIND AS PROBED and both readings are displayed; the named-hypothesis mass completion P + m H_q[+,+] becomes PSD on all 16 edges exactly at m >= 22/15 for the displayed profile with per-edge threshold set {0, 4/15, 2/5, 4/5, 16/15, 6/5, 22/15} and profile-dependent threshold 220/81 at nu = (1,2,3,5), a HAND-INSERTED repair and not a derived structure, while the swap-type completions are VACUOUS here, not merely unhelpful, every swap-type Gram being IDENTICALLY ZERO because the seam Gram vanishes; and Block 142's inertia helper counts DISTINCT real roots and is UNSOUND on this degenerate carrier, reporting (4,0,0) for H_q, so every inertia in this block is computed by EXACT SYMMETRIC CONGRUENCE and the runner uses congruence inertia throughout\nDECISION_CUT: test carriers with NONVANISHING seam Gram, so that the mass re-enters the pairing at all; build CURVATURE-SENSITIVE pairings, since the census as probed cannot separate the curved profile from the flat one; execute the skew-sector program, noting that its object R = beta^{-1} K[-,+] is undefined here because beta = 0; decide the two forced self-edges and the admissibility class of coboundary dressings; execute the joint-lane program; curved OS is not decided\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero"


SCOPE_KEYS = (
    "diagonal_hodge",
    "hodge_law",
    "mass_free_pairing",
    "null_locus",
    "inertia_census",
    "never_semidefinite",
    "corrected_formula",
    "slice_fixing",
    "flat_contrast",
    "curvature_blind",
    "rank_split",
    "mass_thresholds",
    "vacuous_swap",
    "tooling_disclosure",
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
        "diagonal_hodge": "diagonal" in note,
        # Either the law itself or the structural consequence that follows from
        # it; the note is free to lead with whichever reads better.
        "hodge_law": (
            "h(p)" in note
            or "2 nu_p" in note
            or "seam gram" in note
        ),
        "mass_free_pairing": (
            "the mass leaves the pairing" in note or "m-free" in note
        ),
        "null_locus": "cover-time-even-left" in note,
        # Whitespace-insensitive so the note may write (2, 0, 6) or (2,0,6).
        "inertia_census": "(2,0,6)" in compact and "(6,0,2)" in compact,
        "never_semidefinite": "never positive semidefinite" in note,
        "corrected_formula": (
            "5 nu_2" in note or "5nu_2" in compact or "c_l" in note
        ),
        "slice_fixing": "fix every time slice" in note,
        "flat_contrast": "256/256" in note,
        "curvature_blind": "census" in note and "curvature-blind" in note,
        "rank_split": (
            ("rank 12" in note and "rank 16" in note)
            or "not identified" in note
        ),
        "mass_thresholds": "22/15" in note and "profile-dependent" in note,
        "vacuous_swap": "identically zero" in note,
        "tooling_disclosure": "congruence" in note,
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
        "hodge_law_holds": True,
        "seam_gram_is_zero": True,
        "edge_nilpotent_count": PHYS,
        "leftover_companion_rank": LEFTOVER_COMPANION_RANK,
        "pairing_is_mass_free": True,
        "null_edge_count": len(NULL_EDGES),
        "census_counts": CENSUS_COUNTS,
        "chart_offsets": CHART_OFFSETS,
        "psd_live_edges": 0,
        "preserving_reflections": 0,
        "flat_preserving_reflections": SIGNED_REFLECTION_FAMILY,
        "global_threshold": GLOBAL_THRESHOLD,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "break_hodge_law":
        claims["hodge_law_holds"] = False
    elif mutation == "claim_seam_gram_nonzero":
        claims["seam_gram_is_zero"] = False
    elif mutation == "break_edge_nilpotency":
        claims["edge_nilpotent_count"] = PHYS - 1
    elif mutation == "wrong_leftover_rank":
        claims["leftover_companion_rank"] = 3
    elif mutation == "claim_pairing_mass_dependent":
        claims["pairing_is_mass_free"] = False
    elif mutation == "wrong_null_count":
        claims["null_edge_count"] = 3
    elif mutation == "wrong_census":
        claims["census_counts"] = frozenset(
            {((2, 0, 6), 6), ((4, 0, 4), 6)}
        )
    elif mutation == "wrong_formula_offset":
        claims["chart_offsets"] = (0, 0, -1, -1)
    elif mutation == "claim_positive_semidefinite_edge":
        claims["psd_live_edges"] = 1
    elif mutation == "claim_preserver_exists":
        claims["preserving_reflections"] = 1
    elif mutation == "break_flat_contrast":
        claims["flat_preserving_reflections"] = SIGNED_REFLECTION_FAMILY - 1
    elif mutation == "wrong_mass_threshold":
        claims["global_threshold"] = R(3, 2)
    elif mutation == "drop_n5_fence":
        claims["required_scope_keys"] = tuple(
            key for key in SCOPE_KEYS if key != "n5_verbatim"
        )
    return claims


# ---------------------------------------------------------------------------
# gates: pure functions of the measured facts and the claims
# ---------------------------------------------------------------------------
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_MASSLESS_SEAM_VERDICT_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGGERED_HERMITIAN_PAIRING_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.py",
            "logs/runner-cache/admissibility_dirac_kahler_staggered_hermitian_pairing_2026_08_19.txt",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CARRIER_REFLECTION_BLOCKER_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_carrier_reflection_blocker_2026_08_19.py",
        )
        and PARENT_ARTIFACTS
        == (
            BLOCK143_NOTE,
            BLOCK143_RUNNER,
            BLOCK143_CACHE,
            BLOCK142_NOTE,
            BLOCK142_RUNNER,
        )
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.inertia_calibration
        and facts.hodge_is_diagonal
        and facts.hodge_symbolic_diagonal
        and facts.hodge_x_independent
        and facts.hodge_symbolic_x_independent
        and facts.hodge_slice_values == HODGE_SLICE_VALUES
        and facts.hodge_law_symbolic == bool(claims["hodge_law_holds"])
        and facts.hodge_inertia == HODGE_INERTIA
        and facts.gram_inertia == GRAM_INERTIA
        and facts.seam_gram_zero == bool(claims["seam_gram_is_zero"])
        and facts.seam_gram_symbolic_zero == bool(claims["seam_gram_is_zero"])
        and facts.theta_mass_block_zero
        and facts.theta_mass_block_symbolic_zero
        and facts.exact_no_float
    )

    gate_c = bool(
        facts.edge_nilpotent_count == claims["edge_nilpotent_count"]
        and facts.atlas_curvature_nonzero == 0
        and facts.self_dressings_zero
        and facts.companion_rank4_edges == COMPANION_RANK4_EDGES
        and facts.leftover_companion_edges == LEFTOVER_COMPANION_EDGES
        and facts.leftover_companion_ranks
        == frozenset({claims["leftover_companion_rank"]})
        and facts.exact_no_float
    )

    gate_d = bool(
        facts.hermitian_edges == PHYS
        and facts.symbolic_hermitian_charts == len(ORIGINS)
        and facts.pairing_mass_free == bool(claims["pairing_is_mass_free"])
        and facts.symbolic_pairing_mass_free
        == bool(claims["pairing_is_mass_free"])
        and facts.null_edges == facts.predicted_null_edges
        and facts.null_edges == NULL_EDGES
        and len(facts.null_edges) == claims["null_edge_count"]
        and facts.even_left_charts_null_at_zero_weight == len(COVER_TIME_EVEN)
        and facts.odd_left_charts_live_at_zero_weight == len(COVER_TIME_ODD)
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.live_edge_count == PHYS - len(NULL_EDGES)
        and facts.live_edge_ranks == frozenset({LIVE_RANK})
        and facts.census_counts == claims["census_counts"]
        and facts.psd_live_edges == claims["psd_live_edges"]
        and facts.odd_diagonal_zero_symbolic
        and facts.minor_is_negative_modulus
        and facts.minor_negative_edges == PHYS - len(NULL_EDGES)
        and facts.chart_offsets_measured
        == tuple(sp.Integer(value) for value in claims["chart_offsets"])
        and facts.pairing_formula_edges == PHYS
        and facts.fixture_pairing_unit == FIXTURE_PAIRING_UNIT
        and facts.self_edge_22_entry == SELF_EDGE_22_ENTRY
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.distinct_slice_values == PHYS_T
        and facts.slice_shifts_with_symmetry == ()
        and facts.reflection_family_size == SIGNED_REFLECTION_FAMILY
        and facts.reflections_descending == SIGNED_REFLECTION_FAMILY
        and facts.reflections_signed_permutations == SIGNED_REFLECTION_FAMILY
        and facts.slice_action_is_reflection
        and facts.realised_slice_shifts == tuple(range(PHYS_T))
        and facts.reflections_matching_diagonal == 0
        and facts.reflections_preserving == claims["preserving_reflections"]
        and facts.fingerprint_count == FINGERPRINT_COUNT
        and facts.flat_hodge_is_identity
        and facts.flat_reflections_preserving
        == claims["flat_preserving_reflections"]
        and facts.exact_no_float
    )

    gate_g = bool(
        facts.flat_null_edges == facts.null_edges
        and facts.flat_census_counts == facts.census_counts
        and facts.carriers_differ
        and facts.pairing_entries_differ_edges > 0
        and facts.residual_frame_exact
        and facts.residual_rank == RESIDUAL_RANK
        and facts.residual_formula_rank == RESIDUAL_RANK
        and facts.healing_generator_rank == HEALING_GENERATOR_RANK
        and not facts.residual_identified
        and facts.healing_generator_square_zero
        and facts.threshold_set == THRESHOLD_SET
        and facts.global_threshold == claims["global_threshold"]
        and facts.psd_at_threshold
        and facts.fails_below_threshold
        and facts.other_profile_threshold == OTHER_PROFILE_THRESHOLD
        and facts.other_profile_threshold != facts.global_threshold
        and facts.swap_grams_zero
        and facts.swap_grams_symbolic_zero
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
        and elapsed_ns <= 900 * 1_000_000_000
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
    mutation = parser.parse_args().mutation
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
    facts = measure()
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
        "main plus the committed Block 143 note/runner/cache and Block 142 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-diagonal-hodge-law",
        "on the shear-free carrier (0,nu(t)) the quotient Hodge H_q is diagonal, x-independent and positive definite by congruence with inertia (16,0,0), obeying h(p)=(2*nu_p+nu_{p-1}+1/nu_{p-1})/4 symbolically in every positive profile and taking the values (256/255,9/10,1013/1040,10001/10608) at the fixture, and its diagonality makes the seam Gram H_q[-,+] and the mass block [theta*H_q]_{++} vanish identically in nu",
        gate_values["B"],
    )
    checks.check(
        "C-healing-carryover",
        "the Block 141 healing survives the carrier change: 16/16 edge nilpotency, 0/64 atlas curvature, Omega_ii=0, and companion rank 4 on 14/16 edges with the two leftovers being exactly the forced self-edges (2,2),(3,3) at companion rank 0, not rank 3",
        gate_values["C"],
    )
    checks.check(
        "D-massless-pairing",
        "P_ij=[theta*Q_ij]_{++} is Hermitian on 16/16 edges and symbolically in nu and the dressing weight, and it is m-FREE because the seam Gram vanishes, with the null locus being exactly the four zero-dressing cover-time-even-left edges: P(w=0) is identically zero on both even-left charts and nonzero on both odd-left charts",
        gate_values["D"],
    )
    checks.check(
        "E-positivity-verdict",
        "the 12 live edges have rank 8 and congruence-inertia census {(2,0,6)x6,(6,0,2)x6} with no positive-semidefinite edge, P[j,j]=0 identically for j in (1,3,5,7) on every edge and every nu, so minor_{1,3}=-|P[1,3]|^2<0 on all 12, with the corrected closed form P[1,3]=(lambda_ij+c_l)*(nu_2^2+2*nu_2*nu_3+1)/(5*nu_2) and the chart offsets c_l=(0,0,-1,+1) verified symbolically, giving the lambda=0 self-edge (2,2) the nonzero value -10001/13260",
        gate_values["E"],
    )
    checks.check(
        "F-slice-fixing-blocker",
        "0/256 signed lattice reflections preserve H_q, and the mechanism is slice fixing rather than Block 142's fingerprints: h has four distinct values so any preserving signed permutation must fix every time slice, every descended reflection acts on slices as p->b-p with all four shifts realised, and no shift satisfies h(b-p)=h(p), while the flat profile nu=1 gives H_q=I with 256/256 preserving",
        gate_values["F"],
    )
    checks.check(
        "G-curvature-blindness-and-completions",
        "the flat profile reproduces the identical null locus and the identical census while the pairing entries differ, the Block 134 residual keeps its signed-frame closed form at rank 16 while the healing generator Omega* has rank 12 so the two are not identified, every swap-type Gram is identically zero and the swap completion is vacuous, and the mass completion has per-edge thresholds {0,4/15,2/5,4/5,16/15,6/5,22/15} with global threshold 22/15, PSD at 22/15, failure at 22/15-1/1000 and a profile-dependent 220/81 at nu=(1,2,3,5)",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the diagonal-Hodge law, the massless seam, the null locus, the census and its never-semidefinite reading, the corrected chart-offset formula, the slice-fixing mechanism, the flat contrast, the curvature-blindness precision, the rank split, the completion thresholds, the vacuous swap, the tooling disclosure, the disclosures, the firewalls, and the exact N5 fence are present",
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


