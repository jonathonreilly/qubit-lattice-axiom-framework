"""Toy 4: event-rate profile around a jam (2D, 128^2, crowd-tilted moves, no formation).
usage: python3 toy4_profile.py g rho_inf [R0] [Rres] [T] [seed]
Jam = disk of radius R0 at the centre (fully recorded). Sites with r > Rres form a reservoir: every tick they are
redrawn i.i.d. at density rho_inf (a numerical stand-in for a far field held at rho_inf).
Measured over the second half of the run, in radial bins of width 1:
  rho(r)  = record density,  e(r) = events (moves out of the site) per site per tick,
  mob(r)  = e(r)/rho(r) = moves per record per tick.
Fits on r in [R0+4, Rres-4]: A + B ln r (2D harmonic), A + B/r (3D-harmonic form), A + B exp(-r/xi) (screened).
Also reports the jam growth (records within R0+1) and the inflow Q estimated from it.
"""
import sys, time
import numpy as np
from scipy.optimize import curve_fit
from t1lib import move_phase
g = float(sys.argv[1]); rinf = float(sys.argv[2])
R0 = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
Rres = float(sys.argv[4]) if len(sys.argv) > 4 else 56.0
T = int(sys.argv[5]) if len(sys.argv) > 5 else 2000
seed = int(sys.argv[6]) if len(sys.argv) > 6 else 1
L = 128
rng = np.random.default_rng(seed)
yy, xx = np.meshgrid(np.arange(L), np.arange(L), indexing="ij")
r = np.hypot(xx - L / 2 + 0.5, yy - L / 2 + 0.5)
jam0 = r <= R0
res = r > Rres
occ = rng.random((L, L)) < rinf
occ[jam0] = True
expg = np.exp(g * np.arange(5))
rb = np.floor(r).astype(int); nb = rb.max() + 1
cnt = np.bincount(rb.ravel(), minlength=nb)
rho_acc = np.zeros(nb); e_acc = np.zeros(nb); nacc = 0
core = []
t0 = time.time()
for t in range(1, T + 1):
    occ, out, arr, wins = move_phase(occ, g, rng, expg)
    occ[res] = rng.random(res.sum()) < rinf
    if t > T // 2:
        rho_acc += np.bincount(rb.ravel(), weights=occ.ravel().astype(float), minlength=nb)
        e_acc += np.bincount(rb.ravel(), weights=out.ravel().astype(float), minlength=nb)
        nacc += 1
    if t % 50 == 0:
        core.append((t, occ[r <= R0 + 1].sum()))
rho = rho_acc / (cnt * nacc); e = e_acc / (cnt * nacc)
rad = np.arange(nb) + 0.5
core = np.array(core)
Q = np.polyfit(core[len(core) // 2:, 0], core[len(core) // 2:, 1], 1)[0]
print(f"g={g} rho_inf={rinf} R0={R0} Rres={Rres} T={T}: jam(+1) records {core[0,1]}->{core[-1,1]}, inflow Q~{Q:.4f}/tick [{time.time()-t0:.1f}s]")
print(" r    rho(r)    e(r)     moves/record")
for i in list(range(0, int(R0) + 4)) + list(range(int(R0) + 4, int(Rres), 4)):
    if cnt[i] > 0 and rad[i] < Rres:
        print(f"{rad[i]:5.1f} {rho[i]:.5f} {e[i]:.5f} {e[i]/max(rho[i],1e-9):.3f}")
m = (rad >= R0 + 4) & (rad <= Rres - 4)
x = rad[m]; y = e[m]; sig = np.sqrt(np.maximum(e[m], 1e-6) / (cnt[m] * nacc)) * 3  # rough, inflated for correlations
def fit(f, p0):
    try:
        p, _ = curve_fit(f, x, y, p0=p0, sigma=sig, maxfev=20000)
        chi = np.sum(((y - f(x, *p)) / sig) ** 2) / (len(x) - len(p))
        return p, chi
    except Exception as ex:
        return None, np.nan
f_log = lambda x, a, b: a + b * np.log(x)
f_inv = lambda x, a, b: a + b / x
f_exp = lambda x, a, b, xi: a + b * np.exp(-x / xi)
for name, f, p0 in [("A+B ln r", f_log, (y[-1], 0.0)), ("A+B/r", f_inv, (y[-1], 0.0)), ("A+B e^{-r/xi}", f_exp, (y[-1], -0.01, 5.0))]:
    p, chi = fit(f, p0)
    print(f"fit {name:14s}: params={np.round(p, 5) if p is not None else None} reduced chi2={chi:.2f}")
np.savez(f"toy4_g{g}_rho{rinf}_s{seed}.npz", rad=rad, rho=rho, e=e, cnt=cnt, core=core)
