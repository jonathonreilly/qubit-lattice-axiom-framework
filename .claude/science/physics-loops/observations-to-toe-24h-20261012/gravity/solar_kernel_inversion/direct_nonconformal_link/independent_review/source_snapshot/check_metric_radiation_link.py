#!/usr/local/bin/python3
"""Frozen synthetic tests of the metric/source/radiation linkage; no fits."""
import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq


def symbolic():
    psi,lam=sp.symbols('psi lam',real=True)
    m,c,v=sp.symbols('m c v',positive=True)
    A=sp.exp(psi);B=sp.exp(-lam*psi);z=(B/A)**2*v*v/c**2
    L=-m*c*c*A*sp.sqrt(1-z)
    rho=-sp.diff(L,psi)/c**2
    expected=m*A*(1+lam*z)/sp.sqrt(1-z)
    assert sp.simplify(rho-expected)==0
    p=sp.diff(L,v);H=sp.simplify(p*v-L)
    assert sp.simplify(H-m*c*c*A/sp.sqrt(1-z))==0
    assert sp.simplify(H**2-m*m*c**4*A**2-c*c*(A/B)**2*p*p)==0
    t,P,V=sp.symbols('t P V',real=True)
    expanded=sp.series(expected.subs({psi:t*P,v:c*sp.sqrt(t*V)}),t,0,2).removeO()
    assert sp.simplify(expanded-m*(1+t*(P+(lam+sp.Rational(1,2))*V)))==0
    E2,B2=sp.symbols('E2 B2',nonnegative=True);n=B/A
    Lem=(n*E2-B2/n)/2;Hem=(n*E2+B2/n)/2
    assert sp.simplify(-sp.diff(Lem,psi)/c**2-(1+lam)*Hem/c**2)==0
    # Independent coordinate tensor differentiation of the Kepler moment.
    r,k,rd,vt,mu=sp.symbols('r k rd vt mu',positive=True)
    X=sp.Matrix([r,0,0]);vel=sp.Matrix([rd,vt,0]);acc=sp.Matrix([-k/r**2,0,0])
    jerk=sp.Matrix([2*k*rd/r**3,-k*vt/r**3,0])
    third=mu*(jerk*X.T+X*jerk.T+3*(acc*vel.T+vel*acc.T))
    STF=third-sp.eye(3)*sp.trace(third)/3
    assert sp.simplify(sp.trace(third)+2*mu*k*rd/r**2)==0
    assert sp.simplify(sum(x*x for x in STF)-sp.Rational(8,3)*mu**2*k**2/r**4*(rd**2+12*vt**2))==0
    e=sp.symbols('e',positive=True);d=1-e**2
    I3=(2+e**2)/(2*d**sp.Rational(5,2));I4=(2+3*e**2)/(2*d**sp.Rational(7,2))
    I5=(8+24*e**2+3*e**4)/(8*d**sp.Rational(9,2))
    J=sp.simplify(((e*e-1)*I5+2*I4-I3)/e**2)
    assert sp.simplify(J-(4+e**2)/(8*d**sp.Rational(7,2)))==0
    f=(1+sp.Rational(73,24)*e**2+sp.Rational(37,96)*e**4)/d**sp.Rational(7,2)
    assert sp.simplify(sp.Rational(8,3)*(12*(2*I4-I3)-11*e*e*J)-32*f)==0
    return {'exact_particle_source':'PASS','particle_Legendre_identity':'PASS',
            'weak_source_coefficient':'PASS','Maxwell_source_energy_link':'PASS',
            'Kepler_third_moment_and_trace':'PASS','eccentric_integral_algebra':'PASS'}


def bending(eps,kind):
    if eps==0:return 0.0
    if kind=='exponential':
        u0=brentq(lambda u:u-math.exp(eps*u),1,2,xtol=1e-14);h=eps*u0
        def integrand(chi):
            si=math.sin(chi);co2=math.cos(chi)**2
            delta=math.expm1(-2*h*co2/(1+si))/co2 if co2>1e-24 else -h
            return 1/math.sqrt(1+delta)-1
    elif kind=='Schwarzschild':
        u0=brentq(lambda u:1-u*u+2*eps*u**3,1,2,xtol=1e-14);h=eps*u0
        def integrand(chi):
            si=math.sin(chi)
            return 1/math.sqrt(1-2*h*(si+1/(1+si)))-1
    else:raise ValueError(kind)
    return 2*quad(integrand,0,math.pi/2,epsabs=2e-14,epsrel=2e-13)[0]


def orbit_samples(e,order=256):
    # G_N=M=a=1, reduced mass=1/4; c=1000 in radiation_integral.
    q,w=np.polynomial.legendre.leggauss(order);E=(q+1)*math.pi
    u=1-e*np.cos(E);scale=math.sqrt(1-e*e)
    X=np.stack([np.cos(E)-e,scale*np.sin(E),E*0],axis=1)
    V=np.stack([-np.sin(E)/u,scale*np.cos(E)/u,E*0],axis=1)
    r=np.linalg.norm(X,axis=1);xv=np.sum(X*V,axis=1)
    acc=-X/r[:,None]**3;jerk=-V/r[:,None]**3+3*X*xv[:,None]/r[:,None]**5
    def outer(a,b):return a[:,:,None]*b[:,None,:]
    third=.25*(outer(jerk,X)+outer(X,jerk)+3*(outer(acc,V)+outer(V,acc)))
    Udot=.25*xv/r**3;Tdot=.25*np.sum(V*acc,axis=1)
    return w*u/2,third,Udot,Tdot


def radiation_integral(e,lam,s,order=256):
    weights,third,Udot,Tdot=orbit_samples(e,order)
    c=1000.;cs=c*s
    # Integrate the uncompleted monopole/quadrupole amplitude over the sky.
    zs,wz=np.polynomial.legendre.leggauss(6);az=np.arange(16)*2*math.pi/16
    Z,AZ=np.meshgrid(zs,az,indexing='ij')
    normals=np.stack([np.sqrt(1-Z*Z)*np.cos(AZ),np.sqrt(1-Z*Z)*np.sin(AZ),Z],axis=-1).reshape(-1,3)
    angweights=np.repeat(wz/2,16)/16
    projected=np.einsum('ai,tij,aj->ta',normals,third,normals)
    Qdot=(2*Udot+(2*lam+1)*Tdot)/c**2
    amplitude=Qdot[:,None]+projected/(2*cs**2)
    power=float(weights@(amplitude**2@angweights)/cs)
    trace=np.trace(third,axis1=1,axis2=2)
    STF=third-trace[:,None,None]*np.eye(3)/3
    STFavg=float(weights@np.sum(STF*STF,axis=(1,2)))
    Uavg=float(weights@(Udot**2))
    GR=STFavg/(5*c**5)
    F=1+73*e*e/24+37*e**4/96
    ratio=s**-5*(1/6+5/256*((1-2*lam)*s*s-1/3)**2*e*e*(4+e*e)/F)
    relative=abs(power/GR-ratio)/max(1,abs(ratio))
    f=F/(1-e*e)**3.5
    Uclosed=.25**2*e*e*(4+e*e)/(8*(1-e*e)**3.5)
    STFclosed=32*.25**2*f
    assert relative<1e-10,(e,lam,s,relative)
    assert abs(STFavg/STFclosed-1)<1e-10
    assert abs(Uavg-Uclosed)<1e-10*max(1,Uclosed)
    assert np.max(np.abs(trace+2*Udot))<1e-10
    return {'eccentricity':e,'lambda':lam,'c_s_over_c':s,'power':power,
            'same_orbit_GR_comparator':GR,'direct_ratio':power/GR,'formula_ratio':ratio,
            'relative_error':relative,'Udot_squared_average':Uavg,
            'Udot_squared_closed':Uclosed,'STF_third_squared_average':STFavg,
            'STF_third_squared_closed':STFclosed}


def run():
    identities=symbolic();bends=[]
    for eps in [.001,.003,.01,.03]:
        for kind,first,second in [('exponential',2,math.pi),('Schwarzschild',4,15*math.pi/4)]:
            actual=bending(eps,kind);scaled=(actual-first*eps-second*eps**2)/eps**3
            assert 0<scaled<(20 if kind=='exponential' else 100),(eps,kind,scaled)
            bends.append({'kind':kind,'expansion_parameter':eps,'angle':actual,
                          'first_plus_second':first*eps+second*eps**2,'cubic_scaled_residual':scaled})
    rows=[radiation_integral(e,lam,s) for e in [0,.2,.6,.8]
          for lam in [-1,0,1] for s in [.6,1,1.4]]
    # One high-eccentricity grid refinement changes only quadrature order.
    refined=radiation_integral(.8,1,.6,128);target=next(r for r in rows if r['eccentricity']==.8 and r['lambda']==1 and r['c_s_over_c']==.6)
    refinement=abs(refined['power']/target['power']-1);assert refinement<1e-10
    speed=6**(-.2);cancel=(1-1/(3*speed*speed))/2
    calibration=[radiation_integral(e,1,speed) for e in [0,.2,.6,.8]]
    assert abs(calibration[0]['direct_ratio']-1)<1e-10
    assert all(r['direct_ratio']>1 for r in calibration[1:])
    cancellation=[radiation_integral(e,cancel,speed) for e in [0,.2,.6,.8]]
    assert all(abs(r['direct_ratio']-1)<1e-10 for r in cancellation)
    assert 0<cancel<.3 and abs(cancel-1)>.7
    # Same mass/orbit units used above meet the weak-source conditions.
    e=.8;c=1000.;vmax=math.sqrt((1+e)/(1-e));phi_max=1/(1-e)
    assert vmax/c<.01 and vmax/(.6*c)<.01 and phi_max/c**2<1e-5
    path=Path(__file__).resolve()
    return {'status':'PASS conditional synthetic comparisons; no observation fit',
            'created_at':dt.datetime.now(dt.timezone.utc).isoformat(),
            'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
              for p in [path,path.with_name('PROTOCOL.md'),path.with_name('DIRECT_METRIC_RADIATION_LINK.md')]},
            'symbolic':identities,'bending_rows':bends,'radiation_rows':rows,
            'max_ratio_relative_error':max(r['relative_error'] for r in rows),
            '128_to_256_refinement_relative':refinement,
            'circular_calibrated_speed_over_c':speed,'monopole_cancel_lambda':cancel,
            'bending_calibration_lambda':1,'circular_calibration_rows':calibration,
            'alternative_cancellation_rows':cancellation,
            'weak_source_control':{'c':c,'G_N':1,'M':1,'a':1,'mu':.25,
              'largest_e':e,'max_v_over_c':vmax/c,'max_v_over_min_cs':vmax/(.6*c),
              'upper_orbital_potential_over_c2':phi_max/c**2},
            'scope':'Constant-self-term separated weak bodies; isotropic sector; no neutron-star, timing likelihood or full PPN result.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    result=run()
    with Path(args.output).open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if not k.endswith('_rows')},indent=2))
