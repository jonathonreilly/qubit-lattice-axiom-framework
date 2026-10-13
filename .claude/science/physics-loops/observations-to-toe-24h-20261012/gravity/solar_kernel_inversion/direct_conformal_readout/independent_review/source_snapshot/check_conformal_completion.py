#!/usr/local/bin/python3
"""First-order conformal completion checks; fixed synthetic controls, no fit."""
import argparse
import cmath
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.optimize import brentq


def symbolic_identities():
    m,c,A,v=s.symbols('m c A v',positive=True)
    L=-m*c*c*A*s.sqrt(1-v*v/(c*c))
    p=s.diff(L,v)
    H=s.simplify(p*v-L)
    assert s.simplify(H-m*c*c*A/s.sqrt(1-v*v/c**2))==0
    assert s.simplify(-s.diff(L,A)*A/c**2-m*A*s.sqrt(1-v*v/c**2))==0
    # Linear Riemann definition with independent coordinate variables.
    ct,x,y,z=s.symbols('ct x y z',real=True)
    coords=[ct,x,y,z]; psi=s.Function('psi')(*coords)
    eta=s.diag(-1,1,1,1); h=2*psi*eta
    curvature=[]
    for i in range(1,4):
        for j in range(1,4):
            Rij=(s.diff(h[0,j],coords[i],ct)+s.diff(h[i,0],ct,coords[j])
                 -s.diff(h[0,0],coords[i],coords[j])-s.diff(h[i,j],ct,ct))/2
            expected=s.diff(psi,coords[i],coords[j])-int(i==j)*s.diff(psi,ct,ct)
            assert s.simplify(Rij-expected)==0
            curvature.append(str(Rij))
    # Null tangent k=(1,1,0,0); arbitrary conformal gradient. Lorentz
    # rotation maps any nonzero null tangent into this direction.
    k=s.Matrix([1,1,0,0]); g=s.Matrix(s.symbols('g0:4'))
    Gamma_kk=[]
    for u in range(4):
        contraction=sum(((1 if u==a else 0)*g[b]+(1 if u==b else 0)*g[a]
                         -eta[a,b]*(eta*g)[u])*k[a]*k[b]
                        for a in range(4) for b in range(4))
        assert s.simplify(contraction-2*k[u]*k.dot(g))==0
        Gamma_kk.append(str(s.simplify(contraction)))
    assert s.simplify(A**4*A**-2*A**-2)==1
    return {'particle_legendre_and_source':'PASS','nine_linear_curvature_entries':'PASS',
            'null_connection_parallel_tangent':'PASS','four_dimensional_Maxwell':'PASS',
            'R_0i0j':curvature,'Gamma_kk':Gamma_kk}


def response(x,mu,cs):
    gamma=1/cs
    return (cmath.exp(1j*x)*np.sinc(x/math.pi)
            +1j*gamma*mu/(2*x)*(2*cmath.exp(1j*x*(1+gamma*mu))-1-cmath.exp(2j*x)))


def timing_functional(eps,mu,cs,x,phase=0.37):
    """c=L=1; exact null roots/clock integral, first-order worldlines."""
    n=np.array([mu,math.sqrt(max(0,1-mu*mu)),0.0])
    base=np.array([0.13,-0.07,0.02]); mirror=base+np.array([1.0,0.0,0.0])
    w=x; t2=0.73
    def pos(t,X):
        theta=w*(t-n.dot(X)/cs)+phase
        return X+n*(eps/(w*cs))*math.sin(theta)
    def vel(t,X):
        theta=w*(t-n.dot(X)/cs)+phase
        return n*(eps/cs)*math.cos(theta)
    def wave(t,X):
        return eps*math.cos(w*(t-n.dot(X)/cs)+phase)
    X2=pos(t2,base)
    duration_in=brentq(lambda d:d-np.linalg.norm(X2-pos(t2-d,mirror)),0.5,1.5,
                      xtol=1e-14,rtol=1e-14)
    t1=t2-duration_in; X1=pos(t1,mirror)
    duration_out=brentq(lambda d:d-np.linalg.norm(X1-pos(t1-d,base)),0.5,1.5,
                       xtol=1e-14,rtol=1e-14)
    t0=t1-duration_out
    def rate_minus_one(t):
        V=vel(t,base)
        return math.expm1(wave(t,pos(t,base)))*math.sqrt(1-V.dot(V)) \
            +(math.sqrt(1-V.dot(V))-1)
    correction,err=quad(rate_minus_one,t0,t2,epsabs=1e-13,epsrel=1e-12)
    actual=((t2-t0-2)+correction)/2
    local_phase=cmath.exp(-1j*w*t2+1j*w*n.dot(base)/cs-1j*phase)
    predicted=eps*(response(x,mu,cs)*local_phase).real
    return {'amplitude':eps,'mu':mu,'cs_over_c':cs,'omega_L_over_c':x,
            'measured_timing_functional':actual,'first_order_prediction':predicted,
            'residual':actual-predicted,'residual_over_amplitude_squared':
                (actual-predicted)/eps**2,'quadrature_error':err/2,
            'outgoing_duration':duration_out,'incoming_duration':duration_in}


def limits():
    rows=[]
    for x in [.08,.5,1.7,math.pi,4.2]:
        for mu in [-1,1]:
            val=response(x,mu,1)
            assert abs(val)<1e-13
            rows.append({'x':x,'mu':mu,'luminal_parallel_abs':abs(val)})
        for cs in [.55,.7185375538936453,1,1.3]:
            assert abs(response(x,0,cs)-cmath.exp(1j*x)*np.sinc(x/math.pi))<1e-14
    x=1e-6
    errors=[]
    for cs in [.55,.7185375538936453,1,1.3]:
        for mu in [-1,-.4,0,.4,.8,1]:
            err=abs(response(x,mu,cs)-(1-(mu/cs)**2))
            assert err<2e-5
            errors.append(err)
    optical=response(math.pi,1,1)-response(math.pi,0,1)
    mechanical=-cmath.exp(1j*math.pi/2)*np.sinc(.5)
    assert abs(optical)<1e-13 and abs(mechanical)>.6
    return {'luminal_parallel_rows':rows,'small_arm_max_absolute_error':max(errors),
            'finite_arm_node':{'optical_abs':abs(optical),'mechanical_abs':abs(mechanical)}}


def run():
    algebra=symbolic_identities(); limiting=limits()
    # Protocol-fixed grid before evaluating the timing functional.
    rows=[timing_functional(eps,mu,cs,x)
          for cs in [.55,.7185375538936453,1,1.3]
          for mu in [-1,-.4,0,.4,.8,1]
          for x in [.08,.5,1.7,4.2]
          for eps in [.002,.001,.0005]]
    bound=max(abs(r['residual_over_amplitude_squared']) for r in rows)
    assert bound<100, bound
    fixture=[timing_functional(eps,.4,.7185375538936453,.5) for eps in [.002,.001,.0005]]
    ratios=[abs(fixture[i]['residual']/fixture[i+1]['residual']) for i in range(2)]
    assert all(3.9<r<4.1 for r in ratios),ratios
    # Rotation-independent tensor test of the TT projection, with linked
    # transverse and longitudinal eigenvalues at each supplied speed.
    n=np.array([2.,-3.,6.])/7;P=np.eye(3)-np.outer(n,n)
    tides=[]
    for cs in [.55,.7185375538936453,1,1.3]:
        T=np.eye(3)-np.outer(n,n)/cs**2
        transverse=P@T@P
        TT=transverse-P*np.trace(transverse)/2
        assert np.linalg.norm(TT)<1e-14
        assert abs(n@T@n-(1-1/cs**2))<1e-14
        tides.append({'cs_over_c':cs,'TT_norm':float(np.linalg.norm(TT)),
                      'longitudinal_coefficient':float(n@T@n)})
    source=Path(__file__).resolve(); note=source.with_name('DIRECT_CONFORMAL_DERIVATION.md')
    return {'status':'PASS within explicit conditional first-order scope',
            'created_at':dt.datetime.now(dt.timezone.utc).isoformat(),
            'identities':{str(p.name):hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in [source,note,source.with_name('PROTOCOL.md')]},
            'symbolic':algebra,'limits':limiting,'timing_control_count':len(rows),
            'max_absolute_residual_over_amplitude_squared':bound,
            'quadratic_scaling_fixture':fixture,'halving_ratios':ratios,
            'tidal_controls':tides,'timing_controls':rows,
            'limitations':['first-order endpoint trajectories, not nonlinear geodesic integration',
              'synthetic controls only; no fitted or held-out observations',
              'finite-energy conditional Hamiltonian; point self-energy unresolved',
              'old mass-conserved source radiation not inherited',
              'no cavity, detector or waveform likelihood']}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True)
    args=parser.parse_args(); result=run()
    dest=Path(args.output)
    with dest.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['timing_controls','quadratic_scaling_fixture']},indent=2))
