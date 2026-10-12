"""Z2 (E): tau-dependence of the low-frequency weight, signed correlation, and bootstrap errors.
For each eps, w0 in {0, 1, 4}: S(w0)/V = tau_c(w0) on an EARLY and a LATE sub-window (2 l_k each), with bootstrap sd;
Re rho(delta) (signed) on the late window vs the node-ladder rho (z2_B); in-band fractions f(Dw) = Dw tau_c/pi, and the
ratio MC tau_c(0) / node-ladder S_n(0)/V.
"""
import numpy as np, sys
res = np.load("z2_B_res.npy", allow_pickle=True).item()
def tauc_window(x, t, lo, hi, w, dt):
    m = x.mean(0); eta = x - m; V = (np.abs(eta)**2).mean(0)
    idx = np.where((t >= lo) & (t <= hi))[0]; L = int(round(1.0/dt)); lags = np.arange(L+1)*dt
    rho = np.zeros(L+1, complex)
    for l in range(L+1):
        ks = idx[idx + l < len(t)]
        rho[l] = ((eta[:, ks]*np.conj(eta[:, ks+l])).mean(0)/np.sqrt(V[ks]*V[ks+l])).mean()
    return 2*np.real(np.trapezoid(rho*np.exp(1j*w*lags), lags)), rho, lags
for tag in ["e1", "e05", "e025", "e0125"]:
    D = np.load("z2_A_%s.npz" % tag); phi = D["phi"]; t = D["tobs"]; W0 = list(D["W0"]); eps = float(D["eps"]); T = float(D["T"]); d = float(D["d"])
    dt = t[1]-t[0]; R = phi.shape[0]; rng = np.random.default_rng(5)
    node = res[(0, eps)]
    print("=== eps=%g (R=%d): node-ladder S_n(0)/V = %.4f ; windows early [%.2f,%.2f] late [%.2f,%.2f]" % (eps, R, node["S0"], T-4, T-2, T-2, T))
    for w0 in [0.0, 1.0, 4.0]:
        j = W0.index(w0); x = phi[:, :, j] if w0 > 0 else phi[:, :, j].real
        out = []
        for (lo, hi) in [(T-4, T-2), (T-2, T)]:
            tc, rho, lags = tauc_window(x, t, lo, hi, w0, dt)
            bs = [tauc_window(x[rng.integers(0, R, R)], t, lo, hi, w0, dt)[0] for _ in range(30)]
            out.append((tc, np.std(bs), rho, lags))
        (te, se, _, _), (tl, sl, rho, lags) = out
        tau_e = np.sqrt((T-3)**2 - d**2); tau_l = np.sqrt((T-1)**2 - d**2)
        print("  w0=%.0f: S(w0)/V early (tau~%.1f) = %.3f +- %.3f ; late (tau~%.1f) = %.3f +- %.3f ; MC/node(late, w0=0 ref) = %.2f"
              % (w0, tau_e, te, se, tau_l, tl, sl, tl/node["S0"]))
        print("         in-band fraction f = Dw S/(pi V), late: Dw=0.05: %.2e  0.1: %.2e  0.3: %.2e" % (0.05*tl/np.pi, 0.1*tl/np.pi, 0.3*tl/np.pi))
        if w0 == 0:
            sel = [2, 4, 8, 12, 20, 30, 40]
            print("         Re rho(delta) MC late at delta=%s: %s" % (np.array2string(lags[sel], precision=3), np.array2string(rho[sel].real, precision=3)))
            nr = np.interp(lags[sel], node["dl"], node["rho"])
            print("         node-ladder rho(delta) (interp)        : %s" % np.array2string(nr, precision=3))
    sys.stdout.flush()
