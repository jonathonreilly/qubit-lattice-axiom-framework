"""NOT RUN at full size (exceeds the 2D/128^2/2000-tick envelope). For the coordinator.

Two 3D checks of the supplied tick toy T1 (t1lib.py), no formation:

  evap   : net loss rate and half-life of a cube jam of side s in an empty L^3 periodic box, with an absorbing
           sphere at radius Rabs (records reaching r > Rabs are deleted: a numerical stand-in for the infinite empty
           grid; flagged, since records are permanent in the framework).
           Prediction (diffusion-limited): Q = 4 pi D rho_v(R) R Rabs/(Rabs - R), D = 1/7, rho_v(g=1.0) ~ 0.012;
           Q grows ~ linearly in R (not ~R^2 as edge-limited leakage would give); half-life ~ N^(2/3).
  profile: event-rate profile around a spherical jam of radius R0 with a number-controlled bath shell
           (Rb1 < r < Rb2, only the shell core is touched); fits e(r) on [R0+4, Rb1-3] to A + B/r and A + B e^(-r/xi).
           Prediction: rho_far = rho_v -> flat (B ~ 0); rho_far > rho_v -> A + B/r with B < 0; rho_far = 0 -> B > 0.

usage (full size, ~1-3 min each on one core, ~200 MB):
  nice -n 10 python3 big3d_evap_profile.py evap 1.0 4 3 48 3000 20     # g s seeds L T Rabs
  nice -n 10 python3 big3d_evap_profile.py evap 1.0 8 3 48 3000 20
  nice -n 10 python3 big3d_evap_profile.py profile 1.0 0.012 2 56 3000 6 22 26   # g rho_far seeds L T R0 Rb1 Rb2
  nice -n 10 python3 big3d_evap_profile.py profile 1.0 0.0   2 56 3000 6 22 26
  nice -n 10 python3 big3d_evap_profile.py profile 1.0 0.02  2 56 3000 6 22 26
"""
import sys, time
import numpy as np
from scipy import ndimage
from scipy.optimize import curve_fit
from t1lib import move_phase

mode = sys.argv[1]; g = float(sys.argv[2])
expg = np.exp(g * np.arange(7))
t0 = time.time()

if mode == "evap":
    s = int(sys.argv[3]); ns = int(sys.argv[4]); L = int(sys.argv[5]); T = int(sys.argv[6]); Rabs = float(sys.argv[7])
    zz, yy, xx = np.meshgrid(*(np.arange(L),) * 3, indexing="ij")
    r = np.sqrt((xx - L / 2 + 0.5) ** 2 + (yy - L / 2 + 0.5) ** 2 + (zz - L / 2 + 0.5) ** 2)
    sink = r > Rabs
    out = []
    for seed in range(ns):
        rng = np.random.default_rng(seed + 100 * s)
        occ = np.zeros((L, L, L), bool); c = L // 2 - s // 2
        occ[c:c + s, c:c + s, c:c + s] = True
        N0 = occ.sum(); half = np.nan; sizes = []
        for t in range(1, T + 1):
            occ, mv, arr, w = move_phase(occ, g, rng, expg)
            occ[sink] = False
            if t % 20 == 0:
                lab, n = ndimage.label(occ)
                cnt = np.bincount(lab.ravel()); cnt[0] = 0
                sizes.append((t, cnt.max() if n else 0))
                if np.isnan(half) and sizes[-1][1] <= N0 / 2: half = t
        sizes = np.array(sizes)
        q = -np.polyfit(sizes[len(sizes) // 4:, 0], sizes[len(sizes) // 4:, 1], 1)[0]
        out.append((q, half, sizes[-1, 1] / N0))
    o = np.array(out)
    R = s * (3 / (4 * np.pi)) ** (1 / 3)
    pred = 4 * np.pi * (1 / 7) * 0.012 * R * Rabs / (Rabs - R)
    print(f"3D evap g={g} s={s} N0={s**3} R~{R:.2f}: net loss {o[:,0].mean():.4f}+-{o[:,0].std()/np.sqrt(ns):.4f}/tick "
          f"(diffusion-limited guess with rho_v=0.012: {pred:.4f}); half-life {np.nanmean(o[:,1]):.0f}; N(T)/N0 {o[:,2].mean():.3f} "
          f"[{time.time()-t0:.0f}s]")

elif mode == "profile":
    rfar = float(sys.argv[3]); ns = int(sys.argv[4]); L = int(sys.argv[5]); T = int(sys.argv[6])
    R0, Rb1, Rb2 = float(sys.argv[7]), float(sys.argv[8]), float(sys.argv[9])
    zz, yy, xx = np.meshgrid(*(np.arange(L),) * 3, indexing="ij")
    r = np.sqrt((xx - L / 2 + 0.5) ** 2 + (yy - L / 2 + 0.5) ** 2 + (zz - L / 2 + 0.5) ** 2)
    shell = (r > Rb1) & (r <= Rb2)
    core = (r > Rb1 + 1) & (r <= Rb2 - 1)
    outside = r > Rb2                      # kept empty and absorbing beyond the shell
    target = int(round(rfar * core.sum()))
    rb = np.floor(r).astype(int); nb = rb.max() + 1
    cnt = np.bincount(rb.ravel(), minlength=nb)
    rho_acc = np.zeros(nb); e_acc = np.zeros(nb); nacc = 0
    for seed in range(ns):
        rng = np.random.default_rng(seed + int(1e4 * rfar))
        occ = (rng.random((L, L, L)) < rfar) & (r <= Rb2)
        occ[r <= R0] = True
        for t in range(1, T + 1):
            occ, mv, arr, w = move_phase(occ, g, rng, expg)
            occ[outside] = False
            cv = occ[core]; n = cv.sum()
            if n > target:
                idx = np.flatnonzero(cv); cv[rng.choice(idx, n - target, replace=False)] = False
            elif n < target:
                idx = np.flatnonzero(~cv); cv[rng.choice(idx, target - n, replace=False)] = True
            occ[core] = cv
            if t > T // 3:
                rho_acc += np.bincount(rb.ravel(), weights=occ.ravel().astype(float), minlength=nb)
                e_acc += np.bincount(rb.ravel(), weights=mv.ravel().astype(float), minlength=nb)
                nacc += 1
    rho = rho_acc / (cnt * nacc); e = e_acc / (cnt * nacc); rad = np.arange(nb) + 0.5
    print(f"3D profile g={g} rho_far={rfar} R0={R0} shell=({Rb1},{Rb2}) [{time.time()-t0:.0f}s]")
    for i in range(0, int(Rb2) + 1):
        if cnt[i]:
            print(f"{rad[i]:5.1f} rho={rho[i]:.5f} e={e[i]:.5f}")
    m = (rad >= R0 + 4) & (rad <= Rb1 - 3)
    X, Y = rad[m], e[m]
    sig = np.sqrt(np.maximum(Y, 1e-5) / (cnt[m] * nacc)) * 5
    for name, f, p0 in [("A+B/r", lambda x, a, b: a + b / x, (Y[-1], 0.0)),
                        ("A+B e^-r/xi", lambda x, a, b, xi: a + b * np.exp(-x / xi), (Y[-1], Y[0] - Y[-1], 3.0)),
                        ("A", lambda x, a: a + 0 * x, (Y.mean(),))]:
        try:
            p, _ = curve_fit(f, X, Y, p0=p0, sigma=sig, maxfev=20000)
            print(f"fit {name}: chi2r={np.sum(((Y - f(X, *p)) / sig) ** 2) / (len(X) - len(p)):.2f} p={np.round(p, 5)}")
        except Exception:
            print(f"fit {name}: fail")
