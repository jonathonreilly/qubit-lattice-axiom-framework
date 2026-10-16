"""Signed-permutation representations of O (or 2O) on the 8 corners of a 2x2x2 block, rotations about the block centre."""
import itertools, numpy as np
RZ = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); RX = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
corners = [np.array(v) for v in itertools.product((0, 1), repeat=3)]
cidx = {tuple(v): i for i, v in enumerate(corners)}
def perm(R):
    P = np.zeros((8, 8))
    for i, v in enumerate(corners):
        w = R @ (2 * v - 1)          # coordinates relative to centre, doubled
        P[cidx[tuple((w + 1) // 2)], i] = 1
    return P
PZ, PX = perm(RZ), perm(RX)
def group(gens, cap=200):
    G = {np.eye(8).tobytes(): np.eye(8)}; fr = [np.eye(8)]
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = A @ g; k = np.round(B).tobytes()
                if k not in G:
                    G[k] = np.round(B); nx.append(np.round(B))
                    if len(G) > cap: return None
        fr = nx
    return list(G.values())
def char(G):
    # class function: sorted multiset of (trace, order) is enough to tell reps apart here
    return tuple(sorted((int(round(np.trace(g))), next(k for k in range(1, 9) if np.allclose(np.linalg.matrix_power(g, k), np.eye(8)))) for g in G))
reps = {}
for sz in itertools.product((1, -1), repeat=8):
    for sx in itertools.product((1, -1), repeat=8):
        DZ = np.diag(sz) @ PZ; DX = np.diag(sx) @ PX
        G = group([DZ, DX])
        if G is None: continue
        spin = any(np.allclose(g, -np.eye(8)) for g in G)
        if len(G) == 24 or (len(G) == 48 and spin):
            key = (len(G), char(G))
            reps.setdefault(key, (DZ, DX))
print(len(reps), 'inequivalent signed corner reps (by character data)')
for (n, ch), (DZ, DX) in reps.items():
    G = group([DZ, DX])
    # multiplicity of the trivial rep and spinorial flag
    print(n, 'spinorial' if n == 48 else 'integer', 'trace(DZ)=', int(np.trace(DZ)), 'trace(DX)=', int(np.trace(DX)))
np.save('blockreps.npy', np.array([np.stack([DZ, DX]) for (DZ, DX) in reps.values()]))
