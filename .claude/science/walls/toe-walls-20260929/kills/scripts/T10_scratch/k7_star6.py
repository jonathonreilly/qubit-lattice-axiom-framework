"""Static product neighbourhood (no flux): pointer S coupled Z_S X_k to N environment qubits in |0>, c_k~N(0,1), t~U[0.2,2].
chi_F = h((1+prod_{k in F}|cos 2 c_k t|)/2) (exact for pure product branch states).  R = max number of disjoint subsets
with chi>=0.9 (exhaustive).  N=6 is the Z^3 nearest-neighbour coordination number; N=12 the attack's case."""
import numpy as np, itertools, json
rng=np.random.default_rng(1234)
def h2(p):
    p=np.clip(p,1e-15,1-1e-15); return float(-p*np.log2(p)-(1-p)*np.log2(1-p))
def maxR(a,thr):
    # a[k]=|cos|; subsets ok if prod<=cut where chi>=thr  -> find cut
    N=len(a); ok={}
    for mask in range(1,1<<N):
        pr=1.0
        for k in range(N):
            if mask>>k&1: pr*=a[k]
        ok[mask]=h2((1+pr)/2)>=thr
    best=[0]*(1<<N)
    # DP over masks: best[mask]=max disjoint good subsets inside mask
    for mask in range(1,1<<N):
        b=best[mask&(mask-1)]  # drop lowest bit
        sub=mask
        while sub:
            if ok[sub] and sub&(mask&-mask): # subset containing lowest bit
                b=max(b,1+best[mask^sub])
            sub=(sub-1)&mask
        best[mask]=b
    return best[(1<<N)-1]
out={}
for N in (3,4,6):
    Rs=[]
    for _ in range(2000):
        c=rng.normal(size=N); t=rng.uniform(0.2,2.0)
        a=np.abs(np.cos(2*c*t))
        Rs.append(maxR(a,0.9))
    Rs=np.array(Rs)
    out[N]=dict(frac_R_ge_2=float((Rs>=2).mean()),frac_R_ge_3=float((Rs>=3).mean()),frac_R_eq_N=float((Rs>=N).mean()),mean=float(Rs.mean()))
    print(N,out[N],flush=True)
# CNOT point: c_k t = pi/4 for all k -> a=0 -> R=N
print('CNOT-point (all |cos|=0): R =',maxR(np.zeros(6),0.9))
json.dump(out,open('k7_star6.json','w'),indent=1)
