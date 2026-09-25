"""Additional scoped input/header checks, with no primary execution."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PUB = BASE / "input-energy-power-publication"
DEST = HERE / "publication_frozen"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    frozen = json.loads((DEST / "INPUT_ENERGY_POWER_PUBLICATION_FROZEN_SOURCES.json").read_text())
    runner = (PUB / frozen["runner"]).read_bytes()
    tree = ast.parse(runner)
    paths = next(ast.literal_eval(node.value) for node in tree.body if isinstance(node, ast.Assign)
                 and any(isinstance(x, ast.Name) and x.id == "AUDIT_INPUT_PATHS" for x in node.targets))
    expected = dict(frozen["files_sha256"])
    expected.update({row["path"]: row["sha256"] for row in frozen["parents"]})
    scoped = {frozen["note"],
              "docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
              "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
              "docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
              "docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md"}
    scoped.update(path for path in frozen["runtime"] if "/runtime/energy/" in path)
    rows = []
    for path in paths:
        if path in scoped:
            body = (PUB / path).read_bytes()
            actual = sha(body)
            assert actual == expected[path]
            rows.append({"path": path, "sha256": actual, "bytes": len(body),
                         "basis": "Direct scoped source bytes; prior scientific review reused where unchanged."})
        else:
            rows.append({"path": path, "sha256": expected[path],
                         "basis": "Shared frozen-manifest metadata only; source body not read in this check."})
    assert len(rows) == 13 and sum(row["path"] in scoped for row in rows) == 7
    execution = json.loads((BASE / "INPUT_ENERGY_POWER_PUBLICATION_CACHE_EXECUTION.json").read_text())
    info = execution["result"]
    cache_path = Path(execution["cache_path"])
    actual_cache = cache_path.read_text()
    header = json.loads((DEST / "EXECUTION_PART_A_AND_SHARED_METADATA.json").read_text())["cache_header"]
    expected_cache = (
        "===== runner cache v1 =====\n"
        + f"runner: {frozen['runner']}\n"
        + f"runner_sha256: {sha(runner)}\n"
        + f"input_fingerprint_sha256: {header['input_fingerprint_sha256']}\n"
        + f"timeout_sec: {info['timeout_sec']}\n"
        + f"exit_code: {info['exit_code']}\n"
        + f"elapsed_sec: {info['elapsed_sec']:.2f}\n"
        + f"status: {info['status']}\n"
        + "----- stdout -----\n" + info["stdout"][-200000:] + "\n"
        + "----- stderr -----\n" + info["stderr"][-50000:] + "\n"
    )
    assert expected_cache == actual_cache
    helper = PUB / "scripts/runner_cache.py"
    helper_data = helper.read_bytes()
    helper_lines = helper_data.decode().splitlines(keepends=True)
    helper_excerpt = "".join(helper_lines[:265]) + "\n[Unreviewed middle omitted.]\n\n" + "".join(helper_lines[554:625])
    helper_target = DEST / "RUNNER_CACHE_RELEVANT_PROCEDURE.txt"
    helper_target.write_text(helper_excerpt)
    workflow_rev = "48a52f2f19056a134e9f01d8ac2896bc287cd00c"
    workflow_path = "docs/ai_methodology/SCIENCE_WORKFLOW.md"
    workflow_data = subprocess.check_output(["git", "show", workflow_rev + ":" + workflow_path],
                                            cwd=BASE / "campaign-working")
    assert sha(workflow_data) == "d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4"
    result = {
        "verified_utc": datetime.now(timezone.utc).isoformat(),
        "declared_input_count": 13, "direct_scoped_input_byte_checks": 7,
        "remaining_input_hashes_metadata_only": 6, "declared_inputs": rows,
        "combined_input_fingerprint": header["input_fingerprint_sha256"],
        "combined_raw_input_fingerprint_independently_recomputed": False,
        "fingerprint_limit": "The v1 digest hashes complete input bytes, including excluded science. Its recorded value is shared receipt metadata; this check does not claim full-source recomputation.",
        "entire_cache_matches_writer_format_and_execution": True,
        "cache_stdout_retained_characters_before_separator_newline": 200000,
        "complete_external_stdout_characters": len(info["stdout"]),
        "cache_helper": {"path": str(helper), "sha256": sha(helper_data), "bytes": len(helper_data),
                         "read_line_ranges_inclusive": [[1, 265], [555, 625]],
                         "frozen_excerpt": str(helper_target.relative_to(HERE)), "excerpt_sha256": sha(helper_target.read_bytes()),
                         "role": "Read-only cache format and fingerprint procedure; not science or audit execution."},
        "current_workflow": {"repository": str(BASE / "campaign-working"), "revision": workflow_rev,
                             "git_path": workflow_path, "sha256": sha(workflow_data),
                             "read_status": "Identical to the already read workflow; no changed instruction content."},
        "code_sha256": sha(Path(__file__).read_bytes())
    }
    (HERE / "PUBLICATION_METADATA_CHECKS.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
