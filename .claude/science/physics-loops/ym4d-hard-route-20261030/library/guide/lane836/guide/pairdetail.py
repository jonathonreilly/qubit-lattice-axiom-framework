"""GUIDE only: per-event optimal F for the pair block at x = 0.096 (beta 0.384)."""
import itertools
import numpy as np
from blockwalk import links_at, plaquettes_of, plaq_links, admissible, E, add, ends
from blockwalk2 import setup
o = (0,0,0,0); Q = [o, E[0]]
Qs, B, events, plist, Fs = setup(Q)
x = 0.0960
def resp(F, P):
    free = [l for l in B if l not in F]
    idx = {l: k for k, l in enumerate(free)}
    n = len(free)
    C = np.zeros((n, n))
    for p in plist:
        fl = [idx[m] for m in plaq_links(p) if m in idx]
        for c in fl:
            for d in fl:
                if c != d: C[c, d] += x
    col = np.linalg.inv(np.eye(n) - C).sum(axis=0)
    return sum(x * col[idx[m]] for p in P for m in plaq_links(p) if m in idx)
def classify(j, P):
    # number of block links in each changed plaquette, and direction of j relative to e_0
    ks = sorted(len([m for m in plaq_links(p) if m in B]) for p in P)
    return (j[1] == 0, tuple(ks))
types = {}
for j, P in events.items():
    best = min((resp(F, P), sorted(F)) for F in Fs)
    t = classify(j, P)
    types.setdefault(t, []).append(best[0])
tot = 0
for t, v in sorted(types.items()):
    print(t, len(v), "resp min/max %.4f %.4f" % (min(v), max(v)))
    tot += sum(v)
print("total", tot, "|B|", len(B), "alpha", tot/len(B))
