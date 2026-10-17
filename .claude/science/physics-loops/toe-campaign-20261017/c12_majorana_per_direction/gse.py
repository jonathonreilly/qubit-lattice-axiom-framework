"""Majorana-per-direction (GSE-type) fermion code on Z^3: 3 qubits per site carry 6 Majoranas gamma_{v,d}.
Edge operator A_(v,a) = gamma_{v,+a} gamma_{v+a,-a}; vertex parity B_v = (-i)^3 gamma_{v,0..5};
plaquette stabilizer = product of the 4 edge operators around a plaquette. O acts by site permutation and
gamma_{v,d} -> eps_R(d) gamma_{Rv,Rd} (an on-site Clifford)."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb
bk = rb.bk; c1 = rb.c1
from collections import Counter
E, DIRS, O = bk.E, bk.DIRS, c1.O
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
n = 3 * L ** 3
V = list(itertools.product(range(L), repeat=3))
def sidx(v): return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)
# JW on 3 qubits: gamma_0 = X1, gamma_1 = Y1, gamma_2 = Z1 X2, gamma_3 = Z1 Y2, gamma_4 = Z1 Z2 X3, gamma_5 = Z1 Z2 Y3
JW = [((1, 0, 0), (0, 0, 0), 0), ((1, 0, 0), (1, 0, 0), 1), ((0, 1, 0), (1, 0, 0), 0), ((0, 1, 0), (1, 1, 0), 1),
      ((0, 0, 1), (1, 1, 0), 0), ((0, 0, 1), (1, 1, 1), 1)]   # (x bits, z bits, k) with P = i^k X^x Z^z ; Y = i X Z
MAJ = None  # direction d -> Majorana index; set below
def gamma(v, d):
    x = np.zeros(n, np.uint8); z = np.zeros(n, np.uint8)
    xb, zb, k = JW[MAJ[d]]
    s = sidx(v)
    for t in range(3):
        x[3 * s + t] = xb[t]; z[3 * s + t] = zb[t]
    return [x, z, k]
def word(ws):
    P = rb.one()
    for (v, d) in ws: P = rb.mulp(P, gamma(v, d))
    return P
def herm(P):
    if (P[2] - int(P[0].astype(int) @ P[1].astype(int))) % 2: P = [P[0], P[1], (P[2] + 1) % 4]
    return P
def edge_word(v, a):
    w = tuple(v[i] + E[a][i] for i in range(3))
    return [(v, DIRS.index((a, 1))), (w, DIRS.index((a, -1)))]
def plaq_word(v, c):
    a, b = [t for t in range(3) if t != c]
    va = tuple(v[i] + E[a][i] for i in range(3)); vb = tuple(v[i] + E[b][i] for i in range(3))
    return edge_word(v, a) + edge_word(va, b) + edge_word(vb, a) + edge_word(v, b)
def B_word(v): return [(v, d) for d in range(6)]
def B_op(v):
    P = word(B_word(v)); return [P[0], P[1], (P[2] + 3 * 3) % 4]   # (-i)^3 = i
def gens(signs):
    G, lab, words = [], [], []
    for v in V:
        G.append(herm(B_op(v))); lab.append(('B', v, None)); words.append(B_word(v))
        for c in range(3):
            P = herm(word(plaq_word(v, c))); P[2] = (P[2] + 2 * signs[c]) % 4
            G.append(P); lab.append(('S', v, c)); words.append(plaq_word(v, c))
    return G, lab, words
rb.L, rb.N = L, n
def dims_and_comm(G):
    M = np.array([np.concatenate([g[0], g[1]]) for g in G])
    sy = (M[:, :n].astype(np.int32) @ M[:, n:].T.astype(np.int32) + M[:, n:].astype(np.int32) @ M[:, :n].T.astype(np.int32)) % 2
    r = c1.f2_rank_and_null(M)[0]
    return not sy.any(), n - r
if __name__ == '__main__':
    MAJ = list(range(6))
    for signs in itertools.product((0, 1), repeat=3):
        G, lab, words = gens(signs)
        comm, k = dims_and_comm(G)
        valid = rb.valid(G)
        print('signs', signs, 'commuting', comm, 'log2 dim', k, 'valid', valid, flush=True)
