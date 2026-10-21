#!/usr/bin/env python3
"""Reviewer check: binning / autocorrelation of the L=8 beta=16 energy series (read-only on data/raw)."""
import glob, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
res = {}
for tag in ("L8E_s3", "L8E_s5"):
    fs = sorted(glob.glob(os.path.join(HERE, "..", "data", "raw", tag + "_c*.npz")))
    k = list(np.load(fs[0])["keys"])
    Efull = np.concatenate([np.load(f)["m"][:, 0, k.index("E")] for f in fs])
    E = Efull[int(0.2 * len(Efull)):]
    n = len(E); var = E.var(ddof=1)
    print(f"{tag}: nmeas_total={len(Efull)} after discard={n} mean={E.mean():.3f} naive err={np.sqrt(var/n):.4f}")
    for nb in (2, 3, 4, 5, 6, 8, 10, 14, 20, 40, 80, 160):
        m = n // nb
        b = E[:m*nb].reshape(nb, m).mean(1)
        err = b.std(ddof=1)/np.sqrt(nb)
        print(f"   nb={nb:4d} binlen={m:6d} meas  err={err:.3f}  tau_int~{0.5*err**2*n/var:.0f} meas")
    # integrated autocorrelation (Sokal window)
    x = E - E.mean(); f = np.fft.rfft(x, 2*n); ac = np.fft.irfft(f*np.conj(f))[:n]; ac /= ac[0]
    tau = 0.5
    for W in range(1, n):
        tau += ac[W]
        if W >= 6*tau: break
    print(f"   Sokal tau_int={tau:.0f} meas (window {W}); N/(2tau)={n/(2*tau):.1f} indep; err={np.sqrt(var*2*tau/n):.3f}")
    # chunk means
    cm = [np.load(f)["m"][:, 0, k.index("E")].mean() for f in fs]
    print("   per-chunk means:", [round(c, 2) for c in cm])
    res[tag] = (E.mean(), tau, var, n)
