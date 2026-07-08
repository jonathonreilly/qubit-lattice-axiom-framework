#!/usr/bin/env python3
"""Operator-tagged two-band identity runner for the gauged staggered chain.

Companion note:
GAUGED_TWO_BAND_MASS_ENERGY_EQUIVALENCE_OPERATOR_TAGGED_NOTE_2026-07-08.md.

Purpose: the predecessor runner
``scripts/gauged_meson_mass_energy_equivalence_2026_07_08.py`` reported the
two-band equivalence ratio ungated, and its band-2 identification by energy
ordering failed across momentum sectors because of level crossings; the fitted
M2 values swung through 1.6 / 9.3 / 111.6 / negative.  This runner replaces
energy-ordered identification with operator-tagged identification and then
gates the tautology-free identity test.  It derives no gravitational content
and sets no audit status.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import importlib.util
import math
from pathlib import Path
import re
import sys
import time
from typing import Any

sys.dont_write_bytecode = True

import numpy as np
import scipy.sparse as sp


THIS_FILE = Path(__file__).resolve()
REPO_ROOT = THIS_FILE.parents[1]
ENGINE_PATH = THIS_FILE.with_name("gauged_schwinger_staggered_ed_engine_2026_07_08.py")
PREDECESSOR_PATH = THIS_FILE.with_name("gauged_meson_mass_energy_equivalence_2026_07_08.py")
CACHE_PATH = REPO_ROOT / "logs/runner-cache/gauged_meson_mass_energy_equivalence_2026_07_08.txt"
NOTE_NAME = "GAUGED_TWO_BAND_MASS_ENERGY_EQUIVALENCE_OPERATOR_TAGGED_NOTE_2026-07-08.md"

N_MAIN = 16
N_STABILITY = 12
W_MAX = 4
W_SPOT = 5
GRID_MASSES = (0.2, 0.4)
GATED_COUPLINGS = (0.6, 0.8, 1.0, 1.4)
REPORTED_ONLY_COUPLINGS = (0.4, 0.5)
ALL_COUPLINGS = GATED_COUPLINGS + REPORTED_ONLY_COUPLINGS
CACHE_OVERLAP_COUPLINGS = (0.6, 1.0, 1.4)
MOMENTUM_INDICES = (0, 1, 2, 3)
NEIG = 8
LANCZOS_TOL = 1.0e-10
ENGINE_REPRO_TOL = 1.0e-8
CACHE_PRINT_TOL = 5.0e-6
TAG_DOMINANCE = 2.0
IDENTITY_TOL = 0.15
SPECIES_METRIC_TOL = 0.15
STABILITY_TOL = 0.05
W_SPOT_TOL = 1.0e-3
FIT_RES1_TOL = 1.0e-3
FIT_RES2_TOL = 3.0e-2
ORIGIN_ASYMM_TOL = 1.0e-6


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


engine = load_module(ENGINE_PATH, "gauged_schwinger_engine_operator_tagged_20260708")
predecessor = load_module(PREDECESSOR_PATH, "gauged_meson_equivalence_predecessor_20260708")


@dataclass
class FitResult:
    e0: float
    c2: float
    d4: float
    m_comp: float
    e4: float
    r_context: float
    residual: float


@dataclass
class OriginDiscovery:
    rel_index: int
    clean: bool
    asymmetry: float


@dataclass
class SectorTag:
    rel_index: int
    sector_index: int
    momentum: float
    translation_phase: float
    values: np.ndarray
    gaps: np.ndarray
    vector_weights: np.ndarray
    scalar_weights: np.ndarray
    band1_index: int
    band2_index: int
    band1_valid: bool
    band2_valid: bool
    band1_dominance: float
    band2_dominance: float
    band1_old_dominance: float
    band2_old_dominance: float
    band2_over_band1_scalar: float
    energy_order_band1: int
    energy_order_band2: int
    collision: bool = False
    flags: list[str] = field(default_factory=list)


@dataclass
class PointResult:
    n_sites: int
    w_max: int
    mass: float
    coupling: float
    reported_only: bool
    momenta: np.ndarray
    ground_energy: float
    origin_sector: int
    sectors: list[SectorTag]
    band1_all_energies: np.ndarray
    band2_all_energies: np.ndarray
    band1_origin_rel: int
    band2_origin_rel: int
    band1_origin_clean: bool
    band2_origin_clean: bool
    band1_origin_asymmetry: float
    band2_origin_asymmetry: float
    band1_used_rel_indices: tuple[int, ...]
    band2_used_rel_indices: tuple[int, ...]
    band1_k0_energies: np.ndarray
    band1_energies: np.ndarray
    band2_energies: np.ndarray
    band1_min_energy: float
    band2_min_energy: float
    fit1: FitResult
    fit2: FitResult
    ratio_i: float
    c21: float
    threshold_included: bool
    origin_valid: bool
    tag_valid: bool
    tag_valid_band2: bool
    fit_valid: bool
    flags: list[str] = field(default_factory=list)
    drift_i: float = float("nan")
    origin_stable: bool = False
    origin_stability_detail: str = ""
    stability_valid: bool = False


@dataclass
class ZoneResult:
    mass: float
    coupling: float
    origin_sector: int
    sector_indices: list[int]
    band2_energies: np.ndarray
    minimum_rel_index: int


_SETUP_CACHE: dict[tuple[int, int], tuple[Any, Any]] = {}
_HAMILTONIAN_CACHE: dict[tuple[int, int, float, float], sp.csr_matrix] = {}


def finite_float(value: float, digits: int = 6) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    return f"{value:.{digits}g}"


def setup(n_sites: int, w_max: int) -> tuple[Any, Any]:
    key = (n_sites, w_max)
    cached = _SETUP_CACHE.get(key)
    if cached is not None:
        return cached
    basis = engine.Basis(n_sites=n_sites, w_max=w_max, charge_sector=0, rotor=True)
    translation = engine.build_translation_map(basis, engine.magnetic_w_shift_tail)
    cached = (basis, translation)
    _SETUP_CACHE[key] = cached
    return cached


def hamiltonian(n_sites: int, w_max: int, mass: float, coupling: float) -> sp.csr_matrix:
    key = (n_sites, w_max, mass, coupling)
    cached = _HAMILTONIAN_CACHE.get(key)
    if cached is not None:
        return cached
    basis, _translation = setup(n_sites, w_max)
    matrix = engine.build_many_body_hamiltonian(
        basis,
        mass,
        coupling,
        boundary_holonomy_shifts_w=True,
    )
    _HAMILTONIAN_CACHE[key] = matrix
    return matrix


def origin_sector(n_cells: int) -> int:
    # Same fermionic translation convention surfaced by the predecessor as
    # momentum-origin-sector=n_cells/2 for the gauged Q=0 ring.
    return n_cells // 2


def fit_momenta(n_sites: int) -> np.ndarray:
    n_cells = n_sites // 2
    return np.array([np.pi * k / n_cells for k in MOMENTUM_INDICES], dtype=np.float64)


def own_frame_indices(origin_rel: int, n_cells: int) -> tuple[int, ...]:
    return tuple((origin_rel + delta) % n_cells for delta in MOMENTUM_INDICES)


def discover_origin(energies: np.ndarray) -> OriginDiscovery:
    n_cells = len(energies)
    if n_cells == 0 or not np.any(np.isfinite(energies)):
        return OriginDiscovery(rel_index=-1, clean=False, asymmetry=float("nan"))
    rel_index = int(np.nanargmin(energies))
    center = float(energies[rel_index])
    left = float(energies[(rel_index - 1) % n_cells])
    right = float(energies[(rel_index + 1) % n_cells])
    clean = bool(math.isfinite(center) and math.isfinite(left) and math.isfinite(right) and left > center and right > center)
    asymmetries = [
        abs(float(energies[(rel_index + delta) % n_cells]) - float(energies[(rel_index - delta) % n_cells]))
        for delta in (1, 2)
        if math.isfinite(float(energies[(rel_index + delta) % n_cells]))
        and math.isfinite(float(energies[(rel_index - delta) % n_cells]))
    ]
    asymmetry = max(asymmetries, default=float("nan"))
    return OriginDiscovery(rel_index=rel_index, clean=clean, asymmetry=asymmetry)


def origin_location_stable(main_origin: int, main_n_cells: int, small_origin: int, small_n_cells: int) -> bool:
    if main_origin < 0 or small_origin < 0:
        return False
    return math.isclose(main_origin / main_n_cells, small_origin / small_n_cells, rel_tol=0.0, abs_tol=1.0e-12)


def sector_phase(sector_index: int, n_cells: int) -> float:
    return 2.0 * np.pi * sector_index / n_cells


def tag_fourier_phase(fit_momentum: float) -> float:
    # Engine projectors use theta, while the fit uses P = theta/2.
    return 2.0 * fit_momentum


def projected_eigenpairs(matrix: sp.csr_matrix, translation: Any, phase: float, salt: int) -> tuple[np.ndarray, np.ndarray, list[str]]:
    vals, vecs, flags = predecessor.projected_eigenpairs(matrix, translation, phase, NEIG, salt)
    return vals, vecs, flags


def scalar_tag_action(basis: Any, vector: np.ndarray, phase: float) -> np.ndarray:
    n_cells = basis.n_sites // 2
    diagonal = np.zeros(basis.dim, dtype=np.complex128)
    cell_phases = np.exp(-1.0j * phase * np.arange(n_cells, dtype=np.float64))
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        accum = 0.0 + 0.0j
        for cell in range(n_cells):
            even = 2 * cell
            odd = even + 1
            accum += cell_phases[cell] * (((fock >> even) & 1) - ((fock >> odd) & 1))
        for w_index in range(basis.n_w):
            diagonal[basis.index(local_f, w_index)] = accum
    return diagonal * vector


def vector_tag_action(basis: Any, vector: np.ndarray, phase: float) -> np.ndarray:
    n_cells = basis.n_sites // 2
    n_sites = basis.n_sites
    out = np.zeros_like(vector, dtype=np.complex128)
    cell_phases = np.exp(-1.0j * phase * np.arange(n_cells, dtype=np.float64))
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        for cell in range(n_cells):
            link = 2 * cell
            right = (link + 1) % n_sites
            is_boundary = link == n_sites - 1
            delta_w_forward = 1 if is_boundary else 0
            delta_w_backward = -delta_w_forward
            phase_cell = cell_phases[cell]

            forward = engine.apply_cdag_c(fock, link, right)
            if forward is not None:
                new_fock, fermion_sign = forward
                new_local = basis.fock_to_local.get(new_fock)
                if new_local is not None:
                    for w_index in range(basis.n_w):
                        new_w_index = basis.w_index_from_value(basis.w_value(w_index) + delta_w_forward)
                        if new_w_index is None:
                            continue
                        source = basis.index(local_f, w_index)
                        target = basis.index(new_local, new_w_index)
                        out[target] += phase_cell * (1.0j * fermion_sign) * vector[source]

            backward = engine.apply_cdag_c(fock, right, link)
            if backward is not None:
                new_fock, fermion_sign = backward
                new_local = basis.fock_to_local.get(new_fock)
                if new_local is not None:
                    for w_index in range(basis.n_w):
                        new_w_index = basis.w_index_from_value(basis.w_value(w_index) + delta_w_backward)
                        if new_w_index is None:
                            continue
                        source = basis.index(local_f, w_index)
                        target = basis.index(new_local, new_w_index)
                        out[target] += phase_cell * (-1.0j * fermion_sign) * vector[source]
    return out


def normalized_weights(states: np.ndarray, tagged_vector: np.ndarray) -> np.ndarray:
    overlaps = states.conj().T @ tagged_vector
    weights = np.abs(overlaps) ** 2
    total = float(np.sum(weights))
    if total <= 0.0:
        return np.zeros_like(weights, dtype=np.float64)
    return np.asarray(weights / total, dtype=np.float64)


def dominance(weights: np.ndarray, chosen: int, candidates: list[int], excluded: tuple[int, ...] = ()) -> tuple[bool, float]:
    excluded_set = set(excluded)
    runner_candidates = [idx for idx in candidates if idx != chosen and idx not in excluded_set]
    top = float(weights[chosen]) if chosen >= 0 else 0.0
    runner = max((float(weights[idx]) for idx in runner_candidates), default=0.0)
    if runner <= 0.0:
        return top > 0.0, float("inf") if top > 0.0 else 0.0
    ratio = top / runner
    return ratio >= TAG_DOMINANCE, ratio


def ratio_against(weights: np.ndarray, chosen: int, competitor: int) -> tuple[bool, float]:
    top = float(weights[chosen]) if chosen >= 0 else 0.0
    runner = float(weights[competitor]) if competitor >= 0 else 0.0
    if runner <= 0.0:
        return top > 0.0, float("inf") if top > 0.0 else 0.0
    ratio = top / runner
    return ratio >= TAG_DOMINANCE, ratio


def candidate_indices(gaps: np.ndarray) -> list[int]:
    return [idx for idx, gap in enumerate(gaps) if gap > 1.0e-9]


def energy_order_indices(gaps: np.ndarray) -> tuple[int, int]:
    candidates = candidate_indices(gaps)
    if len(candidates) < 2:
        candidates = list(range(min(2, len(gaps))))
    if len(candidates) == 1:
        return candidates[0], candidates[0]
    return candidates[0], candidates[1]


def select_sector_tag(
    basis: Any,
    rel_index: int,
    sector_index: int,
    momentum: float,
    translation_phase: float,
    vals: np.ndarray,
    vecs: np.ndarray,
    ground_energy: float,
    ground_vector: np.ndarray,
) -> SectorTag:
    gaps = np.asarray(vals - ground_energy, dtype=np.float64)
    candidates = candidate_indices(gaps)
    if not candidates:
        candidates = list(range(len(vals)))
    tag_phase = tag_fourier_phase(momentum)
    vector_weights = normalized_weights(vecs, vector_tag_action(basis, ground_vector, tag_phase))
    scalar_weights = normalized_weights(vecs, scalar_tag_action(basis, ground_vector, tag_phase))

    band1_index = max(candidates, key=lambda idx: float(vector_weights[idx]))

    scalar_unrestricted = max(candidates, key=lambda idx: float(scalar_weights[idx]))
    band2_candidates = [idx for idx in candidates if idx != band1_index]
    collision = scalar_unrestricted == band1_index
    flags: list[str] = []
    if collision:
        flags.append(f"P{rel_index}:TAG-COLLISION")
    if not band2_candidates:
        band2_candidates = candidates
        flags.append(f"P{rel_index}:band2-candidate-degenerate")
    band2_index = max(band2_candidates, key=lambda idx: float(scalar_weights[idx]))
    _band1_old_valid, band1_old_dom = dominance(vector_weights, band1_index, candidates)
    band1_valid, band1_dom = dominance(vector_weights, band1_index, candidates, excluded=(band2_index,))
    _band2_old_valid, band2_old_dom = dominance(scalar_weights, band2_index, candidates)
    band2_third_party_valid, band2_dom = dominance(scalar_weights, band2_index, candidates, excluded=(band1_index,))
    band2_over_band1_valid, band2_over_band1 = ratio_against(scalar_weights, band2_index, band1_index)
    band2_valid = bool(band2_third_party_valid and band2_over_band1_valid)
    e1, e2 = energy_order_indices(gaps)
    return SectorTag(
        rel_index=rel_index,
        sector_index=sector_index,
        momentum=momentum,
        translation_phase=translation_phase,
        values=vals,
        gaps=gaps,
        vector_weights=vector_weights,
        scalar_weights=scalar_weights,
        band1_index=band1_index,
        band2_index=band2_index,
        band1_valid=band1_valid,
        band2_valid=band2_valid,
        band1_dominance=band1_dom,
        band2_dominance=band2_dom,
        band1_old_dominance=band1_old_dom,
        band2_old_dominance=band2_old_dom,
        band2_over_band1_scalar=band2_over_band1,
        energy_order_band1=e1,
        energy_order_band2=e2,
        collision=collision,
        flags=flags,
    )


def least_squares_fit(momenta: np.ndarray, energies: np.ndarray) -> FitResult:
    x = momenta * momenta
    design = np.column_stack([np.ones_like(x), x, x * x])
    rel_coeffs, *_ = np.linalg.lstsq(design, energies * energies, rcond=None)
    nr_coeffs, *_ = np.linalg.lstsq(design, energies, rcond=None)
    rel_a, c2, d4 = [float(v) for v in rel_coeffs]
    nr_a, nr_b, e4 = [float(v) for v in nr_coeffs]
    pred = design @ rel_coeffs
    y = energies * energies
    residual = float(np.sqrt(np.mean((pred - y) ** 2)) / max(1.0e-15, np.sqrt(np.mean(y ** 2))))
    e0 = math.sqrt(max(0.0, rel_a))
    m_comp = 1.0 / (2.0 * nr_b) if nr_b != 0.0 else float("nan")
    r_context = (m_comp * c2) / e0 if e0 != 0.0 else float("nan")
    return FitResult(
        e0=float(e0),
        c2=float(c2),
        d4=float(d4),
        m_comp=float(m_comp),
        e4=float(e4),
        r_context=float(r_context),
        residual=residual,
    )


def compute_point(n_sites: int, w_max: int, mass: float, coupling: float, reported_only: bool, salt_base: int) -> PointResult:
    basis, translation = setup(n_sites, w_max)
    matrix = hamiltonian(n_sites, w_max, mass, coupling)
    n_cells = n_sites // 2
    origin = origin_sector(n_cells)
    momenta = fit_momenta(n_sites)
    sectors: list[SectorTag] = []
    raw: dict[int, tuple[np.ndarray, np.ndarray, list[str]]] = {}
    flags: list[str] = []

    for rel_index in range(n_cells):
        sector_index = (origin + rel_index) % n_cells
        phase = sector_phase(sector_index, n_cells)
        vals, vecs, pflags = projected_eigenpairs(matrix, translation, phase, salt_base + 101 * (rel_index + 1))
        raw[rel_index] = (vals, vecs, pflags)
        flags.extend(f"P{rel_index}:{flag}" for flag in pflags)

    ground_vals, ground_vecs, _ground_flags = raw[0]
    ground_energy = float(ground_vals[0])
    ground_vector = ground_vecs[:, 0]

    for rel_index in range(n_cells):
        sector_index = (origin + rel_index) % n_cells
        momentum = float(np.pi * rel_index / n_cells)
        vals, vecs, _pflags = raw[rel_index]
        sector = select_sector_tag(
            basis,
            rel_index,
            sector_index,
            float(momentum),
            sector_phase(sector_index, n_cells),
            vals,
            vecs,
            ground_energy,
            ground_vector,
        )
        sectors.append(sector)
        flags.extend(sector.flags)

    band1_all = np.array([sector.gaps[sector.band1_index] for sector in sectors], dtype=np.float64)
    band2_all = np.array([sector.gaps[sector.band2_index] for sector in sectors], dtype=np.float64)
    band1_origin = discover_origin(band1_all)
    band2_origin = discover_origin(band2_all)
    for label, origin_info in (("BAND1", band1_origin), ("BAND2", band2_origin)):
        if not origin_info.clean:
            flags.append(f"{label}-ORIGIN-NONCLEAN(k*={origin_info.rel_index})")
        if math.isfinite(origin_info.asymmetry) and origin_info.asymmetry > ORIGIN_ASYMM_TOL:
            flags.append(f"{label}-ORIGIN-ASYMMETRIC({origin_info.asymmetry:.2e})")
    if band1_origin.rel_index != 0:
        flags.append(f"BAND1-ORIGIN-NONZERO(k*={band1_origin.rel_index})")

    band1_fit_origin = band1_origin.rel_index if 0 <= band1_origin.rel_index < n_cells else 0
    band2_fit_origin = band2_origin.rel_index if 0 <= band2_origin.rel_index < n_cells else 0
    band1_used = own_frame_indices(band1_fit_origin, n_cells)
    band2_used = own_frame_indices(band2_fit_origin, n_cells)
    band1_k0_used = own_frame_indices(0, n_cells)
    band1 = np.array([band1_all[rel_index] for rel_index in band1_used], dtype=np.float64)
    band2 = np.array([band2_all[rel_index] for rel_index in band2_used], dtype=np.float64)
    band1_k0 = np.array([band1_all[rel_index] for rel_index in band1_k0_used], dtype=np.float64)
    band1_min = float(band1_all[band1_fit_origin])
    band2_min = float(band2_all[band2_fit_origin])
    fit1 = least_squares_fit(momenta, band1)
    fit2 = least_squares_fit(momenta, band2)
    ratio_i = (fit2.m_comp / fit1.m_comp) * (fit1.e0 / fit2.e0) if fit1.m_comp != 0.0 and fit2.e0 != 0.0 else float("nan")
    c21 = fit2.c2 / fit1.c2 if fit1.c2 != 0.0 else float("nan")
    threshold_included = bool(math.isfinite(band1_min) and math.isfinite(band2_min) and band2_min < 2.0 * band1_min)
    origin_valid = bool(band1_origin.clean and band2_origin.clean)
    tag_valid = bool(
        all(sectors[rel_index].band1_valid for rel_index in band1_used)
        and all(sectors[rel_index].band2_valid for rel_index in band2_used)
    )
    tag_valid_band2 = bool(all(sectors[rel_index].band2_valid for rel_index in band2_used))
    fit_valid = bool(fit1.residual <= FIT_RES1_TOL and fit2.residual <= FIT_RES2_TOL)
    if origin != 0:
        flags.append(f"momentum-origin-sector={origin}")
    if not origin_valid:
        flags.append("ORIGIN-EXCLUDED")
    if not threshold_included:
        flags.append("THRESHOLD-EXCLUDED")
    if not fit_valid:
        flags.append("FIT-EXCLUDED")
    if reported_only:
        flags.append("REPORTED-ONLY")
    return PointResult(
        n_sites=n_sites,
        w_max=w_max,
        mass=mass,
        coupling=coupling,
        reported_only=reported_only,
        momenta=momenta,
        ground_energy=ground_energy,
        origin_sector=origin,
        sectors=sectors,
        band1_all_energies=band1_all,
        band2_all_energies=band2_all,
        band1_origin_rel=band1_origin.rel_index,
        band2_origin_rel=band2_origin.rel_index,
        band1_origin_clean=band1_origin.clean,
        band2_origin_clean=band2_origin.clean,
        band1_origin_asymmetry=float(band1_origin.asymmetry),
        band2_origin_asymmetry=float(band2_origin.asymmetry),
        band1_used_rel_indices=band1_used,
        band2_used_rel_indices=band2_used,
        band1_k0_energies=band1_k0,
        band1_energies=band1,
        band2_energies=band2,
        band1_min_energy=band1_min,
        band2_min_energy=band2_min,
        fit1=fit1,
        fit2=fit2,
        ratio_i=float(ratio_i),
        c21=float(c21),
        threshold_included=threshold_included,
        origin_valid=origin_valid,
        tag_valid=tag_valid,
        tag_valid_band2=tag_valid_band2,
        fit_valid=fit_valid,
        flags=flags,
    )


def parse_cache() -> dict[tuple[float, float], dict[str, float]]:
    text = CACHE_PATH.read_text(encoding="utf-8")
    first_line = text.splitlines()[0]
    out: dict[tuple[float, float], dict[str, float]] = {}
    pattern = re.compile(r"m=([0-9.]+),g=([0-9.]+):([^;]+)")
    for match in pattern.finditer(first_line):
        mass = float(match.group(1))
        coupling = float(match.group(2))
        fields: dict[str, float] = {}
        for piece in match.group(3).split(","):
            if "=" not in piece:
                continue
            name, value = piece.split("=", 1)
            try:
                fields[name] = float(value)
            except ValueError:
                continue
        out[(mass, coupling)] = fields
    return out


def predecessor_energy_order_gaps(point: PointResult) -> tuple[np.ndarray, np.ndarray]:
    pairs = [
        predecessor.band_excitations(sector.values, point.ground_energy, sector.rel_index, count=2)
        for sector in point.sectors
    ]
    band1 = np.array([pair[0] for pair in pairs], dtype=np.float64)
    band2 = np.array([pair[1] for pair in pairs], dtype=np.float64)
    return band1, band2


def check_01_regression(points: list[PointResult], cache: dict[tuple[float, float], dict[str, float]]) -> tuple[bool, str]:
    worst_order = 0.0
    worst_cache = 0.0
    parts: list[str] = []
    nonzero_origins: list[str] = []
    for point in points:
        key = (point.mass, point.coupling)
        order_band1, _order_band2 = predecessor_energy_order_gaps(point)
        order_err = float(np.max(np.abs(point.band1_k0_energies[:3] - order_band1[:3])))
        worst_order = max(worst_order, order_err)
        if point.band1_origin_rel != 0:
            nonzero_origins.append(f"m={point.mass},g={point.coupling}:k1*={point.band1_origin_rel}")
        if point.coupling not in CACHE_OVERLAP_COUPLINGS:
            continue
        cache_fields = cache.get(key, {})
        if "E0" in cache_fields:
            cache_err = abs(float(point.band1_k0_energies[0]) - cache_fields["E0"])
            worst_cache = max(worst_cache, cache_err)
            parts.append(f"m={point.mass},g={point.coupling}:E0cache={cache_fields['E0']:.6g},c2cache={cache_fields.get('c2', float('nan')):.6g},err={cache_err:.1e}")
        else:
            worst_cache = float("inf")
            parts.append(f"m={point.mass},g={point.coupling}:cache-missing")
    ok = worst_order <= ENGINE_REPRO_TOL and worst_cache <= CACHE_PRINT_TOL
    detail = f"cache={CACHE_PATH.name},cache_overlap={CACHE_OVERLAP_COUPLINGS},order_err={worst_order:.1e},cache_print_err={worst_cache:.1e};" + "|".join(parts)
    if nonzero_origins:
        detail += ";BAND1-ORIGIN-NONZERO=" + "|".join(nonzero_origins)
    return ok, detail


def attach_stability(main_points: list[PointResult], stability_points: dict[tuple[float, float], PointResult]) -> None:
    for point in main_points:
        if point.reported_only:
            continue
        small = stability_points[(point.mass, point.coupling)]
        point.drift_i = abs(small.ratio_i - point.ratio_i)
        main_n_cells = point.n_sites // 2
        small_n_cells = small.n_sites // 2
        band1_stable = origin_location_stable(point.band1_origin_rel, main_n_cells, small.band1_origin_rel, small_n_cells)
        band2_stable = origin_location_stable(point.band2_origin_rel, main_n_cells, small.band2_origin_rel, small_n_cells)
        point.origin_stable = bool(band1_stable and band2_stable)
        point.origin_stability_detail = (
            f"N{point.n_sites}=({point.band1_origin_rel},{point.band2_origin_rel})/"
            f"N{small.n_sites}=({small.band1_origin_rel},{small.band2_origin_rel})"
        )
        point.flags.append(
            f"{'ORIGIN-STABLE' if point.origin_stable else 'ORIGIN-UNSTABLE'}({point.origin_stability_detail})"
        )
        point.stability_valid = bool(
            point.drift_i <= STABILITY_TOL
            and point.tag_valid_band2
            and small.tag_valid_band2
            and point.origin_valid
            and small.origin_valid
            and point.origin_stable
        )


def gate_included(point: PointResult) -> bool:
    return bool(
        not point.reported_only
        and point.origin_valid
        and point.tag_valid
        and point.stability_valid
        and point.threshold_included
        and point.fit_valid
    )


def check_02_tag_method(points: list[PointResult]) -> tuple[bool, str]:
    gated = [p for p in points if not p.reported_only]
    valid = [p for p in gated if p.tag_valid and p.origin_valid]
    bad = [p for p in gated if not (p.tag_valid and p.origin_valid)]
    detail = f"N={N_MAIN},own_frame_tag_origin_valid={len(valid)}/{len(gated)}"
    if bad:
        detail += ";invalid=" + ",".join(f"m={p.mass},g={p.coupling}" for p in bad)
    return len(valid) >= 4, detail


def check_03_window_trend_identity(points: list[PointResult]) -> tuple[bool, str]:
    details: list[str] = []
    ok = True
    for mass in GRID_MASSES:
        valid = sorted(
            [p for p in points if p.mass == mass and gate_included(p) and math.isfinite(p.c21)],
            key=lambda p: p.coupling,
            reverse=True,
        )
        if len(valid) < 2:
            ok = False
            details.append(f"m={mass}:FAIL(valid_couplings={len(valid)}<2)")
            continue

        violations: list[tuple[float, float, float]] = []
        for stronger, weaker in zip(valid, valid[1:]):
            stronger_dev = abs(stronger.c21 - 1.0)
            weaker_dev = abs(weaker.c21 - 1.0)
            growth = weaker_dev - stronger_dev
            if growth > 1.0e-12:
                violations.append((stronger.coupling, weaker.coupling, growth))
        large_violations = [violation for violation in violations if violation[2] > 0.02 + 1.0e-12]
        trend_ok = not large_violations and len(violations) <= 1
        weakest = min(valid, key=lambda p: p.coupling)
        weakest_dev = abs(weakest.c21 - 1.0)
        weakest_ok = weakest_dev <= IDENTITY_TOL
        if not trend_ok or not weakest_ok:
            ok = False
        series = ">".join(f"g={p.coupling}:dev={abs(p.c21 - 1.0):.4g},c21={p.c21:.4g},ratio_I={p.ratio_i:.4g}" for p in valid)
        violation_text = "none" if not violations else ",".join(
            f"g{hi}->g{lo}:dev_growth={growth:.3g}" for hi, lo, growth in violations
        )
        details.append(
            f"m={mass}:series_desc_g={series},violations={violation_text},"
            f"weakest=g={weakest.coupling}:dev={weakest_dev:.3g},"
            f"valid={len(valid)}"
        )
    return ok, ";".join(details)


def check_04_artifact_collapse(points: list[PointResult]) -> tuple[bool, str]:
    included = [p for p in points if gate_included(p)]
    labels: list[str] = []
    xs: list[float] = []
    ys: list[float] = []
    nonfinite: list[str] = []
    for point in included:
        for band_name, fit in (("b1", point.fit1), ("b2", point.fit2)):
            x = fit.e0 * fit.e0
            y = 1.0 - fit.c2
            label = f"m={point.mass},g={point.coupling},{band_name}"
            if not math.isfinite(x) or not math.isfinite(y):
                nonfinite.append(label)
                continue
            labels.append(label)
            xs.append(float(x))
            ys.append(float(y))
    if nonfinite:
        return False, "nonfinite=" + ",".join(nonfinite)
    if len(xs) < 2:
        return False, f"insufficient-valid-band-points={len(xs)}"
    x_array = np.asarray(xs, dtype=np.float64)
    y_array = np.asarray(ys, dtype=np.float64)
    denom = float(np.dot(x_array, x_array))
    alpha = float(np.dot(x_array, y_array) / denom) if denom > 0.0 else float("nan")
    residual = y_array - alpha * x_array
    rms = float(np.sqrt(np.mean(residual * residual)))
    scale = float(np.sqrt(np.mean(y_array * y_array)))
    scatter = rms / scale if scale > 0.0 else float("inf")
    pairs = ",".join(f"{label}:x={x:.4g},y={y:.4g}" for label, x, y in zip(labels, xs, ys))
    ok = bool(alpha > 0.0 and scatter <= 0.40)
    return ok, f"pairs={pairs};alpha={alpha:.4g},rel_rms_scatter={scatter:.3g}"


def check_04b_cross_species_band2_metric(points: list[PointResult]) -> tuple[bool, str]:
    by_key = {(point.mass, point.coupling): point for point in points}
    weakest_valid: tuple[float, float] | None = None
    details: list[str] = []
    for coupling in sorted(ALL_COUPLINGS):
        low = by_key.get((GRID_MASSES[0], coupling))
        high = by_key.get((GRID_MASSES[1], coupling))
        if low is None or high is None:
            continue
        ratio = low.fit2.c2 / high.fit2.c2 if high.fit2.c2 != 0.0 else float("inf")
        both_valid = gate_included(low) and gate_included(high)
        zone = "gated" if coupling in GATED_COUPLINGS else "reported"
        details.append(
            f"g={coupling}:{zone},ratio={finite_float(ratio,5)},"
            f"valid={'Y' if both_valid else 'N'}"
        )
        if coupling in GATED_COUPLINGS and both_valid and weakest_valid is None:
            weakest_valid = (coupling, float(ratio))
    if weakest_valid is None:
        return False, "no-coupling-with-both-species-valid;" + "|".join(details)
    weakest_coupling, weakest_ratio = weakest_valid
    dev = abs(weakest_ratio - 1.0)
    ok = bool(math.isfinite(dev) and dev <= SPECIES_METRIC_TOL)
    return ok, f"weakest_valid_g={weakest_coupling},dev={dev:.3g};" + "|".join(details)


def check_05_fit_honesty(points: list[PointResult]) -> tuple[bool, str]:
    gated = [p for p in points if not p.reported_only and p.tag_valid]
    excluded = [p for p in gated if not p.fit_valid]
    details = [
        f"m={p.mass},g={p.coupling}:res=({p.fit1.residual:.1e},{p.fit2.residual:.1e}){'-EXCL' if not p.fit_valid else ''}"
        for p in gated
    ]
    return True, "excluded=" + str(len(excluded)) + ";" + ",".join(details)


def check_06_stability(points: list[PointResult], w_spot_drift: float, w_spot_valid: bool) -> tuple[bool, str]:
    gated = [p for p in points if not p.reported_only]
    stable = [p for p in gated if p.stability_valid]
    drift_detail = ",".join(
        f"m={p.mass},g={p.coupling}:drift={finite_float(p.drift_i, 4)},"
        f"stable={'Y' if p.stability_valid else 'N'},"
        f"origin={'ORIGIN-STABLE' if p.origin_stable else 'ORIGIN-UNSTABLE'}({p.origin_stability_detail})"
        for p in gated
    )
    ok = bool(w_spot_valid and w_spot_drift <= W_SPOT_TOL and len(stable) >= 3)
    detail = f"stable={len(stable)}/{len(gated)},Wspot={w_spot_drift:.3g};{drift_detail}"
    return ok, detail


def used_rel_indices(point: PointResult) -> tuple[int, ...]:
    return tuple(sorted(set(point.band1_used_rel_indices + point.band2_used_rel_indices)))


def weights_table(point: PointResult) -> str:
    chunks: list[str] = []
    for rel_index in used_rel_indices(point):
        sector = point.sectors[rel_index]
        vw = ",".join(f"{w:.2g}" for w in sector.vector_weights)
        sw = ",".join(f"{w:.2g}" for w in sector.scalar_weights)
        chunks.append(f"k{sector.rel_index}:V[{vw}]S[{sw}]")
    return "weights={" + "/".join(chunks) + "}"


def result_fragment(point: PointResult) -> str:
    status = []
    if point.reported_only:
        status.append("REPORTED-ONLY")
    status.append("ORG-Y" if point.origin_valid else "ORIGIN-NONCLEAN")
    status.append("TAG-Y" if point.tag_valid else "TAG-N")
    status.append("STAB-Y" if point.stability_valid else "STAB-N")
    if not point.reported_only:
        status.append("ORIGSTAB-Y" if point.origin_stable else "ORIGIN-UNSTABLE")
    status.append("THR-Y" if point.threshold_included else "THRESHOLD-EXCLUDED")
    status.append("FIT-Y" if point.fit_valid else "FIT-EXCLUDED")
    text = (
        f"m={point.mass},g={point.coupling}:"
        f"kstar=({point.band1_origin_rel},{point.band2_origin_rel}),"
        f"asym=({finite_float(point.band1_origin_asymmetry,3)},{finite_float(point.band2_origin_asymmetry,3)}),"
        f"E01={finite_float(point.fit1.e0)},E02={finite_float(point.fit2.e0)},"
        f"M1={finite_float(point.fit1.m_comp)},M2={finite_float(point.fit2.m_comp)},"
        f"c1sq={finite_float(point.fit1.c2)},c2sq={finite_float(point.fit2.c2)},"
        f"ratio_I={finite_float(point.ratio_i)},c21={finite_float(point.c21)},"
        f"Rctx=({finite_float(point.fit1.r_context)},{finite_float(point.fit2.r_context)}),"
        f"res=({point.fit1.residual:.2e},{point.fit2.residual:.2e}),"
        f"thr={finite_float(point.band2_min_energy)}/{finite_float(2.0 * point.band1_min_energy)},"
        f"margin={finite_float(2.0 * point.band1_min_energy - point.band2_min_energy)},"
        f"driftI={finite_float(point.drift_i, 4)},"
        f"status={'+'.join(status)}"
    )
    if not point.tag_valid:
        text += "," + weights_table(point)
    return text


def tags_fragment(point: PointResult) -> str:
    b1_agrees = ",".join(
        f"k{s.rel_index}:{'Y' if s.band1_index == s.energy_order_band1 else 'N'}"
        for s in (point.sectors[rel_index] for rel_index in point.band1_used_rel_indices)
    )
    b2_agrees = ",".join(
        f"k{s.rel_index}:{'Y' if s.band2_index == s.energy_order_band2 else 'N'}"
        for s in (point.sectors[rel_index] for rel_index in point.band2_used_rel_indices)
    )
    b1_dom = ",".join(
        f"k{s.rel_index}:V3={finite_float(s.band1_dominance,3)}"
        for s in (point.sectors[rel_index] for rel_index in point.band1_used_rel_indices)
    )
    b2_dom = ",".join(
        f"k{s.rel_index}:S3={finite_float(s.band2_dominance,3)},S2S1={finite_float(s.band2_over_band1_scalar,3)}"
        for s in (point.sectors[rel_index] for rel_index in point.band2_used_rel_indices)
    )
    collisions = sum(1 for rel_index in used_rel_indices(point) if point.sectors[rel_index].collision)
    chosen_b1 = ",".join(f"k{s.rel_index}:i{s.band1_index}" for s in (point.sectors[rel_index] for rel_index in point.band1_used_rel_indices))
    chosen_b2 = ",".join(f"k{s.rel_index}:i{s.band2_index}" for s in (point.sectors[rel_index] for rel_index in point.band2_used_rel_indices))
    return (
        f"m={point.mass},g={point.coupling}:valid={'Y' if point.tag_valid else 'N'},"
        f"origin={'Y' if point.origin_valid else 'N'},kstar=({point.band1_origin_rel},{point.band2_origin_rel}),"
        f"b1idx={{{chosen_b1}}},b2idx={{{chosen_b2}}},"
        f"agree=({{{b1_agrees}}};{{{b2_agrees}}}),dom=({{{b1_dom}}};{{{b2_dom}}}),"
        f"collisions={collisions}"
    )


def band2_zone_fragment(zone: ZoneResult) -> str:
    entries = ",".join(
        f"k{k}/s{sector}:E={finite_float(float(energy),7)}"
        for k, (sector, energy) in enumerate(zip(zone.sector_indices, zone.band2_energies))
    )
    minimum_energy = (
        float(zone.band2_energies[zone.minimum_rel_index])
        if 0 <= zone.minimum_rel_index < len(zone.band2_energies)
        else float("nan")
    )
    return (
        f"m={zone.mass},g={zone.coupling},origin={zone.origin_sector}:"
        f"{entries};min=k{zone.minimum_rel_index},E={finite_float(minimum_energy,7)};"
        "BAND2-ZONE-STRUCTURE(own-frame origin discovery; fits use k*+d sectors)"
    )


def band2_zone_from_point(point: PointResult) -> ZoneResult:
    return ZoneResult(
        mass=point.mass,
        coupling=point.coupling,
        origin_sector=point.origin_sector,
        sector_indices=[sector.sector_index for sector in point.sectors],
        band2_energies=point.band2_all_energies,
        minimum_rel_index=point.band2_origin_rel,
    )


def spec_note() -> str:
    return (
        "SPEC-NOTE "
        "tag-phase uses engine theta=2P although the prompt writes exp(-iPj), because predecessor fits use P=theta/2; "
        "P=0 vacuum candidate is excluded by positive-gap candidate selection; "
        "O_V literal even-link intra-cell current has no boundary link on even N, so boundary-W handling is implemented but inert; "
        "origin stability compares k*/n_cells because N=12 and N=16 have different sector counts; "
        "threshold test uses tagged band minima E02_min>=2E01_min as exclusion, not a continuum proof."
    )


def gather_flags(points: list[PointResult], w_spot_drift: float) -> list[str]:
    origin_split = "|".join(
        f"m={point.mass},g={point.coupling}:({point.band1_origin_rel},{point.band2_origin_rel})"
        for point in points
    )
    flags = [
        f"note={NOTE_NAME}",
        "Q0-ring-Gauss",
        "finite-W-magnetic-translation",
        "g0-decoupled-comparator-inherited",
        "operator-tagged-band-identification",
        "all-sector-origin-discovery",
        "own-frame-momenta-d0123-Pprime=pi*d/ncells",
        "GATED_COUPLINGS=0.6/0.8/1.0/1.4",
        "REPORTED_ONLY_COUPLINGS=0.4/0.5",
        f"ORIGIN-SPLIT[{origin_split}]",
        "BAND2-ZONE-STRUCTURE(own-frame origin discovery; fits use k*+d sectors)",
        f"Wspot-drift={w_spot_drift:.3g}",
        spec_note(),
    ]
    for point in points:
        flags.extend(f"m={point.mass},g={point.coupling}:{flag}" for flag in point.flags)
    return flags


def verdict_flag(ok02: bool, passed: bool) -> str:
    if not ok02:
        return "TAGGING-FAILED"
    if passed:
        return "IDENTITY-GATED"
    return "IDENTITY-MIXED"


def main() -> int:
    started = time.time()
    cache = parse_cache()
    main_points: list[PointResult] = []
    salt = 0
    for mass in GRID_MASSES:
        for coupling in ALL_COUPLINGS:
            salt += 1
            main_points.append(
                compute_point(
                    N_MAIN,
                    W_MAX,
                    mass,
                    coupling,
                    reported_only=coupling in REPORTED_ONLY_COUPLINGS,
                    salt_base=10000 * salt,
                )
            )

    stability_points: dict[tuple[float, float], PointResult] = {}
    for mass in GRID_MASSES:
        for coupling in GATED_COUPLINGS:
            salt += 1
            stability_points[(mass, coupling)] = compute_point(
                N_STABILITY,
                W_MAX,
                mass,
                coupling,
                reported_only=False,
                salt_base=10000 * salt,
            )
    attach_stability(main_points, stability_points)

    w4 = next(p for p in main_points if p.mass == 0.2 and p.coupling == 1.0)
    salt += 1
    w5 = compute_point(N_MAIN, W_SPOT, 0.2, 1.0, reported_only=True, salt_base=10000 * salt)
    w_spot_drift = float(np.max(np.abs(w5.band2_energies - w4.band2_energies)))
    w_spot_valid = bool(w4.tag_valid_band2 and w5.tag_valid_band2)

    band2_zone_points = [
        next(p for p in main_points if p.mass == 0.2 and p.coupling == 0.8),
        next(p for p in main_points if p.mass == 0.2 and p.coupling == 1.4),
    ]
    band2_zones = [band2_zone_from_point(point) for point in band2_zone_points]

    ok01, detail01 = check_01_regression(main_points, cache)
    ok02, detail02 = check_02_tag_method(main_points)
    ok03, detail03 = check_03_window_trend_identity(main_points)
    ok04, detail04 = check_04_artifact_collapse(main_points)
    ok04b, detail04b = check_04b_cross_species_band2_metric(main_points)
    ok05, detail05 = check_05_fit_honesty(main_points)
    ok06, detail06 = check_06_stability(main_points, w_spot_drift, w_spot_valid)
    checks = [
        ("CHECK-01", ok01, detail01),
        ("CHECK-02", ok02, detail02),
        ("CHECK-03", ok03, detail03),
        ("CHECK-04", ok04, detail04),
        ("CHECK-04b", ok04b, detail04b),
        ("CHECK-05", ok05, detail05),
        ("CHECK-06", ok06, detail06),
    ]
    passed = all(ok for _name, ok, _detail in checks)
    elapsed = time.time() - started
    verdict = verdict_flag(ok02, passed)
    status = "PASS" if passed else "FAIL"

    print("RESULTS " + "; ".join(result_fragment(point) for point in main_points))
    print("TAGS " + "; ".join(tags_fragment(point) for point in main_points))
    print("BAND2-ZONE " + "; ".join(band2_zone_fragment(zone) for zone in band2_zones))
    print("CHECKS " + "; ".join(f"{name}={'ok' if ok else 'FAIL'}({detail})" for name, ok, detail in checks))
    print(f"TOTAL {status} {verdict} elapsed={elapsed:.2f}s flags=" + ",".join(gather_flags(main_points, w_spot_drift)))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
