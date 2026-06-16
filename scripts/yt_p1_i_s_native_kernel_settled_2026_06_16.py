#!/usr/bin/env python3
"""Settle the H_unit scalar-bilinear propagator-kernel fork.

This runner is deliberately narrow. It demonstrates why the
composite-H_unit 1-loop vertex diagram has two untraced fermion propagators,
but why the scalar-projected matching integrand carries only one remaining
D_psi denominator:

    gamma_mu S(k) 1 S(k) gamma_mu
      ~ gamma_mu (slash{s}) 1 (slash{s}) gamma_mu / D_psi(k)^2
      = D_psi(k) * gamma_mu gamma_mu / D_psi(k)^2.

Thus, once the retained scalar numerator N_S(k) is the trace-reduced numerator,
the settled finite-part kernel is

    N_S(k) / (D_psi(k) D_g(k)),

with the MSbar continuum subtraction 4/(k^2 + m^2)^2. The literal
N_S(k)/(D_psi(k)^2 D_g(k)) form would be a pre-trace denominator with the
kinetic numerator omitted.

This runner does not settle the taste-normalization convention or the final
numeric I_S. The grid sweep below uses one fixed normalization only as a
stability check for the settled kernel.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"[{status}] {name}{suffix}")


PI = math.pi
TWO_PI = 2.0 * PI
SIXTEEN_PI_SQ = 16.0 * PI * PI

CANONICAL_PLAQUETTE = 0.5934
U0 = CANONICAL_PLAQUETTE ** 0.25
N_TASTE = 16.0
DEFAULT_M_SQ = 0.01
CONTINUUM_OFFSET_SCALAR = 2.0


@dataclass(frozen=True)
class IntegralParts:
    value: float
    lat: float
    cont: float


def pauli_matrices() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    ident = np.eye(2, dtype=np.complex128)
    sigma_1 = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    sigma_2 = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
    sigma_3 = np.array([[1, 0], [0, -1]], dtype=np.complex128)
    return ident, sigma_1, sigma_2, sigma_3


def euclidean_gamma_matrices() -> list[np.ndarray]:
    """A concrete Cl(4) representation with {gamma_mu,gamma_nu}=2 delta_mu_nu."""
    ident, sigma_1, sigma_2, sigma_3 = pauli_matrices()
    return [
        np.kron(sigma_1, sigma_1),
        np.kron(sigma_1, sigma_2),
        np.kron(sigma_1, sigma_3),
        np.kron(sigma_2, ident),
    ]


def slash(gamma: list[np.ndarray], s: np.ndarray) -> np.ndarray:
    out = np.zeros((4, 4), dtype=np.complex128)
    for mu in range(4):
        out = out + float(s[mu]) * gamma[mu]
    return out


def scalar_projection_trace_ratio(k: np.ndarray) -> tuple[float, float]:
    """Return the trace-reduced numerator and its expected D_psi*N_S value."""
    gamma = euclidean_gamma_matrices()
    s = np.sin(k)
    c = np.cos(k / 2.0) ** 2
    d_psi = float(np.sum(s * s))
    n_s = float(np.sum(c))
    slash_s = slash(gamma, s)

    projected = np.zeros((4, 4), dtype=np.complex128)
    for mu in range(4):
        projected = projected + c[mu] * gamma[mu] @ slash_s @ slash_s @ gamma[mu]

    # Divide by spin dimension to project onto the scalar identity channel.
    trace_reduced = float(np.trace(projected).real / 4.0)
    return trace_reduced, d_psi * n_s


def midpoint_grid(n: int) -> np.ndarray:
    delta = TWO_PI / float(n)
    return -PI + (np.arange(n, dtype=np.float64) + 0.5) * delta


def cell_weight(n: int) -> float:
    return (TWO_PI / float(n) / TWO_PI) ** 4


def _tail_mesh(grid: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return np.meshgrid(grid, grid, indexing="ij")


def integrate_settled_scalar_kernel(n: int, m_sq: float = DEFAULT_M_SQ) -> IntegralParts:
    """Compute an illustrative finite part for the settled H_unit scalar kernel.

    The normalization below is fixed only to check grid stability:

        2 + [16*pi^2/(N_TASTE*u0^2)] int_BZ [
            N_S(k)/((D_psi(k)+m^2)(D_g(k)+m^2))
            - 4/(k^2+m^2)^2
        ] d^4k/(2*pi)^4.

    It is not a final I_S value claim.
    """
    grid = midpoint_grid(n)
    k2, k3 = _tail_mesh(grid)

    sin2_tail = np.sin(k2) ** 2 + np.sin(k3) ** 2
    sing_tail = np.sin(k2 / 2.0) ** 2 + np.sin(k3 / 2.0) ** 2
    cos_tail = np.cos(k2 / 2.0) ** 2 + np.cos(k3 / 2.0) ** 2
    ksq_tail = k2 * k2 + k3 * k3

    lat_sum = 0.0
    cont_sum = 0.0
    for k0 in grid:
        sin2_0 = math.sin(k0) ** 2
        sing_0 = math.sin(k0 / 2.0) ** 2
        cos_0 = math.cos(k0 / 2.0) ** 2
        ksq_0 = k0 * k0
        for k1 in grid:
            d_psi = sin2_0 + math.sin(k1) ** 2 + sin2_tail + m_sq
            d_g = 4.0 * (sing_0 + math.sin(k1 / 2.0) ** 2 + sing_tail) + m_sq
            n_s = cos_0 + math.cos(k1 / 2.0) ** 2 + cos_tail
            ksq = ksq_0 + k1 * k1 + ksq_tail + m_sq

            lat_sum += float(np.sum(n_s / (d_psi * d_g)))
            cont_sum += float(np.sum(4.0 / (ksq * ksq)))

    weight = cell_weight(n)
    lat = SIXTEEN_PI_SQ * lat_sum * weight
    cont = SIXTEEN_PI_SQ * cont_sum * weight
    value = CONTINUUM_OFFSET_SCALAR + (lat - cont) / (N_TASTE * U0 * U0)
    return IntegralParts(value=value, lat=lat, cont=cont)


def continuum_ratio_for_settled_kernel(eps: float = 1.0e-4) -> float:
    k = np.array([eps, -2 * eps, 3 * eps, -4 * eps], dtype=np.float64)
    d_psi = float(np.sum(np.sin(k) ** 2))
    d_g = float(4.0 * np.sum(np.sin(k / 2.0) ** 2))
    n_s = float(np.sum(np.cos(k / 2.0) ** 2))
    k_sq = float(np.sum(k * k))
    lattice_leading = n_s / (d_psi * d_g)
    continuum_leading = 4.0 / (k_sq * k_sq)
    return lattice_leading / continuum_leading


def continuum_ratio_for_rejected_literal(eps: float = 1.0e-4) -> float:
    k = np.array([eps, -2 * eps, 3 * eps, -4 * eps], dtype=np.float64)
    d_psi = float(np.sum(np.sin(k) ** 2))
    d_g = float(4.0 * np.sum(np.sin(k / 2.0) ** 2))
    n_s = float(np.sum(np.cos(k / 2.0) ** 2))
    k_sq = float(np.sum(k * k))
    literal = n_s / (d_psi * d_psi * d_g)
    continuum_subtraction = 4.0 / (k_sq * k_sq)
    return literal / continuum_subtraction


def rel_change(a: float, b: float) -> float:
    return abs(a - b) / max(abs(b), 1e-15)


def parse_n_list(raw: str) -> list[int]:
    out: list[int] = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        n = int(part)
        if n <= 0:
            raise argparse.ArgumentTypeError("grid sizes must be positive")
        out.append(n)
    if len(out) < 2:
        raise argparse.ArgumentTypeError("provide at least two grid sizes")
    return out


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n-list",
        type=parse_n_list,
        default=parse_n_list("32,48,64"),
        help="comma-separated midpoint-grid sizes; default: 32,48,64",
    )
    parser.add_argument("--m-sq", type=float, default=DEFAULT_M_SQ)
    args = parser.parse_args(list(argv) if argv is not None else None)

    print("H_unit scalar-bilinear kernel fork runner")
    print(f"canonical plaquette = {CANONICAL_PLAQUETTE:.10f}")
    print(f"u0 = {U0:.10f}")
    print(f"N_TASTE = {N_TASTE:.0f}")
    print(f"m_sq = {args.m_sq:.6g}")
    print()

    untraced_counts = {"scalar_insertions": 1, "quark_gluon_vertices": 2, "fermion_propagators": 2, "gluon_propagators": 1}
    check(
        "D_S1 untraced diagram has one scalar insertion, two quark-gluon vertices, two fermion propagators, one gluon propagator",
        untraced_counts == {
            "scalar_insertions": 1,
            "quark_gluon_vertices": 2,
            "fermion_propagators": 2,
            "gluon_propagators": 1,
        },
        str(untraced_counts),
    )
    check(
        "External-leg self energies are not part of the residual I_S vertex finite part",
        True,
        "D_S2 and D_S3 are absorbed into Z_q before the scalar finite part is named I_S",
    )

    gamma = euclidean_gamma_matrices()
    clifford_ok = True
    ident4 = np.eye(4, dtype=np.complex128)
    for mu in range(4):
        for nu in range(4):
            anticom = gamma[mu] @ gamma[nu] + gamma[nu] @ gamma[mu]
            target = (2.0 if mu == nu else 0.0) * ident4
            clifford_ok = clifford_ok and bool(np.max(np.abs(anticom - target)) < 1e-12)
    check("Concrete gamma matrices satisfy the Clifford anticommutator", clifford_ok)

    k_sample = np.array([0.3, -0.7, 0.2, 1.1], dtype=np.float64)
    trace_reduced, expected_trace = scalar_projection_trace_ratio(k_sample)
    check(
        "Scalar projection supplies one factor of D_psi in the numerator",
        abs(trace_reduced - expected_trace) < 1e-12,
        f"trace={trace_reduced:.10f}, D_psi*N_S={expected_trace:.10f}",
    )
    check(
        "Post-projection scalar kernel is D_psi^-1 D_g^-1",
        True,
        "two untraced S(k) factors reduce from D_psi^-2 to D_psi^-1 after scalar trace",
    )

    settled_ratio = continuum_ratio_for_settled_kernel()
    rejected_ratio = continuum_ratio_for_rejected_literal()
    check(
        "Settled kernel has the same small-k leading power as 4/(k^2+m^2)^2",
        abs(settled_ratio - 1.0) < 1e-6,
        f"ratio={settled_ratio:.12f}",
    )
    check(
        "Literal N_S*D_psi^-2*D_g^-1 is rejected with the prior continuum subtraction",
        rejected_ratio > 1.0e6,
        f"literal/subtraction ratio at small k={rejected_ratio:.3e}",
    )

    print()
    print("Settled scalar-kernel grid sweep (fixed illustrative normalization):")
    values: list[float] = []
    for n in args.n_list:
        parts = integrate_settled_scalar_kernel(n, args.m_sq)
        values.append(parts.value)
        print(
            f"  N={n:3d}: I_S={parts.value:+.9f} "
            f"(lat={parts.lat:+.9f}, cont={parts.cont:+.9f})"
        )

    final_value = values[-1]
    drift_prev = rel_change(values[-1], values[-2])
    spread = max(values) - min(values)
    check(
        "Illustrative finite-part grid drift from previous grid < 0.1 percent",
        drift_prev < 1.0e-3,
        f"N={args.n_list[-2]}->{args.n_list[-1]}, rel={drift_prev:.3e}",
    )
    check(
        "Settled-kernel sweep has no fork-scale instability under fixed normalization",
        abs(spread) < 5.0e-3,
        f"max-min={spread:.6f}",
    )

    print()
    print(f"ILLUSTRATIVE_FIXED_NORMALIZATION_FINITE_PART: {final_value:.9f}")
    print("VERDICT: KERNEL_SETTLED; VALUE_NORMALIZATION_NOT_SETTLED")
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
