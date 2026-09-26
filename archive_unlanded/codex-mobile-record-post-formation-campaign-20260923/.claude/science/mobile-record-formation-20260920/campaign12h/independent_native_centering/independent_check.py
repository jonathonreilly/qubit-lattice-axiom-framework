#!/usr/bin/env python3
"""Independent sparse full-generator and relative-walk controls.

The full seven-label four-cycle is a degree-two normalization control, not
the three-dimensional target. The latter is checked through its exact
derived two-particle relative generator on growing cubic tori.
No primary code, output, or local dependency is imported.
"""
import hashlib
import itertools
import json
import math
import platform
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.sparse import bmat, coo_matrix, csc_matrix, diags
from scipy.sparse.linalg import expm_multiply
from scipy.special import i0e


START = time.perf_counter()
OUT = {
    "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "scope": "Full 7^4 four-cycle generator plus exact cubic-torus relative process; no simulations",
    "controls": {},
}


def record(name, value):
    OUT["controls"][name] = value


VECTORS = np.array([(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)], dtype=np.int64)
DOT = VECTORS @ VECTORS.T
assert np.array_equal(VECTORS[1:].sum(axis=0), np.zeros(3, dtype=int))
assert np.array_equal(VECTORS[1:].T @ VECTORS[1:], 2 * np.eye(3, dtype=int))
record("six_axis_second_moment", {"sum_vectors": [0, 0, 0], "sum_outer_products": (2 * np.eye(3, dtype=int)).tolist()})

# Complete finite generator, independently assembled from configurations.
STATES = np.array(list(itertools.product(range(7), repeat=4)), dtype=np.int64)
NS = len(STATES)
POWERS = np.array([7**3, 7**2, 7, 1], dtype=np.int64)
assert np.array_equal(STATES @ POWERS, np.arange(NS))
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
neighbors = [[(x - 1) % 4, (x + 1) % 4] for x in range(4)]
rows, cols, vals = [[], [], []], [[], [], []], [[], [], []]


def add(degree, source, target, rate6):
    if rate6:
        rows[degree].extend((target, source))
        cols[degree].extend((source, source))
        vals[degree].extend((rate6, -rate6))


for q, state in enumerate(STATES):
    for x, y in edges:
        if state[x] != state[y]:
            target = q + (int(state[y]) - int(state[x])) * int(POWERS[x] - POWERS[y])
            add(0, q, target, 9)  # exchange alpha=3/2; coefficients stored times six
    for x in range(4):
        if state[x] == 0:
            y, z = neighbors[x]
            for a in range(1, 7):
                d1, d2 = int(DOT[a, state[y]]), int(DOT[a, state[z]])
                target = q + a * int(POWERS[x])
                for degree, rate6 in enumerate((1, d1 + d2, d1 * d2)):
                    add(degree, q, target, rate6)  # beta=1/6

Q6 = [coo_matrix((np.array(vals[k], dtype=np.int64), (rows[k], cols[k])), shape=(NS, NS)).tocsc() for k in range(3)]
for matrix in Q6:
    assert np.array_equal(np.asarray(matrix.sum(axis=0)).ravel(), np.zeros(NS, dtype=np.int64))
Q = [matrix.astype(float) / 6 for matrix in Q6]
record("full_generator_assembly", {"states": NS, "coefficient_nonzeros": [matrix.nnz for matrix in Q6], "integer_column_sums_zero": True, "beta": "1/6", "exchange_rate": "3/2", "degree": 2})

weights = np.prod(np.where(STATES == 0, 6, 1), axis=1).astype(np.int64)
denominator = 12**4
assert weights.sum() == denominator
mu0 = weights.astype(float) / denominator
n0 = (STATES[:, 0] != 0).astype(np.int64)

# Time/j Taylor coefficient independently taken from the complete generator.
BIG6 = bmat([[Q6[i-j] if 0 <= i-j <= 2 else None for j in range(4)] for i in range(4)], format="csc")
initial_integer = np.concatenate((weights, np.zeros(3 * NS, dtype=np.int64)))
third = BIG6 @ (BIG6 @ (BIG6 @ initial_integer))
exact_j3_time3 = Fraction(int(n0 @ third[3*NS:]), denominator * 6**3 * math.factorial(3))
assert exact_j3_time3 == Fraction(1, 36)
assert np.array_equal(Q6[1].T @ n0, np.zeros(NS, dtype=np.int64))
assert int(n0 @ (Q6[2] @ weights)) == 0
record("full_generator_exact_time_and_j_control", {"j3_t3_coefficient": str(exact_j3_time3), "target": "1/36", "first_j_generator_on_density_identically_zero": True, "second_j_product_mean_zero": True})

T = 0.7
BIG = BIG6.astype(float) / 6
initial = initial_integer.astype(float) / denominator
law_coefficients = expm_multiply(T * BIG, initial).reshape(4, NS)
vtime = 0.5 * math.exp(-T)
ptime = np.array([vtime] + [(1 - vtime) / 6] * 6)
product_time = np.prod(ptime[STATES], axis=1)
assert np.max(np.abs(law_coefficients[0] - product_time)) < 2e-14
coefficients = law_coefficients @ n0
assert abs(coefficients[1]) < 2e-14 and abs(coefficients[2]) < 2e-14
assert abs(coefficients[0] - (1-vtime)) < 2e-13
record("full_generator_time_coefficients", {"t": T, "j_coefficients_0_to_3": coefficients.tolist(), "uniform_product_error": float(np.max(np.abs(law_coefficients[0]-product_time))), "coefficient_masses": law_coefficients.sum(axis=1).tolist()})

factor_errors = []
pair_coefficients = {}
for y in range(4):
    for z in range(y+1, 4):
        pair = DOT[STATES[:, y], STATES[:, z]]
        pc = float(pair @ law_coefficients[1])
        pair_coefficients[f"{y},{z}"] = pc
        for x in range(4):
            if x not in (y, z):
                tc = float(((STATES[:, x] == 0) * pair) @ law_coefficients[1])
                factor_errors.append(abs(tc-vtime*pc))
assert max(factor_errors) < 2e-14
record("full_generator_vacancy_pair_factorization", {"maximum_error": max(factor_errors), "pair_coefficients": pair_coefficients})


def augmented_response(D, adjacency, pair_weights, alpha, beta, vacancy, t):
    """Integrate the derived pair ODE and density coefficient by one sparse exponential."""
    size = D.shape[0]
    rr, cc, dd = [], [], []
    Dc = (alpha * D).tocoo()
    rr.extend(Dc.row.tolist()); cc.extend(Dc.col.tolist()); dd.extend(Dc.data.tolist())
    for r in np.flatnonzero(adjacency):
        rr.extend((int(r), int(r))); cc.extend((size+1, size+2))
        dd.extend((4*beta*vacancy*adjacency[r], -4*beta*vacancy**2*adjacency[r]))
    for r in np.flatnonzero(pair_weights):
        rr.append(size); cc.append(int(r)); dd.append(2*beta*vacancy*pair_weights[r])
    rr.extend((size+1, size+2)); cc.extend((size+1, size+2)); dd.extend((-6*beta, -12*beta))
    aug = coo_matrix((dd, (rr, cc)), shape=(size+3, size+3)).tocsc()
    initial = np.zeros(size+3); initial[size+1:] = 1
    result = expm_multiply(t*aug, initial)
    return float(math.exp(-6*beta*t)*result[size]), result[:size]


# Relative walk on a four-cycle: punctured cycle is the three-site path.
D4 = csc_matrix(np.array([[-2, 2, 0], [2, -4, 2], [0, 2, -2]], dtype=float))
adj4 = np.array([1., 0., 1.])
ell4 = np.array([0., 1., 0.])
reduced_a3, reduced_pair = augmented_response(D4, adj4, ell4, 1.5, 1/6, 0.5, T)
assert abs(reduced_a3-coefficients[3]) < 2e-14
for u in (0., 0.01, 0.4, 2.):
    actual = expm_multiply(u*D4, adj4)[1]
    expected = (2/3)*(1-math.exp(-6*u))
    assert abs(actual-expected) < 2e-14
H = lambda s: 0.5*(1-math.exp(-s)) - 0.125*(1-math.exp(-2*s))
closed_a3, quad_error = quad(lambda u: (8/36)*vtime*(2/3)*(1-math.exp(-9*u))*H(T-u), 0., T, epsabs=1e-14)
assert abs(closed_a3-coefficients[3]) < 2e-14
record("independently_reduced_four_cycle", {"full_generator_j3": float(coefficients[3]), "relative_ode_j3": reduced_a3, "closed_kernel_quadrature_j3": closed_a3, "quadrature_error_estimate": quad_error, "relative_opposite_to_adjacency_probability": "(2/3)*(1-exp(-6u))"})

# Direct +j/-j check uses the physical finite generators, not the block system.
odd_ratios = []
for j in (0.2, 0.1, 0.05):
    means = []
    for sign in (1, -1):
        operator = Q[0] + sign*j*Q[1] + j*j*Q[2]
        means.append(float(n0 @ expm_multiply(T*operator, mu0)))
    ratio = (means[0]-means[1])/(2*j**3)
    odd_ratios.append({"j": j, "odd_density_over_j3": ratio, "difference_from_j3": ratio-float(coefficients[3])})
assert abs(odd_ratios[-1]["difference_from_j3"]) < abs(odd_ratios[0]["difference_from_j3"])
record("physical_generator_odd_response", odd_ratios)


def cubic_relative(N):
    coords = np.indices((N, N, N)).reshape(3, -1).T[1:]
    size = N**3-1
    row, col, data = [], [], []
    degree = np.zeros(size, dtype=np.int64)
    for axis in range(3):
        for sign in (-1, 1):
            dest = coords.copy(); dest[:, axis] = (dest[:, axis]+sign) % N
            full_flat = (dest[:, 0]*N+dest[:, 1])*N+dest[:, 2]
            mask = full_flat != 0
            sources = np.flatnonzero(mask)
            row.append(sources); col.append(full_flat[mask]-1); data.append(np.full(len(sources), 2., dtype=float))
            degree[mask] += 1
    row.append(np.arange(size)); col.append(np.arange(size)); data.append(-2.*degree)
    D = coo_matrix((np.concatenate(data), (np.concatenate(row), np.concatenate(col))), shape=(size, size)).tocsc()
    assert (D-D.T).nnz == 0
    assert np.max(np.abs(np.asarray(D.sum(axis=1)))) == 0
    A = []
    for axis in range(3):
        for sign in (-1, 1):
            a = np.zeros(3, dtype=np.int64); a[axis] = sign % N; A.append(a)
    def index(r):
        r = np.asarray(r) % N
        return int((r[0]*N+r[1])*N+r[2]-1)
    adj = np.zeros(size)
    for a in A: adj[index(a)] = 1
    ell = np.zeros(size)
    for a, b in itertools.combinations(A, 2): ell[index(b-a)] += 1
    assert adj.sum() == 6 and ell.sum() == 15
    return D, adj, ell


small_time_geometry = []
for N in (4, 5, 6, 8):
    D, adj, ell = cubic_relative(N)
    slope = int(round(float(ell @ (D @ adj))))
    assert ell @ adj == 0
    assert slope == (60 if N == 4 else 54)
    small_time_geometry.append({"N": N, "F_at_zero": 0, "F_prime_at_zero": slope, "j3_t3_factor_divided_by_beta2_alpha_v02_rho0": str(Fraction(4*slope, 3))})
record("cubic_torus_short_time_geometry", small_time_geometry)

# Finite-torus Poisson identity reconstructed via the full-torus Fourier inverse.
poisson_checks = []
for N in (4, 5, 8):
    D, adj, ell = cubic_relative(N)
    frequencies = 2*np.pi*np.arange(N)/N
    eig = 4*((1-np.cos(frequencies))[:, None, None]+(1-np.cos(frequencies))[None, :, None]+(1-np.cos(frequencies))[None, None, :])
    inverse = np.zeros_like(eig); inverse[eig>0] = 1/eig[eig>0]
    green = np.fft.ifftn(inverse).real.ravel()
    potential = 6*N**3/(N**3-1)*(green[1:] + green[0]/(N**3-1))
    residual = -D @ potential - (adj-6/(N**3-1))
    err = float(np.max(np.abs(residual)))
    assert err < 2e-13
    poisson_checks.append({"N": N, "maximum_residual": err, "centered_potential_mean": float(potential.mean())})
record("finite_punctured_torus_poisson_identity", poisson_checks)

# Infinite-volume ordinary Green kernel, generator 2 Delta.
# Coordinate return kernels equal exp(-4t) I_0(4t); use scaled Bessel and t=s^2.
g0, g0err = quad(lambda s: 2*s*i0e(4*s*s)**3, 0., np.inf, epsabs=2e-13, epsrel=2e-13, limit=300)
Gstar = 90*g0-9
assert Gstar > 0
beta, kappa, vacancy, t = 1/6, 1., 0.5, 1.
vt = vacancy*math.exp(-6*beta*t)
Ht = vacancy/(6*beta)*(1-math.exp(-6*beta*t))-vacancy**2/(12*beta)*(1-math.exp(-12*beta*t))
limit = 8*beta**2*vt*Ht*Gstar/kappa
record("infinite_volume_green_constant", {"g0_generator_2_delta": g0, "quadrature_error_estimate": g0err, "discrete_time_srw_green_at_zero": 12*g0, "G_star": Gstar, "fixed_time_N_times_a3_limit": limit, "parameters": {"beta": beta, "kappa": kappa, "v0": vacancy, "t": t}, "quadrature_is_support_not_proof": True})

growth = []
for N in (4, 6, 8, 12, 16, 24, 32):
    tick = time.perf_counter()
    D, adj, ell = cubic_relative(N)
    a3, _ = augmented_response(D, adj, ell, kappa*N, beta, vacancy, t)
    assert a3 > 0
    growth.append({"N": N, "relative_states": N**3-1, "a3": a3, "N_times_a3": N*a3, "ratio_to_limit": N*a3/limit, "elapsed_seconds": time.perf_counter()-tick})
record("growing_torus_coefficient_controls", growth)

OUT["completed_control_groups"] = len(OUT["controls"])
OUT["elapsed_seconds"] = time.perf_counter()-START
payload = json.dumps(OUT, indent=2, sort_keys=True)+"\n"
Path("RESULTS.json").write_text(payload)
print(payload, end="")
