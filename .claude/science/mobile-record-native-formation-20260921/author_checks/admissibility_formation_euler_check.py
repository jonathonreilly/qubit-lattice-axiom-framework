#!/usr/bin/env python3
"""Exact local reaction and adjoint controls; not a hydrodynamic proof."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from math import factorial, prod
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
V=((0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
checks=[]


def check(name, ok, detail=None):
    if not ok: raise AssertionError((name,detail))
    checks.append(dict(name=name,passed=True,detail=detail))
    print('PASS:',name,flush=True)


def compositions(total,slots):
    if slots==1:
        yield (total,)
    else:
        for a in range(total+1):
            for rest in compositions(total-a,slots-1): yield (a,)+rest


def main():
    menus=[]
    for j in (F(-1,2),F(1,2),F(9,10)):
        menus.append([[F(1)+j*sum(x*y for x,y in zip(V[a],V[b])) for b in range(7)] for a in range(1,7)])
    # A positive, non-symmetric table checks that no unmentioned symmetry is
    # used in the general adjoint identity.
    menus.append([[F(1)]+[F(3+(2*a+3*b)%7,6) for b in range(1,7)] for a in range(1,7)])
    laws=[[F(1,2)]+[F(1,12)]*6,[F(a,35) for a in (5,1,2,3,4,9,11)]]
    sectors=list(compositions(6,7))
    records=[]
    for menu_index,W in enumerate(menus):
        for law_index,p in enumerate(laws):
            means=[]
            for a in range(6):
                observed=F(0)
                for counts in sectors:
                    mass=F(1)
                    for b,c in enumerate(counts):
                        mass *= (p[b]*W[a][b])**c
                    ways=factorial(6)//prod(factorial(c) for c in counts)
                    observed+=ways*mass
                target=sum(p[b]*W[a][b] for b in range(7))**6
                assert observed==target
                means.append(str(p[0]*observed))
            records.append(dict(menu=menu_index,law=law_index,birth_means=means))
    check('six_neighbor_multinomial_direct_hazard_average',True,
          dict(menus=len(menus),laws=len(laws),sectors=len(sectors),labels=6))

    # Assemble only the birth generator on a four-cycle directly from events.
    # This checks product averages and, separately, failure of exact product
    # propagation once the birth rate depends on neighbors.
    states=list(product(range(7),repeat=4));index={a:i for i,a in enumerate(states)}
    p=laws[1];W=menus[1]
    mass=[]
    for word in states:
        z=F(1)
        for a in word: z*=p[a]
        mass.append(z)
    forward=[F(0)]*len(states);birth=[F(0)]*6
    for number,word in enumerate(states):
        for x in range(4):
            if word[x]: continue
            for a in range(1,7):
                rate=W[a-1][word[(x-1)%4]]*W[a-1][word[(x+1)%4]]
                after=list(word);after[x]=a
                amount=mass[number]*rate
                forward[number]-=amount;forward[index[tuple(after)]]+=amount
                birth[a-1]+=amount/4
    B=[p[0]*sum(p[b]*W[a][b] for b in range(7))**2 for a in range(6)]
    check('direct_2401_state_birth_generator_first_moments',birth==B and sum(forward)==0)
    pdot=[-sum(B)]+B
    product_derivative=[]
    for number,word in enumerate(states):
        product_derivative.append(mass[number]*sum(pdot[a]/p[a] for a in word))
    difference=max(abs(a-b) for a,b in zip(forward,product_derivative))
    check('negative_control_interacting_birth_law_is_not_product',difference>0,
          dict(max_probability_derivative_residual=str(difference)))
    # Apply the adjoint explicitly to the uniform product: the sum of
    # incoming rates at each occupied site has no additional ratio.
    for word in states:
        local=F(0)
        for x in range(4):
            if word[x]: local+=W[word[x]-1][word[(x-1)%4]]*W[word[x]-1][word[(x+1)%4]]
            else: local-=sum(W[a][word[(x-1)%4]]*W[a][word[(x+1)%4]] for a in range(6))
        assert local<=4*max(F(1),max(map(max,W)))**2
    check('uniform_reference_birth_adjoint_upper_bound',True)

    p=s.Matrix(s.symbols('p1:7',positive=True));q=s.Matrix(s.symbols('q1:7',positive=True))
    p0=1-sum(p);q0=1-sum(q)
    beta=s.symbols('beta',nonnegative=True)
    H=s.diag(*[1/x for x in p])+s.ones(6)/p0
    for menu_index,W in enumerate(menus):
        Wr=s.Matrix([[s.Rational(x.numerator,x.denominator) for x in row[1:]] for row in W])
        mp=s.ones(6,1)*p0+Wr*p;mq=s.ones(6,1)*q0+Wr*q
        B=s.Matrix([beta*p0*m**6 for m in mp])
        Vbar=sum(beta*(q[a]*p0/p[a]-q0)*mq[a]**6 for a in range(6))
        subs=dict(zip(q,p))
        assert s.simplify(Vbar.subs(subs))==0
        derivative=s.Matrix([s.diff(Vbar,x).subs(subs) for x in q])
        assert all(s.factor(x)==0 for x in derivative-H*B)
    check('reaction_adjoint_constant_and_first_order_cancellation',True,dict(menus=len(menus)))

    rho,j=s.symbols('rho j',real=True)
    field=s.Matrix([[1]*6,[1,-1,0,0,0,0],[0,0,1,-1,0,0],[0,0,0,0,1,-1],
                    [1,1,-1,-1,0,0],[1,1,1,1,-2,-2]])
    gv=[sum(p[a]*V[a+1][i] for a in range(6)) for i in range(3)]
    B=s.Matrix([beta*p0*(1+j*sum(V[a+1][i]*gv[i] for i in range(3)))**6 for a in range(6)])
    jac=field*B.jacobian(p).subs({a:rho/6 for a in p})*field.inv()
    expected=s.diag(-6*beta,12*beta*j*(1-rho),12*beta*j*(1-rho),12*beta*j*(1-rho),0,0)
    check('complete_six_field_linear_reaction',all(s.factor(x)==0 for x in jac-expected))
    gx,gy,gz=s.symbols('gx gy gz',real=True);gs=(gx,gy,gz)
    source_plus=[beta*(1-rho)*(1+j*g)**6 for g in gs]
    source_minus=[beta*(1-rho)*(1-j*g)**6 for g in gs]
    Brho=sum(source_plus)+sum(source_minus)
    scalar=beta*(1-rho)*(6+30*j**2*sum(g*g for g in gs)+30*j**4*sum(g**4 for g in gs)+2*j**6*sum(g**6 for g in gs))
    check('full_nonlinear_density_source',s.expand(Brho-scalar)==0)
    assert all(s.expand(plus-minus-beta*(1-rho)*(12*j*g+40*j**3*g**3+12*j**5*g**5))==0
               for plus,minus,g in zip(source_plus,source_minus,gs))
    check('full_nonlinear_vector_source',True)
    z=s.symbols('z')
    for i,g in enumerate(gs):
        rsource=source_plus[i]+source_minus[i]-Brho/3
        quadratic=s.expand(rsource.subs({h:z*h for h in gs})).coeff(z,2)
        assert s.expand(quadratic-30*beta*(1-rho)*j*j*(g*g-sum(h*h for h in gs)/3))==0
    check('quadratic_axis_occupation_source_retained',True)
    rho0,t=s.symbols('rho0 t',positive=True)
    rhot=1-(1-rho0)*s.exp(-6*beta*t)
    gain=s.exp(2*j*(rhot-rho0))
    check('uniform_linear_response_integrates_exactly',s.simplify(s.diff(gain,t)-12*beta*j*(1-rhot)*gain)==0)
    a,b,k,lam,zz=s.symbols('a b k lam zz')
    matrix=s.Matrix([[-6*beta,-s.I*a*k],[-s.I*b*k,lam]])
    check('frozen_longitudinal_characteristic_polynomial',s.expand(matrix.charpoly(zz).as_expr()-((zz+6*beta)*(zz-lam)+a*b*k*k))==0)
    result=dict(status='primary_algebraic_controls_passed',checks=checks,product_hazard_averages=records,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope='Finite and symbolic reaction controls only. General Euler convergence requires the explicit entropy proof and independent scrutiny.')
    (HERE/'ADMISSIBILITY_FORMATION_EULER_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('TOTAL:',len(checks),'PASS',flush=True)


if __name__=='__main__': main()
