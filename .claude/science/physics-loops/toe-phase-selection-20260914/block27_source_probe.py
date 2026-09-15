#!/usr/bin/env python3
"""Finite challenges of the private coupled-source probe; no phase proof."""
import itertools
import json
import math

import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss


def mgf_control():
    z, c = 1 / 64, 4.0
    nodes, weights = hermgauss(120)
    x, w = math.sqrt(2) * nodes, weights / math.sqrt(math.pi)
    signed = (1 + z * math.exp(c * c / 2) * np.cos(c * x)) / (1 + z)
    errors = []
    for t in [-1.2, -0.4, 0, 0.7, 1.5]:
        direct = float(w @ (signed * np.exp(t * x)))
        target = math.exp(t * t / 2) * (1 + z * math.cos(c * t)) / (1 + z)
        errors.append(abs(direct - target))
    imaginary_value = math.exp(-8) * (1 + z * math.cosh(16)) / (1 + z)
    signed_at_pi_over_four = (1 - z * math.exp(8)) / (1 + z)
    u = sp.symbols('u', real=True)
    # A separate polynomial identity proves |u+z| <= 1+zu on [-1,1].
    rational_z = sp.Rational(1, 64)
    identity = sp.expand((1 + rational_z*u)**2 - (u+rational_z)**2)
    assert sp.expand(identity - (1-rational_z**2)*(1-u**2)) == 0
    assert max(errors) < 2e-12
    assert imaginary_value > 1 and signed_at_pi_over_four < 0
    return dict(laplace_quadrature_errors=errors,
                putative_characteristic_at_four=imaginary_value,
                signed_multiplier_at_pi_over_four=signed_at_pi_over_four,
                exact_log_curvature_lower_bound='47/63',
                conclusion='The proposed moment function is not a probability MGF.')


def contour_control():
    C = np.array([[1.1, .23], [.23, .7]])
    r = np.array([[1.2, .4], [-.3, 1.1]])
    rp = np.array([[.9, -.1], [.2, .8]])
    z = np.array([.09, .07])
    nodes, weights = hermgauss(80)
    standard = np.array(list(itertools.product(nodes, repeat=2))) * math.sqrt(2)
    weights2 = np.array([a*b for a, b in itertools.product(weights, repeat=2)]) / math.pi
    sample = standard @ np.linalg.cholesky(C).T

    def polynomial(a):
        # Direct finite Fourier/Gaussian expansion, with the ORIGINAL r source.
        total = 0j
        for sigma_tuple in itertools.product([-1, 0, 1], repeat=2):
            sigma = np.array(sigma_tuple)
            coefficient = np.prod([1 if s == 0 else z[i]/2
                                   for i, s in enumerate(sigma_tuple)])
            frequency = sigma @ rp
            total += coefficient * np.exp(-frequency @ C @ frequency/2
                                            + 1j*(sigma @ r) @ a)
        return total

    base = np.prod(1 + z*np.cos(sample @ rp.T), axis=1)
    normalization = polynomial(np.zeros(2)).real
    assert abs(weights2 @ base - normalization) < 1e-13
    checks, fault_rejections = [], []
    for v in [np.array([.4, -.7]), np.array([1.1, .6]), np.array([-.8, .2])]:
        eta = (r-rp) @ C @ v
        numerator = np.prod(1 + z*np.cos(sample @ rp.T - 1j*eta), axis=1)
        rhs = weights2 @ (np.exp(-1j*(sample @ v))*numerator) / normalization
        lhs = np.exp(-v @ C @ v/2) * polynomial(-1j*C @ v) / normalization
        omitted = weights2 @ (np.exp(-1j*(sample @ v))*base) / normalization
        wrong_sign = weights2 @ (np.exp(-1j*(sample @ v))*
                       np.prod(1 + z*np.cos(sample @ rp.T + 1j*eta), axis=1)) / normalization
        checks.append(float(abs(lhs-rhs)))
        fault_rejections.extend([float(abs(lhs-omitted)), float(abs(lhs-wrong_sign))])
    assert max(checks) < 2e-13
    assert min(fault_rejections) > 1e-5
    return dict(exact_fourier_versus_real_gaussian_quadrature_errors=checks,
                omitted_ratio_and_wrong_shift_fault_residuals=fault_rejections)


def cochain_control():
    d = 4
    cells = {}
    for p in [1, 2]:
        cells[p] = [(x, ori) for ori in itertools.combinations(range(d), p)
                    for x in itertools.product(range(2), repeat=d)
                    if all(x[j] == 0 for j in ori)]
    edges = {cell: i for i, cell in enumerate(cells[1])}
    D = np.zeros((len(cells[2]), len(cells[1])))
    for k, (x, ori) in enumerate(cells[2]):
        for pos, direction in enumerate(ori):
            face_ori = tuple(j for j in ori if j != direction)
            advanced = list(x)
            advanced[direction] += 1
            D[k, edges[(tuple(advanced), face_ori)]] += (-1)**pos
            D[k, edges[(x, face_ori)]] -= (-1)**pos
    Q = D.T @ D
    eigenvalues, eigenvectors = np.linalg.eigh(Q)
    inv = np.zeros_like(eigenvalues)
    inv[eigenvalues > 1e-10] = 1/eigenvalues[eigenvalues > 1e-10]
    V = (eigenvectors * inv) @ eigenvectors.T
    beta = 3.7
    C = beta*V
    errors, wrong_scale = [], []
    for plaquette in [0, 7, 14, 23]:
        rho = 2*math.pi*D[plaquette]
        selected = int(np.flatnonzero(rho)[0])
        u = np.zeros(Q.shape[0])
        # Free-cube diagonals differ from the periodic value6. The identity
        # being tested only needs r-r'=Qu; this is NOT a damping theorem here.
        u[selected] = rho[selected]/Q[selected, selected]
        damped = rho-Q@u
        h = np.sin(np.arange(D.shape[0])*.43 + plaquette)
        v = D.T@h/math.sqrt(beta)
        eta = (rho-damped)@C@v
        target = math.sqrt(beta)*u@D.T@h
        errors.append(abs(float(eta-target)))
        wrong_scale.append(abs(float(eta-u@D.T@h)))
    assert max(errors) < 1e-12
    assert min(wrong_scale) > 1e-4
    return dict(cells=dict(edges=len(cells[1]), plaquettes=len(cells[2])),
                source_identity_errors=errors, missing_sqrt_beta_fault_residuals=wrong_scale,
                scope='Finite free-cube source algebra only, not periodic ensemble damping.')


def linear_shift_control():
    theta, eta, z = sp.symbols('theta eta z', real=True)
    ratio = (1+z*sp.cos(theta-sp.I*eta))/(1+z*sp.cos(theta))
    first = sp.diff(ratio, eta).subs(eta, 0)
    target = sp.I*z*sp.sin(theta)/(1+z*sp.cos(theta))
    assert sp.simplify(first-target) == 0
    assert sp.simplify(first+target) != 0
    return dict(first_source_derivative='i z sin(theta)/(1+z cos(theta))',
                opposite_sign_fault_rejected=True)


if __name__ == '__main__':
    result = dict(status='finite_checks_passed',
                  scope='Four finite families; no fixed-clock phase or Gaussianity claim.',
                  mgf_control=mgf_control(), contour_control=contour_control(),
                  cochain_control=cochain_control(), linear_shift_control=linear_shift_control())
    print(json.dumps(result, indent=2))
