"""RL1 (C): Monte Carlo of the REALIZATION inverse of the BD operator on flat Poisson diamonds (rho = 1), 2D and 4D.
Fixed tips y (bottom) and x (top) are Palm points.  B = beta(-I + N); H = (I-N)^{-1} - I (row of x by triangular solve).
Checks: (i) MC mean of H(x,y) against the exact mean Hbar from the Volterra equation (RL1_B), i.e. E[B^{-1}] = (E B)^{-1};
        (ii) the realization noise sd H(x,y) and of a source-driven field phi(x) = sum_y H(x,y) J(y) as the diamond grows.
4D: c = (1,-9,16,-8) on n = 0..3.   2D: N = 2*(1,-2,1) on n = 0..2  (B2 = 2 rho(-I + N), mean -> Box).
Johnston one-hop control: H_link(x,y) = L(x,y)  (a L, no recursion).
"""
import numpy as np, sys, time
from scipy.linalg import solve_triangular
rng = np.random.default_rng(20261011)

def sprinkle(T, d):
    if d == 4:
        vol = np.pi/24*T**4; N = rng.poisson(vol); out = []; got = 0
        while got < N:
            m = int((N-got)*1.7)+100
            t = rng.uniform(0, T, m); xyz = rng.uniform(-T/2, T/2, (m, 3))
            ok = np.sqrt((xyz**2).sum(1)) < np.minimum(t, T-t)
            out.append(np.column_stack([t[ok], xyz[ok]])); got += ok.sum()
        P = np.vstack(out)[:N] if N > 0 else np.empty((0, 4))
        tips = (np.zeros((1, 4)), np.array([[T, 0, 0, 0.]]))
    else:
        vol = T*T/2; N = rng.poisson(vol)
        u = rng.uniform(0, T/np.sqrt(2), N); v = rng.uniform(0, T/np.sqrt(2), N)
        P = np.column_stack([(u+v)/np.sqrt(2), (u-v)/np.sqrt(2)])
        tips = (np.zeros((1, 2)), np.array([[T, 0.]]))
    P = P[np.argsort(P[:, 0])]
    return np.vstack([tips[0], P, tips[1]])

def causal(P):
    dt = P[None, :, 0] - P[:, None, 0]          # dt[i,j] = t_j - t_i
    dx2 = ((P[None, :, 1:] - P[:, None, 1:])**2).sum(-1)
    return (dt > 0) & (dt*dt > dx2)              # C[i,j] = i < j

def run(T, d, R, src):
    Hs = []; Ls = []; phis = []; Ns = []
    for r in range(R):
        P = sprinkle(T, d); n = P.shape[0]; Ns.append(n-2)
        C = causal(P); Cf = C.astype(np.float32)
        cnt = np.rint(Cf @ Cf).astype(np.int32)   # cnt[i,j] = # z with i<z<j
        import os
        if d == 4: coef = np.array([float(c) for c in os.environ.get('RL1_COEF', '1,-9,16,-8').split(',')])
        else: coef = 2*np.array([1., -2., 1.])
        Nm = np.zeros((n, n))
        mask = C & (cnt < len(coef))
        Nm[mask] = coef[cnt[mask]]               # Nm[i,j]: weight for i<j  (i in past of j)
        # row of x (= n-1) of (I - N^T)^{-1}: we need H(x,y) = sum_k (N^k)[y->x]; with A[j,i] = Nm[i,j] (lower-tri in time order)
        A = Nm.T                                   # A[j,i] = weight of hop i -> j, strictly lower triangular
        M = np.eye(n) - A
        ex = np.zeros(n); ex[-1] = 1.0
        z = solve_triangular(M.T, ex, lower=False) # z^T = e_x^T (I - A)^{-1}
        hrow = z.copy(); hrow[-1] -= 1.0           # H(x, .) row
        Hs.append(hrow[0]); Ls.append(float(C[0, -1] and cnt[0, -1] == 0))
        J = src(P); J[0] = 0; J[-1] = 0
        phis.append(hrow @ J)
    return np.array(Hs), np.array(Ls), np.array(phis), np.mean(Ns)

if __name__ == "__main__":
    t0 = time.time()
    d = int(sys.argv[1]); Ts = [float(a) for a in sys.argv[2].split(",")]; Rs = [int(a) for a in sys.argv[3].split(",")]
    for T, R in zip(Ts, Rs):
        # source centred ON the past cone of x: t0 = 0.65T, radius r0 = 0.35T along x-axis, width 0.07T
        def src(P, T=T):
            c = np.zeros(P.shape[1]); c[0] = 0.65*T; c[1] = 0.35*T
            return np.exp(-((P-c)**2).sum(1)/(2*(0.07*T)**2))
        H, L, phi, Nm = run(T, d, R, src)
        print(f"d={d} T={T:5.1f} <N>={Nm:8.1f} R={R}:  H(x,y) mean={H.mean(): .4e} +- {H.std(ddof=1)/np.sqrt(R):.2e}  sd={H.std(ddof=1):.4e}"
              f" | phi mean={phi.mean(): .4e} +- {phi.std(ddof=1)/np.sqrt(R):.2e} sd={phi.std(ddof=1):.4e} sd/|mean|={phi.std(ddof=1)/max(abs(phi.mean()),1e-300):.3e}"
              f" | maxabs phi={np.abs(phi).max():.3e}  (%.0fs)" % (time.time()-t0))
        sys.stdout.flush()
