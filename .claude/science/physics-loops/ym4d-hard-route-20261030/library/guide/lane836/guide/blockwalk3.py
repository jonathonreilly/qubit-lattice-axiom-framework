"""GUIDE only (row 836): heuristic fixing sets F = (spanning tree of Q) + (one outward link),
to explore larger Q-blocks.  Lower bounds on the method threshold (heuristic F)."""
import itertools, sys
import numpy as np
from blockwalk import links_at, plaquettes_of, plaq_links, admissible, E, add, ends

def bfs_trees(Q, orders):
    Q = list(Q); Qs = set(Q)
    trees = []
    for r in Q:
        for order in orders:
            seen = {r}; T = []; frontier = [r]
            while frontier:
                nxt = []
                for u in frontier:
                    for i in order:
                        for s in (+1, -1):
                            w = add(u, tuple(s * x for x in E[i]))
                            if w in Qs and w not in seen:
                                seen.add(w)
                                T.append((u, i) if s > 0 else (w, i))
                                nxt.append(w)
                frontier = nxt
            trees.append(frozenset(T))
    return list(set(trees))

def setup(Q):
    Qs = set(Q)
    B = sorted({l for v in Qs for l in links_at(v)})
    internal = [l for l in B if all(u in Qs for u in ends(l))]
    outward = [l for l in B if l not in internal]
    events = {}
    plist = set()
    for l in B:
        for p in plaquettes_of(l):
            plist.add(p)
            for m in plaq_links(p):
                if m not in B:
                    events.setdefault(m, set()).add(p)
    orders = [(0,1,2,3), (3,2,1,0), (1,3,0,2)]
    Fs = []
    for T in bfs_trees(Q, orders):
        for o in outward:
            F = set(T) | {o}
            if admissible(F, Qs):
                Fs.append(F)
    return B, events, sorted(plist), Fs

def total_resp(B, events, plist, Fs, x):
    best = {j: np.inf for j in events}
    for F in Fs:
        free = [l for l in B if l not in F]
        idx = {l: k for k, l in enumerate(free)}
        n = len(free)
        C = np.zeros((n, n))
        for p in plist:
            fl = [idx[m] for m in plaq_links(p) if m in idx]
            for c in fl:
                for d in fl:
                    if c != d:
                        C[c, d] += x
        if np.max(np.abs(np.linalg.eigvalsh((C + C.T) / 2))) >= 1:
            continue
        colsum = np.linalg.inv(np.eye(n) - C).sum(axis=0)
        for j, P in events.items():
            r = sum(x * colsum[idx[m]] for p in P for m in plaq_links(p) if m in idx)
            if r < best[j]:
                best[j] = r
    return sum(best.values())

def threshold(Q, lo=0.0, hi=0.2, it=22):
    B, events, plist, Fs = setup(Q)
    for _ in range(it):
        mid = (lo + hi) / 2
        if total_resp(B, events, plist, Fs, mid) < len(B):
            lo = mid
        else:
            hi = mid
    return 4 * lo, len(B), len(events), len(Fs)

if __name__ == "__main__":
    o = (0, 0, 0, 0)
    def box(sides):
        return [tuple(c) for c in itertools.product(*[range(s) for s in sides])]
    shapes = {"plaq(heur)": box((2,2,1,1)), "cube3": box((2,2,2,1)), "line5": box((5,1,1,1)),
              "rect3x2": box((3,2,1,1)), "sq3": box((3,3,1,1)), "hyper2": box((2,2,2,2))}
    sel = sys.argv[1:] or list(shapes)
    for name in sel:
        print(name, *threshold(shapes[name]), flush=True)
