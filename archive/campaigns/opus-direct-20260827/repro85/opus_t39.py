"""T39 - CLIFFORD CLOSURE DOES NOT FIX THE OPERATOR.  DOES DIFFEOMORPHISM
INVARIANCE FIX IT?
Everything so far used  Gamma^mu = eps_mu + iota_mu(g^-1):  the exterior part
carries NO metric and the interior part carries ALL of it.  That is one member
of a ONE-PARAMETER FAMILY that all satisfy the same Clifford algebra.  For a
diagonal metric with g_11 = A:

     Gamma^1(beta) = A^(-beta) eps_1 + A^(beta-1) iota_1^flat
     {Gamma^1, Gamma^1} = 2 A^(-beta) A^(beta-1) {eps_1, iota_1} = 2/A = 2 g^11

for EVERY beta.  beta = 0 is the split form used up to now; beta = 1/2 is the
balanced frame form  Gamma^mu = e^mu_a gamma^a  with e = sqrt(g).  Closure is
blind to beta.  The first-order diffeomorphism gate is not.

If some beta makes  metric + matter  cancel, then diffeomorphism invariance
SELECTS the operator that Clifford closure left free -- and that is a derivation,
not a choice.  Scanned finely; the residual is reported as a function of beta."""
import numpy as np, itertools
def carrier(D):
    B=[]
    for k in range(D+1): B+=[tuple(c) for c in itertools.combinations(range(D),k)]
    return B,{b:i for i,b in enumerate(B)}
def make_ops(D):
    B,IDX=carrier(D); NF=len(B)
    def epsm(a):
        M=np.zeros((NF,NF))
        for Sx in B:
            if a in Sx: continue
            T=tuple(sorted(Sx+(a,))); M[IDX[T],IDX[Sx]]=(-1)**sum(1 for i in Sx if i<a)
        return M
    def iotam(a,gi):
        M=np.zeros((NF,NF))
        for Sx in B:
            for pos,i in enumerate(Sx):
                T=tuple(x for x in Sx if x!=i); M[IDX[T],IDX[Sx]]+=(-1)**pos*gi[a,i]
        return M
    return B,IDX,NF,epsm,iotam
def Wfun(D,L,mfield,A,beta,WAVE=1):
    """A[x] = g_11(x); all other metric components 1.  Gamma^1 = A^-b eps + A^(b-1) iota."""
    B,IDX,NF,epsm,iotam=make_ops(D)
    EPS=[epsm(a) for a in range(D)]
    IOTf=[iotam(a,np.eye(D)) for a in range(D)]
    trans=[a for a in range(D) if a!=WAVE]; tot=0.0
    G1=[A[x]**(-beta)*EPS[WAVE] + A[x]**(beta-1.0)*IOTf[WAVE] for x in range(L)]
    GT=[[EPS[a]+IOTf[a] for a in range(D)] for x in range(L)]   # transverse: g_aa = 1
    for pidx in itertools.product(range(L),repeat=D-1):
        p={a:2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+=mfield[x]*np.eye(NF)
            for a in trans: Q[i:i+NF,i:i+NF]+=1j*np.sin(p[a])*GT[x][a]
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                Q[i:i+NF,j:j+NF]+=0.5*sgn*0.5*(G1[x]+G1[y])
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def gate(D,L,m0,mu,nw,beta,e=1e-4):
    xs=np.arange(L)
    xi=np.sin(2*np.pi*nw*xs/L); dxi=(2*np.pi*nw/L)*np.cos(2*np.pi*nw*xs/L)
    m=m0+mu*np.cos(2*np.pi*nw*xs/L); dm=-mu*(2*np.pi*nw/L)*np.sin(2*np.pi*nw*xs/L)
    def build(h,which):
        A=np.ones(L); mm=np.array(m,dtype=float)
        if which in ("both","metric"): A=1.0+2*h*dxi
        if which in ("both","matter"): mm=m+h*xi*dm
        return list(mm),list(A)
    o={}
    for which in ("metric","matter","both"):
        mp,Ap=build(+e,which); mm_,Am=build(-e,which)
        o[which]=(Wfun(D,L,mp,Ap,beta)-Wfun(D,L,mm_,Am,beta))/(2*e)
    return o
print("T39  the beta family.  beta=0 is the construction used so far; beta=1/2 is the")
print("     balanced frame form.  Clifford closure holds for every beta.")
print()
for D,L in ((2,16),(2,24),(4,8)):
    print(f"  d={D} L={L}")
    print(f"   {'beta':>7} {'metric':>13} {'matter':>13} {'SUM':>13} {'rel':>10}")
    best=None
    for beta in (-0.5,-0.25,0.0,0.25,0.5,0.75,1.0,1.25,1.5):
        o=gate(D,L,0.9,0.35,1,beta)
        rel=abs(o["both"])/max(abs(o["metric"]),abs(o["matter"]),1e-30)
        flag="  <== CANCELS" if rel<1e-3 else ""
        print(f"   {beta:+7.3f} {o['metric']:+13.5f} {o['matter']:+13.5f} {o['both']:+13.5f} {rel:10.6f}{flag}", flush=True)
        if best is None or rel<best[1]: best=(beta,rel)
    # refine around the minimum by solving the (linear in beta?) metric piece
    b0=best[0]
    for beta in (b0-0.12,b0-0.06,b0,b0+0.06,b0+0.12):
        o=gate(D,L,0.9,0.35,1,beta)
        rel=abs(o["both"])/max(abs(o["metric"]),abs(o["matter"]),1e-30)
        print(f"   refine {beta:+7.4f}  SUM={o['both']:+13.6f}  rel={rel:10.7f}", flush=True)
    print(flush=True)
