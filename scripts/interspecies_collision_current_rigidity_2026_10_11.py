#!/usr/bin/env python3
"""Exact finite author controls for conditional interspecies current rigidity.

Claim: interspecies_collision_current_rigidity_bounded_theorem_note_2026-10-11
Uses only Python's standard library, exact Fraction arithmetic, and fixed
finite fixtures. No file, network, stochastic, or installed-package input is
read. AUDIT_INPUT_PATHS declares the accompanying claim contract for repository
evidence binding; it does not import additional physical assumptions.

The original executable helper body is preserved literally below. This is
author-evidence replay, not independent analytic review or Lean verification.
A root-added exact symmetric-family check follows the unchanged original
body. TOTAL counts eight finite matrix families plus six algebraic families, not individual assertions, continuum proof obligations, or physics.
"""

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = [
    "docs/INTERSPECIES_COLLISION_CURRENT_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]

if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from fractions import Fraction as Q
from itertools import permutations, product
import json


def vec(x):
    return tuple(Q(t) for t in x)


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def cross(x, y):
    return (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2],
            x[0]*y[1]-x[1]*y[0])


def rank(rows, ncols=None):
    if not rows:
        return 0
    a = [list(map(Q, row)) for row in rows]
    width = len(a[0]) if ncols is None else ncols
    assert all(len(row) == width for row in a)
    pivot_row = 0
    for col in range(width):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor*y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def affine_rank(points):
    return rank([sub(x, points[0]) for x in points[1:]])


def determinant3(columns):
    return dot(columns[0], cross(columns[1], columns[2]))


def cross_matrix(x, y, omit=()):
    """Rows of (W_Ai-W_Bj) cross (x_i-y_j)=0; equal edges absent."""
    n = 3 * (len(x) + len(y))
    rows = []
    equal = 0
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            if (i, j) in omit:
                continue
            d = sub(a, b)
            if d == (0, 0, 0):
                equal += 1
                continue
            dx, dy, dz = d
            for block in ((0, dz, -dy), (-dz, 0, dx), (dy, -dx, 0)):
                row = [Q(0)] * n
                for axis, value in enumerate(block):
                    row[3*i + axis] = value
                    row[3*(len(x)+j) + axis] = -value
                rows.append(row)
    return rows, equal


results = []


def case(name, x0, y0, expected, omit=(), full=False):
    x, y = list(map(vec, x0)), list(map(vec, y0))
    rows, equal = cross_matrix(x, y, omit)
    n = 3*(len(x)+len(y))
    actual_rank = rank(rows)
    assert n - actual_rank == expected, (name, n-actual_rank, expected)
    modes = [tuple(Q(int(i % 3 == axis)) for i in range(n)) for axis in range(3)]
    modes.append(tuple(v for point in x+y for v in point))
    assert all(dot(row, mode) == 0 for row in rows for mode in modes)
    assert rank(modes) == 4
    if full:
        assert affine_rank(x) == affine_rank(y) == 3
    record = dict(name=name, a=len(x), b=len(y), equal_edges=equal,
                  rank=actual_rank, nullity=n-actual_rank,
                  image_affine_ranks=[affine_rank(x), affine_rank(y)],
                  omitted_edges=list(omit))
    results.append(record)
    print(json.dumps(record, sort_keys=True))
    return x, y, rows


zero, e1, e2, e3 = (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)
case('noncoplanar_K22', [zero, e1], [e2, e3], 4)
case('delete_one_anchor_edge', [zero, e1], [e2, e3], 6, omit=((1, 1),))
case('one_opposite_line_residual', [zero, e1, (0, 2, -1)], [e2, e3], 5)
case('two_opposite_line_residuals_eliminated',
     [zero, e1, (0, 2, -1)], [e2, e3, (2, 0, 0)], 4)
case('full_span_equal_velocities_and_repeated_label',
     [zero, e1, (0, 2, -1), e2, zero], [e2, e3, (2, 0, 0), zero], 4, full=True)
case('full_span_disjoint_images', [zero, e1, e2, e3],
     [(2, 1, 1), (1, 3, 1), (1, 1, 4), (2, 3, 4)], 4, full=True)
case('collinear_images_not_rigid', [(-1, 0, 0), zero, e1],
     [(-2, 0, 0), zero, (2, 0, 0)], 8)
x, y, rows = case('coplanar_K22_flex', [zero, (1, 1, 0)], [e1, e2], 5)
flex = tuple(map(Q, (0, 0, 0, 2, 3, 0, 2, 0, 0, 0, 3, 0)))
assert all(dot(row, flex) == 0 for row in rows)
assert flex[3] != flex[4]  # Common dilation is impossible on these coordinates.

# The exceptional cross edge: alpha*V-beta*U=t*(x-y) has only the zero solution.
u, v = vec(e1), vec((0, -1, 1))
x, y = vec((0, 2, -1)), vec((2, 0, 0))
skew_det = determinant3([v, tuple(-z for z in u), tuple(-z for z in sub(x, y))])
assert skew_det != 0
print('exceptional_skew_determinant:', str(skew_det))

# Exact proper cubic group and its vector/symmetric-matrix fixed spaces.
def perm_sign(p):
    return -1 if sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3)) % 2 else 1


group = []
for p in permutations(range(3)):
    for signs in product((-1, 1), repeat=3):
        if perm_sign(p) * signs[0]*signs[1]*signs[2] == 1:
            group.append(tuple(tuple(Q(signs[i] if j == p[i] else 0) for j in range(3))
                               for i in range(3)))
assert len(set(group)) == 24


def mv(r, x):
    return tuple(dot(row, x) for row in r)


def mm(r, s):
    return tuple(tuple(sum(r[i][k]*s[k][j] for k in range(3)) for j in range(3))
                 for i in range(3))


assert all(mm(r, s) in group for r in group for s in group)
assert all(sum(r[i][j] for r in group) == 0 for i in range(3) for j in range(3))
for p in (e1, (1, 1, 0), (1, 2, 3), (1, 1, 1)):
    assert affine_rank([mv(r, vec(p)) for r in group]) == 3
vector_rows = [tuple(r[i][j] - int(i == j) for j in range(3))
               for r in group for i in range(3)]
assert rank(vector_rows) == 3
matrix_rows = []
for r in group:
    for i in range(3):
        for j in range(3):
            matrix_rows.append([r[a][i]*r[b][j] - int(a == i and b == j)
                                for a in range(3) for b in range(3)])
assert rank(matrix_rows) == 8
print('proper_cubic_group: 24 elements; vector fixed dimension 0; matrix commutant dimension 1')

# At full-affine-span velocities, closedness of a*E+B*k forces a=0 and B symmetric.
curl_rows = []
for velocity in map(vec, [zero, e1, e2, e3]):
    for i in range(3):
        for j in range(i+1, 3):
            row = [Q(0)] * 12  # a[0:3], B row-major[3:12]
            row[i] += velocity[j]
            row[j] -= velocity[i]
            row[3+3*i+j] += 1
            row[3+3*j+i] -= 1
            curl_rows.append(row)
assert rank(curl_rows) == 6
for i in range(3):
    e = [Q(0)] * 12
    e[i] = 1
    assert rank(curl_rows + [e]) == rank(curl_rows)
print('closed-current constraints: dimension 6, all a components forced zero')

# Exact normal collision exposing the need for full support of the a.e. measure.
a, b = vec(e1), vec(zero)
c, d = vec((Q(1, 2), Q(1, 2), 0)), vec((Q(1, 2), -Q(1, 2), 0))
assert tuple(a[i]+b[i] for i in range(3)) == tuple(c[i]+d[i] for i in range(3))
assert dot(a, a)+dot(b, b) == dot(c, c)+dot(d, d)
defect = a[0]**3 + b[0]**3 - c[0]**3 - d[0]**3
assert defect == Q(3, 4)
print('non_full_support_measure_witness: charge defect', str(defect))

# Disjoint symmetry-orbit balls support the non-invariant-domain counterexample.
q = vec((Q(1, 5), Q(2, 5), Q(3, 5)))
orbit = [mv(r, q) for r in group]
assert len(set(orbit)) == 24
distance2 = min(dot(sub(x, y), sub(x, y)) for i, x in enumerate(orbit)
                for y in orbit[i+1:])
inner_radius = Q(1, 100)
assert distance2 > (4*inner_radius)**2
print('chamber_orbit: min squared separation', str(distance2), 'inner radius', str(inner_radius))
print('PASS: exact finite controls; no continuum proof, amplitude support, or physical adoption certified')

# Identify the six-dimensional kernel itself, not just its dimension.
# A wrong curl sign can preserve rank and a=0 while replacing symmetry by
# antisymmetry off the diagonal. These six independent symmetric modes must
# all solve the original curl constraints.
symmetric_current_modes = []
for i in range(3):
    for j in range(i, 3):
        mode = [Q(0)] * 12
        mode[3+3*i+j] = 1
        mode[3+3*j+i] = 1
        symmetric_current_modes.append(mode)
assert rank(symmetric_current_modes) == 6
assert all(dot(row, mode) == 0 for row in curl_rows for mode in symmetric_current_modes)
print('closed-current symmetric family: six independent modes in kernel')

# Eight matrix families and six algebraic families, including this kernel check.
print(f"TOTAL: PASS={len(results) + 6} FAIL=0")
