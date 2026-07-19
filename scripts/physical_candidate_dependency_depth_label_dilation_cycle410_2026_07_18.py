#!/usr/bin/env python3
"""Cycle 410: reversible candidate dependency-edge/depth-label dilation.

The retained Cycle-406 allocation-history M2 controls one preallocated local
candidate-edge bit and a reversible three-bit branchwise depth oracle.  The
oracle reads the actual Cycle-170/255 fixture's parent-depth register (four)
and writes the counterfactual child label (five) without changing the actual
Record DAG.  The same fixed connected-NN X/CNOT/Toffoli schedule is used for
all basis states and has an exact inverse; no host branch query is used.

The output is a coherent dependency/depth proposal, not an actual edge,
Record, or causal-depth member.  Actual dependency depth remains four.
Circuit layers and dependency depth are not proper time.  Sector weights are
not probabilities or Born weights.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_source_response_reversible_record_append_dilation_cycle406_2026_07_18 as c406
import physical_source_response_record_counter_interface_cycle399_2026_07_18 as c399


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CANDIDATE_DEPENDENCY_DEPTH_LABEL_DILATION_CYCLE410_NOTE_2026-07-18.md"
)
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 7e-10
RECORD_BITS = c406.c364.RECORD_BITS
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


Coord = tuple[int, int, int]
Bits = tuple[int, ...]


@dataclass(frozen=True)
class Site:
    coord: Coord
    role: str
    lane: int
    already_in_E406: bool = False


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class Layer:
    name: str
    gates: tuple[Gate, ...]


@dataclass(frozen=True)
class Layout:
    sites: tuple[Site, ...]
    layers: tuple[Layer, ...]
    candidate_history: int
    edge: int
    depth_valid: int
    depth_bus: tuple[int, ...]
    parent_depth: tuple[int, ...]
    output_depth: tuple[int, ...]
    parent_site: Coord = c406.PREDECESSOR_SITE
    child_site: Coord = c406.TARGET_SITE


@dataclass(frozen=True)
class BasisState:
    layout: Layout
    bits: Bits


@dataclass(frozen=True)
class CoherentDependencyDepthProposal:
    parent_site: Coord
    child_site: Coord
    parent_depth: int
    counterfactual_child_depth: int
    classification: str = (
        "coherent reversible dependency/depth proposal, not an actual edge or causal-depth member"
    )


@dataclass(frozen=True)
class OracleKey:
    cycle406: c406.ExtendedKey
    oracle_bits: Bits


OracleState = dict[OracleKey, np.ndarray]


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
        check("the Cycle-410 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_410 g_410 = g_physical,410 e_410",
        "actual cycle-170/255 graph fixture",
        "preallocated local candidate-edge register",
        "reversible branchwise depth oracle",
        "no host branch query",
        "blind held l6",
        "coherent reversible dependency/depth proposal",
        "counterfactual child depth five",
        "actual causal depth remains four",
        "no actual edge or record is added",
        "sector weight, not probability or born weight",
        "circuit layers are not time",
        "not proper time",
        "no law or branch is selected",
        "no gravity or axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note states the complete edge/depth-label and semantic contract", not missing, missing)


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites, label))
    return Gate(kind, sites, label)


def build_layout() -> Layout:
    sites: list[Site] = []

    def add(role: str, lane: int, coord: Coord, *, existing: bool = False) -> int:
        sites.append(Site(coord, role, lane, existing))
        return len(sites) - 1

    # The interface coordinate is exactly the Cycle-406 allocation-history
    # coordinate.  It is represented here for gate-locality checks but is not
    # counted again as a new M2.
    candidate_history = add(
        "CYCLE406_ALLOCATION_HISTORY",
        0,
        c406.LAYOUT.sites[c406.LAYOUT.allocation_history].coord,
        existing=True,
    )
    edge = add("CANDIDATE_EDGE", 0, (0, 39, RECORD_BITS))
    depth_valid = add("DEPTH_LABEL_VALID", 0, (0, 39, RECORD_BITS - 1))
    depth_bus = tuple(
        add("DEPTH_BUS", lane, (0, 40 + lane, RECORD_BITS))
        for lane in range(3)
    )
    parent_depth = tuple(
        add("PARENT_DEPTH", lane, (1, 40 + lane, RECORD_BITS))
        for lane in range(3)
    )
    output_depth = tuple(
        add("COUNTERFACTUAL_CHILD_DEPTH", lane, (0, 40 + lane, RECORD_BITS - 1))
        for lane in range(3)
    )

    layers = [
        Layer("candidate-edge-latch", (gate("CNOT", (candidate_history, edge), "candidate-edge-latch"),)),
        Layer("depth-valid-latch", (gate("CNOT", (edge, depth_valid), "depth-valid-latch"),)),
        Layer("depth-bus-start", (gate("CNOT", (edge, depth_bus[0]), "depth-bus:lane0"),)),
        Layer("depth-bus-1", (gate("CNOT", (depth_bus[0], depth_bus[1]), "depth-bus:lane1"),)),
        Layer("depth-bus-2", (gate("CNOT", (depth_bus[1], depth_bus[2]), "depth-bus:lane2"),)),
        Layer(
            "controlled-parent-depth-copy",
            tuple(
                gate(
                    "TOFFOLI",
                    (depth_bus[lane], parent_depth[lane], output_depth[lane]),
                    f"depth-copy:lane{lane}",
                )
                for lane in range(3)
            ),
        ),
        # The actual parent depth is four = 100 binary and is even.  Adding
        # one to this declared fixture flips only the least-significant bit.
        Layer("counterfactual-successor", (gate("CNOT", (depth_bus[0], output_depth[0]), "depth-increment"),)),
        Layer("depth-bus-uncompute-2", (gate("CNOT", (depth_bus[1], depth_bus[2]), "depth-bus-uncompute:lane2"),)),
        Layer("depth-bus-uncompute-1", (gate("CNOT", (depth_bus[0], depth_bus[1]), "depth-bus-uncompute:lane1"),)),
        Layer("depth-bus-uncompute-start", (gate("CNOT", (edge, depth_bus[0]), "depth-bus-uncompute:lane0"),)),
    ]
    return Layout(
        tuple(sites),
        tuple(layers),
        candidate_history,
        edge,
        depth_valid,
        depth_bus,
        parent_depth,
        output_depth,
    )


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def support_connected_nn(item: Gate, sites: tuple[Site, ...]) -> bool:
    coords = tuple(sites[index].coord for index in item.sites)
    reached = {0}
    while True:
        grown = reached | {
            right
            for left in reached
            for right in range(len(coords))
            if manhattan(coords[left], coords[right]) == 1
        }
        if grown == reached:
            return len(reached) == len(coords)
        reached = grown


def layer_conflicts(layer: Layer) -> int:
    used: set[int] = set()
    failures = 0
    for item in layer.gates:
        failures += len(used.intersection(item.sites))
        used.update(item.sites)
    return failures


def validate_layout(layout: Layout) -> None:
    if len(layout.sites) != len({site.coord for site in layout.sites}):
        raise RuntimeError("Cycle-410 M2 coordinates overlap")
    if manhattan(layout.parent_site, layout.child_site) != 1:
        raise RuntimeError("candidate dependency edge is not nearest-neighbor")
    for layer in layout.layers:
        if layer_conflicts(layer):
            raise RuntimeError(("layer conflict", layer.name))
        for item in layer.gates:
            if not support_connected_nn(item, layout.sites):
                raise RuntimeError(("nonlocal edge/depth oracle gate", item))


def validate_basis(state: BasisState) -> None:
    if not isinstance(state, BasisState):
        raise TypeError("edge/depth oracle requires one BasisState")
    if len(state.bits) != len(state.layout.sites):
        raise ValueError("edge/depth basis width mismatch")
    if any(value not in (0, 1) for value in state.bits):
        raise ValueError("edge/depth basis is not binary")


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    else:
        raise ValueError(item.kind)


def apply_layers(
    state: BasisState,
    layers: tuple[Layer, ...] | None = None,
    *,
    reverse: bool = False,
) -> BasisState:
    """Apply one fixed state-independent reversible schedule."""

    validate_basis(state)
    bits = list(state.bits)
    selected = state.layout.layers if layers is None else layers
    ordered_layers = reversed(selected) if reverse else selected
    for layer in ordered_layers:
        ordered_gates = reversed(layer.gates) if reverse else layer.gates
        for item in ordered_gates:
            apply_gate(bits, item)
    return replace(state, bits=tuple(bits))


def int_to_bits(value: int, width: int = 3) -> Bits:
    if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value < 2**width:
        raise ValueError((value, width))
    return tuple((value >> lane) & 1 for lane in range(width))


def bits_to_int(values: Bits) -> int:
    return sum(value << lane for lane, value in enumerate(values))


def selected(bits: Bits, sites: tuple[int, ...]) -> Bits:
    return tuple(bits[index] for index in sites)


def actual_graph():
    return c399.c255.event_dag()


def counterfactual_graph(base=None, *, child_site: Coord | None = None, with_parent: bool = True):
    base = actual_graph() if base is None else base
    child_site = LAYOUT.child_site if child_site is None else child_site
    name = "response_candidate"
    events = dict(base.events)
    events[name] = c399.c255.Event(
        name,
        child_site,
        1,
        frozenset((base.completion,)) if with_parent else frozenset(),
    )
    return c399.c255.EventDag(events, name, "response_candidate_counterfactual")


def cycle170_certificate(dag):
    expected = {event.site: str(event.value) for event in dag.events.values()}
    dependencies = {
        event.site: frozenset(dag.events[parent].site for parent in event.parents)
        for event in dag.events.values()
    }
    completion = dag.events[dag.completion].site
    return c399.c170.dag_certificate(expected, dependencies, (completion,))


def prepare(
    layout: Layout,
    base,
    *,
    candidate_history: int,
    declared_parent_depth: int | None = None,
    edge: int = 0,
    depth_valid: int = 0,
    depth_bus: Bits = (0, 0, 0),
    output_depth: Bits = (0, 0, 0),
) -> BasisState:
    if candidate_history not in (0, 1):
        raise ValueError("candidate history must be binary")
    actual_depth = int(c399.c255.depth_certificate(base)["depth"])
    declared_parent_depth = actual_depth if declared_parent_depth is None else declared_parent_depth
    if declared_parent_depth != actual_depth:
        raise ValueError("parent-depth input does not match the actual Cycle-255 fixture")
    if base.events[base.completion].site != layout.parent_site:
        raise ValueError("oracle parent site does not match the actual completion")
    if manhattan(layout.parent_site, layout.child_site) != 1:
        raise ValueError("oracle child is outside the local dependency domain")
    if edge != 0 or depth_valid != 0 or any(depth_bus) or any(output_depth):
        raise ValueError("edge/depth output registers must be preallocated blank")
    if len(depth_bus) != 3 or len(output_depth) != 3:
        raise ValueError("edge/depth oracle requires three-bit registers")

    bits = [0] * len(layout.sites)
    bits[layout.candidate_history] = candidate_history
    for site, value in zip(layout.parent_depth, int_to_bits(declared_parent_depth)):
        bits[site] = value
    return BasisState(layout, tuple(bits))


def workspace_leakage(state: BasisState) -> int:
    return sum(state.bits[index] for index in state.layout.depth_bus)


def proposal_label(state: BasisState) -> CoherentDependencyDepthProposal | None:
    layout = state.layout
    parent = bits_to_int(selected(state.bits, layout.parent_depth))
    child = bits_to_int(selected(state.bits, layout.output_depth))
    accepted = bool(
        state.bits[layout.edge]
        and state.bits[layout.depth_valid]
        and parent == 4
        and child == 5
        and workspace_leakage(state) == 0
    )
    if not accepted:
        return None
    return CoherentDependencyDepthProposal(
        layout.parent_site,
        layout.child_site,
        parent,
        child,
    )


def without_gate(layers: tuple[Layer, ...], label: str) -> tuple[tuple[Layer, ...], int]:
    removed = 0
    output = []
    for layer in layers:
        gates = tuple(item for item in layer.gates if item.label != label)
        removed += len(layer.gates) - len(gates)
        output.append(replace(layer, gates=gates))
    return tuple(output), removed


def encode_oracle(state: c406.ExtendedState, base) -> OracleState:
    output: OracleState = {}
    for key, value in state.items():
        history = key.register_bits[c406.LAYOUT.allocation_history]
        oracle = prepare(LAYOUT, base, candidate_history=history)
        output[OracleKey(key, oracle.bits)] = value.copy()
    return output


def physical_oracle(state: OracleState, *, reverse: bool = False) -> OracleState:
    output: OracleState = {}
    for key, value in state.items():
        basis = BasisState(LAYOUT, key.oracle_bits)
        updated = apply_layers(basis, reverse=reverse)
        new_key = OracleKey(key.cycle406, updated.bits)
        output[new_key] = output.get(new_key, 0) + value
    return output


def oracle_residual(left: OracleState, right: OracleState) -> float:
    keys = set(left) | set(right)
    residual = 0.0
    for key in keys:
        template = left.get(key, right.get(key))
        assert template is not None
        a = left.get(key, np.zeros_like(template))
        b = right.get(key, np.zeros_like(template))
        residual += float(np.vdot(a - b, a - b).real)
    return float(np.sqrt(residual))


def proposal_sector_weight(state: OracleState) -> float:
    return float(
        sum(
            np.vdot(value, value).real
            for key, value in state.items()
            if proposal_label(BasisState(LAYOUT, key.oracle_bits)) is not None
        )
    )


def layout_and_graph_controls() -> None:
    print("\nLOCAL ORACLE LAYOUT / ACTUAL GRAPH FIXTURE")
    validate_layout(LAYOUT)
    added = sum(not site.already_in_E406 for site in LAYOUT.sites)
    gates = sum(len(layer.gates) for layer in LAYOUT.layers)
    support_failures = sum(
        not support_connected_nn(item, LAYOUT.sites)
        for layer in LAYOUT.layers
        for item in layer.gates
    )
    check(
        "the preallocated 11-M2 edge/depth oracle uses one fixed 10-layer connected-NN reversible schedule",
        added == 11
        and len(LAYOUT.layers) == 10
        and gates == 12
        and support_failures == 0
        and sum(layer_conflicts(layer) for layer in LAYOUT.layers) == 0
        and {item.kind for layer in LAYOUT.layers for item in layer.gates}
        == {"CNOT", "TOFFOLI"},
        {
            "added_M2": added,
            "existing_Cycle406_history_interface_M2": 1,
            "total_installed_common_M2": 5078 + added,
            "layers": len(LAYOUT.layers),
            "primitive_gates": gates,
            "maximum_gate_support": 3,
            "connected_NN_failures": support_failures,
            "circuit_layers_are_time": False,
        },
    )

    base = actual_graph()
    proposed = counterfactual_graph(base)
    base255 = c399.c255.depth_certificate(base)
    proposed255 = c399.c255.depth_certificate(proposed)
    base170 = cycle170_certificate(base)
    proposed170 = cycle170_certificate(proposed)
    check(
        "the actual Cycle-170/255 fixture has depth four and the one-edge branchwise counterfactual has depth five",
        base.completion == "tail0"
        and base.events[base.completion].site == LAYOUT.parent_site
        and base255["depth"] == base170["depth"] == 4
        and proposed255["depth"] == proposed170["depth"] == 5
        and not c399.c255.local_failures(base)
        and not c399.c255.local_failures(proposed),
        {
            "actual_completion": base.completion,
            "actual_parent_site": base.events[base.completion].site,
            "actual_depth_Cycle255/Cycle170": (base255["depth"], base170["depth"]),
            "counterfactual_child_site": proposed.events[proposed.completion].site,
            "counterfactual_depth_Cycle255/Cycle170": (
                proposed255["depth"],
                proposed170["depth"],
            ),
            "actual_graph_mutated": False,
        },
    )


def basis_truth_and_inverse_controls() -> None:
    print("\nBRANCHWISE EDGE / DEPTH TRUTH TABLE AND INVERSE")
    base = actual_graph()
    rows = []
    failures = 0
    for history in (0, 1):
        source = prepare(LAYOUT, base, candidate_history=history)
        output = apply_layers(source)
        restored = apply_layers(output, reverse=True)
        label = proposal_label(output)
        failures += int((label is not None) != bool(history))
        failures += int(restored != source)
        failures += workspace_leakage(output)
        rows.append(
            {
                "Cycle406_candidate_history": history,
                "candidate_edge": output.bits[LAYOUT.edge],
                "depth_label_valid": output.bits[LAYOUT.depth_valid],
                "parent_depth_label": bits_to_int(selected(output.bits, LAYOUT.parent_depth)),
                "counterfactual_child_depth_label": bits_to_int(
                    selected(output.bits, LAYOUT.output_depth)
                ),
                "proposal_present": label is not None,
                "workspace_leakage": workspace_leakage(output),
                "inverse_exact": restored == source,
            }
        )
    check(
        "history zero stays blank while history one writes exactly the local edge and branchwise depth-five proposal with an exact inverse",
        failures == 0
        and rows[0]["counterfactual_child_depth_label"] == 0
        and rows[1]["parent_depth_label"] == 4
        and rows[1]["counterfactual_child_depth_label"] == 5,
        {"rows": rows, "failures": failures},
    )


def train_held_controls(factors, packet_layout, packet_initial, fixture, payloads):
    print("\nL5 / BLIND HELD-L6 COMPOSED DILATION")
    payload, prior = payloads[:2]
    base = actual_graph()
    rows = []
    failures = 0
    held = {}
    expected = {
        "unit_weight": 5.958479723237607e-06,
        "coefficient_two": 3.0046754132975383e-05,
    }
    for route in c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                source = c406.c403.pre_admission_response(
                    origin, route, length, factors, packet_layout, packet_initial
                )
                encoded406 = c406.encode_extended(
                    source, origin, c406.LAYOUT, fixture, payload, prior
                )
                output406 = c406.physical_dilation(encoded406)
                encoded410 = encode_oracle(output406, base)
                output410 = physical_oracle(encoded410)
                restored410 = physical_oracle(output410, reverse=True)
                restored406 = c406.physical_dilation(
                    {key.cycle406: value for key, value in restored410.items()},
                    reverse=True,
                )
                target_weight = c406.c403.target_sector_weight(source, origin)
                candidate_weight = c406.candidate_sector_weight(output406, fixture)
                proposal_weight = proposal_sector_weight(output410)
                oracle_inverse = oracle_residual(restored410, encoded410)
                full_inverse = c406.extended_residual(restored406, encoded406)
                failures += int(abs(target_weight - expected[route]) > TOLERANCE)
                failures += int(abs(candidate_weight - target_weight) > TOLERANCE)
                failures += int(abs(proposal_weight - target_weight) > TOLERANCE)
                failures += int(oracle_inverse > TOLERANCE or full_inverse > TOLERANCE)
                rows.append(
                    {
                        "route": route,
                        "L": length,
                        "held": length == HELD_LENGTH,
                        "origin": "A" if origin == 0 else "C",
                        "target_sector_weight": target_weight,
                        "Cycle406_candidate_sector_weight": candidate_weight,
                        "Cycle410_edge_depth_proposal_sector_weight": proposal_weight,
                        "oracle_inverse_residual": oracle_inverse,
                        "composed_inverse_residual": full_inverse,
                    }
                )
                if length == HELD_LENGTH:
                    held[(route, origin)] = (
                        source,
                        encoded406,
                        output406,
                        encoded410,
                        output410,
                    )
    check(
        "the fixed composed dilation preserves reciprocal route-distinct L5/held-L6 weights and closes both inverse layers exactly",
        failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "weight_semantics": "squared-norm sector weight, not probability/Born weight",
            "law_selected": False,
            "branch_selected": False,
        },
    )
    return held


def rotated_layout(layout: Layout, frame: np.ndarray) -> Layout:
    sites = tuple(
        replace(site, coord=c399.c255.add(tuple(int(v) for v in frame @ np.asarray(site.coord)), (0, 0, 0)))
        for site in layout.sites
    )
    parent = tuple(int(v) for v in frame @ np.asarray(layout.parent_site))
    child = tuple(int(v) for v in frame @ np.asarray(layout.child_site))
    return replace(layout, sites=sites, parent_site=parent, child_site=child)


def covariance_controls(factors) -> None:
    print("\nALL 24 PROPER-CUBIC FRAMES")
    coin, first, second, contact = factors
    source_covariance = c399.c396.c319.covariance_schedule_controls(
        c399.c396.LABELS,
        "path",
        coin,
        first,
        second,
        contact,
        contact @ second @ first @ coin,
        contact @ first @ second @ coin,
    )
    failures = support_failures = inherited_support_failures = 0
    base = actual_graph()
    proposed = counterfactual_graph(base)
    for frame in c399.c255.proper_frames():
        framed = rotated_layout(LAYOUT, frame)
        validate_layout(framed)
        support_failures += sum(
            not support_connected_nn(item, framed.sites)
            for layer in framed.layers
            for item in layer.gates
        )
        framed406 = c406.rotated_layout(c406.LAYOUT, frame)
        inherited_support_failures += sum(
            not c406.support_connected_nn(item, framed406.sites)
            for layer in framed406.layers
            for item in layer.gates
        )
        rotated_base = c399.c255.transformed(base, frame)
        rotated_proposed = c399.c255.transformed(proposed, frame)
        source = prepare(framed, rotated_base, candidate_history=1)
        output = apply_layers(source)
        observed = proposal_label(output)
        failures += int(
            observed
            != CoherentDependencyDepthProposal(
                framed.parent_site,
                framed.child_site,
                4,
                5,
            )
        )
        failures += int(c399.c255.depth_certificate(rotated_base)["depth"] != 4)
        failures += int(c399.c255.depth_certificate(rotated_proposed)["depth"] != 5)
        failures += len(c399.c255.local_failures(rotated_base))
        failures += len(c399.c255.local_failures(rotated_proposed))
        failures += int(apply_layers(output, reverse=True) != source)
    frames = c399.c255.proper_frames()
    check(
        "source, inherited candidate compiler, local edge, depth oracle, and counterfactual graph cover all 24 proper-cubic frames",
        len(frames) == 24
        and source_covariance["maximum_update_covariance_residual"] < TOLERANCE
        and source_covariance["frame_group_law_failures"] == 0
        and failures == support_failures == inherited_support_failures == 0,
        {
            "source_covariance": source_covariance,
            "rotated_oracle_graph_or_inverse_failures": failures,
            "rotated_oracle_NN_failures": support_failures,
            "rotated_Cycle406_NN_failures": inherited_support_failures,
        },
    )


def identity_and_fixture_controls(held, factors, packet_layout, packet_initial) -> None:
    print("\nRECORD IDENTITY / PHYSICAL FIXTURES")
    source, _encoded406, output406, encoded410, output410 = held[("unit_weight", 0)]
    prior_failures = payload_failures = counter_hash_failures = cycle406_failures = 0
    original_hash = c399.c360.record_hash(packet_initial)
    reference_register = c406.BasisState(
        c406.LAYOUT, next(iter(output406)).register_bits
    )
    reference_prior = c406.prior_signature(reference_register)
    reference_payload = c406.selected(
        reference_register.bits, c406.LAYOUT.payload_source
    )
    before_by_base = {key.cycle406: key.oracle_bits for key in encoded410}
    for key in output410:
        if key.cycle406 not in before_by_base:
            cycle406_failures += 1
            continue
        before406 = BasisState(LAYOUT, before_by_base[key.cycle406])
        after406 = BasisState(LAYOUT, key.oracle_bits)
        cycle406_failures += int(
            selected(before406.bits, LAYOUT.parent_depth)
            != selected(after406.bits, LAYOUT.parent_depth)
        )
        register = c406.BasisState(c406.LAYOUT, key.cycle406.register_bits)
        prior_failures += int(
            c406.prior_signature(register) != reference_prior
        )
        payload_failures += int(
            c406.selected(register.bits, c406.LAYOUT.payload_source)
            != reference_payload
        )
        bridge = key.cycle406.bridge
        counter_hash_failures += int(
            c399.c360.record_hash(c399.c360.MachineState(packet_layout, bridge.a_bits))
            != original_hash
        )
        counter_hash_failures += int(
            c399.c360.record_hash(c399.c360.MachineState(packet_layout, bridge.c_bits))
            != original_hash
        )
    cycle406_failures += int(
        {key.cycle406 for key in output410} != set(output406)
    )

    number_values = np.asarray(
        [label[0] + label[2] + label[4] for label in c399.c396.LABELS], dtype=float
    )
    before = c399.initial_bridge_state(0, packet_layout, packet_initial)
    number_before = sum(np.vdot(value, number_values * value).real for value in before.values())
    number_after = sum(np.vdot(value, number_values * value).real for value in source.values())
    update_rows, _ = c399.source_factors()
    coefficient_ops = c399.c396.c322.local_source_blocks(c399.c396.ANGLE)
    unit_ops = c399.c396.c325.unit_weight_local_source(c399.c396.ANGLE)
    coefficient_vector = max(
        np.linalg.norm(coefficient_ops[1] @ operator - operator @ coefficient_ops[1])
        for operator in coefficient_ops[4]
    )
    unit_vector = max(
        np.linalg.norm(unit_ops[1] @ operator - operator @ unit_ops[1])
        for operator in unit_ops[7]
    )
    contact_columns = np.count_nonzero(abs(factors[3].diagonal() - 1) > 2e-14)
    check(
        "the oracle preserves every Cycle406 register plus prior Cycle364/Cycle399 Record identity and payload",
        prior_failures == payload_failures == counter_hash_failures == cycle406_failures == 0,
        {
            "Cycle406_key_or_parent_depth_failures": cycle406_failures,
            "Cycle364_prior_identity_failures": prior_failures,
            "proposal_payload_failures": payload_failures,
            "Cycle399_Record_hash": original_hash,
            "Cycle399_hash_failures": counter_hash_failures,
        },
    )
    check(
        "the edge/depth spectator preserves mass, Q, number, vector ledgers, and the Cycle-230 contact fixture",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and abs(number_after - number_before) < TOLERANCE
        and all(key.q_key[0] in ("R", "L") for key in source)
        and coefficient_vector < TOLERANCE
        and unit_vector < TOLERANCE
        and contact_columns == 645,
        {
            "mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_mass": update_rows["three_cell_rest_mass"],
            "global_Q": 1,
            "matter_number_before": float(number_before),
            "matter_number_after": float(number_after),
            "coefficient_two_vector_commutator": coefficient_vector,
            "unit_weight_vector_commutator": unit_vector,
            "contact_nontrivial_columns": int(contact_columns),
            "oracle_action_on_matter": "identity",
        },
    )


def deletion_and_domain_controls() -> None:
    print("\nDELETION / LEAKAGE / DOMAIN CONTROLS")
    base = actual_graph()
    source = prepare(LAYOUT, base, candidate_history=1)
    nominal = apply_layers(source)
    rows = {}
    for name, label in (
        ("edge_latch", "candidate-edge-latch"),
        ("depth_valid", "depth-valid-latch"),
        ("high_parent_bit_copy", "depth-copy:lane2"),
        ("successor_increment", "depth-increment"),
        ("middle_bus", "depth-bus:lane1"),
    ):
        layers, removed = without_gate(LAYOUT.layers, label)
        output = apply_layers(source, layers)
        rows[name] = {
            "removed": removed,
            "proposal_present": proposal_label(output) is not None,
            "edge": output.bits[LAYOUT.edge],
            "valid": output.bits[LAYOUT.depth_valid],
            "child_depth": bits_to_int(selected(output.bits, LAYOUT.output_depth)),
            "workspace_leakage": workspace_leakage(output),
        }

    cut = counterfactual_graph(base, with_parent=False)
    moved = counterfactual_graph(base, child_site=(1, 1, 3))
    cut255 = c399.c255.depth_certificate(cut)["depth"]
    cut170_certificate = cycle170_certificate(cut)
    cut170_output = cut170_certificate["output_depths"][0]
    cut170_global = cut170_certificate["depth"]
    rejections = 0
    malformed = (
        lambda: prepare(LAYOUT, base, candidate_history=2),
        lambda: prepare(LAYOUT, base, candidate_history=1, declared_parent_depth=3),
        lambda: prepare(LAYOUT, base, candidate_history=1, edge=1),
        lambda: prepare(LAYOUT, base, candidate_history=1, output_depth=(1, 0, 1)),
        lambda: prepare(replace(LAYOUT, child_site=(1, 1, 3)), base, candidate_history=1),
    )
    for probe in malformed:
        try:
            probe()
        except (AssertionError, KeyError, TypeError, ValueError):
            rejections += 1
    check(
        "edge, valid, parent-depth, successor, and bus deletions prevent an accepted proposal while nominal workspace is clean",
        proposal_label(nominal) is not None
        and workspace_leakage(nominal) == 0
        and all(row["removed"] == 1 for row in rows.values())
        and not any(row["proposal_present"] for row in rows.values()),
        {"nominal_workspace_leakage": workspace_leakage(nominal), "deletions": rows},
    )
    check(
        "deleting the counterfactual parent edge changes the named child/output depth to one while Cycle170 retains the base graph's global depth four",
        cut255 == cut170_output == 1
        and cut170_global == 4
        and len(c399.c255.local_failures(moved)) == 1,
        {
            "edge_deleted_named_child_depth_Cycle255": cut255,
            "edge_deleted_output_depth_Cycle170": cut170_output,
            "edge_deleted_global_depth_Cycle170": cut170_global,
            "moved_child_local_failures": c399.c255.local_failures(moved),
            "actual_graph_changed": False,
        },
    )
    check(
        "nonbinary history, wrong parent depth, nonblank outputs, and nonlocal child domains are rejected",
        rejections == len(malformed),
        {"rejections": rejections, "probes": len(malformed)},
    )


def physical_intertwiner_controls(factors) -> None:
    print("\nE410 / G410 PHYSICAL INTERTWINER")
    encodings, _reducer, _support, gram_rows = c399.c396.build_shell(HELD_LENGTH)
    encoding = encodings[c399.c396.c319.ORDER_INDEX[(0, 1, 2)]]
    initial = c399.c396.initial_response_state(0)
    physical_initial = c399.c396.encode_state(initial, encoding)
    logical = c399.c396.logical_step(initial, "unit_weight", HELD_LENGTH, factors)
    physical = c399.c396.physical_step(
        physical_initial, encoding, "unit_weight", HELD_LENGTH, factors
    )
    source_residual = c399.c396.state_residual(
        physical, c399.c396.encode_state(logical, encoding)
    )
    basis = prepare(LAYOUT, actual_graph(), candidate_history=1)
    output = apply_layers(basis)
    restored = apply_layers(output, reverse=True)
    check(
        "E_410 G_410 = G_physical,410 E_410 on the declared code and the composed physical inverse closes exactly",
        max(gram_rows) < TOLERANCE
        and source_residual < TOLERANCE
        and restored == basis,
        {
            "six_order_Gram_raw_maxima": gram_rows,
            "Cycle396_source_factor_intertwiner": source_residual,
            "Cycle406_inherited_register_intertwiner": 0,
            "Cycle410_oracle_permutation_intertwiner": 0,
            "Cycle410_inverse_residual": 0,
            "E410": "E406 tensor basis embedding of edge/depth/work registers",
            "host_branch_query": False,
        },
    )


def semantic_and_inventory_controls() -> None:
    print("\nACTUAL-EDGE / CAUSAL-DEPTH SEMANTIC FIREWALL")
    base = actual_graph()
    base_snapshot = dict(base.events)
    output = apply_layers(prepare(LAYOUT, base, candidate_history=1))
    label = proposal_label(output)
    actual255 = c399.c255.depth_certificate(base)["depth"]
    actual170 = cycle170_certificate(base)["depth"]
    counter = counterfactual_graph(base)
    counter255 = c399.c255.depth_certificate(counter)["depth"]
    counter170 = cycle170_certificate(counter)["depth"]
    check(
        "the coherent edge/depth register is only a proposal: the actual Record DAG is unchanged at depth four while its branchwise counterfactual label predicts five",
        label is not None
        and label.classification
        == "coherent reversible dependency/depth proposal, not an actual edge or causal-depth member"
        and base.events == base_snapshot
        and actual255 == actual170 == 4
        and counter255 == counter170 == label.counterfactual_child_depth == 5,
        {
            "proposal_edge": None if label is None else (label.parent_site, label.child_site),
            "actual_edge_added": False,
            "actual_Record_added": False,
            "actual_depth_Cycle255/Cycle170": (actual255, actual170),
            "branchwise_counterfactual_depth_Cycle255/Cycle170": (
                counter255,
                counter170,
            ),
            "oracle_inverse_defined": True,
            "circuit_layers": len(LAYOUT.layers),
            "circuit_layers_are_time": False,
            "depth_is_proper_time": False,
        },
    )
    inventory = {
        "supplied": (
            "exact Cycle406 coherent candidate label and allocation-history interface",
            "actual Cycle170/255 five-Record DAG, completion site, parent depth four, and depth algorithms",
            "11 preallocated edge/depth/work M2 and fixed 10-layer oracle",
            "one chosen adjacent counterfactual child site and binary depth representation",
            "finite L5/L6 source domains, initial column, and all proper-cubic frames",
        ),
        "derived": (
            "exact local candidate-edge export, depth-four to counterfactual-depth-five oracle, cleanup, and inverse",
            "Cycle170/Cycle255 agreement, covariance, reciprocal weights, fixture and identity preservation",
            "deletion and lawful-domain discrimination",
        ),
        "open": (
            "actual Record formation, actual dependency-edge admission, and actual depth-five member",
            "law/outcome selection, irreversible permanence, renewal, and concurrency",
            "normalized statistics/Born law, metric time, source/stress, energy, and gravity",
        ),
        "actual_graph_mutated": False,
        "law_selected": False,
        "branch_selected": False,
        "host_branch_query": False,
        "negative_or_minimum_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
    }
    check(
        "the supplied/derived/open inventory separates the constructive oracle from actual graph mutation and law selection",
        not inventory["actual_graph_mutated"]
        and not inventory["law_selected"]
        and not inventory["branch_selected"]
        and not inventory["host_branch_query"]
        and not inventory["negative_or_minimum_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    print("CYCLE 410: REVERSIBLE CANDIDATE DEPENDENCY-EDGE / DEPTH-LABEL DILATION")
    note_contract()
    layout_and_graph_controls()
    basis_truth_and_inverse_controls()
    fixture = c406.c364.c342.c338.build_fixture(HELD_LENGTH)
    payloads = c406.c364.words(fixture, 2)
    _rows, factors = c399.source_factors()
    packet_layout, packet_initial = c399.packet_fixture()
    held = train_held_controls(
        factors, packet_layout, packet_initial, fixture, payloads
    )
    covariance_controls(factors)
    identity_and_fixture_controls(held, factors, packet_layout, packet_initial)
    deletion_and_domain_controls()
    physical_intertwiner_controls(factors)
    semantic_and_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_CANDIDATE_DEPENDENCY_DEPTH_LABEL_DILATION_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_CANDIDATE_DEPENDENCY_DEPTH_LABEL_DILATION_CERTIFIED")
    return 0


LAYOUT = build_layout()


if __name__ == "__main__":
    raise SystemExit(main())
