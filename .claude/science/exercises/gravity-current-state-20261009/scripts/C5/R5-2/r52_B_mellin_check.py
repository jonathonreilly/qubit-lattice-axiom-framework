"""R5-2 (B): check (i) the closed-form Mellin transform of R4-1's Selberg transform
  H_r(beta) = (4 pi/r) int_0^inf exp(-beta cosh 2d) sinh d sin(r d) dd        (beta = m/(2 l^2))
  Ht_r(s)  = int_0^inf beta^(s-1) H_r(beta) dbeta
           = (pi/(i r)) 2^(s-2) [ G(s/2+1/4+ir/4) G(s/2-1/4-ir/4) - G(s/2-1/4+ir/4) G(s/2+1/4-ir/4) ]   (Re s > 1/2)
and (ii) the residue expansion  H_r(beta) = sum_{k>=0} sum_{+-} Res_{s=1/2+-ir/2-k} Ht_r(s) beta^{-s}  (asymptotic, beta->0)."""
import numpy as np
from scipy.integrate import quad
from scipy.special import gamma as G
def H(r, beta):
    dmax = 0.5*np.arccosh(max(1.0, 60.0/beta)) + 1.0
    f = lambda d: np.exp(-beta*np.cosh(2*d))*np.sinh(d)*np.sin(r*d)
    v, e = quad(f, 0, dmax, limit=2000, epsabs=0, epsrel=1e-12)
    return 4*np.pi/r*v
def Ht_closed(r, s):
    a = G(s/2+0.25+1j*r/4)*G(s/2-0.25-1j*r/4); b = G(s/2-0.25+1j*r/4)*G(s/2+0.25-1j*r/4)
    return (np.pi/(1j*r)*2**(s-2)*(a-b))
def Ht_num(r, s):
    # integrate in t = ln beta
    f = lambda t: np.exp(s*t)*H(r, np.exp(t))
    v, e = quad(f, -40, 6, limit=400, epsabs=0, epsrel=1e-9)
    return v
print("(i) closed form vs numerical Mellin transform")
for r in (1.0, 2.5):
    for s in (1.1, 1.7, 2.5):
        c = Ht_closed(r, s); n = Ht_num(r, s)
        print(f"  r={r} s={s}: closed={c.real:+.10e} (imag {c.imag:.1e})  numeric={n:+.10e}  rel.diff={abs(c-n)/abs(n):.1e}")
def res(r, s0):
    eps = 1e-7
    return 0.5*(Ht_closed(r, s0+eps) - Ht_closed(r, s0-eps))*eps   # simple pole: (Ht(s0+e)-Ht(s0-e))/2 * e
print("(ii) residue sums vs H_r(beta)")
for r in (1.0, 2.5):
    for beta in (1e-2, 1e-3, 1e-4):
        h = H(r, beta); errs = []; tot = 0
        for k in range(4):
            for sg in (+1, -1):
                s0 = 0.5 + sg*1j*r/2 - k
                tot += res(r, s0)*beta**(-s0)
            errs.append(abs(h - tot.real)/abs(h))
        print(f"  r={r} beta={beta:.0e}: H={h:+.8e}; rel.err with k<=0..3: " + ", ".join(f"{e:.1e}" for e in errs))
