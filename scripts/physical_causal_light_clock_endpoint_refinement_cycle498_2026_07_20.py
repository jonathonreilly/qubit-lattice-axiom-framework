#!/usr/bin/env python3
"""Cycle 498: physical causal-front endpoint-clock/refinement tournament.

The positive statements are conditional on a supplied echo/formation law.
Clock readout is computed only from encoded endpoint, lineage, and geometry
words.  Host update count, circuit layer/depth, and phase are never decoder
inputs.  A Cycle219 phase/acoustic shortcut is retained only as an adversarial
finite control, not as an impossibility result.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from math import pi, sqrt
from pathlib import Path
import inspect
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19 as c444
import common_matter_field_coin_family_cycle219_2026_07_16 as c219


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CAUSAL_LIGHT_CLOCK_ENDPOINT_REFINEMENT_CYCLE498_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
CLOCK_BITS = c444.CLOCK_BITS
GEOMETRY_BITS = 6
A_TRAIN_LENGTHS = (1, 2, 3)
A_HELD_LENGTHS = (4, 6)
B_TRAIN_LENGTH = 3
B_HELD_LENGTH = 6
TARGET_CLOCK_CELLS_PER_DIRECTED_EDGE = Fraction(1, 1)
TARGET_FINE_PER_K2 = Fraction(2, 1)
TARGET_FINE_PER_K3 = Fraction(3, 1)
TOL = 2e-12
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3
Word = tuple[int, ...]
Coord = tuple[int, int, int]
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle444 runner": "75a7f42ebbea25702474b8856413cbc2bd4c5e37d8d04b8ccf7e3b4d86f50262",
    "Cycle444 note": "8eceb021c5e14853453d65729ef491042eb8255a48fc47494be475ef4edf48f2",
    "Cycle486 runner": "4cbd0b74df773b64db500647dcd03ab2767d499a7f655c3ac7d8054915246997",
    "Cycle486 note": "43e9536b9dc125f533c982e6c9cf22d68717c3e1ab1c6b5de1bec4e0fc1a3a3d",
    "Cycle347 runner": "7f65c80507d19425a2c481adf8996aa637c6334f3baa4f8508eb53dad3d51db6",
    "Cycle347 note": "1353904c4cdd9e56f7846c7be2060715692bfb92fe015fc7858edae7f125635a",
    "Cycle219 runner": "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "Cycle219 note": "999e88c014f22637caeeb904bba3c27ee5beff8f4bbf04975f625094035a28ec",
    "tick-edge boundary": "ebb1932d9089baf5b3ba36ef8c7565283fec77cf018c97ed04a4457e19df75f6",
    "scale primitive": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "kinetic primitive": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "minimal axioms": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}
FROZEN_PATHS = {
    "Cycle444 runner": Path(c444.__file__),
    "Cycle444 note": c444.NOTE,
    "Cycle486 runner": ROOT / "scripts/physical_record_occurrence_clock_endpoint_adapter_cycle486_2026_07_20.py",
    "Cycle486 note": ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RECORD_OCCURRENCE_CLOCK_ENDPOINT_ADAPTER_CYCLE486_NOTE_2026-07-20.md",
    "Cycle347 runner": ROOT / "scripts/named_record_clock_matcher_refinement_calibration_tournament_synthesis_cycle347_2026_07_18.py",
    "Cycle347 note": ROOT / "docs/work_history/repo/review_feedback/NAMED_RECORD_CLOCK_MATCHER_REFINEMENT_CALIBRATION_TOURNAMENT_SYNTHESIS_CYCLE347_NOTE_2026-07-18.md",
    "Cycle219 runner": Path(c219.__file__),
    "Cycle219 note": c219.NOTE,
    "tick-edge boundary": ROOT / "docs/MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md",
    "scale primitive": ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "kinetic primitive": ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "minimal axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
}


class WallCapExceeded(RuntimeError):
    pass


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def source_and_contract_controls() -> None:
    required = (
        "authority: none", "audit: unset", "exact target contract",
        "route a — causal-front bound-endpoint echo clock",
        "route b — common-history physical refinement",
        "route c — cycle-219 phase/acoustic shortcut control",
        "train lengths 1,2,3", "held lengths 4,6",
        "unary corridor encoding", "decoder ast", "no host divisibility oracle",
        "front speed 1 edge/update", "acoustic group speed 1/sqrt(3)",
        "neither is identified with physical c", "candidate form",
        "not a framework record", "supplied / derived / open",
        "all 24 proper-cubic frames", "gate disposition: fail",
        "moving/lapse/proper-time comparator remains live",
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    check("the Cycle498 note freezes the counter-free target and semantic firewalls", not missing, missing)
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check("all Cycle444/486/347/219 and current far-shore inputs are hash frozen", observed == FROZEN, observed)

    boundary = normalized(FROZEN_PATHS["tick-edge boundary"])
    scale = normalized(FROZEN_PATHS["scale primitive"])
    kinetic = normalized(FROZEN_PATHS["kinetic primitive"])
    axioms = normalized(FROZEN_PATHS["minimal axioms"])
    check(
        "the current source boundary and approved primitives are used only at their registered scope",
        "introduced as the row's naming convention" in boundary
        and "may not be cited as a retained derivation" in boundary
        and "units conversion, not a physics axiom" in scale
        and "not a new dynamics" in kinetic
        and "it does not supply the absolute scale" in kinetic
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "define a time metric" in axioms
        and "formation rules" in axioms,
        {
            "tick_edge": "finite reachability/renaming only",
            "scale": "units conversion only",
            "kinetic_isotropy": "OS0 form only",
            "Record": "formation/lock/permanence/readout; no formation rule or time metric",
        },
    )


def bits(value: int, width: int) -> Word:
    return c444.bits(value, width)


def integer(word: Word) -> int:
    return c444.integer(word)


@dataclass(frozen=True)
class EchoGate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class EchoCodeState:
    length: int
    start_position: int
    rails: Word
    reflector: int
    clock: Word
    geometry: Word


@dataclass(frozen=True)
class EchoApparatus:
    length: int
    schedule: tuple[EchoGate, ...]
    unary_corridor: Word


def unary_geometry(length: int) -> Word:
    if length not in range(1, GEOMETRY_BITS + 1):
        raise ValueError("echo corridor leaves the frozen unary geometry domain")
    return (1,) * length + (0,) * (GEOMETRY_BITS - length)


def decode_unary_geometry(word: Word) -> int:
    if len(word) != GEOMETRY_BITS or any(bit not in (0, 1) for bit in word):
        raise ValueError("geometry word leaves its binary domain")
    length = sum(word)
    if word != (1,) * length + (0,) * (GEOMETRY_BITS - length) or length < 1:
        raise ValueError("geometry word is not a local unary corridor")
    return length


def validate_echo(state: EchoCodeState) -> None:
    if (
        state.length not in range(1, GEOMETRY_BITS + 1)
        or len(state.rails) != state.length + 2
        or sum(state.rails) != 1
        or state.reflector not in (0, 1)
        or any(bit not in (0, 1) for bit in state.rails)
        or decode_unary_geometry(state.geometry) != state.length
    ):
        raise ValueError("echo state leaves the declared code")
    position = c444.clock_position(state.clock)
    if position != state.start_position and not 0 <= position < CLOCK_BITS:
        raise ValueError("echo clock position leaves its word")


def encode_echo(length: int, start_position: int) -> EchoCodeState:
    if start_position + 2 * length >= CLOCK_BITS:
        raise ValueError("echo fixture would wrap the complete clock word")
    state = EchoCodeState(
        length,
        start_position,
        (1,) + (0,) * (length + 1),
        0,
        c444.one_hot(start_position),
        unary_geometry(length),
    )
    validate_echo(state)
    return state


@lru_cache(maxsize=None)
def echo_schedule(length: int) -> tuple[EchoGate, ...]:
    unary_geometry(length)
    output: list[EchoGate] = []

    def clock_sweep(prefix: str) -> None:
        for index, pair in enumerate(c444.CLOCK_FORWARD_SWAPS):
            output.append(EchoGate("clock-swap", pair, f"{prefix}:clock-swap:{index}"))

    for edge in range(length):
        output.append(EchoGate("rail-swap", (edge, edge + 1), f"out:{edge}:rail-swap"))
        clock_sweep(f"out:{edge}")
    output.append(EchoGate("reflect", (length,), "far:reflection-certificate"))
    for edge in reversed(range(length)):
        output.append(EchoGate("rail-swap", (edge, edge + 1), f"return:{edge}:rail-swap"))
        clock_sweep(f"return:{edge}")
    output.append(EchoGate("rail-swap", (0, length + 1), "detector:absorption-swap"))
    return tuple(output)


@lru_cache(maxsize=None)
def echo_apparatus(length: int) -> EchoApparatus:
    """Freeze the law word before any encoded state is presented."""
    return EchoApparatus(length, echo_schedule(length), unary_geometry(length))


def apply_echo_gate(state: EchoCodeState, gate: EchoGate) -> EchoCodeState:
    rails = list(state.rails)
    reflector = state.reflector
    clock = list(state.clock)
    first = gate.sites[0]
    if gate.kind == "rail-swap":
        second = gate.sites[1]
        rails[first], rails[second] = rails[second], rails[first]
    elif gate.kind == "clock-swap":
        second = gate.sites[1]
        clock[first], clock[second] = clock[second], clock[first]
    elif gate.kind == "reflect":
        reflector ^= rails[first]
    else:
        raise ValueError("unknown echo primitive")
    return replace(state, rails=tuple(rails), reflector=reflector, clock=tuple(clock))


def physical_echo(
    state: EchoCodeState,
    apparatus: EchoApparatus,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> EchoCodeState:
    """Apply one declared fixed gate word; state never selects the schedule."""
    validate_echo(state)
    if state.length != apparatus.length or state.geometry != apparatus.unary_corridor:
        raise ValueError("encoded echo state does not match the frozen apparatus")
    schedule = apparatus.schedule
    if delete_label is not None:
        selected = tuple(gate for gate in schedule if gate.label != delete_label)
        if len(selected) != len(schedule) - 1:
            raise ValueError("echo deletion label is absent or nonunique")
        schedule = selected
    output = state
    for gate in reversed(schedule) if reverse else schedule:
        output = apply_echo_gate(output, gate)
    validate_echo(output)
    return output


def coarse_echo(state: EchoCodeState) -> EchoCodeState:
    """Independent encoded-state/geometry evaluator; no physical schedule call."""
    validate_echo(state)
    length = decode_unary_geometry(state.geometry)
    start = c444.clock_position(state.clock)
    if start + 2 * length >= CLOCK_BITS or state.reflector or state.rails[0] != 1:
        raise ValueError("coarse echo input is outside the launch code")
    return replace(
        state,
        rails=(0,) * (length + 1) + (1,),
        reflector=1,
        clock=c444.one_hot(start + 2 * length),
    )


@dataclass(frozen=True)
class BoundClockPair:
    start: c444.Endpoint
    end: c444.Endpoint
    geometry: Word
    formation_law_supplied: bool
    framework_Record: bool = False


@dataclass(frozen=True)
class ClockMap:
    start_identity: int
    end_identity: int
    endpoint_delta_K: int
    encoded_directed_edges: int
    clock_cells_per_directed_edge: Fraction


def bind_endpoints(
    initial: EchoCodeState,
    output: EchoCodeState,
    *,
    formation_enabled: bool = True,
    predecessor_enabled: bool = True,
    delete_latch: bool = False,
) -> BoundClockPair | None:
    start_latch = c444.apply_latch(
        c444.blank_latch(1, initial.clock, bits(1, c444.EVENT_BITS))
    )
    end_latch = c444.apply_latch(
        c444.blank_latch(output.rails[-1], output.clock, bits(2, c444.EVENT_BITS)),
        deleted_gate="valid-copy" if delete_latch else None,
    )
    start = c444.form_endpoint(
        latch=start_latch,
        site=(0, 0, 0),
        predecessors=(),
        formation_enabled=formation_enabled,
    )
    end = c444.form_endpoint(
        latch=end_latch,
        site=(0, 0, 1),
        predecessors=() if start is None or not predecessor_enabled else (start.record,),
        formation_enabled=formation_enabled,
        event_record_edge=bool(output.reflector),
    )
    if start is None or end is None:
        return None
    return BoundClockPair(start, end, initial.geometry, formation_enabled)


def decode_clock_map(pair: BoundClockPair | None) -> ClockMap | None:
    """Read only endpoint payloads, lineage/coincidence, and unary geometry."""
    if pair is None or pair.framework_Record or not pair.formation_law_supplied:
        return None
    interval = c444.match_interval(pair.start, pair.end)
    if interval is None:
        return None
    try:
        length = decode_unary_geometry(pair.geometry)
    except ValueError:
        return None
    directed_edges = 2 * length
    if interval.fine_cells != directed_edges:
        return None
    return ClockMap(
        interval.start_identity,
        interval.end_identity,
        interval.fine_cells,
        directed_edges,
        Fraction(interval.fine_cells, directed_edges),
    )


@dataclass(frozen=True)
class EchoTrace:
    length: int
    unary_geometry_M2: int
    echo_and_clock_M2: int
    fixed_primitives: int
    maximum_gate_support_M2: int
    schedule_reads_state: bool
    sha256: str


@lru_cache(maxsize=None)
def echo_trace(length: int) -> EchoTrace:
    apparatus = echo_apparatus(length)
    schedule = apparatus.schedule
    digest = sha256()
    for gate in schedule:
        digest.update(f"{gate.kind}|{gate.sites}|{gate.label}\n".encode())
    schedule_source = inspect.getsource(echo_schedule).lower()
    state_selected = "state." in schedule_source or "clock_position" in schedule_source
    return EchoTrace(
        length,
        GEOMETRY_BITS,
        length + 2 + 1 + CLOCK_BITS + GEOMETRY_BITS,
        len(schedule) + 2 * len(c444.LATCH_SCHEDULE),
        3,
        state_selected,
        digest.hexdigest(),
    )


def decoder_ast_audit(function: object) -> dict[str, int]:
    source = inspect.getsource(function)
    tree = ast.parse(source)
    names = tuple(node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name))
    attrs = tuple(node.attr.lower() for node in ast.walk(tree) if isinstance(node, ast.Attribute))
    joined = names + attrs
    return {needle: sum(needle in item for item in joined) for needle in ("update", "layer", "depth", "phase", "counter")}


def route_a_controls() -> dict[str, object]:
    print("\nROUTE A / CAUSAL-FRONT BOUND-ENDPOINT ECHO CLOCK")
    thresholds = {
        "train_lengths": A_TRAIN_LENGTHS,
        "held_lengths": A_HELD_LENGTHS,
        "target_cells_per_directed_edge": str(TARGET_CLOCK_CELLS_PER_DIRECTED_EDGE),
        "maximum_endpoint_K": max(2 * length for length in A_HELD_LENGTHS),
    }
    print("FROZEN BEFORE HELD", thresholds)
    rows = []
    fixtures: dict[int, tuple[EchoCodeState, EchoCodeState, BoundClockPair]] = {}
    failures = 0
    for lane, lengths in (("train", A_TRAIN_LENGTHS), ("held", A_HELD_LENGTHS)):
        for length in lengths:
            initial = encode_echo(length, 0)
            apparatus = echo_apparatus(length)
            physical = physical_echo(initial, apparatus)
            coarse = coarse_echo(initial)
            inverse = physical_echo(physical, apparatus, reverse=True)
            pair = bind_endpoints(initial, physical)
            decoded = decode_clock_map(pair)
            failures += int(
                physical != coarse
                or inverse != initial
                or decoded is None
                or decoded.clock_cells_per_directed_edge != TARGET_CLOCK_CELLS_PER_DIRECTED_EDGE
            )
            assert pair is not None
            fixtures[length] = (initial, physical, pair)
            rows.append({
                "lane": lane,
                "length": length,
                "unary_corridor": initial.geometry,
                "start_endpoint_word": pair.start.record.content,
                "end_endpoint_word": pair.end.record.content,
                "E_G_residual": int(physical != coarse),
                "inverse_exact": inverse == initial,
                "decoded": decoded,
                "trace": echo_trace(length),
            })

    # Preserve the exact existing Cycle444 endpoint payload on its direct
    # ell=1/2 domain while extending the same local mechanism through ell=6.
    seam_failures = 0
    for length in (1, 2):
        old_start, old_end = c444.endpoint_pair(length=length, start_position=0)
        _initial, _output, pair = fixtures[length]
        seam_failures += int(
            pair.start.record.content != old_start.record.content
            or pair.end.record.content != old_end.record.content
        )

    decoder_audit = decoder_ast_audit(decode_clock_map)
    physical_source = inspect.getsource(physical_echo).lower()
    physical_schedule_audit = {
        "echo_schedule_calls": physical_source.count("echo_schedule("),
        "state_index_calls": physical_source.count(".index("),
        "apparatus_schedule_bindings": physical_source.count("schedule = apparatus.schedule"),
    }
    check(
        "A: literal unary-corridor fixed schedules derive a dimensionless endpoint clock map through held ell=6 without a host counter",
        failures == seam_failures == 0
        and all(value == 0 for value in decoder_audit.values())
        and physical_schedule_audit == {
            "echo_schedule_calls": 0,
            "state_index_calls": 0,
            "apparatus_schedule_bindings": 1,
        }
        and all(not row["trace"].schedule_reads_state for row in rows),
        {
            "frozen_thresholds": thresholds,
            "rows": rows,
            "Cycle444_ell1_ell2_payload_seam_failures": seam_failures,
            "decoder_AST_forbidden_name_hits": decoder_audit,
            "physical_schedule_authority_audit": physical_schedule_audit,
            "readout_inputs": "two complete endpoint words + lineage/coincidence + unary spatial geometry",
            "candidate_FORM_conditional": True,
            "framework_Record_claimed": False,
        },
    )
    return {"rows": rows, "fixtures": fixtures}


@dataclass(frozen=True)
class RefinementState:
    endpoint_payload: Word
    predecessor_identity: Word
    k2_word: Word
    k3_word: Word
    identity_copy: Word
    predecessor_copy: Word


@dataclass(frozen=True)
class RefineGate:
    source_field: str
    source: int
    target_field: str
    target: int
    label: str


def validate_refinement(state: RefinementState, *, require_blank: bool = False) -> None:
    c444.clock_position(state.endpoint_payload[:CLOCK_BITS])
    if (
        len(state.endpoint_payload) != c444.PAYLOAD_BITS
        or len(state.predecessor_identity) != c444.EVENT_BITS
        or len(state.k2_word) != CLOCK_BITS // 2
        or len(state.k3_word) != (CLOCK_BITS + 2) // 3
        or len(state.identity_copy) != c444.EVENT_BITS
        or len(state.predecessor_copy) != c444.EVENT_BITS
        or any(bit not in (0, 1) for word in (
            state.endpoint_payload, state.predecessor_identity, state.k2_word,
            state.k3_word, state.identity_copy, state.predecessor_copy,
        ) for bit in word)
    ):
        raise ValueError("refinement state leaves its typed word domain")
    if require_blank and any(state.k2_word + state.k3_word + state.identity_copy + state.predecessor_copy):
        raise ValueError("refinement outputs must enter blank")


def refinement_initial(endpoint: c444.Endpoint, predecessor_identity: int) -> RefinementState:
    if not endpoint.record.typed or not endpoint.record.permanent:
        raise ValueError("refinement endpoint is not a typed permanent candidate")
    state = RefinementState(
        endpoint.record.content,
        bits(predecessor_identity, c444.EVENT_BITS),
        (0,) * (CLOCK_BITS // 2),
        (0,) * ((CLOCK_BITS + 2) // 3),
        (0,) * c444.EVENT_BITS,
        (0,) * c444.EVENT_BITS,
    )
    validate_refinement(state, require_blank=True)
    return state


@lru_cache(maxsize=1)
def refinement_schedule() -> tuple[RefineGate, ...]:
    gates: list[RefineGate] = []
    for source in range(CLOCK_BITS):
        gates.append(RefineGate("endpoint_payload", source, "k2_word", source // 2, f"fine-to-k2:{source}"))
        gates.append(RefineGate("endpoint_payload", source, "k3_word", source // 3, f"fine-to-k3:{source}"))
    for lane in range(c444.EVENT_BITS):
        gates.append(RefineGate("endpoint_payload", CLOCK_BITS + lane, "identity_copy", lane, f"identity-copy:{lane}"))
        gates.append(RefineGate("predecessor_identity", lane, "predecessor_copy", lane, f"predecessor-copy:{lane}"))
    return tuple(gates)


def apply_refine_gate(state: RefinementState, gate: RefineGate) -> RefinementState:
    fields = {
        "endpoint_payload": list(state.endpoint_payload),
        "predecessor_identity": list(state.predecessor_identity),
        "k2_word": list(state.k2_word),
        "k3_word": list(state.k3_word),
        "identity_copy": list(state.identity_copy),
        "predecessor_copy": list(state.predecessor_copy),
    }
    fields[gate.target_field][gate.target] ^= fields[gate.source_field][gate.source]
    return RefinementState(**{name: tuple(word) for name, word in fields.items()})


def physical_refinement(
    state: RefinementState,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> RefinementState:
    validate_refinement(state, require_blank=not reverse)
    schedule = refinement_schedule()
    if delete_label is not None:
        selected = tuple(gate for gate in schedule if gate.label != delete_label)
        if len(selected) != len(schedule) - 1:
            raise ValueError("refinement deletion label is absent or nonunique")
        schedule = selected
    output = state
    for gate in reversed(schedule) if reverse else schedule:
        output = apply_refine_gate(output, gate)
    validate_refinement(output)
    return output


def flatten_refinement(state: RefinementState) -> Word:
    validate_refinement(state)
    return (
        state.endpoint_payload
        + state.predecessor_identity
        + state.k2_word
        + state.k3_word
        + state.identity_copy
        + state.predecessor_copy
    )


def unflatten_refinement(word: Word) -> RefinementState:
    _offsets, total = refinement_offsets()
    if len(word) != total or any(bit not in (0, 1) for bit in word):
        raise ValueError("flattened refinement word leaves its 56-M2 domain")
    widths = (c444.PAYLOAD_BITS, c444.EVENT_BITS, CLOCK_BITS // 2, (CLOCK_BITS + 2) // 3, 4, 4)
    fields = []
    cursor = 0
    for width in widths:
        fields.append(word[cursor : cursor + width])
        cursor += width
    state = RefinementState(*fields)
    validate_refinement(state)
    return state


def physical_refinement_nn(
    state: RefinementState,
    *,
    reverse: bool = False,
    delete_logical_label: str | None = None,
) -> RefinementState:
    """Execute the literal restored-line 56-M2 nearest-neighbour manifest."""
    validate_refinement(state, require_blank=not reverse)
    manifest = refinement_nn_manifest()
    if delete_logical_label is not None:
        selected = tuple(
            item for item in manifest
            if not (item[1] == delete_logical_label or item[1].startswith(delete_logical_label + ":"))
        )
        if len(selected) == len(manifest):
            raise ValueError("NN refinement logical deletion block is absent")
        manifest = selected
    bits_line = list(flatten_refinement(state))
    for kind, _label, support in reversed(manifest) if reverse else manifest:
        if kind != "CNOT" or len(support) != 2:
            raise ValueError("NN refinement manifest contains a non-CNOT primitive")
        source, target = support[0][0], support[1][0]
        if abs(source - target) != 1:
            raise ValueError("NN refinement manifest contains a nonlocal primitive")
        bits_line[target] ^= bits_line[source]
    output = unflatten_refinement(tuple(bits_line))
    validate_refinement(output)
    return output


def coarse_refinement(state: RefinementState) -> RefinementState:
    """Direct endpoint-word formula; consumes no path length or step oracle."""
    validate_refinement(state, require_blank=True)
    fine = state.endpoint_payload[:CLOCK_BITS]
    k2 = tuple(sum(fine[2 * index : 2 * index + 2]) for index in range(CLOCK_BITS // 2))
    k3 = tuple(sum(fine[3 * index : min(3 * index + 3, CLOCK_BITS)]) for index in range((CLOCK_BITS + 2) // 3))
    return replace(
        state,
        k2_word=k2,
        k3_word=k3,
        identity_copy=state.endpoint_payload[CLOCK_BITS : CLOCK_BITS + c444.EVENT_BITS],
        predecessor_copy=state.predecessor_identity,
    )


@dataclass(frozen=True)
class RefinementInterval:
    fine: int
    k2: int
    k3: int
    fine_per_k2: Fraction
    fine_per_k3: Fraction


def decode_refinement_interval(
    start: RefinementState,
    end: RefinementState,
    lineage: tuple[RefinementState, ...] = (),
) -> RefinementInterval | None:
    """Read only two encoded endpoint/lineage words; no divisibility oracle."""
    try:
        start_fine = c444.clock_position(start.endpoint_payload[:CLOCK_BITS])
        end_fine = c444.clock_position(end.endpoint_payload[:CLOCK_BITS])
        start_k2 = c444.clock_position(start.k2_word + (0,) * (CLOCK_BITS - len(start.k2_word)))
        end_k2 = c444.clock_position(end.k2_word + (0,) * (CLOCK_BITS - len(end.k2_word)))
        start_k3 = c444.clock_position(start.k3_word + (0,) * (CLOCK_BITS - len(start.k3_word)))
        end_k3 = c444.clock_position(end.k3_word + (0,) * (CLOCK_BITS - len(end.k3_word)))
    except ValueError:
        return None
    start_identity = integer(start.identity_copy)
    end_identity = integer(end.identity_copy)
    chain = (start,) + lineage + (end,)
    lineage_ok = all(
        integer(right.predecessor_copy) == integer(left.identity_copy)
        for left, right in zip(chain[:-1], chain[1:])
    )
    if (
        start_identity == 0
        or end_identity == 0
        or start_identity == end_identity
        or not lineage_ok
        or start.endpoint_payload[20:] != end.endpoint_payload[20:]
        or not (start_fine < end_fine and start_k2 < end_k2 and start_k3 < end_k3)
    ):
        return None
    fine, k2, k3 = end_fine - start_fine, end_k2 - start_k2, end_k3 - start_k3
    return RefinementInterval(fine, k2, k3, Fraction(fine, k2), Fraction(fine, k3))


def make_candidate_endpoint(position: int, identity: int, previous: c444.Endpoint | None) -> c444.Endpoint:
    latch = c444.apply_latch(c444.blank_latch(1, c444.one_hot(position), bits(identity, c444.EVENT_BITS)))
    endpoint = c444.form_endpoint(
        latch=latch,
        site=(1, 0, identity),
        predecessors=() if previous is None else (previous.record,),
    )
    if endpoint is None:
        raise RuntimeError("candidate refinement endpoint did not form")
    return endpoint


def refinement_trace() -> dict[str, object]:
    gates = refinement_schedule()
    # Logical fields are placed consecutively on one bounded line.  Each CNOT
    # is compiled by deterministic restored adjacent SWAP routing.
    widths = (c444.PAYLOAD_BITS, c444.EVENT_BITS, CLOCK_BITS // 2, (CLOCK_BITS + 2) // 3, 4, 4)
    total = sum(widths)
    offsets = {}
    cursor = 0
    for name, width in zip(RefinementState.__dataclass_fields__, widths):
        offsets[name] = cursor
        cursor += width
    digest = sha256()
    nn_primitives = 0
    maximum_span = 0
    for gate in gates:
        source = offsets[gate.source_field] + gate.source
        target = offsets[gate.target_field] + gate.target
        span = abs(target - source)
        maximum_span = max(maximum_span, span)
        # Bring target adjacent, act, and restore: 2(span-1) SWAPs + CNOT.
        nn_primitives += 6 * max(0, span - 1) + 1
        digest.update(f"{source}|{target}|{gate.label}|span={span}\n".encode())
    return {
        "logical_M2": total,
        "fixed_logical_CNOTs": len(gates),
        "restored_line_NN_primitives": nn_primitives,
        "maximum_routing_span": maximum_span,
        "maximum_primitive_support_M2": 2,
        "schedule_reads_state": False,
        "sha256": digest.hexdigest(),
    }


def echo_gate_support(apparatus: EchoApparatus, gate: EchoGate) -> tuple[Coord, ...]:
    def rail(site: int) -> Coord:
        return (-1, 0, 0) if site == apparatus.length + 1 else (site, 0, 0)

    if gate.kind == "rail-swap":
        return tuple(rail(site) for site in gate.sites)
    if gate.kind == "clock-swap":
        return tuple((site, 2, 0) for site in gate.sites)
    if gate.kind == "reflect":
        return (rail(gate.sites[0]), (apparatus.length, 1, 0))
    raise ValueError("unknown echo manifest gate")


def vector_sum(*terms: Coord) -> Coord:
    return tuple(sum(term[index] for term in terms) for index in range(3))


def vector_scale(scale: int, vector: Coord) -> Coord:
    return tuple(scale * value for value in vector)


def carried_echo_gate_support(
    apparatus: EchoApparatus,
    gate: EchoGate,
    *,
    origin: Coord,
    corridor_axis: Coord,
    clock_offset_axis: Coord,
    reflector_offset_axis: Coord,
    detector_side: Coord,
) -> tuple[Coord, ...]:
    """Generate a target-frame support directly from carried apparatus axes."""
    def rail(site: int) -> Coord:
        if site == apparatus.length + 1:
            return vector_sum(origin, detector_side)
        return vector_sum(origin, vector_scale(site, corridor_axis))

    if gate.kind == "rail-swap":
        return tuple(rail(site) for site in gate.sites)
    if gate.kind == "clock-swap":
        clock_origin = vector_sum(origin, vector_scale(2, clock_offset_axis))
        return tuple(vector_sum(clock_origin, vector_scale(site, corridor_axis)) for site in gate.sites)
    if gate.kind == "reflect":
        reflector = vector_sum(
            origin,
            vector_scale(apparatus.length, corridor_axis),
            reflector_offset_axis,
        )
        return (rail(gate.sites[0]), reflector)
    raise ValueError("unknown carried echo manifest gate")


def carried_refinement_support(
    base_support: tuple[Coord, ...],
    *,
    origin: Coord,
    line_axis: Coord,
    offset_axis: Coord,
) -> tuple[Coord, ...]:
    """Generate the target refinement line independently from its basis axes."""
    line_origin = vector_sum(origin, vector_scale(4, offset_axis))
    return tuple(vector_sum(line_origin, vector_scale(site[0], line_axis)) for site in base_support)


def refinement_offsets() -> tuple[dict[str, int], int]:
    widths = (c444.PAYLOAD_BITS, c444.EVENT_BITS, CLOCK_BITS // 2, (CLOCK_BITS + 2) // 3, 4, 4)
    offsets = {}
    cursor = 0
    for name, width in zip(RefinementState.__dataclass_fields__, widths):
        offsets[name] = cursor
        cursor += width
    return offsets, cursor


@lru_cache(maxsize=1)
def refinement_nn_manifest() -> tuple[tuple[str, str, tuple[Coord, ...]], ...]:
    """Literal restored-line CNOT manifest, including routed SWAP CNOTs."""
    offsets, _total = refinement_offsets()
    manifest: list[tuple[str, str, tuple[Coord, ...]]] = []

    def emit_swap(left: int, right: int, label: str) -> None:
        a, b = (left, 4, 0), (right, 4, 0)
        manifest.extend((
            ("CNOT", label + ":swap-cnot-a-b", (a, b)),
            ("CNOT", label + ":swap-cnot-b-a", (b, a)),
            ("CNOT", label + ":swap-cnot-a-b", (a, b)),
        ))

    for gate in refinement_schedule():
        source = offsets[gate.source_field] + gate.source
        target = offsets[gate.target_field] + gate.target
        low, high = sorted((source, target))
        forward_edges = tuple((site, site + 1) for site in reversed(range(low + 1, high)))
        for index, (left, right) in enumerate(forward_edges):
            emit_swap(left, right, f"{gate.label}:route-forward:{index}")
        source_final = low if source == low else low + 1
        target_final = low if target == low else low + 1
        manifest.append((
            "CNOT",
            gate.label + ":act",
            ((source_final, 4, 0), (target_final, 4, 0)),
        ))
        for index, (left, right) in enumerate(reversed(forward_edges)):
            emit_swap(left, right, f"{gate.label}:route-reverse:{index}")
    return tuple(manifest)


def route_b_controls() -> dict[str, object]:
    print("\nROUTE B / COMMON-HISTORY PHYSICAL REFINEMENT")
    thresholds = {
        "train_path_length": B_TRAIN_LENGTH,
        "held_path_length": B_HELD_LENGTH,
        "target_fine_per_k2": str(TARGET_FINE_PER_K2),
        "target_fine_per_k3": str(TARGET_FINE_PER_K3),
    }
    print("FROZEN BEFORE HELD", thresholds)
    endpoints = (
        make_candidate_endpoint(0, 1, None),
        make_candidate_endpoint(6, 2, None),
        make_candidate_endpoint(12, 3, None),
    )
    # Re-form lineage explicitly: midpoint <- start, end <- midpoint.
    endpoints = (
        endpoints[0],
        make_candidate_endpoint(6, 2, endpoints[0]),
        make_candidate_endpoint(12, 3, make_candidate_endpoint(6, 2, endpoints[0])),
    )
    predecessors = (0, 1, 2)
    physical = []
    coarse = []
    inverse_failures = 0
    eg_failures = 0
    logical_nn_failures = 0
    for endpoint, predecessor in zip(endpoints, predecessors):
        initial = refinement_initial(endpoint, predecessor)
        logical = physical_refinement(initial)
        p = physical_refinement_nn(initial)
        q = coarse_refinement(initial)
        physical.append(p)
        coarse.append(q)
        eg_failures += int(p != q)
        logical_nn_failures += int(p != logical)
        inverse_failures += int(physical_refinement_nn(p, reverse=True) != initial)
    train = decode_refinement_interval(physical[0], physical[1])
    held = decode_refinement_interval(physical[0], physical[2], (physical[1],))
    first = train
    second = decode_refinement_interval(physical[1], physical[2])
    whole = held
    additive = (
        first is not None and second is not None and whole is not None
        and tuple(getattr(first, field) + getattr(second, field) for field in ("fine", "k2", "k3"))
        == tuple(getattr(whole, field) for field in ("fine", "k2", "k3"))
    )

    oracle_trees = tuple(ast.parse(inspect.getsource(function)) for function in (coarse_refinement, decode_refinement_interval))
    oracle_names = tuple(
        value
        for tree in oracle_trees
        for node in ast.walk(tree)
        for value in (
            (node.id.lower(),) if isinstance(node, ast.Name)
            else (node.attr.lower(),) if isinstance(node, ast.Attribute)
            else ()
        )
    )
    oracle_hits = {
        token: sum(token in value for value in oracle_names)
        for token in ("divmod", "length", "step", "update", "layer", "depth", "counter")
    }
    oracle_hits["modulo_operator"] = sum(
        isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod)
        for tree in oracle_trees for node in ast.walk(tree)
    )
    check(
        "B: fixed local endpoint codecs give exact fine/k2/k3 train-held ratios and common-history additivity without a divisibility oracle",
        eg_failures == inverse_failures == logical_nn_failures == 0
        and train is not None and held is not None and second is not None
        and train.fine == 2 * B_TRAIN_LENGTH and held.fine == 2 * B_HELD_LENGTH
        and train.fine_per_k2 == held.fine_per_k2 == TARGET_FINE_PER_K2
        and train.fine_per_k3 == held.fine_per_k3 == TARGET_FINE_PER_K3
        and additive
        and all(value == 0 for value in oracle_hits.values()),
        {
            "frozen_thresholds": thresholds,
            "train": train,
            "held": held,
            "split_second": second,
            "additive": additive,
            "E_G_failures": eg_failures,
            "logical_NN_compiler_failures": logical_nn_failures,
            "inverse_failures": inverse_failures,
            "executed_NN_primitives_per_endpoint": len(refinement_nn_manifest()),
            "coarse_decoder_forbidden_oracle_hits": oracle_hits,
            "trace": refinement_trace(),
            "readout_inputs": "encoded fine/k2/k3 endpoint words + event/predecessor lineage + common payload binding",
            "framework_Record_claimed": False,
        },
    )
    return {"physical": tuple(physical), "train": train, "held": held}


def route_c_shortcut_controls() -> dict[str, object]:
    print("\nROUTE C / CYCLE219 PHASE-ACOUSTIC SHORTCUT CONTROL")
    species = c219.common_species(-0.35)
    lifted = c219.c210.cubic_coin(
        pi + 2 * pi,
        species.beta + 2 * pi,
        species.rest_phase + 2 * pi,
    )
    physical_coin_residual = float(np.linalg.norm(lifted - species.coin))
    coordinate_clock_difference = 2 * pi
    front_speed = 1.0
    acoustic_group_speed = sqrt(c219.C_SQUARED)
    source219 = Path(c219.__file__).read_text(encoding="utf-8").lower()
    endpoint_api_absent = all(
        needle not in source219
        for needle in ("def form_endpoint", "def endpoint_payload", "def apply_latch", "framework_record")
    )
    check(
        "C: the direct phase/acoustic shortcut is refused without treating a moving, lapse, or proper-time comparator as impossible",
        physical_coin_residual < TOL
        and coordinate_clock_difference > 6
        and abs(front_speed - acoustic_group_speed) > 0.4
        and endpoint_api_absent,
        {
            "same_physical_coin_after_2pi_coordinate_lift_residual": physical_coin_residual,
            "naive_phase_coordinate_clock_difference": coordinate_clock_difference,
            "front_speed_edges_per_update": front_speed,
            "beta0_acoustic_group_speed": acoustic_group_speed,
            "speed_separation": front_speed - acoustic_group_speed,
            "identified_with_each_other": False,
            "either_identified_with_physical_c": False,
            "Cycle219_endpoint_FORM_latch_API_present": not endpoint_api_absent,
            "disposition": "route-specific shortcut refusal; physical moving/lapse/proper-time comparator remains live",
        },
    )
    return {
        "front_speed": front_speed,
        "acoustic_speed": acoustic_group_speed,
        "shortcut_refused": True,
    }


def deletion_domain_controls(route_a: dict[str, object], route_b: dict[str, object]) -> None:
    print("\nDELETION / MALFORMED / LAWFUL DOMAIN")
    initial, _output, _pair = route_a["fixtures"][3]
    apparatus = echo_apparatus(initial.length)
    deleted = {}
    labels = {
        "transport": "out:0:rail-swap",
        "reflection": "far:reflection-certificate",
        "detector": "detector:absorption-swap",
        "oscillator": "out:0:clock-swap:14",
    }
    for name, label in labels.items():
        damaged = physical_echo(initial, apparatus, delete_label=label)
        deleted[name] = decode_clock_map(bind_endpoints(initial, damaged)) is None
    nominal = physical_echo(initial, apparatus)
    deleted["latch"] = decode_clock_map(bind_endpoints(initial, nominal, delete_latch=True)) is None
    deleted["formation"] = decode_clock_map(bind_endpoints(initial, nominal, formation_enabled=False)) is None
    deleted["predecessor"] = decode_clock_map(bind_endpoints(initial, nominal, predecessor_enabled=False)) is None
    pair = bind_endpoints(initial, nominal)
    assert pair is not None
    broken_geometry = (0,) + pair.geometry[1:]
    deleted["geometry"] = decode_clock_map(replace(pair, geometry=broken_geometry)) is None

    refinement_start = route_b["physical"][0]
    refinement_end = route_b["physical"][1]
    source_position = c444.clock_position(refinement_end.endpoint_payload[:CLOCK_BITS])
    initial_end = physical_refinement_nn(refinement_end, reverse=True)
    damaged_k2 = physical_refinement_nn(initial_end, delete_logical_label=f"fine-to-k2:{source_position}")
    damaged_k3 = physical_refinement_nn(initial_end, delete_logical_label=f"fine-to-k3:{source_position}")
    deleted["k2_codec"] = decode_refinement_interval(refinement_start, damaged_k2) is None
    deleted["k3_codec"] = decode_refinement_interval(refinement_start, damaged_k3) is None
    damaged_pred = physical_refinement_nn(initial_end, delete_logical_label="predecessor-copy:0")
    deleted["lineage"] = decode_refinement_interval(refinement_start, damaged_pred) is None
    nn_manifest = refinement_nn_manifest()
    deleted_block_sizes = {
        label: sum(item[1] == label or item[1].startswith(label + ":") for item in nn_manifest)
        for label in (
            f"fine-to-k2:{source_position}",
            f"fine-to-k3:{source_position}",
            "predecessor-copy:0",
        )
    }

    malformed = 0
    actions = (
        lambda: unary_geometry(0),
        lambda: decode_unary_geometry((1, 0, 1, 0, 0, 0)),
        lambda: encode_echo(6, 4),
        lambda: c444.clock_position((1, 1) + (0,) * 14),
        lambda: refinement_initial(replace(pair.start, record=replace(pair.start.record, typed=False)), 0),
        lambda: physical_echo(initial, apparatus, delete_label="absent"),
        lambda: physical_refinement_nn(initial_end, delete_logical_label="absent"),
    )
    for action in actions:
        try:
            action()
        except ValueError:
            malformed += 1
    check(
        "every route-A/B carrier, endpoint, geometry, codec and lineage deletion is visible and malformed words are refused",
        all(deleted.values()) and all(size > 0 for size in deleted_block_sizes.values())
        and malformed == len(actions),
        {
            "deletions": deleted,
            "removed_NN_block_sizes": deleted_block_sizes,
            "malformed_rejections": malformed,
        },
    )


def rotate(coord: Coord, frame: np.ndarray) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(coord))


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def covariance_resource_controls() -> None:
    print("\nALL24 / LOCALITY / RESOURCE SCALING")
    edges: list[tuple[Coord, Coord]] = []
    for length in A_TRAIN_LENGTHS + A_HELD_LENGTHS:
        corridor = tuple((index, 0, 0) for index in range(length + 1))
        clock = tuple((index, 2, 0) for index in range(CLOCK_BITS))
        edges.extend(zip(corridor[:-1], corridor[1:]))
        edges.append((corridor[-1], (length, 1, 0)))
        edges.append((corridor[0], (-1, 0, 0)))
        edges.extend(zip(clock[:-1], clock[1:]))
    # Route-B restored line is a single finite transported apparatus.
    refinement_m2 = refinement_trace()["logical_M2"]
    edges.extend(((index, 4, 0), (index + 1, 4, 0)) for index in range(refinement_m2 - 1))
    failures = 0
    rows = 0
    manifest_failures = 0
    manifest_rows = 0
    frame_manifest_digests = []
    for frame in c444.FRAMES:
        carried_origin = (0, 0, 0)
        carried_x = rotate((1, 0, 0), frame)
        carried_y = rotate((0, 1, 0), frame)
        carried_detector_side = tuple(-value for value in carried_x)
        for left, right in edges:
            failures += int(manhattan(rotate(left, frame), rotate(right, frame)) != 1)
            rows += 1
        transported = []
        for length in A_TRAIN_LENGTHS + A_HELD_LENGTHS:
            apparatus = echo_apparatus(length)
            for gate in apparatus.schedule:
                base_support = echo_gate_support(apparatus, gate)
                mapped_support = tuple(rotate(site, frame) for site in base_support)
                conjugated = (gate.kind, gate.label, mapped_support)
                expected = (
                    gate.kind,
                    gate.label,
                    carried_echo_gate_support(
                        apparatus,
                        gate,
                        origin=carried_origin,
                        corridor_axis=carried_x,
                        clock_offset_axis=carried_y,
                        reflector_offset_axis=carried_y,
                        detector_side=carried_detector_side,
                    ),
                )
                manifest_failures += int(conjugated != expected)
                manifest_failures += int(any(
                    manhattan(left, right) != 1
                    for left, right in zip(mapped_support[:-1], mapped_support[1:])
                ))
                manifest_rows += 1
                transported.append(conjugated)
        for kind, label, support in refinement_nn_manifest():
            mapped_support = tuple(rotate(site, frame) for site in support)
            conjugated = (kind, label, mapped_support)
            expected = (
                kind,
                label,
                carried_refinement_support(
                    support,
                    origin=carried_origin,
                    line_axis=carried_x,
                    offset_axis=carried_y,
                ),
            )
            manifest_failures += int(conjugated != expected)
            manifest_failures += int(len(mapped_support) != 2 or manhattan(*mapped_support) != 1)
            manifest_rows += 1
            transported.append(conjugated)
        digest = sha256()
        for kind, label, support in transported:
            digest.update(f"{kind}|{label}|{support}\n".encode())
        frame_manifest_digests.append(digest.hexdigest())
    traces = tuple(echo_trace(length) for length in A_TRAIN_LENGTHS + A_HELD_LENGTHS)
    overhead_linear = all(trace.echo_and_clock_M2 == trace.length + 25 for trace in traces)
    check(
        "the complete echo/refinement apparatus is bounded-local and transported through all 24 proper-cubic frames",
        len(c444.FRAMES) == 24
        and failures == 0
        and manifest_failures == 0
        and overhead_linear
        and all(trace.maximum_gate_support_M2 <= 3 for trace in traces)
        and refinement_trace()["maximum_primitive_support_M2"] <= 2
        and len(refinement_nn_manifest()) == refinement_trace()["restored_line_NN_primitives"],
        {
            "proper_cubic_frames": len(c444.FRAMES),
            "transported_edge_rows": rows,
            "failures": failures,
            "transported_gate_manifest_rows": manifest_rows,
            "gate_kind_endpoint_conjugacy_failures": manifest_failures,
            "frame_manifest_sha256": tuple(frame_manifest_digests),
            "echo_traces": traces,
            "refinement_trace": refinement_trace(),
            "literal_refinement_manifest_primitives": len(refinement_nn_manifest()),
            "constant_echo_overhead_beyond_corridor_M2": 25,
            "front_speed_one_edge_per_update_is_resource_label_only": True,
        },
    )


def no_go_controls() -> None:
    print("\nN1-N8 / CLAIM GATE")
    n1 = (
        ("bound-endpoint echo", "ATTEMPTED / POSITIVE", "endpoint+geometry map through ell=6"),
        ("common-history refinement", "ATTEMPTED / POSITIVE", "physical fine/k2/k3 words, ratios/additivity"),
        ("Cycle219 phase/acoustic shortcut", "ATTEMPTED / REFUSED NARROWLY", "phase lift and speed mismatch; no endpoint binding"),
        ("moving light-clock rendezvous", "OPEN / UNTESTED", "could encode launch/reunion and a moving apparatus locally"),
        ("source-conditioned echo lapse", "OPEN / UNTESTED", "could bind two actual endpoint clocks to one local source law"),
        ("matter-band transition clock", "OPEN / UNTESTED", "could derive a repeatable beta-sector transition and endpoint latch"),
        ("Record-causal-depth comparator", "OPEN / UNTESTED", "could compare the same admitted Record lineage to endpoint dK"),
        ("continuum radar/proper-time theorem", "OPEN / UNTESTED", "could prove an operational scaling limit"),
    )
    walls = ("formation/admission", "clock-law selection", "matter-clock binding", "unit/calibration", "continuum/proper-time")
    n2 = tuple((a, b, "no", "no", True) for a, b in combinations(walls, 2))
    n3 = (
        "echo corridor/order", "one oscillator sweep per directed edge", "unary geometry",
        "blank latch/work", "candidate formation rule", "identities/predecessors",
        "fine/k2/k3 codec", "finite nonwrap word", "train/held lengths",
        "target ratios", "proper-cubic placement", "Cycle219 beta and momentum semantics",
    )
    n4 = (
        ("Cycle444", "bounded endpoint dK/calibration", "same endpoint-payload mechanism extended to ell=6", True),
        ("Cycle486", "physical candidate-FORM endpoint binding", "semantic condition only; no framework Record promotion", True),
        ("Cycle347", "conditional same-history ratios without NN compiler", "physical endpoint codec/refinement compiler", True),
        ("Cycle219", "acoustic/matter coin family without clock map", "only shortcut control; no matter-clock conclusion", True),
        ("tick-edge source boundary", "reachability/renaming and scale split", "not used as time derivation", True),
    )
    n5 = (
        ("ell=1..6 bounded echoes", "tested", "positive conditional map"),
        ("fine/k2/k3 positions 0,6,12", "tested", "positive exact ratios/additivity"),
        ("one beta=-0.35 2pi lift and beta0 acoustic speed", "tested", "shortcut only refused"),
        ("arbitrary moving apparatus/source profiles", "untested", "no negative conclusion"),
        ("continuum/lattice-wide actual Records", "untested", "no negative conclusion"),
    )
    n6 = (
        "autonomous FORM/admission law on the bound endpoint word",
        "moving apparatus with locally generated rendezvous endpoints",
        "source-conditioned dual echo with independent physical provenance",
        "matter transition carrier tied to the Cycle219 sector",
        "scale/kinetic primitives used after a dimensionless operational theorem",
        "continuum/refinement theorem with empirical calibration",
    )
    n7 = (
        "A hostile constructive route should start from the positive endpoint and refinement compilers here, place the emitter, mirrors and a beta-sector matter carrier in one reversible moving apparatus, and generate two launch/reunion candidate-FORM endpoints under one local law. A source-conditioned variant could generate a second bound echo and compare only endpoint words. The terminal obligations are local rendezvous, FORM/Record admission, repeatable matter transition, and a scaling theorem; none is excluded by the failed direct phase/acoustic shortcut."
    )
    n8 = (
        "Cycle347 exposed a local compiler route and Cycle498 implements it",
        "Cycle444 replaced depth with physical endpoint words",
        "Cycle486 retired equal-width alias by sidecar/codec construction",
        "source-boundary review demoted tick=edge from derivation to renaming",
        "Cycle219 retained beta selection and no clock binding",
    )
    check(
        "full N1-N8 admits A/B but rejects an impossibility, minimum-content, or axiom-pressure reading of C",
        len(n1) >= 5 and len(n2) == 10 and len(n3) >= 10 and len(n4) == 5
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 250 and len(n8) == 5,
        {
            "N1_normalized_routes": n1,
            "N2_pairwise_wall_audit": n2,
            "N3_hidden_condition_scan": n3,
            "N4_residual_matching": n4,
            "N5_resolution_audit": n5,
            "N6_partial_closure_paths": n6,
            "N7_steelman": n7,
            "N8_cross_cycle_echo": n8,
            "Gate_disposition": "FAIL — partial-attempt-with-live-moving/lapse/proper-time-routes",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN")
    supplied = (
        "Cycle444 fixed echo/latch grammar and conditional endpoint-formation seam",
        "Cycle486 candidate bath-FORM endpoint meaning, without framework Record status",
        "Cycle347 fine/k2/k3 target meanings and identity/predecessor grammar",
        "Cycle219 coin family, selected beta fixture, and beta0 acoustic group speed",
        "finite unary corridors, oscillator-edge pairing, blank words, train/held sizes and ratio thresholds",
        "proper-cubic placement; scale and kinetic primitives only as unused far-shore conversion/form inputs",
    )
    derived = (
        "literal fixed route-A manifests and unary encodings through held ell=6",
        "endpoint-only dK=2ell, exact E/G and inverse, with zero decoder counter names",
        "fixed route-B endpoint codecs, exact E/G/inverse, fine/k2/k3 ratios 2/3 and additivity",
        "no divisibility/length/step oracle in route-B coarse or decoder source",
        "deletion/malformed visibility, bounded resource scaling and all24 transported apparatus",
        "2pi phase shortcut ambiguity and explicit front/acoustic speed separation",
    )
    open_items = (
        "autonomous echo/clock law selection and candidate FORM/Record admission",
        "framework Record identity, actual history and physical permanence implementation",
        "moving matter-clock rendezvous or source-conditioned lapse comparator",
        "Cycle219 matter-sector transition bound to an endpoint clock word",
        "physical-c identification, unit/empirical calibration and arbitrary-epoch renewal",
        "continuum proper time, Lorentz closure, energy/stress/source/gravity and Born history",
    )
    check(
        "the exact inventory separates premises, bounded physical consequences, and live clock/proper-time obligations",
        len(supplied) == len(derived) == len(open_items) == 6,
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "authority": AUTHORITY,
            "audit": AUDIT,
            "candidate_FORM_called_framework_Record": False,
            "front_or_acoustic_speed_called_physical_c": False,
        },
    )


def resource_guard(started: float) -> None:
    elapsed = time.monotonic() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "the cold runner body stays inside its wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and peak < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_rss_bytes": peak, "wall_cap_seconds": WALL_CAP_SECONDS, "rss_cap_bytes": RSS_CAP_BYTES},
    )


def install_wall_cap() -> None:
    def alarm(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle498 exceeded its wall cap")
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(int(WALL_CAP_SECONDS))


def main() -> int:
    started = time.monotonic()
    install_wall_cap()
    print("CYCLE498 PHYSICAL CAUSAL LIGHT CLOCK / RECORD-ENDPOINT CALIBRATION")
    source_and_contract_controls()
    route_a = route_a_controls()
    route_b = route_b_controls()
    route_c_shortcut_controls()
    deletion_domain_controls(route_a, route_b)
    covariance_resource_controls()
    no_go_controls()
    inventory_controls()
    resource_guard(started)
    signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
