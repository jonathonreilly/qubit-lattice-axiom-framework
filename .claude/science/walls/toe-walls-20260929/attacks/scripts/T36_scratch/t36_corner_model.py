#!/usr/bin/env python3
"""T36 scratch: symmetry lifts on the repo's supplied KS corner model (L=4 torus).
Builds: staggered hopping H4, 24 rotation lifts, 3 one-site shift lifts, the 8-dim corner kernel
and the restriction of every lift to it. Shared by the later T36 scripts (import as module).
Model is the repo's own supplied one (docs/CORNER_KERNEL_CUBIC_CARRIERS_..._2026-09-02.md); nothing
here is derived from the four axioms.
"""
from __future__ import annotations
import itertools
from collections import deque
import numpy as np

L4 = 4
EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


S4 = [v for v in itertools.product(range(L4), repeat=3)]
IDX4 = {v: i for i, v in enumerate(S4)}
N4 = len(S4)
H4 = np.zeros((N4, N4))
for v in S4:
    for a in range(3):
        w = tuple((v[i] + EX[a][i]) % L4 for i in range(3))
        H4[IDX4[w], IDX4[v]] += eta_ks(v, a)
        H4[IDX4[v], IDX4[w]] += eta_ks(v, a)

# proper rotations (signed permutation matrices, det +1)
ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1:
            ROTS.append(M)


def rot_act(M, v):
    return tuple(int(sum(M[i, j] * v[j] for j in range(3))) % L4 for i in range(3))


def gauge_lift(sigma):
    """Find signs g(v) with C[sigma(v), v] = g(v) so that C H C^T = H, or None."""
    def target(v, a):
        w = tuple((v[i] + EX[a][i]) % L4 for i in range(3))
        return H4[IDX4[sigma(v)], IDX4[sigma(w)]]
    g = {(0, 0, 0): 1}
    dq = deque([(0, 0, 0)])
    while dq:
        v = dq.popleft()
        for a in range(3):
            for sgn in (1, -1):
                w = list(v)
                w[a] += sgn
                w = tuple(x % L4 for x in w)
                src = v if sgn == 1 else w
                r = target(src, a) * eta_ks(src, a)
                if w in g:
                    if g[w] != g[v] * r:
                        return None
                else:
                    g[w] = g[v] * r
                    dq.append(w)
    C = np.zeros((N4, N4))
    for v in S4:
        C[IDX4[sigma(v)], IDX4[v]] = g[v]
    return C


ROT_LIFTS = [gauge_lift(lambda v, M=M: rot_act(M, v)) for M in ROTS]
SHIFT_LIFTS = [gauge_lift(lambda v, c=c: tuple((v[i] + EX[c][i]) % L4 for i in range(3))) for c in range(3)]

# corner kernel: momentum-pi combination of the 2x2x2 cell (repo's KINT)
KINT = np.zeros((N4, 8), dtype=int)
for s in range(8):
    sv = [(s >> (2 - a)) & 1 for a in range(3)]
    for R in itertools.product(range(2), repeat=3):
        KINT[IDX4[tuple(2 * R[a] + sv[a] for a in range(3))], s] = (-1) ** sum(R)
KER = KINT / np.sqrt(8.0)
HW = np.array([bin(s).count("1") for s in range(8)])


def restrict(C):
    return KER.T @ C @ KER


ROT_K = [restrict(C) for C in ROT_LIFTS]
SHIFT_K = [restrict(C) for C in SHIFT_LIFTS]

if __name__ == "__main__":
    print("rot lifts ok:", all(C is not None for C in ROT_LIFTS), len(ROT_LIFTS))
    print("shift lifts ok:", [C is not None for C in SHIFT_LIFTS])
    print("H4 kernel dim:", int(np.sum(np.abs(np.linalg.eigvalsh(H4)) < 1e-9)))
    print("H4 KINT = 0:", np.allclose(H4 @ KINT, 0))
    print("rot lifts commute with H4:", all(np.allclose(C @ H4 @ C.T, H4) for C in ROT_LIFTS))
    print("shift lifts commute with H4:", all(np.allclose(C @ H4 @ C.T, H4) for C in SHIFT_LIFTS))
    for c, S in enumerate(SHIFT_K):
        print("shift", c, "on kernel: signed-permutation?", np.allclose(np.abs(S).sum(0), 1) and np.allclose(np.abs(S).sum(1), 1))
        # which corner index does it send each basis state to
        tgt = [(int(np.argmax(np.abs(S[:, s]))), int(np.rint(S[np.argmax(np.abs(S[:, s])), s]))) for s in range(8)]
        print("   s -> (s', sign):", tgt)
        print("   hw map:", [(int(HW[s]), int(HW[t[0]])) for s, t in enumerate(tgt)])
