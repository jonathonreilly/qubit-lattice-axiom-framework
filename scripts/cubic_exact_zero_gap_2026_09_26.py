"""Exact integer Schur/inertia certificate; floating eigenvectors only propose Z."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import sqlite3
import numpy as np
from scipy import sparse,linalg

LIMIT=(1<<63)-1
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def row_abs(a):
    assert int(np.max(np.abs(a)))*a.shape[1]<LIMIT
    return np.abs(a).sum(axis=1,dtype=np.int64)

def product(a,b):
    # This bound controls every absolute partial dot sum, not just its result.
    bound=int(row_abs(a).max())*int(np.max(np.abs(b)))
    assert bound<LIMIT,('product overflow guard',bound)
    return a@b,bound

def gersh(a):
    sums=row_abs(a);diag=np.diag(a)
    assert int(np.max(np.abs(diag)))*2+int(sums.max())<LIMIT
    radii=sums-np.abs(diag)
    return diag-radii,diag+radii

def calculate(HERE):
    dbpath=HERE/'quotient-closed.sqlite3'
    assert sha(dbpath)==json.loads((HERE/'QUOTIENT_CLOSURE_FREEZE.json').read_text())['sha256']
    con=sqlite3.connect(f'file:{dbpath}?mode=ro&immutable=1',uri=True)
    rows=con.execute('SELECT id,word,diagonal FROM states ORDER BY id').fetchall()
    edge=np.array(con.execute('SELECT src,dst,coefficient FROM edges').fetchall(),dtype=np.int64)
    con.close();n=len(rows)
    mask=np.array([len(json.loads(word)[1])<=4 for i,word,d in rows])
    # Aggregation cannot overflow: total absolute input sum is an exact bound.
    assert sum(abs(int(v)) for v in edge[:,2])+sum(abs(int(d)) for i,w,d in rows)<LIMIT
    A=sparse.coo_matrix((edge[:,2],(edge[:,1],edge[:,0])),shape=(n,n)).tocsr()+sparse.diags([d for i,w,d in rows],format='csr',dtype=np.int64)
    assert (A-A.T).nnz==0
    P=A[mask][:,mask];B=A[mask][:,~mask];Q=A[~mask][:,~mask]
    qbound=int((2*Q.diagonal()-np.asarray(abs(Q).sum(axis=1)).ravel()).min())
    threshold=-550;g=qbound-threshold;assert g>0
    maxb=int(abs(B).max());brows=np.asarray(abs(B).sum(axis=1)).ravel()
    sparse_product_guard=int(brows.max())*maxb
    assert sparse_product_guard<LIMIT
    BBT=(B@B.T).toarray()
    pmat=(P-threshold*sparse.eye(P.shape[0],format='csr',dtype=np.int64)).toarray()
    assert g*int(np.max(np.abs(pmat)))+int(np.max(np.abs(BBT)))<LIMIT
    F=g*pmat-BBT
    assert np.array_equal(F,F.T)
    vals,Y=linalg.eigh(F.astype(float))
    attempts=[]
    for scale in (4096,16384,65536):
        Z=np.rint(scale*Y).astype(np.int64)
        gram,guard_g=product(Z.T,Z)
        FZ,guard_fz=product(F,Z)
        T,guard_t=product(Z.T,FZ)
        assert np.array_equal(T,T.T)
        gl,gu=gersh(gram);tl,tu=gersh(T)
        neg=np.where(tu<0)[0];pos=np.where(tl>0)[0]
        ok=bool(gl.min()>0 and len(neg)==1 and len(pos)==len(Z)-1)
        attempt={'scale':scale,'gram_min_lower':int(gl.min()),'negative_rows':neg.tolist(),
                 'positive_rows':len(pos),'congruence_negative_upper':int(tu[neg[0]]) if len(neg)==1 else None,
                 'congruence_min_positive_lower':int(tl[pos].min()) if len(pos) else None,
                 'int64_partial_sum_guards':{'BBT':sparse_product_guard,'gram':guard_g,'FZ':guard_fz,'ZTFZ':guard_t},
                 'certificate_passed':ok}
        attempts.append(attempt);print(json.dumps(attempt),flush=True)
        if ok:break
    assert ok, 'No integer congruence certificate found; preserve failed attempts.'
    certfile=HERE/'ZERO_GAP_INTEGER_BASIS.json'
    certfile.write_text(json.dumps(Z.tolist(),separators=(',',':'))+'\n')
    energy=json.loads((HERE/'ZERO_ENERGY_CERTIFICATE.json').read_text())
    U=Fraction(energy['upper']);assert U<threshold
    out={'status':'exact Schur/inertia certificate conditional on frozen integer operator',
         'core_dimension':int(mask.sum()),'remainder_dimension':int((~mask).sum()),
         'core_rule':'at most four nonzero electric edges','Q_exact_Gershgorin_lower':qbound,
         'threshold':threshold,'g':g,'lambda2_strictly_above_threshold':True,
         'zero_isolation_gap_lower_exact':str(Fraction(threshold)-U),
         'zero_isolation_gap_lower_float':float(Fraction(threshold)-U),
         'attempts':attempts,'basis_sha256':sha(certfile),'database_sha256':sha(dbpath),
         'energy_certificate_sha256':sha(HERE/'ZERO_ENERGY_CERTIFICATE.json'),
         'source_sha256':sha(Path(__file__)),
         'scope':'zero fiber only; not a global band gap, full formation gap, or physical mass'}
    (HERE/'ZERO_GAP_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
