"""Finite challenges for the block-6 analytic derivation; no phase numerics."""
from __future__ import annotations
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh


def close(a, b, tol=3e-10):
    err = float(np.max(np.abs(np.asarray(a) - np.asarray(b))))
    assert err < tol, (err, tol)
    return err


def heat(theta, beta, power=1, derivatives=False):
    theta = np.asarray(theta)
    modes = np.arange(-24, 25)
    c = np.exp(-power * modes * modes / (2 * beta))
    phase = np.exp(1j * theta[..., None] * modes)
    value = (phase @ c).real
    if not derivatives:
        return value
    first = (phase @ (1j * modes * c)).real
    second = (phase @ (-modes * modes * c)).real
    return value, first, second


def normalize_transfer(raw):
    val, vec = eigh(raw)
    assert val[0] > 0
    omega = vec[:, -1]
    omega *= np.sign(omega.sum())
    assert omega.min() > 0
    return raw / val[-1], omega, float(val[-2] / val[-1])


def covariance(T, omega, F, G, separation):
    KF, KG = T * F, T * G
    EF, EG = omega @ KF @ omega, omega @ KG @ omega
    return omega @ KF @ np.linalg.matrix_power(T, separation - 1) @ KG @ omega - EF * EG


def pf_checks():
    rng = np.random.default_rng(913206)
    records = []
    for n in (2, 3, 7):
        A = rng.uniform(.1, 1, (n, n))
        T, omega, ratio = normalize_transfer(A @ A.T + .3 * np.eye(n))
        proj = np.outer(omega, omega)
        worst = 0.0
        for _ in range(20):
            F = rng.uniform(-1, 1, (n, n)) + 1j * rng.uniform(-1, 1, (n, n))
            G = rng.uniform(-1, 1, (n, n)) + 1j * rng.uniform(-1, 1, (n, n))
            F /= max(1., np.max(np.abs(F)))
            G /= max(1., np.max(np.abs(G)))
            KF, KG = T * F, T * G
            assert np.linalg.norm(KF @ omega) <= 1 + 1e-12
            assert np.linalg.norm(KF.conj().T @ omega) <= 1 + 1e-12
            for sep in (1, 2, 3, 5):
                c = covariance(T, omega, F, G, sep)
                direct = omega @ KF @ (np.linalg.matrix_power(T, sep - 1) - proj) @ KG @ omega
                close(c, direct)
                bound = ratio ** (sep - 1)
                assert abs(c) <= bound + 1e-12
                worst = max(worst, float(abs(c) / bound))
        records.append(dict(states=n, spectral_ratio=ratio, largest_bound_fraction=worst))
    # Saturation fixes the time separation: the second endpoint of the first
    # slab and the first endpoint of the second slab are sep-1 steps apart.
    r = .4
    T = np.array([[1+r, 1-r], [1-r, 1+r]]) / 2
    omega = np.ones(2) / np.sqrt(2)
    spin = np.array([1., -1.])
    F = np.tile(spin, (2, 1))
    G = np.tile(spin[:, None], (1, 2))
    for sep in (1, 2, 4):
        c = covariance(T, omega, F, G, sep)
        close(c, r ** (sep - 1))
        assert c > r ** sep + 1e-12  # the overstrong exponent is false
    return dict(random_checks=records, sharp_slab_exponent='separation_minus_one')


def finite_clock_transfer():
    N, beta_t, beta_s = 5, 1.2, .8
    theta = 2 * np.pi * np.arange(N) / N
    wt, dwt, _ = heat(theta, beta_t, derivatives=True)
    score = dwt / wt
    wt /= wt.mean()
    ws = heat(theta, beta_s)
    diff = (np.arange(N)[:, None] - np.arange(N)[None, :]) % N
    k = wt[diff] / N
    ks = k * score[diff]
    configs = np.array(list(itertools.product(range(N), repeat=4)))
    flux = (configs[:, 0] + configs[:, 1] - configs[:, 2] - configs[:, 3]) % N
    U = (flux[:, None] == np.arange(N)[None, :]).astype(float) / np.sqrt(N**3)
    close(U.T @ U, np.eye(N))
    K, KS = k, ks
    for _ in range(3):
        K = np.kron(K, k)
        KS = np.kron(KS, k)
    d = np.sqrt(ws[flux])
    raw = U.T @ (d[:, None] * K * d[None, :]) @ U
    insertion = U.T @ (d[:, None] * KS * d[None, :]) @ U
    coeff = (np.fft.fft(wt) / N).real
    assert coeff.min() > 0
    first = np.fft.ifft(coeff**4).real
    independent = np.sqrt(ws[:, None] * ws[None, :]) * first[diff]
    close(raw, independent)
    close((d[:, None] * K * d[None, :]) @ U, U @ raw)
    C = float(np.max(np.abs(score)))
    assert np.all(np.abs(insertion) <= C * raw + 1e-12)
    top = eigh(raw, eigvals_only=True)[-1]
    T, omega, ratio = normalize_transfer(raw)
    KF = insertion / top
    assert np.linalg.norm(KF @ omega) <= C + 1e-12
    assert np.linalg.norm(KF.T @ omega) <= C + 1e-12
    # Compare spectral products with an independently enumerated stationary
    # Markov path law. F is the effective physical slab observation, G a
    # different nonsymmetric bounded increment.
    F = KF / T
    G = np.sin(theta[:, None] + .7 * theta[None, :])
    transition = T * omega[None, :] / omega[:, None]
    close(transition.sum(axis=1), np.ones(N))
    pi = omega**2
    close(pi @ transition, pi)
    errors = []
    for sep in (1, 2, 3):
        expectation = 0.0
        for path in itertools.product(range(N), repeat=sep + 2):
            prob = pi[path[0]]
            for a, b in zip(path[:-1], path[1:]):
                prob *= transition[a, b]
            expectation += prob * F[path[0], path[1]] * G[path[sep], path[sep+1]]
        matrix_value = omega @ KF @ np.linalg.matrix_power(T, sep-1) @ (T*G) @ omega
        errors.append(close(expectation, matrix_value))
        cov = covariance(T, omega, F, G, sep)
        assert abs(cov) <= C * ratio**(sep-1) + 1e-12
    # In the continuous circle model, conjugating the derivative insertion by
    # the inverse square root of the heat transfer has eigenvalues i*m.
    # Its norm on modes |m|<=M is M although the original score stays bounded.
    grid = np.linspace(0, 2*np.pi, 1024, endpoint=False)
    w, dw, _ = heat(grid, .5, derivatives=True)
    sup_score = float(np.max(np.abs(dw / w)))
    ratios = []
    for cutoff in (2, 5, 10):
        modes = np.arange(-cutoff, cutoff+1)
        eigen = np.exp(-modes**2 / (2*.5))
        inserted = 1j * modes * eigen
        conjugated = inserted / eigen
        norm = float(np.max(np.abs(conjugated)))
        close(norm, cutoff)
        assert norm > sup_score
        ratios.append(norm)
    return dict(clock_N=N, full_states=N**4, physical_states=N,
                beta_temporal=beta_t, beta_spatial=beta_s,
                spectral_ratio=ratio, insertion_sup_bound=C,
                path_enumeration_errors=errors, fixed_continuous_score_sup=sup_score,
                inverse_sandwich_norms=ratios)


def cube_contact():
    # On the oriented boundary of a cube, Fourier integration imposes one
    # integer m on all six faces. The angle formulation has six face angles
    # whose oriented sum vanishes modulo 2pi. Integrating four unobserved
    # faces is a heat convolution, leaving a two-angle quadrature.
    points = 128
    theta = 2*np.pi*np.arange(points)/points
    rows = []
    for beta in (.8, 1.7, 2.6):
        w, dw, ddw = heat(theta, beta, derivatives=True)
        assert w.min() > 0
        score = dw/w
        modes = np.arange(-24, 25)
        weights = np.exp(-6 * modes**2 / (2*beta))
        Z = weights.sum()
        integer_variance = float((modes**2 @ weights)/Z)
        convolution4 = heat(-theta[:, None]-theta[None, :], beta, power=4)
        off = float(np.mean(dw[:, None]*dw[None, :]*convolution4)/Z)
        convolution5 = heat(-theta, beta, power=5)
        diagonal = float(np.mean(dw**2/w*convolution5)/Z)
        kappa = float(np.mean((-ddw+dw**2/w)*convolution5)/Z)
        alternate_Z = float(np.mean(w*convolution5))
        close(alternate_Z, Z)
        close(off, -integer_variance)
        close(kappa-diagonal, integer_variance)
        assert abs(diagonal+integer_variance) > 1e-3  # no diagonal shortcut
        assert abs(off-integer_variance) > 1e-3       # sign matters
        cov = np.full((6,6), off)
        np.fill_diagonal(cov, diagonal)
        assert np.linalg.eigvalsh(cov).min() > -1e-10
        rows.append(dict(beta=beta, partition=Z, integer_variance=integer_variance,
                         real_score_offdiagonal=off, real_score_variance=diagonal,
                         contact=kappa, smallest_covariance_eigenvalue=float(np.linalg.eigvalsh(cov).min())))
    return rows


def spectral_and_hypothesis_checks():
    # Exact four-dimensional shell identity, then a convergent independent sum.
    for n in range(1, 40):
        assert (2*n+1)**4-(2*n-1)**4 == 64*n**3+16*n
    q = .25
    direct = 1 + sum(((2*n+1)**4-(2*n-1)**4)*q**(n-1) for n in range(1, 80))
    formula = 1+64*(1+4*q+q*q)/(1-q)**4+16/(1-q)**2
    close(direct, formula)
    directional = []
    for eps in (.1, .01, .001):
        vals = []
        for axis in range(4):
            k = np.zeros(4)
            k[axis] = eps
            symbol = np.abs(np.exp(1j*k)-1)**2
            vals.append(float((symbol[0]+symbol[1])/symbol.sum()))
        close(vals, [1,1,0,0])
        directional.append(vals)
    # Failure to remove the FULL invariant space: a centered vector can be
    # orthogonal to the constant state while still having zero energy.
    T = np.diag([1., 1., .2])
    omega = np.array([1., 1., 0.])/np.sqrt(2)
    centered = np.array([1., -1., 0.])/np.sqrt(2)
    close(centered @ omega, 0)
    for t in (1, 3, 10):
        close(centered @ np.linalg.matrix_power(T,t) @ centered, 1)
    # Anisotropic Gaussian OU field: h(x)=(1+|x|^2)^-1 is a positive mixture
    # of Gaussian kernels. Bounded sin fields have covariance e^-1 sinh(h).
    # Time evolution scales the first Gaussian chaos by a fixed r<1; all
    # nonconstant chaos levels have eigenvalues r^n. Spatial decay is power law.
    r = .3
    examples = []
    for distance in (1, 3, 10, 30):
        h = 1/(1+distance**2)
        spatial = math.exp(-1)*math.sinh(h)
        assert spatial >= math.exp(-1)*h
        temporal = math.exp(-1)*math.sinh(r**distance)
        assert temporal <= r**distance
        examples.append(dict(distance=distance, spatial_covariance=spatial,
                             temporal_covariance=temporal))
    return dict(shell_sum=direct, multiplier_axis_values=directional,
                centered_invariant_vector_detected=True,
                anisotropic_OU_ratio=r, anisotropic_examples=examples)


def main():
    result = dict(status='personal_finite_checks_pass',
                  finite_transfer=pf_checks(),
                  clock_transfer=finite_clock_transfer(),
                  cube_score_contact=cube_contact(),
                  spectral_hypotheses=spectral_and_hypothesis_checks(),
                  limits='No numerical massless-phase proof; FS and Villain monotonicity are named literature inputs, and the general transfer implication rests on the written proof.')
    target = Path(__file__).with_name('BLOCK6_TRANSFER_CONTACT_CHECK.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
