"""R6-3 (c): independent Monte Carlo of the LRL count variance in truncated past cones
P_T = J^-(0) cap {t' >= -T}, t' = time of a frame with rapidity eta (density sinh^2 on [0, eta_max]) along nhat.
Compared with the exact Haar shell-sum values (r63_variance.py: Var/T^3 -> 0.4847)."""
import numpy as np, time, sys
rng = np.random.default_rng(31)
s7 = np.sqrt(7.0)
def count(T, eta, nhat, u):
    ch, sh = np.cosh(eta), np.sinh(eta)
    ctr = -T*sh*nhat
    half = np.sqrt((T*ch)**2*nhat**2 + T**2*(1-nhat**2))
    ax = [np.arange(np.floor(ctr[i]-half[i]-u[i+1])-1, np.ceil(ctr[i]+half[i]-u[i+1])+2) + u[i+1] for i in range(3)]
    X2, X3 = np.meshgrid(ax[1], ax[2], indexing='ij'); tot = 0
    for x1 in ax[0]:
        r = np.sqrt(x1**2 + X2**2 + X3**2)
        thi = -r
        tlo = (-T + sh*(nhat[0]*x1 + nhat[1]*X2 + nhat[2]*X3))/ch
        ok = tlo <= thi
        lo = np.ceil(tlo[ok]/s7 - u[0]); hi = np.floor(thi[ok]/s7 - u[0])
        tot += np.clip(hi - lo + 1, 0, None).sum()
    return tot
def sample_eta(eta_max):
    while True:
        e = rng.random()*eta_max
        if rng.random() < np.sinh(e)**2/np.sinh(eta_max)**2: return e
t0 = time.time(); eta_max = float(sys.argv[1]) if len(sys.argv) > 1 else 1.5
for T, ns in ((13, 1500), (27, 1500), (54, 1000), (108, 600), (216, 200)):
    Ns = np.empty(ns)
    for i in range(ns):
        e = sample_eta(eta_max); v = rng.normal(size=3); v /= np.linalg.norm(v)
        Ns[i] = count(T, e, v, rng.random(4))
    rhoV = np.pi*T**4/3/s7; var = Ns.var(ddof=1)
    bs = [np.var(rng.choice(Ns, ns), ddof=1) for _ in range(300)]
    print("eta_max=%.1f T=%3d n=%d <N>/rhoV=%.6f Var/T^3=%.4f +- %.4f Var/rhoV=%.3e (%.0f s)" %
          (eta_max, T, ns, Ns.mean()/rhoV, var/T**3, np.std(bs)/T**3, var/rhoV, time.time()-t0), flush=True)
