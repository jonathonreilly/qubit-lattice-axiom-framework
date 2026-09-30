"""k2c: in C3-covariant NN symbols (no D2, no Theta), how many nodes lie off the C3 axis (orbits of 3), and their chirality?"""
import sys
import numpy as np
sys.path.insert(0, "rerun")
import A_pin as A
P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
C3 = [np.eye(3, dtype=int), P, P @ P]
res = {}
for s in range(60):
    rg = np.random.default_rng(1000 + s)
    A.rng = rg
    ws = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    C = {w: (rg.normal(size=4), rg.normal(size=4)) for w in ws}
    const = rg.normal(size=4)
    cav, tab = A.average(const, C, C3, "full")
    nodes = A.find_nodes(cav, tab, nseed=12)
    def onaxis(k):
        return abs(((k[0] - k[1]) + np.pi) % (2 * np.pi) - np.pi) < 1e-5 and abs(((k[1] - k[2]) + np.pi) % (2 * np.pi) - np.pi) < 1e-5
    on = [(k, c) for k, c in nodes if onaxis(k)]
    off = [(k, c) for k, c in nodes if not onaxis(k)]
    key = (len(on), len(off), sum(c for _, c in on), sum(c for _, c in off))
    res[key] = res.get(key, 0) + 1
print("(on-axis nodes, off-axis nodes, chi sum on-axis, chi sum off-axis) -> samples")
for k, v in sorted(res.items()):
    print("  ", k, v)
