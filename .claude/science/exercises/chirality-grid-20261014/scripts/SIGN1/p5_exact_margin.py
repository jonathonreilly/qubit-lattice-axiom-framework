"""SIGN-1: exact-equality correction of the Kramers-class decompositions with strict sign margins.
Imports pair_kramers_u1c.py (re-runs its 4 s scan), then for saved angles solves M dg = c - M g exactly in the
rank-11 invariant 4-form space (min-norm), and reports the residual and the smallest sign margin after correction."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    import pair_kramers_u1c as pk
def P(*a): print(*a); sys.stdout.flush()
names = pk.singles + [d + ":" + c for d in pk.doubled for c in ("00", "11", "01")]
def vec(sol):
    return np.array([sol[n] for n in pk.singles] + [sol[d][i, j] for d in pk.doubled for (i, j) in ((0, 0), (1, 1), (0, 1))])
def unvec(v):
    sol = {n: v[k] for k, n in enumerate(pk.singles)}; k = len(pk.singles)
    for d in pk.doubled:
        a, c, b = v[k:k + 3]; k += 3; sol[d] = np.array([[a, b], [b, c]])
    return sol
def Mmat(cols):
    colsl = [cols[n] for n in pk.singles]
    for d in pk.doubled: colsl += [cols[d + ":s"], cols[d + ":c"], 2 * cols[d + ":sc"]]
    return -0.25 * np.array(colsl).T
M = Mmat(pk.cols); Mf = Mmat(pk.fcols)
sv = np.linalg.svd(M, compute_uv=False); P(f"singular values of the sampled constraint map: largest {sv[0]:.3e}, 11th {sv[10]:.3e}, 12th {sv[11] if len(sv) > 11 else 0:.1e}")
def margin(sol):
    m = np.inf
    for n in pk.singles:
        m = min(m, -sol[n] if pk.parity(n) == "even" else sol[n])
    for d in pk.doubled:
        mu = np.linalg.eigvalsh(sol[d]); m = min(m, (-mu).min() if pk.parity(d) == "even" else mu.min())
    return m
sols = np.load("kramers_solutions.npy", allow_pickle=True).item()
for key in sorted(sols):
    th = int(key[2:]); l1, l2 = np.cos(np.radians(th)), np.sin(np.radians(th))
    c = l1 * pk.q1 + l2 * pk.q2; cf = l1 * pk.fq1 + l2 * pk.fq2
    g = vec(sols[key]); m0 = margin(sols[key])
    dg, *_ = np.linalg.lstsq(M, c - M @ g, rcond=1e-12)
    g2 = g + dg
    r_s = np.abs(M @ g2 - c).max() / np.abs(c).max(); r_f = np.abs(Mf @ g2 - cf).max() / np.abs(cf).max()
    P(f"theta={th}: margin before {m0:.3e}; |dg|_inf {np.abs(dg).max():.2e}; after: residual (sample) {r_s:.1e}, (fresh 20000) {r_f:.1e}; "
      f"margin after {margin(unvec(g2)):.3e}")
    if th in (230, 270):
        P(f"  explicit coefficients at theta={th} (lam1={l1:+.4f}, lam2={l2:+.4f}); channel families normalised (sum over each orthonormal family of O^2):")
        sol = unvec(g2)
        for n in pk.singles: P(f"     {n:24s} {sol[n]:+.5f}   ({pk.parity(n)})")
        for d in pk.doubled: P(f"     {d:24s} [[{sol[d][0,0]:+.5f}, {sol[d][0,1]:+.5f}], [{sol[d][1,0]:+.5f}, {sol[d][1,1]:+.5f}]]   ({pk.parity(d)})  eig {np.round(np.linalg.eigvalsh(sol[d]), 5).tolist()}")
