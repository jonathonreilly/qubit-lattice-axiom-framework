# Parameter-free Weyl quantum cellular automaton (D'Ariano-Perinotti 2014, BCC lattice):
# one unitary step per tick, nearest-neighbour, no tunable couplings.
import numpy as np
rng=np.random.default_rng(3)
s3=np.sqrt(3)
def omega(k):
    c=np.cos(k/s3); s=np.sin(k/s3)
    d=c[0]*c[1]*c[2]-s[0]*s[1]*s[2]
    return np.arccos(np.clip(d,-1,1))
# 1. causal cone: one lattice step per tick; group velocity bound
ks=rng.uniform(-np.pi*s3,np.pi*s3,size=(20000,3)); h=1e-6
vmax=0
for k in ks[:4000]:
    g=[(omega(k+h*e)-omega(k-h*e))/(2*h) for e in np.eye(3)]; vmax=max(vmax,np.linalg.norm(g))
print("max group speed over the zone (lattice units per tick):",round(vmax,4))
# 2. small-k speed: same in every direction, no parameter
dirs=rng.normal(size=(500,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
for q in (0.04,0.02,0.01):
    v=np.array([omega(q*d)/q for d in dirs])
    print(f"|k|={q}: mean speed {v.mean():.8f} (1/sqrt3={1/s3:.8f}), relative anisotropy {np.ptp(v)/v.mean():.2e}")
# 3. composite of two collinear constituents (photon-like pair, Bisio-D'Ariano-Perinotti): speed inherited
for q in (0.04,0.02):
    v=np.array([2*omega(q/2*d)/q for d in dirs])
    print(f"pair with total |k|={q}: mean speed {v.mean():.8f}")
