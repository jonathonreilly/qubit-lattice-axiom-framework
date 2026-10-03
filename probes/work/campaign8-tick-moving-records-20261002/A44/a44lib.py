"""A44 shared library (supplied toys; nothing adopted).

Pauli units throughout.  Rule on oriented bonds (x, x+e_a):
  h_J = s_x . s_y,   h_K = s^a_x s^a_y,   h_D = e_a . (s_x x s_y) = s^b_x s^c_y - s^c_x s^b_y, (a,b,c) cyclic.
Per-bond expectations e_J, e_K, e_D are averages over all 3N oriented bonds.

Partons: s_x = f_x^dag s f_x, one fermion per site.  Mean-field hop on (x, x+e_a):
  f_x^dag (t 1 + i lam s^a) f_{x+e_a} + h.c.   ("soldered" when t = 0; A43 route (d))
optionally kind="pi": scalar hop t * eta_a(x) with Kogut-Susskind signs (pi flux per plaquette).
Projected amplitude of a spin configuration (bit_i = 0 up, 1 down) = det Phi[2 i + bit_i, :].
"""
import itertools, numpy as np

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.diag([1., -1.]).astype(complex)
SIG = [SX, SY, SZ]
CYC = {0: (1, 2), 1: (2, 0), 2: (0, 1)}


class Cluster:
    """Sites of Z^3 modulo the superlattice spanned by the columns of T."""
    def __init__(self, T):
        self.T = np.array(T, int)
        self.Tinv = np.linalg.inv(self.T.astype(float))
        self.N = int(round(abs(np.linalg.det(self.T.astype(float)))))
        R = int(np.abs(self.T).sum()) + 1
        reps = set()
        for v in itertools.product(range(-R, R + 1), repeat=3):
            reps.add(tuple(self.canon(np.array(v))[0]))
        self.sites = sorted(reps)
        assert len(self.sites) == self.N, (len(self.sites), self.N)
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.X = np.array(self.sites)
        # oriented bonds (i, j, a, n) with x_i + e_a = x_j + T n
        self.bonds = []
        for i, s in enumerate(self.sites):
            for a in range(3):
                v = np.array(s) + np.eye(3, dtype=int)[a]
                rep, n = self.canon(v)
                self.bonds.append((i, self.idx[tuple(rep)], a, n))
        self.bi = np.array([b[0] for b in self.bonds]); self.bj = np.array([b[1] for b in self.bonds])
        self.ba = np.array([b[2] for b in self.bonds])

    def canon(self, v):
        c = self.Tinv @ v
        n = np.floor(c + 1e-9).astype(int)
        return v - self.T @ n, n


def cube(L):
    return Cluster(L * np.eye(3, dtype=int))


def mf_orbitals(cl, t, lam, twist=(np.pi, np.pi, np.pi), kind="sold"):
    """Lowest N of 2N mean-field orbitals; returns Phi (2N x N), gap at the filling level, all levels."""
    N = cl.N
    h = np.zeros((2 * N, 2 * N), complex)
    tw = np.array(twist, float)
    for (i, j, a, n) in cl.bonds:
        ph = np.exp(1j * (tw @ n))
        if kind == "sold":
            u = t * np.eye(2) + 1j * lam * SIG[a]
        elif kind == "pi":   # KS signs eta_1 = 1, eta_2 = (-1)^x1, eta_3 = (-1)^(x1+x2), scalar
            x = cl.sites[i]
            eta = [1, (-1) ** x[0], (-1) ** (x[0] + x[1])][a]
            u = t * eta * np.eye(2)
        else:
            raise ValueError(kind)
        h[2 * i:2 * i + 2, 2 * j:2 * j + 2] += u * ph
        h[2 * j:2 * j + 2, 2 * i:2 * i + 2] += (u * ph).conj().T
    assert np.allclose(h, h.conj().T)
    ev, V = np.linalg.eigh(h)
    return V[:, :N].copy(), ev[N] - ev[N - 1], ev


def klein_R(x):
    """SO(3) frame of the four-sublattice pi-rotation V_x = (i s1)^x1 (i s2)^x2 (i s3)^x3."""
    x1, x2, x3 = x
    return np.diag([(-1.) ** (x2 + x3), (-1.) ** (x1 + x3), (-1.) ** (x1 + x2)])


# ---------- exact (2^N) tools for N <= 16 ----------
def bits_table(N):
    b = np.arange(2 ** N, dtype=np.int64)
    return ((b[:, None] >> np.arange(N)[None, :]) & 1).astype(np.int8)


def projected_vector(Phi, bits, chunk=4096):
    N = Phi.shape[1]
    out = np.empty(bits.shape[0], complex)
    rows_base = 2 * np.arange(N)
    for s in range(0, bits.shape[0], chunk):
        rows = rows_base[None, :] + bits[s:s + chunk]
        out[s:s + chunk] = np.linalg.det(Phi[rows, :])
    return out


def sparse_terms(cl):
    """H_J, H_K, H_D as CSR matrices on 2^N, built bond-direction by bond-direction to cap memory.
    Ket convention: s^x|s> = |-s>, s^y|s> = i z(s)|-s>, s^z|s> = z(s)|s>  (z = +1 for bit 0)."""
    import scipy.sparse as sp
    N = cl.N; Dm = 2 ** N
    b = np.arange(Dm, dtype=np.int64)
    zz = lambda i: (1 - 2 * ((b >> i) & 1)).astype(float)
    kcoef = {0: lambda z: np.ones_like(z, dtype=complex), 1: lambda z: 1j * z, 2: lambda z: z.astype(complex)}

    def entries(i, j, al, be, w):
        mask = 0
        if al in (0, 1): mask |= 1 << i
        if be in (0, 1): mask |= 1 << j
        c = w * kcoef[al](zz(i)) * kcoef[be](zz(j))
        nz = np.abs(c) > 0
        return (b ^ mask)[nz], b[nz], c[nz]

    mats = {}
    for name in ("J", "K", "D"):
        diag = np.zeros(Dm, complex); acc = None
        for a in range(3):
            rows, cols, vals = [], [], []
            for (i, j, aa, n) in cl.bonds:
                if aa != a: continue
                if name == "J": ops = [(0, 0, 1.), (1, 1, 1.), (2, 2, 1.)]
                elif name == "K": ops = [(a, a, 1.)]
                else:
                    bb, cc = CYC[a]; ops = [(bb, cc, 1.), (cc, bb, -1.)]
                for al, be, w in ops:
                    if al == 2 and be == 2:
                        diag += w * zz(i) * zz(j); continue
                    r, c, v = entries(i, j, al, be, w)
                    rows.append(r); cols.append(c); vals.append(v)
            if rows:
                M = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows).astype(np.int32), np.concatenate(cols).astype(np.int32))), shape=(Dm, Dm))
                acc = M if acc is None else acc + M
                del rows, cols, vals
        M = sp.diags(diag).tocsr() + (acc if acc is not None else 0)
        M = sp.csr_matrix(M); M.sum_duplicates(); M.eliminate_zeros()
        if name in ("J", "K"):
            assert np.abs(M.data.imag).max() < 1e-12
            M = sp.csr_matrix(M.real)
        mats[name] = M
    return mats


def product_vector(ms, bits):
    """|m_1> x ... x |m_N> for Bloch unit vectors m_i (rows)."""
    v = np.ones(bits.shape[0], complex)
    for i, m in enumerate(ms):
        th = np.arccos(np.clip(m[2], -1, 1)); ph = np.arctan2(m[1], m[0])
        up, dn = np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)
        v *= np.where(bits[:, i] == 0, up, dn)
    return v


def classical_vector(cl, ms):
    """(e_J, e_K, e_D) per oriented bond for a product state with Bloch vectors ms."""
    eJ = eK = eD = 0.
    for (i, j, a, n) in cl.bonds:
        mi, mj = ms[i], ms[j]
        eJ += mi @ mj; eK += mi[a] * mj[a]; eD += np.cross(mi, mj)[a]
    nb = len(cl.bonds)
    return np.array([eJ, eK, eD]) / nb


def coupling_mats(Jv):
    J, K, D = Jv
    Ms = []
    for a in range(3):
        e = np.eye(3)[a]
        cx = np.array([[0, -e[2], e[1]], [e[2], 0, -e[0]], [-e[1], e[0], 0]])
        Ms.append(J * np.eye(3) + K * np.outer(e, e) + D * cx.T)   # m^T M m' = J m.m' + K m_a m'_a + D e.(m x m')
    return np.array(Ms)


def greedy_classical(cl, Jv, rng, starts=12, iters=300, seeds=()):
    """Best product state for direction Jv=(J,K,D): sublattice-parallel local-field alignment
    (energy non-increasing on bipartite clusters); returns (E per bond, Bloch vectors)."""
    Ms = coupling_mats(Jv)
    Mb = Ms[cl.ba]                       # (3N,3,3)
    par = cl.X.sum(axis=1) % 2
    assert all(par[i] != par[j] for i, j in zip(cl.bi, cl.bj)), "cluster not bipartite"
    best = (np.inf, None)
    starts_list = [np.array(s, float) for s in seeds] + [rng.normal(size=(cl.N, 3)) for _ in range(starts)]
    for m0 in starts_list:
        m = m0 / np.linalg.norm(m0, axis=1)[:, None]
        for it in range(iters):
            for s in (0, 1):
                h = np.zeros((cl.N, 3))
                np.add.at(h, cl.bi, np.einsum('bij,bj->bi', Mb, m[cl.bj]))
                np.add.at(h, cl.bj, np.einsum('bji,bj->bi', Mb, m[cl.bi]))
                nh = np.linalg.norm(h, axis=1)
                sel = (par == s) & (nh > 1e-14)
                m[sel] = -h[sel] / nh[sel][:, None]
        E = classical_vector(cl, m) @ np.array(Jv)
        if E < best[0]:
            best = (E, m.copy())
    return best
