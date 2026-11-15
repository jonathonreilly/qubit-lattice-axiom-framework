#!/usr/bin/env python3
"""Checks for the mass-retaining rough-core route in MANUSCRIPT_RG.md.

Actual Wilson plaquette loops check the zero-staple Schur diagnostic.
Independent Haar quadrature checks the SU(2) kernel-height bound.
The final arithmetic is a sufficient-threshold check, not an RG simulation.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[name] = "1"
import itertools
import math
import resource
import sys
sys.dont_write_bytecode = True
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm, expm_frechet
from scipy.special import ive


def guard():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    value = int(value if sys.platform == "darwin" else 1024 * value)
    if value >= 1_000_000_000:
        raise RuntimeError(f"RSS limit exceeded: {value}")
    return value


def mul(a, b):
    return np.r_[a[0]*b[0]-a[1:]@b[1:],
                 a[0]*b[1:]+b[0]*a[1:]-np.cross(a[1:], b[1:])]


def inv(q):
    return q*np.array([1., -1., -1., -1.])


def log_z(s):
    if s < 0.5:
        # 2 I1(s)/s = sum_k (s^2/4)^k/[k!(k+1)!].
        term = s*s/8
        tail = term
        k = 1
        while term > max(1e-300, abs(tail)*1e-17):
            k += 1
            term *= (s*s/4)/(k*(k+1))
            tail += term
        return math.log1p(tail)
    return s+math.log(2*float(ive(1, s))/s)


def wilson_core_checks():
    unit = np.array([1., 0., 0., 0.])
    origin = (0, 0, 0, 0)
    def field(x, mu, core, y):
        if mu != 0:
            return unit
        if tuple(x) == origin:
            return core
        for nu in range(1, 4):
            plus = [0]*4
            minus = [0]*4
            plus[nu], minus[nu] = 1, -1
            if tuple(x) == tuple(plus):
                return np.array([math.cos(y), 0., 0., math.sin(y)]) if nu == 1 else unit
            if tuple(x) == tuple(minus):
                return -unit
        return unit

    def plaquette(x, mu, nu, core, y):
        xm, xn = list(x), list(x)
        xm[mu] += 1
        xn[nu] += 1
        return mul(mul(mul(field(x, mu, core, y), field(xm, nu, core, y)),
                       inv(field(xn, mu, core, y))), inv(field(x, nu, core, y)))

    rng = np.random.default_rng(20261031)
    errors = []
    for _ in range(100):
        q = rng.normal(size=4)
        q /= np.linalg.norm(q)
        y = float(rng.uniform(-0.4, 0.4))
        energy = 0.0
        for nu in range(1, 4):
            minus = [0]*4
            minus[nu] = -1
            energy += 1-plaquette(origin, 0, nu, q, y)[0]
            energy += 1-plaquette(minus, 0, nu, q, y)[0]
        predicted = 6-q[0]*(math.cos(y)-1)-q[3]*math.sin(y)
        errors.append(abs(energy-predicted))
    assert max(errors) < 3e-14
    print(f"100 actual six-plaquette loop checks: max absolute error {max(errors):.6g}")
    print("Zero-staple Schur check: (u, predicted second derivative, finite difference)")
    for u in [1., 10., 100., 1000.]:
        h = 1e-3/u
        s = 2*u*abs(math.sin(h/2))
        measured = -2*log_z(s)/h**2
        expected = -u*u/4
        assert abs(measured/expected-1) < 2e-7
        print((u, expected, measured))
    print("Soft outputs in this diagnostic are integrated exactly by normalization; no pinned-output claim.")
    guard()


def height_checks():
    c0 = 25*math.exp(-0.5)/(54*math.pi)
    worst = 0.0
    for s in [0., 1e-4, 0.01, 0.1, 1., 10., 100., 1e3, 1e5]:
        scale = math.sqrt(1+s)
        upper = min(math.pi*scale, 18.)
        def integrand(z):
            theta = z/scale
            return 2/math.pi*math.sin(theta)**2*math.exp(-2*s*math.sin(theta/2)**2)/scale
        direct, _ = quad(integrand, 0, upper, epsabs=1e-13/scale**3, epsrel=1e-11)
        predicted = math.exp(log_z(s)-s)
        assert abs(direct/predicted-1) < 3e-10
        lower = c0/(1+s)**1.5
        assert direct >= lower*(1-2e-11)
        worst = max(worst, lower/direct)
    print(f"Kernel-height lower-integral checks: 9 scales; max bound/exact ratio {worst:.12g}")
    guard()


def stirling(n, k):
    row = [1.]
    for a in range(1, n+1):
        prev = row
        row = [0.]*(a+1)
        for b in range(1, a+1):
            row[b] = (prev[b-1] if b-1 < len(prev) else 0)+(b*prev[b] if b < len(prev) else 0)
    return row[k] if k < len(row) else 0.


def support_checks():
    # Use actual paired-contour readers, not a declared two-block support.
    from push_a_flat_hessian import contours
    block = 3
    dim = 4
    sites = list(itertools.product(range(block), repeat=dim))
    root = (1,)*dim
    basis = [tuple(int(i == j) for i in range(dim)) for j in range(dim)]
    def add(a, b, scale=1):
        return tuple(x+scale*y for x, y in zip(a, b))
    def owner(x):
        return tuple(v//block for v in x)
    def edge_tree(x, mu):
        if owner(x) != owner(add(x, basis[mu])):
            return False
        local = tuple(v % block for v in x)
        for child in [local, add(local, basis[mu])]:
            axis = next((a for a in range(dim) if child[a] != root[a]), None)
            if axis != mu:
                continue
            parent = add(child, basis[axis], 1 if child[axis] < root[axis] else -1)
            if {child, parent} == {local, add(local, basis[mu])}:
                return True
        return False
    def plaquette_edges(x, mu, nu):
        return [(x, mu), (add(x, basis[mu]), nu),
                (add(x, basis[nu]), mu), (x, nu)]
    templates = [{(x, mu) for path in contours(direction) for x, mu, _ in path}
                 for direction in range(dim)]
    zero = (0,)*dim
    for direction, readers in enumerate(templates):
        assert {owner(x) for x, _ in readers} <= {zero, basis[direction]}
    cases = [{zero}, {zero, basis[0]}, {zero, basis[0], basis[1]}]
    print("Actual-contour core supports: (|S|, |A|, free links, plaquettes, kernels, |H|)")
    for selected in cases:
        core = selected | {add(x, step, sign) for x in selected
                           for step in basis for sign in [-1, 1]}
        fine = {add(tuple(block*v for v in x), s) for x in core for s in sites}
        free = {(x, mu) for x in fine for mu in range(dim) if not edge_tree(x, mu)}
        assert len(free) == (3*block**4+1)*len(core)
        plaquettes = {(base, min(mu, nu), max(mu, nu)) for x, mu in free
                      for nu in range(dim) if nu != mu
                      for base in [x, add(x, basis[nu], -1)]}
        candidates = {(base, mu) for x in core for mu in range(dim)
                      for base in [x, add(x, basis[mu], -1)]}
        kernels = {}
        for x, mu in candidates:
            shift = tuple(block*v for v in x)
            readers = {(add(a, shift), direction) for a, direction in templates[mu]}
            if readers & free:
                kernels[x, mu] = readers
        hull = {add(x, shift) for x in core
                for shift in itertools.product([-1, 0, 1], repeat=dim)}
        assert len(core) <= 9*len(selected)
        assert len(free) <= 4*block**4*len(core)
        assert len(plaquettes) <= 24*block**4*len(core)
        assert len(kernels) <= 8*len(core)
        assert len(hull) <= 729*len(selected)
        for x, mu, nu in plaquettes:
            assert {owner(a) for a, _ in plaquette_edges(x, mu, nu)} <= hull
        for (x, mu), readers in kernels.items():
            assert {owner(a) for a, _ in readers} <= hull
            assert {x, add(x, basis[mu])} <= hull
        # Every potential owned witness is a function of core variables only.
        incidences = {}
        for x in selected:
            shift = tuple(block*v for v in x)
            for s in sites:
                base = add(shift, s)
                for mu, nu in itertools.combinations(range(dim), 2):
                    for a, direction in plaquette_edges(base, mu, nu):
                        assert edge_tree(a, direction) or (a, direction) in free
                        edge = (a, direction)
                        incidences[edge] = incidences.get(edge, 0)+1
        assert max(incidences.values()) <= 6
        print((len(selected), len(core), len(free), len(plaquettes), len(kernels), len(hull)))
        guard()


def cap_gradient_checks():
    # Independent 2x2 matrix calculation of the coordinate gradient used in CC12.
    pauli = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]],
                     dtype=complex)
    unit = np.eye(2, dtype=complex)
    def value_and_gradient(coords):
        mats, derivs = [], []
        for link in range(4):
            generator = 1j*np.einsum('a,aij->ij', coords[link], pauli)
            matrix = expm(generator)
            derivatives = [expm_frechet(generator, 1j*axis, compute_expm=False)
                           for axis in pauli]
            if link >= 2:
                matrix = matrix.conj().T
                derivatives = [d.conj().T for d in derivatives]
            mats.append(matrix)
            derivs.append(derivatives)
        product = unit.copy()
        for mat in mats:
            product = product@mat
        value = 1-float(np.trace(product).real)/2
        gradient = np.empty((4, 3))
        for link in range(4):
            for axis in range(3):
                derivative = unit.copy()
                for index in range(4):
                    derivative = derivative@(derivs[index][axis] if index == link else mats[index])
                gradient[link, axis] = -float(np.trace(derivative).real)/2
        return value, gradient
    rng = np.random.default_rng(20261101)
    maximum_ratio, maximum_error = 0., 0.
    for scale in [0.001, 0.05, 0.2, 0.7]:
        for _ in range(25):
            coords = scale*rng.normal(size=(4, 3))
            value, gradient = value_and_gradient(coords)
            ratio = float(np.sum(gradient**2)/(8*value))
            assert ratio <= 1+3e-8
            direction = rng.normal(size=(4, 3))
            direction /= np.linalg.norm(direction)
            step = 1e-5
            plus = value_and_gradient(coords+step*direction)[0]
            minus = value_and_gradient(coords-step*direction)[0]
            error = abs((plus-minus)/(2*step)-float(np.sum(gradient*direction)))
            assert error < 2e-9
            maximum_ratio, maximum_error = max(maximum_ratio, ratio), max(maximum_error, error)
    print(f"100 actual matrix plaquette-gradient checks for CC12: max ||grad f||^2/(8f) {maximum_ratio:.12g}; max directional finite-difference error {maximum_error:.6g}.")
    print("Owned-plaquette incidence multiplicity <= 6 verified in the three support geometries (CC8).")
    print("No nonlinear cap integral, spectral-gap value, or mixed connected jet estimate is numerically certified.")
    guard()


def threshold_checks():
    block = 3
    ell = 5*block-4
    kappa, weight_ratio, delta = 1., 1., 1/8
    source_weight = 4/16
    theta, s0, support_rate = 1/2, 1/4, 3.
    price = theta*s0
    gamma2 = 8/(3*math.pi**3)
    c0 = 25*math.exp(-0.5)/(54*math.pi)
    d1 = 192*block**4+4*kappa*(ell+1)**2
    d2 = 6*block**4+12
    d3 = -4*block**4*math.log(gamma2)+8*math.log(1/c0)+12*math.log(1+kappa)+4*source_weight
    cumulant = [0.]+[sum(stirling(r,k)*math.factorial(k-1) for k in range(1,r+1)) for r in range(1,7)]
    lam = math.sqrt(2)*(ell+weight_ratio)
    kr = [0.]+[lam**r*(kappa+sum(stirling(r,k)*cumulant[k]*kappa**k for k in range(1,r+1))) for r in range(1,7)]
    score = 1+2*source_weight+sum((24*block**4+source_weight)*(4*math.sqrt(2))**r+8*kr[r] for r in range(1,7))
    moment = [1.]+[sum(stirling(r,k)*score**k for k in range(1,r+1)) for r in range(1,11)]
    reciprocal = [1.]
    quotient = [1.]
    for r in range(1,11):
        reciprocal.append(sum(math.comb(r,k)*moment[k]*reciprocal[r-k] for k in range(1,r+1)))
        quotient.append(sum(math.comb(r,k)*moment[k]*reciprocal[r-k] for k in range(r+1)))
    cjet = sum(2**r/math.factorial(r)*math.comb(4,s)*quotient[r+s] for r in range(7) for s in range(5))
    j0 = math.log(cjet)+10*math.log(18)
    scalar_threshold = max(4., 3**(1/(2*delta)), (8/s0)**(1/(1-2*delta)),
                           (54*d1/price)**(1/(1-2*delta)),
                           (108*d2/(math.e*price))**2, 54*d3/price)
    final_threshold = max(scalar_threshold, (48/(math.e*price))**2,
                          8*j0/price, 4/price*(729*support_rate+math.log(2564)))
    print("Declared arithmetic scope: L=3, kappa=R=1, delta=1/8, theta=1/2, s0=1/4, four weights=1/16.")
    print(f"D1={d1:.12g}; D2={d2:.12g}; D3={d3:.12g}; log C_jet={math.log(cjet):.12g}")
    print(f"Sufficient core-price and jet threshold (not an RG threshold): {final_threshold:.12g}")
    for multiplier in [1., 2., 10.]:
        u = final_threshold*multiplier
        debit = 9*(d1*u**(2*delta)+d2*math.log(u)+d3)
        assert debit <= price*u/2*(1+1e-12)
        assert 3*math.log(u)+j0 <= price*u/4
        for size in [1, 2, 5, 17, 100]:
            jet_log = math.log(cjet)+3*math.log(u)+10*math.log(9*size)-price*u*size/2
            assert jet_log <= -price*u*size/4+1e-8
        exponent = 729*support_rate-price*u/4
        root_log = math.log(625)+exponent-math.log1p(-64*math.exp(exponent))
        assert root_log <= math.log(1/4)
        print((u, "debit/linear price", debit/(price*u), "log rooted bound", root_log))
    print("No complete history partition, inherited density, or connected activity representation tested.")
    print(f"Shrinking-threshold hostile test, c=8: 9 D1-theta c = {9*d1-theta*8:.12g} > 0; this upper bound loses its sign.")
    guard()


def main():
    guard()
    wilson_core_checks()
    height_checks()
    support_checks()
    cap_gradient_checks()
    threshold_checks()
    print(f"Peak RSS bytes: {guard()}; ceiling 1000000000; BLAS threads 1.")


if __name__ == "__main__":
    main()
