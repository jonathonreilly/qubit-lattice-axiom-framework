#!/usr/bin/env python3
"""Primary operational-rate checks; no independent report is imported."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import time

import cvxpy as cp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
V = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
PAULI = [np.array([[0,1],[1,0]],complex),
         np.array([[0,-1j],[1j,0]],complex), np.diag([1,-1]).astype(complex)]
I2 = np.eye(2,dtype=complex)
RHO = [(I2+sum(v[i]*PAULI[i] for i in range(3)))/2 for v in V]


def menu(p,q,r):
    D=p+q+4*r
    return [[6*F(p if a==b else q if a^1==b else r,D)
             for b in range(6)] for a in range(6)]


def sparse_rank(rows):
    """Exact sparse elimination; pivots scaled to one."""
    pivots={}
    for row in rows:
        row={i:F(v) for i,v in row.items() if v}
        while row:
            i=min(row)
            if i not in pivots:
                scale=row[i]
                pivots[i]={j:x/scale for j,x in row.items()}
                break
            scale=row[i]
            for j,x in pivots[i].items():
                value=row.get(j,F(0))-scale*x
                if value: row[j]=value
                elif j in row: del row[j]
    return len(pivots)


def rate_constraints(k,W):
    states=list(product(range(6),repeat=k)); index={s:i for i,s in enumerate(states)}
    rows=[]
    for site in range(k):
        for others in product(range(6),repeat=k-1):
            for b in range(6):
                for axis in [1,2]:
                    row={}
                    for a,sign in [(0,1),(1,1),(2*axis,-1),(2*axis+1,-1)]:
                        s=list(others); s.insert(site,a)
                        row[index[tuple(s)]]=sign*W[b][a]
                    rows.append(row)
    rank=sparse_rank(rows)
    return {'parents':k,'variables':len(states),'constraints':len(rows),
            'rank':rank,'nullity':len(states)-rank}


def exact_checks():
    j=sp.symbols('j', real=True)
    I=sp.eye(2)
    sigmas=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
    axis=[sum((int(v[i])*sigmas[i] for i in range(3)),sp.zeros(2)) for v in V]
    actual=sum((sp.kronecker_product(I+j*A,I+j*A) for A in axis),sp.zeros(4))
    expected=6*sp.eye(4)+2*j*j*sum((sp.kronecker_product(A,A) for A in sigmas),sp.zeros(4))
    assert sp.simplify(actual-expected)==sp.zeros(4)
    eigens={}
    for eigenvalue,multiplicity in actual.eigenvals().items():
        expanded=sp.expand(eigenvalue)
        eigens[expanded]=eigens.get(expanded,0)+multiplicity
    assert eigens=={6-6*j*j:1,6+2*j*j:3}
    p,q,r=sp.symbols('p q r',positive=True)
    diff=(p+q)**2/2+4*r*r-(2*r*(p+q)+2*r*r)
    assert sp.factor(diff)==(p+q-2*r)**2/2
    ranks=[]
    for raw,expected_nullities in [((3,1,2),[1,1,1]),((1,1,1),[4,16,64])]:
        for k,target in enumerate(expected_nullities,start=1):
            row=rate_constraints(k,menu(*raw)); assert row['nullity']==target
            row['raw_weights']=raw;ranks.append(row)
    for raw,target in [((6,1,2),0),((12,1,2),0),((2,2,1),3)]:
        row=rate_constraints(1,menu(*raw)); assert row['nullity']==target
        row['raw_weights']=raw;ranks.append(row)
    # Positive total effects rule out the odd three-dimensional residual
    # for p=q!=r: their antipodal averages (the identity coefficient) vanish.
    W=menu(3,1,2); c=b=0
    Z=lambda a:sum(W[h][a]*W[h][c] for h in range(6))
    probability=lambda a:W[b][a]*W[b][c]/Z(a)
    x=(probability(0)+probability(1))/2
    y=(probability(2)+probability(3))/2
    assert x==F(69,286) and y==F(1,4) and x-y==F(-5,572)
    # The unique nonconstant hazard restores the affine marked rates.
    unnormalized=lambda a:W[b][a]*W[b][c]
    assert (unnormalized(0)+unnormalized(1))/2==(unnormalized(2)+unnormalized(3))/2
    return {'two_parent_operator_identity':True,'operator_spectrum':{str(k):v for k,v in eigens.items()},
            'clock_constraint_ranks':ranks,
            'constant_clock_j_half_counterexample':{'x_mixture':str(x),'y_mixture':str(y),'difference':str(x-y)}}


def kron_many(items):
    answer=np.ones((1,1),complex)
    for item in items: answer=np.kron(answer,item)
    return answer


def constructive_checks():
    result=[]
    for j in [-.8,-.5,0,.5,.8]:
        A=[I2+j*sum(v[i]*PAULI[i] for i in range(3)) for v in V]
        for k in [1,2,3]:
            effects=[kron_many([a]*k) for a in A]
            R=sum(effects);dt=.25/np.linalg.norm(R,2)
            kraus=[]
            for E in [dt*F for F in effects]+[np.eye(2**k)-dt*R]:
                lam,vec=np.linalg.eigh(E); assert min(lam)>-1e-12
                kraus.append((vec*np.sqrt(np.maximum(lam,0)))@vec.conj().T)
            completeness=np.linalg.norm(sum(K.conj().T@K for K in kraus)-np.eye(2**k))
            assert completeness<1e-11
            error=0.
            for labels in product(range(6),repeat=k):
                rho=kron_many([RHO[a] for a in labels])
                for b,E in enumerate(effects):
                    target=np.prod([1+j*V[b]@V[a] for a in labels])
                    error=max(error,abs(np.trace(E@rho).real-target))
            assert error<1e-11
            result.append({'j':j,'parents':k,'all_marked_rate_max_error':error,
                           'instrument_completeness_error':completeness,'dt':dt})
    return result


def rate_fit(raw):
    W=np.array(menu(*raw),float);target=W@W
    inputs=[np.kron(a,b) for a in RHO for b in RHO]
    R=cp.Variable((4,4),hermitian=True); delta=cp.Variable(nonneg=True)
    constraints=[R>>0]
    for rho,t in zip(inputs,target.ravel()):
        constraints.append(cp.abs(cp.real(cp.trace(R@rho))-t)<=delta)
    problem=cp.Problem(cp.Minimize(delta),constraints)
    value=problem.solve(solver='CLARABEL',tol_gap_abs=1e-10,tol_feas=1e-10,tol_gap_rel=1e-10,max_iter=300)
    assert problem.status=='optimal',problem.status
    p,q,r=map(F,raw);D=p+q+4*r
    tv=6*(p-q)/D;ta=6*(p+q-2*r)/D
    lower=ta*ta/4
    same=6+ta*ta/3;orth=6-ta*ta/6;orient=tv*tv/2;gap=same-orth
    # Exact minimization within the twirled positive-rate family a I+b sigma.sigma.
    # This is a primary candidate optimal formula, checked against an unrestricted SDP.
    middle=(3*same+3*orient-4*orth)/7
    closed=max(gap/2,middle) if middle<=gap else orient-same/3
    assert value+1e-7>=float(lower)
    assert abs(value-float(closed))<2e-7,(raw,value,closed)
    actual=max(abs(np.trace(R.value@rho).real-t) for rho,t in zip(inputs,target.ravel()))
    assert actual<=value+2e-7 and np.min(np.linalg.eigvalsh(R.value))>=-2e-7
    return {'raw_weights':raw,'equal_density_preparation_gap':str(ta*ta/2),
            'necessary_rate_error_lower_bound':str(lower),'unrestricted_optimum':value,
            'candidate_sharp_formula':str(closed),'formula_error':abs(value-float(closed)),
            'primal_max_error':actual,'minimum_rate_eigenvalue':float(np.min(np.linalg.eigvalsh(R.value)))}


def main():
    started=time.monotonic()
    result={'scope':'Supplied physical-qubit/event-instrument interface; not an axiom derivation.',
            'exact':exact_checks(),'positive_instruments':constructive_checks(),
            'unrestricted_two_parent_rate_fits':[rate_fit(raw) for raw in
                [(1,1,1),(3,1,2),(1,3,2),(6,1,2),(12,1,2),(2,2,1),(1,1,2),(20,1,1),(1,20,1),(1,1,20)]],
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependencies':{'cvxpy':cp.__version__,'numpy':np.__version__,'sympy':sp.__version__}}
    result['elapsed_seconds']=time.monotonic()-started
    result['status']='All primary exact, constructive and numerical checks passed'
    text=json.dumps(result,indent=2)+'\n';(HERE/'QUANTUM_RATE_SELECTION_RESULTS.json').write_text(text);print(text,end='')


if __name__=='__main__':
    main()
