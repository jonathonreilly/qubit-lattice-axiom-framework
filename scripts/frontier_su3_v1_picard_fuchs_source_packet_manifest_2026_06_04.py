#!/usr/bin/env python3
"""Source-packet manifest verifier for the V=1 SU(3) Picard-Fuchs row.

This runner does not re-audit the claim. It checks that the note exposes the
complete primary/helper source packet and that each cached runner output is
SHA-pinned to the current source file on disk.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

NOTE = "docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_RANK_BOUND_CITATION_NOTE_2026-05-06.md"
MANIFEST = {
    "primary_all_order_runner": "scripts/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.py",
    "finite_window_helper_runner": "scripts/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.py",
    "extended_minimality_helper_runner": "scripts/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.py",
    "original_ode_runner": "scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py",
    "all_order_cache": "logs/runner-cache/frontier_su3_v1_picard_fuchs_ode_all_order_certificate_2026_05_09.txt",
    "finite_window_cache": "logs/runner-cache/frontier_su3_v1_picard_fuchs_minimality_2026_05_06.txt",
    "extended_minimality_cache": "logs/runner-cache/frontier_su3_v1_picard_fuchs_minimality_extended_2026_05_06.txt",
    "all_order_json": "outputs/su3_v1_picard_fuchs_all_order_certificate_2026_05_09.json",
    "finite_window_json": "outputs/su3_v1_picard_fuchs_minimality_2026_05_06.json",
    "extended_minimality_json": "outputs/su3_v1_picard_fuchs_minimality_extended_2026_05_06.json",
}

REQUIRED_SOURCE_MARKERS = {
    "primary_all_order_runner": [
        "def certificate_T1_dfiniteness_witness",
        "def certificate_T2_algorithmic_rank_bound",
        "def certificate_T3_bostan_schost_threshold",
        "from frontier_su3_v1_picard_fuchs_minimality_2026_05_06 import",
    ],
    "finite_window_helper_runner": [
        "def matrix_for_ansatz",
        "def _rank_via_numeric",
        "def certificate_B",
        "def certificate_C",
        "def certificate_E",
    ],
    "extended_minimality_helper_runner": [
        "def matrix_for_ansatz",
        "def _rank_via_numeric",
        "def certificate_B_extended",
        "def certificate_E_extended",
        "def certificate_S",
    ],
}

EXPECTED_CACHE_SUMMARIES = {
    "all_order_cache": "SUMMARY: FINITE-WINDOW BOUNDARY PASS=5 FAIL=0",
    "finite_window_cache": "SUMMARY: CERTIFICATE PASS=5 FAIL=0",
    "extended_minimality_cache": "SUMMARY: CERTIFICATE PASS=6 FAIL=0",
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
    out: dict[str, str] = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def check(condition: bool, name: str, detail: str, results: list[dict]) -> None:
    results.append(
        {
            "name": name,
            "pass": bool(condition),
            "detail": detail,
        }
    )


def main() -> int:
    results: list[dict] = []

    note_text = repo_path(NOTE).read_text(encoding="utf-8")
    for label, rel_path in MANIFEST.items():
        path = repo_path(rel_path)
        check(path.exists(), f"manifest_path_exists:{label}", rel_path, results)
        check(
            rel_path in note_text,
            f"note_links_manifest_path:{label}",
            f"{rel_path} is linked or named in {NOTE}",
            results,
        )

    for label, markers in REQUIRED_SOURCE_MARKERS.items():
        source_path = repo_path(MANIFEST[label])
        source = source_path.read_text(encoding="utf-8")
        check(
            len(source) > 5000,
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

    cache_to_runner = {
        "all_order_cache": "primary_all_order_runner",
        "finite_window_cache": "finite_window_helper_runner",
        "extended_minimality_cache": "extended_minimality_helper_runner",
    }
    for cache_label, runner_label in cache_to_runner.items():
        cache_path = repo_path(MANIFEST[cache_label])
        runner_rel = MANIFEST[runner_label]
        header = parse_cache_header(cache_path)
        current_sha = sha256_file(repo_path(runner_rel))
        check(
            header.get("runner") == runner_rel,
            f"cache_runner_matches:{cache_label}",
            f"{header.get('runner')} == {runner_rel}",
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
        expected_summary = EXPECTED_CACHE_SUMMARIES[cache_label]
        check(
            expected_summary in header["_text"],
            f"cache_summary_present:{cache_label}",
            expected_summary,
            results,
        )

    all_order_json = json.loads(repo_path(MANIFEST["all_order_json"]).read_text())
    check(
        all_order_json["summary"]["finite_window_boundary_passed"] is True,
        "all_order_json_finite_window_boundary_passes",
        "summary.finite_window_boundary_passed is true",
        results,
    )
    check(
        all_order_json["summary"]["all_order_certificate_passed"] is False,
        "all_order_json_all_order_not_certified",
        "summary.all_order_certificate_passed is false",
        results,
    )
    check(
        all_order_json["summary"]["all_degree_minimality_certified"] is False,
        "all_order_json_all_degree_minimality_not_certified",
        "summary.all_degree_minimality_certified is false",
        results,
    )
    check(
        all_order_json["certificate_T3_bostan_schost_threshold"]["details"][
            "Bostan_Schost_threshold_M_0"
        ]
        == 17,
        "all_order_json_threshold",
        "T3 Bostan-Salvy-Schost threshold is 17",
        results,
    )

    manifest_section = re.search(
        r"## 2026-06-04 Source Packet Exposure Repair\b", note_text
    )
    check(
        manifest_section is not None,
        "note_has_2026_06_04_source_packet_section",
        "source packet exposure section present",
        results,
    )

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count

    print("=" * 78)
    print("V=1 SU(3) Wilson Picard-Fuchs: SOURCE PACKET MANIFEST")
    print("=" * 78)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 78)
    print(f"SUMMARY: SOURCE PACKET MANIFEST PASS={pass_count} FAIL={fail_count}")
    print("=" * 78)

    out_dir = repo_path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "su3_v1_picard_fuchs_source_packet_manifest_2026_06_04.json"
    out_path.write_text(
        json.dumps(
            {
                "claim_id": "plaquette_v1_picard_fuchs_ode_rank_bound_citation_note_2026-05-06",
                "note": NOTE,
                "manifest": MANIFEST,
                "summary": {"pass": pass_count, "fail": fail_count},
                "results": results,
                "audit_status_authority": "independent audit lane only",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Output written: {out_path.relative_to(REPO_ROOT)}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
