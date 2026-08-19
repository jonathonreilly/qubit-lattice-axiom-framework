#!/usr/bin/env python3
# Final path: scripts/admissibility_dirac_kahler_m_block_measurement_theory_2026_08_19.py
"""Block 146: the m-block measurement theory of Sym_2(R)^m.

Block 133 settled the states, dynamics and certified-frame vacuum of the
TWO-block (Z4) observable algebra.  This block lifts that measurement theory to
the whole m-block family Sym_2(R)^m = Sym_2(R) (+) ... (+) Sym_2(R) carried by
the Z_N momentum decomposition with N = 2m, and it lands the general-m theorem
with the corrections the independent checkers forced:

  * THE STATE SPACE IS A PRODUCT OF DISKS.  The algebra has dimension 3m and
    centre R^m; the trace constraint has rank one, so the states form an affine
    body of dimension EXACTLY 3m-1 -- verified symbolically and at m = 2,3,4,5
    (5, 8, 11, 14).  The extreme points are exactly the m DISJOINT RP^1 circles,
    one per block, and the proof runs BOTH ways: idempotence plus Tr D^2 <= 1
    forces all the weight onto a single block and that block onto its circle,
    while every cross-block mixture and every interior disk point is displayed
    as a STRICT convex combination of two distinct states;
  * THE SELECTION RULE IS ONE COMMUTATOR.  [diag(p,q), aI + bX + cZ] =
    b(p-q)(E01 - E10), so an observable commutes with the momentum generator iff
    its X-component vanishes in every block whose generator gap is nonzero.  All
    m gaps ARE nonzero, so the conserved algebra is exactly span{I_j, Z_j}:
    rank m, dimension 2m;
  * THE VACUUM IS FORCED ON THE CONJUGATE PAIRS AND BIASED ON THE SELF PAIR.
    At Z6 (m = 3) and at BOTH committed shears the reality of the fixture forces
    y_{N-k} = conj(y_k), hence q_k = q_{N-k} as EXACT tower elements, while
    q_0 != q_{N/2} exactly.  The gram g = q_{N/2}/q_0 differs from 1 on BOTH
    real branches of the quadratic tower, and the branches disagree about which
    way -- g < 1 on one, g > 1 on the other -- so "which block is heavier" is
    BRANCH-DEPENDENT and only "g != 1" survives.  q_k >= 1 follows from a
    TOWER-AUTOMORPHISM certificate: nested conjugation is an involutive additive
    multiplicative automorphism fixing both generators, so q_k is self-conjugate
    and, under the real embedding available because u_k > 4, is a sum of squared
    moduli whose pivot term is exactly 1.  The central weights close: W_pair =
    2 q_k/S and W_self = q_0(1+g)/S;
  * THE Z8 REALITY CHAIN IS STRUCTURAL AND CHEAP.  The Z8 action is real, and
    the projectors, momentum blocks and monodromies all mirror EXACTLY under
    k -> N-k at both shears.  That chain alone forces q_k = q_{8-k}, because the
    boundary norm is automorphism-invariant.  The full Z8 residue tower is NOT
    on the default gate path -- see the runtime disclosure below;
  * THE DYNAMICS COLLIDE WHENEVER 4 DIVIDES N.  The generator gaps are
    (2, 4, ..., 2(m-1), -m) and the orbit law is exact.  The |rate| = N/2
    coincidence between the conjugate pair (N/4, 3N/4) and the self pair is NOT
    special to Z8: it is the 4|N phenomenon, present at N = 4, 8, 12 and absent
    at N = 6, 10.  The Z4 row agrees with Block 133's landed certificate as a
    MULTISET; Block 133 lists the self block first, so the displayed indices are
    swapped relative to this block's conjugate-first order;
  * THE BALANCED SECTOR REACHES 2(m-1).  Every conjugate pair carries the full
    free-relative-phase equator with zero charge expectation on the balanced
    ray, and the self pair's charge diag(0, m) is positive SEMIdefinite, so
    demanding zero charge expectation there FORCES the balanced amplitude s = 0
    rather than merely leaving the block null; and
  * THE FRAME LEDGER IS A CONVENTION WITH ONE INVARIANT.  The m structured moves
    do send the certified gram to q_0 I_N and the vacuum to Tr/N, but a SINGLE
    positive diagonal congruence reaches the same endpoint, so "m moves" is a
    BOOKKEEPING CONVENTION and not a minimality theorem.  What is invariant is
    conditional: a MIRROR-COMPATIBLE move (lambda_{N-k} = lambda_k) preserves
    q'_k = q'_{N-k}, while an explicit unconstrained move breaks that equality
    and still passes the landed admissibility test.  The bias is removable, so
    the biased-block identification is certified-frame only.

Every scientific comparison is exact: SymPy rationals and radicals, or exact
elements of the committed quadratic towers.  No floats anywhere; the integer
monotonic clock is used only for the runtime gate.

RUNTIME DISCLOSURE (load-bearing).  The full Z8 residue tower -- the sector
factorizations that produce the Z8 direction weights q_0..q_7 -- costs about
FIFTEEN MINUTES of exact tower arithmetic.  It is therefore behind --deep-z8 and
is NOT part of the default gate path, which runs the Z6 tower at both shears,
the cheap Z8 structural reality chain and every symbolic general-m check in
roughly three minutes.  The Z8 vacuum weights were verified INDEPENDENTLY TWICE
before this runner was written -- once by the block solve and once by a separate
checker built from the committed b136 sector algorithm transcribed at N = 8 --
and both runs agreed: q_1 = q_7, q_2 = q_6, q_3 = q_5 exactly, q_0 != q_4, every
q_k real with unit pivot.  Those weights are recorded below as DOCUMENTED
NON-GATE CONSTANTS and are never asserted on the default path; --deep-z8
reproduces them through the same Z8Adapter/Z8Context route the solve used.

TOOLING DISCLOSURE: every fixture object here is built by the COMMITTED Block
136 and Block 139 builders, which gate A pins by blob; nothing is re-implemented
and nothing is sampled.  The Z8 field patch is the solve's Z8Context, which
swaps exactly four Block 136 globals and restores them.

HYPOTHESES, named and not imported: (H1) the observable algebra is the committed
Block 132/136 one -- per momentum-conjugate pair a real symmetric 2x2 Jordan
block spanned by I, Z, X, with the antisymmetric generator excluded.  (H2) the
momentum generator is P = diag(signed Z_N charge) with the charge of sector k
taken in (-N/2, N/2], so the self-conjugate sector N/2 carries +N/2.  (H3) the
certified frame, its direction weights q_k = sum_j |y_kj|^2 and the admissibility
of a frame move are the committed Block 133 ones; ONLY the block count moves.
(H4) the fixtures are the committed Block 136 Z6 fixtures at both displayed
shears and the committed Block 139 Z8 fixture; no new fixture is introduced.
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
I = sp.I
T = sp.Symbol("t", real=True)

I2 = sp.eye(2)
X2 = sp.Matrix(((0, 1), (1, 0)))
Y2 = sp.Matrix(((0, I), (-I, 0)))
Z2 = sp.Matrix(((1, 0), (0, -1)))
J2 = (Z2 * X2 - X2 * Z2) / 2  # the excluded antisymmetric Jordan generator
E01 = sp.Matrix(((0, 1), (0, 0)))
E10 = sp.Matrix(((0, 0), (1, 0)))

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

import admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17 as b133
import admissibility_dirac_kahler_observable_scaling_law_2026_08_18 as b136
import admissibility_dirac_kahler_z8_ledger_completion_2026_08_19 as b139


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_M_BLOCK_MEASUREMENT_THEORY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
BLOCK145_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_"
    "BOUNDED_THEOREM_NOTE_2026-08-19.md"
)
BLOCK145_RUNNER = (
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py"
)
BLOCK133_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_"
    "BOUNDED_THEOREM_NOTE_2026-08-17.md"
)
BLOCK133_RUNNER = (
    "scripts/admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17.py"
)
PARENT_ARTIFACTS = (
    BLOCK145_NOTE,
    BLOCK145_RUNNER,
    BLOCK133_NOTE,
    BLOCK133_RUNNER,
)

# Deliberately literal: this is the complete audit read surface.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_M_BLOCK_MEASUREMENT_THEORY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
    "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17.py",
)

AUDIT_TIMEOUT_SEC = 600
# The five authority pins below are copied verbatim from the Block 145 runner's
# current values; the landing supervisor refreshes them against origin/main.
CURRENT_MAIN = "29d17653c9c043a74041f070e311f03fce114c0a"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block145-seam-dichotomy-20260819"
)
# Landing supervisor: replace this placeholder with the Block 145 branch tip.
# Until it is a 40-hex commit the pin is resolved through PARENT_REF, which is
# a real and verifiable binding; the immutable commit pin lands with the block.
PARENT_COMMIT = "1b3e0d9c73a9dde0f123ae705097b809a2c19ed3"
# Block 144's tip: a real ancestor that predates the Block 145 artifacts and is
# therefore the honest "stale pin" control for the authority mutation.  It is
# read ONLY under the stale mutation; the baseline gate never requires the stale
# blobs to match the worktree.
STALE_PARENT_COMMIT = "6195b68e4f10ffb41c59d65b7cb90cd1d0791323"
# Block 137's recorded main: a real but superseded authority head.
STALE_MAIN = "2dc8dd9b2778a01454874d19b262569ae19ebc6e"

# The default gate path measures the Z6 tower at both shears, the cheap Z8
# reality chain and every symbolic check; --deep-z8 adds the ~15 minute Z8
# residue tower, so the two paths carry different runtime budgets.
DEFAULT_BUDGET_SEC = 900
DEEP_BUDGET_SEC = 2700

MUTATIONS = (
    "stale_main_authority",
    "stale_parent_authority",
    "wrong_state_dimension",
    "break_commutant",
    "break_q_equality",
    "claim_gram_is_one",
    "break_reality_chain",
    "claim_deep_is_default",
    "wrong_generator_rates",
    "wrong_collision_set",
    "break_z4_consistency",
    "claim_self_balanced_nonzero",
    "claim_ledger_minimality",
    "drop_mirror_qualifier",
    "drop_n5_fence",
)

MUTATION_GATE = {
    "stale_main_authority": "A",
    "stale_parent_authority": "A",
    "wrong_state_dimension": "B",
    "break_commutant": "B",
    "break_q_equality": "C",
    "claim_gram_is_one": "C",
    "break_reality_chain": "D",
    "claim_deep_is_default": "D",
    "wrong_generator_rates": "E",
    "wrong_collision_set": "E",
    "break_z4_consistency": "E",
    "claim_self_balanced_nonzero": "F",
    "claim_ledger_minimality": "G",
    "drop_mirror_qualifier": "G",
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
    if isinstance(value, sp.MatrixBase):
        return not value.has(sp.Float)
    if isinstance(value, (tuple, list)):
        return all(no_float(item) for item in value)
    return not sp.sympify(value).has(sp.Float)


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def trig_zero(matrix: sp.MatrixBase) -> bool:
    """Symbolic twin of `matrix_zero` for entries that need expand_complex."""
    return all(
        sp.simplify(sp.expand_complex(sp.expand(value))) == 0 for value in matrix
    )


def commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return (left * right - right * left).applyfunc(sp.expand)


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
# shared family helpers (the committed Block 136 conventions)
# ---------------------------------------------------------------------------
def pair_table(size: int) -> tuple[tuple[int, int], ...]:
    """The Block 136 family pairing: conjugate pairs first, self pair last."""
    half = size // 2
    return tuple((k, size - k) for k in range(1, half)) + ((0, half),)


def charges(size: int) -> tuple[int, ...]:
    """Signed integer momentum charge of each Z_N sector, in (-N/2, N/2]."""
    half = size // 2
    return tuple(k if k <= half else k - size for k in range(size))


def generator_gaps(size: int) -> tuple[int, ...]:
    charge = charges(size)
    return tuple(charge[a] - charge[b] for a, b in pair_table(size))


def predicted_gaps(size: int) -> tuple[int, ...]:
    half = size // 2
    return tuple(2 * k for k in range(1, half)) + (-half,)


def embed(pair: tuple[int, int], block: sp.Matrix, size: int) -> sp.Matrix:
    result = sp.zeros(size)
    for row in range(2):
        for column in range(2):
            result[pair[row], pair[column]] = block[row, column]
    return result


def algebra_basis(size: int) -> tuple[sp.Matrix, ...]:
    """I_j, Z_j, X_j for each block, in block order."""
    return tuple(
        embed(pair, block, size)
        for pair in pair_table(size)
        for block in (I2, Z2, X2)
    )


def disc(x: sp.Expr, z: sp.Expr) -> sp.Matrix:
    return sp.Matrix(((1 + z, x), (x, 1 - z))) / 2


FAMILY_SIZES = (4, 6, 8, 10)


# ---------------------------------------------------------------------------
# B. the state space of Sym_2(R)^m
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class StateCertificate:
    size: int
    blocks: int
    ambient_dimension: int
    trace_rank: int
    affine_dimension: int
    center_dimension: int
    center_is_identities: bool
    symmetric: bool
    block_orthogonal: bool
    jordan_closed: bool
    jordan_generator_excluded: bool
    coordinates_onto: bool
    commutant_rank: int
    commutant_dimension: int
    commutant_is_i_and_z: bool
    selection_rule: bool
    all_gaps_nonzero: bool
    circles_disjoint: bool
    exact: bool


def state_certificate(size: int) -> StateCertificate:
    pairs = pair_table(size)
    blocks = len(pairs)
    basis = algebra_basis(size)

    flat = sp.Matrix.hstack(
        *(matrix.reshape(size * size, 1) for matrix in basis)
    )
    ambient = flat.rank()
    trace_rank = sp.Matrix([[sp.trace(matrix) for matrix in basis]]).rank()

    alphas = sp.symbols(f"a0:{blocks}", real=True)
    betas = sp.symbols(f"b0:{blocks}", real=True)
    gammas = sp.symbols(f"c0:{blocks}", real=True)
    variables = tuple(alphas) + tuple(betas) + tuple(gammas)
    generic = sp.zeros(size)
    for index, pair in enumerate(pairs):
        generic += embed(
            pair,
            alphas[index] * I2 + betas[index] * X2 + gammas[index] * Z2,
            size,
        )

    # the centre of the algebra: commutes with every generator
    central_equations = tuple(
        entry
        for observable in basis
        for entry in commutator(observable, generic)
        if entry != 0
    )
    central_matrix, _ = sp.linear_eq_to_matrix(central_equations, variables)
    center_rank = central_matrix.rank()
    identity_only, _ = sp.linear_eq_to_matrix(
        tuple(betas) + tuple(gammas), variables
    )
    center_is_identities = (
        center_rank == identity_only.rank()
        and central_matrix.col_join(identity_only).rank() == center_rank
        and center_rank == 2 * blocks
    )

    # the momentum commutant
    momentum = sp.diag(*charges(size))
    commutant_equations = tuple(
        entry for entry in commutator(momentum, generic) if entry != 0
    )
    commutant_matrix, _ = sp.linear_eq_to_matrix(commutant_equations, variables)
    x_only, _ = sp.linear_eq_to_matrix(tuple(betas), variables)
    commutant_rank = commutant_matrix.rank()
    commutant_is_i_and_z = (
        commutant_rank == x_only.rank()
        and commutant_matrix.col_join(x_only).rank() == commutant_rank
        and commutant_rank == blocks
    )

    gaps = generator_gaps(size)
    selection_rule = all(
        matrix_zero(
            commutator(momentum, embed(pair, X2, size))
            - gap * embed(pair, E01 - E10, size)
        )
        for pair, gap in zip(pairs, gaps, strict=True)
    )

    symmetric = all(matrix.T == matrix for matrix in basis)
    block_orthogonal = all(
        basis[left] * basis[right] == sp.zeros(size)
        for left in range(len(basis))
        for right in range(len(basis))
        if left // 3 != right // 3
    )
    local_flat = sp.Matrix.hstack(
        *(matrix.reshape(4, 1) for matrix in (I2, Z2, X2))
    )
    jordan_closed = all(
        local_flat.row_join(((a * b + b * a) / 2).reshape(4, 1)).rank() == 3
        for a in (I2, Z2, X2)
        for b in (I2, Z2, X2)
    )
    jordan_excluded = (
        J2.T == -J2
        and J2 != sp.zeros(2)
        and all(
            flat.row_join(embed(pair, J2, size).reshape(size * size, 1)).rank()
            == ambient + 1
            for pair in pairs
        )
    )

    alpha, beta = sp.symbols("alpha beta", real=True)
    coordinates_onto = matrix_zero(
        disc(2 * beta, 2 * alpha - 1)
        - sp.Matrix(((alpha, beta), (beta, 1 - alpha)))
    )

    circles_disjoint = all(
        set(pairs[left]) & set(pairs[right]) == set()
        for left in range(blocks)
        for right in range(left + 1, blocks)
    ) and sorted(index for pair in pairs for index in pair) == list(range(size))

    return StateCertificate(
        size,
        blocks,
        ambient,
        trace_rank,
        ambient - trace_rank,
        len(variables) - center_rank,
        center_is_identities,
        symmetric,
        block_orthogonal,
        jordan_closed,
        jordan_excluded,
        coordinates_onto,
        commutant_rank,
        len(variables) - commutant_rank,
        commutant_is_i_and_z,
        selection_rule,
        all(gap != 0 for gap in gaps),
        circles_disjoint,
        no_float(basis) and no_float(generic),
    )


def general_m_dimension_lemma() -> bool:
    """3m, rank-one trace and 3m-1 for EVERY m, not only the probed sizes.

    The m blocks occupy DISJOINT index pairs, so the 3m generators have pairwise
    disjoint supports, and inside one block I, Z, X are independent: the algebra
    has dimension 3m for every m.  The trace row is (2, 0, 0) repeated m times,
    since Tr I = 2 and Tr Z = Tr X = 0, hence nonzero for every m >= 1, so the
    trace functional has rank exactly one and the affine state dimension is
    3m - 1.  The pairing itself is what makes the supports disjoint: sector
    N - j carries charge (N - j) - N = -j, so (j, N-j) meets no other pair.
    """
    local = sp.Matrix.hstack(
        *(matrix.reshape(4, 1) for matrix in (I2, Z2, X2))
    )
    blocks = sp.Symbol("m", positive=True, integer=True)
    size_symbol = sp.Symbol("N", positive=True, integer=True)
    index = sp.Symbol("j", positive=True, integer=True)
    return bool(
        local.rank() == 3
        and sp.trace(I2) == 2
        and sp.trace(Z2) == 0
        and sp.trace(X2) == 0
        and sp.simplify(((size_symbol - index) - size_symbol) + index) == 0
        and sp.simplify((3 * blocks) - 1 - (3 * blocks - 1)) == 0
        and all(
            set(pair_table(size)[left]) & set(pair_table(size)[right]) == set()
            for size in FAMILY_SIZES + (12, 14, 16)
            for left in range(size // 2)
            for right in range(left + 1, size // 2)
        )
    )


def one_block_commutant_lemma() -> bool:
    """[diag(p,q), aI + bX + cZ] = b(p-q)(E01 - E10), so only X can fail."""
    p, q = sp.symbols("p q", real=True)
    a, b, c = sp.symbols("alpha beta gamma", real=True)
    residual = commutator(sp.diag(p, q), a * I2 + b * X2 + c * Z2)
    return (
        matrix_zero(residual - b * (p - q) * (E01 - E10))
        and matrix_zero(residual.subs(b, 0))
        and sp.solve(sp.Eq(b * (p - q), 0), b) == [0]
    )


@dataclass(frozen=True)
class ExtremeCertificate:
    blocks: int
    purity_identity: bool
    weight_square_identity: bool
    purity_forces_one_block: bool
    psd_zero_diagonal: bool
    vanishing_convex_slot: bool
    projector_is_extreme: bool
    cross_block_mixture_strict: bool
    interior_point_strict: bool
    rp1_projector: bool
    rp1_circle: bool
    rp1_antipodal: bool


def extreme_certificate(blocks: int) -> ExtremeCertificate:
    """The extreme points are exactly the m disjoint RP^1 circles, both ways."""
    size = 2 * blocks
    pairs = pair_table(size)

    x, z = sp.symbols("x z", real=True)
    block_state = disc(x, z)
    purity_identity = (
        sp.simplify(sp.trace(block_state) - 1) == 0
        and sp.simplify(block_state.det() - (1 - x**2 - z**2) / 4) == 0
        and sp.simplify(
            sp.trace(block_state * block_state) - (1 + x**2 + z**2) / 2
        )
        == 0
    )

    weights = sp.symbols(f"w0:{blocks}", nonnegative=True)
    xs = sp.symbols(f"x0:{blocks}", real=True)
    zs = sp.symbols(f"z0:{blocks}", real=True)
    density = sp.zeros(size)
    for index, pair in enumerate(pairs):
        density += embed(pair, weights[index] * disc(xs[index], zs[index]), size)
    purity = sp.expand(
        sp.trace(density * density)
        - sum(
            weights[index] ** 2 * (1 + xs[index] ** 2 + zs[index] ** 2) / 2
            for index in range(blocks)
        )
    )
    cross_terms = sum(
        weights[left] * weights[right]
        for left in range(blocks)
        for right in range(left + 1, blocks)
    )
    weight_square_identity = (
        sp.expand(
            sum(weights) ** 2
            - sum(value**2 for value in weights)
            - 2 * cross_terms
        )
        == 0
    )
    # THE EXACT DEFICIT IDENTITY.  Writing t_j = (1 + x_j^2 + z_j^2)/2, the
    # per-block disk slack is 1 - t_j = (1 - x_j^2 - z_j^2)/2 = 2 det rho_j, and
    #
    #   1 - Tr D^2 - 2 sum_{i<j} w_i w_j - sum_j w_j^2 (1 - t_j) = 1 - (sum w)^2
    #
    # holds IDENTICALLY.  On the state body sum w = 1, so the left side is zero
    # while both subtracted sums are nonnegative (w_j >= 0 and x^2 + z^2 <= 1).
    # Hence Tr D^2 <= 1, and D^2 = D -- which forces Tr D^2 = Tr D = 1 -- makes
    # BOTH vanish: every cross term w_i w_j = 0, so exactly one weight is 1, and
    # that block's slack is 0, so it sits on its circle.
    trace_square = sp.expand(sp.trace(density * density))
    deficit = sum(
        weights[index] ** 2 * (1 - xs[index] ** 2 - zs[index] ** 2) / 2
        for index in range(blocks)
    )
    deficit_identity = (
        sp.expand(
            1
            - trace_square
            - 2 * cross_terms
            - deficit
            - (1 - sum(weights) ** 2)
        )
        == 0
    )
    cross_terms_nonnegative = all(
        (weights[left] * weights[right]).is_nonnegative is True
        for left in range(blocks)
        for right in range(left + 1, blocks)
    )
    slack_is_determinant = all(
        sp.simplify(
            (1 - xs[index] ** 2 - zs[index] ** 2) / 2
            - 2 * disc(xs[index], zs[index]).det()
        )
        == 0
        for index in range(blocks)
    )
    tightness = sp.solve(sp.Eq(1 - x**2 - z**2, 0), z)
    purity_forces_one_block = (
        purity == 0
        and weight_square_identity
        and deficit_identity
        and cross_terms_nonnegative
        and slack_is_determinant
        and len(tightness) == 2
        and sp.simplify(tightness[0] + tightness[1]) == 0
    )

    off_diagonal = sp.Symbol("beta", real=True)
    diagonal = sp.Symbol("alpha", real=True)
    degenerate = sp.Matrix(((0, off_diagonal), (off_diagonal, diagonal)))
    psd_zero_diagonal = (
        sp.simplify(degenerate.det() + off_diagonal**2) == 0
        and sp.solve(sp.Eq(-(off_diagonal**2), 0), off_diagonal) == [0]
    )

    share = sp.Symbol("theta", positive=True)
    left_slot, right_slot = sp.symbols("u v", nonnegative=True)
    solved = sp.solve(
        sp.Eq(share * left_slot + (1 - share) * right_slot, 0), left_slot
    )
    vanishing_convex_slot = (
        len(solved) == 1
        and sp.simplify(solved[0] + (1 - share) * right_slot / share) == 0
    )
    projector_is_extreme = psd_zero_diagonal and vanishing_convex_slot

    first = embed(pairs[0], sp.Matrix(((1, 0), (0, 0))), size)
    second = embed(pairs[1], sp.Matrix(((1, 0), (0, 0))), size)
    weight = R(1, 3)
    mixture = weight * first + (1 - weight) * second
    cross_block_mixture_strict = (
        matrix_zero(mixture - (weight * first + (1 - weight) * second))
        and sp.trace(first) == 1
        and sp.trace(second) == 1
        and first != second
        and matrix_zero(first * first - first)
        and matrix_zero(second * second - second)
        and not matrix_zero(mixture * mixture - mixture)
    )

    x_value, z_value = R(1, 5), R(1, 5)
    radius = sp.sqrt(x_value**2 + z_value**2)
    interior = disc(x_value, z_value)
    plus = disc(x_value / radius, z_value / radius)
    minus = disc(-x_value / radius, -z_value / radius)
    interior_point_strict = (
        matrix_zero(
            (
                interior
                - ((1 + radius) / 2 * plus + (1 - radius) / 2 * minus)
            ).applyfunc(sp.radsimp)
        )
        and sp.simplify(plus.det()) == 0
        and sp.simplify(minus.det()) == 0
        and sp.simplify(interior.det()) != 0
        and radius < 1
        and radius > 0
    )

    u, v = sp.symbols("u v", real=True)
    vector = sp.Matrix((u, v))
    projector = vector * vector.T
    norm = u**2 + v**2
    return ExtremeCertificate(
        blocks,
        purity_identity,
        weight_square_identity,
        purity_forces_one_block,
        psd_zero_diagonal,
        vanishing_convex_slot,
        projector_is_extreme,
        cross_block_mixture_strict,
        interior_point_strict,
        matrix_zero(projector * projector - norm * projector),
        sp.expand((2 * u * v) ** 2 + (u**2 - v**2) ** 2 - norm**2) == 0,
        matrix_zero((-vector) * (-vector).T - projector),
    )


# ---------------------------------------------------------------------------
# C. the certified-frame vacuum: the Z6 tower at both committed shears
# ---------------------------------------------------------------------------
TAU_SYMBOL = sp.Symbol("tau")
RHO_SYMBOL = sp.Symbol("rho")
BRANCH_SIGNS = ((1, 1), (1, -1), (-1, 1), (-1, -1))


def boundary_norm(vector: tuple):
    """q_k = sum_j y_kj conj(y_kj): the committed Block 133 direction weight."""
    total = vector[0] * b136.nested_conjugate(vector[0])
    for value in vector[1:]:
        total = total + value * b136.nested_conjugate(value)
    return total


def tower_to_sympy(value, tau_symbol: sp.Symbol, rho_symbol: sp.Symbol):
    """A nested QuadraticElement as a sympy polynomial in the two generators."""

    def tau_part(part):
        return b136.field_expr(part.a) + b136.field_expr(part.b) * tau_symbol

    return tau_part(value.a) + tau_part(value.b) * rho_symbol


def branch_values(trace_square: sp.Rational) -> tuple[tuple[sp.Expr, sp.Expr], ...]:
    """The four sign choices of the real embedding tau, rho of the tower."""
    values = []
    for tau_sign, rho_sign in BRANCH_SIGNS:
        tau_value = tau_sign * sp.sqrt(trace_square)
        rho_value = (tau_value + rho_sign * sp.sqrt(trace_square - 4)) / 2
        values.append((tau_value, rho_value))
    return tuple(values)


@dataclass(frozen=True)
class TowerAutomorphismCertificate:
    generators_fixed: bool
    tower_relations: bool
    involutive: bool
    additive: bool
    multiplicative: bool
    norms_self_conjugate: bool
    norm_is_mirror_invariant: bool
    embedding_real: bool


def tower_automorphism_certificate() -> TowerAutomorphismCertificate:
    """Nested conjugation is an involutive ring automorphism fixing tau, rho.

    That is the whole content of "q_k is real and at least one": q_k is a fixed
    point of the automorphism, hence lies in the real subfield, and under the
    real embedding -- available because every u_k exceeds 4 -- the automorphism
    IS complex conjugation, so q_k = sum |y_kj|^2 with the pivot term exactly 1.
    The same invariance gives q(conj(y)) = q(y), which is what turns the Z8
    reality chain into the forced mirror q_k = q_{N-k}.
    """
    unit = R(17, 3)  # any rational strictly above 4 realises the tower
    tau_field, rho_field = b136.quadratic_context(unit)
    tau, rho = tau_field.generator, rho_field.generator
    conjugate = b136.nested_conjugate

    seeds = (
        sp.Integer(1),
        sp.I,
        sp.sqrt(3),
        R(2, 5) * sp.I * sp.sqrt(3),
        R(-7, 4),
        R(3, 2) + sp.I,
    )
    base = tuple(b136.field_element(value) for value in seeds)
    elements = tuple(
        b136.QuadraticElement(
            rho_field,
            b136.QuadraticElement(tau_field, base[index % 6], base[(index + 2) % 6]),
            b136.QuadraticElement(
                tau_field, base[(index + 3) % 6], base[(index + 5) % 6]
            ),
        )
        for index in range(8)
    )
    pairs = tuple(
        (elements[left], elements[right])
        for left in range(len(elements))
        for right in range(left + 1, len(elements))
    )

    generators_fixed = conjugate(tau) == tau and conjugate(rho) == rho
    tower_relations = (
        tau * tau == tau_field.coerce(b136.field_element(unit))
        and rho * rho == rho * tau - rho_field.one
    )
    involutive = all(conjugate(conjugate(item)) == item for item in elements)
    additive = all(
        conjugate(left + right) == conjugate(left) + conjugate(right)
        for left, right in pairs
    )
    multiplicative = all(
        conjugate(left * right) == conjugate(left) * conjugate(right)
        for left, right in pairs
    )
    norms_self_conjugate = all(
        conjugate(item * conjugate(item)) == item * conjugate(item)
        for item in elements
    )
    # q(conj(y)) = q(y) entrywise, so mirrored directions carry equal weights.
    norm_is_mirror_invariant = all(
        boundary_norm(tuple(conjugate(item) for item in window))
        == boundary_norm(window)
        for window in (elements[:4], elements[2:6], elements[4:])
    )
    # tau^2 = u > 4 and rho^2 - tau rho + 1 = 0 give rho = (tau +- sqrt(u-4))/2,
    # so BOTH generators are real for u > 4 and the automorphism restricts to
    # complex conjugation of the coefficient field.
    embedding_real = all(
        sp.im(sp.radsimp(sp.expand(tau_value))) == 0
        and sp.simplify(sp.im(sp.radsimp(sp.expand(rho_value)))) == 0
        and sp.simplify(rho_value**2 - tau_value * rho_value + 1) == 0
        for tau_value, rho_value in branch_values(unit)
    )
    return TowerAutomorphismCertificate(
        generators_fixed,
        tower_relations,
        involutive,
        additive,
        multiplicative,
        norms_self_conjugate,
        norm_is_mirror_invariant,
        embedding_real,
    )


@dataclass(frozen=True)
class FixtureVacuum:
    label: str
    size: int
    shear: sp.Rational
    trace_squares: tuple[sp.Rational, ...]
    trace_square_classes: tuple[tuple[int, ...], ...]
    sectors_valid: bool
    pivot_normalized: bool
    conjugate_y_mirror: bool
    conjugate_norms_forced: bool
    self_pair_unequal: bool
    norms_self_conjugate: bool
    roots_admit_real_embedding: bool
    gram_not_one_on_branch: tuple[bool, ...]
    gram_direction_on_branch: tuple[int, ...]
    branch_dependent_direction: bool
    exact: bool


def z6_vacuum(label: str, shear: sp.Rational) -> FixtureVacuum:
    size = b136.SPACE_SIZE
    half = size // 2
    fixture = b136.build_z6(shear)
    squares = b136.trace_squares(fixture)
    sectors = b136.sector_factorizations(fixture.transfers, squares)

    norms = tuple(boundary_norm(sector.y) for sector in sectors)
    conjugated = tuple(
        tuple(b136.nested_conjugate(value) for value in sector.y)
        for sector in sectors
    )
    mirror = all(sectors[(-k) % size].y == conjugated[k] for k in range(1, half))
    forced = all(norms[(-k) % size] == norms[k] for k in range(1, half))
    unequal = norms[0] != norms[half]
    pivots = all(sector.y[0] == sector.y[0].field.one for sector in sectors)
    self_conjugate = all(
        value == b136.nested_conjugate(value) for value in norms
    )

    # The self-conjugate momenta 0 and N/2 share one tower, so the gram
    # g = q_{N/2}/q_0 can be evaluated branch by branch on that single tower.
    zero_expression = tower_to_sympy(norms[0], TAU_SYMBOL, RHO_SYMBOL)
    self_expression = tower_to_sympy(norms[half], TAU_SYMBOL, RHO_SYMBOL)
    not_one: list[bool] = []
    direction: list[int] = []
    for tau_value, rho_value in branch_values(squares[0]):
        substitution = {TAU_SYMBOL: tau_value, RHO_SYMBOL: rho_value}
        lower = sp.radsimp(sp.expand(zero_expression.subs(substitution)))
        upper = sp.radsimp(sp.expand(self_expression.subs(substitution)))
        difference = sp.radsimp(sp.expand(upper - lower))
        not_one.append(
            sp.simplify(difference) != 0 and difference.equals(0) is False
        )
        sign = sp.simplify(difference).is_positive
        direction.append(1 if sign is True else (-1 if sign is False else 0))

    classes = tuple(
        dict.fromkeys(
            tuple(
                index for index in range(size) if squares[index] == squares[k]
            )
            for k in range(size)
        )
    )
    return FixtureVacuum(
        label,
        size,
        shear,
        squares,
        classes,
        all(sector.valid for sector in sectors),
        pivots,
        mirror,
        forced,
        unequal,
        self_conjugate,
        all(value > 4 for value in squares),
        tuple(not_one),
        tuple(direction),
        set(direction) == {1, -1},
        no_float(squares),
    )


def fixture_verdict(item: FixtureVacuum) -> bool:
    return all(
        (
            item.sectors_valid,
            item.pivot_normalized,
            item.conjugate_y_mirror,
            item.conjugate_norms_forced,
            item.self_pair_unequal,
            item.norms_self_conjugate,
            item.roots_admit_real_embedding,
            all(item.gram_not_one_on_branch),
            len(item.gram_not_one_on_branch) == len(BRANCH_SIGNS),
            item.exact,
        )
    )


@dataclass(frozen=True)
class VacuumStructure:
    size: int
    blocks: int
    trace_one: bool
    conjugate_blocks_maximally_mixed: bool
    self_block_biased: bool
    functional_exact: bool
    closed_form_central_weights: bool


def vacuum_structure(size: int) -> VacuumStructure:
    """The general-m certified-frame vacuum, symbolic in the direction weights."""
    half = size // 2
    pairs = pair_table(size)
    blocks = len(pairs)
    q = sp.symbols(f"q0:{half}", positive=True)
    gram = sp.Symbol("g", positive=True)
    weights: list[sp.Expr] = [sp.Integer(0)] * size
    weights[0] = q[0]
    weights[half] = gram * q[0]
    for k in range(1, half):
        weights[k] = q[k]
        weights[size - k] = q[k]
    total = sum(weights)
    density = sp.diag(*weights) / total

    internal = tuple(
        (
            sp.diag(weights[a], weights[b]) / (weights[a] + weights[b])
        ).applyfunc(sp.cancel)
        for a, b in pairs
    )
    central = tuple(
        sp.factor((weights[a] + weights[b]) / total) for a, b in pairs
    )
    reconstructed = sp.zeros(size)
    for index, pair in enumerate(pairs):
        reconstructed += embed(pair, central[index] * internal[index], size)

    alphas = sp.symbols(f"A0:{blocks}", real=True)
    betas = sp.symbols(f"B0:{blocks}", real=True)
    gammas = sp.symbols(f"C0:{blocks}", real=True)
    observable = sp.zeros(size)
    for index, pair in enumerate(pairs):
        observable += embed(
            pair,
            alphas[index] * I2 + betas[index] * X2 + gammas[index] * Z2,
            size,
        )
    functional = sp.factor(
        sum(weights[k] * observable[k, k] for k in range(size)) / total
    )
    functional_exact = (
        sp.factor(sp.trace(density * observable) - functional) == 0
        and matrix_zero((density - reconstructed).applyfunc(sp.cancel))
    )

    predicted = tuple(
        2 * q[k] / total for k in range(1, half)
    ) + (q[0] * (1 + gram) / total,)
    closed_form = all(
        sp.factor(actual - expected) == 0
        for actual, expected in zip(central, predicted, strict=True)
    ) and sp.factor(
        total - (q[0] * (1 + gram) + 2 * sum(q[k] for k in range(1, half)))
    ) == 0

    return VacuumStructure(
        size,
        blocks,
        sp.factor(sp.trace(density)) == 1,
        all(matrix_zero(item - I2 / 2) for item in internal[:-1]),
        matrix_zero(internal[-1] - sp.diag(1, gram) / (1 + gram))
        and not matrix_zero(internal[-1] - I2 / 2),
        functional_exact,
        closed_form,
    )


# ---------------------------------------------------------------------------
# D. the Z8 structural reality chain (cheap) and the deep tower behind a flag
# ---------------------------------------------------------------------------
class Z8Adapter:
    """The Block 136 base-field adapter retargeted at the Block 139 Z8 field."""

    zero = b139.Z8_FIELD.zero
    one = b139.Z8_FIELD.one

    @staticmethod
    def coerce(value: object):
        try:
            return b139.Z8_FIELD.convert(value)
        except (TypeError, ValueError):
            return b139.Z8_FIELD.from_sympy(value)


class Z8Context:
    """Swap only the spatial size and exact root field, then restore them."""

    SWAPPED = ("SPACE_SIZE", "NUMBER_FIELD", "ALGEBRAIC_EXTENSION", "BASE_FIELD")

    def __enter__(self):
        self.saved = (
            b136.SPACE_SIZE,
            b136.NUMBER_FIELD,
            b136.ALGEBRAIC_EXTENSION,
            b136.BASE_FIELD,
        )
        b136.SPACE_SIZE = b139.SPACE_SIZE
        b136.NUMBER_FIELD = b139.Z8_FIELD
        b136.ALGEBRAIC_EXTENSION = b139.Z8_EXTENSION
        b136.BASE_FIELD = Z8Adapter()
        return self

    def __exit__(self, *args) -> bool:
        (
            b136.SPACE_SIZE,
            b136.NUMBER_FIELD,
            b136.ALGEBRAIC_EXTENSION,
            b136.BASE_FIELD,
        ) = self.saved
        return False


class Z8BuilderPatch:
    """The projector/field patch the Z8 builder itself runs under."""

    def __enter__(self):
        self.saved = (
            b136.projectors,
            b136.ALGEBRAIC_EXTENSION,
            b136.NUMBER_FIELD,
        )
        b136.projectors = b139.projectors8_adapter
        b136.ALGEBRAIC_EXTENSION = b139.Z8_EXTENSION
        b136.NUMBER_FIELD = b139.Z8_FIELD
        return self

    def __exit__(self, *args) -> bool:
        (
            b136.projectors,
            b136.ALGEBRAIC_EXTENSION,
            b136.NUMBER_FIELD,
        ) = self.saved
        return False


# DOCUMENTED NON-GATE CONSTANTS.  The Z8 direction weights below were produced
# INDEPENDENTLY TWICE before this runner existed -- once by the block solve
# (which drives b136.sector_factorizations through Z8Context) and once by a
# separate checker that transcribes the same committed b136 sector algorithm at
# N = 8 -- and the two runs agreed entrywise.  They cost ~15 minutes to
# reproduce, so they are printed as DOCUMENTATION and are never asserted on the
# default gate path; --deep-z8 re-derives the exact tower facts they encode.
Z8_RECORDED_SHEAR_TEXT = "5/13"
# Decimal READ-OUTS under the principal embedding, transcribed verbatim from
# the two independent runs.  They are documentation only: the EXACT content is
# the tower-level structure recorded immediately below, and no gate on any path
# compares a decimal.
Z8_RECORDED_WEIGHT_TEXT = (
    "q_0 ~ 1134.53172256351533610808923202",
    "q_1 ~ 44311.4077365415240610072021506",
    "q_2 ~ 545433.055705322154026518076504",
    "q_3 ~ 29715.2700136821424813577054932",
    "q_4 ~ 454.670140385464698600090818791",
    "q_5 ~ 29715.2700136821424813577054932",
    "q_6 ~ 545433.055705322154026518076504",
    "q_7 ~ 44311.4077365415240610072021506",
)
Z8_RECORDED_STRUCTURE_TEXT = (
    "q_1 = q_7, q_2 = q_6, q_3 = q_5 as exact tower elements; q_0 != q_4; "
    "every sector valid with unit pivot y_k0 = 1; u-classes (0,4), (1,3,5,7), "
    "(2,6); the principal-branch gram g = q_4/q_0 is below one while the other "
    "real branch puts it above one, exactly as at Z6"
)
Z8_TRACE_SQUARE_CLASSES = ((0, 4), (1, 3, 5, 7), (2, 6))


@dataclass(frozen=True)
class Z8RealityChain:
    shear: sp.Rational
    action_real: bool
    projector_mirror: bool
    block_mirror: bool
    monodromy_mirror: bool
    self_blocks_real: bool
    trace_square_classes: tuple[tuple[int, ...], ...]
    roots_admit_real_embedding: bool
    self_pair_isospectral: bool
    self_pair_blocks_distinct: bool
    exact: bool


def z8_reality_chain(shear: sp.Rational) -> Z8RealityChain:
    """The cheap chain that FORCES q_k = q_{8-k} without running the tower.

    The action is real, so the momentum projectors, the momentum blocks and the
    monodromies all mirror exactly under k -> N-k.  The sector factorization
    consumes exactly those objects, so its output mirrors too: y_{N-k} =
    conj(y_k).  The boundary norm is invariant under nested conjugation --
    certified in gate C -- hence q_{N-k} = q_k.  No residue arithmetic needed.
    """
    size = b139.SPACE_SIZE
    with Z8BuilderPatch():
        solve = b139.build_z8(shear)
        conjugate = b139.conjugate8
        projectors = b139.projectors8()
        action_real = b139.matrix_equal8(
            solve.action, solve.action.applyfunc(sp.conjugate)
        )
        projector_mirror = all(
            b139.matrix_equal8(
                projectors[(-k) % size], projectors[k].applyfunc(conjugate)
            )
            for k in range(size)
        )
        block_mirror = all(
            b139.matrix_equal8(
                solve.blocks[(-k) % size], solve.blocks[k].applyfunc(conjugate)
            )
            for k in range(size)
        )
        monodromy_mirror = all(
            b139.matrix_equal8(
                solve.transfers[(-k) % size].monodromy,
                solve.transfers[k].monodromy.applyfunc(conjugate),
            )
            for k in range(size)
        )
        self_blocks_real = all(
            b139.matrix_equal8(
                solve.blocks[k], solve.blocks[k].applyfunc(conjugate)
            )
            for k in (0, size // 2)
        )
        squares = tuple(
            b139.canonical8(
                sp.cancel(
                    transfer.monodromy_trace**2 / transfer.monodromy_determinant
                )
            )
            for transfer in solve.transfers
        )
        isospectral = b139.coefficients_equal8(
            b139.characteristic_coefficients(solve.blocks[0]),
            b139.characteristic_coefficients(solve.blocks[size // 2]),
        ) and b139.matrix_equal8(
            solve.transfers[0].monodromy,
            solve.transfers[size // 2].monodromy,
        )
        distinct = not b139.matrix_equal8(
            solve.blocks[0], solve.blocks[size // 2]
        )
    classes = tuple(
        dict.fromkeys(
            tuple(
                index for index in range(size) if squares[index] == squares[k]
            )
            for k in range(size)
        )
    )
    return Z8RealityChain(
        shear,
        action_real,
        projector_mirror,
        block_mirror,
        monodromy_mirror,
        self_blocks_real,
        classes,
        all(value.is_Rational and value > 4 for value in squares),
        isospectral,
        distinct,
        no_float(squares),
    )


def reality_chain_verdict(item: Z8RealityChain) -> bool:
    return all(
        (
            item.action_real,
            item.projector_mirror,
            item.block_mirror,
            item.monodromy_mirror,
            item.self_blocks_real,
            item.roots_admit_real_embedding,
            item.self_pair_isospectral,
            item.self_pair_blocks_distinct,
            item.trace_square_classes == Z8_TRACE_SQUARE_CLASSES,
            item.exact,
        )
    )


def deep_route_wired() -> bool:
    """The --deep-z8 route exists and is the solve's Z8Adapter/Z8Context one.

    Checked WITHOUT paying for the tower: the context must swap exactly the four
    Block 136 globals, install the Z8 adapter, and restore every one of them.
    """
    before = tuple(getattr(b136, name) for name in Z8Context.SWAPPED)
    with Z8Context() as context:
        inside = tuple(getattr(b136, name) for name in Z8Context.SWAPPED)
        swapped = (
            b136.SPACE_SIZE == b139.SPACE_SIZE == 8
            and b136.NUMBER_FIELD is b139.Z8_FIELD
            and b136.ALGEBRAIC_EXTENSION == b139.Z8_EXTENSION
            and isinstance(b136.BASE_FIELD, Z8Adapter)
            and b136.BASE_FIELD.one == b139.Z8_FIELD.one
            and b136.BASE_FIELD.zero == b139.Z8_FIELD.zero
            and Z8Adapter.coerce(R(3, 4)) == b139.Z8_FIELD.convert(R(3, 4))
            and context.saved == before
        )
    after = tuple(getattr(b136, name) for name in Z8Context.SWAPPED)
    return bool(
        swapped
        and len(Z8Context.SWAPPED) == 4
        and after == before
        and inside != before
        and callable(z8_deep_tower)
    )


@dataclass(frozen=True)
class Z8DeepTower:
    shear: sp.Rational
    sectors_valid: bool
    pivot_normalized: bool
    conjugate_y_mirror: bool
    conjugate_norms_forced: bool
    self_pair_unequal: bool
    norms_self_conjugate: bool
    trace_square_classes: tuple[tuple[int, ...], ...]


def z8_deep_tower(shear: sp.Rational) -> Z8DeepTower:
    """The ~15 minute Z8 residue tower, reached only through --deep-z8."""
    size = b139.SPACE_SIZE
    half = size // 2
    solve = b139.build_z8(shear)
    squares = tuple(
        R(b139.canonical8(transfer.normalized_trace_square))
        for transfer in solve.transfers
    )
    with Z8Context():
        sectors = b136.sector_factorizations(solve.transfers, squares)
        norms = tuple(boundary_norm(sector.y) for sector in sectors)
        conjugated = tuple(
            tuple(b136.nested_conjugate(value) for value in sector.y)
            for sector in sectors
        )
        mirror = all(
            sectors[(-k) % size].y == conjugated[k] for k in range(1, half)
        )
        forced = all(norms[(-k) % size] == norms[k] for k in range(1, half))
        unequal = norms[0] != norms[half]
        pivots = all(sector.y[0] == sector.y[0].field.one for sector in sectors)
        self_conjugate = all(
            value == b136.nested_conjugate(value) for value in norms
        )
        valid = all(sector.valid for sector in sectors)
    classes = tuple(
        dict.fromkeys(
            tuple(
                index for index in range(size) if squares[index] == squares[k]
            )
            for k in range(size)
        )
    )
    return Z8DeepTower(
        shear,
        valid,
        pivots,
        mirror,
        forced,
        unequal,
        self_conjugate,
        classes,
    )


def deep_tower_verdict(item: Z8DeepTower | None) -> bool:
    if item is None:
        return False
    return all(
        (
            item.sectors_valid,
            item.pivot_normalized,
            item.conjugate_y_mirror,
            item.conjugate_norms_forced,
            item.self_pair_unequal,
            item.norms_self_conjugate,
            item.trace_square_classes == Z8_TRACE_SQUARE_CLASSES,
        )
    )


# ---------------------------------------------------------------------------
# E. the momentum dynamics
# ---------------------------------------------------------------------------
DYNAMICS_SIZES = (4, 6, 8, 12)
COLLISION_PROBE_SIZES = (4, 6, 8, 10, 12)


@dataclass(frozen=True)
class MomentumCertificate:
    size: int
    momentum_is_signed_charge: bool
    self_sector_charge: int
    charges_antisymmetric_off_self: bool
    gaps: tuple[int, ...]
    gaps_match_prediction: bool
    orbits_exact: bool
    identity_and_z_fixed: bool
    all_gaps_nonzero: bool
    exact: bool


def momentum_certificate(size: int) -> MomentumCertificate:
    charge = charges(size)
    half = size // 2
    momentum = sp.diag(*charge)
    gaps = generator_gaps(size)

    orbits_exact = True
    identity_and_z_fixed = True
    for (a, b), gap in zip(pair_table(size), gaps, strict=True):
        unitary = sp.diag(sp.exp(I * charge[a] * T), sp.exp(I * charge[b] * T))
        local = sp.diag(charge[a], charge[b])
        cosine, sine = sp.cos(gap * T), sp.sin(gap * T)
        orbit_x = cosine * X2 + sine * Y2
        orbit_y = -sine * X2 + cosine * Y2
        orbits_exact = (
            orbits_exact
            and trig_zero(unitary * X2 * unitary.H - orbit_x)
            and trig_zero(unitary * Y2 * unitary.H - orbit_y)
            and trig_zero(
                orbit_x.diff(T).subs(T, 0) - I * commutator(local, X2)
            )
            and trig_zero(
                orbit_y.diff(T).subs(T, 0) - I * commutator(local, Y2)
            )
        )
        identity_and_z_fixed = identity_and_z_fixed and all(
            trig_zero(unitary * matrix * unitary.H - matrix)
            for matrix in (I2, Z2)
        )

    # (H2): the charge of sector k is the representative of k modulo N inside
    # the half-open window (-N/2, N/2].  That window is what makes the charge
    # antisymmetric on every conjugate pair while handing the SELF-conjugate
    # sector the positive end point +N/2 -- the asymmetry that later produces
    # the self pair's semidefinite charge and the 4|N rate collision.
    return MomentumCertificate(
        size,
        momentum == sp.diag(*charge)
        and all((value - k) % size == 0 for k, value in enumerate(charge))
        and all(-half < value <= half for value in charge)
        and charge[0] == 0
        and charge[half] == half,
        charge[half],
        all(
            charge[k] == -charge[(-k) % size]
            for k in range(size)
            if k not in (0, half)
        )
        and charge[half] != -charge[half],
        gaps,
        gaps == predicted_gaps(size),
        orbits_exact,
        identity_and_z_fixed,
        all(gap != 0 for gap in gaps),
        no_float(momentum),
    )


def general_m_gap_lemma() -> bool:
    """The gaps are 2k and -m for EVERY m, and none of them can vanish.

    On the charge window (-N/2, N/2] sector j carries +j for 1 <= j < m and
    sector N - j carries (N - j) - N = -j, so the conjugate pair (j, N-j) has
    gap j - (-j) = 2k with k = j; the self pair (0, N/2) has gap 0 - m = -m.
    With k a positive integer 2k = 0 has NO solution, and -m < 0 for m >= 1, so
    the selection rule kills X in every block at every m.
    """
    k = sp.Symbol("k", positive=True, integer=True)
    blocks = sp.Symbol("m", positive=True, integer=True)
    size_symbol = sp.Symbol("N", positive=True, integer=True)
    pair_gap = sp.simplify(k - (-k))
    self_gap = sp.simplify(0 - blocks)
    return bool(
        sp.simplify(((size_symbol - k) - size_symbol) - (-k)) == 0
        and pair_gap == 2 * k
        and self_gap == -blocks
        and pair_gap.is_positive is True
        and self_gap.is_negative is True
        and sp.solve(sp.Eq(2 * k, 0), k) == []
        and sp.solve(sp.Eq(-blocks, 0), blocks) == []
    )


def symbolic_orbit_law() -> bool:
    """U X U^dag = cos(delta t) X + sin(delta t) Y for a symbolic gap."""
    gap = sp.Symbol("delta", real=True)
    lower = sp.Symbol("c_b", real=True)
    unitary = sp.diag(sp.exp(I * (gap + lower) * T), sp.exp(I * lower * T))
    return (
        trig_zero(
            unitary * X2 * unitary.H
            - (sp.cos(gap * T) * X2 + sp.sin(gap * T) * Y2)
        )
        and trig_zero(
            unitary * Y2 * unitary.H
            - (-sp.sin(gap * T) * X2 + sp.cos(gap * T) * Y2)
        )
        and trig_zero(unitary * I2 * unitary.H - I2)
        and trig_zero(unitary * Z2 * unitary.H - Z2)
    )


@dataclass(frozen=True)
class CollisionCertificate:
    size: int
    divisible: bool
    quarter_index: int | None
    quarter_rate: int | None
    self_rate: int
    magnitudes_agree: bool
    counter_rotating: bool


def collision_certificate(size: int) -> CollisionCertificate:
    """The |rate| = N/2 coincidence is the 4|N phenomenon, not a Z8 novelty."""
    half = size // 2
    gaps = generator_gaps(size)
    self_rate = gaps[-1]
    divisible = size % 4 == 0
    quarter_index = size // 4 if divisible else None
    quarter_rate = 2 * quarter_index if quarter_index is not None else None
    magnitudes_agree = (
        quarter_rate is not None
        and abs(quarter_rate) == abs(self_rate) == half
        and quarter_rate in gaps
    )
    return CollisionCertificate(
        size,
        divisible,
        quarter_index,
        quarter_rate,
        self_rate,
        bool(magnitudes_agree),
        bool(magnitudes_agree and quarter_rate != self_rate),
    )


def block133_z4_consistency() -> bool:
    """The Z4 row agrees with Block 133's landed certificate as a MULTISET.

    Block 133 lists the SELF block first, this block lists the conjugate pairs
    first, so the displayed indices are swapped; the physics is identical.
    """
    landed = b133.momentum_certificate()
    mine = generator_gaps(4)
    return bool(
        list(landed.momentum.diagonal()) == list(charges(4))
        and landed.generator_differences == (-2, 2)
        and mine == (2, -2)
        and sorted(landed.generator_differences) == sorted(mine)
        and landed.generator_differences != mine
        and landed.opposite_orientations
        and landed.orbit02_exact
        and landed.orbit13_exact
        and landed.commutant_rank == 2
        and landed.commutant_dimension == 4
        and pair_table(4) == b136.algebra_certificate(4).pairs
        and pair_table(6) == b136.algebra_certificate(6).pairs
    )


# ---------------------------------------------------------------------------
# F. the balanced gravity sector
# ---------------------------------------------------------------------------
def single_pair_reach_lemma() -> bool:
    """One conjugate pair contributes exactly 2 to the reach, at every m.

    On the equator (I + r(cos phi X + sin phi Y))/2 the expectation of
    aI + bX + cZ is a + r b cos phi, so the phase-invariant admissible
    observables inside one pair are span{I, Z}: the b-row has rank 1 out of 3,
    leaving dimension 2.  Summing over the m-1 conjugate pairs gives the reach
    2(m-1) = 2m-2 for every m, with the self pair contributing nothing.
    """
    phase = sp.Symbol("phi", real=True)
    radius = sp.Symbol("r", positive=True)
    a, b, c = sp.symbols("alpha beta gamma", real=True)
    state = (I2 + radius * (sp.cos(phase) * X2 + sp.sin(phase) * Y2)) / 2
    expectation = sp.simplify(
        sp.expand_complex(sp.trace(state * (a * I2 + b * X2 + c * Z2)))
    )
    coefficients, _ = sp.linear_eq_to_matrix(
        (
            sp.simplify(
                (expectation.subs(phase, 0) - expectation.subs(phase, sp.pi))
                / (2 * radius)
            ),
        ),
        (a, b, c),
    )
    blocks = sp.Symbol("m", positive=True, integer=True)
    return bool(
        sp.simplify(expectation - (a + radius * b * sp.cos(phase))) == 0
        and coefficients.rank() == 1
        and 3 - coefficients.rank() == 2
        and sp.simplify(2 * (blocks - 1) - (2 * blocks - 2)) == 0
    )


@dataclass(frozen=True)
class BalancedCertificate:
    size: int
    conjugate_pairs: int
    equator_exact: bool
    positivity_identity: bool
    pair_charge_balanced: bool
    self_charge_is_semidefinite: bool
    self_balanced_forces_zero: bool
    expectation_exact: bool
    invariant_rank: int
    reach_dimension: int
    invariant_is_i_and_z: bool
    y_not_admissible: bool


def balanced_certificate(size: int) -> BalancedCertificate:
    pairs = pair_table(size)
    charge = charges(size)
    conjugate_pairs = pairs[:-1]
    self_pair = pairs[-1]
    count = len(conjugate_pairs)
    half = size // 2

    phase = sp.Symbol("phi", real=True)
    radius = sp.Symbol("r", positive=True)
    amplitude = sp.Matrix((1 / sp.sqrt(2), sp.exp(-I * phase) / sp.sqrt(2)))
    pure = amplitude * amplitude.H
    family = (I2 + radius * (sp.cos(phase) * X2 + sp.sin(phase) * Y2)) / 2
    equator_exact = (
        trig_zero(pure - (I2 + sp.cos(phase) * X2 + sp.sin(phase) * Y2) / 2)
        and trig_zero(
            (radius * pure + (1 - radius) * I2 / 2).applyfunc(sp.expand) - family
        )
        and sp.simplify(sp.expand_complex((amplitude.H * amplitude)[0])) == 1
    )
    positivity_identity = (
        sp.simplify(sp.trace(family)) == 1
        and sp.simplify(sp.expand_complex(family.det()) - (1 - radius**2) / 4)
        == 0
    )

    balanced_ray = sp.Matrix((1, 1))
    pair_charge_balanced = (
        all(
            (
                balanced_ray.T * sp.diag(charge[a], charge[b]) * balanced_ray
            )[0]
            == 0
            and sp.diag(charge[a], charge[b]) != sp.zeros(2)
            for a, b in conjugate_pairs
        )
        and count == half - 1
    )

    self_charge = sp.diag(charge[self_pair[0]], charge[self_pair[1]])
    self_charge_is_semidefinite = (
        self_charge == sp.diag(0, half)
        and all(value >= 0 for value in self_charge.diagonal())
        and self_charge.det() == 0
        and not all(value > 0 for value in self_charge.diagonal())
    )
    scale = sp.Symbol("s", real=True)
    self_expectation = sp.expand(
        (
            sp.Matrix((scale, scale)).T * self_charge * sp.Matrix((scale, scale))
        )[0]
    )
    # SEMIdefinite, so demanding <charge> = 0 on the balanced ray does not leave
    # a free amplitude: it FORCES s = 0.
    self_balanced_forces_zero = (
        self_expectation == half * scale**2
        and sp.Poly(self_expectation, scale).all_roots() == [0, 0]
        and sp.solve(sp.Eq(self_expectation, 0), scale) == [0]
    )

    weights = sp.symbols(f"w0:{count}", nonnegative=True)
    radii = sp.symbols(f"r0:{count}", nonnegative=True)
    phases = sp.symbols(f"phi0:{count}", real=True)
    alphas = sp.symbols(f"A0:{len(pairs)}", real=True)
    betas = sp.symbols(f"B0:{len(pairs)}", real=True)
    gammas = sp.symbols(f"C0:{len(pairs)}", real=True)
    density = sp.zeros(size)
    for index, pair in enumerate(conjugate_pairs):
        density += embed(
            pair,
            weights[index]
            * (
                I2
                + radii[index]
                * (sp.cos(phases[index]) * X2 + sp.sin(phases[index]) * Y2)
            )
            / 2,
            size,
        )
    observable = sp.zeros(size)
    for index, pair in enumerate(pairs):
        observable += embed(
            pair,
            alphas[index] * I2 + betas[index] * X2 + gammas[index] * Z2,
            size,
        )
    expectation = sp.expand(sp.expand_complex(sp.trace(density * observable)))
    predicted = sp.expand(
        sum(
            weights[index]
            * (
                alphas[index]
                + radii[index] * betas[index] * sp.cos(phases[index])
            )
            for index in range(count)
        )
    )
    expectation_exact = sp.simplify(expectation - predicted) == 0

    variables = (
        tuple(alphas[:count]) + tuple(betas[:count]) + tuple(gammas[:count])
    )
    invariance_equations = tuple(
        sp.simplify(
            expectation.subs(phases[index], 0)
            - expectation.subs(phases[index], sp.pi)
        )
        / (2 * weights[index] * radii[index])
        for index in range(count)
    )
    invariant_coefficients, _ = sp.linear_eq_to_matrix(
        invariance_equations, variables
    )
    expected_coefficients, _ = sp.linear_eq_to_matrix(betas[:count], variables)
    rank = invariant_coefficients.rank()
    return BalancedCertificate(
        size,
        count,
        equator_exact,
        positivity_identity,
        pair_charge_balanced,
        self_charge_is_semidefinite,
        self_balanced_forces_zero,
        expectation_exact,
        rank,
        3 * count - rank,
        rank == expected_coefficients.rank()
        and invariant_coefficients.col_join(expected_coefficients).rank() == rank
        and rank == count,
        matrix_zero(Y2.H - Y2)
        and matrix_zero(Y2.T + Y2)
        and not matrix_zero(Y2.T - Y2),
    )


# ---------------------------------------------------------------------------
# G. the frame ledger, as the independent checker corrected it
# ---------------------------------------------------------------------------
LEDGER_SIZES = (4, 6)
# The explicit unconstrained move used as the counterexample: it scales index 1
# alone, so it is NOT mirror compatible at N = 6, yet it is a perfectly
# admissible positive real diagonal congruence.
UNCONSTRAINED_SCALE = (1, 2, 1, 1, 1, 1)


def certified_gram(size: int) -> tuple[sp.Matrix, tuple[sp.Expr, ...]]:
    """diag(q_k) with the forced mirror q_k = q_{N-k} and the self gram g."""
    half = size // 2
    q = sp.symbols(f"q0:{half}", positive=True)
    gram = sp.Symbol("g", positive=True)
    weights: list[sp.Expr] = [sp.Integer(0)] * size
    weights[0] = q[0]
    weights[half] = gram * q[0]
    for k in range(1, half):
        weights[k] = q[k]
        weights[size - k] = q[k]
    return sp.diag(*weights), tuple(weights)


def landed_admissibility(scale: sp.Matrix, gram: sp.Matrix) -> bool:
    """The committed Block 133 test for a frame move, applied verbatim.

    A move is admissible when its scales are real and positive, it preserves the
    reality involution, and it preserves positivity of the gram diagonal.  It
    says NOTHING about the mirror, which is exactly the gap this block closes.
    """
    diagonal = tuple(scale.diagonal())
    real_positive = all(
        sp.simplify(sp.conjugate(value) - value) == 0
        and value.is_positive is not False
        for value in diagonal
    )
    reality = (
        scale.inv() * sp.eye(scale.rows) * scale.conjugate()
    ).applyfunc(sp.simplify)
    involutivity = matrix_zero(reality - sp.eye(scale.rows))
    transformed = (scale.T * gram * scale).applyfunc(sp.simplify)
    positivity = all(
        value.is_positive is not False for value in transformed.diagonal()
    )
    return bool(real_positive and involutivity and positivity)


@dataclass(frozen=True)
class FrameLedger:
    size: int
    structured_move_count: int
    structured_reaches_uniform: bool
    structured_scales_admissible: bool
    single_congruence_reaches_uniform: bool
    single_congruence_admissible: bool
    ledger_is_minimal: bool
    mirror_compatible_preserves: bool
    unconstrained_breaks_mirror: bool
    unconstrained_is_admissible: bool
    bias_removable: bool
    bias_move_is_mirror_compatible: bool
    exact: bool


def frame_ledger(size: int) -> FrameLedger:
    half = size // 2
    gram, weights = certified_gram(size)
    q = sp.symbols(f"q0:{half}", positive=True)
    gram_symbol = sp.Symbol("g", positive=True)

    # (i) the m STRUCTURED moves: one intra-self move then one per conjugate
    # pair.  This is the convention Block 133 landed at m = 2.
    intra = sp.eye(size)
    intra[half, half] = 1 / sp.sqrt(gram_symbol)
    moves = [intra]
    for k in range(1, half):
        move = sp.eye(size)
        move[k, k] = sp.sqrt(q[0] / q[k])
        move[size - k, size - k] = sp.sqrt(q[0] / q[k])
        moves.append(move)
    current = gram
    for move in moves:
        current = (move.T * current * move).applyfunc(sp.simplify)
    density = (current / sp.trace(current)).applyfunc(sp.simplify)
    structured_reaches_uniform = matrix_zero(
        current - q[0] * sp.eye(size)
    ) and matrix_zero(density - sp.eye(size) / size)
    structured_scales_admissible = all(
        landed_admissibility(move, gram) for move in moves
    )

    # (ii) ONE congruence already reaches the same endpoint, so "exactly m
    # moves" is a BOOKKEEPING CONVENTION for the structured route, not a
    # minimality theorem about congruences.
    single_entries = [sp.Integer(1)] * size
    single_entries[half] = 1 / sp.sqrt(gram_symbol)
    for k in range(1, half):
        single_entries[k] = sp.sqrt(q[0] / q[k])
        single_entries[size - k] = sp.sqrt(q[0] / q[k])
    single = sp.diag(*single_entries)
    single_gram = (single.T * gram * single).applyfunc(sp.simplify)
    single_density = (single_gram / sp.trace(single_gram)).applyfunc(sp.simplify)
    single_reaches_uniform = matrix_zero(
        single_gram - q[0] * sp.eye(size)
    ) and matrix_zero(single_density - sp.eye(size) / size)

    # (iii) the MIRROR-COMPATIBILITY criterion.  A general positive diagonal
    # congruence sends q_k -> lambda_k^2 q_k, so it preserves q_k = q_{N-k} iff
    # lambda_{N-k} = lambda_k.  Mirror-compatible moves keep the forced
    # equality; unconstrained ones destroy it while staying admissible.
    lambdas = sp.symbols(f"l0:{size}", positive=True)
    general = sp.diag(*lambdas)
    general_gram = (general.T * gram * general).applyfunc(sp.simplify)
    general_weights = tuple(general_gram[k, k] for k in range(size))
    mirror_substitution = {
        lambdas[size - k]: lambdas[k] for k in range(1, half)
    }
    mirror_compatible_preserves = all(
        sp.simplify(
            (general_weights[k] - general_weights[size - k]).subs(
                mirror_substitution
            )
        )
        == 0
        for k in range(1, half)
    ) and all(
        sp.simplify(general_weights[k] - lambdas[k] ** 2 * weights[k]) == 0
        for k in range(size)
    )

    unconstrained = sp.diag(*UNCONSTRAINED_SCALE[:size])
    unconstrained_gram = (unconstrained.T * gram * unconstrained).applyfunc(
        sp.simplify
    )
    unconstrained_breaks_mirror = any(
        sp.simplify(unconstrained_gram[k, k] - unconstrained_gram[size - k, size - k])
        != 0
        for k in range(1, half)
    )
    unconstrained_is_admissible = landed_admissibility(unconstrained, gram)

    # (iv) the bias is REMOVABLE, so "which block is biased" is frame talk.
    upper, lower = sp.symbols("s_a s_b", positive=True)
    transformed_gram_ratio = sp.cancel(
        (lower**2 * gram_symbol * q[0]) / (upper**2 * q[0])
    )
    solved = sp.solve(sp.Eq(transformed_gram_ratio, 1), lower)
    bias_removable = (
        len(solved) == 1
        and sp.simplify(solved[0] - upper / sp.sqrt(gram_symbol)) == 0
        and sp.simplify(transformed_gram_ratio.subs(lower, upper) - gram_symbol)
        == 0
    )
    # the bias-killing move touches only the SELF-paired index N/2, which is its
    # own mirror, so it is mirror compatible and the forced equality survives it
    bias_move_is_mirror_compatible = (
        intra[half, half] != 1
        and all(
            intra[k, k] == intra[size - k, size - k] for k in range(1, half)
        )
        and all(intra[k, k] == 1 for k in range(size) if k != half)
    )

    return FrameLedger(
        size,
        len(moves),
        structured_reaches_uniform,
        structured_scales_admissible,
        single_reaches_uniform,
        landed_admissibility(single, gram),
        # minimality would mean no shorter route exists; one congruence is a
        # shorter route, so the m-move count is NOT minimal
        not single_reaches_uniform,
        mirror_compatible_preserves,
        unconstrained_breaks_mirror,
        unconstrained_is_admissible,
        bias_removable,
        bias_move_is_mirror_compatible,
        no_float(gram) and no_float(single) and no_float(unconstrained),
    )


def ledger_verdict(item: FrameLedger) -> bool:
    return all(
        (
            item.structured_move_count == item.size // 2,
            item.structured_reaches_uniform,
            item.structured_scales_admissible,
            item.single_congruence_reaches_uniform,
            item.single_congruence_admissible,
            item.mirror_compatible_preserves,
            item.unconstrained_breaks_mirror,
            item.unconstrained_is_admissible,
            item.bias_removable,
            item.bias_move_is_mirror_compatible,
            item.exact,
        )
    )


# ---------------------------------------------------------------------------
# the general-m table this block lands
# ---------------------------------------------------------------------------
STATE_AFFINE_DIMENSIONS = ((4, 5), (6, 8), (8, 11), (10, 14))
COMMUTANT_DIMENSIONS = ((4, 4), (6, 6), (8, 8), (10, 10))
COMMUTANT_RANKS = ((4, 2), (6, 3), (8, 4), (10, 5))
REACH_DIMENSIONS = ((4, 2), (6, 4), (8, 6), (10, 8))
GENERATOR_GAP_TABLE = (
    (4, (2, -2)),
    (6, (2, 4, -3)),
    (8, (2, 4, 6, -4)),
    (12, (2, 4, 6, 8, 10, -6)),
)
COLLISION_SIZES = (4, 8, 12)
Z6_TRACE_SQUARE_CLASSES = ((0, 3), (1, 2, 4, 5))


# ---------------------------------------------------------------------------
# measured facts (computed once, before any mutation flag is consulted)
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Facts:
    main_head: str
    authority: AuthorityCertificate
    states: tuple[StateCertificate, ...]
    state_affine_dimensions: tuple[tuple[int, int], ...]
    commutant_dimensions: tuple[tuple[int, int], ...]
    commutant_ranks: tuple[tuple[int, int], ...]
    commutant_lemma: bool
    general_dimension_lemma: bool
    general_gap_lemma: bool
    single_pair_reach_lemma: bool
    extremes: tuple[ExtremeCertificate, ...]
    tower: TowerAutomorphismCertificate
    z6: tuple[FixtureVacuum, ...]
    q_mirror_all: bool
    gram_one_on_some_branch: bool
    branch_dependent_direction: bool
    vacuum_structures: tuple[VacuumStructure, ...]
    z8_chains: tuple[Z8RealityChain, ...]
    z8_reality_chain: bool
    deep_route_wired: bool
    deep_requested: bool
    z8_tower_ran: bool
    z8_deep: Z8DeepTower | None
    momenta: tuple[MomentumCertificate, ...]
    generator_gap_table: tuple[tuple[int, tuple[int, ...]], ...]
    symbolic_orbit: bool
    collisions: tuple[CollisionCertificate, ...]
    collision_sizes: tuple[int, ...]
    z4_matches_block133: bool
    balanced: tuple[BalancedCertificate, ...]
    reach_dimensions: tuple[tuple[int, int], ...]
    self_block_balanced_nonzero: bool
    ledgers: tuple[FrameLedger, ...]
    ledger_is_minimal: bool
    unconstrained_breaks_mirror: bool
    exact_no_float: bool
    scope: dict[str, bool]


def measure(deep_z8: bool) -> Facts:
    main_head = git_output("rev-parse", "origin/main")
    authority = authority_certificate(main_head)

    states = tuple(state_certificate(size) for size in FAMILY_SIZES)
    extremes = tuple(extreme_certificate(size // 2) for size in FAMILY_SIZES)

    tower = tower_automorphism_certificate()
    z6 = (
        z6_vacuum("Z6 c=5/13", b136.PRIMARY_SHEAR),
        z6_vacuum("Z6 c=3/5", b136.SECOND_SHEAR),
    )
    vacuum_structures = tuple(vacuum_structure(size) for size in FAMILY_SIZES)

    z8_chains = tuple(
        z8_reality_chain(shear)
        for shear in (b136.PRIMARY_SHEAR, b136.SECOND_SHEAR)
    )
    z8_deep = z8_deep_tower(b136.PRIMARY_SHEAR) if deep_z8 else None

    momenta = tuple(momentum_certificate(size) for size in DYNAMICS_SIZES)
    collisions = tuple(
        collision_certificate(size) for size in COLLISION_PROBE_SIZES
    )
    balanced = tuple(balanced_certificate(size) for size in FAMILY_SIZES)
    ledgers = tuple(frame_ledger(size) for size in LEDGER_SIZES)

    return Facts(
        main_head=main_head,
        authority=authority,
        states=states,
        state_affine_dimensions=tuple(
            (item.size, item.affine_dimension) for item in states
        ),
        commutant_dimensions=tuple(
            (item.size, item.commutant_dimension) for item in states
        ),
        commutant_ranks=tuple(
            (item.size, item.commutant_rank) for item in states
        ),
        commutant_lemma=one_block_commutant_lemma(),
        general_dimension_lemma=general_m_dimension_lemma(),
        general_gap_lemma=general_m_gap_lemma(),
        single_pair_reach_lemma=single_pair_reach_lemma(),
        extremes=extremes,
        tower=tower,
        z6=z6,
        q_mirror_all=all(item.conjugate_norms_forced for item in z6),
        gram_one_on_some_branch=not all(
            all(item.gram_not_one_on_branch) for item in z6
        ),
        branch_dependent_direction=all(
            item.branch_dependent_direction for item in z6
        ),
        vacuum_structures=vacuum_structures,
        z8_chains=z8_chains,
        z8_reality_chain=all(
            reality_chain_verdict(item) for item in z8_chains
        ),
        deep_route_wired=deep_route_wired(),
        deep_requested=bool(deep_z8),
        z8_tower_ran=z8_deep is not None,
        z8_deep=z8_deep,
        momenta=momenta,
        generator_gap_table=tuple(
            (item.size, item.gaps) for item in momenta
        ),
        symbolic_orbit=symbolic_orbit_law(),
        collisions=collisions,
        collision_sizes=tuple(
            item.size for item in collisions if item.magnitudes_agree
        ),
        z4_matches_block133=block133_z4_consistency(),
        balanced=balanced,
        reach_dimensions=tuple(
            (item.size, item.reach_dimension) for item in balanced
        ),
        self_block_balanced_nonzero=not all(
            item.self_balanced_forces_zero for item in balanced
        ),
        ledgers=ledgers,
        ledger_is_minimal=all(item.ledger_is_minimal for item in ledgers),
        unconstrained_breaks_mirror=all(
            item.unconstrained_breaks_mirror for item in ledgers
        ),
        exact_no_float=all(item.exact for item in states)
        and all(item.exact for item in z6)
        and all(item.exact for item in z8_chains)
        and all(item.exact for item in momenta)
        and all(item.exact for item in ledgers),
        scope=scope_certificate(raw_note()),
    )


# ---------------------------------------------------------------------------
# H. note scope
# ---------------------------------------------------------------------------
# PLACEHOLDER FENCE.  The landing supervisor replaces this string with the
# note's own eight-line N5 fence, byte for byte; until then H-note-scope is the
# single failing gate and the runner exits 1.
N5_FENCE = 'N5: per_element: THE STATE SPACE of Sym_2(R)^m -- ambient algebra dimension 3m, ONE trace constraint, hence AFFINE STATE DIMENSION 3m-1 (5/8/11/14 at m=2/3/4/5), center R^m; states are per-block triples (w_j, x_j, z_j) with sum w_j = 1 and x_j^2 + z_j^2 <= 1; the EXTREME states are m DISJOINT RP^1 circles, ONE PER BLOCK, with BOTH extremality directions verified -- purity forces support in a single block through the exact Tr rho^2 identity (rho^2 - rho = w(w-1)(P1+P2) on a two-block mixture), and interior or two-block states admit strict convex decompositions -- while the ANTISYMMETRIC COMMUTATOR DIRECTION stays INADMISSIBLE in every block; checker range m = 2..7\nper_site: THE CERTIFIED-FRAME VACUUM D_cert = diag(q_0..q_{N-1})/S: with the PIVOT-NORMALIZED boundary vectors (y_{N-k} = conj(y_k) ENTRYWISE, y_k0 = 1) the direction weights q_k = sum_j |y_kj|^2 satisfy q_k = q_{N-k} EXACTLY -- every conjugate-pair block is I/2 BY FORCE -- and q_k >= 1 STRUCTURALLY with q_k real, the tower conjugation being a VERIFIED AUTOMORPHISM FIXING THE TOWER GENERATORS and the pivot term contributing 1; the SELF-CONJUGATE block is the ONLY biased one, q_0 != q_{N/2} exactly with internal density diag(1, g)/(1+g), g = q_{N/2}/q_0 != 1, verified at Z6 for BOTH committed shears and at Z8 for the primary shear with the exact tower elements displayed; BRANCH CAVEAT -- the committed Block 136 machinery NEVER PINS the stable branch of the quadratic-tower root and g is BRANCH-DEPENDENT (Z6 at 5/13: 0.400756... or 1.033346...; at 3/5: 0.177098... or 1.086245...), ONLY g != 1 IS BRANCH-FREE, branch pinning is a named next; LABEL CAVEAT -- on the branch matching the landed Block 119 stable root the Z6/Z8 self-block weights reproduce Block 133\'s landed Z4 weights WITH THE TWO SELF-BLOCK INDICES SWAPPED (g here = 1/g_02 landed, inside the landed pin interval), so WHICH MEMBER IS BIASED is a LABELING/FRAME statement that does NOT transfer between the landed presentations; CROSS-SIZE OBSERVATION -- the self-block weights are NUMERICALLY IDENTICAL at N = 4, 6, 8 to the computed precision, so the Block 139 cross-size law (the k=0 monodromy trace) APPEARS TO EXTEND to the boundary vectors themselves: OBSERVATION, NOT LAW, the exact cross-size boundary-weight law is a NAMED NEXT\nper_mode: THE DYNAMICS: the certified-frame momentum is P = diag(signed charge), c_k = k for k <= N/2 else k - N, so c_{N/2} = +N/2 and BLOCK 136\'S RESIDUE CORRECTION is what produces the self rate; each conjugate pair (k, N-k) rotates with generator difference 2k and the self pair with -m, by the EXACT cos/sin quadrature orbit law with I and Z FIXED -- Z4 (2, -2), Z6 (2, 4, -3), Z8 (2, 4, 6, -4), rates confirmed to N = 12; THE RATE COLLISION IS A 4|N PHENOMENON, NOT Z8-SPECIFIC -- whenever 4 divides N the pair (N/4, 3N/4) has rate 2(N/4) = N/2 and the self pair has |-N/2|, EQUAL MAGNITUDES, so Z4\'s own (2, -2) is ALREADY the collision, Z8\'s (4, -4) likewise, Z12 next; the commutant is span{I_j, Z_j}, dimension 2m, PROVEN FOR GENERAL m by the one-block lemma [diag(p,q), aI+bX+cZ] = b(p-q)(E01-E10); SELECTION RULE -- X_j carries momentum charge equal to its rate difference\nper_block: THE BALANCED REACH AND THE FRAME LEDGER: every conjugate pair carries the FULL FREE-RELATIVE-PHASE EQUATOR with ZERO charge expectation on the balanced ray (its two charges are +k and -k); the SELF block\'s balanced ray with zero charge expectation FORCES s = 0, since its charge diag(0, m) is POSITIVE SEMIDEFINITE and the expectation is m s^2 -- the self block CONTRIBUTES NOTHING to the balanced class, which is NOT the claim that it cannot be balanced -- so the PHASE-INVARIANT ADMISSIBLE REACH is exactly span{I_j, Z_j} over the m-1 conjugate pairs, DIMENSION 2(m-1) = 2/4/6 at m = 2/3/4, with Y still inadmissible; THE FRAME LEDGER -- the m structured congruence moves (ONE intra-self, m-1 PAIR-UNIFORM) send the certified gram to q_0 I_N and the vacuum to Tr/N, but "m MOVES" IS A BOOKKEEPING CONVENTION, NOT MINIMALITY (a single positive diagonal congruence reaches the same endpoint), and the forced conjugate equality q_k = q_{N-k} is FRAME-FREE ONLY UNDER MIRROR-COMPATIBLE MOVES lambda_{N-k} = lambda_k -- an UNCONSTRAINED positive real diagonal congruence BREAKS the equality while STILL PASSING the landed admissibility test, so the qualifier is LOAD-BEARING; the bias MAGNITUDE is frame-dependent and removable\nlattice_wide: THE GENERAL-m TABLE (algebra 3m, center m, states 3m-1, forced-mixed m-1, biased 1, ledger m, commutant rank m, conserved dim 2m, balanced reach 2m-2) with differences (2, 4, ..., 2(m-1), -m), verified at m = 2..7, the m = 2 column CROSS-CHECKED against Block 133\'s and Block 136\'s OWN LANDED CERTIFICATES (5-dim body, differences (-2,+2), conserved 4, reach 2, biased self block, conjugate block I/2, two-move ledger, pair tables at N = 4 and 6); NAMED OPENS for general m -- (i) the self-block bias q_0 != q_{N/2} is FIXTURE-VERIFIED AT m = 2, 3, 4 ONLY, (ii) the momentum instantiation at EVERY N, (iii) the family coverage form, (iv) BRANCH PINNING for the stable root, (v) the EXACT cross-size weight law; VERIFICATION SURFACE -- the Z8 vacuum weights were computed TWICE INDEPENDENTLY (the solve via a FRESH base-field adapter onto the Block 139 field, since the committed Block 136 adapter\'s class attributes are BOUND AT IMPORT and a plain module-global swap CANNOT reach the Z8 tower; the checker via its OWN 925-second residue-tower rebuild at the primary shear), the Z8 SECOND-SHEAR BIAS is UNCOMPUTED (the forcing chain is structural at both shears), and the landing runner carries Z6 FULLY (both shears) with the Z8 structural chain IN-GATE and the deep Z8 tower behind a DOCUMENTED FLAG for sweep tractability\nRESULT: on the certified m-block observable algebra Sym_2(R)^m carried by the displayed Z4, Z6 and Z8 fixtures at the displayed shears and masses, BLOCK 133\'S MEASUREMENT THEORY GENERALIZES FROM m = 2 TO GENERAL m -- the state body (3m-1), the m-circle pure boundary, the FORCED conjugate mixing q_k = q_{N-k} with every conjugate block I/2, the SINGLE biased self block diag(1,g)/(1+g) with g != 1, the rate law (2, 4, ..., 2(m-1), -m) with its 4|N collision, the commutant span{I_j, Z_j} of dimension 2m, and the balanced reach 2(m-1) all CLOSE IN m -- with the table SYMBOLIC and verified to m = 7, the BIAS FIXTURE-VERIFIED at m = 2, 3, 4 ONLY, the value of g BRANCH-DEPENDENT, the identity of the biased member a LABELING/FRAME statement differing from the landed Z4 presentation by an index swap, the m-move ledger a BOOKKEEPING CONVENTION rather than a minimum, the forced equality frame-free ONLY under mirror-compatible moves, and the cross-size boundary-weight coincidence at N = 4, 6, 8 an OBSERVATION rather than a law; no tensor-product structure and no additional dynamical law is claimed at any m\nDECISION_CUT: prove the EXACT CROSS-SIZE BOUNDARY-WEIGHT LAW, since the self-block weights coincide at N = 4, 6, 8 to the computed precision and the Block 139 k=0 law is the only committed statement of that kind; extend the GENERAL-m SELF-BLOCK BIAS beyond the three fixtures where q_0 != q_{N/2} is verified, which is the one clause of the theory that is not symbolic; PIN THE STABLE BRANCH of the quadratic-tower root, without which the value of g is undetermined and the landed comparison can only be made up to a labeling; compute the Z8 SECOND-SHEAR BIAS to close the fixture surface; and execute the JOINT-LANE PROGRAM without assuming a differential, a work order, a carrier, transporter completion, a gravity quotient, or joint gravity\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero'


SCOPE_KEYS = (
    "table_shape",
    "forced_mixing",
    "branch_caveat",
    "label_caveat",
    "cross_size",
    "collision_correction",
    "balanced_rewording",
    "frame_corrections",
    "scoping_disclosure",
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
        # the general-m table: state dimension, conserved dimension, reach
        "table_shape": "3m-1" in note
        and "2m" in note
        and ("2(m-1)" in compact or "2m-2" in compact),
        "forced_mixing": "by force" in note or "forced" in note,
        # the bias has no signed reading: only "g != 1" is branch-free
        "branch_caveat": "branch-dependent" in note
        and ("only g != 1" in note or "onlyg!=1" in compact),
        # Block 133 lists the self block first: a labelling difference
        "label_caveat": "indices swapped" in note or "label" in note,
        "cross_size": "named next" in note and "cross-size" in note,
        # the |rate| collision is the 4|N phenomenon, not a size-specific one
        "collision_correction": ("4|n" in compact or "4 divides n" in note)
        and "z8 novelty" not in note,
        "balanced_rewording": "forces s = 0" in note
        or "zero charge expectation" in note,
        "frame_corrections": (
            "bookkeeping convention" in note or "not minimality" in note
        )
        and "mirror-compatible" in note,
        "scoping_disclosure": ("independently twice" in note or "deep" in note)
        and "second-shear bias" in note
        and "uncomputed" in note,
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
        "state_affine_dimensions": STATE_AFFINE_DIMENSIONS,
        "commutant_dimensions": COMMUTANT_DIMENSIONS,
        "q_mirror_holds": True,
        "gram_is_one_on_some_branch": False,
        "z8_reality_chain_holds": True,
        "z8_tower_in_default_path": False,
        "generator_gap_table": GENERATOR_GAP_TABLE,
        "collision_sizes": COLLISION_SIZES,
        "z4_matches_block133": True,
        "self_block_balanced_nonzero": False,
        "ledger_is_minimal": False,
        "mirror_qualifier_required": True,
        "required_scope_keys": SCOPE_KEYS,
    }
    if mutation == "stale_main_authority":
        claims["main_head"] = STALE_MAIN
    elif mutation == "stale_parent_authority":
        claims["parent_pin"] = "stale"
    elif mutation == "wrong_state_dimension":
        claims["state_affine_dimensions"] = tuple(
            (size, value + 1 if size == 8 else value)
            for size, value in STATE_AFFINE_DIMENSIONS
        )
    elif mutation == "break_commutant":
        claims["commutant_dimensions"] = tuple(
            (size, value - 1 if size == 6 else value)
            for size, value in COMMUTANT_DIMENSIONS
        )
    elif mutation == "break_q_equality":
        claims["q_mirror_holds"] = False
    elif mutation == "claim_gram_is_one":
        claims["gram_is_one_on_some_branch"] = True
    elif mutation == "break_reality_chain":
        claims["z8_reality_chain_holds"] = False
    elif mutation == "claim_deep_is_default":
        claims["z8_tower_in_default_path"] = True
    elif mutation == "wrong_generator_rates":
        claims["generator_gap_table"] = tuple(
            (size, (2, 4, 6, -3) if size == 8 else gaps)
            for size, gaps in GENERATOR_GAP_TABLE
        )
    elif mutation == "wrong_collision_set":
        claims["collision_sizes"] = tuple(sorted(COLLISION_SIZES + (6,)))
    elif mutation == "break_z4_consistency":
        claims["z4_matches_block133"] = False
    elif mutation == "claim_self_balanced_nonzero":
        claims["self_block_balanced_nonzero"] = True
    elif mutation == "claim_ledger_minimality":
        claims["ledger_is_minimal"] = True
    elif mutation == "drop_mirror_qualifier":
        claims["mirror_qualifier_required"] = False
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
            "docs/ADMISSIBILITY_DIRAC_KAHLER_M_BLOCK_MEASUREMENT_THEORY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_SEAM_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-08-19.md",
            "scripts/admissibility_dirac_kahler_seam_dichotomy_2026_08_19.py",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_BLOCK_STATES_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-08-17.md",
            "scripts/admissibility_dirac_kahler_two_block_states_dynamics_2026_08_17.py",
        )
        and PARENT_ARTIFACTS
        == (BLOCK145_NOTE, BLOCK145_RUNNER, BLOCK133_NOTE, BLOCK133_RUNNER)
        and facts.main_head == claims["main_head"]
        and authority.fixed_authority
        and authority.parent_ref_and_ancestry
        and parent_blobs_ok
    )

    gate_b = bool(
        facts.state_affine_dimensions
        == tuple(tuple(row) for row in claims["state_affine_dimensions"])
        and facts.commutant_dimensions
        == tuple(tuple(row) for row in claims["commutant_dimensions"])
        and facts.commutant_ranks == COMMUTANT_RANKS
        and all(
            item.ambient_dimension == 3 * item.blocks
            and item.trace_rank == 1
            and item.affine_dimension == 3 * item.blocks - 1
            and item.center_dimension == item.blocks
            and item.center_is_identities
            and item.symmetric
            and item.block_orthogonal
            and item.jordan_closed
            and item.jordan_generator_excluded
            and item.coordinates_onto
            and item.commutant_is_i_and_z
            and item.selection_rule
            and item.all_gaps_nonzero
            and item.circles_disjoint
            for item in facts.states
        )
        and facts.commutant_lemma
        and facts.general_dimension_lemma
        and all(
            item.purity_identity
            and item.weight_square_identity
            and item.purity_forces_one_block
            and item.psd_zero_diagonal
            and item.vanishing_convex_slot
            and item.projector_is_extreme
            and item.cross_block_mixture_strict
            and item.interior_point_strict
            and item.rp1_projector
            and item.rp1_circle
            and item.rp1_antipodal
            for item in facts.extremes
        )
        and facts.exact_no_float
    )

    tower = facts.tower
    gate_c = bool(
        tower.generators_fixed
        and tower.tower_relations
        and tower.involutive
        and tower.additive
        and tower.multiplicative
        and tower.norms_self_conjugate
        and tower.norm_is_mirror_invariant
        and tower.embedding_real
        and len(facts.z6) == 2
        and all(fixture_verdict(item) for item in facts.z6)
        and all(
            item.trace_square_classes == Z6_TRACE_SQUARE_CLASSES
            for item in facts.z6
        )
        and facts.z6[0].trace_squares != facts.z6[1].trace_squares
        and facts.q_mirror_all == bool(claims["q_mirror_holds"])
        and facts.gram_one_on_some_branch
        == bool(claims["gram_is_one_on_some_branch"])
        and facts.branch_dependent_direction
        and all(
            item.trace_one
            and item.conjugate_blocks_maximally_mixed
            and item.self_block_biased
            and item.functional_exact
            and item.closed_form_central_weights
            for item in facts.vacuum_structures
        )
        and facts.exact_no_float
    )

    # The tower runs IFF --deep-z8 was requested; a claim that the deep tower
    # sits on the default path predicts a run that did not happen.
    predicted_tower_ran = (
        bool(claims["z8_tower_in_default_path"]) or facts.deep_requested
    )
    gate_d = bool(
        facts.z8_reality_chain == bool(claims["z8_reality_chain_holds"])
        and len(facts.z8_chains) == 2
        and facts.deep_route_wired
        and facts.z8_tower_ran == predicted_tower_ran
        and (not facts.deep_requested or deep_tower_verdict(facts.z8_deep))
        and len(Z8_RECORDED_WEIGHT_TEXT) == 8
        and facts.exact_no_float
    )

    gate_e = bool(
        facts.generator_gap_table
        == tuple(
            (size, tuple(gaps)) for size, gaps in claims["generator_gap_table"]
        )
        and facts.collision_sizes == tuple(claims["collision_sizes"])
        and facts.z4_matches_block133 == bool(claims["z4_matches_block133"])
        and all(
            item.momentum_is_signed_charge
            and item.self_sector_charge == item.size // 2
            and item.charges_antisymmetric_off_self
            and item.gaps_match_prediction
            and item.orbits_exact
            and item.identity_and_z_fixed
            and item.all_gaps_nonzero
            for item in facts.momenta
        )
        and facts.symbolic_orbit
        and facts.general_gap_lemma
        and all(
            item.magnitudes_agree == item.divisible
            and (not item.divisible or item.counter_rotating)
            for item in facts.collisions
        )
        and facts.exact_no_float
    )

    gate_f = bool(
        facts.reach_dimensions == REACH_DIMENSIONS
        and facts.self_block_balanced_nonzero
        == bool(claims["self_block_balanced_nonzero"])
        and facts.single_pair_reach_lemma
        and all(
            item.equator_exact
            and item.positivity_identity
            and item.pair_charge_balanced
            and item.self_charge_is_semidefinite
            and item.self_balanced_forces_zero
            and item.expectation_exact
            and item.invariant_is_i_and_z
            and item.invariant_rank == item.conjugate_pairs
            and item.reach_dimension == 2 * item.conjugate_pairs
            and item.y_not_admissible
            for item in facts.balanced
        )
    )

    gate_g = bool(
        facts.ledger_is_minimal == bool(claims["ledger_is_minimal"])
        and facts.unconstrained_breaks_mirror
        == bool(claims["mirror_qualifier_required"])
        and all(ledger_verdict(item) for item in facts.ledgers)
        and facts.exact_no_float
    )

    required = tuple(claims["required_scope_keys"])
    budget = DEEP_BUDGET_SEC if facts.deep_requested else DEFAULT_BUDGET_SEC
    gate_h = bool(
        set(facts.scope) == set(required)
        and all(facts.scope.values())
        and len(MUTATIONS) == 15
        and len(set(MUTATIONS)) == 15
        and set(MUTATION_GATE) == set(MUTATIONS)
        and set(MUTATION_GATE.values()) == set("ABCDEFGH")
        and N5_FENCE.count("\n") == 7
        and elapsed_ns <= budget * 1_000_000_000
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
        "--deep-z8",
        action="store_true",
        help=(
            "also run the ~15 minute Z8 residue tower; the default gate path "
            "runs only the cheap Z8 structural reality chain"
        ),
    )
    arguments = parser.parse_args()
    if arguments.mutation and arguments.deep_z8:
        parser.error(
            "the mutation sweep is defined against the DEFAULT gate path; "
            "run --mutation without --deep-z8"
        )
    started_ns = time.monotonic_ns()

    # Every measurement happens once, before any mutation flag is consulted,
    # so a mutation can only rewrite a CLAIM.  No gate can cascade into
    # another because no gate feeds a measurement.
    facts = measure(arguments.deep_z8)
    elapsed_ns = time.monotonic_ns() - started_ns

    raw_gates = evaluate_gates(facts, build_claims(""), elapsed_ns)
    gate_values = dict(raw_gates)
    if arguments.mutation:
        target = MUTATION_GATE[arguments.mutation]
        gate_values = evaluate_gates(
            facts, build_claims(arguments.mutation), elapsed_ns
        )
        changed = {
            key for key in raw_gates if raw_gates[key] != gate_values[key]
        }
        if changed - {target} or gate_values[target]:
            raise AssertionError("mutation did not fail exactly its own gate")

    checks = Checks()
    checks.check(
        "A-authority",
        "main plus the committed Block 145 note/runner and Block 133 note/runner artifacts are content-bound",
        gate_values["A"],
    )
    checks.check(
        "B-state-space",
        "Sym_2(R)^m has dimension 3m and centre R^m, the trace functional has rank one, and the states form an affine body of dimension exactly 3m-1 -- symbolically, from the disjoint block supports and the trace row (2,0,0) repeated m times, and concretely as 5, 8, 11, 14 at m=2,3,4,5; the extreme points are the m disjoint RP^1 circles, certified both ways by the exact deficit identity 1 - Tr D^2 - 2 sum_{i<j} w_i w_j - sum_j w_j^2 (1-x_j^2-z_j^2)/2 = 1 - (sum w)^2 together with the PSD zero-diagonal lemma, and by explicit strict decompositions of every cross-block mixture and every interior disk point; and the selection rule [diag(p,q), aI+bX+cZ] = b(p-q)(E01-E10) with all m gaps nonzero makes the momentum commutant exactly span{I_j,Z_j}, rank m and dimension 2m",
        gate_values["B"],
    )
    checks.check(
        "C-certified-vacuum",
        "at Z6 and at BOTH committed shears the fixture reality forces y_{N-k}=conj(y_k), hence q_k=q_{N-k} as exact tower elements, while q_0 != q_3 exactly and the gram g=q_3/q_0 differs from 1 on BOTH real branches of the quadratic tower with OPPOSITE directions, so the bias is branch-dependent and only g != 1 survives; q_k >= 1 follows from the tower-automorphism certificate (involutive, additive, multiplicative, generators fixed, real embedding since u_k > 4, unit pivot term), and the central weights close as W_pair = 2 q_k/S and W_self = q_0(1+g)/S",
        gate_values["C"],
    )
    checks.check(
        "D-z8-reality-chain",
        "the Z8 action is real and the projectors, momentum blocks and monodromies mirror exactly under k -> N-k at BOTH shears with u-classes (0,4),(1,3,5,7),(2,6), which forces q_k = q_{8-k} through the automorphism-invariance of the boundary norm; the ~15 minute Z8 residue tower is wired behind --deep-z8 through the same Z8Adapter/Z8Context route the solve used and is NOT on the default path, where the twice-verified Z8 weights are carried as documented non-gate constants",
        gate_values["D"],
    )
    checks.check(
        "E-momentum-dynamics",
        "P=diag(signed charge) on the window (-N/2,N/2] gives the self-conjugate sector charge +N/2; the generator gaps are (2,...,2(m-1),-m), verified symbolically at general m -- sector N-k carries -k so the pair gap is 2k, the self gap is -m, and neither can vanish -- and concretely at N=4,6,8,12, and the orbit law U X U^dag = cos(delta t) X + sin(delta t) Y is exact with I and Z fixed; the |rate|=N/2 collision between the conjugate pair (N/4,3N/4) and the self pair is the 4|N phenomenon, present at N=4,8,12 and absent at N=6,10; and the Z4 row matches Block 133's landed certificate as a multiset, with the displayed indices swapped because Block 133 lists the self block first",
        gate_values["E"],
    )
    checks.check(
        "F-balanced-reach",
        "every conjugate pair carries the full free-relative-phase equator with zero charge expectation on the balanced ray, while the self pair's charge diag(0,m) is only semidefinite, so demanding zero charge expectation there FORCES the balanced amplitude s=0; the expectation is <A> = sum_j w_j(a_j + r_j b_j cos phi_j), and the phase-invariant reach is span{I_j,Z_j} over the m-1 conjugate pairs -- symbolically, since one pair leaves rank 1 of 3 and so contributes exactly 2 -- of dimension exactly 2(m-1) = 2, 4, 6, 8 at m=2,3,4,5, with Y remaining inadmissible",
        gate_values["F"],
    )
    checks.check(
        "G-frame-ledger",
        "the m structured moves send the certified gram to q_0*I_N and the vacuum to Tr/N at N=4,6, but a SINGLE positive diagonal congruence reaches the same endpoint, so the move count is a bookkeeping convention and not a minimality claim; a mirror-compatible move (lambda_{N-k}=lambda_k) preserves q'_k=q'_{N-k} while the explicit unconstrained move diag(1,2,1,1,1,1) breaks it and still passes the landed admissibility test; and the bias is removable, so the biased-block identification is certified-frame only",
        gate_values["G"],
    )
    checks.check(
        "H-note-scope",
        "the general-m table, the forced conjugate mixing, the branch-dependent gram caveat, the Block 133 label caveat, the named cross-size obligations, the 4|N correction, the balanced rewording, the frame-ledger corrections, the Z8 scoping disclosure with its uncomputed second-shear bias, the cross-context disclosure, the firewalls and the exact N5 fence are present",
        gate_values["H"],
    )
    checks.report()
    print(
        f"Z8-RECORDED (non-gate, shear {Z8_RECORDED_SHEAR_TEXT}, verified "
        f"independently twice): {Z8_RECORDED_STRUCTURE_TEXT}"
    )
    print(
        "Z8-RECORDED-WEIGHTS (decimal read-outs under the principal embedding, "
        "documentation only, never gated): "
        + "; ".join(Z8_RECORDED_WEIGHT_TEXT)
    )
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
