"""
T245 - are the framework's monopoles physical excitations?

Prerequisite for R163's fermion route.  Measures, at the Born point on Z^3 with
CP^1 states (the axioms as written): the action cost of a monopole, the spatial
profile of the disturbance around it, and the observed density against a Gaussian
estimate.
"""
import numpy as np, time

L = 20
def equilibrate(nwarm=4000, nsamp=60, gap=6, seed=151, cone=0.6):
    rng = np.random.default_rng(seed)
    psi = rng.normal(size=(L,L,L,2)) + 1j*rng.normal(size=(L,L,L,2))
    psi /= np.linalg.norm(psi, axis=-1, keepdims=True)
    idx = np.indices((L,L,L)); masks = [(idx.sum(axis=0)%2==p) for p in (0,1)]
    def sweep():
        for mask in masks:
            prop = psi + cone*(rng.normal(size=psi.shape)+1j*rng.normal(size=psi.shape))
            prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
            wo = np.ones(psi.shape[:3]); wn = np.ones(psi.shape[:3])
            for ax in range(3):
                for sg in (1,-1):
                    nb = np.roll(psi, sg, ax)
                    wo *= np.abs(np.sum(np.conj(psi)*nb,axis=-1))**2
                    wn *= np.abs(np.sum(np.conj(prop)*nb,axis=-1))**2
            acc = (rng.random(psi.shape[:3]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
            psi[acc] = prop[acc]
    for _ in range(nwarm): sweep()
    out = []
    for _ in range(nsamp):
        for _ in range(gap): sweep()
        out.append(psi.copy())
    return out

def analyse(psi):
    U = []
    for ax in range(3):
        z = np.sum(np.conj(psi)*np.roll(psi,-1,ax),axis=-1)
        U.append(z/np.maximum(np.abs(z),1e-300))
    def plaq(mu,nu):
        return np.angle(U[mu]*np.roll(U[nu],-1,mu)
                        *np.conj(np.roll(U[mu],-1,nu))*np.conj(U[nu]))
    Fs = {}
    tot = np.zeros(psi.shape[:3])
    for (mu,nu) in ((0,1),(1,2),(2,0)):
        F = plaq(mu,nu); Fs[(mu,nu)] = F
        tot += F - np.roll(F,-1,3-mu-nu)
    q = np.round(tot/(2*np.pi))
    # local action on each cube: -log of the product of edge weights on its 12 edges
    w = {}
    for ax in range(3):
        w[ax] = -np.log(np.maximum(np.abs(np.sum(np.conj(psi)*np.roll(psi,-1,ax),axis=-1))**2, 1e-300))
    S = np.zeros(psi.shape[:3])
    for ax in range(3):
        for da in (0,1):
            for db in (0,1):
                o1, o2 = [a for a in range(3) if a != ax]
                A = w[ax]
                if da: A = np.roll(A, -1, o1)
                if db: A = np.roll(A, -1, o2)
                S += A
    Fmag = sum(np.abs(Fs[k]) for k in Fs)/3
    return q, S, Fmag

cfgs = equilibrate()
print(f"L={L}, {len(cfgs)} configurations, Born point, CP^1 on Z^3\n")
Sm, Se, dens, rms = [], [], [], []
prof = np.zeros(6); profn = np.zeros(6)
for c in cfgs:
    q, S, Fmag = analyse(c)
    m = (q != 0)
    Sm.append(S[m].mean() if m.any() else np.nan); Se.append(S[~m].mean())
    dens.append(m.mean()); rms.append(np.sqrt(np.mean(Fmag**2)))
    # radial profile of |F| around monopoles
    idx = np.argwhere(m)
    if len(idx):
        ii, jj, kk = np.indices((L,L,L))
        for (a,b,cc) in idx[:40]:
            d = np.minimum(np.abs(ii-a), L-np.abs(ii-a))**2 \
              + np.minimum(np.abs(jj-b), L-np.abs(jj-b))**2 \
              + np.minimum(np.abs(kk-cc), L-np.abs(kk-cc))**2
            r = np.sqrt(d).astype(int)
            for rr in range(6):
                sel = (r == rr)
                prof[rr] += Fmag[sel].sum(); profn[rr] += sel.sum()
print(f"(a) ACTION COST")
print(f"    local action on MONOPOLE cubes : {np.nanmean(Sm):.5f}")
print(f"    local action on EMPTY   cubes : {np.nanmean(Se):.5f}")
print(f"    excess per monopole            : {np.nanmean(Sm)-np.nanmean(Se):+.5f}"
      f"   ({(np.nanmean(Sm)/np.nanmean(Se)-1)*100:+.1f}%)")
print(f"\n(b) LOCALISATION - mean |F| vs distance from a monopole")
p = prof/np.maximum(profn,1)
for rr in range(6):
    print(f"    r={rr}:  {p[rr]:.5f}" + ("   <- bulk" if rr == 5 else ""))
print(f"    bulk mean |F| (all cubes)      : {np.mean([np.sqrt(x**2) for x in rms]):.5f}")
print(f"\n(c) DENSITY vs a GAUSSIAN ESTIMATE")
r_ = np.mean(rms)
from math import erfc, sqrt
sig6 = r_*np.sqrt(6)
pg = erfc(2*np.pi/(sig6*sqrt(2)))
print(f"    measured monopole density      : {np.mean(dens):.6f}")
print(f"    plaquette rms                  : {r_:.5f} rad")
print(f"    Gaussian estimate P(|sum6|>2pi): {pg:.3e}")
print(f"    ratio measured/Gaussian        : {np.mean(dens)/max(pg,1e-300):.3e}")
