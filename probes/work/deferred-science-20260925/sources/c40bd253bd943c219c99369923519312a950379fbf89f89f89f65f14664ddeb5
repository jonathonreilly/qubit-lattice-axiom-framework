#!/usr/bin/env python3
"""Read-only correspondence and PRE-preservation checks; no author computation."""
import datetime
import hashlib
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "POST_sources"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    pre_seal_hash = "7b3a5de5ad3c2d1d47ad259333aa7ab90297d0108ebe36868306a72f8f4b1234"
    assert sha(ROOT / "PRE_SEAL.json") == pre_seal_hash
    pre = json.loads((ROOT / "PRE_SEAL.json").read_text())
    assert pre["member_count"] == len(pre["members"]) == 23
    for row in pre["members"]:
        path = ROOT / row["path"]
        assert sha(path) == row["sha256"] and path.stat().st_size == row["bytes"]
        assert path.stat().st_mode & 0o222 == 0

    root_pins = []
    for filename in ("POST_RELEASE_FREEZE.json", "POST_CONTROL_FREEZE.json"):
        obj = json.loads((ROOT / filename).read_text())
        rows = obj.get("released_top_level_sources", obj.get("frozen_control_members"))
        for row in rows:
            path = ROOT / row["snapshot"]
            assert sha(path) == sha(Path(row["source"])) == row["sha256"]
            assert path.stat().st_size == row["bytes"]
            root_pins.append(row)

    for seal_name in ("AUTHOR_SEAL.json", "ATTAINMENT_SEAL.json", "CONTROL_SEAL.json"):
        seal = json.loads((SOURCE / seal_name).read_text())
        for name, digest in seal["files_sha256"].items():
            assert sha(SOURCE / name) == digest
    own_pins = json.loads((ROOT / "SOURCE_PINS.json").read_text())
    scientific_hashes = {row["sha256"] for row in own_pins["scientific_sources"]}
    author = json.loads((SOURCE / "AUTHOR_SEAL.json").read_text())
    assert set(author["source_pins"].values()) == scientific_hashes
    for name, digest in author["source_pins"].items():
        assert sha(Path(name)) == digest

    helper = json.loads((ROOT / "POST_REUSED_HELPER_SCOPE.json").read_text())
    assert sha(ROOT / helper["snapshot"]) == sha(Path(helper["source"])) == helper["sha256"]
    result = json.loads((SOURCE / "NOEVENT_CONTROL_RESULTS.json").read_text())
    assert result["source_sha256"] == sha(SOURCE / "noevent_controls.py")
    assert result["actual_spin_one"]["builder_sha256"] == helper["sha256"]

    full_stdout = (SOURCE / "NOEVENT_CONTROL.stdout").read_text()
    decoder = json.JSONDecoder()
    objects, positions = [], []
    position = 0
    while position < len(full_stdout):
        while position < len(full_stdout) and full_stdout[position].isspace():
            position += 1
        if position == len(full_stdout):
            break
        start = position
        value, position = decoder.raw_decode(full_stdout, position)
        objects.append(value)
        positions.append([start, position])
    assert len(objects) == 4
    assert objects[:3] == result["actual_spin_one"]["rows"]
    assert objects[-1] == result
    assert full_stdout[positions[-1][0]:].encode() == (SOURCE / "NOEVENT_CONTROL_RESULTS.json").read_bytes()
    assert (SOURCE / "NOEVENT_CONTROL.stderr").stat().st_size == 0

    # Small independent recount only; no author function or builder imported.
    A = {0, 3, 5, 6}
    B = {1, 2, 4, 7}
    edges = [(a,b) for a in A for b in B if a ^ b in (1,2,4)]
    expected = []
    for occupied in itertools.combinations(range(8),4):
        occ = set(occupied)
        expected.append({"occupied": list(occupied), "grade": len(A-occ),
                         "vacant_edges": sum(a not in occ and b not in occ for a,b in edges)})
    assert expected == result["geometry"]["all_70_occupancy_rows"]
    hist = {}
    for row in expected:
        key = str((row["grade"], row["vacant_edges"]))
        hist[key] = hist.get(key, 0) + 1

    actual = []
    for row in result["actual_spin_one"]["rows"]:
        actual.append({
            "epsilon": row["epsilon"], "dimension": row["dimension"],
            "first_high_relative_error": abs(row["high_norms_over_predicted_powers"][0]/row["expected_first_high_coefficient"]-1),
            "low_component_second_moment": row["low_scaled_second_moment"],
            "low_component_second_moment_target": row["expected_low_coefficient"],
            "low_component_second_moment_relative_error": abs(row["low_scaled_second_moment"]/row["expected_low_coefficient"]-1),
            "low_vector_error": row["low_vector_error"],
            "decomposition_residual": row["decomposition_residual"],
        })
    toy = result["toy"]["rows"][-1]
    checks = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Correspondence and preservation; author controls were not executed or made independent",
        "pre_seal_sha256": pre_seal_hash, "pre_members_unchanged": len(pre["members"]),
        "root_source_pins": root_pins,
        "reused_builder": {k:v for k,v in helper.items() if k != "functions"},
        "author_seal_scientific_pins_equal_PRE_scientific_hashes": len(scientific_hashes),
        "stdout_bytes_consumed": len(full_stdout.encode()),
        "stdout_json_object_count": len(objects), "stdout_object_character_intervals": positions,
        "stdout_progress_rows_equal_result_rows": len(objects)-1,
        "stdout_final_object_byte_identical_to_result_file": True,
        "stderr_bytes": (SOURCE / "NOEVENT_CONTROL.stderr").stat().st_size,
        "exit_code_as_recorded_by_author_seal": json.loads((SOURCE / "CONTROL_SEAL.json").read_text())["exit_code"],
        "independent_occupancy_recount": {"count": len(expected), "histogram_grade_empty_edges": hist},
        "author_fixed_S1_diagnostics": actual,
        "author_finest_toy_diagnostics": {
            "epsilon": toy["epsilon"],
            "scaled_variance": toy["scaled_conditional_variance"],
            "scaled_variance_target": toy["predicted_conditional_coefficient"],
            "scaled_variance_relative_error": abs(toy["scaled_conditional_variance"]/toy["predicted_conditional_coefficient"]-1),
            "scaled_Fisher": toy["scaled_weighted_Fisher"],
            "scaled_Fisher_target": toy["predicted_Fisher_coefficient"],
            "scaled_Fisher_relative_error": abs(toy["scaled_weighted_Fisher"]/toy["predicted_Fisher_coefficient"]-1),
        },
        "execution_limits": "No fixed-S cube run repeated; no independent numerical reproduction of author data; exact dissipativity and graded claims checked analytically in POST",
    }
    (ROOT / "POST_EVIDENCE_CHECK.json").write_text(json.dumps(checks, indent=2) + "\n")
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
