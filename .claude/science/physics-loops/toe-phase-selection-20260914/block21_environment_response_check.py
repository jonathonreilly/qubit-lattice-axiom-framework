#!/usr/bin/env python3
"""Finite Bloch/cochain and Gaussian-precision checks of the response design.

The environment is a two-site layered quadratic potential. This is a
controlled comparison model, not the nonlinear Villain auxiliary law.
"""
from pathlib import Path
import itertools
import json
import numpy as np

D = 4
C = 1 / 32
BASES = [list(itertools.combinations(range(D), r)) for r in range(D + 1)]


def wedge(deltas, r):
    n = deltas[0].shape[0]
    result = np.zeros((len(BASES[r + 1]) * n, len(BASES[r]) * n), complex)
    ids = {I: i for i, I in enumerate(BASES[r])}
    for row, J in enumerate(BASES[r + 1]):
        for j, mu in enumerate(J):
            col = ids[J[:j] + J[j + 1:]]
            result[row*n:(row+1)*n, col*n:(col+1)*n] += (-1)**j * deltas[mu]
    return result


def preconditioner(deltas, local_c=C):
    d2, d3 = wedge(deltas, 2), wedge(deltas, 3)
    assert np.linalg.norm(d3 @ d2) < 2e-13
    derivative = np.vstack([d2.conj().T, d3])
    laplacian = derivative.conj().T @ derivative
    return derivative @ np.linalg.solve(laplacian, derivative.conj().T) - local_c * derivative @ derivative.conj().T


def multiplier(k):
    return preconditioner([np.array([[np.expm1(1j*t)]]) for t in k])


def continuum(p):
    return preconditioner([np.array([[1j*t]]) for t in p], local_c=0)


def gaussian_covariance(K, A):
    # Direct integration of a proper Gaussian density on range(K):
    # inverse of its precision in orthonormal compatible coordinates.
    eigen, vectors = np.linalg.eigh(K)
    V, positive = vectors[:, eigen > 1e-10], eigen[eigen > 1e-10]
    precision = np.diag(1 / positive) - V.conj().T @ A @ V
    assert np.min(np.linalg.eigvalsh(precision)) > .5
    return V @ np.linalg.solve(precision, V.conj().T)


def layered_checks():
    alpha, eta = -.12, .09
    first = np.diag([1.] * 6 + [0.])
    avg, difference = alpha * first, eta * first
    phase_A = np.diag([alpha + eta, alpha - eta])
    A = np.kron(first, phase_A)
    e0 = np.array([[1.], [1.]]) / np.sqrt(2)
    e1 = np.array([[1.], [-1.]]) / np.sqrt(2)
    embed = np.kron(np.eye(7), e0)
    U = np.hstack([embed, np.kron(np.eye(7), e1)])
    pi_shift = np.array([np.pi, 0., 0., 0.])
    Kenv = multiplier(pi_shift)
    effective = avg + difference @ np.linalg.solve(np.eye(7) - Kenv @ avg, Kenv @ difference)
    shortcut_defect = np.linalg.norm(effective - avg)
    assert shortcut_defect > .005
    rows, fiber_errors, precision_errors = [], [], []
    for p in [np.array([1., 2., -1., .5]), np.array([1., 0., 0., 0.]), np.array([0., 1., 0., 0.])]:
        K0 = continuum(p)
        limiting = np.linalg.solve(np.eye(7) - K0 @ effective, K0)
        wrong = np.linalg.solve(np.eye(7) - K0 @ avg, K0)
        errors = []
        for a in [1/8, 1/16, 1/32, 1/64, 1/128, 1/256]:
            k = a * p
            shift = np.array([[0., 1.], [1., 0.]])
            deltas = [np.exp(1j*k[0]) * shift - np.eye(2)]
            deltas += [np.expm1(1j*k[j]) * np.eye(2) for j in range(1, 4)]
            K = preconditioner(deltas)
            blocks = np.zeros((14, 14), complex)
            blocks[:7, :7], blocks[7:, 7:] = multiplier(k), multiplier(k + pi_shift)
            ferr = np.linalg.norm(U.conj().T @ K @ U - blocks)
            fiber_errors.append(float(ferr))
            assert ferr < 2e-9
            covariance = gaussian_covariance(K, A)
            response = np.linalg.solve(np.eye(14) - K @ A, K)
            perr = np.linalg.norm(covariance - response)
            precision_errors.append(float(perr))
            assert perr < 2e-10
            projected = embed.conj().T @ covariance @ embed
            errors.append(float(np.linalg.norm(projected - limiting)))
        assert errors[-1] < errors[0] / 20
        rows.append(dict(direction=p.tolist(),mesh=[1/8,1/16,1/32,1/64,1/128,1/256],limit_errors=errors,mean_hessian_shortcut_limit_error=float(np.linalg.norm(wrong-limiting))))
    assert max(row['mean_hessian_shortcut_limit_error'] for row in rows) > .005
    return dict(alpha=alpha,eta=eta,effective_diagonal=np.real(np.diag(effective)).tolist(),mean_hessian_shortcut_matrix_error=float(shortcut_defect),maximum_fiber_identity_error=max(fiber_errors),maximum_precision_response_error=max(precision_errors),cases=rows)


def symmetry_commutant():
    # General (not assumed symmetric) two-form matrices commuting with all
    # coordinate reflections and adjacent swaps have only one free parameter.
    import sympy as s
    pairs = BASES[2]
    generators = []
    for mu in range(4):
        generators.append(s.diag(*[-1 if mu in I else 1 for I in pairs]))
    for mu in range(3):
        perm = list(range(4))
        perm[mu], perm[mu+1] = perm[mu+1], perm[mu]
        G = s.zeros(6)
        for col, I in enumerate(pairs):
            J = [perm[i] for i in I]
            sign = 1 if J[0] < J[1] else -1
            G[pairs.index(tuple(sorted(J))), col] = sign
        generators.append(G)
    variables = s.symbols('b:36')
    B = s.Matrix(6, 6, variables)
    equations = [entry for G in generators for entry in B*G-G*B]
    matrix, _ = s.linear_eq_to_matrix(equations, variables)
    null = matrix.nullspace()
    assert len(null) == 1
    candidate = s.Matrix(6, 6, null[0])
    assert candidate == candidate[0, 0] * s.eye(6)
    return dict(unknown_entries=36,generators=7,commutant_dimension=1,antisymmetric_component_excluded=True)


def invariant_mixture_control():
    # Average four rotated layered Gaussian environments. The global layer
    # orientation is a translation-invariant random label. Cubic symmetry
    # of the average does not make this environment spatially ergodic.
    alpha, eta = -.12, .09
    first = np.diag([1.] * 6 + [0.])
    avg, diff = alpha * first, eta * first
    p = np.array([0., 0., 0., 1.])
    K0 = continuum(p)
    test = np.zeros(7)
    test[BASES[2].index((0, 1))] = 1
    variances = []
    for mu in range(4):
        k = np.zeros(4)
        k[mu] = np.pi
        Km = multiplier(k)
        effective = avg + diff @ np.linalg.solve(np.eye(7)-Km@avg, Km@diff)
        covariance = np.linalg.solve(np.eye(7)-K0@effective, K0)
        variances.append(float(np.real(test @ covariance @ test)))
    # A mixture of centered Gaussians has fourth cumulant 3 Var(variance).
    fourth = 3 * float(np.var(variances))
    assert fourth > 1e-6
    return dict(component_variances=variances,mixture_fourth_cumulant=fourth,translation_invariant_global_label=True,qualification='Comparison model only; not a counterexample to the actual small-carrier Villain law or its uniform third-influence hypotheses.')


if __name__ == '__main__':
    result = dict(layered=layered_checks(),symmetry=symmetry_commutant(),mixture_control=invariant_mixture_control(),qualification='Exact finite cochain construction, Gaussian precision inversion, and rational symmetry algebra challenge the stationary-response design. Numerical convergence checks do not prove infinite-volume homogenization or nonlinear state matching.')
    Path(__file__).with_name('BLOCK21_ENVIRONMENT_RESPONSE_CHECKS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
