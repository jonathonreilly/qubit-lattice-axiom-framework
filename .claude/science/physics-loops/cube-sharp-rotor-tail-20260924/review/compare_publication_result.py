#!/usr/bin/env python3
"""Bind regenerated publication output to the independently verified witness."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
PUBLICATION = BASE / "sharp-rotor-tail-publication"
OUTPUT = PUBLICATION / "outputs/sharp_rotor_cube_energy_tail_20260924"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    sources = [
        (OUTPUT / "RATIONAL_LAURENT_CERTIFICATES.json", "efed9ff85c39626b132bb897a743bd77d2117757249a9becfcb828f51358cdec"),
        (OUTPUT / "SHARP_TAIL_RESULTS.json", "afdf975511fd04331d91b51829e2d80078b2ea200b60a9cdd11be6f44742b87b"),
        (BASE / "SECOND_PUBLICATION_CACHE_EXECUTION.json", "d997161013d44532da390c40c6200dbe39112904065351b94f12f53e0d4cd2a1"),
    ]
    copied = {}
    records = []
    for source, expected in sources:
        raw = source.read_bytes()
        assert sha(raw) == expected, source
        snapshot = ROOT / "released_sources" / source.name
        assert not snapshot.exists() or snapshot.read_bytes() == raw
        snapshot.write_bytes(raw)
        records.append({"source": str(source), "snapshot": str(snapshot), "sha256": expected, "bytes": len(raw)})
        copied[source.name] = json.loads(raw)
    bindings = json.loads((ROOT / "POST_INPUTS.json").read_text())
    for item in bindings["sources"]:
        assert sha(Path(item["snapshot"]).read_bytes()) == item["sha256"]
        assert sha(Path(item["source"]).read_bytes()) == item["sha256"], "A released original changed"
    prior = json.loads((ROOT / "released_sources/MODULE_EXACT_CERTIFICATES_ALL.json").read_text())
    published = copied["RATIONAL_LAURENT_CERTIFICATES.json"]
    result = copied["SHARP_TAIL_RESULTS.json"]
    envelope = copied["SECOND_PUBLICATION_CACHE_EXECUTION.json"]
    independent_summary = json.loads((ROOT / "POST_CHECK_RESULTS.json").read_text())
    for name, expected in independent_summary["output_sha256"].items():
        assert sha((ROOT / name).read_bytes()) == expected
    primitive = json.loads((ROOT / "INDEPENDENT_PRIMITIVE_Q.json").read_text())
    independent_q = {(row, column, tuple(exponent)): coefficient
                     for row, column, exponent, coefficient in primitive["Q_coefficients"]}
    published_q = {}
    for row, cells in enumerate(published["primitive_Q"]["rows"]):
        for cell in cells:
            for term in cell["terms"]:
                key = (row, cell["column"], tuple(term["exponent"]))
                assert key not in published_q
                published_q[key] = term["coefficient"]
    assert published_q == independent_q
    assert published["certificates"] == prior["certificates"]
    assert published["shifts"] == prior["shifts"]
    assert published["identity"] == prior["identity"]
    for field in ["edges", "chords", "dark_charge_words", "bright_charge_words"]:
        assert published["primitive_Q"][field] == primitive[field], field
    assert result["primitive_dimensions"] == {"bright": 72, "dark": 24, "cycle": 5}
    assert result["multiplier_l1_degree"] == 3
    assert result["identity_count"] == independent_summary["exact_identity_count"] == 120
    assert result["exact_coefficient_checks"] is True
    assert result["maximum_row_coefficient_L1_ceiling"] == independent_summary["maximum_L1_ceiling"]
    assert result["sum_matrix_sup_norm_squared_bound"] == independent_summary["M_P"]
    ranks = json.loads((ROOT / "INDEPENDENT_SIGN_RANKS.json").read_text())["ranks"]
    assert result["sign_phase_exact_ranks"] == [
        {"pi_bits": record["pi_bits"], "exact_rank": record["rank"]} for record in ranks]
    assert result["certificate_sha256"] == sources[0][1]
    assert result["certificate_bytes"] == sources[0][0].stat().st_size
    assert result["source_sha256"] == sha((PUBLICATION / "scripts/sharp_actual_rotor_cube_energy_tail_2026_09_24.py").read_bytes())
    execution = envelope["result"]
    assert execution["runner"] == "scripts/sharp_actual_rotor_cube_energy_tail_2026_09_24.py"
    assert execution["status"] == "ok" and execution["exit_code"] == 0 and execution["stderr"] == ""
    decoder = json.JSONDecoder()
    remaining = execution["stdout"].lstrip()
    events = []
    while remaining.startswith("{"):
        value, end = decoder.raw_decode(remaining)
        events.append(value)
        remaining = remaining[end:].lstrip()
    assert events[-1] == result
    assert remaining.strip() == "TOTAL: PASS=4 FAIL=0"
    phase_events = [event for event in events if "verified_columns" in event]
    assert [(event["phase"], event["verified_columns"]) for event in phase_events] == [(j, 24) for j in range(5)]
    comparison = {
        "sources": records,
        "root_source_bytes_unchanged": True,
        "entire_publication_certificate_list_equal_to_checked_root_witness": True,
        "entire_multiplier_shift_list_equal": True,
        "all_288_publication_Q_coefficients_equal_to_independent_reconstruction": True,
        "all_edge_chord_and_charge_order_metadata_equal_to_independent_reconstruction": True,
        "every_publication_sign_rank_and_coefficient_bound_equal_to_independent_results": True,
        "complete_execution_stdout_final_result_equals_published_result": True,
        "reported_execution_status": execution["status"],
        "reported_execution_exit_code": execution["exit_code"],
        "reported_execution_elapsed_sec": execution["elapsed_sec"],
        "reported_execution_stderr": execution["stderr"],
        "comparison_source_sha256": sha(Path(__file__).read_bytes()),
        "scope": "The complete released execution record was inspected and bound to matching source/result/witness bytes; no root discovery code was executed by this checker and cache machinery is not separately audited.",
    }
    (ROOT / "PUBLICATION_COMPARISON.json").write_text(json.dumps(comparison, indent=2, sort_keys=True) + "\n")
    print(json.dumps(comparison, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
