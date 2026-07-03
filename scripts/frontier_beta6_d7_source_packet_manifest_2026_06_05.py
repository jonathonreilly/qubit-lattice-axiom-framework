#!/usr/bin/env python3
"""Source-packet manifest for the beta6 d7 maxorder-7 repair."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
D7_NOTE = ROOT / "docs" / "BETA6_PLAQUETTE_D7_COEFFICIENT_AND_TADPOLE_VERDICT_BOUNDED_NOTE_2026-05-30.md"
CONNECTED_NOTE = ROOT / "docs" / "BETA6_PLAQUETTE_CONNECTED_BETA6_COEFFICIENT_BOUNDED_NOTE_2026-05-30.md"
OUT = ROOT / "outputs" / "frontier_beta6_d7_source_packet_manifest_2026_06_05.json"

PATHS = {
    "primary_runner": ROOT / "scripts" / "frontier_beta6_connected_coefficient_2026_05_30.py",
    "maxorder7_runner": ROOT / "scripts" / "frontier_beta6_d7_maxorder7_packet_2026_06_05.py",
    "maxorder7_cache": ROOT / "logs" / "runner-cache" / "frontier_beta6_d7_maxorder7_packet_2026_06_05.txt",
    "d9_runner": ROOT / "scripts" / "frontier_beta6_d9_coefficient_2026_06_04.py",
    "d9_cache": ROOT / "logs" / "runner-cache" / "frontier_beta6_d9_coefficient_2026_06_04.txt",
    "manifest_runner": ROOT / "scripts" / "frontier_beta6_d7_source_packet_manifest_2026_06_05.py",
    "manifest_cache": ROOT / "logs" / "runner-cache" / "frontier_beta6_d7_source_packet_manifest_2026_06_05.txt",
    "manifest_json": OUT,
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_header(text: str) -> dict[str, str | None]:
    def find(pattern: str) -> str | None:
        m = re.search(pattern, text, re.MULTILINE)
        return m.group(1).strip() if m else None

    return {
        "runner": find(r"^runner:\s*(.+)$"),
        "runner_sha256": find(r"^runner_sha256:\s*([0-9a-f]{64})$"),
        "exit_code": find(r"^exit_code:\s*(\S+)$"),
        "status": find(r"^status:\s*(\S+)$"),
    }


def main() -> int:
    d7_note = D7_NOTE.read_text(encoding="utf-8")
    connected_note = CONNECTED_NOTE.read_text(encoding="utf-8")
    checks: list[dict[str, object]] = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        checks.append({"name": name, "ok": ok, "detail": detail})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    self_outputs = {"manifest_cache", "manifest_json"}
    for label, path in PATHS.items():
        if label not in self_outputs:
            exists = path.exists()
            check(f"path_exists:{label}", exists, rel(path))
        check(f"d7_note_links:{label}", rel(path) in d7_note, rel(path))

    connected_required_links = [
        "primary_runner",
        "maxorder7_runner",
        "maxorder7_cache",
        "manifest_runner",
        "manifest_cache",
        "manifest_json",
    ]
    for label in connected_required_links:
        check(f"connected_note_links:{label}", rel(PATHS[label]) in connected_note, rel(PATHS[label]))
    check(
        "connected_note_links:d7_companion_note",
        rel(D7_NOTE) in connected_note or D7_NOTE.name in connected_note,
        rel(D7_NOTE),
    )
    connected_markers = [
        "d_7 = 5 / 17006112",
        "d_7 / d_6 = 5/21",
        "completed maxorder-7 packet",
        "full untruncated source runner",
        "SCORECARD: PASS=22 FAIL=0",
        "SUMMARY: BETA6 D7 SOURCE PACKET PASS=53 FAIL=0",
        "beta=6 closure problem remains open",
    ]
    for marker in connected_markers:
        check(f"connected_note_marker:{marker}", marker in connected_note, marker)

    primary = PATHS["primary_runner"].read_text(encoding="utf-8")
    primary_markers = [
        "def compute_dn_frac",
        "def cycle_space_certificate",
        "def cube_shells_size5",
        "if maxorder >= 7",
        "d_7 exact value = 5/17006112",
        "bounded verdict: tadpole/geometric ansatz falsified at order 7",
    ]
    for marker in primary_markers:
        check(f"primary_source_marker:{marker}", marker in primary, marker)

    wrapper = PATHS["maxorder7_runner"].read_text(encoding="utf-8")
    for marker in [
        "AUDIT_TIMEOUT_SEC = 420",
        'delegated_argv: 7',
        "frontier_beta6_connected_coefficient_2026_05_30",
    ]:
        check(f"maxorder7_wrapper_marker:{marker}", marker in wrapper, marker)

    for label in ["maxorder7_cache", "d9_cache"]:
        cache_path = PATHS[label]
        cache = cache_path.read_text(encoding="utf-8")
        header = cache_header(cache)
        runner_key = "maxorder7_runner" if label == "maxorder7_cache" else "d9_runner"
        expected_runner = rel(PATHS[runner_key])
        expected_sha = sha256(PATHS[runner_key])
        check(f"cache_runner_matches:{label}", header["runner"] == expected_runner, f"{header['runner']} == {expected_runner}")
        check(f"cache_sha_fresh:{label}", header["runner_sha256"] == expected_sha, f"{header['runner_sha256']} == {expected_sha}")
        check(f"cache_status_ok:{label}", header["status"] == "ok" and header["exit_code"] == "0", f"status={header['status']} exit={header['exit_code']}")

    max7_cache = PATHS["maxorder7_cache"].read_text(encoding="utf-8")
    for snippet in [
        "delegated_argv: 7",
        f"primary_runner_sha256: {sha256(PATHS['primary_runner'])}",
        "V5. order-beta^7 coefficient",
        "d_7 exact value = 5/17006112",
        "d_7/d_6 = 5/21",
        "SCORECARD:",
        "FAIL=0",
    ]:
        check(f"maxorder7_cache_snippet:{snippet}", snippet in max7_cache, snippet)

    d9_cache = PATHS["d9_cache"].read_text(encoding="utf-8")
    for snippet in [
        "d_7 = 5/17006112",
        "cube-sector closed form 72 K''(K')^5 reproduces the direct-engine d_5, d_6, d_7, d_8 EXACTLY",
        "SCORECARD: PASS=33 FAIL=0",
    ]:
        check(f"d9_cache_snippet:{snippet}", snippet in d9_cache, snippet)

    summary = {
        "pass": sum(1 for item in checks if item["ok"]),
        "fail": sum(1 for item in checks if not item["ok"]),
        "checks": checks,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("=" * 78)
    print(f"SUMMARY: BETA6 D7 SOURCE PACKET PASS={summary['pass']} FAIL={summary['fail']}")
    print("=" * 78)
    print(f"Output written: {rel(OUT)}")
    return 0 if summary["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
