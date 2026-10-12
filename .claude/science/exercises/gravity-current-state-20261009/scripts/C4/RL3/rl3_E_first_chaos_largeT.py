"""RL3 (E): CHECK of Lemma S inside an exact chaos coefficient.  For the kernel H_P(x,y0), tau(y0,x) = T, the exact
first chaos coefficient is a_1(T) = int Gamma(z)^2 d^4z, and by the two-cone parametrisation
   d^4z = (pi r / T) d(tau1^2) d(tau2^2),  r^2 = t^2 - tau2^2,  t = (T^2 + tau2^2 - tau1^2)/(2T),
   cosh th = (T^2 - tau1^2 - tau2^2)/(2 tau1 tau2)   (relative rapidity of the two legs at z).
Gamma = N + rest (script B's vertex function).  Lemma S predicts rest share -> 0 as T grows (the legs' relative
rapidity grows like 2 ln T on the region that carries a_1), while the node part tends to 2 pi I_h^2.
Grid: tau1, tau2 in (0, 3] (Gauss-Legendre in tau^2); the node-only part is also integrated to tau <= min(T,12) (exact
quadrature, no MC) to show the truncation.  Inner integrals: MC, product of two independent estimates (unbiased).
"""
import numpy as np, sys, time
from scipy.special import gammaln
from rl2_core import OPS
import rl3_B_vertex_suppression as B   # reuses run() (vertex function at given tau1, tau2, th); prints its own table on import? no
Hf = B.Hf
d = np.load("rl3_H_op0.npz"); TT, HH = d["taus"], d["H"]
Ih = np.trapezoid(TT*HH**2, TT)
xg, wg = np.polynomial.legendre.leggauss(22)
def grid(smax):
    s = 0.5*smax*(xg+1); w = 0.5*smax*wg; return s, w          # in s = tau^2
def node_only_full(T, tmax):
    s, w = np.polynomial.legendre.leggauss(400); smax = min(T, tmax)**2
    S = 0.5*smax*(s+1); W = 0.5*smax*w; t1 = np.sqrt(S)
    A = 0.0
    for s2, w2 in zip(S, W):
        tt = (T*T + s2 - S)/(2*T); r2 = tt*tt - s2; ok = (r2 > 0) & (t1 + np.sqrt(s2) < T)
        A += w2*np.sum(W[ok]*(np.pi*np.sqrt(r2[ok])/T)*Hf(t1[ok])**2*Hf(np.sqrt(s2))**2)
    return A
t0 = time.time()
print("2 pi I_h^2 (node-only large-T limit of a_1, from g*g -> (4 pi I_h)^2 theta/(8 pi)) = %.4f" % (2*np.pi*Ih**2))
NIN = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
for T in [float(a) for a in (sys.argv[2].split(",") if len(sys.argv) > 2 else ["1.5","2","3","5","8","12"])]:
    S, W = grid(min(3.0, T)**2)
    A_full = 0.0; A_nn = 0.0; A_rest2 = 0.0; ths = []
    for s1, w1 in zip(S, W):
        for s2, w2 in zip(S, W):
            t1, t2 = np.sqrt(s1), np.sqrt(s2)
            if t1 + t2 >= T: continue
            tt = (T*T + s2 - s1)/(2*T); r2 = tt*tt - s2
            if r2 <= 0: continue
            ch = (T*T - s1 - s2)/(2*t1*t2); th = np.arccosh(max(ch, 1.0))
            N, Id, IH, Gd, GH, rest1, _ = B.run(t1, t2, th, n=NIN)
            _, _, _, _, _, rest2, _ = B.run(t1, t2, th, n=NIN)
            wt = w1*w2*np.pi*np.sqrt(r2)/T
            A_full += wt*(N+rest1)*(N+rest2); A_nn += wt*N*N; A_rest2 += wt*rest1*rest2
            ths.append((wt*N*N, th))
    ths = np.array(ths); thm = np.sum(ths[:, 0]*ths[:, 1])/np.sum(ths[:, 0])
    Afull_nn = node_only_full(T, 12.0)
    print("T=%5.1f: a_1(grid tau<=3) = %.4f ; node-only on grid = %.4f ; rest^2 part = %.4f ; cross = %.4f ; share (a_1 - nn)/a_1 = %+.3f ; "
          "node-weighted mean leg rapidity = %.2f ; node-only a_1 with tau<=min(T,12) = %.4f  (%.0fs)"
          % (T, A_full, A_nn, A_rest2, A_full - A_nn - A_rest2, (A_full - A_nn)/A_full, thm, Afull_nn, time.time()-t0), flush=True)
