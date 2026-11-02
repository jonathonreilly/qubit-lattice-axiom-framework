#!/usr/bin/env python3
"""Check for the E7.2 interface toy (PROOF.md, session 3): INHOMOGENEOUS Migdal-Kadanoff tree, SU(2), d = 4, b = 2.
Toy model: a hierarchical lattice. Leaves = fine plaquettes (one orientation) at positions x in {0..2^K-1}^4; the node at
depth k, position X, has the 16 children 2X + o, o in {0,1}^4. One step: bond moving within each decimation slot
(o_0, o_1): log w_slot = sum over (o_2, o_3) of the children's log weights (product of weights); decimation: the parent's
normalised character coefficients are the product over the 4 slots (convolution). Homogeneous case = c7 exactly.
Large-field REGIONS: leaves in a region R carry a strong-coupling bare weight (beta_R = 0 Haar, or 0.5), the rest the
Wilson weight at the tuned beta_K (RC: homogeneous root a_1 = a* = 0.6). Interface nodes = nodes with mixed leaves.
PRE-REGISTERED criteria (written before the first run):
  T0  empty R reproduces the homogeneous flow (1e-12).
  T1  fixed FINE-size Haar defect (a 2^4-leaf box straddling dyadic boundaries): root effect
      E_K = max_{n<=4} |a_n^root - a_n^hom| decays geometrically, per-step ratio <= 0.25 for K = 3..8.
  T2  fixed PHYSICAL region R (box with 1/16-dyadic corners, beta_R = 0.5): Cauchy differences
      D_K = max_{n<=4} |a_n^root(K+1) - a_n^root(K)| per-step ratio <= 0.25 over K = 5..8.
  T3  per-node contraction in T2 between runs K = 7 and 8: Delta(node) = max_n |a_n(node; 8) - a_n(node; 7)|; for every
      parent at depth k <= 4 with max Delta(children) > 1e-14: Delta(parent) / max Delta(children) <= 0.5, separately
      for interface parents and for exterior parents (report both maxima).
TOY ONLY: no configurations, no polymers, exactly local by construction. It tests whether the tree map contracts across
mixed (interface) nodes, nothing about 4D Wilson theory.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
import time, itertools as it, numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(n, ok, s=""):
    global NP, NF
    NP += bool(ok); NF += not ok; print(("PASS " if ok else "FAIL ") + n + (" | " + s if s else ""))
Ng, J, b, d = 1200, 160, 2, 4
x, wg = np.polynomial.legendre.leggauss(Ng); th = (x + 1) * np.pi / 2; wq = wg * np.pi / 2 * (2 / np.pi) * np.sin(th) ** 2
n = np.arange(J + 1); CH = np.sin((n[:, None] + 1) * th[None, :]) / np.sin(th)[None, :]
def coeffs(lw):
    w = np.exp(lw - lw.max()); c = CH @ (wq * w); return c / (c[0] * (n + 1))
def from_coeffs(a):
    w = (n + 1) * a @ CH; return np.log(np.maximum(w, 1e-14 * w.max()))
def hflow(lw, K):
    for _ in range(K):
        a = coeffs(4 * lw); a = a ** 4; lw = from_coeffs(a)
    return a
def tune(K, astar=0.6):
    lo, hi = np.log(0.05), np.log(5000)
    for _ in range(46):
        m = (lo + hi) / 2
        if hflow(np.exp(m) * np.cos(th), K)[1] < astar: lo = m
        else: hi = m
    return np.exp(m)
OFF = list(it.product((0, 1), repeat=4))
def run(K, box, betaR, beta):
    """box = (r0, r1) per dim in leaf units, or None. Returns root coeffs and a memo {(depth, key): coeffs}."""
    memo = {}; lwW = beta * np.cos(th); lwR = betaR * np.cos(th)
    def key(k, X):
        if box is None: return (k, "out")
        s = 2 ** (K - k); kk = []
        for i in range(4):
            lo = min(max(box[0][i] - X[i] * s, 0), s); hi = min(max(box[1][i] - X[i] * s, 0), s)
            if hi <= lo: return (k, "out")
            kk.append((lo, hi))
        return (k, tuple(kk))
    def node(k, X):
        kk = key(k, X)
        if kk in memo: return memo[kk]
        if k == K:
            lw = lwW if kk[1] == "out" else lwR; val = (lw, coeffs(lw))
        else:
            ch = {o: node(k + 1, tuple(2 * np.array(X) + np.array(o)))[0] for o in OFF}
            a = np.ones(J + 1)
            for s0, s1 in it.product((0, 1), repeat=2):
                a = a * coeffs(sum(ch[(s0, s1, o2, o3)] for o2, o3 in it.product((0, 1), repeat=2)))
            val = (from_coeffs(a), a)
        memo[kk] = val; return val
    root = node(0, (0, 0, 0, 0))[1]; return root, node, key
# T0
K = 5; beta = tune(K); r0, _, _ = run(K, None, 0.0, beta); h0 = hflow(beta * np.cos(th), K)
check("T0 empty region reproduces the homogeneous (c7) flow", np.max(np.abs(r0 - h0)) < 1e-12, f"err {np.max(np.abs(r0 - h0)):.1e}")
# T1: fixed fine-size Haar defect: leaves [2^(K-1)-1, 2^(K-1)+1)^4 (straddles every dyadic boundary at the centre)
E = []
for K in range(3, 9):
    beta = tune(K); c = 2 ** (K - 1); rt, _, _ = run(K, ((c - 1,) * 4, (c + 1,) * 4), 0.0, beta)
    E.append(np.max(np.abs(rt[1:5] - hflow(beta * np.cos(th), K)[1:5])))
rat = [E[i + 1] / E[i] for i in range(len(E) - 1)]
check("T1 fixed fine-size Haar defect: root effect decays, per-step ratio <= 0.25 (K = 3..8)", max(rat) <= 0.25,
      "E_K=" + ",".join(f"{v:.1e}" for v in E) + " ratios=" + ",".join(f"{r:.4f}" for r in rat))
# T2: fixed physical box with 1/16-dyadic corners, beta_R = 0.5
lo16 = np.array([5, 3, 1, 6]); hi16 = np.array([9, 7, 9, 11])
roots = {}; runs = {}
for K in range(5, 10):
    beta = tune(K); f = 2 ** (K - 4); rt, nd, ky = run(K, (tuple(lo16 * f), tuple(hi16 * f)), 0.5, beta); roots[K] = rt; runs[K] = (nd, ky)
Dk = [np.max(np.abs(roots[K + 1][1:5] - roots[K][1:5])) for K in range(5, 9)]
rat2 = [Dk[i + 1] / Dk[i] for i in range(len(Dk) - 1)]
check("T2 fixed physical strong-coupling region: Cauchy differences of the root decay, per-step ratio <= 0.25 (K = 5..9)",
      max(rat2) <= 0.25, "D_K=" + ",".join(f"{v:.1e}" for v in Dk) + " ratios=" + ",".join(f"{r:.4f}" for r in rat2))
print("INFO T2 root a_1 with region vs homogeneous a* = 0.6: " + ", ".join(f"K{K}:{roots[K][1]:.6f}" for K in roots))
# T3: per-node contraction between runs K = 7 and 8 (physical node = same depth and position)
(n7, k7), (n8, k8) = runs[7], runs[8]
def delta(k, X): return np.max(np.abs(n8(k, X)[1][1:5] - n7(k, X)[1][1:5]))
worst = {"interface": 0.0, "exterior": 0.0, "interior": 0.0}; cnt = {kk: 0 for kk in worst}; seen = set()
for k in range(0, 5):
    for X in it.product(range(2 ** k), repeat=4):
        sig = (k7(k, X), k8(k, X))
        if sig in seen: continue
        seen.add(sig); dc = max(delta(k + 1, tuple(2 * np.array(X) + np.array(o))) for o in OFF)
        if dc <= 1e-14: continue
        kk = k8(k, X)[1]; s = 2 ** (8 - k)
        typ = "exterior" if kk == "out" else ("interior" if all(lo == 0 and hi == s for lo, hi in kk) else "interface")
        worst[typ] = max(worst[typ], delta(k, X) / dc); cnt[typ] += 1
check("T3 per-node contraction across the interface: Delta(parent)/max Delta(children) <= 0.5 (interface and exterior parents)",
      worst["interface"] <= 0.5 and worst["exterior"] <= 0.5,
      "; ".join(f"{t}: max {worst[t]:.4f} over {cnt[t]} node classes" for t in worst))
# T3b DIAGNOSTIC (added after the first run's T3 FAIL; first run kept as c11_out_firstrun.txt). Hypothesis written
# before running: the worst interface parent has its Delta-carrying child alone (with near-Haar siblings) in one decimation
# slot, so no bond-moving power dilutes it, and the factor is ~ prod of the other three slots' a_1 = a_1(ext slot)^3,
# which -> 1 as a* -> 1 (no contraction uniform in the coupling).
def t3(astar, Ka, Kb):
    rr = {}
    for K in (Ka, Kb):
        beta = tune(K, astar); f = 2 ** (K - 4); rt, nd, ky = run(K, (tuple(lo16 * f), tuple(hi16 * f)), 0.5, beta); rr[K] = (nd, ky, beta)
    (na, ka, _), (nb, kb, bb) = rr[Ka], rr[Kb]; w = 0.0; seen = set()
    for k in range(0, 5):
        for X in it.product(range(2 ** k), repeat=4):
            sig = (ka(k, X), kb(k, X))
            if sig in seen or kb(k, X)[1] == "out": continue
            seen.add(sig); kk = kb(k, X)[1]; s = 2 ** (Kb - k)
            if all(lo == 0 and hi == s for lo, hi in kk): continue
            dl = lambda kq, Y: np.max(np.abs(nb(kq, Y)[1][1:5] - na(kq, Y)[1][1:5]))
            dc = max(dl(k + 1, tuple(2 * np.array(X) + np.array(o))) for o in OFF)
            if dc > 1e-14: w = max(w, dl(k, X) / dc)
    # predicted: exterior node at depth 4 of run Kb; its slot coefficient a_1(w^4)
    ext = nb(4, (15, 15, 15, 15)); pred = coeffs(4 * ext[0])[1] ** 3
    return w, pred
for astar in (0.6, 0.8, 0.9, 0.95):
    w, pred = t3(astar, 7, 8)
    print(f"DIAG T3b a*={astar}: worst interface ratio {w:.4f}; predicted a_1(ext slot)^3 = {pred:.4f}")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
