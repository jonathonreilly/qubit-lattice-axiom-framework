#!/usr/bin/env python3
"""Restricted source-packet manifest for the meson OS-transfer note.

This runner does not re-audit the row or promote its status. It checks that
the meson note exposes the full primary runner source, a SHA-fresh cache for
that source, and the packet-level manifest artifacts needed to inspect the
Berezin/operator kernel-build path named by the conditional audit blocker.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent

CLAIM_ID = "meson_gauge_invariant_os_transfer_representation_bounded_note_2026-05-30"
NOTE = "docs/MESON_GAUGE_INVARIANT_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md"

MANIFEST = {
    "note": NOTE,
    "primary_runner": "scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py",
    "primary_cache": "logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt",
}

NOTE_LINKS = {
    "manifest_runner": "scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py",
    "manifest_cache": "logs/runner-cache/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.txt",
    "manifest_json": "outputs/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.json",
}

REQUIRED_SOURCE_FRAGMENTS = [
    "def block_metric_per_mode",
    "def block_fwd_propagator_berezin",
    "def block_metric_spacetime_eigs",
    "def meson_correlator_full_berezin",
    "def u_averaged_meson",
    "det(M[U]) is ACTUALLY applied",
    "print(f\"SCORECARD PASS={npass} FAIL={nfail}\")",
]

EXPECTED_CACHE_SNIPPETS = [
    "status: ok",
    "P_block : Gf Berezin(M^-1) vs operator(e^-2H)",
    "P1      : per-config Berezin(4-ferm) == operator meson",
    "P0      : det-weighted avg Berezin == operator meson",
    "K2 BREAK: per-mode-factorized Berezin gap",
    "K5 GAUGE: Wilson-line covariance residual",
    "This verifies the gauge-invariant, NUMBER-CONSERVING MESON Berezin==operator",
    "SCORECARD PASS=64 FAIL=0",
]


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

    source_path = repo_path(MANIFEST["primary_runner"])
    source = source_path.read_text(encoding="utf-8")
    check(
        len(source) > 30_000,
        "source_full_length:primary_runner",
        f"{MANIFEST['primary_runner']} has {len(source)} bytes",
        results,
    )
    for fragment in REQUIRED_SOURCE_FRAGMENTS:
        check(
            fragment in source,
            f"source_contains:primary_runner:{fragment}",
            f"{fragment} present in {MANIFEST['primary_runner']}",
            results,
        )

    cache_path = repo_path(MANIFEST["primary_cache"])
    header = parse_cache_header(cache_path)
    current_sha = sha256_file(source_path)
    check(
        header.get("runner") == MANIFEST["primary_runner"],
        "cache_runner_matches:primary_cache",
        f"{header.get('runner')} == {MANIFEST['primary_runner']}",
        results,
    )
    check(
        header.get("runner_sha256") == current_sha,
        "cache_sha_fresh:primary_cache",
        f"cache sha {header.get('runner_sha256')} current sha {current_sha}",
        results,
    )
    check(
        header.get("exit_code") == "0" and header.get("status") == "ok",
        "cache_exit_ok:primary_cache",
        f"exit_code={header.get('exit_code')} status={header.get('status')}",
        results,
    )
    for snippet in EXPECTED_CACHE_SNIPPETS:
        check(
            snippet in header["_text"],
            f"cache_contains:primary_cache:{snippet}",
            snippet,
            results,
        )

    check(
        "2026-06-06 Source Packet Re-audit Repair" in note_text,
        "note_has_source_packet_reaudit_section",
        "meson note has the 2026-06-06 repair section",
        results,
    )
    check(
        "does not promote this row" in note_text,
        "note_preserves_bounded_boundary",
        "repair section states that status movement remains audit-owned",
        results,
    )

    pass_count = sum(1 for item in results if item["pass"])
    fail_count = len(results) - pass_count

    print("=" * 86)
    print("MESON OS TRANSFER: RESTRICTED SOURCE PACKET MANIFEST")
    print("=" * 86)
    for item in results:
        status = "PASS" if item["pass"] else "FAIL"
        print(f"[{status}] {item['name']}: {item['detail']}")
    print("=" * 86)
    print(f"SUMMARY: MESON OS TRANSFER SOURCE PACKET PASS={pass_count} FAIL={fail_count}")
    print("=" * 86)

    out_dir = repo_path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.json"
    out_path.write_text(
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
    print(f"Output written: {out_path.relative_to(REPO_ROOT)}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
