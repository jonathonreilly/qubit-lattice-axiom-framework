AUDIT_INPUT_PATHS = ('docs/THE_D4_FAR_WALL_CAYLEY_TERM_ON_A_TWO_BY_FOUR_PATCH_KEEPS_A_UNIQUE_GAPPED_STATE_AT_G_0_25_0_35_0_5_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-far-wall-2x4: third patch size for the D4 far-wall Cayley term on the (n1, n2) square wall slice.
 Same model as d4-far-wall-2plus1 (4-mode register, Dirac hop i psi^+ Gamma_k psi, Cayley term g, Z4 twist); only Lx x Ly = 2 x 4.
 A [T] structure; B [T] magnetic translations (w = -i on a wrap) and the momentum basis; C [F] 2x2 momentum code = parent code;
 D [F] 2x3 live re-check of the parent gaps; E [R] 2x4 values from the Mac mini (embedded literals, provenance below).
 Supplied: the 4-mode register, Cayley form and weight, naive hop t = 1, Z4 twist, patch shape, g (scanned, nothing fitted)."""
AUDIT_TIMEOUT_SEC = 120
import time
T0 = time.time()
import os, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
pc = lambda a: np.bitwise_count(a).astype(np.int64)
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
g5 = gm[0] @ gm[1] @ gm[2] @ gm[3]; g5 = g5 / np.sqrt((g5 @ g5)[0, 0]); gv = lambda v: np.einsum('m,mab->ab', v, gm)
ut = np.array([1, 1, 0, 0]) / np.sqrt(2)
NV = [np.array([0, 0, 1, 1]) / np.sqrt(2), np.array([0, 0, 1, -1]) / np.sqrt(2), np.array([1, -1, 0, 0]) / np.sqrt(2)]
GAM = [1j * gv(ut) @ gv(n) for n in NV]
def frame():
    # U: columns (c,m) -> c*2+m ; Gamma1 = sz x 1, Gamma2 = sx x 1, g5 = 1 x tz
    w, V = np.linalg.eigh(GAM[0]); Pp = V[:, w > 0]          # Gamma1 = +1 space, commutes with g5
    w5, V5 = np.linalg.eigh(Pp.conj().T @ g5 @ Pp); e = Pp @ V5  # order g5 = -1, +1
    f = GAM[1] @ e; U = np.column_stack([e[:, 0], e[:, 1], f[:, 0], f[:, 1]]); return U, w5
U, W5 = frame()
GP = [U.conj().T @ G @ U for G in GAM]
def species_gamma(k, m): return GP[k][np.ix_([m, 2 + m], [m, 2 + m])]
class Species:
    def __init__(s, dims, twist, m):
        # dims = (Lx, Ly); twist[k] = 2-vector of phases (c = 0, 1) on wraps in direction k; m = species (A=0, B=1)
        Lx, Ly = dims; Ns = Lx * Ly; s.Ns = Ns; Nm = 2 * Ns; s.Nm = Nm
        site = lambda x, y: (x % Lx) * Ly + (y % Ly); h = np.zeros((Nm, Nm), complex)
        for x in range(Lx):
            for y in range(Ly):
                for k, (dx, dy, L) in enumerate([(1, 0, Lx), (0, 1, Ly)]):
                    if L == 1: continue
                    a, b = site(x, y), site(x + dx, y + dy); wrap = (x + dx >= Lx) if k == 0 else (y + dy >= Ly)
                    G = species_gamma(k, m); T = np.diag(twist[k]) if wrap else np.eye(2); M = 1j * G @ T
                    for c in range(2):
                        for c2 in range(2):
                            h[2 * a + c, 2 * b + c2] += M[c, c2]; h[2 * b + c2, 2 * a + c] += np.conj(M[c, c2])
        s.hsp = h; s.cfg = {}
        allc = np.arange(1 << Nm, dtype=np.int64); cnt = pc(allc)
        for n in range(Nm + 1): s.cfg[n] = allc[cnt == n]
        s.H = {}; s.P = {}; s.al = {}
        for n in range(Nm + 1):
            S = s.cfg[n]; D = len(S); r, c, v = [], [], []
            for p, q in zip(*np.nonzero(np.abs(h) > 1e-14)):
                if p == q:
                    o = np.nonzero((S >> p) & 1)[0]; r.append(o); c.append(o); v.append(np.full(len(o), h[p, p])); continue
                ok = ((S >> q) & 1 == 1) & ((S >> p) & 1 == 0); st = S[ok]; lo, hi = min(p, q), max(p, q)
                sg = 1 - 2 * (pc(st & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))) & 1)
                r.append(np.searchsorted(S, st ^ (1 << p) ^ (1 << q))); c.append(np.nonzero(ok)[0]); v.append(h[p, q] * sg)
            s.H[n] = sp.csr_matrix((np.concatenate(v) if v else [], (np.concatenate(r) if r else [], np.concatenate(c) if c else [])), shape=(D, D))
            occ = np.stack([((S >> (2 * x)) & 1) + ((S >> (2 * x + 1)) & 1) for x in range(Ns)], 1); s.al[n] = 1 - occ
            if n >= 2:
                T_ = s.cfg[n - 2]; mats = []
                for x in range(Ns):
                    ok = ((S >> (2 * x)) & 3) == 3; st = S[ok]
                    mats.append(sp.csr_matrix((-np.ones(len(st)), (np.searchsorted(T_, st ^ (3 << (2 * x))), np.nonzero(ok)[0])), shape=(len(T_), D)))
                s.P[n] = mats
class Sector:
    def __init__(s, A, B, Q, par, g, model):
        s.A, s.B, s.g, s.model = A, B, g, model; s.blocks = []; off = 0
        for nA in range(A.Nm + 1):
            nB = nA - Q
            if nA % 2 != par or nB < 0 or nB > B.Nm: continue
            sh = (len(A.cfg[nA]), len(B.cfg[nB])); s.blocks.append((nA, nB, off, sh)); off += sh[0] * sh[1]
        s.dim = off; s.idx = {(b[0], b[1]): i for i, b in enumerate(s.blocks)}; s.D = []
        for nA, nB, o, sh in s.blocks:
            if model == 'Cay':
                aa, bb = A.al[nA], B.al[nB]
                Dg = (np.sum(1 - 2 * aa ** 2, 1)[:, None] + np.sum(1 - 2 * bb ** 2, 1)[None, :] - 4.0 * aa @ bb.T) * g
            else: Dg = np.zeros(sh)
            s.D.append(Dg)
    def mv(s, v):
        v = np.asarray(v).ravel(); out = np.zeros(s.dim, complex); A, B, g = s.A, s.B, s.g
        V = [v[o:o + sh[0] * sh[1]].reshape(sh) for (_, _, o, sh) in s.blocks]
        W = [out[o:o + sh[0] * sh[1]].reshape(sh) for (_, _, o, sh) in s.blocks]
        for i, (nA, nB, o, sh) in enumerate(s.blocks):
            W[i] += A.H[nA] @ V[i] + (B.H[nB] @ V[i].T).T + s.D[i] * V[i]
            j = s.idx.get((nA - 2, nB - 2))
            if j is not None and g != 0:
                for x in range(A.Ns):
                    PA, PB = A.P[nA][x], B.P[nB][x]
                    W[j] += 8 * g * (PA @ (PB @ V[i].T).T)
                    W[i] += 8 * g * (PA.T @ (PB.T @ V[j].T).T)
        return out
    def low(s, k):
        if s.dim <= 600:
            M = np.column_stack([s.mv(e) for e in np.eye(s.dim)]); return np.linalg.eigvalsh(M)[:k]
        op = sla.LinearOperator((s.dim, s.dim), matvec=s.mv, dtype=complex)
        return np.sort(sla.eigsh(op, k=k, which='SA', tol=1e-8, ncv=20 if k == 1 else 32, v0=np.random.default_rng(7).standard_normal(s.dim) + 0j)[0])
def gap(dims, tw, g, model, Qs, twB=None):
    A = Species(dims, tw, 0); B = Species(dims, twB if twB is not None else tw, 1)
    lv = {}
    for Q in Qs:
        for par in (0, 1):
            sc = Sector(A, B, Q, par, g, model)
            if sc.dim == 0: continue
            lv[(Q, par)] = sc.low(2)
    E0 = min(l[0] for l in lv.values()); key0 = min(lv, key=lambda q: lv[q][0])
    rest = sorted([l[0] for q, l in lv.items() if q != key0] + [lv[key0][1]])
    return rest[0] - E0, E0, key0, lv, A, B
# Momentum-sector layer on top of the unchanged parent core.py (d4-far-wall-2plus1).
# Magnetic translations T_x, T_y act as T_A x T_B; each species Fock sector is rotated to a joint T eigenbasis.
import numpy as np, scipy.sparse as sp, resource, sys
from scipy.linalg.blas import zaxpy, zscal

def peak_mb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 2**20 if sys.platform == 'darwin' else r / 2**10

def trans_op(Sp, dims, k, omega, n):
    """Sparse T_k on the n-particle Fock sector of species Sp: c_r^+ -> w_r c_{r+e_k}^+ (w = omega on a wrap)."""
    Lx, Ly = dims; Nm = Sp.Nm; S = Sp.cfg[n]
    sig = np.zeros(Nm, np.int64); ph = np.ones(Nm, complex)
    for x in range(Lx):
        for y in range(Ly):
            for c in range(2):
                if k == 0: x2, y2, wr = (x + 1) % Lx, y, x + 1 >= Lx
                else: x2, y2, wr = x, (y + 1) % Ly, y + 1 >= Ly
                p = 2 * (x * Ly + y) + c; sig[p] = 2 * (x2 * Ly + y2) + c
                if wr and (Lx if k == 0 else Ly) > 1: ph[p] = omega
    new = np.zeros(len(S), np.int64); amp = np.ones(len(S), complex); par = np.zeros(len(S), np.int64)
    for p in range(Nm):
        o = (S >> p) & 1; new |= o << sig[p]; amp *= np.where(o == 1, ph[p], 1)
        for q in range(p + 1, Nm):
            if sig[p] > sig[q]: par ^= o & ((S >> q) & 1)
    amp *= 1 - 2 * par
    return sp.csr_matrix((amp, (np.searchsorted(S, new), np.arange(len(S)))), shape=(len(S), len(S))), np.searchsorted(S, new)

class MomSpecies:
    def __init__(s, Sp, dims, omega):
        s.Sp = Sp; s.dims = dims; Lx, Ly = dims; s.Ns = Sp.Ns; s.U = {}; s.lab = {}; s.cols = {}; s.M = (4 * Lx, 4 * Ly)
        s.T = {}
        for n in range(Sp.Nm + 1):
            D = len(Sp.cfg[n]); Tx, px = trans_op(Sp, dims, 0, omega, n); Ty, py = trans_op(Sp, dims, 1, omega, n)
            s.T[n] = (Tx, Ty)
            orb = np.arange(D)
            for _ in range(Lx * Ly):
                orb = np.minimum(orb, np.minimum(orb[px], orb[py]))
            # iterate to fixed point of orbit minima
            while True:
                o2 = np.minimum(orb, np.minimum(orb[px], orb[py]))
                if np.array_equal(o2, orb): break
                orb = o2
            rows, cols, vals, labs = [], [], [], []; col = 0
            Txd, Tyd = Tx.tocsc(), Ty.tocsc()
            order = np.argsort(orb, kind='stable'); bounds = np.flatnonzero(np.diff(orb[order])) + 1
            for members in np.split(order, bounds):
                d = len(members); mx = Txd[members][:, members].toarray(); my = Tyd[members][:, members].toarray()
                w, V = np.linalg.eig(mx + (np.sqrt(2) + 0.3j) * my)
                V, _ = np.linalg.qr(V)  # normal matrix, distinct eigenvalues -> orthonormal; qr fixes rounding
                lx = np.diag(V.conj().T @ mx @ V); ly = np.diag(V.conj().T @ my @ V)
                ax = np.round(np.angle(lx) / (2 * np.pi / s.M[0])).astype(int) % s.M[0]
                ay = np.round(np.angle(ly) / (2 * np.pi / s.M[1])).astype(int) % s.M[1]
                for j in range(d):
                    rows.append(members); cols.append(np.full(d, col)); vals.append(V[:, j]); labs.append((ax[j], ay[j])); col += 1
            U = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(D, D))
            labs = np.array(labs).reshape(-1, 2); key = labs[:, 0] * s.M[1] + labs[:, 1]
            perm = np.argsort(key, kind='stable'); U = U[:, perm].tocsc(); key = key[perm]
            s.U[n] = U; s.lab[n] = key; s.cols[n] = {int(k): np.flatnonzero(key == k) for k in np.unique(key)}
    def rot(s, M, n_out, n_in, tol=1e-11):
        R = (s.U[n_out].conj().T @ M @ s.U[n_in]).tocsr(); R.data[np.abs(R.data) < tol] = 0; R.eliminate_zeros(); return R
    def blocks(s, R, n_out, n_in):
        """Split a rotated operator into label blocks; assert it is momentum-monomial (one row label per column label)."""
        out = {}
        for kc, cc in s.cols[n_in].items():
            sub = R[:, cc]
            for kr, rr in s.cols[n_out].items():
                b = sub[rr]
                if b.nnz: out.setdefault(kc, []).append((kr, b.tocsr()))
        for kc in out:
            if len(out[kc]) > 1:
                mx = sorted(max(abs(b.data)) for _, b in out[kc])
                if mx[-2] > 1e-9: raise RuntimeError('not momentum-monomial')
                out[kc] = [max(out[kc], key=lambda t: abs(t[1].data).max())]
        return {kc: v[0] for kc, v in out.items()}

def site_xy(i, dims): return divmod(i, dims[1])

def fourier_family(MA, MB, ops_A, ops_B, nA_out, nA_in, nB_out, nB_in, dims):
    """Return list over q of (blocksA, blocksB) with sum_x OA_x x OB_x = (1/N) sum_q OtA(q) x OtB(q).
    Tries plain and half-shifted grids per direction; keeps the choice that is momentum-monomial on both species."""
    Lx, Ly = dims; N = Lx * Ly
    for shx in (0.0, 0.5):
        for shy in (0.0, 0.5):
            try:
                res = []
                for mx in range(Lx):
                    for my in range(Ly):
                        qx = 2 * np.pi * (mx + shx) / Lx; qy = 2 * np.pi * (my + shy) / Ly
                        ph = [np.exp(1j * (qx * site_xy(i, dims)[0] + qy * site_xy(i, dims)[1])) for i in range(N)]
                        OA = sum(ph[i] * ops_A[i] for i in range(N)); OB = sum(np.conj(ph[i]) * ops_B[i] for i in range(N))
                        res.append((MA.blocks(MA.rot(sp.csr_matrix(OA), nA_out, nA_in), nA_out, nA_in),
                                    MB.blocks(MB.rot(sp.csr_matrix(OB), nB_out, nB_in), nB_out, nB_in)))
                return res
            except RuntimeError:
                continue
    raise RuntimeError('no monomial Fourier grid')

class MomModel:
    def __init__(s, dims, tw, omega):
        s.dims = dims; s.N = dims[0] * dims[1]
        s.A = Species(dims, tw, 0); s.B = Species(dims, tw, 1)
        s.MA = MomSpecies(s.A, dims, omega); s.MB = MomSpecies(s.B, dims, omega)
        s.cache = {}
    def kin(s, MS, n):
        Sp = MS.Sp; key = ('kin', id(MS), n)
        if key not in s.cache:
            dg = sp.diags(np.sum(1 - 2 * Sp.al[n].astype(float) ** 2, 1).astype(complex))
            s.cache[key] = (MS.blocks(MS.rot(Sp.H[n], n, n), n, n), MS.blocks(MS.rot(dg.tocsr(), n, n), n, n))
        return s.cache[key]
    def alpha(s, nA, nB):
        key = ('al', nA, nB)
        if key not in s.cache:
            oa = [sp.diags(s.A.al[nA][:, x].astype(complex)) for x in range(s.N)]
            ob = [sp.diags(s.B.al[nB][:, x].astype(complex)) for x in range(s.N)]
            s.cache[key] = fourier_family(s.MA, s.MB, oa, ob, nA, nA, nB, nB, s.dims)
        return s.cache[key]
    def pair(s, nA, nB):
        key = ('P', nA, nB)
        if key not in s.cache:
            s.cache[key] = fourier_family(s.MA, s.MB, [m.astype(complex) for m in s.A.P[nA]], [m.astype(complex) for m in s.B.P[nB]],
                                          nA - 2, nA, nB - 2, nB, s.dims)
        return s.cache[key]

class MomSector:
    def __init__(s, mod, Q, par, K, g):
        s.mod, s.g = mod, g; A, B, MA, MB = mod.A, mod.B, mod.MA, mod.MB; Mx, My = MA.M
        s.blocks = []; off = 0
        for nA in range(A.Nm + 1):
            nB = nA - Q
            if nA % 2 != par or nB < 0 or nB > B.Nm: continue
            for la, ca in MA.cols[nA].items():
                lb = ((K[0] - la // My) % Mx) * My + (K[1] - la % My) % My
                if lb in MB.cols[nB]:
                    sh = (len(ca), len(MB.cols[nB][lb])); s.blocks.append((nA, nB, la, lb, off, sh)); off += sh[0] * sh[1]
        s.dim = off; s.idx = {b[:4]: i for i, b in enumerate(s.blocks)}
        s.terms = []  # (i_out, i_in, X, Y, coef, conj_mode): out_i += coef * X @ V_in @ Y^T
        for i, (nA, nB, la, lb, o, sh) in enumerate(s.blocks):
            kA, dA = mod.kin(MA, nA); kB, dB = mod.kin(MB, nB)
            XA = (kA[la][1] + g * dA[la][1]) if la in kA else g * dA[la][1]
            XB = (kB[lb][1] + g * dB[lb][1]) if lb in kB else g * dB[lb][1]
            s.terms.append(('L', i, i, XA.tocsr(), None, 1.0)); s.terms.append(('R', i, i, None, XB.tocsr(), 1.0))
            if g != 0:
                for bA, bB in mod.alpha(nA, nB):
                    if la in bA and lb in bB:
                        (ra, XA2), (rb, XB2) = bA[la], bB[lb]; j = s.idx.get((nA, nB, ra, rb))
                        if j is not None: s.terms.append(('LR', j, i, XA2, XB2, -4 * g / mod.N))
                if nA >= 2 and nB >= 2:
                    for bA, bB in mod.pair(nA, nB):
                        if la in bA and lb in bB:
                            (ra, XA2), (rb, XB2) = bA[la], bB[lb]; j = s.idx.get((nA - 2, nB - 2, ra, rb))
                            if j is not None:
                                c = 8 * g / mod.N
                                s.terms.append(('LR', j, i, XA2, XB2, c))
                                s.terms.append(('LR', i, j, XA2.conj().T.tocsr(), XB2.conj().T.tocsr(), c))
    def view(s, v, i):
        o, sh = s.blocks[i][4], s.blocks[i][5]; return v[o:o + sh[0] * sh[1]].reshape(sh)
    def mv(s, v, out=None):
        if out is None: out = np.zeros(s.dim, complex)
        else: out[:] = 0
        for kind, j, i, X, Y, c in s.terms:
            Vi = s.view(v, i); Wj = s.view(out, j)
            if kind == 'L': Wj += X @ Vi
            elif kind == 'R': Wj += (Y @ Vi.T).T
            else: Wj += c * (Y @ (X @ Vi).T).T
        return out

def lanczos_low(op, dim, seed, tol=1e-10, maxit=400, defl=None, sigma=200.0, rss_cap_mb=6000, log=None):
    """Plain three-term Lanczos (no reorthogonalisation), lowest Ritz value. defl: vector psi0 to push up by sigma."""
    rng = np.random.default_rng(seed)
    v = np.empty(dim, complex); v.real = rng.standard_normal(dim); v.imag = rng.standard_normal(dim)
    if defl is not None: zaxpy(defl, v, a=-np.vdot(defl, v))
    zscal(1 / np.linalg.norm(v), v)
    vp = np.zeros(dim, complex); w = np.empty(dim, complex); al, be = [], []; prev = None; e = None
    for it in range(maxit):
        op(v, w)
        if defl is not None: zaxpy(defl, w, a=sigma * np.vdot(defl, v))
        a = np.vdot(v, w).real; al.append(a); zaxpy(v, w, a=-a)
        if it > 0: zaxpy(vp, w, a=-be[-1])
        b = np.linalg.norm(w)
        if (it + 1) % 5 == 0 or b < 1e-12:
            from scipy.linalg import eigh_tridiagonal
            e = eigh_tridiagonal(np.array(al), np.array(be), select='i', select_range=(0, 0))[0][0]
            if log: log(it + 1, e, peak_mb())
            if peak_mb() > rss_cap_mb: raise MemoryError('RSS cap')
            if prev is not None and abs(e - prev) < tol: return e, al, be, it + 1
            prev = e
        if b < 1e-12: return e, al, be, it + 1
        be.append(b); vp, v, w = v, w, vp; zscal(1 / b, v)
    return e, al, be, maxit

def lanczos_vector(op, dim, seed, al, be, defl=None, sigma=200.0):
    """Second pass: rebuild the lowest Ritz vector from the stored coefficients (same seed)."""
    from scipy.linalg import eigh_tridiagonal
    n = len(al); y = eigh_tridiagonal(np.array(al), np.array(be[:n - 1]), select='i', select_range=(0, 0))[1][:, 0]
    rng = np.random.default_rng(seed)
    v = np.empty(dim, complex); v.real = rng.standard_normal(dim); v.imag = rng.standard_normal(dim)
    if defl is not None: zaxpy(defl, v, a=-np.vdot(defl, v))
    zscal(1 / np.linalg.norm(v), v)
    psi = np.zeros(dim, complex); vp = np.zeros(dim, complex); w = np.empty(dim, complex)
    for it in range(n):
        zaxpy(v, psi, a=y[it])
        if it == n - 1: break
        op(v, w)
        if defl is not None: zaxpy(defl, w, a=sigma * np.vdot(defl, v))
        zaxpy(v, w, a=-al[it])
        if it > 0: zaxpy(vp, w, a=-be[it - 1])
        vp, v, w = v, w, vp; zscal(1 / be[it], v)
    del vp, w, v
    zscal(1 / np.linalg.norm(psi), psi); return psi
# [R] Mac mini 2x4 values, scratch/drive24.py + scratch/mom.py (same code as sections B-D), host Jonathons-Mac-mini.local,
# 2026-10-26 16:43 -> 2026-10-27 02:34 EDT, wall 35,451 s (9.85 h), one worker, 1 thread, nice 10, peak RSS 3,079 MB (cap 6,000).
# Rows: (g, Q, nA mod 2, Kx, Ky, sector dim, lowest level) from plain Lanczos, tol 1e-8 on the Ritz value.
MINI_E0 = [
    (0.25, 0, 0, 0, 0, 37569958, -33.7511299684),
    (0.25, 0, 0, 0, 4, 37566720, -31.9891013444),
    (0.25, 0, 0, 0, 8, 37569952, -32.2656456093),
    (0.25, 0, 0, 0, 12, 37566720, -31.9891013444),
    (0.25, 0, 0, 4, 0, 37566720, -32.5032336876),
    (0.25, 0, 0, 4, 4, 37569920, -31.9185216041),
    (0.25, 0, 0, 4, 8, 37566720, -33.0510180364),
    (0.25, 0, 0, 4, 12, 37569920, -31.9185216041),
    (0.25, 0, 1, 2, 2, 37566720, -31.6362632991),
    (0.25, 0, 1, 2, 6, 37566720, -31.6362632996),
    (0.25, 0, 1, 2, 10, 37566720, -31.6362632989),
    (0.25, 0, 1, 2, 14, 37566720, -31.6362632996),
    (0.25, 0, 1, 6, 2, 37566720, -31.6362632993),
    (0.25, 0, 1, 6, 6, 37566720, -31.6362632996),
    (0.25, 0, 1, 6, 10, 37566720, -31.6362632997),
    (0.25, 0, 1, 6, 14, 37566720, -31.6362632994),
    (0.25, 1, 0, 1, 1, 35357670, -32.0634574428),
    (0.25, 1, 0, 1, 5, 35357670, -31.7346200777),
    (0.25, 1, 0, 1, 9, 35357670, -32.0634574425),
    (0.25, 1, 0, 1, 13, 35357670, -31.7346200778),
    (0.25, 1, 0, 5, 1, 35357670, -32.0634574428),
    (0.25, 1, 0, 5, 5, 35357670, -31.7346200777),
    (0.25, 1, 0, 5, 9, 35357670, -32.0634574429),
    (0.25, 1, 0, 5, 13, 35357670, -31.7346200774),
    (0.25, 1, 1, 3, 3, 35357670, -31.7346200774),
    (0.25, 1, 1, 3, 7, 35357670, -32.0634574429),
    (0.25, 1, 1, 3, 11, 35357670, -31.7346200778),
    (0.25, 1, 1, 3, 15, 35357670, -32.0634574430),
    (0.25, 1, 1, 7, 3, 35357670, -31.7346200778),
    (0.25, 1, 1, 7, 7, 35357670, -32.0634574430),
    (0.25, 1, 1, 7, 11, 35357670, -31.7346200777),
    (0.25, 1, 1, 7, 15, 35357670, -32.0634574429),
    (0.35, 0, 0, 0, 0, 37569958, -42.7335201634),
    (0.35, 0, 0, 0, 4, 37566720, -37.8324562217),
    (0.35, 0, 0, 0, 8, 37569952, -37.9976481077),
    (0.35, 0, 0, 0, 12, 37566720, -37.8324562217),
    (0.35, 0, 0, 4, 0, 37566720, -39.0693665572),
    (0.35, 0, 0, 4, 4, 37569920, -39.3180502031),
    (0.35, 0, 0, 4, 8, 37566720, -39.8338011281),
    (0.35, 0, 0, 4, 12, 37569920, -39.3180502031),
    (0.35, 0, 1, 2, 2, 37566720, -38.5587678394),
    (0.35, 0, 1, 2, 6, 37566720, -38.5587678395),
    (0.35, 0, 1, 2, 10, 37566720, -38.5587678395),
    (0.35, 0, 1, 2, 14, 37566720, -38.5587678396),
    (0.35, 0, 1, 6, 2, 37566720, -38.5587678394),
    (0.35, 0, 1, 6, 6, 37566720, -38.5587678396),
    (0.35, 0, 1, 6, 10, 37566720, -38.5587678396),
    (0.35, 0, 1, 6, 14, 37566720, -38.5587678393),
    (0.35, 1, 0, 1, 1, 35357670, -39.2620664398),
    (0.35, 1, 0, 1, 5, 35357670, -39.2755363583),
    (0.35, 1, 0, 1, 9, 35357670, -39.2620664398),
    (0.35, 1, 0, 1, 13, 35357670, -39.2755363583),
    (0.35, 1, 0, 5, 1, 35357670, -39.2620664399),
    (0.35, 1, 0, 5, 5, 35357670, -39.2755363583),
    (0.35, 1, 0, 5, 9, 35357670, -39.2620664399),
    (0.35, 1, 0, 5, 13, 35357670, -39.2755363583),
    (0.35, 1, 1, 3, 3, 35357670, -39.2755363582),
    (0.35, 1, 1, 3, 7, 35357670, -39.2620664399),
    (0.35, 1, 1, 3, 11, 35357670, -39.2755363583),
    (0.35, 1, 1, 3, 15, 35357670, -39.2620664399),
    (0.35, 1, 1, 7, 3, 35357670, -39.2755363582),
    (0.35, 1, 1, 7, 7, 35357670, -39.2620664398),
    (0.35, 1, 1, 7, 11, 35357670, -39.2755363583),
    (0.35, 1, 1, 7, 15, 35357670, -39.2620664399),
    (0.5, 0, 0, 0, 0, 37569958, -58.3675729604),
    (0.5, 0, 0, 0, 4, 37566720, -50.4493113284),
    (0.5, 0, 0, 0, 8, 37569952, -51.0416900383),
    (0.5, 0, 0, 0, 12, 37566720, -50.4493113285),
    (0.5, 0, 0, 4, 0, 37566720, -51.5501848738),
    (0.5, 0, 0, 4, 4, 37569920, -51.9506719715),
    (0.5, 0, 0, 4, 8, 37566720, -52.4023680751),
    (0.5, 0, 0, 4, 12, 37569920, -51.9506719715),
    (0.5, 0, 1, 2, 2, 37566720, -51.4541130509),
    (0.5, 0, 1, 2, 6, 37566720, -51.4541130509),
    (0.5, 0, 1, 2, 10, 37566720, -51.4541130508),
    (0.5, 0, 1, 2, 14, 37566720, -51.4541130508),
    (0.5, 0, 1, 6, 2, 37566720, -51.4541130508),
    (0.5, 0, 1, 6, 6, 37566720, -51.4536685212),
    (0.5, 0, 1, 6, 10, 37566720, -51.4541130509),
    (0.5, 0, 1, 6, 14, 37566720, -51.4541130508),
    (0.5, 1, 0, 1, 1, 35357670, -52.5477732951),
    (0.5, 1, 0, 1, 5, 35357670, -52.7392879455),
    (0.5, 1, 0, 1, 9, 35357670, -52.5477732951),
    (0.5, 1, 0, 1, 13, 35357670, -52.7392879455),
    (0.5, 1, 0, 5, 1, 35357670, -52.5477732951),
    (0.5, 1, 0, 5, 5, 35357670, -52.7392879455),
    (0.5, 1, 0, 5, 9, 35357670, -52.5477732951),
    (0.5, 1, 0, 5, 13, 35357670, -52.7392879456),
    (0.5, 1, 1, 3, 3, 35357670, -52.7392879455),
    (0.5, 1, 1, 3, 7, 35357670, -52.5477732951),
    (0.5, 1, 1, 3, 11, 35357670, -52.7392879455),
    (0.5, 1, 1, 3, 15, 35357670, -52.5477732951),
    (0.5, 1, 1, 7, 3, 35357670, -52.7392879455),
    (0.5, 1, 1, 7, 7, 35357670, -52.5477732951),
    (0.5, 1, 1, 7, 11, 35357670, -52.7392879456),
    (0.5, 1, 1, 7, 15, 35357670, -52.5477732951),
]
# Deflated second level in the ground-state momentum sector: (g, Q, par, Kx, Ky, e0, e1, residual |H psi0 - e0 psi0|)
MINI_E1 = [
    (0.25, 0, 0, 0, 0, -33.7511299684, -32.8127902888, 2.5e-07),
    (0.35, 0, 0, 0, 0, -42.7335201634, -37.7862633732, 5.1e-07),
    (0.5, 0, 0, 0, 0, -58.3675729605, -49.8118788825, 4.9e-07),
]

# ------------------------------------------------------------------ checks
NP = [0]; NF = [0]
def chk(name, ok, info=''):
    (NP if ok else NF)[0] += 1; print(('PASS ' if ok else 'FAIL ') + name + ((' | ' + info) if info else ''))
TW = [np.array([1j, 1j])] * 2; OMEGA = -1j
PARENT = {0.25: (0.886, 0.290), 0.35: (2.557, 3.182), 0.5: (5.639, 5.599)}  # parent note, gap 2x2, gap 2x3
def free_gap(dims):
    ks = [[(2 * np.pi * m + np.pi / 2) / L for m in range(L)] for L in dims]
    return min(2 * np.sqrt(np.sin(a) ** 2 + np.sin(b) ** 2) for a in ks[0] for b in ks[1])
def mom_levels(mod, g, sectors, seed=7):
    Mx, My = mod.MA.M; lv = []
    for Q, par in sectors:
        for kx in range(Mx):
            for ky in range(My):
                s = MomSector(mod, Q, par, (kx, ky), g)
                if s.dim == 0: continue
                if s.dim <= 0:
                    M = np.column_stack([s.mv(e) for e in np.eye(s.dim, dtype=complex)]); ev = np.linalg.eigvalsh(M)[:2]
                    lv.append((ev[0], Q, par, (kx, ky))); lv.append((ev[1], Q, par, (kx, ky), 'e1'))
                else:
                    e0, al, be, it = lanczos_low(s.mv, s.dim, seed, tol=1e-10)
                    lv.append((e0, Q, par, (kx, ky)))
    return lv
def gap_from(lv, mod, g, need_e1=True):
    e0s = sorted([l for l in lv if len(l) == 4], key=lambda l: l[0]); gs = e0s[0]
    e1 = [l[0] for l in lv if len(l) == 5 and l[1:4] == gs[1:4]]
    if not e1 and need_e1:
        s = MomSector(mod, gs[1], gs[2], gs[3], g); e0, al, be, it = lanczos_low(s.mv, s.dim, 7, tol=1e-11)
        psi = lanczos_vector(s.mv, s.dim, 7, al, be); e1 = [lanczos_low(s.mv, s.dim, 8, tol=1e-10, defl=psi)[0]]
    return min([e0s[1][0]] + e1) - gs[0], gs

print('d4-far-wall-2x4 runner; labels [T] exact, [F] finite live, [R] embedded Mac mini 2x4 values')
# A [T] structure (inherited) -----------------------------------------------------------------------
ok = all(np.allclose(G, G.conj().T) and np.allclose(G @ G, np.eye(4)) for G in GAM) and all(
    np.allclose(GAM[i] @ GAM[j] + GAM[j] @ GAM[i], 0) for i in range(3) for j in range(i))
chk('A1 [T] Gamma_k Hermitian, square 1, anticommuting', ok)
ok = np.allclose(GP[0], np.kron(s3, I2)) and np.allclose(GP[1], np.kron(s1, I2)) and np.allclose(U.conj().T @ g5 @ U, -np.kron(I2, s3))
chk('A2 [T] frame: Gamma1 = sz x 1, Gamma2 = sx x 1, g5 = -(1 x tz); h_A = h_B', ok and np.allclose(species_gamma(0, 0), species_gamma(0, 1)) and np.allclose(species_gamma(1, 0), species_gamma(1, 1)),
    'A <-> B exchange is exact, so Q -> -Q')
# B [T] magnetic translations --------------------------------------------------------------------------
dims = (2, 2); A22 = Species(dims, TW, 0); errs = {}
for om in (1j, -1j):
    e = 0
    for n in range(A22.Nm + 1):
        for k in (0, 1):
            T, _ = trans_op(A22, dims, k, om, n)
            if A22.H[n].nnz: e = max(e, abs(T @ A22.H[n] - A22.H[n] @ T).max())
    errs[om] = e
chk('B1 [T] T_k (c_r -> w c_{r+e}, w = -i on a wrap) commutes with the twisted hop; w = +i does not',
    errs[-1j] < 1e-13 and errs[1j] > 0.1, 'max|[T,h]| = %.1e (w=-i), %.2f (w=+i)' % (errs[-1j], errs[1j]))
mod22 = MomModel(dims, TW, OMEGA); e = 0
for n in range(mod22.A.Nm + 1):
    for T in mod22.MA.T[n]:
        R = (mod22.MA.U[n].conj().T @ T @ mod22.MA.U[n]).toarray(); e = max(e, np.abs(R - np.diag(np.diag(R))).max())
chk('B2 [T] momentum basis diagonalises T_x, T_y in every Fock sector (2x2)', e < 1e-12, 'max off-diagonal %.1e' % e)
mod23 = MomModel((2, 3), TW, OMEGA); e = 0
for n in range(mod23.A.Nm + 1):
    for T in mod23.MA.T[n]:
        R = (mod23.MA.U[n].conj().T @ T @ mod23.MA.U[n]); D = R.diagonal(); e = max(e, abs(R - sp.diags(D)).max())
chk('B3 [T] same at 2x3 (Z2 x Z3 magnetic translations)', e < 1e-12, 'max off-diagonal %.1e' % e)
# C [F] 2x2: momentum code = parent code ------------------------------------------------------------------
g = 0.25; Mx, My = mod22.MA.M; merr = 0; eerr = 0
for Q, par in [(0, 0), (0, 1), (1, 0)]:
    full = Sector(mod22.A, mod22.B, Q, par, g, 'Cay'); ref = full.low(1)[0]; best = 1e9
    for K in [(a, b) for a in range(Mx) for b in range(My)]:
        s = MomSector(mod22, Q, par, K, g)
        if s.dim == 0: continue
        rng = np.random.default_rng(1); v = rng.standard_normal(s.dim) + 1j * rng.standard_normal(s.dim); vc = np.zeros(full.dim, complex)
        def cb(arr, nA, nB):
            k = full.idx[(nA, nB)]; o, sh = full.blocks[k][2], full.blocks[k][3]; return arr[o:o + sh[0] * sh[1]].reshape(sh)
        for i, (nA, nB, la, lb, o, sh) in enumerate(s.blocks):
            UA = mod22.MA.U[nA][:, mod22.MA.cols[nA][la]]; UB = mod22.MB.U[nB][:, mod22.MB.cols[nB][lb]]; cb(vc, nA, nB)[:] += (UB @ (UA @ s.view(v, i)).T).T
        wc = full.mv(vc); w = s.mv(v)
        for i, (nA, nB, la, lb, o, sh) in enumerate(s.blocks):
            UA = mod22.MA.U[nA][:, mod22.MA.cols[nA][la]]; UB = mod22.MB.U[nB][:, mod22.MB.cols[nB][lb]]
            merr = max(merr, np.abs((UB.conj().T @ (UA.conj().T @ cb(wc, nA, nB)).T).T - s.view(w, i)).max())
        best = min(best, lanczos_low(s.mv, s.dim, 7, tol=1e-12)[0])
    eerr = max(eerr, abs(best - ref))
chk('C1 [F] 2x2 momentum-sector matvec = parent Kronecker matvec mapped through the basis', merr < 1e-12, 'max err %.1e' % merr)
chk('C2 [F] 2x2 min over momenta of e0 = parent full-sector e0, sectors (0,0),(0,1),(1,0)', eerr < 1e-9, 'max err %.1e' % eerr)
for g in (0.25, 0.35, 0.5):
    d, gs = gap_from(mom_levels(mod22, g, [(0, 0), (0, 1), (1, 0), (1, 1)]), mod22, g)
    chk('C3 [F] 2x2 gap g=%.2f = parent %.3f' % (g, PARENT[g][0]), abs(d - PARENT[g][0]) < 1.5e-3, 'gap %.4f, GS (Q,par)=(%d,%d)' % (d, gs[1], gs[2]))
# D [F] 2x3 live re-check --------------------------------------------------------------------------------
for g in (0.25, 0.35, 0.5):
    t = time.time(); d, gs = gap_from(mom_levels(mod23, g, [(0, 0), (1, 0)]), mod23, g)
    chk('D1 [F] 2x3 gap g=%.2f = parent %.3f (sectors (0,0),(1,0), all 6 momenta)' % (g, PARENT[g][1]), abs(d - PARENT[g][1]) < 1.5e-3,
        'gap %.4f, E0/site %.3f, %.0f s' % (d, gs[0] / 6, time.time() - t))
# E [R] 2x4 (embedded Mac mini values; sector dimensions recomputed live) -----------------------------------
from math import comb
t = time.time(); mod24 = MomModel((2, 4), TW, OMEGA); Mx, My = mod24.MA.M
def kdim(Q, par, K):
    d = 0
    for nA in range(17):
        nB = nA - Q
        if nA % 2 != par or not 0 <= nB <= 16: continue
        for la, ca in mod24.MA.cols[nA].items():
            lb = ((K[0] - la // My) % Mx) * My + (K[1] - la % My) % My
            if lb in mod24.MB.cols[nB]: d += len(ca) * len(mod24.MB.cols[nB][lb])
    return d
bad = sum(kdim(Q, p, (kx, ky)) != dm for (g, Q, p, kx, ky, dm, e) in MINI_E0)
tot = all(sum(r[5] for r in MINI_E0 if r[0] == 0.25 and r[1:3] == (Q, p)) == sum(comb(16, n) * comb(16, n - Q) for n in range(17) if n % 2 == p and 0 <= n - Q <= 16)
          for Q in (0, 1) for p in (0, 1))
chk('E1 [R] embedded 2x4 rows: 3 g x 4 (Q,par) x 8 momenta; every sector dim = live recount; sums = C(16,n) formula', len(MINI_E0) == 96 and bad == 0 and tot,
    'GS sector 37,569,958 states (Q=0 total 300,546,630), %.0f s' % (time.time() - t))
F24 = free_gap((2, 4))
chk('E2 [F] free 2x4 single-particle gap', abs(F24 - 2 * np.sqrt(0.5 + np.sin(np.pi / 8) ** 2)) < 1e-12, 'Delta_free = %.4f (2x3: %.4f)' % (F24, free_gap((2, 3))))
cls = {}
for g in (0.25, 0.35, 0.5):
    rows = sorted([r for r in MINI_E0 if r[0] == g], key=lambda r: r[6]); gs = rows[0]
    e1r = [r for r in MINI_E1 if r[0] == g][0]
    lv = sorted([r[6] for r in rows[1:]] + [e1r[6]]); d = lv[0] - gs[6]
    q10 = sorted(r[6] for r in rows if r[1:3] == (1, 0)); q11 = sorted(r[6] for r in rows if r[1:3] == (1, 1))
    uniq = d > 1e-6 and abs(e1r[5] - gs[6]) < 1e-6 and e1r[7] < 1e-5 and gs[1:5] == e1r[1:5]
    r23 = d / PARENT[g][1]
    c = 'CLOSING' if d < 0.5 * PARENT[g][1] else ('SURVIVING' if (r23 >= 0.9 and uniq) else 'INCONCLUSIVE'); cls[g] = c
    chk('E3 [R] g=%.2f: unique GS in (Q,par,K)=(%d,%d,(%d,%d)); (1,0),(1,1) momentum spectra coincide' % ((g,) + gs[1:5]), uniq and np.allclose(q10, q11, atol=1e-6),
        'E0/site %.3f, e1-e0 in GS K %.3f, resid %.0e' % (gs[6] / 8, e1r[6] - e1r[5], e1r[7]))
    chk('E4 [R] g=%.2f pre-set class: %s' % (g, c), c != 'CLOSING',
        'gap 2x2 %.3f -> 2x3 %.3f -> 2x4 %.3f; 2x4/2x3 = %.3f; 2x4/free = %.2f' % (PARENT[g][0], PARENT[g][1], d, r23, d / F24))
chk('E5 [R] verdict at these sizes: no fixed g closes; all three SURVIVING (ratio >= 0.9, unique GS)', all(v == 'SURVIVING' for v in cls.values()),
    'g=0.25 gap is non-monotone (0.886, 0.290, 0.700): 2x3 sits on its own avoided crossing')
print('wall %.1f s, peak RSS %.0f MB' % (time.time() - T0, peak_mb()))
print('TOTAL: PASS=%d FAIL=%d' % (NP[0], NF[0]))
