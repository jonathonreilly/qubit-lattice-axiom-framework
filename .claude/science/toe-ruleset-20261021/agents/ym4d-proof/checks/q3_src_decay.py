"""q3: weighted-sup response of the LINEAR cone-local free-boundary minimiser to sources of unit weighted size
(SQ.md §T2 target Q3). Criteria: checks/q3_criteria.md (written before this script)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import time, itertools, resource
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import lsqr

AUDIT_TIMEOUT_SEC = 1200
t0 = time.time()
L = 3


def T(n, u):
    u = np.asarray(u)
    out = np.minimum(u + 1, 2 * n - 1 - u)
    out[(u < 0) | (u > 2 * n - 2)] = 0
    return out


def kron_list(ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kron(out, m, format="csr")
    return sp.csr_matrix(out)


def restrict(N, lo, hi):
    idx = np.arange(lo, N - hi)
    return sp.csr_matrix((np.ones(len(idx)), (np.arange(len(idx)), idx)), shape=(len(idx), N))


class Chain:
    def __init__(self, d, k):
        self.d, self.k = d, k
        self.shape0 = (2, 2) + (1,) * (d - 2)
        self.blocks = {}
        off = 0
        for i in range(k + 1):
            N = self.Nf(i)
            for mu in range(d):
                sh = [N[a] - (1 if a == mu else 0) for a in range(d)]
                n = int(np.prod(sh)) if min(sh) > 0 else 0
                self.blocks[(i, mu)] = (off, sh, n); off += n
        self.nvar = off
        self.nfree = self.blocks[(k, 0)][0]
        # rows: level-0 plaquettes (combinations order), then residuals (i, mu)
        self.rowblocks = {}; rows = []; roff = 0
        for (mu, nu) in itertools.combinations(range(d), 2):
            R = self.dop(0, mu, nu); rows.append(R)
            self.rowblocks[("p", mu, nu)] = (roff, R.shape[0]); roff += R.shape[0]
        for i in range(k):
            for mu in range(d):
                if self.blocks[(i + 1, mu)][2] > 0:
                    R = self.qstr(i, mu); rows.append(R)
                    self.rowblocks[("r", i, mu)] = (roff, R.shape[0]); roff += R.shape[0]
        self.nrows = roff
        self.Afull = sp.vstack(rows).tocsr()
        self.A = self.Afull[:, :self.nfree]

    def Nf(self, i):
        return [s * L ** (self.k - i) for s in self.shape0]

    def dop(self, i, mu, nu):
        d = self.d; N = self.Nf(i)
        psh = [N[a] - (1 if a in (mu, nu) else 0) for a in range(d)]
        npl = int(np.prod(psh))
        R = sp.csr_matrix((npl, self.nvar))
        for (lnk, shift_dir, s_lo, s_hi) in ((mu, nu, 1, -1), (nu, mu, -1, 1)):
            o, sh, n = self.blocks[(i, lnk)]
            ml, mh = [], []
            for a in range(d):
                if a == shift_dir:
                    ml.append(restrict(sh[a], 0, 1)); mh.append(restrict(sh[a], 1, 0))
                else:
                    ml.append(restrict(sh[a], 0, 0)); mh.append(restrict(sh[a], 0, 0))
            M = (s_lo * kron_list(ml) + s_hi * kron_list(mh)).tocoo()
            R = R + sp.csr_matrix((M.data, (M.row, M.col + o)), shape=(npl, self.nvar))
        return R

    def qstr(self, i, mu):
        d = self.d; Nfi, Nci = self.Nf(i), self.Nf(i + 1)
        o, sh, n = self.blocks[(i, mu)]
        oc, shc, nc = self.blocks[(i + 1, mu)]
        mats = []
        for a in range(d):
            if a == mu:
                Mx = np.zeros((Nci[a] - 1, Nfi[a] - 1))
                for X in range(Nci[a] - 1):
                    Mx[X] = T(L, np.arange(Nfi[a] - 1) - L * X) / L
            else:
                Mx = np.zeros((Nci[a], Nfi[a]))
                for X in range(Nci[a]):
                    Mx[X, L * X:L * X + L] = 1.0 / L
            mats.append(sp.csr_matrix(Mx))
        Q = kron_list(mats).tocoo()
        Qg = sp.csr_matrix((Q.data, (Q.row, Q.col + o)), shape=(nc, self.nvar))
        Ig = sp.csr_matrix((np.ones(nc), (np.arange(nc), np.arange(nc) + oc)), shape=(nc, self.nvar))
        return Qg - Ig

    def centre_base(self, j):
        m = L ** (self.k - j)
        return [(m - 1) // 2] * self.d  # in-plane base and transverse middle sites

    def vortex_rows(self, i, amp):
        """source vector entries (row index -> value) for the CCW circulation on the links of p*_{i+1}."""
        j = i + 1; x = self.centre_base(j); out = {}
        e = lambda a: [1 if b == a else 0 for b in range(self.d)]
        add = lambda u, v: [p + q for p, q in zip(u, v)]
        for (mu, base, sgn) in ((0, x, 1), (1, add(x, e(0)), 1), (0, add(x, e(1)), -1), (1, x, -1)):
            ro, nr = self.rowblocks[("r", i, mu)]
            sh = self.blocks[(j, mu)][1]
            out[ro + np.ravel_multi_index(tuple(base), tuple(sh))] = sgn * amp
        return out

    def solve(self, src):
        b = -src  # rows are A x + src
        sol = lsqr(self.A, b, atol=1e-12, btol=1e-12, iter_lim=400000)
        x = sol[0]
        g0 = np.linalg.norm(self.A.T @ b); g = np.linalg.norm(self.A.T @ (self.A @ x - b))
        conv = bool(g <= 1e-8 * g0) if g0 > 0 else True
        xall = np.r_[x, np.zeros(self.nvar - self.nfree)]
        meas = self.Afull @ xall + src
        k, d = self.k, self.d
        prof_c, prof_r = [], []
        for i in range(k):
            if i == 0:
                mc = max(np.max(np.abs(meas[ro:ro + nr])) for key, (ro, nr) in self.rowblocks.items() if key[0] == "p")
            else:
                mc = max(np.max(np.abs(self.dop(i, mu, nu) @ xall)) for (mu, nu) in itertools.combinations(range(d), 2))
            prof_c.append(mc * L ** (2 * (k - i)))
            mr = max(np.max(np.abs(meas[ro:ro + nr])) for key, (ro, nr) in self.rowblocks.items()
                     if key[0] == "r" and key[1] == i)
            prof_r.append(mr * L ** (2 * (k - 1 - i)))
        ro, nr = self.rowblocks[("p", 0, 1)]
        N = self.Nf(0); psh = [N[a] - (1 if a in (0, 1) else 0) for a in range(d)]
        ctr = meas[ro + np.ravel_multi_index(tuple(self.centre_base(0)), tuple(psh))] * L ** (2 * k)
        return dict(conv=conv, g=(g / g0 if g0 > 0 else 0.0), it=sol[2], pc=prof_c, pr=prof_r, N0=prof_c[0],
                    Nall=max(prof_c + prof_r), ctr=abs(ctr), E=0.5 * float(meas @ meas))

    def plaq_source(self, kind):
        d, k = self.d, self.k; n = L ** k
        src = np.zeros(self.nrows)
        ro, nr = self.rowblocks[("p", 0, 1)]
        N = self.Nf(0); psh = [N[a] - (1 if a in (0, 1) else 0) for a in range(d)]
        idx = np.indices(psh).reshape(d, -1).T.astype(float)
        cen = idx.copy(); cen[:, 0] += 0.5; cen[:, 1] += 0.5
        Xs = np.array([n / 2, n / 2] + [(n - 1) / 2] * (d - 2))
        y = cen - Xs
        P2 = 3 * y[:, 2] ** 2 - np.sum(y ** 2, axis=1)
        if kind == "B":
            vals = np.sign(P2) * L ** (-2 * k); sigma = 1.0
        else:
            vals = P2 / n ** 2 * L ** (-2 * k); sigma = np.max(np.abs(vals)) * L ** (2 * k)
        src[ro:ro + nr] = vals
        return src, sigma


def fmt(r):
    return (f"conv={r['conv']} relgrad={r['g']:.1e} it={r['it']:6d} Nall={r['Nall']:.4f} N0={r['N0']:.4f} "
            f"Rctr={r['ctr']:.4f} E={r['E']:.4e}\n      curv*L^2(k-i): " + " ".join(f"{v:.3f}" for v in r["pc"]) +
            " | res*L^2(k-1-i): " + " ".join(f"{v:.3f}" for v in r["pr"]))


res = {}
allconv = True
for (d, ks) in ((2, (1, 2, 3, 4, 5)), (3, (1, 2, 3)), (4, (1, 2))):
    for k in ks:
        ch = Chain(d, k)
        print(f"=== d={d} k={k} nfree={ch.nfree} rows={ch.nrows}  (t={time.time() - t0:.1f}s)", flush=True)
        src = np.zeros(ch.nrows)
        for i in range(k):
            for key, v in ch.vortex_rows(i, L ** (-2 * (k - 1 - i))).items():
                src[key] += v
        r = ch.solve(src); res[("A", d, k)] = r; allconv &= r["conv"]
        print("  A  all levels : " + fmt(r), flush=True)
        if d <= 3:
            for l in range(k):
                s1 = np.zeros(ch.nrows)
                for key, v in ch.vortex_rows(l, L ** (-2 * (k - 1 - l))).items():
                    s1[key] += v
                r1 = ch.solve(s1); allconv &= r1["conv"]
                print(f"  A1 level {l} only: Nall={r1['Nall']:.4f} N0={r1['N0']:.4f} Rctr={r1['ctr']:.4f} conv={r1['conv']}")
            rng = np.random.default_rng(3)
            s2 = np.zeros(ch.nrows)
            for i in range(k):
                for mu in range(d):
                    key = ("r", i, mu)
                    if key in ch.rowblocks:
                        ro, nr = ch.rowblocks[key]
                        s2[ro:ro + nr] = rng.choice([-1.0, 1.0], size=nr) * L ** (-2 * (k - 1 - i))
            r2 = ch.solve(s2); allconv &= r2["conv"]; res[("A2", d, k)] = r2
            print(f"  A2 random signs: Nall={r2['Nall']:.4f} N0={r2['N0']:.4f} Rctr={r2['ctr']:.4f} conv={r2['conv']}")
        if d == 3:
            for kind in ("B", "C"):
                sB, sig = ch.plaq_source(kind)
                rB = ch.solve(sB); allconv &= rB["conv"]
                for key in ("Nall", "N0", "ctr"):
                    rB[key] /= sig
                res[(kind, d, k)] = rB
                print(f"  {kind} (sigma={sig:.4f}) : " + fmt(rB), flush=True)
        del ch

A = lambda d, k, q: res[("A", d, k)][q]
QA = (A(2, 5, "N0") <= 1.10 * A(2, 3, "N0") + 0.05 and A(2, 5, "Nall") <= 1.10 * A(2, 3, "Nall") + 0.05 and
      A(3, 3, "N0") <= 1.10 * A(3, 2, "N0") + 0.05 and A(3, 3, "Nall") <= 1.10 * A(3, 2, "Nall") + 0.05)
RB = lambda k: res[("B", 3, k)]["ctr"]
QB = RB(3) >= 1.10 * RB(2) and RB(3) - RB(2) >= 0.05
QC = res[("C", 3, 3)]["N0"] <= 1.10 * res[("C", 3, 2)]["N0"] + 0.05
print("SUMMARY  A: d=2 N0 " + " ".join(f"{A(2, k, 'N0'):.4f}" for k in range(1, 6)) +
      " | Nall " + " ".join(f"{A(2, k, 'Nall'):.4f}" for k in range(1, 6)))
print("         A: d=3 N0 " + " ".join(f"{A(3, k, 'N0'):.4f}" for k in range(1, 4)) +
      " | Nall " + " ".join(f"{A(3, k, 'Nall'):.4f}" for k in range(1, 4)) +
      " ; d=4 N0 " + " ".join(f"{A(4, k, 'N0'):.4f}" for k in (1, 2)) + " | Nall " +
      " ".join(f"{A(4, k, 'Nall'):.4f}" for k in (1, 2)))
print("         B: Rctr " + " ".join(f"{RB(k):.4f}" for k in (1, 2, 3)) + " | N0 " +
      " ".join(f"{res[('B', 3, k)]['N0']:.4f}" for k in (1, 2, 3)))
print("         C: N0 " + " ".join(f"{res[('C', 3, k)]['N0']:.4f}" for k in (1, 2, 3)) + " | Rctr " +
      " ".join(f"{res[('C', 3, k)]['ctr']:.4f}" for k in (1, 2, 3)))
print(f"Q1 {'PASS' if allconv else 'FAIL'}  QA {'PASS' if QA else 'FAIL'}  QB {'PASS' if QB else 'FAIL'}  "
      f"QC {'PASS' if QC else 'FAIL'}")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print(f"OVERALL: {'PASS' if (allconv and QA and QB and QC) else 'FAIL'}   (wall {time.time() - t0:.1f} s, peak RSS {rss:.0f} MB)")
