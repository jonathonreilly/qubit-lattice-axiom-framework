"""R6-3 (c): independent Monte Carlo of the LRL diamond count variance at T = 54, 108, 216
(own counting code; frames: rapidity density sinh^2 on [0, eta_max], isotropic direction, fresh torus shift).
Compared with the exact Haar (Siegel shell-sum) values of r63_variance.py."""
import numpy as np, time, sys
rng = np.random.default_rng(2026)
s7 = np.sqrt(7.0)

def count(T, eta, nhat, u):
    # diamond with apex at origin, top at p = T(cosh eta, sinh eta nhat) in the lattice frame;
    # lattice points (s7 (n0+u0), n+u_vec). Count per spatial column the time points in [|x|, p0 - |x - pv|].
    p0 = T*np.cosh(eta); pv = T*np.sinh(eta)*nhat
    half = np.sqrt((p0/2)**2*nhat**2 + (T/2)**2*(1-nhat**2))
    ctr = pv/2
    ax = [np.arange(np.floor(ctr[i]-half[i]-u[i+1])-1, np.ceil(ctr[i]+half[i]-u[i+1])+2) + u[i+1] for i in range(3)]
    tot = 0
    X2, X3 = np.meshgrid(ax[1], ax[2], indexing='ij')
    for x1 in ax[0]:
        r0 = np.sqrt(x1**2 + X2**2 + X3**2)
        r1 = np.sqrt((x1-pv[0])**2 + (X2-pv[1])**2 + (X3-pv[2])**2)
        ok = r0 <= p0 - r1
        lo = np.ceil(r0[ok]/s7 - u[0]); hi = np.floor((p0 - r1[ok])/s7 - u[0])
        tot += np.clip(hi - lo + 1, 0, None).sum()
    return tot

def sample_eta(eta_max):
    while True:
        e = rng.random()*eta_max
        if rng.random() < np.sinh(e)**2/np.sinh(eta_max)**2: return e

t0 = time.time()
eta_max = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
for T, ns in ((54, 1000), (108, 1000), (216, 800), (432, 250)):
    Ns = np.empty(ns)
    for i in range(ns):
        e = sample_eta(eta_max); v = rng.normal(size=3); v /= np.linalg.norm(v)
        Ns[i] = count(T, e, v, rng.random(4))
    rhoV = np.pi*T**4/24/s7
    var = Ns.var(ddof=1)
    # bootstrap error of the variance
    bs = [np.var(rng.choice(Ns, ns), ddof=1) for _ in range(300)]
    print("eta_max=%.1f T=%3d  n=%d  <N>/rhoV=%.6f  Var/T^2=%.4f +- %.4f  Var/rhoV=%.3e   (%.0f s)" %
          (eta_max, T, ns, Ns.mean()/rhoV, var/T**2, np.std(bs)/T**2, var/rhoV, time.time()-t0), flush=True)
