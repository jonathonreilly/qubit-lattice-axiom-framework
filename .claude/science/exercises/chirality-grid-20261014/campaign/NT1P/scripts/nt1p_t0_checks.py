"""NT-1' T0: code checks (no kernel numbers): builder vs lat2d, analytic dq/dA vs finite differences, decomposition identity,
exactness of div kbb = Abar and gauge invariance of kbb, canonical gauge, timing.  usage: python3 nt1p_t0_checks.py Lx T"""
import numpy as np, sys, time
from nt1p_lib import *
from lat2d import Geom, rand_half, nodes

Lx, T = int(sys.argv[1]), int(sys.argv[2]); t00 = time.time()
S = Strip(Lx, T); G = Geom(Lx, T, False, -1); rng = np.random.default_rng(11)
print(f"# NT-1' T0 checks Lx={Lx} Lt={2*T} N={S.N} nl={S.nl} np={S.np_}", flush=True)
ua = rand_half(rng, G, 0.25, 0.55); ub = rand_half(rng, G, 0.25, 0.55); phis = rng.normal(0, 0.2, (3, Lx))
A = S.joined(ua, ub, phis)
d = max(np.abs(S.D(A[i:i+1])[0] - G.full_D(ua, ub, phis[i])).max() for i in range(3))
print(f"builder vs lat2d.full_D: max diff {d:.2e}")
# analytic derivative vs finite differences
th = 1.7 * A[:1]; w, V = eig_H(S, th); R = dq_dA(S, th, w, V)[0]; eps = 1e-5; Rfd = np.zeros_like(R)
for l in range(S.nl):
    tp = th.copy(); tp[0, l] += eps; tm = th.copy(); tm[0, l] -= eps
    Rfd[:, l] = (q_of(S, *eig_H(S, tp)) - q_of(S, *eig_H(S, tm)))[0] / (2 * eps)
print(f"dq/dA analytic vs FD: max diff {np.abs(R - Rfd).max():.2e} (max |R| {np.abs(R).max():.2e}); gauge annihilation max|R dw| {np.abs(R @ (S.gauge(np.zeros((1,S.nl)), rng.normal(0,1,(1,S.ns)))[0])).max():.1e}")
# canonical gauge: same plaquettes/Wilson lines, A_t = 0, gauge orbit independence, theta covariance
Ac = S.canon(A); F1, W1 = S.FW(A); F2, W2 = S.FW(Ac)
om = rng.normal(0, 2.0, (3, S.ns)); Ac2 = S.canon(S.gauge(A, om))
print(f"canon: dF {np.abs(F1-F2).max():.1e} dW {np.abs(W1-W2).max():.1e} max|A_t| {np.abs(Ac[:, S.tl.reshape(-1)]).max():.1e} "
      f"orbit-independence {np.abs(Ac2-Ac).max():.1e} theta-covariance {np.abs(S.canon(S.theta(A)) - S.theta(Ac)).max():.1e}")
for model in ('11112', 'L1'):
    MS = Measure(S, model, Ns=8)
    t0 = time.time(); r = MS.ray(Ac, 8); dt = time.time() - t0
    divk = S.div(r['kbb']); print(f"[{model}] ray Ns=8 on 3 configs: {dt:.2f}s ({dt/3*1e3:.0f} ms/config); identity check {r['idchk']:.1e}; "
          f"|div kbb - Abar| {np.abs(divk - r['Abar']).max():.1e}; |sum Abar| {r['sumA']:.1e}; gmin {r['gmin']:.3f} idx_ok {r['idx_ok']}")
    r2 = MS.ray(S.gauge(Ac, om), 8)
    print(f"   kbb gauge invariance (non-canonical rep, same ray in gauge-transformed A): {np.abs(r2['kbb'] - r['kbb']).max():.1e}; "
          f"|kQ|/|kloc| = {np.abs(r['kQ']).max():.2e}/{np.abs(r['kloc']).max():.2e}; mean|mbar| bulk {np.abs(r['mbar']).mean():.3e}")
print(f"done [{time.time()-t00:.0f}s]")
