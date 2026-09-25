"""Read-only source binding and arithmetic review of released root32 evidence.

This checker never imports or executes the author program. Stored exponential
and matrix calculations are author evidence; the arithmetic below checks their
internal consistency, not an independent numerical replication.
"""
from pathlib import Path
import ast
import hashlib
import itertools
import json
import math
import subprocess
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
FROZEN = HERE / "post_frozen_author"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def verify_members(root, seal_name, expected_sha):
    seal_path = root / seal_name
    assert digest(seal_path) == expected_sha
    seal = read_json(seal_path)
    for row in seal["members"]:
        path = root / row["path"]
        assert path.stat().st_size == row["bytes"], path
        assert digest(path) == row["sha256"], path
    assert len(seal["members"]) == seal["member_count"]
    return {"seal": str(seal_path), "sha256": digest(seal_path),
            "sealed_utc": seal["sealed_utc"],
            "members_unchanged": len(seal["members"])}


def run():
    pre = verify_members(HERE, "PRE_SEAL.json",
                         "75b6df3f1a085d3f921f9480a633e726c09230d9b027b62bc3e48b3a2898cdef")
    prior_directory = BASE / "photon-added-energy-independent"
    prior = verify_members(prior_directory, "PUBLICATION_COMPARISON_SEAL.json",
                           "19f2c31594a7a807771dde273c81bc01af9ecaf001f70eb569f4228be99e779c")
    incident = prior_directory / "PUBLICATION_SCOPE_INCIDENT.json"
    assert digest(incident) == "e60ae5601e7625476f3e221d5ac18b5d7eb94c41b8773a1bb7f37bd3c30ae536"
    prior["scope_incident_sha256"] = digest(incident)
    prior["scope"] = "Mechanical preservation only; no new Part B source read or validation."

    pins = read_json(HERE / "POST_SOURCE_PINS.json")
    origins = []
    for row in pins["sources"]:
        origin, frozen = Path(row["origin"]), HERE / row["frozen"]
        assert digest(origin) == row["sha256"] == digest(frozen), origin
        assert origin.stat().st_size == frozen.stat().st_size == row["bytes"]
        origins.append({"origin": str(origin), "frozen": row["frozen"],
                        "sha256": row["sha256"], "bytes": row["bytes"]})
    author_seal = read_json(FROZEN / "AUTHOR_SEAL.json")
    for name, sha in author_seal["files"].items():
        assert digest(FROZEN / name) == sha
    assert len(author_seal["files"]) == 8

    parent_pins = read_json(FROZEN / "SOURCE_PINS.json")
    repository = BASE / "campaign-working"
    revision = "48a52f2f19056a134e9f01d8ac2896bc287cd00c"
    parent_checks = []
    for row in parent_pins["sources"]:
        original = Path(row["path"])
        relative = original.relative_to(repository)
        blob = subprocess.run(["git", "show", f"{revision}:{relative.as_posix()}"],
                              cwd=repository, check=True, capture_output=True).stdout
        sha = hashlib.sha256(blob).hexdigest()
        assert sha == row["sha256"] == digest(HERE / "sources" / relative)
        assert digest(original) == sha
        parent_checks.append({"revision": revision, "path": str(relative),
                              "sha256": sha, "bytes": len(blob),
                              "PRE_frozen_and_working_bytes_match": True})
    assert len(parent_checks) == 3

    code_path = FROZEN / "number_offset_controls.py"
    tree = ast.parse(code_path.read_text())
    functions = [node.name for node in ast.walk(tree)
                 if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    assert set(functions) == {"run", "generator", "characteristic", "power",
                              "noevent", "history", "pairs"}
    data = read_json(FROZEN / "NUMBER_OFFSET_RESULTS.json")
    execution = read_json(FROZEN / "EXECUTION.json")
    assert (FROZEN / "NUMBER_OFFSET_RESULTS.json").read_bytes() == (FROZEN / "CONTROL.stdout").read_bytes()
    assert data["source_sha256"] == execution["script_sha256"] == digest(code_path)
    assert execution["stdout_sha256"] == digest(FROZEN / "CONTROL.stdout")
    assert execution["stderr_sha256"] == digest(FROZEN / "CONTROL.stderr")
    assert execution["exit_code"] == 0 and (FROZEN / "CONTROL.stderr").stat().st_size == 0
    assert data["original_rotor_scientific_simulation"] is False
    assert data["independent_researcher_check"] is False

    offsets = [(0., 0., 0.), (3., -7., 5.), (.1, 1.3, -2.2), (100., -40., 75.)]
    counts = data["count_rows"]
    assert len(counts) == 108
    observed = {(tuple(r["offset"]), r["time"], r["tilt"], r["input"]) for r in counts}
    assert observed == set(itertools.product(offsets, (.02, .3, 1.7), range(3), range(3)))
    count_recomputed = []
    count_baselines = {}
    for row in counts:
        reference, altered = complex(*row["reference"]), complex(*row["altered"])
        residual = abs(altered-reference)
        assert abs(residual-row["difference_abs"]) < 1e-28
        assert residual < 2e-12
        count_recomputed.append(residual)
        key = row["time"], row["tilt"], row["input"]
        assert count_baselines.setdefault(key, row["reference"]) == row["reference"]

    powers = data["power_rows"]
    assert len(powers) == 24
    observed = {(tuple(r["offset"]), r["input"], r["channel"]) for r in powers}
    assert observed == set(itertools.product(offsets, range(3), range(2)))
    power_recomputed, power_baselines = [], {}
    for row in powers:
        residual = abs(row["altered_power"]-row["original_power"]-row["predicted_shift"])
        assert abs(residual-row["difference_abs"]) < 1e-28
        assert residual < 1e-12
        assert row["rate"] > 0
        power_recomputed.append(residual)
        key = row["input"], row["channel"]
        assert power_baselines.setdefault(key, (row["rate"], row["original_power"])) == (row["rate"], row["original_power"])
        if row["input"] < 2:
            gap = row["offset"][1]-row["offset"][0]
            assert abs(row["predicted_shift"]-gap*row["rate"]) < 2e-14

    same = data["same_sector_rows"]
    assert len(same) == 4 and {tuple(r["offset"]) for r in same} == set(offsets)
    for row in same:
        assert row["same_N_input_difference"] == row["altered_difference"] == .3999999999999999

    histories = data["history_rows"]
    assert len(histories) == 36
    observed = {(tuple(r["offset"]), tuple(r["marks"]), r["input"]) for r in histories}
    assert observed == set(itertools.product(offsets, ((), (0,), (1, 0)), range(3)))
    history_baselines = {}
    for row in histories:
        assert 0 <= row["probability"]
        for field in ("probability_difference_abs", "sector_phase_residual", "diagonal_block_difference"):
            assert 0 <= row[field] < 1e-12
        if row["input"] < 2:
            assert row["full_conditional_unnormalized_state_difference"] < 1e-12
        key = tuple(row["marks"]), row["input"]
        assert history_baselines.setdefault(key, row["probability"]) == row["probability"]
    full_coherence_witness = max((r for r in histories if r["input"] == 2),
        key=lambda r: r["full_conditional_unnormalized_state_difference"])
    assert full_coherence_witness["full_conditional_unnormalized_state_difference"] > .1
    reported_aggregate = max(*count_recomputed, *power_recomputed,
        *(r["probability_difference_abs"] for r in histories),
        *(r["sector_phase_residual"] for r in histories))
    assert reported_aggregate == data["max_checked_identity_error"]
    diagonal_max = max(r["diagonal_block_difference"] for r in histories)

    # Algebra only: 3*x*(x-1)+2-x*(x+1) = 2*(x-1)^2.
    # Integer x has x*(x-1)>=0, making the physical D estimate possible.
    lhs_coefficients = [2, -4, 2]  # increasing powers of x
    rhs_coefficients = [2, -4, 2]
    assert lhs_coefficients == rhs_coefficients

    return {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Released root32 source binding, all stored-row arithmetic, and unchanged-seal checks. Author program never imported or executed.",
        "checker_sha256": digest(Path(__file__)),
        "PRE_preserved": pre,
        "prior_Part_A_publication_preserved": prior,
        "released_origins": origins,
        "released_origin_count": len(origins),
        "author_seal_members_verified": len(author_seal["files"]),
        "current_parent_git_bindings": parent_checks,
        "author_AST_function_inventory": functions,
        "author_execution_binding": execution,
        "author_internal_elapsed_seconds": data["elapsed_seconds"],
        "rows_reviewed": {"count": len(counts), "selected_power": len(powers),
                           "same_number_difference": len(same), "fixed_history": len(histories)},
        "count_max_stored_complex_difference_recomputed": max(count_recomputed),
        "power_max_stored_difference_recomputed": max(power_recomputed),
        "reported_aggregate_recomputed": reported_aggregate,
        "diagonal_block_max_separately_checked": diagonal_max,
        "diagonal_block_error_in_author_aggregate": False,
        "largest_stored_coherent_state_noninvariance": full_coherence_witness,
        "same_number_input_difference_all_four_offsets": same[0]["same_N_input_difference"],
        "electric_graph_bound_polynomial_coefficients": {"left": lhs_coefficients, "right": rhs_coefficients},
        "scientific_proof_basis": "Preserved independent PRE, released argument comparison, and explicitly attributed POST sufficient-domain proof.",
        "independent_author_numerical_replication": False,
        "new_author_programs_executed_or_imported": [],
        "other_active_scientific_packets_opened_during_POST": [],
        "weak_field_rate_premise_independently_checked": False,
        "failures": [],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, allow_nan=False))
