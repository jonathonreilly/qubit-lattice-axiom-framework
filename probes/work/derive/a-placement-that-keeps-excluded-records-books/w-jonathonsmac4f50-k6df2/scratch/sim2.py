import sys, time
from fiber import *
def band_spinor(k, s):
    Hh=np.sin(k[0])*sx+np.sin(k[1])*sy
    w,v=np.linalg.eigh(Hh); return v[:,0 if s<0 else 1]

def exch_apply(v,N,K):
    out=np.zeros_like(v)
    r=np.arange(N); rr=np.where(r<=N//2,r,r-N)
    for rxx in range(N):
        for ryy in range(N):
            src=(((-rxx)%N)*N+((-ryy)%N))*4; dst=(rxx*N+ryy)*4
            ph=np.exp(1j*(K[0]*rr[rxx]+K[1]*rr[ryy]))
            for c1 in range(2):
                for c2 in range(2):
                    out[dst+c1*2+c2]=ph*v[src+c2*2+c1]
    return out

def prepare(N,m,q0,sig,T0,comp=0):
    K,H,H2,P=build(N,*m); J=build_J(N,K,comp); n=N*N
    k1=K/2+q0; k2=K/2-q0
    rx=np.arange(N); X,Y=np.meshgrid(rx,rx,indexing='ij')
    pd=lambda a: (a+N/2)%N-N/2
    env=np.exp(-((pd(X))**2+(pd(Y))**2)/(4*sig**2))*np.exp(1j*(k1[0]*X+k1[1]*Y))
    u=np.kron(band_spinor(k1,+1),band_spinor(k2,+1))
    phi=np.zeros(4*n,complex)
    for c in range(4): phi[c::4]=env.ravel()*u[c]
    phi=phi-exch_apply(phi,N,K)
    phi/=np.linalg.norm(phi)
    psi0=sla.expm_multiply(+1j*H.tocsc()*T0,phi)      # free backward evolution
    pre=np.linalg.norm(psi0-P@psi0)                    # weight removed by projection (should be ~0)
    psi0=P@psi0; psi0/=np.linalg.norm(psi0)
    return K,H,H2,P,J,psi0,pre

def evolve(N,m,q0,sig,T0,T,nt,comp=0,thr=1e-2):
    K,H,H2,P,J,psi0,pre=prepare(N,m,q0,sig,T0,comp)
    n=N*N
    ts=np.linspace(0,T,nt)
    states=sla.expm_multiply(-1j*H2.tocsc(),psi0,start=0,stop=T,num=nt,endpoint=True)
    Jt=np.array([np.vdot(s,J@s).real for s in states])
    rr=np.where(np.arange(N)<=N//2,np.arange(N),np.arange(N)-N)
    mask=np.zeros(4*n,bool)
    for a in range(N):
        for b in range(N):
            if max(abs(rr[a]),abs(rr[b]))<=5: mask[(a*N+b)*4:(a*N+b)*4+4]=True
    wt=np.array([np.linalg.norm(s[mask])**2 for s in states])
    return K,ts,Jt,wt,pre

def windows(ts,Jt,wt,thr):
    ipk=int(np.argmax(wt))
    b=np.where(wt[:ipk]<thr)[0]; a=np.where(wt[ipk:]<thr)[0]+ipk
    ib=(b[0],b[-1]); ia=(a[0],a[-1])
    Wb=ts[ib[1]]-ts[ib[0]]; Wa=ts[ia[1]]-ts[ia[0]]
    avgb=Jt[ib[0]:ib[1]+1].mean(); avga=Jt[ia[0]:ia[1]+1].mean()
    return ts[ipk],(ts[ib[0]],ts[ib[1]]),(ts[ia[0]],ts[ia[1]]),min(Wb,Wa),avgb,avga

if __name__=="__main__":
    q0=np.array([0.9,-0.6])
    for N,m,T0,T,nt in [(48,(5,3),10.0,20.0,81),(96,(10,6),22.0,44.0,177)]:
        t=time.time()
        K,ts,Jt,wt,pre=evolve(N,m,q0,3.0,T0,T,nt)
        pk,wb,wa,W,avgb,avga=windows(ts,Jt,wt,1e-2)
        print(f"N={N} K={K} projection loss on initial state={pre:.2e} peak t={pk:.1f} windows before {wb} after {wa} W={W:.1f} avgb={avgb:.6f} avga={avga:.6f} diff={avga-avgb:.6f} bound={W*abs(avga-avgb)/4:.4f} [{time.time()-t:.1f}s]")
