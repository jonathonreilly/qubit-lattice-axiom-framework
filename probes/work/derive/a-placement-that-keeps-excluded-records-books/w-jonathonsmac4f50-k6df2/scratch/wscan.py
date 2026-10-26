from sim import *
import time
def windows(N,m,T0,T,nt,thr=3e-3):
    t0=time.time()
    ts,Jt,wt,nrm,v,r0,K,el=run(N,m,np.array([0.9,-0.6]),T0,3.0,T,0,nt=nt)
    # before window: initial segment while near-weight<thr ; after window: final segment from first time after peak where weight<thr until the end
    ipk=np.argmax(wt)
    b=np.where(wt[:ipk]<thr)[0]; a=np.where(wt[ipk:]<thr)[0]+ipk
    ib=(b[0],b[-1]); ia=(a[0],a[-1])
    Wb=ts[ib[1]]-ts[ib[0]]; Wa=ts[ia[1]]-ts[ia[0]]
    avgb=Jt[ib[0]:ib[1]+1].mean(); avga=Jt[ia[0]:ia[1]+1].mean()
    W=min(Wb,Wa)
    print(f"N={N} peak t={ts[ipk]:.1f} before window {ts[ib[0]]:.1f}-{ts[ib[1]]:.1f} (W={Wb:.1f}) after window {ts[ia[0]]:.1f}-{ts[ia[1]]:.1f} (W={Wa:.1f}) avgb={avgb:.6f} avga={avga:.6f} diff={avga-avgb:.6f} bound |G|>= W*diff/4 = {W*abs(avga-avgb)/4:.4f}  [{time.time()-t0:.1f}s]")
windows(48,(5,3),12.0,30.0,121,thr=1e-2)
windows(96,(10,6),30.0,70.0,161,thr=1e-2)
windows(96,(10,6),30.0,70.0,161,thr=3e-3)
