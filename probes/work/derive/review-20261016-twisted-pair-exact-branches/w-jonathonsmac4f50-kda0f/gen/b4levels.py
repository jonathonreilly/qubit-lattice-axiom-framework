import pickle,json
from fractions import Fraction as F
from layered import *
m=(0,0,0,0)
gens,levels,ci,keep=build(m,verbose=True)
assert ci is None
seeds=[(k[2],k[1]) for k,_ in [(kd,c) for kd,c in levels] if isinstance(k,tuple)] if False else [(kd[2],kd[1]) for kd,c in levels if isinstance(kd,tuple)]
print('linear consequences used',len(seeds),'levels',len(levels))
# multi-seed pruning
needed=[set() for _ in levels]
for (L,l) in seeds: needed[L].add(l)
for L in range(len(levels)-1,-1,-1):
    kind,cofs=levels[L]
    for j in list(needed[L]):
        pass
    if L>0:
        for j in needed[L]:
            needed[L-1]|=set(cofs[j].keys())
needg=sorted({i for j in needed[0] for i in levels[0][1][j]})
print('needed gens',len(needg),'size',sum(len(q) for L,(k,c) in enumerate(levels) for j in needed[L] for q in c[j].values()))
pickle.dump({'m':m,'gens':gens,'levels':levels,'needed':[sorted(x) for x in needed],'seeds':seeds,'keep':keep,'needg':needg},open('lay_b4.pkl','wb'))
