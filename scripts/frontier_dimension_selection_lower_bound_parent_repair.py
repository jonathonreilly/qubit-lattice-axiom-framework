#!/usr/bin/env python3
"""Parent-row repair runner for DIMENSION_SELECTION_NOTE.md.

The runner verifies the 2026-05-27 lower-bound scope repair by reusing the
finite-k derivative machinery from the bridge row. It checks that the parent
row now claims only the finite-runner lower-bound surface.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DIMENSION_SELECTION_NOTE.md"
BRIDGE_NOTE = ROOT / "docs" / "DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md"
BRIDGE_RUNNER = ROOT / "scripts" / "frontier_dimension_selection_finite_k_centroid_sign_bridge.py"
ORIGINAL_RUNNER = ROOT / "scripts" / "frontier_dimension_selection.py"
SOURCE_PACKET_RUNNER = ROOT / "scripts" / "dimension_selection_parent_source_packet_manifest_2026_06_05.py"
SOURCE_PACKET_JSON = ROOT / "outputs" / "dimension_selection_parent_source_packet_manifest_2026_06_05.json"

PACKET_PATHS = [
    "scripts/frontier_dimension_selection_lower_bound_parent_repair.py",
    "logs/runner-cache/frontier_dimension_selection_lower_bound_parent_repair.txt",
    "scripts/frontier_dimension_selection.py",
    "logs/runner-cache/frontier_dimension_selection.txt",
    "docs/DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md",
    "scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py",
    "logs/runner-cache/frontier_dimension_selection_finite_k_centroid_sign_bridge.txt",
    "outputs/dimension_selection_finite_k_centroid_sign_bridge_2026-05-25.json",
    "scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py",
    "logs/runner-cache/dimension_selection_parent_source_packet_manifest_2026_06_05.txt",
    "outputs/dimension_selection_parent_source_packet_manifest_2026_06_05.json",
]

CACHE_TO_RUNNER = {
    "logs/runner-cache/frontier_dimension_selection.txt": "scripts/frontier_dimension_selection.py",
    "logs/runner-cache/frontier_dimension_selection_finite_k_centroid_sign_bridge.txt": (
        "scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py"
    ),
}

CACHE_SNIPPETS = {
    "logs/runner-cache/frontier_dimension_selection.txt": [
        "I_3/P = <1e-10",
        "d <= 2: EXCLUDED",
        "d >= 3: attractive gravity with beta ~ 1 and I_3 = 0",
        "  3 |       Yes |    Yes |     Yes |    1.01",
        "  4 |       Yes |    Yes |     Yes |    1.05",
        "  5 |       Yes |    Yes |     Yes |    1.03",
    ],
    "logs/runner-cache/frontier_dimension_selection_finite_k_centroid_sign_bridge.txt": [
        "SUMMARY: PASS=56 FAIL=0",
        "d=1 derivative has expected sign",
        "d=5 parent raw_delta sign matches lower-bound sign",
    ],
}

PASS = 0
FAIL = 0
DIMS = (1, 2, 3, 4, 5)
EXPECTED = {1: -1, 2: -1, 3: 1, 4: 1, 5: 1}


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_cache(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    out = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def one_line(text: str) -> str:
    return " ".join(text.split())


def sign(value: float) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def load_bridge_runner():
    spec = importlib.util.spec_from_file_location("finite_k_bridge", BRIDGE_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load finite-k bridge runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_source_packet(note: str) -> None:
    print("\n# Inline source-packet exposure checks")
    flat_note = one_line(note)

    for rel_path in PACKET_PATHS:
        check(f"packet path exists: {rel_path}", (ROOT / rel_path).exists())
        check(f"parent note links packet path: {rel_path}", rel_path in flat_note)

    source_fragments = {
        ORIGINAL_RUNNER: [
            "def measure_gravity_2d_with_d_potential",
            "def measure_I3",
            "SUMMARY TABLE",
            "beta",
            "I_3",
        ],
        BRIDGE_RUNNER: [
            "def finite_k_centroid_derivative",
            "def propagate_centroid_for_mass",
            "def part3_finite_difference",
            "SUMMARY: PASS=",
        ],
        SOURCE_PACKET_RUNNER: [
            "finite_k_bridge_runner",
            "original_cache",
            "cache_sha_fresh",
            "SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS=",
        ],
    }
    for source_path, fragments in source_fragments.items():
        source = read(source_path)
        for fragment in fragments:
            check(f"source fragment present in {source_path.relative_to(ROOT)}: {fragment}", fragment in source)

    for cache_rel, runner_rel in CACHE_TO_RUNNER.items():
        cache_path = ROOT / cache_rel
        runner_path = ROOT / runner_rel
        cache = parse_cache(cache_path)
        runner_sha = sha256_file(runner_path)
        check(f"cache runner matches source: {cache_rel}", cache.get("runner") == runner_rel, cache.get("runner"))
        check(
            f"cache SHA fresh: {cache_rel}",
            cache.get("runner_sha256") == runner_sha,
            f"{cache.get('runner_sha256')} == {runner_sha}",
        )
        check(
            f"cache exits cleanly: {cache_rel}",
            cache.get("exit_code") == "0" and cache.get("status") == "ok",
            f"exit_code={cache.get('exit_code')} status={cache.get('status')}",
        )
        for snippet in CACHE_SNIPPETS[cache_rel]:
            check(f"cache snippet present in {cache_rel}: {snippet}", snippet in cache["_text"])

    source_packet_cache = parse_cache(ROOT / "logs/runner-cache/dimension_selection_parent_source_packet_manifest_2026_06_05.txt")
    check(
        "source-packet cache belongs to verifier",
        source_packet_cache.get("runner") == "scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py",
        source_packet_cache.get("runner"),
    )
    check(
        "source-packet cache exits cleanly",
        source_packet_cache.get("exit_code") == "0" and source_packet_cache.get("status") == "ok",
        f"exit_code={source_packet_cache.get('exit_code')} status={source_packet_cache.get('status')}",
    )
    check(
        "source-packet cache reports zero failures",
        "SUMMARY: DIMENSION SELECTION SOURCE PACKET PASS=57 FAIL=0" in source_packet_cache["_text"],
    )
    if SOURCE_PACKET_JSON.exists():
        payload = json.loads(read(SOURCE_PACKET_JSON))
    else:
        payload = {}
    check("source-packet JSON exists", SOURCE_PACKET_JSON.exists(), SOURCE_PACKET_JSON.relative_to(ROOT))
    check("source-packet JSON reports zero failures", payload.get("summary", {}).get("fail") == 0, payload.get("summary"))


def main() -> int:
    print("# Dimension-selection parent lower-bound repair")
    note = read(NOTE)
    flat_note = one_line(note)
    bridge_note = read(BRIDGE_NOTE)

    for phrase in [
        "finite-runner lower-bound support only",
        "does not claim",
        "not a unique-dimension theorem",
        "DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md",
        "does not authorize any framework-baseline rewrite",
        "This row does not claim:",
        "framework-internal upper-bound derivation",
    ]:
        check(f"parent note contains boundary phrase: {phrase}", phrase in flat_note)

    for phrase in [
        "Exact Finite-k Derivative",
        "d <= 2  ->  negative centroid response",
        "d >= 3  ->  positive centroid response",
        "does not close the upper-bound side",
    ]:
        check(f"bridge note contains support phrase: {phrase}", phrase in bridge_note)

    bridge = load_bridge_runner()
    derivative_results: dict[int, float] = {}
    finite_probe_results: dict[int, float] = {}
    for d in DIMS:
        derivative = float(bridge.finite_k_centroid_derivative(d)["dC_dM_at_zero"])
        finite_probe = float(
            bridge.propagate_centroid_for_mass(d, bridge.FINITE_M)
            - bridge.propagate_centroid_for_mass(d, 0.0)
        )
        derivative_results[d] = derivative
        finite_probe_results[d] = finite_probe
        check(f"d={d} exact finite-k derivative has lower-bound sign", sign(derivative) == EXPECTED[d], derivative)
        check(f"d={d} parent finite-M replay has lower-bound sign", sign(finite_probe) == EXPECTED[d], finite_probe)

    passes = [d for d in DIMS if derivative_results[d] > 0 and finite_probe_results[d] > 0]
    fails = [d for d in DIMS if derivative_results[d] < 0 and finite_probe_results[d] < 0]
    check("finite-k lower-bound pass set is d=3,4,5", passes == [3, 4, 5], passes)
    check("finite-k lower-bound fail set is d=1,2", fails == [1, 2], fails)

    forbidden = [
        "self-consistency uniquely selects d = 3",
        "the Z^3 spatial substrate has been derived",
        "repo-wide framework-baseline rewrite is authorized",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    check_source_packet(note)

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
