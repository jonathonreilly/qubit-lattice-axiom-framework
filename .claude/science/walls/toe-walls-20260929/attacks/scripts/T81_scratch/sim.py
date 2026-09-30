"""B: level-automaton simulations on an L x L torus (site (i,j) at level n has predecessors
(i-1,j),(i,j-1),(i,j) at level n-1).  eta' (two-level noisy majority) and the actual six-state product law."""
import numpy as np, sys, json, time
from fractions import Fraction as Fr

def d123(p,q,r):
    d1=1-p**3/(p**3+q**3+4*r**3)
    d2=1-p*p*q/(p*q*(p+q)+4*r**3)
    d3=1-p*p/(p*p+q*q+r*(p+q)+2*r*r)
    return d1,d2,d3

def run_eta(p,L,T,seed,q=1.0,r=2.0,rec=None):
    rng=np.random.default_rng(seed)
    d1,d2,d3=d123(p,q,r); e1=d1; e2=max(d2,d3)
    s=np.zeros((L,L),dtype=np.int8)
    out=[]
    for n in range(1,T+1):
        a=np.roll(s,1,axis=0)   # (i-1,j)
        b=np.roll(s,1,axis=1)   # (i,j-1)
        c=s
        cnt=a+b+c
        u=rng.random((L,L))
        new=np.where(cnt>=2,1,np.where(cnt==1,(u<e2),(u<e1))).astype(np.int8)
        s=new
        if rec and n%rec==0: out.append((n,float(s.mean())))
        if s.mean()>0.9: 
            out.append((n,float(s.mean()))); break
    return out

_tab={}
def table(p,q=1.0,r=2.0):
    key=(p,q,r)
    if key in _tab: return _tab[key]
    # values 0..5 = +e1,-e1,+e2,-e2,+e3,-e3 ; phi equal p, antipodal q, orthogonal r
    def phi(u,v):
        if u==v: return p
        if u//2==v//2: return q
        return r
    cum=np.zeros((216,6))
    for v1 in range(6):
        for v2 in range(6):
            for v3 in range(6):
                w=np.array([phi(v,v1)*phi(v,v2)*phi(v,v3) for v in range(6)],dtype=float)
                w/=w.sum()
                cum[v1*36+v2*6+v3]=np.cumsum(w)
    _tab[key]=cum
    return cum

def run_actual(p,L,T,seed,q=1.0,r=2.0,rec=None):
    rng=np.random.default_rng(seed)
    cum=table(p,q,r)
    s=np.zeros((L,L),dtype=np.int8)
    out=[]
    for n in range(1,T+1):
        a=np.roll(s,1,axis=0).astype(np.int32); b=np.roll(s,1,axis=1).astype(np.int32); c=s.astype(np.int32)
        idx=a*36+b*6+c
        u=rng.random((L,L))
        cc=cum[idx]                       # (L,L,6)
        new=(u[...,None]>cc).sum(axis=-1).astype(np.int8)
        new=np.minimum(new,5)
        s=new
        if rec and n%rec==0: out.append((n,float((s!=0).mean())))
        if (s!=0).mean()>0.5:
            out.append((n,float((s!=0).mean()))); break
    return out

if __name__=="__main__":
    which=sys.argv[1]; p=float(sys.argv[2]); L=int(sys.argv[3]); T=int(sys.argv[4]); seed=int(sys.argv[5])
    f=run_eta if which=="eta" else run_actual
    t0=time.time()
    o=f(p,L,T,seed,rec=max(1,T//8))
    print(which,p,L,T,seed,[(n,round(v,4)) for n,v in o],"%.1fs"%(time.time()-t0))
