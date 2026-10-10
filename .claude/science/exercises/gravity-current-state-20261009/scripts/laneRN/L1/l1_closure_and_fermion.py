"""Lane RN / L1 part 3.
 (a) O(kappa) diagnostic: does the free-lattice-scalar constraint algebra close by itself?
     {P[xi],P[eta]}, {T00[mu],T00[nu]}, {P[xi],T00[nu]} fitted by c-number combinations of
     P_j(x) and T00(x) (the matter parts of the constraints). Continuum: exact (Dirac algebra).
 (b) staggered fermion: (E) energy continuity with P_j = -1/2{I_j, h}; total P conserved;
     per-quantum P symbol; the antisymmetric (spin) obstruction to a symmetric T is NOT searched here.
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import lsqr

AX = (0, 1, 2)
rng = np.random.default_rng(7)


def build(L, m):
    V = L**3
    idx = np.arange(V).reshape(L, L, L)
    def site(x):
        return idx[x[0] % L, x[1] % L, x[2] % L]
    def ephi(x):
        return site(x)
    def epi(x):
        return V + site(x)
    ent_T, ent_P = [], []  # lists of (rows, cols, vals) per density
    coords = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]
    def form(terms):
        # terms: list of (alpha, u(dict), w(dict)); Q = sum alpha (u.Psi)(w.Psi); A = sum alpha (u w^T + w u^T)
        r, c, v = [], [], []
        for al, u, w in terms:
            for i, ui in u.items():
                for j, wj in w.items():
                    r += [i, j]; c += [j, i]; v += [al * ui * wj, al * ui * wj]
        return sp.coo_matrix((v, (r, c)), shape=(2 * V, 2 * V)).tocsr()
    T00, P = [], [[], [], []]
    for x in coords:
        x = np.array(x)
        terms = [(0.5, {epi(x): 1}, {epi(x): 1}), (0.5 * m * m, {ephi(x): 1}, {ephi(x): 1})]
        for j in AX:
            e = np.eye(3, dtype=int)[j]
            for y in (x, x - e):
                u = {ephi(y + e): 1.0, ephi(y): -1.0}
                terms.append((0.25, u, u))
        T00.append(form(terms))
        for j in AX:
            e = np.eye(3, dtype=int)[j]
            u = {epi(x): 0.5}
            u[epi(x + e)] = u.get(epi(x + e), 0) + 0.5
            w = {ephi(x + e): 1.0}
            w[ephi(x)] = w.get(ephi(x), 0) - 1.0
            P[j].append(form([(1.0, u, w)]))
    Om = sp.bmat([[None, sp.identity(V)], [-sp.identity(V), None]]).tocsr()
    return V, T00, P, Om


def pb(A, B, Om):
    return (A @ Om @ B - B @ Om @ A).tocsr()


def fit(C, basis):
    """least-squares fit of sparse C by c-number combination of sparse basis matrices; rel. residual."""
    rows = set(zip(*C.nonzero()))
    for Bm in basis:
        rows |= set(zip(*Bm.nonzero()))
    rows = sorted(rows)
    pos = {rc: i for i, rc in enumerate(rows)}
    r_, c_, v_ = [], [], []
    for k, Bm in enumerate(basis):
        Bc = Bm.tocoo()
        for i, j, v in zip(Bc.row, Bc.col, Bc.data):
            r_.append(pos[(i, j)]); c_.append(k); v_.append(v)
    D = sp.coo_matrix((v_, (r_, c_)), shape=(len(rows), len(basis))).tocsr()
    Cc = C.tocoo()
    y = np.zeros(len(rows))
    for i, j, v in zip(Cc.row, Cc.col, Cc.data):
        y[pos[(i, j)]] += v
    sol = lsqr(D, y, atol=1e-14, btol=1e-14, iter_lim=20000)[0]
    res = np.linalg.norm(D @ sol - y) / np.linalg.norm(y)
    return res


def smooth(L, amp_scale=1.0):
    x = np.arange(L)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    ph = rng.uniform(0, 2 * np.pi, 3)
    return amp_scale * (np.cos(2 * np.pi * X / L + ph[0]) + 0.5 * np.sin(2 * np.pi * Y / L + ph[1])
                        + 0.3 * np.cos(2 * np.pi * Z / L + ph[2])).ravel()


print("=== (a) O(kappa) closure of the matter constraint algebra (free scalar m=0.6) ===")
for L, kind in ((5, "random"), (8, "smooth"), (12, "smooth")):
    V, T00, P, Om = build(L, 0.6)
    if kind == "random":
        xi = [rng.standard_normal(V) for _ in AX]; et = [rng.standard_normal(V) for _ in AX]
        mu = rng.standard_normal(V); nu = rng.standard_normal(V)
    else:
        xi = [smooth(L) for _ in AX]; et = [smooth(L) for _ in AX]; mu = smooth(L); nu = smooth(L)
    Pxi = sum(xi[j][x] * P[j][x] for j in AX for x in range(V))
    Pet = sum(et[j][x] * P[j][x] for j in AX for x in range(V))
    Tmu = sum(mu[x] * T00[x] for x in range(V))
    Tnu = sum(nu[x] * T00[x] for x in range(V))
    basis = [P[j][x] for j in AX for x in range(V)] + [T00[x] for x in range(V)]
    out = []
    for lab, A, B in (("{P,P}", Pxi, Pet), ("{T00,T00}", Tmu, Tnu), ("{P,T00}", Pxi, Tnu)):
        C = pb(A, B, Om)
        out.append(f"{lab}: rel. residual {fit(C, basis):.3f}")
    print(f"L={L:2d} ({kind:6s} test fields):", "; ".join(out))
print("(continuum control: all three close exactly onto P and T00 -- Dirac hypersurface algebra)")

print("\n=== (b) staggered fermion on L=6 torus: energy continuity with P_j = 1/2 {J_j, h} ===")
L = 6; V = L**3
idx = np.arange(V).reshape(L, L, L)
coords = np.array([(a, b, c) for a in range(L) for b in range(L) for c in range(L)])
for m in (0.0, 0.45):
    h = np.zeros((V, V), complex)
    for s, x in enumerate(coords):
        eta = [1, (-1) ** x[0], (-1) ** (x[0] + x[1])]
        for j in AX:
            y = x.copy(); y[j] = (y[j] + 1) % L
            t = idx[tuple(y)]
            h[s, t] += 0.5j * eta[j]; h[t, s] += -0.5j * eta[j]
        h[s, s] += m * (-1) ** x.sum()
    Pi = [np.diag((np.arange(V) == s).astype(float)) for s in range(V)]
    T00 = [0.5 * (Pi[s] @ h + h @ Pi[s]) for s in range(V)]
    # particle current on link (x, x+e_j):  I = -i (Pi_{x+e} h Pi_x - Pi_x h Pi_{x+e})  (sign fixed by check)
    def I(s, j):
        y = coords[s].copy(); y[j] = (y[j] + 1) % L; t = idx[tuple(y)]
        return 1j * (Pi[t] @ h @ Pi[s] - Pi[s] @ h @ Pi[t])  # J = -(the I of the first draft)
    def back(s, j):
        y = coords[s].copy(); y[j] = (y[j] - 1) % L; return idx[tuple(y)]
    Ij = {(s, j): I(s, j) for s in range(V) for j in AX}
    # check particle continuity  i[h,Pi_x] = sum_j (I_{x,j} - I_{x-e_j,j}) up to sign
    errN = max(np.max(np.abs(1j * (h @ Pi[s] - Pi[s] @ h) - sum(Ij[(s, j)] - Ij[(back(s, j), j)] for j in AX))) for s in range(V))
    Pj = {(s, j): 0.5 * (Ij[(s, j)] @ h + h @ Ij[(s, j)]) for s in range(V) for j in AX}
    dT = [1j * (h @ T00[s] - T00[s] @ h) for s in range(V)]
    errE = max(np.max(np.abs(dT[s] - sum(Pj[(s, j)] - Pj[(back(s, j), j)] for j in AX))) for s in range(V))
    Ptot = [sum(Pj[(s, j)] for s in range(V)) for j in AX]
    comm = max(np.max(np.abs(h @ Pt - Pt @ h)) for Pt in Ptot)
    # per-quantum symbol: eigen-decompose h, compare <P_tot> with -1/2 sin 2k_j  on plane-wave-like eigvecs
    Pd = np.linalg.eigvalsh(Ptot[0])
    kk = 2*np.pi*np.arange(L)/L
    target = np.sort(np.repeat(0.5*np.sin(2*kk), V//L))
    symerr = np.max(np.abs(np.sort(Pd) - target))
    print(f"m={m}: particle continuity err {errN:.1e}; energy continuity err {errE:.1e} (dT00/dt = div P, P = (1/2)(J h + h J));"
          f" ||[h, P_tot]|| = {comm:.1e}; spectrum of P_tot,x vs multiset (1/2) sin 2k_x: max dev {symerr:.1e}")
print("Symmetric T_ij for the fermion needs a local spin (Belinfante) term; not constructed in this probe.")
