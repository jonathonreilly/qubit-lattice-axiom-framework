"""4-site collinear segment: general U(1)-conserving Hermitian h (70 real params: 16 diagonal + 54 hop),
NO Lemma V reduction.  Minimise sum_t ||[h, h_t]||^2 (t=1,2,3) subject to ||hop part|| = 1, with an
analytic Jacobian.  A nonzero minimum is numerical evidence (not proof) that no non-diagonal commuting family exists."""
import itertools, time, numpy as np, scipy.optimize as so, scipy.sparse as ssp
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
emb = [([ssp.csr_matrix(ssp.kron(E, ssp.identity(2**t))) for E in B], [ssp.csr_matrix(ssp.kron(ssp.identity(2**t), E)) for E in B]) for t in (1, 2, 3)]
W = 10.0
FR = 0.5   # fixed hop fraction ||X||^2 = FR, ||D||^2 = 1 - FR (compact; excludes the D -> infinity degenerate limit)
def H(z, L):
    out = L[0] * z[0]
    for c, M in zip(z[1:], L[1:]): out = out + M * c
    return ssp.csr_matrix(out)
def res_jac(z):
    r, J = [], []
    for L0, L1 in emb:
        H0, H1 = H(z, L0), H(z, L1); C = (H0 @ H1 - H1 @ H0).toarray()
        r += [C.real.ravel(), C.imag.ravel()]
        cols = [(L0[i] @ H1 - H1 @ L0[i] + H0 @ L1[i] - L1[i] @ H0).toarray().ravel() for i in range(m)]
        Jc = np.array(cols).T; J += [Jc.real, Jc.imag]
    x, d = z[nd:], z[:nd]; r.append(np.array([W * (x @ x - FR), W * (d @ d - (1 - FR))]))
    jr = np.zeros((2, m)); jr[0, nd:] = 2 * W * x; jr[1, :nd] = 2 * W * d; J.append(jr)
    return np.concatenate(r), np.vstack(J)
cache = {}
def fun(z): rr, JJ = res_jac(z); cache["J"] = JJ; return rr
def jac(z): return res_jac(z)[1]
# check the analytic Jacobian against finite differences
z = rng.normal(size=m); r0, J0 = res_jac(z); e = 1e-6; i = 20; dz = np.zeros(m); dz[i] = e
check("analytic Jacobian matches finite difference", np.allclose((res_jac(z + dz)[0] - r0) / e, J0[:, i], atol=1e-4))
# NOTE: with ||X||=1 and D free the infimum is 0 but is approached only as ||D|| -> infinity
# (h -> c n_2 + o(1) hop; observed in rv1c_inspect.py), i.e. a degenerate limit, not a solution.
# Compact normalisation: if a solution with hop fraction f0 exists, adding multiples of the identity
# gives solutions with every smaller fraction, so testing FR in {0.5, 0.05} probes fractions >= FR.
results = {}
for FR in (0.5, 0.05):
    best = np.inf; t0 = time.time()
    for rs in range(2):
        z0 = rng.normal(size=m); z0[nd:] *= np.sqrt(FR) / np.linalg.norm(z0[nd:]); z0[:nd] *= np.sqrt(1 - FR) / np.linalg.norm(z0[:nd])
        sol = so.least_squares(fun, z0, jac=jac, method="lm", xtol=1e-15, ftol=1e-15, max_nfev=250)
        v = float(np.sum(sol.fun[:-2]**2)); best = min(best, v)
        print(f"FR={FR} restart {rs}: nfev={sol.nfev} commutator^2={v:.5f} constraints={sol.fun[-2:]} {time.time()-t0:.0f}s", flush=True)
    results[FR] = best
check("4-segment, general 70-param U(1) ansatz, compact normalisation: min commutator^2 bounded away from 0 (numerical evidence only)",
      min(results.values()) > 1e-4, results)
total()
