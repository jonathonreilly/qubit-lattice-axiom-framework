#!/usr/bin/env python3
"""Bounded post-seal comparison and new birth/motion operator controls."""
from pathlib import Path
from itertools import product
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent
EXPECTED = {
    'SIX_QUBIT_COVARIANT_POINTER_DYNAMICS.md': '90b3085b20c6ac999806f296fb2a2c7a0db1860b8bcc808e1002de378021c113',
    'six_qubit_orthogonal_code_check.py': '3222b205b8cb304e529a235db859e5badcda20b2c722711f6610edab93a245a0',
    'DEPOLARIZED_POINTER_RATE_BOUNDARY.md': 'e0e646f4b326939c75a8505c5897eaad5ce6ae4b4bc3c5c567197be376f74d4a',
    'noisy_pointer_generator_check.py': 'efb2595eb63a634a5899e3cb55099fca63ccab3bfcc4c729539ae8392473f238',
    'POINTER_AUTHOR_PRECOMPARISON_SEAL.json': '52b053233a34e2d5034b674576fcde0bfd4fe1a73742c28ac497a0ca87325c45',
}


def row(path):
    data = path.read_bytes()
    return {'path': str(path.resolve()), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def count_and_classical_controls():
    # Two distinguishable occupied pointers and a vacancy suffice to test the
    # new operator formulas without numerically constructing the 64-d code.
    eye = s.eye(3)
    P = [eye[:, a]*eye[:, a].T for a in range(3)]
    n = P[1]+P[2]
    N = s.kronecker_product(n, eye)+s.kronecker_product(eye, n)
    counts = [s.kronecker_product(P[a], eye)+s.kronecker_product(eye, P[a]) for a in (1, 2)]
    beta = [s.Rational(2, 3), s.Rational(5, 7)]
    kappa = [s.Rational(3, 5), s.Rational(7, 11)]
    jumps = []
    def outer(o, i):
        return s.eye(9)[:, o]*s.eye(9)[:, i].T
    H = s.zeros(9)
    for a, rate in zip((1, 2), beta):
        j = eye[:, a]*eye[:, 0].T
        for site in (0, 1):
            J = s.kronecker_product(j, eye) if site == 0 else s.kronecker_product(eye, j)
            assert N*J-J*N == J
            jumps.append((rate, J, 'birth'))
    for a, rate in zip((1, 2), kappa):
        J = outer(a, 3*a)  # |0,a><a,0|.
        H += rate*(J+J.T)
        for C in counts:
            assert C*J-J*C == s.zeros(9)
        jumps.extend([(rate, J, 'hop'), (rate, J.T, 'hop')])
    for C in counts:
        assert H*C-C*H == s.zeros(9)
    adjoint_N = s.zeros(9)
    adjoint_color = [s.zeros(9), s.zeros(9)]
    for rate, J, kind in jumps:
        jj = J.T*J
        adjoint_N += rate*(J.T*N*J-(jj*N+N*jj)/2)
        for index, C in enumerate(counts):
            adjoint_color[index] += rate*(J.T*C*J-(jj*C+C*jj)/2)
    vacant_sum = s.kronecker_product(P[0], eye)+s.kronecker_product(eye, P[0])
    assert adjoint_N == sum(beta)*vacant_sum
    for i in range(2):
        assert adjoint_color[i] == beta[i]*vacant_sum
    # Independent classical transition list, then all nine diagonal basis laws.
    Q = s.zeros(9)
    for a, b in product(range(3), repeat=2):
        original = 3*a+b
        for site, old in enumerate((a, b)):
            if old == 0:
                for new, rate in zip((1, 2), beta):
                    nxt = (new, b) if site == 0 else (a, new)
                    target = 3*nxt[0]+nxt[1]
                    Q[target, original] += rate
                    Q[original, original] -= rate
        if (a == 0) != (b == 0):
            color = a+b
            rate = kappa[color-1]
            target = 3*b+a
            Q[target, original] += rate
            Q[original, original] -= rate
    for original in range(9):
        rho = outer(original, original)
        derived = s.zeros(9)
        for rate, J, kind in jumps:
            jj = J.T*J
            derived += rate*(J*rho*J.T-(jj*rho+rho*jj)/2)
        assert derived == s.diag(*list(Q[:, original]))
    return {'classical_diagonal_basis_laws_checked': 9,
            'birth_rates': list(map(str, beta)), 'hop_coefficients': list(map(str, kappa)),
            'birth_total_number_adjoint_coefficient': str(sum(beta)),
            'birth_each_color_adjoint_coefficients': list(map(str, beta)),
            'birth_raises_number_sector_exactly': True,
            'hops_and_coherent_H_preserve_each_color_number': True,
            'scope': 'Finite orthogonal-pointer operator identities; no claim of a microscopic record-site embedding or trajectory simulation.'}


def main():
    prepath = HERE/'PRE_COMPARISON_SEAL.json'
    assert row(prepath)['sha256'] == '7f07e6c710d75cfeddf8feda172e8eb23d1dc4f30175b53b9172f1a07d48385a'
    pre = json.loads(prepath.read_text())
    for bound in pre['sources']+pre['artifacts']:
        assert row(Path(bound['path'])) == bound
    sources = {r['path']: r for r in pre['sources']}
    for name, digest in EXPECTED.items():
        r = row(AUTHOR/name)
        assert r['sha256'] == digest
        sources[r['path']] = r
    authorseal = json.loads((AUTHOR/'POINTER_AUTHOR_PRECOMPARISON_SEAL.json').read_text())
    for name, digest in authorseal['artifacts_sha256'].items():
        r = row(AUTHOR/name)
        assert r['sha256'] == digest
        sources[r['path']] = r
    code = json.loads((AUTHOR/'SIX_QUBIT_ORTHOGONAL_CODE_RESULTS.json').read_text())
    noise = json.loads((AUTHOR/'NOISY_POINTER_GENERATOR_RESULTS.json').read_text())
    own = json.loads((HERE/'RESULTS.json').read_text())
    assert code['script_sha256'] == EXPECTED['six_qubit_orthogonal_code_check.py']
    assert noise['script_sha256'] == EXPECTED['noisy_pointer_generator_check.py']
    for stem in ('SIX_QUBIT_ORTHOGONAL_CODE', 'NOISY_POINTER_GENERATOR'):
        assert (AUTHOR/(stem+'_RUN.log')).read_bytes() == (AUTHOR/(stem+'_RESULTS.json')).read_bytes()
        assert (AUTHOR/(stem+'_RUN.stderr')).read_bytes() == b''
        receipt = json.loads((AUTHOR/(stem+'_RUN_RECEIPT.json')).read_text())
        assert receipt['returncode'] == 0
        assert receipt['script_sha256'] in EXPECTED.values()
    assert code['F_rank'] == own['pointer_code']['rank'] == 14
    assert code['gram_determinant'] == own['pointer_code']['Gram_determinant']
    roots = {s.sympify(k): v for k, v in code['gram_eigenvalues'].items()}
    independent_roots = {s.sympify(k): v for k, v in own['pointer_code']['Gram_eigenvalues'].items()}
    assert roots == independent_roots
    lam = s.symbols('lam')
    own_poly = s.sympify(own['pointer_code']['Gram_characteristic_polynomial'])
    author_poly = s.sympify(code['characteristic_polynomial']).subs(s.Symbol('t'), lam)
    assert s.expand(own_poly-author_poly) == 0
    labels = [s.Matrix(z) for z in own['noisy_intertwiner']['label_order']]
    seen = set()
    for record in code['group_characters']:
        R = s.Matrix(record['rotation'])
        assert R.T*R == s.eye(3) and R.det() == 1
        seen.add(tuple(R))
        assert record['trace_H'] == (1+s.trace(R))**3
        assert record['trace_code'] == sum(R*z == z for z in labels)
    assert len(seen) == 24
    assert noise['full_generator_offdiagonal_entry'] == own['noisy_intertwiner']['full_generator_entry_at_eta_half']
    eta = s.symbols('eta')
    assert s.factor(s.sympify(noise['all_eta_entry'])-s.sympify(own['noisy_intertwiner']['full_generator_symbolic_entry'])) == 0
    for i, record in enumerate(noise['candidate_stencils']):
        reference = own['support']['contributing_four_context_channels'][i]
        assert record['direction'] == reference['delta'] and record['positions'] == reference['sites']
        assert record['total'] == own['noisy_intertwiner']['two_full_four_context_entries_at_eta_half'][i]
        assert record['bias'] == record['total'] and record['baseline'] == '0'
        assert record['enumerated_stencil_states'] == 14**4
        assert record['minimum_rate'] == '1/20'
    assert len(noise['candidate_stencils']) == 2
    bound = 14**4*27**4*2*15**4*42
    assert noise['int64_sum_absolute_bound'] == bound < 2**63-1
    for key in ('u', 'v', 'cross'):
        a = s.sympify(noise['one_factor_wave_metric'][key].replace('^', '**'))
        b = s.sympify(own['noisy_intertwiner']['local_metric'][key])
        assert s.expand(a-b) == 0
    controls = count_and_classical_controls()
    result = {'all_prior_independent_bindings_unchanged': True,
              'source_rows': sorted(sources.values(), key=lambda r: r['path']),
              'author_seal_rows_authenticated': len(authorseal['artifacts_sha256']),
              'exact_code_and_noise_results_match': True,
              'group_character_records_independently_checked': len(seen),
              'noise_int64_bound': bound, 'noise_int64_limit': 2**63-1,
              'new_operator_controls': controls,
              'author_checkers_reexecuted': False,
              'author_development_archives_inspected': False,
              'findings': []}
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
