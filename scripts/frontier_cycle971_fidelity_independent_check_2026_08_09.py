#!/usr/bin/env python3
"""Independent checker specified to REFUTE the axiom-fidelity re-read.

The checker never imports or executes the primary runner or any pinned corpus
runner.  It SHA-pins the primary source, validates stable science digests from
the runtime-bearing cache/receipt, extracts the primary's literal audit surface
by AST, independently rebuilds the commit-scoped token census, checks the
primary classes against a SHA-pinned adversarial adjudication ledger, and
independently searches every pinned Python AST for neighbour-resolved
distribution literals. Any disagreement is a refutation and exits nonzero.
PASS gates agreement and controls, never desired counts.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
PINNED_SNAPSHOT_COMMIT = "323d7fc32d77598f74ea6cd4d30c38dda0fe5070"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle971_axiom_fidelity_reread_2026_08_09.py",
    "logs/runner-cache/frontier_cycle971_axiom_fidelity_reread_2026_08_09.txt",
    "outputs/axiom_fidelity_reread_cycle971_receipt_2026_08_09.json",
    "outputs/axiom_fidelity_reread_cycle971_independent_semantic_adjudications_2026_08_09.json",
)
PINNED_SNAPSHOT_SURFACES = (
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/",
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/",
)
BLOCKLIST_CITED_PRIMARIES = AUDIT_INPUT_PATHS + PINNED_SNAPSHOT_SURFACES

import ast
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE, PRIMARY_RECEIPT, ADJUDICATION_PATH = AUDIT_INPUT_PATHS
EXPECTED_SHA256 = {
    PRIMARY_PATH: "6def914db02ae5cd6c4187a0fc20b11bd640bbb223cfce73ba2df7f675f4be63",
    ADJUDICATION_PATH: "e2b5195b9fd140d30eb551a3906c67dee1e603718b1ea6913d7410923716b68c",
}
EXPECTED_PRIMARY_SCIENCE_DIGEST = (
    "315a5231ab95899e90d8ff9ff1ef3c8126fe431d2a9e391fe90f2d8bbcf64fdc"
)
CLASS_NAMES = (
    "UNAFFECTED",
    "SUPPORT_READING_SAFE",
    "MEANING_CHANGED",
    "NEWLY_WITNESSABLE",
)
def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ("git", *args), cwd=ROOT, capture_output=True, check=check
    )


def git_text(*args: str) -> str:
    return git(*args).stdout.decode("utf-8", errors="replace")


def payload_from_cache(text: str) -> dict | None:
    found = None
    for line in text.splitlines():
        if line.startswith("CHECKER_PAYLOAD: "):
            found = json.loads(line.removeprefix("CHECKER_PAYLOAD: "))
    return found


def cache_header(text: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in text.splitlines():
        if line == "----- stdout -----":
            break
        if ": " in line:
            key, value = line.split(": ", 1)
            header[key] = value
    return header


def input_fingerprint(paths: tuple[str, ...]) -> str:
    hasher = sha256()
    hasher.update(b"runner-cache-input-fingerprint-v1\0")
    for rel in paths:
        body = (ROOT / rel).read_bytes()
        rel_bytes = rel.encode("utf-8")
        hasher.update(len(rel_bytes).to_bytes(8, "big"))
        hasher.update(rel_bytes)
        hasher.update(len(body).to_bytes(8, "big"))
        hasher.update(body)
    return hasher.hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            try:
                return ast.literal_eval(node.value)
            except (ValueError, TypeError):
                return None
    return None


def primary_ast_controls(text: str) -> dict:
    tree = ast.parse(text, filename=PRIMARY_PATH)
    imports = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    allowed_roots = {
        "__future__", "ast", "collections", "hashlib", "json", "pathlib",
        "re", "subprocess", "sys", "time",
    }
    return {
        "literal_pin": literal_assignment(tree, "PINNED_SNAPSHOT_COMMIT"),
        "literal_audit_input_paths": literal_assignment(tree, "AUDIT_INPUT_PATHS"),
        "literal_pinned_snapshot_surfaces": literal_assignment(
            tree, "PINNED_SNAPSHOT_SURFACES"
        ),
        "literal_blocklist": literal_assignment(tree, "BLOCKLIST_EXECUTION"),
        "imports": imports,
        "stdlib_only": all(name.split(".")[0] in allowed_roots for name in imports),
        "uses_git_ls_tree": '"ls-tree"' in text,
        "uses_git_show": '"show"' in text,
        "working_tree_corpus_reads": ".read_text(" in text or ".read_bytes(" in text,
    }


# The checker spells out its token grammar independently instead of importing
# the primary's compiled regular expressions.
TOKEN_RX = {
    "availability": re.compile(r"(?i)\b(?:availability|available)\b"),
    "vary_with": re.compile(r"(?i)\b(?:vary|varies|varied|varying)\s+with\b"),
    "nearest_neighbor_conditions": re.compile(
        r"(?i)\bnearest[-\s]neighbor conditions\b"
    ),
    "admissible_possibility": re.compile(
        r"(?i)\badmissible(?:\s+local)?\s+possibilit(?:y|ies)\b|"
        r"\bpossibilit(?:y|ies)\s+"
        r"(?:(?:is|are|be|being|become|becomes)\s+)?admissible\b"
    ),
}
GREP_ANCHOR = (
    r"\b(?:availability|available|vary|varies|varied|varying|nearest|"
    r"admissible|admissibility|possibility|possibilities)\b"
)


def pinned_corpus() -> dict:
    tracked = tuple(sorted(git_text(
        "ls-tree", "-r", "--name-only", PINNED_SNAPSHOT_COMMIT,
        "--", "docs", "scripts",
    ).splitlines()))
    selected = set()
    prefix = PINNED_SNAPSHOT_COMMIT + ":"
    found = git(
        "grep", "-I", "-i", "-P", "-l", GREP_ANCHOR,
        PINNED_SNAPSHOT_COMMIT, "--", "docs", "scripts", check=False,
    )
    if found.returncode not in (0, 1):
        raise RuntimeError(found.stderr.decode(errors="replace"))
    selected.update(
        row[len(prefix):] for row in found.stdout.decode(errors="replace").splitlines()
        if row.startswith(prefix)
    )
    if not selected <= set(tracked):
        raise AssertionError("candidate outside pinned tree")
    broad_bodies = {
        path: git_text("show", f"{PINNED_SNAPSHOT_COMMIT}:{path}")
        for path in sorted(selected)
    }
    candidates = tuple(
        path for path in sorted(selected)
        if any(regex.search(broad_bodies[path]) for regex in TOKEN_RX.values())
    )
    runner_paths = tuple(path for path in tracked if path.endswith(".py"))
    runner_bodies = {
        path: broad_bodies[path]
        if path in broad_bodies else git_text("show", f"{PINNED_SNAPSHOT_COMMIT}:{path}")
        for path in runner_paths
    }
    return {
        "tracked": tracked,
        "candidates": candidates,
        "bodies": {path: broad_bodies[path] for path in candidates},
        "runner_bodies": runner_bodies,
    }


def literal_numeric_dict(node: ast.AST) -> tuple[tuple[str, float], ...] | None:
    if not isinstance(node, ast.Dict):
        return None
    result = []
    for key_node, value_node in zip(node.keys, node.values):
        try:
            key, value = ast.literal_eval(key_node), ast.literal_eval(value_node)
        except (TypeError, ValueError):
            return None
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            return None
        result.append((key, float(value)))
    return tuple(sorted(result))


def independent_witness_rows(
    path: str, text: str, *, marginal_only: bool = False
) -> list[dict]:
    if not path.endswith(".py"):
        return []
    try:
        tree = ast.parse(text, filename=path)
    except SyntaxError:
        return []
    rows = []
    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    for function in functions:
        if not re.search(r"(?i)distribution|probability", function.name):
            continue
        if marginal_only and not re.search(
            r"(?i)marginal|uniform.*self.*input", function.name
        ):
            continue
        neighbor_args = {
            arg.arg for arg in function.args.args
            if re.search(r"(?i)neighbou?r", arg.arg)
        }
        if not neighbor_args:
            continue
        for branch in (node for node in ast.walk(function) if isinstance(node, ast.If)):
            test_names = {
                node.id for node in ast.walk(branch.test) if isinstance(node, ast.Name)
            }
            used = sorted(neighbor_args & test_names)
            if not used:
                continue
            true_values = [
                literal_numeric_dict(node.value) for node in branch.body
                if isinstance(node, ast.Return)
            ]
            false_values = [
                literal_numeric_dict(node.value) for node in branch.orelse
                if isinstance(node, ast.Return)
            ]
            if not false_values:
                false_values = [
                    literal_numeric_dict(node.value) for node in function.body
                    if isinstance(node, ast.Return) and node.lineno > branch.lineno
                ][:1]
            true_value = next((value for value in true_values if value is not None), None)
            false_value = next((value for value in false_values if value is not None), None)
            if (
                true_value is None or false_value is None or true_value == false_value
                or {key for key, _ in true_value} != {key for key, _ in false_value}
            ):
                continue
            true_support = sorted(key for key, value in true_value if value > 0.0)
            false_support = sorted(key for key, value in false_value if value > 0.0)
            rows.append({
                "path": path,
                "function": function.name,
                "neighbor_arguments": used,
                "condition_lineno": branch.lineno,
                "distribution_branch_true": dict(true_value),
                "distribution_branch_false": dict(false_value),
                "positive_support_true": true_support,
                "positive_support_false": false_support,
                "distribution_change_kind": (
                    "same_support_weight_change"
                    if true_support == false_support else "support_change"
                ),
                "literal_branch_pair_changed": True,
            })
    return rows


def independent_measurement(corpus: dict, adjudication: dict) -> dict:
    rows = []
    witnesses = [
        row
        for path, text in corpus["runner_bodies"].items()
        for row in independent_witness_rows(path, text)
    ]
    marginal_witnesses = [
        row
        for path, text in corpus["runner_bodies"].items()
        for row in independent_witness_rows(path, text, marginal_only=True)
    ]
    bodies = corpus["bodies"]
    consumer_paths = set(corpus["candidates"])
    nondefault = adjudication.get("nondefault_classes", {})
    classes = {
        name: sorted(nondefault.get(name, []))
        for name in CLASS_NAMES if name != "UNAFFECTED"
    }
    nondefault_paths = [path for paths in classes.values() for path in paths]
    classes["UNAFFECTED"] = sorted(consumer_paths - set(nondefault_paths))
    classes = {name: classes[name] for name in CLASS_NAMES}
    class_by_path = {
        path: name for name, paths in classes.items() for path in paths
    }
    adjudication_valid = (
        adjudication.get("pinned_snapshot_commit") == PINNED_SNAPSHOT_COMMIT
        and adjudication.get("default_class") == "UNAFFECTED"
        and adjudication.get("expected_consumer_file_count") == len(consumer_paths)
        and len(nondefault_paths) == len(set(nondefault_paths))
        and set(nondefault_paths) <= consumer_paths
        and set(class_by_path) == consumer_paths
        and adjudication.get("class_counts")
            == {name: len(classes[name]) for name in CLASS_NAMES}
    )
    for path in corpus["candidates"]:
        text = bodies[path]
        counts = {key: sum(1 for _ in regex.finditer(text)) for key, regex in TOKEN_RX.items()}
        rows.append({
            "path": path,
            "token_class_counts": counts,
            "classification": class_by_path.get(path),
        })
    state_paths = sorted({row["path"] for row in witnesses})
    marginal_paths = sorted({row["path"] for row in marginal_witnesses})
    token_rows = [
        {
            "path": row["path"],
            "token_class_counts": row["token_class_counts"],
        }
        for row in rows
    ]
    return {
        "tracked_file_count": len(corpus["tracked"]),
        "tracked_python_file_count": len(corpus["runner_bodies"]),
        "consumer_file_count": len(rows),
        "token_totals": {
            key: sum(row["token_class_counts"][key] for row in rows)
            for key in TOKEN_RX
        },
        "consumer_rows": rows,
        "row_digest": digest(token_rows),
        "classes": classes,
        "class_counts": {name: len(classes[name]) for name in CLASS_NAMES},
        "adjudication_manifest_valid": adjudication_valid,
        "state_paths": state_paths,
        "state_rows": witnesses,
        "marginal_paths": marginal_paths,
        "marginal_rows": marginal_witnesses,
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
        row = {
            "path": rel,
            "exists": path.is_file() and path.resolve().is_relative_to(ROOT.resolve()),
            "observed": observed,
        }
        if rel in EXPECTED_SHA256:
            row["expected"] = EXPECTED_SHA256[rel]
            row["match"] = bool(body) and observed == EXPECTED_SHA256[rel]
        else:
            row["expected"] = "stable science digest checked after parse"
            row["match"] = bool(body)
        pin_rows.append(row)
    pins_ok = all(row["exists"] and row["match"] for row in pin_rows)

    try:
        primary_text = payloads[PRIMARY_PATH].decode("utf-8")
        cache_text = payloads[PRIMARY_CACHE].decode("utf-8")
        primary_receipt = json.loads(payloads[PRIMARY_RECEIPT])
        semantic_adjudication = json.loads(payloads[ADJUDICATION_PATH])
        cache_payload = payload_from_cache(cache_text)
        primary_cache_header = cache_header(cache_text)
        parsed = (
            isinstance(primary_receipt, dict)
            and isinstance(cache_payload, dict)
            and isinstance(semantic_adjudication, dict)
        )
    except (UnicodeDecodeError, json.JSONDecodeError, SyntaxError):
        primary_text, cache_text, primary_receipt, cache_payload = "", "", {}, {}
        primary_cache_header, semantic_adjudication, parsed = {}, {}, False
    controls = primary_ast_controls(primary_text) if primary_text else {}
    primary_measurement = primary_receipt.get("measurement", {})
    primary_source_sha = sha256(payloads.get(PRIMARY_PATH, b"")).hexdigest()
    primary_input_paths = controls.get("literal_audit_input_paths") or ()
    expected_input_fingerprint = (
        input_fingerprint(primary_input_paths)
        if isinstance(primary_input_paths, tuple) and primary_input_paths else ""
    )
    cache_contract_ok = (
        primary_cache_header.get("runner") == PRIMARY_PATH
        and primary_cache_header.get("runner_sha256") == primary_source_sha
        and primary_cache_header.get("input_fingerprint_sha256")
            == expected_input_fingerprint
        and primary_cache_header.get("timeout_sec") == str(AUDIT_TIMEOUT_SEC)
        and primary_cache_header.get("exit_code") == "0"
        and primary_cache_header.get("status") == "ok"
    )
    science_pins_ok = (
        primary_receipt.get("science_digest") == EXPECTED_PRIMARY_SCIENCE_DIGEST
        and cache_payload.get("science_digest") == EXPECTED_PRIMARY_SCIENCE_DIGEST
    )

    corpus = pinned_corpus()
    first = independent_measurement(corpus, semantic_adjudication)
    second = independent_measurement(corpus, semantic_adjudication)
    deterministic = digest(first) == digest(second)

    r0_ok = (
        pins_ok and parsed and science_pins_ok and cache_contract_ok
        and controls.get("literal_pin") == PINNED_SNAPSHOT_COMMIT
        and controls.get("literal_audit_input_paths") == (
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
        )
        and controls.get("literal_pinned_snapshot_surfaces") == (
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/",
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/",
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/MINIMAL_AXIOMS_2026-06-29.md",
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/audit/data/axiom_premise_nodes.json",
        )
        and controls.get("stdlib_only")
        and controls.get("uses_git_ls_tree") and controls.get("uses_git_show")
        and not controls.get("working_tree_corpus_reads")
        and not any(
            name in sys.modules for name in (
                "frontier_cycle971_axiom_fidelity_reread_2026_08_09",
                "audit_companion_minimal_axioms_clean_base_exact",
            )
        )
    )
    r0_finding = (
        f"file_pins_present_or_match={sum(row['match'] for row in pin_rows)}/"
        f"{len(pin_rows)}; stable_science_digest_match={science_pins_ok}; "
        f"cache_contract_match={cache_contract_ok}; "
        f"literal_pin={controls.get('literal_pin')}; git_ls_tree/show="
        f"{controls.get('uses_git_ls_tree')}/{controls.get('uses_git_show')}; "
        f"working_tree_corpus_reads={controls.get('working_tree_corpus_reads')}; "
        f"BLOCKLIST_text_AST_only={list(BLOCKLIST_CITED_PRIMARIES)}"
    )

    r1_ok = (
        parsed
        and first["tracked_file_count"] == primary_measurement.get("tracked_file_count")
        and first["consumer_file_count"] == primary_measurement.get("consumer_file_count")
        and first["token_totals"] == primary_measurement.get("token_totals")
        and [
            {"path": row["path"], "token_class_counts": row["token_class_counts"]}
            for row in first["consumer_rows"]
        ] == [
            {"path": row["path"], "token_class_counts": row["token_class_counts"]}
            for row in primary_measurement.get("consumer_rows", [])
        ]
        and first["row_digest"] == primary_measurement.get("row_digest")
        and first["row_digest"] == cache_payload.get("row_digest")
        and primary_measurement.get("selector_anchor_complete") is True
        and cache_payload.get("selector_anchor_complete") is True
    )
    r1_finding = (
        f"independent_tracked/consumers={first['tracked_file_count']}/"
        f"{first['consumer_file_count']}; token_totals={compact(first['token_totals'])}; "
        f"row_digest={first['row_digest']}; exact_path_token_rows_match="
        f"{[(r['path'],r['token_class_counts']) for r in first['consumer_rows']] == [(r['path'],r['token_class_counts']) for r in primary_measurement.get('consumer_rows', [])]}"
    )

    r2_ok = (
        parsed
        and first["adjudication_manifest_valid"]
        and first["classes"] == primary_measurement.get("classes")
        and first["class_counts"] == primary_measurement.get("class_counts")
        and first["class_counts"] == cache_payload.get("class_counts")
        and digest(first["classes"]) == cache_payload.get("classes_digest")
        and sum(first["class_counts"].values()) == first["consumer_file_count"]
    )
    r2_finding = (
        f"independent_class_counts={compact(first['class_counts'])}; "
        f"adjudication_manifest_valid={first['adjudication_manifest_valid']}; "
        f"adjudication_manifest_sha256={EXPECTED_SHA256[ADJUDICATION_PATH]}; "
        f"full_lists_match={first['classes'] == primary_measurement.get('classes')}; "
        f"classes_digest={digest(first['classes'])}"
    )

    primary_vacuity = primary_measurement.get("vacuity_probe", {})
    r3_ok = (
        parsed
        and first["state_paths"] == primary_vacuity.get("state_resolved_witness_runner_paths")
        and first["state_rows"] == primary_vacuity.get("state_resolved_witness_rows")
        and first["marginal_paths"] == primary_vacuity.get("marginal_witness_runner_paths")
        and first["marginal_rows"] == primary_vacuity.get("marginal_witness_rows")
        and len(first["state_paths"]) == cache_payload.get("state_resolved_witness_runner_count")
        and len(first["state_rows"]) == cache_payload.get("state_resolved_literal_branch_pair_count")
        and len(first["marginal_paths"]) == cache_payload.get("marginal_witness_runner_count")
        and len(first["marginal_rows"]) == cache_payload.get("marginal_literal_branch_pair_count")
        and first["tracked_python_file_count"]
            == primary_measurement.get("tracked_python_file_count")
    )
    r3_finding = (
        f"independent_state_resolved_runners/branch_pairs="
        f"{len(first['state_paths'])}/{len(first['state_rows'])}; "
        f"independent_marginal_runners/branch_pairs="
        f"{len(first['marginal_paths'])}/{len(first['marginal_rows'])}; "
        f"pinned_python_files_scanned={first['tracked_python_file_count']}; "
        f"state_paths={first['state_paths']}; marginal_paths={first['marginal_paths']}"
    )

    axiom = corpus["bodies"]["docs/MINIMAL_AXIOMS_2026-06-29.md"]
    registry = corpus["bodies"]["docs/audit/data/axiom_premise_nodes.json"]
    axiom_flat, registry_flat = " ".join(axiom.split()), " ".join(registry.split())
    authority = {
        "new_distribution_sentence": (
            "For each site, the probability distribution over the possibilities is "
            "determined by, and varies with, the nearest-neighbor conditions."
            in axiom_flat
        ),
        "owner_date": "2026-08-05 owner-approved revision" in axiom_flat,
        "support_provenance": "availability became the distribution's support" in axiom_flat,
        "registry_support": "availability as the distribution's support" in registry_flat,
    }
    r4_ok = all(authority.values())
    r4_finding = f"independent_authority_checks={compact(authority)}"

    elapsed = monotonic() - started
    output_upper_bound = sum(map(len, (
        r0_finding, r1_finding, r2_finding, r3_finding, r4_finding,
    ))) + 3_500
    r5_ok = (
        deterministic and elapsed < AUDIT_TIMEOUT_SEC and AUDIT_TIMEOUT_SEC <= 300
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
        and tuple(BLOCKLIST_CITED_PRIMARIES)
            == tuple(AUDIT_INPUT_PATHS) + tuple(PINNED_SNAPSHOT_SURFACES)
    )
    r5_finding = (
        f"determinism_replay={deterministic}; runtime_s={elapsed:.6f}<"
        f"timeout_s={AUDIT_TIMEOUT_SEC}<=300; "
        f"stdout_upper_bound_bytes={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; "
        f"literal_AUDIT_INPUT_PATHS="
        f"{list(AUDIT_INPUT_PATHS)}"
    )

    certificates = (
        ("R0_REFUTE_PINS_BLOCKLIST_AND_SNAPSHOT_IO", r0_ok, r0_finding),
        ("R1_REFUTE_CONSUMER_CENSUS", r1_ok, r1_finding),
        ("R2_REFUTE_DELTA_CLASSIFICATION", r2_ok, r2_finding),
        ("R3_REFUTE_VACUITY_PROBE", r3_ok, r3_finding),
        ("R4_REFUTE_AXIOM_PROVENANCE", r4_ok, r4_finding),
        ("R5_CONTROLS", r5_ok, r5_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    verdict = (
        "PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT"
        if all_pass else "PRIMARY_REFUTED_ON_THIS_CHECK"
    )
    receipt = {
        "role": "independent_checker",
        "specified_to": "REFUTE",
        "claim_type": "meta",
        "pinned_snapshot_commit": PINNED_SNAPSHOT_COMMIT,
        "pins": pin_rows,
        "blocklist": list(BLOCKLIST_CITED_PRIMARIES),
        "primary_ast_controls": controls,
        "independent_summary": {
            "tracked_file_count": first["tracked_file_count"],
            "consumer_file_count": first["consumer_file_count"],
            "tracked_python_file_count": first["tracked_python_file_count"],
            "token_totals": first["token_totals"],
            "row_digest": first["row_digest"],
            "class_counts": first["class_counts"],
            "classes_digest": digest(first["classes"]),
            "adjudication_manifest_sha256": EXPECTED_SHA256[ADJUDICATION_PATH],
            "adjudication_manifest_valid": first["adjudication_manifest_valid"],
            "state_paths": first["state_paths"],
            "state_literal_branch_pairs": len(first["state_rows"]),
            "marginal_paths": first["marginal_paths"],
            "marginal_literal_branch_pairs": len(first["marginal_rows"]),
        },
        "authority_checks": authority,
        "determinism_replay": deterministic,
        "runtime_sec": elapsed,
        "certificates": {
            name: {"pass": ok, "finding": finding}
            for name, ok, finding in certificates
        },
        "all_certificates_pass": all_pass,
        "verdict": verdict,
    }

    lines = [
        "=" * 78,
        "INDEPENDENT AXIOM-FIDELITY CHECK, SPECIFIED TO REFUTE",
        "=" * 78,
    ]
    lines.extend(
        f"{'PASS' if ok else 'FAIL'} {name} :: {finding}"
        for name, ok, finding in certificates
    )
    lines.append(f"VERDICT: {verdict}")
    pass_count = sum(ok for _, ok, _ in certificates)
    lines.append(f"TOTAL: PASS={pass_count} FAIL={len(certificates) - pass_count}")
    text = "\n".join(lines) + "\n"
    receipt["stdout_bytes"] = len(text.encode())
    receipt_path = (
        ROOT / "outputs" /
        "axiom_fidelity_reread_independent_check_cycle971_receipt_2026_08_09.json"
    )
    receipt_path.write_text(json.dumps(receipt, indent=1, sort_keys=True) + "\n")
    sys.stdout.write(text)
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
