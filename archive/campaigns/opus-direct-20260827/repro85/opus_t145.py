"""T145 - INDEPENDENT CHECK OF THE BRIDGE CLOSURE'S CENTRAL RELATION.

The bridge lane closes the Einstein half by DIFFERENTIATING THE CUTOFF AWAY.
Its key step: instead of W = -(1/2) int_{tau_0}^inf (dtau/tau) K(tau), which
integrates every proper time above tau_0 and so inherits the lattice error at the
bottom of the integral, use dW/dtau_0 = K(tau_0)/(2 tau_0), which puts the whole
bridge at ONE proper time.  The relation it then uses is

    (4 pi s)^2 [ K_pert(s) - K_flat(s) ]  =  dVol + s * dS_Regge / 3 + O(s^2)

FIRST, algebra, by hand.  K(s) ~ (4 pi s)^{-2}[Vol + (s/6) int R sqrt(g)], so
(4 pi s)^2 dK = dVol + (s/6) d(int R sqrt(g)); and R63 established
S_Regge = (1/2) int R sqrt(g), so int R sqrt(g) = 2 S_Regge and the second term is
s dS_Regge/3.  THE RELATION IS RIGHT -- and note it is only right BECAUSE of R63's
factor of 1/2, which this campaign spent four independent routes establishing.

SECOND, numerically, with my own machinery and no import of theirs: compute both
sides directly on a small lattice.  I will not reproduce their 0.99 plateau at
L=6 -- the lattice error is far too large there -- but the ratio must be the right
sign, the right order, and must approach 1/3 as the mesh refines.  That is what a
check at reachable size can establish."""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t116 import kuhn, positions, lengths_from_positions, spectrum
from opus_t114b import build, S_of

def run(L,amp,nk=1):
    verts,vid,simp=kuhn(L); N=len(verts)
    h=1.0/L
    kv=2*np.pi*nk*np.array([1.0,0,0,0])
    # traceless perturbation in the 2-3 plane, wave along x0  (the lane's TT channel)
    ep=np.zeros((4,4)); ep[2,2]=1.0; ep[3,3]=-1.0
    def l2list(a):
        out=[]
        for (ids,base,offs) in simp:
            X=(base[None,:]+offs)*h
            l2=np.zeros((5,5))
            for i,j in itertools.combinations(range(5),2):
                dx=X[i]-X[j]; mid=0.5*(X[i]+X[j])
                g=np.eye(4)+a*np.cos(float(mid@kv))*ep
                l2[i,j]=l2[j,i]=float(dx@g@dx)
            out.append(l2)
        return out
    def vol(l2s):
        t=0.0
        for l2 in l2s:
            G=np.empty((4,4))
            for x in range(4):
                for y in range(4): G[x,y]=0.5*(l2[0,x+1]+l2[0,y+1]-l2[x+1,y+1])
            t+=np.sqrt(max(np.linalg.det(G),0.0))/24.0
        return t
    f0=l2list(0.0); fp=l2list(amp)
    lam0=spectrum(simp,f0,N); lamp=spectrum(simp,fp,N)
    V0,Vp=vol(f0),vol(fp)
    # Regge action on the SAME configuration, my own independent code path
    verts2,vid2,tops,edges,emid,edir,base_len=build(L)
    def ell(a):
        e2=base_len.copy()
        for key,ei in edges.items():
            u=edir[key]; mid=emid[key]
            g=np.eye(4)+a*np.cos(float(mid@kv))*ep
            e2[ei]=np.sqrt(float(u@g@u))
        return e2
    S0=S_of(tops,edges,ell(0.0)); Sp=S_of(tops,edges,ell(amp))
    return lam0,lamp,V0,Vp,S0,Sp

print("T145  independent check: (4 pi s)^2 dK - dVol  ==  s dS_Regge / 3 ?")
print("      (the relation the bridge closure rests on; the 1/3 comes from R63's S = (1/2) int R)")
print()
for L in (5,6):
    lam0,lamp,V0,Vp,S0,Sp=run(L,0.10)
    dV=Vp-V0; dS=Sp-S0
    print(f"   L={L}:  dVol = {dV:+.6e}   dS_Regge = {dS:+.6e}   -> predicted slope dS/3 = {dS/3:+.6e}")
    print(f"      {'s':>7} {'(4 pi s)^2 dK':>16} {'minus dVol':>14} {'/ s':>13} {'ratio to dS/3':>15}")
    for s in (0.05,0.08,0.12,0.18,0.25):
        dK=float(np.sum(np.exp(-s*lamp))-np.sum(np.exp(-s*lam0)))
        lhs=(4*np.pi*s)**2*dK
        val=(lhs-dV)/s
        print(f"      {s:7.3f} {lhs:16.6e} {lhs-dV:14.6e} {val:13.6e} {val/(dS/3):15.4f}")
    print()
print("   Ratio approaching 1 as s grows (lattice error dies) and as L grows is the")
print("   check.  A ratio near 3 instead would mean the 1/3 -- hence R63's factor -- is wrong.")
