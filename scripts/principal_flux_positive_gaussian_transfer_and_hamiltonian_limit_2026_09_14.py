#!/usr/bin/env python3
"""Author checks of a separately derived periodized principal-flux transfer.

Finite calculations and certified elementary truncation tails; no phase proof.
"""
from itertools import product, combinations
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json
import math
import numpy as np
from scipy.linalg import expm, eigvalsh, eigh
from scipy.sparse import csr_matrix

AUDIT_TIMEOUT_SEC = 180

def principal(x, n=3):
    return (np.asarray(x) + n//2) % n - n//2

def theta(q):
    return 1 + 2*sum(q**(j*j) for j in range(1, 65))

def spectral_norm(x):
    return float(np.max(np.abs(eigvalsh((x+x.T.conj())/2))))

def single_square_checks():
    n, e, radius = 3, 4, 12
    f = np.array([1, 1, -1, -1], dtype=int)
    states = np.array(list(product(range(n), repeat=e)), dtype=int)
    flux = principal(states @ f)
    powers = n**np.arange(e)
    residue_delta = ((states[:, None, :]-states[None, :, :]) % n) @ powers
    flux_delta = flux[:, None]-flux[None, :]
    lifts = np.array(list(product(range(-radius, radius+1), repeat=e)), dtype=int)
    energy = np.sum(lifts*lifts, axis=1)
    curl = lifts @ f
    residue = (lifts % n) @ powers
    physical = np.array([-1,0,1])
    u = np.column_stack([(flux==b)/math.sqrt(27) for b in physical])
    assert np.max(np.abs(u.T @ u-np.eye(3))) < 1e-14
    rows=[]
    for q in [.02,.08,.25,.7]:
        one = np.array([q**(j*j) for j in range(-radius,radius+1)])
        conv=one
        for _ in range(e-1):
            conv=np.convolve(conv,one)
        total=np.arange(-radius*e,radius*e+1)
        # A product-tail union bound, divided by the full Theta^E.
        tail1=2*q**((radius+1)**2)/(1-q**(2*radius+3))
        norm_tail=e*tail1/theta(q)
        for mu in [0.,.4,1.2]:
            lookup=np.array([np.bincount(residue,weights=q**energy*np.exp(-mu*(db-curl)**2/n**2),minlength=n**e) for db in range(-2,3)]) / theta(q)**e
            full=lookup[flux_delta+2,residue_delta]
            effective=np.zeros((3,3))
            for i,bp in enumerate(physical):
                for j,b in enumerate(physical):
                    db=bp-b
                    mask=(total-db)%n==0
                    effective[i,j]=np.sum(conv[mask]*np.exp(-mu*((db-total[mask])/n)**2))/theta(q)**e
            symmetry=float(np.max(np.abs(full-full.T)))
            reduction=float(np.max(np.abs(u.T@full@u-effective)))
            invariant=float(np.max(np.abs(full@u-u@effective)))
            mineig=float(eigvalsh(full)[0])
            rowsum=float(np.max(full.sum(axis=0)))
            assert symmetry<2e-13 and reduction<2e-13 and invariant<2e-13
            assert mineig>-norm_tail-1e-13 and rowsum<1+2e-13
            if mu==0:
                assert abs(rowsum-1)<2e-13
            rows.append(dict(q=q,mu=mu,dimension=81,physical_dimension=3,minimum_eigenvalue=mineig,max_row_sum=rowsum,gauge_reduction_error=reduction,gauge_invariance_error=invariant,symmetry_error=symmetry,truncation_norm_tail=norm_tail))
    return rows

def cube_geometry():
    # Boundary maps are constructed cell-by-cell, not copied from a runner.
    vertices=list(product(range(2),repeat=3))
    edges=[(axis,x) for axis in range(3) for x in vertices if x[axis]==0]
    faces=[(axes,x) for axes in combinations(range(3),2) for x in vertices if all(x[a]==0 for a in axes)]
    f=np.zeros((len(faces),len(edges)),dtype=int)
    for p,(axes,x) in enumerate(faces):
        for r,axis in enumerate(axes):
            remaining=axes[1-r]
            high=list(x);high[axis]=1
            f[p,edges.index((remaining,tuple(high)))]+=(-1)**r
            f[p,edges.index((remaining,x))]-=(-1)**r
    d=np.zeros((1,len(faces)),dtype=int)
    for axis in range(3):
        axes=tuple(i for i in range(3) if i!=axis)
        high=[0]*3;high[axis]=1
        d[0,faces.index((axes,tuple(high)))]+=(-1)**axis
        d[0,faces.index((axes,(0,0,0)))]-=(-1)**axis
    incidence=np.zeros((len(edges),len(vertices)),dtype=int)
    for l,(axis,x) in enumerate(edges):
        y=list(x);y[axis]=1
        incidence[l,vertices.index(tuple(y))]=1
        incidence[l,vertices.index(x)]=-1
    assert np.array_equal(d@f,np.zeros((1,12),dtype=int))
    assert np.array_equal(f@incidence,np.zeros((6,8),dtype=int))
    assert np.linalg.matrix_rank(f)==5
    states=np.array([b for b in product([-1,0,1],repeat=6) if int((d@np.array(b)).item())%3==0])
    assert len(states)==243
    # Explicit clock surjectivity certificate: one five-column minor map.
    for cols in combinations(range(12),5):
        b=principal(np.array(list(product(range(3),repeat=5)))@f[:,cols].T)
        if len(set(map(tuple,b)))==243:
            break
    else:
        raise AssertionError('No full finite clock image')
    return f,d,states,cols

def cube_checks():
    f,d,states,basis=cube_geometry()
    e=f.shape[1]; size=len(states); index={tuple(b):i for i,b in enumerate(states)}
    t,mu,kappa,lam=.7,.8,.4,1.1
    charge=(states@d.T/3).ravel()
    assert np.array_equal(charge,np.rint(charge))
    v=1.5*kappa*np.sum(states*states,axis=1)+lam*charge**2
    direct_v=kappa*np.sum(1-np.cos(2*np.pi*states/3),axis=1)+lam*charge**2
    assert np.max(np.abs(v-direct_v))<1e-13 and min(v)>=0
    # Direct Hamiltonian uses all original links with their multiplicities.
    he=2*t*e*np.eye(size)
    a_links=[np.zeros((size,size)) for _ in range(e)]
    escape=np.zeros(size)
    max_dv=0.
    for j,b in enumerate(states):
        for link in range(e):
            for sign in [-1,1]:
                bp=principal(b+sign*f[:,link]); i=index[tuple(bp)]
                mismatch=(bp-b-sign*f[:,link])//3
                assert np.array_equal(bp-b-sign*f[:,link],3*mismatch)
                assert np.array_equal(d@mismatch,d@(bp-b)//3)
                rate=t*np.exp(-mu*(mismatch@mismatch))
                he[i,j]-=rate;escape[j]+=rate
                a_links[link][i,j]+=rate/t
                max_dv=max(max_dv,abs(v[i]-v[j]))
    assert np.max(np.abs(he-he.T))<1e-14
    h=he+np.diag(v)
    comm=he@np.diag(v)-np.diag(v)@he
    commnorm=float(np.linalg.norm(comm,2))
    assert max_dv<=6*kappa+16*lam
    assert commnorm<=2*t*e*max_dv+1e-13
    # Independent low-lift transfer sums vectors in the original 12-link space.
    lifts=[np.zeros(e,dtype=int)]
    for l in range(e):
        for s in [-1,1]:
            z=np.zeros(e,dtype=int);z[l]=s;lifts.append(z)
    for l,r in combinations(range(e),2):
        for sl,sr in product([-1,1],repeat=2):
            z=np.zeros(e,dtype=int);z[l]=sl;z[r]=sr;lifts.append(z)
    assert len(lifts)==289
    matrices=[np.zeros((size,size)) for _ in range(3)]
    for lift in lifts:
        curl=f@lift; degree=lift@lift
        for j,b in enumerate(states):
            bp=principal(b+curl);i=index[tuple(bp)]
            mismatch=(bp-b-curl)//3
            matrices[degree][i,j]+=np.exp(-mu*(mismatch@mismatch))
    assert np.max(np.abs(t*matrices[1]-(2*t*e*np.eye(size)-he)))<1e-14
    a=sum(a_links)
    ck=matrices[2]-a@a/2+2*e*np.eye(size)
    ck_local=sum(2*np.eye(size)-al@al/2 for al in a_links)
    interacting=0;disjoint_error=0.;poisson_pair_error=0.;poisson_pair_ratio=0.
    for l,r in combinations(range(e),2):
        blr=np.zeros((size,size))
        for sl,sr in product([-1,1],repeat=2):
            curl=sl*f[:,l]+sr*f[:,r]
            for j,b in enumerate(states):
                bp=principal(b+curl);i=index[tuple(bp)]
                mismatch=(bp-b-curl)//3
                blr[i,j]+=np.exp(-mu*(mismatch@mismatch))
        sym=(csr_matrix(a_links[l])@csr_matrix(a_links[r])+csr_matrix(a_links[r])@csr_matrix(a_links[l])).toarray()/2
        difference=blr-sym
        pair_norm=spectral_norm(difference)
        assert pair_norm<=4+1e-13
        test_q=.2
        conditional=(np.eye(size)+test_q*(a_links[l]+a_links[r])+test_q**2*sym)/(1+2*test_q)**2
        principal_pair=(np.eye(size)+test_q*(a_links[l]+a_links[r])+test_q**2*blr)/(1+2*test_q)**2
        pair_error=spectral_norm(principal_pair-conditional)
        assert pair_error<=4*test_q**2/(1+2*test_q)**2+1e-13
        poisson_pair_error=max(poisson_pair_error,pair_error)
        poisson_pair_ratio=max(poisson_pair_ratio,pair_error/(4*test_q**2/(1+2*test_q)**2))
        if np.any((f[:,l]!=0)&(f[:,r]!=0)):
            interacting+=1;ck_local+=difference
        else:
            disjoint_error=max(disjoint_error,float(np.max(np.abs(difference))))
    coefficient_error=float(np.max(np.abs(ck-ck_local)))
    assert coefficient_error<1e-13 and disjoint_error<1e-13
    assert spectral_norm(ck)<=4*e+8*interacting
    result=[]
    for eps in [.01,.005,.0025,.00125]:
        q=eps*t;p0=theta(q)**(-e)
        kernel=p0*(matrices[0]+q*matrices[1]+q*q*matrices[2])
        tail=max(0.,-math.expm1(-e*math.log(theta(q))+math.log1p(2*e*q+2*e*(e-1)*q*q)))
        s=np.exp(-eps*v/2)
        transfer=s[:,None]*kernel*s[None,:]
        generator_error=spectral_norm(kernel-np.eye(size)+eps*he)
        exact_step=expm(-eps*h)
        step_error=spectral_norm(transfer-exact_step)
        c=29*e*t*t+commnorm/2
        assert generator_error<=24*e*e*q*q+tail
        assert step_error<=c*eps*eps+tail
        # Fixed physical time, all semigroups contractions; include lift tail.
        steps=round(.1/eps)
        time=steps*eps
        product_error=spectral_norm(np.linalg.matrix_power(transfer,steps)-expm(-time*h))
        assert product_error<=time*eps*c+steps*tail
        eigs,eigvecs=eigh(transfer)
        effective=-(eigvecs*np.log(eigs)[None,:])@eigvecs.T/eps
        logarithm_second_order_residual=spectral_norm(effective-h+eps*t*t*ck)
        result.append(dict(epsilon=eps,logarithm_second_order_residual=logarithm_second_order_residual,logarithm_residual_div_epsilon2=logarithm_second_order_residual/eps**2,integer_lift_count=len(lifts),certified_lift_tail=tail,kernel_first_order_error=generator_error,one_step_error=step_error,one_step_error_div_epsilon2=step_error/eps**2,fixed_time=time,product_error=product_error,product_bound=time*eps*c+steps*tail,finite_volume_C=c,minimum_truncated_kernel_eigenvalue=float(eigvalsh(kernel)[0])))
    assert result[-1]['logarithm_second_order_residual'] < .018*result[0]['logarithm_second_order_residual']
    assert poisson_pair_ratio>.01
    faults=dict(row_normalization_changes_target_diagonal=float(np.max(2*t*e-escape)),wrong_mu_scale_generator_difference=None)
    hewrong=2*t*e*np.eye(size)
    for j,b in enumerate(states):
        for l in range(e):
            for sign in [-1,1]:
                bp=principal(b+sign*f[:,l]);i=index[tuple(bp)]
                delta=bp-b-sign*f[:,l]
                hewrong[i,j]-=t*np.exp(-mu*(delta@delta))
    faults['wrong_mu_scale_generator_difference']=spectral_norm(hewrong-he)
    assert faults['row_normalization_changes_target_diagonal']>.1
    assert faults['wrong_mu_scale_generator_difference']>.1
    return dict(geometry=dict(edges=e,faces=6,physical_flux_states=size,clock_surjectivity_columns=basis),parameters=dict(t=t,mu=mu,K=kappa,lambda_=lam),local_log_coefficient=dict(poisson_pair_max_error=poisson_pair_error,poisson_pair_max_ratio_to_bad_event_bound=poisson_pair_ratio,interacting_link_pairs=interacting,disjoint_pair_error=disjoint_error,local_decomposition_error=coefficient_error,norm=spectral_norm(ck),bound=4*e+8*interacting),commutator_norm=commnorm,commutator_row_bound=2*t*e*max_dv,max_actual_potential_jump=max_dv,universal_cubic_N3_potential_jump_bound=6*kappa+16*lam,checks=result,faults=faults)

def exact_strip_checks():
    n=3;e=10
    f=np.zeros((n,e),dtype=int)
    for j in range(n):
        f[j,j]=1;f[j,j+1]=-1;f[j,n+1+2*j]=1;f[j,n+2+2*j]=-1
    lifts=np.array(list(product([-1,0,1],repeat=e)),dtype=np.int8)
    curl=lifts@f.T;energy=np.sum(lifts*lifts,axis=1)
    states=np.array(list(product([-1,0,1],repeat=n)))
    powers=3**np.arange(n);lookup=np.zeros(27,dtype=int)
    lookup[((states+1)%3)@powers]=np.arange(27)
    counts=np.zeros((27,27,11,13),dtype=np.int64)
    for j,b in enumerate(states):
        bp=principal(b+curl);mismatch=(bp-b-curl)//3
        targets=lookup[((bp+1)%3)@powers]
        penalty=np.sum(mismatch*mismatch,axis=1)
        np.add.at(counts[:,j],(targets,energy,penalty),1)
    assert np.array_equal(counts,counts.transpose(1,0,2,3))
    # Full link multiplicities: each fixed starting flux receives 3^10 lifts.
    assert np.all(counts.sum(axis=(0,2,3))==3**10)
    anti=np.array([[0,1,-1],[-1,0,1],[1,-1,0]])
    w=np.array([[1,-2,1][b[1]+1]*anti[b[0]+1,b[2]+1] for b in states])
    assert int(w@w)==36
    histogram=np.einsum('i,j,ijab->ab',w,w,counts,dtype=np.int64)
    q=Fraction(9,10);r=Fraction(1,2)
    exact=sum((int(histogram[a,b])*q**a*r**b/(1+2*q)**e for a in range(11) for b in range(13)),Fraction(0))
    assert exact==Fraction(-901886967,55267035185152)
    # Compare every coefficient of the independently displayed degree-10
    # polynomial, not just its value at the negative point.
    p9=[-2304,12352,-24800,9504,54056,-124012,126672,-56738,-7097,13659]
    expected=[Fraction(0) for _ in range(11)]
    for degree,coefficient in enumerate(p9):
        expected[degree]-=Fraction(coefficient,64)
        expected[degree+1]+=Fraction(coefficient,64)
    actual=[sum((Fraction(int(histogram[a,b]),2**b) for b in range(13)),Fraction(0)) for a in range(11)]
    assert actual==expected
    unpenalized=[0]*11
    for j in range(10):
        coefficient=36*(-1)**j*math.comb(9,j)
        unpenalized[j]+=coefficient;unpenalized[j+1]+=2*coefficient
    assert histogram.sum(axis=1).tolist()==unpenalized
    # A separate factorized Laurent convolution at q=9/10 uses integer
    # coefficients 10,9,9, with the final normalization 28^10.
    columns=[(1,0,0)]*3+[(0,1,0)]*2+[(0,0,1)]*3+[(-1,1,0),(0,-1,1)]
    polynomial={(0,0,0):1}
    for column in columns:
        next_polynomial=defaultdict(int)
        for exponent,coefficient in polynomial.items():
            next_polynomial[exponent]+=10*coefficient
            for sign in [-1,1]:
                target=tuple(x+sign*y for x,y in zip(exponent,column))
                next_polynomial[target]+=9*coefficient
        polynomial=dict(next_polynomial)
    assert sum(polynomial.values())==28**10
    def witness(b):
        return [1,-2,1][b[1]+1]*int(anti[b[0]+1,b[2]+1])
    convolution=Fraction(0)
    for b in product([-1,0,1],repeat=3):
        for curl_value,coefficient in polynomial.items():
            bp=tuple((x+y+1)%3-1 for x,y in zip(b,curl_value))
            mismatch=tuple((y-x-s)//3 for x,y,s in zip(b,bp,curl_value))
            convolution+=Fraction(coefficient*witness(b)*witness(bp),28**10*2**sum(m*m for m in mismatch))
    assert convolution==exact
    # Congruence preserves the negative witness; squaring instead is PSD.
    weights=np.array([[float(q**a*r**b/(1+2*q)**e) for b in range(13)] for a in range(11)])
    kernel=np.einsum('ijab,ab->ij',counts,weights)
    v=.17*np.sum(states*states,axis=1)
    diagonal=np.exp(-v/2)
    sandwich=diagonal[:,None]*kernel*diagonal[None,:]
    transformed=w/diagonal
    assert abs(float(transformed@sandwich@transformed)-float(exact))<2e-14
    assert float(eigvalsh(kernel@kernel)[0])>-1e-14
    return dict(exact_form=str(exact),norm_squared=int(w@w),physical_dimension=27,link_lift_count=3**10,laurent_coefficient_count=len(polynomial),polynomial_coefficients_checked=11,minimum_numeric_eigenvalue=float(eigvalsh(kernel)[0]),two_step_minimum_numeric_eigenvalue=float(eigvalsh(kernel@kernel)[0]))

def elementary_scaling_checks():
    results=[]
    for q in [.0001,.001,.01,.08,.125]:
        tail=theta(q)-1-2*q
        assert tail<=3*q**4+1e-15
        poisson_repeated=-math.expm1(-2*q+math.log1p(2*q))
        assert poisson_repeated<=2*q*q+1e-15
        for e in [1,2,12,375]:
            alpha=((1+2*q)/theta(q))**e
            assert 2*(1-alpha)<=6*e*q**4+3e-13
            alpha_poisson=math.exp(e*(-2*q+math.log1p(2*q)))
            assert 2*(1-alpha_poisson)<=4*e*q*q+1e-14
        beta_w=2/3*math.log(1/q)
        beta_v=9/(2*math.pi**2)*math.log(1/q)
        assert abs(math.exp(-1.5*beta_w)-q)<1e-15
        assert abs(math.exp(-2*math.pi**2*beta_v/9)-q)<1e-15
        results.append(dict(q=q,Wilson_beta_t=beta_w,Villain_beta_t=beta_v,poisson_repeated_probability=poisson_repeated))
    return results

def square_generator_multiplicity_check():
    # Flux-only derivation: four original links have the same signed flux
    # actions. Each physical off-diagonal hop therefore has factor four.
    mu=.7;radius=12;physical=np.array([-1,0,1]);a=np.zeros((3,3))
    for j,b in enumerate(physical):
        for sign in [-1,1]:
            bp=int(principal(b+sign));i=int(np.where(physical==bp)[0][0])
            mismatch=(bp-b-sign)//3
            a[i,j]+=4*math.exp(-mu*mismatch*mismatch)
    target=8*np.eye(3)-a
    errors=[]
    for q in [.002,.001,.0005]:
        one=np.array([q**(j*j) for j in range(-radius,radius+1)])
        conv=one
        for _ in range(3):
            conv=np.convolve(conv,one)
        total=np.arange(-4*radius,4*radius+1);kernel=np.zeros((3,3))
        for i,bp in enumerate(physical):
            for j,b in enumerate(physical):
                db=bp-b;mask=(total-db)%3==0
                kernel[i,j]=np.sum(conv[mask]*np.exp(-mu*((db-total[mask])/3)**2))/theta(q)**4
        error=spectral_norm((np.eye(3)-kernel)/q-target)
        assert error<=29*4*q
        errors.append(error)
    assert errors[2]<.27*errors[0]
    return dict(errors=errors,fixed_diagonal=8,unwrapped_off_diagonal=4)

def main():
    passed=0
    def report(name,value):
        nonlocal passed
        passed+=1
        print('PASS '+name+': '+json.dumps(value,sort_keys=True),flush=True)
    try:
        square=single_square_checks()
        report('periodized Gaussian square, full and physical kernels',dict(cases=len(square),max_reduction_error=max(x['gauge_reduction_error'] for x in square),minimum_eigenvalue=min(x['minimum_eigenvalue'] for x in square),largest_lift_tail=max(x['truncation_norm_tail'] for x in square)))
        report('Theta tails, local Poisson probabilities and logarithmic time scaling',elementary_scaling_checks())
        report('original-link multiplicity in the reduced generator',square_generator_multiplicity_check())
        cube=cube_checks()
        report('cubical incidence, realizable physical states and current continuity',cube['geometry'])
        report('local Poisson pair coupling and logarithmic coefficient cancellation',cube['local_log_coefficient'])
        report('extensive finite-step, product and first logarithmic correction checks',cube['checks'])
        report('potential-jump and commutator bound',dict(actual_jump=cube['max_actual_potential_jump'],cubic_bound=cube['universal_cubic_N3_potential_jump_bound'],commutator_norm=cube['commutator_norm'],row_bound=cube['commutator_row_bound']))
        report('rejected row normalization and mismatch-scale controls',cube['faults'])
        report('exact physical strip counterexample and independent Laurent convolution',exact_strip_checks())
        print('per_element: checked individual integer lifts, reversal, mismatch scaling and the fixed electric diagonal; no physical phase was inferred.')
        print('per_site: checked all physical one-cube flux states and their exact current continuity; native site-law selection was not executed.')
        print('per_mode: checked finite transfer eigenvalues and a rational negative physical quadratic form; no infinite-volume excitation spectrum was computed.')
        print('per_block: checked full-to-physical square reduction, cubic time limits and the exact three-square certificate by two arithmetic routes.')
        print('lattice_wide: checked and not executed — infinite-volume phase and anisotropic state bounds require an additional proof beyond these finite tests.')
        print(f'TOTAL: PASS={passed} FAIL=0')
    except Exception:
        print(f'TOTAL: PASS={passed} FAIL=1',flush=True)
        raise

if __name__=='__main__':
    main()
