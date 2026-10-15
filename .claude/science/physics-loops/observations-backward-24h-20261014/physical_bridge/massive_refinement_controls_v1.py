#!/usr/local/bin/python3
"""Focused checks of the sharpened mass bound and spatial interference."""
from pathlib import Path
import hashlib
import json
import numpy as np
import sympy as sp
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent
checks=[]


def check(name,value,**details):
    checks.append({'name':name,'passed':bool(value),**details})
    if not value:
        raise AssertionError(name+': '+repr(details))


def bound(mu,C,D,E,V):
    return (C*np.sqrt((2-np.pi/2)*mu)+D*np.sqrt((np.pi/2-4/3)*mu**3)
            +2*mu*np.sqrt(E*V))/(np.sqrt(2)*np.pi)


def chat(omega,T):
    def psi(x):
        z=x*T/np.pi
        return T*(np.sinc(z)+.5*np.sinc(z+1)+.5*np.sinc(z-1))
    return -.5*omega*(psi(omega+1)-psi(omega-1))


def clock_gram(mu,T,cutoff=12,order=32):
    # Resolve the width 1/T spectrum with cells <=1/(2T).
    cells=int(np.ceil(cutoff*2*T))
    gn,gw=leggauss(order)
    left=np.linspace(0,cutoff,cells+1)[:-1,None]
    om=left+cutoff/cells*(gn+1)/2
    v=np.sqrt(np.maximum(0,1-(mu/om)**2))
    spatial=3*v+6*np.sin(np.pi*v*om)/(np.pi*om)
    vals=chat(om,T)**2*spatial/(2*np.pi**2)
    return float(np.sum(vals*gw[None,:])*cutoff/(2*cells))


def run():
    z=sp.symbols('z',real=True)
    i1=sp.integrate(2*z*z/(1+z*z),(z,0,1))
    i2=sp.integrate((1-z*z)**2/(2*(1+z*z)),(z,0,1))
    check('first_radial_constant_exact',sp.simplify(i1-(2-sp.pi/2))==0,expression=str(i1))
    check('second_radial_constant_exact',sp.simplify(i2-(sp.pi/2-sp.Rational(4,3)))==0,expression=str(i2))
    k,mu=sp.symbols('k mu',positive=True)
    om=sp.sqrt(k*k+mu*mu)
    # Algebraic identity is sufficient for k Delta<=mu^2/2.
    check('phase_difference_identity',sp.simplify((om-k)*(om+k)-mu**2)==0)
    numerical=[]
    for mass in [.01,.3,2.]:
        a=quad(lambda t: (1-t/np.hypot(t,mass))**2,0,np.inf,epsabs=1e-11)[0]
        b=quad(lambda t: t*t*(mass*mass/(np.hypot(t,mass)*(np.hypot(t,mass)+t)))**2,0,np.inf,epsabs=1e-11)[0]
        numerical.append([a/(mass*(2-np.pi/2)),b/(mass**3*(np.pi/2-4/3))])
    check('radial_integrals_direct_quadrature',np.max(abs(np.array(numerical)-1))<3e-9,ratios=numerical)

    seq=[{'mu':m,'zero_offset_bound':bound(m,0,20.8,8.4,16),
          'nonzero_offset_bound':bound(m,4,12.4,8.4,16)} for m in [.01,.001,.0001,.00001]]
    limits=[row['zero_offset_bound']/row['mu'] for row in seq]
    check('zero_offset_linear_rate',all(a>b for a,b in zip(limits[:-1],limits[1:])),sequence=seq)
    expected=2*np.sqrt(8.4*16)/(np.sqrt(2)*np.pi)
    check('zero_offset_leading_coefficient',abs(limits[-1]-expected)<.01,leading=expected,last=limits[-1])

    # A compact derivative has zero clock integral. Independently integrate c.
    T=20*np.pi
    zero_integral=quad(lambda t: -np.pi/(2*T)*np.sin(np.pi*t/T)*np.sin(t)
                       +np.cos(np.pi*t/(2*T))**2*np.cos(t),-T,T,epsabs=1e-10,limit=400)[0]
    check('compact_clock_exact_endpoint_and_numeric_moment',abs(zero_integral)<1e-10,numerical_integral=zero_integral,
          analytic_reason='c is derivative of cos^2(pi t/(2T))*sin(t); primitive vanishes at both endpoints')
    maxfourier=0.
    for freq in [.2,.8,1.,1.2,2.]:
        direct=quad(lambda t: (-np.pi/(2*T)*np.sin(np.pi*t/T)*np.sin(t)
                    +np.cos(np.pi*t/(2*T))**2*np.cos(t))*np.cos(freq*t),-T,T,epsabs=1e-10,limit=400)[0]
        maxfourier=max(maxfourier,abs(direct-chat(freq,T)))
    check('compact_clock_fourier_formula',maxfourier<2e-10,maximum_error=maxfourier)

    # Direct 3D spatial-direction integration, independent of pair distances.
    points=np.array([[0.,0.,0.],[np.pi,0.,0.],[np.pi/2,np.sqrt(3)*np.pi/2,0.]])
    zn,zw=leggauss(80)
    az=2*np.pi*np.arange(160)/160
    directions=np.stack(np.broadcast_arrays(np.sqrt(1-zn[:,None]**2)*np.cos(az),
                         np.sqrt(1-zn[:,None]**2)*np.sin(az),zn[:,None]),axis=-1)
    v=2/3
    fields=np.exp(-1j*v*np.einsum('...d,ad->...a',directions,points)).sum(axis=-1)
    angular=float(np.sum(zw[:,None]*abs(fields)**2)/(2*len(az)))
    direct_factor=v*angular
    exact_factor=2+3*np.sqrt(3)/np.pi
    check('triangle_spatial_interference',abs(direct_factor-exact_factor)<2e-12,
          direct=direct_factor,exact=exact_factor,ratio=exact_factor/3)

    masses=[0.,np.sqrt(5)/3]
    comparisons=[]
    for T in [10*np.pi,20*np.pi,40*np.pi]:
        low=[clock_gram(m,T,12,24) for m in masses]
        high=[clock_gram(m,T,12,32) for m in masses]
        ratio=high[1]/high[0]
        convergence=float(np.max(abs(np.array(low)-high)))
        # A rigorous tail bound from |c_hat| <= ||c'||_1/omega is weak but finite.
        # Stronger L2 Parseval tail: integral_K^inf |c_hat|^2 <= pi||c'||_2^2/K^2.
        # Conservative derivative bound ||c'||2 <= sqrt(2T)*(1+pi/T+pi^2/(2T^2)).
        derivative_bound=2*T*(1+np.pi/T+np.pi**2/(2*T*T))**2
        tail=9*derivative_bound/(2*np.pi*12**2)
        check('finite_triangle_mass_reversal_T_'+str(T),ratio>1.15 and convergence<1e-6,
              ratio=ratio,finite_grams=high,quadrature_difference=convergence,
              analytic_each_tail_bound=tail,classification='finite quadrature diagnostic; compact-smooth existence proved separately')
        comparisons.append({'T':T,'mass':masses[1],'finite_grams':high,'ratio':ratio,
                            'cutoff':12,'quadrature_difference':convergence,'analytic_tail_bound':tail})
    check('narrowband_limit_approach',abs(comparisons[-1]['ratio']-(2/3+np.sqrt(3)/np.pi))<.002,
          limit=2/3+np.sqrt(3)/np.pi,actual=comparisons[-1]['ratio'])
    result={'checks':checks,'checks_passed':len(checks),'status':'working mathematical controls, no empirical test',
            'author_source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'working_note_sha256':hashlib.sha256((HERE/'MASSIVE_REFINEMENT_WORKING_v1.md').read_bytes()).hexdigest(),
            'compact_triangle_diagnostics':comparisons,'zero_offset_bounds':seq,
            'scope':'Flat KG prescribed response only. No action/state/mass/error/energy selection. Triangle counterexample is not the two-body coherent fixture.'}
    (HERE/'MASSIVE_REFINEMENT_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'checks_passed':len(checks),'source_sha256':result['author_source_sha256'],
                      'triangle_ratios':[x['ratio'] for x in comparisons],'zero_offset_bounds':seq}))


if __name__=='__main__':
    run()
