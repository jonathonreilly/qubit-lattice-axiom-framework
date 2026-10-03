"""Toy 4 (planar): event-rate profile between a flat jam slab and a bath, 2D Lx x Ly periodic (no formation).
usage: python3 toy4_planar.py g rho_inf nseeds [Lx] [Ly] [T]
Geometry along x (periodic): jam slab of width 16 centred at x=0, bath of width 16 centred at x=Lx/2,
two media of width (Lx-32)/2 in between. Bath redrawn i.i.d. at rho_inf every tick.
Profiles vs distance d from the nearest slab face (both media folded), averaged over t in [T*0.4, T] and seeds.
Harmonic (flux-carrying) prediction in this geometry: linear in d. Screened prediction: A + B exp(-d/xi).
"""
import sys, time
import numpy as np
from scipy.optimize import curve_fit
from t1lib import move_phase
g = float(sys.argv[1]); rinf = float(sys.argv[2]); ns = int(sys.argv[3])
Lx = int(sys.argv[4]) if len(sys.argv) > 4 else 96
Ly = int(sys.argv[5]) if len(sys.argv) > 5 else 128
T = int(sys.argv[6]) if len(sys.argv) > 6 else 2000
x = np.arange(Lx)
xs = np.minimum(x, Lx - x)            # distance from slab centre (x=0), periodic
slab = xs < 8
bath = np.abs(x - Lx // 2) < 8
med = ~slab & ~bath
d = np.where(med, xs - 7, -1)         # d = 1 for the first medium column next to the slab face
dmax = d.max()
expg = np.exp(g * np.arange(5))
rho_acc = np.zeros(dmax + 1); e_acc = np.zeros(dmax + 1); ncol = np.bincount(d[med], minlength=dmax + 1) * Ly
nacc = 0; slab_mass = []
t0 = time.time()
for seed in range(ns):
    rng = np.random.default_rng(seed + int(1e4 * rinf) + int(10 * g))
    occ = rng.random((Lx, Ly)) < rinf
    occ[slab] = True
    sm = []
    for t in range(1, T + 1):
        occ, out, arr, wins = move_phase(occ, g, rng, expg)
        occ[bath] = rng.random((bath.sum(), Ly)) < rinf
        if t >= int(0.4 * T):
            colr = occ.sum(axis=1); cole = out.sum(axis=1)
            rho_acc += np.bincount(d[med], weights=colr[med], minlength=dmax + 1)
            e_acc += np.bincount(d[med], weights=cole[med], minlength=dmax + 1)
            nacc += 1
        if t % 100 == 0:
            sm.append((t, occ[xs < 12].sum()))
    sm = np.array(sm)
    slab_mass.append(np.polyfit(sm[len(sm) // 3:, 0], sm[len(sm) // 3:, 1], 1)[0])
rho = rho_acc / (ncol * nacc); e = e_acc / (ncol * nacc)
dd = np.arange(dmax + 1)
print(f"g={g} rho_inf={rinf} Lx={Lx} Ly={Ly} T={T} seeds={ns}: medium width {dmax}; slab(+4) mass rate {np.mean(slab_mass):+.4f}"
      f" +- {np.std(slab_mass)/np.sqrt(ns):.4f} /tick (both faces) [{time.time()-t0:.1f}s]")
print("  d   rho(d)    e(d)   moves/record")
for i in list(range(1, 7)) + list(range(8, dmax + 1, 3)):
    print(f"{i:3d} {rho[i]:.5f} {e[i]:.5f} {e[i]/max(rho[i],1e-9):.3f}")
m = (dd >= 6) & (dd <= dmax - 3)
X = dd[m]
for lab_, y in (("rho", rho[m]), ("e", e[m])):
    sig = np.sqrt(np.maximum(y, 1e-5) / (ncol[m] * nacc)) * 5
    out = []
    for name, f, p0 in [("A+B d", lambda x, a, b: a + b * x, (y[0], 0.0)),
                        ("A+B e^-d/xi", lambda x, a, b, xi: a + b * np.exp(-x / xi), (y[-1], y[0] - y[-1], 3.0)),
                        ("A", lambda x, a: a + 0 * x, (y.mean(),))]:
        try:
            p, _ = curve_fit(f, X, y, p0=p0, sigma=sig, maxfev=20000)
            chi = np.sum(((y - f(X, *p)) / sig) ** 2) / (len(X) - len(p))
            out.append(f"{name}: chi2r={chi:.2f} p={np.round(p, 5)}")
        except Exception:
            out.append(f"{name}: fail")
    print(f"fits of {lab_}(d), d in [{X[0]},{X[-1]}]: " + " | ".join(out))
np.savez(f"toy4p_g{g}_rho{rinf}.npz", d=dd, rho=rho, e=e)
