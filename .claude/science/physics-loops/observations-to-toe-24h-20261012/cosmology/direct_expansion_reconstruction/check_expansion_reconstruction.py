#!/usr/bin/env python3
"""Direct parent calculation; fixed fixtures, processed-data transfer, no shape fit."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.linalg import cho_factor, cho_solve
import sympy as sp

ROOT = Path(__file__).resolve().parent
CHECKS = []


def check(name, condition, **evidence):
    ok = bool(condition)
    CHECKS.append({"name": name, "pass": ok, **evidence})
    assert ok, (name, evidence)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def qb(a):
    return (1 + a) / (2 * (1 - a))


def bq(z, q):
    return -np.expm1(-q * np.log1p(z)) / q


def q_physical(a, os, ore, y):
    om = 1 - os - ore
    qe = om / 2 + ore + 2 * os
    return (qe + 2 * y + 1.5 * a * om) / (1 + y) ** 2


def square_identity_and_grid(f):
    a, y, os, ore = sp.symbols("a y os ore", real=True)
    om = 1 - os - ore
    qe = om / 2 + ore + 2 * os
    lhs = qe + 2 * y + 3 * a * om / 2 - (1 + y) ** 2 * (1 + a) / (2 * (1 - a))
    rhs = ((1 - 3 * a) * (y + a) ** 2 / (2 * a * (1 - a))
           + sp.Rational(3, 2) * (1 - a) * (os - y ** 2 / (3 * a))
           + (1 - 3 * a) * ore / 2)
    check("symbolic_square_identity", sp.factor(lhs - rhs) == 0)
    # Constant dust trajectory satisfies the actual velocity evolution.
    xe, ae = sp.symbols("xe ae", positive=True)
    fixed_rhs = ((sp.Rational(1, 2) + ae / 2 - 2) * (-xe)
                 - sp.Rational(3, 2) * xe * (1 - ae / 3))
    check("symbolic_equality_trajectory", sp.expand(fixed_rhs) == 0)
    rows = []
    d = f["simplex_denominator"]
    for av in f["couplings"]:
        for si in range(d + 1):
            for ri in range(d + 1 - si):
                sv, rv = si / d, ri / d
                for ti, t in enumerate(f["projection_fractions"]):
                    yv = t * math.sqrt(3 * av * sv)
                    qj = q_physical(av, sv, rv, yv)
                    residual = (1 + yv) ** 2 * (qj - qb(av))
                    if av:
                        squares = ((1 - 3 * av) * (yv + av) ** 2 / (2 * av * (1 - av))
                                   + 1.5 * (1 - av) * (sv - yv ** 2 / (3 * av))
                                   + (1 - 3 * av) * rv / 2)
                    else:
                        squares = 1.5 * sv + rv / 2
                    name = f"simplex_a{av}_s{si}_r{ri}_t{ti}"
                    check(name, qj >= qb(av) - f["identity_atol"]
                          and abs(residual - squares) < f["identity_atol"]
                          and 1 + yv > 0,
                          q_J=qj, q_bound=qb(av), square_error=residual - squares)
                    rows.append([av, sv, rv, t, yv, qj, residual, squares])
    return {"columns": ["a", "Omega_s", "Omega_r", "projection_fraction", "y", "q_J", "bound_residual", "squares"],
            "rows": rows, "row_count": len(rows)}


def history(fixture, max_step, f):
    av = fixture["a"]
    alpha = np.array([math.sqrt(av), 0.0])
    t = fixture["projection"]
    x = math.sqrt(3 * fixture["omega_s"]) * np.array([t, math.sqrt(1 - t * t)])
    initial = np.r_[np.zeros(2), x, fixture["omega_r"], 0.0, 0.0]

    def fun(n, state):
        phi, vel, rad = state[:2], state[2:4], state[4]
        os = np.dot(vel, vel) / 3
        om = 1 - os - rad
        qe = om / 2 + rad + 2 * os
        return np.r_[vel, (qe - 2) * vel - 1.5 * alpha * om,
                     2 * (qe - 1) * rad, -(1 + qe), math.exp(np.dot(alpha, phi) - state[5])]

    endpoints = f["evolution_interval_N"]
    options = dict(method=f["ode_method"], rtol=f["ode_rtol"], atol=f["ode_atol"],
                   max_step=max_step, dense_output=True)
    sols = [solve_ivp(fun, (0, end), initial, **options) for end in endpoints]
    check(f"ode_success_{fixture['id']}_{max_step}", all(s.success for s in sols))

    def at(n):
        return sols[0 if n < 0 else 1].sol(n)

    def physical(n):
        state = at(n)
        return math.exp(n + np.dot(alpha, state[:2])), state[6]

    rows = []
    for n in f["comparison_N"]:
        state = at(n)
        sv, rv = np.dot(state[2:4], state[2:4]) / 3, state[4]
        om = 1 - sv - rv
        y = np.dot(alpha, state[2:4])
        qj = q_physical(av, sv, rv, y)
        check(f"ode_state_{fixture['id']}_{max_step}_{n}",
              min(sv, rv, om) >= -f["simplex_atol"] and 1 + y > 0
              and qj >= qb(av) - f["simplex_atol"], Omega_m=om, Omega_r=rv, Omega_s=sv, q_J=qj)
        ra, ta = physical(n)
        estimates = []
        for h in f["derivative_steps"]:
            rp, tp = physical(n + h)
            rm, tm = physical(n - h)
            r1, t1 = (rp - rm) / (2 * h), (tp - tm) / (2 * h)
            r2, t2 = (rp - 2 * ra + rm) / h ** 2, (tp - 2 * ta + tm) / h ** 2
            estimates.append(-ra * (r2 - r1 * t2 / t1) / r1 ** 2)
        richardson = (4 * estimates[1] - estimates[0]) / 3
        check(f"frame_derivative_{fixture['id']}_{max_step}_{n}",
              abs(estimates[1] - qj) < f["q_finite_difference_atol"]
              and abs(richardson - qj) < f["q_refined_richardson_atol"],
              finite_difference=estimates, richardson=richardson, analytic=qj)
        if fixture["id"] in ["uncoupled_dust", "weak_equality"]:
            check(f"equality_evolution_{fixture['id']}_{max_step}_{n}", abs(qj - qb(av)) < 1e-10)
        rows.append({"N": n, "state": state.tolist(), "Omega_m": om, "Omega_r": rv,
                     "Omega_s": sv, "y": float(y), "q_J": float(qj),
                     "scale_J": ra, "time_J": ta, "finite_difference_q": estimates,
                     "richardson_q": richardson})
    return rows


def evolution_controls(f):
    results = []
    for fixture in f["evolution"]:
        levels = [history(fixture, h, f) for h in f["ode_max_steps"]]
        error = max(np.max(np.abs(np.array(a["state"]) - np.array(b["state"])))
                    for a, b in zip(*levels))
        check(f"ode_refinement_{fixture['id']}", error < f["ode_refinement_atol"], maximum_absolute=error)
        results.append({"fixture": fixture, "max_state_refinement_error": float(error), "levels": levels})
    # A physical second derivative rejects both missing-frame and wrong-trace formulas.
    row = results[-1]["levels"][-1][4]
    av = results[-1]["fixture"]["a"]
    y, om, sv, rv = row["y"], row["Omega_m"], row["Omega_s"], row["Omega_r"]
    qe = om / 2 + rv + 2 * sv
    false = {"missing_2y": (qe + 1.5 * av * om) / (1 + y) ** 2,
             "wrong_trace_sign": (qe + 2 * y - 1.5 * av * om) / (1 + y) ** 2}
    for name, value in false.items():
        check("reject_" + name, abs(value - row["richardson_q"]) > 1e-3,
              false_q=value, physical_derivative_q=row["richardson_q"])
    return results


def distance_controls(f):
    rows = []
    for q in [0.5, qb(1 / 2499)]:
        for curvature in [0, 0.3, 1.0]:
            ratios = []
            for z in f["distance_grid"]:
                direct_b, err = quad(lambda u: (1 + u) ** (-1 - q), 0, z, epsabs=1e-13, epsrel=1e-13)
                check(f"B_integral_{q}_{curvature}_{z}", abs(direct_b - bq(z, q)) < 2e-13)
                inverse_h = lambda u: (1 + u) ** (-1 - q - curvature) * math.exp(curvature - curvature / (1 + u))
                distance = quad(inverse_h, 0, z, epsabs=1e-13, epsrel=1e-13)[0]
                ratios.append(distance / bq(z, q))
            check(f"monotone_distance_ratio_{q}_{curvature}", np.max(np.diff(ratios)) < 2e-12,
                  ratios=ratios)
            rows.append({"q_lower": q, "q_extra_z_over_1plusz": curvature, "ratios": ratios})
    return rows


def primary_bytes(name, manifest):
    item = manifest["files"][name]
    zipped = (ROOT / item["local_gzip"]).read_bytes()
    check("gzip_hash_" + name, sha(zipped) == item["gzip_sha256"])
    data = gzip.decompress(zipped)
    check("primary_hash_" + name, sha(data) == item["raw_sha256"] and len(data) == item["raw_bytes"])
    return data


def data_comparison(f):
    manifest = json.loads((ROOT / "PRIMARY_DATA.json").read_text())
    table_bytes = primary_bytes("table", manifest)
    cov_bytes = primary_bytes("covariance", manifest)
    table = np.genfromtxt(io.BytesIO(table_bytes), names=True, dtype=None, encoding="utf-8")
    entries = np.fromstring(cov_bytes.decode("ascii"), sep=" ")
    n = int(entries[0])
    check("covariance_dimension", entries[0] == n and len(table) == n and len(entries) == 1 + n * n,
          table_rows=len(table), covariance_n=n, covariance_entries=len(entries) - 1)
    raw_cov = entries[1:].reshape(n, n)
    check("covariance_finite", np.isfinite(raw_cov).all())
    asymmetry = float(np.max(np.abs(raw_cov - raw_cov.T)))
    scale = float(np.max(np.diag(raw_cov)))
    check("covariance_text_symmetry", asymmetry <= f["covariance_symmetry_relative_to_max_diagonal"] * scale,
          maximum_asymmetry=asymmetry, diagonal_scale=scale)
    cov = (raw_cov + raw_cov.T) / 2
    all_factor = cho_factor(cov, lower=True, check_finite=True)
    check("full_covariance_positive_definite", np.all(np.diag(all_factor[0]) > 0),
          minimum_cholesky_diagonal=float(np.min(np.diag(all_factor[0]))))
    z, zh, mag = [np.asarray(table[k], dtype=float) for k in ["zHD", "zHEL", "m_b_corr"]]
    check("magnitude_redshift_finite", all(np.isfinite(v).all() for v in [z, zh, mag]))
    selected = np.flatnonzero((table["IS_CALIBRATOR"] == 0) & (z >= 0.0233) & (z <= 1.5))
    z, zh, mag = z[selected], zh[selected], mag[selected]
    c = cov[np.ix_(selected, selected)]
    low = np.flatnonzero(z < 0.1)
    test = np.flatnonzero(z >= 0.1)
    high = np.flatnonzero((z >= 0.3) & (z <= 1.0))
    check("frozen_partition", len(low) > 1 and len(test) > 1 and len(high) > 1
          and len(low) + len(test) == len(selected) and np.min(z[high]) > np.max(z[low]))
    cll, ctl, ctt = c[np.ix_(low, low)], c[np.ix_(test, low)], c[np.ix_(test, test)]
    factor_l = cho_factor(cll, lower=True)
    one_l = np.ones(len(low))
    qi_one = cho_solve(factor_l, one_l)
    vm = 1 / np.dot(one_l, qi_one)
    b = cho_solve(factor_l, ctl.T).T
    v = np.ones(len(test)) - b @ one_l
    s = ctt - b @ ctl.T + vm * np.outer(v, v)
    s = (s + s.T) / 2
    factor_s = cho_factor(s, lower=True)
    factor_all = cho_factor(c, lower=True)
    check("predictive_covariance_positive_definite", np.all(np.diag(factor_s[0]) > 0))
    all_one = np.ones(len(z))
    all_qi_one = cho_solve(factor_all, all_one)
    # This full-data algebra identity is validation only; it is not the prediction fit.
    g_lcdm = []
    max_lcdm_refinement = 0.0
    for zi, zhi in zip(z, zh):
        ds = [quad(lambda u: 1 / math.sqrt(f["lcdm_omega_m"] * (1 + u) ** 3 + 1 - f["lcdm_omega_m"]),
                   0, zi, epsabs=e, epsrel=e)[0] for e in f["distance_quadrature_tolerances"]]
        max_lcdm_refinement = max(max_lcdm_refinement, abs(ds[0] - ds[1]))
        g_lcdm.append(5 * math.log10((1 + zhi) * ds[-1]))
    check("lcdm_distance_refinement", max_lcdm_refinement < 1e-9, maximum_absolute=max_lcdm_refinement)
    shapes = {"q_half": 5 * np.log10((1 + zh) * bq(z, 0.5)),
              "weak_equality": 5 * np.log10((1 + zh) * bq(z, qb(1 / 2499))),
              "supplied_LCDM_0.3": np.array(g_lcdm)}
    predictions = {}
    for name, g in shapes.items():
        dl = mag[low] - g[low]
        mhat = vm * np.dot(one_l, cho_solve(factor_l, dl))
        residual_l = dl - mhat
        chi_l = np.dot(residual_l, cho_solve(factor_l, residual_l))
        prediction = g[test] + b @ dl + v * mhat
        residual_t = mag[test] - prediction
        chi_t = np.dot(residual_t, cho_solve(factor_s, residual_t))
        dall = mag - g
        mhat_all = np.dot(all_qi_one, dall) / np.dot(all_qi_one, all_one)
        resall = dall - mhat_all
        chi_all = np.dot(resall, cho_solve(factor_all, resall))
        check("conditional_quadratic_identity_" + name,
              abs(chi_l + chi_t - chi_all) < f["conditional_identity_relative_tolerance"] * max(1, chi_all),
              calibration_chi2=float(chi_l), conditional_transfer_chi2=float(chi_t),
              full_profile_algebra_check_only=float(chi_all))
        predictions[name] = {"intercept_calibration_only": float(mhat), "intercept_standard_error": math.sqrt(vm),
                             "calibration_chi2": float(chi_l), "calibration_rank": len(low) - 1,
                             "conditional_transfer_chi2": float(chi_t), "transfer_dimension": len(test),
                             "shape_all_selected": g.tolist(), "prediction_transfer": prediction.tolist(),
                             "residual_calibration": residual_l.tolist(), "residual_transfer": residual_t.tolist(),
                             "full_profile_identity_is_not_a_test_fit": float(chi_all)}
    weights = np.zeros(len(selected))
    weights[high] = 1 / len(high)
    weights[low] = -1 / len(low)
    check("contrast_intercept_cancellation", abs(np.sum(weights)) < 1e-12)
    observed = float(np.dot(weights, mag - shapes["q_half"]))
    sigma = math.sqrt(float(weights @ c @ weights))
    log_lever = float(weights @ np.log10(1 + z))
    check("contrast_lever_positive", log_lever > 0)
    nuisance = [{"beta": beta, "corrected_contrast_mag": observed - beta * log_lever,
                 "standardized_contrast": (observed - beta * log_lever) / sigma}
                for beta in f["luminosity_evolution_beta"]]
    contrast = {"definition": "equal arithmetic high mean minus equal arithmetic low mean relative to q=.5 distance",
                "class_mean_upper_bound_mag": 0, "observed_mag": observed,
                "standard_error_full_covariance_mag": sigma, "standardized_contrast": observed / sigma,
                "high_rows": len(high), "low_rows": len(low), "log_luminosity_lever": log_lever,
                "beta_to_cancel_single_contrast_calibration_only": observed / log_lever,
                "frozen_beta_sensitivity": nuisance, "weights_all_selected": weights.tolist()}
    ids = np.asarray(table["CID"]).astype(str)
    counts = {"all_light_curve_rows": len(table), "all_distinct_CID": len(set(ids)),
              "selected_light_curve_rows": len(selected), "selected_distinct_CID": len(set(ids[selected])),
              "calibration_light_curve_rows": len(low), "calibration_distinct_CID": len(set(ids[selected[low]])),
              "transfer_light_curve_rows": len(test), "transfer_distinct_CID": len(set(ids[selected[test]])),
              "contrast_high_light_curve_rows": len(high), "contrast_high_distinct_CID": len(set(ids[selected[high]]))}
    return {"counts": counts, "raw_covariance_asymmetry": asymmetry, "covariance_diagonal_scale": scale,
            "covariance_convention": f["covariance_symmetrization"], "original_selected_row_indices_zero_based": selected.tolist(),
            "selected_CID": ids[selected].tolist(), "zHD": z.tolist(), "zHEL": zh.tolist(), "m_b_corr": mag.tolist(),
            "calibration_indices_in_selection": low.tolist(), "transfer_indices_in_selection": test.tolist(),
            "contrast_high_indices_in_selection": high.tolist(), "fixed_curves": predictions, "class_contrast": contrast,
            "prediction_covariance_sha256_float64_C_order": sha(np.asarray(s, dtype='<f8').tobytes()),
            "scope": "Exposed processed-summary comparison. No raw-photometry refit, global blind test, independent reuse of overlapping diagnostics, or luminosity-evolution claim."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    fixtures = json.loads((ROOT / "NUMERICAL_FIXTURES.json").read_text())
    result = {"author": "direct parent", "versions": {"numpy": np.__version__, "scipy": scipy.__version__, "sympy": sp.__version__},
              "source_hashes": {p: sha((ROOT / p).read_bytes()) for p in ["PROTOCOL.md", "NUMERICAL_FIXTURES.json", "DIRECT_EXPANSION_DERIVATION.md", "PRIMARY_DATA.json", Path(__file__).name]}}
    result["square_identity_grid"] = square_identity_and_grid(fixtures)
    result["direct_evolution"] = evolution_controls(fixtures)
    result["distance_controls"] = distance_controls(fixtures)
    result["processed_data"] = data_comparison(fixtures)
    result["checks"] = CHECKS
    result["checks_count"] = len(CHECKS)
    result["all_passed"] = all(row["pass"] for row in CHECKS)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    brief = {"checks": len(CHECKS), "all_passed": result["all_passed"],
             "counts": result["processed_data"]["counts"],
             "contrast": {k: v for k, v in result["processed_data"]["class_contrast"].items() if k != "weights_all_selected"},
             "curves": {k: {n: v[n] for n in ["intercept_calibration_only", "calibration_chi2", "calibration_rank", "conditional_transfer_chi2", "transfer_dimension"]} for k, v in result["processed_data"]["fixed_curves"].items()}}
    print(json.dumps(brief, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
