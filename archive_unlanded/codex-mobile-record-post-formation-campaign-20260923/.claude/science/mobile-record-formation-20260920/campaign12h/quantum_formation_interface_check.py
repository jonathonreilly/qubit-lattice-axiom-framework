#!/usr/bin/env python3
"""Primary interface check with unrestricted POVM and instrument optimizations.

The exact proof is in the working note. These convex numerical comparisons do
not impose the covariance ansatz or the square-root instrument on the solver.
"""
from itertools import product
from pathlib import Path
import hashlib,json,time
import cvxpy as cp
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
AXES=np.array(((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)),float)
PAULI=np.array(([[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]),complex)
I=np.eye(2,dtype=complex)
RHO=np.array([(I+sum(v[i]*PAULI[i] for i in range(3)))/2 for v in AXES])


def kernel(p,q,r):
    return np.array([[p if a==b else q if (a^1)==b else r for b in range(6)]
                     for a in range(6)],float)/(p+q+4*r)


def symbolic_checks():
    sx=sp.Matrix([[0,1],[1,0]]);sy=sp.Matrix([[0,-sp.I],[sp.I,0]]);sz=sp.diag(1,-1)
    identity=sp.eye(2);pauli=(sx,sy,sz)
    states=[(identity+sign*sigma)/2 for sigma in pauli for sign in (1,-1)]
    swap=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    assert sum((sp.kronecker_product(r,r) for r in states),sp.zeros(4))==sp.eye(4)+swap
    j=sp.symbols('j',real=True)
    effects=[(identity+sign*j*sigma)/6 for sigma in pauli for sign in (1,-1)]
    assert sum(effects,sp.zeros(2))==identity
    for a,b in product(range(6),repeat=2):
        target=(1+j if a==b else 1-j if (a^1)==b else 1)/6
        assert sp.simplify(sp.trace(states[a]*effects[b])-target)==0
    a,b=sp.symbols('a b',real=True)
    kraus=[a*identity+sign*b*sigma for sigma in pauli for sign in (1,-1)]
    for sigma in pauli:
        transformed=sum((K*sigma*K.H for K in kraus),sp.zeros(2))
        assert sp.simplify(transformed-(6*a*a-2*b*b)*sigma)==sp.zeros(2)
    return {'two_design_identity':True,'exact_povm_probabilities':36,'pauli_channel_identities':3}


def povm_minimax(raw):
    target=kernel(*raw)
    alpha=cp.Variable(6)
    beta=cp.Variable((6,3))
    loss=cp.Variable(nonneg=True)
    probs=np.ones((6,1))@cp.reshape(alpha,(1,6),order='C')+AXES@beta.T
    constraints=[cp.sum(alpha)==1,cp.sum(beta,axis=0)==0]
    constraints.extend(cp.norm(beta[b,:],2)<=alpha[b] for b in range(6))
    constraints.extend(cp.norm(probs[a,:]-target[a,:],1)<=2*loss for a in range(6))
    program=cp.Problem(cp.Minimize(loss),constraints)
    program.solve(solver='CLARABEL',tol_gap_abs=1e-10,tol_gap_rel=1e-10,tol_feas=1e-10,max_iter=250)
    assert program.status==cp.OPTIMAL,(raw,program.status)
    p,q,r=raw;D=p+q+4*r;difference=p+q-2*r
    expected=2*abs(difference)/(3*D)
    actual=program.value
    error=abs(actual-expected)
    assert error<2e-7,(raw,actual,expected)
    effects=[alpha.value[b]*I+sum(beta.value[b,i]*PAULI[i] for i in range(3)) for b in range(6)]
    actual_rows=np.array([[np.trace(rho@E).real for E in effects] for rho in RHO])
    residual=max(abs(np.sum(effects,axis=0)-I).flat)
    min_eigenvalue=min(np.linalg.eigvalsh(E).min() for E in effects)
    row_loss=max(np.sum(abs(actual_rows-target),axis=1)/2)
    assert residual<2e-8 and min_eigenvalue>-2e-8
    assert abs(row_loss-expected)<2e-7
    # A direct constructive candidate using the independently derived interval.
    lower=(3*(p-q)-2*abs(difference))/D
    upper=(3*(p-q)+2*abs(difference))/D
    lo=max(-1.,lower);hi=min(1.,upper)
    assert lo<=hi+1e-14
    s=(lo+hi)/2
    candidate=(np.ones((6,6))+s*AXES@AXES.T)/6
    assert abs(max(np.sum(abs(candidate-target),axis=1)/2)-expected)<1e-14
    return {'raw_weights':raw,'convex_optimum':actual,'closed_minimax':expected,
            'absolute_error':error,'primal_row_loss':row_loss,'minimum_effect_eigenvalue':min_eigenvalue,
            'completeness_residual':float(residual),'attaining_covariant_s_interval':[lo,hi]}


def instrument_optimum(j):
    effects=[(I+j*sum(v[i]*PAULI[i] for i in range(3)))/6 for v in AXES]
    constraints=[]
    if abs(j)==1:
        # Exact facial reduction: a positive Choi matrix with rank-one input
        # marginal E.T must be E.T tensor tau for some output density tau.
        # tau is unrestricted. This removes the empty-interior PSD constraints
        # that made both full-Choi endpoint solver attempts inaccurate.
        output=[cp.Variable((2,2),hermitian=True) for _ in range(6)]
        choi=[cp.kron(E.T,tau) for E,tau in zip(effects,output)]
        for tau in output:
            constraints.extend([tau>>0,cp.trace(tau)==1])
    else:
        choi=[cp.Variable((4,4),hermitian=True) for _ in range(6)]
        for C,E in zip(choi,effects):
            constraints.append(C>>0)
            trace_out=cp.bmat([[sum(C[2*i+o,2*k+o] for o in range(2)) for k in range(2)] for i in range(2)])
            constraints.append(trace_out==E.T)
    # Input-major Choi convention. No square-root or covariance ansatz enters.
    score=sum(np.kron(rho.T,rho) for rho in RHO)/6
    objective=sum(cp.real(cp.trace(score@C)) for C in choi)
    program=cp.Problem(cp.Maximize(objective),constraints)
    program.solve(solver='CLARABEL',tol_gap_abs=1e-9,tol_gap_rel=1e-9,tol_feas=1e-9,max_iter=250)
    assert program.status==cp.OPTIMAL,(j,program.status)
    expected=(2+np.sqrt(1-j*j))/3
    assert abs(program.value-expected)<4e-7,(j,program.value,expected)
    min_eigenvalue=min(np.linalg.eigvalsh(C.value).min() for C in choi)
    residual=0.
    for C,E in zip(choi,effects):
        partial=np.array([[sum(C.value[2*i+o,2*k+o] for o in range(2)) for k in range(2)] for i in range(2)])
        residual=max(residual,np.max(abs(partial-E.T)))
    assert min_eigenvalue>-2e-8 and residual<2e-8
    # Explicit channel, calculated directly from positive square roots of E.
    kraus=[]
    for E in effects:
        values,vectors=np.linalg.eigh(E)
        K=(vectors*np.sqrt(np.maximum(0,values)))@vectors.conj().T
        assert np.max(abs(K.conj().T@K-E))<1e-14
        kraus.append(K)
    eta=(1+2*np.sqrt(1-j*j))/3
    fidelities=[]
    for a,rho in enumerate(RHO):
        actual=sum(K@rho@K.conj().T for K in kraus)
        target=(1-eta)*I/2+eta*rho
        assert np.max(abs(actual-target))<1e-14
        fidelities.append(float(np.trace(rho@actual).real))
        probs=np.array([np.trace(K@rho@K.conj().T).real for K in kraus])
        assert np.max(abs(probs-(1+j*AXES@AXES[a])/6))<1e-14
    assert max(abs(f-expected) for f in fidelities)<1e-14
    return {'j':j,'solver':program.solver_stats.solver_name,'exact_rank_one_facial_reduction':abs(j)==1,
            'unrestricted_instrument_optimum':program.value,'sharp_fidelity':expected,
            'absolute_error':abs(program.value-expected),'minimum_choi_eigenvalue':min_eigenvalue,
            'effect_constraint_residual':float(residual),'lueders_eta':eta,'lueders_fidelities':fidelities}


def main():
    started=time.monotonic()
    exact=symbolic_checks()
    raw_cases=list(product((1,2,3,6),repeat=3))+[(12,1,2)]
    povms=[]
    for raw in raw_cases:
        result=povm_minimax(raw);povms.append(result)
        print(json.dumps({'povm':result}),flush=True)
    instruments=[]
    for j in (-1.,-.8,-.5,0.,.05,.2,.5,.8,1.):
        result=instrument_optimum(j);instruments.append(result)
        print(json.dumps({'instrument':result}),flush=True)
    record={'status':'primary exact and convex numerical checks passed','symbolic':exact,
            'povm_cases':povms,'instrument_cases':instruments,
            'dependencies':{'cvxpy':cp.__version__,'numpy':np.__version__,'sympy':sp.__version__},
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'A specified single-unknown-qubit/classical-six-outcome interface; no physical axiom inference.',
            'elapsed_seconds':time.monotonic()-started}
    (HERE/'QUANTUM_FORMATION_INTERFACE_RESULTS.json').write_text(json.dumps(record,indent=2)+'\n')
    print('POVM_CASES',len(povms),'MAX_ERROR',max(r['absolute_error'] for r in povms),flush=True)
    print('INSTRUMENT_CASES',len(instruments),'MAX_ERROR',max(r['absolute_error'] for r in instruments),flush=True)


if __name__=='__main__':
    main()
