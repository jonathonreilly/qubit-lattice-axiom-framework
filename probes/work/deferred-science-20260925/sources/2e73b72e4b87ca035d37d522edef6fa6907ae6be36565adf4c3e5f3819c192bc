#!/usr/bin/env python3
"""Check how the five-site principal Weyl law resolves actual gap aliases."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("weyl_alias_scaling_probe.json")
spec = importlib.util.spec_from_file_location("exact_side_weyl", RUNNER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

rows = []
for S in (96, 192, 384, 512):
    _, _, d, e, _ = module.finite_spin_matrix(S)
    lam = eigh_tridiagonal(d, e, eigvals_only=True)
    C = S * (S + 1)
    j = np.arange(len(lam) - 1, dtype=float)
    actual = C * np.diff(lam) / 4.0
    # From the principal five-site Weyl count N_{<=lambda}~5S sqrt(lambda),
    # lambda_j~(j/(5S))^2, hence delta theta~(S+1)(2j+1)/(100S).
    prediction = (S + 1) * (2 * j + 1) / (100.0 * S)
    residual = actual - prediction
    fit_slope, fit_intercept = np.polyfit(j, actual, 1)
    m_actual = np.rint(actual / (2 * np.pi)).astype(int)
    m_pred = np.rint(prediction / (2 * np.pi)).astype(int)
    corr = float(np.corrcoef(actual, prediction)[0, 1])
    rows.append({
        "S": S, "dimension": len(lam),
        "actual_alpha_min_max": [float(actual.min()), float(actual.max())],
        "weyl_alpha_min_max": [float(prediction.min()), float(prediction.max())],
        "linear_fit_actual_alpha_vs_sorted_index": {
            "slope": float(fit_slope), "intercept": float(fit_intercept),
            "predicted_slope": float((S + 1) / (50.0 * S)),
        },
        "pearson_actual_vs_weyl_increment": corr,
        "residual_rad_quantiles_abs": {
            str(q): float(np.quantile(np.abs(residual), q)) for q in (0.5, 0.9, 0.99, 1.0)
        },
        "residual_over_S_rms": float(np.sqrt(np.mean(residual**2)) / S),
        "actual_distinct_alias_indices": int(np.unique(m_actual).size),
        "weyl_distinct_alias_indices": int(np.unique(m_pred).size),
        "same_nearest_alias_fraction": float(np.mean(m_actual == m_pred)),
        "scope": "finite eigenvalue diagnostic; principal Weyl density does not imply individual-gap asymptotics",
    })
    print(json.dumps(rows[-1], sort_keys=True), flush=True)

result = {
    "source_revision": "5171af01191cc2db9d5bad0f8eca2185114ebbe3",
    "exact_side_runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
    "derivation": "A_plus(lambda)=pi*(2-sqrt(lambda)); five-site Weyl count gives N_{<=lambda}~5*S*sqrt(lambda), so lambda_j~(j/(5*S))^2 and alpha_j~(S+1)*(2j+1)/(100*S).",
    "rows": rows,
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
