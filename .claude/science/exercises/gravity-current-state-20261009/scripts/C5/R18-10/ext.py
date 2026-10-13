"""R18-10 declared second move family (METHOD: used because the first fragments): pattern 'hops' P xor (P + e_d),
d = x, y, z, for each of R18-1's 4 patterns (12 extra local patterns), plus the originals. Same dN = 0 filter."""
import numpy as np
from common import PATTERNS, G_entries
def ext_patterns():
    out = [list(p) for p in PATTERNS]
    for p in PATTERNS:
        for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            cnt = {}
            for (o, t) in p:
                for sh in [(0, 0, 0), d]:
                    key = (tuple(int(o[i]) + sh[i] for i in range(3)), t); cnt[key] = cnt.get(key, 0) ^ 1
            out.append([k for k, v in cnt.items() if v])
    return out
EXT = ext_patterns()
def move_tables_ext(L):
    tabs = []
    for p in EXT:
        cnt = {}
        for d, t in p:
            key = (tuple(int(v) % L for v in d), t); cnt[key] = cnt.get(key, 0) ^ 1
        tabs.append([k for k, v in cnt.items() if v])
    maxs = max(len(t) for t in tabs)
    S = -np.ones((len(tabs), maxs, 4), dtype=np.int64)
    for a, tab in enumerate(tabs):
        for b, (d, t) in enumerate(tab): S[a, b] = (d[0], d[1], d[2], t)
    GE = np.zeros((6, 4, 5), dtype=np.int64); GN = np.zeros(6, dtype=np.int64)
    for t in range(6):
        ent = G_entries((0, 0, 0), t); GN[t] = len(ent)
        for b, ((e, j), c) in enumerate(ent): GE[t, b] = (e[0], e[1], e[2], j, c)
    return S, GE, GN
if __name__ == "__main__":
    print("extended family: %d patterns, sizes %s" % (len(EXT), [len(p) for p in EXT]))
