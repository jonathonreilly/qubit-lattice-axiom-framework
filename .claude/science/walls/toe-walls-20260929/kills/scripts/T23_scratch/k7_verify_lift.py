#!/usr/bin/env python3
"""K7: reproduce the C2d (pi-rotation about [1,-1,0], proper) triplet-preserving range-1 unitary lift found by k4, extract its
period-2 coefficients a_t(x mod 2), REBUILD it on L=6 and L=8 (no wrap coincidences), and verify exactly:
   (i) A^dagger A = 1, (ii) (A P_g) commutes with the staggered D, (iii) the kernel action on the 8 corner waves,
   (iv) the hw=1 triplet is preserved and acted on as the transposition TS.  Saves coefficients to k7_lift_coeffs.npy."""
import sys, itertools, numpy as np
sys.argv=['x']
exec(open('k3_label_lift.py').read().split('if __name__')[0])
name='C2d'; eps=1
l,A4,K4=attempt(name,eps,ntry=40,mode='triplet',seed=7)
print("L=4 residual loss",l)
# extract coefficients a[t][pr] from A4 : A[x,x+t]
coef={}
for ti,t in enumerate(offs):
    for pr in par:
        vals=[]
        for p in pts:
            if (p[0]%2,p[1]%2,p[2]%2)==pr:
                vals.append(A4[idx(*p),idx(p[0]+t[0],p[1]+t[1],p[2]+t[2])])
        vals=np.array(vals); assert np.allclose(vals,vals[0],atol=1e-9), "coefficient not period-2 uniform"
        coef[(t,pr)]=vals[0]
np.save('k7_lift_coeffs.npy',np.array([[coef[(t,pr)] for pr in par] for t in offs]))
def build(Lx):
    Nn=Lx**3; ptsn=list(itertools.product(range(Lx),repeat=3)); ix=lambda x,y,z:((x%Lx)*Lx+(y%Lx))*Lx+(z%Lx)
    Dn=np.zeros((Nn,Nn))
    for (x,y,z) in ptsn:
        eta=[1,(-1)**x,(-1)**(x+y)]
        for mu,e in enumerate([(1,0,0),(0,1,0),(0,0,1)]):
            i=ix(x,y,z); Dn[i,ix(x+e[0],y+e[1],z+e[2])]+=eta[mu]/2; Dn[i,ix(x-e[0],y-e[1],z-e[2])]-=eta[mu]/2
    Pn=np.zeros((Nn,Nn)); M=G[name]
    for p in ptsn:
        q=tuple((M@np.array(p))%Lx); Pn[ix(*q),ix(*p)]=1
    An=np.zeros((Nn,Nn),complex)
    for p in ptsn:
        pr=(p[0]%2,p[1]%2,p[2]%2)
        for t in offs:
            An[ix(*p),ix(p[0]+t[0],p[1]+t[1],p[2]+t[2])]+=coef[(t,pr)]
    Vn=np.zeros((Nn,8))
    for a,c in enumerate(corners):
        for p in ptsn: Vn[ix(*p),a]=(-1)**(c[0]*p[0]+c[1]*p[1]+c[2]*p[2])
    Vn/=np.sqrt(Nn)
    return Dn,Pn,An,Vn
for Lx in (4,6,8):
    Dn,Pn,An,Vn=build(Lx); Nn=Lx**3
    unit=np.abs(An.conj().T@An-np.eye(Nn)).max()
    S=An@Pn
    comm=np.abs(S@Dn-Dn@S).max()
    K=Vn.T@S@Vn                                   # kernel action (complex 8x8)
    ker_ok=np.abs(Dn@(S@Vn)).max()
    leak=np.linalg.norm(K[np.ix_([i for i in range(8) if i not in triplet],triplet)])
    T=K[np.ix_(triplet,triplet)]
    print(f"L={Lx}: |A^dag A - 1|max={unit:.2e}  |[A P_g, D]|max={comm:.2e}  |D (A P_g) V|max={ker_ok:.2e}  triplet leakage={leak:.2e}")
    print("     triplet block (rounded):\n",np.round(T,6))
    print("     max row support of A:",max((np.abs(An[i])>1e-8).sum() for i in range(Nn)), " offsets used within range 1 by construction")
