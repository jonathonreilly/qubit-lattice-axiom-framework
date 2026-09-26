#!/usr/bin/env python3
"""Primary two-history and encoded-memory checks; no independent inputs."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import time

import cvxpy as cp
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
V=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
S=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
rho=[(np.eye(2)+sum(v[i]*S[i] for i in range(3)))/2 for v in V]
OUTCOMES=list(product(range(6),repeat=2))


def exact_witnesses():
    cases=[]
    for j in [F(-1,2),F(0),F(1,10),F(1,2),F(4,5),F(1)]:
        P=[[F(1,6)*(1+j*int(V[a]@V[b])) for b in range(6)] for a in range(6)]
        target=[[P[a][b]*P[a][c] for b,c in OUTCOMES] for a in range(6)]
        x=[(a+b)/2 for a,b in zip(target[0],target[1])]
        y=[(a+b)/2 for a,b in zip(target[2],target[3])]
        tv=sum(abs(a-b) for a,b in zip(x,y))/2
        assert tv==j*j/9
        assert x[0]-y[0]==j*j/36
        marginal_error=F(0)
        if abs(j)<=F(1,2):
            approximate=[[F(1,36)*(1+j*int(V[a]@(V[b]+V[c]))) for b,c in OUTCOMES] for a in range(6)]
            for a in range(6):
                assert sum(abs(x-y) for x,y in zip(target[a],approximate[a]))/2==j*j/18
                for b in range(6):
                    assert sum(approximate[a][6*b+c] for c in range(6))==P[a][b]
                    assert sum(approximate[a][6*c+b] for c in range(6))==P[a][b]
        cases.append({'j':str(j),'mixture_total_variation':str(tv),'one_outcome_mixture_gap':str(x[0]-y[0]),
                      'worst_row_TV_lower_bound':str(j*j/18),'weak_explicit_POVM_checked':abs(j)<=F(1,2)})
    sx=sp.Matrix([[0,1],[1,0]]);sy=sp.Matrix([[0,-sp.I],[sp.I,0]])
    M=sp.kronecker_product(sx,sx)-sp.kronecker_product(sy,sy)
    assert M.eigenvals()=={0:2,-2:1,2:1}
    return {'classical_mixture_cases':cases,'quantum_product_mixture_difference_spectrum':[0,0,-2,2]}


def unrestricted_pair_fit(j):
    single=(1+j*V@V.T)/6
    target=np.array([[single[a,b]*single[a,c] for b,c in OUTCOMES] for a in range(6)])
    t=cp.Variable(36); u=cp.Variable((36,3));delta=cp.Variable(nonneg=True)
    constraints=[cp.norm(u,axis=1)<=t,cp.sum(t)==1,cp.sum(u,axis=0)==0]
    for a in range(6): constraints.append(cp.sum(cp.abs(t+u@V[a]-target[a]))/2<=delta)
    problem=cp.Problem(cp.Minimize(delta),constraints)
    optimum=problem.solve(solver='CLARABEL',tol_gap_abs=1e-10,tol_gap_rel=1e-10,tol_feas=1e-10,max_iter=300)
    assert problem.status=='optimal',problem.status
    bound=j*j/18
    assert optimum>=bound-1e-8
    if abs(j)<=.5: assert abs(optimum-bound)<1e-8
    min_eig=min(t.value-np.linalg.norm(u.value,axis=1))
    primal=max(np.sum(abs(t.value+u.value@V[a]-target[a]))/2 for a in range(6))
    assert min_eig>=-1e-8 and primal<=optimum+1e-8
    return {'j':j,'unrestricted_worst_row_TV':optimum,'analytic_lower_bound':bound,
            'analytic_sharp_for_this_j':abs(j)<=.5,'minimum_effect_eigenvalue':float(min_eig),
            'primal_row_TV':float(primal)}


def encoded_memory():
    vectors=[]
    for a in range(6):
        val,vec=np.linalg.eigh(rho[a]);psi=vec[:,-1]
        axis=np.eye(3)[:,a//2]
        vectors.append(np.kron(axis,psi))
    U=np.column_stack(vectors)
    gram_error=np.linalg.norm(U.conj().T@U-np.eye(6));assert gram_error<1e-12
    cases=[]
    for p,q,r in [(3,1,2),(12,1,2),(2,2,1),(1,3,2)]:
        D=p+q+4*r
        P=np.array([[(p if a==b else q if a^1==b else r)/D for b in range(6)] for a in range(6)])
        K=[U@np.diag(np.sqrt(P[:,b]))@U.conj().T for b in range(6)]
        completeness=np.linalg.norm(sum(k.conj().T@k for k in K)-np.eye(6));assert completeness<1e-11
        nondemolition=0.;history=0.
        for a,psi in enumerate(vectors):
            state=np.outer(psi,psi.conj())
            for b in range(6):
                actual=K[b]@state@K[b].conj().T
                nondemolition=max(nondemolition,np.linalg.norm(actual-P[a,b]*state))
                for c in range(6):
                    history=max(history,abs(np.trace(K[c]@actual@K[c].conj().T).real-P[a,b]*P[a,c]))
        assert nondemolition<1e-12 and history<1e-12
        cases.append({'raw_weights':[p,q,r],'completeness_error':float(completeness),
                      'unnormalized_nondemolition_error':float(nondemolition),'two_history_error':float(history)})
    # Three cross-axis pure parents overlap; their corresponding program
    # states must be orthogonal if the joint states are perfectly distinguishable.
    cross=[abs(np.vdot(np.linalg.eigh(rho[a])[1][:,-1],np.linalg.eigh(rho[b])[1][:,-1]))**2
           for a,b in [(0,2),(0,4),(2,4)]]
    assert np.allclose(cross,[.5,.5,.5])
    return {'axis_register_dimension':3,'record_Hilbert_dimension':6,'gram_error':float(gram_error),
            'cross_axis_parent_squared_overlaps':cross,'instrument_cases':cases,
            'record_plus_orthogonal_vacancy_dimension':7,'sufficient_qubits_for_encoded_cell':3}


def main():
    start=time.monotonic()
    result={'exact':exact_witnesses(),
            'unrestricted_pair_POVMs':[unrestricted_pair_fit(j) for j in [-1,-.8,-.5,-.25,0,.1,.25,.5,.6,.8,1]],
            'encoded_memory':encoded_memory(),'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies':{'cvxpy':cp.__version__,'numpy':np.__version__,'sympy':sp.__version__},
            'scope':'Supplied physical-qubit repeatable-history and explicit encoded-memory interfaces; no axiom inference.'}
    result['elapsed_seconds']=time.monotonic()-start
    result['status']='All primary exact, convex-program and constructive checks passed'
    text=json.dumps(result,indent=2)+'\n';(HERE/'REPEATED_FORMATION_QUANTUM_RESULTS.json').write_text(text);print(text,end='')


if __name__=='__main__': main()
