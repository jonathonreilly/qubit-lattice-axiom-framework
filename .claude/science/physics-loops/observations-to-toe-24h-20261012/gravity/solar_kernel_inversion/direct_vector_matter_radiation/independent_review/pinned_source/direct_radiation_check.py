#!/usr/bin/env python3
"""Synthetic controls for the explicitly supplied matter/radiation extension."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,math,sys,time
import numpy as np
from scipy.optimize import brentq
import sympy as s

ROOT=Path(__file__).resolve().parent

def symbolic():
    N,D,G,m1,m2,a,z=s.symbols('N D G m1 m2 a z',positive=True)
    r=s.sqrt(a*a+z*z)
    U=-G*m1*m2*(N+D+(N-D)*z*z/r**2)/(2*r)
    reduced=m1*m2/(m1+m2)
    vertical=s.simplify(s.diff(U,z,2).subs(z,0)/reduced)
    assert s.simplify(vertical-G*(m1+m2)*(3*D-N)/(2*a**3))==0
    radial=s.simplify(s.diff(U,a).subs(z,0)/(reduced*a))
    assert s.simplify(radial-G*(N+D)*(m1+m2)/(2*a**3))==0
    x=s.symbols('x',real=True)
    integrals=[2*s.pi*s.integrate((1-x*x)**3,(x,-1,1)),
               2*s.pi*s.integrate(x*x*(1-x*x)**2,(x,-1,1))]
    assert integrals==[64*s.pi/35,32*s.pi/105]
    q=s.symbols('q',positive=True)
    ratio=(6*q**s.Rational(7,2)+1)/(21*(q+1))
    derivative=(15*q**s.Rational(7,2)+21*q**s.Rational(5,2)-1)/(21*(q+1)**2)
    assert s.simplify(s.diff(ratio,q)-derivative)==0
    assert ratio.subs(q,1)==s.Rational(1,6)
    return {'equatorial_frequency':str(radial),'vertical_frequency':str(vertical),
            'angular_integrals':[str(v) for v in integrals],
            'ratio':str(ratio),'ratio_derivative':str(derivative),
            'isotropic_ratio':'1/6'}

def angular_tensor_power(N,D,alpha,G,a,Omega,reduced):
    zz,weights=np.polynomial.legendre.leggauss(48)
    phis=np.arange(96)*2*np.pi/96
    # I''' evaluated directly from the rotating second-moment matrix at phase0.
    I3=np.array([[0,-4,0],[-4,0,0],[0,0,0]],dtype=float)*reduced*a*a*Omega**3
    cT,cL=1/math.sqrt(alpha*N),1/math.sqrt(alpha*D)
    totals=np.zeros(2)
    for z,w in zip(zz,weights):
        ns=np.column_stack([np.sqrt(1-z*z)*np.cos(phis),
                            np.sqrt(1-z*z)*np.sin(phis),np.full(len(phis),z)])
        contractions=np.einsum('ni,ij,nj->n',ns,I3,ns)
        prefactor=G/(16*np.pi*alpha)*w*2*np.pi/len(phis)
        totals += prefactor*np.sum(contractions**2)*np.array([(1-z*z)/cT**7,z*z/cL**7])
    expected=np.array([32/(35*cT**7),16/(105*cL**7)])*G*reduced**2*a**4*Omega**6/alpha
    assert np.allclose(totals,expected,rtol=2e-13,atol=0)
    return totals,expected

def exact_source_harmonics(N,D,alpha,G,a,Omega):
    """Full density Fourier coefficients of equal antipodal half-unit masses.

    No moment expansion or Bessel function is used. Total mass1, reduced mass1/4.
    Return finite-harmonic, independently integrated radiation (no near-zone fit).
    """
    zs,ws=np.polynomial.legendre.leggauss(48)
    phases=np.arange(512)*2*np.pi/512
    totals=np.zeros(2);tail=np.zeros(2);oddmax=0.
    for j,c in enumerate([1/math.sqrt(alpha*N),1/math.sqrt(alpha*D)]):
        polarization=(1-zs*zs) if j==0 else zs*zs
        for harmonic in range(1,17):
            omega=harmonic*Omega
            phase_argument=omega*a/(2*c)*np.sqrt(1-zs*zs)[:,None]*np.cos(phases)[None,:]
            density=np.cos(phase_argument)
            coefficient=np.mean(density*np.exp(1j*harmonic*phases)[None,:],axis=1)
            if harmonic%2:oddmax=max(oddmax,float(np.max(np.abs(coefficient))))
            power=G*omega**2/(alpha*c**3)*np.dot(ws,polarization*np.abs(coefficient)**2)
            totals[j]+=power
            if harmonic>=14:tail[j]+=power
    assert oddmax<1e-14
    return totals,tail,oddmax

def bracket():
    polynomial=lambda x:6*x**7-21*x*x-20
    root=brentq(polynomial,1,math.sqrt(3),xtol=1e-14)
    scale=10**12
    lo=F(math.floor(root*scale),scale);hi=lo+F(1,scale)
    assert polynomial(lo)<0<polynomial(hi)
    q=root*root
    return {'sqrt_q_bracket':[str(lo),str(hi)],'q_bracket':[str(lo*lo),str(hi*hi)],
            'q_approx':q,'transverse_to_longitudinal_speed':1/root,
            'polar_to_equatorial_static_potential':2*q/(q+1),
            'vertical_squared_frequency_to_orbital':(3-q)/(1+q),
            'scope':'Exact polynomial sign bracket; equality to a supplied GR comparator with c_L=c_EM, not a measurement fit.'}

def main():
    start=time.monotonic();rows=[];mutations=[]
    for q in [1.,1.5,2.,5.]:
        N,D,alpha,G,Omega,reduced=q,1.,1.,1.,1.,.25
        cT=1/math.sqrt(q)
        for speed_fraction in [.08,.04,.02,.01]:
            a=speed_fraction*cT
            quadrature,leading=angular_tensor_power(N,D,alpha,G,a,Omega,reduced)
            direct,tail,odd=exact_source_harmonics(N,D,alpha,G,a,Omega)
            relative=float(np.sum(direct)/np.sum(leading)-1)
            assert abs(relative)<2*speed_fraction**2
            assert float(np.sum(tail)/np.sum(direct))<1e-14
            rows.append({'q':q,'a_Omega_over_cT':speed_fraction,
                         'angular_tensor_power':quadrature.tolist(),'leading_power':leading.tolist(),
                         'exact_source_harmonic_power':direct.tolist(),'relative_to_leading_minus_one':relative,
                         'harmonics_14_to_16_fraction':float(np.sum(tail)/np.sum(direct)),
                         'max_odd_density_coefficient':odd,
                         'equatorial_orbit_vertically_stable':q<3})
        local=[r for r in rows if r['q']==q]
        for r1,r2 in zip(local[:-1],local[1:]):
            convergence=abs(r1['relative_to_leading_minus_one']/r2['relative_to_leading_minus_one'])
            assert 3.9<convergence<4.1
    # Corrupt only one side of independent angular/multipole comparisons.
    actual,expected=angular_tensor_power(2.,1.,1.,1.,.03,1.,.25)
    mutations=[{'name':'omit_source_Taylor_half','detected':not np.allclose(actual,4*expected,rtol=1e-8,atol=0)},
               {'name':'drop_longitudinal_power','detected':not math.isclose(sum(actual),expected[0],rel_tol=1e-8)},
               {'name':'replace_cT_power7_by5','detected':not math.isclose(actual[0],expected[0]/2,rel_tol=1e-8)}]
    assert all(row['detected'] for row in mutations)
    output={'source_sha256':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in
              ['PROTOCOL.md','DIRECT_MATTER_RADIATION.md','SOURCE_LEDGER.md',Path(__file__).name]},
            'symbolic':symbolic(),'controls':rows,'calibration_example':bracket(),'mutations':mutations,
            'elapsed_sec':time.monotonic()-start,
            'scope':'Leading weak-source circular radiation and conservative mechanics only; no empirical test or relativistic matter model.'}
    out=ROOT/'evidence_v1';out.mkdir(exist_ok=True)
    with (out/'RESULTS.json').open('x') as f:json.dump(output,f,indent=2);f.write('\n')
    print(json.dumps({'symbolic':output['symbolic'],'calibration_example':output['calibration_example'],
                     'control_count':len(rows),'max_abs_relative_error':max(abs(r['relative_to_leading_minus_one']) for r in rows),
                     'mutations':mutations,'elapsed_sec':output['elapsed_sec']},indent=2))

if __name__=='__main__':main()
