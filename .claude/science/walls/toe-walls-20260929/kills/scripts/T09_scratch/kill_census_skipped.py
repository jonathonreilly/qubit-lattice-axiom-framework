"""Kill-check: run the reps the attack's census PRUNED (an irrep repeated >2 times, s<=6), plus
a fresh-seed / 150-start rerun of the s=3,4,5 reps with E or T content.  Uses the attack's own
census.solve so any bug there is shared; independent check follows in kill_independent.py."""
import sys, numpy as np, itertools
sys.path.insert(0,'.')
from census import *
def reps_all(pool, maxdim):
    return reps_up_to(pool, maxdim)
skipped=[]
for names in reps_all(INT_IRREPS, 6):
    dim=sum(IRREP_DIM[n] for n in names)
    if all(IRREP_DIM[n]==1 for n in names): continue          # 1-dim only: lemma
    if max(names.count(n) for n in set(names))>2:
        skipped.append(names)
print(len(skipped),'pruned integer reps with s<=6')
for names in sorted(skipped,key=lambda n:sum(IRREP_DIM[x] for x in n)):
    s=sum(IRREP_DIM[n] for n in names)
    best=1e9; nsol=0
    for tau in (0.3,1.0,s-0.3):
        out=solve(names,tau,60,seed=12345)
        if out[3] is None: continue
        best=min(best,out[3]); nsol+=out[5]
    print(f"s={s} {'+'.join(names):22s} best cost {best:.2e}  n_sol {nsol}", flush=True)
