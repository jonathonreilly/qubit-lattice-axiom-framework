"""RL3 (A): the asymptotic rung constant I_h = int_0^inf tau H_k(tau)^2 dtau of the node-node ladder, for the three
stable L=6 operators (RL2-renormalised), with grid and cutoff convergence.  H_k = flat mean inverse (chains of >=1 hop,
rho_k = 1), from RL1's exact Volterra equation H = f + f*H.  Saves H on the fine grid for (B).
Also prints the bare shared-path constant I_1 for comparison and k = sqrt(4 pi I).
"""
import numpy as np, os, sys, time
from rl2_core import OPS, fvals
RL1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "RL1")
src = open(os.path.join(RL1, "RL1_B_bd_mean_volterra.py")).read().split('if __name__ == "__main__":')[0]
t0 = time.time()
for o, C in enumerate(OPS):
    g = {}; exec(src, g)
    out = {}
    for (hf, h) in [(0.04, 0.08), (0.02, 0.04)]:
        taus, H = g["solve"](lambda s: fvals(C, s), 16.0, hf, h)
        out[hf] = (taus, H)
        Ih = {tm: np.trapezoid((taus*H**2)[taus <= tm], taus[taus <= tm]) for tm in [4, 6, 8, 12, 16]}
        sig = taus**2; W = np.trapezoid(H, sig)
        print("op%d grid hf=%.2f: W=int H dsigma=%.5f ; I_h(tau<=4,6,8,12,16) = %s ; k_h=sqrt(4 pi I_h(16)) = %.4f ; |H| max on [8,16] = %.2e"
              % (o, hf, W, ", ".join("%.5f" % Ih[t] for t in [4, 6, 8, 12, 16]), np.sqrt(4*np.pi*Ih[16]),
                 np.max(np.abs(H[(taus >= 8)])) ), flush=True)
    taus, H = out[0.02]
    np.savez("rl3_H_op%d.npz" % o, taus=taus, H=H)
    u = np.linspace(0, 12, 200001); I1 = np.trapezoid(u*fvals(C, u**2)**2, u)
    print("   op%d bare I_1 = %.5f k_bare = %.4f ; H(0)=f(0)=%.4f, H(1)=%.4f, H(2)=%.4f  (%.0fs)" %
          (o, I1, np.sqrt(4*np.pi*I1), H[0], np.interp(1, taus, H), np.interp(2, taus, H), time.time()-t0), flush=True)
