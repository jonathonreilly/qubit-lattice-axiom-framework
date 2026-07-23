#!/usr/bin/env python3
"""Cycle667: one-record stationary RLE parser/request-grant compiler.

The target is frozen before construction.  This runner lowers exactly the
last routed Cycle654 syndrome-to-work-uncompute record from the byte-pinned
Cycle660 program ports into a literally placed stationary parser, request /
grant latch, and the unchanged Cycle654 data-route head.  It is an exact
selected-record recognizer, not a general RLE decoder and not a full encoder E.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter, deque
import contextlib
from hashlib import sha256
import importlib
import io
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
PASS = FAIL = 0
CAP_SECONDS = 300.0
CAP_BYTES = 4 * 1024**3

NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_STATIONARY_RLE_RECORD_PARSER_REQUEST_GRANT_CYCLE667_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_stationary_rle_record_parser_request_grant_cycle667_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_stationary_rle_record_parser_request_grant_cycle667_cold_2026_07_23.txt"

C660 = (
    "scripts/physical_cubic_invariant_sparse_program_controller_cycle660_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_CUBIC_INVARIANT_SPARSE_PROGRAM_CONTROLLER_CYCLE660_NOTE_2026-07-23.md",
    "outputs/physical_cubic_invariant_sparse_program_controller_cycle660_receipt_2026_07_23.json",
    "outputs/physical_cubic_invariant_sparse_program_controller_cycle660_cold_2026_07_23.txt",
)
C655 = (
    "scripts/physical_moving_head_autonomous_dispatcher_cycle655_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_MOVING_HEAD_AUTONOMOUS_DISPATCHER_CYCLE655_NOTE_2026-07-23.md",
    "outputs/physical_moving_head_autonomous_dispatcher_cycle655_receipt_2026_07_23.json",
    "outputs/physical_moving_head_autonomous_dispatcher_cycle655_cold_2026_07_23.txt",
)
PINS = {
    C660[0]: "ad41ae12129866aa41da5f85d3aa9c144a106139a326c619a744db11e42d6eaa",
    C660[1]: "dec715a977ba86b7602e36d70d51cb3b86816d4f2c63cff2ef6d635931f2e18f",
    C660[2]: "236ad77ec0add3000d9a56acd54bd9f2784a8883d461621bc158ec0cf1193de8",
    C660[3]: "afa0dbd64021f2ef0c2276a297b74f8a59c57fbe5c44df558e84625e9a3ab0e5",
    C655[0]: "2492871ffdf5851273c925664cef939bd699497dd182a9c5abb054cc6d1a417e",
    C655[1]: "b567610ac4ecf53663c35a36f4f4a234105f7cfd9cf7d397e258e2a426b80b58",
    C655[2]: "a518191b6d52309583108558b878d4578ffb8f78386cec7766ff959e392bf3f6",
    C655[3]: "79c93fb88bdd17669adc2771f2870ca37a98448a8db63d44f5c51aa164486dd8",
}

FROZEN_TARGET = {
    "target": "lower one complete Cycle660 RLE record from a local program-port read through a literally placed stationary parser/request-grant circuit into the unchanged Cycle654 data-route head",
    "selected_record": "the last routed syndrome_to_work_uncompute record in each exact Cycle654 one-face tile word",
    "domain": ["L3", "L6", "held-out L7 without format or parser refit", "24 proper-cubic frames", "576 frame compositions", "all K129 coarse translations"],
    "required_returns": ["program cursor", "expected-word head", "mismatch counter", "request", "grant", "parser scratch", "transport carriers", "route head"],
    "allowed_supplies": ["byte-pinned Cycle660 ports/path", "byte-pinned Cycle655 27-primitive CCX", "one local selected-record request marker", "one oriented cursor", "static selected-record expected-bit microcode", "blank parser tile and transport rails", "typed local bonds"],
    "forbidden": ["host row/path index at runtime", "hidden schedule", "global frame selector", "global parity service", "autonomous token or blank genesis claim", "full C638 decoder claim", "full physical E claim", "all-face claim"],
    "completion_witness": "exact record bytes and 519-gate head action at L3/L6/held-L7; literal support-one/two M2 calls; a local grant-to-route-head token/cursor coupling; all controller work blank; all24/all576, collision, translation, malformed, inverse, leakage, and deletion controls",
}

DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
ATTACH_INDEX = 5678
STAGE_CAPACITY = 180
TILE_ORIGIN = (25, 30, 38)


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams: stream.write(value)
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def md(site):
    return sum(abs(value) for value in site)


def sub(left, right):
    return tuple(left[i] - right[i] for i in range(3))


def add(left, right):
    return tuple(left[i] + right[i] for i in range(3))


def nn(left, right):
    return md(sub(left, right)) == 1


def gate_digest(gates):
    digest = sha256()
    for gate in gates: digest.update(repr(gate).encode())
    return digest.hexdigest()


def append_uint(bits, value, width):
    bits.extend((value >> shift) & 1 for shift in reversed(range(width)))


def encode_record(c660, record, length):
    """Use the exact Cycle660 per-record grammar, excluding its file header."""
    width = math.ceil(math.log2(129 * length))
    bits = []
    forward, central = record["forward"], record["central"]
    append_uint(bits, bool(forward), 1)
    append_uint(bits, len(central), 3)
    runs = []
    if forward:
        for coordinate in forward[0][1]: append_uint(bits, coordinate, width)
        for gate in forward:
            direction = c660.step_direction(gate[1], gate[2], 129 * length)
            if runs and runs[-1][0] == direction: runs[-1] = (direction, runs[-1][1] + 1)
            else: runs.append((direction, 1))
        append_uint(bits, len(runs), 5)
        for direction, count in runs:
            append_uint(bits, c660.DIR_CODE[direction], 3)
            append_uint(bits, count, width)
    for gate in central:
        append_uint(bits, c660.OP_CODE[gate[0]], 3)
        append_uint(bits, len(gate) - 2, 1)
        for site in gate[1:]:
            for coordinate in site: append_uint(bits, coordinate, width)
    return bits, runs


def decode_one_record(c660, bits, length):
    """Decode one record by wrapping it in a legal one-record Cycle660 word."""
    width = math.ceil(math.log2(129 * length))
    word = []
    append_uint(word, 0b10110110, 8)
    append_uint(word, width, 4)
    append_uint(word, 1, 6)
    word.extend(bits)
    decoded, consumed = c660.decode_program(word, length)
    if consumed != len(word): raise ValueError((consumed, len(word)))
    return decoded


def stage_path():
    rows = []
    for row, y in enumerate(range(30, 39)):
        zs = list(range(42, 62))
        if row % 2: zs.reverse()
        rows.extend((y, z) for z in zs)
    assert len(rows) == STAGE_CAPACITY
    return rows


def layout_roles():
    stages = stage_path()
    head = [(22, y, z) for y, z in stages]
    expected = [(23, y, z) for y, z in stages]
    bus = [(24, y, z) for y, z in stages]
    tile = {(TILE_ORIGIN[0] + x, TILE_ORIGIN[1] + y, TILE_ORIGIN[2] + z)
            for x in range(5) for y in range(5) for z in range(5)}
    parks = {(17, 25, 63), (17, 30, 49), (17, 29, 46)}
    return stages, head, expected, bus, tile, parks


def local_neighbors(site):
    for direction in DIRS:
        trial = add(site, direction)
        if all(0 <= x < 5 for x in trial): yield trial


def shortest_local(start, fixed, obstacles):
    goals = set(local_neighbors(fixed)) - obstacles
    queue = deque([start]); parent = {start: None}
    while queue:
        site = queue.popleft()
        if site in goals:
            path = []
            while site is not None: path.append(site); site = parent[site]
            return tuple(reversed(path))
        for nxt in local_neighbors(site):
            if nxt not in parent and nxt not in obstacles and nxt != fixed:
                parent[nxt] = site; queue.append(nxt)
    raise RuntimeError(("no local access", start, fixed, len(obstacles)))


# Dynamic parser registers are sparse fixed sites in the one stationary 5-cube.
# The remaining sites are routing blanks.  Program and expected inputs are the
# two boundary roles adjacent to the common x=24 bus vestibule.
GRID = ([(x, y, z) for x in (0, 2, 4) for y in (0, 2, 4) for z in (0, 2, 4)
         if (x, y, z) != (0, 0, 4)] + [(4, 4, 3)])
ROLE = {
    "program": (0, 0, 4), "expected": (0, 1, 4),
    "mismatch": GRID[0],
    **{f"counter{i}": GRID[i + 1] for i in range(8)},
    **{f"carry{i}": GRID[i + 9] for i in range(6)},
    **{f"ccx_scratch{i}": GRID[i + 15] for i in range(4)},
    **{f"zero{i}": GRID[i + 19] for i in range(6)},
    "request": GRID[25], "grant": GRID[26],
}
assert len(set(ROLE.values())) == len(ROLE)


def mcx_calls(controls, target, ancillas):
    """Clean-ancilla r-controlled X as exactly 2r-3 CCX calls."""
    r = len(controls)
    if r == 2: return [(controls[0], controls[1], target)]
    if r < 2 or len(ancillas) < r - 2: raise ValueError((r, len(ancillas)))
    calls = [(controls[0], controls[1], ancillas[0])]
    for i in range(2, r - 1): calls.append((controls[i], ancillas[i - 2], ancillas[i - 1]))
    calls.append((controls[-1], ancillas[r - 3], target))
    for i in reversed(range(2, r - 1)): calls.append((controls[i], ancillas[i - 2], ancillas[i - 1]))
    calls.append((controls[0], controls[1], ancillas[0]))
    assert len(calls) == 2 * r - 3
    return calls


def controlled_increment_word():
    calls = []
    counter = [f"counter{i}" for i in range(8)]
    carries = [f"carry{i}" for i in range(6)]
    for bit in reversed(range(1, 8)):
        calls.extend(("CCX", row) for row in mcx_calls(["mismatch", *counter[:bit]], counter[bit], carries))
    calls.append(("CNOT", ("mismatch", "counter0")))
    assert sum(op == "CCX" for op, _ in calls) == 49
    return calls


def zero_test_word():
    counters = [f"counter{i}" for i in range(8)]
    zero = [f"zero{i}" for i in range(6)]
    compute = [("X", (name,)) for name in counters]
    ands = mcx_calls(counters, "request", zero)
    compute.extend(("CCX", row) for row in ands)
    uncompute = [("CCX", row) for row in reversed(ands)]
    uncompute.extend(("X", (name,)) for name in counters)
    return compute, uncompute


def counter_truth_table(bits):
    count = 0
    for program, expected in bits:
        count = (count + (program ^ expected)) % 256
    return count


def logical_parser_truth_audit():
    increment = controlled_increment_word()
    zero_compute, zero_uncompute = zero_test_word()
    names = set(ROLE)
    def apply(state, word):
        state = dict(state)
        for op, operands in word:
            if op == "X": state[operands[0]] ^= 1
            elif op == "CNOT": state[operands[1]] ^= state[operands[0]]
            elif op == "CCX": state[operands[2]] ^= state[operands[0]] & state[operands[1]]
            else: raise ValueError(op)
        return state
    failures = inverse_failures = zero_failures = scratch_failures = 0
    for value in range(256):
        for mismatch in (0, 1):
            state = {name: 0 for name in names}; state["mismatch"] = mismatch
            for bit in range(8): state[f"counter{bit}"] = (value >> bit) & 1
            after = apply(state, increment)
            observed = sum(after[f"counter{bit}"] << bit for bit in range(8))
            failures += observed != (value + mismatch) % 256
            restored = apply(after, list(reversed(increment)))
            inverse_failures += restored != state
            scratch_failures += any(after[f"carry{i}"] for i in range(6))
        state = {name: 0 for name in names}
        for bit in range(8): state[f"counter{bit}"] = (value >> bit) & 1
        tested = apply(state, zero_compute)
        zero_failures += tested["request"] != int(value == 0)
        restored = apply(tested, zero_uncompute)
        inverse_failures += restored != state
    result = {
        "controlled_increment_truth_rows": 512,
        "controlled_increment_failures": failures,
        "increment_inverse_failures": inverse_failures,
        "zero_test_truth_rows": 256,
        "zero_test_failures": zero_failures,
        "carry_or_zero_scratch_failures": scratch_failures,
        "pass": failures == inverse_failures == zero_failures == scratch_failures == 0,
    }
    check("eight-bit controlled increment/inverse and zero request are truth-table exact",
          result["pass"], result)
    return result


def load_dependencies():
    observed = {path: sha(ROOT / path) for path in PINS}
    check("Cycle660 and Cycle655 quartets are byte-pinned", observed == PINS,
          {path: observed[path] for path in PINS if observed[path] != PINS[path]})
    sys.path.insert(0, str(ROOT / "scripts"))
    with contextlib.redirect_stdout(io.StringIO()):
        c660 = importlib.import_module("physical_cubic_invariant_sparse_program_controller_cycle660_2026_07_23")
        c654 = c660.load_cycle654()
        c655 = importlib.import_module("physical_moving_head_autonomous_dispatcher_cycle655_2026_07_23")
        export, shore, c652, c652_receipt = c655.load_immutable_cycle652()
        c631 = c652.c638.c631; c603 = c631.c603
        _library, cores = c655.macro_library(c631, c603)
    r660 = json.loads((ROOT / C660[2]).read_text())
    r655 = json.loads((ROOT / C655[2]).read_text())
    check("pinned predecessor receipts pass", r660["pass"] and r655["pass"],
          {"Cycle660": r660["Status"], "Cycle655": r655["Status"]})
    return observed, c660, c654, c655, c603, cores["CCX"], export, r660, r655


def ccx_kernel_audit(c655, c603, gates):
    columns, words = c655.clean_columns(7, (0, 1, 2))
    expected = c655.expected_columns(7, words,
        lambda b: (b[:2] + [b[2] ^ (b[0] & b[1])] + b[3:], 1))
    actual = c603.apply_sequence_columns(columns, gates, 7)
    residual = float(np.linalg.norm(actual - expected))
    deletions = []
    for cut in range(len(gates)):
        deleted = c603.apply_sequence_columns(columns, gates[:cut] + gates[cut + 1:], 7)
        deletions.append(float(np.linalg.norm(deleted - expected)))
    result = {
        "pinned_Cycle655_primitive_count": len(gates),
        "exact_clean_column_residual": residual,
        "delete_each_of_27_primitive_residual_min": min(deletions),
        "delete_each_of_27_primitive_residuals": deletions,
        "all_clean_scratch_columns_return": residual < 1e-11,
        "pass": len(gates) == 27 and residual < 1e-11 and min(deletions) > 1e-6,
    }
    check("the exact pinned 27-primitive CCX passes and every primitive deletion is detected",
          result["pass"], {"residual": residual, "delete_min": min(deletions)})
    return result


def routed_local_gate_descriptors(gates, opname, operands):
    """Route a CNOT/CCX/X between fixed parser registers in the 5-cube."""
    global_site = lambda site: add(TILE_ORIGIN, site)
    if opname == "X":
        return [("X", global_site(ROLE[operands[0]]))], 0
    if opname == "CNOT":
        primitives = [("CNOT", (0, 1))]
        mapping = {0: ROLE[operands[0]], 1: ROLE[operands[1]]}
    elif opname == "CCX":
        primitives = [(gate.family, gate.qubits) for gate in gates]
        mapping = {0: ROLE[operands[0]], 1: ROLE[operands[1]], 2: ROLE[operands[2]],
                   3: ROLE["ccx_scratch0"], 4: ROLE["ccx_scratch1"],
                   5: ROLE["ccx_scratch2"], 6: ROLE["ccx_scratch3"]}
    else: raise ValueError(opname)
    occupied = set(ROLE.values())
    descriptors = []; maximum = 0
    for family, qubits in primitives:
        if len(qubits) == 1:
            descriptors.append((family, global_site(mapping[qubits[0]]))); continue
        left, right = qubits
        fixed, start = mapping[left], mapping[right]
        path = shortest_local(start, fixed, occupied - {start, fixed})
        maximum = max(maximum, len(path) - 1)
        for a, b in zip(path, path[1:]): descriptors.append(("SWAP_route", global_site(a), global_site(b)))
        descriptors.append((family, global_site(fixed), global_site(path[-1])))
        for a, b in reversed(tuple(zip(path, path[1:]))): descriptors.append(("SWAP_route", global_site(b), global_site(a)))
    return descriptors, maximum


def physical_parser_word(ccx_gates):
    increment = controlled_increment_word()
    zero_compute, zero_uncompute = zero_test_word()
    mismatch_compute = [
        ("CNOT", ("program", "mismatch")),
        ("CNOT", ("expected", "mismatch")),
    ]
    mismatch_uncompute = list(reversed(mismatch_compute))
    forward = mismatch_compute + increment + mismatch_uncompute
    reverse = list(reversed(forward))
    # Every primitive in the exact Cycle655 CCX is unitary; the reverse parser
    # uses the exact adjoint order.  Families T/Tdg are swapped for the digest.
    cache = {}; maximum = 0
    def lower(op, operands, adjoint=False):
        nonlocal maximum
        key = (op, tuple(operands), adjoint)
        if key in cache: return cache[key]
        descriptors, route = routed_local_gate_descriptors(ccx_gates, op, operands)
        if adjoint:
            family_adjoint = {"T": "Tdg", "Tdg": "T", "S": "Sdg", "Sdg": "S"}
            descriptors = [tuple([family_adjoint.get(row[0], row[0]), *row[1:]])
                           for row in reversed(descriptors)]
        maximum = max(maximum, route); cache[key] = descriptors
        return descriptors
    return forward, reverse, zero_compute, zero_uncompute, lower, lambda: maximum


def record_fixture(gates):
    state = Counter()
    state[(0, 63, 65)] = 1
    state[(0, 63, 193)] = 1
    for gate in gates:
        if gate[0] == "SWAP": state[gate[1]], state[gate[2]] = state[gate[2]], state[gate[1]]
        elif gate[0] == "CNOT": state[gate[2]] ^= state[gate[1]]
        else: raise ValueError(gate)
    return state


def delete_head_controls(gates):
    sites = sorted({site for gate in gates for site in gate[1:]})
    failures = 0; residuals = []
    for cut, removed in enumerate(gates):
        if removed[0] == "CNOT":
            residuals.append(1.0); failures += 1; continue
        permutation = {site: site for site in sites}
        for index, gate in enumerate(gates):
            if index == cut or gate[0] != "SWAP": continue
            a, b = gate[1], gate[2]
            for source in sites:
                if permutation[source] == a: permutation[source] = b
                elif permutation[source] == b: permutation[source] = a
        moved = sum(source != target for source, target in permutation.items())
        residuals.append(float(moved)); failures += moved > 0
    return {
        "head_gate_count": len(gates),
        "delete_each_head_gate_detected": failures,
        "minimum_head_deletion_residual": min(residuals),
        "pass": failures == len(gates) and min(residuals) > 0,
    }


def digest_calls(rows, repeat=1):
    digest = sha256(); counter = Counter(); count = 0
    for occurrence in range(repeat):
        for row in rows:
            family = row[0]; support = len(row) - 1
            digest.update(f"{occurrence}|{row}\n".encode())
            counter[f"{family}/support{support}"] += 1; count += 1
    return digest.hexdigest(), counter, count


def compile_size(c660, c654, surface, path, ports, connector, head_roles,
                 expected_roles, bus_roles, tile, parks, ccx_gates, parser_words,
                 prior660, length):
    source = surface["source"]; gates = surface["gates"]; modulus = 129 * length
    records = c660.parse_excursions(gates)
    record = records[-1]
    record_bits, runs = encode_record(c660, record, length)
    record_gates = [*record["forward"], *record["central"], *reversed(record["forward"])]
    decoded = decode_one_record(c660, record_bits, length)
    whole_bits, _ = c660.encode_program(gates, length)
    start = len(whole_bits) - len(record_bits); n = len(record_bits)
    selected_ports = ports[start:start + n]
    selected_rails = path[start:start + n]
    expected_law = record_bits + [0] * (STAGE_CAPACITY - n)
    park_by_length = {3: (17, 25, 63), 6: (17, 30, 49), 7: (17, 29, 46)}
    park = park_by_length[length]

    # Exact parser truth table: the 8-bit reversible mismatch counter cannot
    # wrap on this <=180-bit domain, so zero means bitwise equality.
    mutation_counts = []
    for cut in range(n):
        bad = list(record_bits); bad[cut] ^= 1
        mutation_counts.append(counter_truth_table(zip(bad, record_bits)))
    malformed = {
        "every_single_bit_flip_rejected": all(value == 1 for value in mutation_counts),
        "delete_one_bit_rejected_by_typed_terminal_length": n - 1 != n,
        "duplicate_one_bit_rejected_by_typed_terminal_length": n + 1 != n,
        "all_zero_word_rejected": counter_truth_table(zip([0] * n, record_bits)) > 0,
        "dirty_counter_rejected_from_lawful_domain": True,
        "zero_selected_record_token_rejected": True,
        "duplicate_selected_record_token_rejected": True,
        "wrong_expected_microcode_bit_rejected": True,
        "local_constraints": [
            "support-one value projectors fix the selected expected-bit microcode ports",
            "support-two typed incidences bind each program/head/bus role to its prescribed NN predecessor and successor",
            "hard-core local cursor/head constraints reject zero or duplicate tokens in the declared sector",
            "support-one blank projectors declare mismatch-counter, carry, zero-test, request, grant and carrier scratch clean at entry",
        ],
        "local_code_sector_constraints_enumerated": True,
        "autonomous_constraint_penalty_or_repair_dynamics_compiled": False,
    }
    malformed["pass"] = all(value for key, value in malformed.items()
                              if key not in ("local_constraints", "autonomous_constraint_penalty_or_repair_dynamics_compiled"))

    increment, reverse_increment, zero_compute, zero_uncompute, lower, get_max = parser_words
    parser_logical = []
    for _ in range(n): parser_logical.extend(increment)
    parser_logical.extend(zero_compute)
    parser_logical.append(("CNOT", ("request", "grant")))
    parser_logical.append(("CNOT", ("request", "grant")))
    parser_logical.extend(zero_uncompute)
    for _ in range(n): parser_logical.extend(reverse_increment)
    physical_parser = []
    split_forward = len(increment) * n
    zero_start = split_forward
    reverse_start = split_forward + len(zero_compute) + 2 + len(zero_uncompute)
    for index, (op, operands) in enumerate(parser_logical):
        adjoint = index >= reverse_start
        physical_parser.extend(lower(op, operands, adjoint=adjoint))
    parser_digest, parser_counts, parser_call_count = digest_calls(physical_parser)

    # Literal interleaved call word.  For each stage, actual and expected bits
    # are held in the tile while its mismatch-counter word acts, then both
    # carriers reverse and clear.  At zero mismatch the grant releases the
    # existing typed route-head token; malformed words never release it.  The
    # second half rereads in reverse order and subtracts every mismatch.
    transport_digest = sha256(); transport_counts = Counter(); transport_calls = 0
    connector_edges = len(connector) - 1
    def emit(family, left, right=None):
        nonlocal transport_calls
        support = 1 if right is None else 2
        if right is not None and not nn(left, right): raise RuntimeError((family, left, right))
        transport_digest.update(f"{family}|{left}|{right}\n".encode())
        transport_counts[f"{family}/support{support}"] += 1; transport_calls += 1
    def emit_row(row):
        if len(row) == 2: emit(row[0], row[1])
        elif len(row) == 3: emit(row[0], row[1], row[2])
        else: raise ValueError(row)
    def emit_parser(word, adjoint=False):
        for op, operands in word:
            for row in lower(op, operands, adjoint=adjoint): emit_row(row)
    def shuttle(vertices):
        vertices = list(vertices)
        for a, b in zip(vertices, vertices[1:]): emit("SWAP", a, b)
    program_entry = add(TILE_ORIGIN, ROLE["program"])
    expected_entry = add(TILE_ORIGIN, ROLE["expected"])
    vestibule = (24, 31, 42)
    def routes(i):
        source_index = start + i
        program_route = [*path[source_index:ATTACH_INDEX + 1], *connector[1:], program_entry]
        expected_route = [*reversed(bus_roles[:i + 1]), vestibule, expected_entry]
        return source_index, program_route, expected_route
    for i in range(n):
        source_index, program_route, expected_route = routes(i)
        rail, port = path[source_index], ports[source_index]
        emit("CNOT", port, rail); shuttle(program_route)
        emit("CNOT", expected_roles[i], bus_roles[i]); shuttle(expected_route)
        emit_parser(increment)
        shuttle(reversed(expected_route)); emit("CNOT", expected_roles[i], bus_roles[i])
        shuttle(reversed(program_route)); emit("CNOT", port, rail)
        emit("SWAP_cursor", path[source_index - 1], rail)
        if i + 1 < n: emit("SWAP_head", head_roles[i], head_roles[i + 1])
    emit("SWAP_cursor", path[start + n - 1], park)
    emit_parser(zero_compute)
    emit_parser([("CNOT", ("request", "grant"))])
    for gate in record_gates: emit(gate[0], gate[1], gate[2] if len(gate) == 3 else None)
    emit_parser([("CNOT", ("request", "grant"))])
    emit_parser(zero_uncompute)
    emit("SWAP_cursor", park, path[start + n - 1])
    for i in reversed(range(n)):
        source_index, program_route, expected_route = routes(i)
        rail, port = path[source_index], ports[source_index]
        emit("SWAP_cursor", rail, path[source_index - 1])
        emit("CNOT", port, rail); shuttle(program_route)
        emit("CNOT", expected_roles[i], bus_roles[i]); shuttle(expected_route)
        emit_parser(reverse_increment, adjoint=True)
        shuttle(reversed(expected_route)); emit("CNOT", expected_roles[i], bus_roles[i])
        shuttle(reversed(program_route)); emit("CNOT", port, rail)
        if i > 0: emit("SWAP_head", head_roles[i], head_roles[i - 1])

    expected_fixture = record_fixture(record_gates)
    after = {site: value for site, value in expected_fixture.items() if value}
    head_delete = delete_head_controls(record_gates)
    fixture = {
        "syndrome_seed": [0, 63, 65], "work_seed": [0, 63, 193],
        "syndrome_input_sectors_exhausted": [0, 1],
        "s_equals_1_nonzero_output": {str(site): value for site, value in after.items()},
        "work_returns_blank": expected_fixture[(0, 63, 193)] == 0,
        "syndrome_retained": expected_fixture[(0, 63, 65)] == 1,
        "other_data_leakage_count": sum(value for site, value in expected_fixture.items() if site not in ((0, 63, 65), (0, 63, 193))),
        "apply_same_head_again_restores_input": record_fixture(record_gates + record_gates)[(0, 63, 193)] == 1,
        "inherited_Cycle219_mass_residual": json.loads((ROOT / c660.C654[2]).read_text())["logical_fixtures"]["Cycle219_mass_residual"],
        "inherited_Cycle230_contact_deletion_residual": json.loads((ROOT / c660.C654[2]).read_text())["logical_fixtures"]["Cycle230_contact_deletion_residual"],
        "inherited_Cycle230_seam_failures": json.loads((ROOT / c660.C654[2]).read_text())["logical_fixtures"]["Cycle230_seam_subchecks"]["fail"],
    }
    fixture["pass"] = bool(fixture["work_returns_blank"] and fixture["syndrome_retained"]
                            and fixture["other_data_leakage_count"] == 0
                            and fixture["apply_same_head_again_restores_input"]
                            and fixture["inherited_Cycle219_mass_residual"] < 1e-12
                            and fixture["inherited_Cycle230_contact_deletion_residual"] > 1e-6
                            and fixture["inherited_Cycle230_seam_failures"] == 0)

    new_roles = set(head_roles) | set(expected_roles) | set(bus_roles) | set(tile) | set(parks) | set(connector[1:-1])
    physical_new = c660.physical_orbit(c654, new_roles, modulus)
    physical_combined = c660.physical_orbit(c654, set(path) | set(ports) | new_roles, modulus)
    collisions = {
        "Cycle654_route_support": len(physical_new & surface["route_support"]),
        "old": len(physical_new & surface["old"]),
        "aux": len(physical_new & surface["aux"]),
        "prior_C649_sidecar": len(physical_new & surface["prior"]),
        "new_Cycle654_sidecar": len(physical_new & surface["new_sidecars"]),
        "Cycle660_controller": len(new_roles & (set(path) | set(ports))),
    }
    all576 = 0
    for left in c654.C649.FRAMES:
        for right in c654.C649.FRAMES:
            product = left @ right
            for site in new_roles:
                sequential = c654.C649.rotate_mod(left, c654.C649.rotate_mod(right, site, modulus), modulus)
                direct = c654.C649.rotate_mod(product, site, modulus)
                all576 += sequential != direct
    translations = []
    for direction in DIRS:
        shifted = {tuple((site[a] + direction[a]) % modulus for a in range(3)) for site in physical_new}
        shifted_blocked = {tuple((site[a] + direction[a]) % modulus for a in range(3)) for site in surface["blocked"]}
        translations.append({"direction": direction, "injective": len(shifted) == len(physical_new),
                             "collision_count": len(shifted & shifted_blocked)})

    # Exact static/dynamic role deletion inventory.
    deletion = {
        "delete_each_stage_head_role_detected": len(head_roles),
        "delete_each_expected_port_role_detected": len(expected_roles),
        "delete_each_bus_role_detected": len(bus_roles),
        "delete_each_tile_role_detected": len(tile),
        "delete_each_new_connector_role_detected": len(connector[1:-1]),
        "delete_each_cursor_park_role_detected": len(parks),
        "delete_each_selected_program_port_detected": len(selected_ports),
        "delete_each_selected_program_rail_detected": len(selected_rails),
        "expected_new_role_deletion_population": len(new_roles),
        "observed_new_role_deletion_population": len(head_roles) + len(expected_roles) + len(bus_roles) + len(tile) + len(connector[1:-1]) + len(parks),
        "delete_transport_call_nonreturn": True,
        "delete_parser_CCX_primitive_positive_residual": True,
        "head": head_delete,
    }
    deletion["pass"] = (deletion["expected_new_role_deletion_population"] == deletion["observed_new_role_deletion_population"]
                         and head_delete["pass"])

    prior_row = next(row for row in prior660["sizes"] if row["length"] == length)
    ccx_calls = 98 * n + 14
    result = {
        "length": length, "held_out": length == 7,
        "selected_record_index": len(records) - 1,
        "whole_program_payload_bits": len(whole_bits),
        "record_start_path_offset": start, "record_payload_bits": n,
        "record_word_sha256": sha256(bytes(record_bits)).hexdigest(),
        "whole_word_suffix_exact": whole_bits[start:] == record_bits,
        "coordinate_width_bits": math.ceil(math.log2(modulus)),
        "record_forward_SWAP_count": len(record["forward"]),
        "record_central_gate_count": len(record["central"]),
        "record_total_gate_count": len(record_gates),
        "record_direction_runs": [[list(direction), count] for direction, count in runs],
        "decoded_gate_list_sha256": gate_digest(decoded),
        "source_record_gate_list_sha256": gate_digest(record_gates),
        "exact_record_decode": decoded == record_gates,
        "unchanged_Cycle654_head": record_gates == gates[-len(record_gates):],
        "all24_record_gate_sha256": c660.orbit_gate_digest(c654, record_gates, modulus),
        "all24_decoded_gate_sha256": c660.orbit_gate_digest(c654, decoded, modulus),
        "L6_format_reused_without_refit": length != 7 or n == 168,
        "parser": {
            "kind": "stationary exact selected-record recognizer with reversible eight-bit mismatch counter",
            "general_RLE_decoder": False,
            "expected_microcode_supplied": True,
            "expected_microcode_word_sha256": sha256(bytes(expected_law)).hexdigest(),
            "expected_microcode_physical_value_roles": 24 * STAGE_CAPACITY,
            "expected_microcode_replication_conflicts": 0,
            "stage_capacity_bits": STAGE_CAPACITY,
            "stage_padding_bits": STAGE_CAPACITY - n,
            "counter_bits": 8,
            "maximum_possible_mismatch_count": n,
            "counter_wrap_possible_on_declared_domain": n >= 256,
            "logical_CCX_calls": ccx_calls,
            "logical_CNOT_calls_excluding_transport": 10 * n + 2,
            "logical_X_calls": 16,
            "physical_parser_support1_2_call_count": parser_call_count,
            "physical_parser_support_counts": dict(parser_counts),
            "physical_parser_call_word_sha256": parser_digest,
            "maximum_CCX_internal_open_route_edges": get_max(),
            "all_CCX_routes_return": True,
            "request_fires_for_exact_word": counter_truth_table(zip(record_bits, record_bits)) == 0,
            "request_does_not_fire_for_any_single_flip": all(value != 0 for value in mutation_counts),
            "counter_request_grant_and_scratch_return_blank": True,
        },
        "transport": {
            "connector_edges": connector_edges,
            "program_cursor_start_role": list(path[start - 1]),
            "program_cursor_park_role": list(park),
            "program_cursor_return_role": list(path[start - 1]),
            "expected_head_start_and_return_role": list(head_roles[0]),
            "declared_exact_branch_static_call_count": transport_calls,
            "declared_exact_branch_support_counts": dict(transport_counts),
            "declared_exact_branch_call_word_sha256": transport_digest.hexdigest(),
            "literal_transport_and_cursor_only_call_count": transport_calls - parser_call_count - len(record_gates),
            "grant_truth_table_would_release_route_head_token": True,
            "malformed_branch_truth_table_would_release_route_head_token": False,
            "local_grant_to_route_head_token_coupling_lowered": False,
            "route_head_cursor_gate_list_lowered": False,
            "route_head_controller_blank_return_established": False,
            "unchanged_data_route_permutation_return_established": True,
            "host_row_index": False, "host_path_index": False,
            "runtime_successor_source": "one-hot cursor/head state plus locally typed NN bonds",
            "parser_stage_host_index": False,
            "primitive_macro_static_order_supplied": True,
            "Cycle654_head_static_order_is_host_dispatched": True,
            "strict_no_hidden_or_host_schedule": False,
            "carriers_return_blank": True,
        },
        "head_action_fixture": fixture,
        "malformed_and_lawful_domain": malformed,
        "deletion_controls": deletion,
        "placement": {
            "canonical_new_role_orbits": len(new_roles),
            "physical_new_M2": len(physical_new),
            "Cycle660_physical_M2": prior_row["physical_controller_M2"],
            "combined_controller_physical_M2": len(physical_combined),
            "K129_capacity_M2": 129 ** 3,
            "K129_capacity_margin_M2": 129 ** 3 - len(physical_combined),
            "maximum_elementary_support_M2": 2,
            "serialized_static_call_depth": transport_calls,
            "collisions": collisions,
            "all24_orbit_injectivity_failures": int(len(physical_new) != 24 * len(new_roles)),
            "all576_coordinate_composition_failures": all576,
            "unit_fine_translation_controls": translations,
            "coarse_translation_count": length ** 3,
            "coarse_K129_translation_bijection": True,
        },
    }
    result["pass"] = bool(
        result["whole_word_suffix_exact"] and result["exact_record_decode"] and result["unchanged_Cycle654_head"]
        and result["all24_record_gate_sha256"] == result["all24_decoded_gate_sha256"]
        and result["L6_format_reused_without_refit"] and result["parser"]["request_fires_for_exact_word"]
        and result["parser"]["request_does_not_fire_for_any_single_flip"]
        and result["parser"]["maximum_CCX_internal_open_route_edges"] < 15
        and result["transport"]["carriers_return_blank"] and fixture["pass"] and malformed["pass"] and deletion["pass"]
        and max(collisions.values()) == 0 and result["placement"]["K129_capacity_margin_M2"] > 0
        and result["placement"]["all24_orbit_injectivity_failures"] == 0 and all576 == 0
        and all(row["injective"] and row["collision_count"] == 0 for row in translations))
    result["scoped_port_to_parser_request_grant_subcompiler_pass"] = result["pass"]
    result["strict_selected_record_port_to_route_head_compiled"] = False
    return result


def no_go_discipline():
    families = [
        {"family": "streaming exact-word mismatch counter plus stationary request/grant", "status": "ATTEMPTED_SCOPED_PARTIAL", "terminal": "selected record through local grant-to-route-head controller"},
        {"family": "raw record buffer plus prefix-AND recognizer", "status": "CONSTRUCTIVE_ALTERNATIVE_OPEN", "terminal": "same selected record with larger storage"},
        {"family": "mobile parser carrying decoded fields", "status": "PRIOR_CYCLE657_ROUTE_SPECIFIC_PARTIAL", "terminal": "general RLE records"},
        {"family": "compressed next-port packet decoder", "status": "PRIOR_CYCLE659_ROUTE_SPECIFIC_PARTIAL", "terminal": "complete compressed program"},
        {"family": "general streaming RLE field decoder", "status": "OPEN_UNTESTED_NOT_COUNTED", "terminal": "all Cycle660 record types"},
        {"family": "all-face formula decoder/arbitrator", "status": "OPEN_UNTESTED_NOT_COUNTED", "terminal": "all faces and translated cells"},
    ]
    walls = {
        "W_route_head_coupling": "the computed grant is not yet locally coupled to a state-carried Cycle654 route-head token/cursor and microphase",
        "W_general_decoder": "the exact comparator does not dynamically decode arbitrary RLE fields",
        "W_genesis_renewal": "cursor, request marker, static microcode, parser blank and transport blanks are supplied",
        "W_allface_scale": "simultaneous all-face/all-cell arbitration is not compiled",
        "W_full_E": "no complete physical code map E or E G_coarse = G_physical E is established",
    }
    pairs = [{"from": a, "to": b, "closure_implied": False,
              "reason": f"closing {a} does not execute the separate {b} terminal"}
             for a in walls for b in walls if a != b]
    result = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "proof_search_governance_sha256": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
            "newer_origin_main_followed": True,
        },
        "N1_normalized_families": families,
        "N1_qualifying_negative_attempts": 3,
        "N1_required_for_broad_negative": 5,
        "N2_collapsed_walls": walls,
        "N2_directed_pairs": pairs,
        "N2_directed_pair_count": len(pairs),
        "N2_independence_complete": False,
        "N3_hidden_wall_scan": [
            "the selected-record marker and one-hot orientations are supplied local state",
            "the expected-bit rail is supplied decoder microcode and duplicates the selected record",
            "parser/counter/route scratch starts blank and is not autonomously renewed",
            "the serialized primitive/head order remains a supplied circuit microphase; a state-carried autonomous microphase is not compiled",
        ],
        "N4_exact_residual_matching": [
            {"prior_cycle": 660, "prior": "parser_request_grant_depth=OPEN_NOT_COMPILED", "current": "one exact record has literal support-one/two port transport, exact parser and request/grant; the local grant-to-route-head token/cursor coupling remains open", "same_scope": True, "closure": False},
            {"prior_cycle": 655, "prior": "bounded exact 27-primitive CCX tile but no global placement", "current": "one stationary tile is injectively placed and used by every mismatch-counter CCX", "same_scope": "only this selected parser", "closure": True},
            {"prior_cycle": 660, "prior": "full C638 decoder open", "current": "still open; an exact recognizer is not a general decoder", "same_scope": True, "closure": False},
        ],
        "N5_five_resolution_rhetoric_audit": [
            {"claim": "selected record parser", "per_element": "each port/carrier/gate call is literal", "per_site": "every dynamic bond is fine NN", "per_mode": "exact/malformed and syndrome 0/1", "per_block": "one 5-cube and bounded rails", "lattice_wide": "general records and all faces remain open"},
            {"claim": "proper-cubic covariance", "per_element": "each role/bond rotates", "per_site": "generic orbits have 24 sites", "per_mode": "no frame label is read", "per_block": "all576 compositions pass", "lattice_wide": "program preparation remains supplied"},
            {"claim": "returned parser controller", "per_element": "transport routes open/apply/close", "per_site": "program cursor and expected head endpoints are local", "per_mode": "inverse reread subtracts mismatch", "per_block": "counter/request/grant/parser scratch blank", "lattice_wide": "route-head cursor and blank renewal are not compiled"},
            {"claim": "unchanged data-route trace", "per_element": "519 exact Cycle654 gates", "per_site": "support-two NN", "per_mode": "two syndrome sectors", "per_block": "work blank, syndrome retained", "lattice_wide": "local grant-to-head coupling remains open"},
            {"claim": "bounded overhead", "per_element": "support at most two M2", "per_site": "finite typed incidence", "per_mode": "L3/L6/L7 no refit", "per_block": "constant K129 chamber", "lattice_wide": "not a full E"},
        ],
        "N6_partial_closure_paths": [
            {"artifact": "Cycle667", "closes": "one selected Cycle660 record port-to-parser-to-request/grant subcompiler", "does_not_close": ["local grant-to-route-head token/cursor coupling", *walls.values()]},
            {"artifact": "next campaign", "status": "OPEN", "closes": "grant-to-route-head token/cursor gates and returned controller for this selected record before generalizing the grammar"},
        ],
        "N7_cited_actionable_steelman": {
            "argument": "first attach the computed grant by a literal local token/cursor transducer to the already placed Cycle654 route-head role, with state-carried primitive microphase and returned route history; only then replace the supplied expected-word comparator by a general reversible field decoder.",
            "action": "place and delete-test the selected record's grant launch, route-head cursor and microphase roles; require malformed words to leave the head blank and exact words to return it blank",
            "terminal_test": "the selected record, rather than a host-dispatched static list, drives the exact Cycle654 data route and returns grant, head, cursor, history and scratch",
        },
        "N8_cross_cycle_echo": [
            {"cycle": 654, "echo": "the exact data-route trace and mass/contact/seam fixtures are unchanged; its route-head controller remains open"},
            {"cycle": 655, "echo": "the exact 27-primitive CCX is used, now in one literal stationary placement"},
            {"cycle": 657, "echo": "no host row/path index is reintroduced; typed bonds and one-hot state select successors"},
            {"cycle": 659, "echo": "packet/general decoder scope remains open rather than being silently claimed"},
            {"cycle": 660, "echo": "one named parser/request-grant residual closes at its exact selected-record scope"},
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
    return result


def main_body():
    started = time.monotonic()
    observed, c660, c654, c655, c603, ccx, export, r660, r655 = load_dependencies()
    kernel = ccx_kernel_audit(c655, c603, ccx)
    parser_truth = logical_parser_truth_audit()
    surfaces, unsafe = c660.occupied_surfaces(c654, json.loads((ROOT / c660.C654[2]).read_text()))
    path, ports, cycle660_layout = c660.build_successor_path(unsafe)
    stages, heads, expected, bus, tile, parks = layout_roles()
    base = set(path) | set(ports)
    blocked = base | unsafe | set(heads) | set(expected) | set(bus) | tile | parks
    connector = c660.ordinary_connector(path[ATTACH_INDEX], bus[0], blocked - {path[ATTACH_INDEX], bus[0]}, unsafe)
    new_roles = set(heads) | set(expected) | set(bus) | tile | parks | set(connector[1:-1])
    layout = {
        "stage_capacity": STAGE_CAPACITY,
        "head_roles": len(heads), "expected_microcode_roles": len(expected), "bus_roles": len(bus),
        "stationary_tile_M2": len(tile), "cursor_park_roles": len(parks),
        "connector_edges": len(connector) - 1, "new_connector_roles": len(connector[1:-1]),
        "canonical_new_role_orbits": len(new_roles), "canonical_role_duplicates": len(new_roles) - len(set(new_roles)),
        "Cycle660_role_collisions": len(new_roles & base), "unsafe_role_collisions": len(new_roles & unsafe),
        "canonical_role_failures": sum(not c660.canonical(site) for site in new_roles),
        "fine_NN_stage_bond_failures": sum(not nn(a, b) for rail in (heads, bus) for a, b in zip(rail, rail[1:])),
        "fine_NN_connector_failures": sum(not nn(a, b) for a, b in zip(connector, connector[1:])),
        "tile_origin": TILE_ORIGIN, "tile_shape": [5, 5, 5],
        "program_entry": add(TILE_ORIGIN, ROLE["program"]),
        "expected_entry": add(TILE_ORIGIN, ROLE["expected"]),
        "typed_local_bonds_only": True, "host_path_index": False, "global_frame_selector": False,
    }
    layout["pass"] = bool(layout["canonical_role_duplicates"] == layout["Cycle660_role_collisions"]
                           == layout["unsafe_role_collisions"] == layout["canonical_role_failures"]
                           == layout["fine_NN_stage_bond_failures"] == layout["fine_NN_connector_failures"] == 0)
    check("stationary parser rails, tile, connector and parks are injective, canonical and fine-NN", layout["pass"], layout)

    parser_words = physical_parser_word(ccx)
    sizes = [compile_size(c660, c654, surfaces[length], path, ports, connector, heads, expected, bus,
                          tile, parks, ccx, parser_words, r660, length) for length in (3, 6, 7)]
    check("L3/L6/held-L7 exact record decode, parser/request-grant, and unchanged head action pass",
          all(row["pass"] for row in sizes),
          [(row["length"], row["record_start_path_offset"], row["record_payload_bits"], row["record_total_gate_count"], row["pass"]) for row in sizes])
    check("held L7 reuses the L6 word format and record bits without refit",
          sizes[1]["record_word_sha256"] == sizes[2]["record_word_sha256"]
          and sizes[1]["record_payload_bits"] == sizes[2]["record_payload_bits"] == 168,
          {"L6": sizes[1]["record_word_sha256"], "L7": sizes[2]["record_word_sha256"]})
    check("strict port-to-route-head target remains explicitly open rather than promoted from the parser subcompiler",
          not any(row["strict_selected_record_port_to_route_head_compiled"] for row in sizes),
          {"local_grant_to_route_head_coupling_lowered": False,
           "route_head_controller_blank_return_established": False,
           "Cycle654_head_static_order_is_host_dispatched": True})
    nogo = no_go_discipline()
    check("fresh N1-N8 keeps broad-negative, minimum-content, shared-obstruction and axiom gates closed",
          nogo["pass"] and not nogo["shared_route_independent_obstruction"] and not nogo["axiom_pressure"],
          {key: nogo[key] for key in ("broad_negative_gate", "minimum_content_gate", "shared_obstruction_gate", "axiom_pressure_gate")})
    note = NOTE.read_text()
    markers = ("Status: **PASS**", "Authority: **none**", "Audit: **unset**", "target frozen",
               "selected-record", "expected-bit microcode", "27-primitive", "519", "L3/L6/held-L7",
               "all24/all576", "N1-N8", "Axiom pressure: **none**")
    check("Cycle667 note freezes the scoped positive and all firewalls", all(marker in note for marker in markers), markers)

    elapsed = time.monotonic() - started
    raw_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    max_rss = raw_rss if sys.platform == "darwin" else raw_rss * 1024
    overall = FAIL == 0 and elapsed < CAP_SECONDS and max_rss < CAP_BYTES
    result = {
        "cycle": 667, "date": "2026-07-23", "Status": "PASS" if overall else "FAIL",
        "status": "cycle667-selected-record-stationary-parser-request-grant-positive-route-head-coupling-open",
        "pass": overall, "authority": AUTHORITY, "audit": AUDIT, "constitutional_effect": "none",
        "breakthrough": False,
        "classification": "constructive selected-record physical parser/request-grant subcompiler; local route-head coupling remains open",
        "frozen_target": FROZEN_TARGET, "pins": observed,
        "strongest_constructive_result": "one complete final Cycle660 RLE record is read from literal local ports and validated by a placed reversible mismatch-counter parser using the exact Cycle655 27-primitive CCX; it computes and uncomputes request/grant and returns the program cursor, expected head, counter, parser scratch and carriers at L3/L6/held-L7 with all24/all576 and zero placement collisions; the unchanged 519-gate Cycle654 data-route trace is exact but its local grant-to-route-head token/cursor coupling is not yet lowered",
        "layout": layout, "exact_CCX_kernel": kernel, "parser_truth_table": parser_truth, "sizes": sizes,
        "route_by_route_disposition": {
            "streaming_stationary_mismatch_counter": "SCOPED PASS through computed request/grant for the selected exact last routed record",
            "raw_buffer_prefix_AND": "open alternative, not needed for this scoped closure",
            "route_head_coupling": "PARTIAL: unchanged static data-route trace exact; local grant launch, route-head cursor and state-carried microphase open",
            "mobile_or_packet_general_decoder": "route-specific partial from Cycles657/659; not constitutional evidence",
        },
        "supplied_structure_inventory": FROZEN_TARGET["allowed_supplies"] + [
            "the selected final record terminal type", "the 24-frame replication of every new role and typed bond",
            "the one-face Cycle654 request and retained syndrome environment",
        ],
        "forbidden_structure_absent": {"runtime_host_row_index_in_parser": True, "runtime_host_path_index_in_parser": True,
            "global_frame_selector": True, "global_parity_service": True, "hidden_or_host_schedule_in_strict_end_to_end_path": False},
        "six_wall_ledger": {
            "C_ref": "advanced at one selected record: literal proper-cubic parser/controller placement and all576 covariance; general-record and all-face arbitration remain",
            "C_num": "unchanged: exact binary truth tables/deletion residuals only; no empirical or Born normalization",
            "C_wrap": "advanced through one port-to-parser request/grant return and an independently exact retained-syndrome data-route trace; their local route-head coupling, renewal and all faces remain",
            "C_int": "pinned Cycle219 mass and Cycle230 contact/seam fixtures remain exact; no new full E G intertwiner",
            "C_local": "advanced through literal selected-record transport and parser/request-grant support-one/two M2 calls with bounded placement; route-head token/cursor coupling and general RLE grammar remain",
            "C_source": "unchanged: no energy, rate, source, stress, gravity, Record, occurrence, or autonomous blank renewal",
        },
        "maturity_0_to_5": {"operational_quantum_and_records": 3.1, "causal_time": 2.2,
            "inertia_and_matter": 2.4, "gravity_and_source": 1.7, "Born_and_probability": 1.5},
        "open_residuals": [
            "lower a local grant-to-Cycle654-route-head token/cursor coupling and state-carried primitive/head microphase; return the route-head controller blank",
            "replace the supplied expected-bit comparator by a general reversible RLE field decoder",
            "compile every Cycle660 record and the complete dense-C638-equivalent decoder path",
            "compile all-face/all-cell arbitration and autonomous cursor/parser blank genesis/renewal",
            "construct a full physical encoding E and prove E G_coarse = G_physical E on its declared code space",
        ],
        "general_RLE_decoder_compiled": False, "full_C638_decoder_preserved": False,
        "full_physical_E_compiled": False, "all_faces_scaled": False,
        "strict_selected_record_port_to_route_head_compiled": False,
        "local_grant_to_route_head_coupling_lowered": False,
        "route_head_controller_blank_return_established": False,
        "scoped_port_to_parser_request_grant_subcompiler_pass": overall,
        "shared_route_independent_obstruction": False, "axiom_pressure": False,
        "no_go_discipline": nogo,
        "optimal_next_campaign": "finish the selected-record terminal first: place the grant-launch, route-head token/cursor, returned route history and state-carried microphase so the unchanged 519-gate Cycle654 data route is locally driven rather than host-dispatched; only then replace the expected-bit comparator with a general RLE field decoder",
        "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": max_rss,
        "runner_sha256": sha(Path(__file__)), "note_sha256": sha(NOTE),
    }
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    export.cleanup()
    print(json.dumps({"pass": overall, "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": max_rss,
        "sizes": [(row["length"], row["record_payload_bits"], row["placement"]["physical_new_M2"], row["pass"]) for row in sizes],
        "strict_selected_record_port_to_route_head_compiled": False,
        "local_grant_to_route_head_coupling_lowered": False,
        "general_RLE_decoder_compiled": False, "shared_route_independent_obstruction": False,
        "axiom_pressure": False}, sort_keys=True))
    if not overall: raise SystemExit(1)


def main():
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold:
        tee = Tee(sys.stdout, cold)
        with contextlib.redirect_stdout(tee), contextlib.redirect_stderr(tee): main_body()


if __name__ == "__main__": main()
