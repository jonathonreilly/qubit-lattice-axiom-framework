"""R4-5 check: count variance of lattice substrates in causal diamonds (3+1), vs Poisson.

Lattice L_s = diag(s,1,1,1) Z^4 + u, u uniform (translation average), seen by a diamond
of proper height T whose axis has rapidity eta along x1 relative to the lattice frame.
  s = sqrt(7): one realization frame of the Lorentz-random lattice LRL (no null reciprocal vectors)
  s = 1      : Z^4 with Minkowski form (null lattice vectors exist; set B/C crystal read as Lorentzian)
Var_u(N) is computed by Monte Carlo over u; Poisson reference Var = rho V = V/s, V = pi T^4/24.
LRL ensemble average over g in SO+(1,3)/Gamma = average of these over a compact set of eta.
"""
import numpy as np, sys, time
rng = np.random.default_rng(12345)

def count_diamond(T, eta, s, u):
    p0, p1 = T*np.cosh(eta), T*np.sinh(eta)
    # spatial columns x = n + u_s inside spheroid |x| + |x-p| <= p0
    x1 = np.arange(np.floor((p1-p0)/2 - u[1]) - 1, np.ceil((p1+p0)/2 - u[1]) + 2) + u[1]
    b = T/2.0
    x2 = np.arange(np.floor(-b - u[2]) - 1, np.ceil(b - u[2]) + 2) + u[2]
    x3 = np.arange(np.floor(-b - u[3]) - 1, np.ceil(b - u[3]) + 2) + u[3]
    X1, X2, X3 = np.meshgrid(x1, x2, x3, indexing='ij')
    r0 = np.sqrt(X1**2 + X2**2 + X3**2)
    r1 = np.sqrt((X1-p1)**2 + X2**2 + X3**2)
    tlo, thi = r0, p0 - r1
    ok = tlo <= thi
    lo = np.ceil(tlo[ok]/s - u[0]); hi = np.floor(thi[ok]/s - u[0])
    c = hi - lo + 1
    return np.sum(np.clip(c, 0, None))

def var_count(T, eta, s, nsamp):
    Ns = np.empty(nsamp)
    for i in range(nsamp):
        Ns[i] = count_diamond(T, eta, s, rng.random(4))
    return Ns.mean(), Ns.var(ddof=1), Ns

t_start = time.time()
print("columns: s, eta, T, <N>, rho V, Var_u(N), Var/(rho V), sd(Var) est")
results = {}
for s, sname in [(np.sqrt(7.0), "L7"), (1.0, "Z4")]:
    for eta in (0.0, 0.7, 1.4):
        rows = []
        for T in (6, 9, 13, 19, 27, 38, 54, 76):
            ns = 1500
            m, v, Ns = var_count(T, eta, s, ns)
            rhoV = np.pi*T**4/24/s
            # rough sd of sample variance: sqrt(2/(n-1)) v (gaussian)
            print("%s eta=%.1f T=%3d  <N>=%.5e  rhoV=%.5e  Var=%.4e  Var/rhoV=%.4e  (+-%.0f%%)" %
                  (sname, eta, T, m, rhoV, v, v/rhoV, 100*np.sqrt(2/(ns-1))), flush=True)
            rows.append((T, v, rhoV))
        rows = np.array(rows)
        sl = np.polyfit(np.log(rows[:,0]), np.log(rows[:,1]), 1)[0]
        sl_hi = np.polyfit(np.log(rows[-4:,0]), np.log(rows[-4:,1]), 1)[0]
        print("  -> %s eta=%.1f  fitted Var ~ T^%.2f (all T), T^%.2f (largest 4); Poisson would be T^4" % (sname, eta, sl, sl_hi), flush=True)
        results[(sname, eta)] = rows
print("elapsed %.1f s" % (time.time()-t_start))
