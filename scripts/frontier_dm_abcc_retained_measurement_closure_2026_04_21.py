#!/usr/bin/env python3
"""Supplied A-BCC basin endpoint diagnostics.

Historical seven-runner integration machinery is preserved but not executed
by default. Endpoint inertia/continuity implications require a supplied
nonsingular path; no physical basin selection or PNS closure is established.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/DM_ABCC_RETAINED_MEASUREMENT_CLOSURE_THEOREM_NOTE_2026-04-21.md']

import math
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


PASS_COUNT = 0
FAIL_COUNT = 0

E1 = math.sqrt(8.0 / 3.0)
E2 = math.sqrt(8.0) / 3.0
GAMMA = 0.5

T_M = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]], dtype=complex)
T_D = np.array([[0.0, -1.0, 1.0], [-1.0, 1.0, 0.0], [1.0, 0.0, -1.0]], dtype=complex)
T_Q = np.array([[0.0, 1.0, 1.0], [1.0, 0.0, 1.0], [1.0, 1.0, 0.0]], dtype=complex)
H_BASE = np.array(
    [
        [0.0, E1, -E1 - 1j * GAMMA],
        [E1, 0.0, -E2],
        [-E1 + 1j * GAMMA, -E2, 0.0],
    ],
    dtype=complex,
)

BASIN_1 = (0.657061342210, 0.933806343759, 0.715042329587)
BASIN_2 = (28.005676879468, 20.721919153777, 5.011726669406)
BASIN_X = (21.128264303040, 12.680028385305, 2.089234625632)

DEPENDENCIES = [
    ("active-chamber completeness", "frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py"),
    ("upper-octant / source-cubic selector", "frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20.py"),
    ("sigma_hier upper-octant selector", "frontier_dm_sigma_hier_upper_octant_selector_theorem_2026_04_20.py"),
    ("P3 Sylvester physical path", "frontier_dm_neutrino_source_surface_p3_sylvester_linear_path_signature_theorem_2026_04_18.py"),
    ("PMNS nonsingularity reduction", "frontier_dm_abcc_pmns_nonsingularity_theorem.py"),
    ("Sylvester signature forcing", "frontier_dm_abcc_signature_forcing_theorem.py"),
    ("sigma-chain attack cascade", "frontier_dm_pns_attack_cascade.py"),
]


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def parse_fail_count(output: str) -> int | None:
    matches = re.findall(r"FAIL\s*=\s*(\d+)", output)
    if not matches:
        return None
    return int(matches[-1])


def parse_pass_count(output: str) -> int | None:
    matches = re.findall(r"PASS\s*=\s*(\d+)", output)
    if not matches:
        return None
    return int(matches[-1])


def run_dependency(label: str, script_name: str) -> tuple[bool, str]:
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / script_name)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    output = proc.stdout + ("\n" + proc.stderr if proc.stderr else "")
    fail_count = parse_fail_count(output)
    pass_count = parse_pass_count(output)
    ok = proc.returncode == 0 and (fail_count == 0 if fail_count is not None else True)
    detail_bits: list[str] = [f"rc={proc.returncode}"]
    if pass_count is not None:
        detail_bits.append(f"PASS={pass_count}")
    if fail_count is not None:
        detail_bits.append(f"FAIL={fail_count}")
    detail = ", ".join(detail_bits)
    check(f"Dependency runner passes: {label}", ok, detail)
    return ok, output


def h_of(point: tuple[float, float, float]) -> np.ndarray:
    m, d, q = point
    return H_BASE + m * T_M + d * T_D + q * T_Q


def main() -> int:
    base_eig = np.linalg.eigvalsh(H_BASE)
    base_inertia = (int(np.sum(base_eig > 0)), int(np.sum(base_eig < 0)))
    check("supplied baseline is Hermitian", np.array_equal(H_BASE,H_BASE.conj().T))
    check("supplied baseline inertia is (1,2)", base_inertia == (1,2), str(base_eig))
    for name, point, expected_inertia in [
        ("Basin 1", BASIN_1, (1,2)),
        ("Basin 2", BASIN_2, (2,1)),
        ("Basin X", BASIN_X, (2,1)),
    ]:
        H = h_of(point)
        eig = np.linalg.eigvalsh(H)
        det = np.linalg.det(H)
        inertia = (int(np.sum(eig > 0)), int(np.sum(eig < 0)))
        check(name+" supplied endpoint Hermitian", np.array_equal(H,H.conj().T))
        check(name+" finite eigenvalues separated from zero", np.all(np.isfinite(eig)) and min(abs(eig)) > 1e-6, str(eig))
        check(name+" determinant agrees with spectral product", abs(det-np.prod(eig)) < 1e-9*max(1,abs(det)), str(det))
        check(name+" supplied endpoint inertia", inertia == expected_inertia, str(inertia))
        det_val = float(np.real(det))
        expect_positive = name == "Basin 1"
        sign_ok = det_val > 0 if expect_positive else det_val < 0
        check(name+" supplied endpoint determinant sign diagnostic", sign_ok, str(det_val))
        if name == "Basin 1":
            check("Basin 1 supplied chamber inequality", point[1]+point[2] > E1)
    print("Finite decimal endpoint checks only. Equal inertia does not select a physical source or certify the specified affine path.")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
