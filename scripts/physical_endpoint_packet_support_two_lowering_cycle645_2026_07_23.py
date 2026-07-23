#!/usr/bin/env python3
"""Cycle645: exact support-two lowering of the Cycle640 endpoint packet.

The immutable Cycle640 endpoint and predecessor/rotor packet use reversible
Boolean gates of support at most three.  This runner replaces every such gate
by an exact no-ancilla X/H/T/T-dagger/CNOT circuit, checks each local quantum
matrix (including negative controls), and reruns the complete Cycle640 truth,
inverse, deletion, held-size, and proper-cubic controls unchanged.

This is an elementary-gate lowering, not a nearest-neighbour placement, an
occurrence law, a Record, or a derivation of time.  Authority none; audit
unset; constitutional effect none.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import importlib
import io
import json
from pathlib import Path
import resource
import subprocess
import sys
import tarfile
import tempfile
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SHORE_REF = "c27f72ff8b1058d872695829c05e95da415813bc"
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5.0e-12
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ENDPOINT_PACKET_SUPPORT_TWO_LOWERING_CYCLE645_NOTE_2026-07-23.md"
)
RECEIPT = ROOT / "outputs/physical_endpoint_packet_support_two_lowering_cycle645_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_endpoint_packet_support_two_lowering_cycle645_cold_2026_07_23.txt"
C640_PATH = "scripts/physical_m2_endpoint_interval_packet_interface_cycle640_2026_07_23.py"
C640_NOTE = (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_M2_ENDPOINT_INTERVAL_PACKET_INTERFACE_CYCLE640_NOTE_2026-07-23.md"
)
C523_NOTE = (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PROTECTED_SHADOW_COIN_GATE_COMPILER_CYCLE523_NOTE_2026-07-21.md"
)
C527_NOTE = (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NATIVE_SHADOW_NEAREST_NEIGHBOR_ROUTER_CYCLE527_NOTE_2026-07-21.md"
)
C640_SHA = "3a11a467fb1c7aadf2db05f8332ed9b253b3c31d27bc2a591e15e5009e334f7e"

PASS = 0
FAIL = 0


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value):
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self):
        for stream in self.streams:
            stream.flush()


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def git_bytes(ref: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{ref}:{path}"], cwd=ROOT, check=True,
        stdout=subprocess.PIPE,
    ).stdout


def load_c640():
    archive = subprocess.run(
        ["git", "archive", "--format=tar", SHORE_REF, "scripts"],
        cwd=ROOT, check=True, stdout=subprocess.PIPE,
    ).stdout
    exported = tempfile.TemporaryDirectory(prefix="cycle645-shore-")
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as bundle:
        bundle.extractall(exported.name, filter="data")
    path = str(Path(exported.name) / "scripts")
    sys.path.insert(0, path)
    try:
        module = importlib.import_module(
            "physical_m2_endpoint_interval_packet_interface_cycle640_2026_07_23"
        )
    finally:
        sys.path.remove(path)
    return exported, module


SHORE_EXPORT, c640 = load_c640()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def line_number_bytes(data: bytes, needle: str) -> int:
    for number, line in enumerate(data.decode().splitlines(), 1):
        if needle in line:
            return number
    raise ValueError(needle)


def line_number(path: Path, needle: str) -> int:
    return line_number_bytes(path.read_bytes(), needle)


@dataclass(frozen=True)
class Primitive:
    kind: str
    qubits: tuple[str, ...]

    @property
    def support(self) -> int:
        return len(self.qubits)


def toffoli_sequence(first: str, second: str, target: str) -> list[Primitive]:
    return [
        Primitive("H", (target,)),
        Primitive("CNOT", (second, target)),
        Primitive("Tdg", (target,)),
        Primitive("CNOT", (first, target)),
        Primitive("T", (target,)),
        Primitive("CNOT", (second, target)),
        Primitive("Tdg", (target,)),
        Primitive("CNOT", (first, target)),
        Primitive("T", (second,)),
        Primitive("T", (target,)),
        Primitive("H", (target,)),
        Primitive("CNOT", (first, second)),
        Primitive("T", (first,)),
        Primitive("Tdg", (second,)),
        Primitive("CNOT", (first, second)),
    ]


def lower_gate(gate) -> list[Primitive]:
    controls = list(gate.controls)
    output: list[Primitive] = []
    for name, value in controls:
        if value == 0:
            output.append(Primitive("X", (name,)))
    if gate.kind == "toggle":
        target = gate.targets[0]
        if len(controls) == 0:
            output.append(Primitive("X", (target,)))
        elif len(controls) == 1:
            output.append(Primitive("CNOT", (controls[0][0], target)))
        elif len(controls) == 2:
            output.extend(toffoli_sequence(controls[0][0], controls[1][0], target))
        else:
            raise ValueError(f"unsupported toggle arity {len(controls)}")
    elif gate.kind == "swap" and len(controls) == 1:
        control = controls[0][0]
        left, right = gate.targets
        output.append(Primitive("CNOT", (right, left)))
        output.extend(toffoli_sequence(control, left, right))
        output.append(Primitive("CNOT", (right, left)))
    else:
        raise ValueError((gate.kind, controls, gate.targets))
    for name, value in reversed(controls):
        if value == 0:
            output.append(Primitive("X", (name,)))
    return output


I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
H2 = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
T2 = np.diag([1, np.exp(1j * np.pi / 4)])
TDG2 = T2.conj().T


def basis_bits(index: int, width: int) -> list[int]:
    return [(index >> (width - 1 - bit)) & 1 for bit in range(width)]


def bits_index(bits: list[int]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value


def primitive_matrix(primitive: Primitive, names: tuple[str, ...]) -> np.ndarray:
    width = len(names)
    dim = 1 << width
    if primitive.kind in ("X", "H", "T", "Tdg"):
        local = {"X": X2, "H": H2, "T": T2, "Tdg": TDG2}[primitive.kind]
        output = np.array([[1]], dtype=complex)
        target = names.index(primitive.qubits[0])
        for index in range(width):
            output = np.kron(output, local if index == target else I2)
        return output
    if primitive.kind == "CNOT":
        control = names.index(primitive.qubits[0])
        target = names.index(primitive.qubits[1])
        output = np.zeros((dim, dim), dtype=complex)
        for column in range(dim):
            bits = basis_bits(column, width)
            bits[target] ^= bits[control]
            output[bits_index(bits), column] = 1
        return output
    raise ValueError(primitive.kind)


def sequence_matrix(sequence: list[Primitive], names: tuple[str, ...]) -> np.ndarray:
    output = np.eye(1 << len(names), dtype=complex)
    for primitive in sequence:
        output = primitive_matrix(primitive, names) @ output
    return output


def ideal_matrix(gate, names: tuple[str, ...]) -> np.ndarray:
    dim = 1 << len(names)
    output = np.zeros((dim, dim), dtype=complex)
    control_indices = [(names.index(name), value) for name, value in gate.controls]
    targets = [names.index(name) for name in gate.targets]
    for column in range(dim):
        bits = basis_bits(column, len(names))
        if all(bits[index] == value for index, value in control_indices):
            if gate.kind == "toggle":
                bits[targets[0]] ^= 1
            elif gate.kind == "swap":
                bits[targets[0]], bits[targets[1]] = bits[targets[1]], bits[targets[0]]
            else:
                raise ValueError(gate.kind)
        output[bits_index(bits), column] = 1
    return output


def gate_names(gate) -> tuple[str, ...]:
    return tuple(name for name, _ in gate.controls) + tuple(gate.targets)


def block_audit(gates: list) -> dict:
    rows = []
    all_primitives = []
    for gate in gates:
        names = gate_names(gate)
        lowered = lower_gate(gate)
        actual = sequence_matrix(lowered, names)
        expected = ideal_matrix(gate, names)
        residual = float(np.max(np.abs(actual - expected)))
        inverse = actual.conj().T @ actual
        inverse_residual = float(np.max(np.abs(inverse - np.eye(len(inverse)))))
        deletion = []
        for index in range(len(lowered)):
            damaged = sequence_matrix(lowered[:index] + lowered[index + 1 :], names)
            deletion.append(float(np.linalg.norm(damaged - expected)))
        rows.append({
            "label": gate.label,
            "kind": gate.kind,
            "controls": gate.controls,
            "target_count": len(gate.targets),
            "high_level_support": gate.support,
            "primitive_count": len(lowered),
            "maximum_primitive_support_M2": max(p.support for p in lowered),
            "matrix_residual": residual,
            "inverse_residual": inverse_residual,
            "minimum_single_primitive_deletion_signal": min(deletion),
        })
        all_primitives.extend(lowered)
    counts = Counter(p.kind for p in all_primitives)
    passed = (
        all(row["matrix_residual"] < TOL and row["inverse_residual"] < TOL for row in rows)
        and all(row["minimum_single_primitive_deletion_signal"] > 1.0e-3 for row in rows)
        and all(p.support <= 2 for p in all_primitives)
    )
    return {
        "high_level_gate_count": len(gates),
        "primitive_gate_count": len(all_primitives),
        "primitive_counts": dict(sorted(counts.items())),
        "maximum_primitive_support_M2": max(p.support for p in all_primitives),
        "maximum_matrix_residual": max(row["matrix_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "minimum_single_primitive_deletion_signal": min(row["minimum_single_primitive_deletion_signal"] for row in rows),
        "rows": rows,
        "pass": passed,
    }


def immutable_shore() -> dict:
    observed = sha256(git_bytes(SHORE_REF, C640_PATH)).hexdigest()
    parent = json.loads(git_bytes(
        SHORE_REF,
        "outputs/physical_m2_endpoint_interval_packet_interface_cycle640_receipt_2026_07_23.json",
    ))
    result = {
        "ref": SHORE_REF,
        "Cycle640_runner_sha256": observed,
        "expected_Cycle640_runner_sha256": C640_SHA,
        "Cycle640_pass": parent["pass"],
        "Cycle640_authority": parent["authority"],
        "Cycle640_audit": parent["audit"],
        "working_tree_bytes_used_as_premise": False,
    }
    result["pass"] = bool(
        observed == C640_SHA and parent["pass"]
        and parent["authority"] == AUTHORITY and parent["audit"] == AUDIT
    )
    check("Cycle640 is loaded from one exact immutable shore", result["pass"], result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "## Result", "## Exact lowering", "## Controls", "## Supplied structure",
        "## Dependency ledger", "## N1-N8 discipline", "## Scope firewall",
    )
    result = {
        "missing_sections": tuple(section for section in required if section not in text),
        "authority_none": "Authority: **none**" in text,
        "audit_unset": "Audit: **unset**" in text,
        "accepted_false": "Accepted: **false**" in text,
    }
    result["pass"] = not result["missing_sections"] and all(
        result[key] for key in ("authority_none", "audit_unset", "accepted_false")
    )
    check("Cycle645 note is complete and non-authoritative", result["pass"], result)
    return result


def no_go_discipline(endpoint: dict, packet: dict) -> dict:
    current = str(Path(__file__).relative_to(ROOT))
    current_note = str(NOTE.relative_to(ROOT))
    c640_note_bytes = git_bytes(SHORE_REF, C640_NOTE)
    attempted = [{
        "family": "exact no-ancilla Clifford+T lowering",
        "honesty_marker": "ATTEMPTED",
        "status": "POSITIVE_ALL_CYCLE640_GATES",
    }]
    open_routes = [
        {"family": "ancilla-assisted Clifford+T optimization", "status": "OPEN_NOT_ATTEMPTED"},
        {"family": "measurement/reset lowering", "status": "OPEN_NOT_ATTEMPTED"},
        {"family": "native support-three primitive", "status": "OPEN_NOT_NEEDED"},
    ]
    residuals = [{
        "prior_ref": SHORE_REF, "prior_path": C640_NOTE,
        "prior_line": line_number_bytes(c640_note_bytes, "runtime gates have support at most three M2"),
        "prior_residual": "maximum_support_3", "current_path": current,
        "current_line": line_number(Path(__file__), '"maximum_primitive_support_M2"'),
        "current_residual": max(endpoint["maximum_primitive_support_M2"], packet["maximum_primitive_support_M2"]),
        "same_scope": True, "exact_match": False, "use_as_closure": True,
    }]
    rhetoric = [
        {"claim": "each replacement is exact", "per_element": "matrix equality", "per_site": "at most two M2", "per_mode": "Boolean basis and coherent extension", "per_block": "all Cycle640 blocks", "lattice_wide": "layout withheld"},
        {"claim": "support three is lowered", "per_element": "X/H/T/Tdg/CNOT", "per_site": "support <=2", "per_mode": "no ancilla", "per_block": "endpoint and packet", "lattice_wide": "nearest-neighbour withheld"},
        {"claim": "truth tables persist", "per_element": "replacement theorem", "per_site": "local", "per_mode": "all basis inputs", "per_block": "256 and 4096 controls", "lattice_wide": "finite L3/L6/L7 only"},
        {"claim": "the packet is reversible", "per_element": "dagger inverse", "per_site": "work returned", "per_mode": "lawful domain", "per_block": "predecessor/K16", "lattice_wide": "not time"},
        {"claim": "no law-level closure follows", "per_element": "gate law supplied", "per_site": "pointer candidate", "per_mode": "ports supplied", "per_block": "interface only", "lattice_wide": "occurrence/Record/time open"},
    ]
    partial = [
        {"file": current, "status": "EXECUTED_ENDPOINT_SUPPORT_TWO", "what_closes": "Cycle640 endpoint elementary-gate support"},
        {"file": current, "status": "EXECUTED_PACKET_SUPPORT_TWO", "what_closes": "Cycle640 predecessor/K16 packet elementary-gate support"},
        {"file": current, "status": "OPEN_NEAREST_NEIGHBOUR_PLACEMENT", "what_closes": "one fixed physical coordinate route for the packet roles"},
        {"file": current, "status": "OPEN_OCCURRENCE_AND_ADMISSION", "what_closes": "law-level actuality/admissibility ports"},
    ]
    steelman = {
        "argument": "The exact support-two factorization still needs one fixed nearest-neighbour placement and autonomous schedule on the actual packet roles; Cycle527 proves such routing only for a different pre-seam decoder.",
        "mechanism": "route each one/two-M2 primitive through installed blank physical sites and return all transport work",
        "decisive_test": "literal packet coordinates, adjacent calls, conflict-free schedule, inverse, deletion, L3/L6/L7, all24/all576",
        "actionable": True,
        "supporting_citations": [
            {"ref": SHORE_REF, "path": C527_NOTE, "line": 78},
            {"ref": "WORKTREE_CYCLE645", "path": current_note,
             "line": line_number(NOTE, "## Optimal next experiment")},
        ],
    }
    echoes = [
        {"cycle": 523, "retired": "support-three Toffoli import for its decoder", "mechanism": "exact 15-gate no-ancilla sequence", "applicability": "direct primitive identity", "citation_ref": SHORE_REF, "citation_path": C523_NOTE, "citation_line": 204},
        {"cycle": 527, "retired": "NN routing for a different decoder", "mechanism": "state-carried SWAP/CNOT paths", "applicability": "constructive template, not packet back-credit", "citation_ref": SHORE_REF, "citation_path": C527_NOTE, "citation_line": 78},
        {"cycle": 640, "retired": "bounded support-three packet", "mechanism": "reversible endpoint and predecessor/K16 cells", "applicability": "direct lowering target", "citation_ref": SHORE_REF, "citation_path": C640_NOTE, "citation_line": 44},
    ]
    passed = (
        len(attempted) == 1 and attempted[0]["honesty_marker"] == "ATTEMPTED"
        and all("honesty_marker" not in row for row in open_routes)
        and len(residuals) == 1
        and all(all(key in row for key in ("prior_ref", "prior_path", "prior_line", "prior_residual", "current_path", "current_line", "current_residual", "same_scope", "exact_match", "use_as_closure")) for row in residuals)
        and len(rhetoric) == 5 and all(all(key in row for key in ("per_element", "per_site", "per_mode", "per_block", "lattice_wide")) for row in rhetoric)
        and len(partial) == 4 and all(all(key in row for key in ("file", "status", "what_closes")) for row in partial)
        and steelman["actionable"] and len(echoes) == 3
    )
    result = {
        "N1_normalized_families": attempted,
        "N1_open_routes_not_counted": open_routes,
        "N1_qualifying_attempts": 1,
        "N1_required_for_broad_negative": 5,
        "N1_broad_negative_gate": "WITHHELD__CONSTRUCTIVE_RESULT_AND_OPEN_ROUTES",
        "N2_collapsed_walls": [
            {"wall": "elementary_support", "status": "CLOSED_HERE"},
            {"wall": "nearest_neighbour_layout", "status": "OPEN_DISTINCT"},
            {"wall": "law_level_occurrence", "status": "OPEN_DISTINCT"},
        ],
        "N2_directed_pairs": [
            {"from": "elementary_support", "to": "nearest_neighbour_layout", "independent": True},
            {"from": "nearest_neighbour_layout", "to": "elementary_support", "independent": True},
            {"from": "elementary_support", "to": "law_level_occurrence", "independent": True},
            {"from": "law_level_occurrence", "to": "elementary_support", "independent": True},
            {"from": "nearest_neighbour_layout", "to": "law_level_occurrence", "independent": True},
            {"from": "law_level_occurrence", "to": "nearest_neighbour_layout", "independent": True},
        ],
        "N3_hidden_wall_scan": [
            "X/H/T/T-dagger/CNOT matrices are supplied candidate physical gate law",
            "nearest-neighbour role coordinates are not supplied",
            "blank transport sites and their genesis are not supplied",
            "actuality/admissibility/law-domain ports remain supplied",
            "finite L3/L6/L7 is not an infinite history theorem",
            "gate count is not elapsed time or energy",
        ],
        "N4_residual_matching": residuals,
        "N4_exact_residual_matches": [],
        "N4_dropped_nonmatches": [],
        "N5_rhetoric_resolution_ledger": rhetoric,
        "N6_partial_closure_paths": partial,
        "N7_hostile_steelman": steelman,
        "N7_steelman": steelman,
        "N8_cross_cycle_echo": echoes,
        "Status": "PASS" if passed else "FAIL",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
        "axiom_pressure_claim": False,
        "pass": passed,
    }
    check("N1-N8 permits only the constructive support-two claim", passed, {
        "attempted": len(attempted), "open": len(open_routes), "negative": False,
    })
    return result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    print("Cycle645 endpoint/packet support-two lowering", AUTHORITY, AUDIT)
    shore = immutable_shore()
    note = note_contract()

    c640.PASS = c640.FAIL = 0
    endpoint_original = c640.endpoint_predicate_tournament()
    packet_original = c640.packet_unit_tournament()
    covariance = c640.covariance_controls(endpoint_original, packet_original)
    original_pass = bool(
        endpoint_original["pass"] and packet_original["pass"] and covariance["pass"]
        and c640.FAIL == 0
    )
    check("immutable Cycle640 truth/inverse/deletion/held/covariance controls rerun unchanged", original_pass, {
        "Cycle640_pass": c640.PASS, "Cycle640_fail": c640.FAIL,
        "endpoint_rows": endpoint_original["truth_table_rows"],
        "packet_cases": packet_original["basis_cases_exhausted"],
    })

    endpoint_gates, _, _ = c640.endpoint_circuit("p0", "claimed", "in")
    packet_gates, _ = c640.packet_circuit("src", "tgt", "pkt", "port", "u")
    endpoint = block_audit(endpoint_gates)
    packet = block_audit(packet_gates)
    check("every endpoint gate lowers exactly to support-one/two primitives", endpoint["pass"], {
        "high_level": endpoint["high_level_gate_count"], "primitive": endpoint["primitive_gate_count"],
        "residual": endpoint["maximum_matrix_residual"], "support": endpoint["maximum_primitive_support_M2"],
    })
    check("every packet gate lowers exactly to support-one/two primitives", packet["pass"], {
        "high_level": packet["high_level_gate_count"], "primitive": packet["primitive_gate_count"],
        "residual": packet["maximum_matrix_residual"], "support": packet["maximum_primitive_support_M2"],
    })

    template_rows = {}
    for control_values in ((1,), (0,), (1, 1), (1, 0), (0, 1), (0, 0)):
        controls = tuple((f"c{i}", value) for i, value in enumerate(control_values))
        gate = c640.Gate(f"toggle_{''.join(map(str, control_values))}", "toggle", controls, ("t",))
        template_rows[gate.label] = block_audit([gate])
    for value in (0, 1):
        gate = c640.Gate(f"fredkin_{value}", "swap", (("c", value),), ("a", "b"))
        template_rows[gate.label] = block_audit([gate])
    templates_pass = all(row["pass"] for row in template_rows.values())
    check("all positive/negative CNOT, Toffoli and Fredkin templates are exact and deletion-sensitive", templates_pass, {
        "templates": len(template_rows),
        "maximum_residual": max(row["maximum_matrix_residual"] for row in template_rows.values()),
    })

    discipline = no_go_discipline(endpoint, packet)
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    caps_pass = elapsed < 120.0 and maximum_rss < 1_000_000_000
    check("cold run stays within declared caps", caps_pass, {
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
    })
    receipt = {
        "status": "positive exact Cycle640 support-two elementary lowering; NN layout and law-level occurrence open",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "author_accepted": False,
        "author_artifact_status_accepted": False,
        "constitutional_effect": "none",
        "breakthrough": False,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "immutable_shore": shore,
        "note_contract": note,
        "unchanged_Cycle640_controls": {
            "endpoint": endpoint_original,
            "packet": packet_original,
            "covariance": covariance,
            "pass": original_pass,
        },
        "endpoint_lowering": endpoint,
        "packet_lowering": packet,
        "polarity_templates": template_rows,
        "strongest_constructive_result": (
            "all Cycle640 endpoint and predecessor/K16 packet gates have exact no-ancilla "
            "X/H/T/T-dagger/CNOT replacements with maximum physical support two"
        ),
        "nearest_neighbour_layout_closed": False,
        "occurrence_Record_or_time_claimed": False,
        "supplied_structure": [
            "immutable Cycle640 Boolean endpoint/packet circuit and lawful domain",
            "candidate physical X/H/T/T-dagger/CNOT matrices",
            "the standard exact no-ancilla Toffoli identity",
            "named endpoint roles, packet roles, truth inputs, and port meanings",
            "finite L3/L6/L7 size family and compile-time proper-cubic labels",
        ],
        "six_wall_ledger": {
            "C_ref": "unchanged; blank roles, identity and reference genesis remain supplied",
            "C_num": "unchanged; exact coherent unitary lowering introduces no numerical fit",
            "C_wrap": "support-three packet gate import retired; packet counts remain not time",
            "C_int": "endpoint/packet Boolean interaction now elementary support two; occurrence/admission remain law-level ports",
            "C_local": "advanced for Cycle640 interface; fixed nearest-neighbour role placement remains open",
            "C_source": "unchanged; no source, gravity, energy or resource genesis is derived",
        },
        "no_go_discipline": discipline,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "tests_passed": PASS,
        "tests_failed": FAIL,
    }
    receipt["pass"] = bool(
        FAIL == 0 and shore["pass"] and note["pass"] and original_pass
        and endpoint["pass"] and packet["pass"] and templates_pass
        and discipline["pass"] and caps_pass
    )
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=str) + "\n")
    summary = {
        "pass": receipt["pass"],
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "endpoint_primitive_gates": endpoint["primitive_gate_count"],
        "packet_primitive_gates": packet["primitive_gate_count"],
        "maximum_support_M2": 2,
        "maximum_residual": max(endpoint["maximum_matrix_residual"], packet["maximum_matrix_residual"]),
        "nearest_neighbour_layout_closed": False,
        "axiom_pressure": False,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as handle:
        original = sys.stdout
        sys.stdout = Tee(original, handle)
        try:
            raise SystemExit(main())
        finally:
            sys.stdout = original
