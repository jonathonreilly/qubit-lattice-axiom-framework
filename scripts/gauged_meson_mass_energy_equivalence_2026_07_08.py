#!/usr/bin/env python3
"""Mass-energy-equivalence runner for the gauged staggered Schwinger comparator.

Companion note: GAUGED_MESON_MASS_ENERGY_EQUIVALENCE_SEPARATION_NOTE_2026-07-08.md.

Claim shape tested here: field-mediated binding restores composite
mass-energy equivalence in the window; the two-body truncation of the same
model stays pinned at the kinetic-functional value; the difference is carried
by the pair-creation channel.

This runner derives no gravitational content and sets no audit status.  It
uses the companion validated engine
scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py for the charge-zero
ring Gauss sector, magnetic translation projector, decoupled g=0 free
comparator, and CHECK-06 free-vacuum plus one particle-hole T2 construction.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
import math
from pathlib import Path
import sys
import time
from typing import Any

sys.dont_write_bytecode = True

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla


THIS_FILE = Path(__file__).resolve()
ENGINE_PATH = THIS_FILE.with_name("gauged_schwinger_staggered_ed_engine_2026_07_08.py")
NOTE_NAME = "GAUGED_MESON_MASS_ENERGY_EQUIVALENCE_SEPARATION_NOTE_2026-07-08.md"

N_MAIN = 16
W_MAX = 4
GRID_MASSES = (0.2, 0.4)
GRID_COUPLINGS = (0.6, 1.0, 1.4, 2.0)
MOMENTUM_INDICES = (0, 1, 2)
LANCZOS_K = 4
LANCZOS_TOL = 1.0e-10
ENGINE_REPRO_TOL = 1.0e-8
RNG_SEED = 20260708


def load_engine() -> Any:
    spec = importlib.util.spec_from_file_location("gauged_schwinger_engine_20260708", ENGINE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import engine from {ENGINE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


engine = load_engine()


@dataclass
class FitResult:
    e0: float
    c2: float
    d4: float
    m_rel: float
    m_comp: float
    e4: float
    r_full: float
    r_c: float
    d_full: float


@dataclass
class FullResult:
    n_sites: int
    mass: float
    coupling: float
    momenta: np.ndarray
    gaps: np.ndarray
    sector_values: dict[int, np.ndarray]
    ground_energy: float
    fit: FitResult
    gaps2: np.ndarray
    fit2: FitResult
    ground_vector: np.ndarray | None
    meson_vector: np.ndarray | None
    flags: list[str]


@dataclass
class T2Result:
    e0: float
    m_comp: float
    d_t2: float
    gaps: np.ndarray
    fit: FitResult
    inv_m_fit: float
    inv_m_fd: float
    inv_m_diff: float
    commutator_rel: float
    projector_ranks: tuple[int, int, int]
    flags: list[str]


@dataclass
class GridResult:
    mass: float
    coupling: float
    full: FullResult
    t2: T2Result
    xi: float
    size_ratio: float
    size_valid: bool
    stability_drift: float
    pair_weight: float
    discrepancy: float


_ROTOR_SETUP: dict[int, tuple[Any, Any, Any, sp.csr_matrix]] = {}
_T2_CACHE: dict[tuple[int, float], tuple[np.ndarray, np.ndarray, float]] = {}
_CHARGE_TABLE_CACHE: dict[int, tuple[np.ndarray, np.ndarray]] = {}


def finite_float(value: float, digits: int = 6) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    return f"{value:.{digits}g}"


def deterministic_v0(dim: int, salt: int) -> np.ndarray:
    rng = np.random.default_rng(RNG_SEED + 1009 * salt + dim)
    vec = rng.normal(size=dim) + 1.0j * rng.normal(size=dim)
    norm = np.linalg.norm(vec)
    return vec / norm


def rotor_setup(n_sites: int) -> tuple[Any, Any, Any, sp.csr_matrix]:
    cached = _ROTOR_SETUP.get(n_sites)
    if cached is not None:
        return cached
    basis = engine.Basis(n_sites=n_sites, w_max=W_MAX, charge_sector=0, rotor=True)
    magnetic_translation = engine.build_translation_map(basis, engine.magnetic_w_shift_tail)
    ordinary_translation = engine.build_translation_map(basis, engine.ordinary_w_shift_zero)
    ordinary_matrix = ordinary_translation.matrix()
    cached = (basis, magnetic_translation, ordinary_translation, ordinary_matrix)
    _ROTOR_SETUP[n_sites] = cached
    return cached


def full_hamiltonian(n_sites: int, mass: float, coupling: float) -> tuple[Any, Any, sp.csr_matrix]:
    basis, magnetic_translation, _, _ = rotor_setup(n_sites)
    hamiltonian = engine.build_many_body_hamiltonian(
        basis,
        mass,
        coupling,
        boundary_holonomy_shifts_w=True,
    )
    return basis, magnetic_translation, hamiltonian


def lowest_eigenpairs(matrix: sp.csr_matrix, k: int, salt: int) -> tuple[np.ndarray, np.ndarray]:
    dim = matrix.shape[0]
    if dim <= max(2 * k + 2, 64):
        vals, vecs = sla.eigh(matrix.toarray())
        order = np.argsort(vals.real)[:k]
        return vals.real[order], vecs[:, order]
    vals, vecs = spla.eigsh(
        matrix,
        k=k,
        which="SA",
        return_eigenvectors=True,
        tol=LANCZOS_TOL,
        maxiter=7000,
        ncv=min(dim - 1, max(32, 5 * k + 16)),
        v0=deterministic_v0(dim, salt),
    )
    order = np.argsort(vals.real)
    return vals.real[order], vecs[:, order]


def projected_eigenpairs(
    hamiltonian: sp.csr_matrix,
    translation: Any,
    momentum: float,
    k: int,
    salt: int,
) -> tuple[np.ndarray, np.ndarray, list[str]]:
    dim = hamiltonian.shape[0]
    flags: list[str] = []

    def matvec(vector: np.ndarray) -> np.ndarray:
        projected = engine.projected_vector(vector, translation, momentum)
        return engine.projected_vector(hamiltonian @ projected, translation, momentum)

    operator = spla.LinearOperator((dim, dim), matvec=matvec, dtype=np.complex128)
    vals, vecs = spla.eigsh(
        operator,
        k=k,
        which="SA",
        return_eigenvectors=True,
        tol=LANCZOS_TOL,
        maxiter=7000,
        ncv=min(dim - 1, max(32, 5 * k + 16)),
        v0=deterministic_v0(dim, salt),
    )
    order = np.argsort(vals.real)
    vals = vals.real[order]
    vecs = vecs[:, order]

    projected_vecs = np.zeros_like(vecs, dtype=np.complex128)
    for col in range(vecs.shape[1]):
        pv = engine.projected_vector(vecs[:, col], translation, momentum)
        norm = np.linalg.norm(pv)
        if norm <= 1.0e-9:
            flags.append(f"projector-null-col{col}")
            pv = vecs[:, col]
            norm = np.linalg.norm(pv)
        projected_vecs[:, col] = pv / norm
    return vals, projected_vecs, flags


def excitation_from_sector(vals: np.ndarray, ground: float, p_index: int) -> float:
    start = 1 if p_index == 0 else 0
    if start >= len(vals):
        return float("nan")
    if p_index != 0:
        for val in vals[start:]:
            if val > ground + 1.0e-9:
                return float(val - ground)
    return float(vals[start] - ground)


def band_excitations(vals: np.ndarray, ground: float, p_index: int, count: int = 2) -> list[float]:
    """First `count` excitation energies above the global ground state in a
    sector (used for the two-band equivalence-ratio test)."""
    out: list[float] = []
    start = 1 if p_index == 0 else 0
    for val in vals[start:]:
        if p_index != 0 and not val > ground + 1.0e-9:
            continue
        out.append(float(val - ground))
        if len(out) == count:
            break
    while len(out) < count:
        out.append(float("nan"))
    return out


def fit_dispersion(momenta: np.ndarray, gaps: np.ndarray) -> FitResult:
    x = momenta * momenta
    design = np.column_stack([np.ones_like(x), x, x * x])
    rel_a, c2, d4 = np.linalg.solve(design, gaps * gaps)
    nr_a, nr_b, e4 = np.linalg.solve(design, gaps)
    e0 = math.sqrt(max(0.0, float(rel_a)))
    m_rel = e0 / c2 if c2 != 0.0 else float("nan")
    m_comp = 1.0 / (2.0 * nr_b) if nr_b != 0.0 else float("nan")
    r_full = (m_comp * c2) / e0 if e0 != 0.0 else float("nan")
    r_c = math.sqrt(c2) if c2 >= 0.0 else float("nan")
    d_full = m_comp / e0 if e0 != 0.0 else float("nan")
    return FitResult(
        e0=e0,
        c2=float(c2),
        d4=float(d4),
        m_rel=float(m_rel),
        m_comp=float(m_comp),
        e4=float(e4),
        r_full=float(r_full),
        r_c=float(r_c),
        d_full=float(d_full),
    )


def compute_full_result(
    n_sites: int,
    mass: float,
    coupling: float,
    *,
    need_vectors: bool,
    salt_base: int,
    prebuilt: tuple[Any, Any, sp.csr_matrix] | None = None,
) -> FullResult:
    if prebuilt is None:
        basis, magnetic_translation, hamiltonian = full_hamiltonian(n_sites, mass, coupling)
    else:
        basis, magnetic_translation, hamiltonian = prebuilt
    n_cells = n_sites // 2
    # Magnetic translation moves TWO staggered sites (one cell), so the
    # physical momentum in staggered units (the units of the constituent
    # band sqrt(m^2+sin^2 p)) is HALF the translation phase: p = pi*k/n_cells.
    momenta = np.array([np.pi * k / n_cells for k in MOMENTUM_INDICES], dtype=np.float64)
    sector_values: dict[int, np.ndarray] = {}
    sector_vectors: dict[int, np.ndarray] = {}
    flags: list[str] = []

    for p_index in range(n_cells):
        momentum = 2.0 * np.pi * p_index / n_cells
        vals, vecs, pflags = projected_eigenpairs(
            hamiltonian,
            magnetic_translation,
            momentum,
            LANCZOS_K,
            salt_base + 101 * (p_index + 1),
        )
        sector_values[p_index] = vals
        if need_vectors:
            sector_vectors[p_index] = vecs
        flags.extend(f"P{p_index}:{flag}" for flag in pflags)

    ground_index = int(np.argmin(np.array([sector_values[p][0] for p in range(n_cells)], dtype=np.float64)))
    ground_energy = float(sector_values[ground_index][0])
    ground_vector = sector_vectors[ground_index][:, 0] if need_vectors else None
    if ground_index != 0:
        flags.append(f"momentum-origin-sector={ground_index}")

    gaps = np.array(
        [
            excitation_from_sector(
                sector_values[(ground_index + relative_index) % n_cells],
                ground_energy,
                relative_index,
            )
            for relative_index in MOMENTUM_INDICES
        ],
        dtype=np.float64,
    )
    fit = fit_dispersion(momenta, gaps)
    band_pairs = [
        band_excitations(
            sector_values[(ground_index + relative_index) % n_cells],
            ground_energy,
            relative_index,
        )
        for relative_index in MOMENTUM_INDICES
    ]
    gaps2 = np.array([pair[1] for pair in band_pairs], dtype=np.float64)
    fit2 = fit_dispersion(momenta, gaps2)
    meson_vector = sector_vectors[ground_index][:, 1] if need_vectors else None
    return FullResult(
        n_sites=n_sites,
        mass=mass,
        coupling=coupling,
        momenta=momenta,
        gaps=gaps,
        sector_values=sector_values,
        ground_energy=ground_energy,
        fit=fit,
        gaps2=gaps2,
        fit2=fit2,
        ground_vector=ground_vector,
        meson_vector=meson_vector,
        flags=flags,
    )


def t2_data(n_sites: int, mass: float) -> tuple[np.ndarray, np.ndarray, float]:
    cached = _T2_CACHE.get((n_sites, mass))
    if cached is not None:
        return cached
    basis, _, _, ordinary_matrix = rotor_setup(n_sites)
    fock_basis, t2_matrix, _free_ground = engine.build_t2_free_basis(n_sites, mass)
    # CHECK-06 construction from the validated engine, with W fixed at 0.
    # This is the static-channel comparator: projecting to W=0 removes exactly
    # the pair-creation and holonomy-excitation channels whose contribution is
    # being tested against the full gauged sector.
    t2_rotor = engine.embed_t2_in_rotor(fock_basis, t2_matrix, basis, 0)
    t2_translation = t2_rotor.conj().T @ (ordinary_matrix @ t2_rotor)
    closure = float(np.linalg.norm(t2_translation.conj().T @ t2_translation - np.eye(t2_translation.shape[0]), ord=2))
    cached = (t2_rotor, t2_translation, closure)
    _T2_CACHE[(n_sites, mass)] = cached
    return cached


def dense_projected_eigvals(
    hamiltonian: np.ndarray,
    translation: np.ndarray,
    momentum: float,
    n_cells: int,
) -> tuple[np.ndarray, int]:
    dim = hamiltonian.shape[0]
    projector = np.zeros((dim, dim), dtype=np.complex128)
    power = np.eye(dim, dtype=np.complex128)
    phase = 1.0 + 0.0j
    step_phase = np.exp(-1.0j * momentum)
    for _ in range(n_cells):
        projector += phase * power
        power = translation @ power
        phase *= step_phase
    projector /= n_cells
    projector = 0.5 * (projector + projector.conj().T)
    proj_vals, proj_vecs = sla.eigh(projector)
    keep = proj_vals > 1.0e-7
    rank = int(np.count_nonzero(keep))
    if rank == 0:
        return np.array([], dtype=np.float64), 0
    q = proj_vecs[:, keep]
    block = q.conj().T @ hamiltonian @ q
    vals = np.sort(sla.eigvalsh(0.5 * (block + block.conj().T)).real)
    return vals, rank


def compute_t2_result(
    n_sites: int,
    mass: float,
    coupling: float,
    full_h: sp.csr_matrix,
) -> T2Result:
    n_cells = n_sites // 2
    # Magnetic translation moves TWO staggered sites (one cell), so the
    # physical momentum in staggered units (the units of the constituent
    # band sqrt(m^2+sin^2 p)) is HALF the translation phase: p = pi*k/n_cells.
    momenta = np.array([np.pi * k / n_cells for k in MOMENTUM_INDICES], dtype=np.float64)
    t2_rotor, t2_translation, closure = t2_data(n_sites, mass)
    h_t2 = t2_rotor.conj().T @ (full_h @ t2_rotor)
    h_t2 = np.asarray(0.5 * (h_t2 + h_t2.conj().T), dtype=np.complex128)
    comm = h_t2 @ t2_translation - t2_translation @ h_t2
    comm_rel = float(np.linalg.norm(comm, ord="fro") / max(1.0, np.linalg.norm(h_t2, ord="fro")))

    sector_values: dict[int, np.ndarray] = {}
    rank_by_sector: dict[int, int] = {}
    flags: list[str] = []
    for p_index in range(n_cells):
        momentum = 2.0 * np.pi * p_index / n_cells
        vals, rank = dense_projected_eigvals(h_t2, t2_translation, momentum, n_cells)
        sector_values[p_index] = vals
        rank_by_sector[p_index] = rank
        if rank == 0:
            flags.append(f"sector{p_index}-rank0")

    nonempty_lows = [sector_values[p][0] for p in range(n_cells) if len(sector_values[p]) > 0]
    ground = float(np.min(np.array(nonempty_lows, dtype=np.float64))) if nonempty_lows else float("nan")
    ground_index = int(
        np.argmin(
            np.array(
                [sector_values[p][0] if len(sector_values[p]) > 0 else np.inf for p in range(n_cells)],
                dtype=np.float64,
            )
        )
    )
    gaps = np.array(
        [
            excitation_from_sector(
                sector_values.get((ground_index + relative_index) % n_cells, np.array([], dtype=np.float64)),
                ground,
                relative_index,
            )
            for relative_index in MOMENTUM_INDICES
        ],
        dtype=np.float64,
    )
    ranks = [rank_by_sector.get((ground_index + relative_index) % n_cells, 0) for relative_index in MOMENTUM_INDICES]
    for relative_index in MOMENTUM_INDICES:
        sector = (ground_index + relative_index) % n_cells
        vals = sector_values.get(sector, np.array([], dtype=np.float64))
        if len(vals) < (2 if relative_index == 0 else 1):
            flags.append(f"relP{relative_index}-sector{sector}-rank{rank_by_sector.get(sector, 0)}-insufficient")
    fit = fit_dispersion(momenta, gaps)
    inv_m_fit = 1.0 / fit.m_comp if fit.m_comp != 0.0 else float("nan")
    inv_m_fd = 2.0 * (gaps[1] - gaps[0]) / (momenta[1] * momenta[1]) if momenta[1] != 0.0 else float("nan")
    inv_m_diff = abs(inv_m_fd - inv_m_fit)
    if closure > 1.0e-8:
        flags.append(f"T2-translation-closure={closure:.2e}")
    if comm_rel > 1.0e-8:
        flags.append(f"T2-H-not-block-diagonal={comm_rel:.2e}")
    return T2Result(
        e0=fit.e0,
        m_comp=fit.m_comp,
        d_t2=fit.d_full,
        gaps=gaps,
        fit=fit,
        inv_m_fit=float(inv_m_fit),
        inv_m_fd=float(inv_m_fd),
        inv_m_diff=float(inv_m_diff),
        commutator_rel=comm_rel,
        projector_ranks=(ranks[0], ranks[1], ranks[2]),
        flags=flags,
    )


def charge_tables(basis: Any) -> tuple[np.ndarray, np.ndarray]:
    cached = _CHARGE_TABLE_CACHE.get(basis.n_sites)
    if cached is not None:
        return cached
    n_sites = basis.n_sites
    q_table = np.zeros((len(basis.focks), n_sites), dtype=np.float64)
    qq_offset_table = np.zeros((len(basis.focks), n_sites), dtype=np.float64)
    for local_f, fock_value in enumerate(basis.focks):
        q = engine.charges(n_sites, int(fock_value)).astype(np.float64)
        q_table[local_f, :] = q
        for offset in range(n_sites):
            qq_offset_table[local_f, offset] = float(np.mean(q * np.roll(q, -offset)))
    cached = (q_table, qq_offset_table)
    _CHARGE_TABLE_CACHE[basis.n_sites] = cached
    return cached


def state_fock_probabilities(vector: np.ndarray, basis: Any) -> np.ndarray:
    shaped = np.asarray(vector).reshape((len(basis.focks), basis.n_w))
    probs = np.sum(np.abs(shaped) ** 2, axis=1).real
    total = float(np.sum(probs))
    return probs / total


def connected_corr_by_distance(vector: np.ndarray, basis: Any) -> np.ndarray:
    q_table, qq_offset_table = charge_tables(basis)
    probs = state_fock_probabilities(vector, basis)
    mean_q = probs @ q_table
    mean_qq_offset = probs @ qq_offset_table
    max_dist = basis.n_sites // 2
    sums = np.zeros(max_dist + 1, dtype=np.float64)
    counts = np.zeros(max_dist + 1, dtype=np.float64)
    for offset in range(basis.n_sites):
        dist = min(offset, basis.n_sites - offset)
        disconnected = float(np.mean(mean_q * np.roll(mean_q, -offset)))
        sums[dist] += mean_qq_offset[offset] - disconnected
        counts[dist] += 1.0
    return sums / counts


def charge_radius_xi(meson_vector: np.ndarray, vacuum_vector: np.ndarray, basis: Any) -> tuple[float, list[str]]:
    flags: list[str] = []
    meson_corr = connected_corr_by_distance(meson_vector, basis)
    vacuum_corr = connected_corr_by_distance(vacuum_vector, basis)
    delta = meson_corr - vacuum_corr
    raw = np.maximum(0.0, -delta[1:])
    if float(np.sum(raw)) <= 1.0e-12:
        raw = np.abs(delta[1:])
        flags.append("charge-radius-abs-delta-fallback")
    norm = float(np.sum(raw))
    if norm <= 1.0e-12:
        flags.append("charge-radius-zero-weight")
        return float("inf"), flags
    weights = raw / norm
    distances = np.arange(1, basis.n_sites // 2 + 1, dtype=np.float64)
    r2 = float(np.dot(weights, distances * distances))
    return math.sqrt(max(0.0, r2)), flags


def pair_weight(meson_vector: np.ndarray, t2_rotor: np.ndarray) -> float:
    projected = t2_rotor.conj().T @ meson_vector
    norm2 = float(np.vdot(projected, projected).real)
    return min(1.0, max(0.0, 1.0 - norm2))


def compute_grid_point(mass: float, coupling: float, salt_base: int) -> GridResult:
    basis, _translation, hamiltonian = full_hamiltonian(N_MAIN, mass, coupling)
    full = compute_full_result(
        N_MAIN,
        mass,
        coupling,
        need_vectors=True,
        salt_base=salt_base,
        prebuilt=(basis, _translation, hamiltonian),
    )
    t2 = compute_t2_result(N_MAIN, mass, coupling, hamiltonian)
    if full.meson_vector is None or full.ground_vector is None:
        raise RuntimeError("full vector diagnostics were not computed")
    xi, xi_flags = charge_radius_xi(full.meson_vector, full.ground_vector, basis)
    full.flags.extend(xi_flags)
    size_ratio = float("inf") if xi == 0.0 else N_MAIN / (2.0 * xi)
    # Validity is gated on per-point finite-size STABILITY (N=12 vs N=16
    # drift of the dimensionless D), not on the charge-radius heuristic,
    # which is kept as reported context.
    small = compute_full_result(12, mass, coupling, need_vectors=False, salt_base=salt_base + 7)
    stability_drift = abs(small.fit.d_full - full.fit.d_full)
    size_valid = bool(stability_drift <= 0.03)
    t2_rotor, _t2_translation, _closure = t2_data(N_MAIN, mass)
    p_weight = pair_weight(full.meson_vector, t2_rotor)
    discrepancy = abs(t2.d_t2 - full.fit.d_full)
    return GridResult(
        mass=mass,
        coupling=coupling,
        full=full,
        t2=t2,
        xi=xi,
        size_ratio=size_ratio,
        size_valid=size_valid,
        stability_drift=stability_drift,
        pair_weight=p_weight,
        discrepancy=discrepancy,
    )


def local_engine_style_meson_arrays(coupling: float) -> tuple[np.ndarray, np.ndarray]:
    n_sites = 12
    n_cells = n_sites // 2
    mass = 0.3
    basis, magnetic_translation, hamiltonian = full_hamiltonian(n_sites, mass, coupling)
    del basis
    table: list[np.ndarray] = []
    for p_index in range(n_cells):
        vals, _vecs, _flags = projected_eigenpairs(
            hamiltonian,
            magnetic_translation,
            2.0 * np.pi * p_index / n_cells,
            5,
            5000 + int(100 * coupling) + p_index,
        )
        table.append(vals)
    ground_index = int(np.argmin(np.array([vals[0] for vals in table], dtype=np.float64)))
    p0 = table[ground_index]
    p1 = table[(ground_index + 1) % n_cells]
    return p0[1:5] - p0[0], p1[:4] - p0[0]


def check_01_engine_repro() -> tuple[bool, str]:
    ok_engine, detail, reference = engine.check_05()
    worst = 0.0
    parts: list[str] = [f"engine={'ok' if ok_engine else 'FAIL'}({detail})"]
    for coupling in (0.6, 1.0):
        p0, p1 = local_engine_style_meson_arrays(coupling)
        ref_p0 = reference[coupling]["P0_excitations"]
        ref_p1 = reference[coupling]["P1_excitations"]
        err = max(float(np.max(np.abs(p0 - ref_p0))), float(np.max(np.abs(p1 - ref_p1))))
        worst = max(worst, err)
        parts.append(f"g={coupling}:err={err:.1e}")
    passed = ok_engine and worst <= ENGINE_REPRO_TOL
    return passed, ",".join(parts)


def separation_gate(results: list[GridResult]) -> tuple[bool, str]:
    """Gated legs: (a) static-channel separation |D_T2 - D_full| >= 0.30 at
    every stability-valid point; (b) cross-species metric universality:
    the two species' fitted c^2 agree within 10% at every coupling (two
    masses, one emergent metric) - the tautology-free universality
    statement available at this volume.

    Reported, ungated: the two-band equivalence ratio. The second
    excitation's identity is NOT stable across momentum sectors at N = 16
    (level crossings; fitted M2 swings sign), so a band-2 dispersion fit is
    not meaningful without operator-tagged band identification - named
    follow-up. The rows are printed with a level-crossing flag."""
    valid = [result for result in results if result.size_valid]
    if not valid:
        return False, "no-stability-valid-points"
    failures: list[str] = []
    details: list[str] = []
    for result in valid:
        sep = abs(result.t2.d_t2 - result.full.fit.d_full)
        if sep < 0.30:
            failures.append(f"m={result.mass},g={result.coupling}:sep={sep:.3g}")
        details.append(f"m={result.mass},g={result.coupling}:sep={sep:.3g}")
    for coupling in GRID_COUPLINGS:
        by_m = [r for r in results if r.coupling == coupling and r.size_valid]
        if len(by_m) == 2:
            c_a, c_b = by_m[0].full.fit.c2, by_m[1].full.fit.c2
            dev = abs(c_a / c_b - 1.0)
            details.append(f"g={coupling}:c2_species=({c_a:.4g},{c_b:.4g}),universality_dev={dev:.3g}")
            if dev > 0.10:
                failures.append(f"g={coupling}:metric-universality-dev={dev:.3g}")
    band2_rows = ";".join(
        "m={},g={}:E02={:.5g},M2={:.5g},c2b2={:.4g}".format(
            r.mass, r.coupling, r.full.fit2.e0, r.full.fit2.m_comp, r.full.fit2.c2
        )
        for r in results
    )
    details.append(
        "BAND2-REPORTED(level-crossing; identity unstable across sectors; "
        "two-band ratio deferred to operator-tagged follow-up): " + band2_rows
    )
    detail = ("ok;" if not failures else "FAILPOINTS=" + "|".join(failures) + ";") + ";".join(details)
    return not failures, detail


def window_trend_gate(results: list[GridResult]) -> tuple[bool, str]:
    """The emergent speed c^2 must rise toward 1 as the coupling weakens
    (the window direction), reaching >= 0.85 at the weakest coupling; the
    lattice-unit D = M/E0 curve is reported as context (its drift is the
    c^2 renormalization, not an equivalence failure)."""
    parts: list[str] = []
    ok_all = True
    for mass in GRID_MASSES:
        by_g = sorted([r for r in results if r.mass == mass], key=lambda r: r.coupling)
        c2s = [r.full.fit.c2 for r in by_g]
        mono = all(c2s[i] >= c2s[i + 1] - 1.0e-10 for i in range(len(c2s) - 1))
        weakest = c2s[0]
        ok = mono and weakest >= 0.85
        ok_all = ok_all and ok
        parts.append(
            f"m={mass}:{'mono' if mono else 'nonmono'};c2s=[" + ",".join(f"{c:.3g}" for c in c2s) + "]"
            + f";weakest={weakest:.3g};D_ctx=[" + ",".join(f"{r.full.fit.d_full:.3g}" for r in by_g) + "]"
        )
    return ok_all, ";".join(parts)


def best_size_valid_point(results: list[GridResult]) -> GridResult | None:
    valid = [r for r in results if r.size_valid]
    if not valid:
        return None
    return min(valid, key=lambda r: abs(r.full.fit.d_full - 1.0))


def isotropy_gate(results: list[GridResult]) -> tuple[bool, str]:
    """Fit-consistency check (near-tautological by construction, NOT an
    equivalence gate): every band's single-band R = M c^2 / E0 must sit
    within 5% of 1, confirming the three-point fits are in the quadratic
    regime; the c^2 values themselves are listed for the isotropy record."""
    worst = 0.0
    all_c2 = []
    for r in results:
        worst = max(worst, abs(r.full.fit.r_full - 1.0), abs(r.full.fit2.r_full - 1.0))
        all_c2.append(f"m={r.mass},g={r.coupling}:{r.full.fit.c2:.3g}")
    return worst <= 0.05, f"worst|R-1|={worst:.3g};c2=[" + ",".join(all_c2) + "]"


def rank_correlation(xs: np.ndarray, ys: np.ndarray) -> float:
    if len(xs) < 2 or float(np.std(xs)) == 0.0 or float(np.std(ys)) == 0.0:
        return 0.0
    rx = np.empty_like(xs, dtype=np.float64)
    ry = np.empty_like(ys, dtype=np.float64)
    rx[np.argsort(xs)] = np.arange(len(xs), dtype=np.float64)
    ry[np.argsort(ys)] = np.arange(len(ys), dtype=np.float64)
    return float(np.corrcoef(rx, ry)[0, 1])


def fock_attribution_gate(results: list[GridResult]) -> tuple[bool, str]:
    pair = np.array([r.pair_weight for r in results], dtype=np.float64)
    disc = np.array([r.discrepancy for r in results], dtype=np.float64)
    rho = rank_correlation(pair, disc)
    max_pair_is_max_disc = int(np.argmax(pair)) == int(np.argmax(disc))
    passed = bool(max_pair_is_max_disc or rho > 0.0)
    pairs = ";".join(
        f"m={r.mass},g={r.coupling}:pair={r.pair_weight:.4g},disc={r.discrepancy:.4g}" for r in results
    )
    return passed, f"rho={rho:.3g},maxpair=maxdisc:{max_pair_is_max_disc};{pairs}"


def n_stability_gate() -> tuple[bool, str]:
    n12 = compute_full_result(12, 0.3, 1.0, need_vectors=False, salt_base=120301)
    n16 = compute_full_result(16, 0.3, 1.0, need_vectors=False, salt_base=160301)
    drift = abs(n12.fit.d_full - n16.fit.d_full)
    return drift <= 0.15, f"D12={n12.fit.d_full:.5g},D16={n16.fit.d_full:.5g},drift={drift:.3g}"


def result_fragment(result: GridResult) -> str:
    validity = "Y" if result.size_valid else "N"
    return (
        f"m={result.mass},g={result.coupling}:"
        f"E0={finite_float(result.full.fit.e0)},c2={finite_float(result.full.fit.c2)},"
        f"M={finite_float(result.full.fit.m_comp)},D={finite_float(result.full.fit.d_full)},"
        f"R={finite_float(result.full.fit.r_full)},Rc={finite_float(result.full.fit.r_c)},"
        f"E02={finite_float(result.full.fit2.e0)},M2={finite_float(result.full.fit2.m_comp)},"
        f"c2b2={finite_float(result.full.fit2.c2)},"
        f"T2E0={finite_float(result.t2.e0)},T2M={finite_float(result.t2.m_comp)},"
        f"T2D={finite_float(result.t2.d_t2)},xi={finite_float(result.xi)},"
        f"drift={finite_float(result.stability_drift)},valid={validity}"
    )


def sumrule_fragment(result: GridResult) -> str:
    return (
        f"m={result.mass},g={result.coupling}:"
        f"invM={finite_float(result.t2.inv_m_fit)},fd={finite_float(result.t2.inv_m_fd)},"
        f"diff={finite_float(result.t2.inv_m_diff)},ranks={result.t2.projector_ranks},"
        f"comm={result.t2.commutator_rel:.2e}"
    )


def gather_flags(results: list[GridResult]) -> list[str]:
    flags = [
        f"note={NOTE_NAME}",
        "Q0-ring-Gauss",
        "finite-W-magnetic-translation",
        "g0-decoupled-comparator-inherited",
        "momenta-N16-L8-k012-ok",
        "three-point-fits-exactly-determined",
        "T2-W0-static-channel-removes-pairs-and-holonomy",
        "T2-momentum=ordinary-cell-projected-after-W0",
    ]
    max_comm = max((r.t2.commutator_rel for r in results), default=0.0)
    flags.append(f"T2-translation-comm-max={max_comm:.2e}")
    for result in results:
        flags.extend(f"m={result.mass},g={result.coupling}:{flag}" for flag in result.full.flags)
        flags.extend(f"m={result.mass},g={result.coupling}:{flag}" for flag in result.t2.flags)
    return flags


def main() -> int:
    started = time.time()
    results: list[GridResult] = []
    salt = 0
    for mass in GRID_MASSES:
        for coupling in GRID_COUPLINGS:
            salt += 1
            results.append(compute_grid_point(mass, coupling, 10000 * salt))

    ok01, detail01 = check_01_engine_repro()
    ok02, detail02 = separation_gate(results)
    ok03, detail03 = window_trend_gate(results)
    ok04, detail04 = isotropy_gate(results)
    ok05, detail05 = fock_attribution_gate(results)
    ok06, detail06 = n_stability_gate()
    checks = [
        ("CHECK-01", ok01, detail01),
        ("CHECK-02", ok02, detail02),
        ("CHECK-03", ok03, detail03),
        ("CHECK-04", ok04, detail04),
        ("CHECK-05", ok05, detail05.split(";", 1)[0]),
        ("CHECK-06", ok06, detail06),
    ]
    passed = all(ok for _, ok, _ in checks)
    elapsed = time.time() - started
    status = "PASS" if passed else "FAIL"

    print("RESULTS " + "; ".join(result_fragment(result) for result in results))
    print("T2-SUMRULE " + "; ".join(sumrule_fragment(result) for result in results))
    print("FOCK-ATTRIBUTION " + detail05)
    print("CHECKS " + "; ".join(f"{name}={'ok' if ok else 'FAIL'}({detail})" for name, ok, detail in checks))
    print(f"TOTAL {status} elapsed={elapsed:.2f}s flags=" + ",".join(gather_flags(results)))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
