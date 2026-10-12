#!/usr/bin/env python3
"""Shared scalar continuum: static response and vacuum coherence benchmarks.

Natural units hbar=c=1. a,d,T,ell share length units. nu has total weight 1.
This does not compute a real apparatus likelihood or a molecular fringe.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import quad
from scipy.special import beta, exp1, gamma


def one_minus_sinc(x):
    x = float(x)
    if abs(x) < 1e-3:
        return x*x/6 - x**4/120 + x**6/5040
    return 1-math.sin(x)/x


def static_potential_factor(s, ell, r):
    return (ell/(ell+r))**s


def static_force_factor(s, ell, r):
    return static_potential_factor(s,ell,r)*(1+s*r/(ell+r))


def local_spectrum(s, ell, omega, a=0., d=None):
    """Positive-frequency Wightman density j with W(t)=int_0^inf j(w)e^-iwt dw.

    Spatial difference uses |exp(ik.x1)-exp(ik.x2)|^2; it is not one local field.
    Change variable u=(mu/omega)^s removes the endpoint power singularity.
    """
    if omega <= 0:
        return 0.
    def f(u):
        t = u**(1/s)
        k = omega*math.sqrt(max(0.,1-t*t))
        diff = 1. if d is None else 2*one_minus_sinc(k*d)
        return math.sqrt(max(0.,1-t*t))*math.exp(-ell*omega*t-a*a*k*k)*diff
    integral = quad(f,0,1,epsabs=1e-13,epsrel=5e-11)[0]
    return ell**s*omega**(s+1)*integral/(4*math.pi**2*gamma(s)*s)


def local_leading(s, ell, omega, d=None):
    if d is None:
        return ell**s*omega**(s+1)*beta(s/2,1.5)/(8*math.pi**2*gamma(s))
    return ell**s*d*d*omega**(s+3)*beta(s/2,2.5)/(24*math.pi**2*gamma(s))


def spatial_decoherence_per_g2(mu, a, d, T):
    """Exponent / g^2 for one massive mode and top-hat hold, direct momentum integral."""
    q, distance, duration = mu*a,d/a,T/a
    def f(x):
        w=math.sqrt(x*x+q*q)
        if w == 0:
            return 0.
        return x*x*math.exp(-x*x)*one_minus_sinc(x*distance)*math.sin(.5*w*duration)**2/w**3
    return quad(f,0,10,epsabs=2e-11,epsrel=2e-9,limit=1000)[0]/math.pi**2


def spatial_saturation_per_g2(mu, a, d):
    q,distance=mu*a,d/a
    def f(x):
        w=math.sqrt(x*x+q*q)
        return 0. if w==0 else x*x*math.exp(-x*x)*one_minus_sinc(x*distance)/w**3
    return quad(f,0,10,epsabs=1e-12,epsrel=2e-11)[0]/(2*math.pi**2)


def spatial_uniform_bound_per_g2(a,d):
    """All mu>=0 and all T: use 1-sinc(x)<=min(x^2/6,2), omega>=k."""
    if d==0:
        return 0.
    ratio=d/a
    h=12/ratio**2
    return ((-math.expm1(-h))/h+exp1(h))/math.pi**2


def direct_static_quadrature(s,ell,r,force=False):
    # u=mu^(s) removes integrable mu^(s-1) singularity; compactify with mu=v/(1-v).
    # Numerical integration of the original mass density, not the closed Laplace formula.
    def f(v):
        if v <= 0 or v >= 1:
            return 0.
        y=v/(1-v)
        mu=y**(1/s)
        # dmu*mu^(s-1)=dy/s
        pref=ell**s/(s*gamma(s)*(1-v)**2)
        value=pref*math.exp(-(ell+r)*mu)
        return value*(1+mu*r) if force else value
    return quad(f,0,1,epsabs=1e-12,epsrel=1e-11,limit=300)[0]


def run():
    checks=[];spectra=[];deco=[]
    def check(name,condition,evidence):
        checks.append({"name":name,"pass":bool(condition),"evidence":evidence})
    for s in (.5,1.,2.):
        for r in (.1,1.,10.):
            for force in (False,True):
                numerical=direct_static_quadrature(s,1.,r,force)
                closed=(static_force_factor if force else static_potential_factor)(s,1.,r)
                check(f"mass quadrature s={s} r={r} force={force}",
                      abs(numerical/closed-1)<1e-9,
                      {"quadrature":numerical,"closed":closed})
        for difference in (False,True):
            d=.8 if difference else None
            values=[]
            for omega in (1e-2,1e-3,1e-4):
                direct=local_spectrum(s,1.,omega,a=.3,d=d)
                leading=local_leading(s,1.,omega,d=d)
                values.append({"omega":omega,"direct":direct,"leading":leading,
                               "ratio":direct/leading})
            spectra.append({"s":s,"spatial_difference":difference,"values":values})
            check(f"infrared leading coefficient s={s} difference={difference}",
                  abs(values[-1]['ratio']-1)<1e-4 and
                  abs(values[-1]['ratio']-1)<abs(values[0]['ratio']-1),values)
    bound=spatial_uniform_bound_per_g2(1.,3.)
    for mu in (0.,.3,3.):
        saturation=spatial_saturation_per_g2(mu,1.,3.)
        for T in (.1,1.,10.,100.):
            value=spatial_decoherence_per_g2(mu,1.,3.,T)
            deco.append({"mu_a":mu,"T_over_a":T,"Gamma_per_g2":value,
                         "saturation_per_g2":saturation,"uniform_bound_per_g2":bound})
            check(f"positive all-time bound mu={mu} T={T}",0<=value<=bound*(1+1e-10),value)
        check(f"long hold limit mu={mu}",
              abs(deco[-1]['Gamma_per_g2']-saturation)<2e-5,saturation)
    zero=spatial_decoherence_per_g2(.3,1.,0.,4.)
    check('zero separation',zero==0,zero)
    # Independent coherent-state derivation and oscillator/frequency integrals
    # check the normalization; no truncated Fock-basis evolution is claimed.
    return {"status":"conditional shared-response construction; no experimental fit",
            "spectra":spectra,"spatial_decoherence":deco,"checks":checks,
            "total_pass":sum(c['pass'] for c in checks),
            "total_fail":sum(not c['pass'] for c in checks),
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    result=run();body=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(body)
    print(body,end='');print(f"TOTAL: PASS={result['total_pass']} FAIL={result['total_fail']}")
    raise SystemExit(bool(result['total_fail']))
