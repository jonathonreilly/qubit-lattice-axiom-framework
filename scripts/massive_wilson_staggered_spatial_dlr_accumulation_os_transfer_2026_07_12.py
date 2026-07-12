#!/usr/bin/env python3
"""Spatial DLR accumulation and OS-transfer certificate for massive staggered matter."""

from __future__ import annotations

from pathlib import Path

import numpy as np

from massive_staggered_logdet_holder_ruelle_uniqueness_2026_07_12 import (
    epsilon_matrix,
    haar_su3,
    identity_links,
    matrix_function_hermitian,
    random_links,
    site_index,
    staggered_hop,
)


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "MASSIVE_WILSON_STAGGERED_SPATIAL_DLR_ACCUMULATION_OS_TRANSFER_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
TOL = 3.0e-10
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {name}: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {name}: {detail}")


def site_trace(matrix: np.ndarray, time: int, position: int, length_x: int) -> complex:
    start = site_index(time, position, 0, length_x)
    return np.trace(matrix[start : start + 3, start : start + 3])


def q_matrix(hop: np.ndarray, mass: float) -> tuple[np.ndarray, float]:
    dimension = hop.shape[0]
    scale = mass**2 + 16.0
    amat = mass**2 * np.eye(dimension) - hop @ hop
    return np.eye(dimension) - amat / scale, 16.0 / scale


def cyclic_distance(left: int, right: int, length: int) -> int:
    direct = abs(left - right)
    return min(direct, length - direct)


def main() -> int:
    rng = np.random.default_rng(20260712)
    mass = 1.25
    radius = 16.0 / (mass**2 + 16.0)

    volume_rows = []
    volume_ok = True
    for length_t, length_x in ((6, 4), (8, 6), (10, 8)):
        temporal, spatial = random_links(length_t, length_x, rng)
        hop = staggered_hop(temporal, spatial, antiperiodic=True)
        epsilon = epsilon_matrix(length_t, length_x)
        qmat, universal_radius = q_matrix(hop, mass)
        qvalues = np.linalg.eigvalsh((qmat + qmat.conj().T) / 2.0)
        dmat = mass * np.eye(hop.shape[0]) + hop
        inverse_norm = float(np.linalg.norm(np.linalg.inv(dmat), 2))
        current_ok = (
            np.linalg.norm(hop + hop.conj().T) < TOL
            and np.linalg.norm(epsilon @ hop + hop @ epsilon) < TOL
            and np.min(qvalues) >= -TOL
            and np.max(qvalues) <= universal_radius + TOL
            and inverse_norm <= 1.0 / mass + TOL
        )
        volume_ok = volume_ok and current_ok
        volume_rows.append(
            f"{length_t}x{length_x}:||Q||={np.max(qvalues):.6f},"
            f"||D^-1||={inverse_norm:.6f}"
        )
    check(
        "Q contraction and massive inverse bounds are independent of finite volume",
        volume_ok and radius < 1.0,
        "; ".join(volume_rows) + f"; universal r={radius:.6f}",
    )

    length_t, length_x = 12, 12
    temporal_a, spatial_a = random_links(length_t, length_x, rng)
    temporal_b = temporal_a.copy()
    spatial_b = spatial_a.copy()
    center_t = length_t // 2
    center_x = length_x // 2
    agreement_radius = 3
    for time in range(length_t):
        for position in range(length_x):
            distance = cyclic_distance(time, center_t, length_t) + cyclic_distance(
                position, center_x, length_x
            )
            if distance > agreement_radius:
                temporal_b[time, position] = random_links(1, 1, rng)[0][0, 0]
                spatial_b[time, position] = random_links(1, 1, rng)[1][0, 0]

    hop_a = staggered_hop(temporal_a, spatial_a, antiperiodic=True)
    hop_b = staggered_hop(temporal_b, spatial_b, antiperiodic=True)
    qa, _ = q_matrix(hop_a, mass)
    qb, _ = q_matrix(hop_b, mass)
    power_a = np.eye(qa.shape[0], dtype=complex)
    power_b = np.eye(qb.shape[0], dtype=complex)
    local_residuals = []
    site_bounds = []
    for order in range(1, 6):
        power_a = power_a @ qa
        power_b = power_b @ qb
        trace_a = site_trace(power_a, center_t, center_x, length_x)
        trace_b = site_trace(power_b, center_t, center_x, length_x)
        local_residuals.append(abs(trace_a - trace_b))
        site_bounds.append(abs(trace_a) <= 3.0 * radius**order + 2.0e-9)
    check(
        "The lowest tested site-anchored Q power is exactly local and all tested powers obey the norm bound",
        max(local_residuals[:1]) < TOL and all(site_bounds),
        "remote-change residuals Q^1..Q^5="
        + ",".join(f"{value:.3e}" for value in local_residuals)
        + "; all |tr_x Q^n|<=3r^n",
    )

    # Compare a central density and inverse entry while moving the changed shell outward.
    density_differences = []
    inverse_differences = []
    remote_t, remote_x = 8, 12
    base_temporal, base_spatial = identity_links(remote_t, remote_x)
    base_hop = staggered_hop(base_temporal, base_spatial, antiperiodic=True)
    base_a = mass**2 * np.eye(base_hop.shape[0]) - base_hop @ base_hop
    base_log = matrix_function_hermitian(base_a, np.log)
    base_d_inverse = np.linalg.inv(mass * np.eye(base_hop.shape[0]) + base_hop)
    fixed_perturbation = haar_su3(rng)
    for distance in (1, 2, 3, 4):
        changed_temporal = base_temporal.copy()
        changed_spatial = base_spatial.copy()
        changed_spatial[4, 4 + distance] = fixed_perturbation
        changed_hop = staggered_hop(changed_temporal, changed_spatial, antiperiodic=True)
        changed_a = mass**2 * np.eye(changed_hop.shape[0]) - changed_hop @ changed_hop
        changed_log = matrix_function_hermitian(changed_a, np.log)
        density_differences.append(
            abs(site_trace(base_log - changed_log, 4, 4, remote_x))
        )
        changed_d_inverse = np.linalg.inv(
            mass * np.eye(changed_hop.shape[0]) + changed_hop
        )
        target = site_index(4, 4, 0, remote_x)
        inverse_differences.append(
            abs(base_d_inverse[target, target] - changed_d_inverse[target, target])
        )
    check(
        "More-remote endpoint samples reduce determinant-density and propagator response",
        density_differences[-1] < density_differences[0]
        and inverse_differences[-1] < inverse_differences[0],
        "density=" + ",".join(f"{value:.3e}" for value in density_differences)
        + "; inverse=" + ",".join(f"{value:.3e}" for value in inverse_differences),
    )

    # Every compression of D^{-1} has norm <=1/m, hence every q-minor <=m^{-q}.
    temporal, spatial = random_links(8, 6, rng)
    hop = staggered_hop(temporal, spatial, antiperiodic=True)
    d_inverse = np.linalg.inv(mass * np.eye(hop.shape[0]) + hop)
    minor_rows = np.array([0, 7, 18, 29])
    minor_cols = np.array([2, 11, 20, 31])
    minor = d_inverse[np.ix_(minor_rows, minor_cols)]
    minor_det = abs(np.linalg.det(minor))
    check(
        "Fixed-degree Wick minors obey the spatial-volume-uniform mass bound",
        np.linalg.norm(d_inverse, 2) <= 1.0 / mass + TOL
        and np.linalg.norm(minor, 2) <= 1.0 / mass + TOL
        and minor_det <= mass ** (-len(minor_rows)) + TOL,
        f"||D^-1||={np.linalg.norm(d_inverse,2):.6f}, "
        f"||minor||={np.linalg.norm(minor,2):.6f}, |det minor|={minor_det:.3e}, "
        f"m^-q={mass**(-len(minor_rows)):.3e}",
    )

    # Four-dimensional center counting and one additional diameter factor.
    orders = np.arange(1, 501, dtype=float)
    absolute_terms = (2.0 * orders + 2.0) ** 4 * radius**orders / orders
    moment_terms = (2.0 * orders + 2.0) ** 5 * radius**orders / orders
    absolute_partial = np.cumsum(absolute_terms)
    moment_partial = np.cumsum(moment_terms)
    absolute_tail_ratio = float(np.sum(absolute_terms[-50:]) / absolute_partial[-1])
    moment_tail_ratio = float(np.sum(moment_terms[-50:]) / moment_partial[-1])
    check(
        "Dimension-four absolute and first-moment interaction majorants converge",
        np.isfinite(absolute_partial[-1])
        and np.isfinite(moment_partial[-1])
        and absolute_tail_ratio < 1.0e-12
        and moment_tail_ratio < 1.0e-12,
        f"sum n^4 r^n/n={absolute_partial[-1]:.6e}, "
        f"sum n^5 r^n/n={moment_partial[-1]:.6e}, "
        f"last-50 fractions={absolute_tail_ratio:.3e},{moment_tail_ratio:.3e}",
    )

    masses = (0.01, 0.1, 1.0, 10.0)
    radii = [16.0 / (value**2 + 16.0) for value in masses]
    check(
        "The thermodynamic interaction is summable for every fixed strictly positive mass",
        all(0.0 < value < 1.0 for value in radii),
        ", ".join(
            f"m={mass_value}:r={radius_value:.12f}"
            for mass_value, radius_value in zip(masses, radii)
        ),
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    conditions = [
        "supplied Wilson-staggered dynamics",
        "positive fermion mass",
        "spatial DLR existence",
        "spatial uniqueness/phase selection",
        "continuum/SM/GR closure",
    ]
    pairs = [
        f"| {conditions[left]} | {conditions[right]} |"
        for left in range(len(conditions))
        for right in range(left + 1, len(conditions))
    ]
    required = [
        "spatial **existence**, not spatial uniqueness",
        "volume-uniform absolutely summable",
        "diameter-weighted summable",
        "DLR accumulation state",
        "subsequential spatial accumulation",
        "does not derive",
        "physical probability rule",
        "No axiom-update stop",
        "No-Go Discipline N1--N8",
        "### N3 — hidden-condition phrase scan",
        "### N4 — citation/residual matching",
        "### N5 — rhetoric and resolution audit",
        "### N6 — partial-closure, convention, reframe, and primitive scan",
        "### N7 — hostile steelman",
        "### N8 — cross-cycle echo",
        "Test and result",
        "Left closes right? | Right closes left? | Independent?",
        "Cited witness and location | Witness residual | Present residual | Match? | Disposition",
        "Statement / resolution | Tested? | Permitted conclusion",
        "Arbitrary nonlocal or volume-growing observable | No",
        "All spatial phases coincide | No",
        "Unique `beta=6` plaquette value or gap | No",
        "No uniqueness theorem is used or asserted",
        "Sole direct in-repo science dependency",
        "Independent scratch derivations found a live nonempty wedge but disagreed",
        "Retirement mechanism and applicability",
        "Lattice, Qubit, Admissibility, and Record",
        "every spatial accumulation point of the time-first states is also a diagonal",
        "reduced `1+1` `SU(3)` carrier",
        "does not numerically prove the full",
    ]
    hidden_rows = [
        "| `we assume` |",
        "| `by construction` |",
        "| `as is standard` |",
        "| `the framework provides` |",
        "| `bridge context` |",
        "| `background` |",
        "| `naturally` |",
        "| `obviously` |",
        "| `standard QFT` |",
        "| `registered` |",
        "| `canonical` |",
    ]
    missing = [item for item in required + hidden_rows + pairs if item not in note_text]
    attempted = note_text.count("| `ATTEMPTED` |")
    directional_pairs = note_text.count("| No | No | Yes |")
    forbidden_native_language = ["Lattice, Quantum", "Block 18", "Block 19", "Blocks 17--19"]
    present_forbidden = [item for item in forbidden_native_language if item in note_text]
    check(
        "Source-note boundary and N1-N8 contract",
        not missing
        and not present_forbidden
        and attempted >= 8
        and directional_pairs >= 10,
        f"missing={missing}; forbidden={present_forbidden}; "
        f"attempted routes={attempted}; directional pairs={directional_pairs}",
    )

    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
