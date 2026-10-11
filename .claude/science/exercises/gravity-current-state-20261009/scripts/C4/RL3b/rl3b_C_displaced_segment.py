"""RL3b (C): Lemma D check -- the pair propagator with displaced endpoints loses the hyperboloid factor.
   W(Delta; z) = int d^4X e^{-z t} h(X + Delta) h(X),   Delta = (D0, Dx, 0, 0) in the lab frame of e^{-zt}.
Exact reduction (axial symmetry; X = (t, r, theta, phi), sigma = tau^2(X), c = cos theta):
   d^4X = pi r dt dsigma dc ;  int dc h~(sigma') = [Hc(s0 + 2 r Dx) - Hc(s0 - 2 r Dx)]/(2 r Dx),  s0 = sigma + 2 t D0 + D0^2 - Dx^2,
   Hc(s) = int_0^s h~ (0 for s < 0);  Dx = 0: int dc h~ = 2 h~(sigma + 2 t D0 + D0^2).
Prediction: Delta = 0 -> z^2 W -> 4 pi I_h ;  spacelike Delta -> z W -> (pi/(2|Dx|)) (int h~ dsigma)^2 (finite), i.e. 1/z not 1/z^2;
timelike -> W = O(ln 1/z).  h from rl3b_B (op0).
"""
import numpy as np, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
d = np.load(os.path.join(HERE, "rl3b_h_op0.npz")); taus, H = d["taus"], d["H"]
sg = np.concatenate([np.linspace(0, 16, 1601)[:-1], np.linspace(16, 256, 1201)])     # sigma grid
ht = np.interp(np.sqrt(sg), taus, H)
Hc_tab = np.concatenate([[0], np.cumsum(0.5*(ht[1:]+ht[:-1])*np.diff(sg))]); Htot = Hc_tab[-1]
def Hc(s): return np.where(s <= 0, 0.0, np.interp(s, sg, Hc_tab))
def hti(s): return np.where((s < 0) | (s > 256), 0.0, np.interp(s, sg, ht))
wsg = np.zeros_like(sg); wsg[1:] += 0.5*np.diff(sg); wsg[:-1] += 0.5*np.diff(sg)
def W(D0, Dx, z):
    tmax = 60.0/z; tt = np.unique(np.concatenate([np.linspace(1e-3, 20, 4001), np.geomspace(20, tmax, 3000)]))
    vals = np.zeros_like(tt)
    for i, t in enumerate(tt):
        if t + D0 <= 0: continue
        m = sg < t*t
        s = sg[m]; r = np.sqrt(t*t - s); w = wsg[m]
        s0 = s + 2*t*D0 + D0*D0 - Dx*Dx
        if Dx > 0:
            ang = (Hc(s0 + 2*r*Dx) - Hc(s0 - 2*r*Dx))/(2*r*Dx)
        else:
            ang = 2*hti(s0)
        vals[i] = np.pi*np.sum(w*r*ht[m]*ang)
    return np.trapezoid(np.exp(-z*tt)*vals, tt)
if __name__ == "__main__":
    t0 = time.time()
    Ih = np.trapezoid(taus*H**2, taus)
    print("op0: int h~ dsigma (tau<=16) = %.5f ; 4 pi I_h = %.4f ; predicted z W for spacelike Delta (D0=0, |Dx|=1): pi Htot^2/2 = %.5f" % (Htot, 4*np.pi*Ih, np.pi*Htot**2/2))
    cases = [(0.0, 0.0, "Delta = 0"), (0.0, 1.0, "spacelike (0,1)"), (0.0, 0.5, "spacelike (0,0.5)"), (0.5, 1.0, "spacelike (0.5,1)"),
             (1.0, 1.0, "null (1,1)"), (0.5, 0.0, "timelike (0.5,0)"), (1.0, 0.5, "timelike (1,0.5)")]
    for D0, Dx, lab in cases:
        out = []
        for z in [0.4, 0.2, 0.1, 0.05, 0.025]:
            w = W(D0, Dx, z); out.append("z=%.3f: W=%.4e z^2W=%.4f zW=%.4f" % (z, w, z*z*w, z*w))
        print("  %-20s " % lab + " | ".join(out)); sys.stdout.flush()
    print("elapsed %.0fs" % (time.time()-t0))
