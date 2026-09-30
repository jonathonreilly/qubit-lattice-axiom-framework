import math, itertools, importlib.util
from collections import Counter
spec = importlib.util.spec_from_file_location('t', 'test_T73.py')
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
for L in (3,4,5,6):
    ms=t.sym_maps(L); print(L,"distinct symmetry maps:",len({tuple(m) for m in ms}))
    # independent: dihedral group via numpy-free rot/reflect of the pattern
    n=L*L; sites=[(i,j) for i in range(L) for j in range(L)]
    def transforms(p):
        i,j=p; res=[]
        for (a,b) in ((i,j),(i,L-1-j),(L-1-i,j),(L-1-i,L-1-j),(j,i),(j,L-1-i),(L-1-j,i),(L-1-j,L-1-i)): res.append((a,b))
        return res
    outs=Counter(); tot=0
    _,adj=t.grid_adj(L,2)
    for g in range(8):
        base=[transforms(p)[g][0]*L+transforms(p)[g][1] for p in sites]
        for s in range(n):
            order=base[s:]+base[:s]; st=t.raster_fill(0,order,adj); outs[st]+=1; tot+=1
    S=-sum(c/tot*math.log(c/tot) for c in outs.values())
    print("  independent S_seed=",round(S,4),"outs",len(outs),"| attack:",round(t.seed_law_entropy(L)[0],4),t.seed_law_entropy(L)[1])
