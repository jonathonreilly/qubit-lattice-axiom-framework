#!/usr/bin/env python3
"""Direct parent potential reconstruction and explicit local quadratic diagnostics."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
import sympy as sp

ROOT = Path(__file__).resolve().parent
CHECKS = []


def check(name, condition, **evidence):
    passed = bool(condition)
    CHECKS.append({"name": name, "pass": passed, **evidence})
    assert passed, (name, evidence)


def symbolic_checks():
    a, p, h, d = sp.symbols("a p h d", nonzero=True)
    pd = h + d + (1 - h) * p + (1 / a - 1) * p ** 2
    hd = h * (-3 - 2 * h)
    dd = d * (2 * p - 3 - 2 * h)
    c = h + (1 + a) * d + 4 * p + (1 / a - 3) * p ** 2
    f = 3 * (1 - p) ** 2 - p ** 2 / a - 2 * d
    fd = sp.diff(f, p) * pd + sp.diff(f, d) * dd
    check("inverse_potential_KG_identity", sp.factor((p + h) * f + fd / 2 + p * c / a) == 0)
    cd = sp.diff(c, h) * hd + sp.diff(c, p) * pd + sp.diff(c, d) * dd
    turning = sp.factor((-(2 * p + 2 * h) * c - cd).subs(p, 0))
    check("turning_point_derivative_identity", sp.factor(turning + h + (1 - 3 * a) * d) == 0)
    check("present_zero_drift_obstruction", sp.factor(turning.subs(h, -(1 + a) * d) - 4 * a * d) == 0)
    check("present_zero_gradient", sp.factor(c.subs({p: 0, h: -(1 + a) * d})) == 0)
    s, cc, eta, k = sp.symbols("s cc eta k", positive=True)
    sg2, sgg = 4 * k ** 2 * s * (cc + s), 2 * k ** 2 * (cc + 2 * s)
    determinant = (1 + eta) * s * a * sgg / 2 - a * sg2
    expected = a * k ** 2 * s * ((eta - 3) * cc + (2 * eta - 2) * s)
    check("two_field_hessian_determinant", sp.factor(determinant - expected) == 0)
    check("eta_three_positive_determinant", sp.factor(expected.subs(eta, 3) - 4 * a * k ** 2 * s ** 2) == 0)
    # Squared branch relation; the chosen negative sinh branch fixes its sign.
    k2 = 3 * (1 + a) / (2 * a)
    h2 = sp.Rational(2, 3) * (1 + a) * (cc + s)
    check("tracking_gradient_relation", sp.factor(4 * k2 * s * (cc + s) - 9 * h2 * s / a) == 0)
    check("tracking_friedmann", sp.expand(2 * s + a * s + 2 * (sp.Symbol('v0') + a * s / 2)
                                          - (2 * (1 + a) * s + 2 * sp.Symbol('v0'))) == 0)
    return {"inverse_p_prime": str(pd), "turning_derivative_times_sqrt_a": str(turning),
            "hessian_determinant": str(sp.factor(expected))}


def inverse_endpoint(f):
    rows = []
    for a in f["weak_couplings"]:
        for m in f["matter_fractions"]:
            d0 = 1.5 * m / (1 + a)

            def equations(n, state):
                zeta, p = state
                e2 = m * math.exp(-3 * n) + 1 - m
                h = -1.5 * m * math.exp(-3 * n) / e2
                d = 1.5 * m * math.exp(2 * zeta - 3 * n) / ((1 + a) * e2)
                return [p, h + d + (1 - h) * p + (1 / a - 1) * p * p]

            sol = solve_ivp(equations, (0, min(f["one_field_endpoint_n"])), [0, 0],
                            method="DOP853", rtol=2e-13, atol=2e-16, max_step=0.002, dense_output=True)
            check(f"inverse_endpoint_integration_{a}_{m}", sol.success)
            sites = []
            for n in f["one_field_endpoint_n"]:
                zeta, p = sol.sol(n)
                e2 = m * math.exp(-3 * n) + 1 - m
                h = -1.5 * m * math.exp(-3 * n) / e2
                d = 1.5 * m * math.exp(2 * zeta - 3 * n) / ((1 + a) * e2)
                pd = equations(n, [zeta, p])[1]
                hd, dd = h * (-3 - 2 * h), d * (2 * p - 3 - 2 * h)
                c = h + (1 + a) * d + 4 * p + (1 / a - 3) * p * p
                cd = hd + (1 + a) * dd + (4 + 2 * (1 / a - 3) * p) * pd
                prefactor = math.exp(2 * zeta) * e2
                phi = zeta / math.sqrt(a)
                gradient = -prefactor * c / math.sqrt(a)
                mass2 = -prefactor * ((2 * p + 2 * h) * c + cd) / p
                potential = prefactor / 2 * (3 * (1 - p) ** 2 - p * p / a - 2 * d)
                ratio_phi = phi / (-math.sqrt(a) * d0 * n * n / 2)
                ratio_gradient = gradient / (4 * math.sqrt(a) * d0 * n)
                ratio_mass = mass2 / (-4 / n)
                check(f"inverse_past_branch_{a}_{m}_{n}", phi < 0 and p > 0 and mass2 > 0 and potential > 0)
                sites.append({"n": n, "zeta": float(zeta), "p": float(p), "phi": float(phi),
                              "V_over_H0_squared": float(potential), "V_phi_over_H0_squared": float(gradient),
                              "V_phiphi_over_H0_squared": float(mass2), "phi_leading_ratio": float(ratio_phi),
                              "gradient_leading_ratio": float(ratio_gradient), "mass_leading_ratio": float(ratio_mass)})
            last = sites[-1]
            check(f"one_sided_cusp_scaling_{a}_{m}",
                  max(abs(last[k] - 1) for k in ["phi_leading_ratio", "gradient_leading_ratio", "mass_leading_ratio"])
                  < f["one_field_cusp_ratio_tolerance_at_last_site"], last=last)
            rows.append({"a": a, "m": m, "endpoint_phi_prime": 0,
                         "endpoint_gradient_derivative_over_H0_squared": 4 * math.sqrt(a) * d0,
                         "smooth_C2_necessary_value": 0, "sites": sites,
                         "disposition": "Exact zero-drift endpoint violates necessary one-field C2 compatibility under supplied target and density."})
    return rows


def constants(a, m):
    v0 = 1.5 * (1 - m)
    cc = v0 / (1 + a)
    k = math.sqrt(3 * (1 + a) / (2 * a))
    chi_c = math.asinh(math.sqrt(m / (1 - m))) / k
    return v0, cc, k, chi_c


def potential(u, chi, a, m, eta):
    v0, cc, k, chi_c = constants(a, m)
    t = k * (chi - chi_c)
    sh, ch = math.sinh(t), math.cosh(t)
    s = cc * sh * sh
    sg = 2 * cc * k * sh * ch
    sgg = 2 * cc * k * k * (ch * ch + sh * sh)
    q = (u - math.sqrt(a)) ** 2 + eta * u * u
    qu = (1 + eta) * u - math.sqrt(a)
    val = v0 + s * q / 2
    grad = np.array([s * qu, sg * q / 2])
    hessian = np.array([[(1 + eta) * s, sg * qu], [sg * qu, sgg * q / 2]])
    return val, grad, hessian, s, sg, sgg


def analytic_background(n, a, m):
    v0, cc, k, chi_c = constants(a, m)
    chi = chi_c - math.asinh(math.sqrt(m / (1 - m)) * math.exp(-1.5 * n)) / k
    s = 1.5 * m * math.exp(-3 * n) / (1 + a)
    h = math.sqrt(m * math.exp(-3 * n) + 1 - m)
    velocity = math.sqrt(a * s)
    return chi, s, h, velocity


def hessian_and_background_grid(f):
    rows = []
    couplings = f["weak_couplings"] + [f["additional_mathematical_coupling"]]
    for a in couplings:
        for m in f["matter_fractions"]:
            v0, cc, k, chi_c = constants(a, m)
            for eta in f["eta_choices"]:
                for n in f["N_grid"]:
                    chi, s, h, velocity = analytic_background(n, a, m)
                    val, grad, mat, spv, sg, sgg = potential(0, chi, a, m, eta)
                    eigs = np.linalg.eigvalsh(mat)
                    det = a * k * k * s * ((eta - 3) * cc + (2 * eta - 2) * s)
                    numeric_det = float(np.linalg.det(mat))
                    name = f"a{a}_m{m}_eta{eta}_n{n}"
                    defects = [spv - s, 3 * h * h - 2 * s - velocity ** 2 - 2 * val,
                               grad[0] + math.sqrt(a) * s, grad[1] + 1.5 * h * velocity,
                               sg * velocity + 3 * h * s]
                    scale = max(1, abs(val), h * h, s)
                    check("background_identities_" + name, max(abs(x) for x in defects) < 2e-11 * scale,
                          maximum_absolute_defect=max(abs(x) for x in defects))
                    check("hessian_determinant_" + name, abs(numeric_det - det) < 2e-11 * max(1, abs(det)),
                          direct=numeric_det, analytic=det)
                    if eta == 0:
                        check("preserve_original_negative_curvature_" + name, det < 0 and eigs[0] < 0)
                    if eta >= 3:
                        check("repaired_positive_curvature_" + name, det > 0 and eigs[0] > 0)
                    values = [potential(t * math.sqrt(a), chi, a, m, eta)[0] for t in [-2, -0.5, 0, 0.5, 1, 2]]
                    check("positive_potential_" + name, min(values) >= v0 - 2e-12)
                    rows.append({"a": a, "m": m, "eta": eta, "n": n, "chi": chi, "S_over_H0_squared": s,
                                 "H_over_H0": h, "chi_dot_over_H0": velocity, "V_over_H0_squared": val,
                                 "hessian_over_H0_squared": mat.tolist(), "hessian_eigenvalues": eigs.tolist(),
                                 "determinant": det, "eta_required_at_site": (3 * cc + 2 * s) / (cc + 2 * s),
                                 "positive_curvature_at_site": bool(eigs[0] > 0)})
    return rows


def full_homogeneous_evolution(f):
    results = []
    for index, fixture in enumerate(f["two_field_ode"]):
        a, m, eta = [fixture[k] for k in ["a", "m", "eta"]]
        alpha = np.array([math.sqrt(a), 0.0])
        _, s0, _, vchi0 = analytic_background(0, a, m)
        initial = np.array([0, 0, 0, vchi0, s0, 0.0])

        def func(nstar, state):
            u, chi, vu, vc, sigma, time_j = state
            val, grad, _, _, _, _ = potential(u, chi, a, m, eta)
            v = np.array([vu, vc])
            h = math.sqrt((2 * sigma + np.dot(v, v) + 2 * val) / 3)
            dv = -3 * v - (grad + alpha * sigma) / h
            ds = sigma * (-3 + np.dot(alpha, v) / h)
            return np.r_[v / h, dv, ds, math.exp(math.sqrt(a) * u) / h]

        levels = []
        for lev, max_step in enumerate(f["ode_max_steps"]):
            opts = dict(method=f["ode_method"], rtol=f["ode_relative_tolerances"][lev],
                        atol=f["ode_absolute_tolerances"][lev], max_step=max_step, dense_output=True)
            sols = [solve_ivp(func, (0, end), initial, **opts) for end in f["ode_interval_N_star"]]
            check(f"two_field_full_ode_success_{index}_{lev}", all(s.success for s in sols))
            rows = []
            for nstar in f["ode_comparison_N_star"]:
                state = sols[0 if nstar < 0 else 1].sol(nstar)
                u, chi, vu, vc, sigma, time_j = state
                aj = math.exp(math.sqrt(a) * u)
                nj = nstar + math.sqrt(a) * u
                val = potential(u, chi, a, m, eta)[0]
                he = math.sqrt((2 * sigma + vu * vu + vc * vc + 2 * val) / 3)
                hj = (he + math.sqrt(a) * vu) / aj
                chi_exact, sig_exact, hj_exact, vc_exact = analytic_background(nj, a, m)
                got = np.array([u, chi, vu, vc, sigma, hj])
                exact = np.array([0, chi_exact, 0, vc_exact, sig_exact, hj_exact])
                error = np.abs(got - exact)
                allowed = f["ode_comparison_absolute_tolerance"] + f["ode_comparison_relative_tolerance"] * np.abs(exact)
                check(f"two_field_analytic_tracking_{index}_{lev}_{nstar}", np.all(error < allowed), maximum_absolute=float(np.max(error)))
                check(f"dust_first_integral_{index}_{lev}_{nstar}",
                      abs(sigma * math.exp(3 * nstar - math.sqrt(a) * u) - s0) < 2e-9)
                rows.append({"N_star": nstar, "n_J": nj, "state": state.tolist(), "H_J_over_H0": hj,
                             "physical_G_over_present": aj * aj, "maximum_absolute_tracking_error": float(np.max(error))})
            levels.append(rows)
        deltas = [np.array(x["state"]) - np.array(y["state"]) for x, y in zip(*levels)]
        refinement = float(np.max(np.abs(deltas)))
        check(f"two_field_ode_refinement_{index}", refinement < 2e-9, maximum_absolute=refinement)
        results.append({"fixture": fixture, "levels": levels, "maximum_state_refinement_error": refinement})
    return results


def local_mass_and_force(f):
    rows = []
    for a in f["weak_couplings"]:
        m = f["observationally_compared_benchmark_m"]
        chi, s, _, _ = analytic_background(0, a, m)
        mat = potential(0, chi, a, m, f["eta_repaired"])[2]
        for choice in f["matrix_choices"]:
            current = mat.copy()
            if choice == "potential_hessian_plus_fixed_number_dust":
                current[0, 0] += a * s
            eigenvalues, eigenvectors = np.linalg.eigh(current)
            weights = a * eigenvectors[0, :] ** 2
            check(f"positive_local_residues_{a}_{choice}", np.all(eigenvalues > 0) and np.all(weights >= 0)
                  and abs(np.sum(weights) - a) < 1e-15)
            check(f"mass_weighted_sum_rule_{a}_{choice}", abs(weights @ eigenvalues - a * current[0, 0]) < 1e-13)
            scales = [("dimensionless", scale) for scale in f["local_dimensionless_H0_r_over_c_controls"]]
            scales += [(f"illustrative_radius_{radius}_m", f["H0_per_second_illustrative"] * radius / f["c_m_per_second"])
                       for radius in f["local_radius_m_illustrative"]]
            force_rows = []
            for label, scale in scales:
                xs = np.sqrt(eigenvalues) * scale
                deficits = [float(x * x * quad(lambda t: t * math.exp(-x * t), 0, 1,
                                             epsabs=f["force_quadrature_epsabs"], epsrel=f["force_quadrature_epsrel"])[0]) for x in xs]
                deficit = float(weights @ np.array(deficits)) / (1 + a)
                upper = a * current[0, 0] * scale * scale / (2 * (1 + a))
                check(f"Yukawa_force_bound_{a}_{choice}_{label}_{scale}",
                      deficit >= 0 and deficit <= upper * (1 + 2e-12) + 1e-300,
                      actual_mass_correction=deficit, bound=upper)
                if scale >= 1e-3:
                    closed = float(weights @ (1 - (1 + xs) * np.exp(-xs))) / (1 + a)
                    check(f"Yukawa_integral_identity_{a}_{choice}_{scale}", abs(closed - deficit) < 1e-15)
                force_rows.append({"label": label, "H0_r_over_c": scale, "mu_r": xs.tolist(),
                                   "relative_mass_force_deficit": deficit, "relative_bound": upper})
            rows.append({"a": a, "m": m, "eta": f["eta_repaired"], "quadratic_diagnostic": choice,
                         "mass_matrix_over_H0_squared": current.tolist(), "mass_squared_eigenvalues": eigenvalues.tolist(),
                         "positive_residues": weights.tolist(), "force_controls": force_rows})
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError(args.output)
    fixtures = json.loads((ROOT / "NUMERICAL_FIXTURES.json").read_text())
    result = {"author": "direct parent", "units": "H0=1 and4pi G*rho=sigma internally; scalar fields dimensionless",
              "versions": {"numpy": np.__version__, "scipy": scipy.__version__, "sympy": sp.__version__},
              "source_sha256": {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in
                                ["PROTOCOL.md", "DIRECT_POTENTIAL_RECONSTRUCTION.md", "NUMERICAL_FIXTURES.json", Path(__file__).name]}}
    result["symbolic"] = symbolic_checks()
    result["single_field_endpoint"] = inverse_endpoint(fixtures)
    result["potential_grid"] = hessian_and_background_grid(fixtures)
    result["two_field_evolution"] = full_homogeneous_evolution(fixtures)
    result["local_quadratic_force"] = local_mass_and_force(fixtures)
    result["historical_drift"] = {"prediction_per_year": 0,
                                  "exposed_mean_per_year": fixtures["historical_LLR_drift_per_year_mean"],
                                  "reported_uncertainty_per_year": fixtures["historical_LLR_drift_per_year_reported_uncertainty"],
                                  "standardized_residual": fixtures["historical_LLR_drift_per_year_mean"] / fixtures["historical_LLR_drift_per_year_reported_uncertainty"],
                                  "reported_tidal_correlation": fixtures["historical_LLR_tidal_correlation"],
                                  "scope": "Historical exposed processed summary; leading homogeneous-to-local tracking assumption. No joint independent likelihood with prior LLR EP result."}
    result["checks"] = CHECKS
    result["checks_count"] = len(CHECKS)
    result["all_passed"] = all(x["pass"] for x in CHECKS)
    args.output.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"checks": len(CHECKS), "all_passed": result["all_passed"], "grid_rows": len(result["potential_grid"]),
                      "eta0_negative_curvature_rows": sum(x["eta"] == 0 and not x["positive_curvature_at_site"] for x in result["potential_grid"]),
                      "eta3_positive_curvature_rows": sum(x["eta"] == 3 and x["positive_curvature_at_site"] for x in result["potential_grid"]),
                      "max_tracking_error": max(t["maximum_absolute_tracking_error"] for row in result["two_field_evolution"] for level in row["levels"] for t in level),
                      "max_refinement_error": max(row["maximum_state_refinement_error"] for row in result["two_field_evolution"]),
                      "drift": result["historical_drift"]}, indent=2))


if __name__ == "__main__":
    main()
