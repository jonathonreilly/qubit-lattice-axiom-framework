#!/usr/bin/env python3
"""Checks for local finite-clock tensor constraints and their declared limits.
The paired note carries the general proof. No scientific input files or helpers.
"""
import itertools
import json
import traceback
import numpy as np
import sympy as sp
from scipy.linalg import null_space, expm
AUDIT_TIMEOUT_SEC = 90
x=sp.symbols('x:3')
pairs=[(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]

def symmetric(v):
    M = sp.zeros(3)
    for a, (i, j) in zip(v, pairs):
        M[i, j] = M[j, i] = a
    return M

def polynomial_space(degree, kind):
    mon = [sp.prod((x[j] ** a[j] for j in range(3))) for a in itertools.product(range(degree + 1), repeat=3) if sum(a) == degree]
    coef = sp.symbols('a:' + str(6 * len(mon)))
    M = symmetric([sum((coef[i * len(mon) + l] * v for l, v in enumerate(mon))) for i in range(6)])
    k = sp.Matrix(x)
    polys = list(M * k) if kind in ['vector', 'vector_trace'] else [k.dot(k) * sp.trace(M) - (k.T * M * k)[0]]
    if kind == 'vector_trace':
        polys.append(sp.trace(M))
    equations = []
    for p in polys:
        equations += sp.Poly(p, *x).coeffs()
    A = sp.linear_eq_to_matrix(equations, coef)[0]
    N = A.nullspace()
    return {'degree': degree, 'kind': kind, 'variables': len(coef), 'rank': A.rank(), 'nullity': len(N)}

def basis6():
    out = []
    for i, j in pairs:
        b = np.zeros((3, 3))
        b[i, j] = b[j, i] = 1 if i == j else 1 / np.sqrt(2)
        out.append(b)
    return np.array(out)

B=basis6()

def cross(k):
    a, b, c = k
    return np.array([[0, -c, b], [c, 0, -a], [-b, a, 0.0]])

def operators(k):
    k = np.asarray(k, dtype=float)
    Q = cross(k)
    R = np.array([[np.sum(a * (-Q @ b @ Q.T)) for b in B] for a in B])
    G = np.array([b @ k for b in B]).T
    tr = np.trace(B, axis1=1, axis2=2)
    S = tr @ R
    C = np.stack([Q @ (b - np.eye(3) * np.trace(b) / 2) for b in B], axis=-1).reshape(9, 6)
    K0 = np.eye(6) - np.outer(tr, tr) / 2
    return (R, G, S, C, K0)

def mode_checks():
    rows = []
    for k in [np.array([0.0, 0.0, 0.7]), np.array([0.2, 0.7, -1.1]), np.array([1.0, 2.0, 3.0])]:
        R, G, S, C, K0 = operators(k)
        q2 = k @ k
        assert np.max(abs(G @ R)) < 1e-13 and np.max(abs(G @ S)) < 1e-13
        assert np.max(abs(C @ S)) < 1e-13
        TT = null_space(np.vstack([G, S]))
        assert TT.shape == (6, 2)
        assert np.max(abs(TT.T @ R @ TT - q2 * np.eye(2))) < 1e-12
        assert np.max(abs(TT.T @ C.T @ C @ TT - q2 * np.eye(2))) < 1e-12
        J = 0.7
        g = 1.3
        spectra = []
        for name, K, V, power in [('L', J * C.T @ C, g * R.T @ R, 3), ('N', J * K0, g * R, 1)]:
            KT = TT.T @ K @ TT
            VT = TT.T @ V @ TT
            F = np.block([[np.zeros((2, 2)), KT], [-VT, np.zeros((2, 2))]])
            w = np.sort(abs(np.linalg.eigvals(F).imag))
            expected = np.sqrt(J * g) * q2 ** (power / 2)
            assert np.max(abs(w - expected)) < 2e-12
            spectra.append({'model': name, 'frequencies': w.tolist(), 'expected': float(expected)})
        rows.append({'k': k.tolist(), 'physical_pairs': TT.shape[1], 'spectra': spectra})
    return rows

def scalar_exact():
    J, g, U, V, k = sp.symbols('J g U V k', positive=True)
    K = sp.Matrix([[0, -J / sp.sqrt(2)], [-J / sp.sqrt(2), J / 2 + U * k * k]])
    b = -g * k * k + 2 * V * k ** 4
    B = sp.diag(b, 0)
    Z = sp.zeros(2)
    F = Z.row_join(K).col_join((-B).row_join(Z))
    assert sp.simplify(K.det() + J ** 2 / 2) == 0
    assert sp.simplify(F ** 4) == sp.zeros(4)
    assert sp.simplify(F ** 3) != sp.zeros(4)
    vals = {J: sp.Rational(7, 10), g: sp.Rational(13, 10), U: 3, V: 5, k: sp.Rational(1, 5)}
    A = np.array(F.subs(vals), dtype=float)
    t = 1.3
    poly = np.eye(4) + t * A + t * t * A @ A / 2 + t ** 3 * A @ A @ A / 6
    assert np.max(abs(expm(t * A) - poly)) < 1e-14
    return {'kinetic_determinant': str(sp.factor(K.det())), 'fourth_power_zero': True, 'third_power_generic_nonzero': True, 'scalar_characteristic_polynomial': str(F.charpoly().as_expr()), 'matrix_exponential_vs_cubic_error': float(np.max(abs(expm(t * A) - poly)))}

def incidence(L):
    sites = list(itertools.product(range(L), repeat=3))
    ids = {x: i for i, x in enumerate(sites)}
    n = len(sites)

    def sid(x):
        return ids[tuple((int(a) % L for a in x))]

    def col(x, a):
        return 6 * sid(x) + a
    G = np.zeros((3 * n, 6 * n), dtype=int)
    S = np.zeros((n, 6 * n), dtype=int)
    T = np.zeros_like(S)
    unit = np.eye(3, dtype=int)
    for s, site in enumerate(sites):
        v = np.array(site)
        for j in range(3):
            row = 3 * s + j
            G[row, col(v + unit[j], j)] += 1
            G[row, col(v, j)] -= 1
            T[s, col(v, j)] = 1
            for i in range(3):
                if i == j:
                    continue
                a = pairs.index(tuple(sorted((i, j))))
                G[row, col(v, a)] += 1
                G[row, col(v - unit[i], a)] -= 1
                S[s, col(v + unit[i], j)] += 1
                S[s, col(v - unit[i], j)] += 1
                S[s, col(v, j)] -= 2
        for a, (i, j) in enumerate(pairs[3:], 3):
            S[s, col(v, a)] -= 1
            S[s, col(v - unit[i], a)] += 1
            S[s, col(v - unit[j], a)] += 1
            S[s, col(v - unit[i] - unit[j], a)] -= 1
    assert np.max(abs(G @ S.T)) == 0
    return (G, S, T, sites)

def static_check():
    rows = []
    for L in [3, 5]:
        G, S, T, sites = incidence(L)
        n = len(sites)
        A = np.vstack([G, T])
        w = np.tile([1.0, 1.0, 1.0, 2.0, 2.0, 2.0], n)
        wi = 1 / w
        rho = np.zeros(n)
        rho[0] = 1
        rho[1] = -1
        b = np.r_[np.zeros(3 * n), rho]
        gram = A * wi @ A.T
        dual = np.linalg.lstsq(gram, b, rcond=1e-12)[0]
        field = wi * (A.T @ dual)
        residual = np.max(abs(A @ field - b))
        assert residual < 2e-12
        energy = np.dot(w * field, field) / 2
        assert abs(energy - np.dot(rho, rho) / 4) < 2e-12
        rho2 = np.zeros(n)
        rho2[-1] = 1
        rho2[-2] = -1
        b2 = np.r_[np.zeros(3 * n), rho2]
        dual2 = np.linalg.lstsq(gram, b2, rcond=1e-12)[0]
        field2 = wi * (A.T @ dual2)
        assert np.max(abs(A @ field2 - b2)) < 2e-12
        crossenergy = np.dot(w * field, field2)
        assert abs(crossenergy) < 2e-12
        assert np.max(abs(field)) > 0
        rows.append({'L': L, 'sites': n, 'integer_G_S_transpose_zero': bool(np.max(abs(G @ S.T)) == 0), 'scalar_source_sum': float(rho.sum()), 'minimum_energy_over_g': float(energy), 'independent_contact_prediction': float(np.dot(rho, rho) / 4), 'constraint_residual': float(residual), 'disjoint_neutral_cross_energy_over_g': float(crossenergy), 'constraint_ranks': [int(np.linalg.matrix_rank(G)), int(np.linalg.matrix_rank(S))]})
    return rows

def clock_alias_checks():
    G, S, T, sites = incidence(5)
    n = len(sites)
    dim = 6 * n
    assert np.max(abs(G).sum(axis=1)) == 6 and np.max(abs(S).sum(axis=1)) == 36
    rng = np.random.default_rng(9140535)
    rows = []
    for N in [7, 11, 17, 101]:
        beta = np.zeros(n, dtype=int)
        beta[0] = (N - 1) // 2
        m = S.T @ beta
        m = (m + N // 2) % N - N // 2
        assert np.max(abs(G @ m)) > 0 and np.max(abs(G @ m % N)) == 0
        alpha = rng.integers(-N // 2, N // 2 + 1, 3 * n)
        r = G.T @ alpha
        r = (r + N // 2) % N - N // 2
        assert np.max(abs(S @ r)) > 0 and np.max(abs(S @ r % N)) == 0
        rows.append({'N': N, 'h_character_largest_integer_syndrome': int(np.max(abs(G @ m))), 'E_character_largest_integer_syndrome': int(np.max(abs(S @ r))), 'modular_syndromes_zero': True, 'not_a_constructed_linear_phase': True})
    trials = []
    for M in [1, 2, 3]:
        N = 36 * M + 1
        for _ in range(20):
            m = rng.integers(-M, M + 1, dim)
            r = rng.integers(-M, M + 1, dim)
            gm = G @ m
            sr = S @ r
            assert np.max(abs(gm)) < N and np.max(abs(sr)) < N
            assert bool(np.all(gm % N == 0)) == bool(np.all(gm == 0))
            assert bool(np.all(sr % N == 0)) == bool(np.all(sr == 0))
        trials.append({'M': M, 'N': N, 'words': 20})
    return {'row_l1_norms': [6, 36], 'alias_witnesses': rows, 'lifting_checks': trials}

def mixed_modes():
    rows = []
    rng = np.random.default_rng(9140536)
    A = rng.normal(size=(15, 15))
    W = A.T @ A + np.eye(15)
    for direction in [np.array([0.0, 0.0, 1.0]), np.array([1.0, 2.0, -3.0]) / np.sqrt(14)]:
        scaled = []
        for kscale in [0.2, 0.1, 0.05, 0.025]:
            k = kscale * direction
            R, G, S, C, K0 = operators(k)
            TT = null_space(np.vstack([G, S]))
            D = np.block([[R @ TT, np.zeros((6, 2))], [np.zeros((9, 2)), 1j * C @ TT]])
            H = D.conj().T @ W @ D
            Rn, Gn, Sn, Cn, K0n = operators(-k)
            Dn = np.block([[Rn @ TT, np.zeros((6, 2))], [np.zeros((9, 2)), 1j * Cn @ TT]])
            Hn = Dn.conj().T @ W @ Dn
            assert np.max(abs(Hn-H.conj())) < 1e-13
            J = np.block([[np.zeros((2, 2)), np.eye(2)], [-np.eye(2), np.zeros((2, 2))]])
            assert np.max(abs(H - H.conj().T)) < 1e-13
            F = J @ H
            scale = np.diag([1.0, 1.0, kscale, kscale])
            rescaled = np.linalg.solve(scale, F @ scale) / kscale ** 3
            eig = np.linalg.eigvals(F)
            assert np.max(abs(eig.real)) < 1e-12
            scaled.append(np.sort(abs(eig.imag)) / kscale ** 3)
            rows.append({'direction': direction.tolist(), 'k': kscale, 'frequency_over_k_cubed': scaled[-1].tolist(), 'rescaled_operator_norm': float(np.linalg.norm(rescaled, 2))})
        assert max((np.max(abs(scaled[0] - a)) for a in scaled[1:])) < 1e-10
    return rows

def fields_from_source(rho, L):
    rh = np.fft.fftn(rho.reshape((L,) * 3))
    freq = 2 * np.pi * np.fft.fftfreq(L)
    rf = np.zeros((L, L, L, 6), dtype=complex)
    hf = np.zeros_like(rf)
    green = 0.0
    for ind in itertools.product(range(L), repeat=3):
        k = np.array([freq[i] for i in ind])
        qh = 2 * np.sin(k / 2)
        q2 = qh @ qh
        if q2 < 1e-20:
            continue
        P = np.eye(3) - np.outer(qh, qh) / q2
        for a, (i, j) in enumerate(pairs):
            offset = np.zeros(3)
            if i != j:
                offset[i] = offset[j] = 0.5
            phase = np.exp(1j * k @ offset)
            rf[ind + (a,)] = rh[ind] * P[i, j] * phase / 2
            hf[ind + (a,)] = -rh[ind] * P[i, j] * phase / (2 * q2)
        green += abs(rh[ind]) ** 2 / q2
    R = np.fft.ifftn(rf, axes=(0, 1, 2))
    h = np.fft.ifftn(hf, axes=(0, 1, 2))
    assert np.max(abs(R.imag)) < 1e-13 and np.max(abs(h.imag)) < 1e-13
    return (R.real.reshape(-1), h.real.reshape(-1), green / L ** 3)

def eps(i, j, k):
    if len({i, j, k}) < 3:
        return 0
    return (-1) ** sum((a > b for a, b in [(i, j), (i, k), (j, k)]))

def curvature_matrices(L):
    G, S, T, sites = incidence(L)
    n = len(sites)
    ids = {tuple(x): i for i, x in enumerate(sites)}
    unit = np.eye(3, dtype=int)
    offsets = [np.zeros(3, dtype=int) if i == j else unit[i] + unit[j] for i, j in pairs]

    def column(pos, i, j):
        a = pairs.index(tuple(sorted((i, j))))
        v = np.asarray(pos) - offsets[a]
        assert not np.any(v % 2)
        site = tuple(v // 2 % L)
        return 6 * ids[site] + a
    R = np.zeros((6 * n, 6 * n), dtype=int)
    C = np.zeros((9 * n, 6 * n), dtype=int)
    for v0, site in enumerate(sites):
        site = 2 * np.array(site)
        for out, (i, j) in enumerate(pairs):
            pos = site + offsets[out]
            row = 6 * v0 + out
            for a, b, c, d in itertools.product(range(3), repeat=4):
                coef = eps(i, a, b) * eps(j, c, d) * (2 if b == d else 1)
                if not coef:
                    continue
                for sa, sc in itertools.product([-1, 1], repeat=2):
                    R[row, column(pos + sa * unit[a] + sc * unit[c], b, d)] += coef * sa * sc
        for i, j in itertools.product(range(3), repeat=2):
            parity = np.ones(3, dtype=int) if i == j else unit[3 - i - j]
            pos = site + parity
            row = 9 * v0 + 3 * i + j
            for a, b in itertools.product(range(3), repeat=2):
                coef = eps(i, a, b)
                if not coef:
                    continue
                for sign in [-1, 1]:
                    point = pos + sign * unit[a]
                    C[row, column(point, b, j)] += 2 * coef * sign
                    if b == j:
                        for c in range(3):
                            C[row, column(point, c, c)] -= coef * sign
    assert np.max(abs(R - R.T)) == 0
    assert np.max(abs(G @ R)) == 0 and np.max(abs(R @ G.T)) == 0
    assert np.max(abs(C @ S.T)) == 0
    assert np.max(abs(T @ R - 2 * S)) == 0
    return (G, S, T, R, C, sites)

def source_field_checks():
    rows = []
    for L in [3, 5]:
        G, S, T, sites = incidence(L)
        n = len(sites)
        w = np.tile([1.0, 1.0, 1.0, 2.0, 2.0, 2.0], n)
        rho = np.zeros(n)
        rho[0] = 1
        rho[1] = -1
        R, h, green = fields_from_source(rho, L)
        assert np.max(abs(G @ R)) < 1e-13 and np.max(abs(T @ R - rho)) < 1e-13
        assert np.max(abs(S @ (w * h) - rho)) < 1e-13
        assert np.max(abs(R.reshape(n, 6).mean(axis=0))) < 1e-13
        A = np.vstack([G, T])
        b = np.r_[np.zeros(3 * n), rho]
        wi = 1 / w
        v = wi * (A.T @ np.linalg.lstsq(A * wi @ A.T, b, rcond=1e-12)[0])
        assert np.max(abs(v - R)) < 2e-13
        El = np.dot(w * R, R) / 2
        En = np.dot(w * h, R) / 2
        assert abs(El - np.dot(rho, rho) / 4) < 1e-13
        assert abs(En + green / 4) < 1e-13
        rows.append({'L': L, 'Fourier_vs_real_variational_field_error': float(np.max(abs(v - R))), 'actual_metric_scalar_constraint_error': float(np.max(abs(S @ (w * h) - rho))), 'L_static_energy_over_g': float(El), 'N_static_energy_over_g': float(En), 'independent_inverse_Laplacian_value': float(-green / 4)})
    return rows

def integer_curvature_checks():
    rows = []
    for L in [3, 5]:
        G, S, T, R, C, sites = curvature_matrices(L)
        n = len(sites)
        rng = np.random.default_rng(9140541)
        q = rng.normal(size=6 * n)
        p = rng.normal(size=6 * n)
        alpha = rng.normal(size=3 * n)
        beta = rng.normal(size=n)
        assert np.max(abs(R @ (q + G.T @ alpha) - R @ q)) < 1e-13
        assert np.max(abs(C @ (p + S.T @ beta) - C @ p)) < 1e-13
        rows.append({'L': L, 'sites': n, 'G_R_zero': True, 'R_G_transpose_zero': True, 'C_S_transpose_zero': True, 'trace_R_equals_2S': True, 'R_symmetric': True, 'largest_R_character_coefficient': int(np.max(abs(R))), 'largest_C_character_coefficient': int(np.max(abs(C))), 'maximum_R_row_l1': int(np.max(abs(R).sum(axis=1))), 'maximum_C_row_l1': int(np.max(abs(C).sum(axis=1)))})
    return rows

def clock_generator_checks():
    rows = []
    for N in [3, 7, 11]:
        omega = np.exp(2j*np.pi/N)
        X = np.diag(omega**np.arange(N))
        Z = np.roll(np.eye(N), 1, axis=0)
        error = np.max(abs(X@Z-omega*Z@X))
        assert error < 3e-15
        penalty = np.eye(N)-(X+X.conj().T)/2
        spectrum = np.linalg.eigvalsh(penalty)
        assert abs(spectrum[0]) < 1e-14
        assert abs(spectrum[1]-(1-np.cos(2*np.pi/N))) < 1e-14
        assert spectrum[-1] <= 2+1e-14
        rows.append({'N':N,'clock_relation_error':float(error),'single_penalty_gap':float(spectrum[1])})
    return rows

def check_polynomial_and_physical_modes():
    spaces=[polynomial_space(d,t) for t,d in [('vector',0),('vector',1),('vector',2),('scalar',0),('scalar',1),('vector_trace',2),('vector_trace',3)]]
    assert [s['nullity'] for s in spaces]==[0,0,6,0,8,0,5]
    print(json.dumps({'polynomial_spaces':spaces,'physical_modes':mode_checks(),'finite_penalty_scalar_block':scalar_exact()},sort_keys=True))

def check_integer_clock_dynamics():
    print(json.dumps({'integer_curvature':integer_curvature_checks(),'modular_lift_and_aliases':clock_alias_checks(),'actual_clock_generators':clock_generator_checks()},sort_keys=True))

def check_static_physical_sources():
    print(json.dumps({'direct_real_space_variational_minimum':static_check(),'actual_metric_Fourier_field':source_field_checks()},sort_keys=True))

def check_mixed_character_scaling():
    print(json.dumps({'Hermitian_mixed_character_dynamics':mixed_modes()},sort_keys=True))

def main():
    checks=[check_polynomial_and_physical_modes,check_integer_clock_dynamics,check_static_physical_sources,check_mixed_character_scaling]
    failed=0
    for check in checks:
        try:
            check()
            print('PASS: '+check.__name__,flush=True)
        except Exception:
            failed+=1
            traceback.print_exc()
            print('FAIL: '+check.__name__,flush=True)
    print('per_element: exact polynomial constraints and scalar Jordan identities challenge derivative order and penalty claims')
    print('per_site: integer site-face stencils and actual clock-character syndromes test the declared local Hamiltonian')
    print('per_mode: non-axial transverse-traceless reduction and Hermitian mixed dynamics challenge the dispersion comparison')
    print('per_block: real-space constrained minimization is checked against the actual Fourier metric field and source incidence')
    print('lattice_wide: analytic moment and stencil proofs have stated quantifiers; no interacting finite-N phase follows from finite examples')
    print(f'TOTAL: PASS={len(checks)-failed} FAIL={failed}')
    return int(failed>0)

if __name__=='__main__':
    raise SystemExit(main())
