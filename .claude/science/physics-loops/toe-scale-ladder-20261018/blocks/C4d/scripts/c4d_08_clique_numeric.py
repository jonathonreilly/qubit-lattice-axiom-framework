"""C4d-08: numerical probe (evidence only) of the k-clique walk system left open by the
single-term deduction of c4d_07 (k=3, G=T).  Imports the constraint system by executing c4d_07's
construction, keeps the surviving unknowns, adds the column-norm conditions, and minimises the
violation with a prescribed off-diagonal weight mu (and separately a COM-moving weight)."""
import sys, runpy, time
import numpy as np
import scipy.sparse as sp
from scipy.optimize import least_squares

k = int(sys.argv[1]) if len(sys.argv) > 1 else 3
sys.argv = ["c4d_07_clique_walks.py", str(k), "T"]
ns = runpy.run_path("c4d_07_clique_walks.py", run_name="c4d07")
from c4d_common import check, total
import c4d_common
c4d_common.PASS = c4d_common.FAIL = 0  # count this script's checks only
constraints, zero, allkeys, stay, classes = ns["constraints"], ns["zero"], ns["allkeys"], ns["stay"], ns["classes"]
K, Wcol = ns["K"], ns["Wcol"]
live = sorted(allkeys - zero)
idx = {kk: i for i, kk in enumerate(live)}
n = len(live)
rows, I, J, FI, FJ, C = [], [], [], [], [], []
seen = set()
nr = 0
skipped = 0
for kind, A, B, d in constraints:
    terms = []
    bad = False
    for t, c in d.items():
        if any(l[0] != "one" and l[0] in zero for l in t):
            continue
        if any(l[0] == "one" for l in t):
            bad = True; break
        terms.append((t, c))
    if bad:
        skipped += 1; continue
    if not terms:
        continue
    key = tuple(sorted(terms))
    if key in seen:
        continue
    seen.add(key)
    for (l1, l2), c in terms:
        for _ in range(c):
            rows.append(nr); I.append(idx[l1[0]]); FI.append(l1[1]); J.append(idx[l2[0]]); FJ.append(l2[1]); C.append(0)
    nr += 1
# column norms
from c4d_common import ball
norm_rows = []
for Y in classes:
    col = Wcol(Y, False)
    terms = [kk for (kk, f) in col.values() if kk not in zero]
    for kk in terms:
        rows.append(nr); I.append(idx[kk]); FI.append(True); J.append(idx[kk]); FJ.append(False)
    norm_rows.append(nr); nr += 1
rows, I, J, FI, FJ = map(np.array, (rows, I, J, FI, FJ))
const = np.zeros(nr); const[norm_rows] = -1.0
print(f"probe: n={n} unknowns, {nr} residual rows ({skipped} constraints with unknown-phase terms skipped)", flush=True)
offdiag = np.array([kk not in stay for kk in live])
def com(S):
    return np.mean(np.array(S), axis=0)
moving = np.array([not np.allclose(com(kk[1]), com(kk[0])) for kk in live])


def val(x, ii, ff):
    v = x[ii]
    return np.where(ff, np.conj(v), v)


def make(mu, mask):
    def fun(z):
        x = z[:n] + 1j * z[n:]
        v = val(x, I, FI) * val(x, J, FJ)
        r = np.zeros(nr, complex) + const
        np.add.at(r, rows, v)
        extra = 10 * (np.sum(np.abs(x[mask]) ** 2) - mu)
        return np.concatenate([r.real, r.imag, [extra]])

    def jac(z):
        x = z[:n] + 1j * z[n:]
        a, b = val(x, I, FI), val(x, J, FJ)
        # d(a*b)/d Re x_I = b * (1) ; d/d Im x_I = b * (i or -i if conj)
        sI = np.where(FI, -1j, 1j); sJ = np.where(FJ, -1j, 1j)
        rr = np.concatenate([rows] * 4); cc = np.concatenate([I, n + I, J, n + J])
        vv = np.concatenate([b, sI * b, a, sJ * a])
        Jr = sp.coo_matrix((vv.real, (rr, cc)), shape=(nr, 2 * n))
        Ji = sp.coo_matrix((vv.imag, (rr, cc)), shape=(nr, 2 * n))
        g = np.zeros(2 * n); g[:n][mask] = 20 * z[:n][mask]; g[n:][mask] = 20 * z[n:][mask]
        return sp.vstack([Jr, Ji, sp.csr_matrix(g.reshape(1, -1))]).tocsr()
    return fun, jac


rng = np.random.default_rng(11)
res = {}
for label, mask in (("offdiag", offdiag), ("moving", moving)):
    for mu in (0.0, 0.05, 0.2):
        best = None
        for trial in range(4):
            fun, jac = make(mu, mask)
            z0 = rng.normal(size=2 * n) * 0.3
            s = least_squares(fun, z0, jac=jac, method="trf", max_nfev=300, xtol=1e-15, ftol=1e-15, gtol=1e-15)
            c = float(np.sum(s.fun ** 2))
            best = c if best is None else min(best, c)
        res[(label, mu)] = best
        print(f"{label} mu={mu}: best cost {best:.3e}", flush=True)
print("RESULT", res)
check(f"k={k}: mu=0 reaches an exact solution (sanity)", res[("offdiag", 0.0)] < 1e-10)
for label in ("offdiag", "moving"):
    print(f"{label}: cost/mu^2 = {res[(label,0.05)]/0.05**2:.3g} (mu=0.05), {res[(label,0.2)]/0.2**2:.3g} (mu=0.2)")
total()
