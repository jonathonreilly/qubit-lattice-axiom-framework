#!/usr/bin/env python3
"""Independent controls for repeated six-axis formation, with no author imports."""
from fractions import Fraction as F
from itertools import product
from math import sqrt
from pathlib import Path
import json
import platform

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
V = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0),
              (0, -1, 0), (0, 0, 1), (0, 0, -1)], dtype=int)
I = np.eye(2, dtype=complex)
PAULI = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]
RHO = [(I+sum(v[i]*PAULI[i] for i in range(3)))/2 for v in V]


def kernel(j):
    return [[(1+j*int(V[a]@V[b]))/6 for b in range(6)] for a in range(6)]


def tv(p, q):
    return sum(abs(a-b) for a, b in zip(p, q))/2


def classical_pair_checks():
    result = []
    for j in [F(-9, 10), F(-1, 2), F(-1, 4), F(0), F(1, 4), F(1, 2), F(3, 4), F(9, 10)]:
        K = kernel(j)
        target = [[K[a][b]*K[a][c] for b, c in product(range(6), repeat=2)] for a in range(6)]
        mixtures = [[(target[2*i][k]+target[2*i+1][k])/2 for k in range(36)] for i in range(3)]
        for i, k in [(0, 1), (0, 2), (1, 2)]:
            assert tv(mixtures[i], mixtures[k]) == j*j/9
        ell = max(F(-1, 2), min(F(1, 2), j))
        approximation = [[(1+ell*int(V[a]@(V[b]+V[c])))/36
                          for b, c in product(range(6), repeat=2)] for a in range(6)]
        errors = [tv(target[a], approximation[a]) for a in range(6)]
        asserted = (j*j+4*max(abs(j)-F(1, 2), F(0)))/18
        assert all(value == asserted for value in errors)
        lower = j*j/18
        if abs(j) <= F(1, 2):
            assert asserted == lower
        effects = [(I+float(ell)*sum((V[b][i]+V[c][i])*PAULI[i] for i in range(3)))/36
                   for b, c in product(range(6), repeat=2)]
        assert np.max(abs(sum(effects)-I)) < 1e-13
        smallest = min(float(np.linalg.eigvalsh(effect).min()) for effect in effects)
        assert smallest > -1e-14
        for a, rho in enumerate(RHO):
            probabilities = [np.trace(effect@rho).real for effect in effects]
            assert max(abs(p-float(q)) for p, q in zip(probabilities, approximation[a])) < 1e-14
            first = [sum(approximation[a][6*b+c] for c in range(6)) for b in range(6)]
            second = [sum(approximation[a][6*b+c] for b in range(6)) for c in range(6)]
            assert first == second == kernel(ell)[a]
            # Copying one classical outcome preserves both target marginals,
            # but fails the product law even at j=0.
            duplicate = [K[a][b] if b == c else F(0) for b, c in product(range(6), repeat=2)]
            assert tv(target[a], duplicate) == 1-sum(p*p for p in K[a])
        result.append({'j': str(j), 'mixture_distance': str(j*j/9),
                       'universal_worst_row_TV_lower_bound': str(lower),
                       'approximation_ell': str(ell), 'actual_worst_row_TV': str(asserted),
                       'optimality_proved': abs(j) <= F(1, 2),
                       'matches_target_individual_marginals': ell == j,
                       'minimum_effect_eigenvalue': smallest})
    return result


def quantum_only_checks():
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    j = sp.Rational(1, 2)
    s = j/3
    mixture_x = (sp.eye(4)+s*s*sp.kronecker_product(sx, sx))/4
    mixture_y = (sp.eye(4)+s*s*sp.kronecker_product(sy, sy))/4
    difference = mixture_x-mixture_y
    assert difference != sp.zeros(4)
    spectrum = difference.eigenvals()
    assert spectrum == {sp.Rational(-1, 72): 1, sp.Rational(1, 72): 1, sp.Rational(0): 2}
    K = kernel(F(1, 2))
    correlated_outputs = []
    for a in range(6):
        joint = sum(float(K[a][b])*np.kron(RHO[b], RHO[b]) for b in range(6))
        target_marginal = (I+float(s)*sum(V[a][i]*PAULI[i] for i in range(3)))/2
        reshaped = joint.reshape(2, 2, 2, 2)
        assert np.max(abs(np.trace(reshaped, axis1=1, axis2=3)-target_marginal)) < 1e-13
        assert np.max(abs(np.trace(reshaped, axis1=0, axis2=2)-target_marginal)) < 1e-13
        correlated_outputs.append(joint)
    assert np.max(abs((correlated_outputs[0]+correlated_outputs[1])/2
                      -(correlated_outputs[2]+correlated_outputs[3])/2)) < 1e-13
    return {'j': '1/2', 'newborn_marginal_shrinkage': '1/6',
            'product_target_same_input_density_matrix_output_difference_eigenvalues':
                {'-1/72': 1, '0': 2, '1/72': 1},
            'correlated_two_newborn_channel_has_correct_marginals': True}


def encoded_instrument_checks():
    flags = [np.diag([int(k == i) for k in range(3)]).astype(complex) for i in range(3)]
    encoded = [np.kron(RHO[a], flags[a//2]) for a in range(6)]
    assert np.max(abs(sum(encoded)-np.eye(6))) < 1e-14
    gram = np.array([[np.trace(a@b).real for b in encoded] for a in encoded])
    assert np.max(abs(gram-np.eye(6))) < 1e-14
    total_history_checks = 0
    max_branch_error = 0.
    max_history_relative_error = 0.
    results = []
    for j in [F(-9, 10), F(1, 2), F(9, 10)]:
        K = kernel(j)
        M = [sum(sqrt(float(K[a][b]))*encoded[a] for a in range(6)) for b in range(6)]
        assert np.max(abs(sum(m.conj().T@m for m in M)-np.eye(6))) < 1e-13
        for a, state in enumerate(encoded):
            assert np.max(abs(np.trace(state.reshape(2, 3, 2, 3), axis1=1, axis2=3)-RHO[a])) < 1e-14
            for b, m in enumerate(M):
                error = float(np.max(abs(m@state@m.conj().T-float(K[a][b])*state)))
                max_branch_error = max(max_branch_error, error)
                assert error < 1e-13
            for history in product(range(6), repeat=3):
                actual = state.copy()
                expected_probability = F(1)
                for b in history:
                    actual = M[b]@actual@M[b].conj().T
                    expected_probability *= K[a][b]
                error = np.max(abs(actual-float(expected_probability)*state))/float(expected_probability)
                max_history_relative_error = max(max_history_relative_error, float(error))
                assert error < 1e-12
                total_history_checks += 1
        results.append({'j': str(j), 'joint_dimension': 6, 'ancillary_dimension': 3,
                        'all_216_length_three_histories_checked_for_each_input': True})
    # One-event resource control: supplied extra copy, parent untouched.
    K = kernel(F(1, 2))
    for a, b in product(range(6), repeat=2):
        effect = (I+.5*sum(V[b][i]*PAULI[i] for i in range(3)))/6
        eigenvalues, eigenvectors = np.linalg.eigh(effect)
        root = (eigenvectors*np.sqrt(eigenvalues))@eigenvectors.conj().T
        operator = np.kron(I, root)
        state = np.kron(RHO[a], RHO[a])
        output = operator@state@operator.conj().T
        parent = np.trace(output.reshape(2, 2, 2, 2), axis1=1, axis2=3)
        assert np.max(abs(parent-float(K[a][b])*RHO[a])) < 1e-13
    # Optional direct-sum vacuum dimension check, not a model premise.
    occupied7 = []
    for state in encoded:
        expanded = np.zeros((7, 7), complex)
        expanded[1:, 1:] = state
        occupied7.append(expanded)
    vacuum = np.diag([1]+[0]*6)
    assert np.max(abs(vacuum+sum(occupied7)-np.eye(7))) < 1e-14
    assert all(abs(np.trace(vacuum@state)) < 1e-14 for state in occupied7)
    return {'encoded_cases': results, 'history_checks': total_history_checks,
            'maximum_single_branch_residual': max_branch_error,
            'maximum_relative_history_residual': max_history_relative_error,
            'one_event_supplied_copy_ancilla_dimension': 2,
            'one_event_copy_checks': 36,
            'optional_orthogonal_vacuum_direct_sum_dimension': 7}


def information_checks():
    K = kernel(F(1, 2))
    for a in range(6):
        for coordinate in range(3):
            assert sum(K[a][b]*int(V[b][coordinate]) for b in range(6)) == F(1, 6)*int(V[a][coordinate])
    affinity = sum(sqrt(float(K[0][b]*K[2][b])) for b in range(6))
    assert abs(affinity-(sqrt(1.5)+sqrt(.5)+1)/3) < 1e-14
    assert 0 < affinity < 1
    horizons = []
    for name, distance in [('one_qubit', sqrt(.5)), ('parent_plus_supplied_copy', sqrt(.75))]:
        n = 1
        while 1-affinity**n <= distance:
            n += 1
        horizons.append({'resource': name, 'initial_cross_axis_trace_distance': distance,
                         'first_N_where_affinity_lower_bound_exceeds_it': n})
    return {'j': '1/2', 'cross_axis_single_mark_Bhattacharyya_affinity': affinity,
            'illustrative_loose_pairwise_history_bounds': horizons,
            'encoded_joint_state_orthogonality_checked_separately': True}


def main():
    result = {'classical_pairs': classical_pair_checks(),
              'quantum_only': quantum_only_checks(),
              'encoded_instrument': encoded_instrument_checks(),
              'information': information_checks(),
              'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'sympy': sp.__version__},
              'all_checks_passed': True}
    text = json.dumps(result, indent=2)+'\n'
    (HERE/'RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
