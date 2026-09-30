# Kill check T12: is exponent 3 reachable by a cubic-symmetric (about a seed) site-once NN order?
# Shell order: orient every NN edge outward in l1 radius from the centre site (edges always change |x-c|_1 by exactly 1).
import sys; sys.argv=["x"]
import numpy as np, json
import interval_exponent as ie
L=61; c=L//2
X,Y,Z=np.meshgrid(*(np.arange(L),)*3,indexing="ij")
tt=(np.abs(X-c)+np.abs(Y-c)+np.abs(Z-c))
t=tt.reshape(-1).astype(float)+1e-9*np.random.default_rng(0).random(L**3)
P,rank,pos=ie.grid_preds(t,L)
for ax in range(3):
    a=np.abs(np.diff(tt,axis=ax)); assert (a==1).all()
print("all NN edges change l1 radius by exactly 1: OK")
def rk(x,y,z): return rank[(x*L+y)*L+z]
targets={"diag":(c+28,c+28,c+28),"generic":(c+25,c+17,c+9),"axis":(c+28,c,c)}
out={}
hs=[2,3,4,5,6,8,10,12,14,16,18,20,24,28,32,40,50]
for name,(x,y,z) in targets.items():
    yv=rk(x,y,z)
    lp=ie.anc_lp(P,int(yv))
    mx={}
    for h in hs:
        cand=np.nonzero(lp==h)[0]
        if len(cand)==0: continue
        best=0
        for xx in cand:
            n=ie.interval_count(P,int(xx),int(yv),lp)
            best=max(best,n)
        mx[h]=best
    hh=sorted(k for k in mx if k>=4)
    lx=np.log(hh); ly=np.log([mx[h] for h in hh])
    p_all=np.polyfit(lx,ly,1)[0]
    k=max(1,len(hh)//3)
    p_hi=(ly[-1]-ly[-k-1])/(lx[-1]-lx[-k-1])
    out[name]=dict(maxN=mx,p_max=float(p_all),p_upper_third=float(p_hi),ratio=[mx[h]/ie.B3(h) for h in hh])
    print(name,"p_max=%.2f upper third=%.2f"%(p_all,p_hi),"max N/B3 =%.3f"%max(out[name]['ratio']),"h range",hh[0],hh[-1])
    print("   maxN",{h:mx[h] for h in list(mx)[:12]})
json.dump(out,open("shell_order_results.json","w"),indent=1)
