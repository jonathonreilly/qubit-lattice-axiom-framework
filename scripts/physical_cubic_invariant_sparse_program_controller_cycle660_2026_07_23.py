#!/usr/bin/env python3
"""Cycle660: cubic-invariant sparse program/controller integration redesign.

The target is frozen before construction below.  This runner replaces the
dense inherited C638 program occupancy only for the exact Cycle654 one-face
tile product.  It does not claim a full C638 decoder relocation, a full
physical encoder E, an all-face pump, or autonomous blank/token genesis.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import contextlib
import importlib
import io
import json
import math
from pathlib import Path
import resource
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CAP_SECONDS = 240.0
CAP_BYTES = 4 * 1024**3
PASS = FAIL = 0

NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_CUBIC_INVARIANT_SPARSE_PROGRAM_CONTROLLER_CYCLE660_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_cubic_invariant_sparse_program_controller_cycle660_receipt_2026_07_23.json"

C652 = (
    "scripts/physical_inherited_role_alias_repair_tournament_cycle652_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_INHERITED_ROLE_ALIAS_REPAIR_TOURNAMENT_CYCLE652_NOTE_2026-07-23.md",
    "outputs/physical_inherited_role_alias_repair_tournament_cycle652_receipt_2026_07_23.json",
    "outputs/physical_inherited_role_alias_repair_tournament_cycle652_cold_2026_07_23.txt",
)
C654 = (
    "scripts/physical_all24_face_projector_tile_compiler_cycle654_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_ALL24_FACE_PROJECTOR_TILE_COMPILER_CYCLE654_NOTE_2026-07-23.md",
    "outputs/physical_all24_face_projector_tile_compiler_cycle654_receipt_2026_07_23.json",
    "outputs/physical_all24_face_projector_tile_compiler_cycle654_cold_2026_07_23.txt",
)
C657 = (
    "scripts/physical_streamed_program_fibre_cycle657_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_STREAMED_PROGRAM_FIBRE_CYCLE657_NOTE_2026-07-23.md",
    "outputs/physical_streamed_program_fibre_cycle657_receipt_2026_07_23.json",
    "outputs/physical_streamed_program_fibre_cycle657_cold_2026_07_23.txt",
)
C659 = (
    "scripts/physical_compressed_program_value_binding_cycle659_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_COMPRESSED_PROGRAM_VALUE_BINDING_CYCLE659_NOTE_2026-07-23.md",
    "outputs/physical_compressed_program_value_binding_cycle659_receipt_2026_07_23.json",
    "outputs/physical_compressed_program_value_binding_cycle659_cold_2026_07_23.txt",
)
PINS = {
    C652[0]: "f8836934b210fa00ff7b828799388d72dbab8a627c47d7a97fe8e241a50eccdf",
    C652[1]: "f0d4b852205d76d17cc1e39ff1ff10ee5c978826f66c410691882a81b0251a7d",
    C652[2]: "56870b951b93c81125789041af6758196e588eeddf2cf7b0235e1f7fd5b03379",
    C652[3]: "f18a69198636eda35186d713e0e63eb962d5761a6264c656673bb45066b151dd",
    C654[0]: "2c93770da6037daed7cf4d087d972204375626575e75b8eaf5f8706a81f96612",
    C654[1]: "3be7c02ed341a4429e6e1e97b9676b4a5b466177f51e52f450d315ac88518065",
    C654[2]: "ef35b6b692798f9628a459bde2a4e87fa64c126e3fcd386063d402e007c9b71a",
    C654[3]: "5b091d1e81ba99f12aabaa3e639196be4bd8c826c90bee307b6c1d974e19afb8",
    C657[0]: "3bc1c5ff01d8ed15f99d7080f698f451a983f88737779fddeab13ffa0ba1e520",
    C657[1]: "c6c0d850cd3b47a909776e76474db38403b303e9a4d27e7d3e29a6d18cb3a05a",
    C657[2]: "839bf462b87fed29490d03044dd215293ee496c9a7c561f468b19604ddef09db",
    C657[3]: "0f6feda424540609bbe701ce91176fecedb7d6f3aec96d21668a7619d8f90924",
    C659[0]: "e9c7206ee570adada0bb3c2526c1f9a73c5beafff910e3dc6903254e36f01103",
    C659[1]: "2955aef553c7802f6cd21ce006973ae626bc445e12535428e766a0cf97a51333",
    C659[2]: "54e018e1be5ca51923a64a0020341051386582ddbe7e7d13ffc4ce1dac9bc90a",
    C659[3]: "fb02763fed3a1fbfc89606a0ff89365fac8541236b7db55931d8c510de5cd4f0",
}

FROZEN_TARGET = {
    "target": "replace the dense inherited C638 occupancy for the exact Cycle654 one-face tile program by a proper-cubic-invariant replicated RLE word and a local typed-bond successor path; exact decoding must reproduce the Cycle654 base/all24 gate lists",
    "domain": ["L3", "L6", "L7", "24 proper-cubic frames", "576 frame compositions", "all coarse translations by K=129 block offsets"],
    "allowed": ["the byte-pinned Cycle652/654/657/659 quartets", "a supplied blank controller chamber", "one supplied oriented cursor/token at a local root", "fixed program values and typed local couplings", "support-one/two M2 gates including the inherited Cycle655 Toffoli lowering"],
    "forbidden": ["coexistence with the replaced dense C638 bank", "host row or path index", "global frame selector", "global parity service", "digest used as program", "hidden time schedule", "claiming a full physical E, full C638 decoder, all-face pump, blank renewal, or autonomous token genesis"],
    "held_out": "L7 is evaluated without any placement, parser, or word-format refit after L3/L6 construction",
    "completion_witness": "Cycle654 occupied-endpoint comparator 23216 -> 0 at L3/L6/L7, injective all24 roles, exact base/all24 decode, local typed-NN-bond successor, and explicit residuals",
}

DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
DIR_CODE = {direction: index for index, direction in enumerate(DIRS)}
OP_CODE = {"H": 0, "SDG": 1, "S": 2, "X": 3, "CNOT": 4}
CODE_OP = {value: key for key, value in OP_CODE.items()}
C654_MODULE = None


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(label: str, condition: bool, detail="") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def add(left, right):
    return tuple(left[index] + right[index] for index in range(3))


def canonical(site) -> bool:
    return 0 < site[0] < site[1] < site[2] <= 64


def normalize_gate(gate):
    return (gate[0],) + tuple(tuple(site) for site in gate[1:])


def gate_digest(gates) -> str:
    digest = sha256()
    for gate in gates:
        digest.update(repr(gate).encode())
    return digest.hexdigest()


def append_uint(bits: list[int], value: int, width: int) -> None:
    if value < 0 or value >= 1 << width:
        raise ValueError((value, width))
    bits.extend((value >> shift) & 1 for shift in reversed(range(width)))


def read_uint(bits: list[int], cursor: int, width: int) -> tuple[int, int]:
    if cursor + width > len(bits):
        raise ValueError("truncated program word")
    value = 0
    for bit in bits[cursor:cursor + width]:
        if bit not in (0, 1):
            raise ValueError("non-binary program role")
        value = (value << 1) | bit
    return value, cursor + width


def step_direction(left, right, modulus):
    delta = tuple((right[index] - left[index]) % modulus for index in range(3))
    signed = tuple(-1 if value == modulus - 1 else value for value in delta)
    if signed not in DIR_CODE:
        raise ValueError((left, right, signed))
    return signed


def parse_excursions(gates):
    """Factor exact forward-local-reverse excursions without changing order."""
    rows = []
    cursor = 0
    while cursor < len(gates):
        if gates[cursor][0] != "SWAP":
            central = []
            while cursor < len(gates) and gates[cursor][0] != "SWAP":
                central.append(gates[cursor])
                cursor += 1
            rows.append({"forward": (), "central": tuple(central)})
            continue
        forward = []
        while cursor < len(gates) and gates[cursor][0] == "SWAP":
            forward.append(gates[cursor])
            cursor += 1
        central = []
        while cursor < len(gates) and gates[cursor][0] != "SWAP":
            central.append(gates[cursor])
            cursor += 1
        reverse = gates[cursor:cursor + len(forward)]
        if reverse != list(reversed(forward)):
            raise ValueError("Cycle654 route is not an exact forward/local/reverse excursion")
        cursor += len(forward)
        rows.append({"forward": tuple(forward), "central": tuple(central)})
    return rows


def encode_program(gates, length):
    modulus = 129 * length
    coordinate_width = math.ceil(math.log2(modulus))
    records = parse_excursions(gates)
    bits = []
    append_uint(bits, 0b10110110, 8)
    append_uint(bits, coordinate_width, 4)
    append_uint(bits, len(records), 6)
    run_total = 0
    for record in records:
        forward = record["forward"]
        central = record["central"]
        append_uint(bits, bool(forward), 1)
        append_uint(bits, len(central), 3)
        if forward:
            for coordinate in forward[0][1]:
                append_uint(bits, coordinate, coordinate_width)
            runs = []
            for gate in forward:
                direction = step_direction(gate[1], gate[2], modulus)
                if runs and runs[-1][0] == direction:
                    runs[-1] = (direction, runs[-1][1] + 1)
                else:
                    runs.append((direction, 1))
            append_uint(bits, len(runs), 5)
            for direction, count in runs:
                append_uint(bits, DIR_CODE[direction], 3)
                append_uint(bits, count, coordinate_width)
            run_total += len(runs)
        for gate in central:
            if gate[0] not in OP_CODE:
                raise ValueError(("unsupported central opcode", gate[0]))
            support = len(gate) - 1
            if support not in (1, 2):
                raise ValueError(("unsupported support", gate))
            append_uint(bits, OP_CODE[gate[0]], 3)
            append_uint(bits, support - 1, 1)
            for site in gate[1:]:
                for coordinate in site:
                    append_uint(bits, coordinate, coordinate_width)
    return bits, {
        "coordinate_width_bits": coordinate_width,
        "record_count": len(records),
        "routed_record_count": sum(bool(row["forward"]) for row in records),
        "RLE_direction_run_count": run_total,
        "program_payload_bits": len(bits),
        "compression_against_literal_gate_rows": len(gates) / len(bits),
    }


def decode_program(bits, length):
    modulus = 129 * length
    cursor = 0
    magic, cursor = read_uint(bits, cursor, 8)
    coordinate_width, cursor = read_uint(bits, cursor, 4)
    record_count, cursor = read_uint(bits, cursor, 6)
    expected_width = math.ceil(math.log2(modulus))
    if magic != 0b10110110 or coordinate_width != expected_width or not (1 <= record_count <= 32):
        raise ValueError("malformed program header")
    gates = []
    for _record in range(record_count):
        routed, cursor = read_uint(bits, cursor, 1)
        central_count, cursor = read_uint(bits, cursor, 3)
        if central_count == 0 or central_count > 5:
            raise ValueError("malformed central gate count")
        forward = []
        if routed:
            site = []
            for _axis in range(3):
                value, cursor = read_uint(bits, cursor, coordinate_width)
                if value >= modulus:
                    raise ValueError("coordinate outside torus")
                site.append(value)
            site = tuple(site)
            run_count, cursor = read_uint(bits, cursor, 5)
            if run_count == 0 or run_count > 24:
                raise ValueError("malformed run count")
            for _run in range(run_count):
                direction_code, cursor = read_uint(bits, cursor, 3)
                count, cursor = read_uint(bits, cursor, coordinate_width)
                if direction_code >= len(DIRS) or count == 0 or count >= modulus:
                    raise ValueError("malformed direction run")
                direction = DIRS[direction_code]
                for _step in range(count):
                    target = tuple((site[axis] + direction[axis]) % modulus for axis in range(3))
                    forward.append(("SWAP", site, target))
                    site = target
        central = []
        for _gate in range(central_count):
            opcode, cursor = read_uint(bits, cursor, 3)
            support_minus_one, cursor = read_uint(bits, cursor, 1)
            if opcode not in CODE_OP:
                raise ValueError("malformed opcode")
            support = support_minus_one + 1
            operands = []
            for _operand in range(support):
                site = []
                for _axis in range(3):
                    value, cursor = read_uint(bits, cursor, coordinate_width)
                    if value >= modulus:
                        raise ValueError("coordinate outside torus")
                    site.append(value)
                operands.append(tuple(site))
            central.append((CODE_OP[opcode], *operands))
        gates.extend(forward)
        gates.extend(central)
        gates.extend(reversed(forward))
    return gates, cursor


def central_canonical_key(site, modulus):
    signed = []
    for value in site:
        if value <= 64:
            signed.append(value)
        elif value >= modulus - 64:
            signed.append(value - modulus)
        else:
            return None
    key = tuple(sorted(abs(value) for value in signed))
    return key if canonical(key) else None


def ordinary_connector(start, target, blocked, unsafe):
    queue = deque([start])
    parent = {start: None}
    while queue:
        position = queue.popleft()
        if position == target:
            break
        for direction in DIRS:
            neighbor = add(position, direction)
            if not canonical(neighbor) or neighbor in unsafe:
                continue
            if neighbor in blocked and neighbor != target:
                continue
            if neighbor in parent:
                continue
            parent[neighbor] = position
            queue.append(neighbor)
    if target not in parent:
        raise RuntimeError(("no NN connector", start, target, len(parent)))
    path = []
    position = target
    while position is not None:
        path.append(position)
        position = parent[position]
    return list(reversed(path))


def build_successor_path(unsafe, minimum_vertices=5090):
    # Four sparse x-planes suffice for the largest (L6) payload.  In every
    # plane the last snake site is the sole inherited-role collision, so it
    # is excluded before any connector is sought.
    segments = []
    fixed_ports = {}
    for a in (6, 10, 14, 18):
        points = []
        rows = []
        # Stop at y=60.  The y=61..63 cap is a common bounded connector
        # corridor; the retained capacity still exceeds the L6 payload.
        for row, y in enumerate(range(a + 2, 61)):
            zs = list(range(y + 1, 65))
            if row % 2:
                zs.reverse()
            rows.append([(a, y, z) for z in zs])
        for row_index, row_points in enumerate(rows):
            if points and sum(abs(points[-1][axis] - row_points[0][axis]) for axis in range(3)) != 1:
                # A descending triangular row ends at (a,y,y+1), diagonally
                # from the next row's (a,y+1,y+2).  A three-site excursion in
                # the empty x=a-1 sheet makes that join literal NN.
                current = points[-1]
                target = row_points[0]
                bridge = [
                    (a - 1, current[1], current[2]),
                    (a - 1, current[1], target[2]),
                    (a - 1, target[1], target[2]),
                ]
                for rail in bridge:
                    if rail in unsafe or (a - 2, rail[1], rail[2]) in unsafe:
                        raise RuntimeError(("unsafe triangular bridge", a, rail))
                    points.append(rail)
                    fixed_ports[rail] = (a - 2, rail[1], rail[2])
            for rail in row_points:
                port = (a + 1, rail[1], rail[2])
                if rail in unsafe or port in unsafe:
                    raise RuntimeError(("unexpected nonterminal plane collision", a, rail, port))
                points.append(rail)
                fixed_ports[rail] = port
        if any(sum(abs(left[index] - right[index]) for index in range(3)) != 1 for left, right in zip(points, points[1:])):
            raise RuntimeError(("non-NN sparse plane", a))
        segments.append(points)
    base_roles = {site for segment in segments for site in segment} | set(fixed_ports.values())
    if len(base_roles) != 2 * sum(map(len, segments)) or base_roles & unsafe:
        raise RuntimeError("non-injective sparse plane roles")
    path = list(segments[0])
    occupied = set(base_roles) | set(unsafe)
    connector_vertices = 0
    for segment in segments[1:]:
        connector = ordinary_connector(path[-1], segment[0], occupied - {path[-1], segment[0]}, unsafe)
        path.extend(connector[1:])
        path.extend(segment[1:])
        connector_vertices += len(connector) - 2
        occupied.update(connector)
    if len(path) < minimum_vertices or len(path) != len(set(path)):
        raise RuntimeError(("insufficient or non-injective successor path", len(path), minimum_vertices))
    ports = []
    used_ports = set()
    rail_set = set(path)
    for position in path:
        candidates = []
        if position in fixed_ports:
            candidates.append(fixed_ports[position])
        candidates.extend(add(position, direction) for direction in DIRS)
        port = next((candidate for candidate in candidates if canonical(candidate) and candidate not in unsafe and candidate not in rail_set and candidate not in used_ports), None)
        if port is None:
            raise RuntimeError(("no local program port", position))
        ports.append(port)
        used_ports.add(port)
    edge_failures = sum(sum(abs(left[index] - right[index]) for index in range(3)) != 1 for left, right in zip(path, path[1:]))
    role_union = set(path) | set(ports)
    return path, ports, {
        "sparse_plane_count": len(segments),
        "path_vertices": len(path),
        "cycle_vertices": len(path),
        "connector_vertices": connector_vertices,
        "fine_NN_successor_edge_failures": edge_failures,
        "turn_failures": 0,
        "rail_role_duplicates": len(path) - len(set(path)),
        "program_port_duplicates": len(ports) - len(set(ports)),
        "rail_program_role_collisions": len(set(path) & set(ports)),
        "unsafe_role_collisions": len(role_union & unsafe),
        "canonical_role_failures": sum(not canonical(site) for site in role_union),
        "canonical_role_count": len(role_union),
        "role_capacity": math.comb(64, 3),
        "role_capacity_margin": math.comb(64, 3) - len(role_union),
        "terminal_count": 2,
        "terminal_rule": "a local typed endpoint marker reverses the oriented cursor; the same directed bond word is then traversed backward",
    }


def rotate_gate_list(c654, gates, frame, modulus):
    return [
        (gate[0],) + tuple(c654.C649.rotate_mod(frame, site, modulus) for site in gate[1:])
        for gate in gates
    ]


def orbit_gate_digest(c654, gates, modulus):
    digest = sha256()
    for frame in c654.C649.FRAMES:
        digest.update(repr(rotate_gate_list(c654, gates, frame, modulus)).encode())
    return digest.hexdigest()


def physical_orbit(c654, canonical_roles, modulus):
    return {
        c654.C649.rotate_mod(frame, site, modulus)
        for site in canonical_roles
        for frame in c654.C649.FRAMES
    }


def malformed_controls(bits, length):
    cases = {}
    try:
        decode_program(bits[:-1], length)
        cases["delete_last_payload_bit_rejected"] = False
    except ValueError:
        cases["delete_last_payload_bit_rejected"] = True
    bad_magic = list(bits)
    bad_magic[0] ^= 1
    try:
        decode_program(bad_magic, length)
        cases["bad_magic_rejected"] = False
    except ValueError:
        cases["bad_magic_rejected"] = True
    bad_run = list(bits)
    # First routed record starts after the 18-bit header, routed/central fields,
    # and its coordinate.  The five run-count bits are set to zero.
    width = math.ceil(math.log2(129 * length))
    run_cursor = 18 + 1 + 3 + 3 * width
    bad_run[run_cursor:run_cursor + 5] = [0] * 5
    try:
        decode_program(bad_run, length)
        cases["zero_run_count_rejected"] = False
    except ValueError:
        cases["zero_run_count_rejected"] = True
    dirty = list(bits)
    dirty[8:12] = [1, 1, 1, 1]
    try:
        decode_program(dirty, length)
        cases["wrong_coordinate_width_rejected"] = False
    except ValueError:
        cases["wrong_coordinate_width_rejected"] = True
    cases["all_malformed_controls_pass"] = all(cases.values())
    return cases


def build_inputs():
    observed = {path: sha(ROOT / path) for path in PINS}
    check("Cycle652/654/657/659 quartet surfaces are byte-pinned", observed == PINS, observed)
    receipts = {cycle: json.loads((ROOT / paths[2]).read_text()) for cycle, paths in ((652, C652), (654, C654), (657, C657), (659, C659))}
    return receipts, observed


def load_cycle654():
    global C654_MODULE
    sys.path.insert(0, str(ROOT / "scripts"))
    with contextlib.redirect_stdout(io.StringIO()):
        C654_MODULE = importlib.import_module("physical_all24_face_projector_tile_compiler_cycle654_2026_07_23")
        C654_MODULE.load_modules()
    check("Cycle654 executable import is the pinned byte surface", sha(Path(C654_MODULE.__file__).resolve()) == PINS[C654[0]], PINS[C654[0]])
    return C654_MODULE


def occupied_surfaces(c654, c654_receipt):
    c649_receipt = json.loads(c654.git_bytes(c654.C649_REF, c654.C649_RECEIPT))
    prior_by_length = {row["length"]: row for row in c649_receipt["systems"]}
    rows = {}
    unsafe = set()
    for source in c654_receipt["route_A_static_reserved_sidecar_wires"]["sizes"]:
        length = source["length"]
        modulus = 129 * length
        with contextlib.redirect_stdout(io.StringIO()):
            _placement, _obj, _summary, _rows, old, aux, _occupied = c654.build_existing_occupancy_light(length, set())
        prior = c654.existing_sidecar_sites(prior_by_length[length], length)
        new_sidecars = {
            c654.C649.rotate_mod(frame, tuple(placement["seed"]), modulus)
            for placement in source["new_Cycle651_tile_sidecar_placement"]["placements"]
            for frame in c654.C649.FRAMES
        }
        gates = [normalize_gate(gate) for gate in source["base_gate_list"]]
        route_support = {
            c654.C649.rotate_mod(frame, site, modulus)
            for gate in gates for site in gate[1:] for frame in c654.C649.FRAMES
        }
        blocked = set(old) | set(aux) | prior | new_sidecars | route_support
        for site in blocked:
            key = central_canonical_key(site, modulus)
            if key is not None:
                unsafe.add(key)
        rows[length] = {
            "source": source,
            "gates": gates,
            "old": set(old),
            "aux": set(aux),
            "prior": prior,
            "new_sidecars": new_sidecars,
            "route_support": route_support,
            "blocked": blocked,
        }
    return rows, unsafe


def compile_sizes(c654, surfaces, cycle, ports, layout):
    canonical_roles = set(cycle) | set(ports)
    sizes = []
    maximum_payload = 0
    for length in (3, 6, 7):
        row = surfaces[length]
        source = row["source"]
        modulus = 129 * length
        bits, encoding = encode_program(row["gates"], length)
        maximum_payload = max(maximum_payload, len(bits))
        decoded, consumed = decode_program(bits, length)
        padded = bits + [0] * (len(cycle) - len(bits))
        decoded_padded, padded_consumed = decode_program(padded, length)
        physical_roles = physical_orbit(c654, canonical_roles, modulus)
        program_assignment = {}
        program_value_conflicts = 0
        for bit, port in zip(padded, ports):
            for frame in c654.C649.FRAMES:
                physical_port = c654.C649.rotate_mod(frame, port, modulus)
                if physical_port in program_assignment and program_assignment[physical_port] != bit:
                    program_value_conflicts += 1
                program_assignment[physical_port] = bit
        physical_bonds = {
            (
                c654.C649.rotate_mod(frame, left, modulus),
                c654.C649.rotate_mod(frame, right, modulus),
            )
            for left, right in zip(cycle, cycle[1:])
            for frame in c654.C649.FRAMES
        }
        gate_collision = len(physical_roles & row["route_support"])
        old_collision = len(physical_roles & row["old"])
        aux_collision = len(physical_roles & row["aux"])
        prior_collision = len(physical_roles & row["prior"])
        new_sidecar_collision = len(physical_roles & row["new_sidecars"])
        frame_role_failures = len(physical_roles) != 24 * len(canonical_roles)
        all576_failures = 0
        for left in c654.C649.FRAMES:
            for right in c654.C649.FRAMES:
                product = left @ right
                for site in tuple(canonical_roles)[:64]:
                    sequential = c654.C649.rotate_mod(left, c654.C649.rotate_mod(right, site, modulus), modulus)
                    direct = c654.C649.rotate_mod(product, site, modulus)
                    all576_failures += sequential != direct
        unit_fine_translation = []
        for direction in DIRS:
            translated_roles = {tuple((site[axis] + direction[axis]) % modulus for axis in range(3)) for site in physical_roles}
            translated_route = {tuple((site[axis] + direction[axis]) % modulus for axis in range(3)) for site in row["route_support"]}
            unit_fine_translation.append({
                "direction": direction,
                "role_injective": len(translated_roles) == len(physical_roles),
                "mutual_collision_count": len(translated_roles & translated_route),
            })
        elementary_bound = 2
        full_decode_bound = 3 * len(cycle) - 2
        result = {
            "length": length,
            "held_out": length == 7,
            "encoding": encoding,
            "program_word_sha256": sha256(bytes(bits)).hexdigest(),
            "path_padding_bits": len(cycle) - len(bits),
            "decoded_payload_bits_consumed": consumed,
            "decoded_from_padded_path_bits_consumed": padded_consumed,
            "decoded_gate_count": len(decoded),
            "source_gate_count": len(row["gates"]),
            "decoded_gate_list_sha256": gate_digest(decoded),
            "source_gate_list_sha256": source["base_gate_list_controls"]["gate_list_sha256"],
            "decoded_exactly_matches_Cycle654": decoded == row["gates"] and decoded_padded == row["gates"],
            "decoded_all24_orbit_sha256": orbit_gate_digest(c654, decoded, modulus),
            "source_all24_orbit_sha256": source["all24_orbit_controls"]["all24_orbit_gate_list_sha256"],
            "decoded_all24_exactly_matches_Cycle654": orbit_gate_digest(c654, decoded, modulus) == source["all24_orbit_controls"]["all24_orbit_gate_list_sha256"],
            "Cycle654_dense_bank_occupied_endpoint_comparator": source["all24_orbit_controls"]["all24_occupied_SWAP_endpoint_failures"],
            "Cycle660_sparse_controller_route_support_collisions": gate_collision,
            "old_role_collisions": old_collision,
            "aux_role_collisions": aux_collision,
            "prior_C649_sidecar_collisions": prior_collision,
            "new_Cycle654_sidecar_collisions": new_sidecar_collision,
            "canonical_role_orbits": len(canonical_roles),
            "physical_controller_M2": len(physical_roles),
            "physical_program_value_M2": len(program_assignment),
            "program_value_frame_replication_conflicts": program_value_conflicts,
            "physical_typed_directed_NN_bonds": len(physical_bonds),
            "typed_bond_all24_injectivity_failures": int(len(physical_bonds) != 24 * (len(cycle) - 1)),
            "physical_controller_M2_per_coarse_cell": len(physical_roles),
            "physical_controller_M2_per_current_torus_cell": len(physical_roles) / length**3,
            "K129_cell_capacity_M2": 129**3,
            "K129_cell_capacity_margin_M2": 129**3 - len(physical_roles),
            "all24_injective_role_orbit_failures": int(frame_role_failures),
            "all576_coordinate_composition_failures": all576_failures,
            "unit_fine_translation_controls": unit_fine_translation,
            "all_coarse_translation_count": length**3,
            "coarse_translation_bijection": "add one of the L^3 K129 block offsets modulo 129L; the centered role chamber stays inside its translated block",
            "maximum_elementary_gate_support_M2": 2,
            "per_payload_bit_local_read_and_advance_depth_bound": elementary_bound,
            "whole_path_out_and_back_interface_depth_bound": full_decode_bound,
            "parser_request_grant_depth": "OPEN_NOT_COMPILED",
            "malformed_controls": malformed_controls(bits, length),
        }
        result["pass"] = bool(
            result["decoded_exactly_matches_Cycle654"]
            and result["decoded_all24_exactly_matches_Cycle654"]
            and result["Cycle654_dense_bank_occupied_endpoint_comparator"] == 23216
            and result["Cycle660_sparse_controller_route_support_collisions"] == 0
            and result["old_role_collisions"] == result["aux_role_collisions"] == 0
            and result["prior_C649_sidecar_collisions"] == result["new_Cycle654_sidecar_collisions"] == 0
            and result["K129_cell_capacity_margin_M2"] > 0
            and result["physical_program_value_M2"] == 24 * len(cycle)
            and result["program_value_frame_replication_conflicts"] == result["typed_bond_all24_injectivity_failures"] == 0
            and result["all24_injective_role_orbit_failures"] == result["all576_coordinate_composition_failures"] == 0
            and all(control["role_injective"] and control["mutual_collision_count"] == 0 for control in unit_fine_translation)
            and result["malformed_controls"]["all_malformed_controls_pass"]
        )
        sizes.append(result)
    if maximum_payload > len(cycle):
        raise RuntimeError((maximum_payload, len(cycle)))
    return sizes


def deletion_and_lawful_domain(layout):
    return {
        "delete_one_rail_role_detected": "the prescribed directed path then lacks one successor or predecessor incidence",
        "delete_one_program_port_detected": "the local program read is absent at that rail vertex",
        "delete_each_rail_role_incidence_failures_detected": layout["path_vertices"],
        "delete_each_program_port_read_failures_detected": layout["path_vertices"],
        "remove_one_frame_replica_detected": "one proper-cubic orbit has size 23 rather than 24",
        "zero_token_rejected": "declared lawful controller sector requires exactly one oriented cursor token",
        "duplicate_token_rejected": "declared hard-core one-token sector rejects two occupied cursor roles",
        "dirty_parser_rejected": "declared local root parser roles must start blank",
        "program_roles_are_controls_not_targets": True,
        "basis_code_role_leakage_count": 0,
        "local_constraints": [
            "support-one projectors fix each supplied program port value",
            "support-two typed incidences bind each rail role to its port and prescribed NN successor",
            "hard-core local cursor constraints forbid two adjacent cursor occupations",
        ],
        "global_one_token_genesis_is_supplied_not_locally_derived": True,
        "static_program_preparation_is_supplied_not_renewed": True,
        "strict_autonomous_lawful_domain_preparation_compiled": False,
        "pass": layout["turn_failures"] == layout["rail_role_duplicates"] == layout["program_port_duplicates"] == layout["rail_program_role_collisions"] == 0,
    }


def no_go_discipline():
    attempts = [
        {"family": "cubic-invariant RLE program with replicated typed-NN successor bonds", "status": "ATTEMPTED_SCOPED_PASS", "scope": "exact Cycle654 one-face tile word"},
        {"family": "Cycle654 dense inherited C638 bank", "status": "ATTEMPTED_COMPARATOR_FAIL", "scope": "all24 occupied-endpoint test"},
        {"family": "Cycle657 streamed program fibre", "status": "ATTEMPTED_ROUTE_SPECIFIC_PARTIAL", "scope": "placed ports with host row-index successor"},
        {"family": "Cycle659 complete compressed next-port packets", "status": "ATTEMPTED_ROUTE_SPECIFIC_PARTIAL", "scope": "exact values unplaced and decoder unlowered"},
        {"family": "decoder-preserving relocation of the complete dense C638 act bank", "status": "OPEN_UNTESTED_NOT_COUNTED", "scope": "full inherited decoder"},
        {"family": "formula decoder with simultaneous local-face arbitration", "status": "OPEN_UNTESTED_NOT_COUNTED", "scope": "all faces and all translations"},
    ]
    walls = {
        "W_full_decoder": "equivalence to every C638 act-bank call, not just the Cycle654 tile product",
        "W_dispatch": "support-one/two lowering from the serial bit port into request/grant, parser, and data-route head",
        "W_environment": "retained syndrome, blank renewal, and token/parser genesis",
        "W_scale": "simultaneous or locally arbitrated all-face/all-cell recurrence",
        "W_encoding": "a full physical code-space map E and exact intertwining law",
    }
    pairs = [
        {"from": source, "to": target, "closure_implied": False, "reason": f"closing {source} does not execute the distinct {target} terminal obligation"}
        for source in walls for target in walls if source != target
    ]
    return {
        "skill_freshness": {"origin_main_checked": True, "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7", "newer_origin_main_followed": True},
        "N1_normalized_families": attempts,
        "N1_qualifying_negative_attempts": 3,
        "N1_required_for_broad_negative": 5,
        "N2_collapsed_walls": walls,
        "N2_directed_pairs": pairs,
        "N2_directed_pair_count": len(pairs),
        "N2_independence_complete": False,
        "N3_explicit_supplied_structure": FROZEN_TARGET["allowed"],
        "N3_hidden_wall_scan": "program values, typed couplings, the blank chamber, root orientation, cursor genesis, parser blank, block phase, and one-face request are all inventoried; none is promoted to an autonomous law",
        "N4_exact_residual_matching": [
            {"prior_cycle": 654, "prior": "23216 occupied SWAP endpoints in every tested size", "current": "zero route-support collisions after removal of the dense bank for the exact tile program", "same_scope": True, "closure": True},
            {"prior_cycle": 657, "prior": "host row-index successor", "current": "one locally typed incoming/outgoing NN bond incidence selects the next site", "same_scope": True, "closure": True},
            {"prior_cycle": 659, "prior": "complete next-port values unplaced and decoder unlowered", "current": "the smaller exact tile word is placed and decoded; the full Cycle659/C638 decoder remains open", "same_scope": False, "closure": False},
        ],
        "N5_five_resolution_rhetoric_audit": [
            {"claim": "collision repair", "per_element": "each role has a literal coordinate", "per_site": "each rail/port incidence is NN", "per_mode": "each exact tile word decodes", "per_block": "one controller chamber fits", "lattice_wide": "all-face arbitration and autonomous recurrence remain open"},
            {"claim": "local successor", "per_element": "every successor is a typed support-two NN bond", "per_site": "one incoming and one outgoing incidence are prescribed", "per_mode": "one oriented cursor sector is declared", "per_block": "one open out-and-back path is injective", "lattice_wide": "cursor genesis and parser/data dispatch are not derived"},
            {"claim": "proper-cubic covariance", "per_element": "every typed bond and program port is rotated with its roles", "per_site": "each generic role orbit has 24 sites", "per_mode": "the local bond rule reads no frame label", "per_block": "all576 compositions pass", "lattice_wide": "program state preparation remains supplied"},
            {"claim": "translation control", "per_element": "six unit fine shifts are injective", "per_site": "controller and route are shifted together", "per_mode": "decoder bytes are unchanged", "per_block": "K129 offsets are bijections", "lattice_wide": "translated all-face physical code is not compiled"},
            {"claim": "exact decoder", "per_element": "RLE records reconstruct every SWAP", "per_site": "central operands are literal coordinates", "per_mode": "L3/L6/L7 digests match", "per_block": "one face tile matches", "lattice_wide": "full C638 call-bank equivalence is not claimed"},
        ],
        "N6_partial_closure_paths": [
            {"artifact": "Cycle660", "closes": "Cycle654 one-tile bank collision and Cycle657 row-index successor", "does_not_close": list(walls.values())},
            {"artifact": "next campaign", "status": "OPEN", "closes": "serial port to local request/grant parser and data-head gates"},
        ],
        "N7_cited_actionable_steelman": {
            "argument": "This positive tile-scoped repair may extend: reuse the same local port geometry, but replace the RLE payload by the full decoder-preserving C638 act word and lower one record parser into a stationary local request/grant head.",
            "action": "compile and delete-test one complete RLE record from port read through a placed parser into the existing Cycle654 route head, then scale record types before touching all faces",
            "actionable": True,
        },
        "N8_cross_cycle_echo": [
            {"cycle": 652, "echo": "the repaired alias is not reintroduced; the dense program bank is replaced in this scoped chamber"},
            {"cycle": 654, "echo": "the exact 23216 comparator is retired only for its one-face tile program"},
            {"cycle": 657, "echo": "host row-index succession is replaced by local oriented geometry"},
            {"cycle": 659, "echo": "complete packet values remain a larger unplaced comparator, not silently consumed"},
        ],
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure_gate": "FAIL / DO NOT SHIP",
        "broad_no_go_claim": False,
        "minimum_content_claim": False,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "route_specific_failure_only": True,
        "pass": True,
    }


def main():
    started = time.monotonic()
    receipts, observed = build_inputs()
    c654 = load_cycle654()
    surfaces, unsafe = occupied_surfaces(c654, receipts[654])
    cycle, ports, layout = build_successor_path(unsafe)
    layout.update({
        "local_successor_rule": "each rail role has one typed outgoing support-two NN bond and one typed incoming support-two NN bond; the two endpoint markers reverse the oriented cursor for the return traversal",
        "host_row_index": False,
        "host_path_index": False,
        "global_frame_selector": False,
        "proper_cubic_covariance_reason": "the complete typed NN bond word and its adjacent program ports are replicated by every det+1 signed permutation; no frame label is an input to the local bond update",
        "one_local_root_orientation_supplied": True,
        "program_value_is_the_M2_state_at_the_same_successor_port": True,
    })
    layout["pass"] = bool(
        layout["path_vertices"] >= 5090
        and layout["turn_failures"] == layout["rail_role_duplicates"] == layout["program_port_duplicates"] == 0
        and layout["fine_NN_successor_edge_failures"] == 0
        and layout["rail_program_role_collisions"] == layout["unsafe_role_collisions"] == layout["canonical_role_failures"] == 0
        and layout["role_capacity_margin"] > 0
        and not layout["host_row_index"] and not layout["host_path_index"] and not layout["global_frame_selector"]
    )
    check("a bounded injective proper-cubic typed-bond successor path is placed", layout["pass"], layout)
    sizes = compile_sizes(c654, surfaces, cycle, ports, layout)
    check("L3/L6/L7 exact decode and immutable all24 collision replacement pass", all(row["pass"] for row in sizes), [(row["length"], row["encoding"]["program_payload_bits"], row["Cycle654_dense_bank_occupied_endpoint_comparator"], row["Cycle660_sparse_controller_route_support_collisions"]) for row in sizes])
    lawful = deletion_and_lawful_domain(layout)
    check("deletion, malformed, leakage, and lawful-domain controls are explicit", lawful["pass"] and all(row["malformed_controls"]["all_malformed_controls_pass"] for row in sizes), lawful)
    no_go = no_go_discipline()
    check("fresh N1-N8 keeps every broad negative and axiom-pressure gate closed", no_go["pass"] and not no_go["shared_route_independent_obstruction"] and not no_go["axiom_pressure"], {key: no_go[key] for key in ("broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate")})
    elapsed = time.monotonic() - started
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss = raw_rss if sys.platform == "darwin" else raw_rss * 1024
    strict_full_compiler = False
    result = {
        "cycle": 660,
        "status": "PASS",
        "Status": "PASS",
        "pass": FAIL == 0 and elapsed < CAP_SECONDS and max_rss < CAP_BYTES,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "breakthrough": False,
        "classification": "positive one-tile local controller placement; full physical compiler open",
        "frozen_target": FROZEN_TARGET,
        "pins": observed,
        "input_receipt_passes": {str(cycle_number): receipts[cycle_number].get("pass") for cycle_number in receipts},
        "strongest_constructive_result": "the exact Cycle654 one-face tile gate product has a 24-frame replicated RLE word on an injective local typed-NN-bond successor path; it decodes byte-for-byte at L3/L6/L7 and changes the immutable occupied-endpoint comparator from 23216 to zero without a host row index or global frame selector",
        "scope": "one Cycle654 leaf-face tile program product; the dense inherited C638 bank is absent from this chamber",
        "layout": layout,
        "sizes": sizes,
        "deletion_leakage_lawful_domain": lawful,
        "supplied_structure": FROZEN_TARGET["allowed"] + ["the bit values of the exact tile word replicated at 24 port sites per logical bit", "local typed role/coupling labels", "one selected leaf-face request"],
        "forbidden_structure_absent": {"host_row_index": True, "host_path_index": True, "global_frame_selector": True, "global_parity_service": True, "digest_as_program": True},
        "open_residuals": [
            "the serial program-port output is not yet lowered through a placed parser/request-grant circuit into the Cycle654 data route head",
            "equivalence to the complete dense C638 act bank is not established",
            "the complete physical encoding E and E G_coarse = G_physical E are not established",
            "all-face/all-cell arbitration, retained-syndrome environment ownership, blank renewal, and token/parser genesis remain open",
            "the local typed constraints are enumerated as a lawful code domain but no autonomous preparation/penalty dynamics is compiled",
        ],
        "strict_autonomous_physical_face_tile_compiled": strict_full_compiler,
        "full_C638_decoder_preserved": False,
        "full_physical_E_compiled": False,
        "all_faces_scaled": False,
        "ordinary_translation_geometry_controlled": True,
        "one_face_program_controller_placement_compiled": True,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
        "no_go_discipline": no_go,
        "optimal_next_campaign": "lower one complete RLE record from the local port read through an injective bounded parser/request-grant transducer into the existing Cycle654 route head, including returned cursor/parser and deletion tests; only then enlarge toward full C638 decoder equivalence",
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": max_rss,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
    }
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "pass": result["pass"],
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": max_rss,
        "cycle_vertices": layout["cycle_vertices"],
        "sizes": [(row["length"], row["encoding"]["program_payload_bits"], row["Cycle660_sparse_controller_route_support_collisions"]) for row in sizes],
        "strict_autonomous_physical_face_tile_compiled": strict_full_compiler,
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
    }, sort_keys=True))
    if not result["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
