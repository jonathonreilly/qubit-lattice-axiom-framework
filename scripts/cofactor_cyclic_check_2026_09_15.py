"""Finite author check of assigned-cofactor cyclic realizations.

The direct comparator enumerates determinant permutations; the alternative
uses local signs and normalized CAR words. Generic matrices test the source
lemma, not physical lattice all-order convergence. CAR builder is shared.
"""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'scripts/determinant_exclusion_check_2026_09_15.py']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'signed_forest_fixed_order_remainders_and_restricted_loop_sums_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/cofactor_cyclic_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
import itertools
import json
from pathlib import Path
import numpy as np
from determinant_exclusion_check_2026_09_15 import creators


def parity(items):
    return (-1)**sum(items[i] > items[j] for i in range(len(items)) for j in range(i+1, len(items)))


def direct_resource(s, members, edges):
    if any(i not in members or j not in members for i, j in edges):
        return 0.
    rows, columns = [i for i, j in edges], [j for i, j in edges]
    if len(set(rows)) != len(rows) or len(set(columns)) != len(columns):
        return 0.
    required = dict(edges)
    value = 0.
    for perm in itertools.permutations(members):
        mapping = dict(zip(members, perm))
        if any(mapping[i] != j for i, j in edges):
            continue
        term = float(parity(perm))
        for i in members:
            if i not in required:
                term *= s[i, mapping[i]]
        value += term
    return value


def operator_resource(c, members, edges, order, omit_local_sign=False):
    if any(i not in members or j not in members for i, j in edges):
        return 0.
    rows, columns = [i for i, j in edges], [j for i, j in edges]
    if len(set(rows)) != len(rows) or len(set(columns)) != len(columns):
        return 0.
    position = {i: k for k, i in enumerate(order)}
    row_order = sorted(rows, key=position.get)
    column_order = sorted(columns, key=position.get)
    mapping = dict(edges)
    sign = parity([column_order.index(mapping[i]) for i in row_order])
    local_phase = 1
    for v in members:
        h = sum(position[r] >= position[v] for r in rows)+sum(position[r] >= position[v] for r in columns)
        local_phase *= (-1)**h
    if not omit_local_sign:
        sign *= local_phase
    matrix = np.eye(c.shape[1])
    for i in reversed(order):
        if i not in members:
            continue
        if i not in rows:
            matrix = c[i].T@matrix
        if i not in columns:
            matrix = matrix@c[i]
    return sign*np.trace(matrix)/c.shape[1]*2.**(len(members)-len(edges))


def compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, n-1):
                yield (first,)+rest


def main():
    rng = np.random.default_rng(515720)
    n = 4
    v = rng.normal(size=(n, n)); v /= np.linalg.norm(v, axis=0)
    s = v.T@v
    c = np.einsum('ki,kab->iab', v, creators(n))
    orders = list(itertools.permutations(range(n)))
    assignments = [[], [(0, 2)], [(0, 1), (1, 2)],
                   [(0, 1), (1, 2), (2, 0)], [(0, 1), (0, 2)]]
    maximum_error = wrong_sign_gap = 0.
    identity_cases = 0
    for bits in itertools.product([0, 1], repeat=n):
        members = [i for i, bit in enumerate(bits) if bit]
        for edges in assignments:
            direct = direct_resource(s, members, edges)
            for order in orders:
                value = operator_resource(c, members, edges, order)
                maximum_error = max(maximum_error, abs(value-direct))
                wrong_sign_gap = max(wrong_sign_gap, abs(operator_resource(c, members, edges, order, True)-direct))
                identity_cases += 1
    assert maximum_error < 3e-13
    assert wrong_sign_gap > .1

    footprints = [set(), {0}, {1}, {0, 1}]
    configurations = list(itertools.product(range(len(footprints)), repeat=n))
    phase = np.exp(1j*rng.normal(size=(n, len(footprints))))
    source = np.array([0., -.7, .3+.1j, 1.4-.2j])
    matrix = rng.normal(size=(len(footprints), len(footprints)))
    j = (matrix+matrix.T)/20
    rho = np.linalg.norm(j, 2)
    s4 = np.trace(np.diag(abs(source)**4)@j@j)
    loop_assignments = [{0:[(0, 2)]}, {0:[(0, 2)],1:[(1, 3)]},
                        {0:[(0, 1),(1, 2)]}, {0:[(0, 1),(1, 2),(2, 0)]}]
    source_checks = []
    for assigned in loop_assignments:
        k = sum(map(len, assigned.values()))
        coefficients = []
        rotated = [[] for _ in range(n)]
        for conf in configurations:
            selected = [footprints[a] for a in conf]
            boost = 2**sum(map(len, selected))
            direct = 1.
            for resource in [0, 1]:
                members = [i for i, a in enumerate(selected) if resource in a]
                direct *= direct_resource(s, members, assigned.get(resource, []))
            scalar = np.prod([j[conf[i], conf[(i+1)%n]]*phase[i, conf[i]] for i in range(n)])/boost
            coefficients.append(scalar*direct)
            for first in range(n):
                order = list(range(first, n))+list(range(first))
                value = 1.
                for resource in [0, 1]:
                    members = [i for i, a in enumerate(selected) if resource in a]
                    value *= operator_resource(c, members, assigned.get(resource, []), order)
                rotated[first].append(scalar*value)
        coefficients = np.array(coefficients)
        rotated = np.array(rotated)
        rotation_error = float(np.max(abs(rotated-coefficients[None, :])))
        assert rotation_error < 2e-13
        bound = 2.**(-k)*rho**(n-2)*s4
        values = []
        for powers in compositions(4, n):
            marks = np.prod(source[np.array(configurations)]**np.array(powers)[None, :], axis=1)
            value = coefficients@marks
            values.append(abs(value))
            assert abs(value) <= bound+1e-13
        source_checks.append(dict(assigned_entries=k, source_distributions=len(values),
                                  maximum_absolute_value=float(max(values)), bound=float(bound),
                                  maximum_ratio=float(max(values)/bound), rotation_error=rotation_error))

    x = rng.normal(size=(2**n, 2**n))
    # L_0(X)=C_0* X; Q_1(X)=C_1* X C_1. These anticommute.
    noncommuting_gap = float(np.linalg.norm(c[0].T@c[1].T@x@c[1]-c[1].T@c[0].T@x@c[1]))
    assert noncommuting_gap > 1
    result = dict(status='finite_author_checks_passed', independent_review=False,
                  cofactor_order_cases=identity_cases, maximum_identity_error=float(maximum_error),
                  omitted_local_sign_failure=float(wrong_sign_gap),
                  false_one_sided_commutation_gap=noncommuting_gap,
                  source_checks=source_checks,
                  limitations=['fixed oriented resource assignments only',
                               'generic finite matrices rather than physical lattice law',
                               'shared CAR construction',
                               'no sum over lattice resource assignments or branching graphs'])
    _OUTPUT_JSON.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: finite cochain, signed phase, partition and derivative fixtures')
    print('per_site: finite source-support configurations only')
    print('per_mode: finite matrix/operator directions; no all-order or infinite-kernel execution')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
