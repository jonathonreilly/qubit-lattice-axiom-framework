#!/usr/bin/env python3
"""Bounded numerical verification for the source note

    docs/D2_SIGN_BOUNDARY_BISECTION_BETWEEN_LANDMARKS_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d2_sign_boundary_bisection_2026_06_12.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from typing import Callable

import numpy as np
from numpy.polynomial.legendre import leggauss


PASS_COUNT = 0
FAIL_COUNT = 0


def check(condition: bool, name: str, note: str = "") -> None:
    """Runner check contract: record PASS/FAIL and print the gated claim."""
    global PASS_COUNT, FAIL_COUNT
    ok = bool(condition)
    if ok:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    suffix = f" | {note}" if note else ""
    print(f"{'PASS' if ok else 'FAIL'}: {name}{suffix}")


def finish() -> None:
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        sys.exit(1)


def gl_rule(n: int, a: float, b: float) -> tuple[np.ndarray, np.ndarray]:
    x, w = leggauss(n)
    nodes = 0.5 * (b - a) * x + 0.5 * (a + b)
    weights = 0.5 * (b - a) * w / (b - a)
    return nodes, weights


def fermi_grand_terms(evals: np.ndarray, mu: float, temp: float) -> np.ndarray:
    return -temp * np.logaddexp(0.0, (mu - evals) / temp)


@dataclass(frozen=True)
class Spectrum2D:
    evals: np.ndarray
    weights: np.ndarray
    bands: int
    label: str

    def omega(self, mu: float, temp: float) -> float:
        terms = fermi_grand_terms(self.evals, mu, temp)
        per_k = np.sum(terms, axis=1) / float(self.bands)
        return float(np.dot(self.weights, per_k))


def staggered_harper_matrix(q: int, m: float, bfield: float, theta_x: float, ky: float) -> np.ndarray:
    """Dense 2q x 2q Landau-gauge Harper matrix for checkerboard staggering.

    Basis: x=0..q-1, sector 0 is ky, sector 1 is ky+pi.  The mass
    m*(-1)^(x+y) couples the two ky sectors with amplitude m*(-1)^x.
    """
    n = 2 * q
    h = np.zeros((n, n), dtype=np.complex128)
    phase_x = np.exp(1j * theta_x)

    xvals = np.arange(q, dtype=float)
    diag0 = -2.0 * np.cos(ky + bfield * xvals)
    diag1 = -diag0
    parity = np.where(np.arange(q) % 2 == 0, 1.0, -1.0)

    for sector, diag in ((0, diag0), (1, diag1)):
        off = sector * q
        h[off + np.arange(q), off + np.arange(q)] = diag
        for x in range(q):
            i = off + x
            xp = (x + 1) % q
            j = off + xp
            hop_phase = phase_x if xp == 0 else 1.0 + 0.0j
            amp = -hop_phase
            h[j, i] += amp
            h[i, j] += np.conjugate(amp)

    for x in range(q):
        amp = m * parity[x]
        h[x, q + x] += amp
        h[q + x, x] += amp

    return h


def finite_field_spectrum(q: int, m: float, order: int) -> Spectrum2D:
    theta_nodes, theta_w = gl_rule(order, 0.0, 2.0 * math.pi)
    ky_nodes, ky_w = gl_rule(order, 0.0, math.pi)
    bfield = 2.0 * math.pi / float(q)
    bands = 2 * q
    evals = np.empty((order * order, bands), dtype=np.float64)
    weights = np.empty(order * order, dtype=np.float64)

    row = 0
    for i, theta_x in enumerate(theta_nodes):
        wx = theta_w[i]
        for j, ky in enumerate(ky_nodes):
            h = staggered_harper_matrix(q, m, bfield, theta_x, ky)
            evals[row, :] = np.linalg.eigvalsh(h)
            weights[row] = wx * ky_w[j]
            row += 1

    return Spectrum2D(evals=evals, weights=weights, bands=bands, label=f"B q={q} n={order}")


def zero_field_spectrum(m: float, order: int) -> Spectrum2D:
    kx_nodes, kx_w = gl_rule(order, 0.0, 2.0 * math.pi)
    ky_nodes, ky_w = gl_rule(order, 0.0, 2.0 * math.pi)
    evals = np.empty((order * order, 2), dtype=np.float64)
    weights = np.empty(order * order, dtype=np.float64)

    row = 0
    for i, kx in enumerate(kx_nodes):
        cx = math.cos(kx)
        wx = kx_w[i]
        for j, ky in enumerate(ky_nodes):
            eps = -2.0 * (cx + math.cos(ky))
            e = math.sqrt(m * m + eps * eps)
            evals[row, 0] = -e
            evals[row, 1] = e
            weights[row] = wx * ky_w[j]
            row += 1

    return Spectrum2D(evals=evals, weights=weights, bands=2, label=f"B=0 n={order}")


@dataclass
class ChiCalculator:
    q: int
    m: float
    field: Spectrum2D
    zero: Spectrum2D

    @property
    def bfield(self) -> float:
        return 2.0 * math.pi / float(self.q)

    def chi(self, mu: float, temp: float) -> float:
        omega_b = self.field.omega(mu, temp)
        omega_0 = self.zero.omega(mu, temp)
        return 2.0 * (omega_b - omega_0) / (self.bfield * self.bfield)


def sign_name(value: float) -> str:
    if value < 0.0:
        return "< 0"
    if value > 0.0:
        return "> 0"
    return "= 0"


def gate_endpoint_sign(label: str, value: float) -> None:
    if value < 0.0:
        check(value < 0.0, f"{label}: chi {sign_name(value)}", f"chi={value:.12e}")
    elif value > 0.0:
        check(value > 0.0, f"{label}: chi {sign_name(value)}", f"chi={value:.12e}")
    else:
        check(value == 0.0, f"{label}: chi {sign_name(value)}", f"chi={value:.12e}")


def find_sign_bracket(
    chi_fn: Callable[[float], float],
    low: float,
    high: float,
    steps: int,
    label: str,
) -> tuple[float, float, float, float]:
    xs = np.linspace(low, high, steps + 1)
    vals = [chi_fn(float(x)) for x in xs]
    for i in range(steps):
        a, b = float(xs[i]), float(xs[i + 1])
        fa, fb = vals[i], vals[i + 1]
        if fa == 0.0:
            eps = (high - low) / float(steps)
            return max(low, a - eps), min(high, a + eps), chi_fn(max(low, a - eps)), chi_fn(min(high, a + eps))
        if fa * fb < 0.0:
            check(fa * fb < 0.0, f"{label}: scanned bracket has endpoint sign change", f"[{a:.6f}, {b:.6f}] fa={fa:.3e} fb={fb:.3e}")
            return a, b, fa, fb
    check(False, f"{label}: scanned bracket has endpoint sign change", f"scan=[{low:.6f}, {high:.6f}]")
    return float(xs[0]), float(xs[-1]), vals[0], vals[-1]


def bisect_root(
    chi_fn: Callable[[float], float],
    low: float,
    high: float,
    f_low: float,
    f_high: float,
    tol: float,
    label: str,
) -> tuple[float, float, float]:
    check(f_low * f_high <= 0.0, f"{label}: initial bisection bracket retains sign change", f"[{low:.6f}, {high:.6f}]")
    last_width = high - low
    iteration = 0
    while (high - low) > 2.0 * tol:
        iteration += 1
        mid = 0.5 * (low + high)
        f_mid = chi_fn(mid)
        check(
            f_low * f_high <= 0.0,
            f"{label}: bisection iter {iteration:02d} pre-update bracket retains sign change",
            f"lo={low:.6f} hi={high:.6f}",
        )
        if f_mid == 0.0:
            low = high = mid
            f_low = f_high = f_mid
        elif f_low * f_mid <= 0.0:
            high = mid
            f_high = f_mid
        else:
            low = mid
            f_low = f_mid
        width = high - low
        check(
            width <= last_width + 1e-15,
            f"{label}: bisection iter {iteration:02d} bracket width does not increase",
            f"width={width:.12e}",
        )
        check(
            f_low * f_high <= 0.0,
            f"{label}: bisection iter {iteration:02d} post-update bracket retains sign change",
            f"lo={low:.6f} hi={high:.6f}",
        )
        last_width = width

    root = 0.5 * (low + high)
    f_root = chi_fn(root)
    check(high - low <= 2.0 * tol, f"{label}: final bisection width locates mu* to 1e-3", f"width={high - low:.12e}")
    return root, f_root, high - low


def band_max(m: float) -> float:
    return math.sqrt(m * m + 16.0)


def van_hove_energy(m: float) -> float:
    return abs(m)


def main() -> None:
    primary_q = 24
    probe_q = 32
    coarse_order = 96
    fine_order = 192
    tol = 1e-3

    for q in (primary_q, probe_q):
        bfield = 2.0 * math.pi / float(q)
        probe_h = staggered_harper_matrix(q, 0.2, bfield, 0.37, 0.41)
        check(q % 2 == 0, f"finite-lattice size probe: q={q} is even")
        check(abs(np.exp(1j * bfield * q) - 1.0) < 1e-12, f"finite-lattice wraparound probe: q={q} magnetic phase exp(i B_q q)=1")
        check(np.allclose(probe_h, probe_h.conjugate().T, atol=1e-12), f"finite-lattice wraparound probe: q={q} Harper matrix is Hermitian")
        check(np.allclose(probe_h[0, q - 1], -np.exp(1j * 0.37), atol=1e-12), f"finite-lattice wraparound probe: q={q} x-boundary Bloch phase is present")
        check(np.allclose(probe_h[q, 2 * q - 1], -np.exp(1j * 0.37), atol=1e-12), f"finite-lattice wraparound probe: q={q} second sector x-boundary Bloch phase is present")

    masses = (0.2, 0.5)
    field_24_96: dict[float, Spectrum2D] = {}
    field_24_192: dict[float, Spectrum2D] = {}
    field_32_96: dict[float, Spectrum2D] = {}
    zero_96: dict[float, Spectrum2D] = {}
    zero_192: dict[float, Spectrum2D] = {}

    for m in masses:
        print(f"PRECOMPUTE m={m:.3f}: q=24 n=96/n=192 and q=32 n=96")
        zero_96[m] = zero_field_spectrum(m, coarse_order)
        zero_192[m] = zero_field_spectrum(m, fine_order)
        field_24_96[m] = finite_field_spectrum(primary_q, m, coarse_order)
        field_24_192[m] = finite_field_spectrum(primary_q, m, fine_order)
        field_32_96[m] = finite_field_spectrum(probe_q, m, coarse_order)

    calc_24_96 = {m: ChiCalculator(primary_q, m, field_24_96[m], zero_96[m]) for m in masses}
    calc_24_192 = {m: ChiCalculator(primary_q, m, field_24_192[m], zero_192[m]) for m in masses}
    calc_32_96 = {m: ChiCalculator(probe_q, m, field_32_96[m], zero_96[m]) for m in masses}

    bracket_mu = (1.5, 2.0)
    bracket_m = 0.2
    bracket_t = 0.2
    f15 = calc_24_192[bracket_m].chi(bracket_mu[0], bracket_t)
    f20 = calc_24_192[bracket_m].chi(bracket_mu[1], bracket_t)
    gate_endpoint_sign("V1a endpoint mu=1.5 at (m=0.2,T=0.2)", f15)
    gate_endpoint_sign("V1a endpoint mu=2.0 at (m=0.2,T=0.2)", f20)
    check(f15 * f20 < 0.0, "V1a bracket [1.5,2.0] at (m=0.2,T=0.2) has a chi sign change", f"chi(1.5)={f15:.12e} chi(2.0)={f20:.12e}")

    for mu in bracket_mu:
        c96 = calc_24_96[bracket_m].chi(mu, bracket_t)
        c192 = calc_24_192[bracket_m].chi(mu, bracket_t)
        check(abs(c192 - c96) <= 1e-8, f"Gauss-Legendre doubling gate: q=24 chi(mu={mu:.1f},m=0.2,T=0.2) n=96 to n=192 differs by <=1e-8", f"diff={abs(c192 - c96):.12e}")
        c32 = calc_32_96[bracket_m].chi(mu, bracket_t)
        rel32 = abs(c32 - c192) / max(abs(c32), abs(c192), 1e-14)
        check(rel32 <= 0.05, f"q=32 size probe: chi(mu={mu:.1f},m=0.2,T=0.2) agrees with q=24 within 5%", f"q24={c192:.12e} q32={c32:.12e} rel={rel32:.6e}")

    instances = [(0.2, 0.2), (0.5, 0.2), (0.2, 0.4)]
    roots: dict[tuple[float, float], float] = {}
    roots_probe: dict[tuple[float, float], float] = {}
    chi_at_roots: dict[tuple[float, float], float] = {}

    for m, temp in instances:
        label = f"V1b q=24 (m={m:.1f},T={temp:.1f})"
        chi_fn = lambda mu, mm=m, tt=temp: calc_24_192[mm].chi(mu, tt)
        if (m, temp) == (0.2, 0.2):
            low, high, flo, fhi = bracket_mu[0], bracket_mu[1], f15, f20
        else:
            low, high, flo, fhi = find_sign_bracket(chi_fn, 0.25, band_max(m) - 1e-6, 48, label)
        root, froot, width = bisect_root(chi_fn, low, high, flo, fhi, tol, label)
        roots[(m, temp)] = root
        chi_at_roots[(m, temp)] = froot
        print(f"mu*(m={m:.1f}, T={temp:.1f}, q=24) = {root:.6f}  chi={froot:.12e}  bracket_width={width:.12e}")

        c96 = calc_24_96[m].chi(root, temp)
        c192 = calc_24_192[m].chi(root, temp)
        check(abs(c192 - c96) <= 1e-8, f"Gauss-Legendre doubling gate: q=24 chi(mu*=m{m:.1f}T{temp:.1f}) n=96 to n=192 differs by <=1e-8", f"diff={abs(c192 - c96):.12e}")

        probe_label = f"q=32 size probe (m={m:.1f},T={temp:.1f})"
        probe_chi = lambda mu, mm=m, tt=temp: calc_32_96[mm].chi(mu, tt)
        plow, phigh, pflo, pfhi = find_sign_bracket(probe_chi, max(0.1, root - 0.5), min(band_max(m) - 1e-6, root + 0.5), 20, probe_label)
        proot, pfroot, _ = bisect_root(probe_chi, plow, phigh, pflo, pfhi, tol, probe_label)
        roots_probe[(m, temp)] = proot
        rel_mu = abs(proot - root) / max(1.0, abs(root))
        check(rel_mu <= 0.05, f"q=32 size probe: mu* agrees with q=24 within 5% for (m={m:.1f},T={temp:.1f})", f"q24={root:.6f} q32={proot:.6f} rel={rel_mu:.6e}")

    mu_m02_t02 = roots[(0.2, 0.2)]
    mu_m05_t02 = roots[(0.5, 0.2)]
    mu_m02_t04 = roots[(0.2, 0.4)]

    check(mu_m05_t02 > mu_m02_t02,
          "V1c fixed-direction gate: mu* increases with m at T=0.2 "
          "(mu*(m=0.5) > mu*(m=0.2))",
          f"{mu_m05_t02:.6f} > {mu_m02_t02:.6f}")

    check(mu_m02_t04 > mu_m02_t02,
          "V1c fixed-direction gate: mu* increases with T at m=0.2 "
          "(mu*(T=0.4) > mu*(T=0.2))",
          f"{mu_m02_t04:.6f} > {mu_m02_t02:.6f}")

    closer_to_vh = []
    closer_to_edge = []
    between_landmarks = []
    print("V1d zero-field analytic landmarks:")
    for m, temp in instances:
        root = roots[(m, temp)]
        e_edge = band_max(m)
        e_vh = van_hove_energy(m)
        d_edge = abs(root - e_edge)
        d_vh = abs(root - e_vh)
        edge_formula = math.sqrt(m * m + 16.0)
        check(abs(e_edge - edge_formula) < 1e-14, f"V1d analytic upper band edge equals sqrt(m^2+16) for m={m:.1f}", f"Emax={e_edge:.12f}")
        check(abs(e_vh - abs(m)) < 1e-14, f"V1d analytic staggered-spectrum van Hove energy equals |m| for m={m:.1f}", f"E_vH={e_vh:.12f}")
        print(
            f"  (m={m:.1f},T={temp:.1f}) mu*={root:.6f}, "
            f"E_vH={e_vh:.6f}, E_upper={e_edge:.6f}, "
            f"|mu*-E_vH|={d_vh:.6f}, |mu*-E_upper|={d_edge:.6f}"
        )
        closer_to_vh.append(d_vh < d_edge)
        closer_to_edge.append(d_edge < d_vh)
        between_landmarks.append(e_vh < root < e_edge)

    # honest anchor: mu* lies strictly BETWEEN the van Hove energy and the upper
    # band edge at every sampled instance, near neither (distance-comparison
    # framings are vacuous here); gate the between-ness, report the distances.
    check(
        all(between for between in between_landmarks),
        "V1d anchor: every sampled mu* lies strictly between the analytic van Hove "
        "energy |m| and the upper band edge sqrt(m^2+16), anchored to NEITHER at "
        "the sampled instances (distances printed; the landmark question stays open)",
    )

    print("SCOPE: sampled instances only; bisection-bracketed finite-field boundary; no continuum claim")
    finish()


if __name__ == "__main__":
    main()
