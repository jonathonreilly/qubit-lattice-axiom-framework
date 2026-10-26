import sys, time
from sim import *
def one(kappa,N,sigfac=3.0,Tfac=2.0):
    Kt=kappa*np.array([1.0,0.5]); m=tuple(int(round(Kt[i]*N/(2*np.pi))) for i in range(2))
    K=2*np.pi*np.array(m)/N
    q0=kappa*np.array([0.6,-0.4])
    sig=sigfac/kappa
    # speed ~ sqrt2-ish: T0 so that r0 ~ 0.28 N
    T0=0.28*N/1.2
    T=2*T0+ (0.0)
    ts,Jt,wt,nrm,v,r0,K,el=run(N,m,q0,T0,sig,T,0,nt=41)
    return K,v,r0,ts,Jt,wt,el
for kappa,N in [(0.8,40),(0.4,80),(0.2,160)]:
    K,v,r0,ts,Jt,wt,el=one(kappa,N)
    print(f"kappa={kappa} N={N} K={K} v={v} r0={r0} time={el:.1f}s")
    i0=np.argmin(wt[:len(wt)//2]); i1=len(wt)//2+np.argmin(wt[len(wt)//2:])
    print("  before J=%.8f (t=%.1f, near-weight %.4f)  after J=%.8f (t=%.1f, near-weight %.4f)  Delta=%.3e"%(Jt[i0],ts[i0],wt[i0],Jt[i1],ts[i1],wt[i1],Jt[i1]-Jt[i0]))
    sys.stdout.flush()
