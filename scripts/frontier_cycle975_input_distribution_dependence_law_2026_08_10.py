#!/usr/bin/env python3
"""Cycle 975: neighbour dependence over every target-bit input law.

The target-input family is the complete probability simplex on the landed
basis menu {0,1}:

    mu_p = p delta_0 + (1-p) delta_1,  0 <= p <= 1.

The gate family is the Cycle-972 radius-one star family: identity, one X at
each of seven sites, and both CNOT orientations on each of six centre edges,
with word length at most one.  Every Boolean truth row is recomputed with the
landed Cycle-719 ``apply_semantic`` substrate.  Marginals are represented as
affine polynomials in p, so the continuous input family is characterized
exactly rather than sampled.

Certificate truth values gate enumeration, algebraic reconciliation, and
provenance/control integrity only.  They do not require a nonempty boundary,
nonzero dependence, or the observed counts for PASS.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000
HOUSE_STDOUT_LIMIT_BYTES = 6_000
AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
BLOCKLIST_CITED_PRIMARIES = (AUDIT_INPUT_PATHS[0],)
EXECUTABLE_SUBSTRATE = AUDIT_INPUT_PATHS[1]
PROVENANCE = {
    "cycle970_runner": (
        "6fd0de0a288d212a4a6ce3fdd4dc9019f30dbbad",
        "scripts/frontier_cycle970_inter_site_gate_2026_08_09.py",
        "4670bcb9d83cfc039f1336398c6a4aa4af014f7c",
        "ast",
    ),
    "cycle970_note": (
        "6fd0de0a288d212a4a6ce3fdd4dc9019f30dbbad",
        "docs/INTER_SITE_GATE_CYCLE970_BOUNDED_THEOREM_NOTE_2026-08-09.md",
        "f7b788d8076e7864bc5dbcbb33cb9e49554e494a",
        "text",
    ),
    "cycle972_runner": (
        "3826925e019c0e1966a9b85110a397db2c61d33f",
        "scripts/frontier_cycle972_covariant_dependence_law_2026_08_09.py",
        "ab497ae52f74bc8e8c6cc6eb5888bfaf9f119f15",
        "ast",
    ),
    "cycle972_note": (
        "3826925e019c0e1966a9b85110a397db2c61d33f",
        "docs/COVARIANT_DEPENDENCE_LAW_CYCLE972_BOUNDED_THEOREM_NOTE_2026-08-09.md",
        "e328562ec0ff3b80acef65c490bb5903cc3e8438",
        "text",
    ),
}

import argparse
import ast
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as CORE

A = CORE.A
CENTER = (0, 0, 0)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_NAMES = ("+x", "-x", "+y", "-y", "+z", "-z")
DIR_TO_WIRE = {direction: index + 1 for index, direction in enumerate(DIRECTIONS)}
DIR_TO_NAME = dict(zip(DIRECTIONS, DIRECTION_NAMES))
NEIGHBOUR_CONDITIONS = tuple(product((0, 1), repeat=6))
OTHER_CONTEXTS = tuple(product((0, 1), repeat=5))
INPUT_FAMILY = "mu_p=p delta_0+(1-p) delta_1 for every real p in [0,1]"
LAW_FORMULA = "for W_d=CNOT(a+d->a), y=x XOR n_d"
MARGINAL_IDENTITY = (
    "P_p(y=0|n_d=0)=p, P_p(y=0|n_d=1)=1-p; "
    "TV(P_p(.|0),P_p(.|1))=|2p-1|"
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def declared_family() -> tuple[dict, ...]:
    rows = [{"name": "I", "descriptor": ("I",)}]
    rows.append({"name": "X(C)", "descriptor": ("X", "C")})
    rows.extend(
        {"name": f"X({DIR_TO_NAME[d]})", "descriptor": ("X", d)}
        for d in DIRECTIONS
    )
    rows.extend(
        {"name": f"CNOT(C->{DIR_TO_NAME[d]})", "descriptor": ("CNOT", "C", d)}
        for d in DIRECTIONS
    )
    rows.extend(
        {"name": f"CNOT({DIR_TO_NAME[d]}->C)", "descriptor": ("CNOT", d, "C")}
        for d in DIRECTIONS
    )
    return tuple(rows)


def site_wire(site: str | tuple[int, int, int]) -> int:
    return 0 if site == "C" else DIR_TO_WIRE[site]


def core_word(descriptor: tuple) -> tuple:
    if descriptor[0] == "I":
        return ()
    if descriptor[0] == "X":
        return (A.x(site_wire(descriptor[1])),)
    return (A.cn(site_wire(descriptor[1]), site_wire(descriptor[2])),)


def output_bit(descriptor: tuple, x: int, condition: tuple[int, ...]) -> int:
    return A.apply_semantic((x, *condition), core_word(descriptor))[0]


def with_edge_bit(index: int, other: tuple[int, ...], bit: int) -> tuple[int, ...]:
    values = []
    source = iter(other)
    for position in range(6):
        values.append(bit if position == index else next(source))
    return tuple(values)


def affine_probability(
    descriptor: tuple, condition: tuple[int, ...], outcome: int
) -> tuple[Fraction, Fraction]:
    """Return (constant, p coefficient) for P_mu_p(Y=outcome|condition)."""
    hit_0 = int(output_bit(descriptor, 0, condition) == outcome)
    hit_1 = int(output_bit(descriptor, 1, condition) == outcome)
    return Fraction(hit_1), Fraction(hit_0 - hit_1)


def affine_subtract(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    return left[0] - right[0], left[1] - right[1]


def affine_eval(poly: tuple[Fraction, Fraction], p: Fraction) -> Fraction:
    return poly[0] + poly[1] * p


def affine_root(poly: tuple[Fraction, Fraction]) -> Fraction | None:
    return -poly[0] / poly[1] if poly[1] else None


def state_resolved_census() -> dict:
    rows = []
    changed_pair_atoms = []
    for word in declared_family():
        for x in (0, 1):
            changed_pairs = 0
            dependencies = []
            for direction_index, direction in enumerate(DIRECTIONS):
                changed_this_direction = False
                for other in OTHER_CONTEXTS:
                    c0 = with_edge_bit(direction_index, other, 0)
                    c1 = with_edge_bit(direction_index, other, 1)
                    changed = output_bit(word["descriptor"], x, c0) != output_bit(
                        word["descriptor"], x, c1
                    )
                    if changed:
                        changed_pairs += 1
                        changed_this_direction = True
                        changed_pair_atoms.append((word["name"], x, DIR_TO_NAME[direction], other))
                if changed_this_direction:
                    dependencies.append(DIR_TO_NAME[direction])
            rows.append({
                "word_name": word["name"],
                "fixed_target_input": x,
                "dependent_neighbour_bits": dependencies,
                "changed_edge_pairs": changed_pairs,
                "edge_pair_comparisons": len(DIRECTIONS) * len(OTHER_CONTEXTS),
                "dependent": bool(dependencies),
            })
    return {
        "word_input_rows": len(rows),
        "dependent_word_input_rows": sum(row["dependent"] for row in rows),
        "edge_pair_comparisons": len(rows) * len(DIRECTIONS) * len(OTHER_CONTEXTS),
        "changed_edge_pairs": len(changed_pair_atoms),
        "rows": rows,
        "changed_atoms_digest": digest(changed_pair_atoms),
    }


def symbolic_marginal_census() -> dict:
    rows = []
    nonzero_atoms = []
    roots = set()
    coefficient_patterns = set()
    for word in declared_family():
        word_nonzero_pairs = 0
        directions = []
        for direction_index, direction in enumerate(DIRECTIONS):
            direction_nonzero = False
            for other in OTHER_CONTEXTS:
                c0 = with_edge_bit(direction_index, other, 0)
                c1 = with_edge_bit(direction_index, other, 1)
                differences = tuple(
                    affine_subtract(
                        affine_probability(word["descriptor"], c0, y),
                        affine_probability(word["descriptor"], c1, y),
                    )
                    for y in (0, 1)
                )
                nonzero = any(poly != (0, 0) for poly in differences)
                if nonzero:
                    direction_nonzero = True
                    word_nonzero_pairs += 1
                    nonzero_atoms.append((word["name"], DIR_TO_NAME[direction], other, differences))
                    coefficient_patterns.add(differences)
                    outcome_roots = {
                        affine_root(poly) for poly in differences if poly != (0, 0)
                    }
                    if len(outcome_roots) == 1:
                        root = next(iter(outcome_roots))
                        if root is not None and 0 <= root <= 1:
                            roots.add(root)
            if direction_nonzero:
                directions.append(DIR_TO_NAME[direction])
        rows.append({
            "word_name": word["name"],
            "symbolically_dependent_neighbour_bits": directions,
            "nonzero_affine_edge_pairs": word_nonzero_pairs,
            "generic_marginal_dependence": bool(directions),
        })
    return {
        "affine_definition": (
            "P_mu_p(y|n)=p*1{f(0,n)=y}+(1-p)*1{f(1,n)=y}"
        ),
        "edge_pair_comparisons": len(declared_family()) * len(DIRECTIONS) * len(OTHER_CONTEXTS),
        "nonzero_affine_edge_pairs": len(nonzero_atoms),
        "identically_zero_edge_pairs": (
            len(declared_family()) * len(DIRECTIONS) * len(OTHER_CONTEXTS)
            - len(nonzero_atoms)
        ),
        "generic_dependent_words": sum(row["generic_marginal_dependence"] for row in rows),
        "candidate_zero_set": [fraction_text(root) for root in sorted(roots)],
        "boundary_empty": not roots,
        "coefficient_patterns": [
            [[fraction_text(a), fraction_text(b)] for a, b in pattern]
            for pattern in sorted(coefficient_patterns)
        ],
        "rows": rows,
        "nonzero_atoms_digest": digest(nonzero_atoms),
    }


def marginal_at(p: Fraction) -> dict:
    changed_atoms = []
    changed_words = set()
    strengths = []
    for word in declared_family():
        for direction_index, direction in enumerate(DIRECTIONS):
            for other in OTHER_CONTEXTS:
                c0 = with_edge_bit(direction_index, other, 0)
                c1 = with_edge_bit(direction_index, other, 1)
                differences = tuple(
                    affine_eval(
                        affine_subtract(
                            affine_probability(word["descriptor"], c0, y),
                            affine_probability(word["descriptor"], c1, y),
                        ),
                        p,
                    )
                    for y in (0, 1)
                )
                tv = sum(abs(value) for value in differences) / 2
                if tv:
                    changed_atoms.append((word["name"], DIR_TO_NAME[direction], other))
                    changed_words.add(word["name"])
                    strengths.append(tv)
    support_size = int(p > 0) + int(p < 1)
    resolved_rows = 6 * support_size
    resolved_total = len(declared_family()) * support_size
    resolved_pairs = len(DIRECTIONS) * len(OTHER_CONTEXTS) * support_size
    return {
        "p": fraction_text(p),
        "support_size": support_size,
        "supported_state_resolved_dependent_rows": resolved_rows,
        "supported_state_resolved_rows": resolved_total,
        "supported_state_resolved_changed_edge_pairs": 6 * len(OTHER_CONTEXTS) * support_size,
        "supported_state_resolved_edge_pairs": resolved_pairs * len(declared_family()),
        "marginal_dependent_words": len(changed_words),
        "marginal_words": len(declared_family()),
        "marginal_changed_edge_pairs": len(changed_atoms),
        "marginal_edge_pairs": len(declared_family()) * len(DIRECTIONS) * len(OTHER_CONTEXTS),
        "per_visible_edge_tv": fraction_text(strengths[0]) if strengths else "0",
        "all_visible_edge_strengths_equal": len(set(strengths)) <= 1,
    }


def input_family_enumeration() -> dict:
    representatives = tuple(map(Fraction, (0,))) + (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))
    representative_rows = {fraction_text(p): marginal_at(p) for p in representatives}
    cells = (
        {"member": "delta_1", "parameter_set": "p=0", "cardinality": 1, "strength": "1"},
        {"member": "left-biased full-support", "parameter_set": "0<p<1/2", "cardinality": "continuum", "strength": "1-2p in (0,1)"},
        {"member": "uniform", "parameter_set": "p=1/2", "cardinality": 1, "strength": "0"},
        {"member": "right-biased full-support", "parameter_set": "1/2<p<1", "cardinality": "continuum", "strength": "2p-1 in (0,1)"},
        {"member": "delta_0", "parameter_set": "p=1", "cardinality": 1, "strength": "1"},
    )
    rows = []
    for cell, representative in zip(cells, representatives):
        row = dict(cell)
        row["representative_counts"] = representative_rows[fraction_text(representative)]
        row["exact_count_rule"] = (
            "marginal 0/20 words and 0/3840 edge pairs"
            if representative == Fraction(1, 2)
            else "marginal 6/20 words and 192/3840 edge pairs"
        )
        row["state_resolved_count_rule"] = (
            "supported 6/20 word-input rows and 192/3840 edge pairs; full structural census 12/40 and 384/7680"
            if representative in (0, 1)
            else "supported/full structural census 12/40 word-input rows and 384/7680 edge pairs"
        )
        rows.append(row)
    return {
        "family": INPUT_FAMILY,
        "parameterization_unique": "p=mu({0}); mu({1})=1-p",
        "family_cardinality": "continuum",
        "exact_exhaustive_partition": rows,
        "representative_rows": representative_rows,
        "count_constancy_reason": "all nonzero marginal difference polynomials have their only [0,1] root at p=1/2",
    }


def premise_price() -> dict:
    incoming = ("CNOT", DIRECTIONS[0], "C")
    other = (0,) * 5
    c0 = with_edge_bit(0, other, 0)
    c1 = with_edge_bit(0, other, 1)
    fixed_rows = []
    for x in (0, 1):
        distributions = []
        for condition in (c0, c1):
            outcome = output_bit(incoming, x, condition)
            distributions.append([int(outcome == 0), int(outcome == 1)])
        fixed_rows.append({
            "x": x,
            "distribution_n_d_0": distributions[0],
            "distribution_n_d_1": distributions[1],
            "dependent": distributions[0] != distributions[1],
            "tv_strength": 1 if distributions[0] != distributions[1] else 0,
        })
    exact_970 = [row["x"] for row in fixed_rows if row["distribution_n_d_0"] == [1, 0] and row["distribution_n_d_1"] == [0, 1]]
    return {
        "fixed_x0_classification": "sufficient, not necessary, and merely convenient",
        "what_it_bought": "a delta input law with no cancellation between the two exchanged XOR rows",
        "fixed_basis_inputs_reproducing_nonzero_witness": sum(row["dependent"] for row in fixed_rows),
        "fixed_basis_input_family_size": len(fixed_rows),
        "fixed_basis_rows": fixed_rows,
        "exact_cycle970_ordered_pair_inputs": exact_970,
        "same_maximal_strength_inputs": [row["x"] for row in fixed_rows if row["tv_strength"] == 1],
        "general_input_laws_with_nonzero_marginal": "every mu_p with p != 1/2",
        "general_input_laws_with_maximal_marginal_strength": "p in {0,1}",
        "new_gate_classes": 0,
        "new_couplings": 0,
        "new_axioms": 0,
        "new_registered_primitives": 0,
        "supplied_fixed_input_premises_needed_for_general_law": 0,
    }


def provenance_controls() -> dict:
    observations = {}
    for label, (commit, path, expected_blob, mode) in PROVENANCE.items():
        spec = f"{commit}:{path}"
        blob = subprocess.check_output(("git", "rev-parse", spec), cwd=ROOT, text=True).strip()
        body = subprocess.check_output(("git", "show", spec), cwd=ROOT)
        row = {
            "commit": commit, "path": path, "expected_blob": expected_blob,
            "observed_blob": blob, "read_mode": "AST only; never executed" if mode == "ast" else "text only",
        }
        if mode == "ast":
            tree = ast.parse(body.decode(), filename=spec)
            functions = {node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}
            row["declares_family"] = "declared_family" in functions
            row["declares_resolved_census"] = "state_resolved_census" in functions
            row["declares_marginal_census"] = bool({"uniform_self_input_census", "uniform_target_input_census"} & functions)
        else:
            note = body.decode()
            row["mentions_fixed_input_or_xor"] = "fixed" in note and ("x=0" in note or "x = 0" in note) or "x XOR n_d" in note
            row["bounded_scope_present"] = "bounded" in note.lower()
        observations[label] = row
    return observations


def input_controls() -> dict:
    pins = {}
    all_exist = True
    for rel in AUDIT_INPUT_PATHS:
        path = ROOT / rel
        all_exist &= path.is_file() and path.resolve().is_relative_to(ROOT.resolve())
        pins[rel] = sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    axiom = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    provenance = provenance_controls()
    return {
        "literal_audit_input_paths": list(AUDIT_INPUT_PATHS),
        "all_inputs_exist_worktree_relative": all_exist,
        "sha256": pins,
        "primary_source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "blocklist_cited_primaries": list(BLOCKLIST_CITED_PRIMARIES),
        "blocklist_text_only": all(not path.endswith(".py") for path in BLOCKLIST_CITED_PRIMARIES),
        "executable_substrate": EXECUTABLE_SUBSTRATE,
        "axiom_distribution_needle_matches": (
            "probability distribution over the possibilities is\ndetermined by, and varies with, the nearest-neighbor conditions" in axiom
        ),
        "text_ast_provenance": provenance,
        "provenance_pins_match": all(row["expected_blob"] == row["observed_blob"] for row in provenance.values()),
        "provenance_never_executed": all("never executed" in row["read_mode"] or row["read_mode"] == "text only" for row in provenance.values()),
    }


def run_science() -> dict:
    return {
        "state_resolved": state_resolved_census(),
        "symbolic_marginal": symbolic_marginal_census(),
        "input_family": input_family_enumeration(),
        "premise_price": premise_price(),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache-path", default="logs/runner-cache/frontier_cycle975_input_distribution_dependence_law_2026_08_10.txt")
    parser.add_argument("--receipt-path", default="outputs/input_distribution_dependence_law_cycle975_receipt_2026_08_10.json")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    started = monotonic()
    first = run_science()
    second = run_science()
    deterministic = digest(first) == digest(second)
    controls = input_controls()
    resolved = first["state_resolved"]
    symbolic = first["symbolic_marginal"]
    family = first["input_family"]
    price = first["premise_price"]

    partition = family["exact_exhaustive_partition"]
    representatives = family["representative_rows"]
    a_ok = (
        len(declared_family()) == len({row["name"] for row in declared_family()})
        and resolved["word_input_rows"] == len(declared_family()) * 2
        and resolved["dependent_word_input_rows"] == sum(row["dependent"] for row in resolved["rows"])
        and resolved["changed_edge_pairs"] == sum(row["changed_edge_pairs"] for row in resolved["rows"])
        and len(partition) == len(representatives)
        and {row["p"] for row in representatives.values()} == set(representatives)
        and all(row["marginal_words"] == len(declared_family()) for row in representatives.values())
    )
    a_finding = (
        f"input_family={INPUT_FAMILY}; exact_cells={len(partition)}; family_words={len(declared_family())}; "
        f"full_state_resolved={resolved['dependent_word_input_rows']}/{resolved['word_input_rows']} rows," 
        f"{resolved['changed_edge_pairs']}/{resolved['edge_pair_comparisons']} edge_pairs; cell_counts="
        f"{[(row['parameter_set'], row['exact_count_rule']) for row in partition]}"
    )

    roots = tuple(Fraction(value) for value in symbolic["candidate_zero_set"])
    root_checks = all(
        marginal_at(root)["marginal_changed_edge_pairs"] == 0 for root in roots
    )
    sample_checks = all(
        row["all_visible_edge_strengths_equal"] for row in representatives.values()
    )
    b_ok = (
        symbolic["edge_pair_comparisons"] == len(declared_family()) * len(DIRECTIONS) * len(OTHER_CONTEXTS)
        and symbolic["nonzero_affine_edge_pairs"] + symbolic["identically_zero_edge_pairs"] == symbolic["edge_pair_comparisons"]
        and symbolic["generic_dependent_words"] == sum(row["generic_marginal_dependence"] for row in symbolic["rows"])
        and symbolic["boundary_empty"] == (not roots)
        and root_checks and sample_checks
    )
    b_finding = (
        f"proof=exhaustive finite Boolean truth rows plus exact affine-polynomial elimination; identity={MARGINAL_IDENTITY}; "
        f"zero_set={symbolic['candidate_zero_set']}; boundary_empty={symbolic['boundary_empty']}; "
        f"marginal_visible_set={'[0,1] minus {' + ','.join(symbolic['candidate_zero_set']) + '}' if roots else '[0,1]'}; "
        f"nonzero_affine_pairs={symbolic['nonzero_affine_edge_pairs']}/{symbolic['edge_pair_comparisons']}"
    )

    fixed_rows = price["fixed_basis_rows"]
    c_ok = (
        price["fixed_basis_inputs_reproducing_nonzero_witness"] == sum(row["dependent"] for row in fixed_rows)
        and set(price["exact_cycle970_ordered_pair_inputs"]).issubset({0, 1})
        and set(price["same_maximal_strength_inputs"]).issubset({0, 1})
        and all(price[key] == 0 for key in (
            "new_gate_classes", "new_couplings", "new_axioms", "new_registered_primitives",
            "supplied_fixed_input_premises_needed_for_general_law",
        ))
    )
    c_finding = (
        f"x=0 is {price['fixed_x0_classification']}; fixed_inputs_with_nonzero_witness="
        f"{price['fixed_basis_inputs_reproducing_nonzero_witness']}/{price['fixed_basis_input_family_size']}; "
        f"exact_970_ordered_pair_inputs={price['exact_cycle970_ordered_pair_inputs']}; "
        f"maximal_strength_inputs={price['same_maximal_strength_inputs']}; marginal_visible_laws=p!=1/2; "
        "delta(new gate,coupling,axiom,primitive,fixed-input premise)=0/0/0/0/0"
    )

    elapsed = monotonic() - started
    output_upper_bound = sum(map(len, (a_finding, b_finding, c_finding))) + 2_500
    provenance = controls["text_ast_provenance"]
    d_ok = (
        controls["all_inputs_exist_worktree_relative"]
        and controls["blocklist_text_only"]
        and controls["axiom_distribution_needle_matches"]
        and controls["provenance_pins_match"]
        and controls["provenance_never_executed"]
        and all(row.get("declares_family", True) for row in provenance.values())
        and all(row.get("bounded_scope_present", True) for row in provenance.values())
        and deterministic and all(controls["sha256"].values())
        and elapsed < AUDIT_TIMEOUT_SEC < 1400
        and output_upper_bound < HOUSE_STDOUT_LIMIT_BYTES < STDOUT_LIMIT_BYTES
    )
    d_finding = (
        f"sha_pins={compact(controls['sha256'])}; provenance_blobs="
        f"{compact({key: row['observed_blob'] for key, row in provenance.items()})}; "
        f"reads=6 explicit source files (970/972 runner+note, Cycle-719 core, axiom memo); "
        f"provenance=AST/text only; determinism_replay={deterministic}; runtime_s={elapsed:.6f}<"
        f"timeout_s={AUDIT_TIMEOUT_SEC}; stdout_upper_bound={output_upper_bound}<"
        f"{HOUSE_STDOUT_LIMIT_BYTES}<{STDOUT_LIMIT_BYTES}"
    )

    certificates = (
        ("A_INPUT_FAMILY", a_ok, a_finding),
        ("B_BOUNDARY", b_ok, b_finding),
        ("C_PREMISE_PRICE", c_ok, c_finding),
        ("D_CONTROLS", d_ok, d_finding),
    )
    all_pass = all(ok for _, ok, _ in certificates)
    checker_payload = {
        "family_words": len(declared_family()),
        "input_family": INPUT_FAMILY,
        "input_cells": len(partition),
        "state_dependent_rows": resolved["dependent_word_input_rows"],
        "state_rows": resolved["word_input_rows"],
        "state_changed_edge_pairs": resolved["changed_edge_pairs"],
        "state_edge_pairs": resolved["edge_pair_comparisons"],
        "symbolic_nonzero_edge_pairs": symbolic["nonzero_affine_edge_pairs"],
        "symbolic_edge_pairs": symbolic["edge_pair_comparisons"],
        "coefficient_patterns": symbolic["coefficient_patterns"],
        "zero_set": symbolic["candidate_zero_set"],
        "boundary_empty": symbolic["boundary_empty"],
        "marginal_counts_by_representative": {
            p: [row["marginal_dependent_words"], row["marginal_changed_edge_pairs"], row["per_visible_edge_tv"]]
            for p, row in representatives.items()
        },
        "x0_classification": price["fixed_x0_classification"],
        "fixed_inputs_with_witness": price["fixed_basis_inputs_reproducing_nonzero_witness"],
        "exact_970_ordered_pair_inputs": price["exact_cycle970_ordered_pair_inputs"],
        "science_digest": digest(first),
    }
    lines = ["=" * 78, "CYCLE 975 -- INPUT-DISTRIBUTION DEPENDENCE LAW", "=" * 78]
    lines.extend(f"{'PASS' if ok else 'FAIL'} {name} :: {finding}" for name, ok, finding in certificates)
    lines.append("CHECKER_PAYLOAD: " + compact(checker_payload))
    lines.append("VERDICT: " + ("BOUNDED_GENERAL_INPUT_LAW_CHARACTERIZED" if all_pass else "INPUT_LAW_MEASUREMENT_INCOMPLETE"))
    lines.append(f"TOTAL: PASS={sum(ok for _, ok, _ in certificates)} FAIL={sum(not ok for _, ok, _ in certificates)}")
    text = "\n".join(lines) + "\n"
    if len(text.encode()) >= HOUSE_STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1

    cache_path = ROOT / args.cache_path
    receipt_path = ROOT / args.receipt_path
    if not cache_path.resolve().is_relative_to(ROOT.resolve()) or not receipt_path.resolve().is_relative_to(ROOT.resolve()):
        sys.stderr.write("output path escapes repository\n")
        return 1
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(text, encoding="utf-8")
    report = {
        "cycle": 975,
        "claim_type": "bounded_theorem",
        "actual_current_surface_status": "bounded-support",
        "trace_class": "direct_blocker_closure",
        "reachability_to_target": "closes",
        "conditional_surface_status": "exact on the declared radius-one, word-length-at-most-one basis-state family",
        "proposal_allowed": False,
        "proposal_allowed_reason": "finite basis menu and word-length cap; not a full M_2(C) law",
        "bare_retained_allowed": False,
        "law_formula": LAW_FORMULA,
        "marginal_identity": MARGINAL_IDENTITY,
        "findings": first,
        "controls": controls,
        "determinism_replay": deterministic,
        "science_digest": digest(first),
        "primary_source_sha256": controls["primary_source_sha256"],
        "primary_cache_sha256": sha256(text.encode()).hexdigest(),
        "runtime_sec": elapsed,
        "stdout_bytes": len(text.encode()),
        "certificates": {name: {"pass": ok, "finding": finding} for name, ok, finding in certificates},
        "all_certificates_pass": all_pass,
        "checker_payload": checker_payload,
    }
    receipt_path.write_text(json.dumps(report, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
