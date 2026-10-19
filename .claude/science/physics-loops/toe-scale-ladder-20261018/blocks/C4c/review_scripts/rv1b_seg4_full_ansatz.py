"""4-site collinear segment: general U(1)-conserving Hermitian h (70 real params: 16 diagonal + 54 hop),
NO Lemma V reduction.  Minimise sum_t ||[h, h_t]||^2 (t=1,2,3) subject to ||hop part|| = 1, with an
analytic Jacobian.  A nonzero minimum is numerical evidence (not proof) that no non-diagonal commuting family exists."""
import itertools, time, numpy as np, scipy.optimize as so
from rv_common import check, total
rng = np.random.default_rng(11)
k = 4; q = np.array([bin(i).count("1") for i in range(16)])
Db, Xb = [], []
for i in range(16):
    for j in range(i, 16):
        if q[i] != q[j]: continue
        if i == j:
            E = np.zeros((16, 16), complex); E[i, i] = 1; Db.append(E)
        else:
            E = np.zeros((16, 16), complex); E[i, j] = E[j, i] = 1; Xb.append(E)
            E = np.zeros((16, 16), complex); E[i, j] = 1j; E[j, i] = -1j; Xb.append(E)
B = Db + Xb; nd = len(Db); m = len(B)
check("parameter count 16 + 54 = 70", (nd, len(Xb)) == (16, 54))
emb = [([np.kron(E, np.eye(2**t)) for E in B], [np.kron(np.eye(2**t), E) for E in B]) for t in (1, 2, 3)]
W = 10.0
def H(z, L): return np.tensordot(z, np.array(L), axes=1)
def res_jac(z):
    r, J = [], []
    for L0, L1 in emb:
        H0, H1 = H(z, L0), H(z, L1); C = H0 @ H1 - H1 @ H0
        r += [C.real.ravel(), C.imag.ravel()]
        cols = [(L0[i] @ H1 - H1 @ L0[i] + H0 @ L1[i] - L1[i] @ H0).ravel() for i in range(m)]
        Jc = np.array(cols).T; J += [Jc.real, Jc.imag]
    x = z[nd:]; r.append(np.array([W * (x @ x - 1)]))
    jr = np.zeros((1, m)); jr[0, nd:] = 2 * W * x; J.append(jr)
    return np.concatenate(r), np.vstack(J)
cache = {}
def fun(z): rr, JJ = res_jac(z); cache["J"] = JJ; return rr
def jac(z): return res_jac(z)[1]
# check the analytic Jacobian against finite differences
z = rng.normal(size=m); r0, J0 = res_jac(z); e = 1e-6; i = 20; dz = np.zeros(m); dz[i] = e
check("analytic Jacobian matches finite difference", np.allclose((res_jac(z + dz)[0] - r0) / e, J0[:, i], atol=1e-4))
# positive control: diagonal h + 0 hop solves the commutators (residual only from the constraint)
best = np.inf; t0 = time.time(); vals = []
for rs in range(6):
    z0 = rng.normal(size=m); z0[nd:] /= np.linalg.norm(z0[nd:])
    sol = so.least_squares(fun, z0, jac=jac, method="lm", xtol=1e-15, ftol=1e-15, max_nfev=3000)
    vals.append(float(np.sum(sol.fun[:-1]**2))); best = min(best, vals[-1])
    print(f"restart {rs}: commutator^2 = {vals[-1]:.5f}, constraint residual = {sol.fun[-1]:.2e}, {time.time()-t0:.0f}s", flush=True)
check("4-segment, general U(1) ansatz: min sum_t ||[h,h_t]||^2 with unit hop part bounded away from 0", best > 1e-3, f"min = {best:.4f}")
total()
