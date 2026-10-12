#!/usr/bin/env python3
"""Independent finite controls and exact witness replay; no author imports."""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS'):
    os.environ[_key] = '1'
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import platform
import time

import mpmath as mp
import numpy as np

SRC = Path(__file__).resolve().parent.parent
RUN = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/quantum/direct_visibility')
OUT = RUN / 'independent_visibility_review'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def block_diag(blocks):
    n = sum(len(b) for b in blocks)
    out = np.zeros((n, n), complex)
    offset = 0
    for b in blocks:
        out[offset:offset+len(b), offset:offset+len(b)] = b
        offset += len(b)
    return out


def polynomial_control():
    # f = P0/4 + P1 - P2/4, sum |a_l| = 3/2 exactly.
    # GL3 x seven azimuths integrates all harmonic products through l=2.
    z = np.array([-math.sqrt(3/5), 0., math.sqrt(3/5)])
    polar_weights = np.array([5/9, 8/9, 5/9])
    phi = 2*math.pi*np.arange(7)/7
    dirs = np.array([[math.sqrt(1-c*c)*math.cos(q),
                      math.sqrt(1-c*c)*math.sin(q), c] for c in z for q in phi])
    probability = np.repeat(polar_weights/14, 7)
    cosine = dirs @ dirs.T
    p2 = (3*cosine*cosine-1)/2
    kernel = .25 + cosine - .25*p2
    root = np.sqrt(probability)
    weighted = root[:, None]*kernel*root[None, :]
    eig = np.linalg.eigvalsh(weighted)
    expected_eig = np.sort(np.array([.25]+[1/3]*3+[-.05]*5+[0.]*12))
    spectral_error = float(np.max(np.abs(eig-expected_eig)))
    assert spectral_error < 2e-14
    trace_norm = float(np.abs(eig).sum())
    assert abs(trace_norm-1.5) < 2e-14
    # Analytic sign operator: sum of mutually orthogonal discrete harmonics.
    sign_kernel = 1 + 3*cosine - 5*p2
    sign = root[:, None]*sign_kernel*root[None, :]
    sign_error = float(np.max(np.abs(sign@sign@sign-sign)))
    assert sign_error < 2e-14
    norm_sign = float(np.linalg.norm(sign, 2))
    assert abs(norm_sign-1) < 2e-14
    witness = float(np.sum(sign*weighted))
    assert abs(witness-1.5) < 2e-14

    pauli_x = np.array([[0, 1], [1, 0]], complex)
    pauli_y = np.array([[0, -1j], [1j, 0]], complex)
    pauli_z = np.diag([1., -1.]).astype(complex)
    eye2 = np.eye(2)
    gamma1 = np.array([pauli_x, pauli_y, pauli_z])
    gamma2 = np.array([np.kron(pauli_x, eye2), np.kron(pauli_y, eye2),
                       np.kron(pauli_z, pauli_x), np.kron(pauli_z, pauli_y),
                       np.kron(pauli_z, pauli_z)])
    clifford_error = 0.
    for gamma in (gamma1, gamma2):
        for i, a in enumerate(gamma):
            for j, b in enumerate(gamma):
                expected = 2*np.eye(len(a)) if i == j else np.zeros_like(a)
                clifford_error = max(clifford_error, float(np.max(np.abs(a@b+b@a-expected))))
    assert clifford_error == 0.

    def features2(a):
        x, y, z = a
        return np.array([math.sqrt(3)/2*(x*x-y*y), (3*z*z-1)/2,
                         math.sqrt(3)*x*y, math.sqrt(3)*x*z, math.sqrt(3)*y*z])

    feature = np.array([features2(a) for a in dirs])
    feature_error = float(np.max(np.abs(feature@feature.T-p2)))
    assert feature_error < 2e-14
    cases = []
    for visibility in (.5, 2/3):
        # Sector dimensions 2,2,4,2; global pure state includes correlated
        # maximally entangled sectors and an uncorrelated product sector.
        weights = [visibility/4, visibility, visibility/4, max(0., 1-1.5*visibility)]
        dims = [2, 2, 4, 2]
        d = sum(dims)
        psi_matrix = np.zeros((d, d), complex)
        offset = 0
        for index, (size, weight) in enumerate(zip(dims, weights)):
            state = np.eye(size)/math.sqrt(size) if index < 3 else np.full((2, 2), .5)
            psi_matrix[offset:offset+size, offset:offset+size] = math.sqrt(weight)*state
            offset += size
        psi = psi_matrix.reshape(-1)
        alice, bob = [], []
        projective_error = 0.
        for direction, feature2 in zip(dirs, feature):
            first = np.einsum('i,ijk->jk', direction, gamma1)
            second = np.einsum('i,ijk->jk', feature2, gamma2)
            a = block_diag([pauli_z, first, second, pauli_z])
            b = block_diag([-pauli_z.T, -first.T, second.T, pauli_z])
            projective_error = max(projective_error, float(np.max(np.abs(a@a-np.eye(d)))),
                                   float(np.max(np.abs(b@b-np.eye(d)))),
                                   float(np.max(np.abs(a-a.conj().T))),
                                   float(np.max(np.abs(b-b.conj().T))))
            alice.append(a)
            bob.append(b)
        correlation = np.empty((len(dirs), len(dirs)))
        marginal = 0.
        for i, a in enumerate(alice):
            marginal = max(marginal, abs(np.vdot(psi, np.kron(a, np.eye(d))@psi)))
            for j, b in enumerate(bob):
                correlation[i, j] = np.vdot(psi, np.kron(a, b)@psi).real
        for b in bob:
            marginal = max(marginal, abs(np.vdot(psi, np.kron(np.eye(d), b)@psi)))
        error = float(np.max(np.abs(correlation+visibility*kernel)))
        assert abs(np.vdot(psi, psi)-1) < 2e-14
        assert error < 2e-14 and projective_error < 2e-14 and marginal < 2e-14
        cases.append({'visibility': visibility, 'local_dimension': d,
                      'correlation_error': error, 'projective_error': projective_error,
                      'fair_marginal_error': float(marginal)})
    return {'kernel': 'P0/4 + P1 - P2/4', 'exact_absolute_coefficient_sum': '3/2',
            'exact_critical_visibility': '2/3', 'settings': len(dirs),
            'eigenvalues_expected': '1/4 (x1), 1/3 (x3), -1/20 (x5), zero (x12)',
            'spectral_error': spectral_error, 'weighted_trace_norm': trace_norm,
            'analytic_sign_operator_norm': norm_sign, 'sign_cubic_identity_error': sign_error,
            'feature_addition_error': feature_error, 'clifford_anticommutation_error': clifford_error,
            'exact_witness_value_at_V_7_10': '21/20', 'realization_cases': cases}


def exact_norm_replay(path, row):
    artifact = np.load(path, allow_pickle=False)
    j_raw = artifact['integer_sign_matrix']
    radius = int(artifact['sign_denominator'])
    denominator = int(artifact['probability_denominator'])
    numerators = [int(x) for x in artifact['probability_numerators']]
    assert all(n > 0 for n in numerators) and sum(numerators) == denominator
    columns = [[int(j_raw[k, i]) for k in range(len(j_raw))] for i in range(len(j_raw))]
    row_sums = [0]*len(columns)
    # Different implementation: scalar Python integer inner products,
    # triangular traversal, no NumPy object matrix product.
    for i, a in enumerate(columns):
        for j in range(i, len(columns)):
            value = abs(sum(x*y for x, y in zip(a, columns[j])))
            row_sums[i] += value
            if i != j:
                row_sums[j] += value
    bound = max(row_sums)
    assert bound <= radius*radius
    assert bound == int(row['exact_gram_row_sum_max'])
    assert radius == math.isqrt(bound)+(math.isqrt(bound)**2 < bound)
    assert sha(path) == row['artifact_sha256']
    p = np.array(numerators)/denominator
    root = np.sqrt(p)
    witness = root[:, None]*(j_raw/radius)*root[None, :]
    witness_error = float(np.max(np.abs(witness-artifact['witness_coefficients'])))
    assert witness_error < 1e-20
    directions = artifact['directions']
    unit_error = float(np.max(np.abs(np.sum(directions*directions, axis=1)-1)))
    numerical_value = float(np.einsum('ij,ij->', witness, artifact['candidate_G']))
    assert abs(numerical_value-row['certified_witness_candidate_value_at_V1']) < 2e-14
    # Recompute the intended analytic grid using 65-digit Gauss roots and an
    # independent form tanh(atanh(2 asin(c)/pi)+k*c), then group the fixed
    # integer coefficients by azimuth difference. This is high precision,
    # not outward-rounded interval evidence.
    mp.mp.dps = 65
    order = row['polar_order']
    azimuths = 2*order+1
    nodes, _ = mp.gauss_quadrature(order, 'legendre')
    k = mp.sqrt(2)*(mp.atanh(1/mp.sqrt(2))-mp.atanh(mp.mpf(1)/2))
    total = mp.mpf(0)
    cosine_control = mp.mpf(0)
    for i in range(order):
        for j in range(order):
            weight = mp.sqrt(mp.mpf(numerators[i*azimuths])*numerators[j*azimuths])/(radius*denominator)
            for delta in range(azimuths):
                coefficient = sum(int(j_raw[i*azimuths+a, j*azimuths+(a+delta)%azimuths])
                                  for a in range(azimuths))
                c = nodes[i]*nodes[j]+mp.sqrt(1-nodes[i]**2)*mp.sqrt(1-nodes[j]**2)*mp.cos(2*mp.pi*delta/azimuths)
                if i == j and delta == 0:
                    c = mp.mpf(1)
                    g = mp.mpf(1)
                else:
                    assert -1 < c < 1
                    g = mp.tanh(mp.atanh(2*mp.asin(c)/mp.pi)+k*c)
                total += coefficient*weight*g
                cosine_control += coefficient*weight*c
    high_precision_difference = abs(float(total)-numerical_value)
    assert high_precision_difference < 2e-12
    return {'settings': len(columns), 'artifact_sha256': sha(path),
            'probability_denominator': denominator, 'probability_sum_exact': True,
            'gram_row_max_exact': str(bound), 'denominator_exact': str(radius),
            'squared_norm_upper_exact': [str(bound), str(radius*radius)],
            'exact_norm_certificate_pass': True, 'stored_witness_max_error': witness_error,
            'stored_direction_unit_norm_error': unit_error,
            'candidate_value_float_replay': numerical_value,
            'candidate_value_65_digits': mp.nstr(total, 65),
            'candidate_V_19_20_value_65_digits': mp.nstr(total*mp.mpf(19)/20, 65),
            'cosine_control_65_digits': mp.nstr(cosine_control, 65),
            'analytic_grid_vs_float_value_difference': high_precision_difference,
            'candidate_value_is_interval_certificate': False}


def main():
    start = time.time()
    paths = [SRC/'DIRECT_VISIBILITY_CRITERION.md', SRC/'direct_visibility_check.py',
             RUN/'FREEZE.json', RUN/'RESULTS_v1.json']
    source_hashes = {str(p): sha(p) for p in paths}
    author = json.loads((RUN/'RESULTS_v1.json').read_text())
    freeze = json.loads((RUN/'FREEZE.json').read_text())
    assert source_hashes[str(SRC/'DIRECT_VISIBILITY_CRITERION.md')] == freeze['note_sha256']
    assert source_hashes[str(SRC/'direct_visibility_check.py')] == author['source_sha256']
    assert source_hashes[str(RUN/'FREEZE.json')] == author['freeze_sha256']
    polynomial = polynomial_control()
    row = next(r for r in author['rows'] if r['polar_order'] == 12)
    replay = exact_norm_replay(RUN/'grid_12_v1.npz', row)
    for p in paths:
        assert sha(p) == source_hashes[str(p)]
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(),
              'source_sha256': sha(__file__), 'reviewed_sources': source_hashes,
              'python': platform.python_version(), 'numpy': np.__version__,
              'mpmath': mp.__version__, 'finite_signed_polynomial_control': polynomial,
              'final_grid_exact_norm_replay': replay,
              'elapsed_seconds': time.time()-start,
              'limits': 'Focused source/mathematical check only. No formal audit, original sphere-threshold proof disposition, empirical fit, or candidate expectation interval certification.'}
    destination = OUT/'CHECKS_v1.json'
    assert not destination.exists()
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
