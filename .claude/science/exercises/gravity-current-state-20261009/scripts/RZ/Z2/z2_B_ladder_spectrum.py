"""Z2 (B): the node-ladder prediction for the observer-time noise spectrum.

Node ladder (RL3b Theorem 1 leading part; RL4 lower-bound structure): the k-th chaos amplitude of phi(x) is
   eps^{..} h(x - z1) h(z1 - z2) ... Psi(zk),
and the observer time t enters ONLY through the last rung h(x_t - z1).  So for the envelope-normalised process
eta(t) e^{-gamma t/2} (planar edge, asymptotic renewal M(z) ∝ e^{gamma t_z}) the spectral density is EXACTLY (within the node ladder)
   S_n(w) = eps * int d^3z | hhat_r(gamma/2 - i w) |^2 ,   hhat_r(q) = int du h(sqrt(u^2-r^2)) e^{-q u}
          = eps * int 4 pi r^2 dr | int tau dtau h(tau) e^{-q sqrt(tau^2+r^2)}/sqrt(tau^2+r^2) |^2
and its w-integral /(2 pi) equals Lambda_node(gamma) = 1 at the root (checked below).  Every chaos term is >= 0 and the
Fourier transform touches only the last rung, so S_n(w) is a sum of nonnegative terms (PSD of a positive ladder).
Far field (r >> 1): hhat_r(q) -> e^{-q r} Wh/(2r), Wh = int h dsigma (= 1/(2 pi c2) in the continuum), so
   S_n(w -> 0) -> eps Wh^2 pi / gamma = eps/(4 pi c2^2 gamma)  (small eps),  i.e. S(0)/V = sqrt(eps)*Wh^2*pi/k  (l_k units).
Outputs: node root gamma(eps); S_n(0)/V; the low-frequency fractions F(Omega) = (1/pi) int_0^Omega S_n dw / V;
the normalised two-time correlation rho(delta) (inverse transform), for comparison with the MC (z2_C).
"""
import numpy as np, os, sys, time
from scipy.special import kv
from scipy.optimize import brentq
from rl2_core import OPS, fvals, c2_of
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "RL1", "RL1_B_bd_mean_volterra.py")).read().split('if __name__ == "__main__":')[0]
t0 = time.time()
res = {}
for o in [0, 1, 2]:
    C = OPS[o]; c2 = c2_of(C)
    g = {}; exec(src, g)
    taus, H = g["solve"](lambda s: fvals(C, s), 16.0, 0.02, 0.05)
    Wh = np.trapezoid(H*2*taus, taus)                      # int h dsigma
    Ih = np.trapezoid(taus*H**2, taus)
    # node root: Lambda(z) = eps 4 pi int tau^3 h^2 K1(z tau)/(z tau) dtau = 1
    Lam = lambda z, eps: eps*4*np.pi*np.trapezoid(taus**3*H**2*kv(1, z*taus+1e-300)/(z*taus+1e-300), taus)
    rgrid = np.concatenate([np.linspace(1e-3, 4, 400), np.linspace(4.01, 400, 4000)])
    def Sn(w, gam, eps):
        q = gam/2 - 1j*w
        rt = np.sqrt(taus[None, :]**2 + rgrid[:, None]**2)
        hh = np.trapezoid(taus[None, :]*H[None, :]*np.exp(-q*rt)/rt, taus, axis=1)
        return eps*np.trapezoid(4*np.pi*rgrid**2*np.abs(hh)**2, rgrid)
    print("op%d: c2=%.4f  Wh=int h dsigma=%.5f (1/(2 pi c2)=%.5f)  I_h(tau<=16)=%.5f" % (o, c2, Wh, 1/(2*np.pi*c2), Ih))
    for eps in [1.0, 0.5, 0.25, 0.125, 0.01, 1e-3, 1e-4]:
        gam = brentq(lambda z: Lam(z, eps) - 1, 1e-4, 50)
        S0 = Sn(0.0, gam, eps)
        asym = eps*Wh**2*np.pi/gam
        ws = np.concatenate([np.linspace(0, 2, 41), np.linspace(2.25, 20, 72), np.linspace(21, 200, 180)])
        if eps >= 0.1:
            Ss = np.array([Sn(w, gam, eps) for w in ws])
            tot = np.trapezoid(Ss, ws)/np.pi                     # should be Lambda(gamma) = 1 minus the w>200 tail
            cum = np.concatenate([[0], np.cumsum(0.5*(Ss[1:]+Ss[:-1])*np.diff(ws))])/np.pi
            F = lambda Om: np.interp(Om, ws, cum)
            # rho(delta) = (1/pi) int_0^inf S cos(w delta) dw / V
            dl = np.array([0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0])
            rho = np.array([np.trapezoid(Ss*np.cos(ws*x), ws)/np.pi for x in dl])/tot
            res[(o, eps)] = dict(gam=gam, S0=S0, ws=ws, Ss=Ss, tot=tot, dl=dl, rho=rho)
            print("  eps=%-6g node root gamma=%.4f  S_n(0)/V=%.4f (far-field law %.4f)  int S dw/pi (w<=200)=%.4f  S(w)/S(0) at w=0.5,1,2,4,8: %s"
                  % (eps, gam, S0, asym, tot, np.array2string(np.interp([0.5, 1, 2, 4, 8], ws, Ss)/S0, precision=3)))
            print("     low-freq fraction F(Omega) for Omega = 0.1, 0.3, 1, 2, 4: %s ;  F(0.1)/(0.1 S0/pi)=%.3f"
                  % (np.array2string(np.array([F(x) for x in [0.1, 0.3, 1, 2, 4]])/tot, precision=4), F(0.1)/(0.1*S0/np.pi)))
            print("     predicted normalised two-time correlation rho(delta) at delta=%s: %s" % (dl, np.array2string(rho, precision=3)))
        else:
            print("  eps=%-6g node root gamma=%.5f (law k_h sqrt(eps)=%.5f)  S_n(0)/V=%.5g  far-field law eps*pi*Wh^2/gamma=%.5g  ratio %.3f ; per sqrt(eps): %.4f"
                  % (eps, gam, np.sqrt(4*np.pi*Ih*eps), S0, asym, S0/asym, S0/np.sqrt(eps)))
    sys.stdout.flush()
np.save("z2_B_res.npy", res, allow_pickle=True)
print("elapsed %.0fs" % (time.time()-t0))
