"""Lower bound (convex relaxation over ALL operations on the slab, any ancilla, Gaussian or not) versus the explicit
best Gaussian isometry (upper bound).  Clarabel with tight tolerances."""
import numpy as np, time, cvxpy as cp
import r1913_lib as L
def sdp(W):
    n = W['n']; R = (n-1)//2; m = 2*R; Gx, Gp = W['Gx'], W['Gp']
    Xo = np.array([[Gx[abs(i-j)] for j in range(m)] for i in range(m)])
    Po = np.array([[Gp[abs(i-j)] for j in range(m)] for i in range(m)])
    Go = np.block([[Xo, np.zeros((m, m))], [np.zeros((m, m)), Po]])
    Q0 = Go + 0.5j*L.J_of(m); w, U = np.linalg.eigh(Q0); keep = w > 1e-13*w.max(); Lm = U[:, keep]*np.sqrt(w[keep]); r = Lm.shape[1]
    Fd = np.zeros((2*m, 2))
    for i in range(m):
        Fd[i, 0] = Gx[abs(i+1)]; Fd[i, 1] = Gx[abs(i+1-(2*R+1))]
    Gs = cp.Variable((2*n, 2*n), symmetric=True); T = cp.Variable((2*n, 2*m))
    TL = T @ Lm
    Mb = cp.bmat([[Gs + 0.5j*L.J_of(n), TL], [TL.H, np.eye(r)]])
    cross = T @ Fd
    # subtract the objective of the product start (identity isometry) so the solver works on O(dE) numbers
    E = 0.5*cp.trace(W['A'] @ Gs) - cross[0, 0] - cross[n-1, 1]
    prob = cp.Problem(cp.Minimize(E), [Mb >> 0])
    prob.solve(solver='CLARABEL', tol_gap_abs=1e-13, tol_gap_rel=1e-13, tol_feas=1e-12, max_iter=400)
    return prob.value + W['const'] - W['Emid_old'] - W['e0'], prob.status
for M in (1.0, 0.3, 0.03):
    for R in (1, 2, 3, 4, 6):
        W = L.window(M, R)
        dU, S = L.symp_opt(W)
        t = time.time(); dL, st = sdp(W)
        print('M=%.2f R=%d  isometry(upper)=%.8e  SDP(lower)=%.8e  diff=%.1e  [%s, %.1fs]' % (M, R, dU, dL, dU-dL, st, time.time()-t), flush=True)
