"""Toy 4 (planar v2): event-rate profile next to a flat jam slab, 2D Lx x Ly periodic, no formation.
usage: python3 toy4_planar2.py g mode rho_far nseeds [h_init] [T]
mode 'closed': no bath; vapour pre-seeded at rho_far, slab holes at h_init (zero net flux at coexistence).
mode 'bath'  : bath of width 16 centred at Lx/2; only its central 8 columns are touched: each tick records are added
               at / removed from random core sites to hold the core count at rho_far (rho_far=0: absorbing core).
               The bath's edge columns follow the ordinary dynamics, so the bath keeps natural correlations.
Profiles vs distance d from the nearest slab face, both sides folded, averaged over t in [T/4, T] and seeds.
"""
import sys, time
import numpy as np
from scipy.optimize import curve_fit
from t1lib import move_phase
g = float(sys.argv[1]); mode = sys.argv[2]; rfar = float(sys.argv[3]); ns = int(sys.argv[4])
h_init = float(sys.argv[5]) if len(sys.argv) > 5 else 0.0
T = int(sys.argv[6]) if len(sys.argv) > 6 else 2000
Lx, Ly = 96, 128
x = np.arange(Lx)
xs = np.minimum(x, Lx - x)
slab = xs < 8
if mode == "bath":
    bath = np.abs(x - Lx // 2) < 8
    core = np.abs(x - Lx // 2) < 4
else:
    bath = np.zeros(Lx, bool); core = bath
med = ~slab & ~bath
d = np.where(med, xs - 7, -1); dmax = d.max()
expg = np.exp(g * np.arange(5))
ncol = np.bincount(d[med], minlength=dmax + 1) * Ly
rho_acc = np.zeros(dmax + 1); e_acc = np.zeros(dmax + 1); nacc = 0; rates = []
target = int(round(rfar * core.sum() * Ly))
t0 = time.time()
for seed in range(ns):
    rng = np.random.default_rng(seed + 77 + int(1e4 * rfar) + int(10 * g))
    occ = rng.random((Lx, Ly)) < rfar
    occ[slab] = rng.random((slab.sum(), Ly)) >= h_init
    sm = []
    for t in range(1, T + 1):
        occ, out, arr, wins = move_phase(occ, g, rng, expg)
        if mode == "bath":
            cv = occ[core]                      # view copy of core columns
            n = cv.sum()
            if n > target:
                idx = np.flatnonzero(cv); rm = rng.choice(idx, n - target, replace=False); cv.flat[rm] = False
            elif n < target:
                idx = np.flatnonzero(~cv); ad = rng.choice(idx, target - n, replace=False); cv.flat[ad] = True
            occ[core] = cv
        if t >= T // 4:
            colr = occ.sum(axis=1); cole = out.sum(axis=1)
            rho_acc += np.bincount(d[med], weights=colr[med], minlength=dmax + 1)
            e_acc += np.bincount(d[med], weights=cole[med], minlength=dmax + 1)
            nacc += 1
        if t % 100 == 0:
            sm.append((t, occ[xs < 10].sum()))
    sm = np.array(sm)
    rates.append(np.polyfit(sm[len(sm) // 4:, 0], sm[len(sm) // 4:, 1], 1)[0])
rho = rho_acc / (ncol * nacc); e = e_acc / (ncol * nacc)
dd = np.arange(dmax + 1)
print(f"g={g} mode={mode} rho_far={rfar} h_init={h_init} T={T} seeds={ns}: medium width {dmax}; slab(+2 cols) mass rate "
      f"{np.mean(rates):+.4f} +- {np.std(rates)/np.sqrt(ns):.4f}/tick [{time.time()-t0:.1f}s]")
print("  d   rho(d)    e(d)   moves/record")
for i in list(range(1, 7)) + list(range(8, dmax + 1, 3)):
    print(f"{i:3d} {rho[i]:.5f} {e[i]:.5f} {e[i]/max(rho[i],1e-9):.3f}")
m = (dd >= 6) & (dd <= dmax - 3)
X = dd[m]
for lab_, y in (("rho", rho[m]), ("e", e[m])):
    sig = np.sqrt(np.maximum(y, 1e-5) / (ncol[m] * nacc)) * 5
    out = []
    for name, f, p0 in [("A+B d", lambda x, a, b: a + b * x, (y[0], 0.0)),
                        ("A", lambda x, a: a + 0 * x, (y.mean(),))]:
        p, _ = curve_fit(f, X, y, p0=p0, sigma=sig, maxfev=20000)
        chi = np.sum(((y - f(X, *p)) / sig) ** 2) / (len(X) - len(p))
        out.append(f"{name}: chi2r={chi:.2f} p={np.round(p, 5)}")
    # slope with naive SE from residual scatter
    A = np.vstack([np.ones_like(X), X]).T; coef, res_, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef; se = np.sqrt(resid.var(ddof=2) / ((X - X.mean()) ** 2).sum())
    print(f"fits of {lab_}(d), d in [{X[0]},{X[-1]}]: " + " | ".join(out) + f" | slope {coef[1]:+.6f} +- {se:.6f} per site")
np.savez(f"toy4p2_{mode}_g{g}_rho{rfar}.npz", d=dd, rho=rho, e=e)
