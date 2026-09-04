"""
T220 - dynamic exponent z, done properly.

T219 fitted Gamma(k) over k = 0.52 .. 2.62 at L=12.  The zone boundary is pi,
so four of five points were at LATTICE scale, not hydrodynamic.  Its control
proved the failure: at lam = 0.5 (DISORDERED, where Gamma must saturate at a
nonzero constant as k -> 0) it reported "relativistic z = 1", which is
impossible.  The k-window, not the physics, was being measured.

Correct design: track the SMALLEST mode k_min = 2 pi / L across several L, so
every point is the longest wavelength the box allows, and fit

    Gamma(k_min) ~ L^-z        z = 1 relativistic ; z = 2 diffusive

CONTROL retained: lam = 0.5 must give z ~ 0 (rate saturates -> no L dependence).
"""
import numpy as np, sys, time

def gamma_kmin(L, lam, nsweep, nwarm, seed=11):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(L,L,L,3)); v /= np.linalg.norm(v,axis=-1,keepdims=True)
    i,j,k = np.indices((L,L,L)); A = ((i+j+k)%2==0); B = ~A
    def half(mask):
        nb = (np.roll(v,1,0), np.roll(v,-1,0), np.roll(v,1,1),
              np.roll(v,-1,1), np.roll(v,1,2), np.roll(v,-1,2))
        prop = rng.normal(size=v.shape)
        prop /= np.linalg.norm(prop,axis=-1,keepdims=True)
        wo = np.ones(v.shape[:3]); wn = np.ones(v.shape[:3])
        for n in nb:
            wo *= 1 + lam*np.sum(v*n,axis=-1)
            wn *= 1 + lam*np.sum(prop*n,axis=-1)
        acc = (rng.random(v.shape[:3]) < np.clip(wn/np.maximum(wo,1e-300),0,1)) & mask
        v[acc] = prop[acc]
    for _ in range(nwarm): half(A); half(B)
    # only three Fourier modes are needed; a full FFT per sweep is ~10x waste.
    # f[1,0,0] = sum_x e^{-2 pi i x/L} ( sum_{y,z} v[x,y,z] )
    ph = np.exp(-2j*np.pi*np.arange(L)/L)
    rec = np.zeros((nsweep,3,3), dtype=complex)
    for t in range(nsweep):
        half(A); half(B)
        rec[t,0] = ph @ v.sum(axis=(1,2))
        rec[t,1] = ph @ v.sum(axis=(0,2))
        rec[t,2] = ph @ v.sum(axis=(0,1))
    x = rec.reshape(nsweep,9); x = x - x.mean(axis=0)
    T = nsweep; tmax = min(T//4, 20000)
    C = np.zeros(tmax)
    for c in range(9):
        f = np.fft.fft(x[:,c], 2*T)
        C += np.fft.ifft(f*np.conj(f)).real[:tmax]
    C /= C[0]
    tau = 0.5
    for t in range(1, tmax):
        if C[t] <= 0: break
        tau += C[t]
        if t > 8*tau: break
    return 1.0/tau, tau

if __name__ == "__main__":
    plan = [(8,40000),(12,70000),(16,110000),(24,200000)]
    for lam in (1.0, 0.5):
        print(f"\n=== lam = {lam} ===")
        print("   L    k_min     tau        Gamma(k_min)")
        Ls=[]; G=[]
        for L, ns in plan:
            t0=time.time()
            g, tau = gamma_kmin(L, lam, ns, 3000)
            Ls.append(L); G.append(g)
            print(f"  {L:3d}  {2*np.pi/L:6.4f}  {tau:9.2f}   {g:.6e}   [{time.time()-t0:.0f}s]")
        z = -np.polyfit(np.log(Ls), np.log(G), 1)[0]
        for a,b in zip(range(len(Ls)-1), range(1,len(Ls))):
            zz = -np.log(G[b]/G[a])/np.log(Ls[b]/Ls[a])
            print(f"    local z between L={Ls[a]} and L={Ls[b]}: {zz:.3f}")
        tag = ("RELATIVISTIC z=1" if abs(z-1)<0.2 else
               "DIFFUSIVE z=2" if abs(z-2)<0.35 else
               "saturating z~0 (expected for the disordered control)" if abs(z)<0.4 else "neither")
        print(f"    overall fitted z = {z:.3f}   ({tag})")
