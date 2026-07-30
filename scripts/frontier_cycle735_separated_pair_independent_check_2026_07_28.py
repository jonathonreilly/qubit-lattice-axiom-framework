#!/usr/bin/env python3
"""Independent checker for the narrowed Cycle-735 finite theorem.

The changed primary is executed in a subprocess and its report contract is
checked.  The finite template calculation is then derived with Python sets.
For the bare Cycle-719 dynamics, this checker imports only the inherited gate
lists and fixture constructors and evaluates X/CNOT/Toffoli gates with a fresh
interpreter.  It never calls Cycle 719's semantic evaluator, controller-step,
or orbit helpers.
"""
from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import subprocess
import sys
from time import perf_counter
from typing import Any

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
PRIMARY_PATH = (
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

ROOT = Path(__file__).resolve().parents[1]
RING_STATIONS = 11
TEMPLATE_DISTANCES = (2, 3, 4, 5)
RING_MASK = (1 << RING_STATIONS) - 1
STDOUT_LIMIT_BYTES = 150 * 1024


def rotate_to_next_source(value: int) -> int:
    return (value >> 1) | ((value & 1) << (RING_STATIONS - 1))


def static_charge_syndrome(a: set[int], refs: set[int]) -> int:
    a_mask = sum(1 << site for site in a)
    refs_mask = sum(1 << site for site in refs)
    return (a_mask ^ refs_mask ^ rotate_to_next_source(refs_mask)) & RING_MASK


def run_primary() -> dict[str, Any]:
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(ROOT / "scripts")
    completed = subprocess.run(
        [sys.executable, PRIMARY_PATH],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    report: dict[str, Any] | None = None
    for line in reversed(completed.stdout.splitlines()):
        if line.startswith("{"):
            report = json.loads(line)
            break
    conditions = {
        "exit_zero": completed.returncode == 0,
        "report_present": isinstance(report, dict),
        "report_pass": bool(report and report.get("pass")),
        "seven_checks": bool(
            report
            and report.get("checks_passed") == 7
            and report.get("checks_failed") == 0
        ),
        "template_census": bool(
            report
            and report["joint_template"]["cases"] == 44
            and report["joint_template"][
                "translation_covariance_identities"
            ]
            == 484
            and report["joint_template"]["deletion_cases"] == 242
        ),
        "transport_census": bool(
            report
            and report["bare_Cycle719_nonadjacent_transport"]["cases"] == 44
            and report["bare_Cycle719_nonadjacent_transport"]["steps"] == 484
            and report["bare_Cycle719_nonadjacent_transport"][
                "station_checks"
            ]
            == 5324
            and report["bare_Cycle719_nonadjacent_transport"][
                "occupied_station_checks"
            ]
            == 968
        ),
        "claim_boundary": bool(
            report
            and report["claim_boundary"]["full_Cycle731_guarded_controller"]
            == "outside this claim"
            and report["guard_specific_adjacent_recount"][
                "used_as_controller_domain_boundary"
            ]
            is False
        ),
    }
    return {
        "pass": all(conditions.values()),
        "conditions": conditions,
        "returncode": completed.returncode,
        "stderr_tail": completed.stderr[-2000:],
        "primary_terminal": report.get("terminal") if report else None,
        "primary_report_sha256":
            report.get("report_sha256") if report else None,
    }


def template_set_recount() -> dict[str, Any]:
    failures: list[tuple[Any, ...]] = []
    pairs: set[tuple[int, int]] = set()
    cases = covariance = deletions = 0
    a_deletions = reference_deletions = 0

    for distance in TEMPLATE_DISTANCES:
        for position in range(RING_STATIONS):
            cases += 1
            a = {
                position,
                (position + distance) % RING_STATIONS,
            }
            refs = {
                (position + edge) % RING_STATIONS
                for edge in range(1, distance + 1)
            }
            pairs.add(tuple(sorted(a)))
            if (
                len(a) != 2
                or len(refs) != distance
                or static_charge_syndrome(a, refs) != 0
            ):
                failures.append(("template", position, distance))

            for shift in range(RING_STATIONS):
                covariance += 1
                shifted_a = {
                    (site + shift) % RING_STATIONS for site in a
                }
                shifted_refs = {
                    (site + shift) % RING_STATIONS for site in refs
                }
                target_a = {
                    (position + shift) % RING_STATIONS,
                    (position + distance + shift) % RING_STATIONS,
                }
                target_refs = {
                    (position + shift + edge) % RING_STATIONS
                    for edge in range(1, distance + 1)
                }
                if shifted_a != target_a or shifted_refs != target_refs:
                    failures.append(("covariance", position, distance, shift))

            entries = tuple(("A", site) for site in sorted(a)) + tuple(
                ("reference", site) for site in sorted(refs)
            )
            for role, site in entries:
                deletions += 1
                a_deletions += role == "A"
                reference_deletions += role == "reference"
                damaged_a = set(a)
                damaged_refs = set(refs)
                if role == "A":
                    damaged_a.remove(site)
                else:
                    damaged_refs.remove(site)
                relation_still_holds = (
                    len(damaged_a) == 2
                    and static_charge_syndrome(damaged_a, damaged_refs) == 0
                )
                if relation_still_holds:
                    failures.append(
                        ("deletion", position, distance, role, site)
                    )

    return {
        "pass": (
            cases == 44
            and len(pairs) == 44
            and covariance == 484
            and deletions == 242
            and a_deletions == 88
            and reference_deletions == 154
            and not failures
        ),
        "cases": cases,
        "unique_unordered_pairs": len(pairs),
        "translation_identities": covariance,
        "deletion_cases": deletions,
        "A_deletions": a_deletions,
        "reference_deletions": reference_deletions,
        "failures": failures[:20],
        "implementation": "set-valued clean-room enumerator",
    }


def apply_gates(
    bits: tuple[int, ...], word: tuple[object, ...]
) -> tuple[int, ...]:
    output = list(bits)
    for gate in word:
        if gate.kind == "X":
            output[gate.wires[0]] ^= 1
        elif gate.kind == "CNOT":
            output[gate.wires[1]] ^= output[gate.wires[0]]
        elif gate.kind == "TOF":
            output[gate.wires[2]] ^= (
                output[gate.wires[0]] & output[gate.wires[1]]
            )
        else:
            raise ValueError((gate.kind, gate.wires))
    return tuple(output)


def gate_interpreter_recount() -> dict[str, Any]:
    program = K.interleaved_program(2)
    banks, links = K.B.chain_genesis(2)
    genesis = K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    allocator = K.M.global_allocator_word(2)
    twice = apply_gates(apply_gates(genesis, allocator), allocator)
    failures: list[tuple[int, int, str]] = []
    nonadjacent_cases = adjacent_cases = 0
    steps = station_checks = occupied_checks = 0
    adjacent_double_allocator_matches = 0

    for distance in (1,) + TEMPLATE_DISTANCES:
        for position in range(RING_STATIONS):
            live = {
                position,
                (position + distance) % RING_STATIONS,
            }
            initial_live = set(live)
            data = genesis
            if distance == 1:
                adjacent_cases += 1
            else:
                nonadjacent_cases += 1
            for step in range(RING_STATIONS):
                if distance != 1:
                    steps += 1
                    station_checks += RING_STATIONS
                    occupied_checks += len(live)
                expected_live = {
                    (position + step) % RING_STATIONS,
                    (position + distance + step) % RING_STATIONS,
                }
                if live != expected_live:
                    failures.append((position, distance, "live_positions"))
                for station in range(RING_STATIONS):
                    if station in live:
                        data = apply_gates(
                            data, K.mapped_macro(program[station])
                        )
                live = {
                    (site + 1) % RING_STATIONS for site in live
                }
            if live != initial_live:
                failures.append((position, distance, "orbit_closure"))
            if distance == 1:
                adjacent_double_allocator_matches += data == twice
            elif data != twice:
                failures.append((position, distance, "double_allocator"))

            restored = data
            reverse_live = set(live)
            for _step in range(RING_STATIONS):
                reverse_live = {
                    (site - 1) % RING_STATIONS for site in reverse_live
                }
                for station in reversed(range(RING_STATIONS)):
                    if station in reverse_live:
                        restored = apply_gates(
                            restored,
                            tuple(reversed(K.mapped_macro(program[station]))),
                        )
            if restored != genesis or reverse_live != initial_live:
                failures.append((position, distance, "literal_reverse"))

    return {
        "pass": (
            nonadjacent_cases == 44
            and adjacent_cases == 11
            and steps == 484
            and station_checks == 5324
            and occupied_checks == 968
            and adjacent_double_allocator_matches == 0
            and not failures
        ),
        "nonadjacent_cases": nonadjacent_cases,
        "adjacent_positive_control_cases": adjacent_cases,
        "steps": steps,
        "station_checks": station_checks,
        "occupied_station_checks": occupied_checks,
        "adjacent_double_allocator_matches":
            adjacent_double_allocator_matches,
        "allocator_gates": len(allocator),
        "program_stations": len(program),
        "failures": failures[:20],
        "implementation":
            "fresh X/CNOT/Toffoli interpreter over inherited gate lists",
    }


def guard_specific_recount() -> dict[str, Any]:
    rows = 0
    failures: list[tuple[int, int]] = []
    for position in range(RING_STATIONS):
        live = {
            position,
            (position + 1) % RING_STATIONS,
        }
        observed = 0
        for station in live:
            left = (station - 1) % RING_STATIONS
            right = (station + 1) % RING_STATIONS
            observed += int(left in live or right in live)
        rows += observed
        if observed != 2:
            failures.append((position, observed))
    return {
        "pass": rows == 22 and not failures,
        "scope":
            "one inherited Cycle-724/734 radius-one guard predicate at step 0",
        "violation_rows": rows,
        "used_as_controller_domain_boundary": False,
        "failures": failures,
    }


def independence_discipline() -> dict[str, Any]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    banned = {"apply_semantic", "apply_controller_step", "run_orbit"}
    used = sorted(
        {
            node.attr
            for node in ast.walk(tree)
            if isinstance(node, ast.Attribute) and node.attr in banned
        }
    )
    imported_cycle_modules = sorted(
        {
            alias.name
            for node in ast.walk(tree)
            if isinstance(node, ast.Import)
            for alias in node.names
            if alias.name.startswith("frontier_cycle")
        }
    )
    return {
        "pass": (
            not used
            and imported_cycle_modules
            == [
                "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
            ]
            and AUDIT_INPUT_PATHS
            == (
                PRIMARY_PATH,
                "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            )
        ),
        "banned_Cycle719_execution_helpers_used": used,
        "imported_cycle_modules": imported_cycle_modules,
        "primary_executed_in_subprocess": True,
        "declared_inputs": AUDIT_INPUT_PATHS,
    }


def main() -> int:
    started = perf_counter()
    results = {
        "primary_execution_contract": run_primary(),
        "template_set_recount": template_set_recount(),
        "fresh_gate_interpreter": gate_interpreter_recount(),
        "guard_specific_recount": guard_specific_recount(),
        "independence_discipline": independence_discipline(),
    }
    checks = {name: bool(detail["pass"]) for name, detail in results.items()}
    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "pass": all(checks.values()),
        "runtime_seconds": round(perf_counter() - started, 6),
        "certificates": results,
    }
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    ]
    lines.append(
        f"{report['checks_passed']}/{report['checks_total']} certificates PASS"
    )
    terminal = (
        "CYCLE735_BARE_TWO_TOKEN_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE735_BARE_TWO_TOKEN_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    text = "\n".join(lines) + "\nSUMMARY_JSON " + json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ) + "\n" + terminal + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
