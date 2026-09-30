"""B2: in the chart's baseline-signature region, where are s12^2, s13^2 inside the NuFIT-6.1 3sigma box and what s23^2, delta occur?
Vectorised random scan of (m,delta,q_+), chamber q_+ + delta >= sqrt(8/3), signature(H) = signature(H_base)."""
import math, numpy as np
from common import BOX61
E1=math.sqrt(8/3); E2=math.sqrt(8)/3; GAMMA=0.5
T_M=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=complex)
T_D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]],dtype=complex)
T_Q=np.array([[0,1,1],[1,0,1],[1,1,0]],dtype=complex)
HB=np.array([[0,E1,-E1-1j*GAMMA],[E1,0,-E2],[-E1+1j*GAMMA,-E2,0]],dtype=complex)
print("H_base eigenvalues", np.linalg.eigvalsh(HB), "-> positive count", np.sum(np.linalg.eigvalsh(HB)>0))
rng=np.random.default_rng(11)
N=3_000_000
m=rng.uniform(-2,4,N); d=rng.uniform(0,3,N); q=rng.uniform(0,3,N)
keep=(q+d>=E1)
m,d,q=m[keep],d[keep],q[keep]
Hs=HB[None]+m[:,None,None]*T_M[None]+d[:,None,None]*T_D[None]+q[:,None,None]*T_Q[None]
w,V=np.linalg.eigh(Hs)                     # ascending eigenvalues
npos=(w>0).sum(1)
basepos=int(np.sum(np.linalg.eigvalsh(HB)>0))
sel=(npos==basepos)
print(f"samples in chamber {keep.sum()}, with baseline signature {sel.sum()}")
m,d,q,w,V=m[sel],d[sel],q[sel],w[sel],V[sel]
P=V[:,[2,1,0],:]                           # sigma_hier = (2,1,0) rows
a=np.abs(P)**2
s13=a[:,0,2]; c13=1-s13; s12=a[:,0,1]/c13; s23=a[:,1,2]/c13
J=(P[:,0,0]*np.conj(P[:,0,1])*np.conj(P[:,1,0])*P[:,1,1]).imag
den=np.sqrt(s12*(1-s12)*s23*(1-s23))*c13*np.sqrt(s13)
sd=J/den
for nm,B in (("NuFIT-6.1 3sigma (repo-quoted)",BOX61),):
    in12=(s12>=B["s12"][0])&(s12<=B["s12"][1]); in13=(s13>=B["s13"][0])&(s13<=B["s13"][1])
    both=in12&in13
    print(f"{nm}: samples with s12^2 and s13^2 in box: {both.sum()}")
    if both.sum():
        print(f"   their s23^2 range: [{s23[both].min():.4f},{s23[both].max():.4f}]  fraction with s23^2 < 0.5: {(s23[both]<0.5).mean():.3f}")
        print(f"   their sin(delta) range: [{sd[both].min():.4f},{sd[both].max():.4f}]")
        print(f"   m range [{m[both].min():.3f},{m[both].max():.3f}], delta range [{d[both].min():.3f},{d[both].max():.3f}], q range [{q[both].min():.3f},{q[both].max():.3f}]")
        lo=both&(s23<0.5335)
        print(f"   with s23^2 < 0.5335 (lane's chamber threshold): {lo.sum()}")
