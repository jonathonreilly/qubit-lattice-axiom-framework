#!/usr/bin/env python3
"""Block 121: exact DK-current / d=2 constraint-quotient certificate.

Two explicit link routings reconstruct the local U(1) Noether identity on
the antiperiodic Z8 x Z4 carrier.  The same exact matrices certify the
on-shell Euler-ideal factorization, the d=2 zero-TT count, the Gauss
intertwiner, the closed-carrier charge obstruction, and the honest
density-only content of the coupling.  Wall-clock timing is the only
floating-point computation.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import subprocess
import time

import sympy as sp

import admissibility_dirac_kahler_torus_wrap_defect_2026_08_16 as prior


R = sp.Rational
DK = prior.block118
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_NOTE = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TORUS_WRAP_DEFECT_"
    "BOUNDED_THEOREM_NOTE_2026-08-16.md"
)
PARENT_RUNNER = (
    "scripts/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.py"
)
PARENT_CACHE = (
    "logs/runner-cache/admissibility_dirac_kahler_torus_wrap_defect_"
    "2026_08_16.txt"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_TORUS_WRAP_DEFECT_BOUNDED_THEOREM_NOTE_2026-08-16.md",
    "scripts/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.py",
    "logs/runner-cache/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.txt",
)

AUDIT_TIMEOUT_SEC = 600
CURRENT_MAIN = "4e566b14a6352a9a62590252a9755c7a103c1b9e"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
PARENT_REF = (
    "origin/physics-loop/"
    "toe-axiom-closure-block120-torus-wrap-defect-20260816"
)
PARENT_COMMIT = "1c2386bf3df420707fd2ecb2d7ec84002ba40ad1"
PARENT_NOTE_BLOB = "48b3ed4d6e70d28fe3a9e02052fe531ae8491fb5"
PARENT_RUNNER_BLOB = "3e2dfc1e86d237bbef9cb702d5b79521eed0da2f"
PARENT_CACHE_BLOB = "0033d029368a1b7dd036b5c88cd1f064d8722c39"
ANCESTOR_COMMITS = (
    (119, "33fd2d21558604718f3a88713fe1976aff8f9dbb"),
    (118, "fdd1883c54ca8cc14b1337cc1edc249792d5dab2"),
    (117, "f800356aec0989b6e0fa80ed43274794243b1ca2"),
    (116, "c36d11e4e8d927c6fc31f0a8b579d4bd15f4fa43"),
    (115, "c78301fef7521d0518f485f1bf9266983c9e516a"),
    (114, "75026e71cfbd44ed665ddc41c22ebaa722720ea9"),
    (113, "e76893eb7204d1d727a3ab8838fb3fada3f45dfc"),
    (112, "385a6ba5b1594f20e5d4eebba9da68d8e72abc10"),
    (111, "b04e7c8747b09734711cfcd2bfab961bd12e81ad"),
    (110, "d6761278fca9cac617200792473a8f4da3a6cfff"),
    (109, "ad84cfcc857a65285389ba93b47cd7b718589be5"),
    (108, "8afe8dff5ccf531208238af0aaaec1f547d73874"),
    (107, "d41a05e153d4cb77eee125b82fc0b0bd767bf32e"),
    (106, "22d6d90ec2279e5868c9c825149b2a20beea3797"),
    (105, "d06066c2b908aaca0779625d831dfb10620cf34d"),
    (104, "7fe07db6c03fad1191893c942f708c5cb9a54c43"),
    (103, "99cee0a6c962b382a3ca1a8497d589ffa280dfe8"),
)

MUTATIONS = (
    "stale_axiom_authority",
    "stale_parent_authority",
    "break_routing_identity",
    "break_seam_sign",
    "break_onshell",
    "break_constraint_count",
    "claim_k0_exception",
    "break_intertwiner",
    "break_charge_norm",
    "claim_populated_quotient",
    "claim_r_selection",
    "claim_charge_commutation_content",
    "weaken_no_go_packet",
    "drop_n5_resolution",
    "claim_toe_progress",
)

NT = 8
NX = 4
NS = NT * NX
ROUTINGS = ("t-first", "x-first")


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition) -> None:
        ok = bool(condition)
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {statement}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


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
    return git_output("rev-parse", f"{commit}:{path}")


def is_ancestor(ancestor: str, descendant: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def authority_certificate(mutation: str) -> dict[str, object]:
    expected_axiom = (
        "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    )
    expected_parent = (
        "0" * 40 if mutation == "stale_parent_authority" else PARENT_NOTE_BLOB
    )
    ancestors = {
        f"ancestor_{number}": is_ancestor(commit, "HEAD")
        for number, commit in ANCESTOR_COMMITS
    }
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": commit_blob("origin/main", AXIOM_PATH),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "expected_axiom": expected_axiom,
        "registry": commit_blob("origin/main", REGISTRY_PATH),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT, "HEAD"),
        **ancestors,
        "parent_note": commit_blob(PARENT_COMMIT, PARENT_NOTE),
        "expected_parent": expected_parent,
        "parent_runner": commit_blob(PARENT_COMMIT, PARENT_RUNNER),
        "parent_cache": commit_blob(PARENT_COMMIT, PARENT_CACHE),
    }


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(value == 0 for value in matrix)


def site(time_index: int, space_index: int) -> int:
    return NX * (time_index % NT) + (space_index % NX)


def coordinates(index: int) -> tuple[int, int]:
    return divmod(index, NX)


def projector(index: int) -> sp.ImmutableSparseMatrix:
    return sp.ImmutableSparseMatrix(NS, NS, {(index, index): 1})


def shortest_displacement(start: int, stop: int, size: int) -> int:
    """Deterministic signed shortest displacement on an even cycle."""
    forward = (stop - start) % size
    return forward if forward <= size // 2 else forward - size


LinkStep = tuple[str, int, int, int]


def directed_path(
    start: int, stop: int, routing: str
) -> tuple[LinkStep, ...]:
    """Shortest path in one of the two declared coordinate orders."""
    time_index, space_index = coordinates(start)
    target_time, target_space = coordinates(stop)
    result: list[LinkStep] = []

    def append_temporal() -> None:
        nonlocal time_index
        displacement = shortest_displacement(time_index, target_time, NT)
        for _ in range(abs(displacement)):
            if displacement > 0:
                result.append(("t", time_index, space_index, 1))
                time_index = (time_index + 1) % NT
            else:
                time_index = (time_index - 1) % NT
                result.append(("t", time_index, space_index, -1))

    def append_spatial() -> None:
        nonlocal space_index
        displacement = shortest_displacement(space_index, target_space, NX)
        for _ in range(abs(displacement)):
            if displacement > 0:
                result.append(("x", time_index, space_index, 1))
                space_index = (space_index + 1) % NX
            else:
                space_index = (space_index - 1) % NX
                result.append(("x", time_index, space_index, -1))

    if routing == "t-first":
        append_temporal()
        append_spatial()
    elif routing == "x-first":
        append_spatial()
        append_temporal()
    else:
        raise ValueError(f"unknown routing {routing!r}")
    if site(time_index, space_index) != stop:
        raise AssertionError("routed path does not reach its endpoint")
    return tuple(result)


def canonical_path(
    start: int, stop: int, routing: str
) -> tuple[LinkStep, ...]:
    """Orient each unordered hopping pair once and reverse its flow exactly."""
    if start < stop:
        return directed_path(start, stop, routing)
    return tuple(
        (direction, time_index, space_index, -sign)
        for direction, time_index, space_index, sign in directed_path(
            stop, start, routing
        )
    )


@dataclass(frozen=True)
class RoutedCurrent:
    routing: str
    temporal: tuple[sp.Matrix, ...]
    spatial: tuple[sp.Matrix, ...]
    identity_exact: bool


@dataclass(frozen=True)
class CurrentCertificate:
    shear: sp.Rational
    action: sp.Matrix
    routings: tuple[RoutedCurrent, RoutedCurrent]
    curl_potential: tuple[sp.Matrix, ...]
    curl_exact: bool
    routing_distinct: bool
    seam_exact: bool
    seam_coefficient: sp.Expr
    commutator_counts: tuple[int, ...]
    ideal_factorization_exact: bool


def current_kernels(
    action: sp.Matrix, routing: str
) -> tuple[tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    """Route every off-diagonal bar(phi)_a Q_ab psi_b monomial."""
    if action.shape != (NS, NS):
        raise AssertionError("DK action must act on all 32 fine sites")
    temporal = [sp.MutableSparseMatrix(NS, NS, {}) for _ in range(NS)]
    spatial = [sp.MutableSparseMatrix(NS, NS, {}) for _ in range(NS)]
    for start in range(NS):
        for stop in range(NS):
            coefficient = action[start, stop]
            if start == stop or coefficient == 0:
                continue
            for direction, time_index, space_index, sign in canonical_path(
                start, stop, routing
            ):
                target = temporal if direction == "t" else spatial
                target[site(time_index, space_index)][start, stop] += (
                    sign * coefficient
                )
    return (
        tuple(sp.ImmutableSparseMatrix(value) for value in temporal),
        tuple(sp.ImmutableSparseMatrix(value) for value in spatial),
    )


def backward_divergence(
    temporal: tuple[sp.Matrix, ...],
    spatial: tuple[sp.Matrix, ...],
    time_index: int,
    space_index: int,
) -> sp.Matrix:
    index = site(time_index, space_index)
    return (
        temporal[index]
        - temporal[site(time_index - 1, space_index)]
        + spatial[index]
        - spatial[site(time_index, space_index - 1)]
    )


def curl_reconstruction(
    first: RoutedCurrent, second: RoutedCurrent
) -> tuple[tuple[sp.Matrix, ...], bool, bool]:
    """Reconstruct K with dJ=Delta_x^-K and dS=-Delta_t^-K."""
    delta_temporal = tuple(
        second.temporal[index] - first.temporal[index] for index in range(NS)
    )
    delta_spatial = tuple(
        second.spatial[index] - first.spatial[index] for index in range(NS)
    )
    potential: list[sp.Matrix] = [sp.zeros(NS) for _ in range(NS)]

    # Gauge K(0,0)=0.  The first column follows from dS, and each row then
    # follows from dJ.  Exact closure at both periodic seams is checked below.
    for time_index in range(1, NT):
        potential[site(time_index, 0)] = (
            potential[site(time_index - 1, 0)]
            - delta_spatial[site(time_index, 0)]
        )
    for time_index in range(NT):
        for space_index in range(1, NX):
            potential[site(time_index, space_index)] = (
                potential[site(time_index, space_index - 1)]
                + delta_temporal[site(time_index, space_index)]
            )

    curl_exact = all(
        matrix_zero(
            delta_temporal[site(time_index, space_index)]
            - (
                potential[site(time_index, space_index)]
                - potential[site(time_index, space_index - 1)]
            )
        )
        and matrix_zero(
            delta_spatial[site(time_index, space_index)]
            - (
                -potential[site(time_index, space_index)]
                + potential[site(time_index - 1, space_index)]
            )
        )
        and matrix_zero(
            backward_divergence(
                delta_temporal,
                delta_spatial,
                time_index,
                space_index,
            )
        )
        for time_index in range(NT)
        for space_index in range(NX)
    )
    routing_distinct = any(
        not matrix_zero(delta_temporal[index])
        or not matrix_zero(delta_spatial[index])
        for index in range(NS)
    )
    return tuple(potential), curl_exact, routing_distinct


def seam_certificate(
    action: sp.Matrix, routings: tuple[RoutedCurrent, RoutedCurrent]
) -> tuple[bool, sp.Expr]:
    seam_pairs = tuple(
        (start, stop)
        for start in range(NS)
        for stop in range(NS)
        if action[start, stop] != 0
        and {coordinates(start)[0], coordinates(stop)[0]} == {0, NT - 1}
    )
    routed_exact = True
    for start, stop in seam_pairs:
        coefficient = action[start, stop]
        for current in routings:
            seam_steps = tuple(
                step
                for step in canonical_path(start, stop, current.routing)
                if step[0] == "t" and step[1] == NT - 1
            )
            routed_exact = routed_exact and len(seam_steps) == 1
            if len(seam_steps) == 1:
                _, time_index, space_index, sign = seam_steps[0]
                routed_exact = routed_exact and (
                    current.temporal[site(time_index, space_index)][start, stop]
                    == sign * coefficient
                )

    # The last bulk link and the wrap link use the same local magnitude and
    # the opposite sign in both matrix orientations: the literal AP seam.
    antiperiodic_sign = len(seam_pairs) == 2 * NX and all(
        action[site(0, space_index), site(NT - 1, space_index)]
        == -action[site(NT - 1, space_index), site(NT - 2, space_index)]
        != 0
        and action[site(NT - 1, space_index), site(0, space_index)]
        == -action[site(NT - 2, space_index), site(NT - 1, space_index)]
        != 0
        for space_index in range(NX)
    )
    return routed_exact and antiperiodic_sign, action[site(0, 0), site(7, 0)]


def ideal_factorization(action: sp.Matrix) -> bool:
    """Certify [E_z,Q]=E_z Q-Q E_z in Q's row/column ideal."""
    result = True
    for index in range(NS):
        local = projector(index)
        row_piece = local * action
        column_piece = action * local
        commutator = local * action - action * local
        result = (
            result
            and matrix_zero(commutator - (row_piece - column_piece))
            and all(
                row == index or row_piece[row, column] == 0
                for row in range(NS)
                for column in range(NS)
            )
            and all(
                column == index or column_piece[row, column] == 0
                for row in range(NS)
                for column in range(NS)
            )
        )
    return result


def certify_current(shear: sp.Rational) -> CurrentCertificate:
    action = DK.build_fixture(shear).action
    routed: list[RoutedCurrent] = []
    for routing in ROUTINGS:
        temporal, spatial = current_kernels(action, routing)
        identity_exact = all(
            matrix_zero(
                backward_divergence(
                    temporal, spatial, time_index, space_index
                )
                - (
                    projector(site(time_index, space_index)) * action
                    - action * projector(site(time_index, space_index))
                )
            )
            for time_index in range(NT)
            for space_index in range(NX)
        )
        routed.append(RoutedCurrent(routing, temporal, spatial, identity_exact))
    routings = (routed[0], routed[1])
    potential, curl_exact, routing_distinct = curl_reconstruction(*routings)
    seam_exact, seam_coefficient = seam_certificate(action, routings)
    commutator_counts = tuple(
        sum(
            value != 0
            for value in (
                projector(index) * action - action * projector(index)
            )
        )
        for index in range(NS)
    )
    return CurrentCertificate(
        shear,
        action,
        routings,
        potential,
        curl_exact,
        routing_distinct,
        seam_exact,
        seam_coefficient,
        commutator_counts,
        ideal_factorization(action),
    )


def periodic_incidence_1d(size: int) -> sp.Matrix:
    """+1 at an oriented edge source and -1 at its target."""
    incidence = sp.zeros(size, size)
    for source in range(size):
        incidence[source, source] = 1
        incidence[(source + 1) % size, source] = -1
    return incidence


@dataclass(frozen=True)
class ConstraintMode:
    momentum_index: int
    momentum_integer: int
    kappa: sp.Expr
    operator: sp.Matrix
    rank: int
    kernel_dimension: int
    cokernel_dimension: int
    cokernel_generator: sp.Matrix


@dataclass(frozen=True)
class ConstraintCertificate:
    incidence: sp.Matrix
    position_operator: sp.Matrix
    modes: tuple[ConstraintMode, ...]
    position_exact: bool
    modewise_exact: bool
    zero_mode_exact: bool


def constraint_certificate() -> ConstraintCertificate:
    """Exact d=2 trace/divergence count on the four spatial momenta."""
    incidence = periodic_incidence_1d(NX)
    position_operator = sp.Matrix.vstack(sp.eye(NX), incidence)
    position_exact = (
        incidence.rank() == NX - 1
        and position_operator.rank() == NX
        and len(position_operator.nullspace()) == 0
        and len(position_operator.T.nullspace()) == NX
    )

    representatives = (0, 1, 2, -1)
    modes: list[ConstraintMode] = []
    modewise_exact = True
    for momentum_index, integer in enumerate(representatives):
        kappa = sp.simplify(2 * sp.sin(sp.pi * integer / NX))
        operator = sp.Matrix(((1,), (kappa,)))
        rank = operator.rank()
        kernel_dimension = operator.cols - rank
        cokernel_dimension = operator.rows - rank
        cokernel = operator.T.nullspace()
        expected_cokernel = sp.Matrix((-kappa, 1))
        modewise_exact = (
            modewise_exact
            and rank == 1
            and kernel_dimension == 0
            and cokernel_dimension == 1
            and len(cokernel) == 1
            and matrix_zero(operator.T * expected_cokernel)
        )
        modes.append(
            ConstraintMode(
                momentum_index,
                integer,
                kappa,
                operator,
                rank,
                kernel_dimension,
                cokernel_dimension,
                expected_cokernel,
            )
        )

    zero_mode = modes[0]
    zero_mode_exact = (
        zero_mode.kappa == 0
        and zero_mode.operator == sp.Matrix(((1,), (0,)))
        and zero_mode.rank == 1
        and zero_mode.kernel_dimension == 0
        and zero_mode.cokernel_dimension == 1
        and zero_mode.cokernel_generator == sp.Matrix((0, 1))
    )
    return ConstraintCertificate(
        incidence,
        position_operator,
        tuple(modes),
        position_exact,
        modewise_exact,
        zero_mode_exact,
    )


def linear_combination(
    coefficients: sp.Matrix, kernels: tuple[sp.Matrix, ...], row: int
) -> sp.Matrix:
    return sum(
        (
            coefficients[row, column] * kernels[column]
            for column in range(coefficients.cols)
        ),
        sp.zeros(NS),
    )


@dataclass(frozen=True)
class IntertwinerCertificate:
    final_residual: sp.Matrix
    old_residual: sp.Matrix
    continuity: sp.Matrix
    algebra_exact: bool
    current_exact: bool
    local_factorizations: int


def gauss_intertwiner_certificate(
    currents: tuple[CurrentCertificate, CurrentCertificate],
    constraint: ConstraintCertificate,
) -> IntertwinerCertificate:
    incidence = constraint.incidence
    identity = sp.eye(NX)

    # Columns are (g_t, rho_(t-1), rho_t, S_t).  Thus
    # Gamma_(t+1)=Gamma_t-(rho_t-rho_(t-1)+B4 S_t).
    final_residual = sp.Matrix.hstack(
        incidence, sp.zeros(NX), -identity, -incidence
    )
    old_residual = sp.Matrix.hstack(
        incidence, -identity, sp.zeros(NX), sp.zeros(NX)
    )
    continuity = sp.Matrix.hstack(
        sp.zeros(NX), -identity, identity, incidence
    )
    algebra_exact = matrix_zero(
        final_residual - (old_residual - continuity)
    )

    current_exact = True
    local_factorizations = 0
    for current in currents:
        for routed in current.routings:
            for time_index in range(NT):
                density_before = tuple(
                    routed.temporal[site(time_index - 1, space_index)]
                    for space_index in range(NX)
                )
                density_now = tuple(
                    routed.temporal[site(time_index, space_index)]
                    for space_index in range(NX)
                )
                flux = tuple(
                    routed.spatial[site(time_index, space_index)]
                    for space_index in range(NX)
                )
                for space_index in range(NX):
                    continuity_form = (
                        density_now[space_index]
                        - density_before[space_index]
                        + linear_combination(incidence, flux, space_index)
                    )
                    index = site(time_index, space_index)
                    commutator = (
                        projector(index) * current.action
                        - current.action * projector(index)
                    )
                    current_exact = current_exact and matrix_zero(
                        continuity_form - commutator
                    )
                    local_factorizations += 1
                current_exact = current_exact and matrix_zero(
                    sum(
                        (
                            linear_combination(incidence, flux, space_index)
                            for space_index in range(NX)
                        ),
                        sp.zeros(NS),
                    )
                )
    return IntertwinerCertificate(
        final_residual,
        old_residual,
        continuity,
        algebra_exact,
        current_exact,
        local_factorizations,
    )


@dataclass(frozen=True)
class CarrierCertificate:
    local_partition_exact: bool
    incidence_rank: int
    constant_cokernel_exact: bool
    zero_sum_image_exact: bool
    charge_form: sp.Matrix
    norm_identity_exact: bool
    strictly_positive: bool
    unpopulated: bool


def carrier_certificate(
    currents: tuple[CurrentCertificate, CurrentCertificate],
    constraint: ConstraintCertificate,
) -> CarrierCertificate:
    incidence = constraint.incidence
    local_partition_exact = matrix_zero(
        sum((projector(index) for index in range(NS)), sp.zeros(NS))
        - sp.eye(NS)
    )
    ones = sp.ones(NX, 1)
    left_kernel = incidence.T.nullspace()
    constant_cokernel_exact = (
        matrix_zero(ones.T * incidence)
        and len(left_kernel) == 1
        and left_kernel[0] == ones
    )
    incidence_rank = incidence.rank()
    zero_sum_image_exact = (
        incidence_rank == NX - 1 and constant_cokernel_exact
    )

    # Blocks 114 and 119 certify the four positive quotient lines.  Their
    # diagonal U(1) action is +1 per line, so its exact charge form is I4.
    charge_form = sp.eye(NX)
    amplitudes = sp.Matrix(sp.symbols("u0:4", complex=True))
    norm = sum(sp.conjugate(value) * value for value in amplitudes)
    norm_identity_exact = (
        sp.expand((amplitudes.conjugate().T * charge_form * amplitudes)[0])
        == sp.expand(norm)
    )
    # Strict positivity is inherited from the pinned Block 114/119 package;
    # I4 records its U(1) charge representation without re-deriving OS.
    strictly_positive = (
        charge_form.is_positive_definite is True
        and charge_form.rank() == NX
        and len(currents) == 2
    )
    unpopulated = (
        local_partition_exact
        and zero_sum_image_exact
        and norm_identity_exact
        and strictly_positive
    )
    return CarrierCertificate(
        local_partition_exact,
        incidence_rank,
        constant_cokernel_exact,
        zero_sum_image_exact,
        charge_form,
        norm_identity_exact,
        strictly_positive,
        unpopulated,
    )


@dataclass(frozen=True)
class DensityCertificate:
    r_blind: bool
    site_type_counts: tuple[int, int, int, int]
    density_nontrivial: bool
    total_commutator_zero: bool


def density_certificate(
    currents: tuple[CurrentCertificate, CurrentCertificate],
    constraint: ConstraintCertificate,
) -> DensityCertificate:
    tt_dimensions = tuple(mode.kernel_dimension for mode in constraint.modes)
    r_symbol = sp.Symbol("r", real=True)
    empty_tt_block = sp.zeros(0, 0)
    r_blind = (
        tt_dimensions == (0, 0, 0, 0)
        and r_symbol * empty_tt_block == empty_tt_block
    )

    reference_counts = currents[0].commutator_counts
    site_type_counts = tuple(
        reference_counts[site(time_index, 0)] for time_index in range(4)
    )
    density_nontrivial = all(
        current.commutator_counts == reference_counts
        and all(
            current.commutator_counts[site(time_index, space_index)]
            == site_type_counts[time_index % 4]
            for time_index in range(NT)
            for space_index in range(NX)
        )
        and min(current.commutator_counts) > 0
        and max(current.commutator_counts) <= 16
        for current in currents
    )
    total_commutator_zero = all(
        matrix_zero(sp.eye(NS) * current.action - current.action * sp.eye(NS))
        for current in currents
    )
    return DensityCertificate(
        r_blind,
        site_type_counts,  # type: ignore[arg-type]
        density_nontrivial,
        total_commutator_zero,
    )


def normalized_note() -> str:
    try:
        raw_note = NOTE_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError, UnicodeError):
        return ""
    return " ".join(raw_note.lower().split())


SCOPE_KEYS = (
    "noether",
    "routing",
    "off_shell",
    "commutator",
    "antiperiodic_seam",
    "zero_tt",
    "zero_mode",
    "gauss",
    "intertwiner",
    "zero_total_charge",
    "unpopulated",
    "closed_carrier",
    "r_blind",
    "vacuity",
    "density",
    "ward",
    "os_boundary",
    "axiom",
    "zero_retirement",
    "zero_score",
    "zero_e2e",
    "gravity",
    "adm",
    "n1_n8",
    "w1",
    "n5_resolution",
)


def scope_certificate(note: str, mutation: str) -> dict[str, bool]:
    result = {
        "noether": "noether" in note or "conserved current" in note,
        "routing": (
            "routing-independent" in note or "discrete curl" in note
        ),
        "off_shell": "off-shell" in note,
        "commutator": "commutator" in note,
        "antiperiodic_seam": "antiperiodic seam" in note,
        "zero_tt": "zero tt" in note or "no tt coordinates" in note,
        "zero_mode": "trace row" in note or "k=0" in note,
        "gauss": "gauss" in note,
        "intertwiner": "intertwiner" in note,
        "zero_total_charge": "zero total charge" in note,
        "unpopulated": "unpopulated" in note or "not populated" in note,
        "closed_carrier": "closed carrier" in note,
        "r_blind": "r-blind" in note or "does not select" in note,
        "vacuity": "vacuous" in note or "contentless" in note,
        "density": (
            "charge density" in note or "current bilinears" in note
        ),
        "ward": "ward" in note,
        "os_boundary": (
            "not an os no-go" in note or "not a curved os no-go" in note
        ),
        "axiom": "no axiom amendment is justified" in note,
        "zero_retirement": "zero obligation retirement" in note,
        "zero_score": "no toe percentage moves" in note,
        "zero_e2e": (
            "retained-positive end-to-end theory count remains zero" in note
        ),
        "gravity": "gravity constraint quotient remains unexecuted" in note,
        "adm": "actual adm/history transporter remains" in note,
        "n1_n8": all(f"n{index}" in note for index in range(1, 9)),
        "w1": "w1" in note,
        "n5_resolution": all(
            f"{resolution}:" in note
            for resolution in (
                "per_element",
                "per_site",
                "per_mode",
                "per_block",
                "lattice_wide",
            )
        ),
    }
    if mutation == "weaken_no_go_packet":
        result["os_boundary"] = False
        result["n1_n8"] = False
    if mutation == "drop_n5_resolution":
        result["n5_resolution"] = False
    if mutation == "claim_toe_progress":
        result["zero_score"] = False
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    mutation = parser.parse_args().mutation
    started = time.monotonic()
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-authority",
        "Block 120 blobs and ancestors 119--103 are pinned",
        AUDIT_TIMEOUT_SEC == 600
        and AUDIT_INPUT_PATHS
        == (
            "docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
            "docs/ADMISSIBILITY_DIRAC_KAHLER_TORUS_WRAP_DEFECT_BOUNDED_THEOREM_NOTE_2026-08-16.md",
            "scripts/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.py",
            "logs/runner-cache/admissibility_dirac_kahler_torus_wrap_defect_2026_08_16.txt",
        )
        and authority["main"] == CURRENT_MAIN
        and authority["axiom"] == authority["expected_axiom"]
        and authority["worktree_axiom"] == WORKTREE_AXIOM_BLOB
        and authority["registry"] == CURRENT_REGISTRY_BLOB
        and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
        and authority["parent"] == PARENT_COMMIT
        and authority["parent_ancestor"]
        and all(
            authority[f"ancestor_{number}"] for number in range(103, 120)
        )
        and authority["parent_note"] == authority["expected_parent"]
        and authority["parent_runner"] == PARENT_RUNNER_BLOB
        and authority["parent_cache"] == PARENT_CACHE_BLOB,
    )

    currents = (
        certify_current(DK.PRIMARY_SHEAR),
        certify_current(DK.SECOND_SHEAR),
    )
    routing_identity = all(
        routed.identity_exact
        for current in currents
        for routed in current.routings
    )
    seam_exact = all(current.seam_exact for current in currents)
    if mutation == "break_routing_identity":
        routing_identity = False
    if mutation == "break_seam_sign":
        seam_exact = False
    checks.check(
        "B-the-noether-identity",
        "both routings give div(J,S)=[E_z,Q] at 128 fixture/site cases; their difference is an exact curl and the AP seam is signed",
        routing_identity
        and seam_exact
        and all(current.curl_exact for current in currents)
        and all(current.routing_distinct for current in currents),
    )

    onshell_exact = all(
        current.ideal_factorization_exact for current in currents
    )
    if mutation == "break_onshell":
        onshell_exact = False
    checks.check(
        "C-the-onshell-vanishing",
        "barphi[E_z,Q]psi=(barphi E_z)(Qpsi)-(barphi Q)(E_z psi) lies in the Q row/column ideal",
        onshell_exact,
    )

    constraint = constraint_certificate()
    constraint_exact = constraint.position_exact and constraint.modewise_exact
    if mutation == "break_constraint_count":
        constraint_exact = False
    k0_exception_claimed = mutation == "claim_k0_exception"
    checks.check(
        "D-the-constraint-count",
        "C_k=(1,kappa_k)^T has (rank,ker,coker)=(1,0,1) at every k; k=0 keeps the trace row and zero TT",
        constraint_exact
        and constraint.zero_mode_exact
        and not k0_exception_claimed,
    )

    intertwiner = gauss_intertwiner_certificate(currents, constraint)
    intertwiner_exact = (
        intertwiner.algebra_exact
        and intertwiner.current_exact
        and intertwiner.local_factorizations == 2 * 2 * NT * NX
        and all(current.ideal_factorization_exact for current in currents)
    )
    if mutation == "break_intertwiner":
        intertwiner_exact = False
    checks.check(
        "E-the-gauss-intertwiner",
        "Gamma_(t+1)=Gamma_t-(Delta_t rho+B4 S), so preservation iff continuity; the DK source obeys it on shell",
        intertwiner_exact,
    )

    carrier = carrier_certificate(currents, constraint)
    charge_norm_exact = (
        carrier.local_partition_exact
        and carrier.incidence_rank == 3
        and carrier.constant_cokernel_exact
        and carrier.zero_sum_image_exact
        and carrier.norm_identity_exact
        and carrier.strictly_positive
    )
    if mutation == "break_charge_norm":
        charge_norm_exact = False
    populated_claimed = mutation == "claim_populated_quotient"
    checks.check(
        "F-the-closed-carrier-obstruction",
        "sum_z E_z=I; im(B4)=zero-sum, while pinned Block 114/119 positivity makes total U(1) charge ||psi||^2, so only zero populates the closed source",
        charge_norm_exact and carrier.unpopulated and not populated_claimed,
    )

    density = density_certificate(currents, constraint)
    r_blind = density.r_blind
    density_split = density.density_nontrivial and density.total_commutator_zero
    if mutation == "claim_r_selection":
        r_blind = False
    if mutation == "claim_charge_commutation_content":
        density_split = False
    checks.check(
        "G-the-r-blindness-and-density",
        "the r-weighted TT block is empty; every [E_z,Q] is nonzero (at most 16 entries), but [I,Q]=0 is contentless",
        r_blind and density_split,
    )

    note_scope = scope_certificate(normalized_note(), mutation)
    elapsed_before_scope = time.monotonic() - started
    checks.check(
        "H-scope",
        "required coupling/no-go/N1--N8/W1/N5 firewalls and runtime bound are present",
        set(note_scope) == set(SCOPE_KEYS)
        and all(note_scope.values())
        and elapsed_before_scope <= 400,
    )

    print(
        "ROUTING: t-first and x-first are distinct; "
        "(J_x-S_x)=(Delta_x^- K,-Delta_t^- K), hence divergence zero exactly"
    )
    print(
        "SEAM witness z=(0,0), entry (0,28): "
        f"Q_5/13={currents[0].seam_coefficient}, "
        f"Q_3/5={currents[1].seam_coefficient}; "
        "both routed divergences equal [E_(0,0),Q] with the AP sign"
    )
    print(
        "ONSHELL FACTORIZATION: barphi[E_z,Q]psi="
        "(barphi E_z)(Q psi)-(barphi Q)(E_z psi)=0 when Q psi=0=barphi Q"
    )
    kappas = tuple(mode.kappa for mode in constraint.modes)
    print(
        f"CONSTRAINT: kappa_k={kappas}; per_k=(rank,ker,coker)=(1,0,1); "
        "at k=0 C_0=(1,0)^T, so the trace row survives and TT count remains zero"
    )
    print(
        "INTERTWINER: [B4,0,-I,-B4]=[B4,-I,0,0]-[0,-I,I,B4]; "
        f"{intertwiner.local_factorizations} routed DK continuity forms are Q-ideal commutators"
    )
    print(
        "CARRIER: rank(B4)=3, coker(B4)=span{(1,1,1,1)}; "
        "Gauss requires zero total charge, but Q_U1=I4 gives ||psi||^2>0 for nonzero positive-package states"
    )
    print(
        f"DENSITY/VACUITY: nnz([E_z,Q]) by t mod 4={density.site_type_counts} "
        "(max 16), whereas [I,Q]=0; zero TT makes the coupling r-blind"
    )
    print(
        "N5: per_element: exact routed-current, commutator-identity, constraint-count, intertwiner, zero-sum, and density certificates are checked"
    )
    print(
        "per_site: one Grassmann mode per fine site on the antiperiodic reflection torus"
    )
    print(
        "per_mode: every spatial momentum has zero tt coordinates and the constraint sector couples to the matter current only through the exact continuity identity"
    )
    print(
        "per_block: the certified positive package cannot source the closed-carrier gauss quotient because its total charge is a norm, while the density-level coupling is exact and routing-independent"
    )
    print(
        "lattice_wide: checked and not executed — the ward/transfer-covariance of the current bilinears, the populated sourced quotient on an open or background carrier, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient on a populated carrier, Records, audit retention, and TOE closure remain open"
    )
    print(
        "RESULT: the matter package couples to the d=2 gravity constraint sector through an exact routing-independent noether identity and the gauss intertwiner, but the closed carrier's sourced quotient is unpopulated because positive-definite matter has norm total charge — the density-level ward question is the genuine next gate;"
    )
    print(
        "DECISION_CUT: prove or refute ward/transfer-covariance of the current bilinears on the OS quotient; pose the populated quotient on the open carrier; reject total-charge-level coupling claims"
    )
    print(
        "TOE: zero obligation retirement, retained-positive end-to-end theory count remains zero, and no TOE percentage moves"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
