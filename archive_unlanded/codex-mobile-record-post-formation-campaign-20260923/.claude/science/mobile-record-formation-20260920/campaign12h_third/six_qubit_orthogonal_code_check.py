#!/usr/bin/env python3
"""Author exact check of a six-qubit proper-cubic orthogonal color code.

The orthonormal code is specified by the polar map F(F^T F)^(-1/2).
Exact rank, positive Gram spectrum, covariance, and a disjoint invariant
vacuum certify its definition; floating polar vectors are diagnostic only.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,itertools,json,math
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent


def main():
    labels=[s.eye(3)[:,i]*sign for i in range(3) for sign in (1,-1)]
    labels += [s.Matrix(z) for z in itertools.product((-1,1),repeat=3)]
    lookup={tuple(z):i for i,z in enumerate(labels)}
    def column(z):
        v=s.Matrix([1,*z])
        return s.kronecker_product(v,v,v)
    F=s.Matrix.hstack(*(column(z) for z in labels))
    gram=F.T*F
    assert gram == s.Matrix(14,14,lambda i,j:(1+labels[i].dot(labels[j]))**3)
    assert F.rank()==14
    eig=gram.eigenvals()
    assert sum(eig.values())==14 and all(e>0 for e in eig)
    vac=s.zeros(64,1)
    for i in range(1,4):
        vac[4*i+i]=1  # |0 i i>
        vac[16*i+i]=-1  # |i 0 i>
    assert (vac.T*vac)[0]==6 and F.T*vac==s.zeros(14,1)
    count=0
    char_records=[]
    for perm in itertools.permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in itertools.product((-1,1),repeat=3):
            if parity*math.prod(signs)!=1:
                continue
            R=s.zeros(3)
            for i in range(3): R[i,perm[i]]=signs[i]
            U=s.diag(1,R)
            V=s.kronecker_product(U,U,U)
            P=s.zeros(14)
            for j,z in enumerate(labels): P[lookup[tuple(R*z)],j]=1
            assert V*F==F*P
            assert P.T*gram*P==gram
            assert V*vac==vac
            count+=1
            char_records.append(dict(rotation=[list(R.row(i)) for i in range(3)],
                                     trace_H=int(s.trace(V)),trace_code=int(s.trace(P))))
    assert count==24
    # A rational polynomial certificate avoids optional huge radical projectors.
    t=s.Symbol('t')
    char=(t-6)**2*(t-48)**4*(t*t-92*t+192)*(t*t-88*t+384)**3
    assert gram.charpoly(t).as_expr()==s.expand(char)
    I=s.eye(14)
    annihilator=(gram-6*I)*(gram-48*I)*(gram**2-92*gram+192*I)*(gram**2-88*gram+384*I)
    assert annihilator==s.zeros(14)
    gn=np.array(gram).astype(float)
    values,vectors=np.linalg.eigh(gn)
    orth=np.array(F).astype(float)@((vectors*(values**-.5))@vectors.T)
    float_error=float(np.max(np.abs(orth.T@orth-np.eye(14))))
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                status='author_exact_construction_independent_check_pending',
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                physical_M2_factors=6,hilbert_dimension=64,color_dimension=14,
                F_rank=14,gram_determinant=str(gram.det()),
                gram_eigenvalues={str(e):int(m) for e,m in eig.items()},
                covariance_checks=count*14,invariant_vacuum_checks=count,
                vacuum_norm_squared=6,code_plus_vacuum_dimension=15,
                characteristic_polynomial=str(char),
                rational_annihilating_polynomial_exact=True,
                floating_orthogonality_residual_diagnostic=float_error,
                orthogonal_metric=dict(u='7',v='7/4',cross='0',u_minus_4v='0'),
                group_characters=char_records,
                scope='Covariant Hilbert-space code with orthogonal color states and an orthogonal invariant vacuum. Rates, Lindblad dynamics, site placement and physical interpretation are separate premises, not supplied by this rank certificate.')
    encoded=json.dumps(result,indent=2,default=lambda z:int(z))+'\n'
    (HERE/'SIX_QUBIT_ORTHOGONAL_CODE_RESULTS.json').write_text(encoded)
    print(encoded,end='')


if __name__=='__main__': main()
