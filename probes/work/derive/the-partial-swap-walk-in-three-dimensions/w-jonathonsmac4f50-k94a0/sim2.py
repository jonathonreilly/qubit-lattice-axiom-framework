import sys, numpy as np, time
from sim_lib import sg, make_tick, SEQ
NODE=np.array([np.pi/2]*3)
I2=np.eye(2,dtype=complex)
def bsymbol(k,eps,order):
    """batched symbol: k (N,3), eps (N,) -> (N,2,2)"""
    k=np.atleast_2d(k);N=k.shape[0];eps=np.broadcast_to(eps,(N,))
    def lay(j,kind,a):
        X=sg[j];Y=sg[(j+1)%3]
        cj=np.cos(k[:,j])[:,None,None];sj=np.sin(k[:,j])[:,None,None]
        g=cj*X-sj*Y if kind=='A' else cj*X+sj*Y
        aa=a[:,None,None]
        return np.cos(aa)*I2-1j*np.sin(aa)*g
    S=np.broadcast_to(I2,(N,2,2)).copy()
    if order=='pal':
        for (j,kd) in SEQ[:5]: S=S@lay(j,kd,eps/2)
        S=S@lay(SEQ[5][0],SEQ[5][1],eps)
        for (j,kd) in reversed(SEQ[:5]): S=S@lay(j,kd,eps/2)
    else:
        for (j,kd) in SEQ: S=lay(j,kd,eps)@S
    return S
def beig(k,eps,order):
    S=bsymbol(k,eps,order)
    ev,V=np.linalg.eig(S)
    ph=np.angle(ev)
    i=np.argmin(ph,axis=1)
    idx=np.arange(len(i))
    th=-ph[idx,i]
    u=V[idx,:,i]
    u/=np.linalg.norm(u,axis=1)[:,None]
    # gauge: make component 0 real positive
    u*= (np.exp(-1j*np.angle(u[:,0])))[:,None]
    return th,u
def bgrad(k,eps,order,h=1e-5):
    g=np.zeros_like(k)
    for a in range(3):
        d=np.zeros(3);d[a]=h
        g[:,a]=(beig(k+d,eps,order)[0]-beig(k-d,eps,order)[0])/(2*h)
    return g
def bberry(k,eps,order,h=2e-4):
    N=len(k);Om=np.zeros((N,3))
    for c in range(3):
        a,b=(c+1)%3,(c+2)%3
        ea=np.zeros(3);ea[a]=h;eb=np.zeros(3);eb[b]=h
        u0=beig(k,eps,order)[1];u1=beig(k+ea,eps,order)[1];u2=beig(k+ea+eb,eps,order)[1];u3=beig(k+eb,eps,order)[1]
        dot=lambda p,q:(p.conj()*q).sum(1)
        P=dot(u0,u1)*dot(u1,u2)*dot(u2,u3)*dot(u3,u0)
        Om[:,c]=-np.angle(P)/h**2
    return Om
def cloud(m,gd,k0,eps0,g,T,order,sigma,anom,Nr=600,seed=0):
    m=np.array(m,float);m/=np.linalg.norm(m);gd=np.array(gd,float);gd/=np.linalg.norm(gd)
    rng=np.random.default_rng(seed)
    x=rng.normal(size=(Nr,3))*sigma
    q=k0*m+rng.normal(size=(Nr,3))/(2*sigma)
    x=np.concatenate([x,-x]);q=np.concatenate([q,2*k0*m-q])   # antithetic
    nt=int(round(T/(2*eps0)))
    def rhs(x,q):
        w=1+g*(x@gd)
        k=NODE+q
        eps=eps0*w
        v=bgrad(k,eps,order)
        dw=1e-5
        dEde=(beig(k,eps*(1+dw),order)[0]-beig(k,eps*(1-dw),order)[0])/(2*dw*eps)   # dtheta/deps
        kd=-(dEde*eps0*g)[:,None]*gd[None,:]
        if anom:
            Om=bberry(k,eps,order)
            v=v-np.cross(kd,Om)
        return v,kd
    X=x.copy();Q=q.copy()
    for _ in range(nt):
        k1x,k1q=rhs(X,Q)
        k2x,k2q=rhs(X+0.5*k1x,Q+0.5*k1q)
        k3x,k3q=rhs(X+0.5*k2x,Q+0.5*k2q)
        k4x,k4q=rhs(X+k3x,Q+k3q)
        X=X+(k1x+2*k2x+2*k3x+k4x)/6;Q=Q+(k1q+2*k2q+2*k3q+k4q)/6
    return (X-x).mean(0)
def prep(m,k0,eps0,order,L,sigma,x0):
    m=np.array(m,float);m/=np.linalg.norm(m)
    q0=k0*m
    n=np.fft.fftfreq(L,1.0/L)  # integer indices
    kg=2*np.pi*n/L
    KX,KY,KZ=np.meshgrid(kg,kg,kg,indexing='ij')
    # wrap momentum relative to q0
    def wrap(a,c): return (a-c+np.pi)%(2*np.pi)-np.pi
    D=np.stack([wrap(KX,q0[0]),wrap(KY,q0[1]),wrap(KZ,q0[2])],-1)
    f=np.exp(-(D**2).sum(-1)*sigma**2)     # |f|^2 has std 1/(2 sigma)
    mask=f>1e-7
    kk=np.stack([KX,KY,KZ],-1)[mask]
    # physical momentum relative to node: q = k (the node shift is applied in real space by i^(x+y+z))
    th,u=beig(NODE+kk,np.full(len(kk),eps0),order)
    psik=np.zeros((L,L,L,2),complex)
    ph=np.exp(-1j*(kk@x0))
    psik[mask]=(f[mask]*ph)[:,None]*u
    # psi(x)=sum_k psik e^{ikx}
    psi=np.fft.ifftn(psik,axes=(0,1,2))*L**3
    X=np.stack(np.meshgrid(*[np.arange(L)]*3,indexing='ij'),-1)
    psi=psi*np.exp(1j*np.pi/2*X.sum(-1))[...,None]
    psi/=np.sqrt((np.abs(psi)**2).sum())
    return psi,X
def run_sim(m,gd,k0,eps0,g,T,order,L,sigma):
    m=np.array(m,float);m/=np.linalg.norm(m);gd=np.array(gd,float);gd/=np.linalg.norm(gd)
    ctr=np.array([L/2]*3)
    x0=ctr-m*T/2
    psi,X=prep(m,k0,eps0,order,L,sigma,x0)
    dens0=(np.abs(psi)**2).sum(-1)
    c0=np.array([(dens0*X[...,a]).sum() for a in range(3)])
    w=1+g*((X-ctr)@gd)
    tick=make_tick(w,eps0,order)
    nt=int(round(T/(2*eps0)))
    for _ in range(nt): psi=tick(psi)
    dens=(np.abs(psi)**2).sum(-1)
    cen=np.array([(dens*X[...,a]).sum() for a in range(3)])
    edge=sum(dens.take(range(0,3),axis=a).sum()+dens.take(range(L-3,L),axis=a).sum() for a in range(3))
    return cen-c0,edge,nt
if __name__=='__main__':
    m=eval(sys.argv[1]);gd=eval(sys.argv[2]);k0=float(sys.argv[3]);eps0=float(sys.argv[4]);order=sys.argv[5];L=int(sys.argv[6]);sigma=float(sys.argv[7]);T=float(sys.argv[8])
    g=0.004
    t=time.time()
    res={}
    for sgn in (1,-1):
        d,edge,nt=run_sim(m,gd,k0,eps0,sgn*g,T,order,L,sigma)
        res[sgn]=d
        print('sim g sign',sgn,np.round(d,4),'edge %.1e'%edge,'ticks',nt,'t=%.0f'%(time.time()-t),flush=True)
    odd=(res[1]-res[-1])/2
    print('SIM odd-in-g',np.round(odd,4))
    for anom in (False,True):
        p=(cloud(m,gd,k0,eps0,g,T,order,sigma,anom)-cloud(m,gd,k0,eps0,-g,T,order,sigma,anom))/2
        print('CLOUD anom=',anom,np.round(p,4),'t=%.0f'%(time.time()-t),flush=True)
