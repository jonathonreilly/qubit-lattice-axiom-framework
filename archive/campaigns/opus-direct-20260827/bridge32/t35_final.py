"""T35 - final: the full tensor structure of the induced a_1 after BOTH
extrapolations (Richardson in a at fixed s k^2, then s k^2 -> 0).
Continuum/Einstein target: 48*(b_S'2, b_Q', b_a0S', b_a0^2) = (+1, -1, 0, 0)."""
import numpy as np, sys; sys.path.insert(0,".")
CH8=[(0,1,1,0),(0,1,-1,0),(1,1,1,1),(1,0,0,0),(0,1,0,0),(0,1,1,1),(0,2,1,0),(2,1,1,1)]
def inv(c):
    a0=c[0]; Sp=c[1]+c[2]+c[3]; Qp=c[1]**2+c[2]**2+c[3]**2
    return np.array([Sp**2,Qp,a0*Sp,a0**2],float)
X=np.array([inv(c) for c in CH8])
def bvec(fn,L,s,imp):
    z=np.load(fn); lf=z['flatlam']; Vf,Rf=z['flatVR']; muf=lf+lf*lf/24.0 if imp else lf
    NORM=float(L)**4*0.06**2*(2*np.pi/L)**2; u=[]
    for c in CH8:
        lp=z[str(c)+'lam']; Vp,Rp=z[str(c)+'VR']; mu=lp+lp*lp/24.0 if imp else lp
        P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
        u.append((P-(Vp-Vf))/s/NORM)
    b,*_=np.linalg.lstsq(X,np.array(u),rcond=None)
    return 48*b, np.linalg.norm(np.array(u)-X@b)/np.linalg.norm(u)
k2=(2*np.pi/32)**2
for imp in (True,False):
    xs=[];ys=[]
    for s in (4,5,6,8,10,12,15,16,20,25):
        b32,_=bvec("struct_L32_a0.06_nk1_14.npz",32,s,imp)
        b64,_=bvec("struct_L64_a0.06_nk1_8.npz",64,4*s,imp)
        xs.append(s*k2); ys.append((4*b64-b32)/3)
    xs=np.array(xs); ys=np.array(ys)
    print(f"\nT35 {'improved' if imp else 'plain'}: Richardson then linear in s k^2 -> 0")
    print(f"  {'s k^2 window':>16} {'b(S^2)':>9} {'b(Q)':>9} {'b(a0S)':>9} {'b(a0^2)':>9}   target (+1,-1,0,0)")
    for i0,i1 in ((0,4),(1,5),(2,6),(3,7),(4,8),(2,8),(3,9)):
        M=np.stack([np.ones(i1-i0),xs[i0:i1]],1)
        c=np.linalg.lstsq(M,ys[i0:i1],rcond=None)[0]
        print(f"  [{xs[i0]:.3f},{xs[i1-1]:.3f}]{'':>5} "+" ".join(f"{c[0,j]:9.4f}" for j in range(4)))
