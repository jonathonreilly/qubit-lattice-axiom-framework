#!/usr/bin/env python3
"""Check c15 (PROOF.md, session 4): MECHANISM of the slow interface contraction in the c11 inhomogeneous MK tree.
Hypothesis H (formulated after a scratch diagnostic of the c11 node classes, written here BEFORE this script's first run):
at an interface node, a decimation slot whose 4 children are j small-field (Wilson-flowed) children and 4-j strong-coupling
(near-Haar, log w ~ 0) children performs bond moving with power j instead of b^{d-2} = 4. The node is then a step of an MK
map of effective dimension d_eff = 2 + log_2 j. Leading-order heuristic (c7 rate argument with p = j): the irrelevant
deviation contracts by b^2 / j^3 (j = 4: 1/16, j = 2: 1/2, j = 3: 0.15, j = 1: no re-expansion; exact slot map is identity,
then a^4: factor ~ 4 a_n^3 > 1 possible).
PRE-REGISTERED criteria:
  H1  synthetic parent with 4 slots of (j small-field children = the c11 exterior depth-4 node, 4-j exact Haar children):
      Delta ratio for j = 2 equals the c11 T3 'IIEE' interface class value (computed here from the same runs) to 1e-3, and
      for j = 4 equals the c11 exterior class value to 1e-3.
  H2  the synthetic ratios are ordered r(1) > r(2) > r(3) > r(4), and r(2) in [0.35, 0.7], r(4) in [0.04, 0.1].
  H3  coupling-flatness: each r(j) varies by less than 25% between a* = 0.6 and a* = 0.9.
  H4  PREDICTION (not used to build H): a small-field box inside a strong-coupling sea (region R = complement of the c11 box)
      creates j = 1 slots at the box corners, and the worst per-node interface ratio there is >= 1 (no per-node contraction).
  H5  in the H4 geometry the per-node ratio at the worst node is reproduced by the synthetic j-model within 20% using that
      node's own slot composition (diagnostic of mechanism, reported).
  H6  COMPOUNDING (REVIEW_S3 point 6; written before the first run): half-space strong region x_c < 1/3 (non-dyadic, so
      interface nodes exist at EVERY depth), boundary normal to a bond-moving coordinate (c = 2). Perturb the bare log
      weight of one leaf layer by eps * chi_2 (adjoint character; P2) either in the first small-field layer next to the
      boundary ("interface layer") or in a layer at x_c = 2/3 ("bulk layer"). Root responses R_K at fixed K (no K-shift
      confound). Prediction: R_K(interface)/R_K(bulk) increases monotonically over K = 6..10 (slower interface
      contraction compounds).
  H7  in the same setting R_K(interface) still decays: R_{K+1}/R_K < 1 for K = 6..9.
  H6' (added AFTER the first run, whose H6 FAILED: there the root response of both layers decays like the layer volume,
      2^-K, i.e. it is dominated by the marginal (coupling) component, which the toy averages): remove the component of
      the root response along the tangent of the one-parameter tuned family (d root / d beta of the small-field leaves)
      and compare the residual (irrelevant) responses. Criterion: residual ratio interface/bulk increases monotonically
      over K = 6..10.
  INFO: the same for the boundary normal to a decimation coordinate (c = 0), and for P1 = eps * cos(theta).
TOY ONLY. It identifies the mechanism of the c11 T3 number; it says nothing directly about 4D Wilson theory.
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
def run2(K, box, betaR, beta, complement=False):
    """As run(); complement=True puts the strong-coupling weight OUTSIDE the box (small-field box in a strong sea)."""
    memo = {}; lwW = beta * np.cos(th); lwR = betaR * np.cos(th)
    def key(k, X):
        s = 2 ** (K - k); kk = []
        for i in range(4):
            lo = min(max(box[0][i] - X[i] * s, 0), s); hi = min(max(box[1][i] - X[i] * s, 0), s)
            if hi <= lo: return (k, "out")
            kk.append((lo, hi))
        return (k, tuple(kk))
    def isin(kk, s):  # fraction type: "out" (no box leaves), "full" (all box leaves), else mixed
        if kk[1] == "out": return "out"
        return "full" if all(lo == 0 and hi == s for lo, hi in kk[1]) else "mixed"
    def node(k, X):
        kk = key(k, X)
        if kk in memo: return memo[kk]
        if k == K:
            inbox = kk[1] != "out"; strong = (not inbox) if complement else inbox
            lw = lwR if strong else lwW; val = (lw, coeffs(lw))
        else:
            ch = {o: node(k + 1, tuple(2 * np.array(X) + np.array(o)))[0] for o in OFF}
            a = np.ones(J + 1)
            for s0, s1 in it.product((0, 1), repeat=2):
                a = a * coeffs(sum(ch[(s0, s1, o2, o3)] for o2, o3 in it.product((0, 1), repeat=2)))
            val = (from_coeffs(a), a)
        memo[kk] = val; return val
    def typ(k, X):  # small-field (S), strong (R), interface (F)
        t = isin(key(k, X), 2 ** (K - k))
        if t == "mixed": return "F"
        inbox = t == "full"; strong = (not inbox) if complement else inbox
        return "R" if strong else "S"
    return node, key, typ
lo16 = np.array([5, 3, 1, 6]); hi16 = np.array([9, 7, 9, 11])
def pair(astar, complement):
    out = []
    for K in (7, 8):
        beta = tune(K, astar); f = 2 ** (K - 4); out.append(run2(K, (tuple(lo16 * f), tuple(hi16 * f)), 0.5, beta, complement))
    return out
def node_ratios(pr):
    (na, ka, ta), (nb, kb, tb) = pr; dl = lambda k, Y: np.max(np.abs(nb(k, Y)[1][1:5] - na(k, Y)[1][1:5]))
    res = {}; seen = set()
    for k in range(0, 5):
        for X in it.product(range(2 ** k), repeat=4):
            sig = (ka(k, X), kb(k, X))
            if sig in seen: continue
            seen.add(sig); t = tb(k, X)
            chs = [tuple(2 * np.array(X) + np.array(o)) for o in OFF]; dc = max(dl(k + 1, c) for c in chs)
            if dc <= 1e-14: continue
            comp = tuple("".join(tb(k + 1, tuple(2 * np.array(X) + np.array((s0, s1, o2, o3)))) for o2, o3 in it.product((0, 1), repeat=2))
                         for s0, s1 in it.product((0, 1), repeat=2))
            res[(k, X)] = (t, dl(k, X) / dc, comp)
    return res
def synth(pr, js, ref=(4, (15, 15, 15, 15))):
    """Parent with slot s holding js[s] copies of a small-field depth-4 node (runs 7, 8) and 4 - js[s] exact Haar children."""
    (na, _, _), (nb, _, _) = pr; e7, e8 = na(*ref), nb(*ref); dch = np.max(np.abs(e8[1][1:5] - e7[1][1:5]))
    par = lambda e: np.prod([coeffs(j * e[0]) for j in js], axis=0)
    return np.max(np.abs(par(e8)[1:5] - par(e7)[1:5])) / dch
R = {}
for astar in (0.6, 0.9):
    pr = pair(astar, False); nr = node_ratios(pr); R[astar] = [synth(pr, (j,) * 4) for j in (1, 2, 3, 4)]
    if astar == 0.6:
        iiee = [v[1] for v in nr.values() if v[0] == "F" and all(sorted(c) == sorted("RRSS") for c in v[2])]
        ext = [v[1] for v in nr.values() if v[0] == "S"]
        h1 = (len(iiee) > 0 and abs(max(iiee) - R[astar][1]) < 1e-3 and abs(max(ext) - R[astar][3]) < 1e-3)
        check("H1 synthetic j-model reproduces the c11 interface (RRSS slots) and exterior class ratios",
              h1, f"c11 RRSS class {max(iiee) if iiee else float('nan'):.4f} vs j=2 {R[astar][1]:.4f}; exterior {max(ext):.4f} vs j=4 {R[astar][3]:.4f}")
for astar in R: print(f"INFO a*={astar}: synthetic ratios r(j=1..4) = " + ", ".join(f"{v:.4f}" for v in R[astar]) + "; leading-order 4/j^3 = 4, 0.5, 0.148, 0.0625")
r = R[0.6]
check("H2 ordering r(1) > r(2) > r(3) > r(4), r(2) in [0.35, 0.7], r(4) in [0.04, 0.1]",
      r[0] > r[1] > r[2] > r[3] and 0.35 <= r[1] <= 0.7 and 0.04 <= r[3] <= 0.1)
var = [abs(R[0.9][i] - R[0.6][i]) / R[0.6][i] for i in range(4)]
check("H3 coupling-flatness: |r_0.9(j) - r_0.6(j)| / r_0.6(j) < 0.25 for every j", max(var) < 0.25, "rel. changes " + ", ".join(f"{v:.3f}" for v in var))
pr = pair(0.6, True); nr = node_ratios(pr)
fi = {k: v for k, v in nr.items() if v[0] == "F"}
wk = max(fi, key=lambda k: fi[k][1]); wv = fi[wk]
check("H4 PREDICTION: small-field box in a strong sea: worst per-node interface ratio >= 1", wv[1] >= 1,
      f"worst {wv[1]:.4f} at depth {wk[0]}, slots {wv[2]}; {len(fi)} interface classes")
js = [c.count("S") for c in wv[2]]; nF = sum(c.count("F") for c in wv[2])
# [first-run bug, fixed after run 1; first output kept as c15_out_firstrun.txt] the reference child must be a SMALL-FIELD
# depth-4 node of THIS geometry; run 1 used (15,15,15,15), which is strong in the complement geometry (synthetic = 0).
refS = next((4, Y) for Y in it.product(range(16), repeat=4) if pr[1][2](4, Y) == "S")
sy = synth(pr, js, ref=refS) if nF == 0 and min(js) > 0 else float("nan")
check("H5 the worst node is reproduced by the synthetic j-model with its own slot counts (within 20%)",
      np.isfinite(sy) and abs(sy - wv[1]) / wv[1] < 0.2, f"slot small-field counts {js}, interface children {nF}, synthetic {sy:.4f}")

def half_space(K, beta, c, phi, layer, eps, g, betaR=0.5):
    """Leaves with x_c < floor(phi 2^K) strong (betaR); leaf layer x_c == layer gets + eps*g. Nodes depend only on (k, X_c)."""
    cut = int(np.floor(phi * 2 ** K)); memo = {}
    def leaf(xc):
        lw = (betaR if xc < cut else beta) * np.cos(th)
        return lw + eps * g if xc == layer else lw
    def node(k, xc):
        if (k, xc) in memo: return memo[(k, xc)]
        if k == K: lw = leaf(xc); val = (lw, coeffs(lw))
        else:
            a = np.ones(J + 1)
            for s0, s1 in it.product((0, 1), repeat=2):
                tot = 0
                for o2, o3 in it.product((0, 1), repeat=2):
                    o = (s0, s1, o2, o3); tot = tot + node(k + 1, 2 * xc + o[c])[0]
                a = a * coeffs(tot)
            val = (from_coeffs(a), a)
        memo[(k, xc)] = val; return val
    return node(0, 0)[1]
chi2 = 4 * np.cos(th) ** 2 - 1; eps = 1e-4
def responses(c, g, Ks=range(6, 11)):
    out = []
    for K in Ks:
        beta = tune(K); base = half_space(K, beta, c, 1 / 3, -1, 0.0, g)
        cut = int(np.floor(2 ** K / 3)); lay_i, lay_b = cut, int(np.floor(2 * 2 ** K / 3))
        ri = np.max(np.abs(half_space(K, beta, c, 1 / 3, lay_i, eps, g)[1:5] - base[1:5]))
        rb = np.max(np.abs(half_space(K, beta, c, 1 / 3, lay_b, eps, g)[1:5] - base[1:5]))
        out.append((K, ri, rb))
    return out
res = responses(2, chi2)
q = [ri / rb for _, ri, rb in res]
check("H6 compounding: R_K(interface)/R_K(bulk) increases monotonically over K = 6..10 (P2, boundary normal to c = 2)",
      all(q[i + 1] > q[i] for i in range(len(q) - 1)), "ratios " + ", ".join(f"K{K}:{v:.3g}" for (K, _, _), v in zip(res, q)))
ri = [r[1] for r in res]; st = [ri[i + 1] / ri[i] for i in range(len(ri) - 1)]
check("H7 interface-layer response still decays: R_{K+1}/R_K < 1 (K = 6..9)", max(st) < 1,
      "R_K(int)=" + ",".join(f"{v:.2e}" for v in ri) + " steps " + ",".join(f"{v:.3f}" for v in st)
      + " | bulk steps " + ",".join(f"{res[i + 1][2] / res[i][2]:.3f}" for i in range(len(res) - 1)))

def resid(K, c, g, layer):
    beta = tune(K); base = half_space(K, beta, c, 1 / 3, -1, 0.0, g)[1:5]; h = 1e-4 * beta
    tang = (half_space(K, beta + h, c, 1 / 3, -1, 0.0, g)[1:5] - half_space(K, beta - h, c, 1 / 3, -1, 0.0, g)[1:5]) / (2 * h)
    dv = half_space(K, beta, c, 1 / 3, layer, eps, g)[1:5] - base; tn = tang / np.linalg.norm(tang)
    return np.linalg.norm(dv - (dv @ tn) * tn), np.linalg.norm(dv)
rq = []; rint = []; rbulk = []
for K in range(6, 11):
    cut = int(np.floor(2 ** K / 3)); ri_, _ = resid(K, 2, chi2, cut); rb_, _ = resid(K, 2, chi2, int(np.floor(2 * 2 ** K / 3)))
    rq.append(ri_ / rb_); rint.append(ri_); rbulk.append(rb_)
check("H6' irrelevant (tangent-removed) residual: interface/bulk ratio increases monotonically over K = 6..10",
      all(rq[i + 1] > rq[i] for i in range(len(rq) - 1)), "ratios " + ", ".join(f"{v:.3g}" for v in rq)
      + " | int steps " + ",".join(f"{rint[i + 1] / rint[i]:.3f}" for i in range(4)) + " | bulk steps " + ",".join(f"{rbulk[i + 1] / rbulk[i]:.3f}" for i in range(4)))
for c, g, nm in ((0, chi2, "P2, c=0"), (2, np.cos(th), "P1, c=2"), (0, np.cos(th), "P1, c=0")):
    rr = responses(c, g)
    print(f"INFO {nm}: R(int) steps " + ",".join(f"{rr[i + 1][1] / rr[i][1]:.3f}" for i in range(len(rr) - 1))
          + "; R(bulk) steps " + ",".join(f"{rr[i + 1][2] / rr[i][2]:.3f}" for i in range(len(rr) - 1))
          + f"; int/bulk at K=10: {rr[-1][1] / rr[-1][2]:.3g}")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
