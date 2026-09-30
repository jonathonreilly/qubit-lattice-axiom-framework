import numpy as np, json
import sea_stiffness as S
# second family: s(k) = (1-mu) sin k + mu sin(3k)/3  (speed 1 at k->0; same 8 nodes for mu < 3/4)
def s3(k, mu): return (1-mu)*np.sin(k) + mu*np.sin(3*k)/3
def kap(N,m,fun,mu,d='x'):
    ks=2*np.pi*(np.arange(N)+0.5)/N
    kx,ky,kz=np.meshgrid(ks,ks,ks,indexing='ij')
    s=np.stack([fun(kx,mu),fun(ky,mu),fun(kz,mu)],-1)
    A=np.linalg.norm(s,axis=-1); n=s/A[...,None]
    sp=np.roll(s,-m,axis=0); sm=np.roll(s,m,axis=0); Ap=np.linalg.norm(sp,axis=-1); npv=sp/Ap[...,None]
    diag=-A/8-(1/16)*np.einsum('...i,...i->...',n,sp+sm)
    pert=-(1/16)*(A-Ap)**2*(1-np.einsum('...i,...i->...',n,npv))/(A+Ap)
    a2=diag.mean()+pert.mean(); c0=-A.mean()
    return 4*(a2-c0/4)/(2-2*np.cos(2*np.pi*m/N)), c0
out=[]
for mu in [-0.6,-0.3,0.0,0.3,0.5,0.6,0.7]:
    (k1,c0),(k2,_)=kap(128,4,s3,mu),kap(128,8,s3,mu)
    q1,q2=(2*np.pi*4/128)**2,(2*np.pi*8/128)**2
    k0=(k1*q2-k2*q1)/(q2-q1)
    out.append(dict(mu=mu,kappa=float(k0),c0=float(c0))); print(out[-1],flush=True)
json.dump(out,open('T69_results_family3.json','w'),indent=1)
