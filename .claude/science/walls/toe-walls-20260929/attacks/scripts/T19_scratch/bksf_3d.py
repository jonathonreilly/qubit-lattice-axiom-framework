"""Test B3: 3D BKSF vacuum on the cubic torus (edge qubits, 3 per vertex).  Local-stabilizer ground-space dimension."""
import numpy as np, itertools, sys
from bksf_tee import gf2_rank, vec, omega

def run(L):
    def v(c): return ((c[0] % L) * L + (c[1] % L)) * L + (c[2] % L)
    n = 3 * L ** 3
    def e(c, d): return 3 * v(c) + d
    def shift(c, d, s=1):
        c = list(c); c[d] += s; return tuple(c)
    def incident(c):
        return [e(c, 0), e(c, 1), e(c, 2), e(shift(c, 0, -1), 0), e(shift(c, 1, -1), 1), e(shift(c, 2, -1), 2)]
    def A(c, d):
        tail = tuple(x % L for x in c); head = tuple(x % L for x in shift(c, d))
        ee = e(c, d); zs = []
        for w in (tail, head):
            lst = incident(w); zs += lst[:lst.index(ee)]
        return vec(n, xs=[ee], zs=zs)
    B = [vec(n, zs=incident(c)) for c in itertools.product(range(L), repeat=3)]
    P = []
    for c in itertools.product(range(L), repeat=3):
        for d1, d2 in ((0, 1), (0, 2), (1, 2)):
            g = A(c, d1) ^ A(shift(c, d1), d2) ^ A(shift(c, d2), d1) ^ A(c, d2)
            P.append(g)
    loops = []
    for d in range(3):
        g = np.zeros(2 * n, dtype=np.uint8)
        for i in range(L):
            c = [0, 0, 0]; c[d] = i
            g ^= A(tuple(c), d)
        loops.append(g)
    Gl = np.array(B + P, dtype=np.uint8); Gall = np.vstack([Gl, np.array(loops, dtype=np.uint8)])
    for a in range(0, Gall.shape[0], 7):  # spot-check commutation
        for b in range(Gall.shape[0]):
            assert omega(Gall[a], Gall[b], n) == 0
    return n, gf2_rank(Gl), gf2_rank(Gall)

for L in (3, 4):
    n, rl, ra = run(L)
    print(f"3D torus L={L}: qubits n={n}, rank(local gens B_v + plaquette loops)={rl}, rank(with 3 noncontractible loops)={ra}; local-stabilizer ground space dim = 2^{n-rl}")
