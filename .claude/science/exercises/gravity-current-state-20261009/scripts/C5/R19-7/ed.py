"""R19-7 ED engine: H(v,bU) = sum_m [-t X^{p_m} + v exp(-bU Delta_m/2)] on the trivial coset (move span) of a torus.
Matrix-free in F2-coefficient coordinates: each move is an XOR mask on the state index."""
import numpy as np, sys, numba as nb
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tcommon import *
from mc import channel_pols, cvec, OFFS
from scipy.sparse.linalg import eigsh, LinearOperator

class Model:
    def __init__(s, T):
        s.T = T; V = T.V; s.V = V
        G = T.G(); P = T.P() % 2
        s.n_identity = int((P.sum(1) == 0).sum())
        P = P[P.sum(1) > 0]; s.P = P
        B = f2_basis(P); d = B.shape[0]; s.d = d; s.N = 2**d
        piv = [int(np.nonzero(B[r])[0][0]) for r in range(d)]
        masks = []
        for p in P:
            c = np.array([p[pv] for pv in piv], dtype=np.int64)
            assert np.array_equal((c @ B) % 2, p % 2)       # p is in the span with these coefficients
            masks.append(int(sum(int(c[r]) << r for r in range(d))))
        s.masks = np.array(masks, dtype=np.int64)
        ns = 6*V; assert ns <= 63
        Bpk = np.array([int(sum(int(B[r, j]) << j for j in range(ns))) for r in range(d)], dtype=np.uint64)
        n = np.zeros(s.N, dtype=np.uint64)
        for r in range(d):
            n[2**r:2**(r+1)] = n[:2**r] ^ Bpk[r]
        s.npk = n
        E = np.zeros(s.N); s.bits_cache = None
        CH = 1 << 16
        Gt = G.T.astype(np.float64)
        for a in range(0, s.N, CH):
            bits = ((n[a:a+CH, None] >> np.arange(ns, dtype=np.uint64)) & np.uint64(1)).astype(np.float64)
            Gn = bits @ Gt
            assert np.all(np.mod(Gn, 2) == 0)
            E[a:a+CH] = ((Gn/2)**2).sum(1)
        s.E = E
        idx = np.arange(s.N, dtype=np.int64)
        s.dE = np.array([E[idx ^ m] - E for m in s.masks], dtype=np.float32)   # (M, N)
        s.maxabsdE = float(np.abs(s.dE).max())
    def Dsum(s, bU):
        return np.exp(-bU*s.dE.astype(np.float64)/2).sum(0)
    def bits(s, a, b):
        return ((s.npk[a:b, None] >> np.arange(6*s.V, dtype=np.uint64)) & np.uint64(1)).astype(np.float64)
    def Ovec(s, kvec, eps):
        """O_k(c) = V^-1/2 sum_s c_s e^{-ik.pos_s}(n_s - 1/2), slot index t*V + site"""
        T = s.T; V = s.V; c = cvec(eps); w = np.zeros(6*V, complex)
        for x in T.sites():
            si = T.sidx(x)
            for t in range(6):
                w[t*V + si] = c[t]*np.exp(-1j*np.dot(kvec, np.array(x) + OFFS[t]))
        out = np.zeros(s.N, complex); CH = 1 << 16
        for a in range(0, s.N, CH):
            out[a:a+CH] = (s.bits(a, a+CH) - 0.5) @ w
        return out/np.sqrt(V)

@nb.njit(cache=True)
def _mv(x, Hd, masks, t, out):
    N = x.shape[0]
    for c in range(N):
        acc = Hd[c]*x[c]
        for m in range(masks.shape[0]):
            acc -= t*x[c ^ masks[m]]
        out[c] = acc
    return out

def make_op(mod, v, bU, t=1.0):
    Hd = v*mod.Dsum(bU)
    def mv(x):
        x = np.ascontiguousarray(x, dtype=np.float64).ravel(); out = np.empty_like(x)
        return _mv(x, Hd, mod.masks, t, out)
    return Hd, mv

def dense_H(mod, v, bU, t=1.0):
    N = mod.N; Hd = v*mod.Dsum(bU); H = np.diag(Hd).astype(float)
    idx = np.arange(N)
    for m in mod.masks:
        H[idx ^ m, idx] += -t
    return H

def ground(mod, v, bU, t=1.0, dense_max=4096):
    if mod.N <= dense_max:
        H = dense_H(mod, v, bU, t); w, U = np.linalg.eigh(H)
        return w[0], U[:, 0]*np.sign(U[:, 0].sum()), w[:6], (w, U)
    Hd, mv = make_op(mod, v, bU, t)
    op = LinearOperator((mod.N, mod.N), matvec=mv, dtype=np.float64)
    import os
    kk = int(os.environ.get('R197_K', '4')); tl = float(os.environ.get('R197_TOL', '1e-11'))
    w, U = eigsh(op, k=kk, which='SA', tol=tl, maxiter=20000, ncv=max(20, 4*kk+8))
    o = np.argsort(w); w = w[o]; U = U[:, o]
    g = U[:, 0]*np.sign(U[:, 0].sum())
    return w[0], g, w, None

def lanczos_poles(mv, phi, M, reorth=True):
    nrm = np.linalg.norm(phi)
    if nrm < 1e-14: return np.array([]), np.array([])
    q = phi/nrm; Q = [q] if reorth else None; al = []; be = []; qprev = np.zeros_like(q); b = 0.0
    for j in range(M):
        w = mv(q); a = np.dot(q, w); w = w - a*q - b*qprev
        if reorth:
            for qq in Q: w -= np.dot(qq, w)*qq
            for qq in Q: w -= np.dot(qq, w)*qq
        al.append(a); b = np.linalg.norm(w)
        if b < 1e-10 or j == M-1: break
        be.append(b); qprev = q; q = w/b
        if reorth: Q.append(q)
    Tm = np.diag(al) + np.diag(be[:len(al)-1], 1) + np.diag(be[:len(al)-1], -1)
    th, S = np.linalg.eigh(Tm)
    return th, nrm**2*S[0, :]**2

def spectral(mod, v, bU, kvec, eps, E0, g, dense=None, M=80, t=1.0):
    O = mod.Ovec(np.array(kvec, float), eps); phi = O*g
    phi = phi - np.vdot(g, phi)*g
    if dense is not None:
        w, U = dense
        amp = U.T @ phi; wt = np.abs(amp)**2; om = w - E0
        return om, wt
    Hd, mv = make_op(mod, v, bU, t)
    reorth = mod.N <= 2**17
    oms = []; wts = []
    for part in (phi.real, phi.imag):
        part = part - np.dot(g, part)*g
        th, wt = lanczos_poles(mv, part, M, reorth=reorth)
        oms.append(th - E0); wts.append(wt)
    return np.concatenate(oms), np.concatenate(wts)

def diagnose(om, wt, tol_main=0.10):
    """merge poles; return S, SMA first moment, main pole (>=10% weight), lowest pole (>=1e-6 S), decay rates"""
    S = wt.sum()
    if S < 1e-12: return dict(S=0.0)
    o = np.argsort(om); om = om[o]; wt = wt[o]
    mo = []; mw = []
    for a, b in zip(om, wt):
        if mo and abs(a - mo[-1]) < 1e-7*max(1, abs(a)): mw[-1] += b
        else: mo.append(a); mw.append(b)
    mo = np.array(mo); mw = np.array(mw)
    keep = mw > 1e-6*S
    sma = (mo*mw).sum()/S
    main = mo[np.argmax(mw >= tol_main*S)]
    dom = mo[np.argmax(mw)]
    low = mo[keep].min()
    def rate(tau):
        C = (mw*np.exp(-np.clip(mo, 0, None)*tau)).sum(); C2 = (mw*np.exp(-np.clip(mo, 0, None)*(tau*1.01))).sum()
        return -np.log(C2/C)/(0.01*tau)
    return dict(S=S, sma=sma, main=main, dom=dom, domw=mw.max()/S, low=low, r2=rate(2/max(sma, 1e-9)), r20=rate(20/max(sma, 1e-9)))
