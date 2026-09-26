#!/usr/bin/env python3
"""Independent finite orthogonal-lift and literal-product controls.
Does not access author checker, results, logs or contextual papers.
"""
from pathlib import Path
from collections import Counter
import datetime, hashlib, itertools, json, math
import numpy as np
import sympy as sp
HERE = Path(__file__).resolve().parent
RAW = HERE.parent

def edge(a, b):
    return tuple(sorted((a, b)))

def matchings(vertices, edges):
    if not vertices:
        return [()]
    a = min(vertices)
    out = []
    for b in sorted(vertices - {a}):
        if edge(a, b) in edges:
            out += [tuple(sorted((edge(a, b), *tail)))
                    for tail in matchings(vertices - {a, b}, edges)]
    return out

def marked_states(n, edges):
    geometries = sorted(matchings(set(range(n)), edges))
    fibers = {}
    K = n // 2
    for M in geometries:
        states = []
        for keys in itertools.permutations(range(K)):
            for orientations in itertools.product(range(2), repeat=K):
                eta = [-1] * n
                for (x, y), k, orient in zip(M, keys, orientations):
                    eta[x] = 2 * k + orient
                    eta[y] = 2 * k + 1 - orient
                states.append(tuple(eta))
        fibers[M] = sorted(states)
    all_states = sorted(eta for states in fibers.values() for eta in states)
    assert len(all_states) == len(set(all_states))
    return geometries, fibers, all_states

def geometry(eta):
    pos = {label: x for x, label in enumerate(eta)}
    return tuple(sorted(edge(pos[2 * k], pos[2 * k + 1]) for k in range(len(eta) // 2)))

def flippable(M, p):
    q = [edge(p[i], p[(i + 1) % 4]) for i in range(4)]
    return ({q[0], q[2]} <= set(M)) or ({q[1], q[3]} <= set(M))

def rotate(eta, p, sign=1):
    result = list(eta)
    for i in range(4):
        result[p[(i + sign) % 4]] = eta[p[i]]
    return tuple(result)

def orthogonal_lift(n, edges, squares, matrices=False):
    geometries, fibers, states = marked_states(n, edges)
    where = {eta: i for i, eta in enumerate(states)}
    F = 2 ** (n // 2) * math.factorial(n // 2)
    channels = 0
    kinetic = np.zeros((len(states), len(states)), dtype=np.int64) if matrices else None
    count = np.zeros(len(states), dtype=np.int64)
    for M in geometries:
        assert len(fibers[M]) == F
        destinations = Counter()
        predicted = Counter()
        for p in squares:
            if flippable(M, p):
                flip = geometry(rotate(fibers[M][0], p))
                predicted[flip] += 2
        for eta in fibers[M]:
            i = where[eta]
            for p in squares:
                enabled = flippable(M, p)
                rotated = rotate(eta, p) if enabled else eta
                if enabled:
                    x = eta
                    for _ in range(4):
                        x = rotate(x, p)
                        assert flippable(geometry(x), p) and x in where
                    assert x == eta
                    assert rotate(rotated, p, -1) == eta
                    for label in eta:
                        x, y = eta.index(label), rotated.index(label)
                        assert x == y or edge(x, y) in edges
                    count[i] += 1
                    for sign in [-1, 1]:
                        target = rotate(eta, p, sign)
                        destinations[target] += 1
                        channels += 1
                        if matrices:
                            kinetic[where[target], i] += 1
                else:
                    assert rotated == eta
        # Raw fiber sum: kinetic marked map equals twice the geometric-flip map.
        for eta in states:
            assert destinations[eta] == predicted[geometry(eta)]
        assert len({int(count[where[eta]]) for eta in fibers[M]}) == 1
    if matrices:
        assert np.array_equal(kinetic, kinetic.T)
    return ({'vertices': n, 'perfect_matchings': len(geometries), 'fiber_size': F,
             'marked_states': len(states), 'two_sense_local_channels': channels,
             'orthogonal_intertwiner_exact': True, 'flippability_and_R4_exact': True},
            geometries, fibers, states, kinetic, count)

def tensor_column(eta, spinors):
    return sp.Matrix([sp.prod(spinors[label][bit] for label, bit in zip(eta, bits))
                      for bits in itertools.product(range(2), repeat=len(eta))])

def square_product_controls(geometries, fibers, states):
    p, q = sp.symbols('p q', real=True)
    spinors = [sp.Matrix([1, 0]), sp.Matrix([0, 1]), sp.Matrix([p, q]), sp.Matrix([-q, p])]
    V = sp.Matrix.hstack(*(tensor_column(eta, spinors) for eta in states))
    S = sp.Matrix([[int(eta in fibers[M]) for M in geometries] for eta in states])
    fiber = sp.simplify(S.T * V.T * V * S / 8)
    expected = sp.Matrix([[2 * (p ** 4 + q ** 4), (p * p + q * q) ** 2],
                          [(p * p + q * q) ** 2, 2 * (p ** 4 + q ** 4)]])
    assert sp.simplify(fiber - expected) == sp.zeros(2)
    vx = V.subs({p: 1 / sp.sqrt(2), q: 1 / sp.sqrt(2)})
    gramx = vx.T * vx
    assert gramx.rank() == 11 and fiber.subs({p: 1 / sp.sqrt(2), q: 1 / sp.sqrt(2)}) == sp.ones(2)
    pair = [(0, 1, 2, 3), (2, 1, 0, 3)]
    assert all(eta in states for eta in pair) and geometry(pair[0]) != geometry(pair[1])
    assert gramx[states.index(pair[0]), states.index(pair[1])] == sp.Rational(1, 2)
    tilted = fiber.subs({p: sp.Rational(3, 5), q: sp.Rational(4, 5)})
    assert tilted == sp.Matrix([[sp.Rational(674, 625), 1], [1, sp.Rational(674, 625)]])
    assert tilted.det() == sp.Rational(63651, 390625) and tilted.rank() == 2
    # Exact nontrivial record-phase changes; all columns get one common phase.
    phases = [sp.I, (3 + 4 * sp.I) / 5, -1, (5 - 12 * sp.I) / 13]
    phased = [phase * psi for phase, psi in zip(phases, [x.subs({p: sp.Rational(3, 5), q: sp.Rational(4, 5)}) for x in spinors])]
    vp = sp.Matrix.hstack(*(tensor_column(eta, phased) for eta in states))
    vt = V.subs({p: sp.Rational(3, 5), q: sp.Rational(4, 5)})
    assert sp.simplify(vp - sp.prod(phases) * vt) == sp.zeros(*vt.shape)
    assert sp.simplify(vp.conjugate().T * vp - vt.T * vt) == sp.zeros(len(states))
    return {'enumeration': [list(x) for x in states], 'generic_fiber_gram_unnormalized_pq': str(fiber),
            'normalized_generic_diagonal': '1+(p^2-q^2)^2', 'normalized_generic_offdiagonal': '1',
            'z_x_gram_rank': 11, 'z_x_fiber_gram': [[1, 1], [1, 1]],
            'overlap_witness_configurations': pair, 'overlap': '1/2',
            'tilted_fiber_gram': [[str(x) for x in tilted.row(i)] for i in range(2)],
            'tilted_determinant': str(tilted.det()), 'record_phase_change_is_global_exactly': True}

def orbit_probability_control():
    tau = sp.symbols('tau', real=True)
    R = sp.zeros(4)
    for i in range(4):
        R[(i + 1) % 4, i] = 1
    H = -(R + R.T) / 2
    Pplus = (sp.eye(4) + R + R ** 2 + R ** 3) / 4
    Pminus = (sp.eye(4) - R + R ** 2 - R ** 3) / 4
    Pzero = sp.eye(4) - Pplus - Pminus
    W = sp.exp(sp.I * tau) * Pplus + sp.exp(-sp.I * tau) * Pminus + Pzero
    assert H * Pplus == -Pplus and H * Pminus == Pminus and H * Pzero == sp.zeros(4)
    assert sp.simplify(W.conjugate().T * W) == sp.eye(4)
    odd = sp.diag(0, 1, 0, 1)
    definite = sp.eye(4)[:, 0]
    coherent = (sp.eye(4)[:, 0] + sp.eye(4)[:, 2]) / sp.sqrt(2)
    mixed = sp.diag(sp.Rational(1, 2), 0, sp.Rational(1, 2), 0)
    pdef = sp.simplify(sp.expand_complex((definite.T * W.conjugate().T * odd * W * definite)[0]))
    pcoh = sp.simplify(sp.expand_complex((coherent.T * W.conjugate().T * odd * W * coherent)[0]))
    pmix = sp.simplify(sp.expand_complex(sp.trace(odd * W * mixed * W.conjugate().T)))
    assert sp.trigsimp(pdef - sp.sin(tau) ** 2 / 2) == 0
    assert sp.trigsimp(pcoh - sp.sin(tau) ** 2) == 0 and sp.simplify(pmix - pdef) == 0
    return {'definite_probability': str(pdef), 'incoherent_probability': str(pmix),
            'coherent_probability': str(pcoh), 'at_pi_over_two': ['1/2', '1/2', '1']}

def ladder_gram_controls(states, kinetic, count):
    # The four non-z spinors contribute denominator 4 in every product column.
    # Gaussian-integer arithmetic below is exact, with entries bounded far below int64.
    unnormalized = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, 1j), (-1, 1j)]
    columns = np.array([[math.prod(unnormalized[a][b] for a, b in zip(eta, bits))
                         for eta in states]
                        for bits in itertools.product(range(2), repeat=6)], dtype=complex)
    vr, vi = columns.real.astype(np.int64), columns.imag.astype(np.int64)
    assert np.array_equal(columns, vr + 1j * vi)
    gr, gi = vr.T @ vr + vi.T @ vi, vr.T @ vi - vi.T @ vr
    assert np.array_equal(gr, gr.T) and np.array_equal(gi, -gi.T)
    assert np.all(np.diag(gr) == 16) and np.all(np.diag(gi) == 0)
    D = np.diag(count)
    dr, di = gr @ D - D @ gr, gi @ D - D @ gi
    kr, ki = gr @ kinetic - kinetic @ gr, gi @ kinetic - kinetic @ gi
    witnesses = []
    for potential in [sp.Integer(0), sp.Integer(1), sp.Rational(2, 3)]:
        a, b = int(sp.numer(potential)), int(sp.denom(potential))
        cr, ci = 2 * a * dr - b * kr, 2 * a * di - b * ki
        indices = np.argwhere((cr != 0) | (ci != 0))
        assert len(indices) > 0
        i, j = map(int, indices[0])
        value = sp.Rational(int(cr[i, j]), 32 * b) + sp.I * sp.Rational(int(ci[i, j]), 32 * b)
        witnesses.append({'v': str(potential), 'row': i, 'column': j,
                          'bra_configuration': list(states[i]), 'ket_configuration': list(states[j]),
                          'commutator_exact': str(value), 'nonzero_commutator_entries': len(indices)})
    return {'spinors': ['(1,0)', '(0,1)', '(1,1)/sqrt(2)', '(-1,1)/sqrt(2)', '(1,i)/sqrt(2)', '(-1,i)/sqrt(2)'],
            'enumeration': 'Lexicographically sorted site-label tuples; intentionally independent of author enumeration.',
            'product_column_denominator': 4, 'Gram_denominator': 16,
            'witnesses': witnesses}

def run():
    square = orthogonal_lift(4, {edge(i, (i + 1) % 4) for i in range(4)}, [(0, 1, 2, 3)])
    ladder = orthogonal_lift(6, {(0, 1), (1, 2), (3, 4), (4, 5), (0, 3), (1, 4), (2, 5)},
                             [(0, 1, 4, 3), (1, 2, 5, 4)], matrices=True)
    cubesquares = []
    for i, j in itertools.combinations(range(3), 2):
        for base in range(8):
            if not base & ((1 << i) | (1 << j)):
                cubesquares.append((base, base ^ (1 << i), base ^ (1 << i) ^ (1 << j), base ^ (1 << j)))
    cube = orthogonal_lift(8, {edge(x, x ^ (1 << i)) for x in range(8) for i in range(3)}, cubesquares)
    result = {'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'orthogonal_controls': [square[0], ladder[0], cube[0]],
              'single_orbit': orbit_probability_control(),
              'square_literal_map': square_product_controls(*square[1:4]),
              'ladder_literal_map': ladder_gram_controls(ladder[3], ladder[4], ladder[5]),
              'author_boundary': 'Author checker, results and logs remain unopened; no contextual paper used.'}
    for key in ['square', 'ladder', 'cube']:
        print('orthogonal lift', key, flush=True)
    print(json.dumps(result['ladder_literal_map']['witnesses'], indent=2), flush=True)
    return result

if __name__ == '__main__':
    assert not (HERE / 'INDEPENDENT_RESULTS.json').exists()
    data = run()
    data['checker_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE / 'INDEPENDENT_RESULTS.json').write_text(json.dumps(data, indent=2) + '\n')
    print('All independent exact controls passed.')
