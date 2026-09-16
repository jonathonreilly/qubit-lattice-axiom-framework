#!/usr/bin/env python3
"""Finite checks of the compact doubled-ground argument, not a phase computation."""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import hashlib
import itertools
import json
import time
import numpy as np
from scipy.linalg import eigh


def model(cutoff, g, interactions):
    labels = list(itertools.product(range(-cutoff, cutoff + 1), repeat=2))
    lookup = {x: i for i, x in enumerate(labels)}
    n = np.array(labels, dtype=float)
    metric = np.array([[4., -1.], [-1., 4.]])
    H = np.diag(.5 * g*g * np.einsum('ni,ij,nj->n', n, metric, n))
    def character(a):
        out = np.zeros_like(H)
        for i, x in enumerate(labels):
            for sign in [-1, 1]:
                y = tuple(x[j] + sign*a[j] for j in range(2))
                if y in lookup:
                    out[lookup[y], i] += .5
        return out
    for a, coupling in interactions:
        H -= coupling * character(a)
    eigen, vectors = eigh(H)
    psi = vectors[:, 0]
    if psi[lookup[(0, 0)]] < 0:
        psi *= -1
    return labels, lookup, n, H, character, eigen, vectors, psi


def connected_check():
    probes = [(1, 0), (0, 1), (1, 1), (1, -1), (2, -1)]
    interactions = [((1, 0), 1.2), ((0, 1), .8),
                    ((1, 1), .3), ((1, -1), .2)]
    rows = []
    for g in [.55, 1.1]:
        previous = None
        for cutoff in [5, 7]:
            labels, lookup, n, H, char, eig, vec, psi = model(cutoff, g, interactions)
            gaps = eig[1:] - eig[0]
            obs = np.stack([char(a) @ psi for a in probes], axis=1)
            means = psi @ obs
            excit = vec[:, 1:].T @ obs
            covariances = []
            for tau in [0., .1, .7, 2.]:
                cov = excit.T @ (np.exp(-tau*gaps)[:, None] * excit)
                covariances.append(float(cov.min()))
                assert cov.min() >= -2e-12
            deriv = 2 * excit.T @ (excit / gaps[:, None])
            assert deriv.min() >= -2e-12
            s = np.array([.7, -.4])
            A2 = (n @ s)**2
            cross = (vec[:, 1:].T @ (A2*psi))
            e_deriv = -2 * cross @ (excit / gaps[:, None])
            assert e_deriv.min() >= -2e-12
            eps = 2e-5
            plus = list(interactions)
            minus = list(interactions)
            plus[1] = (plus[1][0], plus[1][1]+eps)
            minus[1] = (minus[1][0], minus[1][1]-eps)
            mp = model(cutoff, g, plus)
            mm = model(cutoff, g, minus)
            mu_plus = np.array([mp[-1] @ (mp[4](a) @ mp[-1]) for a in probes])
            mu_minus = np.array([mm[-1] @ (mm[4](a) @ mm[-1]) for a in probes])
            finite_diff = (mu_plus-mu_minus)/(2*eps)
            err = float(np.max(np.abs(finite_diff-deriv[:, 1])))
            assert err < 2e-8
            e_plus = float(np.sum((mp[2]@s)**2 * mp[-1]**2))
            e_minus = float(np.sum((mm[2]@s)**2 * mm[-1]**2))
            e_err = abs((e_plus-e_minus)/(2*eps)-e_deriv[1])
            assert e_err < 2e-8
            # Compression of the *lifted* ground kernel, using its parity rule.
            modes = list(itertools.product(range(-3, 4), repeat=2))
            kernel = np.zeros((len(modes), len(modes)))
            for i, r in enumerate(modes):
                for j, s2 in enumerate(modes):
                    if any((r[k]+s2[k]) % 2 for k in range(2)):
                        continue
                    a = tuple((-s2[k]-r[k])//2 for k in range(2))
                    b = tuple((-s2[k]+r[k])//2 for k in range(2))
                    kernel[i, j] = psi[lookup[a]] * psi[lookup[b]]
            symmetry = float(np.linalg.norm(kernel-kernel.T))
            assert symmetry < 2e-12
            k_min = float(np.linalg.eigvalsh((kernel+kernel.T)/2).min())
            assert k_min >= -2e-12
            row = dict(g=g, cutoff=cutoff, dimension=len(labels),
                       cosine_means=means.tolist(),
                       min_connected_cosine_by_tau=covariances,
                       min_cosine_coupling_derivative=float(deriv.min()),
                       min_electric_square_derivative=float(e_deriv.min()),
                       cosine_finite_difference_error=err,
                       electric_square_finite_difference_error=e_err,
                       lifted_kernel_compression_min_eigenvalue=k_min,
                       lifted_kernel_symmetry_error=symmetry)
            if previous is not None:
                row['cutoff_change_cosine_means'] = float(np.max(np.abs(means-previous)))
                assert row['cutoff_change_cosine_means'] < 2e-7
            previous = means
            rows.append(row)
    return rows


def covering_trace_check():
    beta, U, cutoff = 1.3, .7, 18
    n = np.arange(-cutoff, cutoff+1)
    original = float(np.exp(-beta*U*n*n/2).sum()**2)
    m, k = np.meshgrid(n, n, indexing='ij')
    weights = np.exp(-beta*U*(m*m+k*k)/4)
    lifted = float(weights.sum())
    physical = float(weights[((m-k) % 2) == 0].sum())
    assert abs(original-physical) < 2e-12
    assert lifted-original > 1.
    return dict(beta=beta, U=U, original_doubled_trace=original,
                unrestricted_lifted_trace=lifted,
                parity_restricted_lifted_trace=physical,
                restriction_error=abs(original-physical),
                scope='free one-angle thermal control; the proof uses ground-state uniqueness')


def negative_coupling_control():
    # A deliberately frustrated sign violates the nonnegative-coupling premise.
    interactions = [((1, 0), -.4), ((0, 1), .6)]
    data = model(6, 1., interactions)
    char, eig, vec, psi = data[4], data[5], data[6], data[7]
    a = vec[:, 1:].T @ (char((1, 1)) @ psi)
    b = vec[:, 1:].T @ (char((0, 1)) @ psi)
    derivative = float(2*np.dot(a, b/(eig[1:]-eig[0])))
    assert derivative < -1e-3
    return dict(derivative_cos_theta1_plus_theta2_wrt_J2=derivative,
                scope='negative J1 violates the theorem hypothesis; no physical phase inference')


def main():
    start = time.time()
    report = dict(scope='finite two-angle electric Galerkin checks and exact covering combinatorics',
                  connected=connected_check(), covering=covering_trace_check(),
                  negative_coupling_control=negative_coupling_control(),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  seconds=time.time()-start)
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
