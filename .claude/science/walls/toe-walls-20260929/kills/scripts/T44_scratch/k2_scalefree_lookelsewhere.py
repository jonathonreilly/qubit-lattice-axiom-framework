"""Scale-free look-elsewhere: alpha_s free; four-channel spread (max-min)/mean <= observed 2.34% for SOME
(Np,Nc) in {1..4}x{1..5}.  Null worlds: (lam,Vcb,Vub,Vtd) = real * independent log-uniform factors, width W.
E4 is solved by vectorised bisection."""
import math, numpy as np
rng = np.random.default_rng(7)
real = dict(lam=0.22501, Vcb=0.04183, Vub=0.003732, Vtd=0.00858)
def spread_pair(Np, Nc, lam, Vcb, Vub, Vtd):
    Nq = Np*Nc
    e1 = Np*lam**2; e2 = math.sqrt(Nq)*Vcb; e3 = (Np*Nq**2*Vub**2)**(1/3)
    lo = np.full(lam.shape, 1e-6); hi = np.full(lam.shape, 5.0)
    for _ in range(60):
        mid = (lo+hi)/2
        f = mid**3*(Np**4*(Nq-1)+mid**2)/(Np**7*Nc**2) - Vtd**2
        pos = f > 0; hi = np.where(pos, mid, hi); lo = np.where(pos, lo, mid)
    e4 = (lo+hi)/2
    S = np.stack([e1,e2,e3,e4]); m = S.mean(0)
    return (S.max(0)-S.min(0))/m
obs = 0.0234
N = 200000
for W in (math.log(2), 1.0, math.log(5)):
    f = lambda: np.exp(rng.uniform(-W, W, N))
    lam, Vcb, Vub, Vtd = (real['lam']*f(), real['Vcb']*f(), real['Vub']*f(), real['Vtd']*f())
    best = np.full(N, 9.9); bestpair = {}
    hitany = np.zeros(N, bool); hit236 = np.zeros(N, bool)
    for Np in range(1,5):
        for Nc in range(1,6):
            s = spread_pair(Np,Nc,lam,Vcb,Vub,Vtd)
            hitany |= s <= obs
            if (Np,Nc)==(2,3): hit236 = s <= obs
    print(f"jitter width exp(+-{W:.2f}): P(some of 20 pairs has spread<=2.34%) = {hitany.mean():.2e};  P((2,3) specifically) = {hit236.mean():.2e}")
