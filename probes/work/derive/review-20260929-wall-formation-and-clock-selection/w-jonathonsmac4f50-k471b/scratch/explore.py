import itertools, collections
from fractions import Fraction
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
Lx=4
E=[(1,0),(-1,0),(0,1),(0,-1)]
OPP={0:1,1:0,2:3,3:2}
def sid(x,y): return (x%Lx)+Lx*(y%Lx)
def xy(s): return s%Lx, s//Lx
def stream_events(cfg, model):
    ev=[]
    for s,k in cfg.items():
        x,y=xy(s); t=sid(x+E[k][0],y+E[k][1])
        if t not in cfg:
            n=dict(cfg); del n[s]; n[t]=k; ev.append(n)
        else:
            k2=cfg[t]
            if k2==k: continue
            if model=='orig' or k2==OPP[k]:
                n=dict(cfg); n[s]=k2; n[t]=k; ev.append(n)
    return ev
def J(cfg):
    j=[0,0]
    for s,k in cfg.items():
        x,y=xy(s); t=sid(x+E[k][0],y+E[k][1])
        if t not in cfg: j[0]+=E[k][0]; j[1]+=E[k][1]
    return tuple(j)
def P(cfg): return (sum(E[k][0] for k in cfg.values()),sum(E[k][1] for k in cfg.values()))
def key(cfg): return tuple(sorted(cfg.items()))
def allcfg(N):
    for occ in itertools.combinations(range(Lx*Lx),N):
        for ks in itertools.product(range(4),repeat=N):
            yield dict(zip(occ,ks))
for model in ('orig','vstar'):
  for N in (2,3):
    cfgs=[key(c) for c in allcfg(N)]
    idx={c:i for i,c in enumerate(cfgs)}
    n=len(cfgs)
    rows=[];cols=[]
    for c in cfgs:
        cd=dict(c)
        for nn in stream_events(cd,model):
            rows.append(idx[key(nn)]); cols.append(idx[c])
    # generator Q: column c -> destination rate 1
    from collections import defaultdict
    A=sp.coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n)).tocsr()
    out=np.array(A.sum(axis=0)).ravel()
    Q=A-sp.diags(out)
    # sectors by P and connectivity
    nc,lab=sp.csgraph.connected_components(A,directed=True,connection='strong')
    # closed classes: strong comps with no outflow
    comp_out=defaultdict(int)
    r=A.tocoo()
    for a,b in zip(r.row,r.col):
        if lab[a]!=lab[b]: comp_out[lab[b]]+=1
    closed=[c for c in range(nc) if comp_out[c]==0]
    sizes=collections.Counter(lab)
    print(model,N,'configs',n,'strong comps',nc,'closed',len(closed))
    # stationary per closed comp
    resP=[];tot=0
    for c in closed:
        members=np.where(lab==c)[0]
        if len(members)<2: continue
        sub=Q[members][:,members].toarray()
        # solve pi Q =0
        M=np.vstack([sub, np.ones(len(members))])
        b=np.zeros(len(members)+1);b[-1]=1
        pi=np.linalg.lstsq(M,b,rcond=None)[0]
        Pv=P(dict(cfgs[members[0]]))
        Js=np.array([J(dict(cfgs[m])) for m in members])
        EJ=pi@Js
        unif=np.ones(len(members))/len(members)
        EJu=unif@Js
        tvd=0.5*np.abs(pi-unif).sum()
        resP.append((Pv,len(members),EJ,EJu,tvd))
    # print P != 0 comps
    for Pv,sz,EJ,EJu,tvd in sorted(resP, key=lambda r:(-r[1]))[:8]:
        print('  P',Pv,'size',sz,'E[J]',np.round(EJ,4),'unifE[J]',np.round(EJu,4),'TV',round(tvd,4))
