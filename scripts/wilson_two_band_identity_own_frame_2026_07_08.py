#!/usr/bin/env python3
"""Wilson two-band own-frame identity runner.

The staggered two-band identity test filed a bounded methods no-go: a
two-sided validity squeeze (continuum pollution at weak coupling; band-2
zone-origin migration + narrow bands at strong coupling). The Wilson kernel
removes the zone obstruction by construction (both meson bands rest at P = 0;
doublers gapped). This runner re-executes the own-frame identity test on the
Wilson comparator. Companion note:
WILSON_TWO_BAND_MASS_ENERGY_EQUIVALENCE_IDENTITY_NOTE_2026-07-08.md.
No gravitational content, no audit status.
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
import scipy.sparse.linalg as spla


THIS_FILE = Path(__file__).resolve()
REPO_ROOT = THIS_FILE.parents[1]
ENGINE_PATH = THIS_FILE.with_name("gauged_wilson_schwinger_ed_engine_2026_07_08.py")
CACHE_PATH = REPO_ROOT / "logs/runner-cache/gauged_wilson_schwinger_ed_engine_2026_07_08.txt"
NOTE_NAME = "WILSON_TWO_BAND_MASS_ENERGY_EQUIVALENCE_IDENTITY_NOTE_2026-07-08.md"

N_MAIN = 8
N_STABILITY = 6
N10_SPOT = 10
W_MAX = 4
W_SPOT = 5
W_SPOT_MASS = 0.2
W_SPOT_COUPLING = 1.4
N10_SPOT_MASS = 0.2
N10_SPOT_COUPLING = 1.4
N10_SPOT_REL_INDICES = (0, 1, 2, 3)
GRID_MASSES = (0.2, 0.4)
GATED_COUPLINGS = (1.0, 1.2, 1.4, 1.7)
REPORTED_ONLY_COUPLINGS = (0.6, 2.0)
ALL_COUPLINGS = GATED_COUPLINGS + REPORTED_ONLY_COUPLINGS
CACHE_MASS = 0.3
CACHE_COUPLINGS = (0.6, 1.0)
NEIG = 8
FIT_DELTAS = (0, 1, 2, 3)
LANCZOS_TOL = 1.0e-10
CACHE_PRINT_TOL = 5.0e-6
TAG_DOMINANCE = 2.0
IDENTITY_TOL = 0.15
SPECIES_METRIC_TOL = 0.15
STABILITY_TOL = 0.05
N10_SPOT_TOL = 0.10
W_SPOT_TOL = 1.0e-3
FIT_RES1_TOL = 1.0e-3
FIT_RES2_TOL = 3.0e-2
ORIGIN_ASYMM_TOL = 1.0e-6
POSITIVE_GAP_TOL = 1.0e-9


def load_engine(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("wilson_schwinger_engine_own_frame_20260708", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import Wilson engine from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


engine = load_engine(ENGINE_PATH)


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
    ps_weights: np.ndarray
    scalar_weights: np.ndarray
    band1_tag: str
    band2_tag: str
    band1_index: int
    band2_index: int
    band1_valid: bool
    band2_valid: bool
    band1_dominance: float
    band2_dominance: float
    band1_old_dominance: float
    band2_old_dominance: float
    band2_over_band1_owntag: float
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
    ground_sector: int
    tag_roles_swapped: bool
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
    n10_drift_i: float = float("nan")
    origin_stable: bool = False
    origin_stability_detail: str = ""
    stability_valid: bool = False
    stability_leg: str = "NONE"


@dataclass
class N10SpotResult:
    n_sites: int
    w_max: int
    mass: float
    coupling: float
    momenta: np.ndarray
    ground_energy: float
    ground_sector: int
    tag_roles_swapped: bool
    sectors: list[SectorTag]
    band1_energies: np.ndarray
    band2_energies: np.ndarray
    fit1: FitResult
    fit2: FitResult
    ratio_i: float
    c21: float
    threshold_included: bool
    tag_valid: bool
    tag_valid_band2: bool
    fit_valid: bool
    k1_rise_valid: bool
    flags: list[str] = field(default_factory=list)


@dataclass
class ZoneResult:
    mass: float
    coupling: float
    ground_sector: int
    sector_indices: list[int]
    band2_energies: np.ndarray
    minimum_rel_index: int


_SETUP_CACHE: dict[tuple[int, int], tuple[Any, Any]] = {}


def finite_float(value: float, digits: int = 6) -> str:
    if math.isnan(value):
        return "nan"
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    return f"{value:.{digits}g}"


def fmt_array(values: np.ndarray, digits: int = 10) -> str:
    return "[" + ",".join(f"{float(x):.{digits}g}" for x in values) + "]"


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
    basis, _translation = setup(n_sites, w_max)
    return engine.build_many_body_hamiltonian(
        basis,
        mass,
        coupling,
        boundary_holonomy_shifts_w=True,
    )


def sector_phase(sector_index: int, n_sites: int) -> float:
    return 2.0 * np.pi * sector_index / n_sites


def fit_momenta(n_sites: int) -> np.ndarray:
    return 2.0 * np.pi * np.asarray(FIT_DELTAS, dtype=np.float64) / n_sites


def own_frame_indices(origin_rel: int, n_sites: int) -> tuple[int, ...]:
    return tuple((origin_rel + delta) % n_sites for delta in FIT_DELTAS)


def deterministic_v0(dim: int, salt: int) -> np.ndarray:
    if hasattr(engine, "deterministic_v0"):
        return engine.deterministic_v0(dim, salt)
    rng = np.random.default_rng(20260708 + 7919 * salt + dim)
    vec = rng.normal(size=dim) + 1.0j * rng.normal(size=dim)
    return vec / np.linalg.norm(vec)


def projected_eigenpairs(
    matrix: sp.csr_matrix,
    translation: Any,
    momentum: float,
    k: int,
    salt: int,
    tol: float = LANCZOS_TOL,
) -> tuple[np.ndarray, np.ndarray, list[str]]:
    dim = matrix.shape[0]

    def matvec(vector: np.ndarray) -> np.ndarray:
        projected = engine.projected_vector(vector, translation, momentum)
        return engine.projected_vector(matrix @ projected, translation, momentum)

    k_eff = min(dim - 2, k)
    operator = spla.LinearOperator((dim, dim), matvec=matvec, dtype=np.complex128)
    vals, vecs = spla.eigsh(
        operator,
        k=k_eff,
        which="SA",
        return_eigenvectors=True,
        tol=tol,
        maxiter=8000,
        ncv=min(dim - 1, max(36, 6 * k_eff + 18)),
        v0=deterministic_v0(dim, salt),
    )

    items: list[tuple[float, np.ndarray]] = []
    flags: list[str] = []
    for col in range(vecs.shape[1]):
        projected = engine.projected_vector(vecs[:, col], translation, momentum)
        norm = float(np.linalg.norm(projected))
        if norm <= 1.0e-8:
            flags.append("PROJECTED-NULL-EIGENVECTOR")
            continue
        state = projected / norm
        rayleigh = float(np.vdot(state, matrix @ state).real)
        items.append((rayleigh, state))
    items.sort(key=lambda item: item[0])
    if len(items) < k:
        flags.append(f"NEIG-SHORT({len(items)}/{k})")
    values = np.asarray([item[0] for item in items[:k]], dtype=np.float64)
    states = np.column_stack([item[1] for item in items[:k]]) if items else np.zeros((dim, 0), dtype=np.complex128)
    return values, states, flags


def discover_origin(energies: np.ndarray) -> OriginDiscovery:
    n_sites = len(energies)
    if n_sites == 0 or not np.any(np.isfinite(energies)):
        return OriginDiscovery(rel_index=-1, clean=False, asymmetry=float("nan"))
    rel_index = int(np.nanargmin(energies))
    center = float(energies[rel_index])
    left = float(energies[(rel_index - 1) % n_sites])
    right = float(energies[(rel_index + 1) % n_sites])
    clean = bool(math.isfinite(center) and math.isfinite(left) and math.isfinite(right) and left > center and right > center)
    max_delta = min(3, n_sites // 2)
    asymmetries = [
        abs(float(energies[(rel_index + delta) % n_sites]) - float(energies[(rel_index - delta) % n_sites]))
        for delta in range(1, max_delta + 1)
        if math.isfinite(float(energies[(rel_index + delta) % n_sites]))
        and math.isfinite(float(energies[(rel_index - delta) % n_sites]))
    ]
    return OriginDiscovery(rel_index=rel_index, clean=clean, asymmetry=max(asymmetries, default=float("nan")))


def origin_location_stable(main_origin: int, main_n: int, small_origin: int, small_n: int) -> bool:
    if main_origin < 0 or small_origin < 0:
        return False
    return math.isclose(main_origin / main_n, small_origin / small_n, rel_tol=0.0, abs_tol=1.0e-12)


def scalar_tag_action(basis: Any, vector: np.ndarray, phase: float) -> np.ndarray:
    diagonal = np.zeros(basis.dim, dtype=np.complex128)
    site_phases = np.exp(-1.0j * phase * np.arange(basis.n_sites, dtype=np.float64))
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        accum = 0.0 + 0.0j
        for site in range(basis.n_sites):
            up = (fock >> engine.mode_index(site, 0)) & 1
            down = (fock >> engine.mode_index(site, 1)) & 1
            accum += site_phases[site] * (up - down)
        for w_index in range(basis.n_w):
            diagonal[basis.index(local_f, w_index)] = accum
    return diagonal * vector


def pseudoscalar_tag_action(basis: Any, vector: np.ndarray, phase: float) -> np.ndarray:
    out = np.zeros_like(vector, dtype=np.complex128)
    site_phases = np.exp(-1.0j * phase * np.arange(basis.n_sites, dtype=np.float64))
    for local_f, fock_value in enumerate(basis.focks):
        fock = int(fock_value)
        for site in range(basis.n_sites):
            up_mode = engine.mode_index(site, 0)
            down_mode = engine.mode_index(site, 1)
            phase_site = site_phases[site]
            up_from_down = engine.apply_cdag_c(fock, up_mode, down_mode)
            if up_from_down is not None:
                new_fock, fermion_sign = up_from_down
                new_local = basis.fock_to_local.get(new_fock)
                if new_local is not None:
                    coefficient = -1.0j * phase_site * fermion_sign
                    for w_index in range(basis.n_w):
                        source = basis.index(local_f, w_index)
                        target = basis.index(new_local, w_index)
                        out[target] += coefficient * vector[source]
            down_from_up = engine.apply_cdag_c(fock, down_mode, up_mode)
            if down_from_up is not None:
                new_fock, fermion_sign = down_from_up
                new_local = basis.fock_to_local.get(new_fock)
                if new_local is not None:
                    coefficient = 1.0j * phase_site * fermion_sign
                    for w_index in range(basis.n_w):
                        source = basis.index(local_f, w_index)
                        target = basis.index(new_local, w_index)
                        out[target] += coefficient * vector[source]
    return out


def normalized_weights(states: np.ndarray, tagged_vector: np.ndarray) -> np.ndarray:
    if states.shape[1] == 0:
        return np.zeros(0, dtype=np.float64)
    overlaps = states.conj().T @ tagged_vector
    weights = np.abs(overlaps) ** 2
    total = float(np.sum(weights))
    if total <= 0.0:
        return np.zeros_like(weights, dtype=np.float64)
    return np.asarray(weights / total, dtype=np.float64)


def dominance(weights: np.ndarray, chosen: int, candidates: list[int], excluded: tuple[int, ...] = ()) -> tuple[bool, float]:
    excluded_set = set(excluded)
    competitors = [idx for idx in candidates if idx != chosen and idx not in excluded_set]
    top = float(weights[chosen]) if 0 <= chosen < len(weights) else 0.0
    runner = max((float(weights[idx]) for idx in competitors if idx < len(weights)), default=0.0)
    if runner <= 0.0:
        return top > 0.0, float("inf") if top > 0.0 else 0.0
    ratio = top / runner
    return ratio >= TAG_DOMINANCE, ratio


def ratio_against(weights: np.ndarray, chosen: int, competitor: int) -> tuple[bool, float]:
    top = float(weights[chosen]) if 0 <= chosen < len(weights) else 0.0
    runner = float(weights[competitor]) if 0 <= competitor < len(weights) else 0.0
    if runner <= 0.0:
        return top > 0.0, float("inf") if top > 0.0 else 0.0
    ratio = top / runner
    return ratio >= TAG_DOMINANCE, ratio


def candidate_indices(gaps: np.ndarray) -> list[int]:
    return [idx for idx, gap in enumerate(gaps) if gap > POSITIVE_GAP_TOL]


def energy_order_indices(gaps: np.ndarray) -> tuple[int, int]:
    candidates = candidate_indices(gaps)
    if len(candidates) < 2:
        candidates = list(range(min(2, len(gaps))))
    if not candidates:
        return -1, -1
    if len(candidates) == 1:
        return candidates[0], candidates[0]
    return candidates[0], candidates[1]


def selected_gap(gaps: np.ndarray, index: int) -> float:
    if 0 <= index < len(gaps):
        return float(gaps[index])
    return float("nan")


def assignment_indices(primary_weights: np.ndarray, secondary_weights: np.ndarray, candidates: list[int]) -> tuple[int, int, bool]:
    if not candidates:
        return -1, -1, False
    band1 = max(candidates, key=lambda idx: float(primary_weights[idx]))
    secondary_unrestricted = max(candidates, key=lambda idx: float(secondary_weights[idx]))
    band2_candidates = [idx for idx in candidates if idx != band1]
    collision = secondary_unrestricted == band1
    if not band2_candidates:
        band2_candidates = candidates
    band2 = max(band2_candidates, key=lambda idx: float(secondary_weights[idx]))
    return band1, band2, collision


def decide_tag_roles(gaps: np.ndarray, ps_weights: np.ndarray, scalar_weights: np.ndarray) -> tuple[bool, list[str]]:
    candidates = candidate_indices(gaps)
    flags: list[str] = []
    if len(candidates) < 2:
        return False, ["TAG-ROLE-AMBIGUOUS(fewer-than-two-positive-candidates)"]
    default_b1, default_b2, _default_collision = assignment_indices(ps_weights, scalar_weights, candidates)
    swapped_b1, swapped_b2, _swapped_collision = assignment_indices(scalar_weights, ps_weights, candidates)
    default_lower = gaps[default_b1] <= gaps[default_b2] + 1.0e-12
    swapped_lower = gaps[swapped_b1] <= gaps[swapped_b2] + 1.0e-12
    if swapped_lower and (not default_lower or gaps[swapped_b1] < gaps[default_b1] - 1.0e-12):
        return True, ["TAG-ROLES-SWAPPED"]
    if not default_lower and not swapped_lower:
        flags.append("TAG-ROLE-AMBIGUOUS(neither-assignment-has-band1-lower-at-P0)")
        return bool(gaps[swapped_b1] < gaps[default_b1]), flags
    return False, flags


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
    tag_roles_swapped: bool,
) -> SectorTag:
    gaps = np.asarray(vals - ground_energy, dtype=np.float64)
    candidates = candidate_indices(gaps)
    if not candidates:
        candidates = list(range(len(vals)))
    ps_weights = normalized_weights(vecs, pseudoscalar_tag_action(basis, ground_vector, momentum))
    scalar_weights = normalized_weights(vecs, scalar_tag_action(basis, ground_vector, momentum))
    role1_name = "S" if tag_roles_swapped else "PS"
    role2_name = "PS" if tag_roles_swapped else "S"
    role1_weights = scalar_weights if tag_roles_swapped else ps_weights
    role2_weights = ps_weights if tag_roles_swapped else scalar_weights

    band1_index, band2_index, collision = assignment_indices(role1_weights, role2_weights, candidates)
    flags: list[str] = []
    if collision:
        flags.append(f"k{rel_index}:TAG-COLLISION")
    if band1_index < 0 or band2_index < 0:
        flags.append(f"k{rel_index}:TAG-SELECTION-FAILED")
    _band1_old_valid, band1_old_dom = dominance(role1_weights, band1_index, candidates)
    band1_valid, band1_dom = dominance(role1_weights, band1_index, candidates, excluded=(band2_index,))
    _band2_old_valid, band2_old_dom = dominance(role2_weights, band2_index, candidates)
    band2_third_party_valid, band2_dom = dominance(role2_weights, band2_index, candidates, excluded=(band1_index,))
    band2_over_band1_valid, band2_over_band1 = ratio_against(role2_weights, band2_index, band1_index)
    band2_valid = bool(band2_third_party_valid and band2_over_band1_valid)
    e1, e2 = energy_order_indices(gaps)
    return SectorTag(
        rel_index=rel_index,
        sector_index=sector_index,
        momentum=momentum,
        translation_phase=translation_phase,
        values=vals,
        gaps=gaps,
        ps_weights=ps_weights,
        scalar_weights=scalar_weights,
        band1_tag=role1_name,
        band2_tag=role2_name,
        band1_index=band1_index,
        band2_index=band2_index,
        band1_valid=band1_valid,
        band2_valid=band2_valid,
        band1_dominance=band1_dom,
        band2_dominance=band2_dom,
        band1_old_dominance=band1_old_dom,
        band2_old_dominance=band2_old_dom,
        band2_over_band1_owntag=band2_over_band1,
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
    _nr_a, nr_b, e4 = [float(v) for v in nr_coeffs]
    pred = design @ rel_coeffs
    y = energies * energies
    residual = float(np.sqrt(np.mean((pred - y) ** 2)) / max(1.0e-15, np.sqrt(np.mean(y * y))))
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


def compute_all_sector_eigenpairs(
    matrix: sp.csr_matrix,
    translation: Any,
    n_sites: int,
    salt_base: int,
) -> tuple[dict[int, tuple[np.ndarray, np.ndarray, list[str]]], list[str]]:
    raw: dict[int, tuple[np.ndarray, np.ndarray, list[str]]] = {}
    flags: list[str] = []
    for sector_index in range(n_sites):
        phase = sector_phase(sector_index, n_sites)
        vals, vecs, pflags = projected_eigenpairs(matrix, translation, phase, NEIG, salt_base + 101 * (sector_index + 1))
        raw[sector_index] = (vals, vecs, pflags)
        flags.extend(f"s{sector_index}:{flag}" for flag in pflags)
    return raw, flags


def compute_point(n_sites: int, w_max: int, mass: float, coupling: float, reported_only: bool, salt_base: int) -> PointResult:
    basis, translation = setup(n_sites, w_max)
    matrix = hamiltonian(n_sites, w_max, mass, coupling)
    raw, flags = compute_all_sector_eigenpairs(matrix, translation, n_sites, salt_base)
    ground_sector = min(raw, key=lambda sector: float(raw[sector][0][0]) if len(raw[sector][0]) else float("inf"))
    ground_vals, ground_vecs, _ground_flags = raw[ground_sector]
    ground_energy = float(ground_vals[0])
    ground_vector = ground_vecs[:, 0]

    p0_ps = normalized_weights(ground_vecs, pseudoscalar_tag_action(basis, ground_vector, 0.0))
    p0_scalar = normalized_weights(ground_vecs, scalar_tag_action(basis, ground_vector, 0.0))
    tag_roles_swapped, role_flags = decide_tag_roles(np.asarray(ground_vals - ground_energy, dtype=np.float64), p0_ps, p0_scalar)
    flags.extend(role_flags)

    sectors: list[SectorTag] = []
    for rel_index in range(n_sites):
        sector_index = (ground_sector + rel_index) % n_sites
        momentum = 2.0 * np.pi * rel_index / n_sites
        vals, vecs, _pflags = raw[sector_index]
        sector = select_sector_tag(
            basis,
            rel_index,
            sector_index,
            momentum,
            sector_phase(sector_index, n_sites),
            vals,
            vecs,
            ground_energy,
            ground_vector,
            tag_roles_swapped,
        )
        sectors.append(sector)
        flags.extend(sector.flags)

    band1_all = np.array([selected_gap(sector.gaps, sector.band1_index) for sector in sectors], dtype=np.float64)
    band2_all = np.array([selected_gap(sector.gaps, sector.band2_index) for sector in sectors], dtype=np.float64)
    band1_origin = discover_origin(band1_all)
    band2_origin = discover_origin(band2_all)
    for label, origin_info in (("BAND1", band1_origin), ("BAND2", band2_origin)):
        if not origin_info.clean:
            flags.append(f"{label}-ORIGIN-NONCLEAN(k*={origin_info.rel_index})")
        if math.isfinite(origin_info.asymmetry) and origin_info.asymmetry > ORIGIN_ASYMM_TOL:
            flags.append(f"{label}-ORIGIN-ASYMMETRIC({origin_info.asymmetry:.2e})")

    band1_fit_origin = band1_origin.rel_index if 0 <= band1_origin.rel_index < n_sites else 0
    band2_fit_origin = band2_origin.rel_index if 0 <= band2_origin.rel_index < n_sites else 0
    band1_used = own_frame_indices(band1_fit_origin, n_sites)
    band2_used = own_frame_indices(band2_fit_origin, n_sites)
    momenta = fit_momenta(n_sites)
    band1 = np.array([band1_all[rel_index] for rel_index in band1_used], dtype=np.float64)
    band2 = np.array([band2_all[rel_index] for rel_index in band2_used], dtype=np.float64)
    band1_min = float(band1_all[band1_fit_origin])
    band2_min = float(band2_all[band2_fit_origin])
    fit1 = least_squares_fit(momenta, band1)
    fit2 = least_squares_fit(momenta, band2)
    ratio_i = (fit2.m_comp / fit1.m_comp) * (fit1.e0 / fit2.e0) if fit1.m_comp != 0.0 and fit2.e0 != 0.0 else float("nan")
    c21 = fit2.c2 / fit1.c2 if fit1.c2 != 0.0 else float("nan")
    threshold_included = bool(math.isfinite(fit1.e0) and math.isfinite(fit2.e0) and fit2.e0 < 2.0 * fit1.e0)
    origin_valid = bool(band1_origin.clean and band2_origin.clean)
    tag_valid = bool(
        all(sectors[rel_index].band1_valid for rel_index in band1_used)
        and all(sectors[rel_index].band2_valid for rel_index in band2_used)
    )
    tag_valid_band2 = bool(all(sectors[rel_index].band2_valid for rel_index in band2_used))
    fit_valid = bool(fit1.residual <= FIT_RES1_TOL and fit2.residual <= FIT_RES2_TOL)
    if ground_sector != 0:
        flags.append(f"momentum-ground-sector={ground_sector}")
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
        ground_sector=ground_sector,
        tag_roles_swapped=tag_roles_swapped,
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


def compute_n10_spot(salt_base: int) -> N10SpotResult:
    n_sites = N10_SPOT
    basis, translation = setup(n_sites, W_MAX)
    matrix = hamiltonian(n_sites, W_MAX, N10_SPOT_MASS, N10_SPOT_COUPLING)
    raw: dict[int, tuple[np.ndarray, np.ndarray, list[str]]] = {}
    flags: list[str] = []
    for rel_index in N10_SPOT_REL_INDICES:
        phase = sector_phase(rel_index, n_sites)
        vals, vecs, pflags = projected_eigenpairs(
            matrix,
            translation,
            phase,
            NEIG,
            salt_base + 101 * (rel_index + 1),
        )
        raw[rel_index] = (vals, vecs, pflags)
        flags.extend(f"s{rel_index}:{flag}" for flag in pflags)

    ground_sector = 0
    ground_vals, ground_vecs, _ground_flags = raw[ground_sector]
    ground_energy = float(ground_vals[0])
    ground_vector = ground_vecs[:, 0]

    p0_ps = normalized_weights(ground_vecs, pseudoscalar_tag_action(basis, ground_vector, 0.0))
    p0_scalar = normalized_weights(ground_vecs, scalar_tag_action(basis, ground_vector, 0.0))
    tag_roles_swapped, role_flags = decide_tag_roles(np.asarray(ground_vals - ground_energy, dtype=np.float64), p0_ps, p0_scalar)
    flags.extend(role_flags)

    sectors: list[SectorTag] = []
    for rel_index in N10_SPOT_REL_INDICES:
        vals, vecs, _pflags = raw[rel_index]
        sector = select_sector_tag(
            basis,
            rel_index,
            rel_index,
            2.0 * np.pi * rel_index / n_sites,
            sector_phase(rel_index, n_sites),
            vals,
            vecs,
            ground_energy,
            ground_vector,
            tag_roles_swapped,
        )
        sectors.append(sector)
        flags.extend(sector.flags)

    band1 = np.array([selected_gap(sector.gaps, sector.band1_index) for sector in sectors], dtype=np.float64)
    band2 = np.array([selected_gap(sector.gaps, sector.band2_index) for sector in sectors], dtype=np.float64)
    if not (len(band1) > 1 and math.isfinite(float(band1[0])) and math.isfinite(float(band1[1])) and band1[1] > band1[0]):
        flags.append("N10-BAND1-K1-NOT-ABOVE-K0")
    if not (len(band2) > 1 and math.isfinite(float(band2[0])) and math.isfinite(float(band2[1])) and band2[1] > band2[0]):
        flags.append("N10-BAND2-K1-NOT-ABOVE-K0")

    momenta = 2.0 * np.pi * np.asarray(N10_SPOT_REL_INDICES, dtype=np.float64) / n_sites
    fit1 = least_squares_fit(momenta, band1)
    fit2 = least_squares_fit(momenta, band2)
    ratio_i = (fit2.m_comp / fit1.m_comp) * (fit1.e0 / fit2.e0) if fit1.m_comp != 0.0 and fit2.e0 != 0.0 else float("nan")
    c21 = fit2.c2 / fit1.c2 if fit1.c2 != 0.0 else float("nan")
    threshold_included = bool(math.isfinite(fit1.e0) and math.isfinite(fit2.e0) and fit2.e0 < 2.0 * fit1.e0)
    tag_valid = bool(all(sector.band1_valid and sector.band2_valid for sector in sectors))
    tag_valid_band2 = bool(all(sector.band2_valid for sector in sectors))
    fit_valid = bool(fit1.residual <= FIT_RES1_TOL and fit2.residual <= FIT_RES2_TOL)
    k1_rise_valid = not any(flag in flags for flag in ("N10-BAND1-K1-NOT-ABOVE-K0", "N10-BAND2-K1-NOT-ABOVE-K0"))
    if not threshold_included:
        flags.append("THRESHOLD-EXCLUDED")
    if not fit_valid:
        flags.append("FIT-EXCLUDED")

    return N10SpotResult(
        n_sites=n_sites,
        w_max=W_MAX,
        mass=N10_SPOT_MASS,
        coupling=N10_SPOT_COUPLING,
        momenta=momenta,
        ground_energy=ground_energy,
        ground_sector=ground_sector,
        tag_roles_swapped=tag_roles_swapped,
        sectors=sectors,
        band1_energies=band1,
        band2_energies=band2,
        fit1=fit1,
        fit2=fit2,
        ratio_i=float(ratio_i),
        c21=float(c21),
        threshold_included=threshold_included,
        tag_valid=tag_valid,
        tag_valid_band2=tag_valid_band2,
        fit_valid=fit_valid,
        k1_rise_valid=k1_rise_valid,
        flags=flags,
    )


def parse_float_array(text: str) -> np.ndarray:
    if not text.strip():
        return np.zeros(0, dtype=np.float64)
    return np.asarray([float(piece) for piece in text.split(",") if piece.strip()], dtype=np.float64)


def parse_engine_cache() -> dict[float, dict[str, np.ndarray | float]]:
    if not CACHE_PATH.exists():
        return {}
    text = CACHE_PATH.read_text(encoding="utf-8")
    out: dict[float, dict[str, np.ndarray | float]] = {}
    pattern = re.compile(
        r"MESON\s+g=([0-9.]+)\s+P0=\[([^\]]+)\]\s+P=2pi/8=\[([^\]]+)\]\s+"
        r"band2=\(P0:([^,]+),P2pi8:([^)]+)\)"
    )
    for match in pattern.finditer(text):
        coupling = float(match.group(1))
        out[coupling] = {
            "P0": parse_float_array(match.group(2)),
            "P2pi8": parse_float_array(match.group(3)),
            "band2_P0": float(match.group(4)),
            "band2_P2pi8": float(match.group(5)),
        }
    return out


def compute_engine_meson_block(coupling: float, salt_base: int) -> dict[str, np.ndarray | float | int]:
    n_sites = N_MAIN
    basis, translation = setup(n_sites, W_MAX)
    del basis
    matrix = hamiltonian(n_sites, W_MAX, CACHE_MASS, coupling)
    raw, _flags = compute_all_sector_eigenpairs(matrix, translation, n_sites, salt_base)
    ground_sector = min(raw, key=lambda sector: float(raw[sector][0][0]) if len(raw[sector][0]) else float("inf"))
    ground = float(raw[ground_sector][0][0])
    p0_vals = raw[ground_sector][0]
    p1_vals = raw[(ground_sector + 1) % n_sites][0]
    p0_excitations = np.asarray(p0_vals[1:5] - ground, dtype=np.float64)
    p1_excitations = np.asarray(p1_vals[:4] - ground, dtype=np.float64)
    return {
        "ground_sector": ground_sector,
        "P0": p0_excitations,
        "P2pi8": p1_excitations,
        "band2_P0": float(p0_excitations[1]) if len(p0_excitations) > 1 else float("nan"),
        "band2_P2pi8": float(p1_excitations[1]) if len(p1_excitations) > 1 else float("nan"),
    }


def check_01_engine_repro() -> tuple[bool, str]:
    cache = parse_engine_cache()
    worst = 0.0
    details: list[str] = []
    ok = True
    for offset, coupling in enumerate(CACHE_COUPLINGS):
        cached = cache.get(coupling)
        if cached is None:
            ok = False
            details.append(f"g={coupling}:cache-missing")
            continue
        block = compute_engine_meson_block(coupling, 900000 + 10000 * offset)
        p0_cached = np.asarray(cached["P0"], dtype=np.float64)
        p0_got = np.asarray(block["P0"], dtype=np.float64)
        if len(p0_cached) < 4 or len(p0_got) < 4:
            ok = False
            details.append(f"g={coupling}:P0-short")
            continue
        p0_err = float(np.max(np.abs(p0_got[:4] - p0_cached[:4])))
        band2_err = max(
            abs(float(block["band2_P0"]) - float(cached["band2_P0"])),
            abs(float(block["band2_P2pi8"]) - float(cached["band2_P2pi8"])),
        )
        local_worst = max(p0_err, band2_err)
        worst = max(worst, local_worst)
        if local_worst > CACHE_PRINT_TOL:
            ok = False
        details.append(
            f"g={coupling}:P0err={p0_err:.1e},band2err={band2_err:.1e},"
            f"ground_sector={int(block['ground_sector'])}"
        )
    return ok and worst <= CACHE_PRINT_TOL, (
        f"cache={CACHE_PATH.name},CACHE_PRINT_TOL={CACHE_PRINT_TOL:.0e},"
        f"print_precision_regression,worst={worst:.1e};"
    ) + "|".join(details)


def attach_stability(main_points: list[PointResult], stability_points: dict[tuple[float, float], PointResult]) -> None:
    for point in main_points:
        if point.reported_only:
            continue
        small = stability_points[(point.mass, point.coupling)]
        point.drift_i = abs(small.ratio_i - point.ratio_i)
        band1_stable = origin_location_stable(point.band1_origin_rel, point.n_sites, small.band1_origin_rel, small.n_sites)
        band2_stable = origin_location_stable(point.band2_origin_rel, point.n_sites, small.band2_origin_rel, small.n_sites)
        point.origin_stable = bool(band1_stable and band2_stable)
        point.origin_stability_detail = (
            f"N{point.n_sites}=({point.band1_origin_rel},{point.band2_origin_rel})/"
            f"N{small.n_sites}=({small.band1_origin_rel},{small.band2_origin_rel})"
        )
        point.flags.append(
            f"{'ORIGIN-STABLE' if point.origin_stable else 'ORIGIN-UNSTABLE'}({point.origin_stability_detail})"
        )
        point.stability_valid = bool(point.drift_i <= STABILITY_TOL)
        point.stability_leg = "N6" if point.stability_valid else "NONE"


def apply_n10_spot_stability(point: PointResult, spot: N10SpotResult, drift: float) -> None:
    point.n10_drift_i = drift
    n10_ok = bool(math.isfinite(drift) and drift <= N10_SPOT_TOL)
    point.flags.append(
        f"N10-SPOT({'STABLE' if n10_ok else 'UNSTABLE'}):"
        f"drift={finite_float(drift,4)},tag={'Y' if spot.tag_valid else 'N'},"
        f"fit={'Y' if spot.fit_valid else 'N'},rise={'Y' if spot.k1_rise_valid else 'N'}"
    )
    if not n10_ok:
        return
    if point.stability_valid and point.stability_leg != "NONE":
        point.stability_leg = f"{point.stability_leg}+N10"
    else:
        point.stability_valid = True
        point.stability_leg = "N10"


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
    gated = [point for point in points if not point.reported_only]
    valid = [point for point in gated if point.tag_valid and point.origin_valid]
    bad = [point for point in gated if not (point.tag_valid and point.origin_valid)]
    detail = f"N={N_MAIN},tag_plus_origin_clean={len(valid)}/{len(gated)}"
    if bad:
        detail += ";invalid=" + ",".join(f"m={point.mass},g={point.coupling}" for point in bad)
    return len(valid) >= 5, detail


def check_03_window_trend_identity(points: list[PointResult]) -> tuple[bool, str]:
    details: list[str] = []
    ok = True
    for mass in GRID_MASSES:
        valid = sorted(
            [point for point in points if point.mass == mass and gate_included(point) and math.isfinite(point.c21)],
            key=lambda point: point.coupling,
        )
        if len(valid) < 2:
            ok = False
            details.append(f"m={mass}:FAIL(valid_couplings={len(valid)}<2)")
            continue
        violations: list[tuple[float, float, float]] = []
        for weaker, stronger in zip(valid, valid[1:]):
            weaker_dev = abs(weaker.c21 - 1.0)
            stronger_dev = abs(stronger.c21 - 1.0)
            growth = stronger_dev - weaker_dev
            if growth > 1.0e-12:
                violations.append((weaker.coupling, stronger.coupling, growth))
        large_violations = [violation for violation in violations if violation[2] > 0.02 + 1.0e-12]
        trend_ok = not large_violations and len(violations) <= 1
        strongest = max(valid, key=lambda point: point.coupling)
        strongest_dev = abs(strongest.c21 - 1.0)
        strongest_ok = strongest_dev <= IDENTITY_TOL
        if not trend_ok or not strongest_ok:
            ok = False
        series = "<".join(
            f"g={point.coupling}:dev={abs(point.c21 - 1.0):.4g},c21={point.c21:.4g},ratio_I={point.ratio_i:.4g}"
            for point in valid
        )
        violation_text = "none" if not violations else ",".join(
            f"g{lo}->g{hi}:dev_growth={growth:.3g}" for lo, hi, growth in violations
        )
        details.append(
            f"m={mass}:WINDOW-TREND series_asc_g={series},violations={violation_text},"
            f"strongest=g={strongest.coupling}:dev={strongest_dev:.3g},valid={len(valid)}"
        )
    return ok, ";".join(details)


def check_04_wilson_oa_artifact(points: list[PointResult]) -> tuple[bool, str]:
    reports: list[str] = []
    for point in points:
        free_c2 = 1.0 + point.mass
        reports.append(
            f"m={point.mass},g={point.coupling}:free_c2=1+m~{free_c2:.4g},"
            f"b1(E0sq={finite_float(point.fit1.e0 * point.fit1.e0,5)},c2={finite_float(point.fit1.c2,5)}),"
            f"b2(E0sq={finite_float(point.fit2.e0 * point.fit2.e0,5)},c2={finite_float(point.fit2.c2,5)})"
        )
    return True, "WILSON-OA-ARTIFACT ungated,free_level_c2(g->0)~1+m,no_through_origin_fit;" + "|".join(reports)


def check_04b_cross_species_band2_metric(points: list[PointResult]) -> tuple[bool, str]:
    by_key = {(point.mass, point.coupling): point for point in points}
    strongest_valid: tuple[float, float] | None = None
    details: list[str] = []
    for coupling in sorted(ALL_COUPLINGS):
        low = by_key.get((GRID_MASSES[0], coupling))
        high = by_key.get((GRID_MASSES[1], coupling))
        if low is None or high is None:
            continue
        ratio = low.fit2.c2 / high.fit2.c2 if high.fit2.c2 != 0.0 else float("inf")
        both_valid = gate_included(low) and gate_included(high)
        zone = "gated" if coupling in GATED_COUPLINGS else "reported"
        details.append(f"g={coupling}:{zone},ratio={finite_float(ratio,5)},valid={'Y' if both_valid else 'N'}")
        if coupling in GATED_COUPLINGS and both_valid:
            strongest_valid = (coupling, float(ratio))
    if strongest_valid is None:
        return False, "no-coupling-with-both-species-valid;" + "|".join(details)
    strongest_coupling, strongest_ratio = strongest_valid
    dev = abs(strongest_ratio - 1.0)
    ok = bool(math.isfinite(dev) and dev <= SPECIES_METRIC_TOL)
    return ok, f"strongest_valid_g={strongest_coupling},dev={dev:.3g};" + "|".join(details)


def check_05_fit_honesty(points: list[PointResult]) -> tuple[bool, str]:
    gated = [point for point in points if not point.reported_only and point.tag_valid]
    excluded = [point for point in gated if not point.fit_valid]
    details = [
        f"m={point.mass},g={point.coupling}:res=({point.fit1.residual:.1e},{point.fit2.residual:.1e})"
        f"{'-EXCL' if not point.fit_valid else ''}"
        for point in gated
    ]
    return True, "self_exclusion=fit_invalid,excluded=" + str(len(excluded)) + ";" + ",".join(details)


def check_06_stability(points: list[PointResult], w_spot_drift: float, w_spot_valid: bool) -> tuple[bool, str]:
    gated = [point for point in points if not point.reported_only]
    stable = [point for point in gated if point.stability_valid]
    drift_detail = ",".join(
        f"m={point.mass},g={point.coupling}:driftN6={finite_float(point.drift_i,4)},"
        f"driftN10={finite_float(point.n10_drift_i,4)},leg={point.stability_leg},"
        f"stable={'Y' if point.stability_valid else 'N'},"
        f"origin={'ORIGIN-STABLE' if point.origin_stable else 'ORIGIN-UNSTABLE'}({point.origin_stability_detail})"
        for point in gated
    )
    ok = bool(w_spot_valid and w_spot_drift <= W_SPOT_TOL and len(stable) >= 3)
    return ok, (
        f"COARSE-N6-FITS,stable={len(stable)}/{len(gated)},"
        f"Wspot(m={W_SPOT_MASS},g={W_SPOT_COUPLING})={w_spot_drift:.3g},"
        f"WspotTag={'Y' if w_spot_valid else 'N'};{drift_detail}"
    )


def check_07_n10_spot(n8_point: PointResult, spot: N10SpotResult) -> tuple[bool, str, float]:
    drift = abs(spot.ratio_i - n8_point.ratio_i)
    ok = bool(math.isfinite(drift) and drift <= N10_SPOT_TOL)
    flags = "none" if not spot.flags else ",".join(spot.flags)
    detail = (
        f"N={spot.n_sites},W_MAX={spot.w_max},m={spot.mass},g={spot.coupling},"
        f"rel_k={','.join(str(k) for k in N10_SPOT_REL_INDICES)},momenta=2pi*d/{spot.n_sites},"
        f"ratio_I(N8)={finite_float(n8_point.ratio_i,6)},ratio_I(N10)={finite_float(spot.ratio_i,6)},"
        f"drift={finite_float(drift,4)},tol={N10_SPOT_TOL:.2f},"
        f"c21(N8)={finite_float(n8_point.c21,6)},c21(N10)={finite_float(spot.c21,6)},"
        f"E_k1_gt_k0={'Y' if spot.k1_rise_valid else 'N'},"
        f"tagN10={'Y' if spot.tag_valid else 'N'},fitN10={'Y' if spot.fit_valid else 'N'},"
        f"flags={flags}"
    )
    return ok, detail, float(drift)


def used_rel_indices(point: PointResult) -> tuple[int, ...]:
    return tuple(sorted(set(point.band1_used_rel_indices + point.band2_used_rel_indices)))


def weights_table(point: PointResult) -> str:
    chunks: list[str] = []
    for rel_index in used_rel_indices(point):
        sector = point.sectors[rel_index]
        psw = ",".join(f"{weight:.2g}" for weight in sector.ps_weights)
        sw = ",".join(f"{weight:.2g}" for weight in sector.scalar_weights)
        chunks.append(f"k{sector.rel_index}:PS[{psw}]S[{sw}]")
    return "weights={" + "/".join(chunks) + "}"


def result_fragment(point: PointResult) -> str:
    status = ["REPORTED-ONLY" if point.reported_only else "GATED"]
    status.append("ORG-Y" if point.origin_valid else "ORIGIN-NONCLEAN")
    status.append("TAG-Y" if point.tag_valid else "TAG-N")
    status.append("STAB-Y" if point.stability_valid else "STAB-N")
    status.append("THR-Y" if point.threshold_included else "THRESHOLD-EXCLUDED")
    status.append("FIT-Y" if point.fit_valid else "FIT-EXCLUDED")
    if point.tag_roles_swapped:
        status.append("TAG-ROLES-SWAPPED")
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
        f"thr=E02/{finite_float(2.0 * point.fit1.e0)}={finite_float(point.fit2.e0)},"
        f"margin={finite_float(2.0 * point.fit1.e0 - point.fit2.e0)},"
        f"driftI_N6={finite_float(point.drift_i,4)},"
        f"driftI_N10={finite_float(point.n10_drift_i,4)},"
        f"stability_leg={point.stability_leg},"
        f"status={'+'.join(status)}"
    )
    if not point.tag_valid:
        text += "," + weights_table(point)
    return text


def tags_fragment(point: PointResult) -> str:
    b1_agrees = ",".join(
        f"k{sector.rel_index}:{'Y' if sector.band1_index == sector.energy_order_band1 else 'N'}"
        for sector in (point.sectors[rel_index] for rel_index in point.band1_used_rel_indices)
    )
    b2_agrees = ",".join(
        f"k{sector.rel_index}:{'Y' if sector.band2_index == sector.energy_order_band2 else 'N'}"
        for sector in (point.sectors[rel_index] for rel_index in point.band2_used_rel_indices)
    )
    b1_dom = ",".join(
        f"k{sector.rel_index}:{sector.band1_tag}3={finite_float(sector.band1_dominance,3)}"
        for sector in (point.sectors[rel_index] for rel_index in point.band1_used_rel_indices)
    )
    b2_dom = ",".join(
        f"k{sector.rel_index}:{sector.band2_tag}3={finite_float(sector.band2_dominance,3)},"
        f"{sector.band2_tag}2{sector.band1_tag}1={finite_float(sector.band2_over_band1_owntag,3)}"
        for sector in (point.sectors[rel_index] for rel_index in point.band2_used_rel_indices)
    )
    collisions = sum(1 for rel_index in used_rel_indices(point) if point.sectors[rel_index].collision)
    chosen_b1 = ",".join(
        f"k{sector.rel_index}:i{sector.band1_index}" for sector in (point.sectors[rel_index] for rel_index in point.band1_used_rel_indices)
    )
    chosen_b2 = ",".join(
        f"k{sector.rel_index}:i{sector.band2_index}" for sector in (point.sectors[rel_index] for rel_index in point.band2_used_rel_indices)
    )
    role = "S/PS TAG-ROLES-SWAPPED" if point.tag_roles_swapped else "PS/S"
    return (
        f"m={point.mass},g={point.coupling}:valid={'Y' if point.tag_valid else 'N'},"
        f"role={role},origin={'Y' if point.origin_valid else 'N'},kstar=({point.band1_origin_rel},{point.band2_origin_rel}),"
        f"b1idx={{{chosen_b1}}},b2idx={{{chosen_b2}}},"
        f"agree=({{{b1_agrees}}};{{{b2_agrees}}}),dom=({{{b1_dom}}};{{{b2_dom}}}),"
        f"collisions={collisions}"
    )


def band2_zone_from_point(point: PointResult) -> ZoneResult:
    return ZoneResult(
        mass=point.mass,
        coupling=point.coupling,
        ground_sector=point.ground_sector,
        sector_indices=[sector.sector_index for sector in point.sectors],
        band2_energies=point.band2_all_energies,
        minimum_rel_index=point.band2_origin_rel,
    )


def zone_fragment(zone: ZoneResult) -> str:
    entries = ",".join(
        f"k{k}/s{sector}:E={finite_float(float(energy),7)}"
        for k, (sector, energy) in enumerate(zip(zone.sector_indices, zone.band2_energies))
    )
    minimum_energy = (
        float(zone.band2_energies[zone.minimum_rel_index])
        if 0 <= zone.minimum_rel_index < len(zone.band2_energies)
        else float("nan")
    )
    surprise = "" if zone.minimum_rel_index == 0 else ":WILSON-ZONE-SURPRISE"
    return (
        f"m={zone.mass},g={zone.coupling},ground_sector={zone.ground_sector}:"
        f"{entries};min=k{zone.minimum_rel_index},E={finite_float(minimum_energy,7)}{surprise}"
    )


def gather_total_flags(points: list[PointResult], zones: list[ZoneResult], w_spot_drift: float, n10_spot_drift: float) -> list[str]:
    origin_split = "|".join(
        f"m={point.mass},g={point.coupling}:({point.band1_origin_rel},{point.band2_origin_rel})"
        for point in points
    )
    swapped = [f"m={point.mass},g={point.coupling}" for point in points if point.tag_roles_swapped]
    surprises = [f"m={zone.mass},g={zone.coupling}:k2*={zone.minimum_rel_index}" for zone in zones if zone.minimum_rel_index != 0]
    flags = [
        f"note={NOTE_NAME}",
        "Q0-ring-Gauss",
        "finite-W-magnetic-translation",
        "Wilson-full-zone-theta=P",
        "operator-tagged-own-frame",
        "GATED_COUPLINGS=1.0/1.2/1.4/1.7",
        "REPORTED_ONLY_COUPLINGS=0.6/2.0",
        "COARSE-N6-FITS",
        f"ORIGIN-SPLIT[{origin_split}]",
        f"Wspot(m={W_SPOT_MASS},g={W_SPOT_COUPLING})-drift={w_spot_drift:.3g}",
        f"N10spot(m={N10_SPOT_MASS},g={N10_SPOT_COUPLING})-drift={n10_spot_drift:.3g}",
    ]
    if swapped:
        flags.append("TAG-ROLES-SWAPPED[" + "|".join(swapped) + "]")
    if surprises:
        flags.append("WILSON-ZONE-SURPRISE[" + "|".join(surprises) + "]")
    for point in points:
        flags.extend(f"m={point.mass},g={point.coupling}:{flag}" for flag in point.flags)
    return flags


def spec_note() -> str:
    return (
        "SPEC-NOTE "
        "O_PS(P) and O_S(P) are literal prompt bilinears; for P!=0 they are not Hermitian by themselves "
        "(O(P)^dag=O(-P)), and weights use O(P)|Omega> without symmetrizing; "
        "Wilson momentum uses full-site theta=P with sectors ground+k, not staggered theta=2P; "
        "PS/S roles are swapped only when the P=0 lower-energy tagged assignment requires it; "
        "threshold E02<2E01 is a finite-spectrum gate, not a continuum proof."
    )


def verdict_flag(ok02: bool, passed: bool) -> str:
    if not ok02:
        return "TAGGING-FAILED"
    if passed:
        return "IDENTITY-GATED"
    return "IDENTITY-MIXED"


def main() -> int:
    started = time.time()
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

    w4 = next(point for point in main_points if point.mass == W_SPOT_MASS and point.coupling == W_SPOT_COUPLING)
    salt += 1
    w5 = compute_point(N_MAIN, W_SPOT, W_SPOT_MASS, W_SPOT_COUPLING, reported_only=True, salt_base=10000 * salt)
    w_spot_drift = float(np.max(np.abs(w5.band2_all_energies - w4.band2_all_energies)))
    w_spot_valid = bool(w4.tag_valid_band2 and w5.tag_valid_band2)

    zone_points = [
        next(point for point in main_points if point.mass == 0.2 and point.coupling == 1.0),
        next(point for point in main_points if point.mass == 0.2 and point.coupling == 1.4),
    ]
    zones = [band2_zone_from_point(point) for point in zone_points]

    ok01, detail01 = check_01_engine_repro()
    ok02, detail02 = check_02_tag_method(main_points)
    ok04, detail04 = check_04_wilson_oa_artifact(main_points)
    ok05, detail05 = check_05_fit_honesty(main_points)

    print("TAGS " + "; ".join(tags_fragment(point) for point in main_points), flush=True)
    print("ZONE " + "; ".join(zone_fragment(zone) for zone in zones), flush=True)
    print(spec_note(), flush=True)

    n8_spot = next(point for point in main_points if point.mass == N10_SPOT_MASS and point.coupling == N10_SPOT_COUPLING)
    salt += 1
    n10_spot = compute_n10_spot(salt_base=10000 * salt)
    ok07, detail07, n10_spot_drift = check_07_n10_spot(n8_spot, n10_spot)
    apply_n10_spot_stability(n8_spot, n10_spot, n10_spot_drift)

    ok03, detail03 = check_03_window_trend_identity(main_points)
    ok04b, detail04b = check_04b_cross_species_band2_metric(main_points)
    ok06, detail06 = check_06_stability(main_points, w_spot_drift, w_spot_valid)
    checks = [
        ("CHECK-01", ok01, detail01),
        ("CHECK-02", ok02, detail02),
        ("CHECK-03", ok03, detail03),
        ("CHECK-04", ok04, detail04),
        ("CHECK-04b", ok04b, detail04b),
        ("CHECK-05", ok05, detail05),
        ("CHECK-06", ok06, detail06),
        ("CHECK-07", ok07, detail07),
    ]
    passed = all(ok for _name, ok, _detail in checks)
    elapsed = time.time() - started
    verdict = verdict_flag(ok02, passed)
    status = "PASS" if passed else "FAIL"

    print("RESULTS " + "; ".join(result_fragment(point) for point in main_points), flush=True)
    print("CHECKS " + "; ".join(f"{name}={'ok' if ok else 'FAIL'}({detail})" for name, ok, detail in checks), flush=True)
    print(
        f"TOTAL {status} {verdict} elapsed={elapsed:.2f}s flags="
        + ",".join(gather_total_flags(main_points, zones, w_spot_drift, n10_spot_drift)),
        flush=True,
    )
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
