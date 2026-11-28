"""GUIDE run for row 1081 (gap-descent-sign). Refutes or guides only; discharges no proof step.
SU(2) boxes in the spin-network basis |j1 j2 j3> (triangle, integer sum).
  model 'n3' : one sheet, n = 3.   K = l_j1 l_j2 l_j3 (beta_M), D = l_j1^2 l_j3^2 (beta_L), N = 2 c(j1) + 2 c(j3)
  model '2s' : two sheets, n = 2.  K = l_j1^2 l_j3^2 (beta_M),  D = l_j1 l_j2 l_j3 (beta_L), N = c(j1)+c(j2)+c(j3)
  model 'n2' : one sheet, n = 2 (block j3 = 0). K = l_j^2, D = l_j^2, N = 2 c(j)
Face part: E^2 = exp(beta_M (X12 + X23)), X = multiplication by x = chi_{1/2}/2.
Gap m = log(lam0/lam1) of D^(1/2) K^(1/2) E^2 K^(1/2) D^(1/2).
Usage: python3 su2box.py MODEL TWOJMAX   (one BLAS thread; set by caller)
"""
import sys, math, json
import numpy as np
from scipy.special import ive
from scipy.linalg import eigh

def lf(n): return math.lgamma(n + 1)
def tri(a, b, c):  # doubled args
    return 0.5 * (lf((a+b-c)//2) + lf((a-b+c)//2) + lf((-a+b+c)//2) - lf((a+b+c)//2 + 1))
def ok(a, b, c): return (a+b+c) % 2 == 0 and abs(a-b) <= c <= a+b
def sixj(a, b, c, d, e, f):  # doubled args, Racah formula
    if not (ok(a,b,c) and ok(a,e,f) and ok(d,b,f) and ok(d,e,c)): return 0.0
    pre = tri(a,b,c) + tri(a,e,f) + tri(d,b,f) + tri(d,e,c)
    t1, t2, t3, t4 = (a+b+c)//2, (a+e+f)//2, (d+b+f)//2, (d+e+c)//2
    s1, s2, s3 = (a+b+d+e)//2, (b+c+e+f)//2, (a+c+d+f)//2
    tot = 0.0
    for z in range(max(t1,t2,t3,t4), min(s1,s2,s3)+1):
        tot += (-1)**z * math.exp(pre + lf(z+1) - lf(z-t1) - lf(z-t2) - lf(z-t3) - lf(z-t4) - lf(s1-z) - lf(s2-z) - lf(s3-z))
    return tot

def basis(J2, model):
    B = []
    for a in range(J2+1):
        for b in range(J2+1):
            for c in range(J2+1):
                if ok(a, b, c) and (model != 'n2' or c == 0): B.append((a, b, c))
    return B

def xmats(B):
    idx = {s: i for i, s in enumerate(B)}
    n = len(B)
    X12 = np.zeros((n, n)); X23 = np.zeros((n, n))
    for (a, b, c), i in idx.items():
        for da in (-1, 1):
            for db in (-1, 1):
                t = (a+da, b+db, c)
                if t in idx:
                    X12[idx[t], i] = 0.5 * math.sqrt((a+1)*(a+da+1)*(b+1)*(b+db+1)) * sixj(a, b, c, b+db, a+da, 1)**2
                t = (a, b+da, c+db)
                if t in idx:
                    X23[idx[t], i] = 0.5 * math.sqrt((c+1)*(c+db+1)*(b+1)*(b+da+1)) * sixj(c, b, a, b+da, c+db, 1)**2
    return X12, X23

def lam(j2, b):  # I_{2j+1}(b)/I_1(b)
    j2 = np.asarray(j2, dtype=float)
    return ive(j2 + 1, b) / ive(1, b)

def cas(j2):
    j2 = np.asarray(j2, dtype=float); return (j2/2) * (j2/2 + 1)

def setup(model, J2):
    B = basis(J2, model)
    X12, X23 = xmats(B)
    comm = np.abs(X12 @ X23 - X23 @ X12)
    # commutator on the interior (all 2j <= J2 - 2), where truncation does not enter
    inner = [i for i, s in enumerate(B) if max(s) <= J2 - 2]
    cin = comm[np.ix_(inner, inner)].max() if inner else 0.0
    w, U = np.linalg.eigh(X12 + X23)
    j = np.array(B)
    return B, j, w, U, cin, np.abs(X12 - X12.T).max(), np.linalg.eigvalsh(X12)[[0, -1]]

def gaps(model, j, w, U, bM, Dlist):
    E2 = (U * np.exp(bM * (w - w.max()))) @ U.T
    j1, j2, j3 = j[:, 0], j[:, 1], j[:, 2]
    if model == 'n3': K = lam(j1, bM) * lam(j2, bM) * lam(j3, bM)
    elif model == '2s': K = lam(j1, bM)**2 * lam(j3, bM)**2
    else: K = lam(j1, bM)**2
    out = []
    n = len(K)
    for D, Nd in Dlist:
        c = np.sqrt(K * D)
        M = (c[:, None] * E2) * c[None, :]
        ev, V = eigh(M, subset_by_index=[n-3, n-1])
        m = math.log(ev[2] / ev[1]); m2 = math.log(ev[2] / ev[0])
        n0 = float(V[:, 2]**2 @ Nd); n1 = float(V[:, 1]**2 @ Nd)
        out.append((m, m2, n0, n1))
    return out

def Dw(model, j, bL):
    j1, j2, j3 = j[:, 0], j[:, 1], j[:, 2]
    if bL is None: return np.ones(len(j1))
    if model == 'n3': return lam(j1, bL)**2 * lam(j3, bL)**2
    if model == '2s': return lam(j1, bL) * lam(j2, bL) * lam(j3, bL)
    return lam(j1, bL)**2

def Nop(model, j):
    j1, j2, j3 = j[:, 0], j[:, 1], j[:, 2]
    if model == 'n3': return 2*cas(j1) + 2*cas(j3)
    if model == '2s': return cas(j1) + cas(j2) + cas(j3)
    return 2*cas(j1)

if __name__ == '__main__':
    model, J2 = sys.argv[1], int(sys.argv[2])
    bMs = [float(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else [0.5, 1.0, 2.0, 2.4, 3.0, 4.0]
    B, j, w, U, cin, asym, xr = setup(model, J2)
    Nd = Nop(model, j)
    print(f"# model {model} 2Jmax {J2} dim {len(B)} interior |[X12,X23]| max {cin:.2e} asym {asym:.1e} spec(X12) [{xr[0]:.4f},{xr[1]:.4f}]")
    bLs = [0.05, 0.1, 0.2, 0.4, 0.7, 1, 1.5, 2, 2.4, 3, 4, 5, 6, 8, 10, 14, 20, 30, 50, 80, 120, 200, 400, 1000]
    ts = [0.0, 0.002, 0.005, 0.01, 0.02, 0.04, 0.07, 0.1, 0.15, 0.2, 0.3, 0.45, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0]
    res = {}
    for bM in bMs:
        Dl = [(Dw(model, j, None), Nd)] + [(Dw(model, j, bL), Nd) for bL in bLs]
        g = gaps(model, j, w, U, bM, Dl)
        minf = g[0][0]
        diffs = [x[0] - minf for x in g[1:]]
        k = int(np.argmin(diffs))
        print(f"W bM {bM:5.2f} m_inf {minf:.10f} m2_inf {g[0][1]:.6f} min_bL[m-m_inf] {diffs[k]:+.3e} at bL {bLs[k]}  last(bL=1000) {diffs[-1]:+.3e}")
        Dl = [(np.exp(-t * Nd), Nd) for t in ts]
        h = gaps(model, j, w, U, bM, Dl)
        ms = [x[0] for x in h]
        dm = np.diff(ms)
        fx = [x[3] - x[2] for x in h]
        k = int(np.argmin(dm)); k2 = int(np.argmin(fx))
        print(f"H bM {bM:5.2f} m(t=0) {ms[0]:.10f} min step dm {dm[k]:+.3e} at t {ts[k]}->{ts[k+1]}  min(n1-n0) {fx[k2]:+.4e} at t {ts[k2]}  n0(0) {h[0][2]:.4f} n1(0) {h[0][3]:.4f}")
        res[bM] = dict(minf=minf, wilson=list(zip(bLs, diffs)), heat=list(zip(ts, ms, fx)))
    json.dump(res, open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)), f"out_{model}_{J2}.json"), "w"))
