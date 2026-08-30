#!/usr/bin/env python3
"""Block25: exact overlap gate for sharp Block24 hard exclusion.

The runner extracts every constrained one-qubit input factor from the literal
Block24 append constructor.  It first asks whether two cleanly separated
current Records can request partially overlapping radial Blank blocks whose
sharp eligibility projectors fail to commute.  Stage-B conflict-graph
totalization is permitted only if that exact Stage-A screen is green.
"""

from __future__ import annotations

import hashlib
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30 as block24  # noqa: E402


parent = block24.parent
PACKET = ROOT / ".claude/science/physics-loops" / (
    "toe-source-eta-ownership-block25-collision-hard-exclusion-"
    "totalization-20260830"
)
BLOCK24_SOURCE = (
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_"
    "2026_08_30.py"
)
BLOCK24_SOURCE_SHA256 = (
    "f98534f07655e0de296f2060932e34aa7a600f08545f3661be2843d05accc15d"
)
BLOCK24_NOTE = (
    "docs/ADMISSIBILITY_D4_SELF_DELIMITING_FORWARD_RECORD_APPEND_FINITE_"
    "HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md"
)
BLOCK24_NOTE_SHA256 = (
    "8bf1c8dc1bece0a2eaa057a7f1ef6d060afee2337793601a186ce4eab8da4a81"
)
BLOCK23_SOURCE = (
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_"
    "2026_08_30.py"
)
BLOCK23_SOURCE_SHA256 = (
    "426488df2a431cb7d415d5e933013f7ce0826cc9514f96cd041b9fc6ff49742a"
)
AXIOM_NOTE = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AXIOM_NOTE_SHA256 = (
    "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753"
)
FROZEN = {
    "GOAL.md": "148e0df628ce5f78ee95633ff937b1351a31e2371c1b6dc4a28430f292a30467",
    "AUTHORITY_GATE.md": "d565051413ee85ab0f058c8ce9162270ba53fcbaaa8fd1533d289c96b30c92b1",
    "PREFLIGHT_WITNESSES.md": "f0ffec5e07993eba7c60d41b60b4d3d9504952e21a6f18b8a611783edabf8441",
    "PANEL_RETURN.md": "cd115d670024432aebbc300da6dcc688d516b608ca29d4927dfa7dc667fed116",
    "INDEPENDENT_PREREG_ATTACK.md": "1edcbc110b48f3b1b28c345bbe5c3c54736bdf7465020d36dd5ae4b55192a01a",
    "APPROACH_REGISTRY.md": "4e5fca361ed40bb7783e4f00e390bb293a8c490928a4917539d7c8ba4b82bd4e",
    "MUTATION_PLAN.md": "59e2bfd386c0921b71624a3ff809122bea3f2595b41a38b949034f94f497a38d",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "a20e19ba2d17824e50e5ec81fea6971f16338c4a6dba19e44b9ddaeecf12d3af",
}
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py",
    "docs/ADMISSIBILITY_D4_SELF_DELIMITING_FORWARD_RECORD_APPEND_FINITE_HISTORY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-30.md",
    "scripts/admissibility_d4_prior_record_live_preparation_two_event_prefix_2026_08_30.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/AUTHORITY_GATE.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/INDEPENDENT_PREREG_ATTACK.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/NO_GO_DISCIPLINE_CHECKLIST.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block25-collision-hard-exclusion-totalization-20260830/STATE.yaml",
)
AUDIT_TIMEOUT_SEC = 900

ZERO = (0, 0, 0)
DIRECTIONS = parent.DIRECTIONS
OUTCOMES = parent.OUTCOMES
ROTATIONS = parent.ROTATIONS
SUPPORT = frozenset(parent.SUPPORT)
POINTER = frozenset(parent.POINTER)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frozen_hashes_ok() -> bool:
    return (
        all(file_sha256(PACKET / name) == digest for name, digest in FROZEN.items())
        and file_sha256(ROOT / BLOCK24_SOURCE) == BLOCK24_SOURCE_SHA256
        and file_sha256(ROOT / BLOCK24_NOTE) == BLOCK24_NOTE_SHA256
        and file_sha256(ROOT / BLOCK23_SOURCE) == BLOCK23_SOURCE_SHA256
        and file_sha256(ROOT / AXIOM_NOTE) == AXIOM_NOTE_SHA256
    )


def add(left, right):
    return parent.add(left, right)


def negate(vector):
    return parent.negate(vector)


def subtract(left, right):
    return add(left, negate(right))


def scale(number, vector):
    return parent.scale(number, vector)


def translate(sites, center):
    return frozenset(parent.translate(set(sites), center))


@dataclass(frozen=True)
class ConstraintFactor:
    physical_site: tuple
    role: str
    local_site: tuple
    vector: tuple


@dataclass(frozen=True)
class TipControl:
    anchor: tuple
    front: tuple
    source: tuple
    target_center: tuple
    constraints: tuple[ConstraintFactor, ...]
    carrier_sites: frozenset
    physical_factor_derived: bool


@dataclass(frozen=True)
class PairData:
    front_a: tuple
    front_b: tuple
    source_a: tuple
    source_b: tuple
    anchor_a: tuple
    anchor_b: tuple
    target_a: tuple
    target_b: tuple
    target_shift: tuple
    shared_carrier_sites: tuple
    shared_constrained_sites: tuple
    shared_factor_overlaps: tuple
    product_fidelity: object
    commutator_norm_factor: object
    clean_target_only_overlap: bool


@dataclass(frozen=True)
class StageBScopeClaims:
    stage_b_constructed: bool = False
    conflicting_tip_activated: bool = False
    coordinate_priority_selected: bool = False
    double_writer_constructed: bool = False
    old_record_overwritten: bool = False
    blank_debit_claimed: bool = False
    stop_completion_claimed: bool = False
    arbitrary_reference_channel_claimed: bool = False
    runtime_oracle_used: bool = False
    padding_theorem_claimed: bool = False
    collision_liveness_claimed: bool = False
    blank_production_claimed: bool = False
    rate_claimed: bool = False
    gravity_claimed: bool = False
    axiom_change_claimed: bool = False
    audit_retention_claimed: bool = False
    obligation_retirement_claimed: bool = False
    toe_movement_claimed: bool = False
    general_arbitration_no_go_claimed: bool = False


STAGE_B_SCOPE = StageBScopeClaims()
TRANSLATION_SYMBOLS = sp.symbols("tau_x tau_y tau_z", real=True)


def factor_dictionary(factors):
    return block24.factor_dictionary(factors)


def translated_site(center, local_site):
    return add(center, local_site)


@lru_cache(maxsize=None)
def tip_control(anchor, front, source, mutation=None):
    word = parent.locked_word(front, source)
    factors = block24.make_append_factors(anchor, word, OUTCOMES[0])
    effect = block24.contract_append_effect(factors)
    data = factor_dictionary(factors)
    current_maps = tuple(data["current_pointer_projectors"])
    forward_live = tuple(data["forward_live_prep_maps"])
    forward_pointer = tuple(data["forward_pointer_prep_maps"])

    if mutation == "drop_current_factor":
        current_maps = current_maps[:-1]
    if mutation == "drop_blank_factor":
        forward_pointer = forward_pointer[:-1]

    items = []
    for local_site, input_bit, _output_bit in current_maps:
        items.append(
            ConstraintFactor(
                translated_site(anchor, local_site),
                "current_pointer",
                local_site,
                parent.radial_bloch(local_site, input_bit),
            )
        )
    for local_site, input_vector, _output_vector in forward_live:
        items.append(
            ConstraintFactor(
                translated_site(effect.forward_center, local_site),
                "target_live",
                local_site,
                tuple(input_vector),
            )
        )
    for local_site, input_bit, _output_bit in forward_pointer:
        items.append(
            ConstraintFactor(
                translated_site(effect.forward_center, local_site),
                "target_pointer",
                local_site,
                parent.radial_bloch(local_site, input_bit),
            )
        )

    if mutation == "fake_coordinate" and items:
        first = items[0]
        items[0] = ConstraintFactor(
            (99, 99, 99), first.role, first.local_site, first.vector
        )
    if mutation == "label_only_overlap":
        items = []

    items = tuple(
        sorted(items, key=lambda item: (item.physical_site, item.role, item.local_site))
    )
    current_carrier = translate(SUPPORT, anchor)
    target_carrier = translate(SUPPORT, effect.forward_center)
    return TipControl(
        anchor=anchor,
        front=front,
        source=source,
        target_center=effect.forward_center,
        constraints=items,
        carrier_sites=current_carrier | target_carrier,
        physical_factor_derived=mutation != "label_only_overlap",
    )


def constraint_map(control):
    result = {}
    for item in control.constraints:
        if item.physical_site in result:
            raise ValueError("one eligibility control constrains a site twice")
        result[item.physical_site] = item
    return result


def factor_completeness(control):
    current_sites = translate(POINTER, control.anchor)
    target_pointer_sites = translate(POINTER, control.target_center)
    target_live_sites = translate(SUPPORT - POINTER, control.target_center)
    target_sites = target_pointer_sites | target_live_sites
    items = constraint_map(control)
    role_sites = {
        role: {
            item.physical_site for item in items.values() if item.role == role
        }
        for role in ("current_pointer", "target_live", "target_pointer")
    }
    projectors = tuple(
        pure_qubit_projector(item.vector) for item in items.values()
    )
    rank_one_projectors = all(
        sp.simplify(projector - projector.H) == sp.zeros(2)
        and sp.simplify(projector * projector - projector) == sp.zeros(2)
        and sp.simplify(sp.trace(projector) - 1) == 0
        for projector in projectors
    )
    return (
        control.physical_factor_derived
        and len(items) == 58
        and role_sites["current_pointer"] == set(current_sites)
        and role_sites["target_live"] == set(target_live_sites)
        and role_sites["target_pointer"] == set(target_pointer_sites)
        and set(items) == set(current_sites | target_sites)
        and rank_one_projectors
        and control.anchor not in control.carrier_sites
        and control.target_center not in control.carrier_sites
    )


def shared_product_fidelity(left, right):
    left_map = constraint_map(left)
    right_map = constraint_map(right)
    shared = tuple(sorted(set(left_map) & set(right_map)))
    overlaps = tuple(
        sp.simplify(parent.pure_overlap(left_map[site].vector, right_map[site].vector))
        for site in shared
    )
    q = sp.simplify(sp.prod(overlaps)) if overlaps else sp.S.One
    return shared, overlaps, q


def projections_commute(product_fidelity, mutation=None):
    if mutation == "nonzero_means_commuting":
        return sp.simplify(product_fidelity) != 0
    return sp.simplify(product_fidelity) in (sp.S.Zero, sp.S.One)


def target_shift_candidates(mutation=None):
    if mutation == "shared_target_only":
        return (ZERO,)
    differences = {
        subtract(left, right)
        for left in SUPPORT
        for right in SUPPORT
        if left != right
    }
    return tuple(
        sorted(
            differences,
            key=lambda value: (
                parent.norm2(value),
                sum(abs(component) for component in value),
                value,
            ),
        )
    )


def block_pair_sets(anchor, front):
    target = block24.forward_center(anchor, front)
    return translate(SUPPORT, anchor), translate(SUPPORT, target), target


def clean_target_only_pair(anchor_a, front_a, anchor_b, front_b):
    current_a, target_a, center_a = block_pair_sets(anchor_a, front_a)
    current_b, target_b, center_b = block_pair_sets(anchor_b, front_b)
    target_overlap = target_a & target_b
    clean = (
        bool(target_overlap)
        and current_a.isdisjoint(current_b)
        and current_a.isdisjoint(target_b)
        and current_b.isdisjoint(target_a)
    )
    return clean, current_a, target_a, current_b, target_b, center_a, center_b


def build_pair(
    front_a,
    front_b,
    source_a,
    source_b,
    target_shift,
    translation=ZERO,
    mutation=None,
):
    anchor_a = translation
    target_a = block24.forward_center(anchor_a, front_a)
    target_b = add(target_a, target_shift)
    anchor_b = subtract(target_b, scale(parent.DISPLACEMENT, front_b))
    clean, _current_a, target_sites_a, _current_b, target_sites_b, _, _ = (
        clean_target_only_pair(anchor_a, front_a, anchor_b, front_b)
    )
    control_a = tip_control(anchor_a, front_a, source_a, mutation)
    control_b = tip_control(anchor_b, front_b, source_b, mutation)
    shared, overlaps, q = shared_product_fidelity(control_a, control_b)
    shared_carrier = tuple(sorted(control_a.carrier_sites & control_b.carrier_sites))
    clean &= (
        set(shared_carrier) == set(target_sites_a & target_sites_b)
        and control_a.target_center == target_a
        and control_b.target_center == target_b
    )
    return PairData(
        front_a=front_a,
        front_b=front_b,
        source_a=source_a,
        source_b=source_b,
        anchor_a=anchor_a,
        anchor_b=anchor_b,
        target_a=target_a,
        target_b=target_b,
        target_shift=target_shift,
        shared_carrier_sites=shared_carrier,
        shared_constrained_sites=shared,
        shared_factor_overlaps=overlaps,
        product_fidelity=q,
        commutator_norm_factor=sp.simplify(2 * q * (1 - q)),
        clean_target_only_overlap=bool(clean),
    )


PHYSICAL_MUTATIONS = {
    "drop_current_factor",
    "drop_blank_factor",
    "label_only_overlap",
    "nonzero_means_commuting",
    "shared_target_only",
    "fake_coordinate",
}


@lru_cache(maxsize=None)
def first_noncommuting_clean_pair(mutation=None):
    physical_mutation = mutation if mutation in PHYSICAL_MUTATIONS else None
    source = OUTCOMES[0]
    for shift in target_shift_candidates(physical_mutation):
        for front_a in DIRECTIONS:
            for front_b in DIRECTIONS:
                target_a = block24.forward_center(ZERO, front_a)
                target_b = add(target_a, shift)
                anchor_b = subtract(
                    target_b, scale(parent.DISPLACEMENT, front_b)
                )
                clean, *_rest = clean_target_only_pair(
                    ZERO, front_a, anchor_b, front_b
                )
                if not clean:
                    continue
                pair = build_pair(
                    front_a,
                    front_b,
                    source,
                    source,
                    shift,
                    mutation=physical_mutation,
                )
                if not pair.clean_target_only_overlap:
                    continue
                if not projections_commute(pair.product_fidelity, physical_mutation):
                    return pair
    return None


def witness_factor_details(pair, mutation=None):
    physical_mutation = mutation if mutation in PHYSICAL_MUTATIONS else None
    left = tip_control(pair.anchor_a, pair.front_a, pair.source_a, physical_mutation)
    right = tip_control(pair.anchor_b, pair.front_b, pair.source_b, physical_mutation)
    left_map = constraint_map(left)
    right_map = constraint_map(right)
    return tuple(
        (
            site,
            left_map[site].role,
            left_map[site].local_site,
            left_map[site].vector,
            right_map[site].role,
            right_map[site].local_site,
            right_map[site].vector,
            sp.simplify(parent.pure_overlap(left_map[site].vector, right_map[site].vector)),
        )
        for site in pair.shared_constrained_sites
    )


def pure_qubit_projector(vector):
    identity = sp.eye(2)
    pauli_x = sp.Matrix([[0, 1], [1, 0]])
    pauli_y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    pauli_z = sp.Matrix([[1, 0], [0, -1]])
    return sp.simplify(
        (
            identity
            + vector[0] * pauli_x
            + vector[1] * pauli_y
            + vector[2] * pauli_z
        )
        / 2
    )


def product_projector(vectors):
    result = sp.Matrix([[1]])
    for vector in vectors:
        result = sp.kronecker_product(result, pure_qubit_projector(vector))
    return result


def direct_commutator_norm_factor(details):
    left = product_projector(tuple(entry[3] for entry in details))
    right = product_projector(tuple(entry[6] for entry in details))
    commutator = left * right - right * left
    return sp.simplify(sp.trace(commutator.H * commutator))


def source_label_independence(pair):
    comparisons = (
        build_pair(
            pair.front_a,
            pair.front_b,
            source_a,
            source_b,
            pair.target_shift,
        )
        for source_a in OUTCOMES
        for source_b in OUTCOMES
    )
    return all(
        comparison.clean_target_only_overlap
        and sp.simplify(comparison.product_fidelity - pair.product_fidelity) == 0
        and comparison.shared_factor_overlaps == pair.shared_factor_overlaps
        for comparison in comparisons
    )


def proper_cubic_orbit_certificate(pair, mutation=None):
    if pair is None:
        return False, 0
    physical_mutation = mutation if mutation in PHYSICAL_MUTATIONS else None
    frames = ROTATIONS[:-1] if mutation == "incomplete_frames" else ROTATIONS
    orbit = []
    for rotation in frames:
        front_a = parent.mat_vec(rotation, pair.front_a)
        front_b = parent.mat_vec(rotation, pair.front_b)
        source_a = parent.mat_vec(rotation, pair.source_a)
        source_b = parent.mat_vec(rotation, pair.source_b)
        shift = parent.mat_vec(rotation, pair.target_shift)
        moved = build_pair(
            front_a,
            front_b,
            source_a,
            source_b,
            shift,
            mutation=physical_mutation,
        )
        orbit.append(
            (rotation, front_a, front_b, source_a, source_b, shift, moved)
        )
    complete = (
        len(ROTATIONS) == 24
        and len(frames) == 24
        and len(set(frames)) == 24
        and all(
            parent.determinant3(rotation) == 1
            and sp.Matrix(rotation).T * sp.Matrix(rotation) == sp.eye(3)
            for rotation in frames
        )
        and len(orbit) == 24
        and all(moved.clean_target_only_overlap for *_labels, moved in orbit)
        and all(
            moved.front_a == front_a
            and moved.front_b == front_b
            and moved.source_a == source_a
            and moved.source_b == source_b
            and moved.target_shift == shift
            for (
                _rotation,
                front_a,
                front_b,
                source_a,
                source_b,
                shift,
                moved,
            ) in orbit
        )
        and all(
            sp.simplify(moved.product_fidelity - pair.product_fidelity) == 0
            for *_labels, moved in orbit
        )
        and all(
            not projections_commute(moved.product_fidelity, physical_mutation)
            for *_labels, moved in orbit
        )
    )
    return bool(complete), len(orbit)


def symbolic_relative_translation_identity(site, origin):
    return all(
        sp.simplify(
            (sp.Integer(site[index]) + TRANSLATION_SYMBOLS[index])
            - (sp.Integer(origin[index]) + TRANSLATION_SYMBOLS[index])
            - sp.Integer(site[index] - origin[index])
        )
        == 0
        for index in range(3)
    )


def symbolic_translate(site):
    return tuple(
        sp.Integer(site[index]) + TRANSLATION_SYMBOLS[index]
        for index in range(3)
    )


def translation_certificate(pair, mutation=None):
    if pair is None:
        return False
    physical_mutation = mutation if mutation in PHYSICAL_MUTATIONS else None
    controls = (
        tip_control(pair.anchor_a, pair.front_a, pair.source_a, physical_mutation),
        tip_control(pair.anchor_b, pair.front_b, pair.source_b, physical_mutation),
    )
    factor_coordinates = all(
        symbolic_relative_translation_identity(
            item.physical_site,
            control.anchor
            if item.role == "current_pointer"
            else control.target_center,
        )
        and item.local_site
        == subtract(
            item.physical_site,
            control.anchor
            if item.role == "current_pointer"
            else control.target_center,
        )
        for control in controls
        for item in control.constraints
    )
    carrier_coordinates = all(
        symbolic_relative_translation_identity(site, pair.anchor_a)
        for control in controls
        for site in control.carrier_sites
    )
    constraint_maps = tuple(constraint_map(control) for control in controls)
    shifted_shared_constraints = (
        {symbolic_translate(site) for site in constraint_maps[0]}
        & {symbolic_translate(site) for site in constraint_maps[1]}
    )
    shifted_shared_carriers = (
        {symbolic_translate(site) for site in controls[0].carrier_sites}
        & {symbolic_translate(site) for site in controls[1].carrier_sites}
    )
    shared_sets = (
        shifted_shared_constraints
        == {
            symbolic_translate(site)
            for site in pair.shared_constrained_sites
        }
        and shifted_shared_carriers
        == {symbolic_translate(site) for site in pair.shared_carrier_sites}
    )
    geometry = all(
        symbolic_relative_translation_identity(site, origin)
        for site, origin in (
            (pair.target_a, pair.anchor_a),
            (pair.target_b, pair.anchor_b),
            (pair.anchor_b, pair.anchor_a),
            (pair.target_b, pair.target_a),
        )
    )
    return (
        all(factor_completeness(control) for control in controls)
        and factor_coordinates
        and carrier_coordinates
        and shared_sets
        and geometry
        and pair.target_shift == subtract(pair.target_b, pair.target_a)
    )


def same_target_commuting_control():
    source = OUTCOMES[0]
    for front_a in DIRECTIONS:
        for front_b in DIRECTIONS:
            pair = build_pair(front_a, front_b, source, source, ZERO)
            if pair.clean_target_only_overlap:
                return (
                    pair,
                    sp.simplify(pair.product_fidelity) == 1,
                    projections_commute(pair.product_fidelity),
                )
    return None, False, False


def disjoint_factorization_control():
    left = tip_control(ZERO, DIRECTIONS[0], OUTCOMES[0])
    right = tip_control((50, 50, 50), DIRECTIONS[-1], OUTCOMES[-1])
    shared, overlaps, q = shared_product_fidelity(left, right)
    return (
        left.carrier_sites.isdisjoint(right.carrier_sites)
        and shared == ()
        and overlaps == ()
        and q == 1
        and projections_commute(q)
    )


MUTATION_TARGETS = (
    ("drop_current_factor", "literal_physical_controls"),
    ("drop_blank_factor", "literal_physical_controls"),
    ("label_only_overlap", "literal_physical_controls"),
    ("nonzero_means_commuting", "noncommuting_sharp_projectors"),
    ("shared_target_only", "clean_target_overlap"),
    ("fake_coordinate", "literal_physical_controls"),
    ("incomplete_frames", "proper_cubic_and_translation_orbit"),
)


def scope_guard_results():
    claims = STAGE_B_SCOPE
    return (
        ("stage_b_unconstructed", not claims.stage_b_constructed),
        ("no_conflicting_tip_activation", not claims.conflicting_tip_activated),
        ("no_coordinate_priority", not claims.coordinate_priority_selected),
        ("no_double_writer", not claims.double_writer_constructed),
        ("no_old_record_overwrite", not claims.old_record_overwritten),
        ("no_blank_debit_claim", not claims.blank_debit_claimed),
        ("no_stop_completion_claim", not claims.stop_completion_claimed),
        (
            "no_arbitrary_reference_channel_claim",
            not claims.arbitrary_reference_channel_claimed,
        ),
        ("no_runtime_oracle", not claims.runtime_oracle_used),
        ("no_padding_theorem", not claims.padding_theorem_claimed),
        ("no_collision_liveness_claim", not claims.collision_liveness_claimed),
        ("no_blank_production_claim", not claims.blank_production_claimed),
        ("no_rate_claim", not claims.rate_claimed),
        ("no_gravity_claim", not claims.gravity_claimed),
        ("no_axiom_change_claim", not claims.axiom_change_claimed),
        ("no_audit_retention_claim", not claims.audit_retention_claimed),
        ("no_obligation_retirement_claim", not claims.obligation_retirement_claimed),
        ("no_toe_movement_claim", not claims.toe_movement_claimed),
        (
            "no_general_arbitration_no_go",
            not claims.general_arbitration_no_go_claimed,
        ),
    )


def evaluated_checks(mutation=None):
    physical_mutation = mutation if mutation in PHYSICAL_MUTATIONS else None
    witness = first_noncommuting_clean_pair(mutation)
    factor_ok = False
    details = ()
    if witness is not None:
        left = tip_control(
            witness.anchor_a, witness.front_a, witness.source_a, physical_mutation
        )
        right = tip_control(
            witness.anchor_b, witness.front_b, witness.source_b, physical_mutation
        )
        factor_ok = factor_completeness(left) and factor_completeness(right)
        details = witness_factor_details(witness, physical_mutation)

    orbit_ok, orbit_size = proper_cubic_orbit_certificate(witness, mutation)
    same_target, same_target_q, same_target_commutes = same_target_commuting_control()
    exact_noncommuting = (
        witness is not None
        and witness.clean_target_only_overlap
        and witness.target_shift != ZERO
        and 0 < witness.product_fidelity < 1
        and witness.commutator_norm_factor > 0
        and not projections_commute(witness.product_fidelity, physical_mutation)
    )
    literal_shared_factors = (
        bool(details)
        and len(details) == len(witness.shared_constrained_sites)
        and all(0 <= entry[-1] <= 1 for entry in details)
        and sp.simplify(
            sp.prod(entry[-1] for entry in details) - witness.product_fidelity
        )
        == 0
    ) if witness is not None else False
    direct_commutator = (
        direct_commutator_norm_factor(details)
        if details and len(details) <= 8
        else sp.S.Zero
    )
    direct_matrix_certificate = (
        witness is not None
        and 0 < len(details) <= 8
        and direct_commutator > 0
        and sp.simplify(direct_commutator - witness.commutator_norm_factor) == 0
    )

    return [
        (
            "freeze",
            frozen_hashes_ok(),
            "eight preregistration surfaces plus exact Block23/24 sources, Block24 note, and axiom memo are content frozen",
        ),
        (
            "literal_physical_controls",
            factor_ok,
            "both tips contain all 26 current-pointer and 32 selected-Blank physical input factors",
        ),
        (
            "clean_target_overlap",
            witness is not None and witness.clean_target_only_overlap,
            "the derived pair has disjoint current/cross blocks and overlaps only in its two target carriers",
        ),
        (
            "exact_shared_factor_contraction",
            literal_shared_factors,
            "shared physical Bloch factors contract to the displayed exact product fidelity",
        ),
        (
            "noncommuting_sharp_projectors",
            exact_noncommuting,
            "0<q<1 gives exact positive commutator factor 2q(1-q), so no joint sharp eligibility sector exists",
        ),
        (
            "direct_shared_Hilbert_commutator",
            direct_matrix_certificate,
            "literal shared-site qubit matrices independently reproduce the exact positive Hilbert-Schmidt commutator norm",
        ),
        (
            "source_label_independence",
            witness is not None and source_label_independence(witness),
            "the clean witness is a Blank-carrier overlap and is independent of the two stored outcome labels",
        ),
        (
            "proper_cubic_and_translation_orbit",
            orbit_ok
            and orbit_size == 24
            and witness is not None
            and translation_certificate(witness, mutation),
            "the complete proper-cubic orbit and translated copies retain the same exact q and clean geometry",
        ),
        (
            "commuting_controls",
            same_target is not None
            and same_target_q
            and same_target_commutes
            and disjoint_factorization_control(),
            "exact shared-target and disjoint pairs commute, guarding against a blanket overlap rejection",
        ),
        (
            "A0_stop_gate",
            not STAGE_B_SCOPE.stage_b_constructed and exact_noncommuting,
            "Stage B is not constructed after the registered Stage-A noncommutation wall",
        ),
    ]


def main() -> int:
    checks = evaluated_checks()
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")

    mutation_results = []
    for mutation, designated_check in MUTATION_TARGETS:
        altered = evaluated_checks(mutation)
        altered_by_name = {name: ok for name, ok, _detail in altered}
        rejected = designated_check in altered_by_name and not altered_by_name[
            designated_check
        ]
        mutation_results.append(rejected)
        print(
            f"{'PASS' if rejected else 'FAIL'} mutation_{mutation}: "
            f"designated check {designated_check} rejects"
        )
    mutation_ok = all(mutation_results)
    print(
        f"{'PASS' if mutation_ok else 'FAIL'} executed_model_mutations: "
        f"{sum(mutation_results)}/{len(MUTATION_TARGETS)} altered physical models "
        "reject at their designated checks"
    )

    scope_checks = scope_guard_results()
    for name, ok in scope_checks:
        print(f"{'PASS' if ok else 'FAIL'} scope_{name}")
    scope_ok = all(ok for _name, ok in scope_checks)
    print(
        f"{'PASS' if scope_ok else 'FAIL'} coverage_scope_guards: "
        f"{sum(ok for _name, ok in scope_checks)}/{len(scope_checks)} unexecuted "
        "Stage-B and promotion surfaces remain outside the claim"
    )

    witness = first_noncommuting_clean_pair()
    details = witness_factor_details(witness) if witness is not None else ()
    if witness is not None:
        print(f"WITNESS front_a={witness.front_a} front_b={witness.front_b}")
        print(f"WITNESS anchor_a={witness.anchor_a} anchor_b={witness.anchor_b}")
        print(f"WITNESS target_a={witness.target_a} target_b={witness.target_b}")
        print(f"WITNESS target_shift={witness.target_shift}")
        print(f"WITNESS shared_carrier_sites={len(witness.shared_carrier_sites)}")
        print(
            "WITNESS shared_constrained_sites="
            f"{len(witness.shared_constrained_sites)}"
        )
        print(f"WITNESS local_overlaps={witness.shared_factor_overlaps}")
        print(f"WITNESS product_fidelity_q={witness.product_fidelity}")
        print(f"WITNESS commutator_norm_factor={witness.commutator_norm_factor}")

    print(
        "per_element: checked all 58 constrained factors on each witness tip, "
        f"all {len(details)} shared factor overlaps, and the exact "
        "product/commutator contraction"
    )
    print(
        "per_site: checked literal translated lattice coordinates for current pointer, "
        "target live, and target pointer factors; the witness overlaps only in target carriers"
    )
    print(
        "per_mode: checked stored-label independence plus the complete 24-frame proper-cubic "
        "orbit and exact symbolic covariance under every global translation"
    )
    print(
        "per_block: checked a clean partial target-target overlap, an exact shared-target "
        "commuting control, and a disjoint factorization control"
    )
    print(
        "lattice_wide: checked and not executed -- sharp joint sectors fail at Stage A; "
        "Stage-B graph totalization, unsharp arbitration, owned substrate, collision liveness, "
        "Blank generation, clock, source, gravity, retention, obligations, and "
        "TOE closure remain open"
    )

    passed = sum(ok for _name, ok, _detail in checks)
    scope_passed = sum(ok for _name, ok in scope_checks)
    total = len(checks) + 1 + len(scope_checks)
    total_passed = passed + int(mutation_ok) + scope_passed
    ok = total_passed == total
    if ok:
        print(
            "TERMINAL: EXACT-NONCOMMUTING-BLANK-OVERLAP-WALL-FOR-SHARP-"
            "BLOCK24-HARD-EXCLUSION-SECTORS"
        )
        print(
            "SCOPE: fixed Block24 radial alphabet and sharp memoryless eligibility sectors only; "
            "owned disjoint carriers, unsharp controllers, enlarged pointers, and "
            "recorded collision resources remain live"
        )
    print(
        f"TOTAL: PASS={total_passed} FAIL={total - total_passed}"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
