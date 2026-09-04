"""T32 - IS THE INDUCED KINETIC TERM DIFFEOMORPHISM INVARIANT?
The decisive test of whether Result 17's response is GRAVITY or just some
metric-dependent tensor.  A cross-lane review objects that the endpoint-only
transport has trivial closed-loop holonomy and so cannot carry Levi-Civita
curvature.  Holonomy is not what the effective action measures, but the
objection has a sharp falsifier: an Einstein-Hilbert term is diffeomorphism
invariant, so it must NOT respond to a PURE-GAUGE metric perturbation.

With the wave along axis 1 and xi_nu = a_nu sin(k x_1)/k, a_nu PERPENDICULAR to
the wave:  h_(mu,nu) = d_mu xi_nu + d_nu xi_mu  gives  h_(1,2) = h_(2,1) =
a cos(k x_1)  -- traceless, and PURE GAUGE (a diffeomorphism, no geometry).
The physical mode at the same k has BOTH indices transverse: h_(2,3) or
diag(0,0,1,-1).
      induced Einstein-Hilbert  ==>  B(TT) != 0  and  B(gauge) -> 0
      no diff invariance        ==>  B(gauge) comparable to B(TT)
Both are measured in the same run, at the same k, same lattice, same mass."""
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
    return [epsm(a) for a in range(D)],iota,NF
def W(D,L,m0,E,n,h,WAVE=1):
    EPS,iota,NF=ops(D)
    prof=[float(np.cos(2*np.pi*n*x/L)) for x in range(L)]
    gi=[np.linalg.inv(np.eye(D)+h*prof[x]*E) for x in range(L)]
    IOT=[[iota(a,gi[x]) for a in range(D)] for x in range(L)]
    GAM=[[EPS[a]+IOT[x][a] for a in range(D)] for x in range(L)]
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
    return tot
def D2(D,L,m0,E,n,e=2e-3): return (W(D,L,m0,E,n,e)-2*W(D,L,m0,E,n,0.0)+W(D,L,m0,E,n,-e))/e**2
def fitB(L,ns,vals):
    s2=np.array([np.sin(2*np.pi*n/L)**2 for n in ns])
    c=np.polyfit(s2,np.array(vals),1)
    return c[0],c[1],float(np.max(np.abs(np.array(vals)-np.polyval(c,s2))))
D=4; WAVE=1
E_TT   = np.zeros((D,D)); E_TT[2,2]=1.0;  E_TT[3,3]=-1.0        # both indices transverse
E_TTo  = np.zeros((D,D)); E_TTo[2,3]=E_TTo[3,2]=1.0             # off-diag, both transverse
E_GAUGE= np.zeros((D,D)); E_GAUGE[1,2]=E_GAUGE[2,1]=1.0         # ONE index along the wave: PURE GAUGE
E_GAU2 = np.zeros((D,D)); E_GAU2[1,3]=E_GAU2[3,1]=1.0           # the other pure-gauge polarisation
MODES={"TT  diag(0,0,1,-1)":E_TT, "TT  offdiag(2,3)":E_TTo,
       "GAUGE offdiag(1,2)":E_GAUGE, "GAUGE offdiag(1,3)":E_GAU2}
print("T32  d=4  m0=0.9  wave along axis 1.  d2W/dh2 = A + B sin^2 k, per site.")
print("     PHYSICAL modes have both indices transverse; PURE-GAUGE modes have one along the wave.")
print()
for L in (8,10,12):
    ns=list(range(1,L//2)); V=L**4
    print(f"  L={L}  (interior n = {ns})")
    for nm,E in MODES.items():
        vals=[D2(D,L,0.9,E,n) for n in ns]
        B,A,r=fitB(L,ns,vals)
        print(f"    {nm:22s}  A/V={A/V:+.8f}   B/V={B/V:+.9f}   resid={r:.2e}"
              f"   raw d2 = {[f'{v:.4f}' for v in vals]}", flush=True)
    print(flush=True)
print("  READING: if B/V(gauge) is zero (or vanishes as L grows) while B/V(TT) is not,")
print("  the induced kinetic term is diffeomorphism invariant -- an Einstein-Hilbert term.")
print("  If both are comparable, the cross-lane review is right and this is not gravity.")
