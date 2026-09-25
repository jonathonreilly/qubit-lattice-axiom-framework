#!/usr/bin/env python3
"""Direct spectral actual-readout checks at larger spins; diagnostic only."""
from __future__ import annotations
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("actual_readout_extended_sizes.json")

spec = importlib.util.spec_from_file_location("exact_side_large", RUNNER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
rows = []
for S in (512, 640, 768, 896, 1024):
    lo, hi, d, e, _ = module.finite_spin_matrix(S)
    print(f"S={S} dimension={len(d)} diagonalizing", flush=True)
    lam, U = eigh_tridiagonal(d, e, eigvals_only=False)
    C = S * (S + 1)
    origin = np.zeros(len(d), dtype=np.float64)
    origin[-lo] = 1.0
    coeff = U.T @ origin
    direct_phase = np.exp(-0.25j * (lam * lam - C * lam))
    factored_phase = np.exp(0.25j * C * lam) * np.exp(-0.25j * lam * lam)
    state = U @ (direct_phase * coeff)
    state_factored = U @ (factored_phase * coeff)
    nodes = np.arange(lo, hi + 1, dtype=np.int64)
    V = np.exp(2j * np.pi * np.remainder(nodes, 3) / 3)
    v_expect = np.vdot(state, V * state)
    v_factored = np.vdot(state_factored, V * state_factored)
    row = {
        "S": S, "dimension": len(d),
        "actual_period_three_readout": float((1 + 2 * v_expect.real) / 3),
        "actual_V_expectation_real": float(v_expect.real),
        "actual_V_expectation_imag": float(v_expect.imag),
        "factorization_state_l2_error": float(np.linalg.norm(state - state_factored)),
        "factorization_readout_error": float(abs(v_expect - v_factored)),
        "state_norm_error": float(abs(np.vdot(state, state).real - 1)),
        "scope": "finite-spin float64 spectral diagnostic; no interval certificate or asymptotic inference",
    }
    rows.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
    del lam, U, coeff, state, state_factored
    gc.collect()
result = {
    "source_revision": "5171af01191cc2db9d5bad0f8eca2185114ebbe3",
    "exact_side_runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
    "phase": "exp[-i/4*(lambda^2-C*lambda)]",
    "rows": rows,
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
