"""A14 check N3: does a sparse set of records gap the long-wavelength ripple of a
SWAP-type (Heisenberg) change?  Supplied toy, nothing adopted.

Single-excitation sector over the all-0 reference, change H = sum_bonds SWAP:
  bulk: H_rel = A - z  (lattice Laplacian, top eigenvalue 0 at k = 0: the uniform
        re-orientation of the shared possibilities, protected by SU(2)).
Record at x with content a; compressed bond term on neighbour y is |a><a|_y (A8 B1).
  content 0 (= reference): excitation at y keeps diagonal -z, loses the hop  -> Dirichlet at x
  content 1 (= ripple)   : excitation at y gets diagonal -z+2 (relative), loses the hop
  'neutral' (hypothetical, no field): diagonal -(z-1) (graph Laplacian, Neumann).
Prediction (Dirichlet, first order): top eigenvalue = -rho/G(0) = -rho*Cap1, Cap1 = 3.9568.
Neumann: top eigenvalue 0 exactly (uniform mode survives); measure the k^2 stiffness.
"""
import sys, time, signal
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

signal.alarm(58)
L = int(sys.argv[1]); rhos = [float(x) for x in sys.argv[2].split(",")]; nseed = int(sys.argv[3])
N = L**3
idx = np.arange(N).reshape(L, L, L)
rows, cols = [], []
for ax in range(3):
    nb = np.roll(idx, -1, axis=ax)
    rows.append(idx.ravel()); cols.append(nb.ravel())
rows = np.concatenate(rows); cols = np.concatenate(cols)
A = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, N))
A = (A + A.T).tocsr()
z = 6
t0 = time.time()
Cap1 = 1/0.252731009858
kmin = 2*np.pi/L; lam1 = 2 - 2*np.cos(kmin)
print(f"L={L} seeds={nseed}; Cap1=1/G(0)={Cap1:.4f}; clean first k^2 mode = -{lam1:.5f}")
print(" rho    Dirichlet top/rho   (pred -Cap1 = -3.957)   content-1 top/rho   Neumann: top, stiffness c^2 (6 lowest k modes)")
for rho in rhos:
    out = []
    for s in range(nseed):
        rng = np.random.default_rng(500 + s)
        wall = rng.random(N) < rho
        free = np.where(~wall)[0]
        Af = A[free][:, free]
        nwall_nb = np.asarray(A[free][:, np.where(wall)[0]].sum(axis=1)).ravel()   # walls adjacent to each free site
        res = []
        # Dirichlet: diagonal -z everywhere
        H = Af - z*sp.identity(len(free))
        e = sla.eigsh(H.tocsc(), k=1, which='LA', return_eigenvectors=False)
        res.append(e.max())
        # content-1 walls: diagonal -z + 2*(number of adjacent walls)
        H1 = Af + sp.diags(-z + 2.0*nwall_nb)
        e1 = sla.eigsh(H1.tocsc(), k=1, which='LA', return_eigenvectors=False)
        res.append(e1.max())
        # Neumann (graph Laplacian of the diluted graph)
        deg = np.asarray(Af.sum(axis=1)).ravel()
        HN = Af - sp.diags(deg)
        eN = np.sort(sla.eigsh(HN.tocsc(), k=7, which='LA', return_eigenvectors=False))[::-1]
        res.append(eN[0]); res.append(-np.mean(eN[1:7])/lam1)
        out.append(res)
    out = np.array(out); m = out.mean(axis=0); sd = out.std(axis=0)/np.sqrt(nseed)
    print(f" {rho:.3f}   {m[0]/rho:+8.3f} +- {sd[0]/rho:.3f}                       {m[1]/rho:+8.3f} +- {sd[1]/rho:.3f}      {m[2]:+.1e}, c^2 = {m[3]:.4f} +- {sd[3]:.4f}  (1-c^2)/rho = {(1-m[3])/rho:.3f}")
print(f"elapsed {time.time()-t0:.1f}s")
