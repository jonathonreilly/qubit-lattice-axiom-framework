"""Exact rational PF energy enclosure using positive integer power iteration.

The closed numerical operator is an input subject to independent reconstruction.
Given that integer matrix, the interval is exact; no floating rounding enters
the interval endpoints or width comparison.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import time
import numpy as np
from scipy import sparse


def calculate(HERE):
    start=time.monotonic()
    result=json.loads((HERE/'PRIMARY_CLOSED_BAND.json').read_text())
    path=HERE/'closed_quotient_operator.npz'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==result['numerical_data_sha256']
    d=np.load(path);n=len(d['diagonal'])
    A=sparse.coo_matrix((d['coefficient'],(d['dst'],d['src'])),shape=(n,n)).tocsr()+sparse.diags(d['diagonal'],format='csr',dtype=np.int64)
    A.sum_duplicates();A.eliminate_zeros()
    assert (A-A.T).nnz==0
    mu=int(A.diagonal().max())+1
    B=mu*sparse.eye(n,format='csr',dtype=np.int64)-A
    B.eliminate_zeros();assert np.all(B.data>=0)
    br=[[(int(B.indices[p]),int(B.data[p])) for p in range(B.indptr[i],B.indptr[i+1])] for i in range(n)]
    ar=[[(int(A.indices[p]),int(A.data[p])) for p in range(A.indptr[i],A.indptr[i+1])] for i in range(n)]
    initial=d['zero_ground'];initial=initial/initial.max()
    w=[int(float(x)*(1<<160))+1 for x in initial]
    assert all(x>0 for x in w)
    target=Fraction(1,10**18)
    checkpoints=[]
    for it in range(401):
        if it%20==0:
            lo=hi=None
            for i,row in enumerate(ar):
                v=sum(c*w[j] for j,c in row)
                r=Fraction(v,w[i]);lo=r if lo is None or r<lo else lo;hi=r if hi is None or r>hi else hi
            record={'iteration':it,'lower':str(lo),'upper':str(hi),'width':str(hi-lo),
                    'width_float':float(hi-lo),'elapsed':time.monotonic()-start}
            checkpoints.append(record);print(json.dumps(record),flush=True)
            if hi-lo<target:break
        if it==400:break
        nxt=[sum(c*w[j] for j,c in row) for row in br]
        shift=max(nxt).bit_length()-160
        assert shift>=0
        w=[x>>shift for x in nxt]
        assert all(x>0 for x in w)
    assert hi-lo<target, 'Exact energy enclosure did not reach the declared width'
    vector=HERE/'ZERO_ENERGY_POSITIVE_INTEGER_VECTOR.json'
    vector.write_text(json.dumps([str(x) for x in w],separators=(',',':'))+'\n')
    receipt={'status':'exact energy interval conditional on supplied integer matrix',
             'target_width_reached':hi-lo<target,'dimension':n,'mu':mu,
             'lower':str(lo),'upper':str(hi),'width':str(hi-lo),'checkpoints':checkpoints,
             'vector_sha256':hashlib.sha256(vector.read_bytes()).hexdigest(),
             'operator_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'scope':'zero-momentum ground energy only; no exact curvature, gap or eigenvector certificate'}
    (HERE/'ZERO_ENERGY_CERTIFICATE.json').write_text(json.dumps(receipt,indent=2)+'\n')
