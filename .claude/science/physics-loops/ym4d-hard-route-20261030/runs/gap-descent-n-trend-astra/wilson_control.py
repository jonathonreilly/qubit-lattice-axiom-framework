#!/usr/bin/env python3
"""Compare n=3 frozen-top restriction with row 1089's trivalent cube.
Different valence construction, same shared Clebsch-Gordan convention.
"""
from wilson import *
from scipy.sparse import diags
import sys
if __name__=='__main__':
    scratch=Path(sys.argv[1]);dest=scratch/'control_cube_J1'
    cube.build(1,8,dest,E=24)
    cr=np.load(dest/'basis.npy');CX=sum(load_npz(dest/f'face{i}.npz') for i in range(6))
    wr=np.load(scratch/'wilson_J1E36/rows.npy');wd=scratch/'wilson_J1E36'
    if (wd/'X_data.npy').exists():
        WX=csr_matrix((np.load(wd/'X_data.npy'),np.load(wd/'X_indices.npy'),np.load(wd/'X_indptr.npy')),shape=(len(wr),len(wr)))
    else:WX=load_npz(wd/'X.npz')
    k=keys(wr);indices=[];phases=[]
    for row in cr:
        target=np.zeros(24,np.int8)
        for i in range(4):target[i*6:i*6+6]=[row[i],row[4+i],0,row[8+i],0,row[8+i]]
        loc=lookup(target,k);assert loc>=0;indices.append(loc)
        phase=1.
        for i in range(4):
            a,b,c=int(row[4+(i-1)%4]),int(row[4+i]),int(row[8+i])
            found=False
            for m0 in range(-a,a+1,2):
                for m1 in range(-b,b+1,2):
                    m2=-m0+m1
                    den=cube.inv((a,b,c),(m0,m1,m2),(-1,1,-1))
                    if abs(den)>1e-12:
                        num=inv4((a,b,c,0),c,(m0,m1,m2,0));ratio=num/den
                        assert abs(abs(ratio)-1)<1e-12
                        phase*=ratio;found=True;break
                if found:break
            assert found
        phases.append(phase)
    diff=WX[np.ix_(indices,indices)]-diags(phases)@CX@diags(phases)
    err=float(np.max(np.abs(diff.data))) if diff.nnz else 0.
    assert err<2e-12,err
    # Taylor action against the separate SciPy expm action on the full J=1 basis.
    from scipy.sparse.linalg import expm_multiply
    from scipy.sparse import eye
    vec=np.sin(np.arange(len(wr))+.2);vec/=np.linalg.norm(vec);b=2.6;shift=11*b
    term=np.exp(-shift)*vec;result=term.copy();weight=np.exp(-shift)
    for degree in range(1,401):
        term=(b/degree)*(WX@term);result+=term;weight*=shift/degree
        if degree>shift and weight<1e-22:break
    ref=expm_multiply(b*WX-shift*eye(len(wr)),vec,traceA=-shift*len(wr))
    exp_error=float(np.linalg.norm(result-ref)/np.linalg.norm(ref));assert exp_error<2e-12
    record={'grade':'GUIDE control','frozen_top_dimension':len(indices),'cube_matrix_error':err,'taylor_relative_error':exp_error,'peak_RSS_bytes':base.memory_check()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
