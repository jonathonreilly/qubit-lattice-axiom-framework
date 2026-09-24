"""Exact physical seven-site tree; no inherited builder or floating arithmetic."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/finite_path_control.py',)
from pathlib import Path
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
import json

HERE = Path(__file__).resolve().parent
A = (1, 3, 5)
B = (0, 2, 4, 6)
EDGES = ((1, 0), (1, 2), (3, 2), (3, 4), (5, 4), (5, 6))
EDGE = {e: i for i, e in enumerate(EDGES)}
NB = {a: tuple(b for aa, b in EDGES if aa == a) for a in A}
PAIRS = [p for p in combinations(A, 2) if set(NB[p[0]]) & set(NB[p[1]])]

def fields(q):
    # On a tree the charge-compatible physical field is unique.
    source = [q[x] - int(x in A) for x in range(7)]
    assert sum(source) == 0
    result = []
    for a, b in EDGES:
        cut = min(a, b)
        outward_from_left = sum(source[:cut+1])
        result.append(outward_from_left if a < b else -outward_from_left)
    div = [0] * 7
    for (a, b), e in zip(EDGES, result):
        div[a] += e
        div[b] -= e
    assert div == source
    return tuple(result)

def hop(q, a, b):
    if not q[a] or q[b]:
        return None
    old = q[a]
    dest = list(q)
    dest[a] = 0
    dest[b] = old
    dest = tuple(dest)
    before, after = fields(q), fields(dest)
    expected = list(before)
    expected[EDGE[(a, b)]] -= old
    assert tuple(expected) == after
    return dest

def birth(q, a, b, sigma):
    assert not q[a] and not q[b]
    dest = list(q)
    dest[a], dest[b] = sigma, -sigma
    dest = tuple(dest)
    before, after = fields(q), fields(dest)
    expected = list(before)
    expected[EDGE[(a, b)]] += sigma
    assert tuple(expected) == after
    assert sum(x != 0 for x in dest) == sum(x != 0 for x in q) + 2
    return dest

STATES = []
for qa in product((-1, 1), repeat=3):
    for qb in product((-1, 0, 1), repeat=4):
        q = [0] * 7
        for a, val in zip(A, qa): q[a] = val
        for b, val in zip(B, qb): q[b] = val
        if sum(q) == 3:
            STATES.append(tuple(q))
INDEX = {q: i for i, q in enumerate(STATES)}
SIZE = len(STATES)
NUM = [sum(v != 0 for v in q) for q in STATES]
F = [fields(q) for q in STATES]

def zero(): return [[0] * SIZE for _ in range(SIZE)]

def gram(columns):
    g = zero()
    for i, left in enumerate(columns):
        for j, right in enumerate(columns):
            g[i][j] = sum(v * right.get(k, 0) for k, v in left.items())
    return g

def add(target, source, factor=1):
    for i in range(SIZE):
        for j in range(SIZE): target[i][j] += factor * source[i][j]

def mat_columns(columns):
    m = zero()
    for j, col in enumerate(columns):
        for q, val in col.items(): m[INDEX[q]][j] += val
    return m

def mv(matrix, v):
    return [sum(a * b for a, b in zip(row, v)) for row in matrix]

def sparse(matrix):
    return [[i, j, value] for i, row in enumerate(matrix)
            for j, value in enumerate(row) if value]

H4 = zero()
pair_columns = {}
for a, c in PAIRS:
    columns = []
    for q in STATES:
        out = Counter()
        for b in NB[a]:
            first = hop(q, a, b)
            if first is None: continue
            for d in NB[c]:
                second = hop(first, c, d)
                if second is not None: out[second] += 1
        columns.append(dict(out))
    pair_columns[(a, c)] = columns
    add(H4, gram(columns), -2)

D = [sum((1 - int(q[b] != 0)) * e * (e - q[a])
         for (a, b), e in zip(EDGES, field)) for q, field in zip(STATES, F)]
assert min(D) >= 0
assert all(H4[i][j] == H4[j][i] for i in range(SIZE) for j in range(SIZE))
assert all(not H4[i][j] or NUM[i] == NUM[j]
           for i in range(SIZE) for j in range(SIZE))

RES = {}
RAW = {}
GAMMA = zero()
for a, b in EDGES:
    for sigma in (-1, 1):
        cols = []
        for q in STATES:
            out = Counter()
            if not q[b]:
                for c in NB[a]:
                    if c == b: continue
                    first = hop(q, a, c)
                    if first is not None:
                        dest = birth(first, a, b, sigma)
                        assert dest in INDEX
                        out[dest] += 1
            cols.append(dict(out))
        key = (a, b, sigma)
        RAW[key] = cols
        RES[key] = mat_columns(cols)
        add(GAMMA, gram(cols))
        assert all(not RES[key][i][j] or NUM[i] - NUM[j] == 2
                   for i in range(SIZE) for j in range(SIZE))

COH = {}
GAMMA_COH = zero()
for a, b in EDGES:
    negative, positive = RAW[(a, b, -1)], RAW[(a, b, 1)]
    assert all(not (set(left) & set(right)) for left in negative for right in positive)
    cols = []
    for left, right in zip(negative, positive):
        merged = Counter(left)
        merged.update(right)
        cols.append(dict(merged))
    COH[(a, b)] = mat_columns(cols)
    add(GAMMA_COH, gram(cols))
assert GAMMA_COH == GAMMA
assert all(not GAMMA[i][j] or NUM[i] == NUM[j]
           for i in range(SIZE) for j in range(SIZE))

# Twice the Heisenberg dissipator on N equals 4 Gamma, exactly.
for channels in (RES, COH):
    twice_image = zero()
    for matrix in channels.values():
        for i in range(SIZE):
            for j in range(SIZE):
                twice_image[i][j] += sum(
                    matrix[o][i] * matrix[o][j] * (2 * NUM[o] - NUM[i] - NUM[j])
                    for o in range(SIZE))
    assert twice_image == [[4 * x for x in row] for row in GAMMA]

initial = tuple(int(x in A) for x in range(7))
initial_index = INDEX[initial]
psi = [int(i == initial_index) for i in range(SIZE)]
assert D[initial_index] == 0
assert mv(H4, psi) == [-12 * x for x in psi]
assert mv(GAMMA, psi) == [12 * x for x in psi]
assert max(sum(abs(x) for x in row) for row in GAMMA) <= 12

dark = []
for key, matrix in RES.items():
    if key[0] != 3: continue
    out = mv(matrix, psi)
    assert sum(x*x for x in out) == 1
    assert mv(H4, out) == [0] * SIZE
    assert [D[i] * out[i] for i in range(SIZE)] == [0] * SIZE
    assert mv(GAMMA, out) == [0] * SIZE
    state_index = next(i for i, value in enumerate(out) if value)
    assert NUM[state_index] == 5
    q = STATES[state_index]
    assert [b for b in B if not q[b]] == [0, 6]
    dark.append(dict(mark=list(key), q=list(q), E=list(F[state_index]),
                     records=NUM[state_index], D=D[state_index]))
for key, matrix in COH.items():
    if key[0] != 3: continue
    out = mv(matrix, psi)
    assert sum(x*x for x in out) == 2
    assert mv(H4, out) == [0] * SIZE
    assert [D[i] * out[i] for i in range(SIZE)] == [0] * SIZE
    assert mv(GAMMA, out) == [0] * SIZE

result = dict(
    arithmetic='integer and Fraction only', graph='seven-site path, all edges A to B',
    vertices=7, A=list(A), B=list(B), edges=list(EDGES), pair_anchors=PAIRS,
    physical_dimension=SIZE, number_sector_dimensions=dict(sorted(Counter(NUM).items())),
    all_Gauss_constraints=True, exact_number_balance=True,
    resolved_coherent_loss_equal=True, H4_preserves_number=True,
    first_total_rate_divided_by_kappa=12,
    initial_H4_eigenvalue=-12, initial_D_eigenvalue=0,
    dark_first_mark_weight=str(Fraction(4, 12)), dark_first_outputs=dark,
    unused_birth_capacity_in_dark_output=1,
    max_total_births_from_initial=2,
    Gamma_norm_bound_by_row_sum=max(sum(abs(x) for x in row) for row in GAMMA),
    states=[dict(q=list(q), E=list(e), N=n, D=d) for q, e, n, d in zip(STATES, F, NUM, D)],
    sparse_H4=sparse(H4), sparse_Gamma=sparse(GAMMA),
    resolved_jumps={str(k): sparse(v) for k, v in RES.items()},
    coherent_jumps={str(k): sparse(v) for k, v in COH.items()},
)
(HERE / 'FINITE_PATH_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in [
    'physical_dimension', 'number_sector_dimensions', 'all_Gauss_constraints',
    'exact_number_balance', 'resolved_coherent_loss_equal',
    'first_total_rate_divided_by_kappa', 'initial_H4_eigenvalue',
    'dark_first_mark_weight', 'unused_birth_capacity_in_dark_output',
    'Gamma_norm_bound_by_row_sum']}, indent=2))
