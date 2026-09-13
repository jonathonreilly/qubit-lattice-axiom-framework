"""Small native feedback collisions and exact resource arithmetic.

Two fixed square fixtures: initial cycle code and a real old-Record bridge.
The deleted hopping is irrational; original free evolution must be retained.
State errors are numerical counterchecks, not empirical diamond certificates.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS'):
    os.environ[name] = '1'
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import math
import resource
import signal
import time
import numpy as np
from scipy.linalg import expm
from scipy.sparse import csr_matrix, eye as sparse_eye, kron
from scipy.sparse.linalg import expm_multiply

signal.alarm(180)
started = time.monotonic()
ROOT = Path(__file__).resolve().parent
checks = {}
residuals = {}


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


def close(name, actual, expected, tolerance=2e-11):
    residual = float(np.max(np.abs(np.asarray(actual)-np.asarray(expected))))
    residuals[name] = residual
    check(name, residual < tolerance)


def trace_norm(hermitian):
    return float(np.sum(np.abs(np.linalg.eigvalsh((hermitian+hermitian.conj().T)/2))))


edges = ((0, 1), (1, 2), (2, 3), (0, 3))
ident = np.eye(16, dtype=complex)
Z = [np.diag([(-1)**((word >> e) & 1) for word in range(16)]).astype(complex)
     for e in range(4)]
vertex_parity = []
for v in range(4):
    op = ident.copy()
    for e, endpoints in enumerate(edges):
        if v in endpoints:
            op = op@Z[e]
    vertex_parity.append(op)
number = [(ident-b)/2 for b in vertex_parity]
N = sum(number)
native_A = []
T = []
for e, (u, v) in enumerate(edges):
    mask = []
    for root, other in ((u, v), (v, u)):
        for f, endpoints in enumerate(edges):
            if f != e and root in endpoints:
                neighbor = endpoints[1] if endpoints[0] == root else endpoints[0]
                if neighbor < other:
                    mask.append(f)
    a = np.zeros((16, 16), dtype=complex)
    for word in range(16):
        a[word ^ (1 << e), word] = (-1)**sum((word >> f) & 1 for f in mask)
    native_A.append(a)
    t = 1j*a@(vertex_parity[u]-vertex_parity[v])/2
    close(f'native_T_Hermitian_{e}', t, t.conj().T)
    close(f'native_T_number_{e}', t@N, N@t)
    T.append(t)
cycle = -native_A[0]@native_A[1]@native_A[2]@native_A[3]
close('cycle_Hermitian', cycle, cycle.conj().T)
close('cycle_square', cycle@cycle, ident)
for e in range(4):
    close(f'cycle_hopping_{e}', cycle@T[e], T[e]@cycle)
cycle_code = (ident+cycle)/2
PN2 = N@(4*ident-N)/4
J = T[2]@number[2]@(ident-number[3])
record = [(ident+z*Z[2])/2 for z in (1, -1)]
close('feedback_effect', J.conj().T@J, number[2]@(ident-number[3]))
close('opposite_dimers_commute', T[0]@T[2], T[2]@T[0])

energy_centers = np.diag([.5, 1.5, 2.5])
battery_up = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]], dtype=complex)
beta = np.ones(3)/math.sqrt(3)
fuel_lower = np.array([[0, 1], [0, 0]], dtype=complex)
square_root_two_hopping = math.sqrt(2)/3
steps = (.04, .02, .01)


def generator(free, jumps):
    n = free.shape[0]
    eye = sparse_eye(n, format='csr', dtype=complex)
    f = csr_matrix(free)
    loss = sum((j.conj().T@j for j in jumps), np.zeros_like(free))
    r = csr_matrix(loss)
    result = -1j*(kron(eye, f, format='csr')-kron(f.T, eye, format='csr'))
    result -= .5*(kron(eye, r, format='csr')+kron(r.T, eye, format='csr'))
    for jump in jumps:
        j = csr_matrix(jump)
        result += kron(j.conj(), j, format='csr')
    return result, loss


fixtures = {}
for tag in ('initial_cycle', 'old_Record_bridge'):
    old = tag == 'old_Record_bridge'
    if old:
        source_code = (ident+Z[0])/2@PN2
        psi = np.zeros(16, dtype=complex)
        psi[2], psi[4] = 1, 1j
        remaining = np.zeros_like(ident)
        fuel_count = 3
    else:
        source_code = cycle_code@PN2
        psi = np.zeros(16, dtype=complex)
        psi[1], psi[2] = 1, 1j
        remaining = T[0]
        fuel_count = 4
    psi = source_code@psi
    psi /= np.linalg.norm(psi)
    close(tag+'_legal_N2', N@psi, 2*psi)
    close(tag+'_legal_source_code', source_code@psi, psi)
    Ain = remaining+square_root_two_hopping*T[2]+fuel_count*ident
    Aout = remaining+(fuel_count-1)*ident
    Ain_rounded = remaining+fuel_count*ident
    A = np.block([[Aout, np.zeros_like(ident)], [np.zeros_like(ident), Ain]])
    A_rounded = np.block([[Aout, np.zeros_like(ident)], [np.zeros_like(ident), Ain_rounded]])
    # Simultaneous commuting dimers establish these as actual unit-grid
    # rounded spectral values. Eigh checks the entire ambient matrix.
    values, vectors = np.linalg.eigh(A)
    rounded_direct = (vectors*np.rint(values))@vectors.conj().T
    close(tag+'_whole_spectral_rounding', A_rounded, rounded_direct)
    F = np.kron(A, np.eye(3))+np.kron(np.eye(32), energy_centers)
    K = np.kron(A_rounded, np.eye(3))+np.kron(np.eye(32), energy_centers)
    close(tag+'_free_conserves_rounded_K', F@K, K@F)
    jumps = [np.kron(np.kron(fuel_lower, q@J), battery_up) for q in record]
    dim = F.shape[0]
    full_generator, R = generator(F, jumps)
    dissipative_generator, _ = generator(np.zeros_like(F), jumps)
    close(tag+'_actual_loss_projector', R@R, R)
    close(tag+'_actual_loss_not_identity', np.trace(R), 8.)
    for z, jump in enumerate(jumps):
        close(tag+f'_rounded_jump_energy_{z}', K@jump, jump@K)
        target_record = np.kron(np.eye(2), np.kron(record[z], np.eye(3)))
        close(tag+f'_new_Record_jump_{z}', target_record@jump, jump)
    commutator = max(float(np.linalg.norm(F@jump-jump@F, 2)) for jump in jumps)
    check(tag+'_original_free_does_not_commute', commutator > .1)
    cap_last = np.kron(np.eye(32), np.diag([0, 0, 1]))
    close(tag+'_cap_boundary_is_dark', R@cap_last, np.zeros_like(R))
    if old:
        old_record = np.kron(np.eye(2), np.kron(Z[0], np.eye(3)))
        close(tag+'_old_Record_free', F@old_record, old_record@F)
        for z, jump in enumerate(jumps):
            close(tag+f'_old_Record_jump_{z}', jump@old_record, old_record@jump)
    initial = np.kron(np.array([0, 1]), np.kron(psi, beta))
    rho = np.outer(initial, initial.conj())
    close(tag+'_initial_hazard_predicted_third', np.trace(R@rho), 1/3)
    star = np.zeros((3*dim, 3*dim), dtype=complex)
    for a, jump in enumerate(jumps):
        star[(a+1)*dim:(a+2)*dim, :dim] = jump
        star[:dim, (a+1)*dim:(a+2)*dim] = jump.conj().T
    close(tag+'_star_Hermitian', star, star.conj().T)
    K_all = np.kron(np.eye(3), K)
    close(tag+'_star_rounded_energy', K_all@star, star@K_all)
    rows = []
    vector = rho.reshape(-1, order='F')
    for h in steps:
        unitary = expm(-1j*math.sqrt(h)*star)
        blocks = [unitary[a*dim:(a+1)*dim, :dim] for a in range(3)]
        collision = sum((b@rho@b.conj().T for b in blocks), np.zeros_like(rho))
        k0 = np.eye(dim)+(math.cos(math.sqrt(h))-1)*R
        formula = k0@rho@k0.conj().T+math.sin(math.sqrt(h))**2*sum(
            (j@rho@j.conj().T for j in jumps), np.zeros_like(rho))
        close(tag+f'_explicit_unitary_formula_{h}', collision, formula)
        free = expm(-1j*h*F)
        split = free@collision@free.conj().T
        exact = expm_multiply(h*full_generator, vector).reshape((dim, dim), order='F')
        exact_diss = expm_multiply(h*dissipative_generator, vector).reshape((dim, dim), order='F')
        wrong_free = expm(-1j*h*K)
        wrong = wrong_free@collision@wrong_free.conj().T
        error = trace_norm(split-exact)
        dissipative_error = trace_norm(collision-exact_diss)
        wrong_error = trace_norm(wrong-exact)
        check(tag+f'_full_local_error_bound_{h}', 0 < error < 8*h*h)
        check(tag+f'_dissipative_local_error_bound_{h}', 0 < dissipative_error < 6*h*h)
        check(tag+f'_wrong_free_detected_{h}', wrong_error > 5*error)
        close(tag+f'_trace_{h}', np.trace(split), 1)
        close(tag+f'_rounded_energy_mean_{h}', np.trace(K@split), np.trace(K@rho))
        rows.append({'h': h, 'original_free_trace_norm_error': error,
                     'dissipative_trace_norm_error': dissipative_error,
                     'wrong_free_trace_norm_error': wrong_error})
    for first, second in zip(rows, rows[1:]):
        check(tag+f"_h_squared_{first['h']}", 3.5 < first['original_free_trace_norm_error']/second['original_free_trace_norm_error'] < 4.5)
    fixtures[tag] = {'system_dimension': dim, 'explicit_unitary_dimension': 3*dim,
                     'original_free_jump_commutator': commutator,
                     'initial_hazard': float(np.trace(R@rho).real), 'rows': rows}
    print('Completed '+tag, flush=True)

# Exact rational resource certificate, separate from numerical state checks.
delta, Lambda = Q(1, 1280), Q(3)
levels, storage, n = 97*1280, 49, 5401
constant = 6*Lambda**2+2*delta*Lambda
check('coefficient_bound_63', 3+18*Q(10, 3) == 63)
check('finite_battery_levels', levels == 124160 and 2**16 < levels <= 2**17)
check('storage_register_count', 12+12+8+17 == storage)
check('collision_labels_six_qubits', 2**5 < 1+24*2 <= 2**6)
check('collision_constant', constant == Q(34563, 640))
check('collision_step_domain', Lambda/n <= Q(1, 4))
check('collision_error_under_one_percent', constant/n < Q(1, 100))
check('combined_error_budget', 63*delta+Q(1, 100) == Q(379, 6400) < Q(3, 50))
check('total_retained_registers', storage+6*n == 32455)
elapsed = time.monotonic()-started
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/(1024*1024)
check('runtime_under_180_seconds', elapsed < 180)
check('RSS_under_180_MiB', 0 < rss < 180)
payload = {'status': 'small_native_feedback_checks_passed', 'author_check_only': True,
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'fixtures': fixtures, 'checks': checks, 'check_count': len(checks),
           'maximum_equality_residual': max(residuals.values()),
           'runtime_seconds': elapsed, 'peak_RSS_MiB': rss,
           'resources': {'finite_battery_levels': levels, 'storage_qubits': storage,
                         'collision_count': n, 'retained_qubits_total': storage+6*n,
                         'combined_trace_norm_upper_bound': str(Q(379, 6400))},
           'scope': 'Small state-specific native witnesses and exact resource arithmetic; general channel proof is analytical.'}
(ROOT/'BLOCK04_CHECKS.json').write_text(json.dumps(payload, indent=2)+'\n')
print(json.dumps({key: value for key, value in payload.items() if key != 'checks'}, indent=2))
