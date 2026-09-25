#!/usr/bin/env python3
"""J:derive:the-exchange-sign-with-three-or-more-records:a1 -- worker w-macbookpro9927a-j31aa (Claude Opus 5.5).

Exact checks: integers, Gaussian integers as (re, im) int pairs, Fractions, integer polynomials (CRT under a proven
coefficient bound), Descartes counts.  Floats appear only in part C to choose rational windows, which are then
certified exactly.

Walk (block 54 as landed on main): H = sum_j sigma_j D_j, D_j = (i/2)(T_j - T_j^dag), (T_e psi)(x) = psi(x - e);
on Z^2 the two-axis form sigma_1 D_1 + sigma_2 D_2 (block 128, PR #9185).  A hop x -> x + s e_j multiplies the coin
by (s/2) i sigma_j, so 2H has entries s i sigma_j.  N records under exclusion (block 78's compression):
H_N = Pi (sum_i h_i) Pi on configurations with distinct sites; P_pi permutes records; K+ / K- are the totally
symmetric / antisymmetric parts.  Block 55's source (main), uniform rate: e_x = sum_i Re <Psi|Q_x^(i) h_i|Psi>.
Traces are coin-summed; 'H units' = hop amplitude 1/2; 'per site' = divided by V (record 1 pinned at the origin)."""
import sys, time, hashlib
from fractions import Fraction as F
from itertools import product, permutations, combinations
from math import comb
import numpy as np

T0 = time.time()
RES = []


def check(tag, ok, msg):
    RES.append((tag, bool(ok)))
    print(f"{tag} {'PASS' if ok else 'FAIL'}: {msg}", flush=True)


# ---------------------------------------------------------------- lattice, walk, labelled records (2H units)
ISIG = {0: {0: (1, 1), 1: (0, 1)},      # i sigma_1 e_a = i^k e_b  -> (b, k)
        1: {0: (1, 2), 1: (0, 0)},      # i sigma_2
        2: {0: (0, 1), 1: (1, 3)}}      # i sigma_3


def rot(z, k):
    a, b = z
    k %= 4
    return (a, b) if k == 0 else (-b, a) if k == 1 else (-a, -b) if k == 2 else (b, -a)


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


class Torus:
    def __init__(self, d, L):
        self.d, self.L, self.V = d, L, L ** d
        self.coords = list(product(range(L), repeat=d))
        self.idx = {c: n for n, c in enumerate(self.coords)}
        self.nbr = []
        for c in self.coords:
            lst = []
            for j in range(d):
                for s in (1, -1):
                    cc = list(c); cc[j] = (cc[j] + s) % L
                    lst.append((self.idx[tuple(cc)], j, s))
            self.nbr.append(lst)

    def site(self, *c):
        return self.idx[tuple(x % self.L for x in c)]

    def dist(self, x, y):
        return sum(min((a - b) % self.L, (b - a) % self.L) for a, b in zip(self.coords[x], self.coords[y]))


def step(T, vec, free3=False, obstacles=()):
    """2H on {config: gauss}, config = (x1, a1, x2, a2, ...); free3: record 3 ignores records 1, 2 and vice versa"""
    out = {}
    for cfg, amp in vec.items():
        n = len(cfg) // 2
        occ = set(cfg[0::2]) | set(obstacles)
        for i in range(n):
            x, a = cfg[2 * i], cfg[2 * i + 1]
            if free3:
                block = {cfg[2 * (1 - i)]} if i < 2 else set()
            else:
                block = occ
            for (y, j, s) in T.nbr[x]:
                if y in block:
                    continue
                b, k = ISIG[j][a]
                new = cfg[:2 * i] + (y, b) + cfg[2 * i + 2:]
                z = rot(amp, k + (2 if s < 0 else 0))
                o = out.get(new)
                out[new] = z if o is None else (o[0] + z[0], o[1] + z[1])
    return {c: z for c, z in out.items() if z != (0, 0)}


def permute(cfg, perm):
    n = len(cfg) // 2
    new = [None] * n
    for i in range(n):
        new[perm[i]] = (cfg[2 * i], cfg[2 * i + 1])
    return tuple(v for p in new for v in p)


def inner(u, v):
    re = im = 0
    for c, z in v.items():
        w = u.get(c)
        if w is not None:
            re += w[0] * z[0] + w[1] * z[1]
            im += w[0] * z[1] - w[1] * z[0]
    return (re, im)


def perm_elem(T, s, perm, k, free3=False):
    """<P_perm s|(2H)^k|s> = <P v1|v2>, v1 = (2H)^floor(k/2) s, v2 = (2H)^ceil(k/2) s"""
    v1 = {s: (1, 0)}
    for _ in range(k // 2):
        v1 = step(T, v1, free3)
    v2 = v1
    if k % 2:
        v2 = step(T, v1, free3)
    return inner({permute(c, perm): z for c, z in v1.items()}, v2)


# ---------------------------------------------------------------- infinite-lattice path method (2H units)
I2 = ((1, 0), (0, 0), (0, 0), (1, 0))
IS = [((0, 0), (0, 1), (0, 1), (0, 0)), ((0, 0), (1, 0), (-1, 0), (0, 0)), ((0, 1), (0, 0), (0, 0), (0, -1))]


def gm(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def mm(A, B):
    return (gadd(gm(A[0], B[0]), gm(A[1], B[2])), gadd(gm(A[0], B[1]), gm(A[1], B[3])),
            gadd(gm(A[2], B[0]), gm(A[3], B[2])), gadd(gm(A[2], B[1]), gm(A[3], B[3])))


def mtr(A):
    return gadd(A[0], A[3])


def hopmat(j, s):
    return IS[j] if s > 0 else tuple((-z[0], -z[1]) for z in IS[j])


def addv(x, j, s):
    y = list(x); y[j] += s
    return tuple(y)


def l1(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))


def walks(d, start, end, n):
    out = []

    def rec(x, left, acc):
        if l1(x, end) > left:
            return
        if left == 0:
            out.append(list(acc)); return
        for j in range(d):
            for s in (1, -1):
                acc.append((j, s)); rec(addv(x, j, s), left - 1, acc); acc.pop()
    rec(start, n, [])
    return out


def pair_histories(d, x2, m):
    o = tuple([0] * d)
    D = l1(o, x2)
    for n1 in range(D, m - D + 1):
        n2 = m - n1
        if (n1 - D) % 2 or n2 < D:
            continue
        W1, W2 = walks(d, o, x2, n1), walks(d, x2, o, n2)
        for slots in combinations(range(m), n1):
            sl = set(slots)
            for w1 in W1:
                for w2 in W2:
                    p1, p2, M1, M2, i1, i2, ok, traj = o, x2, I2, I2, 0, 0, True, [(o, x2)]
                    for t in range(m):
                        if t in sl:
                            j, s = w1[i1]; i1 += 1; p1 = addv(p1, j, s); M1 = mm(hopmat(j, s), M1)
                        else:
                            j, s = w2[i2]; i2 += 1; p2 = addv(p2, j, s); M2 = mm(hopmat(j, s), M2)
                        if p1 == p2:
                            ok = False; break
                        traj.append((p1, p2))
                    if ok:
                        yield mtr(mm(M1, M2)), traj


def rel_sites(d, r):
    return [x for x in product(range(-r, r + 1), repeat=d) if 0 < sum(abs(v) for v in x) <= r]


def pair_trace(d, m):
    tot = (0, 0)
    for x2 in rel_sites(d, m // 2):
        for amp, _ in pair_histories(d, x2, m):
            tot = gadd(tot, amp)
    return tot


def closed_walks(d, n):
    o = tuple([0] * d)
    res = []
    for w in walks(d, o, o, n):
        M, x, disp = I2, o, [o]
        for (j, s) in w:
            M = mm(hopmat(j, s), M); x = addv(x, j, s); disp.append(x)
        res.append((mtr(M), disp))
    return res


def connected3(d, k):
    """per-site connected three-record part of tr(P_12 (2H_3)^k): minus the reference histories (records 1,2 exclude
    each other, record 3 free) in which record 3 ever shares a site with record 1 or 2; split by record 3's hops"""
    parts = {}
    for n3 in range(0, k - 3, 2):
        m = k - n3
        C3 = closed_walks(d, n3)
        tot = (0, 0)
        for x2 in rel_sites(d, m // 2):
            for amp, traj in pair_histories(d, x2, m):
                for t3, disp in C3:
                    w = gm(amp, t3)
                    for slots3 in combinations(range(k), n3):
                        s3 = set(slots3); ip = i3 = 0
                        p1, p2 = traj[0]; q = disp[0]
                        col = {tuple(a - b for a, b in zip(p1, q)), tuple(a - b for a, b in zip(p2, q))}
                        for t in range(k):
                            if t in s3:
                                i3 += 1; q = disp[i3]
                            else:
                                ip += 1; p1, p2 = traj[ip]
                            col.add(tuple(a - b for a, b in zip(p1, q))); col.add(tuple(a - b for a, b in zip(p2, q)))
                        tot = (tot[0] - w[0] * len(col), tot[1] - w[1] * len(col))
        parts[n3] = tot
    return parts


def cycles_of(pi):
    seen, out = set(), []
    for i in range(len(pi)):
        if i in seen:
            continue
        c = [i]; seen.add(i); j = pi[i]
        while j != i:
            c.append(j); seen.add(j); j = pi[j]
        out.append(c)
    return out


def interleavings(counts):
    out, cnt, seq, total = [], list(counts), [], sum(counts)

    def rec():
        if len(seq) == total:
            out.append(tuple(seq)); return
        for i, c in enumerate(cnt):
            if c:
                cnt[i] -= 1; seq.append(i); rec(); seq.pop(); cnt[i] += 1
    rec()
    return out


def perm_trace(d, pi, k, R):
    """per-site tr(P (2H_n)^k) for a permutation pi without fixed points; record i walks x_i -> x_pi(i)"""
    n = len(pi)
    o = tuple([0] * d)
    box = [x for x in product(range(-R, R + 1), repeat=d) if sum(abs(v) for v in x) <= R and x != o]
    cyc = cycles_of(pi)
    total, cache = (0, 0), {}
    for rest in permutations(box, n - 1):
        X = (o,) + rest
        mins = [l1(X[i], X[pi[i]]) for i in range(n)]
        if sum(mins) > k:
            continue
        comps = []

        def rec(i, left, acc):
            if i == n:
                if left == 0:
                    comps.append(tuple(acc))
                return
            v = mins[i]
            while v <= left:
                if v % 2 == mins[i] % 2:
                    acc.append(v); rec(i + 1, left - v, acc); acc.pop()
                v += 1
        rec(0, k, [])
        for ns in comps:
            W = [walks(d, X[i], X[pi[i]], ns[i]) for i in range(n)]
            if ns not in cache:
                cache[ns] = interleavings(ns)
            for seq in cache[ns]:
                for choice in product(*W):
                    pos, Ms, idx, ok = list(X), [I2] * n, [0] * n, True
                    for r in seq:
                        j, s = choice[r][idx[r]]; idx[r] += 1
                        y = addv(pos[r], j, s)
                        if y in pos:
                            ok = False; break
                        pos[r] = y; Ms[r] = mm(hopmat(j, s), Ms[r])
                    if ok:
                        amp = (1, 0)
                        for c in cyc:
                            P = I2
                            for i in c:
                                P = mm(Ms[i], P)
                            amp = gm(amp, mtr(P))
                        total = gadd(total, amp)
    return total


# ---------------------------------------------------------------- block 55's source: Taylor coefficients (exact)
def hop_i(T, vec, i):
    out = {}
    for cfg, amp in vec.items():
        occ = set(cfg[0::2])
        x, a = cfg[2 * i], cfg[2 * i + 1]
        for (y, j, s) in T.nbr[x]:
            if y in occ:
                continue
            b, k = ISIG[j][a]
            new = cfg[:2 * i] + (y, b) + cfg[2 * i + 2:]
            z = rot(amp, k + (2 if s < 0 else 0))
            o = out.get(new)
            out[new] = z if o is None else (o[0] + z[0], o[1] + z[1])
    return out


def edens(T, phi, chi, N):
    """x -> sum_i <Q_x^(i) phi|2h_i chi> + <2h_i phi|Q_x^(i) chi>  (= 4 <phi|e_x|chi> in 2H units)"""
    f = {}
    for i in range(N):
        for (A, Bv, left) in ((hop_i(T, chi, i), phi, True), (chi, hop_i(T, phi, i), False)):
            for c, z in A.items():
                w = Bv.get(c)
                if w is not None:
                    v = (w[0] * z[0] + w[1] * z[1], w[0] * z[1] - w[1] * z[0])
                    f[c[2 * i]] = gadd(f.get(c[2 * i], (0, 0)), v)
    return f


def parity(p):
    p = list(p); s = 1
    for i in range(len(p)):
        while p[i] != i:
            j = p[i]; p[i], p[j] = p[j], p[i]; s = -s
    return s


def product_state(sites, coins):
    vec = {(): (1, 0)}
    for x, (c0, c1) in zip(sites, coins):
        new = {}
        for cfg, z in vec.items():
            for a, w in ((0, c0), (1, c1)):
                if w != (0, 0):
                    new[cfg + (x, a)] = gm(z, w)
        vec = new
    return vec


def source_coeff(T, S, N, n, which):
    """2 * sum over the chosen permutations of <P S| L^n(e_x) |S>, L(A) = i[H,A], H units, not divided by <S|S>;
    which = 'odd' gives d^n/dt^n (e+ - e-) * <S|S>; 'id' twice the direct part; 'even' twice the even non-identity part"""
    u = [dict(S)]
    for _ in range(n):
        u.append(step(T, u[-1]))
    tot = {}
    for p in permutations(range(N)):
        par = parity(p)
        if (which == "odd" and par != -1) or (which == "id" and p != tuple(range(N))) or \
           (which == "even" and (par != 1 or p == tuple(range(N)))):
            continue
        for j in range(n + 1):
            f = edens(T, {permute(c, p): z for c, z in u[j].items()}, u[n - j], N)
            coef = comb(n, j) * (-1) ** (n - j)
            for x, z in f.items():
                w = rot(z, n)
                tot[x] = gadd(tot.get(x, (0, 0)), (coef * w[0], coef * w[1]))
    out = {}
    for x, z in tot.items():
        assert z[1] == 0
        if z[0]:
            out[x] = F(z[0], 2 ** (n + 1))
    return out


# ---------------------------------------------------------------- sectors on small tori, exact characteristic polynomials
def sort_sign(lst):
    arr, sgn = list(lst), 1
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]; sgn = -sgn
    return tuple(arr), sgn


def sector_hops(T, c, eps):
    occ = {x for (x, _) in c}
    for p, (x, a) in enumerate(c):
        for (y, j, s) in T.nbr[x]:
            if y in occ:
                continue
            b, k = ISIG[j][a]
            lst = list(c); lst[p] = (y, b)
            new, sg = sort_sign(lst)
            yield new, (k + (2 if s < 0 else 0)) % 4, (sg if eps < 0 else 1)


def block_entries(T, N, eps):
    L, d = T.L, T.d
    shifts = list(product(range(L), repeat=d))

    def sh(x, t):
        return T.idx[tuple((a + b) % L for a, b in zip(T.coords[x], t))]
    info, stab, reps = {}, {}, []
    for sites in combinations(range(T.V), N):
        for coins in product((0, 1), repeat=N):
            c = tuple(zip(sites, coins))
            if c in info:
                continue
            rep = min(sort_sign([(sh(x, t), a) for (x, a) in c])[0] for t in shifts)
            reps.append(rep)
            st = []
            for t in shifts:
                im, sg = sort_sign([(sh(x, t), a) for (x, a) in rep])
                sg = sg if eps < 0 else 1
                if im not in info:
                    info[im] = (rep, t, sg)
                if im == rep:
                    st.append((t, sg))
            stab[rep] = st
    terms = {}
    for c in reps:
        for (new, k, sg) in sector_hops(T, c, eps):
            rep, t, sg2 = info[new]
            terms.setdefault((rep, c), []).append((k, sg * sg2, t))
    return reps, stab, terms


def live(reps, stab, K, L):
    out = []
    for r in reps:
        acc = [0] * L
        for (t, sg) in stab[r]:
            acc[sum(a * b for a, b in zip(K, t)) % L] += sg
        zero = (acc[0] == acc[2] and acc[1] == acc[3]) if L == 4 else (acc[0] == acc[1] == acc[2])
        if not zero:
            out.append(r)
    return out


def block_float(reps, stab, terms, K, L):
    lv = live(reps, stab, K, L)
    ix = {r: n for n, r in enumerate(lv)}
    M = np.zeros((len(lv), len(lv)), dtype=complex)
    w = np.exp(2j * np.pi / L)
    for (rp, c), lst in terms.items():
        if rp in ix and c in ix:
            for (k, sg, t) in lst:
                M[ix[rp], ix[c]] += sg * (1j ** k) * w ** (-sum(a * b for a, b in zip(K, t)) % L)
    return M


def block_modp(reps, stab, terms, K, L, p, r, z):
    lv = live(reps, stab, K, L)
    ix = {c: n for n, c in enumerate(lv)}
    A = np.zeros((len(lv), len(lv)), dtype=np.int64)
    zeta = r if L == 4 else z
    ipow = [1, r, p - 1, p - r]
    for (rp, c), lst in terms.items():
        if rp in ix and c in ix:
            for (k, sg, t) in lst:
                v = ipow[k] * pow(zeta, (-sum(a * b for a, b in zip(K, t))) % L, p) % p
                A[ix[rp], ix[c]] = (A[ix[rp], ix[c]] + (v if sg > 0 else p - v)) % p
    return A


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


PRIMES = []
_p = (1 << 26) - ((1 << 26) % 12) + 1
while len(PRIMES) < 200:
    _p -= 12
    if is_prime(_p):
        PRIMES.append(_p)


def roots_mod(p):
    r = next(pow(g, (p - 1) // 4, p) for g in range(2, 500) if pow(pow(g, (p - 1) // 4, p), 2, p) == p - 1)
    z = next(pow(g, (p - 1) // 3, p) for g in range(2, 500) if pow(g, (p - 1) // 3, p) != 1)
    return r, z


def charpoly_mod(A, p):
    A = A.copy() % p
    n = A.shape[0]
    assert n < 2048 and p < (1 << 26)
    for col in range(n - 2):
        piv = next((r for r in range(col + 1, n) if A[r, col] % p), None)
        if piv is None:
            continue
        if piv != col + 1:
            A[[piv, col + 1], :] = A[[col + 1, piv], :]
            A[:, [piv, col + 1]] = A[:, [col + 1, piv]]
        m = (A[col + 2:, col] * pow(int(A[col + 1, col]), p - 2, p)) % p
        if not m.any():
            continue
        A[col + 2:, :] = (A[col + 2:, :] - (m[:, None] * A[col + 1, :][None, :]) % p) % p
        A[:, col + 1] = (A[:, col + 1] + (A[:, col + 2:] @ m) % p) % p
    P = [np.array([1], dtype=np.int64)]
    for k in range(1, n + 1):
        prev = P[k - 1]
        new = np.zeros(k + 1, dtype=np.int64)
        new[1:] = prev
        new[:k] = (new[:k] - (A[k - 1, k - 1] * prev) % p) % p
        prod = 1
        for i in range(k - 1, 0, -1):
            prod = prod * int(A[i, i - 1]) % p
            if prod == 0:
                break
            coef = int(A[i - 1, k - 1]) * prod % p
            if coef:
                q = P[i - 1]
                new[:len(q)] = (new[:len(q)] - (coef * q) % p) % p
        P.append(new)
    return [int(v) for v in P[n]]


def polymul_mod(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        if u:
            for j, v in enumerate(b):
                out[i + j] = (out[i + j] + u * v) % p
    return out


def classes(L):
    Ks = list(product(range(L), repeat=2))
    if L == 4:
        return [[K] for K in Ks]
    seen, out = set(), []
    for K in Ks:
        if K not in seen:
            mK = tuple((-a) % L for a in K)
            cl = [K] if mK == K else [K, mK]
            seen.update(cl); out.append(cl)
    return out


def class_poly(reps, stab, terms, cl, L, R):
    """integer char poly of 2H_N on the momentum class (a Galois orbit {K, -K} on L = 3); CRT with bound
    max_k C(n,k) R^k, |eig| <= R = 2dN (row sums of the Hermitian 2H_N in an orthonormal sector basis)"""
    n = sum(len(live(reps, stab, K, L)) for K in cl)
    B = max(comb(n, k) * R ** k for k in range(n + 1))
    res, M, used = None, 1, 0
    for p in PRIMES:
        r, z = roots_mod(p)
        poly = [1]
        for K in cl:
            poly = polymul_mod(poly, charpoly_mod(block_modp(reps, stab, terms, K, L, p, r, z), p), p)
        if res is None:
            res = poly
        else:
            inv = pow(M % p, p - 2, p)
            res = [a + M * (((c - a) * inv) % p) for a, c in zip(res, poly)]
        M *= p; used += 1
        if M > 4 * B:
            break
    assert M > 4 * B
    res = [v - M if v > M // 2 else v for v in res]
    assert res[-1] == 1 and len(res) == n + 1
    return res


def count_below(c, a, b):
    """roots (with multiplicity) below a/b of a real-rooted integer polynomial c (low->high): sign variations of
    b^n c(a/b - y) (Descartes' rule, exact for real-rooted polynomials: ASSUMED)"""
    n = len(c) - 1
    g = [0]
    for k in range(n, -1, -1):
        ng = [0] * (len(g) + 1)
        for i, v in enumerate(g):
            ng[i] += v * a; ng[i + 1] -= v * b
        ng[0] += c[k] * b ** (n - k)
        g = ng
    while len(g) > 1 and g[-1] == 0:
        g.pop()
    assert g[0] != 0
    s = [v for v in g if v]
    return sum(1 for u, v in zip(s, s[1:]) if (u > 0) != (v > 0))


# ================================================================ W: the walk's coin algebra
def q_of(p):
    M = I2
    for j in range(3):
        if p[j]:
            M = mm(M, IS[j])
    return M


bad = 0
nw = 0
for n in range(0, 7):
    for w in product([(j, s) for j in range(3) for s in (1, -1)], repeat=n):
        M, x = I2, (0, 0, 0)
        for (j, s) in w:
            M = mm(hopmat(j, s), M); x = addv(x, j, s)
        q = q_of(tuple(v % 2 for v in x))
        nw += 1
        if M != q and M != tuple((-z[0], -z[1]) for z in q):
            bad += 1
check("W1", bad == 0, f"all {nw} walks of <= 6 hops on Z^3: coin factor = +-q(displacement mod 2), q in "
                     "{1, i s1, i s2, i s3} products (quaternion group mod sign is abelian)")
check("W2", all(ISIG[j][a][0] == 1 - a for j in (0, 1) for a in (0, 1)),
      "on Z^2 every hop flips the sigma_3 coin and the sublattice: g = (-1)^(a+x1+x2) is kept by each record")

# ================================================================ A: traces
# A1 sector identity on the odd 3x3 torus, N = 3, k = 2, 3, 4 (windings of odd length included)
T3 = Torus(2, 3)
lab = [s for s in product(range(9), (0, 1), range(9), (0, 1), range(9), (0, 1)) if len({s[0], s[2], s[4]}) == 3]
Lt = {}
for k in (2, 3, 4):
    for pi in ((0, 1, 2), (1, 0, 2), (1, 2, 0)):
        tot = (0, 0)
        for s in lab:
            tot = gadd(tot, perm_elem(T3, s, pi, k))
        Lt[(k, pi)] = tot
sec = {}
for eps in (1, -1):
    basis = [tuple(zip(st, a)) for st in combinations(range(9), 3) for a in product((0, 1), repeat=3)]
    for k in (2, 3, 4):
        tot = (0, 0)
        for c in basis:
            v1 = {c: (1, 0)}
            for _ in range(k // 2):
                nv = {}
                for cc, z in v1.items():
                    for (new, kk, sg) in sector_hops(T3, cc, eps):
                        w = rot(z, kk)
                        w = w if sg > 0 else (-w[0], -w[1])
                        nv[new] = gadd(nv.get(new, (0, 0)), w)
                v1 = nv
            v2 = v1
            if k % 2:
                nv = {}
                for cc, z in v1.items():
                    for (new, kk, sg) in sector_hops(T3, cc, eps):
                        w = rot(z, kk)
                        w = w if sg > 0 else (-w[0], -w[1])
                        nv[new] = gadd(nv.get(new, (0, 0)), w)
                v2 = nv
            tot = gadd(tot, inner(v1, v2))
        sec[(eps, k)] = tot
ok = all(sec[(e, k)][0] * 6 == Lt[(k, (0, 1, 2))][0] + e * 3 * Lt[(k, (1, 0, 2))][0] + 2 * Lt[(k, (1, 2, 0))][0]
         for e in (1, -1) for k in (2, 3, 4))
check("A1", ok, "3x3 torus, N=3, k=2,3,4: tr_K+- (2H)^k = [tr + -3 tr P_12 + 2 tr P_123]/6 (exact integers), so "
      f"tr_K+ - tr_K- = tr P_12 (k=4: {Lt[(4, (1, 0, 2))][0]}); the ring exchange enters only tr_K+ + tr_K-")

# A2 pair (block 128's values, conventions)
p4 = {}
for d in (2, 3):
    T = Torus(d, 5)
    o = T.site(*([0] * d))
    tot = {2: (0, 0), 4: (0, 0)}
    per = {}
    for x2 in range(T.V):
        if x2 == o or T.dist(o, x2) > 2:
            continue
        for a1, a2 in product((0, 1), repeat=2):
            for k in (2, 4):
                z = perm_elem(T, (o, a1, x2, a2), (1, 0), k)
                tot[k] = gadd(tot[k], z)
                if k == 4 and d == 3:
                    key = tuple(sorted(min(v, 5 - v) for v in T.coords[x2]))
                    per[key] = gadd(per.get(key, (0, 0)), z)
    p4[d] = tot[4][0]
    ok = tot[2] == (0, 0) and tot[4] == (-128 * (1 if d == 2 else 3), 0)
    if d == 3:
        ok = ok and per[(0, 0, 1)][0] == -2 * 16 * 6 and per[(0, 1, 1)][0] == -16 * 12 and per.get((0, 0, 2), (0, 0)) == (0, 0)
    check(f"A2.{d}", ok, f"Z^{d}: two records, per site tr P(2H_2)^2 = 0, tr P(2H_2)^4 = {tot[4][0]} "
          f"(= {tot[4][0] // 16} in H units: -8 per plaquette)" + ("; per pair -2, -1, 0" if d == 3 else ""))

# A3 three records at order 4, 5-tori (side >= 5: no winding below order 5)
for d in (2, 3):
    T = Torus(d, 5)
    o = T.site(*([0] * d))
    V, npl = T.V, (1 if d == 2 else 3)
    act, ref, cyc3, k2, k3 = (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
    for x2 in range(T.V):
        if x2 == o or T.dist(o, x2) > 2:
            continue
        for x3 in range(T.V):
            for a in product((0, 1), repeat=3):
                s = (o, a[0], x2, a[1], x3, a[2])
                if x3 not in (o, x2):
                    act = gadd(act, perm_elem(T, s, (1, 0, 2), 4))
                    k2 = gadd(k2, perm_elem(T, s, (1, 0, 2), 2))
                    k3 = gadd(k3, perm_elem(T, s, (1, 0, 2), 3))
                    if T.dist(o, x3) <= 2:
                        cyc3 = gadd(cyc3, perm_elem(T, s, (1, 2, 0), 4))
                ref = gadd(ref, perm_elem(T, s, (1, 0, 2), 4, free3=True))
    ok = (act == (-16 * 16 * npl * (V - 4), 0) and ref == (-16 * 16 * npl * V, 0) and cyc3 == (-3 * 16 * npl, 0)
          and k2 == (0, 0) and k3 == (0, 0))
    check(f"A3.{d}", ok, f"Z^{d} side 5, N=3, H units per site: tr P_12 H^2 = tr P_12 H^3 = 0; tr P_12 H^4 = "
          f"{act[0] // 16} = -16*{npl}(V-4); free-third reference {ref[0] // 16}; connected {(act[0] - ref[0]) // 16}; "
          f"ring exchange tr P_123 H^4 = {cyc3[0] // 16}")

# A4 four records at order 4 on the 5x5 torus: general-N formula
T = Torus(2, 5)
o = T.site(0, 0)
acc = (0, 0)
others = [x for x in range(T.V) if x != o]
for x2 in others:
    if T.dist(o, x2) > 2:
        continue
    for x3, x4 in permutations([x for x in others if x != x2], 2):
        for a in product((0, 1), repeat=4):
            acc = gadd(acc, perm_elem(T, (o, a[0], x2, a[1], x3, a[2], x4, a[3]), (1, 0, 2, 3), 4))
V = 25
check("A4", acc == (-16 * 8 * 4 * (V - 4) * (V - 5), 0),
      f"Z^2 side 5, N=4: tr P_12 H^4 / V = {acc[0] // 16} = -8*2^2*(V-4)(V-5); sector difference = tr P_12 H^4/(N-2)! "
      "= -8 n_p V 2^(N-2) C(V-4,N-2)")

# A5 minimal orders on the infinite lattice: no four-record ring exchange below order 6
check("A5", all(perm_trace(d, (1, 2, 3, 0), 4, 2) == (0, 0) for d in (2, 3)),
      "the four-record ring exchange (a 4-cycle, odd) has zero trace at order 4 on Z^2 and Z^3")

# A6-A8 order 6 on the infinite lattice (path method), checked against brute force on the 7x7 torus
P6, C6, R3, R4 = {}, {}, {}, {}
for d in (2, 3):
    P6[d] = pair_trace(d, 6)
    C6[d] = connected3(d, 6)
    R3[d] = (perm_trace(d, (1, 2, 0), 4, 2), perm_trace(d, (1, 2, 0), 6, 3))
    R4[d] = perm_trace(d, (1, 2, 3, 0), 6, 3)
check("A6", P6[2] == (-3840, 0) and P6[3] == (-16128, 0) and pair_trace(2, 4) == (p4[2], 0) and pair_trace(3, 4) == (p4[3], 0),
      f"pair exchange per site, H units: order 4: -8 (Z^2), -24 (Z^3); order 6: {P6[2][0] // 64} (Z^2), {P6[3][0] // 64} (Z^3)")
T = Torus(2, 7)
o = T.site(0, 0)
act, ref = (0, 0), (0, 0)
for x2 in range(T.V):
    if x2 == o or T.dist(o, x2) > 3:
        continue
    for x3 in range(T.V):
        for a in product((0, 1), repeat=3):
            s = (o, a[0], x2, a[1], x3, a[2])
            if x3 not in (o, x2):
                act = gadd(act, perm_elem(T, s, (1, 0, 2), 6))
            ref = gadd(ref, perm_elem(T, s, (1, 0, 2), 6, free3=True))
t2 = sum(z[0] for z, _ in closed_walks(2, 2))
c6 = {d: sum(v[0] for v in C6[d].values()) for d in (2, 3)}
ok = (act[0] - ref[0] == c6[2] and ref[0] == 49 * (15 * p4[2] * t2 + 2 * P6[2][0]) and c6[2] == 112896 and c6[3] == 519936
      and C6[2] == {0: (30720, 0), 2: (82176, 0)} and C6[3] == {0: (119040, 0), 2: (400896, 0)})
check("A7", ok, f"connected three-record part per site, order 6, H units: Z^2 {c6[2] // 64} (third record static "
      f"{C6[2][0][0] // 64}, stepping out and back {C6[2][2][0] // 64}), Z^3 {c6[3] // 64} ({C6[3][0][0] // 64} + "
      f"{C6[3][2][0] // 64}); 7x7 brute force: actual - reference = {(act[0] - ref[0]) // 64}")
b3 = b4 = (0, 0)
ball = [x for x in range(T.V) if x != o and T.dist(o, x) <= 3]
for n, pi in ((3, (1, 2, 0)), (4, (1, 2, 3, 0))):
    inv = [0] * n
    for i in range(n):
        inv[pi[i]] = i
    tot = (0, 0)
    for rest in permutations(ball, n - 1):
        X = (o,) + rest
        if sum(T.dist(X[j], X[inv[j]]) for j in range(n)) > 6:
            continue
        for a in product((0, 1), repeat=n):
            tot = gadd(tot, perm_elem(T, tuple(v for x, c in zip(X, a) for v in (x, c)), pi, 6))
    if n == 3:
        b3 = tot
    else:
        b4 = tot
ok = (R3[2] == ((-48, 0), (5760, 0)) and R3[3] == ((-144, 0), (44928, 0)) and R4[2] == (4992, 0) and R4[3] == (34944, 0)
      and b3 == R3[2][1] and b4 == R4[2])
check("A8", ok, f"ring exchanges per site, H units: three records (even) order 4: -3 (Z^2), -9 (Z^3); order 6: "
      f"{R3[2][1][0] // 64}, {R3[3][1][0] // 64}; four records (odd) order 6: {R4[2][0] // 64} (Z^2), {R4[3][0] // 64} (Z^3); "
      "Z^2 values = 7x7 brute force")

# ================================================================ B: block 55's source of site-localised clusters
T = Torus(2, 11)
gen, g2, y, g3 = ((2, 0), (1, 1)), ((1, 0), (2, -1)), ((1, 0), (0, 1)), ((3, 0), (1, -2))
ok = True
for pts in (((0, 0), (1, 0)), ((0, 0), (1, 1)), ((0, 0), (2, 1))):
    S = product_state(tuple(T.site(*p) for p in pts), (gen, g2))
    for n in range(1, 6):
        ok = ok and not source_coeff(T, S, 2, n, "odd") and not source_coeff(T, S, 2, n, "id")
check("B1", ok, "two records (neighbours, diagonal, knight's move), complex coins: every Taylor coefficient of the "
      "source up to t^5 vanishes, direct and exchange parts alike")
ok = True
for pts in (((0, 0), (1, 0), (0, 1)), ((-1, 0), (0, 0), (1, 0))):
    S = product_state(tuple(T.site(*p) for p in pts), (gen, g2, y))
    for n in (1, 2, 3):
        ok = ok and not source_coeff(T, S, 3, n, "odd") and not source_coeff(T, S, 3, n, "id")
S = product_state((T.site(0, 0), T.site(1, 0), T.site(0, 1)), (gen, g2, y))
norm = sum(z[0] ** 2 + z[1] ** 2 for z in S.values())
E = {T.coords[x]: v / norm / 2 for x, v in source_coeff(T, S, 3, 3, "even").items()}
T3d = Torus(3, 7)
S3 = product_state((T3d.site(0, 0, 0), T3d.site(1, 0, 0), T3d.site(0, 1, 0)), (gen, g2, y))
for n in (1, 2, 3):
    ok = ok and not source_coeff(T3d, S3, 3, n, "odd")
check("B2", ok and E == {(1, 0): F(1, 144), (0, 1): F(-1, 144)},
      "three records (L and line on Z^2, L on Z^3), complex coins: e+ - e- = 0 through t^3; the common source's "
      f"t^3 coefficient is the ring exchange alone, d^3e/dt^3 = {dict((k, str(v)) for k, v in E.items())}")
S = product_state(tuple(T.site(*p) for p in ((0, 0), (1, 0), (1, 1), (0, 1))), (gen, g2, y, g3))
norm = sum(z[0] ** 2 + z[1] ** 2 for z in S.values())
D3 = source_coeff(T, S, 4, 3, "odd")
D5 = {T.coords[x]: v / norm for x, v in source_coeff(T, S, 4, 5, "odd").items()}
want = {(0, 2): -1, (0, 10): 1, (1, 2): 1, (1, 10): -1, (2, 0): 1, (2, 1): -1, (10, 0): -1, (10, 1): 1}
check("B3", not D3 and D5 == {k: F(v, 224) for k, v in want.items()},
      "four records on a plaquette, complex coins: d^3(e+ - e-)/dt^3 = 0, d^5(e+ - e-)/dt^5 = +-1/224 on the far "
      "corners of the four neighbouring plaquettes (sum 0)")

# ================================================================ C: ground energies on the 3x3 and 4x4 tori
import sympy as sp
xs = sp.symbols('x')
summ = {}
for (L, N) in ((3, 2), (3, 3), (3, 4), (4, 2), (4, 3)):
    T = Torus(2, L)
    for eps in (1, -1):
        reps, stab, terms = block_entries(T, N, eps)
        polys, mins = {}, {}
        for cl in classes(L):
            polys[str(cl)] = class_poly(reps, stab, terms, cl, L, 4 * N)
            mins[str(cl)] = min(min(np.linalg.eigvals(block_float(reps, stab, terms, K, L)).real) for K in cl
                                if live(reps, stab, K, L))
        lam = F(min(mins.values())).limit_denominator(10 ** 9)
        lo, hi = lam - F(1, 10 ** 8), lam + F(1, 10 ** 8)
        dim = sum(len(p) - 1 for p in polys.values())
        below_lo = sum(count_below(p, lo.numerator, lo.denominator) for p in polys.values())
        found, mult = None, 0
        for cl, p in polys.items():
            if not count_below(p, hi.numerator, hi.denominator):
                continue
            for qs, m in sp.Poly(list(reversed(p)), xs, domain='ZZ').sqf_list()[1]:
                qsc = [int(c) for c in reversed(qs.all_coeffs())]
                if count_below(qsc, hi.numerator, hi.denominator) == count_below(qsc, lo.numerator, lo.denominator):
                    continue
                for r, _ in qs.factor_list()[1]:
                    rc = [int(c) for c in reversed(r.all_coeffs())]
                    rc = rc if rc[-1] > 0 else [-c for c in rc]
                    kq = count_below(rc, hi.numerator, hi.denominator) - count_below(rc, lo.numerator, lo.denominator)
                    if kq:
                        assert kq == 1
                        found = rc if found is None else found
                        assert found == rc
                        mult += m
        m_hi = sum(count_below(p, hi.numerator, hi.denominator) for p in polys.values())
        summ[(L, N, eps)] = (found, lo, hi, mult)
        h = hashlib.sha256(str(found).encode()).hexdigest()[:10]
        ok = below_lo == 0 and m_hi == mult and dim == 2 ** N * comb(L * L, N)
        qtxt = str(sp.Poly(list(reversed(found)), xs).as_expr()) if len(found) <= 9 else f"deg {len(found) - 1}, sha {h}"
        check(f"C{L}{N}{'+' if eps > 0 else '-'}", ok, f"{L}x{L}, N={N}, {'sym ' if eps > 0 else 'anti'}: E0 = "
              f"{float(lam) / 2:.10f} (2E0 root of {qtxt}), {mult}-fold; no eigenvalue below")
for (L, N) in ((3, 2), (3, 3), (3, 4)):
    sp_, sm_ = summ[(L, N, 1)], summ[(L, N, -1)]
    check(f"D{L}{N}", sm_[2] < sp_[1], f"{L}x{L}, N={N}: antisymmetric ground energy below symmetric (disjoint windows)")
for (L, N) in ((4, 2), (4, 3)):
    sp_, sm_ = summ[(L, N, 1)], summ[(L, N, -1)]
    lo, hi = max(sp_[1], sm_[1]), min(sp_[2], sm_[2])
    q = sp_[0]
    eq = sp_[0] == sm_[0] and lo < hi and count_below(q, hi.numerator, hi.denominator) - count_below(q, lo.numerator, lo.denominator) == 1
    check(f"D{L}{N}", eq, f"{L}x{L}, N={N}: both ground energies are the one root of the same irreducible polynomial "
          "in the common window: equal")

npass = sum(1 for _, ok in RES if ok)
print(f"TOTAL: PASS={npass} FAIL={len(RES) - npass} ({time.time() - T0:.0f}s)")
if npass == len(RES):
    print("SUMMARY: PARTIAL exchange sign with N>=3 records under exclusion: traces first differ at order 4 for every N; "
          "three records add only exclusion; four-record ring exchange from order 6; the source is sector-blind for N<=3; "
          "exact small-torus ground energies")
    print("HIT: for records under exclusion (block 54 walk, block 78 compression), tr_K+ H_N^k - tr_K- H_N^k = (2/N!) "
          "sum_{pi odd} tr P_pi H_N^k is 0 for k<4 and at k=4 equals -8 n_p V 2^(N-2) C(V-4,N-2) on side>=5 tori (n_p = 1 "
          "on Z^2, 3 on Z^3): the pair plaquette exchange with the other corners empty; the three-record ring exchange is "
          "even (-3 per plaquette at order 4, both sectors), so a third record changes the sign term only through "
          "exclusion (connected +64/+192 per site at order 4, +1764/+8124 at order 6, H units); the first many-record odd "
          "process is the four-record ring exchange at order 6 (+78/+546 per site); every hop multiplies the coin by a "
          "quaternion unit, so for records starting on definite sites, any coins, block 55's source is the same in both "
          "sectors at all times for N=2,3 and first differs at N=4 (order t^5); ground energies: 3x3 torus antisymmetric "
          "lower at N=2,3,4 (N=2: -sqrt6), 4x4 torus equal at N=2 (-2 sqrt2) and N=3 (one root of a degree-48 polynomial)")
else:
    print("SUMMARY: ROUTE FAILS AT " + ",".join(t for t, ok in RES if not ok))
