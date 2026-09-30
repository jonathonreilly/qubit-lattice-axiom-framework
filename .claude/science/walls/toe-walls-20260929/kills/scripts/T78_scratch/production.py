"""Production: <N_f>(L,q) in the uniform ice ensemble (flip-only dynamics, physical component of the seed)."""
import numpy as np, json, sys, time
from ice_flux_mc import run_replicas
L=int(sys.argv[1]); nsamp=int(sys.argv[2]); burn=int(sys.argv[3]); seedbase=int(sys.argv[4]) if len(sys.argv)>4 else 1000
nrep_per=int(sys.argv[5]) if len(sys.argv)>5 else 10
qlist=sorted(set([0, max(1,L//4), L//2]))
qs=np.concatenate([np.full(nrep_per,q,dtype=np.int64) for q in qlist])
t=time.time()
out,diag=run_replicas(L,qs,len(qs),burn,nsamp,1,seedbase)
res={"L":L,"nsamp":nsamp,"burn":burn,"seed":seedbase,"qlist":qlist,"nrep_per":nrep_per,"time_s":time.time()-t,"results":{}}
for q in qlist:
    sel=qs==q
    x=out[sel]                       # [nrep, nsamp]
    rep=x.mean(axis=1)
    # drift check: first vs last quarter
    h=nsamp//4
    res["results"][str(q)]={"mean":float(rep.mean()),"err":float(rep.std(ddof=1)/np.sqrt(len(rep))),
        "rep_means":rep.tolist(),"first_quarter":float(x[:,:h].mean()),"last_quarter":float(x[:,-h:].mean()),
        "diag_bad":int(diag[sel,0].max()),"W":[int(v) for v in diag[sel][0,1:4]],"Wdev":int(diag[sel,4].max())}
fn=f"result_L{L}_seed{seedbase}.json"
json.dump(res,open(fn,"w"))
print(L,"done",res["time_s"],[ (q,res["results"][str(q)]["mean"],res["results"][str(q)]["err"]) for q in qlist])
