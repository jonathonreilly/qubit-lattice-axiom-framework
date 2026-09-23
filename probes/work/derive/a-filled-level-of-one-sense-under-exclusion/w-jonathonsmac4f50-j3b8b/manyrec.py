"""Many records under the Record axiom's exclusion (one record per site at a time), each with a
two-component coin, moving by the two-dimensional walk plus block 77's scalar hop.

One record:  (H1 psi)(x) = a0 psi(x) + sum_j [T_j psi(x + e_j) + T_j^dag psi(x - e_j)],
             T_j = a + sigma_j / (2i),
so H1 = a0 + 2a sum_j C_j + sum_j sigma_j S_j, symbol a0 + 2a sum_j cos k_j + sigma . sin k.
Many records: the compressed generator P (sum over records of H1) P, P = at most one record
per site whatever the coins; exchange sign sgn = -1 (antisymmetric) or +1 (symmetric), the
sign not being supplied by the axioms (block 78).
Basis: occupied set (bitmask) and the coins of the occupied sites packed in ascending site
order; the sign of c^dag_x c_y is (-1)^(number of occupied sites strictly between x and y).
"""
import itertools
import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)


class Torus2D:
    def __init__(self, Lx, Ly):
        self.Lx, self.Ly, self.Ns = Lx, Ly, Lx * Ly

    def site(self, x, y):
        return (x % self.Lx) + self.Lx * (y % self.Ly)

    def coords(self, s):
        return s % self.Lx, s // self.Lx

    def moves(self, a):
        """(y, x, M): a record at y moves to x, its coin multiplied by M."""
        T = [a * np.eye(2) + SX / 2j, a * np.eye(2) + SY / 2j]
        out = []
        for s in range(self.Ns):
            x, y = self.coords(s)
            for j, (dx, dy) in enumerate([(1, 0), (0, 1)]):
                t = self.site(x + dx, y + dy)
                out.append((t, s, T[j]))                  # c^dag_s T_j c_t
                out.append((s, t, T[j].conj().T))         # c^dag_t T_j^dag c_s
        return out

    def one_record(self, a0, a):
        H = np.zeros((2 * self.Ns, 2 * self.Ns), dtype=complex)
        for s in range(self.Ns):
            H[2 * s:2 * s + 2, 2 * s:2 * s + 2] += a0 * np.eye(2)
        for (y, x, M) in self.moves(a):
            H[2 * x:2 * x + 2, 2 * y:2 * y + 2] += M
        return H


def ins_bit(code, r, b):
    lo = code & ((1 << r) - 1)
    return lo | (b << r) | ((code >> r) << (r + 1))


def between_sign(m, x, y, sgn):
    lo, hi = min(x, y), max(x, y)
    n = bin(m & (((1 << hi) - 1) & ~((1 << (lo + 1)) - 1))).count('1')
    return (-1) ** n if sgn < 0 else 1


class HardCore:
    def __init__(self, lat, N, a0, a, sgn):
        self.lat, self.N, self.a0, self.a, self.sgn = lat, N, a0, a, sgn
        self.occs = [sum(1 << s for s in c) for c in itertools.combinations(range(lat.Ns), N)]
        self.occ_index = {m: i for i, m in enumerate(self.occs)}
        self.nc = 1 << N
        self.dim = len(self.occs) * self.nc
        cw = np.arange(1 << max(N - 1, 0), dtype=np.int64)
        self.I = {r: (ins_bit(cw, r, 0), ins_bit(cw, r, 1)) for r in range(N)}
        self.hops = []
        for io, m in enumerate(self.occs):
            for (y, x, M) in lat.moves(a):
                if not (m >> y) & 1 or (m >> x) & 1:
                    continue
                m2 = (m & ~(1 << y)) | (1 << x)
                self.hops.append((io, self.occ_index[m2], self.rank(m, y), self.rank(m2, x),
                                  between_sign(m, x, y, sgn), M))

    @staticmethod
    def rank(m, s):
        return bin(m & ((1 << s) - 1)).count('1')

    def matvec(self, v):
        v = v.reshape(len(self.occs), self.nc)
        out = self.a0 * self.N * v.copy()
        for (io, jo, ry, rx, sign, M) in self.hops:
            v0 = v[io, self.I[ry][0]]
            v1 = v[io, self.I[ry][1]]
            out[jo, self.I[rx][0]] += sign * (M[0, 0] * v0 + M[0, 1] * v1)
            out[jo, self.I[rx][1]] += sign * (M[1, 0] * v0 + M[1, 1] * v1)
        return out.reshape(-1)

    def dense(self):
        H = np.zeros((self.dim, self.dim), dtype=complex)
        e = np.zeros(self.dim, dtype=complex)
        for i in range(self.dim):
            e[i] = 1
            H[:, i] = self.matvec(e)
            e[i] = 0
        return H

    def modes(self):
        """basis index -> tuple of occupied modes 2*site + coin (ascending)"""
        out = []
        for m in self.occs:
            sites = [s for s in range(self.lat.Ns) if (m >> s) & 1]
            for code in range(self.nc):
                out.append(tuple(2 * s + ((code >> r) & 1) for r, s in enumerate(sites)))
        return out

    def one_body_dm(self, V):
        """D[s, (x,al), (y,be)] = <v_s| c^dag_{x al} c_{y be} |v_s> for the columns v_s of V."""
        Ns = self.lat.Ns
        ns = V.shape[1]
        W = V.reshape(len(self.occs), self.nc, ns)
        D = np.zeros((ns, 2 * Ns, 2 * Ns), dtype=complex)
        codes = np.arange(self.nc)
        for io, m in enumerate(self.occs):
            for y in range(Ns):
                if not (m >> y) & 1:
                    continue
                r = self.rank(m, y)
                bits = (codes >> r) & 1
                for be in range(2):
                    src = codes[bits == be]
                    for al in range(2):
                        dst = src if al == be else src ^ (1 << r)
                        D[:, 2 * y + al, 2 * y + be] += np.einsum('is,is->s', W[io, dst].conj(), W[io, src])
                for x in range(Ns):
                    if (m >> x) & 1:
                        continue
                    m2 = (m & ~(1 << y)) | (1 << x)
                    jo = self.occ_index[m2]
                    sign = between_sign(m, x, y, self.sgn)
                    rx = self.rank(m2, x)
                    for be in range(2):
                        src = W[io, self.I[r][be]]
                        for al in range(2):
                            dst = W[jo, self.I[rx][al]]
                            D[:, 2 * x + al, 2 * y + be] += sign * np.einsum('is,is->s', dst.conj(), src)
        return D

    def translate(self, v, dx, dy):
        lat = self.lat
        v = v.reshape(len(self.occs), self.nc)
        out = np.zeros_like(v)
        perm = [lat.site(lat.coords(s)[0] + dx, lat.coords(s)[1] + dy) for s in range(lat.Ns)]
        codes = np.arange(self.nc)
        for io, m in enumerate(self.occs):
            sites = [s for s in range(lat.Ns) if (m >> s) & 1]
            new = [perm[s] for s in sites]
            inv = sum(1 for i in range(self.N) for j in range(i + 1, self.N) if new[i] > new[j])
            sign = (-1) ** inv if self.sgn < 0 else 1
            order = sorted(range(self.N), key=lambda i: new[i])
            pos = [0] * self.N
            for nr, i in enumerate(order):
                pos[i] = nr
            nc = np.zeros_like(codes)
            for i in range(self.N):
                nc |= ((codes >> i) & 1) << pos[i]
            out[self.occ_index[sum(1 << s for s in new)], nc] = sign * v[io, codes]
        return out.reshape(-1)


def brute_hamiltonian(lat, N, a0, a, sgn):
    """independent construction: mode tuples, Jordan-Wigner signs over the mode order."""
    states = []
    for sites in itertools.combinations(range(lat.Ns), N):
        for coins in itertools.product(range(2), repeat=N):
            states.append(tuple(2 * s + c for s, c in zip(sites, coins)))
    idx = {s: i for i, s in enumerate(states)}
    H = np.zeros((len(states), len(states)), dtype=complex)
    h1 = lat.one_record(0.0, a)
    for i, st in enumerate(states):
        H[i, i] += a0 * N
        occ = {q // 2 for q in st}
        for p in st:
            y, be = divmod(p, 2)
            rest = [q for q in st if q != p]
            sc = (-1) ** st.index(p)
            for x in range(lat.Ns):
                if x in occ:
                    continue
                for al in range(2):
                    amp = h1[2 * x + al, 2 * y + be]
                    if amp == 0:
                        continue
                    q = 2 * x + al
                    new = sorted(rest + [q])
                    s2 = sc * (-1) ** new.index(q) if sgn < 0 else 1
                    H[idx[tuple(new)], i] += s2 * amp
    return states, H


def momentum_rho(lat, D):
    """rho(k)[al, be] = <c^dag_{k al} c_{k be}>, c_{k al} = Ns^(-1/2) sum_x e^(-ik.x) c_{x al}."""
    out = {}
    for m1 in range(lat.Lx):
        for m2 in range(lat.Ly):
            k = (2 * np.pi * m1 / lat.Lx, 2 * np.pi * m2 / lat.Ly)
            ph = np.array([np.exp(1j * (k[0] * lat.coords(s)[0] + k[1] * lat.coords(s)[1])) for s in range(lat.Ns)])
            rho = np.zeros((2, 2), dtype=complex)
            for al in range(2):
                for be in range(2):
                    rho[al, be] = ph @ D[al::2, be::2] @ ph.conj() / lat.Ns
            out[(m1, m2)] = rho
    return out


def point_symmetry(lat, a):
    """the 90-degree rotation about site 0 and the reflection x -> -x, each with the coin unitary
    (found among a short list of candidates) that makes it commute with the one-record generator."""
    H1 = lat.one_record(0.3, a)
    SZ = np.array([[1, 0], [0, -1]], dtype=complex)
    cands = [np.diag([np.exp(-1j * np.pi / 4), np.exp(1j * np.pi / 4)]),
             np.diag([np.exp(1j * np.pi / 4), np.exp(-1j * np.pi / 4)]), SX, SY, SZ, np.eye(2)]
    out = []
    for f in (lambda x, y: (-y, x), lambda x, y: (-x, y)):
        perm = [lat.site(*f(*lat.coords(s))) for s in range(lat.Ns)]
        found = None
        for U in cands:
            P = np.zeros((2 * lat.Ns, 2 * lat.Ns), dtype=complex)
            for s in range(lat.Ns):
                P[2 * perm[s]:2 * perm[s] + 2, 2 * s:2 * s + 2] = U
            if np.abs(P @ H1 - H1 @ P).max() < 1e-12:
                found = U
                break
        assert found is not None
        out.append((perm, found))
    return out


def apply_site_unitary(hc, v, perm, U):
    """(site permutation perm) x (coin unitary U on every record), with the fermionic reordering sign."""
    N = hc.N
    v = v.reshape(len(hc.occs), hc.nc)
    out = np.zeros_like(v)
    for io, m in enumerate(hc.occs):
        sites = [s for s in range(hc.lat.Ns) if (m >> s) & 1]
        new = [perm[s] for s in sites]
        inv = sum(1 for i in range(N) for j in range(i + 1, N) if new[i] > new[j])
        sign = (-1) ** inv if hc.sgn < 0 else 1
        order = sorted(range(N), key=lambda i: new[i])
        pos = [0] * N
        for nr, i in enumerate(order):
            pos[i] = nr
        T = v[io].reshape([2] * N)                    # axis q <-> code bit N-1-q
        for q in range(N):
            T = np.moveaxis(np.tensordot(U, T, axes=([1], [q])), 0, q)
        inv_pos = [0] * N
        for r in range(N):
            inv_pos[pos[r]] = r
        axes = [N - 1 - inv_pos[N - 1 - q] for q in range(N)]
        out[hc.occ_index[sum(1 << s for s in new)]] = sign * np.transpose(T, axes).reshape(-1)
    return out.reshape(-1)


def close_manifold(hc, Vg, gens, E0, tol=1e-6):
    """span of the ground vectors and all their images under the generators (unitary symmetries)."""
    B = np.linalg.qr(Vg)[0]
    while True:
        imgs = [apply_site_unitary(hc, B[:, i], perm, U) for (perm, U) in gens for i in range(B.shape[1])]
        M = np.column_stack([B] + imgs)
        u, sv, _ = np.linalg.svd(M, full_matrices=False)
        r = int(np.sum(sv > 1e-6 * sv[0]))
        if r == B.shape[1]:
            break
        B = u[:, :r]
    res = max(np.linalg.norm(hc.matvec(B[:, i]) - E0 * B[:, i]) for i in range(B.shape[1]))
    return B, res
