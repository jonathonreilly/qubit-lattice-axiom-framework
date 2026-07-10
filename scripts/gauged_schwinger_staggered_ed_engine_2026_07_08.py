#!/usr/bin/env python3
"""Exact-diagonalization validation runner for the gauged staggered Schwinger chain.

Companion note: GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md.

This runner implements one imported finite Hamiltonian comparator. It validates
finite-volume ED machinery only; it derives neither the comparator from the
framework nor any physics-status or equivalence claim.

Convention note: the Hamiltonian staggered one-body kernel checked here has
E(p) = sqrt(m^2 + sin^2 p).  The two-step arcsinh dispersion in
docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md
is the transfer-matrix cousin and is not silently conflated with this
first-order Hamiltonian kernel.

Supervisor-construction flags deliberately surfaced by this runner:

* The selected ring Gauss sector has total staggered charge Q_tot = 0. The
  Fock x rotor bookkeeping space is useful for construction, but exact
  magnetic translation of E_n = W + sum_{k<=n} q_k is a physical-sector
  statement.
* With a finite W cutoff, magnetic translation is not an everywhere-defined
  unitary on the truncated rotor.  CHECK-01 therefore probes charge-zero
  vectors whose T and H images remain inside the cutoff.
* Keeping the boundary holonomy as U_holo with U|W> = |W+1> means the g = 0
  gauge-fixed rotor Hamiltonian still shifts W.  The free-dispersion check is
  consequently performed on the decoupled U_holo = 1 Hamiltonian comparator
  asserted by the supervisor, and the exact rotor coupling is reported as a
  engineering flag rather than hidden.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import sys
import time
from typing import Callable

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla


CHECK_TOL = 1.0e-12
DISP_TOL = 1.0e-10
T2_TOL = 1.0e-12
RNG_SEED = 20260708


def site_charge(n: int, occupied: int) -> int:
    """Staggered charge q_n = occ_n - background_n."""
    return occupied - (n & 1)


def fock_charge(n_sites: int, fock: int) -> int:
    return fock.bit_count() - n_sites // 2


def charges(n_sites: int, fock: int) -> np.ndarray:
    return np.array([site_charge(n, (fock >> n) & 1) for n in range(n_sites)], dtype=np.int64)


def mass_energy(n_sites: int, fock: int, mass: float) -> float:
    total = 0
    for n in range(n_sites):
        if (fock >> n) & 1:
            total += 1 if (n % 2 == 0) else -1
    return mass * total


def electric_integer_sum(n_sites: int, fock: int, w_value: int) -> int:
    q = charges(n_sites, fock)
    fields = w_value + np.cumsum(q)
    return int(np.dot(fields, fields))


def electric_energy(n_sites: int, fock: int, w_value: int, coupling: float) -> float:
    if coupling == 0.0:
        return 0.0
    return 0.5 * coupling * coupling * electric_integer_sum(n_sites, fock, w_value)


def apply_cdag_c(fock: int, create_site: int, annihilate_site: int) -> tuple[int, int] | None:
    """Apply c_create^dag c_annihilate to an occupation bitstring."""
    if ((fock >> annihilate_site) & 1) == 0:
        return None
    if ((fock >> create_site) & 1) == 1:
        return None
    lower_annihilate = (1 << annihilate_site) - 1
    sign = -1 if ((fock & lower_annihilate).bit_count() & 1) else 1
    fock_after_annihilate = fock ^ (1 << annihilate_site)
    lower_create = (1 << create_site) - 1
    if ((fock_after_annihilate & lower_create).bit_count() & 1):
        sign = -sign
    return fock_after_annihilate | (1 << create_site), sign


def translate_fock_by_two(n_sites: int, fock: int) -> tuple[int, int]:
    """Fermionic unitary for ordinary translation by two staggered sites.

    The operator maps c_n^dag -> c_{n+2}^dag and returns the occupation
    bitstring plus the parity needed to restore canonical site ordering.
    """
    occupied = [n for n in range(n_sites) if (fock >> n) & 1]
    moved = [(n + 2) % n_sites for n in occupied]
    inversions = 0
    for i, left in enumerate(moved):
        for right in moved[i + 1 :]:
            if left > right:
                inversions += 1
    translated = 0
    for n in moved:
        translated |= 1 << n
    return translated, (-1 if (inversions & 1) else 1)


def magnetic_w_shift_tail(n_sites: int, fock: int) -> int:
    """W shift for site translation n -> n+2 on the Q_tot = 0 ring sector."""
    q = charges(n_sites, fock)
    return -int(q[n_sites - 2] + q[n_sites - 1])


def ordinary_w_shift_zero(n_sites: int, fock: int) -> int:
    del n_sites, fock
    return 0


@dataclass(frozen=True)
class Basis:
    n_sites: int
    w_max: int
    charge_sector: int | None = 0
    rotor: bool = True

    def __post_init__(self) -> None:
        focks = [
            f
            for f in range(1 << self.n_sites)
            if self.charge_sector is None or fock_charge(self.n_sites, f) == self.charge_sector
        ]
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


def build_translation_map(basis: Basis, w_shift: Callable[[int, int], int]) -> TranslationMap:
    target = np.full(basis.dim, -1, dtype=np.int64)
    sign = np.zeros(basis.dim, dtype=np.complex128)
    for local_f, fock in enumerate(basis.focks):
        translated_fock, fock_sign = translate_fock_by_two(basis.n_sites, int(fock))
        translated_local = basis.fock_to_local.get(translated_fock)
        if translated_local is None:
            continue
        delta_w = w_shift(basis.n_sites, int(fock))
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
) -> sp.csr_matrix:
    rows: list[int] = []
    cols: list[int] = []
    data: list[complex] = []
    n_sites = basis.n_sites
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        diagonal_mass = mass_energy(n_sites, fock, mass)
        for w_index in range(basis.n_w):
            w_value = basis.w_value(w_index)
            source = basis.index(local_f, w_index)
            rows.append(source)
            cols.append(source)
            data.append(diagonal_mass + electric_energy(n_sites, fock, w_value, coupling))

        for link in range(n_sites):
            right = (link + 1) % n_sites
            is_boundary = link == n_sites - 1
            delta_w_forward = 1 if (basis.rotor and is_boundary and boundary_holonomy_shifts_w) else 0
            delta_w_backward = -delta_w_forward

            forward = apply_cdag_c(fock, link, right)
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

            backward = apply_cdag_c(fock, right, link)
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

    hamiltonian = sp.coo_matrix((data, (rows, cols)), shape=(basis.dim, basis.dim), dtype=np.complex128)
    hamiltonian.sum_duplicates()
    return hamiltonian.tocsr()


def deterministic_v0(size: int) -> np.ndarray:
    """Return a fixed normalized start vector for reproducible ARPACK output."""

    vector = np.linspace(1.0, 2.0, size, dtype=np.float64)
    return vector / np.linalg.norm(vector)


def lowest_eigvals(matrix: sp.spmatrix, k: int, tol: float = 1.0e-12) -> np.ndarray:
    if matrix.shape[0] <= max(2 * k + 2, 64):
        vals = sla.eigvalsh(matrix.toarray())
        return np.sort(vals.real)[:k]
    vals = spla.eigsh(
        matrix,
        k=k,
        which="SA",
        return_eigenvectors=False,
        tol=tol,
        maxiter=5000,
        ncv=min(matrix.shape[0] - 1, max(24, 4 * k + 8)),
        v0=deterministic_v0(matrix.shape[0]),
    )
    return np.sort(vals.real)


def safe_random_vector(basis: Basis, rng: np.random.Generator, samples: int = 96) -> np.ndarray:
    """Random charge-zero vector with enough W margin for CHECK-01 commutators."""
    vec = np.zeros(basis.dim, dtype=np.complex128)
    candidates: list[int] = []
    for idx in range(basis.dim):
        _, fock, w_index = basis.unpack(idx)
        w = basis.w_value(w_index)
        if abs(w) <= max(0, basis.w_max - 3):
            shifted = w + magnetic_w_shift_tail(basis.n_sites, fock)
            if -basis.w_max + 1 <= shifted <= basis.w_max - 1:
                candidates.append(idx)
    chosen = rng.choice(candidates, size=min(samples, len(candidates)), replace=False)
    vec[chosen] = rng.normal(size=len(chosen)) + 1.0j * rng.normal(size=len(chosen))
    norm = np.linalg.norm(vec)
    if norm == 0.0:
        raise RuntimeError("empty safe-vector support")
    return vec / norm


def check_magnetic_translation_rule(n_sites: int, rng: np.random.Generator) -> tuple[str, float]:
    candidates: dict[str, Callable[[int, int], int]] = {
        "tail": magnetic_w_shift_tail,
        "minus_tail": lambda n, f: -magnetic_w_shift_tail(n, f),
        "head": lambda n, f: int(charges(n, f)[0] + charges(n, f)[1]),
        "minus_head": lambda n, f: -int(charges(n, f)[0] + charges(n, f)[1]),
        "zero": ordinary_w_shift_zero,
    }
    focks = [f for f in range(1 << n_sites) if fock_charge(n_sites, f) == 0]
    worst_by_name: dict[str, float] = {}
    for name, shift in candidates.items():
        worst = 0.0
        for _ in range(200):
            fock = int(rng.choice(focks))
            w = int(rng.integers(-2, 3))
            translated_fock, _ = translate_fock_by_two(n_sites, fock)
            old_fields = w + np.cumsum(charges(n_sites, fock))
            new_w = w + shift(n_sites, fock)
            new_fields = new_w + np.cumsum(charges(n_sites, translated_fock))
            rotated_old_fields = np.roll(old_fields, 2)
            worst = max(worst, float(np.max(np.abs(new_fields - rotated_old_fields))))
        worst_by_name[name] = worst
    best = min(worst_by_name, key=worst_by_name.get)
    return best, worst_by_name[best]


def check_01(rng: np.random.Generator) -> tuple[bool, str]:
    best_rule, electric_field_error = check_magnetic_translation_rule(8, rng)
    worst_comm = 0.0
    worst_q_comm = 0.0
    worst_electric = 0.0
    for n_sites in (8, 12):
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

                coo = hamiltonian.tocoo()
                charges_by_index = np.empty(basis.dim, dtype=np.int64)
                for idx in range(basis.dim):
                    _, fock, _ = basis.unpack(idx)
                    charges_by_index[idx] = fock_charge(n_sites, fock)
                if coo.nnz:
                    q_delta = charges_by_index[coo.row] - charges_by_index[coo.col]
                    worst_q_comm = max(worst_q_comm, float(np.max(np.abs(q_delta * coo.data))))

                for _ in range(20):
                    local_f = int(rng.integers(0, len(basis.focks)))
                    fock = int(basis.focks[local_f])
                    w_index = int(rng.integers(0, basis.n_w))
                    w = basis.w_value(w_index)
                    exact_sum = electric_integer_sum(n_sites, fock, w)
                    q = charges(n_sites, fock)
                    direct_sum = int(np.dot(w + np.cumsum(q), w + np.cumsum(q)))
                    worst_electric = max(worst_electric, abs(exact_sum - direct_sum))

    passed = (
        best_rule == "tail"
        and electric_field_error <= CHECK_TOL
        and worst_comm <= CHECK_TOL
        and worst_q_comm <= CHECK_TOL
        and worst_electric <= CHECK_TOL
    )
    detail = (
        f"rule={best_rule}, field={electric_field_error:.1e}, "
        f"comm={worst_comm:.1e}, Q={worst_q_comm:.1e}, E={worst_electric:.1e}"
    )
    return passed, detail


def free_one_body_matrix(n_sites: int, mass: float) -> np.ndarray:
    h = np.zeros((n_sites, n_sites), dtype=np.complex128)
    for n in range(n_sites):
        h[n, n] += mass * (1 if n % 2 == 0 else -1)
        right = (n + 1) % n_sites
        h[n, right] += -0.5j
        h[right, n] += 0.5j
    return h


def analytic_cell_band(n_sites: int, mass: float) -> np.ndarray:
    n_cells = n_sites // 2
    cell_momenta = 2.0 * np.pi * np.arange(n_cells) / n_cells
    return np.sqrt(mass * mass + np.sin(0.5 * cell_momenta) ** 2)


def free_particle_hole_gaps(n_sites: int, mass: float) -> np.ndarray:
    band = analytic_cell_band(n_sites, mass)
    n_cells = n_sites // 2
    gaps = np.empty(n_cells, dtype=np.float64)
    for p_index in range(n_cells):
        gaps[p_index] = min(band[(k + p_index) % n_cells] + band[k] for k in range(n_cells))
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


def check_02() -> tuple[bool, str, dict[tuple[int, float], np.ndarray]]:
    ph_cache: dict[tuple[int, float], np.ndarray] = {}
    worst_band = 0.0
    worst_many_body_gap = 0.0
    for n_sites in (8, 12):
        n_cells = n_sites // 2
        for mass in (0.3, 0.6):
            one_body = free_one_body_matrix(n_sites, mass)
            one_body_eigs = np.sort(sla.eigvalsh(one_body).real)
            band = analytic_cell_band(n_sites, mass)
            expected = np.sort(np.concatenate([-band, band]))
            worst_band = max(worst_band, float(np.max(np.abs(one_body_eigs - expected))))

            ph = free_particle_hole_gaps(n_sites, mass)
            ph_cache[(n_sites, mass)] = ph
            _, hamiltonian, _ = build_free_fermion_hamiltonian(n_sites, mass)
            many_body = lowest_eigvals(hamiltonian, 2)
            many_body_gap = float(many_body[1] - many_body[0])
            worst_many_body_gap = max(
                worst_many_body_gap,
                abs(many_body_gap - float(np.min(ph))),
            )
    passed = worst_band <= DISP_TOL and worst_many_body_gap <= DISP_TOL
    return passed, f"band={worst_band:.1e}, gap={worst_many_body_gap:.1e}", ph_cache


def check_exact_rotor_g0_couples_w() -> bool:
    basis = Basis(n_sites=8, w_max=2, charge_sector=0, rotor=True)
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


def check_03() -> tuple[bool, str]:
    energies: dict[int, np.ndarray] = {}
    for w_max in (2, 3, 4):
        basis = Basis(n_sites=8, w_max=w_max, charge_sector=0, rotor=True)
        hamiltonian = build_many_body_hamiltonian(
            basis,
            0.3,
            1.0,
            boundary_holonomy_shifts_w=True,
        )
        energies[w_max] = lowest_eigvals(hamiltonian, 2)
    diff_23 = energies[2] - energies[3]
    diff_34 = energies[3] - energies[4]
    passed = bool(np.max(np.abs(diff_34)) <= 1.0e-10)
    detail = (
        f"d23=({diff_23[0]:+.2e},{diff_23[1]:+.2e}), "
        f"d34=({diff_34[0]:+.2e},{diff_34[1]:+.2e})"
    )
    return passed, detail


def slater_state_columns(
    fock_basis: Basis,
    one_body_modes: np.ndarray,
    occupied_mode_columns: list[int],
) -> np.ndarray:
    n_particles = len(occupied_mode_columns)
    state = np.zeros(fock_basis.dim, dtype=np.complex128)
    mode_block = one_body_modes[:, occupied_mode_columns]
    for local_f, fock_value in enumerate(fock_basis.focks):
        fock = int(fock_value)
        if fock.bit_count() != n_particles:
            continue
        occupied_sites = [n for n in range(fock_basis.n_sites) if (fock >> n) & 1]
        state[local_f] = np.linalg.det(mode_block[occupied_sites, :])
    return state


def build_t2_free_basis(n_sites: int, mass: float) -> tuple[Basis, np.ndarray, float]:
    fock_basis, _, _ = build_free_fermion_hamiltonian(n_sites, mass)
    one_body = free_one_body_matrix(n_sites, mass)
    eigvals, eigvecs = sla.eigh(one_body)
    order = np.argsort(eigvals.real)
    eigvals = eigvals[order].real
    eigvecs = eigvecs[:, order]
    n_cells = n_sites // 2
    lower = list(range(n_cells))
    upper = list(range(n_cells, n_sites))
    columns: list[np.ndarray] = [slater_state_columns(fock_basis, eigvecs, lower)]
    for hole_position, _hole_mode in enumerate(lower):
        for particle_mode in upper:
            occupied = lower.copy()
            occupied[hole_position] = particle_mode
            columns.append(slater_state_columns(fock_basis, eigvecs, occupied))
    basis_matrix = np.column_stack(columns)
    gram = basis_matrix.conj().T @ basis_matrix
    gram_error = float(np.linalg.norm(gram - np.eye(gram.shape[0]), ord=2))
    if gram_error > 1.0e-10:
        q_matrix, _ = np.linalg.qr(basis_matrix)
        basis_matrix = q_matrix[:, : len(columns)]
    free_ground = float(np.sum(eigvals[:n_cells]))
    return fock_basis, basis_matrix, free_ground


def embed_t2_in_rotor(t2_fermion_basis: Basis, t2_matrix: np.ndarray, rotor_basis: Basis, w_value: int = 0) -> np.ndarray:
    w_index = rotor_basis.w_index_from_value(w_value)
    if w_index is None:
        raise ValueError("requested W value is outside rotor basis")
    embedded = np.zeros((rotor_basis.dim, t2_matrix.shape[1]), dtype=np.complex128)
    for local_f, fock in enumerate(t2_fermion_basis.focks):
        rotor_local = rotor_basis.fock_to_local[int(fock)]
        embedded[rotor_basis.index(rotor_local, w_index), :] = t2_matrix[local_f, :]
    return embedded


def check_06(ph_cache: dict[tuple[int, float], np.ndarray]) -> tuple[bool, str]:
    n_sites = 12
    mass = 0.3
    fock_basis, t2_matrix, _ = build_t2_free_basis(n_sites, mass)
    _, free_hamiltonian, _ = build_free_fermion_hamiltonian(n_sites, mass)
    t2_free_h = t2_matrix.conj().T @ (free_hamiltonian @ t2_matrix)
    t2_free_vals = np.sort(sla.eigvalsh(t2_free_h).real)
    t2_free_gap = float(t2_free_vals[1] - t2_free_vals[0])
    expected_gap = float(np.min(ph_cache[(n_sites, mass)]))
    free_error = abs(t2_free_gap - expected_gap)

    rotor_basis = Basis(n_sites=n_sites, w_max=4, charge_sector=0, rotor=True)
    t2_rotor = embed_t2_in_rotor(fock_basis, t2_matrix, rotor_basis, 0)
    full_h = build_many_body_hamiltonian(
        rotor_basis,
        mass,
        1.0,
        boundary_holonomy_shifts_w=True,
    )
    t2_h = t2_rotor.conj().T @ (full_h @ t2_rotor)
    t2_vals = np.sort(sla.eigvalsh(t2_h).real)
    t2_gap = float(t2_vals[1] - t2_vals[0])
    full_vals = lowest_eigvals(full_h, 2)
    full_gap = float(full_vals[1] - full_vals[0])
    passed = free_error <= T2_TOL
    detail = f"free_err={free_error:.1e}, g1_gap_T2={t2_gap:.8g}, full={full_gap:.8g}"
    return passed, detail


def main() -> int:
    started = time.time()
    rng = np.random.default_rng(RNG_SEED)
    flags: list[str] = [
        "Q0-ring-Gauss",
        "finite-W-translation-interior",
    ]
    if check_exact_rotor_g0_couples_w():
        flags.append("g0-Uholo-shifts-W")

    check_results: list[tuple[str, bool, str]] = []
    ok01, detail01 = check_01(rng)
    check_results.append(("CHECK-01", ok01, detail01))

    ok02, detail02, ph_cache = check_02()
    check_results.append(("CHECK-02", ok02, detail02))

    ok03, detail03 = check_03()
    check_results.append(("CHECK-03", ok03, detail03))

    ok06, detail06 = check_06(ph_cache)
    check_results.append(("CHECK-06", ok06, detail06))

    passed_all = all(ok for _, ok, _ in check_results)
    elapsed = time.time() - started
    status = "PASS" if passed_all else "FAIL"

    c01_c03 = "; ".join(f"{name}={'ok' if ok else 'FAIL'}({detail})" for name, ok, detail in check_results[:3])

    print(f"CHECKS-1-3 {c01_c03}")
    print(f"CHECK-06 {'ok' if ok06 else 'FAIL'}({detail06})")
    print(f"TOTAL {status} elapsed={elapsed:.2f}s flags={','.join(flags)}")
    return 0 if passed_all else 1


if __name__ == "__main__":
    sys.exit(main())
