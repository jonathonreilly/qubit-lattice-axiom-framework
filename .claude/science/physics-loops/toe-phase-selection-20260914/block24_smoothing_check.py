#!/usr/bin/env python3
"""Finite falsifiers for the proposed exact finite-clock smoothing identities.

Author checks only. No infinite-volume, phase, native-law or audit verdict.
The two one-plaquette densities use independent real-space and Fourier sums.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


def cells(d: int, length: int, degree: int):
    return [(tuple(x), tuple(axes))
            for axes in itertools.combinations(range(d), degree)
            for x in itertools.product(*[
                range(length if i in axes else length + 1) for i in range(d)])]


def complex_matrices(d: int, length: int):
    cc = [cells(d, length, k) for k in range(d + 1)]
    incidence = []
    for k in range(1, d + 1):
        ix = {c: i for i, c in enumerate(cc[k - 1])}
        mat = np.zeros((len(cc[k]), len(cc[k - 1])), dtype=np.int64)
        for row, (x, axes) in enumerate(cc[k]):
            for p, axis in enumerate(axes):
                face_axes = axes[:p] + axes[p + 1:]
                upper = list(x)
                upper[axis] += 1
                sign = (-1) ** p
                mat[row, ix[(tuple(upper), face_axes)]] += sign
                mat[row, ix[(x, face_axes)]] -= sign
        incidence.append(mat)
    return cc, incidence


def integer_components(j, edge_cells):
    remaining = set(np.flatnonzero(j).tolist())
    endpoint = {}
    at_vertex = defaultdict(set)
    for e in remaining:
        x, (axis,) = edge_cells[e]
        y = list(x)
        y[axis] += 1
        endpoint[e] = (x, tuple(y))
        for v in endpoint[e]:
            at_vertex[v].add(e)
    answer = []
    while remaining:
        todo = [min(remaining)]
        selected = set()
        while todo:
            e = todo.pop()
            if e in selected:
                continue
            selected.add(e)
            for v in endpoint[e]:
                todo.extend(at_vertex[v] - selected)
        remaining -= selected
        component = np.zeros_like(j)
        component[list(selected)] = j[list(selected)]
        answer.append(component)
    return answer


def fill_current(j, edge_cells, face_cells, sweep_order=None):
    """Coordinate strip homotopy; verification uses the incidence matrix."""
    d = len(edge_cells[0][0])
    face_ix = {c: i for i, c in enumerate(face_cells)}
    current = {edge_cells[i]: int(v) for i, v in enumerate(j) if v}
    points = []
    for x, (axis,) in current:
        y = list(x)
        y[axis] += 1
        points.extend([x, tuple(y)])
    lower = tuple(min(p[i] for p in points) for i in range(d))
    upper = tuple(max(p[i] for p in points) for i in range(d))
    filling = np.zeros(len(face_cells), dtype=np.int64)
    for axis in (range(d) if sweep_order is None else sweep_order):
        projected = defaultdict(int)
        for (x, (direction,)), coefficient in current.items():
            if direction == axis:
                continue
            oriented_axes = tuple(sorted((axis, direction)))
            sign = 1 if axis < direction else -1
            for t in range(lower[axis], x[axis]):
                base = list(x)
                base[axis] = t
                filling[face_ix[(tuple(base), oriented_axes)]] += sign * coefficient
            base = list(x)
            base[axis] = lower[axis]
            projected[(tuple(base), (direction,))] += coefficient
        current = {c: v for c, v in projected.items() if v}
    assert not current, "coordinate contraction did not terminate"
    return filling, lower, upper


def check_chain_and_folding():
    rng = np.random.default_rng(240915)
    results = []
    for d, length in [(2, 2), (3, 2), (4, 1), (4, 2)]:
        cc, inc = complex_matrices(d, length)
        G, D = inc[:2]
        B = inc[2] if d >= 3 else np.zeros((0, len(cc[2])), dtype=int)
        assert not np.any(D @ G)
        assert not np.any(B @ D)
        for _ in range(4):
            # Angles measured in turns make every folding check integer-exact.
            N = 5
            clock = rng.integers(0, N, size=len(cc[1]))
            noise_numer = rng.integers(-37, 38, size=len(cc[1]))
            denom = 10
            unwrapped_numer = 2 * clock + noise_numer
            ell = np.floor_divide(unwrapped_numer, denom)
            theta_numer = unwrapped_numer - denom * ell
            k = rng.integers(-3, 4, size=len(cc[2]))
            kprime = k - D @ ell
            before = D @ (2 * clock) - denom * k
            after = D @ theta_numer - denom * kprime
            assert np.array_equal(after, before + D @ noise_numer)
            assert np.array_equal(B @ kprime, B @ k)
            wrong = D @ theta_numer - denom * (k + D @ ell)
            assert np.any(wrong != before + D @ noise_numer)
        results.append({"dimension": d, "length": length,
                        "cells": [len(c) for c in cc], "fold_trials": 4})
    return results


def check_completion_and_bundle():
    cc, inc = complex_matrices(3, 1)
    D = sp.Matrix(inc[1])
    B = sp.Matrix(inc[2])
    E, P = D.cols, D.rows
    beta, s2 = sp.Rational(7, 5), sp.Rational(5, 448)
    tau = beta * s2
    assert tau == sp.Rational(1, 64)
    A = sp.eye(E) + tau * D.T * D
    M = A / s2
    K = (sp.eye(P) + tau * D * D.T).inv()
    theta = sp.Matrix([sp.Rational((3 * i) % 17, 13) for i in range(E)])
    z = sp.Matrix([sp.Rational((5 * i) % 19 - 9, 7) for i in range(E)])
    image = sp.Matrix([sp.Rational(i - 2, 3) for i in range(P)])
    # 'image' denotes 2pi k here; the quadratic identity holds for every real value.
    Fs = D * theta - image
    r = theta - beta * M.inv() * D.T * Fs
    assert K == sp.eye(P) - beta * D * M.inv() * D.T
    assert D * r - image == K * Fs
    assert theta == r + tau * D.T * (D * r - image)
    assert B * K == B
    lhs = ((theta-z).dot(theta-z) / s2 + beta*(D*z-image).dot(D*z-image))
    rhs = (z-r).dot(M*(z-r)) + beta*Fs.dot(K*Fs)
    assert lhs == rhs
    assert A.det() == (sp.eye(P) + tau * D * D.T).det()
    jac = sp.eye(E) - beta * M.inv() * D.T * D
    assert jac == A.inv()
    # Exact equivariance under a nontrivial bundle-chart shift.
    shift = sp.Matrix([(i % 5) - 2 for i in range(E)])
    newtheta, newimage = theta + shift, image + D * shift
    newr = newtheta - beta * M.inv() * D.T * (D * newtheta - newimage)
    assert newr == r + shift
    return {"edge_dimension": E, "face_dimension": P,
            "det_A": str(A.det()), "tau": str(tau),
            "square_completion": "exact rational", "bundle_inverse": "exact rational"}


def check_poisson_density():
    # The real-space sum and Fourier sum are evaluated separately.
    D = np.array([[1., 1., -1., -1.]])
    beta, s2, N = .7, .4, 3
    delta = 2 * np.pi / N
    A = np.eye(4) + beta * s2 * D.T @ D
    M = A / s2
    invM = np.linalg.inv(M)
    K = np.linalg.inv(np.eye(1) + beta * s2 * D @ D.T)
    zz = delta * np.array(list(itertools.product(range(-6, 7), repeat=4)), dtype=float)
    jj = np.array(list(itertools.product(range(-10, 11), repeat=4)), dtype=float)
    fourier_weights = np.exp(-N*N*np.einsum('bi,ij,bj->b', jj, invM, jj)/2)
    output = []
    for theta, image in [(np.array([.2, 1.1, 2.4, 4.9]), 0),
                         (np.array([5.8, .1, 3.0, .7]), 1),
                         (np.array([.4, 5.1, .8, 1.3]), -1)]:
        Fs = D @ theta - 2*np.pi*image
        r = theta - beta * invM @ D.T @ Fs
        exponent = (np.sum((theta-zz)**2, axis=1)/s2
                    + beta*np.ravel(zz @ D.T-2*np.pi*image)**2)/2
        direct = ((2*np.pi)**4 / (N**4*(2*np.pi*s2)**2)
                  * np.exp(-exponent).sum())
        theta_fourier = np.dot(fourier_weights, np.exp(1j*N*(jj @ r)))
        transformed = (np.exp(-beta*float(Fs @ K @ Fs)/2)
                       * theta_fourier/np.sqrt(np.linalg.det(A)))
        error = abs(direct-transformed)/direct
        assert error < 2e-12, (direct, transformed, error)
        assert abs(theta_fourier.imag) < 2e-13
        assert theta_fourier.real > 0
        output.append({"image": image, "relative_error": float(error),
                       "unnormalized_density": float(direct)})
    return {"beta": beta, "s2": s2, "N": N,
            "real_lattice_points": len(zz), "Fourier_points": len(jj), "cases": output}


def check_one_plaquette_law():
    mp.mp.dps = 75
    tau = mp.mpf(1)/64
    noise_var = 4*tau
    K = 1/(1+noise_var)
    assert K == mp.mpf(16)/17
    cases = []
    for gs in ['1.1', '2.5', '4', '8']:
        g = mp.mpf(gs)
        h = 2*mp.pi/g
        cutoff_x = int(mp.ceil(mp.sqrt(500)/h))+3
        cutoff_j = int(mp.ceil(mp.sqrt(500*34)/g))+3
        lattice = [(h*k, mp.exp(-(h*k)**2/2)) for k in range(-cutoff_x, cutoff_x+1)]
        norm_x = sum(w for x, w in lattice)
        denominator = sum(mp.exp(-g*g*j*j/2) for j in range(-cutoff_j, cutoff_j+1))
        assert abs(norm_x-h**(-1)*mp.sqrt(2*mp.pi)*denominator) < mp.mpf('1e-65')
        max_relative = mp.mpf(0)
        for zs in ['-2', '-.9', '0', '.2', '1.7', '3.1']:
            z = mp.mpf(zs)
            direct = sum(w*mp.exp(-(z-K*x)**2/(2*K*K*noise_var))
                         /mp.sqrt(2*mp.pi*K*K*noise_var) for x, w in lattice)/norm_x
            numerator = sum(mp.exp(-g*g*j*j/34)*mp.cos(g*j*z)
                            for j in range(-cutoff_j, cutoff_j+1))
            transformed = mp.exp(-z*z/(2*K))*numerator/mp.sqrt(2*mp.pi*K)/denominator
            relative = abs(direct-transformed)/direct
            assert relative < mp.mpf('1e-45'), (gs, zs, relative)
            max_relative = max(max_relative, relative)
        second_x = sum(w*x*x for x, w in lattice)/norm_x
        fourth_x = sum(w*x**4 for x, w in lattice)/norm_x
        second_z = K*K*(second_x+noise_var)
        fourth_z = K**4*(fourth_x+6*second_x*noise_var+3*noise_var**2)
        cumulant_x = fourth_x-3*second_x**2
        cumulant_z = fourth_z-3*second_z**2
        assert abs(cumulant_z-K**4*cumulant_x) < mp.mpf('1e-65')
        assert abs(cumulant_z) > mp.mpf('1e-12'), "finite smoothing must not erase non-Gaussianity"
        # Integrating each Fourier mode against the variance-K Gaussian is exact.
        norm_fourier = sum(mp.exp(-g*g*j*j/34-K*g*g*j*j/2)
                           for j in range(-cutoff_j, cutoff_j+1))/denominator
        assert abs(norm_fourier-1) < mp.mpf('1e-65')
        # An independently differentiated Gaussian characteristic gives the moments.
        moment2 = sum(mp.exp(-g*g*j*j/2)*(K-K*K*(g*j)**2)
                      for j in range(-cutoff_j, cutoff_j+1))/denominator
        moment4 = sum(mp.exp(-g*g*j*j/2)*(3*K*K-6*K**3*(g*j)**2+K**4*(g*j)**4)
                      for j in range(-cutoff_j, cutoff_j+1))/denominator
        assert abs(moment2-second_z) < mp.mpf('1e-65')
        assert abs(moment4-fourth_z) < mp.mpf('1e-65')
        cases.append({"g": gs, "maximum_relative_density_error": str(max_relative),
                      "filtered_variance": str(second_z),
                      "filtered_fourth_cumulant": str(cumulant_z)})
    return {"K": "16/17", "noise_variance": "1/16", "precision_digits": mp.mp.dps,
            "cases": cases}


def check_fillings_and_gauge():
    rng = np.random.default_rng(150924)
    cc, inc = complex_matrices(4, 2)
    G, D, B = inc[:3]
    results, nonphysical_difference = [], []
    prime, N = 127, 3
    for trial in range(24):
        seeds = np.zeros(len(cc[2]), dtype=np.int64)
        selected = rng.choice(len(seeds), size=1+(trial % 11), replace=False)
        seeds[selected] = rng.choice([-2, -1, 1, 2], size=len(selected))
        j = D.T @ seeds
        assert not np.any(G.T @ j)
        components = integer_components(j, cc[1])
        for component in components:
            assert not np.any(G.T @ component)
            filling, lo, hi = fill_current(component, cc[1], cc[2])
            assert np.array_equal(D.T @ filling, component), "integer filling has wrong boundary"
            mass = int(np.abs(component).sum())
            area = int(np.abs(filling).sum())
            assert area <= 4*mass*mass
            for face in np.flatnonzero(filling):
                x, axes = cc[2][face]
                for i in range(4):
                    assert lo[i] <= x[i] <= hi[i]-(i in axes)
            negfill, _, _ = fill_current(-component, cc[1], cc[2])
            assert np.array_equal(negfill, -filling)
            for order in [(3, 2, 1, 0), (1, 3, 0, 2)]:
                other_fill, other_lo, other_hi = fill_current(component, cc[1], cc[2], order)
                assert np.array_equal(D.T @ other_fill, component), "alternate sweep has wrong orientation"
                assert np.abs(other_fill).sum() <= 4*mass*mass
                assert other_lo == lo and other_hi == hi
            results.append({"mass": mass, "area": area})
        filling = sum((fill_current(c, cc[1], cc[2])[0] for c in components), np.zeros_like(seeds))
        cube = np.zeros(len(cc[3]), dtype=int)
        cube[trial % len(cube)] = 1
        alternate = filling+B.T @ cube
        assert np.array_equal(D.T @ alternate, j)
        # Rational turns establish filling independence modulo one without trig tolerance.
        psi_numer = rng.integers(-10, 11, size=len(cc[1]))
        image = rng.integers(-2, 3, size=len(cc[2]))
        flux_numer = D @ psi_numer-7*image
        difference = int(N*np.dot(alternate-filling, flux_numer))
        assert difference % 7 == 0
        assert (N*int(np.dot(filling, flux_numer)-np.dot(j, psi_numer))) % 7 == 0
        off_carrier = flux_numer.astype(float)/7 + .013*(B.T @ cube)
        off_phase = np.exp(2j*np.pi*N*np.dot(alternate-filling, off_carrier))
        assert abs(off_phase-1) > .1
        nonphysical_difference.append(float(abs(off_phase-1)))
        # Discrete quadrature of the continuous gauge character factors by vertex.
        for candidate, expected in [(j, 1), (np.eye(1, len(j), trial, dtype=int).ravel(), 0)]:
            divergence = N*(G.T @ candidate)
            assert np.max(np.abs(divergence)) < prime
            factors = [np.mean(np.exp(2j*np.pi*m*np.arange(prime)/prime))
                       for m in divergence if m]
            average = np.prod(factors) if factors else 1.
            assert abs(average-expected) < 1e-12
    return {"random_current_cases": 24, "components": len(results),
            "coordinate_orders_per_component": 3,
            "maximum_area_over_mass_squared": max(v['area']/v['mass']**2 for v in results),
            "minimum_off_carrier_phase_disagreement": min(nonphysical_difference),
            "gauge_character_cases": 48, "gauge_quadrature_order": prime}


def weighted_norm(matrix, left_cells, right_cells):
    x = np.array([c[0] for c in left_cells])
    y = np.array([c[0] for c in right_cells])
    weights = 2.**np.max(np.abs(x[:, None, :]-y[None, :, :]), axis=2)
    weighted = np.abs(matrix)*weights
    return float(max(weighted.sum(axis=0).max(), weighted.sum(axis=1).max()))


def check_massive_geometry():
    cc, inc = complex_matrices(4, 2)
    D = inc[1].astype(float)
    tau = 1/64
    DtD, DDt = D.T @ D, D @ D.T
    A = np.eye(len(cc[1]))+tau*DtD
    K = np.linalg.inv(np.eye(len(cc[2]))+tau*DDt)
    invA = np.linalg.inv(A)
    Cscaled = invA/64-np.eye(len(cc[1]))/128
    edge_weighted = weighted_norm(tau*DtD, cc[1], cc[1])
    face_weighted = weighted_norm(tau*DDt, cc[2], cc[2])
    assert edge_weighted <= 42/64+1e-14
    assert face_weighted <= 44/64+1e-14
    assert np.linalg.eigvalsh(DtD).max() <= 16+1e-12
    assert weighted_norm(invA, cc[1], cc[1]) <= 16/5
    assert weighted_norm(K, cc[2], cc[2]) <= 16/5
    eigC = np.linalg.eigvalsh(Cscaled)
    assert eigC.min() >= 3/640-1e-14
    assert eigC.max() <= 1/128+1e-14
    assert weighted_norm(Cscaled, cc[1], cc[1]) <= 37/640
    return {"edges": len(cc[1]), "faces": len(cc[2]),
            "tau_DtD_weighted": edge_weighted, "tau_DDt_weighted": face_weighted,
            "invA_weighted": weighted_norm(invA, cc[1], cc[1]),
            "K_weighted": weighted_norm(K, cc[2], cc[2]),
            "beta_C_eigenvalue_interval": [float(eigC.min()), float(eigC.max())]}


def cubic_cell_map(cell_list, permutation, signs, length=1):
    index = {cell: i for i, cell in enumerate(cell_list)}
    targets, orientations = [], []
    for x, axes in cell_list:
        y = [0]*len(x)
        for i in range(len(x)):
            y[permutation[i]] = x[i] if signs[i] == 1 else length-x[i]
        mapped_axes = [permutation[i] for i in axes]
        orientation = math.prod(signs[i] for i in axes)
        inversions = sum(mapped_axes[i] > mapped_axes[j]
                         for i in range(len(axes)) for j in range(i+1, len(axes)))
        orientation *= (-1)**inversions
        for i in axes:
            if signs[i] == -1:
                y[permutation[i]] -= 1
        targets.append(index[(tuple(y), tuple(sorted(mapped_axes)))])
        orientations.append(orientation)
    return np.array(targets), np.array(orientations)


def check_cubic_filling_average():
    cc, inc = complex_matrices(4, 1)
    D = inc[1]
    maps = []
    for permutation in itertools.permutations(range(4)):
        for signs in itertools.product([-1, 1], repeat=4):
            e = cubic_cell_map(cc[1], permutation, signs)
            f = cubic_cell_map(cc[2], permutation, signs)
            maps.append((e, f))
    assert len(maps) == 384

    def averaged_fillings(j):
        answer = []
        for (et, es), (ft, fs) in maps:
            transformed = np.zeros_like(j)
            transformed[et] = es*j
            s, _, _ = fill_current(transformed, cc[1], cc[2])
            pulled = fs*s[ft]
            assert np.array_equal(D.T @ pulled, j)
            answer.append(pulled)
        return np.array(answer)

    source = np.zeros(len(cc[2]), dtype=int)
    source[[0, 5, 9]] = [1, -1, 2]
    j = D.T @ source
    fillings = averaged_fillings(j)
    reference = sorted(map(tuple, fillings))
    for h in [0, 39, 151, 299, 383]:
        (et, es), (ft, fs) = maps[h]
        transformed_j = np.zeros_like(j)
        transformed_j[et] = es*j
        transformed_fillings = averaged_fillings(transformed_j)
        pulled = transformed_fillings[:, ft]*fs[None, :]
        assert sorted(map(tuple, pulled)) == reference, "signed cubic filling average is not covariant"
    return {"group_elements": 384, "covariance_controls": 5,
            "distinct_fillings_for_current": len(set(reference)),
            "current_mass": int(np.abs(j).sum()),
            "maximum_area": int(np.abs(fillings).sum(axis=1).max())}


def check_polymer_positivity_and_response():
    # Three polymer supports form a path. Species 0 and 2 are compatible.
    supports = [{0, 1}, {1, 2}, {2, 3}]
    rho = .03
    currents, coefficients = [], []
    for choices in itertools.product([-1, 0, 1], repeat=3):
        active = [i for i, value in enumerate(choices) if value]
        if any(supports[i] & supports[j] for i, j in itertools.combinations(active, 2)):
            continue
        currents.append(choices)
        coefficients.append(rho**len(active))
    currents = np.array(currents, dtype=float)
    coefficients = np.array(coefficients)
    assert len(coefficients) == 11
    # Direct subset enumeration versus an independently coded site-addition recursion.
    activities = {i: 2*rho*np.cos(t) for i, t in enumerate([.1, 2.9, -1.2])}

    def subset_sum(vertices):
        total = 0.
        for chosen in itertools.product([False, True], repeat=3):
            active = [i for i, selected in enumerate(chosen) if selected]
            if any(not supports[i] <= vertices for i in active):
                continue
            if any(supports[i] & supports[j] for i, j in itertools.combinations(active, 2)):
                continue
            total += math.prod(activities[i] for i in active)
        return total

    def recurrence(vertices):
        if not vertices:
            return 1.
        v = min(vertices)
        return (recurrence(vertices-{v})
                + sum(activities[i]*recurrence(vertices-supports[i])
                      for i in range(3) if v in supports[i] and supports[i] <= vertices))

    ratios = []
    for mask in range(16):
        vertices = {i for i in range(4) if mask & (1 << i)}
        assert abs(subset_sum(vertices)-recurrence(vertices)) < 1e-14
        assert subset_sum(vertices) > 0
        for v in vertices:
            ratio = subset_sum(vertices)/subset_sum(vertices-{v})
            assert abs(ratio-1) <= .5
            ratios.append(ratio)
    for v in range(4):
        root_majorant = sum(2*rho*2**(len(support)-1) for support in supports if v in support)
        assert root_majorant <= .5
    assert 1+2*.6*np.cos(np.pi) < 0, "large activity negative control must be visible"
    a = 256.
    epsilon = 58_320_000_000*math.exp(-a/4)
    g2 = 256*a
    q = (37/640)*g2*epsilon
    assert q < 4e-14
    r = q/(1-q)
    second_response = q*(1+r)**2/(1-q)
    assert (1+r)**2+second_response < 3

    # Positive Gaussian integration, checked by quadrature and finite Fourier sums.
    covariance = np.array([[1.1, .14, -.08], [.14, .9, .11], [-.08, .11, 1.3]])
    assert np.linalg.eigvalsh(covariance).min() > .5
    coupling = np.array([[1., 0.], [1., 1.], [0., -2.]])
    w = np.array([.4, -.8])
    frequencies = currents @ coupling
    mode_weight = coefficients*np.exp(-np.einsum('bi,ij,bj->b', currents, covariance, currents)/2)
    phase = np.exp(1j*(frequencies @ w))

    def moments(weights):
        zeroth = weights.sum()
        first = np.einsum('b,bi->i', weights, 1j*frequencies)
        second = np.einsum('b,bi,bj->ij', weights, 1j*frequencies, 1j*frequencies)
        third = np.einsum('b,bi,bj,bk->ijk', weights, 1j*frequencies, 1j*frequencies, 1j*frequencies)
        return zeroth, first, second, third

    z0, z1, z2, z3 = moments(mode_weight*phase)
    exact_gradient = z1/z0
    exact_hessian = z2/z0-np.einsum('i,j->ij', z1, z1)/z0**2
    exact_third = (z3/z0
                   -(np.einsum('ij,k->ijk', z2, z1)+np.einsum('ik,j->ijk', z2, z1)
                     +np.einsum('jk,i->ijk', z2, z1))/z0**2
                   +2*np.einsum('i,j,k->ijk', z1, z1, z1)/z0**3)
    nodes, weights = np.polynomial.hermite.hermgauss(24)
    grid = np.array(list(itertools.product(range(24), repeat=3)))
    normal = np.sqrt(2)*nodes[grid]
    uu = normal @ np.linalg.cholesky(covariance).T
    gaussian_weight = np.prod(weights[grid]/np.sqrt(np.pi), axis=1)
    terms = coefficients[None, :]*np.exp(1j*(uu @ currents.T+(frequencies @ w)[None, :]))
    x0 = terms.sum(axis=1)
    assert np.max(np.abs(x0.imag)) < 1e-14
    assert x0.real.min() > .8
    x1 = np.einsum('ab,bi->ai', terms, 1j*frequencies)
    x2 = np.einsum('ab,bi,bj->aij', terms, 1j*frequencies, 1j*frequencies)
    x3 = np.einsum('ab,bi,bj,bk->aijk', terms, 1j*frequencies, 1j*frequencies, 1j*frequencies)
    U1 = x1/x0[:, None]
    U2 = x2/x0[:, None, None]-np.einsum('ai,aj->aij', x1, x1)/x0[:, None, None]**2
    U3 = (x3/x0[:, None, None, None]
          -(np.einsum('aij,ak->aijk', x2, x1)+np.einsum('aik,aj->aijk', x2, x1)
            +np.einsum('ajk,ai->aijk', x2, x1))/x0[:, None, None, None]**2
          +2*np.einsum('ai,aj,ak->aijk', x1, x1, x1)/x0[:, None, None, None]**3)
    quadrature_z = np.dot(gaussian_weight, x0)
    tilted = gaussian_weight*x0/quadrature_z
    mean1 = np.einsum('a,ai->i', tilted, U1)
    mean2 = np.einsum('a,aij->ij', tilted, U2)
    centered = U1-mean1[None, :]
    hessian = mean2+np.einsum('a,ai,aj->ij', tilted, centered, centered)
    third = (np.einsum('a,aijk->ijk', tilted, U3)
             +np.einsum('a,aij,ak->ijk', tilted, U2, centered)
             +np.einsum('a,aik,aj->ijk', tilted, U2, centered)
             +np.einsum('a,ajk,ai->ijk', tilted, U2, centered)
             +np.einsum('a,ai,aj,ak->ijk', tilted, centered, centered, centered))
    errors = [abs(quadrature_z-z0), np.max(np.abs(mean1-exact_gradient)),
              np.max(np.abs(hessian-exact_hessian)), np.max(np.abs(third-exact_third))]
    assert max(errors) < 2e-11
    omitted_covariance_error = np.max(np.abs(mean2-exact_hessian))
    assert omitted_covariance_error > 1e-3
    # The deterministic MAP substitution generally differs from Gaussian integration.
    u_map = np.zeros(3)
    for _ in range(100):
        terms_map = coefficients*np.exp(1j*(currents @ u_map+frequencies @ w))
        gradient_u = np.real(np.einsum('b,bi->i', terms_map, 1j*currents)/terms_map.sum())
        u_map = covariance @ gradient_u
    map_terms = coefficients*np.exp(1j*(currents @ u_map+frequencies @ w))
    map_gradient = np.einsum('b,bi->i', map_terms, 1j*frequencies)/map_terms.sum()
    map_error = float(np.max(np.abs(map_gradient-exact_gradient)))
    assert map_error > 1e-2
    return {"signed_configurations": len(coefficients), "vertex_regions": 16,
            "deletion_ratio_interval": [min(ratios), max(ratios)],
            "sufficient_q_at_a256": q, "quadrature_points": len(grid),
            "partition_gradient_hessian_third_errors": [float(v) for v in errors],
            "omitting_covariance_error": float(omitted_covariance_error),
            "MAP_substitution_gradient_error": map_error}


def check_macroscopic_sources():
    tau = 1/64
    # Exterior multiplication by the discrete gradient is formed directly.
    pair = list(itertools.combinations(range(4), 2))
    rows = []
    previous = None
    for L in [8, 16, 32, 64, 128, 256]:
        wave = np.array([1, 2, 0, -1])*(2*np.pi/L)
        delta = np.exp(1j*wave)-1
        D = np.zeros((6, 4), dtype=complex)
        for i, (a, b) in enumerate(pair):
            D[i, b] = delta[a]
            D[i, a] = -delta[b]
        h = np.array([1., .3, -.2, .5, .1, -.7], dtype=complex)
        h /= np.linalg.norm(h)
        K = np.linalg.inv(np.eye(6)+tau*D @ D.conj().T)
        error = np.linalg.norm((K-np.eye(6)) @ h)**2+tau*np.linalg.norm(D.conj().T @ K @ h)**2
        exact_bound = np.real(h.conj() @ (np.eye(6)-K) @ h)
        assert abs(error-exact_bound) < 1e-14
        upper = tau*np.linalg.norm(D.conj().T @ h)**2
        assert error <= upper+1e-14
        scaled = float(error*L*L)
        assert scaled < 2.5
        if previous is not None:
            assert error < previous*.32
        previous = error
        # A coexact test has no added-noise or filtering error.
        _, singular, vh = np.linalg.svd(D.conj().T)
        rank = int(np.sum(singular > 1e-12))
        coexact = vh[rank].conj()
        assert np.linalg.norm(D.conj().T @ coexact) < 1e-13
        assert np.linalg.norm((K-np.eye(6)) @ coexact) < 1e-13
        rows.append({"L": L, "error_variance_bound": float(error), "L2_times_error": scaled})
    return rows


def main():
    families = [check_chain_and_folding, check_completion_and_bundle,
                check_poisson_density, check_one_plaquette_law,
                check_fillings_and_gauge, check_massive_geometry,
                check_cubic_filling_average, check_polymer_positivity_and_response,
                check_macroscopic_sources]
    result = {"status": "author finite checks; no independent review or phase theorem",
              "checks": {}}
    for check in families:
        answer = check()
        result['checks'][check.__name__] = answer
        print(f"PASS {check.__name__}: {json.dumps(answer, sort_keys=True)}", flush=True)
    destination = Path(__file__).with_name('BLOCK24_SMOOTHING_CHECKS.json')
    destination.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(f"TOTAL: PASS={len(families)} FAIL=0")


if __name__ == '__main__':
    main()
