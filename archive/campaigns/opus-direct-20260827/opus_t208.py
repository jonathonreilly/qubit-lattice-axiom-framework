"""
T208 - is M4(C) FORCED, or merely sufficient?

The campaign's single axiom-level recommendation (R122/R123) is to enlarge the
Qubit axiom's possibility domain from M2(C) to M4(C).  It is established as
SUFFICIENT.  Two gaps:

  (A) R122 showed the PRODUCT of all gammas fails to anticommute with them when
      d is odd.  It never showed that no OTHER element can serve as a chirality.
      Tested here by solving {X, Gamma_a} = 0 for all a as a nullspace.

  (B) Nobody showed M4(C) is MINIMAL.  Tested here by an elementary counting
      argument (the 2^k Clifford products are linearly independent, so
      n^2 >= 2^k), verified numerically, plus a failed numerical search.
"""
import numpy as np, itertools

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)

def kron(*a):
    out = np.array([[1.0+0j]])
    for m in a: out = np.kron(out, m)
    return out

def cliff(k):
    """k mutually anticommuting matrices in the minimal dimension 2^floor(k/2)."""
    m = k//2
    G = []
    for j in range(m):
        pre = [SZ]*j
        G.append(kron(*(pre+[SX]+[I2]*(m-j-1))))
        G.append(kron(*(pre+[SY]+[I2]*(m-j-1))))
    if k % 2 == 1:
        G.append(kron(*([SZ]*m)))
    return G[:k]

def anticomm_max(G):
    return max(np.max(np.abs(G[a]@G[b] + G[b]@G[a])) for a in range(len(G)) for b in range(a+1, len(G)))

def chirality_space(G, n):
    """dim of {X : {X, G_a} = 0 for all a}, via nullspace of the stacked map."""
    M = np.vstack([np.kron(g, np.eye(n)) + np.kron(np.eye(n), g.T) for g in G])
    U, sv, Vt = np.linalg.svd(M, full_matrices=False)
    tol = max(M.shape)*np.finfo(float).eps*(sv.max() if sv.size else 1.0)
    return int(np.sum(sv <= tol)), sv

print("=== (A) does ANY chirality exist?  dim{X : {X,Gamma_a}=0 for all a} ===")
print(f"{'k':>3} {'n':>4} {'anticomm err':>14} {'prod-anticomm':>15} {'dim chiral':>11}  verdict")
for k in range(2, 8):
    G = cliff(k); n = G[0].shape[0]
    P = G[0].copy()
    for g in G[1:]: P = P @ g
    pa = max(np.max(np.abs(P@g + g@P)) for g in G)
    d, sv = chirality_space(G, n)
    print(f"{k:3d} {n:4d} {anticomm_max(G):14.1e} {pa:15.1e} {d:11d}  "
          f"{'CHIRALITY EXISTS' if d > 0 else 'NONE - no element at all'}")

print("\n=== (B) minimality: are the 2^k Clifford products independent? ===")
print(f"{'k':>3} {'n':>4} {'n^2':>5} {'2^k':>5} {'rank of products':>18} {'n^2>=2^k':>9}")
for k in range(2, 7):
    G = cliff(k); n = G[0].shape[0]
    prods = []
    for r in range(k+1):
        for S in itertools.combinations(range(k), r):
            M = np.eye(n, dtype=complex)
            for a in S: M = M @ G[a]
            prods.append(M.ravel())
    rk = np.linalg.matrix_rank(np.array(prods), tol=1e-9)
    print(f"{k:3d} {n:4d} {n*n:5d} {2**k:5d} {rk:18d} {str(n*n >= 2**k):>9}")

print("\n=== (B') the bound: 4 mutually anticommuting elements need n >= 4 ===")
print("  nonempty Clifford products are traceless (k even), so the 2^k products")
print("  are linearly independent in M_n(C), forcing n^2 >= 2^k = 16, i.e. n >= 4.")
G4 = cliff(4)
def prod(G, S, n):
    M = np.eye(n, dtype=complex)
    for a in S: M = M @ G[a]
    return M
tr = [abs(np.trace(prod(G4, S, 4)))
      for r in range(1, 5) for S in itertools.combinations(range(4), r)]
print(f"  max |trace| over the 15 nonempty products in M4(C): {max(tr):.2e}")

print("\n=== (B'') numerical search for 4 anticommuting elements in M2(C), M3(C) ===")
rng = np.random.default_rng(0)
def residual(V, n, k):
    G = [V[i].reshape(n, n) for i in range(k)]
    r = 0.0
    for a in range(k):
        r += np.sum(np.abs(G[a]@G[a] - np.eye(n))**2)
        for b in range(a+1, k):
            r += np.sum(np.abs(G[a]@G[b] + G[b]@G[a])**2)
    return r
from scipy.optimize import minimize
for n in (2, 3, 4):
    best = np.inf
    for trial in range(40):
        x0 = rng.normal(size=2*4*n*n)
        f = lambda x: residual((x[:4*n*n]+1j*x[4*n*n:]).reshape(4, n*n), n, 4)
        res = minimize(f, x0, method="L-BFGS-B", options={"maxiter": 3000})
        best = min(best, res.fun)
    print(f"  M{n}(C): best residual over 40 restarts = {best:.3e}   "
          f"{'SOLUTION EXISTS' if best < 1e-10 else 'NO SOLUTION'}")

print("\n=== (C) direct sums cannot beat it ===")
print("  projection to a simple block is an algebra homomorphism, so each block")
print("  independently needs 4 anticommuting elements, hence n_i >= 4.")
print("  minimal complex dimension: one block, M4(C), dim 16.")
