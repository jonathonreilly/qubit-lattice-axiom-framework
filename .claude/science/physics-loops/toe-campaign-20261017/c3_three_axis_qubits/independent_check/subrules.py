# For the 23/31 sets: which single-orbit deletions / the shared 15-core / complements admit a -1-free signing (local)?
import sys,pickle,itertools
sys.path.insert(0,'.')
from core import *
from signs import elim_masked, solve
D=pickle.load(open('B.pkl','rb')); reps,cl=D['reps'],D['cliques']; cl=sorted(cl,key=len)
def ok(c):
    items=[(to_op(T,s,5),1<<k) for k,u in enumerate(c) for T,s in reps[u][1].items()]
    _,eqs=elim_masked(items,375); return solve(eqs,len(c))[0]
core=set(cl[8])&set(cl[9])
print('core15 solvable:',ok(sorted(core)))
for c in cl[8:10]:
    rest=sorted(set(c)-core); print(len(c),'non-core part solvable:',ok(rest))
    print('  single deletions solvable:',sum(ok([v for v in c if v!=u]) for u in c))
# greedy: largest -1-free subsets of the core
best=0
for r in range(15,0,-1):
    for sub in itertools.combinations(sorted(core),r):
        if ok(list(sub)): best=r; break
    if best: break
print('largest -1-free subset of core15 has',best,'orbits')
