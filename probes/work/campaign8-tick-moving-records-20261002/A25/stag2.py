"""A25 shared module: real-space operators for a linear symmetric-tensor (spin-2-like)
field on a periodic cubic lattice.  Supplied toy algebra only; nothing here is framework content.

Layouts
  'stag'    : staggered (Yee/Regge-type) geometric layout, cell = vertex x in Z_L^3.
              h_ii, p_ii at the vertex x;  h_ij, p_ij (i<j) at the face centre x+(e_i+e_j)/2;
              gauge vector xi_i at the edge centre x+e_i/2;  C=curl h: C_ll at the cube centre,
              C_lj, C_jl (l!=j) at the edge centre x+e_m/2 (m = third axis).
              A field component is stored with offset bits o in {0,1}^3 (position x + o/2).
              Every derivative is one half-step difference (symbol i*2 sin(k/2) in the
              half-shift Fourier convention).
  'central' : every component at the site; d_k = (f(x+e_k)-f(x-e_k))/2 (symbol i sin k).
  'forward' : every component at the site; d_k = f(x+e_k)-f(x) (one-sided).

Coordinates: independent components h_ij (i<=j) and their canonical momenta p_ij.
  H_kin = 1/2 p.Mp.p,  ADM/DeWitt:  H_kin = pi:pi - 1/2 (tr pi)^2 with p_ii = pi_ii, p_ij = 2 pi_ij.
  V(h)  = 1/4 sum C:C^T with C = curl h  (= linearized Einstein-Hilbert potential, symbol V_EH(s)).
Matrices are component-major: index = comp * n_cells + cell.
"""
import itertools
import numpy as np
import scipy.sparse as sp

EPS = np.zeros((3, 3, 3))
for a, b, c in itertools.permutations(range(3)):
    EPS[a, b, c] = np.linalg.det(np.eye(3)[[a, b, c]])

H_PAIR = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
C_PAIR = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)]


def bits(*ax):
    o = [0, 0, 0]
    for a in ax:
        o[a] = 1
    return tuple(o)


def hidx(i, j):
    return H_PAIR.index((min(i, j), max(i, j)))


def cidx(l, j):
    return C_PAIR.index((l, j))


# offsets (staggered layout)
H_OFF = [bits(), bits(), bits(), bits(0, 1), bits(0, 2), bits(1, 2)]
XI_OFF = [bits(0), bits(1), bits(2)]
C_OFF = [bits(0, 1, 2)] * 3 + [bits(3 - l - j) for (l, j) in C_PAIR[3:]]
VERT_OFF = [bits()]
CUBE_OFF = [bits(0, 1, 2)]
FACEP_OFF = [tuple(1 - b for b in bits(j)) for j in range(3)]   # face perpendicular to axis j


class Lat:
    def __init__(self, L):
        self.L = L
        self.n = L ** 3
        idx = np.arange(self.n).reshape(L, L, L)
        self.coords = np.array(np.unravel_index(np.arange(self.n), (L, L, L))).T
        I = sp.identity(self.n, format='csr')
        self.Sp, self.Sm = [], []
        for k in range(3):
            tgt = np.roll(idx, -1, axis=k).ravel()          # tgt[x] = index of x+e_k
            S = sp.csr_matrix((np.ones(self.n), (idx.ravel(), tgt)), shape=(self.n, self.n))
            self.Sp.append(S)                                 # (S f)(x) = f(x+e_k)
            self.Sm.append(S.T.tocsr())                       # (S f)(x) = f(x-e_k)
        self.I = I

    def d(self, k, bit_in, mode):
        if mode == 'stag':
            return (self.Sp[k] - self.I) if bit_in == 0 else (self.I - self.Sm[k])
        if mode == 'central':
            return 0.5 * (self.Sp[k] - self.Sm[k])
        if mode == 'forward':
            return self.Sp[k] - self.I
        raise ValueError(mode)


def toggle(o, k):
    o = list(o)
    o[k] = 1 - o[k]
    return tuple(o)


def assemble(lat, out_off, in_off, terms, mode):
    """terms: list of (a_out, b_in, coeff, axes).  Builds sum coeff * prod_k d_k as a block matrix.
    In 'stag' mode the offset bookkeeping is asserted (every term must land on the output role)."""
    n = lat.n
    blocks = [[None] * len(in_off) for _ in out_off]
    for a, b, c, axes in terms:
        o = in_off[b] if mode == 'stag' else (0, 0, 0)
        M = lat.I
        for k in axes:
            M = lat.d(k, o[k], mode) @ M
            if mode == 'stag':
                o = toggle(o, k)
        if mode == 'stag':
            assert o == out_off[a], (a, b, axes, o, out_off[a])
        blk = c * M
        blocks[a][b] = blk if blocks[a][b] is None else blocks[a][b] + blk
    for a in range(len(out_off)):
        for b in range(len(in_off)):
            if blocks[a][b] is None:
                blocks[a][b] = sp.csr_matrix((n, n))
    return sp.bmat(blocks, format='csr')


def build(L, mode='stag'):
    lat = Lat(L)
    ops = {'lat': lat, 'mode': mode}
    # gauge generator xi -> h :  dh_ii = 2 d_i xi_i ; dh_ij = d_i xi_j + d_j xi_i
    t = [(i, i, 2.0, (i,)) for i in range(3)]
    for a, (i, j) in enumerate(H_PAIR):
        if i != j:
            t += [(a, j, 1.0, (i,)), (a, i, 1.0, (j,))]
    ops['D'] = assemble(lat, H_OFF, XI_OFF, t, mode)
    # curl: C_lj = eps_lki d_k h_ij
    t = []
    for c, (l, j) in enumerate(C_PAIR):
        for k in range(3):
            for i in range(3):
                if EPS[l, k, i] != 0:
                    t.append((c, hidx(i, j), EPS[l, k, i], (k,)))
    ops['Curl'] = assemble(lat, C_OFF, H_OFF, t, mode)
    # transpose pairing J on C
    n = lat.n
    rows, cols = [], []
    for c, (l, j) in enumerate(C_PAIR):
        c2 = cidx(j, l)
        rows += list(c * n + np.arange(n))
        cols += list(c2 * n + np.arange(n))
    ops['J'] = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(9 * n, 9 * n))
    ops['Vp'] = (0.5 * ops['Curl'].T @ ops['J'] @ ops['Curl']).tocsr()
    # DeWitt kinetic matrix (on-site)
    m = np.zeros((6, 6))
    m[:3, :3] = 2 * np.eye(3) - np.ones((3, 3))
    m[3:, 3:] = np.eye(3)
    ops['m_onsite'] = m
    ops['Mp'] = sp.kron(sp.csr_matrix(m), sp.identity(n), format='csr')
    # Hamiltonian constraint R(h) = d_i d_j h_ij - lap tr h  (vertex)
    t = []
    for a, (i, j) in enumerate(H_PAIR):
        if i != j:
            t.append((0, a, 2.0, (i, j)))
        else:
            for k in range(3):
                if k != i:
                    t.append((0, a, -1.0, (k, k)))
    ops['R'] = assemble(lat, VERT_OFF, H_OFF, t, mode)
    ops['Div'] = assemble(lat, VERT_OFF, XI_OFF, [(0, j, 1.0, (j,)) for j in range(3)], mode)
    # compatibility rows of C: (div_1 C)_j = d_l C_lj (face perp to j); tr C (cube)
    ops['div1C'] = assemble(lat, FACEP_OFF, C_OFF,
                            [(j, cidx(l, j), 1.0, (l,)) for j in range(3) for l in range(3)], mode)
    ops['trC'] = assemble(lat, CUBE_OFF, C_OFF, [(0, cidx(l, l), 1.0, ()) for l in range(3)], mode)
    # Hamiltonian constraint written on C:  R = - eps_ikl d_k C_il
    t = []
    for i in range(3):
        for k in range(3):
            for l in range(3):
                if EPS[i, k, l] != 0:
                    t.append((0, cidx(i, l), -EPS[i, k, l], (k,)))
    ops['RC'] = assemble(lat, VERT_OFF, C_OFF, t, mode)
    return ops


# ------------------------------------------------------------------ leapfrog layers (h,p) form
def layers_hp(ops, tau):
    n6 = ops['Mp'].shape[0]
    I = sp.identity(n6, format='csr')
    Z = sp.csr_matrix((n6, n6))
    K = lambda a: sp.bmat([[I, a * ops['Mp']], [Z, I]], format='csr')
    P = lambda b: sp.bmat([[I, Z], [-b * ops['Vp'], I]], format='csr')
    return K(tau / 2), P(tau), K(tau / 2)


# curl-split (C, p) form: z = (C, p);  C-layer: C += a Curl Mp p ; p-layer: p -= b 1/2 Curl^T J C
def layers_cp(ops, tau):
    nC = ops['Curl'].shape[0]
    n6 = ops['Mp'].shape[0]
    IC = sp.identity(nC, format='csr')
    Ip = sp.identity(n6, format='csr')
    A = (ops['Curl'] @ ops['Mp']).tocsr()
    B = (0.5 * ops['Curl'].T @ ops['J']).tocsr()
    Kc = lambda a: sp.bmat([[IC, a * A], [None, Ip]], format='csr')
    Pp = lambda b: sp.bmat([[IC, None], [-b * B, Ip]], format='csr')
    return Kc(tau / 2), Pp(tau), Kc(tau / 2)


# ------------------------------------------------------------------ Bloch symbols
def bloch(lat, A, out_off, in_off, kvecs, ref_cell=0, mode='stag'):
    """Bloch block A(k)[a,b] = sum_y A[(a,x0),(b,y)] exp(i k.(pos_b(y)-pos_a(x0))), half-shift convention."""
    n, L = lat.n, lat.L
    A = A.tocsr()
    nout, nin = len(out_off), len(in_off)
    res = np.zeros((len(kvecs), nout, nin), complex)
    x0 = lat.coords[ref_cell]
    for a in range(nout):
        r = a * n + ref_cell
        cols = A.indices[A.indptr[r]:A.indptr[r + 1]]
        vals = A.data[A.indptr[r]:A.indptr[r + 1]]
        for col, v in zip(cols, vals):
            b, y = divmod(col, n)
            d = (lat.coords[y] - x0 + L // 2) % L - L // 2   # wrapped displacement
            if mode == 'stag':
                d = d + (np.array(in_off[b]) - np.array(out_off[a])) / 2.0
            res[:, a, b] += v * np.exp(1j * kvecs @ d)
    return res


def kgrid(L):
    g = 2 * np.pi * np.arange(L) / L
    g = np.where(g > np.pi + 1e-12, g - 2 * np.pi, g)
    return np.array(list(itertools.product(g, g, g)))


# ------------------------------------------------------------------ A23 symbols in our ordering
SQ2 = np.sqrt(2.0)


def orth_basis():
    B = []
    for (i, j) in H_PAIR:
        E = np.zeros((3, 3))
        if i == j:
            E[i, i] = 1.0
        else:
            E[i, j] = E[j, i] = 1 / SQ2
        B.append(E)
    return B


def V_EH_orth(s):
    B = orth_basis()

    def V(h):
        return (0.25 * s @ s * np.sum(h * h) - 0.5 * np.sum((h @ s) ** 2)
                + 0.5 * (s @ h @ s) * np.trace(h) - 0.25 * (s @ s) * np.trace(h) ** 2)
    Vm = np.zeros((6, 6))
    for I in range(6):
        Vm[I, I] = 2 * V(B[I])
        for J in range(I + 1, 6):
            Vm[I, J] = Vm[J, I] = V(B[I] + B[J]) - V(B[I]) - V(B[J])
    return Vm


def M_orth_GR():
    a1 = np.array([1, 1, 1, 0, 0, 0]) / np.sqrt(3)
    return 2 * (np.eye(6) - 1.5 * np.outer(a1, a1))


S_ORTH = np.diag([1, 1, 1, SQ2, SQ2, SQ2])     # q = S h (orthonormal coordinates)


def tt_basis_orth(s):
    B = orth_basis()
    sh = s / np.linalg.norm(s)
    a = np.array([1.0, 0, 0]) if abs(sh[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(sh, a); u /= np.linalg.norm(u); w = np.cross(sh, u)
    co = lambda E: np.array([np.sum(Eb * E) for Eb in B])
    e1 = co(np.outer(u, u) - np.outer(w, w)); e2 = co(np.outer(u, w) + np.outer(w, u))
    return np.array([e1 / np.linalg.norm(e1), e2 / np.linalg.norm(e2)]).T


# ------------------------------------------------------------------ rotations (signed permutations)
def signed_perms(proper=None):
    out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3), int)
            for i in range(3):
                R[p[i], i] = sg[i]          # R e_i = sg_i e_{p(i)}
            d = round(np.linalg.det(R))
            if proper is True and d < 0:
                continue
            if proper is False and d > 0:
                continue
            out.append(R)
    return out


def perm_sign(R):
    P = [int(np.nonzero(R[:, i])[0][0]) for i in range(3)]
    s = [int(R[P[i], i]) for i in range(3)]
    return P, s


def rot_matrix(lat, offs, kind, R, centre_bits, mode='stag'):
    """Signed permutation implementing a rotation R about the point centre_bits/2 (staggered
    half-units; for 'central'/'forward' the centre is a site).  kind: 'sym2','vec','scalar','C','pvec'.
    Returns None if R about this centre does not map each role onto the role of the image component."""
    n, L = lat.n, lat.L
    P, s = perm_sign(R)
    det = round(np.linalg.det(R))
    c = np.array(centre_bits)
    rows, cols, vals = [], [], []
    ncomp = len(offs)
    for comp in range(ncomp):
        if kind == 'sym2':
            i, j = H_PAIR[comp]
            img = hidx(P[i], P[j]); sgn = s[i] * s[j]
        elif kind == 'C':
            l, j = C_PAIR[comp]
            img = cidx(P[l], P[j]); sgn = s[l] * s[j] * det
        elif kind == 'vec':
            img = P[comp]; sgn = s[comp]
        elif kind == 'pvec':
            img = P[comp]; sgn = s[comp] * det
        elif kind == 'scalar':
            img = comp; sgn = 1
        o = np.array(offs[comp]) if mode == 'stag' else np.zeros(3, int)
        p2 = 2 * lat.coords + o                       # positions in half-units
        if mode == 'stag':
            q2 = (p2 - c) @ R.T + c
        else:
            q2 = (p2 - 2 * c) @ R.T + 2 * c
        o2 = q2 % 2
        oi = np.array(offs[img]) if mode == 'stag' else np.zeros(3, int)
        if not np.all(o2 == oi):
            return None
        x2 = ((q2 - o2) // 2) % L
        cell2 = (x2[:, 0] * L + x2[:, 1]) * L + x2[:, 2]
        rows += list(img * n + cell2)
        cols += list(comp * n + np.arange(n))
        vals += [sgn] * n
    return sp.csr_matrix((vals, (rows, cols)), shape=(ncomp * n, ncomp * n))


def maxabs(A):
    A = A.tocsr() if sp.issparse(A) else A
    if sp.issparse(A):
        A.eliminate_zeros()
        return 0.0 if A.nnz == 0 else float(np.max(np.abs(A.data)))
    return float(np.max(np.abs(A))) if A.size else 0.0
