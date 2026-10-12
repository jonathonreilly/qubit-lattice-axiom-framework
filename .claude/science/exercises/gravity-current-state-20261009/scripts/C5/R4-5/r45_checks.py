"""R4-5 checks: (1) aligned-row coefficient; (2) Bernoulli thinning of sites (records formed at random);
(3) boost-averaged LRL count variance (rapidity ~ sinh^2 on [0, eta_max], isotropic direction)."""
import numpy as np, time
rng = np.random.default_rng(777)

def count_diamond_dir(T, eta, nhat, s, u, keep_p=None):
    p0 = T*np.cosh(eta); pv = T*np.sinh(eta)*nhat
    half = np.sqrt((p0/2)**2*nhat**2 + (T/2)**2*(1-nhat**2))
    ctr = pv/2
    ax = [np.arange(np.floor(ctr[i]-half[i]-u[i+1])-1, np.ceil(ctr[i]+half[i]-u[i+1])+2) + u[i+1] for i in range(3)]
    X1, X2, X3 = np.meshgrid(*ax, indexing='ij')
    r0 = np.sqrt(X1**2+X2**2+X3**2)
    r1 = np.sqrt((X1-pv[0])**2+(X2-pv[1])**2+(X3-pv[2])**2)
    tlo, thi = r0, p0 - r1
    ok = tlo <= thi
    lo = np.ceil(tlo[ok]/s - u[0]); hi = np.floor(thi[ok]/s - u[0])
    c = np.clip(hi - lo + 1, 0, None)
    n = c.sum()
    if keep_p is None: return n
    return n, rng.binomial(int(n), keep_p)

s7 = np.sqrt(7.0)
print("(1) aligned time-row prediction Var/rhoV = (2 pi/15) rho s^4:")
print("    L7: %.4f   Z4: %.4f" % (2*np.pi/15*(1/s7)*s7**4, 2*np.pi/15))

print("(2) Bernoulli thinning, L7, eta=0.7 along x1, T=27, p in {0.3, 0.7}")
for p in (0.3, 0.7):
    Ns, Nr = [], []
    for i in range(1500):
        n, k = count_diamond_dir(27, 0.7, np.array([1.0,0,0]), s7, rng.random(4), keep_p=p)
        Ns.append(n); Nr.append(k)
    Ns, Nr = np.array(Ns), np.array(Nr)
    rhoV = np.pi*27**4/24/s7
    pred = p*(1-p)*Ns.mean() + p*p*Ns.var(ddof=1)
    print("    p=%.1f  Var(N_rec)=%.4e  predicted p(1-p)<N>+p^2 Var(N_sites)=%.4e  Var(N_rec)/(p rho V)=%.4f (1-p=%.1f)"
          % (p, Nr.var(ddof=1), pred, Nr.var(ddof=1)/(p*rhoV), 1-p))

print("(3) boost-averaged L7 (rapidity density ~ sinh^2 eta on [0, eta_max], isotropic direction, fresh u)")
def sample_eta(eta_max):
    while True:
        e = rng.random()*eta_max
        if rng.random() < np.sinh(e)**2/np.sinh(eta_max)**2: return e
t0 = time.time()
for eta_max in (1.0, 2.0):
    rows = []
    for T in (9, 13, 19, 27, 38):
        ns = 1200
        Ns = np.empty(ns)
        for i in range(ns):
            e = sample_eta(eta_max); v = rng.normal(size=3); v /= np.linalg.norm(v)
            Ns[i] = count_diamond_dir(T, e, v, s7, rng.random(4))
        rhoV = np.pi*T**4/24/s7
        print("    eta_max=%.1f T=%2d  <N>/rhoV=%.5f  Var/rhoV=%.4e (+-%.0f%%)" % (eta_max, T, Ns.mean()/rhoV, Ns.var(ddof=1)/rhoV, 100*np.sqrt(2/(ns-1))), flush=True)
        rows.append((T, Ns.var(ddof=1)))
    rows = np.array(rows)
    print("    -> eta_max=%.1f: Var ~ T^%.2f" % (eta_max, np.polyfit(np.log(rows[:,0]), np.log(rows[:,1]), 1)[0]), flush=True)
print("elapsed %.0f s" % (time.time()-t0))
