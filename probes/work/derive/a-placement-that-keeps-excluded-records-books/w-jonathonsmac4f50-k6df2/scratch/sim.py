import sys, time
from fiber import *
def band_spinor(k, s):
    H=np.sin(k[0])*sx+np.sin(k[1])*sy
    w,v=np.linalg.eigh(H); return v[:,0 if s<0 else 1]
def eps(k): return np.hypot(np.sin(k[0]),np.sin(k[1]))
def run(N,m,q0,T0,sig,T,comp,nt=61):
    K,H,H2,P=build(N,*m)
    J=build_J(N,K,comp)
    n=N*N
    k1=K/2+q0; k2=K/2-q0
    # group velocity of relative wave phi=e^{i k1 r}: d/dk1 [eps(k1)+eps(K-k1)]
    def Eof(k): return eps(k)+eps(K-k)
    h=1e-6
    v=np.array([(Eof(k1+np.array([h,0]))-Eof(k1-np.array([h,0])))/(2*h),(Eof(k1+np.array([0,h]))-Eof(k1-np.array([0,h])))/(2*h)])
    r0=-v*T0
    # Gaussian packet, periodic distance
    rx=np.arange(N); X,Y=np.meshgrid(rx,rx,indexing='ij')
    def pd(a,c): d=(a-c+N/2)%N-N/2; return d
    env=np.exp(-((pd(X,r0[0]))**2+(pd(Y,r0[1]))**2)/(4*sig**2))*np.exp(1j*(k1[0]*X+k1[1]*Y))
    u=np.kron(band_spinor(k1,+1),band_spinor(k2,+1))
    phi=np.zeros(4*n,complex)
    for c in range(4): phi[c::4]=env.ravel()*u[c]
    # antisymmetrise: (X phi)(r;c1,c2)=e^{iK r} phi(-r;c2,c1)
    Xop=np.zeros((4*n,4*n),dtype=complex) if False else None
    def Xapply(v):
        out=np.zeros_like(v)
        for rxx in range(N):
            for ryy in range(N):
                src=(((-rxx)%N)*N+((-ryy)%N))*4
                dst=(rxx*N+ryy)*4
                ph=np.exp(1j*(K[0]*(rxx if rxx<=N//2 else rxx-N)+K[1]*(ryy if ryy<=N//2 else ryy-N)))
                for c1 in range(2):
                    for c2 in range(2):
                        out[dst+c1*2+c2]=ph*v[src+c2*2+c1]
        return out
    psi=phi-Xapply(phi); psi=P@psi
    psi/=np.linalg.norm(psi)
    # check exchange symmetry commutes
    t0=time.time()
    ts=np.linspace(0,T,nt)
    Ht=-1j*H2.tocsc()
    states=sla.expm_multiply(Ht,psi,start=0,stop=T,num=nt,endpoint=True)
    Jt=np.array([np.vdot(s,J@s).real for s in states])
    # weight near coincidence |r|inf<=5
    mask=np.zeros(4*n,bool)
    for rxx in range(N):
        for ryy in range(N):
            a=rxx if rxx<=N//2 else rxx-N; b=ryy if ryy<=N//2 else ryy-N
            if max(abs(a),abs(b))<=5: mask[(rxx*N+ryy)*4:(rxx*N+ryy)*4+4]=True
    wt=np.array([np.linalg.norm(s[mask])**2 for s in states])
    nrm=np.array([np.linalg.norm(s)**2 for s in states])
    return ts,Jt,wt,nrm,v,r0,K,time.time()-t0

if __name__=="__main__":
    N=int(sys.argv[1]); 
    ts,Jt,wt,nrm,v,r0,K,el=run(N,(5,3),np.array([0.9,-0.6]),12.0,3.0,30.0,0)
    print("K",K,"v",v,"r0",r0,"time",el)
    for t,j,w,nn in zip(ts,Jt,wt,nrm): print(f"{t:6.2f}  J={j:+.6f}  near-weight={w:.4f} norm={nn:.8f}")
