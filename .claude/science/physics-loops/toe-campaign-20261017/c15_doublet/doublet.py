"""Spinful Majorana-per-direction code: 5 qubits/site = 10 Majoranas: links b_d (d = 0..5) and matter
g_{up,1}, g_{up,2}, g_{dn,1}, g_{dn,2}. Stabilizers: D_v (total parity), W_p (link plaquettes), P_up, P_dn."""
import sys, itertools
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import bksf_cubic_fermion_codes_rotations_act_by_bare_permutation_2026_10_17 as rb
bk, c1 = rb.bk, rb.c1
from collections import Counter
E, DIRS = bk.E, bk.DIRS
L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
Q = 5; n = Q * L ** 3
rb.L, rb.N = L, n
V = list(itertools.product(range(L), repeat=3))
def sidx(v): return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)
def one(): return [np.zeros(n, np.uint8), np.zeros(n, np.uint8), 0]
def maj(v, k):
    """chi_k on site v, Jordan-Wigner inside the site: chi_{2j} = Z..Z X_j, chi_{2j+1} = Z..Z Y_j."""
    P = one(); s = sidx(v); j = k // 2
    for t in range(j): P[1][Q * s + t] = 1
    P[0][Q * s + j] = 1
    if k % 2: P[1][Q * s + j] ^= 1; P[2] = 1      # Y = i X Z
    # reorder: P = i^k X^x Z^z with Z's on t<j and X (Z) on j: X^x Z^z ordering is fine (different qubits commute)
    return P
def mul(*Ps):
    R = one()
    for P in Ps: R = rb.mulp(R, P)
    return R
def herm(P):
    if (P[2] - int(P[0].astype(int) @ P[1].astype(int))) % 2: P = [P[0], P[1], (P[2] + 1) % 4]
    return P
UP1, UP2, DN1, DN2 = 6, 7, 8, 9
def u_edge(v, a):
    w = tuple(v[i] + E[a][i] for i in range(3))
    return mul(maj(v, DIRS.index((a, 1))), maj(w, DIRS.index((a, -1))))
def gens():
    G, lab = [], []
    for v in V:
        G.append(herm(mul(*[maj(v, k) for k in range(10)]))); lab.append(('D', v))
        G.append(herm(mul(maj(v, UP1), maj(v, UP2)))); lab.append(('Pup', v))
        G.append(herm(mul(maj(v, DN1), maj(v, DN2)))); lab.append(('Pdn', v))
        for c in range(3):
            a, b = [t for t in range(3) if t != c]
            va = tuple(v[i] + E[a][i] for i in range(3)); vb = tuple(v[i] + E[b][i] for i in range(3))
            G.append(herm(mul(u_edge(v, a), u_edge(va, b), u_edge(vb, a), u_edge(v, b)))); lab.append(('W', v, c))
    return G, lab
om = lambda P, R: int((P[0].astype(int) @ R[1].astype(int) + P[1].astype(int) @ R[0].astype(int)) % 2)
if __name__ == '__main__':
    G, lab = gens()
    M = np.array([np.concatenate([g[0], g[1]]) for g in G])
    sy = (M[:, :n].astype(np.int32) @ M[:, n:].T.astype(np.int32) + M[:, n:].astype(np.int32) @ M[:, :n].T.astype(np.int32)) % 2
    print('commuting:', not sy.any(), ' valid (no -1):', rb.valid(G), ' log2 code dim:', n - c1.f2_rank_and_null(M)[0], flush=True)
    # (b) sectors: gamma_up at v violates exactly D_v and Pup_v; no operator near v violates Pup_v alone
    v0 = (0, 0, 0)
    g = maj(v0, UP1)
    print('gamma_up(0) violates:', [l for G_, l in zip(G, lab) if om(g, G_)])
    # local solve for an operator in the radius-2 box with syndrome {Pup_0} only
    box = [p for p in itertools.product(range(-2, 3), repeat=3)]
    cols = np.array(sorted({Q * sidx(p) + t for p in box for t in range(Q)}))
    rows, rhs = [], []
    for G_, l in zip(G, lab):
        cg = np.concatenate([G_[1][cols], G_[0][cols]])
        if not cg.any(): continue
        rows.append(cg); rhs.append(1 if (l[0] == 'Pup' and l[1] == v0) else 0)
    A = np.concatenate([np.array(rows, np.uint8), np.array(rhs, np.uint8)[:, None]], 1)
    r, Nn = c1.f2_rank_and_null(A[:, :-1])
    r2 = c1.f2_rank_and_null(A)[0]
    print('local (radius-2) operator creating Pup_0 alone exists:', r2 == r)
    # (c) statistics of the up excitation: hops h_e = g_up1(v) u_e g_up1(w)
    def hop(v, a):
        w = tuple(v[i] + E[a][i] for i in range(3))
        return mul(maj(v, UP1), u_edge(v, a), maj(w, UP1))
    def leg(d, steps=2):
        a, s = DIRS[d]; v = (0, 0, 0); P = one()
        for _ in range(steps):
            if s == 1: base = v; v = tuple(v[i] + E[a][i] for i in range(3))
            else: v = tuple(v[i] - E[a][i] for i in range(3)); base = v
            P = rb.mulp(P, hop(base, a))
        return P
    legs = [leg(d) for d in range(6)]
    viol = [[l for G_, l in zip(G, lab) if om(lg, G_)] for lg in legs]
    print('each up-leg violates only Pup at its two ends:', all(len(vv) == 2 and all(x[0] == 'Pup' for x in vv) for vv in viol))
    tj = Counter((-1) ** (om(legs[a], legs[b]) + om(legs[b], legs[c]) + om(legs[a], legs[c])) for a, b, c in itertools.combinations(range(6), 3))
    print('T-junction signs of the up excitation:', dict(tj))
    # up and down at the same site related by a local operator (same sector)
    conv = mul(maj(v0, UP1), maj(v0, DN1))
    print('g_up1 g_dn1 at 0 violates:', [l for G_, l in zip(G, lab) if om(conv, G_)])
