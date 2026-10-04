"""A49 library (supplied toys; nothing adopted).  Inverse 'parent rule from a state' search.
The inverse method itself (energy-variance covariance matrix of a local operator basis) is a COMPARATOR
computational technique (Chertkov-Clark 2018, Qi-Ranard 2019, Greiter-Schnells-Thomale 2018; from memory).

Frames.
 * Operators are BUILT in the soldered frame: exact soldered action of the 24 proper turns,
   alpha_g(s^b_x) = sum_c g_cb s^c_{gx}; translation-invariant sums of Pauli strings with REAL coefficients and
   EVEN weight  =>  Hermitian and time-reversal even.  Covariance = invariance under all 24 alpha_g (checked).
 * States and estimators live in the Klein-dual frame of A44: O_dual = V^dag O V, i.e. s^b_x -> R_x(b) s^b_x with
   R_x = diag((-1)^{x2+x3}, (-1)^{x1+x3}, (-1)^{x1+x2});  psi_sold = (x)V_x psi_dual (A44, EXACT).
Estimators (configuration basis = dual-frame s^z, bit 0 = up, z = 1 - 2 bit).
 * 'full'   : E_i(s) = (h_i psi)(s)/psi(s);  C_ij = <E_i^* E_j> - <E_i>^*<E_j>   (valid iff psi(s) != 0 wherever
              (h_i psi)(s) != 0).
 * 'singlet': psi an exact SU(2) singlet (dual frame, lam' = 0).  psi = 0 outside S^z = 0, so 'full' silently drops
              every S^z-changing component.  Wigner-Eckart: rank-k parts of different k do not mix and
              <A_q^dag B_q> is q-independent, so C = Cov(rank 0) + sum_c <O1_c O1_c> + (3/2) sum_m <O2_m O2_m>, built
              only from S^z-conserving q = 0 operators (s.s, (s x s)_z, T_zz = s^z s^z - s.s/3)."""
import sys, itertools, time, numpy as np
D49 = __file__.rsplit('/', 1)[0]
sys.path.insert(0, D49.rsplit('/', 1)[0] + "/A46"); sys.path.insert(0, D49.rsplit('/', 1)[0] + "/A44")
from a46lib import Cluster, cube, SIG, Vx, FD, binerr, bits_table, projected_vector

# ------------------------------------------------------------------ turns and strings
def _rots():
    out = []
    for perm in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            g = np.zeros((3, 3), int)
            for i in range(3):
                g[perm[i], i] = sg[i]
            if round(np.linalg.det(g)) == 1:
                out.append(g)
    return out
ROT = _rots(); assert len(ROT) == 24


def canon(st):
    st = sorted(st); x0 = st[0][0]
    return tuple(sorted(((s[0] - x0[0], s[1] - x0[1], s[2] - x0[2]), b) for s, b in st))


def rot_string(g, st):
    c = 1; out = []
    for s, b in st:
        s2 = tuple(int(v) for v in g @ np.array(s)); col = g[:, b]; b2 = int(np.flatnonzero(col)[0]); c *= int(col[b2])
        out.append((s2, b2))
    return canon(out), c


def add(d, k, v):
    d[k] = d.get(k, 0.) + v


def clean(d, eps=1e-12):
    return {k: v for k, v in d.items() if abs(v) > eps}


def gavg(op):
    out = {}
    for g in ROT:
        for P, c in op.items():
            P2, s = rot_string(g, P); add(out, P2, s * c / 24.)
    return clean(out)


def cov_defect(op):
    worst = 0.
    for g in ROT:
        out = {}
        for P, c in op.items():
            P2, s = rot_string(g, P); add(out, P2, s * c)
        for k in set(out) | set(op):
            worst = max(worst, abs(out.get(k, 0.) - op.get(k, 0.)))
    return worst


def hs(o1, o2):
    return sum(c * o2.get(P, 0.) for P, c in o1.items())


def normalize(op):
    n = np.sqrt(hs(op, op)); return {k: v / n for k, v in op.items()}


def kR(x, b):
    return -1 if (int(x[(b + 1) % 3]) + int(x[(b + 2) % 3])) % 2 else 1


def klein_rel(op):
    """Klein sign map on a canonical dict; only translation-consistent when every Pauli type occurs an even number
    of times in each string (true for dual SU(2)-invariant products of dot products)."""
    return clean({P: c * np.prod([kR(s, b) for s, b in P]) for P, c in op.items()})


def levi(i, j, k):
    return (i - j) * (j - k) * (k - i) / 2


def eps_mat(n):
    return np.array([[sum(n[c] * levi(c, a, b) for c in range(3)) for b in range(3)] for a in range(3)])


def bilinear(d, M):
    op = {}
    for a in range(3):
        for b in range(3):
            if abs(M[a, b]) > 1e-14:
                add(op, canon([((0, 0, 0), a), (tuple(d), b)]), float(M[a, b]))
    return op


# ------------------------------------------------------------------ the basis
E3 = np.eye(3)
def bilinear_basis():
    n2 = np.array([1, 1, 0]) / np.sqrt(2); n4 = np.ones(3) / np.sqrt(3)
    spec = [  # name, class, displacement, seed tensor
        ("J1", "S1", (1, 0, 0), np.eye(3)), ("K1", "S1", (1, 0, 0), np.outer(E3[0], E3[0])), ("D1", "S1", (1, 0, 0), eps_mat(E3[0])),
        ("J2", "S1", (1, 1, 0), np.eye(3)), ("Kn2", "S1", (1, 1, 0), np.outer(E3[2], E3[2])), ("Kd2", "S1", (1, 1, 0), np.outer(n2, n2)), ("D2", "S1", (1, 1, 0), eps_mat(n2)),
        ("J3", "S1", (2, 0, 0), np.eye(3)), ("K3", "S1", (2, 0, 0), np.outer(E3[0], E3[0])), ("D3", "S1", (2, 0, 0), eps_mat(E3[0])),
        ("J4", "S2", (1, 1, 1), np.eye(3)), ("Kd4", "S2", (1, 1, 1), np.outer(n4, n4)), ("D4", "S2", (1, 1, 1), eps_mat(n4)),
    ]
    return [(nm, cls, normalize(gavg(bilinear(d, M)))) for nm, cls, d, M in spec]


SHAPES = {  # four-site supports; S1 = inside one star, S2 = plaquette
    "T": ("S1", [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0)]),
    "C": ("S1", [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]),
    "Dm": ("S1", [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]),
    "Y": ("S1", [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1)]),
    "P": ("S2", [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]),
}
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def posavg4(sites, pairing):
    """dual-frame (s_i.s_j)(s_k.s_l) averaged over the 24 turns acting on positions only:
    {(canonical positions, canonical pairing index): weight}."""
    out = {}
    for g in ROT:
        P = [tuple(int(v) for v in g @ np.array(s)) for s in sites]
        x0 = min(P); P = [tuple(p[c] - x0[c] for c in range(3)) for p in P]
        order = sorted(range(4), key=lambda k: P[k]); Ps = tuple(P[k] for k in order)
        inv = {order[k]: k for k in range(4)}
        pr = tuple(sorted(tuple(sorted((inv[a], inv[b]))) for a, b in pairing))
        add(out, (Ps, PAIRINGS.index(pr)), 1. / 24)
    return out


def strings4(d4):
    out = {}
    for (Ps, pi), w in d4.items():
        (i, j), (k, l) = PAIRINGS[pi]
        for a in range(3):
            for b in range(3):
                add(out, canon([(Ps[i], a), (Ps[j], a), (Ps[k], b), (Ps[l], b)]), w)
    return clean(out)


def four_basis():
    """Klein duals of dual-frame SU(2)-invariant products (s.s)(s.s) on star / plaquette four-sets; one operator per
    distinct pairing orbit.  Returns [(name, class, dual posavg dict, soldered canonical dict)]."""
    out = []
    for nm, (cls, sites) in SHAPES.items():
        seen = []
        for pi, pr in enumerate(PAIRINGS):
            d4 = posavg4(sites, pr)
            sold = klein_rel(strings4(d4))
            nrm = np.sqrt(hs(sold, sold)); sold = {k: v / nrm for k, v in sold.items()}
            d4 = {k: v / nrm for k, v in d4.items()}
            if any(max(abs(sold.get(k, 0) - o.get(k, 0)) for k in set(sold) | set(o)) < 1e-10 for o in seen):
                continue
            seen.append(sold)
            out.append((f"{nm}{pi}", cls, d4, sold))
    return out


# ------------------------------------------------------------------ mean-field states (dual frame)
def mf_state(cl, lam2=0., m=0., pattern="neel", axis=(0, 0, 1), twist=(np.pi, np.pi, np.pi)):
    """A46 mf_dual with the order field along an arbitrary dual-frame axis.  Soldered NN hop i s^a (lam = 1),
    face-diagonal i lam2 s.d/|d|, APBC; rotated by V = (+)V_x; plus m * sign_x * (axis . s)."""
    N = cl.N; tw = np.array(twist, float); h = np.zeros((2 * N, 2 * N), complex)
    def addh(i, j, u, n):
        ph = np.exp(1j * (tw @ n)); h[2 * i:2 * i + 2, 2 * j:2 * j + 2] += u * ph; h[2 * j:2 * j + 2, 2 * i:2 * i + 2] += (u * ph).conj().T
    for (i, j, a, n) in cl.bonds:
        addh(i, j, 1j * SIG[a], n)
    if lam2 != 0:
        for i, s in enumerate(cl.sites):
            for d in FD:
                rep, n = cl.canon(np.array(s) + np.array(d)); dh = np.array(d, float) / np.sqrt(2)
                addh(i, cl.idx[tuple(rep)], 1j * lam2 * sum(dh[c] * SIG[c] for c in range(3)), n)
    V = np.zeros((2 * N, 2 * N), complex)
    for i, s in enumerate(cl.sites):
        V[2 * i:2 * i + 2, 2 * i:2 * i + 2] = Vx(s)
    hd = V.conj().T @ h @ V
    ax = np.array(axis, float); ax /= np.linalg.norm(ax); As = sum(ax[c] * SIG[c] for c in range(3))
    for i, s in enumerate(cl.sites):
        sg = (-1) ** int(sum(s)) if pattern == "neel" else (-1) ** int(s[0] + s[1])
        hd[2 * i:2 * i + 2, 2 * i:2 * i + 2] += m * sg * As
    ev, W = np.linalg.eigh(hd)
    return W[:, :N].copy(), ev[N] - ev[N - 1]


def product_state(blochs):
    """Slater form of a product state: orbital k sits on site k with the spinor of Bloch vector blochs[k]."""
    N = len(blochs); Phi = np.zeros((2 * N, N), complex)
    for k, m in enumerate(blochs):
        th = np.arccos(np.clip(m[2], -1, 1)); ph = np.arctan2(m[1], m[0])
        Phi[2 * k, k] = np.cos(th / 2); Phi[2 * k + 1, k] = np.exp(1j * ph) * np.sin(th / 2)
    return Phi


# ------------------------------------------------------------------ cluster tables
def disps():
    out = [(0, 0, 0)]
    for v in itertools.product(range(-2, 3), repeat=3):
        n2 = sum(c * c for c in v)
        if v != (0, 0, 0) and (n2 in (1, 2, 3) or (n2 == 4 and max(abs(c) for c in v) == 2)):
            out.append(tuple(v))
    return out
DISPS = disps(); assert len(DISPS) == 33


class Tables:
    """Dual-frame expansion of the operator list on a cluster: per-pair 3x3 tensors (bilinears) and per-four-set
    pairing weights (four-spin), plus cluster Pauli strings (for exact application and the Gram matrix)."""
    def __init__(self, cl, ops):
        self.cl = cl; N = self.N = cl.N; self.names = [o[0] for o in ops]; self.cls = [o[1] for o in ops]; n = len(ops)
        X = np.array(cl.sites)
        loc = lambda x: cl.idx[tuple(cl.canon(np.array(x))[0])]
        self.nbr = np.array([[loc(X[i] + np.array(d)) for i in range(N)] for d in DISPS])
        pairs = {}; Ms = []          # pair key (i<j) -> index ; Ms[op][pair] 3x3
        sets = {}; W4 = []
        for k, op in enumerate(ops):
            Mk = {}; Wk = {}
            if op[2] == "b":
                for i in range(N):
                    for P, c in op[3].items():
                        (r0, a), (r, b) = P; assert r0 == (0, 0, 0)
                        j = loc(X[i] + np.array(r)); assert j != i
                        coef = c * kR(X[i], a) * kR(X[i] + np.array(r), b)
                        if i < j: key, aa, bb = (i, j), a, b
                        else: key, aa, bb = (j, i), b, a
                        if key not in pairs: pairs[key] = len(pairs)
                        Mk.setdefault(pairs[key], np.zeros((3, 3)))[aa, bb] += coef
            else:
                for i in range(N):
                    for (Ps, pi), w in op[3].items():
                        cs = [loc(X[i] + np.array(p)) for p in Ps]; assert len(set(cs)) == 4
                        order = sorted(range(4), key=lambda q: cs[q]); S = tuple(cs[q] for q in order)
                        inv = {order[q]: q for q in range(4)}
                        pr = tuple(sorted(tuple(sorted((inv[u], inv[v]))) for u, v in PAIRINGS[pi]))
                        if S not in sets: sets[S] = len(sets)
                        Wk.setdefault(sets[S], np.zeros(3))[PAIRINGS.index(pr)] += w
            Ms.append(Mk); W4.append(Wk)
        self.np_, self.ns = len(pairs), len(sets)
        pk = sorted(pairs, key=pairs.get); self.pi = np.array([p[0] for p in pk], int); self.pj = np.array([p[1] for p in pk], int)
        self.W = np.zeros((n, 3, 3, self.np_))
        for k in range(n):
            for p, M in Ms[k].items():
                self.W[k, :, :, p] = M
        sk = sorted(sets, key=sets.get); self.sets = np.array(sk, int).reshape(-1, 4)
        self.W4 = np.zeros((n, self.ns, 3))
        for k in range(n):
            for q, w in W4[k].items():
                self.W4[k, q] = w
        # singlet (Wigner-Eckart) decomposition of the dual-frame pair tensors
        B = [np.diag([1, -1, 0]) / np.sqrt(2), np.diag([-1, -1, 2]) / np.sqrt(6)]
        for (a, b) in ((0, 1), (0, 2), (1, 2)):
            Bm = np.zeros((3, 3)); Bm[a, b] = Bm[b, a] = 1 / np.sqrt(2); B.append(Bm)
        self.B = np.array(B)
        Wt = self.W
        self.W0 = np.trace(Wt, axis1=1, axis2=2) / 3.
        A = (Wt - Wt.transpose(0, 2, 1, 3)) / 2
        LC = np.array([[[levi(c, a, b) for b in range(3)] for a in range(3)] for c in range(3)])
        self.W1 = 0.5 * np.einsum('cab,kabp->kcp', LC, A)        # D_c = (1/2) eps_cab A_ab
        S = (Wt + Wt.transpose(0, 2, 1, 3)) / 2 - self.W0[:, None, None, :] * np.eye(3)[None, :, :, None]
        self.W2 = np.einsum('kabp,mab->kmp', S, self.B)
        # G-entry lookup: flat index d*N + a  for G[a, nbr[d, a]]
        look = {}
        for d in range(len(DISPS)):
            for a in range(N):
                look.setdefault((a, int(self.nbr[d, a])), d * N + a)
        self.gij = np.array([look[(i, j)] for i, j in zip(self.pi, self.pj)], int)
        self.gji = np.array([look[(j, i)] for i, j in zip(self.pi, self.pj)], int)
        self.idx4 = np.array([[[look[(int(S[u]), int(S[v]))] for v in range(4)] for u in range(4)] for S in self.sets], int).reshape(-1, 4, 4)
        self.rows0 = 2 * np.arange(N)

    def cluster_strings(self, k):
        out = {}
        for p in range(self.np_):
            M = self.W[k, :, :, p]
            for a in range(3):
                for b in range(3):
                    if M[a, b] != 0:
                        add(out, tuple(sorted(((int(self.pi[p]), a), (int(self.pj[p]), b)))), M[a, b])
        for q in range(self.ns):
            S = self.sets[q]
            for pi in range(3):
                w = self.W4[k, q, pi]
                if w == 0: continue
                (u, v), (x, y) = PAIRINGS[pi]
                for a in range(3):
                    for b in range(3):
                        add(out, tuple(sorted(((int(S[u]), a), (int(S[v]), a), (int(S[x]), b), (int(S[y]), b)))), w)
        return clean(out)

    def gram(self, strs):
        n = len(strs); G = np.zeros((n, n))
        for i in range(n):
            for j in range(i, n):
                G[i, j] = G[j, i] = hs(strs[i], strs[j]) / self.N
        return G


# ------------------------------------------------------------------ exact application (N <= 16)
def zarrays(N):
    b = np.arange(2 ** N, dtype=np.int64)
    return [(1 - 2 * ((b >> i) & 1)).astype(float) for i in range(N)]


def apply_strings(strs, psi, Z):
    idx = np.arange(len(psi)); out = np.zeros_like(psi)
    for key, c in strs.items():
        mask = 0; ph = c
        for site, b in key:
            if b < 2: mask |= 1 << site
            if b == 1: ph = ph * (-1j * Z[site])
            elif b == 2: ph = ph * Z[site]
        out += ph * psi[idx ^ mask]
    return out


def exact_C(strs, psi, Z, N):
    phis = np.array([apply_strings(s, psi, Z) for s in strs])
    ex = phis.conj() @ psi
    C = (phis.conj() @ phis.T) - np.outer(ex.conj(), ex)
    return C.real / N, ex.real / N, phis


# ------------------------------------------------------------------ local estimators
EYE4 = np.eye(4, dtype=complex)


def estimators(T, Phi, Q, s, mode):
    """Per-configuration local estimators.  'full': E (n_ops,) complex.  'singlet': (E0 (n), E1 (n,3), E2 (n,5))."""
    N = T.N
    Pa = Phi[T.rows0 + 1 - s]
    Gd = np.empty((len(DISPS), N), complex)
    for d in range(len(DISPS)):
        Gd[d] = np.einsum('an,na->a', Pa, Q[:, T.nbr[d]])
    Gf = Gd.ravel(); R1 = Gd[0]; z = 1. - 2. * s
    zi, zj = z[T.pi], z[T.pj]
    R2 = R1[T.pi] * R1[T.pj] - Gf[T.gij] * Gf[T.gji]
    # four-spin (dual SU(2)-invariant) estimators: (s_u.s_v)(s_x.s_y) = 4 P_uv P_xy - 2 P_uv - 2 P_xy + 1
    E4 = 0.
    if T.ns:
        G4 = Gf[T.idx4]; s4 = s[T.sets]; Y = np.empty((T.ns, 3), complex)
        for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
            c1 = s4[:, u] != s4[:, v]; c2 = s4[:, x] != s4[:, y]
            r1 = np.where(c1, G4[:, u, u] * G4[:, v, v] - G4[:, u, v] * G4[:, v, u], 1.)
            r2 = np.where(c2, G4[:, x, x] * G4[:, y, y] - G4[:, x, y] * G4[:, y, x], 1.)
            ch = np.zeros((T.ns, 4), bool); ch[:, u] = ch[:, v] = c1; ch[:, x] = ch[:, y] = c2
            Mm = np.where(ch[:, :, None] & ch[:, None, :], G4, EYE4[None])
            Y[:, pi] = 4. * np.linalg.det(Mm) - 2. * r1 - 2. * r2 + 1.
        E4 = np.einsum('kqp,qp->k', T.W4, Y)
    if mode == "full":
        one = np.ones(N, complex); cc = [one, -1j * z, z.astype(complex)]
        X = np.empty((3, 3, T.np_), complex)
        for a in range(3):
            for b in range(3):
                r = R2 if (a < 2 and b < 2) else (R1[T.pi] if a < 2 else (R1[T.pj] if b < 2 else 1.))
                X[a, b] = cc[a][T.pi] * cc[b][T.pj] * r
        return np.einsum('kabp,abp->k', T.W, X) + E4
    X0 = zi * zj + (1. - zi * zj) * R2
    X1 = 1j * (zi - zj) * R2
    X2 = zi * zj - X0 / 3.
    return T.W0 @ X0 + E4, np.einsum('kcp,p->kc', T.W1, X1), np.einsum('kmp,p->km', T.W2, X2)


def pack(est, mode):
    if mode == "full":
        return est
    E0, E1, E2 = est
    return np.concatenate([E0, E1.ravel(), E2.ravel()])


def cov_from_samples(S, n, mode, N, w=None):
    """S: (n_samples, width) packed estimators.  Returns C (per site, real) and <h> (per site)."""
    if w is None: w = np.full(len(S), 1. / len(S))
    if mode == "full":
        m = w @ S
        C = (S.conj().T * w) @ S - np.outer(m.conj(), m)
        return C.real / N, m.real / N
    E0 = S[:, :n]; E1 = S[:, n:4 * n].reshape(-1, n, 3); E2 = S[:, 4 * n:9 * n].reshape(-1, n, 5)
    m = w @ E0
    C0 = (E0.conj().T * w) @ E0 - np.outer(m.conj(), m)
    C1 = np.einsum('s,sic,sjc->ij', w, E1.conj(), E1)
    C2 = 1.5 * np.einsum('s,sim,sjm->ij', w, E2.conj(), E2)
    return (C0 + C1 + C2).real / N, m.real / N


def releig(C, G, tol=1e-9):
    """Generalized eigenproblem C v = lam G v on the range of G.  Returns lam (ascending) and coefficient vectors
    normalized to v^T G v = 1."""
    w, U = np.linalg.eigh(G); keep = w > tol * w.max()
    T = U[:, keep] / np.sqrt(w[keep])
    lam, V = np.linalg.eigh(T.T @ C @ T)
    return lam, T @ V


# ------------------------------------------------------------------ VMC (A44/A46 move set)
def vmc(T, Phi, nsweep, ntherm, seed, tlimit, mode, conserve, nup=None, every=1):
    """Samples packed estimators every `every` sweeps; also records sum_{i down}|R1_i|^2 and sum_{i up}|R1_i|^2
    (bridge estimators for sector weights).  conserve=True: exchange moves on NN bonds only (fixed n_up)."""
    cl = T.cl; N = cl.N; rng = np.random.default_rng(seed); rows0 = T.rows0
    if nup is None: nup = N // 2
    for _ in range(2000):
        s = rng.permutation(np.r_[np.zeros(nup, int), np.ones(N - nup, int)])
        M = Phi[rows0 + s]
        if np.linalg.cond(M) < 1e10: break
    Q = np.linalg.inv(M); bi, bj = cl.bi, cl.bj
    acc = [0, 0, 0, 0]; samples = []; bridge = []; drift = 0.; t0 = time.time()
    for sw in range(ntherm + nsweep):
        for _ in range(N):
            if (not conserve) and rng.random() < 0.5:
                i = rng.integers(N); v = Phi[2 * i + 1 - s[i]]; R = v @ Q[:, i]; acc[1] += 1
                if rng.random() < abs(R) ** 2:
                    u = v @ Q; u[i] -= 1.; Q -= np.outer(Q[:, i], u) / R; s[i] = 1 - s[i]; acc[0] += 1
            else:
                b = rng.integers(len(bi)); i, j = bi[b], bj[b]
                if conserve and s[i] == s[j]:
                    acc[3] += 1; continue
                vi, vj = Phi[2 * i + 1 - s[i]], Phi[2 * j + 1 - s[j]]; Qc = Q[:, [i, j]]
                Rm = np.array([[vi @ Qc[:, 0], vi @ Qc[:, 1]], [vj @ Qc[:, 0], vj @ Qc[:, 1]]])
                R = Rm[0, 0] * Rm[1, 1] - Rm[0, 1] * Rm[1, 0]; acc[3] += 1
                if rng.random() < abs(R) ** 2:
                    U = np.vstack([vi @ Q, vj @ Q]); U[0, i] -= 1.; U[1, j] -= 1.
                    Q -= Qc @ np.linalg.solve(Rm, U); s[i], s[j] = 1 - s[i], 1 - s[j]; acc[2] += 1
        if sw % 10 == 0 or sw == ntherm + nsweep - 1:
            Qf = np.linalg.inv(Phi[rows0 + s]); drift = max(drift, np.abs(Q - Qf).max() / np.abs(Qf).max()); Q = Qf
        if sw < ntherm or (sw - ntherm) % every:
            continue
        samples.append(pack(estimators(T, Phi, Q, s, mode), mode))
        R1 = np.einsum('in,ni->i', Phi[rows0 + 1 - s], Q)
        bridge.append([np.sum(np.abs(R1[s == 1]) ** 2), np.sum(np.abs(R1[s == 0]) ** 2)])
        if time.time() - t0 > tlimit:
            break
    return np.array(samples), np.array(bridge), dict(acc=acc, drift=drift, secs=time.time() - t0)
