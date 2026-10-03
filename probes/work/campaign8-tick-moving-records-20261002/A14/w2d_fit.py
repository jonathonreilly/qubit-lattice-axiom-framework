"""A14 check N2d: finite-density coherent dispersion of the 2D conveyor walk with walls,
fit w_eff^2 = v^2 k^2 + M^2 over the axis k-points with k in [0.13, 0.40]; report
v, M, group velocity at k = 0.26, and extinction G.  Usage: L T r m nseed rho"""
import sys, signal, time
import numpy as np
import w2d_walls as W
signal.alarm(58)
L = int(sys.argv[1]); T = int(sys.argv[2]); r = complex(sys.argv[3]); m = float(sys.argv[4])
nseed = int(sys.argv[5]); rho = float(sys.argv[6])
t0 = time.time()
klist = [(n, 0) for n in (4, 5, 6, 7, 8, 10, 12)]
ks = np.array([2*np.pi*n/L for n, _ in klist])
res = []
for s in range(nseed):
    g, om0, nrm = W.run(L, T, rho, r, m, 3000 + s, klist)
    res.append([W.fit(g[j], om0[j], 5) for j in range(len(klist))])
res = np.array(res)
dw = np.nanmean(res[:, :, 0], axis=0); dws = np.nanstd(res[:, :, 0], axis=0)/np.sqrt(nseed)
G = np.nanmean(res[:, :, 1], axis=0)
we = om0 + dw
A = np.vstack([ks**2, np.ones_like(ks)]).T
coef, *_ = np.linalg.lstsq(A, we**2, rcond=None)
v = np.sqrt(coef[0]); M2 = coef[1]
kref = 2*np.pi*8/L
vg = v**2*kref/np.sqrt(v**2*kref**2 + M2)
# jackknife over seeds for v, M2
jv, jm = [], []
for s in range(nseed):
    keep = [i for i in range(nseed) if i != s]
    d = np.nanmean(res[keep, :, 0], axis=0); c, *_ = np.linalg.lstsq(A, (om0+d)**2, rcond=None)
    jv.append(np.sqrt(c[0])); jm.append(c[1])
jv = np.array(jv); jm = np.array(jm)
ev = np.sqrt((nseed-1)*np.var(jv)); em = np.sqrt((nseed-1)*np.var(jm))
print(f"r={r} m={m} rho={rho} L={L} T={T} seeds={nseed}")
print("  k:      " + " ".join(f"{k:.3f}" for k in ks))
print("  dw/rho: " + " ".join(f"{x/rho:+.2f}" for x in dw) + "   (+-" + " ".join(f"{x/rho:.2f}" for x in dws) + ")")
print("  G/rho:  " + " ".join(f"{x/rho:.2f}" for x in G))
print(f"  fit w^2 = v^2 k^2 + M^2: v = {v:.4f} +- {ev:.4f}  (1-v)/rho = {(1-v)/rho:.2f} +- {ev/rho:.2f};  M^2 = {M2:+.2e} +- {em:.1e}  (M^2/rho^2 = {M2/rho**2:+.1f}, M^2/rho = {M2/rho:+.3f})")
print(f"  group velocity at k={kref:.3f}: v_g = {vg:.4f}  (1-v_g)/rho = {(1-vg)/rho:.2f}")
print(f"elapsed {time.time()-t0:.1f}s")
