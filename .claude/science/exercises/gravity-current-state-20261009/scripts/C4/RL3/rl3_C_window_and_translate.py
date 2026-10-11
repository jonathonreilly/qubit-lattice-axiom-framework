"""RL3 (C): (i) the windowed rung constants used by the explicit lower bound: I_h[W] = int_W tau H^2 dtau over
tau-windows where |H| >= h0 (so the node amplitude is bounded below there), c_low[W] = sqrt(4 pi I_h[W]);
(ii) sup|H| (needed by the vertex bound); (iii) translation: sd e-folds n = (c/2) l_P^2 tau / l_k^3 at l_k = 1e-19 m,
tau = sqrt(2 D s) (RL2 B.1), D = 1 Gpc, s = 1.2e4 m; the FAIL threshold c_fail (n = 1 at the bar); l_k needed for n <= 1.
"""
import numpy as np
lP = 1.616255e-35; D = 3.0857e25; s = 1.2e4; lk = 1e-19
tau = np.sqrt(2*D*s + s*s)
X = lP**2*tau/lk**3               # = sqrt(eps) * tau / l_k at the bar
print("tau = %.4e m ; sqrt(eps)*tau/l_k at the bar = %.2f ; eps at the bar = %.3e ; ln(tau/l_k) = %.1f" % (tau, X, (lP/lk)**4, np.log(tau/lk)))
c_fail = 2.0/X
print("FAIL threshold on the variance-rate constant c (n = (c/2) X >= 1): c_fail = %.5f" % c_fail)
for o in range(3):
    d = np.load("rl3_H_op%d.npz" % o); t, H = d["taus"], d["H"]
    Ih = np.trapezoid(t*H**2, t); supH = np.max(np.abs(H))
    print("op%d: I_h = %.5f  c* = sqrt(4 pi I_h) = %.4f ; sup|H| = %.4f" % (o, Ih, np.sqrt(4*np.pi*Ih), supH))
    for h0 in [0.05, 0.1, 0.3]:
        m = np.abs(H) >= h0
        IW = np.trapezoid(np.where(m, t*H**2, 0.0), t)
        print("    window |H| >= %.2f : I_h[W] = %.4f  c_low = %.4f  (c_low/c_fail = %.0f)" % (h0, IW, np.sqrt(4*np.pi*IW), np.sqrt(4*np.pi*IW)/c_fail))
    m = t <= 0.6; IW = np.trapezoid(np.where(m, t*H**2, 0.0), t)
    print("    window tau <= 0.6 (min|H| there = %.3f): I_h[W] = %.4f  c_low = %.4f  (c_low/c_fail = %.0f)" % (np.min(np.abs(H[m])), IW, np.sqrt(4*np.pi*IW), np.sqrt(4*np.pi*IW)/c_fail))
    for c in [np.sqrt(4*np.pi*Ih), np.sqrt(4*np.pi*IW)]:
        n = 0.5*c*X; lk_need = (0.5*c*lP**2*tau)**(1/3)
        print("    c = %.4f: sd e-folds at the bar n = %.1f ; l_k needed for n <= 1: %.3e m (%.2f x bar, %.2f decades)" % (c, n, lk_need, lk_need/lk, np.log10(lk_need/lk)))
print("\nTheorem 3 constants (cone-alternation costs a factor 4 in the rung): c_low[W] = sqrt(pi I_h[W]) = sqrt(4 pi I_h[W])/2")
for o in range(3):
    d = np.load("rl3_H_op%d.npz" % o); t, H = d["taus"], d["H"]
    for name, m in [("|H|>=0.3", np.abs(H) >= 0.3), ("tau<=0.6", t <= 0.6)]:
        IW = np.trapezoid(np.where(m, t*H**2, 0.0), t); c = np.sqrt(np.pi*IW)
        n = 0.5*c*X; lk_need = (0.5*c*lP**2*tau)**(1/3)
        print("  op%d W=%-9s c_low = %.4f (c_low/c_fail = %.0f): sd e-folds at the bar n = %.1f ; l_k needed %.3e m (%.2f x bar)"
              % (o, name, c, c/c_fail, n, lk_need, lk_need/lk))
print("\nPrefactor estimate (SUGGESTED; point-to-point kernel, renewal pole => Var ~ Lam m^(1/2) e^(m tau)/(4 pi sqrt(2 pi) tau^(3/2)), m = c sqrt(eps)):")
for c in [2.7317, 1.176, 0.717]:
    m = c*(lP/lk)**2; T = tau/lk; Lam = c*c
    lnV = m*T + 0.5*np.log(m) - 1.5*np.log(T) + np.log(Lam/(4*np.pi*np.sqrt(2*np.pi)))
    print("  c = %.4f: m tau = %.1f ; ln Var ~ %.1f (sd e-folds ~ %.1f) on the unit scale of the l_k-normalised kernel" % (c, m*T, lnV, lnV/2))
