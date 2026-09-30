"""Why the projected Majorana mass vanishes for every class: the 8 KS zero modes carry a real
8-dim representation R_g of the (projective) covariance group.  A first-order Majorana mass
matrix M must be an R-invariant ANTISYMMETRIC form.  Count them (and the symmetric ones)."""
import sys, numpy as np
src = open('verify_and_bdg.py').read().split('print("\\n== step 2')[0].replace('print(', '(lambda *a, **k: None)(')
sys.argv = ['x', sys.argv[1] if len(sys.argv) > 1 else '8']
exec(src)
h = np.zeros((N, N))
for (i, j), e in hop.items(): h[i, j] = e
w, V = np.linalg.eigh(h)
Z = V[:, np.abs(w) < 1e-9]
k = Z.shape[1]
print("L =", L, " zero modes:", k)
Rs = []
for name, (perm, s) in gens.items():
    U = np.zeros((N, N))
    U[perm, np.arange(N)] = s          # (U f)(perm[v]) = s_v f(v)
    assert np.allclose(U @ h, h @ U)   # symmetry of the hopping
    R = Z.T @ U @ Z
    assert np.allclose(R @ R.T, np.eye(k), atol=1e-9), name
    Rs.append((name, R))
def inv_dim(kind):
    # basis of symmetric / antisymmetric k x k matrices
    basis = []
    for a in range(k):
        for b in range(a, k):
            E = np.zeros((k, k))
            if kind == 'sym':
                E[a, b] = 1; E[b, a] = 1
            else:
                if a == b: continue
                E[a, b] = 1; E[b, a] = -1
            basis.append(E)
    B = np.array([E.flatten() for E in basis]).T  # k^2 x nb
    rows = []
    for name, R in Rs:
        rows.append((np.kron(R, R) - np.eye(k * k)) @ B)
    Mx = np.vstack(rows)
    sv = np.linalg.svd(Mx, compute_uv=False)
    return int(np.sum(sv < 1e-8)) + max(0, B.shape[1] - len(sv))
print("invariant symmetric bilinear forms on the light sector :", inv_dim('sym'))
print("invariant ANTIsymmetric bilinear forms on the light sector:", inv_dim('anti'))
# commutant dimension (all k x k X with R X = X R)
rows = [np.kron(np.eye(k), R) - np.kron(R.T, np.eye(k)) for name, R in Rs]
sv = np.linalg.svd(np.vstack(rows), compute_uv=False)
print("commutant dimension of the light-sector rep:", int(np.sum(sv < 1e-8)))
