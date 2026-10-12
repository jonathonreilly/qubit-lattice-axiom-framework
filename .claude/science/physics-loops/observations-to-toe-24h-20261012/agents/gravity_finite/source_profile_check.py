#!/usr/bin/env python3
"""Independent mass-integral/hypergeometric source-kernel and SVD check."""
import os
for _name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ[_name]="1"
import hashlib
import json
from pathlib import Path
from datetime import datetime,timezone
import mpmath as mp

ROOT=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=ROOT/'gravity_measurements'/'finite'/'source_profile_results.json'
mp.mp.dps=110
R=mp.mpf('6371000')
RC=mp.mpf('.55')*R
FC=mp.mpf('.32')
FM=mp.mpf('.68')
RADII=[R,R+mp.mpf('710000'),2*R]
ELLS=[mp.mpf('1e7'),mp.mpf('1e9'),mp.mpf('1e11'),mp.mpf('1e13')]


def guard():
    assert not list(ROOT.glob('*STOP_REQUESTED*'))
    assert datetime.now(timezone.utc).timestamp()<json.loads((ROOT/'DEADLINE.json').read_text())['deadline_epoch']


def ball_form(mu,radius):
    # Angular/radial Yukawa average: 0F1(;5/2;(mu*radius)^2/4).
    return mp.hyp0f1(mp.mpf('2.5'),(mu*radius)**2/4)


def ball_kernel(ell,r,radius):
    # Integrate the gamma(s=1) mass distribution term-by-term, then resum.
    beta=1+r/ell
    z=(radius/(ell+r))**2
    return (mp.hyp2f1(mp.mpf('.5'),1,mp.mpf('2.5'),z)/beta
            +(r/ell)*mp.hyp2f1(1,mp.mpf('1.5'),mp.mpf('2.5'),z)/beta**2)


def kernels(ell,r):
    c=ball_kernel(ell,r,RC)
    outer=ball_kernel(ell,r,R)
    return c,(R**3*outer-RC**3*c)/(R**3-RC**3)


def direct_mass_kernel(ell,r,radius):
    def integrand(x):
        return mp.exp(-x*(1+r/ell))*(1+x*r/ell)*ball_form(x/ell,radius)
    return mp.quad(integrand,[0,1,4,12,40,mp.inf])


def stringify(x):
    if isinstance(x,mp.mpf):return mp.nstr(x,100)
    if isinstance(x,dict):return {k:stringify(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [stringify(v) for v in x]
    return x


def run():
    guard()
    rows=[]
    mean_c=mp.mpf(3)/5*RC**2
    mean_m=mp.mpf(3)/5*(R**5-RC**5)/(R**3-RC**3)
    for ell in ELLS:
        guard()
        values=[kernels(ell,r) for r in RADII]
        ratio=[c/m for c,m in values]
        assert ratio[0]<ratio[1]<ratio[2]
        inversions=[]
        for j in (1,2):
            matrix=mp.matrix([[FC*values[0][0],FM*values[0][1]],
                              [FC*values[j][0],FM*values[j][1]]])
            _,sv,_=mp.svd(matrix)
            condition=sv[0]/sv[1]
            determinant=mp.det(matrix)
            assert determinant<0
            asymptotic=(12*(FC**2+FM**2)*ell**4
                       /(FC*FM*1*2*5*(mean_m-mean_c)*(RADII[j]**2-RADII[0]**2)))
            inversions.append(dict(second_radius=RADII[j],matrix=list(matrix),
                determinant=determinant,singular_values=list(sv),condition_number_2=condition,
                long_range_asymptotic_condition=asymptotic,condition_over_asymptotic=condition/asymptotic))
        rows.append(dict(ell=ell,core_force=[v[0] for v in values],
                         mantle_force=[v[1] for v in values],ratios=ratio,inversion=inversions))
    direct=[]
    # Independent quadrature over mediator mass at a source surface and above it.
    with mp.workdps(75):
        for ell,r,radius in ((ELLS[0],RADII[0],R),(ELLS[0],RADII[1],RC),
                             (ELLS[1],RADII[2],R)):
            guard()
            integrated=direct_mass_kernel(ell,r,radius)
            closed=ball_kernel(ell,r,radius)
            assert abs(integrated-closed)<mp.mpf('1e-65')
            direct.append(dict(ell=ell,r=r,source_radius=radius,direct_mass_integral=integrated,
                               hypergeometric_value=closed,absolute_difference=abs(integrated-closed)))
    # Discrete covariance with a broad measure, and the single-pole control.
    masses=[mp.mpf('6e-8'),mp.mpf('1.7e-7')]
    weights=[mp.mpf('.4'),mp.mpf('.6')]
    r=mp.mpf('1.1')*R
    core=[ball_form(mu,RC) for mu in masses]
    mantle=[(R**3*ball_form(mu,R)-RC**3*ball_form(mu,RC))/(R**3-RC**3) for mu in masses]
    q=[c/m for c,m in zip(core,mantle)]
    h=[(1+mu*r)*mp.exp(-mu*r) for mu in masses]
    probability=[w*m*hh for w,m,hh in zip(weights,mantle,h)]
    total=sum(probability);probability=[v/total for v in probability]
    slope=[-r*mu**2/(1+r*mu) for mu in masses]
    covariance=sum(p*qq*g for p,qq,g in zip(probability,q,slope))-sum(p*qq for p,qq in zip(probability,q))*sum(p*g for p,g in zip(probability,slope))
    ratio_function=lambda rr:sum(w*c*(1+mu*rr)*mp.exp(-mu*rr) for w,c,mu in zip(weights,core,masses))/sum(w*m*(1+mu*rr)*mp.exp(-mu*rr) for w,m,mu in zip(weights,mantle,masses))
    derivative=mp.diff(ratio_function,r)
    assert covariance>0 and abs(covariance-derivative)<mp.mpf('1e-95')
    single_rows=[(core[0]*(1+masses[0]*rr)*mp.exp(-masses[0]*rr),
                  mantle[0]*(1+masses[0]*rr)*mp.exp(-masses[0]*rr)) for rr in RADII[:2]]
    single_det=mp.det(mp.matrix(single_rows))
    assert abs(single_det)<mp.mpf('1e-100')
    result=dict(generated_utc=datetime.now(timezone.utc).isoformat(),
        method='mass-space 0F1 form factors, independently resummed 2F1 kernels, direct SVD',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        mpmath_version=mp.__version__,main_precision_digits=mp.mp.dps,
        geometry=dict(R=R,RC=RC,f_core=FC,f_mantle=FM,radii=RADII),
        radial_second_moments=dict(core=mean_c,mantle=mean_m),rows=rows,
        direct_mass_integral_checks=direct,
        discrete_covariance=dict(masses=masses,weights=weights,radius=r,
                                  covariance=covariance,numerical_derivative=derivative,
                                  single_mass_determinant=single_det),
        parent_functions_imported=False)
    OUT.write_text(json.dumps(stringify(result),indent=2)+'\n')
    print(json.dumps(stringify(dict(output=str(OUT),
        first_pair_conditions=[r['inversion'][0]['condition_number_2'] for r in rows],
        direct_mass_max_difference=max(r['absolute_difference'] for r in direct))),indent=2))


if __name__=='__main__':run()
