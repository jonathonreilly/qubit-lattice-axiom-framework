"""Bounded post-seal comparison. Never executes/imports an author runner.

Original PRE, scientific scripts and results are read-only. The new spectral
point uses the independently assembled physical square in finite_spin_check.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import sys
import numpy as np
import sympy as sp
from scipy.linalg import eigh

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PRE_HASH = 'f8f457305153006eccda68740a518cfed0c11d3c28d1c77ad3ce6df71970e3c5'
AUTHOR_HASH = '40797e4620ebb864744753ae5429a1727c7b407fc712bda4360e75ea295a1f3b'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def authenticate(path, expected, keys):
    assert sha(path) == expected, (str(path), sha(path), expected)
    obj = json.loads(Path(path).read_text())
    rows = []
    for key in keys:
        for row in obj[key]:
            data = Path(row['path']).read_bytes()
            assert len(data) == row['bytes'], row['path']
            assert hashlib.sha256(data).hexdigest() == row['sha256'], row['path']
            rows.append(dict(row))
    return rows


def exact_comparison():
    blind = json.loads((HERE/'FINITE_SPIN_RESULTS.json').read_text())
    author = json.loads((BASE/'LARGE_SPIN_RECORD_ELECTRIC_RING_RESULTS.json').read_text())
    live = json.loads((BASE/'LARGE_SPIN_LIVE_BIRTH_AND_WEIGHT_RESULTS.json').read_text())
    exact = {int(r['spin']): r for r in author['exact_square_coefficients'] if r['spin'] != '1/2'}
    live_by_s = {r['spin']: r for r in live['complete_live_sectors']}
    rows = []
    for b in blind['exact_square_controls']:
        s = b['spin']; a = exact[s]; l = live_by_s[s]
        assert b['initial_number_dimension'] == a['dimension']
        assert b['dimension'] == l['complete_physical_dimension']
        assert b['low_dimension'] == a['low_dimension'] == l['code_dimension']
        for c in b['coefficients'].values():
            assert c['H2'] == a['second_coefficient']
            assert c['normalized_H4'] == a['fourth_coefficient']
        for e in b['birth_loss_controls']:
            assert max(map(sp.Rational, e['loss_eigenvalues'])) == sp.Rational(l['largest_local_loss_eigenvalue_exact'])
        rows.append({'spin': s, 'full_live_dimension': b['dimension'],
                     'initial_number_dimension': a['dimension'],
                     'both_penalties_H2_and_H4_identical': True,
                     'loss_and_dimension_normalizations_match': True})
    half = author['exact_square_coefficients'][0]
    assert half['spin'] == '1/2'
    # At spin half the normalized link is 2/sqrt(3) times the unit link.
    scale2 = sp.Rational(4,3)
    assert sp.Matrix(half['second_coefficient']) == -2*scale2*sp.eye(2)
    assert sp.Matrix(half['fourth_coefficient']) == scale2**2*sp.Matrix([[2,-2],[-2,2]])
    return {'rows': rows, 'extra_spin_half_normalization_exact': True}


def fourth_order_basis_control():
    """A permitted analytic code rotation can change finite-S fourth order.

    This is distinct from the PRE's specific edgewise circuit, whose order-four
    code coefficient was checked equal to the canonical coefficient. Write
    exp(epsilon^2 G), G=W_S-W_S^dag. Its change is [G,H2].
    """
    rows = []
    for s in (1,2,3,5):
        c = sp.Integer(s*(s+1)); levels = list(range(-s,s+1)); n = len(levels)
        w = sp.zeros(n)
        for i,m in enumerate(levels[:-1]):
            w[i+1,i] = (1-sp.Rational(m*(m+1),c))**2
        g = w-w.T
        h2 = sp.diag(*[-4+4*sp.Rational(m*m,c) for m in levels])
        change = g*h2-h2*g
        assert change == change.T and change != sp.zeros(n)
        assert change[s+1,s] == -4/c
        weighted = c*change*sp.diag(*[sp.Rational(1,1+m*m) for m in levels])
        maxrow = max(sum(abs(weighted[i,j]) for j in range(n)) for i in range(n))
        maxcol = max(sum(abs(weighted[i,j]) for i in range(n)) for j in range(n))
        assert maxrow <= 12 and maxcol <= 12
        assert g*(-4*sp.eye(n))-(-4*sp.eye(n))*g == sp.zeros(n)
        rows.append({'spin': s, 'entry_1_0_in_GH2_commutator': str(-4/c),
                     'nonzero_finite_spin_fourth_order_basis_change': True,
                     'C_times_right_weighted_max_row_sum': str(maxrow),
                     'C_times_right_weighted_max_column_sum': str(maxcol),
                     'scalar_second_order_commutator_zero': True})
    return {'rows': rows,
            'scope': 'Independent post-seal illustration of admissible analytic block-basis freedom; does not assert the author circuit has a nonzero basis change.',
            'general_certificate': 'For integer m, |2m+1|/(1+m^2)<=3/2. Each row/column has at most two entries, each <=6/C after right multiplication by (1+E^2)^-1. The unit-shift H2 is scalar.'}


def spectral_point():
    # Import our own frozen assembly, not an author script.
    from finite_spin_check import square
    model = square(16)
    active = [i for i,n in enumerate(model['count']) if n == 2]
    tmat = np.array(model['h'].extract(active,active), dtype=float)
    penalty = np.array([model['nb'][i] for i in active], dtype=float)
    code = np.flatnonzero(penalty == 0)
    spin = 16; c = spin*(spin+1); electric = .3; magnetic = 1.
    h = electric*c; delta = 2*h*h/magnetic; hopping = math.sqrt(h*delta)
    constant = -4*h+6*magnetic
    mat = delta*np.diag(penalty)+hopping*tmat-constant*np.eye(len(active))
    energies, vecs = eigh(mat, subset_by_index=(0,5))
    author = json.loads((BASE/'LARGE_SPIN_RECORD_ELECTRIC_RING_RESULTS.json').read_text())['joint_scaling']['rows'][0]
    difference = float(np.max(np.abs(energies-np.array(author['lowest_six_shifted_microscopic_energies']))))
    weight = float(np.sum(vecs[code,0]**2))
    assert difference < 1e-8 and abs(weight-author['ground_code_weight']) < 1e-10
    return {'spin': spin, 'independently_assembled_full_live_dimension': len(model['states']),
            'initial_number_dimension': len(active),
            'lowest_six_shifted_energies': energies.tolist(),
            'largest_difference_from_author_energies': difference,
            'ground_code_weight': weight,
            'residual': float(np.max(np.linalg.norm(mat@vecs-vecs*energies[None,:],axis=0))),
            'scope': 'One independently assembled floating-point finite-square check, not an interval enclosure, large-volume run, or replay of the other three author spectrum points.'}


def receipts_and_arithmetic():
    prefixes = [('LARGE_SPIN_RECORD_ELECTRIC_RING','large_spin_record_electric_ring_check.py'),
                ('LARGE_SPIN_LIVE_BIRTH_AND_WEIGHT','large_spin_live_birth_and_weight_check.py')]
    receipts = []
    for prefix, runner in prefixes:
        result = json.loads((BASE/(prefix+'_RESULTS.json')).read_text())
        receipt = json.loads((BASE/(prefix+'_RUN_RECEIPT.json')).read_text())
        assert result['source_sha256'] == sha(BASE/runner) == receipt['runner_sha256']
        assert result['status'] == 'PASS' and receipt['exit_code'] == 0
        assert (BASE/(prefix+'_RUN.stderr')).read_bytes() == b''
        if prefix == 'LARGE_SPIN_LIVE_BIRTH_AND_WEIGHT':
            assert json.loads((BASE/(prefix+'_RUN.stdout')).read_text()) == result
        else:
            logs = [json.loads(line) for line in (BASE/(prefix+'_RUN.stdout')).read_text().splitlines()]
            assert logs[4:8] == result['joint_scaling']['rows']
            assert logs[-1]['elapsed_seconds'] == result['elapsed_seconds']
        receipts.append({'prefix': prefix, 'source_result_receipt_bound': True, 'exit_code': 0, 'stderr_empty': True})
    result = json.loads((BASE/'LARGE_SPIN_RECORD_ELECTRIC_RING_RESULTS.json').read_text())
    target = np.array(result['joint_scaling']['rotor_lowest_six_energies'])
    rows=[]
    for a in result['joint_scaling']['rows']:
        s=a['spin']; c=s*(s+1); k=a['electric_K']; j=a['magnetic_J']
        error=float(np.max(np.abs(np.array(a['lowest_six_shifted_microscopic_energies'])-target)))
        assert math.isclose(a['Delta'],2*k*k*c*c/j,rel_tol=1e-13)
        assert math.isclose(a['epsilon']**2,j/(2*k*c),rel_tol=1e-13)
        assert math.isclose(a['removed_scalar'],-4*k*c+6*j,rel_tol=1e-13)
        assert math.isclose(a['hopping_t']**2/a['Delta'],k*c,rel_tol=1e-13)
        assert a['dimension'] == 12*s+1
        assert error == a['largest_six_energy_error_against_rotor']
        assert math.isclose(error/(a['epsilon']**2),a['error_divided_by_epsilon_squared'],rel_tol=1e-13)
        rows.append({'spin': s, 'energy_difference': error, 'scaling_arithmetic_exactly_recomputed': True})
    return {'receipts': receipts, 'spectrum_arithmetic': rows,
            'scope': 'Identity/arithmetic authentication of all recorded runs; only the separate spin-16 calculation is independently repeated.'}


def main():
    pre = authenticate(HERE/'PRE_COMPARISON_SEAL.json',PRE_HASH,('sources','artifacts'))
    author = authenticate(BASE/'LARGE_SPIN_RECORD_AUTHOR_SEAL.json',AUTHOR_HASH,('artifacts',))
    context = json.loads((BASE/'LARGE_SPIN_RECORD_SOURCE_CONTEXT.json').read_text())
    for row in context['dependencies']:
        assert sha(row['path']) == row['sha256'] and Path(row['path']).stat().st_size == row['bytes']
    out={'created_utc':datetime.now(timezone.utc).isoformat(), 'status':'PASS',
         'authenticated_PRE_bindings':len(pre), 'authenticated_author_bindings':len(author),
         'authenticated_context_dependency_bindings':len(context['dependencies']),
         'exact_presealed_comparison':exact_comparison(),
         'block_basis_control':fourth_order_basis_control(),
         'independent_spectral_point':spectral_point(),
         'receipts_and_arithmetic':receipts_and_arithmetic(),
         'runner_sha256':sha(__file__),
         'limits':'These finite controls do not prove uniform locality, infinite-rotor domains, or a thermodynamic phase. The complete independent analytic reconstruction and source comparison supply the stated mathematical assessment.'}
    text=json.dumps(out,indent=2)+'\n'
    (HERE/'COMPARISON_RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__': main()
