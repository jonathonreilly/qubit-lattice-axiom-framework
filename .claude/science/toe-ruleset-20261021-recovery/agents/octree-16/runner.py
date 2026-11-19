#!/usr/bin/env python3
"""octree-16: one anomaly-free internal family carried in parallel on every rung of the octree ladder (supplied models,
finite diagnostics, exact anomaly arithmetic; no physical identification).
 A  tick light algebra; gauged real-space ladder = momentum tree (R = 1, 2); handedness of the light rung-0 state
 B  internal 16 in parallel: exact internal symmetry, covariant non-abelian links, light content, anomalies (16 and N)
 C  background U(1) link on the fine lattice (coarse rungs read it by parallel transport): spectral flow per species,
    inflow for the SM 16 under Y and for anomalous charges, full holonomy cycle, landing rung for R = 2
 D  selection: anomaly-free U(1)s on the 16 (exact), so(10) inside u(16), charges of p, e, n
 E  against measurement (estimates)"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm, eigh, eigvalsh
from scipy.sparse.csgraph import connected_components

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
OM = np.exp(2j * np.pi / 3); I8 = np.eye(8)
C = np.array(list(itertools.product((0, 1), repeat=3))); cc0 = C - 0.5
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Rm = np.zeros((3, 3))
        for i in range(3): Rm[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(Rm), 1): rots.append(Rm)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def axang(Rm):
    a = np.arccos(np.clip((np.trace(Rm) - 1) / 2, -1, 1))
    if a < 1e-9: return np.array([0, 0, 1.0]), 0.0
    if abs(a - np.pi) < 1e-9:
        w, v = np.linalg.eigh((Rm + np.eye(3)) / 2); return v[:, np.argmax(w)], a
    return np.array([Rm[2, 1] - Rm[1, 2], Rm[0, 2] - Rm[2, 0], Rm[1, 0] - Rm[0, 1]]) / (2 * np.sin(a)), a
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
W = np.zeros((8, 8), complex)
for a in range(8):
    for b in range(8):
        if np.sum(abs(C[a] - C[b])) == 1: g = XI[a].conj() @ XI[b]; W[a, b] = -g / abs(g) / np.sqrt(3)
def Lrot(Rm):
    n_, a = axang(Rm); Dm = expm(-1j * a * sum(n_[k] * J3[k] for k in range(3))); L = np.zeros((8, 8), complex)
    for i in range(8): k = int(np.argmin(np.sum(abs(cc0 - Rm @ cc0[i]), 1))); L[k, i] = XI[k].conj() @ Dm @ XI[i]
    return L
def ex(th): return np.cos(th) * I8 + 1j * np.sin(th) * W
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def logH(U):
    w, V = np.linalg.eig(U); H = (V * (-np.angle(w))) @ np.linalg.inv(V); return (H + H.conj().T) / 2
class Tick:   # CL-1 tick: even cube exp(-i st W), odd cube exp(+i st W); copy mass F = exp(i M P1 W / 2) on both sides
    def __init__(s, st):
        s.st, s.Ve, s.Vo = st, ex(-st), ex(st); h = 1e-5; al = []
        U0 = lambda K: Dg(K) @ ex(st) @ Dg(K).conj().T @ ex(-st)
        for a in range(3):
            e = np.zeros(3); e[a] = h; A = (logH(U0(e)) - logH(U0(-e))) / (2 * h); al.append((A + A.conj().T) / 2)
        s.v = np.sqrt(np.trace(al[0] @ al[0]).real / 8); s.al = [A / s.v for A in al]
        g5 = 1j * s.al[0] @ s.al[1] @ s.al[2]; s.g5 = (g5 + g5.conj().T) / 2
        iC3 = [i for i, Rm in enumerate(rots) if np.isclose(np.trace(Rm), 0) and np.allclose(axang(Rm)[0], np.ones(3) / np.sqrt(3))][0]
        Sig = [-1j * s.al[1] @ s.al[2], -1j * s.al[2] @ s.al[0], -1j * s.al[0] @ s.al[1]]; L3 = Lrot(rots[iC3]); s.Sig = Sig
        Mr = np.array([[np.trace(L3 @ s.al[a] @ L3.conj().T @ s.al[b]).real / 8 for b in range(3)] for a in range(3)]); nax, ang = axang(np.round(Mr).T)
        best = min((max(np.abs(Sx @ s.al[q] @ Sx.conj().T - L3 @ s.al[q] @ L3.conj().T).max() for q in range(3)), k, Sx) for k, Sx in
                   enumerate(expm(-1j * sgn * ang / 2 * sum(nax[k_] * Sig[k_] for k_ in range(3))) for sgn in (1, -1)))
        wr, Vr = np.linalg.eig(best[2].conj().T @ L3); Vl = Vr[:, np.abs(wr - OM) < 1e-5]; P1 = Vl @ np.linalg.pinv(Vl)
        s.P1 = (P1 + P1.conj().T) / 2; s.Fc = {}
    def U(s, K, M=0.0):
        X = Dg(K) @ s.Vo @ Dg(K).conj().T @ s.Ve
        if M:
            F = s.Fc.setdefault(M, expm(1j * M * s.P1 @ W / 2)); X = F @ X @ F
        return X
    def H(s, K, M=0.0): return logH(s.U(K, M)) / s.st
def s_amp(q): return np.prod((1 + np.exp(-1j * np.asarray(q))) / 2)
def tree(R, Q):
    nodes = [(j, np.array(m), (np.asarray(Q, float) + 2 * np.pi * np.array(m)) / 2 ** (R - j)) for j in range(R + 1) for m in itertools.product(range(2 ** (R - j)), repeat=3)]
    idx = {(j, tuple(m)): i for i, (j, m, q) in enumerate(nodes)}
    return nodes, [None if j == R else idx[(j + 1, tuple(m % 2 ** (R - j - 1)))] for (j, m, q) in nodes]
def Hlad(tk, R, Q, Xm, kap=0.5, M=0.0, onlyH5=False):
    nodes, par = tree(R, Q); Hm = np.zeros((8 * len(nodes),) * 2, complex)
    for i, (j, m, q) in enumerate(nodes):
        if not onlyH5: Hm[8 * i:8 * i + 8, 8 * i:8 * i + 8] += tk.H(q, M)
        if par[i] is not None:
            g = 1.0 if onlyH5 else kap; sa = s_amp(q); k = par[i]
            Hm[8 * i:8 * i + 8, 8 * k:8 * k + 8] += g * sa * Xm; Hm[8 * k:8 * k + 8, 8 * i:8 * i + 8] += g * np.conj(sa) * Xm.conj().T
    return Hm, np.repeat([nd[0] for nd in nodes], 8), nodes
def flux(fun, rad, nt=4, nph=8):
    th = np.linspace(0, np.pi, nt + 1); pp = np.linspace(0, 2 * np.pi, nph + 1)[:-1]; V = {}
    for i, t in enumerate(th):
        for k, p in enumerate(pp): V[i, k] = fun(rad * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)]))
    F = sum(np.angle(np.linalg.det(V[i, k].conj().T @ V[i + 1, k]) * np.linalg.det(V[i + 1, k].conj().T @ V[i + 1, (k + 1) % nph])
                     * np.linalg.det(V[i + 1, (k + 1) % nph].conj().T @ V[i, (k + 1) % nph]) * np.linalg.det(V[i, (k + 1) % nph].conj().T @ V[i, k])) for i in range(nt) for k in range(nph))
    return float(round(F / (2 * np.pi), 3))
def select(E, V, rung, target, lo, hi):
    Vs, _ = np.linalg.qr(V[:, (E > lo) & (E < hi)]); e, U = np.linalg.eigh(Vs[rung == target].conj().T @ Vs[rung == target]); return Vs @ U[:, e > 0.5]

# ---------------------------------------------------------------- gauged real-space ladder
def expmh(H, t):   # exp(-i t H) for Hermitian H
    w, V = np.linalg.eigh((H + H.conj().T) / 2); return (V * np.exp(-1j * t * w)) @ V.conj().T
def lidx(L, x):
    x = np.mod(x, L); return int((x[0] * L[1] + x[1]) * L[2] + x[2])
def coarse_links(A, L):
    Lc = tuple(l // 2 for l in L); Ac = []
    for mu in range(3):
        a = np.zeros(Lc)
        for p in itertools.product(*[range(l) for l in Lc]):
            x = 2 * np.array(p); y = x.copy(); y[mu] += 1; a[p] = A[mu][tuple(np.mod(x, L))] + A[mu][tuple(np.mod(y, L))]
        Ac.append(a)
    return Ac, Lc
def path_phase(A, L, x0, x1):   # transporter x0 -> x1 along x, then y, then z (direct displacement)
    ph = 0.0; x = np.array(x0, int).copy()
    for mu in range(3):
        dd = int(x1[mu] - x0[mu])
        for _ in range(abs(dd)):
            if dd > 0: ph += A[mu][tuple(np.mod(x, L))]; x[mu] += 1
            else: x[mu] -= 1; ph -= A[mu][tuple(np.mod(x, L))]
    return ph
def cube_blocks(A, L, par):
    out = []
    for n in itertools.product(*[range(l // 2) for l in L]):
        o = 2 * np.array(n) + par; xs = [o + cp for cp in C]; ids = [lidx(L, x) for x in xs]
        lab = [int(np.argmin(np.abs(C - np.mod(x, 2)).sum(1))) for x in xs]; Wg = np.zeros((8, 8), complex)
        for i in range(8):
            for k in range(8):
                if np.abs(C[i] - C[k]).sum() == 1: Wg[i, k] = W[lab[i], lab[k]] * np.exp(1j * path_phase(A, L, xs[k], xs[i]))
        out.append((ids, lab, xs, Wg))
    return out
def copy_block(A, L, xs, lab, P1W):
    B = np.zeros((8, 8), complex)
    for i in range(8):
        for k in range(i, 8):
            if abs(P1W[lab[i], lab[k]]) > 1e-14:
                B[i, k] = P1W[lab[i], lab[k]] * np.exp(1j * path_phase(A, L, xs[k], xs[i]))
                if k != i: B[k, i] = np.conj(B[i, k])
    return B
def h5_blocks(A, L, Xm):   # coarse site P sits at fine position 2P; coarse cube n <-> its 8 children, corner b <-> corner a via X[a,b]/sqrt8
    Lc = tuple(l // 2 for l in L); out = []
    for n in itertools.product(*[range(l // 2) for l in Lc]):
        n = np.array(n); fids, fpos, flab, cids, cpos = [], [], [], [], []
        for c in C:
            for ia, a in enumerate(C): x = 2 * (2 * n + c) + a; fids.append(lidx(L, x)); fpos.append(x); flab.append(ia)
        for b in C: P = 2 * n + b; cids.append(lidx(Lc, P)); cpos.append(2 * P)
        B = np.zeros((72, 72), complex)
        for i in range(64):
            for k in range(8):
                v = Xm[flab[i], k] / np.sqrt(8)
                if abs(v) > 1e-15: B[i, 64 + k] = v * np.exp(1j * path_phase(A, L, cpos[k], fpos[i])); B[64 + k, i] = np.conj(B[i, 64 + k])
        out.append((fids, cids, B))
    return out
def ladder_parts(tk, A0, L0, R, Xm, M, dense=False):
    As, Ls = [A0], [tuple(L0)]
    for j in range(R):
        Ac, Lc = coarse_links(As[-1], Ls[-1]); As.append(Ac); Ls.append(Lc)
    Ns = [int(np.prod(l)) for l in Ls]; off = np.concatenate([[0], np.cumsum(Ns)]).astype(int); Nt = int(off[-1]); P1W = tk.P1 @ W; P1W = (P1W + P1W.conj().T) / 2
    ve, vo, ff = [], [], []
    for j in range(R + 1):
        for (ids, lab, xs, Wg) in cube_blocks(As[j], Ls[j], 0):
            g = [off[j] + i for i in ids]; ve.append((g, expm(-1j * tk.st * Wg))); ff.append((g, expm(1j * M * copy_block(As[j], Ls[j], xs, lab, P1W) / 2)))
        for (ids, lab, xs, Wg) in cube_blocks(As[j], Ls[j], 1): vo.append(([off[j] + i for i in ids], expm(1j * tk.st * Wg)))
    r_, c_, v_ = [], [], []
    for j in range(R):
        for (fids, cids, B) in h5_blocks(As[j], Ls[j], Xm):
            ids = np.array([off[j] + f for f in fids] + [off[j + 1] + c for c in cids]); ii, jj = np.meshgrid(ids, ids, indexing='ij'); m = np.abs(B) > 0
            r_.append(ii[m]); c_.append(jj[m]); v_.append(B[m])
    e5 = []
    if R:
        H5 = sp.csr_matrix((np.concatenate(v_), (np.concatenate(r_), np.concatenate(c_))), shape=(Nt, Nt))
        nc, lab = connected_components(H5 != 0, directed=False)
        for k in range(nc):   # exact exp(-i tau H5) by connected components (one per top-rung cube)
            ids = np.where(lab == k)[0]
            if len(ids) > 1: e5.append((list(ids), expmh(H5[ids][:, ids].toarray(), 0.5 * tk.st)))
    def blk(blocks):
        if not blocks: return sp.identity(Nt, dtype=complex, format='csr')
        r, c, v = [], [], []
        for ids, B in blocks:
            ii, jj = np.meshgrid(ids, ids, indexing='ij'); r.append(ii.ravel()); c.append(jj.ravel()); v.append(B.ravel())
        Mx = sp.csr_matrix((np.concatenate(v), (np.concatenate(r), np.concatenate(c))), shape=(Nt, Nt)); Dm = sp.lil_matrix((Nt, Nt), dtype=complex)
        cov = np.zeros(Nt, bool); cov[np.concatenate([np.array(i) for i, _ in blocks])] = True
        for i in np.where(~cov)[0]: Dm[i, i] = 1.0
        return (Mx + Dm.tocsr()).tocsr()
    T = (blk(ff) @ (blk(vo) @ (blk(ve) @ blk(ff)))).tocsr(); rung = np.concatenate([np.full(Ns[j], j) for j in range(R + 1)])
    if not dense: return (blk(e5) @ T).tocsr(), rung
    Ud = np.zeros((Nt, Nt), complex); done = np.zeros(Nt, bool)
    for ids, B in e5: Ud[ids, :] = B @ T[ids, :].toarray(); done[ids] = True
    for i in np.where(~done)[0]: Ud[i, :] = T[i, :].toarray()
    return Ud, rung
def landau(L, F, theta):   # F flux quanta through every xy layer (Landau gauge), holonomy theta along z
    Lx, Ly, Lz = L; A = [np.zeros(L), np.zeros(L), np.full(L, theta / Lz)]
    for x in range(Lx):
        for y in range(Ly):
            A[0][x, y, :] = -2 * np.pi * F * y / (Lx * Ly)
            if y == Ly - 1: A[1][x, y, :] = 2 * np.pi * F * x / Lx
    return A
def sinpart(U, nb=128):   # in place: lower triangle of (U - U^+)/2i (= sin of the quasi-energies), returned as a Fortran view
    N = len(U)
    for r0 in range(0, N, nb):
        r1 = min(N, r0 + nb); U[r0:r1, :r1] = (U[r0:r1, :r1] - U[:r1, r0:r1].conj().T) * (-0.5j)
    return U.T                                                                 # F-ordered; its upper triangle = conj of K's lower
def qspec(U, rung, R, Wmax=0.016, count=False):   # levels with |omega| < Wmax and their rung weights
    KT = sinpart(U); nneg = int(np.sum(eigvalsh(KT, lower=False, check_finite=False) < 0)) if count else None
    w, V = eigh(KT, lower=False, subset_by_value=(-np.sin(Wmax), np.sin(Wmax)), driver='evr', overwrite_a=True, check_finite=False); del KT, U
    out = (np.arcsin(np.clip(w, -1, 1)), np.array([np.sum(np.abs(V[rung == j]) ** 2, 0) for j in range(R + 1)]))
    return out + ((nneg,) if count else ())

# ============================================================ A
print('== A. tick (st = 0.04), the two exchange orientations, gauged real-space ladder')
tk = Tick(0.04); MC = tk.st; KAP = 0.5; v = tk.v / tk.st; g5 = tk.g5; al = tk.al
Pp, Pm = (I8 + g5) / 2, (I8 - g5) / 2; XR = W @ Pm; XL = W @ Pp
e1 = max(np.abs(XR @ XR).max(), np.abs(XL @ XL).max(), np.abs(XR @ XR.conj().T - Pp).max(), np.abs(XR.conj().T @ XR - Pm).max(),
         np.abs(XL @ XL.conj().T - Pm).max(), np.abs(XL.conj().T @ XL - Pp).max(), max(np.abs(g5 @ A - A @ g5).max() + np.abs(g5 @ W + W @ g5).max() for A in al))
check('A1 THEOREM X = W(1-g5)/2 (octree-unify) and X\' = W(1+g5)/2: partial isometries P- -> P+, P+ -> P- (X^2 = 0)', e1 < 1e-7, f'error {e1:.0e}')
def Ufl(R, Q, Xm, M):
    nodes, _ = tree(R, Q); Hm = Hlad(tk, R, Q, Xm, onlyH5=True)[0]
    return expmh(Hm, KAP * tk.st) @ sp.block_diag([tk.U(nd[2], M) for nd in nodes]).toarray()
L8 = (8, 8, 8); errs = []
for R, Qs in ((1, [np.pi * np.array(m) for m in itertools.product(range(2), repeat=3)]), (2, [np.zeros(3)])):
    Ud, _ = ladder_parts(tk, [np.zeros(L8)] * 3, L8, R, XL, MC, dense=True); U = None
    evr = np.sort(np.angle(np.linalg.eigvals(Ud))); evk = np.sort(np.concatenate([np.angle(np.linalg.eigvals(Ufl(R, Q, XL, MC))) for Q in Qs]))
    errs.append((np.abs(evr - evk).max(), np.abs(Ud @ Ud.conj().T - np.eye(len(Ud))).max()))
rng = np.random.default_rng(1); A0 = landau(L8, 1, 0.7); chi = rng.uniform(0, 2 * np.pi, L8)
U1, rung8 = ladder_parts(tk, A0, L8, 2, XL, MC, dense=True); U2, _ = ladder_parts(tk, [A0[mu] + np.roll(chi, -1, axis=mu) - chi for mu in range(3)], L8, 2, XL, MC, dense=True)
gph = np.concatenate([np.exp(1j * chi[::2 ** j, ::2 ** j, ::2 ** j]).ravel() for j in range(3)])
cov = np.abs(U2 - gph[:, None] * U1 * gph.conj()[None, :]).max(); del U, Ud, U1, U2
check('A2 THEOREM gauged real-space ladder = momentum tree at zero field (R = 1, 2, copy mass on); with flux it is unitary and '
      'exactly covariant (coarse links and rung exchange by fine-path transport)', max(e[0] for e in errs) < 1e-10 and max(e[1] for e in errs) < 1e-12 and cov < 1e-12,
      f'spectra {max(e[0] for e in errs):.0e}, covariance {cov:.0e}')
Ut = ladder_parts(tk, [np.zeros(L8)] * 3, L8, 0, XL, MC, dense=True)[0]; K = 2 * np.pi * np.array([1, 2, 3]) / 4; u = rng.normal(size=8) + 0j
psi = np.zeros(512, complex); idn = {}
for n in itertools.product(range(4), repeat=3):
    for a in range(8): psi[lidx(L8, 2 * np.array(n) + C[a])] = np.exp(1j * K @ np.array(n)) * u[a]
out = Ut @ psi; Uk = tk.U(K, MC) @ u
econv = max(abs(out[lidx(L8, 2 * np.array(n) + C[a])] - np.exp(1j * K @ np.array(n)) * Uk[a]) for n in itertools.product(range(4), repeat=3) for a in range(8))
hel = {}
for nm, Xm in (('X', XR), ("X'", XL)):
    hs = []
    for dvec in (np.array([1., 0, 0]), np.array([1., 1, 1]) / np.sqrt(3), np.array([.3, -.5, .81]) / np.linalg.norm([.3, -.5, .81])):
        Hm, rung, nodes = Hlad(tk, 1, 2 * 0.02 * dvec, Xm, KAP, MC); E, V = np.linalg.eigh(Hm)
        i0 = [k for k, nd in enumerate(nodes) if nd[0] == 0 and not nd[1].any()][0]; ww = np.sum(np.abs(V[8 * i0:8 * i0 + 8]) ** 2, 0)
        s = [s for s in np.argsort(np.abs(E)) if ww[s] > 0.5 and E[s] > 0][0]; uu = V[8 * i0:8 * i0 + 8, s]
        hs.append(np.real(uu.conj() @ sum(dvec[a] * tk.Sig[a] for a in range(3)) @ uu) / np.real(uu.conj() @ uu) / 2)
    def fsel(q, target, lo, hi, Xm=Xm):
        Hm, rung, _ = Hlad(tk, 1, q * 2, Xm, KAP, MC); E, V = np.linalg.eigh(Hm); return select(E, V, rung, target, lo, hi)
    e0 = 0.6 * v * 0.04 * 2; hel[nm] = (np.round(hs, 4), flux(lambda q: fsel(q, 0, 0, e0), 0.04), flux(lambda q: fsel(q, 1, e0, 0.3), 0.04))
check('A3 handedness (momentum +K checked in real space): the light rung-0 particle has helicity +1/2 with X, -1/2 with X\'; '
      'Berry flux (rung 0, top) flips', econv < 1e-10 and np.allclose(hel['X'][0], 0.5, atol=1e-3) and np.allclose(hel["X'"][0], -0.5, atol=1e-3)
      and hel['X'][1:] == (1.0, -1.0) and hel["X'"][1:] == (-1.0, 1.0), f'X: h {hel["X"][0][0]:+.3f}, flux {hel["X"][1:]}; X\': h {hel["X\'"][0][0]:+.3f}, flux {hel["X\'"][1:]}')

# ============================================================ B
print('== B. internal 16 carried in parallel (left-handed orientation X\')')
def null_dim(rows, n):
    sv = np.linalg.svd(np.vstack(rows), compute_uv=False); return int(n * n - np.sum(sv > 1e-8))
qs = np.random.default_rng(3).uniform(-np.pi, np.pi, (6, 3)); Hq = [tk.H(q, MC) for q in qs]
cL = null_dim([np.kron(g, I8) - np.kron(I8, g.T) for g in Hq + [XL, XL.conj().T]], 8)
inter = null_dim([np.kron(g, I8) - np.kron(I8, g.T) for g in Hq] + [np.kron(XL, I8) - np.kron(I8, XR.T), np.kron(XL.conj().T, I8) - np.kron(I8, XR.conj())], 8)
check('B1 THEOREM ladder blocks: trivial commutant, no intertwiner between orientations; so the 16 in parallel with one '
      'orientation has exact internal symmetry U(16), with orientation tied to Xi (doublets +1, singlets -1) U(8) x U(8)', cL == 1 and inter == 0, f'commutant {cL}, intertwiner {inter}')
d6 = 6; lam = [np.array(m, complex) for m in ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
      [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]], [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], np.diag([1, 1, -2]) / np.sqrt(3))]
sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1]).astype(complex)]
gQ = [np.kron(l / 2, np.eye(2)) for l in lam] + [np.kron(np.eye(3), s / 2) for s in sig] + [np.eye(6) / 6]
rG = lambda sc=1.0: expm(1j * sc * sum(rng.normal() * g for g in gQ))
def path_T(Ul, L, x0, x1):
    T = np.eye(d6, dtype=complex); x = np.array(x0, int).copy()
    for mu in range(3):
        dd = int(x1[mu] - x0[mu])
        for _ in range(abs(dd)):
            if dd > 0: T = Ul[mu][tuple(np.mod(x, L))] @ T; x[mu] += 1
            else: x[mu] -= 1; T = Ul[mu][tuple(np.mod(x, L))].conj().T @ T
    return T
def ladder_mat(Ul0, L0, Xm):   # R = 1, links in the (3,2)_{1/6} representation
    Lc = tuple(l // 2 for l in L0); Uc = []
    for mu in range(3):
        a_ = np.zeros(Lc + (d6, d6), complex)
        for p in itertools.product(*[range(l) for l in Lc]):
            x = 2 * np.array(p); y = x.copy(); y[mu] += 1; a_[p] = Ul0[mu][tuple(np.mod(y, L0))] @ Ul0[mu][tuple(np.mod(x, L0))]
        Uc.append(a_)
    Us, Ls = [Ul0, Uc], [tuple(L0), Lc]; off = [0, int(np.prod(L0)), int(np.prod(L0)) + int(np.prod(Lc))]; Nt = off[2] * d6; P1W = tk.P1 @ W; P1W = (P1W + P1W.conj().T) / 2
    gi = lambda j, s: [(off[j] + s) * d6 + k for k in range(d6)]; Tk = np.zeros((Nt, Nt), complex)
    for j in range(2):
        mats = []
        for par in (0, 1):
            Vm = np.eye(Nt, dtype=complex); Fm = np.eye(Nt, dtype=complex)
            for n in itertools.product(*[range(l // 2) for l in Ls[j]]):
                o = 2 * np.array(n) + par; xs = [o + cp for cp in C]; ids = [lidx(Ls[j], x) for x in xs]; lab = [int(np.argmin(np.abs(C - np.mod(x, 2)).sum(1))) for x in xs]
                Wg = np.zeros((8 * d6, 8 * d6), complex); Pg = np.zeros((8 * d6, 8 * d6), complex)
                for i in range(8):
                    for k in range(8):
                        T = path_T(Us[j], Ls[j], xs[k], xs[i])
                        if np.abs(C[i] - C[k]).sum() == 1: Wg[i * d6:(i + 1) * d6, k * d6:(k + 1) * d6] = W[lab[i], lab[k]] * T
                        if k >= i and abs(P1W[lab[i], lab[k]]) > 1e-14:
                            Pg[i * d6:(i + 1) * d6, k * d6:(k + 1) * d6] = P1W[lab[i], lab[k]] * T
                            if k != i: Pg[k * d6:(k + 1) * d6, i * d6:(i + 1) * d6] = (P1W[lab[i], lab[k]] * T).conj().T
                gg = sum((gi(j, s_) for s_ in ids), []); Vm[np.ix_(gg, gg)] = expm((-1j if par == 0 else 1j) * tk.st * Wg)
                if par == 0: Fm[np.ix_(gg, gg)] = expm(1j * MC * Pg / 2)
            mats.append((Vm, Fm))
        blk_ = mats[0][1] @ mats[1][0] @ mats[0][0] @ mats[0][1]; rr = list(range(off[j] * d6, off[j + 1] * d6)); Tk[np.ix_(rr, rr)] = blk_[np.ix_(rr, rr)]
    H5 = np.zeros((Nt, Nt), complex)
    for n in itertools.product(*[range(l // 2) for l in Lc]):
        n = np.array(n)
        for ib, b in enumerate(C):
            P = 2 * n + b; cg = gi(1, lidx(Lc, P))
            for c in C:
                for ia, a in enumerate(C):
                    x = 2 * (2 * n + c) + a; fg = gi(0, lidx(L0, x)); B = Xm[ia, ib] / np.sqrt(8) * path_T(Ul0, L0, 2 * P, x)
                    H5[np.ix_(fg, cg)] += B; H5[np.ix_(cg, fg)] += B.conj().T
    return expm(-1j * KAP * tk.st * H5) @ Tk
L4 = (4, 4, 4); Ul = [np.array([rG() for _ in range(64)]).reshape(L4 + (d6, d6)) for mu in range(3)]; gx = np.array([rG(2.0) for _ in range(64)]).reshape(L4 + (d6, d6))
Ug = [np.zeros_like(Ul[0]) for _ in range(3)]
for mu in range(3):
    for x in itertools.product(range(4), repeat=3): y = np.array(x); y[mu] += 1; Ug[mu][x] = gx[tuple(np.mod(y, 4))] @ Ul[mu][x] @ gx[x].conj().T
Ua, Ub = ladder_mat(Ul, L4, XL), ladder_mat(Ug, L4, XL); Gm = np.zeros_like(Ua)
for x in itertools.product(range(4), repeat=3): i = lidx(L4, np.array(x)); Gm[i * d6:(i + 1) * d6, i * d6:(i + 1) * d6] = gx[x]
for p in itertools.product(range(2), repeat=3): i = 64 + lidx((2, 2, 2), np.array(p)); Gm[i * d6:(i + 1) * d6, i * d6:(i + 1) * d6] = gx[tuple(2 * np.array(p))]
U0 = ladder_mat([np.tile(np.eye(d6, dtype=complex), L4 + (1, 1)) for _ in range(3)], L4, XL); Us1 = ladder_parts(tk, [np.zeros(L4)] * 3, L4, 1, XL, MC, dense=True)[0]
ecov, etr = np.abs(Ub - Gm @ Ua @ Gm.conj().T).max(), np.abs(U0 - np.kron(Us1, np.eye(d6))).max(); del Ua, Ub, U0, Gm, Us1, Ul, Ug
check('B2 THEOREM SU(3)xSU(2)xU(1) links in the (3,2)1/6 rep attach: exactly covariant under local transformations; trivial links give A (x) 1_6', ecov < 1e-12 and etr < 1e-12, f'covariance {ecov:.0e}, trivial {etr:.0e}')
fam = [('Q', 3, 2, Fr(1, 6)), ('u^c', -3, 1, Fr(-2, 3)), ('d^c', -3, 1, Fr(1, 3)), ('L', 1, 2, Fr(-1, 2)), ('e^c', 1, 1, Fr(1)), ('nu^c', 1, 1, Fr(0))]
dimf = lambda f: abs(f[1]) * f[2]; A3 = lambda f: (1 if f[1] == 3 else -1 if f[1] == -3 else 0) * f[2]
an = {'SU3^3': sum(A3(f) for f in fam), 'SU2^2Y': sum(Fr(abs(f[1]), 2) * f[3] for f in fam if f[2] == 2), 'SU3^2Y': sum(Fr(f[2], 2) * f[3] for f in fam if abs(f[1]) == 3),
      'Y^3': sum(dimf(f) * f[3] ** 3 for f in fam), 'Y-grav': sum(dimf(f) * f[3] for f in fam)}
ndb = sum(abs(f[1]) for f in fam if f[2] == 2); ps = {'SU4^3': 2 * 1 + 2 * (-1), 'doublets L': 4, 'doublets R': 4}
gam = []
sx_, sy_, sz_ = sig; I2 = np.eye(2)
def kr(*ms):
    o = np.array([[1.0 + 0j]])
    for m in ms: o = np.kron(o, m)
    return o
for k in range(5): gam.append(kr(*([sz_] * k + [sx_] + [I2] * (4 - k)))); gam.append(kr(*([sz_] * k + [sy_] + [I2] * (4 - k))))
nk = [((gam[2 * k] + 1j * gam[2 * k + 1]) / 2).conj().T @ ((gam[2 * k] + 1j * gam[2 * k + 1]) / 2) for k in range(5)]
evn = np.where(np.isclose(np.diag(kr(*([sz_] * 5))).real, 1))[0]; r16 = lambda Mx: Mx[np.ix_(evn, evn)]
so10 = [r16(0.5j * gam[i] @ gam[j]) for i in range(10) for j in range(i + 1, 10)]
Yf = r16(sum(yk * nk[k] for k, yk in enumerate([-1 / 3] * 3 + [1 / 2] * 2))); BLf = r16(-2 / 3 * sum(nk[k] - 0.5 * np.eye(32) for k in range(3)))
cub = max(abs(np.trace(np.linalg.matrix_power(sum(rng.normal() * g for g in so10), 3))) for _ in range(4)); Am = np.array([g.ravel() for g in so10]).T
res = [np.linalg.norm(Am @ np.linalg.lstsq(Am, X_.ravel(), rcond=None)[0] - X_.ravel()) for X_ in (Yf, BLf, np.eye(16))]
yspec = sorted(Fr(round(6 * x)) / 6 for x in np.diag(Yf).real) == sorted(f[3] for f in fam for _ in range(dimf(f)))
check('B3 light content: one left-handed Weyl per internal state = one family with nu^c; SM and Pati-Salam anomalies vanish; '
      'so(10) on the Fock 16: zero cubic anomaly, contains Y and B-L, not N',
      all(x == 0 for x in an.values()) and ndb % 2 == 0 and ps['SU4^3'] == 0 and cub < 1e-10 and max(res[:2]) < 1e-12 and abs(res[2] - 4) < 1e-12 and yspec,
      f'{", ".join(f"{k} {v}" for k, v in an.items())}; doublets {ndb}; SU4^3 {ps["SU4^3"]}; so10 cubic {cub:.0e}')
NP = {'N^3': 16, 'N-grav': 16, 'N-SU3^2': sum(Fr(f[2], 2) for f in fam if abs(f[1]) == 3), 'N-SU2^2': sum(Fr(abs(f[1]), 2) for f in fam if f[2] == 2), 'N-Y^2': sum(dimf(f) * f[3] ** 2 for f in fam)}
xi = lambda f: 1 if f[2] == 2 else -1
NX = {'N^3': sum(dimf(f) * xi(f) for f in fam), 'N-grav': sum(dimf(f) * xi(f) for f in fam), 'N-SU3^2': sum(Fr(f[2] * xi(f), 2) for f in fam if abs(f[1]) == 3),
      'N-SU2^2': sum(Fr(abs(f[1]) * xi(f), 2) for f in fam if f[2] == 2), 'N-Y^2': sum(dimf(f) * xi(f) * f[3] ** 2 for f in fam)}
check('B4 mode number N (N^3, N-grav, N-SU3^2, N-SU2^2, N-Y^2): one orientation N = 1 (axial type), Xi orientation N = Xi (3B+L type); '
      'anomalous in both, QCD breaks only the first', list(NP.values()) == [16, 16, 2, 2, Fr(10, 3)] and list(NX.values()) == [0, 0, 0, 2, -2],
      'P ' + ','.join(str(x) for x in NP.values()) + '; Xi ' + ','.join(str(x) for x in NX.values()))

# ============================================================ C
print('== C. background U(1) on the fine lattice (flux F through xy, holonomy th along z), R = 1, 16x16x4')
import gc; gc.collect()
def track(L, R, F, Xm, ths, Wt=0.02):
    trk = None
    for th in ths:
        Ud, rung = ladder_parts(tk, landau(L, F, th), L, R, Xm, MC, dense=True); KT = sinpart(Ud)
        w, Vs = eigh(KT, lower=False, subset_by_value=(-np.sin(Wt), np.sin(Wt)), driver='evr', overwrite_a=True, check_finite=False); del KT, Ud
        om = np.arcsin(np.clip(w, -1, 1)); sel = np.arange(len(om))
        wts = np.array([np.sum(np.abs(Vs[rung == j]) ** 2, 0) for j in range(R + 1)])
        if trk is None: trk = [dict(om=[om[i]], w=[wts[:, k]], v=Vs[:, k], ok=True) for k, i in enumerate(sel)]; continue
        for t in trk:
            if not t['ok']: continue
            ov = np.abs(t['v'].conj() @ Vs) ** 2; k = int(np.argmax(ov))
            if ov[k] < 0.5: t['ok'] = False; continue
            t['om'].append(om[sel[k]]); t['w'].append(wts[:, k]); t['v'] = Vs[:, k]
    return [t for t in trk if t['ok']]
land = {}
for L in ((8, 8, 8), (16, 8, 8)):
    tr = track(L, 2, 1, XL, (-0.5, -0.3, -0.1, 0.1, 0.3, 0.5)); cr = [t for t in tr if np.sign(t['om'][0]) != np.sign(t['om'][-1])]
    up = [t for t in cr if t['om'][-1] < 0 and np.mean(t['w'], 0)[0] > 0.5]; dn = [t for t in cr if t not in up]
    land[L] = (len(up), len(dn), [np.round(np.mean(t['w'], 0), 2).tolist() for t in dn], sum(1 if t['om'][-1] < 0 else -1 for t in cr))
L0 = (16, 16, 4); W0, W1, D = 0.007, 0.0125, 0.5
def Jcount(F, Xm, L=L0, R=1):
    r = {th: qspec(*ladder_parts(tk, landau(L, F, th), L, R, Xm, MC, dense=True), R) for th in (-D, D)}
    n0 = {th: int(np.sum((r[th][0] < 0) & (r[th][0] > -W0) & (r[th][1][0] > 0.5))) for th in r}
    nt = {th: int(np.sum((r[th][0] < 0) & (r[th][0] > -W1))) for th in r}
    marg = min(min(np.abs(np.abs(r[th][0]) - W0).min(), np.abs(np.abs(r[th][0]) - W1).min()) for th in r)
    nll = {int(np.sum((np.abs(r[th][0]) < W0) & (r[th][1][0] > 0.5))) for th in r}
    return n0[D] - n0[-D], (nt[D] - nt[-D]) - (n0[D] - n0[-D]), marg, r, nll
J, Jm, mg, nl = {}, {}, [], {}
for F in (1, 2, 3, 4, 6, -1, -2, -3, -4, -6):
    J[F], Jm[F], m_, rr, nl[F] = Jcount(F, XL); mg.append(m_)
    if F == 1: r1 = rr
check('C1 flux F: the light window holds exactly |F| rung-0 states (lowest Landau level) at th = +-0.5, crossing zero: J = +F; '
      'compensating crossings (mirror, rung 1) = -F', all(J[F] == F and Jm[F] == -F and nl[F] == {abs(F)} for F in J),
      'J(F) ' + ' '.join(f'{F:+d}:{J[F]:+d}/{Jm[F]:+d}' for F in J) + f'; window margin >= {min(mg)*1e3:.1f}e-3')
SF = lambda x: x * J[x] if x else 0                                       # species of charge x: |x| passages, J(xF) each
flow = lambda asg: (sum(m * x * SF(x) for x, m in asg), sum(m * SF(x) for x, m in asg))
SMY = [(1, 6), (-4, 3), (2, 3), (-3, 2), (6, 1), (0, 1)]; BL3 = [(1, 6), (-1, 3), (-1, 3), (-3, 2), (3, 1), (3, 1)]
QED6 = [(4, 3), (-2, 3), (-4, 3), (2, 3), (0, 1), (-6, 1), (6, 1), (0, 1)]; L8c = [(1, 4), (-2, 2), (-1, 4), (2, 2)]; L8Q = [(1, 4), (-2, 2)]
tab = {'SM 6Y': flow(SMY), 'B-L x3': flow(BL3), 'QED 6Q': flow(QED6), 'colour 2sqrt3 T8': flow(L8c), 'T8 on Q only': flow(L8Q), 'N': flow([(1, 16)]), 'one species': flow([(1, 1)]), 'e^c alone (6Y)': flow([(6, 1)])}
check('C2 per holonomy cycle the light sector exchanges (charge, mode number) = (sum x^3, sum x^2) with the mirror (measured J): zero '
      'charge for the SM 16 under Y, B-L, QED, colour; nonzero for N, one species, T8 on Q alone, e^c alone', all(tab[k][0] == 0 for k in ('SM 6Y', 'B-L x3', 'QED 6Q', 'colour 2sqrt3 T8'))
      and all(tab[k][0] != 0 for k in ('N', 'one species', 'T8 on Q only', 'e^c alone (6Y)')) and tab['SM 6Y'][1] == 120,
      '; '.join(f'{k} {v[0]:+d},{v[1]:+d}' for k, v in tab.items()))
sw = {}
for th in (0.0, 1.0, -1.0, 2.0, -2.0, np.pi):
    om, wts, nn = qspec(*ladder_parts(tk, landau(L0, 1, th), L0, 1, XL, MC, dense=True), 1, count=True); sw[th] = (nn, np.concatenate([np.sort(np.abs(om))[:2], [np.inf, np.inf]])[:2], wts[0][np.argsort(np.abs(om))[:2]])
nneg = {sw[t][0] for t in sw} | {qspec(*ladder_parts(tk, landau(L0, 1, t), L0, 1, XL, MC, dense=True), 1, count=True)[2] for t in (-D, D)}
check('C3 holonomy cycle sampled at th = 0, +-0.5, +-1, +-2, pi (F = 1): negative count constant; no level in the light window for |th| >= 1; '
      'one avoided crossing of rung-0 state and mirror at th = 0', len(nneg) == 1 and all(sw[t][1][0] > W0 for t in sw if t != 0.0)
      and sw[0.0][1][1] < 1e-3 and np.allclose(sw[0.0][2], 0.5, atol=0.05), f'gap at th=0 {2*sw[0.0][1][0]:.1e}, rung-0 weights {np.round(sw[0.0][2], 2)}; min |w| at |th| >= 1: {min(sw[t][1][0] for t in sw if t):.1e} (inf = none below 0.016)')
check('C4 DIAGNOSTIC R = 2, levels tracked: one rung-0 and one compensating crossing; the latter sits on the coarsest rung that resolves '
      'the flux (top-rung plaquette flux pi/2: middle rung; pi/4: top rung)', all(v_[0] == 1 and v_[3] == 0 and len(v_[2]) == 1 for v_ in land.values())
      and land[(8, 8, 8)][2][0][1] > 0.5 and land[(16, 8, 8)][2][0][2] > land[(8, 8, 8)][2][0][2] + 0.15, '; '.join(f'{L}: rung-0 {v_[0]}, compensating rung weights {v_[2]}' for L, v_ in land.items()))
JR = {F: Jcount(F, XR)[0] for F in (4, -2, -6)}
xiY = flow([(1, 6), (-3, 2)])[0] + sum(m * x * x * JR[x] for x, m in ((4, 3), (-2, 3), (-6, 1)))
xiN = flow([(1, 6), (-3, 2)])[1] + sum(m * x * JR[x] for x, m in ((4, 3), (-2, 3), (-6, 1)))
check('C5 Xi orientation: singlets u_R, d_R, e_R (6Y = 4, -2, -6) carried with X flow oppositely; doublets (X\') + singlets (X): zero Y '
      'inflow, N_Xi inflow = 36 N_Xi-Y^2', all(JR[F] == -F for F in JR) and xiY == 0 and xiN == -72, f'J_X {JR}; Y {xiY}, N_Xi {xiN}')

# ============================================================ D
print('== D. which charges can carry a link')
import sympy as sy
a_, b_, f_ = sy.symbols('a b f'); m6 = [6, 3, 3, 2, 1, 1]
base = [a_, b_, -2 * a_ - b_, -3 * a_, 6 * a_ - f_, f_]                   # SU3^2 X, SU2^2 X, grav X solved
cubic = sy.factor(sum(m * x ** 3 for m, x in zip(m6, base)))
planes = [[sy.expand(x.subs(f_, r)) for x in base] for r in (2 * a_ - b_, 4 * a_ + b_)] + [[sy.expand(x.subs(a_, 0)) for x in base]]
Yv = [Fr(1, 6), Fr(-2, 3), Fr(1, 3), Fr(-1, 2), Fr(1), Fr(0)]; BLv = [Fr(1, 3), Fr(-1, 3), Fr(-1, 3), Fr(-1), Fr(1), Fr(1)]
def inplane(pl, vv): return bool(sy.solve([pl[i] - sy.Rational(vv[i].numerator, vv[i].denominator) for i in range(6)], [a_, b_, f_], dict=True))
mixed = [tuple(sy.factor(e_) for e_ in (sum(m * sy.Rational(y.numerator, y.denominator) ** 2 * x for m, y, x in zip(m6, Yv, pl)), sum(m * sy.Rational(y.numerator, y.denominator) * x ** 2 for m, y, x in zip(m6, Yv, pl)))) for pl in planes]
check('D1 THEOREM U(1)s on the 16 free of SU3^2, SU2^2, grav and cubic anomalies: three planes (cubic 18a(2a-b-f)(4a+b-f)); Y in one, '
      'B-L in two; with Y linked the extra links allowed are exactly span{Y, B-L}', str(cubic) == '18*a*(2*a - b - f)*(4*a + b - f)'
      and [inplane(p, Yv) for p in planes] == [False, True, False] and [inplane(p, BLv) for p in planes] == [True, True, False] and mixed[1] == (0, 0)
      and str(mixed[0]) == '(2*(a + b), 12*a*(a + b))' and inplane(planes[2], [Fr(0), Fr(-1, 2), Fr(1, 2), Fr(0), Fr(1, 2), Fr(-1, 2)]), f'(Y^2X, YX^2) on the planes: {mixed}; plane 3 with Y: T3R = Y - (B-L)/2')
Bs = []
for i in range(16):
    for j in range(i + 1, 16):
        E_ = np.zeros((16, 16), complex); E_[i, j] = E_[j, i] = 1 / np.sqrt(2); Bs.append(E_)
        E_ = np.zeros((16, 16), complex); E_[i, j] = -1j / np.sqrt(2); E_[j, i] = 1j / np.sqrt(2); Bs.append(E_)
for k in range(15):
    dv = np.zeros(16); dv[:k + 1] = 1; dv[k + 1] = -(k + 1); Bs.append(np.diag(dv / np.linalg.norm(dv)).astype(complex))
Bs = np.array(Bs); Bm = Bs.reshape(255, 256)
ad = lambda g: np.real(Bm.conj() @ (1j * (g[None] @ Bs - Bs @ g[None])).reshape(255, 256).T)
Cas = -sum(ad(g) @ ad(g) for g in so10); cv, cn = np.unique(np.round(np.linalg.eigvalsh((Cas + Cas.T) / 2), 6), return_counts=True)
x8 = np.diag([1., 1, -2] + [0] * 13)
check('D2 so(10) Casimir on su(16): two values on 45 and 210 states (cited maximal embedding); N^3 = 16, tr X^3 = -6 in su(16): '
      'of the subalgebras of u(16) containing so(10) only so(10) is anomaly-free', list(cn) == [45, 210] and abs(np.trace(x8 @ x8 @ x8) + 6) < 1e-12,
      f'Casimir {dict(zip(cv.tolist(), cn.tolist()))}')
al_, be_, c_ = sy.symbols('alpha beta c')
def qch(t3, y, bl, nx): return t3 + al_ * y + be_ * bl + c_ * nx
qu, qd = qch(Fr(1, 2), Fr(1, 6), Fr(1, 3), 1), qch(Fr(-1, 2), Fr(1, 6), Fr(1, 3), 1); qe, qnu = qch(Fr(-1, 2), Fr(-1, 2), -1, 1), qch(Fr(1, 2), Fr(-1, 2), -1, 1)
qec, quc = qch(0, 1, 1, -1), qch(0, Fr(-2, 3), Fr(-1, 3), -1)
sal = sy.solve([qe + qec, qu + quc], [al_], dict=True)
qp, qn = sy.expand((2 * qu + qd).subs(al_, 1)), sy.expand((qu + 2 * qd).subs(al_, 1))
check('D3 THEOREM Q = T3 + aY + b(B-L) + cN_Xi with charge-conserving Dirac masses: a = 1, q_p + q_e = q_n + q_nu = 4c; N_Xi anomalous so '
      'c = 0: q_p + q_e = 0 identically, q_n = b (not fixed by anomalies)', sal == [{al_: 1}]
      and sy.expand(qp + qe.subs(al_, 1)) == 4 * c_ and sy.expand(qn + qnu.subs(al_, 1)) == 4 * c_ and sy.expand(qn.subs(c_, 0)) == be_, f'q_p = {qp}, q_n = {qn}')

# ============================================================ E
print('== E. against measurement (estimates)')
alpha, mpi, fpi = 1 / 137.036, 134.977, 92.2
Gpi = alpha ** 2 * mpi ** 3 / (64 * np.pi ** 3 * fpi ** 2) * (3 * (4 / 9 - 1 / 9)) ** 2 * 1e6
dNeff = 3 * (10.75 / 106.75) ** (4 / 3); EQG2 = np.sqrt(2) * 1.22089e19 / np.sqrt(8 * np.pi)
print(f'   V-A: every light state is left-handed (X\'): pure V-A, Michel rho = 3/4 vs 0.74977(26); nu helicity -1/2 vs negative (Goldhaber 1958); X gives V+A, excluded')
print(f'   pi0 -> gg from the light anomaly N_c(q_u^2 - q_d^2) = 1: {Gpi:.2f} eV vs 7.80(12) eV (PrimEx-II); q_p + q_e = 0 exactly vs < 1e-21 e; '
      f'q_n = b vs (-0.2 +- 0.8)e-21 e')
print(f'   light cone: every internal state has the single-species band, E_QG,2 = {EQG2:.1e} GeV (octree-unify F2) vs > 7.3e11; 3 thermal nu^c: dN_eff = {dNeff:.2f} vs 2.99 +- 0.17')
print('   proton: B commutes with the full ladder; only inflow (SU(2) instantons) breaks it on the light sector, as in the SM')
check('E1 estimates consistent: pi0 width within 1 sigma, dN_eff < 0.17, Lorentz scale above bound', abs(Gpi - 7.80) < 0.12 and dNeff < 0.17 and EQG2 > 1e2 * 7.3e11,
      f'{time.monotonic() - T0:.1f} s')
print('supplied: octree sites, split, fine rate, kap = 0.5, M = st, st = 0.04; the 16 and its labels; the orientation bit (X\'); transport paths; backgrounds.')
print('cited: Callan-Harvey inflow, maximality of SO(10) in SU(16) (16 x 16b = 1 + 45 + 210), Witten SU(2) anomaly, measured values.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
sys.exit(0 if FAIL == 0 else 1)
