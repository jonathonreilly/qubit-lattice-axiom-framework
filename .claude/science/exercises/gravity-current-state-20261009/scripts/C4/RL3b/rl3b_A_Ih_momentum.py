"""RL3b (A): the small-eps rate constant I_h = int_0^inf tau h(tau)^2 dtau, computed EXACTLY in momentum space
(no position-space tail truncation), and cross-checked in position space (RL1 Volterra h, tau <= 16 / 24).

Identity used (derived in the report, sec. 3):  for a retarded Lorentz-invariant h with symbol Phi(w), w = q^2 (Euclidean sign),
    int d^4X e^{-z t} h(X)^2  =  4 pi I_h / z^2 + o(1/z^2),         and
    I_h = (1/(16 pi^4)) int_0^inf b db int_R dsigma |Phi(sigma - i b)|^2 ,
with Phi(w) = ftilde(w)/(1 - ftilde(w)) the flat mean inverse (rho_k = l_k = 1), ftilde the 4D symbol continued off the real axis
(K1 formula with principal sqrt).  Polar coordinates w = r e^{-i theta}: I_h = (1/16 pi^4) int_0^pi sin(theta) dtheta int r^2 dr |Phi|^2.
TEST of the identity on a function with known I: h(s) = exp(-s^2) (s = tau^2): I = int tau e^{-2 tau^4} dtau = sqrt(pi/8)/2.
"""
import numpy as np, os, sys, time
from scipy.special import kv, gammaln
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rl2_core_copy import OPS, fvals, c2_of
# s-quadrature in log variable (resolves s ~ 1/|w| for large |w|)
v = np.linspace(np.log(1e-9), np.log(24.0), 6001); sv = np.exp(v); wv = np.full_like(v, v[1]-v[0])*sv; wv[0] *= 0.5; wv[-1] *= 0.5
def symbol(fs, w):
    """2 pi int s f(s) K1(sqrt(w s))/sqrt(w s) ds for complex w (array), fs = f on sv."""
    w = np.atleast_1d(w).astype(complex); out = np.empty(w.shape, complex)
    for i in range(0, w.size, 200):
        y = np.sqrt(w[i:i+200])[:, None]*np.sqrt(sv)[None, :]
        out[i:i+200] = 2*np.pi*((kv(1, y)/y) @ (wv*sv*fs))
    return out
th_x, th_w = np.polynomial.legendre.leggauss(64)
TH = 0.5*np.pi*(th_x+1); WTH = 0.5*np.pi*th_w
lr = np.linspace(np.log(1e-5), np.log(3e3), 1401); R = np.exp(lr); dl = lr[1]-lr[0]
def Ih_momentum(fs, inverse=True, f0=None):
    tot = 0.0; tail = 0.0
    for t, wt in zip(TH, WTH):
        w = R*np.exp(-1j*t); ft = symbol(fs, w)
        Phi = ft/(1-ft) if inverse else ft
        g = R**3*np.abs(Phi)**2            # r^2 dr = r^3 dl
        tot += wt*np.sin(t)*np.trapezoid(g, dx=dl)
        # analytic large-r tail: |Phi| ~ |ftilde| ~ 8 pi f(0)/r^2  =>  int_Rmax^inf r^2 (8 pi f0)^2/r^4 dr = (8 pi f0)^2/Rmax
        tail += wt*np.sin(t)*(8*np.pi*f0)**2/R[-1]
    return (tot+tail)/(16*np.pi**4), tail/(16*np.pi**4)
if __name__ == "__main__":
    t0 = time.time()
    # (0) test of the identity on h(s) = exp(-s^2)
    fs = np.exp(-sv**2); I_exact = 0.5*np.sqrt(np.pi/8)
    I_m, tl = Ih_momentum(fs, inverse=False, f0=1.0)
    print("TEST h(s)=exp(-s^2): momentum formula I = %.7f (tail %.1e) ; exact sqrt(pi/8)/2 = %.7f ; rel err %.1e" % (I_m, tl, I_exact, I_m/I_exact-1))
    # symbol sanity at small w: 1 - ftilde ~ c2 w
    for k, C in enumerate(OPS):
        fs = fvals(C, sv)
        w0 = np.array([1e-3, 1e-3*np.exp(-1j*np.pi/2), 1e-3*np.exp(-1j*0.99*np.pi)])
        print("op%d: C0=%.6f c2=%.6f ; (1-ftilde)/(c2 w) at |w|=1e-3, arg 0,-pi/2,-0.99pi:" % (k, C[0], c2_of(C)),
              np.round((1-symbol(fs, w0))/(c2_of(C)*w0), 4))
        # zero check of 1 - ftilde on the lower half plane grid (stability): min |1-ftilde|/|w| away from 0
        mins = []
        for t in TH:
            w = R*np.exp(-1j*t); ft = symbol(fs, w); mins.append(np.min(np.abs(1-ft)/np.minimum(np.abs(w), 1.0)))
        I_m, tl = Ih_momentum(fs, inverse=True, f0=C[0])
        print("   I_h (momentum, exact identity) = %.6f  (analytic tail part %.1e) ; k_h = sqrt(4 pi I_h) = %.5f ; min|1-ft|/min(|w|,1) on grid = %.3f"
              % (I_m, tl, np.sqrt(4*np.pi*I_m), min(mins)))
        sys.stdout.flush()
    print("elapsed %.0fs" % (time.time()-t0))
