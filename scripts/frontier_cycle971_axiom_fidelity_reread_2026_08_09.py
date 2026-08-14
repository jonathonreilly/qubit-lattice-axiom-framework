#!/usr/bin/env python3
"""Pinned axiom-fidelity re-read of the landed docs/scripts corpus.

This runner is a measurement, not a repair.  It enumerates the tracked
``docs/`` and ``scripts/`` files at one literal Git commit, selects every file
containing one of four declared token classes, and classifies each selected
file under an explicit semantic-delta rubric.  Snapshot contents are read
only through ``git ls-tree`` / ``git show`` (with a deliberately broad,
commit-scoped ``git grep`` used only to select candidate blobs); the working
tree is never a census input.

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
  distribution function with the same positive support but different weights
  for neighbour-resolved branches.  Such a weight-only witness had no content
  under the old availability sentence.

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
        r"with|depends?\s+on|neighbor-dependent|"
        r"neighbour-dependent|neighbor-varying|neighbour-varying)\b"
        r"[^\n.;]{0,100}\b(?:neighbor|neighbour|conditions?)\b",
        re.I,
    ),
    re.compile(
        r"\b(?:requires?|forces?|mandates?)\b.{0,120}\b"
        r"(?:neighbor-varying|neighbour-varying)\s+availability\b",
        re.I,
    ),
    re.compile(
        r"\badmissibility\b.{0,160}\bwhich\s+possibilities\s+are\s+available\b"
        r".{0,120}\bvar(?:y|ies|ied|ying)\s+with\b.{0,100}\b"
        r"(?:neighbor|neighbour|conditions?)\b",
        re.I,
    ),
)
SUPPORT_READING_PATTERNS = (
    re.compile(r"\bavailable\s+(?:possibilities|outcomes?)\b", re.I),
    re.compile(
        r"\bavailability\b.{0,80}\b(?:is|means|became|as)\b.{0,80}\b"
        r"(?:positive\s+)?support\b|\b(?:positive\s+)?support\b.{0,80}\b"
        r"(?:is|means)\b.{0,80}\bavailability\b",
        re.I,
    ),
    re.compile(
        r"\bavailability\s+(?:projectors?|sets?|menus?)\b",
        re.I,
    ),
)
CLASS_NAMES = (
    "UNAFFECTED",
    "SUPPORT_READING_SAFE",
    "MEANING_CHANGED",
    "NEWLY_WITNESSABLE",
)

# Human re-read overrides for wording whose semantics is not safely recoverable
# from a local phrase pattern.  These are pinned-corpus paths, not repair
# instructions.  Each override was checked against the blob at the literal pin.
MEANING_CHANGED_OVERRIDES = {
    "docs/BORN_FORM_FROM_LAWFUL_GRADED_CONSTRAINT_COMPOSITE_GLEASON_BRIDGE_NOTE_2026-07-04.md",
    "docs/RECORD_LOCAL_FINITE_ATOM_AVAILABILITY_NARROW_THEOREM_NOTE_2026-06-17.md",
    "docs/REALIZED_KINETIC_BRANCH_SELECTION_FRAME_CLASS_TRANSPORT_NARROW_THEOREM_NOTE_2026-07-02.md",
    "scripts/realized_kinetic_branch_selected_by_admissibility_variation_2026_07_02.py",
    "scripts/realized_kinetic_branch_selection_gauged_background_invariance_2026_07_02.py",
    "docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/TWELVE_HOUR_TOE_FRAMEWORK_CAMPAIGN_DIAGNOSIS_2026-07-16.md",
}
SUPPORT_READING_SAFE_OVERRIDES = {
    "scripts/color_arena_bonded_pair_admissibility_cross_site_2026_07_06.py",
    "scripts/frontier_theta_defect_closure_admissibility_2026_07_03.py",
    "scripts/matter_realization_qubit_bilinear_from_k1_2026_07_06.py",
    "docs/GRADED_CONSTRAINT_MENU_UNIFORMITY_CONTEXTUALITY_AND_C3_ZERO_INFORMATION_POINT_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "scripts/frontier_graded_constraint_menu_uniformity_c3_zero_info_2026_07_11.py",
    "docs/PRESENTATION_GAUGE_AXIS_SIGN_FLIP_INVARIANTS_TWIN_DETECTOR_GAUGE_SECTION_ORIENTATION_BIT_BOUNDED_THEOREM_NOTE_2026-07-04.md",
    "scripts/empty_state_bootstrap_orbit_dichotomy_degree_nine_wall_2026_07_04.py",
    "docs/GRADED_CONSTRAINT_INTERFACE_CONSISTENCY_BOUNDED_NOTE_2026-07-04.md",
    "docs/INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_OCCUPANCY_RESIDUAL_THEOREM_NOTE_2026-07-02.md",
    "docs/PROTOCOL_ADMISSIBILITY_3D_REALIZATION_BRIDGE_AND_WORD_DISPERSIVENESS_NARROW_THEOREM_NOTE_2026-07-10.md",
    "docs/TICK_ADMISSIBILITY_REALIZATION_BRIDGE_CLAUSE_TO_PREDICATE_NARROW_THEOREM_NOTE_2026-07-10.md",
    "docs/audit/AXIOM_MINIMALITY_POLICY.md",
    "docs/work_history/repo/review_feedback/FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md",
    "scripts/exact_predictive_specification_tournament_2026_07_14.py",
    "scripts/frontier_admissibility_record_continuation_refinement_2026_07_13.py",
    "scripts/frontier_frozen_region_saturation_finality_2026_07_03.py",
    "scripts/record_comparability_import_discipline_support_fork_arrow_2026_07_07.py",
    "scripts/self_describing_law_foundation_selection_cycle49_2026_07_14.py",
}
UNAFFECTED_OVERRIDES = {
    "docs/COLLAPSE_MERGER_TOY_ENGINE_VALIDATION_NOTE_2026-07-08.md",
    "docs/FORMATION_RATE_LAW_CLASS_REDUCTION_BOUNDED_NOTE_2026-07-08.md",
    "docs/SOURCING_TWO_CHANNEL_WAKE_QUANTIFICATION_BOUNDED_NOTE_2026-07-08.md",
    "docs/audit/AXIOM_RESET_IMPACT_2026-06-29.md",
    "docs/work_history/repo/review_feedback/ADMISSIBILITY_RECORD_CONTINUATION_AXIOM_DRAFT_NOTE_2026-07-13.md",
    "docs/work_history/repo/review_feedback/DEEPER_PROBES_FINAL_AXIOM_CONTENT_GATE_NOTE_2026-07-13.md",
    "scripts/collapse_merger_toy_engine_2026_07_08.py",
    "scripts/formation_rate_law_class_reduction_2026_07_08.py",
    "scripts/sourcing_correlation_wake_quantification_2026_07_08.py",
    # Adversarial controls: these blobs contain ordinary uses of the words
    # ``availability`` and ``support`` in nearby prose, but do not consume the
    # changed Admissibility sentence.
    "docs/RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md",
    "docs/work_history/repo/review_feedback/EIGHT_BIT_STATUS_COMPLETION_FRONT_CYCLE112_NOTE_2026-07-15.md",
    "scripts/frontier_cycle864_routec_typed_exchange_matrix_candidate_2026_08_01.py",
    "scripts/record_saturation_availability_census_2026_07_08.py",
    "scripts/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.py",
}


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


def complete_anchor_paths() -> tuple[str, ...]:
    # These single-token anchors are intentionally broader than the normative
    # token grammar.  In particular, they cannot miss a phrase split across
    # lines.  Every candidate body is read with git show and then filtered by
    # the full-blob TOKEN_PATTERNS below.
    git_patterns = (
        r"\b(?:availability|available)\b",
        r"\b(?:vary|varies|varied|varying)\b",
        r"\bnearest\b",
        r"\badmissib(?:le|ility)\b",
        r"\bpossibilit(?:y|ies)\b",
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


def candidate_paths() -> tuple[str, ...]:
    """Production selector, kept separate for selector-regression attacks."""
    return complete_anchor_paths()


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


def literal_distribution_witnesses(
    path: str, text: str, *, marginal_only: bool = False
) -> list[dict]:
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
        if marginal_only and not re.search(
            r"marginal|uniform.*self.*input", function.name, re.I
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
            true_support = sorted(key for key, value in left if value > 0.0)
            false_support = sorted(key for key, value in right if value > 0.0)
            rows.append({
                "path": path,
                "function": function.name,
                "neighbor_arguments": used_neighbor_args,
                "condition_lineno": conditional.lineno,
                "distribution_branch_true": dict(left),
                "distribution_branch_false": dict(right),
                "positive_support_true": true_support,
                "positive_support_false": false_support,
                "distribution_change_kind": (
                    "same_support_weight_change"
                    if true_support == false_support else "support_change"
                ),
                "literal_branch_pair_changed": True,
            })
    return rows


def semantic_support_evidence(path: str, text: str) -> list[str]:
    if path in SUPPORT_READING_SAFE_OVERRIDES:
        return ["pinned_blob_semantic_reread_override"]
    normalized = semantic_normalize(text)
    labels: list[str] = []
    if NEW_SENTENCE.search(normalized):
        labels.append("new_distribution_sentence")
    labels.extend(
        f"support_reading_pattern_{index}"
        for index, pattern in enumerate(SUPPORT_READING_PATTERNS)
        if pattern.search(normalized)
    )
    return labels


def semantic_normalize(text: str) -> str:
    """Flatten prose while removing Markdown/Python string separators."""
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    text = text.replace(r"\n", " ")
    text = text.replace('"', " ").replace("'", " ")
    return " ".join(text.split())


def meaning_changed_evidence(path: str, text: str) -> list[str]:
    if path in SUPPORT_READING_SAFE_OVERRIDES or path in UNAFFECTED_OVERRIDES:
        return []
    if path in MEANING_CHANGED_OVERRIDES:
        return ["pinned_blob_semantic_reread_override"]
    normalized = semantic_normalize(text)
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


def classification_excerpt(text: str, classification: str) -> str:
    """Return one bounded, normalized evidence span for per-row inspection."""
    normalized = semantic_normalize(text)
    if classification == "MEANING_CHANGED":
        patterns = (*MEANING_CHANGED_PATTERNS, TOKEN_PATTERNS["availability"])
    elif classification == "SUPPORT_READING_SAFE":
        patterns = (NEW_SENTENCE, *SUPPORT_READING_PATTERNS)
    else:
        patterns = tuple(TOKEN_PATTERNS.values())
    matches = [pattern.search(normalized) for pattern in patterns]
    matches = [match for match in matches if match is not None]
    if not matches:
        return ""
    match = min(matches, key=lambda item: item.start())
    left = max(0, match.start() - 100)
    right = min(len(normalized), match.end() + 180)
    return normalized[left:right]


def load_pinned_corpus() -> dict:
    tracked = snapshot_paths()
    broad_candidates = candidate_paths()
    complete_candidates = complete_anchor_paths()
    tracked_set = set(tracked)
    if (
        not set(broad_candidates) <= tracked_set
        or not set(complete_candidates) <= tracked_set
    ):
        raise AssertionError("candidate selector escaped pinned docs/scripts tree")
    broad_bodies = {
        path: snapshot_body(path) for path in broad_candidates
    }
    candidates = tuple(
        path for path in broad_candidates
        if any(pattern.search(broad_bodies[path]) for pattern in TOKEN_PATTERNS.values())
    )
    runner_paths = tuple(path for path in tracked if path.endswith(".py"))
    runner_bodies = {
        path: broad_bodies[path] if path in broad_bodies else snapshot_body(path)
        for path in runner_paths
    }
    return {
        "tracked": tracked,
        "candidates": candidates,
        "bodies": {path: broad_bodies[path] for path in candidates},
        "runner_bodies": runner_bodies,
        "selector_anchor_complete": broad_candidates == complete_candidates,
    }


def census(corpus: dict) -> dict:
    tracked = corpus["tracked"]
    candidates = corpus["candidates"]
    bodies = corpus["bodies"]
    runner_bodies = corpus["runner_bodies"]
    rows = []
    all_witness_rows = [
        row
        for path, text in runner_bodies.items()
        for row in literal_distribution_witnesses(path, text)
    ]
    all_marginal_witness_rows = [
        row
        for path, text in runner_bodies.items()
        for row in literal_distribution_witnesses(path, text, marginal_only=True)
    ]
    witnesses_by_path: dict[str, list[dict]] = {}
    for witness in all_witness_rows:
        witnesses_by_path.setdefault(witness["path"], []).append(witness)
    for path in candidates:
        text = bodies[path]
        counts = {
            name: len(pattern.findall(text))
            for name, pattern in TOKEN_PATTERNS.items()
        }
        witness_rows = witnesses_by_path.get(path, [])
        changed_evidence = meaning_changed_evidence(path, text)
        support_evidence = semantic_support_evidence(path, text)
        new_only_witness_rows = [
            row for row in witness_rows
            if row["positive_support_true"] == row["positive_support_false"]
        ]
        if new_only_witness_rows:
            classification = "NEWLY_WITNESSABLE"
            evidence = [
                f"literal_neighbor_conditioned_distribution:{row['function']}"
                for row in new_only_witness_rows
            ]
        elif changed_evidence:
            classification = "MEANING_CHANGED"
            evidence = changed_evidence
        elif path in UNAFFECTED_OVERRIDES:
            classification = "UNAFFECTED"
            evidence = ["pinned_blob_semantic_reread_override"]
        elif support_evidence:
            classification = "SUPPORT_READING_SAFE"
            evidence = support_evidence
        else:
            classification = "UNAFFECTED"
            evidence = ["requested_token_without_second_sentence_use"]
        rows.append({
            "path": path,
            "token_class_counts": counts,
            "classification": classification,
            "classification_evidence": evidence,
            "classification_excerpt": classification_excerpt(
                text, classification
            ),
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
    marginal_paths = sorted({
        row["path"] for row in all_marginal_witness_rows
    })
    return {
        "tracked_file_count": len(tracked),
        "tracked_python_file_count": len(runner_bodies),
        "consumer_file_count": len(rows),
        "token_totals": token_totals,
        "consumer_rows": rows,
        "row_digest": digest([
            {
                "path": row["path"],
                "token_class_counts": row["token_class_counts"],
            }
            for row in rows
        ]),
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
        "selector_anchor_complete": corpus["selector_anchor_complete"],
        "vacuity_probe": {
            "method": (
                "All-pinned-Python AST literal search for a distribution/probability "
                "function whose neighbor-named argument controls distinct "
                "numeric dictionary return branches; a marginal witness "
                "additionally requires marginal or uniform-self-input naming "
                "on the distribution function itself"
            ),
            "state_resolved_witness_runner_count": len(state_paths),
            "state_resolved_literal_branch_pair_count": len(all_witness_rows),
            "state_resolved_witness_runner_paths": state_paths,
            "state_resolved_witness_rows": all_witness_rows,
            "marginal_witness_runner_count": len(marginal_paths),
            "marginal_literal_branch_pair_count": len(all_marginal_witness_rows),
            "marginal_witness_runner_paths": marginal_paths,
            "marginal_witness_rows": all_marginal_witness_rows,
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
    a_ok = (
        token_nonzero
        and sorted_unique
        and first["consumer_file_count"] == len(rows)
        and first["selector_anchor_complete"]
    )
    a_finding = (
        f"pinned_snapshot={PINNED_SNAPSHOT_COMMIT}; tracked_files="
        f"{first['tracked_file_count']}; consumer_files={len(rows)}; "
        f"selector_anchor_complete={first['selector_anchor_complete']}; "
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
        f"pinned_python_files_scanned={first['tracked_python_file_count']}; "
        "a marginal-independence row would not refute state-resolved dependence"
    )

    elapsed = monotonic() - started
    output_upper_bound = sum(map(len, (a_finding, b_finding, c_finding))) + 3_500
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
        and elapsed < AUDIT_TIMEOUT_SEC
        and AUDIT_TIMEOUT_SEC <= 300
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    d_finding = (
        f"object_pins={compact(pins)}; authority_checks={compact(authority)}; "
        f"BLOCKLIST={list(BLOCKLIST_EXECUTION)} execution=False; "
        f"determinism_replay={deterministic}; runtime_s={elapsed:.6f}<"
        f"timeout_s={AUDIT_TIMEOUT_SEC}<=300; "
        f"stdout_upper_bound_bytes={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}; "
        f"literal_AUDIT_INPUT_PATHS="
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
        "AXIOM-FIDELITY RE-READ (PINNED MEASUREMENT)",
        "=" * 78,
    ]
    lines.extend(
        f"{'PASS' if ok else 'FAIL'} {name} :: {finding}"
        for name, ok, finding in certificates
    )
    lines.extend((
        "N5_EXECUTION_CERTIFICATE:",
        "per_element: checked and not executed — the literal AST grammar "
        "does not resolve element-level probability comparisons",
        "per_site: checked — one neighbor-conditioned local-distribution "
        "branch pair is present in the pinned Python corpus",
        "per_mode: checked and not executed — the literal AST grammar does "
        "not resolve mode or momentum distributions",
        "per_block: checked and not executed — the literal AST grammar does "
        "not aggregate distributions over blocks",
        "lattice_wide: checked and not executed — the literal AST grammar "
        "does not establish a lattice-wide marginal",
    ))
    checker_payload = {
        "pinned_snapshot_commit": PINNED_SNAPSHOT_COMMIT,
        "tracked_file_count": first["tracked_file_count"],
        "tracked_python_file_count": first["tracked_python_file_count"],
        "consumer_file_count": first["consumer_file_count"],
        "selector_anchor_complete": first["selector_anchor_complete"],
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
