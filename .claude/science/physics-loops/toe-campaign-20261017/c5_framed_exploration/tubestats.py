"""T-junction statistics with leg operators confined to tubes around straight segments (legs meet only near
the junction). gens: list of dicts {pos: labels}; pattern: list of (offset, gen index)."""
import itertools, numpy as np
from stats import build, solve, symp
def tube_sites(t, radius=1, junction=1):
    pts = set()
    n = max(abs(c) for c in t)
    for k in range(n + 1):
        c = tuple(round(k * t[i] / n) for i in range(3))
        for d in itertools.product(range(-radius, radius + 1), repeat=3):
            if sum(abs(x) for x in d) <= radius: pts.add(tuple(c[i] + d[i] for i in range(3)))
    return pts
def t_junction_tube(gens, q, pattern, legs, R=4, radius=1):
    sites, sidx, inst, M, nq = build(gens, q, R)
    iidx = {x: i for i, x in enumerate(inst)}
    T = []
    for t in legs:
        allowed = tube_sites(t, radius)
        cols = [q * sidx[p] + a for p in allowed if p in sidx for a in range(q)]
        colmask = np.zeros(nq, bool); colmask[cols] = True
        keep = np.concatenate([colmask, colmask])
        tgt = np.zeros(len(inst), np.uint8)
        for off, j in pattern:
            tgt[iidx[(tuple(off), j)]] ^= 1; tgt[iidx[(tuple(np.add(off, t)), j)]] ^= 1
        w = solve(M[:, keep], tgt)
        if w is None: return None, f'no tube leg to {t}'
        full = np.zeros(2 * nq, np.uint8); full[keep] = w; T.append(full)
    s = [symp(T[a], T[b], nq) for a, b in ((0, 1), (1, 2), (0, 2))]
    return (-1) ** sum(s), s
if __name__ == '__main__':
    X, Z = 1, 3
    A2 = {(0,0,0): (X, X), (-1,0,0): (X, 0), (0,-1,0): (0, X)}; B2 = {(0,0,0): (Z, Z), (0,1,0): (Z, 0), (1,0,0): (0, Z)}
    for legs in ([(3,0,0),(0,3,0),(-3,-3,0)], [(-3,0,0),(0,-3,0),(3,3,0)], [(3,0,0),(-3,0,0),(0,3,0)]):
        print('2D toric e', t_junction_tube([A2,B2], 2, [((0,0,0),0)], legs)[0], ' m', t_junction_tube([A2,B2], 2, [((0,0,0),1)], legs)[0],
              ' e x m', t_junction_tube([A2,B2], 2, [((0,0,0),0),((0,0,0),1)], legs)[0], ' legs', legs)
