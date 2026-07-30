#!/usr/bin/env python3
"""Cycle 818: exact period-structure census across the landed strata.

The named Cycle-790/791/797/814 primaries are provenance-only inputs:
they are SHA-pinned, parsed as text/AST, and blocked from import.  Dynamics
are independently reconstructed from the landed Cycle-719 controller core.

The named caches contain a material lineage discrepancy that this runner
keeps visible.  The strict 14-row inventory is the twelve Cycle-797
certifications (eleven inherited from Cycle 790 and one from Cycle 791) plus
the two Cycle-814 certifications.  Cycle 801 separately records four
k=3 cycles of period 5952 and the same two k=4 keys later certified by
Cycle 814; adding those k=3 rows would make 18 distinct keys, not 14.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
    "logs/runner-cache/frontier_cycle814_deep_silence_probe_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
import json
from math import gcd
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

REFERENCE_PRIMARIES = (
    {
        "cycle": 790,
        "commit": "935e46cac19230caf123c8810af367d7cd843469",
        "path":
            "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
        "blob": "c322bb975900b2611c3f42d19da347a1dd5bfc56",
        "sha256":
            "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    },
    {
        "cycle": 791,
        "commit": "6255426f36a48494de43ccc8bd3eb9592e584c00",
        "path":
            "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
        "blob": "f026960526f2f2a8d990a5a7856b02217ea798ce",
        "sha256":
            "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    },
    {
        "cycle": 797,
        "commit": "3cf5931aa901fb45cbb2030eb119c5a09dd32c02",
        "path":
            "scripts/frontier_cycle797_deep_horizon_continuation_2026_07_28.py",
        "blob": "5d70ba232efcbd4f8c0a2d798f735907d4207b81",
        "sha256":
            "7ece6f7c818a4dcffb3019c610ca0861998f19cfae0287e23fe98562c1a09698",
    },
    {
        "cycle": 814,
        "commit": "6cb13f88f3430a201374b5f1d8b01cf000bc6b35",
        "path":
            "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
        "blob": "19ba617ad1f6be9f8fdc637b764dc7b38cae8d7b",
        "sha256":
            "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
    },
)

REFERENCE_CACHES = (
    {
        "cycle": 790,
        "commit": "935e46cac19230caf123c8810af367d7cd843469",
        "path":
            "logs/runner-cache/frontier_cycle790_horizon_extension_2026_07_28.txt",
        "blob": "f58caebdd7a3e519b679dd0cdd098c1c80c05e34",
        "sha256":
            "2f428ebba168dc9f9e2602c43409ab7e80b24587f873d895ab54d6ebf26c8634",
    },
    {
        "cycle": 791,
        "commit": "6255426f36a48494de43ccc8bd3eb9592e584c00",
        "path":
            "logs/runner-cache/frontier_cycle791_open_keys_resolution_2026_07_28.txt",
        "blob": "460cb3ae346ef10440d5a3ef03a3c19299374edf",
        "sha256":
            "9ab66b127341c63a664ae1631527ae803358a1dd2d2dcacc4639f49aaeadfc8d",
    },
    {
        "cycle": 797,
        "commit": "3cf5931aa901fb45cbb2030eb119c5a09dd32c02",
        "path":
            "logs/runner-cache/frontier_cycle797_deep_horizon_continuation_2026_07_28.txt",
        "blob": "cb956f584b81899965d961aa356e14dd98a32d38",
        "sha256":
            "e44f1b3739b7f78680c963462a4d2e1ae3277f5b75118a1b2cc2b3ba74c8005a",
    },
    {
        "cycle": 801,
        "commit": "d42048111b5eb75f7a283db2e9039d57017a26cf",
        "path":
            "logs/runner-cache/frontier_cycle801_silent_strata_deep_scan_2026_07_28.txt",
        "blob": "b50059cfb5123439a8848cd32dc17515ae364712",
        "sha256":
            "33c10abc491b78bd2e346263d70ccf77f9b82227a5dcfa8fbe86fa62e891bf3d",
    },
    {
        "cycle": 814,
        "commit": "6cb13f88f3430a201374b5f1d8b01cf000bc6b35",
        "path":
            "logs/runner-cache/frontier_cycle814_deep_silence_probe_2026_07_28.txt",
        "blob": "a81e0f017f68a71af48329eb7d139dba21d0648b",
        "sha256":
            "521e1217d0e36440220fb6226e4872638dbe0abfda3df36986337a06acf4e89c",
    },
)

EXPECTED_AUDIT_SHA256 = {
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py":
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py":
        "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
    "logs/runner-cache/frontier_cycle814_deep_silence_probe_2026_07_28.txt":
        "521e1217d0e36440220fb6226e4872638dbe0abfda3df36986337a06acf4e89c",
}

BLOCKLISTED_MODULES = tuple(
    Path(row["path"]).stem for row in REFERENCE_PRIMARIES
)


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if any provenance-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def emit(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"{label} {compact(value)}")


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def git_payload(commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def literal_audit_paths() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    return (
        len(assignments) == 1
        and isinstance(assignments[0].value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignments[0].value.elts
        )
        and tuple(ast.literal_eval(assignments[0].value))
        == AUDIT_INPUT_PATHS
    )


def source_controls() -> dict[str, object]:
    audit_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes()
        audit_rows.append(
            {
                "path": relative,
                "exists": path.is_file(),
                "worktree_relative": (
                    not Path(relative).is_absolute()
                    and path.is_relative_to(ROOT)
                ),
                "sha256": sha256(payload).hexdigest(),
                "expected_sha256": EXPECTED_AUDIT_SHA256[relative],
                "match":
                    sha256(payload).hexdigest()
                    == EXPECTED_AUDIT_SHA256[relative],
            }
        )

    primary_rows = []
    for reference in REFERENCE_PRIMARIES:
        payload = git_payload(
            str(reference["commit"]), str(reference["path"])
        )
        tree = ast.parse(payload.decode("utf-8"))
        primary_rows.append(
            {
                **reference,
                "actual_blob": git_blob_sha(payload),
                "actual_sha256": sha256(payload).hexdigest(),
                "ast_body_nodes": len(tree.body),
                "TEXT_AST_ONLY_BLOCKLISTED":
                    Path(str(reference["path"])).stem
                    in BLOCKLISTED_MODULES,
                "match": (
                    git_blob_sha(payload) == reference["blob"]
                    and sha256(payload).hexdigest() == reference["sha256"]
                ),
            }
        )

    cache_rows = []
    cache_payloads: dict[int, str] = {}
    for reference in REFERENCE_CACHES:
        payload = git_payload(
            str(reference["commit"]), str(reference["path"])
        )
        cache_payloads[int(reference["cycle"])] = payload.decode("utf-8")
        cache_rows.append(
            {
                **reference,
                "actual_blob": git_blob_sha(payload),
                "actual_sha256": sha256(payload).hexdigest(),
                "match": (
                    git_blob_sha(payload) == reference["blob"]
                    and sha256(payload).hexdigest() == reference["sha256"]
                ),
            }
        )

    passed = (
        literal_audit_paths()
        and all(
            row["exists"] and row["worktree_relative"] and row["match"]
            for row in audit_rows
        )
        and all(row["match"] for row in primary_rows)
        and all(row["match"] for row in cache_rows)
        and not IMPORT_FIREWALL.hits
    )
    return {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_audit_paths(),
        "all_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in audit_rows
        ),
        "audit_rows": tuple(audit_rows),
        "primary_rows": tuple(primary_rows),
        "cache_rows": tuple(cache_rows),
        "cache_payloads": cache_payloads,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_runtime_modules": tuple(IMPORT_FIREWALL.hits),
        "pass": passed,
    }


def json_line(payload: str, prefix: str) -> Any:
    rows = [line for line in payload.splitlines() if line.startswith(prefix)]
    if len(rows) != 1:
        raise AssertionError(("cache JSON line", prefix, len(rows)))
    suffix = rows[0][len(prefix):].strip()
    if suffix.startswith("::"):
        suffix = suffix[2:].strip()
    return json.loads(suffix)


def cache_inventory(
    cache_payloads: dict[int, str],
) -> dict[str, object]:
    """Extract, rather than assume, the exact named-lineage inventory."""

    primary_by_cycle = {
        int(row["cycle"]): row for row in REFERENCE_PRIMARIES
    }
    cache_by_cycle = {
        int(row["cycle"]): row for row in REFERENCE_CACHES
    }

    def provenance(cycles: tuple[int, ...]) -> tuple[dict[str, object], ...]:
        return tuple(
            {
                "cycle": cycle,
                "commit": primary_by_cycle[cycle]["commit"],
                "primary_path": primary_by_cycle[cycle]["path"],
                "primary_blob": primary_by_cycle[cycle]["blob"],
                "primary_sha256": primary_by_cycle[cycle]["sha256"],
                "cache_path": cache_by_cycle[cycle]["path"],
                "cache_blob": cache_by_cycle[cycle]["blob"],
                "cache_sha256": cache_by_cycle[cycle]["sha256"],
            }
            for cycle in cycles
        )

    cycle790 = json_line(cache_payloads[790], "DATA B ")
    cycle791_row = json_line(
        cache_payloads[791], "DATA D_KEY_ROW_095 "
    )
    cycle797 = json_line(
        cache_payloads[797], "DATA B_T1024_IDENTITY "
    )["T1024"]
    cycle814 = json_line(
        cache_payloads[814],
        "PASS CERTIFICATE_B_EVENTS_OR_NULL_WITH_PROVEN_COVERAGE ",
    )
    cycle801 = json_line(cache_payloads[801], "NEW_RESOLUTIONS ")

    lower_rows = []
    for certification in cycle797["cycle_certifications"]:
        event, positions = certification["key"]
        key = (2, tuple(int(item) for item in positions), int(event))
        provenance_cycles = (
            (791, 797) if key == (2, (0, 9), 2) else (790, 797)
        )
        lower_rows.append(
            {
                "key": key,
                "k": 2,
                "positions": key[1],
                "event": key[2],
                "period": int(certification["state_period"]),
                "preperiod": int(certification["entry"]),
                "residual_period":
                    int(certification["residual_period"]),
                "source_cycles": provenance_cycles,
                "provenance": provenance(provenance_cycles),
                "source_cache_rows": (
                    (
                        "Cycle791 DATA D_KEY_ROW_095; "
                        "Cycle797 DATA B_T1024_IDENTITY"
                    )
                    if provenance_cycles[0] == 791
                    else (
                        "Cycle790 DATA B periodic_keys/table; "
                        "Cycle797 DATA B_T1024_IDENTITY"
                    )
                ),
            }
        )

    upper_rows = []
    for certification in cycle814["coverage_accounting"][
        "certified_cycle_periods"
    ]:
        k, positions, event = certification["key"]
        key = (
            int(k),
            tuple(int(item) for item in positions),
            int(event),
        )
        upper_rows.append(
            {
                "key": key,
                "k": key[0],
                "positions": key[1],
                "event": key[2],
                "period": int(certification["period"]),
                "preperiod": 0,
                "residual_period": None,
                "source_cycles": (814,),
                "provenance": provenance((814,)),
                "source_cache_rows":
                    "Cycle814 CERTIFICATE_B coverage_accounting",
            }
        )

    strict_rows = tuple(
        sorted(lower_rows + upper_rows, key=lambda row: row["key"])
    )

    cycle790_keys = {
        (2, tuple(int(item) for item in positions), int(event))
        for event, positions, _period in cycle790["periodic_keys"]
    }
    extracted_790_keys = {
        row["key"] for row in lower_rows if row["source_cycles"][0] == 790
    }
    cycle791_key = (
        2,
        tuple(int(item) for item in cycle791_row["positions"]),
        int(cycle791_row["event"]),
    )

    cycle801_cycles = tuple(
        {
            "key": (
                int(row["key"][0]),
                tuple(int(item) for item in row["key"][1]),
                int(row["key"][2]),
            ),
            "period": int(row["cycle_period"]),
            "preperiod": int(row["cycle_start_t"]),
        }
        for row in cycle801["cycles"]
    )
    strict_keys = {row["key"] for row in strict_rows}
    cycle801_new_keys = {
        row["key"] for row in cycle801_cycles
    } - strict_keys
    cycle801_duplicate_keys = {
        row["key"] for row in cycle801_cycles
    } & strict_keys
    k3_5952_rows = tuple(
        row
        for row in cycle801_cycles
        if row["key"][0] == 3 and row["period"] == 5952
    )
    k4_4464_rows = tuple(
        row
        for row in cycle801_cycles
        if row["key"][0] == 4 and row["period"] == 4464
    )
    lineage_discrepancy = {
        "strict_named_790_791_797_814_distinct_keys": len(strict_rows),
        "strict_period_census":
            dict(sorted(Counter(row["period"] for row in strict_rows).items())),
        "strict_contains_5952":
            any(row["period"] == 5952 for row in strict_rows),
        "Cycle801_cache_period_5952_k3_rows": k3_5952_rows,
        "Cycle801_cache_period_4464_k4_rows": k4_4464_rows,
        "Cycle801_k4_keys_duplicate_Cycle814":
            {row["key"] for row in k4_4464_rows}
            == {row["key"] for row in upper_rows},
        "Cycle801_extra_distinct_keys": tuple(sorted(cycle801_new_keys)),
        "Cycle801_duplicate_distinct_keys":
            tuple(sorted(cycle801_duplicate_keys)),
        "union_distinct_key_count":
            len(strict_keys | {row["key"] for row in cycle801_cycles}),
        "conclusion": (
            "THE_STRICT_14_ROW_TABLE_AND_A_5952_MEMBER_CANNOT_BOTH_BE "
            "EXTRACTED_FROM_THE_NAMED_790_791_797_814_INVENTORY; "
            "ADDING_THE_FOUR_CYCLE801_K3_KEYS MAKES_18_DISTINCT_KEYS"
        ),
    }
    extraction_pass = (
        len(strict_rows) == 14
        and len(lower_rows) == 12
        and len(upper_rows) == 2
        and cycle790_keys == extracted_790_keys
        and cycle791_key == (2, (0, 9), 2)
        and cycle791_row["state_period"] == 288
        and cycle791_row["residual_period"] == 6
        and len(k3_5952_rows) == 4
        and len(k4_4464_rows) == 2
        and lineage_discrepancy["Cycle801_k4_keys_duplicate_Cycle814"]
        and lineage_discrepancy["union_distinct_key_count"] == 18
    )
    return {
        "strict_rows": strict_rows,
        "cycle790_keys": tuple(sorted(cycle790_keys)),
        "cycle791_row": cycle791_row,
        "cycle801_cycles": cycle801_cycles,
        "lineage_discrepancy": lineage_discrepancy,
        "pass": extraction_pass,
    }


def build_fixtures(
    program: tuple[object, ...],
) -> dict[int, tuple[tuple[int, int], tuple[int, ...]]]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    rows = {}
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows[event] = (direction, before)
        state = K.A.apply_semantic(
            before, K.M.global_allocator_word(FIXTURE_BANKS)
        )
    return rows


def synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Independent exact Cycle-736 synchronous composition."""

    positions = tuple(token_positions)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station in range(len(program)):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    compiled = []
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        expected_arity = {"X": 1, "CNOT": 2, "TOF": 3}
        if kind not in expected_arity or len(wires) != expected_arity[kind]:
            raise AssertionError(("unsupported exact gate", kind, wires))
        if len(set(wires)) != len(wires):
            raise AssertionError(("non-distinct gate wires", kind, wires))
        if kind == "X":
            compiled.append((1, wires[0], -1, -1))
        elif kind == "CNOT":
            compiled.append((2, wires[0], wires[1], -1))
        else:
            compiled.append((3, wires[0], wires[1], wires[2]))
    return tuple(compiled)


def apply_compiled_word(
    state: list[int],
    compiled: tuple[tuple[int, int, int, int], ...],
) -> None:
    for kind, first, second, third in compiled:
        if kind == 1:
            state[first] ^= 1
        elif kind == 2:
            state[second] ^= state[first]
        else:
            state[third] ^= state[first] & state[second]


def tuple_state_to_int(state: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(state))


def state_sha256(state: Iterable[int]) -> str:
    return sha256(str(tuple_state_to_int(state)).encode("ascii")).hexdigest()


def divisors(number: int) -> tuple[int, ...]:
    small = []
    large = []
    candidate = 1
    while candidate * candidate <= number:
        if number % candidate == 0:
            small.append(candidate)
            if candidate * candidate != number:
                large.append(number // candidate)
        candidate += 1
    return tuple(small + list(reversed(large)))


def verify_cycle_row(
    row: dict[str, object],
    program: tuple[object, ...],
    fixtures: dict[int, tuple[tuple[int, int], tuple[int, ...]]],
) -> dict[str, object]:
    positions = tuple(row["positions"])
    event = int(row["event"])
    period = int(row["period"])
    direction, before = fixtures[event]
    word = synchronous_word(program, positions)
    compiled = compile_word(word)
    initial, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    expected_initial = K.A.apply_semantic(before, word)
    expected_rail = tuple(
        int(station in positions) for station in range(len(program))
    )
    state = [int(bit) for bit in initial]
    anchor_state = tuple(state)
    anchor_sha256 = state_sha256(anchor_state)
    earlier_returns = []
    proper_divisor_returns = []
    proper_divisor_set = frozenset(divisors(period)[:-1])
    for moment in range(1, period + 1):
        apply_compiled_word(state, compiled)
        if state == list(anchor_state):
            if moment < period:
                earlier_returns.append(moment)
            if moment in proper_divisor_set:
                proper_divisor_returns.append(moment)
    closure_state = tuple(state)
    closure_sha256 = state_sha256(closure_state)
    minimal = (
        closure_state == anchor_state
        and not earlier_returns
        and not proper_divisor_returns
    )
    result = {
        **row,
        "direction": direction,
        "word_gate_count": len(compiled),
        "anchor_t": int(row["preperiod"]),
        "closure_t": int(row["preperiod"]) + period,
        "anchor_state_sha256": anchor_sha256,
        "anchor_plus_period_state_sha256": closure_sha256,
        "full_state_recurrence": closure_state == anchor_state,
        "earlier_return_moments": tuple(earlier_returns),
        "proper_divisors": tuple(sorted(proper_divisor_set)),
        "proper_divisor_returns": tuple(proper_divisor_returns),
        "proper_divisors_rejected":
            len(proper_divisor_set) - len(proper_divisor_returns),
        "minimal_period": minimal,
        "initial_composition_exact": initial == expected_initial,
        "initial_rails_exact":
            rail_a == expected_rail and not any(rail_b),
    }
    result["pass"] = (
        result["preperiod"] == 0
        and result["full_state_recurrence"]
        and result["minimal_period"]
        and result["anchor_state_sha256"]
        == result["anchor_plus_period_state_sha256"]
        and result["initial_composition_exact"]
        and result["initial_rails_exact"]
    )
    return result


def verify_inventory(
    rows: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    program = K.interleaved_program(FIXTURE_BANKS)
    fixtures = build_fixtures(program)
    return tuple(
        verify_cycle_row(row, program, fixtures) for row in rows
    )


def factorization(number: int) -> tuple[tuple[int, int], ...]:
    remaining = number
    rows = []
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            rows.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        rows.append((remaining, 1))
    return tuple(rows)


def factor_product(factors: tuple[tuple[int, int], ...]) -> int:
    product = 1
    for prime, exponent in factors:
        product *= prime ** exponent
    return product


def lcm_pair(left: int, right: int) -> int:
    return left // gcd(left, right) * right


def gcd_many(values: Iterable[int]) -> int:
    result = 0
    for value in values:
        result = gcd(result, int(value))
    return result


def lcm_many(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result = lcm_pair(result, int(value))
    return result


def structure_arithmetic(
    rows: tuple[dict[str, object], ...],
) -> dict[str, object]:
    periods = tuple(int(row["period"]) for row in rows)
    unique_periods = tuple(sorted(set(periods)))
    counts = Counter(periods)
    factors = tuple(
        {
            "period": period,
            "multiplicity": counts[period],
            "factorization": factorization(period),
        }
        for period in unique_periods
    )
    divisibility_relations = tuple(
        (left, right)
        for left in unique_periods
        for right in unique_periods
        if left < right and right % left == 0
    )
    hasse_edges = tuple(
        (left, right)
        for left, right in divisibility_relations
        if not any(
            left < middle < right
            and middle % left == 0
            and right % middle == 0
            for middle in unique_periods
        )
    )
    period_strata = {
        period: tuple(
            sorted(
                {
                    int(row["k"])
                    for row in rows
                    if int(row["period"]) == period
                }
            )
        )
        for period in unique_periods
    }
    across_strata = tuple(
        period
        for period, strata in period_strata.items()
        if len(strata) > 1
    )
    strict_ratios = tuple(
        {
            "numerator_period": numerator,
            "denominator_period": denominator,
            "reduced_ratio": (
                Fraction(numerator, denominator).numerator,
                Fraction(numerator, denominator).denominator,
            ),
        }
        for numerator in unique_periods
        for denominator in unique_periods
        if numerator > denominator
    )
    strict_gcd = gcd_many(periods)
    strict_lcm = lcm_many(periods)
    diagnostic_values = (6, 288, 4464, 5952)
    diagnostic_factors = tuple(
        {
            "value": value,
            "factorization": factorization(value),
            "scope": (
                "STRICT_STATE_PERIOD"
                if value in unique_periods
                else (
                    "CYCLE791_RESIDUAL_PERIOD_NOT_STATE_PERIOD"
                    if value == 6
                    else "CYCLE801_EXTERNAL_TO_STRICT_14"
                )
            ),
        }
        for value in diagnostic_values
    )
    late_clock_values = (288, 4464, 5952)
    external_ratio = Fraction(5952, 4464)
    return {
        "period_multiset": tuple(sorted(periods)),
        "period_census": dict(sorted(counts.items())),
        "unique_periods": unique_periods,
        "factor_table": factors,
        "divisibility_relations": divisibility_relations,
        "hasse_edges": hasse_edges,
        "gcd": strict_gcd,
        "gcd_factorization": factorization(strict_gcd),
        "lcm": strict_lcm,
        "lcm_factorization": factorization(strict_lcm),
        "period_strata": period_strata,
        "periods_recurring_across_strata": across_strata,
        "strict_ratio_table": strict_ratios,
        "diagnostic_factor_table": diagnostic_factors,
        "Cycle801_external_ratio_5952_over_4464": (
            external_ratio.numerator, external_ratio.denominator
        ),
        "late_clock_subset_scope":
            "NOT_THE_STRICT_14_MULTISET; INCLUDES_EXTERNAL_CYCLE801_5952",
        "late_clock_subset": late_clock_values,
        "late_clock_subset_gcd": gcd_many(late_clock_values),
        "late_clock_subset_lcm": lcm_many(late_clock_values),
        "pass": (
            len(periods) == 14
            and counts == Counter({3: 9, 2: 2, 4464: 2, 288: 1})
            and all(
                factor_product(row["factorization"]) == row["period"]
                for row in factors
            )
            and factorization(4464) == ((2, 4), (3, 2), (31, 1))
            and factorization(5952) == ((2, 6), (3, 1), (31, 1))
            and factorization(288) == ((2, 5), (3, 2))
            and strict_gcd == 1
            and strict_lcm == 8928
            and divisibility_relations
            == ((2, 288), (2, 4464), (3, 288), (3, 4464))
            and hasse_edges == divisibility_relations
            and not across_strata
            and external_ratio == Fraction(4, 3)
            and gcd_many(late_clock_values) == 48
            and lcm_many(late_clock_values) == 17856
        ),
    }


def circular_gaps(
    positions: tuple[int, ...],
) -> tuple[int, ...]:
    ordered = tuple(sorted(positions))
    return tuple(
        (
            ordered[(index + 1) % len(ordered)] - ordered[index]
        ) % RING_STATIONS
        for index in range(len(ordered))
    )


def canonical_rotation(
    positions: tuple[int, ...],
) -> tuple[int, ...]:
    return min(
        tuple(
            sorted(
                (position + shift) % RING_STATIONS
                for position in positions
            )
        )
        for shift in range(RING_STATIONS)
    )


def candidate_regularities(
    rows: tuple[dict[str, object], ...],
    structure: dict[str, object],
) -> dict[str, object]:
    properties = tuple(
        {
            "key": row["key"],
            "period": int(row["period"]),
            "k": int(row["k"]),
            "tuple_size": len(tuple(row["positions"])),
            "event": int(row["event"]),
            "ordered_circular_gaps": circular_gaps(
                tuple(row["positions"])
            ),
            "sorted_circular_gaps": tuple(
                sorted(circular_gaps(tuple(row["positions"])))
            ),
            "canonical_rotation":
                canonical_rotation(tuple(row["positions"])),
            "pairwise_separated":
                min(circular_gaps(tuple(row["positions"]))) >= 2,
            "contains_zero": 0 in tuple(row["positions"]),
        }
        for row in rows
    )
    periods_by_k = {
        k: tuple(
            sorted(
                {
                    row["period"]
                    for row in properties
                    if row["k"] == k
                }
            )
        )
        for k in sorted({row["k"] for row in properties})
    }
    periods_by_event = {
        event: tuple(
            sorted(
                {
                    row["period"]
                    for row in properties
                    if row["event"] == event
                }
            )
        )
        for event in sorted({row["event"] for row in properties})
    }
    periods_by_sorted_gaps: dict[
        tuple[int, ...], set[int]
    ] = defaultdict(set)
    periods_by_rotation: dict[
        tuple[int, tuple[int, ...], int], set[int]
    ] = defaultdict(set)
    for row in properties:
        periods_by_sorted_gaps[row["sorted_circular_gaps"]].add(
            row["period"]
        )
        periods_by_rotation[
            (row["k"], row["canonical_rotation"], row["event"])
        ].add(row["period"])

    short_orbit_rows = tuple(
        row
        for row in properties
        if row["k"] == 2
        and row["event"] == 3
        and row["sorted_circular_gaps"] == (5, 6)
    )
    k4_rows = tuple(row for row in properties if row["k"] == 4)
    exact_regularities = (
        {
            "candidate": "k_equals_family_tuple_size",
            "holds": all(row["k"] == row["tuple_size"] for row in properties),
            "evidence": f"{len(properties)}/{len(properties)} rows",
        },
        {
            "candidate": "all_certified_positions_pairwise_separated",
            "holds": all(row["pairwise_separated"] for row in properties),
            "evidence": "every circular gap is >=2",
        },
        {
            "candidate": "all_preperiods_zero",
            "holds": all(int(row["preperiod"]) == 0 for row in rows),
            "evidence": dict(
                sorted(Counter(row["preperiod"] for row in rows).items())
            ),
        },
        {
            "candidate": "k4_period_constant_4464",
            "holds": (
                len(k4_rows) == 2
                and {row["period"] for row in k4_rows} == {4464}
            ),
            "evidence": tuple(
                (row["key"], row["sorted_circular_gaps"])
                for row in k4_rows
            ),
        },
        {
            "candidate": (
                "within_k2_event3_gap_5_6_period2_iff_contains_zero"
            ),
            "holds": (
                len(short_orbit_rows) == 11
                and all(
                    (row["period"] == 2) == row["contains_zero"]
                    for row in short_orbit_rows
                )
            ),
            "evidence": tuple(
                (row["key"], row["period"], row["contains_zero"])
                for row in short_orbit_rows
            ),
        },
        {
            "candidate": "period4464_iff_k4_event1_in_strict_table",
            "holds": all(
                (row["period"] == 4464)
                == (row["k"] == 4 and row["event"] == 1)
                for row in properties
            ),
            "evidence": "exact biconditional over 14 rows",
        },
    )
    tested_failures = (
        {
            "candidate": "nontrivial_common_period_divisor",
            "holds": int(structure["gcd"]) > 1,
            "counterexample": "gcd(2,3)=1",
            "exact_result": structure["gcd"],
        },
        {
            "candidate": "period_constant_in_every_stratum",
            "holds": all(len(values) == 1 for values in periods_by_k.values()),
            "counterexample": "k=2 has periods 2,3,288",
            "exact_result": periods_by_k,
        },
        {
            "candidate": "stratum_k_alone_determines_period",
            "holds": all(len(values) == 1 for values in periods_by_k.values()),
            "counterexample": "k=2 has three distinct periods",
            "exact_result": periods_by_k,
        },
        {
            "candidate": "event_alone_determines_period",
            "holds":
                all(len(values) == 1 for values in periods_by_event.values()),
            "counterexample": "event=3 has periods 2 and 3",
            "exact_result": periods_by_event,
        },
        {
            "candidate": "sorted_spacing_multiset_determines_period",
            "holds": all(
                len(values) == 1
                for values in periods_by_sorted_gaps.values()
            ),
            "counterexample":
                "gap multiset (5,6) has periods 2 and 3",
            "exact_result": {
                str(key): tuple(sorted(value))
                for key, value in sorted(periods_by_sorted_gaps.items())
            },
        },
        {
            "candidate":
                "rotation_equivalent_key_structure_determines_period",
            "holds": all(
                len(values) == 1
                for values in periods_by_rotation.values()
            ),
            "counterexample":
                "k2/event3 canonical rotation (0,5) has periods 2 and 3",
            "exact_result": {
                str(key): tuple(sorted(value))
                for key, value in sorted(periods_by_rotation.items())
            },
        },
        {
            "candidate": "some_period_recurs_across_strata",
            "holds":
                bool(structure["periods_recurring_across_strata"]),
            "counterexample":
                "strict k2 periods {2,3,288}; strict k4 period {4464}",
            "exact_result":
                structure["periods_recurring_across_strata"],
        },
        {
            "candidate": "5952_is_a_member_of_the_strict_14_multiset",
            "holds": 5952 in structure["period_multiset"],
            "counterexample":
                "5952 belongs to four extra Cycle801 k3 keys; union count 18",
            "exact_result": structure["period_multiset"],
        },
    )
    return {
        "key_property_table": properties,
        "periods_by_stratum": periods_by_k,
        "periods_by_event": periods_by_event,
        "exact_regularities": exact_regularities,
        "tested_and_failed_candidates": tested_failures,
        "pass": (
            all(row["holds"] for row in exact_regularities)
            and all(not row["holds"] for row in tested_failures)
        ),
    }


def main() -> int:
    started = monotonic()
    source = source_controls()
    inventory = cache_inventory(source["cache_payloads"])
    verified_rows = verify_inventory(inventory["strict_rows"])
    for row in verified_rows:
        emit("PERIOD_TABLE_ROW", row)
    emit("LINEAGE_DATA_CONFLICT", inventory["lineage_discrepancy"])
    unavailable_rows = ()
    certificate_a = (
        source["pass"]
        and inventory["pass"]
        and len(verified_rows) == 14
        and len({row["key"] for row in verified_rows}) == 14
        and all(row["pass"] for row in verified_rows)
        and not unavailable_rows
    )
    check(
        "CERTIFICATE_A_COMPLETE_PERIOD_TABLE_DIRECT_RECURRENCE",
        certificate_a,
        {
            "status": "COMPLETE_STRICT_14_WITH_EXPLICIT_LINEAGE_CONFLICT",
            "row_count": len(verified_rows),
            "k_census":
                dict(sorted(Counter(row["k"] for row in verified_rows).items())),
            "period_census":
                dict(
                    sorted(
                        Counter(
                            row["period"] for row in verified_rows
                        ).items()
                    )
                ),
            "preperiod_census":
                dict(
                    sorted(
                        Counter(
                            row["preperiod"] for row in verified_rows
                        ).items()
                    )
                ),
            "all_direct_full_state_recurrences":
                all(row["full_state_recurrence"] for row in verified_rows),
            "all_minimal":
                all(row["minimal_period"] for row in verified_rows),
            "all_anchor_hashes_equal":
                all(
                    row["anchor_state_sha256"]
                    == row["anchor_plus_period_state_sha256"]
                    for row in verified_rows
                ),
            "DATA_UNAVAILABLE_HERE": unavailable_rows,
            "table_sha256": digest(verified_rows),
            "lineage_discrepancy": inventory["lineage_discrepancy"],
        },
    )

    structure = structure_arithmetic(verified_rows)
    for factor_row in structure["factor_table"]:
        emit("FACTOR_TABLE_ROW", factor_row)
    for factor_row in structure["diagnostic_factor_table"]:
        emit("DIAGNOSTIC_FACTOR_TABLE_ROW", factor_row)
    emit(
        "DIVISIBILITY_LATTICE",
        {
            "nodes": structure["unique_periods"],
            "relations": structure["divisibility_relations"],
            "hasse_edges": structure["hasse_edges"],
        },
    )
    emit("STRICT_RATIO_TABLE", structure["strict_ratio_table"])
    emit(
        "EXTERNAL_RATIO_CONTROL",
        {
            "scope":
                "CYCLE801_5952_IS_NOT_A_MEMBER_OF_THE_STRICT_14_TABLE",
            "5952_over_4464":
                structure["Cycle801_external_ratio_5952_over_4464"],
        },
    )
    check(
        "CERTIFICATE_B_EXACT_PERIOD_ARITHMETIC",
        bool(structure["pass"]),
        {
            key: value
            for key, value in structure.items()
            if key != "pass"
        },
    )

    regularities = candidate_regularities(verified_rows, structure)
    for row in regularities["key_property_table"]:
        emit("KEY_STRUCTURE_ROW", row)
    for row in regularities["exact_regularities"]:
        emit("EXACT_REGULARITY_FOUND", row)
    for row in regularities["tested_and_failed_candidates"]:
        emit("TESTED_CANDIDATE_FAILED", row)
    check(
        "CERTIFICATE_C_EXACT_CANDIDATE_REGULARITIES",
        bool(regularities["pass"]),
        {
            "exact_regularities": regularities["exact_regularities"],
            "tested_and_failed_candidates":
                regularities["tested_and_failed_candidates"],
            "periods_by_stratum": regularities["periods_by_stratum"],
            "periods_by_event": regularities["periods_by_event"],
            "no_fitting_used": True,
            "only_exact_equality_divisibility_and_tuple_facts": True,
        },
    )

    identity_keys = {
        (4, (0, 2, 4, 7), 1),
        (4, (0, 2, 4, 8), 1),
        (2, (0, 9), 2),
    }
    identity_source_rows = tuple(
        row
        for row in inventory["strict_rows"]
        if row["key"] in identity_keys
    )
    identity_rows = verify_inventory(identity_source_rows)
    for row in identity_rows:
        emit("IDENTITY_CONTROL_ROW", row)
    identity_periods = {
        row["key"]: row["period"] for row in identity_rows
    }
    certificate_d = (
        len(identity_rows) == 3
        and all(row["pass"] and row["minimal_period"] for row in identity_rows)
        and identity_periods[(4, (0, 2, 4, 7), 1)] == 4464
        and identity_periods[(4, (0, 2, 4, 8), 1)] == 4464
        and identity_periods[(2, (0, 9), 2)] == 288
    )
    check(
        "CERTIFICATE_D_IDENTITY_CONTROLS",
        certificate_d,
        {
            "Cycle814_controls": tuple(
                {
                    "key": row["key"],
                    "period": row["period"],
                    "minimal": row["minimal_period"],
                    "proper_divisors_rejected":
                        row["proper_divisors_rejected"],
                    "anchor_state_sha256":
                        row["anchor_state_sha256"],
                    "anchor_plus_period_state_sha256":
                        row["anchor_plus_period_state_sha256"],
                }
                for row in identity_rows
                if row["k"] == 4
            ),
            "k_le_3_control": next(
                {
                    "key": row["key"],
                    "period": row["period"],
                    "residual_period": row["residual_period"],
                    "minimal": row["minimal_period"],
                    "anchor_state_sha256":
                        row["anchor_state_sha256"],
                    "anchor_plus_period_state_sha256":
                        row["anchor_plus_period_state_sha256"],
                }
                for row in identity_rows
                if row["k"] <= 3
            ),
        },
    )

    replay_rows = verify_inventory(inventory["strict_rows"])
    primary_sha256 = digest(verified_rows)
    replay_sha256 = digest(replay_rows)
    source_public = {
        key: value
        for key, value in source.items()
        if key != "cache_payloads"
    }
    elapsed = monotonic() - started
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(compact(source_public).encode("utf-8"))
        + 16 * 1024
    )
    certificate_e = (
        source["pass"]
        and not IMPORT_FIREWALL.hits
        and verified_rows == replay_rows
        and primary_sha256 == replay_sha256
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_SHA_BLOCKLIST_DETERMINISM_PATHS_RUNTIME_STDOUT",
        certificate_e,
        {
            "source_controls": source_public,
            "determinism": {
                "exact_row_match": verified_rows == replay_rows,
                "primary_table_sha256": primary_sha256,
                "replay_table_sha256": replay_sha256,
                "pass":
                    verified_rows == replay_rows
                    and primary_sha256 == replay_sha256,
            },
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    passed = all(CHECKS.values())
    terminal = {
        "terminal": (
            "CYCLE818_PERIOD_STRUCTURE_CENSUS_PASS"
            if passed
            else "CYCLE818_PERIOD_STRUCTURE_CENSUS_HONEST_FAIL"
        ),
        "pass": passed,
        "strict_row_count": len(verified_rows),
        "strict_period_census": structure["period_census"],
        "strict_gcd": structure["gcd"],
        "strict_lcm": structure["lcm"],
        "periods_recurring_across_strata":
            structure["periods_recurring_across_strata"],
        "lineage_conflict":
            inventory["lineage_discrepancy"]["conclusion"],
        "table_sha256": primary_sha256,
        "runtime_seconds": round(monotonic() - started, 6),
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
