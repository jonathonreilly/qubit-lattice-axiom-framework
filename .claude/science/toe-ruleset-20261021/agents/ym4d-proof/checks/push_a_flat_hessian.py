#!/usr/bin/env python3
"""Two checks of the flat Decision-4 conditional Hessian, SU(2), d=4.

Direct nonlinear contour evaluation vs the derived quadratic form, then
Bloch matrices on a one-block cell in a block-root Dirichlet gauge.  The
momentum grid is diagnostic; compactness, not this grid, proves the gap.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
import itertools
import math
import resource
import sys
import numpy as np
from scipy import sparse
from scipy.special import ive

L = 3
D = 4
ROOT = (1, 1, 1, 1)
PERMS = list(itertools.permutations(range(D)))
SITES = list(itertools.product(range(L), repeat=D))
INDEX = {x: i for i, x in enumerate(SITES)}


def guard():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    value = int(value if sys.platform == "darwin" else 1024 * value)
    if value >= 1_000_000_000:
        raise RuntimeError(f"RSS exceeds 1GB: {value}")
    return value


def walk(start, end, order):
    x = list(start)
    edges = []
    for axis in order:
        while x[axis] != end[axis]:
            sign = 1 if end[axis] > x[axis] else -1
            if sign == 1:
                edges.append((tuple(x), axis, 1))
                x[axis] += 1
            else:
                x[axis] -= 1
                edges.append((tuple(x), axis, -1))
    assert tuple(x) == tuple(end)
    return edges


def contours(mu):
    out = []
    root2 = list(ROOT)
    root2[mu] += L
    for sigma in PERMS:
        for y in SITES:
            y2 = list(y)
            y2[mu] += L
            first = walk(ROOT, y, sigma)
            middle = walk(y, y2, [mu])
            last = walk(root2, y2, sigma)
            out.append(first + middle + [(x, a, -sgn) for x, a, sgn in reversed(last)])
    return out


def qmul(a, b):
    # Matrices are q0 I+i q.sigma, so the vector cross term has a minus sign.
    scalar = a[:, :1]*b[:, :1] - np.sum(a[:, 1:]*b[:, 1:], axis=1, keepdims=True)
    vector = a[:, :1]*b[:, 1:] + b[:, :1]*a[:, 1:] - np.cross(a[:, 1:], b[:, 1:])
    return np.concatenate([scalar, vector], axis=1)


def nonlinear_check():
    paths = contours(0)
    keys = sorted({(x, a) for p in paths for x, a, sign in p})
    rng = np.random.default_rng(20261030)
    fields = {key: rng.normal(size=3) / 4 for key in keys}
    path_a = np.array([sum((sign*fields[(x, a)] for x, a, sign in p), np.zeros(3)) for p in paths])
    avg_sq = float(np.mean(np.sum(path_a**2, axis=1)))
    avg = np.mean(path_a, axis=0)
    avg_mean_sq = float(avg @ avg)
    steps = []
    for slot in range(max(map(len, paths))):
        steps.append(np.array([p[slot][2]*fields[(p[slot][0], p[slot][1])]
                               if slot < len(p) else np.zeros(3) for p in paths]))

    def mean_quat(eps):
        q = np.zeros((len(paths), 4))
        q[:, 0] = 1
        for vectors in steps:
            length = np.linalg.norm(vectors, axis=1)
            theta = eps * length
            fac = np.divide(np.sin(theta), length, out=np.full_like(length, eps), where=length != 0)
            e = np.concatenate([np.cos(theta)[:, None], vectors*fac[:, None]], axis=1)
            q = qmul(q, e)
        assert np.max(abs(np.sum(q*q, axis=1)-1)) < 2e-12
        return q.mean(axis=0)

    def log_a(s):
        return math.log(2) + math.log(float(ive(1, s))) - math.log(s)

    def energy_diff(t, eps):
        m = mean_quat(eps)
        r = float(np.linalg.norm(m))
        # r-m0 = |m_vec|^2/(r+m0), avoiding cancellation at small eps.
        return t*float(m[1:] @ m[1:])/(r+m[0]) + log_a(t*r)-log_a(t)

    rows = []
    for t in [0.3, 1, 10, 100]:
        alpha = float(ive(2, t)/ive(1, t))
        predicted = t*((1-alpha)*avg_sq + alpha*avg_mean_sq)
        for eps in [0.002, 0.001, 0.0005]:
            measured = (energy_diff(t, eps)+energy_diff(t, -eps))/eps**2
            relative = abs(measured/predicted-1)
            assert relative < 2e-5, (t, eps, predicted, measured, relative)
            rows.append((t, eps, predicted, measured, relative))
        guard()
    return rows


def rough_normalized_check():
    # Actual RENEW flux background, varied in a commuting SU(2) subgroup.
    # All paths and their normalizers are evaluated; this is not a prescribed
    # mean proxy.  L=3, kappa=1 is the declared numerical scope.
    paths_by_mu = [contours(mu) for mu in range(4)]
    def means(eps):
        out = []
        for paths in paths_by_mu:
            q = np.zeros((len(paths), 4))
            q[:, 0] = 1
            for slot in range(max(map(len, paths))):
                link = np.zeros_like(q)
                link[:, 0] = 1
                for row, path in enumerate(paths):
                    if slot >= len(path):
                        continue
                    x, direction, orient = path[slot]
                    if direction == 0:
                        sign = (-1)**x[1]
                        link[row, 0] = sign*math.cos(eps)
                        link[row, 3] = orient*math.sin(eps)
                q = qmul(q, link)
            out.append(q.mean(axis=0))
        return out

    def log_a(s):
        return math.log(2) + math.log(float(ive(1, s))) - math.log(s)

    def delta_action(u, eps):
        evaluated = means(eps)
        s_total = -2*u*math.sin(eps)**2
        for mu, m in enumerate(evaluated):
            sign = 1 if mu != 1 else (-1)**((L-1)//2)
            h = sign*m[0]
            r = float(np.linalg.norm(m))
            r0 = 1/L if mu < 2 else 1
            gap = float(m[1:] @ m[1:])/(r+h)
            s_total += (u*gap+log_a(u*r)-log_a(u*r0))/L**4
        expected_m1 = np.array([math.cos(L*eps)/L, 0, 0, math.sin(L*eps)])
        expected_m2 = sum((-1)**s*math.cos(2*s*eps)
                          for s in range(-(L-1)//2, (L-1)//2+1))/L
        assert np.max(abs(evaluated[0]-expected_m1)) < 2e-12
        assert abs(evaluated[1][0]-expected_m2) < 2e-12
        assert np.max(abs(evaluated[1][1:])) < 2e-12
        return s_total

    rows = []
    for u in [1, 10, 100]:
        alpha = float(ive(2, u/L)/ive(1, u/L))
        prediction = u*(-4+(2*L**2-1+(L**2-1)**2*alpha)/L**5)
        eps = 0.0005
        measured = (delta_action(u, eps)+delta_action(u, -eps))/eps**2
        assert prediction < 0 and measured < 0
        assert abs(measured/prediction-1) < 2e-5
        rows.append((u, prediction, measured, abs(measured/prediction-1)))
        guard()
    return rows


def bloch_edge(x, mu, k):
    block = np.floor_divide(np.array(x), L)
    within = tuple(np.mod(x, L))
    return 4*INDEX[within]+mu, np.exp(1j*float(np.dot(k, block)))


def bloch_site(x, k):
    block = np.floor_divide(np.array(x), L)
    within = tuple(np.mod(x, L))
    return INDEX[within], np.exp(1j*float(np.dot(k, block)))


def path_matrix(paths, k):
    rows, cols, vals = [], [], []
    for row, path in enumerate(paths):
        for x, mu, sign in path:
            col, phase = bloch_edge(x, mu, k)
            rows.append(row)
            cols.append(col)
            vals.append(sign*phase)
    return sparse.coo_matrix((vals, (rows, cols)), shape=(len(paths), 4*L**4)).tocsr()


def matrices(k):
    n = L**4
    d0 = np.zeros((4*n, n), complex)
    d1 = np.zeros((6*n, 4*n), complex)
    for x in SITES:
        for mu in range(4):
            xp = list(x)
            xp[mu] += 1
            col, phase = bloch_site(xp, k)
            row = 4*INDEX[x]+mu
            d0[row, col] += phase
            d0[row, INDEX[x]] -= 1
        for orient, (mu, nu) in enumerate(itertools.combinations(range(4), 2)):
            row = 6*INDEX[x]+orient
            xm, xn = list(x), list(x)
            xm[mu] += 1
            xn[nu] += 1
            for base, direction, sign in [(x, mu, 1), (xm, nu, 1), (xn, mu, -1), (x, nu, -1)]:
                col, phase = bloch_edge(base, direction, k)
                d1[row, col] += sign*phase

    direct = []
    gram = np.zeros((4*n, 4*n), complex)
    for mu in range(4):
        r = path_matrix(contours(mu), k)
        direct.append(np.asarray(r.mean(axis=0)).ravel())
        gram += (r.conj().T @ r).toarray()/r.shape[0]
    q = np.array(direct)

    # Independent cancellation formula: axial legs average to h(X)-h(X+mu).
    h = np.asarray(path_matrix([walk(ROOT, y, sigma) for sigma in PERMS for y in SITES], k).mean(axis=0)).ravel()
    factored = np.zeros_like(q)
    for mu in range(4):
        for y in SITES:
            yp = list(y)
            yp[mu] += L
            for x, a, sign in walk(y, yp, [mu]):
                col, phase = bloch_edge(x, a, k)
                factored[mu, col] += sign*phase/n
        factored[mu] += (1-np.exp(1j*k[mu]))*h
    assert np.max(abs(q-factored)) < 2e-13
    assert np.max(abs(d1 @ d0)) < 2e-13
    expected = np.zeros((4, n), complex)
    expected[:, INDEX[ROOT]] = np.exp(1j*np.array(k))-1
    assert np.max(abs(q @ d0-expected)) < 3e-13

    nonroot = [i for i in range(n) if i != INDEX[ROOT]]
    gauge = d0[:, nonroot] @ d0[:, nonroot].conj().T
    h0 = d1.conj().T @ d1 + gauge
    # For t>=3, alpha(t)>=1-3/(2t)>=1/2. Use kappa=1 in this diagnostic.
    h_lower = h0 + 0.5*q.conj().T @ q
    eig_lower = np.linalg.eigvalsh(h_lower)
    assert eig_lower[0] > 0
    # Check actual normalized Hessian at t=3 and t=100.
    actual = []
    for t in [3, 100]:
        alpha = float(ive(2, t)/ive(1, t))
        h = h0 + alpha*q.conj().T @ q + (1-alpha)*gram
        eig = np.linalg.eigvalsh(h)
        assert eig[0] >= eig_lower[0]-1e-10
        actual.append((t, float(eig[0]), float(eig[-1])))
    # Separate exact tree-gauge restriction; no artificial divergence term.
    tree_columns = set()
    for x in SITES:
        if x == ROOT:
            continue
        axis = next(mu for mu in range(4) if x[mu] != ROOT[mu])
        parent = list(x)
        parent[axis] += 1 if x[axis] < ROOT[axis] else -1
        base = x if x[axis] < parent[axis] else tuple(parent)
        tree_columns.add(4*INDEX[base]+axis)
    assert len(tree_columns) == n-1
    free = [col for col in range(4*n) if col not in tree_columns]
    dt = d1[:, free]
    qt = q[:, free]
    tree_lower = dt.conj().T @ dt + 0.5*qt.conj().T @ qt
    tree_minimum = float(np.linalg.eigvalsh(tree_lower)[0])
    assert tree_minimum > 0
    guard()
    return float(eig_lower[0]), actual, tree_minimum


def main():
    guard()
    print("Nonlinear SU(2) mean: (t, epsilon, predicted Hessian, finite difference, relative error)")
    for row in nonlinear_check():
        print(row)
    print("Rough flux, full normalized conditional action: (u, predicted Hessian/fine cell, finite difference, relative error)")
    for row in rough_normalized_check():
        print(row)
    print("4D L=3 Bloch fibers, kappa=1, exact block-root Dirichlet gauge.")
    print("(k, Dirichlet-gauge lower eigenvalue, actual t=3/100 endpoints, tree-gauge lower eigenvalue)")
    momenta = [(0, 0, 0, 0), (0.01, 0, 0, 0), (math.pi/3, 0, 0, 0),
               (math.pi, 0, 0, 0), (math.pi, math.pi, 0, 0),
               (math.pi/2, math.pi/3, math.pi/5, math.pi/7),
               (math.pi, math.pi, math.pi, math.pi)]
    for k in momenta:
        low, actual, tree_minimum = matrices(k)
        print((k, low, actual, tree_minimum))
    print(f"Peak RSS bytes: {guard()}; limit 1000000000; BLAS threads 1.")
    print("The momentum grid is not a uniform spectral certificate.")
    print("Only the explicit rough flux direction is checked, not arbitrary history sectors.")
    print("No rough-core extension or RG regeneration tested.")


if __name__ == "__main__":
    main()
