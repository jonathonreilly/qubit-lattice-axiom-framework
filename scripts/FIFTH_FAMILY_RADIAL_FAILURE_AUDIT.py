#!/usr/bin/env python3
"""Boundary audit for the fifth-family radial-shell connectivity slice."""

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

from DISTANCE_LAW_PORTABILITY_COMPARE import (
    Family,
    _build_radial_shell_connectivity,
)
from CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP import _measure_family
from fifth_family_radial_symmetry_orientation_certificate_2026_06_08 import (
    compute_certificate,
)
from gate_b_no_restore_farfield import grow


TARGETS = [(0.20, 0), (0.05, 0), (0.30, 1)]
REPO_ROOT = Path(ROOT)
ORIENTATION_RUNNER = REPO_ROOT / "scripts" / "fifth_family_radial_symmetry_orientation_certificate_2026_06_08.py"
ORIENTATION_CACHE = REPO_ROOT / "logs" / "runner-cache" / "fifth_family_radial_symmetry_orientation_certificate_2026_06_08.txt"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _cache_header(cache_path: Path) -> dict[str, str]:
    header = cache_path.read_text(encoding="utf-8").split("----- stdout -----", 1)[0]
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def _verify_orientation_certificate() -> bool:
    print()
    print("INDEPENDENT ORIENTATION CERTIFICATE")
    if not ORIENTATION_RUNNER.exists():
        print("  FAIL missing certificate runner")
        return False
    if not ORIENTATION_CACHE.exists():
        print("  FAIL missing certificate cache")
        return False

    fields = _cache_header(ORIENTATION_CACHE)
    runner_rel = ORIENTATION_RUNNER.relative_to(REPO_ROOT).as_posix()
    source_sha = _sha256(ORIENTATION_RUNNER)
    source_text = ORIENTATION_RUNNER.read_text(encoding="utf-8")
    sha_fresh = fields.get("runner_sha256") == source_sha
    cache_ok = (
        fields.get("runner") == runner_rel
        and fields.get("status") == "ok"
        and fields.get("exit_code") == "0"
        and sha_fresh
    )
    cert = compute_certificate()
    direct_ok = cert.assertions_ok
    ok = cache_ok and direct_ok
    print(
        f"  runner={fields.get('runner')} status={fields.get('status')} "
        f"exit={fields.get('exit_code')} sha_fresh={sha_fresh}"
    )
    print(f"  source_sha256={source_sha}")
    print(f"  source_bytes={len(source_text.encode('utf-8'))}")
    print(
        "  direct_certificate="
        f"{'PASS' if direct_ok else 'FAIL'} "
        f"zero={cert.zero_delta:+.12e} neutral={cert.neutral_delta:+.12e} "
        f"plus={cert.plus_delta:+.12e} minus={cert.minus_delta:+.12e} "
        f"slope={cert.linear_slope:+.12e}"
    )
    print(f"  certificate={'PASS' if ok else 'FAIL'}")
    return ok


def main() -> None:
    print("=" * 96)
    print("FIFTH FAMILY RADIAL FAILURE AUDIT")
    print("  radial-shell boundary on the no-restore grown slice")
    print("=" * 96)
    print(f"targets={TARGETS}")
    print()
    print(f"{'drift':>5s} {'seed':>4s} {'zero':>12s} {'plus':>12s} {'minus':>12s} {'neutral':>12s} {'double':>12s} {'exp':>7s} {'ok':>4s}")
    print("-" * 96)

    failing = []
    for drift, seed in TARGETS:
        pos, adj, layers, _nmap = grow(drift, seed)
        fam = Family(pos, layers, adj)
        radial = _build_radial_shell_connectivity(fam)
        out = _measure_family(radial.positions, radial.adj, radial.layers)
        print(
            f"{drift:5.2f} {seed:4d} "
            f"{out.zero:+12.3e} {out.plus:+12.3e} {out.minus:+12.3e} "
            f"{out.neutral:+12.3e} {out.double:+12.3e} {out.exponent:7.3f} "
            f"{'YES' if out.ok else 'no':>4s}"
        )
        if not out.ok:
            failing.append((drift, seed, out.plus, out.minus, out.exponent))

    print()
    print("SAFE READ")
    print(f"  failing rows: {len(failing)}")
    if failing:
        for drift, seed, plus, minus, exponent in failing[:5]:
            print(
                f"    drift={drift:.2f} seed={seed} plus={plus:+.3e} "
                f"minus={minus:+.3e} exp={exponent:.3f}"
            )
        print("  the miss is a sign-orientation boundary, not a control leak")
    else:
        print("  no boundary failures found in this audit window")
    orientation_certificate_ok = _verify_orientation_certificate()
    assertions_ok = (
        len(failing) == 1
        and abs(failing[0][0] - 0.20) < 1e-12
        and failing[0][1] == 0
        and failing[0][2] < 0.0
        and failing[0][3] > 0.0
        and orientation_certificate_ok
    )
    print(f"ASSERTIONS: {'PASS' if assertions_ok else 'FAIL'}")
    if not assertions_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
