"""RL3 (B): CHECK of Lemma S (interior and grouped insertions are suppressed when the in- and out-legs of a vertex
have a large relative rapidity).  Units l_k = 1, rho_k = 1; every amplitude below carries the same factor eps^2 (exact),
which is dropped.
Three inserted points: z_prev (node), z (the vertex being tested), z_next (node).  z = 0,
  z_prev - z      = tau1 (1, 0, 0, 0)
  z - z_next      = tau2 (cosh th, -sinh th, 0, 0)        (th = relative rapidity of the two legs)
Exact chaos-kernel contributions with z_prev, z_next nodes (Theorem 1 of the report):
  N   = H(tau1) H(tau2)                                         z a node
  Id  = int_{v in I(z_next,z)} f'(m(z_prev,v)) H(tau(z_next,v)) dv          z interior to the hop z_prev -> v
  IH  = int_{u in I(z,z_prev)} int_{v in I(z_next,z)} H(u,z_prev) f'(m(u,v)) H(z_next,v)   hop u -> v after a mean chain
  Gd  = f'(m(z_prev, z_next))                                   z interior to the hop z_prev -> z_next (grouped)
  GH  = int_{u in I(z,z_prev)} H(u,z_prev) f'(m(u,z_next)) du
  (u, v are confined to the two causal diamonds exactly: u in J-(z_prev) and J+(z), v in J-(z) and J+(z_next).)
f'(m) = d f_C/dm (the mean of one forward difference of the eps-thinned weight, divided by eps^2: exact).
Output: R(th) = (Id+IH+Gd+GH)/N with MC errors.
"""
import numpy as np, sys
from rl2_core import OPS
from scipy.special import gammaln
op = int(sys.argv[1]) if (len(sys.argv) > 1 and __name__ == "__main__") else 0
C = OPS[op]; L = len(C)
dC = np.array([C[j+1]-C[j] for j in range(L-1)] + [-C[L-1]])
def fpoly(c, m):
    m = np.asarray(m, float); return np.exp(-m)*sum(c[j]*m**j/np.exp(gammaln(j+1)) for j in range(len(c)))
mof = lambda tau2: np.pi*np.maximum(tau2, 0)**2/24          # m = (pi/24) tau^4, argument tau^2
d = np.load("rl3_H_op%d.npz" % op); TT, HH = d["taus"], d["H"]
Hf = lambda tau: np.interp(tau, TT, HH, right=0.0)
rng = np.random.default_rng(7 + op)
def mink2(a):   # squared proper time of a (timelike positive), a[...,0]=t
    return a[..., 0]**2 - (a[..., 1:]**2).sum(-1)
def diamond(tau, n):
    """uniform points in the causal diamond between 0 (bottom) and (tau,0,0,0) (top), rest frame."""
    out = np.empty((0, 4))
    while len(out) < n:
        k = 3*n; t = rng.uniform(0, tau, k); x = rng.uniform(-tau/2, tau/2, (k, 3))
        ok = np.sqrt((x**2).sum(1)) < np.minimum(t, tau-t); out = np.vstack([out, np.column_stack([t[ok], x[ok]])])
    return out[:n]
def boost(p, th):   # boost along -x by rapidity th: (t,x) -> (t ch + x sh ... ) mapping (1,0) -> (ch, -sh)
    ch, sh = np.cosh(th), np.sinh(th); q = p.copy()
    q[..., 0] = ch*p[..., 0] - sh*p[..., 1]; q[..., 1] = -sh*p[..., 0] + ch*p[..., 1]; return q
def run(tau1, tau2, th, n=400000):
    zp = np.array([tau1, 0, 0, 0.]); zn = -boost(np.array([tau2, 0, 0, 0.]), th)
    V1 = np.pi/24*tau1**4; V2 = np.pi/24*tau2**4
    N = Hf(tau1)*Hf(tau2)
    u = diamond(tau1, n)                       # in I(z, z_prev): bottom z=0, top z_prev
    v = zn + boost(diamond(tau2, n), th)       # in I(z_next, z): bottom z_next, top z=0
    hu = Hf(np.sqrt(np.maximum(mink2(zp-u), 0)))
    hv = Hf(np.sqrt(np.maximum(mink2(v-zn), 0)))
    Id_s = fpoly(dC, mof(mink2(zp-v)))*hv*V2
    IH_s = hu*fpoly(dC, mof(mink2(u-v)))*hv*V1*V2
    GH_s = hu*fpoly(dC, mof(mink2(u-zn)))*V1
    Gd = float(fpoly(dC, mof(mink2(zp-zn))))
    est = lambda s: (s.mean(), s.std()/np.sqrt(len(s)))
    Id, eId = est(Id_s); IH, eIH = est(IH_s); GH, eGH = est(GH_s)
    rest = Id+IH+Gd+GH; err = np.sqrt(eId**2+eIH**2+eGH**2)
    return N, Id, IH, Gd, GH, rest, err
if __name__ == "__main__":
  print("op%d  H(0.5)=%.4f H(0.8)=%.4f H(1)=%.4f H(1.5)=%.4f" % (op, Hf(0.5), Hf(0.8), Hf(1.0), Hf(1.5)))
  for (t1, t2) in [(0.6, 0.6), (1.0, 1.0), (0.6, 1.4)]:
      print(" legs tau1=%.1f tau2=%.1f" % (t1, t2))
      for th in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]:
          N, Id, IH, Gd, GH, rest, err = run(t1, t2, th)
          print("   th=%.1f  N=%+.4e  Id=%+.3e IH=%+.3e Gd=%+.3e GH=%+.3e | R=(rest)/N = %+.3e +- %.1e  ; e^{-2th}=%.1e"
                % (th, N, Id, IH, Gd, GH, rest/N, err/abs(N), np.exp(-2*th)), flush=True)
