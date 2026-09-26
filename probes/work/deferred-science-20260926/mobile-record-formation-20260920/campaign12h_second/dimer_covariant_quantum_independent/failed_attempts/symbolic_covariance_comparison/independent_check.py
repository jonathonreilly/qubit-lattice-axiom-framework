#!/usr/bin/env python3
"""Pre-author independent controls for the supplied mixed two-qubit encoding."""
from pathlib import Path
from itertools import product,permutations
import json,math
import numpy as np
from scipy.linalg import expm
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.I
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-I],[I,0]]),s.diag(1,-1)]
singlet=s.Matrix([0,1,-1,0])/s.sqrt(2)
magic=s.Matrix.hstack(singlet,*[s.kronecker_product(x,s.eye(2))*singlet for x in pauli])
A=[];B=[]
for i in range(3):
    X=s.zeros(4);Y=s.zeros(4);X[0,i+1]=X[i+1,0]=1;Y[0,i+1]=-I;Y[i+1,0]=I
    A.append(X);B.append(Y)
O=A+B;J=s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),s.eye(3)),s.Matrix.hstack(-s.eye(3),s.zeros(3)))
clean=lambda M:M.applyfunc(s.simplify)

def rotations():
    answer=[]
    for p in permutations(range(3)):
        for signs in product([-1,1],repeat=3):
            R=s.zeros(3)
            for i in range(3):R[i,p[i]]=signs[i]
            if R.det()==1:answer.append(R)
    assert len(answer)==24;return answer

def rho(q,r,la,lb,e,b):
    w=la*e+I*lb*b
    return s.Matrix.vstack(s.Matrix.hstack(s.Matrix([[q]]),w.H),s.Matrix.hstack(w,r*s.eye(3)))

def encoding():
    assert clean(magic.H*magic)==s.eye(4)
    for i in range(3):
        physicalA=(s.kronecker_product(pauli[i],s.eye(2))-s.kronecker_product(s.eye(2),pauli[i]))/2
        physicalB=-sum((s.LeviCivita(i,j,k)*s.kronecker_product(pauli[j],pauli[k]) for j in range(3) for k in range(3)),s.zeros(4))/2
        assert clean(magic*A[i]*magic.H)==physicalA
        assert clean(magic*B[i]*magic.H)==physicalB
    q=s.Rational(1,2);r=s.Rational(1,6);la=s.Rational(1,8);lb=s.Rational(1,16)
    labels=[]
    for i in range(3):
        for sign in [-1,1]:labels.append((sign*s.eye(3)[:,i],s.zeros(3,1)))
    for signs in product([-1,1],repeat=3):labels.append((s.zeros(3,1),s.Matrix(signs)))
    densities=[rho(q,r,la,lb,e,b) for e,b in labels]
    assert len({tuple(D) for D in densities})==14
    schur=[]
    SWAP=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
    Smagic=clean(magic.H*SWAP*magic);assert Smagic==s.diag(-1,1,1,1)
    for (e,b),D in zip(labels,densities):
        assert D==D.H and s.trace(D)==1
        w=la*e+I*lb*b;complement=s.simplify(q-(w.H*w)[0]/r);schur.append(str(complement));assert complement>0
        assert D.to_DM().rank()==4
        assert s.Matrix([s.trace(D*X) for X in O])==s.Matrix.vstack(2*la*e,2*lb*b)
        assert Smagic*D*Smagic==rho(q,r,la,lb,-e,-b)
        for R in rotations():
            T=s.diag(1,1,1,1);T[1:4,1:4]=R
            assert T*D*T.H==rho(q,r,la,lb,R*e,R*b)
    assert schur[:6]==['13/32']*6 and schur[6:]==['55/128']*8
    F=s.Matrix.hstack(*[s.Matrix.vstack(e,b) for e,b in labels]);tangent=s.Matrix.hstack(*[s.eye(14)[:,i]-s.eye(14)[:,13] for i in range(13)])
    assert (F*tangent).to_DM().rank()==6
    for masses in [(s.Rational(3,7),s.Rational(4,7)),(s.Rational(1,3),s.Rational(2,3))]:
        mixture=sum((mass*D for mass,D in zip([masses[0]/6]*6+[masses[1]/8]*8,densities)),s.zeros(4))
        assert mixture==s.diag(q,r,r,r)
    boundary=rho(s.Rational(1,4),s.Rational(1,4),s.Rational(1,4),0,s.Matrix([1,0,0]),s.zeros(3,1))
    assert boundary.to_DM().rank()==3 and min(boundary.eigenvals())==0
    invalid=rho(s.Rational(1,4),s.Rational(1,4),s.Rational(1,3),0,s.Matrix([1,0,0]),s.zeros(3,1))
    assert min(invalid.eigenvals())==-s.Rational(1,12)
    return {'labels':14,'proper_cubic_state_transformations':14*24,'Pauli_readout_identities':6,
        'Schur_complements':{'A':'13/32','B':'55/128'},'population_tangent_rank':6,
        'endpoint_swap_reverses_color':True,'strictness_countercontrols':{'boundary_rank':3,'outside_bound_negative_eigenvalue':'-1/12'}}

def covariance():
    q,r=s.symbols('q r',real=True,positive=True);R=s.diag(q,r,r,r)
    means=s.Matrix([s.trace(R*X) for X in O]);assert means==s.zeros(6,1)
    G=s.Matrix([[s.trace(R*X*Y) for Y in O] for X in O]);V=clean((G+G.T)/2);Sigma=clean(-I*(G-G.T))
    assert V==(q+r)*s.eye(6) and Sigma==2*(q-r)*J
    assert G==V+I*Sigma/2 and G.eigenvals()=={2*q:3,2*r:3}
    tracial=Sigma.subs({q:s.Rational(1,4),r:s.Rational(1,4)})
    assert tracial==s.zeros(6) and A[0]*B[0]-B[0]*A[0]!=s.zeros(4)
    Q=s.Rational(1,2);Rval=s.Rational(1,6);state=s.diag(Q,Rval,Rval,Rval)
    T=-I*(A[0]*B[0]-B[0]*A[0]);mean=s.trace(state*T);variance=s.trace(state*T*T)-mean**2
    assert mean==s.Rational(2,3) and variance==s.Rational(20,9)
    return {'symbolic_quantum_covariance_eigenvalues':{'2*q':3,'2*r':3},
        'tracial_state_limiting_CCR_zero_despite_nonzero_finite_commutator':True,
        'averaged_commutator_exact_L2_variance':'20/(9*K)'}

def weyl():
    q=s.Rational(1,2);r=s.Rational(1,6);state=s.diag(q,r,r,r);V=(q+r)*s.eye(6);Sigma=2*(q-r)*J
    zs=[s.Matrix([s.Rational(1,3),-s.Rational(1,5),0,s.Rational(1,7),0,s.Rational(1,11)]),
        s.Matrix([0,s.Rational(2,7),s.Rational(1,2),-s.Rational(1,3),s.Rational(1,4),0]),
        s.Matrix([-s.Rational(1,6),0,s.Rational(1,9),0,s.Rational(1,5),-s.Rational(2,7)])]
    h=s.symbols('h',real=True);P=s.eye(4);total=sum(zs,s.zeros(6,1));phase=sum(((zs[j].T*Sigma*zs[k])[0] for j in range(len(zs)) for k in range(j+1,len(zs))),s.Integer(0))
    for z in zs:
        Z=sum((z[i]*O[i] for i in range(6)),s.zeros(4));P=P*(s.eye(4)+I*h*Z-h*h*Z*Z/2)
    value=s.expand(s.trace(state*P));assert value.coeff(h,0)==1 and value.coeff(h,1)==0
    expected=-(total.T*V*total)[0]/2-I*phase/2
    assert s.simplify(value.coeff(h,2)-expected)==0 and phase!=0
    # Ordered commutator word has zero summed test but a nonzero phase.
    group=[s.eye(6)[:,0],s.eye(6)[:,3],-s.eye(6)[:,0],-s.eye(6)[:,3]]
    target=np.exp(-2j/3);state_np=np.array(state.tolist(),dtype=complex);rows=[]
    for K in [16,64,256,1024,4096]:
        product_matrix=np.eye(4,dtype=complex)
        for z in group:
            Z=np.array(sum((z[i]*O[i] for i in range(6)),s.zeros(4)).tolist(),dtype=complex)
            product_matrix=product_matrix@expm(1j*Z/math.sqrt(K))
        local=np.trace(state_np@product_matrix);actual=local**K
        reverse=np.conjugate(actual)
        assert abs(actual-target)<4/K
        rows.append({'blocks':K,'real':float(actual.real),'imag':float(actual.imag),'error_to_negative_phase':float(abs(actual-target)),
            'error_to_wrong_positive_phase':float(abs(actual-np.conjugate(target)))})
    assert rows[-1]['error_to_wrong_positive_phase']>1
    # Exact tensor factorization on two physical pair blocks.
    K=2;Z1=np.array(A[0].tolist(),dtype=complex);Z2=np.array(B[0].tolist(),dtype=complex);eye=np.eye(4)
    global_product=expm(1j*(np.kron(Z1,eye)+np.kron(eye,Z1))/math.sqrt(K))@expm(1j*(np.kron(Z2,eye)+np.kron(eye,Z2))/math.sqrt(K))
    direct=np.trace(np.kron(state_np,state_np)@global_product)
    factored=np.trace(state_np@expm(1j*Z1/math.sqrt(K))@expm(1j*Z2/math.sqrt(K)))**K
    assert abs(direct-factored)<1e-13
    return {'exact_general_three_test_second_coefficient':str(s.factor(expected)),'exact_general_ordering_bilinear':str(phase),
        'ordered_commutator_word_limit':'exp(-2*i/3)','finite_matrix_checks':rows,
        'two_block_tensor_factorization_numeric_error':float(abs(direct-factored)),
        'scope':'Numerical finite-K checks supplement the uniform bounded-matrix Taylor remainder proof, not an interacting quantum CLT.'}

def cross(q):
    x,y,z=q;return s.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])

def energy():
    Q=s.Matrix([1,2,2]);C=I*cross(Q);c=s.Rational(2,7);s0=s.Rational(2,3)
    assert C==C.H and C.eigenvals()=={-3:1,0:1,3:1}
    D=s.diag(C,C);Sigma=s0*J;L=c*J*D;H=Sigma.inv()*L
    assert H==c/s0*D and H==H.H
    assert H.eigenvals()=={-s.Rational(9,7):2,0:2,s.Rational(9,7):2}
    covariance=s.Rational(2,3)*s.eye(6)
    assert L*covariance+covariance*L.H==s.zeros(6) and L*Sigma+Sigma*L.H==s.zeros(6)
    assert Sigma!=L # Positive identity Hessian does not generate this drift.
    z=s.symbols('z',real=True);negative=s.Matrix([s.cos(z),s.sin(z),0]);positive=s.Matrix([s.cos(z),-s.sin(z),0])
    curl=lambda F:s.Matrix([-s.diff(F[1],z),s.diff(F[0],z),0])
    assert curl(negative)==-negative and curl(positive)==positive
    negative_energy=s.simplify(c/(2*s0)*(negative.T*curl(negative))[0]);assert negative_energy==-s.Rational(3,14)
    # Canonical potential/momentum -> E=-P, B=CQ transformation.
    T=s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),-s.eye(3)),s.Matrix.hstack(C,s.zeros(3)))
    derivative=T*J*T.H;expected=s.Matrix.vstack(s.Matrix.hstack(s.zeros(3),C),s.Matrix.hstack(-C,s.zeros(3)))
    assert derivative==expected and derivative.to_DM().rank()==4 and T.to_DM().rank()==5
    Hplus=s.diag(C*C,s.eye(3));assert all(v>=0 for v in Hplus.eigenvals())
    assert T*J*Hplus==derivative*T
    assert Q.T*C==s.zeros(1,3) and C*Q==s.zeros(3,1)
    assert cross(s.zeros(3,1))==s.zeros(3)
    return {'wavevector':list(Q),'curl_eigenvalues':{'-3':1,'0':1,'3':1},
        'onsite_Hessian_eigenvalues':{'-9/7':2,'0':2,'9/7':2},'real_negative_helicity_energy_density':'-3/14',
        'quantum_covariance_and_CCR_preserved_by_candidate_linear_flow':True,
        'derivative_bracket_rank_at_nonzero_mode':4,'canonical_to_EB_map_rank':5,
        'positive_canonical_energy_eigenvalues':{str(k):v for k,v in Hplus.eigenvals().items()},
        'zero_mode_scope':'B=curl Q has zero spatial mean on a periodic box; the construction does not include arbitrary harmonic B fields without an added sector.',
        'Gauss_scope':'Magnetic divergence vanishes identically; electric divergence requires its own initial constraint.'}

if __name__=='__main__':
    p=OUT/'INDEPENDENT_RESULTS.json';assert not p.exists();answer={}
    for name,fn in [('encoding',encoding),('covariance',covariance),('Weyl_limit',weyl),('energy_and_derivative_bracket',energy)]:
        answer[name]=fn();print(name+' '+json.dumps(answer[name],default=str),flush=True)
    p.write_text(json.dumps(answer,indent=2,default=str)+'\n')
