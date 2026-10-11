"""W1 (c): is the LOCAL PART of the full free-momentum flow of the interaction a cancelling (principled) dressing?  E channel.
Exact identity (density transport, RN L2 design): the full flow of (1/24) sum phi^4 has lab vertex delta(sum_i Phi_eps(k_i)),
so E2_full(eps) = -(1/24) int delta(sum Phi(k)) w_eps(k) = const (change of variables).  L2 design: -(1/24) int delta(K) w_eps.
Local part of the full-flow vertex (centroid = symmetric k-space convention): v_loc(kappa) = int dK delta(sum_i Phi(K/4+kappa_i))
  = 1/det M(K*), M = (1/4) sum_i DPhi(k_i*), sum_i Phi(k_i*) = 0, k_i* = K*/4 + kappa_i.   E2_loc = -(1/24) int delta(K) v_loc^2 w_eps.
E channel flow dk/ds = eps sin k (x), -eps sin k (y) is exactly solvable: Phi(k) = 2 atan2(e^eps sin(k/2), cos(k/2)).
Monte Carlo over kappa (K=0 surface), common random numbers across eps; Richardson Hessians."""
import numpy as np, sys
m = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
N = int(float(sys.argv[2])) if len(sys.argv) > 2 else 400000
nchunk = int(sys.argv[3]) if len(sys.argv) > 3 else 10
def Phi1(k, a):   # exact flow by 'a' of dk/ds = sin k
    return 2*np.arctan2(np.exp(a)*np.sin(k/2), np.cos(k/2))
def J1(k, a):
    return np.exp(a)/(np.cos(k/2)**2 + np.exp(2*a)*np.sin(k/2)**2)
AS = lambda e: (e, -e, 0.0)
def wd(P): return np.sqrt(m**2 + (4*np.sin(P/2)**2).sum(-1))
def weight(k, e):
    P = np.stack([Phi1(k[..., c], AS(e)[c]) for c in range(3)], -1)
    J = np.prod(np.stack([J1(k[..., c], AS(e)[c]) for c in range(3)], -1), -1)
    W = wd(P)
    return np.prod(J/(2*W), axis=-1)/W.sum(-1)
def quantities(kap, e):
    w0 = weight(kap, e); v = np.ones(kap.shape[0]); kst = np.empty_like(kap); res_max = 0
    for c in range(3):
        a = AS(e)[c]; K = np.zeros(kap.shape[0])
        for it in range(8):
            kk = kap[..., c] + K[:, None]/4
            r = Phi1(kk, a).sum(1); r = (r + np.pi) % (2*np.pi) - np.pi
            Mc = J1(kk, a).sum(1)/4
            K = K - r/Mc
        kk = kap[..., c] + K[:, None]/4; kst[..., c] = kk
        r = Phi1(kk, a).sum(1); res_max = max(res_max, np.abs((r+np.pi) % (2*np.pi) - np.pi).max())
        v = v/(J1(kk, a).sum(1)/4)
    wst = weight(kst, e)
    return w0, v, wst, res_max
rng = np.random.default_rng(12345)
d = 0.04; eps_list = [-d, -d/2, 0, d/2, d]
allrows = []
for c in range(nchunk):
    k3 = rng.uniform(-np.pi, np.pi, size=(N, 3, 3)); k4 = -k3.sum(1, keepdims=True)
    kap = np.concatenate([k3, k4], 1)
    rows = {}
    for e in eps_list:
        w0, v, wst, rmax = quantities(kap, e)
        rows[e] = np.array([w0.mean(), (w0*v*v).mean(), (wst*v).mean(), (w0*v).mean(), (w0*(v*v-1)).mean()])
    allrows.append(rows)
def hess(idx, rows):
    D = lambda e: (rows[e][idx]+rows[-e][idx]-2*rows[0][idx])/e**2
    return (4*D(d/2)-D(d))/3
names = ['L2 design        int delta(K) w        ', 'local part       int delta(K) v_loc^2 w', 'full flow        int w(k*) v_loc       ',
         'linear-v variant int delta(K) v_loc w  ', 'local - L2       int delta(K)(v^2-1) w ']
print(f'm={m} channel E: MC samples {N*nchunk:.1e} ({nchunk} chunks); Hessians H per cell (mu2/lam^2 = -H/24); Newton residual {rmax:.1e}')
for idx in range(5):
    hs = np.array([hess(idx, r) for r in allrows])
    print(f'   {names[idx]}: H = {hs.mean():+.4e} +- {hs.std(ddof=1)/np.sqrt(len(hs)):.1e}  -> mu2/lam^2 = {-hs.mean()/24:+.3e}')
print(f'   int w at eps=0: {np.mean([r[0][0] for r in allrows]):.5e} (lattice I4(L=24) = 1.656164e-04); exact L2 H = 2.42235e-05')
