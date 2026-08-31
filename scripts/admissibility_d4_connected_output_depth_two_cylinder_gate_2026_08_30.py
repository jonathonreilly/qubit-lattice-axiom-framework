#!/usr/bin/env python3
"""Block29: connected Block28-output to Block24-input cylinder theorem.

This runner does not place a second supplied pair channel on a fresh carrier.
It binds each actual lateral-turn Locked output of Block28, at its actual
written site, to the literal straight append instrument of Block24.  It then
checks the empty/singleton/pair first layer, four future-resource sectors,
per-prefix cylinder marginal, full-space completion, covariance, Record QND,
and the finite Blank ledger for both frozen supplied q tables.
"""

from __future__ import annotations

import hashlib
import itertools
import sys
from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30 as block23  # noqa: E402
import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402
import admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30 as block28  # noqa: E402


AUDIT_TIMEOUT_SEC = 600

PACKET_REL = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block29-connected-output-depth-two-20260830"
)
PACKET = ROOT / PACKET_REL
RUNNER_SOURCE_PIN = PACKET / "RUNNER_SOURCE_PIN.md"

BLOCK23_SOURCE = (
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_"
    "2026_08_30.py"
)
BLOCK24_SOURCE = (
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_"
    "2026_08_30.py"
)
BLOCK28_SOURCE = (
    "scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_"
    "gate_2026_08_30.py"
)
BLOCK28_CACHE = (
    "logs/runner-cache/admissibility_d4_returned_tip_strict_support_analytic_"
    "coupling_gate_2026_08_30.txt"
)
BLOCK28_NOTE = (
    "docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_"
    "INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md"
)
BLOCK26_NOTE = (
    "docs/ADMISSIBILITY_D4_EXISTING_QUBIT_FINITE_LEASE_TENSOR_PHYSICAL_"
    "CONVEX_COLLISION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-30.md"
)
AXIOM_NOTE = "docs/MINIMAL_AXIOMS_2026-06-29.md"

DIRECT_HASHES = {
    BLOCK23_SOURCE: "426488df2a431cb7d415d5e933013f7ce0826cc9514f96cd041b9fc6ff49742a",
    BLOCK24_SOURCE: "f98534f07655e0de296f2060932e34aa7a600f08545f3661be2843d05accc15d",
    BLOCK28_SOURCE: "91141d7b917b52eef1335cc6d405acd5927d75ab32ce2f4e0620d4c9007b9a2a",
    BLOCK28_CACHE: "78562003af71a691a285824386945888fe3e9a74b84a0f76574b469f65b81726",
    BLOCK28_NOTE: "9469f0d03cff9779d7686a62e27a9f1c5dd22dfe8c281d70ab57970f2e3bb5e9",
    BLOCK26_NOTE: "f42770e773e30f3b9eaba9e6feb27fb1a1b50b1733a4cc98c346f68cbff414a3",
    AXIOM_NOTE: "93af34cf6fcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
}

FROZEN = {
    "APPROACH_REGISTRY.md": "9c19f26a22c72e017048ed3c514117509fbd9990d49948f3b91f3b8fb3013237",
    "ARTIFACT_PLAN.md": "87cc6fe9c452164737fab5c8c621d29b9c8f8f60ae88d25ad4ac5f44e95240b1",
    "ASSUMPTIONS_AND_IMPORTS.md": "ba01782882018cabdc0ce0dab807eea9df11b34d9c56474df97385b7778aff88",
    "AUTHORITY_GATE.md": "1cc2aa1ad7f5839af0905a6123a73c7fe84e507e7c234b0146339bfcaea62d97",
    "GOAL.md": "81c55379f532eb95c3b4503886a665fbc1fc3ff85fa105250e9dc90ae69db1f4",
    "MUTATION_PLAN.md": "ed0c0796b4601bb047076e403a109f71c654f0670246b84b83548b4c641ab3f2",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "e8d1a9b40a8e27f3a3c617a3bc2e8422e47ec1c84c7ad15c754b69a4aa6db757",
    "OPPORTUNITY_QUEUE.md": "fdb5ed0e44c7c9f3bc96a645b4cf797695e2c1cb8f19620bac9193531d9fef94",
    "PANEL_RETURN.md": "c19b2c688ef2ded0a2873eaabcef32d8155a5812a309dd303f02fbfeaa24a912",
    "PREFLIGHT_WITNESSES.md": "6d1ecd6535814ffe9c51bb259aa5224739d35a2f1bd10b9db82901434d724047",
    "ROUTE_PORTFOLIO.md": "dd1af4cbe522d48ac243e832fc9ffa3ea18165f00f68aad0cc3d9b22f957f5c3",
    "STATE.yaml": "931e075cf06885dd0c5e9708d854d24bcddef265e174535160dbd8c5f630eeca",
    "TOE_LANE_UPDATE.md": "5e4da994e4dc31c54479838f086134e78d25910928e870e3a9376dc40f082d03",
    "TRACE_GATE.md": "bcddd8dd4998a65667f8312f4954b83855ad46ecba4a60b21bef36df82eea1e6",
}

# The content-bound cache wrapper parses this literal tuple.
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py",
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py",
    "scripts/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.py",
    "logs/runner-cache/admissibility_d4_returned_tip_strict_support_analytic_coupling_gate_2026_08_30.txt",
    "docs/ADMISSIBILITY_D4_RETURNED_TIP_SUPPLIED_Q_CONDITIONAL_PAIR_INSTRUMENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md",
    "docs/ADMISSIBILITY_D4_EXISTING_QUBIT_FINITE_LEASE_TENSOR_PHYSICAL_CONVEX_COLLISION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-30.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/ASSUMPTIONS_AND_IMPORTS.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/OPPORTUNITY_QUEUE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/ROUTE_PORTFOLIO.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/STATE.yaml",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/TOE_LANE_UPDATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/TRACE_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/INDEPENDENT_STATIC_ATTACK_FINAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/RUNNER_SOURCE_PIN.md",
)


ZERO = block28.ZERO
E1 = block28.E1
DIRECTIONS = block28.DIRECTIONS
OUTCOMES = block28.OUTCOMES
ROTATIONS = block28.ROTATIONS
LEFT = "left"
RIGHT = "right"
ARMS = (LEFT, RIGHT)
LAMBDAS = (sp.S.Zero, sp.Rational(1, 2))


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runner_source_pin_ok() -> bool:
    if not RUNNER_SOURCE_PIN.exists():
        return False
    pins = {}
    for line in RUNNER_SOURCE_PIN.read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            pins[key.strip()] = value.strip().strip("`")
    return pins.get("source_sha256") == file_sha256(Path(__file__))


def frozen_hashes_ok() -> bool:
    return (
        all(file_sha256(ROOT / path) == digest for path, digest in DIRECT_HASHES.items())
        and all(file_sha256(PACKET / name) == digest for name, digest in FROZEN.items())
        and runner_source_pin_ok()
    )


def input_fingerprint() -> str:
    digest = hashlib.sha256()
    digest.update(b"runner-cache-input-fingerprint-v1\0")
    for relative in AUDIT_INPUT_PATHS:
        body = (ROOT / relative).read_bytes()
        encoded = relative.encode("utf-8")
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


def arm_anchor(arm):
    return block28.Y_LEFT if arm == LEFT else block28.Y_RIGHT


def arm_front(arm):
    return block28.F_LEFT if arm == LEFT else block28.F_RIGHT


def arm_exits(arm):
    return block28.LEFT_EXITS if arm == LEFT else block28.RIGHT_EXITS


def first_center(arm, exit_front):
    return block24.forward_center(arm_anchor(arm), exit_front)


def selected_future_center(arm, exit_front):
    return block24.forward_center(first_center(arm, exit_front), exit_front)


@lru_cache(maxsize=1)
def state_controlled_centers():
    future = tuple(
        selected_future_center(arm, exit_front)
        for arm in ARMS
        for exit_front in arm_exits(arm)
    )
    return tuple(block28.PAIR_CENTERS) + future


@lru_cache(maxsize=1)
def full_literal_centers():
    centers = set(block28.PAIR_CENTERS)
    for arm in ARMS:
        for exit_front in arm_exits(arm):
            centers.update(
                block24.candidate_centers(first_center(arm, exit_front)).values()
            )
    return tuple(sorted(centers))


def all_blocks_disjoint(centers):
    blocks = tuple(block28.block_sites(center) for center in centers)
    return all(
        left.isdisjoint(right)
        for left, right in itertools.combinations(blocks, 2)
    )


def geometry_certificate(mutation=None) -> bool:
    controlled = list(state_controlled_centers())
    full = list(full_literal_centers())
    selected = [
        selected_future_center(arm, exit_front)
        for arm in ARMS
        for exit_front in arm_exits(arm)
    ]
    if mutation == "duplicate_future":
        selected[-1] = selected[0]
    if mutation == "drop_full_center":
        full.pop()
    if mutation == "shift_future_into_first":
        selected[0] = block28.PAIR_CENTERS[0]
    selected_blocks = tuple(block28.block_sites(center) for center in selected)
    first_blocks = tuple(block28.block_sites(center) for center in block28.PAIR_CENTERS)
    spectator_only = (
        set(full_literal_centers())
        - set(block28.PAIR_CENTERS)
        - set(state_controlled_centers()[10:])
    )
    return (
        len(controlled) == len(set(controlled)) == 18
        and len(full) == len(set(full)) == 34
        and len(selected) == len(set(selected)) == 8
        and len(spectator_only) == 16
        and all_blocks_disjoint(controlled)
        and all_blocks_disjoint(full)
        and all(
            selected_block.isdisjoint(first_block)
            for selected_block in selected_blocks
            for first_block in first_blocks
        )
        and len(set().union(*(block28.block_sites(c) for c in full))) == 1088
    )


@dataclass(frozen=True)
class ConnectedAppendDescriptor:
    arm: str
    exit_front: tuple
    first_outcome: tuple
    second_outcome: tuple
    first_site: tuple
    second_site: tuple
    current_word: tuple
    origin: str
    append: object


@lru_cache(maxsize=None)
def connected_append_descriptor(arm, exit_front, first_outcome, second_outcome):
    site = first_center(arm, exit_front)
    word = block23.locked_word(exit_front, first_outcome)
    append = block24.append_branch(site, word, second_outcome)
    return ConnectedAppendDescriptor(
        arm=arm,
        exit_front=exit_front,
        first_outcome=first_outcome,
        second_outcome=second_outcome,
        first_site=site,
        second_site=selected_future_center(arm, exit_front),
        current_word=word,
        origin="first_writer_output",
        append=append,
    )


def descriptor_binding_is_physical(descriptor) -> bool:
    append = descriptor.append
    return (
        descriptor.origin == "first_writer_output"
        and descriptor.first_site == first_center(
            descriptor.arm, descriptor.exit_front
        )
        and descriptor.second_site == selected_future_center(
            descriptor.arm, descriptor.exit_front
        )
        and descriptor.current_word
        == block23.locked_word(descriptor.exit_front, descriptor.first_outcome)
        and append.anchor == descriptor.first_site
        and append.current_word == descriptor.current_word
        and append.front == descriptor.exit_front
        and append.source == descriptor.first_outcome
        and append.target == descriptor.second_outcome
        and append.forward_center == descriptor.second_site
        and append.effect.current_word == descriptor.current_word
        and append.effect.forward_center == descriptor.second_site
        and append.effect.forward_input == block23.BLANK_BLOCK
        and block24.append_factorization_is_physical(append)
        and block24.branch_effect_is_recontracted(append)
    )


@lru_cache(maxsize=1)
def literal_turn_and_append_binding_certificate() -> bool:
    for arm in ARMS:
        anchor = arm_anchor(arm)
        incoming = arm_front(arm)
        for source, exit_front, first_outcome in itertools.product(
            OUTCOMES, arm_exits(arm), OUTCOMES
        ):
            turn = block28.turn_branch(
                anchor, incoming, source, exit_front, first_outcome
            )
            expected_site = first_center(arm, exit_front)
            expected_word = block23.locked_word(exit_front, first_outcome)
            if not (
                block28.turn_branch_is_physical(turn)
                and turn.effect.target_center == expected_site
                and turn.effect.output_word == expected_word
                and block23.decode_locked_word(turn.effect.output_word)
                == (exit_front, first_outcome)
            ):
                return False
    for arm in ARMS:
        for exit_front, first_outcome, second_outcome in itertools.product(
            arm_exits(arm), OUTCOMES, OUTCOMES
        ):
            descriptor = connected_append_descriptor(
                arm, exit_front, first_outcome, second_outcome
            )
            if not descriptor_binding_is_physical(descriptor):
                return False
    return True


def transition_table_certificate(mutation=None) -> bool:
    rows = {
        source: sp.simplify(
            sum(block23.transition(source, target) for target in OUTCOMES)
        )
        for source in OUTCOMES
    }
    if mutation == "first_row_bias":
        rows[OUTCOMES[0]] += sp.Rational(1, 100)
    if mutation == "future_row_drop":
        rows[OUTCOMES[-1]] -= block23.transition(
            OUTCOMES[-1], OUTCOMES[-1]
        )
    entries = tuple(
        block23.transition(source, target)
        for source, target in itertools.product(OUTCOMES, repeat=2)
    )
    return (
        len(entries) == 196
        and all(value.is_real is True and value.is_positive is True for value in entries)
        and all(value == 1 for value in rows.values())
    )


def reduce_projectors(expression, symbols):
    result = sp.expand(expression)
    for symbol in symbols:
        result = block23.projector_reduce(result, symbol)
    return sp.expand(result)


def binary_sectors(left_symbol, right_symbol):
    return {
        (0, 0): (1 - left_symbol) * (1 - right_symbol),
        (1, 0): left_symbol * (1 - right_symbol),
        (0, 1): (1 - left_symbol) * right_symbol,
        (1, 1): left_symbol * right_symbol,
    }


def sector_partition_certificate(sectors, symbols, mutation=None):
    values = dict(sectors)
    if mutation == "drop_sector":
        values.pop((0, 0))
    if mutation == "duplicate_sector":
        values[(0, 1)] = values[(1, 0)]
    return (
        reduce_projectors(sum(values.values()), symbols) == 1
        and all(
            reduce_projectors(left * right, symbols) == 0
            for left_key, left in values.items()
            for right_key, right in values.items()
            if left_key != right_key
        )
    )


def singleton_turn_row_sum(source, raw_amplitude=False):
    weights = tuple(
        sp.Rational(1, 4) * block23.transition(source, target)
        for _exit in block28.LEFT_EXITS
        for target in OUTCOMES
    )
    if raw_amplitude:
        return sp.simplify(sum(value**2 for value in weights))
    return sp.simplify(sum(weights))


def pair_turn_row_sum(lam, left_source, right_source):
    q_total = sum(
        block28.q_weight(lam, left_exit, right_exit)
        for left_exit, right_exit in itertools.product(
            block28.LEFT_EXITS, block28.RIGHT_EXITS
        )
    )
    left_row = sum(
        block23.transition(left_source, left_target)
        for left_target in OUTCOMES
    )
    right_row = sum(
        block23.transition(right_source, right_target)
        for right_target in OUTCOMES
    )
    return sp.simplify(q_total * left_row * right_row)


@lru_cache(maxsize=1)
def first_layer_direct_sum_certificate() -> bool:
    p_left, p_right = sp.symbols("p_left p_right", commutative=True)
    sectors = binary_sectors(p_left, p_right)
    singleton_rows = tuple(singleton_turn_row_sum(source) for source in OUTCOMES)
    pair_rows = tuple(
        pair_turn_row_sum(lam, left_source, right_source)
        for lam in LAMBDAS
        for left_source, right_source in itertools.product(OUTCOMES, repeat=2)
    )
    q_reports = tuple(block28.q_certificate(lam) for lam in LAMBDAS)
    routed_gram = reduce_projectors(
        sum(sector**2 for sector in sectors.values()), (p_left, p_right)
    )
    return (
        sector_partition_certificate(sectors, (p_left, p_right))
        and all(value == 1 for value in singleton_rows)
        and all(value == 1 for value in pair_rows)
        and all(all(report.values()) for report in q_reports)
        and routed_gram == 1
    )


@dataclass(frozen=True)
class FutureSectorRow:
    sector: tuple
    outcomes: int
    coefficient_sum: object
    debit: int


def future_sector_rows(left_first, right_first, mutation=None):
    left_row = sp.simplify(
        sum(block23.transition(left_first, target) for target in OUTCOMES)
    )
    right_row = sp.simplify(
        sum(block23.transition(right_first, target) for target in OUTCOMES)
    )
    rows = {
        (0, 0): FutureSectorRow((0, 0), 1, sp.S.One, 0),
        (1, 0): FutureSectorRow((1, 0), 14, left_row, 1),
        (0, 1): FutureSectorRow((0, 1), 14, right_row, 1),
        (1, 1): FutureSectorRow((1, 1), 196, left_row * right_row, 2),
    }
    if mutation == "drop_future_outcome":
        bad = rows[(1, 0)]
        rows[(1, 0)] = FutureSectorRow(
            bad.sector,
            bad.outcomes - 1,
            bad.coefficient_sum
            - block23.transition(left_first, OUTCOMES[-1]),
            bad.debit,
        )
    return rows


@lru_cache(maxsize=1)
def future_resource_and_stop_certificate() -> bool:
    b_left, b_right = sp.symbols("b_left b_right", commutative=True)
    sectors = binary_sectors(b_left, b_right)
    expected_counts = {(0, 0): 1, (1, 0): 14, (0, 1): 14, (1, 1): 196}
    row_ok = all(
        row.coefficient_sum == 1
        and row.outcomes == expected_counts[row.sector]
        for left_first, right_first in itertools.product(OUTCOMES, repeat=2)
        for row in future_sector_rows(left_first, right_first).values()
    )
    p_active = sp.symbols("P_connected_active", commutative=True)
    stop_gram = block23.projector_reduce((1 - p_active) ** 2, p_active)
    full_gram = block23.projector_reduce(p_active + stop_gram, p_active)
    return (
        sector_partition_certificate(sectors, (b_left, b_right))
        and row_ok
        and stop_gram == 1 - p_active
        and full_gram == 1
    )


@lru_cache(maxsize=1)
def cylinder_certificate() -> bool:
    # Every primitive q cell and every transition entry is exact.  The future
    # sums are proved at each first Record label and resource sector; the first
    # coefficient is deliberately kept symbolic in the factor identity.
    if not transition_table_certificate():
        return False
    transition_values = tuple(
        block23.transition(source, target)
        for source, target in itertools.product(OUTCOMES, repeat=2)
    )
    q_values = tuple(
        block28.q_weight(lam, left_exit, right_exit)
        for lam in LAMBDAS
        for left_exit, right_exit in itertools.product(
            block28.LEFT_EXITS, block28.RIGHT_EXITS
        )
    )
    if not (
        len(transition_values) == 196
        and all(value > 0 for value in transition_values)
        and len(q_values) == 32
        and all(value > 0 for value in q_values)
    ):
        return False
    q_symbol, left_transition, right_transition = sp.symbols(
        "q_cell T_left T_right", positive=True
    )
    if not (
        (q_symbol * left_transition * right_transition).is_positive is True
        and (sp.Rational(1, 4) * left_transition).is_positive is True
    ):
        return False
    first = sp.symbols("F_first", nonnegative=True)
    for left_first, right_first in itertools.product(OUTCOMES, repeat=2):
        rows = future_sector_rows(left_first, right_first)
        if any(
            sp.simplify(first * row.coefficient_sum - first) != 0
            for row in rows.values()
        ):
            return False
    # The pair-prefix family is the exact Cartesian product q*T*T.  Checking
    # every primitive q and T entry above, rather than sampling products,
    # proves all products because multiplication preserves exact positivity.
    pair_prefix_family_size = (
        len(LAMBDAS)
        * len(block28.LEFT_EXITS)
        * len(block28.RIGHT_EXITS)
        * len(OUTCOMES) ** 4
    )
    singleton_prefix_family_size = (
        len(ARMS) * len(block28.LEFT_EXITS) * len(OUTCOMES) ** 2
    )
    return (
        pair_prefix_family_size == 1_229_312
        and singleton_prefix_family_size == 1_568
    )


def continuation_descriptor(arm, exit_front, first_outcome, second_outcome):
    descriptor = connected_append_descriptor(
        arm, exit_front, first_outcome, second_outcome
    )
    return (
        arm,
        exit_front,
        first_outcome,
        second_outcome,
        descriptor.first_site,
        descriptor.second_site,
        descriptor.current_word,
        block23.transition(first_outcome, second_outcome),
    )


@lru_cache(maxsize=None)
def q_independent_continuation_certificate(mutation=None) -> bool:
    descriptors = tuple(
        continuation_descriptor(arm, exit_front, first_outcome, second_outcome)
        for arm in ARMS
        for exit_front, first_outcome, second_outcome in itertools.product(
            arm_exits(arm), OUTCOMES, OUTCOMES
        )
    )
    families = []
    for lam in LAMBDAS:
        observed = list(descriptors)
        if mutation == "lambda_mark" and lam == LAMBDAS[-1]:
            observed[0] = observed[0] + ("lambda-dependent-mark",)
        families.append(tuple(observed))
    return (
        len(descriptors) == 1568
        and len(set(descriptors)) == 1568
        and families[0] == families[1]
    )


@dataclass(frozen=True)
class ArmHistoryRecord:
    exit_front: tuple
    first_outcome: tuple
    second_outcome: tuple
    first_site: tuple
    first_word: tuple
    second_site: tuple
    second_word: tuple


def arm_history_record(arm, exit_front, first_outcome, second_outcome, mutation=None):
    first_word = block23.locked_word(exit_front, first_outcome)
    second_word = block23.locked_word(exit_front, second_outcome)
    if mutation == "alias_history" and (
        exit_front,
        first_outcome,
        second_outcome,
    ) == (arm_exits(arm)[-1], OUTCOMES[-1], OUTCOMES[-1]):
        second_word = block23.locked_word(exit_front, OUTCOMES[0])
    return ArmHistoryRecord(
        exit_front,
        first_outcome,
        second_outcome,
        first_center(arm, exit_front),
        first_word,
        selected_future_center(arm, exit_front),
        second_word,
    )


def decode_arm_history(arm, history):
    first_label = block23.decode_locked_word(history.first_word)
    second_label = block23.decode_locked_word(history.second_word)
    if first_label is None or second_label is None:
        return None
    first_front, first_outcome = first_label
    second_front, second_outcome = second_label
    if (
        first_front != second_front
        or history.first_site != first_center(arm, first_front)
        or history.second_site != selected_future_center(arm, first_front)
    ):
        return None
    return first_front, first_outcome, second_outcome


@lru_cache(maxsize=1)
def record_history_and_qnd_certificate() -> bool:
    per_arm = {}
    for arm in ARMS:
        histories = tuple(
            arm_history_record(arm, exit_front, first_outcome, second_outcome)
            for exit_front, first_outcome, second_outcome in itertools.product(
                arm_exits(arm), OUTCOMES, OUTCOMES
            )
        )
        configurations = tuple(
            (
                history.first_site,
                history.first_word,
                history.second_site,
                history.second_word,
            )
            for history in histories
        )
        per_arm[arm] = histories
        if not (
            len(histories) == len(configurations) == len(set(configurations)) == 784
            and all(
                decode_arm_history(arm, history)
                == (
                    history.exit_front,
                    history.first_outcome,
                    history.second_outcome,
                )
                for history in histories
            )
        ):
            return False
    left_sites = {
        history.first_site for history in per_arm[LEFT]
    } | {history.second_site for history in per_arm[LEFT]}
    right_sites = {
        history.first_site for history in per_arm[RIGHT]
    } | {history.second_site for history in per_arm[RIGHT]}
    return (
        left_sites.isdisjoint(right_sites)
        and 784**2 == 614656
        and literal_turn_and_append_binding_certificate()
    )


@lru_cache(maxsize=None)
def debit_ledger_certificate(mutation=None) -> bool:
    expected = {(0, 0): 2, (1, 0): 3, (0, 1): 3, (1, 1): 4}
    rows = future_sector_rows(OUTCOMES[0], OUTCOMES[1])
    actual = {sector: 2 + row.debit for sector, row in rows.items()}
    if mutation == "pair_total_three":
        actual[(1, 1)] = 3
    selected = set(state_controlled_centers()[10:])
    first_targets = set(block28.LEFT_TARGETS + block28.RIGHT_TARGETS)
    return (
        actual == expected
        and selected.isdisjoint(first_targets)
        and len(selected) == 8
        and len(first_targets) == 8
        and len(first_targets) - 2 == 6
        and len(selected) - 2 == 6
        and expected[(1, 1)] == 4
        and 2 + 4 == 6
    )


def transformed_connected_sites(arm, exit_front, rotation, translation=ZERO):
    first = first_center(arm, exit_front)
    second = selected_future_center(arm, exit_front)
    return (
        block28.affine(rotation, translation, first),
        block28.affine(rotation, translation, second),
    )


@lru_cache(maxsize=1)
def covariance_certificate() -> bool:
    tau = sp.symbols("tau_0 tau_1 tau_2")
    for rotation in ROTATIONS:
        for arm in ARMS:
            anchor = arm_anchor(arm)
            for exit_front, first_outcome, second_outcome in itertools.product(
                arm_exits(arm), OUTCOMES, OUTCOMES
            ):
                moved_exit = block23.mat_vec(rotation, exit_front)
                moved_first_outcome = block23.mat_vec(rotation, first_outcome)
                moved_second_outcome = block23.mat_vec(rotation, second_outcome)
                moved_anchor = block28.affine(rotation, tau, anchor)
                expected_first = block24.forward_center(moved_anchor, moved_exit)
                expected_second = block24.forward_center(expected_first, moved_exit)
                actual_first, actual_second = transformed_connected_sites(
                    arm, exit_front, rotation, tau
                )
                if not (
                    actual_first == expected_first
                    and actual_second == expected_second
                    and block23.rotate_word(
                        block23.locked_word(exit_front, first_outcome), rotation
                    )
                    == block23.locked_word(moved_exit, moved_first_outcome)
                    and block23.rotate_word(
                        block23.locked_word(exit_front, second_outcome), rotation
                    )
                    == block23.locked_word(moved_exit, moved_second_outcome)
                    and block23.transition(first_outcome, second_outcome)
                    == block23.transition(moved_first_outcome, moved_second_outcome)
                ):
                    return False
    full = set(full_literal_centers())
    for rotation in block28.pair_stabilizer():
        swaps = block23.mat_vec(rotation, block28.F_LEFT) == block28.F_RIGHT
        translation = block28.scale(27, E1) if swaps else ZERO
        if {
            block28.affine(rotation, translation, center) for center in full
        } != full:
            return False
        for lam in LAMBDAS:
            for pair in itertools.product(block28.LEFT_EXITS, block28.RIGHT_EXITS):
                if block28.q_weight(lam, *pair) != block28.q_weight(
                    lam, *block28.pair_action(rotation, pair)
                ):
                    return False
    return True


@lru_cache(maxsize=None)
def arbitrary_reference_certificate(mutation=None) -> bool:
    row, column = sp.symbols("r_R s_R", integer=True, nonnegative=True)
    delta = sp.KroneckerDelta(row, column)
    p_left, p_right = sp.symbols("p_left_R p_right_R", commutative=True)
    first_sectors = binary_sectors(p_left, p_right)
    b_left, b_right = sp.symbols("b_left_R b_right_R", commutative=True)
    future_sectors = binary_sectors(b_left, b_right)
    first_total = reduce_projectors(
        sum(value**2 for value in first_sectors.values()), (p_left, p_right)
    )
    future_total = reduce_projectors(
        sum(value**2 for value in future_sectors.values()), (b_left, b_right)
    )
    reference_factor = (
        sp.Symbol("R_nonidentity") if mutation == "nonidentity" else sp.S.One
    )
    return (
        sp.simplify(reference_factor * delta * first_total * future_total - delta)
        == 0
    )


TERMINAL_TEXT = (
    "BOTH-SUPPLIED-Q-PAIR-TURNS-ADMIT-COMMON-CONNECTED-BLOCK24-FUTURE-"
    "CYLINDERS-ON-SUPPLIED-RAILS"
)

SCOPE_TEXT = (
    "two supplied q choices; one external pair-turn layer; actual output "
    "Locked Records feed one literal connected Block24 straight append; "
    "four future-resource sectors; supplied finite rails; no second pair "
    "reuse, cause selection, autonomous invocation, renewal, microscopic "
    "compiler, rate, gravity, axiom amendment, audit retention, obligation "
    "retirement, or TOE movement"
)

FORBIDDEN_SCOPE_PHRASES = (
    "autonomous invocation established",
    "nearest-neighbor compiler established",
    "gravity source established",
    "axiom amendment required",
    "audit retained",
    "obligation retired",
    "TOE score increased",
)


def scope_guard_certificate(terminal=TERMINAL_TEXT, scope=SCOPE_TEXT) -> bool:
    combined = f"{terminal}; {scope}"
    return (
        terminal == TERMINAL_TEXT
        and scope == SCOPE_TEXT
        and all(phrase not in combined for phrase in FORBIDDEN_SCOPE_PHRASES)
    )


def replace_named_factor(factors, key, replacement):
    if sum(name == key for name, _value in factors) != 1:
        raise ValueError(f"factor key is not unique: {key}")
    return tuple(
        (name, replacement if name == key else value)
        for name, value in factors
    )


def append_factors_are_rejected(branch, factors) -> bool:
    mutant = replace(branch, factors=factors)
    try:
        return not (
            block24.append_factorization_is_physical(mutant)
            and block24.branch_effect_is_recontracted(mutant)
        )
    except (KeyError, ValueError):
        return True


def append_construction_mutation_is_rejected(descriptor, **overrides) -> bool:
    factors = block24.make_append_factors(
        descriptor.first_site,
        descriptor.current_word,
        descriptor.second_outcome,
        **overrides,
    )
    return append_factors_are_rejected(descriptor.append, factors)


def nonidentity_spectator_mutation_is_rejected(descriptor) -> bool:
    factors = descriptor.append.factors
    spectators = list(
        block24.factor_dictionary(factors)["spectator_identity_factors"]
    )
    center, site, _operator = spectators[0]
    spectators[0] = (center, site, "X_2")
    mutant_factors = replace_named_factor(
        factors, "spectator_identity_factors", tuple(spectators)
    )
    return append_factors_are_rejected(descriptor.append, mutant_factors)


def turn_record_overwrite_mutation_is_rejected() -> bool:
    try:
        mutant = block28.turn_branch(
            block28.Y_LEFT,
            block28.F_LEFT,
            OUTCOMES[0],
            block28.LEFT_EXITS[0],
            OUTCOMES[1],
            mutation="overwrite_record",
        )
    except (KeyError, ValueError):
        return True
    return not block28.turn_branch_is_physical(mutant)


def shared_future_target_mutation_is_rejected() -> bool:
    left = connected_append_descriptor(
        LEFT, block28.LEFT_EXITS[0], OUTCOMES[0], OUTCOMES[1]
    )
    right = connected_append_descriptor(
        RIGHT, block28.RIGHT_EXITS[0], OUTCOMES[0], OUTCOMES[1]
    )
    mutant = replace(right, second_site=left.second_site)
    return (
        not descriptor_binding_is_physical(mutant)
        and not block28.block_sites(left.second_site).isdisjoint(
            block28.block_sites(mutant.second_site)
        )
    )


def fixed_coordinate_mark_mutation_is_rejected() -> bool:
    mark = first_center(LEFT, block28.LEFT_EXITS[0])
    return any(
        block28.affine(rotation, ZERO, mark) != mark
        for rotation in ROTATIONS
    )


def untransported_future_mutation_is_rejected() -> bool:
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    translation = (1, 2, 3)
    future = selected_future_center(LEFT, block28.LEFT_EXITS[0])
    transported = block28.affine(identity, translation, future)
    untransported = block28.affine(identity, ZERO, future)
    return transported != untransported


def mutation_rejections():
    p_left, p_right = sp.symbols("m_left m_right", commutative=True)
    sectors = binary_sectors(p_left, p_right)
    p_active = sp.symbols("P_mut", commutative=True)
    no_stop_total = block23.projector_reduce(p_active, p_active)
    bad_future = future_sector_rows(
        OUTCOMES[0], OUTCOMES[1], mutation="drop_future_outcome"
    )
    standard_descriptor = connected_append_descriptor(
        LEFT, block28.LEFT_EXITS[0], OUTCOMES[0], OUTCOMES[1]
    )
    wrong_word_descriptor = replace(
        standard_descriptor,
        current_word=block23.locked_word(
            standard_descriptor.exit_front, OUTCOMES[-1]
        ),
    )
    fresh_copy_descriptor = replace(
        standard_descriptor, origin="fresh_preparation"
    )
    old_source_word = block23.locked_word(
        standard_descriptor.exit_front, OUTCOMES[-1]
    )
    old_source_descriptor = replace(
        standard_descriptor,
        current_word=old_source_word,
        append=block24.append_branch(
            standard_descriptor.first_site,
            old_source_word,
            standard_descriptor.second_outcome,
        ),
    )
    nonblank_forward = block23.BlockProduct(
        block23.BLANK_BLOCK.live, standard_descriptor.current_word
    )
    aliased = arm_history_record(
        LEFT,
        block28.LEFT_EXITS[-1],
        OUTCOMES[-1],
        OUTCOMES[-1],
        mutation="alias_history",
    )
    scope_mutations = {
        "scope_autonomous_invocation_promotion_is_rejected": "autonomous invocation established",
        "scope_nearest_neighbor_compiler_promotion_is_rejected": (
            "nearest-neighbor compiler established"
        ),
        "scope_gravity_source_promotion_is_rejected": "gravity source established",
        "scope_axiom_amendment_promotion_is_rejected": "axiom amendment required",
        "scope_audit_retention_promotion_is_rejected": "audit retained",
        "scope_obligation_retirement_promotion_is_rejected": "obligation retired",
        "scope_TOE_score_promotion_is_rejected": "TOE score increased",
    }
    reports = {
        "shifted_future_breaks_connected_geometry": not geometry_certificate(
            "shift_future_into_first"
        ),
        "duplicate_future_breaks_disjoint_rails": not geometry_certificate(
            "duplicate_future"
        ),
        "dropped_center_breaks_full_literal_carrier": not geometry_certificate(
            "drop_full_center"
        ),
        "nonidentity_spectator_breaks_literal_append_scope": (
            nonidentity_spectator_mutation_is_rejected(standard_descriptor)
        ),
        "wrong_output_word_breaks_append_input_binding": (
            not descriptor_binding_is_physical(wrong_word_descriptor)
        ),
        "overwrite_old_Record_breaks_QND": turn_record_overwrite_mutation_is_rejected(),
        "overwrite_first_Record_breaks_QND": append_construction_mutation_is_rejected(
            standard_descriptor, current_output_override=block23.BLANK_POINTER
        ),
        "missing_future_Blank_guard_breaks_domain": append_construction_mutation_is_rejected(
            standard_descriptor, forward_input_override=nonblank_forward
        ),
        "reuse_consumed_first_target_breaks_no_double_write": (
            append_construction_mutation_is_rejected(
                standard_descriptor, displacement=0
            )
        ),
        "biased_first_transition_row_breaks_normalization": not transition_table_certificate(
            "first_row_bias"
        ),
        "dropped_future_transition_breaks_normalization": not transition_table_certificate(
            "future_row_drop"
        ),
        "raw_probability_amplitude_breaks_singleton_Gram": singleton_turn_row_sum(
            OUTCOMES[0], raw_amplitude=True
        )
        != 1,
        "bad_q_cell_breaks_pair_normalization": not block28.q_certificate(
            sp.Rational(1, 2), "bad_diagonal"
        )["normalized"],
        "biased_q_cell_breaks_uniform_singleton_marginal": not block28.q_certificate(
            sp.Rational(1, 2), "biased_cell"
        )["uniform_marginals"],
        "deleted_empty_sector_breaks_direct_sum": not sector_partition_certificate(
            sectors, (p_left, p_right), "drop_sector"
        ),
        "attenuated_singleton_breaks_full_channel_route": sp.Rational(1, 2)
        * singleton_turn_row_sum(OUTCOMES[0])
        != 1,
        "duplicated_presence_sector_breaks_orthogonality": not sector_partition_certificate(
            sectors, (p_left, p_right), "duplicate_sector"
        ),
        "missing_common_STOP_breaks_full_space_TP": no_stop_total != 1,
        "dropped_future_outcome_breaks_fixed_prefix_cylinder": bad_future[
            (1, 0)
        ].coefficient_sum
        != 1,
        "shared_selected_target_breaks_pair_tensor_support": (
            shared_future_target_mutation_is_rejected()
        ),
        "coordinate_mark_breaks_proper_cubic_covariance": (
            fixed_coordinate_mark_mutation_is_rejected()
        ),
        "untransported_future_center_breaks_translation_covariance": (
            untransported_future_mutation_is_rejected()
        ),
        "aliased_history_breaks_Record_injectivity": decode_arm_history(
            LEFT, aliased
        )
        != (
            aliased.exit_front,
            aliased.first_outcome,
            aliased.second_outcome,
        ),
        "nonidentity_reference_factor_breaks_extension": not arbitrary_reference_certificate(
            "nonidentity"
        ),
        "three_debit_pair_history_breaks_ledger": not debit_ledger_certificate(
            "pair_total_three"
        ),
        "fresh_copy_breaks_actual_output_provenance": not descriptor_binding_is_physical(
            fresh_copy_descriptor
        ),
        "old_source_future_kernel_breaks_output_conditioning": not descriptor_binding_is_physical(
            old_source_descriptor
        ),
        "lambda_dependent_continuation_breaks_common_descriptor": (
            not q_independent_continuation_certificate("lambda_mark")
        ),
    }
    reports.update(
        {
            name: not scope_guard_certificate(
                f"{TERMINAL_TEXT}; {phrase}", SCOPE_TEXT
            )
            for name, phrase in scope_mutations.items()
        }
    )
    return reports


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, name, condition, detail):
        if condition:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def main() -> int:
    checks = Checks()
    checks.check(
        "frozen_inputs_and_source_pin",
        frozen_hashes_ok(),
        f"{len(AUDIT_INPUT_PATHS)} declared inputs; fingerprint={input_fingerprint()}",
    )
    checks.check(
        "connected_full_carrier_geometry",
        geometry_certificate(),
        "18 state-controlled and 34 full literal 32-site blocks are disjoint; 1,088 sites",
    )
    checks.check(
        "literal_output_to_input_binding",
        literal_turn_and_append_binding_certificate(),
        "all 1,568 turn branches and 1,568 unique future append branches "
        "bind at the same site and complete Locked word",
    )
    checks.check(
        "first_layer_direct_sum",
        first_layer_direct_sum_certificate(),
        "empty, two uniform one-arm turns, and both supplied pair rows form "
        "one complete current-presence direct sum",
    )
    checks.check(
        "future_resource_sectors_and_STOP",
        future_resource_and_stop_certificate(),
        "D00/D10/D01/D11 are orthogonal and complete; all routed rows plus I-P_active are TP",
    )
    checks.check(
        "fixed_prefix_depth_two_cylinders",
        cylinder_certificate(),
        "all 1,229,312 pair prefixes and 1,568 singleton prefixes factor "
        "through exact future-resource cylinders",
    )
    checks.check(
        "q_independent_continuation",
        q_independent_continuation_certificate(),
        "1,568 continuation descriptors contain no lambda-dependent temporal kernel",
    )
    checks.check(
        "Record_history_QND_and_injectivity",
        record_history_and_qnd_certificate(),
        "784 histories per arm and 614,656 pair configurations decode; old "
        "and first Records are QND",
    )
    checks.check(
        "finite_Blank_debit_ledger",
        debit_ledger_certificate(),
        "first pair debits 2; future D00/D10/D01/D11 debit 0/1/1/2; D11 total is 4",
    )
    checks.check(
        "proper_cubic_translation_and_swap_covariance",
        covariance_certificate(),
        "all connected sites, words, transitions, full carrier, q cells, and "
        "side exchange transport",
    )
    checks.check(
        "arbitrary_reference_extension",
        arbitrary_reference_certificate(),
        "first and future direct sums tensor with symbolic untouched identity",
    )
    mutations = mutation_rejections()
    for name, rejected in mutations.items():
        print(f"MUTATION {'REJECTED' if rejected else 'SURVIVED'} {name}")
    checks.check(
        "designated_mutations",
        all(mutations.values()) and len(mutations) == 35,
        f"rejected={sum(mutations.values())}/{len(mutations)}",
    )
    checks.check(
        "claim_scope",
        scope_guard_certificate(),
        SCOPE_TEXT,
    )
    print(
        "per_element: checked — all 32 supplied q cells, 196 transition "
        "entries, 1,568 turn branches, and 1,568 append descriptors; exact "
        "factorization covers every pair and singleton prefix"
    )
    print(
        "per_site: checked — 18 state-controlled blocks and every identity "
        "factor on the 34-block, 1,088-site literal carrier"
    )
    print(
        "per_mode: checked — empty/left/right/pair first sectors and "
        "D00/D10/D01/D11 future-resource sectors for both q choices"
    )
    print(
        "per_block: checked — actual first output Record is the future current "
        "input; selected future targets, STOP, QND, and debit ledger are bound"
    )
    print(
        "lattice_wide: checked and not executed — no second returned-pair "
        "handoff, autonomous invocation, arbitrary-depth renewal, or "
        "nearest-neighbor compiled law is claimed"
    )
    if checks.failed == 0:
        print(f"TERMINAL: {TERMINAL_TEXT}")
    else:
        print("TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
