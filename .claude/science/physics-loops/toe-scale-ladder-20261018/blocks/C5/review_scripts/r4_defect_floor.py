"""Reviewer re-evaluation of the r=2 near-unitary W3=-1 matrix (worker's logs/s4d_params_final.npy), own code:
true sup-defect (dense grid + local maximisation; the defect is a trig polynomial of degree 4 per axis),
W3 by the GL formula on three offset grids (non-Laurent inverse, so convergence is checked), min|det|,
sup distance to the nearest point where the straight-line homotopy could fail; then a short own
Levenberg-Marquardt continuation of the pure unitarity residual to see the trend (time-capped)."""
import sys, time, itertools, numpy as np
from scipy.optimize import least_squares, minimize
from rlib import Ck, w3_GL, grid
ck = Ck()
p = np.load('../logs/s4d_params_final.npy')
H = np.array(list(itertools.product(range(-2,3), repeat=3))); nh = len(H)
def A_of(p): return (p[:nh*4] + 1j*p[nh*4:]).reshape(nh,2,2)
def U_at(A, k):  # k (...,3)
    ph = np.exp(1j*(k @ H.T)); return np.einsum('...n,nij->...ij', ph, A)
def defect_at(A, k):
    U = U_at(A, k); return np.linalg.norm(U@np.conj(np.swapaxes(U,-1,-2)) - np.eye(2), ord=2, axis=(-2,-1))
def sup_defect(A, N=40, nloc=20):
    K = np.stack(grid(N, 0.0), -1).reshape(-1,3); d = defect_at(A, K)
    best = d.max(); idx = np.argsort(d)[-nloc:]
    for i in idx:
        r = minimize(lambda k: -defect_at(A, k[None,:])[0], K[i], method='Nelder-Mead', options={'xatol':1e-10,'fatol':1e-16,'maxiter':2000})
        best = max(best, -r.fun)
    return best
def w3_of(A, N, off):
    K = np.stack(grid(N, off), -1)
    ph = np.exp(1j*(K @ H.T))
    U = np.einsum('...n,nij->...ij', ph, A)
    dU = [np.einsum('...n,nij->...ij', ph*(1j*H[:,b]), A) for b in range(3)]
    return w3_GL(U, dU).real, np.abs(np.linalg.det(U)).min()
A = A_of(p)
coef_norm = np.abs(A).max()
sd = sup_defect(A)
ws = [w3_of(A, N, off) for N, off in ((40,0.5),(56,0.37),(72,0.11))]
print(f'loaded params: max|coef| {coef_norm:.3f}; sup defect (operator norm, dense+local max) {sd:.3e}; '
      f'W3 at N=40,56,72: {[round(w[0],9) for w in ws]}; min|det| {[round(w[1],6) for w in ws]}', flush=True)
ck(f'worker defect figure reproduced to within a factor 2 (own sup {sd:.2e} vs reported 1.82e-6)', sd < 3.7e-6 and sd > 0.9e-6)
ck('W3 = -1 converged on three independent grids (|W3+1| < 1e-6)', all(abs(w[0]+1) < 1e-6 for w in ws))
# own LM continuation of pure unitarity residual on 9^3 grid (exact: a degree-4 trig polynomial vanishing on 9^3 vanishes)
Ku = np.stack(grid(9, 0.0), -1).reshape(-1,3); Cu = np.exp(1j*(Ku @ H.T))
E = np.zeros((nh*4, nh, 2, 2)); 
for t in range(nh*4): E[t].flat[t] = 1
def res(q):
    U = np.einsum('kn,nij->kij', Cu, A_of(q)); R = U@np.conj(np.swapaxes(U,1,2)) - np.eye(2)
    return np.concatenate([R.real.ravel(), R.imag.ravel()])
def jac(q):
    U = np.einsum('kn,nij->kij', Cu, A_of(q)); Ud = np.conj(np.swapaxes(U,1,2))
    dU = np.einsum('kn,tnij->tkij', Cu, E)          # derivative wrt real parts
    cols = []
    for alpha in (1.0, 1j):
        dX = alpha*dU
        dR = dX@Ud[None] + U[None]@np.conj(np.swapaxes(dX,-1,-2))
        cols.append(dR)
    dR = np.concatenate(cols, 0)  # (2*nh*4, k, 2, 2)
    return np.concatenate([dR.real.reshape(len(dR),-1), dR.imag.reshape(len(dR),-1)], 1).T
r0 = res(p)
fd = (res(p + 1e-7*np.eye(len(p))[5]) - r0)/1e-7
ck('own analytic Jacobian matches finite difference', np.allclose(jac(p)[:,5], fd, atol=1e-5))
hist = [(0.5*np.sum(r0**2), sd, ws[0][0])]
q = p.copy(); t0 = time.time()
for stage in range(6):
    if time.time()-t0 > 900: break
    sol = least_squares(res, q, jac=jac, method='lm', max_nfev=200, xtol=3e-16, ftol=3e-16, gtol=3e-16)
    q = sol.x; Aq = A_of(q); sdq = sup_defect(Aq, N=24, nloc=8); wq, md = w3_of(Aq, 40, 0.5)
    hist.append((sol.cost, sdq, wq))
    print(f'own LM stage {stage}: cost {sol.cost:.3e}  sup defect {sdq:.3e}  W3(N=40) {wq:+.6f}  min|det| {md:.5f}  t={time.time()-t0:.0f}s', flush=True)
np.save('r4_params_after_review_LM.npy', q)
ck('all continuation iterates keep integer W3 (no silent crossing of det = 0)', all(abs(h[2]-round(h[2])) < 1e-6 for h in hist))
ck('no exact (defect < 1e-10) range-2 unitary with W3 = -1 reached (Theorem K consistency)', not (hist[-1][1] < 1e-10 and abs(hist[-1][2]+1) < 1e-6))
sys.exit(ck.total())
