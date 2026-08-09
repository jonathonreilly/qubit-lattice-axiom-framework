#!/usr/bin/env python3
"""Cycle-970 independent checker, specified to REFUTE the gate result.

The checker never imports or executes the primary runner or Cycle-719 core.
It SHA-pins every cited input, treats Python sources as AST/text only, verifies
the landed three-CNOT SWAP macro structurally, and recomputes the full declared
two-site census with an independent XOR interpreter.  Disagreement is a
refutation and exits nonzero.

PASS predicates test pinning, reconciliation, agreement, and resource bounds.
They do not demand a positive dependence count or a successful construction.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle970_inter_site_gate_2026_08_09.py",
    "logs/runner-cache/frontier_cycle970_inter_site_gate_2026_08_09.txt",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
BLOCKLIST_CITED_PRIMARIES = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE, AXIOM_PATH, CORE_PATH = AUDIT_INPUT_PATHS
EXPECTED_SHA256 = {
    PRIMARY_PATH: "cb08af69f87b45ebd1fef2748493139fa249570d3986104857a523bfe79f4d6e",
    PRIMARY_CACHE: "ca9e621ee61d5346ff6fbf5e68f454962edfd1c215395dc208545b1c2cd3d654",
    AXIOM_PATH: "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
    CORE_PATH: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
BLOCKLIST_MODULES = (
    "frontier_cycle970_inter_site_gate_2026_08_09",
    "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def parse_checker_payload(cache_text: str) -> dict | None:
    found = None
    for line in cache_text.splitlines():
        if line.startswith("CHECKER_PAYLOAD: "):
            found = json.loads(line[len("CHECKER_PAYLOAD: "):])
    return found


def swap_word_ast_evidence(core_text: str) -> dict:
    """Verify the exact landed three-CNOT SWAP macro without importing it."""
    tree = ast.parse(core_text, filename=CORE_PATH)
    function = next(
        (
            node for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == "swap_word"
        ),
        None,
    )
    calls = []
    if function is not None:
        returned = next(
            (node.value for node in function.body if isinstance(node, ast.Return)),
            None,
        )
        if isinstance(returned, ast.Tuple):
            for element in returned.elts:
                if (
                    isinstance(element, ast.Call)
                    and isinstance(element.func, ast.Attribute)
                    and isinstance(element.func.value, ast.Name)
                    and element.func.value.id == "A"
                    and element.func.attr == "cn"
                    and len(element.args) == 2
                    and all(isinstance(arg, ast.Name) for arg in element.args)
                ):
                    calls.append(tuple(arg.id for arg in element.args))
                else:
                    calls.append(("AST_MISMATCH",))
    expected = [
        ("left", "right"),
        ("right", "left"),
        ("left", "right"),
    ]
    return {
        "swap_word_found": function is not None,
        "cnot_argument_order": calls,
        "matches_landed_three_cnot_word": calls == expected,
        "single_cnot_1_to_0_is_landed_gate_instance": ("left", "right") in calls,
    }


def primary_ast_evidence(primary_text: str) -> dict:
    tree = ast.parse(primary_text, filename=PRIMARY_PATH)
    assigned = None
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
               for target in node.targets):
            assigned = ast.literal_eval(node.value)
            break
    return {
        "literal_audit_input_paths": list(assigned) if assigned is not None else None,
        "matches_expected_primary_inputs": assigned == (AXIOM_PATH, CORE_PATH),
    }


# Independent representation: no gate object or function is imported from the
# primary or core.
FAMILY = (
    ("I", ()),
    ("X_0", (("X", 0),)),
    ("X_1", (("X", 1),)),
    ("CNOT_0_TO_1", (("CNOT", 0, 1),)),
    ("CNOT_1_TO_0", (("CNOT", 1, 0),)),
)


def apply_direct(state: tuple[int, int], word: tuple) -> tuple[int, int]:
    output = list(state)
    for gate in word:
        if gate[0] == "X":
            output[gate[1]] ^= 1
        elif gate[0] == "CNOT":
            output[gate[2]] ^= output[gate[1]]
        else:
            raise AssertionError(gate)
    return tuple(output)


def distribution_direct(
    word: tuple, target: int, local_input: int, neighbor_bit: int
) -> tuple[int, int]:
    state = [0, 0]
    state[target] = local_input
    state[1 - target] = neighbor_bit
    outcome = apply_direct(tuple(state), word)[target]
    return (int(outcome == 0), int(outcome == 1))


def direct_censuses() -> dict:
    resolved_rows = []
    for word_name, word in FAMILY:
        for target in (0, 1):
            for local_input in (0, 1):
                d0 = distribution_direct(word, target, local_input, 0)
                d1 = distribution_direct(word, target, local_input, 1)
                resolved_rows.append({
                    "word_name": word_name,
                    "target_site": target,
                    "local_input": local_input,
                    "d0": d0,
                    "d1": d1,
                    "changed": d0 != d1,
                })

    uniform_rows = []
    for word_name, word in FAMILY:
        for target in (0, 1):
            by_neighbor = []
            for neighbor_bit in (0, 1):
                # Exact numerators over two equiprobable local inputs.
                by_neighbor.append(tuple(
                    sum(distribution_direct(word, target, x, neighbor_bit)[y]
                        for x in (0, 1))
                    for y in (0, 1)
                ))
            uniform_rows.append({
                "word_name": word_name,
                "target_site": target,
                "numerators_n0": by_neighbor[0],
                "numerators_n1": by_neighbor[1],
                "changed": by_neighbor[0] != by_neighbor[1],
            })

    witness_word = (("CNOT", 1, 0),)
    before = ((0, 0), (0, 1))
    after = tuple(apply_direct(state, witness_word) for state in before)
    witness_distributions = tuple(
        distribution_direct(witness_word, 0, 0, neighbor_bit)
        for neighbor_bit in (0, 1)
    )
    return {
        "resolved_total": len(resolved_rows),
        "resolved_changed": sum(row["changed"] for row in resolved_rows),
        "uniform_total": len(uniform_rows),
        "uniform_changed": sum(row["changed"] for row in uniform_rows),
        "witness_word": "CNOT(1->0)",
        "witness_before": before,
        "witness_after": after,
        "witness_distributions": witness_distributions,
        "construction_succeeded": witness_distributions[0] != witness_distributions[1],
        "state_mutated_on_neighbor_1": after[1] != before[1],
        "resolved_rows": resolved_rows,
        "uniform_rows": uniform_rows,
    }


def main() -> int:
    started = monotonic()
    payloads = {}
    pin_rows = []
    for rel in AUDIT_INPUT_PATHS:
        path = ROOT / rel
        body = path.read_bytes() if path.is_file() else b""
        payloads[rel] = body
        observed = sha256(body).hexdigest()
        pin_rows.append({
            "path": rel,
            "exists": path.is_file() and path.resolve().is_relative_to(ROOT.resolve()),
            "expected": EXPECTED_SHA256[rel],
            "observed": observed,
            "match": bool(body) and observed == EXPECTED_SHA256[rel],
        })
    pins_ok = all(row["match"] and row["exists"] for row in pin_rows)

    try:
        claims = parse_checker_payload(
            payloads[PRIMARY_CACHE].decode("utf-8")
        )
        parsed = isinstance(claims, dict)
    except (UnicodeDecodeError, json.JSONDecodeError):
        claims = {}
        parsed = False
    if claims is None:
        claims = {}
    primary_text = payloads[PRIMARY_PATH].decode("utf-8", errors="replace")
    core_text = payloads[CORE_PATH].decode("utf-8", errors="replace")
    ast_evidence = swap_word_ast_evidence(core_text)
    primary_ast = primary_ast_evidence(primary_text)

    first = direct_censuses()
    second = direct_censuses()
    deterministic = compact(first) == compact(second)

    primary_resolved = {
        "comparison_contexts": claims.get("resolved_total"),
        "changed_comparisons": claims.get("resolved_changed"),
        "conditioned_configurations": claims.get("conditioned_configurations"),
    }
    primary_uniform = {
        "comparison_contexts": claims.get("uniform_total"),
        "changed_comparisons": claims.get("uniform_changed"),
    }
    primary_construction = {
        "construction_succeeded": claims.get("construction_succeeded"),
        "gate_word": claims.get("gate_word"),
        "distribution_neighbor_0": claims.get("distribution_neighbor_0"),
        "distribution_neighbor_1": claims.get("distribution_neighbor_1"),
        "state_mutated_on_neighbor_1": claims.get("state_mutated_on_neighbor_1"),
    }
    primary_price = {
        "route": claims.get("price_route"),
        "delta": claims.get("price_delta", {}),
        "axiom_ledger_entries": claims.get("axiom_ledger_entries"),
        "primitive_ledger_entries": claims.get("primitive_ledger_entries"),
    }

    r0_ok = (
        pins_ok
        and not any(name in sys.modules for name in BLOCKLIST_MODULES)
        and ast_evidence["matches_landed_three_cnot_word"]
        and ast_evidence["single_cnot_1_to_0_is_landed_gate_instance"]
        and primary_ast["matches_expected_primary_inputs"]
    )
    r0_finding = (
        f"pins_match={sum(row['match'] for row in pin_rows)}/{len(pin_rows)}; "
        f"BLOCKLIST_text_AST_only={list(BLOCKLIST_CITED_PRIMARIES)}; "
        f"blocked_modules_loaded={any(name in sys.modules for name in BLOCKLIST_MODULES)}; "
        f"swap_word_cnot_order={ast_evidence['cnot_argument_order']}"
    )

    r1_ok = (
        parsed
        and first["resolved_total"] == len(FAMILY) * 2 * 2
        and 0 <= first["resolved_changed"] <= first["resolved_total"]
        and primary_resolved.get("comparison_contexts") == first["resolved_total"]
        and primary_resolved.get("changed_comparisons") == first["resolved_changed"]
        and primary_resolved.get("conditioned_configurations")
            == 2 * first["resolved_total"]
    )
    r1_finding = (
        f"independent_state_resolved_changed={first['resolved_changed']}/"
        f"{first['resolved_total']}; primary="
        f"{primary_resolved.get('changed_comparisons')}/"
        f"{primary_resolved.get('comparison_contexts')}"
    )

    r2_ok = (
        parsed
        and first["uniform_total"] == len(FAMILY) * 2
        and 0 <= first["uniform_changed"] <= first["uniform_total"]
        and primary_uniform.get("comparison_contexts") == first["uniform_total"]
        and primary_uniform.get("changed_comparisons") == first["uniform_changed"]
    )
    r2_finding = (
        f"independent_uniform_self_input_changed={first['uniform_changed']}/"
        f"{first['uniform_total']}; primary="
        f"{primary_uniform.get('changed_comparisons')}/"
        f"{primary_uniform.get('comparison_contexts')}"
    )

    direct_distributions = [list(row) for row in first["witness_distributions"]]
    r3_ok = (
        parsed
        and primary_construction.get("construction_succeeded")
            == first["construction_succeeded"]
        and primary_construction.get("gate_word") == [first["witness_word"]]
        and primary_construction.get("distribution_neighbor_0")
            == direct_distributions[0]
        and primary_construction.get("distribution_neighbor_1")
            == direct_distributions[1]
        and primary_construction.get("state_mutated_on_neighbor_1")
            == first["state_mutated_on_neighbor_1"]
    )
    r3_finding = (
        f"independent_verdict="
        f"{'CONSTRUCTED' if first['construction_succeeded'] else 'OBSTRUCTED'}; "
        f"word={first['witness_word']}; D0={direct_distributions[0]}; "
        f"D1={direct_distributions[1]}; transition_n1="
        f"{list(first['witness_before'][1])}->{list(first['witness_after'][1])}"
    )

    expected_route = (
        "successful_landed_construction"
        if first["construction_succeeded"] else "failed_landed_construction"
    )
    primary_delta = primary_price.get("delta", {})
    r4_ok = (
        parsed
        and primary_price.get("route") == expected_route
        and (
            not first["construction_succeeded"]
            or (
                all(primary_delta.get(key) == 0 for key in (
                    "new_gate_classes", "new_couplings", "new_axioms",
                    "new_registered_primitives",
                ))
                and primary_delta.get("supplied_premises") == 1
                and primary_price.get("axiom_ledger_entries") == 4
                and primary_price.get("primitive_ledger_entries") == 3
            )
        )
    )
    r4_finding = (
        f"price_route={primary_price.get('route')}; "
        f"delta_gate/coupling/axiom/primitive="
        f"{[primary_delta.get(key) for key in ('new_gate_classes', 'new_couplings', 'new_axioms', 'new_registered_primitives')]}; "
        "uniform independence scoped, not deleted"
    )

    elapsed = monotonic() - started
    finding_size = sum(map(len, (r0_finding, r1_finding, r2_finding, r3_finding, r4_finding)))
    output_upper_bound = finding_size + 2_000
    r5_ok = (
        deterministic
        and elapsed < 1400
        and AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES
        and HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
        and tuple(AUDIT_INPUT_PATHS) == tuple(BLOCKLIST_CITED_PRIMARIES)
        and all((ROOT / rel).is_file() for rel in AUDIT_INPUT_PATHS)
    )
    r5_finding = (
        f"determinism_replay={deterministic}; runtime_s={elapsed:.6f}<1400; "
        f"stdout_upper_bound_bytes={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; "
        f"timeout_s={AUDIT_TIMEOUT_SEC}<1400; literal_inputs="
        f"{list(AUDIT_INPUT_PATHS)}"
    )

    certificates = [
        ("R0_PINS_BLOCKLIST_AND_LANDED_GATE_AST", r0_ok, r0_finding),
        ("R1_REFUTE_STATE_RESOLVED_CENSUS", r1_ok, r1_finding),
        ("R2_REFUTE_UNIFORM_CENSUS", r2_ok, r2_finding),
        ("R3_REFUTE_GATE_CONSTRUCTION", r3_ok, r3_finding),
        ("R4_REFUTE_PRICE_AND_SCOPE", r4_ok, r4_finding),
        ("R5_CONTROLS", r5_ok, r5_finding),
    ]
    all_pass = all(ok for _, ok, _ in certificates)
    verdict = (
        "PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT"
        if all_pass else "PRIMARY_REFUTED_ON_THIS_CHECK"
    )
    receipt = {
        "cycle": 970,
        "role": "independent_checker",
        "claim_type": "bounded_theorem",
        "verdict": verdict,
        "pins": pin_rows,
        "blocklist": list(BLOCKLIST_CITED_PRIMARIES),
        "primary_ast_evidence": primary_ast,
        "core_ast_evidence": ast_evidence,
        "independent_findings": {
            key: value for key, value in first.items()
            if key not in ("resolved_rows", "uniform_rows")
        },
        "runtime_sec": elapsed,
        "certificates": {
            name: {"pass": ok, "finding": finding}
            for name, ok, finding in certificates
        },
        "all_certificates_pass": all_pass,
    }

    lines = [
        "=" * 78,
        "CYCLE 970 -- INDEPENDENT CHECKER, SPECIFIED TO REFUTE",
        "=" * 78,
    ]
    lines.extend(
        f"{'PASS' if ok else 'FAIL'} {name} :: {finding}"
        for name, ok, finding in certificates
    )
    lines.append(f"VERDICT: {verdict}")
    pass_count = sum(ok for _, ok, _ in certificates)
    fail_count = len(certificates) - pass_count
    lines.append(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
    text = "\n".join(lines) + "\n"
    receipt["stdout_bytes"] = len(text.encode())
    receipt_path = (
        ROOT / "outputs" /
        "inter_site_gate_independent_check_cycle970_receipt_2026_08_09.json"
    )
    receipt_path.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    sys.stdout.write(text)
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
