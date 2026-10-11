"""RL2 (D): (1) fit the MC sd growth rates of the fixed-source field (rl2_B outputs) vs the bare-ladder predictions (rl2_C);
(2) physical translation with the Lorentz-invariant growth variable (proper time), vs RL1's coordinate-distance translation.
(1) uses the printed sd values; error bars from the sd of a log-normal-ish sample are not available here, so the fit is
    an unweighted least-squares slope of ln sd(phi) over the last 4 T values, plus the last-3 slope as a spread estimate.
(2) z_var = k sqrt(eps)/l_k = k l_P^2/l_k^3 (small-eps ladder law, k = sqrt(4 pi I1) = 2.84..3.33; node ladder 2.73..3.25).
    By exact Poincare invariance in law, the field covariance from a source of rest-frame extent s at null distance D depends on
    the invariants of (x, y, y') only; the largest proper time between a source event and x is tau_max = sqrt(2 D s + s^2).
    sd e-folds n = z_var tau_max / 2.  RL1 used tau = D.
"""
import numpy as np, re, glob
PRED = {(0, 1.0): 2.488, (0, 0.5): 1.470, (0, 0.25): 0.868, (0, 0.125): 0.536, (1, 0.25): 0.904, (2, 0.25): 0.945}  # bare-ladder sd rates (rl2_C)
print("(1) fixed-source field phi: MC sd growth rate per unit proper time (l_k units)")
for (op, eps) in PRED:
    pred = {eps: PRED[(op, eps)]}
    txt = open("rl2_B_op%d_eps%g.out" % (op, eps)).read()
    rows = re.findall(r"T=\s*([\d.]+).*?phi: mean=([-+.\deE]+) \+- [\d.eE+-]+ sd=([\d.eE+-]+)", txt)
    T = np.array([float(r[0]) for r in rows]); sd = np.array([float(r[2]) for r in rows])
    s4 = np.polyfit(T[-4:], np.log(sd[-4:]), 1)[0]; s3 = np.polyfit(T[-3:], np.log(sd[-3:]), 1)[0]
    print("   op%d eps=%-6g T=%s  sd=%s\n      slope(last4)=%.3f slope(last3)=%.3f  ladder-predicted sd rate %.3f  MC/ladder=%.2f..%.2f ; law sqrt(eps)*%.3f"
          % (op, eps, T, np.array2string(sd, precision=3), s4, s3, pred[eps], s4/pred[eps], s3/pred[eps], 0.5*2.8446*np.sqrt(eps)))
lP = 1.616255e-35; Gpc = 3.0857e25
print("\n(2) translation (D = 1 Gpc).  sd e-folds n = k l_P^2 tau/(2 l_k^3);  bounded (n<=1) needs l_k >= (k l_P^2 tau/2)^(1/3)")
for k in [2.73, 2.84, 3.33]:
    for lab, s in [("RL1 (tau = D)", None), ("s = 1.2e4 m (E1'-b source scale)", 1.23e4), ("s = 3e6 m (one 100 Hz cycle)", 3e6), ("s = 3e10 m (100 s of emission)", 3e10)]:
        tau = Gpc if s is None else np.sqrt(2*Gpc*s + s*s)
        n19 = k*lP**2*tau/(2*1e-57); lk = (k*lP**2*tau/2)**(1/3)
        print("   k=%.2f %-34s tau=%.2e m: sd e-folds at l_k=1e-19 m: %.2e ; needs l_k >= %.2e m (= %.1f x bar)" % (k, lab, tau, n19, lk, lk/1e-19))
k = 2.84; tau_bar = 2*1e-57/(k*lP**2)
print("   at the bar l_k = 1e-19 m (k=2.84): noise bounded only for tau <= %.2e m, i.e. D <= tau^2/(2s) = %.2e m (%.1f kpc) for s = 1.2e4 m"
      % (tau_bar, tau_bar**2/(2*1.23e4), tau_bar**2/(2*1.23e4)/3.0857e19))
print("   factor by which k*tau must shrink for PASS at the bar (s=1.2e4 m): %.0f" % ((((k*lP**2*np.sqrt(2*Gpc*1.23e4)/2)**(1/3))/1e-19)**3))
