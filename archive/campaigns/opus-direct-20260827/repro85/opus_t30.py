"""T30 - DOES THE GRAVITON HAVE A KINETIC TERM?  The test that decides whether
the induced action is Einstein-Hilbert or merely some tensor equation.
Expand the rule's effective action to SECOND order in a traceless plane-wave
metric perturbation  g = flat + h cos(k.x) E,  tr E = 0, in the VACUUM (uniform
matter -- no source at all).  Write
      d^2W/dh^2 (k)  =  A + B k^2 + O(k^4).
B is the coefficient of the graviton kinetic term: B != 0 IS the induced
Einstein-Hilbert term, i.e. geometry that PROPAGATES.  (The second-order volume
change det(I + h f E) = 1 - h^2 f^2 contributes only through <cos^2> = 1/2,
which is k-INDEPENDENT, so it lands in A and leaves B clean.)"""
import numpy as np, itertools
D=2; BAS=[(),(0,),(1,),(0,1)]; IDX={b:i for i,b in enumerate(BAS)}; NF=4
def epsm(a):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        if a in Sx: continue
        T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
    return M
def iota(a,gi):
    M=np.zeros((NF,NF))
    for Sx in BAS:
        for pos,i in enumerate(Sx):
            T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
    return M
EPS=[epsm(a) for a in range(D)]
def D2(L, m0, E, n, axis=1, e=2e-3):
    sites=[(t,x) for t in range(L) for x in range(L)]; sid={s:i for i,s in enumerate(sites)}
    NS=len(sites)
    prof={s: float(np.cos(2*np.pi*n*s[axis]/L)) for s in sites}
    def W(h):
        Q=np.zeros((NF*NS,NF*NS))
        gi={s:np.linalg.inv(np.eye(D)+h*prof[s]*E) for s in sites}
        IOT={s:[iota(a,gi[s]) for a in range(D)] for s in sites}
        for s in sites:
            i=sid[s]*NF; Q[i:i+NF,i:i+NF]+=m0*np.eye(NF)
            for a in range(D):
                for sgn in (+1,-1):
                    r=((s[0]+sgn*(a==0))%L,(s[1]+sgn*(a==1))%L); j=sid[r]*NF
                    Q[i:i+NF,j:j+NF]+=0.25*sgn*(2*EPS[a]+IOT[s][a]+IOT[r][a])
        return np.linalg.slogdet(Q)[1]
    return (W(e)-2*W(0.0)+W(-e))/e**2
Ed=np.array([[1.,0.],[0.,-1.]])
for L in (12,16):
    print(f"L={L}  m0=0.9   traceless plane wave E=diag(1,-1), wave along x, VACUUM")
    ks=[]; ds=[]
    for n in range(0, L//2+1):
        k=2*np.pi*n/L; d=D2(L,0.9,Ed,n)
        ks.append(k); ds.append(d)
        print(f"   n={n:2d}  k={k:.6f}  k^2={k*k:.6f}   d2W/dh2 = {d:+.8f}", flush=True)
    ks=np.array(ks); ds=np.array(ds)
    sel=ks<=2*np.pi*3/L+1e-9        # small-k fit
    A,B=np.polyfit(ks[sel]**2, ds[sel], 1)[::-1]
    resid=ds[sel]-(B+A*ks[sel]**2)
    print(f"   small-k fit  d2W/dh2 = A + B k^2 :  A={B:+.8f}   B={A:+.8f}   "
          f"max|resid|={np.max(np.abs(resid)):.2e}")
    print(f"   GRAVITON KINETIC TERM PRESENT (B != 0): {abs(A)>1e-6}", flush=True)
    print()
print("mass dependence of the induced coupling B (Sakharov: B should depend on m):")
for m0 in (0.5,0.9,1.5,2.5):
    L=12; ks=[]; ds=[]
    for n in (1,2,3):
        k=2*np.pi*n/L; ks.append(k); ds.append(D2(L,m0,Ed,n))
    ks=np.array(ks); ds=np.array(ds)
    A,B=np.polyfit(ks**2, ds, 1)
    print(f"   m0={m0}:  B = {A:+.8f}    (A0 = {B:+.8f})", flush=True)
