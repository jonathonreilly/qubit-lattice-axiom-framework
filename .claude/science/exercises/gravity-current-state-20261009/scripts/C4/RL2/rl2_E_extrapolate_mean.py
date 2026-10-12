"""RL2 (E): p -> 0 extrapolation of the needle-order mean magnification ratio M(p) = [hhat_lens/hhat_flat](p)/sqrt(Delta)
(values from rl2_A_mid.out/rl2_A_quarter.out (p=0.03,0.01,0.005; Richardson), *_smallp.out (p=0.002,0.001; Richardson),
 *_tinyp.out (p=5e-4, 2.5e-4; grid q/10 only: ratio grid error ~4e-4 at p=1e-3, but the ABSOLUTE flat value is off by >50% there)).
Also prints the local log-slope of the excess M-1 between successive p.
Fits with a FREE intercept M0 over the 4 smallest p: (a) M0 + a sqrt(p) + b p ; (b) M0 + a p^alpha (alpha free) ; (c) M0 + a sqrt p + b p ln p.
PASS-type outcome: M0 = 1 within the fit spread; link (G-L) would give (nu Delta)^{-1/2} = 0.4857 (mid) / 0.5426 (quarter)."""
import numpy as np, re
from scipy.optimize import curve_fit
def load(mode):
    d = {}
    for fn in ["rl2_A_%s.out" % mode, "rl2_A_%s_smallp.out" % mode, "rl2_A_%s_tinyp.out" % mode]:
        txt = open(fn).read()
        for blk in re.split(r"\n  p=", txt)[1:]:
            p = float(blk.split()[0])
            for o, val in re.findall(r"op(\d):.*?ratio/sqrt\(Delta\)=([\d.]+)", blk): d.setdefault(int(o), {})[p] = float(val)
    return d
for mode in ["mid", "quarter"]:
    d = load(mode)
    for o in range(3):
        P = np.array(sorted(d[o])); M = np.array([d[o][p] for p in P])
        Ps, Ms = P[:4], M[:4]
        ex = M - 1; sl = np.diff(np.log(ex))/np.diff(np.log(P))
        print("%-7s op%d  excess M-1 = %s ; local slopes d ln(M-1)/d ln p = %s" % (mode, o, np.array2string(ex, precision=4), np.array2string(sl, precision=2)))
        fa, _ = curve_fit(lambda p, m0, a, b: m0 + a*np.sqrt(p) + b*p, Ps, Ms)
        fb, _ = curve_fit(lambda p, m0, a, al: m0 + a*p**al, Ps, Ms, p0=[1, 1, 0.6], maxfev=20000)
        fc, _ = curve_fit(lambda p, m0, a, b: m0 + a*np.sqrt(p) + b*p*np.log(p), Ps, Ms)
        print("%-7s op%d  p=%s  M=%s\n          M0: (a) %.4f  (b) %.4f [alpha=%.2f]  (c) %.4f   -> M0 = %.3f +- %.3f"
              % (mode, o, P, np.array2string(M, precision=5), fa[0], fb[0], fb[2], fc[0],
                 np.mean([fa[0], fb[0], fc[0]]), np.ptp([fa[0], fb[0], fc[0]])/2 + abs(M[0]-np.mean([fa[0], fb[0], fc[0]]))*0))
