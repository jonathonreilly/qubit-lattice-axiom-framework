#!/usr/bin/env python3
"""Finite controls of supplied lattice thresholds and leading tree rates.

The analytic note, not finite optimization, carries global quantifiers.
No event likelihood, detector simulation, or empirical exclusion is computed.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    'docs/PHOTON_ELECTRON_LATTICE_THRESHOLD_AND_RATE_BOUNDED_THEOREM_NOTE_2026-10-12.md',
    'data/photon_electron_inverse_2026_10_12/observations.json',
)

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.optimize import brentq, differential_evolution, minimize_scalar

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / 'outputs/photon_electron_inverse_2026_10_12/results.json'
MUTATION = ''


def photon(k):
    return 2*np.linalg.norm(np.sin(np.asarray(k)/2))


def electron(p, mu):
    return math.sqrt(mu*mu+np.sin(p)@np.sin(p))


def threshold(k):
    """Rationalized z-variational expression; stable at small momentum."""
    k=np.asarray(k)
    w=2*np.sin(k/2)**2
    c=1-w
    b=np.sin(k)
    def rz(z):
        d=np.sqrt(1-z*b*b)
        return z*(1-z)*np.sum(w*b*b/(2*(d+c)*(1+d)))
    fit=minimize_scalar(lambda z:-rz(z),bounds=(0,1),method='bounded',
                        options={'xatol':1e-13})
    assert fit.success
    value=rz(fit.x)
    if MUTATION=='threshold_factor': value*=2
    q=.5*np.arctan(math.sqrt(1-fit.x)*np.tan(k))
    return float(value),float(fit.x),k/2+q


def threshold_controls():
    rng=np.random.default_rng(20261012)
    rows=[]
    cases=[np.array(x,dtype=float) for x in [(1.,0,0),(.7,.7,0),(.4,.4,.4),(.8,-.5,.2)]]
    cases += [rng.uniform(-1.3,1.3,3) for _ in range(8)]
    for i,k in enumerate(cases):
        r,z,pstar=threshold(k)
        omega=photon(k)
        residual=electron(pstar,math.sqrt(r))+electron(k-pstar,math.sqrt(r))-omega
        assert abs(residual)<2e-9,(k,residual)
        direct=[]
        for factor in [.8,1.2]:
            mu=math.sqrt(r)*factor
            sol=differential_evolution(lambda p:electron(p,mu)+electron(k-p,mu),
                 [(-math.pi,math.pi)]*3,seed=100+i,popsize=12,maxiter=700,
                 tol=1e-10,polish=True)
            assert sol.success
            gap=sol.fun-omega
            assert (gap<0)==(factor<1),(k,factor,gap)
            direct.append(gap)
        symmetric=2*electron(k/2,math.sqrt(r))-omega
        assert symmetric>0
        # All eight momentum corners preserve the independent energy sum.
        shift_error=max(abs(electron(pstar+np.array(t)*math.pi,math.sqrt(r))+
                            electron(k-pstar-np.array(t)*math.pi,math.sqrt(r))-omega)
                        for t in itertools.product([0,1],repeat=3))
        assert shift_error<2e-9
        rows.append({'k':k.tolist(),'R':r,'z':z,'threshold_residual':residual,
                     'direct_pair_gaps':direct,'symmetric_gap':symmetric,
                     'corner_residual':shift_error})
    return rows


def angular_controls():
    rng=np.random.default_rng(312)
    rows=[]
    for s in [.005,.05,.2,.49]:
        lower=s*s/(4*(3-s)); upper=s*s/(4*(1-s))
        if MUTATION=='angular_order': lower,upper=upper,lower
        for v in [np.array([s,0,0]),np.full(3,s/3)]+list(rng.dirichlet([1,1,1],12)*s):
            k=2*np.arcsin(np.sqrt(v)); r,z,_=threshold(k)
            assert lower-1e-13<=r<=upper+1e-13
            eps=max(abs(k)); q4=np.sum(k**4)
            assert q4/64*(1-eps*eps/12)**2-1e-13<=r<=q4/(64*math.cos(eps))+1e-13
            rows.append({'S':s,'v':v.tolist(),'R':r,'lower':lower,'upper':upper})
    return rows


PAULI=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1])]
ALPHA=[np.block([[np.zeros((2,2)),s],[s,np.zeros((2,2))]]) for s in PAULI]
BETA=np.diag([1,1,-1,-1])


def hamiltonian(p,mu):
    return mu*BETA+sum(a*s for a,s in zip(ALPHA,np.sin(p)))


def spin_formula(p,k,mu,eps):
    sp=np.sin(p); sq=np.sin(k-p)
    phase=p+k/2 if MUTATION=='vertex_phase' else p-k/2
    a=eps*np.cos(phase)
    ep,eq=electron(p,mu),electron(k-p,mu)
    return float(a@a*(1+(mu*mu-sp@sq)/(ep*eq))+2*(sp@a)*(sq@a)/(ep*eq))


def spin_controls():
    rng=np.random.default_rng(7721)
    errors=[]
    for _ in range(50):
        p=rng.uniform(-math.pi,math.pi,3); k=rng.uniform(-1.2,1.2,3)
        eps=rng.normal(size=3); eps/=np.linalg.norm(eps)
        mu=rng.uniform(.05,.7)
        v=sum(a*x for a,x in zip(ALPHA,eps*np.cos(p-k/2)))
        pp=(np.eye(4)+hamiltonian(p,mu)/electron(p,mu))/2
        pm=(np.eye(4)-hamiltonian(p-k,mu)/electron(k-p,mu))/2
        direct=np.trace(pp@v@pm@v).real
        closed=spin_formula(p,k,mu,eps)
        error=abs(closed-direct)
        assert error<3e-14
        a=eps*np.cos(p-k/2)
        assert closed+1e-14>=2*mu*mu*(a@a)/(electron(p,mu)*electron(k-p,mu))
        ward=sum(a*x for a,x in zip(ALPHA,2*np.sin(k/2)*np.cos(p-k/2)))
        assert np.max(abs(ward-(hamiltonian(p,mu)-hamiltonian(p-k,mu))))<2e-14
        for t in itertools.product([0,1],repeat=3):
            assert abs(spin_formula(p+np.array(t)*math.pi,k,mu,eps)-closed)<3e-14
        errors.append(error)
    return {'cases':len(errors),'max_trace_error':max(errors)}


def scaling_I(chi):
    d=math.sqrt(1-1/chi)
    tlo,thi=math.sqrt((1-d)/2),math.sqrt((1+d)/2)
    def primitive(t):return t**3/6+t**5/10+t/(8*chi)
    return 16*chi*(primitive(thi)-primitive(tlo))


def exact_axis_rate(r,mu,nx=64,nphi=24):
    """Central pi-cell coarea quadrature, gamma/alpha, near the tested shell."""
    omega=2*math.sin(r/2)
    def deficit(x):
        return omega-math.hypot(mu,math.sin(x*r))-math.hypot(mu,math.sin((1-x)*r))
    c=math.cos(r); u=(1+3*c)/(4*(1+c))
    xstar=.5-math.atan(math.sqrt(u)*math.tan(r))/(2*r)
    assert deficit(0)<0 and deficit(xstar)>0 and deficit(.5)<0
    roots=[brentq(deficit,0,xstar,xtol=1e-14),brentq(deficit,xstar,.5,xtol=1e-14)]
    intervals=[roots,[1-roots[1],1-roots[0]]]
    nodes,weights=leggauss(nx)
    total=0.; residual=0.
    for x0,x1 in intervals:
        for x,w in zip((nodes+1)*(x1-x0)/2+x0,weights*(x1-x0)/2):
            a=mu*mu+math.sin(x*r)**2; b=mu*mu+math.sin((1-x)*r)**2
            t=((omega-math.sqrt(a)-math.sqrt(b))*(omega+math.sqrt(a)+math.sqrt(b))
                *(omega-math.sqrt(a)+math.sqrt(b))*(omega+math.sqrt(a)-math.sqrt(b))
                /(4*omega*omega))
            assert t>0
            ep,eq=math.sqrt(a+t),math.sqrt(b+t)
            angular=0.
            for phi in (np.arange(nphi)+.5)*(2*math.pi/nphi):
                ty,tz=math.cos(phi),math.sin(phi)
                rho=brentq(lambda y:math.sin(y*ty)**2+math.sin(y*tz)**2-t,
                           0,2*math.sqrt(t),xtol=1e-16)
                sy,sz=math.sin(rho*ty),math.sin(rho*tz)
                cy,cz=math.cos(rho*ty),math.cos(rho*tz)
                derivative=(1/ep+1/eq)*(ty*sy*cy+tz*sz*cz)
                p=np.array([x*r,rho*ty,rho*tz]); k=np.array([r,0,0])
                spin=(spin_formula(p,k,mu,np.array([0,1,0]))+
                      spin_formula(p,k,mu,np.array([0,0,1])))/2
                assert spin>0
                angular+=rho/derivative*spin*(2*math.pi/nphi)
                residual=max(residual,abs(ep+eq-omega))
            total+=w*angular
    coefficient=r*total/(2*math.pi*omega)
    if MUTATION=='rate_normalization': coefficient*=2
    return coefficient,residual


def rate_controls():
    rows=[]
    for chi in [1.05,1.5,3.,10.]:
        ratios=[]
        for r in [.08,.04,.02]:
            mu=r*r/(8*math.sqrt(chi)); exact,err=exact_axis_rate(r,mu)
            target=mu*mu/(2*r)*scaling_I(chi); ratio=exact/target
            ratios.append(ratio)
            assert abs(ratio-1)<.02
            rows.append({'kind':'fixed_chi','r':r,'chi':chi,'ratio':ratio,'shell_error':err})
        assert abs(ratios[-1]-1)<abs(ratios[0]-1)/8
    for r in [.2,.4]:
        c=math.cos(r); R=(1-c)**2/(8*(1+c)); u=(1+3*c)/(4*(1+c))
        coeff=math.sqrt(1-c)/((1+c)*math.sqrt(2*u))
        for frac in [.03,.003,.0003]:
            delta=R*frac; mu=math.sqrt(R-delta)
            exact,err=exact_axis_rate(r,mu)
            ratio=exact/(coeff*math.sqrt(delta))
            assert abs(ratio-1)<.007
            rows.append({'kind':'fixed_k_threshold','r':r,'delta_over_R':frac,
                         'ratio':ratio,'shell_error':err})
    mu=.04**2/(8*math.sqrt(1.5))
    low,_=exact_axis_rate(.04,mu,32,12); high,_=exact_axis_rate(.04,mu,128,48)
    assert abs(low/high-1)<1e-9
    return {'rows':rows,'refinement_relative_change':abs(low/high-1)}


def comparator_controls():
    rng=np.random.default_rng(883)
    minimum=math.inf
    for _ in range(300):
        k=rng.uniform(-math.pi,math.pi,3); p=rng.uniform(-math.pi,math.pi,3)
        mu=rng.uniform(.01,.5)
        pair=math.hypot(mu,photon(p))+math.hypot(mu,photon(k-p))
        lower=math.sqrt(4*mu*mu+photon(k)**2)
        if MUTATION=='comparator_mass': lower=math.sqrt(400*mu*mu+photon(k)**2)
        assert pair>=lower-1e-13
        minimum=min(minimum,pair-lower)
    return {'sample_count':300,'min_sample_slack':minimum}


def observation_envelopes():
    record=json.loads((ROOT/AUDIT_INPUT_PATHS[1]).read_text())
    datum={r['id']:r for r in record['data']}
    m=datum['electron_rest_energy']['value']
    # Separate CODATA's original MeV unit checks the GeV transcription path.
    assert abs(m*1000-.51099895069)<1e-15
    alpha=datum['alpha']['value']
    exact=record['exact_SI_definitions']
    hc=exact['h_J_s']*exact['c_m_per_s']/(2*math.pi*exact['elementary_charge_C']*1e9)
    assert abs(hc/1.973269804593025e-16-1)<2e-15
    rows=[]
    for name in ['J2032_cutoff','Crab_cutoff']:
        d=datum[name]
        for shift in [-1,0,1]:
            energy=d['value']+shift*d['systematic_shift']
            if MUTATION=='energy_unit':energy*=1000
            lam=math.sqrt(energy*energy/4+energy**4/(64*m*m))
            # Independent inversion of the exact axis equality via S and R.
            s=energy*energy/(4*lam*lam)
            assert abs((m/lam)**2/(s*s/(4*(1-s)))-1)<2e-14
            # Records must not silently change the unit of the source input.
            assert .6e6<energy<1.3e6
            rows.append({'source_datum':name,'systematic_shift_index':shift,
                         'E_GeV':energy,'Lambda_axis_GeV':lam,
                         'Lambda_necessary_any_orientation_GeV':lam/math.sqrt(3),
                         'ell_axis_m':hc/lam,'ell_necessary_m':math.sqrt(3)*hc/lam,
                         'interpretation':'conditional kinematic sensitivity; no new confidence bound'})
    eqg=datum['timing_EQG2_subluminal']['value']
    energy=datum['J2032_cutoff']['value']
    length=[{'chi':chi,'central_decay_length_m_leading':hc/(alpha*m*m/(2*energy)*scaling_I(chi))}
            for chi in [1.05,1.5,3,10]]
    return {'calibration_hbar_c_GeV_m':hc,'envelopes':rows,
            'timing_Lambda_axis_GeV':eqg/math.sqrt(12),
            'timing_Lambda_necessary_GeV':eqg/6,
            'illustrative_tree_lengths':length,
            'length_scope':'fixed-chi leading coefficient only; no renormalized/detector bridge',
            'fit_count':0,'blind_validation_count':0}


def main():
    global MUTATION
    parser=argparse.ArgumentParser()
    parser.add_argument('--mutation',choices=['threshold_factor','angular_order','vertex_phase',
                         'rate_normalization','comparator_mass','energy_unit'])
    args=parser.parse_args(); MUTATION=args.mutation or ''
    result={'scope':'finite controls and conditional envelopes; no empirical fit',
            'threshold':threshold_controls(),'angular':angular_controls(),
            'spin':spin_controls(),'rate':rate_controls(),
            'comparator':comparator_controls(),'observations':observation_envelopes()}
    if MUTATION:
        print('MUTATION SURVIVED: '+MUTATION)
        return
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'threshold_cases':len(result['threshold']),
                      'angular_cases':len(result['angular']),
                      'spin':result['spin'],'rate':result['rate'],
                      'observations':result['observations']},indent=2))
    print('per_element: checked exact 4x4 Dirac traces against the separate scalar formula.')
    print('per_site: checked and not executed — no real-space source or detector dynamics are simulated here.')
    print('per_mode: checked finite momentum thresholds, Ward differences and polarization matrix elements.')
    print('per_block: checked declared fixed-chi and fixed-momentum coarea quadratures with resolution controls.')
    print('lattice_wide: checked and not executed — finite numerical controls do not prove the analytic torus quantifiers.')
    print('TOTAL: PASS=6 FAIL=0')


if __name__=='__main__':main()
