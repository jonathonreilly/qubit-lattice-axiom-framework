#!/usr/bin/env python3
"""Independent two-parent waiting-law checks; no primary-author imports."""
from itertools import combinations, product
from pathlib import Path
import json
import math
import platform

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
I2 = sp.eye(2)
I4 = sp.eye(4)
SIGMA = [sp.Matrix([[0, 1], [1, 0]]),
         sp.Matrix([[0, -sp.I], [sp.I, 0]]),
         sp.Matrix([[1, 0], [0, -1]])]
V = [sp.Matrix(v) for v in [(1, 0, 0), (-1, 0, 0),
                            (0, 1, 0), (0, -1, 0),
                            (0, 0, 1), (0, 0, -1)]]


def bloch(v):
    return sum((v[i]*SIGMA[i] for i in range(3)), sp.zeros(2))


RHO = [(I2+bloch(v))/2 for v in V]
T = sum((sp.kronecker_product(s, s) for s in SIGMA), sp.zeros(4))
PS = (I4-T)/4
PT = I4-PS


def exact_checks():
    j = sp.Symbol('j', real=True)
    eps = sp.Symbol('epsilon', positive=True)
    t = sp.Symbol('t', nonnegative=True)
    F = [eps*sp.kronecker_product(I2+j*bloch(v), I2+j*bloch(v)) for v in V]
    R = sum(F, sp.zeros(4))
    assert sp.simplify(R-eps*(6*I4+2*j*j*T)) == sp.zeros(4)
    assert PS*PS == PS and PT*PT == PT and PS*PT == sp.zeros(4)
    assert sp.trace(PS) == 1 and sp.trace(PT) == 3
    rt, rs = eps*(6+2*j*j), eps*(6-6*j*j)
    assert sp.simplify(R*PT-rt*PT) == sp.zeros(4)
    assert sp.simplify(R*PS-rs*PS) == sp.zeros(4)
    rates, marks, mixture_weights, quadratic_checks = 0, 0, 0, 0
    for a, c in product(range(6), repeat=2):
        state = sp.kronecker_product(RHO[a], RHO[c])
        u = (V[a].T*V[c])[0]
        classical_rate = eps*sum((1+j*(v.T*V[a])[0])*(1+j*(v.T*V[c])[0]) for v in V)
        assert sp.simplify(classical_rate-eps*(6+2*j*j*u)) == 0
        assert sp.simplify(sp.trace(R*state)-classical_rate) == 0
        rates += 1
        for b in range(6):
            expected = eps*(1+j*(V[b].T*V[a])[0])*(1+j*(V[b].T*V[c])[0])
            assert sp.simplify(sp.trace(F[b]*state)-expected) == 0
            marks += 1
        assert sp.trace(PS*state) == (1-u)/4
        assert sp.trace(PT*state) == (3+u)/4
        mixture_weights += 1
        variance = sp.trace(R*R*state)-classical_rate**2
        assert sp.simplify(variance-4*eps**2*j**4*(1-u)*(3+u)) == 0
        quadratic_checks += 1
    # Same physical mixed input, two different target waiting probabilities.
    c = 4  # +z
    parallel_mixture = (sp.kronecker_product(RHO[4], RHO[c])
                        + sp.kronecker_product(RHO[5], RHO[c]))/2
    perpendicular_mixture = (sp.kronecker_product(RHO[0], RHO[c])
                             + sp.kronecker_product(RHO[1], RHO[c]))/2
    assert parallel_mixture == perpendicular_mixture == sp.kronecker_product(I2/2, RHO[c])
    # Direct matrix exponential, not just a constructed spectral expression.
    j0, eps0, t0 = sp.Rational(1, 2), sp.Integer(1), sp.Rational(1, 6)
    R0 = R.subs({j: j0, eps: eps0})
    E0 = (-t0*R0).exp()
    spectral = PT*sp.exp(-t0*rt.subs({j: j0, eps: eps0}))+PS*sp.exp(-t0*rs.subs({j: j0, eps: eps0}))
    assert sp.simplify(E0-spectral) == sp.zeros(4)
    K0 = (-t0*R0/2).exp()
    assert sp.simplify(K0.conjugate().T*K0-E0) == sp.zeros(4)
    for a, c in product(range(6), repeat=2):
        state = sp.kronecker_product(RHO[a], RHO[c])
        u = (V[a].T*V[c])[0]
        direct = sp.trace(K0*state*K0.conjugate().T)
        predicted = (3+u)*sp.exp(-sp.Rational(13, 12))/4+(1-u)*sp.exp(-sp.Rational(3, 4))/4
        assert sp.simplify(direct-predicted) == 0
    return {'symbolic_total_rate_checks': rates, 'symbolic_marked_rate_checks': marks,
            'symbolic_singlet_triplet_weight_checks': mixture_weights,
            'symbolic_second_order_gap_checks': quadratic_checks,
            'identical_mixed_input_checked_exactly': True,
            'direct_matrix_exponential': {'j': '1/2', 'epsilon': '1', 'time': '1/6',
                                          'all_36_input_survivals_checked': True},
            'total_rate_eigenvalues': {'triplet': 'epsilon*(6+2*j^2)',
                                      'singlet': 'epsilon*(6-6*j^2)'}}


def finite_time_checks():
    result = []
    for j, t in [(sp.Rational(1, 2), sp.Rational(1, 6)),
                 (sp.Rational(-1, 2), sp.Rational(1, 6)),
                 (sp.Rational(3, 4), sp.Rational(1, 6))]:
        rt, rs = 6+2*j*j, 6-6*j*j
        rows = []
        for u in [-1, 0, 1]:
            sc = sp.exp(-t*(6+2*j*j*u))
            sq = sp.Rational(3+u, 4)*sp.exp(-rt*t)+sp.Rational(1-u, 4)*sp.exp(-rs*t)
            gap = sp.N(sq-sc, 50)
            assert gap == 0 if u == 1 else gap > 0
            rows.append({'u': u, 'classical_survival_exact': str(sc),
                         'jump_survival_exact': str(sq),
                         'classical_survival': float(sc), 'jump_survival': float(sq),
                         'absolute_gap': float(gap)})
        q, x = sp.exp(-6*t), 2*j*j*t
        obstruction = q*(sp.cosh(x)-1)
        assert sp.N(obstruction, 50) > 0
        result.append({'j': str(j), 'epsilon': '1', 'time': str(t),
                       'same_input_mixture_target_gap': float(obstruction),
                       'universal_deadline_error_lower_bound': float(obstruction/2),
                       'rows': rows})
    return result


def vertex_optimum(j, x):
    """Independent vertex enumeration of the normalized symmetric-effect LP."""
    q = math.exp(-3*x/(j*j))
    A, b = [], []
    for u in [-1., 0., 1.]:
        target = math.exp(-x*u)
        A.extend([[1., u, -1.], [-1., -u, -1.]])
        b.extend([target, -target])
    # E/q = eta I + zeta T; both singlet and triplet eigenvalues must be in [0,1/q].
    A.extend([[-1., -1., 0.], [-1., 3., 0.],
              [1., 1., 0.], [1., -3., 0.], [0., 0., -1.]])
    b.extend([0., 0., 1/q, 1/q, 0.])
    A, b = np.array(A), np.array(b)
    feasible = []
    for indices in combinations(range(len(b)), 3):
        lhs = A[list(indices)]
        if abs(np.linalg.det(lhs)) < 1e-12:
            continue
        point = np.linalg.solve(lhs, b[list(indices)])
        if np.max(A@point-b) <= 1e-9:
            feasible.append(point)
    assert feasible
    best = min(feasible, key=lambda point: point[2])
    if x <= math.log(3):
        eta = (math.cosh(x)+1)/2
        zeta = -math.sinh(x)
        asserted = (math.cosh(x)-1)/2
    else:
        eta = (math.exp(x)+1)/3
        zeta = -eta
        asserted = (math.exp(x)-2)/3
    assert abs(best[2]-asserted) < 1e-9
    eigenvalues = [q*(eta+zeta), q*(eta-3*zeta)]
    assert min(eigenvalues) >= -1e-12 and max(eigenvalues) <= 1+1e-12
    errors = [abs(q*(eta+zeta*u)-q*math.exp(-x*u)) for u in [-1, 0, 1]]
    assert abs(max(errors)-q*asserted) < 1e-12
    return {'j': j, 'x': x, 'time_at_epsilon_one': x/(2*j*j),
            'normalized_LP_optimum': float(best[2]), 'normalized_asserted_optimum': asserted,
            'absolute_optimum': q*asserted,
            'attaining_triplet_and_singlet_effect_eigenvalues': eigenvalues}


def main():
    result = {'exact_checks': exact_checks(), 'finite_time_cases': finite_time_checks(),
              'pointwise_binary_minimax_controls': [vertex_optimum(j, x) for j, x in
                  [(0.25, 0.02), (0.5, 1/12), (-0.5, 1/12),
                   (0.75, 0.5), (0.75, math.log(3)), (0.75, 1.25), (0.9, 2.0)]],
              'versions': {'python': platform.python_version(), 'numpy': np.__version__,
                           'sympy': sp.__version__}, 'all_checks_passed': True}
    text = json.dumps(result, indent=2)+'\n'
    (HERE/'RESULTS.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
