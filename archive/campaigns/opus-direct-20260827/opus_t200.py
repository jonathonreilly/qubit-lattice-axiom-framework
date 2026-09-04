"""
T200 - INDEPENDENT re-measurement of the conformal heat-trace channel (R85/R89).

Deliberately independent of the recheck lane:
  * different discretisation: divergence-form tensor-product FEM with lumped mass
    (NOT the Kuhn simplicial complex),
  * different continuum prediction: closed-form conformal identities derived by
    hand (below), not a numerical Gilkey evaluation,
  * different code.

METRIC       g = e^{2w} delta,  e^{2w}(x) = 1 + eps*cos(kappa*x0)      (d=4)
Bilinear     int sqrt(g) g^{uv} d_u f d_v f = int e^{2w} |grad f|^2
Mass         int sqrt(g) f^2      = int e^{4w} f^2
Improvement  Delta -> Delta + c Delta^2 ,  c = tr g/96 = e^{2w}/24     (R89)

CONTINUUM PREDICTION, derived here:
  R = -6 e^{-2w} [ lap w + |grad w|^2 ]                       (conformally flat, d=4)
  sqrt(g) = e^{4w};  w = (1/2)log(1+eps*phi)
  int R sqrt(g) = -6 int e^{2w}[lap w + |grad w|^2]
                = 6 int (w')^2 + O(w^3)   [ int lap w = 0, int w lap w = -int w'^2 ]
  => O(eps^2) part = (3/2) int phi'^2
  Vol   O(eps^2) part = int phi^2
  a2 = (1/360)(12 lap R + 5R^2 - 2 Ric^2 + 2 Riem^2); with u = w'' the ONLY
  nonzero second derivative:  R=-6u, Ric=diag(-3u,-u,-u,-u), Riem_{0j0j}=-u
  => 5(36) - 2(12) + 2(12) = 180 u^2  =>  int a2 = (1/2) int u^2 = (1/8) int phi''^2

  With phi = cos(kappa x): int phi^2 = L^4/2, int phi'^2 = k2*L^4/2,
  int phi''^2 = k2^2*L^4/2   (k2 = kappa^2)

  (4 pi s)^2 K_2(s) / (L^4/2)  =  1 + x/4 + x^2/8 + O(x^3),   x = s*kappa^2
                                   ^a0   ^a1    ^a2
so the measured ratio must equal that, and F = (ratio-1)/(x/4) -> 1.
"""
import numpy as np, sys, time
from collections import Counter
from numpy.polynomial.legendre import leggauss

XS, WS = leggauss(40)

def integ(fun, lo, hi):
    lo = np.asarray(lo, float); hi = np.asarray(hi, float)
    pts = 0.5*(lo+hi)[:, None] + 0.5*(hi-lo)[:, None]*XS[None, :]
    return 0.5*(hi-lo)*np.sum(WS[None, :]*fun(pts), axis=1)

def qspec(L):
    """distinct values of Q = sum_j 2(1-cos q_j) over 3 transverse directions,
       with multiplicity.  Exact: histogram convolution."""
    e = 2*(1-np.cos(2*np.pi*np.arange(L)/L))
    c1 = Counter(np.round(e, 12))
    def conv(ca, cb):
        c = Counter()
        for a, na in ca.items():
            for b, nb in cb.items():
                c[round(a+b, 12)] += na*nb
        return c
    return conv(conv(c1, c1), c1)

def heat(L, eps, kappa, svals, improved=True, QC=None):
    t = np.arange(L, dtype=float)
    W   = lambda x: 1.0 + eps*np.cos(kappa*x)      # e^{2w}
    Rho = lambda x: (1.0 + eps*np.cos(kappa*x))**2 # e^{4w} = sqrt(g)
    w  = integ(W,   t,     t+1.0)   # x0-edge stiffness  int_t^{t+1} e^{2w}
    v  = integ(W,   t-0.5, t+0.5)   # transverse stiffness over dual cell
    m  = integ(Rho, t-0.5, t+0.5)   # lumped mass
    C  = W(t)                       # tr g / 4
    isq = 1.0/np.sqrt(m)
    idx = np.arange(L)
    K0 = np.zeros((L, L))
    K0[idx, idx] += w + np.roll(w, 1)
    jp = (idx+1) % L
    K0[idx, jp] -= w
    K0[jp, idx] -= w
    if QC is None: QC = qspec(L)
    sv = np.asarray(svals, float)
    out = np.zeros(len(sv))
    for Q, mult in QC.items():
        K = K0.copy()
        K[idx, idx] += Q*v
        B = (isq[:, None]*K)*isq[None, :]
        if improved:
            B = B + ((B*C[None, :]) @ B)/24.0
            B = 0.5*(B+B.T)
        lam = np.linalg.eigvalsh(B)
        np.maximum(lam, 0.0, out=lam)
        out += mult*np.exp(-np.outer(sv, lam)).sum(axis=1)
    return out

def K2(L, kappa, svals, h, improved=True, QC=None):
    """4th-order 5-point second difference / 2  ->  eps^2 Taylor coefficient."""
    f = {e: heat(L, e*h, kappa, svals, improved, QC) for e in (-2, -1, 0, 1, 2)}
    d2 = (-f[2] + 16*f[1] - 30*f[0] + 16*f[-1] - f[-2])/(12*h*h)
    return 0.5*d2, f[0]

def winding(L, s):
    n = np.arange(-40, 41)
    th = np.sum(np.exp(-np.outer(1.0/(4*np.asarray(s, float)), (n*L)**2.0)), axis=1)
    return (L**4)*(th**4)/(4*np.pi*np.asarray(s, float))**2

if __name__ == "__main__":
    Ls = [int(a) for a in sys.argv[1:]] or [32]
    n_mode = 2
    xs = np.array([0.25, 0.4, 0.6, 0.8, 1.0, 1.4, 2.0, 3.0])
    for L in Ls:
        kappa = 2*np.pi*n_mode/L
        k2 = kappa**2
        sv = xs/k2
        t0 = time.time(); QC = qspec(L)
        print(f"\n=== L={L}  n={n_mode}  kappa^2={k2:.6f}  distinctQ={len(QC)} ===")
        for improved in (True, False):
            k2c, kflat = K2(L, kappa, sv, 0.05, improved, QC)
            ratio = (4*np.pi*sv)**2 * k2c / (L**4/2.0)
            Fraw = (ratio-1.0)/(xs/4.0)
            Fa2  = (ratio-1.0-xs**2/8.0)/(xs/4.0)
            wind = winding(L, sv)
            flatrel = kflat/wind - 1.0
            tag = "IMPROVED" if improved else "plain   "
            print(f"  {tag}  s      : " + " ".join(f"{q:9.3f}" for q in sv))
            print(f"  {tag}  x=s*k^2: " + " ".join(f"{q:9.3f}" for q in xs))
            print(f"  {tag}  flat err: " + " ".join(f"{q:9.2e}" for q in flatrel))
            print(f"  {tag}  F raw  : " + " ".join(f"{q:9.4f}" for q in Fraw))
            print(f"  {tag}  F -a2  : " + " ".join(f"{q:9.4f}" for q in Fa2))
        print(f"  [{time.time()-t0:.1f}s]")
