#!/usr/bin/env python3
"""Independent structural controls; no author matching coefficients or data."""
import json
from datetime import datetime, timezone
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

SEED = 2026101207
rng = np.random.default_rng(SEED)
passed = 0
I2, I4 = np.eye(2), np.eye(4)
zero = np.zeros((2, 2))
sigma = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
G0 = np.block([[I2, zero], [zero, -I2]])
G = [np.block([[zero, s], [-s, zero]]) for s in sigma]
ALPHA = [G0 @ g for g in G]


def emit(name, condition, **details):
    global passed
    print(json.dumps({"check": name, "pass": bool(condition), **details}, sort_keys=True), flush=True)
    if not condition:
        raise AssertionError(name)
    passed += 1


def slash(E, p):
    return E * G0 - sum(x * g for x, g in zip(p, G))


def H(c, mass, p):
    return sum(c * x * a for x, a in zip(p, ALPHA)) + mass * G0


print(json.dumps({"utc": datetime.now(timezone.utc).isoformat(), "phase": "pre-author-bridge-and-coefficient-exposure", "seed": SEED,
                  "scope": "local projection, edge and leading radiation identities; not a full-action remainder bound"}), flush=True)
err = 0.0
for i, a in enumerate([G0] + G):
    for j, b in enumerate([G0] + G):
        target = 2 * (1 if i == 0 else -1) * I4 if i == j else np.zeros((4, 4))
        err = max(err, np.max(np.abs(a @ b + b @ a - target)))
emit("Minkowski-Clifford-matrices", err < 1e-14, max_error=float(err))

# Direct finite-matrix mass/clock projection. These coefficients are arbitrary controls.
zt, zs, bE, bB, C = 0.13, -0.09, 0.11, -0.07, 0.70
hg = (bB - bE) / 2
chi = zs - zt - hg


def local_projection(g, M, curve):
    Zt = 1 + g * zt
    cg = np.sqrt((1 + g * bB) / (1 + g * bE))
    mb = Zt * cg * M - g * C
    a = np.sqrt(1 - mb) if curve else 1.0
    vd = (a + g * zs) / Zt
    mass0 = (mb + g * C) / Zt
    vals = []
    for r in [0.001, 0.002]:
        ev = np.linalg.eigvalsh(H(vd, mass0 + r * r / (2 * Zt), np.array([0, 0, r])))
        e = np.mean(ev[2:]) / cg
        vals.append((e * e - M * M) / (r * r))
    B = (4 * vals[0] - vals[1]) / 3
    rest = np.linalg.eigvalsh(H(vd, mass0, np.zeros(3)))[-1] / cg
    return B, rest, mb


errors, rest_errors = [], []
for M in [0.0001, 0.01, 0.08]:
    for curve in [False, True]:
        h = 0.0001
        B0 = local_projection(0, M, curve)[0]
        B1, rest, mb = local_projection(h, M, curve)
        B2 = local_projection(2 * h, M, curve)[0]
        slope = 2 * (B1 - B0) / h - (B2 - B0) / (2 * h)
        target = C + 2 * np.sqrt(1 - M) * zs - 2 * zt - 2 * hg if curve else 2 * chi - M * (hg + zt)
        errors.append(abs(slope - target))
        rest_errors.append(abs(rest - M))
        print(json.dumps({"local_projection": "curve" if curve else "fixed", "M": M, "g": h, "bare_mass": mb,
                          "slope_from_matrix_eigenvalues": slope, "expected_slope": target}), flush=True)
emit("mass-and-clock-calibration-matrix-projection", max(errors) < 3e-7 and max(rest_errors) < 1e-13,
     max_slope_error=max(errors), max_rest_error=max(rest_errors), arbitrary_coefficients={"zt": zt, "zs": zs, "bE": bE, "bB": bB, "C": C})

f, h = rng.normal(size=(2, 200))
invariant = (zs + f - zt - f) - ((bB + h) - (bE + h)) / 2
emit("common-field-rescaling-invariant-local-combination", np.max(np.abs(invariant - chi)) < 1e-14,
     max_error=float(np.max(np.abs(invariant - chi))))

# Pure-gauge inverse variation factors vanish between on-shell spinors.
ward_error = 0.0
for _ in range(100):
    mass = rng.uniform(0.1, 1)
    p = rng.normal(size=3)
    vals, vectors = np.linalg.eigh(H(1, mass, p))
    E = vals[-1]
    u = vectors[:, -1]
    Dp = slash(E, p) - mass * I4
    q = rng.normal(size=3)
    Sq = np.linalg.inv(slash(0.07, q) - mass * I4)
    variation = Dp - Dp @ Sq @ Dp
    ward_error = max(ward_error, abs(u.conj() @ G0 @ variation @ u))
emit("on-shell-gauge-variation-factors", ward_error < 1e-12, cases=100, max_error=float(ward_error))

# Compare the isotropic electron+photon continuum edge against independent minimization.
edge_error = 0.0
for c in [0.95, 1.0, 1.02, 1.2]:
    M, cg = 0.2, 1.0
    for p in np.linspace(0.01, 3, 31):
        fun = lambda q: np.sqrt(M * M + c * c * q * q) + cg * abs(p - q)
        result = minimize_scalar(fun, bounds=(0, p), method="bounded", options={"xatol": 1e-13})
        numeric = min(result.fun, fun(0), fun(p))
        if c <= cg:
            expected = fun(p)
        else:
            star = M * cg / (c * np.sqrt(c * c - cg * cg))
            expected = fun(p) if p <= star else np.sqrt(M * M + c * c * star * star) + cg * (p - star)
        edge_error = max(edge_error, abs(numeric - expected))
emit("charged-continuum-edge-minimization", edge_error < 1e-11, cases=124, max_error=float(edge_error))


def emission(c, M, p, k, matrix=False):
    d = c * c - 1
    E = np.sqrt(M * M + c * c * p * p)
    cost = (E + d * k / 2) / (c * c * p)
    sint = np.sqrt(max(0.0, 1 - cost * cost))
    if matrix:
        pv = np.array([0.0, 0.0, p])
        kv = k * np.array([sint, 0.0, cost])
        N = slash(E, c * pv) + M * I4
        Np = slash(E - k, c * (pv - kv)) + M * I4
        pols = [np.array([cost, 0.0, -sint]), np.array([0.0, 1.0, 0.0])]
        amp = 0.0
        for eps in pols:
            vertex = c * sum(e * g for e, g in zip(eps, G))
            amp += (np.trace(Np @ vertex @ N @ vertex) / 2).real
    else:
        amp = 4 * c**4 * p * p * sint * sint + 2 * c * c * d * k * k
    return amp, amp / (16 * np.pi * E * c * c * p)


def integrated(c, M, p):
    d = c * c - 1
    E = np.sqrt(M * M + c * c * p * p)
    if c * c * p <= E:
        return 0.0, 0.0, 0.0
    K = 2 * (c * c * p - E) / d
    B0, B1, B2 = c * c * d * p * p - M * M, -E * d, d * (c * c + 1) / 4
    F = 1 / (4 * np.pi * E * c * c * p)
    return K, F * (B0 * K + B1 * K**2 / 2 + B2 * K**3 / 3), F * (B0 * K**2 / 2 + B1 * K**3 / 3 + B2 * K**4 / 4)


amplitude_error, rate_error, power_error = 0.0, 0.0, 0.0
kinematic_error = 0.0
for _ in range(40):
    c = rng.uniform(1.002, 1.25)
    M = rng.uniform(0.05, 0.3)
    pstar = M / (c * np.sqrt(c * c - 1))
    p = pstar * rng.uniform(1.02, 8)
    K, rate, power = integrated(c, M, p)
    for k in K * rng.uniform(0.01, 0.99, size=5):
        amp, _ = emission(c, M, p, k, matrix=True)
        expected, _ = emission(c, M, p, k)
        amplitude_error = max(amplitude_error, abs(amp - expected) / max(1, abs(expected)))
        E = np.sqrt(M * M + c * c * p * p)
        cost = (E + (c * c - 1) * k / 2) / (c * c * p)
        Ep = np.sqrt(M * M + c * c * (p * p + k * k - 2 * p * k * cost))
        kinematic_error = max(kinematic_error, abs(E - Ep - k))
    nr = quad(lambda k: emission(c, M, p, k, matrix=True)[1], 0, K, epsabs=1e-12, epsrel=1e-11)[0]
    npow = quad(lambda k: k * emission(c, M, p, k, matrix=True)[1], 0, K, epsabs=1e-12, epsrel=1e-11)[0]
    rate_error = max(rate_error, abs(nr - rate) / max(1e-10, abs(rate)))
    power_error = max(power_error, abs(npow - power) / max(1e-10, abs(power)))
emit("transverse-spinor-trace-and-emission-shell", amplitude_error < 1e-12 and kinematic_error < 1e-12,
     cases=200, max_relative_amplitude_error=amplitude_error, max_energy_residual=kinematic_error)
emit("matrix-phase-space-rate-and-power-integrals", max(rate_error, power_error) < 1e-10,
     cases=40, max_relative_rate_error=rate_error, max_relative_power_error=power_error)

asym_errors = []
for y in [0.05, 0.3, 0.8]:
    series = []
    for d in [0.001, 0.0001, 0.00001]:
        c, p, M = np.sqrt(1 + d), 1.0, np.sqrt(d * y)
        _, rate, power = integrated(c, M, p)
        alpha = 1 / (4 * np.pi)
        arate = alpha * d * p * (1 - y)**2 * (4 - y) / 6
        apower = alpha * d * p * p * (1 - y)**3 * (7 - 3 * y) / 24
        error = max(abs(rate / arate - 1), abs(power / apower - 1))
        series.append(error)
    asym_errors.append(series)
emit("small-cone-splitting-rate-limit", all(s[2] < s[1] < s[0] and s[2] < 0.001 for s in asym_errors),
     y_values=[0.05, 0.3, 0.8], relative_errors=asym_errors)

worst_r, worst_dr = 0.0, 0.0
for _ in range(5000):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    r, M, a = rng.uniform(0.05, 1), rng.uniform(0, 0.2), rng.uniform(0.8, 1.2)
    k = r * n
    W = np.sum(2 * np.sin(k / 2)**2)
    Wp = np.sum(n * np.sin(k))
    A4 = np.sum(n**4)
    beta = 0.25 - a * a * A4 / 3 - M * A4 / 12
    E2 = a * a * np.sum(np.sin(k)**2) + (M + W)**2
    derivative = a * a * np.sum(n * np.sin(2 * k)) + 2 * (M + W) * Wp
    rem = abs(E2 - M * M - (a * a + M) * r * r - beta * r**4)
    drem = abs(derivative - 2 * (a * a + M) * r - 4 * beta * r**3)
    bound = (2 * a * a / 45 + M / 360 + 1 / 24) * r**6
    dbound = (4 * a * a / 15 + M / 60 + 1 / 4) * r**5
    worst_r, worst_dr = max(worst_r, rem / bound), max(worst_dr, drem / dbound)
emit("uniform-directional-tree-remainder-bounds", max(worst_r, worst_dr) <= 1 + 1e-9,
     cases=5000, worst_value_bound_ratio=worst_r, worst_derivative_bound_ratio=worst_dr)

k = rng.uniform(-np.pi, np.pi, size=(10000, 3))
omega = 2 * np.linalg.norm(np.sin(k / 2), axis=1)
gap = omega - 2 * np.linalg.norm(k, axis=1) / np.pi
emit("full-torus-real-photon-momentum-bound", np.min(gap) >= -1e-14, cases=10000, minimum_gap=float(np.min(gap)))
print(f"TOTAL: PASS={passed} FAIL=0", flush=True)
