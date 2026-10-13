"""R19-22 s3: can the two N-type constraints be imposed jointly when the CCR pairs are replaced by spin-S (HP)?

Pre-registered (06:28Z, before running):
 HP slots: q_a = S^y_a/sqrt(S), p_a = S^z_a/sqrt(S), so [q_a, p_b] = i delta_ab S^x_a / S.
 Vector law (G p)_e (edges e), scalar law (S q)_y (sites y), N0914's integer stencils (N0914:105-113).
 Then [(G p)_e, (S q)_y] = -(i/S) sum_a G[e,a] S[y,a] S^x_a  (exact operator identity).
 Lemma J: if the matrix C[(e,y), a] = G[e,a] S[y,a] has full column rank, any joint zero vector psi of all
 constraints obeys S^x_a psi = 0 for every slot a. For half-integer S, S^x_a has no zero eigenvalue => no joint
 physical state at all. Check: G S^T = 0 over Z on L^3 tori (L=3,4,5), and rank C = #slots.
"""
import numpy as np, itertools

def stencils(L):
    sites = list(itertools.product(range(L), repeat=3))
    sid = {s: i for i, s in enumerate(sites)}
    nS = len(sites)
    # slots: per site 3 diagonal (jj) + 3 off-diagonal (ij, i<j) ; index = 6*site + c
    pairs = [(0, 1), (1, 2), (0, 2)]
    def sl_diag(x, j): return 6*sid[tuple(np.mod(x, L))] + j
    def sl_off(x, i, j):
        c = pairs.index((min(i, j), max(i, j)))
        return 6*sid[tuple(np.mod(x, L))] + 3 + c
    e = np.eye(3, dtype=int)
    G = np.zeros((3*nS, 6*nS), dtype=int)
    for s in sites:
        x = np.array(s)
        for j in range(3):
            r = 3*sid[s] + j
            G[r, sl_diag(x + e[j], j)] += 1; G[r, sl_diag(x, j)] -= 1
            for i in range(3):
                if i == j: continue
                G[r, sl_off(x, i, j)] += 1; G[r, sl_off(x - e[i], i, j)] -= 1
    Sm = np.zeros((nS, 6*nS), dtype=int)
    for s in sites:
        x = np.array(s); r = sid[s]
        for j in range(3):
            for i in range(3):
                if i == j: continue
                Sm[r, sl_diag(x + e[i], j)] += 1; Sm[r, sl_diag(x - e[i], j)] += 1; Sm[r, sl_diag(x, j)] -= 2
        for (i, j) in pairs:
            Sm[r, sl_off(x, i, j)] -= 1; Sm[r, sl_off(x - e[i], i, j)] += 1
            Sm[r, sl_off(x - e[j], i, j)] += 1; Sm[r, sl_off(x - e[i] - e[j], i, j)] -= 1
    return G, Sm

for L in [3, 4, 5]:
    G, Sm = stencils(L)
    gs = np.abs(G @ Sm.T).max()
    # C rows: all (edge, site) pairs with overlapping support
    rows = []
    for ei in range(G.shape[0]):
        ge = G[ei]
        nz = np.nonzero(ge)[0]
        ys = np.unique(np.nonzero(Sm[:, nz])[0])
        for y in ys:
            rows.append(ge*Sm[y])
    C = np.array(rows, dtype=float)
    rk = np.linalg.matrix_rank(C)
    print(f"L={L}: slots={G.shape[1]}  max|G S^T|={gs}  rows(C)={C.shape[0]}  rank C = {rk}  full column rank: {rk == G.shape[1]}")

# small explicit operator check of the commutator identity on 2 slots (S=1/2 and S=1)
def spin_ops(S):
    d = int(round(2*S + 1)); m = S - np.arange(d); Sp = np.zeros((d, d))
    for i in range(1, d): Sp[i-1, i] = np.sqrt(S*(S+1) - m[i]*(m[i]+1))
    return (Sp + Sp.T)/2, (Sp - Sp.T)/(2j), np.diag(m)
for S in [0.5, 1.0, 1.5]:
    Sx, Sy, Sz = spin_ops(S); d = Sx.shape[0]; I = np.eye(d)
    q = [np.kron(Sy, I)/np.sqrt(S), np.kron(I, Sy)/np.sqrt(S)]; p = [np.kron(Sz, I)/np.sqrt(S), np.kron(I, Sz)/np.sqrt(S)]
    X = [np.kron(Sx, I), np.kron(I, Sx)]
    g = np.array([1, -1]); s = np.array([2, 3])
    A = g[0]*p[0] + g[1]*p[1]; B = s[0]*q[0] + s[1]*q[1]
    lhs = A@B - B@A; rhs = -(1j/S)*(g[0]*s[0]*X[0] + g[1]*s[1]*X[1])
    print(f"S={S}: commutator identity residual {np.abs(lhs - rhs).max():.2e};  min |eig S^x| = {np.abs(np.linalg.eigvalsh(Sx)).min():.3f}")

print("\nRank deficiency of C is the uniform vector (S^x_a = const passes); go to double commutators (added 06:31Z):")
print(" [Gp_e,[Gp_e',Sq_y]] = (1/S) sum_a G[e,a]G[e',a]S[y,a] q_a ;  [Sq_y',[Gp_e,Sq_y]] = -(1/S) sum_a G[e,a]S[y,a]S[y',a] p_a")
print(" On a joint zero vector both vanish; full column rank of the coefficient matrices => q_a psi = p_a psi = 0 for all a")
print(" => S^x_a psi = -i[S^y_a,S^z_a] psi = 0 => S_a^2 psi = S(S+1) psi = 0 => psi = 0 (every S >= 1/2).")
for L in [3, 4]:
    G, Sm = stencils(L)
    nz_e = [np.nonzero(G[e])[0] for e in range(G.shape[0])]
    rowsQ, rowsP = [], []
    for e in range(G.shape[0]):
        ys = np.unique(np.nonzero(Sm[:, nz_e[e]])[0])
        es = np.unique(np.nonzero(G[:, nz_e[e]])[0])
        for y in ys:
            for e2 in es:
                v = G[e]*G[e2]*Sm[y]
                if v.any(): rowsQ.append(v)
            ys2 = np.unique(np.nonzero(Sm[:, nz_e[e]])[0])
            for y2 in ys2:
                v = G[e]*Sm[y]*Sm[y2]
                if v.any(): rowsP.append(v)
    DQ = np.array(rowsQ, float); DP = np.array(rowsP, float)
    print(f"L={L}: slots={G.shape[1]}  rank D_q = {np.linalg.matrix_rank(DQ)}  rank D_p = {np.linalg.matrix_rank(DP)}")

# direct brute-force check on a toy 'constraint pair' with the same structure (2 slots is too small for the lattice
# stencils; instead check the logic: joint kernel of p-type and q-type spin constraints with GS^T=0 over Z on 3 slots)
for S in [0.5, 1.0, 1.5, 2.0]:
    Sx, Sy, Sz = spin_ops(S); d = Sx.shape[0]; I = np.eye(d)
    def op(M, a):
        mats = [I, I, I]; mats[a] = M
        return np.kron(np.kron(mats[0], mats[1]), mats[2])
    g = np.array([1, -1, 0]); s = np.array([1, 1, 5])        # g.s = 0 over Z: classical first-class
    A = sum(g[a]*op(Sz, a) for a in range(3)); B = sum(s[a]*op(Sy, a) for a in range(3))
    M = A.conj().T@A + B.conj().T@B
    print(f" toy 3-slot S={S}: g.s={g@s}; smallest eig of A^dag A + B^dag B = {np.linalg.eigvalsh(M).min():.3e}  (0 => joint kernel exists)")
