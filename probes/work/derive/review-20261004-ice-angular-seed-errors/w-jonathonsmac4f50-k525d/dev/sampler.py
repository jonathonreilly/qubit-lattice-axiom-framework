import numpy as np, time, sys

KVEC=np.array([[0,1,1],[0,1,-1],[1,0,1],[1,0,-1],[1,1,0],[1,-1,0]])   # in units 2pi/L ; S(-k)=S(k)
AMASK=(KVEC.T==0)           # (3,6): component i has folded index 0 -> P_ii=1
BMASK=~AMASK                # component i has |index|=1 -> P_ii=1/2

def tables(L):
    N=L**3
    idx=np.arange(N); x=idx//(L*L); y=(idx//L)%L; z=idx%L
    site=lambda a,b,c:((a%L)*L+(b%L))*L+(c%L)
    NF=np.stack([site(x+1,y,z),site(x,y+1,z),site(x,y,z+1)])
    NB=np.stack([site(x-1,y,z),site(x,y-1,z),site(x,y,z-1)])
    ph=np.exp(-2j*np.pi*(KVEC[:,0:1]*x+KVEC[:,1:2]*y+KVEC[:,2:3]*z)/L)   # (6,N)
    return N,(x,y,z),NF,NB,np.ascontiguousarray(ph.T)

def init_E(L,M):
    N,(x,y,z),_,_,_=tables(L)
    alt=lambda a:(1-2*(a%2)).astype(np.int8)
    E=np.empty((3,N),np.int8); E[0]=alt(y);E[1]=alt(z);E[2]=alt(x)
    return np.broadcast_to(E.reshape(1,3*N),(M,3*N)).copy()

def amplitudes(E1,L):
    """F[i,j]=sum_x E_i(x) exp(-i k_j.x) for one config E1 (3N,) by direct sum"""
    N,(x,y,z),_,_,PH=tables(L)
    return np.einsum('is,sj->ij',E1.reshape(3,N).astype(float),PH)

def run(L,M,nkeep,burn,seed,keep_series=True,wind=False):
    ss=np.random.SeedSequence(seed)
    rng=np.random.default_rng(ss.spawn(1)[0])
    N,_,NF,NB,PH=tables(L)
    E=init_E(L,M)
    F=np.zeros((M*3,6),complex)
    F0=amplitudes(E[0],L)
    F[:]=np.tile(F0,(M,1))
    cs=rng.integers(0,N,M); s0=cs.copy(); ll=-np.ones(M,np.int64)
    ar=np.arange(M); base=np.arange(3)*N
    want=np.concatenate([np.ones((M,3),np.int8),-np.ones((M,3),np.int8)],1)
    nl=np.zeros(M,np.int64); T=burn+nkeep
    ser=np.zeros((M,T,2),np.float32)
    acc=np.zeros((M,3,6))
    nacc=np.zeros(M)
    W2=np.zeros(M); 
    while nl.min()<T:
        fid=base[None,:]+cs[:,None]
        bs=NB[:,cs].T
        ids=np.concatenate([fid,base[None,:]+bs],1)
        vals=np.take_along_axis(E,ids,1)
        valid=(vals==want)&(ids!=ll[:,None])
        cnt=valid.sum(1)
        r=(rng.random(M)*cnt).astype(np.int64)
        pos=(np.cumsum(valid,1)>r[:,None]).argmax(1)
        lid=ids[ar,pos]
        eold=E[ar,lid]
        E[ar,lid]=-eold
        ll=lid
        typ=lid//N; sit=lid-typ*N
        F[ar*3+typ]+= (-2.0*eold)[:,None]*PH[sit]
        cs=np.where(pos<3,NF[np.minimum(pos,2),cs],bs[ar,np.maximum(pos-3,0)])
        done=cs==s0
        if done.any():
            d=np.nonzero(done)[0]
            S=(np.abs(F.reshape(M,3,6)[d])**2)/N        # (nd,3,6)
            Av=(S*AMASK).sum((1,2))/AMASK.sum(); Bv=(S*BMASK).sum((1,2))/BMASK.sum()
            t=nl[d]
            ok=t<T
            if ok.any():
                dd=d[ok]; tt=t[ok]
                ser[dd,tt,0]=Av[ok]; ser[dd,tt,1]=Bv[ok]
                post=tt>=burn
                acc[dd[post]]+=S[ok][post]; nacc[dd[post]]+=1
            nl[d]+=1
            s0[d]=rng.integers(0,N,len(d)); cs[d]=s0[d]; ll[d]=-1
    return dict(E=E,F=F.reshape(M,3,6),ser=ser,acc=acc/np.maximum(nacc,1)[:,None,None],L=L,N=N)

if __name__=="__main__":
    L=int(sys.argv[1]);M=int(sys.argv[2]);nk=int(sys.argv[3]);b=int(sys.argv[4])
    t=time.time();r=run(L,M,nk,b,1);print("time",time.time()-t)
    Kc=(2*r['N']+1)/(3*r['N'])
    D=Kc*(2*r['ser'][:,b:,1]-r['ser'][:,b:,0])
    cm=D.mean(1); print("D mean",cm.mean(),"seedSE",cm.std(ddof=1)/np.sqrt(M),"naive",D.std()/np.sqrt(D.size))
    # check amplitudes vs fft
    E=r['E'][0].reshape(3,L,L,L).astype(float)
    for i in range(3):
        Fn=np.fft.fftn(E[i])
        for j,k in enumerate(KVEC): 
            assert abs(Fn[tuple(k%L)]-r['F'][0,i,j])<1e-9,(i,j,Fn[tuple(k%L)],r['F'][0,i,j])
    print("fft ok")
