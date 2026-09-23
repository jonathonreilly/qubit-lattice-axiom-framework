#!/usr/bin/env python3
"""J:derive:uniqueness-up-2:a2 - checks for ATTEMPT.md (same directory).

Objects of blocks 08 and 28 as restated in round 1 (probes/work/derive/uniqueness-region-up/w-jonathonsmac4f50-j1ba5):
menu M = {+-e1,+-e2,+-e3} (index 2k = +e_(k+1), 2k+1 = -e_(k+1)), phi = p, 1, 2 for equal, antipodal, orthogonal; level
automaton r(s|a1,a2,a3) = prod phi(s,a_j)/Z; ground metric rho = 1 (orthogonal), alpha (antipodal); W = W_rho.
Criterion (ATTEMPT.md steps 1-6): the two-level contraction with group-consistent environments,
K2c = sum over the six grand-predecessor positions z of kappa2c(z) < 1, where kappa2c(z) is the largest averaged
two-level sensitivity (switch at z, exact propagation over two levels) over environments whose laws come from ONE
configuration of the level below within each of the two groups (sites before / after z in the lexicographic order).
Exact: Fractions for every law, plan, W and table entry; the maximisation over realisable environments is done in
integers with every rounding upward (tables x 2^34, laws x 2^24), so each printed kappa2c is a rigorous upper bound.
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np

FAILS = []
T0 = time.time()


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg, flush=True)
    if not good:
        FAILS.append(tag)


S1, S2 = 34, 24


def ceil_scaled(x, s):
    return -((-(x.numerator << s)) // x.denominator)


class Model:
    def __init__(self, p, alpha):
        self.p, self.alpha = Fr(p), Fr(alpha)
        self.phi = [[self.p if s == a else (Fr(1) if s == a ^ 1 else Fr(2)) for a in range(6)] for s in range(6)]
        self._law = {}

    def law(self, a, b, c):
        key = tuple(sorted((a, b, c)))
        if key not in self._law:
            w = [self.phi[s][a] * self.phi[s][b] * self.phi[s][c] for s in range(6)]
            t = sum(w)
            self._law[key] = tuple(x / t for x in w)
        return self._law[key]

    def rho(self, i, j):
        return Fr(0) if i == j else (self.alpha if i == j ^ 1 else Fr(1))

    def W(self, mu, nu):
        e = [max(m - n, Fr(0)) for m, n in zip(mu, nu)]
        d = [max(n - m, Fr(0)) for m, n in zip(mu, nu)]
        tv = sum(e)
        return tv + (self.alpha - 1) * max([Fr(0)] + [e[i] + d[i ^ 1] - tv for i in range(6)])

    def plan(self, mu, nu):
        """the equivariant rho-optimal plan of ATTEMPT.md step 1"""
        pi = {}
        m = [min(a, b) for a, b in zip(mu, nu)]
        for i in range(6):
            if m[i]:
                pi[i, i] = m[i]
        e = [a - x for a, x in zip(mu, m)]
        d = [b - x for b, x in zip(nu, m)]
        tv = sum(e)
        if tv == 0:
            return pi
        crit = [e[i] + d[i ^ 1] - tv for i in range(6)]
        A = max(crit)
        if A > 0:
            i0 = crit.index(A)
            assert sum(1 for c in crit if c > 0) == 1
            pi[i0, i0 ^ 1] = A
            e[i0] -= A
            d[i0 ^ 1] -= A
        E = [e[0] + e[1], e[2] + e[3], e[4] + e[5]]
        D = [d[0] + d[1], d[2] + d[3], d[4] + d[5]]
        if sum(E) == 0:
            return pi
        lo = max(Fr(0), D[1] - E[2], D[0] + D[1] - E[1] - E[2])
        hi = min(E[0], D[1], D[0] + D[1] - E[2])
        assert lo <= hi
        s = (lo + hi) / 2
        F = {(0, 1): s, (0, 2): E[0] - s, (2, 1): D[1] - s, (2, 0): E[2] - D[1] + s,
             (1, 0): D[0] - E[2] + D[1] - s, (1, 2): E[1] - D[0] + E[2] - D[1] + s}
        for i in range(6):
            for j in range(6):
                k, l = i // 2, j // 2
                if k != l and E[k] and D[l] and e[i] and d[j]:
                    pi[i, j] = pi.get((i, j), 0) + F[k, l] * e[i] / E[k] * d[j] / D[l]
        return pi

    def certify_plan(self, mu, nu, pi):
        """marginals, nonnegativity, and a 1-Lipschitz dual witness f with sum f(mu - nu) = cost: pi optimal, cost = W"""
        rows = [sum(v for (i, j), v in pi.items() if i == r) for r in range(6)]
        cols = [sum(v for (i, j), v in pi.items() if j == c) for c in range(6)]
        cost = sum(v * self.rho(i, j) for (i, j), v in pi.items())
        e = [max(m - n, Fr(0)) for m, n in zip(mu, nu)]
        d = [max(n - m, Fr(0)) for m, n in zip(mu, nu)]
        tv = sum(e)
        crit = [e[i] + d[i ^ 1] - tv for i in range(6)]
        if max(crit) > 0:
            i0 = crit.index(max(crit))
            f = [Fr(1) if not d[i] else self.alpha - 1 for i in range(6)]
            f[i0], f[i0 ^ 1] = self.alpha, Fr(0)
        else:
            f = [Fr(0) if d[i] else Fr(1) for i in range(6)]
        lip = all(abs(f[i] - f[j]) <= self.rho(i, j) for i in range(6) for j in range(6))
        dual = sum(f[i] * (mu[i] - nu[i]) for i in range(6))
        return (rows == list(mu) and cols == list(nu) and min(pi.values()) >= 0 and lip and dual == cost
                and cost == self.W(mu, nu))

    def tables(self, w, w2):
        """exact two-level single-switch tables: Fd (corner position, env order (ij, ik, jj, jk, kk)) and
        Fs (edge position, env order (ii, ik, jj, jk, kk)); see ATTEMPT.md step 4"""
        L, W = self.law, self.W
        Wd = {k: W(L(k[0], k[2], k[3]), L(k[1], k[2], k[3])) for k in itertools.product(range(6), repeat=4)}
        Fd = np.empty((6,) * 5, dtype=object)
        plans = []
        for u12, u13 in itertools.product(range(6), repeat=2):
            mu, nu = L(w, u12, u13), L(w2, u12, u13)
            g = self.plan(mu, nu)
            plans.append((mu, nu, g))
            G = [[sum(v * Wd[a1, b1, a2, a3] for (a1, b1), v in g.items()) for a3 in range(6)] for a2 in range(6)]
            for ud2, u23, ud3 in itertools.product(range(6), repeat=3):
                l2, l3 = L(u12, ud2, u23), L(u13, u23, ud3)
                Fd[u12, u13, ud2, u23, ud3] = sum(l2[a2] * l3[a3] * G[a2][a3] for a2 in range(6) for a3 in range(6))
        Fs = np.empty((6,) * 5, dtype=object)
        g1 = {xy: self.plan(L(xy[0], w, xy[1]), L(xy[0], w2, xy[1])) for xy in itertools.product(range(6), repeat=2)}
        g2 = {xy: self.plan(L(w, xy[0], xy[1]), L(w2, xy[0], xy[1])) for xy in itertools.product(range(6), repeat=2)}
        Wc = {}
        for u11, u13, u22, u23 in itertools.product(range(6), repeat=4):
            H = [Fr(0)] * 6
            for (a1, b1), v1 in g1[u11, u13].items():
                for (a2, b2), v2 in g2[u22, u23].items():
                    for a3 in range(6):
                        k = (a1, b1, a2, b2, a3)
                        if k not in Wc:
                            Wc[k] = W(L(a1, a2, a3), L(b1, b2, a3))
                        H[a3] += v1 * v2 * Wc[k]
            for u33 in range(6):
                l3 = L(u13, u23, u33)
                Fs[u11, u13, u22, u23, u33] = sum(H[a3] * l3[a3] for a3 in range(6))
        return Fd, Fs, plans


def signed_perms():
    out = []
    for sig in itertools.permutations(range(3)):
        for flips in itertools.product((0, 1), repeat=3):
            out.append([2 * sig[i // 2] + ((i % 2) ^ flips[i // 2]) for i in range(6)])
    return out


combos = list(itertools.combinations_with_replacement(range(6), 3))
cidx = {c: i for i, c in enumerate(combos)}


def P(site2):
    return [''.join(sorted(site2 + k)) for k in '123']


def group_tuples(sites):
    """all tuples (pattern multiset index per site) realised by ONE configuration of the level below on the union
    of the sites' predecessors (exhaustive enumeration)"""
    if not sites:
        return np.zeros((1, 0), dtype=np.int64), 0
    R = sorted(set(s for z in sites for s in P(z)))
    pos = {s: i for i, s in enumerate(R)}
    preds = [[pos[s] for s in P(z)] for z in sites]
    n = len(R)
    lut = np.zeros((6, 6, 6), dtype=np.int16)
    for a, b, c in itertools.product(range(6), repeat=3):
        lut[a, b, c] = cidx[tuple(sorted((a, b, c)))]
    rest = np.indices((6,) * (n - 2), dtype=np.int8).reshape(n - 2, -1).T
    found = []
    for v0, v1 in itertools.product(range(6), repeat=2):
        grid = np.concatenate([np.full((len(rest), 1), v0, np.int8), np.full((len(rest), 1), v1, np.int8), rest], 1)
        cols = np.stack([lut[grid[:, q[0]], grid[:, q[1]], grid[:, q[2]]] for q in preds], 1)
        found.append(np.unique(cols, axis=0))
    return np.unique(np.concatenate(found), axis=0).astype(np.int64), n


def int_trie(G, S, Lup):
    """G int64 (m, 6..6) with k trailing group axes, S (n, k) tuples; upward-rounded contraction -> (n, m)"""
    k = S.shape[1]
    S = S[np.lexsort(S.T[::-1])]
    cur = G[None]
    parent = np.zeros(len(S), dtype=np.int64)
    for j in range(k):
        pref, inv = np.unique(S[:, :j + 1], axis=0, return_inverse=True)
        inv = inv.ravel()
        first = np.zeros(len(pref), dtype=np.int64)
        first[inv[::-1]] = np.arange(len(S))[::-1]
        tot = np.einsum('pa,pma...->pm...', Lup[pref[:, j]], cur[parent[first]])
        cur = (tot + ((1 << S2) - 1)) >> S2
        parent = inv
    return cur[parent]


def position_max(Fup, tmpl, before, after, Lup, cache):
    for g in (tuple(before), tuple(after)):
        if g not in cache:
            cache[g] = group_tuples(list(g))[0]
    SB, SA = cache[tuple(before)], cache[tuple(after)]
    Fp = np.transpose(Fup, [tmpl.index(s) for s in before + after])
    nb, na = len(before), len(after)
    if nb == 0:
        return int(int_trie(Fp[None], SA, Lup).max())
    if na == 0:
        return int(int_trie(Fp[None], SB, Lup).max())
    Fb = np.ascontiguousarray(np.transpose(Fp, list(range(nb, nb + na)) + list(range(nb))))
    vals = int_trie(Fb.reshape((6 ** na,) + (6,) * nb), SB, Lup)
    best = 0
    for s in range(0, len(vals), 256):
        best = max(best, int(int_trie(vals[s:s + 256].reshape((-1,) + (6,) * na), SA, Lup).max()))
    return best


ORDER = ['11', '12', '13', '22', '23', '33']          # lexicographic order of the six positions (ATTEMPT step 5)
TEMPLATES = {'11': ('d', ['12', '13', '22', '23', '33']), '22': ('d', ['12', '23', '11', '13', '33']),
             '33': ('d', ['13', '23', '11', '12', '22']), '12': ('s', ['11', '13', '22', '23', '33']),
             '13': ('s', ['11', '12', '33', '23', '22']), '23': ('s', ['22', '12', '33', '13', '11'])}


def certify(p, alpha, cache, detail=False):
    M = Model(p, alpha)
    Lup = np.array([[ceil_scaled(x, S2) for x in M.law(*c)] for c in combos], dtype=np.int64)
    kap = {z: Fr(0) for z in ORDER}
    nplan, plans_ok = 0, True
    for (w, w2) in ((0, 1), (0, 2)):
        Fd, Fs, plans = M.tables(w, w2)
        for mu, nu, g in plans:
            plans_ok &= M.certify_plan(mu, nu, g)
            nplan += 1
        up = np.vectorize(lambda x: ceil_scaled(x, S1), otypes=[object])
        Fdu, Fsu = up(Fd).astype(np.int64), up(Fs).astype(np.int64)
        for i, z in enumerate(ORDER):
            kind, tmpl = TEMPLATES[z]
            m = position_max(Fdu if kind == 'd' else Fsu, tmpl, ORDER[:i], ORDER[i + 1:], Lup, cache)
            kap[z] = max(kap[z], Fr(m, 1 << S1) / M.rho(w, w2))
    return sum(kap.values()), kap, nplan, plans_ok, M


# ---------------------------------------------------------------- A1: W, the plan, round 1's constant reproduced
M1 = Model(Fr(51, 10), Fr(5, 4))
A = [M1.law(*c) for c in combos]
best = Fr(0)
for (w, w2) in ((0, 1), (0, 2)):
    K = [[M1.W(M1.law(w, u1, u2), M1.law(w2, u1, u2)) / M1.rho(w, w2) for u2 in range(6)] for u1 in range(6)]
    for l1 in A:
        v1 = [sum(l1[u1] * K[u1][u2] for u1 in range(6)) for u2 in range(6)]
        for l2 in A:
            best = max(best, sum(v1[u2] * l2[u2] for u2 in range(6)))
r1 = Fr(52187574259076840991934694, 156963184970376094931272779)
rng_ok, nrand = True, 0
Mr = Model(Fr(27, 5), Fr(27, 20))
for a in itertools.product(range(6), repeat=3):
    for b in itertools.product(range(6), repeat=3):
        if sum(a) % 7 == 0 and sum(b) % 5 == 1:
            mu, nu = Mr.law(*a), Mr.law(*b)
            rng_ok &= Mr.certify_plan(mu, nu, Mr.plan(mu, nu))
            nrand += 1
ok("A1", best == r1 and rng_ok,
   f"round 1's exact constant reproduced (kappa_bar at p = 51/10, alpha = 5/4 equals its 52187574259076840991934694/"
   f"156963184970376094931272779); W = TV + (alpha-1) max_i(e_i + d_-i - TV)+ and the equivariant plan (step 1) is a "
   f"coupling of cost W with a 1-Lipschitz dual witness of equal value on {nrand} pairs of laws (so it is optimal)")

# ---------------------------------------------------------------- A2: equivariance of the plan (the two types suffice)
G48 = signed_perms()
eq_ok, neq = True, 0
for (w, w2) in ((0, 1), (0, 2)):
    for u, v in itertools.combinations_with_replacement(range(6), 2):
        mu, nu = Mr.law(w, u, v), Mr.law(w2, u, v)
        base = Mr.plan(mu, nu)
        for g in G48:
            gmu, gnu = Mr.law(g[w], g[u], g[v]), Mr.law(g[w2], g[u], g[v])
            direct = Mr.plan(gmu, gnu)
            moved = {(g[i], g[j]): val for (i, j), val in base.items()}
            eq_ok &= direct == moved and all(gmu[g[i]] == mu[i] for i in range(6))
            neq += 1
ok("A2", eq_ok and len({tuple(g) for g in G48}) == 48,
   f"the plan commutes with all 48 signed permutations on every pair used ({neq} checks), laws are equivariant, so "
   f"each maximum over ordered pairs (w, w') is attained at (+x,-x) or (+x,+y)")

# ---------------------------------------------------------------- A3: realisable environments
cache = {}
sizes = []
for i in range(len(ORDER)):
    for grp in (ORDER[:i], ORDER[i + 1:]):
        if tuple(grp) not in cache:
            cache[tuple(grp)], n = group_tuples(list(grp))
        sizes.append(len(cache[tuple(grp)]))
full = cache[tuple(ORDER[1:])]
ok("A3", len(full) < 56 ** 5 and min(sizes) >= 1,
   f"group environments enumerated exhaustively (one configuration of the level below per group): the five-site group "
   f"after the first position realises {len(full)} of the 56^5 = {56 ** 5} law tuples")

# ---------------------------------------------------------------- A4: certificates
PLIST = [(Fr(s), Fr(a)) for s, a in (x.split(':') for x in (sys.argv[1] if len(sys.argv) > 1 else
         '51/10:27/20,21/4:27/20,27/5:27/20,11/2:27/20,111/20:27/20,139/25:34/25').split(','))]
rows, cert_ok, top = [], True, None
for p, a in PLIST:
    K, kap, nplan, pok, M = certify(p, a, cache)
    rows.append(f"p = {p} (alpha {a}): K2c <= {float(K):.6f}")
    cert_ok &= K < 1 and pok
    top = (p, a, K, kap, M) if K < 1 and (top is None or p > top[0]) else top
ok("A4", cert_ok,
   "exact certificates, every plan certified optimal, maxima in upward-rounded integers: " + "; ".join(rows)
   + (f"; at p = {top[0]} the six positions give " + ", ".join(f"{z}: {float(v):.5f}" for z, v in top[3].items())
      if top else "") + f" ({time.time() - T0:.0f} s)")

# ---------------------------------------------------------------- A5: the constants for the first levels
M = top[4] if top else M
kmax = max(M.W(M.law(w, u1, u2), M.law(w2, u1, u2)) / M.rho(w, w2)
           for (w, w2) in ((0, 1), (0, 2)) for u1 in range(6) for u2 in range(6))
ok("A5", 0 < kmax < 1, f"at p = {top[0] if top else '-'}: kappa_max = {float(kmax):.5f}, so D_1 <= 3 kappa_max D_0 and "
   f"D_2k <= 3 kappa_max D_(2k-1); with K2c < 1, D_t <= alpha max(1, 3 kappa_max)^2 K2c^floor((t-1)/2)")

label = 'PARTIAL' if not FAILS else 'PARTIAL (failed: ' + ', '.join(FAILS) + ')'
print(f"SUMMARY: {label} exact certificates of uniqueness and exponential memory loss for the six-axis formation law "
      f"on (p,1,2) up to p = {top[0] if top else '-'} (round 1: 5.1; a3: 5.26) by a two-level Wasserstein contraction: "
      "optimal couplings on odd levels, glued couplings on even levels, switch one grand-predecessor, propagate two "
      "levels exactly, average the environment over the level below with each order-group's laws drawn from one "
      "configuration; the located threshold 10.5 is not reached")
if not FAILS and top:
    print(f"HIT: the level automaton of the six-axis formation law on (p,1,2) has exactly one invariant law and forgets "
          f"every initial plane exponentially at p = {top[0]} (alpha = {top[1]}), and at each p of the table: the "
          f"two-level constant K2c (sum over the six grand-predecessors of the averaged two-level sensitivity with "
          f"group-consistent environments) is <= {float(top[2]):.6f} < 1 there, an exact upper bound; the one-level "
          "criteria stop at 5.11 (round 1) and 5.26 (a3)")
