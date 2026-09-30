"""Kill check: transfer matrix on a 3x3 cross-section (periodic, non-bipartite, all sites carry +-1), rule at EVERY site.
rule 'nbr6' : sum of 6 neighbours == 0 (attack's exact balance, coupled version)
rule 'star7': sum of the closed 7-site star (centre included) in {-1,+1} (admissibility-form: centre conditioned on neighbours)
rule 'star7pm3': closed star sum in {-3,-1,1,3}
Reports dominant growth rate lambda per layer and log2(lambda)/9 per site."""
import numpy as np, itertools, sys
Lc=3; m=Lc*Lc
idx=lambda x,y:(x%Lc)*Lc+(y%Lc)
nb=[[idx(x+1,y),idx(x-1,y),idx(x,y+1),idx(x,y-1)] for x in range(Lc) for y in range(Lc)]
S=2**m
bits=((np.arange(S)[:,None]>>np.arange(m))&1)*2-1   # S x m of +-1
def run(rule,iters=60):
    allowed={'nbr6':{0},'star7':{-1,1},'star7pm3':{-3,-1,1,3}}[rule]
    centre = 0 if rule=='nbr6' else 1
    M=[None]*S
    T=np.zeros((S,S),dtype=np.float64)  # will hold via list of matrices
    mats=np.zeros((S,S,S),dtype=bool) if S<=512 else None
    for b in range(S):
        bb=bits[b]
        inpl=np.array([sum(bb[j] for j in nb[s]) for s in range(m)])+centre*bb
        ok=np.ones((S,S),dtype=bool)
        for s in range(m):
            tot=inpl[s]+bits[:,s][:,None]+bits[:,s][None,:]
            ok&=np.isin(tot,list(allowed))
        mats[b]=ok
    # state (a,b): vector v[a,b]; v'[b,c]=sum_a v[a,b]*mats[b][a,c]
    v=np.ones((S,S))
    lam=None
    for it in range(iters):
        vn=np.zeros((S,S))
        for b in range(S):
            vn[b,:]=v[:,b]@mats[b]
        nrm=vn.sum()/v.sum()
        v=vn/vn.sum()*S*S
        lam=nrm
    # closed-walk counts (torus) for period n via trace of transfer power is heavy; report lambda only
    return lam, mats.sum()
for rule in ('nbr6','star7','star7pm3'):
    lam,ne=run(rule)
    print(rule,'lambda~',round(lam,4),'log2(lambda)/9 =',round(np.log2(lam)/9,4) if lam>0 else None,'edges',ne,flush=True)
