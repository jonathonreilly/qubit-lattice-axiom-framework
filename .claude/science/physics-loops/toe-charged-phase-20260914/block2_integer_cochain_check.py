"""Integer contracting-homotopy certificates for rectangular cell complexes."""
from itertools import product,combinations
from pathlib import Path
import json
import numpy as np
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form


def complex_box(d,L):
    cells=[]
    for k in range(d+1):
        cells.append([(p,S) for S in combinations(range(d),k) for p in product(*[range(L if i in S else L+1) for i in range(d)])])
    index=[{v:i for i,v in enumerate(ck)} for ck in cells];D=[];H=[None]
    for k in range(d):
        mat=np.zeros((len(cells[k+1]),len(cells[k])),dtype=np.int64)
        for row,(p,S) in enumerate(cells[k+1]):
            for j,axis in enumerate(S):
                R=tuple(a for a in S if a!=axis);up=list(p);up[axis]+=1
                mat[row,index[k][tuple(up),R]]+=(-1)**j
                mat[row,index[k][p,R]]-=(-1)**j
        D.append(mat)
    for k in range(1,d+1):
        mat=np.zeros((len(cells[k-1]),len(cells[k])),dtype=np.int64)
        for row,(y,R) in enumerate(cells[k-1]):
            for axis in range(min(R) if R else d):
                S=(axis,)+R
                for t in range(y[axis]):
                    p=tuple(0 if j<axis else t if j==axis else y[j] for j in range(d))
                    mat[row,index[k][p,S]]+=1
        H.append(mat)
    return cells,D,H


results=[]
for d,L in [(2,1),(2,2),(3,1),(3,2),(4,1)]:
    cells,D,H=complex_box(d,L)
    for k in range(d-1):assert not np.any(D[k+1]@D[k])
    ev=np.zeros((len(cells[0]),len(cells[0])),dtype=np.int64);ev[:,cells[0].index(((0,)*d,()))]=1
    assert np.array_equal(H[1]@D[0],np.eye(len(cells[0]),dtype=np.int64)-ev)
    for k in range(1,d+1):
        identity=D[k-1]@H[k]
        if k<d:identity+=H[k+1]@D[k]
        assert np.array_equal(identity,np.eye(len(cells[k]),dtype=np.int64))
    smith=[]
    if L==1:
        for k,mat in enumerate(D):
            S=smith_normal_form(Matrix(mat.tolist()),domain=ZZ)
            nonzero=[abs(int(S[i,i])) for i in range(min(S.shape)) if S[i,i]]
            assert all(x==1 for x in nonzero)
            smith.append({'degree':k,'rank':len(nonzero),'nonunit_invariant_factors':[]})
    row={'dimension':d,'intervals_per_axis':L,'cell_counts':[len(x) for x in cells],'integer_homotopy_identity':True,'smith_checks':smith}
    results.append(row);print(row,flush=True)
Path(__file__).with_name('BLOCK2_INTEGER_COCHAIN_CHECK.json').write_text(json.dumps(results,indent=2)+'\n')
