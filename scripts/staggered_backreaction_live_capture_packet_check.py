#!/usr/bin/env python3
"""Live bounded packet for staggered capture-closure backreaction."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import frontier_staggered_backreaction_capture_closure_harness as cap  # noqa: E402

NOTE = ROOT / "docs" / "STAGGERED_BACKREACTION_LIVE_CAPTURE_PACKET_NOTE_2026-05-29.md"
MANIFEST_CACHE = ROOT / "logs" / "runner-cache" / "staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.txt"
MANIFEST_JSON = ROOT / "outputs" / "staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.json"

PACKET_PATHS = [
    "scripts/frontier_staggered_backreaction_capture_closure_harness.py",
    "logs/runner-cache/frontier_staggered_backreaction_capture_closure_harness.txt",
    "scripts/frontier_staggered_backreaction_iterative.py",
    "logs/runner-cache/frontier_staggered_backreaction_iterative.txt",
    "scripts/frontier_staggered_cycle_battery.py",
    "logs/runner-cache/frontier_staggered_cycle_battery.txt",
    "scripts/frontier_staggered_layered_backreaction.py",
    "logs/runner-cache/frontier_staggered_layered_backreaction.txt",
    "scripts/frontier_staggered_backreaction_prototype.py",
    "logs/runner-cache/frontier_staggered_backreaction_prototype.txt",
    "scripts/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.py",
    "logs/runner-cache/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.txt",
    "outputs/staggered_backreaction_live_capture_source_packet_manifest_2026_06_06.json",
]

SOURCE_MARKERS = {
    "scripts/frontier_staggered_backreaction_capture_closure_harness.py": [
        "import frontier_staggered_backreaction_iterative as iterative",
        "import frontier_staggered_cycle_battery as cycle",
        "import frontier_staggered_layered_backreaction as layered",
        "def _measure_cycle_graph",
        "def _measure_holdout",
    ],
    "scripts/frontier_staggered_backreaction_iterative.py": [
        "import frontier_staggered_backreaction_prototype as base",
        "def _apply_mapping",
        "def _source_density",
        "def _measure_family",
    ],
    "scripts/frontier_staggered_cycle_battery.py": [
        "def make_random_geometric",
        "def make_growing",
        "def _source_density",
        "def _solve_phi",
        "def _build_H",
    ],
    "scripts/frontier_staggered_layered_backreaction.py": [
        "def _build_layered_family",
        "def _source_density",
        "def _solve_phi",
        "def _force_from_phi",
    ],
    "scripts/frontier_staggered_backreaction_prototype.py": [
        "def _make_graphs",
        "def _source_density",
        "def _solve_phi",
        "def _build_hamiltonian",
        "def _evolve_cn",
        "def _force_from_phi",
    ],
}

CACHE_TO_RUNNER = {
    "logs/runner-cache/frontier_staggered_backreaction_capture_closure_harness.txt": (
        "scripts/frontier_staggered_backreaction_capture_closure_harness.py",
        "STAGGERED BACKREACTION CAPTURE-CLOSURE HARNESS",
    ),
    "logs/runner-cache/frontier_staggered_backreaction_iterative.txt": (
        "scripts/frontier_staggered_backreaction_iterative.py",
        "STAGGERED BACKREACTION ITERATIVE SOURCE-MAPPING PROBE",
    ),
    "logs/runner-cache/frontier_staggered_cycle_battery.txt": (
        "scripts/frontier_staggered_cycle_battery.py",
        "STAGGERED FERMION",
    ),
    "logs/runner-cache/frontier_staggered_layered_backreaction.txt": (
        "scripts/frontier_staggered_layered_backreaction.py",
        "STAGGERED LAYERED BACKREACTION BRIDGE",
    ),
    "logs/runner-cache/frontier_staggered_backreaction_prototype.txt": (
        "scripts/frontier_staggered_backreaction_prototype.py",
        "STAGGERED SOURCE-GENERATED BACKREACTION PROTOTYPE",
    ),
}

INLINE_PASS = 0
INLINE_FAIL = 0


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_cache(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    fields = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def check_packet(name: str, condition: bool, detail="") -> None:
    global INLINE_PASS, INLINE_FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        INLINE_PASS += 1
    else:
        INLINE_FAIL += 1
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def inline_source_packet_checks() -> int:
    print()
    print("=" * 96)
    print("INLINE SOURCE-PACKET EXPOSURE CHECKS")
    print("=" * 96)
    note_text = NOTE.read_text(encoding="utf-8")

    for rel_path in PACKET_PATHS:
        check_packet(f"packet path exists: {rel_path}", (ROOT / rel_path).exists())
        check_packet(f"note links packet path: {rel_path}", rel_path in note_text)

    for rel_path, markers in SOURCE_MARKERS.items():
        source = (ROOT / rel_path).read_text(encoding="utf-8")
        check_packet(f"source appears untruncated: {rel_path}", len(source) > 3000, f"{len(source)} bytes")
        for marker in markers:
            check_packet(f"source marker present in {rel_path}: {marker}", marker in source)

    for cache_rel, (runner_rel, snippet) in CACHE_TO_RUNNER.items():
        cache = parse_cache(ROOT / cache_rel)
        runner_sha = sha256_file(ROOT / runner_rel)
        check_packet(f"cache runner matches source: {cache_rel}", cache.get("runner") == runner_rel, cache.get("runner"))
        check_packet(
            f"cache SHA fresh: {cache_rel}",
            cache.get("runner_sha256") == runner_sha,
            f"{cache.get('runner_sha256')} == {runner_sha}",
        )
        check_packet(
            f"cache exits cleanly: {cache_rel}",
            cache.get("exit_code") == "0" and cache.get("status") == "ok",
            f"exit_code={cache.get('exit_code')} status={cache.get('status')}",
        )
        check_packet(f"cache contains expected marker: {cache_rel}", snippet in cache["_text"], snippet)

    manifest_cache = parse_cache(MANIFEST_CACHE)
    check_packet(
        "source-packet manifest cache reports zero failures",
        "SUMMARY: STAGGERED CAPTURE SOURCE PACKET PASS=91 FAIL=0" in manifest_cache["_text"],
    )
    if MANIFEST_JSON.exists():
        payload = json.loads(MANIFEST_JSON.read_text(encoding="utf-8"))
    else:
        payload = {}
    check_packet("source-packet manifest JSON exists", MANIFEST_JSON.exists(), MANIFEST_JSON.relative_to(ROOT))
    check_packet("source-packet manifest JSON reports zero failures", payload.get("summary", {}).get("fail") == 0, payload.get("summary"))

    print(f"INLINE SOURCE PACKET: PASS={INLINE_PASS} FAIL={INLINE_FAIL}")
    return INLINE_FAIL


def main() -> int:
    cycle_graphs = [
        cap.cycle.make_random_geometric(seed=42),
        cap.cycle.make_growing(seed=42),
    ]
    holdout = cap.layered._build_layered_family(seed=29, layers=10, width=6, fanout=2)

    print("=" * 96)
    print("STAGGERED BACKREACTION LIVE CAPTURE-CLOSURE PACKET")
    print("  current runner surface; bounded positive read only")
    print("=" * 96)
    print(
        f"closure={cap.CLOSURE.name}, map={cap.CLOSURE.mapping.name}, "
        f"self_mix={cap.CLOSURE.self_mix:.2f}, "
        f"capture_exp={cap.CLOSURE.capture_exponent:.2f}"
    )

    cycle_results = []
    for graph in cycle_graphs:
        print()
        print(f"CAPTURE BATTERY: {graph.name} ({graph.n} nodes)")
        result = cap._measure_cycle_graph(graph, cap.CLOSURE)
        cycle_results.append(result)

    holdout_result = cap._measure_holdout(holdout, cap.CLOSURE)

    baseline_cycle_mean = statistics.fmean(row.baseline_gap for row in cycle_results)
    closed_cycle_mean = statistics.fmean(row.closed_gap for row in cycle_results)
    cycle_improvement = baseline_cycle_mean / max(closed_cycle_mean, 1e-30)
    holdout_improvement = holdout_result.baseline_gap / max(
        holdout_result.closed_gap, 1e-30
    )
    mean_r2 = statistics.fmean(row.linearity_r2 for row in cycle_results)
    two_body_max = max(row.two_body_resid for row in cycle_results)
    norm_max = max(row.norm_drift for row in cycle_results + [holdout_result])
    min_score = min(row.score for row in cycle_results)

    print()
    print("HOLDOUT")
    print(
        f"  {holdout_result.graph}: baseline gap={holdout_result.baseline_gap:.3e}, "
        f"closed gap={holdout_result.closed_gap:.3e}, "
        f"improvement={holdout_improvement:.2f}x, "
        f"R2={holdout_result.linearity_r2:.6f}, TOWARD={holdout_result.toward}/3"
    )

    assertions_ok = (
        min_score == 9
        and baseline_cycle_mean > 0.95
        and closed_cycle_mean < 0.50
        and cycle_improvement > 2.0
        and mean_r2 > 0.99
        and two_body_max < 1e-12
        and holdout_result.zero_force == 0.0
        and holdout_result.closed_force > 0.0
        and holdout_result.closed_gap < holdout_result.baseline_gap
        and holdout_improvement > 1.9
        and holdout_result.linearity_r2 > 0.999
        and norm_max < 1e-12
    )

    print()
    print("SAFE READ")
    print(f"  cycle battery scores: {[row.score for row in cycle_results]}")
    print(f"  cycle mean gap: {baseline_cycle_mean:.3e} -> {closed_cycle_mean:.3e}")
    print(f"  cycle gap improvement factor: {cycle_improvement:.2f}x")
    two_body_readout = (
        "<1e-12" if two_body_max < 1e-12 else f"={two_body_max:.3e}"
    )
    print(f"  cycle mean R2: {mean_r2:.6f}; two-body max {two_body_readout}")
    print(
        f"  holdout gap: {holdout_result.baseline_gap:.3e} -> "
        f"{holdout_result.closed_gap:.3e} ({holdout_improvement:.2f}x)"
    )
    print("  bounded live packet only: no old stale table or continuum closure")
    print(f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] live capture packet")
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    inline_fail = inline_source_packet_checks()
    return 0 if assertions_ok and inline_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
