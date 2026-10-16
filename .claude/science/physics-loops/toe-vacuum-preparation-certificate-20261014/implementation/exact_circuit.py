#!/usr/bin/env python3
"""Independent bounded exact Boolean/Gaussian-rational circuit controls.

No candidate runner is imported. Bit q is (basis_index >> q) & 1.
All gate lists are chronological; matrices act on column vectors.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import sys

ZERO = (F(0), F(0))
ONE = (F(1), F(0))
IMAG = (F(0), F(1))


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def times(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def star(a):
    return a[0], -a[1]


def printable(a):
    return [str(a[0]), str(a[1])]


def eye(d):
    return [[ONE if i == j else ZERO for j in range(d)] for i in range(d)]


def multiply(a, b):
    result = [[ZERO for _ in b[0]] for _ in a]
    for i, row in enumerate(a):
        for k, value in enumerate(row):
            if value != ZERO:
                for j, other in enumerate(b[k]):
                    if other != ZERO:
                        result[i][j] = plus(result[i][j], times(value, other))
    return result


def adjoint(a):
    return [[star(a[j][i]) for j in range(len(a))] for i in range(len(a))]


def first_matrix_difference(actual, expected):
    for i in range(len(actual)):
        for j in range(len(actual)):
            if actual[i][j] != expected[i][j]:
                return {'row': i, 'column': j,
                        'actual': printable(actual[i][j]),
                        'expected': printable(expected[i][j])}
    return None


def boolean_gate(state, gate):
    kind, *w = gate
    if kind == 'x':
        return state ^ (1 << w[0])
    if kind == 'cx':
        return state ^ (((state >> w[0]) & 1) << w[1])
    if kind == 'ccx':
        return state ^ ((((state >> w[0]) & 1) * ((state >> w[1]) & 1)) << w[2])
    if kind == 'swap':
        return state ^ ((((state >> w[0]) ^ (state >> w[1])) & 1) * ((1 << w[0]) | (1 << w[1])))
    raise ValueError(gate)


def apply_boolean_word(state, word):
    for gate in word:
        assert len(gate[1:]) == len(set(gate[1:])), gate
        state = boolean_gate(state, gate)
    return state


def ladder_halves(controls, target, dirty):
    m = len(controls)
    assert m >= 3 and len(dirty) == m - 2
    assert len(set(controls + [target] + dirty)) == 2*m - 1
    gates = [('ccx', controls[0], controls[1], dirty[0])]
    for j in range(1, m - 2):
        gates.append(('ccx', controls[j + 1], dirty[j - 1], dirty[j]))
    gates.append(('ccx', controls[-1], dirty[-1], target))
    before = gates[:-1]
    shortened = gates[1:-1]
    return before + [gates[-1]] + before[::-1], shortened + [gates[-1]] + shortened[::-1]


def multi_word(controls, target, dirty):
    if len(controls) == 1:
        assert not dirty
        return [('cx', controls[0], target)]
    if len(controls) == 2:
        assert not dirty
        return [('ccx', controls[0], controls[1], target)]
    a, b = ladder_halves(controls, target, dirty)
    return a + b


def all_set(state, sites):
    return all((state >> q) & 1 for q in sites)


def verify_permutation(word, n_qubits, expected):
    seen = set()
    for state in range(1 << n_qubits):
        result = apply_boolean_word(state, word)
        assert result == expected(state), (state, result, expected(state))
        seen.add(result)
    assert len(seen) == 1 << n_qubits
    return len(seen)


def first_boolean_difference(word, n_qubits, expected):
    for state in range(1 << n_qubits):
        result = apply_boolean_word(state, word)
        if result != expected(state):
            return {'input': state, 'actual': result, 'expected': expected(state),
                    'input_bits_low_to_high': [(state >> q) & 1 for q in range(n_qubits)]}
    return None


def check_ladder(m):
    controls = list(range(m))
    target = m
    dirty = list(range(m + 1, 2*m - 1)) if m >= 3 else []
    n_qubits = 2*m - 1 if m >= 3 else m + 1
    expected = lambda s: s ^ (int(all_set(s, controls)) << target)
    word = multi_word(controls, target, dirty)
    result = {'kind': 'dirty_ladder', 'm': m, 'n_qubits': n_qubits,
              'basis_columns_exact': verify_permutation(word, n_qubits, expected),
              'chronological_word': word, 'gate_count': len(word)}
    assert len(word) == ({1: 1, 2: 1}.get(m, 4*(m - 2)))
    if m >= 3:
        a, b = ladder_halves(controls, target, dirty)
        def dirty_polynomial(s):
            parity = 0
            for j, site in enumerate(dirty):
                parity ^= ((s >> site) & 1) * int(all_set(s, controls[j + 2:]))
            return parity
        verify_permutation(a, n_qubits, lambda s: s ^ ((dirty_polynomial(s) ^ int(all_set(s, controls))) << target))
        verify_permutation(b, n_qubits, lambda s: s ^ (dirty_polynomial(s) << target))
        witness = first_boolean_difference(a, n_qubits, expected)
        assert witness is not None
        result['separate_A_B_dirty_polynomial_and_return'] = True
        result['omit_B_mutant_first_counterexample'] = witness
    return result


def composed_parts(n):
    a = 2 if n == 4 else (n + 2)//2
    s = list(range(a))
    t = list(range(a, n))
    c, f = n, n + 1
    # Intentionally borrow the pointer first in A whenever any dirty bit is used.
    da = ([f] + t)[:max(0, len(s) - 2)]
    db = s[:len(t) - 1]
    aw = multi_word(s, c, da)
    bw = multi_word(t + [c], f, db)
    return aw, bw, {'S': s, 'T': t, 'C': c, 'F': f, 'A_dirty': da, 'B_dirty': db}


def check_composed(n):
    a, b, sites = composed_parts(n)
    f = sites['F']
    expected_one = lambda s: s ^ (int(all_set(s, list(range(n)))) << f)
    word = a + b + a + b
    count = verify_permutation(word, n + 2, expected_one)
    assert len(word) == (10 if n == 4 else 8*(n - 3))
    xs = [('x', q) for q in range(n)]
    zero_word = xs + word + xs
    mask = (1 << n) - 1
    expected_zero = lambda s: s ^ (int((s & mask) == 0) << f)
    verify_permutation(zero_word, n + 2, expected_zero)
    wrong = first_boolean_difference(xs + a + b + a + xs, n + 2, expected_zero)
    assert wrong is not None
    return {'kind': 'composed_predicate', 'n': n, 'n_qubits': n + 2,
            'basis_columns_exact': count, 'all_C_and_F_values': True,
            'sites': sites, 'Toffoli_count': len(word), 'single_X_count': 2*n,
            'chronological_zero_word': zero_word,
            'omit_final_B_mutant_first_counterexample': wrong}


V = [[(F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2))],
     [(F(1, 2), F(-1, 2)), (F(1, 2), F(1, 2))]]
X = [[ZERO, ONE], [ONE, ZERO]]


def gate_matrix(n, gate, root=V):
    kind, *w = gate
    d = 1 << n
    result = [[ZERO for _ in range(d)] for _ in range(d)]
    if kind not in ('cv', 'cv_dagger'):
        for column in range(d):
            result[boolean_gate(column, gate)][column] = ONE
        return result
    control, target = w
    local = root if kind == 'cv' else adjoint(root)
    for column in range(d):
        if not ((column >> control) & 1):
            result[column][column] = ONE
        else:
            old_target = (column >> target) & 1
            for new_target in (0, 1):
                row = (column & ~(1 << target)) | (new_target << target)
                result[row][column] = local[new_target][old_target]
    return result


def word_matrix(n, word, root=V):
    result = eye(1 << n)
    for gate in word:
        result = multiply(gate_matrix(n, gate, root), result)
    return result


def exact_norm_square(z):
    return z[0]*z[0] + z[1]*z[1]


def check_five_gate():
    assert multiply(V, V) == X
    assert multiply(adjoint(V), V) == eye(2)
    word = [('cv', 1, 2), ('cx', 0, 1), ('cv_dagger', 1, 2), ('cx', 0, 1), ('cv', 0, 2)]
    actual = word_matrix(3, word)
    expected = [[ZERO for _ in range(8)] for _ in range(8)]
    for column in range(8):
        row = column ^ (4 if (column & 3) == 3 else 0)
        expected[row][column] = ONE
    assert actual == expected
    # W=iV still induces the same basis permutation in the five-gate word,
    # but W^2=-X produces a controlled relative phase. Probability-only checks miss it.
    wrong_root = [[times(IMAG, value) for value in row] for row in V]
    wrong = word_matrix(3, word, wrong_root)
    diff = first_matrix_difference(wrong, expected)
    assert diff is not None
    assert all(exact_norm_square(wrong[i][j]) == exact_norm_square(expected[i][j]) for i in range(8) for j in range(8))
    return {'kind': 'five_two_qubit_Toffoli', 'dimension': 8,
            'entries_exact': 64, 'chronological_word': word,
            'V_squared_exactly_X': True, 'matrix_exact_not_up_to_phase': True,
            'iV_phase_only_mutant_preserves_basis_probabilities': True,
            'iV_phase_only_mutant_first_matrix_difference': diff}


def tensor_operator(site_operators):
    n = len(site_operators)
    d = 1 << n
    out = [[ZERO for _ in range(d)] for _ in range(d)]
    for row in range(d):
        for column in range(d):
            value = ONE
            for q, op in enumerate(site_operators):
                value = times(value, op[(row >> q) & 1][(column >> q) & 1])
            out[row][column] = value
    return out


def check_route(length):
    n = length + 1
    swaps = [('swap', q, q + 1) for q in range(length - 1)]
    word = swaps + [('cv', length - 1, length)] + swaps[::-1]
    assert len(word) == 2*length - 1
    p0 = [[ONE, ZERO], [ZERO, ZERO]]
    p1 = [[ZERO, ZERO], [ZERO, ONE]]
    first = tensor_operator([p0] + [eye(2)]*(n - 1))
    second = tensor_operator([p1] + [eye(2)]*(n - 2) + [V])
    expected = [[plus(first[i][j], second[i][j]) for j in range(1 << n)] for i in range(1 << n)]
    actual = word_matrix(n, word)
    assert actual == expected
    reversed_word = swaps + [('cv', length, length - 1)] + swaps[::-1]
    reversed_difference = first_matrix_difference(word_matrix(n, reversed_word), expected)
    no_return_difference = first_matrix_difference(word_matrix(n, swaps + [('cv', length - 1, length)]), expected)
    assert reversed_difference is not None and no_return_difference is not None
    return {'kind': 'generic_endpoint_route', 'path_edge_length': length,
            'dimension': 1 << n, 'entries_exact': (1 << n)**2,
            'chronological_word': word, 'intermediate_identity_exact': True,
            'reversed_operand_mutant_first_matrix_difference': reversed_difference,
            'omitted_return_mutant_first_matrix_difference': no_return_difference,
            'concrete_physical_layout_checked': False}


def main():
    supplied = json.loads(Path(sys.argv[1]).read_text())
    rows = [check_ladder(m) for m in supplied['dirty_ladder_control_counts']]
    rows += [check_composed(n) for n in supplied['composed_predicate_control_counts']]
    rows += [check_five_gate(), check_route(supplied['routing_path_edges'])]
    for row in rows:
        print(json.dumps(row, sort_keys=True), flush=True)
    print(json.dumps({'completed': True, 'row_count': len(rows),
                      'arithmetic': 'exact Boolean permutations and pairs of fractions.Fraction',
                      'all_m_proof_is_not_a_finite_test': True,
                      'candidate_programs_imported_or_executed': False}, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
