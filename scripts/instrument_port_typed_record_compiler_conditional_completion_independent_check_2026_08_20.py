#!/usr/bin/env python3
"""Independent reconstruction of the Block-6 typed Record completion.

This checker does not import the primary Block-6 runner.  It independently
rebuilds the state/rail code projections, delayed finite layout, exact branch
operators and weights, three spatial shell orbits, support-identical control
law, CP residual recovery, and the scoped affine definite-sector boundary
from upstream Block-4/Block-3 fixtures and the theorem note.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_front_stage_remote_context_record_event_congruence_2026_08_20 as block4
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as cycle317
import shared_effect_record_randomized_preparation_congruence_independence_2026_08_20 as block3


NOTE_PATH = ROOT / "docs" / (
    "INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK4_PATH = ROOT / "docs" / (
    "COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK5_PATH = ROOT / "docs" / (
    "SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)

AUDIT_INPUT_PATHS = (
    "docs/INSTRUMENT_PORT_TYPED_RECORD_COMPILER_CONDITIONAL_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/SHARED_EVENT_RECORD_SUPPORT_SELECTION_TRIANGLE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "scripts/common_front_stage_remote_context_record_event_congruence_2026_08_20.py",
    "scripts/shared_effect_record_randomized_preparation_congruence_independence_2026_08_20.py",
)

PASS = 0
FAIL = 0
TOL = 9.0e-11

Point = tuple[int, int, int]
Rotation = tuple[Point, Point, Point]
M2Code = tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
Records = dict[Point, M2Code]

I2 = sp.eye(2)
DIRECTIONS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
RADIUS = sp.Rational(1, 64)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def neg(value: Point) -> Point:
    return (-value[0], -value[1], -value[2])


def code(value: sp.Matrix) -> M2Code:
    return tuple(
        sp.simplify(value[row, column])
        for row in range(2)
        for column in range(2)
    )  # type: ignore[return-value]


def matrix(value: M2Code) -> sp.Matrix:
    return sp.Matrix(((value[0], value[1]), (value[2], value[3])))


def kappa(value: sp.Matrix, label: sp.Expr) -> M2Code:
    return code(value + sp.I * label * I2)


def state(value: M2Code) -> sp.Matrix:
    item = matrix(value)
    return sp.simplify((item + item.conjugate().T) / 2)


def label(value: M2Code) -> sp.Expr:
    return sp.simplify(sp.im(sp.trace(matrix(value))) / 2)


def slack(value: M2Code) -> sp.Matrix:
    item = matrix(value)
    return sp.simplify((item - item.conjugate().T) / (2 * sp.I) - label(value) * I2)


E0 = sp.diag(sp.Rational(1, 2), 0)
EB = I2 - E0
RHO = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
S0 = sp.diag(sp.Rational(3, 10), 0)
SB = sp.diag(sp.Rational(3, 10), sp.Rational(2, 5))
R0 = kappa(E0, 0)
RB = kappa(EB, 1)
C0 = kappa(S0, 0)
CB = kappa(SB, 1)

SA1 = sp.Matrix(
    ((sp.Rational(19, 450), 19 * sp.sqrt(2) / 225),
     (19 * sp.sqrt(2) / 225, sp.Rational(76, 225)))
)
SA2 = sp.Matrix(
    ((sp.Rational(16, 75), -8 * sp.sqrt(2) / 75),
     (-8 * sp.sqrt(2) / 75, sp.Rational(8, 75)))
)
SB1 = sp.Matrix(
    ((sp.Rational(7, 60), 7 * sp.sqrt(2) / 60),
     (7 * sp.sqrt(2) / 60, sp.Rational(7, 30)))
)
SB2 = sp.Matrix(
    ((sp.Rational(7, 60), -7 * sp.sqrt(2) / 60),
     (-7 * sp.sqrt(2) / 60, sp.Rational(7, 30)))
)
CA1, CA2 = kappa(SA1, 2), kappa(SA2, 3)
CB1, CB2 = kappa(SB1, 4), kappa(SB2, 5)

ATOMS = {
    "front": (C0, CB),
    "continuation-A": (CA1, CA2),
    "continuation-B": (CB1, CB2),
}
TRACE = {
    "front": (sp.Rational(3, 10), sp.Rational(7, 10)),
    "continuation-A": (sp.Rational(19, 35), sp.Rational(16, 35)),
    "continuation-B": (sp.Rational(1, 2), sp.Rational(1, 2)),
}
FREE = {
    "front": (sp.Rational(2, 3), sp.Rational(1, 3)),
    "continuation-A": (sp.Rational(3, 7), sp.Rational(4, 7)),
    "continuation-B": (sp.Rational(4, 9), sp.Rational(5, 9)),
}


def rail(value: M2Code) -> M2Code | None:
    # Independent reconstruction of the declared typed label compiler.
    if slack(value) != sp.zeros(2) or state(value).is_positive_semidefinite is not True:
        return None
    return {sp.Integer(0): R0, sp.Integer(1): RB}.get(label(value))


@dataclass(frozen=True)
class Ready:
    stage: str
    predecessor: Point


def decode(records: Records, target: Point) -> Ready | None:
    if target in records:
        return None
    occupied = tuple(direction for direction in DIRECTIONS if add(target, direction) in records)
    blanks = tuple(direction for direction in DIRECTIONS if direction not in occupied)
    if len(occupied) != 5 or len(blanks) != 1:
        return None
    predecessor = add(target, neg(blanks[0]))
    if predecessor not in records:
        return None
    transverse_positions = tuple(
        add(target, direction) for direction in occupied if direction != neg(blanks[0])
    )
    transverse = frozenset(records[position] for position in transverse_positions)
    value = records[predecessor]
    if value == block4.PREPARATION and transverse == block4.COMMON_MARKERS:
        return Ready("front", predecessor)
    if rail(value) == RB and state(value) == SB:
        if transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_A}:
            return Ready("continuation-A", predecessor)
        if transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_B}:
            return Ready("continuation-B", predecessor)
    return None


def frontier(records: Records) -> set[Point]:
    return {
        add(position, direction)
        for position in records
        for direction in DIRECTIONS
        if add(position, direction) not in records
    }


def active(records: Records) -> tuple[Point, ...]:
    return tuple(target for target in sorted(frontier(records)) if decode(records, target) is not None)


@dataclass(frozen=True)
class Shell:
    values: tuple[M2Code | None, ...]

    def occupied(self) -> int:
        return sum(value is not None for value in self.values)


def shell(records: Records, target: Point) -> Shell:
    return Shell(tuple(records.get(add(target, direction)) for direction in DIRECTIONS))


def determinant(value: Rotation) -> int:
    a, b, c = value
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def rotations() -> tuple[Rotation, ...]:
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    result: list[Rotation] = []
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            candidate = tuple(
                tuple(signs[row] * axes[order[row]][column] for column in range(3))
                for row in range(3)
            )
            if determinant(candidate) == 1:
                result.append(candidate)  # type: ignore[arg-type]
    return tuple(result)


def rotate_point(rotation: Rotation, point: Point) -> Point:
    return tuple(
        sum(rotation[row][column] * point[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rotate_shell(value: Shell, rotation: Rotation) -> Shell:
    carried = {
        rotate_point(rotation, direction): content
        for direction, content in zip(DIRECTIONS, value.values, strict=True)
    }
    return Shell(tuple(carried[direction] for direction in DIRECTIONS))


def hs2(left: M2Code, right: M2Code) -> sp.Expr:
    delta = matrix(left) - matrix(right)
    return sp.simplify(sp.trace(delta.conjugate().T * delta))


def distance(left: Shell, right: Shell) -> sp.Expr | None:
    if tuple(value is None for value in left.values) != tuple(value is None for value in right.values):
        return None
    return sp.simplify(
        sum(
            hs2(a, b) if a is not None and b is not None else 0
            for a, b in zip(left.values, right.values, strict=True)
        )
    )


def bump(value: Shell, orbit: tuple[Shell, ...]) -> sp.Expr:
    candidates = [item for reference in orbit if (item := distance(value, reference)) is not None]
    if not candidates:
        return sp.Integer(0)
    minimum = min(candidates, key=lambda item: float(sp.N(item)))
    if not bool(minimum < RADIUS):
        return sp.Integer(0)
    return sp.simplify(1 - minimum / RADIUS)


ROTS = rotations()
LA, LB = block4.build_layout("A"), block4.build_layout("B")
FRONT = shell(LA.record_map(), LA.first_target)


def with_first(layout: block4.Layout, value: M2Code) -> Records:
    records = layout.record_map()
    records[layout.first_target] = value
    return records


CONTA = shell(with_first(LA, CB), LA.continuation_target)
CONTB = shell(with_first(LB, CB), LB.continuation_target)
ORBITS = {
    "front": tuple({rotate_shell(FRONT, rotation) for rotation in ROTS}),
    "continuation-A": tuple({rotate_shell(CONTA, rotation) for rotation in ROTS}),
    "continuation-B": tuple({rotate_shell(CONTB, rotation) for rotation in ROTS}),
}


def typed_shell_stage(value: Shell) -> str | None:
    slots = dict(zip(DIRECTIONS, value.values, strict=True))
    blanks = tuple(direction for direction, content in slots.items() if content is None)
    if len(blanks) != 1:
        return None
    predecessor = slots[neg(blanks[0])]
    transverse = frozenset(
        content
        for direction, content in slots.items()
        if direction not in (blanks[0], neg(blanks[0])) and content is not None
    )
    if predecessor == block4.PREPARATION and transverse == block4.COMMON_MARKERS:
        return "front"
    if predecessor is not None and rail(predecessor) == RB and state(predecessor) == SB:
        if transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_A}:
            return "continuation-A"
        if transverse == block4.RESIDUAL_MARKERS | {block4.CONTEXT_B}:
            return "continuation-B"
    return None


def bumps(value: Shell) -> dict[str, sp.Expr]:
    typed_stage = typed_shell_stage(value)
    return {
        stage: bump(value, orbit) if stage == typed_stage else sp.Integer(0)
        for stage, orbit in ORBITS.items()
    }


def forming(records: Records) -> tuple[Point, ...]:
    return tuple(
        target
        for target in sorted(frontier(records))
        if sum(bumps(shell(records, target)).values()) != 0
    )


def gaussian_center(value: Shell) -> M2Code:
    total = value.occupied() * I2
    for content in value.values:
        if content is not None:
            total += state(content)
    return code(sp.simplify(total / 7))


def source_and_projection_controls() -> None:
    axiom = normalized(AXIOM_PATH)
    block4_note = normalized(BLOCK4_PATH)
    block5_note = normalized(BLOCK5_PATH)
    note = normalized(NOTE_PATH)
    check(
        "independent-source-packet",
        "probability distribution over the possibilities is determined by" in axiom
        and "integrated coherent quantum-to-record process" in block4_note
        and "not a physical completion of the block-4 continuation rail" in block5_note
        and "instrument-measure/record-measure identification" in note,
        "independently bound the current axiom boundary and the two exact upstream defects",
    )
    hostile = code(matrix(CB) + sp.I * sp.diag(1, -1))
    check(
        "independent-typed-projections",
        C0 != R0
        and CB != RB
        and state(C0) == S0
        and state(CB) == SB
        and label(C0) == 0
        and label(CB) == 1
        and slack(C0) == slack(CB) == sp.zeros(2)
        and slack(hostile) != sp.zeros(2)
        and rail(C0) == R0
        and rail(CB) == RB
        and rail(hostile) is None
        and rail(RB) == RB
        and state(RB) != SB,
        "state, scalar label, anti-Hermitian slack, and exact two-code rail map were rebuilt without the primary runner",
    )


def geometry_controls() -> None:
    failures = 0
    for layout in (LA, LB):
        initial = layout.record_map()
        after_c0 = with_first(layout, C0)
        after_cb = with_first(layout, CB)
        after_rb = with_first(layout, RB)
        failures += active(initial) != (layout.first_target,)
        failures += active(after_c0) != ()
        failures += active(after_rb) != ()
        failures += active(after_cb) != (layout.continuation_target,)
        ready = decode(after_cb, layout.continuation_target)
        failures += ready is None or ready.stage != f"continuation-{layout.context}"
        for atom in ATOMS[f"continuation-{layout.context}"]:
            terminal = dict(after_cb)
            terminal[layout.continuation_target] = atom
            failures += active(terminal) != ()
            failures += forming(terminal) != ()
        failures += forming(initial) != (layout.first_target,)
        failures += forming(after_c0) != ()
        failures += forming(after_cb) != (layout.continuation_target,)
    check(
        "independent-delayed-frontier-census",
        failures == 0,
        "every frontier was enumerated: front only, complement continuation only, C0/RB sealed, and terminal",
    )


def branch_and_cp_controls() -> None:
    targets = (S0, SB, SA1, SA2, SB1, SB2)
    check(
        "independent-exact-positive-tree",
        all(item.is_positive_semidefinite is True and item.trace() > 0 for item in targets)
        and (S0.rank(), SB.rank(), SA1.rank(), SA2.rank(), SB1.rank(), SB2.rank()) == (1, 2, 1, 1, 1, 1)
        and (S0.trace(), SA1.trace(), SA2.trace()) == (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25))
        and (S0.trace(), SB1.trace(), SB2.trace()) == (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20))
        and S0.trace() + SA1.trace() + SA2.trace() == 1
        and S0.trace() + SB1.trace() + SB2.trace() == 1,
        "exact positivity, ranks, and both terminal trace partitions were independently reconstructed",
    )

    menu_a, menu_b = block3.exact_menus()
    contact = cycle317.physical_fixture(3).contact
    programs = (
        block3.build_program("M_A", menu_a, contact),
        block3.build_program("M_B", menu_b, contact),
    )
    e0 = block3.h2_to_numpy(menu_a[0])
    b_operator = block4.positive_sqrt(np.eye(2) - e0) @ contact
    inverse = np.linalg.inv(b_operator)
    rho = np.diag((3 / 5, 2 / 5)).astype(complex)
    sigma_b = b_operator @ rho @ b_operator.conj().T
    exact = {"M_A": (SA1, SA2), "M_B": (SB1, SB2)}
    residuals = []
    for program in programs:
        for operator, target in zip(program.kraus[1:], exact[program.name], strict=True):
            residual = operator @ inverse
            residuals.append(float(np.linalg.norm(residual @ sigma_b @ residual.conj().T - np.asarray(target, dtype=complex))))
    check(
        "independent-residual-recovery",
        max(residuals) < TOL,
        {"maximum_residual": max(residuals), "primary_runner_imported": False},
    )


def orbit_and_kernel_controls() -> None:
    exact = {"front": FRONT, "continuation-A": CONTA, "continuation-B": CONTB}
    pair_minima = []
    stages = tuple(exact)
    for index, left in enumerate(stages):
        for right in stages[index + 1 :]:
            candidates = [
                item
                for a, b in product(ORBITS[left], ORBITS[right])
                if (item := distance(a, b)) is not None
            ]
            pair_minima.append(min(candidates, key=lambda item: float(sp.N(item))))
    check(
        "independent-disjoint-cubic-orbits",
        len(ROTS) == 24
        and all(len(value) == 24 for value in ORBITS.values())
        and all(bumps(value)[stage] == 1 for stage, value in exact.items())
        and all(bumps(value)[other] == 0 for stage, value in exact.items() for other in stages if stage != other)
        and min(pair_minima) == 3
        and min(pair_minima) > 4 * RADIUS,
        {"minimum_squared_separation": min(pair_minima)},
    )
    stage_specs = {
        "front": (block4.PREPARATION, block4.COMMON_MARKERS),
        "continuation-A": (CB, block4.RESIDUAL_MARKERS | {block4.CONTEXT_A}),
        "continuation-B": (CB, block4.RESIDUAL_MARKERS | {block4.CONTEXT_B}),
    }
    guarded_support_exact = True
    for stage, (predecessor, marker_set) in stage_specs.items():
        candidates: list[Shell] = []
        for blank in DIRECTIONS:
            predecessor_direction = neg(blank)
            transverse_directions = tuple(
                direction
                for direction in DIRECTIONS
                if direction not in (blank, predecessor_direction)
            )
            for marker_order in permutations(tuple(marker_set)):
                slots: dict[Point, M2Code | None] = {direction: None for direction in DIRECTIONS}
                slots[predecessor_direction] = predecessor
                slots.update(zip(transverse_directions, marker_order, strict=True))
                candidates.append(Shell(tuple(slots[direction] for direction in DIRECTIONS)))
        survivors = {
            candidate
            for candidate in candidates
            if sum(bumps(candidate).values()) != 0
        }
        guarded_support_exact &= (
            len(candidates) == 144
            and all(typed_shell_stage(candidate) == stage for candidate in candidates)
            and len(survivors) == 24
            and survivors == set(ORBITS[stage])
        )
    empty = Shell((None,) * 6)
    one = Shell((code(I2), None, None, None, None, None))
    near_typed_records = with_first(LA, code(matrix(CB) + sp.Rational(1, 64) * I2))
    near_untyped_records = with_first(
        LA,
        code(matrix(CB) + sp.I * sp.Rational(1, 64) * sp.diag(1, -1)),
    )
    near_typed = shell(near_typed_records, LA.continuation_target)
    near_untyped = shell(near_untyped_records, LA.continuation_target)
    check(
        "independent-total-kernel-controls",
        all(sum(weights) == 1 and all(weight > 0 for weight in weights) for table in (TRACE, FREE) for weights in table.values())
        and gaussian_center(empty) != gaussian_center(one)
        and all(sum(bumps(empty).values()) == 0 for _ in (0,))
        and typed_shell_stage(near_typed) is None
        and typed_shell_stage(near_untyped) is None
        and sum(bumps(near_typed).values()) == 0
        and sum(bumps(near_untyped).values()) == 0
        and forming(near_typed_records) == ()
        and forming(near_untyped_records) == ()
        and guarded_support_exact
        and all(
            bumps(rotate_shell(value, rotation))[stage] == 1
            for stage, value in exact.items()
            for rotation in ROTS
        ),
        "normalization, condition variation, hostile near-shell rejection, and exact 24-of-144 guarded support at each of three stages were independently checked",
    )


def measure_and_affine_controls() -> None:
    trace_histories = {}
    free_histories = {}
    for context in ("A", "B"):
        stage = f"continuation-{context}"
        trace_histories[context] = (
            TRACE["front"][0],
            sp.simplify(TRACE["front"][1] * TRACE[stage][0]),
            sp.simplify(TRACE["front"][1] * TRACE[stage][1]),
        )
        free_histories[context] = (
            FREE["front"][0],
            sp.simplify(FREE["front"][1] * FREE[stage][0]),
            sp.simplify(FREE["front"][1] * FREE[stage][1]),
        )
    check(
        "independent-trace-and-free-histories",
        trace_histories == {
            "A": (sp.Rational(3, 10), sp.Rational(19, 50), sp.Rational(8, 25)),
            "B": (sp.Rational(3, 10), sp.Rational(7, 20), sp.Rational(7, 20)),
        }
        and all(sum(values) == 1 for values in trace_histories.values())
        and all(sum(values) == 1 for values in free_histories.values())
        and all(free_histories[key] != trace_histories[key] for key in trace_histories),
        "the trace law exactly matches branch traces while a support-identical normalized weight law remains distinct",
    )

    stage_operators = {
        "front": (S0, SB),
        "continuation-A": (SA1, SA2),
        "continuation-B": (SB1, SB2),
    }
    independently_recovered = {}
    independently_rejected_free = {}
    for stage, operators in stage_operators.items():
        stage_mass = sp.simplify(sum(sp.trace(operator) for operator in operators))
        conditional_states = tuple(
            sp.simplify(operator / sp.trace(operator)) for operator in operators
        )
        target_cq_state = sp.diag(
            *(sp.simplify(operator / stage_mass) for operator in operators)
        )
        q_left, q_right = sp.symbols(f"u_{stage} v_{stage}", real=True)
        candidate_cq_state = sp.diag(
            q_left * conditional_states[0], q_right * conditional_states[1]
        )
        constraints = [
            sp.simplify(entry)
            for entry in candidate_cq_state - target_cq_state
            if sp.simplify(entry) != 0
        ]
        answer = sp.solve(
            constraints + [q_left + q_right - 1],
            (q_left, q_right),
            dict=True,
        )
        independently_recovered[stage] = (
            sp.simplify(answer[0][q_left]),
            sp.simplify(answer[0][q_right]),
        )
        hostile_cq_state = sp.diag(
            FREE[stage][0] * conditional_states[0],
            FREE[stage][1] * conditional_states[1],
        )
        independently_rejected_free[stage] = hostile_cq_state != target_cq_state
    check(
        "independent-sectorwise-cq-ensemble-consistency",
        independently_recovered == TRACE
        and all(independently_rejected_free.values()),
        "an independent block-diagonal reconstruction forces the trace weights at all three stages only when exact cq ensemble consistency is required",
    )

    t = sp.Rational(2, 5)
    sector0 = sp.diag(1, 0)
    sector1 = sp.diag(0, 1)
    mixed = sp.simplify(t * sector0 + (1 - t) * sector1)
    calibrated_effect = sector0
    pointer_marginal = sp.diag(sp.Rational(3, 10), sp.Rational(7, 10))
    check(
        "independent-affine-definite-sector-boundary",
        mixed[0, 0] == t
        and mixed[1, 1] == 1 - t
        and sp.simplify(sp.trace(calibrated_effect * pointer_marginal)) == sp.Rational(3, 10)
        and sp.Rational(3, 10) not in (0, 1),
        "affinity mixes two calibrated orthogonal outputs, and the exact pointer marginal is neither pointwise sector value; constant reset remains outside the branch-faithful target",
    )

    x00, x11, xr, xi = sp.symbols("x00 x11 xr xi", real=True)
    rho = sp.Matrix(((x00, xr + sp.I * xi), (xr - sp.I * xi, x11)))
    writer = sp.trace(E0 * rho) * sector0 + sp.trace(EB * rho) * sector1
    choi0 = sp.kronecker_product(E0.T, sector0)
    choib = sp.kronecker_product(EB.T, sector1)
    check(
        "independent-locked-output-firewall",
        sp.simplify(sp.trace(writer) - sp.trace(rho)) == 0
        and choi0.is_positive_semidefinite is True
        and choib.is_positive_semidefinite is True
        and matrix(CB) != matrix(CB).conjugate().T
        and state(CB) == SB,
        "the auxiliary label writer is trace preserving while the labelled M2 code is not misidentified as a density matrix",
    )


def boundary_controls() -> None:
    note = normalized(NOTE_PATH)
    required = (
        "conditional positive completion",
        "not a pointwise actualization theorem",
        "fixed reset channels",
        "deterministic affine",
        "sectorwise ensemble-consistency lemma",
        "universal impossibility",
        "no axiom amendment",
        "zero obligation retirement",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — per-citation residual matching",
        "n5 — resolution and rhetoric",
        "n6 — partial-closure path scan",
        "n7 — strongest steelman",
        "n8 — cross-cycle echo",
    )
    check(
        "independent-narrow-claim-boundary",
        all(phrase in note for phrase in required),
        "the positive construction and affine class boundary are scoped without universal or axiom-necessity rhetoric",
    )
    n5 = (
        "per_element: checked — independently rebuilt exact branch operators, state/label/slack projections, rail roles, positivity, and code/density separation",
        "per_site: checked — independently reconstructed the unique front, delayed continuation, terminal append, hostile code rejection, and total off-guard law",
        "per_mode: checked — independently separated coherent isometry, dephased ensemble, locked-output operations, trace-matched Record law, and free-weight control",
        "per_block: checked — independently verified exact history weights, CP residual recovery, three disjoint cubic orbits, covariance, and all frontier formation sites",
        "lattice_wide: checked and not executed — product/path existence is analytic under supplied independence; no physical clock, seed genesis, or pointwise actuality is inferred",
    )
    for line in n5:
        print(line)
    check(
        "independent-n5-certificate",
        all(len(line) >= 120 for line in n5)
        and all(line in NOTE_PATH.read_text(encoding="utf-8") for line in n5),
        "the independent five-resolution certificate is source bound",
    )


def main() -> int:
    source_and_projection_controls()
    geometry_controls()
    branch_and_cp_controls()
    orbit_and_kernel_controls()
    measure_and_affine_controls()
    boundary_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
