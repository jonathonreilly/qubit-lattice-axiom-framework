#!/usr/bin/env python3
"""Native derivation and independent Peierls reference for the LP prefactor.

This runner is intentionally self-contained.  It does not import a stored
Landau-Peierls constant; the numeric LP prefactor is the exact rational returned
by the symbolic Moyal/star-product derivation below.

Run:
    python3 scripts/frontier_landau_peierls_prefactor_native_derivation_2026_06_13.py
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

import numpy as np
import sympy as sp
from scipy.linalg import eigvalsh
from scipy.special import expit


# Frozen before evaluating the gates.  These values are deliberately not fitted
# to the exact diagonalization output.
TEMPERATURE = 0.5
CHEMICAL_POTENTIAL = -0.9
KGRID_COARSE = 48
KGRID_FINE = 96
L_BSTEP = 24
L_SMALL = 20
L_MEDIUM = 24
L_LARGE = 28
FLUX_STEP = 1
LP_GRID_TOL = 1.0e-13
BSTEP_ABS_TOL = 3.0e-6
BSTEP_RATIO_MAX = 0.35
SIZE_ABS_TOL = 1.5e-5
SIZE_RATIO_MAX = 0.35
LP_EXACT_ABS_TOL = 1.0e-6
NONZERO_RESPONSE_MIN = 1.0e-4


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    tag = "PASS" if ok else "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {name}{suffix}")


@dataclass(frozen=True)
class SymbolicDerivation:
    local_omega_b2: sp.Expr
    integrated_omega_b2: sp.Expr
    response_integrand: sp.Expr
    lp_prefactor: sp.Rational
    divergence_residual: sp.Expr
    target_residual: sp.Expr
    wrong_prefactor_residual: sp.Expr


def derive_symbolic_prefactor() -> SymbolicDerivation:
    """Derive the B^2 response integrand from the magnetic star product.

    For a one-band symbol E(k_x,k_y), magnetic Weyl multiplication is

        a star b = a b + (iB/2){a,b} - (B^2/8) Lambda^2(a,b) + O(B^3).

    The code computes the B^2 term in G_star(E) by star-power recursion for a
    generic polynomial G(E), then maps the polynomial derivatives to the
    arbitrary smooth grand-potential function G.  The final -1/12 appears only
    after the independent periodic divergence identity is applied and the
    centered second difference in B is taken.
    """

    x, y = sp.symbols("x y")
    eps = sp.Function("E")(x, y)
    grand = sp.Function("G")
    c = sp.symbols("c0:8")

    def lambda2(a: sp.Expr, b: sp.Expr) -> sp.Expr:
        return (
            sp.diff(a, x, 2) * sp.diff(b, y, 2)
            - 2 * sp.diff(a, x, y) * sp.diff(b, x, y)
            + sp.diff(a, y, 2) * sp.diff(b, x, 2)
        )

    poly = sum(c[n] * eps**n for n in range(len(c)))
    star_power_b2: list[sp.Expr] = [sp.Integer(0)] * len(c)
    star_power_b2[0] = sp.Integer(0)
    if len(c) > 1:
        star_power_b2[1] = sp.Integer(0)
    for n in range(1, len(c) - 1):
        # If E^{star n} = E^n + B^2 C_n, then
        # E^{star(n+1)} = E^n star E + B^2 C_n E + O(B^4).
        star_power_b2[n + 1] = sp.simplify(
            eps * star_power_b2[n] - sp.Rational(1, 8) * lambda2(eps**n, eps)
        )

    poly_b2 = sp.simplify(sum(c[n] * star_power_b2[n] for n in range(len(c))))

    D = sp.diff(eps, x, 2) * sp.diff(eps, y, 2) - sp.diff(eps, x, y) ** 2
    Q = (
        sp.diff(eps, x) ** 2 * sp.diff(eps, y, 2)
        - 2 * sp.diff(eps, x) * sp.diff(eps, y) * sp.diff(eps, x, y)
        + sp.diff(eps, y) ** 2 * sp.diff(eps, x, 2)
    )

    poly_prime_2 = sp.diff(poly, eps, 2)
    poly_prime_3 = sp.diff(poly, eps, 3)
    derived_poly_residual = sp.simplify(
        poly_b2 + sp.Rational(1, 8) * poly_prime_2 * D
        + sp.Rational(1, 24) * poly_prime_3 * Q
    )
    if derived_poly_residual != 0:
        raise AssertionError(f"star-power derivation failed: {derived_poly_residual}")

    local_omega_b2 = (
        -sp.Rational(1, 8) * sp.diff(grand(eps), eps, 2) * D
        - sp.Rational(1, 24) * sp.diff(grand(eps), eps, 3) * Q
    )

    vx = sp.diff(grand(eps), eps, 2) * (
        sp.diff(eps, x) * sp.diff(eps, y, 2)
        - sp.diff(eps, y) * sp.diff(eps, x, y)
    )
    vy = sp.diff(grand(eps), eps, 2) * (
        sp.diff(eps, y) * sp.diff(eps, x, 2)
        - sp.diff(eps, x) * sp.diff(eps, x, y)
    )
    divergence_residual = sp.simplify(
        sp.diff(vx, x)
        + sp.diff(vy, y)
        - sp.diff(grand(eps), eps, 3) * Q
        - 2 * sp.diff(grand(eps), eps, 2) * D
    )

    # On the Brillouin torus the divergence integrates to zero, hence
    # integral G'''(E) Q = -2 integral G''(E) det Hess(E).
    integrated_omega_b2 = sp.simplify(
        -sp.Rational(1, 8) * sp.diff(grand(eps), eps, 2) * D
        + sp.Rational(1, 12) * sp.diff(grand(eps), eps, 2) * D
    )
    response_integrand = sp.simplify(2 * integrated_omega_b2)
    lp_prefactor = sp.simplify(
        response_integrand / (sp.diff(grand(eps), eps, 2) * D)
    )
    target_residual = sp.simplify(
        response_integrand + sp.Rational(1, 12) * sp.diff(grand(eps), eps, 2) * D
    )
    wrong_prefactor_residual = sp.simplify(
        response_integrand + sp.Rational(1, 11) * sp.diff(grand(eps), eps, 2) * D
    )

    return SymbolicDerivation(
        local_omega_b2=sp.simplify(local_omega_b2),
        integrated_omega_b2=integrated_omega_b2,
        response_integrand=response_integrand,
        lp_prefactor=lp_prefactor,
        divergence_residual=divergence_residual,
        target_residual=target_residual,
        wrong_prefactor_residual=wrong_prefactor_residual,
    )


def fermi_prime(energy: np.ndarray) -> np.ndarray:
    f = expit(-(energy - CHEMICAL_POTENTIAL) / TEMPERATURE)
    return -(f * (1.0 - f)) / TEMPERATURE


def square_lattice_lp_response(kgrid: int, prefactor: sp.Rational) -> float:
    k = (np.arange(kgrid, dtype=float) + 0.5) * (2.0 * np.pi / kgrid) - np.pi
    kx, ky = np.meshgrid(k, k, indexing="ij")
    energy = -2.0 * (np.cos(kx) + np.cos(ky))
    det_hess = 4.0 * np.cos(kx) * np.cos(ky)
    return float(np.mean(float(prefactor) * fermi_prime(energy) * det_hess))


def peierls_hamiltonian_square(L: int, nflux: int) -> np.ndarray:
    """Periodic LxL square-lattice Hofstadter Hamiltonian with n flux quanta."""

    total = L * L
    B = 2.0 * np.pi * nflux / total
    h = np.zeros((total, total), dtype=np.complex128)

    def idx(x: int, y: int) -> int:
        return (x % L) * L + (y % L)

    for x in range(L):
        for y in range(L):
            i = idx(x, y)

            # Landau gauge A_y = B x.  The x-boundary twist makes the vector
            # potential periodic on the magnetic torus when B L^2 = 2 pi n.
            x_phase = np.exp(-1j * B * L * y) if x == L - 1 else 1.0
            j = idx(x + 1, y)
            amp = -x_phase
            h[i, j] += amp
            h[j, i] += np.conj(amp)

            y_phase = np.exp(1j * B * x)
            j = idx(x, y + 1)
            amp = -y_phase
            h[i, j] += amp
            h[j, i] += np.conj(amp)

    return h


def grand_potential(evals: np.ndarray) -> float:
    return float(
        -TEMPERATURE
        * np.sum(np.logaddexp(0.0, -(evals - CHEMICAL_POTENTIAL) / TEMPERATURE))
    )


def exact_peierls_response_per_site(L: int, nflux: int) -> float:
    evals0 = eigvalsh(peierls_hamiltonian_square(L, 0), overwrite_a=True)
    evals_plus = eigvalsh(peierls_hamiltonian_square(L, nflux), overwrite_a=True)
    evals_minus = eigvalsh(peierls_hamiltonian_square(L, -nflux), overwrite_a=True)
    B = 2.0 * np.pi * nflux / (L * L)
    curvature = (
        grand_potential(evals_plus)
        + grand_potential(evals_minus)
        - 2.0 * grand_potential(evals0)
    ) / (B * B)
    return float(curvature / (L * L))


def main() -> int:
    print("Landau-Peierls native prefactor derivation")
    print(f"fixed numeric gate point: T={TEMPERATURE:.17g}, mu={CHEMICAL_POTENTIAL:.17g}")
    print()

    symbolic = derive_symbolic_prefactor()
    print("S1 symbolic Moyal derivation")
    print(f"  local Omega B^2 term: {symbolic.local_omega_b2}")
    print(f"  integrated Omega B^2 term: {symbolic.integrated_omega_b2}")
    print(f"  centered-response prefactor: {symbolic.lp_prefactor}")
    check(
        "star/Moyal derivation gives the LP response prefactor exactly",
        symbolic.target_residual == 0 and symbolic.lp_prefactor == -sp.Rational(1, 12),
        f"prefactor={symbolic.lp_prefactor}",
    )
    check(
        "periodic divergence reduction is symbolic, not a fitted scalar",
        symbolic.divergence_residual == 0,
        f"residual={symbolic.divergence_residual}",
    )
    check(
        "wrong prefactor discriminator rejects -1/11",
        symbolic.wrong_prefactor_residual != 0,
        f"wrong residual={symbolic.wrong_prefactor_residual}",
    )
    print()

    print("S2 derived LP Brillouin-zone integral")
    lp_coarse = square_lattice_lp_response(KGRID_COARSE, symbolic.lp_prefactor)
    lp_fine = square_lattice_lp_response(KGRID_FINE, symbolic.lp_prefactor)
    lp_grid_delta = abs(lp_fine - lp_coarse)
    print(f"  LP kgrid {KGRID_COARSE}: {lp_coarse:.17e}")
    print(f"  LP kgrid {KGRID_FINE}: {lp_fine:.17e}")
    check(
        "derived LP integral is converged under k-grid refinement",
        lp_grid_delta < LP_GRID_TOL,
        f"|fine-coarse|={lp_grid_delta:.3e}, tol={LP_GRID_TOL:.1e}",
    )
    print()

    print("S0 independent finite-lattice Peierls diagonalization")
    r1 = exact_peierls_response_per_site(L_BSTEP, 1)
    r2 = exact_peierls_response_per_site(L_BSTEP, 2)
    r3 = exact_peierls_response_per_site(L_BSTEP, 3)
    bstep_delta_12 = abs(r2 - r1)
    bstep_delta_23 = abs(r3 - r2)
    bstep_ratio = bstep_delta_23 / bstep_delta_12
    print(f"  exact L={L_BSTEP}, nflux=1: {r1:.17e}")
    print(f"  exact L={L_BSTEP}, nflux=2: {r2:.17e}")
    print(f"  exact L={L_BSTEP}, nflux=3: {r3:.17e}")
    check(
        "exact Peierls response is nonzero real diagonalization data",
        abs(r1) > NONZERO_RESPONSE_MIN,
        f"|response|={abs(r1):.3e}",
    )
    check(
        "finite Peierls B-step is converging",
        bstep_delta_12 < BSTEP_ABS_TOL and bstep_ratio < BSTEP_RATIO_MAX,
        (
            f"|r2-r1|={bstep_delta_12:.3e}, "
            f"|r3-r2|/|r2-r1|={bstep_ratio:.3f}"
        ),
    )
    print()

    print("S2 exact-vs-derived thermodynamic comparison")
    exact_small = exact_peierls_response_per_site(L_SMALL, FLUX_STEP)
    exact_medium = r1 if L_MEDIUM == L_BSTEP else exact_peierls_response_per_site(L_MEDIUM, FLUX_STEP)
    exact_large = exact_peierls_response_per_site(L_LARGE, FLUX_STEP)
    err_small = abs(exact_small - lp_fine)
    err_medium = abs(exact_medium - lp_fine)
    err_large = abs(exact_large - lp_fine)
    size_ratio = err_large / err_medium
    print(f"  exact L={L_SMALL}, nflux={FLUX_STEP}: {exact_small:.17e}  err={err_small:.3e}")
    print(f"  exact L={L_MEDIUM}, nflux={FLUX_STEP}: {exact_medium:.17e}  err={err_medium:.3e}")
    print(f"  exact L={L_LARGE}, nflux={FLUX_STEP}: {exact_large:.17e}  err={err_large:.3e}")
    print(f"  derived LP thermodynamic value: {lp_fine:.17e}")
    check(
        "finite-size Peierls sequence converges toward derived LP integral",
        err_medium < SIZE_ABS_TOL and size_ratio < SIZE_RATIO_MAX,
        f"err_medium={err_medium:.3e}, err_large/err_medium={size_ratio:.3f}",
    )
    check(
        "derived -1/12 LP integral matches exact Peierls reference",
        err_large < LP_EXACT_ABS_TOL,
        f"err_large={err_large:.3e}, tol={LP_EXACT_ABS_TOL:.1e}",
    )

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
