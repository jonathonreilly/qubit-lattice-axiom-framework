#!/usr/bin/env python3
"""Test whether principal-Weyl quadratic aliases select the important lags."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.linalg import eigh_tridiagonal

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / "scripts" / "postmark_electric_exact_side_fixed_index_kernel_2026_09_24.py"
OUT = Path(__file__).with_name("quadratic_phase_resonant_lag_probe.json")
EPS = (0.01, 0.03, 0.1)

spec = importlib.util.spec_from_file_location("exact_side_quad", RUNNER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

def wrap(x):
    return (x + np.pi) % (2 * np.pi) - np.pi

rows = []
for S in (96, 192, 384, 512):
    lo, hi, d, e, _ = module.finite_spin_matrix(S)
    lam, U = eigh_tridiagonal(d, e, eigvals_only=False)
    profile, _ = module.infinite_reference_profile(0.25, radius=24)
    nodes = np.arange(lo, hi + 1)
    eta = np.zeros(len(nodes), dtype=np.complex128)
    for n, val in profile.items():
        eta[n - lo] = val
    c = U.T @ eta
    char = np.cos(2 * np.pi * np.remainder(nodes, 3) / 3)
    V = U.T @ (char[:, None] * U)
    D = len(lam)
    C = S * (S + 1)
    theta = C * lam / 4.0
    j = np.arange(D, dtype=float)
    # Stable least-squares quadratic fit; the constant phase cancels in q.
    x = j / max(1.0, D - 1)
    coeff_fit = np.linalg.lstsq(np.column_stack((x*x, x, np.ones(D))), theta, rcond=None)[0]
    theta_fit = coeff_fit[0]*x*x + coeff_fit[1]*x + coeff_fit[2]
    resid = theta - theta_fit
    state_exact = U @ (np.exp(1j * theta) * c)
    state_fit = U @ (np.exp(1j * theta_fit) * c)
    q_exact = np.vdot(state_exact, char * state_exact)
    q_fit = np.vdot(state_fit, char * state_fit)
    a_fit = float(coeff_fit[0] / (D - 1)**2)
    b_fit = float(coeff_fit[1] / (D - 1))
    a_weyl = (S + 1) / (100.0 * S)
    lags = []
    for h in range(1, D):
        w = np.conjugate(c[:-h]) * c[h:] * np.diag(V, k=h)
        ph = theta[h:] - theta[:-h]
        z = np.sum(w * np.exp(1j * ph))
        lags.append({"h": h, "real": float(z.real), "imag": float(z.imag), "abs": float(abs(z))})
    lag_arr = np.array([v["h"] for v in lags], dtype=int)
    lag_z = np.array([v["real"] + 1j*v["imag"] for v in lags])
    lag_abs = np.abs(lag_z)
    row = {
        "S": S, "dimension": D,
        "principal_weyl_quadratic_coefficient": float(a_weyl),
        "fitted_theta_coefficients_a_b": [a_fit, b_fit],
        "fit_residual_abs_quantiles_rad": {str(q): float(np.quantile(np.abs(resid), q)) for q in (0.5, 0.9, 0.99, 1.0)},
        "fit_residual_rms_rad": float(np.sqrt(np.mean(resid**2))),
        "q_exact_real_imag": [float(q_exact.real), float(q_exact.imag)],
        "q_quadratic_fit_real_imag": [float(q_fit.real), float(q_fit.imag)],
        "q_fit_absolute_error": float(abs(q_exact - q_fit)),
        "lag_resonance_bins": {},
        "largest_lag_terms": sorted(lags, key=lambda v:v["abs"], reverse=True)[:12],
        "scope": "finite float64 diagnostic; a fitted phase is a discriminator, not a theorem or asymptotic substitution",
    }
    for eps in EPS:
        # For theta_j ~= a*j^2+b*j, the lag-h phase derivative is 2*a*h.
        mask_weyl = np.abs(wrap(2*a_weyl*lag_arr)) < eps
        mask_fit = np.abs(wrap(2*a_fit*lag_arr)) < eps
        row["lag_resonance_bins"][str(eps)] = {
            "weyl_alias_lag_count": int(np.count_nonzero(mask_weyl)),
            "weyl_alias_sum_abs_Lh": float(np.sum(lag_abs[mask_weyl])),
            "weyl_alias_signed_real_Lh": float(np.sum(lag_z[mask_weyl].real)),
            "weyl_alias_signed_readout_contribution": float(2*np.sum(lag_z[mask_weyl].real)),
            "fitted_alias_lag_count": int(np.count_nonzero(mask_fit)),
            "fitted_alias_sum_abs_Lh": float(np.sum(lag_abs[mask_fit])),
            "fitted_alias_signed_real_Lh": float(np.sum(lag_z[mask_fit].real)),
            "fitted_alias_signed_readout_contribution": float(2*np.sum(lag_z[mask_fit].real)),
            "all_lag_sum_abs_Lh": float(np.sum(lag_abs)),
            "all_lag_signed_real_Lh": float(np.sum(lag_z.real)),
        }
    rows.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)
    del lam, U, V, c, state_exact, state_fit

result = {
    "source_revision": "5171af01191cc2db9d5bad0f8eca2185114ebbe3",
    "exact_side_runner_sha256": hashlib.sha256(RUNNER.read_bytes()).hexdigest(),
    "derivation": "A_plus(lambda)=pi(2-sqrt(lambda)) gives principal Weyl count N_{<=lambda}~5S sqrt(lambda), hence lambda_j~(j/(5S))^2 and theta_j~(S+1)j^2/(100S). A quadratic phase predicts lag-derivative aliases at 2*a*h=2*pi*m, i.e. h near 100*pi*m.",
    "rows": rows,
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
