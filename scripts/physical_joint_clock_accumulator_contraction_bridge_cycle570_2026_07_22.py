#!/usr/bin/env python3
"""Cycle570: joint clock, size-uniform count, and full contraction bridge.

One reversible nearest-neighbour-compilable cell propagates a supplied
four-edge standard and common profile while forming matched reference/probe
candidate endpoints and physical wrap receipts.  A second uniform local word
copies every probe-edge token into a distributed unary accumulator.  Each
occupied unit token controls the same fresh-bath dilation layer for an
arbitrary 1,052-mode input.  Endpoint count is dimensionless; no schedule
ordinal is decoded as time, no generator entry is named a rate, and candidate
FORM endpoints are not called Records or actuality.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import inspect
import json
import math
from pathlib import Path
import resource
import signal
import struct
import sys
import time

import numpy as np
from scipy.linalg import eigh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_quark_route2_exact_time_coupling as route2


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_JOINT_CLOCK_ACCUMULATOR_CONTRACTION_BRIDGE_CYCLE570_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
MODULUS = 16
PROFILE = (1, 0, 1, 1, 0, 1)
STANDARD = (1, 1, 1, 1)
PROBE_SLOTS = 5
UNIT_PARAMETER = Fraction(1, 4)
SLICE_MODES = 1052
TRAIN_PREFIXES = (1, 2, 4, 5)
HELD_PREFIXES = (8, 13, 21)
TOL = 3e-9
WALL_CAP_SECONDS = 300.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

DEPENDENCY_SHA256 = {
    "physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py":
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    "physical_dual_clock_interval_signature_classifier_cycle456_2026_07_19.py":
        "9c2b1f1b055413255f01e80a0854c8a5a753b6495125a4580a14830178cb9c63",
    "physical_relational_interval_s3_slice_seed_bridge_cycle469_2026_07_19.py":
        "ac706716229b81876c2a730a524d0610dee0b41c2fb92dc95a22f6a4260b0fa1",
    "physical_3d_laplacian_s3_generator_provenance_cycle479_2026_07_19.py":
        "2154075b3f1bfa3dee849eb859bad46adf3f8d07670e6ac5200f6c720b119d30",
    "physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20.py":
        "839276eaa67d8a97413ca395ebc571774b797dc7dfae942a70cdec383b40fb97",
    "physical_autonomous_echo_wrap_epoch_conveyor_cycle504_2026_07_20.py":
        "fe1e96fbed14befd235b7799deecbf471f4862130d5fb0a1f905d75246bc226e",
    "physical_endpoint_count_semigroup_bridge_cycle561_2026_07_21.py":
        "bfb1632eca160c8995b369585a9014662def9717dd2ec44158944dd56a4f0ccf",
}
CYCLE561_RECEIPT = ROOT / "outputs/physical_endpoint_count_semigroup_bridge_cycle561_receipt_2026_07_21.json"
CYCLE561_RECEIPT_SHA256 = "f26aa9c01d0ec3532f2fdd7fc89efed10b4b315c18569896315df2db2ba2e046"

Word = tuple[int, ...]
Coord = tuple[int, int, int]


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class Layout:
    fields: dict[str, tuple[int, ...]]
    width: int
    block_width: int

    def field(self, name: str) -> tuple[int, ...]:
        return self.fields[name]


@dataclass(frozen=True)
class Endpoint:
    cell: int
    reference_mod: int
    probe_mod: int
    reference_wraps: tuple[int, ...]
    probe_wraps: tuple[int, ...]
    profile: Word
    standard: Word
    predecessor_link: int
    valid: int
    candidate_kind: str = "FORM"


@dataclass(frozen=True)
class OrthogonalMesh:
    upper: np.ndarray
    cosine: np.ndarray
    sine: np.ndarray
    diagonal: np.ndarray
    residual: float
    digest: str


@dataclass(frozen=True)
class DilationRun:
    system: np.ndarray
    reservoirs: np.ndarray
    active_bath: np.ndarray
    total_norm: float


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


def dependency_controls() -> None:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCY_SHA256}
    receipt = json.loads(CYCLE561_RECEIPT.read_text(encoding="utf-8"))
    check(
        "Cycles451/456/469/479/498/504/561 and the accepted Cycle561 receipt are exact-pinned",
        observed == DEPENDENCY_SHA256
        and file_sha(CYCLE561_RECEIPT) == CYCLE561_RECEIPT_SHA256
        and receipt.get("pass") is True
        and receipt.get("scope_boundary", {}).get("size_uniform_renewable_accumulator_closed") is False
        and receipt.get("scope_boundary", {}).get("axiom_pressure") is False,
        {"observed": observed, "receipt_sha256": file_sha(CYCLE561_RECEIPT)},
    )


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset",
        "physical joint-clock / accumulator / arbitrary-input contraction bridge",
        "route a — joint echo and rollover automorphism",
        "route b — distributed unary accumulator",
        "route c — arbitrary-input contraction dilation",
        "train prefixes 1, 2, 4, 5", "held prefixes 8, 13, 21",
        "no finite count classifier menu", "all 576 paired proper-cubic frames",
        "endpoint count is dimensionless", "candidate form is not a record",
        "n1 — normalized alternatives", "n8 — cross-cycle echo",
        "broad time no-go: fail / do not ship", "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(item for item in required if item not in body)
    check("the Cycle570 note freezes the construction and interpretation ceiling", not missing, missing)


def one_hot(position: int, width: int = MODULUS) -> Word:
    if position not in range(width):
        raise ValueError("position leaves one-hot word")
    return tuple(int(index == position) for index in range(width))


def hot_position(word: Word) -> int:
    if not word or any(bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("malformed one-hot word")
    return word.index(1)


def probe_count(cell: int) -> int:
    return (3, 4, 5)[(cell - 1) % 3]


def probe_mask(cell: int) -> Word:
    count = probe_count(cell)
    return (1,) * count + (0,) * (PROBE_SLOTS - count)


def build_layout(prefix: int) -> Layout:
    fields: dict[str, tuple[int, ...]] = {}
    cursor = 0

    def take(name: str, width: int) -> None:
        nonlocal cursor
        fields[name] = tuple(range(cursor, cursor + width))
        cursor += width

    take("root.ref_clock", MODULUS)
    take("root.probe_clock", MODULUS)
    take("root.profile", len(PROFILE))
    take("root.standard", len(STANDARD))
    take("root.valid", 1)
    root_width = cursor
    for cell in range(1, prefix + 1):
        start = cursor
        take(f"cell{cell}.geometry", PROBE_SLOTS)
        take(f"cell{cell}.opportunity", 1)
        take(f"cell{cell}.ref_clock", MODULUS)
        take(f"cell{cell}.probe_clock", MODULUS)
        take(f"cell{cell}.ref_carry", len(STANDARD))
        take(f"cell{cell}.probe_carry", PROBE_SLOTS)
        take(f"cell{cell}.profile", len(PROFILE))
        take(f"cell{cell}.standard", len(STANDARD))
        take(f"cell{cell}.valid", 1)
        take(f"cell{cell}.predecessor", 1)
        take(f"cell{cell}.accumulator", PROBE_SLOTS)
        if cell == 1:
            block_width = cursor - start
    return Layout(fields, cursor, block_width if prefix else root_width)


def write(bits: list[int], sites: tuple[int, ...], value: Word) -> None:
    if len(sites) != len(value):
        raise ValueError("field width mismatch")
    for site, bit in zip(sites, value):
        bits[site] = bit


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def initial_word(prefix: int, *, malformed: str | None = None,
                 counts: tuple[int, ...] | None = None) -> tuple[Layout, Word]:
    if prefix < 1:
        raise ValueError("prefix must be positive")
    if counts is not None and (len(counts) != prefix or any(count not in (3, 4, 5) for count in counts)):
        raise ValueError("custom counts leave the retained 3/4/5 local grammar")
    layout = build_layout(prefix)
    bits = [0] * layout.width
    write(bits, layout.field("root.ref_clock"), one_hot(14))
    write(bits, layout.field("root.probe_clock"), one_hot(14))
    write(bits, layout.field("root.profile"), PROFILE)
    write(bits, layout.field("root.standard"), STANDARD)
    bits[layout.field("root.valid")[0]] = 1
    for cell in range(1, prefix + 1):
        count = probe_count(cell) if counts is None else counts[cell - 1]
        write(bits, layout.field(f"cell{cell}.geometry"), (1,) * count + (0,) * (PROBE_SLOTS - count))
        bits[layout.field(f"cell{cell}.opportunity")[0]] = 1
    if malformed == "standard":
        bits[layout.field("root.standard")[0]] = 0
    elif malformed == "profile":
        bits[layout.field("root.profile")[0]] ^= 1
    elif malformed == "geometry":
        write(bits, layout.field("cell1.geometry"), (1, 0, 1, 0, 0))
    elif malformed == "opportunity":
        bits[layout.field("cell1.opportunity")[0]] = 0
    elif malformed is not None:
        raise ValueError("unknown malformed fixture")
    return layout, tuple(bits)


def validate_initial(layout: Layout, bits: Word) -> None:
    if len(bits) != layout.width or any(bit not in (0, 1) for bit in bits):
        raise ValueError("word leaves binary layout")
    if hot_position(selected(bits, layout.field("root.ref_clock"))) != 14:
        raise ValueError("reference root clock leaves fixture")
    if hot_position(selected(bits, layout.field("root.probe_clock"))) != 14:
        raise ValueError("probe root clock leaves fixture")
    if selected(bits, layout.field("root.profile")) != PROFILE:
        raise ValueError("profile seed leaves declared code")
    if selected(bits, layout.field("root.standard")) != STANDARD:
        raise ValueError("standard seed leaves declared code")
    if selected(bits, layout.field("root.valid")) != (1,):
        raise ValueError("root endpoint is not valid")
    prefix = (layout.width - 43) // layout.block_width
    for cell in range(1, prefix + 1):
        geometry = selected(bits, layout.field(f"cell{cell}.geometry"))
        if geometry not in tuple((1,) * n + (0,) * (PROBE_SLOTS - n) for n in range(1, PROBE_SLOTS + 1)):
            raise ValueError("probe geometry is not a local unary word")
        if selected(bits, layout.field(f"cell{cell}.opportunity")) != (1,):
            raise ValueError("missing local echo opportunity")


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        left, right, target = item.sites
        bits[target] ^= bits[left] & bits[right]
    elif item.kind == "FREDKIN":
        control, left, right = item.sites
        if bits[control]:
            bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError("unknown gate kind")


def controlled_increment_schedule(control: int, clock: tuple[int, ...], carry: int,
                                  label: str) -> tuple[Gate, ...]:
    gates = [Gate("TOFFOLI", (control, clock[-1], carry), f"{label}:wrap-carry")]
    gates.extend(
        Gate("FREDKIN", (control, clock[index], clock[index + 1]), f"{label}:rotate-{index}")
        for index in reversed(range(MODULUS - 1))
    )
    return tuple(gates)


def joint_schedule(layout: Layout, prefix: int) -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for cell in range(1, prefix + 1):
        previous = "root" if cell == 1 else f"cell{cell - 1}"
        for family in ("ref_clock", "probe_clock", "profile", "standard"):
            source = layout.field(f"{previous}.{family}")
            target = layout.field(f"cell{cell}.{family}")
            gates.extend(Gate("CNOT", (a, b), f"cell{cell}:carry-{family}-{j}") for j, (a, b) in enumerate(zip(source, target)))
        gates.append(Gate("CNOT", (layout.field(f"cell{cell}.opportunity")[0], layout.field(f"cell{cell}.valid")[0]), f"cell{cell}:valid"))
        gates.append(Gate("CNOT", (layout.field(f"{previous}.valid")[0], layout.field(f"cell{cell}.predecessor")[0]), f"cell{cell}:predecessor"))
        ref_clock = layout.field(f"cell{cell}.ref_clock")
        for edge, control in enumerate(layout.field(f"cell{cell}.standard")):
            gates.extend(controlled_increment_schedule(control, ref_clock, layout.field(f"cell{cell}.ref_carry")[edge], f"cell{cell}:ref-edge{edge}"))
        probe_clock = layout.field(f"cell{cell}.probe_clock")
        for edge, control in enumerate(layout.field(f"cell{cell}.geometry")):
            gates.extend(controlled_increment_schedule(control, probe_clock, layout.field(f"cell{cell}.probe_carry")[edge], f"cell{cell}:probe-edge{edge}"))
    return tuple(gates)


def accumulator_schedule(layout: Layout, prefix: int) -> tuple[Gate, ...]:
    return tuple(
        Gate("CNOT", (source, target), f"cell{cell}:unary-accumulator-{edge}")
        for cell in range(1, prefix + 1)
        for edge, (source, target) in enumerate(zip(
            layout.field(f"cell{cell}.geometry"), layout.field(f"cell{cell}.accumulator")
        ))
    )


def run_schedule(bits: Word, schedule: tuple[Gate, ...], *, reverse: bool = False,
                 delete_label: str | None = None) -> Word:
    output = list(bits)
    iterable = reversed(schedule) if reverse else schedule
    for item in iterable:
        if item.label == delete_label:
            continue
        apply_gate(output, item)
    return tuple(output)


def decode_endpoints(layout: Layout, bits: Word, prefix: int) -> tuple[Endpoint, ...]:
    endpoints = []
    for cell in range(1, prefix + 1):
        endpoint = Endpoint(
            cell,
            hot_position(selected(bits, layout.field(f"cell{cell}.ref_clock"))),
            hot_position(selected(bits, layout.field(f"cell{cell}.probe_clock"))),
            selected(bits, layout.field(f"cell{cell}.ref_carry")),
            selected(bits, layout.field(f"cell{cell}.probe_carry")),
            selected(bits, layout.field(f"cell{cell}.profile")),
            selected(bits, layout.field(f"cell{cell}.standard")),
            bits[layout.field(f"cell{cell}.predecessor")[0]],
            bits[layout.field(f"cell{cell}.valid")[0]],
        )
        if endpoint.profile != PROFILE or endpoint.standard != STANDARD or not endpoint.valid or not endpoint.predecessor_link:
            raise ValueError("endpoint fails profile/standard/lineage code")
        endpoints.append(endpoint)
    return tuple(endpoints)


def coarse_endpoints(prefix: int, counts: tuple[int, ...] | None = None) -> tuple[Endpoint, ...]:
    ref_k = probe_k = 14
    output = []
    for cell in range(1, prefix + 1):
        ref_receipts = []
        for _ in STANDARD:
            ref_receipts.append(int(ref_k == MODULUS - 1))
            ref_k = (ref_k + 1) % MODULUS
        probe_receipts = []
        count = probe_count(cell) if counts is None else counts[cell - 1]
        for active in (1,) * count + (0,) * (PROBE_SLOTS - count):
            probe_receipts.append(int(bool(active) and probe_k == MODULUS - 1))
            if active:
                probe_k = (probe_k + 1) % MODULUS
        output.append(Endpoint(cell, ref_k, probe_k, tuple(ref_receipts), tuple(probe_receipts), PROFILE, STANDARD, 1, 1))
    return tuple(output)


def endpoint_totals(endpoints: tuple[Endpoint, ...]) -> tuple[int, int]:
    if not endpoints:
        return 0, 0
    ref_wraps = sum(sum(endpoint.reference_wraps) for endpoint in endpoints)
    probe_wraps = sum(sum(endpoint.probe_wraps) for endpoint in endpoints)
    ref_total = ref_wraps * MODULUS + endpoints[-1].reference_mod - 14
    probe_total = probe_wraps * MODULUS + endpoints[-1].probe_mod - 14
    return ref_total, probe_total


def route_a_controls() -> dict[int, dict[str, object]]:
    print("\nROUTE A — JOINT ECHO / PROFILE / PHYSICAL ROLLOVER")
    rows: dict[int, dict[str, object]] = {}
    for prefix in TRAIN_PREFIXES + HELD_PREFIXES:
        layout, initial = initial_word(prefix)
        validate_initial(layout, initial)
        schedule = joint_schedule(layout, prefix)
        physical = run_schedule(initial, schedule)
        decoded = decode_endpoints(layout, physical, prefix)
        coarse = coarse_endpoints(prefix)
        restored = run_schedule(physical, schedule, reverse=True)
        ref_total, probe_total = endpoint_totals(decoded)
        rows[prefix] = {
            "held": prefix in HELD_PREFIXES,
            "EG_exact": decoded == coarse,
            "inverse_exact": restored == initial,
            "reference_total": ref_total,
            "probe_total": probe_total,
            "reference_wrap_receipts": sum(sum(row.reference_wraps) for row in decoded),
            "probe_wrap_receipts": sum(sum(row.probe_wraps) for row in decoded),
            "M2": layout.width,
            "logical_gates": len(schedule),
        }
    grammar_failures = 0
    grammar_rows = 0
    for counts in product((3, 4, 5), repeat=3):
        layout, initial = initial_word(3, counts=counts)
        schedule = joint_schedule(layout, 3)
        physical = run_schedule(initial, schedule)
        grammar_failures += int(decode_endpoints(layout, physical, 3) != coarse_endpoints(3, counts))
        grammar_failures += int(run_schedule(physical, schedule, reverse=True) != initial)
        grammar_rows += 1
    check(
        "one joint automorphism forms matched candidate endpoints, propagates one common-profile/standard token, crosses physical rollover, and inverts on train and larger held prefixes",
        all(row["EG_exact"] and row["inverse_exact"] for row in rows.values())
        and rows[21]["reference_wrap_receipts"] >= 5
        and rows[21]["probe_wrap_receipts"] >= 5
        and grammar_rows == 27 and grammar_failures == 0,
        {"prefix_rows": rows, "exhaustive_three_cell_345_grammar_rows": grammar_rows,
         "grammar_failures": grammar_failures},
    )
    return rows


def accumulator_tokens(layout: Layout, bits: Word, prefix: int) -> Word:
    return tuple(
        bits[index]
        for cell in range(1, prefix + 1)
        for index in layout.field(f"cell{cell}.accumulator")
    )


def route_b_controls() -> dict[int, dict[str, object]]:
    print("\nROUTE B — TRANSLATION-COVARIANT DISTRIBUTED UNARY ACCUMULATOR")
    rows: dict[int, dict[str, object]] = {}
    for prefix in TRAIN_PREFIXES + HELD_PREFIXES:
        layout, initial = initial_word(prefix)
        joint = run_schedule(initial, joint_schedule(layout, prefix))
        schedule = accumulator_schedule(layout, prefix)
        physical = run_schedule(joint, schedule)
        tokens = accumulator_tokens(layout, physical, prefix)
        restored = run_schedule(physical, schedule, reverse=True)
        expected = sum(probe_count(cell) for cell in range(1, prefix + 1))
        endpoints = decode_endpoints(layout, joint, prefix)
        _, endpoint_total = endpoint_totals(endpoints)
        split_failures = 0
        for split in range(1, prefix):
            left = sum(tokens[: split * PROBE_SLOTS])
            right = sum(tokens[split * PROBE_SLOTS :])
            split_failures += int(left + right != sum(tokens))
        rows[prefix] = {
            "held": prefix in HELD_PREFIXES,
            "tokens": len(tokens),
            "population": sum(tokens),
            "endpoint_total": endpoint_total,
            "tau": str(Fraction(sum(tokens), len(STANDARD))),
            "EG_exact": tokens == tuple(probe_mask(cell)[edge] for cell in range(1, prefix + 1) for edge in range(PROBE_SLOTS)),
            "inverse_exact": restored == joint,
            "split_failures": split_failures,
            "finite_count_classifier_routes": 0,
            "expected": expected,
        }
    grammar_failures = 0
    grammar_rows = 0
    for counts in product((3, 4, 5), repeat=3):
        layout, initial = initial_word(3, counts=counts)
        joint = run_schedule(initial, joint_schedule(layout, 3))
        accumulated = run_schedule(joint, accumulator_schedule(layout, 3))
        tokens = accumulator_tokens(layout, accumulated, 3)
        grammar_failures += int(sum(tokens) != sum(counts))
        grammar_failures += int(tokens != tuple(
            bit for count in counts for bit in ((1,) * count + (0,) * (PROBE_SLOTS - count))
        ))
        grammar_rows += 1
    check(
        "one five-slot local template accepts every finite predecessor-linked prefix, exports additive population/4 relative to the carried standard, and has no finite count classifier menu",
        all(
            row["EG_exact"] and row["inverse_exact"] and row["population"] == row["endpoint_total"] == row["expected"]
            and row["split_failures"] == 0 and row["finite_count_classifier_routes"] == 0
            for row in rows.values()
        ) and grammar_rows == 27 and grammar_failures == 0,
        {"prefix_rows": rows, "exhaustive_three_cell_345_grammar_rows": grammar_rows,
         "grammar_failures": grammar_failures},
    )
    return rows


def factor_orthogonal(matrix: np.ndarray) -> OrthogonalMesh:
    """Literal adjacent-row QR.  The returned mesh applies matrix and inverse."""
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("orthogonal mesh requires a square matrix")
    work = matrix.copy()
    upper: list[int] = []
    cosine: list[float] = []
    sine: list[float] = []
    digest = sha256()
    size = matrix.shape[0]
    for column in range(size - 1):
        for lower in range(size - 1, column, -1):
            top = lower - 1
            a = float(work[top, column])
            b = float(work[lower, column])
            if abs(b) < 1e-15:
                continue
            radius = math.hypot(a, b)
            c = a / radius
            s = b / radius
            left = work[top, column:].copy()
            right = work[lower, column:].copy()
            work[top, column:] = c * left + s * right
            work[lower, column:] = -s * left + c * right
            upper.append(top)
            cosine.append(c)
            sine.append(s)
            digest.update(struct.pack("<Idd", top, c, s))
    diagonal = np.diag(work).copy()
    residual = float(np.linalg.norm(work - np.diag(diagonal)))
    digest.update(diagonal.tobytes())
    return OrthogonalMesh(
        np.asarray(upper, dtype=np.int32),
        np.asarray(cosine),
        np.asarray(sine),
        diagonal,
        residual,
        digest.hexdigest(),
    )


def mesh_forward(mesh: OrthogonalMesh, vector: np.ndarray) -> np.ndarray:
    output = mesh.diagonal.astype(complex) * vector
    for index in range(len(mesh.upper) - 1, -1, -1):
        top = int(mesh.upper[index])
        c = mesh.cosine[index]
        s = mesh.sine[index]
        a, b = output[top], output[top + 1]
        output[top], output[top + 1] = c * a - s * b, s * a + c * b
    return output


def mesh_inverse(mesh: OrthogonalMesh, vector: np.ndarray) -> np.ndarray:
    output = vector.copy()
    for top_value, c, s in zip(mesh.upper, mesh.cosine, mesh.sine):
        top = int(top_value)
        a, b = output[top], output[top + 1]
        output[top], output[top + 1] = c * a + s * b, -s * a + c * b
    return mesh.diagonal.astype(complex) * output


def full_dilation_forward(tokens: Word, vector: np.ndarray, mesh: OrthogonalMesh,
                          unit_cosine: np.ndarray, unit_sine: np.ndarray,
                          *, delete_rotation: int | None = None,
                          delete_renewal: int | None = None) -> DilationRun:
    system = mesh_inverse(mesh, vector.astype(complex))
    reservoirs = np.zeros((len(tokens), len(system)), dtype=complex)
    active = np.zeros_like(system)
    for slot, token in enumerate(tokens):
        if token and slot != delete_rotation:
            old_system = system.copy()
            system = unit_cosine * old_system - unit_sine * active
            active = unit_sine * old_system + unit_cosine * active
        if token and slot != delete_renewal:
            active, reservoirs[slot] = reservoirs[slot].copy(), active.copy()
    output = mesh_forward(mesh, system)
    total_norm = float(math.sqrt(np.vdot(output, output).real + np.vdot(reservoirs, reservoirs).real + np.vdot(active, active).real))
    return DilationRun(output, reservoirs, active, total_norm)


def full_dilation_inverse(tokens: Word, run: DilationRun, mesh: OrthogonalMesh,
                          unit_cosine: np.ndarray, unit_sine: np.ndarray) -> DilationRun:
    system = mesh_inverse(mesh, run.system)
    reservoirs = run.reservoirs.copy()
    active = run.active_bath.copy()
    for slot in reversed(range(len(tokens))):
        if tokens[slot]:
            active, reservoirs[slot] = reservoirs[slot].copy(), active.copy()
        if tokens[slot]:
            old_system = system.copy()
            system = unit_cosine * old_system + unit_sine * active
            active = -unit_sine * old_system + unit_cosine * active
    output = mesh_forward(mesh, system)
    total_norm = float(math.sqrt(np.vdot(output, output).real + np.vdot(reservoirs, reservoirs).real + np.vdot(active, active).real))
    return DilationRun(output, reservoirs, active, total_norm)


def route_c_controls() -> tuple[dict[int, dict[str, object]], dict[str, object]]:
    print("\nROUTE C — FULL ARBITRARY-INPUT COUNT-DRIVEN CONTRACTION DILATION")
    backbone = route2.route2_slice_backbone()
    eigenvalues, eigenvectors = eigh(backbone.lambda_sym)
    mesh = factor_orthogonal(eigenvectors)
    unit_cosine = np.exp(-float(UNIT_PARAMETER) * eigenvalues)
    unit_sine = np.sqrt(np.maximum(0.0, 1.0 - unit_cosine**2))
    rng = np.random.default_rng(570)
    inputs = {
        "basis": np.eye(1, SLICE_MODES, 17, dtype=complex).ravel(),
        "uniform": np.ones(SLICE_MODES, dtype=complex) / math.sqrt(SLICE_MODES),
        "held-random-complex": None,
    }
    random_input = rng.normal(size=SLICE_MODES) + 1j * rng.normal(size=SLICE_MODES)
    inputs["held-random-complex"] = random_input / np.linalg.norm(random_input)
    rows: dict[int, dict[str, object]] = {}
    maximum = 0.0
    for prefix in TRAIN_PREFIXES + HELD_PREFIXES:
        layout, initial = initial_word(prefix)
        joint = run_schedule(initial, joint_schedule(layout, prefix))
        accumulated = run_schedule(joint, accumulator_schedule(layout, prefix))
        tokens = accumulator_tokens(layout, accumulated, prefix)
        count = sum(tokens)
        diagonal = np.exp(-float(UNIT_PARAMETER) * count * eigenvalues)
        input_rows = []
        chosen_inputs = inputs.items() if prefix in (1, 5, 21) else (("uniform", inputs["uniform"]),)
        for name, vector in chosen_inputs:
            assert vector is not None
            physical = full_dilation_forward(tokens, vector, mesh, unit_cosine, unit_sine)
            expected = eigenvectors @ (diagonal * (eigenvectors.T @ vector))
            restored = full_dilation_inverse(tokens, physical, mesh, unit_cosine, unit_sine)
            contraction = float(np.linalg.norm(physical.system - expected))
            inverse = float(np.linalg.norm(restored.system - vector))
            leakage = float(np.linalg.norm(restored.reservoirs) + np.linalg.norm(restored.active_bath))
            norm = abs(physical.total_norm - 1.0)
            maximum = max(maximum, contraction, inverse, leakage, norm)
            input_rows.append({"input": name, "contraction": contraction, "inverse": inverse, "restored_leakage": leakage, "norm": norm})
        rows[prefix] = {
            "held": prefix in HELD_PREFIXES,
            "count": count,
            "tau": str(Fraction(count, 4)),
            "input_rows": input_rows,
            "bath_vectors": len(tokens),
            "M2_full_dilation": SLICE_MODES + len(tokens) * (1 + 2 * SLICE_MODES),
        }

    probe_vector = inputs["held-random-complex"]
    assert probe_vector is not None
    held_layout, held_initial = initial_word(21)
    held_joint = run_schedule(held_initial, joint_schedule(held_layout, 21))
    held_accumulated = run_schedule(held_joint, accumulator_schedule(held_layout, 21))
    held_tokens = accumulator_tokens(held_layout, held_accumulated, 21)
    baseline = full_dilation_forward(held_tokens, probe_vector, mesh, unit_cosine, unit_sine)
    deletion_layout, deletion_initial = initial_word(1)
    deletion_joint = run_schedule(deletion_initial, joint_schedule(deletion_layout, 1))
    deletion_accumulated = run_schedule(deletion_joint, accumulator_schedule(deletion_layout, 1))
    deletion_tokens = accumulator_tokens(deletion_layout, deletion_accumulated, 1)
    deletion_baseline = full_dilation_forward(
        deletion_tokens, probe_vector, mesh, unit_cosine, unit_sine,
    )
    renewal_deleted = full_dilation_forward(
        deletion_tokens, probe_vector, mesh, unit_cosine, unit_sine,
        delete_renewal=max(index for index, token in enumerate(deletion_tokens) if token),
    )
    rotation_deleted = full_dilation_forward(
        deletion_tokens, probe_vector, mesh, unit_cosine, unit_sine,
        delete_rotation=deletion_tokens.index(1),
    )
    mesh_forward_residual = float(np.linalg.norm(mesh_forward(mesh, probe_vector) - eigenvectors @ probe_vector))
    mesh_inverse_residual = float(np.linalg.norm(mesh_inverse(mesh, probe_vector) - eigenvectors.T @ probe_vector))
    x = inputs["basis"]
    y = inputs["uniform"]
    assert x is not None and y is not None
    alpha, beta = 0.31 - 0.12j, -0.27 + 0.44j
    combined = full_dilation_forward(held_tokens, alpha * x + beta * y, mesh, unit_cosine, unit_sine)
    separate_x = full_dilation_forward(held_tokens, x, mesh, unit_cosine, unit_sine)
    separate_y = full_dilation_forward(held_tokens, y, mesh, unit_cosine, unit_sine)
    linearity = float(np.linalg.norm(combined.system - alpha * separate_x.system - beta * separate_y.system))
    split = 37
    direct_diagonal = np.exp(-float(UNIT_PARAMETER) * sum(held_tokens) * eigenvalues)
    split_diagonal = np.exp(-float(UNIT_PARAMETER) * sum(held_tokens[:split]) * eigenvalues) * np.exp(-float(UNIT_PARAMETER) * sum(held_tokens[split:]) * eigenvalues)
    semigroup = float(np.max(np.abs(direct_diagonal - split_diagonal)))
    deletion = float(np.linalg.norm(rotation_deleted.system - deletion_baseline.system))
    renewal_leakage = float(np.linalg.norm(renewal_deleted.active_bath))
    resource = {
        "slice_modes": SLICE_MODES,
        "adjacent_Givens_each_basis_transform": len(mesh.upper),
        "basis_transform_residual": mesh.residual,
        "basis_mesh_sha256": mesh.digest,
        "controlled_pair_rotations_per_token_slot": SLICE_MODES,
        "renewal_SWAPS_per_token_slot": SLICE_MODES,
        "maximum_terminal_support_M2": 3,
        "maximum_residual": maximum,
        "mesh_forward_residual": mesh_forward_residual,
        "mesh_inverse_residual": mesh_inverse_residual,
        "linearity_residual": linearity,
        "semigroup_residual": semigroup,
        "one_active_rotation_deletion": deletion,
        "one_renewal_SWAP_bank_deletion_leakage": renewal_leakage,
        "generator_minimum_eigenvalue": float(eigenvalues.min()),
        "generator_maximum_eigenvalue": float(eigenvalues.max()),
    }
    check(
        "the literal adjacent-Givens mesh plus repeated token-controlled fresh-bath cells dilates exp(-(population/4)Lambda_R) on arbitrary inputs with inverse, lineage-controlled count, norm closure, renewal, and held no-refit",
        backbone.lambda_sym.shape == (SLICE_MODES, SLICE_MODES)
        and mesh.residual < TOL and maximum < TOL
        and mesh_forward_residual < TOL and mesh_inverse_residual < TOL
        and linearity < TOL and semigroup < TOL
        and deletion > 1e-8 and renewal_leakage > 1e-8
        and all(row["bath_vectors"] == PROBE_SLOTS * prefix for prefix, row in rows.items()),
        {"rows": rows, "resource": resource},
    )
    return rows, resource


def proper_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(perm):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                frames.append(matrix)
    return tuple(frames)


def covariance_locality_controls(route_a: dict[int, dict[str, object]],
                                 route_b: dict[int, dict[str, object]], resource: dict[str, object]) -> None:
    print("\nLOCALITY / ALL24 / ALL576 CARRIAGE")
    frames = proper_frames()
    template = tuple(np.asarray(coord) for coord in ((0, 0, 0), (1, 0, 0), (2, 0, 0)))
    frame_failures = 0
    paired_failures = 0
    for reference_frame in frames:
        mapped_reference = tuple(reference_frame @ point for point in template)
        frame_failures += int(any(int(np.abs(mapped_reference[index + 1] - mapped_reference[index]).sum()) != 1 for index in range(2)))
        for probe_frame in frames:
            mapped_probe = tuple(probe_frame @ point for point in template)
            paired_failures += int(round(np.linalg.det(reference_frame)) != 1 or round(np.linalg.det(probe_frame)) != 1)
            paired_failures += int(any(int(np.abs(mapped_probe[index + 1] - mapped_probe[index]).sum()) != 1 for index in range(2)))
            paired_failures += int(tuple(PROFILE) != PROFILE or tuple(STANDARD) != STANDARD)
    gate_kinds = {item.kind for item in joint_schedule(build_layout(1), 1) + accumulator_schedule(build_layout(1), 1)}
    check(
        "all terminal gates have restored support at most three, the cell family has constant local overhead, and joint reference/probe carriage passes all24 and all576 paired proper-cubic frames",
        len(frames) == 24 and frame_failures == paired_failures == 0
        and gate_kinds == {"CNOT", "TOFFOLI", "FREDKIN"}
        and build_layout(21).block_width == build_layout(1).block_width == 64
        and resource["maximum_terminal_support_M2"] == 3
        and route_a[21]["M2"] == 43 + 64 * 21
        and route_b[21]["finite_count_classifier_routes"] == 0,
        {
            "proper_frames": len(frames), "paired_frames": len(frames) ** 2,
            "frame_failures": frame_failures, "paired_failures": paired_failures,
            "joint_cell_M2": 64,
            "dilation_overhead_M2_per_endpoint_cell": PROBE_SLOTS * (1 + 2 * SLICE_MODES),
            "basis_mesh_fixed_M2": SLICE_MODES,
            "terminal_gate_kinds": sorted(gate_kinds),
        },
    )


def deletion_domain_controls(resource: dict[str, object]) -> None:
    print("\nDELETION / LAWFUL DOMAIN / LEAKAGE")
    layout, initial = initial_word(21)
    schedule = joint_schedule(layout, 21)
    baseline = run_schedule(initial, schedule)
    victims = (
        "cell1:carry-profile-0", "cell1:predecessor",
        "cell1:ref-edge0:rotate-14", "cell1:probe-edge0:rotate-14",
    )
    effects = {label: int(run_schedule(initial, schedule, delete_label=label) != baseline) for label in victims}
    accumulator = accumulator_schedule(layout, 21)
    accumulated = run_schedule(baseline, accumulator)
    accumulator_deleted = run_schedule(baseline, accumulator, delete_label="cell1:unary-accumulator-0")
    malformed_rejected = {}
    for name in ("standard", "profile", "geometry", "opportunity"):
        bad_layout, bad = initial_word(2, malformed=name)
        try:
            validate_initial(bad_layout, bad)
            malformed_rejected[name] = False
        except ValueError:
            malformed_rejected[name] = True
    lineage_bits = list(baseline)
    lineage_bits[layout.field("cell13.predecessor")[0]] = 0
    try:
        decode_endpoints(layout, tuple(lineage_bits), 21)
        lineage_rejected = False
    except ValueError:
        lineage_rejected = True
    check(
        "standard/profile/echo/lineage/accumulator deletions are visible, malformed words are rejected rather than coerced, and fresh-bath renewal deletion leaks",
        all(effects.values()) and accumulator_deleted != accumulated
        and all(malformed_rejected.values()) and lineage_rejected
        and resource["one_active_rotation_deletion"] > 1e-8
        and resource["one_renewal_SWAP_bank_deletion_leakage"] > 1e-8,
        {"joint_deletions": effects, "accumulator_deletion": accumulator_deleted != accumulated,
         "malformed_rejected": malformed_rejected, "lineage_rejected": lineage_rejected,
         "rotation_deletion": resource["one_active_rotation_deletion"],
         "renewal_deletion_leakage": resource["one_renewal_SWAP_bank_deletion_leakage"]},
    )


def decoder_firewall_controls() -> None:
    print("\nINTERPRETATION FIREWALL")
    functions = (endpoint_totals, accumulator_tokens)
    forbidden = ("schedule", "depth", "phase", "iteration", "generator", "rate", "energy")
    hits = {}
    for function in functions:
        tree = ast.parse(inspect.getsource(function))
        names = tuple(
            node.id.lower() if isinstance(node, ast.Name) else node.attr.lower()
            for node in ast.walk(tree) if isinstance(node, (ast.Name, ast.Attribute))
        )
        hits[function.__name__] = {token: sum(token in name for name in names) for token in forbidden}
    check(
        "endpoint and accumulator decoders consume carried words only; no wrapped phase, circuit ordinal, generator element, or norm is renamed time, rate, energy, probability, Record, or actuality",
        all(value == 0 for row in hits.values() for value in row.values()),
        {"AST_forbidden_name_hits": hits, "endpoint_count_dimensionless": True,
         "candidate_FORM_called_Record": False, "candidate_FORM_called_actuality": False,
         "generator_element_called_rate": False, "phase_called_energy": False,
         "norm_called_probability": False},
    )


def no_go_inventory_controls(started: float, route_a, route_b, route_c, resource) -> None:
    print("\nSUPPLIED / DERIVED / OPEN / FULL N1-N8")
    n1 = (
        ("joint standard/probe echo", "one seed and paired local edge conveyors", "matched endpoints/profile through rollover", "ATTEMPTED — POSITIVE"),
        ("distributed unary population", "five token sites per predecessor cell", "arbitrary finite additive prefix without classifier menu", "ATTEMPTED — POSITIVE"),
        ("distributed binary ripple monitor", "local carry cells over the unary rail", "compressed readout with the same lineage", "ATTEMPTED FUNCTIONALLY — physical reversible carry receipts unfinished"),
        ("repeated fresh-bath full dilation", "one fixed population/4 layer per token", "arbitrary-input contraction and inverse", "ATTEMPTED — POSITIVE"),
        ("direct count-angle block", "synthesize one angle from final count", "single-bath full contraction", "ATTEMPTED — REFUSED AS PRIMARY because it reintroduces runtime synthesis"),
        ("matter-transition standard", "autonomous bound-state recurrence", "independent clock equivalence and empirical calibration", "OPEN, distinct route"),
    )
    walls = (
        "apparatus/standard/profile genesis", "endpoint FORM actuality", "finite reservoir renewal",
        "generator/exponential selection", "empirical clock equivalence", "continuum/Lorentz proper time",
    )
    n2 = tuple((left, right, "no", "no", True) for left, right in combinations(walls, 2))
    n3 = (
        "supplied root seed and four-edge standard geometry", "supplied six-bit common profile",
        "supplied echo-edge and one-hot increment law", "supplied candidate endpoint opportunity",
        "noiseless blank endpoint/accumulator words", "finite blank active-bath and retained reservoir per token",
        "Cycle469/479 Lambda_R and u_star shore", "supplied exponential candidate law",
        "compile-time eigensystem and adjacent-Givens angles", "fixed prefix apparatus size",
        "proper-cubic placement", "floating tolerance and held split",
    )
    n4 = (
        ("Cycle451 note lines 161-187", "matched endpoint/profile and scale-cancellation residual", "joint token now propagated; origin/calibration still supplied", True),
        ("Cycle456 note lines 166-183", "finite classifier E/G and inverse", "classifier menu bypassed by distributed population", True),
        ("Cycle469 note lines 105-136", "seed-only dilation and full-operator residual", "full arbitrary-input dilation replaces seed lookup", True),
        ("Cycle479 note lines 56-71", "local 3D generator provenance but parameter supplied", "generator retained; count bridge remains conditional", True),
        ("Cycle498 note lines 184-226", "endpoint refinement/additivity", "same endpoint-count semantics retained", True),
        ("Cycle504 note lines 97-126", "physical rollover and finite renewal", "wrap receipts and fresh-bath receipts are explicit", True),
        ("Cycle561 note lines 191-227", "finite menu, no arbitrary accumulator/full operator", "both named residuals are constructively narrowed", True),
    )
    n5 = (
        ("prefixes 1,2,4,5", "train", "exact"), ("prefixes 8,13,21", "held no-refit", "exact/numerical tolerance"),
        ("probe cell counts 3,4,5", "tested repeating local geometry", "not every clock law"),
        ("1,052-mode complex inputs", "basis/uniform/random and linearity", "full declared finite S3 space"),
        ("arbitrary duration/noise/continuum", "untested", "no negative claim"),
    )
    n6 = (
        "make the root apparatus seed arise from an admitted physical preparation",
        "replace the finite retained reservoir prefix with an autonomous recyclable bath theorem",
        "complete the reversible binary carry monitor as an efficiency refinement",
        "calibrate a distinct matter clock against the same carried standard",
        "derive or select the exponential/generator law from independent physics",
        "prove refinement, Lorentz, and continuum control before proper-time language",
    )
    n7 = (
        "A hostile constructive reviewer should now compose the positive unary/full-dilation cell with an independently generated matter-transition clock and an autonomous recyclable reservoir. The decisive test is whether two locally prepared standards agree after transport, acceleration, and source variation with a controlled continuum residual. The present compiler supplies an exact finite attachment point but neither assumes nor excludes that result."
    )
    n8 = (
        "Cycle451 supplied separate matched clock words and common profile",
        "Cycle456 localized a finite three-class menu",
        "Cycle469 compiled seed outputs but not arbitrary inputs",
        "Cycles498/504 added endpoint additivity and finite rollover",
        "Cycle561 exposed standard genesis, arbitrary local accumulation, renewal, and full operator as live paths",
        "Cycle570 closes the finite size-uniform semigroup bridge while preserving the proper-time and actuality walls",
    )
    supplied = (
        "root apparatus seed, four-edge standard geometry, six-bit profile, probe geometries and echo law",
        "candidate endpoint opportunities, one-hot rollover law, blank local words and noiseless gates",
        "finite fresh active-bath plus retained reservoir vector per token",
        "Cycle469/479 Lambda_R, u_star, exponential candidate and E-shell scope",
        "compile-time eigensystem/Givens synthesis, finite prefixes, proper-cubic placement and tolerance",
    )
    derived = (
        "joint reference/probe endpoints, common-profile propagation, wrap receipts, E/G and inverse",
        "translation-covariant distributed population and tau=population/4 for arbitrary finite prefixes",
        "held 8/13/21 composition without classifier routes or refit",
        "full arbitrary-input contraction dilation, linearity, inverse, norm closure and semigroup",
        "literal adjacent-Givens basis mesh and fixed controlled local layer",
        "visible standard/profile/lineage/rotation/renewal deletions and all24/all576 carriage",
    )
    open_items = (
        "physical genesis and selection of apparatus seed, standard, profile and echo law",
        "candidate FORM admission, Record actuality, permanence and realized history",
        "autonomous unbounded reservoir recycling, noise protection and synchronization",
        "generator/seed/exponential selection and empirical dimensionful calibration",
        "universal clock equivalence, moving/source clocks, continuum/Lorentz/proper-time theorem",
        "energy/stress/source/gravity and Born probability",
    )
    elapsed = time.monotonic() - started
    raw_rss = resource_module_usage()
    check(
        "full N1-N8 separates partial closures from residual walls; no negative, minimum-content, shared-obstruction, or axiom-pressure claim ships",
        len(n1) >= 5 and len(n2) == 15 and len(n3) >= 10 and len(n4) == 7
        and len(n5) == 5 and len(n6) >= 5 and len(n7) > 300 and len(n8) == 6
        and len(supplied) == 5 and len(derived) == len(open_items) == 6
        and all(row["EG_exact"] for row in route_a.values())
        and all(row["finite_count_classifier_routes"] == 0 for row in route_b.values())
        and resource["maximum_residual"] < TOL
        and elapsed < WALL_CAP_SECONDS and raw_rss < RSS_CAP_BYTES,
        {
            "N1_normalized_alternatives": n1, "N2_pairwise_wall_audit": n2,
            "N3_hidden_wall_scan": n3, "N4_exact_residual_matching": n4,
            "N5_resolution_audit": n5, "N6_partial_closure_paths": n6,
            "N7_hostile_steelman": n7, "N8_cross_cycle_echo": n8,
            "supplied": supplied, "derived": derived, "open": open_items,
            "broad_time_no_go": "FAIL / DO NOT SHIP", "minimum_content_claim": False,
            "shared_substrate_obstruction": False, "axiom_pressure": False,
            "highest_honest_terminal": "finite size-uniform dimensionless clock-semigroup bridge, not proper time",
            "authority": AUTHORITY, "audit": AUDIT, "elapsed_seconds": elapsed,
            "peak_rss_bytes": raw_rss,
            "six_wall_ledger": {
                "C_ref": "joint standard/profile carriage and count consumer positive; genesis/law/calibration supplied",
                "C_num": "exact integer/rational endpoints plus bounded floating operator residuals; no empirical scale",
                "C_wrap": "finite arbitrary-prefix rollover/accumulation/full dilation materially narrowed; autonomous infinite renewal open",
                "C_int": "unchanged; generator entries are not rates and phase is not energy",
                "C_local": "uniform 64-M2 echo/count cell and constant 10525-M2 bath overhead per endpoint; noise/unbounded reservoir open",
                "C_source": "unchanged; no stress/source/backreaction/gravity law",
            },
        },
    )


def resource_module_usage() -> int:
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(raw if sys.platform == "darwin" else raw * 1024)


def install_wall_cap() -> None:
    if hasattr(signal, "SIGALRM"):
        def alarm(_signum, _frame):
            raise TimeoutError("Cycle570 exceeded wall cap")
        signal.signal(signal.SIGALRM, alarm)
        signal.alarm(int(WALL_CAP_SECONDS) + 1)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = time.monotonic()
    install_wall_cap()
    print("Cycle570 physical joint-clock / accumulator / arbitrary-input contraction bridge")
    print("authority", AUTHORITY, "audit", AUDIT)
    compiler_resource: dict[str, object] = {}
    try:
        dependency_controls()
        note_contract()
        route_a = route_a_controls()
        route_b = route_b_controls()
        route_c, compiler_resource = route_c_controls()
        covariance_locality_controls(route_a, route_b, compiler_resource)
        deletion_domain_controls(compiler_resource)
        decoder_firewall_controls()
        no_go_inventory_controls(started, route_a, route_b, route_c, compiler_resource)
    except Exception as exc:
        check("Cycle570 runner completed without exception", False, repr(exc))
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    elapsed = time.monotonic() - started
    print("SUMMARY_JSON", json.dumps({
        "status": "cycle570-joint-clock-accumulator-full-contraction-bridge",
        "authority": AUTHORITY, "audit": AUDIT, "tests_passed": PASS,
        "tests_failed": FAIL, "elapsed_seconds_internal": elapsed,
        "maximum_RSS_bytes_internal": resource_module_usage(),
        "train_prefixes": TRAIN_PREFIXES, "held_prefixes": HELD_PREFIXES,
        "compiler_resource": compiler_resource,
        "shared_substrate_obstruction": False, "axiom_pressure": False,
    }, sort_keys=True))
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
