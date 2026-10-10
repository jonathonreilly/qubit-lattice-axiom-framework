"""Lane RN / L1: Yee-Maxwell.  Necessary condition for (E)+(M) with ONE P: the total energy current
P_tot = d/dt D, D_i = sum_x x_i T00(x), must be conserved: d^2 D/dt^2 = 0 on the physical (Gauss) subspace.
T00 at sites with symmetric placement (link energy 1/2 to each end, plaquette energy 1/4 to each corner).
Computed on an L^3 torus via minimum-image first moments of the local forms F(x) = d^2 T00(x)/dt^2
(exact for L > 2*range).  Scalar control included.
"""
import numpy as np
import scipy.sparse as sp

AX = (0, 1, 2)
L = 6
V = L**3
idx = np.arange(V).reshape(L, L, L)
coords = np.array([(a, b, c) for a in range(L) for b in range(L) for c in range(L)])


def site(x):
    return idx[x[0] % L, x[1] % L, x[2] % L]


def link(x, j):
    return 3 * site(x) + j


E3 = np.eye(3, dtype=int)
# curl: plaquette (x; i<j) -> A_i(x) + A_j(x+e_i) - A_i(x+e_j) - A_j(x)
plaqs = [(i, j) for i in AX for j in AX if i < j]
rows, cols, vals = [], [], []
for s, x in enumerate(coords):
    for pi_, (i, j) in enumerate(plaqs):
        p = 3 * s + pi_
        for l, v in ((link(x, i), 1), (link(x + E3[i], j), 1), (link(x + E3[j], i), -1), (link(x, j), -1)):
            rows.append(p); cols.append(l); vals.append(v)
C = sp.coo_matrix((vals, (rows, cols)), shape=(3 * V, 3 * V)).tocsr()
nl = 3 * V
Om = sp.bmat([[None, sp.identity(nl)], [-sp.identity(nl), None]]).tocsr()
H = sp.block_diag([C.T @ C, sp.identity(nl)]).tocsr()  # 1/2 Psi^T H Psi, Psi=(A,E)


def pb(A, B):
    return (A @ Om @ B - B @ Om @ A).tocsr()


def T00_max(s):
    x = coords[s]
    r, c, v = [], [], []
    def add(vec, w):  # Q += w * (vec.Psi)^2  -> A += 2 w vec vec^T
        for a, va in vec.items():
            for b, vb in vec.items():
                r.append(a); c.append(b); v.append(2 * w * va * vb)
    for j in AX:  # E energy of links touching x
        for y in (x, x - E3[j]):
            add({nl + link(y, j): 1.0}, 0.5 * 0.5)
    for (i, j) in plaqs:  # plaquettes with corner x: base points x, x-e_i, x-e_j, x-e_i-e_j
        for y in (x, x - E3[i], x - E3[j], x - E3[i] - E3[j]):
            vec = {}
            for l, s_ in ((link(y, i), 1), (link(y + E3[i], j), 1), (link(y + E3[j], i), -1), (link(y, j), -1)):
                vec[l] = vec.get(l, 0) + s_
            add(vec, 0.5 * 0.25)
    return sp.coo_matrix((v, (r, c)), shape=(2 * nl, 2 * nl)).tocsr()


def pos_of_var(a):
    l = a % nl
    return coords[l // 3] + 0.5 * E3[l % 3]


def minimg(d):
    return (d + L / 2) % L - L / 2


def second_moment_check(Tfun, Hm, Omega, nvar, posfun, physP=None):
    Ddd = [sp.csr_matrix((nvar, nvar)) for _ in AX]
    for s in range(V):
        T = Tfun(s)
        F = pb(pb(T, Hm), Hm) if Omega is None else None
        F = F.tocoo()
        a_pos = np.array([posfun(a) for a in F.row])
        d = minimg(coords[s][None, :] - a_pos)
        for i in AX:
            Ddd[i] = Ddd[i] + sp.coo_matrix((F.data * d[:, i], (F.row, F.col)), shape=(nvar, nvar)).tocsr()
    out = []
    for i in AX:
        M = Ddd[i].toarray()
        if physP is not None:
            M = physP.T @ M @ physP
        out.append(np.max(np.abs(M)))
    return out


# physical subspace: A transverse (gauge fixed) and E transverse (Gauss law): projector onto range of C^T
CT = C.T.toarray()
U, sv, _ = np.linalg.svd(CT, full_matrices=False)
Ut = U[:, sv > 1e-9]  # transverse link fields (range of curl^T)
Pphys = np.block([[Ut, np.zeros_like(Ut)], [np.zeros_like(Ut), Ut]])
print(f"Yee Maxwell L={L}: transverse dimension {Ut.shape[1]} of {nl} link fields")
res = second_moment_check(T00_max, H, None, 2 * nl, pos_of_var, Pphys)
print("max |d^2 D_i/dt^2| on the physical subspace (i=x,y,z):", [f"{r:.2e}" for r in res])
full = second_moment_check(T00_max, H, None, 2 * nl, pos_of_var, None)
print("  (on the full unconstrained space:", [f"{r:.2e}" for r in full], ")")
# sanity: the total energy is conserved and sum T00 = H/2-form
Ht = sum(T00_max(s) for s in range(V))
print("sum_x T00(x) form equals H form:", abs(Ht - H).max())

# ---- scalar control with the same machinery ----
m = 0.6
Hs_rows = []
Lap = sp.lil_matrix((V, V))
for s, x in enumerate(coords):
    for j in AX:
        for y in (x + E3[j], x - E3[j]):
            Lap[s, site(y)] += 1
        Lap[s, s] -= 2
Lap = Lap.tocsr()
Hs = sp.block_diag([(-Lap + m * m * sp.identity(V)), sp.identity(V)]).tocsr()
Oms = sp.bmat([[None, sp.identity(V)], [-sp.identity(V), None]]).tocsr()


def T00_sc(s):
    x = coords[s]
    r, c, v = [], [], []
    def add(vec, w):
        for a, va in vec.items():
            for b, vb in vec.items():
                r.append(a); c.append(b); v.append(2 * w * va * vb)
    add({V + s: 1.0}, 0.5); add({s: 1.0}, 0.5 * m * m)
    for j in AX:
        for y in (x, x - E3[j]):
            add({site(y + E3[j]): 1.0, site(y): -1.0}, 0.25)
    return sp.coo_matrix((v, (r, c)), shape=(2 * V, 2 * V)).tocsr()


def pbs(A, B):
    return (A @ Oms @ B - B @ Oms @ A).tocsr()


Dd = [sp.csr_matrix((2 * V, 2 * V)) for _ in AX]
for s in range(V):
    F = pbs(pbs(T00_sc(s), Hs), Hs).tocoo()
    a_pos = coords[F.row % V]
    d = minimg(coords[s][None, :] - a_pos)
    for i in AX:
        Dd[i] = Dd[i] + sp.coo_matrix((F.data * d[:, i], (F.row, F.col)), shape=(2 * V, 2 * V)).tocsr()
print("scalar control: max|d^2 D/dt^2| =", [f"{abs(M).max():.2e}" for M in Dd])
