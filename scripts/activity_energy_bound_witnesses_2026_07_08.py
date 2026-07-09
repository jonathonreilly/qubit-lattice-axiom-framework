#!/usr/bin/env python3
"""Block01 of the energy-to-records campaign, sourcing-link SUPPORT half.

The rate of local state change is bounded by local interaction energy, so
record formation -- which requires local change to have anything to lock -- is
possible only where energy acts. Witnesses run exactly: stationary eigenstates
have zero activity everywhere despite nonzero energy; empty regions have zero
activity; a moving packet's activity co-moves with its energy. Activity proxies
are declared readout devices for record-formation opportunity; the bridge to
the quantum-Darwinism record premise is a named premise, not derived.

Companion note: ACTIVITY_ENERGY_BOUND_WITNESSES_BOUNDED_NOTE_2026-07-08.md.
No formation rule chosen; no gravity claim; sets no audit status.

Definitions implemented here:
  ACTIVITY a_R := || d rho_R / dt ||_1
    = || Tr_{R^c}(-i [H, rho]) ||_1.
  LOCAL ENERGY SCALE e_R := sum ||h_x|| over Hamiltonian terms h_x whose
    support intersects R.
  LOCAL ENERGY EXPECTATION eps_R := <sum h_x touching R> minus the vacuum
    value where a vacuum reference exists.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import sys
import time

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla


RNG_SEED = 20260708
TRACE_TOL = 1.0e-12
GAUGED_TRACE_TOL = 1.0e-10


def apply_cdag_c(fock: int, create_site: int, annihilate_site: int) -> tuple[int, int] | None:
    if ((fock >> annihilate_site) & 1) == 0:
        return None
    if ((fock >> create_site) & 1) == 1:
        return None
    sign = -1 if ((fock & ((1 << annihilate_site) - 1)).bit_count() & 1) else 1
    after_annihilate = fock ^ (1 << annihilate_site)
    if (after_annihilate & ((1 << create_site) - 1)).bit_count() & 1:
        sign = -sign
    return after_annihilate | (1 << create_site), sign


def normalize(vector: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(vector)
    if norm == 0.0:
        raise RuntimeError("zero vector cannot be normalized")
    return np.asarray(vector, dtype=np.complex128) / norm


def centroid(weights: np.ndarray) -> float:
    w = np.asarray(weights, dtype=np.float64)
    total = float(np.sum(w))
    if total <= 0.0:
        return float("nan")
    return float(np.dot(np.arange(w.size, dtype=np.float64), w) / total)


def bhattacharyya_overlap(left: np.ndarray, right: np.ndarray) -> float:
    x = np.asarray(left, dtype=np.float64)
    y = np.asarray(right, dtype=np.float64)
    sx = float(np.sum(x))
    sy = float(np.sum(y))
    if sx <= 0.0 and sy <= 0.0:
        return 1.0
    if sx <= 0.0 or sy <= 0.0:
        return 0.0
    return float(np.sum(np.sqrt((x / sx) * (y / sy))))


def threshold_support(values: np.ndarray, relative_threshold: float = 1.0e-3) -> np.ndarray:
    profile = np.asarray(values, dtype=np.float64)
    peak = float(np.max(profile)) if profile.size else 0.0
    if peak <= 0.0:
        return np.array([], dtype=np.int64)
    return np.flatnonzero(profile > relative_threshold * peak)


def support_contained_in_broadened(
    activity: np.ndarray,
    energy: np.ndarray,
    *,
    broaden_by: int = 2,
    periodic: bool = False,
) -> bool:
    active = threshold_support(activity)
    energetic = threshold_support(energy)
    if active.size == 0:
        return True
    if energetic.size == 0:
        return False
    n = int(np.asarray(activity).size)
    for bond in active:
        distances = np.abs(energetic - bond)
        if periodic:
            distances = np.minimum(distances, n - distances)
        if int(np.min(distances)) > broaden_by:
            return False
    return True


def active_span(values: np.ndarray, threshold: float) -> str:
    active = np.flatnonzero(np.asarray(values) > threshold)
    if active.size == 0:
        return "none"
    return f"{int(active[0])}-{int(active[-1])}"


@dataclass
class FreeChain:
    n_sites: int
    mass: float
    n_particles: int
    basis: np.ndarray
    fock_to_index: dict[int, int]
    hamiltonian: sp.csr_matrix
    occupations: np.ndarray
    bond_terms: list[sp.csr_matrix]
    local_energy_scale: np.ndarray

    @classmethod
    def build(cls, n_sites: int, mass: float, n_particles: int) -> "FreeChain":
        focks = np.array(
            [sum(1 << x for x in sites) for sites in itertools.combinations(range(n_sites), n_particles)],
            dtype=np.int64,
        )
        fock_to_index = {int(f): i for i, f in enumerate(focks)}
        rows: list[int] = []
        cols: list[int] = []
        data: list[complex] = []
        bond_rows: list[list[int]] = [[] for _ in range(n_sites - 1)]
        bond_cols: list[list[int]] = [[] for _ in range(n_sites - 1)]
        bond_data: list[list[complex]] = [[] for _ in range(n_sites - 1)]

        for col, fock_value in enumerate(focks):
            fock = int(fock_value)
            diagonal = sum(mass * (1 if x % 2 == 0 else -1) * ((fock >> x) & 1) for x in range(n_sites))
            rows.append(col)
            cols.append(col)
            data.append(diagonal)
            for x in range(n_sites - 1):
                y = x + 1
                for create_site, annihilate_site in ((x, y), (y, x)):
                    applied = apply_cdag_c(fock, create_site, annihilate_site)
                    if applied is None:
                        continue
                    new_fock, sign = applied
                    row = fock_to_index[new_fock]
                    value = -0.5 * sign
                    rows.append(row)
                    cols.append(col)
                    data.append(value)
                    bond_rows[x].append(row)
                    bond_cols[x].append(col)
                    bond_data[x].append(value)

        dim = len(focks)
        hamiltonian = sp.coo_matrix((data, (rows, cols)), shape=(dim, dim), dtype=np.complex128).tocsr()
        occupations = np.array([[(int(f) >> x) & 1 for f in focks] for x in range(n_sites)], dtype=np.float64)
        bond_terms = [
            sp.coo_matrix((bond_data[x], (bond_rows[x], bond_cols[x])), shape=(dim, dim), dtype=np.complex128).tocsr()
            for x in range(n_sites - 1)
        ]
        local_energy_scale = np.array(
            [abs(mass) + 0.5 * (x > 0) + 0.5 * (x < n_sites - 1) for x in range(n_sites)],
            dtype=np.float64,
        )
        return cls(
            n_sites=n_sites,
            mass=mass,
            n_particles=n_particles,
            basis=focks,
            fock_to_index=fock_to_index,
            hamiltonian=hamiltonian,
            occupations=occupations,
            bond_terms=bond_terms,
            local_energy_scale=local_energy_scale,
        )

    def site_activities(self, psi: np.ndarray) -> np.ndarray:
        hpsi = self.hamiltonian @ psi
        dn_dt = np.array(
            [2.0 * np.imag(np.vdot(self.occupations[x] * psi, hpsi)) for x in range(self.n_sites)],
            dtype=np.float64,
        )
        # Fixed-number states have diagonal one-site reductions:
        # rho_x = diag(1 - <n_x>, <n_x>), hence ||d rho_x/dt||_1 = 2 |d<n_x>/dt|.
        return 2.0 * np.abs(dn_dt)

    def local_energy_expectation(self, psi: np.ndarray) -> np.ndarray:
        probabilities = np.abs(psi) ** 2
        out = np.array(
            [
                self.mass * (1 if x % 2 == 0 else -1) * float(np.dot(probabilities, self.occupations[x]))
                for x in range(self.n_sites)
            ],
            dtype=np.float64,
        )
        for x, bond in enumerate(self.bond_terms):
            bond_exp = float(np.vdot(psi, bond @ psi).real)
            out[x] += bond_exp
            out[x + 1] += bond_exp
        return out

    def basis_vector(self, fock: int) -> np.ndarray:
        vector = np.zeros(self.hamiltonian.shape[0], dtype=np.complex128)
        vector[self.fock_to_index[fock]] = 1.0
        return vector


def check_free_bound(chain: FreeChain, rng: np.random.Generator) -> tuple[bool, float]:
    max_ratio = 0.0
    ok = True
    for _ in range(20):
        psi = normalize(rng.normal(size=chain.hamiltonian.shape[0]) + 1.0j * rng.normal(size=chain.hamiltonian.shape[0]))
        activity = chain.site_activities(psi)
        bound = 2.0 * chain.local_energy_scale
        max_ratio = max(max_ratio, float(np.max(activity / bound)))
        ok = ok and bool(np.all(activity <= bound + 5.0e-13))
    # Bound reason: in Tr_{R^c}[-i[H,rho]], terms disjoint from R vanish under
    # the partial trace/cyclicity. Each touching term contributes at most
    # ||[h_x,rho]||_1 <= 2 ||h_x|| ||rho||_1 = 2 ||h_x||, then triangle sums.
    return ok, max_ratio


def check_free_eigenstates(chain: FreeChain) -> tuple[bool, float, float]:
    low_vals, low_vecs = spla.eigsh(chain.hamiltonian, k=2, which="SA", tol=1.0e-13, ncv=40, maxiter=10000)
    mid_vals, mid_vecs = spla.eigsh(chain.hamiltonian, k=1, sigma=0.0, which="LM", tol=1.0e-13, ncv=40, maxiter=10000)
    high_vals, high_vecs = spla.eigsh(chain.hamiltonian, k=2, which="LA", tol=1.0e-13, ncv=40, maxiter=10000)
    del low_vals, mid_vals, high_vals

    vectors = [low_vecs[:, 0], low_vecs[:, 1], mid_vecs[:, 0], high_vecs[:, 0], high_vecs[:, 1]]
    max_activity = 0.0
    min_abs_energy = float("inf")
    for vec in vectors:
        psi = normalize(vec)
        max_activity = max(max_activity, float(np.max(chain.site_activities(psi))))
        min_abs_energy = min(min_abs_energy, float(np.min(np.abs(chain.local_energy_expectation(psi)))))
    return max_activity <= TRACE_TOL and min_abs_energy > 1.0e-9, max_activity, min_abs_energy


def check_empty_region(chain: FreeChain) -> tuple[bool, float, str]:
    left_fock = sum(1 << x for x in range(chain.n_particles))
    psi0 = chain.basis_vector(left_fock)
    activity0 = chain.site_activities(psi0)
    far_right = np.arange(chain.n_particles + 1, chain.n_sites)
    far_right_max = float(np.max(activity0[far_right]))
    spans: list[str] = []
    for t in (0.0, 0.5, 1.0, 2.0):
        psi_t = psi0 if t == 0.0 else spla.expm_multiply((-1.0j * t) * chain.hamiltonian, psi0)
        spans.append(f"{t:g}:{active_span(chain.site_activities(psi_t), 1.0e-8)}")
    return far_right_max <= TRACE_TOL, far_right_max, ",".join(spans)


def one_body_hamiltonian(n_sites: int, mass: float) -> np.ndarray:
    h = np.zeros((n_sites, n_sites), dtype=np.complex128)
    for x in range(n_sites):
        h[x, x] = mass * (1 if x % 2 == 0 else -1)
    for x in range(n_sites - 1):
        h[x, x + 1] = -0.5
        h[x + 1, x] = -0.5
    return h


def packet_bond_activity(psi: np.ndarray, h: np.ndarray) -> np.ndarray:
    dpsi_dt = -1.0j * (h @ psi)
    activity = np.empty(psi.size - 1, dtype=np.float64)
    for x in range(psi.size - 1):
        y = x + 1
        # In the one-particle sector, tracing out the rest of the chain gives
        # rho_b=(1-|psi_x|^2-|psi_y|^2)|00><00| + |v><v| on
        # span{00,10,01}, where v=psi_x|10>+psi_y|01>; the |10><01|
        # coherence is psi_x psi_y*. Differentiating this formula with
        # dpsi/dt=-i h psi gives the exact bond activity, with no finite
        # differences.
        dpx_dt = 2.0 * float(np.real(np.conj(psi[x]) * dpsi_dt[x]))
        dpy_dt = 2.0 * float(np.real(np.conj(psi[y]) * dpsi_dt[y]))
        dcoh_dt = dpsi_dt[x] * np.conj(psi[y]) + psi[x] * np.conj(dpsi_dt[y])
        drho = np.zeros((4, 4), dtype=np.complex128)
        drho[0, 0] = -(dpx_dt + dpy_dt)
        drho[1, 1] = dpx_dt
        drho[2, 2] = dpy_dt
        drho[1, 2] = dcoh_dt
        drho[2, 1] = np.conj(dcoh_dt)
        activity[x] = float(np.sum(np.abs(np.linalg.eigvalsh(drho))))
    return activity


def packet_bond_energy_density(psi: np.ndarray, mass: float) -> np.ndarray:
    n_sites = psi.size
    density = np.abs(psi) ** 2
    site_mass = mass * np.where(np.arange(n_sites) % 2 == 0, 1.0, -1.0) * density
    degrees = np.ones(n_sites, dtype=np.float64)
    if n_sites > 2:
        degrees[1:-1] = 2.0
    eps = np.empty(n_sites - 1, dtype=np.float64)
    for x in range(n_sites - 1):
        y = x + 1
        hopping = float((-0.5 * (np.conj(psi[x]) * psi[y] + np.conj(psi[y]) * psi[x])).real)
        eps[x] = site_mass[x] / degrees[x] + site_mass[y] / degrees[y] + hopping
    return eps


def check_packet() -> tuple[bool, bool, float, float, list[float], list[float]]:
    n_sites = 40
    mass = 0.3
    h = one_body_hamiltonian(n_sites, mass)
    eigvals, eigvecs = sla.eigh(h)
    xs = np.arange(n_sites, dtype=np.float64)
    psi0 = np.exp(-0.5 * ((xs - 12.0) / 3.0) ** 2) * np.exp(1.0j * (np.pi / 4.0) * xs)
    psi0 = normalize(psi0)

    support_ok = True
    overlaps: list[float] = []
    centroid_deltas: list[float] = []
    for t in (0.0, 5.0, 10.0, 15.0):
        psi = eigvecs @ (np.exp(-1.0j * eigvals * t) * (eigvecs.conj().T @ psi0))
        activity = packet_bond_activity(psi, h)
        energy = np.abs(packet_bond_energy_density(psi, mass))
        support_ok = support_ok and support_contained_in_broadened(activity, energy, broaden_by=2)
        overlaps.append(bhattacharyya_overlap(activity, energy))
        centroid_deltas.append(abs(centroid(activity) - centroid(energy)))

    min_overlap = float(np.min(overlaps))
    max_centroid_delta = float(np.max(centroid_deltas))
    return (
        support_ok and min_overlap >= 0.6 and max_centroid_delta <= 2.0,
        support_ok,
        min_overlap,
        max_centroid_delta,
        overlaps,
        centroid_deltas,
    )


@dataclass(frozen=True)
class BondTraceGroups:
    indices: list[np.ndarray]
    local_indices: list[np.ndarray]


def gauged_local_arrays(engine: object, basis: object, mass: float, coupling: float) -> tuple[np.ndarray, np.ndarray]:
    n_sites = basis.n_sites
    occupations = np.empty((n_sites, basis.dim), dtype=np.float64)
    diagonal_bond_energy = np.empty((n_sites, basis.dim), dtype=np.float64)
    for idx in range(basis.dim):
        _, fock_value, w_index = basis.unpack(idx)
        fock = int(fock_value)
        w_value = basis.w_value(w_index)
        q = engine.charges(n_sites, fock)
        fields = w_value + np.cumsum(q)
        mass_terms = np.empty(n_sites, dtype=np.float64)
        for x in range(n_sites):
            occupied = (fock >> x) & 1
            occupations[x, idx] = occupied
            mass_terms[x] = mass * (1 if x % 2 == 0 else -1) * occupied
        for x in range(n_sites):
            right = (x + 1) % n_sites
            diagonal_bond_energy[x, idx] = (
                0.5 * mass_terms[x]
                + 0.5 * mass_terms[right]
                + 0.5 * coupling * coupling * fields[x] ** 2
            )
    return occupations, diagonal_bond_energy


def gauged_hopping_terms(engine: object, basis: object) -> list[sp.csr_matrix]:
    terms: list[sp.csr_matrix] = []
    n_sites = basis.n_sites
    for link in range(n_sites):
        rows: list[int] = []
        cols: list[int] = []
        data: list[complex] = []
        right = (link + 1) % n_sites
        is_boundary = link == n_sites - 1
        delta_w_forward = 1 if (basis.rotor and is_boundary) else 0
        delta_w_backward = -delta_w_forward
        for local_f, fock_value in enumerate(basis.focks):
            fock = int(fock_value)
            forward = engine.apply_cdag_c(fock, link, right)
            if forward is not None:
                new_fock, fermion_sign = forward
                new_local = basis.fock_to_local.get(new_fock)
                if new_local is not None:
                    for w_index in range(basis.n_w):
                        new_w_index = basis.w_index_from_value(basis.w_value(w_index) + delta_w_forward)
                        if new_w_index is not None:
                            rows.append(basis.index(new_local, new_w_index))
                            cols.append(basis.index(local_f, w_index))
                            data.append((-0.5j) * fermion_sign)
            backward = engine.apply_cdag_c(fock, right, link)
            if backward is not None:
                new_fock, fermion_sign = backward
                new_local = basis.fock_to_local.get(new_fock)
                if new_local is not None:
                    for w_index in range(basis.n_w):
                        new_w_index = basis.w_index_from_value(basis.w_value(w_index) + delta_w_backward)
                        if new_w_index is not None:
                            rows.append(basis.index(new_local, new_w_index))
                            cols.append(basis.index(local_f, w_index))
                            data.append((0.5j) * fermion_sign)
        terms.append(
            sp.coo_matrix((data, (rows, cols)), shape=(basis.dim, basis.dim), dtype=np.complex128).tocsr()
        )
    return terms


def build_bond_trace_groups(basis: object, bond: int) -> BondTraceGroups:
    x = bond
    y = (bond + 1) % basis.n_sites
    clear_mask = ~((1 << x) | (1 << y))
    groups: dict[tuple[int, int], tuple[list[int], list[int]]] = {}
    for idx in range(basis.dim):
        _, fock_value, w_index = basis.unpack(idx)
        fock = int(fock_value)
        local_index = ((fock >> x) & 1) + 2 * ((fock >> y) & 1)
        key = (fock & clear_mask, int(w_index))
        if key not in groups:
            groups[key] = ([], [])
        groups[key][0].append(idx)
        groups[key][1].append(local_index)
    return BondTraceGroups(
        indices=[np.array(value[0], dtype=np.int64) for value in groups.values()],
        local_indices=[np.array(value[1], dtype=np.int64) for value in groups.values()],
    )


def reduced_outer(left: np.ndarray, right: np.ndarray, groups: BondTraceGroups) -> np.ndarray:
    out = np.zeros((4, 4), dtype=np.complex128)
    for indices, local_indices in zip(groups.indices, groups.local_indices):
        left_local = np.zeros(4, dtype=np.complex128)
        right_local = np.zeros(4, dtype=np.complex128)
        left_local[local_indices] = left[indices]
        right_local[local_indices] = right[indices]
        out += np.outer(left_local, np.conj(right_local))
    return out


def reduced_density(vector: np.ndarray, groups: BondTraceGroups) -> np.ndarray:
    rho = reduced_outer(vector, vector, groups)
    return 0.5 * (rho + rho.conj().T)


def gauged_bond_activities(
    psi: np.ndarray,
    hamiltonian: sp.csr_matrix,
    trace_groups: list[BondTraceGroups],
) -> np.ndarray:
    hpsi = hamiltonian @ psi
    dpsi_dt = -1.0j * hpsi
    activity = np.empty(len(trace_groups), dtype=np.float64)
    for bond, groups in enumerate(trace_groups):
        drho = reduced_outer(dpsi_dt, psi, groups) + reduced_outer(psi, dpsi_dt, groups)
        drho = 0.5 * (drho + drho.conj().T)
        activity[bond] = float(np.sum(np.abs(np.linalg.eigvalsh(drho))))
    return activity


def gauged_bond_energy_expectation(
    psi: np.ndarray,
    diagonal_bond_energy: np.ndarray,
    hopping_terms: list[sp.csr_matrix],
) -> np.ndarray:
    probabilities = np.abs(psi) ** 2
    out = diagonal_bond_energy @ probabilities
    for bond, hopping in enumerate(hopping_terms):
        out[bond] += float(np.vdot(psi, hopping @ psi).real)
    return np.asarray(out, dtype=np.float64)


def circular_site_distance(site: int, origin: int, n_sites: int) -> int:
    direct = abs(site - origin)
    return min(direct, n_sites - direct)


def periodic_bond_distances(n_sites: int, origin: int) -> np.ndarray:
    distances = np.empty(n_sites, dtype=np.float64)
    for bond in range(n_sites):
        right = (bond + 1) % n_sites
        distances[bond] = min(
            circular_site_distance(bond, origin, n_sites),
            circular_site_distance(right, origin, n_sites),
        )
    return distances


def check_gauged() -> tuple[bool, bool, float, float, float, float, float, dict[str, bool]]:
    old_dont_write_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        import gauged_schwinger_staggered_ed_engine_2026_07_08 as engine
    finally:
        sys.dont_write_bytecode = old_dont_write_bytecode

    n_sites = 12
    mass = 1.0
    coupling = 0.6
    x0 = 0
    basis = engine.Basis(n_sites=n_sites, w_max=4, charge_sector=0, rotor=True)
    hamiltonian = engine.build_many_body_hamiltonian(
        basis,
        mass,
        coupling,
        boundary_holonomy_shifts_w=True,
    ).tocsr()
    vals, vecs = spla.eigsh(hamiltonian, k=1, which="SA", tol=1.0e-11, ncv=32, maxiter=8000)
    del vals
    gs = normalize(vecs[:, 0])
    occupations, diagonal_bond_energy = gauged_local_arrays(engine, basis, mass, coupling)
    hopping_terms = gauged_hopping_terms(engine, basis)
    trace_groups = [build_bond_trace_groups(basis, bond) for bond in range(n_sites)]
    distances = periodic_bond_distances(n_sites, x0)

    psi0 = np.exp(1.0j * 0.7 * occupations[x0]) * gs
    gs_energy = gauged_bond_energy_expectation(gs, diagonal_bond_energy, hopping_terms)

    max_initial_distance = 0.0
    check_05a_ok = True
    for bond, groups in enumerate(trace_groups):
        if distances[bond] <= 1.0:
            continue
        delta = reduced_density(psi0, groups) - reduced_density(gs, groups)
        distance = float(np.sum(np.abs(np.linalg.eigvalsh(0.5 * (delta + delta.conj().T)))))
        max_initial_distance = max(max_initial_distance, distance)
        check_05a_ok = check_05a_ok and distance <= 1.0e-12

    support_ok = True
    overlaps: list[float] = []
    max_active_distance = 0.0
    measured_front_speed = 0.0
    lightcone_ok = True
    for t in (0.5, 1.0, 2.0):
        psi_t = spla.expm_multiply((-1.0j * t) * hamiltonian, psi0)
        activity = gauged_bond_activities(psi_t, hamiltonian, trace_groups)
        eps = np.abs(gauged_bond_energy_expectation(psi_t, diagonal_bond_energy, hopping_terms) - gs_energy)
        support_ok = support_ok and support_contained_in_broadened(
            activity,
            eps,
            broaden_by=2,
            periodic=True,
        )
        overlaps.append(bhattacharyya_overlap(activity, eps))
        active = threshold_support(activity)
        if active.size:
            max_dist_t = float(np.max(distances[active]))
            max_active_distance = max(max_active_distance, max_dist_t)
            measured_front_speed = max(measured_front_speed, max(0.0, (max_dist_t - 1.0) / t))
            lightcone_ok = lightcone_ok and bool(np.all(distances[active] <= 1.0 + 3.0 * t + 1.0e-12))

    min_overlap = float(np.min(overlaps))
    gs_activity = gauged_bond_activities(gs, hamiltonian, trace_groups)
    stationary_ok = bool(np.max(gs_activity) <= GAUGED_TRACE_TOL)
    gates = {
        "CHECK-05a-unitary-locality": check_05a_ok,
        "CHECK-05-support": support_ok,
        "CHECK-05-overlap": min_overlap >= 0.5,
        "CHECK-05-lightcone": lightcone_ok,
        "CHECK-06-stationary": stationary_ok,
    }
    return (
        all(gates.values()),
        support_ok,
        min_overlap,
        max_initial_distance,
        max_active_distance,
        measured_front_speed,
        float(np.max(gs_activity)),
        gates,
    )


def run() -> tuple[list[str], int]:
    started = time.time()
    rng = np.random.default_rng(RNG_SEED)
    chain = FreeChain.build(n_sites=14, mass=0.3, n_particles=7)

    bound_ok, max_ratio = check_free_bound(chain, rng)
    eigen_ok, eigen_activity, eigen_energy_min = check_free_eigenstates(chain)
    empty_ok, empty_far_max, spread = check_empty_region(chain)
    packet_ok, packet_support_ok, packet_overlap_min, packet_centroid_max, packet_overlaps, packet_centroids = check_packet()
    (
        gauged_ok,
        gauged_support_ok,
        gauged_overlap_min,
        gauged_locality_max,
        gauged_max_dist,
        gauged_front_speed,
        gauged_gs_activity,
        gauged_gates,
    ) = check_gauged()
    del gauged_ok, gauged_support_ok

    checks = {
        "CHECK-01-bound": bound_ok,
        "CHECK-02-eigen": eigen_ok,
        "CHECK-03-empty": empty_ok,
        "CHECK-04-packet-support": packet_support_ok,
        "CHECK-04-packet-overlap": packet_overlap_min >= 0.6,
        "CHECK-04-packet-centroid": packet_centroid_max <= 2.0,
        **gauged_gates,
    }
    failed = [name for name, ok in checks.items() if not ok]
    verdict = "SUPPORT-HALF-ESTABLISHED" if not failed else "SUPPORT-HALF-FAILED"
    exit_code = 0 if not failed else 1
    elapsed = time.time() - started

    lines = [
        f"BOUND CHECK-01={'ok' if bound_ok else 'FAIL'} max_ratio={max_ratio:.6g}",
        (
            "WITNESSES "
            f"CHECK-02={'ok' if eigen_ok else 'FAIL'} max_a={eigen_activity:.3e} min_abs_eps={eigen_energy_min:.3e} "
            f"remark=stationary-worlds-form-no-records; "
            f"CHECK-03={'ok' if empty_ok else 'FAIL'} far_right_t0={empty_far_max:.3e} spread={spread}"
        ),
        (
            "PACKET "
            f"CHECK-04={'ok' if packet_ok else 'FAIL'} support={'ok' if packet_support_ok else 'FAIL'} "
            f"overlap_min={packet_overlap_min:.6g} "
            f"centroid_delta_max={packet_centroid_max:.6g} "
            f"overlaps={[round(x, 4) for x in packet_overlaps]} centroids={[round(x, 4) for x in packet_centroids]}"
        ),
        (
            "GAUGED "
            f"CHECK-05a={'ok' if gauged_gates['CHECK-05a-unitary-locality'] else 'FAIL'} "
            f"locality_max={gauged_locality_max:.3e}; "
            f"CHECK-05={'ok' if gauged_gates['CHECK-05-support'] and gauged_gates['CHECK-05-overlap'] and gauged_gates['CHECK-05-lightcone'] else 'FAIL'} "
            f"overlap_min={gauged_overlap_min:.6g} max_active_dist={gauged_max_dist:.3g} front_v={gauged_front_speed:.3g}; "
            f"CHECK-06={'ok' if gauged_gates['CHECK-06-stationary'] else 'FAIL'} gs_max_a={gauged_gs_activity:.3e}"
        ),
        "CHECKS " + ";".join(f"{name}={'ok' if ok else 'FAIL'}" for name, ok in checks.items()),
        (
            f"TOTAL {verdict} gates={'none' if not failed else ','.join(failed)} elapsed={elapsed:.2f}s "
            "flags=SPEC-NOTE:CHECK-01-03-single-site-controls,"
            "packet-two-site-bond-trace-norm,"
            "gauged-unitary-local-kick,"
            "gauged-bond-energy-local-apportioning,"
            "no-formation-rule,no-gravity-claim,no-audit-status"
        ),
    ]
    return lines, exit_code


def main() -> int:
    try:
        lines, exit_code = run()
    except Exception as exc:  # noqa: BLE001 - runner verdict must stay within six stdout lines.
        print(f"TOTAL MACHINERY-FAIL error={type(exc).__name__}:{str(exc)[:180]}")
        return 2
    for line in lines:
        print(line)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
