"""Bounded released-source POST checks. Never imports or executes author code.

The root's results are inspected as author evidence. A separate two-state
dark/bright balance is checked in exact rational arithmetic. Neither is a
large-spin cube computation or a retained/audit verdict.
"""
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path
import cmath
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'POST_sources'
PRE_SEAL_SHA = 'ab052a8061d0103417c6ce431d132530951df70eea588e709c31f0f4bbc7995d'
ROOT_SCRIPT_SHA = '7354476b7b253e966f66bfe0b3d6cca32f3949b18c4208470de27951e33ad7c7'
HELPER = HERE.parent / 'preparation-uniform-personal/mixed_preparation_controls.py'
HELPER_SHA = '8f4320e1cb333098bb3a609b0a95366380ffc7f1c693cffb8342d757fbc7a09a'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def matrix_add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def matrix_scale(a, x):
    return [[x*v for v in row] for row in a]


def matrix_mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def frobenius(a):
    return math.sqrt(sum(abs(x)**2 for row in a for x in row))


def ldl_positive_pivots(a):
    """Floating diagnostics only, not interval positivity certification."""
    n = len(a)
    lower = [[0j]*n for _ in range(n)]
    pivots = []
    for i in range(n):
        lower[i][i] = 1.
        p = a[i][i]-sum(abs(lower[i][k])**2*pivots[k] for k in range(i))
        assert abs(p.imag) < 1e-12
        assert p.real > 0
        pivots.append(p.real)
        for j in range(i+1, n):
            lower[j][i] = (a[j][i]-sum(lower[j][k]*pivots[k]*lower[i][k].conjugate()
                                     for k in range(i)))/p.real
    return pivots


def source_checks():
    assert sha(HERE/'PRE_SEAL.json') == PRE_SEAL_SHA
    pre = load(HERE/'PRE_SEAL.json')
    for member in pre['members']:
        path = HERE/member['path']
        assert sha(path) == member['sha256']
        assert path.stat().st_size == member['bytes']
    freeze = load(HERE/'POST_SOURCE_FREEZE.json')
    released = []
    for row in freeze['released_sources']:
        copy = HERE/row['snapshot']
        source = Path(row['source'])
        assert sha(copy) == row['sha256'] == sha(source)
        assert copy.stat().st_size == row['bytes'] == source.stat().st_size
        released.append({'snapshot': row['snapshot'], 'sha256': row['sha256'],
                         'bytes': row['bytes'], 'live_source_matches': True})
    for row in freeze['procedural_sources']:
        copy = HERE/row['snapshot']
        assert sha(copy) == row['sha256'] and copy.stat().st_size == row['bytes']
    sealed_counts = {}
    for filename in ('AUTHOR_SEAL.json', 'CONTROL_SEAL.json'):
        seal = load(SNAP/filename)
        for name, expected in seal['files_sha256'].items():
            assert sha(SNAP/name) == expected
        sealed_counts[filename] = len(seal['files_sha256'])
    result = SNAP/'FULL_ENSEMBLE_CONTROL_RESULTS.json'
    assert (SNAP/'CONTROL.stdout.txt').read_bytes() == result.read_bytes()
    assert (SNAP/'CONTROL.stderr.txt').read_bytes() == b''
    execution = load(SNAP/'CONTROL_EXECUTION.json')
    assert execution['exit_code'] == 0
    assert execution['script_sha256'] == ROOT_SCRIPT_SHA == sha(SNAP/'full_ensemble_energy_controls.py')
    author_pins = load(SNAP/'SOURCE_PINS.json')
    own_source_hashes = {m['sha256'] for m in pre['members'] if m['path'].startswith('sources/')}
    overlap = [p for p in author_pins['sources'] if p['sha256'] in own_source_hashes]
    declared_only = [p for p in author_pins['sources'] if p['sha256'] not in own_source_hashes]
    assert len(overlap) == 9
    assert len(declared_only) == 3
    # Byte identity only: the external helper body is not imported or re-reviewed.
    assert sha(HELPER) == HELPER_SHA
    return {
        'PRE_seal_sha256': PRE_SEAL_SHA,
        'PRE_unchanged_member_count': len(pre['members']),
        'released_snapshots': released,
        'author_sealed_member_counts': sealed_counts,
        'procedural_snapshot_count': len(freeze['procedural_sources']),
        'stdout_identical_to_complete_result': True,
        'stderr_empty': True,
        'author_execution': execution,
        'shared_scientific_source_pin_count': len(overlap),
        'root_only_declared_sources_not_imported': declared_only,
        'reused_helper': {'path': str(HELPER), 'sha256': HELPER_SHA,
                          'current_bytes_match': True,
                          'scope': 'Byte pin only; body not re-reviewed or executed. The root word controls remain author evidence.'},
    }


def root_result_checks():
    result = load(SNAP/'FULL_ENSEMBLE_CONTROL_RESULTS.json')
    assert result['source_sha256'] == ROOT_SCRIPT_SHA
    algebra = result['source_algebra']
    assert algebra['reused_helper_sha256'] == HELPER_SHA
    assert [r['S'] for r in algebra['rows']] == [None, 2, 3, 7, 21, 100]
    assert sum(r['edge_mark_checks'] for r in algebra['rows']) == 1260
    assert algebra['mutant_nonzero_cases'] == 1239
    for r in algebra['rows']:
        assert r['edge_mark_checks'] == r['input_count']*12*3
        assert r['moving_boundary_word_included'] == (r['S'] is not None)
        assert r['max_twice_first_high_identity_residual_squared'] < 1e-24
        assert r['max_six_times_second_high_coefficient_residual_squared'] < 1e-23
        assert r['missing_middle_factor_mutant_max_norm_squared'] > 0
    assert algebra['rows'][0]['max_twice_first_high_identity_residual_squared'] == 0
    assert algebra['rows'][0]['max_six_times_second_high_coefficient_residual_squared'] == 0

    toy = result['evolving_input_cascade']
    delta, kappa, birth, strength = 1.1, .17, 2., 4.
    assert toy['parameters'] == {'delta': delta, 'kappa': kappa, 'b': birth,
                                  'r': strength, 'age_cap': 2.6}
    # Independently transcribed literal matrices, no import of the author builder.
    q = [[1.+0j, .2j], [-.3+0j, .65+0j]]
    small_b = [[.2+0j, .1+0j], [.1+0j, -.4+0j]]
    qstar = dagger(q)
    g = [[0j]*4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            g[i][j+2] = qstar[i][j]
            g[i+2][j] = q[i][j]
            g[i+2][j+2] = small_b[i][j]
    z = matrix_scale(g, -1j*delta)
    for i in (2, 3):
        z[i][i] -= kappa
    psi = [1/math.sqrt(2), 1j/math.sqrt(2)]
    rho_initial = [[x*y.conjugate() for y in psi] for x in psi]
    target_checks = []
    assert [row['t'] for row in toy['targets']] == [.4, 1.1, 2.3]
    assert len(toy['rows']) == 15
    for target in toy['targets']:
        t = target['t']
        sigma = [[complex(re, im) for re, im in zip(rr, ii)]
                 for rr, ii in zip(target['Sigma_real'], target['Sigma_imag'])]
        assert len(sigma) == 4 and all(len(row) == 4 for row in sigma)
        # Closed two-state exponential: hI=.05 I + [[.25,.7],[.7,-.25]].
        frequency = math.sqrt(.25**2+.7**2)
        a = [[.25, .7], [.7, -.25]]
        u = [[cmath.exp(-.05j*t)*((math.cos(frequency*t) if i == j else 0)
                                  -1j*math.sin(frequency*t)*a[i][j]/frequency)
              for j in range(2)] for i in range(2)]
        rhoi = matrix_scale(matrix_mul(matrix_mul(u, rho_initial), dagger(u)),
                            math.exp(-kappa*birth*t))
        source = [[0j]*4 for _ in range(4)]
        for i in range(2):
            for j in range(2):
                source[i][j] = strength*rhoi[i][j]
        residual = matrix_add(matrix_add(matrix_mul(z, sigma), matrix_mul(sigma, dagger(z))),
                              matrix_scale(source, kappa))
        residual_frobenius = frobenius(residual)
        hermitian_error = frobenius(matrix_add(sigma, matrix_scale(dagger(sigma), -1)))
        high_trace = trace(sigma).real
        bright_trace = sigma[2][2].real+sigma[3][3].real
        bright_target = strength*math.exp(-kappa*birth*t)/2
        assert residual_frobenius < 6e-15
        assert hermitian_error < 2e-14
        assert abs(high_trace-target['Sigma_trace']) < 1e-14
        assert abs(bright_trace-bright_target) < 4e-15
        assert abs(bright_target-target['bright_trace_target']) < 1e-14
        assert abs(target['mean_target']-(target['common_low_mean']+delta*high_trace)) < 2e-14
        assert abs(target['scaled_variance_target']-delta**2*high_trace) < 2e-14
        rows = [r for r in toy['rows'] if r['t'] == t]
        assert [r['epsilon'] for r in rows] == [.16, .08, .04, .02, .01]
        for row in rows:
            assert row['mean_target'] == target['mean_target']
            assert row['scaled_variance_target'] == target['scaled_variance_target']
            assert abs(row['target_high_trace']-high_trace) < 1e-14
            assert row['terminal_probability'] >= -1e-12
            assert row['minimum_diagonal_block_eigenvalue'] > -1e-11
            assert row['scaled_high_density_trace_distance']+1e-12 >= abs(row['scaled_high_trace']-high_trace)
            assert row['scaled_recent_density_trace_distance'] >= 0
            assert row['scaled_older_than_epsilon_high_trace'] >= 0
        fine = rows[-1]
        target_checks.append({
            't': t,
            'literal_array_Lyapunov_residual_frobenius': residual_frobenius,
            'Hermitian_residual_frobenius': hermitian_error,
            'floating_LDL_pivots': ldl_positive_pivots(sigma),
            'Sigma_trace': high_trace,
            'bright_trace': bright_trace,
            'bright_trace_target': bright_target,
            'finest_epsilon': fine['epsilon'],
            'finest_mean_absolute_error': abs(fine['full_mean']-target['mean_target']),
            'finest_scaled_variance_absolute_error': abs(fine['scaled_full_variance']-target['scaled_variance_target']),
            'finest_scaled_high_density_trace_distance': fine['scaled_high_density_trace_distance'],
            'author_wrong_unevolved_source_trace_distance': target['incorrect_zero_field_source_trace_distance'],
        })
    r11 = next(r for r in toy['rows'] if r['t'] == 1.1 and r['epsilon'] == .01)
    assert round(r11['full_mean'], 6) == 2.877541
    assert round(r11['mean_target'], 6) == 2.876752
    assert round(r11['scaled_full_variance'], 6) == 3.265279
    assert round(r11['scaled_variance_target'], 6) == 3.264409
    assert abs(r11['scaled_high_density_trace_distance']-.000937434) < 5e-10
    return {
        'source_algebra_case_count': 1260,
        'source_algebra_mutant_nonzero_count': 1239,
        'max_author_source_identity_residual_squared': max(
            max(r['max_twice_first_high_identity_residual_squared'],
                r['max_six_times_second_high_coefficient_residual_squared']) for r in algebra['rows']),
        'author_toy_row_count': 15,
        'toy_scope': toy['scope'],
        'toy_maximum_real_fast_eigenvalue_reported_not_recomputed': toy['maximum_real_fast_eigenvalue'],
        'target_checks': target_checks,
        'minimum_reported_diagonal_block_eigenvalue': min(r['minimum_diagonal_block_eigenvalue'] for r in toy['rows']),
        'scope_prose_rounding_checked': True,
        'scope': 'Complete reported result and source correspondence. Literal-array matrix residuals recomputed; author cascade propagations and imported word helper not executed. No independent cube numerical claim.'
    }


# Gaussian-rational scalar algebra, deliberately separate from author code.
def qc(a=0, b=0): return (F(a), F(b))
def qa(a, b): return (a[0]+b[0], a[1]+b[1])
def qn(a): return (-a[0], -a[1])
def qm(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def qconj(a): return (a[0], -a[1])
def qsum(xs):
    ans = qc()
    for x in xs: ans = qa(ans, x)
    return ans
def qmm(a, b):
    return [[qsum(qm(a[i][k], b[k][j]) for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def qdag(a): return [[qconj(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]
def qma(a, b): return [[qa(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]
def qnorm2(a): return sum(x*x+y*y for row in a for x, y in row)
def qstrings(a): return [[[str(x), str(y)] for x, y in row] for row in a]


def exact_dark_bright_checks():
    rows = []
    for g, k, a in ((F(2, 3), F(1, 5), F(7, 4)),
                    (F(3, 2), F(4, 7), F(5, 9)),
                    (F(1, 10), F(3, 5), F(2))):
        # L=[0,-ig;-ig,-k], Sigma00=a/2+k²a/(2g²), Sigma11=a/2,
        # Sigma01=i k a/(2g). Source is k*a*|dark><dark|.
        loss = [[qc(), qc(0, -g)], [qc(0, -g), qc(-k)]]
        x, y, v = a/2+k*k*a/(2*g*g), a/2, k*a/(2*g)
        sigma = [[qc(x), qc(0, v)], [qc(0, -v), qc(y)]]
        balance = qma(qmm(loss, sigma), qmm(sigma, qdag(loss)))
        source = [[qc(k*a), qc()], [qc(), qc()]]
        residual = qma(balance, source)
        assert qnorm2(residual) == 0
        determinant = x*y-v*v
        assert determinant == a*a/4 and determinant > 0 and x > 0 and y > 0
        assert 2*y == a
        mutant = qma(balance, [[qc(a), qc()], [qc(), qc()]])
        assert qnorm2(mutant) == a*a*(1-k)**2 > 0
        # Hermitian transpose is not a sign mutant; explicitly reverse the current.
        reversed_current = [[qc(x), qc(0, -v)], [qc(0, v), qc(y)]]
        reversed_residual = qma(qma(qmm(loss, reversed_current), qmm(reversed_current, qdag(loss))), source)
        assert qnorm2(reversed_residual) > 0
        rows.append({'g': str(g), 'kappa': str(k), 'source_squared_norm': str(a),
                     'Sigma_Gaussian_rational_entries': qstrings(sigma),
                     'Lyapunov_residual_squared': str(qnorm2(residual)),
                     'determinant': str(determinant), 'trace': str(x+y),
                     'Gamma_trace': str(2*y), 'bright_trace': str(y),
                     'missing_kappa_mutant_residual_squared': str(qnorm2(mutant)),
                     'reversed_current_mutant_residual_squared': str(qnorm2(reversed_residual))})
    return {
        'model': 'Independent two-state supplied dark/bright generator L=[[0,-ig],[-ig,-kappa]], Gamma=2|bright><bright|; source kappa*a|dark><dark|.',
        'rows': rows,
        'integrability_hypothesis_control': {
            'g_zero': 'L leaves the dark source unchanged; its integrated density has trace kappa*a*age and diverges.',
            'Lyapunov_obstruction': 'For g=0 every matrix has (L Sigma+Sigma L*)_00=0; the required right side is -kappa*a != 0.',
            'scope': 'Shows bounded dissipativity alone cannot replace the cube decay/tightness premise. It is not a counterexample under that premise.'},
        'scope': 'Exact rational signs, source factor, bright trace and positivity in a separate stable two-state mechanism. No cube tail, finite-spin limit or apparatus claim.'
    }


def main():
    result = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': sha(Path(__file__)),
        'source_and_seal_checks': source_checks(),
        'released_author_result_checks': root_result_checks(),
        'independent_exact_balance_check': exact_dark_bright_checks(),
        'author_code_imported_or_executed': False,
        'expensive_primary_or_parent_run_repeated': False,
        'audit_verdict_applied': False,
    }
    data = json.dumps(result, indent=2)+'\n'
    (HERE/'POST_EVIDENCE_CHECK.json').write_text(data)
    print(data, end='')


if __name__ == '__main__':
    main()
