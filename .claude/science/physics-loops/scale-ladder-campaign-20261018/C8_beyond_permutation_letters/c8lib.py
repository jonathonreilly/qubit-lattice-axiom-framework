"""C8 library.  Model: B26_new_shift_letters/b26lib.py -> B20_check/chklib.py -> B18_check/chk_model.py (all imported
read-only, not modified).  Adds
  * real-space momentum-shift (staggering) signs D_Q, Q in pi{0,1}^3, and the doubled-cell group O x 2Z^3 on modes;
  * range-0 doubled-cell O-covariant phased permutations (sublattice blocks p_s, s in {0,1}^3);
  * the class-3 letters E+- = exp(+-i pi/4 R_L) = (1 +- i R_L)/sqrt2 (R_L^2 = 1), Et+- = exp(+-i pi/4 Rt);
  * batched words / analytic gradients / DPT node classifier for the extended token set (same conventions as b26lib)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B26_new_shift_letters'))
from b26lib import *            # noqa  (b26lib sets OMP/BLAS threads = 1)
import itertools, collections, numpy as np
import scipy.linalg as sla

SUBL = list(itertools.product((0, 1), repeat=3))
QS = [np.array(q) * np.pi for q in SUBL]                     # Q in pi{0,1}^3 (same index set as sublattices)
def vid(v, c): return C['VID'][(tuple(int(x) % L for x in v), c)]
def DQ(q):
    """real-space diag e^{iQ.x} = (-1)^{q.x}, q in {0,1}^3"""
    return np.diag([(-1.0) ** int(np.dot(q, v)) for v, c in VERTS])
EVEN = [i for i, t in enumerate(TV) if all(x % 2 == 0 for x in t)]
def G2_elements():
    """the doubled-cell group O x 2Z^3 on L=4 as (perm, sign, chiA2): mode a -> perm[a], sign sg[a]"""
    out = []
    for (Pr, sr), ch in zip(rots, CHI):
        for it in EVEN:
            Pt, st = trans[it]
            out.append((Pt[Pr], (-1.0) ** ((sr + st[Pr]) % 2), ch))
    return out
def gavg(src, tgt, twist, G):
    """group average of the elementary map |tgt><src| (twist: weight chiA2)"""
    acc = {}
    for P, sg, ch in G:
        w = (ch if twist else 1.0) * sg[tgt] * sg[src]
        key = (P[tgt], P[src]); acc[key] = acc.get(key, 0.0) + w
    return {k: v for k, v in acc.items() if abs(v) > 1e-9}
def is_partial_phased_perm(d):
    rows = collections.Counter(k[0] for k in d); cols = collections.Counter(k[1] for k in d)
    vals = np.abs(np.array(list(d.values())))
    return bool(d) and max(rows.values()) == 1 and max(cols.values()) == 1 and np.allclose(vals, vals[0])

# ---------- class-3 letters and extended batched words ----------
E_TOK = {'E+': ('R', 1), 'E-': ('R', -1), 'Et+': ('Rt', 1), 'Et-': ('Rt', -1)}
MAT_R = {'R': ML, 'Rt': MLt}
BLK = {}            # optional extra block letters: name -> (shifts (n,3), mats (n,12,12))
def _blk(name):
    if name in MAT_R: return shL, MAT_R[name]
    return BLK[name]
def Wb2(w, ks):
    ks = np.atleast_2d(ks); N = len(ks); W = np.broadcast_to(np.eye(12, dtype=complex), (N, 12, 12)).copy()
    I = np.eye(12)
    for Lt in w:
        if isinstance(Lt, str):
            if Lt in PW:
                p = PW[Lt]; W = W * ((sig ** abs(p)) * np.exp(1j * p * ks @ fc.T))[:, None, :]
            elif Lt in E_TOK:
                b, s = E_TOK[Lt]; sh, M = _blk(b)
                R = np.einsum('nt,tij->nij', np.exp(1j * ks @ sh.T), M)
                W = W @ ((I + 1j * s * R) / np.sqrt(2))
            else:
                sh, M = _blk(Lt); W = W @ np.einsum('nt,tij->nij', np.exp(1j * ks @ sh.T), M)
        else: W = W @ Lt
    return W
def letter_grad2(Lt, k):
    if isinstance(Lt, str):
        if Lt in PW:
            p = PW[Lt]; d = (sig ** abs(p)) * np.exp(1j * p * (fc @ k)); return np.diag(d), [np.diag(1j * p * fc[:, j] * d) for j in range(3)]
        if Lt in E_TOK:
            b, s = E_TOK[Lt]; sh, MM = _blk(b); ph = np.exp(1j * sh @ k); R = np.einsum('t,tij->ij', ph, MM)
            return (np.eye(12) + 1j * s * R) / np.sqrt(2), [1j * s * np.einsum('t,tij->ij', 1j * sh[:, j] * ph, MM) / np.sqrt(2) for j in range(3)]
        sh, MM = _blk(Lt); ph = np.exp(1j * sh @ k); M = np.einsum('t,tij->ij', ph, MM)
        return M, [np.einsum('t,tij->ij', 1j * sh[:, j] * ph, MM) for j in range(3)]
    return Lt, [np.zeros((12, 12), complex)] * 3
def W_grad2(w, k):
    k = np.asarray(k, float); fs = [letter_grad2(Lt, k) for Lt in w]; n = len(fs)
    pre = [np.eye(12, dtype=complex)]
    for M, _ in fs: pre.append(pre[-1] @ M)
    suf = [np.eye(12, dtype=complex)]
    for M, _ in fs[::-1]: suf.append(M @ suf[-1])
    suf = suf[::-1]
    return pre[-1], [sum(pre[i] @ fs[i][1][j] @ suf[i + 1] for i in range(n)) for j in range(3)]
NSP2 = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
def nS2(w): return sum(NSP2.get(Lt, 0) for Lt in w if isinstance(Lt, str))
def dist_E2(w, ks, E):
    return np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Wb2(w, ks))) - E)), axis=-1)
def dpt2(w, k, E, tol=1e-5):
    W0, G = W_grad2(w, k)
    T, Zs = sla.schur(W0, output='complex'); ev = np.angle(np.diag(T)); dd = np.abs(wrap(ev - E))
    idx = np.where(dd < tol)[0]; m = len(idx)
    if m == 0: return None
    P = Zs[:, idx]
    h = [-1j * np.exp(-1j * E) * P.conj().T @ G[j] @ P for j in range(3)]
    h = [(x + x.conj().T) / 2 for x in h]
    return m, h, float(np.sort(dd)[m]) if m < 12 else np.inf
def classify2(w, k, E, vs):
    r = dpt2(w, k, E)
    if r is None: return None
    m, h, nxt = r
    if m == 1: return (1, 'band', dict(slope=float(np.real(h[0][0, 0]))))
    tilt = max(abs(np.trace(x).real) / m for x in h)
    sp = np.array([np.linalg.eigvalsh(sum(d[j] * h[j] for j in range(3))) for d in DIRS43])
    a = np.abs(sp); smin, smax = float(a.min()), float(a.max())
    info = dict(tilt=tilt, smin=smin, smax=smax, next=nxt)
    if smin < 1e-6: v = 'flat'
    elif tilt > 1e-5: v = 'tilt'
    elif smax - smin > 1e-5: v = 'aniso'
    elif abs(smin - vs) > 1e-5: v = 'iso-otherspeed'
    else: v = 'ok'
    return (m, v, info)
def compressed_velocity(Xfun_grad, k, D):
    """2x2 compressed derivative h_j = -i D^+ X^-1 dX_j D for a unitary letter X at k on the 2-dim subspace D;
    returns (X restricted to D is scalar?, scalar, list h_j)"""
    X, G = Xfun_grad(k); XD = D.conj().T @ X @ D
    sc = XD[0, 0]; isscalar = np.allclose(XD, sc * np.eye(2), atol=1e-9) and np.allclose(X @ D, D @ XD, atol=1e-9)
    h = [-1j * D.conj().T @ X.conj().T @ G[j] @ D for j in range(3)]
    return isscalar, sc, h
def iso_speed(h):
    """for 2x2 Hermitian h_j: return (is v*(Pauli frame), v) -- h_j traceless, h_i h_j + h_j h_i = 2 v^2 delta_ij"""
    h = [(x + x.conj().T) / 2 for x in h]
    tr = max(abs(np.trace(x)) for x in h)
    G = np.array([[np.trace(h[i] @ h[j]).real / 2 for j in range(3)] for i in range(3)])
    v2 = np.trace(G) / 3
    return bool(tr < 1e-9 and np.allclose(G, v2 * np.eye(3), atol=1e-9)), float(np.sqrt(max(v2, 0)))
