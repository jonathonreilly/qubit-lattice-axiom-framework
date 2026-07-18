#!/usr/bin/env python3
"""Cycle 282: bounded autonomous apparatus-law route on the Cycle-278 code.

A one-hot program token moves through an immutable physical role word under
one repeated reversible update.  The roles autonomously sequence arming,
Cycle-278 contact-pointer coupling, coherent amplification, fact correlation,
workspace uncomputation, and a close flag.  The role word, phase origin,
blank apparatus, and episode domain remain explicit supplied structure.

The close is a coherent candidate flag, not occurrence or a Record.  Repeated
update composition is not physical time.
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

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CONNECTED_EDGE_AUTONOMOUS_APPARATUS_LAW_CYCLE282_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0

IDLE = 0
INIT = 1
COUPLE = 2
AMPLIFY = 3
FACT = 4
UNAMPLIFY = 5
UNCOUPLE = 6
CLOSE = 7

ROLE_NAMES = {
    IDLE: "IDLE",
    INIT: "INIT",
    COUPLE: "COUPLE",
    AMPLIFY: "AMPLIFY",
    FACT: "FACT",
    UNAMPLIFY: "UNAMPLIFY",
    UNCOUPLE: "UNCOUPLE",
    CLOSE: "CLOSE",
}

PROGRAM = (
    INIT,
    COUPLE,
    AMPLIFY,
    FACT,
    UNAMPLIFY,
    UNCOUPLE,
    CLOSE,
    IDLE,
    IDLE,
    IDLE,
    IDLE,
    IDLE,
)


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
        check("the Cycle-282 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "cycle-278 connected physical-m2 code",
        "bounded autonomous local update",
        "one fixed repeated update",
        "physical role word",
        "one-hot program token",
        "supplied phase/role marker",
        "homogeneously generated state",
        "pointer initialization",
        "contact-pointer coupling",
        "coherent amplification",
        "close",
        "without host-side schedule control",
        "l=3,4,5",
        "held-out l=6",
        "all 24 proper-cubic frames",
        "local-check and wilson preservation",
        "actual cycle-230 contact/coin/stream",
        "deletion",
        "finite-register recurrence",
        "pointer is not a record",
        "compiler iteration is not physical time",
        "n1 — alternative-route enumeration",
        "n2 — condition-independence audit",
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
        "the note preserves the autonomous apparatus, marker, endpoint, scope, and N1-N8 contracts",
        not missing,
        missing,
    )


@dataclass(frozen=True)
class ApparatusState:
    phase: int
    ready: int
    pointer: int
    amplifier: int
    fact_no: int
    fact_yes: int
    close: int


BLANK = ApparatusState(0, 0, 0, 0, 0, 0, 0)


def autonomous_step(
    contact_active: int,
    state: ApparatusState,
    program: tuple[int, ...] = PROGRAM,
    disabled_roles: frozenset[int] = frozenset(),
    shift_enabled: bool = True,
) -> ApparatusState:
    """One fixed reversible update on the one-hot phase sector.

    `state.phase` is the occupied site of a physical one-hot token rail.  The
    immutable three-bit role marker at that site selects a reversible local
    gate.  No host chooses a different gate at different compositions.
    """

    if contact_active not in (0, 1):
        raise ValueError("contact_active must be a bit")
    if len(program) < 8 or any(role not in ROLE_NAMES for role in program):
        raise ValueError("invalid physical role word")
    if not 0 <= state.phase < len(program):
        raise ValueError("phase token outside the supplied rail")
    if any(
        bit not in (0, 1)
        for bit in (
            state.ready,
            state.pointer,
            state.amplifier,
            state.fact_no,
            state.fact_yes,
            state.close,
        )
    ):
        raise ValueError("apparatus registers must be bits")

    role = program[state.phase]
    if role in disabled_roles:
        role = IDLE
    next_state = state
    if role == INIT:
        next_state = replace(next_state, ready=next_state.ready ^ 1)
    elif next_state.ready:
        if role == COUPLE:
            next_state = replace(
                next_state, pointer=next_state.pointer ^ contact_active
            )
        elif role == AMPLIFY:
            next_state = replace(
                next_state,
                amplifier=next_state.amplifier ^ next_state.pointer,
            )
        elif role == FACT:
            next_state = replace(
                next_state,
                fact_no=next_state.fact_no ^ (1 - next_state.amplifier),
                fact_yes=next_state.fact_yes ^ next_state.amplifier,
            )
        elif role == UNAMPLIFY:
            next_state = replace(
                next_state,
                amplifier=next_state.amplifier ^ next_state.pointer,
            )
        elif role == UNCOUPLE:
            next_state = replace(
                next_state, pointer=next_state.pointer ^ contact_active
            )
        elif role == CLOSE:
            one_fact = next_state.fact_no ^ next_state.fact_yes
            clean = not next_state.pointer and not next_state.amplifier
            if one_fact and clean:
                next_state = replace(next_state, close=next_state.close ^ 1)

    next_phase = (
        (next_state.phase + 1) % len(program)
        if shift_enabled
        else next_state.phase
    )
    return replace(next_state, phase=next_phase)


def run_episode(
    contact_active: int,
    steps: int = 7,
    initial: ApparatusState = BLANK,
    program: tuple[int, ...] = PROGRAM,
    disabled_roles: frozenset[int] = frozenset(),
    shift_enabled: bool = True,
) -> tuple[ApparatusState, ...]:
    history = [initial]
    for _ in range(steps):
        history.append(
            autonomous_step(
                contact_active,
                history[-1],
                program,
                disabled_roles,
                shift_enabled,
            )
        )
    return tuple(history)


def exhaustive_permutation_controls() -> None:
    print("\nONE FIXED REVERSIBLE UPDATE / AUTONOMOUS SEQUENCE")
    programs = {"intended": PROGRAM}
    for role in (INIT, COUPLE, AMPLIFY, FACT, UNAMPLIFY, UNCOUPLE, CLOSE):
        programs[f"delete_{ROLE_NAMES[role]}"] = tuple(
            IDLE if candidate == role else candidate for candidate in PROGRAM
        )
    permutation_rows = []
    failures = []
    for label, program in programs.items():
        outputs = set()
        inputs = 0
        for contact in (0, 1):
            for phase in range(len(program)):
                for bits in product((0, 1), repeat=6):
                    state = ApparatusState(phase, *bits)
                    outputs.add((contact, autonomous_step(contact, state, program)))
                    inputs += 1
        row = {"program": label, "inputs": inputs, "unique_outputs": len(outputs)}
        permutation_rows.append(row)
        if len(outputs) != inputs:
            failures.append(row)

    histories = {contact: run_episode(contact) for contact in (0, 1)}
    expected = {
        0: ApparatusState(7, 1, 0, 0, 1, 0, 1),
        1: ApparatusState(7, 1, 0, 0, 0, 1, 1),
    }
    check(
        "one fixed repeated update is a permutation on the complete declared basis for the intended and single-role-deleted programs",
        not failures
        and all(histories[contact][-1] == expected[contact] for contact in (0, 1)),
        {
            "permutation_rows": permutation_rows,
            "role_sequence": tuple(ROLE_NAMES[role] for role in PROGRAM[:7]),
            "inactive_tail": len(PROGRAM) - 7,
            "final_states": {contact: histories[contact][-1] for contact in (0, 1)},
        },
    )
    check(
        "the autonomous episode correlates a one-hot fact and close, then clears pointer and amplifier on both contact branches",
        all(
            history[-1].close == 1
            and history[-1].pointer == 0
            and history[-1].amplifier == 0
            and history[-1].fact_no + history[-1].fact_yes == 1
            for history in histories.values()
        )
        and histories[0][-1].fact_no == 1
        and histories[1][-1].fact_yes == 1,
        {
            "inactive_branch": histories[0],
            "active_branch": histories[1],
            "host_selected_stage_actions": 0,
            "fixed_update_compositions": 7,
        },
    )


def marker_and_deletion_controls() -> None:
    print("\nROLE/PHASE MARKER / DELETION / FAITHFULNESS CONTROLS")
    active = run_episode(1)[-1]
    inactive = run_episode(0)[-1]
    deletion_rows = {}
    for role in (INIT, COUPLE, AMPLIFY, FACT, UNAMPLIFY, UNCOUPLE, CLOSE):
        deletion_rows[ROLE_NAMES[role]] = run_episode(
            1, disabled_roles=frozenset((role,))
        )[-1]
    split_data_deleted = run_episode(
        1, disabled_roles=frozenset((COUPLE, UNCOUPLE))
    )[-1]

    homogeneous_idle = (IDLE,) * len(PROGRAM)
    homogeneous_init = (INIT,) * len(PROGRAM)
    wrong_phase = replace(BLANK, phase=1)
    wrong_pointer = replace(BLANK, pointer=1)
    no_token = run_episode(1, shift_enabled=False)[-1]
    check(
        "the supplied phase origin and nonhomogeneous physical role word are load bearing and are not generated from a homogeneous blank",
        run_episode(1, program=homogeneous_idle)[-1].close == 0
        and run_episode(1, program=homogeneous_init)[-1].close == 0
        and run_episode(1, initial=wrong_phase)[-1].close == 0
        and run_episode(1, initial=wrong_pointer)[-1].close == 0
        and no_token.close == 0,
        {
            "intended_role_codes": PROGRAM,
            "role_marker_M2": 3 * len(PROGRAM),
            "one_hot_phase_token_M2": len(PROGRAM),
            "all_IDLE_close": run_episode(1, program=homogeneous_idle)[-1].close,
            "all_INIT_close": run_episode(1, program=homogeneous_init)[-1].close,
            "wrong_phase_close": run_episode(1, initial=wrong_phase)[-1].close,
            "nonblank_pointer_close": run_episode(1, initial=wrong_pointer)[-1].close,
            "shift_deleted_close": no_token.close,
            "homogeneous_generation_theorem": False,
        },
    )
    check(
        "role and gate deletions distinguish the bounded apparatus clauses and expose a split-coupling false close",
        deletion_rows["INIT"].close == 0
        and deletion_rows["AMPLIFY"].close == 0
        and deletion_rows["FACT"].close == 0
        and deletion_rows["UNAMPLIFY"].close == 0
        and deletion_rows["UNCOUPLE"].close == 0
        and deletion_rows["CLOSE"].close == 0
        and deletion_rows["COUPLE"].close == 0
        and split_data_deleted.close == 1
        and split_data_deleted.fact_no == 1
        and split_data_deleted.fact_yes == 0
        and active.close == inactive.close == 1,
        {
            "active_baseline": active,
            "inactive_baseline": inactive,
            "single_role_deletions": deletion_rows,
            "split_data_coupling_deletion": split_data_deleted,
            "split_data_coupling_false_NO_close": split_data_deleted.close,
        },
    )


def physical_code_and_state_controls() -> dict[int, c269.WilsonSubsystemCode]:
    print("\nCYCLE-278 SAME-CODE STATES / LEAKAGE / HELD SIZE")
    coefficients = c278.walsh_coefficients()
    expected = {None: Fraction(57, 64), 1: Fraction(13, 16), -1: Fraction(31, 32)}
    cache = {}
    rows = []
    failures = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        bs = c278.cell_bs(code, (0, 0, 0))
        terms = tuple(c278.pauli_product(bs, mask) for mask in range(64))
        matter_union = 0
        for b in bs:
            matter_union |= b.x | b.z
        leakage = sum(
            not term.commutes(row)
            for term in terms
            for row in code.local_checks + code.wilsons
        )
        state_failures = 0
        state_rows = 0
        for bits in product((0, 1), repeat=3):
            for bias in (None, 1, -1):
                stabilizers = c278.biased_rows(code, bits, bias)
                pivots, bad = c278.phase_reducer(stabilizers, code.qubits)
                values = c278.moments(bs, pivots, code.qubits)
                probability = c278.probability_from_moments(coefficients, values)
                state_failures += bool(bad)
                state_failures += probability != expected[bias]
                state_failures += run_episode(0)[-1].fact_no != 1
                state_failures += run_episode(1)[-1].fact_yes != 1
                state_rows += 1
        row = {
            "L": length,
            "state_rows": state_rows,
            "state_failures": state_failures,
            "local_check_or_Wilson_leakage": leakage,
            "matter_support_union": matter_union.bit_count(),
            "working_apparatus_M2": 6,
            "program_token_M2": len(PROGRAM),
            "role_marker_M2": 3 * len(PROGRAM),
            "apparatus_overhead_M2": 6 + 4 * len(PROGRAM),
            "total_block_M2": matter_union.bit_count() + 6 + 4 * len(PROGRAM),
            "data_working_support_M2": matter_union.bit_count() + 6,
            "maximum_declared_update_neighborhood_M2": (
                matter_union.bit_count() + 6 + 4 * len(PROGRAM)
            ),
            "uniform_yes_weight": str(expected[None]),
            "B0_plus_yes_weight": str(expected[1]),
            "B0_minus_yes_weight": str(expected[-1]),
        }
        rows.append(row)
        if not (
            state_rows == 24
            and state_failures == 0
            and leakage == 0
            and row["matter_support_union"] == 18
            and row["apparatus_overhead_M2"] == 54
            and row["total_block_M2"] == 72
            and row["data_working_support_M2"] == 24
            and row["maximum_declared_update_neighborhood_M2"] == 72
        ):
            failures.append(row)
    check(
        "the autonomous apparatus preserves every connected-code local check and Wilson sector and gives the Cycle-278 fact weights through held-out L=6",
        not failures,
        rows,
    )
    check(
        "the supplied apparatus block has constant overhead and bounded active support independent of torus size",
        not failures
        and all(row["apparatus_overhead_M2"] == 54 for row in rows)
        and all(row["data_working_support_M2"] == 24 for row in rows)
        and all(row["maximum_declared_update_neighborhood_M2"] == 72 for row in rows),
        {
            "rows": rows,
            "same_code": "Cycle-269/271/275/278 connected edge code only",
            "Cycle251_splice": False,
        },
    )
    return cache


def covariance_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nALL-24 / FULL-27 APPARATUS-CARRIED COVARIANCE")
    base_bs = c278.cell_bs(code, (0, 0, 0))
    local_family = set(code.local_checks)
    central_rows = list(code.local_checks + code.wilsons)
    central_pivots, central_bad = c278.phase_reducer(central_rows, code.qubits)
    failures = []
    tests = 0
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
                translation_edge[frame_edge[index]]
                for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(
                code.graph, vertex_map, edge_map
            )
            transformed_bs = tuple(
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in base_bs
            )
            target_cell = tuple(value % code.length for value in displacement)
            target_bs = c278.cell_bs(code, target_cell)
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
            if not (
                set(transformed_bs) == set(target_bs)
                and transformed_local == local_family
                and not central_bad
                and all(
                    not c278.reduce_pauli(
                        row, central_pivots, code.qubits
                    ).symplectic(code.qubits)
                    for row in transformed_wilsons
                )
                and run_episode(0)[-1].fact_no == 1
                and run_episode(1)[-1].fact_yes == 1
            ):
                failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "all 24 proper-cubic frames and the full 27-element L=3 translation group preserve the carried apparatus family",
        not failures and tests == 24 * 27,
        {
            "combined_tests": tests,
            "failures": failures[:5],
            "spatial_scalar": "Q_(N>=2)",
            "carried_data": "program block, role word, and phase origin",
            "homogeneous_unit_translation_generation": False,
        },
    )


def actual_update_and_stream_controls() -> None:
    print("\nACTUAL CYCLE-230 COIN/CONTACT/STREAM COMPATIBILITY")
    occupations = np.asarray([index.bit_count() for index in range(64)])
    q = np.diag((occupations >= 2).astype(float)).astype(complex)
    species = c219.common_species(c230.BETA)
    fock_coin = c229.fock_lift(species.coin)
    contact = np.diag(
        np.exp(1j * c230.COUPLING * occupations * (occupations - 1) / 2)
    )
    reverse = np.zeros((6, 6), dtype=complex)
    for source, target in enumerate((1, 0, 3, 2, 5, 4)):
        reverse[target, source] = 1
    fock_reverse = c229.fock_lift(reverse)

    stream_block = np.zeros((8, 8), dtype=complex)
    local_pair = np.zeros((8, 8), dtype=complex)
    for index in range(8):
        left = (index >> 0) & 1
        right = (index >> 1) & 1
        spectator = (index >> 2) & 1
        target = (index & ~0b11) | (left << 1) | (right << 0)
        stream_block[target, index] = -1 if left and right else 1
        local_pair[index, index] = left * spectator
    stream_commutator = local_pair @ stream_block - stream_block @ local_pair

    g_deleted = np.eye(64, dtype=complex)
    rho_n2 = np.zeros((64, 64), dtype=complex)
    rho_n2[3, 3] = 1
    rho_after_contact = contact @ rho_n2 @ contact.conj().T
    rho_after_deletion = g_deleted @ rho_n2 @ g_deleted.conj().T
    q_after_contact = int(round(float(np.trace(q @ rho_after_contact).real)))
    q_after_deletion = int(round(float(np.trace(q @ rho_after_deletion).real)))
    packet_after_contact = run_episode(q_after_contact)[-1]
    packet_after_deletion = run_episode(q_after_deletion)[-1]
    contact_deleted_same_apparatus = (
        np.linalg.norm(q @ g_deleted - g_deleted @ q) == 0
        and q_after_contact == q_after_deletion == 1
        and packet_after_contact == packet_after_deletion
    )
    check(
        "the apparatus effect commutes with the actual beta=-0.3 onsite coin, g=0.37 contact, and onsite reversal while preserving the one-particle mass fixture",
        np.linalg.norm(q @ fock_coin - fock_coin @ q) < 2e-14
        and np.linalg.norm(q @ contact - contact @ q) == 0
        and np.linalg.norm(q @ fock_reverse - fock_reverse @ q) == 0
        and np.all(np.diag(q)[occupations <= 1] == 0)
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "Q_coin_commutator": float(np.linalg.norm(q @ fock_coin - fock_coin @ q)),
            "Q_contact_commutator": float(np.linalg.norm(q @ contact - contact @ q)),
            "one_particle_pointer_action": "identity",
        },
    )
    check(
        "an actual intercell FSWAP changes a local contact-active condition, so stream/apparatus insertion order remains supplied",
        abs(np.linalg.norm(stream_commutator) - np.sqrt(2)) < 2e-14
        and abs(np.linalg.norm(stream_commutator, 2) - 1) < 2e-14,
        {
            "three_mode_FSWAP_commutator_Frobenius": float(
                np.linalg.norm(stream_commutator)
            ),
            "operator_norm": float(np.linalg.norm(stream_commutator, 2)),
            "declared_interface": "apparatus episode at a supplied boundary of the actual A/B stream schedule",
        },
    )
    check(
        "deleting the physical contact phase leaves the occupation-conditioned apparatus packet unchanged and therefore defeats a contact-occurrence claim",
        contact_deleted_same_apparatus
        and np.linalg.norm(contact - g_deleted) > 1,
        {
            "contact_deleted_matrix_residual": float(np.linalg.norm(contact - g_deleted)),
            "Q_after_contact": q_after_contact,
            "Q_after_contact_deletion": q_after_deletion,
            "apparatus_active_branch_after_contact": packet_after_contact,
            "apparatus_active_branch_after_contact_deletion": packet_after_deletion,
            "close_certifies_contact_application": False,
        },
    )


def recurrence_and_lawful_domain_controls() -> None:
    print("\nFINITE REGISTER RECURRENCE / LAWFUL DOMAIN / INTERPRETATION")
    rows = []
    for contact in (0, 1):
        history = run_episode(contact, steps=60)
        baseline = history[7]
        first_packet_change = next(
            index
            for index, state in enumerate(history[8:], start=8)
            if (state.fact_no, state.fact_yes, state.close)
            != (baseline.fact_no, baseline.fact_yes, baseline.close)
        )
        first_close_loss = next(
            index
            for index, state in enumerate(history[8:], start=8)
            if state.close != baseline.close
        )
        rows.append(
            {
                "contact": contact,
                "first_close_composition": 7,
                "first_packet_change": first_packet_change,
                "first_close_loss": first_close_loss,
                "program_period": len(PROGRAM),
            }
        )
    check(
        "finite-register recurrence preserves a bounded close episode but falsifies unrestricted permanence",
        all(row["first_packet_change"] == 28 for row in rows)
        and all(row["first_close_loss"] == 55 for row in rows),
        rows,
    )

    rejected = 0
    invalid = (
        (2, BLANK, PROGRAM),
        (1, replace(BLANK, phase=len(PROGRAM)), PROGRAM),
        (1, BLANK, (99,) * len(PROGRAM)),
    )
    for contact, state, program in invalid:
        try:
            autonomous_step(contact, state, program)
        except ValueError:
            rejected += 1
    check(
        "lawful-domain and Record/time firewalls remain explicit",
        rejected == len(invalid),
        {
            "rejected_controls": rejected,
            "supplied": "role word, phase origin/token, blanks, code states, repeated-update law, insertion boundary, trace/read effect, and finite episode domain",
            "pointer_is_Record": False,
            "fact_is_Record": False,
            "close_is_occurrence": False,
            "close_is_Record": False,
            "compiler_iteration_is_physical_time": False,
            "causal_depth_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    exhaustive_permutation_controls()
    marker_and_deletion_controls()
    cache = physical_code_and_state_controls()
    covariance_controls(cache[3])
    actual_update_and_stream_controls()
    recurrence_and_lawful_domain_controls()
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE282_BOUNDED_AUTONOMOUS_APPARATUS_EPISODE_GREEN"
        if FAIL == 0
        else "CYCLE282_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
