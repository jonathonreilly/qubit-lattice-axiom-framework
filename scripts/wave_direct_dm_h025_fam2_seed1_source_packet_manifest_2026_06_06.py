#!/usr/bin/env python3
"""Restricted source-packet manifest for the Wave direct-dM Fam2 seed1 row."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

CLAIM_ID = "wave_direct_dm_h025_fam2_seed1_followup_note"
NOTE = "docs/WAVE_DIRECT_DM_H025_FAM2_SEED1_FOLLOWUP_NOTE.md"
OUTPUT = REPO_ROOT / "outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json"

MANIFEST = {
    "note": NOTE,
    "target_runner": "scripts/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.py",
    "target_cache": "logs/runner-cache/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.txt",
    "target_json": "outputs/wave_direct_dm_h025_fam2_seed1_point_runner_2026_06_04.json",
    "generic_point_runner": "scripts/wave_direct_dm_h025_point_runner.py",
    "generic_point_runner_cache": "logs/runner-cache/wave_direct_dm_h025_point_runner.txt",
    "measure_dm_source": "scripts/wave_direct_dm_matched_history_probe.py",
    "measure_dm_cache": "logs/runner-cache/wave_direct_dm_matched_history_probe.txt",
    "continuum_helper_source": "scripts/wave_retardation_continuum_limit.py",
    "continuum_helper_cache": "logs/runner-cache/wave_retardation_continuum_limit.txt",
}

NOTE_LINKS = {
    "manifest_runner": "scripts/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.py",
    "manifest_cache": "logs/runner-cache/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.txt",
    "manifest_json": "outputs/wave_direct_dm_h025_fam2_seed1_source_packet_manifest_2026_06_06.json",
}

REQUIRED_SOURCE_MARKERS = {
    "target_runner": [
        "FAMILY = \"Fam2\"",
        "SEED = 1",
        "H_VALUE = 0.25",
        "from wave_direct_dm_matched_history_probe import FAMILIES, measure_dm",
        "from wave_retardation_continuum_limit import S_PHYS",
        "EXPECTED = {",
        "SUMMARY: WAVE H025 FAM2 SEED1 PASS",
    ],
    "generic_point_runner": [
        "from wave_direct_dm_matched_history_probe import FAMILIES, measure_dm",
        "from wave_retardation_continuum_limit import S_PHYS",
    ],
    "measure_dm_source": [
        "from wave_retardation_continuum_limit import",
        "def measure_dm",
        "free = prop_beam",
        "z_free = cz",
        "h_early = solve_wave",
        "h_late = solve_wave",
    ],
    "continuum_helper_source": [
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
    "target_runner": 4_000,
    "generic_point_runner": 1_000,
    "measure_dm_source": 5_000,
    "continuum_helper_source": 20_000,
}

EXPECTED_CACHE_SNIPPETS = {
    "target_cache": [
        "status: ok",
        "PASS family is fixed to Fam2",
        "PASS seed is fixed to 1",
        "PASS H is fixed to 0.25",
        "dM(early)  = +0.003777",
        "dM(late)   = +0.005814",
        "delta_hist = -0.002037",
        "MEASURE_DM_SOURCE_PACKET=PASS",
        "SUMMARY: WAVE H025 FAM2 SEED1 PASS=33 FAIL=0",
    ],
    "generic_point_runner_cache": [
        "status: ok",
        "WAVE DIRECT-DM SINGLE-POINT RUNNER",
        "dM(early)  =",
        "dM(late)   =",
        "delta_hist =",
    ],
    "measure_dm_cache": [
        "status: ok",
        "WAVE DIRECT-DM MATCHED-HISTORY PROBE",
        "Two source schedules with the same start/end/final geometry",
        "[strength=0.004000]",
    ],
    "continuum_helper_cache": [
        "status: ok",
        "WAVE-RETARDATION CONTINUUM-LIMIT REFINEMENT",
        "S_phys (field source strength) = 0.004",
        "[fine] H = 0.25",
        "dM = +0.007212",
        "PARTIAL",
    ],
}

CACHE_TO_SOURCE = {
    "target_cache": "target_runner",
    "generic_point_runner_cache": "generic_point_runner",
    "measure_dm_cache": "measure_dm_source",
    "continuum_helper_cache": "continuum_helper_source",
}


def repo_path(rel_path: str) -> Path:
    return REPO_ROOT / rel_path


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


def check(condition: bool, name: str, detail: str, results: list[dict]) -> None:
    results.append({"name": name, "pass": bool(condition), "detail": detail})


def main() -> int:
    results: list[dict] = []
    note_text = repo_path(NOTE).read_text(encoding="utf-8")

    for label, rel_path in MANIFEST.items():
        path = repo_path(rel_path)
        check(path.exists(), f"manifest_path_exists:{label}", rel_path, results)
        if label != "note":
            check(
                rel_path in note_text,
                f"note_names_manifest_path:{label}",
                f"{rel_path} is named in {NOTE}",
                results,
            )

    for label, rel_path in NOTE_LINKS.items():
        check(
            rel_path in note_text,
            f"note_names_manifest_artifact:{label}",
            f"{rel_path} is named in {NOTE}",
            results,
        )

    for label, markers in REQUIRED_SOURCE_MARKERS.items():
        source_path = repo_path(MANIFEST[label])
        source = source_path.read_text(encoding="utf-8")
        check(
            len(source) > MIN_SOURCE_BYTES[label],
            f"source_untruncated:{label}",
            f"{MANIFEST[label]} has {len(source)} bytes",
            results,
        )
        for marker in markers:
            check(
                marker in source,
                f"source_marker:{label}:{marker}",
                f"{marker} present in {MANIFEST[label]}",
                results,
            )

    for cache_label, source_label in CACHE_TO_SOURCE.items():
        cache_path = repo_path(MANIFEST[cache_label])
        source_rel = MANIFEST[source_label]
        header = parse_cache_header(cache_path)
        current_sha = sha256_file(repo_path(source_rel))
        check(
            header.get("runner") == source_rel,
            f"cache_runner_matches:{cache_label}",
            f"{header.get('runner')} == {source_rel}",
            results,
        )
        check(
            header.get("runner_sha256") == current_sha,
            f"cache_sha_fresh:{cache_label}",
            f"cache sha {header.get('runner_sha256')} current sha {current_sha}",
            results,
        )
        check(
            header.get("exit_code") == "0" and header.get("status") == "ok",
            f"cache_exit_ok:{cache_label}",
            f"exit_code={header.get('exit_code')} status={header.get('status')}",
            results,
        )
        for snippet in EXPECTED_CACHE_SNIPPETS[cache_label]:
            check(
                snippet in header["_text"],
                f"cache_contains:{cache_label}:{snippet}",
                snippet,
                results,
            )

    check(
        "2026-06-06 transitive helper source-packet repair" in note_text,
        "note_has_transitive_helper_repair_section",
        "wave note has the 2026-06-06 helper repair section",
        results,
    )
    check(
        "does not promote this note" in note_text,
        "note_preserves_bounded_boundary",
        "repair section states that status movement remains audit-owned",
        results,
    )

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count

    print("=" * 88)
    print("WAVE DIRECT-DM H025 FAM2 SEED1: TRANSITIVE SOURCE PACKET MANIFEST")
    print("=" * 88)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 88)
    print(f"SUMMARY: WAVE SOURCE PACKET PASS={pass_count} FAIL={fail_count}")
    print("=" * 88)

    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "claim_id": CLAIM_ID,
                "note": NOTE,
                "manifest": {**MANIFEST, **NOTE_LINKS},
                "summary": {"pass": pass_count, "fail": fail_count},
                "results": results,
                "status_boundary": (
                    "bounded-support source-packet repair only; independent "
                    "audit owns any ledger/status movement"
                ),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Output written: {OUTPUT.relative_to(REPO_ROOT)}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
