#!/usr/bin/env python3
"""Pair-orientation and quadratic-kernel controls, without an RG claim."""
import itertools
import json
import math

import numpy as np


def orientations():
    rows = []
    opposite_sign_faults = []
    for theta, s, t in [(0.17, .23, -.31), (.8, .6, .2), (2.2, -.4, .9)]:
        mixed = sum(np.exp(1j*(a*s+b*t+a*b*theta))
                    for a, b in itertools.product([-1, 1], repeat=2))
        formula = 4*(math.cos(theta)*math.cos(s)*math.cos(t)
                     -1j*math.sin(theta)*math.sin(s)*math.sin(t))
        same = sum(np.exp(1j*(a*s+b*t)-a*b*theta)
                   for a, b in itertools.product([-1, 1], repeat=2))
        same_formula = 4*(math.cosh(theta)*math.cos(s)*math.cos(t)
                          +math.sinh(theta)*math.sin(s)*math.sin(t))
        derivative = sum(-a*b*np.exp(1j*a*b*theta)
                         for a, b in itertools.product([-1, 1], repeat=2))
        derivative_same = sum(-a*b*np.exp(-a*b*theta)
                              for a, b in itertools.product([-1, 1], repeat=2))
        residuals = [abs(mixed-formula), abs(same-same_formula),
                     abs(derivative+4j*math.sin(theta)),
                     abs(derivative_same-4*math.sinh(theta))]
        assert max(residuals) < 1e-13
        fault = abs(mixed-4*(math.cos(theta)*math.cos(s)*math.cos(t)
                            +1j*math.sin(theta)*math.sin(s)*math.sin(t)))
        assert fault > .01
        opposite_sign_faults.append(fault)
        rows.append(dict(theta=theta, residuals=residuals,
                         vacuum_connected=4*(math.cos(theta)-1),
                         mixed_source_derivative_imaginary=float(derivative.imag)))
    # Independent log-partition finite-difference test, with complex sources.
    theta, s, t = .7, .2, -.3
    joint = sum(np.exp(1j*(a*s+b*t+a*b*theta))
                for a, b in itertools.product([-1, 1], repeat=2))
    first, second = 2*math.cos(s), 2*math.cos(t)
    expected = joint-first*second
    def logz(z, w):
        return np.log(1+first*z+second*w+joint*z*w)
    step = 1e-4
    stencil = (logz(step, step)-logz(step, -step)
               -logz(-step, step)+logz(-step, -step))/(4*step**2)
    assert abs(stencil-expected) < 1e-6
    return dict(orientation_controls=rows, opposite_sign_fault_residuals=opposite_sign_faults,
                log_partition_cross_difference_error=float(abs(stencil-expected)))


def exterior_projection(xi):
    pairs = list(itertools.combinations(range(4), 2))
    D = np.zeros((6, 4))
    for n, (i, j) in enumerate(pairs):
        D[n, j], D[n, i] = xi[i], -xi[j]
    return D@D.T/(xi@xi)


def quadratic():
    controls = []
    for xi in [np.array([1., .7, .2, 1.4]), np.array([0., 0., 2., 0.]),
               np.array([.2, -.8, 1.3, .4])]:
        P = exterior_projection(xi)
        Q = np.eye(6)-P
        assert np.max(abs(P@P-P)) < 1e-14
        assert np.linalg.matrix_rank(P, tol=1e-10) == 3
        for a, b, c in [(0.1, .3, .2), (2., 4., 7.), (0., 0., 11.)]:
            A = np.array([[a, -1j*c], [-1j*c, 0.]])
            B = np.array([[0., 0.], [0., b]])
            full = np.eye(12)+np.kron(A, P)+np.kron(B, Q)
            direct = np.linalg.inv(full)
            split = np.kron(np.linalg.inv(np.eye(2)+A), P)+np.kron(np.linalg.inv(np.eye(2)+B), Q)
            residual = float(np.max(abs(direct-split)))
            norm = float(np.linalg.svd(direct, compute_uv=False)[0])
            wrong = np.kron(np.linalg.inv(np.eye(2)+A), Q)+np.kron(np.linalg.inv(np.eye(2)+B), P)
            fault = float(np.max(abs(direct-wrong)))
            assert residual < 3e-14 and norm <= 1+1e-13 and fault > .01
            assert abs(np.linalg.det(np.eye(2)+A)-(1+a+c*c)) < 1e-12
            controls.append(dict(parameters=[a,b,c], residual=residual,
                                 inverse_norm=norm, swapped_projection_fault=fault))
    return controls


def fft_controls():
    rows = []
    for length in [8, 12, 16, 24, 32]:
        v = 4*np.sin(np.pi*np.arange(length)/length)**2
        arrays = [v.reshape(tuple(length if j == i else 1 for j in range(4)))
                  for i in range(4)]
        denominator = sum(arrays)
        numerator = arrays[0]+arrays[1]
        symbol = np.divide(numerator, denominator, out=np.zeros_like(denominator),
                           where=denominator > 0)
        kernel = np.fft.ifftn(symbol).real
        diagonal_target = (1-length**(-4))/2
        parseval_error = abs(float(np.sum(kernel**2)-np.mean(symbol**2)))
        assert abs(kernel.flat[0]-diagonal_target) < 1e-14
        assert parseval_error < 1e-14
        # The rank-zero harmonic point is explicitly excluded above.
        assert symbol[1,0,0,0] == 1 and symbol[0,0,1,0] == 0
        theta = 2*math.pi*3*kernel
        vacuum_sum = float(np.sum(abs(np.cos(theta)-1)))
        upper = float(np.sum(theta**2)/2)
        assert vacuum_sum <= upper+1e-12
        rows.append(dict(length=length, absolute_row_sum=float(np.sum(abs(kernel))),
                         same_orientation_square_sum=float(np.sum(kernel**2)),
                         periodic_diagonal=float(kernel.flat[0]),
                         parseval_error=float(parseval_error),
                         vacuum_pair_absolute_sum=vacuum_sum,
                         square_majorant=upper,
                         source_pair_absolute_sum=float(np.sum(abs(np.sin(theta))))))
    return dict(rows=rows,
                scope='Finite Fourier controls; no fitted divergence rate or thermodynamic proof.')


if __name__ == '__main__':
    print(json.dumps(dict(status='finite_checks_passed',
                         scope='Orientation/source algebra, signed quadratic inverse and finite Fourier checks only.',
                         orientations=orientations(), quadratic=quadratic(), fft=fft_controls()), indent=2))
