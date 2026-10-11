"""RL3b (B): flat mean inverse h(tau) (l_k = rho_k = 1; RL1 Volterra solver, tau <= 16) for op0..2, saved to npz;
then the characteristic function of the EXACT second-moment renewal  M2 = K + rho K * M2  restricted to its terms with
coincident endpoints (d = 0):
   Lambda_node(z)  = 4 pi eps int tau^3 h^2 K1(z tau)/(z tau) dtau          (node-node rung rho Hbar^2 = eps h^2; PROVED part)
   Lambda_hopvar(z)= 4 pi eps int tau^3 Var_n[g_eps(n)] K1(z tau)/(z tau)    (exact single-hop variance part of K_c)
Roots z* (variance rate per l_k) of Lambda = 1; sd rate = z*/2.  Small-eps law: z* = sqrt(4 pi I_h eps).
Compared with RL2's fixed-source MC sd rates (rl2_D_rates_and_translation.out).
"""
import numpy as np, os, sys, time
from scipy.special import kv, gammaln
from scipy.optimize import brentq
from scipy.stats import poisson
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rl2_core_copy import OPS, fvals
src = open(os.path.join(HERE, "RL1in", "RL1_B_bd_mean_volterra.py")).read().split('if __name__ == "__main__":')[0]
IH_MOM = [0.595189, 0.639705, 0.842548]       # rl3b_A (momentum-space, exact identity)
MC = {(0, 1.0): (2.034, 1.931), (0, 0.5): (1.297, 1.344), (0, 0.25): (0.683, 0.590), (0, 0.125): (0.403, 0.424),
      (1, 0.25): (0.777, 0.771), (2, 0.25): (0.796, 0.925)}
xg, wg = np.polynomial.legendre.leggauss(600)
def hopvar(C, eps, tau):
    lam = (np.pi/24)*tau**4/eps; out = np.zeros_like(tau)
    for i, l in enumerate(lam):
        if tau[i] > 5.0: continue            # f and all its finite differences are < 1e-20 there (V > 80)
        nmax = int(l + 12*np.sqrt(l+1) + 40); n = np.arange(nmax+1); pn = poisson.pmf(n, l)
        if eps == 1.0:
            g = np.zeros(nmax+1); g[:min(len(C), nmax+1)] = C[:nmax+1]
        else:
            g = sum(C[j]*np.where(n >= j, np.exp(gammaln(n+1)-gammaln(j+1)-gammaln(np.maximum(n-j, 0)+1)+j*np.log(eps)+(n-j)*np.log1p(-eps)), 0.0)
                    for j in range(len(C)))
        m1 = np.sum(pn*g); out[i] = np.sum(pn*g*g) - m1*m1
    return out
if __name__ == "__main__":
    t0 = time.time()
    for o, C in enumerate(OPS):
        g = {}; exec(src, g)
        fn = os.path.join(HERE, "rl3b_h_op%d.npz" % o)
        if os.path.exists(fn):
            d = np.load(fn); taus, H = d["taus"], d["H"]
        else:
            taus, H = g["solve"](lambda s: fvals(C, s), 16.0, 0.02, 0.05)
        np.savez(os.path.join(HERE, "rl3b_h_op%d.npz" % o), taus=taus, H=H)
        Ih_pos = np.trapezoid(taus*H**2, taus)
        print("op%d: I_h position space (tau<=16) = %.6f ; momentum (exact) = %.6f ; diff %.1e ; int h dsigma = %.5f (target 1/(2 pi c2))"
              % (o, Ih_pos, IH_MOM[o], Ih_pos-IH_MOM[o], np.trapezoid(2*taus*H, taus)))
        hs = lambda t: np.interp(t, taus, H)
        T = 8.0*(xg+1); W = 8.0*wg       # tau in [0,16]
        h2 = hs(T)**2
        lam_node = lambda z, eps: 4*np.pi*eps*np.sum(W*T**3*h2*kv(1, z*T)/(z*T))
        for eps in [1.0, 0.5, 0.25, 0.125, 0.05, 0.01, 1e-3]:
            hv = hopvar(C, eps, T)
            lam_hv = lambda z: 4*np.pi*eps*np.sum(W*T**3*hv*kv(1, z*T)/(z*T))
            z_node = brentq(lambda z: lam_node(z, eps) - 1, 1e-5, 60)
            z_both = brentq(lambda z: lam_node(z, eps) + lam_hv(z) - 1, 1e-5, 60)
            law = np.sqrt(4*np.pi*IH_MOM[o]*eps)
            mc = MC.get((o, eps))
            mcs = ("  MC sd rate %.3f/%.3f -> MC/node %.2f/%.2f" % (mc[0], mc[1], mc[0]/(z_node/2), mc[1]/(z_node/2))) if mc else ""
            print("   eps=%-6g var-rate roots: node %.4f  node+hopvar %.4f  law %.4f  (node/law %.3f ; sd node %.3f)%s"
                  % (eps, z_node, z_both, law, z_node/law, z_node/2, mcs))
        sys.stdout.flush()
    print("elapsed %.0fs" % (time.time()-t0))
