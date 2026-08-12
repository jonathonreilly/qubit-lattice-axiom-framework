#!/usr/bin/env python3
"""Cycle-970 independent recomputation of the one-CNOT witness.

The checker imports none of the primary or substrate modules. It binds stable source
inputs, validates the freshly written primary cache envelope without pinning
timing-bearing cache bytes, independently validates the exact Cycle-719 to
Cycle-715 alias chain and the primary's equivalent local CNOT semantics by
AST, and recomputes the finite census with an independent XOR interpreter.

PASS predicates test source pinning, cache-envelope integrity, exact census
reconciliation, the positive witness, and resource bounds.
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
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
)
BLOCKLIST_CITED_PRIMARIES = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
(
    PRIMARY_PATH,
    PRIMARY_CACHE,
    AXIOM_PATH,
    CORE_PATH,
    HANDSHAKE_PATH,
    FINALIZER_PATH,
    BANK_PATH,
    RETURN_PATH,
    SEMANTICS_PATH,
) = AUDIT_INPUT_PATHS
SUBSTRATE_PATHS = AUDIT_INPUT_PATHS[3:]
EXPECTED_SHA256 = {
    PRIMARY_PATH: "361ebed36d4b29cfb60f27dbe4b452a8e0bac0a1b70cf07d58a4185923d2bf18",
    AXIOM_PATH: "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
    CORE_PATH: "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    HANDSHAKE_PATH: "0008837e938fdc589473967763c5319aeb5fc4996bd8380d5d33c3ec61062691",
    FINALIZER_PATH: "b514b0e20197bb0ce5e5440b4b0c1f2a0f74a1962b127e8a4e4a2e97c8f86a1a",
    BANK_PATH: "b8afe7e4697b0838715a079203930fb37bc7a6fc133e092f02a22141049aad8c",
    RETURN_PATH: "c9196fdfe2ed6101f7f62ac3552c9fb4944276b67f9f82fe326c89f8c21e23d7",
    SEMANTICS_PATH: "7ffe1dd4b169f774dce5bc9db29c5329c6e06c92e02506fbc734916ff11de884",
}
BLOCKLIST_MODULES = (
    "frontier_cycle970_inter_site_gate_2026_08_09",
    "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    "frontier_cycle719_local_handshake_controller_core_2026_07_26",
    "frontier_cycle719_source_local_finalizer_core_2026_07_26",
    "frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26",
    "frontier_cycle718_carrier_return_core_2026_07_26",
    "frontier_cycle715_recurrent_directional_packet_bank_2026_07_26",
)
ALIAS_CHAIN = (
    (CORE_PATH, "frontier_cycle719_local_handshake_controller_core_2026_07_26", "H", "H.A"),
    (HANDSHAKE_PATH, "frontier_cycle719_source_local_finalizer_core_2026_07_26", "M", "M.A"),
    (FINALIZER_PATH, "frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26", "B", "B.A"),
    (BANK_PATH, "frontier_cycle718_carrier_return_core_2026_07_26", "P", "P.A"),
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def parse_checker_payload(cache_text: str) -> dict | None:
    found = None
    for line in cache_text.splitlines():
        if line.startswith("CHECKER_PAYLOAD: "):
            found = json.loads(line[len("CHECKER_PAYLOAD: "):])
    return found


def parse_cache_header(cache_text: str) -> dict[str, str] | None:
    if not cache_text.startswith("===== runner cache v1 =====\n"):
        return None
    header_text = cache_text.split("----- stdout -----", 1)[0]
    fields: dict[str, str] = {}
    for line in header_text.splitlines()[1:]:
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value
    required = {
        "runner", "runner_sha256", "input_fingerprint_sha256",
        "exit_code", "status",
    }
    return fields if required <= set(fields) else None


def declared_input_fingerprint(paths: tuple[str, ...]) -> str:
    digest = sha256()
    digest.update(b"runner-cache-input-fingerprint-v1\0")
    for rel in paths:
        body = (ROOT / rel).read_bytes()
        rel_bytes = rel.encode("utf-8")
        digest.update(len(rel_bytes).to_bytes(8, "big"))
        digest.update(rel_bytes)
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


def top_assignments(tree: ast.Module, name: str) -> list[str]:
    return [
        ast.unparse(node.value)
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == name for target in node.targets)
    ]


def imports_as(tree: ast.Module, module: str, alias: str) -> bool:
    return any(
        isinstance(node, ast.Import)
        and any(item.name == module and item.asname == alias for item in node.names)
        for node in tree.body
    )


def semantics_alias_mutated(tree: ast.Module, alias: str) -> bool:
    protected = {"Gate", "x", "cn", "apply_semantic"}
    for node in tree.body:
        targets = []
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.append(node.target)
        if any(
            isinstance(target, ast.Attribute)
            and isinstance(target.value, ast.Name)
            and target.value.id == alias
            and target.attr in protected
            for target in targets
        ):
            return True
    return False


def substrate_ast_evidence(payloads: dict[str, bytes]) -> dict:
    edges = []
    for path, module, alias, assignment in ALIAS_CHAIN:
        tree = ast.parse(payloads[path].decode("utf-8"), filename=path)
        assignments = top_assignments(tree, "A")
        imported = imports_as(tree, module, alias)
        mutation = semantics_alias_mutated(tree, "A")
        edges.append({
            "path": path,
            "import_matches": imported,
            "a_assignments": assignments,
            "assignment_matches": assignments == [assignment],
            "semantics_alias_mutated": mutation,
            "pass": imported and assignments == [assignment] and not mutation,
        })

    return_tree = ast.parse(payloads[RETURN_PATH].decode("utf-8"), filename=RETURN_PATH)
    direct_import = imports_as(
        return_tree,
        "frontier_cycle715_recurrent_directional_packet_bank_2026_07_26",
        "A",
    )
    direct_assignments = top_assignments(return_tree, "A")
    direct_mutation = semantics_alias_mutated(return_tree, "A")
    edges.append({
        "path": RETURN_PATH,
        "import_matches": direct_import,
        "a_assignments": direct_assignments,
        "assignment_matches": direct_assignments == [],
        "semantics_alias_mutated": direct_mutation,
        "pass": direct_import and direct_assignments == [] and not direct_mutation,
    })

    tree = ast.parse(payloads[SEMANTICS_PATH].decode("utf-8"), filename=SEMANTICS_PATH)
    functions = {
        node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)
    }
    cn = functions.get("cn")
    apply_semantic = functions.get("apply_semantic")
    cn_return = next(
        (node.value for node in cn.body if isinstance(node, ast.Return)), None
    ) if cn is not None else None
    cnot_update = None
    if apply_semantic is not None:
        for node in ast.walk(apply_semantic):
            if isinstance(node, ast.If) and ast.unparse(node.test) == "gate.kind == 'CNOT'":
                cnot_update = next(
                    (item for item in node.body if isinstance(item, ast.AugAssign)), None
                )
                break
    cn_ok = cn_return is not None and ast.unparse(cn_return) == "Gate('CNOT', (control, target))"
    update_ok = (
        cnot_update is not None
        and isinstance(cnot_update.op, ast.BitXor)
        and ast.unparse(cnot_update.target) == "state[gate.wires[1]]"
        and ast.unparse(cnot_update.value) == "state[gate.wires[0]]"
    )
    semantics = {
        "path": SEMANTICS_PATH,
        "cn_shape": ast.unparse(cn_return) if cn_return is not None else "",
        "cnot_update": ast.unparse(cnot_update) if cnot_update is not None else "",
        "pass": cn_ok and update_ok,
    }
    return {
        "alias_edges": edges,
        "cycle715_semantics": semantics,
        "pass": all(edge["pass"] for edge in edges) and semantics["pass"],
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
    functions = {
        node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)
    }
    cn = functions.get("cn")
    apply_semantic = functions.get("apply_semantic")
    cn_return = next(
        (node.value for node in cn.body if isinstance(node, ast.Return)), None
    ) if cn is not None else None
    cn_shape = ast.unparse(cn_return) if cn_return is not None else ""
    cnot_update = None
    if apply_semantic is not None:
        for node in ast.walk(apply_semantic):
            if not isinstance(node, ast.If):
                continue
            test = ast.unparse(node.test)
            if test != "gate.kind == 'CNOT'":
                continue
            cnot_update = next(
                (item for item in node.body if isinstance(item, ast.AugAssign)), None
            )
            break
    imported_modules = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imported_modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported_modules.append(node.module or "")
    return {
        "literal_audit_input_paths": list(assigned) if assigned is not None else None,
        "matches_expected_primary_inputs": assigned == (AXIOM_PATH,) + SUBSTRATE_PATHS,
        "imported_modules": imported_modules,
        "imports_cycle719_or_cycle715": any(
            "cycle719" in name or "cycle715" in name for name in imported_modules
        ),
        "cn_shape": cn_shape,
        "cn_constructs_control_target_cnot": (
            cn_shape == "Gate('CNOT', (control, target))"
        ),
        "cnot_update": ast.unparse(cnot_update) if cnot_update is not None else "",
        "cnot_is_target_xor_control": (
            cnot_update is not None
            and isinstance(cnot_update.op, ast.BitXor)
            and ast.unparse(cnot_update.target) == "output[gate.wires[1]]"
            and ast.unparse(cnot_update.value) == "output[gate.wires[0]]"
        ),
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
        "witness_word": "CNOT(1->0)",
        "witness_before": before,
        "witness_after": after,
        "witness_distributions": witness_distributions,
        "construction_succeeded": witness_distributions[0] != witness_distributions[1],
        "state_mutated_on_neighbor_1": after[1] != before[1],
        "resolved_rows": resolved_rows,
    }


def main() -> int:
    started = monotonic()
    payloads = {
        rel: (ROOT / rel).read_bytes() if (ROOT / rel).is_file() else b""
        for rel in AUDIT_INPUT_PATHS
    }
    pin_rows = []
    for rel, expected in EXPECTED_SHA256.items():
        path = ROOT / rel
        body = payloads[rel]
        observed = sha256(body).hexdigest()
        pin_rows.append({
            "path": rel,
            "exists": path.is_file() and path.resolve().is_relative_to(ROOT.resolve()),
            "expected": expected,
            "observed": observed,
            "match": bool(body) and observed == expected,
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
    primary_ast = primary_ast_evidence(primary_text)
    substrate_ast = substrate_ast_evidence(payloads)
    primary_inputs = tuple(primary_ast["literal_audit_input_paths"] or ())
    cache_header = parse_cache_header(
        payloads[PRIMARY_CACHE].decode("utf-8", errors="replace")
    )
    expected_input_fingerprint = (
        declared_input_fingerprint(primary_inputs)
        if primary_ast["matches_expected_primary_inputs"] else ""
    )
    cache_envelope_ok = bool(
        cache_header
        and cache_header.get("runner") == PRIMARY_PATH
        and cache_header.get("runner_sha256") == sha256(payloads[PRIMARY_PATH]).hexdigest()
        and cache_header.get("input_fingerprint_sha256") == expected_input_fingerprint
        and cache_header.get("status") == "ok"
        and cache_header.get("exit_code") == "0"
    )

    first = direct_censuses()
    second = direct_censuses()
    deterministic = compact(first) == compact(second)

    primary_resolved = {
        "comparison_contexts": claims.get("resolved_total"),
        "changed_comparisons": claims.get("resolved_changed"),
        "conditioned_configurations": claims.get("conditioned_configurations"),
    }
    primary_construction = {
        "construction_succeeded": claims.get("construction_succeeded"),
        "gate_word": claims.get("gate_word"),
        "distribution_neighbor_0": claims.get("distribution_neighbor_0"),
        "distribution_neighbor_1": claims.get("distribution_neighbor_1"),
        "state_mutated_on_neighbor_1": claims.get("state_mutated_on_neighbor_1"),
    }
    primary_scope = {
        "route": claims.get("scope_route"),
        "family_words": claims.get("family_words"),
    }

    r0_ok = (
        pins_ok
        and not any(name in sys.modules for name in BLOCKLIST_MODULES)
        and primary_ast["matches_expected_primary_inputs"]
        and not primary_ast["imports_cycle719_or_cycle715"]
        and primary_ast["cn_constructs_control_target_cnot"]
        and primary_ast["cnot_is_target_xor_control"]
        and substrate_ast["pass"]
        and cache_envelope_ok
    )
    r0_finding = (
        f"pins_match={sum(row['match'] for row in pin_rows)}/{len(pin_rows)}; "
        f"primary_cache_envelope={cache_envelope_ok}; "
        f"BLOCKLIST_text_AST_only={list(BLOCKLIST_CITED_PRIMARIES)}; "
        f"blocked_modules_loaded={any(name in sys.modules for name in BLOCKLIST_MODULES)}; "
        f"transitive_cycle_import={primary_ast['imports_cycle719_or_cycle715']}; "
        f"self_contained_semantics={primary_ast['cnot_update']}; "
        f"cycle719_to_cycle715_ast_bridge={substrate_ast['pass']}"
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

    direct_distributions = [list(row) for row in first["witness_distributions"]]
    r2_ok = (
        parsed
        and first["construction_succeeded"]
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
    r2_finding = (
        f"independent_one_cnot_witness={first['construction_succeeded']}; "
        f"word={first['witness_word']}; D0={direct_distributions[0]}; "
        f"D1={direct_distributions[1]}; transition_n1="
        f"{list(first['witness_before'][1])}->{list(first['witness_after'][1])}"
    )

    r3_ok = (
        parsed
        and primary_scope.get("route") == "one_cnot_finite_family_witness"
        and primary_scope.get("family_words") == len(FAMILY)
    )
    r3_finding = (
        f"scope_route={primary_scope.get('route')}; "
        f"family_words={primary_scope.get('family_words')}; "
        f"contexts={first['resolved_total']}"
    )

    elapsed = monotonic() - started
    finding_size = sum(map(len, (r0_finding, r1_finding, r2_finding, r3_finding)))
    output_upper_bound = finding_size + 2_000
    r4_ok = (
        deterministic
        and elapsed < 1400
        and AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES
        and HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
        and tuple(AUDIT_INPUT_PATHS) == tuple(BLOCKLIST_CITED_PRIMARIES)
        and all((ROOT / rel).is_file() for rel in AUDIT_INPUT_PATHS)
    )
    r4_finding = (
        f"determinism_replay={deterministic}; runtime_s={elapsed:.6f}<1400; "
        f"stdout_upper_bound_bytes={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; "
        f"timeout_s={AUDIT_TIMEOUT_SEC}<1400; literal_inputs="
        f"{list(AUDIT_INPUT_PATHS)}"
    )

    certificates = [
        ("R0_SOURCE_PINS_CACHE_ENVELOPE_AND_AST", r0_ok, r0_finding),
        ("R1_INDEPENDENT_STATE_RESOLVED_CENSUS", r1_ok, r1_finding),
        ("R2_INDEPENDENT_ONE_CNOT_WITNESS", r2_ok, r2_finding),
        ("R3_SCOPE_RECONCILIATION", r3_ok, r3_finding),
        ("R4_CONTROLS", r4_ok, r4_finding),
    ]
    all_pass = all(ok for _, ok, _ in certificates)
    verdict = (
        "INDEPENDENT_ONE_CNOT_WITNESS_RECOMPUTED"
        if all_pass else "INDEPENDENT_CHECKS_INCOMPLETE"
    )
    receipt = {
        "cycle": 970,
        "role": "independent_checker",
        "claim_type": "bounded_theorem",
        "target_claim_type": "bounded_theorem",
        "claim_type_reason": (
            "independent finite-family recomputation of the exact one-CNOT witness"
        ),
        "verdict": verdict,
        "pins": pin_rows,
        "blocklist": list(BLOCKLIST_CITED_PRIMARIES),
        "primary_ast_evidence": primary_ast,
        "substrate_ast_evidence": substrate_ast,
        "primary_cache_envelope": cache_header,
        "primary_cache_envelope_valid": cache_envelope_ok,
        "independent_findings": {
            key: value for key, value in first.items()
            if key != "resolved_rows"
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
        "CYCLE 970 -- INDEPENDENT ONE-CNOT WITNESS CHECK",
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
