"""K2: independent 4D U(1) staggered check with larger L (attack stopped at L=6, c=0.81 'unconverged').
Own implementation: D (staggered), Gamma = (-1)^{x0+x2} * (1/24) sum_perm C_a C_b C_c C_d (validated equal to the attack's
spin-taste singlet at L=6 in p0b_4d.py), U(1) flux F01 = 2 pi Q1/L^2, F23 = 2 pi Q2/L^2.  Sparse LU determinant phase."""
import itertools, sys, time
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl

def perm_sign(p):
    n = len(p); seen = np.zeros(n, bool); s = 1
    for i in range(n):
        if not seen[i]:
            j = i; ln = 0
            while not seen[j]:
                seen[j] = True; j = p[j]; ln += 1
            if ln % 2 == 0:
                s = -s
    return s

def detphase(M):
    M = sp.csc_matrix(M)
    lu = spl.splu(M, permc_spec="COLAMD", diag_pivot_thresh=1.0)
    d = lu.U.diagonal()
    ph = np.prod(d / np.abs(d))
    ph *= perm_sign(lu.perm_r) * perm_sign(lu.perm_c)
    return np.angle(ph), np.sum(np.log(np.abs(d)))

def build4(L, Q1, Q2):
    V = L ** 4
    X = np.indices((L, L, L, L)).reshape(4, -1).T   # index = ((x0 L + x1) L + x2) L + x3
    def idx(x):
        return ((x[:, 0] % L * L + x[:, 1] % L) * L + x[:, 2] % L) * L + x[:, 3] % L
    p1, p2 = 2 * np.pi * Q1 / L ** 2, 2 * np.pi * Q2 / L ** 2
    U = np.ones((4, V), complex)
    U[1] = np.exp(1j * p1 * X[:, 0])
    U[0] = np.where(X[:, 0] == L - 1, np.exp(-1j * p1 * L * X[:, 1]), 1.0)
    U[3] = np.exp(1j * p2 * X[:, 2])
    U[2] = np.where(X[:, 2] == L - 1, np.exp(-1j * p2 * L * X[:, 3]), 1.0)
    T = []
    for mu in range(4):
        Y = X.copy(); Y[:, mu] += 1
        T.append(sp.csr_matrix((U[mu], (np.arange(V), idx(Y))), shape=(V, V)))
    eta = [np.ones(V)] + [(-1.0) ** X[:, :mu].sum(1) for mu in range(1, 4)]
    D = sum(0.5 * sp.diags(eta[mu]) @ (T[mu] - T[mu].conj().T) for mu in range(4)).tocsr()
    C = [0.5 * (T[mu] + T[mu].conj().T) for mu in range(4)]
    S = None
    for pm in itertools.permutations(range(4)):
        P = C[pm[0]] @ C[pm[1]] @ C[pm[2]] @ C[pm[3]]
        S = P if S is None else S + P
    G = (sp.diags((-1.0) ** (X[:, 0] + X[:, 2])) @ S / 24.0).tocsr()
    # check fluxes
    def plaq(mu, nu):
        Ymu = X.copy(); Ymu[:, mu] += 1
        Ynu = X.copy(); Ynu[:, nu] += 1
        return np.angle(U[mu] * U[nu][idx(Ymu)] * np.conj(U[mu][idx(Ynu)]) * np.conj(U[nu])).sum() / (2 * np.pi)
    return D, G, plaq(0, 1), plaq(2, 3)

if __name__ == "__main__":
    out = []
    def rep(s):
        print(s, flush=True); out.append(s)
    r = 0.1
    ms = (0.02, 0.05, 0.1, 0.2, 0.5)
    Ls = [int(a) for a in sys.argv[1].split(",")] if len(sys.argv) > 1 else [4, 6, 8]
    for (Q1, Q2) in [(1, 1), (2, 1)]:
        Q = Q1 * Q2
        for L in Ls:
            t0 = time.time()
            D, G, f1, f2 = build4(L, Q1, Q2)
            V = L ** 4
            I = sp.identity(V, format="csr")
            row = []
            for m in ms:
                a, _ = detphase(D + m * I + 1j * r * m * G)
                row.append(f"m={m}:{-a/(4*Q*np.arctan(r)):.4f}")
            rep(f"4D Q1,Q2=({Q1},{Q2}) Q={Q} L={L:2d} (flux {f1:.3f},{f2:.3f})  c=-arg/(4 Q atan r):  " + "  ".join(row) + f"   [{time.time()-t0:.0f}s]")
    open("k2_out_%s.txt" % ("_".join(map(str, Ls))), "w").write("\n".join(out) + "\n")
