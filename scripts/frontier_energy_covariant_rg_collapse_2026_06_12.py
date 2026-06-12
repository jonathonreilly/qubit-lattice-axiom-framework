#!/usr/bin/env python3
"""Dense finite-ring verification of the energy-covariant Schur RG collapse.

The source note gives the algebraic all-admissible formula. This runner samples
finite rings away from the singular odd-block gate and checks the formula,
threshold, length, sign quotient, and chart boundary diagnostics.

    docs/ENERGY_COVARIANT_RG_COLLAPSE_SHIFTED_COUPLING_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_energy_covariant_rg_collapse_2026_06_12.py
"""
import sys

import numpy as np


PASS = 0
FAIL = 0
TOL = 1e-12


def check(name, condition, detail):
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {name}: {detail}")


def finish():
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        sys.exit(1)


def chain_matrix(n, t, mu):
    hmat = np.eye(n, dtype=float) * mu
    for i in range(n):
        j = (i + 1) % n
        hmat[i, j] = -t
        hmat[j, i] = -t
    return hmat


def schur_even_effective(n, t, mu, energy):
    hmat = chain_matrix(n, t, mu)
    even = np.arange(0, n, 2)
    odd = np.arange(1, n, 2)
    hee = hmat[np.ix_(even, even)]
    heo = hmat[np.ix_(even, odd)]
    hoe = hmat[np.ix_(odd, even)]
    hoo = hmat[np.ix_(odd, odd)]
    return hee - heo @ np.linalg.inv(hoo - energy * np.eye(len(odd))) @ hoe


def extract_uniform_nn(hmat):
    n = hmat.shape[0]
    diag = np.diag(hmat)
    mu_prime = float(np.mean(diag))
    nn_values = []
    for i in range(n):
        nn_values.append(hmat[i, (i - 1) % n])
        nn_values.append(hmat[i, (i + 1) % n])
    nn_values = np.array(nn_values, dtype=float)
    t_prime = -float(np.mean(nn_values))
    model = chain_matrix(n, t_prime, mu_prime)
    residual = float(np.max(np.abs(hmat - model)))
    diag_spread = float(np.max(np.abs(diag - mu_prime)))
    nn_spread = float(np.max(np.abs(nn_values + t_prime)))
    return mu_prime, t_prime, residual, diag_spread, nn_spread


def rg_map(h):
    return (h * h) / (1.0 - 2.0 * h * h)


def xi_analytic(h):
    return 1.0 / np.arccosh(1.0 / (2.0 * abs(h)))


def min_spectral_distance(n, t, mu, energy):
    shifted = chain_matrix(n, t, mu) - energy * np.eye(n)
    return float(np.min(np.abs(np.linalg.eigvalsh(shifted))))


def measured_xi(energy, h, r0, r1, n=128):
    delta = 1.0
    mu = energy + delta
    t = h * delta
    resolvent = np.linalg.inv(chain_matrix(n, t, mu) - energy * np.eye(n))
    rs = np.arange(r0, r1 + 1)
    values = np.abs(resolvent[0, rs])
    slope, intercept = np.polyfit(rs.astype(float), np.log(values), 1)
    xi = -1.0 / slope
    return float(xi), float(intercept), float(np.min(values)), float(np.max(values))


def main():
    print(
        "SCOPE: free 1D, the declared b=2 Schur convention, now E-COVARIANT "
        "in the shifted quotient coupling |h| = |t/(mu-E)| by the algebraic "
        "Schur formula; dense checks run on sampled admissible (E,t,mu) "
        "instances away from the singular odd-block gate, with chart "
        "|h| < 1/sqrt(2). NOT claimed: interacting, d=3, gauge, universality "
        "beyond the convention. Statuses pipeline-derived; audit lane grades."
    )

    energies = [-0.7, 0.3, 1.1]
    points = [
        (0.17, 2.8),
        (0.31, -2.4),
        (-0.23, 4.2),
        (0.41, -3.6),
    ]

    records = []
    for energy in energies:
        for t, mu in points:
            eff = schur_even_effective(16, t, mu, energy)
            mu_prime, t_prime, residual, diag_spread, nn_spread = extract_uniform_nn(eff)
            h = t / (mu - energy)
            shifted_identity_err = abs(
                (mu_prime - energy) - (mu - energy) * (1.0 - 2.0 * h * h)
            )
            collapse_err = abs(t_prime / (mu_prime - energy) - rg_map(h))
            records.append(
                {
                    "energy": energy,
                    "t": t,
                    "mu": mu,
                    "h": h,
                    "mu_prime": mu_prime,
                    "t_prime": t_prime,
                    "residual": residual,
                    "diag_spread": diag_spread,
                    "nn_spread": nn_spread,
                    "shifted_identity_err": shifted_identity_err,
                    "collapse_err": collapse_err,
                }
            )

    sampled_mu_e_gaps = [abs(r["mu"] - r["energy"]) for r in records]
    check(
        "X1 domain: every sampled (E,t,mu) has |mu-E| > 0.1",
        min(sampled_mu_e_gaps) > 0.1,
        "admissible-domain gate over the actual sample list; "
        f"min_abs_mu_minus_E={min(sampled_mu_e_gaps):.6g}, "
        f"samples={len(sampled_mu_e_gaps)}",
    )

    max_closure = max(r["residual"] for r in records)
    max_diag_spread = max(r["diag_spread"] for r in records)
    max_nn_spread = max(r["nn_spread"] for r in records)
    extracted_mu = [r["mu_prime"] for r in records]
    extracted_t = [r["t_prime"] for r in records]
    check(
        "X1a closure at E != 0",
        max_closure < TOL and max_diag_spread < TOL and max_nn_spread < TOL,
        "E={-0.7,0.3,1.1}, 4 points, N=16; "
        f"max_uniform_NN_residual={max_closure:.3e}, "
        f"diag_spread={max_diag_spread:.3e}, nn_spread={max_nn_spread:.3e}, "
        f"diag_prime_range=[{min(extracted_mu):.12g},{max(extracted_mu):.12g}], "
        f"t_prime_range=[{min(extracted_t):.12g},{max(extracted_t):.12g}]",
    )

    max_shift_err = max(r["shifted_identity_err"] for r in records)
    check(
        "X1b shift identity",
        max_shift_err < TOL,
        "mu_prime - E = (mu - E)(1 - 2 h^2) at every sampled admissible "
        "(E,t,mu) instance; the source note gives the algebraic all-domain "
        "formula for mu != E; "
        f"max_abs_error={max_shift_err:.3e}",
    )

    max_collapse_err = max(r["collapse_err"] for r in records)
    check(
        "X1c collapse on sampled admissible (E,t,mu) instances",
        max_collapse_err < TOL,
        "Schur h_prime equals h^2/(1 - 2 h^2) on the sampled grid; this "
        "matches the E=0 quotient map in the shifted coupling; "
        f"max_abs_error={max_collapse_err:.3e}",
    )

    singular_energy = 0.37
    singular_t = 0.4
    singular_mu = singular_energy
    singular_hmat = chain_matrix(16, singular_t, singular_mu)
    singular_odd = np.arange(1, 16, 2)
    singular_hoo = singular_hmat[np.ix_(singular_odd, singular_odd)]
    singular_block = singular_hoo - singular_energy * np.eye(len(singular_odd))
    min_singular_value = float(np.min(np.linalg.svd(singular_block, compute_uv=False)))
    try:
        schur_even_effective(16, singular_t, singular_mu, singular_energy)
        singular_decimation_rejected = False
        singular_decimation_detail = "decimation returned"
    except np.linalg.LinAlgError as exc:
        singular_decimation_rejected = True
        singular_decimation_detail = f"decimation raised {type(exc).__name__}"
    check(
        "mu=E excluded from the domain",
        min_singular_value < 1.0e-12 and singular_decimation_rejected,
        "at mu=E exactly with t=0.4, N=16, h_oo - E is singular and the "
        "runner decimation path rejects it; "
        f"min_singular_value={min_singular_value:.3e}, "
        f"{singular_decimation_detail}",
    )

    threshold_t = 1.0
    threshold_mu = 0.0
    below_energy = 2.5
    above_energy = 0.3
    threshold_rows = []
    covariance_ok = True
    for label, energy in [("below", below_energy), ("above", above_energy)]:
        h = threshold_t / (threshold_mu - energy)
        band_claim = abs(threshold_mu - energy) <= 2.0 * abs(threshold_t)
        shifted_claim = abs(h) >= 0.5
        gap64 = min_spectral_distance(64, threshold_t, threshold_mu, energy)
        gap128 = min_spectral_distance(128, threshold_t, threshold_mu, energy)
        threshold_rows.append((label, energy, h, band_claim, shifted_claim, gap64, gap128))
        covariance_ok = covariance_ok and (band_claim == shifted_claim)
    below = threshold_rows[0]
    above = threshold_rows[1]
    threshold_spectral_ok = (
        (not below[3])
        and below[5] > 0.45
        and below[6] > 0.45
        and above[3]
        and above[6] < above[5]
        and above[6] < 2.0e-2
    )
    check(
        "X1d threshold covariance",
        covariance_ok and threshold_spectral_ok,
        "|mu-E| <= 2|t| iff |h| >= 1/2 at E=2.5 and E=0.3; "
        f"below_gap64={below[5]:.6g}, below_gap128={below[6]:.6g}, "
        f"below_resolvent_norm128<={1.0 / below[6]:.6g}; finite-N witness "
        f"above_gap64={above[5]:.6g}, above_gap128={above[6]:.6g}",
    )

    xi_rows = []
    for energy, h, r0, r1 in [(-0.4, 0.31, 5, 24), (0.85, 0.44, 8, 42)]:
        xi_measured, intercept, vmin, vmax = measured_xi(energy, h, r0, r1)
        xi_expected = xi_analytic(h)
        rel_err = abs(xi_measured - xi_expected) / xi_expected
        xi_rows.append((energy, h, xi_measured, xi_expected, rel_err, vmin, vmax))
    max_xi_rel = max(row[4] for row in xi_rows)
    near_h = 0.49
    near_ratio = xi_analytic(rg_map(near_h)) / xi_analytic(near_h)
    check(
        "X1e energy-resolved length",
        max_xi_rel < 1.0e-3 and abs(near_ratio - 0.5) < 5.0e-2,
        "N=128 resolvent log-slope below threshold matches "
        "xi_E=1/arccosh(1/(2|h|)); "
        f"(E,h)=({xi_rows[0][0]:.3g},{xi_rows[0][1]:.3g}) "
        f"xi_meas={xi_rows[0][2]:.6g}, xi_exact={xi_rows[0][3]:.6g}, "
        f"rel={xi_rows[0][4]:.3e}; "
        f"(E,h)=({xi_rows[1][0]:.3g},{xi_rows[1][1]:.3g}) "
        f"xi_meas={xi_rows[1][2]:.6g}, xi_exact={xi_rows[1][3]:.6g}, "
        f"rel={xi_rows[1][4]:.3e}; xi(h')/xi(h) at h=0.49 is "
        f"{near_ratio:.6g}",
    )

    quotient_energy = 0.37
    quotient_t = 0.73
    quotient_mu = 1.2
    spec_plus = np.linalg.eigvalsh(
        chain_matrix(32, quotient_t, quotient_mu) - quotient_energy * np.eye(32)
    )
    spec_minus = np.linalg.eigvalsh(
        chain_matrix(32, -quotient_t, quotient_mu) - quotient_energy * np.eye(32)
    )
    sign_spectrum_err = float(np.max(np.abs(spec_plus - spec_minus)))
    chart_boundary_h = 0.7065
    chart_boundary_mu = quotient_energy + 1.0
    chart_boundary_t = chart_boundary_h * (chart_boundary_mu - quotient_energy)
    chart_eff = schur_even_effective(16, chart_boundary_t, chart_boundary_mu, quotient_energy)
    chart_mu_prime, chart_t_prime, _, _, _ = extract_uniform_nn(chart_eff)
    chart_boundary_h_prime = chart_t_prime / (chart_mu_prime - quotient_energy)
    sign_samples = np.array([0.11, 0.37, 0.61])
    evenness_err = float(np.max(np.abs(rg_map(sign_samples) - rg_map(-sign_samples))))
    finite_inside_chart = bool(np.all(np.isfinite(rg_map(sign_samples))))
    check(
        "X1f quotient/chart inherited",
        sign_spectrum_err < TOL
        and abs(chart_boundary_h_prime) > 50.0
        and evenness_err < 1.0e-15
        and finite_inside_chart,
        "E=0.37 sign quotient spectra(t) = spectra(-t); chart discloses "
        "boundary blow-up from actual Schur output at |h|=0.7065 just below "
        "1/sqrt(2)=0.70711; "
        f"sign_spectrum_err={sign_spectrum_err:.3e}, "
        f"abs_h_prime={abs(chart_boundary_h_prime):.6g}, "
        f"map_evenness_err={evenness_err:.3e}",
    )

    finish()


if __name__ == "__main__":
    main()
