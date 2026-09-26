"""Primary full-quotient spectral calculation, gated on frozen exact closure.

Only the k=0 Collatz--Wielandt interval uses exact rational arithmetic.
Other spectral numbers are numerical, with residual and consistency checks.
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib
import json
import sqlite3
import sys
import time
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh, cg, LinearOperator
from scipy.sparse.csgraph import connected_components

import cubic_one_pair_primitives_2026_09_26 as m
from cubic_closed_quotient_2026_09_26 import canonical

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def decode(raw):return m.pack({tuple(v):q for v,q in raw[0]},
                             {(tuple(a),tuple(b)):e for (a,b),e in raw[1]})
def rational_bound(A,v):
    assert np.all(v>0)
    ratios=[float(x).as_integer_ratio() for x in v]
    den=max(b for a,b in ratios)
    assert all(den%b==0 for a,b in ratios)
    w=[a*(den//b) for a,b in ratios]
    low=high=None
    for i in range(len(w)):
        val=sum(int(A.data[p])*w[int(A.indices[p])] for p in range(A.indptr[i],A.indptr[i+1]))
        rat=Fraction(val,w[i])
        low=rat if low is None or rat<low else low
        high=rat if high is None or rat>high else high
    return {'lower_exact':str(low),'upper_exact':str(high),
            'lower_float':float(low),'upper_float':float(high),'width_float':float(high-low),
            'scope':'exact integer H and positive rational trial vector; only k=0 ground energy'}

def calculate(HERE):
    t0=time.monotonic()
    path=HERE/'quotient-closed.sqlite3'
    freeze=json.loads((HERE/'QUOTIENT_CLOSURE_FREEZE.json').read_text())
    assert sha(path)==freeze['sha256']
    db=sqlite3.connect(f'file:{path}?mode=ro',uri=True)
    meta={k:json.loads(v) for k,v in db.execute('SELECT key,value FROM metadata')}
    assert meta['status']=='exact_coordinate_quotient_closed'
    rows=db.execute('SELECT id,word,processed,diagonal FROM states ORDER BY id').fetchall()
    edges=db.execute('SELECT src,dst,tx,ty,tz,coefficient FROM edges').fetchall()
    db.close()
    assert all(i==j and done==1 and d is not None for j,(i,s,done,d) in enumerate(rows))
    states=[decode(json.loads(s)) for i,s,done,d in rows]
    index={s:i for i,s in enumerate(states)}
    assert len(index)==len(states)
    for s in states:
        assert m.gauss(s) and m.cost(s)==0 and canonical(s)[1]==(0,0,0)
        assert all(abs(e)<=1 for ab,e in s[1])
        assert sum(q==-1 for v,q in s[0])==1
        assert sum(not m.even(v) for v,q in s[0])==2
    ed=Counter((a,b,x,y,z,c) for a,b,x,y,z,c in edges)
    assert max(ed.values())==1
    for a,b,x,y,z,c in edges:
        assert c<0 and ed[(b,a,-x,-y,-z,c)]==1
    n=len(states)
    ar=np.asarray(edges,dtype=np.int64)
    src,dst=ar[:,0],ar[:,1];tau=ar[:,2:5];coeff=ar[:,5]
    diag=np.array([r[3] for r in rows],dtype=np.int64)
    # Integer aggregation and all weighted binary64 sums remain exact.
    assert sum(abs(int(c)) for c in coeff)*max(1,int(abs(tau).max())**2)+sum(abs(int(d)) for d in diag)<2**53
    A=sparse.coo_matrix((coeff,(dst,src)),shape=(n,n)).tocsr()+sparse.diags(diag,format='csr',dtype=np.int64)
    A.sum_duplicates();A.eliminate_zeros()
    assert (A-A.T).nnz==0
    assert connected_components(A,directed=False,return_labels=False)==1
    first={}
    for sign in (-1,1):
        vec=np.zeros(n)
        for s,c in m.jump(m.OMEGA,(0,0,0),(1,0,0),sign).items():
            can,shift=canonical(s);assert shift==(0,0,0)
            vec[index[can]]+=c
        assert np.dot(vec,vec)==5
        first[str(sign)]=vec
    first['coherent']=first['-1']+first['1']
    assert np.dot(first['coherent'],first['coherent'])==10
    first={key:vec/np.linalg.norm(vec) for key,vec in first.items()}
    rowbound=float((np.abs(diag)+np.bincount(dst,weights=np.abs(coeff),minlength=n)).max())
    structure={'internal_states':n,'directed_displacement_edges':len(edges),
       'zero_fiber_nonzeros':A.nnz,'full_reversed_displacement_Hermiticity':True,
       'connected_quotient':True,'complete_first_vectors_present':True,
       'absolute_row_bound':rowbound,'diagonal_range':[int(diag.min()),int(diag.max())],
       'negative_on_A':sum(m.even(next(v for v,q in s[0] if q==-1)) for s in states),
       'negative_on_B':sum(not m.even(next(v for v,q in s[0] if q==-1)) for s in states)}
    print(json.dumps(structure),flush=True)
    vals,vecs=eigsh(A.astype(float),k=4,which='SA',tol=1e-12,maxiter=10000,v0=np.ones(n))
    order=np.argsort(vals);vals=vals[order];vecs=vecs[:,order]
    v=vecs[:,0];v*=np.sign(v.sum())
    assert np.all(v>0),float(v.min())
    zero_res=[float(np.linalg.norm(A@vecs[:,i]-vals[i]*vecs[:,i])) for i in range(4)]
    certified=rational_bound(A,v)
    assert certified['lower_float']-1e-10<=vals[0]<=certified['upper_float']+1e-10
    zero={'eigenvalues':vals.tolist(),'residual_norms':zero_res,
          'numerical_gap':float(vals[1]-vals[0]),'gap_certification':'not certified',
          'ground_Collatz_Wielandt':certified,
          'first_fiber_weights':{key:float(abs(v@phi)**2) for key,phi in first.items()},
          'positive_vector_range':[float(v.min()),float(v.max())]}
    print(json.dumps({'zero':zero}),flush=True)
    # Derivatives H_j=i*Aj, where Aj is real antisymmetric in this convention.
    deriv=[sparse.coo_matrix((-tau[:,j]*coeff,(dst,src)),shape=(n,n)).tocsr() for j in range(3)]
    for mat in deriv: assert (mat+mat.T).nnz==0
    lam=float(vals[0]);B=LinearOperator((n,n),matvec=lambda x:A@x-lam*x+v*(v@x),dtype=float)
    M=LinearOperator((n,n),matvec=lambda x:x/(A.diagonal()-lam+v*v),dtype=float)
    f=[mat@v for mat in deriv];y=[];solve=[]
    for j in range(3):
        sol,info=cg(B,-f[j],rtol=1e-12,atol=0,maxiter=20000,M=M)
        y.append(sol)
        solve.append({'axis':j,'info':int(info),'residual':float(np.linalg.norm(B@sol+f[j])),
                      'rhs_norm':float(np.linalg.norm(f[j])),'ground_overlap':float(v@sol)})
        assert info==0
    hessian=np.empty((3,3));second_bounds=np.empty((3,3))
    for i in range(3):
        for j in range(3):
            pp=sparse.coo_matrix((-tau[:,i]*tau[:,j]*coeff,(dst,src)),shape=(n,n)).tocsr()
            hessian[i,j]=v@(pp@v)+f[i]@y[j]+f[j]@y[i]
            second_bounds[i,j]=float(np.bincount(dst,weights=np.abs(tau[:,i]*tau[:,j]*coeff),minlength=n).max())
    print(json.dumps({'hessian':hessian.tolist(),'reduced_solve':solve}),flush=True)
    finite=[]
    for kv in [(h,0.,0.) for h in (.04,.02,.01,.005)]+[(.01,.01,0.),(.01,-.01,0.),(0.,0.,.01)]:
        kvec=np.array(kv)
        H=sparse.coo_matrix((coeff*np.exp(-1j*(tau@kvec)),(dst,src)),shape=(n,n)).tocsr()+sparse.diags(diag)
        delta=H-H.getH();herm=0. if not delta.nnz else float(abs(delta.data).max())
        assert herm<1e-12
        w,z=eigsh(H,k=1,which='SA',tol=1e-12,maxiter=10000,v0=v.astype(complex))
        residual=float(np.linalg.norm(H@z[:,0]-w[0]*z[:,0]))
        row={'k':list(kv),'energy':float(w[0]),'residual':residual,
             'delta_energy':float(w[0]-lam),'delta_over_k_squared':float((w[0]-lam)/(kvec@kvec)),
             'first_fiber_weights':{key:float(abs(np.vdot(z[:,0],phi))**2) for key,phi in first.items()}}
        finite.append(row);print(json.dumps(row),flush=True)
    np.savez_compressed(HERE/'closed_quotient_operator.npz',src=src,dst=dst,tau=tau,coefficient=coeff,diagonal=diag,
                        first_minus=first['-1'],first_plus=first['1'],first_coherent=first['coherent'],
                        zero_ground=v,zero_eigenvalues=vals)
    result={'structure':structure,'zero':zero,'numerical_hessian':hessian.tolist(),'reduced_solve':solve,
            'finite_momentum':finite,'derivative_operator_row_bounds':[float(np.bincount(dst,weights=np.abs(tau[:,j]*coeff),minlength=n).max()) for j in range(3)],
            'second_derivative_row_bounds':second_bounds.tolist(),'elapsed_seconds':time.monotonic()-t0,
            'status':'numerical full-quotient probe; curvature and weights are floating estimates',
            'sources':{str(p):sha(p) for p in (path,Path(__file__),Path(m.__file__),Path(__file__).with_name('cubic_closed_quotient_2026_09_26.py'))},
            'numerical_data_sha256':sha(HERE/'closed_quotient_operator.npz')}
    (HERE/'PRIMARY_CLOSED_BAND.json').write_text(json.dumps(result,indent=2)+'\n')
