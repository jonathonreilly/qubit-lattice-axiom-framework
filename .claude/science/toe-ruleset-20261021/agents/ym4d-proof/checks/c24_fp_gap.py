"""c24: gap of the legitimate soft-step gauge fixing on H_0 (criteria: checks/c24_criteria.md, written first).

Coarse units, eps = 1/n. O_D = d*d + dd* + a Q^T Q and O_FP = d*d + d P_res d* + a Q^T Q on H_0 = {h = 0}, a = 1.
H_0 is imposed by a large penalty on the row-normalised h; dense generalised eigenproblems (eigenvalues only).
"""
import itertools
import resource
import time

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp

T0 = time.time()
A_COEF = 1.0


def axial(a, b, order):
    out = []; z = list(a)
    for c in order:
        while z[c] != b[c]:
            if b[c] > z[c]:
                out.append((tuple(z), c, 1)); z[c] += 1
            else:
                w = list(z); w[c] -= 1; out.append((tuple(w), c, -1)); z[c] -= 1
    return out


def run(d, T, n):
    eps = 1.0 / n; N = n * T; NS = N ** d; NE = d * NS; hn = (n - 1) // 2
    sid = lambda x: int(np.ravel_multi_index(tuple(c % N for c in x), (N,) * d))
    lid = lambda x, mu: mu * NS + sid(x)
    sites = list(itertools.product(range(N), repeat=d))
    cr, cc, cv = [], [], []; dr, dc, dv = [], [], []
    r = 0
    for x in sites:
        for (mu, nu) in itertools.combinations(range(d), 2):
            xm = list(x); xm[mu] += 1; xn = list(x); xn[nu] += 1
            for (l_, s_) in ((lid(x, mu), 1), (lid(xm, nu), 1), (lid(xn, mu), -1), (lid(x, nu), -1)):
                cr.append(r); cc.append(l_); cv.append(s_)
            r += 1
        s = sid(x)
        for mu in range(d):
            w = list(x); w[mu] -= 1
            dr += [s, s]; dc += [lid(x, mu), lid(w, mu)]; dv += [1.0, -1.0]
    Cm = sp.csr_matrix((cv, (cr, cc)), shape=(r, NE))
    Gd = sp.csr_matrix((dv, (dr, dc)), shape=(NS, NE))
    coarse = list(itertools.product(range(T), repeat=d))
    orders = list(itertools.permutations(range(d)))
    qr_, qc, qv = [], [], []; hr, hc, hv = [], [], []
    wQ = 1.0 / (len(orders) * n ** d)
    for Xi, X in enumerate(coarse):
        cX = [n * X[i] + hn for i in range(d)]
        for sig in orders:
            for off in itertools.product(range(-hn, hn + 1), repeat=d):
                y = [cX[i] + off[i] for i in range(d)]
                for (z, c, s_) in axial(cX, y, sig):
                    hr.append(Xi); hc.append(lid(z, c)); hv.append(s_ * eps * wQ)
                for mu in range(d):
                    cY = list(cX); cY[mu] += n
                    yL = list(y); yL[mu] += n
                    seq = axial(cX, y, sig) + [(tuple(y[i] + (j if i == mu else 0) for i in range(d)), mu, 1)
                                               for j in range(n)]
                    seq += [(z, c, -s_) for (z, c, s_) in reversed(axial(cY, yL, sig))]
                    for (z, c, s_) in seq:
                        qr_.append(mu * len(coarse) + Xi); qc.append(lid(z, c)); qv.append(s_ * eps * wQ)
    Q = sp.csr_matrix((qv, (qr_, qc)), shape=(d * len(coarse), NE))
    H = sp.csr_matrix((hv, (hr, hc)), shape=(len(coarse), NE)).toarray()
    Uperp = np.zeros((NS, 2 * len(coarse)))
    for Xi, X in enumerate(coarse):
        cX = [n * X[i] + hn for i in range(d)]
        Uperp[sid(cX), Xi] = 1.0
        for off in itertools.product(range(-hn, hn + 1), repeat=d):
            Uperp[sid([cX[i] + off[i] for i in range(d)]), len(coarse) + Xi] = 1.0
    Uo, _ = np.linalg.qr(Uperp)
    sc = eps ** (d - 2) / eps ** d
    S_curl = (Cm.T @ Cm).tocoo(); S_div = (Gd.T @ Gd).tocoo(); S_Q = (Q.T @ Q).tocoo()
    GU = np.asarray(Gd.T @ Uo) * np.sqrt(sc)
    Hn = H / np.linalg.norm(H, axis=1, keepdims=True)
    dmax = 0.0
    for S_, f_ in ((S_curl, sc), (S_div, sc), (S_Q, A_COEF / eps ** d)):
        dd = np.zeros(NE); np.add.at(dd, S_.row[S_.row == S_.col], f_ * S_.data[S_.row == S_.col]); dmax += dd.max()
    t = 1e7 * dmax
    out = {}
    B = 512
    for name in ("D", "FP"):
        Kx = np.zeros((NE, NE))
        for S_, f_ in ((S_curl, sc), (S_div, sc), (S_Q, A_COEF / eps ** d)):
            np.add.at(Kx, (S_.row, S_.col), f_ * S_.data)
        for i0 in range(0, NE, B):
            Kx[i0:i0 + B] += t * (Hn[:, i0:i0 + B].T @ Hn)
            if name == "FP":
                Kx[i0:i0 + B] -= GU[i0:i0 + B] @ GU.T
        out[name] = sla.eigh(Kx, eigvals_only=True, overwrite_a=True, subset_by_index=[0, 3], driver="evr")
        del Kx
    return out, NE, len(coarse)


rows = []
v1 = True; q1 = True
for (d, T, ns) in ((2, 4, (3, 5, 7, 9)), (3, 3, (3, 5)), (4, 2, (3,))):
    for n in ns:
        tt = time.time()
        out, NE, Nc = run(d, T, n)
        lD, lF = float(out["D"][0]), float(out["FP"][0])
        v1 &= lD >= 0.2 - 1e-9; q1 &= lF > 1e-8
        rows.append((d, n, lD, lF))
        print(f"d={d} T={T} n={n}: {NE} links, {Nc} blocks; lambda_min(O_D on H_0) = {lD:.5f}, "
              f"lambda_min(O_FP on H_0) = {lF:.5f}, ratio {lF / lD:.4f}  ({time.time() - tt:.0f} s, "
              f"RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.0f} MB)", flush=True)
print(f"V1 lambda_min(O_D) >= 1/5 at every size: {'PASS' if v1 else 'FAIL'}")
print(f"Q1 lambda_min(O_FP) > 1e-8 at every size: {'PASS' if q1 else 'FAIL'}")
print(f"c24: {'VALID' if v1 else 'INVALID'}; time {time.time() - T0:.0f} s, "
      f"peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.0f} MB")
