#!/usr/bin/env python3
"""Cycle-971 independent checker, specified to REFUTE the fidelity re-read.

The checker never imports or executes the primary runner or any pinned corpus
runner.  It SHA-pins the primary source/cache/receipt, extracts the primary's
literal audit surface by AST, independently rebuilds the commit-scoped token
census and semantic classes, and independently searches Python ASTs for
neighbour-resolved distribution literals.  Any disagreement is a refutation
and exits nonzero.  PASS gates agreement and controls, never desired counts.
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
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/",
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/",
)
BLOCKLIST_CITED_PRIMARIES = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE, PRIMARY_RECEIPT = AUDIT_INPUT_PATHS[:3]
EXPECTED_SHA256 = {
    PRIMARY_PATH: "c622cb6634287864f33982b35836c8532155f89fd14801c12000550a4f5969dc",
    PRIMARY_CACHE: "4ce9f8c2076b775384d3420be613cf03cf954b1ced8f800b86e18749142de11c",
    PRIMARY_RECEIPT: "d4894bce60db3b0ae5f39fee1f89677f4f52796bb6b2fca51c4f50335d649486",
}
CLASS_NAMES = (
    "UNAFFECTED",
    "SUPPORT_READING_SAFE",
    "MEANING_CHANGED",
    "NEWLY_WITNESSABLE",
)
MARGINAL_LITERALS = (
    "uniform_self_input_census",
    "uniform_self_input_changed",
    "uniform-self-input marginal",
    "uniform self input marginal",
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
GREP_PATTERNS = (
    r"\b(?:availability|available)\b",
    r"\b(?:vary|varies|varied|varying)\s+with\b",
    r"\bnearest[- ]neighbor conditions\b",
    r"\badmissible(?:\s+local)?\s+possibilit(?:y|ies)\b|"
    r"\bpossibilit(?:y|ies)\s+"
    r"(?:(?:is|are|be|being|become|becomes)\s+)?admissible\b",
)


def pinned_corpus() -> dict:
    tracked = tuple(sorted(git_text(
        "ls-tree", "-r", "--name-only", PINNED_SNAPSHOT_COMMIT,
        "--", "docs", "scripts",
    ).splitlines()))
    selected = set()
    prefix = PINNED_SNAPSHOT_COMMIT + ":"
    for pattern in GREP_PATTERNS:
        found = git(
            "grep", "-I", "-i", "-P", "-l", pattern,
            PINNED_SNAPSHOT_COMMIT, "--", "docs", "scripts", check=False,
        )
        if found.returncode not in (0, 1):
            raise RuntimeError(found.stderr.decode(errors="replace"))
        selected.update(
            row[len(prefix):] for row in found.stdout.decode(errors="replace").splitlines()
            if row.startswith(prefix)
        )
    candidates = tuple(sorted(selected))
    if not set(candidates) <= set(tracked):
        raise AssertionError("candidate outside pinned tree")
    return {
        "tracked": tracked,
        "candidates": candidates,
        "bodies": {
            path: git_text("show", f"{PINNED_SNAPSHOT_COMMIT}:{path}")
            for path in candidates
        },
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


def independent_witness_rows(path: str, text: str) -> list[dict]:
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
            rows.append({
                "path": path,
                "function": function.name,
                "neighbor_arguments": used,
                "condition_lineno": branch.lineno,
                "distribution_branch_true": dict(true_value),
                "distribution_branch_false": dict(false_value),
                "literal_branch_pair_changed": True,
            })
    return rows


def changed_reasons(text: str) -> list[str]:
    flat = " ".join(text.split())
    rules = (
        re.compile(
            r"(?i)(?:the\s+)?available\s+possibilities\s+are\s+determined\s+"
            r"by,?\s+and\s+vary\s+with,?\s+the\s+nearest[-\s]neighbor\s+conditions"
        ),
        re.compile(
            r"(?i)\b(?:neighbor-dependent|neighbour-dependent|neighbor-varying|"
            r"neighbour-varying)\s+availability\b"
        ),
        re.compile(
            r"(?i)\bavailability(?:\s+rule)?\b[^\n.;]{0,140}\b"
            r"(?:var(?:y|ies|ying)\s+with|depends?\s+on|determined\s+by|"
            r"neighbor-dependent|neighbour-dependent|neighbor-varying|"
            r"neighbour-varying)\b[^\n.;]{0,100}\b"
            r"(?:neighbor|neighbour|conditions?)\b"
        ),
        re.compile(
            r"(?i)\b(?:requires?|forces?|mandates?)\b[^\n.;]{0,120}\b"
            r"(?:neighbor-varying|neighbour-varying)\s+availability\b"
        ),
    )
    reasons = []
    for index, rule in enumerate(rules):
        match = rule.search(flat)
        if match is None:
            continue
        if index and "probability distribution" in match.group(0).lower():
            continue
        reasons.append(
            "old_available_possibilities_sentence"
            if index == 0 else f"availability_variation_pattern_{index}"
        )
    return reasons


def support_context(text: str) -> bool:
    new_sentence = re.compile(
        r"(?i)for\s+each\s+site,?\s+the\s+probability\s+distribution\s+over\s+"
        r"the\s+possibilities\s+is\s+determined\s+by,?\s+and\s+varies\s+with,?\s+"
        r"the\s+nearest[-\s]neighbor\s+conditions"
    )
    if new_sentence.search(text):
        return True
    semantic_words = re.compile(
        r"(?i)\b(?:admissib|possibilit|record|lock|support|neighbor|neighbour|axiom|site)"
    )
    for key in ("availability", "admissible_possibility"):
        for match in TOKEN_RX[key].finditer(text):
            context = text[max(0, match.start() - 180):match.end() + 180]
            if semantic_words.search(context):
                return True
    return False


def independent_measurement(corpus: dict) -> dict:
    rows = []
    witnesses = []
    bodies = corpus["bodies"]
    for path in corpus["candidates"]:
        text = bodies[path]
        counts = {key: sum(1 for _ in regex.finditer(text)) for key, regex in TOKEN_RX.items()}
        local_witnesses = independent_witness_rows(path, text)
        witnesses.extend(local_witnesses)
        reasons = changed_reasons(text)
        if local_witnesses:
            classification = "NEWLY_WITNESSABLE"
            evidence = [
                f"literal_neighbor_conditioned_distribution:{row['function']}"
                for row in local_witnesses
            ]
        elif reasons:
            classification, evidence = "MEANING_CHANGED", reasons
        elif support_context(text):
            classification = "SUPPORT_READING_SAFE"
            evidence = ["support_or_new_distribution_context"]
        else:
            classification = "UNAFFECTED"
            evidence = ["requested_token_without_second_sentence_use"]
        rows.append({
            "path": path,
            "token_class_counts": counts,
            "classification": classification,
            "classification_evidence": evidence,
        })
    classes = {
        name: [row["path"] for row in rows if row["classification"] == name]
        for name in CLASS_NAMES
    }
    state_paths = sorted({row["path"] for row in witnesses})
    marginal_paths = sorted(
        path for path in state_paths
        if any(marker in bodies[path].lower() for marker in MARGINAL_LITERALS)
    )
    return {
        "tracked_file_count": len(corpus["tracked"]),
        "consumer_file_count": len(rows),
        "token_totals": {
            key: sum(row["token_class_counts"][key] for row in rows)
            for key in TOKEN_RX
        },
        "consumer_rows": rows,
        "row_digest": digest(rows),
        "classes": classes,
        "class_counts": {name: len(classes[name]) for name in CLASS_NAMES},
        "state_paths": state_paths,
        "state_rows": witnesses,
        "marginal_paths": marginal_paths,
        "marginal_rows": [row for row in witnesses if row["path"] in marginal_paths],
    }


def main() -> int:
    started = monotonic()
    payloads = {}
    pin_rows = []
    for rel in AUDIT_INPUT_PATHS[:3]:
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
    pins_ok = all(row["exists"] and row["match"] for row in pin_rows)

    try:
        primary_text = payloads[PRIMARY_PATH].decode("utf-8")
        cache_text = payloads[PRIMARY_CACHE].decode("utf-8")
        primary_receipt = json.loads(payloads[PRIMARY_RECEIPT])
        cache_payload = payload_from_cache(cache_text)
        parsed = isinstance(primary_receipt, dict) and isinstance(cache_payload, dict)
    except (UnicodeDecodeError, json.JSONDecodeError, SyntaxError):
        primary_text, cache_text, primary_receipt, cache_payload, parsed = "", "", {}, {}, False
    controls = primary_ast_controls(primary_text) if primary_text else {}
    primary_measurement = primary_receipt.get("measurement", {})

    corpus = pinned_corpus()
    first = independent_measurement(corpus)
    second = independent_measurement(corpus)
    deterministic = digest(first) == digest(second)

    r0_ok = (
        pins_ok and parsed
        and controls.get("literal_pin") == PINNED_SNAPSHOT_COMMIT
        and controls.get("literal_audit_input_paths") == (
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
        f"pins_match={sum(row['match'] for row in pin_rows)}/{len(pin_rows)}; "
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
        and first["consumer_rows"] == primary_measurement.get("consumer_rows")
        and first["row_digest"] == primary_measurement.get("row_digest")
        and first["row_digest"] == cache_payload.get("row_digest")
    )
    r1_finding = (
        f"independent_tracked/consumers={first['tracked_file_count']}/"
        f"{first['consumer_file_count']}; token_totals={compact(first['token_totals'])}; "
        f"row_digest={first['row_digest']}; exact_rows_match="
        f"{first['consumer_rows'] == primary_measurement.get('consumer_rows')}"
    )

    r2_ok = (
        parsed
        and first["classes"] == primary_measurement.get("classes")
        and first["class_counts"] == primary_measurement.get("class_counts")
        and first["class_counts"] == cache_payload.get("class_counts")
        and digest(first["classes"]) == cache_payload.get("classes_digest")
        and sum(first["class_counts"].values()) == first["consumer_file_count"]
    )
    r2_finding = (
        f"independent_class_counts={compact(first['class_counts'])}; "
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
    )
    r3_finding = (
        f"independent_state_resolved_runners/branch_pairs="
        f"{len(first['state_paths'])}/{len(first['state_rows'])}; "
        f"independent_marginal_runners/branch_pairs="
        f"{len(first['marginal_paths'])}/{len(first['marginal_rows'])}; "
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
    ))) + 2_200
    r5_ok = (
        deterministic and elapsed < 1400 and AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
        and tuple(AUDIT_INPUT_PATHS) == tuple(BLOCKLIST_CITED_PRIMARIES)
    )
    r5_finding = (
        f"determinism_replay={deterministic}; runtime_s={elapsed:.6f}<1400; "
        f"stdout_upper_bound_bytes={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; "
        f"timeout_s={AUDIT_TIMEOUT_SEC}<1400; literal_AUDIT_INPUT_PATHS="
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
        "cycle": 971,
        "role": "independent_checker",
        "specified_to": "REFUTE",
        "claim_type": "bounded_theorem_measurement",
        "pinned_snapshot_commit": PINNED_SNAPSHOT_COMMIT,
        "pins": pin_rows,
        "blocklist": list(BLOCKLIST_CITED_PRIMARIES),
        "primary_ast_controls": controls,
        "independent_summary": {
            "tracked_file_count": first["tracked_file_count"],
            "consumer_file_count": first["consumer_file_count"],
            "token_totals": first["token_totals"],
            "row_digest": first["row_digest"],
            "class_counts": first["class_counts"],
            "classes_digest": digest(first["classes"]),
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
        "CYCLE 971 -- INDEPENDENT FIDELITY CHECK, SPECIFIED TO REFUTE",
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
