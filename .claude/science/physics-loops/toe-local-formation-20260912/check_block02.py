"""Small exact challenges to Block 2; same author, not independent review.

Direct bit-action Fock densities and real leaf pulses are compared with the
derived covariance updates. Complete normal moments test Gaussian closure.
The non-Gaussian counterexample must disagree with the Gaussian formula.
"""
from pathlib import Path
from itertools import combinations, product
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
R = s.Rational
checks = {}


def clean(value):
    # Every fixture entry is in Q(i); canonical expansion prevents expression
    # trees growing across histories. No floating arithmetic or tolerance.
    return value.applyfunc(s.expand) if isinstance(value, s.MatrixBase) else s.expand(value)


def equal(left, right):
    delta = clean(left - right)
    if isinstance(delta, s.MatrixBase):
        return all(v == 0 for v in delta)
    return delta == 0


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


def car(m):
    ops = []
    for j in range(m):
        a = s.zeros(2**m)
        for n in range(2**m):
            if (n >> j) & 1:
                a[n ^ (1 << j), n] = (-1)**((n % (1 << j)).bit_count())
        ops.append(a)
    return ops


def covariance(rho, ops):
    return clean(s.Matrix(len(ops), len(ops),
                    lambda i, j: s.trace(rho * ops[j].H * ops[i])))


def pair_dwell(ops, i, j, co, si):
    h = ops[i].H * ops[j] + ops[j].H * ops[i]
    return s.eye(h.rows) + (co-1)*h*h - s.I*si*h


OPS = car(3)
IDENT = s.eye(8)
NUM = [a.H*a for a in OPS]
DWELL = pair_dwell(OPS, 0, 1, R(3, 5), R(4, 5))
PHASE = IDENT + (R(5, 13) + s.I*R(12, 13) - 1)*NUM[1]
DWELL2 = pair_dwell(OPS, 1, 2, R(8, 17), R(15, 17))
ROTATE = clean(DWELL2*PHASE*DWELL)
check('rotation_unitary', equal(ROTATE.H*ROTATE, IDENT))


def ready(occupations, rotate=True):
    entries = []
    for n in range(8):
        entries.append(s.prod(q if (n >> j) & 1 else 1-q
                              for j, q in enumerate(occupations)))
    rho = s.diag(*entries)
    return clean(ROTATE*rho*ROTATE.H) if rotate else rho


def direct_leaf(rho, j, leaf, r, same):
    if same:
        k = IDENT + (r-1)*(NUM[j] if leaf == 0 else IDENT-NUM[j])
        unnormalized = k*rho*k.H
    else:
        k = OPS[j] if leaf == 0 else OPS[j].H
        unnormalized = (1-r*r)*k*rho*k.H
    unnormalized = clean(unnormalized)
    mass = clean(s.trace(unnormalized))
    return mass, clean(unnormalized/mass) if mass else None


def formula(C, j, leaf, r, same):
    eye = s.eye(C.rows)
    p = s.zeros(C.rows)
    p[j, j] = 1
    d = eye + (r-1)*p
    a = 1-r*r
    q = C if leaf == 0 else eye-C
    if same:
        mass = 1-a*q[j, j]
        updated = d*(q+a/mass*q*p*q)*d if mass else None
    else:
        mass = a*q[j, j]
        updated = q-q*p*q/q[j, j] if mass else None
    if updated is not None and leaf == 1:
        updated = eye-updated
    return clean(mass), clean(updated) if updated is not None else None


def wick(rho, C):
    for k in range(4):
        lists = list(combinations(range(3), k))
        for rows in lists:
            for cols in lists:
                op = IDENT
                for j in cols:
                    op = op*OPS[j].H
                for i in reversed(rows):
                    op = op*OPS[i]
                expected = C.extract(rows, cols).det() if k else 1
                if not equal(s.trace(rho*op), expected):
                    return False
    return True


fixtures = [
    ('complex_mixed', ready((R(1, 5), R(2, 3), R(3, 7))), 1, R(3, 5)),
    ('complex_pure', ready((s.S.One, s.S.Zero, s.S.Zero)), 0, R(3, 5)),
    ('boundary_mixed', ready((s.S.One, s.S.Zero, R(1, 2))), 2, s.S.Zero),
    ('vacuum_r0', ready((0, 0, 0), False), 0, s.S.Zero),
    ('filled_r0', ready((1, 1, 1), False), 1, s.S.Zero),
    ('vacuum_r1', ready((0, 0, 0), False), 2, s.S.One),
    ('filled_r1', ready((1, 1, 1), False), 0, s.S.One),
]
for name, rho, j, r in fixtures:
    C = covariance(rho, OPS)
    check(name+'_input_Wick', wick(rho, C))
    for leaf, same in product((0, 1), (True, False)):
        tag = f'{name}_leaf{leaf}_same{same}'
        mass, out = direct_leaf(rho, j, leaf, r, same)
        predicted_mass, predicted_C = formula(C, j, leaf, r, same)
        check(tag+'_mass', equal(mass, predicted_mass))
        check(tag+'_support', (out is None) == (predicted_C is None))
        if out is not None:
            check(tag+'_covariance', equal(covariance(out, OPS), predicted_C))
            check(tag+'_full_Wick', wick(out, predicted_C))
print('Four branches, complex covariances, pure/mixed boundaries and null support checked.', flush=True)

# Explicit fourth-mode leaf pulse and projective readout; no Kraus shortcut.
ops4 = car(4)
id4 = s.eye(16)
for leaf in (0, 1):
    rho = fixtures[0][1]
    ready4 = s.zeros(16)
    for i in range(8):
        for j in range(8):
            ready4[i+8*leaf, j+8*leaf] = rho[i, j]
    pulse = pair_dwell(ops4, 1, 3, R(3, 5), R(4, 5))
    evolved = clean(pulse*ready4*pulse.H)
    for bit in (0, 1):
        out = evolved.extract(range(8*bit, 8*(bit+1)),
                              range(8*bit, 8*(bit+1)))
        mass, normalized = direct_leaf(rho, 1, leaf, R(3, 5), bit == leaf)
        check(f'actual_leaf_pulse_{leaf}{bit}', equal(out, mass*normalized))

# One complete three-event tree, including both sorts of initially sharp leaf.
histories = [('', s.S.One, fixtures[0][1], covariance(fixtures[0][1], OPS))]
for event, (j, leaf, r, co, si) in enumerate([
        (0, 0, R(3, 5), R(5, 13), R(12, 13)),
        (2, 1, R(4, 5), R(8, 17), R(15, 17)),
        (1, 0, R(5, 13), s.S.One, s.S.Zero)]):
    next_histories = []
    unitary = pair_dwell(OPS, event % 2, event % 2 + 1, co, si)
    # Derive single-particle matrix from the one-particle Fock sector.
    one_particle = unitary.extract((1, 2, 4), (1, 2, 4))
    for history, weight, rho, C in histories:
        evolved = clean(unitary*rho*unitary.H)
        C_evolved = clean(one_particle*C*one_particle.H)
        check(f'dwell_{event}_{history}', equal(covariance(evolved, OPS), C_evolved))
        for same in (True, False):
            mass, out = direct_leaf(evolved, j, leaf, r, same)
            predicted_mass, predicted_C = formula(C_evolved, j, leaf, r, same)
            tag = history+str(leaf if same else 1-leaf)
            check('history_mass_'+tag, equal(mass, predicted_mass))
            if mass:
                check('history_covariance_'+tag, equal(covariance(out, OPS), predicted_C))
                next_histories.append((tag, weight*mass, out, predicted_C))
    histories = next_histories
    print(f'Complete event depth {event+1}: {len(histories)} supported histories.', flush=True)
check('complete_history_mass', equal(sum(row[1] for row in histories), 1))

# Deliberate assumption challenge: equal covariance, different conditional law.
correlated = s.zeros(8)
correlated[0, 0] = correlated[3, 3] = R(1, 2)
C_bad = covariance(correlated, OPS)
mass_bad, out_bad = direct_leaf(correlated, 0, 0, R(3, 5), True)
_, predicted_bad = formula(C_bad, 0, 0, R(3, 5), True)
actual_other = covariance(out_bad, OPS)[1, 1]
check('nonGaussian_input_violates_Wick', not wick(correlated, C_bad))
check('nonGaussian_formula_must_disagree', not equal(actual_other, predicted_bad[1, 1]))
check('nonGaussian_exact_other_occupation', equal(actual_other, R(9, 34)))

# Finite-path shortest-walk coefficients, and separate infinite walk counts.
for length in (3, 5):
    path = s.zeros(length)
    for j in range(length-1):
        path[j+1, j] = path[j, j+1] = R(j+2, j+1)
    for d in range(1, length):
        for k in range(d):
            check(f'path_zero_{length}_{d}_{k}', equal((path**k)[d, 0], 0))
        check(f'path_shortest_{length}_{d}',
              equal((path**d)[d, 0], s.prod(path[j+1, j] for j in range(d))))
        check(f'path_parity_{length}_{d}', equal((path**(d+1))[d, 0], 0))

for d in range(5):
    for n in range(4):
        # Number of length d+2n signed-step walks with net displacement d.
        k = d+2*n
        walk_coefficient = (-s.I)**k*s.binomial(k, n)/s.factorial(k)
        series_coefficient = (-s.I)**d*(-1)**n/(s.factorial(n)*s.factorial(n+d))
        check(f'shift_coefficient_{d}_{n}', equal(walk_coefficient, series_coefficient))

payload = {
    'status': 'all_small_exact_checks_passed',
    'author_check_only': True,
    'proof': 'BLOCK02_DERIVATION.md',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'checks': checks,
    'check_count': len(checks),
    'complete_three_event_law': {history: str(weight) for history, weight, _, _ in histories},
    'nonGaussian_counterexample': {
        'actual_other_occupation_after_same': str(actual_other),
        'Gaussian_formula_wrongly_predicts': str(predicted_bad[1, 1]),
        'interpretation': 'The Gaussian restriction is necessary for the general covariance update.'
    },
}
(ROOT/'BLOCK02_CHECKS.json').write_text(json.dumps(payload, indent=2)+'\n')
print(json.dumps({key: value for key, value in payload.items()
                  if key not in ('checks', 'complete_three_event_law')}, indent=2))
