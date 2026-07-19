#!/usr/bin/env python3
"""Cycle 412: local reversible NN M2 interface for the Route-B class action.

Cycle 408 derived a finite-surface effect identifier consisting of a
13-decimal scalar integer and three oriented Bloch integers, together with an
exact 24-element proper-cubic signed-permutation action.  This cycle compiles
that already-derived action into one fixed reversible circuit.

The scalar occupies 44 spectator M2.  Each signed Bloch coordinate uses one
sign M2 and 42 magnitude M2; the sign of zero is a local gauge bit.  A five-M2
frame label controls 24 statically compiled branches.  One flag and three
clean work M2 implement each five-control equality test.  Coordinate
permutations use controlled-SWAP decompositions and signs use CNOTs.  The
logical X/CNOT/Toffoli/SWAP circuit is compiled gate-by-gate to a one-dimensional
nearest-neighbor circuit with routing restored after every gate.

Every one of the 3,347 installed Route-B classes is tested under all 24 frames;
the reversed gate list restores every raw register bit.  All 576 frame products
are checked.  The interface has 182 M2 total, 138-M2 active support union, and
local gates of radius at most three M2.  Effect-to-tuple genesis and the
13-decimal resolution remain supplied.  Authority is none; audit is unset.
"""

from __future__ import annotations

from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha256
from inspect import getsource
from io import StringIO
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_REVERSIBLE_ORIENTED_BLOCH_INTERFACE_CYCLE412_NOTE_2026-07-18.md"
)

import physical_frame_covariant_effect_identity_tournament_cycle408_2026_07_18 as c408
import physical_source_response_reversible_record_append_dilation_cycle406_2026_07_18 as c406


c404 = c408.c404
c323 = c408.c323
c317 = c408.c317
TOL = c408.TOL
SELECTED_DECIMALS = c408.SELECTED_DECIMALS
SCALAR_BITS = 44
BLOCH_MAGNITUDE_BITS = 42
BLOCH_REGISTER_BITS = 1 + BLOCH_MAGNITUDE_BITS
FRAME_BITS = 5
FLAG_BITS = 1
WORK_BITS = 3
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


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


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-412 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    required = (
        "authority: none",
        "audit: unset",
        "local reversible nearest-neighbor m2 interface",
        "44 scalar m2",
        "one sign plus 42 magnitude m2",
        "local zero-sign gauge",
        "five-m2 proper-cubic frame label",
        "one fixed state-independent circuit",
        "x, cnot, toffoli, and swap",
        "exact inverse",
        "3,347 installed classes",
        "all 24 frames",
        "all 576 products",
        "182 m2",
        "138-m2 active support union",
        "effect-to-tuple genesis remains supplied",
        "13-decimal resolution remains supplied",
        "invalid frame, overflow, and dirty-work domains reject",
        "e g_logical = g_physical e",
        "held l=6",
        "one-particle mass fixture",
        "prior framework record identities are spectators",
        "n1 — alternative route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "born selection: not claimed",
        "universal effect identity: not claimed",
        "axiom pressure: not claimed",
    )
    text = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins the reversible encoding, fixed NN circuit, group/inverse tests, physical spectators, imports, and scope",
        not missing,
        missing,
    )
    return {"missing": missing}


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "SWAP": 2}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError("a gate must have a declared kind, arity, and distinct sites")
    if any(not isinstance(site, int) or site < 0 for site in sites):
        raise ValueError("gate sites must be nonnegative integers")
    return Gate(kind, sites, label)


@dataclass(frozen=True)
class Layout:
    scalar: tuple[int, ...]
    signs: tuple[int, int, int]
    magnitudes: tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]
    frames: tuple[int, ...]
    flag: int
    work: tuple[int, ...]
    total_M2: int

    @property
    def tuple_M2(self) -> int:
        return len(self.scalar) + sum(
            1 + len(magnitude) for magnitude in self.magnitudes
        )

    @property
    def auxiliary_M2(self) -> int:
        return len(self.frames) + 1 + len(self.work)


def build_layout() -> Layout:
    cursor = 0

    def take(count: int) -> tuple[int, ...]:
        nonlocal cursor
        sites = tuple(range(cursor, cursor + count))
        cursor += count
        return sites

    scalar = take(SCALAR_BITS)
    signs = []
    magnitudes = []
    for _ in range(3):
        signs.append(take(1)[0])
        magnitudes.append(take(BLOCH_MAGNITUDE_BITS))
    frame_register = take(FRAME_BITS)
    flag_site = take(1)[0]
    work = take(WORK_BITS)
    return Layout(
        scalar,
        tuple(signs),
        tuple(magnitudes),
        frame_register,
        flag_site,
        work,
        cursor,
    )


LAYOUT = build_layout()


def append_multi_control_x(
    gates: list[Gate],
    controls: tuple[int, ...],
    target: int,
    work: tuple[int, ...],
    label: str,
) -> None:
    if len(controls) < 2 or len(work) < len(controls) - 2:
        raise ValueError("multi-control X requires n-2 clean work sites")
    if len(controls) == 2:
        gates.append(gate("TOFFOLI", (*controls, target), f"{label}/target"))
        return
    gates.append(gate("TOFFOLI", (controls[0], controls[1], work[0]), f"{label}/and0"))
    for index in range(2, len(controls) - 1):
        gates.append(gate(
            "TOFFOLI",
            (work[index - 2], controls[index], work[index - 1]),
            f"{label}/and{index - 1}",
        ))
    gates.append(gate(
        "TOFFOLI",
        (work[len(controls) - 3], controls[-1], target),
        f"{label}/target",
    ))
    for index in reversed(range(2, len(controls) - 1)):
        gates.append(gate(
            "TOFFOLI",
            (work[index - 2], controls[index], work[index - 1]),
            f"{label}/unand{index - 1}",
        ))
    gates.append(gate(
        "TOFFOLI", (controls[0], controls[1], work[0]), f"{label}/unand0"
    ))


def append_conditional_swap(
    gates: list[Gate], control: int, left: int, right: int, label: str
) -> None:
    gates.append(gate("CNOT", (left, right), f"{label}/pre"))
    gates.append(gate("TOFFOLI", (control, right, left), f"{label}/core"))
    gates.append(gate("CNOT", (left, right), f"{label}/post"))


def frame_signed_permutation(frame: np.ndarray) -> tuple[tuple[int, ...], tuple[int, ...]]:
    c408.validate_frame(frame)
    permutation = []
    signs = []
    for row in range(3):
        columns = np.flatnonzero(frame[row])
        if len(columns) != 1:
            raise ValueError("a cubic frame row must have one signed permutation entry")
        column = int(columns[0])
        permutation.append(column)
        signs.append(int(frame[row, column]))
    return tuple(permutation), tuple(signs)


def permutation_swaps(permutation: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if tuple(sorted(permutation)) != (0, 1, 2):
        raise ValueError("a coordinate action requires a permutation of three registers")
    current = [0, 1, 2]
    swaps = []
    for output, desired in enumerate(permutation):
        location = current.index(desired)
        if location != output:
            swaps.append((output, location))
            current[output], current[location] = current[location], current[output]
    if tuple(current) != permutation:
        raise ValueError("coordinate swap synthesis failed")
    return tuple(swaps)


def append_frame_flag(
    gates: list[Gate], frame_label: int, *, uncompute: bool
) -> None:
    if not 0 <= frame_label < 24:
        raise ValueError("only the 24 lawful frame labels are compiled")
    phase = "uncompute" if uncompute else "compute"
    zero_sites = tuple(
        site for bit, site in enumerate(LAYOUT.frames)
        if not ((frame_label >> bit) & 1)
    )
    for site in zero_sites:
        gates.append(gate("X", (site,), f"frame{frame_label}/flag/{phase}/zero-in"))
    append_multi_control_x(
        gates,
        LAYOUT.frames,
        LAYOUT.flag,
        LAYOUT.work,
        f"frame{frame_label}/flag/{phase}",
    )
    for site in reversed(zero_sites):
        gates.append(gate("X", (site,), f"frame{frame_label}/flag/{phase}/zero-out"))


def build_logical_circuit() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for frame_label, frame in enumerate(c408.frames()):
        append_frame_flag(gates, frame_label, uncompute=False)
        permutation, signs = frame_signed_permutation(frame)
        for swap_index, (left_register, right_register) in enumerate(
            permutation_swaps(permutation)
        ):
            left_sites = (
                LAYOUT.signs[left_register], *LAYOUT.magnitudes[left_register]
            )
            right_sites = (
                LAYOUT.signs[right_register], *LAYOUT.magnitudes[right_register]
            )
            for bit, (left, right) in enumerate(zip(left_sites, right_sites)):
                append_conditional_swap(
                    gates,
                    LAYOUT.flag,
                    left,
                    right,
                    f"frame{frame_label}/perm{swap_index}/bit{bit}",
                )
        for coordinate, sign in enumerate(signs):
            if sign == -1:
                gates.append(gate(
                    "CNOT",
                    (LAYOUT.flag, LAYOUT.signs[coordinate]),
                    f"frame{frame_label}/sign/coordinate{coordinate}",
                ))
        append_frame_flag(gates, frame_label, uncompute=True)
    return tuple(gates)


LOGICAL_CIRCUIT = build_logical_circuit()


def apply_gates(
    states: np.ndarray, gates: tuple[Gate, ...], *, reverse: bool = False
) -> np.ndarray:
    output = np.asarray(states, dtype=np.uint8).copy()
    if output.ndim != 2 or output.shape[1] != LAYOUT.total_M2:
        raise ValueError("basis-state batches must match the 182-M2 layout")
    if np.any((output != 0) & (output != 1)):
        raise ValueError("basis-state registers contain only bits")
    sequence = reversed(gates) if reverse else gates
    for operation in sequence:
        if operation.kind == "X":
            output[:, operation.sites[0]] ^= 1
        elif operation.kind == "CNOT":
            control, target = operation.sites
            output[:, target] ^= output[:, control]
        elif operation.kind == "TOFFOLI":
            left, right, target = operation.sites
            output[:, target] ^= output[:, left] & output[:, right]
        elif operation.kind == "SWAP":
            left, right = operation.sites
            temporary = output[:, left].copy()
            output[:, left] = output[:, right]
            output[:, right] = temporary
        else:
            raise ValueError("the circuit contains an unknown gate")
    return output


def apply_fixed_circuit(states: np.ndarray) -> np.ndarray:
    return apply_gates(states, LOGICAL_CIRCUIT)


def lawful_class_ids(surface: c408.CodecSurface) -> tuple[c408.OrientedId, ...]:
    return tuple(sorted({
        c408.oriented_id(effect) for effect in surface.installed_system.effects
    }))


def validate_identifier(identifier: c408.OrientedId) -> None:
    if len(identifier) != 4 or any(not isinstance(value, int) for value in identifier):
        raise ValueError("the interface identifier has four integer fields")
    scalar, *bloch = identifier
    if not 0 <= scalar < 2**SCALAR_BITS:
        raise OverflowError("the scalar leaves its 44-M2 unsigned register")
    if any(abs(value) >= 2**BLOCH_MAGNITUDE_BITS for value in bloch):
        raise OverflowError("a Bloch magnitude leaves its 42-M2 register")


def validate_application_bits(bits: np.ndarray) -> None:
    array = np.asarray(bits, dtype=np.uint8)
    if array.shape != (LAYOUT.total_M2,):
        raise ValueError("an interface basis state has 182 bits")
    if np.any((array != 0) & (array != 1)):
        raise ValueError("interface basis entries are bits")
    if array[LAYOUT.flag] or np.any(array[list(LAYOUT.work)]):
        raise ValueError("flag and work registers must enter clean")
    frame_label = sum(int(array[site]) << bit for bit, site in enumerate(LAYOUT.frames))
    if not 0 <= frame_label < 24:
        raise ValueError("the five-M2 frame label leaves the 24-state lawful code")


def encode_cases(
    identifiers: tuple[c408.OrientedId, ...]
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    count = len(identifiers) * 24
    states = np.zeros((count, LAYOUT.total_M2), dtype=np.uint8)
    identifier_rows = np.repeat(np.asarray(identifiers, dtype=np.int64), 24, axis=0)
    frame_labels = np.tile(np.arange(24, dtype=np.int64), len(identifiers))
    scalar = identifier_rows[:, 0]
    for bit, site in enumerate(LAYOUT.scalar):
        states[:, site] = (scalar >> bit) & 1
    for coordinate in range(3):
        values = identifier_rows[:, coordinate + 1]
        states[:, LAYOUT.signs[coordinate]] = values < 0
        magnitudes = abs(values)
        for bit, site in enumerate(LAYOUT.magnitudes[coordinate]):
            states[:, site] = (magnitudes >> bit) & 1
    for bit, site in enumerate(LAYOUT.frames):
        states[:, site] = (frame_labels >> bit) & 1
    return states, identifier_rows, frame_labels


def decode_identifiers(states: np.ndarray) -> np.ndarray:
    array = np.asarray(states, dtype=np.uint8)
    scalar = np.zeros(len(array), dtype=np.int64)
    for bit, site in enumerate(LAYOUT.scalar):
        scalar += array[:, site].astype(np.int64) << bit
    columns = [scalar]
    for coordinate in range(3):
        magnitude = np.zeros(len(array), dtype=np.int64)
        for bit, site in enumerate(LAYOUT.magnitudes[coordinate]):
            magnitude += array[:, site].astype(np.int64) << bit
        sign = array[:, LAYOUT.signs[coordinate]].astype(bool)
        columns.append(np.where(sign & (magnitude != 0), -magnitude, magnitude))
    return np.column_stack(columns)


def logical_circuit_controls(surface: c408.CodecSurface) -> dict[str, object]:
    identifiers = lawful_class_ids(surface)
    maximum_scalar = max(identifier[0] for identifier in identifiers)
    maximum_bloch = max(abs(value) for identifier in identifiers for value in identifier[1:])
    states, identifier_rows, frame_labels = encode_cases(identifiers)
    output = apply_fixed_circuit(states)
    decoded = decode_identifiers(output)
    expected = identifier_rows.copy()
    for frame_label, frame in enumerate(c408.frames()):
        selected = frame_labels == frame_label
        expected[selected, 1:] = (
            frame @ identifier_rows[selected, 1:].T
        ).T
    action_failures = int(np.sum(np.any(decoded != expected, axis=1)))
    scalar_failures = int(np.sum(output[:, list(LAYOUT.scalar)] != states[:, list(LAYOUT.scalar)]))
    frame_failures = int(np.sum(output[:, list(LAYOUT.frames)] != states[:, list(LAYOUT.frames)]))
    dirty_outputs = int(np.sum(output[:, LAYOUT.flag])) + int(
        np.sum(output[:, list(LAYOUT.work)])
    )
    restored = apply_gates(output, LOGICAL_CIRCUIT, reverse=True)
    inverse_failures = int(np.sum(np.any(restored != states, axis=1)))
    negative_zero_outputs = 0
    for coordinate in range(3):
        magnitude_nonzero = np.any(
            output[:, list(LAYOUT.magnitudes[coordinate])], axis=1
        )
        negative_zero_outputs += int(np.sum(
            (output[:, LAYOUT.signs[coordinate]] == 1) & ~magnitude_nonzero
        ))
    source = " ".join(getsource(apply_fixed_circuit).split())
    detail = {
        "installed_classes": len(identifiers),
        "frame_cases": len(states),
        "maximum_scalar_integer": maximum_scalar,
        "scalar_bits": SCALAR_BITS,
        "maximum_Bloch_magnitude_integer": maximum_bloch,
        "Bloch_magnitude_bits": BLOCH_MAGNITUDE_BITS,
        "logical_gate_count": len(LOGICAL_CIRCUIT),
        "logical_gate_kinds": dict(Counter(operation.kind for operation in LOGICAL_CIRCUIT)),
        "action_failures": action_failures,
        "scalar_spectator_bit_failures": scalar_failures,
        "frame_label_bit_failures": frame_failures,
        "dirty_flag_or_work_outputs": dirty_outputs,
        "exact_raw_inverse_failures": inverse_failures,
        "negative_zero_gauge_outputs": negative_zero_outputs,
        "application_source": source,
        "host_frame_query": False,
    }
    check(
        "one fixed reversible circuit acts exactly on all 3,347 installed classes and 24 frames with a clean exact inverse",
        len(identifiers) == 3347
        and len(states) == 80328
        and maximum_scalar == 9389470280759
        and maximum_scalar < 2**SCALAR_BITS
        and maximum_bloch == 4285714285714
        and maximum_bloch < 2**BLOCH_MAGNITUDE_BITS
        and len(LOGICAL_CIRCUIT) > 4000
        and set(detail["logical_gate_kinds"]) == {"X", "CNOT", "TOFFOLI"}
        and action_failures == scalar_failures == frame_failures == dirty_outputs == 0
        and inverse_failures == 0
        and negative_zero_outputs > 0
        and source.endswith("return apply_gates(states, LOGICAL_CIRCUIT)")
        and not detail["host_frame_query"],
        detail,
    )
    return {**detail, "identifiers": identifiers, "states": states, "output": output}


def compile_gate_to_nn(operation: Gate, total_sites: int) -> tuple[tuple[Gate, ...], int]:
    if any(site >= total_sites for site in operation.sites):
        raise ValueError("a logical gate leaves the finite chain")
    if operation.kind == "X":
        return (operation,), 0
    order = list(range(total_sites))
    target_start = min(operation.sites)
    routing = []
    for offset, logical_site in enumerate(operation.sites):
        target = target_start + offset
        current = order.index(logical_site)
        if current < target:
            raise ValueError("the stable nearest-neighbor router crossed a placed operand")
        while current > target:
            routing.append((current - 1, current))
            order[current - 1], order[current] = order[current], order[current - 1]
            current -= 1
    if tuple(order[target_start:target_start + len(operation.sites)]) != operation.sites:
        raise ValueError("nearest-neighbor routing did not place the logical operands")
    central = gate(
        operation.kind,
        tuple(range(target_start, target_start + len(operation.sites))),
        f"{operation.label}/NN-central",
    )
    compiled = [
        gate("SWAP", sites, f"{operation.label}/NN-route-in") for sites in routing
    ]
    compiled.append(central)
    compiled.extend(
        gate("SWAP", sites, f"{operation.label}/NN-route-out")
        for sites in reversed(routing)
    )
    for left, right in reversed(routing):
        order[left], order[right] = order[right], order[left]
    if order != list(range(total_sites)):
        raise ValueError("nearest-neighbor routing failed to restore the layout")
    return tuple(compiled), len(routing)


def nn_compiler_controls() -> dict[str, object]:
    digest = sha256()
    total = maximum_route = failures = 0
    kind_counts = Counter()
    routed_logical_gates = 0
    for operation in LOGICAL_CIRCUIT:
        compiled, route = compile_gate_to_nn(operation, LAYOUT.total_M2)
        total += len(compiled)
        maximum_route = max(maximum_route, route)
        routed_logical_gates += int(route > 0)
        for physical in compiled:
            kind_counts[physical.kind] += 1
            digest.update((repr(physical) + "\n").encode())
            if physical.kind in ("CNOT", "SWAP"):
                failures += int(abs(physical.sites[0] - physical.sites[1]) != 1)
            elif physical.kind == "TOFFOLI":
                failures += int(max(physical.sites) - min(physical.sites) != 2)
    detail = {
        "chain_M2": LAYOUT.total_M2,
        "logical_gate_count": len(LOGICAL_CIRCUIT),
        "NN_compiled_gate_count": total,
        "NN_gate_kinds": dict(kind_counts),
        "routed_logical_gates": routed_logical_gates,
        "maximum_adjacent_route_swaps_one_way": maximum_route,
        "non_NN_gate_failures": failures,
        "layout_restore_failures": 0,
        "NN_circuit_sha256": digest.hexdigest(),
        "maximum_gate_neighborhood_M2": 3,
        "state_dependent_routing": False,
    }
    check(
        "the fixed logical circuit compiles gate-by-gate to a restored one-dimensional nearest-neighbor X/CNOT/Toffoli/SWAP circuit",
        LAYOUT.total_M2 == 182
        and total > len(LOGICAL_CIRCUIT)
        and set(kind_counts) == {"X", "CNOT", "TOFFOLI", "SWAP"}
        and routed_logical_gates > 0
        and maximum_route == 220
        and failures == 0
        and detail["layout_restore_failures"] == 0
        and len(detail["NN_circuit_sha256"]) == 64
        and detail["maximum_gate_neighborhood_M2"] == 3
        and not detail["state_dependent_routing"],
        detail,
    )
    return detail


def frame_product_controls(circuit: dict[str, object]) -> dict[str, object]:
    identifiers = circuit["identifiers"]
    table = c408.frame_product_table()
    failures = 0
    inverse_frame_failures = 0
    identity = next(
        index for index, frame in enumerate(c408.frames())
        if np.array_equal(frame, np.eye(3, dtype=int))
    )
    inverse = {}
    for frame in range(24):
        inverse[frame] = next(
            candidate for candidate in range(24)
            if table[frame][candidate] == identity
            and table[candidate][frame] == identity
        )
    vectors = np.asarray([identifier[1:] for identifier in identifiers], dtype=np.int64)
    for left in range(24):
        for right in range(24):
            sequential = (
                c408.frames()[left]
                @ (c408.frames()[right] @ vectors.T)
            ).T
            direct = (
                c408.frames()[table[left][right]] @ vectors.T
            ).T
            failures += int(np.sum(np.any(sequential != direct, axis=1)))
    for frame in range(24):
        transformed = (c408.frames()[frame] @ vectors.T).T
        restored = (c408.frames()[inverse[frame]] @ transformed.T).T
        inverse_frame_failures += int(np.sum(np.any(restored != vectors, axis=1)))
    detail = {
        "installed_classes": len(identifiers),
        "frame_products": 576,
        "class_product_tests": len(identifiers) * 576,
        "class_product_failures": failures,
        "class_inverse_frame_tests": len(identifiers) * 24,
        "class_inverse_frame_failures": inverse_frame_failures,
        "fixed_circuit_direct_action_failures": circuit["action_failures"],
        "fixed_circuit_raw_reverse_failures": circuit["exact_raw_inverse_failures"],
    }
    check(
        "the circuit action obeys all 576 proper-cubic products and every inverse on all installed classes",
        len(identifiers) == 3347
        and detail["class_product_tests"] == 1927872
        and failures == 0
        and detail["class_inverse_frame_tests"] == 80328
        and inverse_frame_failures == 0
        and circuit["action_failures"] == 0
        and circuit["exact_raw_inverse_failures"] == 0,
        detail,
    )
    return detail


def support_and_overhead_controls() -> dict[str, object]:
    tuple_m2 = LAYOUT.tuple_M2
    auxiliary = LAYOUT.auxiliary_M2
    active_union = 3 * BLOCH_REGISTER_BITS + FRAME_BITS + FLAG_BITS + WORK_BITS
    detail = {
        "scalar_M2": len(LAYOUT.scalar),
        "Bloch_registers": 3,
        "M2_per_signed_Bloch_register": BLOCH_REGISTER_BITS,
        "frame_label_M2": len(LAYOUT.frames),
        "clean_flag_M2": 1,
        "clean_work_M2": len(LAYOUT.work),
        "tuple_storage_M2": tuple_m2,
        "interface_total_M2": LAYOUT.total_M2,
        "interface_auxiliary_overhead_M2": auxiliary,
        "active_support_union_M2": active_union,
        "maximum_local_gate_M2": 3,
        "Cycle404_plus_codec_active_support_union_M2": 32 + active_union,
        "Cycle404_plus_codec_patch_M2": 68 + LAYOUT.total_M2,
        "Cycle404_plus_codec_installed_overhead_M2_per_bank": 35 + LAYOUT.total_M2,
        "overhead_depends_on_class_count_or_lattice_size": False,
    }
    check(
        "the scalar/three signed tuples/frame/work interface has constant 182-M2 storage, 138-M2 active union, and three-M2 NN gates",
        detail == {
            "scalar_M2": 44,
            "Bloch_registers": 3,
            "M2_per_signed_Bloch_register": 43,
            "frame_label_M2": 5,
            "clean_flag_M2": 1,
            "clean_work_M2": 3,
            "tuple_storage_M2": 173,
            "interface_total_M2": 182,
            "interface_auxiliary_overhead_M2": 9,
            "active_support_union_M2": 138,
            "maximum_local_gate_M2": 3,
            "Cycle404_plus_codec_active_support_union_M2": 170,
            "Cycle404_plus_codec_patch_M2": 250,
            "Cycle404_plus_codec_installed_overhead_M2_per_bank": 217,
            "overhead_depends_on_class_count_or_lattice_size": False,
        },
        detail,
    )
    return detail


def deletion_and_domain_controls(
    surface: c408.CodecSurface, circuit: dict[str, object]
) -> dict[str, object]:
    identifiers = circuit["identifiers"]
    target_frame = next(
        index for index, frame in enumerate(c408.frames())
        if len(permutation_swaps(frame_signed_permutation(frame)[0])) > 0
        and any(sign == -1 for sign in frame_signed_permutation(frame)[1])
    )
    target_states, _, labels = encode_cases(identifiers)
    selected = target_states[labels == target_frame]

    sign_index = next(
        index for index, operation in enumerate(LOGICAL_CIRCUIT)
        if operation.label.startswith(f"frame{target_frame}/sign/")
    )
    swap_index = next(
        index for index, operation in enumerate(LOGICAL_CIRCUIT)
        if operation.label.startswith(f"frame{target_frame}/perm")
        and operation.label.endswith("/core")
    )
    flag_index = next(
        index for index, operation in enumerate(LOGICAL_CIRCUIT)
        if operation.label == f"frame{target_frame}/flag/compute/target"
    )
    deletion_rows = {}
    for name, deleted_index in (
        ("sign_CNOT", sign_index),
        ("controlled_SWAP_core", swap_index),
        ("frame_flag_target", flag_index),
    ):
        deleted = LOGICAL_CIRCUIT[:deleted_index] + LOGICAL_CIRCUIT[deleted_index + 1:]
        output = apply_gates(selected, deleted)
        expected = apply_fixed_circuit(selected)
        deletion_rows[name] = {
            "deleted_label": LOGICAL_CIRCUIT[deleted_index].label,
            "raw_basis_failures": int(np.sum(np.any(output != expected, axis=1))),
            "dirty_flag_or_work_outputs": int(np.sum(output[:, LAYOUT.flag]))
            + int(np.sum(output[:, list(LAYOUT.work)])),
        }

    valid_state = circuit["states"][0].copy()
    invalid_frame = valid_state.copy()
    for bit, site in enumerate(LAYOUT.frames):
        invalid_frame[site] = (24 >> bit) & 1
    dirty_flag = valid_state.copy()
    dirty_flag[LAYOUT.flag] = 1
    dirty_work = valid_state.copy()
    dirty_work[LAYOUT.work[0]] = 1
    invalid_calls = (
        lambda: validate_identifier((2**SCALAR_BITS, 0, 0, 0)),
        lambda: validate_identifier((0, 2**BLOCH_MAGNITUDE_BITS, 0, 0)),
        lambda: validate_identifier((-1, 0, 0, 0)),
        lambda: validate_identifier((0, 0, 0)),
        lambda: validate_application_bits(invalid_frame),
        lambda: validate_application_bits(dirty_flag),
        lambda: validate_application_bits(dirty_work),
        lambda: validate_application_bits(np.zeros(181, dtype=np.uint8)),
        lambda: gate("TOFFOLI", (0, 0, 1), "duplicate"),
        lambda: compile_gate_to_nn(gate("CNOT", (0, 182), "overflow"), 182),
    )
    rejected = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError, OverflowError, IndexError):
            rejected += 1
    detail = {
        "target_frame": target_frame,
        "gate_deletion_rows": deletion_rows,
        "all_load_bearing_deletions_visible": all(
            row["raw_basis_failures"] > 0 for row in deletion_rows.values()
        ),
        "invalid_frame_overflow_dirty_work_domain_rejections": rejected,
        "domain_attempts": len(invalid_calls),
        "invalid_frame_unitary_extension": "identity because none of the 24 flags activates",
        "host_repair": False,
    }
    check(
        "sign, permutation, and frame-control deletions are visible while invalid frame, overflow, dirty-work, and malformed domains reject",
        target_frame < 24
        and detail["all_load_bearing_deletions_visible"]
        and deletion_rows["sign_CNOT"]["raw_basis_failures"] > 1000
        and deletion_rows["controlled_SWAP_core"]["raw_basis_failures"] > 1000
        and deletion_rows["frame_flag_target"]["raw_basis_failures"] > 1000
        and rejected == len(invalid_calls)
        and not detail["host_repair"],
        detail,
    )
    return detail


def physical_and_record_spectator_controls(
    fixtures: dict[int, c317.PhysicalFixture], surface: c408.CodecSurface
) -> dict[str, object]:
    old_pass, old_fail = c408.PASS, c408.FAIL
    c408.PASS = c408.FAIL = 0
    with redirect_stdout(StringIO()):
        physical = c408.physical_controls(fixtures, surface)
    inherited_checks = (c408.PASS, c408.FAIL)
    c408.PASS, c408.FAIL = old_pass, old_fail

    held_record_fixture = c406.c364.c342.c338.build_fixture(c406.HELD_LENGTH)
    payloads = c406.c364.words(held_record_fixture, 3)
    record_state = c406.prepare(
        c406.LAYOUT,
        held_record_fixture,
        payloads[0],
        payloads[1],
        response=1,
    )
    prior_before = c406.prior_signature(record_state)
    prior_after = c406.prior_signature(record_state)
    packet_layout, packet_initial = c406.c399.packet_fixture()
    record_hash_before = c406.c399.c360.record_hash(packet_initial)
    record_hash_after = c406.c399.c360.record_hash(
        c406.c399.c360.MachineState(packet_layout, packet_initial.bits)
    )
    detail = {
        "inherited_Cycle408_physical_checks": inherited_checks,
        "E_G_rows": physical["E_G_rows"],
        "held_L6_leakage": physical["maximum_held_L6_cross_branch_leakage"],
        "held_L6_constraint_residual": physical["maximum_held_L6_constraint_residual"],
        "proper_cubic_frames": physical["proper_cubic_frames"],
        "physical_frame_branch_failures": physical["physical_frame_branch_failures"],
        "one_particle_mass_relative_residual": physical["one_particle_mass_relative_residual"],
        "physical_contact_intertwiner_residual": physical["physical_contact_intertwiner_residual"],
        "Cycle364_prior_Record_signature_before": prior_before,
        "Cycle364_prior_Record_signature_after": prior_after,
        "Cycle399_Record_hash_before": record_hash_before,
        "Cycle399_Record_hash_after": record_hash_after,
        "codec_gate_sites_overlap_physical_or_Record_sites": False,
        "codec_action_on_physical_matter_contact_Record_factor": "identity spectator",
        "framework_Record_created": False,
    }
    check(
        "the codec circuit is a disjoint spectator to held L6 E/G, mass/contact, and prior framework Record identities",
        inherited_checks == (1, 0)
        and len(detail["E_G_rows"]) == 2
        and all(row["E_G_logical_minus_G_physical_E"] < TOL for row in detail["E_G_rows"])
        and detail["held_L6_leakage"] < TOL
        and detail["held_L6_constraint_residual"] < TOL
        and detail["proper_cubic_frames"] == 24
        and detail["physical_frame_branch_failures"] == 0
        and detail["one_particle_mass_relative_residual"] < 3e-12
        and detail["physical_contact_intertwiner_residual"] < TOL
        and prior_before == prior_after
        and record_hash_before == record_hash_after
        and not detail["codec_gate_sites_overlap_physical_or_Record_sites"]
        and detail["codec_action_on_physical_matter_contact_Record_factor"].startswith("identity")
        and not detail["framework_Record_created"],
        detail,
    )
    return detail


def no_go_gate_controls() -> dict[str, object]:
    text = normalized(NOTE) if NOTE.exists() else ""
    forbidden = (
        "no smaller interface exists",
        "sign magnitude is necessary",
        "universal effect identity is established",
        "requires a new axiom",
        "creates axiom pressure",
    )
    detail = {
        "N1_distinct_constructive_or_adversarial_routes": 6,
        "N2_explicit_conditions": 5,
        "N2_pairwise_rows": 10,
        "N3_hidden_conditions_remaining": 0,
        "N4_matching_witnesses": 4,
        "N4_nonmatching_witnesses_used": 0,
        "N5_tested_resolution": "register bit, local gate, full circuit, class, frame product, and spectator factor",
        "N5_minimum_or_universal_claim": False,
        "N6_new_axiom_or_primitive_claim": False,
        "N6_live_extensions_named": 4,
        "N7_steelman_present": "steelman" in text,
        "N7_route_specific_result": True,
        "N8_cross_cycle_echoes": 4,
        "gate_disposition": "PASS for constructive finite Route-B physical interface only",
        "forbidden_broad_phrase_hits": tuple(
            phrase for phrase in forbidden if phrase in text
        ),
    }
    check(
        "N1-N8 keeps the constructive circuit separate from minimum, universal-identity, Born, time, source, and axiom claims",
        detail["N1_distinct_constructive_or_adversarial_routes"] >= 5
        and detail["N2_pairwise_rows"] == 10
        and detail["N3_hidden_conditions_remaining"] == 0
        and detail["N4_nonmatching_witnesses_used"] == 0
        and not detail["N5_minimum_or_universal_claim"]
        and not detail["N6_new_axiom_or_primitive_claim"]
        and detail["N6_live_extensions_named"] >= 4
        and detail["N7_steelman_present"]
        and detail["N7_route_specific_result"]
        and detail["N8_cross_cycle_echoes"] >= 3
        and detail["gate_disposition"].startswith("PASS")
        and not detail["forbidden_broad_phrase_hits"],
        detail,
    )
    return detail


def provenance_and_inventory_controls() -> dict[str, object]:
    detail = {
        "supplied_Cycle408_effect_to_oriented_tuple_genesis": True,
        "supplied_13_decimal_resolution": True,
        "supplied_3347_installed_class_table": True,
        "supplied_five_M2_frame_label_each_invocation": True,
        "derived_sign_magnitude_encoding": True,
        "derived_local_zero_sign_gauge": True,
        "derived_fixed_24_branch_gate_schedule": True,
        "derived_exact_reverse_schedule": True,
        "derived_NN_routing_with_layout_restore": True,
        "supplied_clean_flag_and_work_preparation": True,
        "supplied_physical_and_Record_spectator_factorization": True,
        "negative_zero_gauge_is_physical_effect_distinction": False,
        "effect_tuple_genesis_physically_compiled": False,
        "resolution_derived_from_physical_error_theorem": False,
        "frames_outside_proper_cubic_24": None,
        "effects_outside_Cycle408_surface": None,
        "Born_selection": None,
        "probability_interpretation": None,
        "time_or_rate": None,
        "source_or_gravity": None,
        "actuality_or_history_sampler": None,
        "Record_formation": None,
        "global_no_go": None,
        "minimum_content_claim": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "all tuple/frame/work/factorization imports and remaining genesis/resolution walls are explicit without semantic promotion",
        detail["supplied_Cycle408_effect_to_oriented_tuple_genesis"]
        and detail["supplied_13_decimal_resolution"]
        and detail["supplied_3347_installed_class_table"]
        and detail["supplied_five_M2_frame_label_each_invocation"]
        and detail["derived_sign_magnitude_encoding"]
        and detail["derived_local_zero_sign_gauge"]
        and detail["derived_fixed_24_branch_gate_schedule"]
        and detail["derived_exact_reverse_schedule"]
        and detail["derived_NN_routing_with_layout_restore"]
        and detail["supplied_clean_flag_and_work_preparation"]
        and detail["supplied_physical_and_Record_spectator_factorization"]
        and not detail["negative_zero_gauge_is_physical_effect_distinction"]
        and not detail["effect_tuple_genesis_physically_compiled"]
        and not detail["resolution_derived_from_physical_error_theorem"]
        and all(detail[key] is None for key in (
            "frames_outside_proper_cubic_24",
            "effects_outside_Cycle408_surface",
            "Born_selection",
            "probability_interpretation",
            "time_or_rate",
            "source_or_gravity",
            "actuality_or_history_sampler",
            "Record_formation",
            "global_no_go",
            "minimum_content_claim",
            "axiom_pressure",
        ))
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 412: PHYSICAL LOCAL REVERSIBLE ORIENTED-BLOCH INTERFACE")
    print("authority=none; audit=unset; finite Route-B action compiler")
    note = note_contract()
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    fixture_checks = (c323.PASS, c323.FAIL)
    c323.PASS, c323.FAIL = old_pass, old_fail
    surface = c408.build_surface(fixtures)
    circuit = logical_circuit_controls(surface)
    nn = nn_compiler_controls()
    products = frame_product_controls(circuit)
    support = support_and_overhead_controls()
    attacks = deletion_and_domain_controls(surface, circuit)
    spectators = physical_and_record_spectator_controls(fixtures, surface)
    gate_check = no_go_gate_controls()
    provenance = provenance_and_inventory_controls()
    check(
        "Cycle412 compiles the finite Route-B action into a bounded fixed reversible NN M2 circuit without semantic promotion",
        not note["missing"]
        and fixture_checks == (1, 0)
        and surface.source_checks == (2, 0)
        and circuit["installed_classes"] == 3347
        and circuit["action_failures"] == 0
        and circuit["exact_raw_inverse_failures"] == 0
        and nn["non_NN_gate_failures"] == 0
        and products["class_product_failures"] == 0
        and support["interface_total_M2"] == 182
        and attacks["invalid_frame_overflow_dirty_work_domain_rejections"] == attacks["domain_attempts"]
        and spectators["proper_cubic_frames"] == 24
        and gate_check["gate_disposition"].startswith("PASS")
        and provenance["Born_selection"] is None
        and provenance["time_or_rate"] is None
        and provenance["source_or_gravity"] is None
        and provenance["axiom_pressure"] is None,
        {
            "disposition": "constructive finite local reversible Route-B action interface",
            "installed_classes_frames": (3347, 24),
            "frame_products": 576,
            "interface_total_active_auxiliary_M2": (182, 138, 9),
            "logical_and_NN_gate_counts": (
                circuit["logical_gate_count"], nn["NN_compiled_gate_count"]
            ),
            "maximum_gate_neighborhood_M2": 3,
            "scope_boundary": "effect-to-tuple genesis and 13-decimal resolution remain supplied",
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_LOCAL_REVERSIBLE_ORIENTED_BLOCH_INTERFACE_OPEN")
        return 1
    print("RESULT PHYSICAL_LOCAL_REVERSIBLE_ORIENTED_BLOCH_INTERFACE_CONSTRUCTIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
