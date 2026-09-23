"""Post-PRE source authentication and selective independent band controls.

No author builder is imported or executed.  The physical hopping builder is
the already sealed independent one; the new tests concern the added band/gap
proof and the full lowest eigenspace at exceptional angles.
"""
from pathlib import Path
import ast
import difflib
import hashlib
import itertools
import json
import math

import numpy as np
import sympy as sp
from scipy.linalg import eigh

D = Path(__file__).resolve().parent
A = D.parent / 'post_birth_ring_spectrum_author'
PRE_SHA = 'cffc3495e440045bd73077e8be1a5e231ff39a07e53889a22336c204f60f5c37'
AUTHOR_SHA = 'c2e0e2adcff2dee95c682da2789c19f3113445e7f3e53f20d95936ab25ec07b9'


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def identity(p):
    b = p.read_bytes()
    return {'path': str(p), 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}


assert digest(D / 'PRE_COMPARISON_SEAL.json') == PRE_SHA
assert digest(A / 'AUTHOR_SEAL.json') == AUTHOR_SHA
pre = json.loads((D / 'PRE_COMPARISON_SEAL.json').read_text())
author = json.loads((A / 'AUTHOR_SEAL.json').read_text())
for row in pre['sources'] + pre['artifacts']:
    p = Path(row['path'])
    assert identity(p) == row, p
author_rows = []
for rel, sha in author['files'].items():
    p = A / rel
    assert digest(p) == sha, p
    author_rows.append(identity(p))
for rel, sha in author['parent_source'].items():
    p = D.parent.parent / rel
    assert digest(p) == sha, p
    author_rows.append(identity(p))

# Authenticate the actual author command receipts and complete saved results.
result_rows = []
for sub, result, runner in [
    ('', 'RING_SPECTRUM_RESULTS.json', 'ring_spectrum_check.py'),
    ('initial_probe', 'RING_SPECTRUM_PROBE_RESULTS.json', 'ring_spectrum_probe.py'),
]:
    base = A / sub
    receipt = json.loads((base / 'RUN_RECEIPT.json').read_text())
    data = json.loads((base / result).read_text())
    sha = digest(base / runner)
    assert data['source_sha256'] == receipt['source_sha256'] == sha
    assert receipt['returncode'] == 0 and receipt['command'][-1] == str(base / runner)
    assert (base / 'stderr.log').read_bytes() == b''
    assert (base / 'stdout.log').read_bytes() == (base / result).read_bytes()
    assert [r['L'] for r in data['rows']] == list(range(3, 9))
    for r in data['rows']:
        L = r['L']
        assert r['P_dimension'] == (L + 2) * math.comb(L, 2)
        assert r['sites'] == 2 * L and r['word_and_vacancy_factorization_exact']
        assert len(r['angles']) == 4
        for angle in r['angles']:
            assert angle['max_spectrum_error'] < 2e-12
        for output in r['formation_outputs']:
            assert abs(output['mean_H2'] + 2 * (L - 2)) < 2e-12
            assert abs(output['variance_H2'] - 2) < 2e-12
            assert abs(output['ground_weight_theta_zero'] - output['ground_weight_formula']) < 1e-12
        if not sub:
            assert abs(r['gap_theta_zero'] - r['gap_formula']) < 1e-12
            assert abs(r['crossing_lowest_gap']) < 1e-12
            assert len(r['full_spectral_measures']) == 10
            for m in r['full_spectral_measures']:
                assert len(m['characteristic_function_errors']) == 5
                assert max(m['characteristic_function_errors']) < 2e-12
                assert abs(m['measure_normalization'] - 1) < 2e-14
                assert abs(m['lowest_band_weight'] - m['lowest_band_formula']) < 2e-12
                assert abs(m['mean_H2'] + 2 * (L - 2)) < 2e-12
                assert abs(m['variance_H2'] - 2) < 2e-12
    result_rows.append({'subdirectory': sub, 'source_sha256': sha,
                        'rows_authenticated': len(data['rows']),
                        'author_returncode': receipt['returncode'],
                        'reexecuted': False})
final_data = json.loads((A / 'RING_SPECTRUM_RESULTS.json').read_text())
assert max(a['max_spectrum_error'] for r in final_data['rows'] for a in r['angles']) == author['checks']['max_spectrum_error']
assert max(e for r in final_data['rows'] for a in r['full_spectral_measures'] for e in a['characteristic_function_errors']) == author['checks']['max_measure_characteristic_error']
diff = ''.join(difflib.unified_diff(
    (A / 'initial_probe/ring_spectrum_probe.py').read_text().splitlines(True),
    (A / 'ring_spectrum_check.py').read_text().splitlines(True),
    fromfile='author preserved initial probe', tofile='author final checker'))
diff_path = D / 'AUTHOR_PROBE_TO_FINAL.diff'
assert not diff_path.exists()
diff_path.write_text(diff)

# Reuse ONLY already sealed independent function definitions; executing the
# original top-level script would overwrite its frozen outputs.
own = D / 'ring_control.py'
assert digest(own) == 'b082190bf88df120577cf9337a4edee200e1306a96bcd05d8bcfedd4978e5bf9'
ns = {'np': np, 'sp': sp, 'math': math, 'itertools': itertools}
module = ast.parse(own.read_text())
exec(compile(ast.Module(body=[n for n in module.body if isinstance(n, ast.FunctionDef)],
                        type_ignores=[]), str(own), 'exec'), ns)
fiber, form_q = ns['fiber'], ns['form_q']

band_rows = []
for L in (3, 4, 6, 9):
    M = L + 2
    weight = 4 * math.sin(math.pi / L)**2 / (L * L * M)
    for theta in (-math.pi / L, 0., math.pi / L - .031,
                  math.pi / L, math.pi / L + .031, 3 * math.pi / L, .27):
        ps, H = fiber(L, theta)
        ev, V = eigh(H)
        alpha = np.angle(np.exp(1j * (L * theta + 2 * math.pi * np.arange(M)) / M))
        winning = np.flatnonzero(abs(abs(alpha) - min(abs(alpha))) < 1e-12)
        expected_e = -2 * (L - 2) - 4 * math.cos(math.pi / L) * math.cos(float(alpha[winning[0]]) / L)
        low = abs(ev - ev[0]) < 1e-10
        assert int(sum(low)) == len(winning)
        assert abs(ev[0] - expected_e) < 2e-12
        resolved = np.zeros(len(ps))
        resolved[ps.index(form_q(L, 1))] = 1
        coherent = resolved.copy()
        coherent[ps.index(form_q(L, -1))] = 1
        coherent /= math.sqrt(2)
        wr = float(np.sum(abs(V[:, low].conj().T @ resolved)**2))
        wc = float(np.sum(abs(V[:, low].conj().T @ coherent)**2))
        expected_wr = weight * len(winning)
        expected_wc = weight * sum(1 + math.cos(theta - float(alpha[s])) for s in winning)
        assert abs(wr - expected_wr) < 2e-12
        assert abs(wc - expected_wc) < 2e-12
        row = {'L': L, 'theta': theta, 'dimension': len(ps),
               'lowest_dimension': int(sum(low)), 'energy': float(ev[0]),
               'energy_formula_error': float(abs(ev[0] - expected_e)),
               'resolved_full_lowest_weight': wr, 'resolved_formula': expected_wr,
               'coherent_full_lowest_weight': wc, 'coherent_formula': expected_wc}
        if theta == 0:
            gap = 4 * math.cos(math.pi / L) * (1 - math.cos(2 * math.pi / (L * M)))
            assert abs((ev[1] - ev[0]) - gap) < 2e-12
            assert sum(abs(ev - ev[1]) < 1e-10) == 2
            row.update({'gap': float(ev[1] - ev[0]), 'gap_formula': gap,
                        'first_excited_dimension': 2,
                        'curvature_formula': 4 * math.cos(math.pi / L) / M**2})
        band_rows.append(row)

# Direct-integral control.  Sum each equally spaced L-tuple of angles before
# integration; the coherent correction vanishes pointwise in this grouping.
# This tests arbitrary generic base angles, avoiding a quadrature crossing.
angle_rows = []
for L in (3, 4, 6, 9, 20):
    M = L + 2
    sums = []
    for theta in (.071, .173, .311):
        terms = []
        for j in range(L):
            x = theta + 2 * math.pi * j / L
            alpha = np.angle(np.exp(1j * (L * x + 2 * math.pi * np.arange(M)) / M))
            chosen = float(alpha[np.argmin(abs(alpha))])
            terms.append(math.cos(x - chosen))
        sums.append(sum(terms))
    assert max(abs(x) for x in sums) < 3e-13
    angle_rows.append({'L': L, 'cyclic_angle_sums': sums})

# The crossing exception is real, not a numerical choice of eigenvectors.
cross = next(r for r in band_rows if r['L'] == 4 and r['theta'] == math.pi / 4)
assert abs(cross['resolved_full_lowest_weight'] - 1 / 24) < 2e-12
assert abs(cross['resolved_full_lowest_weight'] - 1 / 48) > .02

out = {
    'status': 'All selective comparisons passed; no author builder was imported or executed.',
    'pre_seal_sha256': PRE_SHA,
    'pre_source_bindings_authenticated': len(pre['sources']),
    'pre_artifact_bindings_authenticated': len(pre['artifacts']),
    'author_seal_sha256': AUTHOR_SHA,
    'author_bindings_authenticated': author_rows,
    'author_saved_execution_checks': result_rows,
    'new_independent_ground_gap_and_crossing_controls': band_rows,
    'normalizable_uniform_angle_controls': angle_rows,
    'crossing_countercontrol': {'L': 4, 'theta': math.pi / 4,
        'full_ground_space_resolved_weight': cross['resolved_full_lowest_weight'],
        'generic_rank_one_weight_inapplicable_at_crossing': 1 / 48},
    'coverage_limits': 'Finite controls corroborate the reconstructed proof; they do not establish arbitrary L or microscopic conditioned histories. Author scripts and all saved result fields were inspected, not rerun.',
}
p = D / 'COMPARISON_RESULTS.json'
assert not p.exists()
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
