#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 all seam physical source, part 1/5."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
PART_ORDINAL = 1
PART_COUNT = 5
FIRST_SOURCE_LINE = 1
LAST_SOURCE_LINE = 563
TOTAL_SOURCE_LINES = 2038
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 000001|#!/usr/bin/env python3
# C873SRC 000002|"""Cycle873 physical core: recurrent F17-only all-seam augmentation.
# C873SRC 000003|
# C873SRC 000004|The load-bearing object is the 20-M2 F17-only bank on every landed Cycle870
# C873SRC 000005|directed seam: three clean returned work sites plus a persistent 17-rail unary
# C873SRC 000006|link.  The core emits the actual selected seam, exact H/T/CNOT controlled
# C873SRC 000007|cyclic shifts, returned nearest-neighbour routes, and the fixed 24-colour
# C873SRC 000008|all-seam schedule on the L2, L3, and held 3x2x2 open boxes.
# C873SRC 000009|
# C873SRC 000010|Cycle714 packet coexistence is retained as an explicit secondary diagnostic
# C873SRC 000011|because its primitive library also supplies the H/T/CNOT matrices used here.
# C873SRC 000012|It is not in the primary failure predicate.  One-hot state preparation,
# C873SRC 000013|admission/genesis, finite synthesis,
# C873SRC 000014|periodic Wilson sectors, source/gravity, time, Record, and Born interpretation
# C873SRC 000015|remain outside this bounded core.
# C873SRC 000016|"""
# C873SRC 000017|
# C873SRC 000018|from __future__ import annotations
# C873SRC 000019|
# C873SRC 000020|from collections import Counter, defaultdict
# C873SRC 000021|from dataclasses import dataclass
# C873SRC 000022|from hashlib import sha256
# C873SRC 000023|from itertools import product
# C873SRC 000024|import argparse
# C873SRC 000025|import json
# C873SRC 000026|import math
# C873SRC 000027|from pathlib import Path
# C873SRC 000028|import subprocess
# C873SRC 000029|import sys
# C873SRC 000030|
# C873SRC 000031|import numpy as np
# C873SRC 000032|
# C873SRC 000033|
# C873SRC 000034|ROOT = Path(__file__).resolve().parents[1]
# C873SRC 000035|sys.path.insert(0, str(ROOT / "scripts"))
# C873SRC 000036|
# C873SRC 000037|import frontier_cycle870_openreference_native_recurrent_update_2026_08_02 as C870
# C873SRC 000038|import frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02 as J870
# C873SRC 000039|import frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02 as C871
# C873SRC 000040|import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as C714
# C873SRC 000041|
# C873SRC 000042|
# C873SRC 000043|Coord = tuple[int, int, int]
# C873SRC 000044|Instruction = C870.c707.Instruction
# C873SRC 000045|F17 = 17
# C873SRC 000046|TOL = 3.0e-10
# C873SRC 000047|SHAPES = ((2, 2, 2), (3, 3, 3), (3, 2, 2))
# C873SRC 000048|EXPECTED_BASE_COMMIT = "c73a11d1ea7ddd564c48aa2a5a459a43d94262ef"
# C873SRC 000049|OUT = ROOT / "outputs/cycle873_recurrent_f17_all_seam_physical_core_receipt_2026_08_03.json"
# C873SRC 000050|
# C873SRC 000051|SOURCE_PATHS = (
# C873SRC 000052|    "scripts/frontier_cycle870_openreference_native_recurrent_update_2026_08_02.py",
# C873SRC 000053|    "scripts/frontier_cycle870_openreference_joined_recurrent_compiler_2026_08_02.py",
# C873SRC 000054|    "scripts/frontier_cycle871_openreference_endpoint_packet_bridge_2026_08_02.py",
# C873SRC 000055|    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
# C873SRC 000056|)
# C873SRC 000057|PRIMARY_SOURCE_PATHS = SOURCE_PATHS
# C873SRC 000058|SECONDARY_OPTIONAL_SOURCE_PATHS = ()
# C873SRC 000059|EXPECTED_SOURCE_SHA256 = {
# C873SRC 000060|    SOURCE_PATHS[0]: "687b22a0bd0fd71fc20e7597443886a4990b49fcef7c80164d5f685210e84237",
# C873SRC 000061|    SOURCE_PATHS[1]: "1b66c061dcb8e0082fd9e7264e78ccbd0f77440c0f517aa93696bde49f78c1bd",
# C873SRC 000062|    SOURCE_PATHS[2]: "6645156635b4354d937759a28e71215121a19cefcc2f294a2791e6a84cf1423b",
# C873SRC 000063|    SOURCE_PATHS[3]: "eb6c9a50681c69ea4fae47724c58d8ba10b48a270e7efa67a811af234afe9a1a",
# C873SRC 000064|}
# C873SRC 000065|
# C873SRC 000066|# A single nearest-neighbour path, expressed in every seam's supplied coframe.
# C873SRC 000067|# It was searched against the live packet, encoded carrier, and preparation
# C873SRC 000068|# banks on all three requested fixtures.  Its radius is the constant two.
# C873SRC 000069|RAIL_LOCAL_OFFSETS: tuple[Coord, ...] = (
# C873SRC 000070|    (-2, 2, 0), (-2, 2, -1), (-1, 2, -1), (-1, 2, -2),
# C873SRC 000071|    (0, 2, -2), (1, 2, -2), (1, 1, -2), (2, 1, -2),
# C873SRC 000072|    (2, 0, -2), (2, -1, -2), (1, -1, -2), (1, -2, -2),
# C873SRC 000073|    (0, -2, -2), (-1, -2, -2), (-1, -2, -1), (-2, -2, -1),
# C873SRC 000074|    (-2, -2, -2),
# C873SRC 000075|)
# C873SRC 000076|
# C873SRC 000077|
# C873SRC 000078|def digest(path: Path) -> str:
# C873SRC 000079|    return sha256(path.read_bytes()).hexdigest()
# C873SRC 000080|
# C873SRC 000081|
# C873SRC 000082|def add(*rows: Coord) -> Coord:
# C873SRC 000083|    return tuple(sum(values) for values in zip(*rows))
# C873SRC 000084|
# C873SRC 000085|
# C873SRC 000086|def sub(left: Coord, right: Coord) -> Coord:
# C873SRC 000087|    return tuple(a - b for a, b in zip(left, right))
# C873SRC 000088|
# C873SRC 000089|
# C873SRC 000090|def scale(value: int, row: Coord) -> Coord:
# C873SRC 000091|    return tuple(value * item for item in row)
# C873SRC 000092|
# C873SRC 000093|
# C873SRC 000094|def l1(left: Coord, right: Coord) -> int:
# C873SRC 000095|    return sum(abs(a - b) for a, b in zip(left, right))
# C873SRC 000096|
# C873SRC 000097|
# C873SRC 000098|def at(midpoint: Coord, basis: tuple[Coord, Coord, Coord], local: Coord) -> Coord:
# C873SRC 000099|    return add(midpoint, *(scale(value, direction) for value, direction in zip(local, basis)))
# C873SRC 000100|
# C873SRC 000101|
# C873SRC 000102|def localize(site: Coord, midpoint: Coord, basis) -> Coord:
# C873SRC 000103|    return C871.coframe_coordinates(sub(site, midpoint), basis)
# C873SRC 000104|
# C873SRC 000105|
# C873SRC 000106|def shape_cells(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
# C873SRC 000107|    return tuple(product(*(range(length) for length in shape)))
# C873SRC 000108|
# C873SRC 000109|
# C873SRC 000110|def matrix_digest(matrix: np.ndarray) -> str:
# C873SRC 000111|    return C870.c707.c655.matrix_digest(matrix)
# C873SRC 000112|
# C873SRC 000113|
# C873SRC 000114|def instruction_signature(row: Instruction):
# C873SRC 000115|    return row.kind, row.sites, matrix_digest(row.matrix)
# C873SRC 000116|
# C873SRC 000117|
# C873SRC 000118|def word_digest(word) -> str:
# C873SRC 000119|    return sha256(repr(tuple(map(instruction_signature, word))).encode()).hexdigest()
# C873SRC 000120|
# C873SRC 000121|
# C873SRC 000122|def json_default(value):
# C873SRC 000123|    if isinstance(value, np.generic):
# C873SRC 000124|        return value.item()
# C873SRC 000125|    if isinstance(value, set | frozenset):
# C873SRC 000126|        return sorted(value)
# C873SRC 000127|    raise TypeError(f"cannot JSON-encode {type(value).__name__}")
# C873SRC 000128|
# C873SRC 000129|
# C873SRC 000130|def json_safe(value):
# C873SRC 000131|    if isinstance(value, dict):
# C873SRC 000132|        return {
# C873SRC 000133|            key if isinstance(key, str | int | float | bool) or key is None else repr(key):
# C873SRC 000134|            json_safe(item)
# C873SRC 000135|            for key, item in value.items()
# C873SRC 000136|        }
# C873SRC 000137|    if isinstance(value, tuple | list | set | frozenset):
# C873SRC 000138|        return [json_safe(item) for item in value]
# C873SRC 000139|    if isinstance(value, np.generic):
# C873SRC 000140|        return value.item()
# C873SRC 000141|    return value
# C873SRC 000142|
# C873SRC 000143|
# C873SRC 000144|@dataclass(frozen=True)
# C873SRC 000145|class IntegratedPlacement:
# C873SRC 000146|    packet: C871.PacketPlacement
# C873SRC 000147|    rails: tuple[Coord, ...]
# C873SRC 000148|    blocked: frozenset[Coord]
# C873SRC 000149|
# C873SRC 000150|    @property
# C873SRC 000151|    def midpoint(self) -> Coord:
# C873SRC 000152|        return self.packet.midpoint
# C873SRC 000153|
# C873SRC 000154|    @property
# C873SRC 000155|    def basis(self):
# C873SRC 000156|        return self.packet.basis
# C873SRC 000157|
# C873SRC 000158|    @property
# C873SRC 000159|    def pointer(self) -> Coord:
# C873SRC 000160|        return self.packet.sites[C714.POINTER]
# C873SRC 000161|
# C873SRC 000162|    @property
# C873SRC 000163|    def q_u(self) -> Coord:
# C873SRC 000164|        return self.packet.sites[C714.MCX_WORK[0]]
# C873SRC 000165|
# C873SRC 000166|    @property
# C873SRC 000167|    def q_v(self) -> Coord:
# C873SRC 000168|        return self.packet.sites[C714.MCX_WORK[1]]
# C873SRC 000169|
# C873SRC 000170|    @property
# C873SRC 000171|    def current(self) -> Coord:
# C873SRC 000172|        return self.packet.sites[C714.MCX_WORK[2]]
# C873SRC 000173|
# C873SRC 000174|    @property
# C873SRC 000175|    def f17_roles(self) -> frozenset[Coord]:
# C873SRC 000176|        return frozenset((self.q_u, self.q_v, self.current, *self.rails))
# C873SRC 000177|
# C873SRC 000178|    @property
# C873SRC 000179|    def bank(self) -> frozenset[Coord]:
# C873SRC 000180|        return frozenset((*self.packet.sites, *self.rails))
# C873SRC 000181|
# C873SRC 000182|    @property
# C873SRC 000183|    def radius(self) -> int:
# C873SRC 000184|        return max(
# C873SRC 000185|            max(map(abs, localize(site, self.midpoint, self.basis)))
# C873SRC 000186|            for site in self.bank
# C873SRC 000187|        )
# C873SRC 000188|
# C873SRC 000189|
# C873SRC 000190|def integrated_placement(graph, context, seam) -> IntegratedPlacement:
# C873SRC 000191|    packet = C871.packet_placement(graph, context, seam)
# C873SRC 000192|    blocked = frozenset(set(context.sites) | J870.auxiliary_registers(graph))
# C873SRC 000193|    rails = tuple(at(packet.midpoint, packet.basis, row) for row in RAIL_LOCAL_OFFSETS)
# C873SRC 000194|    placement = IntegratedPlacement(packet, rails, blocked)
# C873SRC 000195|    if len(placement.f17_roles) != 20:
# C873SRC 000196|        raise AssertionError("20-role F17 bank is not injective")
# C873SRC 000197|    if len(placement.bank) != C714.N + F17:
# C873SRC 000198|        raise AssertionError("packet-plus-rail bank is not 76 distinct M2")
# C873SRC 000199|    if set(rails) & set(packet.sites):
# C873SRC 000200|        raise AssertionError("persistent F17 rail collides with live packet")
# C873SRC 000201|    if placement.bank & blocked:
# C873SRC 000202|        raise AssertionError(("integrated bank collision", placement.bank & blocked))
# C873SRC 000203|    if any(l1(left, right) != 1 for left, right in zip(rails, rails[1:])):
# C873SRC 000204|        raise AssertionError("F17 rail order is not a nearest-neighbour path")
# C873SRC 000205|    if placement.radius > 2:
# C873SRC 000206|        raise AssertionError(("bank radius exceeded", placement.radius))
# C873SRC 000207|    return placement
# C873SRC 000208|
# C873SRC 000209|
# C873SRC 000210|def x_gate(site: Coord, kind: str) -> Instruction:
# C873SRC 000211|    return C871.one(site, C714.X, kind)
# C873SRC 000212|
# C873SRC 000213|
# C873SRC 000214|def primitive_word(a: Coord, b: Coord, target: Coord, prefix: str, *, clean_target=False):
# C873SRC 000215|    rows = list(C714.toffoli_primitives(0, 1, 2))
# C873SRC 000216|    if clean_target:
# C873SRC 000217|        if rows[1] != ("CNOT", (1, 2)):
# C873SRC 000218|            raise AssertionError("landed Toffoli primitive order changed")
# C873SRC 000219|        del rows[1]
# C873SRC 000220|    matrices = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
# C873SRC 000221|    local = (a, b, target)
# C873SRC 000222|    return tuple(
# C873SRC 000223|        Instruction(prefix + kind, tuple(local[index] for index in wires), matrices[kind])
# C873SRC 000224|        for kind, wires in rows
# C873SRC 000225|    )
# C873SRC 000226|
# C873SRC 000227|
# C873SRC 000228|def predicate_compute(q_u: Coord, q_v: Coord, current: Coord, sign: int, prefix: str):
# C873SRC 000229|    negative = q_v if sign > 0 else q_u
# C873SRC 000230|    return (
# C873SRC 000231|        x_gate(negative, prefix + "negative_X"),
# C873SRC 000232|    ) + primitive_word(
# C873SRC 000233|        q_u, q_v, current, prefix + "clean_target_Toffoli_", clean_target=True
# C873SRC 000234|    ) + (x_gate(negative, prefix + "negative_X"),)
# C873SRC 000235|
# C873SRC 000236|
# C873SRC 000237|def predicate_uncompute(q_u: Coord, q_v: Coord, current: Coord, sign: int, prefix: str):
# C873SRC 000238|    # The target now contains the predicate, so the unchanged exact Toffoli is
# C873SRC 000239|    # retained.  Only the two initial, clean-target compute occurrences shrink.
# C873SRC 000240|    negative = q_v if sign > 0 else q_u
# C873SRC 000241|    return (
# C873SRC 000242|        x_gate(negative, prefix + "negative_X"),
# C873SRC 000243|    ) + primitive_word(q_u, q_v, current, prefix + "Toffoli_") + (
# C873SRC 000244|        x_gate(negative, prefix + "negative_X"),
# C873SRC 000245|    )
# C873SRC 000246|
# C873SRC 000247|
# C873SRC 000248|def fredkin_word(control: Coord, left: Coord, right: Coord, prefix: str):
# C873SRC 000249|    return (
# C873SRC 000250|        C871.cnot(left, right, prefix + "outer_CNOT"),
# C873SRC 000251|    ) + primitive_word(control, right, left, prefix + "Toffoli_") + (
# C873SRC 000252|        C871.cnot(left, right, prefix + "outer_CNOT"),
# C873SRC 000253|    )
# C873SRC 000254|
# C873SRC 000255|
# C873SRC 000256|def shift_word(placement: IntegratedPlacement, direction: int, prefix: str):
# C873SRC 000257|    order = range(15, -1, -1) if direction > 0 else range(16)
# C873SRC 000258|    return tuple(
# C873SRC 000259|        instruction
# C873SRC 000260|        for rail in order
# C873SRC 000261|        for instruction in fredkin_word(
# C873SRC 000262|            placement.current,
# C873SRC 000263|            placement.rails[rail],
# C873SRC 000264|            placement.rails[rail + 1],
# C873SRC 000265|            f"{prefix}{rail}_",
# C873SRC 000266|        )
# C873SRC 000267|    )
# C873SRC 000268|
# C873SRC 000269|
# C873SRC 000270|@dataclass(frozen=True)
# C873SRC 000271|class IntegratedProgram:
# C873SRC 000272|    endpoint_pre: tuple[Instruction, ...]
# C873SRC 000273|    selected_seam: tuple[Instruction, ...]
# C873SRC 000274|    positive_compute: tuple[Instruction, ...]
# C873SRC 000275|    positive_shift: tuple[Instruction, ...]
# C873SRC 000276|    positive_uncompute: tuple[Instruction, ...]
# C873SRC 000277|    negative_compute: tuple[Instruction, ...]
# C873SRC 000278|    negative_shift: tuple[Instruction, ...]
# C873SRC 000279|    negative_uncompute: tuple[Instruction, ...]
# C873SRC 000280|    pointer_write: tuple[Instruction, ...]
# C873SRC 000281|    endpoint_clean: tuple[Instruction, ...]
# C873SRC 000282|    packet: tuple[Instruction, ...]
# C873SRC 000283|
# C873SRC 000284|    @property
# C873SRC 000285|    def branch(self):
# C873SRC 000286|        return (
# C873SRC 000287|            self.positive_compute + self.positive_shift + self.positive_uncompute
# C873SRC 000288|            + self.negative_compute + self.negative_shift + self.negative_uncompute
# C873SRC 000289|        )
# C873SRC 000290|
# C873SRC 000291|    @property
# C873SRC 000292|    def added_excluding_seam_and_packet(self):
# C873SRC 000293|        return self.endpoint_pre + self.branch + self.pointer_write + self.endpoint_clean
# C873SRC 000294|
# C873SRC 000295|    @property
# C873SRC 000296|    def f17_only_added_excluding_seam(self):
# C873SRC 000297|        return self.endpoint_pre + self.branch + self.endpoint_clean
# C873SRC 000298|
# C873SRC 000299|    @property
# C873SRC 000300|    def f17_only_macro(self):
# C873SRC 000301|        return self.endpoint_pre + self.selected_seam + self.branch + self.endpoint_clean
# C873SRC 000302|
# C873SRC 000303|    @property
# C873SRC 000304|    def coexistence_macro(self):
# C873SRC 000305|        return (
# C873SRC 000306|            self.endpoint_pre + self.selected_seam + self.branch
# C873SRC 000307|            + self.pointer_write + self.endpoint_clean + self.packet
# C873SRC 000308|        )
# C873SRC 000309|
# C873SRC 000310|
# C873SRC 000311|def emit_program(graph, context, seam, placement: IntegratedPlacement, alpha: int):
# C873SRC 000312|    if alpha not in (-1, 1):
# C873SRC 000313|        raise ValueError("only the supplied alpha=+/-1 typed families are in scope")
# C873SRC 000314|    cell, _axis, target, left_mode, right_mode = seam
# C873SRC 000315|    left_b = C871.physical_b(graph, context, cell, left_mode)
# C873SRC 000316|    right_b = C871.physical_b(graph, context, target, right_mode)
# C873SRC 000317|    selected = C871.selected_seam_rotations(graph, seam)
# C873SRC 000318|    program = IntegratedProgram(
# C873SRC 000319|        endpoint_pre=(
# C873SRC 000320|            C871.extract_b(left_b, context, placement.q_u, "F17_pre_left_B")
# C873SRC 000321|            + C871.extract_b(right_b, context, placement.q_v, "F17_pre_right_B")
# C873SRC 000322|        ),
# C873SRC 000323|        selected_seam=C871.compile_rotations(selected, context),
# C873SRC 000324|        positive_compute=predicate_compute(
# C873SRC 000325|            placement.q_u, placement.q_v, placement.current, 1,
# C873SRC 000326|            "F17_positive_compute_",
# C873SRC 000327|        ),
# C873SRC 000328|        positive_shift=shift_word(
# C873SRC 000329|            placement, alpha, "F17_positive_shift_"
# C873SRC 000330|        ),
# C873SRC 000331|        positive_uncompute=predicate_uncompute(
# C873SRC 000332|            placement.q_u, placement.q_v, placement.current, 1,
# C873SRC 000333|            "F17_positive_uncompute_",
# C873SRC 000334|        ),
# C873SRC 000335|        negative_compute=predicate_compute(
# C873SRC 000336|            placement.q_u, placement.q_v, placement.current, -1,
# C873SRC 000337|            "F17_negative_compute_",
# C873SRC 000338|        ),
# C873SRC 000339|        negative_shift=shift_word(
# C873SRC 000340|            placement, -alpha, "F17_negative_shift_"
# C873SRC 000341|        ),
# C873SRC 000342|        negative_uncompute=predicate_uncompute(
# C873SRC 000343|            placement.q_u, placement.q_v, placement.current, -1,
# C873SRC 000344|            "F17_negative_uncompute_",
# C873SRC 000345|        ),
# C873SRC 000346|        pointer_write=(
# C873SRC 000347|            C871.cnot(placement.q_u, placement.pointer, "F17_pointer_XOR"),
# C873SRC 000348|            C871.cnot(placement.q_v, placement.pointer, "F17_pointer_XOR"),
# C873SRC 000349|        ),
# C873SRC 000350|        endpoint_clean=(
# C873SRC 000351|            C871.extract_b(
# C873SRC 000352|                right_b, context, placement.q_u, "F17_clean_right_B_into_q_u"
# C873SRC 000353|            )
# C873SRC 000354|            + C871.extract_b(
# C873SRC 000355|                left_b, context, placement.q_v, "F17_clean_left_B_into_q_v"
# C873SRC 000356|            )
# C873SRC 000357|        ),
# C873SRC 000358|        packet=C871.packet_word(placement.packet),
# C873SRC 000359|    )
# C873SRC 000360|    return program
# C873SRC 000361|
# C873SRC 000362|
# C873SRC 000363|def compose_small(gates, qubits: int):
# C873SRC 000364|    matrices = {"H": C714.H, "T": C714.T, "TD": C714.TD, "CNOT": C714.CNOT}
# C873SRC 000365|    output = np.eye(1 << qubits, dtype=complex)
# C873SRC 000366|    for kind, wires in gates:
# C873SRC 000367|        output = np.column_stack([
# C873SRC 000368|            C714.apply_small(output[:, column], matrices[kind], wires, qubits)
# C873SRC 000369|            for column in range(1 << qubits)
# C873SRC 000370|        ])
# C873SRC 000371|    return output
# C873SRC 000372|
# C873SRC 000373|
# C873SRC 000374|def primitive_certificate():
# C873SRC 000375|    full = list(C714.toffoli_primitives(0, 1, 2))
# C873SRC 000376|    reduced = [row for index, row in enumerate(full) if index != 1]
# C873SRC 000377|    target = compose_small(full, 3)
# C873SRC 000378|    observed = compose_small(reduced, 3)
# C873SRC 000379|    clean_columns = tuple(range(4))  # target is the most-significant local bit.
# C873SRC 000380|    deletion_residuals = []
# C873SRC 000381|    for deleted in range(len(reduced)):
# C873SRC 000382|        damaged = compose_small(
# C873SRC 000383|            [row for index, row in enumerate(reduced) if index != deleted], 3
# C873SRC 000384|        )
# C873SRC 000385|        deletion_residuals.append(float(np.linalg.norm(
# C873SRC 000386|            (damaged - target)[:, clean_columns]
# C873SRC 000387|        )))
# C873SRC 000388|    fredkin = (
# C873SRC 000389|        [("CNOT", (1, 2))]
# C873SRC 000390|        + list(C714.toffoli_primitives(0, 2, 1))
# C873SRC 000391|        + [("CNOT", (1, 2))]
# C873SRC 000392|    )
# C873SRC 000393|    fredkin_matrix = compose_small(fredkin, 3)
# C873SRC 000394|    fredkin_target = np.zeros((8, 8), dtype=complex)
# C873SRC 000395|    for source in range(8):
# C873SRC 000396|        control = source & 1
# C873SRC 000397|        left, right = (source >> 1) & 1, (source >> 2) & 1
# C873SRC 000398|        target_index = source
# C873SRC 000399|        if control:
# C873SRC 000400|            target_index = (
# C873SRC 000401|                (source & ~(1 << 1) & ~(1 << 2)) | (right << 1) | (left << 2)
# C873SRC 000402|            )
# C873SRC 000403|        fredkin_target[target_index, source] = 1
# C873SRC 000404|    return {
# C873SRC 000405|        "landed_full_Toffoli_primitives": len(full),
# C873SRC 000406|        "clean_target_Toffoli_primitives": len(reduced),
# C873SRC 000407|        "removed_primitive": repr(full[1]),
# C873SRC 000408|        "removed_occurrences_per_macro": 2,
# C873SRC 000409|        "clean_target_column_residual": float(np.linalg.norm(
# C873SRC 000410|            (observed - target)[:, clean_columns]
# C873SRC 000411|        )),
# C873SRC 000412|        "off_domain_full_space_difference": float(np.linalg.norm(observed - target)),
# C873SRC 000413|        "remaining_clean_target_primitive_deletion_residuals": deletion_residuals,
# C873SRC 000414|        "minimum_remaining_clean_target_primitive_deletion_residual": min(deletion_residuals),
# C873SRC 000415|        "inactive_remaining_clean_target_primitive_deletions": tuple(
# C873SRC 000416|            index for index, residual in enumerate(deletion_residuals) if residual <= TOL
# C873SRC 000417|        ),
# C873SRC 000418|        "unchanged_full_Toffoli_residual": C714.toffoli_residual(),
# C873SRC 000419|        "Fredkin_residual": float(np.linalg.norm(fredkin_matrix - fredkin_target)),
# C873SRC 000420|        "primitive_deletion_scope": (
# C873SRC 000421|            "the reduced isolated clean-target compute word only; no per-occurrence "
# C873SRC 000422|            "essentiality claim is made for the supplied-domain Cycle714 packet word"
# C873SRC 000423|        ),
# C873SRC 000424|    }
# C873SRC 000425|
# C873SRC 000426|
# C873SRC 000427|# Semantic state: matter u/v, q_u/q_v/current, F17 label, packet pointer.
# C873SRC 000428|SemanticKey = tuple[int, int, int, int, int, int, int]
# C873SRC 000429|SemanticState = dict[SemanticKey, complex]
# C873SRC 000430|
# C873SRC 000431|
# C873SRC 000432|def prune(state: SemanticState):
# C873SRC 000433|    return {key: value for key, value in state.items() if abs(value) > 1.0e-14}
# C873SRC 000434|
# C873SRC 000435|
# C873SRC 000436|def semantic_operations(
# C873SRC 000437|    alpha: int, mutation: str | None = None, *, include_pointer: bool = False
# C873SRC 000438|):
# C873SRC 000439|    rows = [
# C873SRC 000440|        ("pre_u", ("CNOT", 0, 2)),
# C873SRC 000441|        ("pre_v", ("CNOT", 1, 3)),
# C873SRC 000442|        ("seam", ("FSWAP",)),
# C873SRC 000443|        ("plus_X_pre", ("X", 3)),
# C873SRC 000444|        ("plus_compute", ("TOF", 2, 3, 4)),
# C873SRC 000445|        ("plus_X_post", ("X", 3)),
# C873SRC 000446|        ("plus_shift", ("SHIFT", alpha)),
# C873SRC 000447|        ("plus_un_X_pre", ("X", 3)),
# C873SRC 000448|        ("plus_uncompute", ("TOF", 2, 3, 4)),
# C873SRC 000449|        ("plus_un_X_post", ("X", 3)),
# C873SRC 000450|        ("minus_X_pre", ("X", 2)),
# C873SRC 000451|        ("minus_compute", ("TOF", 2, 3, 4)),
# C873SRC 000452|        ("minus_X_post", ("X", 2)),
# C873SRC 000453|        ("minus_shift", ("SHIFT", -alpha)),
# C873SRC 000454|        ("minus_un_X_pre", ("X", 2)),
# C873SRC 000455|        ("minus_uncompute", ("TOF", 2, 3, 4)),
# C873SRC 000456|        ("minus_un_X_post", ("X", 2)),
# C873SRC 000457|        ("pointer_u", ("CNOT", 2, 6)),
# C873SRC 000458|        ("pointer_v", ("CNOT", 3, 6)),
# C873SRC 000459|        ("clean_u", ("CNOT", 1, 2)),
# C873SRC 000460|        ("clean_v", ("CNOT", 0, 3)),
# C873SRC 000461|    ]
# C873SRC 000462|    omissions = {
# C873SRC 000463|        "delete_plus_shift": {"plus_shift"},
# C873SRC 000464|        "delete_minus_shift": {"minus_shift"},
# C873SRC 000465|        "delete_pointer_u": {"pointer_u"},
# C873SRC 000466|        "delete_pointer_v": {"pointer_v"},
# C873SRC 000467|        "delete_cleanup": {"clean_u", "clean_v"},
# C873SRC 000468|        "delete_seam": {"seam"},
# C873SRC 000469|    }.get(mutation, set())
# C873SRC 000470|    if not include_pointer:
# C873SRC 000471|        omissions = set(omissions) | {"pointer_u", "pointer_v"}
# C873SRC 000472|    return tuple(row for name, row in rows if name not in omissions)
# C873SRC 000473|
# C873SRC 000474|
# C873SRC 000475|def apply_semantic_operation(state: SemanticState, operation):
# C873SRC 000476|    output: SemanticState = {}
# C873SRC 000477|    for key, amplitude in state.items():
# C873SRC 000478|        bits = list(key[:5])
# C873SRC 000479|        label, pointer = key[5], key[6]
# C873SRC 000480|        phase = 1.0 + 0.0j
# C873SRC 000481|        kind = operation[0]
# C873SRC 000482|        if kind == "X":
# C873SRC 000483|            bits[operation[1]] ^= 1
# C873SRC 000484|        elif kind == "CNOT":
# C873SRC 000485|            control, target = operation[1], operation[2]
# C873SRC 000486|            source = bits[control] if control < 5 else pointer
# C873SRC 000487|            if target < 5:
# C873SRC 000488|                bits[target] ^= source
# C873SRC 000489|            else:
# C873SRC 000490|                pointer ^= source
# C873SRC 000491|        elif kind == "TOF":
# C873SRC 000492|            bits[operation[3]] ^= bits[operation[1]] & bits[operation[2]]
# C873SRC 000493|        elif kind == "FSWAP":
# C873SRC 000494|            phase = -1.0 if bits[0] == bits[1] == 1 else 1.0
# C873SRC 000495|            bits[0], bits[1] = bits[1], bits[0]
# C873SRC 000496|        elif kind == "SHIFT":
# C873SRC 000497|            if bits[4]:
# C873SRC 000498|                label = (label + operation[1]) % F17
# C873SRC 000499|        else:
# C873SRC 000500|            raise AssertionError(operation)
# C873SRC 000501|        target_key = (*bits, label, pointer)
# C873SRC 000502|        output[target_key] = output.get(target_key, 0.0j) + phase * amplitude
# C873SRC 000503|    return prune(output)
# C873SRC 000504|
# C873SRC 000505|
# C873SRC 000506|def execute_semantic(state: SemanticState, rows):
# C873SRC 000507|    current = state
# C873SRC 000508|    for row in rows:
# C873SRC 000509|        current = apply_semantic_operation(current, row)
# C873SRC 000510|    return current
# C873SRC 000511|
# C873SRC 000512|
# C873SRC 000513|def inverse_semantic(rows):
# C873SRC 000514|    output = []
# C873SRC 000515|    for row in reversed(rows):
# C873SRC 000516|        output.append(("SHIFT", -row[1]) if row[0] == "SHIFT" else row)
# C873SRC 000517|    return tuple(output)
# C873SRC 000518|
# C873SRC 000519|
# C873SRC 000520|def state_distance(left, right) -> float:
# C873SRC 000521|    return float(math.sqrt(sum(
# C873SRC 000522|        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
# C873SRC 000523|        for key in set(left) | set(right)
# C873SRC 000524|    )))
# C873SRC 000525|
# C873SRC 000526|
# C873SRC 000527|def semantic_target(
# C873SRC 000528|    a: int, b: int, label: int, alpha: int, *, include_pointer: bool = False
# C873SRC 000529|):
# C873SRC 000530|    phase = -1.0 if a == b == 1 else 1.0
# C873SRC 000531|    return {
# C873SRC 000532|        (
# C873SRC 000533|            b, a, 0, 0, 0, (label + alpha * (a - b)) % F17,
# C873SRC 000534|            (a ^ b) if include_pointer else 0,
# C873SRC 000535|        ):
# C873SRC 000536|        phase + 0.0j
# C873SRC 000537|    }
# C873SRC 000538|
# C873SRC 000539|
# C873SRC 000540|def semantic_certificate(alpha: int):
# C873SRC 000541|    rows = semantic_operations(alpha, include_pointer=False)
# C873SRC 000542|    inverse = inverse_semantic(rows)
# C873SRC 000543|    failures = scratch = pointer_failures = gauss = inverse_failures = 0
# C873SRC 000544|    outputs = set()
# C873SRC 000545|    coherent, coherent_expected = {}, {}
# C873SRC 000546|    normalization = math.sqrt(4 * F17)
# C873SRC 000547|    for a, b in product((0, 1), repeat=2):
# C873SRC 000548|        for label in range(F17):
# C873SRC 000549|            initial = {(a, b, 0, 0, 0, label, 0): 1.0 + 0.0j}
# C873SRC 000550|            expected = semantic_target(a, b, label, alpha)
# C873SRC 000551|            observed = execute_semantic(initial, rows)
# C873SRC 000552|            failures += state_distance(observed, expected) > TOL
# C873SRC 000553|            key = next(iter(observed))
# C873SRC 000554|            outputs.add(key)
# C873SRC 000555|            scratch += any(key[index] for index in (2, 3, 4))
# C873SRC 000556|            pointer_failures += key[6] != 0
# C873SRC 000557|            inverse_failures += state_distance(execute_semantic(observed, inverse), initial) > TOL
# C873SRC 000558|            after_a, after_b, _qu, _qv, _current, after_label, _pointer = key
# C873SRC 000559|            family_sign = alpha
# C873SRC 000560|            before_g = (
# C873SRC 000561|                (a + family_sign * label) % F17,
# C873SRC 000562|                (b - family_sign * label) % F17,
# C873SRC 000563|            )
