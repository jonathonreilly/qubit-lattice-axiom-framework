"""q2: decay class of the LINEAR cone-local free-boundary minimiser (linear case of (REG-min), SQ.md §0.3).
Criteria: checks/q2_criteria.md (written before this script)."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import time, itertools, resource
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import lsqr

AUDIT_TIMEOUT_SEC = 3600
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


def restrict(N, lo, hi):  # rows: positions lo..N-1-hi of a length-N axis
    idx = np.arange(lo, N - hi)
    return sp.csr_matrix((np.ones(len(idx)), (np.arange(len(idx)), idx)), shape=(len(idx), N))


def run(d, k):
    shape0 = (2, 2) + (1,) * (d - 2)
    Nf = lambda i: [s * L ** (k - i) for s in shape0]
    # link index blocks
    blocks = {}; off = 0
    for i in range(k + 1):
        N = Nf(i)
        for mu in range(d):
            sh = [N[a] - (1 if a == mu else 0) for a in range(d)]
            n = int(np.prod(sh)) if min(sh) > 0 else 0
            blocks[(i, mu)] = (off, sh, n); off += n
    nvar_total = off
    top_off = blocks[(k, 0)][0]
    nfree = top_off  # levels 0..k-1 are free; level k fixed

    def dop(i, mu, nu):
        """sparse rows: (mu,nu) plaquettes of level i in terms of all link variables (global columns)."""
        N = Nf(i)
        psh = [N[a] - (1 if a in (mu, nu) else 0) for a in range(d)]
        npl = int(np.prod(psh))
        cols = []
        # B_mu(x) - B_mu(x+e_nu)
        for (lnk, shift_dir, sign_lo, sign_hi) in ((mu, nu, 1, -1), (nu, mu, -1, 1)):
            o, sh, n = blocks[(i, lnk)]
            # for axes: restrict along shift_dir to lo (x) and hi (x+e)
            mats_lo, mats_hi = [], []
            for a in range(d):
                if a == shift_dir:
                    mats_lo.append(restrict(sh[a], 0, 1)); mats_hi.append(restrict(sh[a], 1, 0))
                else:
                    mats_lo.append(restrict(sh[a], 0, 0)); mats_hi.append(restrict(sh[a], 0, 0))
            M = sign_lo * kron_list(mats_lo) + sign_hi * kron_list(mats_hi)
            cols.append((o, M))
        R = sp.lil_matrix((npl, nvar_total)).tocsr()
        R = sp.csr_matrix((npl, nvar_total))
        for (o, M) in cols:
            M = M.tocoo()
            R = R + sp.csr_matrix((M.data, (M.row, M.col + o)), shape=(npl, nvar_total))
        return R

    def qstr(i, mu):
        Nfi, Nci = Nf(i), Nf(i + 1)
        o, sh, n = blocks[(i, mu)]
        oc, shc, nc = blocks[(i + 1, mu)]
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
        Qg = sp.csr_matrix((Q.data, (Q.row, Q.col + o)), shape=(nc, nvar_total))
        Ig = sp.csr_matrix((np.ones(nc), (np.arange(nc), np.arange(nc) + oc)), shape=(nc, nvar_total))
        return Qg - Ig

    rows = []
    for (mu, nu) in itertools.combinations(range(d), 2):
        rows.append(dop(0, mu, nu))
    for i in range(k):
        for mu in range(d):
            if blocks[(i + 1, mu)][2] > 0:
                rows.append(qstr(i, mu))
    Afull = sp.vstack(rows).tocsr()
    xtop = np.zeros(nvar_total - nfree)
    xtop[0] = 1.0  # theta = 1 on the first top link (direction 0)
    A = Afull[:, :nfree]; b = -Afull[:, nfree:] @ xtop
    sol = lsqr(A, b, atol=1e-12, btol=1e-12, iter_lim=200000)
    x = sol[0]
    g0 = np.linalg.norm(A.T @ b); g = np.linalg.norm(A.T @ (A @ x - b))
    conv = g <= 1e-8 * g0
    xall = np.r_[x, xtop]
    E = 0.5 * np.sum((Afull @ xall) ** 2)
    # curvatures and residuals per level
    prof_c, prof_r = [], []
    for i in range(k):
        mc = 0.0
        for (mu, nu) in itertools.combinations(range(d), 2):
            mc = max(mc, np.max(np.abs(dop(i, mu, nu) @ xall)))
        prof_c.append(mc * L ** (2 * (k - i)))
        mr = 0.0
        for mu in range(d):
            if blocks[(i + 1, mu)][2] > 0:
                mr = max(mr, np.max(np.abs(qstr(i, mu) @ xall)))
        prof_r.append(mr * L ** (2 * (k - 1 - i)))
    topc = np.abs((dop(k, 0, 1) @ xall)[0])
    return dict(conv=conv, g=g / g0, it=sol[2], E=E, Cc=max(prof_c), Cr=max(prof_r), pc=prof_c, pr=prof_r,
                top=topc, nvar=nfree)


res = {}
for (d, ks) in ((2, (1, 2, 3, 4, 5)), (4, (1, 2))):
    for k in ks:
        r = run(d, k); res[(d, k)] = r
        print(f"d={d} k={k} nvar={r['nvar']:7d} conv={r['conv']} relgrad={r['g']:.1e} it={r['it']:6d} "
              f"theta_check={r['top']:.3f} e=E/th^2={r['E']:.5f} C_curv={r['Cc']:.4f} C_res={r['Cr']:.4f}")
        print("    level profile curv*L^{2(k-i)}: " + " ".join(f"{v:.3f}" for v in r["pc"]) +
              " | res*L^{2(k-1-i)}: " + " ".join(f"{v:.3f}" for v in r["pr"]))
CD = {key: max(v["Cc"], v["Cr"]) for key, v in res.items()}
C1 = all(v["conv"] for v in res.values())
C2 = CD[(2, 5)] <= 1.5 * CD[(2, 3)] + 0.5 and CD[(2, 4)] <= 1.5 * CD[(2, 3)] + 0.5
C3 = all(res[(4, k)]["E"] >= 1 / 40 for k in (1, 2)) and all(res[(2, k)]["E"] > 0 for k in range(1, 6)) \
    and res[(2, 5)]["E"] >= 0.5 * res[(2, 3)]["E"]
C4 = CD[(4, 2)] <= 2 * CD[(4, 1)] + 1
print(f"C1 {'PASS' if C1 else 'FAIL'}  C2 {'PASS' if C2 else 'FAIL'}  C3 {'PASS' if C3 else 'FAIL'}  C4 {'PASS' if C4 else 'FAIL'}")
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
print(f"OVERALL: {'PASS' if (C1 and C2 and C3 and C4) else 'FAIL'}   (wall {time.time() - t0:.1f} s, peak RSS {rss:.0f} MB)")
