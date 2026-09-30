import numpy as np
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
def kappa(sfun,N=96):
    s,A,n=make(N,sfun); c0=-A.mean(); ks=[]
    for m in (2,3,4):
        q=2*np.pi*m/N; ks.append((q*q,4*(a2(s,A,n,(m,0,0))-c0/4)/(2-2*np.cos(q))))
    cf=np.polyfit([a for a,_ in ks],[b for _,b in ks],2)
    return cf[-1],c0
res={}
print('family3 s=(1-mu)sin k + mu sin3k/3  (all 8 species keep |speed| = 1)')
for mu in [0,0.1,0.25,0.3,0.4,0.5]:
    k,c0=kappa(lambda x,mu=mu:(1-mu)*np.sin(x)+mu*np.sin(3*x)/3); res[mu]=k
    print(' mu',mu,'kappa',round(k,5),'c0',round(c0,5),' -c0/12',round(-c0/12,5),' c0+12k',round(c0+12*k,4))
sel=[res[m] for m in (0,0.25,0.4)]; sel2=[res[m] for m in (0,0.1,0.25,0.3,0.4,0.5)]
print('spread (max-min)/mean over registered mu {0,0.25,0.4}:',(max(sel)-min(sel))/np.mean(sel))
print('spread over mu in [0,0.5]:',(max(sel2)-min(sel2))/np.mean(sel2))
