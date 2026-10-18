"""Global 2O lift on the full 768-dim space by BFS from two generators (C4z, C3[111]),
independent of the runner's GF(2) cocycle solve. Exposes OPS2O: list of (SU2 matrix, 768x768 op)."""
import itertools
import numpy as np
from common import *

PAU = [np.array([[0,1],[1,0]]), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]])]
def su2(axis, ang):
    n = np.array(axis, float); n /= np.linalg.norm(n)
    return np.cos(ang/2) * np.eye(2) - 1j * np.sin(ang/2) * sum(n[i] * PAU[i] for i in range(3))
def so3(U): return np.rint(np.array([[0.5*np.real(np.trace(PAU[i]@U@PAU[j]@U.conj().T)) for j in range(3)] for i in range(3)])).astype(int)
def rid(R): return [k for k, S in enumerate(ROTS) if (S == R).all()][0]
TW = [dense(ROT[r], 1j ** W1[r]) for r in range(24)]   # twisted ops i^{w1} M_R

def build(eps1, eps2):
    g1, g2 = su2((0,0,1), np.pi/2), su2((1,1,1), 2*np.pi/3)
    gens = [(g1, eps1 * TW[rid(so3(g1))]), (g2, eps2 * TW[rid(so3(g2))])]
    elems = [(np.eye(2, dtype=complex), np.eye(nV, dtype=complex))]
    frontier = list(elems)
    while frontier:
        nf = []
        for U, M in frontier:
            for gU, gM in gens:
                U2 = gU @ U; M2 = gM @ M
                hit = [x for x in elems if np.allclose(x[0], U2)]
                if hit:
                    if not np.allclose(hit[0][1], M2): return None
                else:
                    elems.append((U2, M2)); nf.append((U2, M2))
        frontier = nf
    assert len(elems) == 48
    return elems

if __name__ == '__main__':
    res = {}
    for e1, e2 in itertools.product((1, -1), repeat=2):
        r = build(e1, e2); res[(e1, e2)] = r is not None
        print("generator signs", (e1, e2), "consistent homomorphism:", r is not None)
