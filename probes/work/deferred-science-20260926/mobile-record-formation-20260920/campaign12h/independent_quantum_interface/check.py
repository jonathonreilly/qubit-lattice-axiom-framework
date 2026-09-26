#!/usr/bin/env python3
"""Independent checks from the supplied six-state interface specification.

No primary campaign source is read or imported. Exact algebra supports the
proof; floating LP/certificate checks are separately labeled and bounded.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import platform

import numpy as np
import scipy
from scipy.optimize import linprog
import sympy as sp

HERE = Path(__file__).resolve().parent
V = np.array([(1, 0, 0), (-1, 0, 0), (0, 1, 0),
              (0, -1, 0), (0, 0, 1), (0, 0, -1)], dtype=int)
I = np.eye(2, dtype=complex)
SIGMA = [np.array([[0, 1], [1, 0]], complex),
         np.array([[0, -1j], [1j, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]
RHO = [(I+sum(v[i]*SIGMA[i] for i in range(3)))/2 for v in V]
OMEGA = np.array([1, 0, 0, 1], complex)
OMEGA_PROJECTOR = np.outer(OMEGA, OMEGA.conj())


def raw_weight(a, b, p, q, r):
    return p if a == b else q if (a ^ 1) == b else r


def kernel(p, q, r):
    D = p+q+4*r
    return [[F(raw_weight(a, b, p, q, r), D) for b in range(6)] for a in range(6)]


def relaxed_measurement_lp(K):
    # Hermitian effects with sum E_b=I, with PSD deliberately relaxed.
    # This is a global numerical LOWER bound, paired with an explicit PSD
    # construction in the exact checks below; it is not mislabeled as an SDP.
    # E_b=(t_b I+r_b.sigma)/2, Q_ab=(t_b+r_b.v_a)/2.
    unknowns = 61  # 24 effect parameters, 36 absolute slacks, worst-row TV
    Aeq = np.zeros((4, unknowns))
    for b in range(6):
        for j in range(4):
            Aeq[j, 4*b+j] = 1
    beq = np.array([2, 0, 0, 0.])
    Aub, bub = [], []
    for a, b in product(range(6), repeat=2):
        probability = np.zeros(unknowns)
        probability[4*b] = .5
        probability[4*b+1:4*b+4] = V[a]/2
        for sign in [1, -1]:
            row = sign*probability
            row[24+6*a+b] = -1
            Aub.append(row)
            bub.append(sign*float(K[a][b]))
    for a in range(6):
        row = np.zeros(unknowns)
        row[24+6*a:24+6*a+6] = 1
        row[-1] = -2
        Aub.append(row)
        bub.append(0.)
    objective = np.zeros(unknowns)
    objective[-1] = 1
    answer = linprog(objective, A_ub=np.array(Aub), b_ub=np.array(bub),
                     A_eq=Aeq, b_eq=beq,
                     bounds=[(None, None)]*24+[(0, None)]*37,
                     method='highs')
    assert answer.success, answer.message
    return float(answer.fun)


def measurement_checks():
    menus = [(1, 1, 1), (3, 1, 2), (1, 3, 2), (2, 2, 1),
             (10, 1, 1), (1, 10, 1), (2, 7, 3), (11, 4, 2),
             (9, 2, 8), (4, 9, 1), (2, 2, 7), (5, 3, 4), (1, 4, 1)]
    out = []
    for p, q, r in menus:
        D, P = p+q+4*r, p+q
        K = kernel(p, q, r)
        eta = F(p-q, P)
        Q = [[(1+eta*int(V[a]@V[b]))/6 for b in range(6)] for a in range(6)]
        error = max(sum(abs(K[a][b]-Q[a][b]) for b in range(6))/2 for a in range(6))
        predicted = abs(F(P, D)-F(1, 3))
        assert error == predicted
        assert all((1-abs(eta))/6 > 0 for _ in [0])
        assert all(sum(row) == 1 for row in Q)
        # A fixed effect must have the same antipodal input-pair sum on all axes.
        consistent = all(K[0][b]+K[1][b] == K[2][b]+K[3][b] == K[4][b]+K[5][b]
                         for b in range(6))
        assert consistent == (P == 2*r) == (error == 0)
        lower = relaxed_measurement_lp(K)
        assert abs(lower-float(predicted)) < 1e-9
        out.append({'pqr': [p, q, r], 'exact_POVM': consistent,
                    'exact_optimal_worst_row_TV': str(predicted),
                    'attaining_eta': str(eta), 'PSD_relaxed_LP_lower_bound': lower})
    return out


def hermitian_power(matrix, power):
    values, vectors = np.linalg.eigh(matrix)
    assert values.min() > 0
    return (vectors*(values**power))@vectors.conj().T


def fidelity_checks():
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    exact_states = [(sp.eye(2)+sum((int(v[i])*s for i, s in enumerate([sx, sy, sz])), sp.zeros(2)))/2
                    for v in V]
    moment = sum((sp.kronecker_product(rho.T, rho) for rho in exact_states), sp.zeros(4))/6
    omega = sp.Matrix([1, 0, 0, 1])
    assert moment == (sp.eye(4)+omega*omega.T)/6
    rng = np.random.default_rng(20260921)
    result = []
    for eta in [-.9, -.5, 0., .5, .9]:
        effects = [(I+eta*sum(v[i]*SIGMA[i] for i in range(3)))/6 for v in V]
        roots = [hermitian_power(effect, .5) for effect in effects]
        assert np.max(abs(sum(effects)-I)) < 1e-13
        upper = (2+np.sqrt(1-eta*eta))/3
        luders = sum(np.trace(rho@root@rho@root.conj().T).real
                     for rho in RHO for root in roots)/6
        assert abs(luders-upper) < 1e-13
        # Independent numerical SDP-dual certificate for each outcome:
        # Y tensor I >= |Omega><Omega| and Tr(Y E^T)=(Tr sqrt E)^2.
        minimum_dual_eigenvalue = 1.
        dual_cost = 0.
        for effect, root in zip(effects, roots):
            Y = np.trace(root).real*np.linalg.inv(root.T)
            gap = np.kron(Y, I)-OMEGA_PROJECTOR
            eigmin = float(np.linalg.eigvalsh(gap).min())
            minimum_dual_eigenvalue = min(minimum_dual_eigenvalue, eigmin)
            assert eigmin > -1e-12
            dual_cost += np.trace(Y@effect.T).real
        assert abs((2+dual_cost)/6-upper) < 1e-13
        largest_random = 0.
        maximum_effect_error = 0.
        for trial in range(12):
            all_kraus = []
            for effect, root in zip(effects, roots):
                A = [rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)) for _ in range(3)]
                normalizer = hermitian_power(sum(a.conj().T@a for a in A), -.5)
                K = [a@normalizer@root for a in A]
                effect_error = np.max(abs(sum(k.conj().T@k for k in K)-effect))
                maximum_effect_error = max(maximum_effect_error, float(effect_error))
                assert effect_error < 1e-12
                all_kraus.extend(K)
            actual = sum(np.trace(rho@k@rho@k.conj().T).real for rho in RHO for k in all_kraus)/6
            design_formula = (2+sum(abs(np.trace(k))**2 for k in all_kraus))/6
            assert abs(actual-design_formula) < 1e-12
            assert actual <= upper+1e-12
            largest_random = max(largest_random, actual)
        result.append({'eta': eta, 'optimal_average_overlap_fidelity': upper,
                       'Luders_value': luders, 'minimum_dual_certificate_eigenvalue': minimum_dual_eigenvalue,
                       'random_instruments': 12, 'largest_random_instrument_fidelity': largest_random,
                       'maximum_effect_error': maximum_effect_error})
    return {'exact_six_state_second_moment_identity': True, 'cases': result}


def marginal_and_two_parent_checks():
    records = []
    for p, q, r in [(1, 1, 1), (3, 1, 2), (1, 3, 2), (2, 2, 1),
                    (10, 1, 1), (1, 10, 1), (1, 4, 1)]:
        D = p+q+4*r
        K = kernel(p, q, r)
        delta = F(p-q, D)
        choi = float(delta)*OMEGA_PROJECTOR+(1-float(delta))*np.eye(4)/2
        cp = delta >= F(-1, 3) and delta <= 1
        assert (np.linalg.eigvalsh(choi).min() >= -1e-12) == cp
        for a in range(6):
            marginal = sum(float(K[a][b])*RHO[b] for b in range(6))
            expected = float(delta)*RHO[a]+(1-float(delta))*I/2
            assert np.max(abs(marginal-expected)) < 1e-13
        W = [[6*K[a][b] for a in range(6)] for b in range(6)]
        x, y = F(3*(p-q), D), F(3*(p+q-2*r), D)
        intensity = [[sum(W[b][a]*W[b][c] for b in range(6)) for c in range(6)] for a in range(6)]
        for a, c in product(range(6), repeat=2):
            dot = int(V[a]@V[c])
            assert intensity[a][c] == 6+2*x*x*dot+2*y*y*(dot*dot-F(1, 3))
        # Other parent fixed to +x: two decompositions of I/2 must agree.
        same_axis_mixture = (intensity[0][0]+intensity[1][0])/2
        other_axis_mixture = (intensity[2][0]+intensity[3][0])/2
        assert same_axis_mixture-other_axis_mixture == 2*y*y
        record = {'pqr': [p, q, r], 'newborn_shrinkage': str(delta),
                  'newborn_marginal_CP': cp,
                  'two_parent_same_density_matrix_rate_difference_per_epsilon': str(2*y*y)}
        if y == 0:
            Ftotal = 6*np.eye(4)+2*float(x*x)*sum(np.kron(s, s) for s in SIGMA)
            Fsum = sum(np.kron(I+float(x)*sum(v[i]*SIGMA[i] for i in range(3)),
                               I+float(x)*sum(v[i]*SIGMA[i] for i in range(3))) for v in V)
            assert np.max(abs(Ftotal-Fsum)) < 1e-13
            eig = np.linalg.eigvalsh(Ftotal)
            expected_eig = sorted([float(6-6*x*x)]+[float(6+2*x*x)]*3)
            assert np.max(abs(eig-expected_eig)) < 1e-12
            assert eig.min() > 0
            record['two_parent_rate_operator_spectrum_per_epsilon'] = expected_eig
        records.append(record)
    return records


def product_odds_constraints(n, p, q, r):
    inputs = list(product(range(6), repeat=n))
    index = {a: i for i, a in enumerate(inputs)}
    def weight(b, a):
        result = 1
        for value in a:
            result *= raw_weight(b, value, p, q, r)
        return result
    rows = []
    for coordinate in range(n):
        for other in product(range(6), repeat=n-1):
            for b in range(6):
                for compared_axis in [1, 2]:
                    row = [0]*len(inputs)
                    for axis, sign in [(0, 1), (compared_axis, -1)]:
                        for orientation in [0, 1]:
                            a = list(other)
                            a.insert(coordinate, 2*axis+orientation)
                            a = tuple(a)
                            row[index[a]] += sign*weight(b, a)
                    rows.append(row)
    return inputs, sp.Matrix(rows)


def postselection_checks():
    out = []
    for n in [1, 2]:
        for p, q, r in [(3, 1, 2), (1, 1, 1), (3, 1, 1), (2, 2, 1)]:
            inputs, matrix = product_odds_constraints(n, p, q, r)
            nullity = len(inputs)-matrix.rank()
            valid = p+q == 2*r
            expected = 1 if valid and p != q else 4**n if valid else 0 if p != q else 3**n
            assert nullity == expected
            A = np.array(matrix.tolist(), float)
            eq = np.vstack([A, np.ones((1, len(inputs)))])
            rhs = np.r_[np.zeros(A.shape[0]), 1.]
            feasible = linprog(np.zeros(len(inputs)), A_eq=eq, b_eq=rhs,
                               bounds=[(0, None)]*len(inputs), method='highs')
            assert feasible.success == valid
            if not valid:
                assert feasible.status == 2  # certified infeasible by HiGHS
            elif p != q:
                assert matrix*sp.ones(len(inputs), 1) == sp.zeros(matrix.rows, 1)
                assert np.max(abs(feasible.x-1/len(inputs))) < 1e-10
            out.append({'parents': n, 'pqr': [p, q, r],
                        'exact_linearity_nullity_for_h': nullity,
                        'nonnegative_nonzero_h_feasible_LP': bool(feasible.success)})
    # Positive three-parent construction, checked against all 216 preparations.
    eta = F(1, 2)
    effects = []
    for b in range(6):
        A = I+float(eta)*sum(V[b][i]*SIGMA[i] for i in range(3))
        effects.append(np.kron(np.kron(A, A), A))
    for effect in effects:
        assert np.linalg.eigvalsh(effect).min() > 0
    for a in product(range(6), repeat=3):
        state = np.kron(np.kron(RHO[a[0]], RHO[a[1]]), RHO[a[2]])
        for b, effect in enumerate(effects):
            target = F(1)
            for parent in a:
                target *= 1+eta*int(V[b]@V[parent])
            assert abs(np.trace(effect@state).real-float(target)) < 1e-12
    return {'one_and_two_parent_linearity_tests': out,
            'three_parent_positive_effect_preparations': 216,
            'three_parent_individual_outcome_rates_checked': 1296}


def main():
    result = {'measurement': measurement_checks(),
              'parent_fidelity': fidelity_checks(),
              'marginal_and_two_parent_rate': marginal_and_two_parent_checks(),
              'postselection': postselection_checks(),
              'arithmetic': 'Exact fractions/SymPy identities; floating HiGHS LPs and matrix certificates at declared tolerances.',
              'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                           'scipy': scipy.__version__, 'sympy': sp.__version__},
              'all_checks_passed': True}
    text = json.dumps(result, indent=2)+'\n'
    (HERE/'RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
