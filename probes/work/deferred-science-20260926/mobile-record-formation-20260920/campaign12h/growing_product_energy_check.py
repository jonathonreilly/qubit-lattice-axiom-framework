#!/usr/bin/env python3
"""Exact finite-generator controls for the nonstationary energy argument.

Uses a three-label four-site model and augmented moment ODEs, not a sampler.
It does not certify the general proof or its large-volume limits.
"""
from pathlib import Path
from itertools import product
import hashlib,json
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import solve
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent


def main():
    states=np.array(list(product(range(3),repeat=4)))
    index={tuple(s):i for i,s in enumerate(states)};size=len(states)
    f=np.array([0.,1.,-1.]);n=np.array([0.,1.,1.]);N=7.;beta=.3
    L=np.zeros((size,size));R=np.zeros_like(L);current=np.zeros(size)
    sectors={}
    for z,s in enumerate(states):
        sectors.setdefault(tuple(np.bincount(s,minlength=3)),[]).append(z)
        for x in range(4):
            l,a,b,r=s[(x-1)%4],s[x],s[(x+1)%4],s[(x+2)%4]
            h=(f[a]-f[b])*(n[l]+n[r])+(n[a]-n[b])*(f[l]+f[r])
            c=.2+max(h,0.)
            swapped=s.copy();swapped[x],swapped[(x+1)%4]=b,a
            zz=index[tuple(swapped)]
            if zz!=z: L[z,zz]+=c;L[z,z]-=c
            if x==0: current[z]=c*(n[a]-n[b])
        for x in range(4):
            if s[x]==0:
                for label in (1,2):
                    new=s.copy();new[x]=label;zz=index[tuple(new)]
                    R[z,zz]+=beta;R[z,z]-=beta
    G=N*L+R
    h=current.copy()
    for sector in sectors.values(): h[sector]-=current[sector].mean()
    p_initial=np.array([.4,.2,.4])
    def law(t):
        p0=p_initial[0]*np.exp(-2*beta*t)
        p=p_initial.copy();p[0]=p0;p[1:]+=(p_initial[0]-p0)/2
        pdot=np.array([-2*beta*p0,beta*p0,beta*p0])
        nu=np.prod(p[states],axis=1)
        nudot=nu*np.sum(pdot[states]/p[states],axis=1)
        return nu,nudot
    errors={'product_forward_equation':0.,'reverse_row_sum':0.,'symmetric_detailed_balance':0.,
            'form_identity':0.,'poisson_residual':0.,'centered_current':0.}
    naive_adjoint_defect=0.;minimum_extra_eigenvalue=1.
    def norm(t,record=False):
        nonlocal naive_adjoint_defect,minimum_extra_eigenvalue
        nu,nudot=law(t);F=np.cos(t)*h
        adj=G.T*nu[None,:]/nu[:,None]
        rev=adj.copy();np.fill_diagonal(rev,0.)
        np.fill_diagonal(rev,-rev.sum(axis=1))
        S=(G+rev)/2
        augmented=np.block([[-S,np.ones((size,1))],[nu[None,:],np.zeros((1,1))]])
        u=solve(augmented,np.r_[F,0.],assume_a='gen')[:size]
        energy=float(np.dot(nu*F,u))
        if record:
            errors['product_forward_equation']=max(errors['product_forward_equation'],float(np.max(abs(nu@G-nudot))))
            errors['reverse_row_sum']=max(errors['reverse_row_sum'],float(np.max(abs(rev.sum(axis=1)))))
            errors['symmetric_detailed_balance']=max(errors['symmetric_detailed_balance'],float(np.max(abs(nu[:,None]*S-(nu[:,None]*S).T))))
            errors['poisson_residual']=max(errors['poisson_residual'],float(np.max(abs(-S@u-F))))
            errors['centered_current']=max(errors['centered_current'],float(abs(nu@F)))
            gamma=np.sum(nu[:,None]*G*(u[:,None]-u[None,:])**2)
            errors['form_identity']=max(errors['form_identity'],float(abs(gamma-2*energy)))
            naive_adjoint_defect=max(naive_adjoint_defect,float(np.max(abs(adj.sum(axis=1)))))
            Ladj=L.T*nu[None,:]/nu[:,None]
            extra=np.diag(np.sqrt(nu))*(-1.)@(S-N*(L+Ladj)/2)@np.diag(1/np.sqrt(nu))
            minimum_extra_eigenvalue=min(minimum_extra_eigenvalue,float(np.linalg.eigvalsh((extra+extra.T)/2).min()))
        return energy
    for t in np.linspace(0,3,17): norm(t,True)
    assert max(errors.values())<1e-10 and minimum_extra_eigenvalue>-1e-10 and naive_adjoint_defect>1.
    nu0=law(0)[0]
    def moments(t,y):
        nu,a,b=y.reshape(3,size);F=np.cos(t)*h
        return np.r_[G.T@nu,G.T@a+F*nu,G.T@b+2*F*a]
    times=np.array([.1,1.,3.])
    solution=solve_ivp(moments,(0,3),np.r_[nu0,np.zeros(2*size)],method='DOP853',
        t_eval=times,rtol=1e-11,atol=1e-13)
    assert solution.success
    nodes,weights=leggauss(64);comparisons=[]
    for j,T in enumerate(times):
        variance=float(solution.y[2*size:,j].sum())
        upper=float(T*np.dot(weights,[norm(T*(z+1)/2) for z in nodes]))
        assert variance>=-1e-12 and variance<=upper+1e-10
        comparisons.append({'time':float(T),'exact_augmented_moment_variance':variance,
            'forward_backward_energy_upper_bound':upper})
    result={'states':size,'swap_acceleration':N,'per_label_birth_rate':beta,
        'maximum_residuals':errors,'minimum_added_birth_form_eigenvalue':minimum_extra_eigenvalue,
        'wrong_plain_adjoint_row_sum_defect':naive_adjoint_defect,'energy_comparisons':comparisons,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Finite-model independent implementation paths: full forward equation, physical reverse rates, Poisson forms and augmented additive-functional moments. General theorem scrutiny remains pending.'}
    (HERE/'GROWING_PRODUCT_ENERGY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
