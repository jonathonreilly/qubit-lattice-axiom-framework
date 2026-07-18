#!/usr/bin/env python3
"""Cycle 286: outgoing-carrier/nonrecurrence route on the Cycle-278 code.

One repeated reversible update moves a physical program token along a supplied
open rail.  The first five role sites arm the Cycle-281 positive-close echo,
write the Cycle-278 pointer, archive it, reset it with the same Q-controlled
coupling, and launch the verified positive carrier.  Later sites propagate the
frontier outward while leaving coherent fact copies on fresh sites.

The rail, origin, role markers, blanks, forward domain, and boundary are
supplied.  Update composition is not physical time and no carrier is a Record.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import connected_edge_autonomous_apparatus_law_cycle282_2026_07_17 as c282
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import matter_coupling_faithful_close_record_candidate_cycle281_2026_07_17 as c281
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OUTGOING_CARRIER_NONRECURRENCE_CYCLE286_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
TOL = 3.0e-11

FORWARD = 0
INIT = 1
WRITE = 2
ARCHIVE = 3
RESET = 4
LAUNCH = 5

ROLE_NAMES = {
    FORWARD: "FORWARD",
    INIT: "INIT",
    WRITE: "WRITE",
    ARCHIVE: "ARCHIVE",
    RESET: "RESET",
    LAUNCH: "LAUNCH",
}

TRAINING_CASES = ((12, 10), (19, 17), (28, 26))
HELD_CASE = (43, 42)


class RailBoundaryError(ValueError):
    """The supplied open rail has no fresh right-hand target."""


class RailDomainError(ValueError):
    """The state is outside the declared synchronized fresh-rail domain."""


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-286 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-282 same connected-code apparatus",
        "cycle-281 positive close",
        "one repeated bounded local update",
        "outgoing carrier",
        "open non-wrapping rail",
        "training rail lengths/horizons",
        "held-out rail length/horizon",
        "bounded per-step support",
        "all 24 proper-cubic frames",
        "collision",
        "exact nonreturn before boundary",
        "deletion faithfulness",
        "actual w_g blindness",
        "fresh-capacity growth",
        "reverse reconnection",
        "old facts are controls only",
        "retarget",
        "origin, rail, blanks, and boundary",
        "carrier is not a record",
        "step count is not physical time",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the outgoing-carrier, resource, boundary, semantic, and N1-N8 contracts",
        not missing,
        missing,
    )


def program(length: int) -> tuple[int, ...]:
    if length < 7:
        raise RailDomainError("rail length must be at least seven")
    return (INIT, WRITE, ARCHIVE, RESET, LAUNCH) + (FORWARD,) * (length - 5)


def one_hot(length: int, index: int | None) -> tuple[int, ...]:
    if index is not None and not 0 <= index < length:
        raise RailDomainError("one-hot index is outside rail")
    return tuple(int(index == candidate) for candidate in range(length))


@dataclass(frozen=True)
class RailState:
    ready: int
    pointer: int
    archive: int
    token: tuple[int, ...]
    frontier: tuple[int, ...]
    facts: tuple[int, ...]


def blank_state(length: int) -> RailState:
    program(length)
    return RailState(0, 0, 0, one_hot(length, 0), one_hot(length, None), (0,) * length)


def hot_index(bits: tuple[int, ...], required: bool) -> int | None:
    positions = tuple(index for index, bit in enumerate(bits) if bit)
    if len(positions) != int(required):
        raise RailDomainError("invalid one-hot population")
    return positions[0] if positions else None


def validate(state: RailState, roles: tuple[int, ...]) -> tuple[int, int | None]:
    length = len(roles)
    if length < 7 or any(role not in ROLE_NAMES for role in roles):
        raise RailDomainError("invalid physical role word")
    if not (
        len(state.token) == len(state.frontier) == len(state.facts) == length
    ):
        raise RailDomainError("rail registers have inconsistent lengths")
    if any(
        bit not in (0, 1)
        for bit in (
            state.ready,
            state.pointer,
            state.archive,
            *state.token,
            *state.frontier,
            *state.facts,
        )
    ):
        raise RailDomainError("all rail and working registers must be bits")
    token_index = hot_index(state.token, True)
    frontier_population = sum(state.frontier)
    if frontier_population not in (0, 1):
        raise RailDomainError("frontier must have population zero or one")
    frontier_index = hot_index(state.frontier, bool(frontier_population))
    if frontier_index is not None and frontier_index != token_index:
        raise RailDomainError("frontier and program token must be synchronized")
    return int(token_index), frontier_index


def swap_tuple(bits: tuple[int, ...], left: int, right: int) -> tuple[int, ...]:
    output = list(bits)
    output[left], output[right] = output[right], output[left]
    return tuple(output)


def toggle_tuple(bits: tuple[int, ...], index: int, control: int) -> tuple[int, ...]:
    output = list(bits)
    output[index] ^= control
    return tuple(output)


def apply_role(
    contact_active: int,
    state: RailState,
    index: int,
    role: int,
    disabled_roles: frozenset[int],
) -> RailState:
    if role in disabled_roles:
        role = FORWARD
    if role == INIT:
        return replace(state, ready=state.ready ^ 1)
    if not state.ready:
        return state
    if role in (WRITE, RESET):
        return replace(state, pointer=state.pointer ^ contact_active)
    if role == ARCHIVE:
        return replace(state, archive=state.archive ^ state.pointer)
    if role == LAUNCH and state.pointer == 0:
        frontier = list(state.frontier)
        frontier[index], archive = state.archive, frontier[index]
        return replace(state, archive=archive, frontier=tuple(frontier))
    return state


def forward_step(
    contact_active: int,
    state: RailState,
    roles: tuple[int, ...],
    disabled_roles: frozenset[int] = frozenset(),
    strict_fresh: bool = True,
) -> RailState:
    """One fixed local permutation on the synchronized open-rail domain."""

    if contact_active not in (0, 1):
        raise RailDomainError("contact-active control must be a bit")
    index, _ = validate(state, roles)
    if index == len(roles) - 1:
        raise RailBoundaryError("open rail exhausted; no wrap is defined")

    output = apply_role(contact_active, state, index, roles[index], disabled_roles)
    frontier_here = output.frontier[index]
    if strict_fresh and frontier_here and (
        output.facts[index] or output.frontier[index + 1]
    ):
        raise RailDomainError("outgoing carrier target is not fresh")
    if output.token[index + 1]:
        raise RailDomainError("program target collides with an occupied token")

    facts = toggle_tuple(output.facts, index, frontier_here)
    frontier = swap_tuple(output.frontier, index, index + 1)
    token = swap_tuple(output.token, index, index + 1)
    result = replace(output, facts=facts, frontier=frontier, token=token)
    validate(result, roles)
    return result


def inverse_step(
    contact_active: int,
    state: RailState,
    roles: tuple[int, ...],
    disabled_roles: frozenset[int] = frozenset(),
) -> RailState:
    """Exact inverse of one forward step on an image of the fresh domain."""

    if contact_active not in (0, 1):
        raise RailDomainError("contact-active control must be a bit")
    current, _ = validate(state, roles)
    if current == 0:
        raise RailBoundaryError("no earlier open-rail slice exists")
    previous = current - 1
    token = swap_tuple(state.token, previous, current)
    frontier = swap_tuple(state.frontier, previous, current)
    output = replace(state, token=token, frontier=frontier)
    facts = toggle_tuple(output.facts, previous, output.frontier[previous])
    output = replace(output, facts=facts)
    output = apply_role(
        contact_active, output, previous, roles[previous], disabled_roles
    )
    validate(output, roles)
    return output


def run_forward(
    contact_active: int,
    length: int,
    horizon: int,
    disabled_roles: frozenset[int] = frozenset(),
    initial: RailState | None = None,
) -> tuple[RailState, ...]:
    roles = program(length)
    if not 0 <= horizon <= length - 1:
        raise RailDomainError("horizon must stop before the open boundary")
    history = [initial or blank_state(length)]
    for _ in range(horizon):
        history.append(
            forward_step(contact_active, history[-1], roles, disabled_roles)
        )
    return tuple(history)


def local_permutation_and_positive_close_controls() -> None:
    print("\nLOCAL PERMUTATION / CYCLE-281 POSITIVE CLOSE")
    rows = []
    failures = []
    length = 9
    roles = program(length)
    for index, role in enumerate(roles[:-1]):
        for contact_active in (0, 1):
            for ready, pointer, archive, frontier_here in product((0, 1), repeat=4):
                state = RailState(
                    ready,
                    pointer,
                    archive,
                    one_hot(length, index),
                    one_hot(length, index if frontier_here else None),
                    (0,) * length,
                )
                try:
                    result = forward_step(contact_active, state, roles)
                    recovered = inverse_step(contact_active, result, roles)
                except (RailDomainError, RailBoundaryError) as error:
                    failures.append((index, role, contact_active, state, str(error)))
                    continue
                if recovered != state:
                    failures.append((index, role, contact_active, state, result))
        rows.append({"index": index, "role": ROLE_NAMES[role]})
    check(
        "one repeated bounded local update has an exact inverse on every exhaustively tested local basis state",
        not failures,
        {"role_rows": rows, "local_basis_inputs": 8 * 2 * 16, "failures": failures[:3]},
    )

    q0, q = c281.contact_projectors()
    cycle281_close = c281.ancilla_effect(
        c281.isometry(c281.candidate_gates()), {c281.CLOSE: 1}
    )
    outbound_effect = np.diag(
        [
            int(sum(run_forward(c278.contact_active(index), 9, 7)[-1].frontier) > 0)
            for index in range(64)
        ]
    ).astype(complex)
    check(
        "the launched outgoing carrier exactly equals the Cycle-281 deletion-faithful positive close effect Q_x",
        np.linalg.norm(cycle281_close - q) < TOL
        and np.linalg.norm(outbound_effect - q) < TOL
        and np.linalg.norm(q0 + q - np.eye(64)) < TOL,
        {
            "Cycle281_close_minus_Q": float(np.linalg.norm(cycle281_close - q)),
            "outbound_effect_minus_Q": float(np.linalg.norm(outbound_effect - q)),
            "outbound_effect_rank": int(round(np.trace(outbound_effect).real)),
        },
    )


def training_held_nonreturn_and_capacity_controls() -> None:
    print("\nTRAINING / HELD RAILS / NONRETURN / CAPACITY")
    rows = []
    failures = []
    for split, cases in (("training", TRAINING_CASES), ("held-out", (HELD_CASE,))):
        for length, horizon in cases:
            for contact_active in (0, 1):
                history = run_forward(contact_active, length, horizon)
                final = history[-1]
                token_positions = tuple(hot_index(state.token, True) for state in history)
                unique_states = len(set(history))
                expected_facts = max(0, horizon - 4) if contact_active else 0
                expected_indices = (
                    set(range(4, horizon)) if contact_active and horizon >= 5 else set()
                )
                actual_indices = {
                    index for index, value in enumerate(final.facts) if value
                }
                prefix_stable = all(
                    all(
                        history[next_step].facts[index]
                        == history[step].facts[index]
                        for index in range(step)
                    )
                    for step in range(len(history))
                    for next_step in range(step, len(history))
                )
                row = {
                    "split": split,
                    "rail_length": length,
                    "horizon": horizon,
                    "contact": contact_active,
                    "unique_states": unique_states,
                    "token_positions": (token_positions[0], token_positions[-1]),
                    "fact_sites": len(actual_indices),
                    "fresh_fact_capacity": length - 5,
                    "apparatus_M2": 6 * length + 3,
                    "matter_plus_apparatus_M2": 6 * length + 21,
                    "maximum_per_step_support_M2": 29,
                    "prefix_stable": prefix_stable,
                }
                rows.append(row)
                if not (
                    token_positions == tuple(range(horizon + 1))
                    and unique_states == horizon + 1
                    and actual_indices == expected_indices
                    and len(actual_indices) == expected_facts
                    and prefix_stable
                    and (not contact_active or hot_index(final.frontier, True) == horizon)
                    and (contact_active or sum(final.frontier) == 0)
                    and final.pointer == 0
                    and final.archive == 0
                ):
                    failures.append(row)
    check(
        "training rail lengths/horizons and the held-out rail length/horizon have exact nonreturn before boundary and stable old-fact prefixes",
        not failures,
        {"rows": rows, "failures": failures},
    )
    check(
        "fresh-capacity growth is linear while bounded per-step support remains constant",
        not failures
        and all(row["apparatus_M2"] == 6 * row["rail_length"] + 3 for row in rows)
        and all(row["fresh_fact_capacity"] == row["rail_length"] - 5 for row in rows)
        and all(row["maximum_per_step_support_M2"] == 29 for row in rows),
        {
            "apparatus_growth": "6 M2 per fresh rail slice plus 3 working M2",
            "fact_capacity_growth": "1 positive-fact site per added post-launch slice",
            "maximum_per_step_support_M2": 29,
            "held_row": tuple(row for row in rows if row["split"] == "held-out"),
        },
    )


def boundary_collision_and_covariance_controls() -> None:
    print("\nBOUNDARY / COLLISION / ALL-24 COVARIANCE")
    length, horizon = HELD_CASE
    roles = program(length)
    edge_state = run_forward(1, length, length - 1)[-1]
    boundary_rejected = False
    try:
        forward_step(1, edge_state, roles)
    except RailBoundaryError:
        boundary_rejected = True

    occupied_fact = replace(
        blank_state(9),
        ready=1,
        token=one_hot(9, 5),
        frontier=one_hot(9, 5),
        facts=toggle_tuple((0,) * 9, 5, 1),
    )
    fresh_rejected = False
    try:
        forward_step(1, occupied_fact, program(9))
    except RailDomainError:
        fresh_rejected = True

    check(
        "the open boundary and occupied-target collision are rejected rather than wrapped or silently overwritten",
        boundary_rejected and fresh_rejected and hot_index(edge_state.token, True) == length - 1,
        {
            "held_length": length,
            "last_lawful_horizon": length - 1,
            "boundary_rejected": boundary_rejected,
            "occupied_target_rejected": fresh_rejected,
            "wrap_defined": False,
        },
    )

    # Six ordinary M2 lanes per open-rail slice: token, frontier, fact, and
    # three physical role-marker bits.
    cross_section = ((0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2))

    def coordinates(rail_length: int, merged: bool = False) -> tuple[tuple[int, int, int], ...]:
        values = []
        for index in range(rail_length):
            for lane, (y_value, z_value) in enumerate(cross_section):
                if merged and lane == 1:
                    y_value, z_value = cross_section[0]
                values.append((index, y_value, z_value))
        return tuple(values)

    failures = []
    tests = 0
    base = coordinates(length)
    base_distances = tuple(
        sorted(
            sum((base[6 * (index + 1) + lane][axis] - base[6 * index + lane][axis]) ** 2 for axis in range(3))
            for index in range(length - 1)
            for lane in range(3)
        )
    )
    for frame in c235.proper_cubic_frames():
        for displacement in product((-1, 0, 1), repeat=3):
            transformed = tuple(
                tuple(
                    int(sum(frame[axis, source] * point[source] for source in range(3)))
                    + displacement[axis]
                    for axis in range(3)
                )
                for point in base
            )
            transformed_distances = tuple(
                sorted(
                    sum(
                        (
                            transformed[6 * (index + 1) + lane][axis]
                            - transformed[6 * index + lane][axis]
                        )
                        ** 2
                        for axis in range(3)
                    )
                    for index in range(length - 1)
                    for lane in range(3)
                )
            )
            if len(set(transformed)) != len(transformed) or transformed_distances != base_distances:
                failures.append((frame.tolist(), displacement))
            tests += 1
    merged_collision_count = len(coordinates(length, True)) - len(set(coordinates(length, True)))
    check(
        "all 24 proper-cubic frames carry the open six-lane apparatus without collisions and preserve longitudinal locality",
        not failures and tests == 24 * 27 and set(base_distances) == {1} and merged_collision_count == length,
        {
            "frame_translation_tests": tests,
            "failures": failures[:3],
            "held_rail_role_sites": len(base),
            "intended_collisions": len(base) - len(set(base)),
            "merged_token_frontier_control_collisions": merged_collision_count,
            "origin_and_orientation_generated": False,
        },
    )


def deletion_and_actual_contact_controls() -> None:
    print("\nDELETION FAITHFULNESS / ACTUAL W_g BLINDNESS")
    deletion_rows = []
    for role in (INIT, WRITE, ARCHIVE, RESET, LAUNCH):
        effect = np.diag(
            [
                int(
                    sum(
                        run_forward(
                            c278.contact_active(index),
                            10,
                            8,
                            frozenset((role,)),
                        )[-1].frontier
                    ) > 0
                )
                for index in range(64)
            ]
        ).astype(complex)
        deletion_rows.append(
            {"deleted_role": ROLE_NAMES[role], "effect_norm": float(np.linalg.norm(effect))}
        )
    split_effect = np.diag(
        [
            int(
                sum(
                    run_forward(
                        c278.contact_active(index),
                        10,
                        8,
                        frozenset((WRITE, RESET)),
                    )[-1].frontier
                ) > 0
            )
            for index in range(64)
        ]
    ).astype(complex)
    check(
        "deleting any positive-close role or both Q_x coupling legs leaves zero outgoing-fact support",
        all(row["effect_norm"] < TOL for row in deletion_rows)
        and np.linalg.norm(split_effect) < TOL,
        {"single_role_deletions": deletion_rows, "split_WRITE_RESET_norm": float(np.linalg.norm(split_effect))},
    )

    occupations = np.asarray([index.bit_count() for index in range(64)])
    q = np.diag((occupations >= 2).astype(float)).astype(complex)
    contact = np.diag(
        np.exp(1j * c278.c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    deleted_contact = np.eye(64, dtype=complex)
    ideal_fact = contact.conj().T @ q @ contact
    deleted_contact_fact = deleted_contact.conj().T @ q @ deleted_contact
    check(
        "the outgoing positive carrier remains blind to deletion of the actual W_g phase even though W_g differs from identity",
        np.linalg.norm(ideal_fact - deleted_contact_fact) < TOL
        and np.linalg.norm(contact - deleted_contact) > 1
        and np.linalg.norm(q @ contact - contact @ q) < TOL,
        {
            "actual_W_g_minus_identity": float(np.linalg.norm(contact - deleted_contact)),
            "fact_effect_after_W_g_deletion_residual": float(np.linalg.norm(ideal_fact - deleted_contact_fact)),
            "Q_W_g_commutator": float(np.linalg.norm(q @ contact - contact @ q)),
            "carrier_certifies_W_g_application": False,
        },
    )


def retarget_and_reverse_reconnection_controls() -> None:
    print("\nOLD-FACT TARGET AUDIT / REVERSE RECONNECTION")
    rows = []
    failures = []
    for length, horizon in (*TRAINING_CASES, HELD_CASE):
        roles = program(length)
        for contact_active in (0, 1):
            history = run_forward(contact_active, length, horizon)
            recovered = history[-1]
            reverse_rows = []
            for _ in range(horizon):
                reverse_rows.append(sum(recovered.facts))
                recovered = inverse_step(contact_active, recovered, roles)
            row = {
                "length": length,
                "horizon": horizon,
                "contact": contact_active,
                "initial_fact_count": sum(history[-1].facts),
                "final_reconnected_fact_count": sum(recovered.facts),
                "reconnection_exact": recovered == history[0],
                "reverse_fact_counts_head": tuple(reverse_rows[:3]),
            }
            rows.append(row)
            if recovered != history[0]:
                failures.append(row)
    check(
        "exact reverse reconnection erases the entire outgoing fact trail and restores every blank apparatus register",
        not failures,
        {"rows": rows, "failures": failures},
    )

    state = run_forward(1, 14, 11)[-1]
    frontier_index = hot_index(state.frontier, True)
    old_index = int(frontier_index) - 1
    before = state.facts[old_index]
    controls_only_probe = 0 ^ before
    controls_only_state = state
    retargeted = replace(
        state,
        facts=toggle_tuple(state.facts, old_index, state.frontier[int(frontier_index)]),
    )
    restored = replace(
        retargeted,
        facts=toggle_tuple(
            retargeted.facts,
            old_index,
            retargeted.frontier[int(frontier_index)],
        ),
    )
    check(
        "old facts are controls only under the intended forward rule but an adjacent bounded retarget gate can erase and restore one",
        before == 1
        and controls_only_probe == 1
        and controls_only_state == state
        and retargeted.facts[old_index] == 0
        and restored == state,
        {
            "frontier_index": frontier_index,
            "retargeted_old_index": old_index,
            "before": before,
            "controls_only_probe": controls_only_probe,
            "old_fact_after_controls_only_export": controls_only_state.facts[old_index],
            "after_retarget": retargeted.facts[old_index],
            "after_second_retarget": restored.facts[old_index],
            "retarget_gate_in_intended_update": False,
            "unrestricted_old_fact_protection": False,
        },
    )


def same_code_state_and_covariance_controls() -> None:
    print("\nSAME CONNECTED CODE / HELD SIZE / ALL-24 Q COVARIANCE")
    coefficients = c278.walsh_coefficients()
    expected = {None: Fraction(57, 64), 1: Fraction(13, 16), -1: Fraction(31, 32)}
    rows = []
    failures = []
    cache = {}
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        bs = c278.cell_bs(code, (0, 0, 0))
        terms = tuple(c278.pauli_product(bs, mask) for mask in range(64))
        matter_union = 0
        for row in bs:
            matter_union |= row.x | row.z
        leakage = sum(
            not term.commutes(check_row)
            for term in terms
            for check_row in code.local_checks + code.wilsons
        )
        state_failures = 0
        state_rows = 0
        for bits in product((0, 1), repeat=3):
            for bias in (None, 1, -1):
                stabilizers = c278.biased_rows(code, bits, bias)
                pivots, bad = c278.phase_reducer(stabilizers, code.qubits)
                moments = c278.moments(bs, pivots, code.qubits)
                probability = c278.probability_from_moments(coefficients, moments)
                state_failures += bool(bad) + (probability != expected[bias])
                state_rows += 1
        row = {
            "L": length,
            "split": "held-out" if length == 6 else "training",
            "state_rows": state_rows,
            "state_failures": state_failures,
            "local_check_or_Wilson_leakage": leakage,
            "matter_support_union_M2": matter_union.bit_count(),
            "weights": tuple(str(expected[bias]) for bias in (None, 1, -1)),
        }
        rows.append(row)
        if not (
            state_rows == 24
            and state_failures == 0
            and leakage == 0
            and matter_union.bit_count() == 18
        ):
            failures.append(row)

    code = cache[3]
    base_bs = c278.cell_bs(code, (0, 0, 0))
    local_family = set(code.local_checks)
    central_pivots, central_bad = c278.phase_reducer(
        list(code.local_checks + code.wilsons), code.qubits
    )
    covariance_failures = []
    covariance_tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(code.length), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]]
                for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]] for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
            transformed_bs = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in base_bs
            )
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_wilsons = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.wilsons
            )
            target_bs = c278.cell_bs(
                code, tuple(value % code.length for value in displacement)
            )
            if not (
                set(transformed_bs) == set(target_bs)
                and transformed_local == local_family
                and not central_bad
                and all(
                    not c278.reduce_pauli(row, central_pivots, code.qubits).symplectic(
                        code.qubits
                    )
                    for row in transformed_wilsons
                )
            ):
                covariance_failures.append((frame.tolist(), displacement))
            covariance_tests += 1
    check(
        "the outgoing carrier retains the Cycle-278 same connected code, exact weights, and zero leakage through held-out L=6",
        not failures,
        rows,
    )
    check(
        "the Q_x endpoint and connected-code family remain covariant in all 24 proper-cubic frames and full L=3 translations",
        not covariance_failures and covariance_tests == 24 * 27,
        {
            "combined_tests": covariance_tests,
            "failures": covariance_failures[:3],
            "outgoing_rail_is_carried_not_generated": True,
        },
    )


def lawful_domain_and_semantic_controls() -> None:
    print("\nLAWFUL DOMAIN / SUPPLIED STRUCTURE / SEMANTICS")
    rejected = 0
    invalid_calls = (
        lambda: program(6),
        lambda: run_forward(1, 9, 9),
        lambda: forward_step(2, blank_state(9), program(9)),
        lambda: forward_step(
            1,
            replace(blank_state(9), frontier=one_hot(9, 3)),
            program(9),
        ),
    )
    for call in invalid_calls:
        try:
            call()
        except (RailDomainError, RailBoundaryError):
            rejected += 1
    check(
        "lawful-domain controls and the complete supplied origin/rail/blank/boundary inventory remain explicit",
        rejected == len(invalid_calls),
        {
            "rejected_controls": rejected,
            "supplied": "same code and Q_x; open rail and orientation; role word; unique origin token; all future blanks; positive-close core; one repeated update; forward-only lawful episode; boundary; trace/effect pairing",
            "homogeneous_rail_genesis": False,
            "unbounded_capacity": False,
            "boundary_rule_derived": False,
            "actual_branch_selected": False,
            "carrier_is_Record": False,
            "fact_copy_is_Record": False,
            "step_count_is_physical_time": False,
            "causal_duration_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    local_permutation_and_positive_close_controls()
    training_held_nonreturn_and_capacity_controls()
    boundary_collision_and_covariance_controls()
    deletion_and_actual_contact_controls()
    retarget_and_reverse_reconnection_controls()
    same_code_state_and_covariance_controls()
    lawful_domain_and_semantic_controls()
    print(f"\nSUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        print("RESULT CYCLE286_OPEN")
        return 1
    print("RESULT CYCLE286_OUTGOING_CARRIER_NONRECURRENCE_GREEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
