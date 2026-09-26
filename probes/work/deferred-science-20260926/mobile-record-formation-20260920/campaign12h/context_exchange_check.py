#!/usr/bin/env python3
"""Exact controls for the supplied context-dependent exchange construction.

Finite controls supplement the displayed stationarity proof; the script does
not prove a hydrodynamic limit or replace an independent derivation.
"""
from pathlib import Path
from itertools import product, permutations
from fractions import Fraction as F
import hashlib
import json
import math
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
V = np.array([[0, 0, 0], [1, 0, 0], [-1, 0, 0],
              [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], dtype=int)
OCC = np.array([0, 1, 1, 1, 1, 1, 1], dtype=int)
ALPHABET = range(7)
STRINGS = np.array(list(product(ALPHABET, repeat=4)), dtype=int)


def h_batch(strings, axis, u, coupling):
    l, a, b, r = strings.T
    f = V[:, axis]
    return (u * (f[a] - f[b]) + coupling * (
        (f[a] - f[b]) * (OCC[l] + OCC[r])
        + (OCC[a] - OCC[b]) * (f[l] + f[r])))


def rotations():
    result = []
    lookup = {tuple(v): i for i, v in enumerate(V)}
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for i in range(3):
                matrix[perm[i], i] = signs[i]
            if round(np.linalg.det(matrix)) == 1:
                mapping = np.array([lookup[tuple(matrix @ v)] for v in V])
                result.append((matrix, mapping))
    assert len(result) == 24
    return result


def main():
    output = {'status': 'primary_finite_and_symbolic_controls',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    menus = [(-1, 1), (2, 0), (1, -2), (0, 1)]
    rate_checks = 0
    rotation_checks = 0
    for u, coupling in menus:
        bound = 2 * abs(u) + 4 * abs(coupling)
        for i in range(3):
            h = h_batch(STRINGS, i, u, coupling)
            assert int(np.abs(h).max()) <= bound
            swapped = STRINGS[:, [0, 2, 1, 3]]
            assert np.array_equal(h, -h_batch(swapped, i, u, coupling))
            k = abs(u) + 2 * abs(coupling) + 1
            assert np.all(2 * k + h > 0)
            assert np.array_equal(np.maximum(h, 0) - np.maximum(-h, 0), h)
            rate_checks += len(STRINGS)
            for matrix, mapping in rotations():
                direction = matrix[:, i]
                j = int(np.flatnonzero(direction)[0])
                transformed = mapping[STRINGS]
                if direction[j] < 0:
                    transformed = transformed[:, ::-1]
                assert np.array_equal(h, h_batch(transformed, j, u, coupling))
                rotation_checks += len(STRINGS)
    output['local_rate_cases'] = rate_checks
    output['rotation_cases'] = rotation_checks

    stationarity = []
    for length in [4, 5, 6]:
        strings = np.array(list(product(ALPHABET, repeat=length)), dtype=np.int8)
        for u, coupling in menus:
            total = np.zeros(len(strings), dtype=np.int32)
            for x in range(length):
                block = strings[:, [(x - 1) % length, x, (x + 1) % length,
                                    (x + 2) % length]]
                total += h_batch(block, 0, u, coupling)
            assert not total.any()
            stationarity.append({'length': length, 'states': len(strings),
                                 'u': u, 'E': coupling, 'max_residual': int(abs(total).max())})
    output['pointwise_periodic_stationarity'] = stationarity

    currents = []
    for weights in [[5, 1, 2, 3, 4, 5, 6], [6, 1, 1, 1, 1, 1, 1],
                    [1, 3, 3, 2, 2, 4, 4]]:
        weights = np.array(weights, dtype=np.int64)
        denominator = int(weights.sum())
        masses = np.prod(weights[STRINGS], axis=1)
        p = [F(int(w), denominator) for w in weights]
        rho = sum(p[1:])
        g = [sum(p[a] * int(V[a, i]) for a in ALPHABET) for i in range(3)]
        for u, coupling in menus:
            flow = u + 2 * coupling * rho
            other = -u + 2 * coupling * (1 - 2 * rho)
            k = abs(u) + 2 * abs(coupling) + 1
            for i in range(3):
                hs = h_batch(STRINGS, i, u, coupling)
                for a in range(1, 7):
                    indicator = ((STRINGS[:, 1] == a).astype(int)
                                 - (STRINGS[:, 2] == a).astype(int))
                    observed = F(int(np.dot(masses * (2 * k + hs), indicator)),
                                 2 * denominator ** 4)
                    minimal = F(int(np.dot(masses * (1 + 20 * np.maximum(hs, 0)), indicator)),
                                20 * denominator ** 4)
                    expected = p[a] * (flow * int(V[a, i]) + other * g[i])
                    assert observed == expected == minimal
                    currents.append(str(observed))
    output['exact_product_current_entries'] = len(currents)

    rho, u, coupling = sp.symbols('rho u E', real=True)
    kx, ky, kz, omega = sp.symbols('kx ky kz omega', real=True)
    p = sp.ones(6, 1) * rho / 6
    one = sp.ones(6, 1)
    q = sp.Matrix([kx, -kx, ky, -ky, kz, -kz])
    flow = u + 2 * coupling * rho
    other = -u + 2 * coupling * (1 - 2 * rho)
    A = (flow * sp.diag(*q) + 2 * coupling * rho / 6 * q * one.T
         + other * p * q.T)
    C = sp.diag(*p) - p * p.T
    assert all(sp.expand(x) == 0 for x in A * C - C * A.T)
    tuned = sp.simplify(A.subs(u, -2 * coupling * rho))
    speed2k2 = 4 * coupling**2 * rho**2 * (1 - rho) * (kx*kx + ky*ky + kz*kz)/3
    assert all(sp.expand(x) == 0 for x in tuned**3 - speed2k2 * tuned)
    assert sp.simplify(sp.trace(tuned**2) - 2 * speed2k2) == 0
    # Rank <=2 follows independently from the displayed sum of two outer products.
    expected = omega**4 * (omega**2 - speed2k2)
    characteristic = tuned.charpoly(omega)
    # SymPy strips assumptions from its polynomial generator. Compare using
    # one actual symbol, rather than two identically printed symbols.
    actual = characteristic.as_expr().subs(characteristic.gen, omega)
    assert sp.expand(actual - expected) == 0
    output['generic_symbolic_checks'] = ['A C symmetric', 'A^3=c^2|k|^2 A',
                                        'trace A^2=2c^2|k|^2', 'six by six characteristic polynomial']

    # An exact full four-site forward equation includes insertion, independent
    # of the pointwise outgoing/incoming cancellation checked above.
    weights = np.array([5, 1, 2, 3, 4, 5, 6], dtype=np.int64)
    masses = np.prod(weights[STRINGS], axis=1)
    lookup = {tuple(s): i for i, s in enumerate(STRINGS)}
    got = np.zeros(len(STRINGS), dtype=np.int64)
    predicted = np.zeros(len(STRINGS), dtype=np.int64)
    for idx, state in enumerate(STRINGS):
        for x in range(4):
            block = state[[(x-1)%4,x,(x+1)%4,(x+2)%4]][None,:]
            rate2 = 8 + int(h_batch(block, 0, -1, 1)[0])
            target = state.copy()
            target[x], target[(x+1)%4] = state[(x+1)%4], state[x]
            got[lookup[tuple(target)]] += masses[idx] * rate2
            got[idx] -= masses[idx] * rate2
            if state[x] == 0:
                for a in range(1,7):
                    target=state.copy(); target[x]=a
                    got[lookup[tuple(target)]] += 2 * masses[idx]
                    got[idx] -= 2 * masses[idx]
            dp = -6 * weights[0] if state[x] == 0 else weights[0]
            predicted[idx] += 2 * dp * int(np.prod(weights[np.delete(state, x)]))
    assert np.array_equal(got, predicted)
    output['full_generator_insertion_identity_states'] = len(STRINGS)
    output['example'] = {'rho_star': 0.5, 'u': -1, 'E': 1,
                         'sound_speed_squared': str(F(1, 6)),
                         'minimal_rate_floor': '1/20',
                         'interpretation': 'exact current eigenvalues; microscopic waves not established'}
    text = json.dumps(output, indent=2) + '\n'
    (HERE/'CONTEXT_EXCHANGE_RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
