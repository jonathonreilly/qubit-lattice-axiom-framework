"""Toy 4 (v2): event-rate profile around a jam in 2D, far field held at rho_inf by a bath at r > Rres.
usage: python3 toy4_profile2.py g rho_inf nseeds [R0] [Rres] [T]
Bath: sites with r > Rres redrawn i.i.d. at rho_inf each tick (numerical stand-in for the far field).
Jam mass = largest 4-connected cluster (sampled every 50 ticks); accretion rate Q from its slope over the 2nd half.
Profiles averaged over the 2nd half and over seeds; fits on the vapour window r in [R0+8, Rres-10].
Prints rho(r), e(r) (moves out per site per tick), moves per record; and harmonic-vs-screened fits of rho(r).
"""
import sys, time
import numpy as np
from scipy import ndimage
from scipy.optimize import curve_fit
from t1lib import move_phase
g = float(sys.argv[1]); rinf = float(sys.argv[2]); ns = int(sys.argv[3])
R0 = float(sys.argv[4]) if len(sys.argv) > 4 else 8.0
Rres = float(sys.argv[5]) if len(sys.argv) > 5 else 56.0
T = int(sys.argv[6]) if len(sys.argv) > 6 else 2000
L = 128
yy, xx = np.meshgrid(np.arange(L), np.arange(L), indexing="ij")
r = np.hypot(xx - L / 2 + 0.5, yy - L / 2 + 0.5)
res = r > Rres
rb = np.floor(r).astype(int); nb = rb.max() + 1
cnt = np.bincount(rb.ravel(), minlength=nb)
expg = np.exp(g * np.arange(5))
rho_acc = np.zeros(nb); e_acc = np.zeros(nb); nacc = 0; Qs = []; m0 = []; m1 = []
t0 = time.time()
for seed in range(ns):
    rng = np.random.default_rng(seed + int(1000 * rinf) + int(10 * g))
    occ = rng.random((L, L)) < rinf
    occ[r <= R0] = True
    mass = []
    for t in range(1, T + 1):
        occ, out, arr, wins = move_phase(occ, g, rng, expg)
        occ[res] = rng.random(res.sum()) < rinf
        if t > T // 2:
            rho_acc += np.bincount(rb.ravel(), weights=occ.ravel().astype(float), minlength=nb)
            e_acc += np.bincount(rb.ravel(), weights=out.ravel().astype(float), minlength=nb)
            nacc += 1
        if t % 50 == 0:
            lab, n = ndimage.label(occ & (r <= Rres))
            c = np.bincount(lab.ravel()); c[0] = 0
            mass.append((t, c.max()))
    mass = np.array(mass)
    Qs.append(np.polyfit(mass[len(mass) // 2:, 0], mass[len(mass) // 2:, 1], 1)[0])
    m0.append(mass[0, 1]); m1.append(mass[-1, 1])
rho = rho_acc / (cnt * nacc); e = e_acc / (cnt * nacc)
rad = np.arange(nb) + 0.5
print(f"g={g} rho_inf={rinf} R0={R0} Rres={Rres} T={T} seeds={ns}: jam mass {np.mean(m0):.0f}->{np.mean(m1):.0f}; "
      f"accretion Q={np.mean(Qs):+.4f} +- {np.std(Qs)/np.sqrt(ns):.4f} records/tick [{time.time()-t0:.1f}s]")
print("    r   rho(r)    e(r)   moves/record")
show = list(range(0, int(R0) + 6, 2)) + list(range(int(R0) + 6, int(Rres) + 1, 4))
for i in show:
    if i < nb and cnt[i] > 0:
        print(f"{rad[i]:5.1f} {rho[i]:.5f} {e[i]:.5f} {e[i]/max(rho[i],1e-9):.3f}")
m = (rad >= R0 + 8) & (rad <= Rres - 10)
x = rad[m]
for lab_, y in (("rho", rho[m]), ("e", e[m])):
    sig = np.sqrt(np.maximum(y, 1e-5) / (cnt[m] * nacc)) * 5
    out = []
    for name, f, p0 in [("A+B ln r", lambda x, a, b: a + b * np.log(x), (y[-1], 0.0)),
                        ("A+B/r", lambda x, a, b: a + b / x, (y[-1], 0.0)),
                        ("A+B e^-r/xi", lambda x, a, b, xi: a + b * np.exp(-x / xi), (y[-1], (y[0] - y[-1]) * np.e, 3.0))]:
        try:
            p, _ = curve_fit(f, x, y, p0=p0, sigma=sig, maxfev=20000)
            chi = np.sum(((y - f(x, *p)) / sig) ** 2) / (len(x) - len(p))
            out.append(f"{name}: chi2r={chi:.2f} p={np.round(p, 4)}")
        except Exception:
            out.append(f"{name}: fail")
    slope = np.polyfit(np.log(x), y, 1)[0]
    print(f"fits of {lab_}(r) on r in [{x[0]:.1f},{x[-1]:.1f}]: " + " | ".join(out) + f" | d{lab_}/dln r = {slope:+.5f}")
np.savez(f"toy4v2_g{g}_rho{rinf}.npz", rad=rad, rho=rho, e=e, cnt=cnt)
