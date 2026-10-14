#!/usr/bin/env python3
"""Fixed positive-mediator construction checks, with independent kernel paths."""
import os
for _thread_name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[_thread_name]='1'

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'scripts/data/positive_mediator_inverse_2026_10_12.json',
    'docs/POSITIVE_MEDIATOR_FORCE_NOISE_AND_SOURCE_INVERSION_BOUNDED_THEOREM_NOTE_2026-10-12.md',
)

import json
import math
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal
from scipy.special import gamma, gammainc, gammaincc, gammaln, roots_genlaguerre
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
COUNTS=[0,0]


def check(name,condition,detail=''):
    passed=bool(condition)
    COUNTS[0 if passed else 1]+=1
    print(f"{'PASS' if passed else 'FAIL'} {name}"+(f': {detail}' if detail else ''))


def gauss(shape,order):
    nodes,raw=roots_genlaguerre(order,shape-1)
    return nodes,raw/gamma(shape)


def potential(nodes,weights,radius):
    return float(np.dot(weights,np.exp(-nodes*radius)))


def force(nodes,weights,radius):
    return float(np.dot(weights,(1+nodes*radius)*np.exp(-nodes*radius)))


def atomic_noise(omega,nodes,weights,width):
    k=np.sqrt(np.maximum(omega*omega-nodes*nodes,0))
    return float(np.dot(weights,k*np.exp(-width*width*k*k)))/(4*math.pi**2)


def continuum_noise(omega,shape,width):
    integral,error=quad(lambda u:u**(shape-1)*math.exp(-omega*u)
        *math.sqrt(max(0,1-u*u))*math.exp(-width*width*omega*omega*(1-u*u)),
        0,1,epsabs=2e-12,epsrel=2e-11)
    return omega**(shape+1)*integral/(4*math.pi**2*gamma(shape)),error


def bounds(shape,order,radius):
    b=math.exp(2*order*math.log(radius)+gammaln(order+1)+gammaln(order+shape)
               -gammaln(2*order+1)-gammaln(shape))
    return b,(2*order-1)*b


def positive_bins(shape,count,cap):
    edges=np.linspace(0,cap,count+1)
    tail=gammaincc(shape,cap)
    means=(edges[:-1]+edges[1:])/2
    tail_mean=shape*gammaincc(shape+1,cap)/tail
    return np.r_[means,tail_mean],np.r_[np.diff(gammainc(shape,edges)),tail]


def ball_mass_form(mu,radius):
    return mp.hyp0f1(mp.mpf('2.5'),(mu*radius)**2/4)


def ball_mass_kernel(ell,r,radius):
    beta=1+r/ell;z=(radius/(ell+r))**2
    return (mp.hyp2f1(mp.mpf('.5'),1,mp.mpf('2.5'),z)/beta
            +(r/ell)*mp.hyp2f1(1,mp.mpf('1.5'),mp.mpf('2.5'),z)/beta**2)


def shell_kernel(ell,r,u):
    v=u/(ell+r)
    removable=mp.atanh(v)/v if v else mp.mpf(1)
    return ell/(ell+r)*(removable+(r/(ell+r))/(1-v*v))


def ball_radial_kernel(ell,r,radius):
    # An independent integral over physical radius, not the mass-space formula.
    return mp.quad(lambda y:3*y*y*shell_kernel(ell,r,radius*y),[0,mp.mpf('.5'),1])


def source_kernels(ell,r,R,RC):
    core=ball_mass_kernel(ell,r,RC)
    mantle=(R**3*ball_mass_kernel(ell,r,R)-RC**3*core)/(R**3-RC**3)
    return core,mantle


def field_checks():
    s=1.7;n=5;ell=1.3
    d=2*np.arange(n)+s;e=-np.sqrt(np.arange(1,n)*(np.arange(n-1)+s))
    J=np.diag(d)+np.diag(e,1)+np.diag(e,-1)
    x,w=gauss(s,n)
    ev,u=eigh_tridiagonal(d,e)
    check('local_action_positive_measure',min(x)>0 and min(w)>0
          and abs(sum(w)-1)<1e-14 and np.max(abs(x-ev))<1e-13
          and np.max(abs(w-u[0]**2))<2e-14)
    z=.31-(.71+.17j)**2
    direct=np.linalg.inv((J@J)/ell**2+z*np.eye(n))[0,0]
    spectral=sum(w/(x*x/ell**2+z))
    check('local_action_resolvent',abs(direct-spectral)<2e-13,
          f'complex matrix/spectral difference={abs(direct-spectral):.3g}')


def quadrature_checks(c):
    conditions=[];worst=0.
    for s in c['s_grid']:
        for n in c['orders']:
            nodes,weights=gauss(s,n)
            conditions.append(min(nodes)>0 and min(weights)>0 and abs(sum(weights)-1)<3e-14)
            # Polynomial moments have an independently known gamma integral.
            for power in range(min(2*n,8)):
                exact=gamma(s+power)/gamma(s)
                conditions.append(abs(np.dot(weights,nodes**power)/exact-1)<3e-13)
            for r in c['radii_dimensionless']:
                y=(1+r)**(-s);h=y*(1+s*r/(1+r))
                by,bh=bounds(s,n,r)
                ey=y-potential(nodes,weights,r);eh=h-force(nodes,weights,r)
                conditions.extend([-3e-14<=ey<=by+3e-14,abs(eh)<=bh+3e-14])
                worst=max(worst,abs(ey))
    check('laguerre_moments_and_static_bounds',all(conditions),
          f'{len(conditions)} predicates, largest sampled potential error={worst:.9g}; rounding slack=3e-14')


def noise_checks(c):
    # Frequency integral of (3) versus the original one-mass equal-time Wightman integral.
    mu=.7;a=.6
    spectral,qe=quad(lambda w:atomic_noise(w,np.array([mu]),np.array([1.]),a),
                     mu,np.inf,epsabs=1e-13,epsrel=2e-12)
    momentum,qk=quad(lambda k:k*k*math.exp(-a*a*k*k)/(4*math.pi**2*math.hypot(k,mu)),
                     0,np.inf,epsabs=1e-13,epsrel=2e-12)
    check('noise_normalization',abs(spectral-momentum)<2e-12,
          f'equal-time frequency/momentum discrepancy={abs(spectral-momentum):.3g}')
    nodes,w=gauss(1.,8)
    y=potential(nodes,w,1.)
    j,err=continuum_noise(.1,1.,c['gaussian_width'])
    jn=atomic_noise(.1,nodes,w,c['gaussian_width'])
    check('explicit_response_pair',abs(.5-y)<1e-7 and j>1e-4 and jn==0,
          f'N=8 Y(1)={y:.15g}, gap={nodes[0]:.12g}, j(.1)={j:.12g}, jN(.1)={jn:.1f}')


def bin_checks(c):
    conditions=[];max_noise_error=0.
    R=c['radius_window'];Omega=c['frequency_window'];M=c['bin_cap'];a=c['gaussian_width']
    assert Omega<=M and max(c['frequencies_dimensionless'])<=Omega
    assert max(c['radii_dimensionless'])<=R
    for s in c['s_grid']:
        for n in c['bin_counts']:
            nodes,w=positive_bins(s,n,M);h=M/n;tail=w[-1]
            conditions.extend([min(w)>0,abs(sum(w)-1)<3e-14,nodes[-1]>M])
            for r in c['radii_dimensionless']:
                y=(1+r)**(-s);f=y*(1+s*r/(1+r))
                conditions.extend([abs(y-potential(nodes,w,r))<=R*h/2+tail,
                                   abs(f-force(nodes,w,r))<=R*h/(2*math.e)+tail])
            for omega in c['frequencies_dimensionless']:
                exact,error=continuum_noise(omega,s,a)
                difference=abs(exact-atomic_noise(omega,nodes,w,a))
                max_noise_error=max(max_noise_error,difference)
                conditions.append(difference<=math.sqrt(Omega*h)/(4*math.pi**2))
    check('positive_bins_joint_bounds',all(conditions),
          f'{len(conditions)} predicates, largest sampled noise error={max_noise_error:.6g}')


def source_checks(c):
    mp.mp.dps=90
    g=c['source_geometry']
    if g['shape'] != 1:
        raise ValueError('The source-geometry kernel in this runner is explicitly restricted to s=1.')
    R=mp.mpf(g['radius_m']);RC=R*mp.mpf(g['core_radius_fraction'])
    fc=mp.mpf(g['core_mass_fraction']);fm=mp.mpf(g['mantle_mass_fraction'])
    r1=R;r2=R+mp.mpf(g['height_m'])
    rows=[];kernel_errors=[];inverse_errors=[]
    da2=mp.mpf(3)/5*((R**5-RC**5)/(R**3-RC**3)-RC**2)
    for ell_text in g['ell_m']:
        ell=mp.mpf(ell_text)
        vals=[source_kernels(ell,r,R,RC) for r in (r1,r2)]
        for r in (r1,r2):
            for radius in (RC,R):
                kernel_errors.append(abs(ball_mass_kernel(ell,r,radius)-ball_radial_kernel(ell,r,radius)))
        matrix=mp.matrix([[fc*x,fm*y] for x,y in vals])
        determinant=mp.det(matrix);_,sv,_=mp.svd(matrix);condition=sv[0]/sv[1]
        target=mp.matrix([mp.mpf('.25'),mp.mpf('-.6')]);observed=matrix*target
        d=vals[0][0]*vals[1][1]-vals[1][0]*vals[0][1]
        inverse=mp.matrix([(observed[0]*vals[1][1]-observed[1]*vals[0][1])/(fc*d),
                           (vals[0][0]*observed[1]-vals[1][0]*observed[0])/(fm*d)])
        inverse_errors.append(mp.norm(inverse-target))
        asym=12*(fc*fc+fm*fm)*ell**4/(fc*fm*1*2*5*da2*(r2*r2-r1*r1))
        rows.append((ell,determinant,condition,condition/asym))
    check('source_kernel_independent_paths',max(kernel_errors)<mp.mpf('1e-70'),
          f'max radial/mass formula discrepancy={mp.nstr(max(kernel_errors),6)}')
    check('source_inverse',max(inverse_errors)<mp.mpf('1e-55') and all(row[1]<0 for row in rows),
          f'max reconstructed charge error={mp.nstr(max(inverse_errors),6)}')
    check('source_conditioning',abs(rows[-1][3]-1)<mp.mpf('5e-6')
          and all(rows[i][2]<rows[i+1][2] for i in range(len(rows)-1)),
          'ell, weighted determinant, kappa2, kappa/asymptotic = '+
          json.dumps([[mp.nstr(x,14) for x in row] for row in rows]))
    # A separate finite positive spectral measure checks the covariance sign, not gamma fitting.
    masses=[mp.mpf(0),mp.mpf('6e-8'),mp.mpf('1.7e-7')]
    weights=[mp.mpf('.2'),mp.mpf('.3'),mp.mpf('.5')]
    core=[ball_mass_form(mu,RC) for mu in masses]
    mantle=[(R**3*ball_mass_form(mu,R)-RC**3*cc)/(R**3-RC**3) for mu,cc in zip(masses,core)]
    r=mp.mpf('1.2')*R;q=[cc/mm for cc,mm in zip(core,mantle)]
    un=[ww*mm*(1+mu*r)*mp.exp(-mu*r) for ww,mm,mu in zip(weights,mantle,masses)]
    pp=[v/sum(un) for v in un];ss=[-r*mu*mu/(1+r*mu) for mu in masses]
    cov=sum(p*x*y for p,x,y in zip(pp,q,ss))-sum(p*x for p,x in zip(pp,q))*sum(p*y for p,y in zip(pp,ss))
    def ratio(rr):
        h=[(1+mu*rr)*mp.exp(-mu*rr) for mu in masses]
        return sum(w*x*z for w,x,z in zip(weights,core,h))/sum(w*x*z for w,x,z in zip(weights,mantle,h))
    derivative=mp.diff(ratio,r)
    mu=masses[1]
    single=mp.matrix([[core[1]*(1+mu*rr)*mp.exp(-mu*rr),mantle[1]*(1+mu*rr)*mp.exp(-mu*rr)] for rr in (r1,r2)])
    check('source_covariance_and_single_mass_control',cov>0 and abs(cov-derivative)<mp.mpf('1e-80')
          and abs(mp.det(single))<mp.mpf('1e-80'),
          f'covariance={mp.nstr(cov,14)}, derivative difference={mp.nstr(abs(cov-derivative),6)}')


def main():
    c=json.loads((ROOT/AUDIT_INPUT_PATHS[0]).read_text())
    for name in AUDIT_INPUT_PATHS:
        assert (ROOT/name).is_file(),name
    print(f'python={platform.python_version()} numpy={np.__version__} scipy={scipy.__version__} mpmath={mp.__version__}')
    print('Scope: fixed synthetic diagnostics of a conditional positive-mediator construction; no empirical fit.')
    field_checks();quadrature_checks(c);noise_checks(c);bin_checks(c);source_checks(c)
    print(f'TOTAL: PASS={COUNTS[0]} FAIL={COUNTS[1]}')
    return bool(COUNTS[1])


if __name__=='__main__':
    raise SystemExit(main())
