#!/usr/bin/env python3
"""Exact controls for integer-history quotients; no empirical fit or state selection."""
AUDIT_TIMEOUT_SEC = 180

from fractions import Fraction as F
from itertools import product
from math import floor, gcd
from functools import reduce
from pathlib import Path
import json
import sympy as s


def centered(x, period=F(1)):
    x, period = F(x), F(period)
    if period <= 0:
        raise ValueError('positive period required')
    return x-period*floor(x/period+F(1,2))


def projected_period(weights, period=F(1)):
    """Exact rational weights only; never round an arbitrary real coefficient."""
    if not weights:
        raise ValueError('at least one exact rational weight required')
    if any(not isinstance(x, (int, F, s.Rational)) for x in [*weights, period]):
        raise TypeError('floating or non-rational coefficients cannot establish a period')
    if period <= 0:
        raise ValueError('positive period required')
    values=[F(x)*period for x in weights]
    den=s.ilcm(*[x.denominator for x in values]) if len(values)>1 else values[0].denominator
    return F(reduce(gcd,[abs(int(x*den)) for x in values]),int(den))


def lattice_minimum_2d(r, G, period=s.Rational(1)):
    """Complete finite enumeration from an incumbent and exact trace bound.

    For SPD G, x^T G^-1 x >= ||x||^2/trace(G), so every improving
    lattice representative lies in the returned enclosing box.
    """
    G=s.Matrix(G);r=s.Matrix(r)
    if G.shape!=(2,2) or G!=G.T or G[0,0]<=0 or G.det()<=0 or period<=0:
        raise ValueError('2D SPD Gram and positive period required')
    inv=G.inv();inc=(r.T*inv*r)[0]
    # Integer ceiling via squared rational comparison avoids a floating search bound.
    radius2=s.cancel(inc*s.trace(G));R=0
    while R*R<radius2:R+=1
    bounds=[range(int(s.ceiling((-R-r[i])/period)),int(s.floor((R-r[i])/period))+1) for i in range(2)]
    vals=[((r+period*s.Matrix(k)).T*inv*(r+period*s.Matrix(k)))[0] for k in product(*bounds)]
    ks=list(product(*bounds));best=min(vals)
    return best,[list(k) for k,v in zip(ks,vals) if v==best],dict(radius_squared=str(radius2),radius=R,examined=len(vals))


def scalar_energy_floor(value, sigma_squared, error_bound, period=F(1)):
    """Conditional scalar Hilbert-norm floor, using the supplied image period."""
    sigma_squared, error_bound = F(sigma_squared), F(error_bound)
    if sigma_squared < 0 or error_bound < 0:
        raise ValueError('nonnegative norm and error bound required')
    distance = abs(centered(value, period))
    if sigma_squared == 0:
        if distance > error_bound:
            raise ValueError('datum incompatible with zero response and supplied error')
        return F(0)
    return max(distance-error_bound, F(0))**2/sigma_squared


def run():
    checks={}
    def check(name,cond):
        checks[name]=bool(cond)
        if not cond:raise AssertionError(name)
    M=2**32
    endpoints=[F(3,7),F(11,13),F(-5,17),F(7,19)]
    gamma=[-1,3,-3,1]
    base=sum(a*b for a,b in zip(gamma,endpoints))
    # Independent hand sums and exact fractions, not complex floating exponentials.
    for j,shifts in enumerate([(0,0,0,0),(M,-2*M,3*M,-4*M),(17,-11,31,-8),(M+3,-M-2,M+1,5)]):
        shifted=sum(a*(b+n+F(123,29)) for a,b,n in zip(gamma,endpoints,shifts))
        check('endpoint_integer_history_'+str(j),centered(shifted)==centered(base))
    for degree in range(3):check('polynomial_nuisance_degree_'+str(degree),sum(gamma[i]*i**degree for i in range(4))==0)
    counts=[b-a for a,b in zip(endpoints[:-1],endpoints[1:])]
    check('count_endpoint_incidence',counts[0]-2*counts[1]+counts[2]==base)
    check('half_weight_fails_mod_one',centered(F(1,7)+F(1,2))!=centered(F(1,7)))
    check('rational_period_restored',projected_period([F(1,2),1])==F(1,2))
    check('nonprimitive_period',projected_period([2,-4,2],F(7))==14)
    for name,values,period in [('floating_weight',[2**0.5,1],1),('floating_period',[1,2],1.0),('symbolic_irrational',[1,s.sqrt(2)],1)]:
        try:projected_period(values,period)
        except TypeError:check(name+'_rejected',True)
        else:check(name+'_rejected',False)
    check('fractional_reset_not_removed',centered(base+F(1,7))!=centered(base))
    # Displayed curved fixture: integer combinations generate a constant and H.
    H=s.symbols('H');b0=-1+H/5;b3=1-s.Rational(16,5)*H
    check('curved_group_H',s.expand(b0+b3)==-3*H)
    check('curved_group_constant',s.expand(15*b0+b0+b3)==-15)
    # Pell witnesses give arbitrarily small nonzero members of Z+sqrt(2)Z.
    pp,qq=1,1;pell=[]
    for i in range(8):
        check('pell_identity_'+str(i),pp*pp-2*qq*qq in (-1,1))
        pell.append({'p':pp,'q':qq,'absolute_group_element':str(1/(s.Integer(pp)+qq*s.sqrt(2)))})
        pp,qq=pp+2*qq,pp+qq
    G=s.Matrix([[3064,-1871],[-1871,3064]])/1620  # physical Gram is G/pi.
    r=[s.Rational(49,100)]*2
    best,lifts,box=lattice_minimum_2d(r,G)
    component=(s.Matrix(r).T*G.inv()*s.Matrix(r))[0]
    check('component_rounding_not_optimal',best<component and [-1,0] in lifts and [0,-1] in lifts)
    check('lattice_translation_same_minimum',lattice_minimum_2d([r[0]+2,r[1]-3],G)[0]==best)
    check('diagonal_gram_nearest_point',lattice_minimum_2d([s.Rational(3,5),s.Rational(2,7)],s.eye(2))[0]==s.Rational(4,25)+s.Rational(4,49))
    check('scalar_alias_saturation',centered(F(100000003,7))==centered(F(100000003,7)+M))
    # Exact scalar Cauchy lower bound under explicit endpoint errors.
    v=[1,-2,1];a=[F(2,3),F(-1,5),F(7,11)];x=F(5,7)
    e=[F(1,1000),-F(1,2000),F(1,3000)];k=[M+1,-8,19]
    r=[aa*x+ee+kk for aa,ee,kk in zip(a,e,k)]
    response=sum(vi*aa for vi,aa in zip(v,a));eta=sum(abs(vi*ee) for vi,ee in zip(v,e))
    d=abs(centered(sum(vi*rr for vi,rr in zip(v,r))))
    check('physical_error_scalar_bound',max(d-eta,0)**2<=response**2*x*x)
    # Separate example where no real error and the bound is exactly attained.
    response=F(3,2);x=F(1,9);d=abs(centered(response*x+7))
    check('sharp_scalar_Riesz_example',scalar_energy_floor(response*x+7,response**2,F(0))==x*x)
    check('nonzero_error_sharp_floor',scalar_energy_floor(F(3,20),1,F(1,20))==F(1,100))
    check('error_can_remove_floor',scalar_energy_floor(F(1,20),1,F(1,10))==0)
    check('zero_response_compatible',scalar_energy_floor(F(1,20),0,F(1,10))==0)
    try:scalar_energy_floor(F(1,5),0,F(1,10))
    except ValueError:check('zero_response_incompatible',True)
    else:check('zero_response_incompatible',False)
    check('arbitrary_integer_data_zero_signal',all(centered(z)==0 for z in [0,17,-8,M+1]))
    for name,fn in [('zero_period',lambda:centered(1,0)),('singular_Gram',lambda:lattice_minimum_2d([1,2],[[1,1],[1,1]]))]:
        try:fn()
        except ValueError:check(name+'_rejected',True)
        else:check(name+'_rejected',False)
    return {'role':'Exact mathematical controls under declared integer ambiguity and supplied response; no empirical validation','checks':checks,'passed':len(checks),'failed':0,'two_count_Gram_example':{'G_times_pi':str(G),'r':['49/100','49/100'],'minimum_N_over_pi':str(best),'component_rounding_N_over_pi':str(component),'minimizing_lifts':lifts,'complete_search_box':box},'irrational_group_Pell_witnesses':pell}


if __name__=='__main__':
    out=run()
    print(json.dumps({'passed':out['passed'],'failed':out['failed'],'two_count_Gram_example':out['two_count_Gram_example']},indent=2))
