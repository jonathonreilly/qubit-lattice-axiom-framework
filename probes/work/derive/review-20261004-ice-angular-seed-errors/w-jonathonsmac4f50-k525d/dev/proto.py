import numpy as np, time, sys

def make_tables(L):
    N=L**3
    idx=np.arange(N); x=idx//(L*L); y=(idx//L)%L; z=idx%L
    def site(x,y,z): return ((x%L)*L+(y%L))*L+(z%L)
    NF=np.stack([site(x+1,y,z),site(x,y+1,z),site(x,y,z+1)])
    NB=np.stack([site(x-1,y,z),site(x,y-1,z),site(x,y,z-1)])
    return N,x,y,z,NF,NB

def init_E(L,M):
    N,x,y,z,_,_=make_tables(L)
    alt=lambda a:(1-2*(a%2)).astype(np.int8)
    E=np.empty((3,N),np.int8)
    E[0]=alt(y);E[1]=alt(z);E[2]=alt(x)
    return np.broadcast_to(E.reshape(1,3*N),(M,3*N)).copy()

def run(L,M,nsteps,seed):
    rng=np.random.default_rng(seed)
    N,x,y,z,NF,NB=make_tables(L)
    E=init_E(L,M)
    cs=rng.integers(0,N,M); s0=cs.copy(); ll=-np.ones(M,np.int64)
    ar=np.arange(M)
    nloops=np.zeros(M,np.int64); steps=0
    for t in range(nsteps):
        base=np.arange(3)*N
        fid=base[None,:]+cs[:,None]            # (M,3)
        bs=NB[:,cs].T                          # (M,3)
        bid=base[None,:]+bs
        ids=np.concatenate([fid,bid],1)        # (M,6)
        vals=np.take_along_axis(E,ids,1)
        want=np.concatenate([np.ones((M,3),np.int8),-np.ones((M,3),np.int8)],1)
        valid=(vals==want)&(ids!=ll[:,None])
        cnt=valid.sum(1)
        r=(rng.random(M)*cnt).astype(np.int64)
        cum=np.cumsum(valid,1)
        pos=(cum>r[:,None]).argmax(1)
        lid=ids[ar,pos]
        E[ar,lid]=-E[ar,lid]
        ll=lid
        dest=np.where(pos<3,NF[np.minimum(pos,2),cs],bs[ar,np.maximum(pos-3,0)])
        cs=dest
        done=cs==s0
        if done.any():
            d=np.nonzero(done)[0]
            nloops[d]+=1
            s0[d]=rng.integers(0,N,len(d)); cs[d]=s0[d]; ll[d]=-1
    return nloops

if __name__=="__main__":
    L=int(sys.argv[1]);M=int(sys.argv[2]);n=int(sys.argv[3])
    t=time.time();nl=run(L,M,n,1);dt=time.time()-t
    print(L,M,n,"time",dt,"loops total",nl.sum(),"mean loop len",M*n/nl.sum(),"steps/s per chain-batch",M*n/dt)
