"""QMC-1 analysis: binning errors, mirror-gap fits (jackknife over bins), structure factors.

    python3 analysis.py runs/a.npz [runs/b.npz ...]
"""
import sys
import numpy as np
from scipy.optimize import curve_fit


def binned(x, nbins=20):
    """mean and binning error of a series (axis 0 = sweeps); also returns errors at 1/4 and 1/2 of the bin count
    (stable error = autocorrelation captured)."""
    x = np.asarray(x, float)
    x = x[~np.isnan(x).any(axis=tuple(range(1, x.ndim)))] if x.ndim > 1 else x[~np.isnan(x)]
    n = len(x)
    out = []
    for nb in (nbins * 4, nbins * 2, nbins):
        nb = max(2, min(nb, n))
        m = n // nb
        b = x[: nb * m].reshape((nb, m) + x.shape[1:]).mean(1)
        out.append((b.mean(0), b.std(0, ddof=1) / np.sqrt(nb), b))
    return out[-1][0], out[-1][1], out


def jack_bins(x, nbins=20):
    x = np.asarray(x, float)
    n = len(x); m = n // nbins
    b = x[: nbins * m].reshape((nbins, m) + x.shape[1:]).mean(1)
    tot = b.sum(0)
    return (tot[None] - b) / (nbins - 1), b.mean(0)


def cosh_fit(tau, g, beta, lo=1.0):
    sel = (tau >= lo - 1e-9) & (tau <= beta - lo + 1e-9)
    f = lambda t, A, D: A * np.cosh(D * (t - beta / 2))
    try:
        p, _ = curve_fit(f, tau[sel], g[sel], p0=[max(g[sel].min(), 1e-6), 0.5], maxfev=20000)
        return abs(p[1]), p[0]
    except Exception:
        return np.nan, np.nan


def wcosh_fit(tau, g, err, beta, lo=0.4):
    sel = (tau >= lo - 1e-9) & (tau <= beta - lo + 1e-9)
    f = lambda t, A, D: A * np.cosh(D * (t - beta / 2))
    e = np.maximum(err[sel], 1e-6)
    try:
        p, _ = curve_fit(f, tau[sel], g[sel], p0=[max(g[sel].min(), 1e-4), 1.0], sigma=e, absolute_sigma=True,
                         maxfev=20000)
        return abs(p[1])
    except Exception:
        return np.nan


def gap_e2(tau, G, beta, nbins=20, lo=0.4):
    """E2 (PREREG follow-up D): weighted cosh fit on [0.4, beta-0.4], jackknife over bins."""
    J, full = jack_bins(G, nbins)
    _, err, _ = binned(G, nbins)
    d0 = wcosh_fit(tau, full, err, beta, lo)
    dj = np.array([wcosh_fit(tau, j, err, beta, lo) for j in J]); dj = dj[~np.isnan(dj)]
    e = np.sqrt((len(dj) - 1) / len(dj) * np.sum((dj - dj.mean()) ** 2)) if len(dj) > 2 else np.nan
    return d0, e


def weight_bound(tau, G, beta, nbins=20, E=1.0):
    """E3: low-energy mirror spectral weight bound w_E = 2 cosh(beta E / 2) G(beta/2)."""
    i = int(np.argmin(np.abs(tau - beta / 2)))
    m, e, _ = binned(G[:, i], nbins)
    c = 2 * np.cosh(beta * E / 2)
    return c * m, c * e


def weight_bound_window(tau, G, beta, nbins=20, E=1.0, lo=1.0):
    """E3w: w_E <= 2 cosh(beta E / 2) * mean_{tau in [lo, beta-lo]} G(tau)  (A >= 0, kernel >= 1/(2cosh(beta E/2)))."""
    sel = (tau >= lo - 1e-9) & (tau <= beta - lo + 1e-9)
    m, e, _ = binned(G[:, sel].mean(1), nbins)
    c = 2 * np.cosh(beta * E / 2)
    return c * m, c * e


def gap(tau, G, beta, nbins=20, lo=1.0):
    """G: (sweeps, ntau) mirror propagator; jackknife over bins of the cosh-fit gap."""
    J, full = jack_bins(G, nbins)
    d0, A0 = cosh_fit(tau, full, beta, lo)
    dj = np.array([cosh_fit(tau, j, beta, lo)[0] for j in J])
    dj = dj[~np.isnan(dj)]
    err = np.sqrt((len(dj) - 1) / len(dj) * np.sum((dj - dj.mean()) ** 2)) if len(dj) > 2 else np.nan
    return d0, err, full


def summarize(path, nbins=20, verbose=True):
    z = np.load(path, allow_pickle=True)
    args = eval(str(z["args"]))
    beta = args["beta"]; tau = z["tau"]
    res = dict(path=path, args=args, n=len(z["acc"]), sec=float(z["sec_per_sweep"]))
    N = int(np.prod(args["dims"]))
    S0 = z["SX0"].sum(1) + z["SY0"].sum(1)
    res["S10"], res["S10_err"], lv = binned(S0, nbins)
    res["S10_err_levels"] = [l[1] for l in lv]
    res["S10_over_N"] = res["S10"] / N; res["S10_over_N_err"] = res["S10_err"] / N
    res["SX0"], res["SX0_err"], _ = binned(z["SX0"], nbins)
    res["SY0"], res["SY0_err"], _ = binned(z["SY0"], nbins)
    Spi = z["SXpi"].sum(1) + z["SYpi"].sum(1)
    res["Spi"], res["Spi_err"], _ = binned(Spi, nbins)
    res["WQ"], res["WQ_err"], _ = binned(z["WQ"], nbins)
    if "WQc" in z.files:
        res["WQc"], res["WQc_err"], _ = binned(z["WQc"], nbins)
    if not np.all(np.isnan(z["Ekin"])):
        res["Ekin"], res["Ekin_err"], _ = binned(z["Ekin"], nbins)
    gm = z["gt_mirror"][:, :, :, 0].mean(2)          # s block (psi propagator), averaged over mirror corners
    gmc = z["gt_mirror"][:, :, :, 1].mean(2)         # c block (psi_c hole propagator)
    gl = z["gt_light"][:, :, :, 0].mean(2)
    res["gap"], res["gap_err"], res["Gm"] = gap(tau, gm, beta, nbins)
    res["gap_c"], res["gap_c_err"], _ = gap(tau, gmc, beta, nbins)
    res["gap2"], res["gap2_err"] = gap_e2(tau, gm, beta, nbins)
    res["w1"], res["w1_err"] = weight_bound(tau, gm, beta, nbins)
    res["w1w"], res["w1w_err"] = weight_bound_window(tau, gm, beta, nbins)
    _, res["Gm_err"], _ = binned(gm, nbins)
    res["Gl"], res["Gl_err"], _ = binned(gl, nbins)
    res["light_dev"] = float(np.max(z["light_dev"]))
    res["maxphase"] = float(np.max(z["maxphase"])); res["maxdev"] = float(np.max(z["maxdev"]))
    res["acc"] = float(np.mean(z["acc"]))
    res["tau"] = tau
    if verbose:
        print(f"{path}: n={res['n']} {res['sec']:.2f}s/sweep acc={res['acc']:.2f} W={args['W']} L={args['dims']} {args['filt']}")
        print(f"   S10(Q0) = {res['S10']:.4f} +- {res['S10_err']:.4f} (err at 80/40/20 bins: "
              f"{', '.join(f'{e:.4f}' for e in res['S10_err_levels'])}); S10/N = {res['S10_over_N']:.5f} +- {res['S10_over_N_err']:.5f}")
        print(f"   S(Qpi) = {res['Spi']:.4f} +- {res['Spi_err']:.4f}; WQ = {res['WQ']:.4f} +- {res['WQ_err']:.4f}"
              + (f"; WQ(HS channels) = {res['WQc']:.4f} +- {res['WQc_err']:.4f}" if "WQc" in res else "")
              + (f"; Ekin = {res['Ekin']:.4f} +- {res['Ekin_err']:.4f}" if "Ekin" in res else ""))
        print(f"   per component SX0 {np.round(res['SX0'], 4).tolist()}")
        print(f"   per component SY0 {np.round(res['SY0'], 4).tolist()}")
        print(f"   mirror gap (cosh fit tau in [1, beta-1]) = {res['gap']:.4f} +- {res['gap_err']:.4f}; c-block {res['gap_c']:.4f} +- {res['gap_c_err']:.4f}")
        print(f"   E2 weighted cosh gap [0.4, beta-0.4] = {res['gap2']:.4f} +- {res['gap2_err']:.4f}; "
              f"E3 weight bound w_1 = 2cosh(beta/2) G(beta/2) = {res['w1']:.4f} +- {res['w1_err']:.4f}; "
              f"E3w (window [1, beta-1]) = {res['w1w']:.4f} +- {res['w1w_err']:.4f}")
        print(f"   G_mirror(tau) = {np.round(res['Gm'], 4).tolist()}")
        print(f"   G_light(tau)  = {np.round(res['Gl'], 6).tolist()}  per-config light dev {res['light_dev']:.1e}")
        print(f"   gate(ii) max|phase| {res['maxphase']:.1e}; wrap-vs-fresh max {res['maxdev']:.1e}")
    return res


if __name__ == "__main__":
    for p in sys.argv[1:]:
        summarize(p)
