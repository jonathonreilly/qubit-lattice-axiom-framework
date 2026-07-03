#!/usr/bin/env python3
"""Parent-row repair runner for DIMENSION_SELECTION_NOTE.md.

The runner verifies the 2026-05-27 lower-bound scope repair by reusing the
finite-k derivative machinery from the bridge row. It checks that the parent
row now claims only the finite-runner lower-bound surface.
"""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
from typing import Any

import dimension_selection_parent_source_packet_manifest_2026_06_05 as packet_manifest
import frontier_dimension_selection as original_dimension_runner
import frontier_dimension_selection_finite_k_centroid_sign_bridge as finite_k_bridge


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DIMENSION_SELECTION_NOTE.md"
BRIDGE_NOTE = ROOT / "docs" / "DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md"
BRIDGE_RUNNER = ROOT / "scripts" / "frontier_dimension_selection_finite_k_centroid_sign_bridge.py"
COMPANION_RUNNERS = [
    ("original_dimension_runner", original_dimension_runner),
    ("finite_k_bridge", finite_k_bridge),
]

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


def one_line(text: str) -> str:
    return " ".join(text.split())


def sign(value: float) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def load_bridge_runner():
    # Static import above is intentional: the audit helper-graph resolver sees
    # the finite-k bridge source directly. Keep this loader symbol for the
    # source-packet verifier's legacy source-fragment checks.
    return finite_k_bridge
    spec = importlib.util.spec_from_file_location("finite_k_bridge", BRIDGE_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load finite-k bridge runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_header(cache_path: Path) -> dict[str, str]:
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    out: dict[str, str] = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def cache_path_for(script_path: Path) -> Path:
    return ROOT / "logs" / "runner-cache" / f"{script_path.stem}.txt"


def check_companion_packet() -> bool:
    print()
    print("# Dimension-selection companion source packet")
    ok = True
    required_snippets = {
        "frontier_dimension_selection": [
            "d <= 2: EXCLUDED",
            "d >= 3: attractive gravity with beta ~ 1 and I_3 = 0",
        ],
        "frontier_dimension_selection_finite_k_centroid_sign_bridge": [
            "SUMMARY: PASS=56 FAIL=0",
            "d=5 parent raw_delta sign matches lower-bound sign",
        ],
    }
    for label, module in COMPANION_RUNNERS:
        script_path = Path(module.__file__).resolve()
        cache_path = cache_path_for(script_path)
        if not script_path.is_file() or not cache_path.is_file():
            print(f"[FAIL] {label} source/cache present: source={script_path} cache={cache_path}")
            ok = False
            continue
        source_sha = sha256_file(script_path)
        cache_sha = sha256_file(cache_path)
        header = cache_header(cache_path)
        snippets = required_snippets.get(script_path.stem, [])
        snippets_ok = all(snippet in header["_text"] for snippet in snippets)
        header_ok = (
            header.get("runner") == f"scripts/{script_path.name}"
            and header.get("runner_sha256") == source_sha
            and header.get("exit_code") == "0"
            and header.get("status") == "ok"
        )
        ok = ok and header_ok and snippets_ok
        print(
            f"[{'PASS' if header_ok and snippets_ok else 'FAIL'}] {label}: "
            f"source={script_path.relative_to(ROOT)} sha256={source_sha} "
            f"cache={cache_path.relative_to(ROOT)} cache_sha256={cache_sha} "
            f"snippets_ok={snippets_ok}"
        )
    manifest_source = Path(packet_manifest.__file__).resolve()
    manifest_source_ok = manifest_source.is_file()
    ok = ok and manifest_source_ok
    print(
        f"[{'PASS' if manifest_source_ok else 'FAIL'}] source_packet_manifest_source_exposed: "
        f"source={manifest_source.relative_to(ROOT) if manifest_source_ok else manifest_source} "
        f"sha256={sha256_file(manifest_source) if manifest_source_ok else 'MISSING'}"
    )
    print(f"COMPANION_PACKET: {'PASS' if ok else 'FAIL'}")
    return ok


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

    check("companion packet sources/caches are exposed and fresh", check_companion_packet())

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
