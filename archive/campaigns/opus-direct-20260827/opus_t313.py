"""
T313 - R157 recheck done properly: extrapolate in s FIRST, then in B.

T312 extrapolated in B without removing the 1/s lattice artefact and got
c2(0) ~ -0.155, 7% off. That was my error, not R157's: c2(s) is still climbing
across every window (L=224: -0.1386 -> -0.1561 over s in [3,8.9]). The squeeze
is 1 << s << 1/B, so BOTH limits must be taken, in order.

Step 1: at fixed B, fit c2(s) = c2_inf + A/s  (the artefact R188 measured).
Step 2: extrapolate c2_inf(B) -> B = 0.
Controls: report the step-1 fit residual, and compare linear vs quadratic in B,
so the answer's sensitivity to the extrapolation form is visible rather than
assumed away -- which is the whole point of rechecking R157.
"""
import numpy as np
def spectrum(L,B):
    ev=[]
    for n2 in range(L):
        k2=2*np.pi*n2/L
        H=np.zeros((L,L),dtype=complex)
        for x in range(L):
            H[x,x]=4.0-2.0*np.cos(k2-B*x)
            H[x,(x+1)%L]-=1.0; H[(x+1)%L,x]-=1.0
        ev.append(np.linalg.eigvalsh(H))
    return np.concatenate(ev)
print("step 1: c2(s) = c2_inf + A/s at fixed B      target c2_inf -> -1/6 as B->0\n")
print("    L       B       c2_inf      A       fit resid")
rows=[]
for L in (64,96,128,160,224,288):
    B=2*np.pi/L
    ev=spectrum(L,B); ev0=spectrum(L,0.0)
    smax=0.30/B; sv=np.linspace(max(4.0,0.35*smax),smax,7)
    c=np.array([((np.sum(np.exp(-s*ev))/np.sum(np.exp(-s*ev0)))-1.0)/(s*B)**2 for s in sv])
    co,res,_,_,_=np.polyfit(1.0/sv,c,1,full=True)
    rows.append((B,co[1]))
    print(f"  {L:4d}  {B:.5f}  {co[1]:+.6f}  {co[0]:+.4f}   {np.sqrt(res[0]/len(sv)):.2e}")
Bs=np.array([r[0] for r in rows]); cs=np.array([r[1] for r in rows])
print("\nstep 2: extrapolate c2_inf(B) -> 0")
for nm,deg,sel in (("linear, all",1,slice(None)),("quadratic, all",2,slice(None)),
                   ("linear, 4 smallest B",1,slice(2,None))):
    co=np.polyfit(Bs[sel],cs[sel],deg)
    print(f"    {nm:22s} c2(0) = {co[-1]:+.7f}   vs -1/6 = -0.1666667   dev {abs(co[-1]+1/6):.2e}")
    print(f"    {'':22s} a2 coeff of F^2 = {co[-1]/2:+.7f}  vs -1/12 = -0.0833333")
print(f"\n  R157 reported: c2(0) = -0.166538 (dev 1.3e-04), a2 coeff = -0.083269 (dev 6.5e-05)")
