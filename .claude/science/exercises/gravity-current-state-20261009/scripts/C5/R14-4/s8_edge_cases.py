# R14-4 s8: edge cases of the reduction.
#  (iii) the A1g (trace) pair entirely soft at k=0 (M_A1 = 0): the linear branches are still those of the traceless
#        soft system with V2_0 (Schur over traceless E only); the trace pair is O(k^2).
#  (R)   Lemma R: if the Eg block is entirely soft at k=0 (M_Eg = 0), the axis TT sector carries at most ONE linear
#        branch (proper-cubic, parity-odd terms on).
import numpy as np, itertools
import s3_mixed_models as M
rng=np.random.default_rng(5)
def model(soft12,m=14):
    Pi=np.eye(12)-soft12
    Fx=[rng.normal(size=(m,12)) for _ in M.nbrs]; Fpx=[rng.normal(size=(m,12)) for _ in M.nbrs]
    def F(k): return sum(np.exp(1j*k@x)*A@Pi + (np.exp(1j*k@x)-1)*B for x,A,B in zip(M.nbrs,Fx,Fpx))
    def H(k):
        out=np.zeros((12,12),complex)
        for R in M.G24:
            D=M.D12(R); Fk=F(R.T@k); out+=D@(Fk.conj().T@Fk)@D.T
        return out/len(M.G24)
    return H
Z6=np.zeros((6,6))
# ---- (iii): soft = traceless h (mixed angles) + full trace pair ----
thE,thT=0.7,1.1
W=M.onsite_rot(thE,thT)
soft=W@np.block([[M.PEg+M.PT2,Z6],[Z6,Z6]])@W.T + np.block([[M.PA1,Z6],[Z6,M.PA1]])
H=model(soft)
print("(iii) trace pair fully soft at k=0; mixing angles",thE,thT)
J10=np.block([[np.zeros((5,5)),np.eye(5)],[-np.eye(5),np.zeros((5,5))]])
for d in [(0,0,1),(1,1,0),(1,1,1),(1,2,3)]:
    n=np.array(d,float); n/=np.linalg.norm(n)
    H0,H1,H2=[W.T@X@W for X in M.taylor(H,n)]
    Ph=np.zeros((12,5)); Ph[:6,:]=M.L5; Pe=np.zeros((12,5)); Pe[6:,:]=M.L5
    K0=Pe.T@H0@Pe; A1=Pe.T@H1@Ph; V2=Ph.T@H2@Ph
    Hs=np.block([[V2,A1.conj().T],[A1,K0]]); wt=np.sort(np.abs(np.linalg.eigvals(1j*J10@Hs).real))
    t=1e-3; we=np.sort(np.abs(np.linalg.eigvals(1j*M.J12@H(t*n)).real))/t
    print("  n=%-9s exact 12 smallest w/k: %s"%(str(d),np.round(we[:12],4)))
    print("  %-11s theory (traceless, V2_0) : %s"%("",np.round(wt,4)))
# ---- (R): Eg entirely soft (both h and E), T2g rank-1 mixed ----
soft=np.block([[M.PEg,Z6],[Z6,M.PEg]]) + W@np.block([[M.PT2,Z6],[Z6,Z6]])@W.T
H=model(soft)
print("(R) Eg block entirely soft at k=0: axis B sector (TT1=xx-yy, TT2=xy pairs)")
PB=np.zeros((12,4)); PB[:6,0]=M.T1; PB[:6,1]=M.X; PB[6:,2]=M.T1; PB[6:,3]=M.X
Jb=np.block([[np.zeros((2,2)),np.eye(2)],[-np.eye(2),np.zeros((2,2))]])
for t in (1e-2,1e-3,1e-4):
    Hk=H(np.array([0,0,t])); HB=PB.T@Hk@PB
    leak=np.abs(PB.T@Hk@(np.eye(12)-PB@PB.T)).max()
    w=np.sort(np.abs(np.linalg.eigvals(1j*Jb@HB).real))
    print("  |k|=%.0e  B-sector |omega| = %s ; omega/|k| = %s ; omega/|k|^2 = %s ; B leak %.1e"%(t,np.round(w,8),np.round(w/t,4),np.round(w/t**2,3),leak))
