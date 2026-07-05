#!/usr/bin/env python3
"""Aggregate verifier for the Koide A1 fractional-topology no-go synthesis.

The source note is a synthesis row whose load-bearing evidence is a five-probe
no-go packet.  This runner makes that packet auditable as one primary runner:
it imports each probe as a helper source, executes it, and checks the expected
PASS-only obstruction counts.
"""

from __future__ import annotations

import contextlib
import importlib
import io
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.frontier_koide_a1_cheeger_simons_rz_probe as o13_cheeger
import scripts.frontier_koide_a1_orbifold_chern_probe as o14_orbifold
import scripts.frontier_koide_a1_eta_to_radian_lift_probe as o15_eta
import scripts.frontier_koide_a1_fqhe_analog_probe as o16_fqhe
import scripts.frontier_koide_a1_twisted_k_theory_probe as o17_twisted_k


@dataclass(frozen=True)
class Probe:
    obstruction: str
    module: ModuleType
    expected_passes: int


PROBES = [
    Probe("O13 Cheeger-Simons R/Z period inheritance", o13_cheeger, 49),
    Probe("O14 orbifold-Chern pi-factor inheritance", o14_orbifold, 54),
    Probe("O15 eta mod-Z vs phase mod-2pi gap", o15_eta, 47),
    Probe("O16 many-body promotion cost", o16_fqhe, 59),
    Probe("O17 cyclotomic exponent vs rational mismatch", o17_twisted_k, 34),
]


def _counts(module: ModuleType) -> tuple[int, int]:
    if hasattr(module, "PASSES"):
        rows = getattr(module, "PASSES")
        passed = sum(1 for _, ok, _ in rows if ok)
        failed = len(rows) - passed
        return passed, failed
    return int(getattr(module, "PASS")), int(getattr(module, "FAIL"))


def _run_probe(probe: Probe) -> tuple[bool, str]:
    module = importlib.reload(probe.module)
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        rc = module.main()
    passed, failed = _counts(module)
    ok = rc == 0 and failed == 0 and passed == probe.expected_passes
    detail = (
        f"return={rc}; PASS={passed}; FAIL={failed}; "
        f"expected_PASS={probe.expected_passes}"
    )
    return ok, detail


def main() -> int:
    print("Koide A1 fractional-topology no-go synthesis aggregate verifier")
    print("=" * 78)
    print("Scope: aggregate the five existing PASS-only obstruction probes.")
    print("Status: runner certificate only; independent audit owns verdicts.")
    print()

    results: list[bool] = []
    for probe in PROBES:
        ok, detail = _run_probe(probe)
        results.append(ok)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {probe.obstruction}: {detail}")

    all_ok = all(results)
    print()
    print(
        "FRACTIONAL_TOPOLOGY_PACKET="
        + ("5_PROBES_ALL_OBSTRUCTION_CONFIRMED" if all_ok else "FAILED")
    )
    print("LOAD_BEARING_ROLE=no-go packet aggregation, not new status authority")
    print(f"TOTAL: PASS={sum(1 for ok in results if ok)}, FAIL={sum(1 for ok in results if not ok)}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
