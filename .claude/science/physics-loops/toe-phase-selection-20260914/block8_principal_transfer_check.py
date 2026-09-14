#!/usr/bin/env python3
"""Author checks of a separately derived periodized principal-flux transfer.

Finite calculations and certified elementary truncation tails; no phase proof.
"""
from itertools import product, combinations
from pathlib import Path
import json
import math
import numpy as np
from scipy.linalg import expm, eigvalsh, eigh
from scipy.sparse import csr_matrix

BASE = Path(__file__).resolve().parent

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
                rate=t*np.exp(-mu*(mismatch@mismatch))
                he[i,j]-=rate;escape[j]+=rate
                a_links[link][i,j]+=rate/t
                max_dv=max(max_dv,abs(v[i]-v[j]))
    assert np.max(np.abs(he-he.T))<1e-14
    h=he+np.diag(v)
    comm=he@np.diag(v)-np.diag(v)@he
    commnorm=float(np.linalg.norm(comm,2))
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
    interacting=0;disjoint_error=0.
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
    return dict(geometry=dict(edges=e,faces=6,physical_flux_states=size,clock_surjectivity_columns=basis),parameters=dict(t=t,mu=mu,K=kappa,lambda_=lam),local_log_coefficient=dict(interacting_link_pairs=interacting,disjoint_pair_error=disjoint_error,local_decomposition_error=coefficient_error,norm=spectral_norm(ck),bound=4*e+8*interacting),commutator_norm=commnorm,commutator_row_bound=2*t*e*max_dv,max_actual_potential_jump=max_dv,universal_cubic_N3_potential_jump_bound=6*kappa+16*lam,checks=result,faults=faults)

def main():
    result=dict(status='author_finite_checks_only',single_square=single_square_checks(),cube=cube_checks())
    path=BASE/'BLOCK8_PRINCIPAL_TRANSFER_CHECKS.json'
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
