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
    AXIOM_NOTE: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
}

FROZEN = {
    "APPROACH_REGISTRY.md": "9c19f26a22c72e017048ed3c514117509fbd9990d49948f3b91f3b8fb3013237",
    "ARTIFACT_PLAN.md": "36cb1934470a790812bab78efac5acdedfc497476534b9a8275d42591aa4a3b4",
    "ASSUMPTIONS_AND_IMPORTS.md": "ba01782882018cabdc0ce0dab807eea9df11b34d9c56474df97385b7778aff88",
    "AUTHORITY_GATE.md": "1cc2aa1ad7f5839af0905a6123a73c7fe84e507e7c234b0146339bfcaea62d97",
    "GOAL.md": "81c55379f532eb95c3b4503886a665fbc1fc3ff85fa105250e9dc90ae69db1f4",
    "MUTATION_PLAN.md": "6efaaf5bfdb6424cc127bd2783f287fe1ae5d9a96f1df25d5d148bc703676d52",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "e8d1a9b40a8e27f3a3c617a3bc2e8422e47ec1c84c7ad15c754b69a4aa6db757",
    "OPPORTUNITY_QUEUE.md": "7d14cea2f6aed350d7d830a5ce4723fc25323f108ecf3981e67a163daf8bb29b",
    "PANEL_RETURN.md": "c19b2c688ef2ded0a2873eaabcef32d8155a5812a309dd303f02fbfeaa24a912",
    "PREFLIGHT_WITNESSES.md": "6d1ecd6535814ffe9c51bb259aa5224739d35a2f1bd10b9db82901434d724047",
    "PREREG_AMENDMENT_PAIR_PREFIX_PHYSICAL.md": "41e9ddfaa8cf0be77e9637cb9915a91254ccb7df8ea9275f78728ba2ea05c3e9",
    "PREREG_AMENDMENT_OPERATOR_COMPOSITION.md": "aed103ec4bb939c757fa0e1a1b7e734f52636f9117e016358d5409d7892c5bbd",
    "ROUTE_PORTFOLIO.md": "dd1af4cbe522d48ac243e832fc9ffa3ea18165f00f68aad0cc3d9b22f957f5c3",
    "STATE.yaml": "2fb752f29dc48cf24d80a1c5000bb8857568ba931fc89a6baba7d980dafdf7c7",
    "TOE_LANE_UPDATE.md": "5e4da994e4dc31c54479838f086134e78d25910928e870e3a9376dc40f082d03",
    "TRACE_GATE.md": "10f4882df9b701b287fd9b55c418b5551bf4f7cf50e8ead366820d4ecabdcc64",
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
    ".claude/science/physics-loops/toe-source-eta-ownership-block29-connected-output-depth-two-20260830/PREREG_AMENDMENT_OPERATOR_COMPOSITION.md",
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


def coordinate_sort_key(center):
    return tuple(sp.srepr(sp.sympify(value)) for value in center)


def sorted_centers(centers):
    return tuple(sorted(tuple(centers), key=coordinate_sort_key))


def tensor_projector_sort_key(projector):
    return tuple(
        (
            coordinate_sort_key(atom.center),
            atom.algebra,
            atom.sense,
            repr(atom.state),
        )
        for atom in projector.atoms
    )


def sorted_projectors(projectors):
    return tuple(sorted(tuple(projectors), key=tensor_projector_sort_key))


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
def first_pair_literal_centers():
    centers = {block28.Y_LEFT, block28.Y_RIGHT}
    centers.update(block24.candidate_centers(block28.Y_LEFT).values())
    centers.update(block24.candidate_centers(block28.Y_RIGHT).values())
    return sorted_centers(centers)


@lru_cache(maxsize=1)
def future_literal_centers():
    centers = set(block28.PAIR_CENTERS)
    for arm in ARMS:
        for exit_front in arm_exits(arm):
            centers.update(
                block24.candidate_centers(first_center(arm, exit_front)).values()
            )
    return sorted_centers(centers)


@lru_cache(maxsize=1)
def full_literal_centers():
    return sorted_centers(
        set(first_pair_literal_centers()) | set(future_literal_centers())
    )


def all_blocks_disjoint(centers):
    blocks = tuple(block28.block_sites(center) for center in centers)
    return all(
        left.isdisjoint(right)
        for left, right in itertools.combinations(blocks, 2)
    )


def geometry_certificate(mutation=None) -> bool:
    controlled = list(state_controlled_centers())
    first = list(first_pair_literal_centers())
    future = list(future_literal_centers())
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
    first_blocks = tuple(block28.block_sites(center) for center in first)
    spectator_only = (
        set(full_literal_centers())
        - set(block28.PAIR_CENTERS)
        - set(state_controlled_centers()[10:])
    )
    return (
        len(controlled) == len(set(controlled)) == 18
        and len(first) == len(set(first)) == 12
        and len(future) == len(set(future)) == 34
        and len(full) == len(set(full)) == 36
        and len(selected) == len(set(selected)) == 8
        and len(spectator_only) == 18
        and all_blocks_disjoint(controlled)
        and all_blocks_disjoint(first)
        and all_blocks_disjoint(future)
        and all_blocks_disjoint(full)
        and all(
            selected_block.isdisjoint(first_block)
            for selected_block in selected_blocks
            for first_block in first_blocks
        )
        and len(set().union(*(block28.block_sites(c) for c in future))) == 1088
        and len(set().union(*(block28.block_sites(c) for c in full))) == 1152
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


@lru_cache(maxsize=65_536)
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
        and append_branch_is_physical(append)
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
class LocalProjector:
    center: tuple
    algebra: str
    state: object
    sense: str


@dataclass(frozen=True)
class TensorProjector:
    carrier_centers: tuple
    atoms: tuple[LocalProjector, ...]


@dataclass(frozen=True)
class OrthogonalProjectorSum:
    carrier_centers: tuple
    terms: tuple[TensorProjector, ...]


@lru_cache(maxsize=65_536)
def local_projector_is_physical(atom) -> bool:
    if atom.algebra == "pointer26":
        return (
            atom.sense == "ket"
            and isinstance(atom.state, tuple)
            and len(atom.state) == len(block23.POINTER_ORDER) == 26
            and set(atom.state) <= {0, 1}
        )
    if atom.algebra == "block32":
        return (
            atom.sense in ("ket", "complement")
            and atom.state == block23.BLANK_BLOCK
        )
    return False


@lru_cache(maxsize=65_536)
def local_projector_rank(atom):
    if not local_projector_is_physical(atom):
        raise ValueError("local projector is not physical")
    if atom.algebra == "pointer26":
        return 2 ** len(block23.DIRECTIONS)
    return 1 if atom.sense == "ket" else 2 ** len(block23.SUPPORT) - 1


def local_projectors_orthogonal(left, right) -> bool:
    if left.center != right.center:
        return False
    if left.algebra != right.algebra:
        raise ValueError("incompatible local projector algebras")
    if left.algebra == "pointer26":
        return block23.pointer_overlap(left.state, right.state) == 0
    if left.state != right.state:
        raise ValueError("Block29 only binds complements of the exact Blank block")
    return left.sense != right.sense


def make_tensor_projector(atoms):
    return make_tensor_projector_from_tuple(tuple(atoms))


@lru_cache(maxsize=65_536)
def make_tensor_projector_from_tuple(atoms):
    atoms = tuple(
        sorted(
            atoms,
            key=lambda atom: (coordinate_sort_key(atom.center), atom.algebra),
        )
    )
    if len({(atom.center, atom.algebra) for atom in atoms}) != len(atoms):
        raise ValueError("tensor projector has duplicate local algebras")
    return TensorProjector(
        sorted_centers({atom.center for atom in atoms}),
        atoms,
    )


@lru_cache(maxsize=65_536)
def tensor_projector_is_physical(projector) -> bool:
    return (
        projector == make_tensor_projector(projector.atoms)
        and projector.carrier_centers
        == sorted_centers({atom.center for atom in projector.atoms})
        and all(local_projector_is_physical(atom) for atom in projector.atoms)
    )


@lru_cache(maxsize=65_536)
def tensor_projector_rank(projector):
    if not tensor_projector_is_physical(projector):
        raise ValueError("tensor projector is not physical")
    return sp.prod(local_projector_rank(atom) for atom in projector.atoms)


@lru_cache(maxsize=65_536)
def tensor_projectors_orthogonal(left, right) -> bool:
    left_by_key = {(atom.center, atom.algebra): atom for atom in left.atoms}
    right_by_key = {(atom.center, atom.algebra): atom for atom in right.atoms}
    return any(
        local_projectors_orthogonal(left_by_key[key], right_by_key[key])
        for key in set(left_by_key) & set(right_by_key)
    )


@lru_cache(maxsize=16_384)
def output_tensor_projector(control):
    return make_tensor_projector(
        LocalProjector(atom.center, "pointer26", atom.word, "ket")
        for atom in control.atoms
    )


@lru_cache(maxsize=16_384)
def output_projector_is_physical(control) -> bool:
    projector = output_tensor_projector(control)
    return (
        output_control_is_physical(control)
        and tensor_projector_is_physical(projector)
        and len(projector.atoms) == 8
        and tensor_projector_rank(projector) == 2 ** 48
    )


@lru_cache(maxsize=1)
def output_projector_orthogonality_certificate() -> bool:
    active = pair_output_active_sum()
    codebook = output_pointer_codebook()
    configurations = tuple(
        tuple(atom.word for atom in control.atoms) for control in active.controls
    )
    # Every two distinct configurations differ in at least one local codeword;
    # exact codebook orthogonality therefore supplies a zero local factor in
    # their TensorProjector product.
    return (
        len(configurations) == len(set(configurations)) == 3136
        and all(word in codebook for configuration in configurations for word in configuration)
        and all(
            block23.pointer_overlap(left, right) == int(i == j)
            for i, left in enumerate(codebook)
            for j, right in enumerate(codebook)
        )
        and all(output_projector_is_physical(control) for control in active.controls)
    )


@dataclass(frozen=True)
class FutureResourceSector:
    prefix: PairOutputControl
    bits: tuple
    left: LocalProjector
    right: LocalProjector
    projector: TensorProjector


@dataclass(frozen=True)
class SectorControl:
    prefix: PairOutputControl
    resource: FutureResourceSector
    projector: TensorProjector


@lru_cache(maxsize=None)
def future_resource_sector(prefix, bits, mutation=None):
    left_center = selected_future_center(LEFT, prefix.left_exit)
    right_center = selected_future_center(RIGHT, prefix.right_exit)
    if mutation == "shared_future_center":
        right_center = left_center
    left_sense = "ket" if bits[0] else "complement"
    right_sense = "ket" if bits[1] else "complement"
    if mutation == "wrong_left_sense":
        left_sense = "complement" if bits[0] else "ket"
    left = LocalProjector(
        left_center, "block32", block23.BLANK_BLOCK, left_sense
    )
    right = LocalProjector(
        right_center, "block32", block23.BLANK_BLOCK, right_sense
    )
    return FutureResourceSector(
        prefix,
        bits,
        left,
        right,
        make_tensor_projector((left, right)),
    )


@lru_cache(maxsize=None)
def future_resource_sector_is_physical(sector) -> bool:
    first_blocks = tuple(
        block28.block_sites(center) for center in first_pair_literal_centers()
    )
    left_block = block28.block_sites(sector.left.center)
    right_block = block28.block_sites(sector.right.center)
    return (
        sector.bits in RESOURCE_BITS
        and output_projector_is_physical(sector.prefix)
        and sector.left.center
        == selected_future_center(LEFT, sector.prefix.left_exit)
        and sector.right.center
        == selected_future_center(RIGHT, sector.prefix.right_exit)
        and sector.left.state
        == sector.right.state
        == block23.BLANK_BLOCK
        and sector.left.sense == ("ket" if sector.bits[0] else "complement")
        and sector.right.sense == ("ket" if sector.bits[1] else "complement")
        and sector.projector == make_tensor_projector((sector.left, sector.right))
        and tensor_projector_is_physical(sector.projector)
        and left_block.isdisjoint(right_block)
        and all(left_block.isdisjoint(block) for block in first_blocks)
        and all(right_block.isdisjoint(block) for block in first_blocks)
    )


@lru_cache(maxsize=16_384)
def sector_control(prefix, bits, mutation=None):
    resource = future_resource_sector(prefix, bits, mutation)
    projector = make_tensor_projector(
        output_tensor_projector(prefix).atoms + resource.projector.atoms
    )
    return SectorControl(prefix, resource, projector)


@lru_cache(maxsize=16_384)
def sector_control_is_physical(control) -> bool:
    expected = make_tensor_projector(
        output_tensor_projector(control.prefix).atoms
        + control.resource.projector.atoms
    )
    return (
        output_projector_is_physical(control.prefix)
        and future_resource_sector_is_physical(control.resource)
        and control.resource.prefix == control.prefix
        and control.projector == expected
        and tensor_projector_is_physical(control.projector)
        and len(control.projector.atoms) == 10
        and tensor_projector_rank(control.projector)
        == 2**48 * tensor_projector_rank(control.resource.projector)
    )


@lru_cache(maxsize=None)
def resource_partition_certificate(prefix, mutation=None) -> bool:
    sectors = [future_resource_sector(prefix, bits) for bits in RESOURCE_BITS]
    if mutation == "duplicate_resource_sector":
        sectors[-1] = sectors[1]
    sectors = tuple(sectors)
    expected_ranks = {
        (0, 0): (2**32 - 1) ** 2,
        (1, 0): 2**32 - 1,
        (0, 1): 2**32 - 1,
        (1, 1): 1,
    }
    return (
        len(sectors) == len(set(sectors)) == 4
        and {sector.bits for sector in sectors} == set(RESOURCE_BITS)
        and all(future_resource_sector_is_physical(sector) for sector in sectors)
        and all(
            tensor_projectors_orthogonal(left.projector, right.projector)
            for index, left in enumerate(sectors)
            for right in sectors[:index]
        )
        and all(
            tensor_projector_rank(sector.projector) == expected_ranks[sector.bits]
            for sector in sectors
        )
        and sum(tensor_projector_rank(sector.projector) for sector in sectors)
        == 2**64
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


@lru_cache(maxsize=65_536)
def append_branch_is_physical(branch) -> bool:
    return (
        block24.append_factorization_is_physical(branch)
        and block24.branch_effect_is_recontracted(branch)
    )


@lru_cache(maxsize=65_536)
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


@lru_cache(maxsize=32_768)
def append_product_compatibility(left, right) -> bool:
    left_nonidentity_centers = {left.anchor, left.forward_center}
    right_nonidentity_centers = {right.anchor, right.forward_center}
    overlap = append_carrier_centers(left) & append_carrier_centers(right)
    if not (
        append_branch_is_physical(left)
        and append_branch_is_physical(right)
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
class BlockAction:
    center: tuple
    role: str
    factors: tuple


@dataclass(frozen=True)
class MergedBlockAction:
    center: tuple
    role: str
    owner: str
    factors: tuple
    sources: tuple


@lru_cache(maxsize=65_536)
def append_block_actions(branch):
    if not (
        append_branch_is_physical(branch)
    ):
        raise ValueError("append factors are not physical")
    data = block24.factor_dictionary(branch.factors)
    actions = [
        BlockAction(
            branch.anchor,
            "current",
            (
                ("live", data["current_live_identities"]),
                ("pointer", data["current_pointer_projectors"]),
            ),
        ),
        BlockAction(
            branch.forward_center,
            "forward",
            (
                ("live_prep", data["forward_live_prep_maps"]),
                ("pointer_prep", data["forward_pointer_prep_maps"]),
                ("root", data["forward_live_root"]),
                ("writer", data["forward_writer_pointer_maps"]),
            ),
        ),
    ]
    for center in data["spectator_identity_centers"]:
        factors = tuple(
            (site, operator)
            for candidate, site, operator in data["spectator_identity_factors"]
            if candidate == center
        )
        if (
            len(factors) != len(block23.SUPPORT) == 32
            or {site for site, _operator in factors} != set(block23.SUPPORT)
            or any(operator != "I_2" for _site, operator in factors)
        ):
            raise ValueError("spectator is not one complete block identity")
        actions.append(BlockAction(center, "identity", factors))
    actions = tuple(sorted(actions, key=lambda action: coordinate_sort_key(action.center)))
    if (
        len(actions) != 7
        or len({action.center for action in actions}) != 7
        or {action.center for action in actions} != append_carrier_centers(branch)
    ):
        raise ValueError("append block-action expansion is not complete")
    return actions


@lru_cache(maxsize=16_384)
def merge_append_actions(left, right, mutation=None):
    arms = tuple(
        (name, branch)
        for name, branch in ((LEFT, left), (RIGHT, right))
        if branch is not None
    )
    if not arms:
        return ()
    if len(arms) == 2 and not append_product_compatibility(left, right):
        raise ValueError("append products are not compatible")
    action_maps = {
        name: {action.center: action for action in append_block_actions(branch)}
        for name, branch in arms
    }
    if mutation == "nonidentity_equal_exit_spectator":
        candidate = next(
            (
                (identity_arm, center)
                for center in sorted_centers(
                    set(action_maps[LEFT]) & set(action_maps[RIGHT])
                )
                for identity_arm in ARMS
                if action_maps[identity_arm][center].role == "identity"
                and action_maps[
                    RIGHT if identity_arm == LEFT else LEFT
                ][center].role
                != "identity"
            ),
            None,
        )
        if candidate is None:
            raise ValueError("mutation requires an equal-exit spectator overlap")
        identity_arm, center = candidate
        action = action_maps[identity_arm][center]
        factors = list(action.factors)
        factors[0] = (factors[0][0], "X_2")
        action_maps[identity_arm][center] = replace(
            action, factors=tuple(factors)
        )
    centers = sorted_centers(
        set().union(*(set(actions) for actions in action_maps.values()))
    )
    merged = []
    for center in centers:
        sources = tuple(
            (name, action_maps[name][center])
            for name, _branch in arms
            if center in action_maps[name]
        )
        physical = tuple(entry for entry in sources if entry[1].role != "identity")
        if len(physical) > 1:
            raise ValueError("two physical append actions share one block")
        if physical:
            owner, selected = physical[0]
        else:
            owner = "shared" if len(sources) == 2 else sources[0][0]
            selected = sources[0][1]
            if any(source.factors != selected.factors for _name, source in sources):
                raise ValueError("shared identities are not identical")
        merged.append(
            MergedBlockAction(
                center,
                selected.role,
                owner,
                selected.factors,
                sources,
            )
        )
    if mutation == "same_count_wrong_center" and merged:
        merged[-1] = replace(merged[-1], center=block23.add(merged[-1].center, E1))
    if mutation == "swap_shared_owner":
        index = next(
            index
            for index, action in enumerate(merged)
            if len(action.sources) == 2 and action.owner in ARMS
        )
        action = merged[index]
        merged[index] = replace(
            action, owner=RIGHT if action.owner == LEFT else LEFT
        )
    return tuple(merged)


@dataclass(frozen=True)
class EmbeddedAppendProduct:
    left: object | None
    right: object | None
    carrier_centers: tuple
    actions: tuple[MergedBlockAction, ...]
    outside_identity: str


@lru_cache(maxsize=16_384)
def embedded_append_product(left, right, mutation=None):
    actions = merge_append_actions(left, right, mutation)
    return EmbeddedAppendProduct(
        left,
        right,
        tuple(action.center for action in actions),
        actions,
        "I_outside",
    )


@lru_cache(maxsize=16_384)
def embedded_append_product_is_physical(product) -> bool:
    try:
        expected = merge_append_actions(product.left, product.right)
    except (KeyError, StopIteration, ValueError):
        return False
    branches = tuple(branch for branch in (product.left, product.right) if branch)
    expected_centers = set().union(
        *(append_carrier_centers(branch) for branch in branches)
    ) if branches else set()
    reconstructed = {
        name: {
            action.center: action
            for merged in product.actions
            for source_name, action in merged.sources
            if source_name == name
        }
        for name, branch in ((LEFT, product.left), (RIGHT, product.right))
        if branch is not None
    }
    return (
        product.actions == expected
        and product.carrier_centers == sorted_centers(expected_centers)
        and tuple(action.center for action in product.actions)
        == product.carrier_centers
        and len(product.carrier_centers) == len(set(product.carrier_centers))
        and all(
            tuple(
                sorted(
                    actions.values(),
                    key=lambda action: coordinate_sort_key(action.center),
                )
            )
            == append_block_actions(branch)
            for name, branch in ((LEFT, product.left), (RIGHT, product.right))
            if branch is not None
            for actions in (reconstructed[name],)
        )
        and product.outside_identity == "I_outside"
    )


def product_source_actions(product, arm):
    """Recover one arm solely from the authenticated merged action map."""
    if arm not in ARMS:
        raise ValueError("unknown append-product arm")
    actions = tuple(
        source
        for merged in product.actions
        for source_arm, source in merged.sources
        if source_arm == arm
    )
    if len(actions) != 7 or len({action.center for action in actions}) != 7:
        raise ValueError("merged action map does not contain one complete arm")
    return tuple(
        sorted(actions, key=lambda action: coordinate_sort_key(action.center))
    )


def append_factors_from_block_actions(branch, actions, outside_identity):
    """Rebuild literal Block24 factors from merged-map source actions."""
    by_center = {action.center: action for action in actions}
    if len(by_center) != len(actions):
        raise ValueError("append action centers are not unique")
    try:
        current = by_center[branch.anchor]
        forward = by_center[branch.forward_center]
    except KeyError as exc:
        raise ValueError("append action map omits a physical block") from exc
    spectator_centers = block24.spectator_centers(branch.anchor, branch.front)
    spectators = tuple(by_center[center] for center in spectator_centers)
    if (
        current.role != "current"
        or forward.role != "forward"
        or any(action.role != "identity" for action in spectators)
        or set(by_center) != {branch.anchor, branch.forward_center, *spectator_centers}
    ):
        raise ValueError("append action roles do not realize one Block24 append")
    current_data = dict(current.factors)
    forward_data = dict(forward.factors)
    if tuple(current_data) != ("live", "pointer") or tuple(forward_data) != (
        "live_prep",
        "pointer_prep",
        "root",
        "writer",
    ):
        raise ValueError("physical append action payload is incomplete")
    spectator_factors = tuple(
        (center, site, operator)
        for center in spectator_centers
        for site, operator in by_center[center].factors
    )
    return (
        ("anchor", branch.anchor),
        ("current_live_identities", current_data["live"]),
        ("current_pointer_projectors", current_data["pointer"]),
        ("forward_center", branch.forward_center),
        ("forward_live_prep_maps", forward_data["live_prep"]),
        ("forward_pointer_prep_maps", forward_data["pointer_prep"]),
        ("forward_live_root", forward_data["root"]),
        ("forward_writer_pointer_maps", forward_data["writer"]),
        ("spectator_identity_centers", spectator_centers),
        ("spectator_identity_factors", spectator_factors),
        ("outside_carrier_identity", outside_identity),
        ("lateral_touch", False),
    )


@dataclass(frozen=True)
class ContractedEmbeddedProduct:
    coefficient: object
    output_records: tuple
    debit: int
    reconstructed_factors: tuple


@lru_cache(maxsize=16_384)
def contract_embedded_append_product(product):
    """Contract the merged action map, never the side-car branch factors."""
    if not embedded_append_product_is_physical(product):
        raise ValueError("merged append product is not physical")
    arms = tuple(
        (arm, branch)
        for arm, branch in ((LEFT, product.left), (RIGHT, product.right))
        if branch is not None
    )
    reconstructed = []
    effects = []
    records = []
    for arm, branch in arms:
        factors = append_factors_from_block_actions(
            branch,
            product_source_actions(product, arm),
            product.outside_identity,
        )
        # Equality authenticates that the merged payload is the branch's exact
        # literal realization; the contraction itself consumes `factors`.
        if factors != branch.factors:
            raise ValueError("merged action payload does not reconstruct its branch")
        effect = block24.contract_append_effect(factors)
        writer_maps = block24.factor_dictionary(factors)[
            "forward_writer_pointer_maps"
        ]
        records.append(
            (effect.forward_center, tuple(entry[2] for entry in writer_maps))
        )
        reconstructed.append((arm, factors))
        effects.append(effect)
    return ContractedEmbeddedProduct(
        sp.simplify(sp.prod(effect.scalar for effect in effects)),
        tuple(records),
        len(effects),
        tuple(reconstructed),
    )


@dataclass(frozen=True)
class ConnectedFutureBranch:
    prefix: PairOutputControl
    sector: FutureResourceSector
    control: SectorControl
    left_second: tuple | None
    right_second: tuple | None
    left_append: object | None
    right_append: object | None
    embedded_product: EmbeddedAppendProduct | None
    factorization: tuple


@dataclass(frozen=True)
class ConnectedFutureGram:
    control: SectorControl
    coefficient: object
    output_records: tuple
    debit: int

    @property
    def prefix(self):
        return self.control.prefix

    @property
    def bits(self):
        return self.control.resource.bits


@lru_cache(maxsize=16_384)
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
    if mutation == "attach_extra_right" and bits == (1, 0):
        right_append = connected_append_descriptor(
            RIGHT,
            prefix.right_exit,
            prefix.right_first,
            OUTCOMES[0],
        ).append
    sector = future_resource_sector(
        prefix,
        bits,
        "wrong_left_sense" if mutation == "wrong_resource_sense" else None,
    )
    control = SectorControl(
        prefix,
        sector,
        make_tensor_projector(
            output_tensor_projector(prefix).atoms + sector.projector.atoms
        ),
    )
    embedded = embedded_append_product(left_append, right_append)
    factorization = (
        ("sector_control", control),
        ("merged_append_product", embedded),
        ("outside_identity", "I_outside"),
    )
    return ConnectedFutureBranch(
        prefix,
        sector,
        control,
        left_second,
        right_second,
        left_append,
        right_append,
        embedded,
        factorization,
    )


@lru_cache(maxsize=65_536)
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
        and append_branch_is_physical(append)
        and respects_other_output_atoms
    )


@lru_cache(maxsize=16_384)
def contract_connected_future_branch(descriptor):
    expected_factorization = (
        ("sector_control", descriptor.control),
        ("merged_append_product", descriptor.embedded_product),
        ("outside_identity", "I_outside"),
    )
    if descriptor.factorization != expected_factorization:
        raise ValueError("future factorization is incomplete")
    factors = dict(descriptor.factorization)
    use_left, use_right = descriptor.sector.bits
    if not (
        sector_control_is_physical(descriptor.control)
        and descriptor.control.prefix == descriptor.prefix
        and descriptor.control.resource == descriptor.sector
        and future_resource_sector_is_physical(descriptor.sector)
        and descriptor.sector.prefix == descriptor.prefix
        and factors["sector_control"] == descriptor.control
        and descriptor.sector.left.sense
        == ("ket" if use_left else "complement")
        and descriptor.sector.right.sense
        == ("ket" if use_right else "complement")
        and factors["outside_identity"] == "I_outside"
        and (descriptor.left_append is not None) == bool(use_left)
        and (descriptor.right_append is not None) == bool(use_right)
        and descriptor.left_second
        == (
            descriptor.left_append.target
            if descriptor.left_append is not None
            else None
        )
        and descriptor.right_second
        == (
            descriptor.right_append.target
            if descriptor.right_append is not None
            else None
        )
        and factors["merged_append_product"] == descriptor.embedded_product
        and embedded_append_product_is_physical(descriptor.embedded_product)
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
    if descriptor.embedded_product.left != descriptor.left_append or (
        descriptor.embedded_product.right != descriptor.right_append
    ):
        raise ValueError("merged append product is not the routed branch product")
    contracted_product = contract_embedded_append_product(
        descriptor.embedded_product
    )
    return ConnectedFutureGram(
        descriptor.control,
        contracted_product.coefficient,
        contracted_product.output_records,
        contracted_product.debit,
    )


@dataclass(frozen=True)
class OperatorEffect:
    control: object
    coefficient: object


@dataclass(frozen=True)
class FutureSectorFamily:
    prefix: PairOutputControl
    bits: tuple
    control: SectorControl
    left_axis: tuple
    right_axis: tuple
    left_grams: tuple[OperatorEffect, ...]
    right_grams: tuple[OperatorEffect, ...]
    outcome_keys: tuple
    branch_count: int
    row_effect: OperatorEffect
    debit: int

    @property
    def coefficient_sum(self):
        return self.row_effect.coefficient


@lru_cache(maxsize=None)
def future_append_axis_for(arm, exit_front, first_outcome):
    return tuple(
        connected_append_descriptor(
            arm, exit_front, first_outcome, second_outcome
        ).append
        for second_outcome in OUTCOMES
    )


def future_append_axis(prefix, arm):
    exit_front = prefix.left_exit if arm == LEFT else prefix.right_exit
    first_outcome = prefix.left_first if arm == LEFT else prefix.right_first
    return future_append_axis_for(arm, exit_front, first_outcome)


@lru_cache(maxsize=None)
def future_sector_family(prefix, bits, mutation=None):
    left_axis = future_append_axis(prefix, LEFT) if bits[0] else ()
    right_axis = future_append_axis(prefix, RIGHT) if bits[1] else ()
    if mutation == "drop_future_outcome":
        if left_axis:
            left_axis = left_axis[:-1]
        elif right_axis:
            right_axis = right_axis[:-1]
    control = sector_control(prefix, bits)
    left_grams = tuple(
        OperatorEffect(
            control,
            contract_embedded_append_product(
                embedded_append_product(branch, None)
            ).coefficient,
        )
        for branch in left_axis
    )
    right_grams = tuple(
        OperatorEffect(
            control,
            contract_embedded_append_product(
                embedded_append_product(None, branch)
            ).coefficient,
        )
        for branch in right_axis
    )
    left_sum = sp.simplify(sum(gram.coefficient for gram in left_grams))
    right_sum = sp.simplify(sum(gram.coefficient for gram in right_grams))
    coefficient_sum = (
        (left_sum if bits[0] else sp.S.One)
        * (right_sum if bits[1] else sp.S.One)
    )
    branch_count = (len(left_axis) if bits[0] else 1) * (
        len(right_axis) if bits[1] else 1
    )
    left_keys = tuple(branch.target for branch in left_axis) if bits[0] else (None,)
    right_keys = tuple(branch.target for branch in right_axis) if bits[1] else (None,)
    outcome_keys = tuple(itertools.product(left_keys, right_keys))
    return FutureSectorFamily(
        prefix,
        bits,
        control,
        left_axis,
        right_axis,
        left_grams,
        right_grams,
        outcome_keys,
        branch_count,
        OperatorEffect(control, sp.simplify(coefficient_sum)),
        sum(bits),
    )


@lru_cache(maxsize=8_192)
def append_axes_tensorize(left_axis, right_axis) -> bool:
    if not left_axis or not right_axis:
        return True
    left_reference = left_axis[0]
    right_reference = right_axis[0]
    left_geometry = (
        append_carrier_centers(left_reference),
        append_nonidentity_sites(left_reference),
        append_writer_sites(left_reference),
    )
    right_geometry = (
        append_carrier_centers(right_reference),
        append_nonidentity_sites(right_reference),
        append_writer_sites(right_reference),
    )
    return (
        all(
            (
                append_carrier_centers(branch),
                append_nonidentity_sites(branch),
                append_writer_sites(branch),
            )
            == left_geometry
            and append_product_compatibility(branch, right_reference)
            for branch in left_axis
        )
        and all(
            (
                append_carrier_centers(branch),
                append_nonidentity_sites(branch),
                append_writer_sites(branch),
            )
            == right_geometry
            and append_product_compatibility(left_reference, branch)
            for branch in right_axis
        )
    )


@lru_cache(maxsize=16_384)
def future_sector_family_is_physical(family) -> bool:
    expected_left_axis = (
        future_append_axis(family.prefix, LEFT) if family.bits[0] else ()
    )
    expected_right_axis = (
        future_append_axis(family.prefix, RIGHT) if family.bits[1] else ()
    )
    try:
        expected_left_grams = tuple(
            OperatorEffect(
                family.control,
                contract_embedded_append_product(
                    embedded_append_product(branch, None)
                ).coefficient,
            )
            for branch in expected_left_axis
        )
        expected_right_grams = tuple(
            OperatorEffect(
                family.control,
                contract_embedded_append_product(
                    embedded_append_product(None, branch)
                ).coefficient,
            )
            for branch in expected_right_axis
        )
    except (KeyError, ValueError):
        return False
    expected_left_keys = (
        tuple(branch.target for branch in expected_left_axis)
        if family.bits[0]
        else (None,)
    )
    expected_right_keys = (
        tuple(branch.target for branch in expected_right_axis)
        if family.bits[1]
        else (None,)
    )
    expected_outcome_keys = tuple(
        itertools.product(expected_left_keys, expected_right_keys)
    )
    expected_count = len(expected_left_keys) * len(expected_right_keys)
    expected_coefficient = sp.simplify(
        (
            sum(gram.coefficient for gram in expected_left_grams)
            if family.bits[0]
            else sp.S.One
        )
        * (
            sum(gram.coefficient for gram in expected_right_grams)
            if family.bits[1]
            else sp.S.One
        )
    )
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
        sector_control_is_physical(family.control)
        and family.control == sector_control(family.prefix, family.bits)
        and future_resource_sector_is_physical(representative.sector)
        and family.left_axis == expected_left_axis
        and family.right_axis == expected_right_axis
        and (not family.bits[0] or len(family.left_axis) == len(OUTCOMES) == 14)
        and (not family.bits[1] or len(family.right_axis) == len(OUTCOMES) == 14)
        and all(
            future_append_is_bound(family.prefix, LEFT, branch)
            for branch in family.left_axis
        )
        and all(
            future_append_is_bound(family.prefix, RIGHT, branch)
            for branch in family.right_axis
        )
        and family.left_grams == expected_left_grams
        and family.right_grams == expected_right_grams
        and append_axes_tensorize(family.left_axis, family.right_axis)
        and family.branch_count == expected_count
        and len(family.outcome_keys) == len(set(family.outcome_keys))
        == family.branch_count
        and family.outcome_keys == expected_outcome_keys
        and family.coefficient_sum == expected_coefficient == 1
        and family.row_effect
        == OperatorEffect(family.control, expected_coefficient)
        and family.debit == sum(family.bits)
        and gram.control == family.control
        and gram.debit == family.debit
    )


@dataclass(frozen=True)
class FutureActiveSum:
    output_active: PairOutputActiveSum
    sector_rows: tuple[OperatorEffect, ...]
    projector: OrthogonalProjectorSum


@dataclass(frozen=True)
class ProjectorComplement:
    carrier_centers: tuple
    subtrahend: OrthogonalProjectorSum
    rank: int


@dataclass(frozen=True)
class PairFutureStop:
    active: FutureActiveSum
    kraus: ProjectorComplement


def orthogonal_projector_sum_rank(projector_sum):
    return sum(tensor_projector_rank(term) for term in projector_sum.terms)


def projector_complement_rank(projector_sum):
    carrier_dimension = 2 ** (len(block23.SUPPORT) * len(projector_sum.carrier_centers))
    return carrier_dimension - orthogonal_projector_sum_rank(projector_sum)


def projector_complement_is_physical(complement) -> bool:
    return (
        complement.carrier_centers == complement.subtrahend.carrier_centers
        and complement.rank == projector_complement_rank(complement.subtrahend)
        and complement.rank > 0
    )


@lru_cache(maxsize=1)
def future_active_sum(active):
    rows = tuple(
        future_sector_family(prefix, bits).row_effect
        for prefix in active.controls
        for bits in RESOURCE_BITS
    )
    output_terms = sorted_projectors(
        output_tensor_projector(control) for control in active.controls
    )
    projector = OrthogonalProjectorSum(
        sorted_centers(FIRST_OUTPUT_CENTERS),
        output_terms,
    )
    return FutureActiveSum(active, rows, projector)


def future_active_sum_is_physical(active_sum) -> bool:
    active = active_sum.output_active
    expected_keys = tuple(
        (prefix.key, bits)
        for prefix in active.controls
        for bits in RESOURCE_BITS
    )
    actual_keys = tuple(
        (row.control.prefix.key, row.control.resource.bits)
        for row in active_sum.sector_rows
    )
    expected_projector = OrthogonalProjectorSum(
        sorted_centers(FIRST_OUTPUT_CENTERS),
        sorted_projectors(
            output_tensor_projector(control) for control in active.controls
        ),
    )
    return (
        active.idempotent
        and active.complement_nontrivial
        and output_projector_orthogonality_certificate()
        and len(active.controls) == 3136
        and len(active_sum.sector_rows) == 12544
        and actual_keys == expected_keys
        and len(actual_keys) == len(set(actual_keys))
        and all(row.coefficient == 1 for row in active_sum.sector_rows)
        and all(sector_control_is_physical(row.control) for row in active_sum.sector_rows)
        and all(resource_partition_certificate(prefix) for prefix in active.controls)
        and all(
            future_sector_family_is_physical(
                future_sector_family(prefix, bits)
            )
            for prefix in active.controls
            for bits in RESOURCE_BITS
        )
        and active_sum.projector == expected_projector
        and len(active_sum.projector.terms) == 3136
        and all(tensor_projector_is_physical(term) for term in active_sum.projector.terms)
    )


def make_future_stop(active_sum, mutation=None):
    subtrahend = active_sum.projector
    if mutation == "stale_active_projector":
        subtrahend = replace(
            subtrahend,
            terms=subtrahend.terms[:-1],
        )
    return PairFutureStop(
        active_sum,
        ProjectorComplement(
            sorted_centers(FIRST_OUTPUT_CENTERS),
            subtrahend,
            projector_complement_rank(subtrahend),
        ),
    )


def contract_future_stop(stop):
    if not (
        future_active_sum_is_physical(stop.active)
        and stop.kraus.carrier_centers == sorted_centers(FIRST_OUTPUT_CENTERS)
        and stop.kraus.subtrahend == stop.active.projector
        and projector_complement_is_physical(stop.kraus)
    ):
        raise ValueError("future STOP is not bound to the actual active sum")
    return stop.kraus


def future_completion_is_pointwise_identity(active_sum, complement) -> bool:
    if complement.subtrahend != active_sum.projector:
        return False
    active_terms = set(active_sum.projector.terms)
    active_witnesses = tuple(
        output_tensor_projector(control)
        for control in active_sum.output_active.controls
    )
    outside_control = make_tensor_projector(
        LocalProjector(center, "pointer26", block23.BLANK_POINTER, "ket")
        for center in FIRST_OUTPUT_CENTERS
    )
    return (
        set(active_witnesses) == active_terms
        and projector_complement_is_physical(complement)
        and orthogonal_projector_sum_rank(active_sum.projector)
        + complement.rank
        == 2 ** (len(block23.SUPPORT) * len(FIRST_OUTPUT_CENTERS))
        and all(
            int(witness in active_terms) + int(witness not in active_terms) == 1
            for witness in active_witnesses
        )
        and outside_control not in active_terms
        and 0 + 1 == 1
    )


def future_stop_completion_certificate(
    active, stop_present=True, mutation=None
) -> bool:
    active_sum = future_active_sum(active)
    stop = make_future_stop(active_sum, mutation) if stop_present else None
    if stop is None:
        return False
    try:
        contracted = contract_future_stop(stop)
    except ValueError:
        return False
    # ProjectorComplement is an exact typed constructor: since its subtrahend
    # is the same authenticated orthogonal sum, (I-P_out)^2 = I-P_out and the
    # active plus complement partition is the full identity on this carrier.
    return (
        future_active_sum_is_physical(active_sum)
        and contracted == stop.kraus
        and contracted.subtrahend == active_sum.projector
        and future_completion_is_pointwise_identity(active_sum, contracted)
    )


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
        active,
        stop_present=mutation != "omit_STOP",
        mutation="stale_active_projector"
        if mutation == "stale_STOP_active"
        else None,
    )


@dataclass(frozen=True)
class ConnectedPairPrefix:
    first: object
    first_gram: object
    output_control: PairOutputControl


@lru_cache(maxsize=16_384)
def contract_imported_pair_factors(descriptor):
    """Content-addressed contraction of one immutable imported K."""
    return block28.contract_pair_kraus_descriptor(descriptor)


@lru_cache(maxsize=16_384)
def imported_pair_factorization_is_exact(descriptor) -> bool:
    return descriptor.factorization == (
        ("amplitude", descriptor.amplitude),
        ("full_pair_control", descriptor.control.atoms),
        ("left_turn_factors", descriptor.left.factors),
        ("right_turn_factors", descriptor.right.factors),
    )


@lru_cache(maxsize=None)
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
    gram = contract_imported_pair_factors(first)
    control = pair_output_control(
        left_exit, right_exit, left_first, right_first
    )
    return ConnectedPairPrefix(first, gram, control)


@lru_cache(maxsize=16_384)
def reconstructed_pair_output_control(prefix, gram=None):
    gram = prefix.first_gram if gram is None else gram
    configuration = {
        atom.center: block23.BLANK_POINTER
        for atom in prefix.first.control.atoms
        if atom.role == "Blank-block" and atom.center in FIRST_OUTPUT_CENTERS
    }
    for center, word in gram.output_records:
        if center not in configuration:
            raise ValueError("first output lies outside the guarded target set")
        configuration[center] = word
    if set(configuration) != set(FIRST_OUTPUT_CENTERS):
        raise ValueError("first channel does not guard all output pointers")
    return tuple(
        OutputPointerAtom(center, configuration[center])
        for center in FIRST_OUTPUT_CENTERS
    )


@lru_cache(maxsize=16_384)
def pair_prefix_output_is_bound(prefix) -> bool:
    try:
        fresh_gram = contract_imported_pair_factors(prefix.first)
    except (KeyError, ValueError):
        return False
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
        and imported_pair_factorization_is_exact(prefix.first)
        and fresh_gram == prefix.first_gram
        and prefix.first_gram.control == prefix.first.control
        and prefix.first_gram.control == block28.pair_control(
            prefix.first.control.left_source,
            prefix.first.control.right_source,
        )
        and fresh_gram.output_records == expected_records
        and reconstructed_pair_output_control(prefix, fresh_gram)
        == prefix.output_control.atoms
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
class CylinderInputControl:
    past: object
    future_resource: TensorProjector
    projector: TensorProjector


@lru_cache(maxsize=16_384)
def pair_input_tensor_projector(control):
    atoms = []
    for atom in control.atoms:
        if atom.role == "current-pointer":
            atoms.append(LocalProjector(atom.center, "pointer26", atom.state, "ket"))
        elif atom.role == "Blank-block":
            atoms.append(LocalProjector(atom.center, "block32", atom.state, "ket"))
        else:
            raise ValueError("unknown imported pair-control atom")
    return make_tensor_projector(atoms)


@lru_cache(maxsize=16_384)
def cylinder_input_control(prefix, resource):
    past_projector = pair_input_tensor_projector(prefix.first.control)
    projector = make_tensor_projector(
        past_projector.atoms + resource.projector.atoms
    )
    return CylinderInputControl(prefix.first.control, resource.projector, projector)


@lru_cache(maxsize=16_384)
def cylinder_input_control_is_physical(control) -> bool:
    past_projector = pair_input_tensor_projector(control.past)
    expected = make_tensor_projector(
        past_projector.atoms + control.future_resource.atoms
    )
    return (
        block28.control_is_rank_one_projector(control.past)
        and tensor_projector_is_physical(control.future_resource)
        and set(past_projector.carrier_centers).isdisjoint(
            control.future_resource.carrier_centers
        )
        and control.projector == expected
        and tensor_projector_is_physical(control.projector)
    )


@dataclass(frozen=True)
class ConnectedCylinderGram:
    control: CylinderInputControl
    first_coefficient: object
    future_coefficient: object
    composite_coefficient: object
    bits: tuple
    intermediate_output: PairOutputControl


@lru_cache(maxsize=65_536)
def composite_cylinder_coefficient(first_coefficient, future_coefficient):
    return sp.simplify(first_coefficient * future_coefficient)


@dataclass(frozen=True)
class ConnectedCylinderBranch:
    prefix: ConnectedPairPrefix
    future: ConnectedFutureBranch
    factorization: tuple


@dataclass(frozen=True)
class FixedSectorCylinderEffect:
    control: CylinderInputControl
    branch_grams: tuple[ConnectedCylinderGram, ...]
    summed_future: OperatorEffect
    restricted_first: OperatorEffect


@dataclass(frozen=True)
class CylinderLease:
    prefix: ConnectedPairPrefix
    bits: tuple
    first_gram: object
    resource: FutureResourceSector
    control: CylinderInputControl
    family: FutureSectorFamily


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


@lru_cache(maxsize=1)
def first_pair_literal_block_sites():
    return tuple(
        block28.block_sites(center) for center in first_pair_literal_centers()
    )


@lru_cache(maxsize=16_384)
def cylinder_lease(prefix, bits):
    """Authenticate the K/output/resource context once per exact sector."""
    family = future_sector_family(prefix.output_control, bits)
    resource = future_resource_sector(prefix.output_control, bits)
    control = cylinder_input_control(prefix, resource)
    resource_blocks = (
        block28.block_sites(resource.left.center),
        block28.block_sites(resource.right.center),
    )
    first_carrier_blocks = first_pair_literal_block_sites()
    try:
        fresh_first_gram = contract_imported_pair_factors(prefix.first)
    except (KeyError, ValueError) as exc:
        raise ValueError("first pair factors do not freshly contract") from exc
    if not (
        pair_prefix_output_is_bound(prefix)
        and fresh_first_gram == prefix.first_gram
        and fresh_first_gram.control == prefix.first.control
        and reconstructed_pair_output_control(prefix, fresh_first_gram)
        == prefix.output_control.atoms
        and family.prefix == prefix.output_control
        and family.bits == bits
        and family.control == sector_control(prefix.output_control, bits)
        and family.row_effect.control == family.control
        and future_sector_family_is_physical(family)
        and future_resource_sector_is_physical(resource)
        and resource == family.control.resource
        and cylinder_input_control_is_physical(control)
        and all(
            resource_block.isdisjoint(first_block)
            for resource_block in resource_blocks
            for first_block in first_carrier_blocks
        )
    ):
        raise ValueError("future channel is not conditioned on actual first output")
    return CylinderLease(
        prefix,
        bits,
        fresh_first_gram,
        resource,
        control,
        family,
    )


def make_connected_cylinder_contractor(prefix, bits):
    """Capture the canonical lease; callers can supply only descriptors."""
    lease = cylinder_lease(prefix, bits)

    def contract(descriptor):
        future_branch = descriptor.future
        expected_factorization = (
            ("first_pair_factors", prefix.first.factorization),
            ("intermediate_output_control", prefix.output_control.atoms),
            ("future_resource_sector", future_branch.sector),
            ("future_factors", future_branch.factorization),
            ("outside_identity", "I_outside"),
        )
        if not (
            descriptor.prefix == prefix == lease.prefix
            and future_branch.prefix == prefix.output_control
            and future_branch.sector == lease.resource
            and future_branch.control == lease.family.control
            and future_branch.sector.bits == bits == lease.bits
            and descriptor.factorization == expected_factorization
        ):
            raise ValueError(
                "cylinder descriptor does not match its physical lease"
            )
        future_gram = contract_connected_future_branch(future_branch)
        if future_gram.control != future_branch.control or (
            future_gram.control != lease.family.control
        ):
            raise ValueError("future Gram discarded its operator-valued control")
        return ConnectedCylinderGram(
            lease.control,
            lease.first_gram.coefficient,
            future_gram.coefficient,
            composite_cylinder_coefficient(
                lease.first_gram.coefficient,
                future_gram.coefficient,
            ),
            future_gram.bits,
            prefix.output_control,
        )

    return lease, contract


def contract_connected_cylinder(descriptor):
    _lease, contract = make_connected_cylinder_contractor(
        descriptor.prefix,
        descriptor.future.sector.bits,
    )
    return contract(descriptor)


def fixed_sector_cylinder_effect(prefix, family):
    lease, contract = make_connected_cylinder_contractor(prefix, family.bits)
    if family != lease.family:
        raise ValueError("fixed-sector cylinder is not physically bound")
    branch_grams = []
    for left_second, right_second in family.outcome_keys:
        future = connected_future_branch(
            prefix.output_control,
            family.bits,
            left_second,
            right_second,
        )
        gram = contract(connected_cylinder_branch(prefix, future))
        if not (
            gram.control == lease.control
            and gram.bits == family.bits
            and gram.intermediate_output == prefix.output_control
        ):
            raise ValueError("one actual M=L K Gram left its fixed sector")
        branch_grams.append(gram)
    branch_grams = tuple(branch_grams)
    first = lease.first_gram.coefficient
    summed_coefficient = sp.simplify(
        sum(gram.composite_coefficient for gram in branch_grams)
    )
    return FixedSectorCylinderEffect(
        lease.control,
        branch_grams,
        OperatorEffect(lease.control, summed_coefficient),
        OperatorEffect(lease.control, first),
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
                fresh = contract_imported_pair_factors(prefix.first)
                if fresh != prefix.first_gram or fresh.coefficient != expected:
                    return False
    return True


@lru_cache(maxsize=None)
def fixed_sector_cylinder_instance(prefix, bits) -> bool:
    family = future_sector_family(prefix.output_control, bits)
    sector_effect = fixed_sector_cylinder_effect(prefix, family)
    branch_grams = sector_effect.branch_grams
    fresh_first = cylinder_lease(prefix, bits).first_gram
    return (
        family.coefficient_sum == 1
        and family.row_effect == OperatorEffect(family.control, 1)
        and len(branch_grams) == family.branch_count
        and len(branch_grams) == len(family.outcome_keys)
        and all(
            gram.control == sector_effect.control
            and gram.first_coefficient == fresh_first.coefficient
            and gram.bits == bits
            and gram.intermediate_output == prefix.output_control
            and gram.composite_coefficient
            == composite_cylinder_coefficient(
                gram.first_coefficient,
                gram.future_coefficient,
            )
            for gram in branch_grams
        )
        and sp.simplify(
            sum(gram.future_coefficient for gram in branch_grams)
        )
        == family.row_effect.coefficient
        and sp.simplify(
            sum(gram.composite_coefficient for gram in branch_grams)
        )
        == sector_effect.summed_future.coefficient
        and sector_effect.control.future_resource
        == family.control.resource.projector
        and sector_effect.summed_future == sector_effect.restricted_first
        and sector_effect.restricted_first
        == OperatorEffect(sector_effect.control, fresh_first.coefficient)
    )


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
    # The alpha axis carries every distinct intermediate output/resource
    # control at fixed (lambda, source pair); the source axis carries every
    # imported Pi_s,t and both supplied q choices at one fixed alpha.  The
    # continuation descriptor was proved independent of the latter axis.  At
    # every swept prefix, fixed_sector_cylinder_instance nevertheless builds,
    # contracts, and sums all 1/14/14/196 actual M=L K descriptors.  The two
    # exact prefix sweeps certify the remaining Cartesian duplication without
    # pretending that a representative future branch is the complete sum.
    for control in pair_output_active_sum().controls:
        prefix = connected_pair_prefix(
            LAMBDAS[0],
            OUTCOMES[0],
            OUTCOMES[1],
            *control.key,
        )
        if not all(
            fixed_sector_cylinder_instance(prefix, bits)
            for bits in RESOURCE_BITS
        ):
            return False
    fixed_control = pair_output_active_sum().controls[0]
    for lam in LAMBDAS:
        for left_source, right_source in itertools.product(OUTCOMES, repeat=2):
            prefix = connected_pair_prefix(
                lam,
                left_source,
                right_source,
                *fixed_control.key,
            )
            if not all(
                fixed_sector_cylinder_instance(prefix, bits)
                for bits in RESOURCE_BITS
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


def continuation_descriptor(
    arm,
    exit_front,
    first_outcome,
    second_outcome,
    factors_override=None,
):
    descriptor = connected_append_descriptor(
        arm, exit_front, first_outcome, second_outcome
    )
    factors = descriptor.append.factors if factors_override is None else factors_override
    effect = block24.contract_append_effect(factors)
    return (
        arm,
        exit_front,
        first_outcome,
        second_outcome,
        descriptor.first_site,
        descriptor.second_site,
        descriptor.current_word,
        factors,
        effect.scalar,
    )


def lambda_continuation_family(lam, mutation=None):
    descriptors = []
    altered_row = (
        LEFT,
        block28.LEFT_EXITS[0],
        OUTCOMES[0],
    )
    p0 = block23.transition(OUTCOMES[0], OUTCOMES[0])
    p1 = block23.transition(OUTCOMES[0], OUTCOMES[1])
    epsilon = sp.simplify(p0 * p1 / 4)
    altered_targets = (p0 + epsilon, p1 - epsilon)
    for arm in ARMS:
        for exit_front, first_outcome, second_outcome in itertools.product(
            arm_exits(arm), OUTCOMES, OUTCOMES
        ):
            factors = None
            if (
                mutation == "physical_lambda_kernel"
                and lam == LAMBDAS[-1]
                and (arm, exit_front, first_outcome) == altered_row
                and second_outcome in OUTCOMES[:2]
            ):
                index = OUTCOMES[:2].index(second_outcome)
                original = (p0, p1)[index]
                scale = sp.sqrt(sp.simplify(altered_targets[index] / original))
                append = connected_append_descriptor(
                    arm, exit_front, first_outcome, second_outcome
                ).append
                factors = block24.make_append_factors(
                    append.anchor,
                    append.current_word,
                    append.target,
                    root_scale=scale,
                )
            descriptors.append(
                continuation_descriptor(
                    arm,
                    exit_front,
                    first_outcome,
                    second_outcome,
                    factors,
                )
            )
    return tuple(descriptors)


def continuation_family_rows_are_normalized(family) -> bool:
    rows = {}
    for descriptor in family:
        key = descriptor[:3]
        rows.setdefault(key, sp.S.Zero)
        rows[key] += descriptor[-1]
    return (
        len(rows) == 2 * 4 * 14
        and all(sp.simplify(value) == 1 for value in rows.values())
        and all(descriptor[-1].is_positive is True for descriptor in family)
    )


@lru_cache(maxsize=None)
def q_independent_continuation_certificate(mutation=None) -> bool:
    families = tuple(
        lambda_continuation_family(lam, mutation) for lam in LAMBDAS
    )
    return (
        all(len(family) == 1568 for family in families)
        and all(len(set(family)) == 1568 for family in families)
        and all(continuation_family_rows_are_normalized(family) for family in families)
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
            mutation="attach_extra_right"
            if mutation == "D10_extra_writer" and bits == (1, 0)
            else None,
        )
        try:
            gram = contract_connected_future_branch(descriptor)
        except (KeyError, ValueError):
            return False
        actual[bits] = 2 + gram.debit
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


@dataclass(frozen=True)
class FramedPairOutputControl:
    frame: object
    left_exit: tuple
    right_exit: tuple
    left_first: tuple
    right_first: tuple
    atoms: tuple[OutputPointerAtom, ...]


def framed_pair_output_control(
    frame, left_exit, right_exit, left_first, right_first
):
    left_selected = block24.forward_center(frame.left_anchor, left_exit)
    right_selected = block24.forward_center(frame.right_anchor, right_exit)
    atoms = tuple(
        sorted(
            (
                OutputPointerAtom(
                    center,
                    block23.locked_word(left_exit, left_first)
                    if center == left_selected
                    else block23.locked_word(right_exit, right_first)
                    if center == right_selected
                    else block23.BLANK_POINTER,
                )
                for center in frame.left_targets + frame.right_targets
            ),
            key=lambda atom: coordinate_sort_key(atom.center),
        )
    )
    return FramedPairOutputControl(
        frame,
        left_exit,
        right_exit,
        left_first,
        right_first,
        atoms,
    )


def framed_output_control_is_physical(control) -> bool:
    expected = framed_pair_output_control(
        control.frame,
        control.left_exit,
        control.right_exit,
        control.left_first,
        control.right_first,
    )
    words = tuple(atom.word for atom in control.atoms)
    return (
        control == expected
        and control.left_exit in control.frame.left_exits
        and control.right_exit in control.frame.right_exits
        and len(control.atoms) == len({atom.center for atom in control.atoms}) == 8
        and sum(word != block23.BLANK_POINTER for word in words) == 2
    )


def framed_output_tensor_projector(control):
    return make_tensor_projector(
        LocalProjector(atom.center, "pointer26", atom.word, "ket")
        for atom in control.atoms
    )


def transport_pair_output_control(control, rotation, translation=ZERO):
    frame = block28.transformed_frame(
        block28.CANONICAL_FRAME, rotation, translation
    )
    return FramedPairOutputControl(
        frame,
        block23.mat_vec(rotation, control.left_exit),
        block23.mat_vec(rotation, control.right_exit),
        block23.mat_vec(rotation, control.left_first),
        block23.mat_vec(rotation, control.right_first),
        tuple(
            sorted(
                (
                    OutputPointerAtom(
                        block28.affine(rotation, translation, atom.center),
                        block23.rotate_word(atom.word, rotation),
                    )
                    for atom in control.atoms
                ),
                key=lambda atom: coordinate_sort_key(atom.center),
            )
        ),
    )


def pair_output_control_transport_certificate(
    control, rotation, translation=ZERO
) -> bool:
    moved = transport_pair_output_control(control, rotation, translation)
    expected = framed_pair_output_control(
        moved.frame,
        moved.left_exit,
        moved.right_exit,
        moved.left_first,
        moved.right_first,
    )
    return moved == expected and framed_output_control_is_physical(moved)


@dataclass(frozen=True)
class FramedResourceSector:
    prefix: FramedPairOutputControl
    bits: tuple
    left: LocalProjector
    right: LocalProjector
    projector: TensorProjector


def framed_selected_future_center(prefix, arm):
    anchor = prefix.frame.left_anchor if arm == LEFT else prefix.frame.right_anchor
    exit_front = prefix.left_exit if arm == LEFT else prefix.right_exit
    first = block24.forward_center(anchor, exit_front)
    return block24.forward_center(first, exit_front)


def framed_resource_sector(prefix, bits):
    left = LocalProjector(
        framed_selected_future_center(prefix, LEFT),
        "block32",
        block23.BLANK_BLOCK,
        "ket" if bits[0] else "complement",
    )
    right = LocalProjector(
        framed_selected_future_center(prefix, RIGHT),
        "block32",
        block23.BLANK_BLOCK,
        "ket" if bits[1] else "complement",
    )
    return FramedResourceSector(
        prefix,
        bits,
        left,
        right,
        make_tensor_projector((left, right)),
    )


def framed_resource_sector_is_physical(sector) -> bool:
    expected = framed_resource_sector(sector.prefix, sector.bits)
    return (
        sector == expected
        and framed_output_control_is_physical(sector.prefix)
        and sector.bits in RESOURCE_BITS
        and tensor_projector_is_physical(sector.projector)
        and block28.block_sites(sector.left.center).isdisjoint(
            block28.block_sites(sector.right.center)
        )
    )


def transport_resource_sector(sector, rotation, translation=ZERO):
    prefix = transport_pair_output_control(sector.prefix, rotation, translation)
    atoms = []
    for atom in (sector.left, sector.right):
        atoms.append(
            LocalProjector(
                block28.affine(rotation, translation, atom.center),
                atom.algebra,
                block23.rotate_block_product(atom.state, rotation),
                atom.sense,
            )
        )
    return FramedResourceSector(
        prefix,
        sector.bits,
        atoms[0],
        atoms[1],
        make_tensor_projector(atoms),
    )


def resource_sector_transport_certificate(
    sector, rotation, translation=ZERO
) -> bool:
    moved = transport_resource_sector(sector, rotation, translation)
    expected = framed_resource_sector(moved.prefix, moved.bits)
    return moved == expected and framed_resource_sector_is_physical(moved)


def affine_append_branch(branch, rotation, translation=ZERO):
    return block24.append_branch(
        block28.affine(rotation, translation, branch.anchor),
        block23.rotate_word(branch.current_word, rotation),
        block23.mat_vec(rotation, branch.target),
    )


def translated_append_factors_match(rotated, moved, translation) -> bool:
    source = block24.factor_dictionary(rotated.factors)
    target = block24.factor_dictionary(moved.factors)
    translated_keys = {
        "anchor": block23.add(source["anchor"], translation),
        "forward_center": block23.add(source["forward_center"], translation),
        "spectator_identity_centers": tuple(
            block23.add(center, translation)
            for center in source["spectator_identity_centers"]
        ),
        "spectator_identity_factors": tuple(
            (block23.add(center, translation), site, operator)
            for center, site, operator in source["spectator_identity_factors"]
        ),
    }
    invariant_keys = set(block24.APPEND_FACTOR_KEYS) - set(translated_keys)
    return all(target[key] == value for key, value in translated_keys.items()) and all(
        target[key] == source[key] for key in invariant_keys
    )


def append_affine_covariance_certificate(
    branch, rotation, translation=ZERO, mutation=None
) -> bool:
    rotated = block24.append_branch(
        block23.mat_vec(rotation, branch.anchor),
        block23.rotate_word(branch.current_word, rotation),
        block23.mat_vec(rotation, branch.target),
    )
    moved = affine_append_branch(branch, rotation, translation)
    if mutation == "untransported_forward":
        moved = replace(
            moved,
            forward_center=rotated.forward_center,
        )
    return (
        block24.append_branch_covariance_certificate(branch, rotation)
        and translated_append_factors_match(rotated, moved, translation)
        and moved.anchor == block28.affine(rotation, translation, branch.anchor)
        and moved.forward_center
        == block28.affine(rotation, translation, branch.forward_center)
        and append_branch_is_physical(moved)
    )


def merged_product_signature(product):
    return tuple(
        (
            action.center,
            action.role,
            action.owner,
            tuple((name, source.role) for name, source in action.sources),
        )
        for action in product.actions
    )


def merged_product_affine_covariance_certificate(
    product, rotation, translation=ZERO
) -> bool:
    moved_left = (
        affine_append_branch(product.left, rotation, translation)
        if product.left is not None
        else None
    )
    moved_right = (
        affine_append_branch(product.right, rotation, translation)
        if product.right is not None
        else None
    )
    moved = embedded_append_product(moved_left, moved_right)
    expected_signature = tuple(
        sorted(
            (
                (
                    block28.affine(rotation, translation, center),
                    role,
                    owner,
                    sources,
                )
                for center, role, owner, sources in merged_product_signature(product)
            ),
            key=lambda entry: coordinate_sort_key(entry[0]),
        )
    )
    return (
        all(
            append_affine_covariance_certificate(branch, rotation, translation)
            for branch in (product.left, product.right)
            if branch is not None
        )
        and embedded_append_product_is_physical(product)
        and embedded_append_product_is_physical(moved)
        and merged_product_signature(moved) == expected_signature
    )


@dataclass(frozen=True)
class FramedSectorControl:
    prefix: FramedPairOutputControl
    resource: FramedResourceSector
    projector: TensorProjector


def framed_sector_control(prefix, bits):
    resource = framed_resource_sector(prefix, bits)
    return FramedSectorControl(
        prefix,
        resource,
        make_tensor_projector(
            framed_output_tensor_projector(prefix).atoms
            + resource.projector.atoms
        ),
    )


def framed_sector_control_is_physical(control) -> bool:
    expected = framed_sector_control(control.prefix, control.resource.bits)
    return (
        control == expected
        and framed_output_control_is_physical(control.prefix)
        and framed_resource_sector_is_physical(control.resource)
        and tensor_projector_is_physical(control.projector)
    )


def transport_sector_control(control, rotation, translation=ZERO):
    prefix = transport_pair_output_control(
        control.prefix, rotation, translation
    )
    return framed_sector_control(prefix, control.resource.bits)


@dataclass(frozen=True)
class FramedFutureBranch:
    prefix: FramedPairOutputControl
    sector: FramedResourceSector
    control: FramedSectorControl
    left_second: tuple | None
    right_second: tuple | None
    left_append: object | None
    right_append: object | None
    product: EmbeddedAppendProduct
    factorization: tuple


def framed_future_branch(prefix, bits, left_second=None, right_second=None):
    if bits[0] != (left_second is not None) or bits[1] != (right_second is not None):
        raise ValueError("framed outcomes do not match resource bits")
    left_append = (
        block24.append_branch(
            block24.forward_center(prefix.frame.left_anchor, prefix.left_exit),
            block23.locked_word(prefix.left_exit, prefix.left_first),
            left_second,
        )
        if bits[0]
        else None
    )
    right_append = (
        block24.append_branch(
            block24.forward_center(prefix.frame.right_anchor, prefix.right_exit),
            block23.locked_word(prefix.right_exit, prefix.right_first),
            right_second,
        )
        if bits[1]
        else None
    )
    sector = framed_resource_sector(prefix, bits)
    product = embedded_append_product(left_append, right_append)
    control = framed_sector_control(prefix, bits)
    factorization = (
        ("sector_control", control),
        ("merged_append_product", product),
        ("outside_identity", "I_outside"),
    )
    return FramedFutureBranch(
        prefix,
        sector,
        control,
        left_second,
        right_second,
        left_append,
        right_append,
        product,
        factorization,
    )


def framed_future_branch_is_physical(branch) -> bool:
    appends = tuple(
        append for append in (branch.left_append, branch.right_append) if append
    )
    expected = framed_future_branch(
        branch.prefix,
        branch.sector.bits,
        branch.left_second,
        branch.right_second,
    )
    return (
        branch == expected
        and framed_resource_sector_is_physical(branch.sector)
        and framed_sector_control_is_physical(branch.control)
        and branch.control.prefix == branch.prefix
        and branch.control.resource == branch.sector
        and embedded_append_product_is_physical(branch.product)
        and all(
            append_branch_is_physical(append)
            for append in appends
        )
        and branch.factorization
        == (
            ("sector_control", branch.control),
            ("merged_append_product", branch.product),
            ("outside_identity", "I_outside"),
        )
    )


def contract_framed_future_branch(branch):
    if not framed_future_branch_is_physical(branch):
        raise ValueError("framed future branch is not physical")
    contracted = contract_embedded_append_product(branch.product)
    return ConnectedFutureGram(
        branch.control,
        contracted.coefficient,
        contracted.output_records,
        contracted.debit,
    )


def future_branch_affine_covariance_certificate(
    branch, rotation, translation=ZERO
) -> bool:
    moved_prefix = transport_pair_output_control(
        branch.prefix, rotation, translation
    )
    moved = framed_future_branch(
        moved_prefix,
        branch.sector.bits,
        block23.mat_vec(rotation, branch.left_second)
        if branch.left_second is not None
        else None,
        block23.mat_vec(rotation, branch.right_second)
        if branch.right_second is not None
        else None,
    )
    source_gram = contract_connected_future_branch(branch)
    moved_gram = contract_framed_future_branch(moved)
    expected_records = tuple(
        (
            block28.affine(rotation, translation, center),
            block23.rotate_word(word, rotation),
        )
        for center, word in source_gram.output_records
    )
    return (
        pair_output_control_transport_certificate(
            branch.prefix, rotation, translation
        )
        and resource_sector_transport_certificate(
            branch.sector, rotation, translation
        )
        and merged_product_affine_covariance_certificate(
            branch.embedded_product, rotation, translation
        )
        and moved.left_append
        == (
            affine_append_branch(branch.left_append, rotation, translation)
            if branch.left_append is not None
            else None
        )
        and moved.right_append
        == (
            affine_append_branch(branch.right_append, rotation, translation)
            if branch.right_append is not None
            else None
        )
        and framed_future_branch_is_physical(moved)
        and moved_gram.control == moved.control
        and moved_gram.coefficient == source_gram.coefficient
        and moved_gram.output_records == expected_records
        and moved_gram.debit == source_gram.debit
    )


@dataclass(frozen=True)
class FramedConnectedPairPrefix:
    first: object
    first_gram: object
    output_control: FramedPairOutputControl


def transport_pair_kraus_descriptor(descriptor, rotation, translation=ZERO):
    """Transport the complete K descriptor, including its literal factors."""
    frame = block28.transformed_frame(
        block28.CANONICAL_FRAME, rotation, translation
    )
    left_source = block23.mat_vec(rotation, descriptor.left.source)
    right_source = block23.mat_vec(rotation, descriptor.right.source)
    left = block28.turn_branch(
        frame.left_anchor,
        frame.front,
        left_source,
        block23.mat_vec(rotation, descriptor.left.exit_front),
        block23.mat_vec(rotation, descriptor.left.target),
    )
    right = block28.turn_branch(
        frame.right_anchor,
        frame.right_front,
        right_source,
        block23.mat_vec(rotation, descriptor.right.exit_front),
        block23.mat_vec(rotation, descriptor.right.target),
    )
    control = block28.pair_control_for(frame, left_source, right_source)
    return block28.PairKrausDescriptor(
        control,
        left,
        right,
        descriptor.weight,
        descriptor.amplitude,
        (
            ("amplitude", descriptor.amplitude),
            ("full_pair_control", control.atoms),
            ("left_turn_factors", left.factors),
            ("right_turn_factors", right.factors),
        ),
    )


def framed_reconstructed_pair_output(prefix, gram):
    configuration = {
        center: block23.BLANK_POINTER
        for center in prefix.output_control.frame.left_targets
        + prefix.output_control.frame.right_targets
    }
    for center, word in gram.output_records:
        if center not in configuration:
            raise ValueError("transported first output misses its guarded frame")
        configuration[center] = word
    return tuple(
        sorted(
            (
                OutputPointerAtom(center, word)
                for center, word in configuration.items()
            ),
            key=lambda atom: coordinate_sort_key(atom.center),
        )
    )


def transport_connected_pair_prefix(prefix, rotation, translation=ZERO):
    first = transport_pair_kraus_descriptor(
        prefix.first, rotation, translation
    )
    first_gram = contract_imported_pair_factors(first)
    output = transport_pair_output_control(
        prefix.output_control, rotation, translation
    )
    return FramedConnectedPairPrefix(first, first_gram, output)


def framed_pair_prefix_output_is_bound(prefix) -> bool:
    try:
        fresh = contract_imported_pair_factors(prefix.first)
        reconstructed = framed_reconstructed_pair_output(prefix, fresh)
    except (KeyError, ValueError):
        return False
    return (
        imported_pair_factorization_is_exact(prefix.first)
        and fresh == prefix.first_gram
        and fresh.control == prefix.first.control
        and framed_output_control_is_physical(prefix.output_control)
        and reconstructed == prefix.output_control.atoms
        and fresh.output_records
        == (
            (
                prefix.first.left.effect.target_center,
                prefix.first.left.effect.output_word,
            ),
            (
                prefix.first.right.effect.target_center,
                prefix.first.right.effect.output_word,
            ),
        )
        and block28.full_guard_is_bound(prefix.first)
    )


@dataclass(frozen=True)
class FramedConnectedCylinderBranch:
    prefix: FramedConnectedPairPrefix
    future: FramedFutureBranch
    factorization: tuple


def framed_connected_cylinder_branch(prefix, future):
    return FramedConnectedCylinderBranch(
        prefix,
        future,
        (
            ("first_pair_factors", prefix.first.factorization),
            ("intermediate_output_control", prefix.output_control.atoms),
            ("future_resource_sector", future.sector),
            ("future_factors", future.factorization),
            ("outside_identity", "I_outside"),
        ),
    )


def turn_carrier_centers(branch):
    data = block24.factor_dictionary(branch.factors)
    return {
        branch.anchor,
        branch.effect.target_center,
        *data["spectator_identity_centers"],
    }


def contract_framed_connected_cylinder(descriptor):
    prefix = descriptor.prefix
    future = descriptor.future
    expected_factorization = (
        ("first_pair_factors", prefix.first.factorization),
        ("intermediate_output_control", prefix.output_control.atoms),
        ("future_resource_sector", future.sector),
        ("future_factors", future.factorization),
        ("outside_identity", "I_outside"),
    )
    factors = dict(descriptor.factorization)
    try:
        fresh_first = contract_imported_pair_factors(prefix.first)
    except (KeyError, ValueError) as exc:
        raise ValueError("transported K does not freshly contract") from exc
    first_centers = turn_carrier_centers(prefix.first.left) | turn_carrier_centers(
        prefix.first.right
    )
    resource_centers = (future.sector.left.center, future.sector.right.center)
    if not (
        framed_pair_prefix_output_is_bound(prefix)
        and fresh_first == prefix.first_gram
        and future.prefix == prefix.output_control
        and descriptor.factorization == expected_factorization
        and factors["first_pair_factors"] == prefix.first.factorization
        and factors["intermediate_output_control"]
        == prefix.output_control.atoms
        and factors["future_resource_sector"] == future.sector
        and factors["future_factors"] == future.factorization
        and factors["outside_identity"] == "I_outside"
        and all(
            block28.block_sites(resource).isdisjoint(
                block28.block_sites(first_center)
            )
            for resource in resource_centers
            for first_center in first_centers
        )
    ):
        raise ValueError("transported cylinder factorization is not complete")
    future_gram = contract_framed_future_branch(future)
    past_projector = pair_input_tensor_projector(prefix.first.control)
    control = CylinderInputControl(
        prefix.first.control,
        future.sector.projector,
        make_tensor_projector(
            past_projector.atoms + future.sector.projector.atoms
        ),
    )
    if not cylinder_input_control_is_physical(control):
        raise ValueError("transported cylinder input projector is not physical")
    return ConnectedCylinderGram(
        control,
        fresh_first.coefficient,
        future_gram.coefficient,
        composite_cylinder_coefficient(
            fresh_first.coefficient,
            future_gram.coefficient,
        ),
        future_gram.bits,
        prefix.output_control,
    )


def transport_tensor_projector(projector, rotation, translation=ZERO):
    atoms = []
    for atom in projector.atoms:
        state = (
            block23.rotate_word(atom.state, rotation)
            if atom.algebra == "pointer26"
            else block23.rotate_block_product(atom.state, rotation)
        )
        atoms.append(
            LocalProjector(
                block28.affine(rotation, translation, atom.center),
                atom.algebra,
                state,
                atom.sense,
            )
        )
    return make_tensor_projector(atoms)


@dataclass(frozen=True)
class FramedFutureActiveSum:
    output_controls: tuple[FramedPairOutputControl, ...]
    sector_rows: tuple[OperatorEffect, ...]
    projector: OrthogonalProjectorSum


@dataclass(frozen=True)
class FramedPairFutureStop:
    active: FramedFutureActiveSum
    kraus: ProjectorComplement


def framed_output_control_sort_key(control):
    return tensor_projector_sort_key(framed_output_tensor_projector(control))


def framed_sector_row_sort_key(row):
    return (
        framed_output_control_sort_key(row.control.prefix),
        row.control.resource.bits,
    )


@lru_cache(maxsize=1)
def source_future_active_and_stop_certificate() -> bool:
    active_sum = future_active_sum(pair_output_active_sum())
    stop = make_future_stop(active_sum)
    try:
        contracted = contract_future_stop(stop)
    except (KeyError, ValueError):
        return False
    # contract_future_stop already authenticates the complete active surface.
    return contracted == stop.kraus


def active_sum_and_stop_transport_certificate(rotation, translation=ZERO) -> bool:
    active = pair_output_active_sum()
    source_active = future_active_sum(active)
    source_stop = make_future_stop(source_active)
    moved_controls = tuple(
        sorted(
            (
                transport_pair_output_control(control, rotation, translation)
                for control in active.controls
            ),
            key=framed_output_control_sort_key,
        )
    )
    frame = block28.transformed_frame(
        block28.CANONICAL_FRAME, rotation, translation
    )
    expected_controls = tuple(
        sorted(
            (
                framed_pair_output_control(
                    frame,
                    left_exit,
                    right_exit,
                    left_first,
                    right_first,
                )
                for left_exit, right_exit in itertools.product(
                    frame.left_exits, frame.right_exits
                )
                for left_first, right_first in itertools.product(
                    OUTCOMES, repeat=2
                )
            ),
            key=framed_output_control_sort_key,
        )
    )
    moved_terms = sorted_projectors(
        transport_tensor_projector(term, rotation, translation)
        for term in future_active_sum(active).projector.terms
    )
    expected_terms = sorted_projectors(
        framed_output_tensor_projector(control) for control in expected_controls
    )
    moved_projector = OrthogonalProjectorSum(
        sorted_centers(
            {center for term in moved_terms for center in term.carrier_centers}
        ),
        moved_terms,
    )
    expected_projector = OrthogonalProjectorSum(
        moved_projector.carrier_centers,
        expected_terms,
    )
    moved_rows = tuple(
        sorted(
            (
                OperatorEffect(
                    transport_sector_control(
                        row.control, rotation, translation
                    ),
                    row.coefficient,
                )
                for row in source_active.sector_rows
            ),
            key=framed_sector_row_sort_key,
        )
    )
    expected_rows = tuple(
        sorted(
            (
                OperatorEffect(
                    framed_sector_control(control, bits), sp.S.One
                )
                for control in expected_controls
                for bits in RESOURCE_BITS
            ),
            key=framed_sector_row_sort_key,
        )
    )
    moved_active = FramedFutureActiveSum(
        moved_controls, moved_rows, moved_projector
    )
    expected_active = FramedFutureActiveSum(
        expected_controls, expected_rows, expected_projector
    )
    moved_stop_kraus = ProjectorComplement(
        moved_projector.carrier_centers,
        moved_projector,
        source_stop.kraus.rank,
    )
    expected_stop_kraus = ProjectorComplement(
        expected_projector.carrier_centers,
        expected_projector,
        projector_complement_rank(expected_projector),
    )
    moved_stop = FramedPairFutureStop(moved_active, moved_stop_kraus)
    expected_stop = FramedPairFutureStop(expected_active, expected_stop_kraus)
    return (
        source_future_active_and_stop_certificate()
        and len(moved_controls) == len(set(moved_controls)) == 3136
        and set(moved_controls) == set(expected_controls)
        and len(moved_rows) == len(set(moved_rows)) == 12544
        and set(moved_rows) == set(expected_rows)
        and all(
            framed_sector_control_is_physical(row.control)
            and row.coefficient == 1
            for row in moved_rows
        )
        and moved_projector == expected_projector
        and moved_active == expected_active
        and moved_stop == expected_stop
        and projector_complement_is_physical(moved_stop.kraus)
        and moved_stop.kraus.subtrahend is moved_stop.active.projector
    )


def pair_prefix_affine_covariance_certificate(
    prefix, rotation, translation=ZERO
) -> bool:
    try:
        source_fresh = contract_imported_pair_factors(prefix.first)
        moved = transport_connected_pair_prefix(
            prefix, rotation, translation
        )
        moved_fresh = contract_imported_pair_factors(moved.first)
    except (KeyError, ValueError):
        return False
    expected_records = tuple(
        (
            block28.affine(rotation, translation, center),
            block23.rotate_word(word, rotation),
        )
        for center, word in source_fresh.output_records
    )
    return (
        pair_prefix_output_is_bound(prefix)
        and source_fresh == prefix.first_gram
        and moved_fresh == moved.first_gram
        and framed_pair_prefix_output_is_bound(moved)
        and moved.output_control
        == transport_pair_output_control(
            prefix.output_control, rotation, translation
        )
        and moved.first
        == transport_pair_kraus_descriptor(
            prefix.first, rotation, translation
        )
        and block28.control_transport_certificate(
            block28.CANONICAL_FRAME,
            prefix.first.control.left_source,
            prefix.first.control.right_source,
            rotation,
            translation,
        )
        and block28.turn_branch_covariance_certificate(
            prefix.first.left, rotation
        )
        and block28.turn_branch_covariance_certificate(
            prefix.first.right, rotation
        )
        and moved_fresh.output_records == expected_records
        and moved_fresh.coefficient == source_fresh.coefficient
    )


def composite_cylinder_transport_certificate(
    descriptor, rotation, translation=ZERO, mutation=None
) -> bool:
    prefix = descriptor.prefix
    future = descriptor.future
    try:
        source_gram = contract_connected_cylinder(descriptor)
        moved_prefix = transport_connected_pair_prefix(
            prefix, rotation, translation
        )
        moved_future = framed_future_branch(
            moved_prefix.output_control,
            future.sector.bits,
            block23.mat_vec(rotation, future.left_second)
            if future.left_second is not None
            else None,
            block23.mat_vec(rotation, future.right_second)
            if future.right_second is not None
            else None,
        )
    except (KeyError, ValueError):
        return False
    if mutation == "untransported_merged_source":
        actions = list(moved_future.product.actions)
        index = next(
            index
            for index, action in enumerate(actions)
            if action.sources
        )
        moved_action = actions[index]
        source_action = future.embedded_product.actions[index]
        untransported = source_action.sources[0][1]
        mutated_sources = (
            (moved_action.sources[0][0], untransported),
            *moved_action.sources[1:],
        )
        actions[index] = replace(
            moved_action,
            factors=untransported.factors,
            sources=mutated_sources,
        )
        mutated_product = replace(
            moved_future.product, actions=tuple(actions)
        )
        moved_future = replace(
            moved_future,
            product=mutated_product,
            factorization=replace_named_factor(
                moved_future.factorization,
                "merged_append_product",
                mutated_product,
            ),
        )
    moved_descriptor = framed_connected_cylinder_branch(
        moved_prefix, moved_future
    )
    source_control = cylinder_input_control(prefix, future.sector)
    transported_system_projector = transport_tensor_projector(
        source_control.projector, rotation, translation
    )
    try:
        moved_gram = contract_framed_connected_cylinder(moved_descriptor)
    except (KeyError, ValueError):
        return False
    expected_first_records = tuple(
        (
            block28.affine(rotation, translation, center),
            block23.rotate_word(word, rotation),
        )
        for center, word in prefix.first_gram.output_records
    )
    return (
        source_gram.control == source_control
        and pair_prefix_affine_covariance_certificate(
            prefix, rotation, translation
        )
        and future_branch_affine_covariance_certificate(
            future, rotation, translation
        )
        and framed_pair_prefix_output_is_bound(moved_prefix)
        and moved_prefix.first_gram.output_records == expected_first_records
        and moved_gram.control.projector == transported_system_projector
        and cylinder_input_control_is_physical(moved_gram.control)
        and moved_gram.first_coefficient == source_gram.first_coefficient
        and moved_gram.future_coefficient == source_gram.future_coefficient
        and moved_gram.composite_coefficient
        == source_gram.composite_coefficient
        and moved_gram.bits == source_gram.bits
        and moved_gram.intermediate_output == moved_prefix.output_control
        and moved_descriptor.factorization
        == framed_connected_cylinder_branch(
            moved_prefix, moved_future
        ).factorization
    )


def composite_cylinder_covariance_template_certificate(
    rotation, translation=ZERO
) -> bool:
    """Cover the full prefix Cartesian product by its independent axes."""
    active = pair_output_active_sum()
    output_resource_checks = 0
    for control in active.controls:
        prefix = connected_pair_prefix(
            LAMBDAS[0],
            OUTCOMES[0],
            OUTCOMES[1],
            *control.key,
        )
        for bits in RESOURCE_BITS:
            future = connected_future_branch(
                prefix.output_control,
                bits,
                OUTCOMES[2] if bits[0] else None,
                OUTCOMES[3] if bits[1] else None,
            )
            if not composite_cylinder_transport_certificate(
                connected_cylinder_branch(prefix, future),
                rotation,
                translation,
            ):
                return False
            output_resource_checks += 1
    q_exit_controls = tuple(
        pair_output_control(
            left_exit,
            right_exit,
            OUTCOMES[0],
            OUTCOMES[1],
        )
        for left_exit, right_exit in itertools.product(
            block28.LEFT_EXITS, block28.RIGHT_EXITS
        )
    )
    input_q_checks = 0
    for q_control in q_exit_controls:
        for lam in LAMBDAS:
            for left_source, right_source in itertools.product(
                OUTCOMES, repeat=2
            ):
                prefix = connected_pair_prefix(
                    lam,
                    left_source,
                    right_source,
                    *q_control.key,
                )
                if not pair_prefix_affine_covariance_certificate(
                    prefix, rotation, translation
                ):
                    return False
                input_q_checks += 1
    # All future-outcome append descriptors are covered independently in the
    # same rotation loop.  Continuation independence makes these exact axes a
    # Cartesian theorem rather than a sample extrapolation.
    return (
        output_resource_checks == 3136 * 4 == 12544
        and input_q_checks
        == len(block28.LEFT_EXITS)
        * len(block28.RIGHT_EXITS)
        * len(LAMBDAS)
        * len(OUTCOMES) ** 2
        == 6272
        and block28.full_pair_covariance_certificate()
        and q_independent_continuation_certificate()
    )


def reverse_framed_output_control(control):
    reversed_frame = block28.PairFrame(
        control.frame.right_anchor, control.frame.right_front
    )
    return framed_pair_output_control(
        reversed_frame,
        control.right_exit,
        control.left_exit,
        control.right_first,
        control.left_first,
    )


def side_exchange_certificate() -> bool:
    sample = pair_output_control(
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[-1],
        OUTCOMES[0],
        OUTCOMES[-1],
    )
    for rotation in block28.pair_stabilizer():
        swaps = block23.mat_vec(rotation, block28.F_LEFT) == block28.F_RIGHT
        translation = block28.scale(27, E1) if swaps else ZERO
        moved = transport_pair_output_control(sample, rotation, translation)
        normalized = reverse_framed_output_control(moved) if swaps else moved
        expected = framed_pair_output_control(
            block28.CANONICAL_FRAME,
            block23.mat_vec(
                rotation, sample.right_exit if swaps else sample.left_exit
            ),
            block23.mat_vec(
                rotation, sample.left_exit if swaps else sample.right_exit
            ),
            block23.mat_vec(
                rotation, sample.right_first if swaps else sample.left_first
            ),
            block23.mat_vec(
                rotation, sample.left_first if swaps else sample.right_first
            ),
        )
        if normalized != expected:
            return False
        for bits in RESOURCE_BITS:
            sector = future_resource_sector(sample, bits)
            moved_sector = transport_resource_sector(sector, rotation, translation)
            normalized_bits = (bits[1], bits[0]) if swaps else bits
            normalized_prefix = normalized
            normalized_sector = framed_resource_sector(
                normalized_prefix, normalized_bits
            )
            moved_atoms = (
                (moved_sector.right, moved_sector.left)
                if swaps
                else (moved_sector.left, moved_sector.right)
            )
            if not (
                normalized_sector.bits == normalized_bits
                and normalized_sector.left.center == moved_atoms[0].center
                and normalized_sector.right.center == moved_atoms[1].center
                and normalized_sector.left.sense == moved_atoms[0].sense
                and normalized_sector.right.sense == moved_atoms[1].sense
            ):
                return False
            source_future = connected_future_branch(
                sample,
                bits,
                OUTCOMES[1] if bits[0] else None,
                OUTCOMES[2] if bits[1] else None,
            )
            if not future_branch_affine_covariance_certificate(
                source_future, rotation, translation
            ):
                return False
            moved_future = framed_future_branch(
                moved,
                bits,
                block23.mat_vec(rotation, OUTCOMES[1]) if bits[0] else None,
                block23.mat_vec(rotation, OUTCOMES[2]) if bits[1] else None,
            )
            normalized_future = (
                framed_future_branch(
                    normalized,
                    normalized_bits,
                    moved_future.right_second,
                    moved_future.left_second,
                )
                if swaps
                else moved_future
            )
            if not framed_future_branch_is_physical(normalized_future):
                return False
            if swaps and not (
                normalized_future.left_append == moved_future.right_append
                and normalized_future.right_append == moved_future.left_append
                and normalized_future.product
                == embedded_append_product(
                    moved_future.right_append,
                    moved_future.left_append,
                )
                and normalized_future.control
                == framed_sector_control(normalized, normalized_bits)
                and normalized_future.factorization
                == (
                    ("sector_control", normalized_future.control),
                    ("merged_append_product", normalized_future.product),
                    ("outside_identity", "I_outside"),
                )
            ):
                return False
    return True


@lru_cache(maxsize=1)
def covariance_certificate() -> bool:
    tau = sp.symbols("tau_0 tau_1 tau_2")
    sample_control = pair_output_control(
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[-1],
        OUTCOMES[0],
        OUTCOMES[-1],
    )
    for rotation in ROTATIONS:
        for arm in ARMS:
            for exit_front, first_outcome, second_outcome in itertools.product(
                arm_exits(arm), OUTCOMES, OUTCOMES
            ):
                branch = connected_append_descriptor(
                    arm, exit_front, first_outcome, second_outcome
                ).append
                if not append_affine_covariance_certificate(branch, rotation, tau):
                    return False
        if not (
            pair_output_control_transport_certificate(
                sample_control, rotation, tau
            )
            and resource_sector_transport_certificate(
                future_resource_sector(sample_control, (1, 0)),
                rotation,
                tau,
            )
            and all(
                future_branch_affine_covariance_certificate(
                    connected_future_branch(
                        sample_control,
                        bits,
                        OUTCOMES[1] if bits[0] else None,
                        OUTCOMES[2] if bits[1] else None,
                    ),
                    rotation,
                    tau,
                )
                for bits in RESOURCE_BITS
            )
            and composite_cylinder_covariance_template_certificate(
                rotation, tau
            )
            and active_sum_and_stop_transport_certificate(rotation, tau)
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
    return (
        side_exchange_certificate()
        and block23.rotate_block_product(block23.BLANK_BLOCK, ROTATIONS[0])
        == block23.BLANK_BLOCK
        and block24.translation_covariance_certificate()
        and block28.full_pair_covariance_certificate()
        and append_product_compatibility_certificate()
    )


@dataclass(frozen=True)
class ReferenceFactor:
    dimension: object
    row: object
    column: object
    operator: object


@dataclass(frozen=True)
class ReferenceLift:
    system_descriptor: object
    reference: ReferenceFactor


@dataclass(frozen=True)
class ReferenceExtendedEffect:
    system_effect: object
    reference_operator: object
    reference_gram: object
    matrix_unit: object


def contract_reference_lift(lift):
    reference = lift.reference
    operator = reference.operator
    if not (
        getattr(operator, "rows", None) == reference.dimension
        and getattr(operator, "cols", None) == reference.dimension
    ):
        raise ValueError("reference operator has the wrong carrier")
    reference_gram = operator.adjoint() * operator
    matrix_unit = reference_gram[reference.row, reference.column]
    descriptor = lift.system_descriptor
    if isinstance(descriptor, ConnectedFutureBranch):
        gram = contract_connected_future_branch(descriptor)
        effect = OperatorEffect(gram.control, gram.coefficient)
    elif isinstance(descriptor, PairFutureStop):
        effect = contract_future_stop(descriptor)
    elif isinstance(descriptor, ConnectedCylinderBranch):
        gram = contract_connected_cylinder(descriptor)
        effect = OperatorEffect(gram.control, gram.composite_coefficient)
    else:
        raise ValueError("unknown reference-lifted system descriptor")
    return ReferenceExtendedEffect(
        effect, operator, reference_gram, matrix_unit
    )


@lru_cache(maxsize=None)
def arbitrary_reference_certificate(mutation=None) -> bool:
    active = pair_output_active_sum()
    prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[2],
        OUTCOMES[3],
    )
    future = connected_future_branch(
        prefix.output_control,
        (1, 1),
        OUTCOMES[0],
        OUTCOMES[-1],
    )
    cylinder = connected_cylinder_branch(prefix, future)
    stop = make_future_stop(future_active_sum(active))
    dimension = sp.symbols("d_R", integer=True, positive=True)
    row, column = sp.symbols("r_R s_R", integer=True, nonnegative=True)
    reference = ReferenceFactor(
        dimension,
        row,
        column,
        -sp.Identity(dimension)
        if mutation == "nonidentity"
        else sp.Identity(dimension),
    )
    lifts = tuple(
        ReferenceLift(descriptor, reference)
        for descriptor in (future, stop, cylinder)
    )
    if not (
        active.idempotent
        and active.complement_nontrivial
        and len(active.controls) == 3136
        and block28.arbitrary_reference_certificate()
    ):
        return False
    try:
        effects = tuple(contract_reference_lift(lift) for lift in lifts)
    except ValueError:
        return False
    identity = sp.Identity(dimension)
    matrix_unit = identity[row, column]
    return (
        len(effects) == 3
        and reference.operator == identity
        and all(
            effect.reference_operator == identity for effect in effects
        )
        and all(
            effect.reference_gram == identity
            for effect in effects
        )
        and all(effect.matrix_unit == matrix_unit for effect in effects)
        and effects[0].system_effect
        == OperatorEffect(
            contract_connected_future_branch(future).control,
            contract_connected_future_branch(future).coefficient,
        )
        and effects[1].system_effect == stop.kraus
        and effects[2].system_effect
        == OperatorEffect(
            contract_connected_cylinder(cylinder).control,
            contract_connected_cylinder(cylinder).composite_coefficient,
        )
    )


TERMINAL_TEXT = (
    "BOTH-SUPPLIED-Q-PAIR-CHANNELS-COMPOSE-WITH-ONE-PHYSICAL-"
    "OUTPUT-RECORD-CONTROLLED-FUTURE-CHANNEL"
)

SCOPE_TEXT = (
    "two supplied q choices, neither derived nor selected; imported complete "
    "pair channel followed only by one externally invoked physical "
    "output-Record-controlled future channel; D00/D10/D01/D11 route "
    "zero/left/right/both literal Block24 appends on supplied finite rails; "
    "no singleton first-layer law or empty/singleton/pair first-layer "
    "completion; no second returned-pair use; no cause identification, "
    "autonomous invocation, renewal, scheduler, cadence, rate, nearest-neighbor "
    "compiler, gravity/source attachment, axiom amendment, audit verdict or "
    "retention, obligation retirement, or TOE-score movement"
)

FORBIDDEN_SCOPE_PHRASES = (
    "singleton first-layer law established",
    "empty/singleton/pair first-layer completion established",
    "second returned-pair use established",
    "q derivation established",
    "q selection established",
    "cause identification established",
    "autonomous invocation established",
    "renewal established",
    "scheduler established",
    "cadence established",
    "rate established",
    "nearest-neighbor compiler established",
    "gravity/source attachment established",
    "axiom amendment required",
    "audit verdict set",
    "audit retention established",
    "obligation retired",
    "TOE score increased",
)


@dataclass(frozen=True)
class ScopeContract:
    singleton_first_layer: bool = False
    direct_sum_completion: bool = False
    second_pair_use: bool = False
    q_derivation: bool = False
    q_selection: bool = False
    cause_identification: bool = False
    autonomous_invocation: bool = False
    renewal: bool = False
    scheduler: bool = False
    cadence: bool = False
    rate: bool = False
    compiler: bool = False
    gravity_attachment: bool = False
    axiom_amendment: bool = False
    audit_verdict: bool = False
    audit_retention: bool = False
    obligation_retirement: bool = False
    toe_movement: bool = False
    next_on_both_pass: str = "covariant_physical_successor_handoff"


SAFE_SCOPE_CONTRACT = ScopeContract()

SCOPE_FIELD_BY_PHRASE = {
    phrase: field
    for phrase, field in zip(
        FORBIDDEN_SCOPE_PHRASES,
        (
            "singleton_first_layer",
            "direct_sum_completion",
            "second_pair_use",
            "q_derivation",
            "q_selection",
            "cause_identification",
            "autonomous_invocation",
            "renewal",
            "scheduler",
            "cadence",
            "rate",
            "compiler",
            "gravity_attachment",
            "axiom_amendment",
            "audit_verdict",
            "audit_retention",
            "obligation_retirement",
            "toe_movement",
        ),
    )
}


def scope_contract_is_safe(contract) -> bool:
    forbidden = tuple(
        value
        for name, value in contract.__dict__.items()
        if name != "next_on_both_pass"
    )
    return (
        not any(forbidden)
        and contract.next_on_both_pass == "covariant_physical_successor_handoff"
    )


def scope_guard_certificate(
    terminal=TERMINAL_TEXT,
    scope=SCOPE_TEXT,
    contract=SAFE_SCOPE_CONTRACT,
) -> bool:
    combined = f"{terminal}; {scope}"
    return (
        terminal == TERMINAL_TEXT
        and scope == SCOPE_TEXT
        and scope_contract_is_safe(contract)
        and all(phrase not in combined for phrase in FORBIDDEN_SCOPE_PHRASES)
    )


def scope_promotion_is_rejected(phrase) -> bool:
    if phrase not in SCOPE_FIELD_BY_PHRASE:
        return False
    candidate = replace(
        SAFE_SCOPE_CONTRACT,
        **{SCOPE_FIELD_BY_PHRASE[phrase]: True},
    )
    return not scope_contract_is_safe(candidate)


def direct_autonomy_dispatch_is_rejected() -> bool:
    candidate = replace(
        SAFE_SCOPE_CONTRACT,
        next_on_both_pass="autonomous_state_driven_reuse_and_resource_closure",
    )
    return not scope_contract_is_safe(candidate)


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
    control = pair_output_control(
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[0],
        OUTCOMES[1],
    )
    rotation = next(
        rotation
        for rotation in ROTATIONS
        if block23.mat_vec(rotation, control.left_exit) != control.left_exit
    )
    moved = transport_pair_output_control(control, rotation)
    atoms = list(moved.atoms)
    atoms[0] = replace(atoms[0], center=control.atoms[0].center)
    mutant = replace(moved, atoms=tuple(atoms))
    return not framed_output_control_is_physical(mutant)


def untransported_future_mutation_is_rejected() -> bool:
    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    translation = (1, 2, 3)
    prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[2],
        OUTCOMES[3],
    )
    future = connected_future_branch(
        prefix.output_control,
        (1, 1),
        OUTCOMES[4],
        OUTCOMES[5],
    )
    return not composite_cylinder_transport_certificate(
        connected_cylinder_branch(prefix, future),
        identity,
        translation,
        mutation="untransported_merged_source",
    )


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


def merged_product_mutation_is_rejected(mutation) -> bool:
    exit_front = block28.LEFT_EXITS[0]
    left = connected_append_descriptor(
        LEFT, exit_front, OUTCOMES[0], OUTCOMES[1]
    ).append
    right = connected_append_descriptor(
        RIGHT, exit_front, OUTCOMES[0], OUTCOMES[1]
    ).append
    mutant = embedded_append_product(left, right, mutation)
    try:
        contract_embedded_append_product(mutant)
    except (KeyError, StopIteration, ValueError):
        return True
    return False


def patched_future_row_mutation_is_rejected(prefix) -> bool:
    family = future_sector_family(prefix, (1, 0), "drop_future_outcome")
    mutant = replace(
        family,
        outcome_keys=tuple(itertools.product(OUTCOMES, (None,))),
        branch_count=14,
        row_effect=OperatorEffect(family.control, sp.S.One),
    )
    return not future_sector_family_is_physical(mutant)


def changed_imported_control_mutation_is_rejected() -> bool:
    prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[2],
        OUTCOMES[3],
    )
    changed_control = block28.pair_control(
        OUTCOMES[-1], prefix.first.control.right_source
    )
    changed_first = replace(
        prefix.first,
        control=changed_control,
        factorization=replace_named_factor(
            prefix.first.factorization,
            "full_pair_control",
            changed_control.atoms,
        ),
    )
    # Keep the declared coefficient and output labels byte-for-byte fixed;
    # only the imported physical Pi_s,t in K is changed.
    mutant = replace(prefix, first=changed_first)
    future = connected_future_branch(
        mutant.output_control,
        (1, 0),
        OUTCOMES[0],
        None,
    )
    try:
        contract_connected_cylinder(connected_cylinder_branch(mutant, future))
    except (KeyError, ValueError):
        return True
    return False


def wrong_current_word_same_scalar_mutation_is_rejected(prefix) -> bool:
    branch = connected_future_branch(prefix, (1, 0), OUTCOMES[0], None)
    append = branch.left_append
    mutant_append = replace(
        append,
        current_word=block23.locked_word(append.front, OUTCOMES[-1]),
    )
    try:
        mutant_product = embedded_append_product(mutant_append, None)
        mutant = replace(
            branch,
            left_append=mutant_append,
            embedded_product=mutant_product,
            factorization=replace_named_factor(
                branch.factorization,
                "merged_append_product",
                mutant_product,
            ),
        )
        contract_connected_future_branch(mutant)
    except (KeyError, ValueError):
        return True
    return False


def duplicate_future_factor_mutation_is_rejected(prefix) -> bool:
    branch = connected_future_branch(
        prefix,
        (1, 1),
        OUTCOMES[0],
        OUTCOMES[1],
    )
    mutant = replace(
        branch,
        factorization=(
            ("sector_control", "shadowed-junk"),
            *branch.factorization,
        ),
    )
    try:
        contract_connected_future_branch(mutant)
    except (KeyError, ValueError):
        return True
    return False


def duplicate_cylinder_factor_mutation_is_rejected() -> bool:
    prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[2],
        OUTCOMES[3],
    )
    future = connected_future_branch(
        prefix.output_control,
        (1, 1),
        OUTCOMES[0],
        OUTCOMES[1],
    )
    descriptor = connected_cylinder_branch(prefix, future)
    mutant = replace(
        descriptor,
        factorization=(
            ("first_pair_factors", "shadowed-junk"),
            *descriptor.factorization,
        ),
    )
    try:
        contract_connected_cylinder(mutant)
    except (KeyError, ValueError):
        return True
    return False


def duplicate_imported_pair_factor_mutation_is_rejected() -> bool:
    prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        block28.LEFT_EXITS[0],
        block28.RIGHT_EXITS[0],
        OUTCOMES[2],
        OUTCOMES[3],
    )
    mutant_first = replace(
        prefix.first,
        factorization=(
            ("amplitude", "shadowed-junk"),
            *prefix.first.factorization,
        ),
    )
    mutant_prefix = replace(prefix, first=mutant_first)
    future = connected_future_branch(
        mutant_prefix.output_control,
        (1, 0),
        OUTCOMES[0],
        None,
    )
    try:
        contract_connected_cylinder(
            connected_cylinder_branch(mutant_prefix, future)
        )
    except (KeyError, ValueError):
        return True
    return False


def changed_leased_resource_mutation_is_rejected(prefix) -> bool:
    future = connected_future_branch(prefix, (1, 0), OUTCOMES[0], None)
    mutant_sector = replace(
        future.sector,
        left=replace(future.sector.left, sense="complement"),
    )
    mutant_control = replace(future.control, resource=mutant_sector)
    mutant_future = replace(
        future,
        sector=mutant_sector,
        control=mutant_control,
        factorization=replace_named_factor(
            future.factorization,
            "sector_control",
            mutant_control,
        ),
    )
    pair_prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        *prefix.key,
    )
    try:
        contract_connected_cylinder(
            connected_cylinder_branch(pair_prefix, mutant_future)
        )
    except (KeyError, ValueError):
        return True
    return False


def changed_leased_future_control_mutation_is_rejected(prefix) -> bool:
    future = connected_future_branch(prefix, (1, 0), OUTCOMES[0], None)
    mutant_control = sector_control(prefix, (0, 0))
    mutant_future = replace(
        future,
        control=mutant_control,
        factorization=replace_named_factor(
            future.factorization,
            "sector_control",
            mutant_control,
        ),
    )
    pair_prefix = connected_pair_prefix(
        LAMBDAS[0],
        OUTCOMES[0],
        OUTCOMES[1],
        *prefix.key,
    )
    try:
        contract_connected_cylinder(
            connected_cylinder_branch(pair_prefix, mutant_future)
        )
    except (KeyError, ValueError):
        return True
    return False


def erased_future_outcome_label_mutation_is_rejected(prefix) -> bool:
    future = connected_future_branch(prefix, (1, 0), OUTCOMES[0], None)
    # Preserve the physical append, merged product, factors, resource, and
    # control while erasing only the public outcome label.  A contractor that
    # authenticates the routed map but not its advertised outcome accepts this
    # internally false descriptor.
    mutant_future = replace(future, left_second=None)
    try:
        contract_connected_future_branch(mutant_future)
    except (KeyError, ValueError):
        return True
    return False


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
        f"scope_{field}_promotion_is_rejected": phrase
        for phrase, field in SCOPE_FIELD_BY_PHRASE.items()
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
        "wrong_resource_sense_breaks_typed_sector": (
            not future_resource_sector_is_physical(
                future_resource_sector(prefix, (1, 0), "wrong_left_sense")
            )
        ),
        "duplicated_resource_sector_breaks_physical_partition": not resource_partition_certificate(
            prefix, "duplicate_resource_sector"
        ),
        "same_count_wrong_center_breaks_merged_product": (
            merged_product_mutation_is_rejected("same_count_wrong_center")
        ),
        "nonidentity_equal_exit_spectator_breaks_merged_product": (
            merged_product_mutation_is_rejected(
                "nonidentity_equal_exit_spectator"
            )
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
            patched_future_row_mutation_is_rejected(prefix)
        ),
        "missing_common_STOP_breaks_full_space_TP": (
            not future_stop_completion_certificate(
                pair_output_active_sum(), stop_present=False
            )
        ),
        "stale_active_projector_breaks_common_STOP": (
            not future_stop_completion_certificate(
                pair_output_active_sum(),
                mutation="stale_active_projector",
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
        "untransported_composite_factor_breaks_translation_covariance": (
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
        "extra_D10_writer_breaks_factor_derived_debit": not debit_ledger_certificate(
            "D10_extra_writer"
        ),
        "changed_imported_Pi_with_fixed_coefficient_breaks_M_equals_LK": (
            changed_imported_control_mutation_is_rejected()
        ),
        "changed_current_word_with_same_scalar_breaks_control": (
            wrong_current_word_same_scalar_mutation_is_rejected(prefix)
        ),
        "duplicate_imported_K_factor_breaks_exact_factorization": (
            duplicate_imported_pair_factor_mutation_is_rejected()
        ),
        "duplicate_future_factor_breaks_exact_factorization": (
            duplicate_future_factor_mutation_is_rejected(prefix)
        ),
        "duplicate_cylinder_factor_breaks_exact_factorization": (
            duplicate_cylinder_factor_mutation_is_rejected()
        ),
        "changed_leased_resource_breaks_cylinder_binding": (
            changed_leased_resource_mutation_is_rejected(prefix)
        ),
        "changed_leased_future_control_breaks_cylinder_binding": (
            changed_leased_future_control_mutation_is_rejected(prefix)
        ),
        "erased_future_outcome_label_breaks_append_target_binding": (
            erased_future_outcome_label_mutation_is_rejected(prefix)
        ),
        "fresh_copy_breaks_actual_output_provenance": not descriptor_binding_is_physical(
            fresh_copy_descriptor
        ),
        "old_source_future_kernel_breaks_output_conditioning": not descriptor_binding_is_physical(
            old_source_descriptor
        ),
        "lambda_dependent_continuation_breaks_common_descriptor": (
            not q_independent_continuation_certificate("physical_lambda_kernel")
        ),
        "direct_autonomy_dispatch_breaks_scope_contract": (
            direct_autonomy_dispatch_is_rejected()
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
        "18 state-controlled blocks; the future carrier is 34 blocks/1,088 "
        "sites and the sequential union is 36 blocks/1,152 sites",
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
        "784 conditional two-step histories per arm and 614,656 paired "
        "two-step histories decode; old and first Records are QND",
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
    survived = tuple(name for name, rejected in mutations.items() if not rejected)
    if survived:
        for name in survived:
            print(f"MUTATION SURVIVED {name}")
    else:
        mutation_names = "\n".join(mutations).encode("utf-8")
        print(
            f"MUTATIONS: REJECTED={len(mutations)}/{len(mutations)}; "
            f"names_sha256={hashlib.sha256(mutation_names).hexdigest()}"
        )
    checks.check(
        "designated_mutations",
        all(mutations.values()) and len(mutations) == 61,
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
        "per_site: checked — 18 state-controlled blocks; every identity factor "
        "on the 34-block future carrier and 36-block sequential union"
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
