"""Z2 (C): spectral analysis of the carrier MC time series (z2_A_*.npz) and finite-tau fits of V.
For each eps and each carrier w0 (complex carrier e^{i w0 t}; noise eta = phi - <phi>):
 (1) mean signal: |<phi>| and its dominant frequency in the late window (checks the carrier is carried by the mean).
 (2) V(t) = E|eta|^2 ; fits ln V = ln A + p ln tau + gamma tau, tau = sqrt(t^2 - d^2) (centre of the edge), and p = 0, -3/2 fixed.
 (3) normalised two-time correlation rho(t,t+delta) = C/sqrt(V V'), averaged over t in the late window; |rho| and its phase
     relative to the carrier phase w0*delta (multiplicative noise on the carrier would give rho ~ e^{i w0 delta} x slow decay).
 (4) tau_c(w) = int rho(delta) e^{-i w delta} d delta (two-sided)  = S(w)/V for the envelope-normalised process;
     in-band fraction (white-noise form) f(Dw) = Dw tau_c(w0)/pi  (complex carrier, one band |w-w0|<Dw).
 (5) direct periodogram of eta/sqrt(V) on the late window (Hann taper): fraction of power with |w - w0| < Dw, near 0, near -w0.
"""
import numpy as np, glob, sys
from scipy.optimize import curve_fit
files = sys.argv[1:] if len(sys.argv) > 1 else sorted(glob.glob("z2_A_e*.npz"))
for fn in files:
    D = np.load(fn); phi = D["phi"]; t = D["tobs"]; W0 = D["W0"]; eps = float(D["eps"]); T = float(D["T"]); d = float(D["d"])
    R, K, nw = phi.shape; dt = t[1]-t[0]
    print("=== %s: eps=%g T=%g d=%g R=%d <n>=%.0f" % (fn, eps, T, d, R, D["ns"].mean()))
    tl = max(d + 1.5, T - 4.0)      # late window start (after the wavefront has passed the observer)
    late = t >= tl
    for j, w0 in enumerate(W0):
        x = phi[:, :, j]
        if w0 == 0: x = x.real
        m = x.mean(0); eta = x - m; V = (np.abs(eta)**2).mean(0)
        sem_m = np.sqrt(V/R)
        # (1) mean
        mm = np.abs(m[late]).mean(); snr_m = np.median(np.abs(m[late])/sem_m[late])
        # (2) fits of V vs tau over the late window
        tau = np.sqrt(np.maximum(t**2 - d**2, 1e-9)); sel = late
        y = np.log(V[sel]); X1 = np.column_stack([np.ones(sel.sum()), tau[sel]]); X2 = np.column_stack([np.ones(sel.sum()), np.log(tau[sel]), tau[sel]])
        b1 = np.linalg.lstsq(X1, y, rcond=None)[0]; b2 = np.linalg.lstsq(X2, y, rcond=None)[0]
        b3 = np.linalg.lstsq(X1, y + 1.5*np.log(tau[sel]), rcond=None)[0]
        # bootstrap over realizations for gamma (p=0)
        rng = np.random.default_rng(1); gb = []
        for _ in range(100):
            idx = rng.integers(0, R, R); Vb = (np.abs(x[idx] - x[idx].mean(0))**2).mean(0)
            gb.append(np.linalg.lstsq(X1, np.log(Vb[sel]), rcond=None)[0][1])
        # (3) normalised correlation averaged over t in late window, lags up to 2.0
        L = int(round(2.0/dt)); lags = np.arange(0, L+1)*dt
        idx_late = np.where(late)[0]
        rho = np.zeros(L+1, complex); cnt = np.zeros(L+1)
        for l in range(L+1):
            ks = idx_late[idx_late + l < K]
            if len(ks) == 0: continue
            c = (eta[:, ks]*np.conj(eta[:, ks+l])).mean(0)/np.sqrt(V[ks]*V[ks+l])
            rho[l] = c.mean(); cnt[l] = len(ks)
        # (4) tau_c(w) = 2 Re int_0^Lmax rho(delta) e^{+i w delta} d delta   [rho(t,t+delta) = E eta(t) eta*(t+delta);
        #     for eta ~ e^{i w0 t}, rho ~ e^{-i w0 delta}, so S(w) at w = w0 is 2 Re int rho e^{+i w delta}]
        def tauc(w):
            return 2*np.real(np.trapezoid(rho*np.exp(1j*w*lags), lags)) - dt*np.real(rho[0])*0  # trapezoid already halves rho[0]
        tc0 = tauc(0.0); tcw = tauc(w0); tcm = tauc(-w0)
        # (5) periodogram on the late window of the envelope-normalised noise
        z = eta[:, late]/np.sqrt(V[late]); n = z.shape[1]; win = np.hanning(n)
        F = np.fft.fft(z*win, axis=1); P = (np.abs(F)**2).mean(0); om = 2*np.pi*np.fft.fftfreq(n, dt)
        Ptot = P.sum()
        def frac(c, Dw): return P[np.abs(om - c) < Dw].sum()/Ptot
        print(" w0=%.1f |mean|~%.3g (median |mean|/sem %.1f)  V(T)=%.3g  rel var V/|mean|^2 (late median)=%.3g" %
              (w0, mm, snr_m, V[-1], np.median(V[late]/np.abs(m[late])**2)))
        print("     fit late window tau in [%.2f,%.2f]: p=0: gamma=%.3f +- %.3f lnA=%.2f | free p: p=%.2f gamma=%.3f lnA=%.2f | p=-3/2: gamma=%.3f lnA=%.2f" %
              (tau[sel][0], tau[sel][-1], b1[1], np.std(gb), b1[0], b2[1], b2[2], b2[0], b3[1], b3[0]))
        print("     |rho(delta)| at delta=0.025,0.05,0.1,0.2,0.3,0.5,1,2: %s" % np.array2string(np.abs(rho[[1, 2, 4, 8, 12, 20, 40, 80]]), precision=3))
        print("     arg rho / (-w0 delta) at delta=0.1,0.3,0.5,1: %s" % (np.array2string(np.angle(rho[[4, 12, 20, 40]])/(-w0*lags[[4, 12, 20, 40]]), precision=2) if w0 > 0 else "-"))
        print("     tau_c(0)=%.4f tau_c(+w0)=%.4f tau_c(-w0)=%.4f [=S(w)/V]; white in-band fraction f(Dw)=Dw tau_c(w0)/pi: Dw=0.1 -> %.4f, 0.3 -> %.4f" %
              (tc0, tcw, tcm, 0.1*tcw/np.pi, 0.3*tcw/np.pi))
        print("     periodogram (late window %.2f l_k, resolution %.2f): frac |w-w0|<1: %.3f  <2: %.3f ; |w|<1: %.3f ; |w+w0|<1: %.3f ; |w|>10: %.3f ; |w|>20: %.3f" %
              (n*dt, 2*np.pi/(n*dt), frac(w0, 1.0), frac(w0, 2.0), frac(0, 1.0), frac(-w0, 1.0), 1 - frac(0, 10.0), 1 - frac(0, 20.0)))
    sys.stdout.flush()
