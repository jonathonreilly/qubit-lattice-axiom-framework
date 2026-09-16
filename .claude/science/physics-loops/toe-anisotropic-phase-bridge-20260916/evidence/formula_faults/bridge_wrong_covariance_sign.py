"""Deterministic finite-bridge challenges for the continuous-time derivation.

Gaussian quadrature treats one or two actual plaquette coordinates, with
the shared-link metric retained. Time quadrature is explicitly finite and
uses its own Dirichlet eigenvalue, not the continuum pi^2/T^2 constant.
No result here establishes a phase or a uniform time-quadrature error.
"""
AUDIT_TIMEOUT_SEC = 180
from hashlib import sha256
from pathlib import Path
import json
import math
import time

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.linalg import eigh


class BridgeQuadrature:
    def __init__(self, metric, g, duration, slices, order):
        self.metric = np.asarray(metric, dtype=float)
        self.q = len(metric)
        self.g = g
        self.duration = duration
        self.slices = slices
        self.fraction = np.linspace(0, 1, slices + 1)
        self.time_weights = np.full(slices + 1, duration / slices)
        self.time_weights[[0, -1]] *= 0.5
        s = self.fraction[1:-1] * duration
        covariance_time = np.minimum(s[:, None], s[None, :]) - s[:, None] * s[None, :] / duration
        covariance = g * g * np.kron(covariance_time, self.metric)
        dimension = covariance.shape[0]
        nodes, weights = hermgauss(order)
        indices = np.indices((order,) * dimension).reshape(dimension, -1).T
        self.weights = np.prod(weights[indices] / np.sqrt(np.pi), axis=1)
        standard = np.sqrt(2) * nodes[indices]
        interior = standard @ np.linalg.cholesky(covariance).T
        self.noise = np.zeros((len(indices), slices + 1, self.q))
        self.noise[:, 1:-1] = interior.reshape(-1, slices - 1, self.q)
        self.design = np.zeros((slices + 1, self.q, 2 * self.q))
        for p in range(self.q):
            self.design[:, p, p] = 1 - self.fraction
            self.design[:, p, self.q + p] = self.fraction
        self.source_gram = np.einsum("t,tpi,tpj->ij", self.time_weights, self.design, self.design)
        self.kappa = (duration / slices) ** 2 / (4 * np.sin(np.pi / (2 * slices)) ** 2)
        self.r = np.linalg.eigvalsh(self.metric)[-1] * self.kappa
        assert self.r < 1

    def evaluate(self, endpoints, derivatives=True):
        endpoints = np.asarray(endpoints, dtype=float)
        straight = np.einsum("tpi,i->tp", self.design, endpoints)
        field = straight[None, :, :] + self.noise
        action = np.einsum("t,ntp->n", self.time_weights, 1 - np.cos(field))
        density = self.weights * np.exp(-action / (self.g * self.g))
        normalization = density.sum()
        probability = density / normalization
        value = -self.g * self.g * np.log(normalization)
        if not derivatives:
            return float(value)
        gradient_action = np.einsum("t,ntp,tpi->ni", self.time_weights, np.sin(field), self.design)
        mean_gradient = probability @ gradient_action
        centered = gradient_action - mean_gradient
        covariance = centered.T @ (probability[:, None] * centered)
        mean_cos = np.einsum("n,ntp->tp", probability, np.cos(field))
        direct_hessian = np.einsum("t,tp,tpi,tpj->ij", self.time_weights, mean_cos, self.design, self.design)
        hessian = direct_hessian + covariance / (self.g * self.g)
        reference_hessian = np.einsum("t,tp,tpi,tpj->ij", self.time_weights, np.cos(straight), self.design, self.design)
        mean_noise = np.einsum("n,ntp->tp", probability, self.noise)
        noise_var = np.einsum("n,ntp->tp", probability, (self.noise - mean_noise) ** 2)
        return dict(value=float(value), gradient=mean_gradient, hessian=hessian,
                    reference_hessian=reference_hessian, covariance=covariance,
                    mean_noise=mean_noise, noise_var=noise_var)


def actual_cosine_checks():
    metric = np.array([[4., -1.], [-1., 4.]])
    # These are two adjacent oriented square cycles in a seven-link graph.
    c = np.array([[1, 1, -1, -1, 0, 0, 0], [0, 0, 1, 0, 1, -1, -1]])
    assert np.array_equal(c @ c.T, metric)
    rows = []
    largest_covariance_signal = 0.0
    endpoints_list = [[0.3, -0.5, 0.7, 0.2], [np.pi, 0, np.pi, 0], [-2.9, 2.7, 2.8, -2.6]]
    direction = np.array([0.7, -0.2, 0.4, 0.8])
    for g, duration in [(0.5, 0.1), (0.5, 0.35), (1.2, 0.35), (0.8, 0.7)]:
        quadrature = BridgeQuadrature(metric, g, duration, slices=3, order=16)
        high_order = BridgeQuadrature(metric, g, duration, slices=3, order=20)
        eigenvalues, vectors = eigh(quadrature.source_gram)
        inverse_root = (vectors / np.sqrt(eigenvalues)) @ vectors.T
        # Finite time quadrature has kappa != T^2/pi^2. The same proof uses
        # its exact discrete Dirichlet eigenvalue and the trapezoidal Q.
        r = quadrature.r
        delta = 2 * duration ** 2 + g * g * duration / (2 * (1 - r)) + r / (1 - r)
        for endpoints in endpoints_list:
            endpoints = np.array(endpoints)
            out = quadrature.evaluate(endpoints)
            refined = high_order.evaluate(endpoints)
            order_error = max(abs(out["value"] - refined["value"]),
                              float(np.max(abs(out["hessian"] - refined["hessian"]))))
            assert order_error < 3e-8
            normalized = inverse_root @ (out["hessian"] - out["reference_hessian"]) @ inverse_root
            correction_norm = float(np.max(abs(np.linalg.eigvalsh(normalized))))
            assert correction_norm <= delta + 2e-9
            assert np.max(abs(out["mean_noise"])) <= 2 * duration ** 2 + 2e-10
            assert np.max(out["noise_var"]) <= g * g * duration / (1 - r) + 2e-10
            h = 0.001
            plus = quadrature.evaluate(endpoints + h * direction, derivatives=False)
            minus = quadrature.evaluate(endpoints - h * direction, derivatives=False)
            finite_difference = (plus - 2 * out["value"] + minus) / (h * h)
            analytic = float(direction @ out["hessian"] @ direction)
            assert abs(finite_difference - analytic) < 2e-7
            signal = float(direction @ out["covariance"] @ direction) / (g * g)
            largest_covariance_signal = max(largest_covariance_signal, signal)
            rows.append(dict(g=g, duration=duration, endpoints=endpoints.tolist(),
                             time_slices=3, radial_dimension=4, gaussian_points=len(quadrature.weights),
                             order_comparison_error=order_error, r=r, delta_bound=delta,
                             measured_relative_hessian_norm=correction_norm,
                             hessian_direction=analytic, finite_difference=finite_difference,
                             mean_noise_max=float(np.max(abs(out["mean_noise"]))),
                             noise_variance_max=float(np.max(out["noise_var"])),
                             omitted_covariance_error=signal))
    assert largest_covariance_signal > 1e-4
    return rows


def nonconvex_endpoint_control():
    quadrature = BridgeQuadrature([[4.]], g=0.5, duration=0.2, slices=3, order=32)
    out = quadrature.evaluate([np.pi, np.pi])
    direction = np.ones(2)
    curvature = float(direction @ out["hessian"] @ direction)
    assert curvature < -0.15
    assert quadrature.r < 1
    return dict(common_endpoint_curvature=curvature, interior_convexity_r=quadrature.r,
                scope="convex interior bridge does not imply convex endpoint action")


def compact_kernel(g, duration, x, y, cutoff):
    n = np.arange(-cutoff, cutoff + 1)
    h = np.diag(2 * g * g * n * n + 1 / (g * g))
    h += np.diag(np.full(len(n) - 1, -1 / (2 * g * g)), 1)
    h += np.diag(np.full(len(n) - 1, -1 / (2 * g * g)), -1)
    values, vectors = eigh(h)
    kernel = (np.exp(1j * y * n) @ vectors * np.exp(-duration * values)) @ (vectors.T @ np.exp(-1j * x * n))
    assert abs(kernel.imag) < 1e-12
    return float(kernel.real)


def time_limit_check():
    g, duration, x, y = 0.4, 0.2, 0.3, 0.7
    k24 = compact_kernel(g, duration, x, y, 24)
    k36 = compact_kernel(g, duration, x, y, 36)
    assert abs(k24 - k36) < 1e-11
    free_lift = 2 * np.pi / np.sqrt(8 * np.pi * g * g * duration) * np.exp(-(y - x) ** 2 / (8 * g * g * duration))
    target = -g * g * np.log(k36 / free_lift)
    # Bounded cosine potential bounds the nonzero winding contribution by
    # exp(2T/g^2) times the corresponding free-kernel image ratios.
    # Bound the entire infinite image sum, including the omitted tail. For
    # |k|>=1, k^2>=|k| gives this geometric majorant for both signs.
    image_ratio = math.exp(-((2 * math.pi) ** 2 - 4 * math.pi * abs(y - x))
                           / (8 * g * g * duration))
    wrap_bound = math.exp(2 * duration / (g * g)) * 2 * image_ratio / (1 - image_ratio)
    assert wrap_bound < 1e-40
    rows = []
    for slices in [2, 3, 4, 5]:
        quadrature = BridgeQuadrature([[4.]], g, duration, slices=slices, order=18)
        value = quadrature.evaluate([x, y], derivatives=False)
        rows.append(dict(slices=slices, effective_action=value, spectral_target=float(target),
                         absolute_error=abs(value - target)))
    assert rows[-1]["absolute_error"] < rows[0]["absolute_error"] / 3
    assert rows[-1]["absolute_error"] < 0.001
    return dict(rows=rows, compact_cutoff_difference=abs(k24 - k36),
                nonzero_winding_relative_bound=wrap_bound,
                scope="one-plaquette time-quadrature challenge only")


def main():
    start = time.monotonic()
    result = {"source_sha256": sha256(Path(__file__).read_bytes()).hexdigest()}
    result["cosine_bridge"] = actual_cosine_checks()
    result["endpoint_nonconvex_control"] = nonconvex_endpoint_control()
    result["time_limit"] = time_limit_check()
    result["elapsed_seconds"] = time.monotonic() - start
    result["status"] = "PASS"
    result["scope"] = "deterministic finite bridge and one-plaquette kernel checks; no phase proof"
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
