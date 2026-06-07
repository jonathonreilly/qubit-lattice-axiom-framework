#!/usr/bin/env python3
"""Basin probe for the fifth-family radial-shell connectivity slice."""

from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP import (
    Family,
    _build_radial_shell_connectivity,
    _measure_family,
    _mean,
)
from gate_b_no_restore_farfield import grow


AUDIT_TIMEOUT_SEC = 300

DRIFTS = [0.05, 0.10, 0.20, 0.30, 0.40]
SEEDS = [0, 1]

REPO_ROOT = Path(ROOT)
NOTE_PATH = REPO_ROOT / "docs" / "FIFTH_FAMILY_RADIAL_REPAIRED_POSITIVE_PACKET_NOTE_2026-05-29.md"

COMPANION_PACKET_PATHS = [
    "scripts/FIFTH_FAMILY_RADIAL_BASIN.py",
    "logs/runner-cache/FIFTH_FAMILY_RADIAL_BASIN.txt",
    "scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py",
    "logs/runner-cache/FIFTH_FAMILY_RADIAL_FM_TRANSFER.txt",
    "scripts/FIFTH_FAMILY_RADIAL_SWEEP.py",
    "logs/runner-cache/FIFTH_FAMILY_RADIAL_SWEEP.txt",
    "scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py",
    "logs/runner-cache/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.txt",
    "scripts/CONNECTIVITY_FAMILY_V2_QUADRANT_SWEEP.py",
    "scripts/gate_b_no_restore_farfield.py",
]

SOURCE_MARKERS = {
    "scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py": [
        "TARGETS = [(0.05, 0), (0.30, 1)]",
        "def _fm(drift: float, seed: int) -> float:",
        "for strength in (5e-5, 1e-4):",
        "math.log(d2 / d1) / math.log(2.0)",
        "mean F~M among passes",
        "ASSERTIONS:",
    ],
    "scripts/FIFTH_FAMILY_RADIAL_SWEEP.py": [
        "TARGETS = [(0.05, 0), (0.20, 0), (0.30, 1)]",
        "pass_keys == {(0.05, 0), (0.30, 1)}",
        "boundary[3] < 0.0",
        "boundary[4] > 0.0",
        "ASSERTIONS:",
    ],
    "scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py": [
        "TARGETS = [(0.20, 0), (0.05, 0), (0.30, 1)]",
        "if not out.ok:",
        "the miss is a sign-orientation boundary",
    ],
}

MIN_SOURCE_BYTES = {
    "scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py": 2_500,
    "scripts/FIFTH_FAMILY_RADIAL_SWEEP.py": 3_000,
    "scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py": 2_000,
}

CACHE_TO_RUNNER = {
    "logs/runner-cache/FIFTH_FAMILY_RADIAL_FM_TRANSFER.txt": (
        "scripts/FIFTH_FAMILY_RADIAL_FM_TRANSFER.py",
        [
            "FIFTH FAMILY RADIAL F~M TRANSFER",
            "passed rows: 2/2",
            "mean F~M among passes: 0.999439",
            "ASSERTIONS: PASS",
        ],
    ),
    "logs/runner-cache/FIFTH_FAMILY_RADIAL_SWEEP.txt": (
        "scripts/FIFTH_FAMILY_RADIAL_SWEEP.py",
        [
            "FIFTH FAMILY RADIAL SWEEP",
            "passed rows: 2/3",
            "drift coverage: [0.05, 0.3]",
            "ASSERTIONS: PASS",
        ],
    ),
    "logs/runner-cache/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.txt": (
        "scripts/FIFTH_FAMILY_RADIAL_FAILURE_AUDIT.py",
        [
            "FIFTH FAMILY RADIAL FAILURE AUDIT",
            "failing rows: 1",
            "drift=0.20 seed=0 plus=-2.028e-06 minus=+2.028e-06 exp=1.000",
            "the miss is a sign-orientation boundary, not a control leak",
        ],
    ),
}


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _parse_cache_header(cache_path: Path) -> dict[str, str]:
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    fields: dict[str, str] = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def _inline_companion_packet_checks() -> tuple[int, int]:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str = "") -> None:
        nonlocal passed, failed
        status = "PASS" if condition else "FAIL"
        if condition:
            passed += 1
        else:
            failed += 1
        suffix = f": {detail}" if detail else ""
        print(f"[{status}] {name}{suffix}")

    note_text = NOTE_PATH.read_text(encoding="utf-8")

    for rel_path in COMPANION_PACKET_PATHS:
        path = REPO_ROOT / rel_path
        check(f"packet path exists: {rel_path}", path.exists())
        check(f"note links packet path: {rel_path}", rel_path in note_text)

    for rel_path, markers in SOURCE_MARKERS.items():
        source_path = REPO_ROOT / rel_path
        source = source_path.read_text(encoding="utf-8")
        check(
            f"companion source appears untruncated: {rel_path}",
            len(source) > MIN_SOURCE_BYTES[rel_path],
            f"{len(source)} bytes",
        )
        for marker in markers:
            check(
                f"source marker present in {rel_path}",
                marker in source,
                marker,
            )

    for cache_rel, (runner_rel, snippets) in CACHE_TO_RUNNER.items():
        cache_path = REPO_ROOT / cache_rel
        header = _parse_cache_header(cache_path)
        current_sha = _sha256_file(REPO_ROOT / runner_rel)
        check(
            f"cache runner matches source: {cache_rel}",
            header.get("runner") == runner_rel,
            runner_rel,
        )
        check(
            f"cache SHA fresh: {cache_rel}",
            header.get("runner_sha256") == current_sha,
            f"{header.get('runner_sha256')} == {current_sha}",
        )
        check(
            f"cache exits cleanly: {cache_rel}",
            header.get("exit_code") == "0" and header.get("status") == "ok",
            f"exit_code={header.get('exit_code')} status={header.get('status')}",
        )
        for snippet in snippets:
            check(
                f"cache contains expected marker: {cache_rel}",
                snippet in header["_text"],
                snippet,
            )

    print(f"INLINE COMPANION PACKET: PASS={passed} FAIL={failed}")
    return passed, failed


def main() -> None:
    print("=" * 96)
    print("FIFTH FAMILY RADIAL BASIN")
    print("  radial-shell connectivity on the no-restore grown slice")
    print("=" * 96)
    print(f"drifts={DRIFTS}, seeds={SEEDS}")
    print("guards: exact zero-source baseline, exact neutral cancellation, sign orientation")
    print()
    print(f"{'drift':>5s} {'seed':>4s} {'zero':>12s} {'plus':>12s} {'minus':>12s} {'neutral':>12s} {'double':>12s} {'exp':>7s} {'ok':>4s}")
    print("-" * 96)

    rows = []
    for drift in DRIFTS:
        for seed in SEEDS:
            pos, adj, layers, _nmap = grow(drift, seed)
            fam = Family(pos, layers, adj)
            radial = _build_radial_shell_connectivity(fam)
            out = _measure_family(radial.positions, radial.adj, radial.layers)
            rows.append((drift, seed, out.zero, out.plus, out.minus, out.neutral, out.double, out.exponent, out.ok))
            print(
                f"{drift:5.2f} {seed:4d} "
                f"{out.zero:+12.3e} {out.plus:+12.3e} {out.minus:+12.3e} "
                f"{out.neutral:+12.3e} {out.double:+12.3e} {out.exponent:7.3f} "
                f"{'YES' if out.ok else 'no':>4s}"
            )

    passed = [r for r in rows if r[-1]]
    print()
    print("SAFE READ")
    print(f"  passed rows: {len(passed)}/{len(rows)}")
    pass_keys = {(r[0], r[1]) for r in passed}
    assertions_ok = pass_keys == {(0.05, 0), (0.10, 0), (0.30, 0), (0.30, 1)}
    if passed:
        drift_vals = sorted({r[0] for r in passed})
        print(f"  drift coverage: {drift_vals}")
        print(f"  mean exponent among passes: {_mean([r[7] for r in passed]):.6f}")
        print("  this radial-shell family is a real bounded basin, but not family-wide")
    else:
        print("  no row survived the exact zero/neutral gate")
        print("  the radial-shell rule is a diagnosed failure on this slice")
    print(
        f"  [{'PASS' if assertions_ok else 'FAIL'} (C)] finite basin assertion surface"
    )
    _inline_passed, inline_failed = _inline_companion_packet_checks()
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    if not assertions_ok or inline_failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
