"""Root exact terminal-count calculation from the sealed independent 7-site data.

This script reads matrices but does not import or execute the independent
finite_path_control.py, whose top-level code writes its frozen result file.
"""

from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib
import json
import os
import sympy as sp

HERE = Path(__file__).resolve().parent
D = HERE.parent
OUTPUT = Path(os.environ.get('TERMINAL_PATH_OUTPUT_DIR', HERE))
OUTPUT.mkdir(parents=True, exist_ok=True)
INPUT = D / 'formation_capacity_independent/FINITE_PATH_RESULTS.json'
PRE = D / 'formation_capacity_independent/PRE_COMPARISON_SEAL.json'
DRAFT = D / 'terminal_path_author/SEVEN_SITE_TERMINAL_FORMATION_COUNTS_DRAFT.md'
EXPECTED_PRE = '85c7668c76e47cc472f7b04b380f27f267ab7a3323f39b87b722223286bf45e4'
EXPECTED_INPUT = 'cea5eadb26ba699d2230befbcbb805ec6df29db52ca1b78c4da19d720ff85553'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


assert sha(PRE) == EXPECTED_PRE
assert sha(INPUT) == EXPECTED_INPUT
data = json.loads(INPUT.read_text())
assert data['physical_dimension'] == 52
assert data['number_sector_dimensions'] == {'3': 1, '5': 30, '7': 21}
assert data['all_Gauss_constraints'] and data['exact_number_balance']
assert data['resolved_coherent_loss_equal'] and data['H4_preserves_number']

states = data['states']
initial = next(i for i, s in enumerate(states) if s['N'] == 3)
middle = [i for i, s in enumerate(states) if s['N'] == 5]
assert len(middle) == 30
loc = {v: i for i, v in enumerate(middle)}
D5 = sp.diag(*[states[i]['D'] for i in middle])
H4 = sp.zeros(30)
G0 = sp.zeros(30)
for a, b, v in data['sparse_H4']:
    if a in loc and b in loc:
        H4[loc[a], loc[b]] = v
for a, b, v in data['sparse_Gamma']:
    if a in loc and b in loc:
        G0[loc[a], loc[b]] = v
assert H4 == H4.T and G0 == G0.T
assert G0.is_positive_semidefinite


def first_vectors(sparse_channels):
    result = []
    for label, entries in sparse_channels.items():
        v = sp.zeros(30, 1)
        for row, col, value in entries:
            if col == initial:
                assert row in loc
                v[loc[row]] += value
        if v != sp.zeros(30, 1):
            result.append((label, v))
    return result


sources = {'resolved': first_vectors(data['resolved_jumps']),
           'coherent': first_vectors(data['coherent_jumps'])}
assert all(sum((v.T*v)[0] for _, v in cols) == 12 for cols in sources.values())


def exact_projection(H):
    # Each iteration is the observable row space of Gamma,H. Stability gives
    # the largest H-invariant subspace of ker Gamma by Cayley-Hamilton.
    rows = sp.Matrix.vstack(*[r for r in G0.rowspace()])
    ranks = [rows.rows]
    for power in range(30):
        advanced = rows * H
        next_rows = sp.Matrix.vstack(*[r for r in sp.Matrix.vstack(rows, advanced).rowspace()])
        if next_rows.rows == rows.rows:
            break
        rows = next_rows
        ranks.append(rows.rows)
    else:
        raise AssertionError('Krylov row span failed to stabilize')
    dark_basis = rows.nullspace()
    if not dark_basis:
        P = sp.zeros(30)
    else:
        B = sp.Matrix.hstack(*dark_basis)
        P = B * (B.T*B).inv() * B.T
    assert P*P == P and P.T == P
    assert G0*P == sp.zeros(30) and P*G0 == sp.zeros(30)
    assert H*P == P*H
    assert rows*P == sp.zeros(rows.rows, 30)
    return P, ranks


profiles = []
for name, K, delta in [
    ('pure_magnetic', sp.Rational(0), sp.Rational(1)),
    ('ratio_one_third', sp.Rational(1, 3), sp.Rational(1)),
    ('ratio_one', sp.Rational(1), sp.Rational(1)),
    ('ratio_two', sp.Rational(2), sp.Rational(1)),
    ('ratio_five', sp.Rational(5), sp.Rational(1)),
    ('pure_electric', sp.Rational(1), sp.Rational(0)),
    ('zero_H', sp.Rational(0), sp.Rational(0)),
]:
    H = K*D5 + delta*H4
    assert H == H.T
    P, ranks = exact_projection(H)
    conventions = {}
    for instrument, cols in sources.items():
        projected = [(label, sp.factor((v.T*P*v)[0])) for label, v in cols]
        numerator = sum(value for _, value in projected)
        p1 = sp.factor(numerator/12)
        assert 0 <= p1 <= 1
        assert p1 >= sp.Rational(1, 3)
        conventions[instrument] = {
            'p_exactly_one_birth': str(p1),
            'p_exactly_two_births': str(1-p1),
            'projected_norm_by_first_channel': [
                {'channel': label, 'projected_norm_squared': str(value)}
                for label, value in projected],
            'total_first_norm_squared': '12',
        }
    profiles.append({'name': name, 'K': str(K), 'delta': str(delta),
                     'dark_dimension': int(P.trace()), 'row_ranks': ranks,
                     'instruments': conventions})

out = {
    'exact_arithmetic': 'SymPy rational matrices, no fitted evolution',
    'source_bindings': {str(p): sha(p) for p in (PRE, INPUT, DRAFT)},
    'scope': 'Seven-site physical tree at kappa>0, exact selected K/delta values only',
    'first_event_probability': '1',
    'no_event_survival': 'exp(-12*kappa*t)',
    'physical_dimensions': {'N3': 1, 'N5': 30, 'N7': 21},
    'profiles': profiles,
}
(OUTPUT/'TERMINAL_PATH_EXACT_RESULTS.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({p['name']: {'dark_dimension': p['dark_dimension'],
    'ranks': p['row_ranks'],
    'p1': {k:v['p_exactly_one_birth'] for k,v in p['instruments'].items()}}
    for p in profiles}, indent=2))
