#!/usr/bin/env python3
"""Author challenges for massive Wilson curvature, gauge covariance and defects.

Self-contained: no scientific file inputs. Direct mathematical proofs live in
the companion note. Finite checks do not establish an interacting compact
phase, physical photon spectrum or independent scientific review.
"""
AUDIT_TIMEOUT_SEC = 90
_ASSERTIONS = 0

def require(condition, label):
    global _ASSERTIONS
    _ASSERTIONS += 1
    if not condition:
        print("FAIL:", label, flush=True)
        raise AssertionError(label)


def check_loop_filling():
    from collections import Counter
    from itertools import product
    import json

    def clean(c):
        return {k: v for k, v in c.items() if v}

    def edge_chain(word, d):
        p = [0] * d
        c = Counter()
        points = [tuple(p)]
        for axis, sg in word:
            anchor = p.copy()
            if sg < 0:
                anchor[axis] -= 1
            c[tuple(anchor), axis] += sg
            p[axis] += sg
            points.append(tuple(p))
        return (clean(c), points)

    def fill(word, d):
        word = list(word)
        surface = Counter()
        swaps = 0
        while True:
            changed = False
            p = [0] * d
            for i in range(len(word) - 1):
                a, sa = word[i]
                b, sb = word[i + 1]
                if a > b:
                    anchor = p.copy()
                    if sa < 0:
                        anchor[a] -= 1
                    if sb < 0:
                        anchor[b] -= 1
                    surface[tuple(anchor), b, a] += -sa * sb
                    word[i], word[i + 1] = (word[i + 1], word[i])
                    swaps += 1
                    changed = True
                axis, sg = word[i]
                p[axis] += sg
            if not changed:
                break
        return (clean(surface), swaps, word)

    def boundary(surface, d):
        c = Counter()
        for (p, a, b), coeff in surface.items():
            pa = list(p)
            pa[a] += 1
            pb = list(p)
            pb[b] += 1
            c[p, a] += coeff
            c[tuple(pa), b] += coeff
            c[tuple(pb), a] -= coeff
            c[p, b] -= coeff
        return clean(c)
    out = []
    for d, lengths in [(2, [0, 2, 4, 6, 8]), (3, [2, 4, 6]), (4, [2, 4, 6])]:
        choices = [(i, s) for i in range(d) for s in [-1, 1]]
        for n in lengths:
            count = 0
            maxarea = 0
            maxswaps = 0
            for word in product(choices, repeat=n):
                if any((sum((s for a, s in word if a == i)) for i in range(d))):
                    continue
                count += 1
                chain, points = edge_chain(word, d)
                surface, swaps, sortedword = fill(word, d)
                require(boundary(surface, d) == chain, 'loop_filling: original line 55')
                require(edge_chain(sortedword, d)[0] == {}, 'loop_filling: original line 56')
                area = sum((abs(x) for x in surface.values()))
                require(area <= swaps <= n * (n - 1) // 2, 'loop_filling: original line 58')
                lo = [min((p[i] for p in points)) for i in range(d)]
                hi = [max((p[i] for p in points)) for i in range(d)]
                for (p, a, b), coeff in surface.items():
                    require(all((lo[i] <= p[i] and p[i] + int(i in (a, b)) <= hi[i] for i in range(d))), 'loop_filling: original line 61')
                if n < 4:
                    require(area == 0, 'loop_filling: original line 62')
                maxarea = max(maxarea, area)
                maxswaps = max(maxswaps, swaps)
            out.append({'dimension': d, 'length': n, 'closed_words': count, 'maximum_filling_l1': maxarea, 'maximum_swaps': maxswaps, 'stated_swap_bound': n * (n - 1) // 2})
            print(out[-1], flush=True)
    L = 5
    wind = [(0, 1)] * L
    require(edge_chain(wind, 2)[1][-1] == (L, 0), 'loop_filling: original line 69')
    require(L % L == 0 and sum((s for a, s in wind if a == 0)) == L, 'loop_filling: original line 70')

def check_wilson_curvature():
    from itertools import product, combinations
    from fractions import Fraction
    import json, math
    import numpy as np
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.diag([1.0, -1.0])
    I = np.eye(2)
    gamma = [np.kron(sx, s) for s in [sx, sy, sz]] + [np.kron(sy, I)]
    B = gamma[0] @ gamma[2]
    G5 = gamma[0] @ gamma[1] @ gamma[2] @ gamma[3]
    for i in range(4):
        require(np.linalg.norm(B @ gamma[i].T @ B.conj().T + gamma[i]) < 1e-12, 'wilson_curvature: original line 12')
        for j in range(4):
            require(np.linalg.norm(gamma[i] @ gamma[j] + gamma[j] @ gamma[i] - 2 * (i == j) * np.eye(4)) < 1e-12, 'wilson_curvature: original line 13')

    def majorant(d, m, q, nmax=100):
        q = Fraction(q)
        terms = [Fraction(m, 2) * n ** 3 * (2 * n + 1) ** d * q ** n for n in range(4, nmax + 1)]
        nextterm = Fraction(m, 2) * (nmax + 1) ** 3 * (2 * nmax + 3) ** d * q ** (nmax + 1)
        ratio = q * Fraction(nmax + 2, nmax + 1) ** (d + 3)
        require(ratio < 1, 'wilson_curvature: original line 20')
        partial = sum(terms)
        remainder = nextterm / (1 - ratio)
        if d == 4 and m == 4 and (q == Fraction(1, 20)):
            require(Fraction(1, 100) * (partial + remainder) < Fraction('0.066164'), 'wilson_curvature: original line 23')
            require(remainder < Fraction('1.46e-116'), 'wilson_curvature: original line 24')
        return (float(partial), float(remainder))
    rng = np.random.default_rng(621017)
    results = []
    for d in [2, 3, 4]:
        sites = list(product(range(2), repeat=d))
        site = {x: i for i, x in enumerate(sites)}
        links = []
        for x in sites:
            for mu in range(d):
                if x[mu] == 0:
                    y = list(x)
                    y[mu] = 1
                    links.append((x, tuple(y), mu))
        ix = {(x, mu): i for i, (x, y, mu) in enumerate(links)}
        curl = []
        for x in sites:
            for mu, nu in combinations(range(d), 2):
                if x[mu] or x[nu]:
                    continue
                row = np.zeros(len(links))
                xm = list(x)
                xm[mu] = 1
                xn = list(x)
                xn[nu] = 1
                row[ix[x, mu]] += 1
                row[ix[tuple(xm), nu]] += 1
                row[ix[tuple(xn), mu]] -= 1
                row[ix[x, nu]] -= 1
                curl.append(row)
        C = np.array(curl)
        M = 20.0
        e = 0.7
        t0 = 1.0
        q = Fraction(2 * d, 20)
        cb, tail = majorant(d, 4, q)
        phases = rng.normal(size=len(links)) * 2.1
        direction = rng.normal(size=len(links))
        chi = rng.normal(size=len(sites))
        grad = np.array([chi[site[y]] - chi[site[x]] for x, y, mu in links])
        require(np.linalg.norm(C @ grad) < 1e-12, 'wilson_curvature: original line 45')

        def matrices(A, a):
            D = M * np.eye(4 * len(sites), dtype=complex)
            first = np.zeros_like(D)
            second = np.zeros_like(D)
            for k, (x, y, mu) in enumerate(links):
                i, j = (site[x], site[y])
                f = -t0 * (np.eye(4) - gamma[mu]) / 2
                back = -t0 * (np.eye(4) + gamma[mu]) / 2
                for src, dst, T, sg in [(i, j, f, 1), (j, i, back, -1)]:
                    block = T * np.exp(1j * sg * e * A[k])
                    s1 = slice(4 * src, 4 * (src + 1))
                    s2 = slice(4 * dst, 4 * (dst + 1))
                    D[s1, s2] += block
                    first[s1, s2] += 1j * sg * e * a[k] * block
                    second[s1, s2] -= e * e * a[k] * a[k] * block
            return (D, first, second)
        D, D1, D2 = matrices(phases, direction)
        inv = np.linalg.inv(D)
        curvature = 2 * np.trace(inv @ D2 - inv @ D1 @ inv @ D1).real
        fullB = np.kron(np.eye(len(sites)), B)
        fullG5 = np.kron(np.eye(len(sites)), G5)
        reverse = matrices(-phases, direction)[0]
        require(np.linalg.norm(reverse - fullB @ D.T @ fullB.conj().T) < 1e-12, 'wilson_curvature: original line 58')
        require(np.linalg.norm(D.conj().T - fullG5 @ D @ fullG5) < 1e-12, 'wilson_curvature: original line 59')

        def logweight(A):
            return 2 * np.linalg.slogdet(matrices(A, np.zeros(len(links)))[0] / M)[1]
        logw = logweight(phases)
        require(abs(logweight(-phases) - logw) < 1e-12, 'wilson_curvature: original line 62')
        require(abs(logweight(phases + grad) - logw) < 1e-12, 'wilson_curvature: original line 63')
        _, g1, g2 = matrices(phases, grad)
        gaugecurvature = 2 * np.trace(inv @ g2 - inv @ g1 @ inv @ g1).real
        require(abs(gaugecurvature) < 1e-12, 'wilson_curvature: original line 65')
        finite = []
        for h in [0.08, 0.04, 0.02]:
            fd = (logweight(phases + h * direction) - 2 * logw + logweight(phases - h * direction)) / h ** 2
            finite.append({'step': h, 'finite_difference': fd, 'error': abs(fd - curvature)})
        require(finite[-1]['error'] < max(1e-08, abs(curvature) * 0.02), 'wilson_curvature: original line 70')
        require(finite[-1]['error'] < finite[0]['error'] * 0.2 + 1e-11, 'wilson_curvature: original line 71')
        bound = e * e * (cb + tail) * np.linalg.norm(C @ direction) ** 2
        require(abs(curvature) <= bound + 1e-12, 'wilson_curvature: original line 73')
        results.append({'d': d, 'sites': len(sites), 'links': len(links), 'matrix_dimension': len(D), 'q': float(q), 'curvature': curvature, 'curl_bound': bound, 'majorant': cb, 'majorant_tail_bound': tail, 'gauge_null_curvature': gaugecurvature, 'finite_differences': finite})
        print(results[-1], flush=True)
    low, tail = majorant(4, 4, Fraction(1, 20))
    require(0.01 * (low + tail) < 1, 'wilson_curvature: original line 76')
    print('d4 m4 q=.05 e=.1 beta=1 alpha_upper', 0.01 * (low + tail), 'tail', tail)

def check_covariance_projection():
    from itertools import combinations
    import json, math
    import numpy as np
    from scipy.integrate import quad
    M = 4.0
    t = 1.0
    e = 0.7
    c = M ** 4 - 4 * M * M * t * t + 2 * t ** 4
    b = 2 * t ** 4
    require(c > 2 * b, 'covariance_projection: original line 11')
    alpha = e * e * 2 * b / (c - b)
    for phi in np.linspace(-4, 4, 29):
        K = np.zeros((4, 4), complex)
        for i in range(4):
            j = (i + 1) % 4
            z = np.exp(1j * phi) if i == 3 else 1
            K[i, j] = t * z
            K[j, i] = t * np.conjugate(z)
        require(abs(np.linalg.det(M * np.eye(4) + K) - (c - b * np.cos(phi))) < 1e-10, 'covariance_projection: original line 18')
    cov = []
    for beta in [0.03, 0.1, 0.3, 1.0]:
        require(beta > alpha, 'covariance_projection: original line 21')
        den = c * c + b * b / 2 - 2 * c * b * np.exp(-e * e / (2 * beta)) + b * b / 2 * np.exp(-2 * e * e / beta)
        analytic = 1 / beta + (2 * c * b * e * e * np.exp(-e * e / (2 * beta)) - 2 * b * b * e * e * np.exp(-2 * e * e / beta)) / (beta * beta * den)

        def weight(x):
            return np.exp(-beta * x * x / 2) * (c - b * np.cos(e * x)) ** 2 / (c * c)

        def score(x):
            return beta * x - 2 * b * e * np.sin(e * x) / (c - b * np.cos(e * x))

        def hessian(x):
            return beta - 2 * b * e * e * (c * np.cos(e * x) - b) / (c - b * np.cos(e * x)) ** 2
        Z = quad(weight, -np.inf, np.inf, epsabs=1e-10)[0]
        var = quad(lambda x: x * x * weight(x), -np.inf, np.inf, epsabs=1e-10)[0] / Z
        cross = quad(lambda x: x * score(x) * weight(x), -np.inf, np.inf, epsabs=1e-10)[0] / Z
        eg2 = quad(lambda x: score(x) ** 2 * weight(x), -np.inf, np.inf, epsabs=1e-10)[0] / Z
        eh = quad(lambda x: hessian(x) * weight(x), -np.inf, np.inf, epsabs=1e-10)[0] / Z
        require(abs(var - analytic) < 1e-08, 'covariance_projection: original line 32')
        require(abs(cross - 1) < 1e-09 and abs(eg2 - eh) < 1e-09, 'covariance_projection: original line 33')
        require(1 / (beta + alpha) <= var <= 1 / (beta - alpha), 'covariance_projection: original line 34')
        require(var >= 1 / eh - 1e-10, 'covariance_projection: original line 35')
        cov.append({'beta': beta, 'alpha': alpha, 'variance_quadrature': var, 'variance_closed_form': analytic, 'lower_comparison': 1 / (beta + alpha), 'upper_comparison': 1 / (beta - alpha), 'score_cross': cross, 'score_second_moment': eg2, 'expected_action_hessian': eh})
        print(cov[-1], flush=True)

    def curl_symbol(q):
        d = len(q)
        pairs = list(combinations(range(d), 2))
        C = np.zeros((len(pairs), d), complex)
        for r, (i, j) in enumerate(pairs):
            C[r, j] = q[i]
            C[r, i] = -q[j]
        return (pairs, C)

    def bianchi_symbol(q):
        d = len(q)
        pairs = list(combinations(range(d), 2))
        pos = {p: i for i, p in enumerate(pairs)}
        B = np.zeros((math.comb(d, 3) if d >= 3 else 0, len(pairs)), complex)
        for r, (i, j, k) in enumerate(combinations(range(d), 3)):
            B[r, pos[j, k]] = q[i]
            B[r, pos[i, k]] = -q[j]
            B[r, pos[i, j]] = q[k]
        return B
    symbols = []
    for d in [2, 3, 4, 5]:
        cases = [np.linspace(0.21, 0.87, d)] + [np.eye(d)[i] * v for i in range(d) for v in [0.3, 0.03, 0.003]]
        for k in cases:
            q = np.exp(1j * k) - 1
            pairs, C = curl_symbol(q)
            P = C @ C.conj().T / np.vdot(q, q).real
            require_norm = max(np.linalg.norm(P @ P - P), np.linalg.norm(P - P.conj().T), np.linalg.norm(bianchi_symbol(q) @ C))
            require(require_norm < 1e-12, 'covariance_projection: original line 59')
            require(abs(np.trace(P).real - (d - 1)) < 1e-12, 'covariance_projection: original line 60')
            for j, (mu, nu) in enumerate(pairs):
                require(abs(P[j, j] - (abs(q[mu]) ** 2 + abs(q[nu]) ** 2) / np.vdot(q, q).real) < 1e-12, 'covariance_projection: original line 62')
        stacked = np.concatenate([bianchi_symbol(np.eye(d)[i]) for i in range(d)], axis=0)
        nullity = len(pairs) - (np.linalg.matrix_rank(stacked) if len(stacked) else 0)
        require(nullity == (1 if d == 2 else 0), 'covariance_projection: original line 65')
        symbols.append({'dimension': d, 'momenta_checked': len(cases), 'curl_range_rank': d - 1, 'common_Bianchi_kernel_dimension': int(nullity)})
        print(symbols[-1], flush=True)
    require(math.cos(math.pi) < 0, 'covariance_projection: original line 70')

def check_integer_cochain():
    from itertools import product, combinations
    import json
    import numpy as np
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form

    def complex_box(d, L):
        cells = []
        for k in range(d + 1):
            cells.append([(p, S) for S in combinations(range(d), k) for p in product(*[range(L if i in S else L + 1) for i in range(d)])])
        index = [{v: i for i, v in enumerate(ck)} for ck in cells]
        D = []
        H = [None]
        for k in range(d):
            mat = np.zeros((len(cells[k + 1]), len(cells[k])), dtype=np.int64)
            for row, (p, S) in enumerate(cells[k + 1]):
                for j, axis in enumerate(S):
                    R = tuple((a for a in S if a != axis))
                    up = list(p)
                    up[axis] += 1
                    mat[row, index[k][tuple(up), R]] += (-1) ** j
                    mat[row, index[k][p, R]] -= (-1) ** j
            D.append(mat)
        for k in range(1, d + 1):
            mat = np.zeros((len(cells[k - 1]), len(cells[k])), dtype=np.int64)
            for row, (y, R) in enumerate(cells[k - 1]):
                for axis in range(min(R) if R else d):
                    S = (axis,) + R
                    for t in range(y[axis]):
                        p = tuple((0 if j < axis else t if j == axis else y[j] for j in range(d)))
                        mat[row, index[k][p, S]] += 1
            H.append(mat)
        return (cells, D, H)
    results = []
    for d, L in [(2, 1), (2, 2), (3, 1), (3, 2), (4, 1)]:
        cells, D, H = complex_box(d, L)
        for k in range(d - 1):
            require(not np.any(D[k + 1] @ D[k]), 'integer_cochain: original line 38')
        ev = np.zeros((len(cells[0]), len(cells[0])), dtype=np.int64)
        ev[:, cells[0].index(((0,) * d, ()))] = 1
        require(np.array_equal(H[1] @ D[0], np.eye(len(cells[0]), dtype=np.int64) - ev), 'integer_cochain: original line 40')
        for k in range(1, d + 1):
            identity = D[k - 1] @ H[k]
            if k < d:
                identity += H[k + 1] @ D[k]
            require(np.array_equal(identity, np.eye(len(cells[k]), dtype=np.int64)), 'integer_cochain: original line 44')
        smith = []
        if L == 1:
            for k, mat in enumerate(D):
                S = smith_normal_form(Matrix(mat.tolist()), domain=ZZ)
                nonzero = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i]]
                require(all((x == 1 for x in nonzero)), 'integer_cochain: original line 50')
                smith.append({'degree': k, 'rank': len(nonzero), 'nonunit_invariant_factors': []})
        row = {'dimension': d, 'intervals_per_axis': L, 'cell_counts': [len(x) for x in cells], 'integer_homotopy_identity': True, 'smith_checks': smith}
        results.append(row)
        print(row, flush=True)

def check_compact_marginal():
    from itertools import product, combinations
    import json, math
    import numpy as np
    from scipy.integrate import quad
    from scipy.special import log_ndtr
    M = 8.0
    t = 1.0
    c = M ** 4 - 4 * M * M * t * t + 2 * t ** 4
    b = 2 * t ** 4
    eta = 2 * b / (c - b)
    require(c > 2 * b, 'compact_marginal: original line 14')
    vertices = list(product(range(2), repeat=3))
    links = []
    for x in vertices:
        for axis in range(3):
            if x[axis] == 0:
                links.append((x, axis))
    linkpos = {v: i for i, v in enumerate(links)}
    rows = []
    for x in vertices:
        for mu, nu in combinations(range(3), 2):
            if x[mu] or x[nu]:
                continue
            row = np.zeros(len(links))
            xm = list(x)
            xm[mu] = 1
            xn = list(x)
            xn[nu] = 1
            row[linkpos[x, mu]] += 1
            row[linkpos[tuple(xm), nu]] += 1
            row[linkpos[tuple(xn), mu]] -= 1
            row[linkpos[x, nu]] -= 1
            rows.append(row)
    C = np.array(rows)
    P = C @ np.linalg.pinv(C)
    require(C.shape == (6, 12) and np.linalg.matrix_rank(C) == 5, 'compact_marginal: original line 28')
    require(np.linalg.norm(P @ P - P) < 1e-12 and np.max(abs(np.diag(P) - 5 / 6)) < 1e-12, 'compact_marginal: original line 29')
    out = []
    for beta in [0.1, 0.5, 2.0, 20.0]:
        require(beta > eta, 'compact_marginal: original line 32')
        W = lambda F: ((c - b * np.cos(F)) / c) ** 2
        gaussian_expect = lambda shift, var: 1 + (b / c) ** 2 / 2 - 2 * (b / c) * np.exp(-var / 2) * np.cos(shift) + (b / c) ** 2 / 2 * np.exp(-2 * var) * np.cos(2 * shift)
        cutoff = 12
        compact = quad(lambda phi: W(phi) * sum((np.exp(-beta * (phi + 2 * np.pi * n) ** 2 / 2) for n in range(-cutoff, cutoff + 1))), -np.pi, np.pi, epsabs=1e-11)[0] / (2 * np.pi)
        unfolded = math.sqrt(2 * np.pi / beta) * gaussian_expect(0, 1 / beta) / (2 * np.pi)
        radius = (2 * cutoff + 1) * np.pi
        tail_log = 2 * math.log(1 + b / c) + 0.5 * math.log(2 * np.pi / beta) + math.log(2) + float(log_ndtr(-radius * math.sqrt(beta))) - math.log(2 * np.pi)
        tail = math.exp(max(tail_log, -660))
        require(abs(compact - unfolded) < tail + 1e-11, 'compact_marginal: original line 41')
        sigma2 = 5 / (6 * beta)
        require(abs(sigma2 - P[0, 0] / beta) < 1e-12, 'compact_marginal: original line 46')
        normal = gaussian_expect(0, sigma2)
        sectors = []

        def logratio(m):
            y2 = (2 * np.pi * m) ** 2 / 6
            shift = 2 * np.pi * m / 6
            return -beta * y2 / 2 + np.log(gaussian_expect(shift, sigma2) / normal)
        for m in [0, 1, 2, 3, 5]:
            y2 = (2 * np.pi * m) ** 2 / 6
            shift = 2 * np.pi * m / 6
            integral = quad(lambda z: np.exp(-z * z / 2) * W(np.sqrt(sigma2) * z + shift) / np.sqrt(2 * np.pi), -np.inf, np.inf, epsabs=1e-11)[0]
            require(abs(integral - gaussian_expect(shift, sigma2)) < 1e-10, 'compact_marginal: original line 54')
            lr = logratio(m)
            require(-(beta + eta) * y2 / 2 - 1e-12 <= lr <= -(beta - eta) * y2 / 2 + 1e-12, 'compact_marginal: original line 56')
            sectors.append({'m': m, 'log_sector_ratio': lr, 'lower_log_bound': -(beta + eta) * y2 / 2, 'upper_log_bound': -(beta - eta) * y2 / 2, 'gaussian_marginal_integral': integral})
        a = (beta - eta) * np.pi ** 2 / 6
        ms = np.arange(-40, 41)
        weights = np.exp([logratio(int(m)) for m in ms])
        density = float(np.dot(ms * ms, weights) / sum(weights))
        theta_bound = 4 * np.exp(-a / 2) / (a * (1 - np.exp(-3 * a / 2)))
        nextm = 41
        r = np.exp(-a * (2 * nextm + 1))
        rt = ((nextm + 1) / nextm) ** 2 * r
        require(rt < 1, 'compact_marginal: original line 60')
        ztail = math.exp(max(math.log(2) - a * nextm ** 2 - math.log1p(-r), -660))
        qtail = math.exp(max(math.log(2 * nextm ** 2) - a * nextm ** 2 - math.log1p(-rt), -660))
        density_error = qtail + density * ztail
        require(density + density_error <= theta_bound + 1e-14, 'compact_marginal: original line 63')
        out.append({'beta': beta, 'exact_one_face_Hessian_bound': eta, 'compact_partition': compact, 'unfolded_partition': unfolded, 'periodization_tail_bound': tail, 'periodization_tail_log_estimate': tail_log, 'sector_cases': sectors, 'current_squared_density': density, 'density_truncation_error_upper': density_error, 'proved_density_upper': theta_bound})
        print(out[-1], flush=True)
    require(abs(((c - b * np.cos(0.5 * 2 * np.pi)) / c) ** 2 - ((c - b) / c) ** 2) > 0.0001, 'compact_marginal: original line 67')

def check_compact_response():
    from itertools import combinations, product
    from fractions import Fraction as F
    import json, math
    import numpy as np
    from sympy import Matrix, I as sympy_i
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.diag([1, -1])
    I = np.eye(4, dtype=complex)
    gamma = [np.kron(sx, s) for s in [sx, sy, sz]] + [np.kron(sy, np.eye(2))]
    basis = []
    for k in range(5):
        for S in combinations(range(4), k):
            B = I.copy()
            for i in S:
                B = B @ gamma[i]
            require(np.trace(B) == (4 if not S else 0), 'compact_response: original line 16')
            basis.append(B)
    for A in basis:
        for B in basis:
            C = A @ B
            require(any((np.array_equal(C, sign * D) for D in basis for sign in [-1, 1])), 'compact_response: original line 22')
    r = 2
    t0 = 2
    M = 80
    vertices = [(0, 0), (1, 0), (0, 1), (1, 1)]
    index = {x: i for i, x in enumerate(vertices)}

    def square_det(flux_sign):
        D = np.eye(16, dtype=complex) * M
        for x in vertices:
            for mu in range(2):
                y = list(x)
                y[mu] += 1
                y = tuple(y)
                if y not in index:
                    continue
                phase = flux_sign if x == (0, 0) and mu == 0 else 1
                a = slice(4 * index[x], 4 * index[x] + 4)
                b = slice(4 * index[y], 4 * index[y] + 4)
                D[a, b] = -t0 / 2 * (r * I - gamma[mu]) * phase
                D[b, a] = -t0 / 2 * (r * I + gamma[mu]) * phase
        exact = Matrix([[int(z.real) + int(z.imag) * sympy_i for z in row] for row in D])
        return int(exact.det())
    d0 = square_det(1)
    dpi = square_det(-1)
    require(d0 > 0 and dpi > d0, 'compact_response: original line 41')
    require(8 * (t0 * (r + 1) / 2) < M, 'compact_response: original line 42')
    vs4 = list(product(range(2), repeat=4))
    ix4 = {v: i for i, v in enumerate(vs4)}

    def box4_hop(sign):
        K = np.zeros((64, 64), complex)
        for x in vs4:
            for mu in range(4):
                y = list(x)
                y[mu] += 1
                y = tuple(y)
                if y not in ix4:
                    continue
                phase = sign if x == (0, 0, 0, 0) and mu == 0 else 1
                a = slice(4 * ix4[x], 4 * ix4[x] + 4)
                b = slice(4 * ix4[y], 4 * ix4[y] + 4)
                K[a, b] = -(2 * I - gamma[mu]) * phase
                K[b, a] = -(2 * I + gamma[mu]) * phase
        return K
    K0, Kpi = (box4_hop(1), box4_hop(-1))
    require(np.trace(Kpi @ Kpi) == np.trace(K0 @ K0), 'compact_response: original line 59')
    trace4 = np.trace(np.linalg.matrix_power(Kpi, 4) - np.linalg.matrix_power(K0, 4))
    require(trace4 == -1344, 'compact_response: original line 61')
    mass4 = 10000
    q4 = F(24, mass4)
    leading4 = F(672, mass4 ** 4)
    tail4 = F(4 * 64, 6) * q4 ** 6 / (1 - q4)
    require(leading4 > tail4, 'compact_response: original line 64')
    full4 = {'vertices': 16, 'M': mass4, 'r': 2, 't0': 2, 'trace4_difference': int(trace4.real), 'leading_logW_difference': str(leading4), 'absolute_logW_difference_tail_upper': str(tail4), 'strict_logW_increase_lower': str(leading4 - tail4)}
    looprows = []
    for L in [1, 2, 4, 8, 16, 32]:
        edges = {}

        def add(x, mu, sign):
            edges[x, mu] = edges.get((x, mu), 0) + sign
        for v in range(L):
            add((v, 0), 0, 1)
            add((v, L), 0, -1)
            add((L, v), 1, 1)
            add((0, v), 1, -1)
        div = {}
        for (x, mu), sign in edges.items():
            y = list(x)
            y[mu] += 1
            y = tuple(y)
            div[x] = div.get(x, 0) + sign
            div[y] = div.get(y, 0) - sign
        require(not any(div.values()), 'compact_response: original line 76')
        require(len(edges) == 4 * L and sum((s * s for (x, mu), s in edges.items() if mu == 0)) == 2 * L, 'compact_response: original line 77')
        for k in [np.array([0.173, 0.241]), np.array([1e-06 / L, 0.0])]:
            direct = np.array([sum((s * np.exp(-1j * np.dot(k, x)) for (x, a), s in edges.items() if a == mu)) for mu in [0, 1]])
            S = np.prod([sum((np.exp(-1j * k[a] * v) for v in range(L))) for a in [0, 1]])
            diff = 1 - np.exp(-1j * k)
            closed = np.array([diff[1], -diff[0]]) * S
            require(np.linalg.norm(direct - closed) < 1e-10, 'compact_response: original line 82')
            require(abs(np.dot(diff, direct)) < 1e-10, 'compact_response: original line 83')
        rho = F(1, 10 ** 6)
        lam = rho / (2 * L)
        coefficient = lam * L ** 4
        numerical = float(lam) * float(np.vdot(direct, direct).real) / float(np.vdot(diff, diff).real)
        require(abs(numerical / float(coefficient) - 1) < 1e-06, 'compact_response: original line 86')
        looprows.append({'L': L, 'component_second_moment': str(rho), 'infrared_coefficient_exact': str(coefficient), 'direct_Fourier_coefficient': numerical})
    kappa = F(100) - F(66164, 10000)
    require(kappa * F(314, 100) ** 2 / 8 > 115, 'compact_response: original line 90')
    partial = sum((F(115, 2) ** n / math.factorial(n) for n in range(201)))
    require(partial > 9 * 10 ** 24, 'compact_response: original line 91')
    require(1 + F(345, 2) > 100, 'compact_response: original line 92')
    upper = F(4) / (115 * F(99, 100) * 9 * 10 ** 24)
    require(upper < F(4, 10 ** 27), 'compact_response: original line 93')
    result = {'Clifford_basis_zero_traces_and_exact_multiplication': True, 'actual_r2_Wilson_negative_Fourier_type': {'det_zero': str(d0), 'det_pi': str(dpi), 'W_pi_over_W_zero': float(F(dpi, d0) ** 2), 'M': M, 'r': r, 't0': t0}, 'full_4d_negative_Fourier_type': full4, 'closed_current_density_counterexample': looprows, 'strict_compact_density_upper': '4e-27', 'density_certificate': 'pi>3.14, a>115, exp(57.5)>9e24 by positive rational Taylor partial sum, exp(172.5)>100'}
    print(json.dumps(result, indent=2), flush=True)

def check_signed_source():
    from itertools import product
    import json
    import numpy as np
    from numpy.polynomial.hermite import hermgauss
    from scipy.integrate import quad

    def model(Q, B, z, U):
        eta = np.abs(z) * (1 + np.abs(z)) / (1 - np.abs(z)) ** 2
        R = np.diag(eta)
        vals, vecs = np.linalg.eigh(Q)
        Qi = vecs / np.sqrt(vals) @ vecs.T
        delta = float(np.linalg.eigvalsh(Qi @ B.T @ R @ B @ Qi)[-1])
        require(delta < 1, 'signed_source: original line 13')
        ns = np.array(list(product([-1, 0, 1], repeat=len(z))), float)
        coeff = np.prod(np.where(ns == 0, 1, z[None, :] / 2), axis=1)
        current = ns @ B
        coeff = coeff * np.exp(-np.einsum('ni,ij,nj->n', current, np.linalg.inv(Q), current) / 2)

        def exact(theta):
            weights = coeff * np.exp(1j * (ns @ theta))
            partition = np.sum(weights)
            first = np.einsum('n,ni->i', weights, 1j * ns)
            second = -np.einsum('n,ni,nj->ij', weights, ns, ns)
            require(abs(partition.imag) < 1e-12 and partition.real > 0, 'signed_source: original line 20')
            H = second / partition - np.outer(first, first) / partition ** 2
            require(np.max(np.abs(H.imag)) < 1e-12, 'signed_source: original line 22')
            return (float(partition.real), H.real)

        def quadrature(theta, n):
            nodes, weights = hermgauss(n)
            a = np.array(list(product(nodes, nodes))) * np.sqrt(2)
            w = np.prod(np.array(list(product(weights, weights))), axis=1) / np.pi
            a = a @ Qi
            f = np.prod(1 + z[None, :] * np.cos(a @ B.T + theta[None, :]), axis=1)
            return float(w @ f)
        p0, H0 = exact(np.zeros(len(z)))
        require(p0 > 0, 'signed_source: original line 28')
        rng = np.random.default_rng(709)
        worst = 0.0
        rows = []
        for theta in [np.zeros(len(z)), np.arange(len(z)) * 0.7, *rng.normal(size=(12, len(z))) * 3]:
            p, H = exact(theta)
            lr = np.log(p / p0)
            bound = theta @ R @ theta / 2
            require(np.linalg.eigvalsh(H + R)[0] > -1e-12, 'signed_source: original line 32')
            require(np.linalg.eigvalsh(R / (1 - delta) - H)[0] > -1e-12, 'signed_source: original line 33')
            require(-bound - 1e-12 <= lr <= bound / (1 - delta) + 1e-12, 'signed_source: original line 34')
            for n in [40, 64]:
                worst = max(worst, abs(quadrature(theta, n) - p))
            rows.append({'phase_norm': float(np.linalg.norm(theta)), 'log_ratio': float(lr), 'lower': -float(bound), 'upper': float(bound / (1 - delta))})
        require(worst < 1e-11, 'signed_source: original line 37')
        return {'Q': Q, 'B': B, 'R': R, 'U': U, 'delta': delta, 'partition0': p0, 'H0': H0, 'exact': exact, 'rows': rows, 'quadrature_error': worst}
    Q1 = np.diag([0.8, 1.3])
    B1 = np.array([[1, 0], [0, 1], [1, 1], [1, -1.0]])
    z1 = np.array([0.02, -0.025, 0.012, -0.008])
    U1 = np.array([[1, 0.2], [-0.3, 1], [0.4, -0.2], [-0.2, 0.5]])
    Q2 = np.array([[1.2, 0.2], [0.2, 1.7]])
    B2 = np.array([[0.8, 0.1], [0.2, 0.9], [1, -0.4]])
    z2 = np.array([-0.03, 0.015, -0.01])
    U2 = np.array([[0.5, -0.1], [0.4, 0.8], [0.7, 0.2]])
    models = [model(Q1, B1, z1, U1), model(Q2, B2, z2, U2)]
    G = np.diag([2.0, 3.0])
    Gi = np.diag(1 / np.sqrt(np.diag(G)))
    epsilon = max((float(np.linalg.eigvalsh(Gi @ m['U'].T @ m['R'] @ m['U'] @ Gi)[-1]) for m in models))
    delta = max((m['delta'] for m in models))
    require(epsilon < 1, 'signed_source: original line 45')
    cs = np.array([1.0, 2.0])
    weights = cs * np.array([m['partition0'] for m in models])
    weights /= sum(weights)
    Cov = G + sum((w * m['U'].T @ m['H0'] @ m['U'] for w, m in zip(weights, models)))
    require(np.linalg.eigvalsh(Cov - (1 - epsilon) * G)[0] > 0, 'signed_source: original line 48')
    require(np.linalg.eigvalsh((1 + epsilon / (1 - delta)) * G - Cov)[0] > 0, 'signed_source: original line 49')
    for h in [np.array([x, y]) for x, y in product([-0.9, 0, 0.5, 2.0], repeat=2)]:
        ratio = sum((w * m['exact'](m['U'] @ h)[0] / m['partition0'] for w, m in zip(weights, models)))
        logM = h @ G @ h / 2 + np.log(ratio)
        require((1 - epsilon) * h @ G @ h / 2 - 1e-12 <= logM <= (1 + epsilon / (1 - delta)) * h @ G @ h / 2 + 1e-12, 'signed_source: original line 52')
    z = -0.2
    Q = 2.0
    p0 = 1 + z * np.exp(-1 / (2 * Q))
    ppi = 1 - z * np.exp(-1 / (2 * Q))
    require(ppi > p0 > 0, 'signed_source: original line 55')
    beta = 12.0
    n = 6.0
    rho = 0.7
    c = 0.4
    var = beta / n
    integrand = lambda a: np.exp(-(a + c) ** 2 / (2 * var)) / np.sqrt(2 * np.pi * var)
    actual = quad(lambda a: integrand(a) * np.cos(rho * a), -np.inf, np.inf, epsabs=1e-12)[0] + 1j * quad(lambda a: integrand(a) * np.sin(rho * a), -np.inf, np.inf, epsabs=1e-12)[0]
    correct = np.exp(-beta * rho * rho / (2 * n) - 1j * rho * c)
    double_exponent = np.exp(-beta * rho * rho / n - 1j * rho * c)
    require(abs(actual - correct) < 1e-11 and abs(actual - double_exponent) > 0.1, 'signed_source: original line 61')
    out = {'models': [{'delta': m['delta'], 'quadrature_error': m['quadrature_error'], 'phase_cases': m['rows']} for m in models], 'mixture': {'delta': delta, 'epsilon': epsilon, 'covariance': Cov.tolist(), 'lower_covariance': ((1 - epsilon) * G).tolist(), 'upper_covariance': ((1 + epsilon / (1 - delta)) * G).tolist()}, 'negative_activity_shift_ratio': ppi / p0, 'conditional_Gaussian_correct_error': abs(actual - correct), 'doubled_exponent_rejected_error': abs(actual - double_exponent)}
    print(json.dumps(out, indent=2), flush=True)

def main():
    checks = [check_loop_filling, check_wilson_curvature, check_covariance_projection, check_integer_cochain, check_compact_marginal, check_compact_response, check_signed_source]
    for fn in checks:
        fn()
        print("PASS:", fn.__name__, flush=True)
    print("per_element: integer loop boundaries, Clifford traces and a full-box Fourier-type counterexample are checked")
    print("per_site: exact integer cochain contraction verifies sector labels without a real-rank torsion assumption")
    print("per_mode: curl and Bianchi symbols test covariance discontinuity and the closed-current response counterexample")
    print("per_block: determinant derivatives, normalized compact marginals and signed-source integrals use separate representations")
    print("lattice_wide: volume-uniform analytic bounds are proved in the note; compact infrared and Hamiltonian matching remain open")
    print("Internal finite assertions:", _ASSERTIONS, "(not independent scientific results)")
    print(f"TOTAL: PASS={len(checks)} FAIL=0")

if __name__ == "__main__":
    main()
