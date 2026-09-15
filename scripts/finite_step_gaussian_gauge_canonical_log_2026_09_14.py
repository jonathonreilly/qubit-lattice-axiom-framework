#!/usr/bin/env python3
"""Author checks of transfer-log identities; no compact-clock phase inference."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools
import json

import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad, quad_vec
from scipy.linalg import eigh, expm, norm
from scipy.special import eval_hermite, factorial, ive


def positive_log(a):
    w, u = eigh(a)
    assert w.min() > 0
    return (u * np.log(w)) @ u.conj().T


def response_multiplier(x):
    x = np.asarray(x)
    y = np.ones_like(x, dtype=float)
    nz = np.abs(x) > 1e-8
    y[nz] = (x[nz] / 2) / np.tanh(x[nz] / 2)
    y[~nz] += x[~nz] ** 2 / 12
    return y


def inverse_response_checks():
    rng = np.random.default_rng(71020914)
    rows = []
    for energies in ([0., 0., .6, 2.], [-1., -.2, .7, 1.9]):
        z = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        u, _ = np.linalg.qr(z)
        h0 = (u * energies) @ u.conj().T
        z = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        v = (z + z.conj().T) / 4
        t0 = expm(-h0)
        for s in (0., .37):
            def transfer(sigma):
                a = expm(sigma * v / 2)
                return a @ t0 @ a
            t = transfer(s)
            h = -positive_log(t)
            e, u = eigh(h)
            gap = e[:, None] - e[None, :]
            ve = u.conj().T @ v @ u
            predicted = -u @ (response_multiplier(gap) * ve) @ u.conj().T
            eps = 2e-5
            finite_difference = (-positive_log(transfer(s + eps))
                                 + positive_log(transfer(s - eps))) / (2 * eps)
            dt = (v @ t + t @ v) / 2
            eye = np.eye(4)
            def log_integrand(x):
                inv = np.linalg.solve(t + x * eye, eye)
                return -inv @ dt @ inv
            integral, _ = quad_vec(log_integrand, 0., np.inf, epsabs=1e-10)
            w = h @ (h @ v - v @ h) - (h @ v - v @ h) @ h
            we = u.conj().T @ w @ u
            def time_integrand(tau):
                kernel = -np.log(-np.expm1(-2 * np.pi * tau)) / (2 * np.pi)
                return kernel * (2 * np.cos(tau * gap) * we)
            correction_e, _ = quad_vec(time_integrand, 0., np.inf, epsabs=1e-10)
            from_time = -v - u @ correction_e @ u.conj().T
            err_fd = norm(predicted - finite_difference, 2)
            err_integral = norm(predicted - integral, 2)
            err_time = norm(predicted - from_time, 2)
            assert max(err_fd, err_integral, err_time) < 2e-8
            correction = norm(predicted + v, 2)
            upper = norm(w, 2) / 12
            assert correction <= upper + 1e-10
            wrong = -u @ (ve / response_multiplier(gap)) @ u.conj().T
            wrong_error = norm(wrong - integral, 2)
            assert wrong_error > .01
            rows.append(dict(s=s, energies=energies, finite_difference_error=err_fd,
                             resolvent_integral_error=err_integral,
                             time_kernel_error=err_time, correction_norm=correction,
                             double_commutator_bound=upper,
                             reciprocal_mutation_error=wrong_error))
    kernel_integral = quad(lambda x: -np.log(-np.expm1(-2 * np.pi * x)) /
                           (2 * np.pi), 0., np.inf, epsabs=1e-12)[0]
    assert abs(kernel_integral - 1 / 24) < 1e-11
    return dict(cases=rows, kernel_integral=kernel_integral)


def gaussian_functions(r):
    r = np.asarray(r, dtype=float)
    assert np.min(r) >= -1e-12
    r = np.maximum(r, 0)
    x = np.sqrt(r) / 2
    omega = 2 * np.arcsinh(x)
    fg = np.ones_like(r)
    nz = x > 1e-8
    fg[nz] = np.arcsinh(x[nz]) / (x[nz] * np.sqrt(1 + x[nz] ** 2))
    fg[~nz] -= r[~nz] / 6
    return omega, fg


def oscillator_checks():
    nodes, weights = hermgauss(80)
    rows = []
    for bt, bs, lam in ((1., 1., .03), (.7, 2., 1.4), (3., .4, 8.)):
        r = bs * lam / bt
        omega, fg = (float(x) for x in gaussian_functions(r))
        aa, bb = fg / bt, bs * lam * (1 + r / 4) * fg
        eta = np.sqrt(bb / aa)
        assert abs(aa * bb - omega ** 2) < 1e-12
        resolvent = quad(lambda u: 1 / (1 + r * (1 - u * u) / 4), 0, 1)[0]
        assert abs(resolvent - fg) < 1e-12
        # Integrate the original transfer kernel acting on normalized oscillator
        # wave functions. This does not exponentiate the proposed Hamiltonian.
        exponent = bt / 2 + bs * lam / 4 + eta / 2
        z = nodes / np.sqrt(exponent)
        max_error = 0.
        for n in (0, 1, 2, 4):
            normalization = (eta / np.pi) ** .25 / np.sqrt(2 ** n * factorial(n))
            for x in (-.9, -.2, .4, 1.1):
                integrated = (np.sqrt(bt / (2 * np.pi * exponent)) * normalization *
                              np.exp(-(bt / 2 + bs * lam / 4) * x * x) *
                              np.dot(weights, np.exp(bt * x * z) *
                                     eval_hermite(n, np.sqrt(eta) * z)))
                expected = (np.exp(-omega * (n + .5)) * normalization *
                            eval_hermite(n, np.sqrt(eta) * x) * np.exp(-eta*x*x/2))
                max_error = max(max_error, abs(integrated - expected))
        assert max_error < 1e-11
        # Independent Gaussian convolution of two original transfer kernels.
        x, y = .6, -.3
        ct = bt + bs * lam / 2
        actual_t2 = bt / (2 * np.pi) * np.sqrt(np.pi / ct) * np.exp(
            -(bt / 2 + bs * lam / 4) * (x*x+y*y) + bt*bt*(x+y)**2/(4*ct))
        predicted_t2 = np.sqrt(omega / (2*np.pi*aa*np.sinh(2*omega))) * np.exp(
            -omega / (2*aa*np.sinh(2*omega)) *
            ((x*x+y*y)*np.cosh(2*omega)-2*x*y))
        assert abs(actual_t2 - predicted_t2) < 1e-12
        # A missing vacuum scalar would leave the n=0 eigenvalue at one.
        assert abs(np.exp(-omega/2) - 1) > .05
        rows.append(dict(beta_t=bt, beta_s=bs, lam=lam, omega=omega,
                         A=aa, B=bb, integral_eigenfunction_max_error=max_error,
                         two_step_normalization_error=abs(actual_t2-predicted_t2)))
    omega, fg = gaussian_functions(np.array([0., 1e-14, 1e-8]))
    assert omega[0] == 0 and fg[0] == 1
    return dict(cases=rows, zero_mode_frequency=float(omega[0]),
                zero_mode_fg=float(fg[0]))


def cubic_incidence(length):
    vertices = list(itertools.product(range(length), repeat=3))
    edges = [(x, j) for x in vertices for j in range(3)]
    edge_index = {e: i for i, e in enumerate(edges)}
    vertex_index = {x: i for i, x in enumerate(vertices)}
    faces = [(x, i, j) for x in vertices for i in range(3) for j in range(i+1, 3)]
    def step(x, j):
        y = list(x)
        y[j] = (y[j] + 1) % length
        return tuple(y)
    f = np.zeros((len(faces), len(edges)))
    g = np.zeros((len(edges), len(vertices)))
    for row, (x, i, j) in enumerate(faces):
        for e, sign in (((x, i), 1), ((step(x, i), j), 1),
                        ((step(x, j), i), -1), ((x, j), -1)):
            f[row, edge_index[e]] += sign
    for row, (x, j) in enumerate(edges):
        g[row, vertex_index[step(x, j)]] += 1
        g[row, vertex_index[x]] -= 1
    assert np.array_equal(f @ g, np.zeros((len(faces), len(vertices))))
    return edges, f, g


def cubic_and_locality_checks():
    rows = []
    for length in (3, 4):
        edges, f, g = cubic_incidence(length)
        k = f.T @ f
        values, u = eigh(k)
        assert values.min() > -1e-12 and values.max() <= 12 + 1e-12
        predicted = []
        symbol_error = 0.
        anchors = np.array([x for x, _ in edges])
        orientations = np.array([j for _, j in edges])
        for momentum in itertools.product(range(length), repeat=3):
            lam = 4 * sum(np.sin(np.pi*j/length)**2 for j in momentum)
            predicted.extend([0, lam, lam])
            d = np.exp(2j*np.pi*np.array(momentum)/length)-1
            symbol = lam*np.eye(3)-d[:, None]*d[None, :].conj()
            phase = np.exp(2j*np.pi*(anchors@np.array(momentum))/length)
            embedded = phase[:, None]*np.eye(3)[orientations]
            symbol_error = max(symbol_error, norm(k@embedded-embedded@symbol, 2))
        assert symbol_error < 2e-12
        assert np.max(abs(np.sort(predicted) - values)) < 1e-11
        assert np.count_nonzero(values > 1e-8) == 2 * (length**3-1)
        assert np.linalg.matrix_rank(g) == length**3 - 1
        bt, bs, ceiling = 1., 1., 12.
        omega, fg = gaussian_functions(values * bs / bt)
        aa = (u * (fg / bt)) @ u.T
        bb = (u * (bs * np.maximum(values, 0) * (1 +
                         bs*np.maximum(values, 0)/(4*bt)) * fg)) @ u.T
        assert norm(aa @ bb - (u * omega**2) @ u.T, 2) < 2e-12
        # Direct local-layer symplectic product versus the canonical log.
        if length == 3:
            dim = len(edges)
            eye, zero = np.eye(dim), np.zeros((dim, dim))
            position_layer = np.block([[eye, zero], [-1j*bs*k/2, eye]])
            momentum_layer = np.block([[eye, 1j*eye/bt], [zero, eye]])
            # The palindromic local-layer product is checked against the log's
            # matrix exponential and its entries calculated separately.
            direct = position_layer @ momentum_layer @ position_layer
            canonical = expm(np.block([[zero, 1j*aa], [-1j*bb, zero]]))
            direct_explicit = np.block([[eye+bs*k/(2*bt), 1j*eye/bt],
                [-1j*bs*k@(eye+bs*k/(4*bt)), eye+bs*k/(2*bt)]])
            assert norm(direct - direct_explicit, 2) < 1e-12
            symplectic_error = norm(canonical - direct_explicit, 2)
            assert symplectic_error < 3e-11
        else:
            symplectic_error = None
        a = bs/(4*bt)
        qmax = a*ceiling/(1+a*ceiling)
        shifted = np.eye(len(edges)) - k/ceiling
        current = np.eye(len(edges))
        polynomial = np.zeros_like(k)
        tails = []
        for degree in range(25):
            def weight_integrand(v):
                z = a*(1-v*v)*ceiling
                q = z/(1+z)
                return (1-q)*q**degree
            weight = quad(weight_integrand, 0, 1, epsabs=1e-14)[0]
            polynomial += weight * current
            if degree in (0, 1, 3, 8, 16, 24):
                err_a = norm(aa-polynomial/bt, 2)
                approx_b = bs*k@(np.eye(len(edges))+a*k)@polynomial
                err_b = norm(bb-approx_b, 2)
                bound_a = qmax**(degree+1)/bt
                bound_b = bs*ceiling*(1+a*ceiling)*qmax**(degree+1)
                assert err_a <= bound_a+2e-12
                assert err_b <= bound_b+2e-11
                tails.append(dict(degree=degree, A_error=err_a, A_bound=bound_a,
                                  B_error=err_b, B_bound=bound_b))
            current = current @ shifted
        rows.append(dict(length=length, edges=len(edges), spectrum_max=float(values.max()),
                         transverse_modes=int(np.count_nonzero(values>1e-8)),
                         symplectic_error=symplectic_error, symbol_error=symbol_error,
                         polynomial_tails=tails))
    # Small momentum behavior: frequency is linear, canonical coefficients are
    # regular even functions. This is a diagnostic, not the analyticity proof.
    sample = []
    for t in (1e-2, 1e-3, 1e-4):
        lam = 4*np.sin(t/2)**2
        omega, fg = (float(v) for v in gaussian_functions(lam))
        sample.append(dict(k=t, omega_over_k=omega/t, A=fg,
                           B_over_lambda=(1+lam/4)*fg))
        assert abs(omega/t-1) < t*t
        assert abs(fg-1) < t*t
    return dict(cubic_cases=rows, infrared=sample)


def pinv_positive(a):
    values, vectors = eigh(a)
    inverse = np.zeros_like(values)
    active = values > 1e-10
    inverse[active] = 1 / values[active]
    return (vectors * inverse) @ vectors.T


def charge_and_kernel_checks():
    rng = np.random.default_rng(31914)
    charge_rows = []
    for length, bt, bs in ((3, .7, 1.8), (4, 2., .3)):
        edges, f, g = cubic_incidence(length)
        k = f.T @ f
        values, u = eigh(k)
        _, fg = gaussian_functions(bs * values / bt)
        aa = (u * (fg / bt)) @ u.T
        rho = np.zeros(length**3)
        rho[0], rho[1] = 1, -1
        delta_inverse = pinv_positive(g.T @ g)
        longitudinal = g @ delta_inverse @ rho
        a_inv = np.linalg.inv(aa)
        # Solve the general A-dependent KKT problem, without using A G=G/bt.
        kkt = a_inv @ g @ pinv_positive(g.T @ a_inv @ g) @ rho
        assert norm(g.T @ kkt - rho) < 1e-12
        assert norm(kkt-longitudinal) < 2e-12
        cost = float(kkt @ aa @ kkt / 2)
        expected = float(rho @ delta_inverse @ rho / (2*bt))
        assert abs(cost-expected) < 1e-12
        et = f.T @ rng.normal(size=len(f))
        # Add a harmonic circulation as well as contractible transverse curl.
        et += np.array([.3 if j == 0 else 0 for _, j in edges])
        assert norm(g.T @ et) < 1e-12
        residual = float((longitudinal+et) @ aa @ (longitudinal+et) / 2 -
                         cost - et @ aa @ et / 2)
        assert abs(residual) < 1e-11
        charge_rows.append(dict(length=length, beta_t=bt, beta_s=bs,
                                kkt_error=norm(kkt-longitudinal),
                                charge_energy=cost, inverse_laplacian_energy=expected,
                                transverse_cross_error=abs(residual)))
    # Fourier matrix kernels on a larger torus, with all three link orientations.
    length, bt, bs = 12, 1., 1.
    momenta = np.array(list(itertools.product(range(length), repeat=3)))
    d = np.exp(2j*np.pi*momenta/length)-1
    lam = np.sum(abs(d)**2, axis=1)
    _, fg = gaussian_functions(bs*lam/bt)
    pl = np.zeros((len(lam), 3, 3), complex)
    active = lam > 0
    pl[active] = d[active, :, None]*d[active, None, :].conj()/lam[active, None, None]
    eye = np.eye(3)[None, :, :]
    ak = (fg[:, None, None]*eye+(1-fg)[:, None, None]*pl)/bt
    bk = (bs*lam*(1+bs*lam/(4*bt))*fg)[:, None, None]*(eye-pl)
    ac = np.fft.ifftn(ak.reshape(length, length, length, 3, 3), axes=(0, 1, 2))
    bc = np.fft.ifftn(bk.reshape(length, length, length, 3, 3), axes=(0, 1, 2))
    assert max(np.max(abs(ac.imag)), np.max(abs(bc.imag))) < 1e-12
    distances = np.max(np.minimum(momenta, length-momenta), axis=1).reshape((length,)*3)
    q, cb = .75, 48.
    shells = []
    for distance in range(length//2+1):
        mask = distances == distance
        ma, mb = float(np.max(abs(ac[mask]))), float(np.max(abs(bc[mask])))
        assert ma <= q**distance/bt+1e-12
        assert mb <= cb*q**max(distance-2, 0)+1e-12
        shells.append(dict(distance=distance, max_A_entry=ma, max_B_entry=mb))
    mu = -np.log(q)/2
    z = q*np.exp(mu)
    shell_sum = 3+72*z*(1+z)/(1-z)**3+6*z/(1-z)
    actual_a = np.max(np.sum(abs(ac)*np.exp(mu*distances)[..., None, None], axis=(0,1,2,4)))
    actual_b = np.max(np.sum(abs(bc)*np.exp(mu*distances)[..., None, None], axis=(0,1,2,4)))
    assert actual_a <= shell_sum/bt
    assert actual_b <= cb*q**-2*shell_sum
    return dict(charge_sectors=charge_rows, spatial_kernel_shells=shells,
                weighted_kernel=dict(mu=mu, A_row=float(actual_a), B_row=float(actual_b),
                                     A_bound=shell_sum/bt, B_bound=cb*q**-2*shell_sum))


def green_and_covariance_checks():
    # Independent heat-kernel representation of the infinite cubic Green
    # function: integrate exp(-t Delta) via three modified Bessel functions.
    def green(x):
        return quad(lambda t: np.prod(ive(np.asarray(x), 2*t)),
                    0, np.inf, epsabs=2e-11, limit=250)[0]
    g0 = green((0, 0, 0))
    g1 = green((1, 0, 0))
    assert abs(6*(g0-g1)-1) < 2e-9
    samples = []
    for n in (2, 4, 8, 16, 32):
        value = green((n, 0, 0))
        scaled = 4*np.pi*n*value
        # This finite asymptotic check does not prove the rate in (D3).
        assert abs(scaled-1) < .4/n
        samples.append(dict(distance=n, green=value, scaled_coulomb=scaled))
    covariance = []
    for bt, bs, lam in ((.7, 1.8, .02), (2., .3, 7.), (1., 1., 12.)):
        r = bs*lam/bt
        omega, fg = (float(v) for v in gaussian_functions(r))
        aa, bb = fg/bt, bs*lam*(1+r/4)*fg
        position = 1/(2*np.sqrt(bs*bt)*np.sqrt(lam)*np.sqrt(1+r/4))
        momentum = np.sqrt(bs*bt)*np.sqrt(lam)*np.sqrt(1+r/4)/2
        assert abs(position-np.sqrt(aa/bb)/2) < 1e-12
        assert abs(momentum-np.sqrt(bb/aa)/2) < 1e-12
        assert abs(position*momentum-.25) < 1e-12
        assert abs((aa*momentum+bb*position)/2-omega/2) < 1e-12
        covariance.append(dict(beta_t=bt, beta_s=bs, lam=lam, x_variance=position,
                               p_variance=momentum, vacuum_energy=omega/2))
    return dict(green_origin=g0, discrete_source_residual=abs(6*(g0-g1)-1),
                coulomb_samples=samples, oscillator_covariances=covariance)


def main():
    result = dict(inverse_response=inverse_response_checks(),
                  gaussian_transfer=oscillator_checks(),
                  cubic_locality=cubic_and_locality_checks(),
                  charge_and_kernels=charge_and_kernel_checks(),
                  green_and_covariance=green_and_covariance_checks(),
                  status="author_checked_finite_identities_only",
                  compact_clock_phase="not_established")
    print(json.dumps(result, indent=2))
    print('per_element: finite 4x4 inverse-log identities, oscillator kernel eigenfunctions and explicit Gaussian coefficient formulas checked numerically.')
    print('per_site: full gradient/curl incidence on L3/L4 tori and L12 three-orientation spatial kernels.')
    print('per_mode: all finite cubic eigenmodes, zero-mode coefficient limit, selected oscillator covariances and infrared samples.')
    print('per_block: polynomial tails, weighted row bounds, charge KKT solves and independent Bessel Green-function samples.')
    print('lattice_wide: checked and not executed — volume-uniform Gaussian coefficient/Weyl bounds and Coulomb asymptotic rely on written proofs; no compact phase or native Record law simulated.')
    print('TOTAL: PASS=5 FAIL=0')


if __name__ == "__main__":
    main()
