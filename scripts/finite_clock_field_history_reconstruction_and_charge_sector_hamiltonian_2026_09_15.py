#!/usr/bin/env python3
"""Author finite history and endpoint-filling checks; no review verdict."""
AUDIT_TIMEOUT_SEC = 300


from pathlib import Path
import itertools, hashlib, json
import numpy as np

def check_history_reconstruction():
    rows = []
    D = np.zeros((4, 4), dtype=int)
    for e in range(4):
        D[e, e] = -1
        D[e, (e + 1) % 4] = 1
    j = np.array([1, 0, 0, 0])
    loop = np.ones(4, dtype=int)
    zero = np.zeros(4, dtype=int)
    histories = [[('u', j)], [('u', j), ('t', 1), ('u', loop)], [('u', loop), ('t', 2), ('u', j)], [('u', j), ('t', 1), ('u', -loop), ('t', 1)], [('u', 2 * j), ('t', 1), ('u', -j)], [], [('u', loop), ('t', 1), ('u', -loop)], [('u', -j), ('t', 1), ('u', j)], [('u', j), ('t', 2), ('u', j)]]
    for N, beta in [(2, 0.4), (3, 0.6), (4, 0.8)]:
        a = np.array(list(itertools.product(range(N), repeat=4)))
        count = len(a)
        angles = 2 * np.pi * np.arange(N) / N
        weight = np.exp(-beta * (angles[:, None] + 2 * np.pi * np.arange(-10, 11)) ** 2 / 2).sum(axis=1)
        coeff = np.fft.fft(weight).real / N
        assert coeff.min() > 0
        delta = (a[:, None, :] - a[None, :, :]) % N
        C = np.prod(weight[delta], axis=2) / count
        root = np.sqrt(weight[a.sum(axis=1) % N])
        T = root[:, None] * C * root[None, :]
        eig, vec = np.linalg.eigh(T)
        lam = eig[-1]
        Omega = vec[:, -1]
        if Omega.sum() < 0:
            Omega = -Omega
        assert Omega.min() > 0 and eig[0] > 0
        tau = T / lam
        projected = {}

        def temporal(rho):
            key = tuple(rho % N)
            if key not in projected:
                value = np.zeros_like(C, dtype=complex)
                for eta in a:
                    kernel = np.prod(weight[(delta + D @ eta) % N], axis=2) / count
                    value += kernel * np.exp(-2j * np.pi * (rho @ eta) / N) / count
                projected[key] = root[:, None] * value * root[None, :] / lam
            return projected[key]
        cols = []
        profiles = []
        checks = []
        for index, history in enumerate(histories):
            original = Omega.astype(complex)
            direct = original.copy()
            wrong = original.copy()
            rho = zero.copy()
            for kind, arg in history:
                if kind == 'u':
                    phase = np.exp(2j * np.pi * (a @ arg) / N)
                    original *= phase
                    direct *= phase
                    wrong *= phase
                    rho += D.T @ arg
                else:
                    original = np.linalg.matrix_power(tau, arg) @ original
                    direct = np.linalg.matrix_power(temporal(rho), arg) @ direct
                    wrong = np.linalg.matrix_power(temporal(zero), arg) @ wrong
            discrepancy = float(np.max(abs(original - direct)))
            assert discrepancy < 3e-12
            cols.append(original)
            profiles.append(rho % N)
            final = history[-1][1] if history and history[-1][0] == 'u' else zero
            K = float(np.prod([max(coeff / coeff[(np.arange(N) + int(q)) % N]) for q in final]))
            norm = float(np.vdot(original, original).real)
            inverse = float(np.vdot(original, np.linalg.solve(tau, original)).real)
            spectral = float(np.sum(abs(vec.conj().T @ original) ** 2 * lam / eig))
            assert norm <= 1 + 3e-12 and inverse <= K + 3e-10
            assert abs(inverse - spectral) < 3e-10 * max(1, inverse)
            checks.append({'word': index, 'final_insertion': final.tolist(), 'charge': (rho % N).tolist(), 'norm_squared': norm, 'inverse_moment': inverse, 'K_final_insertion': K, 'temporal_link_discrepancy': discrepancy, 'wrong_neutral_projector_error': float(np.linalg.norm(original - wrong))})
        W = np.column_stack(cols)
        gram = W.conj().T @ W
        field = np.exp(2j * np.pi * (a @ (j - loop)) / N)
        prefixed = field[:, None] * W
        assert np.max(abs(prefixed.conj().T @ prefixed - gram)) < 3e-12
        lower = {'gram': float(np.linalg.eigvalsh(gram)[0]), 'positive_transfer': float(np.linalg.eigvalsh(W.conj().T @ tau @ W)[0]), 'contractive_form': float(np.linalg.eigvalsh(W.conj().T @ (np.eye(count) - tau) @ W)[0]), 'contractive_norm': float(np.linalg.eigvalsh(gram - (tau @ W).conj().T @ (tau @ W))[0])}
        assert min(lower.values()) > -3e-12
        orthogonal = []
        for i in range(len(histories)):
            for k in range(i):
                if not np.array_equal(profiles[i], profiles[k]):
                    orthogonal.append(abs(gram[i, k]))
        assert max(orthogonal) < 3e-12
        assert max((x['wrong_neutral_projector_error'] for x in checks)) > 0.001
        assert checks[0]['inverse_moment'] > 1.01
        assert checks[3]['K_final_insertion'] == 1 and checks[3]['inverse_moment'] <= 1 + 3e-12
        rows.append({'N': N, 'beta': beta, 'dimension': count, 'histories': checks, 'gram_lower_eigenvalues': lower, 'maximum_distinct_charge_overlap': float(max(orthogonal)), 'temporal_charge_matrices': len(projected)})
    result = {'status': 'personal_finite_checks_not_independent_review', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': rows, 'limits': 'Finite words and explicit temporal sums; no finite check proves cofinal limits, time-zero cyclicity or equality of larger-sector bottoms.'}
    return result

from pathlib import Path
import itertools, hashlib, json
import numpy as np

def check_endpoint_comparison():
    rows = []
    cube_rows = []
    D = np.zeros((4, 4), dtype=int)
    for e in range(4):
        D[e, e] = -1
        D[e, (e + 1) % 4] = 1
    j = np.array([1, 0, 0, 0])
    loop = np.ones(4, dtype=int)
    zero = np.zeros(4, dtype=int)
    histories = [[('u', j)], [('u', j), ('t', 1), ('u', loop)], [('u', loop), ('t', 2), ('u', j)], [('u', j), ('t', 1), ('u', -loop), ('t', 1)], [('u', 2 * j), ('t', 1), ('u', -j)], [], [('u', loop), ('t', 1), ('u', -loop)], [('u', -j), ('t', 1), ('u', j)], [('u', j), ('t', 2), ('u', j)]]
    for N, beta in [(2, 0.4), (3, 0.6), (4, 0.8)]:
        a = np.array(list(itertools.product(range(N), repeat=4)))
        count = len(a)
        angles = 2 * np.pi * np.arange(N) / N
        weight = np.exp(-beta * (angles[:, None] + 2 * np.pi * np.arange(-10, 11)) ** 2 / 2).sum(axis=1)
        coeff = np.fft.fft(weight).real / N
        delta = (a[:, None, :] - a[None, :, :]) % N
        C = np.prod(weight[delta], axis=2) / count
        root = np.sqrt(weight[a.sum(axis=1) % N])
        T = root[:, None] * C * root[None, :]
        eig, vec = np.linalg.eigh(T)
        lam = eig[-1]
        Omega = vec[:, -1]
        if Omega.sum() < 0:
            Omega = -Omega
        tau = T / lam
        for index, history in enumerate(histories):
            phi = Omega.astype(complex)
            total = sum((arg for kind, arg in history if kind == 'u'), start=zero.copy())
            t = 0
            past = zero.copy()
            strips = []
            insertions = {}
            for kind, arg in history:
                if kind == 'u':
                    phi *= np.exp(2j * np.pi * (a @ arg) / N)
                    past += arg
                    insertions[t] = insertions.get(t, zero.copy()) + arg
                else:
                    phi = np.linalg.matrix_power(tau, arg) @ phi
                    for _ in range(arg):
                        strips.append(-(total - past))
                        t += 1
            length = t
            R = 1.0
            spatial = np.zeros((length + 1, 4), dtype=int)
            temporal = np.zeros((length, 4), dtype=int)
            for t, current in enumerate(strips):
                spatial[t] += current
                spatial[t + 1] -= current
                temporal[t] += D.T @ current
                R *= float(np.prod([max(coeff / coeff[(np.arange(N) + int(q)) % N]) for q in current]))
            expected_spatial = np.zeros_like(spatial)
            expected_spatial[0] -= total
            for t, current in insertions.items():
                expected_spatial[t] += current
            assert np.array_equal(spatial, expected_spatial)
            cumulative = zero.copy()
            for t in range(length):
                cumulative += insertions.get(t, zero)
                assert np.array_equal(temporal[t], D.T @ (cumulative - total))
            ref = np.exp(2j * np.pi * (a @ total) / N) * Omega
            for n in (0, 1, 3, 7):
                value = float(np.vdot(phi, np.linalg.matrix_power(tau, n) @ phi).real)
                reference = float(np.vdot(ref, np.linalg.matrix_power(tau, n + 2 * length) @ ref).real)
                assert reference > 0 and value > 0
                assert reference / R ** 2 - 5e-12 <= value <= reference * R ** 2 + 5e-12
                wrong_time = float(np.vdot(ref, np.linalg.matrix_power(tau, n) @ ref).real)
                rows.append({'N': N, 'beta': beta, 'word': index, 'time': n, 'history_length': length, 'endpoint_ratio': R, 'history_value': value, 'reference_value': reference, 'ratio': value / reference, 'omitted_time_shift_difference': abs(wrong_time - reference)})
    P = np.zeros((6, 12), dtype=int)
    P[0, :4] = 1
    P[1, 4:8] = 1
    for e in range(4):
        P[e + 2, e] = 1
        P[e + 2, e + 4] = -1
        P[e + 2, 8 + (e + 1) % 4] = 1
        P[e + 2, 8 + e] = -1
    for N, beta in [(2, 0.4), (3, 0.6)]:
        angles = 2 * np.pi * np.arange(N) / N
        weight = np.exp(-beta * (angles[:, None] + 2 * np.pi * np.arange(-10, 11)) ** 2 / 2).sum(axis=1)
        coeff = np.fft.fft(weight).real / N
        flux = np.array(list(itertools.product(range(N), repeat=6)))
        charges = flux @ P % N
        fweights = np.prod(coeff[flux], axis=1)
        base = np.zeros(6, dtype=int)
        base[2] = 1
        J0 = base @ P
        shifts = [np.array([1, 0, 0, 0, 0, 0]), np.array([0, 0, 1, 1, 0, 0]), np.array([1, -1, 2, 0, -1, 0])]
        targets = [np.zeros(12, dtype=int), J0] + [J0 + shift @ P for shift in shifts]
        numer = np.zeros(len(targets), dtype=complex)
        denom = 0.0
        iterator = itertools.product(range(N), repeat=12)
        while True:
            batch = list(itertools.islice(iterator, 8192))
            if not batch:
                break
            links = np.array(batch)
            weights = np.prod(weight[links @ P.T % N], axis=1)
            denom += weights.sum()
            numer += np.sum(weights[:, None] * np.exp(2j * np.pi * (links @ np.array(targets).T) / N), axis=0)
        direct = numer / denom
        z = np.array([fweights[np.all(charges == target % N, axis=1)].sum() for target in targets])
        fourier = z / z[0]
        assert np.max(abs(direct - fourier)) < 2e-12
        comparisons = []
        for index, shift in enumerate(shifts):
            R = float(np.prod([max(coeff / coeff[(np.arange(N) + int(q)) % N]) for q in shift]))
            assert fourier[1] / R - 2e-12 <= fourier[index + 2] <= R * fourier[1] + 2e-12
            comparisons.append({'shift': shift.tolist(), 'R': R, 'base': float(fourier[1]), 'shifted': float(fourier[index + 2])})
        cube_rows.append({'N': N, 'beta': beta, 'link_assignments': N ** 12, 'plaquette_assignments': N ** 6, 'direct_fourier_discrepancy': float(np.max(abs(direct - fourier))), 'comparisons': comparisons})
    assert max((abs(x['ratio'] - 1) for x in rows)) > 0.01
    assert max((x['omitted_time_shift_difference'] for x in rows)) > 0.01
    return {'status': 'personal_finite_checks_not_independent_review', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'history_comparisons': rows, 'cube_current_fibers': cube_rows, 'limits': 'Finite Fourier fibers and actual histories; infinite state passage and dense-space spectral conclusion require the proof.'}


from pathlib import Path
import itertools, hashlib, json
import numpy as np

def check_local_charge_floor():
    rows = []
    D = np.zeros((4, 4), dtype=int)
    for e in range(4):
        D[e, e] = -1
        D[e, (e + 1) % 4] = 1
    for N, beta in [(2, 0.4), (3, 0.6), (4, 0.8)]:
        a = np.array(list(itertools.product(range(N), repeat=4)))
        size = len(a)
        theta = 2 * np.pi * np.arange(N) / N
        w = np.exp(-beta * (theta[:, None] + 2 * np.pi * np.arange(-10, 11)) ** 2 / 2).sum(axis=1)
        delta2 = float((w.min() / w.max()) ** 2)
        delta6 = float((w.min() / w.max()) ** 6)
        r = 1 - delta2
        assert 0 < r < 1
        Fourier = np.exp(2j * np.pi * (a @ a.T) / N) / np.sqrt(size)
        diff = (a[:, None, :] - a[None, :, :]) % N
        C = np.prod(w[diff], axis=2) / size
        root = np.sqrt(w[a.sum(axis=1) % N])
        T = root[:, None] * C * root[None, :]
        lam = np.linalg.eigvalsh(T)[-1]
        Tf = Fourier.conj().T @ T @ Fourier
        kernels = {}

        def kernel(rho):
            key = tuple(rho % N)
            if key not in kernels:
                K = np.zeros((size, size), dtype=complex)
                for eta in a:
                    K += np.prod(w[(diff + D @ eta) % N], axis=2) * np.exp(-2j * np.pi * (rho @ eta) / N) / size ** 2
                kernels[key] = K
            return kernels[key]
        K0 = kernel(np.zeros(4, dtype=int))
        assert np.max(abs(K0.imag)) < 2e-13 and K0.real.min() > 0
        cases = []
        for current in [np.array([1, 0, 0, 0]), np.array([1, 1, 0, 0]), np.array([1, 0, 1, 0]), np.array([N, 0, 0, 0])]:
            rho = D.T @ current
            charge = rho % N
            support = np.flatnonzero(charge)
            independent = []
            for bits in itertools.product((0, 1), repeat=len(support)):
                selected = [int(v) for v, bit in zip(support, bits) if bit]
                if all(((u - v) % 4 not in (1, 3) for u, v in itertools.combinations(selected, 2))) and len(selected) > len(independent):
                    independent = selected
            count = len(independent)
            bound = r ** count
            mask = np.flatnonzero(np.all(a @ D % N == charge, axis=1))
            assert len(mask) == N
            block = Tf[np.ix_(mask, mask)]
            ratio = float(np.linalg.eigvalsh(block)[-1] / lam)
            K = kernel(rho)
            projected = root[:, None] * K * root[None, :]
            direct_ratio = float(np.linalg.eigvalsh(projected)[-1] / lam)
            assert abs(ratio - direct_ratio) < 3e-12
            assert np.max(abs(K) - bound * K0.real) < 3e-13
            assert ratio <= bound + 3e-12 and ratio > 0
            energy = float(-np.log(ratio))
            floor = float(-count * np.log(r))
            floor6 = float(-count * np.log1p(-delta6))
            assert energy >= floor - 3e-12 and floor >= floor6 - 3e-12
            if not len(support):
                assert abs(ratio - 1) < 3e-12
            cases.append({'current': current.tolist(), 'charge': charge.tolist(), 'independent_vertices': independent, 'transfer_ratio': ratio, 'kernel_ratio_bound': bound, 'energy': energy, 'degree2_floor': floor, 'cubic_degree6_floor': floor6})
        harmonic = []
        for b0, b1 in itertools.product(range(N), repeat=2):
            probability = w[(b0 + np.arange(N)) % N] * w[(b1 - np.arange(N)) % N]
            probability /= probability.sum()
            assert probability.min() >= delta2 / N - 2e-13
            for q in range(1, N):
                value = abs(np.sum(probability * np.exp(2j * np.pi * q * np.arange(N) / N)))
                assert value <= r + 2e-13
                harmonic.append(float(value))
        assert abs(np.sum(probability)) - r > 1e-05
        rows.append({'N': N, 'beta': beta, 'min_max_weight_ratio': float(w.min() / w.max()), 'cases': cases, 'maximum_nontrivial_conditional_harmonic': max(harmonic), 'conditional_harmonic_bound': r, 'conditional_distributions': N * N, 'trivial_harmonic_exceeds_bound': float(1 - r)})
    return {'status': 'personal_finite_checks_not_independent_review', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'cases': rows, 'limits': 'Finite squares and exact charge projections; cubic degree6 and infinite history passage are analytic statements.'}

def main():
    result={'history_reconstruction':check_history_reconstruction(),'endpoint_comparison':check_endpoint_comparison(),'charge_floor':check_local_charge_floor()}
    print('EVIDENCE_JSON: '+json.dumps(result,sort_keys=True))
    print('per_element: positive local Fourier coefficients and temporal strip ratios are directly evaluated at finite N and beta.')
    print('per_site: explicit temporal-link gauge sums are matched to actual histories with changing intermediate external charges.')
    print('per_mode: finite history Gram matrices, transfer contractions, inverse spectra and prefix unitary relations are checked.')
    print('per_block: exact integer temporal-strip boundaries and full-cube clock sums are compared with positive current fibers.')
    print('lattice_wide: checked and not executed — the cofinal history limit and full-sector spectral bottom require the written proof.')
    print('TOTAL: PASS=3 FAIL=0')
if __name__=='__main__':main()
