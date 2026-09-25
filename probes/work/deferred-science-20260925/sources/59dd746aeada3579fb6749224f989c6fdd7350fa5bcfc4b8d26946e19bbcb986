"""Own complete physical-tree GKLS calculation, with two possible births."""
from itertools import product
from pathlib import Path
import json
import platform
import numpy as np
import scipy
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
A = (0, 1)
EDGES = ((0, 2), (0, 3), (0, 4), (1, 4), (1, 5))
NV = 6


def triples(matrix):
    rows, cols = np.nonzero(matrix)
    return [[int(r), int(c), int(matrix[r, c])] for r, c in zip(rows, cols)]


def flow(q):
    result = []
    for deleted, (a, b) in enumerate(EDGES):
        reached, pending = {a}, [a]
        while pending:
            u = pending.pop()
            for i, (x, y) in enumerate(EDGES):
                if i == deleted:
                    continue
                if x == u and y not in reached:
                    reached.add(y); pending.append(y)
                if y == u and x not in reached:
                    reached.add(x); pending.append(x)
        result.append(sum(q[v] - int(v in A) for v in reached))
    div = [0] * NV
    for value, (a, b) in zip(result, EDGES):
        div[a] += value; div[b] -= value
    assert div == [q[v] - int(v in A) for v in range(NV)]
    return tuple(result)


def build():
    words = [q for q in product((-1, 0, 1), repeat=NV) if sum(q) == len(A)]
    index = {q: i for i, q in enumerate(words)}
    fields = [flow(q) for q in words]
    full_n = len(words)
    F = {a: np.zeros((full_n, full_n), dtype=np.int64) for a in A}
    j = {(e, sign): np.zeros((full_n, full_n), dtype=np.int64)
         for e in range(len(EDGES)) for sign in (-1, 1)}
    for col, q in enumerate(words):
        for e, (a, b) in enumerate(EDGES):
            if q[a] and not q[b]:
                r = list(q); r[b] = q[a]; r[a] = 0; r = tuple(r)
                expected = list(fields[col]); expected[e] -= q[a]
                assert fields[index[r]] == tuple(expected)
                F[a][index[r], col] += 1
            if not q[a] and not q[b]:
                for sign in (-1, 1):
                    r = list(q); r[a] = sign; r[b] = -sign; r = tuple(r)
                    expected = list(fields[col]); expected[e] += sign
                    assert fields[index[r]] == tuple(expected)
                    j[e, sign][index[r], col] += 1
    keep = [i for i, q in enumerate(words) if all(q[a] for a in A)]
    qwords = [words[i] for i in keep]
    S = F[1] @ F[0][:, keep]
    H4 = -2 * S.T @ S
    resolved = {(e, sign): (j[e, sign] @ F[a][:, keep])[keep, :]
                for e, (a, b) in enumerate(EDGES) for sign in (-1, 1)}
    coherent = {e: resolved[e, -1] + resolved[e, 1] for e in range(len(EDGES))}
    D = []
    for i in keep:
        q, electric = words[i], fields[i]
        value = sum(electric[e] * (electric[e] - q[a])
                    for e, (a, b) in enumerate(EDGES) if q[b] == 0)
        assert value >= 0
        D.append(value)
    number = np.array([sum(abs(x) for x in q) for q in qwords])
    charge = np.array(qwords)
    N = np.diag(number)
    assert np.array_equal(N @ H4, H4 @ N)
    for B in [*resolved.values(), *coherent.values()]:
        assert np.array_equal(N @ B - B @ N, 2 * B)
    initial = qwords.index((1, 1, 0, 0, 0, 0))
    return locals()


def liouvillian(H, jumps, kappa, include_loss=True, include_recycling=True):
    n = len(H); I = sparse.eye(n, format='csr')
    Hs = sparse.csr_matrix(H)
    generator = -1j * (sparse.kron(I, Hs) - sparse.kron(Hs.T, I))
    for B in jumps:
        b = sparse.csr_matrix(B)
        loss = b.T @ b
        if include_recycling:
            generator += kappa * sparse.kron(b, b)
        if include_loss:
            generator -= 0.5 * kappa * (sparse.kron(I, loss) + sparse.kron(loss.T, I))
    return generator.tocsr()


def main():
    built = build()
    qwords, H4, D = built['qwords'], built['H4'], built['D']
    number, charge, initial = built['number'], built['charge'], built['initial']
    n = len(qwords)
    rho0 = np.zeros((n, n), dtype=complex); rho0[initial, initial] = 1
    vec0 = rho0.reshape(-1, order='F')
    rows, derivative_rows, mutations = [], [], []
    for label in ('resolved', 'coherent'):
        jumps = list(built[label].values())
        for K in (0.0, 2.0, 200.0):
            delta, kappa = 0.3, 0.4
            H = K * np.diag(D) + delta * H4
            G = liouvillian(H, jumps, kappa)
            drho = (G @ vec0).reshape((n, n), order='F')
            pprime = np.diag(drho).real
            dq = charge - charge[initial]
            derivative_rows.append({'instrument': label, 'K': K, 'delta': delta, 'kappa': kappa,
                                     'trace_derivative': float(np.trace(drho).real),
                                     'mean_slope': (pprime @ dq).tolist(),
                                     'covariance_slope': (dq.T @ (pprime[:, None] * dq)).tolist()})
            for t in (0.0001, 0.0002, 0.0004, 0.01):
                rho = expm_multiply(t * G, vec0).reshape((n, n), order='F')
                p = np.diag(rho).real
                mean = p @ charge
                cov = charge.T @ (p[:, None] * charge) - np.outer(mean, mean)
                first = np.array(derivative_rows[-1]['covariance_slope'])
                rows.append({'instrument': label, 'K': K, 'delta': delta, 'kappa': kappa, 't': t,
                             'trace_real': float(np.trace(rho).real),
                             'trace_imag': float(np.trace(rho).imag),
                             'hermiticity_max': float(np.max(np.abs(rho - rho.conj().T))),
                             'min_eigenvalue': float(np.linalg.eigvalsh(rho)[0]),
                             'mean_charge': mean.tolist(), 'covariance': cov.tolist(),
                             'number_probabilities': {str(N): float(sum(p[number == N])) for N in (2, 4, 6)},
                             'total_charge_mean': float(sum(mean)),
                             'max_abs_covariance_remainder_over_t2': float(np.max(np.abs(cov - t * first)) / t**2),
                             'pearson_0_2': float(cov[0, 2] / np.sqrt(cov[0, 0] * cov[2, 2]))})
        H = 2.0 * np.diag(D) + 0.3 * H4
        for name, loss, recycling in [('drop_loss', False, True), ('drop_recycling', True, False)]:
            G = liouvillian(H, jumps, 0.4, loss, recycling)
            rho = expm_multiply(0.01 * G, vec0).reshape((n, n), order='F')
            mutations.append({'instrument': label, 'mutation': name,
                              'trace': float(np.trace(rho).real),
                              'N6_probability': float(np.diag(rho).real[number == 6].sum())})
        G = liouvillian(H, jumps, 0.0)
        pure = expm_multiply(0.01 * G, vec0).reshape((n, n), order='F')
        assert np.max(np.abs(pure - rho0)) < 1e-12
    result = {
        'scope': 'Exact finite physical tree, not a rotor truncation; full original GKLS and both possible later births.',
        'environment': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
        'A': A, 'edges_A_to_B': EDGES, 'full_charge_words': built['words'], 'full_fields': built['fields'],
        'P_full_indices': built['keep'], 'P_charge_words': qwords, 'D': D,
        'F_columns': {str(a): triples(B) for a, B in built['F'].items()},
        'j_columns': {str(e) + ':' + str(sign): triples(B) for (e, sign), B in built['j'].items()},
        'S_columns': triples(built['S']), 'H4_columns': triples(H4),
        'resolved_B_columns': {str(e) + ':' + str(sign): triples(B) for (e, sign), B in built['resolved'].items()},
        'coherent_B_columns': {str(e): triples(B) for e, B in built['coherent'].items()},
        'number': number.tolist(), 'initial_P_index': initial,
        'derivative_rows': derivative_rows, 'finite_time_rows': rows, 'mutations': mutations,
    }
    (HERE / 'TREE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'result': 'TREE_RESULTS.json', 'full_dimension': len(built['words']),
                      'P_dimension': n, 'finite_time_rows': len(rows),
                      'largest_trace_error': max(abs(row['trace_real'] - 1) for row in rows),
                      'smallest_later_N6_probability': min(row['number_probabilities']['6'] for row in rows),
                      'mutations': mutations, 'environment': result['environment']}, indent=2))


if __name__ == '__main__':
    main()
