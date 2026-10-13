"""R18-1 xi fits (pre-registered form): r(q) = S_V(k z)/S_TT(k z) along the axis; xi^2(q) = (1/r - 1)/q^2 at each q
(a single Lorentzian has q-independent xi^2); weighted LSQ of S_V = A/(1 + xi^2 q^2) + B on the axis points (B = 0 and free).
Also gam/q^2 = S_gamma/q^2 at the smallest q (Stillinger-Lovett-type: finite -> screened, -> 0 -> pinch)."""
import numpy as np, sys, glob, pickle
from scipy.optimize import curve_fit
from analyze import channels
def fit(path):
    res = pickle.load(open(path, "rb")); tab = channels(res); L = res['L']
    rows = [tab[("axis", m)] for m in range(1, L//2 + 1)]
    q2 = np.array([r[0] for r in rows]); SV = np.array([r[1]['V'][0] for r in rows]); eV = np.array([max(r[1]['V'][1], 1e-6) for r in rows])
    rr = np.array([r[1]['r'][0] for r in rows]); er = np.array([r[1]['r'][1] for r in rows])
    xi2q = (1/rr - 1)/q2
    try:
        p, cov = curve_fit(lambda q, A, x2: A/(1 + x2*q), q2, SV, p0=[SV[0], 1.0], sigma=eV, maxfev=20000)
        xi2_fit, exi2 = p[1], np.sqrt(cov[1, 1])
    except Exception as e:
        xi2_fit, exi2 = np.nan, np.nan
    # error on xi^2 at q_min from r error
    exq = er[0]/rr[0]**2/q2[0]
    return dict(L=L, bU=res['bU'], E=res['Eb'].mean(), xi2q=xi2q, exq=exq, xi2_fit=xi2_fit, exi2=exi2, r=rr, er=er,
                gq=tab[("axis", 1)][1]['gam'][0]/q2[0], q2=q2, TT=np.array([r[1]['TT'][0] for r in rows]))
if __name__ == "__main__":
    out = []
    for p in sys.argv[1:]:
        d = fit(p)
        print("L=%2d bU=%5.2f E/edge=%.5f  r(qmin)=%.4f+-%.4f  xi^2(q) per axis q: %s (+-%.2f at qmin)  xi^2 fit=%.3f+-%.3f  xi(qmin)=%.3f  xi/L=%.3f  S_gam/q^2(qmin)=%.4f  TT(q): %s"
              % (d['L'], d['bU'], d['E'], d['r'][0], d['er'][0], np.round(d['xi2q'], 3), d['exq'], d['xi2_fit'], d['exi2'],
                 np.sqrt(max(d['xi2q'][0], 0)), np.sqrt(max(d['xi2q'][0], 0))/d['L'], d['gq'], np.round(d['TT'], 3)))
