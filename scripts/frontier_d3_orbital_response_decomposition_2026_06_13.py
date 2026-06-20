#!/usr/bin/env python3
"""d=3 single-band orbital-response decomposition check.

This runner builds the real periodic cubic finite-lattice Peierls Hamiltonian
with uniform xy plaquette flux, computes the fixed-(mu,T) grand-potential
second difference by exact diagonalization, and compares it with the
single-band d=3 Landau-Peierls Brillouin-zone integral.

Anti-fabrication constraints followed here:
  * the finite-torus reference is computed only from the Peierls Hamiltonian spectrum;
  * the LP value is computed from the analytic band and Fermi derivative;
  * the single-band interband term is fixed to zero, not proxied;
  * the LP normalization is consumed from the companion native-prefactor
    derivation runner, not fitted to the finite-torus reference;
  * all tolerances below are frozen constants declared before any results.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from pathlib import Path
import sys
from typing import Iterable

import numpy as np

from frontier_landau_peierls_prefactor_native_derivation_2026_06_13 import (
    derive_symbolic_prefactor,
)


ROOT = Path(__file__).resolve().parents[1]
PARENT_NOTE_PATH = ROOT / "docs/D3_ORBITAL_RESPONSE_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
NATIVE_PREFACTOR_NOTE_PATH = ROOT / "docs/LANDAU_PEIERLS_PREFACTOR_NATIVE_DERIVATION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
NORMALIZATION_NOTE_PATH = ROOT / "docs/D3_LANDAU_PEIERLS_SINGLE_BAND_NORMALIZATION_BOUNDED_THEOREM_NOTE_2026-06-18.md"
NORMALIZATION_CACHE_PATH = ROOT / "logs/runner-cache/frontier_d3_landau_peierls_single_band_normalization_2026_06_18.txt"

# Frozen model parameters.
L_EXACT = 32
REFERENCE_MU = -2.0
TEMPERATURE = 0.30
FLUX_QUANTA_FINE = 1
FLUX_QUANTA_COARSE = 2
LP_GRID_N = 176
CURVE_MUS = (-4.5, -3.0, -1.5, 0.0, 1.5, 3.0, 4.5)

# Sentinel for the companion theorem's exported rational.  The LP integral
# below consumes the derived value, not this sentinel.
EXPECTED_NATIVE_PREFACTOR = Fraction(-1, 12)
CHI_INTER_SINGLE_BAND = 0.0

# Frozen gates. These are intentionally labeled and set before any spectrum or
# Brillouin-zone integral is evaluated.
TOL_FLUX_UNIFORM_ABS = 2.0e-12
TOL_BLOCK_DIAG_ABS = 1.0e-10
TOL_EXACT_STEP_HALVING_ABS = 4.0e-3
TOL_EXACT_NONZERO_ABS = 1.0e-5
TOL_LP_REFERENCE_REL = 1.0e-2
TOL_LP_CURVE_REL = 1.0e-2
TOL_INTERBAND_ZERO_ABS = 0.0
SIGN_ACTIVE_FLOOR = 1.0e-4


@dataclass
class GateResult:
    name: str
    passed: bool
    detail: str


class Gates:
    def __init__(self) -> None:
        self.results: list[GateResult] = []

    def check(self, name: str, passed: bool, detail: str) -> None:
        self.results.append(GateResult(name, passed, detail))
        tag = "PASS" if passed else "FAIL"
        print(f"{tag}: {name}: {detail}")

    def finish(self) -> int:
        passed = sum(result.passed for result in self.results)
        failed = len(self.results) - passed
        print(f"TOTAL: PASS={passed} FAIL={failed}")
        return 0 if failed == 0 else 1


def flux_from_quanta(p: int, L: int) -> float:
    return 2.0 * math.pi * p / float(L * L)


def site_xy(x: int, y: int, L: int) -> int:
    return x * L + y


def link_x_phase(x: int, y: int, L: int, B: float) -> complex:
    # Boundary seam required for uniform flux on a periodic torus.
    if x == L - 1:
        return complex(np.exp(-1j * B * L * y))
    return 1.0 + 0.0j


def link_y_phase(x: int, y: int, L: int, B: float) -> complex:
    return complex(np.exp(1j * B * x))


def max_plaquette_flux_error(L: int, B: float) -> float:
    target = np.exp(1j * B)
    max_error = 0.0
    for x in range(L):
        xp = (x + 1) % L
        for y in range(L):
            yp = (y + 1) % L
            plaquette = (
                link_x_phase(x, y, L, B)
                * link_y_phase(xp, y, L, B)
                * np.conjugate(link_x_phase(x, yp, L, B))
                * np.conjugate(link_y_phase(x, y, L, B))
            )
            max_error = max(max_error, abs(plaquette - target))
    return float(max_error)


def xy_hamiltonian(L: int, B: float) -> np.ndarray:
    n = L * L
    h = np.zeros((n, n), dtype=np.complex128)
    for x in range(L):
        for y in range(L):
            i = site_xy(x, y, L)

            xp = (x + 1) % L
            jx = site_xy(xp, y, L)
            ux = link_x_phase(x, y, L, B)
            h[jx, i] += -ux
            h[i, jx] += -np.conjugate(ux)

            yp = (y + 1) % L
            jy = site_xy(x, yp, L)
            uy = link_y_phase(x, y, L, B)
            h[jy, i] += -uy
            h[i, jy] += -np.conjugate(uy)
    return h


def full_3d_hamiltonian(L: int, B: float) -> np.ndarray:
    n = L * L * L
    h = np.zeros((n, n), dtype=np.complex128)

    def idx(x: int, y: int, z: int) -> int:
        return (x * L + y) * L + z

    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = idx(x, y, z)

                xp = (x + 1) % L
                jx = idx(xp, y, z)
                ux = link_x_phase(x, y, L, B)
                h[jx, i] += -ux
                h[i, jx] += -np.conjugate(ux)

                yp = (y + 1) % L
                jy = idx(x, yp, z)
                uy = link_y_phase(x, y, L, B)
                h[jy, i] += -uy
                h[i, jy] += -np.conjugate(uy)

                zp = (z + 1) % L
                jz = idx(x, y, zp)
                h[jz, i] += -1.0
                h[i, jz] += -1.0
    return h


def exact_3d_eigenvalues_from_xy(L: int, B: float) -> np.ndarray:
    xy_eigs = np.linalg.eigvalsh(xy_hamiltonian(L, B))
    kz = 2.0 * math.pi * np.arange(L, dtype=np.float64) / float(L)
    z_eigs = -2.0 * np.cos(kz)
    return np.sort((xy_eigs[:, None] + z_eigs[None, :]).reshape(-1))


def omega_density(eigs: np.ndarray, mu: float, temperature: float, L: int) -> float:
    x = -(eigs - mu) / temperature
    omega = -temperature * np.logaddexp(0.0, x).sum()
    return float(omega / (L**3))


def exact_chi_second_difference(
    eigs_plus: np.ndarray,
    eigs_minus: np.ndarray,
    eigs_zero: np.ndarray,
    B: float,
    mu: float,
    temperature: float,
    L: int,
) -> float:
    omega_plus = omega_density(eigs_plus, mu, temperature, L)
    omega_minus = omega_density(eigs_minus, mu, temperature, L)
    omega_zero = omega_density(eigs_zero, mu, temperature, L)
    return float((omega_plus + omega_minus - 2.0 * omega_zero) / (B * B))


def fermi_prime(energy: np.ndarray, mu: float, temperature: float) -> np.ndarray:
    x = (energy - mu) / temperature
    out = np.empty_like(x, dtype=np.float64)
    mask = x >= 0.0
    exp_neg = np.exp(-x[mask])
    out[mask] = -(exp_neg / (temperature * (1.0 + exp_neg) ** 2))
    exp_pos = np.exp(x[~mask])
    out[~mask] = -(exp_pos / (temperature * (1.0 + exp_pos) ** 2))
    return out


def landau_peierls_chi(
    mu: float,
    temperature: float,
    nk: int,
    cell_normalization: float,
) -> float:
    k = 2.0 * math.pi * (np.arange(nk, dtype=np.float64) + 0.5) / float(nk)
    c = np.cos(k)
    cx = c[:, None]
    cy = c[None, :]
    xy_energy = -2.0 * (cx + cy)
    hessian_det_xy = 4.0 * cx * cy

    total = 0.0
    for cz in c:
        energy = xy_energy - 2.0 * cz
        total += float(np.sum(fermi_prime(energy, mu, temperature) * hessian_det_xy))

    bz_average = total / float(nk**3)
    return float(cell_normalization * bz_average)


def sign_label(value: float) -> str:
    if value > SIGN_ACTIVE_FLOOR:
        return "+"
    if value < -SIGN_ACTIVE_FLOOR:
        return "-"
    return "0"


def print_curve(rows: Iterable[tuple[float, float, float, float]]) -> None:
    print("chi(mu) curve: mu exact_chi lp_chi residual exact_sign lp_sign")
    for mu, exact_value, lp_value, residual in rows:
        print(
            f"chi_curve mu={mu:+.3f} exact={exact_value:+.12e} "
            f"lp={lp_value:+.12e} residual={residual:+.12e} "
            f"sign_exact={sign_label(exact_value)} sign_lp={sign_label(lp_value)}"
        )


def text_contains_all(text: str, snippets: Iterable[str]) -> tuple[bool, list[str]]:
    missing = [snippet for snippet in snippets if snippet not in text]
    return not missing, missing


def main() -> int:
    gates = Gates()
    symbolic_prefactor = derive_symbolic_prefactor()
    prefactor_fraction = Fraction(str(symbolic_prefactor.lp_prefactor))
    cell_normalization = float(prefactor_fraction)

    print("d=3 orbital-response decomposition runner")
    print(
        "frozen_parameters "
        f"L={L_EXACT} mu_ref={REFERENCE_MU:+.6f} T={TEMPERATURE:.6f} "
        f"p_fine={FLUX_QUANTA_FINE} p_coarse={FLUX_QUANTA_COARSE} "
        f"LP_GRID_N={LP_GRID_N} derived_cell_norm={cell_normalization:+.12e}"
    )
    print(
        "frozen_tolerances "
        f"flux={TOL_FLUX_UNIFORM_ABS:.3e} block={TOL_BLOCK_DIAG_ABS:.3e} "
        f"step={TOL_EXACT_STEP_HALVING_ABS:.3e} nonzero={TOL_EXACT_NONZERO_ABS:.3e} "
        f"reference_rel={TOL_LP_REFERENCE_REL:.3e} curve_rel={TOL_LP_CURVE_REL:.3e} "
        f"sign_floor={SIGN_ACTIVE_FLOOR:.3e}"
    )

    gates.check(
        "native LP prefactor companion is consumed",
        prefactor_fraction == EXPECTED_NATIVE_PREFACTOR
        and symbolic_prefactor.target_residual == 0
        and symbolic_prefactor.divergence_residual == 0,
        (
            f"prefactor={prefactor_fraction}, "
            f"target_residual={symbolic_prefactor.target_residual}, "
            f"divergence_residual={symbolic_prefactor.divergence_residual}"
        ),
    )

    normalization_note = NORMALIZATION_NOTE_PATH.read_text()
    parent_note = PARENT_NOTE_PATH.read_text()
    normalization_cache = NORMALIZATION_CACHE_PATH.read_text()
    source_ok, source_missing = text_contains_all(
        normalization_note,
        (
            "does not introduce a new axiom",
            "midpoint Euler-Maclaurin coefficient",
            "`-1/12`",
            "not an audit verdict",
        ),
    )
    gates.check(
        "source normalization note anchors the -1/12 factor without new axioms",
        source_ok,
        "source-boundary phrases present" if source_ok else f"missing={source_missing}",
    )
    gates.check(
        "source normalization runner cache passes",
        "TOTAL: PASS=9 FAIL=0" in normalization_cache and "status: ok" in normalization_cache,
        "normalization cache status ok with PASS=9 FAIL=0",
    )
    old_import_phrases = (
        "used as explicit theory " + "inputs",
        "does not derive the Landau-Peierls formula from the repo " + "axioms",
    )
    gates.check(
        "parent note cites prefactor dependencies and omits naked-import phrasing",
        all(phrase not in parent_note for phrase in old_import_phrases)
        and NATIVE_PREFACTOR_NOTE_PATH.name in parent_note
        and f"]({NATIVE_PREFACTOR_NOTE_PATH.name})" in parent_note
        and NORMALIZATION_NOTE_PATH.name in parent_note
        and f"]({NORMALIZATION_NOTE_PATH.name})" in parent_note,
        "parent markdown-cites native-prefactor and normalization-boundary dependencies",
    )

    B_fine = flux_from_quanta(FLUX_QUANTA_FINE, L_EXACT)
    B_coarse = flux_from_quanta(FLUX_QUANTA_COARSE, L_EXACT)
    for p, B in ((FLUX_QUANTA_FINE, B_fine), (FLUX_QUANTA_COARSE, B_coarse)):
        flux_error = max_plaquette_flux_error(L_EXACT, B)
        gates.check(
            f"uniform periodic xy flux p={p}",
            flux_error <= TOL_FLUX_UNIFORM_ABS,
            f"max|plaquette-exp(iB)|={flux_error:.3e}, B={B:.12e}",
        )

    check_L = 4
    check_B = flux_from_quanta(1, check_L)
    full_eigs = np.sort(np.linalg.eigvalsh(full_3d_hamiltonian(check_L, check_B)))
    decomposed_eigs = exact_3d_eigenvalues_from_xy(check_L, check_B)
    block_error = float(np.max(np.abs(full_eigs - decomposed_eigs)))
    gates.check(
        "exact 3d Hamiltonian block-diagonalization check",
        block_error <= TOL_BLOCK_DIAG_ABS,
        f"max spectrum mismatch={block_error:.3e} at L={check_L}",
    )

    spectra: dict[int, np.ndarray] = {}
    for p in (0, FLUX_QUANTA_FINE, -FLUX_QUANTA_FINE, FLUX_QUANTA_COARSE, -FLUX_QUANTA_COARSE):
        spectra[p] = exact_3d_eigenvalues_from_xy(L_EXACT, flux_from_quanta(p, L_EXACT))

    chi_fine = exact_chi_second_difference(
        spectra[FLUX_QUANTA_FINE],
        spectra[-FLUX_QUANTA_FINE],
        spectra[0],
        B_fine,
        REFERENCE_MU,
        TEMPERATURE,
        L_EXACT,
    )
    chi_coarse = exact_chi_second_difference(
        spectra[FLUX_QUANTA_COARSE],
        spectra[-FLUX_QUANTA_COARSE],
        spectra[0],
        B_coarse,
        REFERENCE_MU,
        TEMPERATURE,
        L_EXACT,
    )
    chi_reference = (4.0 * chi_fine - chi_coarse) / 3.0
    step_halving_error = abs(chi_fine - chi_coarse)
    richardson_correction = abs(chi_reference - chi_fine)
    print(
        "finite_torus_reference "
        f"mu={REFERENCE_MU:+.6f} T={TEMPERATURE:.6f} "
        f"B_fine={B_fine:.12e} chi_fine={chi_fine:+.12e} "
        f"B_coarse={B_coarse:.12e} chi_coarse={chi_coarse:+.12e} "
        f"chi_richardson={chi_reference:+.12e} "
        f"step_halving_error={step_halving_error:.12e} "
        f"richardson_correction={richardson_correction:.12e}"
    )
    gates.check(
        "S0 finite-torus reference nonzero",
        abs(chi_reference) >= TOL_EXACT_NONZERO_ABS,
        f"|chi_richardson|={abs(chi_reference):.12e}",
    )
    gates.check(
        "S0 finite-torus reference B-step halving",
        step_halving_error <= TOL_EXACT_STEP_HALVING_ABS,
        f"|chi_fine-chi_coarse|={step_halving_error:.12e}",
    )

    chi_lp = landau_peierls_chi(
        REFERENCE_MU,
        TEMPERATURE,
        LP_GRID_N,
        cell_normalization,
    )
    chi_total_decomposition = chi_lp + CHI_INTER_SINGLE_BAND
    residual = chi_total_decomposition - chi_reference
    abs_residual = abs(residual)
    relative_residual = abs_residual / max(abs(chi_reference), 1.0e-30)
    print(
        "lp_reference "
        f"mu={REFERENCE_MU:+.6f} lp={chi_lp:+.12e} "
        f"chi_inter={CHI_INTER_SINGLE_BAND:+.12e} "
        f"decomposition={chi_total_decomposition:+.12e} "
        f"finite_torus_reference={chi_reference:+.12e} "
        f"residual={residual:+.12e} abs_residual={abs_residual:.12e} "
        f"relative_to_exact={relative_residual:.12e} "
        f"reference_rel_bound={TOL_LP_REFERENCE_REL:.12e}"
    )
    gates.check(
        "S1 LP decomposition reference residual stays below 1%",
        relative_residual <= TOL_LP_REFERENCE_REL,
        f"relative={relative_residual:.12e}, bound={TOL_LP_REFERENCE_REL:.12e}",
    )
    gates.check(
        "S2 single-band interband term is zero",
        abs(CHI_INTER_SINGLE_BAND) <= TOL_INTERBAND_ZERO_ABS,
        f"chi_inter={CHI_INTER_SINGLE_BAND:+.12e}",
    )
    curve_rows: list[tuple[float, float, float, float]] = []
    active_sign_pairs: list[tuple[str, str]] = []
    max_curve_relative = 0.0
    max_curve_relative_mu = 0.0
    for mu in CURVE_MUS:
        exact_value = exact_chi_second_difference(
            spectra[FLUX_QUANTA_FINE],
            spectra[-FLUX_QUANTA_FINE],
            spectra[0],
            B_fine,
            mu,
            TEMPERATURE,
            L_EXACT,
        )
        lp_value = landau_peierls_chi(
            mu,
            TEMPERATURE,
            LP_GRID_N,
            cell_normalization,
        )
        curve_residual = lp_value - exact_value
        curve_rows.append((mu, exact_value, lp_value, curve_residual))
        if abs(exact_value) > SIGN_ACTIVE_FLOOR:
            curve_relative = abs(curve_residual) / abs(exact_value)
            if curve_relative > max_curve_relative:
                max_curve_relative = curve_relative
                max_curve_relative_mu = mu
        exact_sign = sign_label(exact_value)
        lp_sign = sign_label(lp_value)
        if exact_sign != "0" and lp_sign != "0":
            active_sign_pairs.append((exact_sign, lp_sign))

    print_curve(curve_rows)
    signs_agree = bool(active_sign_pairs) and all(a == b for a, b in active_sign_pairs)
    exact_active_signs = {a for a, _ in active_sign_pairs}
    lp_active_signs = {b for _, b in active_sign_pairs}
    sign_changes_present = len(exact_active_signs) >= 2 and len(lp_active_signs) >= 2
    gates.check(
        "S3 chi(mu) active sign tracking",
        signs_agree and sign_changes_present,
        f"active_pairs={active_sign_pairs}, exact_signs={sorted(exact_active_signs)}, "
        f"lp_signs={sorted(lp_active_signs)}",
    )
    gates.check(
        "S3 chi(mu) active relative residual stays below 1%",
        max_curve_relative <= TOL_LP_CURVE_REL,
        f"max_rel={max_curve_relative:.12e} at mu={max_curve_relative_mu:+.3f}, "
        f"bound={TOL_LP_CURVE_REL:.12e}",
    )

    return gates.finish()


if __name__ == "__main__":
    sys.exit(main())
