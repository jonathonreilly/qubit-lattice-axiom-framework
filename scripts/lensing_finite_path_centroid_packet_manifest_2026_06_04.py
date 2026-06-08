#!/usr/bin/env python3
"""Restricted-packet manifest for the lensing finite-path open gate.

This runner does not re-audit the row or promote its status. It checks that the
finite-path note exposes the long-path falsification runner/cache and that the
two cached computations are SHA-pinned to the current source files. It also
checks the narrow detector-centroid facts that the previous audits named as
missing from the restricted packet.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

CLAIM_ID = "lensing_finite_path_explanation_note"
NOTE = "docs/LENSING_FINITE_PATH_EXPLANATION_NOTE.md"

MANIFEST = {
    "finite_path_note": NOTE,
    "long_path_note": "docs/LENSING_LONG_PATH_TEST_NOTE.md",
    "finite_path_runner": "scripts/lensing_analytical_finite_path.py",
    "long_path_runner": "scripts/lensing_long_path_test.py",
    "finite_path_cache": "logs/runner-cache/lensing_analytical_finite_path.txt",
    "long_path_cache": "logs/runner-cache/lensing_long_path_test.txt",
    "finite_path_legacy_log": "logs/2026-04-07-lensing-analytical-finite-path.txt",
    "long_path_legacy_log": "logs/2026-04-07-lensing-long-path-test.txt",
}

NOTE_LINKS = {
    "manifest_runner": "scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py",
    "manifest_cache": "logs/runner-cache/lensing_finite_path_centroid_packet_manifest_2026_06_04.txt",
    "manifest_json": "outputs/lensing_finite_path_centroid_packet_manifest_2026_06_04.json",
}

REQUIRED_SOURCE_MARKERS = {
    "finite_path_runner": [
        "def alpha_centered_surrogate",
        "def alpha_full_path_reg",
        "def shift_weighted_reg",
        "MEASUREMENTS =",
        "x_src = 5.0",
        "x_det = 14.75",
        "detector-shift proxy",
    ],
    "long_path_runner": [
        "AUDIT_TIMEOUT_SEC = 1800",
        "from kubo_continuum_limit import",
        "T_PHYS_LONG = 45.0",
        "T_PHYS_SHORT = 7.5",
        "B_VALUES = [3.0, 4.0, 5.0, 6.0]",
        "def measure_at",
        "true_kubo_at_H",
    ],
}

EXPECTED_CACHE_SNIPPETS = {
    "finite_path_cache": [
        "status: ok",
        "measured H=0.25                 -1.4335",
        "centered L=10 surrogate         -1.4188",
        "actual full path (+0.1)         -1.2425",
        "shift-weighted full path        -1.3400",
        "The actual static-mass full-path",
    ],
    "long_path_cache": [
        "status: ok",
        "T_phys = 45.0",
        "T_phys = 7.5",
        "H=0.25 kubo_true:        slope = -1.4356",
        "analytical (no fit):    slope = -1.7336",
        "H=0.5 kubo_true:        slope = -1.8128",
        "POOR MATCH",
    ],
}

CACHE_TO_RUNNER = {
    "finite_path_cache": "finite_path_runner",
    "long_path_cache": "long_path_runner",
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
    results.append({"name": name, "pass": bool(condition), "detail": detail})


def main() -> int:
    results: list[dict] = []
    note_text = repo_path(NOTE).read_text(encoding="utf-8")

    for label, rel_path in MANIFEST.items():
        path = repo_path(rel_path)
        check(path.exists(), f"manifest_path_exists:{label}", rel_path, results)
        if label != "finite_path_note":
            check(
                rel_path in note_text,
                f"finite_path_note_names_manifest_path:{label}",
                f"{rel_path} is named in {NOTE}",
                results,
            )
    for label, rel_path in NOTE_LINKS.items():
        check(
            rel_path in note_text,
            f"finite_path_note_names_manifest_artifact:{label}",
            f"{rel_path} is named in {NOTE}",
            results,
        )

    long_note_text = repo_path(MANIFEST["long_path_note"]).read_text(encoding="utf-8")
    check(
        "Falsifies: [`LENSING_FINITE_PATH_EXPLANATION_NOTE.md`]" in long_note_text,
        "long_path_note_points_back_to_finite_path_note",
        "long-path note names finite-path note as falsified target",
        results,
    )

    for label, markers in REQUIRED_SOURCE_MARKERS.items():
        source = repo_path(MANIFEST[label]).read_text(encoding="utf-8")
        check(
            len(source) > 4500,
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

    for cache_label, runner_label in CACHE_TO_RUNNER.items():
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
        for snippet in EXPECTED_CACHE_SNIPPETS[cache_label]:
            check(
                snippet in header["_text"],
                f"cache_contains:{cache_label}:{snippet}",
                snippet,
                results,
            )

    check(
        "2026-06-04 Source Packet Re-audit Repair" in note_text,
        "note_has_source_packet_reaudit_section",
        "finite-path note has the 2026-06-04 repair section",
        results,
    )
    check(
        "does not promote this row" in note_text,
        "note_preserves_open_gate_boundary",
        "repair section states that status movement remains audit-owned",
        results,
    )
    check(
        "Centered Finite-Path Surrogate Negative Boundary" in note_text,
        "note_has_negative_boundary_title",
        "finite-path note is narrowed to a negative boundary packet",
        results,
    )
    check(
        "does not claim a positive explanation" in note_text,
        "note_disclaims_positive_explanation",
        "finite-path note disclaims positive detector-centroid explanation",
        results,
    )
    check(
        "claim_type: no_go" in note_text or "**Claim type:** no_go" in note_text,
        "note_registers_no_go_claim_type",
        "audit registration records no_go claim type",
        results,
    )
    check(
        "detector-centroid" in note_text and "layer-weighted" in note_text,
        "note_names_remaining_centroid_bridge",
        "note keeps the centroid/layer-weighted bridge visible",
        results,
    )

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count

    print("=" * 78)
    print("LENSING FINITE-PATH: RESTRICTED SOURCE PACKET MANIFEST")
    print("=" * 78)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 78)
    print(f"SUMMARY: LENSING SOURCE PACKET PASS={pass_count} FAIL={fail_count}")
    print("=" * 78)

    out_dir = repo_path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "lensing_finite_path_centroid_packet_manifest_2026_06_04.json"
    out_path.write_text(
        json.dumps(
            {
                "claim_id": CLAIM_ID,
                "note": NOTE,
                "manifest": MANIFEST,
                "summary": {"pass": pass_count, "fail": fail_count},
                "results": results,
                "status_boundary": (
                    "open_gate packet-completeness repair only; independent "
                    "audit owns any ledger/status movement"
                ),
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
