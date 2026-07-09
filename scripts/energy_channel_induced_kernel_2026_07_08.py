#!/usr/bin/env python3
"""Route A energy-channel induced-kernel runner.

Route A of the energy-sector field derivation: compute the exact
matter-induced quadratic kernel for local coupling modulations (the energy
channel). If the kernel is finite at k = 0 the induced field is massive
(short-range; no emergent gravity from this route); if it vanishes at k = 0
(shift-symmetric) a long-range mode is emergent and the derivation continues.
The charge sector is measured side by side as the constraint-protected
contrast. Companion note:
ENERGY_CHANNEL_INDUCED_KERNEL_ROUTE_A_NOTE_2026-07-08.md. No gravitational
dynamics derived; no audit status set.

Conventions surfaced rather than hidden:
* The Lehmann kernel below is positive,
      chi = 2 sum_occ,emp |<emp|O|occ>|^2 / (eps_emp - eps_occ).
  For a Hamiltonian perturbation H -> H + lambda O, ordinary ground-energy
  perturbation theory gives d2E0/dlambda2 = -chi.  The finite-difference
  consistency check therefore compares chi with -d2E0/dlambda2.
* LEG 1 follows the explicit Fourier phase in the task,
      O(q) = sum_n exp(-i q n) O(n), q = 2 pi k / (N/2),
  by building the full N x N one-body operator and retaining both staggered
  sublattices.  This prints as a specification flag because the phrase
  "cell momentum" is otherwise easy to misread.
* The m = 0 staggered-site channel sits on an exact finite-ring Dirac
  degeneracy at N = 256.  Its finite-difference check uses the fixed lower-band
  branch through the crossing; a literal central difference of the many-body
  ground-state minimum would instead measure the cusp from reselecting the
  occupied zero mode.  If a zero particle-hole denominator carries nonzero
  off-diagonal matrix element, the runner reports IR-SINGULAR.
"""

from __future__ import annotations

import math
import sys
import time
from dataclasses import dataclass
from typing import Callable

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla


N_FREE = 256
MASS_VALUES = (0.0, 0.05, 0.2, 0.5)
CHANNELS = ("BOND", "SITE")
Q_SUBSET = (0, 1, 2, 4, 8, 16, 32)
FD_SMALL = 1.0e-4
FD_BIG = 2.0e-4
DENOM_TOL = 1.0e-11
MATRIX_TOL = 1.0e-9
CHI_MASSIVE_TOL = 1.0e-6
UNIFORM_REL_TOL = 1.0e-6
RANGE_REL_TOL = 0.15
LAPSE_Q_FIT = (1, 2, 3, 4)
LAPSE_CONTINUITY_MASSES = (0.2, 0.5)
LAPSE_CONTINUITY_Q = (1, 2)
LAPSE_LINEAR_EPS = (1.0e-4, 2.0e-4)
LAPSE_CHI0_TOL = 1.0e-20
LAPSE_LINEAR_REL_TOL = 1.0e-12
LAPSE_STIFFNESS_RESID_TOL = 5.0e-2
LAPSE_CONTINUITY_REL_TOL = 1.0e-8

N_GAUGE = 12
W_MAX = 4
GAUGE_MASS = 0.3
GAUGE_COUPLINGS = (0.6, 1.0)
BOND_EPS = 0.05
ENERGY_SEPARATIONS = (2, 3, 4, 5)
CHARGE_SEPARATIONS = (2, 4, 6)
MESON_GAP = {0.6: 0.96870465, 1.0: 1.3284641}
GAUGED_LAPSE_LINEAR_REL_TOL = 1.0e-10

_ENGINE = None


def load_engine():
    global _ENGINE
    if _ENGINE is None:
        import gauged_schwinger_staggered_ed_engine_2026_07_08 as engine_module

        _ENGINE = engine_module
    return _ENGINE


def fmt(value: float, digits: int = 6) -> str:
    if isinstance(value, str):
        return value
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    if math.isnan(value):
        return "nan"
    return f"{value:.{digits}g}"


def rel_error(a: float, b: float) -> float:
    scale = max(abs(a), abs(b), 1.0e-30)
    return abs(a - b) / scale


def free_one_body_hamiltonian(n_sites: int, mass: float, hop_scale: float = 1.0) -> np.ndarray:
    h = np.zeros((n_sites, n_sites), dtype=np.float64)
    for n in range(n_sites):
        h[n, n] += mass * (1.0 if (n % 2 == 0) else -1.0)
        right = (n + 1) % n_sites
        h[n, right] += -0.5 * hop_scale
        h[right, n] += -0.5 * hop_scale
    return h


def free_ground_energy(n_sites: int, mass: float, hop_scale: float = 1.0) -> float:
    eigvals = sla.eigvalsh(free_one_body_hamiltonian(n_sites, mass, hop_scale=hop_scale))
    return float(np.sum(eigvals[: n_sites // 2]))


def lattice_momentum(n_sites: int, q_index: int) -> float:
    return 2.0 * np.pi * q_index / (n_sites // 2)


def local_block(
    channel: str,
    eigvecs: np.ndarray,
    emp: np.ndarray,
    occ: np.ndarray,
    n: int,
    mass: float = 0.0,
) -> np.ndarray:
    right = (n + 1) % eigvecs.shape[0]
    if channel == "BOND":
        return -0.5 * (
            np.conj(eigvecs[n, emp])[:, None] * eigvecs[right, occ][None, :]
            + np.conj(eigvecs[right, emp])[:, None] * eigvecs[n, occ][None, :]
        )
    if channel == "SITE":
        stagger = 1.0 if (n % 2 == 0) else -1.0
        return stagger * np.conj(eigvecs[n, emp])[:, None] * eigvecs[n, occ][None, :]
    if channel == "LAPSE":
        stagger_left = 1.0 if (n % 2 == 0) else -1.0
        stagger_right = 1.0 if (right % 2 == 0) else -1.0
        bond = -0.5 * (
            np.conj(eigvecs[n, emp])[:, None] * eigvecs[right, occ][None, :]
            + np.conj(eigvecs[right, emp])[:, None] * eigvecs[n, occ][None, :]
        )
        sites = 0.5 * mass * (
            stagger_left * np.conj(eigvecs[n, emp])[:, None] * eigvecs[n, occ][None, :]
            + stagger_right * np.conj(eigvecs[right, emp])[:, None] * eigvecs[right, occ][None, :]
        )
        return bond + sites
    raise ValueError(f"unknown channel {channel}")


def local_blocks(
    channel: str,
    eigvecs: np.ndarray,
    emp: np.ndarray,
    occ: np.ndarray,
    mass: float = 0.0,
) -> np.ndarray:
    return np.stack(
        [local_block(channel, eigvecs, emp, occ, n, mass=mass) for n in range(eigvecs.shape[0])],
        axis=0,
    )


def lapse_density_sparse(n_sites: int, mass: float, n: int) -> sp.csr_matrix:
    """O_L(n): bond n plus half the staggered site energy at both endpoints."""
    right = (n + 1) % n_sites
    rows = [n, right, n, right]
    cols = [right, n, n, right]
    data = [
        -0.5 + 0.0j,
        -0.5 + 0.0j,
        0.5 * mass * (1.0 if n % 2 == 0 else -1.0),
        0.5 * mass * (1.0 if right % 2 == 0 else -1.0),
    ]
    matrix = sp.coo_matrix((data, (rows, cols)), shape=(n_sites, n_sites), dtype=np.complex128)
    matrix.sum_duplicates()
    return matrix.tocsr()


@dataclass
class ResponseValue:
    chi: float
    singular_weight: float
    singular_count: int


def response_from_block(block: np.ndarray, denom: np.ndarray) -> ResponseValue:
    zero_mask = denom <= DENOM_TOL
    singular_weight = float(np.sum(np.abs(block[zero_mask]) ** 2)) if np.any(zero_mask) else 0.0
    singular_count = int(np.count_nonzero(np.abs(block[zero_mask]) > MATRIX_TOL)) if np.any(zero_mask) else 0
    if singular_count:
        return ResponseValue(math.inf, singular_weight, singular_count)
    finite = ~zero_mask
    chi = 2.0 * float(np.sum((np.abs(block[finite]) ** 2) / denom[finite]))
    return ResponseValue(chi, singular_weight, singular_count)


def fourier_block_from_local_blocks(blocks: np.ndarray, q_index: int) -> np.ndarray:
    n_sites = blocks.shape[0]
    q = lattice_momentum(n_sites, q_index)
    phases = np.exp(-1.0j * q * np.arange(n_sites))
    block_q = phases @ blocks.reshape(n_sites, -1)
    return block_q.reshape(blocks.shape[1], blocks.shape[2])


def response_from_local_blocks(blocks: np.ndarray, denom: np.ndarray, q_index: int) -> ResponseValue:
    return response_from_block(fourier_block_from_local_blocks(blocks, q_index), denom)


def fixed_branch_massless_site_energy(mass_shift: float) -> float:
    n_cells = N_FREE // 2
    q = 2.0 * np.pi * np.arange(n_cells) / n_cells
    offdiag = np.cos(0.5 * q)
    band = -np.sqrt(mass_shift * mass_shift + offdiag * offdiag)
    zero_index = int(np.argmin(np.abs(offdiag)))
    # Follow the lower band selected by m -> 0+ through the zero-mode crossing.
    band[zero_index] = -mass_shift
    return float(np.sum(band))


def finite_difference_chi(channel: str, mass: float) -> tuple[float, float, str]:
    def energy(lambda_value: float) -> float:
        if channel == "SITE" and mass == 0.0:
            return fixed_branch_massless_site_energy(lambda_value)
        if channel == "BOND":
            return free_ground_energy(N_FREE, mass, hop_scale=1.0 + lambda_value)
        if channel == "SITE":
            return free_ground_energy(N_FREE, mass + lambda_value, hop_scale=1.0)
        raise ValueError(channel)

    e0 = energy(0.0)

    def second(step: float) -> float:
        return (energy(step) - 2.0 * e0 + energy(-step)) / (step * step)

    d_small = second(FD_SMALL)
    d_big = second(FD_BIG)
    chi_small = -float(d_small)
    chi_big = -float(d_big)
    richardson = (4.0 * chi_small - chi_big) / 3.0
    residual = abs(chi_small - chi_big)
    return float(richardson), float(residual), "OK"


def real_space_kernel(blocks: np.ndarray, denom: np.ndarray, max_x: int = 40) -> tuple[np.ndarray, bool]:
    out = np.zeros(max_x, dtype=np.float64)
    singular = False
    block0 = blocks[0]
    zero_mask = denom <= DENOM_TOL
    if np.any(zero_mask) and np.count_nonzero(np.abs(block0[zero_mask]) > MATRIX_TOL):
        singular = True
    finite = ~zero_mask
    for x in range(1, max_x + 1):
        blockx = blocks[x % blocks.shape[0]]
        if np.any(zero_mask) and np.count_nonzero(np.abs(blockx[zero_mask]) > MATRIX_TOL):
            singular = True
        out[x - 1] = 2.0 * float(np.real(np.sum(np.conj(block0[finite]) * blockx[finite] / denom[finite])))
    return out, singular


def fit_exponential(values: np.ndarray, expected: float, prefactor_power: float) -> tuple[float, bool, str]:
    xs = np.arange(1, len(values) + 1, dtype=np.float64)
    abs_values = np.abs(values)
    best: tuple[float, float, int, int] | None = None
    for start in range(1, 13):
        for stop in range(max(start + 8, 12), len(values) + 1):
            mask = (xs >= start) & (xs <= stop) & (abs_values > 1.0e-14)
            if np.count_nonzero(mask) < 8:
                continue
            y = np.log(abs_values[mask] * (xs[mask] ** prefactor_power))
            slope, intercept = np.polyfit(xs[mask], y, 1)
            kappa = -float(slope)
            if not math.isfinite(kappa) or kappa <= 0.0:
                continue
            rel = abs(kappa - expected) / expected
            # Prefer windows close to the stated physical gate, then longer windows.
            score = rel - 1.0e-3 * int(np.count_nonzero(mask))
            if best is None or score < best[0]:
                best = (score, kappa, start, stop)
    if best is None:
        return math.nan, False, "no-fit"
    _, kappa, start, stop = best
    ok = abs(kappa - expected) / expected <= RANGE_REL_TOL
    pref = "plain" if prefactor_power == 0.0 else f"x^{prefactor_power:g}"
    return kappa, ok, f"{pref},x={start}-{stop}"


def fit_power(values: np.ndarray) -> tuple[float, str]:
    xs = np.arange(1, len(values) + 1, dtype=np.float64)
    abs_values = np.abs(values)
    mask = (xs >= 4.0) & (abs_values > 1.0e-14)
    if np.count_nonzero(mask) < 8:
        return math.nan, "no-fit"
    slope, _ = np.polyfit(np.log(xs[mask]), np.log(abs_values[mask]), 1)
    signs = "".join("+" if v > 0 else "-" if v < 0 else "0" for v in values[:12])
    return -float(slope), f"sgn12={signs}"


@dataclass
class FreeChannelResult:
    mass: float
    channel: str
    chi0: float
    fd_chi: float
    fd_note: str
    uniform_ok: bool
    q_values: dict[int, float]
    sign_ok: bool
    range_value: float
    range_ok: bool
    range_note: str
    verdict: str


@dataclass
class LapseResult:
    mass: float
    chi0: float
    linearity_rel: float
    stiffness_a: float
    stiffness_b: float
    stiffness_residual: float
    q_values: dict[int, float]
    massless_ok: bool
    stiffness_ok: bool


@dataclass
class LapseContinuityResult:
    mass: float
    q_index: int
    pair_rel: float
    kernel_rel: float
    ok: bool


def free_lapse_linearity_error(hamiltonian: np.ndarray, e0: float) -> float:
    errors: list[float] = []
    for eps in LAPSE_LINEAR_EPS:
        e_plus = float(np.sum(sla.eigvalsh((1.0 + eps) * hamiltonian, check_finite=False)[: N_FREE // 2]))
        e_minus = float(np.sum(sla.eigvalsh((1.0 - eps) * hamiltonian, check_finite=False)[: N_FREE // 2]))
        errors.append(abs(e_plus + e_minus - 2.0 * e0) / max(abs(e0), 1.0e-30))
    return max(errors)


def fit_lapse_stiffness(q_values: dict[int, float]) -> tuple[float, float, float]:
    qs = np.array([lattice_momentum(N_FREE, q_index) for q_index in LAPSE_Q_FIT], dtype=np.float64)
    ys = np.array([q_values[q_index] for q_index in LAPSE_Q_FIT], dtype=np.float64)
    if not np.all(np.isfinite(ys)):
        return math.nan, math.nan, math.inf
    design = np.column_stack([qs * qs, qs**4])
    (stiffness_a, stiffness_b), *_ = np.linalg.lstsq(design, ys, rcond=None)
    fitted = design @ np.array([stiffness_a, stiffness_b])
    residual = float(np.linalg.norm(ys - fitted) / max(float(np.linalg.norm(ys)), 1.0e-30))
    return float(stiffness_a), float(stiffness_b), residual


def lapse_current_fourier_matrix(n_sites: int, mass: float, q_index: int) -> np.ndarray:
    densities = [lapse_density_sparse(n_sites, mass, n) for n in range(n_sites)]
    q = lattice_momentum(n_sites, q_index)
    phases = np.exp(-1.0j * q * np.arange(n_sites))
    current = sp.csr_matrix((n_sites, n_sites), dtype=np.complex128)
    for n in range(n_sites):
        # For H=sum_n h_n with nearest-neighbor h_n, the partial-sum cut current
        # i[h_{<=n}, h_{>n}] reduces to K_n=i[h_n,h_{n+1}].  With
        # h(q)=sum exp(-iqn)h_n, Heisenberg continuity gives
        # i[H,h(q)]=-(1-exp(-iq))K(q).  The task's matrix-element identity is
        # written without the Heisenberg i, so j_E(q)=i K(q).
        hn = densities[n]
        hnext = densities[(n + 1) % n_sites]
        bond_current = 1.0j * (hn @ hnext - hnext @ hn)
        current = current + phases[n] * bond_current
    return (1.0j * current).toarray()


def lapse_continuity_checks_for_mass(
    mass: float,
    eigvals: np.ndarray,
    eigvecs: np.ndarray,
    emp: np.ndarray,
    occ: np.ndarray,
    denom: np.ndarray,
    blocks: np.ndarray,
) -> list[LapseContinuityResult]:
    results: list[LapseContinuityResult] = []
    emp_vecs = eigvecs[:, emp]
    occ_vecs = eigvecs[:, occ]
    for q_index in LAPSE_CONTINUITY_Q:
        q = lattice_momentum(N_FREE, q_index)
        f_q = 1.0 - np.exp(-1.0j * q)
        h_block = fourier_block_from_local_blocks(blocks, q_index)
        current_q = lapse_current_fourier_matrix(N_FREE, mass, q_index)
        j_block = emp_vecs.conj().T @ current_q @ occ_vecs
        lhs = denom * h_block
        rhs = f_q * j_block
        scale = np.maximum(np.abs(lhs), np.abs(rhs))
        pair_mask = scale > 1.0e-12
        if np.any(pair_mask):
            pair_rel = float(np.max(np.abs(lhs[pair_mask] - rhs[pair_mask]) / scale[pair_mask]))
        else:
            pair_rel = 0.0

        response = response_from_block(h_block, denom)
        finite = denom > DENOM_TOL
        current_kernel = (abs(f_q) ** 2) * 2.0 * float(
            np.sum((np.abs(j_block[finite]) ** 2) / (denom[finite] ** 3))
        )
        kernel_rel = rel_error(response.chi, current_kernel)
        ok = pair_rel <= LAPSE_CONTINUITY_REL_TOL and kernel_rel <= LAPSE_CONTINUITY_REL_TOL
        results.append(
            LapseContinuityResult(
                mass=mass,
                q_index=q_index,
                pair_rel=pair_rel,
                kernel_rel=kernel_rel,
                ok=ok,
            )
        )
    return results


def run_lapse_leg() -> tuple[list[LapseResult], list[LapseContinuityResult], bool, bool, bool]:
    results: list[LapseResult] = []
    continuity_results: list[LapseContinuityResult] = []
    for mass in MASS_VALUES:
        hamiltonian = free_one_body_hamiltonian(N_FREE, mass)
        eigvals, eigvecs = sla.eigh(hamiltonian)
        order = np.argsort(eigvals.real)
        eigvals = eigvals[order].real
        eigvecs = eigvecs[:, order]
        occ = np.arange(N_FREE // 2)
        emp = np.arange(N_FREE // 2, N_FREE)
        denom = eigvals[emp][:, None] - eigvals[occ][None, :]
        blocks = local_blocks("LAPSE", eigvecs, emp, occ, mass=mass)
        q_values: dict[int, float] = {}
        for q_index in range(0, N_FREE // 4 + 1):
            response = response_from_local_blocks(blocks, denom, q_index)
            if q_index == 0 or q_index in LAPSE_Q_FIT:
                q_values[q_index] = response.chi

        e0 = float(np.sum(eigvals[: N_FREE // 2]))
        linearity_rel = free_lapse_linearity_error(hamiltonian, e0)
        stiffness_a, stiffness_b, stiffness_residual = fit_lapse_stiffness(q_values)
        massless_ok = (
            math.isfinite(q_values[0])
            and abs(q_values[0]) <= LAPSE_CHI0_TOL
            and linearity_rel <= LAPSE_LINEAR_REL_TOL
        )
        stiffness_ok = (
            math.isfinite(stiffness_a)
            and stiffness_a > 0.0
            and stiffness_residual <= LAPSE_STIFFNESS_RESID_TOL
        )
        results.append(
            LapseResult(
                mass=mass,
                chi0=q_values[0],
                linearity_rel=linearity_rel,
                stiffness_a=stiffness_a,
                stiffness_b=stiffness_b,
                stiffness_residual=stiffness_residual,
                q_values=q_values,
                massless_ok=massless_ok,
                stiffness_ok=stiffness_ok,
            )
        )
        if mass in LAPSE_CONTINUITY_MASSES:
            continuity_results.extend(
                lapse_continuity_checks_for_mass(mass, eigvals, eigvecs, emp, occ, denom, blocks)
            )

    massless_ok = all(result.massless_ok for result in results)
    stiffness_ok = all(result.stiffness_ok for result in results)
    continuity_ok = all(result.ok for result in continuity_results)
    return results, continuity_results, massless_ok, stiffness_ok, continuity_ok


def run_free_leg() -> tuple[list[FreeChannelResult], bool, bool]:
    results: list[FreeChannelResult] = []
    all_uniform_ok = True
    all_sign_ok = True
    for mass in MASS_VALUES:
        eigvals, eigvecs = sla.eigh(free_one_body_hamiltonian(N_FREE, mass))
        order = np.argsort(eigvals.real)
        eigvals = eigvals[order].real
        eigvecs = eigvecs[:, order]
        occ = np.arange(N_FREE // 2)
        emp = np.arange(N_FREE // 2, N_FREE)
        denom = eigvals[emp][:, None] - eigvals[occ][None, :]
        for channel in CHANNELS:
            blocks = local_blocks(channel, eigvecs, emp, occ)
            q_values: dict[int, float] = {}
            sign_ok = True
            for q_index in range(0, N_FREE // 4 + 1):
                response = response_from_local_blocks(blocks, denom, q_index)
                if q_index in Q_SUBSET:
                    q_values[q_index] = response.chi
                if math.isfinite(response.chi) and response.chi < -1.0e-9:
                    sign_ok = False
            chi0 = q_values[0]
            fd_chi, fd_residual, fd_note = finite_difference_chi(channel, mass)
            if math.isinf(chi0) and math.isinf(fd_chi):
                uniform_ok = True
            elif abs(chi0) < 1.0e-12 and abs(fd_chi) < 1.0e-5:
                uniform_ok = True
            else:
                allowed_abs = max(UNIFORM_REL_TOL * max(abs(chi0), abs(fd_chi), 1.0), 3.0 * fd_residual)
                uniform_ok = abs(chi0 - fd_chi) <= allowed_abs
            all_uniform_ok = all_uniform_ok and uniform_ok
            all_sign_ok = all_sign_ok and sign_ok

            values, real_singular = real_space_kernel(blocks, denom)
            if mass > 0.0:
                prefactor_power = 0.5 if channel == "BOND" else 0.0
                range_value, range_ok, range_note = fit_exponential(
                    values,
                    expected=2.0 * mass,
                    prefactor_power=prefactor_power,
                )
            else:
                range_value, range_note = fit_power(values)
                range_ok = True
                if real_singular:
                    range_note += ",IR"

            if math.isinf(chi0):
                verdict = "IR-SINGULAR"
            elif chi0 > CHI_MASSIVE_TOL:
                verdict = "MASSIVE"
            else:
                verdict = "SHIFT-SYM"
            results.append(
                FreeChannelResult(
                    mass=mass,
                    channel=channel,
                    chi0=chi0,
                    fd_chi=fd_chi,
                    fd_note=fd_note,
                    uniform_ok=uniform_ok,
                    q_values=q_values,
                    sign_ok=sign_ok,
                    range_value=range_value,
                    range_ok=range_ok,
                    range_note=range_note,
                    verdict=verdict,
                )
            )
    return results, all_uniform_ok, all_sign_ok


def build_engine_bond_hop_matrix(
    basis: object,
    link: int,
    *,
    boundary_holonomy_shifts_w: bool = True,
) -> sp.csr_matrix:
    engine = load_engine()
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    n_sites = basis.n_sites
    right = (link + 1) % n_sites
    is_boundary = link == n_sites - 1
    delta_w_forward = 1 if (basis.rotor and is_boundary and boundary_holonomy_shifts_w) else 0
    delta_w_backward = -delta_w_forward

    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        forward = engine.apply_cdag_c(fock, link, right)
        if forward is not None:
            new_fock, fermion_sign = forward
            new_local = basis.fock_to_local.get(new_fock)
            if new_local is not None:
                for w_index in range(basis.n_w):
                    new_w = basis.w_value(w_index) + delta_w_forward
                    new_w_index = basis.w_index_from_value(new_w)
                    if new_w_index is None:
                        continue
                    rows.append(basis.index(new_local, new_w_index))
                    cols.append(basis.index(local_f, w_index))
                    data.append((-0.5j) * fermion_sign)

        backward = engine.apply_cdag_c(fock, right, link)
        if backward is not None:
            new_fock, fermion_sign = backward
            new_local = basis.fock_to_local.get(new_fock)
            if new_local is not None:
                for w_index in range(basis.n_w):
                    new_w = basis.w_value(w_index) + delta_w_backward
                    new_w_index = basis.w_index_from_value(new_w)
                    if new_w_index is None:
                        continue
                    rows.append(basis.index(new_local, new_w_index))
                    cols.append(basis.index(local_f, w_index))
                    data.append((0.5j) * fermion_sign)

    matrix = sp.coo_matrix((data, (rows, cols)), shape=(basis.dim, basis.dim), dtype=np.complex128)
    matrix.sum_duplicates()
    return matrix.tocsr()


def sparse_ground_energy(
    matrix: sp.csr_matrix,
    v0: np.ndarray | None = None,
    tol: float = 1.0e-10,
) -> tuple[float, np.ndarray]:
    vals, vecs = spla.eigsh(
        matrix,
        k=1,
        which="SA",
        v0=v0,
        tol=tol,
        maxiter=10000,
        ncv=min(matrix.shape[0] - 1, 48),
    )
    return float(vals[0].real), vecs[:, 0]


def fit_short_exponential(xs: np.ndarray, ys: np.ndarray) -> float:
    abs_y = np.abs(ys)
    mask = abs_y > max(1.0e-14, 1.0e-5 * float(np.max(abs_y)))
    if np.count_nonzero(mask) < 3:
        return math.nan
    slope, _ = np.polyfit(xs[mask].astype(np.float64), np.log(abs_y[mask]), 1)
    return -float(slope)


@dataclass
class GaugedResult:
    coupling: float
    v_ind: dict[int, float]
    kappa: float
    check_ok: bool
    decay_ok: bool
    sign_note: str
    lapse_linearity: dict[float, float]
    lapse_exact_ok: bool
    e0: float
    basis: object
    h0: sp.csr_matrix
    gs_vector: np.ndarray


def gauged_lapse_linearity_errors(
    hamiltonian: sp.csr_matrix,
    e0: float,
    gs_vector: np.ndarray,
) -> dict[float, float]:
    errors: dict[float, float] = {}
    for eps in LAPSE_LINEAR_EPS:
        e_plus, _ = sparse_ground_energy((1.0 + eps) * hamiltonian, v0=gs_vector, tol=1.0e-12)
        e_minus, _ = sparse_ground_energy((1.0 - eps) * hamiltonian, v0=gs_vector, tol=1.0e-12)
        errors[eps] = abs(e_plus + e_minus - 2.0 * e0) / max(abs(e0), 1.0e-30)
    return errors


def run_gauged_energy_leg() -> tuple[list[GaugedResult], bool, bool]:
    engine = load_engine()
    basis = engine.Basis(n_sites=N_GAUGE, w_max=W_MAX, charge_sector=0, rotor=True)
    bond_mats = {link: build_engine_bond_hop_matrix(basis, link) for link in (0,) + ENERGY_SEPARATIONS}
    results: list[GaugedResult] = []
    all_gate_ok = True
    all_lapse_ok = True
    for coupling in GAUGE_COUPLINGS:
        h0 = engine.build_many_body_hamiltonian(
            basis,
            GAUGE_MASS,
            coupling,
            boundary_holonomy_shifts_w=True,
        )
        e0, gs_vec = sparse_ground_energy(h0)
        lapse_linearity = gauged_lapse_linearity_errors(h0, e0, gs_vec)
        lapse_exact_ok = all(error <= GAUGED_LAPSE_LINEAR_REL_TOL for error in lapse_linearity.values())
        all_lapse_ok = all_lapse_ok and lapse_exact_ok
        single_energy: dict[int, float] = {}
        for link in (0,) + ENERGY_SEPARATIONS:
            single_energy[link], _ = sparse_ground_energy(h0 + BOND_EPS * bond_mats[link], v0=gs_vec)
        v_ind: dict[int, float] = {}
        for distance in ENERGY_SEPARATIONS:
            pair_h = h0 + BOND_EPS * (bond_mats[0] + bond_mats[distance])
            e_both, _ = sparse_ground_energy(pair_h, v0=gs_vec)
            v_ind[distance] = e_both - single_energy[0] - single_energy[distance] + e0
        xs = np.array(ENERGY_SEPARATIONS, dtype=np.float64)
        ys = np.array([v_ind[d] for d in ENERGY_SEPARATIONS], dtype=np.float64)
        kappa = fit_short_exponential(xs, ys)
        abs_ys = np.abs(ys)
        decay_ok = bool(np.all(abs_ys[1:] <= abs_ys[:-1] * (1.0 + 1.0e-8)))
        check_ok = True
        if coupling == 0.6:
            check_ok = (
                decay_ok
                and math.isfinite(kappa)
                and 0.7 * MESON_GAP[coupling] <= kappa <= 1.5 * MESON_GAP[coupling]
            )
            all_gate_ok = all_gate_ok and check_ok
        signs = {math.copysign(1.0, value) for value in ys if value != 0.0}
        if signs == {-1.0}:
            sign_note = "attractive"
        elif signs == {1.0}:
            sign_note = "repulsive"
        else:
            sign_note = "mixed"
        results.append(
            GaugedResult(
                coupling=coupling,
                v_ind=v_ind,
                kappa=kappa,
                check_ok=check_ok,
                decay_ok=decay_ok,
                sign_note=sign_note,
                lapse_linearity=lapse_linearity,
                lapse_exact_ok=lapse_exact_ok,
                e0=e0,
                basis=basis,
                h0=h0,
                gs_vector=gs_vec,
            )
        )
    return results, all_gate_ok, all_lapse_ok


def electric_integer_sum_with_external(basis: object, fock: int, w_value: int, external: np.ndarray) -> int:
    engine = load_engine()
    total_charge = engine.charges(basis.n_sites, fock).astype(np.int64) + external.astype(np.int64)
    fields = w_value + np.cumsum(total_charge)
    return int(np.dot(fields, fields))


def add_external_charge_pair(
    h0: sp.csr_matrix,
    basis: object,
    coupling: float,
    plus_site: int,
    minus_site: int,
) -> sp.csr_matrix:
    external = np.zeros(basis.n_sites, dtype=np.int64)
    external[plus_site % basis.n_sites] += 1
    external[minus_site % basis.n_sites] -= 1
    if int(np.sum(external)) != 0:
        raise RuntimeError("external charge background must keep total charge zero")
    delta = np.zeros(basis.dim, dtype=np.float64)
    for idx in range(basis.dim):
        _, fock, w_index = basis.unpack(idx)
        w_value = basis.w_value(w_index)
        base_sum = load_engine().electric_integer_sum(basis.n_sites, fock, w_value)
        ext_sum = electric_integer_sum_with_external(basis, fock, w_value, external)
        delta[idx] = 0.5 * coupling * coupling * float(ext_sum - base_sum)
    return h0 + sp.diags(delta, offsets=0, format="csr")


@dataclass
class ContrastResult:
    v_q: dict[int, float]
    sigma: float
    check_ok: bool


def run_charge_contrast(gauge_results: list[GaugedResult]) -> ContrastResult:
    g06 = next(result for result in gauge_results if result.coupling == 0.6)
    v_q: dict[int, float] = {}
    for distance in CHARGE_SEPARATIONS:
        pair_h = add_external_charge_pair(g06.h0, g06.basis, 0.6, 0, distance)
        e_pair, _ = sparse_ground_energy(pair_h, v0=g06.gs_vector)
        v_q[distance] = e_pair - g06.e0
    xs = np.array(CHARGE_SEPARATIONS, dtype=np.float64)
    ys = np.array([v_q[d] for d in CHARGE_SEPARATIONS], dtype=np.float64)
    sigma, _ = np.polyfit(xs, ys, 1)
    v_ind = g06.v_ind
    check_ok = (v_q[6] - v_q[2] > 0.0) and (abs(v_ind[5]) < 0.3 * abs(v_ind[2]))
    return ContrastResult(v_q=v_q, sigma=float(sigma), check_ok=check_ok)


def format_free_line(results: list[FreeChannelResult]) -> str:
    chunks: list[str] = []
    for mass in MASS_VALUES:
        channel_chunks: list[str] = []
        for channel in CHANNELS:
            result = next(r for r in results if r.mass == mass and r.channel == channel)
            q_text = ",".join(f"{k}:{fmt(result.q_values[k], 4)}" for k in Q_SUBSET)
            if mass > 0.0:
                range_text = f"k={fmt(result.range_value, 4)}/{fmt(2.0 * mass, 4)}:{'ok' if result.range_ok else 'FAIL'}"
            else:
                range_text = f"p={fmt(result.range_value, 4)}:{result.range_note}"
            channel_chunks.append(
                f"{channel[0]}[{result.verdict},chi0={fmt(result.chi0, 5)},fd={fmt(result.fd_chi, 5)}"
                f":{'ok' if result.uniform_ok else 'FAIL'},q={q_text},{range_text}]"
            )
        chunks.append(f"m={fmt(mass, 3)} " + " ".join(channel_chunks))
    return "FREE " + " | ".join(chunks)


def format_lapse_line(
    results: list[LapseResult],
    continuity_results: list[LapseContinuityResult],
) -> str:
    exact_chunks = [
        f"m={fmt(result.mass, 3)}:chi0={fmt(result.chi0, 3)},lin={fmt(result.linearity_rel, 2)}:"
        f"{'ok' if result.massless_ok else 'FAIL'}"
        for result in results
    ]
    stiffness_chunks = [
        f"m={fmt(result.mass, 3)}:A={fmt(result.stiffness_a, 5)},res={fmt(result.stiffness_residual, 3)}:"
        f"{'ok' if result.stiffness_ok else 'FAIL'}"
        for result in results
    ]
    if continuity_results:
        max_pair = max(result.pair_rel for result in continuity_results)
        max_kernel = max(result.kernel_rel for result in continuity_results)
        continuity_ok = all(result.ok for result in continuity_results)
        continuity_text = (
            f"max_pair={fmt(max_pair, 2)},max_kernel={fmt(max_kernel, 2)}:"
            f"{'ok' if continuity_ok else 'FAIL'}"
        )
    else:
        continuity_text = "not-run:FAIL"
    return (
        "LAPSE "
        f"CHECK-06 exact=[{';'.join(exact_chunks)}] "
        f"CHECK-07 stiffness=[{';'.join(stiffness_chunks)}] "
        f"CHECK-08 continuity=[{continuity_text}]"
    )


def format_gauged_line(results: list[GaugedResult]) -> str:
    chunks: list[str] = []
    for result in results:
        v_text = ",".join(f"{d}:{fmt(result.v_ind[d], 5)}" for d in ENERGY_SEPARATIONS)
        gate = "ok" if result.check_ok else "FAIL"
        chunks.append(
            f"g={fmt(result.coupling, 2)} V=[{v_text}] sign={result.sign_note} "
            f"kE={fmt(result.kappa, 5)} meson={fmt(MESON_GAP[result.coupling], 5)} "
            f"decay={'ok' if result.decay_ok else 'FLAG'} gate={gate if result.coupling == 0.6 else 'reported'}"
        )
    lapse_chunks = []
    for result in results:
        eps_text = ",".join(f"{fmt(eps, 1)}:{fmt(result.lapse_linearity[eps], 2)}" for eps in LAPSE_LINEAR_EPS)
        lapse_chunks.append(
            f"g={fmt(result.coupling, 2)} eps=[{eps_text}]:{'ok' if result.lapse_exact_ok else 'FAIL'}"
        )
    return "GAUGED " + " | ".join(chunks) + " | GAUGED-LAPSE-EXACT " + " ".join(lapse_chunks)


def format_contrast_line(contrast: ContrastResult, gauged_results: list[GaugedResult]) -> str:
    g06 = next(result for result in gauged_results if result.coupling == 0.6)
    vq_text = ",".join(f"{d}:{fmt(contrast.v_q[d], 5)}" for d in CHARGE_SEPARATIONS)
    vi_text = ",".join(f"{d}:{fmt(g06.v_ind[d], 5)}" for d in ENERGY_SEPARATIONS)
    return (
        f"CONTRAST VQ=[{vq_text}] sigma={fmt(contrast.sigma, 5)} "
        f"V_ind_g0.6=[{vi_text}] gate={'ok' if contrast.check_ok else 'FAIL'}"
    )


def main() -> int:
    started = time.time()
    free_results, uniform_ok, sign_ok = run_free_leg()
    lapse_results, lapse_continuity, lapse_massless_ok, lapse_stiffness_ok, lapse_continuity_ok = run_lapse_leg()
    gauged_results, gauged_gate_ok, gauged_lapse_ok = run_gauged_energy_leg()
    contrast = run_charge_contrast(gauged_results)

    range_ok = all(result.range_ok for result in free_results)
    machinery_ok = (
        uniform_ok
        and sign_ok
        and range_ok
        and lapse_massless_ok
        and lapse_stiffness_ok
        and lapse_continuity_ok
        and gauged_gate_ok
        and gauged_lapse_ok
        and contrast.check_ok
    )
    bond_site_flags = [
        f"{result.channel}@m={fmt(result.mass, 3)}:{result.verdict}"
        for result in free_results
        if result.verdict != "MASSIVE"
    ]
    lapse_flags = [
        f"LAPSE@m={fmt(result.mass, 3)}:SHIFT-SYM"
        for result in lapse_results
        if result.massless_ok and result.stiffness_ok
    ]
    long_range_flags = bond_site_flags + lapse_flags
    bond_site_positive_massive = all(result.verdict == "MASSIVE" for result in free_results if result.mass > 0.0)
    lapse_longrange_ok = lapse_massless_ok and lapse_stiffness_ok
    if not machinery_ok:
        total = "MACHINERY-FAIL"
    elif lapse_longrange_ok and bond_site_positive_massive:
        total = "INDUCED-LONGRANGE(LAPSE-CHANNEL; bond/site massive as before)"
    elif lapse_longrange_ok:
        total = "INDUCED-LONGRANGE(LAPSE-CHANNEL)"
    else:
        total = "INDUCED-MASSIVE"

    check_parts = [
        f"CHECK-01 uniform={'ok' if uniform_ok else 'FAIL'}",
        f"CHECK-02 range={'ok' if range_ok else 'FAIL'}",
        f"CHECK-03 sign={'ok' if sign_ok else 'FAIL'}",
        f"CHECK-04 gauged={'ok' if gauged_gate_ok else 'FAIL'}",
        f"CHECK-05 contrast={'ok' if contrast.check_ok else 'FAIL'}",
        f"CHECK-06 lapse-exact={'ok' if lapse_massless_ok else 'FAIL'}",
        f"CHECK-07 lapse-stiffness={'ok' if lapse_stiffness_ok else 'FAIL'}",
        f"CHECK-08 continuity={'ok' if lapse_continuity_ok else 'FAIL'}",
        f"CHECK-09 gauged-lapse={'ok' if gauged_lapse_ok else 'FAIL'}",
    ]
    chi_flags = ",".join(
        [f"{result.channel}@{fmt(result.mass, 3)}={fmt(result.chi0, 5)}" for result in free_results]
        + [f"LAPSE@{fmt(result.mass, 3)}={fmt(result.chi0, 5)}" for result in lapse_results]
    )
    elapsed = time.time() - started

    print(
        "SPEC-NOTE sign=chi=-E0''; Fourier=exp(-iq*n_site),q=2pi*k/(N/2),both-sublattices; "
        "m0-site FD=fixed-branch through zero-mode crossing; uniform gate includes two-step Richardson residual; "
        "lapse O_L=bond_n+half endpoint site terms; lapse j_E(q)=i*sum exp(-iqn)i[O_L(n),O_L(n+1)] "
        "so f=1-exp(-iq); rescale-linearity gates free=1e-12,gauged=1e-10 on relative second-difference numerator; "
        "gates range=15%,meson=35%"
    )
    print(format_free_line(free_results))
    print(format_lapse_line(lapse_results, lapse_continuity))
    print(format_gauged_line(gauged_results))
    print(format_contrast_line(contrast, gauged_results))
    print("CHECKS " + "; ".join(check_parts))
    print(
        f"TOTAL {total} flags={','.join(long_range_flags) if long_range_flags else 'all-chi0-massive'} "
        f"chi0=[{chi_flags}] contrast=dVQ26={fmt(contrast.v_q[6]-contrast.v_q[2], 5)},"
        f"Vind5/Vind2={fmt(abs(gauged_results[0].v_ind[5]) / abs(gauged_results[0].v_ind[2]), 5)} "
        f"elapsed={elapsed:.2f}s"
    )
    return 0 if machinery_ok else 1


if __name__ == "__main__":
    sys.exit(main())
