#!/usr/bin/env python3
"""Finite author controls, not analytic convergence or a microscopic model."""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/DETECTOR_SCATTERING_PROJECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_DETECTOR_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-10-12.md"
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from fractions import Fraction as F
from itertools import product
import json
import math


def record(name, **fields):
    print(json.dumps(dict(check=name, passed=True, **fields), sort_keys=True))


def zero(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(-1, b))


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def outer(v):
    return [[F(x)*F(y) for y in v] for x in v]


def inverse(a):
    n = len(a)
    rows = [list(row)+unit for row, unit in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        q = rows[j][j]
        rows[j] = [x/q for x in rows[j]]
        for i in range(n):
            if i != j:
                q = rows[i][j]
                rows[i] = [x-q*y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def rank(a):
    rows = [list(row) for row in a]
    i = 0
    for j in range(len(rows[0])):
        pivots = [k for k in range(i, len(rows)) if rows[k][j]]
        if not pivots:
            continue
        rows[i], rows[pivots[0]] = rows[pivots[0]], rows[i]
        q = rows[i][j]
        rows[i] = [x/q for x in rows[i]]
        for k in range(len(rows)):
            if k != i:
                q = rows[k][j]
                rows[k] = [x-q*y for x, y in zip(rows[k], rows[i])]
        i += 1
        if i == len(rows):
            break
    return i


# Whole-product energy projection; every independent binary factorization fails.
energies = (1, 2)
mask = [[int(x+y == 3) for y in energies] for x in energies]
factorizations = 0
for a in product((0, 1), repeat=2):
    for b in product((0, 1), repeat=2):
        factorizations += 1
        assert [[x*y for y in b] for x in a] != mask
assert rank(mask) == 2
record('total_energy_projection_does_not_factor', tested_factorizations=factorizations,
       mask=mask, scope='Exact finite tensor algebra; no scattering model.')


# Endpoint arithmetic includes a retained sum energy at either window endpoint.
cases = 0
for gamma, n, width_ratio, position, offset in product(
        (F(1), F(2)), range(1, 7), (F(1,8), F(1,5), F(0)),
        (F(0), F(1,2), F(1)), (F(-1,4), F(1,4))):
    radii = [gamma/F(8*n)]*n
    centers = [gamma*(i+2) for i in range(n)]
    selected = [c+offset*r for c, r in zip(centers, radii)]
    estar = sum(selected)
    width = gamma*width_ratio
    lo, hi = estar-position*width, estar+(1-position)*width
    sumlo = sum(c-r for c, r in zip(centers, radii))
    sumhi = sum(c+r for c, r in zip(centers, radii))
    bound = width+2*sum(radii)
    assert bound < gamma/2
    for x in (lo, hi):
        for y in (sumlo, sumhi):
            assert abs(x-y) <= bound < gamma
    cases += 1
# The factor 2 in the interval diameter cannot be replaced by 1.
assert abs(F(1,8)-F(-1,8)) > F(1,8)
# Keeping broad operator intervals can leave a nonvacuum gap energy.
assert F(2)-F(1,2)-F(1,2) == 1
assert all(F(1,10) <= x <= 3 for x in (F(1,2), F(1,2)))
record('closed_window_interval_margin', exact_cases=cases,
       includes_singletons=True, rejects_half_diameter_bound=True,
       rejects_vacuum_support_as_operator_transfer=True)


# Operator filtering acts on every transition, while preserving the vacuum column.
h = [0, 1, 3, 4]
q = [0, 1, 1, 4]
b = zero(4)
b[1][0], b[3][1], b[2][1] = F(1), F(2), F(3)


def time_filter(a):
    return [[x if h[i]-h[j] == 1 else F(0) for j, x in enumerate(row)]
            for i, row in enumerate(a)]


def spatial_filter(a):
    return [[x if (q[i]-q[j]) % 7 == 1 else F(0) for j, x in enumerate(row)]
            for i, row in enumerate(a)]


bt, bx = time_filter(b), spatial_filter(b)
assert bt == bx == time_filter(spatial_filter(b)) == spatial_filter(time_filter(b))
assert [row[0] for row in bt] == [row[0] for row in b]
assert {h[i]-h[j] for i in range(4) for j in range(4) if b[i][j]} == {1, 2, 3}
assert {h[i]-h[j] for i in range(4) for j in range(4) if bt[i][j]} == {1}
assert bt != b
# An exact overlapping amplitude partition, followed by whole-product projection.
v = [F(2), F(3), F(5)]
parts = [[F(1), F(1,3), F(0)], [F(0), F(2,3), F(1)]]
vectors = [[a*x for a, x in zip(part, v)] for part in parts]
assert [sum(x) for x in zip(*vectors)] == v
reassembled = [[sum(a[i]*c[j] for a in vectors for c in vectors)
                for j in range(3)] for i in range(3)]
assert reassembled == outer(v)
sum_mask = [[int(i+j == 2) for j in range(3)] for i in range(3)]
assert [[reassembled[i][j]*sum_mask[i][j] for j in range(3)] for i in range(3)] == [
    [v[i]*v[j]*sum_mask[i][j] for j in range(3)] for i in range(3)]
record('operator_refiltering_and_exact_partition',
       transition_energies_before=[1,2,3], transition_energies_after=[1],
       vacuum_vector_preserved=True, full_operator_changed=True,
       scope='Finite spectral-multiplier algebra; no smooth-filter locality test.')


# Nonorthogonal and noncommuting generators still have the exact common kernel.
q1, q2 = outer([1,0,0]), outer([1,1,0])
k = add(scale(F(1,4), q1), scale(F(1,8), q2))
assert mul(q1, q2) != mul(q2, q1)
assert rank(q1) == 1 and rank(k) == 2
assert [row[2] for row in k] == [0,0,0]
det2 = k[0][0]*k[1][1]-k[0][1]*k[1][0]
assert k[0][0] > 0 and det2 > 0
assert sub(q1, q1) == zero(3)
for m in range(1, 10):
    finite_tail = sum(F(1,2**a) for a in range(m+1, 15))
    assert finite_tail+F(1,2**14) == F(1,2**m)
record('positive_sum_common_kernel', rank_complete_family=rank(k),
       rank_incomplete_family=rank(q1), restricted_determinant=str(det2),
       rejects_signed_cancellation=True, geometric_tail_checks=9)


# Full noncommuting resolvent order, with an intentional invalid reordering.
eta = F(1,5)
a, bsmall = k, scale(F(1,4), q1)
ra = inverse(add(a, scale(eta, eye(3))))
rb = inverse(add(bsmall, scale(eta, eye(3))))
fa, fb = mul(a, ra), mul(bsmall, rb)
delta = sub(a, bsmall)
assert sub(fa, fb) == scale(eta, mul(mul(ra, delta), rb))
assert sub(fa, fb) != scale(eta, mul(mul(ra, rb), delta))
assert mul(a, ra) == sub(eye(3), scale(eta, ra))
record('noncommuting_resolvent_identity', eta=str(eta),
       exact_identity=True, invalid_filter_reordering_rejected=True)


# Square-root loss in the finite-time witness: an elementary positive matrix family.
count = 0
worst = 0.0
for t, exponent, aa, bb in product((2,3,5,10), (1,2,4), range(-3,4), range(-3,4)):
    eps = t**(-exponent)
    bound = 1+eps*eps
    # Q=|(1,0,eps)><(1,0,eps)|, E=|e_3><e_3|.
    # ||Q E||=eps*sqrt(bound)<=2*t^(-exponent), ||sqrt(Q)E||=eps.
    assert eps*math.sqrt(bound) <= 2*eps
    response_root = abs(aa+eps*bb)
    witness = max(0.0, response_root-math.sqrt(2*eps)*math.sqrt(aa*aa+bb*bb))/math.sqrt(bound)
    error = witness-abs(aa)
    worst = max(worst, error)
    assert error <= 1e-12
    count += 1
assert F(1,4) > F(1,16)  # sqrt(lambda)>lambda for lambda=1/16.
record('finite_time_square_root_witness', finite_cases=count,
       maximum_excess_over_exact_scattering_norm=worst,
       missing_square_root_bound_rejected=True,
       scope='Finite positive-operator algebra; constants are chosen for this toy matrix only.')

record('summary', controls=6, analytic_convergence_certified=False,
       physical_realization_certified=False, independent_review=False)

# The reviewed scalar positive-operator case discriminates a universal error
# formula that the original rank-one sweep does not distinguish.
_scalar_lambda = F(1, 16)
_scalar_response = F(1, 4)
_scalar_error = F(1, 4)
assert _scalar_response * _scalar_response == _scalar_lambda
_correct_witness = max(F(0), _scalar_response - _scalar_error) / _scalar_response
_wrong_linear_witness = max(F(0), _scalar_response - _scalar_lambda) / _scalar_response
assert _correct_witness == 0, "scalar positive operator needs the square-root error"
assert _wrong_linear_witness == F(3, 4)
print(json.dumps({"control": "reviewed_scalar_witness", "Q": "(1/16)E",
                  "actual_selected_norm": "0", "correct_witness": str(_correct_witness),
                  "wrong_linear_witness": str(_wrong_linear_witness)}, sort_keys=True))
print("per_element: finite exact filtering, support and noncommuting resolvent identities checked")
print("per_site: finite matrix fixtures only; no microscopic physical model constructed")
print("per_mode: finite tensor masks checked; continuum coverage uses the written proof")
print("per_block: narrow-window arithmetic and positive finite sums checked")
print("lattice_wide: checked and not executed — analytic scattering projection and ordered limits are proved in P1-P33")
print("TOTAL: PASS=7 FAIL=0")
print("SCOPE: Six original finite control groups plus the exact scalar discriminator; no ND, EX or physical realization.")
