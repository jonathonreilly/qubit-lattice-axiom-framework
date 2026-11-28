"""GUIDE only (row 836): faster walk-sum thresholds, per-F inverse reused across events."""
import itertools, sys
import numpy as np
from blockwalk import links_at, plaquettes_of, plaq_links, admissible, E, add

def setup(Q):
    Q = set(Q)
    B = sorted({l for v in Q for l in links_at(v)})
    events = {}
    plist = set()
    for l in B:
        for p in plaquettes_of(l):
            plist.add(p)
            for m in plaq_links(p):
                if m not in B:
                    events.setdefault(m, set()).add(p)
    Fs = [set(F) for F in itertools.combinations(B, len(Q)) if admissible(F, Q)]
    return Q, B, events, sorted(plist), Fs

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
        if np.max(np.abs(np.linalg.eigvals(C))) >= 1:
            continue
        Minv = np.linalg.inv(np.eye(n) - C)
        colsum = Minv.sum(axis=0)
        for j, P in events.items():
            r = 0.0
            for p in P:
                for m in plaq_links(p):
                    if m in idx:
                        r += x * colsum[idx[m]]
            if r < best[j]:
                best[j] = r
    return sum(best.values())

def threshold(Q, lo=0.0, hi=0.25, it=30):
    Q, B, events, plist, Fs = setup(Q)
    for _ in range(it):
        mid = (lo + hi) / 2
        if total_resp(B, events, plist, Fs, mid) < len(B):
            lo = mid
        else:
            hi = mid
    return 4 * lo, len(B), len(events), len(Fs)

if __name__ == "__main__":
    o = (0, 0, 0, 0)
    shapes = {"star": [o], "pair": [o, E[0]], "line3": [o, E[0], add(E[0], E[0])],
              "Lshape": [o, E[0], E[1]]}
    if len(sys.argv) > 1:
        shapes = {"plaq": [o, E[0], E[1], add(E[0], E[1])], "line4": [o, E[0], add(E[0],E[0]), add(add(E[0],E[0]),E[0])]}
    for name, Q in shapes.items():
        print(name, *threshold(Q), flush=True)
