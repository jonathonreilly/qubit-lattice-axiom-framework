#!/usr/bin/env python3
"""Exact-diagonalization validation runner for the gauged Wilson Schwinger ring.

Companion note:
GAUGED_WILSON_SCHWINGER_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md.

This runner declares import I-GAUGE-W: the Wilson-kernel bridge instantiation
of the record-preservation-forced covariant-hopping class.  The Wilson term is
gauge-invariant-local and hence remains in-class.  This is distinct from both
the staggered Hamiltonian kernel and the two-step transfer kernel; do not
conflate them.

The checks validate finite-volume ED machinery only.  They make no physics
claim and set no audit status.

Momentum convention: Wilson spinors live on every site, so momentum sectors
use the full Brillouin zone P = 2 pi k / N.  The P = theta/2 unit fix used by
the staggered engine does not apply here; theta = P.

Supervisor-construction flags deliberately surfaced by this runner:

* The ring Gauss law forces total charge Q_tot = 0 with
  q_n = n_{n,u} + n_{n,d} - 1, i.e. one-particle-per-site background.
* With a finite W cutoff, magnetic translation is only validated on interior
  vectors whose T and H images remain inside the cutoff.
* Keeping the boundary holonomy as U_holo with U|W> = |W+1> means the g = 0
  gauge-fixed rotor Hamiltonian still shifts W.  The free-dispersion check is
  therefore performed on the decoupled U_holo = 1 comparator.
* SPEC-NOTE: the Wilson hopping matrix is K = -(i sigma1 + r sigma3)/2 with
  r = 1; the one-site magnetic translation shift is empirically checked as
  Delta W = -q_{N-1}; the half-filling background is fixed, not fitted.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import sys
import time
from typing import Callable

sys.dont_write_bytecode = True

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla


R_FIXED = 1.0
CHECK_TOL = 1.0e-12
BAND_TOL = 1.0e-12
DISP_TOL = 1.0e-10
W_TRUNC_TOL = 1.0e-10
REASSEMBLY_TOL = 1.0e-10
RNG_SEED = 20260708


def mode_index(site: int, spin: int) -> int:
    return 2 * site + spin


def site_charge(n_sites: int, fock: int, site: int) -> int:
    del n_sites
    return ((fock >> mode_index(site, 0)) & 1) + ((fock >> mode_index(site, 1)) & 1) - 1


def fock_charge(n_sites: int, fock: int) -> int:
    return fock.bit_count() - n_sites


def charges(n_sites: int, fock: int) -> np.ndarray:
    return np.array([site_charge(n_sites, fock, n) for n in range(n_sites)], dtype=np.int64)


def mass_energy(n_sites: int, fock: int, mass: float, r: float = R_FIXED) -> float:
    total = 0
    for n in range(n_sites):
        total += (fock >> mode_index(n, 0)) & 1
        total -= (fock >> mode_index(n, 1)) & 1
    return (mass + r) * total


def electric_integer_sum(n_sites: int, fock: int, w_value: int) -> int:
    q = charges(n_sites, fock)
    fields = w_value + np.cumsum(q)
    return int(np.dot(fields, fields))


def electric_energy(n_sites: int, fock: int, w_value: int, coupling: float) -> float:
    if coupling == 0.0:
        return 0.0
    return 0.5 * coupling * coupling * electric_integer_sum(n_sites, fock, w_value)


def apply_cdag_c(fock: int, create_mode: int, annihilate_mode: int) -> tuple[int, int] | None:
    """Apply c_create^dag c_annihilate to an occupation bitstring."""
    if ((fock >> annihilate_mode) & 1) == 0:
        return None
    if ((fock >> create_mode) & 1) == 1:
        return None
    lower_annihilate = (1 << annihilate_mode) - 1
    sign = -1 if ((fock & lower_annihilate).bit_count() & 1) else 1
    fock_after_annihilate = fock ^ (1 << annihilate_mode)
    lower_create = (1 << create_mode) - 1
    if ((fock_after_annihilate & lower_create).bit_count() & 1):
        sign = -sign
    return fock_after_annihilate | (1 << create_mode), sign


def translate_fock_by_one(n_sites: int, fock: int) -> tuple[int, int]:
    """Fermionic unitary for ordinary one-site translation, c_n^dag -> c_{n+1}^dag."""
    n_modes = 2 * n_sites
    occupied = [mode for mode in range(n_modes) if (fock >> mode) & 1]
    moved = [(mode + 2) % n_modes for mode in occupied]
    inversions = 0
    for i, left in enumerate(moved):
        for right in moved[i + 1 :]:
            if left > right:
                inversions += 1
    translated = 0
    for mode in moved:
        translated |= 1 << mode
    return translated, (-1 if (inversions & 1) else 1)


def magnetic_w_shift_tail(n_sites: int, fock: int) -> int:
    """Large-gauge W shift for one-site translation on the Q_tot = 0 ring sector."""
    return -int(charges(n_sites, fock)[n_sites - 1])


def ordinary_w_shift_zero(n_sites: int, fock: int) -> int:
    del n_sites, fock
    return 0


def wilson_k_matrix(r: float = R_FIXED) -> np.ndarray:
    """Wilson nearest-neighbor matrix K = -(i sigma1 + r sigma3)/2."""
    # Symbol check:
    # K e^{ip} + K^dag e^{-ip} + (m+r) sigma3
    #   = sigma1 sin p + sigma3 (m + r(1 - cos p)).
    return np.array([[-0.5 * r, -0.5j], [-0.5j, 0.5 * r]], dtype=np.complex128)


@dataclass(frozen=True)
class Basis:
    n_sites: int
    w_max: int
    charge_sector: int | None = 0
    rotor: bool = True

    def __post_init__(self) -> None:
        n_modes = 2 * self.n_sites
        focks = [
            f
            for f in range(1 << n_modes)
            if self.charge_sector is None or fock_charge(self.n_sites, f) == self.charge_sector
        ]
        object.__setattr__(self, "n_modes", n_modes)
        object.__setattr__(self, "focks", np.array(focks, dtype=np.int64))
        object.__setattr__(self, "fock_to_local", {int(f): i for i, f in enumerate(focks)})
        n_w = 2 * self.w_max + 1 if self.rotor else 1
        object.__setattr__(self, "n_w", n_w)
        object.__setattr__(self, "dim", len(focks) * n_w)

    def index(self, fock_local: int, w_index: int = 0) -> int:
        return fock_local * self.n_w + w_index

    def unpack(self, index: int) -> tuple[int, int, int]:
        fock_local = index // self.n_w
        w_index = index % self.n_w
        return fock_local, int(self.focks[fock_local]), w_index

    def w_value(self, w_index: int) -> int:
        return w_index - self.w_max if self.rotor else 0

    def w_index_from_value(self, w_value: int) -> int | None:
        if not self.rotor:
            return 0 if w_value == 0 else None
        if -self.w_max <= w_value <= self.w_max:
            return w_value + self.w_max
        return None


@dataclass
class TranslationMap:
    basis: Basis
    target: np.ndarray
    sign: np.ndarray

    def apply(self, vector: np.ndarray) -> np.ndarray:
        out = np.zeros_like(vector, dtype=np.complex128)
        mask = self.target >= 0
        np.add.at(out, self.target[mask], self.sign[mask] * vector[mask])
        return out

    def matrix(self) -> sp.csr_matrix:
        mask = self.target >= 0
        cols = np.nonzero(mask)[0]
        rows = self.target[mask]
        data = self.sign[mask].astype(np.complex128)
        return sp.coo_matrix((data, (rows, cols)), shape=(self.basis.dim, self.basis.dim)).tocsr()


def build_translation_map(
    basis: Basis,
    w_shift: Callable[[int, int], int] = magnetic_w_shift_tail,
) -> TranslationMap:
    target = np.full(basis.dim, -1, dtype=np.int64)
    sign = np.zeros(basis.dim, dtype=np.complex128)
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        translated_fock, fock_sign = translate_fock_by_one(basis.n_sites, fock)
        translated_local = basis.fock_to_local.get(translated_fock)
        if translated_local is None:
            continue
        delta_w = w_shift(basis.n_sites, fock)
        for w_index in range(basis.n_w):
            old_w = basis.w_value(w_index)
            new_w_index = basis.w_index_from_value(old_w + delta_w)
            source = basis.index(local_f, w_index)
            if new_w_index is None:
                continue
            target[source] = basis.index(translated_local, new_w_index)
            sign[source] = fock_sign
    return TranslationMap(basis=basis, target=target, sign=sign)


def build_many_body_hamiltonian(
    basis: Basis,
    mass: float,
    coupling: float,
    *,
    boundary_holonomy_shifts_w: bool,
    r: float = R_FIXED,
) -> sp.csr_matrix:
    if abs(r - R_FIXED) > 0.0:
        raise ValueError("this supervisor-fixed runner implements Wilson r = 1 only")
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    n_sites = basis.n_sites
    k_matrix = wilson_k_matrix(r)
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        diagonal_mass = mass_energy(n_sites, fock, mass, r)
        for w_index in range(basis.n_w):
            w_value = basis.w_value(w_index)
            source = basis.index(local_f, w_index)
            rows.append(source)
            cols.append(source)
            data.append(diagonal_mass + electric_energy(n_sites, fock, w_value, coupling))

        for link in range(n_sites):
            right = (link + 1) % n_sites
            is_boundary = link == n_sites - 1
            shifts_w = basis.rotor and is_boundary and boundary_holonomy_shifts_w
            delta_w_forward = 1 if shifts_w else 0
            delta_w_backward = -delta_w_forward

            for alpha in range(2):
                for beta in range(2):
                    coefficient = k_matrix[alpha, beta]
                    create_left = mode_index(link, alpha)
                    annihilate_right = mode_index(right, beta)
                    forward = apply_cdag_c(fock, create_left, annihilate_right)
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
                                data.append(coefficient * fermion_sign)

                    create_right = mode_index(right, beta)
                    annihilate_left = mode_index(link, alpha)
                    backward = apply_cdag_c(fock, create_right, annihilate_left)
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
                                data.append(np.conjugate(coefficient) * fermion_sign)

    hamiltonian = sp.coo_matrix((data, (rows, cols)), shape=(basis.dim, basis.dim), dtype=np.complex128)
    hamiltonian.sum_duplicates()
    return hamiltonian.tocsr()


def lowest_eigvals(matrix: sp.spmatrix, k: int, tol: float = 1.0e-12) -> np.ndarray:
    if matrix.shape[0] <= max(2 * k + 2, 96):
        vals = sla.eigvalsh(matrix.toarray())
        return np.sort(vals.real)[:k]
    k_eff = min(matrix.shape[0] - 2, k + max(4, k // 2))
    vals = spla.eigsh(
        matrix,
        k=k_eff,
        which="SA",
        return_eigenvectors=False,
        tol=tol,
        maxiter=8000,
        ncv=min(matrix.shape[0] - 1, max(28, 5 * k_eff + 12)),
    )
    return np.sort(vals.real)[:k]


def projected_vector(vector: np.ndarray, translation: TranslationMap, momentum: float) -> np.ndarray:
    n_steps = translation.basis.n_sites
    accum = np.zeros_like(vector, dtype=np.complex128)
    current = np.asarray(vector, dtype=np.complex128)
    phase = 1.0 + 0.0j
    step_phase = np.exp(-1.0j * momentum)
    for _ in range(n_steps):
        accum += phase * current
        current = translation.apply(current)
        phase *= step_phase
    return accum / n_steps


def deterministic_v0(dim: int, salt: int) -> np.ndarray:
    rng = np.random.default_rng(RNG_SEED + 7919 * salt + dim)
    vec = rng.normal(size=dim) + 1.0j * rng.normal(size=dim)
    norm = np.linalg.norm(vec)
    return vec / norm


def projected_lowest_eigvals(
    hamiltonian: sp.csr_matrix,
    translation: TranslationMap,
    momentum: float,
    k: int,
    tol: float = 1.0e-11,
) -> np.ndarray:
    dim = hamiltonian.shape[0]

    def matvec(vector: np.ndarray) -> np.ndarray:
        pv = projected_vector(vector, translation, momentum)
        return projected_vector(hamiltonian @ pv, translation, momentum)

    operator = spla.LinearOperator((dim, dim), matvec=matvec, dtype=np.complex128)
    salt = int(round((momentum % (2.0 * np.pi)) * 1.0e6)) + 17 * k
    vals = spla.eigsh(
        operator,
        k=k,
        which="SA",
        return_eigenvectors=False,
        tol=tol,
        maxiter=8000,
        ncv=min(dim - 1, max(36, 6 * k + 18)),
        v0=deterministic_v0(dim, salt),
    )
    return np.sort(vals.real)


def sector_lowest_table(
    hamiltonian: sp.csr_matrix,
    translation: TranslationMap,
    k: int,
    tol: float = 1.0e-11,
) -> list[np.ndarray]:
    n_sites = translation.basis.n_sites
    table: list[np.ndarray] = []
    for p_index in range(n_sites):
        momentum = 2.0 * np.pi * p_index / n_sites
        table.append(projected_lowest_eigvals(hamiltonian, translation, momentum, k, tol=tol))
    return table


def ground_sector_index(sector_table: list[np.ndarray]) -> int:
    lows = np.array([vals[0] for vals in sector_table], dtype=np.float64)
    return int(np.argmin(lows))


def safe_random_vector(basis: Basis, rng: np.random.Generator, samples: int = 128) -> np.ndarray:
    vec = np.zeros(basis.dim, dtype=np.complex128)
    candidates: list[int] = []
    interior_limit = max(0, basis.w_max - 3)
    for idx in range(basis.dim):
        _, fock, w_index = basis.unpack(idx)
        w = basis.w_value(w_index)
        shifted = w + magnetic_w_shift_tail(basis.n_sites, fock)
        if abs(w) <= interior_limit and abs(shifted) <= interior_limit:
            candidates.append(idx)
    chosen = rng.choice(candidates, size=min(samples, len(candidates)), replace=False)
    vec[chosen] = rng.normal(size=len(chosen)) + 1.0j * rng.normal(size=len(chosen))
    norm = np.linalg.norm(vec)
    if norm == 0.0:
        raise RuntimeError("empty safe-vector support")
    return vec / norm


def free_one_body_matrix(n_sites: int, mass: float, r: float = R_FIXED) -> np.ndarray:
    h = np.zeros((2 * n_sites, 2 * n_sites), dtype=np.complex128)
    sigma3 = np.array([1.0, -1.0], dtype=np.float64)
    k_matrix = wilson_k_matrix(r)
    for n in range(n_sites):
        for alpha in range(2):
            h[mode_index(n, alpha), mode_index(n, alpha)] += (mass + r) * sigma3[alpha]
        right = (n + 1) % n_sites
        for alpha in range(2):
            for beta in range(2):
                left_mode = mode_index(n, alpha)
                right_mode = mode_index(right, beta)
                h[left_mode, right_mode] += k_matrix[alpha, beta]
                h[right_mode, left_mode] += np.conjugate(k_matrix[alpha, beta])
    return h


def wilson_energy(momentum: float, mass: float, r: float = R_FIXED) -> float:
    return float(np.sqrt(np.sin(momentum) ** 2 + (mass + r * (1.0 - np.cos(momentum))) ** 2))


def analytic_wilson_band(n_sites: int, mass: float, r: float = R_FIXED) -> np.ndarray:
    momenta = 2.0 * np.pi * np.arange(n_sites) / n_sites
    return np.array([wilson_energy(p, mass, r) for p in momenta], dtype=np.float64)


def free_particle_hole_gaps(n_sites: int, mass: float) -> np.ndarray:
    band = analytic_wilson_band(n_sites, mass)
    gaps = np.empty(n_sites, dtype=np.float64)
    for p_index in range(n_sites):
        gaps[p_index] = min(band[(k + p_index) % n_sites] + band[k] for k in range(n_sites))
    return gaps


def build_free_fermion_hamiltonian(n_sites: int, mass: float) -> tuple[Basis, sp.csr_matrix, TranslationMap]:
    basis = Basis(n_sites=n_sites, w_max=0, charge_sector=0, rotor=False)
    hamiltonian = build_many_body_hamiltonian(
        basis,
        mass,
        0.0,
        boundary_holonomy_shifts_w=False,
    )
    translation = build_translation_map(basis, ordinary_w_shift_zero)
    return basis, hamiltonian, translation


def check_magnetic_translation_rule(n_sites: int, rng: np.random.Generator) -> tuple[str, float]:
    candidates: dict[str, Callable[[int, int], int]] = {
        "tail": magnetic_w_shift_tail,
        "minus_tail": lambda n, f: -magnetic_w_shift_tail(n, f),
        "head": lambda n, f: int(charges(n, f)[0]),
        "minus_head": lambda n, f: -int(charges(n, f)[0]),
        "zero": ordinary_w_shift_zero,
    }
    focks = [f for f in range(1 << (2 * n_sites)) if fock_charge(n_sites, f) == 0]
    worst_by_name: dict[str, float] = {}
    for name, shift in candidates.items():
        worst = 0.0
        for _ in range(240):
            fock = int(rng.choice(focks))
            w = int(rng.integers(-2, 3))
            translated_fock, _ = translate_fock_by_one(n_sites, fock)
            old_fields = w + np.cumsum(charges(n_sites, fock))
            new_w = w + shift(n_sites, fock)
            new_fields = new_w + np.cumsum(charges(n_sites, translated_fock))
            rotated_old_fields = np.roll(old_fields, 1)
            worst = max(worst, float(np.max(np.abs(new_fields - rotated_old_fields))))
        worst_by_name[name] = worst
    best = min(worst_by_name, key=worst_by_name.get)
    return best, worst_by_name[best]


def sparse_max_abs(matrix: sp.spmatrix) -> float:
    if matrix.nnz == 0:
        return 0.0
    return float(np.max(np.abs(matrix.data)))


def check_exact_rotor_g0_couples_w() -> bool:
    basis = Basis(n_sites=6, w_max=2, charge_sector=0, rotor=True)
    hamiltonian = build_many_body_hamiltonian(
        basis,
        0.3,
        0.0,
        boundary_holonomy_shifts_w=True,
    )
    coo = hamiltonian.tocoo()
    for row, col, value in zip(coo.row, coo.col, coo.data):
        if abs(value) == 0.0:
            continue
        _, _, row_w = basis.unpack(int(row))
        _, _, col_w = basis.unpack(int(col))
        if row_w != col_w:
            return True
    return False


def check_01(rng: np.random.Generator) -> tuple[bool, str]:
    best_rule, field_error = check_magnetic_translation_rule(8, rng)
    worst_comm = 0.0
    worst_q_comm = 0.0
    worst_electric = 0.0

    q_basis = Basis(n_sites=6, w_max=1, charge_sector=None, rotor=True)
    q_hamiltonian = build_many_body_hamiltonian(q_basis, 0.3, 0.6, boundary_holonomy_shifts_w=True)
    q_coo = q_hamiltonian.tocoo()
    charges_by_index = np.empty(q_basis.dim, dtype=np.int64)
    for idx in range(q_basis.dim):
        _, fock, _ = q_basis.unpack(idx)
        charges_by_index[idx] = fock_charge(q_basis.n_sites, fock)
    if q_coo.nnz:
        q_delta = charges_by_index[q_coo.row] - charges_by_index[q_coo.col]
        worst_q_comm = max(worst_q_comm, float(np.max(np.abs(q_delta * q_coo.data))))

    for n_sites in (6, 8):
        basis = Basis(n_sites=n_sites, w_max=4, charge_sector=0, rotor=True)
        translation = build_translation_map(basis, magnetic_w_shift_tail)
        for mass in (0.3, 0.6):
            for coupling in (0.0, 0.6, 1.0):
                hamiltonian = build_many_body_hamiltonian(
                    basis,
                    mass,
                    coupling,
                    boundary_holonomy_shifts_w=True,
                )
                for _ in range(20):
                    v = safe_random_vector(basis, rng)
                    comm = hamiltonian @ translation.apply(v) - translation.apply(hamiltonian @ v)
                    worst_comm = max(worst_comm, float(np.linalg.norm(comm)))

                for _ in range(20):
                    local_f = int(rng.integers(0, len(basis.focks)))
                    fock = int(basis.focks[local_f])
                    w_index = int(rng.integers(0, basis.n_w))
                    w = basis.w_value(w_index)
                    source = basis.index(local_f, w_index)
                    diag = complex(hamiltonian[source, source])
                    exact_electric = electric_energy(n_sites, fock, w, coupling)
                    got_electric = diag.real - mass_energy(n_sites, fock, mass)
                    direct_sum = int(np.dot(w + np.cumsum(charges(n_sites, fock)), w + np.cumsum(charges(n_sites, fock))))
                    worst_electric = max(
                        worst_electric,
                        abs(electric_integer_sum(n_sites, fock, w) - direct_sum),
                        abs(got_electric - exact_electric),
                        abs(diag.imag),
                    )

    passed = (
        best_rule == "tail"
        and field_error <= CHECK_TOL
        and worst_comm <= CHECK_TOL
        and worst_q_comm <= CHECK_TOL
        and worst_electric <= CHECK_TOL
    )
    detail = (
        f"rule={best_rule},field={field_error:.1e},comm={worst_comm:.1e},"
        f"Q={worst_q_comm:.1e},E={worst_electric:.1e}"
    )
    return passed, detail


def check_02() -> tuple[bool, str]:
    worst_band = 0.0
    worst_sector = 0.0
    for n_sites in (6, 8):
        for mass in (0.3, 0.6):
            one_body = free_one_body_matrix(n_sites, mass)
            one_body_eigs = np.sort(sla.eigvalsh(one_body).real)
            band = analytic_wilson_band(n_sites, mass)
            expected = np.sort(np.concatenate([-band, band]))
            worst_band = max(worst_band, float(np.max(np.abs(one_body_eigs - expected))))

            ph_gaps = free_particle_hole_gaps(n_sites, mass)
            _, hamiltonian, translation = build_free_fermion_hamiltonian(n_sites, mass)
            sector_table = sector_lowest_table(hamiltonian, translation, 4)
            ground_index = ground_sector_index(sector_table)
            ground = sector_table[ground_index][0]
            for p_index in range(n_sites):
                vals = sector_table[(ground_index + p_index) % n_sites]
                excitation = vals[1] - ground if p_index == 0 else vals[0] - ground
                worst_sector = max(worst_sector, abs(float(excitation - ph_gaps[p_index])))
    passed = worst_band <= BAND_TOL and worst_sector <= DISP_TOL
    sample_band = analytic_wilson_band(6, 0.3)
    return passed, f"band={worst_band:.1e},ph={worst_sector:.1e},E6m03={fmt_array(sample_band)}"


def check_03() -> tuple[bool, str]:
    worst = 0.0
    parts: list[str] = []
    for mass in (0.3, 0.6):
        e0 = wilson_energy(0.0, mass)
        epi = wilson_energy(np.pi, mass)
        worst = max(worst, abs(e0 - mass), abs(epi - (mass + 2.0 * R_FIXED)))
        parts.append(f"m={mass}:E0={e0:.12g},Epi={epi:.12g}")
    return worst <= BAND_TOL, f"max={worst:.1e};" + ";".join(parts)


def check_04() -> tuple[bool, str]:
    energies: dict[int, np.ndarray] = {}
    for w_max in (3, 4):
        basis = Basis(n_sites=6, w_max=w_max, charge_sector=0, rotor=True)
        hamiltonian = build_many_body_hamiltonian(
            basis,
            0.3,
            1.0,
            boundary_holonomy_shifts_w=True,
        )
        energies[w_max] = lowest_eigvals(hamiltonian, 2)
    diff = energies[3] - energies[4]
    passed = bool(np.max(np.abs(diff)) <= W_TRUNC_TOL)
    return passed, f"d34=({diff[0]:+.2e},{diff[1]:+.2e})"


def check_05() -> tuple[bool, str]:
    n_sites = 6
    worst = 0.0
    summaries: list[str] = []
    for mass in (0.3, 0.6):
        free_basis, free_h, free_t = build_free_fermion_hamiltonian(n_sites, mass)
        del free_basis
        full = lowest_eigvals(free_h, 12)[:8]
        sector_vals: list[float] = []
        for vals in sector_lowest_table(free_h, free_t, 10):
            sector_vals.extend(vals)
        reassembled = np.sort(np.array(sector_vals, dtype=np.float64))[:8]
        err = float(np.max(np.abs(full - reassembled)))
        worst = max(worst, err)
        summaries.append(f"m={mass},g=0/free:{err:.1e}")

    basis = Basis(n_sites=n_sites, w_max=4, charge_sector=0, rotor=True)
    translation = build_translation_map(basis, magnetic_w_shift_tail)
    for mass in (0.3, 0.6):
        for coupling in (0.6, 1.0):
            hamiltonian = build_many_body_hamiltonian(
                basis,
                mass,
                coupling,
                boundary_holonomy_shifts_w=True,
            )
            full = lowest_eigvals(hamiltonian, 12)[:8]
            sector_vals = []
            for vals in sector_lowest_table(hamiltonian, translation, 10):
                sector_vals.extend(vals)
            reassembled = np.sort(np.array(sector_vals, dtype=np.float64))[:8]
            err = float(np.max(np.abs(full - reassembled)))
            worst = max(worst, err)
            summaries.append(f"m={mass},g={coupling}:{err:.1e}")
    return worst <= REASSEMBLY_TOL, f"max={worst:.1e} [" + ";".join(summaries) + "]"


def check_06() -> tuple[bool, str, dict[float, dict[str, np.ndarray]]]:
    n_sites = 8
    mass = 0.3
    basis = Basis(n_sites=n_sites, w_max=4, charge_sector=0, rotor=True)
    translation = build_translation_map(basis, magnetic_w_shift_tail)
    results: dict[float, dict[str, np.ndarray]] = {}
    gaps: list[float] = []
    ok = True
    for coupling in (0.6, 1.0):
        hamiltonian = build_many_body_hamiltonian(
            basis,
            mass,
            coupling,
            boundary_holonomy_shifts_w=True,
        )
        sector_lows = sector_lowest_table(hamiltonian, translation, 1, tol=1.0e-10)
        ground_index = ground_sector_index(sector_lows)
        ground = sector_lows[ground_index][0]
        p0_vals = projected_lowest_eigvals(
            hamiltonian,
            translation,
            2.0 * np.pi * ground_index / n_sites,
            5,
            tol=1.0e-10,
        )
        p1_index = (ground_index + 1) % n_sites
        p1_vals = projected_lowest_eigvals(
            hamiltonian,
            translation,
            2.0 * np.pi * p1_index / n_sites,
            4,
            tol=1.0e-10,
        )
        p0_excitations = p0_vals[1:5] - ground
        p1_excitations = p1_vals[:4] - ground
        gap = float(p0_excitations[0])
        gaps.append(gap)
        ok = ok and gap > 1.0e-10 and np.all(np.diff(p0_vals[:5]) >= -1.0e-9)
        results[coupling] = {
            "P0_excitations": p0_excitations,
            "P1_excitations": p1_excitations,
        }
    ok = ok and gaps[1] > gaps[0]
    detail = f"gap0(g=.6)={gaps[0]:.8g},gap0(g=1)={gaps[1]:.8g}"
    return ok, detail, results


def fmt_array(values: np.ndarray) -> str:
    return "[" + ",".join(f"{float(x):.6g}" for x in values) + "]"


def main() -> int:
    started = time.time()
    rng = np.random.default_rng(RNG_SEED)
    flags: list[str] = [
        "Q0-ring-Gauss",
        "finite-W-translation-interior",
        "wilson-r1-no-doublers",
    ]
    if check_exact_rotor_g0_couples_w():
        flags.append("g0-Uholo-shifts-W")

    checks: list[tuple[str, bool, str]] = []
    ok01, detail01 = check_01(rng)
    checks.append(("CHECK-01", ok01, detail01))
    ok02, detail02 = check_02()
    checks.append(("CHECK-02", ok02, detail02))
    ok03, detail03 = check_03()
    checks.append(("CHECK-03", ok03, detail03))
    ok04, detail04 = check_04()
    checks.append(("CHECK-04", ok04, detail04))
    ok05, detail05 = check_05()
    checks.append(("CHECK-05", ok05, detail05))
    ok06, detail06, meson = check_06()
    checks.append(("CHECK-06", ok06, detail06))

    passed_all = all(ok for _, ok, _ in checks)
    status = "PASS" if passed_all else "FAIL"
    elapsed = time.time() - started

    check_line = "; ".join(f"{name}={'ok' if ok else 'FAIL'}({detail})" for name, ok, detail in checks)
    print(f"CHECKS {check_line}")
    print(
        "SPEC-NOTE K=-(i*sigma1+r*sigma3)/2; DeltaW=-q[N-1]; "
        "q=n_u+n_d-1; g0 free uses Uholo=1 comparator"
    )
    for coupling in (0.6, 1.0):
        p0 = meson[coupling]["P0_excitations"]
        p1 = meson[coupling]["P1_excitations"]
        print(
            f"MESON g={coupling:.1f} P0={fmt_array(p0)} P=2pi/8={fmt_array(p1)} "
            f"band2=(P0:{p0[1]:.6g},P2pi8:{p1[1]:.6g})"
        )
    print(f"TOTAL {status} elapsed={elapsed:.2f}s flags={','.join(flags)}")
    return 0 if passed_all else 1


if __name__ == "__main__":
    sys.exit(main())
