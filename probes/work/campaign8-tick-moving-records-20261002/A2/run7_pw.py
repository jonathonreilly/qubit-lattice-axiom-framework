"""Polyakov-Wiegmann additivity W3[UV]=W3[U]+W3[V], and node/W3 sign relation on the mirror map."""
import numpy as np
from wlib import grid, w3_from, find_nodes_su2
from models import E1, E3

def prod(f, g):
    def h(K):
        U, dU = f(K); V, dV = g(K)
        return U @ V, np.stack([dU[j] @ V + U @ dV[j] for j in range(3)])
    return h

def mirror(K):
    U, dU = E3(-np.atleast_2d(K)); return U, -dU

K = grid(40)
for name, f in (("E3", E3), ("E1", E1), ("E3*E1", prod(E3, E1)), ("E3*E3", prod(E3, E3)), ("E3*mirror", prod(E3, mirror))):
    U, dU = f(K)
    print(f"  W3[{name}] = {w3_from(U, dU, U.conj().transpose(0,2,1))[0]:+.6f}")
nodes = find_nodes_su2(mirror, N=20)
net = {1: 0, -1: 0}
for k0, u0, chi, _ in nodes: net[u0] += chi
print(f"  mirror map: {len(nodes)} nodes, net chi at 0: {net[1]:+d}, at pi: {net[-1]:+d}")
