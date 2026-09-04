"""
T312 - independent recomputation of R157's induced Maxwell coefficient.

R157 extrapolated c2 -> -1/6 (hence a2 = -(1/12)F^2) with error 6.5e-5. But its
own "implied slope" column DRIFTS upward over the last three sizes
(0.24232, 0.24338, 0.24455) while being reported as "constant to 1%". A drifting
slope means the linear-in-B form is not right, and the intercept then carries a
bias -- the same class of error R196 just found in tau0.

Also note the window: with B = 2pi/L, the continuum regime needs 1 << s (lattice)
AND sB << 1 (weak field), i.e. 1 << s << L/2pi. At L=48 that is 1 << s << 7.6 --
very tight. This is R188's squeeze again.

Independent implementation: magnetic Laplacian on an LxL torus, Landau gauge
A_x = 0, A_y = B x1, B = 2pi/L per plaquette (total flux 2pi L, integral).
k2 is a good quantum number so the spectrum is L matrices of size L -- exact.
Continuum target: (4 pi s) K/V = sB/sinh(sB) = 1 - (sB)^2/6 + ...
"""
import numpy as np
def spectrum(L,B):
    ev=[]
    for n2 in range(L):
        k2=2*np.pi*n2/L
        H=np.zeros((L,L),dtype=complex)
        for x in range(L):
            H[x,x]=4.0-2.0*np.cos(k2-B*x)          # y-hops carry the phase
            H[x,(x+1)%L]-=1.0; H[(x+1)%L,x]-=1.0   # x-hops
        ev.append(np.linalg.eigvalsh(H))
    return np.concatenate(ev)
def c2_at(L,svals):
    B=2*np.pi/L; V=L*L
    ev=spectrum(L,B); ev0=spectrum(L,0.0)
    out=[]
    for s in svals:
        K=np.sum(np.exp(-s*ev)); K0=np.sum(np.exp(-s*ev0))
        # ratio kills the B-independent lattice artefact in a0
        out.append(((K/K0)-1.0)/(s*B)**2)
    return np.array(out),B
print("c2 from the RATIO K(B)/K(0), which cancels the B-independent lattice a0 artefact")
print("target: c2 -> -1/6 = -0.1666667\n")
print("    L      B       s window        c2(s) across the window          c2 (mean)")
rows=[]
for L in (48,64,96,128,160,224):
    B=2*np.pi/L
    smax=0.25/B                      # keep sB <= 0.5
    sv=np.linspace(max(3.0,0.3*smax),smax,5)
    c,_=c2_at(L,sv)
    rows.append((B,float(np.mean(c))))
    print(f"  {L:4d}  {B:.5f}  [{sv[0]:5.1f},{sv[-1]:5.1f}]   "
          +" ".join(f"{v:8.5f}" for v in c)+f"   {np.mean(c):9.6f}")
Bs=np.array([r[0] for r in rows]); cs=np.array([r[1] for r in rows])
print("\n  extrapolation form sensitivity (the point of this check):")
for nm,deg in (("linear in B",1),("quadratic in B",2)):
    co=np.polyfit(Bs,cs,deg)
    print(f"    {nm:16s} c2(0) = {co[-1]:+.6f}   vs -1/6   dev {abs(co[-1]+1/6):.2e}")
co=np.polyfit(Bs[-4:],cs[-4:],1)
print(f"    linear, 4 smallest B  c2(0) = {co[-1]:+.6f}   dev {abs(co[-1]+1/6):.2e}")
print(f"\n  R157 reported c2(0) = -0.166538  (dev 1.3e-04) and a2 coeff -0.083269")
