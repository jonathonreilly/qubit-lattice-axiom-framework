"""Finite falsification diagnostics, not an infinite-time proof."""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import hashlib
import json
import pathlib
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
import numpy as np
import scipy
from scipy import sparse
from scipy.sparse.linalg import expm_multiply
from scipy.special import roots_legendre

from autonomous_boundary_reflection_check_2026_10_16 import run_reflection_checks, run_readiness_checks

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/AUTONOMOUS_BOUNDARY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-16.md',
    'scripts/autonomous_boundary_reflection_check_2026_10_16.py',
    'outputs/autonomous_boundary_reflection_2026_10_16_inputs/frozen_sources/CANDIDATE_V2.md',
    'outputs/autonomous_boundary_reflection_2026_10_16_inputs/frozen_sources/FINITE_READINESS_ADDENDUM.md',
)
START = time.monotonic()
ROOT = pathlib.Path(__file__).resolve().parents[1]
J = 3 / 16
w0 = 1 / 4
M = 384
T = 160.0
sigma = 0.12
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
I4 = np.eye(4, dtype=complex)
XX = np.kron(X, X)
K = 2 * I4 + np.kron(Z, Z)
Pm = (I4 - XX) / 2
W = ((9 + 12j) * I4 + (-16 + 12j) * XX) / 25
rstar = (-7 - 24j) / 25
R = (I4 + XX) / 2 + rstar * Pm
assert np.linalg.norm(R - rstar * W) < 1e-14
assert np.linalg.norm(K @ W - W @ K) < 1e-14

def reflection(k, w):
    return -(w + J * np.exp(1j * k)) / (w + J * np.exp(-1j * k))

def quadrature(q):
    x, weights = roots_legendre(q)
    k = np.pi / 2 + sigma * x
    f = np.sqrt(15) / (4 * np.sqrt(sigma)) * (1 - x**2)
    coeff = sigma * weights * f / np.sqrt(2 * np.pi)
    nn = np.arange(M)[:, None]
    return k, coeff, np.exp(-1j * nn * k), np.exp(1j * nn * k)

def packets(s, w, quad):
    k, coeff, em, ep = quad
    z = coeff * np.exp(-1j * 2 * J * (1 - np.cos(k)) * s)
    return em @ z, ep @ (z * reflection(k, w))

quad = quadrature(512)
quad_check = quadrature(768)
a0, b0 = packets(-T, 0, quad)
chi = a0 / np.linalg.norm(a0)
h0 = sparse.diags([-J * np.ones(M - 1), 2 * J * np.ones(M), -J * np.ones(M - 1)], [-1, 0, 1], format='csr')
p0 = sparse.csr_matrix(([1.0], ([0], [0])), shape=(M, M))
ready = np.kron(I4, chi[:, None])
results = []
for w in [w0, w0 + 0.02]:
    H = sparse.kron(K, sparse.eye(M), format='csr') + sparse.kron(I4, h0, format='csr') + sparse.kron(w * Pm, p0, format='csr')
    k = quad[0]
    rr = reflection(k, w)
    # Rebuild the boundary equation directly, not by differentiating r.
    boundary_res = np.max(np.abs((2 * J + w - 2 * J * (1 - np.cos(k))) * (1 + rr) - J * (np.exp(-1j * k) + rr * np.exp(1j * k))))
    assert boundary_res < 2e-15
    a_init, b_init = packets(-T, w, quad)
    init_scattering_error = np.linalg.norm(chi - a_init - b_init)
    assert init_scattering_error <= 2 * np.linalg.norm(b_init) + 1e-11
    for elapsed in [2 * T, 3 * T]:
        actual = expm_multiply((-1j * elapsed) * H, ready)
        s = elapsed - T
        a, b = packets(s, 0, quad)
        beta = b / np.linalg.norm(b)
        old = np.diag(np.exp(-1j * elapsed * np.diag(K)))
        wanted = np.kron(old @ R, beta[:, None])
        wrong_phase = np.kron(old @ W, beta[:, None])
        err = np.linalg.norm(actual - wanted, 2)
        phase_mutant_err = np.linalg.norm(actual - wrong_phase, 2)
        qa, qb = packets(s, 0, quad_check)
        quadrature_delta = max(np.linalg.norm(qa - a), np.linalg.norm(qb - b))
        assert quadrature_delta < 1e-10
        assert err < 0.2
        assert phase_mutant_err > 1
        # A direct reduced-clock-sector evolution checks the independent sparse joint calculation.
        hw = h0 + w * p0
        actual_minus = expm_multiply((-1j * elapsed) * hw, chi)
        a_exact, b_exact = packets(s, w, quad)
        gauge_error = np.linalg.norm(actual_minus - a_exact - b_exact)
        assert gauge_error <= init_scattering_error + 1e-9
        F0 = np.sqrt(15 * sigma) / 3
        F1 = np.sqrt(15) / (2 * np.sqrt(sigma))
        CA = F1 + (2 / np.sqrt(3)) * F0
        CB = F1 + (11 / 3 + 2 / np.sqrt(3)) * F0
        upper = 2 * (CA + CB) / np.sqrt(np.pi * np.sqrt(3) * J * T) + (17 / 3) * sigma + 2 * abs(w - w0) / J
        assert err <= upper
        results.append(dict(w=w, elapsed=elapsed, boundary_residual=float(boundary_res), isometry_error=float(err), omitted_global_phase_error=float(phase_mutant_err), quadrature_delta=float(quadrature_delta), initial_scattering_error=float(init_scattering_error), scattering_evolution_error=float(gauge_error), conservative_analytic_bound=float(upper), bound_is_informative=bool(upper < 2)))
    bound_vector = (-J / w) ** np.arange(M)
    bound_vector /= np.linalg.norm(bound_vector)
    bound_energy = 2 * J + w + J**2 / w
    residual = np.linalg.norm((h0 + w * p0) @ bound_vector - bound_energy * bound_vector)
    overlap = abs(np.vdot(bound_vector, chi))
    assert residual < 1e-13
    assert overlap <= init_scattering_error + 1e-10
    results.append(dict(w=w, bound_state_energy=float(bound_energy), bound_state_residual=float(residual), actual_ready_bound_overlap=float(overlap)))

# Full-qubit positive blocks, including zero/two-head sectors, on a small finite chain.
nc = 4
dim = 2 ** (nc + 2)
def onsite(A, site):
    out = np.array([[1.0]], dtype=complex)
    for s in range(nc + 2):
        out = np.kron(out, A if s == site else I2)
    return out

lower = np.array([[0, 1], [0, 0]], dtype=complex)
lower_ops = [onsite(lower, 2 + j) for j in range(nc)]
number_ops = [a.conj().T @ a for a in lower_ops]
clock = J * (number_ops[0] + number_ops[-1])
min_bond_eigenvalue = 0.0
for j in range(nc - 1):
    b = J * (number_ops[j] + number_ops[j+1] - lower_ops[j+1].conj().T @ lower_ops[j] - lower_ops[j].conj().T @ lower_ops[j+1])
    eig = np.linalg.eigvalsh(b)
    assert eig.min() > -1e-14 and abs(eig.max() - 2 * J) < 1e-14
    min_bond_eigenvalue = min(min_bond_eigenvalue, float(eig.min()))
    clock += b
oldK = 2 * np.eye(dim) + onsite(Z, 0) @ onsite(Z, 1)
oldPm = (np.eye(dim) - onsite(X, 0) @ onsite(X, 1)) / 2
boundary = w0 * number_ops[0] @ oldPm
fullH = oldK + clock + boundary
num = sum(number_ops)
assert np.linalg.eigvalsh(boundary).min() > -1e-14
assert np.linalg.eigvalsh(fullH).min() >= 1 - 1e-13
assert np.linalg.norm(fullH @ num - num @ fullH) < 1e-13
assert np.linalg.norm(fullH @ oldK - oldK @ fullH) < 1e-13
results.append(dict(full_qubit_dimension=dim, minimum_full_H_eigenvalue=float(np.linalg.eigvalsh(fullH).min()), boundary_norm=float(np.linalg.norm(boundary, 2)), smallest_bond_eigenvalue=min_bond_eigenvalue))

resource_examples = []
for eps in [0.5, 0.25, 0.1]:
    sig = 3 * eps / 68
    F0 = np.sqrt(15 * sig) / 3
    F1 = np.sqrt(15) / (2 * np.sqrt(sig))
    CA = F1 + 2 / np.sqrt(3) * F0
    CB = F1 + (11 / 3 + 2 / np.sqrt(3)) * F0
    tau = max(1 / (np.sqrt(3) * J), 16 * (CA + CB) ** 2 / (np.pi * np.sqrt(3) * J * eps**2))
    budget = 2 * (CA + CB) / np.sqrt(np.pi * np.sqrt(3) * J * tau) + (17/3) * sig + eps/4
    assert budget <= eps * (1 + 1e-14)
    resource_examples.append(dict(epsilon=eps, sigma=float(sig), T_lower_bound=float(tau), guaranteed_after_time=float(2*tau), boundary_error_allowance=float(J*eps/8), budget=float(budget), physical_evolution_executed=False))

independent_reflection = run_reflection_checks()
independent_readiness = run_readiness_checks()

report = dict(status='finite author and source-exposed checker diagnostics passed; all-future claim rests on the written proof', input_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}, python=sys.version, numpy=np.__version__, scipy=scipy.__version__, platform=platform.platform(), resource_caps=dict(cpu_seconds=120, largest_sparse_joint_dimension=4*M, largest_dense_full_qubit_dimension=dim, quadrature_orders=[512,768], sparse_input_columns=4), finite_fixture=dict(J=J, M=M, T=T, sigma=sigma), diagnostics=results, sufficient_parameter_examples=resource_examples, independent_reflection=independent_reflection, independent_readiness=independent_readiness, elapsed_seconds=time.monotonic()-START)
(ROOT/'outputs/autonomous_boundary_reflection_2026_10_16.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'status': report['status'], 'author_diagnostics': results, 'sufficient_parameter_examples': resource_examples, 'input_sha256': report['input_sha256'], 'elapsed_seconds': report['elapsed_seconds']}, indent=2))
