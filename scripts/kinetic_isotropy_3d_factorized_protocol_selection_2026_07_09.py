#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
3D factorized-protocol selection on the analyzed period-2 classes.

The runner constructs every protocol both on the 2^3 Bloch cell and on an
L=4 site ring.  It probes the complete inventory before applying any
selection gate.  All verdicts below are computed from those constructions.
"""
from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp


PASS, FAIL = 0, 0
TOL = 1.0e-10
L = 4


def check(label, ok, detail=""):
    """Record one computed boolean."""
    global PASS, FAIL
    verdict = bool(ok)
    if verdict:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def heading(text):
    print(f"\n{text}")
    print("=" * 96)


# ---------------------------------------------------------------------------
# (S1) Reused constructions and inventory unitarity
comps = list(itertools.product((0, 1), repeat=3))
idx = {p: i for i, p in enumerate(comps)}


def eta_val(mu, p):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** p[0]
    return (-1) ** (p[0] + p[1])


# Recomputed site-license degree table on the 2^3 cell.
allowed = {}
for ptgt in comps:
    for qsrc in comps:
        offsets = []
        for dj in itertools.product((-1, 0, 1), repeat=3):
            distance = sum(abs((qsrc[a] + 2 * dj[a]) - ptgt[a]) for a in range(3))
            if distance <= 1:
                offsets.append(dj)
        allowed[(ptgt, qsrc)] = offsets


def S_axis(kvec, axis, decorated=True):
    S = np.zeros((8, 8), dtype=complex)
    for p in comps:
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        phase = np.exp(-1j * kvec[axis]) if p[axis] == 0 else 1.0
        S[idx[p], idx[q]] += (eta_val(axis, q) if decorated else 1.0) * phase
    return S


def S_axis_reverse(kvec, axis, decorated=True):
    """Opposite mover, constructed by its reversed offset convention."""
    S = np.zeros((8, 8), dtype=complex)
    for p in comps:
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        phase = np.exp(+1j * kvec[axis]) if p[axis] == 1 else 1.0
        S[idx[p], idx[q]] += (eta_val(axis, q) if decorated else 1.0) * phase
    return S


def mixed_cycle_tick(kvec):
    Um = np.zeros((8, 8), dtype=complex)
    cycle0 = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    moves = ["across", "across", "within", "within"]
    for i, move in enumerate(moves):
        src, tgt = cycle0[i], cycle0[(i + 1) % 4]
        axis = [a for a in range(3) if src[a] != tgt[a]][0]
        sign = +1 if tgt[axis] == 1 else -1
        phase = np.exp(1j * sign * kvec[axis]) if move == "across" else 1.0
        Um[idx[tgt], idx[src]] = phase
    cycle1 = [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
    for i in range(4):
        src, tgt = cycle1[i], cycle1[(i + 1) % 4]
        Um[idx[tgt], idx[src]] = 1.0
    return Um


def staircase(kvec):
    W = np.zeros((8, 8), dtype=complex)
    for p in comps:
        axis = 0 if (p[0] + p[1]) % 2 == 0 else 1
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        sign = +1 if q[axis] == 1 else -1
        phase = np.exp(1j * sign * kvec[axis]) if q[axis] == 0 else 1.0
        W[idx[q], idx[p]] = phase
    return W


THETA = np.pi / 5


def pairing_bloch(kvec, axis):
    M = np.zeros((8, 8), dtype=complex)
    for p in comps:
        ql = list(p)
        ql[axis] ^= 1
        q = tuple(ql)
        phase = np.exp(+1j * kvec[axis]) if p[axis] == 1 else np.exp(-1j * kvec[axis])
        M[idx[q], idx[p]] = phase
    return M


def pairflat_bloch(kvec):
    P = np.eye(8, dtype=complex)
    for axis in range(3):
        M = pairing_bloch(kvec, axis)
        P = P @ (np.cos(THETA) * np.eye(8) + 1j * np.sin(THETA) * M)
    return P


def diag_bloch(_kvec):
    return np.diag([np.exp(1j * THETA * ((-1) ** sum(p))) for p in comps])


coords = list(itertools.product(range(L), repeat=3))
site_idx = {x: i for i, x in enumerate(coords)}


def shifted(x, axis, amount):
    y = list(x)
    y[axis] = (y[axis] + amount) % L
    return tuple(y)


def site_shift(axis, direction, decorated=True):
    F = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        target = shifted(source, axis, direction)
        parity = tuple(v % 2 for v in source)
        phase = eta_val(axis, parity) if decorated else 1.0
        F[site_idx[target], site_idx[source]] = phase
    return F


def site_mixed_cycle():
    F = np.zeros((L**3, L**3), dtype=complex)
    cycles = {
        0: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
        1: [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)],
    }
    for source in coords:
        p = tuple(v % 2 for v in source)
        cycle = cycles[p[2]]
        i = cycle.index(p)
        q = cycle[(i + 1) % 4]
        axis = [a for a in range(3) if p[a] != q[a]][0]
        amount = -1 if p[2] == 0 else q[axis] - p[axis]
        target = shifted(source, axis, amount)
        F[site_idx[target], site_idx[source]] = 1.0
    return F


def site_staircase():
    F = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        p = tuple(v % 2 for v in source)
        axis = 0 if (p[0] + p[1]) % 2 == 0 else 1
        target = shifted(source, axis, +1)
        F[site_idx[target], site_idx[source]] = 1.0
    return F


def site_pairing(axis):
    M = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        amount = +1 if source[axis] % 2 == 1 else -1
        target = shifted(source, axis, amount)
        M[site_idx[target], site_idx[source]] = 1.0
    return M


def site_pairflat():
    P = np.eye(L**3, dtype=complex)
    for axis in range(3):
        M = site_pairing(axis)
        P = P @ (np.cos(THETA) * np.eye(L**3) + 1j * np.sin(THETA) * M)
    return P


def site_diagonal():
    return np.diag([
        np.exp(1j * THETA * ((-1) ** sum(v % 2 for v in x))) for x in coords
    ])


def compose(matrices, dimension):
    out = np.eye(dimension, dtype=complex)
    for matrix in matrices:
        out = out @ matrix
    return out


def forward(axis, decorated=True):
    return lambda kvec: S_axis(kvec, axis, decorated)


def reverse(axis, decorated=True):
    return lambda kvec: S_axis_reverse(kvec, axis, decorated)


site_forward = [site_shift(a, +1, decorated=True) for a in range(3)]
site_reverse = [site_shift(a, -1, decorated=True) for a in range(3)]

protocols = {
    "P_SYM": {
        "bloch_factors": [forward(0), forward(1), forward(2)],
        "site_factors": [site_forward[0], site_forward[1], site_forward[2]],
    },
    "P_SYM_OCT": {
        "bloch_factors": [reverse(0), forward(1), forward(2)],
        "site_factors": [site_reverse[0], site_forward[1], site_forward[2]],
    },
    "P_REORDER": {
        "bloch_factors": [forward(1), forward(0), forward(2)],
        "site_factors": [site_forward[1], site_forward[0], site_forward[2]],
    },
    "P_WEIGHT": {
        "bloch_factors": [forward(0), forward(0), forward(1), forward(2)],
        "site_factors": [site_forward[0], site_forward[0], site_forward[1], site_forward[2]],
    },
    "P_AXIS": {
        "bloch_factors": [forward(0)],
        "site_factors": [site_forward[0]],
    },
    "P_MIX4": {
        "bloch_factors": [mixed_cycle_tick],
        "site_factors": [site_mixed_cycle()],
    },
    "P_STAIR": {
        "bloch_factors": [staircase],
        "site_factors": [site_staircase()],
    },
    "P_PAIRFLAT": {
        "bloch_factors": [pairflat_bloch],
        "site_factors": [site_pairflat()],
    },
    "P_CANCEL": {
        "bloch_factors": [forward(0), reverse(0), forward(1), reverse(1), forward(2), reverse(2)],
        "site_factors": [site_forward[0], site_reverse[0], site_forward[1], site_reverse[1], site_forward[2], site_reverse[2]],
    },
    "P_DIAG": {
        "bloch_factors": [diag_bloch],
        "site_factors": [site_diagonal()],
    },
}


def bloch_protocol(name, kvec):
    return compose([f(kvec) for f in protocols[name]["bloch_factors"]], 8)


def site_protocol(name):
    return compose(protocols[name]["site_factors"], L**3)


rng = np.random.default_rng(20260709)
sample_k = [tuple(row) for row in rng.uniform(0.17, 2.63, size=(5, 3))]

heading("(S1) REUSED CONSTRUCTIONS AND UNITARITY")
diag_const = all(allowed[(p, p)] == [(0, 0, 0)] for p in comps)
partner_shape = all(
    len(allowed[(p, q)]) == (2 if sum(abs(p[a] - q[a]) for a in range(3)) == 1 else 0)
    for p in comps for q in comps if p != q
)
check(
    "site-license degree table has constant diagonals and two own-axis offsets for parity partners",
    diag_const and partner_shape,
)

eye8 = np.eye(8)
eye64 = np.eye(L**3)
for name in protocols:
    bloch_errors = []
    factor_errors = []
    for kvec in sample_k:
        U = bloch_protocol(name, kvec)
        bloch_errors.append(np.max(np.abs(U @ U.conj().T - eye8)))
        factor_errors.extend(
            np.max(np.abs(f(kvec) @ f(kvec).conj().T - eye8))
            for f in protocols[name]["bloch_factors"]
        )
    site_factors_now = protocols[name]["site_factors"]
    site_errors = [np.max(np.abs(F @ F.conj().T - eye64)) for F in site_factors_now]
    site_errors.append(np.max(np.abs(site_protocol(name) @ site_protocol(name).conj().T - eye64)))
    maximum = max(bloch_errors + factor_errors + site_errors)
    check(f"{name} is unitary on the Bloch cell and the L=4 ring, including every factor", maximum < TOL, f"max error={maximum:.3g}")

bare_axis_bloch = all(
    np.max(np.abs(S_axis(k, 0, False) @ S_axis(k, 0, False).conj().T - eye8)) < TOL
    for k in sample_k
)
bare_axis_site = np.max(np.abs(site_shift(0, +1, False) @ site_shift(0, +1, False).conj().T - eye64)) < TOL
check("P_AXIS bare and decorated forms are both unitary", bare_axis_bloch and bare_axis_site)

reverse_direct_ok = all(
    np.max(np.abs(S_axis_reverse(k, 0, True) - S_axis(k, 0, True).conj().T)) < TOL
    for k in sample_k
)
reverse_site_ok = np.max(np.abs(site_reverse[0] - site_forward[0].conj().T)) < TOL
check("the P_SYM_OCT opposite mover was directly constructed and matches the inverse mover", reverse_direct_ok and reverse_site_ok)


# ---------------------------------------------------------------------------
# Property computations used by the probe table and later gates.
translations = []
for axis in range(3):
    T = np.zeros((L**3, L**3), dtype=complex)
    for source in coords:
        T[site_idx[shifted(source, axis, +1)], site_idx[source]] = 1.0
    translations.append(T)


def factor_translation_defect(F):
    defects = [
        np.max(np.abs(np.abs(T @ F @ T.conj().T) - np.abs(F)))
        for T in translations
    ]
    return max(defects)


def protocol_translation_defect(name):
    return max(factor_translation_defect(F) for F in protocols[name]["site_factors"])


def is_nearest_neighbor_pair(target, source, axis):
    same_transverse = all(target[a] == source[a] for a in range(3) if a != axis)
    delta = (target[axis] - source[axis]) % L
    return same_transverse and delta in (1, L - 1)


def conditioning_vector_from_factors(factors):
    vector = []
    for axis in range(3):
        occupied = any(
            abs(F[site_idx[target], site_idx[source]]) > TOL
            for F in factors
            for source in coords
            for target in coords
            if is_nearest_neighbor_pair(target, source, axis)
        )
        vector.append(int(occupied))
    return tuple(vector)


dispersion_k = [
    (0.31, 0.73, 1.17),
    (1.09, 0.73, 1.17),
    (0.31, 1.43, 1.17),
    (0.31, 0.73, 2.11),
]


def dispersion_measure_from_function(function):
    coefficients = [np.poly(function(kvec)) for kvec in dispersion_k]
    return max(np.max(np.abs(c - coefficients[0])) for c in coefficients[1:])


properties = {}
for name in protocols:
    vector = conditioning_vector_from_factors(protocols[name]["site_factors"])
    measure = dispersion_measure_from_function(lambda kvec, n=name: bloch_protocol(n, kvec))
    properties[name] = {
        "defect": protocol_translation_defect(name),
        "nonvacuity": vector,
        "axis_uniform": len(set(vector)) == 1,
        "dispersion_measure": measure,
        "dispersive": measure > 1.0e-7,
    }


heading("(S2) FULL PROTOCOL PROPERTY PROBE TABLE -- PRINTED BEFORE SELECTION GATES")
print(f"{'protocol':<12} {'factor translation defect':>27}  {'per-axis nonvacuity':>22}  {'axis-uniform':>13}  {'dispersive':>11}")
print("-" * 96)
for name, prop in properties.items():
    defect_text = "0" if prop["defect"] < TOL else f"{prop['defect']:.6g}"
    vector_text = "[" + ",".join(str(x) for x in prop["nonvacuity"]) + "]"
    print(
        f"{name:<12} {defect_text:>27}  {vector_text:>22}  "
        f"{('yes' if prop['axis_uniform'] else 'no'):>13}  "
        f"{('YES' if prop['dispersive'] else 'NO'):>11}"
    )


# ---------------------------------------------------------------------------
heading("(S3) TRANSLATION-DEFECT COMPUTATIONS")
expected_zero = {"P_SYM", "P_SYM_OCT", "P_REORDER", "P_WEIGHT", "P_AXIS", "P_CANCEL", "P_DIAG"}
computed_zero = {name for name, prop in properties.items() if prop["defect"] < TOL}
check("zero-defect protocols equal the specified translation-clause set", computed_zero == expected_zero, f"computed={sorted(computed_zero)}")
positive_rejectors = all(properties[name]["defect"] > TOL for name in ("P_MIX4", "P_STAIR", "P_PAIRFLAT"))
check("P_MIX4, P_STAIR, and P_PAIRFLAT have positive site-modulus translation defects", positive_rejectors)


# ---------------------------------------------------------------------------
heading("(S4) CONDITIONING NONVACUITY VECTORS")
expected_vectors = {
    "P_SYM": (1, 1, 1),
    "P_SYM_OCT": (1, 1, 1),
    "P_REORDER": (1, 1, 1),
    "P_WEIGHT": (1, 1, 1),
    "P_AXIS": (1, 0, 0),
    "P_MIX4": (1, 1, 0),
    "P_STAIR": (1, 1, 0),
    "P_PAIRFLAT": (1, 1, 1),
    "P_CANCEL": (1, 1, 1),
    "P_DIAG": (0, 0, 0),
}
computed_vectors = {name: prop["nonvacuity"] for name, prop in properties.items()}
check("all per-axis nonvacuity vectors match the site-level nearest-neighbor support probe", computed_vectors == expected_vectors)
uniform_names = {name for name, prop in properties.items() if prop["axis_uniform"]}
expected_uniform = {"P_SYM", "P_SYM_OCT", "P_REORDER", "P_WEIGHT", "P_PAIRFLAT", "P_CANCEL", "P_DIAG"}
check("axis-uniform protocols are exactly the all-axis and vacuous patterns", uniform_names == expected_uniform)


# ---------------------------------------------------------------------------
heading("(S5) FLATNESS, DISPERSIVENESS, AND SLOPES")
expected_dispersive = {"P_SYM", "P_SYM_OCT", "P_REORDER", "P_WEIGHT", "P_AXIS", "P_MIX4", "P_STAIR"}
computed_dispersive = {name for name, prop in properties.items() if prop["dispersive"]}
check("dispersive protocols match the momentum-dependent characteristic-polynomial probe", computed_dispersive == expected_dispersive, f"computed={sorted(computed_dispersive)}")

square_identity = all(
    np.max(np.abs(S_axis(k, axis, True) @ S_axis(k, axis, True) - np.exp(-1j * k[axis]) * eye8)) < TOL
    for axis in range(3) for k in sample_k
)
reverse_square_identity = all(
    np.max(np.abs(S_axis_reverse(k, 0, True) @ S_axis_reverse(k, 0, True) - np.exp(+1j * k[0]) * eye8)) < TOL
    for k in sample_k
)
check("decorated mover squares give the independent central targets exp(-ik_i), with exp(+ik_1) for the reversed mover", square_identity and reverse_square_identity)

mix_block0 = [idx[p] for p in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]]
mix_block1 = [idx[p] for p in [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]]
mix_power_ok = all(
    np.max(np.abs(
        np.linalg.matrix_power(mixed_cycle_tick(k), 4)
        - np.diag([
            np.exp(1j * (k[0] + k[1])) if i in mix_block0 else 1.0
            for i in range(8)
        ])
    )) < TOL
    for k in sample_k
)
stair_power_ok = all(
    np.max(np.abs(
        np.linalg.matrix_power(staircase(k), 4)
        - np.exp(-1j * (k[0] + k[1])) * eye8
    )) < TOL
    for k in sample_k
)

K1, K2, K3 = sp.symbols("k1 k2 k3", real=True)
mix_phase = (K1 + K2) / 4
stair_phase = -(K1 + K2) / 4
mix_slopes_site = tuple(sp.simplify(2 * sp.diff(mix_phase, q)) for q in (K1, K2, K3))
stair_slopes_site = tuple(sp.simplify(2 * sp.diff(stair_phase, q)) for q in (K1, K2, K3))
nonunit_target = (sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(0, 1))
check(
    "P_MIX4 and P_STAIR fourth-power identities recompute site-slope magnitudes (1/2,1/2,0)",
    mix_power_ok and stair_power_ok
    and tuple(abs(v) for v in mix_slopes_site) == nonunit_target
    and tuple(abs(v) for v in stair_slopes_site) == nonunit_target,
)

sym_square_ok = all(
    np.max(np.abs(
        bloch_protocol("P_SYM", k) @ bloch_protocol("P_SYM", k)
        + np.exp(-1j * sum(k)) * eye8
    )) < TOL
    for k in sample_k
)
oct_square_ok = all(
    np.max(np.abs(
        bloch_protocol("P_SYM_OCT", k) @ bloch_protocol("P_SYM_OCT", k)
        + np.exp(1j * k[0] - 1j * k[1] - 1j * k[2]) * eye8
    )) < TOL
    for k in sample_k
)
weight_square_ok = all(
    np.max(np.abs(
        bloch_protocol("P_WEIGHT", k) @ bloch_protocol("P_WEIGHT", k)
        + np.exp(-1j * (2 * k[0] + k[1] + k[2])) * eye8
    )) < TOL
    for k in sample_k
)
sym_word_slopes = tuple(abs(sp.simplify(2 * sp.diff(-(K1 + K2 + K3) / 2, q))) for q in (K1, K2, K3))
oct_word_slopes = tuple(abs(sp.simplify(2 * sp.diff((K1 - K2 - K3) / 2, q))) for q in (K1, K2, K3))
weight_word_slopes = tuple(abs(sp.simplify(2 * sp.diff(-(2 * K1 + K2 + K3) / 2, q))) for q in (K1, K2, K3))
check("symmetric and octant cycle word slopes have magnitude one edge/tick on every axis", sym_square_ok and oct_square_ok and sym_word_slopes == (1, 1, 1) and oct_word_slopes == (1, 1, 1))
check("P_WEIGHT composite slopes are computed as (2,1,1), not (1,1,1)", weight_square_ok and weight_word_slopes == (2, 1, 1))

cancel_identity = all(
    np.max(np.abs(bloch_protocol("P_CANCEL", k) - eye8)) < TOL
    for k in sample_k
)
cancel_site_identity = np.max(np.abs(site_protocol("P_CANCEL") - eye64)) < TOL
check("P_CANCEL pairs opposite movers on every axis and is the diagonal flat identity word", cancel_identity and cancel_site_identity)


# ---------------------------------------------------------------------------
heading("(S6) P_PAIRFLAT CONSTRUCTION FACTS")
pair_facts = []
for k in sample_k:
    Ms = [pairing_bloch(k, axis) for axis in range(3)]
    hermitian = all(np.max(np.abs(M - M.conj().T)) < TOL for M in Ms)
    involutions = all(np.max(np.abs(M @ M - eye8)) < TOL for M in Ms)
    commuting = all(np.max(np.abs(Ms[i] @ Ms[j] - Ms[j] @ Ms[i])) < TOL for i in range(3) for j in range(i + 1, 3))
    pair_facts.append(hermitian and involutions and commuting)
check("the three P_PAIRFLAT M_i are commuting Hermitian unitaries", all(pair_facts))

expected_pair_roots = [
    np.exp(1j * THETA * sum(signs))
    for signs in itertools.product((-1, 1), repeat=3)
]
expected_pair_poly = np.poly(expected_pair_roots)
pair_unitary_flat = all(
    np.max(np.abs(pairflat_bloch(k) @ pairflat_bloch(k).conj().T - eye8)) < TOL
    and np.max(np.abs(np.poly(pairflat_bloch(k)) - expected_pair_poly)) < 1.0e-8
    for k in sample_k
)
check("P_PAIRFLAT is unitary with the k-independent bands exp(i theta sum_i +/-1)", pair_unitary_flat)

P12 = np.zeros((8, 8), dtype=complex)
for p in comps:
    P12[idx[(p[1], p[0], p[2])], idx[p]] = 1.0
pair_p12_covariant = all(
    np.max(np.abs(
        P12 @ pairflat_bloch(k) @ P12.T
        - pairflat_bloch((k[1], k[0], k[2]))
    )) < TOL
    for k in sample_k
)
check("P_PAIRFLAT is axis-permutation covariant under the computed P12 conjugation", pair_p12_covariant)

Vg = np.diag([(-1.0) ** (p[0] * p[1]) for p in comps]).astype(complex)
projective_covariance = all(
    np.max(np.abs(
        P12 @ S_axis(k, 0, True) @ P12.T
        - Vg @ S_axis((k[1], k[0], k[2]), 1, True) @ Vg
    )) < TOL
    for k in sample_k
)
check("decorated per-axis factors satisfy the P12 plus diagonal-gauge projective covariance check", projective_covariance)


# ---------------------------------------------------------------------------
heading("(S7) SELECTION GATES G1-G5")


def run_gates(prop_map):
    g1 = {name for name, prop in prop_map.items() if prop["defect"] < TOL}
    g2 = {
        name for name in g1
        if prop_map[name]["axis_uniform"] and any(prop_map[name]["nonvacuity"])
    }
    g3 = {name for name in g2 if prop_map[name]["dispersive"]}
    return g1, g2, g3


G1, G2, G3 = run_gates(properties)
expected_G1 = {"P_SYM", "P_SYM_OCT", "P_REORDER", "P_WEIGHT", "P_AXIS", "P_CANCEL", "P_DIAG"}
expected_G2 = {"P_SYM", "P_SYM_OCT", "P_REORDER", "P_WEIGHT", "P_CANCEL"}
expected_G3 = {"P_SYM", "P_SYM_OCT", "P_REORDER", "P_WEIGHT"}
check("G1 translation-clause survivors", G1 == expected_G1, f"computed={sorted(G1)}")
check("G2 translation plus nonvacuous all-axes-uniform survivors", G2 == expected_G2, f"computed={sorted(G2)}")
check("G3 adds the named dispersiveness conditional", G3 == expected_G3, f"computed={sorted(G3)}")

bare_commuting = all(
    np.max(np.abs(S_axis(k, i, False) @ S_axis(k, j, False) - S_axis(k, j, False) @ S_axis(k, i, False))) < TOL
    for k in sample_k for i in range(3) for j in range(i + 1, 3)
)
decorated_anticommuting = all(
    np.max(np.abs(S_axis(k, i, True) @ S_axis(k, j, True) + S_axis(k, j, True) @ S_axis(k, i, True))) < TOL
    for k in sample_k for i in range(3) for j in range(i + 1, 3)
)
reorder_identity = all(
    np.max(np.abs(bloch_protocol("P_REORDER", k) + bloch_protocol("P_SYM", k))) < TOL
    for k in sample_k
)
weight_identity = all(
    np.max(np.abs(
        bloch_protocol("P_WEIGHT", k)
        - np.exp(-1j * k[0]) * (S_axis(k, 1, True) @ S_axis(k, 2, True))
    )) < TOL
    for k in sample_k
)
check("G4 ingredients: decorated anticommutation, central reorder sign, and S1^2 weight identity", decorated_anticommuting and reorder_identity and weight_identity)


def scalar_multiple(A, B):
    ratio = A @ B.conj().T
    scalar = np.trace(ratio) / ratio.shape[0]
    return np.max(np.abs(ratio - scalar * np.eye(ratio.shape[0]))) < TOL


weight_central_times_symmetric = all(
    scalar_multiple(bloch_protocol("P_WEIGHT", k), bloch_protocol("P_SYM", k))
    for k in sample_k
)
g4_claim = decorated_anticommuting and reorder_identity and weight_identity and weight_central_times_symmetric
check(
    "G4 divergence is detected: the specified P_WEIGHT is not the symmetric three-axis cycle times a central scalar",
    (not g4_claim) and (not weight_central_times_symmetric),
)

all_survivor_word_slopes_one = (
    sym_word_slopes == (1, 1, 1)
    and oct_word_slopes == (1, 1, 1)
    and weight_word_slopes == (1, 1, 1)
)
factor_shift_slopes_one = square_identity and reverse_square_identity
check(
    "G5 divergence is detected: factor slopes are one, but the P_WEIGHT composite has slope magnitudes (2,1,1)",
    factor_shift_slopes_one and (not all_survivor_word_slopes_one) and weight_word_slopes == (2, 1, 1),
)


# ---------------------------------------------------------------------------
heading("(S8) REFUTATION AND REJECTOR LEGS L1-L6")

# L1 distinguishes the variation-only filter from a literal G1-only
# ablation, which retains the G2 axis-uniformity test.
variation_only = {
    name for name, prop in properties.items()
    if any(prop["nonvacuity"]) and prop["dispersive"]
}
literal_drop_translation = {
    name for name, prop in properties.items()
    if prop["axis_uniform"] and any(prop["nonvacuity"]) and prop["dispersive"]
}
l1_variation_only = {"P_MIX4", "P_STAIR"} <= variation_only
l1_literal = {"P_MIX4", "P_STAIR"} <= literal_drop_translation
check("L1 variation-only filter admits P_MIX4 and P_STAIR with nonunit computed slopes", l1_variation_only and mix_power_ok and stair_power_ok)
check("L1 divergence is detected: dropping only G1 while retaining axis-uniformity does not admit P_MIX4 or P_STAIR", (not l1_literal) and literal_drop_translation == expected_G3)

drop_axis_uniformity = {
    name for name in G1
    if any(properties[name]["nonvacuity"]) and properties[name]["dispersive"]
}
check("L2 dropping axis-uniformity admits P_AXIS", "P_AXIS" in drop_axis_uniformity)

drop_dispersiveness = G2
cancel_flat = not properties["P_CANCEL"]["dispersive"]
check("L3 dropping dispersiveness admits the flat P_CANCEL word", "P_CANCEL" in drop_dispersiveness and cancel_flat)

l4_properties = (
    pair_p12_covariant
    and properties["P_PAIRFLAT"]["nonvacuity"] == (1, 1, 1)
    and properties["P_PAIRFLAT"]["axis_uniform"]
    and not properties["P_PAIRFLAT"]["dispersive"]
    and properties["P_PAIRFLAT"]["defect"] > TOL
)
check("L4 P_PAIRFLAT is covariant, all-axes varying, flat, and translation-defective", l4_properties)

bare_site_factors = [site_shift(a, +1, False) for a in range(3)]
bare_defect = max(factor_translation_defect(F) for F in bare_site_factors)
bare_vector = conditioning_vector_from_factors(bare_site_factors)
bare_dispersion = dispersion_measure_from_function(
    lambda k: compose([S_axis(k, a, False) for a in range(3)], 8)
)
bare_protocol_passes = bare_defect < TOL and bare_vector == (1, 1, 1) and bare_dispersion > 1.0e-7
check("L5 bare cycle passes the protocol-level filters while bare factors commute and decorated factors anticommute", bare_protocol_passes and bare_commuting and decorated_anticommuting)

corrupted = {name: dict(prop) for name, prop in properties.items()}
corrupted["P_SYM"] = dict(properties["P_MIX4"])
corrupt_G1, corrupt_G2, corrupt_G3 = run_gates(corrupted)
check(
    "L6 replacing P_SYM by P_MIX4 changes the G1-G3 survivor stack",
    (corrupt_G1, corrupt_G2, corrupt_G3) != (G1, G2, G3),
    f"honest G3={sorted(G3)}; corrupted G3={sorted(corrupt_G3)}",
)


print("\n" + "=" * 96)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
