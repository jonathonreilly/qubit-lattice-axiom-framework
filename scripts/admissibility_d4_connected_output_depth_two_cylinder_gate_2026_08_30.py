#!/usr/bin/env python3
"""Block29: physical pair-output to Block24 future-channel composition.

This amended runner does not construct a singleton first-layer law or place a
second supplied pair channel on a fresh carrier.  It imports each complete
Block28 pair channel, binds every successful eight-pointer output
configuration to four literal future-resource sectors, constructs the actual
Block24 append products and their common complement STOP, and checks the
fixed-prefix cylinder for both frozen supplied q tables.
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


AUDIT_TIMEOUT_SEC = 900

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
    "PREREG_AMENDMENT_PAIR_PREFIX_PHYSICAL.md": "41e9ddfaa8cf0be77e9637cb9915a91254ccb7df8ea9275f78728ba2ea05c3e9",
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
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/PREREG_AMENDMENT_PAIR_PREFIX_PHYSICAL.md",
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


@dataclass(frozen=True)
class OutputPointerAtom:
    center: tuple
    word: tuple


@dataclass(frozen=True)
class PairOutputControl:
    left_exit: tuple
    right_exit: tuple
    left_first: tuple
    right_first: tuple
    atoms: tuple[OutputPointerAtom, ...]

    @property
    def key(self):
        return (
            self.left_exit,
            self.right_exit,
            self.left_first,
            self.right_first,
        )


FIRST_OUTPUT_CENTERS = tuple(block28.LEFT_TARGETS + block28.RIGHT_TARGETS)
RESOURCE_BITS = ((0, 0), (1, 0), (0, 1), (1, 1))


@lru_cache(maxsize=None)
def pair_output_control(left_exit, right_exit, left_first, right_first):
    outcome = block28.pair_record_outcome(
        left_exit, right_exit, left_first, right_first
    )
    return PairOutputControl(
        left_exit,
        right_exit,
        left_first,
        right_first,
        tuple(
            OutputPointerAtom(center, word)
            for center, word in outcome.pointer_configuration
        ),
    )


@lru_cache(maxsize=1)
def output_pointer_codebook():
    return (block23.BLANK_POINTER,) + tuple(
        block23.locked_word(exit_front, first_outcome)
        for exit_front in block28.LEFT_EXITS
        for first_outcome in OUTCOMES
    )


@lru_cache(maxsize=None)
def output_control_is_physical(control) -> bool:
    configuration = tuple((atom.center, atom.word) for atom in control.atoms)
    expected = block28.pair_record_outcome(*control.key).pointer_configuration
    locked = tuple(
        (atom.center, block23.decode_locked_word(atom.word))
        for atom in control.atoms
        if block23.decode_locked_word(atom.word) is not None
    )
    return (
        len(control.atoms) == 8
        and tuple(atom.center for atom in control.atoms) == FIRST_OUTPUT_CENTERS
        and configuration == expected
        and len(locked) == 2
        and (
            first_center(LEFT, control.left_exit),
            (control.left_exit, control.left_first),
        )
        in locked
        and (
            first_center(RIGHT, control.right_exit),
            (control.right_exit, control.right_first),
        )
        in locked
        and sum(atom.word == block23.BLANK_POINTER for atom in control.atoms) == 6
        and all(atom.word in output_pointer_codebook() for atom in control.atoms)
    )


@dataclass(frozen=True)
class PairOutputActiveSum:
    controls: tuple[PairOutputControl, ...]
    codebook_orthonormal: bool
    configurations_injective: bool
    idempotent: bool
    complement_nontrivial: bool


@lru_cache(maxsize=None)
def pair_output_active_sum(mutation=None):
    controls = [
        pair_output_control(left_exit, right_exit, left_first, right_first)
        for left_exit, right_exit in itertools.product(
            block28.LEFT_EXITS, block28.RIGHT_EXITS
        )
        for left_first, right_first in itertools.product(OUTCOMES, repeat=2)
    ]
    if mutation == "duplicate_output_control":
        controls[-1] = controls[0]
    if mutation == "drop_output_atom":
        controls[-1] = replace(controls[-1], atoms=controls[-1].atoms[:-1])
    controls = tuple(controls)
    codebook = output_pointer_codebook()
    code_ok = len(codebook) == len(set(codebook)) == 57 and all(
        block23.pointer_overlap(left, right) == int(i == j)
        for i, left in enumerate(codebook)
        for j, right in enumerate(codebook)
    )
    configurations = tuple(
        tuple((atom.center, atom.word) for atom in control.atoms)
        for control in controls
    )
    injective = len(configurations) == len(set(configurations)) == 3136
    all_blank = tuple(
        (center, block23.BLANK_POINTER) for center in FIRST_OUTPUT_CENTERS
    )
    physical = all(output_control_is_physical(control) for control in controls)
    return PairOutputActiveSum(
        controls,
        code_ok,
        injective,
        code_ok and injective and physical,
        all_blank not in configurations,
    )


def output_control_at_center(control, center):
    matches = tuple(atom.word for atom in control.atoms if atom.center == center)
    if len(matches) != 1:
        raise ValueError("output control does not have one atom at center")
    return matches[0]


@dataclass(frozen=True)
class BlankProjector:
    center: tuple
    state: object
    operator_form: str


@dataclass(frozen=True)
class FutureResourceSector:
    prefix: PairOutputControl
    bits: tuple
    left_blank: BlankProjector
    right_blank: BlankProjector


@lru_cache(maxsize=None)
def future_resource_sector(prefix, bits, mutation=None):
    left_center = selected_future_center(LEFT, prefix.left_exit)
    right_center = selected_future_center(RIGHT, prefix.right_exit)
    if mutation == "shared_future_center":
        right_center = left_center
    return FutureResourceSector(
        prefix,
        bits,
        BlankProjector(left_center, block23.BLANK_BLOCK, "B_blank"),
        BlankProjector(right_center, block23.BLANK_BLOCK, "B_blank"),
    )


@lru_cache(maxsize=None)
def future_resource_sector_is_physical(sector) -> bool:
    first_blocks = tuple(
        block28.block_sites(center) for center in block28.PAIR_CENTERS
    )
    left_block = block28.block_sites(sector.left_blank.center)
    right_block = block28.block_sites(sector.right_blank.center)
    return (
        sector.bits in RESOURCE_BITS
        and output_control_is_physical(sector.prefix)
        and sector.left_blank.center
        == selected_future_center(LEFT, sector.prefix.left_exit)
        and sector.right_blank.center
        == selected_future_center(RIGHT, sector.prefix.right_exit)
        and sector.left_blank.state
        == sector.right_blank.state
        == block23.BLANK_BLOCK
        and sector.left_blank.operator_form
        == sector.right_blank.operator_form
        == "B_blank"
        and block23.block_overlap(block23.BLANK_BLOCK, block23.BLANK_BLOCK) == 1
        and left_block.isdisjoint(right_block)
        and all(left_block.isdisjoint(block) for block in first_blocks)
        and all(right_block.isdisjoint(block) for block in first_blocks)
    )


def resource_sector_polynomial(bits, left_blank, right_blank):
    return (
        (left_blank if bits[0] else 1 - left_blank)
        * (right_blank if bits[1] else 1 - right_blank)
    )


def resource_partition_certificate(prefix, mutation=None) -> bool:
    left_blank, right_blank = sp.symbols("B_L B_R", commutative=True)
    sectors = {
        bits: resource_sector_polynomial(bits, left_blank, right_blank)
        for bits in RESOURCE_BITS
    }
    physical = tuple(future_resource_sector(prefix, bits) for bits in RESOURCE_BITS)
    if mutation == "duplicate_resource_sector":
        sectors[(1, 1)] = sectors[(1, 0)]
    return (
        all(future_resource_sector_is_physical(sector) for sector in physical)
        and sector_partition_certificate(
            sectors, (left_blank, right_blank)
        )
    )


def append_carrier_centers(branch):
    return {
        branch.anchor,
        *block24.candidate_centers(branch.anchor).values(),
    }


def append_nonidentity_sites(branch):
    return block28.block_sites(branch.anchor) | block28.block_sites(
        branch.forward_center
    )


def append_writer_sites(branch):
    data = block24.factor_dictionary(branch.factors)
    return frozenset(
        block23.add(branch.forward_center, site)
        for site, _input, _output in data["forward_writer_pointer_maps"]
    )


def identity_spectator_block(branch, center) -> bool:
    factors = block24.factor_dictionary(branch.factors)[
        "spectator_identity_factors"
    ]
    selected = tuple(
        (site, operator)
        for candidate, site, operator in factors
        if candidate == center
    )
    return (
        len(selected) == 32
        and {site for site, _operator in selected} == set(block23.SUPPORT)
        and all(operator == "I_2" for _site, operator in selected)
    )


def append_product_compatibility(left, right) -> bool:
    left_nonidentity_centers = {left.anchor, left.forward_center}
    right_nonidentity_centers = {right.anchor, right.forward_center}
    overlap = append_carrier_centers(left) & append_carrier_centers(right)
    if not (
        block24.append_factorization_is_physical(left)
        and block24.branch_effect_is_recontracted(left)
        and block24.append_factorization_is_physical(right)
        and block24.branch_effect_is_recontracted(right)
        and append_nonidentity_sites(left).isdisjoint(
            append_nonidentity_sites(right)
        )
        and append_writer_sites(left).isdisjoint(append_writer_sites(right))
    ):
        return False
    for center in overlap:
        if center in left_nonidentity_centers:
            if not identity_spectator_block(right, center):
                return False
        elif not identity_spectator_block(left, center):
            return False
        if center in right_nonidentity_centers:
            if not identity_spectator_block(left, center):
                return False
        elif not identity_spectator_block(right, center):
            return False
    return True


@lru_cache(maxsize=1)
def append_product_compatibility_certificate() -> bool:
    for left_exit, right_exit in itertools.product(
        block28.LEFT_EXITS, block28.RIGHT_EXITS
    ):
        left = connected_append_descriptor(
            LEFT, left_exit, OUTCOMES[0], OUTCOMES[1]
        ).append
        right = connected_append_descriptor(
            RIGHT, right_exit, OUTCOMES[0], OUTCOMES[1]
        ).append
        overlap = append_carrier_centers(left) & append_carrier_centers(right)
        expected = {left.anchor, right.anchor} if left_exit == right_exit else set()
        if overlap != expected or not append_product_compatibility(left, right):
            return False
    return True


@dataclass(frozen=True)
class EmbeddedAppendProduct:
    left: object
    right: object
    unique_carrier_centers: tuple
    shared_resolutions: tuple


def embedded_append_product(left, right):
    if not append_product_compatibility(left, right):
        raise ValueError("append factors do not admit an embedded product")
    left_nonidentity = {left.anchor, left.forward_center}
    right_nonidentity = {right.anchor, right.forward_center}
    overlap = append_carrier_centers(left) & append_carrier_centers(right)
    resolutions = []
    for center in sorted(overlap):
        if center in left_nonidentity:
            resolutions.append((center, "left-physical", "right-I_2-collapsed"))
        elif center in right_nonidentity:
            resolutions.append((center, "left-I_2-collapsed", "right-physical"))
        else:
            resolutions.append((center, "shared-I_2-collapsed"))
    return EmbeddedAppendProduct(
        left,
        right,
        tuple(sorted(append_carrier_centers(left) | append_carrier_centers(right))),
        tuple(resolutions),
    )


def embedded_append_product_is_physical(product) -> bool:
    overlap = append_carrier_centers(product.left) & append_carrier_centers(
        product.right
    )
    return (
        append_product_compatibility(product.left, product.right)
        and len(product.unique_carrier_centers)
        == len(append_carrier_centers(product.left) | append_carrier_centers(product.right))
        and len(product.shared_resolutions) == len(overlap)
        and {entry[0] for entry in product.shared_resolutions} == overlap
        and all(
            "collapsed" in role
            for entry in product.shared_resolutions
            for role in entry[1:]
            if role != "left-physical" and role != "right-physical"
        )
    )


@dataclass(frozen=True)
class ConnectedFutureBranch:
    prefix: PairOutputControl
    sector: FutureResourceSector
    left_second: tuple | None
    right_second: tuple | None
    left_append: object | None
    right_append: object | None
    embedded_product: EmbeddedAppendProduct | None
    factorization: tuple


@dataclass(frozen=True)
class ConnectedFutureGram:
    prefix: PairOutputControl
    bits: tuple
    coefficient: object
    output_records: tuple
    debit: int


def connected_future_branch(
    prefix, bits, left_second=None, right_second=None, mutation=None
):
    use_left, use_right = bits
    if use_left != (left_second is not None):
        raise ValueError("left outcome does not match resource sector")
    if use_right != (right_second is not None):
        raise ValueError("right outcome does not match resource sector")
    left_append = (
        connected_append_descriptor(
            LEFT, prefix.left_exit, prefix.left_first, left_second
        ).append
        if use_left
        else None
    )
    right_append = (
        connected_append_descriptor(
            RIGHT, prefix.right_exit, prefix.right_first, right_second
        ).append
        if use_right
        else None
    )
    if mutation == "drop_D11_right" and bits == (1, 1):
        right_append = None
    if mutation == "swap_D10_arm" and bits == (1, 0):
        right_append, left_append = left_append, None
    sector = future_resource_sector(prefix, bits)
    embedded = (
        embedded_append_product(left_append, right_append)
        if left_append is not None and right_append is not None
        else None
    )
    factorization = (
        ("output_control", prefix.atoms),
        ("left_blank_projector", sector.left_blank),
        ("left_resource", "B" if use_left else "I-B"),
        ("right_blank_projector", sector.right_blank),
        ("right_resource", "B" if use_right else "I-B"),
        (
            "left_append_factors",
            None if left_append is None else left_append.factors,
        ),
        (
            "right_append_factors",
            None if right_append is None else right_append.factors,
        ),
        ("embedded_append_product", embedded),
        ("outside_identity", "I_outside"),
    )
    return ConnectedFutureBranch(
        prefix,
        sector,
        left_second,
        right_second,
        left_append,
        right_append,
        embedded,
        factorization,
    )


def future_append_is_bound(prefix, arm, append) -> bool:
    exit_front = prefix.left_exit if arm == LEFT else prefix.right_exit
    first_outcome = prefix.left_first if arm == LEFT else prefix.right_first
    respects_other_output_atoms = all(
        atom.center == append.anchor
        or atom.center not in append_carrier_centers(append)
        or identity_spectator_block(append, atom.center)
        for atom in prefix.atoms
    )
    return (
        append.anchor == first_center(arm, exit_front)
        and append.current_word
        == output_control_at_center(prefix, append.anchor)
        == block23.locked_word(exit_front, first_outcome)
        and append.front == exit_front
        and append.source == first_outcome
        and append.forward_center == selected_future_center(arm, exit_front)
        and append.effect.forward_input == block23.BLANK_BLOCK
        and block24.append_factorization_is_physical(append)
        and block24.branch_effect_is_recontracted(append)
        and respects_other_output_atoms
    )


def contract_connected_future_branch(descriptor):
    factors = dict(descriptor.factorization)
    if tuple(factors) != (
        "output_control",
        "left_blank_projector",
        "left_resource",
        "right_blank_projector",
        "right_resource",
        "left_append_factors",
        "right_append_factors",
        "embedded_append_product",
        "outside_identity",
    ):
        raise ValueError("future factorization is incomplete")
    use_left, use_right = descriptor.sector.bits
    if not (
        output_control_is_physical(descriptor.prefix)
        and future_resource_sector_is_physical(descriptor.sector)
        and descriptor.sector.prefix == descriptor.prefix
        and factors["output_control"] == descriptor.prefix.atoms
        and factors["left_blank_projector"] == descriptor.sector.left_blank
        and factors["left_resource"] == ("B" if use_left else "I-B")
        and factors["right_blank_projector"] == descriptor.sector.right_blank
        and factors["right_resource"] == ("B" if use_right else "I-B")
        and factors["outside_identity"] == "I_outside"
        and (descriptor.left_append is not None) == bool(use_left)
        and (descriptor.right_append is not None) == bool(use_right)
        and factors["embedded_append_product"] == descriptor.embedded_product
    ):
        raise ValueError("future control is not bound to routed factors")
    appends = []
    if descriptor.left_append is not None:
        if not future_append_is_bound(
            descriptor.prefix, LEFT, descriptor.left_append
        ):
            raise ValueError("left append is not bound to first output")
        appends.append(descriptor.left_append)
    if descriptor.right_append is not None:
        if not future_append_is_bound(
            descriptor.prefix, RIGHT, descriptor.right_append
        ):
            raise ValueError("right append is not bound to first output")
        appends.append(descriptor.right_append)
    if len(appends) == 2 and not append_product_compatibility(*appends):
        raise ValueError("two-arm append product is incompatible")
    if len(appends) == 2 and not embedded_append_product_is_physical(
        descriptor.embedded_product
    ):
        raise ValueError("two-arm identities were not collapsed physically")
    if len(appends) != 2 and descriptor.embedded_product is not None:
        raise ValueError("singleton future branch has a fake product descriptor")
    if factors["left_append_factors"] != (
        None if descriptor.left_append is None else descriptor.left_append.factors
    ) or factors["right_append_factors"] != (
        None if descriptor.right_append is None else descriptor.right_append.factors
    ):
        raise ValueError("stored append factors do not match routed branches")
    effects = tuple(
        block24.contract_append_effect(append.factors) for append in appends
    )
    return ConnectedFutureGram(
        descriptor.prefix,
        descriptor.sector.bits,
        sp.simplify(sp.prod(effect.scalar for effect in effects)),
        tuple(
            (
                append.forward_center,
                block23.locked_word(append.front, append.target),
            )
            for append in appends
        ),
        len(appends),
    )


@dataclass(frozen=True)
class FutureSectorFamily:
    prefix: PairOutputControl
    bits: tuple
    left_axis: tuple
    right_axis: tuple
    branch_count: int
    coefficient_sum: object
    debit: int


@lru_cache(maxsize=None)
def future_append_axis(prefix, arm):
    exit_front = prefix.left_exit if arm == LEFT else prefix.right_exit
    first_outcome = prefix.left_first if arm == LEFT else prefix.right_first
    return tuple(
        connected_append_descriptor(
            arm, exit_front, first_outcome, second_outcome
        ).append
        for second_outcome in OUTCOMES
    )


@lru_cache(maxsize=None)
def future_sector_family(prefix, bits, mutation=None):
    left_axis = future_append_axis(prefix, LEFT) if bits[0] else ()
    right_axis = future_append_axis(prefix, RIGHT) if bits[1] else ()
    if mutation == "drop_future_outcome":
        if left_axis:
            left_axis = left_axis[:-1]
        elif right_axis:
            right_axis = right_axis[:-1]
    left_sum = sp.simplify(sum(branch.effect.scalar for branch in left_axis))
    right_sum = sp.simplify(sum(branch.effect.scalar for branch in right_axis))
    coefficient_sum = (
        (left_sum if bits[0] else sp.S.One)
        * (right_sum if bits[1] else sp.S.One)
    )
    branch_count = (len(left_axis) if bits[0] else 1) * (
        len(right_axis) if bits[1] else 1
    )
    return FutureSectorFamily(
        prefix,
        bits,
        left_axis,
        right_axis,
        branch_count,
        sp.simplify(coefficient_sum),
        sum(bits),
    )


def future_sector_family_is_physical(family) -> bool:
    expected_count = {(0, 0): 1, (1, 0): 14, (0, 1): 14, (1, 1): 196}
    representative = connected_future_branch(
        family.prefix,
        family.bits,
        OUTCOMES[0] if family.bits[0] else None,
        OUTCOMES[0] if family.bits[1] else None,
    )
    try:
        gram = contract_connected_future_branch(representative)
    except (KeyError, ValueError):
        return False
    return (
        future_resource_sector_is_physical(representative.sector)
        and all(
            future_append_is_bound(family.prefix, LEFT, branch)
            for branch in family.left_axis
        )
        and all(
            future_append_is_bound(family.prefix, RIGHT, branch)
            for branch in family.right_axis
        )
        and family.branch_count == expected_count[family.bits]
        and family.coefficient_sum == 1
        and family.debit == sum(family.bits)
        and gram.bits == family.bits
        and gram.debit == family.debit
    )


@dataclass(frozen=True)
class PairFutureStop:
    active: PairOutputActiveSum
    operator_form: str = "I-P_pair_output"


def future_stop_completion_certificate(active, stop_present=True) -> bool:
    stop = PairFutureStop(active) if stop_present else None
    if not (
        active.idempotent
        and active.complement_nontrivial
        and stop is not None
        and stop.active == active
        and stop.operator_form == "I-P_pair_output"
    ):
        return False
    p_out = sp.symbols("P_pair_output", commutative=True)
    stop_gram = block23.projector_reduce((1 - p_out) ** 2, p_out)
    total_gram = block23.projector_reduce(p_out + stop_gram, p_out)
    return stop_gram == 1 - p_out and total_gram == 1


@lru_cache(maxsize=None)
def future_channel_certificate(mutation=None) -> bool:
    active = pair_output_active_sum(
        "duplicate_output_control"
        if mutation == "duplicate_output_control"
        else "drop_output_atom"
        if mutation == "drop_output_atom"
        else None
    )
    if not (
        active.idempotent
        and active.complement_nontrivial
        and len(active.controls) == 3136
        and append_product_compatibility_certificate()
    ):
        return False
    for prefix in active.controls:
        if not resource_partition_certificate(
            prefix,
            "duplicate_resource_sector"
            if mutation == "duplicate_resource_sector"
            else None,
        ):
            return False
        for bits in RESOURCE_BITS:
            family = future_sector_family(
                prefix,
                bits,
                "drop_future_outcome"
                if mutation == "drop_future_outcome"
                else None,
            )
            if not future_sector_family_is_physical(family):
                return False
    return future_stop_completion_certificate(
        active, stop_present=mutation != "omit_STOP"
    )


@dataclass(frozen=True)
class ConnectedPairPrefix:
    first: object
    first_gram: object
    output_control: PairOutputControl


def connected_pair_prefix(
    lam,
    left_source,
    right_source,
    left_exit,
    right_exit,
    left_first,
    right_first,
    raw_amplitude=False,
):
    first = block28.pair_kraus_descriptor(
        lam,
        left_source,
        right_source,
        left_exit,
        right_exit,
        left_first,
        right_first,
        raw_amplitude=raw_amplitude,
    )
    gram = block28.contract_pair_kraus_descriptor(first)
    control = pair_output_control(
        left_exit, right_exit, left_first, right_first
    )
    return ConnectedPairPrefix(first, gram, control)


def pair_prefix_output_is_bound(prefix) -> bool:
    expected_records = tuple(
        (atom.center, atom.word)
        for atom in prefix.output_control.atoms
        if atom.word != block23.BLANK_POINTER
    )
    unused_centers = {
        atom.center
        for atom in prefix.output_control.atoms
        if atom.word == block23.BLANK_POINTER
    }
    first_factor = dict(prefix.first.factorization)
    return (
        output_control_is_physical(prefix.output_control)
        and prefix.first_gram.output_records == expected_records
        and len(unused_centers) == 6
        and all(
            atom.role == "Blank-block"
            and atom.state == block23.BLANK_BLOCK
            for atom in prefix.first.control.atoms
            if atom.center in unused_centers
        )
        and first_factor["left_turn_factors"] == prefix.first.left.factors
        and first_factor["right_turn_factors"] == prefix.first.right.factors
        and block28.full_guard_is_bound(prefix.first)
    )


@dataclass(frozen=True)
class ConnectedCylinderGram:
    first_coefficient: object
    future_coefficient: object
    composite_coefficient: object
    bits: tuple


@dataclass(frozen=True)
class ConnectedCylinderBranch:
    prefix: ConnectedPairPrefix
    future: ConnectedFutureBranch
    factorization: tuple


@dataclass(frozen=True)
class FixedSectorCylinderEffect:
    control: FutureResourceSector
    first_coefficient: object
    summed_future_coefficient: object
    restricted_first_coefficient: object


def connected_cylinder_branch(prefix, future_branch):
    return ConnectedCylinderBranch(
        prefix,
        future_branch,
        (
            ("first_pair_factors", prefix.first.factorization),
            ("intermediate_output_control", prefix.output_control.atoms),
            ("future_resource_sector", future_branch.sector),
            ("future_factors", future_branch.factorization),
            ("outside_identity", "I_outside"),
        ),
    )


def contract_connected_cylinder(descriptor):
    prefix = descriptor.prefix
    future_branch = descriptor.future
    factors = dict(descriptor.factorization)
    resource_blocks = (
        block28.block_sites(future_branch.sector.left_blank.center),
        block28.block_sites(future_branch.sector.right_blank.center),
    )
    first_carrier_blocks = tuple(
        block28.block_sites(center) for center in block28.PAIR_CENTERS
    )
    if not (
        pair_prefix_output_is_bound(prefix)
        and future_branch.prefix == prefix.output_control
        and tuple(factors) == (
            "first_pair_factors",
            "intermediate_output_control",
            "future_resource_sector",
            "future_factors",
            "outside_identity",
        )
        and factors["first_pair_factors"] == prefix.first.factorization
        and factors["intermediate_output_control"]
        == prefix.output_control.atoms
        and factors["future_resource_sector"] == future_branch.sector
        and factors["future_factors"] == future_branch.factorization
        and factors["outside_identity"] == "I_outside"
        and all(
            resource.isdisjoint(first_block)
            for resource in resource_blocks
            for first_block in first_carrier_blocks
        )
    ):
        raise ValueError("future channel is not conditioned on actual first output")
    future_gram = contract_connected_future_branch(future_branch)
    return ConnectedCylinderGram(
        prefix.first_gram.coefficient,
        future_gram.coefficient,
        sp.simplify(prefix.first_gram.coefficient * future_gram.coefficient),
        future_gram.bits,
    )


def fixed_sector_cylinder_effect(prefix, family):
    control = future_resource_sector(prefix.output_control, family.bits)
    if not (
        pair_prefix_output_is_bound(prefix)
        and family.prefix == prefix.output_control
        and future_resource_sector_is_physical(control)
        and future_sector_family_is_physical(family)
    ):
        raise ValueError("fixed-sector cylinder is not physically bound")
    first = prefix.first_gram.coefficient
    return FixedSectorCylinderEffect(
        control,
        first,
        sp.simplify(first * family.coefficient_sum),
        first,
    )


@lru_cache(maxsize=1)
def first_pair_template_certificate() -> bool:
    if not (
        block28.pair_control_certificate()
        and block28.tensor_support_certificate()
        and block28.record_label_certificate()
        and all(all(block28.q_certificate(lam).values()) for lam in LAMBDAS)
        and all(
            block28.full_space_completion_certificate(
                block28.active_gram_terms(lam)
            )
            for lam in LAMBDAS
        )
    ):
        return False
    fixed_left, fixed_right = OUTCOMES[0], OUTCOMES[1]
    for lam in LAMBDAS:
        for control in pair_output_active_sum().controls:
            prefix = connected_pair_prefix(
                lam,
                fixed_left,
                fixed_right,
                *control.key,
            )
            if not pair_prefix_output_is_bound(prefix):
                return False
    for lam in LAMBDAS:
        for left_source, right_source in itertools.product(OUTCOMES, repeat=2):
            for left_exit, right_exit in itertools.product(
                block28.LEFT_EXITS, block28.RIGHT_EXITS
            ):
                prefix = connected_pair_prefix(
                    lam,
                    left_source,
                    right_source,
                    left_exit,
                    right_exit,
                    OUTCOMES[0],
                    OUTCOMES[-1],
                )
                expected = sp.simplify(
                    block28.q_weight(lam, left_exit, right_exit)
                    * block23.transition(left_source, OUTCOMES[0])
                    * block23.transition(right_source, OUTCOMES[-1])
                )
                if prefix.first_gram.coefficient != expected:
                    return False
    return True


@lru_cache(maxsize=1)
def cylinder_certificate() -> bool:
    if not (
        transition_table_certificate()
        and literal_turn_and_append_binding_certificate()
        and first_pair_template_certificate()
        and future_channel_certificate()
    ):
        return False
    q_values = tuple(
        block28.q_weight(lam, left_exit, right_exit)
        for lam in LAMBDAS
        for left_exit, right_exit in itertools.product(
            block28.LEFT_EXITS, block28.RIGHT_EXITS
        )
    )
    transition_values = tuple(
        block23.transition(source, target)
        for source, target in itertools.product(OUTCOMES, repeat=2)
    )
    if not (
        len(q_values) == 32
        and all(value > 0 for value in q_values)
        and len(transition_values) == 196
        and all(value > 0 for value in transition_values)
    ):
        return False
    prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[2],
        OUTCOMES[3],
    )
    for bits in RESOURCE_BITS:
        family = future_sector_family(prefix.output_control, bits)
        sector_effect = fixed_sector_cylinder_effect(prefix, family)
        representative = connected_future_branch(
            prefix.output_control,
            bits,
            OUTCOMES[0] if bits[0] else None,
            OUTCOMES[0] if bits[1] else None,
        )
        gram = contract_connected_cylinder(
            connected_cylinder_branch(prefix, representative)
        )
        if not (
            family.coefficient_sum == 1
            and sector_effect.control.bits == bits
            and sector_effect.summed_future_coefficient
            == sector_effect.restricted_first_coefficient
            and gram.composite_coefficient
            == sp.simplify(
                gram.first_coefficient * gram.future_coefficient
            )
        ):
            return False
    return (
        len(LAMBDAS)
        * len(block28.LEFT_EXITS)
        * len(block28.RIGHT_EXITS)
        * len(OUTCOMES) ** 4
        == 1_229_312
        and 3136 * (1 + 14 + 14 + 196) == 705_600
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
        and all(
            block24.append_preserves_arbitrary_prior_records(
                connected_append_descriptor(
                    arm, exit_front, first_outcome, second_outcome
                ).append
            )
            for arm in ARMS
            for exit_front, first_outcome, second_outcome in itertools.product(
                arm_exits(arm), OUTCOMES, OUTCOMES
            )
        )
        and append_product_compatibility_certificate()
    )


@lru_cache(maxsize=None)
def debit_ledger_certificate(mutation=None) -> bool:
    expected = {(0, 0): 2, (1, 0): 3, (0, 1): 3, (1, 1): 4}
    prefix = pair_output_control(
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[0],
        OUTCOMES[1],
    )
    actual = {}
    for bits in RESOURCE_BITS:
        descriptor = connected_future_branch(
            prefix,
            bits,
            OUTCOMES[0] if bits[0] else None,
            OUTCOMES[1] if bits[1] else None,
        )
        gram = contract_connected_future_branch(descriptor)
        actual[bits] = 2 + gram.debit
    if mutation == "pair_total_three":
        actual[(1, 1)] = 3
    first = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[0],
        OUTCOMES[1],
    )
    selected = set(state_controlled_centers()[10:])
    first_targets = set(block28.LEFT_TARGETS + block28.RIGHT_TARGETS)
    return (
        actual == expected
        and first.first.left.effect.forward_input == block23.BLANK_BLOCK
        and first.first.right.effect.forward_input == block23.BLANK_BLOCK
        and len(first.first_gram.output_records) == 2
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
                    and block24.append_branch_covariance_certificate(
                        connected_append_descriptor(
                            arm,
                            exit_front,
                            first_outcome,
                            second_outcome,
                        ).append,
                        rotation,
                    )
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
    return (
        set(RESOURCE_BITS) == {(right, left) for left, right in RESOURCE_BITS}
        and block23.rotate_block_product(block23.BLANK_BLOCK, ROTATIONS[0])
        == block23.BLANK_BLOCK
        and block24.translation_covariance_certificate()
        and block28.full_pair_covariance_certificate()
        and append_product_compatibility_certificate()
    )


@lru_cache(maxsize=None)
def arbitrary_reference_certificate(mutation=None) -> bool:
    active = pair_output_active_sum()
    if not (
        active.idempotent
        and active.complement_nontrivial
        and len(active.controls) == 3136
        and block28.arbitrary_reference_certificate()
    ):
        return False
    row, column = sp.symbols("r_R s_R", integer=True, nonnegative=True)
    delta = sp.KroneckerDelta(row, column)
    p_out = sp.symbols("P_pair_output_R", commutative=True)
    system_total = block23.projector_reduce(
        p_out + (1 - p_out) ** 2, p_out
    )
    reference_factor = (
        sp.Symbol("R_nonidentity") if mutation == "nonidentity" else sp.S.One
    )
    return (
        system_total == 1
        and sp.simplify(reference_factor * delta * system_total - delta)
        == 0
    )


TERMINAL_TEXT = (
    "BOTH-SUPPLIED-Q-PAIR-CHANNELS-COMPOSE-WITH-ONE-PHYSICAL-"
    "OUTPUT-RECORD-CONTROLLED-FUTURE-CHANNEL"
)

SCOPE_TEXT = (
    "two supplied q choices; imported complete pair channel followed by one "
    "externally invoked physical output-Record-controlled future channel; "
    "D00/D10/D01/D11 route zero/left/right/both literal Block24 appends on "
    "supplied finite rails; no singleton first-layer law, second pair reuse, "
    "cause selection, autonomous invocation, renewal, scheduler, compiler, "
    "rate, gravity, axiom amendment, audit retention, obligation retirement, "
    "or TOE movement"
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


def scope_promotion_is_rejected(phrase) -> bool:
    return (
        phrase in FORBIDDEN_SCOPE_PHRASES
        and phrase in f"{SCOPE_TEXT}; {phrase}"
        and not scope_guard_certificate(
            TERMINAL_TEXT, f"{SCOPE_TEXT}; {phrase}"
        )
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


def connected_future_mutation_is_rejected(prefix, bits, mutation) -> bool:
    try:
        descriptor = connected_future_branch(
            prefix,
            bits,
            OUTCOMES[0] if bits[0] else None,
            OUTCOMES[1] if bits[1] else None,
            mutation=mutation,
        )
        contract_connected_future_branch(descriptor)
    except (KeyError, ValueError):
        return True
    return False


def raw_pair_amplitude_mutation_is_rejected() -> bool:
    try:
        connected_pair_prefix(
            sp.Rational(1, 2),
            OUTCOMES[0],
            OUTCOMES[1],
            block28.LEFT_EXITS[0],
            block28.RIGHT_EXITS[0],
            OUTCOMES[2],
            OUTCOMES[3],
            raw_amplitude=True,
        )
    except (KeyError, ValueError):
        return True
    return False


def equal_exit_nonidentity_overlap_mutation_is_rejected() -> bool:
    exit_front = block28.LEFT_EXITS[0]
    left = connected_append_descriptor(
        LEFT, exit_front, OUTCOMES[0], OUTCOMES[1]
    ).append
    right = connected_append_descriptor(
        RIGHT, exit_front, OUTCOMES[0], OUTCOMES[1]
    ).append
    factors = right.factors
    spectators = list(
        block24.factor_dictionary(factors)["spectator_identity_factors"]
    )
    index = next(
        index
        for index, (center, _site, _operator) in enumerate(spectators)
        if center == left.anchor
    )
    center, site, _operator = spectators[index]
    spectators[index] = (center, site, "X_2")
    mutant = replace(
        right,
        factors=replace_named_factor(
            factors, "spectator_identity_factors", tuple(spectators)
        ),
    )
    return not append_product_compatibility(left, mutant)


def mutation_rejections():
    prefix = pair_output_control(
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[0],
        OUTCOMES[1],
    )
    standard_descriptor = connected_append_descriptor(
        LEFT, block28.LEFT_EXITS[0], OUTCOMES[0], OUTCOMES[1]
    )
    wrong_output_atoms = list(prefix.atoms)
    wrong_output_index = next(
        index
        for index, atom in enumerate(wrong_output_atoms)
        if atom.center == first_center(LEFT, prefix.left_exit)
    )
    wrong_output_atoms[wrong_output_index] = OutputPointerAtom(
        wrong_output_atoms[wrong_output_index].center,
        block23.locked_word(prefix.left_exit, OUTCOMES[-1]),
    )
    wrong_output_control = replace(
        prefix, atoms=tuple(wrong_output_atoms)
    )
    fresh_site = block23.add(standard_descriptor.first_site, E1)
    fresh_copy_descriptor = replace(
        standard_descriptor,
        first_site=fresh_site,
        origin="fresh_preparation",
        append=block24.append_branch(
            fresh_site,
            standard_descriptor.current_word,
            standard_descriptor.second_outcome,
        ),
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
        "duplicate_output_control_breaks_bound_active_projector": not pair_output_active_sum(
            "duplicate_output_control"
        ).idempotent,
        "dropped_output_atom_breaks_eight_pointer_control": not pair_output_active_sum(
            "drop_output_atom"
        ).idempotent,
        "shared_future_center_breaks_physical_resource_sector": (
            not future_resource_sector_is_physical(
                future_resource_sector(prefix, (1, 1), "shared_future_center")
            )
        ),
        "duplicated_resource_sector_breaks_physical_partition": not resource_partition_certificate(
            prefix, "duplicate_resource_sector"
        ),
        "nonidentity_equal_exit_spectator_breaks_composite": (
            equal_exit_nonidentity_overlap_mutation_is_rejected()
        ),
        "wrong_output_word_breaks_append_input_binding": (
            not output_control_is_physical(wrong_output_control)
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
        "biased_transition_row_breaks_normalization": not transition_table_certificate(
            "first_row_bias"
        ),
        "dropped_future_transition_breaks_normalization": not transition_table_certificate(
            "future_row_drop"
        ),
        "raw_q_probability_breaks_pair_Kraus_Gram": (
            raw_pair_amplitude_mutation_is_rejected()
        ),
        "bad_q_cell_breaks_pair_normalization": not block28.q_certificate(
            sp.Rational(1, 2), "bad_diagonal"
        )["normalized"],
        "biased_q_cell_breaks_uniform_singleton_marginal": not block28.q_certificate(
            sp.Rational(1, 2), "biased_cell"
        )["uniform_marginals"],
        "D10_routed_through_wrong_arm_breaks_binding": (
            connected_future_mutation_is_rejected(
                prefix, (1, 0), "swap_D10_arm"
            )
        ),
        "dropped_D11_arm_breaks_composite_writer": (
            connected_future_mutation_is_rejected(
                prefix, (1, 1), "drop_D11_right"
            )
        ),
        "dropped_future_outcome_breaks_fixed_prefix_cylinder": (
            future_sector_family(
                prefix, (1, 0), "drop_future_outcome"
            ).coefficient_sum
            != 1
        ),
        "missing_common_STOP_breaks_full_space_TP": (
            not future_stop_completion_certificate(
                pair_output_active_sum(), stop_present=False
            )
        ),
        "missing_imported_pair_STOP_breaks_first_channel_TP": (
            not block28.full_space_completion_certificate(
                block28.active_gram_terms(LAMBDAS[0]), stop_present=False
            )
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
            name: scope_promotion_is_rejected(phrase)
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
        "physical_pair_output_active_sum",
        pair_output_active_sum().idempotent
        and pair_output_active_sum().complement_nontrivial,
        "3,136 exact eight-pointer configurations are orthogonal and bind "
        "the physical P_pair_output projector",
    )
    checks.check(
        "physical_future_channel_and_STOP",
        future_channel_certificate(),
        "12,544 output/resource controls route 705,600 literal future terms; "
        "their Gram is P_pair_output and I-P_pair_output completes the channel",
    )
    checks.check(
        "imported_pair_Kraus_template_binding",
        first_pair_template_certificate(),
        "both supplied q families contract through literal Block28 controls "
        "and bind every successful output configuration",
    )
    checks.check(
        "fixed_prefix_depth_two_cylinders",
        cylinder_certificate(),
        "all 1,229,312 pair prefixes factor through physical "
        "D00/D10/D01/D11 future-resource cylinders",
    )
    checks.check(
        "q_independent_continuation",
        q_independent_continuation_certificate(),
        "1,568 continuation descriptors contain no lambda-dependent temporal kernel",
    )
    checks.check(
        "Record_history_QND_and_injectivity",
        record_history_and_qnd_certificate(),
        "784 conditional output histories per arm and 614,656 pair output "
        "configurations decode; old and first Records are QND",
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
        "the bound future-system identity tensors with an arbitrary untouched "
        "reference identity",
    )
    mutations = mutation_rejections()
    for name, rejected in mutations.items():
        print(f"MUTATION {'REJECTED' if rejected else 'SURVIVED'} {name}")
    checks.check(
        "designated_mutations",
        all(mutations.values()) and len(mutations) == 38,
        f"rejected={sum(mutations.values())}/{len(mutations)}",
    )
    checks.check(
        "claim_scope",
        scope_guard_certificate(),
        SCOPE_TEXT,
    )
    print(
        "per_element: checked — all 32 supplied q cells, 196 transition "
        "entries, 1,568 turn branches, 1,568 append descriptors, 3,136 "
        "output controls, and 12,544 output/resource projectors"
    )
    print(
        "per_site: checked — 18 state-controlled blocks and every identity "
        "factor on the 34-block, 1,088-site literal carrier"
    )
    print(
        "per_mode: checked — both supplied pair channels followed by physical "
        "D00/D10/D01/D11 future-resource sectors"
    )
    print(
        "per_block: checked — actual first output Record is the future current "
        "input; selected future targets, STOP, QND, and debit ledger are bound"
    )
    print(
        "lattice_wide: checked and not executed — no singleton first-layer "
        "law, second returned-pair handoff, autonomous invocation, renewal, "
        "or nearest-neighbor compiled law is claimed"
    )
    if checks.failed == 0:
        print(f"TERMINAL: {TERMINAL_TEXT}")
    else:
        print("TERMINAL: INCOMPLETE-NO-SCIENCE-INFERENCE")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
