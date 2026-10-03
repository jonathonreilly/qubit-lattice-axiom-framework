"""A21 re-check 1: Z^3 lattice Green function -> Cap(site), Cap(star), A17 floor;
plus arithmetic for (a) vacuum freezing time at unit vs weak formation strength,
(b) D23 wake geometry, (c) persistence loophole for D23."""
import os, signal
for v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
signal.alarm(55)
import numpy as np
from scipy.special import ive
from scipy.integrate import quad

def G(r):
    # (-Delta)^{-1}(0,r) with Delta f(x) = sum_{y~x} (f(y)-f(x)); heat kernel prod_i e^{-2t} I_{r_i}(2t)
    f = lambda t: np.prod([ive(abs(ri), 2*t) for ri in r])
    a, _ = quad(f, 0, 50, limit=400)
    b, _ = quad(f, 50, np.inf, limit=400)
    return a + b

G0 = G((0,0,0)); G1 = G((1,0,0)); G11 = G((1,1,0)); G2 = G((2,0,0))
print("G(0)=%.6f  G(e1)=%.6f (G0-1/6=%.6f)  G(1,1,0)=%.6f  G(2,0,0)=%.6f" % (G0, G1, G0-1/6, G11, G2))
star = [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
cache = {}
def Gd(a, b):
    d = tuple(sorted(abs(a[i]-b[i]) for i in range(3)))
    if d not in cache: cache[d] = G(d)
    return cache[d]
GKK = np.array([[Gd(a,b) for b in star] for a in star])
one = np.ones(len(star))
cap_star = one @ np.linalg.solve(GKK, one)
cap_site = 1/G0
kappa, u = 1/12, 0.5
print("Cap(site)=%.4f  Cap(star)=%.4f" % (cap_site, cap_star))
print("A17 floor 2(1-u)/(u kappa Cap): site %.3f ticks, star %.3f ticks (u=1/2)" % (2*(1-u)/(u*kappa*cap_site), 2*(1-u)/(u*kappa*cap_star)))

# (a) freezing times for the half-filled sea, best star projector (A9: 5.0e-6 per unit strength), energy rule 0.012
tP = 5.391e-44
for label, c in [("unit strength", 1.0), ("records a full-overlap particle within ~1 s", tP/1.0), ("A13 interference bound c<=1e-43", 1e-43)]:
    for name, lam in [("best projector 5e-6", 5.0e-6), ("energy rule 0.012", 0.012)]:
        rate = c*lam
        print("freeze e-fold [%s, %s]: rate %.2e/tick -> %.3g s" % (label, name, rate, (1/rate)*tP))
age_ticks = 4.35e17/tP
print("strength needed for <=1 false record per site in the universe's age (best projector): c <= %.2e" % (1/(age_ticks*5e-6)))

# (b) D23 wake geometry
lP = 1.616e-35; D = lP**2/(12*tP)
for v in (3.0e4, 3.7e5):
    r = 3.84e8
    print("v=%.1e m/s: D=%.3e m^2/s, D/v=%.2e m, wake half-width at Moon sqrt(4Dr/v)=%.2e m, upstream screening exponent v r/D=%.2e" % (v, D, D/v, np.sqrt(4*D*r/v), v*r/D))
# (c) persistence loophole: carriers ballistic up to length ell, then diffusive with D ~ c*ell/3
c = 2.998e8
for ell in (5e-5, 1.0, 1e5):
    Dp = c*ell/3
    print("persistence %.0e m: D=%.2e, D/v(30 km/s)=%.2e m (Moon at 3.84e8 m)" % (ell, Dp, Dp/3.0e4))
