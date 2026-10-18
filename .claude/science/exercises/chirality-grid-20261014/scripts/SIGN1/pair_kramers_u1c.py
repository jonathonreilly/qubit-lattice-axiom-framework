"""SIGN-1 follow-up A: Kramers-class pair SDP (see ../PREREG.md follow-up A).  Families in kramers_fams.py."""
import numpy as np, sys, time, resource
sys.path.insert(0, __file__.rsplit("/", 1)[0])
t0 = time.time()
from kramers_fams import *
import cvxpy as cp
def mem(): return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2**20
rng = np.random.default_rng(91)
# samples and 4-forms
n = 64; S = 3000
quads = np.array(sorted({tuple(sorted(rng.choice(n, 4, replace=False))) for _ in range(S + 400)}))[:S]
Kb = vertex_B()
q1 = sum(alt_s(-Kb[a].conj(), Kb[a], quads) for a in range(10)).real
q2 = sum(2 * alt_s(Kb[a], Kb[a], quads).real for a in range(10))
for R, nm, anti in ((O1, "T1", True), (OU, "U", False)):
    Kt = [R.T @ Kk @ R for Kk in Kb]
    if anti: Kt = [Kk.conj() for Kk in Kt]
    q1t = sum(alt_s(-Kt[a].conj(), Kt[a], quads) for a in range(10)).real
    q2t = sum(2 * alt_s(Kt[a], Kt[a], quads).real for a in range(10))
    P(f"Q invariant under {nm}: {np.allclose(q1t, q1) and np.allclose(q2t, q2)}")

cols = {}; kinds = []
for nm, ms in famo.items():
    cols[nm] = sum(alt_s(a, a, quads) for a in ms)
for d in doubled:
    cols[d + ":sc"] = sum(alt_s(a, b, quads) for a, b in zip(famo[d + ":s"], famo[d + ":c"]))
Mall = np.array([cols[k] for k in cols]).T * (-0.25)
for nm_, qq in (("q1", q1), ("q2", q2)):
    g, *_ = np.linalg.lstsq(Mall, qq, rcond=None)
    P(f"unconstrained fit of {nm_}: relative residual {np.linalg.norm(Mall @ g - qq) / np.linalg.norm(qq):.2e}")
P(f"rank of channel 4-forms on sample: {np.linalg.matrix_rank(Mall, tol=1e-9)}")

def solve(l1, l2, verbose=False):
    c = l1 * q1 + l2 * q2
    gs = {nm: cp.Variable() for nm in singles}
    Gd = {d: cp.Variable((2, 2), symmetric=True) for d in doubled}
    cons = []
    expr = 0
    for nm in singles:
        cons.append(gs[nm] <= 0 if parity(nm) == "even" else gs[nm] >= 0)
        expr = expr + gs[nm] * cols[nm]
    for d in doubled:
        assert parity(d + ":s") == parity(d + ":c")
        cons.append(Gd[d] << 0 if parity(d + ":s") == "even" else Gd[d] >> 0)
        expr = expr + Gd[d][0, 0] * cols[d + ":s"] + Gd[d][1, 1] * cols[d + ":c"] + 2 * Gd[d][0, 1] * cols[d + ":sc"]
    res = -0.25 * expr - c
    prob = cp.Problem(cp.Minimize(cp.norm1(res)), cons)
    prob.solve(solver="CLARABEL")
    val = prob.value / np.abs(c).sum()
    sol = {nm: float(gs[nm].value) for nm in singles}; sol.update({d: np.array(Gd[d].value) for d in doubled})
    return val, sol, prob.status

P("\nangle  lam1   lam2   min L1 residual/|q|_1 (Kramers class with U(1)_c)   status")
rows = []
for th in sorted(set(np.arange(0, 360, 10.0)) | set(np.arange(176, 194, 2.0)) | set(np.arange(262, 290, 2.0))):
    l1, l2 = np.cos(np.radians(th)), np.sin(np.radians(th))
    val, sol, st = solve(l1, l2)
    rows.append((th, val, sol))
    P(f" {th:5.0f} {l1:+.3f} {l2:+.3f}   {val:.3e}   {st}" + ("   FEASIBLE" if val < 1e-7 else ""))
feas = [r for r in rows if r[1] < 1e-7]
P(f"feasible angles: {[r[0] for r in feas]}")
for th, val, sol in feas[:3]:
    P(f"  decomposition at {th:.0f} deg (nonzero coefficients):")
    for k, v in sol.items():
        vv = np.atleast_1d(v)
        if np.abs(vv).max() > 1e-6: P(f"     {k:26s} {np.round(v, 5).tolist()}  ({parity(k if k in info else k + ':s')})")

# ---- clean feasible solutions (exact sign cone), verify on a fresh sample, save
def clean(sol):
    out = {}
    for nm in singles:
        v = sol[nm]; out[nm] = min(v, 0.0) if parity(nm) == "even" else max(v, 0.0)
    for d in doubled:
        mu, V = np.linalg.eigh(sol[d]); mu = np.minimum(mu, 0) if parity(d) == "even" else np.maximum(mu, 0)
        out[d] = V @ np.diag(mu) @ V.T
    return out
rng2 = np.random.default_rng(777)
fresh = np.array(sorted({tuple(sorted(rng2.choice(64, 4, replace=False))) for _ in range(21000)}))[:20000]
fq1 = sum(alt_s(-Kb[a].conj(), Kb[a], fresh) for a in range(10)).real
fq2 = sum(2 * alt_s(Kb[a], Kb[a], fresh).real for a in range(10))
fcols = {nm: sum(alt_s(a, a, fresh) for a in ms) for nm, ms in famo.items()}
for d in doubled:
    fcols[d + ":sc"] = sum(alt_s(a, b, fresh) for a, b in zip(famo[d + ":s"], famo[d + ":c"]))
def quartic(sol, cc):
    e = 0
    for nm in singles: e = e + sol[nm] * cc[nm]
    for d in doubled: e = e + sol[d][0, 0] * cc[d + ":s"] + sol[d][1, 1] * cc[d + ":c"] + 2 * sol[d][0, 1] * cc[d + ":sc"]
    return -0.25 * e
saved = {}
for th, val, sol in rows:
    if val < 1e-7:
        l1, l2 = np.cos(np.radians(th)), np.sin(np.radians(th))
        cs = clean(sol)
        r_s = np.abs(quartic(cs, cols) - (l1 * q1 + l2 * q2)).sum() / np.abs(l1 * q1 + l2 * q2).sum()
        r_f = np.abs(quartic(cs, fcols) - (l1 * fq1 + l2 * fq2)).sum() / np.abs(l1 * fq1 + l2 * fq2).sum()
        P(f"  {th:5.0f} deg: cleaned solution residual: sample {r_s:.2e}, fresh 20000-sample {r_f:.2e}")
        if th in (190.0, 200.0, 230.0, 250.0, 270.0):
            saved[f"th{int(th)}"] = cs
np.save("kramers_solutions.npy", saved, allow_pickle=True)
P(f"saved cleaned solutions for {sorted(saved)}")
P(f"total {time.time() - t0:.0f}s, peak RSS {mem():.0f} MB")

