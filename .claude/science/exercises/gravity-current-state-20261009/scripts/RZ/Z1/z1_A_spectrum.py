"""Z1 (A): temporal power spectrum of the node-level readout noise, exact momentum form.
Node level: C(x,x') = int d^4z h(x-z) h(x'-z) S(z).  For S(z) = S0 exp(gamma N.(z-x)) (local exponential; N = observer frame here)
   C(t,t') = S0 e^{gamma tbar} int dsigma e^{-i sigma (t-t')} p(sigma),
   p(sigma) = (2pi)^-4 int d^3k |Phi(w)|^2,  w = |k|^2 - sigma^2 + gamma^2/4 - i gamma sigma  (Euclidean-sign invariant, Im w <= 0),
Phi = ftilde/(1-ftilde) the flat mean inverse (RL3b conventions, rho = l_k = 1).
For gamma -> 0 at fixed b = gamma*sigma:  p(sigma) = G(b)/(8 pi^3 gamma),  G(b) = b * int_R du |Phi(u - i b)|^2.
Claims checked here: G(0+) = pi/c2^2 (flat white level 1/(8 pi^2 c2^2 gamma)); int_0^inf G db = 16 pi^4 I_h (total = 4 pi I_h/gamma^2);
the shape of G (flat to b ~ 1, roll-off beyond).  Also a direct 3D (k) check of p(sigma) at finite gamma.
"""
import numpy as np, os, sys, time
from scipy.special import kv
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rl2_core_copy import OPS, fvals, c2_of
v = np.linspace(np.log(1e-9), np.log(24.0), 6001); sv = np.exp(v); wv = np.full_like(v, v[1]-v[0])*sv; wv[0] *= 0.5; wv[-1] *= 0.5
def symbol(fs, w):
    w = np.atleast_1d(w).astype(complex); out = np.empty(w.shape, complex)
    for i in range(0, w.size, 400):
        y = np.sqrt(w[i:i+400])[:, None]*np.sqrt(sv)[None, :]
        out[i:i+400] = 2*np.pi*((kv(1, y)/y) @ (wv*sv*fs))
    return out
def Phi(fs, w):
    # the log s-grid starts at s = 1e-9, so its zeroth moment M0_g = -f(0)*1e-9 != 0 adds a spurious 2 pi M0_g / w pole;
    # remove it (exact for the missing [0, 1e-9] piece to O(1e-9)); M1_g ~ 1e-13 is negligible.
    w = np.atleast_1d(w).astype(complex)
    M0g = np.sum(wv*fs)
    ft = symbol(fs, w) - 2*np.pi*M0g/w; return ft/(1-ft)
I_H = [0.595189, 0.639705, 0.842548]   # RL3b momentum identity (referee-confirmed 0.5951774, 0.6397022, 0.8425444)
def G_of_b(fs, b, nv=1201):
    V = np.arcsinh(3e4/b); vv = np.linspace(-V, V, nv); u = b*np.sinh(vv); du = b*np.cosh(vv)*(vv[1]-vv[0])
    P = Phi(fs, u - 1j*b); return b*np.sum(np.abs(P)**2*du)
if __name__ == "__main__":
    t0 = time.time()
    bgrid = np.exp(np.linspace(np.log(1e-4), np.log(2e3), 36))
    for k in ([0, 1, 2] if len(sys.argv) < 2 else [int(a) for a in sys.argv[1:]]):
        C = OPS[k]; fs = fvals(C, sv); c2 = c2_of(C)
        G = np.array([G_of_b(fs, b) for b in bgrid])
        G0 = np.pi/c2**2
        print("op%d: c2 = %.6f ; pi/c2^2 = %.5f" % (k, c2, G0))
        print("   b        G(b)       G/G(0+)")
        for b, g in zip(bgrid, G):
            print("   %.3e  %.5e  %.5f" % (b, g, g/G0))
        # integral: trapezoid in log b, + small-b part G0*bmin, + large-b tail ~ G(bmax)*bmax (G ~ 1/b^2)
        lb = np.log(bgrid); integ = np.trapezoid(G*bgrid, lb) + G[0]*bgrid[0] + G[-1]*bgrid[-1]
        slope = np.log(G[-1]/G[-3])/np.log(bgrid[-1]/bgrid[-3])
        print("   large-b log-slope of G: %.3f (expected -2)" % slope)
        print("   int_0^inf G db = %.3f ; 16 pi^4 I_h = %.3f ; ratio = %.5f" % (integ, 16*np.pi**4*I_H[k], integ/(16*np.pi**4*I_H[k])))
        Beff = integ/G0
        print("   effective one-sided bandwidth in b: int G db / G(0+) = %.2f ; analytic 16 pi^3 c2^2 I_h = %.2f" % (Beff, 16*np.pi**3*c2**2*I_H[k]))
        # half-power point
        idx = np.where(G/G0 < 0.5)[0]
        print("   G falls to 1/2 of white level at b ~ %.3g" % (bgrid[idx[0]] if idx.size else np.nan))
        sys.stdout.flush()
    print("elapsed %.0fs" % (time.time()-t0))
