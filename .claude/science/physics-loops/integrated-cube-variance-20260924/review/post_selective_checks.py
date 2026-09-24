"""Narrow POST checks: independent words and a rectangular Sylvester identity.

No author control is imported. The numerical Sylvester check is illustrative;
the dimension-free inverse bound is established analytically in POST.md.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json

import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm, solve_sylvester

A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
edges = tuple((a, b) for a in A for b in B if (a ^ b).bit_count() == 1)
omega = {(tuple(int(v in A) for v in range(8)), (0,) * 12): 1}

def check_gauss(key):
    q, fields = key
    divergence = [0] * 8
    for field, (a, b) in zip(fields, edges):
        divergence[a] += field
        divergence[b] -= field
    assert divergence == [q[v] - int(v in A) for v in range(8)]

def F(state):
    out = defaultdict(int)
    for (q, fields), amplitude in state.items():
        for e, (a, b) in enumerate(edges):
            if q[a] and not q[b]:
                nq, ne = list(q), list(fields)
                nq[a], nq[b] = 0, q[a]
                ne[e] -= q[a]
                key = tuple(nq), tuple(ne)
                check_gauss(key)
                out[key] += amplitude
    return {key: value for key, value in out.items() if value}

def J(state, edge, signs):
    out = defaultdict(int)
    a, b = edges[edge]
    for (q, fields), amplitude in state.items():
        if q[a] or q[b]:
            continue
        for sign in signs:
            nq, ne = list(q), list(fields)
            nq[a], nq[b] = sign, -sign
            ne[edge] += sign
            key = tuple(nq), tuple(ne)
            check_gauss(key)
            out[key] += amplitude
    return {key: value for key, value in out.items() if value}

def norm2(state):
    return sum(value * value for value in state.values())

word_rows = []
for label, signs in [('plus', (1,)), ('minus', (-1,)), ('coherent', (1, -1))]:
    born = J(F(omega), 0, signs)
    b = norm2(born)
    moved = F(born)
    loss_form = 0
    loss_square = 0
    for (q, fields), amplitude in moved.items():
        gamma = 2 * sum(not q[a] and not q[b] for a, b in edges)
        assert gamma in (0, 2)
        loss_form += gamma * amplitude**2
        loss_square += gamma**2 * amplitude**2
    resolved = sum(norm2(J(moved, edge, (sign,))) for edge in range(12) for sign in (1, -1))
    coherent = sum(norm2(J(moved, edge, (1, -1))) for edge in range(12))
    assert resolved == coherent == loss_form == 8 * b
    assert loss_square == 16 * b
    word_rows.append({'mark': label, 'b': b, 'loss_expectation': str(Fraction(loss_form, b)), 'Gamma_F_norm_squared': str(Fraction(loss_square, b)), 'resolved_second_sum': str(Fraction(resolved, b)), 'coherent_second_sum': str(Fraction(coherent, b))})

R0 = np.array([[-1+2j, .3+.2j], [0, -1.5-1j]], complex)
R1 = np.array([[-2+.5j, .2j, .3], [0, -1.2-.7j, .15], [0, 0, -1.7+.4j]], complex)
C = np.array([[1+.2j, -.3+.7j, .5], [.2-.4j, .8, -1+.3j]], complex)
initial0 = np.array([1., 1j]) / np.sqrt(2)
initial1 = np.array([1., 2j, 1.-1j]) / np.sqrt(7)
lower, upper = .002, .009
sylvester_rows = []
for epsilon in (.25, .125):
    K0 = R0 / epsilon**2
    K1 = -1j * np.eye(3) / epsilon**4 + R1 / epsilon**2
    Y = solve_sylvester(K0.conj().T, K1, C)
    residual = np.linalg.norm(K0.conj().T @ Y + Y @ K1 - C)
    scalar_gap = epsilon**-4
    remainder_bound = (np.linalg.norm(R0, 2) + np.linalg.norm(R1, 2)) / epsilon**2
    assert scalar_gap > remainder_bound
    bound = np.linalg.norm(C, 2) / (scalar_gap - remainder_bound)
    assert residual < 1e-12 and np.linalg.norm(Y, 2) <= bound
    f = lambda t: np.vdot(expm(t*K0) @ initial0, C @ (expm(t*K1) @ initial1))
    integral = quad(lambda t: f(t).real, lower, upper, epsabs=1e-13, epsrel=1e-12)[0] + 1j * quad(lambda t: f(t).imag, lower, upper, epsabs=1e-13, epsrel=1e-12)[0]
    endpoint = lambda t, matrix: np.vdot(expm(t*K0) @ initial0, matrix @ (expm(t*K1) @ initial1))
    correct = endpoint(upper, Y) - endpoint(lower, Y)
    wrong_Y = solve_sylvester(K0, K1, C)
    wrong = endpoint(upper, wrong_Y) - endpoint(lower, wrong_Y)
    assert abs(correct-integral) < 1e-12
    assert abs(wrong-integral) > 1e-7
    sylvester_rows.append({'epsilon':epsilon,'shape':[2,3], 'Sylvester_residual':float(residual), 'solution_operator_norm':float(np.linalg.norm(Y,2)), 'Neumann_operator_norm_bound':float(bound), 'independent_quadrature_endpoint_error':float(abs(correct-integral)), 'wrong_missing_adjoint_error':float(abs(wrong-integral))})

result = {'original_word_rows':word_rows,'rectangular_Sylvester_rows':sylvester_rows,'scope':'Exact physical charge/field words plus a separate 2x3 nonnormal finite-matrix diagnostic; no new joint-limit simulation.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('POST_SELECTIVE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
