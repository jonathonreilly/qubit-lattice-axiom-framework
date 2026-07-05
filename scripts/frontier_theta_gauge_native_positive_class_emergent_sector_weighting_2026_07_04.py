#!/usr/bin/env python3
"""Finite checks for the native positive-class theta-sector theorem.

The enumerations below are exact finite sums over the toy state spaces.  Floating
point enters only through the positive Boltzmann factors exp(beta cos(theta)).
No Monte Carlo sampling is used for sector masses.
"""

from __future__ import annotations

import cmath
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "THETA_GAUGE_NATIVE_POSITIVE_CLASS_EMERGENT_SECTOR_WEIGHTING_NARROW_THEOREM_NOTE_2026-07-04.md"
TOL = 1.0e-9


def rel_close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def check_su2_connectivity() -> tuple[bool, str]:
    rng = np.random.default_rng(20260704)
    eye = np.eye(2, dtype=complex)
    pauli = [
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    ]

    def axis_angle_path(axis: np.ndarray, angle: float, t: float) -> np.ndarray:
        generator = axis[0] * pauli[0] + axis[1] * pauli[1] + axis[2] * pauli[2]
        return math.cos(t * angle) * eye + 1j * math.sin(t * angle) * generator

    worst = 0.0
    for _ in range(6):
        for _component in range(3):
            axis = rng.normal(size=3)
            axis = axis / np.linalg.norm(axis)
            angle = rng.uniform(-math.pi + 0.05, math.pi - 0.05)
            target = axis_angle_path(axis, angle, 1.0)
            start_err = np.linalg.norm(axis_angle_path(axis, angle, 0.0) - eye)
            end_err = np.linalg.norm(axis_angle_path(axis, angle, 1.0) - target)
            worst = max(worst, float(start_err), float(end_err))
            for t in np.linspace(0.0, 1.0, 9):
                g_t = axis_angle_path(axis, angle, float(t))
                unit_err = np.linalg.norm(g_t.conj().T @ g_t - eye)
                det_err = abs(np.linalg.det(g_t) - 1.0)
                worst = max(worst, float(unit_err), float(det_err))
    return worst < 1.0e-11, f"explicit SU(2)^3 paths endpoint/unitarity worst_err={worst:.3e}"


def circle_lift_weights(N: int, beta: float) -> list[tuple[int, float]]:
    # For even N, include both oriented antipodal lifts +/-N/2.  This keeps the
    # finite lifted path model exactly conjugation-paired.
    return [
        (d, math.exp(beta * math.cos(2.0 * math.pi * d / N)))
        for d in range(-N // 2, N // 2 + 1)
    ]


def circle_masses(N: int = 24, T: int = 6, beta: float = 5.0) -> dict[int, float]:
    weights = circle_lift_weights(N, beta)
    masses: dict[int, float] = defaultdict(float)
    for start in range(N):
        states: dict[tuple[int, int], float] = {(start, 0): 1.0}
        for _tick in range(T):
            nxt: dict[tuple[int, int], float] = defaultdict(float)
            for (pos, lift_sum), value in states.items():
                for d, w in weights:
                    nxt[((pos + d) % N, lift_sum + d)] += value * w
            states = nxt
        for (pos, lift_sum), value in states.items():
            if pos == start:
                if lift_sum % N != 0:
                    raise AssertionError("closed lifted path produced non-integer winding")
                masses[lift_sum // N] += value
    return dict(masses)


def normalize_masses(masses: dict[int, float]) -> dict[int, float]:
    total = sum(masses.values())
    return {q: value / total for q, value in masses.items()}


def adjacent_populated_pair(masses: dict[int, float]) -> tuple[int, int] | None:
    populated = {q for q, value in masses.items() if value > 0.0}
    for q in sorted(populated):
        if q + 1 in populated:
            return q, q + 1
    return None


def check_circle_positive_sector_masses() -> tuple[bool, str, dict[int, float], tuple[int, int]]:
    N, T, beta = 24, 6, 5.0
    masses = circle_masses(N=N, T=T, beta=beta)
    min_link_weight = min(w for _d, w in circle_lift_weights(N, beta))
    all_masses_nonnegative = all(value >= 0.0 and math.isfinite(value) for value in masses.values())
    pair = adjacent_populated_pair(masses)
    pairing_ok = all(rel_close(masses.get(q, 0.0), masses.get(-q, 0.0), 1.0e-8) for q in masses)
    ok = min_link_weight > 0.0 and all_masses_nonnegative and pair is not None and pairing_ok
    if pair is None:
        pair = (0, 0)
    detail = (
        f"N={N} T={T} sectors={sorted(masses)} min_link_weight={min_link_weight:.3e} "
        f"adjacent={pair} conjugation_pairing={pairing_ok}"
    )
    return ok, detail, masses, pair


def check_theta_fit_discriminator(masses: dict[int, float], pair: tuple[int, int]) -> tuple[bool, str]:
    # Quantifier sweep, constructed rather than assumed: a representation
    # m(q) = e^{i theta q} m~(q) with m~ > 0 exists iff m~(q) = e^{-i theta q} m(q)
    # is real and positive on every populated sector. Sweep theta over a grid
    # and verify existence EXACTLY at theta = 0 (mod 2 pi) and nowhere else.
    populated = [q for q, value in masses.items() if value > 0.0 and q != 0]
    if not populated:
        return False, "no populated nonzero sector to constrain theta"

    def positive_rep_exists(theta: float) -> bool:
        for q, value in masses.items():
            if value <= 0.0:
                continue
            m_tilde_q = cmath.exp(-1j * theta * q) * value
            if abs(m_tilde_q.imag) > 1.0e-10 or m_tilde_q.real <= 0.0:
                return False
        return True

    grid = [2.0 * math.pi * k / 360.0 for k in range(360)]
    admitted = [theta for theta in grid if positive_rep_exists(theta)]
    only_zero = admitted == [0.0]

    # Positive control: a genuinely theta-weighted (complex) sector family is
    # detected -- the inverse rotation recovers positivity exactly at theta_0.
    theta_0 = 0.7
    fake = {q: cmath.exp(1j * theta_0 * q) * value for q, value in masses.items()}
    has_nonreal_sector = any(abs(value.imag) > 1.0e-8 for value in fake.values())

    def fake_rep_exists(theta: float) -> bool:
        for q, value in fake.items():
            if abs(value) <= 0.0:
                continue
            m_tilde_q = cmath.exp(-1j * theta * q) * value
            if abs(m_tilde_q.imag) > 1.0e-10 or m_tilde_q.real <= 0.0:
                return False
        return True

    recovered = [theta for theta in grid + [theta_0] if fake_rep_exists(theta)]
    control_ok = has_nonreal_sector and recovered == [theta_0]

    ok = only_zero and control_ok
    detail = (
        f"admitted_thetas_from_positive_masses={admitted} (360-point grid) "
        f"fake_recovered_thetas={recovered} nonreal_fake={has_nonreal_sector}"
    )
    return ok, detail


def check_theta_pi_branch(masses: dict[int, float]) -> tuple[bool, str]:
    odd_sectors = sorted(q for q, value in masses.items() if q % 2 != 0 and value > 0.0)
    even_sectors = sorted(q for q, value in masses.items() if q % 2 == 0 and value > 0.0)
    if not odd_sectors:
        return False, "no populated odd sector found"
    if not even_sectors:
        return False, "no populated even sector found"
    q = odd_sectors[0]
    q_even = even_sectors[0]
    signed_value = ((-1) ** q) * masses[q]
    relative_sign = ((-1) ** (q - q_even))
    ok = relative_sign < 0 and signed_value < 0.0 < masses[q]
    return (
        ok,
        f"mixed_parity=True even_sector={q_even} odd_sector={q} "
        f"native_mass={masses[q]:.6e} pi_weighted_value={signed_value:.6e}",
    )


def check_sparse_support_aliases() -> tuple[bool, str]:
    sparse_even = {0: 0.2, 2: 0.3, 4: 0.5}
    sparse_odd = {1: 0.4, 3: 0.6}
    mixed_parity = {0: 0.4, 1: 0.6}
    singleton = {5: 1.0}

    def positive_rep_exists(theta: float, masses: dict[int, float]) -> bool:
        for q, value in masses.items():
            if value <= 0.0:
                continue
            m_tilde_q = cmath.exp(-1j * theta * q) * value
            if abs(m_tilde_q.imag) > 1.0e-10 or m_tilde_q.real <= 0.0:
                return False
        return True

    def relative_alias_exists(theta: float, masses: dict[int, float]) -> bool:
        populated = sorted(q for q, value in masses.items() if value > 0.0)
        if len(populated) <= 1:
            return True
        q0 = populated[0]
        return all(abs(cmath.exp(1j * theta * (q - q0)) - 1.0) <= 1.0e-10 for q in populated)

    grid = [2.0 * math.pi * k / 360.0 for k in range(360)]
    relative_even = [round(theta, 12) for theta in grid if relative_alias_exists(theta, sparse_even)]
    relative_odd = [round(theta, 12) for theta in grid if relative_alias_exists(theta, sparse_odd)]
    relative_mixed = [round(theta, 12) for theta in grid if relative_alias_exists(theta, mixed_parity)]
    exact_odd = [round(theta, 12) for theta in grid if positive_rep_exists(theta, sparse_odd)]
    singleton_all_alias = all(relative_alias_exists(theta, singleton) for theta in grid)
    expected_single_parity = [0.0, round(math.pi, 12)]
    expected_mixed = [0.0]
    ok = (
        relative_even == expected_single_parity
        and relative_odd == expected_single_parity
        and relative_mixed == expected_mixed
        and exact_odd == expected_mixed
        and singleton_all_alias
    )
    detail = (
        f"relative_even={relative_even} relative_odd={relative_odd} "
        f"relative_mixed={relative_mixed} exact_odd={exact_odd} "
        f"singleton_all_alias={singleton_all_alias}"
    )
    return ok, detail


def circle_block_transitions(N: int = 24, beta: float = 5.0, block_ticks: int = 2) -> list[dict[tuple[int, int], float]]:
    weights = circle_lift_weights(N, beta)
    transitions: list[dict[tuple[int, int], float]] = []
    for start in range(N):
        states: dict[tuple[int, int], float] = {(start, 0): 1.0}
        for _tick in range(block_ticks):
            nxt: dict[tuple[int, int], float] = defaultdict(float)
            for (pos, lift_sum), value in states.items():
                for d, w in weights:
                    nxt[((pos + d) % N, lift_sum + d)] += value * w
            states = nxt
        transitions.append(dict(states))
    return transitions


def masses_from_block_transitions(
    transitions: list[dict[tuple[int, int], float]], N: int = 24, blocks: int = 3
) -> dict[int, float]:
    masses: dict[int, float] = defaultdict(float)
    for start in range(N):
        states: dict[tuple[int, int], float] = {(start, 0): 1.0}
        for _block in range(blocks):
            nxt: dict[tuple[int, int], float] = defaultdict(float)
            for (pos, lift_sum), value in states.items():
                for (new_pos, block_lift), block_weight in transitions[pos].items():
                    nxt[(new_pos, lift_sum + block_lift)] += value * block_weight
            states = nxt
        for (pos, lift_sum), value in states.items():
            if pos == start:
                if lift_sum % N != 0:
                    raise AssertionError("closed block path produced non-integer winding")
                masses[lift_sum // N] += value
    return dict(masses)


def check_inheritance() -> tuple[bool, str]:
    N, beta = 24, 5.0
    fine = circle_masses(N=N, T=6, beta=beta)
    block_transitions = circle_block_transitions(N=N, beta=beta, block_ticks=2)
    coarse = masses_from_block_transitions(block_transitions, N=N, blocks=3)
    coarse_nonnegative = all(value >= 0.0 for value in coarse.values())
    same_as_fine = all(rel_close(fine.get(q, 0.0), coarse.get(q, 0.0), 1.0e-8) for q in set(fine) | set(coarse))
    block_entries_nonnegative = all(
        value >= 0.0 for trans in block_transitions for value in trans.values()
    )

    weak_windows = []
    for T in (2, 4, 6):
        # A tightening finite-window scaling: beta=T keeps the positive kernel
        # in the same heat-kernel-like class and gives an explicit weak
        # convergence demo toward the non-negative delta mass at q=0.
        weak_windows.append(normalize_masses(circle_masses(N=N, T=T, beta=float(T))))
    tv_to_delta = [1.0 - window.get(0, 0.0) for window in weak_windows]
    normalized_ok = all(
        all(value >= 0.0 for value in window.values()) and rel_close(sum(window.values()), 1.0, 1.0e-10)
        for window in weak_windows
    )
    converges_to_positive_delta = tv_to_delta[2] <= tv_to_delta[1] <= tv_to_delta[0] and tv_to_delta[2] < 1.0e-6
    ok = coarse_nonnegative and same_as_fine and block_entries_nonnegative and normalized_ok and converges_to_positive_delta
    detail = (
        f"coarse_nonnegative={coarse_nonnegative} coarse_equals_fine={same_as_fine} "
        f"weak_T_windows={[sorted(w) for w in weak_windows]} tv_to_delta0={[f'{v:.3e}' for v in tv_to_delta]}"
    )
    return ok, detail


def centered_lifts_for_delta(delta: int, N: int) -> list[int]:
    delta %= N
    lifts = []
    for d in range(-N // 2, N // 2 + 1):
        if d % N == delta:
            lifts.append(d)
    return lifts


def config_index_to_tuple(index: int, N: int, links: int) -> tuple[int, ...]:
    values = []
    current = index
    for _ in range(links):
        values.append(current % N)
        current //= N
    return tuple(values)


def gauge_fermion_diag(config: tuple[int, ...], N: int) -> float:
    # Positive diagonal insertion standing in for the determinant-positive
    # factor in the real canonical class.
    average_cos = sum(math.cos(2.0 * math.pi * value / N) for value in config) / len(config)
    return 1.2 + 0.1 * average_cos


def check_gauge_miniature() -> tuple[bool, str]:
    N, links, ticks, beta = 6, 3, 3, 1.4
    configs = [config_index_to_tuple(i, N, links) for i in range(N**links)]
    transition_entries: list[dict[tuple[int, int], float]] = []
    min_plaquette_weight = float("inf")
    min_transfer_entry = float("inf")
    conjugation_ok = True

    for config in configs:
        row: dict[tuple[int, int], float] = defaultdict(float)
        for new_config in configs:
            per_link_lifts = [centered_lifts_for_delta(new_config[i] - config[i], N) for i in range(links)]
            entry_total = 0.0
            for d0 in per_link_lifts[0]:
                for d1 in per_link_lifts[1]:
                    for d2 in per_link_lifts[2]:
                        plaquette_weights = [
                            math.exp(beta * math.cos(2.0 * math.pi * d / N)) for d in (d0, d1, d2)
                        ]
                        min_plaquette_weight = min(min_plaquette_weight, *plaquette_weights)
                        weight = plaquette_weights[0] * plaquette_weights[1] * plaquette_weights[2]
                        weight *= gauge_fermion_diag(new_config, N)
                        lift_sum = d0 + d1 + d2
                        row[(configs.index(new_config), lift_sum)] += weight
                        entry_total += weight
            min_transfer_entry = min(min_transfer_entry, entry_total)
        transition_entries.append(dict(row))

    for i, config in enumerate(configs):
        conj_i = configs.index(tuple((-value) % N for value in config))
        for (j, lift_sum), value in transition_entries[i].items():
            conj_j = configs.index(tuple((-value) % N for value in configs[j]))
            paired = transition_entries[conj_i].get((conj_j, -lift_sum), 0.0)
            if not rel_close(value, paired, 1.0e-8):
                conjugation_ok = False
                break
        if not conjugation_ok:
            break

    masses: dict[int, float] = defaultdict(float)
    for start in range(len(configs)):
        states: dict[tuple[int, int], float] = {(start, 0): 1.0}
        for _tick in range(ticks):
            nxt: dict[tuple[int, int], float] = defaultdict(float)
            for (state, lift_sum), value in states.items():
                for (new_state, plaquette_lift), transition_weight in transition_entries[state].items():
                    nxt[(new_state, lift_sum + plaquette_lift)] += value * transition_weight
            states = nxt
        for (state, lift_sum), value in states.items():
            if state == start:
                if lift_sum % N != 0:
                    raise AssertionError("closed gauge history produced non-integer flux")
                masses[lift_sum // N] += value

    masses_nonnegative = all(value >= 0.0 for value in masses.values())
    ok = (
        min_plaquette_weight > 0.0
        and min_transfer_entry >= 0.0
        and conjugation_ok
        and masses_nonnegative
        and all(gauge_fermion_diag(config, N) > 0.0 for config in configs)
    )
    detail = (
        f"N={N} links={links} ticks={ticks} min_plaquette={min_plaquette_weight:.3e} "
        f"min_transfer={min_transfer_entry:.3e} conjugation={conjugation_ok} sectors={sorted(masses)}"
    )
    return ok, detail


def check_text_guards() -> tuple[bool, str]:
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "natively 3+1",
        "no fundamental fourth lattice direction",
        "emergent OS0 surface",
        "vacuous or zero",
        "context handle, not a citation-graph dependency",
        "not a discharge",
    ]
    banned = [
        "discharges",
        "retires",
        "closes the admission",
        "retained bridge",
        "status certificate",
        "audit_required_before_effective_retained",
    ]
    allowed_md = {
        "MINIMAL_AXIOMS_2026-06-29.md",
        "GAUGE_WILSON_SU3_ALL_WEIGHT_POSITIVE_COEFFICIENT_FORMAL_BRIDGE_NOTE_2026-06-07.md",
        "WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md",
        "STAGGERED_WILSON_DET_POSITIVITY_BRIDGE_THEOREM_NOTE_2026-05-05.md",
        "REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md",
        "RP_MIXED_OBSERVABLE_SINGLE_TRANSFER_MATRIX_NARROW_THEOREM_NOTE_2026-05-29.md",
        "SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md",
    }
    missing = [phrase for phrase in required if phrase not in text]
    present_banned = [phrase for phrase in banned if phrase in text]
    md_targets = re.findall(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)", text)
    bad_targets = sorted({Path(target).name for target in md_targets if Path(target).name not in allowed_md})
    ok = not missing and not present_banned and not bad_targets
    detail = f"missing={missing} banned={present_banned} bad_md_targets={bad_targets}"
    return ok, detail


def main() -> int:
    results: list[tuple[str, bool, str]] = []

    ok_a, detail_a = check_su2_connectivity()
    results.append(("A", ok_a, detail_a))

    ok_b, detail_b, masses, pair = check_circle_positive_sector_masses()
    results.append(("B", ok_b, detail_b))

    ok_c, detail_c = check_theta_fit_discriminator(masses, pair)
    results.append(("C", ok_c, detail_c))

    ok_d, detail_d = check_theta_pi_branch(masses)
    results.append(("D", ok_d, detail_d))

    ok_h, detail_h = check_sparse_support_aliases()
    results.append(("H", ok_h, detail_h))

    ok_e, detail_e = check_inheritance()
    results.append(("E", ok_e, detail_e))

    ok_f, detail_f = check_gauge_miniature()
    results.append(("F", ok_f, detail_f))

    ok_g, detail_g = check_text_guards()
    results.append(("G", ok_g, detail_g))

    pass_count = 0
    fail_count = 0
    for label, ok, detail in results:
        if ok:
            pass_count += 1
            status = "PASS"
        else:
            fail_count += 1
            status = "FAIL"
        print(f"{label} {status} {detail}")

    print(f"SUMMARY PASS={pass_count} FAIL={fail_count}")
    print("DONE")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
