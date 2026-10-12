#!/usr/bin/env python3
"""Independent small controls; no author helper imports or empirical data."""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import sys
sys.dont_write_bytecode = True
import hashlib
import json
import math
import resource
import time
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path
import mpmath as mp
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
RT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = RT/'quantum/angular_robustness/independent_angular_review'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def guard():
    assert time.time() < json.loads((RT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RT/p).exists() for p in (
        'STOP_REQUESTED.json', 'USER_STOP_REQUESTED.json', 'STOP_REQUESTED',
        'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'))

def rational(row):
    return Q(int(row['numerator']), int(row['denominator']))

def packed(q):
    return {'numerator':str(q.numerator),'denominator':str(q.denominator),
            'decimal':mp.nstr(mp.mpf(q.numerator)/q.denominator, 45)}

def mpq(q):
    return mp.mpf(q.numerator)/q.denominator

def ceiling(q):
    return q.numerator//q.denominator + bool(q.numerator%q.denominator)

def atan_enclosure(x, terms):
    # Independently used identity pi/4=atan(1/2)+atan(1/3), not author's Machin identity.
    partial = Q(0)
    for j in range(terms):
        partial += (-1)**j*x**(2*j+1)/(2*j+1)
    next_partial = partial+(-1)**terms*x**(2*terms+1)/(2*terms+1)
    return min(partial,next_partial),max(partial,next_partial)

def run():
    started = time.perf_counter()
    guard()
    mp.mp.dps = 90
    manifest = json.loads((OUT/'snapshot_manifest_v1.json').read_text())
    v2 = json.loads((OUT/'v2_wording_snapshot.json').read_text())
    records = manifest['sources']+manifest['receipts']+[v2]
    for r in records:
        assert sha(r['original']) == sha(r['snapshot']) == r['sha256']
    freeze = json.loads((OUT/'snapshot_FREEZE.json').read_text())
    receipt = json.loads((OUT/'snapshot_RESULTS_v1.json').read_text())
    premise = json.loads((HERE/'DIRECT_REFLECTION_RESULT.json').read_text())
    assert receipt['sources'] == freeze['sources'] == {
        Path(r['original']).name:r['sha256'] for r in manifest['sources']}
    assert receipt['freeze_sha256'] == sha(OUT/'snapshot_FREEZE.json')
    assert datetime.fromisoformat(freeze['at']) < datetime.fromisoformat(receipt['at'])
    assert freeze['equal_angle_radians'] == ['0','1/2000','1/1000','1/500','1/250']
    assert freeze['candidate_absolute_correlation_error'] == ['0','1/1000']
    assert freeze['visibility'] == '19/20' and freeze['data_fit'] is None

    # P3's zero r has r^2=3/5. Its even antiderivative can be evaluated rationally.
    primitive_r = Q(5,8)*Q(3,5)**2-Q(3,4)*Q(3,5)
    primitive_1 = Q(5,8)-Q(3,4)
    absolute_integral = 2*(primitive_1-2*primitive_r)
    product_tv = 7*absolute_integral
    J = 1+product_tv
    assert absolute_integral == Q(13,20) and product_tv == Q(91,20) and J == Q(111,20)
    assert J == rational(premise['total_absolute_weight'])
    # The separately assigned diagonal sign is measurable and does not affect product integration.
    norm_attainment = 1+product_tv
    diagonal_only = Q(-1)
    assert norm_attainment == J and diagonal_only == -1

    # Exact differentiation and inequalities on u,t in [0,1].
    u,t=sp.symbols('u t', real=True)
    g=(u+t)/(1+u*t)
    gu=(1-t*t)/(1+u*t)**2
    gt=(1-u*u)/(1+u*t)**2
    assert sp.simplify(sp.diff(g,u)-gu)==0
    assert sp.simplify(sp.diff(g,t)-gt)==0
    # Numerators of 1-gu and 1-gt are sums of nonnegative terms here.
    assert sp.expand((1+u*t)**2-(1-t*t)) == 2*u*t+u*u*t*t+t*t
    assert sp.expand((1+u*t)**2-(1-u*u)) == 2*u*t+u*u*t*t+u*u
    k = mp.sqrt(2)*mp.log((1+mp.sqrt(2))/mp.sqrt(3))
    klo,khi = map(rational,premise['k_exact_interval'])
    assert mpq(klo) < k < mpq(khi)
    true_L = 2/mp.pi+k
    def curve(theta):
        uu=1-2*theta/mp.pi
        tt=mp.tanh(k*mp.cos(theta))
        return (uu+tt)/(1+uu*tt)
    midpoint_slope = mp.diff(curve,mp.pi/2)
    assert abs(midpoint_slope+true_L) < mp.mpf('1e-85')
    derivative_ratios=[]
    for j in range(1001):
        theta=mp.pi*j/1000
        derivative=mp.diff(curve,theta)
        assert derivative <= 0
        assert abs(derivative) <= true_L+mp.mpf('1e-85')
        assert abs(curve(mp.pi-theta)+curve(theta)) < mp.mpf('1e-85')
        derivative_ratios.append(abs(derivative)/true_L)
    endpoint_slope = -2/mp.pi*mp.exp(-2*k)
    assert abs(mp.diff(curve,mp.mpf(0))-endpoint_slope)<mp.mpf('1e-85')

    lo2,hi2=atan_enclosure(Q(1,2),120)
    lo3,hi3=atan_enclosure(Q(1,3),80)
    pi_lo,pi_hi=4*(lo2+lo3),4*(hi2+hi3)
    assert mpq(pi_lo) < mp.pi < mpq(pi_hi)
    independent_L_bounds=(2/pi_hi+khi,2/pi_lo+khi)
    lower_ceil,upper_ceil=(Q(ceiling(v*10**30),10**30) for v in independent_L_bounds)
    assert lower_ceil == upper_ceil == rational(receipt['L_certified_upper'])
    L=upper_ceil
    V=Q(19,20)
    a3lo,a3hi=map(rational,premise['a3_interval'])
    B_lower=V*(1-2*a3hi)
    B_upper=V*(1-2*a3lo)
    witness=next(r for r in premise['witnesses'] if rational(r['V'])==V)
    assert [B_lower,B_upper] == list(map(rational,witness['B_interval']))
    gap0=B_lower-1
    assert gap0==rational(receipt['ideal_gap_lower'])
    angle_limit=gap0/(2*J*V*L)
    assert angle_limit==rational(receipt['strict_pure_angle_tolerance_rad'])
    rows=[]
    for index,(dt,et) in enumerate((d,e) for d in freeze['equal_angle_radians']
                                 for e in freeze['candidate_absolute_correlation_error']):
        delta,eps=Q(dt),Q(et)
        allowance=J*(2*V*L*delta+eps)
        gap=gap0-allowance
        n=ceiling(40*J**2/gap**2) if gap>0 else None
        recorded=receipt['rows'][index]
        assert recorded['angle_per_side_rad']==dt and recorded['extra_candidate_error']==et
        assert allowance==rational(recorded['B_allowance_upper'])
        assert gap==rational(recorded['effective_gap_lower'])
        assert n==recorded['N_for_each_error_at_most_1_percent']
        if n is not None:
            needed=40*J**2/gap**2
            assert n-1 < needed <= n
            exponent=Q(n)*gap**2/(8*J**2)
            assert exponent>=5
        if delta:
            optional=mpq(V)*(1-curve(2*mpq(delta)))+mpq(Q(91,10)*V*L*delta)
            assert 0 <= optional <= mpq(J*2*V*L*delta)
        rows.append({'delta':dt,'epsilon':et,'gap':packed(gap),'N':n})
    assert len(rows)==10 and sum(r['N'] is None for r in rows)==1
    assert rows[-1]['gap']['numerator'].startswith('-')
    assert sum(Q(5)**j/math.factorial(j) for j in range(8))>100  # e^5>100, exact.
    for i in range(0,8,2):
        assert rows[i+2]['N'] > rows[i]['N']
    for i in range(0,8,2):
        assert rows[i+1]['N'] > rows[i]['N']

    # A finite exact-degree sphere quadrature realizes the l=3 projector.
    # This control tests the common-map operator argument; it is not a TV discretization.
    z,wz=np.polynomial.legendre.leggauss(8)
    phi=2*np.pi*np.arange(17)/17
    points=np.array([[np.sqrt(1-zz*zz)*np.cos(pp),np.sqrt(1-zz*zz)*np.sin(pp),zz]
                     for zz in z for pp in phi])
    weights=np.repeat(wz/(2*17),17)
    dots=points@points.T
    P3=(5*dots**3-3*dots)/2
    M=7*np.sqrt(weights[:,None]*weights[None,:])*P3
    reflection=np.eye(len(points))-2*M
    projector_error=float(np.max(np.abs(M@M-M)))
    reflection_error=float(np.max(np.abs(reflection@reflection-np.eye(len(points)))))
    eig=np.linalg.eigvalsh(M)
    assert projector_error<1e-13 and reflection_error<1e-12
    assert int(np.sum(eig>.5))==7 and np.max(np.abs(eig-np.round(eig)))<1e-12
    def normalized(x):
        return x/np.linalg.norm(x,axis=1,keepdims=True)
    def value(aa,bb):
        C=-aa@bb.T
        result=-np.sum(weights*np.diag(C))+14*np.sum(weights[:,None]*weights[None,:]*P3*C)
        assert abs(result) <= 1+1e-12
        return float(result)
    warped=normalized(points+np.array([.2,-.1,.4]))
    rotated=points[:,[1,2,0]]
    prob=(1+points[:,2])/2
    mixed=prob[:,None]*warped+(1-prob[:,None])*rotated
    assert np.max(np.linalg.norm(mixed,axis=1))<=1+1e-14
    local_values={'identity':value(points,points),'warp':value(warped,rotated),
                  'source_independent_mixture':value(mixed,points)}
    assert abs(local_values['identity']-1)<1e-13

    # Independent jitter signs can still correlate with local source registers.
    signs=[(a,b) for a in (-1,1) for b in (-1,1)]
    actual=sum(Q(1,4)*(a*a)*(b*b) for a,b in signs)
    averaged_a=sum(Q(1,2)*a for a in (-1,1))
    averaged_b=sum(Q(1,2)*b for b in (-1,1))
    naive=averaged_a*averaged_b
    assert actual==1 and naive==0
    # Common enlarged state and local controlled observable give the actual C=1, B=-1.
    enlarged_B=-actual
    assert abs(enlarged_B)<=1

    # Common constant outputs before retention have B=-1. Retaining only fresh
    # product-branch settings with positive P3 gives Z=J without looking at outcomes.
    p_diag=1/J
    p_product_positive=(J-1)/(2*J)
    original_mean=J*(-p_diag+p_product_positive-p_product_positive)
    selected_mean=J
    assert original_mean==-1 and p_product_positive==Q(91,222) and selected_mean>1
    guard()
    for r in records:
        assert sha(r['original']) == sha(r['snapshot']) == r['sha256']
    result={'at':datetime.now(timezone.utc).isoformat(),'status':'PASS_WITH_V2_PREMISE_CLARIFICATIONS',
        'reviewer_script_sha256':sha(__file__),'source_records':records,
        'method':'Independent exact rational integration/propagation, alternate arctangent pi identity, symbolic derivatives, 90-digit curve controls, degree-exact spherical projector, explicit classical fixtures; no author helper imports.',
        'total_variation':packed(J),'product_total_variation':packed(product_tv),
        'diagonal_only_B':packed(diagonal_only),'operator_norm_attainment':packed(norm_attainment),
        'true_L_numerical':mp.nstr(true_L,70),'max_grid_derivative_ratio':mp.nstr(max(derivative_ratios),45),
        'certified_L_upper':packed(L),'independent_pi_interval_width':packed(pi_hi-pi_lo),
        'pure_angle_strict_bound':packed(angle_limit),'rows':rows,
        'sphere_control':{'nodes':len(points),'projector_rank':7,'idempotence_max_error':projector_error,
                          'reflection_square_max_error':reflection_error,'common_local_values':local_values},
        'correlated_jitter_fixture':{'independent_signs':4,'actual_C':str(actual),'naive_C':str(naive),'enlarged_state_B':str(enlarged_B)},
        'fresh_setting_retention_fixture':{'original_mean':str(original_mean),'retained_mean':str(selected_mean),'retention_probability':str(p_product_positive)},
        'finite_sample_scope':'Fixed N; fresh conditional branch/setting law; common local quantum maps and every-trial candidate conditional lower mean. Each one-sided error <=exp(-5)<.01.',
        'limits':'Pinned a3/reflection interval is a premise, not recertified full sphere classification. No measured calibration, detection model, actual experiment, or empirical exclusion.',
        'elapsed_seconds':time.perf_counter()-started,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    with (OUT/'angular_independent_checks_v1.json').open('x') as f:
        json.dump(result,f,indent=2)
    print(json.dumps({'status':result['status'],'rows':len(rows),'L':packed(L)['decimal'],
                      'angle_limit':packed(angle_limit)['decimal'],'elapsed_seconds':result['elapsed_seconds'],
                      'max_rss_bytes':result['max_rss_bytes']},indent=2))

if __name__=='__main__':
    run()
