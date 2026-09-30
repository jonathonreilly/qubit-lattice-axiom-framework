import sys, json, numpy as np
from scipy.optimize import curve_fit

def jack(x, f, nb=10):
    """x: (n, ...) samples; f: function of the mean array -> value(s). block jackknife."""
    n = len(x); nb = min(nb, n); bs = n // nb
    xs = x[:bs*nb].reshape((nb, bs) + x.shape[1:])
    tot = xs.sum(axis=(0,1))
    full = f(tot/(nb*bs))
    reps = np.array([f((tot - xs[b].sum(axis=0))/((nb-1)*bs)) for b in range(nb)])
    err = np.sqrt((nb-1)/nb*((reps-reps.mean(axis=0))**2).sum(axis=0))
    return full, err, reps

def creutz(W, R, T):
    return -np.log(W[R,T]*W[R-1,T-1]/(W[R,T-1]*W[R-1,T]))

def analyze_wilson(fn, label, nb=10):
    d = np.load(fn)
    Wu = d['Wu']; Ws = d['Ws']; O = d['O']; plaq = d['plaq']
    dims = d['dims']; Rm = Wu.shape[1]-1
    res = {'label': label, 'dims': dims.tolist(), 'n': int(len(plaq))}
    pm, pe, _ = jack(plaq, lambda m: m, nb)
    res['plaq'] = [float(pm), float(pe)]
    print("\n=== %s  dims=%s  n=%d  plaq=%.5f +- %.5f" % (label, dims.tolist(), len(plaq), pm, pe))
    # symmetrised unsmeared W
    symf = lambda m: 0.5*(m + m.T)
    print("Creutz ratios (unsmeared, symmetrised) chi(R,R):")
    res['chi'] = {}
    for R in range(2, Rm+1):
        v, e, _ = jack(Wu, lambda m: creutz(symf(m), R, R), nb)
        print("  chi(%d,%d) = %.4f +- %.4f" % (R, R, v, e)); res['chi'][str(R)] = [float(v), float(e)]
    # smeared static potential
    for lev in range(Ws.shape[1]):
        print(" smear level index %d (n_APE=%d):" % (lev, d['smear'][lev]))
        Rmax = Ws.shape[2]-1; Tmax = Ws.shape[3]-1
        for Tp in range(1, Tmax):
            row = []
            for R in range(1, Rmax+1):
                v, e, _ = jack(Ws[:, lev], lambda m: np.log(m[R, Tp]/m[R, Tp+1]), nb)
                row.append("%.4f(%.4f)" % (v, e))
            print("   V_eff(R=1..%d; T=%d->%d): " % (Rmax, Tp, Tp+1) + "  ".join(row))
    # force fits: V(R) from T-plateau choices, F(R+1/2)=V(R+1)-V(R), fit sigma + e/r^2 with r=R+1/2
    out = {}
    for lev in range(Ws.shape[1]):
        for Tp in range(2, Ws.shape[3]-1):
            Rmax = Ws.shape[2]-1
            Rlist = list(range(1, min(Rmax, dims[0]//2)+1))
            def fitfun(m, lev=lev, Tp=Tp, Rlist=Rlist):
                V = np.array([np.log(m[R, Tp]/m[R, Tp+1]) for R in Rlist])
                F = V[1:] - V[:-1]; r = np.array(Rlist[:-1]) + 0.5
                # use r >= 1.5 points; linear least squares in (sigma, e): F = sigma + e/r^2
                A = np.vstack([np.ones_like(r), 1.0/r**2]).T
                sol = np.linalg.lstsq(A, F, rcond=None)[0]
                return np.array([sol[0], sol[1]] + list(F))
            v, e, _ = jack(Ws[:, lev], fitfun, nb)
            sig, ee = v[0], v[1]
            print(" fit lev=%d T=%d->%d: sigma=%.4f +- %.4f  sqrt(sigma)=%.4f  e=%.3f +- %.3f ; forces F=%s" %
                  (lev, Tp, Tp+1, sig, e[0], np.sqrt(abs(sig)), ee, e[1], np.round(v[2:], 4)))
            out['lev%d_T%d' % (lev, Tp)] = dict(sigma=float(sig), sigma_err=float(e[0]), e=float(ee), F=[float(x) for x in v[2:]])
    res['force_fits'] = out
    # glueball: connected correlator of O(t)
    Lt = O.shape[2]
    for lev in range(O.shape[1]):
        def corr(m, lev=lev):
            Om = m[lev]  # mean over configs of O(t)? not usable for connected corr -> handled below
            return Om
    # compute C(tau) with jackknife on configs
    for lev in range(O.shape[1]):
        Oc = O[:, lev, :]            # (n, Lt)
        def Cfun(prod_mean):        # prod_mean: (Lt,)  mean over configs of sum_t O(t)O(t+tau)/Lt  ; second: handled via aug array
            return prod_mean
        # build per-config arrays: A_tau = (1/Lt) sum_t O(t)O(t+tau), B = mean_t O(t)
        n = len(Oc)
        A = np.array([[np.mean(Oc[i]*np.roll(Oc[i], -tau)) for tau in range(Lt//2+1)] for i in range(n)])
        B = Oc.mean(axis=1, keepdims=True)
        X = np.hstack([A, B])
        def meff_fun(m, taus=range(0, Lt//2)):
            C = m[:Lt//2+1] - m[-1]**2
            return np.array([np.log(C[t]/C[t+1]) if C[t] > 0 and C[t+1] > 0 else np.nan for t in taus] + [C[0]])
        v, e, _ = jack(X, meff_fun, nb)
        print(" glueball 0++ smear idx %d: m_eff(tau->tau+1) =" % lev, " ".join("%.3f(%.3f)" % (v[t], e[t]) for t in range(Lt//2)), "  C(0)=%.2e" % v[-1])
        res['meff_lev%d' % lev] = [[float(a), float(b)] for a, b in zip(v[:-1], e[:-1])]
    return res

def analyze_pol(fn):
    d = np.load(fn)
    P = d['polyak']; Pa = d['polyak_abs']; dims = d['dims']
    th = np.angle(P)
    # sector: nearest of 0, +-2pi/3
    nP = np.abs(P)
    z3 = np.real(P**3)/np.maximum(nP**3, 1e-30)
    lab = "%dx%dx%dx%d" % tuple(dims)
    r = dict(dims=dims.tolist(), absP_spatial_avg_of_abs=float(Pa.mean()), abs_of_spatial_avg=float(nP.mean()),
             rms_P=float(np.sqrt((nP**2).mean())), cos3theta=float(z3.mean()), n=int(len(P)),
             frac_gt_0p25=float((nP > 0.25).mean()))
    # sector histogram of phases for configs with |P|>0.1
    sel = nP > 0.05
    ph = np.mod(th[sel] + np.pi/3, 2*np.pi)  # sector boundaries at +-pi/3, pi
    sectors = np.floor(ph/(2*np.pi/3)).astype(int)
    r['sector_counts'] = np.bincount(sectors, minlength=3).tolist()
    print("%s: <|Pbar|>=%.4f  <|P|>_site=%.4f  <cos3theta>=%.3f  frac(|Pbar|>0.25)=%.3f sector counts (0,+2pi/3,-2pi/3 windows)=%s n=%d" %
          (lab, r['abs_of_spatial_avg'], r['absP_spatial_avg_of_abs'], r['cos3theta'], r['frac_gt_0p25'], r['sector_counts'], r['n']))
    return r

if __name__ == "__main__":
    out = {}
    for fn, lab in (("runs/L4_b6.npz", "4^4"), ("runs/L8_b6.npz", "8^4"), ("runs/L10_b6.npz", "10^4")):
        try:
            out[lab] = analyze_wilson(fn, lab)
        except FileNotFoundError:
            print("missing", fn)
    print("\n=== Polyakov loops (spatial average), beta=6.0")
    for ls in (8, 12):
        for nt in (4, 6, 8, 10):
            try:
                out['pol_L%d_Nt%d' % (ls, nt)] = analyze_pol("runs/pol_L%d_Nt%d.npz" % (ls, nt))
            except FileNotFoundError:
                print("missing pol", ls, nt)
    try:
        out['pol_L10_Nt10'] = analyze_pol("runs/L10_b6.npz")
    except FileNotFoundError:
        pass
    json.dump(out, open("analysis_results.json", "w"), indent=1)
