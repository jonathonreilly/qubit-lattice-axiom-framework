"""Independent narrow controls for preparation-uniform actual cube births.

Primitive physical (charge, electric-field) words; no campaign builder imported.
The mixed-state experiment is explicitly a leading two-cluster model, not the
full microscopic cube. The written proof supplies its application to that cube.
"""
from collections import defaultdict
from pathlib import Path
import hashlib
import json
import math

import numpy as np

A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
EDGES = tuple((a, b) for a in A for b in B if (a ^ b).bit_count() == 1)
INDEX = {edge: i for i, edge in enumerate(EDGES)}
Q0 = tuple(int(v in A) for v in range(8))


def gauss(key):
    q, E = key
    divergence = [0] * 8
    for value, (a, b) in zip(E, EDGES):
        divergence[a] += value
        divergence[b] -= value
    assert divergence == [q[v] - int(v in A) for v in range(8)]


def shift_weight(field, change, spin):
    if spin is None:
        return 1.
    if abs(field + change) > spin:
        return 0.
    square = 1 - field * (field + change) / (spin * (spin + 1))
    assert square >= -1e-15
    return math.sqrt(max(0., square))


def hop(state, spin, center=None):
    out = defaultdict(complex)
    for (q, E), amplitude in state.items():
        for edge, (a, b) in enumerate(EDGES):
            if center is not None and a != center:
                continue
            if not q[a] or q[b]:
                continue
            weight = shift_weight(E[edge], -q[a], spin)
            if not weight:
                continue
            nq, ne = list(q), list(E)
            nq[a], nq[b] = 0, q[a]
            ne[edge] -= q[a]
            key = tuple(nq), tuple(ne)
            gauss(key)
            out[key] += amplitude * weight
    return dict(out)


def birth(state, signs, spin):
    out = defaultdict(complex)
    edge = INDEX[(0, 1)]
    for (q, E), amplitude in state.items():
        if q[0] or q[1]:
            continue
        for sign in signs:
            weight = shift_weight(E[edge], sign, spin)
            if not weight:
                continue
            nq, ne = list(q), list(E)
            nq[0], nq[1] = sign, -sign
            ne[edge] += sign
            key = tuple(nq), tuple(ne)
            gauss(key)
            out[key] += amplitude * weight
    return dict(out)


def linear_combination(*terms):
    result = defaultdict(complex)
    for coefficient, state in terms:
        for word, amplitude in state.items():
            result[word] += coefficient * amplitude
    return {key: value for key, value in result.items() if abs(value) > 1e-14}


def inner(left, right):
    return sum(np.conj(value) * right.get(key, 0) for key, value in left.items())


def gram(columns):
    return np.array([[inner(x, y) for y in columns] for x in columns])


def circulation(vertices, strength):
    E = [0] * 12
    for a, b, sign in vertices:
        E[INDEX[(a, b)]] = sign * strength
    key = Q0, tuple(E)
    gauss(key)
    return key


inputs = [(Q0, (0,) * 12)]
for square in [((0, 1, 1), (3, 1, -1), (3, 2, 1), (0, 2, -1)),
               ((0, 1, 1), (5, 1, -1), (5, 4, 1), (0, 4, -1))]:
    for strength in (-1, 1):
        inputs.append(circulation(square, strength))
assert len(set(inputs)) == 5


def diagonal_predictions(word, spin, label):
    E = word[1]
    fields = [E[INDEX[(0, leaf)]] for leaf in (1, 2, 4)]
    if spin is None:
        down = up = [1.] * 3
    else:
        C = spin * (spin + 1)
        down = [1 - e * (e - 1) / C for e in fields]
        up = [1 - e * (e + 1) / C for e in fields]
    bp = up[0] * (down[1] + down[2])
    bm = down[0] * (down[1] + down[2])
    rp = 4 * up[0] * down[1] * down[2]
    rm = down[0] * (down[1] * up[2] + up[1] * down[2])
    return {'plus': (bp, rp), 'minus': (bm, rm), 'coherent': (bp + bm, rp + rm)}[label]


word_rows = []
rotor_columns = {}
for spin in (None, 2, 3, 7, 19):
    for label, signs in [('plus', (1,)), ('minus', (-1,)), ('coherent', (1, -1))]:
        low, high = [], []
        cancellation_residuals, wrong_denominator_residuals = [], []
        for key in inputs:
            initial = {key: 1.}
            F = hop(initial, spin)
            FF = hop(F, spin)
            Bj = birth(F, signs, spin)
            direct = linear_combination((.5, birth(FF, signs, spin)), (-1, hop(Bj, spin)))
            local = linear_combination((-1, hop(Bj, spin, center=0)))
            difference = linear_combination((1, direct), (-1, local))
            cancellation_residuals.append(math.sqrt(abs(inner(difference, difference))))
            wrong = linear_combination((1, birth(FF, signs, spin)), (-1, hop(Bj, spin)), (-1, local))
            wrong_denominator_residuals.append(math.sqrt(abs(inner(wrong, wrong))))
            assert all(sum(1 for a in A if q[a] == 0) == 0 for q, E in Bj)
            assert all(q[0] == q[7] == 0 and sum(x == 0 for x in q) == 2 for q, E in local)
            low.append(Bj)
            high.append(local)
        expected_b, expected_r = zip(*(diagonal_predictions(word, spin, label) for word in inputs))
        b_error = float(np.linalg.norm(gram(low) - np.diag(expected_b)))
        r_error = float(np.linalg.norm(gram(high) - np.diag(expected_r)))
        assert max(b_error, r_error, *cancellation_residuals) < 2e-12
        assert min(wrong_denominator_residuals) > .1
        word_rows.append({'spin': 'rotor' if spin is None else spin, 'mark': label,
                          'input_count': len(inputs), 'B_Gram_error': b_error,
                          'R_Gram_error': r_error,
                          'full_second_order_minus_local_residual': max(cancellation_residuals),
                          'wrong_missing_half_minimum_residual': min(wrong_denominator_residuals),
                          'B_diagonal': list(expected_b), 'R_diagonal': list(expected_r)})
        if spin is None:
            rotor_columns[label] = low, high

# A spin-boundary example is outside the fixed-span limit and can block a mark.
boundary = circulation(((0, 1, 1), (3, 1, -1), (3, 2, 1), (0, 2, -1)), 3)
blocked = birth(hop({boundary: 1.}, 3), (1,), 3)
assert abs(inner(blocked, blocked)) == 0


def trace_norm(matrix):
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def fisher_subnormalized(state, H):
    values, vectors = np.linalg.eigh((state + state.conj().T) / 2)
    assert values.min() > -1e-12
    values = np.maximum(values, 0)
    matrix = vectors.conj().T @ H @ vectors
    numerator = (values[:, None] - values[None, :])**2
    denominator = values[:, None] + values[None, :]
    quotient = np.divide(numerator, denominator, out=np.zeros_like(numerator), where=denominator > 1e-14)
    return float(2 * np.sum(quotient * abs(matrix)**2))


latent_dimension = len(inputs)
rng = np.random.default_rng(2026092417)
raw = rng.normal(size=(latent_dimension, latent_dimension)) + 1j * rng.normal(size=(latent_dimension, latent_dimension))
unitary = np.linalg.qr(raw)[0]
rho_cases = {
    'maximally_mixed': np.eye(latent_dimension) / latent_dimension,
    'full_rank_coherent_mixture': unitary @ np.diag([.4, .25, .2, .1, .05]) @ unitary.conj().T,
    'rank_two_mixture': unitary @ np.diag([.7, .3, 0, 0, 0]) @ unitary.conj().T,
    'orthogonal_to_first_word': np.diag([0., 1., 0, 0, 0]),
}
mixed_rows = []
alpha, delta = .1, 1.3
for label, (low, high) in rotor_columns.items():
    words = sorted(set().union(*(set(column) for column in low + high)))
    Bmat = np.array([[column.get(word, 0) for column in low] for word in words])
    Rmat = np.array([[column.get(word, 0) for column in high] for word in words])
    b, r = {'plus': (2, 4), 'minus': (2, 2), 'coherent': (4, 6)}[label]
    L, U = Bmat / math.sqrt(b), Rmat / math.sqrt(r)
    assert np.linalg.norm(L.conj().T @ U) == 0
    P0, P1 = L @ L.conj().T, U @ U.conj().T
    phase = 1j * (U @ L.conj().T - L @ U.conj().T)
    frequency_test = U @ L.conj().T + L @ U.conj().T
    assert np.linalg.norm(phase @ phase - P0 - P1) < 1e-14
    for epsilon in (.12, .06, .03):
        # Exactly degenerate blocks isolate the mixed-state issue; these are
        # not the finite-spin microscopic matrices or their canonical rotation.
        H = delta * epsilon**-4 * P1
        k = epsilon * Bmat + epsilon**2 * Rmat
        for state_name, rho in rho_cases.items():
            omega = alpha**2 * k @ rho @ k.conj().T
            p = float(np.trace(omega).real)
            derivative = 1j * (H @ phase - phase @ H)
            d = abs(np.trace(omega @ derivative))
            v = float(np.trace(omega @ phase @ phase).real)
            witness = float(d*d / v)
            fisher = fisher_subnormalized(omega, H)
            cross = P1 @ omega @ P0
            expected_cross = alpha**2 * epsilon**3 * math.sqrt(b*r)
            assert abs(trace_norm(cross) / expected_cross - 1) < 1e-11
            assert abs(float(np.trace(omega @ frequency_test).real) / (2*expected_cross) - 1) < 1e-11
            assert abs(fisher / witness - 1) < 2e-10
            target = 4 * alpha**2 * delta**2 * r
            exact_scaled = target * b / (b + epsilon**2 * r)
            assert abs(epsilon**4*fisher / exact_scaled - 1) < 2e-10

            pinched = P0 @ omega @ P0 + P1 @ omega @ P1
            pinched_fisher = fisher_subnormalized(pinched, H)
            mean = float(np.trace(omega @ H).real) / p
            variance = float(np.trace(omega @ H @ H).real) / p - mean**2
            pinched_variance = float(np.trace(pinched @ H @ H).real) / p - mean**2
            assert abs(variance-pinched_variance) <= 1e-10 * variance
            assert pinched_fisher < 1e-10 * fisher

            stationary_noise = p * P0 / latent_dimension
            sigma = (1-epsilon**2)*omega + epsilon**2*stationary_noise
            eta = trace_norm(sigma-omega)
            hnorm = np.linalg.norm(H, 2)
            robust = max(0., d - 2*hnorm*eta)**2 / (v+eta)
            noisy_fisher = fisher_subnormalized(sigma, H)
            assert noisy_fisher + 1e-8 >= robust
            bad_phase = 1j * (np.outer(U[:,0],L[:,0].conj())-np.outer(L[:,0],U[:,0].conj()))
            bad_d = abs(np.trace(omega @ (1j*(H@bad_phase-bad_phase@H))))
            if state_name == 'orthogonal_to_first_word':
                assert bad_d < 1e-10 and d > 0
            mixed_rows.append({'mark':label,'epsilon':epsilon,'density':state_name,
                               'scaled_selected_Fisher':epsilon**4*fisher,'limiting_coefficient':target,
                               'witness_over_Fisher':witness/fisher,'low_high_trace_norm':trace_norm(cross),
                               'pinched_Fisher_over_target_Fisher':pinched_fisher/fisher,
                               'pinched_variance_over_target_variance':pinched_variance/variance,
                               'noise_trace_error':eta,'scaled_robust_lower_bound':epsilon**4*robust,
                               'scaled_noisy_Fisher':epsilon**4*noisy_fisher,
                               'old_single_word_derivative':float(bad_d)})

report = {'primitive_operator_checks':word_rows,'spin_boundary_plus_mark_blocked':True,
          'mixed_state_checks':mixed_rows,
          'scope':'Five fixed physical low electric words; original primitive finite-spin/rotor hops and marks. Mixed-state controls use their leading two-cluster maps only, not a full microscopic cube or apparatus simulation.',
          'independence':'No author code or campaign builder imported; original source premises and old pure-input coefficients were known.',
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('FINITE_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
