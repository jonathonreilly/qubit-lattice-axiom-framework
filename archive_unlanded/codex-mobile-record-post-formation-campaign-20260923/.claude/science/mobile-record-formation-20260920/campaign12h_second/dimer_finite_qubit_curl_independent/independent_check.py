#!/usr/bin/env python3
"""Independent finite-qubit occupation, actual curl, and quadratic-time controls."""
from pathlib import Path
from itertools import product
from math import factorial,comb,sqrt
import json,math
import numpy as np
import sympy as s
from scipy.sparse import diags
from scipy.sparse.linalg import expm_multiply

OUT=Path(__file__).resolve().parent

def occupations(K):
    return [(i,j,n-i-j) for n in range(K+1) for i in range(n+1) for j in range(n-i+1)]

def f(K,n):return s.sqrt(max(s.Rational(1)-s.Rational(n,K),s.Integer(0)))

def symmetric_blocks():
    rows=[]
    for K in [1,2,3]:
        words=list(product(range(4),repeat=K));wi={w:i for i,w in enumerate(words)};basis=occupations(K);bi={n:i for i,n in enumerate(basis)}
        U=s.zeros(4**K,len(basis))
        for row,w in enumerate(words):
            n=tuple(w.count(i) for i in [1,2,3]);vac=K-sum(n);multiplicity=factorial(K)//(factorial(vac)*math.prod(factorial(a) for a in n))
            U[row,bi[n]]=1/s.sqrt(multiplicity)
        assert U.T*U==s.eye(len(basis)) and len(basis)==comb(K+3,3)
        lowered=[]
        for i in range(3):
            physical=s.zeros(4**K)
            for col,w in enumerate(words):
                for slot,label in enumerate(w):
                    if label==i+1:
                        target=list(w);target[slot]=0;physical[wi[tuple(target)],col]+=1/s.sqrt(K)
            F=s.zeros(len(basis))
            for col,n in enumerate(basis):
                if n[i]:
                    target=list(n);target[i]-=1;F[bi[tuple(target)],col]=s.sqrt(n[i])*f(K,sum(n)-1)
            assert (physical*U-U*F).applyfunc(s.simplify)==s.zeros(*U.shape)
            assert (physical.T*U-U*F.T).applyfunc(s.simplify)==s.zeros(*U.shape)
            lowered.append(F)
        for i in range(3):
            for j in range(3):
                expected=s.zeros(len(basis))
                for col,n in enumerate(basis):
                    if i==j:expected[col,col]=1-s.Rational(sum(n)+n[i],K)
                    elif n[i]:
                        target=list(n);target[i]-=1;target[j]+=1
                        expected[bi[tuple(target)],col]=-s.sqrt(n[i]*(n[j]+1))/K
                assert (lowered[i]*lowered[j].T-lowered[j].T*lowered[i]-expected).applyfunc(s.simplify)==s.zeros(len(basis))
        rows.append({'pairs':K,'actual_qubits':2*K,'full_pair_Hilbert_dimension':4**K,'symmetric_dimension':len(basis),
            'exact_lowering_and_raising_intertwiners':6,'exact_deformed_commutator_controls':9})
    # Orthogonal quartet is the actual singlet/Cartesian-triplet pair basis.
    pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
    singlet=s.Matrix([0,1,-1,0])/s.sqrt(2);M=s.Matrix.hstack(singlet,*[s.kronecker_product(a,s.eye(2))*singlet for a in pauli])
    assert (M.H*M).applyfunc(s.simplify)==s.eye(4)
    return {'blocks':rows,'physical_two_qubit_basis_unitary':True,
        'finite_CCR_boundary':'[a_iK,a_iK^dagger]=1-(N_x+n_i)/K; canonical CCR are not asserted at finite K.'}

def tail_and_weight_controls():
    rows=[]
    for K in [1,2,5,11]:
        states=[(0,0,0),(1,0,0),(K,0,0),(K-1,1,0),(K+1,0,0),(K,1,1),(2*K+3,2,1)]
        for n in states:
            total=sum(n)
            for i in range(3):
                low=s.sqrt(n[i])*f(K,total-1) if n[i] else s.Integer(0)
                up=s.sqrt(n[i]+1)*f(K,total)
                if total>K:assert low==up==0
                lowerr=s.simplify((low-s.sqrt(n[i]))**2*K*K)
                uperr=s.simplify((up-s.sqrt(n[i]+1))**2*K*K)
                assert s.simplify((total+1)**3-lowerr)>=0 and s.simplify((total+1)**3-uperr)>=0
            rows.append({'K':K,'occupation':n,'outside_physical_sector':total>K,'coefficient_error_bounds_exact':True})
    return {'exact_cases':rows,'individual_coefficient_bound':'||(a_K-a)psi|| and ||(a_K^dagger-a^dagger)psi|| <= K^-1||(N+1)^(3/2)psi||',
        'quadratic_product_constant':'2+3*sqrt(2), multiplied by the two linear coefficient l1 norms',
        'outside_sector_tested':True}

def discrete_curl():
    rows=[]
    for L in [3,4]:
        coords=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(coords)};V=len(coords);D=[]
        for j in range(3):
            M=s.zeros(V)
            for x in coords:
                a=list(x);a[j]=(a[j]+1)%L;b=list(x);b[j]=(b[j]-1)%L
                M[index[x],index[tuple(a)]]+=s.Rational(1,2);M[index[x],index[tuple(b)]]-=s.Rational(1,2)
            assert M.T==-M;D.append(M)
        for a in D:
            for b in D:assert a*b==b*a
        C=sum((s.kronecker_product(D[j],s.Matrix(3,3,lambda i,k:s.LeviCivita(i,j,k))) for j in range(3)),s.zeros(3*V))
        div=sum((s.kronecker_product(D[j],s.eye(3)[j,:]) for j in range(3)),s.zeros(V,3*V))
        assert C.T==C and div*C==s.zeros(V,3*V)
        assert all(sum(abs(C[i,j]) for j in range(C.cols))==2 for i in range(C.rows))
        zeros=[];spectrum={}
        for m in product(range(L),repeat=3):
            wave=[s.sin(2*s.pi*k/L) for k in m];squared=s.simplify(sum(t*t for t in wave))
            spectrum[str(squared)]=spectrum.get(str(squared),0)+1
            if squared==0:zeros.append(m)
        expected_zero=1 if L%2 else 8;assert len(zeros)==expected_zero
        rank=C.to_DM().rank();assert rank==2*(V-len(zeros))
        assert div.to_DM().rank()==V-len(zeros)
        rows.append({'side':L,'cells':V,'curl_dimension':3*V,'exact_curl_rank':rank,
            'exact_divergence_rank':V-len(zeros),'zero_momenta':zeros,'squared_frequency_inventory':spectrum,
            'derivative_bracket_rank':2*rank,'row_l1_norm':'2',
            'one_sufficient_Hamiltonian_error_constant':str(s.Rational(5*3*V,2)*(2+3*s.sqrt(2)))})
    return rows

def reduced_hamiltonian(R,constant_occupations,K=None):
    """Exact Galerkin entries for one cell C=diag(1,0,1).

    Other two occupations are conserved. Only the free middle mode changes.
    For R>=K this contains the full finite-K physical sector exactly.
    """
    nleft,nright=constant_occupations;diagonal=np.zeros(R+1);upper=np.zeros(R-1)
    def ff(n):return 1. if K is None else sqrt(max(1.-n/K,0.))
    for middle in range(R+1):
        ns=(nleft,middle,nright);total=sum(ns)
        for n,w2 in zip(ns,[1.,0.,1.]):
            diagonal[middle]+=(w2+1)/4*((n+1)*ff(total)**2+(n*ff(total-1)**2 if n else 0.))
        if middle+2<=R:upper[middle]=-.25*sqrt((middle+1)*(middle+2))*ff(total)*ff(total+1)
    return diags([upper,diagonal,upper],offsets=[-2,0,2],format='csr')

def time_control():
    rows=[];cutoff_rows=[];max_cutoff=0.
    for fixed in [(0,0),(1,1)]:
        for time in [.3,.7,1.]:
            references={}
            for R in [80,100]:
                initial=np.zeros(R+1,dtype=complex);initial[0]=1
                H=reduced_hamiltonian(R,fixed,None)
                references[R]=expm_multiply(-1j*time*H,initial)
            error=np.linalg.norm(np.pad(references[80],(0,20))-references[100]);max_cutoff=max(max_cutoff,float(error))
            assert error<3e-12
            cutoff_rows.append({'fixed_other_occupations':fixed,'time':time,'reference_cutoffs':[80,100],'reference_vector_difference':float(error)})
            for K in [2,4,8,16,32,64]:
                R=100;initial=np.zeros(R+1,dtype=complex);initial[0]=1
                H=reduced_hamiltonian(R,fixed,K)
                # The entire physical sector, including its actual boundary,
                # is present in this invariant occupation sector.
                physical_max=K-sum(fixed);assert physical_max>=0
                active=H[:physical_max+1,:physical_max+1].toarray()
                assert np.linalg.eigvalsh(active).min()>-1e-12
                evolved=expm_multiply(-1j*time*H,initial)
                tail=np.linalg.norm(evolved[physical_max+1:]);assert tail<2e-13
                difference=np.linalg.norm(evolved-references[100])
                rows.append({'K':K,'fixed_other_occupations':fixed,'time':time,'norm_error':float(difference),
                    'K_times_norm_error':float(K*difference),'outside_physical_norm':float(tail)})
    # An empirical bounded-K corroboration, not the analytic Duhamel proof.
    assert max(r['K_times_norm_error'] for r in rows)<30
    return {'scope':'One-cell diagonal positive quadratic test C=diag(1,0,1), not a simulation of the spatial cubic curl. It tests the same exact shared-total-occupation cutoff and a zero-frequency coordinate.',
        'finite_K_physical_sector_included_without_truncation':True,'canonical_reference_cutoff_checks':cutoff_rows,
        'maximum_reference_cutoff_discrepancy':max_cutoff,'evolution_rows':rows,
        'no_uniform_time_or_volume_rate_inferred_from_rows':True}

if __name__=='__main__':
    p=OUT/'INDEPENDENT_RESULTS.json';assert not p.exists();answer={}
    for name,fn in [('symmetric_qubit_representation',symmetric_blocks),('extension_and_weight',tail_and_weight_controls),('actual_periodic_curl',discrete_curl),('finite_time_control',time_control)]:
        answer[name]=fn();print(name+' '+json.dumps(answer[name],default=str),flush=True)
    p.write_text(json.dumps(answer,indent=2,default=str)+'\n')
