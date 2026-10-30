#!/usr/bin/env python3
"""Independent finite exact algebra, not an analytic or numerical physics proof.

All 64 retained-coordinate masks of one rational six-coordinate model are
checked.  The cover has a collar on both patches and a nontrivial rational
partition of squares.  Gaussian elimination is the comparison route.
"""

from fractions import Fraction as F
from itertools import product
import json


def zeros(n, m=None):
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mul(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def inv(a):
    n = len(a)
    rows = [list(a[i]) + eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if rows[k][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        p = rows[j][j]
        rows[j] = [x / p for x in rows[j]]
        for i in range(n):
            if i != j:
                c = rows[i][j]
                rows[i] = [x - c * y for x, y in zip(rows[i], rows[j])]
    return [r[n:] for r in rows]


def principal(a, ids):
    return [[a[i][j] for j in ids] for i in ids]


def diag(ds):
    return [[x if i == j else F(0) for j in range(len(ds))]
            for i, x in enumerate(ds)]


def patch_inverse(k, ids, patch):
    local = [i for i, owner in enumerate(ids) if owner in patch]
    result = zeros(len(ids))
    small = inv(principal(k, local))
    for i, row in enumerate(local):
        for j, col in enumerate(local):
            result[row][col] = small[i][j]
    return result


def check():
    n = 6
    ambient = [[F(4 + i) if i == j else F(-1 if abs(i-j) == 1 else 0)
                for j in range(n)] for i in range(n)]
    cutoffs = [list(map(F, [1, 1, F(3, 5), 0, 0, 0])),
               list(map(F, [0, 0, F(4, 5), 1, 1, 1]))]
    patches = [set(range(4)), set(range(1, 6))]
    assert all(sum(c[i] ** 2 for c in cutoffs) == 1 for i in range(n))
    assert all(all(abs(i-j) > 1 or j in a
                   for i, ci in enumerate(c) if ci
                   for j in range(n)) for c, a in zip(cutoffs, patches))

    checked = sign_caught = order_caught = compression_caught = 0
    ambient_inverse = inv(ambient)
    for mask in product([False, True], repeat=n):
        ids = [i for i in range(n) if mask[i]]
        k = principal(ambient, ids)
        identity = eye(len(ids))
        p, residual = zeros(len(ids)), zeros(len(ids))
        for c, patch in zip(cutoffs, patches):
            chi = diag([c[i] for i in ids])
            local_inverse = patch_inverse(k, ids, patch)
            core_piece = mul(mul(chi, local_inverse), chi)
            commutator = add(mul(k, chi), mul(chi, k), -1)
            residual_piece = mul(mul(commutator, local_inverse), chi)
            p = add(p, core_piece)
            residual = add(residual, residual_piece, -1)
        assert mul(k, p) == add(identity, residual, -1)
        direct_inverse = inv(k)
        assert mul(p, inv(add(identity, residual, -1))) == direct_inverse
        sign_caught += mul(k, p) != add(identity, residual)
        compression_caught += direct_inverse != principal(ambient_inverse, ids)

        perturbation = diag([F(i+1, 200) for i in ids])
        critical_direct = inv(add(k, perturbation))
        right_factor = inv(add(identity, mul(perturbation, direct_inverse)))
        assert mul(direct_inverse, right_factor) == critical_direct
        order_caught += mul(right_factor, direct_inverse) != critical_direct
        checked += 1

    assert checked == 64
    assert sign_caught > 0 and order_caught > 0 and compression_caught > 0
    return {
        "scope": "finite exact rational algebra only; not the uniform analytic theorem",
        "retained_masks_checked": checked,
        "includes_empty_and_full_masks": True,
        "boundary_commutator_and_ordered_lift_inverse": "PASS",
        "ordered_critical_inverse": "PASS",
        "wrong_commutator_sign_detected_on_masks": sign_caught,
        "wrong_critical_inverse_order_detected_on_masks": order_caught,
        "ambient_inverse_compression_mismatch_on_masks": compression_caught,
    }


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
