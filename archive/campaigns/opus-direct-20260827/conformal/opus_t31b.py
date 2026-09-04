"""T31b - the k-dependence is a LATTICE function, and my k^2 fit in T31 was the
wrong basis.  The measured d^2W/dh^2(k) is EXACTLY symmetric under k -> pi - k
(n=1 and n=L/2-1 agree to 8 digits at every L), which is the signature of a
function of sin^2 k, not of k^2 across the zone.  Refit in the correct basis
     d^2W/dh^2  =  A + B sin^2(k) [+ C sin^4(k)]
whose small-k limit is A + B k^2: B is still the graviton kinetic coefficient,
but only this fit gives a stable, convergent value.  Also compare E TRANSVERSE
to the wave (the TT-type mode) against E containing the wave axis."""
import numpy as np, itertools
def carrier(D):
    B=[]
    for k in range(D+1): B+=[tuple(c) for c in itertools.combinations(range(D),k)]
    return B,{b:i for i,b in enumerate(B)}
def ops(D):
    B,IDX=carrier(D); NF=len(B)
    def epsm(a):
        M=np.zeros((NF,NF))
        for Sx in B:
            if a in Sx: continue
            T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
        return M
    def iota(a,gi):
        M=np.zeros((NF,NF))
        for Sx in B:
            for pos,i in enumerate(Sx):
                T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
        return M
    return [epsm(a) for a in range(D)], iota, NF
CACHE={}
def W(D,L,m0,E,n,h,WAVE=1):
    key=(D,L,m0,E.tobytes(),n,h,WAVE)
    if key in CACHE: return CACHE[key]
    EPS,iota,NF=ops(D)
    prof=[float(np.cos(2*np.pi*n*x/L)) for x in range(L)]
    gi=[np.linalg.inv(np.eye(D)+h*prof[x]*E) for x in range(L)]
    GAM=[[EPS[a]+iota(a,gi[x]) for a in range(D)] for x in range(L)]
    IOT=[[iota(a,gi[x]) for a in range(D)] for x in range(L)]
    trans=[a for a in range(D) if a!=WAVE]
    tot=0.0
    for pidx in itertools.product(range(L),repeat=D-1):
        p={a:2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+=m0*np.eye(NF)
            for a in trans: Q[i:i+NF,i:i+NF]+=1j*np.sin(p[a])*GAM[x][a]
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                Q[i:i+NF,j:j+NF]+=0.25*sgn*(2*EPS[WAVE]+IOT[x][WAVE]+IOT[y][WAVE])
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    CACHE[key]=tot; return tot
def D2(D,L,m0,E,n,e=2e-3): return (W(D,L,m0,E,n,e)-2*W(D,L,m0,E,n,0.0)+W(D,L,m0,E,n,-e))/e**2
def fit(L,vals,ns):
    s2=np.array([np.sin(2*np.pi*n/L)**2 for n in ns]); d=np.array(vals)
    c1=np.polyfit(s2,d,1); r1=np.max(np.abs(d-np.polyval(c1,s2)))
    if len(ns)>=3:
        c2=np.polyfit(s2,d,2); r2=np.max(np.abs(d-np.polyval(c2,s2)))
    else: c2=[0,c1[0],c1[1]]; r2=r1
    return c1[0],c1[1],r1,c2[1],r2
E_TT=np.zeros((4,4)); E_TT[2,2]=1.0; E_TT[3,3]=-1.0        # transverse to wave axis 1
E_LN=np.zeros((4,4)); E_LN[1,1]=1.0; E_LN[3,3]=-1.0        # contains the wave axis
print("d=4  m0=0.9  wave along axis 1.  Fit  d2W/dh2 = A + B sin^2 k  (+ C sin^4 k)")
print("   E_TT = diag(0,1,0,-1)->no wave-axis component ; E_LN = diag(0,1,0,-1) with wave axis")
for nm,E in (("E transverse (TT-type)",E_TT),("E along the wave axis",E_LN)):
    print(f"  --- {nm}")
    for L in (8,10,12,14):
        ns=list(range(1,L//2)); vals=[D2(4,L,0.9,E,n) for n in ns]
        B,A,r1,B2,r2=fit(L,vals,ns); V=L**4
        print(f"    L={L:2d}  A/V={A/V:+.8f}  B/V={B/V:+.9f}  resid(lin)={r1:.3e}"
              f"   B2/V={B2/V:+.9f} resid(quad)={r2:.3e}", flush=True)
print()
print("d=4 mass dependence of the induced kinetic coefficient, correct basis (L=12, TT):")
for m0 in (0.4,0.7,1.0,1.6,2.4,3.5):
    ns=list(range(1,6)); vals=[D2(4,12,m0,E_TT,n) for n in ns]
    B,A,r1,B2,r2=fit(12,vals,ns)
    print(f"   m0={m0:<4}  B/V={B/12**4:+.9f}   A/V={A/12**4:+.8f}   resid={r1:.2e}", flush=True)
