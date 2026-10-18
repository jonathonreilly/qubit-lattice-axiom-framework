"""B23 shared definitions: Dirac (4-fold D+ (+) D-) k* level screen.
Model: B20_check/chklib.py (built on B18_check/chk_model.py); independent of b20lib/b18lib/walklib.
Adds: batched words, analytic letter gradients, degenerate perturbation theory (DPT) for m-fold nodes,
family generators matching B20's screen_words.py palettes (global phase of each factor fixed by putting
phase 1 on the first projector; a different projector ordering only changes global phases, i.e. shifts E)."""
import os, sys
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[_v] = "1"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B20_check'))
from chklib import *            # noqa
import itertools, numpy as np
import scipy.linalg as sla
from scipy.optimize import minimize

fc = np.array([FACE[c] for c in CORN], float); sig = np.real(np.diag(SKc(np.zeros(3))))
shL = np.array(list(blL.keys()), float); ML = np.array([blL[s] for s in blL])
PW = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
def Wb(w, ks):
    ks = np.atleast_2d(ks); N = len(ks); W = np.broadcast_to(np.eye(12, dtype=complex), (N, 12, 12)).copy()
    for L in w:
        if isinstance(L, str):
            if L == 'R': W = W @ np.einsum('nt,tij->nij', np.exp(1j * ks @ shL.T), ML)
            else:
                p = PW[L]; W = W * ((sig ** abs(p)) * np.exp(1j * p * ks @ fc.T))[:, None, :]
        else: W = W @ L
    return W
def letter_grad(L, k):
    if isinstance(L, str):
        if L == 'R':
            ph = np.exp(1j * shL @ k); M = np.einsum('t,tij->ij', ph, ML)
            return M, [np.einsum('t,tij->ij', 1j * shL[:, j] * ph, ML) for j in range(3)]
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
def lip_bound(w):
    """Rigorous bound on sup_k ||d/dk_u W(k)|| over unit u: sum over k-letters of sup ||u.grad letter||.
    S^p: diagonal, |p| max_c |u.f_c| <= |p| sqrt2.  R: bounded by sum_t ||M_t|| |u.t| <= sum_t ||M_t|| |t| (computed)."""
    Rb = float(sum(np.linalg.norm(M, 2) * np.linalg.norm(t) for t, M in zip(shL, ML)))
    return sum((Rb if L == 'R' else abs(PW[L]) * np.sqrt(2)) for L in w if isinstance(L, str))

# ---- palettes
def onH(a, b, unit=3): return PH[0] + np.exp(1j * np.pi * unit * a / 6) * PH[1] + np.exp(1j * np.pi * unit * b / 6) * PH[2]
def onL(a, b, c, unit=3): return PLm[0] + np.exp(1j * np.pi * unit * a / 6) * PLm[1] + np.exp(1j * np.pi * unit * b / 6) * PLm[2] + np.exp(1j * np.pi * unit * c / 6) * PLm[3]
PC = {f"H{a}{b}": onH(a, b) for a in range(4) for b in range(4)}; PC.update({f"L{a}{b}{c}": onL(a, b, c) for a in range(4) for b in range(4) for c in range(4)})
PHL = dict(PC); PHL.update({f"{h}*{l}": PC[h] @ PC[l] for h in PC if h[0] == 'H' for l in PC if l[0] == 'L'})
P6 = {f"H{a}.{b}": onH(a, b, 1) for a in range(12) for b in range(12)}; P6.update({f"L{a}.{b}.{c}": onL(a, b, c, 1) for a in range(12) for b in range(12) for c in range(12)})
def p6_is_cliff(n): return all(int(x) % 3 == 0 for x in n[1:].split('.'))
L202 = onL(2, 0, 2)
ALL = {**PHL, **P6, 'L202': L202}
SKEL1 = [('S', 'o'), ('S', 'R', 'o'), ('S', 'o', 'R'), ('S2', 'o'), ('S', 'S', 'R', 'o'), ('S', 'R', 'S', 'o'), ('S', 'R', 'Si', 'o'), ('S', 'R', 'S', 'R', 'o')]
SKEL2 = [('S', 'o', 'S', 'o'), ('S', 'o', 'Si', 'o'), ('S', 'o', 'R', 'o'), ('S', 'R', 'o', 'R', 'o'), ('S2', 'o', 'S2', 'o'), ('S2', 'o', 'S2i', 'o'),
         ('S', 'R', 'o', 'S', 'R', 'o'), ('S', 'R', 'o', 'Si', 'R', 'o'), ('S', 'o', 'S', 'R', 'o'), ('S', 'o', 'Si', 'R', 'o'), ('S', 'R', 'o', 'S', 'o')]
SKPI6 = [('S', 'o'), ('S', 'R', 'o'), ('S', 'o', 'R'), ('S2', 'o')]
SKTASTE = [('S', 'o', 'S', 'o'), ('S2', 'o', 'S2', 'o')]
def jobs(tag):
    """cliff2:i,j  -> SKEL2[i] x PC x PC ; pi6 -> SKPI6 x P6 (all, incl. Clifford-phase entries);
       taste_pi6 -> SKTASTE x (P6 minus Clifford entries) x L202  (the PHL part was screened by B20_check/chk5)."""
    if tag.startswith('cliff2'):
        sel = [SKEL2[int(i)] for i in tag.split(':')[1].split(',')]
        for sk in sel:
            for n1 in PC:
                for n2 in PC: yield sk, (n1, n2)
    elif tag == 'pi6':
        for sk in SKPI6:
            for n in P6: yield sk, (n,)
    elif tag == 'taste_pi6':
        for sk in SKTASTE:
            for n in P6:
                if not p6_is_cliff(n): yield sk, (n, 'L202')
def build(sk, names):
    it = iter(names); return [ALL[next(it)] if L == 'o' else L for L in sk]

def eigsp(M, lam):
    w_, V = np.linalg.eigh(M); return V[:, np.abs(w_ - lam) < 1e-6]
Dpm = eigsp(Hon0, 2.0)
g16 = np.linspace(-np.pi, np.pi, 16, endpoint=False) + 0.0731; GRID = np.array(list(itertools.product(g16, repeat=3)))
SPEC = np.array(list(itertools.product(np.arange(-4, 4) * np.pi / 4, repeat=3)))      # (pi/4)Z^3 in the BZ: 512 points
def dist_E(w, ks, E):
    return np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Wb(w, ks))) - E)), axis=-1)
def chord_E(w, ks, E):
    return np.min(np.abs(np.linalg.eigvals(Wb(w, ks)) - np.exp(1j * E)), axis=-1)

# ---- DPT classification of a node at k (approximate), level E
def dpt(w, k, E, tol=1e-5):
    W0, G = W_grad(w, k)
    T, Z = sla.schur(W0, output='complex'); ev = np.angle(np.diag(T)); dd = np.abs(wrap(ev - E))
    idx = np.where(dd < tol)[0]; m = len(idx)
    if m == 0: return None
    P = Z[:, idx]
    h = [-1j * np.exp(-1j * E) * P.conj().T @ G[j] @ P for j in range(3)]
    h = [(x + x.conj().T) / 2 for x in h]
    return m, h, float(np.sort(dd)[m]) if m < 12 else np.inf
_rng = np.random.default_rng(7)
DIRS = np.vstack([np.eye(3), _rng.normal(size=(40, 3))]); DIRS /= np.linalg.norm(DIRS, axis=1)[:, None]
def classify(w, k, E, vs):
    """Return (m, verdict, info).  verdict 'ok' = isotropic untilted linear cone(s) at speed vs:
    every directional DPT spectrum is +-vs with equal multiplicities (equivalently {h_i,h_j} = 2 vs^2 delta_ij, tr h_j = 0)."""
    r = dpt(w, k, E)
    if r is None: return None
    m, h, nxt = r
    if m == 1: return (1, 'band', dict(slope=float(np.real(h[0][0, 0]))))
    tilt = max(abs(np.trace(x).real) / m for x in h)
    sp = np.array([np.linalg.eigvalsh(sum(d[j] * h[j] for j in range(3))) for d in DIRS])
    a = np.abs(sp); smin, smax = float(a.min()), float(a.max())
    anti = max(np.linalg.norm(h[i] @ h[j] + h[j] @ h[i] - (2 * vs ** 2 if i == j else 0) * np.eye(m)) for i in range(3) for j in range(3))
    info = dict(tilt=tilt, smin=smin, smax=smax, anti=anti, next=nxt)
    if smin < 1e-6: v = 'flat'
    elif tilt > 1e-5: v = 'tilt'
    elif smax - smin > 1e-5: v = 'aniso'
    elif abs(smin - vs) > 1e-5: v = 'iso-otherspeed'
    else: v = 'ok'
    return (m, v, info)
def kclass(k):
    a = np.abs(np.mod(np.asarray(k) / np.pi + 1, 2) - 1); a = np.round(a, 3); key = tuple(sorted(a))
    names = {(0.5, 0.5, 0.5): 'cube(+-k*,doublers)', (0, 0, 0): 'Gamma', (0, 0, 1): 'X_pi', (0, 1, 1): 'M_pi', (1, 1, 1): 'R_pi', (0, 0, 0.5): 'X_r(pi/2 e_i)',
             (0, 0.5, 0.5): 'M_r(pi/2(1,1,0))', (0, 0.25, 0.25): '(pi/4)(1,1,0)', (0, 0, 0.25): '(pi/4)e_i', (0.25, 0.25, 0.25): '(pi/4)(1,1,1)'}
    return names.get(key, 'other' if not np.allclose(a * 4, np.round(a * 4), atol=1e-3) else 'piZ/4:' + str(key))
