"""Kill check for T65 Test 1: geodesic (step-count) norm vs long-wavelength wave metric of a periodic graph.
Graph Laplacian symbol L(q)=sum_s (1-cos q.s). Rank-2 part is isotropic for any cubic-symmetric S;
anisotropy first shows up at rank 4 (order q^4)."""
import itertools, numpy as np
def orbit(v):
    out=set()
    for p in set(itertools.permutations(v)):
        for s in itertools.product([1,-1],repeat=3): out.add(tuple(a*b for a,b in zip(p,s)))
    return sorted(out)
sets={'NN(6)':orbit((1,0,0)),'26-star':orbit((1,0,0))+orbit((1,1,0))+orbit((1,1,1)),'fcc(12)':orbit((1,1,0))}
dirs={'100':np.array([1,0,0.]),'110':np.array([1,1,0.])/2**.5,'111':np.array([1,1,1.])/3**.5}
for name,S in sets.items():
    S=np.array(S,float)
    print(name,'D=',len(S))
    for q in (0.4,0.1,0.02):
        vals={k:np.sum(1-np.cos(S@(q*d)))/q**2 for k,d in dirs.items()}
        v=list(vals.values()); print('  |q|=%.2f  L/q^2 by direction %s  max/min=%.6f'%(q,{k:round(x,6) for k,x in vals.items()},max(v)/min(v)))
