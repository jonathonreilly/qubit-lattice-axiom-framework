#!/usr/bin/env python3
"""Source-packet manifest for the Fam2 seed-1 H=0.25 wave direct-dM row."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json"

PATHS = {
    "target_runner": "scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py",
    "target_runner_cache": "logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt",
    "generic_point_runner": "scripts/wave_direct_dm_h025_point_runner.py",
    "generic_point_runner_cache": "logs/runner-cache/wave_direct_dm_h025_point_runner.txt",
    "matched_history_helper": "scripts/wave_direct_dm_matched_history_probe.py",
    "matched_history_helper_cache": "logs/runner-cache/wave_direct_dm_matched_history_probe.txt",
    "wave_retardation_helper": "scripts/wave_retardation_continuum_limit.py",
    "wave_retardation_helper_cache": "logs/runner-cache/wave_retardation_continuum_limit.txt",
}

MARKERS = {
    "target_runner": [
        "FAMILY = \"Fam2\"",
        "SEED = 1",
        "H_VALUE = 0.25",
        "from wave_direct_dm_matched_history_probe import FAMILIES, measure_dm",
        "from wave_retardation_continuum_limit import S_PHYS as SOURCE_STRENGTH_CONSTANT",
    ],
    "generic_point_runner": ["from wave_direct_dm_matched_history_probe import FAMILIES, measure_dm"],
    "matched_history_helper": [
        "from wave_retardation_continuum_limit import (",
        "def measure_dm(",
        "prop_beam(",
        "cz(",
    ],
    "wave_retardation_helper": [
        "def field_at(",
        "def prop_beam(",
        "def cz(",
        "def solve_wave(",
        "def grow(",
    ],
}

CACHE_SNIPPETS = {
    "target_runner_cache": "SUMMARY: WAVE H025 FAM2 SEED1 PASS=27 FAIL=0",
    "generic_point_runner_cache": "WAVE DIRECT-DM SINGLE-POINT RUNNER",
    "matched_history_helper_cache": "DIRECT-DM MATCHED-HISTORY PROBE",
    "wave_retardation_helper_cache": "WAVE-RETARDATION CONTINUUM-LIMIT REFINEMENT",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in text.splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value
    return fields


def main() -> int:
    passed = 0
    failed = 0
    checks: list[dict[str, object]] = []
    note_path = ROOT / "docs/WAVE_DIRECT_DM_H025_FAM2_SEED1_FOLLOWUP_NOTE.md"
    note = note_path.read_text()

    def check(name: str, ok: bool, detail: str) -> None:
        nonlocal passed, failed
        checks.append({"name": name, "ok": ok, "detail": detail})
        if ok:
            passed += 1
            print(f"[PASS] {name}: {detail}")
        else:
            failed += 1
            print(f"[FAIL] {name}: {detail}")

    for label, rel in PATHS.items():
        path = ROOT / rel
        check(f"path_exists:{label}", path.exists(), rel)
        check(f"note_links:{label}", rel in note, rel)

    for label, snippets in MARKERS.items():
        rel = PATHS[label]
        text = (ROOT / rel).read_text()
        check(f"source_untruncated:{label}", len(text) > 1000, f"{rel} bytes={len(text)}")
        for snippet in snippets:
            check(f"source_marker:{label}:{snippet}", snippet in text, snippet)

    for label, snippet in CACHE_SNIPPETS.items():
        cache_rel = PATHS[label]
        runner_rel = cache_rel.removeprefix("logs/runner-cache/").removesuffix(".txt")
        cache = (ROOT / cache_rel).read_text()
        fields = cache_fields(cache)
        runner = fields.get("runner", "")
        runner_path = ROOT / runner
        check(f"cache_runner_present:{label}", runner_path.exists(), runner)
        if runner_path.exists():
            check(
                f"cache_sha_fresh:{label}",
                fields.get("runner_sha256") == sha256(runner_path),
                f"{fields.get('runner_sha256')} == {sha256(runner_path)}",
            )
        check(f"cache_exit_ok:{label}", fields.get("exit_code") == "0", f"exit_code={fields.get('exit_code')}")
        check(f"cache_status_ok:{label}", fields.get("status") == "ok", f"status={fields.get('status')}")
        check(f"cache_snippet:{label}", snippet in cache, snippet)
        check(f"cache_name_consistent:{label}", runner_rel in runner, f"{runner_rel} in {runner}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "claim_id": "wave_direct_dm_h025_fam2_seed1_followup_note",
                "pass_count": passed,
                "fail_count": failed,
                "paths": PATHS,
                "checks": checks,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    print("=" * 88)
    print(f"SUMMARY: WAVE FAM2 SEED1 SOURCE PACKET PASS={passed} FAIL={failed}")
    print(f"OUTPUT_JSON={OUTPUT.relative_to(ROOT)}")
    print("=" * 88)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
