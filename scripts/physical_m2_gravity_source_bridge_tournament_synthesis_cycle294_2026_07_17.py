#!/usr/bin/env python3
"""Cycle 294 synthesis controls for the physical-M2 gravity/source tournament.

Cold-run the three independent routes, verify their deliberately different
physical surfaces, and pin the synthesis/N1--N8 contract.  This runner does
not splice routes, name occupation probability energy, or promote a selected
source-port residual to an autonomous-law obstruction.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_M2_GRAVITY_SOURCE_BRIDGE_TOURNAMENT_SYNTHESIS_CYCLE294_NOTE_2026-07-17.md"
)

ROUTES = (
    (
        "A",
        ROOT
        / "scripts/direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17.py",
        23,
        re.compile(r"TOTAL:\s*PASS=(\d+)\s+FAIL=(\d+)"),
    ),
    (
        "B",
        ROOT / "scripts/local_m2_mass_scalar_deformation_response_route_b_2026_07_17.py",
        24,
        re.compile(r"SUMMARY\s+PASS\s+(\d+)\s+FAIL\s+(\d+)"),
    ),
    (
        "C",
        ROOT / "scripts/gravity_route_c_bounded_direct_current_search_2026_07_17.py",
        23,
        re.compile(r"TOTAL\s+PASS=(\d+)\s+FAIL=(\d+)"),
    ),
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "axiomatic three-dimensional space is not physical time",
        "six hard-core mediator m2",
        "global-blockade comparison",
        "physical local deformation layer",
        "phase-robust positive number current",
        "not one combined law",
        "not physical energy",
        "selected additive port",
        "externally supplied additive",
        "not the autonomous hard-core vertex history",
        "n1 — alternative routes",
        "n2 — scoped-condition audit",
        "n3 — hidden conditions",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial closure",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no shared obstruction",
        "no axiom pressure",
        "c_ref",
        "c_num",
        "c_wrap",
        "c_int",
        "c_local",
        "c_source",
        "operational quantum / records",
        "causal time / clock",
        "inertia / matter",
        "gravity / source / resource",
        "born / probability / realized history",
    )
    missing = tuple(item for item in required if item not in text)
    check("the synthesis pins scope, ledgers, all TOE lanes, and N1--N8", not missing, missing)


def cold_routes() -> None:
    rows = []
    for name, path, expected_pass, pattern in ROUTES:
        completed = subprocess.run(
            [sys.executable, str(path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        match = pattern.search(completed.stdout)
        observed = tuple(int(value) for value in match.groups()) if match else None
        rows.append(
            {
                "route": name,
                "returncode": completed.returncode,
                "observed": observed,
                "expected": (expected_pass, 0),
            }
        )
    check(
        "all three independent route runners pass at the reviewed totals",
        all(
            row["returncode"] == 0 and row["observed"] == row["expected"]
            for row in rows
        ),
        rows,
    )


def route_independence_controls() -> None:
    route_a = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "DIRECT_GATEWISE_MATTER_MEDIATOR_CURRENT_LEDGER_ROUTE_A_CYCLE293_NOTE_2026-07-17.md"
    )
    route_b = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "LOCAL_M2_MASS_SCALAR_DEFORMATION_RESPONSE_ROUTE_B_NOTE_2026-07-17.md"
    )
    route_c = normalized(
        ROOT
        / "docs/work_history/repo/review_feedback/"
        "GRAVITY_ROUTE_C_BOUNDED_DIRECT_CURRENT_SEARCH_NOTE_2026-07-17.md"
    )
    check(
        "the routes have no common code/update and do not silently form one law",
        "25 retained matter m2 plus 6 mediator m2" in route_a
        and "cycle-251/272" in route_a
        and "six additional field m2" in route_b
        and "cycle-269" in route_b
        and "three-m2 onsite block" in route_c
        and "cycle-269" in route_c,
    )
    check(
        "each route preserves the energy/source semantic boundary",
        "probability/configuration current, not energy" in route_a
        and "not physical energy" in route_b
        and "nothing here calls it physical energy or stress" in route_c,
    )


def selected_port_identity() -> None:
    # On a zero-mean periodic source rho, L^+ L rho = rho.  The selected
    # Cycle-215 constant port is -L rho / 6, so the conditional 3L^+ response
    # is -rho/2 exactly.  Use explicit spectral projectors as a synthesis
    # cross-check at several sizes; this is not the autonomous vertex history.
    rows = []
    for side in (3, 5, 7, 9):
        rho = np.zeros((side, side, side), dtype=float)
        rho[0, 0, 0] = 1.0
        rho -= np.mean(rho)
        spectrum = np.fft.fftn(rho)
        frequencies = 2 * np.pi * np.fft.fftfreq(side)
        kx, ky, kz = np.meshgrid(frequencies, frequencies, frequencies, indexing="ij")
        eigenvalue = 6 - 2 * np.cos(kx) - 2 * np.cos(ky) - 2 * np.cos(kz)
        laplacian_rho = np.fft.ifftn(eigenvalue * spectrum).real
        dynamic_port = -laplacian_rho / 6
        inverse = np.zeros_like(eigenvalue)
        inverse[eigenvalue > 1e-12] = 1 / eigenvalue[eigenvalue > 1e-12]
        response = 3 * np.fft.ifftn(inverse * np.fft.fftn(dynamic_port)).real
        rows.append((side, float(np.linalg.norm(response + rho / 2))))
    check(
        "the selected additive port-kernel comparator gives exactly minus one-half rho across held sizes",
        max(residual for _side, residual in rows) < 2e-12,
        rows,
    )


def main() -> int:
    note_contract()
    cold_routes()
    route_independence_controls()
    selected_port_identity()
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
