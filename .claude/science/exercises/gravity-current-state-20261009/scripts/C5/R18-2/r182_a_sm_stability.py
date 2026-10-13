"""R18-2 probes (a),(b): SM lambda(mu), instability scale, M_t stability bound, tension in sigma.
All inputs RECALLED (see PREREG.md)."""
import numpy as np
from scipy.optimize import brentq
from smrge import run, lam_eff, matching, MP, MPRED

Mh0, as0 = 125.20, 0.1180
Mt0 = 172.57


def profile(Mt, Mh=Mh0, als=as0, loops=2, mu_max=MP):
    T, Y = run(Mt, Mh, als, mu_max=mu_max * 1.01, loops=loops, npts=1500)
    le, le_loc = lam_eff(T, Y)
    return T, Y, le, le_loc


def stats(Mt, Mh=Mh0, als=as0, loops=2, mu_max=MP):
    T, Y, le, _ = profile(Mt, Mh, als, loops, mu_max)
    msk = (T >= np.log(1e3)) & (T <= np.log(mu_max))
    lam = Y[4]
    out = dict(lam_min=lam[msk].min(), mu_lam_min=np.exp(T[msk][np.argmin(lam[msk])]),
               le_min=le[msk].min(), h_le_min=np.exp(T[msk][np.argmin(le[msk])]),
               lam_MP=np.interp(np.log(mu_max), T, lam))
    # instability scales (first zero crossing)
    def first_zero(f):
        idx = np.where((f[:-1] > 0) & (f[1:] <= 0) & (T[:-1] >= np.log(1e3)))[0]
        if len(idx) == 0:
            return np.nan
        i = idx[0]
        return np.exp(T[i] - f[i] * (T[i + 1] - T[i]) / (f[i + 1] - f[i]))
    out['mu_I_lam'] = first_zero(lam)
    out['h_I_eff'] = first_zero(le)
    out['yt_MP'] = np.interp(np.log(mu_max), T, Y[3])
    out['g_MP'] = [np.interp(np.log(mu_max), T, Y[k]) for k in range(3)]
    return out


def Mt_crit(Mh=Mh0, als=as0, loops=2, use_eff=True, mu_max=MP):
    key = 'le_min' if use_eff else 'lam_min'
    return brentq(lambda m: stats(m, Mh, als, loops, mu_max)[key], 168.0, 176.0, xtol=1e-4)


if __name__ == '__main__':
    print("Matching at M_t (Buttazzo NNLO fit, RECALLED), inputs M_t=%.2f M_h=%.2f as=%.4f:" % (Mt0, Mh0, as0))
    print("   gY, g2, g3, yt, lam =", np.round(matching(Mt0, Mh0, as0), 5))
    print()
    print("a1. Central profile (2-loop running, 1-loop lambda_eff), M_P = 1/a = %.4e GeV:" % MP)
    T, Y, le, le_loc = profile(Mt0)
    for mu in [1e3, 1e6, 1e8, 1e9, 1e10, 1e11, 1e12, 1e14, 1e16, 1e17, 1e18, MPRED, MP]:
        t = np.log(mu)
        print("   mu=%.2e  lam=%+.5f  lam_eff(h=mu)=%+.5f  yt=%.4f g3=%.4f g2=%.4f gY=%.4f" % (
            mu, np.interp(t, T, Y[4]), np.interp(t, T, le), np.interp(t, T, Y[3]), np.interp(t, T, Y[2]),
            np.interp(t, T, Y[1]), np.interp(t, T, Y[0])))
    s = stats(Mt0)
    print("   lam_min = %+.5f at mu = %.2e ; lam(M_P) = %+.5f ; lam_eff,min = %+.5f at h = %.2e" % (
        s['lam_min'], s['mu_lam_min'], s['lam_MP'], s['le_min'], s['h_le_min']))
    print("   instability scale: lam(mu)=0 at mu_I = %.2e GeV ; lam_eff(h)=0 at h_I = %.2e GeV" % (s['mu_I_lam'], s['h_I_eff']))
    print()
    # 1-loop running comparison
    s1 = stats(Mt0, loops=1)
    print("   (1-loop running, same matching: lam(M_P) = %+.5f, mu_I = %.2e) -- shows the 2-loop terms act" % (s1['lam_MP'], s1['mu_I_lam']))
    print()
    print("a2. Comparator (RECALLED): Buttazzo et al. 2013 NNLO fit lam(M_Pl) = -0.0143 - 0.0066 dMt + 0.0018 das + 0.0029 dMh")
    for (Mt, Mh, als) in [(173.34, 125.15, 0.1184), (Mt0, Mh0, as0)]:
        bz = -0.0143 - 0.0066 * (Mt - 173.34) + 0.0018 * (als - 0.1184) / 0.0007 + 0.0029 * (Mh - 125.15)
        mine = stats(Mt, Mh, als, mu_max=MP)['lam_MP']
        print("   (Mt,Mh,as)=(%.2f,%.2f,%.4f): mine lam(M_P)=%+.5f  comparator=%+.5f  diff=%+.5f" % (Mt, Mh, als, mine, bz, mine - bz))
    print("   comparator instability scale (RECALLED): ~1e10-1e11 GeV; lam_min ~ -0.015 near 1e17 GeV (R17-7 used these)")
    print()
    print("a3. Absolute-stability bound on M_t (min over h in [1 TeV, M_P] of lambda_eff = 0):")
    mc = Mt_crit()
    mc_l = Mt_crit(use_eff=False)
    mc_red = Mt_crit(mu_max=MPRED)
    print("   M_t,crit(lambda_eff) = %.3f GeV ; M_t,crit(lambda(mu)) = %.3f GeV ; with h_max = reduced M_P: %.3f GeV" % (mc, mc_l, mc_red))
    dMh = (Mt_crit(Mh=Mh0 + 0.5) - Mt_crit(Mh=Mh0 - 0.5)) / 1.0
    das = (Mt_crit(als=as0 + 0.0009) - Mt_crit(als=as0 - 0.0009)) / (2 * 0.0009)
    print("   dMtc/dMh = %.3f ; dMtc/das = %.1f GeV per unit (i.e. %.3f GeV per 0.0009)" % (dMh, das, das * 0.0009))
    # comparator in the same variables (RECALLED): M_h > 129.6 + 2.0 (M_t - 173.35) - 0.5 (as-0.1184)/0.0007 +- 0.3
    bz_mc = 173.35 + (Mh0 - 129.6 + 0.5 * (as0 - 0.1184) / 0.0007) / 2.0
    print("   comparator (RECALLED Buttazzo: M_h > 129.6 + 2.0(M_t-173.35) - 0.5 das +- 0.3_th) -> M_t,crit = %.2f GeV at our M_h, as" % bz_mc)
    print("   comparator (RECALLED Buttazzo text: M_t < 171.36 +- 0.46 GeV at M_h = 125.66 GeV, as = 0.1184); mine there: %.3f" % Mt_crit(Mh=125.66, als=0.1184))
    print()
    print("b. Tension (one-sided Gaussian), n_sigma = (M_t - M_t,crit)/sigma_tot; s_th = 0.30 (declared):")
    s_th = 0.30
    rows = [("PRIMARY PDG2024 direct 172.57+-0.29, amb 0.5", 172.57, 0.29, 0.5),
            ("PDG2024 direct, amb 0.0", 172.57, 0.29, 0.0),
            ("PDG2024 direct, amb 0.3", 172.57, 0.29, 0.3),
            ("PDG2024 direct, amb 1.0", 172.57, 0.29, 1.0),
            ("ATLAS+CMS Run1 172.52+-0.33, amb 0.5", 172.52, 0.33, 0.5),
            ("x-section pole mass 172.4+-0.7 (no extra amb)", 172.4, 0.7, 0.0)]
    for lab, mt, smt, amb in rows:
        sig = np.sqrt(smt**2 + amb**2 + s_th**2 + (dMh * 0.11)**2 + (das * 0.0009)**2)
        n = (mt - mc) / sig
        print("   %-48s sigma_tot=%.3f  n_sigma=%.2f  -> %s" % (lab, sig, n, "beyond 2 sigma" if n > 2 else "within 2 sigma"))
    sig0 = np.sqrt(0.29**2 + s_th**2 + (dMh * 0.11)**2 + (das * 0.0009)**2)
    amb2 = np.sqrt(max(((Mt0 - mc) / 2)**2 - sig0**2, 0))
    print("   ambiguity at which the PRIMARY row reaches exactly 2 sigma: amb = %.2f GeV" % amb2)
    sth2 = np.sqrt(max(((Mt0 - mc) / 2)**2 - 0.29**2 - 0.5**2 - (dMh * 0.11)**2 - (das * 0.0009)**2, 0))
    print("   s_th at which the PRIMARY row (amb 0.5) reaches 2 sigma: s_th = %.2f GeV" % sth2)
