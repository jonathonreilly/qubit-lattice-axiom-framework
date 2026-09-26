#!/usr/bin/env python3
"""Primary exact checks of the all-density immutable context construction."""
from pathlib import Path
from itertools import product, permutations
from fractions import Fraction as R
import hashlib
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
V=np.array([[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=int)
n=np.array([0]+[1]*6)
s=2*n[:,None]-3*V**2
CHECKS=[]


def check(name,okay,details=None):
    if not okay: raise AssertionError((name,details))
    CHECKS.append({'name':name,'passed':True,'details':details})


def h2(axis,string):
    l,a,b,r=string;f=V[:,axis];v=s[:,axis]
    return int((f[a]-f[b])*(v[l]+v[r])+(v[a]-v[b])*(f[l]+f[r]))


def iszero(matrix): return all(sp.expand(x)==0 for x in matrix)


def main():
    strings=list(product(range(7),repeat=4))
    rates=np.array([[h2(i,string) for string in strings] for i in range(3)])
    check('sharp_local_asymmetry_bound',rates.min()==-8 and rates.max()==8,
          {'local_axis_cases':int(rates.size),'h_min':int(rates.min()/2),'h_max':int(rates.max()/2)})
    check('endpoint_antisymmetry',all(h2(i,(l,b,a,r))==-h2(i,(l,a,b,r))
          for i in range(3) for l,a,b,r in strings))
    check('strict_floors_both_implementations',np.min(1+np.maximum(10*rates,0))==1 and np.min(50+5*rates)==10,
          {'minimal_floor':'1/20','linear_K':'5/2','linear_floor':'1/2'})
    lookup={tuple(v):a for a,v in enumerate(V)}
    tested=0
    for perm in permutations(range(3)):
        for signs in product([-1,1],repeat=3):
            transform=np.zeros((3,3),dtype=int)
            for old in range(3): transform[perm[old],old]=signs[old]
            labels=[lookup[tuple(transform@v)] for v in V]
            for old in range(3):
                for string in strings:
                    new=tuple(labels[a] for a in string)
                    if signs[old]<0: new=new[::-1]
                    assert h2(perm[old],new)==h2(old,string)
                    tested+=1
    check('all_signed_cubic_transforms',tested==48*3*7**4,{'local_cases':tested})
    for length in (4,5):
        total=0
        for state in product(range(7),repeat=length):
            for axis in range(3):
                balance=sum(h2(axis,(state[(x-1)%length],state[x],state[(x+1)%length],state[(x+2)%length])) for x in range(length))
                assert balance==0
                total+=1
        check(f'periodic_pointwise_balance_length_{length}',True,{'axis_configurations':total})

    probability_cases=[[R(3,4)]+[R(1,24)]*6,[R(1,2)]+[R(1,12)]*6,
                       [R(1,4)]+[R(1,8)]*6,[R(x,26) for x in [5,1,2,3,4,5,6]]]
    averages=[]
    for case,p in enumerate(probability_cases):
        for axis in range(3):
            g=sum(p[a]*int(V[a,axis]) for a in range(7))
            S=sum(p[a]*int(s[a,axis]) for a in range(7))
            target=[p[a]*(S*int(V[a,axis])+(int(s[a,axis])-2*S)*g) for a in range(7)]
            for variant in ('minimal','linear'):
                current=[R(0)]*7
                for string in strings:
                    l,a,b,r=string
                    mass=p[l]*p[a]*p[b]*p[r]
                    h=R(h2(axis,string),2)
                    c=R(1,20)+max(h,0) if variant=='minimal' else R(5,2)+h/2
                    current[a]+=mass*c;current[b]-=mass*c
                assert current==target
                averages.append({'case':case,'axis':axis,'variant':variant,'currents':[str(x) for x in current]})
    check('direct_four_site_product_current',True,{'case_count':len(averages),'species_per_case':7})

    p=sp.Matrix(sp.symbols('p1:7'));rho=sum(p);one=sp.ones(6,1)
    C=sp.diag(*p)-p*p.T
    alpha=sp.symbols('alpha',real=True)
    field=sp.Matrix([[1]*6,[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1],
                     [1,1,-1,-1,0,0],[1,1,1,1,-2,-2]])
    rho0=sp.symbols('rho',positive=True);balanced={x:rho0/6 for x in p}
    ks=sp.symbols('kx ky kz',real=True)
    combined=sp.zeros(6)
    general=sp.zeros(6)
    u,E,aa,bb=sp.symbols('u E a b',real=True)
    for axis in range(3):
        f=sp.Matrix(V[1:,axis].tolist());feature=sp.Matrix(s[1:,axis].tolist())
        g=(p.T*f)[0];S=(p.T*feature)[0];potential=alpha*S*g
        J=sp.Matrix([alpha*p[a]*(S*f[a]+(feature[a]-2*S)*g) for a in range(6)])
        check(f'flux_potential_axis_{axis}',iszero(C*sp.Matrix([sp.diff(potential,x) for x in p])-J))
        jac=J.jacobian(p)
        check(f'full_entropy_symmetry_axis_{axis}',iszero(jac*C-(jac*C).T))
        combined+=ks[axis]*field*jac.subs(balanced)*field.inv()
        feature_general=aa*one+bb*sp.Matrix((V[1:,axis]**2).tolist())
        Sg=(p.T*feature_general)[0]
        Jg=sp.Matrix([p[a]*(u*(f[a]-g)+2*E*(Sg*f[a]+(feature_general[a]-2*Sg)*g)) for a in range(6)])
        general+=ks[axis]*field*Jg.jacobian(p).subs(balanced)*field.inv()
    x,y,z=ks
    ac=2*alpha*rho0*(1-rho0);bc=2*alpha*rho0/3
    expected=sp.Matrix([[0,ac*x,ac*y,ac*z,0,0],[bc*x,0,0,0,0,0],
                        [bc*y,0,0,0,0,0],[bc*z,0,0,0,0,0],[0]*6,[0]*6])
    check('all_density_all_direction_field_matrix',iszero(combined-expected))
    T=u+4*E*(aa+bb/3)*rho0
    ell=u+2*E*(aa+2*bb/3)*rho0
    ag=(1-rho0)*T;bg=T/3
    expectedg=sp.Matrix([[0,ag*x,ag*y,ag*z,0,0],[bg*x,0,0,0,ell*x/2,ell*x/6],
                         [bg*y,0,0,0,-ell*y/2,ell*y/6],[bg*z,0,0,0,0,-ell*z/3],
                         [0,ell*x,-ell*y,0,0,0],[0,ell*x,ell*y,-2*ell*z,0,0]])
    check('general_polarized_family_field_matrix',iszero(general-expectedg))
    lam=sp.symbols('lambda')
    cp=expected.charpoly(lam)
    check('all_direction_acoustic_polynomial',sp.factor(cp.as_expr()-cp.gen**4*(cp.gen**2-ac*bc*(x*x+y*y+z*z)))==0)
    A,B,L=sp.symbols('A B L',real=True)
    template=sp.Matrix([[0,A*x,A*y,A*z,0,0],[B*x,0,0,0,L*x/2,L*x/6],
                        [B*y,0,0,0,-L*y/2,L*y/6],[B*z,0,0,0,0,-L*z/3],
                        [0,L*x,-L*y,0,0,0],[0,L*x,L*y,-2*L*z,0,0]])
    axis=template.subs({x:1,y:0,z:0}).charpoly(lam)
    diagonal=template.subs({x:1/sp.sqrt(3),y:1/sp.sqrt(3),z:1/sp.sqrt(3)}).charpoly(lam)
    check('generic_axis_spectrum',sp.factor(axis.as_expr()-axis.gen**4*(axis.gen**2-A*B-2*L**2/3))==0)
    check('generic_body_diagonal_spectrum',sp.factor(diagonal.as_expr()-(diagonal.gen**2-L**2/3)**2*(diagonal.gen**2-A*B))==0)
    selection=sp.Poly(ell,rho0)
    check('all_density_decoupling_coefficients',selection.all_coeffs()==[2*E*aa+4*E*bb/3,u])
    result={'status':'all_primary_exact_checks_passed','checks':CHECKS,'count':len(CHECKS),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'direct_product_averages':averages,
            'scope':'Supplied rates, exact product currents, entropy symmetry and current spectrum. No independent status or microscopic limit inferred from enumeration.'}
    output=json.dumps(result,indent=2)+'\n'
    (HERE/'AXIS_BALANCED_CONTEXT_RESULTS.json').write_text(output)
    print(output,end='')


if __name__=='__main__': main()
