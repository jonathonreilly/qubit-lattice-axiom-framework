#!/usr/bin/env python3
"""Actual flat soft-chain tests: absolute walks and the coarse Gaussian action.

This is a quadratic diagnostic, not an inherited nonlinear RG computation.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import sys
sys.dont_write_bytecode = True
import itertools
import math
import resource
from fractions import Fraction
import numpy as np
from scipy.special import ive
from push_a_flat_hessian import L, ROOT, SITES, INDEX, contours, path_matrix, bloch_edge


def guard():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    value = int(value if sys.platform == "darwin" else 1024*value)
    if value >= 1_000_000_000:
        raise RuntimeError(f"RSS limit exceeded: {value}")
    return value


def free_columns():
    tree = set()
    for x in SITES:
        if x == ROOT:
            continue
        mu = next(a for a in range(4) if x[a] != ROOT[a])
        parent = list(x)
        parent[mu] += 1 if x[mu] < ROOT[mu] else -1
        base = x if x[mu] < parent[mu] else tuple(parent)
        tree.add(4*INDEX[base]+mu)
    return [col for col in range(4*L**4) if col not in tree]


PATHS = [contours(mu) for mu in range(4)]
FREE = free_columns()


def actual_matrices(k, with_gram=False):
    curl = np.zeros((6*L**4, 4*L**4), complex)
    for x in SITES:
        for orient, (mu, nu) in enumerate(itertools.combinations(range(4), 2)):
            row = 6*INDEX[x]+orient
            xm, xn = list(x), list(x)
            xm[mu] += 1
            xn[nu] += 1
            for base, direction, sign in [(x, mu, 1), (xm, nu, 1), (xn, mu, -1), (x, nu, -1)]:
                column, phase = bloch_edge(base, direction, k)
                curl[row, column] += sign*phase
    q, gram = [], np.zeros((len(FREE), len(FREE)), complex)
    for paths in PATHS:
        r = path_matrix(paths, k)[:, FREE]
        q.append(np.asarray(r.mean(axis=0)).ravel())
        if with_gram:
            gram += (r.conj().T@r).toarray()/r.shape[0]
    curl = curl[:, FREE]
    guard()
    return curl.conj().T@curl, np.array(q), gram


def comparison(h):
    off = h.copy()
    np.fill_diagonal(off, 0)
    return np.diag(np.diag(h).real)-abs(off)


def walk_test():
    w, q, gram = actual_matrices((0, 0, 0, 0), with_gram=True)
    w, q, gram = w.real, q.real, gram.real
    q_integer = np.array([[int(column % 4 == mu) for column in FREE]
                          for mu in range(4)], dtype=np.int64)
    assert np.max(abs(q-q_integer/L**3)) < 1e-13
    curl_integer = np.zeros((6*L**4, 4*L**4), dtype=np.int64)
    for x in SITES:
        for orient, (mu, nu) in enumerate(itertools.combinations(range(4), 2)):
            row = 6*INDEX[x]+orient
            xm, xn = list(x), list(x)
            xm[mu] += 1
            xn[nu] += 1
            for base, direction, sign in [(x, mu, 1), (xm, nu, 1), (xn, mu, -1), (x, nu, -1)]:
                within = tuple(v % L for v in base)
                curl_integer[row, 4*INDEX[within]+direction] += sign
    curl_integer = curl_integer[:, FREE]
    w_integer = curl_integer.T@curl_integer
    assert np.max(abs(w-w_integer)) < 1e-13
    h_integer = L**6*w_integer+q_integer.T@q_integer
    off_integer = h_integer.copy()
    np.fill_diagonal(off_integer, 0)
    ray_numerator = int(np.trace(h_integer)-np.sum(abs(off_integer)))
    rayleigh = Fraction(ray_numerator, L**6*len(FREE))
    assert rayleigh < 0
    same = different = 0
    for i, ci in enumerate(FREE):
        for j, cj in enumerate(FREE):
            if i != j and w_integer[i, j] != 0:
                assert abs(w_integer[i, j]) == 1
                if ci % 4 == cj % 4:
                    same += 1
                else:
                    different += 1
    assert (same, different) == (1392, 2256)
    print(f"L={L}, kappa=1, zero Bloch momentum, tree-gauge free coordinates={len(FREE)}.")
    print(f"Exact integer counts: same-direction off-diagonal incidences {same}, different-direction {different}, scaled trace {np.trace(h_integer)}, scaled absolute off-diagonal sum {np.sum(abs(off_integer))}.")
    print(f"Exact comparison-matrix Rayleigh quotient at t=infinity: {rayleigh} = {float(rayleigh):.12g}.")
    ell = 5*L-4
    sufficient_u = 2*(24*ell**2+2/3)/(-float(rayleigh))
    print(f"Conservative finite-u threshold for a negative comparison Rayleigh quotient: {sufficient_u:.12g}.")
    print("(u, min eigenvalue H, comparison Rayleigh quotient, signed Neumann norm, absolute Neumann radius)")
    for u in [3., 1000., 10000.]:
        alpha = float(ive(2, u)/ive(1, u))
        h = w+alpha*(q.T@q)+(1-alpha)*gram+(2/(3*u))*np.eye(len(FREE))
        eig = np.linalg.eigvalsh(h)
        comp_ray = float(np.sum(comparison(h))/len(FREE))
        bound = float(rayleigh)+(24*ell**2+2/3)/u
        assert comp_ray <= bound+1e-10
        j = 27+8*ell**2
        c = np.eye(len(FREE))-h/j
        signed = float(max(abs(np.linalg.eigvalsh(c))))
        absolute = float(np.linalg.eigvalsh(abs(c))[-1])
        assert eig[0] > 0 and signed < 1
        if u >= sufficient_u:
            assert comp_ray < 0 and absolute > 1
        print((u, float(eig[0]), comp_ray, signed, absolute))
    print("The folded comparison upper-bounds the actual periodic positive-vector Rayleigh quotient; no uniform spectral gap is inferred from this grid.")
    guard()


def schur_test():
    a_l = (L**2-1)/(6*L**2)
    print("Axial transverse Schur complement: (kappa, k, actual, alias sum, rational prediction, relative error)")
    for kappa in [1., 1/a_l, 10.]:
        for angle in [math.pi/6, math.pi/2, math.pi]:
            w, q, _ = actual_matrices((angle, 0, 0, 0))
            h = w+kappa*(q.conj().T@q)
            effective = kappa*np.eye(4)-kappa**2*q@np.linalg.solve(h, q.conj().T)
            actual = float(effective[1, 1].real)
            s = 4*math.sin(angle/2)**2
            aliases = [(angle+2*math.pi*n)/L for n in range(L)]
            filt = [sum(np.exp(1j*p*r) for r in range(L))/L for p in aliases]
            var = sum(abs(f)**2/(4*math.sin(p/2)**2) for p, f in zip(aliases, filt))/L**2
            alias_answer = 1/(1/kappa+var)
            prediction = s/(1+(1/kappa-a_l)*s)
            error = abs(actual/prediction-1)
            assert error < 5e-11 and abs(alias_answer/prediction-1) < 2e-14
            assert np.max(abs(effective[0, :])) < 1e-11
            print((kappa, angle, actual, alias_answer, prediction, error))
            guard()
    tau = 0.
    target = L**2/(L**2-1)-1/6
    for depth in range(1, 13):
        tau = 1-a_l+tau/L**2
        assert abs(tau-target*(1-L**(-2*depth))) < 3e-15
    print(f"Axial Gaussian flow at kappa=1: tau_1={1-a_l:.12g}, tau_*={target:.12g}; 12-step algebra checked.")
    print("The scalar axial flow is not a full four-dimensional matrix-kernel flow, a nonlinear history return, or an activity norm certificate.")


if __name__ == "__main__":
    guard()
    walk_test()
    schur_test()
    print(f"Peak RSS bytes: {guard()}; ceiling 1000000000; BLAS threads 1.")
