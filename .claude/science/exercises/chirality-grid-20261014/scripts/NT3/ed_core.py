"""NT-3 / T-G1 exact-diagonalisation core (see ../PREREG.md).

Momentum-space fermion Fock space of the NON-LIGHT modes (light modes have f = 0 and commute with H_Q).
Mode index p = a*M + j  (flavour a = 0..3, j = index into the list of included momenta).
Basis states are int64 bitmasks; fermion sign for c_p / c_p^dag = (-1)^{# occupied modes with index < p}.
Sectors: SU(4) weight modulo diagonal shift (eps-term shifts every n_a by -1) and total momentum.
"""
import numpy as np, itertools
import scipy.sparse as sp, scipy.sparse.linalg as sla, scipy.linalg as la

NF = 4


class Group:
    """Finite abelian momentum group with labels 0..n-1."""
    def __init__(self, n, add, neg, kvec, light, name):
        self.n, self.add, self.neg, self.kvec, self.light, self.name = n, add, neg, kvec, light, name

def ring(L):
    add = [[(i + j) % L for j in range(L)] for i in range(L)]
    neg = [(-i) % L for i in range(L)]
    kvec = [np.array([2 * np.pi * i / L]) for i in range(L)]
    return Group(L, add, neg, kvec, {0}, f"ring L={L}")

def cube2():
    # labels = 3-bit corners; bit a set <=> p_a = pi.  hw1 corners (one bit set) are light.
    add = [[i ^ j for j in range(8)] for i in range(8)]
    neg = list(range(8))
    kvec = [np.pi * np.array([(i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1], float) for i in range(8)]
    light = {i for i in range(8) if bin(i).count("1") == 1}
    return Group(8, add, neg, kvec, light, "cube 2x2x2")


def popcount(x):
    return np.bitwise_count(x)


class Model:
    def __init__(self, G, fval, include_light=False, kin=None):
        """fval: dict label -> f(k) (normalised).  kin: dict label -> single-particle energy (optional)."""
        self.G = G
        self.moms = [m for m in range(G.n) if include_light or m not in G.light]
        self.M = len(self.moms)
        self.jof = {m: j for j, m in enumerate(self.moms)}
        self.f = np.array([fval[m] for m in self.moms], float)
        self.kin = None if kin is None else np.array([kin[m] for m in self.moms], float)
        self.V = G.n
        # per-flavour subsets grouped by (size, momentum)
        self.sub = {}
        for n in range(self.M + 1):
            for comb in itertools.combinations(range(self.M), n):
                mom = 0
                for j in comb:
                    mom = G.add[mom][self.moms[j]]
                mask = 0
                for j in comb:
                    mask |= 1 << j
                self.sub.setdefault((n, mom), []).append(mask)
        self.sub = {k: np.array(v, np.int64) for k, v in self.sub.items()}
        # eps-term momentum quadruples (k1+k2+k3+k4 = 0)
        q = []
        for j1, j2, j3 in itertools.product(range(self.M), repeat=3):
            m123 = G.add[G.add[self.moms[j1]][self.moms[j2]]][self.moms[j3]]
            m4 = G.neg[m123]
            if m4 in self.jof:
                j4 = self.jof[m4]
                c = self.f[j1] * self.f[j2] * self.f[j3] * self.f[j4]
                if abs(c) > 1e-15:
                    q.append((j1, j2, j3, j4, c))
        self.quads = q

    def p(self, a, j):
        return a * self.M + j

    # ---------------- sectors ----------------
    def sector_states(self, nvec, K):
        """All basis states with flavour occupations nvec (tuple of 4) and total momentum K."""
        G, M = self.G, self.M
        if any(n < 0 or n > M for n in nvec):
            return np.zeros(0, np.int64)
        partial = {0: np.zeros(1, np.int64)}
        for a, n in enumerate(nvec):
            new = {}
            for m1, arr in partial.items():
                for m2 in range(G.n):
                    key = (n, m2)
                    if key not in self.sub:
                        continue
                    s2 = self.sub[key] << (a * M)
                    comb = (arr[:, None] | s2[None, :]).ravel()
                    mm = G.add[m1][m2]
                    new.setdefault(mm, []).append(comb)
            partial = {k: np.concatenate(v) for k, v in new.items()}
        return partial.get(K, np.zeros(0, np.int64))

    def chain_sector(self, d, K):
        """Sector: weights n = (m+d0, m+d1, m+d2, m+d3) for all m (eps term moves along the chain)."""
        out = []
        for m in range(-max(abs(x) for x in d) - 1, self.M + 2):
            nvec = tuple(m + x for x in d)
            st = self.sector_states(nvec, K)
            if len(st):
                out.append(st)
        if not out:
            return np.zeros(0, np.int64)
        return np.sort(np.concatenate(out))

    # ---------------- operator application ----------------
    @staticmethod
    def apply(s, ops):
        """ops applied in the listed order (first element acts first). Each op = (dag, p)."""
        s = s.copy(); ok = np.ones(len(s), bool); sign = np.ones(len(s))
        for dag, p in ops:
            bit = (s >> p) & 1
            ok &= (bit == 0) if dag else (bit == 1)
            par = popcount(s & ((np.int64(1) << p) - 1)) & 1
            sign *= 1 - 2 * par.astype(float)
            s ^= (np.int64(1) << p)
        return s, sign, ok

    def build_H(self, basis, W=1.0, v=0.0):
        """H = W*[ -(1/V) sum f f f f c1 c2 c3 c4 + h.c.  +  v * sum_{a<b} B_ab^dag B_ab ] + kinetic."""
        N = len(basis)
        rows, cols, vals = [], [], []
        idx = np.arange(N)
        for (j1, j2, j3, j4, c) in self.quads:
            # c_1(k1) c_2(k2) c_3(k3) c_4(k4): c_4 acts first
            ops = [(False, self.p(3, j4)), (False, self.p(2, j3)), (False, self.p(1, j2)), (False, self.p(0, j1))]
            s2, sg, ok = self.apply(basis, ops)
            if not ok.any():
                continue
            s2, sg, src = s2[ok], sg[ok], idx[ok]
            t = np.searchsorted(basis, s2)
            good = (t < N)
            good[good] &= basis[t[good]] == s2[good]
            rows.append(t[good]); cols.append(src[good]); vals.append(-W * c / self.V * sg[good])
        if rows:
            r = np.concatenate(rows); cc = np.concatenate(cols); vv = np.concatenate(vals)
            A = sp.csr_matrix((vv, (r, cc)), shape=(N, N))
            H = A + A.T
        else:
            H = sp.csr_matrix((N, N))
        if v != 0.0:
            H = H + W * v * self.build_BdB(basis)
        if self.kin is not None:
            diag = np.zeros(N)
            for a in range(NF):
                for j in range(self.M):
                    diag += self.kin[j] * ((basis >> self.p(a, j)) & 1)
            H = H + sp.diags(diag)
        return H.tocsr()

    def build_BdB(self, basis):
        N = len(basis); idx = np.arange(N)
        rows, cols, vals = [], [], []
        G = self.G
        for a, b in itertools.combinations(range(NF), 2):
            for j1, j2, j3 in itertools.product(range(self.M), repeat=3):
                # k1 + k2 = k3 + k4  ->  k4 = k1 + k2 - k3
                m4 = G.add[G.add[self.moms[j1]][self.moms[j2]]][G.neg[self.moms[j3]]]
                if m4 not in self.jof:
                    continue
                j4 = self.jof[m4]
                c = self.f[j1] * self.f[j2] * self.f[j3] * self.f[j4] / self.V
                if abs(c) < 1e-15:
                    continue
                # c_b^dag(k1) c_a^dag(k2) c_a(k3) c_b(k4)
                ops = [(False, self.p(b, j4)), (False, self.p(a, j3)), (True, self.p(a, j2)), (True, self.p(b, j1))]
                s2, sg, ok = self.apply(basis, ops)
                if not ok.any():
                    continue
                s2, sg, src = s2[ok], sg[ok], idx[ok]
                t = np.searchsorted(basis, s2)
                good = t < N
                good[good] &= basis[t[good]] == s2[good]
                rows.append(t[good]); cols.append(src[good]); vals.append(c * sg[good])
        if not rows:
            return sp.csr_matrix((N, N))
        B = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(N, N))
        return B

    def apply_op_sum(self, terms, basis, vec, tbasis):
        """Apply sum_t coef_t * opstring_t to vec (on basis) and express on tbasis (sorted)."""
        out = np.zeros(len(tbasis))
        for coef, ops in terms:
            s2, sg, ok = self.apply(basis, ops)
            if not ok.any():
                continue
            t = np.searchsorted(tbasis, s2[ok])
            good = t < len(tbasis)
            good[good] &= tbasis[t[good]] == s2[ok][good]
            np.add.at(out, t[good], coef * sg[ok][good] * vec[ok][good])
        return out

    def occ(self, basis, vec):
        """<n(k)> summed over flavours, per included momentum j."""
        w = vec ** 2
        return np.array([sum((w * ((basis >> self.p(a, j)) & 1)).sum() for a in range(NF)) for j in range(self.M)])


def lowest(H, k=3):
    N = H.shape[0]
    if N == 0:
        return np.array([]), None
    if N <= 600:
        e, v = la.eigh(H.toarray())
        return e[:k], v[:, :k]
    k = min(k, N - 2)
    e, v = sla.eigsh(H, k=k, which="SA", tol=1e-12, ncv=max(20, 2 * k + 10))
    o = np.argsort(e)
    return e[o], v[:, o]


def dominant_weights(M):
    """d = (d0>=d1>=d2>=d3=0) up to diagonal shift; d0 <= M."""
    out = []
    for d0 in range(M + 1):
        for d1 in range(d0 + 1):
            for d2 in range(d1 + 1):
                out.append((d0, d1, d2, 0))
    return out
