#!/usr/bin/env python3
"""Primary exact controls for the supplied immutable directional-exchange law."""
from pathlib import Path
from itertools import product, permutations
from collections import defaultdict
from fractions import Fraction as F
import json,hashlib,platform
import numpy as np
import sympy as sp
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent
V=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

def tagged_bijections():
    L=3;sites=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(sites)}
    vectors=[V[0],V[3],V[4]]
    configurations=list(permutations(range(len(sites)),len(vectors)))
    def event(s,tag,sign=1):
        point=sites[s[tag]]
        target=index[tuple((point[i]+sign*vectors[tag][i])%L for i in range(3))]
        t=list(s)
        if target in s:
            other=s.index(target);t[other]=s[tag]
        t[tag]=target
        return tuple(t)
    for tag in range(len(vectors)):
        images=set()
        for s in configurations:
            t=event(s,tag)
            assert t[tag]!=s[tag]
            assert event(t,tag,-1)==s
            images.add(t)
        assert len(images)==len(configurations)
    return {'torus_side':L,'labeled_records':3,'placements':len(configurations),'event_inverse_checks':len(configurations)*3}

def full_ring_controls():
    # The x-direction contribution on a four-site periodic line. The other
    # four content species are transported by exchanges but have no own x clock.
    n=4;states=list(product(range(-1,6),repeat=n));B={};Q={}
    for s in states:
        hops=defaultdict(F);births=defaultdict(F)
        for x,a in enumerate(s):
            if a in (0,1):
                y=(x+(1 if a==0 else -1))%n
                t=list(s);t[x],t[y]=t[y],t[x];t=tuple(t)
                if t!=s:hops[t]+=1
            if a==-1:
                for b in range(6):
                    t=list(s);t[x]=b;births[tuple(t)]+=1
        Q[s]=dict(hops);B[s]=dict(births)
    incoming=defaultdict(F)
    for s in states:
        for t,rate in Q[s].items():incoming[t]+=rate;incoming[s]-=rate
    assert all(incoming[s]==0 for s in states)
    p=[F(1,3)]+[F(2*(a+1),63) for a in range(6)]
    mu={s:sp.prod(p[a+1] for a in s) for s in states}
    eps=F(2,7);dp=[-6*eps*p[0]]+[eps*p[0]]*6
    incoming=defaultdict(F)
    for s in states:
        for t,rate in Q[s].items():incoming[t]+=mu[s]*rate;incoming[s]-=mu[s]*rate
        for t,rate in B[s].items():incoming[t]+=mu[s]*eps*rate;incoming[s]-=mu[s]*eps*rate
    for s in states:
        assert incoming[s]==mu[s]*sum(dp[a+1]/p[a+1] for a in s)
    # Exact generator linear response at a homogeneous isotropic product law.
    rho=F(2,3);r=rho/6;p=[1-rho]+[r]*6
    mu={s:sp.prod(p[a+1] for a in s) for s in states}
    phases=[1,sp.I,-1,-sp.I]
    generator_values={}
    for s in states:
        generator_values[s]=[sum(rate*(int(t[0]==a)-int(s[0]==a)) for t,rate in Q[s].items()) for a in range(6)]
    measured=sp.zeros(6)
    for b in range(6):
        for s in states:
            score=sum(phases[x]*((-1/p[0]) if a==-1 else (1/p[b+1] if a==b else 0)) for x,a in enumerate(s))
            for a in range(6): measured[a,b]+=mu[s]*score*generator_values[s][a]
    D=sp.Matrix([-sp.I-1,sp.I-1,0,0,0,0])
    expected=sp.diag(*D)-2*r*sp.eye(6)-r*sp.ones(6,1)*D.T
    assert sp.simplify(measured-expected)==sp.zeros(6)
    return {'ring_states':len(states),'biased_product_forward_equations':len(states),'exact_initial_response_entries':36,'response_wavevector':'pi/2','response_density':str(rho)}

def currents_and_entropy():
    p=sp.symbols('p0:6',positive=True);q=sp.symbols('q0:6',positive=True)
    pfull=[1-sum(p)]+list(p);qfull=[1-sum(q)]+list(q)
    checks=0;covariance_checks=0
    C=sp.diag(*p)-sp.Matrix(p)*sp.Matrix(p).T
    for axis in range(3):
        plus,minus=2*axis,2*axis+1
        for a in range(6):
            actual=0
            for left,right in product(range(-1,6),repeat=2):
                rate=int(left==plus)+int(right==minus)
                actual+=pfull[left+1]*qfull[right+1]*rate*(int(left==a)-int(right==a))
            wanted=int(a==plus)*p[a]-int(a==minus)*q[a]-p[plus]*q[a]+q[minus]*p[a]
            assert sp.expand(actual-wanted)==0
            g=p[plus]-p[minus]
            assert sp.expand(actual.subs(dict(zip(q,p)))-p[a]*(V[a][axis]-g))==0
            for b in range(6):
                current_covariance=0
                for left,right in product(range(-1,6),repeat=2):
                    current=(int(left==plus)+int(right==minus))*(int(left==a)-int(right==a))
                    current_covariance+=pfull[left+1]*pfull[right+1]*current*(int(left==b)+int(right==b)-2*p[b])
                jacobian_covariance=sum(((V[a][axis]-g)*int(a==c)-p[a]*V[c][axis])*C[c,b] for c in range(6))
                assert sp.expand(current_covariance-jacobian_covariance)==0
                covariance_checks+=1
            checks+=1
    n=sp.symbols('n0:3');direction=sp.Matrix([sum(n[i]*V[a][i] for i in range(3)) for a in range(6)])
    pp=sp.Matrix(p);u=(pp.T*direction)[0];vac=1-sum(p)
    A=sp.diag(*(x-u for x in direction))-pp*direction.T
    H=sp.diag(*(1/x for x in p))+sp.ones(6)/vac
    wanted=sp.diag(*((direction[a]-u)/p[a] for a in range(6)))-u*sp.ones(6)/vac
    assert all(sp.factor(x)==0 for x in H*A-wanted)
    return {'bond_current_symbolic_identities':checks,'entropy_symmetrizer_entries':36,'current_conserved_density_covariance_entries':covariance_checks,'spatial_moment_scope':'local coefficient checked; infinite spatial sums justified analytically in note, not by enumeration'}

def mode_checks():
    rho,w,kx,ky,kz=sp.symbols('rho w kx ky kz');r=rho/6
    q=sp.Matrix([kx,-kx,ky,-ky,kz,-kz]);A=(sp.eye(6)-r*sp.ones(6))*sp.diag(*q)
    determinant=A.charpoly(w).as_expr()
    squares=[kx*kx,ky*ky,kz*kz]
    wanted=sp.prod(w*w-x for x in squares)+rho*sum(x*sp.prod(w*w-y for j,y in enumerate(squares) if j!=i) for i,x in enumerate(squares))/3
    assert sp.expand(determinant-wanted)==0
    axial=sp.factor(determinant.subs({ky:0,kz:0}))
    assert sp.expand(axial-w**4*(w*w-(1-rho/3)*kx*kx))==0
    diagonal=sp.factor(determinant.subs({ky:kx,kz:kx}))
    assert sp.expand(diagonal-(w*w-kx*kx)**2*(w*w-(1-rho)*kx*kx))==0
    u=sp.ones(6,1)/6;left=sp.ones(1,6)
    Aa=A.subs({ky:0,kz:0});speed2=(1-rho/3)*kx*kx
    assert all(sp.expand(x)==0 for x in Aa**3-speed2*Aa)
    assert sp.factor((left*Aa*u)[0])==0
    amplitude=sp.factor((left*Aa**2*u)[0]/speed2)
    assert sp.factor(amplitude-(1-rho)/(3-rho))==0
    Ad=A.subs({ky:kx,kz:kx})
    assert all(sp.expand(x)==0 for x in Ad**2*u-(1-rho)*kx*kx*u)
    errors=[]
    for density,t,k in product([.1,.5,.9],[.1,1.,10.],[.05,.4,1.]):
        B=np.eye(6)-density*np.ones((6,6))/6
        for direction in [np.array([k,0.,0.]),np.ones(3)*k/np.sqrt(3)]:
            qq=np.array(V)@direction;matrix=B@np.diag(qq)
            actual=(np.ones(6)@expm(-1j*t*matrix)@np.ones(6)/6).real
            if direction[1]==0:
                expected=2/(3-density)+(1-density)/(3-density)*np.cos(np.sqrt(1-density/3)*k*t)
            else:expected=np.cos(np.sqrt((1-density)/3)*k*t)
            errors.append(abs(actual-expected));assert abs(actual-expected)<1e-12
    return {'generic_characteristic_polynomial':str(sp.factor(wanted)),'axis_density_oscillation_amplitude':str(amplitude),'matrix_exponential_cases':len(errors),'maximum_response_error':max(errors)}

def one_record_check():
    L=5;Q=np.zeros((L,L))
    for x in range(L):Q[x,(x+1)%L]=1;Q[x,x]=-1
    errors=[]
    for mode,t in product(range(L),[.01,.2,1.,3.]):
        k=2*np.pi*mode/L;wave=np.exp(-1j*k*np.arange(L))
        actual=expm(Q*t)[0]@wave;expected=np.exp(t*(np.exp(-1j*k)-1))
        errors.append(abs(actual-expected));assert abs(actual-expected)<1e-12
    return {'one_direction_full_transition_matrix_cases':len(errors),'maximum_error':max(errors),'six_direction_propagator':'sum_i exp[(cos k_i-1)t] cos[t sin k_i]/3'}

def main():
    results={'tagged_bijections':tagged_bijections(),'full_ring_controls':full_ring_controls(),'currents_and_entropy':currents_and_entropy(),'mode_checks':mode_checks(),'one_record':one_record_check(),'status':'primary checks passed; no independent check or hydrodynamic limit','versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    text=json.dumps(results,indent=2)+'\n';(HERE/'IMMUTABLE_STREAMING_RESULTS.json').write_text(text);print(text,end='')
if __name__=='__main__':main()
