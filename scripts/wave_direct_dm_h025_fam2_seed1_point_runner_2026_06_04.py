#!/usr/bin/env python3
"""Target-specific Fam2 seed-1 H=0.25 direct-dM replay certificate.

The generic point runner defaults to Fam1 seed0.  This wrapper fixes the exact
arguments used by the Fam2 seed1 follow-up row so the audit cache is tied to
the row being rechecked, not to the reusable runner's default invocation.
"""

from __future__ import annotations


AUDIT_TIMEOUT_SEC = 1800

import json
import hashlib
import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from wave_direct_dm_matched_history_probe import FAMILIES, measure_dm
from wave_retardation_continuum_limit import S_PHYS as SOURCE_STRENGTH_CONSTANT

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = REPO_ROOT / "outputs" / "wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json"
NOTE_PATH = REPO_ROOT / "docs" / "WAVE_DIRECT_DM_H025_FAM2_SEED1_FOLLOWUP_NOTE.md"
MANIFEST_CACHE = REPO_ROOT / "logs" / "runner-cache" / "wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.txt"
MANIFEST_JSON = REPO_ROOT / "outputs" / "wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json"

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

SOURCE_PACKET_PATHS = [
    "scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py",
    "logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt",
    "outputs/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json",
    "scripts/wave_direct_dm_h025_point_runner.py",
    "logs/runner-cache/wave_direct_dm_h025_point_runner.txt",
    "scripts/wave_direct_dm_matched_history_probe.py",
    "logs/runner-cache/wave_direct_dm_matched_history_probe.txt",
    "scripts/wave_retardation_continuum_limit.py",
    "logs/runner-cache/wave_retardation_continuum_limit.txt",
    "scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py",
    "logs/runner-cache/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.txt",
    "outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json",
]

SOURCE_MARKERS = {
    "scripts/wave_direct_dm_matched_history_probe.py": [
        "from wave_retardation_continuum_limit import",
        "def measure_dm",
        "free = prop_beam",
        "z_free = cz",
        "h_early = solve_wave",
        "h_late = solve_wave",
    ],
    "scripts/wave_retardation_continuum_limit.py": [
        "S_PHYS = 0.004",
        "def grow",
        "def solve_wave",
        "def field_at",
        "def prop_beam",
        "field[idx] = field_at",
        "def cz",
    ],
}

MIN_SOURCE_BYTES = {
    "scripts/wave_direct_dm_matched_history_probe.py": 5_000,
    "scripts/wave_retardation_continuum_limit.py": 20_000,
}

CACHE_TO_RUNNER = {
    "logs/runner-cache/wave_direct_dm_h025_point_runner.txt": (
        "scripts/wave_direct_dm_h025_point_runner.py",
        "WAVE DIRECT-DM SINGLE-POINT RUNNER",
    ),
    "logs/runner-cache/wave_direct_dm_matched_history_probe.txt": (
        "scripts/wave_direct_dm_matched_history_probe.py",
        "WAVE DIRECT-DM MATCHED-HISTORY PROBE",
    ),
    "logs/runner-cache/wave_retardation_continuum_limit.txt": (
        "scripts/wave_retardation_continuum_limit.py",
        "WAVE-RETARDATION CONTINUUM-LIMIT REFINEMENT",
    ),
}


def family_specs(label: str) -> tuple[str, float, float]:
    for family_label, drift, restore in FAMILIES:
        if family_label == label:
            return family_label, drift, restore
    raise SystemExit(f"missing family fixture: {label}")


def close(actual: float, expected: float, tol: float = 5e-7) -> bool:
    return math.isclose(actual, expected, rel_tol=0.0, abs_tol=tol)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_cache_header(cache_path: Path) -> dict[str, str]:
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    fields: dict[str, str] = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def inline_source_packet_checks() -> tuple[int, int]:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str = "") -> None:
        nonlocal passed, failed
        status = "PASS" if condition else "FAIL"
        if condition:
            passed += 1
        else:
            failed += 1
        suffix = f": {detail}" if detail else ""
        print(f"[{status}] {name}{suffix}")

    note_text = NOTE_PATH.read_text(encoding="utf-8")

    for rel_path in SOURCE_PACKET_PATHS:
        path = REPO_ROOT / rel_path
        check(f"packet path exists: {rel_path}", path.exists())
        check(f"note links packet path: {rel_path}", rel_path in note_text)

    for rel_path, markers in SOURCE_MARKERS.items():
        source_path = REPO_ROOT / rel_path
        source_text = source_path.read_text(encoding="utf-8")
        check(
            f"source appears untruncated: {rel_path}",
            len(source_text) > MIN_SOURCE_BYTES[rel_path],
            f"{len(source_text)} bytes",
        )
        for marker in markers:
            check(
                f"source marker present in {rel_path}",
                marker in source_text,
                marker,
            )

    for cache_rel, (runner_rel, expected_marker) in CACHE_TO_RUNNER.items():
        cache_path = REPO_ROOT / cache_rel
        header = parse_cache_header(cache_path)
        current_sha = sha256_file(REPO_ROOT / runner_rel)
        check(
            f"cache runner matches source: {cache_rel}",
            header.get("runner") == runner_rel,
            runner_rel,
        )
        check(
            f"cache SHA fresh: {cache_rel}",
            header.get("runner_sha256") == current_sha,
            f"{header.get('runner_sha256')} == {current_sha}",
        )
        check(
            f"cache exits cleanly: {cache_rel}",
            header.get("exit_code") == "0" and header.get("status") == "ok",
            f"exit_code={header.get('exit_code')} status={header.get('status')}",
        )
        check(
            f"cache contains expected marker: {cache_rel}",
            expected_marker in header["_text"],
            expected_marker,
        )

    manifest_header = parse_cache_header(MANIFEST_CACHE)
    check(
        "source-packet manifest cache reports zero failures",
        "SUMMARY: WAVE SOURCE PACKET PASS=85 FAIL=0" in manifest_header["_text"],
    )
    check(
        "source-packet manifest JSON exists",
        MANIFEST_JSON.exists(),
        str(MANIFEST_JSON.relative_to(REPO_ROOT)),
    )
    if MANIFEST_JSON.exists():
        payload = json.loads(MANIFEST_JSON.read_text(encoding="utf-8"))
        summary = payload.get("summary", {})
        check(
            "source-packet manifest JSON reports zero failures",
            summary.get("fail") == 0 and summary.get("pass") == 85,
            str(summary),
        )

    print(f"INLINE SOURCE PACKET: PASS={passed} FAIL={failed}")
    return passed, failed


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
    _inline_passed, inline_failed = inline_source_packet_checks()
    return 0 if failed == 0 and inline_failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
