import os; os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex); S=[sx,sy,sz]
def U(k):
    c=np.cos(k); s=np.sin(k); a=np.prod(c); s2=(s**2).sum()
    g=np.sqrt((1-a**2)/s2) if s2>1e-300 else 1.0
    return a*np.eye(2)-1j*g*sum(s[j]*S[j] for j in range(3))
def dU(k,j,e=1e-7):
    d=np.zeros(3); d[j]=e; return (U(k+d)-U(k-d))/(2*e)
rng=np.random.default_rng(3)
for K,lab in ((np.zeros(3),"eps=0 node K=0"),(np.array([np.pi,0,0]),"eps=pi node K=(pi,0,0)")):
    out=[]
    for r in (1e-2,1e-3,1e-4):
        vals=[]; sins=[]
        for _ in range(200):
            n=rng.normal(size=3); n/=np.linalg.norm(n); k=K+r*n
            w,v=np.linalg.eig(U(k)); eps=-np.angle(w)          # U v = e^{-i eps} v
            ip=int(np.argmax(np.sin(eps))) if True else 0       # empty band: eps in (0,pi)
            im=1-ip
            up=v[:,ip]/np.linalg.norm(v[:,ip]); um=v[:,im]/np.linalg.norm(v[:,im])
            M=[up.conj()@dU(k,j)@um for j in range(3)]
            vals.append(sum(abs(m)**2 for m in M)); sins.append(abs(np.sin(eps[ip])))
        out.append((r,np.mean(vals),np.mean(sins)))
        print(f"{lab:26s} r={r:.0e}: <sum_j |M_j|^2> = {np.mean(vals):.6f}   <|sin eps|> = {np.mean(sins):.2e}")
    ratio=out[1][1]/out[2][1]
    print(f"   ratio r=1e-3 / r=1e-4 = {ratio:.4f} ->", "PASS (finite nonzero)" if (abs(ratio-1)<0.1 and out[2][1]>1e-3) else "FAIL")
