"""Claims (1) and (2)."""
import itertools, time
from core import *

t0 = time.time()
# Claim 1 on L=4 torus (local check suffices by translation invariance; we check A's at origin vs all gens)
lat = Lattice(4)
bad1 = 0
for order in ORDERS:
    rk = rank_of_order(order)
    Bs, Ss = lat.gens(rk)
    vlist = list(lat.verts())
    for a in range(3):
        Ae = lat.A((1, 1, 1), a, rk)
        if any(lat.comm(Ae, s) for s in Ss):
            bad1 += 1
        anti = [vlist[i] for i, b in enumerate(Bs) if lat.comm(Ae, b)]
        w = [1, 1, 1]; w[a] += 1
        if sorted(anti) != sorted([(1, 1, 1), tuple(w)]):
            bad1 += 1
    # generators commute: S at origin-ish vs all gens (translation invariance)
    G = Bs + Ss
    loc = [lat.plaq((1, 1, 1), a, b, rk) for (a, b) in [(0, 1), (1, 2), (0, 2)]] + [lat.B((1, 1, 1))]
    if any(lat.comm(g, h) for g in loc for h in G):
        bad1 += 1
print('claim1 violations over 720 orders:', bad1, f'{time.time()-t0:.1f}s')

# Claim 2: L=10 torus, legs length 3 from origin o=(5,5,5)
t0 = time.time()
lat = Lattice(10)
o = (5, 5, 5)


def leg(d, rk):
    a, s = DIRS[d]
    p = 0
    for k in range(3):
        v = list(o)
        if s == 1:
            v[a] += k
        else:
            v[a] -= k + 1
        p ^= lat.A(tuple(v), a, rk)
    return p


def tj(rk):
    legs = [leg(d, rk) for d in range(6)]
    res = {}
    for tr in itertools.combinations(range(6), 3):
        i, j, k = tr
        s = lat.comm(legs[i], legs[j]) ^ lat.comm(legs[j], legs[k]) ^ lat.comm(legs[k], legs[i])
        res[tr] = -1 if s else 1
    return res, legs

# sanity: each leg violates B only at o and endpoint
rk0 = rank_of_order(ORDERS[0])
_, legs = tj(rk0)
for d in range(6):
    viol = [v for v in lat.verts() if lat.comm(legs[d], lat.B(v))]
    print('leg', DNAME[d], 'B-violations at', viol)
vals = set()
allneg = True
for order in ORDERS:
    res, _ = tj(rank_of_order(order))
    vals |= set(res.values())
    if any(x != -1 for x in res.values()):
        allneg = False
print('twisted: all 20 triples = -1 for all 720 orders:', allneg, 'values seen', vals)
res, _ = tj(None)
print('toric code values:', set(res.values()))
print(f'{time.time()-t0:.1f}s')
