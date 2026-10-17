"""QMC-1b analysis (PREREG section 6). summarize(path) -> dict.
S10/L^2 with sigma = max(20-bin, 10-bin) binning error over all measured sweeps; E3w primary = mirror propagator
averaged over all mirror corners and all 32 components (s and c blocks), symmetric window tau in [1, beta-1]."""
import os
import numpy as np


def binerr(x, nb):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    n = len(x); nb = max(2, min(nb, n)); m = n // nb
    b = x[: nb * m].reshape(nb, m).mean(1)
    return b.std(ddof=1) / np.sqrt(nb)


def stat(x):
    """mean over all values (NaN rows dropped), sigma = max(error at 20 bins, error at 10 bins)."""
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    return float(x.mean()), float(max(binerr(x, 20), binerr(x, 10))), len(x)


def tau_int(x, c=6.0):
    x = np.asarray(x, float); x = x[~np.isnan(x)] - np.nanmean(x); n = len(x)
    if n < 8 or np.var(x) == 0:
        return np.nan
    ac = np.correlate(x, x, "full")[n - 1:] / (np.var(x) * np.arange(n, 0, -1))
    t = 0.5
    for w in range(1, n // 2):
        t += ac[w]
        if w >= c * t:
            break
    return float(max(t, 0.5))


def summarize(path):
    z = np.load(path, allow_pickle=True)
    a = eval(str(z["args"]))
    beta = a["beta"]; tau = z["tau"]; N = int(np.prod(a["dims"]))
    r = dict(path=os.path.basename(path), filt=a["filt"], L=a["dims"][0], W=a["W"], dtau=a["dtau"], ns=a["ns"],
             n=len(z["acc"]), sec=float(z["sec_per_sweep"]), acc=float(np.mean(z["acc"])) if len(z["acc"]) else np.nan)
    S0 = (z["SX0"].sum(1) + z["SY0"].sum(1)) / N
    r["S"], r["Se"], _ = stat(S0)
    r["tau_int"] = tau_int(S0)
    th = len(S0) // 3
    r["thirds"] = [float(np.mean(S0[i * th:(i + 1) * th])) for i in range(3)] if th > 0 else []
    s910 = z["SX0"][:, 8:].sum(1) + z["SY0"][:, 8:].sum(1)
    r["frac910"] = float(np.mean(s910) / np.mean(S0 * N)) if len(S0) else np.nan
    r["Spi"], r["Spie"], r["nSpi"] = stat((z["SXpi"].sum(1) + z["SYpi"].sum(1)) / N)
    r["WQ"], r["WQe"], _ = stat(z["WQ"] / N)
    gmall = z["gt_mirror"]                                  # (sweeps, ntau, ncorner, 2)
    sel = (tau >= 1.0 - 1e-9) & (tau <= beta - 1.0 + 1e-9)
    c = 2 * np.cosh(beta / 2)
    def e3w(G):
        return stat(c * G[:, sel].mean(1))[:2]
    r["E3w"], r["E3we"] = e3w(gmall.mean(axis=(2, 3)))      # PRIMARY
    r["E3w_s"], r["E3w_se"] = e3w(gmall[:, :, :, 0].mean(2))  # QMC-1 definition (s block)
    if a["filt"] == "fG":
        r["E3w_pp"], _ = e3w(gmall[:, :, 0, :].mean(2)); r["E3w_p0"], _ = e3w(gmall[:, :, 1:, :].mean(axis=(2, 3)))
    elif a["filt"] == "f2":
        r["E3w_00"], _ = e3w(gmall[:, :, 0, :].mean(2)); r["E3w_pp"], _ = e3w(gmall[:, :, 1, :].mean(2))
    r["Gm"] = gmall.mean(axis=(0, 2, 3)) if len(gmall) else None
    r["tau"] = tau
    r["light_dev"] = float(np.max(z["light_dev"])) if len(z["light_dev"]) else np.nan
    r["maxphase"] = float(np.max(z["maxphase"])) if len(z["maxphase"]) else np.nan
    r["maxdev"] = float(np.max(z["maxdev"])) if len(z["maxdev"]) else np.nan
    r["complete"] = r["n"] >= 200
    return r


def load_all(rundir):
    out = {}
    for f in sorted(os.listdir(rundir)):
        if f.startswith("L") and f.endswith(".npz") and "_W0" not in f:
            try:
                r = summarize(os.path.join(rundir, f))
            except Exception as e:
                print(f"skip {f}: {e}")
                continue
            out[(r["filt"], r["L"], r["W"])] = r
    return out


def ratio(r4, r6):
    R = r6["S"] / r4["S"]
    return R, R * np.hypot(r4["Se"] / r4["S"], r6["Se"] / r6["S"])
