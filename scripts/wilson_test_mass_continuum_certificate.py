#!/usr/bin/env python3
"""Deterministic certificate for the bounded open-Wilson companion.

This wrapper executes the three load-bearing computations named by
WILSON_TEST_MASS_CONTINUUM_NOTE_2026-04-11.md and checks their reported
exponents and R^2 values.  It deliberately does not promote the diagnostic
L->infinity extrapolation.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1200
AUDIT_INPUT_PATHS = (
    "docs/WILSON_TEST_MASS_CONTINUUM_NOTE_2026-04-11.md",
    "scripts/frontier_test_mass_limit.py",
    "scripts/frontier_perturbative_mass_law.py",
    "scripts/frontier_continuum_limit.py",
)

RUNNERS = (
    "scripts/frontier_test_mass_limit.py",
    "scripts/frontier_perturbative_mass_law.py",
    "scripts/frontier_continuum_limit.py",
)
N5_PREFIXES = (
    "per_element:",
    "per_site:",
    "per_mode:",
    "per_block:",
    "lattice_wide:",
)


def run_child(path: str) -> tuple[int, str, str]:
    proc = subprocess.run(
        [sys.executable, "-u", path],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    print(f"CHILD {path} exit={proc.returncode}")
    # Child N5 lines remain available in the returned stdout for parsing, but
    # the registered wrapper emits one canonical five-line N5 tail of its own.
    visible_stdout = "\n".join(
        line
        for line in proc.stdout.splitlines()
        if not line.startswith(N5_PREFIXES)
    )
    print(visible_stdout)
    if proc.stderr:
        print(f"STDERR {path}")
        print(proc.stderr, end="" if proc.stderr.endswith("\n") else "\n")
    return proc.returncode, proc.stdout, proc.stderr


def require(pattern: str, text: str, label: str) -> tuple[float, ...]:
    match = re.search(pattern, text, re.MULTILINE)
    if match is None:
        raise ValueError(f"missing {label}")
    return tuple(float(value) for value in match.groups())


def main() -> int:
    outputs: dict[str, str] = {}
    child_ok = True
    for runner in RUNNERS:
        code, stdout, _stderr = run_child(runner)
        outputs[runner] = stdout
        child_ok &= code == 0

    try:
        test_mass, test_mass_r2 = require(
            r"\|dx_total\|\s*~\s*M_source\^([+-]?\d+(?:\.\d+)?)"
            r"\s+\(R\^2=([0-9.]+)",
            outputs[RUNNERS[0]],
            "test-mass source exponent",
        )
        test_distance, test_distance_r2 = require(
            r"\|dx_total\|\s*~\s*d\^([+-]?\d+(?:\.\d+)?)"
            r"\s+\(R\^2=([0-9.]+)",
            outputs[RUNNERS[0]],
            "test-mass distance exponent",
        )
        perturb_mass, perturb_mass_r2 = require(
            r"MASS EXPONENT:\s*([+-]?\d+(?:\.\d+)?)[\s\S]*?"
            r"R\^2\s*=\s*([0-9.]+)",
            outputs[RUNNERS[1]],
            "perturbative mass exponent",
        )
        perturb_distance, perturb_distance_r2 = require(
            r"DISTANCE EXPONENT:\s*([+-]?\d+(?:\.\d+)?)[\s\S]*?"
            r"R\^2\s*=\s*([0-9.]+)",
            outputs[RUNNERS[1]],
            "perturbative distance exponent",
        )
        perturb_g, perturb_g_r2 = require(
            r"G EXPONENT:\s*([+-]?\d+(?:\.\d+)?)[\s\S]*?"
            r"R\^2\s*=\s*([0-9.]+)",
            outputs[RUNNERS[1]],
            "perturbative G exponent",
        )
        finite_rows = [
            (int(side), float(alpha), float(r2))
            for side, alpha, r2 in re.findall(
                r"^L =\s*(\d+).*?^  FIT: \|a_mut\| ~ d\^"
                r"([+-]?\d+(?:\.\d+)?)\s+\(R\^2=([0-9.]+)\)",
                outputs[RUNNERS[2]],
                re.MULTILINE | re.DOTALL,
            )
        ]
    except ValueError as exc:
        print(f"CERTIFICATE parse_error={exc}")
        return 1

    expected_sides = [12, 15, 18, 20, 22, 25]
    numerical_ok = (
        0.98 <= test_mass <= 1.02
        and test_mass_r2 >= 0.999
        and -2.30 <= test_distance <= -1.80
        and test_distance_r2 >= 0.98
        and 0.999 <= perturb_mass <= 1.001
        and perturb_mass_r2 >= 0.999
        and -2.05 <= perturb_distance <= -1.80
        and perturb_distance_r2 >= 0.999
        and 0.999 <= perturb_g <= 1.001
        and perturb_g_r2 >= 0.999
        and [side for side, _alpha, _r2 in finite_rows] == expected_sides
        and all(-2.10 <= alpha <= -1.75 for _side, alpha, _r2 in finite_rows)
        and all(r2 >= 0.999 for _side, _alpha, r2 in finite_rows)
    )

    print()
    print(
        f"per_element: computed child finite-grid matrix/field updates; "
        f"test_mass={test_mass:+.4f} (R^2={test_mass_r2:.6f})"
    )
    print(
        f"per_site: computed every site on the declared open-Wilson grids; "
        f"test_distance={test_distance:+.4f} (R^2={test_distance_r2:.6f})"
    )
    print(
        f"per_mode: computed test-mass and perturbative mass, distance, and G "
        f"modes; perturbative=({perturb_mass:+.4f}, "
        f"{perturb_distance:+.4f}, {perturb_g:+.4f})"
    )
    print(
        "per_block: computed finite-L blocks "
        + ", ".join(
            f"L={side}:alpha={alpha:+.4f},R^2={r2:.6f}"
            for side, alpha, r2 in finite_rows
        )
    )
    print(
        "lattice_wide: checked and not executed — an asymptotic continuum "
        "certificate needs an independently justified extrapolation model; "
        "the executed evidence is the six finite-L blocks"
    )
    passed = child_ok and numerical_ok
    print(
        f"CERTIFICATE child_ok={child_ok} numerical_ok={numerical_ok} "
        f"finite_rows={len(finite_rows)}"
    )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
