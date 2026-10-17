"""Item 2: pair test with own creators (many q, many paths), under the corrected U.

lambda defined by  S^dag (U S U^dag) = lambda * g,  g in the stabilizer group (+1 on the code space).
Then U S|psi> = lambda S U|psi> for every code state psi: a relative eigenvalue, independent of how
U acts on the 8-dimensional logical space.
"""
import sys, time, pickle, random
import numpy as np
from ccode import CornerCode, StabGroup, pmul, pdag, commute
from geom import rotations, classify, w1, rot_vec, CTYPES, add
from rot import Op

L = 4
import os; SEED = os.environ.get("SEED"); C = CornerCode(L, ordering_seed=None if SEED is None else int(SEED))
Ms = rotations()
d = pickle.load(open(f'U_L{L}' + ('' if SEED is None else '_s' + SEED) + '.pkl', 'rb'))
Uc = [Op(*t) for t in d['Uc']]
gens = C.generators()
G = StabGroup(C.nq)
for g in gens:
    G.add(g[2])
lat = C.lat


def rot_uc(M, node):
    v, ct = node
    return (rot_vec(M, v), frozenset(rot_vec(M, x) for x in ct))


def nbr_uc(node, box):
    v, ct = node
    out = []
    for (v2, ct2, kind) in lat.neighbours(v, ct):
        if all(-box <= a <= box for a in v2):
            out.append((v2, frozenset(ct2)))
    return out


def rand_path(a, b, box, rng, detour=True):
    """random path a->b in unwrapped box via random-weight Dijkstra (optionally through a random waypoint)."""
    import heapq
    def dij(s, t):
        w = {}
        dist = {s: 0.0}
        prev = {}
        pq = [(0.0, s)]
        while pq:
            dd, u = heapq.heappop(pq)
            if u == t:
                break
            if dd > dist[u]:
                continue
            for x in nbr_uc(u, box):
                key = (u, x)
                if key not in w:
                    w[key] = rng.random() + 0.05
                nd = dd + w[key]
                if nd < dist.get(x, 1e18):
                    dist[x] = nd
                    prev[x] = u
                    heapq.heappush(pq, (nd, x))
        path = [t]
        while path[-1] != s:
            path.append(prev[path[-1]])
        return path[::-1]
    if detour:
        allnodes = [((x, y, z), ct) for x in range(-box, box + 1) for y in range(-box, box + 1)
                    for z in range(-box, box + 1) for ct in CTYPES]
        mid = rng.choice(allnodes)
        p1 = dij(a, mid)
        p2 = dij(mid, b)
        return p1 + p2[1:]
    return dij(a, b)


def cid(node):
    return lat.corner(node[0], node[1])


def string(path):
    S = (0, 0, 0)
    for i in range(len(path) - 1):
        S = pmul(S, C.hop(cid(path[i]), cid(path[i + 1])))
    return S


Bgens = {g[1]: g[2] for g in gens if g[0] == 'B'}
other = [g for g in gens if g[0] != 'B']


def syndrome_ok(S, q1, q2):
    for c, B in Bgens.items():
        want = c in (q1, q2) and q1 != q2
        if commute(S, B) == want:
            return False
    return all(commute(S, g[2]) for g in other)


def main():
    rng = random.Random(12345)
    box = 1
    C2s = [i for i, M in enumerate(Ms) if classify(M) in ('C2axis', 'C2edge')]
    results = {}
    nclean = 0
    ntests = 0
    for gi in C2s:
        M = Ms[gi]
        typ = classify(M)
        lams = []
        # choose q's: various sites in the box, not fixed by R
        cand = [((x, y, z), ct) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for ct in CTYPES]
        cand = [q for q in cand if rot_uc(M, q) != q]
        qs = rng.sample(cand, 6)
        # include an on-site pair at the origin site
        qs.append(next(q for q in cand if q[0] == (0, 0, 0)))
        for q in qs:
            Rq = rot_uc(M, q)
            for t in range(4):
                path = rand_path(q, Rq, box, rng, detour=(t > 0))
                S = string(path)
                ntests += 1
                if syndrome_ok(S, cid(q), cid(Rq)):
                    nclean += 1
                SR = Uc[gi].conj(S)
                Mx = pmul(pdag(S), SR)
                lam = G.member_sign(Mx)
                lams.append(lam)
        results[gi] = (typ, w1(M), sorted(set(lams), key=str), len(lams))
        print(typ, 'w1 =', w1(M), 'axis/matrix', M.tolist(), 'lambda_U values', set(lams),
              'twisted lambda_V =', {(l * (-1) ** w1(M)) for l in lams if l is not None})
    print('clean creators (flip exactly B_q, B_Rq, nothing else):', nclean, '/', ntests)
    # control: S = (noncontractible loop along axis a at q) * (short path q->Rq)
    print('--- control: creators carrying a winding loop ---')
    import heapq
    def dij(s0, t, lo, hi):
        dist = {s0: 0}; prev = {}; pq = [(0, s0)]
        while pq:
            dd, u = heapq.heappop(pq)
            if u == t: break
            if dd > dist[u]: continue
            v, ct = u
            for (v2, ct2, kind) in lat.neighbours(v, ct):
                if all(lo <= a <= hi for a in v2):
                    x = (v2, frozenset(ct2))
                    if dd + 1 < dist.get(x, 1e9):
                        dist[x] = dd + 1; prev[x] = u; heapq.heappush(pq, (dd + 1, x))
        path = [t]
        while path[-1] != s0: path.append(prev[path[-1]])
        return path[::-1]
    for gi in C2s:
        M = Ms[gi]
        typ = classify(M)
        q = ((0, 0, 0), frozenset([(1, 0, 0), (0, 1, 0)]))
        if rot_uc(M, q) == q:
            q = ((0, 0, 0), frozenset([(1, 0, 0), (0, 0, 1)]))
        Rq = rot_uc(M, q)
        out = []
        for ax in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            qa = (tuple(L * t for t in ax), q[1])
            wind = dij(q, qa, -1, L + 1)
            tail = dij(q, Rq, -1, 1)
            S = pmul(string(wind), string(tail))
            SR = Uc[gi].conj(S)
            lam = G.member_sign(pmul(pdag(S), SR))
            out.append((ax, lam))
        print(typ, M.tolist(), out)


if __name__ == '__main__':
    main()
