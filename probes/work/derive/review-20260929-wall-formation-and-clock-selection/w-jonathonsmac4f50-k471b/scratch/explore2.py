import itertools, collections, sys
import numpy as np, scipy.sparse as sp
Lx=4
E=[(1,0),(-1,0),(0,1),(0,-1)]
OPP={0:1,1:0,2:3,3:2}
def sid(x,y): return (x%Lx)+Lx*(y%Lx)
def xy(s): return s%Lx, s//Lx
def cross2(p,c): return p[0]*c[1]-p[1]*c[0]
_cls={}
def class_moves(loc,ks):
    key=(tuple(loc),ks)
    if key in _cls: return _cls[key]
    Pt=(sum(E[k][0] for k in ks),sum(E[k][1] for k in ks)); Lt=sum(cross2(p,E[k]) for p,k in zip(loc,ks))
    out=[]
    for cand in itertools.product(range(4),repeat=len(ks)):
        if cand==ks: continue
        P2=(sum(E[k][0] for k in cand),sum(E[k][1] for k in cand)); L2=sum(cross2(p,E[k]) for p,k in zip(loc,cand))
        if P2==Pt and L2==Lt: out.append(cand)
    _cls[key]=out; return out
def events(cfg,model,gamma):
    ev=[]
    for s,k in cfg.items():
        x,y=xy(s); t=sid(x+E[k][0],y+E[k][1])
        if t not in cfg:
            n=dict(cfg); del n[s]; n[t]=k; ev.append((1.0,n))
        else:
            k2=cfg[t]
            if k2==k: continue
            if model=='orig' or k2==OPP[k]:
                n=dict(cfg); n[s]=k2; n[t]=k; ev.append((1.0,n))
    for y in range(Lx):
        for x in range(Lx):
            sites=[sid(x,y),sid(x+1,y),sid(x,y+1),sid(x+1,y+1)]; loc=[(0,0),(1,0),(0,1),(1,1)]
            occ=[i for i in range(4) if sites[i] in cfg]
            if len(occ)<2: continue
            ks=tuple(cfg[sites[i]] for i in occ)
            for cand in class_moves([loc[i] for i in occ],ks):
                n=dict(cfg)
                for i,kk in zip(occ,cand): n[sites[i]]=kk
                ev.append((gamma,n))
    return ev
def J(cfg):
    j=[0,0]
    for s,k in cfg.items():
        x,y=xy(s); t=sid(x+E[k][0],y+E[k][1])
        if t not in cfg: j[0]+=E[k][0]; j[1]+=E[k][1]
    return tuple(j)
def P(cfg): return (sum(E[k][0] for k in cfg.values()),sum(E[k][1] for k in cfg.values()))
def key(cfg): return tuple(sorted(cfg.items()))
N=int(sys.argv[1]); gamma=float(sys.argv[2])
cfgs=[key(dict(zip(occ,ks))) for occ in itertools.combinations(range(Lx*Lx),N) for ks in itertools.product(range(4),repeat=N)]
idx={c:i for i,c in enumerate(cfgs)}; n=len(cfgs)
V=Lx*Lx
for model in ('orig','vstar'):
    rows=[];cols=[];vals=[]
    for c in cfgs:
        for r,nn in events(dict(c),model,gamma):
            rows.append(idx[key(nn)]); cols.append(idx[c]); vals.append(r)
    A=sp.coo_matrix((vals,(rows,cols)),shape=(n,n)).tocsr()
    out=np.array(A.sum(axis=0)).ravel(); Q=A-sp.diags(out)
    nc,lab=sp.csgraph.connected_components(A,directed=True,connection='strong')
    comp_out=collections.defaultdict(int); r=A.tocoo()
    for a,b in zip(r.row,r.col):
        if lab[a]!=lab[b]: comp_out[lab[b]]+=1
    closed=[c for c in range(nc) if comp_out[c]==0]
    print(model,'N',N,'gamma',gamma,'comps',nc,'closed',len(closed))
    res=[]
    for c in closed:
        mem=np.where(lab==c)[0]
        if len(mem)<2: continue
        sub=Q[mem][:,mem].toarray()
        M=np.vstack([sub,np.ones(len(mem))]); b=np.zeros(len(mem)+1); b[-1]=1
        pi=np.linalg.lstsq(M,b,rcond=None)[0]
        Pv=P(dict(cfgs[mem[0]])); Js=np.array([J(dict(cfgs[m])) for m in mem])
        EJ=pi@Js; EJu=Js.mean(axis=0)
        tv=0.5*np.abs(pi-1/len(mem)).sum()
        res.append((len(mem),Pv,EJ,EJu,tv))
    for sz,Pv,EJ,EJu,tv in sorted(res,key=lambda r:-r[0])[:10]:
        ratio=None
        if Pv[0]!=0: ratio=EJ[0]/Pv[0]
        elif Pv[1]!=0: ratio=EJ[1]/Pv[1]
        print('  size',sz,'P',Pv,'E[J]',np.round(EJ,5),'unifE[J]',np.round(EJu,5),'ratio',None if ratio is None else round(ratio,5),'canon',round((V-N)/(V-1),5),'TV',round(tv,4))
