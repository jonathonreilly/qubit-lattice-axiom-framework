#!/usr/bin/env python3
"""Pre-author exact local/routing-cycle reconstruction and independent symbols."""
from pathlib import Path
from itertools import product
import json
import numpy as np
import sympy as sp
from scipy.linalg import expm

OUT = Path(__file__).resolve().parent


def cross_matrix(x):
    a, b, c = x
    return np.array([[0, -c, b], [c, 0, -a], [-b, a, 0]])


def moment_matrix(x):
    cx = cross_matrix(x)
    return np.block([[np.zeros((3, 3), dtype=cx.dtype), -cx],
                     [cx, np.zeros((3, 3), dtype=cx.dtype)]])


def gaussian_integer_cov(a, b):
    ar = np.rint(a.real).astype(np.int64); ai = np.rint(a.imag).astype(np.int64)
    br = np.rint(b.real).astype(np.int64); bi = np.rint(b.imag).astype(np.int64)
    assert np.array_equal(a, ar + 1j * ai) and np.array_equal(b, br + 1j * bi)
    real = ar.T @ br + ai.T @ bi
    imag = ai.T @ br - ar.T @ bi
    return sp.Matrix(real.tolist()) + sp.I * sp.Matrix(imag.tolist())


def exact_local_and_cycle():
    e, b = [], []
    for i in range(3):
        for sign in [1, -1]:
            v = [0, 0, 0]; v[i] = sign
            e.append(v); b.append([0, 0, 0])
    for signs in product([-1, 1], repeat=3):
        e.append([0, 0, 0]); b.append(list(signs))
    e, b = np.array(e, dtype=np.int64), np.array(b, dtype=np.int64)
    q = len(e)
    s2 = np.cross(e[:, None, :], b[None, :, :])[:, :, 0]
    s2 += np.cross(e[None, :, :], b[:, None, :])[:, :, 0]
    assert np.array_equal(s2, s2.T) and np.all(s2.sum(axis=0) == 0)
    colors = np.array(list(product(range(q), repeat=4)), dtype=np.int64)
    states = len(colors)
    l, a, bb, r = colors.T
    h2 = s2[l, a] + s2[a, r] - s2[l, bb] - s2[bb, r]
    assert np.max(abs(h2)) == 4
    # Actual rate is k0/2+h/4=(5+h2)/8 for k0=5/4,gamma=1.
    weight = 5 + h2
    conditionals = []
    for position in range(4):
        numerator = np.zeros((q, q), dtype=np.int64)
        np.add.at(numerator, (a, colors[:, position]), weight)
        np.add.at(numerator, (bb, colors[:, position]), -weight)
        conditional = sp.Matrix(numerator.tolist()) / (8 * q ** 3)
        if position in [0, 3]:
            expected = sp.Matrix(s2.tolist()) / 56  # A_delta/4
        else:
            expected = sp.Rational(5 if position == 1 else -5, 8) * (sp.eye(q) - sp.ones(q) / q)
        assert conditional == expected
        conditionals.append({'position': ['l', 'u', 'v', 'r'][position],
                             'exact_matrix_match': True})

    # Six normalized features are sqrt(7)/2 * u(s), u=(2e,b).
    # On four sites F=sqrt(7)/4 * U, U=sum_x(-i)^x u(s_x).
    features = np.hstack([2 * e, b])
    phase = np.array([1, -1j, -1, 1j])
    U = sum(phase[x] * features[colors[:, x]] for x in range(4))
    ident = np.arange(states, dtype=np.int64)
    place = np.array([q ** 3, q ** 2, q, 1], dtype=np.int64)
    swapped, drive = [], []
    for x in range(4):
        y = (x + 1) % 4
        left, right = (x - 1) % 4, (x + 2) % 4
        aa, cc = colors[:, x], colors[:, y]
        swap = ident + (cc - aa) * place[x] + (aa - cc) * place[y]
        hh = s2[colors[:, left], aa] + s2[aa, colors[:, right]] - s2[colors[:, left], cc] - s2[cc, colors[:, right]]
        swapped.append(swap); drive.append(hh)
        assert np.array_equal(swap[swap], ident)
    T = sp.Matrix(moment_matrix([1, 0, 0]).astype(int).tolist())
    covariance = sp.Rational(7, 16 * states) * gaussian_integer_cov(U, U)
    assert covariance == sp.eye(6)
    cycle_rows = []
    for gamma in [0, 1]:
        weights = [5 + gamma * h for h in drive]
        # Eight times the generator acting on U, then 64 times L^2 U.
        LU8 = sum(w[:, None] * (U[swap] - U) for w, swap in zip(weights, swapped))
        L2U64 = sum(w[:, None] * (LU8[swap] - LU8) for w, swap in zip(weights, swapped))
        B = -sp.Rational(5, 4) * sp.eye(6) + sp.I * sp.Rational(gamma, 7) * T
        C1 = sp.Rational(7, 128 * states) * gaussian_integer_cov(LU8, U)
        C2 = sp.Rational(7, 1024 * states) * gaussian_integer_cov(L2U64, U)
        # Row arrays carry component vectors; multiply T on the right transpose.
        Rnum = 7 * LU8 + 70 * U - 8j * gamma * (U @ np.array(T.tolist(), dtype=int).T)
        residual = gaussian_integer_cov(Rnum, Rnum) / (7168 * states)
        assert C1 == B
        assert C2 == B ** 2 - residual
        assert residual == residual.conjugate().T
        assert all(sp.sign(ev) >= 0 for ev in residual.eigenvals())
        if gamma == 0:
            assert residual == sp.zeros(6)
        else:
            assert sp.trace(residual) > 0
        cycle_rows.append({'gamma': gamma, 'k0': '5/4', 'states': states,
                           'phase': 'pi/2', 'C1_equals_projected_B_exactly': True,
                           'C2_equals_B_squared_minus_R_cov_exactly': True,
                           'residual_covariance': [[str(x) for x in row] for row in residual.tolist()],
                           'residual_eigenvalues': {str(k): v for k, v in residual.eigenvals().items()},
                           'trace_residual': str(sp.trace(residual)),
                           'closure_exact': gamma == 0})
    return {'alphabet': 'six A axes and eight B corners', 'all_local_four_label_inputs': states,
            'conditional_projection_coefficients': conditionals, 'auxiliary_cycle': cycle_rows}


def symbol(k, k0, gamma):
    directions = list(np.eye(3)) + list(-np.eye(3))
    # Assemble the four separately reindexed coefficients, before simplifying.
    assembled = np.zeros((6, 6), dtype=complex)
    d, qeff = 0., np.zeros(3)
    for delta in directions:
        z = k @ (delta - np.array([1, 0, 0]))
        adelta = 2 * gamma / 7 * moment_matrix(delta)
        assembled += (np.exp(-1j * z) - 1) * (
            adelta / 4 * (np.exp(-1j * z) + np.exp(2j * z))
            + k0 / 2 * (1 - np.exp(1j * z)) * np.eye(6))
        d += 2 * k0 * np.sin(z / 2) ** 2
        qeff += (np.sin(2 * z) - np.sin(z)) * delta / 2
    expected = -d * np.eye(6) - 2j * gamma / 7 * moment_matrix(qeff)
    assert np.max(abs(assembled - expected)) < 3e-14
    return assembled, d, qeff


def symbols_and_statistics():
    # Oblique wavevectors and both signs of gamma check signs beyond axis data.
    symbol_rows = []
    for k in [np.array([.37, .21, -.19]), np.array([-.31, .29, .11]), np.zeros(3)]:
        for gamma in [-1, 0, 1]:
            _, d, qe = symbol(k, 1.1, gamma)
            symbol_rows.append({'k': k.tolist(), 'gamma': gamma, 'd': d, 'q_eff': qe.tolist()})
    predictions = []
    for N in [16, 32, 64, 128]:
        theta = 2 * np.pi / N
        for axis in range(3):
            n = np.eye(3)[axis]; k = theta * n; Q = 2 * np.pi * n
            B, d, qe = symbol(k, 1.1, 1)
            d_axis = 2 * 1.1 * (np.sin(theta) ** 2 + 4 * np.sin(theta / 2) ** 2) if axis == 0 else 4 * 1.1 * np.sin(theta / 2) ** 2
            q_axis = (np.sin(4 * theta) - np.sin(2 * theta)) / 2 if axis == 0 else np.sin(2 * theta) - np.sin(theta)
            assert abs(d - d_axis) < 3e-15 and np.max(abs(qe - q_axis * n)) < 3e-15
            P3 = np.outer(n, n)
            PL = np.block([[P3, np.zeros((3, 3))], [np.zeros((3, 3)), P3]])
            PT = np.eye(6) - PL
            D = -1j * moment_matrix(n)
            assert np.max(abs(D.conj().T + D)) == 0
            assert np.max(abs(D @ D + PT)) == 0
            for t in [0, .25, .5, .75, 1.]:
                U = expm(-2j / 7 * moment_matrix(Q) * t)
                C = expm(N * t * B)
                values = [2 - np.trace(U.conj().T @ C).real / 3,
                          np.trace(PT @ C).real / 4,
                          np.trace(D.conj().T @ C).real / 4,
                          np.trace(PL @ C).real / 2]
                damp = np.exp(-N * t * d)
                angle = 2 / 7 * N * q_axis * t
                continuum = 2 / 7 * 2 * np.pi * t
                scalar = [2 - damp * (2 + 4 * np.cos(angle - continuum)) / 3,
                          damp * np.cos(angle), damp * np.sin(angle), damp]
                assert np.max(abs(np.array(values) - scalar)) < 2e-14
                predictions.append({'N': N, 'axis': axis, 't': t, 'd': d, 'q_eff_axis': q_axis,
                                    'error': values[0], 'transverse_auto': values[1],
                                    'signed_cross': values[2], 'longitudinal_auto': values[3]})
    # Exact stationary endpoints versus an incorrect deterministic damping path.
    r = sp.Rational(1, 2)
    stationary_error = 2 * (1 - r)
    deterministic_error = (1 - r) ** 2
    assert stationary_error == 1 and deterministic_error == sp.Rational(1, 4)
    return {'oblique_symbol_checks': symbol_rows, 'unfitted_axis_predictions_N_le_128': predictions,
            'stationarity_normalization_countercontrol': {'C': '(1/2) I, U=I',
                'correct_error': str(stationary_error), 'incorrect_deterministic_damping_error': str(deterministic_error)}}


def main():
    exact = exact_local_and_cycle()
    print('exact local projection and full fourteen-label auxiliary cycle complete', flush=True)
    spectral = symbols_and_statistics()
    result = {'read_boundary': 'Before author finite-wavelength checker, results, by-axis comparison or original analyzer access.',
              'exact_controls': exact, 'symbol_and_statistic_controls': spectral,
              'limits': 'Parameter-free projected exponential is a benchmark at gamma!=0. No production values accessed; no N256 observable accessed.'}
    (OUT / 'PRE_COMPARISON_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'pass', 'local_states': 14 ** 4, 'prediction_rows': len(spectral['unfitted_axis_predictions_N_le_128'])}))


if __name__ == '__main__':
    main()
