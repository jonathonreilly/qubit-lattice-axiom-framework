#!/usr/bin/env python3
"""B20 check 5 (scope probe): the B20 screen keeps only EXACTLY 2-fold k* levels.  A 4-fold k* level D+ + D-
(possible whenever the two doublet eigenvalues coincide) is, by the L1 argument plus the E1/2 x T1 selection
rule, an isotropic untilted Dirac point: two cones of one speed |n_S| sqrt2/3 and opposite chirality, net 0.
Such levels evade L2/L3's chirality obstruction.  This runner screens the cliff1 skeletons (B20's SKEL1 x PHL
palette, rebuilt in the checker's model) and the S^2 taste skeleton for them: r(k) sign test on 16^3, then a
node census of the survivors.  Prints PASS/FAIL and candidate lists."""
import time, collections
from chklib import *
from scipy.optimize import minimize
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
fc = np.array([FACE[c] for c in CORN], float); sig = np.real(np.diag(SKc(np.zeros(3))))
shL = np.array(list(blL.keys()), float); ML = np.array([blL[s] for s in blL])
def Wb(w, ks):
    N = len(ks); W = np.broadcast_to(np.eye(12, dtype=complex), (N, 12, 12)).copy()
    for L in w:
        if isinstance(L, str):
            if L == 'R': W = W @ np.einsum('nt,tij->nij', np.exp(1j * ks @ shL.T), ML)
            else:
                p = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}[L]; W = W * ((sig ** abs(p)) * np.exp(1j * p * ks @ fc.T))[:, None, :]
        else: W = W @ L
    return W
_k = np.array([[0.3, -0.7, 1.1]]); assert np.allclose(Wb(['S', 'R', UH, 'S2i', UL], _k)[0], Wword(['S', 'R', UH, 'S2i', UL], _k[0]))
def onH(a, b): return PH[0] + 1j ** a * PH[1] + 1j ** b * PH[2]
def onL(a, b, c): return PLm[0] + 1j ** a * PLm[1] + 1j ** b * PLm[2] + 1j ** c * PLm[3]
PC = {f"H{a}{b}": onH(a, b) for a in range(4) for b in range(4)}; PC.update({f"L{a}{b}{c}": onL(a, b, c) for a in range(4) for b in range(4) for c in range(4)})
PHL = dict(PC); PHL.update({f"{h}*{l}": PC[h] @ PC[l] for h in PC if h[0] == 'H' for l in PC if l[0] == 'L'})
SKEL1 = [('S', 'o'), ('S', 'R', 'o'), ('S', 'o', 'R'), ('S2', 'o'), ('S', 'S', 'R', 'o'), ('S', 'R', 'S', 'o'), ('S', 'R', 'Si', 'o'), ('S', 'R', 'S', 'R', 'o')]
jobs = [(sk, (n,)) for sk in SKEL1 for n in PHL]
L202 = onL(2, 0, 2)
jobs += [(('S2', 'o', 'S2', 'o'), (n, 'L202')) for n in PHL]
jobs += [(('S', 'o', 'S', 'o'), (n, 'L202')) for n in PHL]
PHL['L202'] = L202
def build(sk, names):
    it = iter(names); return [PHL[next(it)] if L == 'o' else L for L in sk]
Dproj = None
def eigsp(M, lam):
    w_, V = np.linalg.eigh(M); return V[:, np.abs(w_ - lam) < 1e-6]
Dpm = eigsp(Hon0, 2.0)      # = D+ + D-  (the H_on = 2 space is exactly D+ + D-)
check("H_on = 2 eigenspace is 4-dim and equals D+ + D- (Lambda = -+2sqrt2 on it)", Dpm.shape[1] == 4 and np.allclose(np.sort(np.linalg.eigvalsh(Dpm.conj().T @ Lam @ Dpm)), [-2 * np.sqrt(2)] * 2 + [2 * np.sqrt(2)] * 2))
g = np.linspace(-np.pi, np.pi, 16, endpoint=False) + 0.0731; GRID = np.array(list(itertools.product(g, repeat=3)))
cands = []; stats = collections.Counter()
for sk, names in jobs:
    w = build(sk, names); ns = nS(w)
    if ns == 0: continue
    W0 = Wword(w, kst); e, V = np.linalg.eig(W0)
    for E, m in levels(W0):
        if m != 4: continue
        Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
        if abs(np.linalg.norm(Q.conj().T @ Dpm) ** 2 - 4) > 1e-6: stats['G3/2 4-fold'] += 1; continue
        stats['D+D- 4-fold'] += 1
        Ws = Wb(w, GRID); c0 = np.linalg.det(Wword(w, np.zeros(3)))
        r = np.linalg.det(Ws - np.exp(1j * E) * np.eye(12)) / (np.exp(6j * E) * np.sqrt(c0))
        if r.real.max() > 0 and r.real.min() < 0: stats['fermi'] += 1; continue
        d = np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Ws)) - E)), axis=-1)
        cands.append((sk, names, E, ns, float(d.min())))
print("  4-fold k* level statistics:", dict(stats), f"[{time.time() - t0:.0f}s]")
print(f"  {len(cands)} Dirac-level (word, E) pairs without an r sign change")
# census of survivors: nodes in the BZ, FD classification
def classify(w, k, E):
    W = Wword(w, k); e = eigph(W); dd = np.sort(np.abs(wrap(e - E))); mult = int(np.sum(dd < 1e-6))
    if mult == 0: return None
    dirs, sp = fd_speeds(w, k, E, m=mult, h=1e-6, ndir=30)
    sl = np.array([np.sort(a) / 1e-6 for a, _ in sp])
    return mult, float(np.abs(sl).min()), float(np.abs(sl).max()), float(np.abs(sl.sum(1)).max() / mult)
seen = set(); results = []
for sk, names, E, ns, dmin in cands:
    w = build(sk, names); vs = abs(ns) * np.sqrt(2) / 3
    f = lambda k: float(np.min(np.abs(wrap(eigph(Wword(w, np.asarray(k))) - E))))
    Ws = Wb(w, GRID); d = np.min(np.abs(wrap(np.angle(np.linalg.eigvals(Ws)) - E)), axis=-1)
    special = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)] + [np.pi * np.array(v) for v in itertools.product((0, 1), repeat=3)] \
              + [np.pi / 2 * np.array(v) for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1))] + [np.pi / 4 * np.array(v) for v in ((1, 0, 0), (1, 1, 0), (1, 1, 1))]
    starts = [GRID[i] for i in np.argsort(d)[:25]]
    nodes = []
    for k0 in special:
        if f(k0) < 1e-7: nodes.append(k0)
    for k0 in starts:
        r_ = minimize(f, k0, method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-12, 'maxiter': 2500})
        if r_.fun < 1e-7: nodes.append(r_.x)
    bad = []
    for k in nodes:
        c = classify(w, k, E)
        if c is None: continue
        mult, smin, smax, tilt = c
        if mult == 1: bad.append(('band', tuple(np.round(k / np.pi, 3)))); break
        if abs(smin - vs) > 1e-4 or abs(smax - vs) > 1e-4 or tilt > 1e-4: bad.append((mult, tuple(np.round(k / np.pi, 3)), round(smin / vs, 3), round(smax / vs, 3)))
    results.append((sk, names, round(E, 4), ns, len(nodes), bad[:2]))
nclean = [x for x in results if not x[5]]
for x in results[:30]: print("   ", x)
print(f"  {len(nclean)} survivors with every found node isotropic at the Dirac speed (screen level)")
for x in nclean[:20]: print("   CLEAN-AT-SCREEN:", x)
check("bookkeeping: Dirac 4-fold k* levels exist in the parameter-free families and were outside B20's screen", stats['D+D- 4-fold'] > 0, f"{stats['D+D- 4-fold']} levels")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
