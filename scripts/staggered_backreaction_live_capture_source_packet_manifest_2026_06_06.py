#!/usr/bin/env python3
"""Source-packet manifest for the staggered live capture packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "outputs"
    / "staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.json"
)


PATHS = {
    "packet_checker": "scripts/staggered_backreaction_live_capture_packet_check.py",
    "packet_cache": "logs/runner-cache/staggered_backreaction_live_capture_packet_check.txt",
    "capture_harness": "scripts/frontier_staggered_backreaction_capture_closure_harness.py",
    "capture_harness_cache": "logs/runner-cache/frontier_staggered_backreaction_capture_closure_harness.txt",
    "iterative_helper": "scripts/frontier_staggered_backreaction_iterative.py",
    "iterative_helper_cache": "logs/runner-cache/frontier_staggered_backreaction_iterative.txt",
    "cycle_helper": "scripts/frontier_staggered_cycle_battery.py",
    "cycle_helper_cache": "logs/runner-cache/frontier_staggered_cycle_battery.txt",
    "layered_helper": "scripts/frontier_staggered_layered_backreaction.py",
    "layered_helper_cache": "logs/runner-cache/frontier_staggered_layered_backreaction.txt",
    "prototype_helper": "scripts/frontier_staggered_backreaction_prototype.py",
    "prototype_helper_cache": "logs/runner-cache/frontier_staggered_backreaction_prototype.txt",
}

MARKERS = {
    "packet_checker": [
        "import frontier_staggered_backreaction_capture_closure_harness as cap",
        "ASSERTIONS:",
    ],
    "capture_harness": [
        "import frontier_staggered_backreaction_iterative as iterative",
        "import frontier_staggered_cycle_battery as cycle",
        "import frontier_staggered_layered_backreaction as layered",
        "def _measure_cycle_graph(",
        "def _measure_holdout(",
        "CLOSURE = ClosureSpec(",
    ],
    "iterative_helper": [
        "import frontier_staggered_backreaction_prototype as base",
        "class MappingSpec",
        "def _apply_mapping(",
        "def _measure_family(",
    ],
    "cycle_helper": ["def make_random_geometric(", "def make_growing("],
    "layered_helper": ["def _build_layered_family("],
    "prototype_helper": [
        "def _source_density(",
        "def _solve_phi(",
        "def _build_hamiltonian(",
        "def _force_from_phi(",
        "def _measure_family(",
    ],
}

CACHE_SNIPPETS = {
    "packet_cache": "ASSERTIONS: PASS",
    "capture_harness_cache": "CAPTURE-CLOSURE HARNESS",
    "iterative_helper_cache": "STAGGERED BACKREACTION ITERATIVE SOURCE-MAPPING PROBE",
    "cycle_helper_cache": "CYCLE-BEARING GRAPH BATTERY",
    "layered_helper_cache": "STAGGERED LAYERED BACKREACTION",
    "prototype_helper_cache": "STAGGERED SOURCE-GENERATED BACKREACTION PROTOTYPE",
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
    note_path = ROOT / "docs/STAGGERED_BACKREACTION_LIVE_CAPTURE_PACKET_NOTE_2026-05-29.md"
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
                "claim_id": "staggered_backreaction_live_capture_packet_note_2026-05-29",
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
    print(f"SUMMARY: STAGGERED CAPTURE SOURCE PACKET PASS={passed} FAIL={failed}")
    print(f"OUTPUT_JSON={OUTPUT.relative_to(ROOT)}")
    print("=" * 88)
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
