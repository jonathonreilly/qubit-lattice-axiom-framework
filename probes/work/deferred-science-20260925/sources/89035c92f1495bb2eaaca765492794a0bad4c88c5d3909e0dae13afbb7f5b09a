#!/usr/bin/env python3
"""Finite-spectrum corroboration for the principal electric Weyl-count note.

The analytic trace-moment proof is in the paired note. This script checks
finite empirical moments/counts only; it does not certify the weak limit or
any adjacent-eigenvalue spacing.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = (
    "docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/ZERO_MODE_AND_GOEGENBAUER_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/POSTMARK_ELECTRIC_PRINCIPAL_WEYL_COUNT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "scripts/postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py",
)

ROOT = Path(__file__).resolve().parents[1]
EXACT_SIDE = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
EXACT_NOTE = ROOT / "docs" / "POSTMARK_ELECTRIC_EXACT_SIDE_FIXED_INDEX_KERNEL_BOUNDED_THEOREM_NOTE_2026-09-24.md"
FIVE_NOTE = ROOT / "docs" / "POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md"
NOTE = ROOT / "docs" / "POSTMARK_ELECTRIC_PRINCIPAL_WEYL_COUNT_BOUNDED_THEOREM_NOTE_2026-09-24.md"
OUT = ROOT / "outputs" / "postmark_moving_index_2026_09_24" / "principal_weyl_count_2026_09_24.json"


def load_exact_side():
    spec = importlib.util.spec_from_file_location("exact_side_weyl_runner", EXACT_SIDE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def run():
    exact = load_exact_side()
    rows = []
    thresholds = (0.25, 1.0, 2.25, 3.24)
    for spin in (8, 16, 32, 64, 128):
        _lo, _hi, diagonal, offdiagonal, _positive = exact.finite_spin_matrix(spin)
        eigenvalues = eigh_tridiagonal(diagonal, offdiagonal, eigvals_only=True)
        moments = {}
        for m in range(9):
            finite = float(np.mean(eigenvalues ** m))
            limiting = float(4**m / (2*m + 1))
            moments[str(m)] = {
                "finite_empirical_moment": finite,
                "limit_formula": limiting,
                "absolute_error": abs(finite - limiting),
            }
        cdf = {}
        for level in thresholds:
            empirical = float(np.mean(eigenvalues <= level))
            target = float(np.sqrt(level) / 2.0)
            cdf[str(level)] = {
                "finite_counting_fraction": empirical,
                "limit_formula": target,
                "absolute_error": abs(empirical - target),
            }
        rows.append({
            "S": spin,
            "dimension": int(len(eigenvalues)),
            "eigenvalue_min_max": [float(eigenvalues[0]), float(eigenvalues[-1])],
            "moments_0_through_8": moments,
            "cdf_samples": cdf,
            "scope": "finite eigensolve corroboration only; no weak-limit certificate or local-gap bound",
        })
    return {
        "claim_id": "postmark_electric_principal_weyl_count_2026_09_24",
        "source_revision": "5171af01191cc2db9d5bad0f8eca2185114ebbe3",
        "inputs_sha256": {
            "exact_side_runner": hashlib.sha256(EXACT_SIDE.read_bytes()).hexdigest(),
            "exact_side_note": hashlib.sha256(EXACT_NOTE.read_bytes()).hexdigest(),
            "five_site_note": hashlib.sha256(FIVE_NOTE.read_bytes()).hexdigest(),
            "this_runner": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "limiting_measure": "1_(0,4)(lambda)/(4*sqrt(lambda)) d lambda",
        "limiting_moments": "4^m/(2m+1)",
        "limiting_counting_fraction": "sqrt(lambda)/2 for 0<=lambda<=4",
        "rows": rows,
    }


def main():
    result = run()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
