"""Scalar (P1 Whitney 0-forms) and Maxwell (Whitney 1-forms) on the same 4D Kuhn path complex
with flat metric g0 (edge lengths^2 = v^T g0 v). Bloch symbols; leading order vs continuum;
on-shell O(k^4) dispersion vs the Regge TT law  w^2 = k^2 [1 - k^2 (1 + sum n^4)/12]."""
import itertools, numpy as np

SIMPLICES = []
for s in itertools.permutations(range(4)):
    vs = [np.zeros(4, int)]
    for a in s:
        v = vs[-1].copy(); v[a] += 1; vs.append(v)
    SIMPLICES.append(vs)
DIRS = [np.array(v) for v in itertools.product([0, 1], repeat=4) if any(v)]
DIDX = {tuple(v): i for i, v in enumerate(DIRS)}

def edge(p, q):   # edge from p to q (q-p is 0/1); returns (class, anchor, sign)
    d = q - p
    if tuple(d) in DIDX: return DIDX[tuple(d)], p, 1
    return DIDX[tuple(-d)], q, -1

def simplex_geom(vs, g0):
    E = np.array([vs[i] - vs[0] for i in range(1, 5)], float)   # rows = edge vectors
    G = E @ g0 @ E.T
    vol = np.sqrt(np.linalg.det(G)) / 24.0
    return E, vol

def scalar_symbol(k, g0):
    """sum_simplices vol * |grad phi|^2_g0 with phi = P1 interpolant of e^{ik.x}; one site per cell."""
    gi = np.linalg.inv(g0); S = 0j
    for vs in SIMPLICES:
        E, vol = simplex_geom(vs, g0)
        ph = np.array([np.exp(1j * k @ v) for v in vs])
        dphi = ph[1:] - ph[0]                     # = E @ grad
        grad = np.linalg.solve(E, dphi)
        S += vol * np.conj(grad) @ gi @ grad
    return S.real

def maxwell_symbol(k, g0):
    """15x15 Hermitian form on edge amplitudes a_c (per cell) of sum vol*|F|^2_g0/2, F=dA Whitney."""
    gi = np.linalg.inv(g0); Q = np.zeros((15, 15), complex)
    for vs in SIMPLICES:
        E, vol = simplex_geom(vs, g0)
        # F(e_i, e_j) for edge vectors from vertex 0: line integral around triangle (0,i,j)
        rows = []
        for i in range(1, 5):
            for j in range(i + 1, 5):
                r = np.zeros(15, complex)
                for (p, q) in [(0, i), (i, j), (j, 0)]:
                    c, anc, sg = edge(vs[p], vs[q])
                    r[c] += sg * np.exp(1j * k @ anc)
                rows.append(((i - 1, j - 1), r))
        # F_ab in edge basis (4x4 antisym, each entry a linear functional of a)
        Fe = np.zeros((4, 4, 15), complex)
        for (a, b), r in rows: Fe[a, b] = 2 * r; Fe[b, a] = -2 * r
        Einv = np.linalg.inv(E)                    # F_mu nu = Einv[mu,a] Fe[a,b] Einv[nu,b]
        F = np.einsum('ma,abc,nb->mnc', Einv, Fe, Einv)
        # |F|^2/2 = 1/2 F_mn F_rs g^mr g^ns
        Q += 0.5 * vol * np.einsum('mnc,rsd,mr,ns->cd', np.conj(F), F, gi, gi)
    return Q

def line_map(k, g0):
    """continuum A_mu e^{ik.x} -> edge amplitudes: integral of A along edge (anchor phase x sinc)."""
    M = np.zeros((15, 4), complex)
    for c, v in enumerate(DIRS):
        z = k @ v; ph = 1.0 if abs(z) < 1e-14 else (np.exp(1j * z) - 1) / (1j * z)
        M[c] = ph * v
    return M

def maxwell_continuum(k, A, g0):
    gi = np.linalg.inv(g0); F = 1j * (np.outer(k, A) - np.outer(A, k))
    return 0.5 * np.real(np.einsum('mn,rs,mr,ns->', np.conj(F), F, gi, gi))

def dispersion_coeff(sym_fn, n, kmags=(0.04, 0.02, 0.01)):
    """Locate Euclidean on-shell omega (k_t = i omega at index 3) by root of det/smallest sv.
    Return alpha with omega^2 = k^2 (1 + alpha k^2)."""
    out = []
    for km in kmags:
        ks = km * np.asarray(n, float)
        def f(om):
            kk = np.array([ks[0], ks[1], ks[2], 1j * om])
            return sym_fn(kk)
        out.append((km, f))
    return out

if __name__ == '__main__':
    rng = np.random.default_rng(7)
    U = np.ones(4)
    for b in [0.0, 0.3]:
        g0 = np.eye(4) + b * np.outer(U, U); gi = np.linalg.inv(g0); sq = np.sqrt(np.linalg.det(g0))
        # scalar: leading symbol / (sqrt g * k g^-1 k)
        rs = []
        for _ in range(6):
            kd = rng.standard_normal(4); kd /= np.linalg.norm(kd)
            e = 1e-3; r = [scalar_symbol(s * kd, g0) / s**2 for s in (2 * e, e)]
            rs.append(((4 * r[1] - r[0]) / 3) / (sq * kd @ gi @ kd))
        print(f"b={b}: scalar leading / (sqrt g k.g^-1.k) over 6 dirs: {np.min(rs):.9f}..{np.max(rs):.9f}")
        rm = []
        for _ in range(6):
            kd = rng.standard_normal(4); kd /= np.linalg.norm(kd); A = rng.standard_normal(4)
            e = 1e-3; r = []
            for s in (2 * e, e):
                k = s * kd; M = line_map(k, g0); Q = maxwell_symbol(k, g0)
                r.append(np.real(np.conj(M @ A) @ Q @ (M @ A)) / maxwell_continuum(k, A, g0))
            rm.append((4 * r[1] - r[0]) / 3 / sq)
        print(f"b={b}: Maxwell (Whitney) leading / (sqrt g * continuum F^2/2) over 6 dirs: {np.min(rm):.9f}..{np.max(rm):.9f}")
