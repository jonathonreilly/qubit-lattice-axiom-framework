"""Independent finite oscillator checks; no parent or author runner is imported.

The polynomial state moments are exact in the finite matrices used below,
because all states stay clear of the truncation boundary. The cosine
expectations use independent Hermite-Gauss quadrature, with a second order
comparison; floating agreement is not an interval enclosure. The spatial
matrix is explicitly auxiliary, not a simulated cubic record generator.
"""
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np
from numpy.polynomial.hermite import hermgauss, hermval
from numpy.polynomial.legendre import leggauss


def annihilation(n):
    return np.diag(np.sqrt(np.arange(1, n, dtype=float)), 1).astype(complex)


def pure(c):
    c = np.asarray(c, dtype=complex)
    c = c / np.linalg.norm(c)
    return np.outer(c, c.conj())


def expectation(rho, op):
    return np.trace(rho @ op)


def characteristic(rho, g, nodes_count):
    nodes, weights = hermgauss(nodes_count)
    # Harmonic Hermite functions with their shared Gaussian removed.
    polys = np.stack([
        hermval(nodes, [0] * n + [1]) / math.sqrt(2**n * math.factorial(n))
        for n in range(rho.shape[0])
    ])
    density = np.einsum("ni,nm,mi->i", polys, rho, polys).real
    norm = float(np.dot(weights, density) / math.sqrt(math.pi))
    value = float(np.dot(weights, density * np.cos(g * math.sqrt(2) * nodes))
                  / math.sqrt(math.pi))
    return norm, value


def one_mode_controls():
    dim = 8
    a = annihilation(dim)
    q = a + a.conj().T
    states = {}
    for n in [0, 1, 2]:
        c = np.zeros(dim); c[n] = 1
        states[f"number_{n}"] = pure(c)
    states["equal_vacuum_two_mixture"] = (states["number_0"] + states["number_2"]) / 2
    for name, entries in [
        ("vacuum_one_superposition", {0: 1, 1: 1}),
        ("zero_calibrated_mean", {0: math.sqrt(2), 2: -1}),
        ("same_occupation_bright", {0: math.sqrt(2), 2: 1}),
        ("negative_calibrated_mean", {0: 2, 2: -1}),
    ]:
        c = np.zeros(dim)
        for n, value in entries.items(): c[n] = value
        states[name] = pure(c)
    rows = []
    max_norm_error = 0.0
    max_quadrature_difference = 0.0
    for name, rho in states.items():
        occupation = float(expectation(rho, a.conj().T @ a).real)
        pair = expectation(rho, a @ a)
        direct = float(expectation(rho, q @ q).real - 1)
        formula = 2 * occupation + 2 * pair.real
        assert abs(direct - formula) < 2e-14
        factorial2 = float(expectation(rho, a.conj().T @ a.conj().T @ a @ a).real)
        scales = []
        for g in [.4, .2, .1, .05, .025]:
            norm, cosine = characteristic(rho, g, 48)
            _, cosine_again = characteristic(rho, g, 80)
            max_norm_error = max(max_norm_error, abs(norm - 1))
            max_quadrature_difference = max(max_quadrature_difference, abs(cosine - cosine_again))
            effect = 23 + 2 * cosine
            vacuum_effect = 23 + 2 * math.exp(-g*g/2)
            response = (vacuum_effect - effect) / (g*g)
            assert 21 - 1e-12 <= effect <= 25 + 1e-12
            scales.append({"g": g, "raw_boundary_effect": effect,
                           "vacuum_subtracted_scaled_mean": response,
                           "difference_from_leading": response - direct,
                           "difference_over_g2": (response - direct) / (g*g)})
        assert abs(scales[-1]["difference_from_leading"]) < .004
        rows.append({"state": name, "ideal_matched_single_intensity": occupation,
                     "ideal_same_mode_factorial_pair": factorial2,
                     "anomalous_pair_real": float(pair.real),
                     "leading_record_deficit": direct, "scales": scales})
    by_name = {row["state"]: row for row in rows}
    assert abs(by_name["zero_calibrated_mean"]["leading_record_deficit"]) < 1e-14
    assert by_name["negative_calibrated_mean"]["leading_record_deficit"] < 0
    assert abs(by_name["zero_calibrated_mean"]["ideal_matched_single_intensity"] - 2/3) < 1e-14
    assert abs(by_name["same_occupation_bright"]["ideal_matched_single_intensity"] - 2/3) < 1e-14
    assert abs(by_name["number_1"]["leading_record_deficit"] -
               by_name["equal_vacuum_two_mixture"]["leading_record_deficit"]) < 1e-14
    assert by_name["number_1"]["ideal_same_mode_factorial_pair"] == 0
    assert abs(by_name["equal_vacuum_two_mixture"]["ideal_same_mode_factorial_pair"] - 1) < 1e-14
    assert max_norm_error < 1e-13 and max_quadrature_difference < 2e-14
    return {"rows": rows, "quadrature_orders": [48, 80],
            "max_normalization_error": max_norm_error,
            "max_cosine_quadrature_difference": max_quadrature_difference}


def averaged_controls():
    dim = 5
    eye = np.eye(dim)
    aa = [np.kron(annihilation(dim), eye), np.kron(eye, annihilation(dim))]
    # C.T C = diag(2, 6); two positive modes and three tested components.
    curl = np.array([[1., 1.], [-1., 1.], [0., 2.]])
    omega = np.sqrt(np.array([2., 6.]))
    coupling = curl / np.sqrt(2 * omega)[None, :]
    assert np.allclose(coupling.T @ coupling, np.diag(omega/2), atol=1e-15)
    states = {}
    for name, entries in [
        ("number_one_wavepacket", {(1, 0): 1, (0, 1): 1j}),
        ("same_mode_anomalous", {(0, 0): 2, (2, 0): -1}),
        ("cross_mode_anomalous", {(0, 0): 1, (1, 1): 1}),
    ]:
        vec = np.zeros(dim*dim, complex)
        for (n, m), value in entries.items(): vec[n*dim+m] = value
        states[name] = pure(vec)
    rows = []
    nodes, weights = leggauss(160)
    for name, rho in states.items():
        number = np.array([expectation(rho, a.conj().T @ a).real for a in aa])
        pairs = np.array([[expectation(rho, a @ b) for b in aa] for a in aa])
        energy = float(omega @ number)
        spatial_checks = []
        for t in [0., .3, 1., 2.]:
            excess = []
            intensities = []
            for d in coupling:
                positive = sum(d[k] * np.exp(-1j*omega[k]*t) * aa[k] for k in range(2))
                quadrature = positive + positive.conj().T
                vacuum = float(d @ d)
                excess.append(float(expectation(rho, quadrature @ quadrature).real-vacuum))
                intensities.append(float(expectation(rho, positive.conj().T @ positive).real))
            diagonal_anomaly = float(np.real(np.sum(omega * np.diag(pairs) * np.exp(-2j*omega*t))))
            assert abs(sum(excess) - energy - diagonal_anomaly) < 2e-14
            assert abs(2*sum(intensities)-energy) < 2e-14
            spatial_checks.append({"time": t, "local_quadrature_excess": excess,
                                   "spatial_sum": sum(excess), "energy_weighted_occupation": energy,
                                   "surviving_anomalous_term": diagonal_anomaly})
        temporal_checks = []
        d = coupling[0]
        nu = omega[:, None] + omega[None, :]
        coefficients = d[:, None]*d[None, :]*pairs
        for duration in [.5, 5., 30.]:
            times = duration*(nodes+1)/2
            integrand = np.array([2*np.real(np.sum(coefficients*np.exp(-1j*nu*t))) for t in times])
            quadrature_average = float(weights @ integrand / 2)
            filt = -np.expm1(-1j*nu*duration)/(1j*nu*duration)
            exact_average = float(2*np.real(np.sum(coefficients*filt)))
            bound = float(2*np.sum(np.abs(coefficients)*np.minimum(1,2/(nu*duration))))
            assert abs(quadrature_average-exact_average) < 3e-13
            assert abs(exact_average) <= bound + 1e-14
            lam = 1.3
            weighted_filter = (lam/(lam+1j*nu)) * (-np.expm1(-(lam+1j*nu)*duration))/(-math.expm1(-lam*duration))
            weighted = float(2*np.real(np.sum(coefficients*weighted_filter)))
            infinite_weighted = float(2*np.real(np.sum(coefficients*lam/(lam+1j*nu))))
            temporal_checks.append({"duration":duration,
                                    "unweighted_excess_over_twice_intensity":exact_average,
                                    "quadrature_value":quadrature_average,
                                    "oscillatory_bound":bound,
                                    "survival_weighted_excess_over_twice_intensity":weighted,
                                    "infinite_survival_weighted_limit":infinite_weighted})
        rows.append({"state":name,"spatial_checks":spatial_checks,"temporal_checks":temporal_checks})
    return {"scope":"Auxiliary two-mode geometry, not the cubic record process.",
            "curl_matrix":curl.tolist(),"frequencies":omega.tolist(),"survival_rate":1.3,"rows":rows}


def benchmark_methods_arithmetic():
    # Published Fig. 3 parameters; no fitting and no record-model identification.
    n1, n2, bin_width, elapsed, fraction = 5780., 5990., 1e-9, 11450., .34
    poisson_bin = n1*n2*bin_width*elapsed
    raw_normalized_if_corrected_zero = 1-fraction*fraction
    return {"scope":"Arithmetic illustration of Brouri et al.'s published normalization, not a fitted datum.",
            "count_rates": [n1,n2],"bin_seconds":bin_width,"integration_seconds":elapsed,
            "signal_fraction":fraction,"poisson_reference_counts_per_bin":poisson_bin,
            "raw_normalized_coincidence_if_corrected_g2_zero":raw_normalized_if_corrected_zero,
            "implied_raw_counts_if_corrected_g2_zero":poisson_bin*raw_normalized_if_corrected_zero}


if __name__ == "__main__":
    start = time.monotonic()
    result = {"scope": __doc__, "one_mode":one_mode_controls(),
              "spatial_temporal":averaged_controls(),
              "benchmark_methods":benchmark_methods_arithmetic(),
              "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "numpy":np.__version__,"all_assertions_passed":True,
              "elapsed_seconds":time.monotonic()-start}
    data=json.dumps(result,indent=2,allow_nan=False)+"\n"
    (Path(__file__).resolve().parent/"CONTROL_RESULTS.json").write_text(data)
    print(data,end="")
