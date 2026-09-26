#!/usr/bin/env python3
"""Post-seal source authentication and selective independent exact controls.

Imports only the earlier independently written finite generator, never an
author function. Author outputs are read for comparison, not used to build it.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as s
from sympy.polys.domains import QQ_I
from check import one_color_operators, extract

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def authenticate():
    pre = HERE / 'PRE_COMPARISON_SEAL.json'
    assert digest(pre) == 'f18244dc934652e8e6570923d5582476e605c10fb99615c6c7218037b05f5f09'
    own = json.loads(pre.read_text())
    for row in own['artifacts']:
        p = Path(row['path'])
        assert p.stat().st_size == row['bytes'] and digest(p) == row['sha256']
    author_seal = AUTHOR / 'BIRTH_BACKACTION_AUTHOR_PRECOMPARISON_SEAL.json'
    assert digest(author_seal) == '437ce4aa2f75bcde51eab5e7e31a27d4387d58d19dde0e54b4d155227dec859b'
    authors = json.loads(author_seal.read_text())
    for row in authors['artifacts']:
        p = Path(row['path'])
        assert p.stat().st_size == row['bytes'] and digest(p) == row['sha256']
    for stem, script in [('QUANTUM_BIRTH_BACKACTION', 'quantum_birth_backaction_check.py'),
                         ('PAIR_BIRTH_DEPHASING', 'pair_birth_dephasing_check.py')]:
        result = AUTHOR / (stem + '_RESULTS.json')
        assert result.read_bytes() == (AUTHOR / (stem + '_RUN.log')).read_bytes()
        assert (AUTHOR / (stem + '_RUN.stderr')).read_bytes() == b''
        receipt = json.loads((AUTHOR / (stem + '_RUN_RECEIPT.json')).read_text())
        assert receipt['returncode'] == 0
        assert receipt['script_sha256'] == digest(AUTHOR / script)
        assert json.loads(result.read_text())['script_sha256'] == digest(AUTHOR / script)
    return {'own_pre_seal_artifacts_unchanged': len(own['artifacts']),
            'author_seal_artifacts_authenticated': len(authors['artifacts']),
            'both_stdout_files_equal_results': True,
            'both_stderr_files_empty': True,
            'both_success_receipts_match_script_identities': True}


def one_hole_controls():
    # Derive ranks from exact Krylov subspaces, with independently chosen
    # vertex order. A projector makes the localized overlap explicit.
    square = s.Matrix(4, 4, lambda a, b: int((a-b) % 4 in (1, 3)))
    e0 = s.eye(4)[:, 0]
    krylov = s.Matrix.hstack(*(square**j * e0 for j in range(4)))
    dark = krylov.T.nullspace()
    assert len(dark) == 1
    v = dark[0]
    P = v * v.T / (v.T * v)[0]
    assert P[1, 1] == s.Rational(1, 2)
    vertices = list(product((-1, 1), repeat=3))
    H = s.Matrix(8, 8, lambda a, b: int(sum(x != y for x, y in zip(vertices[a], vertices[b])) == 1))
    source = s.eye(8)[:, 0]
    K = s.Matrix.hstack(*(H**j * source for j in range(8)))
    assert K.rank() == 4
    return {'square_observable_rank': krylov.rank(),
            'square_localized_dark_overlap': str(P[1, 1]),
            'cube_observable_rank': K.rank(),
            'cube_uniform_eventual_completion': '1/2'}


def exact_stationarity_and_detuning():
    edges = [(0, 1), (1, 2), (2, 3), (0, 3)]
    even = [mask for mask in range(16) if mask.bit_count() % 2 == 0]
    cases = [('all_birth_with_monitoring', 1, 1, edges),
             ('all_birth_without_monitoring', 1, 0, edges),
             ('one_birth_source_with_monitoring', 1, 1, edges[:1]),
             ('no_birth', 1, 1, []), ('no_hopping', 0, 1, edges)]
    rows = []
    for name, k, d, births in cases:
        _, full = one_color_operators(4, edges, births, k, 1, d)
        L = extract(full, 16, even)
        nullity = L.rows - L.to_DM().convert_to(QQ_I).rank()
        rows.append({'case': name, 'stationary_operator_nullity': nullity})
    reported = json.loads((AUTHOR / 'PAIR_BIRTH_DEPHASING_RESULTS.json').read_text())
    assert [x['stationary_operator_nullity'] for x in rows] == [x['exact_stationary_operator_nullity'] for x in reported['stationarity']]
    # Admissible H0 which changes the square mean, while preserving even cycle
    # symmetry: one energy unit on both opposite-hole states, zero elsewhere.
    H0 = s.zeros(16)
    H0[5, 5] = H0[10, 10] = 1
    for x in range(4):
        nx = s.diag(*[1 - ((z >> x) & 1) for z in range(16)])
        assert H0 * nx == nx * H0
    _, full = one_color_operators(4, edges, edges, 1, 1, 1)
    full -= s.I * (s.kronecker_product(s.eye(16), H0) - s.kronecker_product(H0.T, s.eye(16)))
    h2 = [z for z in range(16) if z.bit_count() == 2]
    K = extract(full, 16, h2)
    vecT = -K.inv(method='DM').conjugate().T * s.eye(6).vec()
    T = s.Matrix(6, 6, lambda r, c: vecT[r + 6*c]).applyfunc(s.expand)
    assert (T - T.conjugate().T).applyfunc(s.expand) == s.zeros(6)
    # Simplify the exact residual: unlike the zero-detuning controls, the
    # expanded complex products are not structurally canonical in SymPy.
    assert (K.conjugate().T * T.vec() + s.eye(6).vec()).applyfunc(s.expand) == s.zeros(36, 1)
    minors = [s.factor(T[:j, :j].det(method='domain-ge')) for j in range(1, 7)]
    assert all(x > 0 for x in minors)
    cert = {'leading_principal_minors': list(map(str, minors)),
            'adjoint_mean_equation_residual': '0'}
    v = s.zeros(6, 1)
    v[h2.index(5)], v[h2.index(10)] = 1, -1
    rho = v * v.T / 2
    mean = s.factor((T * rho).trace())
    assert mean != s.Rational(161, 48)
    return {'nullity_comparison': rows,
            'H0_countercontrol': {'H0': '|holes02><holes02|+|holes13><holes13|',
                                 'commutes_with_every_nx': True,
                                 'rates': 'kappa=beta=d=1',
                                 'exact_mean': str(mean),
                                 'H0_zero_mean': '161/48',
                                 'difference': str(mean - s.Rational(161, 48)),
                                 'positive_mean_operator': cert}}


def author_matching_and_clock():
    author = json.loads((AUTHOR / 'QUANTUM_BIRTH_BACKACTION_RESULTS.json').read_text())
    xyz = list(product(range(4), repeat=3))
    edges = author['paired_vacancy']['matching']
    flat = [v for edge in edges for v in edge]
    assert len(edges) == 31 and len(set(flat)) == 62
    holes = set(range(64)) - set(flat)
    assert {xyz[i] for i in holes} == {(0, 0, 0), (1, 1, 1)}
    for i, j in edges:
        delta = [(a-b) % 4 for a, b in zip(xyz[i], xyz[j])]
        assert sum(v != 0 for v in delta) == 1 and all(v in (0, 1, 3) for v in delta)
    # A closed-form critical-damping point checks an author numerical value
    # without replaying the same matrix-exponential implementation.
    row = next(x for x in author['two_block']['diagnostics'] if x['beta'] == '4' and x['t'] == 1.0)
    exact = 1 - 5 * s.exp(-2)
    error = abs(float(exact) - row['full_Lindblad_birth_probability'])
    assert error < 1e-14
    k, b = s.symbols('k b', positive=True)
    mean = 2/b + b/(4*k*k)
    assert s.simplify(mean.subs(b, 2*s.sqrt(2)*k) - s.sqrt(2)/k) == 0
    # Symbolic independent source and author waiting expressions coincide.
    own = json.loads((HERE / 'RESULTS.json').read_text())
    theirs = json.loads((AUTHOR / 'PAIR_BIRTH_DEPHASING_RESULTS.json').read_text())
    env = {'k': k, 'kappa': k, 'beta': b, 'd': s.Symbol('d', positive=True)}
    assert s.factor(s.sympify(own['square_symbolic']['mean_compact'], locals=env) - s.sympify(theirs['symbolic_waiting']['mean_from_dark_state'], locals=env)) == 0
    return {'author_31_edge_matching_checked_independently': True,
            'critical_damping_birth_probability_beta4_t1': str(exact),
            'reported_numerical_error': error,
            'clock_optimum_exact': True,
            'independent_author_square_mean_difference': '0'}


if __name__ == '__main__':
    result = {'boundary': 'Post-seal comparison; earlier independent artifacts remain unchanged.',
              'authentication': authenticate(),
              'one_hole': one_hole_controls(),
              'full_finite_comparison': exact_stationarity_and_detuning(),
              'matching_and_clock': author_matching_and_clock()}
    (HERE / 'COMPARISON_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
