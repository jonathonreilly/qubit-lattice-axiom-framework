import numpy as np, itertools
def make(N,sfun):
    ks=2*np.pi*(np.arange(N)+0.5)/N
    kx,ky,kz=np.meshgrid(ks,ks,ks,indexing='ij')
    s=np.stack([sfun(kx),sfun(ky),sfun(kz)],-1); A=np.linalg.norm(s,axis=-1); return s,A,s/A[...,None]
def a2(s,A,n,m):
    def sh(arr,sign):
        out=arr
        for ax,mm in enumerate(m):
            if mm: out=np.roll(out,-sign*mm,axis=ax)
        return out
    sP,sM=sh(s,1),sh(s,-1); AP=np.linalg.norm(sP,axis=-1); nP=sP/AP[...,None]
    d=-A/8-(1/16)*np.einsum('...i,...i->...',n,sP+sM)
    p=-(1/16)*(A-AP)**2*(1-np.einsum('...i,...i->...',n,nP))/(A+AP)
    return d.mean()+p.mean()
# q fixed physically: q = 2 pi m/N with several N to see mesh convergence at fixed q
res={}
for N,ms in [(96,[1,2,3,4,6]),(144,[1,2,3,4,6]),(192,[1,2,3,4,6])]:
    s,A,n=make(N,np.sin); c0=-A.mean()
    ks=[]
    for m in ms:
        q=2*np.pi*m/N; k=4*(a2(s,A,n,(m,0,0))-c0/4)/(2-2*np.cos(q)); ks.append((q,k))
    q2=np.array([q*q for q,_ in ks]); kk=np.array([k for _,k in ks])
    # polynomial fit kappa(q^2)=k0+k1 q^2+k2 q^4 using smallest-q points where mesh error is small
    sel=[i for i,(q,_) in enumerate(ks) if q>0.06]
    cf=np.polyfit(q2[sel],kk[sel],2)
    res[N]=(c0,cf[-1],ks)
    print(N,'c0',c0,'kappa0 (quad fit)',cf[-1],'-c0/12',-c0/12,'diff',cf[-1]+c0/12,flush=True)
    for q,k in ks: print('   q',round(q,4),'kappa(q)',k)
