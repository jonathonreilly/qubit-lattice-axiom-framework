"""T37 - CONTROL THE GATE BEFORE TRUSTING ITS VERDICT.
Result 19 concluded 'not diffeomorphism invariant' from a first-order gate.
But an infinitesimal TRANSLATION is also a diffeomorphism, and a lattice cannot
represent one: only integer shifts are lattice symmetries.  So the gate must be
controlled first.

  CONTROL A  xi = constant (pure translation): delta g = 0, delta m = xi d_1 m.
             A sound gate must return ~0.  If it does not, the gate is measuring
             lattice-translation breaking, not diffeomorphism breaking, and
             Result 19's verdict must be withdrawn or heavily qualified.
  CONTROL B  the same, as a function of how SMOOTH the matter field is (wave
             number p): lattice breaking must die as the field gets smoother;
             a structural failure must not.
  CONTROL C  an exact one-site translation, which is a lattice symmetry: must be 0."""
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
def Wfun(D,L,mfield,gfield,WAVE=1):
    B,IDX,NF,epsm,iotam=make_ops(D)
    EPS=[epsm(a) for a in range(D)]
    gi=[np.linalg.inv(gfield[x]) for x in range(L)]
    IOT=[[iotam(a,gi[x]) for a in range(D)] for x in range(L)]
    GAM=[[EPS[a]+IOT[x][a] for a in range(D)] for x in range(L)]
    trans=[a for a in range(D) if a!=WAVE]
    tot=0.0
    for pidx in itertools.product(range(L),repeat=D-1):
        p={a:2*np.pi*pidx[i]/L for i,a in enumerate(trans)}
        Q=np.zeros((L*NF,L*NF),dtype=complex)
        for x in range(L):
            i=x*NF
            Q[i:i+NF,i:i+NF]+=mfield[x]*np.eye(NF)
            for a in trans: Q[i:i+NF,i:i+NF]+=1j*np.sin(p[a])*GAM[x][a]
            for sgn in (+1,-1):
                y=(x+sgn)%L; j=y*NF
                Q[i:i+NF,j:j+NF]+=0.25*sgn*(2*EPS[WAVE]+IOT[x][WAVE]+IOT[y][WAVE])
        tot+=float(np.real(np.linalg.slogdet(Q)[1]))
    return tot
def m_of(L,m0,mu,pw,shift=0.0):
    xs=np.arange(L)+shift
    return list(m0+mu*np.cos(2*np.pi*pw*xs/L))
def flat(D,L): return [np.eye(D) for _ in range(L)]
print("T37  CONTROL A/B: pure translation (delta g = 0, delta m = xi d_1 m, xi const)")
print("     the gate must return ~0 for a sound test of diffeomorphism invariance")
print()
print(f"   {'d':>2} {'L':>3} {'p':>2} {'dW/dh (translation)':>24} {'|dW/dh| / |matter piece of T35|':>34}")
for D,L in ((4,8),(4,10),(2,12),(2,16)):
    for pw in (1,2,3):
        e=1e-4
        wp=Wfun(D,L,m_of(L,0.9,0.35,pw,shift=+e),flat(D,L))
        wm=Wfun(D,L,m_of(L,0.9,0.35,pw,shift=-e),flat(D,L))
        d=(wp-wm)/(2*e)
        print(f"   {D:2d} {L:3d} {pw:2d} {d:+24.10f}", flush=True)
print()
print("   CONTROL C: exact ONE-SITE translation (a genuine lattice symmetry)")
for D,L in ((4,8),(2,12)):
    a=Wfun(D,L,m_of(L,0.9,0.35,1,shift=0.0),flat(D,L))
    b=Wfun(D,L,m_of(L,0.9,0.35,1,shift=1.0),flat(D,L))
    print(f"   d={D} L={L}:  W(shift 0) = {a:.10f}   W(shift 1) = {b:.10f}   diff = {abs(a-b):.3e}", flush=True)
print()
print("   READING: if CONTROL A is ~0 the gate is sound and Result 19 stands.")
print("   If CONTROL A is comparable to the T35 residual, Result 19 is measuring")
print("   the lattice's inability to represent an infinitesimal translation.")
