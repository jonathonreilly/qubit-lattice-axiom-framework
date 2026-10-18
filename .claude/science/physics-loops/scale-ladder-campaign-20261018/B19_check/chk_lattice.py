#!/usr/bin/env python3
"""B19 check, lattice (fresh code; scipy sparse operators; exact parts via sympy DomainMatrix over QQ).

Definitions taken from the source notes (docs 10-18 note / B16 FINDINGS), re-implemented:
  G_m[xi] = sum_b xi_b (phi_{x+e} - phi_x)(pi_x + pi_{x+e})/2          -> delta phi = D_xi phi
  G_A[xi] = sum_{y,i} xi_(y,i) sum_{j!=i} E_(y+i,j) F_ij(y)             -> delta A = M_xi A
  {pi^T X phi, pi^T Y phi} = -pi^T [X,Y] phi  (sign irrelevant to span questions)
L1  exact (L=3,4): scalar [D_xi,D_eta] has a nonzero entry between diagonal next-nearest sites (x, x+e_i+e_j), where every D_zeta
    vanishes -> not in span{D_zeta}; also rank test over QQ.
L2  exact (L=3,4): Maxwell [M_xi,M_eta] not in span{M_zeta} + Gauss (curl-projection + harmonic rows), rank over QQ.
L3  control: span test accepts M_zeta' + (pure Gauss) for a random zeta'.
L4  float: OPTIMAL-zeta defect on the smooth subspace (27 lowest Fourier modes): min_zeta ||([X_xi,X_eta] - X_zeta) Pi|| / ||[X_xi,X_eta] Pi||
    vs L, smooth xi, eta. Tests whether the O(a^2)/O(a) orders survive optimising zeta (B19 used one 'natural' zeta).
"""
from __future__ import annotations
import sys, time
from itertools import product
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import lsqr
import sympy as sp
from sympy.polys.matrices import DomainMatrix

RES = {"pass": 0, "fail": 0}
def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)

def idx_site(L, x): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
def idx_link(L, x, j): return 3 * idx_site(L, x) + j
def sh(x, j, s=1): y = list(x); y[j] += s; return tuple(y)

def D_scalar(L, xi):
    """xi: array (L^3*3,) bond values. returns sparse (L^3 x L^3)."""
    r, c, v = [], [], []
    for x in product(range(L), repeat=3):
        for j in range(3):
            w = xi[idx_link(L, x, j)]
            if w == 0: continue
            a, b = idx_site(L, x), idx_site(L, sh(x, j))
            for row in (a, b):
                r += [row, row]; c += [b, a]; v += [w / 2, -w / 2]
    return sps.csr_matrix((v, (r, c)), shape=(L ** 3, L ** 3), dtype=object if isinstance(w, sp.Rational) else float)

def Fplaq(L, y, i, j):
    return {idx_link(L, sh(y, i), j): 1, idx_link(L, y, j): -1, idx_link(L, sh(y, j), i): -1, idx_link(L, y, i): 1}

def M_maxwell(L, xi):
    r, c, v = [], [], []
    for y in product(range(L), repeat=3):
        for i in range(3):
            w = xi[idx_link(L, y, i)]
            if w == 0: continue
            for j in range(3):
                if j == i: continue
                row = idx_link(L, sh(y, i), j)
                for col, s in Fplaq(L, y, i, j).items():
                    r.append(row); c.append(col); v.append(w * s)
    n = 3 * L ** 3
    return sps.coo_matrix((v, (r, c)), shape=(n, n)).tocsr()

def to_int_dense(Msp):
    return np.array(Msp.toarray(), dtype=object)

def comm(X, Y): return X @ Y - Y @ X

def qq_rank(rows):
    M = DomainMatrix([[sp.QQ(int(a.numerator), int(a.denominator)) if hasattr(a, "numerator") else sp.QQ(int(a)) for a in row] for row in rows], (len(rows), len(rows[0])), sp.QQ)
    return M.rank()

def exact_part(L, seed):
    rng = np.random.default_rng(seed)
    nb = 3 * L ** 3
    xi = rng.integers(-3, 4, nb).astype(float); et = rng.integers(-3, 4, nb).astype(float)
    # ---- scalar, entries scaled by 4 are integers
    Dx, De = D_scalar(L, xi), D_scalar(L, et)
    C = (comm(Dx, De) * 4).toarray()
    assert np.allclose(C, np.round(C))
    C = np.round(C).astype(np.int64)
    diag_nnz = 0
    for x in product(range(L), repeat=3):
        for i in range(3):
            for j in range(i + 1, 3):
                for s in (1, -1):
                    y = sh(sh(x, i), j, s)
                    if C[idx_site(L, x), idx_site(L, y)] != 0: diag_nnz += 1
    # rank test: vec(C) in span{vec(4 D_b)} ?
    basis = []
    for b in range(nb):
        e = np.zeros(nb); e[b] = 1
        basis.append(np.round(D_scalar(L, e).toarray() * 4).astype(np.int64).ravel())
    B = np.array(basis).T
    keep = np.where((np.abs(B).sum(1) > 0) | (C.ravel() != 0))[0]
    Bk, tk = B[keep], C.ravel()[keep]
    rB = qq_rank(Bk.tolist()); rBt = qq_rank(np.column_stack([Bk, tk]).tolist())
    scal_not = rBt > rB
    # ---- Maxwell mod Gauss
    Mx, Me = M_maxwell(L, xi), M_maxwell(L, et)
    T = comm(Mx, Me)
    # projection rows: curl (plaquettes) and harmonic sums
    prow = []
    for y in product(range(L), repeat=3):
        for (i, j) in ((0, 1), (0, 2), (1, 2)):
            v = np.zeros(nb, dtype=np.int64)
            for col, s in Fplaq(L, y, i, j).items(): v[col] += s
            prow.append(v)
    for j in range(3):
        v = np.zeros(nb, dtype=np.int64); v[j::3] = 1; prow.append(v)
    Pm = sps.csr_matrix(np.array(prow))
    def proj_vec(X):  # rows of Pm @ X, flattened
        return np.asarray((Pm @ X).toarray(), dtype=np.int64).ravel()
    t = proj_vec(T)
    Bm = []
    for b in range(nb):
        e = np.zeros(nb); e[b] = 1
        Bm.append(proj_vec(M_maxwell(L, e)))
    Bm = np.array(Bm).T
    keep = np.where((np.abs(Bm).sum(1) > 0) | (t != 0))[0]
    rB2 = qq_rank(Bm[keep].tolist()); rBt2 = qq_rank(np.column_stack([Bm[keep], t[keep]]).tolist())
    max_not = rBt2 > rB2
    # control: M_zeta' + pure Gauss piece must be in span
    z = rng.integers(-3, 4, nb).astype(float)
    grad = sps.lil_matrix((nb, L ** 3))
    for x in product(range(L), repeat=3):
        for j in range(3):
            grad[idx_link(L, x, j), idx_site(L, sh(x, j))] += 1; grad[idx_link(L, x, j), idx_site(L, x)] -= 1
    Yr = sps.csr_matrix(rng.integers(-2, 3, (L ** 3, nb)).astype(float))
    ctrl = M_maxwell(L, z) + grad.tocsr() @ Yr
    tc = proj_vec(ctrl)
    rc = qq_rank(np.column_stack([Bm[keep], tc[keep]]).tolist())
    ctrl_ok = rc == rB2
    return diag_nnz, scal_not, (rB, rBt), max_not, (rB2, rBt2), ctrl_ok

# ---------------------------------------------------------------- optimal-zeta smooth-subspace defect
def smooth_bond(L, seed):
    rng = np.random.default_rng(seed)
    out = np.zeros(3 * L ** 3)
    grid = np.array(list(product(range(L), repeat=3)), float) / L
    for j in range(3):
        pos = grid.copy(); pos[:, j] += 0.5 / L
        f = np.zeros(L ** 3)
        for _ in range(3):
            k = rng.integers(-1, 2, 3)
            if not k.any(): k[0] = 1
            f += rng.uniform(0.5, 1) * np.cos(2 * np.pi * pos @ k + rng.uniform(0, 6.3))
        out[j::3] = f
    return out

def low_modes(L, nsites_fields):
    """columns: real/imag parts of the 27 lowest plane waves on sites (nsites_fields = 1) or on links (3, per component)."""
    grid = np.array(list(product(range(L), repeat=3)), float)
    cols = []
    for n in product((-1, 0, 1), repeat=3):
        ph = np.exp(2j * np.pi * grid @ np.array(n) / L)
        for comp in range(nsites_fields):
            v = np.zeros(nsites_fields * L ** 3, complex)
            v[comp::nsites_fields] = ph
            cols.append(v)
    return np.array(cols).T

def opt_defect(L, kind):
    xi, et = smooth_bond(L, 11), smooth_bond(L, 23)
    nb = 3 * L ** 3
    if kind == "scalar":
        op = lambda z: D_scalar(L, z); Pi = low_modes(L, 1)
    else:
        op = lambda z: M_maxwell(L, z); Pi = low_modes(L, 3)
    Cx = comm(op(xi), op(et)) @ Pi           # target
    if kind == "maxwell":
        # mod Gauss: project rows onto transverse subspace via FFT-free dense projector (small L only)
        n = nb
        G = sps.lil_matrix((n, L ** 3))
        for x in product(range(L), repeat=3):
            for j in range(3):
                G[idx_link(L, x, j), idx_site(L, sh(x, j))] += 1; G[idx_link(L, x, j), idx_site(L, x)] -= 1
        G = G.toarray()
        Pt = np.eye(n) - G @ np.linalg.pinv(G)   # projector onto ker(G^T) = ker(div)
        proj = lambda Y: Pt @ Y
    else:
        proj = lambda Y: Y
    tgt = proj(np.asarray(Cx))
    # design matrix columns: proj(X_b Pi) for each bond b
    cols = []
    for b in range(nb):
        e = np.zeros(nb); e[b] = 1
        cols.append(proj(np.asarray(op(e) @ Pi)).ravel())
    Amat = np.array(cols).T
    Ar = np.vstack([Amat.real, Amat.imag]); tr = np.concatenate([tgt.ravel().real, tgt.ravel().imag])
    z, *_ = np.linalg.lstsq(Ar, tr, rcond=None)
    res = np.linalg.norm(Ar @ z - tr) / np.linalg.norm(tr)
    return res

if __name__ == "__main__":
    for L in (3, 4):
        for seed in (1, 2):
            t0 = time.time()
            dn, sn, rs, mn, rm, cok = exact_part(L, 100 * L + seed)
            print(f"   L={L} seed={seed} ({time.time()-t0:.0f}s): scalar diagonal-NNN nonzeros={dn}, rank(B)={rs[0]} rank(B|t)={rs[1]}; "
                  f"Maxwell mod Gauss rank(B)={rm[0]} rank(B|t)={rm[1]}; control in span={cok}", flush=True)
            check(f"L1[L={L},s={seed}]", dn > 0 and sn, "scalar {G_m,G_m} not in span{G_m[zeta]} (exact: NNN-diagonal entries + QQ rank)")
            check(f"L2[L={L},s={seed}]", mn and cok, "Maxwell {G_A,G_A} not in span{G_A[zeta]} mod Gauss (exact QQ rank); control G_A[zeta']+Gauss accepted")
    if "--opt" in sys.argv:
        rows = []
        for L in (4, 6, 8, 10):
            t0 = time.time()
            rs, rm = opt_defect(L, "scalar"), opt_defect(L, "maxwell")
            rows.append((L, rs, rm))
            print(f"   L={L} ({time.time()-t0:.0f}s): optimal-zeta smooth-subspace defect: scalar {rs:.3e}, Maxwell(mod Gauss) {rm:.3e}", flush=True)
        Ls = np.array([r[0] for r in rows], float)
        ss = np.polyfit(np.log(Ls[1:]), np.log([r[1] for r in rows][1:]), 1)[0]
        sm = np.polyfit(np.log(Ls[1:]), np.log([r[2] for r in rows][1:]), 1)[0]
        print(f"   slopes (L=6..10): scalar {ss:.2f}, Maxwell {sm:.2f}  [reported, not gated: pre-asymptotic small L]")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
