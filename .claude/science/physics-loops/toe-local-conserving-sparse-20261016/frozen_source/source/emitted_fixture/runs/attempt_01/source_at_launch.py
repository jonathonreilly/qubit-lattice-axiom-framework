#!/usr/bin/env python3
"""One numerical emitted-word fixture, not interval arithmetic or a general proof.

Gate lists are chronological: list[0] acts first. Qubit zero is the most
significant bit. The last (fifth) qubit is the clean synthesis ancilla.
No old checker is imported. All emitted words and complete matrices are saved.
"""
import argparse
import collections
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np

TOL = 1.0e-9  # Fixed before execution; empirical discriminator, not proof bound.
M = 5
DIM = 1 << M
I2 = np.eye(2, dtype=np.complex128)
X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
Y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
Z = np.diag([1, -1]).astype(np.complex128)
SIGMA = (X, Y, Z)
DIAGNOSTICS = {"euler": [], "commutator": []}


def opnorm(a):
    return float(np.linalg.norm(a, ord=2))


def wrap(phi):
    return float((float(phi) + math.pi) % (2 * math.pi) - math.pi)


def zg(site, phi):
    return [{"kind": "Z", "sites": [int(site)], "phi": wrap(phi)}]


def ap(i, j, power=1):
    assert i != j and power >= 0
    return [{"kind": "A", "sites": [int(i), int(j)]} for _ in range(power)]


def product(*words):
    """Convert a left-to-right MATRIX product to a chronological gate list."""
    return [g for word in reversed(words) for g in word]


def ex(t0, t1, theta):
    # E(theta)=S0^* A Z0(theta/2) Z1(-theta/2) A^* S0.
    return product(zg(t0, math.pi / 4), ap(t0, t1),
                   zg(t0, theta / 2), zg(t1, -theta / 2),
                   ap(t0, t1, 7), zg(t0, -math.pi / 4))


def fword(c, t0, t1, dagger=False):
    # F=iSWAP(c,t1) iSWAP(t0,t1)^* iSWAP(c,t0).
    if not dagger:
        return product(ap(c, t1, 2), ap(t0, t1, 6), ap(c, t0, 2))
    return product(ap(c, t0, 6), ap(t0, t1, 2), ap(c, t1, 6))


def controlled_x(c, bit, t0, t1, theta):
    # Equation (9), including both independent F and F^* expansions.
    out = product(ex(t0, t1, theta / 2), fword(c, t0, t1, True),
                  zg(t1, math.pi / 4),
                  ex(t0, t1, ((-1) ** bit) * theta / 2),
                  zg(t1, -math.pi / 4), fword(c, t0, t1))
    assert len(out) == 50
    return out


def quaternion(u):
    a = float(np.trace(u).real / 2)
    v = np.array([float((np.trace(s @ u) / (2j)).real) for s in SIGMA])
    return a, v


def rotation(axis, theta):
    return math.cos(theta) * I2 + 1j * math.sin(theta) * axis


def euler_xyx(u):
    # For U=aI+i(bX+cY+dZ): a+ib=cos(beta)e^{i(gamma+alpha)},
    # c-id=sin(beta)e^{i(gamma-alpha)}. Explicit convention is tested below.
    a, v = quaternion(u)
    b, c, d = (float(x) for x in v)
    cb, sb = math.hypot(a, b), math.hypot(c, d)
    su = math.atan2(b, a) if cb > 1.0e-15 else 0.0
    di = math.atan2(-d, c) if sb > 1.0e-15 else 0.0
    beta = math.atan2(sb, cb)
    gamma, alpha = (su + di) / 2, (su - di) / 2
    reconstructed = rotation(X, gamma) @ rotation(Y, beta) @ rotation(X, alpha)
    err = opnorm(reconstructed - u)
    DIAGNOSTICS["euler"].append(err)
    assert err < 1.0e-12, ("Euler", err, u)
    return gamma, beta, alpha


def controlled_su2(c, bit, t0, t1, u):
    gamma, beta, alpha = euler_xyx(u)
    # S0 X S0^*=Y in the ordered |01>,|10> target subspace.
    cy = product(zg(t0, -math.pi / 4),
                 controlled_x(c, bit, t0, t1, beta), zg(t0, math.pi / 4))
    out = product(controlled_x(c, bit, t0, t1, gamma), cy,
                  controlled_x(c, bit, t0, t1, alpha))
    assert len(out) == 152
    return out


def commutator_factors(u):
    a, v = quaternion(u)
    s = float(np.linalg.norm(v))
    if s <= 1.0e-14:
        a0, b0 = (I2.copy(), 1j * X) if a >= 0 else (1j * Z, 1j * X)
    else:
        theta = math.atan2(s, a)
        axis = v / s
        coordinate = np.zeros(3)
        coordinate[int(np.argmin(np.abs(axis)))] = 1
        perpendicular = np.cross(axis, coordinate)
        perpendicular /= np.linalg.norm(perpendicular)
        vs = sum((axis[j] * SIGMA[j] for j in range(3)), np.zeros((2, 2), complex))
        ws = sum((perpendicular[j] * SIGMA[j] for j in range(3)), np.zeros((2, 2), complex))
        a0 = rotation(vs, theta / 2)
        b0 = 1j * ws
    err = opnorm(a0 @ b0 @ a0.conj().T @ b0.conj().T - u)
    DIAGNOSTICS["commutator"].append(err)
    assert err < 1.0e-12, ("commutator", err)
    return a0, b0


def controlled_many(controls, t0, t1, u):
    assert len(controls) >= 1
    if len(controls) == 1:
        c, bit = controls[0]
        return controlled_su2(c, bit, t0, t1, u)
    middle = len(controls) // 2
    c1, c2 = controls[:middle], controls[middle:]
    a0, b0 = commutator_factors(u)
    return product(controlled_many(c1, t0, t1, a0),
                   controlled_many(c2, t0, t1, b0),
                   controlled_many(c1, t0, t1, a0.conj().T),
                   controlled_many(c2, t0, t1, b0.conj().T))


def bits(number, n):
    return [(number >> (n - 1 - j)) & 1 for j in range(n)]


def two_level(b, bp, u):
    assert len(b) == len(bp) and sum(b) == sum(bp)
    zero_to_one = [j for j in range(len(b)) if b[j] == 0 and bp[j] == 1]
    one_to_zero = [j for j in range(len(b)) if b[j] == 1 and bp[j] == 0]
    assert len(zero_to_one) == len(one_to_zero) == 1  # q=1 fixture only.
    t0, t1 = zero_to_one[0], one_to_zero[0]
    controls = [(j, b[j]) for j in range(len(b)) if j not in (t0, t1)]
    return controlled_many(controls, t0, t1, u)


def route(word):
    out = []
    for logical_index, gate in enumerate(word):
        if gate["kind"] == "Z":
            out.append(dict(gate, logical_index=logical_index, route_role="onsite"))
            continue
        i, j = gate["sites"]
        if i < j:
            swaps = [(k, k + 1) for k in range(i, j - 1)]
            adjacent = [j - 1, j]
        else:
            swaps = [(k - 1, k) for k in range(i, j + 1, -1)]
            adjacent = [j + 1, j]
        for edge in swaps:
            out.append({"kind": "SWAP", "sites": list(edge),
                        "logical_index": logical_index, "route_role": "out"})
        out.append({"kind": "A", "sites": adjacent,
                    "logical_index": logical_index, "route_role": "local_A"})
        for edge in reversed(swaps):
            out.append({"kind": "SWAP", "sites": list(edge),
                        "logical_index": logical_index, "route_role": "return"})
    assert all(g["kind"] == "Z" or abs(g["sites"][0] - g["sites"][1]) == 1 for g in out)
    return out


def gate_matrix(gate):
    kind = gate["kind"]
    if kind == "Z":
        p = gate["phi"]
        return np.diag([np.exp(1j * p), np.exp(-1j * p)])
    if kind == "A":
        out = np.eye(4, dtype=complex)
        out[1:3, 1:3] = np.array([[1, 1j], [1j, 1]]) / math.sqrt(2)
        return out
    if kind == "SWAP":
        return np.eye(4, dtype=complex)[[0, 2, 1, 3]]
    raise ValueError(kind)


def positive_matrix(gate):
    # Independent finite Hermitian spectral exponential of the parent's Q.
    # This tests reserve scalars without simply multiplying the logical gate.
    kind = gate["kind"]
    if kind == "Z":
        p = gate["phi"]
        q = abs(p) * I2 - p * Z
    elif kind == "A":
        r = np.zeros((4, 4), dtype=complex)
        r[1, 2] = r[2, 1] = 1
        q = (math.pi / 4) * (np.eye(4) - r)
    elif kind == "SWAP":
        s = np.eye(4, dtype=complex)[[0, 2, 1, 3]]
        q = (math.pi / 2) * (np.eye(4) - s)
    else:
        raise ValueError(kind)
    values, vectors = np.linalg.eigh(q)
    assert values.min() >= -1.0e-14
    return (vectors * np.exp(-1j * values)) @ vectors.conj().T


def local_left(matrix, sites, state):
    """Apply a 1/2-qubit matrix to every column; MSB convention explicit."""
    width = state.shape[1]
    axes = list(sites) + [j for j in range(M) if j not in sites] + [M]
    tensor = state.reshape([2] * M + [width]).transpose(axes)
    applied = matrix @ tensor.reshape(1 << len(sites), -1)
    return applied.reshape([2] * M + [width]).transpose(np.argsort(axes)).reshape(DIM, width)


def execute(word, initial, positive=False):
    state = initial.copy()
    cache = {}
    for gate in word:
        key = (gate["kind"], gate.get("phi"))
        if key not in cache:
            cache[key] = positive_matrix(gate) if positive else gate_matrix(gate)
        state = local_left(cache[key], gate["sites"], state)
    return state


def residuals(actual, expected, selected):
    outside = [j for j in range(16) if j not in selected]
    return {
        "complete_isometry_operator_norm": opnorm(actual - expected),
        "complete_isometry_frobenius_norm": float(np.linalg.norm(actual - expected)),
        "maximum_column_l2_error": float(np.linalg.norm(actual - expected, axis=0).max()),
        "identity_off_selected_operator_norm": opnorm((actual - expected)[:, outside]),
        "ancilla_one_leakage_operator_norm": opnorm(actual[1::2]),
        "isometry_defect_operator_norm": opnorm(actual.conj().T @ actual - np.eye(16)),
    }


def save_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")
    return {"path": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size}


def recurrence(k):
    return 1 if k == 1 else 2 * recurrence(k // 2) + 2 * recurrence(k - k // 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    outdir = args.output
    outdir.mkdir(parents=True, exist_ok=True)
    z = (5 + 12j) / 13
    target_v = z * np.array([[3 / 5, 4j / 5], [4j / 5, 3 / 5]], dtype=complex)
    det_v = np.linalg.det(target_v)
    a, b = target_v[:, 0]
    radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
    givens = np.array([[a.conjugate(), b.conjugate()], [-b, a]], dtype=complex) / radius
    theta = float(np.angle(det_v))
    blocks = [(4, 8), (6, 12), (7, 14)]
    selected = sorted(j for pair in blocks for j in pair)
    target_u = np.eye(16, dtype=complex)
    logical, mutant = [], []
    segments = []
    for sector, (b0, b1) in enumerate(blocks, start=1):
        target_u[np.ix_([b0, b1], [b0, b1])] = target_v
        original = bits(b1, 4) + [0]
        partner = original.copy()
        partner[0], partner[4] = 0, 1
        phase = two_level(original, partner, np.diag([np.exp(1j * theta), np.exp(-1j * theta)]))
        gu = two_level(bits(b0, 4), bits(b1, 4), givens.conj().T)
        # V=G^* D: D MUST act first in a chronological list.
        segments.append({"sector": sector, "basis_pair": [b0, b1],
                         "phase_start": len(logical), "phase_count": len(phase),
                         "givens_start": len(logical) + len(phase), "givens_count": len(gu)})
        logical += phase + gu
        mutant += gu  # Load-bearing mutation: omit ALL determinant compensations.
    routed, routed_mutant = route(logical), route(mutant)
    expected_g0 = 3 * (152 * recurrence(2) + 152 * recurrence(3))
    expected_gbar = 7 * expected_g0
    assert expected_g0 == 6384 and expected_gbar == 44688
    assert len(logical) == expected_g0
    assert len(routed) <= expected_gbar
    words = {
        "logical": save_json(outdir / "logical_word.json", logical),
        "routed": save_json(outdir / "routed_word.json", routed),
        "mutant_logical": save_json(outdir / "mutant_logical_word.json", mutant),
        "mutant_routed": save_json(outdir / "mutant_routed_word.json", routed_mutant),
        "segments": save_json(outdir / "segments.json", segments),
    }
    j = np.zeros((32, 16), dtype=complex)
    j[np.arange(16) * 2, np.arange(16)] = 1
    expected = j @ target_u
    logical_u = execute(logical, np.eye(32, dtype=complex))
    routed_u = execute(routed, np.eye(32, dtype=complex))
    routed_isometry = routed_u @ j
    mutant_isometry = execute(routed_mutant, j)
    positive_isometry = execute(routed, j, positive=True)
    counts = {name: dict(collections.Counter(g["kind"] for g in word))
              for name, word in [("logical", logical), ("routed", routed),
                                 ("mutant_logical", mutant), ("mutant_routed", routed_mutant)]}
    phase_phi = counts["routed"]["A"] * math.pi / 4 + math.fsum(
        abs(g["phi"]) for g in routed if g["kind"] == "Z")
    positive_expected = np.exp(-1j * phase_phi) * routed_isometry
    # Concrete endpoint illustration in declared units: hbar=1, h=1, E0=1/5,
    # Delta=7/10. Choose g=4Q*, sigma=4piQ*, so parent h inequality holds.
    # Use EXACT integer rational r from this fixture's floating x/(2pi), and
    # record the observed margin; this remains numerical evidence only.
    hbar, h, e0, delta = 1.0, 1.0, 0.2, 0.7
    tau = (len(routed) + 1) * h
    x = delta * tau / hbar
    r = round(x / (2 * math.pi) * 16) / 16
    k = math.floor(r) + 2
    lam = 2 * math.pi * k - x
    assert abs(r - x / (2 * math.pi)) <= 0.25
    assert 1.5 * math.pi < lam <= 4.5 * math.pi
    number = np.array([sum(bits(jj, M)) for jj in range(32)])
    free_energy = e0 + delta * number
    endpoint = np.exp(-1j * tau * free_energy)[:, None] * (
        np.exp(-1j * lam * number)[:, None] * positive_isometry)
    gamma = np.exp(-1j * (e0 * tau + phase_phi))
    nominal = residuals(routed_isometry, expected, selected)
    mutation = residuals(mutant_isometry, expected, selected)
    result = {
        "status": "numerical_fixture_only_not_certified_interval_arithmetic",
        "dtype": "numpy.complex128", "machine_epsilon": float(np.finfo(float).eps),
        "threshold_fixed_before_execution": TOL,
        "python": sys.version, "numpy": np.__version__, "platform": platform.platform(),
        "parameters": {"q": 1, "L": 1, "M_reservoir": 3, "n_data": 4, "m_with_ancilla": 5},
        "qubit_order": "MSB first, clean ancilla is site 4/least significant bit",
        "target": {"formula": "((5+12i)/13)*[[3/5,4i/5],[4i/5,3/5]]",
                   "determinant_exact": "(-119+120i)/169",
                   "determinant_numeric": [float(det_v.real), float(det_v.imag)],
                   "determinant_theta": theta, "selected_pairs": blocks,
                   "givens_residual": opnorm(givens @ target_v - np.diag([1, det_v])),
                   "givens_unitarity": opnorm(givens.conj().T @ givens - I2),
                   "target_unitarity": opnorm(target_u.conj().T @ target_u - np.eye(16))},
        "counts": {"by_kind": counts, "logical_total": len(logical), "routed_total": len(routed),
                   "mutant_logical_total": len(mutant), "mutant_routed_total": len(routed_mutant),
                   "G0": expected_g0, "Gbar": expected_gbar,
                   "tight_uniform_route_bound": counts["logical"]["Z"] + 7 * counts["logical"]["A"],
                   "T2": recurrence(2), "T3": recurrence(3)},
        "nominal": nominal,
        "all_32_input_routing_operator_residual": opnorm(routed_u - logical_u),
        "all_32_input_number_commutator": opnorm(number[:, None] * routed_u - routed_u * number[None, :]),
        "logical_isometry_residual": opnorm(logical_u @ j - expected),
        "mutant_omit_determinant_compensation": mutation,
        "mutant_exact_expected_operator_error": "24/13",
        "mutant_error_difference_from_24_over_13": abs(mutation["complete_isometry_operator_norm"] - 24/13),
        "maximum_internal_euler_residual": max(DIAGNOSTICS["euler"]),
        "number_internal_euler_checks": len(DIAGNOSTICS["euler"]),
        "maximum_internal_commutator_residual": max(DIAGNOSTICS["commutator"]),
        "number_internal_commutator_checks": len(DIAGNOSTICS["commutator"]),
        "scalar": {"logical_scalar": [1, 0], "positive_reserve_phase_Phi": phase_phi,
                   "positive_word_residual": opnorm(positive_isometry - positive_expected),
                   "Phi_includes_all_A_and_Z_reserves": True,
                   "SWAP_positive_generator_exp_is_full_SWAP": True},
        "endpoint_illustration": {"hbar": hbar, "h": h, "E0": e0, "Delta": delta,
                                  "Q_star": 6 * math.pi, "g": 24 * math.pi, "sigma": 24 * math.pi**2,
                                  "tau": tau, "r": r, "k": k, "lambda": lam,
                                  "gamma": [float(gamma.real), float(gamma.imag)],
                                  "operator_residual": opnorm(endpoint - gamma * expected),
                                  "maximum_free_energy": float(free_energy.max()),
                                  "ideal_common_added_incident_cap": delta + 12 * math.pi,
                                  "absolute_work_upper_bound": 24 * math.pi * (len(routed) + M),
                                  "whole_free_energy_commutation_is_exact_by_gate_definition": True},
        "words": words,
    }
    np.savez_compressed(outdir / "complete_matrices.npz", target_v=target_v, givens=givens,
                        target_u=target_u, input_j=j, expected=expected,
                        logical_u=logical_u, routed_u=routed_u, routed_isometry=routed_isometry,
                        mutant_isometry=mutant_isometry, positive_isometry=positive_isometry,
                        endpoint=endpoint)
    save_json(outdir / "RESULT.json", result)
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    assert all(value < TOL for value in nominal.values())
    assert result["all_32_input_routing_operator_residual"] < TOL
    assert result["all_32_input_number_commutator"] < TOL
    assert result["scalar"]["positive_word_residual"] < TOL
    assert result["endpoint_illustration"]["operator_residual"] < TOL
    assert mutation["complete_isometry_operator_norm"] > 1.0
    assert result["mutant_error_difference_from_24_over_13"] < TOL
    print("All predeclared fixture discriminators satisfied; numerical evidence only.", flush=True)


if __name__ == "__main__":
    main()
