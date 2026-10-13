"""R18-2 probe (d): minimal stabilizers.
(d1) real singlet S with Higgs portal and VEV w (tree-level threshold, Lebedev / Elias-Miro-Espinosa-Giudice-Lee-Strumia
     2012, comparator RECALLED):  V = lH (|H|^2 - v^2/2)^2 + (lS/4)(S^2 - w^2)^2 + (lHS/2)(|H|^2 - v^2/2)(S^2 - w^2).
     Below m_S: lam_SM = lH - lHS^2/(4 lS);  m_S^2 = 2 lS w^2.  (v, w) is the global tree minimum iff 4 lH lS > lHS^2
     (positive-definite quadratic form in X = |H|^2 - v^2/2, Y = S^2 - w^2)  <=>  lam_SM(m_S) > 0.
     Large-field conditions to M_P: lH > 0, lS > 0, and (lHS >= 0 or 4 lH lS > lHS^2); perturbativity |l| < 4.
(d2) n5 vector-like Dirac 5-plets of mass M_F, no Higgs Yukawa (one-loop gauge shift only; their 2-loop gauge terms
     neglected): a scale-free (chirally protected) alternative.
Inputs RECALLED (PREREG.md)."""
import numpy as np
from smrge import run, lam_eff, MP

Mt0, Mh0, as0 = 172.57, 125.20, 0.1180
LMAX = 4.0


def singlet_ok(mS, lS, lHS, Mt=Mt0, detail=False):
    T, Y = run(Mt, Mh0, as0, mu_max=MP * 1.01, singlet=dict(mS=mS, lS=lS, lHS=lHS), npts=900)
    h = np.exp(T)
    le, le_loc = lam_eff(T, Y)
    below = (h >= 1e3) & (h < mS)
    above = (h >= mS) & (h <= MP)
    ok_below = (le[below].min() > 0) if below.any() else True
    lH, lHSr, lSr = Y[4][above], Y[5][above], Y[6][above]
    # lH large-field: use lambda_eff-type value (SM one-loop correction included) -> le above threshold
    lHe = le[above]
    cop = np.where(lHSr >= 0, True, 4 * lH * lSr > lHSr**2)
    ok_above = (lHe.min() > 0) and (lSr.min() > 0) and cop.all() and (np.abs(Y[4:7, above]).max() < LMAX)
    ok_thr = Y[4][h < mS][-1] > 0 if below.any() else True  # lam_SM(m_S) > 0 <=> global tree minimum at (v, w)
    if detail:
        return dict(ok=ok_below and ok_above and ok_thr, ok_below=ok_below, ok_above=ok_above,
                    lH_min=lHe.min(), lS_MP=lSr[-1], lHS_MP=lHSr[-1], lH_MP=lH[-1], maxc=np.abs(Y[4:7, above]).max())
    return ok_below and ok_above and ok_thr


print("d1. Real-singlet threshold scan (M_t = %.2f, M_h = %.2f, as = %.4f; 2-loop SM + 1-loop singlet):" % (Mt0, Mh0, as0))
lHS_grid = np.round(np.linspace(-0.8, 0.8, 81), 3)
summary = []
for mS in [1e3, 1e5, 1e7, 1e9, 1e10, 1e11, 3e11]:
    for lS in [0.02, 0.05, 0.1, 0.2, 0.3, 0.4]:
        good = [x for x in lHS_grid if singlet_ok(mS, lS, x)]
        if good:
            pos = [x for x in good if x > 0]
            neg = [x for x in good if x < 0]
            s = "lHS in " + (("[%+.2f, %+.2f]" % (min(pos), max(pos))) if pos else "none>0") + (
                ("  and [%+.2f, %+.2f]" % (min(neg), max(neg))) if neg else "")
            dl = [x**2 / (4 * lS) for x in pos]
            s += "  (threshold delta = lHS^2/(4 lS) in [%.3f, %.3f])" % (min(dl), max(dl)) if pos else ""
        else:
            s = "no stable lHS on the grid"
        summary.append((mS, lS, len(good)))
        print("   m_S = %.0e GeV, lS = %.2f : %2d/%d grid points stable; %s" % (mS, lS, len(good), len(lHS_grid), s))

print()
print("   explicit benchmark (checked): m_S = 1e7 GeV, lS = 0.2, lHS = +0.25")
d = singlet_ok(1e7, 0.2, 0.25, detail=True)
print("     ", {k: (round(v, 5) if isinstance(v, float) else v) for k, v in d.items()})
for Mt in [171.5, 172.57, 173.5, 174.5]:
    print("     same benchmark at M_t = %.2f: stable = %s" % (Mt, singlet_ok(1e7, 0.2, 0.25, Mt=Mt)))

print()
print("   window widths at the benchmark (one parameter varied, others fixed):")
lhs_ok = [x for x in np.linspace(0.0, 0.8, 161) if singlet_ok(1e7, 0.2, x)]
print("     lHS (lS=0.2, m_S=1e7): stable for lHS in [%.3f, %.3f] (width %.3f; natural range O(1))" % (min(lhs_ok), max(lhs_ok), max(lhs_ok) - min(lhs_ok)))
ls_ok = [x for x in np.linspace(0.01, 0.6, 119) if singlet_ok(1e7, x, 0.25)]
print("     lS (lHS=0.25, m_S=1e7): stable for lS in [%.3f, %.3f]" % (min(ls_ok), max(ls_ok)))
ms_ok = [x for x in np.logspace(2.5, 12, 77) if singlet_ok(x, 0.2, 0.25)]
print("     m_S (lS=0.2, lHS=0.25): stable for m_S in [%.2e, %.2e] GeV, i.e. log10 width %.1f decades;"
      " in lattice units m_S a in [%.1e, %.1e]" % (min(ms_ok), max(ms_ok), np.log10(max(ms_ok) / min(ms_ok)), min(ms_ok) / MP, max(ms_ok) / MP))

print()
print("d2. Scale-free alternative: n5 vector-like Dirac 5-plets at M_F (no Yukawa), one-loop gauge shift only:")
for MF in [1e3, 1e6, 1e9]:
    for n5 in [2, 4, 6, 8, 10]:
        T, Y = run(Mt0, Mh0, as0, mu_max=MP * 1.01, n5=n5, MF=MF, npts=900)
        h = np.exp(T)
        le, _ = lam_eff(T, Y)
        m = (h >= 1e3) & (h <= MP)
        ok_pert = np.all(np.isfinite(Y[:5, m])) and np.abs(Y[:3, m]).max() < 3.0
        print("   M_F = %.0e, n5 = %2d : min lambda_eff = %+.5f at h = %.1e ; g(M_P) = (%.3f, %.3f, %.3f) yt(M_P) = %.3f ; %s"
              % (MF, n5, le[m].min(), h[m][np.argmin(le[m])], Y[0][m][-1], Y[1][m][-1], Y[2][m][-1], Y[3][m][-1],
                 "STABLE" if (le[m].min() > 0 and ok_pert) else ("non-perturbative" if not ok_pert else "metastable")))
