"""R2-2: larger Monte Carlo of Lorentz invariance in law for the 1+1 LRL (Z[sqrt2] lattice, uniform
boost phase eta in [0,eta0), uniform shift). Statistic: count in the unit square W and in boosted
windows Lambda_chi W, plus a two-window joint statistic (N(W1), N(W2)) for timelike-separated squares."""
import numpy as np
rng = np.random.default_rng(7)
r2 = np.sqrt(2.0); s = 2**-0.25; eta0 = np.log(3 + 2*r2)
def basis_tx(eta):
    cols = []
    for a, b in [(1, 0), (0, 1)]:
        u = s*np.exp(eta)*(a + b*r2); v = s*np.exp(-eta)*(a - b*r2)
        cols.append([(u+v)/2, (u-v)/2])
    return np.array(cols).T
def boost(chi):
    return np.array([[np.cosh(chi), np.sinh(chi)], [np.sinh(chi), np.cosh(chi)]])
sq = np.array([[.5, .5], [.5, -.5], [-.5, .5], [-.5, -.5]])
def counts(chi, nsamp, offset=np.array([0., 0.])):
    L = boost(chi); Linv = np.linalg.inv(L)
    c1 = np.empty(nsamp, int); c2 = np.empty(nsamp, int)
    for i in range(nsamp):
        eta = rng.uniform(0, eta0); sh = rng.uniform(0, 1, 2); B = basis_tx(eta)
        corners = np.vstack([(L @ sq.T).T, (L @ (sq + offset).T).T])
        lc = np.linalg.solve(B, corners.T).T; lo = np.floor(lc.min(0)) - 2; hi = np.ceil(lc.max(0)) + 2
        g = np.mgrid[int(lo[0]):int(hi[0])+1, int(lo[1]):int(hi[1])+1].reshape(2, -1).T
        X = (B @ (g + sh).T).T
        Y = (Linv @ X.T).T
        c1[i] = np.sum(np.all(np.abs(Y) < 0.5, axis=1))
        c2[i] = np.sum(np.all(np.abs(Y - offset) < 0.5, axis=1))
    return c1, c2
N = 30000
off = np.array([1.7, 0.4])   # second square displaced by a timelike vector (in the window frame)
for chi in [0.0, 0.7, 2.5]:
    c1, c2 = counts(chi, N, off)
    p = [np.mean(c1 == k) for k in range(3)]
    cov = np.mean(c1*c2) - c1.mean()*c2.mean()
    se_p0 = np.sqrt(p[0]*(1-p[0])/N)
    print(f"chi={chi:3.1f}: mean={c1.mean():.4f} var={c1.var():.4f} P(N=0,1,2)={np.round(p,4)} (SE of P0 {se_p0:.4f})  Cov(N(W),N(W+a))={cov:+.4f}")
