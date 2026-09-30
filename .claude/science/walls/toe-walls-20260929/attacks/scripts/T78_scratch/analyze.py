import json, glob, numpy as np
rows=[]
print("L  q  mean  err  | c_q=(m0-mq)L/q^2 +/- err | drift(first-last quarter)")
data={}
for fn in sorted(glob.glob("result_L*_seed*.json"), key=lambda f:(int(f.split('_L')[1].split('_')[0]),f)):
    r=json.load(open(fn)); L=r["L"]
    data.setdefault(L,[]).append(r)
summary={}
for L in sorted(data):
    # pool replicas from all files of this L (same q list)
    pooled={}
    for r in data[L]:
        for q,v in r["results"].items():
            pooled.setdefault(int(q),[]).extend(v["rep_means"])
    ms={q:(np.mean(v),np.std(v,ddof=1)/np.sqrt(len(v)),len(v)) for q,v in pooled.items()}
    # paired-by-index differences are not valid (different seeds) -> independent errors add
    cs={}
    for q in sorted(ms):
        if q==0: continue
        d=ms[0][0]-ms[q][0]; ed=np.hypot(ms[0][1],ms[q][1])
        cs[q]=(d*L/q**2, ed*L/q**2)
    # weighted LSQ for c using x=q^2/L, y=m: fit m=a-c x (a free), weights 1/err^2
    qs=sorted(ms); x=np.array([q**2/L for q in qs]); y=np.array([ms[q][0] for q in qs]); w=np.array([1/ms[q][1]**2 for q in qs])
    A=np.vstack([np.ones_like(x),-x]).T
    cov=np.linalg.inv(A.T@(A*w[:,None])); beta=cov@(A.T@(w*y))
    chi2=float(np.sum(w*(y-A@beta)**2))
    summary[L]={"c_fit":float(beta[1]),"c_fit_err":float(np.sqrt(cov[1,1])),"chi2":chi2,"dof":len(qs)-2,
                "per_q":{str(q):[float(cs[q][0]),float(cs[q][1])] for q in cs},
                "m0":float(ms[0][0]),"m0_err":float(ms[0][1]),"density0":float(ms[0][0]/(3*L**3)),"nrep":{str(q):ms[q][2] for q in ms}}
    print(f"L={L}: N0={ms[0][0]:.4f}({ms[0][1]:.4f}) dens={ms[0][0]/(3*L**3):.5f} | " + "  ".join(f"q={q}: c={cs[q][0]:.3f}+/-{cs[q][1]:.3f}" for q in cs) + f" | fit c={beta[1]:.3f}+/-{np.sqrt(cov[1,1]):.3f} chi2/dof={chi2:.2f}/{len(qs)-2}")
    if len(cs)==2:
        qq=sorted(cs); 
        d1=ms[0][0]-ms[qq[0]][0]; d2=ms[0][0]-ms[qq[1]][0]
        print(f"     ratio dN(q2)/dN(q1)={d2/d1:.3f}  (Gaussian expects {(qq[1]/qq[0])**2:.3f})")
json.dump(summary,open("summary.json","w"),indent=1)
# power law fit of c_L over L>=lmin
Ls=[L for L in summary]
for lmin in (6,8,12):
    LL=np.array([L for L in Ls if L>=lmin],float); 
    if len(LL)<3: continue
    c=np.array([summary[int(L)]["c_fit"] for L in LL]); e=np.array([summary[int(L)]["c_fit_err"] for L in LL])
    X=np.vstack([np.ones_like(LL),np.log(LL)]).T; W=1/(e/c)**2
    cov=np.linalg.inv(X.T@(X*W[:,None])); b=cov@(X.T@(W*np.log(c)))
    print(f"power-law c_L ~ L^-p over L>={lmin}: p={-b[1]:.3f}+/-{np.sqrt(cov[1,1]):.3f}; c(L->inf const fit)=", np.sum(c/e**2)/np.sum(1/e**2), "+/-", 1/np.sqrt(np.sum(1/e**2)))
