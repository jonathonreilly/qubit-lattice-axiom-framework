"""Cycle 818 independent adversarial period-census checker.

This checker never imports or executes the Cycle-818 primary.  It reconstructs
the landed inventory from SHA-pinned caches, evolves every strict-table row
with a separately implemented Boolean-gate engine, and treats any missed or
mis-certified row as a refutation.
"""

from __future__ import annotations

import ast
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
import importlib
import importlib.abc
import json
from math import gcd
import os
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic
from typing import Iterable


AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
    "logs/runner-cache/frontier_cycle814_deep_silence_probe_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

PRIMARY_MODULE = "frontier_cycle818_period_structure_census_2026_07_28"
PRIMARY_PATH = "scripts/frontier_cycle818_period_structure_census_2026_07_28.py"
BLOCKLIST_HITS: list[str] = []


class _PrimaryBlocklist(importlib.abc.MetaPathFinder):
    """Trap the primary before Python can read or execute its source."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname == PRIMARY_MODULE:
            BLOCKLIST_HITS.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryBlocklist()
sys.meta_path.insert(0, PRIMARY_FIREWALL)


def probe_primary_blocklist() -> dict[str, object]:
    caught = False
    message = ""
    try:
        importlib.import_module(PRIMARY_MODULE)
    except ImportError as exc:
        caught = True
        message = str(exc)
    return {
        "module": PRIMARY_MODULE,
        "path": PRIMARY_PATH,
        "caught_before_source_load": caught,
        "message": message,
        "hits": tuple(BLOCKLIST_HITS),
        "present_in_sys_modules": PRIMARY_MODULE in sys.modules,
        "access_mode": "IMPORT_BLOCKED; PRIMARY_SOURCE_NOT_READ_OR_EXECUTED",
    }


PRIMARY_BLOCKLIST_PROBE = probe_primary_blocklist()

# The controller core supplies only the landed circuit/state constructors.
# All repeated state evolution below is implemented in this checker.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


EXPECTED_AUDIT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
    AUDIT_INPUT_PATHS[2]:
        "521e1217d0e36440220fb6226e4872638dbe0abfda3df36986337a06acf4e89c",
}

RUNNER_REFS = (
    {
        "cycle": 790,
        "commit": "935e46cac19230caf123c8810af367d7cd843469",
        "path": "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
        "blob": "c322bb975900b2611c3f42d19da347a1dd5bfc56",
        "sha256": "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    },
    {
        "cycle": 791,
        "commit": "6255426f36a48494de43ccc8bd3eb9592e584c00",
        "path": "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
        "blob": "f026960526f2f2a8d990a5a7856b02217ea798ce",
        "sha256": "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    },
    {
        "cycle": 797,
        "commit": "3cf5931aa901fb45cbb2030eb119c5a09dd32c02",
        "path": "scripts/frontier_cycle797_deep_horizon_continuation_2026_07_28.py",
        "blob": "5d70ba232efcbd4f8c0a2d798f735907d4207b81",
        "sha256": "7ece6f7c818a4dcffb3019c610ca0861998f19cfae0287e23fe98562c1a09698",
    },
    {
        "cycle": 814,
        "commit": "6cb13f88f3430a201374b5f1d8b01cf000bc6b35",
        "path": "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
        "blob": "19ba617ad1f6be9f8fdc637b764dc7b38cae8d7b",
        "sha256": "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
    },
)

CACHE_REFS = (
    {
        "cycle": 790,
        "commit": "935e46cac19230caf123c8810af367d7cd843469",
        "path": "logs/runner-cache/frontier_cycle790_horizon_extension_2026_07_28.txt",
        "blob": "f58caebdd7a3e519b679dd0cdd098c1c80c05e34",
        "sha256": "2f428ebba168dc9f9e2602c43409ab7e80b24587f873d895ab54d6ebf26c8634",
    },
    {
        "cycle": 791,
        "commit": "6255426f36a48494de43ccc8bd3eb9592e584c00",
        "path": "logs/runner-cache/frontier_cycle791_open_keys_resolution_2026_07_28.txt",
        "blob": "460cb3ae346ef10440d5a3ef03a3c19299374edf",
        "sha256": "9ab66b127341c63a664ae1631527ae803358a1dd2d2dcacc4639f49aaeadfc8d",
    },
    {
        "cycle": 797,
        "commit": "3cf5931aa901fb45cbb2030eb119c5a09dd32c02",
        "path": "logs/runner-cache/frontier_cycle797_deep_horizon_continuation_2026_07_28.txt",
        "blob": "cb956f584b81899965d961aa356e14dd98a32d38",
        "sha256": "e44f1b3739b7f78680c963462a4d2e1ae3277f5b75118a1b2cc2b3ba74c8005a",
    },
    {
        "cycle": 814,
        "commit": "6cb13f88f3430a201374b5f1d8b01cf000bc6b35",
        "path": AUDIT_INPUT_PATHS[2],
        "blob": "a81e0f017f68a71af48329eb7d139dba21d0648b",
        "sha256": EXPECTED_AUDIT_SHA256[AUDIT_INPUT_PATHS[2]],
    },
)

SIBLING_CACHE_NAME = "frontier_cycle801_silent_strata_deep_scan_2026_07_28.txt"
SIBLING_EXPECTED_SHA256 = (
    "33c10abc491b78bd2e346263d70ccf77f9b82227a5dcfa8fbe86fa62e891bf3d"
)
SIBLING_EXPECTED_BLOB = "b50059cfb5123439a8848cd32dc17515ae364712"
SIBLING_LANDED_COMMIT = "d42048111b5eb75f7a283db2e9039d57017a26cf"

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(label: str, detail: object) -> None:
    OUTPUT_LINES.append(f"{label} :: {compact(detail)}")


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}")
    return passed


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def git_bytes(commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def git_oid(commit: str, path: str) -> str:
    completed = subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout.strip()


def json_line(payload: str, prefix: str) -> object:
    lines = [line for line in payload.splitlines() if line.startswith(prefix)]
    if len(lines) != 1:
        raise AssertionError(("expected one JSON line", prefix, len(lines)))
    suffix = lines[0][len(prefix):].strip()
    if suffix.startswith("::"):
        suffix = suffix[2:].strip()
    return json.loads(suffix)


def parse_cache_header(payload: str) -> dict[str, object]:
    rows: dict[str, str] = {}
    for line in payload.splitlines():
        if line == "----- stdout -----":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            rows[key.strip()] = value.strip()
    return {
        "runner": rows.get("runner"),
        "runner_sha256": rows.get("runner_sha256"),
        "exit_code": int(rows.get("exit_code", "-1")),
        "status": rows.get("status"),
    }


def normalize_row(
    key: tuple[int, tuple[int, ...], int],
    period: int,
    preperiod: int,
    source: str,
) -> dict[str, object]:
    return {
        "key": key,
        "k": key[0],
        "positions": key[1],
        "event": key[2],
        "period": int(period),
        "preperiod": int(preperiod),
        "source": source,
    }


def literal_audit_paths() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    nodes = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    return (
        len(nodes) == 1
        and isinstance(nodes[0].value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in nodes[0].value.elts
        )
        and tuple(ast.literal_eval(nodes[0].value)) == AUDIT_INPUT_PATHS
    )


def load_landed_sources() -> dict[str, object]:
    """Read the six non-sibling evidence resources and verify their pins."""
    audit_rows = []
    current_payloads: dict[str, bytes] = {}
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes()
        current_payloads[relative] = payload
        actual = sha256(payload).hexdigest()
        audit_rows.append(
            {
                "path": relative,
                "exists": path.is_file(),
                "worktree_relative": (
                    not Path(relative).is_absolute()
                    and path.resolve().is_relative_to(ROOT.resolve())
                ),
                "sha256": actual,
                "expected_sha256": EXPECTED_AUDIT_SHA256[relative],
                "match": actual == EXPECTED_AUDIT_SHA256[relative],
            }
        )

    runner_by_cycle = {int(row["cycle"]): row for row in RUNNER_REFS}
    runner_rows = []
    for reference in RUNNER_REFS:
        actual_oid = git_oid(str(reference["commit"]), str(reference["path"]))
        runner_rows.append(
            {
                **reference,
                "actual_blob": actual_oid,
                "blob_match": actual_oid == reference["blob"],
                "content_sha256_recomputed": int(reference["cycle"]) == 814,
                "actual_worktree_sha256": (
                    sha256(current_payloads[AUDIT_INPUT_PATHS[1]]).hexdigest()
                    if int(reference["cycle"]) == 814
                    else None
                ),
            }
        )

    cache_payloads: dict[int, str] = {}
    cache_rows = []
    for reference in CACHE_REFS:
        cycle = int(reference["cycle"])
        payload = (
            current_payloads[AUDIT_INPUT_PATHS[2]]
            if cycle == 814
            else git_bytes(str(reference["commit"]), str(reference["path"]))
        )
        text = payload.decode("utf-8")
        header = parse_cache_header(text)
        expected_runner = runner_by_cycle[cycle]
        actual_sha = sha256(payload).hexdigest()
        actual_blob = git_blob_sha(payload)
        landed_blob = git_oid(str(reference["commit"]), str(reference["path"]))
        cache_payloads[cycle] = text
        cache_rows.append(
            {
                **reference,
                "actual_blob": actual_blob,
                "landed_blob": landed_blob,
                "actual_sha256": actual_sha,
                "header": header,
                "match": (
                    actual_blob == reference["blob"]
                    and landed_blob == reference["blob"]
                    and actual_sha == reference["sha256"]
                    and header["runner"] == expected_runner["path"]
                    and header["runner_sha256"] == expected_runner["sha256"]
                    and header["exit_code"] == 0
                    and header["status"] == "ok"
                ),
            }
        )

    source_pass = (
        literal_audit_paths()
        and all(
            row["exists"] and row["worktree_relative"] and row["match"]
            for row in audit_rows
        )
        and all(
            row["blob_match"]
            and (
                int(row["cycle"]) != 814
                or row["actual_worktree_sha256"] == row["sha256"]
            )
            for row in runner_rows
        )
        and all(row["match"] for row in cache_rows)
    )
    return {
        "audit_rows": tuple(audit_rows),
        "runner_rows": tuple(runner_rows),
        "cache_rows": tuple(cache_rows),
        "cache_payloads": cache_payloads,
        "literal_audit_input_tuple": literal_audit_paths(),
        "all_audit_inputs_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in audit_rows
        ),
        "pass": source_pass,
    }


def row_signature(row: dict[str, object]) -> tuple[object, int, int]:
    return (row["key"], int(row["period"]), int(row["preperiod"]))


def extract_inventory(cache_payloads: dict[int, str]) -> dict[str, object]:
    """Scan every certification-bearing surface in the four landed caches."""
    payload790 = cache_payloads[790]
    data790 = json_line(payload790, "DATA B ")
    rows790_summary = []
    for event, positions, period in data790["periodic_keys"]:
        key = (2, tuple(int(value) for value in positions), int(event))
        rows790_summary.append(
            normalize_row(key, int(period), 0, "Cycle790 DATA B periodic_keys")
        )

    ctable_lines = [
        line
        for line in payload790.splitlines()
        if line.startswith("DATA C_TABLE ")
    ]
    ctable_pattern = re.compile(
        r"^DATA C_TABLE row=\d+ event=(\d+) positions=\(([^)]*)\)"
        r".* T256=CYCLE\(period=(\d+),entry=(\d+),"
        r"state_period=(\d+),closure=(\d+)\)$"
    )
    rows790_table = []
    for line in ctable_lines:
        match = ctable_pattern.match(line)
        if match is None:
            continue
        event, positions_text, residual, entry, state_period, closure = match.groups()
        positions = tuple(
            int(value.strip())
            for value in positions_text.split(",")
            if value.strip()
        )
        if int(closure) - int(entry) != int(state_period):
            raise AssertionError(("Cycle790 malformed cycle row", line))
        key = (2, positions, int(event))
        rows790_table.append(
            normalize_row(
                key,
                int(state_period),
                int(entry),
                "Cycle790 exhaustive DATA C_TABLE T256 scan",
            )
        )
        if int(residual) != int(state_period):
            raise AssertionError(("Cycle790 residual/state period drift", line))

    payload791 = cache_payloads[791]
    data791 = json_line(payload791, "DATA B ")
    d_rows791 = []
    for line in payload791.splitlines():
        if line.startswith("DATA D_KEY_ROW_"):
            d_rows791.append(json.loads(line.split(" ", 2)[2]))
    rows791_cycles = []
    for row in d_rows791:
        if row["state_period"] is not None:
            key = (
                2,
                tuple(int(value) for value in row["positions"]),
                int(row["event"]),
            )
            rows791_cycles.append(
                normalize_row(
                    key,
                    int(row["state_period"]),
                    int(row["cycle_entry"]),
                    "Cycle791 exhaustive DATA D_KEY_ROW scan",
                )
            )

    data797 = json_line(cache_payloads[797], "DATA B_T1024_IDENTITY ")["T1024"]
    rows797 = []
    for row in data797["cycle_certifications"]:
        event, positions = row["key"]
        key = (2, tuple(int(value) for value in positions), int(event))
        rows797.append(
            normalize_row(
                key,
                int(row["state_period"]),
                int(row["entry"]),
                "Cycle797 DATA B_T1024_IDENTITY cycle_certifications",
            )
        )

    payload814 = cache_payloads[814]
    depth_rows814 = [
        json.loads(line[len("SILENT_KEY_DEPTH_ROW "):])
        for line in payload814.splitlines()
        if line.startswith("SILENT_KEY_DEPTH_ROW ")
    ]
    rows814_depth = []
    for row in depth_rows814:
        if row["cycle_period"] is not None:
            k, positions, event = row["key"]
            key = (int(k), tuple(int(value) for value in positions), int(event))
            rows814_depth.append(
                normalize_row(
                    key,
                    int(row["cycle_period"]),
                    int(row["cycle_start_t"]),
                    "Cycle814 exhaustive SILENT_KEY_DEPTH_ROW scan",
                )
            )
    certificate814 = json_line(
        payload814,
        "PASS CERTIFICATE_B_EVENTS_OR_NULL_WITH_PROVEN_COVERAGE ",
    )
    coverage814 = certificate814["coverage_accounting"]
    rows814_certificate = []
    for row in coverage814["certified_cycle_periods"]:
        k, positions, event = row["key"]
        key = (int(k), tuple(int(value) for value in positions), int(event))
        rows814_certificate.append(
            normalize_row(
                key,
                int(row["period"]),
                0,
                "Cycle814 CERTIFICATE_B certified_cycle_periods",
            )
        )

    sig790_summary = {row_signature(row) for row in rows790_summary}
    sig790_table = {row_signature(row) for row in rows790_table}
    sig791 = {row_signature(row) for row in rows791_cycles}
    sig797 = {row_signature(row) for row in rows797}
    sig814_depth = {row_signature(row) for row in rows814_depth}
    sig814_certificate = {row_signature(row) for row in rows814_certificate}
    strict_rows = tuple(
        sorted(rows797 + rows814_certificate, key=lambda row: row["key"])
    )
    strict_signatures = {row_signature(row) for row in strict_rows}
    independently_discovered = (
        sig790_table | sig791 | sig814_depth
    )
    missed = independently_discovered - strict_signatures
    unexplained = strict_signatures - independently_discovered

    completeness_pass = (
        int(data790["keys"]) == len(ctable_lines) == 176
        and int(data790["cycles"]) == len(rows790_summary) == 11
        and sig790_summary == sig790_table
        and int(data791["checkpoint_count"]) == len(d_rows791) == 164
        and len(rows791_cycles) == 1
        and next(iter(sig791)) == ((2, (0, 9), 2), 288, 0)
        and int(data797["T1024_counts"]["cycle"]) == len(rows797) == 12
        and int(data797["T1024_counts"]["uncovered"]) == 0
        and sig790_table | sig791 == sig797
        and len(depth_rows814) == int(coverage814["key_count"]) == 24
        and int(coverage814["certified_cycle_count"]) == len(rows814_depth) == 2
        and sig814_depth == sig814_certificate
        and coverage814["partial_keys"] == []
        and int(coverage814["observed_total_key_transitions"])
        == int(coverage814["expected_total_key_transitions"])
        and int(coverage814["observed_complete_family_word_applications"])
        == int(coverage814["expected_complete_family_word_applications"])
        and len(strict_rows) == len(strict_signatures) == 14
        and not missed
        and not unexplained
    )
    return {
        "strict_rows": strict_rows,
        "Cycle790": {
            "table_rows_scanned": len(ctable_lines),
            "summary_cycle_count": len(rows790_summary),
            "table_cycle_count": len(rows790_table),
            "cycle_signatures": tuple(sorted(sig790_table)),
            "summary_table_exact_agreement": sig790_summary == sig790_table,
        },
        "Cycle791": {
            "key_rows_scanned": len(d_rows791),
            "new_cycle_signatures": tuple(sorted(sig791)),
        },
        "Cycle797": {
            "declared_cycle_count": data797["T1024_counts"]["cycle"],
            "uncovered": data797["T1024_counts"]["uncovered"],
            "cycle_signatures": tuple(sorted(sig797)),
            "equals_Cycle790_plus_Cycle791": sig790_table | sig791 == sig797,
        },
        "Cycle814": {
            "depth_rows_scanned": len(depth_rows814),
            "cycle_signatures": tuple(sorted(sig814_depth)),
            "certificate_signatures": tuple(sorted(sig814_certificate)),
            "partial_keys": coverage814["partial_keys"],
            "transition_accounting_exact": (
                coverage814["observed_total_key_transitions"]
                == coverage814["expected_total_key_transitions"]
            ),
        },
        "independently_discovered_signatures": tuple(
            sorted(independently_discovered)
        ),
        "strict_signatures": tuple(sorted(strict_signatures)),
        "missed_by_strict_table": tuple(sorted(missed)),
        "strict_rows_not_found_by_independent_scans": tuple(sorted(unexplained)),
        "pass": completeness_pass,
    }


def compile_word(word: Iterable[object]) -> tuple[tuple[int, int], ...]:
    """Compile X/CNOT/Toffoli into (control-mask, target-mask) instructions."""
    compiled = []
    expected_arity = {"X": 1, "CNOT": 2, "TOF": 3}
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind not in expected_arity or len(wires) != expected_arity[kind]:
            raise AssertionError(("unsupported gate", kind, wires))
        if len(set(wires)) != len(wires):
            raise AssertionError(("repeated gate wire", kind, wires))
        if kind == "X":
            controls = 0
            target = 1 << wires[0]
        elif kind == "CNOT":
            controls = 1 << wires[0]
            target = 1 << wires[1]
        else:
            controls = (1 << wires[0]) | (1 << wires[1])
            target = 1 << wires[2]
        compiled.append((controls, target))
    return tuple(compiled)


def tuple_to_int(state: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(state))


def int_to_tuple(state: int, width: int) -> tuple[int, ...]:
    return tuple((state >> index) & 1 for index in range(width))


def apply_word(state: int, compiled: tuple[tuple[int, int], ...]) -> int:
    for controls, target in compiled:
        if state & controls == controls:
            state ^= target
    return state


def build_fixtures() -> tuple[
    tuple[object, ...],
    dict[int, tuple[tuple[int, int], int]],
]:
    program = K.interleaved_program(2)
    banks, links = K.B.chain_genesis(2)
    state_tuple = tuple(int(bit) for bit in K.M.pack_state(banks, links))
    width = len(state_tuple)
    allocator = compile_word(K.M.global_allocator_word(2))
    fixtures = {}
    for event in range(4):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before_tuple = tuple(
            int(bit) for bit in K.M.prepare_endpoint(state_tuple, direction)
        )
        before = tuple_to_int(before_tuple)
        fixtures[event] = (direction, before)
        state_tuple = int_to_tuple(apply_word(before, allocator), width)
    return program, fixtures


def synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(token_positions)
    word = []
    for _ in range(len(program)):
        live = frozenset(positions)
        for station, instruction in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(instruction))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    if positions != tuple(token_positions):
        raise AssertionError(("token rotation did not close", token_positions, positions))
    return tuple(word)


def proper_divisors(number: int) -> tuple[int, ...]:
    values = []
    for candidate in range(1, int(number ** 0.5) + 1):
        if number % candidate == 0:
            values.append(candidate)
            quotient = number // candidate
            if quotient != candidate and quotient != number:
                values.append(quotient)
    return tuple(sorted(set(values)))


def state_hash(state: int) -> str:
    return sha256(str(state).encode("ascii")).hexdigest()


def verify_rows_independently(
    rows: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    """Evolve each row without K.run_orbit or K.A.apply_semantic."""
    program, fixtures = build_fixtures()
    verified = []
    for source_row in rows:
        positions = tuple(int(value) for value in source_row["positions"])
        event = int(source_row["event"])
        period = int(source_row["period"])
        direction, before = fixtures[event]
        compiled = compile_word(synchronous_word(program, positions))

        # The certified t=0 anchor is the independently composed first sweep.
        anchor = apply_word(before, compiled)
        state = anchor
        divisors = proper_divisors(period)
        divisor_returns = []
        for moment in range(1, period + 1):
            state = apply_word(state, compiled)
            if moment in divisors and state == anchor:
                divisor_returns.append(moment)
        recurrence = state == anchor
        minimal = recurrence and not divisor_returns
        anchor_sha = state_hash(anchor)
        closure_sha = state_hash(state)
        row = {
            **source_row,
            "direction": direction,
            "word_gate_count": len(compiled),
            "anchor_t": 0,
            "closure_t": period,
            "anchor_state_sha256": anchor_sha,
            "anchor_plus_period_state_sha256": closure_sha,
            "full_state_recurrence": recurrence,
            "proper_divisors": divisors,
            "proper_divisor_returns": tuple(divisor_returns),
            "proper_divisors_rejected": len(divisors) - len(divisor_returns),
            "minimal_period": minimal,
            "minimality_justification": (
                "all proper divisors rejected; the minimal period must divide "
                "any verified recurrence period"
            ),
            "preperiod_zero": int(source_row["preperiod"]) == 0 and recurrence,
            "anchor_hashes_match": anchor_sha == closure_sha,
        }
        row["pass"] = (
            row["preperiod_zero"]
            and recurrence
            and minimal
            and row["anchor_hashes_match"]
        )
        verified.append(row)
    return tuple(verified)


def factorization(number: int) -> tuple[tuple[int, int], ...]:
    remaining = int(number)
    factors = []
    candidate = 2
    while candidate * candidate <= remaining:
        exponent = 0
        while remaining % candidate == 0:
            remaining //= candidate
            exponent += 1
        if exponent:
            factors.append((candidate, exponent))
        candidate = 3 if candidate == 2 else candidate + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def gcd_many(values: Iterable[int]) -> int:
    result = 0
    for value in values:
        result = gcd(result, int(value))
    return result


def lcm_many(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        value = int(value)
        result = result // gcd(result, value) * value
    return result


def exact_arithmetic(rows: tuple[dict[str, object], ...]) -> dict[str, object]:
    periods = tuple(int(row["period"]) for row in rows)
    counts = Counter(periods)
    unique = tuple(sorted(counts))
    factors = {period: factorization(period) for period in unique}
    strata = {
        period: tuple(
            sorted({int(row["k"]) for row in rows if row["period"] == period})
        )
        for period in unique
    }
    across = tuple(period for period, ks in strata.items() if len(ks) > 1)
    gcd_value = gcd_many(periods)
    lcm_value = lcm_many(periods)
    result = {
        "period_multiset": tuple(sorted(periods)),
        "period_census": dict(sorted(counts.items())),
        "factorizations": factors,
        "gcd": gcd_value,
        "gcd_factorization": factorization(gcd_value),
        "lcm": lcm_value,
        "lcm_factorization": factorization(lcm_value),
        "period_strata": strata,
        "periods_recurring_across_strata": across,
    }
    result["pass"] = (
        counts == Counter({2: 2, 3: 9, 288: 1, 4464: 2})
        and factors[4464] == ((2, 4), (3, 2), (31, 1))
        and factors[288] == ((2, 5), (3, 2))
        and gcd_value == 1
        and lcm_value == 8928
        and factorization(lcm_value) == ((2, 5), (3, 2), (31, 1))
        and not across
    )
    return result


RING_STATIONS = 11


def circular_gaps(positions: tuple[int, ...]) -> tuple[int, ...]:
    ordered = tuple(sorted(positions))
    return tuple(
        (ordered[(index + 1) % len(ordered)] - ordered[index]) % RING_STATIONS
        for index in range(len(ordered))
    )


def canonical_rotation(positions: tuple[int, ...]) -> tuple[int, ...]:
    return min(
        tuple(
            sorted((position + shift) % RING_STATIONS for position in positions)
        )
        for shift in range(RING_STATIONS)
    )


def test_candidates(
    rows: tuple[dict[str, object], ...],
    arithmetic: dict[str, object],
    lineage: dict[str, object],
) -> dict[str, object]:
    properties = []
    for row in rows:
        positions = tuple(int(value) for value in row["positions"])
        properties.append(
            {
                "key": row["key"],
                "period": int(row["period"]),
                "k": int(row["k"]),
                "event": int(row["event"]),
                "positions": positions,
                "contains_zero": 0 in positions,
                "position_sum_parity": sum(positions) % 2,
                "sorted_gaps": tuple(sorted(circular_gaps(positions))),
                "canonical_rotation": canonical_rotation(positions),
            }
        )

    periods_by_k = {
        k: tuple(sorted({row["period"] for row in properties if row["k"] == k}))
        for k in sorted({row["k"] for row in properties})
    }
    periods_by_event = {
        event: tuple(
            sorted({row["period"] for row in properties if row["event"] == event})
        )
        for event in sorted({row["event"] for row in properties})
    }
    by_gap: dict[tuple[int, ...], set[int]] = defaultdict(set)
    by_rotation: dict[tuple[int, tuple[int, ...], int], set[int]] = defaultdict(set)
    for row in properties:
        by_gap[row["sorted_gaps"]].add(row["period"])
        by_rotation[
            (row["k"], row["canonical_rotation"], row["event"])
        ].add(row["period"])

    strict_periods = tuple(arithmetic["period_multiset"])
    failed = (
        {
            "candidate": "nontrivial_common_period_divisor",
            "holds": int(arithmetic["gcd"]) > 1,
            "reason": "gcd(2,3)=1",
            "exact_result": arithmetic["gcd"],
            "failure_verified": arithmetic["gcd"] == 1,
        },
        {
            "candidate": "period_constant_in_every_stratum",
            "holds": all(len(values) == 1 for values in periods_by_k.values()),
            "reason": "k=2 has periods 2,3,288",
            "exact_result": periods_by_k,
            "failure_verified": periods_by_k.get(2) == (2, 3, 288),
        },
        {
            "candidate": "stratum_k_alone_determines_period",
            "holds": all(len(values) == 1 for values in periods_by_k.values()),
            "reason": "k=2 has three distinct periods",
            "exact_result": periods_by_k,
            "failure_verified": len(periods_by_k.get(2, ())) == 3,
        },
        {
            "candidate": "event_alone_determines_period",
            "holds": all(len(values) == 1 for values in periods_by_event.values()),
            "reason": "event=3 has periods 2 and 3",
            "exact_result": periods_by_event,
            "failure_verified": periods_by_event.get(3) == (2, 3),
        },
        {
            "candidate": "sorted_spacing_multiset_determines_period",
            "holds": all(len(values) == 1 for values in by_gap.values()),
            "reason": "gap multiset (5,6) has periods 2 and 3",
            "exact_result": {
                str(key): tuple(sorted(value))
                for key, value in sorted(by_gap.items())
            },
            "failure_verified": by_gap.get((5, 6)) == {2, 3},
        },
        {
            "candidate": "rotation_equivalent_key_structure_determines_period",
            "holds": all(len(values) == 1 for values in by_rotation.values()),
            "reason": "k2/event3 canonical rotation (0,5) has periods 2 and 3",
            "exact_result": {
                str(key): tuple(sorted(value))
                for key, value in sorted(by_rotation.items())
            },
            "failure_verified": by_rotation.get((2, (0, 5), 3)) == {2, 3},
        },
        {
            "candidate": "some_period_recurs_across_strata",
            "holds": bool(arithmetic["periods_recurring_across_strata"]),
            "reason": "strict k2 periods {2,3,288}; strict k4 period {4464}",
            "exact_result": arithmetic["periods_recurring_across_strata"],
            "failure_verified": (
                periods_by_k == {2: (2, 3, 288), 4: (4464,)}
                and not arithmetic["periods_recurring_across_strata"]
            ),
        },
        {
            "candidate": "5952_is_a_member_of_the_strict_14_multiset",
            "holds": 5952 in strict_periods,
            "reason": (
                "5952 belongs to four extra Cycle801 k3 keys; union count 18"
            ),
            "exact_result": strict_periods,
            "failure_verified": (
                5952 not in strict_periods
                and lineage["k3_5952_count"] == 4
                and lineage["union_distinct_key_count"] == 18
            ),
        },
    )

    event_zero_groups: dict[tuple[int, bool], set[int]] = defaultdict(set)
    parity_groups: dict[int, set[int]] = defaultdict(set)
    for row in properties:
        event_zero_groups[(row["event"], row["contains_zero"])].add(row["period"])
        parity_groups[row["position_sum_parity"]].add(row["period"])
    k2_periods = [row["period"] for row in properties if row["k"] == 2]
    k4_periods = [row["period"] for row in properties if row["k"] == 4]
    new_candidates = (
        {
            "candidate": "period_even_iff_positions_contain_zero",
            "holds": all(
                (row["period"] % 2 == 0) == row["contains_zero"]
                for row in properties
            ),
            "exact_result": tuple(
                (row["key"], row["period"], row["contains_zero"])
                for row in properties
            ),
            "scope": "strict 14-row table only",
        },
        {
            "candidate": "period_greater_than_3_iff_event_is_not_3",
            "holds": all(
                (row["period"] > 3) == (row["event"] != 3)
                for row in properties
            ),
            "exact_result": periods_by_event,
            "scope": "strict 14-row table only",
        },
        {
            "candidate": "every_observed_k2_period_is_below_every_k4_period",
            "holds": max(k2_periods) < min(k4_periods),
            "exact_result": {
                "max_k2": max(k2_periods),
                "min_k4": min(k4_periods),
            },
            "scope": "observed strict strata k=2 and k=4 only",
        },
        {
            "candidate": "event_and_zero_membership_jointly_determine_period",
            "holds": all(len(values) == 1 for values in event_zero_groups.values()),
            "exact_result": {
                str(key): tuple(sorted(value))
                for key, value in sorted(event_zero_groups.items())
            },
            "scope": "strict 14-row table only",
        },
        {
            "candidate": "position_sum_parity_determines_period",
            "holds": all(len(values) == 1 for values in parity_groups.values()),
            "exact_result": {
                str(key): tuple(sorted(value))
                for key, value in sorted(parity_groups.items())
            },
            "scope": "strict 14-row table only",
        },
    )
    return {
        "failed": failed,
        "new": new_candidates,
        "all_eight_failed_for_printed_exact_reason": all(
            not row["holds"] and row["failure_verified"] for row in failed
        ),
        "pass": (
            len(failed) == 8
            and all(not row["holds"] and row["failure_verified"] for row in failed)
            and len(new_candidates) >= 3
        ),
    }


def locate_sibling_cache() -> Path:
    direct = ROOT.parent / "lockfix-worktree" / "logs" / "runner-cache" / SIBLING_CACHE_NAME
    if direct.is_file():
        return direct
    matches = sorted(
        path
        for path in ROOT.parent.glob(
            f"*-worktree/logs/runner-cache/{SIBLING_CACHE_NAME}"
        )
        if path.is_file()
    )
    if len(matches) != 1:
        raise AssertionError(("Cycle801 sibling cache location", matches))
    return matches[0]


def verify_lineage_conflict(
    strict_rows: tuple[dict[str, object], ...],
) -> dict[str, object]:
    sibling_path = locate_sibling_cache()
    sibling_root = sibling_path.parents[2]
    relative_in_sibling = sibling_path.relative_to(sibling_root).as_posix()
    before = sibling_path.stat()
    payload = sibling_path.read_bytes()
    after = sibling_path.stat()
    text = payload.decode("utf-8")
    header = parse_cache_header(text)
    resolutions = json_line(text, "NEW_RESOLUTIONS ")
    final = json_line(text, "FINAL ")
    cycles = []
    for row in resolutions["cycles"]:
        k, positions, event = row["key"]
        cycles.append(
            {
                "key": (int(k), tuple(int(value) for value in positions), int(event)),
                "period": int(row["cycle_period"]),
                "preperiod": int(row["cycle_start_t"]),
            }
        )
    k3 = tuple(
        row for row in cycles if row["key"][0] == 3 and row["period"] == 5952
    )
    k4 = tuple(
        row for row in cycles if row["key"][0] == 4 and row["period"] == 4464
    )
    expected_k3_keys = {
        (3, (0, 2, position), 1) for position in (5, 6, 7, 8)
    }
    strict_keys = {row["key"] for row in strict_rows}
    strict_k4_keys = {row["key"] for row in strict_rows if row["k"] == 4}
    cycle801_keys = {row["key"] for row in cycles}
    ratio = Fraction(5952, 4464)
    landed_blob = git_oid(SIBLING_LANDED_COMMIT, relative_in_sibling)
    sibling_head = subprocess.run(
        ("git", "-C", str(sibling_root), "rev-parse", "HEAD"),
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()
    actual_sha = sha256(payload).hexdigest()
    actual_blob = git_blob_sha(payload)
    read_only_unchanged = (
        before.st_size == after.st_size
        and before.st_mtime_ns == after.st_mtime_ns
        and before.st_ino == after.st_ino
    )
    result = {
        "sibling_cache_citation": os.path.relpath(sibling_path, ROOT),
        "sibling_worktree_head": sibling_head,
        "landed_commit": SIBLING_LANDED_COMMIT,
        "cache_header": header,
        "actual_sha256": actual_sha,
        "expected_sha256": SIBLING_EXPECTED_SHA256,
        "actual_blob": actual_blob,
        "landed_blob": landed_blob,
        "expected_blob": SIBLING_EXPECTED_BLOB,
        "read_only_access_stat_unchanged": read_only_unchanged,
        "Cycle801_cycles": tuple(cycles),
        "k3_5952_keys": tuple(sorted(row["key"] for row in k3)),
        "k3_5952_count": len(k3),
        "k4_4464_keys": tuple(sorted(row["key"] for row in k4)),
        "Cycle801_k4_equals_strict_k4": {row["key"] for row in k4}
        == strict_k4_keys,
        "strict_distinct_key_count": len(strict_keys),
        "Cycle801_distinct_key_count": len(cycle801_keys),
        "union_distinct_key_count": len(strict_keys | cycle801_keys),
        "5952_over_4464": (ratio.numerator, ratio.denominator),
    }
    result["pass"] = (
        header["runner"]
        == "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py"
        and header["exit_code"] == 0
        and header["status"] == "ok"
        and final["pass"] is True
        and actual_sha == SIBLING_EXPECTED_SHA256
        and actual_blob == landed_blob == SIBLING_EXPECTED_BLOB
        and read_only_unchanged
        and len(k3) == 4
        and {row["key"] for row in k3} == expected_k3_keys
        and all(row["preperiod"] == 0 for row in k3)
        and len(k4) == 2
        and {row["key"] for row in k4} == strict_k4_keys
        and len(strict_keys) == 14
        and len(strict_keys | cycle801_keys) == 18
        and ratio == Fraction(4, 3)
    )
    return result


def git_head() -> str:
    return subprocess.run(
        ("git", "rev-parse", "HEAD"),
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout.strip()


def main() -> int:
    started = monotonic()
    sources = load_landed_sources()
    inventory = extract_inventory(sources["cache_payloads"])
    strict_rows = inventory["strict_rows"]

    verified = verify_rows_independently(strict_rows)
    for row in verified:
        check(
            f"ROW RE-VERIFICATION {compact(row['key'])}",
            bool(row["pass"]),
            row,
        )
    period_census = dict(
        sorted(Counter(int(row["period"]) for row in verified).items())
    )
    row_pass = (
        len(verified) == 14
        and len({row["key"] for row in verified}) == 14
        and all(row["pass"] for row in verified)
        and all(row["preperiod_zero"] for row in verified)
        and all(row["minimal_period"] for row in verified)
        and all(row["anchor_hashes_match"] for row in verified)
        and period_census == {2: 2, 3: 9, 288: 1, 4464: 2}
    )
    check(
        "ROW RE-VERIFICATION",
        row_pass,
        {
            "row_count": len(verified),
            "distinct_key_count": len({row["key"] for row in verified}),
            "period_census": period_census,
            "preperiod_census": dict(
                sorted(Counter(row["preperiod"] for row in verified).items())
            ),
            "all_recurrences": all(
                row["full_state_recurrence"] for row in verified
            ),
            "all_proper_divisor_sets_rejected": all(
                not row["proper_divisor_returns"] for row in verified
            ),
            "all_periods_minimal": all(
                row["minimal_period"] for row in verified
            ),
            "all_preperiods_zero": all(
                row["preperiod_zero"] for row in verified
            ),
            "all_anchor_hashes_match": all(
                row["anchor_hashes_match"] for row in verified
            ),
            "evolution_engine": (
                "checker-local integer Boolean X/CNOT/TOF evolution; "
                "K.run_orbit and K.A.apply_semantic unused"
            ),
            "table_sha256": digest(verified),
        },
    )

    if inventory["missed_by_strict_table"]:
        emit(
            "LOUD REFUTATION: MISSED CERTIFIED ROWS",
            inventory["missed_by_strict_table"],
        )
    check(
        "COMPLETENESS ATTACK",
        bool(inventory["pass"]),
        {
            key: value
            for key, value in inventory.items()
            if key not in {"strict_rows", "pass"}
        },
    )

    arithmetic = exact_arithmetic(verified)
    check(
        "THE ARITHMETIC",
        bool(arithmetic["pass"]),
        {key: value for key, value in arithmetic.items() if key != "pass"},
    )

    lineage = verify_lineage_conflict(strict_rows)
    candidates = test_candidates(verified, arithmetic, lineage)
    for row in candidates["failed"]:
        check(
            f"FAILED CANDIDATE {row['candidate']}",
            not row["holds"] and row["failure_verified"],
            {
                "candidate": row["candidate"],
                "holds": row["holds"],
                "reason": row["reason"],
                "exact_result": row["exact_result"],
                "finding_verbatim": (
                    f"{row['candidate']} FAILS EXACTLY: {row['reason']}"
                ),
            },
        )
    for row in candidates["new"]:
        emit(
            (
                "LOUD POSITIVE NEW REGULARITY FOUND"
                if row["holds"]
                else "NEW CANDIDATE EXACTLY DOES NOT HOLD"
            ),
            row,
        )
    check(
        "THE FAILED CANDIDATES",
        bool(candidates["pass"]),
        {
            "eight_retested": len(candidates["failed"]),
            "all_eight_failed_for_printed_exact_reason": candidates[
                "all_eight_failed_for_printed_exact_reason"
            ],
            "new_candidates_tested": len(candidates["new"]),
            "new_candidate_outcomes": candidates["new"],
            "positive_new_regularities": tuple(
                row["candidate"] for row in candidates["new"] if row["holds"]
            ),
        },
    )

    check(
        "THE LINEAGE CONFLICT",
        bool(lineage["pass"]),
        {key: value for key, value in lineage.items() if key != "pass"},
    )

    # A full second evolution is deliberately expensive: determinism is
    # certified by recomputation, not by re-hashing the first result.
    replay = verify_rows_independently(strict_rows)
    verified_sha = digest(verified)
    replay_sha = digest(replay)
    source_public = {
        key: value
        for key, value in sources.items()
        if key not in {"cache_payloads", "pass"}
    }
    sibling_citation = str(lineage["sibling_cache_citation"])
    evidence_resources = (
        AUDIT_INPUT_PATHS[0],
        AUDIT_INPUT_PATHS[1],
        AUDIT_INPUT_PATHS[2],
        (
            f"git:{CACHE_REFS[0]['commit']}:"
            f"{CACHE_REFS[0]['path']}"
        ),
        (
            f"git:{CACHE_REFS[1]['commit']}:"
            f"{CACHE_REFS[1]['path']}"
        ),
        (
            f"git:{CACHE_REFS[2]['commit']}:"
            f"{CACHE_REFS[2]['path']}"
        ),
        sibling_citation,
    )
    elapsed = monotonic() - started
    control_core_pass = (
        bool(sources["pass"])
        and PRIMARY_BLOCKLIST_PROBE["caught_before_source_load"]
        and PRIMARY_BLOCKLIST_PROBE["hits"] == (PRIMARY_MODULE,)
        and not PRIMARY_BLOCKLIST_PROBE["present_in_sys_modules"]
        and verified == replay
        and verified_sha == replay_sha
        and len(evidence_resources) == 7
        and sibling_citation not in AUDIT_INPUT_PATHS
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    control_base = {
        "worktree_head": git_head(),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS": sources["literal_audit_input_tuple"],
        "all_AUDIT_INPUT_PATHS_existing_worktree_relative": sources[
            "all_audit_inputs_existing_worktree_relative"
        ],
        "source_sha_controls": source_public,
        "Cycle818_primary_BLOCKLIST": PRIMARY_BLOCKLIST_PROBE,
        "determinism": {
            "full_second_evolution": True,
            "exact_rows_equal": verified == replay,
            "first_sha256": verified_sha,
            "replay_sha256": replay_sha,
        },
        "evidence_read_budget": {
            "maximum": 7,
            "actual": len(evidence_resources),
            "resources": evidence_resources,
            "primary_excluded_because_blocked_and_not_read": PRIMARY_PATH,
            "sibling_is_read_only_and_not_an_audit_input": sibling_citation,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }

    substantive_labels = (
        "ROW RE-VERIFICATION",
        "COMPLETENESS ATTACK",
        "THE ARITHMETIC",
        "THE FAILED CANDIDATES",
        "THE LINEAGE CONFLICT",
    )
    base_lines = tuple(OUTPUT_LINES)
    stdout_bytes = 0
    controls_pass = control_core_pass
    rendered = ""
    terminal: dict[str, object] = {}
    for _ in range(20):
        CHECKS["CONTROLS"] = controls_pass
        primary_refuted = not all(CHECKS[label] for label in substantive_labels)
        all_checks_pass = all(CHECKS.values())
        if not controls_pass:
            terminal_name = "CYCLE818_INDEPENDENT_CHECK_INVALID_CONTROL_FAILURE"
        elif primary_refuted:
            terminal_name = "CYCLE818_PRIMARY_REFUTED"
        elif all_checks_pass:
            terminal_name = "CYCLE818_INDEPENDENT_CHECK_PASS_PRIMARY_NOT_REFUTED"
        else:
            terminal_name = "CYCLE818_INDEPENDENT_CHECK_HONEST_FAIL"
        terminal = {
            "terminal": terminal_name,
            "pass": all_checks_pass,
            "primary_refuted": primary_refuted,
            "strict_row_count": len(verified),
            "strict_period_census": period_census,
            "gcd": arithmetic["gcd"],
            "lcm": arithmetic["lcm"],
            "union_with_Cycle801_distinct_key_count": lineage[
                "union_distinct_key_count"
            ],
            "runtime_seconds": round(elapsed, 6),
        }
        control_detail = {
            **control_base,
            "stdout_bytes": stdout_bytes,
            "stdout_below_limit": stdout_bytes < STDOUT_LIMIT_BYTES,
        }
        control_line = (
            f"{'PASS' if controls_pass else 'FAIL'} CONTROLS :: "
            f"{compact(control_detail)}"
        )
        rendered = (
            "\n".join((*base_lines, control_line))
            + "\nFINAL :: "
            + compact(terminal)
            + "\n"
        )
        actual_bytes = len(rendered.encode("utf-8"))
        next_controls_pass = control_core_pass and actual_bytes < STDOUT_LIMIT_BYTES
        if actual_bytes == stdout_bytes and next_controls_pass == controls_pass:
            break
        stdout_bytes = actual_bytes
        controls_pass = next_controls_pass
    else:
        raise AssertionError("stdout fixed-point accounting did not converge")

    if len(rendered.encode("utf-8")) != stdout_bytes:
        raise AssertionError(("stdout byte accounting", len(rendered), stdout_bytes))
    if monotonic() - started >= AUDIT_TIMEOUT_SEC:
        raise AssertionError(("runtime limit crossed after certificate", monotonic() - started))
    sys.stdout.write(rendered)
    return 0 if terminal["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
