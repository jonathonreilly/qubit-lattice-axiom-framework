#!/usr/bin/env python3
"""
Grid-free classification of bounded real-linear covariant nearest-neighbour flows on the
vertex-edge-face-cube cochain complex of the cubic torus, and what the two Gauss rows
add inside it.   Task: review-20260929-wall-local-code-and-gauge-selection (T79 neighbourhood).

Machinery (disjoint from the sources' role-compiled doubled-lattice runners):
  * oriented cochain complex d0 (E x V), C (F x E), d2 (Cube x F) built from cell data;
  * proper cubic rotations acting on oriented cells as signed permutations (chain maps);
  * exact integer / Fraction / sympy linear algebra; floating point only where labelled NUMERIC.

Premises of the classified class (all SUPPLIED, none derived from the four axioms):
  one real component per vertex (phi), edge (E), face (B), cube (psi); real, linear,
  first-order, continuous-time generator; nearest-neighbour = incident cells or the same cell;
  covariance under translations and the 24 proper rotations about a vertex.
Stability notion: every orbit bounded for all t in R (both time directions).
"""
import sys, itertools, time
from fractions import Fraction as Fr
import numpy as np
import scipy.sparse as sp
import scipy.linalg as sla
import sympy as sps

T0 = time.time()
RESULTS = []


def rec(ok, msg):
    RESULTS.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + msg, flush=True)


# ----------------------------------------------------------------------------------------
# 1. oriented cochain complex of the cubic torus Z_L^3
# ----------------------------------------------------------------------------------------
class Complex:
    def __init__(self, L):
        self.L = L
        self.nV = L ** 3
        self.nE = 3 * L ** 3
        self.nF = 3 * L ** 3
        self.nC = L ** 3
        self.oE = self.nV
        self.oF = self.nV + self.nE
        self.oC = self.nV + self.nE + self.nF
        self.N = self.nV + self.nE + self.nF + self.nC
        L_ = L
        self.coords = [(x, y, z) for x in range(L_) for y in range(L_) for z in range(L_)]
        d0 = sp.lil_matrix((self.nE, self.nV), dtype=np.int64)
        Cm = sp.lil_matrix((self.nF, self.nE), dtype=np.int64)
        d2 = sp.lil_matrix((self.nC, self.nF), dtype=np.int64)
        for v in self.coords:
            for i in range(3):
                e = self.eidx(v, i)
                d0[e, self.vidx(self.sh(v, i, 1))] += 1
                d0[e, self.vidx(v)] += -1
                k = i
                a, b = (k + 1) % 3, (k + 2) % 3
                f = self.fidx(v, k)
                Cm[f, self.eidx(v, a)] += 1
                Cm[f, self.eidx(self.sh(v, a, 1), b)] += 1
                Cm[f, self.eidx(self.sh(v, b, 1), a)] += -1
                Cm[f, self.eidx(v, b)] += -1
                c = self.cidx(v)
                d2[c, self.fidx(self.sh(v, k, 1), k)] += 1
                d2[c, self.fidx(v, k)] += -1
        self.d0 = d0.tocsr()
        self.C = Cm.tocsr()
        self.d2 = d2.tocsr()

    def sh(self, v, axis, s):
        w = list(v)
        w[axis] = (w[axis] + s) % self.L
        return tuple(w)

    def vidx(self, v):
        L = self.L
        return ((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)

    def eidx(self, v, i):
        return 3 * self.vidx(v) + i

    def fidx(self, v, k):
        return 3 * self.vidx(v) + k

    def cidx(self, v):
        return self.vidx(v)

    # global index helpers
    def gE(self, e): return self.oE + e
    def gF(self, f): return self.oF + f
    def gC(self, c): return self.oC + c

    def generator_blocks(self):
        """The ten basic generators as sparse N x N integer matrices, keyed by coefficient name.
        State order (phi, E, B, psi).  Row = component whose derivative is formed."""
        N = self.N
        def blk(rows_off, cols_off, M, shape):
            M = sp.coo_matrix(M)
            return sp.coo_matrix((M.data, (M.row + rows_off, M.col + cols_off)), shape=(N, N)).tocsr()
        I = sp.identity
        G = {}
        G['w'] = blk(0, 0, I(self.nV, dtype=np.int64), None)
        G['u'] = blk(self.oE, self.oE, I(self.nE, dtype=np.int64), None)
        G['v'] = blk(self.oF, self.oF, I(self.nF, dtype=np.int64), None)
        G['wc'] = blk(self.oC, self.oC, I(self.nC, dtype=np.int64), None)
        G['gve'] = blk(0, self.oE, self.d0.T, None)      # phi' <- d0^T E
        G['gev'] = blk(self.oE, 0, self.d0, None)        # E'   <- d0 phi
        G['r'] = blk(self.oE, self.oF, self.C.T, None)   # E'   <- C^T B
        G['q'] = blk(self.oF, self.oE, self.C, None)     # B'   <- C E
        G['gbc'] = blk(self.oF, self.oC, self.d2.T, None)  # B' <- d2^T psi
        G['gcb'] = blk(self.oC, self.oF, self.d2, None)  # psi' <- d2 B
        return G


NAMES = ['w', 'u', 'v', 'wc', 'gve', 'gev', 'q', 'r', 'gbc', 'gcb']


def sparse_equal(A, B):
    return (A != B).nnz == 0


# ----------------------------------------------------------------------------------------
# 2. rotations and translations as signed permutations on oriented cells
# ----------------------------------------------------------------------------------------
def rot_matrix(axis, quarter=1):
    c, s = 0, 1
    if axis == 'z':
        R = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    elif axis == 'x':
        R = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    else:
        R = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    out = np.eye(3, dtype=int)
    for _ in range(quarter):
        out = R @ out
    return out


def rot_rep(cx, R):
    """Signed permutation on the global cochain space induced by the proper rotation R about vertex 0."""
    L = cx.L
    N = cx.N
    rows, cols, vals = [], [], []
    def cvec(v):
        return np.array(v, dtype=int)
    for v in cx.coords:
        vv = tuple(int(t) % L for t in (R @ cvec(v)))
        rows.append(cx.vidx(vv)); cols.append(cx.vidx(v)); vals.append(1)
        for i in range(3):
            col = R[:, i]
            j = int(np.nonzero(col)[0][0]); s = int(col[j])
            base = np.array(vv)
            if s < 0:
                base[j] -= 1
            rows.append(cx.oE + cx.eidx(tuple(base % L), j)); cols.append(cx.oE + cx.eidx(v, i)); vals.append(s)
        for k in range(3):
            a, b = (k + 1) % 3, (k + 2) % 3
            base = np.array(vv)
            for m in (a, b):
                col = R[:, m]
                j = int(np.nonzero(col)[0][0]); s = int(col[j])
                if s < 0:
                    base[j] -= 1
            colk = R[:, k]
            c_ax = int(np.nonzero(colk)[0][0]); sk = int(colk[c_ax])
            rows.append(cx.oF + cx.fidx(tuple(base % L), c_ax)); cols.append(cx.oF + cx.fidx(v, k)); vals.append(sk)
        base = np.array(vv)
        for m in range(3):
            col = R[:, m]
            j = int(np.nonzero(col)[0][0]); s = int(col[j])
            if s < 0:
                base[j] -= 1
        rows.append(cx.oC + cx.cidx(tuple(base % L))); cols.append(cx.oC + cx.cidx(v)); vals.append(1)
    return sp.coo_matrix((vals, (rows, cols)), shape=(N, N)).tocsr()


def trans_rep(cx, axis):
    L = cx.L
    N = cx.N
    rows, cols = [], []
    for v in cx.coords:
        w = cx.sh(v, axis, 1)
        rows.append(cx.vidx(w)); cols.append(cx.vidx(v))
        for i in range(3):
            rows.append(cx.oE + cx.eidx(w, i)); cols.append(cx.oE + cx.eidx(v, i))
            rows.append(cx.oF + cx.fidx(w, i)); cols.append(cx.oF + cx.fidx(v, i))
        rows.append(cx.oC + cx.cidx(w)); cols.append(cx.oC + cx.cidx(v))
    return sp.coo_matrix((np.ones(len(rows), dtype=np.int64), (rows, cols)), shape=(N, N)).tocsr()


def coboundary_total(cx):
    """Block operator D mapping (phi,E,B,psi) -> (0, d0 phi, C E, d2 B)."""
    N = cx.N
    D = sp.lil_matrix((N, N), dtype=np.int64)
    D[cx.oE:cx.oE + cx.nE, 0:cx.nV] = cx.d0
    D[cx.oF:cx.oF + cx.nF, cx.oE:cx.oE + cx.nE] = cx.C
    D[cx.oC:cx.oC + cx.nC, cx.oF:cx.oF + cx.nF] = cx.d2
    return D.tocsr()


# ----------------------------------------------------------------------------------------
# helpers: exact rank / nullspace over Q using Fractions
# ----------------------------------------------------------------------------------------
def frac_rank(M):
    """Exact rank of an integer matrix (list of lists or sparse) by Fraction Gaussian elimination."""
    A = [[Fr(int(x)) for x in row] for row in (M.toarray() if sp.issparse(M) else M)]
    rows = len(A); cols = len(A[0]) if rows else 0
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i][c] != 0:
                piv = i; break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        for i in range(r + 1, rows):
            if A[i][c] != 0:
                f = A[i][c] / pv
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
        if r == rows:
            break
    return r


# ----------------------------------------------------------------------------------------
# STEP A. complex identities and Betti numbers (exact)
# ----------------------------------------------------------------------------------------
def step_A(L):
    cx = Complex(L)
    ok1 = (cx.C @ cx.d0).nnz == 0
    ok2 = (cx.d2 @ cx.C).nnz == 0
    rec(ok1 and ok2, f"A1 L={L}: C d0 = 0 and d2 C = 0 exactly (integer matrices {cx.nE}x{cx.nV}, {cx.nF}x{cx.nE}, {cx.nC}x{cx.nF})")
    r0, r1, r2 = frac_rank(cx.d0), frac_rank(cx.C), frac_rank(cx.d2)
    b = (cx.nV - r0, cx.nE - r0 - r1, cx.nF - r1 - r2, cx.nC - r2)
    rec(b == (1, 3, 3, 1), f"A2 L={L}: Betti numbers of the torus complex from exact ranks = {b} (expected (1,3,3,1))")
    return cx


# ----------------------------------------------------------------------------------------
# STEP B. independent derivation of the covariant nearest-neighbour class (dimension 10)
# ----------------------------------------------------------------------------------------
def step_B(L):
    cx = Complex(L)
    N = cx.N
    Rz = rot_rep(cx, rot_matrix('z'))
    Rx = rot_rep(cx, rot_matrix('x'))
    D = coboundary_total(cx)
    okchain = True
    for P in (Rz, Rx):
        okchain &= (P @ D - D @ P).nnz == 0
        okchain &= ((P @ P.T) != sp.identity(N, dtype=np.int64)).nnz == 0
    rec(okchain, f"B1 L={L}: rotation representations are orthogonal signed permutations and chain maps (P D = D P)")
    # nearest-neighbour support pairs (global indices): same cell, or incident cells in adjacent degrees
    pairs = set()
    for a in range(N):
        pairs.add((a, a))
    for (A, offr, offc) in ((cx.d0, cx.oE, 0), (cx.C, cx.oF, cx.oE), (cx.d2, cx.oC, cx.oF)):
        Ac = sp.coo_matrix(A)
        for r_, c_ in zip(Ac.row, Ac.col):
            pairs.add((int(r_ + offr), int(c_ + offc)))
            pairs.add((int(c_ + offc), int(r_ + offr)))
    # translation orbits of the support pairs
    Ts = [trans_rep(cx, ax) for ax in range(3)]
    perms = []
    for T in Ts:
        Tc = sp.coo_matrix(T)
        p = np.zeros(N, dtype=int)
        p[Tc.col] = Tc.row           # old index -> new index
        perms.append(p)
    # all translations: compose
    allperm = []
    for dx in range(L):
        for dy in range(L):
            for dz in range(L):
                p = np.arange(N)
                for _ in range(dx): p = perms[0][p]
                for _ in range(dy): p = perms[1][p]
                for _ in range(dz): p = perms[2][p]
                allperm.append(p)
    allperm = np.array(allperm)
    orbit_of = {}
    orbits = []
    for pr in sorted(pairs):
        if pr in orbit_of:
            continue
        k = len(orbits)
        members = set()
        for p in allperm:
            members.add((int(p[pr[0]]), int(p[pr[1]])))
        for m in members:
            orbit_of[m] = k
        orbits.append(sorted(members))
    nO = len(orbits)
    rec(len(pairs) == sum(len(o) for o in orbits), f"B2 L={L}: {len(pairs)} nearest-neighbour entries fall in {nO} translation orbits")
    Gk = []
    for o in orbits:
        rows = [a for a, b in o]; cols = [b for a, b in o]
        Gk.append(sp.coo_matrix((np.ones(len(o), dtype=np.int64), (rows, cols)), shape=(N, N)).tocsr())
    # constraint columns: vec(G P - P G) for the two rotation generators
    cols_data = []
    big_r, big_c, big_v = [], [], []
    for k, G in enumerate(Gk):
        off = 0
        for P in (Rz, Rx):
            Acm = (G @ P - P @ G).tocoo()
            big_r.extend((Acm.row.astype(np.int64) * N + Acm.col + off).tolist())
            big_c.extend([k] * Acm.nnz)
            big_v.extend(Acm.data.tolist())
            off += N * N
    Amat = sp.coo_matrix((big_v, (big_r, big_c)), shape=(2 * N * N, nO)).tocsr()
    Gram = (Amat.T @ Amat).toarray().astype(object)
    # exact nullspace of the Gram matrix (null(A) = null(A^T A) over Q)
    Msym = sps.Matrix(nO, nO, lambda i, j: int(Gram[i, j]))
    ns = Msym.nullspace()
    rec(len(ns) == 10, f"B3 L={L}: dimension of the covariant nearest-neighbour class (exact nullspace) = {len(ns)} (expected 10)")
    # expected generators lie in it and span it
    blocks = cx.generator_blocks()
    # orbit coefficient of an expected generator: entry value at a representative pair
    coefs = []
    ok_translation = True
    for nme in NAMES:
        Gm = blocks[nme].tocsr()
        c = []
        recon = sp.csr_matrix((N, N), dtype=np.int64)
        for k, o in enumerate(orbits):
            a, b = o[0]
            val = int(Gm[a, b])
            c.append(val)
            recon = recon + val * Gk[k]
        ok_translation &= sparse_equal(recon, Gm)
        coefs.append(c)
    rec(ok_translation, f"B4 L={L}: the ten named generators (w,u,v,wc,gve,gev,q,r,gbc,gcb) are translation invariant NN stencils")
    cm = sps.Matrix(coefs)
    resid = Msym * cm.T
    rec(all(x == 0 for x in resid), f"B5 L={L}: each named generator commutes with both rotation generators (exact, via Gram)")
    rec(cm.rank() == 10, f"B6 L={L}: the ten named generators are linearly independent, so they span the whole class")
    return cx


# ----------------------------------------------------------------------------------------
# STEP C. necessity: explicit eigen / Jordan subspaces with exact rational vectors
# ----------------------------------------------------------------------------------------
COS = {2: Fr(-1), 3: Fr(-1, 2), 4: Fr(0), 6: Fr(1, 2)}


def cos_table(L):
    c = COS[L]
    t = [Fr(1), c]
    for _ in range(2, L):
        t.append(2 * c * t[-1] - t[-2])
    return t[:L]


def vec_apply(M, x):
    """sparse integer matrix times Fraction vector -> list of Fractions (exact)"""
    M = sp.csr_matrix(M)
    out = [Fr(0)] * M.shape[0]
    for i in range(M.shape[0]):
        s = Fr(0)
        for jj in range(M.indptr[i], M.indptr[i + 1]):
            xv = x[M.indices[jj]]
            if xv != 0:
                s += int(M.data[jj]) * xv
        out[i] = s
    return out


def coords_of(v):
    return v


def step_C(L):
    cx = Complex(L)
    blocks = cx.generator_blocks()
    N = cx.N
    ct = cos_table(L)
    lam = 2 - 2 * COS[L]
    zero = [Fr(0)] * N

    def put(vec, off, idx, val):
        vec[off + idx] = val

    # (i) constants: phi = 1, E = x-constant field, B = x-constant field (face normal x), psi = 1
    consts = {}
    v = list(zero)
    for p in cx.coords: put(v, 0, cx.vidx(p), Fr(1))
    consts['w'] = v
    v = list(zero)
    for p in cx.coords: put(v, cx.oE, cx.eidx(p, 0), Fr(1))
    consts['u'] = v
    v = list(zero)
    for p in cx.coords: put(v, cx.oF, cx.fidx(p, 0), Fr(1))
    consts['v'] = v
    v = list(zero)
    for p in cx.coords: put(v, cx.oC, cx.cidx(p), Fr(1))
    consts['wc'] = v
    ok = True
    for nme, vec in consts.items():
        for g in NAMES:
            img = vec_apply(blocks[g], vec)
            if g == nme:
                ok &= (img == vec)
            else:
                ok &= all(x == 0 for x in img)
    rec(ok, f"C1 L={L}: the four constant (harmonic) vectors are exact eigenvectors, G h = w h, u h, v h, wc h with every other generator annihilating them")

    # (ii) invariant 2-d subspaces, built from the x-dependent Fourier mode cos(2 pi x / L)
    # gradient pair:   b1 = (phi,0,0,0), b2 = (0,d0 phi,0,0)
    phi = list(zero)
    for p in cx.coords: put(phi, 0, cx.vidx(p), ct[p[0]])
    dphi = vec_apply(cx.d0, phi[:cx.nV])
    b2 = list(zero)
    for e in range(cx.nE): b2[cx.oE + e] = dphi[e]
    grad = (phi, b2)
    # transverse pair: b1 = (0,Et,0,0) with Et on y-edges, b2 = (0,0,C Et,0)
    Et = [Fr(0)] * cx.nE
    for p in cx.coords: Et[cx.eidx(p, 1)] = ct[p[0]]
    t1 = list(zero)
    for e in range(cx.nE): t1[cx.oE + e] = Et[e]
    CE = vec_apply(cx.C, Et)
    t2 = list(zero)
    for f in range(cx.nF): t2[cx.oF + f] = CE[f]
    trans = (t1, t2)
    # cube pair: b1 = (0,0,d2^T psi,0), b2 = (0,0,0,psi)
    psi = [Fr(0)] * cx.nC
    for p in cx.coords: psi[cx.cidx(p)] = ct[p[0]]
    BL = vec_apply(cx.d2.T, psi)
    c1 = list(zero)
    for f in range(cx.nF): c1[cx.oF + f] = BL[f]
    c2 = list(zero)
    for c in range(cx.nC): c2[cx.oC + c] = psi[c]
    cube = (c1, c2)

    def coords_in(img, b1, b2):
        # solve img = a b1 + b b2 exactly
        a = b = None
        # find pivot entries
        import itertools as it
        i1 = next(i for i, x in enumerate(b1) if x != 0)
        i2 = next(i for i, x in enumerate(b2) if x != 0)
        # b1 and b2 live in disjoint blocks, so coefficients read off at pivots
        a = img[i1] / b1[i1]
        b = img[i2] / b2[i2]
        ok = all(img[i] == a * b1[i] + b * b2[i] for i in range(len(img)))
        return a, b, ok

    # lam checks
    chk = []
    # d0^T d0 phi = lam phi
    chk.append(vec_apply(cx.d0.T, dphi) == [lam * x for x in phi[:cx.nV]])
    # C^T C Et = lam Et and d0^T Et = 0
    chk.append(vec_apply(cx.C.T, CE) == [lam * x for x in Et])
    chk.append(all(x == 0 for x in vec_apply(cx.d0.T, Et)))
    # d2 d2^T psi = lam psi and C^T d2^T psi = 0
    chk.append(vec_apply(cx.d2, BL) == [lam * x for x in psi])
    chk.append(all(x == 0 for x in vec_apply(cx.C.T, BL)))
    rec(all(chk), f"C2 L={L}: Fourier-mode identities d0^T d0 phi = l phi, C^T C E = l E, d2 d2^T psi = l psi with l = 2-2cos(2pi/L) = {lam}, plus d0^T E = 0, C^T d2^T psi = 0 (exact)")

    # block matrices as linear functions of the ten coefficients
    p = sps.symbols('w u v wc gve gev q r gbc gcb')
    P = dict(zip(NAMES, p))
    L_ = sps.Rational(lam.numerator, lam.denominator)
    blocks_sym = {}
    allok = True
    for tag, (b1, b2) in (('grad', grad), ('trans', trans), ('cube', cube)):
        M = sps.zeros(2, 2)
        for g in NAMES:
            a1, b1c, ok1 = coords_in(vec_apply(blocks[g], b1), b1, b2)
            a2, b2c, ok2 = coords_in(vec_apply(blocks[g], b2), b1, b2)
            allok &= ok1 and ok2
            M += P[g] * sps.Matrix([[sps.Rational(a1.numerator, a1.denominator), sps.Rational(a2.numerator, a2.denominator)],
                                    [sps.Rational(b1c.numerator, b1c.denominator), sps.Rational(b2c.numerator, b2c.denominator)]])
        blocks_sym[tag] = M
    rec(allok, f"C3 L={L}: each of the three 2-d subspaces is exactly invariant under all ten generators")
    w, u, v, wc, gve, gev, q, r, gbc, gcb = p
    exp_grad = sps.Matrix([[w, gve * L_], [gev, u]])
    exp_trans = sps.Matrix([[u, r * L_], [q, v]])
    exp_cube = sps.Matrix([[v, gbc], [gcb * L_, wc]])
    rec(sps.simplify(blocks_sym['grad'] - exp_grad) == sps.zeros(2, 2) and
        sps.simplify(blocks_sym['trans'] - exp_trans) == sps.zeros(2, 2) and
        sps.simplify(blocks_sym['cube'] - exp_cube) == sps.zeros(2, 2),
        f"C4 L={L}: induced 2x2 blocks are [[w,gve*l],[gev,u]], [[u,r*l],[q,v]], [[v,gbc],[gcb*l,wc]] with l = {lam}")
    return cx


# 2x2 criterion, symbolic (done once)
def step_C5():
    a, b, c, d, t = sps.symbols('a b c d t', real=True)
    M0 = sps.Matrix([[0, b], [c, 0]])
    # M0^2 = b c I
    rec(sps.simplify(M0 * M0 - b * c * sps.eye(2)) == sps.zeros(2, 2),
        "C5 [[0,b],[c,0]]^2 = b c I (symbolic): bc<0 gives e^{tM} = cos(wt) I + sin(wt)/w M bounded (w^2=-bc); bc>0 gives cosh growth; bc=0 and M != 0 gives e^{tM} = I + tM unbounded")
    # exponential in the three cases
    w2 = sps.symbols('omega', positive=True)
    Mb = sps.Matrix([[0, -w2 ** 2], [1, 0]])   # bc = -w^2 < 0
    E = sps.simplify((Mb * t).exp())
    ok_b = all(sps.simplify(sps.diff(E[i, j], t, 2) + w2 ** 2 * E[i, j]) == 0 for i in range(2) for j in range(2))
    Mn = sps.Matrix([[0, 1], [0, 0]])
    En = (Mn * t).exp()
    ok_n = En == sps.Matrix([[1, t], [0, 1]])
    Mg = sps.Matrix([[0, w2 ** 2], [1, 0]])
    Eg = sps.simplify((Mg * t).exp())
    ok_g = sps.simplify(Eg[0, 0] - sps.cosh(w2 * t)) == 0
    rec(ok_b and ok_n and ok_g, "C6 symbolic matrix exponentials: bc<0 oscillates at frequency sqrt(-bc); nilpotent block gives linear growth; bc>0 gives cosh growth")


# ----------------------------------------------------------------------------------------
# STEP D. the decision rule, a certificate for sufficiency, and counts
# ----------------------------------------------------------------------------------------
def bounded_by_rule(par):
    """Exact decision rule proved in ATTEMPT.md (Theorem 1). par: dict of Fractions/ints."""
    if any(par[k] != 0 for k in ('w', 'u', 'v', 'wc')):
        return False
    for a, b in (('gve', 'gev'), ('q', 'r'), ('gbc', 'gcb')):
        pa, pb = par[a], par[b]
        if not ((pa == 0 and pb == 0) or (pa * pb < 0)):
            return False
    return True


def exact_certificate(cx, par):
    """Positive diagonal W with G^T W + W G = 0 exactly (Fractions). Returns (ok, W role weights)."""
    Wv = Fr(1)
    # weights: determine chain V - E - B - C
    a1, a2 = Fr(par['gve']), Fr(par['gev'])
    q_, r_ = Fr(par['q']), Fr(par['r'])
    b1, b2 = Fr(par['gbc']), Fr(par['gcb'])
    We = Wv if (a1 == 0 and a2 == 0) else -a1 * Wv / a2
    Wb = We if (q_ == 0 and r_ == 0) else -r_ * We / q_
    Wc = Wb if (b1 == 0 and b2 == 0) else -b1 * Wb / b2
    if not (We > 0 and Wb > 0 and Wc > 0):
        return False, None
    blocks = cx.generator_blocks()
    N = cx.N
    # G as dict of nonzeros with Fractions
    G = {}
    for nme in NAMES:
        Mc = blocks[nme].tocoo()
        for i, j, val in zip(Mc.row, Mc.col, Mc.data):
            G[(int(i), int(j))] = G.get((int(i), int(j)), Fr(0)) + Fr(par[nme]) * int(val)
    W = [Wv] * cx.nV + [We] * cx.nE + [Wb] * cx.nF + [Wc] * cx.nC
    # (G^T W + W G)_{ij} = G_{ji} W_j + W_i G_{ij}
    keys = set(G.keys()) | {(j, i) for (i, j) in G.keys()}
    ok = all(G.get((j, i), Fr(0)) * W[j] + W[i] * G.get((i, j), Fr(0)) == 0 for (i, j) in keys)
    return ok, (Wv, We, Wb, Wc)


def step_D():
    # sufficiency certificates on L=3 and L=4 for members that are not on any integer grid
    members = [
        dict(w=0, u=0, v=0, wc=0, gve=0, gev=0, q=Fr(2), r=Fr(-1, 3), gbc=0, gcb=0),
        dict(w=0, u=0, v=0, wc=0, gve=Fr(5, 7), gev=Fr(-11, 3), q=Fr(1, 9), r=Fr(-4), gbc=Fr(3, 2), gcb=Fr(-1, 5)),
        dict(w=0, u=0, v=0, wc=0, gve=0, gev=0, q=Fr(-3, 5), r=Fr(7, 2), gbc=Fr(-2), gcb=Fr(13, 4)),
    ]
    for L in (3, 4):
        cx = Complex(L)
        oks = []
        for m in members:
            assert bounded_by_rule(m)
            ok, W = exact_certificate(cx, m)
            oks.append(ok)
        rec(all(oks), f"D1 L={L}: three non-grid members with all pair products negative carry an exact positive diagonal invariant G^T W + W G = 0, hence every orbit is bounded for all t")
    # the same weights make the Gaussian with covariance W^{-1} stationary
    cx = Complex(3)
    m = members[1]
    ok, W = exact_certificate(cx, m)
    rec(ok and W[0] > 0, "D2 L=3: for that member G W^{-1} + W^{-1} G^T = 0, so the Gaussian ensemble with precision W (and its conditioning on any invariant Gauss surface) is stationary; the ensemble carries no information about the flow beyond W")


def step_D3_counts():
    def count(n, fixed_zero=()):
        vals = range(-n, n + 1)
        cnt = 0
        pts = []
        for tup in itertools.product(vals, repeat=10):
            par = dict(zip(NAMES, tup))
            if any(par[k] != 0 for k in fixed_zero):
                continue
            if all(x == 0 for x in tup):
                continue
            if bounded_by_rule({k: Fr(x) for k, x in par.items()}):
                cnt += 1
                pts.append(tup)
        return cnt, pts
    # n=1 full grid is 59049 points, n=2 would be 9.7M: restrict n=2 to the (q,r) plane and to pairs
    c26, _ = count(1)
    c2, pts2 = count(1, fixed_zero=('gev', 'gbc'))
    c8e, _ = count(1, fixed_zero=('gev',))
    c8m, _ = count(1, fixed_zero=('gbc',))
    rec(c26 == 26, f"D3 rule on {{-1,0,1}}^10: {c26} bounded nonzero members (rule-based count; the earlier numerical grid scan reported 26)")
    rec(c2 == 2, f"D4 rule with g_ev = g_bc = 0 on {{-1,0,1}}^10: {c2} members, the pair (q,r) = (1,-1), (-1,1) (earlier scan: 2)")
    rec(c8e == 8 and c8m == 8, f"D5 rule with only the electric row (g_ev=0): {c8e}; only the magnetic row (g_bc=0): {c8m} (earlier scan: 8 and 8)")
    # on {-2..2} in (q,r) with everything else zero
    cnt = sum(1 for q_ in range(-2, 3) for r_ in range(-2, 3)
              if (q_, r_) != (0, 0) and bounded_by_rule({**{k: Fr(0) for k in NAMES}, 'q': Fr(q_), 'r': Fr(r_)}))
    rec(cnt == 8, f"D6 rule on (q,r) in {{-2..2}}^2 with both Gauss rows: {cnt} members; the integer grid gives 2n^2 = 2, 8, 18 ... so the number 2 is a property of the grid {{-1,0,1}}, not of the class")
    # the Maxwell member with speed c = sqrt(-q r): all of qr<0 are bounded
    pts = [(Fr(a), Fr(-b)) for a in range(1, 6) for b in range(1, 6)]
    rec(all(bounded_by_rule({**{k: Fr(0) for k in NAMES}, 'q': a, 'r': b}) for a, b in pts),
        "D7 every (q,r) with q r < 0 (25 sampled, speeds sqrt(ab) from 1 to 5) is in the bounded class: the speed is a free positive parameter")


# ----------------------------------------------------------------------------------------
# STEP E. independent numerical replication on the full 3^10 grid at L=2 (the sources' side 4)
# ----------------------------------------------------------------------------------------
def step_E():
    cx = Complex(2)
    blocks = cx.generator_blocks()
    base = np.array([blocks[n].toarray().astype(float) for n in NAMES])   # 10 x N x N
    N = cx.N
    grid = np.array(list(itertools.product((-1, 0, 1), repeat=10)), dtype=float)
    grid = grid[np.any(grid != 0, axis=1)]
    pred = np.array([bounded_by_rule({k: Fr(int(x)) for k, x in zip(NAMES, row)}) for row in grid])
    num = np.zeros(len(grid), dtype=bool)
    B = 1500
    cand = []
    for s in range(0, len(grid), B):
        chunk = grid[s:s + B]
        Gs = np.tensordot(chunk, base, axes=(1, 0))
        ev = np.linalg.eigvals(Gs)
        mre = np.abs(ev.real).max(axis=1)
        for i in range(len(chunk)):
            if mre[i] < 1e-7:
                cand.append(s + i)
    # candidates: check no Jordan growth through matrix exponential growth
    for idx in cand:
        G = np.tensordot(grid[idx], base, axes=(0, 0))
        n1 = np.linalg.norm(sla.expm(50 * G), 2)
        n2 = np.linalg.norm(sla.expm(200 * G), 2)
        num[idx] = (n2 < 5.0) and (n1 < 5.0)
    agree = np.array_equal(num, pred)
    rec(agree, f"E1 L=2, all {len(grid)} nonzero grid members: numerical boundedness (eigenvalues, then ||expm(50G)||,||expm(200G)||) agrees with the exact rule on every one; bounded count = {int(num.sum())}")
    mask_gauss = (grid[:, NAMES.index('gev')] == 0) & (grid[:, NAMES.index('gbc')] == 0)
    rec(int((num & mask_gauss).sum()) == 2, f"E2 L=2: with g_ev = g_bc = 0 the numerical scan also gives exactly {int((num & mask_gauss).sum())} bounded members on this grid")
    # the non-grid example from the rule, numerically at L=3 and L=2 (speed free)
    for L in (2, 3):
        cx2 = Complex(L)
        bl = cx2.generator_blocks()
        par = dict(w=0, u=0, v=0, wc=0, gve=0, gev=0, q=2.0, r=-1 / 3, gbc=0, gcb=0)
        G = sum(par[n] * bl[n].toarray().astype(float) for n in NAMES)
        ev = np.linalg.eigvals(G)
        ok = ev.real.max() < 1e-9 and np.linalg.norm(sla.expm(300 * G), 2) < 10
        rec(ok, f"E3 L={L}: q=2, r=-1/3 with both Gauss rows (speed sqrt(2/3)) is bounded numerically; max Re(lambda) = {ev.real.max():.1e}")


# ----------------------------------------------------------------------------------------
# STEP F. Gauss rows: exact invariance conditions on the coefficients
# ----------------------------------------------------------------------------------------
def nullspace_basis_int(M):
    """Exact rational nullspace basis (as sympy columns) of an integer sparse matrix."""
    S = sps.Matrix(M.toarray().tolist())
    return S.nullspace()


def int_nullspace(M):
    """Exact integer basis of the rational nullspace of an integer matrix (columns scaled to integers)."""
    ns = sps.Matrix(M.toarray().tolist()).nullspace()
    out = []
    for x in ns:
        den = sps.ilcm(*[sps.fraction(t)[1] for t in x]) if len(x) else 1
        out.append(np.array([int(t * den) for t in x], dtype=np.int64))
    return out


def surface_columns(cx, which, ns):
    N = cx.N
    cols = []
    def unit(i):
        z = np.zeros(N, dtype=np.int64); z[i] = 1; return z
    def emb(off, vec):
        z = np.zeros(N, dtype=np.int64); z[off:off + len(vec)] = vec; return z
    for i in range(cx.nV): cols.append(unit(i))
    if which == 'E':
        for x in ns: cols.append(emb(cx.oE, x))
    else:
        for i in range(cx.nE): cols.append(unit(cx.oE + i))
    if which == 'B':
        for x in ns: cols.append(emb(cx.oF, x))
    else:
        for i in range(cx.nF): cols.append(unit(cx.oF + i))
    for i in range(cx.nC): cols.append(unit(cx.oC + i))
    return np.array(cols, dtype=np.int64).T


def constraint_gram(cx, blocks, S, rowoff, rowlen, op):
    """Gram matrix of the ten maps x -> op (G_j x)[rowoff:rowoff+rowlen] restricted to surface columns S."""
    imgs = []
    for g in NAMES:
        Gj = blocks[g].toarray().astype(np.int64)
        part = (Gj @ S)[rowoff:rowoff + rowlen, :]
        imgs.append((op @ part).ravel())
    V = np.array(imgs, dtype=np.int64)          # 10 x (many)
    return V @ V.T


def step_F(L=3):
    cx = Complex(L)
    blocks = cx.generator_blocks()
    # electric zero-charge row: surface {d0^T E = 0}
    nsE = int_nullspace(cx.d0.T)
    S = surface_columns(cx, 'E', nsE)
    chk = (cx.d0.T.toarray().astype(np.int64) @ S[cx.oE:cx.oE + cx.nE, :])
    assert not chk.any()
    Gm = constraint_gram(cx, blocks, S, cx.oE, cx.nE, cx.d0.T.toarray().astype(np.int64))
    kern = sps.Matrix(Gm.tolist()).nullspace()
    gev_i = NAMES.index('gev')
    ok = (len(kern) == 9) and all(k[gev_i] == 0 for k in kern)
    rec(ok, f"F1 L={L}: invariance of the zero-charge electric surface {{d0^T E = 0}} imposes exactly one coefficient condition on the ten-parameter class, g_ev = 0 (exact nullspace has dimension {len(kern)} and every solution has g_ev = 0)")
    # magnetic zero-charge row: surface {d2 B = 0}
    nsB = int_nullspace(cx.d2)
    S = surface_columns(cx, 'B', nsB)
    chk = (cx.d2.toarray().astype(np.int64) @ S[cx.oF:cx.oF + cx.nF, :])
    assert not chk.any()
    Gm = constraint_gram(cx, blocks, S, cx.oF, cx.nF, cx.d2.toarray().astype(np.int64))
    kern = sps.Matrix(Gm.tolist()).nullspace()
    gbc_i = NAMES.index('gbc')
    ok = (len(kern) == 9) and all(k[gbc_i] == 0 for k in kern)
    rec(ok, f"F2 L={L}: invariance of the zero-charge magnetic surface {{d2 B = 0}} imposes exactly one coefficient condition, g_bc = 0 (exact nullspace dimension {len(kern)}, every solution has g_bc = 0)")
    z1 = (cx.d0.T @ cx.C.T).nnz == 0
    z2 = (cx.C.T @ cx.d2.T).nnz == 0
    rec(z1 and z2 and (cx.d0.T @ cx.d0).nnz > 0 and (cx.d2 @ cx.d2.T).nnz > 0,
        f"F3 L={L}: d0^T C^T = 0, C^T d2^T = 0 (exact) while d0^T d0 and d2 d2^T are nonzero; so d/dt(d0^T E) = gev (d0^T d0) phi + u d0^T E and d/dt(d2 B) = v d2 B + gbc (d2 d2^T) psi exactly; charged rows (rho != 0) add u = 0 and v = 0")


# ----------------------------------------------------------------------------------------
# STEP G. consequences: payload inertness iff row, within the bounded class; second speed
# ----------------------------------------------------------------------------------------
def step_G():
    # logical consequence checked exhaustively on the rule over a larger integer grid for each pair
    ok_v = True; ok_c = True
    vals = [Fr(x, d) for x in range(-4, 5) for d in (1, 2, 3)]
    for a2 in vals:
        for a1 in vals:
            base = {k: Fr(0) for k in NAMES}
            base['gev'] = a2; base['gve'] = a1
            if bounded_by_rule(base) and a2 == 0 and a1 != 0:
                ok_v = False
            if bounded_by_rule(base) and a2 == 0 and a1 == 0:
                pass
            base = {k: Fr(0) for k in NAMES}
            base['gbc'] = a2; base['gcb'] = a1
            if bounded_by_rule(base) and a2 == 0 and a1 != 0:
                ok_c = False
    rec(ok_v and ok_c, "G1 on a rational test grid: within the bounded rule, g_ev = 0 forces g_ve = 0 and g_bc = 0 forces g_cb = 0 (a one-sided coupling is a nilpotent block, hence unbounded)")
    # electric row only: the cube pair survives, giving a second independent speed
    cx = Complex(3)
    bl = cx.generator_blocks()
    par = dict(w=0, u=0, v=0, wc=0, gve=0, gev=0, q=1.0, r=-1.0, gbc=3.0, gcb=-1.0)
    G = sum(par[n] * bl[n].toarray().astype(float) for n in NAMES)
    ev = np.linalg.eigvals(G)
    freqs = np.sort(np.unique(np.round(np.abs(ev.imag), 9)))
    lamC = np.linalg.eigvalsh((cx.C.T @ cx.C).toarray().astype(float))
    lamD = np.linalg.eigvalsh((cx.d2 @ cx.d2.T).toarray().astype(float))
    maxwell = set(np.round(np.sqrt(np.unique(np.round(lamC[lamC > 1e-9], 9))), 9))
    cubef = set(np.round(np.sqrt(3.0) * np.sqrt(np.unique(np.round(lamD[lamD > 1e-9], 9))), 9))
    present = set(freqs[freqs > 1e-9])
    ok = ev.real.max() < 1e-9 and maxwell <= present and cubef <= present and len(cubef - maxwell) > 0
    rec(ok, "G2 L=3: with the electric row only (g_ev=0=g_ve) and (g_bc,g_cb)=(3,-1) the bounded flow carries the Maxwell frequencies sqrt(spec C^T C) AND an independent family sqrt(3)*sqrt(spec d2 d2^T): a second speed from the cube payload, absent iff the magnetic row (equivalently g_cb=0) is imposed")
    # with both rows, frequencies are exactly the Maxwell ones scaled by c = sqrt(-q r)
    par = dict(w=0, u=0, v=0, wc=0, gve=0, gev=0, q=4.0, r=-1.0, gbc=0, gcb=0)
    G = sum(par[n] * bl[n].toarray().astype(float) for n in NAMES)
    ev = np.linalg.eigvals(G)
    f = set(np.round(np.abs(ev.imag[np.abs(ev.imag) > 1e-9]), 8))
    expect = set(np.round(2.0 * np.sqrt(np.unique(np.round(lamC[lamC > 1e-9], 9))), 8))
    rec(ev.real.max() < 1e-9 and f == expect, "G3 L=3: with both rows the nonzero frequencies are exactly c sqrt(spec C^T C) with c = sqrt(-q r) = 2 (one speed per member, speed itself free)")


# ----------------------------------------------------------------------------------------
def main():
    step_A(2); step_A(3); step_A(4)
    step_B(4)
    step_B(3)
    for L in (2, 3, 4, 6):
        step_C(L)
    step_C5()
    step_D()
    step_D3_counts()
    step_E()
    step_F(3)
    step_G()
    npass = sum(RESULTS); nfail = len(RESULTS) - npass
    print(f"TOTAL: PASS={npass} FAIL={nfail}")
    if nfail == 0:
        print("HIT: scoped exact theorem (strengthens the known review correction that the {-1,0,1}-grid count 'exactly 2, one speed' is a grid artifact, from a count to a proof): in the supplied 10-coefficient covariant nearest-neighbour vertex/edge/face/cube flow class on cubic tori, every orbit is bounded for all t iff w=u=v=wc=0 and each pair (gve,gev), (q,r), (gbc,gcb) is (0,0) or has negative product, equivalently a positive diagonal invariant exists; the speed is free; and, given boundedness, the electric (magnetic) Gauss row is equivalent to the vertex (cube) payload being frozen and decoupled")
    print(f"(elapsed {time.time() - T0:.1f} s)")
    print("SUMMARY: exact grid-free classification of bounded orbits in the supplied 10-coefficient covariant nearest-neighbour vertex/edge/face/cube flow class (necessity from explicit exact eigen/Jordan subspaces, sufficiency from an exact positive diagonal invariant), cross-checked against the full 3^10 grid at L=2, showing speed is free and that, given boundedness, the magnetic Gauss row is equivalent to a frozen, decoupled cube payload; derivation of boundedness or of the class from the four axioms is not attempted.")
    sys.exit(0 if nfail == 0 else 1)


if __name__ == '__main__':
    main()
