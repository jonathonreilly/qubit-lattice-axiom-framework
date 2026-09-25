#!/usr/bin/env python3
"""Independent small controls of the finite-bin proof machinery.

Neither control builds the cubic record model or checks the provisional
23 I + W + W* effect. The Fourier check uses exact finite trigonometric
polynomials; the two-state jump model tests finite-bin integration and
the need to control evolution during the lag. No sampled value proves
an unbounded-domain theorem or a microscopic process comparison.
"""
from __future__ import annotations

import hashlib
import json
import math
import platform
import time
from pathlib import Path

import numpy as np
import scipy
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm


def cosine(v):
    """Multiply a finite Fourier polynomial by cos(theta), without wrap."""
    out = np.zeros(len(v) + 2, dtype=complex)
    out[:-2] += v / 2
    out[2:] += v / 2
    return out


def fourier_graph_rows():
    rows = []
    for g in (0.5, 0.25, 0.125, 0.0625):
        cutoff = math.ceil(8 / g)
        m = np.arange(-cutoff, cutoff + 1, dtype=float)
        ground = np.exp(-0.5 * g * g * m * m).astype(complex)
        first = -1j * g * m * ground
        ground /= np.linalg.norm(ground)
        first /= np.linalg.norm(first)
        for label, psi in (
            ("ground_polynomial", ground),
            ("complex_two_mode_polynomial", ground + (0.3 + 0.2j) * first),
        ):
            psi = psi / np.linalg.norm(psi)
            kinetic_scale = g * g / 2
            qpsi = m * m * psi
            vpsi = (np.pad(psi, 1) - cosine(psi)) / (g * g)
            hpsi = kinetic_scale * np.pad(qpsi, 1) + vpsi
            grad = 1j * m * psi
            grad_cos_grad = np.vdot(np.pad(grad, 1), cosine(grad)).real
            grad_v_grad = (np.vdot(grad, grad).real - grad_cos_grad) / (g * g)
            lap_v_expectation = np.vdot(np.pad(psi, 1), cosine(psi)).real / (g * g)
            h_norm_sq = np.vdot(hpsi, hpsi).real
            kinetic_norm_sq = kinetic_scale**2 * np.vdot(qpsi, qpsi).real
            potential_norm_sq = np.vdot(vpsi, vpsi).real
            identity_rhs = (kinetic_norm_sq + potential_norm_sq
                            + 2 * kinetic_scale * grad_v_grad
                            - kinetic_scale * lap_v_expectation)
            identity_error = abs(h_norm_sq - identity_rhs)
            # K ||Delta V||_infinity = 1/2 exactly in this one-angle model.
            graph_bound_margin = h_norm_sq + 0.5 - kinetic_norm_sq - potential_norm_sq
            shifts = []
            for nu in (-2, -1, 1, 2):
                diagonal = (m + nu) * (m + nu - 1)
                shifted_norm = np.linalg.norm(diagonal * psi)
                bound = 4 * np.linalg.norm(qpsi) + 4 * nu * nu + 1
                shifts.append({"nu": nu, "shifted_D_norm": float(shifted_norm),
                               "analytic_upper_bound": float(bound)})
                assert np.all(diagonal >= 0)
                assert np.all(diagonal <= 4 * m * m + 4 * nu * nu + 1)
                assert shifted_norm <= bound + 1e-10
            assert identity_error < 2e-10
            assert grad_v_grad > -1e-10
            assert graph_bound_margin > -1e-10
            rows.append({"g": g, "state": label, "cutoff": cutoff,
                         "H_norm": float(math.sqrt(h_norm_sq)),
                         "K_Q_norm": float(math.sqrt(kinetic_norm_sq)),
                         "integration_by_parts_error": float(identity_error),
                         "graph_bound_margin": float(graph_bound_margin),
                         "electric_translation_checks": shifts})
    return rows


def integrated_effect(A, eta, effect, lag):
    """Exact finite-matrix integral via an augmented Liouvillian exponential."""
    rho = np.outer(eta, eta.conj())
    eye = np.eye(2)
    L = np.kron(eye, A) + np.kron(A.conj(), eye)
    augmented = np.zeros((5, 5), dtype=complex)
    augmented[:4, :4] = L
    augmented[:4, 4] = rho.reshape(4, order="F")
    integral_rho = expm(lag * augmented)[:4, 4].reshape((2, 2), order="F")
    exact = float(np.trace(effect @ integral_rho).real)
    # Separately evaluate the same two-by-two semigroup integral.
    nodes, weights = leggauss(64)
    values = []
    for node in nodes:
        u = lag * (node + 1) / 2
        evolved = expm(u * A) @ eta
        values.append(float(np.vdot(evolved, effect @ evolved).real))
        assert np.linalg.norm(evolved) <= np.linalg.norm(eta) + 2e-12
    quadrature = float(lag * np.dot(weights, values) / 2)
    assert abs(exact - quadrature) < 2e-12 * max(1, exact)
    return exact, abs(exact - quadrature)


def finite_bin_rows():
    # This is a separate finite jump instrument, not a cubic-model truncation.
    # B_j* B_j = 5 I, selected next effect M, and total postbirth loss Gamma.
    kappa = 0.4
    first_total_rate = 2.3  # >= the selected first-mark rate 5*kappa = 2.
    interval = (0.07, 0.23)
    weight = (math.exp(-first_total_rate * interval[0])
              - math.exp(-first_total_rate * interval[1])) / first_total_rate
    effect = np.diag([5.2, 4.8]).astype(complex)
    other_loss = 0.3 * np.array([[1, 0.2], [0.2, 2]], dtype=complex)
    total_loss = effect + other_loss
    assert np.linalg.eigvalsh(other_loss).min() > 0
    rows = []
    for g in (0.4, 0.2, 0.1, 0.05, 0.025):
        H = np.array([[0.2, 1 / (g * g)], [1 / (g * g), -0.2]], dtype=complex)
        A = -1j * H - kappa * total_loss / 2
        eta_v = math.sqrt(5) * np.array([math.sqrt(0.5),
                        np.exp(1j * math.pi / 4) * math.sqrt(0.5)])
        eta_p = math.sqrt(5) * np.array([math.sqrt(0.5 - g * g),
                        np.exp(1j * (math.pi / 4 + 0.4 * g)) * math.sqrt(0.5 + g * g)])
        boundary = [float(np.vdot(eta, effect @ eta).real) for eta in (eta_v, eta_p)]
        assert abs(boundary[0] - 25) < 1e-12
        assert abs(boundary[1] - (25 - 2 * g * g)) < 1e-12
        for family, lag in (("controlled_lag_0.2_g5", 0.2 * g**5),
                            ("fixed_lag_0.01", 0.01)):
            vals = []
            for label, eta, f0 in zip(("v", "p"), (eta_v, eta_p), boundary):
                integral, quadrature_error = integrated_effect(A, eta, effect, lag)
                error = abs(integral - lag * f0)
                # Integral of 2 ||M|| ||eta|| ||A eta|| u over [0,lag].
                rigorous_bound = (np.linalg.norm(effect, 2) * np.linalg.norm(eta)
                                   * np.linalg.norm(A @ eta) * lag * lag)
                assert error <= rigorous_bound + 1e-13 * lag
                probability = kappa * kappa * weight * integral
                assert 0 <= probability <= 5 * kappa * weight
                vals.append({"state": label, "integrated_effect": float(integral),
                             "probability": float(probability),
                             "boundary_integral_error": float(error),
                             "semigroup_error_bound": float(rigorous_bound),
                             "quadrature_difference": float(quadrature_error),
                             "g2_A_eta_norm": float(g * g * np.linalg.norm(A @ eta))})
            pv, pp = vals[0]["probability"], vals[1]["probability"]
            n = math.ceil(1 / (lag * g**4))
            mean = n * (pp - pv)
            variance = n * (pv * (1 - pv) + pp * (1 - pp))
            rows.append({"g": g, "family": family, "lag": float(lag),
                         "lag_over_g4": float(lag / g**4), "states": vals,
                         "contrast_over_kappa2_weight_lag_g2": float(
                             (pp - pv) / (kappa * kappa * weight * lag * g * g)),
                         "independent_repetitions_per_arm": n,
                         "count_difference_mean": float(mean),
                         "count_difference_variance": float(variance),
                         "count_signal_to_standard_deviation": float(abs(mean) / math.sqrt(variance))})
    controlled = [r for r in rows if r["family"] == "controlled_lag_0.2_g5"]
    assert abs(controlled[-1]["contrast_over_kappa2_weight_lag_g2"] + 2) < 0.005
    return {"kappa": kappa, "first_total_rate": first_total_rate,
            "first_interval": interval, "first_survival_integral": weight,
            "rows": rows}


def main():
    start = time.perf_counter()
    result = {
        "scope": "Independent small analytic-machinery controls, not original-cube controls.",
        "limits": ["No verification of the imported 23 I + W + W* effect or boundary contrast.",
                   "No infinite-domain enclosure follows from a finite Fourier check.",
                   "No optimal lag power follows from this sufficient-bound control.",
                   "No microscopic marked-process convergence is numerically established."],
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__,
        "fourier_graph_rows": fourier_graph_rows(),
        "finite_bin_toy": finite_bin_rows(),
    }
    result["elapsed_seconds"] = time.perf_counter() - start
    result["all_assertions_passed"] = True
    text = json.dumps(result, indent=2, allow_nan=False) + "\n"
    Path(__file__).with_name("CONTROL_RESULTS.json").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
