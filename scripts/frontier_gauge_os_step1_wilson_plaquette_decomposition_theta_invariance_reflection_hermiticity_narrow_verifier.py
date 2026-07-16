#!/usr/bin/env python3
"""Finite SU(3) verifier for the repaired Gauge OS Step 1 narrow theorem.

The tested theorem is deliberately restricted to the trivial temporal
Polyakov-holonomy, U_0=I sector.  It separates:

* the exact Wilson-action split on a finite even periodic carrier;
* the criterion and construction for periodic complete temporal gauge;
* a worked raw-link support witness for one declared f from the still-open
  downstream positive-half admissibility bridge;
* reflection-Hermiticity only for the explicitly symmetrized class
  F = f + conj(f o Theta).

Hostile controls are computational: nontrivial temporal holonomy, a missing
periodic-wrap plaquette family, a wrong temporal reflection orientation, a
negative-half leak into f, an unsymmetrized reflection-Hermiticity overclaim,
and the attempted classification of F as plus-local.  The source-scope gate
parses an exact export contract and discovers direct consumers from the tracked
sharded ledger without reading or pinning audit outcomes.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Callable, Iterable

import numpy as np


PASS = 0
FAIL = 0
LOG: list[str] = []

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = (
    "gauge_os_step1_wilson_plaquette_decomposition_theta_invariance_"
    "reflection_hermiticity_narrow_theorem_note_2026-06-02"
)

L_T = 4
L_S = 2
N_C = 3
BETA = 1.75
SEED = 20260602
TOL = 1.0e-10
DTYPE = np.complex128

Site = tuple[int, int, int, int]
Plaquette = tuple[int, int, int, int, int, int]
LinkKey = tuple[int, int, int, int, int]
Observable = Callable[[np.ndarray], complex]

EXPECTED_EXPORT_CONTRACT = {
    "carrier": "finite periodic L_t=2n>=4 and L_s>=2",
    "group_and_action": "pure-gauge SU(N_c) Wilson plaquette action",
    "sector": (
        "configurations already satisfying U_0=I; periodic construction from "
        "an unfixed configuration requires P(x)=I at every spatial site"
    ),
    "proved": [
        (
            "P_+, P_-, and the two-boundary P_mixed form a disjoint exhaustive "
            "plaquette partition and "
            "S_W(U)=S_+(U)+S_+(Theta U)+S_mixed(U)"
        ),
        (
            "the half-actions are real and S_+(Theta U)=S_+(U) on Theta-fixed "
            "configurations"
        ),
        (
            "F_f=f+conj(f o Theta) is reflection-Hermitian for the explicitly "
            "symmetrized observable class"
        ),
    ],
    "worked_witness_only": (
        "one declared spatial plaquette has raw link support contained in E_+"
    ),
    "open_downstream_bridge": (
        "positive-half localization and admissibility of the actual observable "
        "consumed by any downstream OS argument"
    ),
}


def record(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        LOG.append(f"[PASS] {name}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"[FAIL] {name}" + (f"  ({detail})" if detail else ""))


def _random_su3(rng: np.random.Generator) -> np.ndarray:
    """Draw a reproducible SU(3) matrix from a complex Ginibre matrix."""
    a = rng.standard_normal((N_C, N_C)) + 1j * rng.standard_normal((N_C, N_C))
    q, r = np.linalg.qr(a)
    phases = np.diag(r)
    phases = phases / np.abs(phases)
    u = q @ np.diag(phases)
    u = u / np.linalg.det(u) ** (1.0 / N_C)
    return np.asarray(u, dtype=DTYPE)


def _identity_config() -> np.ndarray:
    shape = (L_T, L_S, L_S, L_S, 4, N_C, N_C)
    u = np.zeros(shape, dtype=DTYPE)
    u[...] = np.eye(N_C, dtype=DTYPE)
    return u


def _random_config(seed: int = SEED) -> np.ndarray:
    rng = np.random.default_rng(seed)
    u = _identity_config()
    for t in range(L_T):
        for x1 in range(L_S):
            for x2 in range(L_S):
                for x3 in range(L_S):
                    for mu in range(4):
                        u[t, x1, x2, x3, mu] = _random_su3(rng)
    return u


def _complete_temporal_gauge_config(seed: int = SEED) -> np.ndarray:
    """Random spatial links with U_0=I, inside the declared theorem sector."""
    u = _random_config(seed)
    u[:, :, :, :, 0] = np.eye(N_C, dtype=DTYPE)
    return u


def _trivial_holonomy_config(seed: int = SEED + 1) -> np.ndarray:
    """Build nontrivial temporal links whose ordered Polyakov product is I."""
    u = _random_config(seed)
    for x1 in range(L_S):
        for x2 in range(L_S):
            for x3 in range(L_S):
                product = np.eye(N_C, dtype=DTYPE)
                for t in range(L_T - 1):
                    product = product @ u[t, x1, x2, x3, 0]
                u[L_T - 1, x1, x2, x3, 0] = product.conj().T
    return u


def _nontrivial_holonomy_control() -> tuple[np.ndarray, np.ndarray]:
    """Exact SU(3) control with P=diag(-1,-1,1) at one spatial site."""
    u = _identity_config()
    h = np.diag([-1.0, -1.0, 1.0]).astype(DTYPE)
    u[L_T - 1, 0, 0, 0, 0] = h
    return u, h


def _extent(direction: int) -> int:
    return L_T if direction == 0 else L_S


def _shift(site: Site, direction: int, amount: int = 1) -> Site:
    coords = list(site)
    coords[direction] = (coords[direction] + amount) % _extent(direction)
    return tuple(coords)  # type: ignore[return-value]


def _physical_time(t_index: int) -> int:
    return t_index - L_T // 2


def _reflected_time_index(t_index: int) -> int:
    return (L_T - 1 - t_index) % L_T


def _all_sites() -> Iterable[Site]:
    for t in range(L_T):
        for x1 in range(L_S):
            for x2 in range(L_S):
                for x3 in range(L_S):
                    yield (t, x1, x2, x3)


def _all_plaquettes() -> list[Plaquette]:
    out: list[Plaquette] = []
    for t, x1, x2, x3 in _all_sites():
        for mu in range(4):
            for nu in range(mu + 1, 4):
                out.append((t, x1, x2, x3, mu, nu))
    return out


def _plaquette_holonomy(u: np.ndarray, p: Plaquette) -> np.ndarray:
    t, x1, x2, x3, mu, nu = p
    site = (t, x1, x2, x3)
    x_plus_mu = _shift(site, mu)
    x_plus_nu = _shift(site, nu)
    a = u[site + (mu,)]
    b = u[x_plus_mu + (nu,)]
    c = u[x_plus_nu + (mu,)].conj().T
    d = u[site + (nu,)].conj().T
    return a @ b @ c @ d


def _normalized_plaquette(u: np.ndarray, p: Plaquette) -> float:
    return float(np.real(np.trace(_plaquette_holonomy(u, p))) / N_C)


def _wilson_action(u: np.ndarray, plaquettes: Iterable[Plaquette]) -> float:
    return -BETA * sum(_normalized_plaquette(u, p) for p in plaquettes)


def _classify_plaquette(p: Plaquette) -> str:
    t, _, _, _, mu, _ = p
    t_phys = _physical_time(t)
    if mu != 0:
        return "plus" if t_phys >= 0 else "minus"
    if t_phys == -1:
        return "mixed_plane"
    if t_phys == L_T // 2 - 1:
        return "mixed_wrap"
    return "plus" if t_phys >= 0 else "minus"


def _partition(plaquettes: Iterable[Plaquette]) -> dict[str, list[Plaquette]]:
    parts = {
        "plus": [],
        "minus": [],
        "mixed_plane": [],
        "mixed_wrap": [],
    }
    for p in plaquettes:
        parts[_classify_plaquette(p)].append(p)
    return parts


def _classify_shape(t_index: int, mu: int, l_t: int) -> str:
    """Plaquette class for an arbitrary even temporal extent."""
    t_phys = t_index - l_t // 2
    if mu != 0:
        return "plus" if t_phys >= 0 else "minus"
    if t_phys == -1:
        return "mixed_plane"
    if t_phys == l_t // 2 - 1:
        return "mixed_wrap"
    return "plus" if t_phys >= 0 else "minus"


def _reflected_shape_class(t_index: int, mu: int, l_t: int) -> str:
    reflected_t = (l_t - 1 - t_index) % l_t
    if mu == 0:
        reflected_t = (reflected_t - 1) % l_t
    return _classify_shape(reflected_t, mu, l_t)


def _shape_partition_certificate(l_t: int, l_s: int) -> tuple[bool, str]:
    """Check the general count formulas and reflection classes by enumeration."""
    if l_t < 4 or l_t % 2:
        return False, f"invalid l_t={l_t}"
    counts = {
        "plus": 0,
        "minus": 0,
        "mixed_plane": 0,
        "mixed_wrap": 0,
    }
    class_map_ok = True
    for t in range(l_t):
        for _ in range(l_s**3):
            for mu in range(4):
                for _nu in range(mu + 1, 4):
                    cls = _classify_shape(t, mu, l_t)
                    counts[cls] += 1
                    reflected = _reflected_shape_class(t, mu, l_t)
                    expected = {
                        "plus": "minus",
                        "minus": "plus",
                        "mixed_plane": "mixed_plane",
                        "mixed_wrap": "mixed_wrap",
                    }[cls]
                    class_map_ok = class_map_ok and reflected == expected
    n = l_t // 2
    expected = {
        "plus": 3 * (2 * n - 1) * l_s**3,
        "minus": 3 * (2 * n - 1) * l_s**3,
        "mixed_plane": 3 * l_s**3,
        "mixed_wrap": 3 * l_s**3,
    }
    total_ok = sum(counts.values()) == 6 * l_t * l_s**3
    ok = counts == expected and total_ok and class_map_ok
    return (
        ok,
        (
            f"L_t={l_t}, L_s={l_s}, counts={counts}, "
            f"total_ok={total_ok}, theta_map={class_map_ok}"
        ),
    )


def _reflected_plaquette_class(p: Plaquette) -> str:
    """Class of the geometrically reflected plaquette.

    Spatial plaquettes move to r(t).  Temporal plaquettes reverse temporal
    orientation and, when rewritten in the standard positive-temporal
    orientation, are based at r(t)-1.
    """
    t, x1, x2, x3, mu, nu = p
    reflected_t = _reflected_time_index(t)
    if mu == 0:
        reflected_t = (reflected_t - 1) % L_T
    reflected = (reflected_t, x1, x2, x3, mu, nu)
    return _classify_plaquette(reflected)


def _reflect_config(u: np.ndarray) -> np.ndarray:
    """Correct OS link reflection through t=-1/2."""
    theta_u = np.zeros_like(u)
    for site in _all_sites():
        t, x1, x2, x3 = site
        t_ref = _reflected_time_index(t)
        for i in range(1, 4):
            theta_u[site + (i,)] = u[t_ref, x1, x2, x3, i]
        temporal_source = (t_ref - 1) % L_T
        theta_u[site + (0,)] = u[temporal_source, x1, x2, x3, 0].conj().T
    return theta_u


def _reflect_config_wrong_temporal_orientation(u: np.ndarray) -> np.ndarray:
    """Hostile rule: correct base point but missing temporal dagger."""
    theta_u = np.zeros_like(u)
    for site in _all_sites():
        t, x1, x2, x3 = site
        t_ref = _reflected_time_index(t)
        for i in range(1, 4):
            theta_u[site + (i,)] = u[t_ref, x1, x2, x3, i]
        temporal_source = (t_ref - 1) % L_T
        theta_u[site + (0,)] = u[temporal_source, x1, x2, x3, 0]
    return theta_u


def _max_link_difference(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.max(np.linalg.norm(a - b, axis=(-2, -1))))


def _polyakov_holonomy(u: np.ndarray, x1: int, x2: int, x3: int) -> np.ndarray:
    product = np.eye(N_C, dtype=DTYPE)
    for t in range(L_T):
        product = product @ u[t, x1, x2, x3, 0]
    return product


def _max_polyakov_identity_deviation(u: np.ndarray) -> float:
    identity = np.eye(N_C, dtype=DTYPE)
    deviation = 0.0
    for x1 in range(L_S):
        for x2 in range(L_S):
            for x3 in range(L_S):
                deviation = max(
                    deviation,
                    float(np.linalg.norm(_polyakov_holonomy(u, x1, x2, x3) - identity)),
                )
    return deviation


def _random_periodic_gauge(seed: int = SEED + 7) -> np.ndarray:
    rng = np.random.default_rng(seed)
    g = np.zeros((L_T, L_S, L_S, L_S, N_C, N_C), dtype=DTYPE)
    for site in _all_sites():
        g[site] = _random_su3(rng)
    return g


def _gauge_transform(u: np.ndarray, g: np.ndarray) -> np.ndarray:
    transformed = np.zeros_like(u)
    for site in _all_sites():
        for mu in range(4):
            endpoint = _shift(site, mu)
            transformed[site + (mu,)] = (
                g[site] @ u[site + (mu,)] @ g[endpoint].conj().T
            )
    return transformed


def _construct_complete_temporal_gauge(u: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    """Construct g(t+1)=g(t)U_0(t); valid only when every P is I."""
    if _max_polyakov_identity_deviation(u) >= TOL:
        raise ValueError("complete periodic temporal gauge requires P(x)=I")
    identity = np.eye(N_C, dtype=DTYPE)
    g = np.zeros((L_T, L_S, L_S, L_S, N_C, N_C), dtype=DTYPE)
    closure_deviation = 0.0
    for x1 in range(L_S):
        for x2 in range(L_S):
            for x3 in range(L_S):
                g[0, x1, x2, x3] = identity
                for t in range(L_T - 1):
                    g[t + 1, x1, x2, x3] = (
                        g[t, x1, x2, x3] @ u[t, x1, x2, x3, 0]
                    )
                endpoint = (
                    g[L_T - 1, x1, x2, x3]
                    @ u[L_T - 1, x1, x2, x3, 0]
                )
                closure_deviation = max(
                    closure_deviation,
                    float(np.linalg.norm(endpoint - identity)),
                )
    return _gauge_transform(u, g), g, closure_deviation


def _max_temporal_identity_deviation(u: np.ndarray) -> float:
    identity = np.eye(N_C, dtype=DTYPE)
    return max(
        float(np.linalg.norm(u[site + (0,)] - identity))
        for site in _all_sites()
    )


def _build_time_symmetric_config(seed: int = SEED + 2) -> np.ndarray:
    u = _complete_temporal_gauge_config(seed)
    for t in range(L_T):
        t_ref = _reflected_time_index(t)
        if t > t_ref:
            continue
        for x1 in range(L_S):
            for x2 in range(L_S):
                for x3 in range(L_S):
                    for i in range(1, 4):
                        u[t_ref, x1, x2, x3, i] = u[t, x1, x2, x3, i]
    return u


def _plaquette_support(p: Plaquette) -> set[LinkKey]:
    t, x1, x2, x3, mu, nu = p
    site = (t, x1, x2, x3)
    return {
        site + (mu,),
        _shift(site, mu) + (nu,),
        _shift(site, nu) + (mu,),
        site + (nu,),
    }


def _is_plus_dynamical_key(key: LinkKey) -> bool:
    t, _, _, _, mu = key
    return mu in (1, 2, 3) and _physical_time(t) >= 0


def _reflect_spatial_key(key: LinkKey) -> LinkKey:
    t, x1, x2, x3, mu = key
    if mu == 0:
        raise ValueError("the declared observable support contains only spatial links")
    return (_reflected_time_index(t), x1, x2, x3, mu)


P_PLUS: Plaquette = (L_T // 2, 0, 0, 0, 1, 2)
P_MINUS: Plaquette = (_reflected_time_index(L_T // 2), 0, 0, 0, 1, 2)
SUPPORT_F = _plaquette_support(P_PLUS)
SUPPORT_THETA_F = {_reflect_spatial_key(key) for key in SUPPORT_F}


def _f_plus(u: np.ndarray) -> complex:
    return complex(np.trace(_plaquette_holonomy(u, P_PLUS)) / N_C)


def _f_minus(u: np.ndarray) -> complex:
    return complex(np.trace(_plaquette_holonomy(u, P_MINUS)) / N_C)


def _theta_observable(f: Observable, u: np.ndarray) -> complex:
    return f(_reflect_config(u)).conjugate()


def _symmetrized_f(u: np.ndarray) -> complex:
    return _f_plus(u) + _theta_observable(_f_plus, u)


def _mutate_link(u: np.ndarray, key: LinkKey) -> np.ndarray:
    mutated = u.copy()
    h = np.diag([-1.0, -1.0, 1.0]).astype(DTYPE)
    mutated[key] = h @ mutated[key]
    return mutated


def part_a_carrier_and_decomposition() -> None:
    print("\n=== Part A: finite carrier, reflection, and Wilson decomposition ===")
    plaquettes = _all_plaquettes()
    parts = _partition(plaquettes)
    p_plus = parts["plus"]
    p_minus = parts["minus"]
    p_plane = parts["mixed_plane"]
    p_wrap = parts["mixed_wrap"]
    p_mixed = p_plane + p_wrap

    expected_total = 6 * L_T * L_S**3
    record(
        "A.carrier.plaquette_count",
        len(plaquettes) == expected_total == 192,
        f"count={len(plaquettes)}, formula=6*{L_T}*{L_S}^3={expected_total}",
    )
    record(
        "A.partition.exact_counts",
        (len(p_plus), len(p_minus), len(p_plane), len(p_wrap)) == (72, 72, 24, 24),
        (
            f"|P+|={len(p_plus)}, |P-|={len(p_minus)}, "
            f"|plane|={len(p_plane)}, |wrap|={len(p_wrap)}"
        ),
    )
    partition_sets = [set(p_plus), set(p_minus), set(p_plane), set(p_wrap)]
    union = set().union(*partition_sets)
    pairwise_disjoint = all(
        not (partition_sets[i] & partition_sets[j])
        for i in range(len(partition_sets))
        for j in range(i + 1, len(partition_sets))
    )
    record(
        "A.partition.disjoint_exhaustive",
        pairwise_disjoint and union == set(plaquettes),
        f"union={len(union)}, total={len(plaquettes)}, disjoint={pairwise_disjoint}",
    )
    class_map_ok = (
        all(_reflected_plaquette_class(p) == "minus" for p in p_plus)
        and all(_reflected_plaquette_class(p) == "plus" for p in p_minus)
        and all(_reflected_plaquette_class(p) == "mixed_plane" for p in p_plane)
        and all(_reflected_plaquette_class(p) == "mixed_wrap" for p in p_wrap)
    )
    record(
        "A.partition.theta_class_bijection",
        class_map_ok,
        "P+<->P-; reflection-plane and periodic-wrap families fixed setwise",
    )
    shape_certificates = [
        _shape_partition_certificate(l_t, l_s)
        for l_t in (4, 6, 8, 10)
        for l_s in (2, 3)
    ]
    record(
        "A.partition.even_periodic_formula_sweep",
        all(ok for ok, _ in shape_certificates),
        "; ".join(detail for _, detail in shape_certificates),
    )

    u = _complete_temporal_gauge_config()
    theta_u = _reflect_config(u)
    s_full = _wilson_action(u, plaquettes)
    s_plus = _wilson_action(u, p_plus)
    s_minus = _wilson_action(u, p_minus)
    s_mixed = _wilson_action(u, p_mixed)
    s_plus_theta = _wilson_action(theta_u, p_plus)
    record(
        "A.theta.complete_temporal_gauge_sector_stable",
        _max_temporal_identity_deviation(theta_u) < TOL,
        f"max ||(Theta U)_0-I||={_max_temporal_identity_deviation(theta_u):.3e}",
    )
    record(
        "A.action.disjoint_sum",
        abs(s_full - (s_plus + s_minus + s_mixed)) < TOL,
        f"diff={abs(s_full - (s_plus + s_minus + s_mixed)):.3e}",
    )
    record(
        "A.action.reflected_half",
        abs(s_minus - s_plus_theta) < TOL,
        f"|S--S+(Theta U)|={abs(s_minus - s_plus_theta):.3e}",
    )
    record(
        "A.action.decomposition",
        abs(s_full - (s_plus + s_plus_theta + s_mixed)) < TOL,
        f"diff={abs(s_full - (s_plus + s_plus_theta + s_mixed)):.3e}",
    )
    record(
        "A.action.half_reality",
        all(np.isreal(value) for value in (s_plus, s_minus, s_mixed)),
        f"S+={s_plus:.8f}, S-={s_minus:.8f}, Smixed={s_mixed:.8f}",
    )

    sector_generic = _complete_temporal_gauge_config(SEED + 3)
    sector_generic_theta = _reflect_config(sector_generic)
    sector_generic_theta2 = _reflect_config(sector_generic_theta)
    full_sector_generic = _wilson_action(sector_generic, plaquettes)
    full_sector_generic_theta = _wilson_action(sector_generic_theta, plaquettes)
    record(
        "A.theta.involution_u0_identity_sector",
        _max_link_difference(sector_generic_theta2, sector_generic) < TOL,
        (
            "max_link_diff="
            f"{_max_link_difference(sector_generic_theta2, sector_generic):.3e}"
        ),
    )
    record(
        "A.action.full_theta_invariance_u0_identity_sector",
        abs(full_sector_generic - full_sector_generic_theta) < TOL,
        (
            "|S(Theta U)-S(U)|="
            f"{abs(full_sector_generic_theta-full_sector_generic):.3e}"
        ),
    )

    symmetric = _build_time_symmetric_config()
    symmetric_theta = _reflect_config(symmetric)
    symmetric_s_plus = _wilson_action(symmetric, p_plus)
    symmetric_theta_s_plus = _wilson_action(symmetric_theta, p_plus)
    record(
        "A.action.theta_fixed_half_reality",
        np.isreal(symmetric_s_plus),
        f"S+={symmetric_s_plus:.8f}",
    )
    record(
        "A.action.theta_fixed_half_invariance",
        (
            _max_link_difference(symmetric, symmetric_theta) < TOL
            and abs(symmetric_s_plus - symmetric_theta_s_plus) < TOL
        ),
        f"max_link_diff={_max_link_difference(symmetric, symmetric_theta):.3e}",
    )


def part_b_temporal_holonomy() -> None:
    print("\n=== Part B: periodic complete temporal gauge criterion ===")
    plaquettes = _all_plaquettes()
    u = _trivial_holonomy_config()
    holonomy_deviation = _max_polyakov_identity_deviation(u)
    s_before = _wilson_action(u, plaquettes)
    gauge_fixed, _, closure_deviation = _construct_complete_temporal_gauge(u)
    s_after = _wilson_action(gauge_fixed, plaquettes)
    record(
        "B.trivial_holonomy.constructed",
        holonomy_deviation < TOL,
        f"max ||P-I||={holonomy_deviation:.3e}",
    )
    record(
        "B.periodic_recursion.closes",
        closure_deviation < TOL,
        f"max endpoint mismatch={closure_deviation:.3e}",
    )
    record(
        "B.complete_temporal_gauge.constructed",
        _max_temporal_identity_deviation(gauge_fixed) < TOL,
        f"max ||U0^g-I||={_max_temporal_identity_deviation(gauge_fixed):.3e}",
    )
    record(
        "B.gauge_transform.wilson_invariance",
        abs(s_before - s_after) < TOL,
        f"|S(U^g)-S(U)|={abs(s_after-s_before):.3e}",
    )

    control, h = _nontrivial_holonomy_control()
    p_control = _polyakov_holonomy(control, 0, 0, 0)
    trace_obstruction = abs(np.trace(p_control) - np.trace(np.eye(N_C))) > 1.0
    rejected = False
    try:
        _construct_complete_temporal_gauge(control)
    except ValueError:
        rejected = True
    record(
        "B.hostile.nontrivial_holonomy",
        np.linalg.norm(p_control - h) < TOL and trace_obstruction and rejected,
        (
            f"P=diag(-1,-1,1), Tr(P)={np.trace(p_control).real:.1f}, "
            f"Tr(I)={N_C}, constructor_rejected={rejected}"
        ),
    )

    periodic_g = _random_periodic_gauge()
    transformed_control = _gauge_transform(control, periodic_g)
    p_transformed = _polyakov_holonomy(transformed_control, 0, 0, 0)
    expected_conjugate = periodic_g[0, 0, 0, 0] @ h @ periodic_g[0, 0, 0, 0].conj().T
    record(
        "B.holonomy.periodic_gauge_conjugacy",
        (
            np.linalg.norm(p_transformed - expected_conjugate) < TOL
            and abs(np.trace(p_transformed) - np.trace(h)) < TOL
        ),
        (
            f"conjugacy_diff={np.linalg.norm(p_transformed-expected_conjugate):.3e}, "
            f"trace_diff={abs(np.trace(p_transformed)-np.trace(h)):.3e}"
        ),
    )


def part_c_localization_and_hermiticity() -> None:
    print("\n=== Part C: raw-link f witness versus symmetrized F ===")
    u = _complete_temporal_gauge_config(SEED + 4)
    theta_u = _reflect_config(u)
    support_f_plus = all(_is_plus_dynamical_key(key) for key in SUPPORT_F)
    support_theta_negative = all(
        not _is_plus_dynamical_key(key) for key in SUPPORT_THETA_F
    )
    record(
        "C.f.structural_plus_support",
        len(SUPPORT_F) == 4 and support_f_plus,
        f"supp(f)={sorted(SUPPORT_F)}",
    )
    record(
        "C.theta_f.structural_negative_support",
        len(SUPPORT_THETA_F) == 4 and support_theta_negative,
        f"supp(Theta f)={sorted(SUPPORT_THETA_F)}",
    )

    negative_key = sorted(SUPPORT_THETA_F)[0]
    mutated = _mutate_link(u, negative_key)
    f_before = _f_plus(u)
    f_after = _f_plus(mutated)
    record(
        "C.f.negative_mutation_independence",
        abs(f_after - f_before) < TOL,
        f"|f(U_mut)-f(U)|={abs(f_after-f_before):.3e}",
    )

    theta_f_u = _theta_observable(_f_plus, u)
    os_product = theta_f_u * f_before
    reflected_plaquette_product = _f_minus(u).conjugate() * f_before
    record(
        "C.os_form.independent_reflected_plaquette",
        abs(os_product - reflected_plaquette_product) < TOL,
        (
            "|Theta(f)f-conj(f_minus(U))f|="
            f"{abs(os_product-reflected_plaquette_product):.3e}"
        ),
    )

    f_full = _symmetrized_f(u)
    f_full_theta = _symmetrized_f(theta_u)
    record(
        "C.F.reflection_hermiticity",
        abs(f_full_theta - f_full.conjugate()) < TOL,
        f"|F(Theta U)-conj(F(U))|={abs(f_full_theta-f_full.conjugate()):.3e}",
    )
    unsymmetrized_gap = abs(_f_plus(theta_u) - _f_plus(u).conjugate())
    record(
        "C.hostile.unsymmetrized_f_not_reflection_hermitian",
        unsymmetrized_gap > 1.0e-8,
        f"|f(Theta U)-conj(f(U))|={unsymmetrized_gap:.3e}",
    )
    wrong_full_product = f_full.conjugate() * f_full
    record(
        "C.hostile.F_product_is_not_OS_f_product",
        abs(wrong_full_product - os_product) > 1.0e-8,
        f"|conj(F)F-Theta(f)f|={abs(wrong_full_product-os_product):.3e}",
    )

    support_f_full = SUPPORT_F | SUPPORT_THETA_F
    f_full_plus_local = all(_is_plus_dynamical_key(key) for key in support_f_full)
    f_full_mutated = _symmetrized_f(mutated)
    record(
        "C.hostile.F_is_not_plus_local",
        (
            not f_full_plus_local
            and bool(SUPPORT_THETA_F)
            and abs(f_full_mutated - f_full) > 1.0e-8
        ),
        (
            f"structural_plus_local={f_full_plus_local}, "
            f"|F(U_mut)-F(U)|={abs(f_full_mutated-f_full):.3e}"
        ),
    )

    support_bad = SUPPORT_F | SUPPORT_THETA_F

    def f_bad(config: np.ndarray) -> complex:
        return _f_plus(config) + 0.25 * _f_minus(config)

    bad_plus_local = all(_is_plus_dynamical_key(key) for key in support_bad)
    bad_before = f_bad(u)
    bad_after = f_bad(mutated)
    record(
        "C.hostile.negative_half_leak_rejected",
        not bad_plus_local and abs(bad_after - bad_before) > 1.0e-8,
        (
            f"structural_plus_local={bad_plus_local}, "
            f"|f_bad(U_mut)-f_bad(U)|={abs(bad_after-bad_before):.3e}"
        ),
    )


def part_d_hostile_partition_and_orientation() -> None:
    print("\n=== Part D: hostile partition and reflection-orientation controls ===")
    plaquettes = _all_plaquettes()
    parts = _partition(plaquettes)
    omitted_wrap = parts["plus"] + parts["minus"] + parts["mixed_plane"]
    missing = set(plaquettes) - set(omitted_wrap)
    u = _complete_temporal_gauge_config(SEED + 5)
    correct_action = _wilson_action(u, plaquettes)
    wrong_action = _wilson_action(u, omitted_wrap)
    record(
        "D.hostile.omitted_wrap_partition_fails",
        len(missing) == 24 and abs(correct_action - wrong_action) > 1.0e-8,
        f"missing={len(missing)}, |S_full-S_wrong|={abs(correct_action-wrong_action):.3e}",
    )

    generic = _random_config(SEED + 6)
    correct_theta = _reflect_config(generic)
    wrong_theta = _reflect_config_wrong_temporal_orientation(generic)
    s_generic = _wilson_action(generic, plaquettes)
    correct_diff = abs(_wilson_action(correct_theta, plaquettes) - s_generic)
    wrong_diff = abs(_wilson_action(wrong_theta, plaquettes) - s_generic)
    record(
        "D.hostile.wrong_temporal_orientation_fails",
        correct_diff < TOL and wrong_diff > 1.0e-8,
        f"correct_diff={correct_diff:.3e}, wrong_diff={wrong_diff:.3e}",
    )


NOTE = ROOT / (
    "docs/"
    "GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_"
    "REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md"
)
LEDGER_DIR = ROOT / "docs" / "audit" / "data" / "ledger"


def _dependency_in_worktree(filename: str) -> bool:
    return (ROOT / "docs" / filename).is_file()


def _parse_export_contract(text: str) -> dict | None:
    start = "<!-- gauge-os-step1-export-contract:start -->"
    end = "<!-- gauge-os-step1-export-contract:end -->"
    pattern = re.compile(
        re.escape(start) + r"\s*```json\s*(\{.*?\})\s*```\s*" + re.escape(end),
        re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        return None
    try:
        parsed = json.loads(match.group(1))
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def _direct_consumers_from_shards() -> list[tuple[str, Path]]:
    """Discover direct consumers without consulting status/cache fields."""
    consumers: list[tuple[str, Path]] = []
    for shard in sorted(LEDGER_DIR.glob("*/*.json")):
        raw = shard.read_text(encoding="utf-8")
        if CLAIM_ID not in raw:
            continue
        row = json.loads(raw)
        if CLAIM_ID not in row.get("deps", []):
            continue
        claim_id = row.get("claim_id")
        note_path = row.get("note_path")
        if isinstance(claim_id, str) and isinstance(note_path, str):
            consumers.append((claim_id, ROOT / note_path))
    return consumers


def _consumer_has_noninheritance_firewall(text: str) -> bool:
    flat = " ".join(text.split())
    markers = (
        "non-load-bearing",
        "does not by itself prove membership",
        "supplies neither this blocked membership",
        "graph-bookkeeping section",
    )
    return any(marker in flat for marker in markers)


def part_e_scope_firewall() -> None:
    print("\n=== Part E: source contract and sharded-ledger consumer firewall ===")
    text = NOTE.read_text(encoding="utf-8")
    contract = _parse_export_contract(text)
    record(
        "E.note.export_contract_exact",
        contract == EXPECTED_EXPORT_CONTRACT,
        "exact match" if contract == EXPECTED_EXPORT_CONTRACT else repr(contract),
    )
    required = [
        "trivial temporal Polyakov-holonomy sector",
        "if and only if",
        "supp(f)⊂E_+",
        "open downstream\nbridge",
        "No such\nidentity is asserted for an arbitrary unsymmetrized Wilson loop",
        "This source repair does not edit any audit ledger",
    ]
    forbidden_patterns = [
        r"gauge orbit representative choice",
        r"representative of (?:a|any|every) (?:general )?periodic gauge orbit",
        r"every periodic gauge orbit",
        r"arbitrary periodic gauge orbit",
        r"symmetrized Wilson-loop observables satisfy reflection-Hermiticity",
        r"F\(U\)` is exactly the test-function class",
        r"· \|F\(U\)\|²",
        r"structural positive-half localization of an explicitly consumed observable",
        r"`F` is an admissible positive-half test observable",
    ]
    missing = [marker for marker in required if marker not in text]
    stale = [
        pattern
        for pattern in forbidden_patterns
        if re.search(pattern, text, flags=re.IGNORECASE)
    ]
    record(
        "E.note.required_scope_markers",
        not missing,
        "all present" if not missing else f"missing={missing}",
    )
    record(
        "E.note.unsupported_exports_absent",
        not stale,
        "none present" if not stale else f"stale={stale}",
    )

    consumers = _direct_consumers_from_shards()
    consumer_failures: list[str] = []
    for consumer_id, note_path in consumers:
        if not note_path.is_file():
            consumer_failures.append(f"{consumer_id}:missing:{note_path}")
            continue
        consumer_text = note_path.read_text(encoding="utf-8")
        if not _consumer_has_noninheritance_firewall(consumer_text):
            consumer_failures.append(f"{consumer_id}:missing_noninheritance_firewall")
    record(
        "E.direct_consumers.sharded_ledger_noninheritance",
        bool(consumers) and not consumer_failures,
        (
            ", ".join(consumer_id for consumer_id, _ in consumers)
            if not consumer_failures
            else "; ".join(consumer_failures)
        ),
    )

    dep = (
        "GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_"
        "NARROW_THEOREM_NOTE_2026-05-10.md"
    )
    record(
        "E.load_bearing_dependency.present_in_worktree",
        _dependency_in_worktree(dep),
        dep,
    )


def main() -> int:
    print("=" * 78)
    print("Gauge OS Step 1: U_0=I sector + symmetrized reflection-Hermiticity")
    print("=" * 78)
    print(
        f"Carrier: (Z/{L_T}) x (Z/{L_S})^3, {L_T*L_S**3} sites, "
        f"SU({N_C}), beta={BETA}, seed={SEED}"
    )
    print(
        "Scope: pure Wilson action; P(x)=I/U_0=I sector; raw-link f is a "
        "worked witness only; downstream OS admissibility remains open."
    )

    part_a_carrier_and_decomposition()
    part_b_temporal_holonomy()
    part_c_localization_and_hermiticity()
    part_d_hostile_partition_and_orientation()
    part_e_scope_firewall()

    print("\n" + "=" * 78)
    for line in LOG:
        print(line)
    print(f"\nSCORECARD: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("All narrowed finite-sector and hostile-control checks PASSED.")
        print("Independent audit alone decides effective status.")
        return 0
    print("One or more checks FAILED.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
