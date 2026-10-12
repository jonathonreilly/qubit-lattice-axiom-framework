"""RL2 (A): curved MEAN of the per-sprinkling inverse for the three stable L=6 operators, via the exact mean-inverse identity
E[(I-N)^{-1}] = (I - Nbar)^{-1}, solved on the Penrose-limit (needle-order) geometry of the G-L conformal lens ray.

Reduction (derived in the report, section A):
 * On a plane wave, Hbar(x,y) = h(u_y, u_x, s), s = tau^2 = -2 sigma (isometries). For z in I(y,x) with y, x on the axis,
   d^4z = (2 pi/Lam) g du dsigma1 dsigma2,  g = sqrt(Delta(y,x)/(Delta(y,z)Delta(z,x))), region identical to flat's.
 * Laplace in s: hhat(Lam, p).  With q = p*Lam the recursion closes at fixed q (k(Lam,q) := hhat(Lam, q/Lam)):
     k(Lam,q) = nu(0,Lam)^{-1/2} fhat(q/(Lam sqrt nu(0,Lam)))
              + (pi rho/(2q)) int_0^Lam du g(u;Lam) nu(u,Lam)^{-1/2} fhat(q/((Lam-u) sqrt nu(u,Lam))) k(u,q)
   a 1D Volterra equation in the affine parameter for each q (rho = 1; exact homothety makes the plane-wave answer
   density-independent).  Flat: k(Lam,q) = hhat0(q/Lam), hhat0(0) = W = 1/(2 pi c2)  [checks].
 * Direct (delta(s)) coefficient: W(Lam) = lim_{p->0} hhat(Lam, p).  GR: W/W_flat = Delta^{1/2}; one-hop link: nu^{-1/2}.
 * Conformal lens (G-L lane B): Omega^2 = 1 + A exp(-|x-c|^2/w^2), R = 100, w = 10, A = 3, c = 50 (mid) or 25 (quarter);
   along the ray Delta = <Om^2>^2/(Om_a^2 Om_b^2), nu = <Om^4>_w/<Om^2>^2 (G-L, exact at needle order), affine u = int Om^2 dt.
"""
import numpy as np, sys, time
from scipy.special import erf
from rl2_core import OPS, fhat_factory, c2_of
Rr, Ww = 100.0, 10.0
FH = [fhat_factory(C)[0] for C in OPS]
WT = [1/(2*np.pi*c2_of(C)) for C in OPS]
xg6, wg6 = np.polynomial.legendre.leggauss(8)

class Ray:
    def __init__(self, A, c):
        self.A, self.c = A, c
        tt = np.linspace(0, Rr, 200001)
        self.tt = tt; self.uu = self.u_of_t(tt)
    def om2(self, t): return 1.0 + self.A*np.exp(-(t-self.c)**2/Ww**2)
    def u_of_t(self, t): return t + self.A*Ww*np.sqrt(np.pi)/2*(erf((t-self.c)/Ww) - erf(-self.c/Ww))
    def t_of_u(self, u):
        t = np.interp(u, self.uu, self.tt)
        for _ in range(3): t = t - (self.u_of_t(t) - u)/self.om2(t)
        return t
    def Q(self, ta, tb, a):
        b = a/Ww**2; ya = ta-self.c; yb = tb-self.c; sb = np.sqrt(b)
        I0 = np.sqrt(np.pi)/(2*sb)*(erf(sb*yb)-erf(sb*ya)); ea = np.exp(-b*ya**2); eb = np.exp(-b*yb**2)
        I1 = (ea-eb)/(2*b); I2 = (ya*ea - yb*eb)/(2*b) + I0/(2*b)
        return -I2 + (ya+yb)*I1 - ya*yb*I0
    def nu_Delta(self, ta, tb):
        """ta < tb arrays (broadcast). returns nu, Delta for the ray segment [ta,tb]."""
        ta, tb = np.broadcast_arrays(np.asarray(ta, float), np.asarray(tb, float))
        dt = tb - ta; om2a = self.om2(ta); om2b = self.om2(tb)
        mo2 = np.where(dt > 0, (self.u_of_t(tb)-self.u_of_t(ta))/np.where(dt > 0, dt, 1), om2a)
        Dl = mo2**2/(om2a*om2b)
        big = dt >= 2.0
        num = np.empty_like(dt)
        if big.any():
            num[big] = dt[big]**3/6 + 2*self.A*self.Q(ta[big], tb[big], 1.0) + self.A**2*self.Q(ta[big], tb[big], 2.0)
        sm = ~big
        if sm.any():
            a_, d_ = ta[sm], dt[sm]
            tn = a_[:, None] + 0.5*d_[:, None]*(xg6[None, :]+1); wn = 0.5*d_[:, None]*wg6[None, :]
            num[sm] = np.sum(wn*(tn-a_[:, None])*(a_[:, None]+d_[:, None]-tn)*self.om2(tn)**2, axis=1)
        O4w = np.where(dt > 0, 6*num/np.where(dt > 0, dt, 1)**3, om2a**2)
        return O4w/mo2**2, Dl

def solve(ray, q, delta, uobs):
    N = int(round(uobs/delta)); u = np.linspace(0, uobs, N+1); d = u[1]-u[0]
    t = ray.t_of_u(u)
    nu0, D0 = ray.nu_Delta(np.zeros(N+1), t); nu0[0] = 1; D0[0] = 1
    K = np.zeros((len(OPS), N+1))
    for o in range(len(OPS)):
        K[o, 1:] = nu0[1:]**-0.5*FH[o](q/(u[1:]*np.sqrt(nu0[1:])))
    k = K.copy()   # k[o,i] starts with source term A_i
    k[:, 0] = 0.0
    for i in range(2, N+1):
        j = np.arange(1, i)
        nu, Dl = ray.nu_Delta(t[j], t[i])
        g = np.sqrt(D0[i]/(D0[j]*Dl)); pre = (np.pi/(2*q))*d*g*nu**-0.5
        x = q/((u[i]-u[j])*np.sqrt(nu))
        for o in range(len(OPS)):
            k[o, i] += np.sum(pre*FH[o](x)*k[o, j])
    return u, k, nu0[-1], D0[-1]

if __name__ == "__main__":
    mode = sys.argv[1]
    t0 = time.time()
    if mode == "flat":
        # one solve gives hhat0(p) for all p >= q/Lam_max; compare two (q, Lam) pairs at equal p and the p->0 target
        flat = Ray(0.0, 50.0)
        for (q, uob, fac) in [(0.5, 100.0, 20), (0.25, 50.0, 20), (0.5, 100.0, 40)]:
            u, k, _, _ = solve(flat, q, q/fac, uob)
            print("flat q=%.3f Lam_max=%.0f delta=q/%d (%.0fs):" % (q, uob, fac, time.time()-t0))
            for p in [1.0, 0.3, 0.1, 0.03, 0.01, 0.005]:
                Lam = q/p
                if Lam <= uob: print("   p=%-6g hhat0 = %s" % (p, "  ".join("%+.6f" % np.interp(Lam, u, k[o]) for o in range(3))))
            sys.stdout.flush()
        print("   p->0 targets W = 1/(2 pi c2):", "  ".join("%+.6f" % w for w in WT))
    else:
        A = 3.0; c = 50.0 if mode == "mid" else 25.0
        ray = Ray(A, c); flat = Ray(0.0, 50.0)
        uobs = ray.u_of_t(Rr)
        print("lens %s A=%g: u_obs=%.4f  GR sqrt(Delta)=%.5f  link nu^-1/2=%.5f  G-L link/GR=%.5f" % (mode, A, uobs, np.sqrt(ray.nu_Delta(0.0, Rr)[1]), ray.nu_Delta(0.0, Rr)[0]**-0.5, np.prod(ray.nu_Delta(0.0, Rr))**-0.5))
        PL = [float(a) for a in sys.argv[2].split(',')] if len(sys.argv) > 2 else [0.03, 0.01, 0.005]
        FACS = tuple(int(a) for a in sys.argv[3].split(',')) if len(sys.argv) > 3 else (20, 40)
        for p in PL:
            res = {}
            for fac in FACS:
                qL = p*uobs; qF = p*Rr
                uL, kL, nuL, DL = solve(ray, qL, qL/fac, uobs)
                uF, kF, _, _ = solve(flat, qF, qF/fac, Rr)
                res[fac] = (kL[:, -1], kF[:, -1])
            print("  p=%g (%.0fs):" % (p, time.time()-t0))
            fa, fb = FACS[0], FACS[-1]
            for o in range(3):
                r20 = res[fa][0][o]/res[fa][1][o]; r40 = res[fb][0][o]/res[fb][1][o]; rR = (4*r40 - r20)/3 if fb == 2*fa else r40
                print("   op%d: hhat_lens(q/%d)=%+.6f hhat_flat(q/%d)=%+.6f | ratio q/%d=%.5f q/%d=%.5f Richardson=%.5f | ratio/sqrt(Delta)=%.5f" %
                      (o, fb, res[fb][0][o], fb, res[fb][1][o], fa, r20, fb, r40, rR, rR/np.sqrt(DL)))
            sys.stdout.flush()
