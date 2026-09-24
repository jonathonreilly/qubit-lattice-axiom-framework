#!/usr/bin/env python3
"""Current-source scratch-copy mutations for the five-site primary runner."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts/postmark_electric_five_site_inter_fiber_phase_2026_09_24.py"
NOTE = ROOT / "docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md"
OUT = Path(__file__).resolve().parent / "five_site"
OUT.mkdir(parents=True, exist_ok=True)

MUTATIONS = (
    ("wrong_five_site_left_offset", "ELL = (0, 1, 0, 1, 1)",
     "ELL = (0, 2, 0, 1, 1)"),
    ("wrong_period_three_fiber_index", "transformed[(k - 2) % cells]",
     "transformed[(k - 1) % cells]"),
    ("wrong_bragg_principal_slope",
     "4 * (rt5 - 1) * sp.Abs(u) / 5,\n         (1-u**2) * root_plus / 5)",
     "4 * (rt5 - 1) * sp.Abs(u) / 5,\n         (1-u**2) * root_plus / 6)"),
)


def main() -> int:
    results = []
    for name, before, after in MUTATIONS:
        with tempfile.TemporaryDirectory(prefix=f"mutation_{name}_") as temp:
            scratch = Path(temp)
            source_copy = scratch / "scripts" / RUNNER.name
            source_copy.parent.mkdir(parents=True)
            shutil.copy2(RUNNER, source_copy)
            text = source_copy.read_text()
            if text.count(before) != 1:
                raise RuntimeError((name, "expected unique mutation anchor", text.count(before)))
            source_copy.write_text(text.replace(before, after, 1))

            # Copy every declared provenance input so the scratch run remains
            # self-contained and fails only on the intended mutated check.
            for rel in (
                "docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
                "docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
                "docs/MINIMAL_AXIOMS_2026-06-29.md",
                "docs/POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md",
                "docs/POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md",
                "docs/POSTMARK_ELECTRIC_MOVING_INDEX_CELL_SYMBOL_BOUNDED_THEOREM_NOTE_2026-09-24.md",
                "docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
                "scripts/core_derivation.py",
            ):
                target = scratch / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / rel, target)

            completed = subprocess.run(
                [sys.executable, str(source_copy)], cwd=scratch,
                capture_output=True, text=True, timeout=300,
            )
        log = OUT / f"{name}.log"
        log.write_text(completed.stdout + "\n--- stderr ---\n" + completed.stderr)
        failure = next((line.strip() for line in reversed(completed.stderr.splitlines())
                        if line.strip()), "")
        results.append({
            "mutation": name,
            "exit_code": completed.returncode,
            "expected_failure_observed": completed.returncode != 0,
            "failure_signature": failure,
            "log": str(log.relative_to(ROOT)),
        })

    report = {
        "source_revision": "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8",
        "runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
        "note_sha256": hashlib.sha256(NOTE.read_bytes()).hexdigest(),
        "mutations": results,
        "all_expected_failures_observed": all(r["expected_failure_observed"] for r in results),
        "interpretation": "Scratch-copy sensitivity checks only; they are not independent validation of the unmutated formulas.",
    }
    target = OUT / "MUTATION_CHECKS.json"
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in (
        "source_revision", "runner_sha256", "note_sha256",
        "all_expected_failures_observed")}, indent=2))
    return 0 if report["all_expected_failures_observed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
