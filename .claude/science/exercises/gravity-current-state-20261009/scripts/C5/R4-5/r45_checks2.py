"""R4-5 checks 2: (a) small-misalignment suppression of the aligned volume law (L7, eta = 0.05, 0.2);
analytic time-row prediction with misalignment: Var_row = rho^2 sum_n 4 pi^2 T^4 sinc^2(M_n d T/2)/M_n^4 (x2 for +-n),
M_n = 2 pi n / s, d = sinh(eta) (spatial wavenumber k = M sinh eta). (b) Haar-ball-averaged L7 to T = 108."""
import numpy as np, time
exec(open('r45_checks.py').read().split('s7 = np.sqrt(7.0)')[0])
s7 = np.sqrt(7.0); rho = 1/s7
def row_pred(T, eta, s, rho, nmax=4000):
    n = np.arange(1, nmax+1); M = 2*np.pi*n/s; k = M*np.sinh(eta); q0 = M*np.cosh(eta)
    x = k*T/2
    sinc = np.where(x > 1e-12, np.sin(x)/np.where(x > 1e-12, x, 1), 1.0)
    return rho**2*np.sum(2*4*np.pi**2*T**4*sinc**2/q0**4)
t0 = time.time()
print("(a) L7 small misalignment: measured Var/rhoV vs time-row prediction")
for eta in (0.05, 0.2):
    for T in (6, 13, 27, 54, 108):
        ns = 600 if T < 100 else 300
        Ns = np.array([count_diamond_dir(T, eta, np.array([1.0,0,0]), s7, rng.random(4)) for i in range(ns)])
        rhoV = np.pi*T**4/24/s7
        print("   eta=%.2f T=%3d  Var/rhoV=%.4e (+-%.0f%%)   row-pred/rhoV=%.4e" % (eta, T, Ns.var(ddof=1)/rhoV, 100*np.sqrt(2/(ns-1)), row_pred(T, eta, s7, rho)/rhoV), flush=True)
def sample_eta(eta_max):
    while True:
        e = rng.random()*eta_max
        if rng.random() < np.sinh(e)**2/np.sinh(eta_max)**2: return e
print("(b) Haar-ball-averaged L7")
for eta_max in (1.5, 3.0):
    rows = []
    for T in (13, 27, 54, 108):
        ns = 1000 if T < 100 else 400
        if eta_max > 2 and T > 100: ns = 250
        Ns = np.empty(ns)
        for i in range(ns):
            e = sample_eta(eta_max); v = rng.normal(size=3); v /= np.linalg.norm(v)
            Ns[i] = count_diamond_dir(T, e, v, s7, rng.random(4))
        rhoV = np.pi*T**4/24/s7
        print("   eta_max=%.1f T=%3d  Var/rhoV=%.4e (+-%.0f%%)  Var/T^2=%.4f" % (eta_max, T, Ns.var(ddof=1)/rhoV, 100*np.sqrt(2/(ns-1)), Ns.var(ddof=1)/T**2), flush=True)
        rows.append((T, Ns.var(ddof=1)))
    rows = np.array(rows)
    print("   -> eta_max=%.1f: Var ~ T^%.2f (all), T^%.2f (last 3)" % (eta_max, np.polyfit(np.log(rows[:,0]), np.log(rows[:,1]),1)[0], np.polyfit(np.log(rows[1:,0]), np.log(rows[1:,1]),1)[0]), flush=True)
print("elapsed %.0f s" % (time.time()-t0))
