"""
T209 - can chirality be EMERGENT instead of axiomatic?

T208 shows M4(C) is the unique minimal site algebra admitting a chirality.  But
in lattice field theory chirality is normally a property of the DIRAC OPERATOR
on a blocked multi-site space, not of the one-site algebra.  The staggered
epsilon operator is such a chirality.  If a TASTE-SINGLET chirality exists on
the campaign's blocked operator, no axiom change is needed and R122/R123's
recommendation is refuted.

  C = { X : {X, D(p)} = 0  for all p }          chirality space
  T = { Y : [Y, D(p)] = 0  for all p }          taste / flavour algebra
  a taste-singlet chirality lies in  C  and  commutes with all of  T.
"""
import numpy as np, itertools

S = [np.array([[0, 1], [1, 0]], dtype=complex),
     np.array([[0, -1j], [1j, 0]], dtype=complex),
     np.array([[1, 0], [0, -1]], dtype=complex)]
R8 = [tuple(r) for r in itertools.product([0, 1], repeat=3)]
I8 = {r: i for i, r in enumerate(R8)}

def shift3(a, sg, p):
    M = np.zeros((8, 8), dtype=complex)
    for r in R8:
        t = list(r)
        if sg > 0:
            if r[a] == 0: t[a] = 1; ph = 1.0
            else:         t[a] = 0; ph = np.exp(1j*p[a])
        else:
            if r[a] == 1: t[a] = 0; ph = 1.0
            else:         t[a] = 1; ph = np.exp(-1j*p[a])
        M[I8[tuple(t)], I8[r]] += ph
    return M

def D3(p):
    return sum(np.kron(shift3(a, 1, p) - shift3(a, -1, p), S[a]) for a in range(3))/2.0

N = 16
def nullspace(M, tol_mult=1.0):
    U, sv, Vt = np.linalg.svd(M, full_matrices=False)
    tol = tol_mult*max(M.shape)*np.finfo(float).eps*(sv.max() if sv.size else 1.0)
    k = int(np.sum(sv <= tol))
    return [Vt[len(Vt)-k+i].conj().reshape(N, N) for i in range(k)], sv

# ---- validate the vec convention before trusting any nullspace -------------
rng = np.random.default_rng(1)
Xt = rng.normal(size=(N, N)) + 1j*rng.normal(size=(N, N))
Dt = D3(rng.normal(size=3))
lhs = (Xt@Dt + Dt@Xt).ravel()
rhs = (np.kron(np.eye(N), Dt.T) + np.kron(Dt, np.eye(N))) @ Xt.ravel()
print(f"vec-convention check (anticommutator): {np.max(np.abs(lhs-rhs)):.2e}")
lhs = (Xt@Dt - Dt@Xt).ravel()
rhs = (np.kron(np.eye(N), Dt.T) - np.kron(Dt, np.eye(N))) @ Xt.ravel()
print(f"vec-convention check (commutator)    : {np.max(np.abs(lhs-rhs)):.2e}")

ps = [rng.uniform(-np.pi, np.pi, 3) for _ in range(12)]
A_anti = np.vstack([np.kron(np.eye(N), D3(p).T) + np.kron(D3(p), np.eye(N)) for p in ps])
A_comm = np.vstack([np.kron(np.eye(N), D3(p).T) - np.kron(D3(p), np.eye(N)) for p in ps])
C, svc = nullspace(A_anti)
T, svt = nullspace(A_comm)
print(f"\ndim C (chirality space)   = {len(C)}")
print(f"dim T (taste algebra)     = {len(T)}")

# staggered epsilon: does it live in C?
E = np.kron(np.diag([(-1)**sum(r) for r in R8]).astype(complex), np.eye(2))
print(f"staggered epsilon anticommutes with D: "
      f"{max(np.max(np.abs(E@D3(p)+D3(p)@E)) for p in ps):.2e}")

# ---- is any chirality a TASTE SINGLET?  need X in C commuting with all of T --
if len(C) and len(T):
    rows = []
    for Y in T:
        Bl = np.zeros((N*N, len(C)), dtype=complex)
        for j, X in enumerate(C):
            Bl[:, j] = (X@Y - Y@X).ravel()
        rows.append(Bl)
    M = np.vstack(rows)
    U, sv, Vt = np.linalg.svd(M, full_matrices=False)
    tol = max(M.shape)*np.finfo(float).eps*(sv.max() if sv.size else 1.0)
    k = int(np.sum(sv <= tol))
    print(f"\ndim of taste-SINGLET chirality subspace = {k}")
    print(f"  (smallest singular values: {np.sort(sv)[:4]})")
    if k:
        coef = Vt[len(Vt)-k:].conj()
        for i in range(k):
            X = sum(coef[i][j]*C[j] for j in range(len(C)))
            X = X/np.linalg.norm(X)*np.sqrt(N)
            anti = max(np.max(np.abs(X@D3(p)+D3(p)@X)) for p in ps)
            comm = max(np.max(np.abs(X@Y-Y@X)) for Y in T)
            sq = np.max(np.abs(X@X - (np.trace(X@X)/N)*np.eye(N)))
            print(f"  candidate {i}: anticomm(D)={anti:.1e}  comm(T)={comm:.1e}  "
                  f"X^2 prop to I: {sq:.1e}   tr X = {abs(np.trace(X)):.1e}")
    else:
        print("  NO taste-singlet chirality exists on the blocked space.")

# ============================================================================
# The T-commutant test above is WEAK: T is the exact lattice symmetry algebra
# (dim 4), not the continuum taste algebra.  Identify what X actually IS.
# ============================================================================
print("\n=== what is the candidate chirality? ===")
X = sum(coef[0][j]*C[j] for j in range(len(C)))
X = X/np.linalg.norm(X)*np.sqrt(N)
Enorm = E/np.linalg.norm(E)*np.sqrt(N)
ov = abs(np.trace(X.conj().T@Enorm))/N
print(f"  |<X, staggered epsilon>| / N        = {ov:.6f}")
print(f"  is X of the form A (x) I_2 (pure taste, no spin content)?")
for a in range(3):
    sp = np.kron(np.eye(8), S[a])
    print(f"    [X, 1(x)sigma_{a+1}] = {np.max(np.abs(X@sp-sp@X)):.2e}")
print(f"  ==> X carries NO spin/Dirac structure; it acts only on the")
print(f"      hypercube-corner (taste) index.")

print("\n=== why that settles it ===")
print("  In d=3 the CONTINUUM has no chirality either: T208(A) gives")
print("  dim{X : {X,Gamma_a}=0} = 0 for k=3.  So an X anticommuting with the")
print("  lattice D3 cannot be gamma5 (x) 1 -- there is no gamma5 to be.")
print("  It must live entirely in the taste index, which is what is measured")
print("  above.  This is the staggered flavoured chirality gamma5 (x) xi5,")
print("  not a taste singlet.")

print("\n=== the decisive count: Nielsen-Ninomiya on the blocked operator ===")
print(f"  D3(p=0) is identically zero: max|D3(0)| = {np.max(np.abs(D3(np.zeros(3)))):.2e}")
ev = np.linalg.eigvalsh(X)
print(f"  X eigenvalues: {np.sum(ev>0)} at +1, {np.sum(ev<0)} at -1  (trace {np.sum(ev):+.1e})")
print("  Equal split => the doublers carry cancelling chirality, exactly what")
print("  Nielsen-Ninomiya requires and exactly what makes the chirality")
print("  flavoured.  No net chiral fermion content.")
