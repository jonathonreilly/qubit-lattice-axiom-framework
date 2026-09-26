#!/usr/bin/env python3
"""Bounded post-seal checks; no author implementation is imported or executed."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations
from math import comb
import hashlib
import json
import time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent
AUTHOR_SEAL = 'QUANTUM_CLOCK_AND_COHERENT_COMPLETION_AUTHOR_SEAL.json'
AUTHOR_HASH = '7231481bd65aec211905948c3f30c0e55d4923ccf89bd281ef40c758d26d1195'
PRE_HASH = '5e850f785c0f41eb34d75a30f84f86830963763b57cac1b6f6bcaa7466531395'


def identity(path):
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def authenticate():
    assert identity(AUTHOR / AUTHOR_SEAL)['sha256'] == AUTHOR_HASH
    assert identity(HERE / 'PRE_COMPARISON_SEAL.json')['sha256'] == PRE_HASH
    pre = json.loads((HERE / 'PRE_COMPARISON_SEAL.json').read_text())
    author = json.loads((AUTHOR / AUTHOR_SEAL).read_text())
    for row in pre['sources'] + pre['artifacts'] + author['artifacts']:
        got = identity(Path(row['path']))
        assert got['bytes'] == row['bytes'] and got['sha256'] == row['sha256'], row
    return {'original_independent_bindings': len(pre['sources']) + len(pre['artifacts']),
            'author_bindings': len(author['artifacts']),
            'author_seal': identity(AUTHOR / AUTHOR_SEAL),
            'precomparison_seal': identity(HERE / 'PRE_COMPARISON_SEAL.json')}


def evidence_consistency():
    clock = json.loads((AUTHOR / 'QUANTUM_LAST_PAIR_CLOCK_SCREEN_RESULTS.json').read_text())
    obs = json.loads((AUTHOR / 'COHERENT_RING_CONTACT_OBSERVABILITY_RESULTS.json').read_text())
    assert clock['script_sha256'] == identity(AUTHOR / 'quantum_last_pair_clock_screen.py')['sha256']
    assert obs['script_sha256'] == identity(AUTHOR / 'coherent_ring_contact_observability_check.py')['sha256']
    cl = [json.loads(x) for x in (AUTHOR / 'QUANTUM_LAST_PAIR_CLOCK_SCREEN_RUN.log').read_text().splitlines()]
    assert cl[:-1] == clock['screen'] and cl[-1] == {
        'finished': True, 'exact_C4': clock['exact_C4'], 'runtime_seconds': clock['runtime_seconds']}
    assert [(x['K'], x['d']) for x in clock['screen']] == [
        (K, d) for K in (4, 6, 8, 12, 16, 24) for d in (.001, .01, .1, .3, 1., 3., 10., 100.)]
    assert all(x['beta'] == x['kappa'] == 1 for x in clock['screen'])
    assert max(x['linear_residual_inf'] for x in clock['screen']) < 1e-12
    assert all(('direct_full_Poisson_residual_inf' in x) == (x['K'] <= 8) for x in clock['screen'])
    assert all(abs(x['adjacent_localized_mean'] - (x['K']-1)/2) < 1e-10 for x in clock['screen'])
    for row in clock['dark_projection_controls']:
        K = row['K']; r = K//2-2+int(K % 4 == 0)
        assert row['dark_dimension'] == r
        assert s.sympify(row['predicted_fixed_K_weak_d_mean_coefficient_for_uniform_input']) == s.Rational(r, (K-1)*(K-2))
        assert s.sympify(row['predicted_fixed_K_strong_d_mean_coefficient_for_uniform_input']) == s.Rational((K-2)*(K-3), 48)
    counts = []; previous = 0
    for K in (4, 6, 8, 10, 12, 14):
        group = [r for r in obs['cases'] if r['K'] == K]
        assert len(group) == 3*K//2+5
        previous += len(group); counts.append({'K': K, 'completed_cases': previous})
        for row in group:
            h = row['holes']; D = comb(K, h)
            if row['open_chain']:
                free = comb(K-h+1, h) if K-h+1 >= h else 0
            else:
                free = K*comb(K-h, h)//(K-h) if 0 < h <= K//2 else 0
            assert (row['dimension'], row['noncontact_dimension'], row['contact_dimension']) == (D, free, D-free)
            deficit = K//2-2+int(K % 4 == 0) if h == 2 and row['phase'] == 'real' and not any(
                row[k] for k in ('open_chain', 'inhomogeneous_hopping', 'diagonal_potential', 'one_occupation_monitor')) else 0
            assert row['unobserved_dimension_mod_prime'] == deficit
            assert row['observable_rank_mod_prime'] == D-deficit
            assert row['full_rank_certifies_characteristic_zero_observability'] == (deficit == 0)
    ol = [json.loads(x) for x in (AUTHOR / 'COHERENT_RING_CONTACT_OBSERVABILITY_RUN.log').read_text().splitlines()]
    assert ol == counts + [{'finished': True, 'cases': 111, 'runtime_seconds': obs['runtime_seconds']}]
    cr = json.loads((AUTHOR / 'QUANTUM_LAST_PAIR_CLOCK_SCREEN_RUN_RECEIPT.json').read_text())
    assert cr['exit_code'] == 0 and cr['script_sha256'] == clock['script_sha256']
    for key, value in cr.items():
        if key.endswith(('.log', '.stderr', 'RESULTS.json')):
            assert identity(AUTHOR / key)['sha256'] == value
    ore = json.loads((AUTHOR / 'COHERENT_RING_CONTACT_OBSERVABILITY_RUN_RECEIPT.json').read_text())
    assert ore['returncode'] == 0 and ore['script_sha256'] == obs['script_sha256']
    assert (AUTHOR / 'QUANTUM_LAST_PAIR_CLOCK_SCREEN_RUN.stderr').read_bytes() == b''
    assert (AUTHOR / 'COHERENT_RING_CONTACT_OBSERVABILITY_RUN.stderr').read_bytes() == b''
    return {'clock_rows_read_and_authenticated': len(clock['screen']),
            'observable_rows_read_and_metadata_checked': len(obs['cases']),
            'clock_max_recorded_reduced_residual': max(r['linear_residual_inf'] for r in clock['screen']),
            'clock_full_matrix_checks_recorded': sum('direct_full_Poisson_residual_inf' in x for x in clock['screen']),
            'gauge_sector_rows': len(obs['gauge_sector_controls']), 'exact_dark_rows': len(obs['exact_dark_controls']),
            'both_stdout_streams_match_result_fields': True, 'both_stderr_empty': True,
            'note': 'Authentication and algebraic metadata checks do not replay all author calculations.'}


def symbolic_clock_match():
    data = json.loads((AUTHOR / 'QUANTUM_LAST_PAIR_CLOCK_SCREEN_RESULTS.json').read_text())['exact_C4']
    beta, d, kappa = s.symbols('beta d kappa', positive=True)
    a = 3/(2*beta)
    b = a+1/(beta+d)+1/(2*(beta+2*d))+1/(2*d)+(d+beta/2)/(8*kappa**2)
    expected = {'uniform_incoherent_mean': (2*a+b)/3,
                'opposite_localized_mean': b, 'adjacent_localized_mean': a,
                'dark_initial_mean': b+1/(2*d), 'weak_dephasing_uniform_coefficient': s.Rational(1, 6),
                'strong_dephasing_uniform_coefficient': 1/(24*kappa**2)}
    residuals = {}
    for name, value in expected.items():
        residual = s.cancel(s.sympify(data[name], locals={'beta': beta, 'd': d, 'kappa': kappa})-value)
        assert residual == 0
        residuals[name] = str(residual)
    return {'method': 'Compare author expressions with independently sealed closed formulas, exactly over rational functions.',
            'residuals': residuals}


def unreduced_poisson_check():
    K, d = 12, .3
    states = list(reversed(list(combinations(range(K), 2))))
    ix = {a: j for j, a in enumerate(states)}; D = len(states)
    H = np.zeros((D, D)); loss = np.zeros(D); holes = np.zeros((D, K))
    for col, a in enumerate(states):
        holes[col, list(a)] = 1
        loss[col] = int(any((x+1) % K in a for x in a))
        for x in a:
            for step in (-1, 1):
                y = (x+step) % K
                if y not in a:
                    b = tuple(sorted((set(a)-{x}) | {y}))
                    H[ix[b], col] += 1
    dephase = .5*((holes[:, None, :]-holes[None, :, :])**2).sum(axis=2)
    damping = d*dephase + (loss[:, None]+loss[None, :])/2
    hs = sp.csc_matrix(H); eye = sp.eye(D, format='csc')
    A = -1j*(sp.kron(eye, hs)-sp.kron(hs.T, eye))+sp.diags(damping.reshape(-1, order='F'))
    F = sla.spsolve(A.tocsc(), np.eye(D).reshape(-1, order='F')).reshape((D, D), order='F')
    residual = -1j*(H@F-F@H)+damping*F-np.eye(D)
    target = next(r for r in json.loads((AUTHOR/'QUANTUM_LAST_PAIR_CLOCK_SCREEN_RESULTS.json').read_text())['screen'] if r['K'] == K and r['d'] == d)
    got = {'uniform_incoherent_mean': float(np.trace(F).real/D),
           'adjacent_localized_mean': float(F[ix[(0, 1)], ix[(0, 1)]].real),
           'opposite_localized_mean': float(F[ix[(0, K//2)], ix[(0, K//2)]].real)}
    delta = {k: abs(v-target[k]) for k, v in got.items()}
    assert max(delta.values()) < 1e-10
    assert abs(F-F.conj().T).max() < 1e-10 and abs(residual).max() < 1e-10
    assert np.linalg.eigvalsh(F).min() > 0
    return {'K': K, 'd': d, 'beta': 1, 'kappa': 1, 'unknowns': D*D,
            'method': 'Full matrix-unit sparse Poisson solve; no translation or reflection reduction and no author import.',
            'means': got, 'absolute_differences_from_author': delta,
            'full_entry_residual': float(abs(residual).max()), 'Hermiticity_residual': float(abs(F-F.conj().T).max()),
            'minimum_eigenvalue': float(np.linalg.eigvalsh(F).min())}


def exact_path_control():
    K = 7; states = list(combinations(range(K), 2)); ix = {a: i for i, a in enumerate(states)}
    weights = [1+s.I, 2-s.I, 3*s.I, 4, 1-2*s.I, 2+3*s.I]
    H = s.zeros(len(states))
    for j, a in enumerate(states):
        H[j, j] = sum(2**x for x in a)+3*(a[0]+1)*(a[1]+1)
        for x, t in enumerate(weights):
            y = x+1
            if (x in a) != (y in a):
                b = tuple(sorted((set(a)-{x, y}) | ({y} if x in a else {x})))
                H[ix[b], j] = t if x in a else s.conjugate(t)
    assert H == H.H
    contacts = [i for i, a in enumerate(states) if a[1]-a[0] == 1]
    free = [i for i in range(len(states)) if i not in contacts]
    A, C = H.extract(free, free), H.extract(contacts, free)
    O = C; word = C; ranks = []
    for depth in range(len(free)):
        rank = DomainMatrix.from_Matrix(O).convert_to(s.QQ_I).rank()
        ranks.append({'maximum_power': depth, 'rank': rank})
        if rank == len(free):
            break
        word = word*A; O = O.col_join(word)
    assert ranks[-1]['rank'] == len(free)
    return {'path_vertices': K, 'holes': 2, 'dimension': len(states), 'contact_dimension': len(contacts),
            'noncontact_dimension': len(free), 'weights': [str(x) for x in weights],
            'potential': 'sum(2**x for holes x)+3*(x_first+1)*(x_second+1)',
            'exact_Qi_observability_ranks': ranks, 'dark_dimension': 0,
            'scope': 'Finite control of the open-path step, not the all-size proof.'}


def exact_physical_sector_control():
    K, h = 6, 2; mask = 2**K-1
    bit = lambda b, i: (b >> (i % K)) & 1
    holes = lambda b: tuple(i for i in range(K) if bit(b, i) == bit(b, i-1))
    bits = [b for b in range(2**K) if len(holes(b)) == h]; bix = {b: i for i, b in enumerate(bits)}
    states = list(combinations(range(K), h)); ix = {a: i for i, a in enumerate(states)}
    reps = {holes(b): b for b in bits if bit(b, 0) == 0}
    t = [1+s.I, 2, 3, 4, 5, 6]
    H = s.zeros(len(bits)); T = s.zeros(len(bits)); G = s.zeros(len(bits))
    for col, b in enumerate(bits):
        a = holes(b)
        f = sum((x+1)**2 for x in a); g = s.Rational(1+sum(a), 7)
        H[col, col] += f; H[bix[b ^ mask], col] += g
        T[bix[b ^ mask], col] = 1
        G[col, col] = sum(i+1 for i in range(K) if i in a and (i+1) % K in a)
        for edge in range(K):
            target = b ^ (1 << edge)
            if target in bix:
                assert len(set(a)-set(holes(target))) == 1
                H[bix[target], col] += t[edge] if edge in a else s.conjugate(t[edge])
    assert H == H.H and H*T == T*H and G*T == T*G
    out = []
    for tau in (1, -1):
        B = s.zeros(len(bits), len(states))
        expected = s.zeros(len(states)); expectedG = s.zeros(len(states))
        for a, col in ix.items():
            b = reps[a]; B[bix[b], col] = 1; B[bix[b ^ mask], col] = tau
            expected[col, col] = sum((x+1)**2 for x in a)+tau*s.Rational(1+sum(a), 7)
            expectedG[col, col] = sum(i+1 for i in range(K) if i in a and (i+1) % K in a)
            for edge in range(K):
                y = (edge+1) % K
                if (edge in a) != (y in a):
                    target = tuple(sorted((set(a)-{edge, y}) | ({y} if edge in a else {edge})))
                    amp = t[edge] if edge in a else s.conjugate(t[edge])
                    expected[ix[target], col] += (tau if edge == 0 else 1)*amp
        assert B.T*B == 2*s.eye(len(states)) and T*B == tau*B
        assert B.T*H*B/2 == expected and B.T*G*B/2 == expectedG
        flux_product = tau*s.prod(t)
        assert s.simplify((flux_product/s.conjugate(flux_product))**1) == s.I
        out.append({'T_sector': tau, 'dimension': len(states), 'hopping_product': str(flux_product),
                    'exp_2iPhi': 'I', 'full_H_and_loss_compression_exact': True})
    return {'K': K, 'holes': h, 'physical_dimension': len(bits), 'weights': [str(x) for x in t],
            'H0': 'f(holes) I + g(holes) T with f=sum(x+1)^2, g=(1+sum holes)/7',
            'loss': 'sum(edge+1) over adjacent-hole edges', 'sectors': out,
            'scope': 'Exact characteristic-zero check of complex phases and nontrivial T-dependent H0.'}


if __name__ == '__main__':
    started = time.monotonic()
    result = {'created_utc': datetime.now(timezone.utc).isoformat(),
              'script': identity(Path(__file__)), 'authentication': authenticate(),
              'author_evidence_consistency': evidence_consistency(),
              'symbolic_clock_comparison': symbolic_clock_match(),
              'unreduced_clock_comparison': unreduced_poisson_check(),
              'open_path_control': exact_path_control(),
              'physical_sector_control': exact_physical_sector_control(),
              'author_scripts_executed': False, 'runtime_seconds': time.monotonic()-started}
    text = json.dumps(result, indent=2)+'\n'
    (HERE/'COMPARISON_RESULTS.json').write_text(text)
    print(text, end='')
