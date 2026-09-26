#!/usr/bin/env python3
"""Exact leakage certificates via small Gram matrices; integer site actions."""
from pathlib import Path
import datetime, hashlib, itertools, json
import numpy as np
import sympy as s
import geometric_local_quantum_combination_check as old

HERE=Path(__file__).resolve().parent

def main():
    out=HERE/'geometric_local_quantum_gram_checks';out.mkdir(exist_ok=False)
    rows=[]
    for shape in [(2,2),(2,3),(2,4),(2,2,2),(2,2,3)]:
        xyz,edges,loops,black=old.patch(shape);n=len(xyz);K=n//2
        states=[z for z in itertools.product((0,1),repeat=n) if sum(z)==K]
        index={z:i for i,z in enumerate(states)};covers=old.matchings(n,edges)
        D=np.zeros((len(states),len(covers)),dtype=np.int64)
        for j,cover in enumerate(covers):
            for i,z in enumerate(states):
                value=1
                for x,y in cover:
                    if x not in black:x,y=y,x
                    if z[x]==z[y]:value=0;break
                    value*=1 if z[x]==0 else -1
                D[i,j]=value
        def action(permutation):
            inverse=np.argsort(permutation)
            targets=[index[tuple(z[j] for j in inverse)] for z in states]
            assert sorted(targets)==list(range(len(states)))
            A=np.empty_like(D);A[targets]=D
            return A
        NN=np.zeros_like(D);RR=np.zeros_like(D)
        for x,y in edges:
            p=list(range(n));p[x],p[y]=p[y],p[x];NN+=action(p)
        for square in loops:
            for sense in (-1,1):
                p=list(range(n))
                for i,x in enumerate(square):p[x]=square[(i+sense)%4]
                RR+=action(p)
        # All input entries are exact integers. The displayed conservative
        # bound excludes overflow in every dot product used below.
        max_value=max(int(abs(A).max()) for A in (D,NN,RR))
        max_dot_bound=len(states)*max_value**2
        assert max_dot_bound<2**63
        G=s.Matrix((D.T@D).tolist());Gi=G.inv(method='DM')
        assert G*Gi==s.eye(len(covers))
        CN=s.Matrix((D.T@NN).tolist());CR=s.Matrix((D.T@RR).tolist())
        LN=s.Matrix((NN.T@NN).tolist())-CN.T*Gi*CN
        LR=s.Matrix((RR.T@RR).tolist())-CR.T*Gi*CR
        CROSS=s.Matrix((NN.T@RR).tolist())-CN.T*Gi*CR
        # These are Gram matrices of physical leakage vectors, so their
        # kernels equal the corresponding rectangular leakage kernels.
        normN=s.trace(LN);normR=s.trace(LR);cross=s.trace(CROSS)
        if normN:
            alpha=-cross/normN
            residual=LR+alpha*(CROSS+CROSS.T)+alpha**2*LN
            minimum=s.trace(residual)
            assert minimum>=0
            closes=minimum==0
            if closes:assert residual==s.zeros(*residual.shape)
        else:
            alpha=None;minimum=normR;closes=normR==0
        row=dict(shape=shape,sites=n,singlet_covers=len(covers),magnetization_zero_dimension=len(states),
                 integer_dot_product_bound=max_dot_bound,NN_leakage_rank=LN.rank(),ring_leakage_rank=LR.rank(),
                 NN_squared_Frobenius_leakage=str(normN/2**K),ring_squared_Frobenius_leakage=str(normR/2**K),
                 exact_least_squares_alpha=str(alpha) if alpha is not None else 'unrestricted',
                 minimum_squared_Frobenius_leakage=str(minimum/2**K),
                 exact_cover_subspace_closure=closes)
        rows.append(row);print(json.dumps(row),flush=True)
    previous=HERE/'dimer_routed_development/local_quantum_combination_dense_attempt/GEOMETRIC_LOCAL_QUANTUM_COMBINATION_RUN.log'
    first=[json.loads(line) for line in previous.read_text().splitlines() if line.startswith('{')]
    assert len(first)==4
    for a,b in zip(first,rows):
        assert a['shape']==b['shape']
        for key in ['NN_leakage_rank','ring_leakage_rank','NN_squared_Frobenius_leakage','ring_squared_Frobenius_leakage']:
            assert a[key]==b[key]
        assert a['exact_subspace_closure']==b['exact_cover_subspace_closure']
    answer=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in (
                    Path(__file__).name,'geometric_local_quantum_combination_check.py')},
                rows=rows,earlier_completed_patch_rows_reproduced=4,
                scope='Exact finite-patch rational Gram certificates. Positive residual is a boundary of this two-operator family only. No infinite-volume or other-Hamiltonian conclusion.')
    (out/'RESULTS.json').write_text(json.dumps(answer,indent=2)+'\n')

if __name__=='__main__':main()
