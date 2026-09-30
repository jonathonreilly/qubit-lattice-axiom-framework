# Kill check T12: does the attack's "25 l1-nearest ancestors" estimator understate the LARGEST interval for site-once Eden orders?
# Compare max N over (a) 25 nearest (attack), (b) 25 farthest by l1 (d1 close to h), (c) 150 random ancestors at exact height h.
import sys; sys.argv=["x"]
import numpy as np, json
import interval_exponent as ie
rng=np.random.default_rng(7)
Lg=61
hs=[2,3,4,5,6,8,10,12,14,16,18,20,24,28,32]
res={}
for name,mode in (("eden_point","point"),("eden_plane","plane")):
    t=ie.eden_times(Lg,seed_plane=(mode=="plane"))
    P,rank,pos=ie.grid_preds(t,Lg)
    ys=rank[ie.pick_ys(Lg,12,mode)]
    A={h:[] for h in hs};B={h:[] for h in hs};C={h:[] for h in hs};D={h:[] for h in hs}
    for y in ys:
        lp=ie.anc_lp(P,int(y))
        for h in hs:
            cand=np.nonzero(lp==h)[0]
            if len(cand)==0: continue
            d=ie.d1(pos,cand,int(y),Lg,False)+1e-3*rng.random(len(cand))
            o=np.argsort(d)
            near=cand[o[:25]]; far=cand[o[-25:]]
            rnd=cand[rng.choice(len(cand),size=min(150,len(cand)),replace=False)]
            for grp,store in ((near,A),(far,B),(rnd,C)):
                for x in grp: store[h].append(ie.interval_count(P,int(x),int(y),lp))
            D[h].append(float(np.mean(d[o[-25:]])))
    def fit(S):
        hh=[h for h in hs if h>=4 and len(S[h])>=3]
        m=[max(S[h]) for h in hh]
        return float(np.polyfit(np.log(hh),np.log(m),1)[0]), dict(zip(hh,m))
    out={}
    for lab,S in (("near25_attack",A),("far25",B),("random150",C)):
        p,mm=fit(S); out[lab]=dict(p_max=p,maxN=mm)
    # union max
    U={h:A[h]+B[h]+C[h] for h in hs}
    p,mm=fit(U); out["union"]=dict(p_max=p,maxN=mm)
    out["mean_d1_of_far25"]={h:float(np.mean(D[h])) for h in hs if D[h]}
    res[name]=out
    print(name,{k:round(v['p_max'],2) for k,v in out.items() if isinstance(v,dict) and 'p_max' in v})
    print("  maxN near vs far vs union at h=8,16,32:",[(h,out['near25_attack']['maxN'].get(h),out['far25']['maxN'].get(h),out['union']['maxN'].get(h)) for h in (8,16,32)])
    print("  mean d1 of far25:",{h:round(v,1) for h,v in out['mean_d1_of_far25'].items() if h in (8,16,32)})
json.dump(res,open("estimator_bias_results.json","w"),indent=1)
