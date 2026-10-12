#!/usr/bin/env python3
"""Independent finite periodic-CAR diagnostics; no author helper imports."""
import itertools
import json
import platform
import sys
import time

import numpy as np
import scipy
from scipy.linalg import eigh, expm

TOL = 5e-10
DETECT = 1e-5
SERIES_TERMS = 384


def scalar(x):
    z = complex(x)
    return {"real": z.real, "imag": z.imag}


def norm(a):
    return float(np.linalg.norm(a, 2))


def majoranas(n):
    identity = np.eye(2, dtype=complex)
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    z = np.diag([1., -1.]).astype(complex)
    result = []
    for j in range(n):
        for final in (x, y):
            factors = [z] * j + [final] + [identity] * (n-j-1)
            out = np.ones((1, 1), dtype=complex)
            for factor in factors:
                out = np.kron(out, factor)
            result.append(out)
    return np.asarray(result)


def chain(n, a, m, v):
    gam = majoranas(n)
    dim = 2**n
    sig = np.sqrt(m*m/4 + v*v/(a*a))
    coupling_g = sig/2 + m/4
    coupling_j = sig/2 - m/4
    r = coupling_j/coupling_g
    ham = np.zeros((dim, dim), dtype=complex)
    for j in range(n):
        ham += 1j*coupling_g*(gam[2*j] @ gam[2*j+1])
        ham += 1j*coupling_j*(gam[2*j+1] @ gam[2*((j+1) % n)])

    # Reconstruct the beta generator from its absolutely convergent real-space
    # interaction; this code never calls theta, arg, or the polar formula.
    beta_generator = np.zeros((2*n, 2*n), dtype=float)
    for length in range(1, SERIES_TERMS+1):
        coefficient = r**length/(4*length)
        for j in range(n):
            for component, sign in ((0, 1), (1, -1)):
                beta_generator[2*j+component, 2*((j+length) % n)+component] += sign*coefficient
                beta_generator[2*j+component, 2*((j-length) % n)+component] -= sign*coefficient
    q = np.zeros_like(ham)
    for i in range(2*n):
        for j in range(i+1, 2*n):
            q += 0.5j*beta_generator[i, j]*(gam[i] @ gam[j])
    unitary = expm(1j*q)
    transformed = np.asarray([unitary @ item @ unitary.conj().T for item in gam])
    field_rows = np.einsum("iab,jba->ij", transformed, gam)/dim
    # beta(c(f))=c(F f): rows of the field action become columns for smearings.
    f_complex = field_rows.T
    reality_error = float(np.max(np.abs(f_complex.imag)))
    f = f_complex.real
    vacuum = np.zeros(dim, dtype=complex)
    vacuum[0] = 1
    beta_vacuum = unitary.conj().T @ vacuum
    energies, vectors = eigh(ham)
    ground = vectors[:, 0]
    ground_alignment_error = float(abs(1 - abs(np.vdot(ground, beta_vacuum))**2))

    # Extract the actual one-body generator from many-body commutators.
    derivs = np.asarray([1j*(ham @ item - item @ ham) for item in gam])
    a_matrix = np.einsum("iab,jba->ij", derivs, gam)/dim
    d_matrix = 1j*a_matrix
    eig, vec = eigh(d_matrix)
    abs_d = (vec*np.abs(eig)) @ vec.conj().T
    scalar_energy = abs_d[0::2, 0::2]
    series_tail = (r**(SERIES_TERMS+1)/((SERIES_TERMS+1)*(1-r))) if r else 0.
    return dict(n=n, a=a, m=m, v=v, gam=gam, ham=ham, f=f, unitary=unitary,
                ground=ground, d_matrix=d_matrix, scalar_energy=scalar_energy,
                metadata=dict(n=n, a=a, m=m, v=v, coupling_g=float(coupling_g),
                              coupling_j=float(coupling_j), r=float(r),
                              energy_gap=float(energies[1]-energies[0]),
                              hermiticity_error=norm(ham-ham.conj().T),
                              beta_reality_error=reality_error,
                              beta_orthogonality_error=norm(f.T@f-np.eye(2*n)),
                              beta_trace_vs_one_body_expm_error=norm(f-expm(-beta_generator)),
                              beta_ground_alignment_error=ground_alignment_error,
                              beta_series_angle_tail_bound=float(series_tail)))


def product(items, indices, dim):
    result = np.eye(dim, dtype=complex)
    for i in indices:
        result = result @ items[i]
    return result


def expectation(items, indices, state):
    transformed = state.copy()
    for i in reversed(indices):
        transformed = items[i] @ transformed
    return np.vdot(state, transformed)


def run_case(a, m, v):
    coarse, fine = chain(3, a, m, v), chain(6, a/2, m, v)
    hc = np.zeros((6, 3))
    for j in range(3):
        hc[2*j:2*j+2, j] = 1/np.sqrt(2)
    haar = np.kron(hc, np.eye(2))
    fc, ff = coarse["f"], fine["f"]
    maps = {
        "specified_adapted": ff.T @ haar @ fc,
        "bare_haar": haar,
        "reversed_fine_rotation": ff @ haar @ fc,
        "reversed_coarse_rotation": ff.T @ haar @ fc.T,
    }
    basis = [s for size in range(0, 7, 2) for s in itertools.combinations(range(6), size)]
    measured = {}
    for name, refinement in maps.items():
        field_images = np.einsum("ki,kab->iab", refinement, fine["gam"])
        rows = []
        for indices in basis:
            c = expectation(coarse["gam"], indices, coarse["ground"])
            f = expectation(field_images, indices, fine["ground"])
            rows.append(dict(indices=list(indices), coarse=scalar(c), fine=scalar(f), error=float(abs(c-f))))
        measured[name] = dict(isometry_error=norm(refinement.T@refinement-np.eye(6)),
                              max_moment_error=max(row["error"] for row in rows),
                              all_moment_rows=rows)

    refinement = maps["specified_adapted"]
    field_images = np.einsum("ki,kab->iab", refinement, fine["gam"])
    cbasis = [product(coarse["gam"], indices, 8) for indices in basis]
    fbasis = [product(field_images, indices, 64) for indices in basis]

    def embed(matrix):
        return sum((np.trace(b.conj().T@matrix)/8)*fb for b, fb in zip(cbasis, fbasis))

    zc = -1j*coarse["gam"][0]@coarse["gam"][1]
    nc = (np.eye(8)-zc)/2
    uc = coarse["unitary"]
    x = uc.conj().T@nc@uc
    xf = embed(x)
    coarse_derivative = 1j*(coarse["ham"]@x-x@coarse["ham"])
    fine_derivative = 1j*(fine["ham"]@xf-xf@fine["ham"])
    defect = fine_derivative - embed(coarse_derivative)
    dynamical_defect = norm(defect)
    s = hc[:, 0]
    g = fine["scalar_energy"]@s-hc@coarse["scalar_energy"][:, 0]
    variance = float(np.vdot(g, g).real - abs(np.vdot(s, g))**2)
    expected_rank_two = float(np.sqrt(max(0., variance)))
    zf = embed(zc)
    support_rows = []
    for j in range(2, 6):
        external_z = -1j*fine["gam"][2*j]@fine["gam"][2*j+1]
        support_rows.append(dict(site=j, commutator_norm=norm(zf@external_z-external_z@zf)))
    max_support = max(row["commutator_norm"] for row in support_rows)
    strict = v > 0
    gates = {
        "beta_ground_and_CAR": all(c["metadata"][key] < TOL for c in (coarse, fine)
            for key in ("hermiticity_error", "beta_reality_error", "beta_orthogonality_error",
                        "beta_trace_vs_one_body_expm_error", "beta_ground_alignment_error")),
        "adapted_isometry": measured["specified_adapted"]["isometry_error"] < TOL,
        "all_even_moments": measured["specified_adapted"]["max_moment_error"] < TOL,
        "mutation_behavior": all((measured[name]["max_moment_error"] > DETECT if strict
                                  else measured[name]["max_moment_error"] < TOL)
                                 for name in maps if name != "specified_adapted"),
        "even_dynamic_behavior": dynamical_defect > DETECT if strict else dynamical_defect < TOL,
        "rank_two_norm_crosscheck": abs(dynamical_defect-expected_rank_two) < TOL,
        "finite_support_behavior": max_support > DETECT if strict else max_support < TOL,
    }
    return dict(parameters=dict(a=a, m=m, v=v), strict_target_domain=strict,
                coarse=coarse["metadata"], fine=fine["metadata"], maps=measured,
                dynamics=dict(direct_many_body_defect_norm=dynamical_defect,
                              one_body_rank_two_norm=expected_rank_two,
                              norm_difference=abs(dynamical_defect-expected_rank_two),
                              raw_one_body_defect_norm=norm(fine["d_matrix"]@refinement-refinement@coarse["d_matrix"])),
                finite_support=support_rows, gates=gates)


started = time.time()
cases = [run_case(*args) for args in ((0.7, 1.3, 0.8), (0.4, 0.7, 1.1), (1.0, 0.9, 0.0))]
passed = sum(value for case in cases for value in case["gates"].values())
total = sum(len(case["gates"]) for case in cases)
result = dict(kind="finite_periodic_CAR_diagnostic_not_infinite_chain_proof",
              versions=dict(python=sys.version, numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform()),
              seconds=time.time()-started, cases=cases, passed=int(passed), failed=int(total-passed))
print(json.dumps(result, indent=2))
print(f"TOTAL: PASS={passed} FAIL={total-passed}")
sys.exit(0 if passed == total else 1)
