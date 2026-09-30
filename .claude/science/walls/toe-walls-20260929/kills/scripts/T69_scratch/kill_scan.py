import numpy as np, itertools, json, time
def make(N, sfun):
    ks=2*np.pi*(np.arange(N)+0.5)/N
    kx,ky,kz=np.meshgrid(ks,ks,ks,indexing='ij')
    s=np.stack([sfun(kx),sfun(ky),sfun(kz)],-1)
    A=np.linalg.norm(s,axis=-1); n=s/A[...,None]
    return s,A,n
def a2(s,A,n,m):
    def sh(arr,sign):
        out=arr
        for ax,mm in enumerate(m):
            if mm: out=np.roll(out,-sign*mm,axis=ax)
        return out
    sP,sM=sh(s,1),sh(s,-1)
    AP=np.linalg.norm(sP,axis=-1); nP=sP/AP[...,None]
    d=-A/8-(1/16)*np.einsum('...i,...i->...',n,sP+sM)
    p=-(1/16)*(A-AP)**2*(1-np.einsum('...i,...i->...',n,nP))/(A+AP)
    return d.mean()+p.mean()
def zone_scan(sfun,N=24,label=''):
    s,A,n=make(N,sfun); c0=-A.mean()
    # kappa from small q along x
    def kap(m):
        q=2*np.pi*m/N; return 4*(a2(s,A,n,(m,0,0))-c0/4)/(2-2*np.cos(q))
    k1,k2=kap(1),kap(2); q1,q2=(2*np.pi/N)**2,(2*np.pi*2/N)**2
    kappa=(k1*q2-k2*q1)/(q2-q1)
    mx=-1e9; worst_dev=0; rows=[]
    for m in itertools.combinations_with_replacement(range(0,N//2+1),3):
        if m==(0,0,0): continue
        v=a2(s,A,n,m)
        # real-cos normalisation: components at q=pi in an axis double
        L=sum(2-2*np.cos(2*np.pi*mm/N) for mm in m)
        comp=(c0+kappa*L)/4
        rows.append((m,v,comp,L))
        mx=max(mx,v)
    vals=np.array([r[1] for r in rows]); comps=np.array([r[2] for r in rows])
    # positive points?
    pos=[(r[0],r[1]) for r in rows if r[1]>1e-9]
    dev=np.max(np.abs(vals-comps)/np.abs(comps).clip(1e-3))
    # deviation relative to |c0|/4 scale
    dev2=np.max(np.abs(vals-comps))/(abs(c0)/4)
    return dict(label=label,c0=c0,kappa=kappa,max_a2=mx,n_positive=len(pos),positive_examples=pos[:5],
                max_abs_dev_over_c0q=dev2, rel_dev_max=dev)
out=[]
t0=time.time()
out.append(zone_scan(np.sin,24,'mu=0 (landed walk)')); print(out[-1],time.time()-t0,flush=True)
for mu in [0.25,0.4]:
    f=lambda k,mu=mu:(1-mu)*np.sin(k)+mu*np.sin(2*k)/2
    out.append(zone_scan(f,24,f'family2 mu={mu}')); print(out[-1],flush=True)
for mu in [0.3,-0.3,0.5]:
    f=lambda k,mu=mu:(1-mu)*np.sin(k)+mu*np.sin(3*k)/3
    out.append(zone_scan(f,24,f'family3 mu={mu}')); print(out[-1],flush=True)
json.dump(out,open('kill_scan_out.json','w'),indent=1,default=float)
