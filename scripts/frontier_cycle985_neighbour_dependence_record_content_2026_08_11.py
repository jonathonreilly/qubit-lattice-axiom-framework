#!/usr/bin/env python3
"""Cycle 985: locked-content and readout census for three neighbour classes.

The finite calculation is conditional on a record forming at the target.  It
reconstructs the three basis-state target laws directly, enumerates their
locked contents, and tests the complete additive scalar readout family on the
binary content alphabet.  Checks gate construction and reconciliation only:
the same visibility validator accepts a coherent no-separator outcome.
"""

from __future__ import annotations

import ast
import json
import subprocess
import sys
from hashlib import sha1, sha256
from itertools import permutations, product
from pathlib import Path
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
CYCLE = 985
AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 6_000
BASE_ORIGIN_MAIN_COMMIT = "ea0968c71ad46c39c6dacb39f88a18780363b71f"
AUDIT_INPUT_PATHS = ("docs/MINIMAL_AXIOMS_2026-06-29.md",)
EXPECTED_INPUT_SHA256 = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "53175250f0458168330160ad6a39c8ec708316f338efd69c49e8eb09e3267b39",
}
EXPECTED_INPUT_BLOBS = {
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "2f5fdd26898f62c17fcabc846761f7785c2eadb1",
}
BLOCKLIST_AST_FRAGMENTS = (
    "cycle977", "cycle980", "cycle982", "cycle983", "cycle984",
)
PRIMARY_PATH = (
    "scripts/frontier_cycle985_neighbour_dependence_record_content_2026_08_11.py"
)
RECEIPT_PATH = (
    "outputs/neighbour_dependence_record_content_cycle985_receipt_2026_08_11.json"
)

DIRECTIONS = {
    "+x": (1, 0, 0),
    "-x": (-1, 0, 0),
    "+y": (0, 1, 0),
    "-y": (0, -1, 0),
    "+z": (0, 0, 1),
    "-z": (0, 0, -1),
}
CLASS_SPECS = (
    {
        "class": "incoming CNOT",
        "representative": "CNOT(+x->C)",
        "kind": "CNOT",
        "controls": ("+x",),
    },
    {
        "class": "perpendicular-control TOF",
        "representative": "TOF(+x,+y->C)",
        "kind": "TOF",
        "controls": ("+x", "+y"),
    },
    {
        "class": "opposite-control TOF",
        "representative": "TOF(+x,-x->C)",
        "kind": "TOF",
        "controls": ("+x", "-x"),
    },
)
CONTENT_EMBEDDING = {
    0: ((1, 0), (0, 0)),
    1: ((0, 0), (0, 1)),
}
READOUT_BASIS = (
    {"name": "I_zero", "singleton_values": (1, 0)},
    {"name": "I_one", "singleton_values": (0, 1)},
)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def ast_literal_assignment(tree: ast.Module, name: str):
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def vector_sum_squared(control_names: tuple[str, ...]) -> int:
    total = tuple(
        sum(DIRECTIONS[name][axis] for name in control_names)
        for axis in range(3)
    )
    return sum(component * component for component in total)


def determinant(matrix: tuple[tuple[int, int, int], ...]) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple:
    rotations = set()
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * int(column == order[row]) for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                rotations.add(matrix)
    return tuple(sorted(rotations))


ROTATIONS = proper_cubic_rotations()


def rotate_vector(matrix: tuple, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(row[column] * vector[column] for column in range(3))
        for row in matrix
    )


def orbit_certificate(control_names: tuple[str, ...]) -> dict:
    controls = tuple(DIRECTIONS[name] for name in control_names)
    unordered = len(controls) == 2
    canonical = tuple(sorted(controls)) if unordered else controls
    images = {
        tuple(sorted(rotate_vector(rotation, vector) for vector in controls))
        if unordered else tuple(rotate_vector(rotation, vector) for vector in controls)
        for rotation in ROTATIONS
    }
    stabilizer = sum(
        (
            tuple(sorted(rotate_vector(rotation, vector) for vector in controls))
            if unordered else tuple(rotate_vector(rotation, vector) for vector in controls)
        ) == canonical
        for rotation in ROTATIONS
    )
    return {
        "group_order": len(ROTATIONS),
        "orbit_size": len(images),
        "stabilizer": stabilizer,
        "orbit_stabilizer_product": len(images) * stabilizer,
        "orbit_digest": digest(sorted(images)),
    }


def locked_content(kind: str, target_input: int, control_bits: tuple[int, ...]) -> int:
    if kind == "CNOT":
        trigger = control_bits[0]
    elif kind == "TOF":
        trigger = int(all(control_bits))
    else:
        raise ValueError(kind)
    return target_input ^ trigger


def class_content_table(spec: dict) -> dict:
    rows = []
    for control_bits in product((0, 1), repeat=len(spec["controls"])):
        output_bits = {
            str(target_input): locked_content(spec["kind"], target_input, control_bits)
            for target_input in (0, 1)
        }
        rows.append({
            "control_configuration": {
                name: bit for name, bit in zip(spec["controls"], control_bits)
            },
            "output_bit_by_target_input": output_bits,
            "locked_content_by_target_input": output_bits,
            "locked_possibility_by_target_input": {
                target_input: f"P_{output_bit}"
                for target_input, output_bit in output_bits.items()
            },
            "point_mass_distribution_by_target_input": {
                target_input: {
                    "P_0": int(output_bit == 0),
                    "P_1": int(output_bit == 1),
                }
                for target_input, output_bit in output_bits.items()
            },
            "spectator_neighbours": "arbitrary",
        })

    hamming_edges = []
    for target_input in (0, 1):
        configurations = tuple(product((0, 1), repeat=len(spec["controls"])))
        for left_index, left in enumerate(configurations):
            for right in configurations[left_index + 1:]:
                hamming = sum(a != b for a, b in zip(left, right))
                if hamming != 1:
                    continue
                content_left = locked_content(spec["kind"], target_input, left)
                content_right = locked_content(spec["kind"], target_input, right)
                hamming_edges.append({
                    "target_input": target_input,
                    "configuration_before": {
                        name: bit for name, bit in zip(spec["controls"], left)
                    },
                    "configuration_after": {
                        name: bit for name, bit in zip(spec["controls"], right)
                    },
                    "content_before": content_left,
                    "content_after": content_right,
                    "changes_locked_content": content_left != content_right,
                })
    orbit = orbit_certificate(spec["controls"])
    return {
        "class": spec["class"],
        "representative": spec["representative"],
        "induced_target_law": (
            "y=x XOR n_(+x)" if spec["kind"] == "CNOT"
            else "y=x XOR (n_1 AND n_2)"
        ),
        "controls": list(spec["controls"]),
        **orbit,
        "J": vector_sum_squared(spec["controls"]),
        "table": rows,
        "one_neighbour_bit_edges": hamming_edges,
        "one_neighbour_bit_separations": [
            edge for edge in hamming_edges if edge["changes_locked_content"]
        ],
    }


def locked_content_census() -> dict:
    classes = [class_content_table(spec) for spec in CLASS_SPECS]
    return {
        "condition": "conditional on a record forming at the target site",
        "content_alphabet": [0, 1],
        "M2C_possibility_embedding": {
            f"P_{bit}": [list(row) for row in matrix]
            for bit, matrix in CONTENT_EMBEDDING.items()
        },
        "distribution_construction": (
            "for each fixed target input and representative law, mu(P_y|n)=1 "
            "and mu(P_(1-y)|n)=0; Record locks the unique supported P_y"
        ),
        "target_input_role": (
            "fixed supplied parameter for each finite conditioned law, not an "
            "additional varying neighbour coordinate"
        ),
        "spectator_neighbours": "arbitrary in every displayed row",
        "classes": classes,
        "class_count": len(classes),
        "witness_multiplicity": sum(row["orbit_size"] for row in classes),
        "J_values_by_class": {row["class"]: row["J"] for row in classes},
        "proper_cubic_group_order": len(ROTATIONS),
        "point_mass_normalization_failures": sum(
            sum(distribution.values()) != 1
            for row in classes for table_row in row["table"]
            for distribution in table_row["point_mass_distribution_by_target_input"].values()
        ),
        "locked_content_support_failures": sum(
            distribution[f"P_{content}"] != 1
            for row in classes for table_row in row["table"]
            for target_input, distribution in table_row[
                "point_mass_distribution_by_target_input"
            ].items()
            for content in [table_row["locked_content_by_target_input"][target_input]]
        ),
    }


def finite_additive_readout(contents: tuple[int, ...], weights: tuple[int, int]) -> int:
    return sum(weights[content] for content in contents)


def analyse_visibility(content_pairs: list[dict], basis: tuple[dict, ...]) -> dict:
    pair_rows = []
    for pair in content_pairs:
        values = []
        for readout in basis:
            weights = tuple(readout["singleton_values"])
            before = finite_additive_readout((pair["content_before"],), weights)
            after = finite_additive_readout((pair["content_after"],), weights)
            values.append({
                "readout": readout["name"],
                "before": before,
                "after": after,
                "delta": after - before,
            })
        pair_rows.append({**pair, "basis_readout_values": values})

    visible = [
        row for row in pair_rows
        if any(value["delta"] != 0 for value in row["basis_readout_values"])
    ]
    if pair_rows and len(visible) == len(pair_rows):
        outcome = "SEPARATING_ADMISSIBLE_READOUT_EXISTS"
        proof = None
    elif pair_rows and not visible:
        outcome = "DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS"
        proof = {
            "basis_dimension": len(basis),
            "all_basis_functionals_equal_on_all_compared_pairs": all(
                all(value["delta"] == 0 for value in row["basis_readout_values"])
                for row in pair_rows
            ),
            "span_argument": (
                "every declared readout is a real linear combination of the basis; "
                "basis equality therefore implies family-wide equality"
            ),
        }
    elif pair_rows:
        outcome = "PARTIAL_VISIBILITY_IN_DECLARED_READOUT_FAMILY"
        proof = None
    else:
        outcome = "EMPTY_COMPARISON_DOMAIN"
        proof = None
    return {
        "outcome": outcome,
        "pair_count": len(pair_rows),
        "visible_pair_count": len(visible),
        "pairs": pair_rows,
        "nonseparation_proof": proof,
    }


def readout_visibility(census: dict) -> dict:
    content_pairs = [
        {"class": row["class"], **pair}
        for row in census["classes"]
        for pair in row["one_neighbour_bit_separations"]
    ]
    analysis = analyse_visibility(content_pairs, READOUT_BASIS)

    additivity_failures = 0
    for weights in (tuple(row["singleton_values"]) for row in READOUT_BASIS):
        for left_size in range(4):
            for right_size in range(4):
                for left in product((0, 1), repeat=left_size):
                    for right in product((0, 1), repeat=right_size):
                        additivity_failures += (
                            finite_additive_readout(left + right, weights)
                            != finite_additive_readout(left, weights)
                            + finite_additive_readout(right, weights)
                        )

    i_one_rows = []
    for pair in content_pairs:
        before = finite_additive_readout((pair["content_before"],), (0, 1))
        after = finite_additive_readout((pair["content_after"],), (0, 1))
        i_one_rows.append({
            "class": pair["class"],
            "target_input": pair["target_input"],
            "I_one_before": before,
            "I_one_after": after,
            "delta": after - before,
        })

    exact_separator = None
    if analysis["outcome"] == "SEPARATING_ADMISSIBLE_READOUT_EXISTS":
        exact_separator = {
            "name": "I_one",
            "singleton_rule": "I_one({record with content c})=c",
            "collection_rule": "I_one(R)=number of records in R whose content is 1",
            "values_on_separated_pairs": i_one_rows,
            "separates_every_declared_pair": all(
                row["delta"] != 0 for row in i_one_rows
            ),
        }

    return {
        "declared_family": (
            "all functions phi:{0,1}->R, extended to finite pairwise-disjoint "
            "record collections by I_phi(R)=sum_{r in R} phi(content(r))"
        ),
        "basis": list(READOUT_BASIS),
        "empty_value": finite_additive_readout((), (0, 1)),
        "record_content_only": True,
        "additivity_checks": 2 * sum(
            (2 ** left_size) * (2 ** right_size)
            for left_size in range(4) for right_size in range(4)
        ),
        "additivity_failure_count": additivity_failures,
        "analysis": analysis,
        "exact_separator": exact_separator,
        "blind_admissible_example": {
            "singleton_values": [1, 1],
            "meaning": "record count; admissible but content-blind on equal-size collections",
        },
        "selection_boundary": (
            "the Record axiom permits this separating readout but does not select it "
            "or require every admissible readout to separate the contents"
        ),
    }


def scope_measurement() -> dict:
    return {
        "tested": (
            "one forming target record at a time on the binary radius-one true-Z3 "
            "star, for the three finite deterministic witness classes"
        ),
        "established": (
            "in the declared P0/P1 point-mass construction, the exact changing "
            "neighbour edges change the unique supported locked content and I_one reads it"
        ),
        "binary_M2C_embedding_declared_not_unique": True,
        "point_mass_distribution_constructed_at_finite_cap": True,
        "target_input_fixed_per_conditioned_law": True,
        "full_mosaic_claimed": False,
        "formation_site_probability_or_rate_claimed": False,
        "selected_physical_readout_claimed": False,
        "born_weight_selection_claimed": False,
        "continuous_M2_probability_law_claimed": False,
        "infinite_simultaneous_translation_uniform_law_claimed": False,
        "generic_axiom_only_consequence_claimed": False,
        "generic_axiom_boundary": (
            "distribution variation alone need not force disjoint supports or a different "
            "realized draw; the positive result uses the declared P0/P1 point-mass laws"
        ),
    }


def validate_visibility_payload(payload: dict) -> bool:
    analysis = payload["analysis"]
    recomputed = analyse_visibility(analysis["pairs"], tuple(payload["basis"]))
    return recomputed == analysis


def validate_readout_measurement(payload: dict) -> bool:
    if not validate_visibility_payload(payload):
        return False
    analysis = payload["analysis"]
    if payload["empty_value"] != 0 or not payload["record_content_only"]:
        return False
    if payload["additivity_failure_count"] != 0:
        return False
    if analysis["outcome"] == "SEPARATING_ADMISSIBLE_READOUT_EXISTS":
        separator = payload["exact_separator"]
        expected_values = []
        for pair in analysis["pairs"]:
            before = finite_additive_readout((pair["content_before"],), (0, 1))
            after = finite_additive_readout((pair["content_after"],), (0, 1))
            expected_values.append({
                "class": pair["class"],
                "target_input": pair["target_input"],
                "I_one_before": before,
                "I_one_after": after,
                "delta": after - before,
            })
        return bool(
            separator
            and separator["name"] == "I_one"
            and separator["values_on_separated_pairs"] == expected_values
            and separator["separates_every_declared_pair"]
            == all(row["delta"] != 0 for row in expected_values)
        )
    if analysis["outcome"] == "DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS":
        proof = analysis["nonseparation_proof"]
        return bool(
            payload["exact_separator"] is None
            and proof
            and proof["all_basis_functionals_equal_on_all_compared_pairs"] is True
        )
    return payload["exact_separator"] is None


def synthetic_agreement_visibility_control() -> bool:
    pairs = [{
        "class": "synthetic equal-content fixture",
        "target_input": 0,
        "configuration_before": {"n": 0},
        "configuration_after": {"n": 1},
        "content_before": 0,
        "content_after": 0,
    }]
    analysis = analyse_visibility(pairs, READOUT_BASIS)
    payload = {
        "basis": list(READOUT_BASIS),
        "analysis": analysis,
        "empty_value": 0,
        "record_content_only": True,
        "additivity_failure_count": 0,
        "exact_separator": None,
    }
    return bool(
        analysis["outcome"] == "DECLARED_READOUT_FAMILY_AGREES_ON_ALL_COMPARED_PAIRS"
        and validate_readout_measurement(payload)
    )


def input_controls() -> dict:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    input_paths = ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
    fragments = ast_literal_assignment(tree, "BLOCKLIST_AST_FRAGMENTS")
    payloads = {path: (ROOT / path).read_bytes() for path in input_paths}
    sha_rows = {path: sha256(payload).hexdigest() for path, payload in payloads.items()}
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    imported_names = {
        alias.name for node in ast.walk(tree) if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    base_is_ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", BASE_ORIGIN_MAIN_COMMIT, "HEAD"],
        cwd=ROOT, check=False, capture_output=True,
    ).returncode == 0
    return {
        "literal_audit_input_paths": list(input_paths),
        "literal_source_read_count": len(input_paths),
        "input_sha256": sha_rows,
        "input_git_blobs": blob_rows,
        "sha_pins_match": sha_rows == EXPECTED_INPUT_SHA256,
        "blob_pins_match": blob_rows == EXPECTED_INPUT_BLOBS,
        "all_inputs_relative_and_present": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in input_paths
        ),
        "blocked_ast_imports": sorted(
            name for name in imported_names
            if any(fragment in name.lower() for fragment in fragments)
        ),
        "prior_cycle_modules_loaded": False,
        "base_origin_main_commit": BASE_ORIGIN_MAIN_COMMIT,
        "base_is_ancestor_of_head": base_is_ancestor,
    }


def science_measurement() -> dict:
    census = locked_content_census()
    return {
        "A_LOCKED_CONTENT_CENSUS": census,
        "B_READOUT_VISIBILITY": readout_visibility(census),
        "C_SCOPE": scope_measurement(),
    }


def render_stdout(receipt: dict) -> str:
    findings = receipt["findings"]
    census = findings["A_LOCKED_CONTENT_CENSUS"]
    visibility = findings["B_READOUT_VISIBILITY"]
    scope = findings["C_SCOPE"]
    class_rows = [
        [row["class"], row["orbit_size"], row["J"], len(row["table"])]
        for row in census["classes"]
    ]
    lines = [
        "CYCLE985_NEIGHBOUR_DEPENDENCE_RECORD_CONTENT",
        "A_LOCKED_CONTENT_CENSUS "
        + ("PASS" if receipt["checks"]["A_LOCKED_CONTENT_CENSUS"] else "FAIL")
        + f" :: classes={compact(class_rows)}; witnesses={census['witness_multiplicity']};"
        + f" separated_pairs={sum(len(row['one_neighbour_bit_separations']) for row in census['classes'])}",
        "B_READOUT_VISIBILITY "
        + ("PASS" if receipt["checks"]["B_READOUT_VISIBILITY"] else "FAIL")
        + f" :: outcome={visibility['analysis']['outcome']};"
        + f" readout=I_one; visible={visibility['analysis']['visible_pair_count']}/{visibility['analysis']['pair_count']}",
        "C_SCOPE " + ("PASS" if receipt["checks"]["C_SCOPE"] else "FAIL")
        + f" :: single_site={not scope['full_mosaic_claimed']};"
        + f" full_mosaic_claimed={scope['full_mosaic_claimed']};"
        + f" selected_readout_claimed={scope['selected_physical_readout_claimed']}",
        "D_CONTROLS " + ("PASS" if receipt["checks"]["D_CONTROLS"] else "FAIL")
        + f" :: source_reads={receipt['controls']['literal_source_read_count']}<=6;"
        + f" pins={receipt['controls']['sha_pins_match'] and receipt['controls']['blob_pins_match']};"
        + f" deterministic={receipt['controls']['determinism_replay']};"
        + f" agreement_gate={receipt['controls']['synthetic_agreement_outcome_accepted']}",
    ]
    passed = sum(receipt["checks"].values())
    lines.append(f"TOTAL: PASS={passed} FAIL={len(receipt['checks']) - passed}")
    return "\n".join(lines) + "\n"


def run() -> tuple[dict, str]:
    started = monotonic()
    controls = input_controls()
    first = science_measurement()
    second = science_measurement()
    deterministic = first == second
    census = first["A_LOCKED_CONTENT_CENSUS"]
    visibility = first["B_READOUT_VISIBILITY"]
    scope = first["C_SCOPE"]

    a_reconciliation = bool(
        census["class_count"] == len(census["classes"])
        and census["proper_cubic_group_order"] == len(ROTATIONS)
        and census["witness_multiplicity"] == sum(
            row["orbit_size"] for row in census["classes"]
        )
        and all(
            len(row["table"]) == 2 ** len(row["controls"])
            for row in census["classes"]
        )
        and all(
            row["J"] == vector_sum_squared(tuple(row["controls"]))
            and row["orbit_stabilizer_product"] == row["group_order"]
            and len(row["one_neighbour_bit_edges"])
            == len(row["controls"]) * 2 ** len(row["controls"])
            and all(
                edge["changes_locked_content"]
                == (edge["content_before"] != edge["content_after"])
                for edge in row["one_neighbour_bit_edges"]
            )
            for row in census["classes"]
        )
        and census["point_mass_normalization_failures"] == 0
        and census["locked_content_support_failures"] == 0
    )
    b_reconciliation = validate_readout_measurement(visibility)
    c_reconciliation = bool(
        scope["full_mosaic_claimed"] is False
        and scope["formation_site_probability_or_rate_claimed"] is False
        and scope["selected_physical_readout_claimed"] is False
        and scope["generic_axiom_only_consequence_claimed"] is False
        and scope["binary_M2C_embedding_declared_not_unique"] is True
        and scope["point_mass_distribution_constructed_at_finite_cap"] is True
        and bool(scope["tested"] and scope["established"])
    )
    runtime_budget_met = monotonic() - started < AUDIT_TIMEOUT_SEC
    controls.update({
        "determinism_replay": deterministic,
        "synthetic_agreement_outcome_accepted": synthetic_agreement_visibility_control(),
        "runtime_budget_met": runtime_budget_met,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    })
    d_controls = bool(
        controls["literal_source_read_count"] <= 6
        and controls["all_inputs_relative_and_present"]
        and controls["sha_pins_match"] and controls["blob_pins_match"]
        and not controls["blocked_ast_imports"]
        and not controls["prior_cycle_modules_loaded"]
        and controls["base_is_ancestor_of_head"]
        and deterministic
        and controls["synthetic_agreement_outcome_accepted"]
        and runtime_budget_met
    )
    receipt = {
        "cycle": CYCLE,
        "artifact": "neighbour-dependence locked-content and readout bounded theorem primary",
        "audit_status_authority": "independent audit lane only",
        "integrity_policy": (
            "checks gate construction and reconciliation only; a coherent family-wide "
            "agreement outcome passes the same top-level visibility validator"
        ),
        "findings": first,
        "science_digest": digest(first),
        "controls": controls,
        "checks": {
            "A_LOCKED_CONTENT_CENSUS": a_reconciliation,
            "B_READOUT_VISIBILITY": b_reconciliation,
            "C_SCOPE": c_reconciliation,
            "D_CONTROLS": d_controls,
        },
    }
    receipt["primary_source_sha256"] = sha256((ROOT / PRIMARY_PATH).read_bytes()).hexdigest()
    stdout = render_stdout(receipt)
    controls["stdout_bytes"] = len(stdout.encode())
    if controls["stdout_bytes"] >= STDOUT_LIMIT_BYTES:
        receipt["checks"]["D_CONTROLS"] = False
        stdout = render_stdout(receipt)
        controls["stdout_bytes"] = len(stdout.encode())
    receipt["pass"] = all(receipt["checks"].values())
    receipt["stdout_sha256"] = sha256(stdout.encode()).hexdigest()
    return receipt, stdout


def main() -> int:
    if sys.argv[1:]:
        raise SystemExit(f"usage: {Path(__file__).name}")
    receipt, stdout = run()
    receipt_path = ROOT / RECEIPT_PATH
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    sys.stdout.write(stdout)
    return 0 if receipt["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
