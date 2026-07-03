#!/usr/bin/env python3
"""Source-packet manifest for the meson OS transfer representation runner."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs/meson_os_transfer_source_packet_manifest_2026_06_06.json"

PATHS = {
    "primary_runner": "scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py",
    "primary_runner_cache": "logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt",
}

REQUIRED_SOURCE_FRAGMENTS = [
    "def block_fwd_propagator_berezin(",
    "def block_fwd_propagator_operator(",
    "def block_metric_spacetime_eigs(",
    "def meson_op_on_vacuum_norm(",
    "def meson_correlator_full_berezin(",
    "def meson_correlator_from_propagator(",
    "def u_averaged_meson(",
    "def gauge_transform_links(",
    "K1  VACUUM-ANNIHILATION HANDLED",
    "K2  PER-MODE-FACTORIZED BEREZIN BREAKS",
    "K3  det-WEIGHT control",
    "K4  SINGLE-STEP control",
    "K5  GAUGE INVARIANCE",
]

REQUIRED_CACHE_SNIPPETS = [
    "SCORECARD PASS=64 FAIL=0",
    "P0      : det-weighted avg Berezin == operator meson",
    "P1      : per-config Berezin(4-ferm) == operator meson",
    "K1 VAC  : ||F|Omega>||",
    "K2 BREAK: per-mode-factorized Berezin gap",
    "K3 DIFF : flat(no-det) vs det-weighted gap",
    "K4 CTRL : single-step block-metric min eig",
    "K5 GAUGE: ||<Theta(F)F> invariance|| under g",
]


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
    note_path = ROOT / "docs/MESON_GAUGE_INVARIANT_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md"
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

    source_path = ROOT / PATHS["primary_runner"]
    source = source_path.read_text()
    check("source_full_length", len(source) > 40000, f"bytes={len(source)}")
    for fragment in REQUIRED_SOURCE_FRAGMENTS:
        check(f"source_contains:{fragment}", fragment in source, fragment)

    cache_path = ROOT / PATHS["primary_runner_cache"]
    cache = cache_path.read_text()
    fields = cache_fields(cache)
    runner = fields.get("runner", "")
    runner_path = ROOT / runner
    check("cache_runner_present", runner_path.exists(), runner)
    if runner_path.exists():
        check(
            "cache_sha_fresh",
            fields.get("runner_sha256") == sha256(runner_path),
            f"{fields.get('runner_sha256')} == {sha256(runner_path)}",
        )
    check("cache_exit_ok", fields.get("exit_code") == "0", f"exit_code={fields.get('exit_code')}")
    check("cache_status_ok", fields.get("status") == "ok", f"status={fields.get('status')}")
    for snippet in REQUIRED_CACHE_SNIPPETS:
        check(f"cache_contains:{snippet}", snippet in cache, snippet)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "claim_id": "meson_gauge_invariant_os_transfer_representation_bounded_note_2026-05-30",
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
    print(f"SUMMARY: MESON OS SOURCE PACKET PASS={passed} FAIL={failed}")
    print(f"OUTPUT_JSON={OUTPUT.relative_to(ROOT)}")
    print("=" * 88)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
