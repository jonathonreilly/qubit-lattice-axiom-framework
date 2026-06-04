#!/usr/bin/env python3
"""Target-specific Fam2 seed-1 H=0.25 direct-dM replay certificate.

The generic point runner defaults to Fam1 seed0.  This wrapper fixes the exact
arguments used by the Fam2 seed1 follow-up row so the audit cache is tied to
the row being rechecked, not to the reusable runner's default invocation.
"""

from __future__ import annotations


AUDIT_TIMEOUT_SEC = 1800

import json
import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from wave_direct_dm_matched_history_probe import FAMILIES, measure_dm
from wave_retardation_continuum_limit import S_PHYS as SOURCE_STRENGTH_CONSTANT

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "outputs" / "wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json"

FAMILY = "Fam2"
SEED = 1
H_VALUE = 0.25
STRENGTH = SOURCE_STRENGTH_CONSTANT

EXPECTED = {
    "d_early": 0.003777,
    "d_late": 0.005814,
    "delta_hist": -0.002037,
    "r_hist": -0.3503,
    "NL": 60,
    "PW": 6.0,
    "src_layer": 20,
    "iz_start_real": 3.0,
    "iz_end_real": 0.0,
}

ARTIFACTS = [
    "scripts/wave_direct_dm_h025_point_runner.py",
    "scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py",
    "logs/2026-04-08-wave-direct-dm-h025-fam2-seed1.txt",
    "docs/WAVE_DIRECT_DM_H025_FAM2_SEED1_FOLLOWUP_NOTE.md",
    "docs/WAVE_DIRECT_DM_H025_FAM2_SEED1_CONTROL_NOTE.md",
    "docs/WAVE_DIRECT_DM_H025_FAM2_SEED0_CONTROL_NOTE.md",
    "docs/WAVE_DIRECT_DM_H025_FAM2_TWO_POINT_SYNTHESIS_NOTE.md",
    "docs/WAVE_DIRECT_DM_H025_TWO_POINT_SYNTHESIS_NOTE.md",
    "docs/WAVE_DIRECT_DM_PORTABILITY_BATCH_NOTE.md",
]


def family_specs(label: str) -> tuple[str, float, float]:
    for family_label, drift, restore in FAMILIES:
        if family_label == label:
            return family_label, drift, restore
    raise SystemExit(f"missing family fixture: {label}")


def close(actual: float, expected: float, tol: float = 5e-7) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}")
        else:
            failed += 1
            print(f"FAIL {name}")

    family_label, drift, restore = family_specs(FAMILY)
    row = measure_dm(H_VALUE, STRENGTH, family_label, drift, restore, seed=SEED)

    check("family is fixed to Fam2", family_label == "Fam2")
    check("seed is fixed to 1", SEED == 1)
    check("H is fixed to 0.25", close(H_VALUE, 0.25))
    check("source strength is fixed to 0.004", close(STRENGTH, 0.004))
    check("drift fixture matches Fam2", close(drift, 0.05))
    check("restore fixture matches Fam2", close(restore, 0.30))

    for key, expected in EXPECTED.items():
        tol = 5e-5 if key == "r_hist" else 5e-7 if isinstance(expected, float) else 0.0
        actual = row[key]
        check(f"{key} matches archived target log", close(float(actual), float(expected), tol=tol))

    late_gain = row["d_late"] - row["d_early"]
    check("late gain equals -delta_hist", close(late_gain, -row["delta_hist"]))
    check("late gain is on the seed-1 coarse scale", 0.00190 < late_gain < 0.00210)
    check("normalized response is not a stable amplitude-law promotion", row["r_hist"] < -0.30)

    for rel in ARTIFACTS:
        check(f"artifact present: {rel}", (REPO_ROOT / rel).exists())

    payload = {
        "claim_id": "wave_direct_dm_h025_fam2_seed1_followup_note",
        "runner_role": "target-specific exact invocation cache",
        "family": family_label,
        "seed": SEED,
        "h": H_VALUE,
        "strength": STRENGTH,
        "drift": drift,
        "restore": restore,
        "observables": {
            "dM_early": row["d_early"],
            "dM_late": row["d_late"],
            "delta_hist": row["delta_hist"],
            "R_hist": row["r_hist"],
            "late_gain": late_gain,
        },
        "claim_boundary": (
            "Exact Fam2 seed1 H=0.25 replay feeding controlled pair/batch "
            "surface; not an independent theorem-grade surface or portability law."
        ),
        "pass_count": passed,
        "fail_count": failed,
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print("WAVE DIRECT-DM H025 FAM2 SEED1 TARGET CERTIFICATE")
    print(f"family={family_label} drift={drift:.2f} restore={restore:.2f}")
    print(f"seed={SEED}")
    print(f"H={H_VALUE:.3f} strength={STRENGTH:.6f}")
    print(f"dM(early)  = {row['d_early']:+.6f}")
    print(f"dM(late)   = {row['d_late']:+.6f}")
    print(f"delta_hist = {row['delta_hist']:+.6f}")
    print(f"R_hist     = {row['r_hist']:+.2%}")
    print(f"late_gain  = {late_gain:+.6f}")
    print(f"OUTPUT_JSON={OUTPUT_PATH.relative_to(REPO_ROOT)}")
    print(f"SUMMARY: WAVE H025 FAM2 SEED1 PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
