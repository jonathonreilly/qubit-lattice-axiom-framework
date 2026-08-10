#!/usr/bin/env python3
"""Cycle 971: pinned axiom-fidelity re-read of the landed docs/scripts corpus.

This runner is a measurement, not a repair.  It enumerates the tracked
``docs/`` and ``scripts/`` files at one literal Git commit, selects every file
containing one of four declared token classes, and classifies each selected
file under an operational semantic-delta rubric.  Snapshot contents are read
only through ``git ls-tree`` / ``git show`` (with commit-scoped ``git grep``
used only to select candidates); the working tree is never a census input.

The four classification labels mean:

* UNAFFECTED: no literal use of Admissibility's changed second-sentence
  availability semantics was found near the selected token.
* SUPPORT_READING_SAFE: availability/admissible possibility is used only as
  support, or the new distribution sentence is quoted without a stronger
  support-variation inference.
* MEANING_CHANGED: the file literally attributes mandatory neighbour
  variation/determination to availability or the available-possibility set,
  which the new distribution sentence does not itself license.
* NEWLY_WITNESSABLE: a tracked runner contains a literal conditional
  distribution function with distinct numeric probability dictionaries for
  neighbour-resolved branches.  That distribution-level witness was not axiom
  content under the old availability sentence.

All certificate truth values gate completeness, reconciliation, and controls.
They never require a desired class count or a nonzero/zero witness count.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
PINNED_SNAPSHOT_COMMIT = "323d7fc32d77598f74ea6cd4d30c38dda0fe5070"
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
PINNED_SNAPSHOT_SURFACES = (
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/",
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/",
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/MINIMAL_AXIOMS_2026-06-29.md",
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/audit/data/axiom_premise_nodes.json",
)
BLOCKLIST_EXECUTION = (
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/**",
    "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/**",
)

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
RECEIPT_PATH = (
    ROOT / "outputs" /
    "axiom_fidelity_reread_cycle971_receipt_2026_08_09.json"
)

TOKEN_PATTERNS = {
    "availability": re.compile(r"\b(?:availability|available)\b", re.I),
    "vary_with": re.compile(
        r"\b(?:vary|varies|varied|varying)\s+with\b", re.I
    ),
    "nearest_neighbor_conditions": re.compile(
        r"\bnearest[-\s]neighbor conditions\b", re.I
    ),
    "admissible_possibility": re.compile(
        r"\badmissible(?:\s+local)?\s+possibilit(?:y|ies)\b|"
        r"\bpossibilit(?:y|ies)\s+"
        r"(?:(?:is|are|be|being|become|becomes)\s+)?admissible\b",
        re.I,
    ),
}

OLD_SENTENCE = re.compile(
    r"(?:the\s+)?available\s+possibilities\s+are\s+determined\s+by,?\s+"
    r"and\s+vary\s+with,?\s+the\s+nearest[-\s]neighbor\s+conditions",
    re.I,
)
NEW_SENTENCE = re.compile(
    r"for\s+each\s+site,?\s+the\s+probability\s+distribution\s+over\s+the\s+"
    r"possibilities\s+is\s+determined\s+by,?\s+and\s+varies\s+with,?\s+"
    r"the\s+nearest[-\s]neighbor\s+conditions",
    re.I,
)
MEANING_CHANGED_PATTERNS = (
    OLD_SENTENCE,
    re.compile(
        r"\b(?:neighbor-dependent|neighbour-dependent|neighbor-varying|"
        r"neighbour-varying)\s+availability\b",
        re.I,
    ),
    re.compile(
        r"\bavailability(?:\s+rule)?\b[^\n.;]{0,140}\b(?:var(?:y|ies|ying)\s+"
        r"with|depends?\s+on|determined\s+by|neighbor-dependent|"
        r"neighbour-dependent|neighbor-varying|neighbour-varying)\b"
        r"[^\n.;]{0,100}\b(?:neighbor|neighbour|conditions?)\b",
        re.I,
    ),
    re.compile(
        r"\b(?:requires?|forces?|mandates?)\b.{0,120}\b"
        r"(?:neighbor-varying|neighbour-varying)\s+availability\b",
        re.I,
    ),
)
SUPPORT_CONTEXT = re.compile(
    r"\b(?:admissib|possibilit|record|lock|support|neighbor|neighbour|axiom|site)",
    re.I,
)
MARGINAL_MARKERS = (
    "uniform_self_input_census",
    "uniform_self_input_changed",
    "uniform-self-input marginal",
    "uniform self input marginal",
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
        ("git", *args), cwd=ROOT, check=check, capture_output=True
    )


def git_text(*args: str) -> str:
    return git(*args).stdout.decode("utf-8", errors="replace")


def snapshot_paths() -> tuple[str, ...]:
    output = git_text(
        "ls-tree", "-r", "--name-only", PINNED_SNAPSHOT_COMMIT,
        "--", "docs", "scripts",
    )
    return tuple(sorted(line for line in output.splitlines() if line))


def candidate_paths() -> tuple[str, ...]:
    # Git grep is only a commit-scoped selector.  Every selected body used for
    # counting/classification is subsequently read with git show.
    git_patterns = (
        r"\b(?:availability|available)\b",
        r"\b(?:vary|varies|varied|varying)\s+with\b",
        r"\bnearest[- ]neighbor conditions\b",
        r"\badmissible(?:\s+local)?\s+possibilit(?:y|ies)\b|"
        r"\bpossibilit(?:y|ies)\s+"
        r"(?:(?:is|are|be|being|become|becomes)\s+)?admissible\b",
    )
    selected: set[str] = set()
    prefix = PINNED_SNAPSHOT_COMMIT + ":"
    for pattern in git_patterns:
        result = git(
            "grep", "-I", "-i", "-P", "-l", pattern,
            PINNED_SNAPSHOT_COMMIT, "--", "docs", "scripts", check=False,
        )
        if result.returncode not in (0, 1):
            raise RuntimeError(result.stderr.decode(errors="replace"))
        for raw in result.stdout.decode(errors="replace").splitlines():
            if raw.startswith(prefix):
                selected.add(raw[len(prefix):])
    return tuple(sorted(selected))


def snapshot_body(path: str) -> str:
    return git_text("show", f"{PINNED_SNAPSHOT_COMMIT}:{path}")


def numeric_dict(node: ast.AST) -> tuple[tuple[str, float], ...] | None:
    if not isinstance(node, ast.Dict) or len(node.keys) != len(node.values):
        return None
    result = []
    for key_node, value_node in zip(node.keys, node.values):
        try:
            key = ast.literal_eval(key_node)
            value = ast.literal_eval(value_node)
        except (ValueError, TypeError):
            return None
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            return None
        result.append((key, float(value)))
    return tuple(sorted(result))


def names_in(node: ast.AST) -> set[str]:
    return {child.id for child in ast.walk(node) if isinstance(child, ast.Name)}


def literal_distribution_witnesses(path: str, text: str) -> list[dict]:
    """Find explicit neighbour-conditioned distinct numeric distributions."""
    if not path.endswith(".py"):
        return []
    try:
        tree = ast.parse(text, filename=path)
    except SyntaxError:
        return []
    rows = []
    for function in (
        node for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ):
        arg_names = {arg.arg for arg in function.args.args}
        neighbor_args = {
            name for name in arg_names
            if "neighbor" in name.lower() or "neighbour" in name.lower()
        }
        if not neighbor_args or not re.search(
            r"distribution|probability", function.name, re.I
        ):
            continue
        for conditional in (
            node for node in ast.walk(function) if isinstance(node, ast.If)
        ):
            used_neighbor_args = sorted(neighbor_args & names_in(conditional.test))
            if not used_neighbor_args:
                continue
            body_returns = [
                numeric_dict(node.value) for node in conditional.body
                if isinstance(node, ast.Return)
            ]
            else_returns = [
                numeric_dict(node.value) for node in conditional.orelse
                if isinstance(node, ast.Return)
            ]
            # A following return is the literal else branch for an early-return
            # conditional, as in the landed minimal-axioms companion.
            if not else_returns:
                following = [
                    node for node in function.body
                    if isinstance(node, ast.Return) and node.lineno > conditional.lineno
                ]
                else_returns = [numeric_dict(node.value) for node in following[:1]]
            left = next((value for value in body_returns if value is not None), None)
            right = next((value for value in else_returns if value is not None), None)
            if left is None or right is None or left == right:
                continue
            if {key for key, _ in left} != {key for key, _ in right}:
                continue
            rows.append({
                "path": path,
                "function": function.name,
                "neighbor_arguments": used_neighbor_args,
                "condition_lineno": conditional.lineno,
                "distribution_branch_true": dict(left),
                "distribution_branch_false": dict(right),
                "literal_branch_pair_changed": True,
            })
    return rows


def semantic_support_context(text: str) -> bool:
    if NEW_SENTENCE.search(text):
        return True
    for pattern_name in ("availability", "admissible_possibility"):
        for match in TOKEN_PATTERNS[pattern_name].finditer(text):
            window = text[max(0, match.start() - 180):match.end() + 180]
            if SUPPORT_CONTEXT.search(window):
                return True
    return False


def meaning_changed_evidence(text: str) -> list[str]:
    normalized = " ".join(text.split())
    labels = []
    for index, pattern in enumerate(MEANING_CHANGED_PATTERNS):
        match = pattern.search(normalized)
        if match is not None:
            # "availability ... probability distribution ... varies" is the
            # new support reading, not a claim that support itself must vary.
            if index > 0 and "probability distribution" in match.group(0).lower():
                continue
            labels.append((
                "old_available_possibilities_sentence"
                if index == 0 else f"availability_variation_pattern_{index}"
            ))
    return labels


def load_pinned_corpus() -> dict:
    tracked = snapshot_paths()
    candidates = candidate_paths()
    tracked_set = set(tracked)
    if not set(candidates) <= tracked_set:
        raise AssertionError("candidate selector escaped pinned docs/scripts tree")
    return {
        "tracked": tracked,
        "candidates": candidates,
        "bodies": {path: snapshot_body(path) for path in candidates},
    }


def census(corpus: dict) -> dict:
    tracked = corpus["tracked"]
    candidates = corpus["candidates"]
    bodies = corpus["bodies"]
    rows = []
    all_witness_rows = []
    for path in candidates:
        text = bodies[path]
        counts = {
            name: len(pattern.findall(text))
            for name, pattern in TOKEN_PATTERNS.items()
        }
        witness_rows = literal_distribution_witnesses(path, text)
        all_witness_rows.extend(witness_rows)
        changed_evidence = meaning_changed_evidence(text)
        if witness_rows:
            classification = "NEWLY_WITNESSABLE"
            evidence = [
                f"literal_neighbor_conditioned_distribution:{row['function']}"
                for row in witness_rows
            ]
        elif changed_evidence:
            classification = "MEANING_CHANGED"
            evidence = changed_evidence
        elif semantic_support_context(text):
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
    token_totals = dict(Counter({
        name: sum(row["token_class_counts"][name] for row in rows)
        for name in TOKEN_PATTERNS
    }))
    state_paths = sorted({row["path"] for row in all_witness_rows})
    marginal_paths = sorted(
        path for path in state_paths
        if any(marker in bodies[path].lower() for marker in MARGINAL_MARKERS)
    )
    marginal_rows = [
        row for row in all_witness_rows if row["path"] in marginal_paths
    ]
    return {
        "tracked_file_count": len(tracked),
        "consumer_file_count": len(rows),
        "token_totals": token_totals,
        "consumer_rows": rows,
        "row_digest": digest(rows),
        "classes": classes,
        "class_counts": {name: len(classes[name]) for name in CLASS_NAMES},
        "classification_complete_and_disjoint": (
            sum(len(paths) for paths in classes.values()) == len(rows)
            and set().union(*(set(paths) for paths in classes.values()))
                == set(candidates)
            and all(
                set(classes[left]).isdisjoint(classes[right])
                for i, left in enumerate(CLASS_NAMES)
                for right in CLASS_NAMES[i + 1:]
            )
        ),
        "vacuity_probe": {
            "method": (
                "Python-AST literal search for a distribution/probability "
                "function whose neighbor-named argument controls distinct "
                "numeric dictionary return branches; marginal witnesses "
                "additionally require an explicit uniform-self-input marker"
            ),
            "state_resolved_witness_runner_count": len(state_paths),
            "state_resolved_literal_branch_pair_count": len(all_witness_rows),
            "state_resolved_witness_runner_paths": state_paths,
            "state_resolved_witness_rows": all_witness_rows,
            "marginal_witness_runner_count": len(marginal_paths),
            "marginal_literal_branch_pair_count": len(marginal_rows),
            "marginal_witness_runner_paths": marginal_paths,
            "marginal_witness_rows": marginal_rows,
        },
    }


def object_pins() -> dict:
    commit = git_text("rev-parse", f"{PINNED_SNAPSHOT_COMMIT}^{{commit}}").strip()
    return {
        "snapshot_commit": commit,
        "snapshot_tree": git_text(
            "rev-parse", f"{PINNED_SNAPSHOT_COMMIT}^{{tree}}"
        ).strip(),
        "docs_tree": git_text(
            "rev-parse", f"{PINNED_SNAPSHOT_COMMIT}:docs"
        ).strip(),
        "scripts_tree": git_text(
            "rev-parse", f"{PINNED_SNAPSHOT_COMMIT}:scripts"
        ).strip(),
        "axiom_blob": git_text(
            "rev-parse", f"{PINNED_SNAPSHOT_COMMIT}:{AXIOM_PATH}"
        ).strip(),
        "registry_blob": git_text(
            "rev-parse", f"{PINNED_SNAPSHOT_COMMIT}:{REGISTRY_PATH}"
        ).strip(),
    }


def authority_checks() -> dict:
    axiom = snapshot_body(AXIOM_PATH)
    registry = snapshot_body(REGISTRY_PATH)
    normalized_axiom = " ".join(axiom.split())
    normalized_registry = " ".join(registry.split())
    return {
        "new_sentence_in_axiom": bool(NEW_SENTENCE.search(normalized_axiom)),
        "provenance_date_in_axiom": (
            "2026-08-05 owner-approved revision" in normalized_axiom
        ),
        "availability_support_in_axiom": (
            "availability became the distribution's support" in normalized_axiom
        ),
        "registry_has_new_sentence": bool(NEW_SENTENCE.search(normalized_registry)),
        "registry_has_support_note": (
            "availability as the distribution's support" in normalized_registry
        ),
    }


def main() -> int:
    started = monotonic()
    corpus = load_pinned_corpus()
    first = census(corpus)
    second = census(corpus)
    deterministic = digest(first) == digest(second)
    pins = object_pins()
    authority = authority_checks()

    rows = first["consumer_rows"]
    token_nonzero = all(
        any(value > 0 for value in row["token_class_counts"].values())
        for row in rows
    )
    sorted_unique = [row["path"] for row in rows] == sorted({
        row["path"] for row in rows
    })
    a_ok = token_nonzero and sorted_unique and first["consumer_file_count"] == len(rows)
    a_finding = (
        f"pinned_snapshot={PINNED_SNAPSHOT_COMMIT}; tracked_files="
        f"{first['tracked_file_count']}; consumer_files={len(rows)}; "
        f"token_totals={compact(first['token_totals'])}; file_to_token_counts="
        f"receipt.consumer_rows; row_digest={first['row_digest']}"
    )

    class_counts = first["class_counts"]
    b_ok = (
        first["classification_complete_and_disjoint"]
        and tuple(class_counts) == CLASS_NAMES
        and sum(class_counts.values()) == len(rows)
    )
    b_finding = (
        f"class_counts={compact(class_counts)}; complete_disjoint="
        f"{first['classification_complete_and_disjoint']}; full_file_lists="
        "receipt.classes; classification is measurement-only"
    )

    vacuity = first["vacuity_probe"]
    state_count = vacuity["state_resolved_witness_runner_count"]
    state_pairs = vacuity["state_resolved_literal_branch_pair_count"]
    marginal_count = vacuity["marginal_witness_runner_count"]
    marginal_pairs = vacuity["marginal_literal_branch_pair_count"]
    c_ok = (
        state_count == len(vacuity["state_resolved_witness_runner_paths"])
        and state_pairs == len(vacuity["state_resolved_witness_rows"])
        and marginal_count == len(vacuity["marginal_witness_runner_paths"])
        and marginal_pairs == len(vacuity["marginal_witness_rows"])
        and set(vacuity["marginal_witness_runner_paths"]) <= set(
            vacuity["state_resolved_witness_runner_paths"]
        )
    )
    c_finding = (
        f"literal_state_resolved_witness_runners={state_count}; "
        f"literal_state_resolved_branch_pairs={state_pairs}; "
        f"literal_marginal_witness_runners={marginal_count}; "
        f"literal_marginal_branch_pairs={marginal_pairs}; "
        f"state_paths={vacuity['state_resolved_witness_runner_paths']}; "
        f"marginal_paths={vacuity['marginal_witness_runner_paths']}; "
        "a marginal-independence row would not refute state-resolved dependence"
    )

    elapsed = monotonic() - started
    output_upper_bound = sum(map(len, (a_finding, b_finding, c_finding))) + 2_200
    d_ok = (
        pins["snapshot_commit"] == PINNED_SNAPSHOT_COMMIT
        and all(authority.values())
        and deterministic
        and tuple(AUDIT_INPUT_PATHS) == (
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
            "docs/audit/data/axiom_premise_nodes.json",
        )
        and tuple(PINNED_SNAPSHOT_SURFACES) == (
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/",
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/",
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/MINIMAL_AXIOMS_2026-06-29.md",
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/audit/data/axiom_premise_nodes.json",
        )
        and BLOCKLIST_EXECUTION == (
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:docs/**",
            "323d7fc32d77598f74ea6cd4d30c38dda0fe5070:scripts/**",
        )
        and elapsed < 1400
        and AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    d_finding = (
        f"object_pins={compact(pins)}; authority_checks={compact(authority)}; "
        f"BLOCKLIST={list(BLOCKLIST_EXECUTION)} execution=False; "
        f"determinism_replay={deterministic}; runtime_s={elapsed:.6f}<1400; "
        f"stdout_upper_bound_bytes={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; "
        f"timeout_s={AUDIT_TIMEOUT_SEC}<1400; literal_AUDIT_INPUT_PATHS="
        f"{list(AUDIT_INPUT_PATHS)}; pinned_snapshot_surfaces="
        f"{list(PINNED_SNAPSHOT_SURFACES)}"
    )

    certificates = (
        ("A_CONSUMER_CENSUS", a_ok, a_finding),
        ("B_DELTA_CLASSIFICATION", b_ok, b_finding),
        ("C_VACUITY_PROBE", c_ok, c_finding),
        ("D_CONTROLS", d_ok, d_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    report = {
        "cycle": 971,
        "claim_type": "bounded_theorem",
        "actual_current_surface_status": "bounded-support",
        "trace_class": "methodology",
        "reachability_to_target": "none",
        "measurement_only": True,
        "rewrite_proposals": [],
        "pinned_snapshot_commit": PINNED_SNAPSHOT_COMMIT,
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "pinned_snapshot_surfaces": list(PINNED_SNAPSHOT_SURFACES),
        "blocklist_execution": list(BLOCKLIST_EXECUTION),
        "object_pins": pins,
        "authority_checks": authority,
        "measurement": first,
        "determinism_replay": deterministic,
        "science_digest": digest(first),
        "runtime_sec": elapsed,
        "certificates": {
            name: {"pass": ok, "finding": finding}
            for name, ok, finding in certificates
        },
        "all_certificates_pass": all_pass,
    }

    lines = [
        "=" * 78,
        "CYCLE 971 -- AXIOM-FIDELITY RE-READ (PINNED MEASUREMENT)",
        "=" * 78,
    ]
    lines.extend(
        f"{'PASS' if ok else 'FAIL'} {name} :: {finding}"
        for name, ok, finding in certificates
    )
    checker_payload = {
        "pinned_snapshot_commit": PINNED_SNAPSHOT_COMMIT,
        "tracked_file_count": first["tracked_file_count"],
        "consumer_file_count": first["consumer_file_count"],
        "token_totals": first["token_totals"],
        "row_digest": first["row_digest"],
        "class_counts": class_counts,
        "classes_digest": digest(first["classes"]),
        "state_resolved_witness_runner_count": state_count,
        "state_resolved_literal_branch_pair_count": state_pairs,
        "marginal_witness_runner_count": marginal_count,
        "marginal_literal_branch_pair_count": marginal_pairs,
        "state_paths": vacuity["state_resolved_witness_runner_paths"],
        "marginal_paths": vacuity["marginal_witness_runner_paths"],
        "science_digest": report["science_digest"],
    }
    lines.append("CHECKER_PAYLOAD: " + compact(checker_payload))
    lines.append(
        "VERDICT: " + (
            "PINNED_AXIOM_FIDELITY_MEASUREMENT_COMPLETE"
            if all_pass else "PINNED_AXIOM_FIDELITY_MEASUREMENT_INCOMPLETE"
        )
    )
    pass_count = sum(ok for _, ok, _ in certificates)
    lines.append(f"TOTAL: PASS={pass_count} FAIL={len(certificates) - pass_count}")
    text = "\n".join(lines) + "\n"
    report["stdout_bytes"] = len(text.encode())
    RECEIPT_PATH.write_text(json.dumps(report, indent=1, sort_keys=True) + "\n")

    sys.stdout.write(text)
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
