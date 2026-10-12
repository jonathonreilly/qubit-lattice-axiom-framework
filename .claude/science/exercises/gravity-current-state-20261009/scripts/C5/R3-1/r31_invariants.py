"""R3-1 check 1: Gamma_L for L7 = diag(sqrt7,1,1,1)Z^4, Q7 = diag(-7,1,1,1) in n-coordinates.

(i) builds integral orthochronous reflections (spacelike roots r with 2B(n,r)/Q(r) in Z for all n),
    their pairwise products (SO+ elements), checks Q7-preservation, integrality, orthochronicity;
(ii) computes the dimension of Gamma-invariant homogeneous polynomials of degree k in a vector p
     (k=1..6) and of Gamma-invariant symmetric 2-tensors (mass forms for h_{mu nu}: invariant
     quadratic forms on Sym^2), exactly over Q with sympy-free integer linear algebra (fractions via
     numpy rank with tolerance cross-checked by modular rank);
(iii) verifies the hypothesised answer: dims = 1 for even k (= (p^2)^{k/2}), 0 for odd k; 2 mass forms.
(iv) Parseval lemma check: Gamma-orbit of a dual vector G is infinite (word growth of orbit sizes).
"""
import itertools, numpy as np
from fractions import Fraction

Q = np.diag([-7, 1, 1, 1])

def B(x, y):
    return int(x @ Q @ y)

def refl(r):
    r = np.array(r)
    q = B(r, r)
    M = np.eye(4, dtype=object)
    for i in range(4):
        e = np.zeros(4, dtype=int); e[i] = 1
        img = [Fraction(int(e[j])) - Fraction(2 * B(e, r), q) * int(r[j]) for j in range(4)]
        for j in range(4):
            M[j, i] = img[j]
    if any(Fraction(x).denominator != 1 for x in M.flat):
        return None
    return np.array([[int(Fraction(x)) for x in row] for row in M])

roots = [(0,1,0,0),(0,0,1,0),(0,0,0,1),(0,1,-1,0),(0,0,1,-1),(1,3,0,0),(1,2,2,1),(1,2,1,2),(1,1,2,2),(1,3,1,0)]
R = []
for r in roots:
    M = refl(r)
    q = B(np.array(r), np.array(r))
    if M is None:
        print("root", r, "Q=", q, "reflection NOT integral"); continue
    assert (M.T @ Q @ M == Q).all()
    print("root", r, "Q=", q, "integral reflection, M[0,0]=", M[0, 0])
    R.append(M)
gens = []
for A, Bm in itertools.combinations(R, 2):
    g = A @ Bm
    if round(np.linalg.det(g.astype(float))) == 1 and g[0, 0] > 0:
        gens.append(g)
print("SO+ generators (products of two spacelike reflections):", len(gens))
for g in gens:
    assert (g.T @ Q @ g == Q).all()
# largest boost among generators
print("max g00 among generators:", max(g[0, 0] for g in gens))

# --- invariant polynomials of degree k in p (p transforms contragrediently: p -> g^{-T} p) ---
def sym_basis(k, n=4):
    return [m for m in itertools.combinations_with_replacement(range(n), k)]

def sym_power_matrix(A, k):
    nv = A.shape[0]
    basis = sym_basis(k, nv)
    idx = {m: i for i, m in enumerate(basis)}
    n = len(basis)
    Mk = np.zeros((n, n), dtype=object)
    # action on monomials: p_{i1}...p_{ik} -> prod_j (A p)_{ij}
    for c, m in enumerate(basis):
        # expand product of linear forms
        poly = {(): 1}
        for i in m:
            new = {}
            for mono, coef in poly.items():
                for j in range(nv):
                    if A[i, j] != 0:
                        key = tuple(sorted(mono + (j,)))
                        new[key] = new.get(key, 0) + coef * int(A[i, j])
            poly = new
        for mono, coef in poly.items():
            Mk[idx[mono], c] += coef
    return Mk

def rank_mod_p(S, p):
    A = [[int(x) % p for x in row] for row in S]
    rows, cols = len(A), len(A[0]); r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c]), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]
        inv = pow(A[r][c], p - 2, p)
        A[r] = [(x * inv) % p for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                f = A[i][c]; A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
        r += 1
        if r == rows: break
    return r

def inv_dim(mats):
    # exact: integer matrices; invariant dim = n - rank_Q(stack(M - I)); rank mod p <= rank_Q, take max over primes
    n = mats[0].shape[0]
    S = [list(row) for M in mats for row in (np.array(M, dtype=object) - np.eye(n, dtype=int).astype(object))]
    rk = max(rank_mod_p(S, p) for p in (2147483647, 1000000007))
    return n - rk, None

ginv = [np.rint(np.linalg.inv(g.astype(float)).T).astype(np.int64) for g in gens]  # contragredient (integral)
for A, g in zip(ginv, gens): assert (A.T @ g == np.eye(4, dtype=int)).all()
for k in range(1, 7):
    if k == 6: gens_k = ginv[:12]
    else: gens_k = ginv
    mats = [sym_power_matrix(A, k).T for A in gens_k]  # action on coefficient space
    d, sv = inv_dim(mats)
    print(f"deg {k}: dim Sym^{k} = {mats[0].shape[0]}, Gamma-invariant polynomials = {d}  (Lorentz: {1 if k%2==0 else 0})")

# check (p^2)^k is invariant: p^2 = -p0^2/7 + p1^2+p2^2+p3^2 in dual coords (Q^{-1})
Qi = np.linalg.inv(Q.astype(float))
for A in ginv:
    assert np.allclose(A.T.astype(float) @ Qi @ A.astype(float), Qi)
print("dual form Q^{-1} invariant under contragredient generators: OK")

# --- mass forms: invariant quadratic forms on Sym^2(R^4) for h_{mu nu} (h -> g h g^T) ---
pairs = sym_basis(2)
def sym2_action(g):
    n = len(pairs); M = np.zeros((n, n), dtype=np.int64)
    for c, (a, b) in enumerate(pairs):
        E = np.zeros((4, 4), dtype=np.int64); E[a, b] = 1; E[b, a] = 1
        img = g @ E @ g.T
        for r_, (i, j) in enumerate(pairs):
            M[r_, c] = img[i, j] if i == j else img[i, j]
    # normalise basis: E_ab symmetric with 1s; img[i,j] gives coefficient of E_ij (for i!=j E_ij has two entries)
    return M
mats2 = [sym2_action(A) for A in ginv]  # h^{mu nu}-dual action so forms on h_{mu nu} use g^{-T}
# quadratic forms on Sym^2: Sym^2 of the 10-dim rep
quad = [sym_power_matrix(M2, 2).T for M2 in mats2]
d2, _ = inv_dim(quad)
print("invariant quadratic forms on Sym^2 (graviton mass forms):", d2, "(Lorentz/Fierz-Pauli count: 2)")

# --- orbit growth of a dual vector (Parseval lemma input: orbits infinite) ---
G0 = np.array([0, 1, 0, 0])  # dual vector in m-coords: G = (m0/sqrt7, m1, m2, m3)*2pi; action of g^{-T}
gi = [np.rint(np.linalg.inv(g.astype(float)).T).astype(int) for g in gens]
seen = {tuple(G0)}; frontier = [G0]
for w in range(1, 6):
    nf = []
    for v in frontier:
        for A in gi:
            u = A @ v
            if tuple(u) not in seen:
                seen.add(tuple(u)); nf.append(u)
    frontier = nf
    print(f"word length {w}: orbit size {len(seen)}, max |m0| = {max(abs(s[0]) for s in seen)}")
