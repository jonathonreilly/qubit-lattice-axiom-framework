#!/usr/bin/env python3
"""Finite direct-clock and shifted-current checks, not an infinite-volume proof."""
from itertools import product
from pathlib import Path
import json
import numpy as np
from scipy.special import logsumexp


def theta_f(beta,x,qmax=12):
    q=np.arange(1,qmax+1,dtype=float)
    r=np.exp(-np.pi**2*beta*q*q/3)
    return (1+2*np.cos(2*np.pi*np.asarray(x)[...,None]*q)@r)/(1+2*r.sum())


def curvature_majorant(beta):
    q=np.arange(1,30,dtype=float)
    r=np.exp(-np.pi**2*beta*q*q/3)
    floor=1-2*r.sum()
    assert floor>0
    m1=4*np.pi*(q*r).sum()
    m2=8*np.pi**2*(q*q*r).sum()
    return m2/floor+(m1/floor)**2


def clock_character(n,beta,source):
    # On one oriented three-cube the six face fluxes obey sum b=0 mod N.
    # The first five are independent uniform gauge-quotient coordinates.
    x=np.asarray(list(product(range(n),repeat=5)),dtype=float)
    b=np.column_stack((x,np.mod(-x.sum(axis=1),n)))
    angles=2*np.pi*np.arange(n)/n
    images=np.arange(-7,8)
    lw=logsumexp(-beta/2*(angles[:,None]-2*np.pi*images)**2,axis=1)
    logweights=lw[b.astype(int)].sum(axis=1)
    probabilities=np.exp(logweights-logsumexp(logweights))
    phases=np.exp(2j*np.pi*(b@source)/n)
    value=probabilities@phases
    assert abs(value.imag)<2e-13 and value.real>0
    return float(value.real)


def current_coset(n,beta,source,cutoff,drop_magnetic=False,wrong_shift=False):
    basis=np.asarray(list(product(range(-cutoff,cutoff+1),repeat=5)),dtype=float)
    basis=np.column_stack((basis,np.zeros(len(basis))))
    shift=(source-source[-1])/ (1 if wrong_shift else n)
    def weights(a):
        projected=a-a.mean(axis=1)[:,None]
        value=np.exp(-n*n/(2*beta)*(projected*projected).sum(axis=1))
        if not drop_magnetic:
            value*=theta_f(beta,n*projected[:,-1])
        return value
    return float(weights(basis+shift).sum()/weights(basis).sum())


def coset_tail_bound(n,beta,source,cutoff,ratio):
    # P on the five-coordinate quotient is I-11^T/6. Conditioning on
    # one coordinate gives energy x_i^2/2. The remaining precision is
    # B=I_4-11^T/6, det B=1/3 and B^-1>=I. Gaussian Poisson summation
    # bounds every translated four-dimensional sum by the expression below.
    a=n*n/(2*beta)
    q=np.pi*np.pi/a
    theta_bound=1+2*np.exp(-q)/(1-np.exp(-3*q))
    conditional_bound=np.sqrt(3)*(np.pi/a)**2*theta_bound**4
    def tail(shift):
        result=0.
        for value in shift:
            for sign in [-1,1]:
                x=cutoff+1+sign*value
                assert x>0
                result+=np.exp(-a*x*x/2)/(1-np.exp(-a*(x+.5)))
        return conditional_bound*result
    shifted=(source[:-1]-source[-1])/n
    # The retained denominator is at least its unit origin weight.
    return float(tail(shifted)+ratio*tail(np.zeros(5)))


def periodized_log(alpha,z,shift,center=0):
    grid=np.arange(-20,21,dtype=float)+shift
    v=alpha*(grid-center)**2/2-z*np.cos(2*np.pi*grid)
    return float(logsumexp(-v))


def main():
    data={'scope':'Finite three-cube and one-dimensional challenges; not the four-dimensional thermodynamic theorem.',
          'independent_review':False,'families':{}}
    cases=[]
    for alpha,z in [(3.,.03),(1.,.2),(20.,.3)]:
        upper=alpha+z*(2*np.pi)**2
        for shift in [.025,.15,.5,1.15]:
            actual=periodized_log(alpha,z,shift)-periodized_log(alpha,z,0)
            bound=-upper*shift*shift/2
            assert actual>=bound-2e-13
            assert abs(actual-(periodized_log(alpha,z,shift+1)-periodized_log(alpha,z,0)))<2e-13
            cases.append({'alpha':alpha,'z':z,'shift':shift,'log_ratio':actual,'lower_bound':bound,
                          'potential_is_nonconvex':alpha-z*(2*np.pi)**2<0})
    data['families']['periodized_curvature']={'cases':cases}
    alpha,z,shift=20.,.3,.025
    actual=periodized_log(alpha,z,shift)-periodized_log(alpha,z,0)
    wrong_bound=-(alpha-z*(2*np.pi)**2)*shift**2/2
    assert actual<wrong_bound-1e-4
    nonsym=periodized_log(80.,0.,-.2,.2)-periodized_log(80.,0.,0.,.2)
    assert nonsym< -80*.2**2/2-1
    data['families']['assumption_faults']={'wrong_curvature_margin':wrong_bound-actual,
                                         'non_even_log_ratio':nonsym,'invalid_even_bound':-80*.2**2/2}

    sources=[np.array([1,0,0,0,0,0]),np.array([1,1,0,0,0,0]),np.array([1,2,0,-1,0,0])]
    checks=[]
    for n,beta in [(2,2.),(3,2.),(5,2.),(3,3.)]:
        eps=curvature_majorant(beta)
        for source in sources:
            exact=clock_character(n,beta,source)
            projections=source-source.mean()
            energy=float(projections@projections)
            lower=float(np.exp(-(1/beta+eps)*energy/2))
            assert exact>=lower-2e-13 and exact<=1+2e-13
            cutoffs=[3,4,5,6,7] if n==2 else ([2,3,4,5,6] if beta==3 else [2,3,4,5])
            sums=[current_coset(n,beta,source,k) for k in cutoffs]
            tail_bound=coset_tail_bound(n,beta,source,cutoffs[-1],sums[-1])
            assert abs(sums[-1]-exact)<3e-8
            assert abs(sums[-1]-exact)<=tail_bound+5e-13
            checks.append({'N':n,'beta':beta,'source':source.tolist(),'curvature_epsilon_majorant':eps,
                           'coulomb_energy':energy,'direct_clock':exact,'lower_bound':lower,
                           'cutoffs':cutoffs,'coset_values':sums,'last_absolute_discrepancy':abs(sums[-1]-exact),
                           'analytic_gaussian_truncation_bound_evaluated_in_float':tail_bound})
    data['families']['clock_vs_current_coset']={'cases':checks}
    source=sources[0]
    exact=clock_character(3,2.,source)
    wrong=current_coset(3,2.,source,4,wrong_shift=True)
    dropped=current_coset(3,2.,source,4,drop_magnetic=True)
    assert abs(wrong-exact)>1e-4 and abs(dropped-exact)>1e-8
    alias=clock_character(3,2.,3*source)
    assert abs(alias-1)<2e-13
    charge2=clock_character(3,2.,2*source)
    assert abs(charge2-exact)<2e-13
    data['families']['physical_alias_and_source_faults']={'physical_character':exact,'wrong_shift':wrong,
                'dropped_magnetic_factor':dropped,'charge_N_alias':alias,'charge_two_equals_minus_one':charge2}
    path=Path(__file__).with_name('BLOCK29_WILSON_SHIFT_CHECKS.json')
    path.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'families':len(data['families']),'all_assertions_completed':True,'output':str(path)},indent=2))


if __name__=='__main__':
    main()
