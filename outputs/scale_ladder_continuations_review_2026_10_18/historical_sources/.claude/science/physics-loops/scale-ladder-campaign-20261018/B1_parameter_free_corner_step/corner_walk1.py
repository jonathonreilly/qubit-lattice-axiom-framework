import sys, itertools, numpy as np
sys.path.insert(0,'.')
exec(open('diraclib.py').read().split("Xb=np.load")[0])
Hon=H0(1.0,0.0); Hli=H0(0.0,1.0)
blon=blocks_from(Hon); blli=blocks_from(Hli)
Hon0=Hk(blon,np.zeros(3)).real
w,V=np.linalg.eigh(Hon0)
def P(lam): idx=np.abs(w-lam)<1e-6; return V[:,idx]@V[:,idx].T
lams=sorted(set(np.round(w,6)))
cands={f"1-2P[{l:+.3f}]":np.eye(12)-2*P(l) for l in lams}
cands["i*Hon-phase? skip"]=None
def W(k,Uon): return (Hk(blli,k)/np.sqrt(2))@Uon
def qe(k,Uon): return np.sort(np.angle(np.linalg.eigvals(W(k,Uon))))
rng=np.random.default_rng(0); dirs=rng.normal(size=(60,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
for name,U in cands.items():
    if U is None: continue
    e=qe(kst,U);
    # group into levels
    lv=[];
    for x in e:
        if lv and abs(x-lv[-1][0])<1e-7: lv[-1][1]+=1
        else: lv.append([x,1])
    print(name, "levels at k*:", [(round(a,4),m) for a,m in lv])
    for a,m in lv:
        if m<2: continue
        for q in (1e-3,5e-4):
            sp=[]
            for d in dirs:
                ee=np.angle(np.linalg.eigvals(W(kst+q*d,U)))
                near=np.sort(ee[np.abs(np.angle(np.exp(1j*(ee-a))))<0.05])
                sp.append((near[-1]-near[0])/(2*q) if len(near)>=2 else np.nan)
            sp=np.array(sp)
            print(f"   level {a:+.4f} (x{m}) q={q}: half-splitting/q mean {np.nanmean(sp):.5f} spread {np.nanmax(sp)-np.nanmin(sp):.2e}")
