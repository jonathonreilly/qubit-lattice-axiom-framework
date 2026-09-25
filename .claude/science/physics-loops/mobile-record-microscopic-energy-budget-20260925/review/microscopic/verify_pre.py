#!/usr/bin/env python3
"""Read-only evidence verifier: no imports of control programs and no writes."""
import ast
import hashlib
import importlib.metadata
import json
import math
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def data(path):
    return json.loads(path.read_text())


def key(row):
    return row["graph"], tuple(row["q"]), tuple(row["E"])


def main():
    sources = data(HERE / "SOURCE_PINS.json")
    for row in sources["sources"]:
        raw = (HERE / row["snapshot"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == row["sha256"]
        assert len(raw) == row["bytes"]
        if "origin" in row:
            assert Path(row["origin"]).read_bytes() == raw
        if "git_path" in row:
            repo = row.get("origin_git_repository",
                           str(HERE.parent / "campaign-working"))
            old = subprocess.run(
                ["git", "show", row["git_revision"] + ":" + row["git_path"]],
                cwd=repo, check=True, capture_output=True).stdout
            assert old == raw
    attempts = [
        ("primitive_attempt01", "primitive_control.py", 1, None),
        ("primitive_attempt02", "primitive_control.py", 0, "PRIMITIVE_RESULTS.json"),
        ("primitive_attempt03", "primitive_control.py", 0, "PRIMITIVE_RESULTS.json"),
        ("microscopic_attempt01", "microscopic_control.py", 0, "MICROSCOPIC_RESULTS.json")
    ]
    receipts = []
    for name, code, exit_code, result in attempts:
        d = HERE / name
        receipt = data(d / "EXECUTION.json")
        assert receipt["exit_code"] == exit_code
        assert receipt["source_sha256"] == digest(d / code)
        for stream in ("stdout", "stderr"):
            assert receipt[stream + "_sha256"] == digest(d / (stream + ".log"))
            assert receipt[stream + "_bytes"] == (d / (stream + ".log")).stat().st_size
        if result:
            assert (d / result).read_bytes() == (d / "stdout.log").read_bytes()
            assert data(d / result)["source_sha256"] == receipt["source_sha256"]
            assert data(d / result)["all_assertions_passed"]
            assert receipt["stderr_bytes"] == 0
        else:
            assert receipt["stdout_bytes"] == 0
            assert "not enough values to unpack" in (d / "stderr.log").read_text()
        receipts.append({"attempt": name, **receipt})
    old = data(HERE / "primitive_attempt02/PRIMITIVE_RESULTS.json")
    final = data(HERE / "primitive_attempt03/PRIMITIVE_RESULTS.json")
    old_rows = {key(x): x for x in old["local_identity_rows"]}
    final_rows = {key(x): x for x in final["local_identity_rows"]}
    assert len(old_rows) == 45 and len(final_rows) == 51
    assert all(final_rows[k] == row for k, row in old_rows.items())
    assert final["scalar_weight_rows"] == old["scalar_weight_rows"]
    assert final["unconfined_flux_operator_counterexample_rows"] == old["unconfined_flux_operator_counterexample_rows"]
    assert digest(HERE / "primitive_control.py") == final["source_sha256"]
    assert sum(x["primitive_Gauss_outputs_checked"] for x in final["graph_totals"]) == 13035
    assert sum(x["integer_shift_cases"] for x in final["scalar_weight_rows"]) == 556
    for filename, expected in (("PRIMITIVE_REVIEW.tsv", old_rows),
                               ("PRIMITIVE_FINAL_REVIEW.tsv", final_rows)):
        lines = (HERE / filename).read_text().splitlines()
        names = lines[0].split("\t")
        restored = [dict(zip(names, map(json.loads, line.split("\t"))))
                    for line in lines[1:]]
        assert {key(x): x for x in restored} == expected
    positive_D = sum(int(x["D"]) > 0 for x in final_rows.values())
    false_omission = sum(x["dropping_finite_spin_correction_is_wrong"]
                         for x in final_rows.values())
    assert positive_D == 6 and false_omission > 0
    micro = data(HERE / "microscopic_attempt01/MICROSCOPIC_RESULTS.json")
    assert digest(HERE / "microscopic_control.py") == micro["source_sha256"]
    assert micro["couplings"] == {"K": 1, "delta": 1, "kappa": 1}
    assert [r["S"] for r in micro["rows"]] == [4, 8, 12, 16, 24]
    mixed_count = 0
    for row in micro["rows"]:
        eps = row["epsilon"]
        assert math.isclose(eps*eps*row["S"]*(row["S"]+1), 1., abs_tol=1e-14)
        assert row["high_cluster_minimum"] > .5
        assert row["low_cluster_dimension"] == 2*row["S"]+1
        assert row["bare_P_rate"] == 0
        assert math.isclose(row["bare_P_mean_energy"], 4/eps**2, abs_tol=1e-9)
        assert abs(row["common_ground_rate"]-8) < 1e-12
        assert row["full_occupancy_escaping_word"]["stationary_exact"]
        energies = [x["actual_mean_energy"] for x in row["mixed_state_rows"]]
        assert max(energies) == min(energies)
        rates = [x["actual_rate"] for x in row["mixed_state_rows"]]
        assert max(rates) > min(rates)
        for x in row["mixed_state_rows"]:
            assert math.isclose(x["rotated_high_weight"], eps**4/2, abs_tol=1e-18)
            assert x["mean_energy_excess"] > .49
            mixed_count += 1
    assert mixed_count == 20
    imports = {}
    allowed = {"collections", "fractions", "hashlib", "itertools", "pathlib",
               "json", "math", "time", "numpy"}
    for filename in ("primitive_control.py", "microscopic_control.py"):
        tree = ast.parse((HERE / filename).read_text())
        names = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names += [x.name.split(".")[0] for x in node.names]
            elif isinstance(node, ast.ImportFrom):
                names.append(node.module.split(".")[0])
        assert set(names) <= allowed
        imports[filename] = sorted(set(names))
    report_text = (HERE / "PRE.md").read_text()
    assert not [x for x in report_text if ord(x) < 32 and x not in "\n\t"]
    own_tree = ast.parse(Path(__file__).read_text())
    mutations = [n for n in ast.walk(own_tree)
                 if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                 and n.func.attr in ("write_text", "write_bytes", "unlink",
                                     "mkdir", "rename", "replace", "chmod")]
    assert not mutations
    report = {
        "checked_utc": datetime.now(timezone.utc).isoformat(),
        "verifier_source_sha256": digest(Path(__file__)),
        "PRE_sha256": digest(HERE / "PRE.md"),
        "source_manifest_sha256": digest(HERE / "SOURCE_PINS.json"),
        "source_entries_verified": len(sources["sources"]),
        "live_origins_verified": sum("origin" in r for r in sources["sources"]),
        "exact_git_objects_verified": sum("git_path" in r for r in sources["sources"]),
        "attempt_receipts": receipts,
        "primitive_counts": {
            "previous_rows_unchanged": 45, "current_rows": 51,
            "nonzero_D_rows_added": positive_D,
            "omitting_finite_spin_correction_rejected_rows": false_omission,
            "primitive_Gauss_output_checks": 13035,
            "integer_weight_cases": 556,
            "unconfined_flux_formula_rows": 8},
        "microscopic_controls": {
            "spin_rows": 5, "mixed_coherence_rows": mixed_count,
            "S_values": [r["S"] for r in micro["rows"]],
            "smallest_retained_roundoff_high_weight":
                min(r["ground_rotated_high_weight"] for r in micro["rows"])},
        "control_imports": imports,
        "runtime": {"python": sys.version, "numpy": importlib.metadata.version("numpy")},
        "verifier_has_no_file_mutation_calls": True,
        "root37_or_other_checker_access": False,
        "parent_or_author_scientific_execution": False,
        "provisional_dependency_retained": "Root36 common-law energy/activity inequality, including its fixed-graph small-K/delta global scope.",
        "all_evidence_comparisons_passed": True,
        "limits": "Bookkeeping and arithmetic correspondence; no rerun of scientific controls, formal audit, empirical test or proof replacement."
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
