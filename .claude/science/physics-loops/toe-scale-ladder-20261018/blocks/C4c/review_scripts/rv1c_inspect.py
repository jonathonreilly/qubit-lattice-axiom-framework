import numpy as np, scipy.optimize as so, time
src = open('rv1b_seg4_full_ansatz.py').read().split('# check the analytic')[0]
exec(src)
# original (non-compact) normalisation: ||X|| = 1, D free
def res_jac(z):
    r, J = [], []
    for L0, L1 in emb:
        H0, H1 = H(z, L0), H(z, L1); C = (H0 @ H1 - H1 @ H0).toarray()
        r += [C.real.ravel(), C.imag.ravel()]
        Jc = np.array([(L0[i] @ H1 - H1 @ L0[i] + H0 @ L1[i] - L1[i] @ H0).toarray().ravel() for i in range(m)]).T
        J += [Jc.real, Jc.imag]
    x = z[nd:]; r.append(np.array([W * (x @ x - 1)])); jr = np.zeros((1, m)); jr[0, nd:] = 2 * W * x; J.append(jr)
    return np.concatenate(r), np.vstack(J)
rng = np.random.default_rng(11); _ = rng.normal(size=m)   # same stream as rv1b restart 0
z0 = rng.normal(size=m); z0[nd:] /= np.linalg.norm(z0[nd:])
sol = so.least_squares(fun, z0, jac=jac, method="lm", xtol=1e-15, ftol=1e-15, max_nfev=400)
print("commutator^2", np.sum(sol.fun[:-1]**2), "hop norm", np.linalg.norm(sol.x[nd:]))
z = sol.x; h = sum(c*E for c,E in zip(z,B))
print("||D|| =", np.linalg.norm(z[:nd]), " D pattern (depends only on n_2):", np.round(z[:nd], 2))
print("=> degenerate limit h ~ c n_2 + O(1) hop with c -> infinity; not a solution (informational, no PASS/FAIL)")
