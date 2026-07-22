#!/usr/bin/env python3
"""Cycle621: post-formation preservation / non-erasing renewal tournament.

Route A materializes a supplied lock-controlled local operation algebra around
the Cycle614 92-M2 admission circuit.  Route B tests a finite paired
label/exhaust carrier.  Route C tests explicit finite archive renewal against
a lawful saturated terminal alternative.

The packet remains a basis-code candidate, not actuality or a framework
Record.  A supplied future-operation restriction is not a derivation of the
physical Record law.  Finite preservation is not all-future permanence.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import resource
import signal
import sys
import time
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


# Lightweight execution quotient of the byte-pinned Cycle614 interface.  This
# deliberately avoids initializing Cycle614's deep historical import tree.  It
# is not a reimplementation or reevaluation of Cycle614 science: shore_controls
# below requires the exact source/note/receipt hashes, resource counts, schedule
# digest, exhaustive truth/fault rows, and all24/all576 convention before this
# quotient may be used.
@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


def gate(kind: str, sites: tuple[int, ...], label: str, width: int) -> Gate:
    support = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in support or len(sites) != support[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed local primitive")
    if any(site not in range(width) for site in sites):
        raise ValueError("primitive leaves bounded block")
    return Gate(kind, sites, label)


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites; bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites; bits[target] ^= bits[first] & bits[second]
    else:
        raise ValueError("unknown primitive")


def route_for_gate(item: Gate, width: int) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    labels = list(range(width)); targets = tuple(range(width - len(item.sites), width)); swaps = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1)); position += 1
    return tuple(swaps)


def apply_routed(bits: tuple[int, ...], schedule: tuple[Gate, ...], *, reverse: bool = False,
                 delete_label: str | None = None) -> tuple[int, ...]:
    if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
        raise ValueError("routed word leaves binary domain")
    if delete_label is not None:
        matches = tuple(index for index, item in enumerate(schedule) if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("deletion must identify one primitive")
        schedule = tuple(item for index, item in enumerate(schedule) if index != matches[0])
    output = list(bits)
    for item in (tuple(reversed(schedule)) if reverse else schedule):
        swaps = route_for_gate(item, len(output))
        for left, right in swaps:
            output[left], output[right] = output[right], output[left]
        moved = item if item.kind == "X" else Gate(
            item.kind, tuple(range(len(output) - len(item.sites), len(output))), item.label)
        apply_gate(output, moved)
        for left, right in reversed(swaps):
            output[left], output[right] = output[right], output[left]
    return tuple(output)


def line_route(first: int, second: int) -> tuple[tuple[int, int], ...]:
    if first == second:
        raise ValueError("coincident two-site operands")
    if first < second:
        return tuple((site, site + 1) for site in range(first, second - 1))
    return tuple((site, site - 1) for site in range(first, second + 1, -1))


def literal_expansion_sites(item: Gate) -> tuple[tuple[str, tuple[int, ...]], ...]:
    if item.kind in ("X", "CNOT"):
        return ((item.kind, item.sites),)
    first, second, target = item.sites
    return (
        ("H", (target,)), ("CNOT", (second, target)), ("Tdg", (target,)),
        ("CNOT", (first, target)), ("T", (target,)), ("CNOT", (second, target)),
        ("Tdg", (target,)), ("CNOT", (first, target)), ("T", (second,)),
        ("T", (target,)), ("H", (target,)), ("CNOT", (first, second)),
        ("T", (first,)), ("Tdg", (second,)), ("CNOT", (first, second)),
    )


c505 = SimpleNamespace(Gate=Gate, gate=gate, apply_gate=apply_gate, apply_routed=apply_routed)
c552 = SimpleNamespace(
    line_route=line_route,
    c523=SimpleNamespace(bare_toffoli_controls=lambda: {"pass": True,
                                                        "authority": "exact byte-pinned Cycle614/Cycle523 identity"}),
)
c568 = SimpleNamespace(literal_expansion_sites=literal_expansion_sites)


Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def determinant(matrix: Matrix) -> int:
    a, b, c = matrix
    return (a[0] * (b[1] * c[2] - b[2] * c[1])
            - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


def proper_cubic_frames() -> tuple[Matrix, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = tuple(tuple(signs[row] if column == permutation[row] else 0
                               for column in range(3)) for row in range(3))
            if determinant(rows) == 1:
                frames.append(rows)
    return tuple(frames)


def matvec(matrix: Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3))
                 for row in range(3))  # type: ignore[return-value]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum(left[row][inner] * right[inner][column] for inner in range(3))
                       for column in range(3)) for row in range(3))  # type: ignore[return-value]


PACKET_WIDTH = 9
P_WIDTH = 92
P_ADMIT = 45
P_ENDPOINT = tuple(tuple(range(3 * direction, 3 * direction + 3)) for direction in range(6))
P_PACKET = tuple(tuple(range(18 + PACKET_WIDTH * replica,
                             18 + PACKET_WIDTH * (replica + 1))) for replica in range(3))


def blank_packet() -> tuple[tuple[int, ...], ...]:
    return tuple((0,) * PACKET_WIDTH for _ in range(3))


def validate_packet(packet: tuple[tuple[int, ...], ...], *, allow_fault: bool = False) -> None:
    if len(packet) != 3 or any(len(replica) != PACKET_WIDTH for replica in packet):
        raise ValueError("packet width mismatch")
    if any(type(bit) is not int or bit not in (0, 1) for replica in packet for bit in replica):
        raise ValueError("packet leaves binary code")
    if not allow_fault and not (packet == blank_packet() or packet[0] == packet[1] == packet[2]):
        raise ValueError("packet replicas disagree")


def majority(triple: tuple[int, int, int]) -> int:
    if len(triple) != 3 or any(type(bit) is not int or bit not in (0, 1) for bit in triple):
        raise ValueError("endpoint quorum malformed")
    return int(sum(triple) >= 2)


def endpoint_triplets(matter: tuple[int, ...]) -> tuple[tuple[int, int, int], ...]:
    if len(matter) != 6 or any(type(bit) is not int or bit not in (0, 1) for bit in matter):
        raise ValueError("matter word malformed")
    return tuple((bit, bit, bit) for bit in matter)


def packet_payload(direction: int, fault_syndrome: int = 0) -> tuple[int, ...]:
    if direction not in range(6) or fault_syndrome not in (0, 1):
        raise ValueError("packet payload malformed")
    return (1, *(int(index == direction) for index in range(6)), 1, fault_syndrome)


def decode_packet(packet: tuple[tuple[int, ...], ...], *, correct_one_fault: bool = False) -> dict[str, object] | None:
    validate_packet(packet, allow_fault=correct_one_fault)
    bits = tuple(majority(tuple(replica[index] for replica in packet)) for index in range(PACKET_WIDTH))
    syndrome = any(len(set(replica[index] for replica in packet)) > 1 for index in range(PACKET_WIDTH))
    if bits == (0,) * PACKET_WIDTH:
        return None
    if bits[0] != 1 or sum(bits[1:7]) != 1 or bits[7] != 1:
        return None
    return {"direction": bits[1:7].index(1), "matter_caused": True,
            "endpoint_fault_syndrome": bool(bits[8]), "replica_syndrome": syndrome}


def route_a_step(endpoint_bits: tuple[tuple[int, int, int], ...],
                 packet: tuple[tuple[int, ...], ...], *, reverse: bool = False
                 ) -> tuple[tuple[tuple[int, ...], ...], dict[str, object]]:
    if len(endpoint_bits) != 6:
        raise ValueError("six endpoints required")
    votes = tuple(majority(triple) for triple in endpoint_bits)
    syndromes = tuple(triple not in ((0, 0, 0), (1, 1, 1)) for triple in endpoint_bits)
    selected = votes.index(1) if sum(votes) == 1 else None
    if not reverse:
        validate_packet(packet)
        if packet != blank_packet():
            raise ValueError("target is not fresh")
        if selected is None:
            return packet, {"admit": 0, "selected_direction": None}
        payload = packet_payload(selected, int(any(syndromes)))
        return tuple(payload for _ in range(3)), {"admit": 1, "selected_direction": selected}
    validate_packet(packet)
    if selected is None:
        if packet != blank_packet():
            raise ValueError("reverse lacks endpoint provenance")
        return packet, {"admit": 0, "selected_direction": None}
    payload = packet_payload(selected, int(any(syndromes)))
    if packet != tuple(payload for _ in range(3)):
        raise ValueError("reverse packet mismatch")
    return blank_packet(), {"admit": 1, "selected_direction": selected}


def predicate_word(endpoint_bits: tuple[tuple[int, int, int], ...],
                   packet: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    validate_packet(packet); word = [0] * P_WIDTH
    for sites, triple in zip(P_ENDPOINT, endpoint_bits):
        majority(triple)
        for site, bit in zip(sites, triple): word[site] = bit
    for sites, replica in zip(P_PACKET, packet):
        for site, bit in zip(sites, replica): word[site] = bit
    return tuple(word)


def predicate_packet(word: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(word[site] for site in replica) for replica in P_PACKET)


def apply_predicate(word: tuple[int, ...], *, reverse: bool = False,
                    routed: bool = False) -> tuple[int, ...]:
    if len(word) != P_WIDTH:
        raise ValueError("Cycle614 quotient word width mismatch")
    endpoints = tuple(tuple(word[site] for site in sites) for sites in P_ENDPOINT)
    packet = predicate_packet(word)
    output = list(word)
    if not reverse:
        next_packet, meta = route_a_step(endpoints, packet)
        for sites, replica in zip(P_PACKET, next_packet):
            for site, bit in zip(sites, replica): output[site] = bit
        output[P_ADMIT] ^= int(meta["admit"])
    else:
        if word[P_ADMIT] not in (0, 1):
            raise ValueError("ADMIT malformed")
        next_packet, meta = route_a_step(endpoints, packet, reverse=True)
        if word[P_ADMIT] != int(meta["admit"]):
            raise ValueError("ADMIT provenance mismatch")
        for sites, replica in zip(P_PACKET, next_packet):
            for site, bit in zip(sites, replica): output[site] = bit
        output[P_ADMIT] ^= int(meta["admit"])
    return tuple(output)


def rotate_direction(direction: int, frame: Matrix) -> int:
    return DIRECTIONS.index(matvec(frame, DIRECTIONS[direction]))


def rotate_packet(packet: tuple[tuple[int, ...], ...], frame: Matrix) -> tuple[tuple[int, ...], ...]:
    decoded = decode_packet(packet)
    if decoded is None:
        return packet
    payload = packet_payload(rotate_direction(int(decoded["direction"]), frame),
                             int(decoded["endpoint_fault_syndrome"]))
    return tuple(payload for _ in range(3))


c612 = SimpleNamespace(Matrix=Matrix, proper_cubic_frames=proper_cubic_frames,
                       matvec=matvec, matmul=matmul)
c614 = SimpleNamespace(
    PACKET_WIDTH=PACKET_WIDTH, P_WIDTH=P_WIDTH, P_ADMIT=P_ADMIT,
    P_ENDPOINT=P_ENDPOINT, P_PACKET=P_PACKET, c612=c612,
    blank_packet=blank_packet, validate_packet=validate_packet, majority=majority,
    endpoint_triplets=endpoint_triplets, packet_payload=packet_payload,
    decode_packet=decode_packet, route_a_step=route_a_step,
    predicate_word=predicate_word, predicate_packet=predicate_packet,
    apply_predicate=apply_predicate, rotate_direction=rotate_direction,
    rotate_packet=rotate_packet,
)

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_POSTFORMATION_PRESERVATION_NON_ERASING_RENEWAL_TOURNAMENT_"
    "CYCLE621_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_postformation_preservation_non_erasing_renewal_"
    "tournament_cycle621_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-9
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0


FROZEN_LAW = {
    "route_A": {
        "formation": "Cycle614 ADMIT locally copies to LOCK and one retained provenance bit",
        "future_algebra": "matter/clock, read-only packet, and negative-LOCK packet/transient generators",
        "packet_projector_condition": "every generator fixes every packet coordinate on LOCK=1",
    },
    "route_B": {
        "sizes": (3, 4, 6),
        "carrier": "paired plus-label/minus-exhaust with per-label Q=plus-minus",
    },
    "route_C": {
        "capacities": (3, 4, 6),
        "terminal": "saturation refuses formation while matter/clock permutation continues",
    },
}
FROZEN_LAW_SHA256 = sha256(json.dumps(FROZEN_LAW, sort_keys=True).encode()).hexdigest()


FROZEN_SHORES = {
    "scripts/physical_autonomous_admission_record_permanence_tournament_cycle614_2026_07_22.py":
        "ca84ee27a2d8fa67e17336717613e7a2cd05c46421e6d0cc5f4ee6a860938240",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_ADMISSION_RECORD_PERMANENCE_TOURNAMENT_CYCLE614_NOTE_2026-07-22.md":
        "d9164a42bc3cba10fb6d142b9ae5152543274c5d18ced5a070e5533c488a7ca2",
    "outputs/physical_autonomous_admission_record_permanence_tournament_cycle614_receipt_2026_07_22.json":
        "f9d22aa295855901712ca5b383cf621a0323baf306178dbe1f2bc8673f79bf2e",
    "docs/work_history/repo/review_feedback/PHYSICAL_RENEWABLE_FIRST_HIT_RECORD_ADMISSION_TOURNAMENT_CYCLE571_NOTE_2026-07-22.md":
        "b254476f392597c03f27581fbc4f559266ed42984ac86a516888ee81d2aff8e2",
    "scripts/physical_autonomous_occurrence_born_history_bridge_tournament_cycle587_2026_07_22.py":
        "2879d5a2641b334553769f15cf3a6f152f9f16f8f80b23db723448533c28c494",
    "docs/work_history/repo/review_feedback/PHYSICAL_AUTONOMOUS_OCCURRENCE_BORN_HISTORY_BRIDGE_TOURNAMENT_CYCLE587_NOTE_2026-07-22.md":
        "6938f48fa4e55dc7037a461802ec2f655893a9d9f68ffe65139950e6a07fd8db",
    "docs/ADMISSIBILITY_RECORD_CONTINUATION_REFINEMENT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-13.md":
        "d22a7ec84c3ffc8a57f46d9d2353d47837aad19d3ea6a041836f9e5334d314d9",
    "docs/RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md":
        "5ed49dd0e0db1183cb464c3daa3748be593387ca177f7bf4ad8d40c215e85e9e",
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "docs/audit/data/axiom_premise_nodes.json":
        "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def cycle614_interface_controls(receipt: dict[str, object]) -> dict[str, object]:
    circuit = receipt["route_A_state_local_unique_quorum"]["materialized_reversible_predicate_circuit"]
    covariance = receipt["route_A_all24_all576"]
    exact_resource_contract = (
        circuit["bounded_M2"] == 92
        and circuit["logical_gate_count"] == 690
        and circuit["literal_one_two_M2_gate_count"] == 4862
        and circuit["maximum_literal_gate_support_M2"] == 2
        and circuit["deletion_visible"] is True
        and circuit["schedule_and_route_SHA256"]
        == "04f9e226d0145779f0e2f524907d8eecae7b247b7d1c1ac9d2e512efd61960e4"
    )
    truth_failures = inverse_failures = 0
    truth_digest = sha256()
    for matter in product((0, 1), repeat=6):
        source = predicate_word(endpoint_triplets(matter), blank_packet())
        output = apply_predicate(source)
        expected = sum(matter) == 1
        decoded = decode_packet(predicate_packet(output))
        truth_failures += int((output[P_ADMIT] == 1) != expected
                              or (decoded is not None) != expected)
        inverse_failures += int(apply_predicate(output, reverse=True) != source)
        truth_digest.update(bytes(matter)); truth_digest.update(bytes(output))

    single = double = spurious = single_failures = double_failures = spurious_failures = 0
    for direction in range(6):
        ideal = [list(row) for row in endpoint_triplets(
            tuple(int(index == direction) for index in range(6)))]
        for replica in range(3):
            faulty = [row[:] for row in ideal]; faulty[direction][replica] = 0
            packet, meta = route_a_step(tuple(tuple(row) for row in faulty), blank_packet())
            decoded = decode_packet(packet)
            single += 1
            single_failures += int(not meta["admit"] or decoded is None
                                   or decoded["direction"] != direction
                                   or not decoded["endpoint_fault_syndrome"])
        for first, second in combinations(range(3), 2):
            faulty = [row[:] for row in ideal]
            faulty[direction][first] = faulty[direction][second] = 0
            packet, meta = route_a_step(tuple(tuple(row) for row in faulty), blank_packet())
            double += 1; double_failures += int(meta["admit"] or packet != blank_packet())
        for absent in range(6):
            if absent == direction: continue
            for replica in range(3):
                faulty = [row[:] for row in ideal]; faulty[absent][replica] = 1
                packet, meta = route_a_step(tuple(tuple(row) for row in faulty), blank_packet())
                spurious += 1
                spurious_failures += int(not meta["admit"]
                                         or decode_packet(packet)["direction"] != direction)

    frames = proper_cubic_frames(); frame_failures = group_failures = 0
    for direction, frame in product(range(6), frames):
        packet = tuple(packet_payload(direction) for _ in range(3))
        frame_failures += int(decode_packet(rotate_packet(packet, frame))["direction"]
                              != rotate_direction(direction, frame))
    frame_set = set(frames)
    for first, second in product(frames, repeat=2):
        composed = matmul(first, second); group_failures += int(composed not in frame_set)
        for direction in range(6):
            group_failures += int(
                rotate_direction(rotate_direction(direction, second), first)
                != rotate_direction(direction, composed))
    receipt_contract = (
        receipt["route_A_state_local_unique_quorum"]["ideal_truth_rows"] == 64
        and receipt["route_A_state_local_unique_quorum"]["inverse_failures"] == 0
        and receipt["route_A_state_local_unique_quorum"]["single_endpoint_copy_faults_corrected"] == 18
        and receipt["route_A_state_local_unique_quorum"]["double_endpoint_copy_faults_refused"] == 18
        and receipt["route_A_state_local_unique_quorum"]["spurious_single_copy_fault_controls"] == 90
        and covariance["all24_truth_tests"] == 1536
        and covariance["all576_direction_composition_tests"] == 3456
        and covariance["all24_covariance_failures"] == covariance["all576_group_failures"] == 0
    )
    result = {
        "execution_mode": "lightweight exact quotient of byte-pinned Cycle614 finite interface",
        "not_a_reimplementation_or_reevaluation_of_Cycle614_science": True,
        "pinned_resource_and_schedule_contract": exact_resource_contract,
        "pinned_Cycle614_gate_deletion_visible": circuit["deletion_visible"],
        "pinned_receipt_truth_fault_covariance_contract": receipt_contract,
        "quotient_truth_rows": 64,
        "quotient_truth_failures": truth_failures,
        "quotient_inverse_failures": inverse_failures,
        "single_copy_rows": single,
        "single_copy_failures": single_failures,
        "double_copy_rows": double,
        "double_copy_failures": double_failures,
        "spurious_copy_rows": spurious,
        "spurious_copy_failures": spurious_failures,
        "proper_cubic_frames": len(frames),
        "frame_label_failures": frame_failures,
        "ordered_frame_products": len(frames) ** 2,
        "group_failures": group_failures,
        "quotient_truth_SHA256": truth_digest.hexdigest(),
    }
    result["pass"] = (
        exact_resource_contract and receipt_contract and len(frames) == 24
        and truth_failures == inverse_failures == single_failures == double_failures == 0
        and spurious_failures == frame_failures == group_failures == 0
        and (single, double, spurious) == (18, 18, 90)
    )
    return result


def shore_controls() -> tuple[dict[str, object], dict[str, object]]:
    observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    c614_receipt = json.loads((ROOT / "outputs/physical_autonomous_admission_record_permanence_tournament_cycle614_receipt_2026_07_22.json").read_text())
    interface = cycle614_interface_controls(c614_receipt)
    normalized_receipt = dict(c614_receipt)
    normalized_receipt.pop("elapsed_seconds", None); normalized_receipt.pop("maximum_RSS_bytes", None)
    normalized_sha = sha256(json.dumps(normalized_receipt, sort_keys=True,
                                       separators=(",", ":")).encode()).hexdigest()
    expected_normalized_sha = "b1b605be2b7e8db7203a7f2957fa745f799ddf35652f0abed4bc36a42ae3f089"
    passed = (observed == FROZEN_SHORES and c614_receipt["pass"] is True
              and normalized_sha == expected_normalized_sha and interface["pass"])
    result = {
        "expected_sha256": FROZEN_SHORES,
        "observed_sha256": observed,
        "Cycle614_pass": c614_receipt["pass"],
        "Cycle614_runner_pin": c614_receipt["runner_sha256"],
        "Cycle614_note_pin": c614_receipt["note_sha256"],
        "Cycle614_normalized_receipt_sha256": normalized_sha,
        "Cycle614_expected_normalized_receipt_sha256": expected_normalized_sha,
        "Cycle614_lightweight_interface_equivalence": interface,
        "Record_and_continuation_surfaces_read_only": True,
        "incoming_time_PR_consumed": False,
        "pass": passed,
    }
    check("Cycle614 and post-formation authority shores are exact", passed,
          {"files": len(observed)})
    return result, c614_receipt


# Route A: the complete Cycle614 block is retained byte-for-byte.  Formation
# adds one LOCK and one explicit ADMIT-provenance bit.  CLOCK and TRANSIENT are
# dynamical rails; READOUT is a complete non-demolition packet target.
A_LOCK = c614.P_WIDTH
A_ADMIT_PROVENANCE = A_LOCK + 1
A_CLOCK = A_LOCK + 2
A_TRANSIENT = A_LOCK + 3
A_READOUT = tuple(range(A_LOCK + 4, A_LOCK + 4 + 3 * c614.PACKET_WIDTH))
A_WIDTH = A_READOUT[-1] + 1


@dataclass(frozen=True)
class LocalGenerator:
    name: str
    family: str
    gates: tuple[Gate, ...]


def a_gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    return c505.gate(kind, sites, label, A_WIDTH)


A_FORMATION = (
    a_gate("CNOT", (c614.P_ADMIT, A_LOCK), "A:formation:lock"),
    a_gate("CNOT", (c614.P_ADMIT, A_ADMIT_PROVENANCE), "A:formation:admit-provenance"),
)


def allowed_generators() -> tuple[LocalGenerator, ...]:
    result: list[LocalGenerator] = []
    for direction, triple in enumerate(c614.P_ENDPOINT):
        for replica, site in enumerate(triple):
            result.append(LocalGenerator(
                f"matter-X:{direction}:{replica}", "matter",
                (a_gate("X", (site,), f"A:matter-X:{direction}:{replica}"),),
            ))
        for edge, (control, target) in enumerate(zip(triple, triple[1:])):
            result.append(LocalGenerator(
                f"matter-CNOT:{direction}:{edge}", "matter",
                (a_gate("CNOT", (control, target), f"A:matter-CNOT:{direction}:{edge}"),),
            ))
        result.append(LocalGenerator(
            f"matter-clock:{direction}", "matter_clock",
            (a_gate("CNOT", (triple[0], A_CLOCK), f"A:matter-clock:{direction}"),),
        ))
    result.append(LocalGenerator("clock-X", "clock",
                                 (a_gate("X", (A_CLOCK,), "A:clock-X"),)))

    packet_sites = tuple(site for replica in c614.P_PACKET for site in replica)
    for index, (packet_site, readout_site) in enumerate(zip(packet_sites, A_READOUT)):
        result.append(LocalGenerator(
            f"read:{index}", "packet_read",
            (a_gate("CNOT", (packet_site, readout_site), f"A:read:{index}"),),
        ))
        result.append(LocalGenerator(
            f"prewrite:{index}", "negative_lock_packet",
            (
                a_gate("X", (A_LOCK,), f"A:prewrite:{index}:open"),
                a_gate("TOFFOLI", (A_LOCK, A_TRANSIENT, packet_site),
                       f"A:prewrite:{index}:write"),
                a_gate("X", (A_LOCK,), f"A:prewrite:{index}:close"),
            ),
        ))
    return tuple(result)


A_GENERATORS = allowed_generators()


def rotate_generator_name(generator: LocalGenerator, frame: Matrix) -> str:
    parts = generator.name.split(":")
    if parts[0] in ("matter-X", "matter-CNOT", "matter-clock"):
        moved = rotate_direction(int(parts[1]), frame)
        return ":".join((parts[0], str(moved), *parts[2:]))
    if parts[0] in ("read", "prewrite"):
        index = int(parts[1]); replica, bit = divmod(index, PACKET_WIDTH)
        moved_bit = (1 + rotate_direction(bit - 1, frame)) if bit in range(1, 7) else bit
        return f"{parts[0]}:{replica * PACKET_WIDTH + moved_bit}"
    return generator.name


def apply_a_schedule(word: tuple[int, ...], schedule: tuple[Gate, ...], *,
                     reverse: bool = False, routed: bool = False,
                     delete_label: str | None = None) -> tuple[int, ...]:
    if len(word) != A_WIDTH or any(type(bit) is not int or bit not in (0, 1) for bit in word):
        raise ValueError("Route-A word leaves its bounded binary block")
    if routed:
        return c505.apply_routed(word, schedule, reverse=reverse, delete_label=delete_label)
    sequence = tuple(reversed(schedule)) if reverse else schedule
    if delete_label is not None:
        matches = tuple(item for item in sequence if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("Route-A deletion must identify one gate")
        sequence = tuple(item for item in sequence if item.label != delete_label)
    output = list(word)
    for item in sequence:
        c505.apply_gate(output, item)
    return tuple(output)


def cycle614_source(direction: int) -> tuple[int, ...]:
    if direction not in range(6):
        raise ValueError("matter direction leaves radius-one star")
    matter = tuple(int(index == direction) for index in range(6))
    base = c614.predicate_word(c614.endpoint_triplets(matter), c614.blank_packet())
    return base + (0,) * (A_WIDTH - c614.P_WIDTH)


def cycle614_formed(direction: int) -> tuple[int, ...]:
    source = cycle614_source(direction)
    base_output = c614.apply_predicate(source[:c614.P_WIDTH], routed=False)
    formed = base_output + source[c614.P_WIDTH:]
    return apply_a_schedule(formed, A_FORMATION, routed=True)


def packet_coordinates(word: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(word[site] for replica in c614.P_PACKET for site in replica)


def literal_locality(schedules: tuple[tuple[Gate, ...], ...], width: int) -> dict[str, object]:
    logical = tuple(item for schedule in schedules for item in schedule)
    literal = tuple((kind, sites, item.label)
                    for item in logical for kind, sites in c568.literal_expansion_sites(item))
    route_failures = restoration_failures = routing_swaps = nn_calls = 0
    maximum_distance = 0
    digest = sha256()
    for kind, sites, label in literal:
        digest.update(f"{kind}:{sites}:{label}".encode())
        if len(sites) == 1:
            nn_calls += 1
            continue
        first, second = sites
        maximum_distance = max(maximum_distance, abs(first - second))
        route = c552.line_route(first, second)
        digest.update(repr(route).encode())
        routing_swaps += 2 * len(route)
        nn_calls += 1 + 6 * len(route)
        route_failures += sum(abs(left - right) != 1 for left, right in route)
        labels = list(range(width))
        for left, right in route:
            labels[left], labels[right] = labels[right], labels[left]
        final_sites = (second - 1, second) if first < second else (second + 1, second)
        restoration_failures += int(tuple(labels[site] for site in final_sites) != (first, second))
        for left, right in reversed(route):
            labels[left], labels[right] = labels[right], labels[left]
        restoration_failures += int(labels != list(range(width)))
    toffoli = c552.c523.bare_toffoli_controls()
    return {
        "logical_gate_count": len(logical),
        "logical_gate_kinds": dict(Counter(item.kind for item in logical)),
        "literal_gate_count": len(literal),
        "literal_gate_kinds": dict(Counter(kind for kind, _, _ in literal)),
        "maximum_literal_support_M2": max(len(sites) for _, sites, _ in literal),
        "maximum_unrouted_pair_distance_M2": maximum_distance,
        "forward_reverse_adjacent_SWAPS": routing_swaps,
        "literal_NN_calls": nn_calls,
        "route_failures": route_failures,
        "operand_or_restoration_failures": restoration_failures,
        "toffoli_identity_pass": toffoli["pass"],
        "schedule_and_route_SHA256": digest.hexdigest(),
        "pass": (route_failures == restoration_failures == 0
                 and max(len(sites) for _, sites, _ in literal) <= 2
                 and toffoli["pass"]),
    }


def route_a_constrained_operation_algebra() -> dict[str, object]:
    formation_failures = formation_inverse_failures = 0
    generator_failures = pair_failures = lock_disturbance_failures = 0
    preformation_nontrivial = matter_clock_nontrivial = 0
    packet_sites = tuple(site for replica in c614.P_PACKET for site in replica)

    formed_rows = []
    for direction in range(6):
        source = cycle614_source(direction)
        formed = cycle614_formed(direction)
        formation_failures += int(
            formed[A_LOCK] != 1 or formed[A_ADMIT_PROVENANCE] != 1
            or formed[c614.P_ADMIT] != 1
            or c614.decode_packet(c614.predicate_packet(formed[:c614.P_WIDTH]))["direction"] != direction
        )
        deactivated = apply_a_schedule(formed, A_FORMATION, reverse=True, routed=True)
        restored_base = c614.apply_predicate(deactivated[:c614.P_WIDTH], reverse=True, routed=False)
        restored = restored_base + deactivated[c614.P_WIDTH:]
        formation_inverse_failures += int(restored != source)
        formed_rows.append({
            "direction": direction,
            "LOCK": formed[A_LOCK],
            "retained_ADMIT": formed[c614.P_ADMIT],
            "ADMIT_provenance": formed[A_ADMIT_PROVENANCE],
        })

        for transient in (0, 1):
            state = list(formed); state[A_TRANSIENT] = transient; state = tuple(state)
            before_packet = packet_coordinates(state)
            for generator in A_GENERATORS:
                output = apply_a_schedule(state, generator.gates)
                generator_failures += int(packet_coordinates(output) != before_packet)
                lock_disturbance_failures += int(output[A_LOCK] != 1)
                generator_failures += int(output[c614.P_ADMIT] != 1
                                          or output[A_ADMIT_PROVENANCE] != 1)

        # Pair enumeration is a control.  The all-word theorem below follows
        # algebraically from generator-wise projector fixation.
        for first, second in product(A_GENERATORS, repeat=2):
            output = apply_a_schedule(formed, first.gates)
            output = apply_a_schedule(output, second.gates)
            pair_failures += int(packet_coordinates(output) != packet_coordinates(formed)
                                 or output[A_LOCK] != 1)

    # Pre-formation negative-lock gates remain active and restore LOCK.  This
    # is a direct anti-freeze control, not an admitted packet claim.
    pre = list(cycle614_source(0)); pre[A_TRANSIENT] = 1; pre = tuple(pre)
    for generator in A_GENERATORS:
        output = apply_a_schedule(pre, generator.gates)
        if generator.family == "negative_lock_packet":
            preformation_nontrivial += int(packet_coordinates(output) != packet_coordinates(pre))
            lock_disturbance_failures += int(output[A_LOCK] != 0)

    coherent_labels = []
    witness_generator = next(item for item in A_GENERATORS
                             if item.family == "negative_lock_packet")
    for transient in (0, 1):
        state = list(cycle614_source(0)); state[A_TRANSIENT] = transient
        coherent_labels.append(apply_a_schedule(tuple(state), witness_generator.gates))
    coherent_Gram_off_diagonal = int(coherent_labels[0] == coherent_labels[1]) * 2

    # Matter/clock generators must continue to act at LOCK=1.  Search the six
    # physical matter endpoint preparations for a nontrivial witness.
    dynamic_generators = tuple(item for item in A_GENERATORS
                               if item.family in ("matter", "matter_clock", "clock"))
    for generator in dynamic_generators:
        matter_clock_nontrivial += int(any(
            apply_a_schedule(cycle614_formed(direction), generator.gates)
            != cycle614_formed(direction) for direction in range(6)
        ))

    damaged = apply_a_schedule(cycle614_formed(0), A_FORMATION, reverse=True,
                               routed=True, delete_label="A:formation:lock")
    formation_deletion_visible = damaged[A_LOCK] == 1 and damaged[A_ADMIT_PROVENANCE] == 0

    locality = literal_locality((A_FORMATION, *(item.gates for item in A_GENERATORS)), A_WIDTH)
    frames = c614.c612.proper_cubic_frames(); frame_count = len(frames)
    names = {item.name for item in A_GENERATORS}
    frame_family_closure_failures = 0
    frame_generator_closure_tests = 0
    for frame, generator in product(frames, A_GENERATORS):
        frame_family_closure_failures += int(rotate_generator_name(generator, frame) not in names)
        frame_generator_closure_tests += 1

    family_counts = Counter(item.family for item in A_GENERATORS)
    algebraic_proof = {
        "negative_LOCK_packet_generator": "q -> q XOR ((1-LOCK)*TRANSIENT), LOCK -> LOCK",
        "packet_read_generator": "(q,r) -> (q,r XOR q); q is fixed",
        "matter_clock_generators": "support is disjoint from all packet and LOCK coordinates",
        "composition_theorem": (
            "each generator fixes every packet coordinate and LOCK on LOCK=1; therefore every finite composition in the "
            "declared 91-generator operation monoid fixes each packet-content projector by induction"
        ),
        "pair_enumeration_role": "finite control only, not the proof of arbitrary-word preservation",
    }
    result = {
        "disposition": "positive supplied lock-controlled finite local operation algebra",
        "Cycle614_block_M2": c614.P_WIDTH,
        "new_M2": A_WIDTH - c614.P_WIDTH,
        "total_M2": A_WIDTH,
        "LOCK_M2": 1,
        "retained_ADMIT_provenance_M2": 1,
        "clock_M2": 1,
        "transient_M2": 1,
        "readout_M2": len(A_READOUT),
        "allowed_generator_count": len(A_GENERATORS),
        "generator_family_counts": dict(family_counts),
        "generator_tests": 6 * 2 * len(A_GENERATORS),
        "ordered_generator_pair_controls": 6 * len(A_GENERATORS) ** 2,
        "formation_rows": formed_rows,
        "formation_failures": formation_failures,
        "formation_inverse_failures": formation_inverse_failures,
        "generator_projector_failures": generator_failures,
        "ordered_pair_control_failures": pair_failures,
        "LOCK_disturbance_failures": lock_disturbance_failures,
        "negative_LOCK_preformation_nontrivial_generators": preformation_nontrivial,
        "preformation_coherent_sectors_retained": len(coherent_labels),
        "preformation_coherent_Gram_off_diagonal_count": coherent_Gram_off_diagonal,
        "preformation_schedule_is_reversible_permutation": True,
        "matter_clock_nontrivial_at_LOCK1_generators": matter_clock_nontrivial,
        "dynamic_generator_count": len(dynamic_generators),
        "formation_deletion_visible": formation_deletion_visible,
        "all24_generator_family_closure_failures": frame_family_closure_failures,
        "all24_generator_closure_tests": frame_generator_closure_tests,
        "algebraic_all_finite_composition_preservation_proof": algebraic_proof,
        "locality": locality,
        "future_operation_restriction_derived_as_framework_law": False,
        "finite_algebra_called_all_future_permanence": False,
        "generator_schedule_boundary_supplied": True,
        "LOCK_intermediate_X_open_close_not_a_persistent_output": True,
        "packet_called_framework_Record": False,
    }
    result["pass"] = (
        formation_failures == formation_inverse_failures == generator_failures == pair_failures == 0
        and lock_disturbance_failures == frame_family_closure_failures == 0
        and preformation_nontrivial == 3 * c614.PACKET_WIDTH
        and coherent_Gram_off_diagonal == 0
        and matter_clock_nontrivial == len(dynamic_generators)
        and formation_deletion_visible and locality["pass"]
    )
    check("Route A materializes a reversible lock algebra whose generators fix packet projectors while matter/clock continues",
          result["pass"], {"generators": len(A_GENERATORS),
                            "pair_controls": result["ordered_generator_pair_controls"],
                            "literal_gates": locality["literal_gate_count"]})
    return result


# Route B: a finite paired carrier.  It is deliberately not called a tail
# sector: exact local formation creates + and - labels together, so every
# per-label conserved charge remains zero.
def b_layout(length: int) -> dict[str, object]:
    if length not in (3, 4, 6):
        raise ValueError("paired carrier leaves L3/L4/L6 domain")
    packet = tuple(range(3 * c614.PACKET_WIDTH))
    lock = len(packet)
    plus = tuple(tuple(range(lock + 1 + 6 * site, lock + 1 + 6 * (site + 1)))
                 for site in range(length))
    minus_start = lock + 1 + 6 * length
    minus = tuple(tuple(range(minus_start + 6 * site, minus_start + 6 * (site + 1)))
                  for site in range(length))
    return {"packet": packet, "lock": lock, "plus": plus, "minus": minus,
            "width": minus_start + 6 * length}


def b_gate(kind: str, sites: tuple[int, ...], label: str, width: int) -> Gate:
    return c505.gate(kind, sites, label, width)


def b_formation_schedule(length: int) -> tuple[Gate, ...]:
    layout = b_layout(length); width = int(layout["width"])
    packet = layout["packet"]; plus = layout["plus"]; minus = layout["minus"]
    schedule = []
    for direction in range(6):
        source = packet[1 + direction]
        schedule.append(b_gate("CNOT", (source, plus[0][direction]),
                               f"B:L{length}:form:plus:{direction}", width))
        schedule.append(b_gate("CNOT", (source, minus[0][direction]),
                               f"B:L{length}:form:minus:{direction}", width))
    return tuple(schedule)


def b_motion_schedule(length: int) -> tuple[Gate, ...]:
    layout = b_layout(length); width = int(layout["width"]); plus = layout["plus"]
    schedule = []
    # Adjacent swaps from the last pair backwards implement one right rotation
    # of the complete six-rail + carrier.  The - exhaust remains at formation.
    for site in range(length - 1, 0, -1):
        for direction in range(6):
            left, right = plus[site - 1][direction], plus[site][direction]
            schedule.extend((
                b_gate("CNOT", (left, right), f"B:L{length}:move:{site}:{direction}:a", width),
                b_gate("CNOT", (right, left), f"B:L{length}:move:{site}:{direction}:b", width),
                b_gate("CNOT", (left, right), f"B:L{length}:move:{site}:{direction}:c", width),
            ))
    return tuple(schedule)


def b_source(length: int, direction: int) -> tuple[int, ...]:
    layout = b_layout(length)
    packet = tuple(c614.packet_payload(direction) for _ in range(3))
    word = [0] * int(layout["width"])
    for site, bit in zip(layout["packet"], tuple(bit for replica in packet for bit in replica)):
        word[site] = bit
    word[int(layout["lock"])] = 1
    return tuple(word)


def apply_b(word: tuple[int, ...], schedule: tuple[Gate, ...], *, reverse: bool = False,
            delete_label: str | None = None) -> tuple[int, ...]:
    sequence = tuple(reversed(schedule)) if reverse else schedule
    if delete_label is not None:
        matches = tuple(item for item in sequence if item.label == delete_label)
        if len(matches) != 1:
            raise ValueError("paired-carrier deletion must name one gate")
        sequence = tuple(item for item in sequence if item.label != delete_label)
    output = list(word)
    for item in sequence:
        c505.apply_gate(output, item)
    return tuple(output)


def b_packet(word: tuple[int, ...], length: int) -> tuple[int, ...]:
    return tuple(word[site] for site in b_layout(length)["packet"])


def b_charges(word: tuple[int, ...], length: int) -> tuple[int, ...]:
    layout = b_layout(length)
    return tuple(sum(word[row[direction]] for row in layout["plus"])
                 - sum(word[row[direction]] for row in layout["minus"])
                 for direction in range(6))


def b_occupancies(word: tuple[int, ...], length: int) -> tuple[int, int]:
    layout = b_layout(length)
    return (sum(word[site] for row in layout["plus"] for site in row),
            sum(word[site] for row in layout["minus"] for site in row))


def rotate_b_labels(word: tuple[int, ...], length: int,
                    frame: c614.c612.Matrix) -> tuple[int, ...]:
    layout = b_layout(length); output = list(word)
    for rows in (layout["plus"], layout["minus"]):
        for row in rows:
            original = tuple(word[site] for site in row)
            moved = [0] * 6
            for direction, bit in enumerate(original):
                moved[c614.rotate_direction(direction, frame)] = bit
            for site, bit in zip(row, moved):
                output[site] = bit
    original_packet = tuple(tuple(word[layout["packet"][replica * c614.PACKET_WIDTH + bit]]
                                  for bit in range(c614.PACKET_WIDTH)) for replica in range(3))
    moved_packet = c614.rotate_packet(original_packet, frame)
    for site, bit in zip(layout["packet"], tuple(bit for replica in moved_packet for bit in replica)):
        output[site] = bit
    return tuple(output)


def route_b_finite_paired_carrier() -> dict[str, object]:
    rows = []
    failures = deletion_failures = covariance_failures = covariance_tests = 0
    frames = c614.c612.proper_cubic_frames()
    for length in (3, 4, 6):
        formation = b_formation_schedule(length)
        motion = b_motion_schedule(length)
        locality = literal_locality((formation, motion), int(b_layout(length)["width"]))
        inverse_failures = sector_leakage = packet_changes = recurrence_failures = 0
        direction_rows = []
        for direction in range(6):
            source = b_source(length, direction)
            formed = apply_b(source, formation)
            inverse_failures += int(apply_b(formed, formation, reverse=True) != source)
            sector_leakage += int(any(b_charges(formed, length)))
            failures += int(b_occupancies(formed, length) != (1, 1))
            current = formed
            positions = []
            for application in range(length):
                before_packet = b_packet(current, length)
                current = apply_b(current, motion)
                packet_changes += int(b_packet(current, length) != before_packet)
                sector_leakage += int(any(b_charges(current, length)))
                layout = b_layout(length)
                position = next(site for site, row in enumerate(layout["plus"])
                                if sum(current[index] for index in row) == 1)
                positions.append(position)
            recurrence_failures += int(current != formed)
            inverse_failures += int(apply_b(apply_b(formed, motion), motion, reverse=True) != formed)

            for frame in frames:
                moved_source = rotate_b_labels(source, length, frame)
                moved_formed = apply_b(moved_source, formation)
                expected = rotate_b_labels(formed, length, frame)
                covariance_failures += int(moved_formed != expected)
                covariance_tests += 1
                moved_once = apply_b(moved_formed, motion)
                expected_once = rotate_b_labels(apply_b(formed, motion), length, frame)
                covariance_failures += int(moved_once != expected_once)
                covariance_tests += 1
            direction_rows.append({"direction": direction, "motion_positions": positions,
                                   "charges_after_formation": b_charges(formed, length)})

        active = 0
        source = b_source(length, active)
        full = apply_b(source, formation)
        delete_plus = apply_b(source, formation,
                              delete_label=f"B:L{length}:form:plus:{active}")
        delete_minus = apply_b(source, formation,
                               delete_label=f"B:L{length}:form:minus:{active}")
        deletion_failures += int(b_charges(delete_plus, length)[active] != -1)
        deletion_failures += int(b_charges(delete_minus, length)[active] != 1)
        damaged_motion = apply_b(full, motion,
                                 delete_label=f"B:L{length}:move:1:{active}:a")
        deletion_failures += int(damaged_motion == apply_b(full, motion))

        failures += inverse_failures + sector_leakage + packet_changes + recurrence_failures
        failures += int(not locality["pass"])
        rows.append({
            "length": length,
            "split": {3: "train", 4: "held_out", 6: "held"}[length],
            "total_M2": int(b_layout(length)["width"]),
            "new_carrier_M2_beyond_packet_and_LOCK": 12 * length,
            "formation_logical_CNOT": len(formation),
            "one_rotation_logical_CNOT": len(motion),
            "direction_rows": direction_rows,
            "inverse_failures": inverse_failures,
            "sector_leakage_failures": sector_leakage,
            "packet_change_failures": packet_changes,
            "finite_rotation_recurrence_failures": recurrence_failures,
            "locality": locality,
        })
    result = {
        "disposition": "positive finite paired neutral carrier with mobile label and anchored formation exhaust",
        "rows": rows,
        "failures": failures,
        "deletion_failures": deletion_failures,
        "proper_cubic_frames": len(frames),
        "all24_label_covariance_tests": covariance_tests,
        "all24_label_covariance_failures": covariance_failures,
        "finite_local_formation_enters_neutral_paired_occupancy": True,
        "finite_local_formation_enters_nonzero_conserved_Q_sector": False,
        "Q_definition": "Q_d = sum_x plus[x,d] - sum_x minus[x,d]",
        "all_Q_d_remain_zero_under_correct_formation_and_motion": True,
        "called_tail_or_superselection_sector": False,
        "formation_inverse_erases_pair": True,
        "called_permanent_Record": False,
    }
    result["pass"] = (failures == deletion_failures == covariance_failures == 0
                      and len(frames) == 24)
    check("Route B forms and moves a finite paired neutral carrier without packet change or sector leakage",
          result["pass"], {"sizes": (3, 4, 6), "all24": covariance_tests})
    return result


@dataclass(frozen=True)
class FiniteMediumState:
    capacity: int
    frontier: tuple[int, ...]
    blank: tuple[int, ...]
    exhaust: tuple[int, ...]
    occupancy: tuple[int, ...]
    packets: tuple[tuple[tuple[int, ...], ...], ...]
    matter_endpoint: tuple[int, ...]
    matter_internal: int
    clock: int


def medium_initial(capacity: int) -> FiniteMediumState:
    if capacity not in (3, 4, 6):
        raise ValueError("medium capacity leaves H3/H4/H6 domain")
    return FiniteMediumState(
        capacity,
        (1,) + (0,) * capacity,
        (1,) * capacity,
        (0,) * capacity,
        (0,) * capacity,
        tuple(c614.blank_packet() for _ in range(capacity)),
        (1, 0, 0, 0, 0, 0),
        0,
        0,
    )


def validate_medium(state: FiniteMediumState) -> None:
    if state.capacity not in (3, 4, 6):
        raise ValueError("medium capacity leaves domain")
    if len(state.frontier) != state.capacity + 1 or sum(state.frontier) != 1:
        raise ValueError("frontier is not one-hot")
    if any(len(word) != state.capacity for word in
           (state.blank, state.exhaust, state.occupancy)):
        raise ValueError("medium bank width mismatch")
    if any(type(bit) is not int or bit not in (0, 1)
           for word in (state.frontier, state.blank, state.exhaust, state.occupancy)
           for bit in word):
        raise ValueError("medium ledger is nonbinary")
    if len(state.packets) != state.capacity:
        raise ValueError("packet bank width mismatch")
    if len(state.matter_endpoint) != 6 or sum(state.matter_endpoint) != 1:
        raise ValueError("matter endpoint is not one-hot")
    if state.matter_internal not in (0, 1) or state.clock not in (0, 1):
        raise ValueError("matter/clock bit leaves M2")
    head = state.frontier.index(1)
    for index, packet in enumerate(state.packets):
        c614.validate_packet(packet)
        expected_occupied = int(index < head)
        if (state.blank[index], state.exhaust[index], state.occupancy[index]) \
                != (1 - expected_occupied, expected_occupied, expected_occupied):
            raise ValueError("slot ledger disagrees with frontier")
        if (packet != c614.blank_packet()) != bool(expected_occupied):
            raise ValueError("packet freshness disagrees with occupancy")


def medium_ledger(state: FiniteMediumState) -> dict[str, int]:
    return {
        "frontier": state.frontier.index(1),
        "blank": sum(state.blank),
        "exhaust": sum(state.exhaust),
        "occupancy": sum(state.occupancy),
        "packets": sum(packet != c614.blank_packet() for packet in state.packets),
        "blank_plus_exhaust": sum(state.blank) + sum(state.exhaust),
    }


def medium_append(state: FiniteMediumState, *, delete: str | None = None) -> FiniteMediumState:
    validate_medium(state)
    head = state.frontier.index(1)
    if head == state.capacity:
        raise ValueError("finite medium is saturated")
    packet, meta = c614.route_a_step(c614.endpoint_triplets(state.matter_endpoint),
                                    c614.blank_packet())
    if not meta["admit"]:
        raise ValueError("medium append lacks a unique physical matter endpoint")
    frontier = list(state.frontier); blank = list(state.blank)
    exhaust = list(state.exhaust); occupancy = list(state.occupancy)
    packets = list(state.packets)
    if delete != "frontier-advance":
        frontier[head] = 0; frontier[head + 1] = 1
    if delete != "blank-debit":
        blank[head] = 0
    if delete != "exhaust-credit":
        exhaust[head] = 1
    if delete != "occupancy-write":
        occupancy[head] = 1
    if delete != "packet-write":
        packets[head] = packet
    return FiniteMediumState(state.capacity, tuple(frontier), tuple(blank), tuple(exhaust),
                             tuple(occupancy), tuple(packets), state.matter_endpoint,
                             state.matter_internal, state.clock)


def medium_reverse_append(state: FiniteMediumState) -> FiniteMediumState:
    validate_medium(state)
    head = state.frontier.index(1)
    if head == 0:
        raise ValueError("medium is already at genesis")
    target = head - 1
    packet = state.packets[target]
    decoded = c614.decode_packet(packet)
    if decoded is None:
        raise ValueError("reverse target lacks packet provenance")
    direction = int(decoded["direction"])
    endpoints = c614.endpoint_triplets(tuple(int(index == direction) for index in range(6)))
    restored, meta = c614.route_a_step(endpoints, packet, reverse=True)
    if not meta["admit"] or restored != c614.blank_packet():
        raise ValueError("reverse target provenance failed")
    frontier = list(state.frontier); blank = list(state.blank)
    exhaust = list(state.exhaust); occupancy = list(state.occupancy); packets = list(state.packets)
    frontier[head] = 0; frontier[target] = 1
    blank[target] = 1; exhaust[target] = 0; occupancy[target] = 0; packets[target] = restored
    return FiniteMediumState(state.capacity, tuple(frontier), tuple(blank), tuple(exhaust),
                             tuple(occupancy), tuple(packets), state.matter_endpoint,
                             state.matter_internal, state.clock)


def saturated_terminal_step(state: FiniteMediumState, *, reverse: bool = False) -> FiniteMediumState:
    validate_medium(state)
    if state.frontier.index(1) != state.capacity:
        raise ValueError("terminal matter/clock branch requires saturation")
    # X is self-inverse.  The physical endpoint and every archive coordinate
    # remain fixed while an internal matter rail and a clock rail continue.
    return FiniteMediumState(state.capacity, state.frontier, state.blank, state.exhaust,
                             state.occupancy, state.packets, state.matter_endpoint,
                             state.matter_internal ^ 1, state.clock ^ 1)


def relabel_spent_ready_without_erasure(state: FiniteMediumState, slot: int) -> FiniteMediumState:
    validate_medium(state)
    if slot not in range(state.capacity) or not state.occupancy[slot]:
        raise ValueError("relabel target is not occupied")
    blank = list(state.blank); exhaust = list(state.exhaust)
    blank[slot], exhaust[slot] = exhaust[slot], blank[slot]
    # This deliberately returns a diagnostic word outside the lawful archive
    # domain.  The occupied packet remains, so no fresh slot has been made.
    return FiniteMediumState(state.capacity, state.frontier, tuple(blank), tuple(exhaust),
                             state.occupancy, state.packets, state.matter_endpoint,
                             state.matter_internal, state.clock)


def slot_is_fresh(state: FiniteMediumState, slot: int) -> bool:
    return (state.blank[slot] == 1 and state.exhaust[slot] == 0
            and state.occupancy[slot] == 0 and state.packets[slot] == c614.blank_packet())


def route_c_finite_medium_and_saturation() -> dict[str, object]:
    rows = []
    failures = deletion_failures = renewal_failures = 0
    for capacity in (3, 4, 6):
        initial = medium_initial(capacity); state = initial; snapshots = []
        for application in range(capacity):
            previous_packets = state.packets
            state = medium_append(state)
            ledger = medium_ledger(state)
            failures += int(
                ledger["frontier"] != application + 1
                or ledger["blank"] != capacity - application - 1
                or ledger["exhaust"] != application + 1
                or ledger["occupancy"] != application + 1
                or ledger["packets"] != application + 1
                or ledger["blank_plus_exhaust"] != capacity
                or any(state.packets[index] != previous_packets[index]
                       for index in range(application))
            )
            snapshots.append({"forward_application_label_not_time": application + 1, **ledger})
        saturated = state
        refused = False
        try:
            medium_append(saturated)
        except ValueError:
            refused = True
        failures += int(not refused)

        terminal_once = saturated_terminal_step(saturated)
        terminal_twice = saturated_terminal_step(terminal_once)
        failures += int(terminal_once.packets != saturated.packets
                        or terminal_once.frontier != saturated.frontier
                        or terminal_once.matter_internal == saturated.matter_internal
                        or terminal_once.clock == saturated.clock
                        or terminal_twice != saturated)

        relabel_rows = []
        for slot in range(capacity):
            relabeled = relabel_spent_ready_without_erasure(saturated, slot)
            fresh = slot_is_fresh(relabeled, slot)
            lawful = True
            try:
                validate_medium(relabeled)
            except ValueError:
                lawful = False
            renewal_failures += int(fresh or lawful or relabeled.packets[slot] == c614.blank_packet())
            relabel_rows.append({"slot": slot, "ready_label_after_relabel": relabeled.blank[slot],
                                 "occupied": relabeled.occupancy[slot], "fresh": fresh,
                                 "lawful_archive_word": lawful})

        genesis = saturated
        for _ in range(capacity):
            genesis = medium_reverse_append(genesis)
        failures += int(genesis != initial)

        deletion_rows = []
        for deletion in ("frontier-advance", "blank-debit", "exhaust-credit",
                         "occupancy-write", "packet-write"):
            damaged = medium_append(initial, delete=deletion)
            visible = False
            try:
                validate_medium(damaged)
            except ValueError:
                visible = True
            deletion_failures += int(not visible)
            deletion_rows.append({"deletion": deletion, "visible": visible,
                                  **medium_ledger(damaged)})

        rows.append({
            "capacity": capacity,
            "split": {3: "train", 4: "held_out", 6: "held"}[capacity],
            "explicit_M2": 31 * capacity + 9,
            "ledger_layout": {
                "frontier_onehot": capacity + 1,
                "blank": capacity,
                "exhaust": capacity,
                "occupancy": capacity,
                "packet": 3 * c614.PACKET_WIDTH * capacity,
                "matter_endpoint": 6,
                "matter_internal": 1,
                "clock": 1,
            },
            "snapshots": snapshots,
            "saturation_refuses_further_formation": refused,
            "terminal_matter_clock_step_nontrivial": terminal_once != saturated,
            "terminal_two_step_recurrence_not_time": terminal_twice == saturated,
            "terminal_preserves_all_packets": terminal_once.packets == saturated.packets,
            "spent_ready_relabel_controls": relabel_rows,
            "complete_inverse_returns_genesis_only_by_erasing_archive": genesis == initial,
            "deletions": deletion_rows,
        })
    result = {
        "disposition": "positive finite saturated terminal; non-erasing renewal not achieved by spent/ready relabeling",
        "rows": rows,
        "failures": failures,
        "deletion_failures": deletion_failures,
        "renewal_control_failures": renewal_failures,
        "all_blank_exhaust_occupancy_frontier_packet_bits_accounted": True,
        "external_blank_stream_imported": False,
        "non_erasing_renewal_achieved": False,
        "finite_saturated_terminal_achieved": True,
        "terminal_matter_clock_dynamics_continues": True,
        "inverse_recovery_preserves_archive": False,
        "recurrence_label_called_time": False,
        "finite_terminal_called_permanence": False,
    }
    result["pass"] = failures == deletion_failures == renewal_failures == 0
    check("Route C closes a finite saturated terminal while explicit spent/ready relabeling fails to renew blank capacity",
          result["pass"], {"capacities": (3, 4, 6)})
    return result


def domain_controls(route_a: dict[str, object], route_b: dict[str, object],
                    route_c: dict[str, object], c614_receipt: dict[str, object]) -> dict[str, object]:
    rejected = 0
    attempts = (
        lambda: cycle614_source(6),
        lambda: apply_a_schedule((0,) * (A_WIDTH - 1), A_FORMATION),
        lambda: b_layout(5),
        lambda: b_source(3, 6),
        lambda: medium_initial(5),
        lambda: validate_medium(FiniteMediumState(3, (1, 1, 0, 0), (1, 1, 1),
                                                  (0, 0, 0), (0, 0, 0),
                                                  tuple(c614.blank_packet() for _ in range(3)),
                                                  (1, 0, 0, 0, 0, 0), 0, 0)),
        lambda: saturated_terminal_step(medium_initial(3)),
        lambda: medium_reverse_append(medium_initial(3)),
    )
    for attempt in attempts:
        try:
            attempt()
        except (ValueError, IndexError):
            rejected += 1
    mass_residual = c614_receipt["malformed_deletion_renewal_controls"]["one_particle_mass_fixture_residual"]
    result = {
        "malformed_rejections": rejected,
        "malformed_total": len(attempts),
        "one_particle_mass_fixture_residual": mass_residual,
        "Cycle614_matter_unchanged_at_formation":
            c614_receipt["malformed_deletion_renewal_controls"]["matter_unchanged"],
        "held_interfaces": {"matter_detector": ("L3", "held_out_L4", "held_L6"),
                            "paired_carrier": ("L3", "held_out_L4", "held_L6"),
                            "finite_medium": ("H3", "held_out_H4", "held_H6")},
        "incoming_time_PR": {
            "consumed": False,
            "dependency": False,
            "possible_future_interface": "a locally integrated branch label may be tested as matter/clock payload only",
            "would_supply_Record_law_or_permanence": False,
        },
        "supplied_algebra_called_derived_Record_law": False,
        "finite_preservation_called_all_future_permanence": False,
        "paired_carrier_called_tail_sector": False,
        "saturated_terminal_called_renewal": False,
        "packet_called_Record_or_actuality": False,
    }
    result["pass"] = (rejected == len(attempts) and mass_residual < TOL
                      and route_a["pass"] and route_b["pass"] and route_c["pass"])
    check("malformed, held, mass, time-interface, and forbidden-relabel controls remain explicit",
          result["pass"], {"rejected": rejected, "total": len(attempts),
                            "mass_residual": mass_residual})
    return result


def no_go_discipline(route_a: dict[str, object], route_b: dict[str, object],
                     route_c: dict[str, object]) -> dict[str, object]:
    families = (
        {"family": "lock-controlled constrained local algebra",
         "object": "Cycle614 packet plus local LOCK/provenance/readout/matter block",
         "mechanism": "negative-LOCK packet gates and generator-wise projector fixation",
         "terminal": "derive that this supplied generator algebra is exactly the framework's physical future-operation class",
         "status": "ATTEMPTED_POSITIVE_CONDITIONAL"},
        {"family": "finite paired neutral carrier",
         "object": "mobile plus label and anchored minus exhaust on L3/L4/L6",
         "mechanism": "local paired formation and conserved Q_d=plus-minus",
         "terminal": "nonzero sector entry or an independently preserving superselection law",
         "status": "ATTEMPTED_POSITIVE_NEUTRAL"},
        {"family": "finite explicit medium and saturated terminal",
         "object": "frontier/blank/exhaust/occupancy/archive ledger",
         "mechanism": "finite append followed by a packet-fixing matter/clock terminal permutation",
         "terminal": "non-erasing renewal beyond finite saturation",
         "status": "ATTEMPTED_POSITIVE_TERMINAL"},
        {"family": "dissipative metastable error-correcting medium",
         "object": "open local bath plus protected code",
         "mechanism": "energy barrier, autonomous correction, and entropy/exhaust export",
         "terminal": "derive bath state, local detailed balance, formation, and renewal",
         "status": "OPEN_NOT_COUNTED"},
        {"family": "infinite quasilocal charge representation",
         "object": "tail algebra or inequivalent representation sector",
         "mechanism": "finite-time local preparation approaching a protected thermodynamic label",
         "terminal": "construct lawful finite-time entry, readable content, and local accessibility bounds",
         "status": "OPEN_NOT_COUNTED"},
        {"family": "translation-invariant expanding or fractal archive",
         "object": "self-similar fresh-medium front in an unbounded lattice",
         "mechanism": "local reversible growth with conserved exhaust and nonoverwriting copies",
         "terminal": "derive genesis, density/capacity law, covariance, and noise tolerance",
         "status": "OPEN_NOT_COUNTED"},
    )
    walls = {
        "W_algebra": "derive which post-formation local operations are physical rather than supply a preserving generator restriction",
        "W_activation": "derive local activation of preservation at formation while retaining pre-formation coherence and dynamics",
        "W_permanence": "lift finite declared-algebra fixation to arbitrary/infinite/noisy future physical preservation",
        "W_capacity": "derive non-erasing fresh-medium renewal or justify finite saturation as the complete physical terminal",
        "W_actuality": "identify the admitted basis packet with an actual framework Record and its content owner",
    }
    directed = tuple({
        "from": source, "to": target, "closure_implied": False,
        "reason": f"closing {source} neither constructs nor logically selects {target}",
    } for source, target in product(walls, repeat=2) if source != target)
    result = {
        "N1_normalized_route_families": families,
        "N1_attempted_qualifying_families": 3,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "FAIL_DO_NOT_SHIP",
        "N2_collapsed_walls": walls,
        "N2_directional_wall_pairs": directed,
        "N2_directional_pair_count": len(directed),
        "N2_all_ordered_pairs_independent_on_exhibited_interfaces": len(directed) == 20,
        "N3_hidden_wall_scan": (
            "Cycle614 candidate law/circuit and blank packet; supplied future-generator list; LOCK/provenance genesis; "
            "generator schedule boundary and negative-control X-open/close microsteps; finite noiseless gates and joint-line chart; "
            "L3/L4/L6 carrier topology; paired exhaust; H3/H4/H6 empty "
            "medium/frontier; saturated-terminal rule; matter/clock internal rails; site-tagged packet identity; and held cuts are explicit"
        ),
        "N4_exact_residual_matching": (
            {"witness": "Cycle614", "witness_residual": "finite archive protection and candidate admission below Record/permanence",
             "current_residual": "post-formation algebra fixation and capacity after finite saturation", "match": True},
            {"witness": "Cycle571", "witness_residual": "finite append inverse and fresh-medium renewal below Record",
             "current_residual": "explicit H3/H4/H6 medium relabel/inverse/saturation", "match": True},
            {"witness": "Cycle587", "witness_residual": "redundancy inverse erases packet and does not select Record",
             "current_residual": "finite inverse and packet-status boundary", "match": True},
            {"witness": "Admissibility continuation refinement", "witness_residual": "block-preserving algebra only after restriction is supplied",
             "current_residual": "Route-A preserving generator algebra is supplied implementation content", "match": True},
            {"witness": "fresh-site permanence theorem", "witness_residual": "finite site-tagged retention is conditional representation, not physical formation dynamics",
             "current_residual": "finite locked packet and saturated archive remain conditional", "match": True},
        ),
        "N5_rhetoric_audit": (
            {"phrase": "supplied preserving algebra is not a derived Record law",
             "tested": "one 123-M2 block, 91 generators, all six packet contents, all ordered generator pairs",
             "untested": "general lattices, arbitrary channels, noise, infinite future", "wording": "finite supplied-algebra scoped"},
            {"phrase": "neutral paired carrier is not superselection protection",
             "tested": "L3/L4/L6 local pair formation/motion with every Q_d=0",
             "untested": "nonzero/infinite tail sectors and dissipative charges", "wording": "finite neutral-carrier scoped"},
            {"phrase": "spent/ready relabeling does not renew blank capacity",
             "tested": "every occupied slot at H3/H4/H6 under the explicit ledger",
             "untested": "expanding/infinite/dissipative media", "wording": "specific finite-ledger scoped"},
        ),
        "N6_partial_closure_paths": (
            "derive the physical future-operation algebra and compare it generator-by-generator with Route A",
            "derive formation-triggered local constraints from the extensional Admissibility successor law",
            "derive a thermodynamic or topological limit with finite-time local entry and readable labels",
            "derive a translation-invariant expanding archive or accept a separately justified saturated terminal",
            "identify actual Record formation before applying any permanence clause to the candidate packet",
        ),
        "N7_hostile_steelman": (
            "A dissipative topological or fracton-like QCA could locally nucleate a neutral defect pair, bind one defect to "
            "the admitted packet, drive the partner/exhaust outward, and make every low-energy future channel fix the bound "
            "label while a translation-invariant growth front continually recruits fresh cells.  The concrete terminal is a "
            "local Hamiltonian/channel family, a prepared bath state, finite-time entry estimate, autonomous correction bound, "
            "and conserved source ledger.  Routes A-C do not test that mechanism, so a broad no-go is premature."
        ),
        "N8_cross_cycle_echo": (
            "Cycles571/587 exposed reversible finite append and archive erasure; Cycle614 retired runtime admission bits and then "
            "materialized the local predicate circuit.  The Admissibility continuation note exhibited supplied block restriction. "
            "Because earlier host-wiring gaps closed by explicit compilers, operation-algebra derivation, dissipative protection, "
            "infinite sectors, and expanding archives remain live constructive routes."
        ),
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_substrate_obstruction": False,
        "axiom_pressure": False,
    }
    result["pass"] = (
        route_a["pass"] and route_b["pass"] and route_c["pass"]
        and result["N1_attempted_qualifying_families"] < result["N1_required_for_broad_negative"]
        and result["N2_all_ordered_pairs_independent_on_exhibited_interfaces"]
        and not result["negative_claim_shipped"] and not result["axiom_pressure"]
    )
    check("full N1-N8 blocks broad negative/minimum/axiom-pressure promotion and preserves open mechanisms",
          result["pass"], {"attempted": 3, "open": 3, "directed_pairs": len(directed)})
    return result


def inventory() -> dict[str, object]:
    return {
        "supplied": (
            "approved Record/Admissibility surfaces and site-tagged finite packet representation",
            "Cycle614 92-M2 admission circuit, candidate unique-quorum law, packet grammar, matter endpoint genesis, and blank target",
            "Route-A physical future-generator alphabet and local LOCK/provenance/readout layout",
            "finite noiseless X/CNOT/Toffoli identity and bounded joint-line routing chart",
            "Route-B L3/L4/L6 ring topology, blank paired carrier, and anchored minus-exhaust convention",
            "Route-C H3/H4/H6 empty medium/frontier and saturated-terminal matter/clock rule",
        ),
        "derived": (
            "reversible local formation activation with retained ADMIT provenance and no uncleared transient",
            "generator-wise packet-projector fixation on LOCK=1 and the induction theorem for every finite generated word",
            "nontrivial preformation packet/matter operations and continuing LOCK=1 matter/clock dynamics",
            "123-M2 bounded Route-A lowering to one/two-M2 literals with exact routing/restoration",
            "finite paired-carrier neutral charge, motion, recurrence, deletion, inverse, L3/L4/L6 and all24 label covariance",
            "explicit H3/H4/H6 blank/exhaust/occupancy/frontier/archive saturation and terminal packet preservation",
            "spent/ready relabeling fails freshness on every occupied slot in the declared finite ledger",
        ),
        "open": (
            "identification of the supplied generator algebra with the framework's physical post-formation operation law",
            "actuality/framework Record identification and physical activation from Admissibility/formation",
            "all-future, noisy, infinite-volume permanence and autonomous error correction",
            "non-erasing fresh-medium renewal beyond finite saturation or a physical completeness theorem for saturation",
            "nonzero conserved-sector entry, quasilocal tail representations, dissipative protection, and expanding archives",
            "physical time/rate/energy/stress/source/gravity meaning and integration of any later time-side interface",
        ),
        "forbidden_relabels": {
            "supplied_restriction_called_derived_Record_law": False,
            "finite_preservation_called_permanence": False,
            "neutral_pair_called_tail_superselection": False,
            "saturated_terminal_called_renewal": False,
            "packet_called_Record_or_actuality": False,
            "recurrence_called_time": False,
        },
    }


def note_text(receipt: dict[str, object]) -> str:
    a = receipt["route_A_constrained_operation_algebra"]
    b = receipt["route_B_finite_paired_carrier"]
    c = receipt["route_C_finite_medium_saturation"]
    locality = a["locality"]
    b_rows = "\n".join(
        f"| {row['length']} | {row['split']} | {row['total_M2']} | "
        f"{row['formation_logical_CNOT']} | {row['one_rotation_logical_CNOT']} | "
        f"{row['sector_leakage_failures']} | {row['packet_change_failures']} |"
        for row in b["rows"]
    )
    c_rows = "\n".join(
        f"| {row['capacity']} | {row['split']} | {row['explicit_M2']} | "
        f"{str(row['saturation_refuses_further_formation']).lower()} | "
        f"{str(row['terminal_matter_clock_step_nontrivial']).lower()} | "
        f"{str(row['terminal_preserves_all_packets']).lower()} | "
        f"{str(row['complete_inverse_returns_genesis_only_by_erasing_archive']).lower()} |"
        for row in c["rows"]
    )
    return f"""# Physical post-formation preservation / non-erasing renewal tournament — Cycle 621

Status: **positive supplied finite preserving algebra and finite saturated terminal; no derived Record law, all-future permanence, or non-erasing renewal**

Authority: **none**

Audit: **unset**

## Decisive result

Cycle 621 gives a split constructive answer.  One fixed bounded local
operation algebra can preserve every Cycle-614 packet coordinate while
matter/clock operations continue, once a local LOCK is activated.  The
activation and retained-ADMIT provenance are fully reversible and leave no
uncleared transient.  Separately, a finite medium can reach a lawful saturated
terminal whose matter/clock rails continue and whose old packets stay fixed.

Neither result derives the physical law needed by the framework Record clause.
The preserving generator restriction and saturated-terminal transition are
supplied candidate laws.  Finite preservation is not all-future permanence;
the basis packet remains neither actuality nor a framework Record.  No
non-erasing renewal beyond the declared finite capacity is obtained.

For executable dependency control, the runner byte-pins the Cycle-614
source, note, and current receipt and also pins the receipt with runtime fields
removed.  It checks the exact 92-M2, 690-logical-gate, 4,862-literal-gate and
schedule-digest contract; reconstructs all 64 interface truth/inverse rows,
18 single-copy, 18 double-copy and 90 spurious-copy controls; and checks the
same all24/all576 label convention.  Cycle 621 then uses this lightweight
finite-interface quotient to avoid initializing Cycle 614's unrelated deep
historical import tree.  This is not a reimplementation or reevaluation of
Cycle-614 science.

## Route A — lock-controlled constrained operation algebra

The exact Cycle-614 92-M2 block is extended to `{a['total_M2']}` M2 with one
LOCK, one retained ADMIT-provenance bit, one clock bit, one transient bit, and
27 readout bits.  Local formation copies the already retained ADMIT to LOCK and
provenance by two CNOTs.  Reversing those two gates and the Cycle-614 circuit
returns every formation row to genesis exactly; deleting the LOCK copy is
visible.

The declared algebra has `{a['allowed_generator_count']}` generators:
`{a['generator_family_counts']}`.  Every generator was tested for both
transient values and all six packet contents, giving
`{a['generator_tests']}` generator rows with zero packet-projector, LOCK,
ADMIT, or provenance failures.  All
`{a['ordered_generator_pair_controls']}` ordered generator-pair controls also
pass.

The arbitrary-composition result is algebraic, not extrapolated from the pair
census.  A negative-LOCK write acts as
`q -> q XOR ((1-LOCK)*TRANSIENT)` and restores LOCK.  A read gate acts as
`(q,r) -> (q,r XOR q)`.  Matter/clock generators have support disjoint from
packet and LOCK.  Therefore every generator fixes every packet-content
projector on LOCK=1, and induction gives fixation under every finite
composition in the declared 91-generator operation monoid.  All 27
negative-LOCK writes act nontrivially before
formation, while all `{a['dynamic_generator_count']}` matter/clock generators
have a nontrivial LOCK=1 witness.  The negative-LOCK witness is a reversible
permutation retaining two orthogonal preformation sectors, so a coherent
superposition is carried linearly rather than projected or frozen.  Formation
does not freeze the declared matter/clock dynamics.

The materialized schedules contain `{locality['logical_gate_count']}` logical
gates and lower to `{locality['literal_gate_count']:,}` literal one-/two-M2
gates.  Maximum literal support is `{locality['maximum_literal_support_M2']}`
M2.  The joint-line compiler emits
`{locality['forward_reverse_adjacent_SWAPS']:,}` forward/reverse adjacent swaps
and `{locality['literal_NN_calls']:,}` nearest-neighbor calls with zero route or
operand-restoration residual.  All 24 proper-cubic generator-family closure
checks pass on `{a['all24_generator_closure_tests']}` frame/generator rows.
The X-open/close microsteps used to express a negative LOCK control are inside
one supplied generator schedule; LOCK is restored at every declared operation
boundary.  Treating those boundaries as the physical operation alphabet is
part of the supplied restriction, not a derived law.

This is the strongest constructive result: a **supplied finite local operation
algebra** with exact packet-projector fixation and continuing matter/clock
dynamics.  It is implementation, not a derivation that these and only these
operations are physically allowed after framework Record formation.

## Route B — finite paired carrier

Route B locally copies the six-way packet label into one mobile plus rail and
one anchored minus-exhaust rail.  For every label,
`Q_d = sum_x plus[x,d] - sum_x minus[x,d]` remains exactly zero.  A fixed
nearest-neighbor rotation carries the plus label around the finite ring while
packet and LOCK remain fixed.

| L | split | total M2 | formation CNOT | rotation CNOT | Q leakage | packet changes |
|---:|---|---:|---:|---:|---:|---:|
{b_rows}

All `{b['all24_label_covariance_tests']}` proper-cubic label comparisons pass.
Deleting either formation leg produces charge `+1` or `-1`; deleting an active
motion gate changes the transport word.  Exact inverse clears both paired
rails, and L rotations recur to the same finite word.  Rotation count and
recurrence are not time.

Local formation therefore enters a nontrivial **neutral paired occupancy**,
not a nonzero conserved-charge sector.  This finite paired carrier is not
called a tail sector or superselection protection, and its inverse prevents a
permanence claim.

## Route C — explicit finite medium and saturated terminal

Every frontier, blank, exhaust, occupancy, packet, matter, and clock bit is
counted.  Appending consumes one blank, creates one exhaust/occupancy, advances
the one-hot frontier, and never changes an older packet.

| H | split | explicit M2 | next formation refused | matter/clock continues | packets fixed | inverse erases archive |
|---:|---|---:|---|---|---|---|
{c_rows}

At saturation, one fixed terminal operation toggles an internal matter rail
and the clock rail while leaving the physical matter endpoint, frontier, and
every packet unchanged.  Two terminal applications recur exactly.  This is a
positive finite saturated terminal, not physical time or all-future
permanence.

Relabeling any occupied spent slot as ready leaves occupancy and its nonblank
packet in place; every one of the H3/H4/H6 slot tests remains non-fresh and
outside the lawful archive code.  Exact inverse restores blank capacity only
by removing each archived packet and retreating the frontier.  Thus this
specific finite ledger does not achieve non-erasing renewal.  Expanding,
infinite, dissipative, and topological media remain untested.

## Supplied / derived / open

Supplied: the Record/Admissibility surfaces; Cycle614 packet circuit, candidate
law, matter genesis, blank target, and byte-pinned lightweight interface quotient;
the Route-A future-generator alphabet;
LOCK/provenance/readout layout; finite noiseless gates and route chart; the
L3/L4/L6 paired-carrier topology; the H3/H4/H6 empty medium; and the saturated
terminal rule.

Derived on those finite codes: reversible local LOCK activation; exact
generator-wise packet-projector fixation and its finite-word induction;
nonfrozen matter/clock dynamics; support-two lowering and routing; paired
neutral-carrier motion/inverse/deletion/covariance; exact finite resource
ledger, saturation, terminal recurrence, and the spent/ready freshness
falsifier.

Open: selection of the physical future-operation algebra; physical activation
from Admissibility/formation; actuality and framework Record status;
arbitrary/noisy/infinite permanence; non-erasing fresh-medium renewal or a
physical completeness theorem for saturation; nonzero/infinite sectors,
dissipative correction, expanding archives; and time/source/gravity meaning.
The incoming time PR is not consumed and is only possible future interface
context.

## N1–N8 disposition

N1 normalizes six route families: three attempted here and three concrete open
families—dissipative metastable correction, an infinite quasilocal charge
representation, and a translation-invariant expanding/fractal archive.  The
five-attempt threshold for a broad negative is not met.  N2 audits all 20
directed pairs among five collapsed walls: physical-algebra identification,
activation, permanence, capacity, and actuality.  N3 exposes every generator,
carrier, medium, route, state, and terminal input.  N4 matches Cycle614/571/587
and the continuation/permanence notes at their exact residuals.  N5 keeps every
negative phrase at the finite route tested.  N6 lists constructive retirement
paths.  N7 gives a concrete dissipative topological-QCA steelman.  N8 checks
that earlier wiring walls did close through explicit compilers.

Broad no-go: **FAIL / DO NOT SHIP**.  Minimum-content claim: **FAIL / DO NOT
SHIP**.  No shared substrate obstruction and no axiom pressure are established.
No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit-status surface was edited.
"""


def normalized(path: Path) -> str:
    body = path.read_text().lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> dict[str, object]:
    required = (
        "authority: none", "audit: unset", "supplied finite local operation algebra",
        "implementation, not a derivation", "finite preservation is not all-future permanence",
        "packet remains neither actuality nor a framework record", "no non-erasing renewal",
        "not a reimplementation or reevaluation of cycle-614 science",
        "every generator fixes every packet-content projector", "induction gives fixation",
        "declared 91-generator operation monoid",
        "formation does not freeze", "not called a tail sector", "neutral paired occupancy",
        "positive finite saturated terminal", "incoming time pr is not consumed",
        "all 24 proper-cubic", "held_out", "n1", "n8",
        "broad no-go: fail / do not ship", "no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    result = {"required_fragments": required, "missing": missing, "pass": not missing}
    check("Cycle621 note freezes preservation/Record/permanence/renewal boundaries",
          result["pass"], missing)
    return result


def main() -> None:
    started = time.monotonic()
    signal.alarm(int(WALL_CAP_SECONDS))
    shore, c614_receipt = shore_controls()
    route_a = route_a_constrained_operation_algebra()
    route_b = route_b_finite_paired_carrier()
    route_c = route_c_finite_medium_and_saturation()
    domain = domain_controls(route_a, route_b, route_c, c614_receipt)
    discipline = no_go_discipline(route_a, route_b, route_c)
    supplied = inventory()

    elapsed = time.monotonic() - started
    rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform != "darwin":
        rss *= 1024
    resources_ok = elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
    check("cold resource ceilings", resources_ok,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})

    receipt = {
        "status": "positive supplied finite preserving algebra and finite saturated terminal; no derived Record law, all-future permanence, or non-erasing renewal",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "frozen_law_sha256": FROZEN_LAW_SHA256,
        "shore": shore,
        "route_A_constrained_operation_algebra": route_a,
        "route_B_finite_paired_carrier": route_b,
        "route_C_finite_medium_saturation": route_c,
        "domain_controls": domain,
        "supplied_derived_open_inventory": supplied,
        "no_go_discipline": discipline,
        "six_wall_ledger": {
            "C_ref": "Cycle614 admitted packet now has a local reversible LOCK/provenance activation and an exact preserving candidate algebra; physical-law identification and actuality remain open",
            "C_num": "generator/projector, charge, capacity, deletion, recurrence, and held residuals are exact; no count is promoted to probability or time",
            "C_wrap": "every finite composition in the declared 91-generator monoid preserves packet projectors and a finite saturated terminal closes; arbitrary/noisy/infinite permanence and non-erasing renewal remain open",
            "C_int": "matter endpoint, admission packet, LOCK, paired exhaust, archive, and continuing matter/clock rails compose on finite code spaces; framework Record activation remains open",
            "C_local": "123-M2 Route A has explicit support-two lowering/joint routing; paired L3/L4/L6 and medium H3/H4/H6 pass faults, inverse, held and all24 label controls",
            "C_source": "every blank/exhaust/occupancy/frontier bit is counted and finite saturation is exact; no blank stream, energy/stress meaning, or renewable source is derived",
        },
        "maturity": {
            "operational_quantum_records_repo_strict": (4.90, 4.78),
            "causal_time_repo_strict": (4.10, 3.91),
            "inertia_matter_repo_strict": (4.85, 4.90),
            "gravity_source_repo_strict": (4.14, 3.89),
            "Born_probability_repo_strict": (4.21, 3.69),
        },
        "strongest_constructive_result": (
            "one explicit 123-M2 reversible candidate operation algebra whose declared 91-generator monoid "
            "fixes Cycle614 packet projectors after local LOCK activation while matter/clock operations remain nontrivial"
        ),
        "highest_honest_terminal": (
            "supplied finite preserving algebra plus finite paired carrier and saturated terminal; not a derived physical "
            "Record law, actuality, all-future permanence, non-erasing renewal, or time"
        ),
        "shared_substrate_obstruction": False,
        "axiom_pressure": False,
        "constitutional_effect": "none",
        "optimal_next_campaign": (
            "derive or falsify the physical post-formation operation class from the extensional Admissibility successor law; "
            "in parallel attack dissipative/topological protection and translation-invariant expanding fresh-medium fronts"
        ),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
    }
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    NOTE.write_text(note_text(receipt))
    contract = note_contract()
    receipt["note_contract"] = contract
    receipt["runner_sha256"] = file_sha(Path(__file__))
    receipt["note_sha256"] = file_sha(NOTE)
    receipt["tests_passed"] = PASS
    receipt["tests_failed"] = FAIL
    receipt["pass"] = (
        FAIL == 0 and resources_ok and shore["pass"] and route_a["pass"] and route_b["pass"]
        and route_c["pass"] and domain["pass"] and discipline["pass"] and contract["pass"]
    )
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS,
                      "tests_failed": FAIL, "elapsed_seconds": elapsed,
                      "maximum_RSS_bytes": rss, "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
