#!/usr/bin/env python3
"""Replay frozen evidence in temporary directories without changing its bytes.

This author-written portability check is not another independent derivation.
Every subprocess has a 120-second deadline and disables bytecode writes.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BUNDLE = HERE/"independent"
ORIGINAL_SUBDIR = Path(".claude/science/physics-loops/observations-backward-derivation-24h-20261015/independent_non_equilibrium_scalar")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    records = []
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")

    def run_case(name, tree, script, expected_exit, expected_bytes, output=None):
        process = subprocess.run([sys.executable, "-B", str(script)], cwd=tree,
                                 env=environment, capture_output=True, timeout=120)
        actual = (tree/output).read_bytes() if output else process.stdout
        same = actual == expected_bytes
        record = {"case": name, "exit_code": process.returncode,
                  "expected_exit_code": expected_exit,
                  "byte_identical_output": same,
                  "expected_sha256": digest(expected_bytes),
                  "actual_sha256": digest(actual),
                  "stdout_sha256": digest(process.stdout),
                  "stderr": process.stderr.decode(),
                  "passed": process.returncode == expected_exit and same}
        records.append(record)
        print(("PASS" if record["passed"] else "FAIL")+": "+name)

    with tempfile.TemporaryDirectory(prefix="scalar-history-bundle-") as directory:
        tree = Path(directory)
        original = tree/ORIGINAL_SUBDIR
        original.mkdir(parents=True)
        for filename in ("NEUTRAL_CONTRACT_BEFORE_EXPOSURE_v1.json",
                         "DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md",
                         "PRE_CODE_FREEZE_v1.json", "independent_exact_controls_v1.py"):
            (original/filename).write_bytes((BUNDLE/filename).read_bytes())
        run_case("independent pre-exposure mathematics", tree,
                 ORIGINAL_SUBDIR/"independent_exact_controls_v1.py", 0,
                 (BUNDLE/"independent_attempt01.stdout.json").read_bytes())

        additions = tree/"independent_additions_v1.py"
        additions.write_bytes((BUNDLE/additions.name).read_bytes())
        run_case("post-exposure independent additions", tree, additions, 0,
                 (BUNDLE/"additions_attempt01.stdout.json").read_bytes())

        historical = tree/"historical"
        historical.mkdir()
        for filename in ("NON_EQUILIBRIUM_SCALAR_INVERSE_v1.md",
                         "check_nonequilibrium_scalar_v1.py",
                         "check_nonequilibrium_scalar_v2.py"):
            (historical/filename).write_bytes((BUNDLE/"original_replay"/filename).read_bytes())
        for version, expected_exit in ((1, 1), (2, 0)):
            output = Path("historical")/f"NON_EQUILIBRIUM_SCALAR_CONTROLS_v{version}.json"
            run_case(f"preserved exploratory v{version}", tree,
                     historical/f"check_nonequilibrium_scalar_v{version}.py", expected_exit,
                     (BUNDLE/"original_replay"/output.name).read_bytes(), output)

        for filename in ("docs/SCALAR_HISTORY_COMPATIBILITY_NOTE_2026-10-16.md",
                         "scripts/scalar_history_inverse.py",
                         "scripts/scalar_history_inverse_math.py"):
            target = tree/filename
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT/filename).read_bytes())
        run_case("canonical primary", tree, Path("scripts/scalar_history_inverse.py"), 0,
                 (HERE/"result.json").read_bytes(),
                 Path("outputs/scalar_history_inverse/result.json"))

    result = {"schema": "scalar-history-portable-replay-v1",
              "scope": "Root-authored portability/reproduction; no new independent or empirical checks",
              "runner_sha256": digest(Path(__file__).read_bytes()),
              "cases": records, "passed": sum(row["passed"] for row in records),
              "failed": sum(not row["passed"] for row in records)}
    (HERE/"portable_replay.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    return int(result["failed"] != 0)


if __name__ == "__main__":
    raise SystemExit(main())
