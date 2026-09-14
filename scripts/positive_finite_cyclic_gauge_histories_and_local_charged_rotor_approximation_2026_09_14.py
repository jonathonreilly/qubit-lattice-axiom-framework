#!/usr/bin/env python3
"""Author checks for positive finite cyclic gauge histories and local rotor approximation.

This runner has no scientific file inputs. It compares independent finite
representations and falsifiers; the general bounds are proved in the note.
Passing these checks does not establish an interacting thermodynamic phase
or constitute independent scientific review.
"""
AUDIT_TIMEOUT_SEC = 90

_ASSERTIONS = 0

def require(condition, label):
    global _ASSERTIONS
    _ASSERTIONS += 1
    if not condition:
        print("FAIL:", label, flush=True)
        raise AssertionError(label)

def check_positive_trace():
    import itertools
    import numpy as np
    from scipy.linalg import expm

    def annihilator(mode, nmodes):
        a = np.zeros((2 ** nmodes, 2 ** nmodes), complex)
        for n in range(2 ** nmodes):
            if n >> mode & 1:
                a[n ^ 1 << mode, n] = (-1) ** (n & (1 << mode) - 1).bit_count()
        return a

    def fixture(N, beta=0.71, tel=0.43):
        X = np.roll(np.eye(N), 1, axis=0)
        om = np.exp(2j * np.pi / N)
        Z = np.diag(om ** np.arange(N))
        a = [annihilator(i, 4) for i in range(4)]
        num = [z.conj().T @ z for z in a]
        Q = [num[0] - num[2], num[1] - num[3]]
        He = np.kron(tel * (2 * np.eye(N) - X - X.T), np.eye(16))
        h = []
        hm = []
        for q in range(N):
            hp = np.array([[0.31, (0.8 + 0.37j) * om ** q], [(0.8 - 0.37j) * om ** (-q), -0.67]])
            h.append(hp)
            block = sum((hp[i, j] * a[i].conj().T @ a[j] + hp[i, j].conjugate() * a[i + 2].conj().T @ a[j + 2] for i in range(2) for j in range(2)))
            hm.append(block)
        Hm = np.zeros_like(He, dtype=complex)
        for q, block in enumerate(hm):
            Hm[q * 16:(q + 1) * 16, q * 16:(q + 1) * 16] = block
        gam = [np.kron(np.linalg.matrix_power(X, d), expm(2j * np.pi * Q[x] / N)) for x, d in enumerate([1, -1])]
        P = sum((np.linalg.matrix_power(gam[0], s0) @ np.linalg.matrix_power(gam[1], s1) for s0, s1 in itertools.product(range(N), repeat=2))) / N ** 2
        require(np.linalg.norm(P @ P - P) < 1e-12, 'positive_trace assertion from exploratory source line 31')
        require(np.linalg.norm(P - P.conj().T) < 1e-12, 'positive_trace assertion from exploratory source line 32')
        for G in gam:
            require(np.linalg.norm(G @ Hm - Hm @ G) < 1e-12, 'positive_trace assertion from exploratory source line 34')
            require(np.linalg.norm(G @ He - He @ G) < 1e-12, 'positive_trace assertion from exploratory source line 35')
        H = He + Hm
        exact = np.trace(P @ expm(-beta * H))
        out = {'N': N, 'physical_dimension': round(np.trace(P).real), 'exact_partition': exact.real, 'slices': []}
        require(abs(exact.imag) < 1e-12, 'positive_trace assertion from exploratory source line 39')
        for M in [1, 2, 3, 4]:
            delta = beta / M
            K = expm(-delta * tel * (2 * np.eye(N) - X - X.T))
            A = [expm(-delta * x) for x in h]
            require(K.min() >= 0 and np.linalg.norm(K.sum(axis=0) - 1) < 1e-12, 'positive_trace assertion from exploratory source line 42')
            T = expm(-delta * He) @ expm(-delta * Hm)
            direct = np.trace(P @ np.linalg.matrix_power(T, M))
            terms = []
            maxsinglephase = 0
            badcomplex = 0
            badtotal = 0j
            for s0, s1 in itertools.product(range(N), repeat=2):
                R = np.diag([om ** s0, om ** s1])
                shift = s0 - s1
                for qs in itertools.product(range(N), repeat=M):
                    B = np.eye(2, dtype=complex)
                    for q in qs:
                        B = A[q] @ B
                    detplus = np.linalg.det(np.eye(2) + R @ B)
                    detminus = np.linalg.det(np.eye(2) + (R @ B).conjugate())
                    require(abs(detminus - detplus.conjugate()) < 1e-12, 'positive_trace assertion from exploratory source line 53')
                    maxsinglephase = max(maxsinglephase, abs(detplus.imag))
                    end = (qs[0] - shift) % N
                    weight = K[end, qs[-1]]
                    for j in range(M - 1):
                        weight *= K[qs[j + 1], qs[j]]
                    val = weight * abs(detplus) ** 2 / N ** 2
                    terms.append(val)
                    bad = detplus * np.linalg.det(np.eye(2) + R @ B.conjugate())
                    badcomplex = max(badcomplex, abs(bad.imag))
                    badtotal += weight * bad / N ** 2
            require(maxsinglephase > 1e-3, 'single charged determinant has a nonzero phase')
            require(badcomplex > 1e-3, 'wrong temporal conjugation gives a complex weight')
            measure = sum(terms)
            require(abs(direct - measure) < 2e-10, 'positive_trace assertion from exploratory source line 63')
            out['slices'].append({'M': M, 'operator_trace': direct.real, 'positive_history_sum': measure, 'min_summand': min(terms), 'max_single_species_imaginary_part': maxsinglephase, 'wrong_temporal_conjugation_max_imaginary_part': badcomplex, 'wrong_temporal_conjugation_total': {'real': badtotal.real, 'imag': badtotal.imag}, 'trotter_error': abs(direct - exact)})
        return out
    result = [fixture(N) for N in [3, 4, 5]]
    for r in result:
        print('N', r['N'], 'physical_dimension', r['physical_dimension'], 'partition', r['exact_partition'])
        for z in r['slices']:
            print(' slices', z['M'], 'trace mismatch', abs(z['operator_trace'] - z['positive_history_sum']), 'trotter error', z['trotter_error'], 'single phase', z['max_single_species_imaginary_part'], 'wrong temporal phase', z['wrong_temporal_conjugation_max_imaginary_part'])

def check_charge_interaction():
    import itertools
    import numpy as np
    from scipy.linalg import expm

    def annihilator(mode, nmodes):
        a = np.zeros((2 ** nmodes, 2 ** nmodes), complex)
        for n in range(2 ** nmodes):
            if n >> mode & 1:
                a[n ^ 1 << mode, n] = (-1) ** (n & (1 << mode) - 1).bit_count()
        return a
    N = 3
    beta = 0.63
    tel = 0.39
    u = np.array([0.7, 1.1])
    omega = np.exp(2j * np.pi / N)
    X = np.roll(np.eye(N), 1, axis=0)
    aa = [annihilator(i, 4) for i in range(4)]
    num = [a.conj().T @ a for a in aa]
    Q = [num[0] - num[2], num[1] - num[3]]
    uf = sum((u[i] * Q[i] @ Q[i] / 2 for i in range(2)))
    HU = np.kron(np.eye(N), uf)
    He = np.kron(tel * (2 * np.eye(N) - X - X.T), np.eye(16))
    hs = []
    Hm = np.zeros_like(He, dtype=complex)
    for q in range(N):
        h = np.array([[0.23, (0.6 + 0.29j) * omega ** q], [(0.6 - 0.29j) * omega ** (-q), -0.41]])
        hs.append(h)
        Hm[q * 16:(q + 1) * 16, q * 16:(q + 1) * 16] = sum((h[i, j] * aa[i].conj().T @ aa[j] + h[i, j].conjugate() * aa[i + 2].conj().T @ aa[j + 2] for i in range(2) for j in range(2)))
    G = [np.kron(np.linalg.matrix_power(X, d), expm(2j * np.pi * Q[j] / N)) for j, d in enumerate([1, -1])]
    P = sum((np.linalg.matrix_power(G[0], s0) @ np.linalg.matrix_power(G[1], s1) for s0, s1 in itertools.product(range(N), repeat=2))) / N ** 2
    exact = np.trace(P @ expm(-beta * (He + HU + Hm)))
    out = []
    for M in [1, 2, 3]:
        dt = beta / M
        theta = np.arccos(np.exp(-dt * u / 2))
        A = [expm(-dt * h) for h in hs]
        K = expm(-dt * tel * (2 * np.eye(N) - X - X.T))
        for j in range(2):
            require(np.linalg.norm(expm(-dt * u[j] * Q[j] @ Q[j] / 2) - (expm(1j * theta[j] * Q[j]) + expm(-1j * theta[j] * Q[j])) / 2) < 1e-12, 'charge_interaction assertion from exploratory source line 20')
        HS = [np.diag(np.exp(1j * theta * np.array(z))) for z in itertools.product([-1, 1], repeat=2)]
        direct = np.trace(P @ np.linalg.matrix_power(expm(-dt * (He + HU)) @ expm(-dt * Hm), M))
        total = 0
        smallest = 1000000000.0
        for s0, s1 in itertools.product(range(N), repeat=2):
            R = np.diag([omega ** s0, omega ** s1])
            shift = s0 - s1
            for qs in itertools.product(range(N), repeat=M):
                scalar = K[(qs[0] - shift) % N, qs[-1]]
                for j in range(M - 1):
                    scalar *= K[qs[j + 1], qs[j]]
                for fields in itertools.product(range(4), repeat=M):
                    B = np.eye(2, dtype=complex)
                    for q, field in zip(qs, fields):
                        B = HS[field] @ A[q] @ B
                    weight = scalar * abs(np.linalg.det(np.eye(2) + R @ B)) ** 2 / (N * N * 4 ** M)
                    total += weight
                    smallest = min(smallest, weight)
        require(abs(direct - total) < 5e-11, 'charge_interaction assertion from exploratory source line 33')
        out.append({'M': M, 'operator_trace': direct.real, 'positive_HS_sum': total, 'difference': abs(direct - total), 'minimum_weight': smallest, 'trotter_error': abs(direct - exact)})
    for z in out:
        print(z)

def check_clock_rotor():
    import math
    import numpy as np
    from scipy.sparse import coo_matrix
    from scipy.sparse.linalg import expm_multiply
    L = 4
    g = 0.7
    r = 0.25
    kappa = 1 / g ** 2
    time = 0.65

    def flux(a, b, n):
        charge = np.zeros(L, dtype=int)
        charge[a] += 1
        charge[b] -= 1
        return tuple(np.r_[np.cumsum(charge)[:L - 1], 0] + n)

    def divergence(e):
        return tuple((e[i] - e[(i - 1) % L] for i in range(L)))

    def assemble(S, cyclic):
        N = 2 * S + 1
        basis = []
        for a in range(L):
            for b in range(L):
                for n in range(-S, S + 1):
                    e = flux(a, b, n)
                    if cyclic:
                        e = tuple(((v + S) % N - S for v in e))
                    if all((abs(v) <= S for v in e)):
                        basis.append((a, b, e))
        ix = {v: i for i, v in enumerate(basis)}
        rows = []
        cols = []
        vals = []

        def add(i, target, z):
            if cyclic:
                target = (target[0], target[1], tuple(((v + S) % N - S for v in target[2])))
            if target in ix:
                rows.append(ix[target])
                cols.append(i)
                vals.append(z)
        for i, (a, b, e) in enumerate(basis):
            lam = lambda n: g * g * N * N / (2 * math.pi ** 2) * math.sin(math.pi * n / N) ** 2 if cyclic else g * g * n * n / 2
            add(i, (a, b, e), sum((lam(v) for v in e)) + kappa)
            for orient in [-1, 1]:
                add(i, (a, b, tuple((v + orient for v in e))), -kappa / 2)
            for l in range(L):
                x = l
                y = (l + 1) % L
                for pos, species, charge in [(a, 0, 1), (b, 1, -1)]:
                    if pos == y:
                        new = list(e)
                        new[l] += charge
                        add(i, (x if species == 0 else a, x if species == 1 else b, tuple(new)), r)
                    if pos == x:
                        new = list(e)
                        new[l] -= charge
                        add(i, (y if species == 0 else a, y if species == 1 else b, tuple(new)), r)
        H = coo_matrix((vals, (rows, cols)), shape=(len(basis), len(basis))).tocsr()
        require(np.linalg.norm((H - H.T).data) < 1e-12, 'clock_rotor assertion from exploratory source line 42')
        init = np.zeros(len(basis))
        init[ix[0, 0, (0,) * L]] = 1
        state = expm_multiply(-1j * time * H, init)
        require(abs(np.vdot(state, state) - 1) < 1e-12, 'clock_rotor assertion from exploratory source line 45')
        return (basis, state)
    reference, psi = assemble(40, False)
    lookup = dict(zip(reference, psi))
    J = 2 * r + kappa / 2
    lam = 1.0
    C = math.exp(2 * J * time * math.sinh(lam))
    A4 = (4 / (math.e * lam)) ** 4
    reference_bound = 2 * time * L * J * math.exp(-2 * 40 + 2 * J * time * math.sinh(2))
    out = []
    for S in [1, 2, 3, 4, 6, 8, 12, 16, 24, 32]:
        basis, phi = assemble(S, True)
        N = 2 * S + 1
        overlap = sum((np.conjugate(lookup.get(v, 0)) * z for v, z in zip(basis, phi)))
        err2 = max(0, 2 - 2 * overlap.real)
        err = math.sqrt(err2)
        alias = 0
        for (a, b, e), z in zip(basis, phi):
            q = [0] * L
            q[a] += 1
            q[b] -= 1
            if divergence(e) != tuple(q):
                alias += abs(z) ** 2
        bound = min(2, 4 * time * L * J * math.exp(-lam * S) * C + math.pi ** 2 * g * g * time / (6 * N * N) * A4 * L * C)
        require(err <= bound + reference_bound + 1e-10, 'clock_rotor assertion from exploratory source line 61')
        out.append({'N': N, 'dimension': len(basis), 'state_norm_error': err, 'N_squared_error': N * N * err, 'modulo_alias_probability': alias, 'proved_bound': bound})
    print('reference truncation bound', reference_bound)
    for z in out:
        print(z)

def check_fourier_pairing():
    import math
    import numpy as np
    from scipy.linalg import expm
    from scipy.integrate import quad

    def ring(phi):
        h = np.zeros((4, 4), complex)
        for i in range(4):
            j = (i + 1) % 4
            z = np.exp(1j * phi) if i == 3 else 1
            h[i, j] = z
            h[j, i] = z.conjugate() if hasattr(z, 'conjugate') else z
        return h

    def analytic(phi, x):
        return 4 * (1 + np.cosh(2 * x * np.cos(phi / 4))) * (1 + np.cosh(2 * x * np.sin(phi / 4)))
    out = {'ring': [], 'nodes': []}
    for x in [0.05, 0.1, 0.4, 1.0, 2.0]:
        errs = []
        for phi in np.linspace(0, 2 * np.pi, 37):
            d = np.linalg.det(np.eye(4) + expm(-x * ring(phi)))
            errs.append(abs(d - analytic(phi, x)))
            require(abs(d - analytic(phi, x)) < 1e-08, 'fourier_pairing assertion from exploratory source line 23')
        c1, qe = quad(lambda phi: analytic(phi, x) ** 2 * np.cos(phi) / (2 * np.pi), 0, 2 * np.pi, epsabs=1e-10)
        require(analytic(np.pi, x) > analytic(0, x), 'fourier_pairing assertion from exploratory source line 25')
        require(c1 < 0, 'fourier_pairing assertion from exploratory source line 26')
        out['ring'].append({'beta_t': x, 'max_matrix_formula_error': max(errs), 'F0': analytic(0, x) ** 2, 'Fpi': analytic(np.pi, x) ** 2, 'first_Fourier_coefficient': c1, 'quadrature_error_estimate': qe, 'small_x_coefficient_ratio': c1 / x ** 4})
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.diag([1.0, -1.0])
    zeta = 0.6
    b = 0.7

    def hp(k):
        x, y, z = np.array(k) - np.array([b, 0, 0])
        return np.sin(x) * sx + np.sin(y) * sy + (2 + zeta - np.cos(x) - np.cos(y) - np.cos(z)) * sz
    for sgx in [-1, 1]:
        for sgz in [-1, 1]:
            k = np.array([sgx * b, 0, sgz * np.arccos(zeta)])
            f = hp if sgx == 1 else lambda q: hp(-np.array(q)).conjugate()
            require(np.linalg.norm(f(k)) < 1e-14, 'fourier_pairing assertion from exploratory source line 39')
            jac = np.stack([np.array([np.trace(s @ ((f(k + np.eye(3)[i] * 1e-05) - f(k - np.eye(3)[i] * 1e-05)) / 2e-05)) / 2 for s in [sx, sy, sz]]).real for i in range(3)], axis=1)
            require(np.linalg.norm(jac.T @ jac - np.diag([1, 1, 1 - zeta * zeta])) < 2e-09, 'fourier_pairing assertion from exploratory source line 41')
            out['nodes'].append({'k': k.tolist(), 'charge': sgx, 'chirality': int(np.sign(np.linalg.det(jac))), 'metric': (jac.T @ jac).tolist()})
    require(sum((v['chirality'] * v['charge'] ** 3 for v in out['nodes'])) == 0, 'fourier_pairing assertion from exploratory source line 43')
    for k in [np.array([b, 0, np.arccos(zeta)]), np.array([0.1, 0.2, 0.3]), np.array([2.0, 1.0, -1.0])]:
        h = hp(k)
        delta = 0.23
        bdg = np.block([[h, delta * np.eye(2)], [delta * np.eye(2), -h]])
        require(np.linalg.norm(bdg @ bdg - np.kron(np.eye(2), h @ h + delta * delta * np.eye(2))) < 1e-12, 'fourier_pairing assertion from exploratory source line 46')
        require(min(abs(np.linalg.eigvalsh(bdg))) >= delta - 1e-12, 'fourier_pairing assertion from exploratory source line 47')
    out['pairing_gap'] = 0.23
    for v in out['ring']:
        print(v)
    print('nodes', out['nodes'])
    print('pairing lower gap', out['pairing_gap'])

def check_wilson_fock():
    import itertools
    import numpy as np
    from scipy.linalg import expm

    def second_quantize(h):
        n = h.shape[0]
        out = np.zeros((2 ** n, 2 ** n), complex)
        for f in range(2 ** n):
            for j in range(n):
                if not f >> j & 1:
                    continue
                f1 = f ^ 1 << j
                sg1 = (-1) ** (f & (1 << j) - 1).bit_count()
                for i in range(n):
                    if f1 >> i & 1 or abs(h[i, j]) == 0:
                        continue
                    f2 = f1 | 1 << i
                    sg2 = (-1) ** (f1 & (1 << i) - 1).bit_count()
                    out[f2, f] += sg1 * sg2 * h[i, j]
        return out
    sx = np.array([[0, 1], [1, 0]], complex)
    sz = np.diag([1.0, -1.0])
    onsite = 2.6 * sz
    hop = (-sz - 1j * sx) / 2 * np.exp(-0.7j)
    beta = 0.49
    rate = 0.37
    r = 0.6
    out = []
    for N in [3, 5]:
        om = np.exp(2j * np.pi / N)
        X = np.roll(np.eye(N), 1, axis=0)
        hs = []
        blocks = []
        for q in range(N):
            h = r * np.block([[onsite, hop * om ** q], [hop.conj().T * om ** (-q), onsite]])
            hs.append(h)
            blocks.append(second_quantize(np.block([[h, np.zeros((4, 4))], [np.zeros((4, 4)), h.conjugate()]])))
        charges = []
        valid = []
        for f in range(256):
            ns = [f >> i & 1 for i in range(8)]
            q0 = sum(ns[:2]) - sum(ns[4:6])
            q1 = sum(ns[2:4]) - sum(ns[6:])
            charges.append((q0, q1))
            if (q0 + q1) % N == 0:
                valid.append(f)
        Q = np.zeros((N * 256, len(valid)), complex)
        for j, f in enumerate(valid):
            for q in range(N):
                Q[q * 256 + f, j] = om ** (charges[f][0] * q) / np.sqrt(N)
        require(np.linalg.norm(Q.conj().T @ Q - np.eye(len(valid))) < 1e-12, 'wilson_fock assertion from exploratory source line 35')
        He = np.kron(rate * (2 * np.eye(N) - X - X.T), np.eye(256))
        Hm = np.zeros_like(He, dtype=complex)
        for q in range(N):
            Hm[q * 256:(q + 1) * 256, q * 256:(q + 1) * 256] = blocks[q]
        er = Q.conj().T @ He @ Q
        mr = Q.conj().T @ Hm @ Q
        require(np.linalg.norm(He @ Q - Q @ er) < 1e-11, 'wilson_fock assertion from exploratory source line 39')
        require(np.linalg.norm(Hm @ Q - Q @ mr) < 1e-11, 'wilson_fock assertion from exploratory source line 40')
        for site, d in enumerate([1, -1]):
            rg = np.diag([om ** z[site] for z in charges])
            GG = np.kron(np.linalg.matrix_power(X, d), rg)
            require(np.linalg.norm(GG @ Q - Q) < 1e-11, 'wilson_fock assertion from exploratory source line 43')
        data = {'N': N, 'full_dimension': N * 256, 'physical_dimension': len(valid), 'nonzero_integer_total_charge_states': sum((sum(charges[f]) != 0 for f in valid)), 'traces': []}
        for M in [1, 2, 3]:
            dt = beta / M
            K = expm(-dt * rate * (2 * np.eye(N) - X - X.T))
            A = [expm(-dt * h) for h in hs]
            direct = np.trace(np.linalg.matrix_power(expm(-dt * er) @ expm(-dt * mr), M))
            total = 0
            for s in itertools.product(range(N), repeat=2):
                R = np.diag(np.repeat(om ** np.array(s), 2))
                shift = s[0] - s[1]
                for qs in itertools.product(range(N), repeat=M):
                    B = np.eye(4, dtype=complex)
                    for q in qs:
                        B = A[q] @ B
                    w = K[(qs[0] - shift) % N, qs[-1]]
                    for j in range(M - 1):
                        w *= K[qs[j + 1], qs[j]]
                    total += w * abs(np.linalg.det(np.eye(4) + R @ B)) ** 2 / N ** 2
            require(abs(direct - total) < 1e-10 * max(1, abs(direct)), 'wilson_fock assertion from exploratory source line 56')
            data['traces'].append({'M': M, 'full_Fock_projected_trace': direct.real, 'history_sum': total, 'relative_error': abs(direct - total) / abs(direct)})
        out.append(data)
    for z in out:
        print(z)

def check_generator_bound():
    import math
    import numpy as np
    from scipy.linalg import expm, eigvalsh
    rng = np.random.default_rng(821517)
    out = []
    for S in [1, 2, 4, 7]:
        d = 3
        E = np.repeat(np.arange(-S, S + 1), d)
        V = np.zeros((len(E), len(E)), complex)
        for n in range(2 * S):
            z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
            z /= np.linalg.norm(z, 2)
            V[(n + 1) * d:(n + 2) * d, n * d:(n + 1) * d] = z
        J = np.linalg.norm(V, 2)
        H = V + V.conj().T + np.diag(rng.normal(size=len(E)) * 17)
        require(np.linalg.norm(np.diag(E) @ V - V @ np.diag(E) - V) < 1e-12, 'generator_bound assertion from exploratory source line 14')
        psi = np.zeros(len(E), complex)
        z = rng.normal(size=d) + 1j * rng.normal(size=d)
        z /= np.linalg.norm(z)
        psi[S * d:(S + 1) * d] = z
        for lam in [0.13, 0.7, 1.2]:
            w = np.exp(lam * abs(E))
            Hw = w[:, None] * H / w[None, :]
            skew = (Hw - Hw.conj().T) / 2j
            actual = np.max(abs(eigvalsh(skew)))
            bound = 2 * J * np.sinh(lam)
            require(actual <= bound + 1e-12, 'generator_bound assertion from exploratory source line 19')
            t = 0.61
            state = expm(-1j * t * H) @ psi
            weighted = np.linalg.norm(w * state)
            cb = np.exp(bound * t)
            require(weighted <= cb + 1e-12, 'generator_bound assertion from exploratory source line 21')
            tail = np.linalg.norm(state[abs(E) == S])
            require(tail <= np.exp(-lam * S) * cb + 1e-12, 'generator_bound assertion from exploratory source line 22')
            moment = np.linalg.norm(E ** 4 * state)
            mb = (4 / (math.e * lam)) ** 4 * cb
            require(moment <= mb + 1e-12, 'generator_bound assertion from exploratory source line 23')
            out.append({'S': S, 'lambda': lam, 'skew_norm': actual, 'skew_bound': bound, 'weighted_state_norm': weighted, 'weighted_bound': cb, 'endpoint_norm': tail, 'endpoint_bound': np.exp(-lam * S) * cb, 'eighth_moment_sqrt': moment, 'moment_bound': mb})
    for N in range(3, 100, 2):
        S = (N - 1) // 2
        for n in range(-S, S + 1):
            x = math.pi * n / N
            error = 1 - (math.sin(x) / x if x else 1) ** 2
            require(error >= -1e-15 and error <= x * x / 3 + 1e-15, 'generator_bound assertion from exploratory source line 29')
    print('noncommuting block weighted bounds checked:', len(out))
    print('largest ratio', max((x['skew_norm'] / x['skew_bound'] for x in out)))

def check_plaquette_trace():
    import itertools
    import numpy as np
    from scipy.linalg import expm
    N = 3
    V = 4
    omega = np.exp(2j * np.pi / N)
    beta = 0.41
    tel = 0.36
    mag = 0.73
    hop = 0.38 + 0.12j
    D = np.zeros((V, V), int)
    for l in range(V):
        D[l, l] = 1
        D[(l + 1) % V, l] = -1

    def charges(f):
        return np.array([(f >> i & 1) - (f >> i + V & 1) for i in range(V)])

    def fermi_hop(f, i, j):
        if not f >> j & 1:
            return None
        f1 = f ^ 1 << j
        sg = (-1) ** (f & (1 << j) - 1).bit_count()
        if f1 >> i & 1:
            return None
        return (f1 | 1 << i, sg * (-1) ** (f1 & (1 << i) - 1).bit_count())
    basis = []
    for f in range(2 ** (2 * V)):
        Q = charges(f)
        if sum(Q) % N:
            continue
        base = np.r_[np.cumsum(Q)[:3], 0]
        for n in range(N):
            basis.append((f, tuple((base + n) % N)))
    lookup = {v: i for i, v in enumerate(basis)}
    dim = len(basis)
    He = np.zeros((dim, dim), complex)
    Hbm = np.zeros_like(He)
    for i, (f, e) in enumerate(basis):
        He[i, i] = tel * sum(2 - 2 * np.cos(2 * np.pi * np.array(e) / N))
        Hbm[i, i] += mag
        for sg in [-1, 1]:
            Hbm[lookup[f, tuple((np.array(e) + sg) % N)], i] -= mag / 2
        for l in range(V):
            x = l
            y = (l + 1) % V
            for species, charge in [(0, 1), (1, -1)]:
                z = hop if species == 0 else hop.conjugate()
                for src, dst, amp, de in [(y, x, z, charge), (x, y, z.conjugate(), -charge)]:
                    step = fermi_hop(f, dst + species * V, src + species * V)
                    if step:
                        f2, sign = step
                        ee = list(e)
                        ee[l] = (ee[l] + de) % N
                        Hbm[lookup[f2, tuple(ee)], i] += sign * amp
    require(np.linalg.norm(Hbm - Hbm.conj().T) < 1e-12, 'plaquette_trace assertion from exploratory source line 38')
    qs = list(itertools.product(range(N), repeat=V))
    qindex = {v: i for i, v in enumerate(qs)}
    h = []
    vb = []
    for q in qs:
        m = np.zeros((V, V), complex)
        for l in range(V):
            x = l
            y = (l + 1) % V
            m[x, y] = hop * omega ** q[l]
            m[y, x] = m[x, y].conjugate()
        h.append(m)
        vb.append(mag * (1 - np.cos(2 * np.pi * sum(q) / N)))
    X = np.roll(np.eye(N), 1, axis=0)
    out = []
    for M in [1, 2]:
        dt = beta / M
        K = expm(-dt * tel * (2 * np.eye(N) - X - X.T))
        A = [expm(-dt * x) for x in h]
        weights = np.exp(-dt * np.array(vb))
        direct = np.trace(np.linalg.matrix_power(expm(-dt * He) @ expm(-dt * Hbm), M))
        total = 0
        for s in itertools.product(range(N), repeat=V):
            R = np.diag(omega ** np.array(s))
            shift = D.T @ np.array(s)
            for hol in range(N):
                q0 = (0, 0, 0, hol)
                i0 = qindex[q0]
                end = (np.array(q0) - shift) % N
                for q1 in qs if M == 2 else [q0]:
                    i1 = qindex[q1]
                    scalar = np.prod([K[end[l], q1[l]] for l in range(V)]) * weights[i0]
                    B = A[i0]
                    if M == 2:
                        scalar *= np.prod([K[q1[l], q0[l]] for l in range(V)]) * weights[i1]
                        B = A[i1] @ B
                    total += scalar * abs(np.linalg.det(np.eye(V) + R @ B)) ** 2 / N
        require(abs(direct - total) < 2e-10 * abs(direct), 'plaquette_trace assertion from exploratory source line 62')
        out.append({'M': M, 'flux_CAR_trace': direct.real, 'positive_history_trace': total, 'relative_difference': abs(direct - total) / abs(direct)})
        if M == 1:
            brute = 0
            for s in itertools.product(range(N), repeat=V):
                R = np.diag(omega ** np.array(s))
                shift = D.T @ np.array(s)
                for q in qs:
                    idx = qindex[q]
                    end = (np.array(q) - shift) % N
                    scalar = np.prod([K[end[l], q[l]] for l in range(V)]) * weights[idx]
                    brute += scalar * abs(np.linalg.det(np.eye(V) + R @ A[idx])) ** 2 / N ** V
            require(abs(brute - total) < 2e-10 * abs(total), 'plaquette_trace assertion from exploratory source line 72')
            out[-1]['unfixed_full_history_sum'] = brute
    print('physical dimension', dim)
    for x in out:
        print(x)

def check_antiunitary_pairing():
    from itertools import combinations
    import numpy as np
    from scipy.linalg import expm

    def annihilator(mode, nmodes):
        a = np.zeros((2 ** nmodes, 2 ** nmodes), complex)
        for n in range(2 ** nmodes):
            if n >> mode & 1:
                a[n ^ 1 << mode, n] = (-1) ** (n & (1 << mode) - 1).bit_count()
        return a

    def second_quantization(u):
        n = len(u)
        ans = np.zeros((2 ** n, 2 ** n), complex)
        for k in range(n + 1):
            for rows in combinations(range(n), k):
                for cols in combinations(range(n), k):
                    i = sum((1 << x for x in rows))
                    j = sum((1 << x for x in cols))
                    ans[i, j] = np.linalg.det(u[np.ix_(rows, cols)])
        return ans
    m = 2
    cs = [annihilator(i, 2 * m) for i in range(2 * m)]
    nums = [c.conj().T @ c for c in cs]
    Q = sum(nums[:m]) - sum(nums[m:])
    nt = sum(nums)
    r = np.block([[np.zeros((m, m)), np.eye(m)], [-np.eye(m), np.zeros((m, m))]])
    f = second_quantization(r)
    parity = np.diag([(-1) ** n.bit_count() for n in range(2 ** (2 * m))])
    h = np.array([[0.31, 0.4 + 0.7j], [0.4 - 0.7j, -0.62]])
    hn = sum((h[i, j] * cs[i].conj().T @ cs[j] + h[i, j].conjugate() * cs[i + m].conj().T @ cs[j + m] for i in range(m) for j in range(m)))
    create = sum((cs[i].conj().T @ cs[i + m].conj().T for i in range(m)))
    pair = 0.23 * (create + create.conj().T)
    metrics = {'fock_antiunitary_square_parity_error': np.linalg.norm(f @ f.conjugate() - parity), 'normal_antiunitary_error': np.linalg.norm(f @ hn.conjugate() @ f.conj().T - hn), 'pair_antiunitary_error': np.linalg.norm(f @ pair.conjugate() @ f.conj().T - pair), 'pair_charge_commutator': np.linalg.norm(Q @ pair - pair @ Q), 'pair_number_commutator': np.linalg.norm(nt @ pair - pair @ nt)}
    for phi in [0.3, 1.7]:
        g = expm(1j * phi * Q)
        require(np.linalg.norm(f @ g.conjugate() @ f.conj().T - g) < 1e-12, 'antiunitary_pairing assertion from exploratory source line 41')
    for key in ['fock_antiunitary_square_parity_error', 'normal_antiunitary_error', 'pair_antiunitary_error', 'pair_charge_commutator']:
        require(metrics[key] < 1e-12, 'antiunitary_pairing assertion from exploratory source line 43')
    require(metrics['pair_number_commutator'] > 0.5, 'antiunitary_pairing assertion from exploratory source line 44')
    print(metrics)


def main():
    checks = [check_positive_trace, check_charge_interaction, check_clock_rotor, check_fourier_pairing, check_wilson_fock, check_generator_bound, check_plaquette_trace, check_antiunitary_pairing]
    for fn in checks:
        fn()
        print("PASS:", fn.__name__, flush=True)
    print("per_element: cyclic kernels, finite Fock algebra and noncommuting electric-weight generators are checked")
    print("per_site: opposite charge Gauss projection includes modulo aliases; neutral pairing respects its stated antiunitary")
    print("per_mode: free four-node metrics and a permitted gapping pairing are checked without an interacting phase inference")
    print("per_block: bond and full plaquette projected traces match positive histories, with finite-slice errors disclosed")
    print("lattice_wide: local fixed-time approximation is proved in the note; ground-state and infrared phase limits remain open")
    print("Internal finite assertions:", _ASSERTIONS, "(not independent scientific results)")
    print(f"TOTAL: PASS={len(checks)} FAIL=0")

if __name__ == "__main__":
    main()
