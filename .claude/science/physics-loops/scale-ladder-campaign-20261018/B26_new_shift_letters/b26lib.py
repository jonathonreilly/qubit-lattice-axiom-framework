"""B26 library.  Model: B20_check/chklib.py on B18_check/chk_model.py (imported read-only, not modified; same
model build as B23/B25 checks).  Adds the A2-pseudoscalar antipodal letter A0 ({c}@v -> {-c}@v, PSG-twisted
average), its conjugates, and the B23-style batched-word / gradient / DPT machinery extended to new letters."""
import os, sys
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[_v] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B20_check'))
from chklib import *            # noqa
import itertools, numpy as np
import scipy.linalg as sla

def chiA2(M):
    M = np.asarray(M); perm = [int(np.nonzero(M[i])[0][0]) for i in range(3)]
    return (-1) ** sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
CHI = [chiA2(R) for R in ROTS]
# --- A0: PSG A2-twisted average of the on-site elementary map c0 -> -c0 (real space, all rotations x translations)
c0 = CORN[0]; cm0 = frozenset(neg(x) for x in c0)
_E = np.zeros((12, 12)); _E[CI[cm0], CI[c0]] = 1.0
def _twavg(B, chis):
    O = onsite_real(B); acc = np.zeros_like(O)
    for (P, s), ch in zip(rots, chis): acc += ch * conj(O, P, s)
    acc2 = np.zeros_like(acc)
    for P, s in trans: acc2 += conj(acc, P, s)
    blk = acc2[np.ix_(loc0, loc0)]                       # site-0 block (on-site operator)
    mx = np.abs(blk).max()
    return blk / mx if mx > 1e-12 else blk
A0 = _twavg(_E, CHI).astype(complex)
A0_sym_try = _twavg(_E, [1] * 24)
def covariance(B):
    """returns (comm with all rotations, A2-covariant, translation invariant) for on-site block B"""
    O = onsite_real(B)
    comm = all(np.allclose(conj(O, P, s), O) for P, s in rots)
    a2 = all(np.allclose(conj(O, P, s), ch * O) for (P, s), ch in zip(rots, CHI))
    tr = all(np.allclose(conj(O, P, s), O) for P, s in trans)
    return comm, a2, tr
A0i = A0.conj().T
def RLt(k): return A0 @ RLk(k) @ A0i                     # A0 R_L A0^-1  (symmetric: chi^2 = 1)

# ---- batched letters (B23 conventions) + new 'Rt'
fc = np.array([FACE[c] for c in CORN], float); sig = np.real(np.diag(SKc(np.zeros(3))))
shL = np.array(list(blL.keys()), float); ML = np.array([blL[s] for s in blL]); MLt = np.array([A0 @ M @ A0i for M in ML])
PW = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
def Wb(w, ks):
    ks = np.atleast_2d(ks); N = len(ks); W = np.broadcast_to(np.eye(12, dtype=complex), (N, 12, 12)).copy()
    for L in w:
        if isinstance(L, str):
            if L in ('R', 'Rt'): W = W @ np.einsum('nt,tij->nij', np.exp(1j * ks @ shL.T), ML if L == 'R' else MLt)
            else:
                p = PW[L]; W = W * ((sig ** abs(p)) * np.exp(1j * p * ks @ fc.T))[:, None, :]
        else: W = W @ L
    return W
def letter_grad(L, k):
    if isinstance(L, str):
        if L in ('R', 'Rt'):
            MM = ML if L == 'R' else MLt
            ph = np.exp(1j * shL @ k); M = np.einsum('t,tij->ij', ph, MM)
            return M, [np.einsum('t,tij->ij', 1j * shL[:, j] * ph, MM) for j in range(3)]
        p = PW[L]; d = (sig ** abs(p)) * np.exp(1j * p * (fc @ k)); return np.diag(d), [np.diag(1j * p * fc[:, j] * d) for j in range(3)]
    return L, [np.zeros((12, 12), complex)] * 3
def W_grad(w, k):
    k = np.asarray(k, float); fs = [letter_grad(L, k) for L in w]; n = len(fs)
    pre = [np.eye(12, dtype=complex)]
    for M, _ in fs: pre.append(pre[-1] @ M)
    suf = [np.eye(12, dtype=complex)]
    for M, _ in fs[::-1]: suf.append(M @ suf[-1])
    suf = suf[::-1]
    return pre[-1], [sum(pre[i] @ fs[i][1][j] @ suf[i + 1] for i in range(n)) for j in range(3)]
RB = float(sum(np.linalg.norm(M, 2) * np.linalg.norm(t) for t, M in zip(shL, ML)))   # same for Rt (unitary conj.)
def lip_bound(w):
    return sum((RB if L in ('R', 'Rt') else abs(PW[L]) * np.sqrt(2)) for L in w if isinstance(L, str))
NSPW = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2, 'R': 0, 'Rt': 0}
def nS(w): return sum(NSPW[L] for L in w if isinstance(L, str))
def nR(w): return sum(1 for L in w if isinstance(L, str) and L in ('R', 'Rt'))

# ---- on-site palettes (B23 conventions)
def onH(a, b, unit=3): return PH[0] + np.exp(1j * np.pi * unit * a / 6) * PH[1] + np.exp(1j * np.pi * unit * b / 6) * PH[2]
def onL(a, b, c, unit=3): return PLm[0] + np.exp(1j * np.pi * unit * a / 6) * PLm[1] + np.exp(1j * np.pi * unit * b / 6) * PLm[2] + np.exp(1j * np.pi * unit * c / 6) * PLm[3]
PC = {f"H{a}{b}": onH(a, b) for a in range(4) for b in range(4)}; PC.update({f"L{a}{b}{c}": onL(a, b, c) for a in range(4) for b in range(4) for c in range(4)})

def eigsp(M, lam):
    w_, V = np.linalg.eigh(M); return V[:, np.abs(w_ - lam) < 1e-6]
Dpm = eigsp(Hon0, 2.0)
_Pd = Dpm @ Dpm.conj().T
Dp = Dpm @ eigsp(Dpm.conj().T @ Lam @ Dpm, -2 * np.sqrt(2))     # D+ : Lambda = -2sqrt2
Dm = Dpm @ eigsp(Dpm.conj().T @ Lam @ Dpm, 2 * np.sqrt(2))      # D- : Lambda = +2sqrt2
g16 = np.linspace(-np.pi, np.pi, 16, endpoint=False) + 0.0731; GRID = np.array(list(itertools.product(g16, repeat=3)))
SPEC = np.array(list(itertools.product(np.arange(-4, 4) * np.pi / 4, repeat=3)))
def dist_E(w, ks, E):
    return np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Wb(w, ks))) - E)), axis=-1)

def dpt(w, k, E, tol=1e-5):
    W0, G = W_grad(w, k)
    T, Zs = sla.schur(W0, output='complex'); ev = np.angle(np.diag(T)); dd = np.abs(wrap(ev - E))
    idx = np.where(dd < tol)[0]; m = len(idx)
    if m == 0: return None
    P = Zs[:, idx]
    h = [-1j * np.exp(-1j * E) * P.conj().T @ G[j] @ P for j in range(3)]
    h = [(x + x.conj().T) / 2 for x in h]
    return m, h, float(np.sort(dd)[m]) if m < 12 else np.inf
_rng = np.random.default_rng(7)
DIRS43 = np.vstack([np.eye(3), _rng.normal(size=(40, 3))]); DIRS43 /= np.linalg.norm(DIRS43, axis=1)[:, None]
def classify(w, k, E, vs):
    r = dpt(w, k, E)
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
def kclass(k):
    a = np.abs(np.mod(np.asarray(k) / np.pi + 1, 2) - 1); key = tuple(sorted(float(x) for x in np.round(a, 3)))
    names = {(0.5, 0.5, 0.5): 'cube', (0, 0, 0): 'Gamma', (0, 0, 1): 'X_pi', (0, 1, 1): 'M_pi', (1, 1, 1): 'R_pi', (0, 0, 0.5): 'X_r',
             (0, 0.5, 0.5): 'M_r', (0.5, 1, 1): '(1,1,1/2)pi', (0.5, 0.5, 1): '(1,1/2,1/2)pi', (0, 0.5, 1): '(0,1/2,1)pi'}
    if key in names: return names[key]
    if np.allclose(np.array(key) * 4, np.round(np.array(key) * 4), atol=1e-3): return 'pi/4:' + ','.join(str(int(round(4 * x))) for x in key)
    return 'generic'
