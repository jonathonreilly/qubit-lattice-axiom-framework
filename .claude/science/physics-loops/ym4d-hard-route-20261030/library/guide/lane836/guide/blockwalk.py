"""GUIDE only (row 836). Walk-sum thresholds for gauge-fixed Q-blocks.

Block B(Q) = all links of Z^4 touching the vertex set Q.  For each exterior
event (a link j outside B sharing a plaquette with B), choose an admissible
gauge-fixing set F (links of B set to 1 by gauge rotations at vertices of Q),
compute the Dobrushin walk sum of the response, and sum over events.
Condition for a lattice-symmetric family: sum_events resp(x) < |B|.
Decides nothing.
"""
import itertools, sys
import numpy as np

D = 4
E = [tuple(1 if k == i else 0 for k in range(D)) for i in range(D)]

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def link(v, i):            # positively oriented link (base, direction)
    return (v, i)

def links_at(v):
    out = []
    for i in range(D):
        out.append((v, i))                                  # v -> v+e_i
        out.append((add(v, tuple(-x for x in E[i])), i))    # v-e_i -> v
    return out

def ends(l):
    v, i = l
    return v, add(v, E[i])

def plaquettes_of(l):
    v, i = l
    ps = []
    for j in range(D):
        if j == i:
            continue
        for s in (+1, -1):
            w = add(v, tuple(s * x for x in E[j])) if s < 0 else v
            # plaquette with base w in plane (i,j): links (w,i),(w+e_i,j),(w+e_j,i),(w,j)
            a, b = (i, j) if i < j else (j, i)
            ps.append((w, a, b))
    return ps

def plaq_links(p):
    w, a, b = p
    return [(w, a), (add(w, E[a]), b), (add(w, E[b]), a), (w, b)]

def admissible(F, Q):
    # F: set of links; each component of (vertices, F) is a tree with at most
    # one vertex outside Q.
    parent = {}
    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for l in F:
        u, w = ends(l)
        ru, rw = find(u), find(w)
        if ru == rw:
            return False
        parent[ru] = rw
    comp_out = {}
    for l in F:
        for u in ends(l):
            r = find(u)
            comp_out.setdefault(r, set())
            if u not in Q:
                comp_out[r].add(u)
    return all(len(s) <= 1 for s in comp_out.values())

def analyse(Q, Fchoices, x):
    Q = set(Q)
    B = set()
    for v in Q:
        for l in links_at(v):
            B.add(l)
    B = sorted(B)
    events = {}
    for l in B:
        for p in plaquettes_of(l):
            for m in plaq_links(p):
                if m not in B:
                    events.setdefault(m, set()).add(p)
    total = 0.0
    for j, P in events.items():
        best = None
        for F in Fchoices:
            free = [l for l in B if l not in F]
            idx = {l: k for k, l in enumerate(free)}
            n = len(free)
            C = np.zeros((n, n))
            seen = set()
            for l in B:
                for p in plaquettes_of(l):
                    if p in seen:
                        continue
                    seen.add(p)
                    fl = [m for m in plaq_links(p) if m in idx]
                    for c in fl:
                        for d in fl:
                            if c != d:
                                C[idx[c], idx[d]] += x
            b = np.zeros(n)
            for p in P:
                fl = [m for m in plaq_links(p) if m in idx]
                for c in fl:
                    b[idx[c]] += x
            if np.max(np.abs(np.linalg.eigvals(C))) >= 1:
                resp = np.inf
            else:
                resp = np.linalg.solve(np.eye(n) - C, b).sum()
            if best is None or resp < best:
                best = resp
        total += best
    return total, len(B), len(events)

def fchoices(Q, maxsize=None):
    Q = set(Q)
    B = set()
    for v in Q:
        for l in links_at(v):
            B.add(l)
    B = sorted(B)
    k = len(Q)
    out = []
    for F in itertools.combinations(B, k):
        if admissible(F, Q):
            out.append(set(F))
    return out

def threshold(Q, lo=0.0, hi=0.25, it=40):
    Fs = fchoices(Q)
    for _ in range(it):
        mid = (lo + hi) / 2
        tot, nB, ne = analyse(Q, Fs, mid)
        if tot < nB:
            lo = mid
        else:
            hi = mid
    return 4 * lo, nB, ne, len(Fs)

if __name__ == "__main__":
    o = (0, 0, 0, 0)
    shapes = {
        "star": [o],
        "pair": [o, E[0]],
    }
    if len(sys.argv) > 1 and sys.argv[1] == "big":
        shapes["line3"] = [o, E[0], add(E[0], E[0])]
        shapes["plaq"] = [o, E[0], E[1], add(E[0], E[1])]
    for name, Q in shapes.items():
        b, nB, ne, nF = threshold(Q)
        print(name, "beta_threshold=%.5f" % b, "|B|=", nB, "events=", ne, "Fchoices=", nF)
    # exact star formula
    xs = (37 ** 0.5 - 5) / 12
    print("star exact (sqrt37-5)/3 =", 4 * xs)
