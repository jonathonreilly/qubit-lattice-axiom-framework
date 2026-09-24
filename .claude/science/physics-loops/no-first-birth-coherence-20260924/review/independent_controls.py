#!/usr/bin/env python3
"""Narrow independent controls; no author matrix builder or campaign code.

The word enumeration checks actual cube combinatorics. The two-band example is
an explicitly labelled consistency model, not a finite-spin cube simulation.
No target value is fitted. All proposed leading constants were known when this
script was written, having first been derived in the independent PRE argument.
"""
from __future__ import annotations

import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path

import mpmath as mp

mp.mp.dps = 70
ROOT = Path(__file__).resolve().parent
A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
EDGES = tuple((a, b) for a in A for b in B if a ^ b in (1, 2, 4))
EDGE_ID = {frozenset(e): i for i, e in enumerate(EDGES)}
Q0 = tuple(int(v in A) for v in range(8))
ZERO = (0,) * 12


def gauss(q: tuple[int, ...], field: tuple[int, ...]) -> bool:
    div = [0] * 8
    for value, (a, b) in zip(field, EDGES):
        div[a] += value
        div[b] -= value
    return tuple(div) == tuple(q[v] - int(v in A) for v in range(8))


def rotor_hops(q: tuple[int, ...], field: tuple[int, ...]):
    out = []
    for k, (a, b) in enumerate(EDGES):
        if q[a] != 0 and q[b] == 0:
            qq, ff = list(q), list(field)
            qq[b], qq[a] = qq[a], 0
            ff[k] -= qq[b]
            out.append((tuple(qq), tuple(ff)))
    return out


def empty_edges(q: tuple[int, ...]):
    return [k for k, (a, b) in enumerate(EDGES) if q[a] == q[b] == 0]


def loss(q: tuple[int, ...], field: tuple[int, ...], spin: int | None):
    if spin is None:
        return Fraction(2 * len(empty_edges(q)))
    c = spin * (spin + 1)
    return sum((Fraction(2) - Fraction(2 * field[k] ** 2, c)
                for k in empty_edges(q)), Fraction(0))


def face_field(cycle: tuple[int, ...], coefficient: int):
    field = [0] * 12
    for u, v in zip(cycle, cycle[1:] + cycle[:1]):
        field[EDGE_ID[frozenset((u, v))]] += coefficient * (1 if u in A else -1)
    return tuple(field)


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def word_controls():
    assert len(EDGES) == 12 and gauss(Q0, ZERO)
    words = rotor_hops(Q0, ZERO)
    assert len(words) == len(set(words)) == 12
    assert all(gauss(q, e) for q, e in words)
    exact_rows = []
    for spin in (1, 2, 7, 31):
        losses = [loss(q, e, spin) for q, e in words]
        assert set(losses) == {Fraction(4)}
        exact_rows.append({
            "spin": spin,
            "F_norm_squared": len(words),
            "F_Gamma_F": fraction_string(sum(losses)),
            "Gamma_F_norm_squared": fraction_string(sum(x*x for x in losses)),
        })

    field_samples = (
        ZERO,
        face_field((0, 1, 3, 2), 1),
        face_field((0, 1, 5, 4), -1),
        face_field((0, 2, 6, 4), 2),
    )
    outputs = []
    for field in field_samples:
        assert gauss(Q0, field)
        image = rotor_hops(Q0, field)
        assert all(gauss(q, e) for q, e in image)
        assert len(image) == 12
        assert all(loss(q, e, None) == 4 for q, e in image)
        outputs.extend(image)
    assert len(set(outputs)) == 12 * len(field_samples)

    vacancy_counts = {}
    for a in A:
        for b in B:
            q = tuple(int((v in A and v != a) or v == b) for v in range(8))
            count = len(empty_edges(q))
            vacancy_counts[count] = vacancy_counts.get(count, 0) + 1
            assert count >= 2
    assert vacancy_counts == {2: 12, 3: 4}

    boundary_rows = []
    for spin in (1, 2, 7, 31):
        c = spin * (spin + 1)
        edge_min = min(Fraction(2) - Fraction(2*m*m, c)
                       for m in range(-spin, spin + 1))
        assert edge_min == Fraction(2, spin + 1)
        plus_only_min = min(Fraction(1) - Fraction(m*(m+1), c)
                            for m in range(-spin, spin + 1))
        assert plus_only_min == 0
        boundary_rows.append({
            "spin": spin,
            "two_sign_edge_loss_minimum": fraction_string(edge_min),
            "N4_grade1_loss_lower_bound": fraction_string(2 * edge_min),
            "one_sign_only_minimum_countercontrol": fraction_string(plus_only_min),
        })

    # A one-link shift changes w by a uniformly bounded factor. Sampling is
    # only a check of the elementary inequality proved algebraically in PRE.
    ratios = [Fraction(1 + (m+k)**2, 1 + m*m)
              for m in range(-100, 101) for k in (-1, 1)]
    assert max(ratios) <= 3
    return {
        "description": "Exact physical words and rational loss coefficients, no matrix builder",
        "edges": EDGES,
        "all_zero_field_F_words": [{"q": q, "E": e} for q, e in words],
        "zero_field_spin_rows": exact_rows,
        "rotor_field_samples": field_samples,
        "rotor_sample_output_words_distinct": len(set(outputs)),
        "grade1_vacancy_count_histogram": vacancy_counts,
        "spin_boundary_rows": boundary_rows,
        "sampled_weight_ratio_maximum": fraction_string(max(ratios)),
    }


def to_float(value):
    return float(mp.re(value))


def two_band_controls():
    """Direct high precision exponentiation of a finite, compensated model.

    Bare h=[[m*eps^2,-sqrt(m)*eps],[-sqrt(m)*eps,1]]. Its exact Hermitian
    low eigenvalue is zero. In that eigenbasis, the loss is g|w><w| with
    w=(sqrt(m)*eps,1)/sqrt(1+m*eps^2). A third, zero-energy terminal state
    receives its loss, making the state a full no-event-plus-terminal ensemble.
    """
    m, g = mp.mpf(12), mp.mpf(4)
    delta, kappa = mp.mpf("1.25"), mp.mpf("0.03")
    epsilons = tuple(map(mp.mpf, ("0.04", "0.02", "0.01", "0.005")))
    times = tuple(map(mp.mpf, ("0.15", "0.6", "1.25")))
    rows = []
    for t in times:
        q_limit = mp.exp(-kappa * g * m * t)
        for eps in epsilons:
            w = mp.matrix([mp.sqrt(m)*eps, 1]) / mp.sqrt(1+m*eps**2)
            gamma = g * w * w.T
            energy = delta * eps**(-4) * (1+m*eps**2)
            ham = mp.matrix([[0, 0], [0, energy]])
            generator = -1j * ham - kappa * gamma / (2*eps**2)
            x, y = mp.expm(t*generator) * mp.matrix([1, 0])
            px, py = abs(x)**2, abs(y)**2
            p = px + py
            assert 0 < p <= 1
            conditional_mean = energy * py / p
            conditional_variance = energy**2 * px * py / p**2
            weighted_qfi = 4*p*conditional_variance
            d = 2*abs(x)*abs(y)*energy
            assert abs(d*d/p - weighted_qfi) < mp.mpf("1e-50")
            pinch_error = 2*abs(x)*abs(y)
            rho = mp.matrix([[px, x*mp.conj(y)], [y*mp.conj(x), py]])
            rho_pinched = mp.diag([px, py])
            mean_difference = sum(((rho-rho_pinched)*ham)[k, k] for k in range(2))
            m2_difference = sum(((rho-rho_pinched)*ham*ham)[k, k] for k in range(2))
            pinch_commutator = ham*rho_pinched-rho_pinched*ham
            assert mean_difference == m2_difference == 0
            assert all(z == 0 for z in pinch_commutator)
            coefficient = kappa*g*mp.sqrt(m)/(2*delta)
            graph_ratio = y/(1j*coefficient*eps**3*x)

            # Countercontrol: diagonalizing the loss by fiat removes the entire
            # high component. This exposes reliance on the physical H/Gamma
            # mismatch, rather than a generator eigenvalue used as energy.
            wrong = -1j*ham - kappa*mp.diag([gamma[0, 0], gamma[1, 1]])/(2*eps**2)
            _, wrong_y = mp.expm(t*wrong)*mp.matrix([1, 0])
            assert wrong_y == 0 and abs(y) > 0

            row = {
                "epsilon": to_float(eps), "time": to_float(t),
                "survival": to_float(p), "survival_limit": to_float(q_limit),
                "survival_relative_error": to_float(abs(p/q_limit-1)),
                "high_probability": to_float(py),
                "graph_ratio_real": to_float(graph_ratio),
                "graph_ratio_imag": float(mp.im(graph_ratio)),
                "conditional_mean": to_float(conditional_mean),
                "eps2_conditional_variance": to_float(eps**2*conditional_variance),
                "eps2_conditional_variance_target": to_float(kappa**2*g**2*m/4),
                "variance_relative_error": to_float(abs(
                    eps**2*conditional_variance/(kappa**2*g**2*m/4)-1)),
                "eps2_weighted_qfi": to_float(eps**2*weighted_qfi),
                "eps2_weighted_qfi_target": to_float(kappa**2*g**2*m*q_limit),
                "qfi_relative_error": to_float(abs(
                    eps**2*weighted_qfi/(kappa**2*g**2*m*q_limit)-1)),
                "pinch_error_over_eps3": to_float(pinch_error/eps**3),
                "pinch_error_over_eps3_target": to_float(kappa*g*mp.sqrt(m)*q_limit/delta),
                "commuting_loss_high_probability": to_float(abs(wrong_y)**2),
                "pinch_mean_difference": to_float(mean_difference),
                "pinch_second_moment_difference": to_float(m2_difference),
                "pinched_energy_commutator_norm": to_float(mp.norm(pinch_commutator)),
            }
            rows.append(row)

    for t in times:
        selected = [r for r in rows if r["time"] == to_float(t)]
        finest = selected[-1]
        assert finest["survival_relative_error"] < 0.001
        assert finest["variance_relative_error"] < 0.002
        assert finest["qfi_relative_error"] < 0.002
        assert abs(finest["graph_ratio_real"] - 1) < 0.001
        assert abs(finest["graph_ratio_imag"]) < 0.001
        for key in ("variance_relative_error", "qfi_relative_error"):
            assert selected[-1][key] < 0.3 * selected[-2][key]
            assert selected[-2][key] < 0.3 * selected[-3][key]

    return {
        "description": "Two-band consistency model only; not a finite-spin cube or joint-limit reproduction",
        "known_before_execution": "m=12 and g=4 from word derivation; predicted constants were not fitted",
        "precision_decimal_digits": mp.mp.dps,
        "parameters": {"delta": str(delta), "kappa": str(kappa), "m": str(m), "g": str(g)},
        "rows": rows,
    }


def main():
    result = {
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "mpmath": mp.__version__,
        "word_control": word_controls(),
        "two_band_control": two_band_controls(),
        "scope": "All assertions completed; corroboration of identified steps only, not an audit verdict",
    }
    destination = ROOT / "INDEPENDENT_CONTROL_RESULTS.json"
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
