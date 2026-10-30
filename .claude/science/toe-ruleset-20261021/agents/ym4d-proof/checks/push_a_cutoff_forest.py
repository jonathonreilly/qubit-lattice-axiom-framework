#!/usr/bin/env python3
"""Finite actual-Gaussian and tree-combinatoric checks, not nonlinear RG.

Reconstruct selected covariances on a compatible 2^4 coarse torus from
all sixteen actual one-colour Bloch fibres. No sampled uniform gap claim.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
import sys
sys.dont_write_bytecode = True
import itertools
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ndtr
from numpy.polynomial.legendre import leggauss
from push_a_resolvent_paths import actual_matrices, FREE, guard


def actual_covariance():
    # Three distinct coordinates, all of the same colour and in one block.
    chosen = [0, 1, 2]
    covariance = np.zeros((3, 3), complex)
    lowest, highest, residual = math.inf, 0.0, 0.0
    for bits in itertools.product((0, 1), repeat=4):
        k = tuple(math.pi*a for a in bits)
        w, q, _ = actual_matrices(k)
        h = w+q.conj().T@q
        rhs = np.eye(len(FREE))[:, chosen]
        cols = np.linalg.solve(h, rhs)
        residual = max(residual, float(np.max(abs(h@cols-rhs))))
        covariance += cols[chosen, :]/16
        eig = np.linalg.eigvalsh(h)
        lowest, highest = min(lowest, eig[0]), max(highest, eig[-1])
        guard()
    assert np.max(abs(covariance.imag)) < 1e-12
    covariance = covariance.real
    assert np.max(abs(covariance-covariance.T)) < 1e-12
    assert residual < 1e-10
    print("Actual L=3, kappa=1, coarse 2^4 torus; all 16 Bloch fibres, one colour.")
    print("Selected fine free-column labels:", [FREE[j] for j in chosen])
    print("Selected 3-by-3 covariance:", covariance.tolist())
    print(f"This finite torus: Hessian eigenvalue interval [{lowest:.12g}, {highest:.12g}], solve residual {residual:.12g}.")
    print("The finite torus interval is not the uniform g_T constant.")
    return covariance


def hard_pair_check(covariance):
    worst = 0.0
    for i, j in itertools.combinations(range(3), 2):
        c = covariance[np.ix_([i, j], [i, j])]
        r = 1.5*math.sqrt(max(c[0, 0], c[1, 1]))
        v1, v2, cross = c[0, 0], c[1, 1], c[0, 1]
        sd1 = math.sqrt(v1)
        conditional_sd = math.sqrt(v2-cross*cross/v1)
        def joint_integrand(x):
            mean = cross*x/v1
            tails = ndtr((mean-r)/conditional_sd)+ndtr((-r-mean)/conditional_sd)
            return math.exp(-x*x/(2*v1))/(math.sqrt(2*math.pi)*sd1)*tails
        joint = 2*quad(joint_integrand, r, math.inf, epsabs=2e-13, epsrel=2e-12)[0]
        direct = joint-4*ndtr(-r/math.sqrt(v1))*ndtr(-r/math.sqrt(v2))
        def edge_integrand(h):
            s = c.copy()
            s[0, 1] = s[1, 0] = h*cross
            inv = np.linalg.inv(s)
            norm = 1/(2*math.pi*math.sqrt(np.linalg.det(s)))
            x, y = np.array([r, r]), np.array([r, -r])
            return 2*cross*norm*(math.exp(-0.5*x@inv@x)-math.exp(-0.5*y@inv@y))
        forest = quad(edge_integrand, 0, 1, epsabs=2e-13, epsrel=2e-12)[0]
        error = abs(direct-forest)
        assert error < 3e-12
        worst = max(worst, error)
        print(f"Hard pair {i,j}: direct truncated moment {direct:.12g}, boundary-forest value {forest:.12g}, discrepancy {error:.3g}.")
    print(f"Largest hard-pair discrepancy {worst:.12g}; both calculations retain the cutoff boundary.")


def smooth_three_check(c):
    a = np.array([0.7, 1.1, 0.9])/np.diag(c)
    def moment(indices):
        s = c[np.ix_(indices, indices)]
        return np.linalg.det(np.eye(len(indices))+2*s@np.diag(a[indices]))**-0.5
    singles = [moment([i]) for i in range(3)]
    direct = moment([0, 1, 2])+2*np.prod(singles)
    for i in range(3):
        direct -= singles[i]*moment([j for j in range(3) if j != i])
    nodes, weights = leggauss(24)
    nodes, weights = (nodes+1)/2, weights/2
    forest = 0.0
    # A triangle's three trees are identified by their degree-two vertex.
    # Split h1<h2 and h2<h1, avoiding a quadrature kink at min(h1,h2).
    for middle in range(3):
        left, right = [j for j in range(3) if j != middle]
        for orientation in (0, 1):
            for t, wt in zip(nodes, weights):
                for z, wz in zip(nodes, weights):
                    h1, h2 = (t*z, t) if orientation == 0 else (t, t*z)
                    w = np.eye(3)
                    w[middle, left] = w[left, middle] = h1
                    w[middle, right] = w[right, middle] = h2
                    w[left, right] = w[right, left] = min(h1, h2)
                    s = c*w
                    tilted = np.linalg.inv(np.linalg.inv(s)+2*np.diag(a))
                    mass = np.linalg.det(np.eye(3)+2*s@np.diag(a))**-0.5
                    wick = (tilted[middle, middle]*tilted[left, right]
                            +2*tilted[middle, left]*tilted[middle, right])
                    derivative = mass*(16*a[middle]**2*a[left]*a[right]*wick
                                      -8*a[middle]*a[left]*a[right]*tilted[left, right])
                    forest += wt*wz*t*c[middle, left]*c[middle, right]*derivative
    assert abs(direct-forest) < 3e-11
    print(f"Three distinct smooth insertions: determinant cumulant {direct:.12g}, three-tree integral {forest:.12g}, discrepancy {abs(direct-forest):.3g}.")
    eig = np.linalg.eigvalsh(c)
    rng = np.random.default_rng(20261030)
    for _ in range(50):
        h1, h2 = rng.random(2)
        w = np.array([[1, h1, min(h1, h2)], [h1, 1, h2], [min(h1, h2), h2, 1]])
        e = np.linalg.eigvalsh(c*w)
        assert e[0] >= eig[0]-1e-12 and e[-1] <= eig[-1]+1e-12
    print("50 forest interpolations preserve the selected covariance spectral interval; the Schur-product proof handles all sizes.")


def tree_degree_check():
    a0 = math.e*math.sqrt(6)
    for n in range(2, 8):
        enumerated = 0.0
        for word in itertools.product(range(n), repeat=n-2):
            degrees = [1]*n
            for entry in word:
                degrees[entry] += 1
            enumerated += math.prod(math.sqrt(math.factorial(d)) for d in degrees)
        series = np.array([math.sqrt(math.factorial(k+1))/math.factorial(k) for k in range(n-1)])
        power = np.array([1.0])
        for _ in range(n):
            power = np.convolve(power, series)[:n-1]
        coefficient = math.factorial(n-2)*power[n-2]
        assert abs(enumerated/coefficient-1) < 3e-12
        root_sum = enumerated/math.factorial(n-1)
        bound = a0**n/(n-1)
        assert root_sum <= bound
        print(f"n={n}: degree-weighted labelled trees {enumerated:.12g}; root sum {root_sum:.12g}, bound {bound:.12g}.")
    print("Tree counts check only the Hermite degree factor, not an RG activity norm.")
    # Explicit failure of a uniform-noise estimate for duplicate readers.
    for h in (0.5, 0.9, 0.99, 0.999):
        s = np.array([[1.0, h], [h, 1.0]])
        low = np.linalg.eigvalsh(s)[0]
        assert abs(low/(1-h)-1) < 1e-12
        print(f"Duplicate-coordinate interpolation h={h}: lowest eigenvalue {low:.12g}, inverse-noise edge cost {1/low:.12g}.")
    print("The resulting 1/(1-h) upper majorant is nonintegrable; this is failure of that estimate, not of the bounded covariance.")
    cutoff = 2.0
    boundary = quad(lambda theta: math.exp(-cutoff**2/(1+math.sin(theta)))/(2*math.pi),
                    0, math.pi/2, epsabs=2e-13, epsrel=2e-12)[0]
    probability = ndtr(-cutoff)
    exact = probability*(1-probability)
    assert abs(boundary-exact) < 2e-12
    print(f"Duplicate reader, indicator x>2: retained boundary integral {boundary:.12g}, exact variance {exact:.12g}, discrepancy {abs(boundary-exact):.3g}.")


if __name__ == "__main__":
    guard()
    c = actual_covariance()
    hard_pair_check(c)
    smooth_three_check(c)
    tree_degree_check()
    print(f"Peak RSS bytes: {guard()}; ceiling 1000000000; BLAS threads 1.")
