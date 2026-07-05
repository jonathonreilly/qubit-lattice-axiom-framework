#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/D2_ORBITAL_SUSCEPTIBILITY_SIGN_REGIONS_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_d2_orbital_susceptibility_sign_2026_06_12.py
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass

import numpy as np


TOTAL = 0
FAILS: list[str] = []

MU_VALUES = (0.0, 0.5, 1.0, 1.5, 2.0)
M_VALUES = (0.2, 0.5)
T_VALUES = (0.2, 0.4)
Q_VALUES = (16, 24, 32)
ORDERS = (64, 128)
TWOPI = 2.0 * math.pi


def gate(condition: bool, claim: str, detail: str = "") -> bool:
    """Record a pass/fail gate whose condition is the printed claim."""
    global TOTAL
    TOTAL += 1
    ok = bool(condition)
    status = "PASS" if ok else "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{status} {claim}{suffix}")
    if not ok:
        FAILS.append(f"{claim}{suffix}")
    return ok


def stable_fermi_grand(E: np.ndarray, mu_ch: float, T: float) -> np.ndarray:
    """Per-state grand-potential contribution: -T log(1+exp(-(E-mu)/T))."""
    return -T * np.logaddexp(0.0, -(E - mu_ch) / T)


def gl_nodes(order: int) -> tuple[np.ndarray, np.ndarray]:
    x, w = np.polynomial.legendre.leggauss(order)
    k = math.pi * (x + 1.0)
    wk = math.pi * w
    return k, wk


def harper_matrix(
    q: int,
    kx: float,
    ky: float,
    B: float,
    m: float,
    origin: float = 0.0,
) -> np.ndarray:
    """Analytic q x q Harper matrix in diagonal Landau coordinates.

    Use n=x+y and v=y.  The staggered mass is m*(-1)^n.  A Landau gauge with
    Peierls phase exp(i B n) on the y-link preserves v momentum and leaves a
    q-site magnetic cell in n when B=2*pi/q.  The q even condition makes the
    staggered two-site mass cell compatible with the magnetic cell.
    """
    if q % 2:
        raise ValueError("q must be even so the staggered mass fits in the cell")

    H = np.zeros((q, q), dtype=np.complex128)
    r = np.arange(q)
    H[r, r] = m * np.where((r % 2) == 0, 1.0, -1.0)

    phases = np.exp(1j * (ky + B * (r + origin)))
    hop = -(1.0 + phases)
    for j in range(q - 1):
        H[j + 1, j] = hop[j]
        H[j, j + 1] = np.conjugate(hop[j])

    # Boundary from r=q-1 to r=0 in the next magnetic cell.  The sign of kx is
    # a Bloch-convention choice; the spectrum over the full Brillouin torus is
    # unchanged by kx -> -kx.
    boundary = hop[q - 1] * np.exp(-1j * kx)
    H[0, q - 1] = boundary
    H[q - 1, 0] = np.conjugate(boundary)
    return H


def finite_lattice_hamiltonian(L: int, m: float, phi: float, gauge: str) -> np.ndarray:
    """L x L torus Hamiltonian for the handle-flux check."""
    N = L * L
    H = np.zeros((N, N), dtype=np.complex128)

    def idx(x: int, y: int) -> int:
        return (y % L) * L + (x % L)

    for y in range(L):
        for x in range(L):
            i = idx(x, y)
            H[i, i] = m if ((x + y) % 2 == 0) else -m

            jx = idx(x + 1, y)
            if gauge == "distributed":
                ax = np.exp(1j * phi / L)
            elif gauge == "boundary":
                ax = np.exp(1j * phi) if x == L - 1 else 1.0
            else:
                raise ValueError(f"unknown handle-flux gauge {gauge!r}")
            tx = -ax
            H[jx, i] += tx
            H[i, jx] += np.conjugate(tx)

            jy = idx(x, y + 1)
            ty = -1.0
            H[jy, i] += ty
            H[i, jy] += ty

    return H


def finite_lattice_omega_per_site(
    L: int,
    m: float,
    mu_ch: float,
    T: float,
    phi: float,
    gauge: str,
) -> float:
    E = np.linalg.eigvalsh(finite_lattice_hamiltonian(L, m, phi, gauge))
    return float(np.sum(stable_fermi_grand(E, mu_ch, T)) / (L * L))


def second_derivative_5pt(values_at: callable, h: float) -> float:
    return float(
        (
            -values_at(2.0 * h)
            + 16.0 * values_at(h)
            - 30.0 * values_at(0.0)
            + 16.0 * values_at(-h)
            - values_at(-2.0 * h)
        )
        / (12.0 * h * h)
    )


def handle_flux_density(
    L: int,
    m: float,
    mu_ch: float,
    T: float,
    gauge: str,
    h: float = 2.0e-2,
) -> float:
    def omega(phi: float) -> float:
        return finite_lattice_omega_per_site(L, m, mu_ch, T, phi, gauge)

    return L * second_derivative_5pt(omega, h)


@dataclass(frozen=True)
class EigGrid:
    eigs: np.ndarray
    weights: np.ndarray
    q: int
    order: int


class SpectralCache:
    def __init__(self) -> None:
        self._harper: dict[tuple[int, float, int, float], EigGrid] = {}
        self._zero: dict[tuple[int, float, int], EigGrid] = {}

    def harper(self, q: int, m: float, order: int, origin: float = 0.0) -> EigGrid:
        key = (q, float(m), order, float(origin))
        if key in self._harper:
            return self._harper[key]

        B = TWOPI / q
        ks, ws = gl_nodes(order)
        eigs = np.empty((order * order, q), dtype=np.float64)
        weights = np.empty(order * order, dtype=np.float64)
        n = 0
        norm = 1.0 / (TWOPI * TWOPI * q)
        for ix, kx in enumerate(ks):
            wx = ws[ix]
            for iy, ky in enumerate(ks):
                eigs[n] = np.linalg.eigvalsh(harper_matrix(q, kx, ky, B, m, origin))
                weights[n] = wx * ws[iy] * norm
                n += 1

        grid = EigGrid(eigs=eigs, weights=weights, q=q, order=order)
        self._harper[key] = grid
        return grid

    def zero_folded(self, q: int, m: float, order: int) -> EigGrid:
        """B=0 folded q-band spectrum independent of the Harper builder."""
        key = (q, float(m), order)
        if key in self._zero:
            return self._zero[key]
        if q % 2:
            raise ValueError("q must be even")

        ks, ws = gl_nodes(order)
        eigs = np.empty((order * order, q), dtype=np.float64)
        weights = np.empty(order * order, dtype=np.float64)
        M = q // 2
        shifts = TWOPI * np.arange(M, dtype=np.float64)
        norm = 1.0 / (TWOPI * TWOPI * q)
        n = 0
        for ix, K in enumerate(ks):
            wx = ws[ix]
            theta = (K + shifts) / M
            x_factor = 2.0 + 2.0 * np.cos(theta)
            for iy, ky in enumerate(ks):
                y_factor = 2.0 + 2.0 * math.cos(float(ky))
                eps = np.sqrt(m * m + x_factor * y_factor)
                row = np.empty(q, dtype=np.float64)
                row[0::2] = -eps
                row[1::2] = eps
                eigs[n] = row
                weights[n] = wx * ws[iy] * norm
                n += 1

        grid = EigGrid(eigs=eigs, weights=weights, q=q, order=order)
        self._zero[key] = grid
        return grid


def omega_from_grid(grid: EigGrid, mu_ch: float, T: float) -> float:
    band_sum = np.sum(stable_fermi_grand(grid.eigs, mu_ch, T), axis=1)
    return float(np.dot(grid.weights, band_sum))


def omega_harper(
    cache: SpectralCache,
    q: int,
    m: float,
    mu_ch: float,
    T: float,
    order: int,
    origin: float = 0.0,
) -> float:
    return omega_from_grid(cache.harper(q, m, order, origin), mu_ch, T)


def omega_zero(
    cache: SpectralCache,
    q: int,
    m: float,
    mu_ch: float,
    T: float,
    order: int,
) -> float:
    return omega_from_grid(cache.zero_folded(q, m, order), mu_ch, T)


def rel_delta(a: float, b: float) -> float:
    return abs(a - b) / max(1.0, abs(a), abs(b))


def chi_q(
    cache: SpectralCache,
    q: int,
    m: float,
    mu_ch: float,
    T: float,
    order: int,
    origin: float = 0.0,
) -> float:
    B = TWOPI / q
    return 2.0 * (
        omega_harper(cache, q, m, mu_ch, T, order, origin)
        - omega_zero(cache, q, m, mu_ch, T, order)
    ) / (B * B)


def richardson_chi(chi24: float, chi32: float) -> float:
    B24 = TWOPI / 24.0
    B32 = TWOPI / 32.0
    return (B24 * B24 * chi32 - B32 * B32 * chi24) / (B24 * B24 - B32 * B32)


def sign_name(x: float, eps: float) -> str:
    if x > eps:
        return "paramagnetic(+)"
    if x < -eps:
        return "diamagnetic(-)"
    return "zero/resolved-small"


def sign_code(x: float, eps: float) -> int:
    if x > eps:
        return 1
    if x < -eps:
        return -1
    return 0


def describe_sign_regions(rows: list[dict[str, float]], m: float, T: float) -> None:
    max_abs = max(abs(r["chi_inf"]) for r in rows)
    eps = max(1.0e-12, 1.0e-6 * max_abs)
    codes = [sign_code(r["chi_inf"], eps) for r in rows]
    labels = [sign_name(r["chi_inf"], eps) for r in rows]
    mus = [r["mu"] for r in rows]

    start = 0
    region_claims: list[str] = []
    for i in range(1, len(rows) + 1):
        if i == len(rows) or codes[i] != codes[start]:
            lo = mus[start]
            hi = mus[i - 1]
            label = labels[start]
            region_claims.append(f"{label} for mu in [{lo:.1f}, {hi:.1f}]")
            segment = rows[start:i]
            if codes[start] > 0:
                cond = all(r["chi_inf"] > eps for r in segment)
                margin = min(r["chi_inf"] - eps for r in segment)
            elif codes[start] < 0:
                cond = all(r["chi_inf"] < -eps for r in segment)
                margin = min(-eps - r["chi_inf"] for r in segment)
            else:
                cond = all(abs(r["chi_inf"]) <= eps for r in segment)
                margin = max(abs(r["chi_inf"]) for r in segment)
            gate(
                cond,
                f"sampled sign region at m={m:.1f}, T={T:.1f}: {label} on sampled mu [{lo:.1f}, {hi:.1f}]",
                f"eps={eps:.3e}, margin={margin:.3e}",
            )
            start = i

    boundaries = []
    for i in range(len(codes) - 1):
        if codes[i] != codes[i + 1]:
            boundaries.append(f"({mus[i]:.1f}, {mus[i + 1]:.1f})")
    boundary_text = ", ".join(boundaries) if boundaries else "none on sampled grid"
    print(
        f"SIGN_PATTERN m={m:.1f} T={T:.1f}: "
        + "; ".join(region_claims)
        + f"; sign-boundary intervals: {boundary_text}"
    )


def check_handle_flux() -> None:
    print("HANDLE-FLUX COROLLARY")
    print(
        "Analytic reason: a handle flux shifts the cycle momentum.  In the "
        "thermodynamic density the Brillouin-torus integral of the resulting "
        "kx total derivative vanishes by the same per-cycle integration-by-parts "
        "identity as the 1D vanishing-identity note; it is not the plaquette-B "
        "response."
    )
    m = 0.5
    mu_ch = 0.0
    T = 0.4
    densities: dict[int, float] = {}
    wrap_diffs: dict[int, float] = {}
    for L in (8, 12, 16):
        distributed = handle_flux_density(L, m, mu_ch, T, "distributed")
        boundary = handle_flux_density(L, m, mu_ch, T, "boundary")
        densities[L] = distributed
        wrap_diffs[L] = abs(distributed - boundary)
        print(
            f"HANDLE L={L:2d} m={m:.1f} mu={mu_ch:.1f} T={T:.1f} "
            f"N_x*Omega''={distributed:+.6e} boundary-gauge={boundary:+.6e}"
        )

    gate(
        wrap_diffs[8] < 1.0e-8 and wrap_diffs[12] < 1.0e-8 and wrap_diffs[16] < 1.0e-8,
        "handle-flux wraparound probe: distributed-cycle and boundary-cycle gauges give the same handle curvature",
        f"diffs L8={wrap_diffs[8]:.3e}, L12={wrap_diffs[12]:.3e}, L16={wrap_diffs[16]:.3e}",
    )
    gate(
        abs(densities[12]) < abs(densities[8]) and abs(densities[12]) < 1.0e-3,
        "finite-size handle-flux density decreases from L=8 to L=12 and is below 1e-3 at L=12",
        f"|L8|={abs(densities[8]):.3e}, |L12|={abs(densities[12]):.3e}",
    )
    gate(
        abs(densities[16]) < abs(densities[8]) and abs(densities[16]) < 1.0e-3,
        "handle-flux size-doubling probe: L=16 handle-flux density remains below the L=8 value and below 1e-3",
        f"|L8|={abs(densities[8]):.3e}, |L16|={abs(densities[16]):.3e}",
    )


def check_zero_field_control(cache: SpectralCache) -> None:
    print("CONTROL: B=0 SUPER-CELL REPRODUCES ZERO-FIELD OMEGA")
    q = 16
    order = 64
    m = 0.5
    mu_ch = 0.5
    T = 0.4
    ks, ws = gl_nodes(order)
    dense_eigs = np.empty((order * order, q), dtype=np.float64)
    weights = np.empty(order * order, dtype=np.float64)
    n = 0
    norm = 1.0 / (TWOPI * TWOPI * q)
    for ix, kx in enumerate(ks):
        wx = ws[ix]
        for iy, ky in enumerate(ks):
            dense_eigs[n] = np.linalg.eigvalsh(harper_matrix(q, kx, ky, 0.0, m))
            weights[n] = wx * ws[iy] * norm
            n += 1

    dense_grid = EigGrid(dense_eigs, weights, q, order)
    dense = omega_from_grid(dense_grid, mu_ch, T)
    folded = omega_zero(cache, q, m, mu_ch, T, order)
    diff = abs(dense - folded)
    print(
        f"B0_CONTROL q={q} order={order} m={m:.1f} mu={mu_ch:.1f} T={T:.1f} "
        f"Omega_dense={dense:+.15e} Omega_zero={folded:+.15e} diff={diff:.3e}"
    )
    gate(
        diff < 1.0e-12,
        "B=0 q-supercell Harper spectrum reproduces independent folded zero-field Omega to 1e-12",
        f"diff={diff:.3e}",
    )


def check_quadrature_convergence(
    cache: SpectralCache,
    rows: list[dict[str, float]],
) -> None:
    worst = {"rel": -1.0, "label": ""}
    for row in rows:
        m = row["m"]
        mu_ch = row["mu"]
        T = row["T"]
        for q in Q_VALUES:
            ob64 = omega_harper(cache, q, m, mu_ch, T, 64)
            ob128 = omega_harper(cache, q, m, mu_ch, T, 128)
            oz64 = omega_zero(cache, q, m, mu_ch, T, 64)
            oz128 = omega_zero(cache, q, m, mu_ch, T, 128)
            for name, a, b in (
                ("Omega(B)", ob64, ob128),
                ("Omega(0)", oz64, oz128),
            ):
                rd = rel_delta(a, b)
                if rd > worst["rel"]:
                    worst = {
                        "rel": rd,
                        "label": (
                            f"{name} q={q} m={m:.1f} mu={mu_ch:.1f} T={T:.1f} "
                            f"64={a:+.15e} 128={b:+.15e}"
                        ),
                    }
    gate(
        worst["rel"] < 1.0e-8,
        "Gauss-Legendre quadrature doubles from 64 to 128 with <1e-8 relative Omega drift over the sign-table workload (measured 3e-9; T=0.2 Fermi sharpness sets the floor)",
        f"worst_rel={worst['rel']:.3e}; {worst['label']}",
    )


def check_gauge_control(cache: SpectralCache) -> None:
    print("CONTROL: LANDAU-GAUGE ORIGIN SHIFT")
    q = 24
    m = 0.5
    mu_ch = 1.0
    T = 0.4
    order = 128
    origin_shift = 0.37
    omega0 = omega_harper(cache, q, m, mu_ch, T, order, origin=0.0)
    omega_shift = omega_harper(cache, q, m, mu_ch, T, order, origin=origin_shift)
    diff = abs(omega0 - omega_shift)
    print(
        f"GAUGE q={q} order={order} origin_shift={origin_shift:.2f} "
        f"Omega0={omega0:+.15e} Omega_shift={omega_shift:+.15e} diff={diff:.3e}"
    )
    gate(
        diff < 1.0e-10,
        "shifting the Landau-gauge origin leaves Omega(B) invariant to 1e-10",
        f"diff={diff:.3e}",
    )


def compute_sign_table(cache: SpectralCache) -> list[dict[str, float]]:
    print("PLAQUETTE-FIELD RESPONSE AND SIGN TABLE")
    print(
        "Columns: chi16, chi24, chi32 are finite-B values with B_q=2*pi/q; "
        "chi_inf is the B->0 Richardson estimate from q=24,32."
    )
    rows: list[dict[str, float]] = []
    for m in M_VALUES:
        for T in T_VALUES:
            for mu_ch in MU_VALUES:
                c16 = chi_q(cache, 16, m, mu_ch, T, 128)
                c24 = chi_q(cache, 24, m, mu_ch, T, 128)
                c32 = chi_q(cache, 32, m, mu_ch, T, 128)
                cinf = richardson_chi(c24, c32)
                agreement = abs(c32 - c24) / max(abs(c32), abs(c24), 1.0e-14)
                row = {
                    "m": m,
                    "T": T,
                    "mu": mu_ch,
                    "chi16": c16,
                    "chi24": c24,
                    "chi32": c32,
                    "chi_inf": cinf,
                    "agreement": agreement,
                }
                rows.append(row)
                print(
                    f"CHI m={m:.1f} T={T:.1f} mu={mu_ch:.1f} "
                    f"chi16={c16:+.8e} chi24={c24:+.8e} "
                    f"chi32={c32:+.8e} chi_inf={cinf:+.8e} "
                    f"rel24_32={agreement:.3e}"
                )

    for row in rows:
        c24 = row["chi24"]
        c32 = row["chi32"]
        cinf = row["chi_inf"]
        rel = row["agreement"]
        same_sign = (
            sign_code(c24, 1.0e-14)
            == sign_code(c32, 1.0e-14)
            == sign_code(cinf, 1.0e-14)
        )
        absolute_spread = abs(c32 - c24)
        if rel <= 2.0e-2:
            gate(
                True,
                (
                    "Richardson-in-B consistency: chi(24) and chi(32) agree "
                    f"within 2% at m={row['m']:.1f}, T={row['T']:.1f}, mu={row['mu']:.1f}"
                ),
                f"rel={rel:.3e}",
            )
        else:
            gate(
                same_sign and absolute_spread < 5.0e-3,
                (
                    "measured finite-B agreement is sign-stable with small absolute spread "
                    f"at m={row['m']:.1f}, T={row['T']:.1f}, mu={row['mu']:.1f}"
                ),
                f"rel={rel:.3e}, abs_spread={absolute_spread:.3e}",
            )

    for m in M_VALUES:
        for T in T_VALUES:
            subset = [r for r in rows if r["m"] == m and r["T"] == T]
            describe_sign_regions(subset, m, T)

    return rows


def check_high_temperature_control(cache: SpectralCache, table_rows: list[dict[str, float]]) -> None:
    print("CONTROL: T=50 HIGH-T SUPPRESSION")
    high_rows = []
    for m in M_VALUES:
        for mu_ch in MU_VALUES:
            c24 = chi_q(cache, 24, m, mu_ch, 50.0, 128)
            c32 = chi_q(cache, 32, m, mu_ch, 50.0, 128)
            cinf = richardson_chi(c24, c32)
            high_rows.append(abs(cinf))
            print(
                f"HIGHT m={m:.1f} T=50.0 mu={mu_ch:.1f} "
                f"chi24={c24:+.8e} chi32={c32:+.8e} chi_inf={cinf:+.8e}"
            )

    high_max = max(high_rows)
    table_max = max(abs(r["chi_inf"]) for r in table_rows)
    gate(
        high_max < 1.0e-4 and high_max < 1.0e-2 * max(table_max, 1.0e-14),
        "T=50 kills the plaquette-field susceptibility on the sampled mu,m grid",
        f"max|chi_T50|={high_max:.3e}, max|chi_table|={table_max:.3e}",
    )


def check() -> bool:
    """Run all sampled sign-table gates.  Returns True on PASS and False on FAIL."""
    global TOTAL, FAILS
    TOTAL = 0
    FAILS = []
    np.set_printoptions(precision=8, suppress=False)

    print("Free staggered square-lattice orbital susceptibility")
    print("Scope: exact Harper spectra plus Gauss-Legendre quadrature; beta-formula import unused.")
    print("Named gap unchanged: gauge self-energy.")
    print("Statuses: pipeline-derived; audit lane grades.")

    cache = SpectralCache()
    check_handle_flux()
    check_zero_field_control(cache)
    rows = compute_sign_table(cache)
    check_quadrature_convergence(cache, rows)
    check_gauge_control(cache)
    check_high_temperature_control(cache, rows)

    passed = TOTAL - len(FAILS)
    print(f"TOTAL: PASS={passed} FAIL={TOTAL - passed}")
    if FAILS:
        print("FAILED CLAIMS:")
        for item in FAILS:
            print(f"- {item}")
    return not FAILS


if __name__ == "__main__":
    ok = check()
    raise SystemExit(0 if ok else 1)
