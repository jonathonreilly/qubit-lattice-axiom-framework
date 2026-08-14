#!/usr/bin/env python3
"""Independent, refute-specified checker for the target-input law.

This checker imports neither the primary nor the Cycle-719 core.  It parses
the primary as AST, reconstructs the declared Boolean family directly, and
tries active corruptions of every headline result before accepting the pinned
primary receipt/cache pair.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
PRIMARY_PATH = "scripts/frontier_cycle975_input_distribution_dependence_law_2026_08_10.py"
CORE_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
PRIMARY_RECEIPT_PATH = "outputs/input_distribution_dependence_law_cycle975_receipt_2026_08_10.json"
PRIMARY_CACHE_PATH = "logs/runner-cache/frontier_cycle975_input_distribution_dependence_law_2026_08_10.txt"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle975_input_distribution_dependence_law_2026_08_10.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "outputs/input_distribution_dependence_law_cycle975_receipt_2026_08_10.json",
    "logs/runner-cache/frontier_cycle975_input_distribution_dependence_law_2026_08_10.txt",
)
BLOCKLIST_EXECUTION = (PRIMARY_PATH, CORE_PATH, AXIOM_PATH)
REFUTE_SPEC = (
    {
        "claim": "A_INPUT_FAMILY",
        "target": "complete five-cell partition and dependence counts",
        "falsifier": "any omitted p-cell or independently reconstructed count mismatch",
    },
    {
        "claim": "B_BOUNDARY",
        "target": "zero set {1/2} and TV strength |2p-1|",
        "falsifier": "a second root, a nonzero uniform marginal, or a different affine coefficient pattern",
    },
    {
        "claim": "C_PREMISE_PRICE",
        "target": "x=0 sufficient but unnecessary; both fixed inputs have unit strength",
        "falsifier": "either fixed basis row is independent or only x=0 has unit strength",
    },
    {
        "claim": "D_CONTROLS",
        "target": "source/cache/receipt pins and non-executing AST boundary",
        "falsifier": "any digest mismatch, executable import, missing certificate, or nondeterministic receipt flag",
    },
)

import argparse
import ast
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import runner_cache

DIRECTIONS = ("+x", "-x", "+y", "-y", "+z", "-z")
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))
REPRESENTATIVES = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))
RECORD_NO_ADDITIVITY_NEEDLES = (
    "Finite additivity, a named scalar collection functional `I`, and an assigned\n"
    "value `I(empty)=0` are not Record axiom content.",
    "probability rules beyond the distribution clause",
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest_bytes(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def declared_family() -> tuple[tuple, ...]:
    rows = [("I",)]
    rows.append(("X", "C"))
    rows.extend(("X", direction) for direction in DIRECTIONS)
    rows.extend(("CNOT", "C", direction) for direction in DIRECTIONS)
    rows.extend(("CNOT", direction, "C") for direction in DIRECTIONS)
    return tuple(rows)


def output_bit(descriptor: tuple, x: int, condition: tuple[int, ...]) -> int:
    if descriptor == ("X", "C"):
        return x ^ 1
    if descriptor[0] == "CNOT" and descriptor[2] == "C":
        return x ^ condition[DIRECTIONS.index(descriptor[1])]
    return x


def with_edge_bit(index: int, other: tuple[int, ...], bit: int) -> tuple[int, ...]:
    result = []
    source = iter(other)
    for position in range(6):
        result.append(bit if position == index else next(source))
    return tuple(result)


def affine_probability(
    descriptor: tuple, condition: tuple[int, ...], outcome: int
) -> tuple[Fraction, Fraction]:
    hit_0 = int(output_bit(descriptor, 0, condition) == outcome)
    hit_1 = int(output_bit(descriptor, 1, condition) == outcome)
    return Fraction(hit_1), Fraction(hit_0 - hit_1)


def subtract(left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]):
    return left[0] - right[0], left[1] - right[1]


def evaluate(poly: tuple[Fraction, Fraction], p: Fraction) -> Fraction:
    return poly[0] + poly[1] * p


def independent_reconstruction() -> dict:
    state_rows = state_dependent_rows = state_pairs = state_changed_pairs = 0
    symbolic_pairs = symbolic_nonzero = 0
    coefficient_patterns = set()
    roots = set()
    marginal_by_p = {
        p: {"words": set(), "pairs": 0, "strengths": set()}
        for p in REPRESENTATIVES
    }
    for descriptor in declared_family():
        for x in (0, 1):
            state_rows += 1
            row_changed = False
            for direction_index, _direction in enumerate(DIRECTIONS):
                for other in OTHER_CONTEXTS:
                    state_pairs += 1
                    c0 = with_edge_bit(direction_index, other, 0)
                    c1 = with_edge_bit(direction_index, other, 1)
                    if output_bit(descriptor, x, c0) != output_bit(descriptor, x, c1):
                        row_changed = True
                        state_changed_pairs += 1
            state_dependent_rows += row_changed

        for direction_index, _direction in enumerate(DIRECTIONS):
            for other in OTHER_CONTEXTS:
                symbolic_pairs += 1
                c0 = with_edge_bit(direction_index, other, 0)
                c1 = with_edge_bit(direction_index, other, 1)
                differences = tuple(
                    subtract(
                        affine_probability(descriptor, c0, outcome),
                        affine_probability(descriptor, c1, outcome),
                    )
                    for outcome in (0, 1)
                )
                if any(poly != (0, 0) for poly in differences):
                    symbolic_nonzero += 1
                    coefficient_patterns.add(differences)
                    local_roots = {
                        -constant / slope
                        for constant, slope in differences if slope
                    }
                    roots.update(root for root in local_roots if 0 <= root <= 1)
                for p, row in marginal_by_p.items():
                    deltas = tuple(evaluate(poly, p) for poly in differences)
                    strength = sum(abs(delta) for delta in deltas) / 2
                    if strength:
                        row["words"].add(descriptor)
                        row["pairs"] += 1
                        row["strengths"].add(strength)
    marginal_counts = {}
    for p, row in marginal_by_p.items():
        strengths = row["strengths"]
        marginal_counts[fraction_text(p)] = [
            len(row["words"]), row["pairs"],
            fraction_text(next(iter(strengths))) if strengths else "0",
        ]
    patterns = [
        [[fraction_text(a), fraction_text(b)] for a, b in pattern]
        for pattern in sorted(coefficient_patterns)
    ]
    return {
        "family_words": len(declared_family()),
        "input_family": "mu_p=p delta_0+(1-p) delta_1 for every real p in [0,1]",
        "input_cells": 5,
        "input_cell_definitions": ["p=0", "0<p<1/2", "p=1/2", "1/2<p<1", "p=1"],
        "state_dependent_rows": state_dependent_rows,
        "state_rows": state_rows,
        "state_changed_edge_pairs": state_changed_pairs,
        "state_edge_pairs": state_pairs,
        "symbolic_nonzero_edge_pairs": symbolic_nonzero,
        "symbolic_edge_pairs": symbolic_pairs,
        "coefficient_patterns": patterns,
        "zero_set": [fraction_text(root) for root in sorted(roots)],
        "boundary_empty": not roots,
        "marginal_counts_by_representative": marginal_counts,
        "x0_classification": "sufficient, not necessary, and merely convenient",
        "fixed_inputs_with_witness": sum(
            output_bit(("CNOT", "+x", "C"), x, (0, 0, 0, 0, 0, 0))
            != output_bit(("CNOT", "+x", "C"), x, (1, 0, 0, 0, 0, 0))
            for x in (0, 1)
        ),
        "exact_970_ordered_pair_inputs": [
            x for x in (0, 1)
            if output_bit(("CNOT", "+x", "C"), x, (0, 0, 0, 0, 0, 0)) == 0
            and output_bit(("CNOT", "+x", "C"), x, (1, 0, 0, 0, 0, 0)) == 1
        ],
    }


def parse_primary_ast(path: Path) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports = []
    function_names = set()
    string_literals = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.FunctionDef):
            function_names.add(node.name)
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            string_literals.add(node.value)
    return {
        "imports": sorted(imports),
        "functions": sorted(function_names),
        "has_required_certificates": all(
            name in string_literals
            for name in ("A_INPUT_FAMILY", "B_BOUNDARY", "C_PREMISE_PRICE", "D_CONTROLS")
        ),
        "imports_cycle719_substrate": any("frontier_cycle719_two_rail" in name for name in imports),
        "imports_provenance_runner": any("cycle970" in name or "cycle972" in name for name in imports),
    }


def parse_cache_payload(cache: str) -> dict | None:
    prefix = "CHECKER_PAYLOAD: "
    matches = [line[len(prefix):] for line in cache.splitlines() if line.startswith(prefix)]
    return json.loads(matches[0]) if len(matches) == 1 else None


def canonical_cache_stdout(cache: str) -> str | None:
    stdout_marker = "----- stdout -----\n"
    stderr_marker = "\n----- stderr -----"
    if stdout_marker not in cache or stderr_marker not in cache:
        return None
    return cache.split(stdout_marker, 1)[1].split(stderr_marker, 1)[0]


def input_pins_survive(controls: dict, current_pins: dict[str, str]) -> bool:
    declared = controls.get("literal_audit_input_paths", [])
    recorded = controls.get("sha256", {})
    return (
        set(declared) == set(recorded) == set(current_pins)
        and all(recorded[path] == current_pins[path] for path in declared)
    )


def payload_survives(candidate: dict, expected: dict) -> bool:
    tested_keys = set(expected)
    return tested_keys.issubset(candidate) and all(candidate[key] == expected[key] for key in tested_keys)


def active_corruption_probes(
    primary_payload: dict, expected: dict, controls: dict, current_pins: dict[str, str]
) -> dict:
    mutations = {}
    candidate = deepcopy(primary_payload)
    candidate["zero_set"] = []
    candidate["boundary_empty"] = True
    mutations["erase_boundary"] = payload_survives(candidate, expected)

    candidate = deepcopy(primary_payload)
    candidate["coefficient_patterns"] = [[[
        "0", "0"
    ], ["0", "0"]]]
    mutations["erase_affine_signal"] = payload_survives(candidate, expected)

    candidate = deepcopy(primary_payload)
    candidate["marginal_counts_by_representative"]["1/2"] = [6, 192, "1"]
    mutations["make_uniform_visible"] = payload_survives(candidate, expected)

    candidate = deepcopy(primary_payload)
    candidate["x0_classification"] = "necessary"
    mutations["make_x0_necessary"] = payload_survives(candidate, expected)

    candidate = deepcopy(primary_payload)
    candidate["symbolic_nonzero_edge_pairs"] += 1
    mutations["corrupt_count"] = payload_survives(candidate, expected)

    candidate = deepcopy(primary_payload)
    candidate["input_cell_definitions"][3] = "0<p<1/2"
    mutations["duplicate_and_omit_input_cell"] = payload_survives(candidate, expected)

    stale_controls = deepcopy(controls)
    stale_path = next(iter(current_pins))
    stale_controls["sha256"][stale_path] = "0" * 64
    mutations["stale_declared_input_digest"] = input_pins_survive(stale_controls, current_pins)
    return {
        "probe_count": len(mutations),
        "false_acceptances": sum(mutations.values()),
        "mutations": mutations,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary-receipt", default=PRIMARY_RECEIPT_PATH)
    parser.add_argument("--primary-cache", default=PRIMARY_CACHE_PATH)
    parser.add_argument("--receipt-path", default="outputs/input_distribution_dependence_law_cycle975_independent_check_receipt_2026_08_10.json")
    return parser.parse_args()


def safe_repo_path(relative: str) -> Path:
    path = ROOT / relative
    if not path.resolve().is_relative_to(ROOT.resolve()):
        raise ValueError(f"path escapes repository: {relative}")
    return path


def main() -> int:
    args = parse_args()
    started = monotonic()
    primary_path = safe_repo_path(PRIMARY_PATH)
    receipt_path = safe_repo_path(args.primary_receipt)
    primary_cache_path = safe_repo_path(args.primary_cache)
    checker_receipt_path = safe_repo_path(args.receipt_path)
    ast_report = parse_primary_ast(primary_path)
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    primary_cache = primary_cache_path.read_text(encoding="utf-8")
    cache_header = runner_cache.parse_cache_header(primary_cache)
    cache_stdout = canonical_cache_stdout(primary_cache)
    cache_payload = parse_cache_payload(cache_stdout) if cache_stdout is not None else None
    expected = independent_reconstruction()
    primary_payload = receipt.get("checker_payload", {})
    receipt_controls = receipt.get("controls", {})
    axiom_text = safe_repo_path(AXIOM_PATH).read_text(encoding="utf-8")
    record_no_additivity_boundary = all(
        needle in axiom_text for needle in RECORD_NO_ADDITIVITY_NEEDLES
    )
    current_input_pins = {
        rel: digest_bytes(safe_repo_path(rel))
        for rel in receipt_controls.get("literal_audit_input_paths", [])
    }
    probes = active_corruption_probes(
        primary_payload, expected, receipt_controls, current_input_pins
    )

    r0_ok = (
        ast_report["has_required_certificates"]
        and ast_report["imports_cycle719_substrate"]
        and not ast_report["imports_provenance_runner"]
        and all(path.endswith(".py") or path.endswith(".md") for path in BLOCKLIST_EXECUTION)
    )
    r0_finding = (
        f"primary_read=AST_only; checker_imports_primary_or_core=False; blocklist={list(BLOCKLIST_EXECUTION)}; "
        f"primary_imports_cycle719={ast_report['imports_cycle719_substrate']}; primary_imports_provenance={ast_report['imports_provenance_runner']}"
    )

    family_keys = (
        "family_words", "input_family", "input_cells", "input_cell_definitions", "state_dependent_rows",
        "state_rows", "state_changed_edge_pairs", "state_edge_pairs",
    )
    r1_ok = all(primary_payload.get(key) == expected[key] for key in family_keys)
    r1_finding = (
        f"family={expected['family_words']} words; input_cells={expected['input_cells']}; "
        f"state_resolved={expected['state_dependent_rows']}/{expected['state_rows']} rows,"
        f"{expected['state_changed_edge_pairs']}/{expected['state_edge_pairs']} edge_pairs"
    )

    boundary_keys = (
        "symbolic_nonzero_edge_pairs", "symbolic_edge_pairs", "coefficient_patterns",
        "zero_set", "boundary_empty", "marginal_counts_by_representative",
    )
    r2_ok = all(primary_payload.get(key) == expected[key] for key in boundary_keys)
    r2_finding = (
        f"independent_affine_patterns={expected['coefficient_patterns']}; zero_set={expected['zero_set']}; "
        f"boundary_empty={expected['boundary_empty']}; representative_counts={compact(expected['marginal_counts_by_representative'])}"
    )

    premise_keys = ("x0_classification", "fixed_inputs_with_witness", "exact_970_ordered_pair_inputs")
    r3_ok = all(primary_payload.get(key) == expected[key] for key in premise_keys)
    r3_finding = (
        f"x0={expected['x0_classification']}; fixed_inputs_with_witness={expected['fixed_inputs_with_witness']}/2; "
        f"exact_ordered_pair={expected['exact_970_ordered_pair_inputs']}"
    )

    r4_ok = probes["probe_count"] >= len(REFUTE_SPEC) and probes["false_acceptances"] == 0
    r4_finding = f"active_corruptions={probes['probe_count']}; false_acceptances={probes['false_acceptances']}; mutations={compact(probes['mutations'])}"

    source_sha = digest_bytes(primary_path)
    cache_sha = sha256(primary_cache.encode()).hexdigest()
    input_pins_match = input_pins_survive(receipt_controls, current_input_pins)
    primary_cache_fresh = runner_cache.cache_identity_status(PRIMARY_PATH) == "fresh"
    receipt_certificates = receipt.get("certificates", {})
    elapsed = monotonic() - started
    r5_ok = (
        receipt.get("primary_source_sha256") == source_sha
        and cache_header is not None
        and cache_header.get("runner_path") == PRIMARY_PATH
        and cache_header.get("runner_sha256") == source_sha
        and primary_cache_fresh
        and input_pins_match
        and record_no_additivity_boundary
        and receipt_controls.get("record_no_additivity_boundary_matches") is True
        and cache_payload == primary_payload
        and receipt.get("all_certificates_pass")
        and all(receipt_certificates.get(name, {}).get("pass") for name in (
            "A_INPUT_FAMILY", "B_BOUNDARY", "C_PREMISE_PRICE", "D_CONTROLS"
        ))
        and receipt.get("determinism_replay")
        and "VERDICT: BOUNDED_GENERAL_INPUT_LAW_CHARACTERIZED" in primary_cache
        and elapsed < AUDIT_TIMEOUT_SEC < 1400
    )
    r5_finding = (
        f"source_sha_match={receipt.get('primary_source_sha256') == source_sha}; canonical_cache_fresh="
        f"{primary_cache_fresh}; cache_payload_match={cache_payload == primary_payload}; live_input_pins_match="
        f"{input_pins_match}; Record_no_additivity_boundary={record_no_additivity_boundary}; "
        f"primary_certificates={len(receipt_certificates)}; "
        f"determinism={receipt.get('determinism_replay')}; runtime_s={elapsed:.6f}"
    )

    certificates = (
        ("R0_PINS_BLOCKLIST_AND_AST", r0_ok, r0_finding),
        ("R1_REFUTE_INPUT_FAMILY", r1_ok, r1_finding),
        ("R2_REFUTE_BOUNDARY_AND_STRENGTH", r2_ok, r2_finding),
        ("R3_REFUTE_PREMISE_PRICE", r3_ok, r3_finding),
        ("R4_ACTIVE_CORRUPTION_PROBES", r4_ok, r4_finding),
        ("R5_CONTROLS", r5_ok, r5_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    checker_payload = {
        "independent_expected": expected,
        "primary_payload_matches": payload_survives(primary_payload, expected),
        "active_corruption_probes": probes,
        "primary_source_sha256": source_sha,
        "primary_cache_sha256": cache_sha,
        "refute_spec_count": len(REFUTE_SPEC),
    }
    lines = ["=" * 78, "INDEPENDENT INPUT-LAW REFUTATION", "=" * 78]
    lines.extend(f"{'PASS' if ok else 'FAIL'} {name} :: {finding}" for name, ok, finding in certificates)
    lines.append("CHECKER_PAYLOAD: " + compact(checker_payload))
    lines.append("VERDICT: " + ("PRIMARY_SURVIVES_INDEPENDENT_REFUTATION_ATTEMPT" if all_pass else "PRIMARY_REFUTED_OR_UNVERIFIED"))
    lines.extend((
        "per_element: checked and executed -- the independent Boolean reconstruction enumerated both target inputs and outcomes",
        "per_site: checked and executed -- all six target-neighbour directions on the declared star were enumerated",
        "per_mode: checked and not executed -- no Fourier or mode decomposition belongs to the reviewed claim",
        "per_block: checked and executed -- every independent word/input/neighbour/spectator block was enumerated",
        "lattice_wide: checked and not executed -- the checker refutes only the declared target-centred-star theorem",
    ))
    lines.append(f"TOTAL: PASS={sum(ok for _, ok, _ in certificates)} FAIL={sum(not ok for _, ok, _ in certificates)}")
    text = "\n".join(lines) + "\n"
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    checker_receipt_path.parent.mkdir(parents=True, exist_ok=True)
    checker_receipt = {
        "artifact": "input_distribution_dependence_law_independent_refutation",
        "checker_type": "independent_refutation_attempt",
        "imports_primary": False,
        "imports_core": False,
        "primary_read_mode": "AST only; never executed",
        "blocklist_execution": list(BLOCKLIST_EXECUTION),
        "refute_spec": list(REFUTE_SPEC),
        "checker_payload": checker_payload,
        "runtime_sec": elapsed,
        "stdout_bytes": len(text.encode()),
        "checker_source_sha256": digest_bytes(Path(__file__)),
        "certificates": {name: {"pass": ok, "finding": finding} for name, ok, finding in certificates},
        "all_certificates_pass": all_pass,
    }
    checker_receipt_path.write_text(json.dumps(checker_receipt, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
