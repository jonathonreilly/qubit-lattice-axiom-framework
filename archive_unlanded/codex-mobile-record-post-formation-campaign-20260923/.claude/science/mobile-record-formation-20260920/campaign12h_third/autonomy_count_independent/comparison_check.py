#!/usr/bin/env python3
"""Selective post-seal comparisons; never imports or executes author code."""
from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp
import sympy as sp

OUT=Path(__file__).resolve().parent
BASE=OUT.parent
AUTHOR_SEAL=BASE/'AUTONOMY_AND_FORMATION_COUNT_AUTHOR_SEAL.json'
EXPECTED_AUTHOR='fc3e56328ffbf995b9ee34432e6fd9187a48a9cc6bff48d549c928d7c4499358'
EXPECTED_PRE='2fca7f6f5052aed71e25f24120eb2e8813e60d6e489e9093c8f3da29b0c13e14'


def identity(path):
    path=Path(path).resolve();raw=path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}


def authenticate():
    assert identity(AUTHOR_SEAL)['sha256']==EXPECTED_AUTHOR
    author=json.loads(AUTHOR_SEAL.read_text())
    assert len(author['artifacts'])==13
    for row in author['artifacts']:
        assert identity(row['path'])==row,row['path']
    prepath=OUT/'PRE_COMPARISON_SEAL.json'
    assert identity(prepath)['sha256']==EXPECTED_PRE
    pre=json.loads(prepath.read_text())
    for row in pre['sources']+pre['artifacts']:
        got=identity(row['path'])
        assert all(got[k]==row[k] for k in ['path','bytes','sha256']),row['path']
    receipts=[]
    for prefix,script in [('AUTONOMOUS_GAUGE_BIRTH_RAIL','autonomous_gauge_birth_rail_check.py'),
                          ('GAUGE_FORMATION_COUNT_COHERENCE','gauge_formation_count_coherence_check.py')]:
        result=json.loads((BASE/(prefix+'_RESULTS.json')).read_text())
        receipt=json.loads((BASE/(prefix+'_RUN_RECEIPT.json')).read_text())
        sha=identity(BASE/script)['sha256']
        assert result['script_sha256']==receipt['script_sha256']==sha
        assert receipt['returncode']==0
        assert (BASE/(prefix+'_RUN.log')).read_bytes()==(BASE/(prefix+'_RESULTS.json')).read_bytes()
        assert (BASE/(prefix+'_RUN.stderr')).read_bytes()==b''
        receipts.append({'prefix':prefix,'source_binding':sha,'exit_code':0,
                         'stdout_is_complete_result':True,'stderr_empty':True})
    return {'author_artifacts':13,'prior_sources':len(pre['sources']),
            'prior_artifacts':len(pre['artifacts']),'author_receipts':receipts}


def packet_comparisons(author):
    bounds=[]
    for row in author['packet_moments_and_bounds']['finite_time_bounds']:
        m,l,t=row['M'],row['L'],row['T']
        mean=F(2*m,m+1)*t-l+F(m,2)
        var=F(m*m,4*(2*m-1))+F(4*(2*m+1),(m+1)**2*(m+2))*t*t
        bound=var/(var+mean*mean)
        assert mean>0
        assert mean==F(row['mean_position']) and var==F(row['position_variance_at_T'])
        assert bound==F(row['uniform_later_nonpassage_bound'])
        assert float(bound)==row['decimal_bound']
        bounds.append({'M':m,'L':l,'T':t,'independent_exact_bound':str(bound)})
    old=json.loads((OUT/'CARRIER_RESULTS.json').read_text())
    independent_moments={r['M']:r for r in old['exact_rational_moments']}
    for row in author['packet_moments_and_bounds']['exact_finite_sum_controls']:
        ours=independent_moments[row['M']]
        for theirs,own in [('position_variance','variance_X'),('mean_velocity_at_J1','mean_V_J1'),
                           ('velocity_variance_at_J1','variance_V_J1')]:
            assert F(row[theirs])==F(ours[own])
        assert row['symmetrized_covariance']=='0'
    # Alternative exact integral: expand (1-sin s)^M on 0<=s<=pi,
    # rather than using the author's Fourier-coefficient tail expression.
    mp.mp.dps=90
    tails=[]
    for row in author['asymptotic_directional_tail_controls']:
        m=row['M'];central=math.comb(2*m,m);integral=sp.S.Zero
        for j in range(m+1):
            if j%2==0:
                power_integral=sp.pi*sp.Rational(math.comb(j,j//2),2**j)
            else:
                q=(j-1)//2
                power_integral=sp.Rational(2*4**q*math.factorial(q)**2,math.factorial(2*q+1))
            integral+=(-1)**j*math.comb(m,j)*power_integral
        delta=sp.factor(sp.Rational(2**m,2*central)*integral/sp.pi)
        assert sp.expand(delta-sp.sympify(row['exact_tail']))==0
        exact_first=F(2**(m-1),central);exact_second=F(2*m+1,2**(m+1))
        assert exact_first==F(row['integral_bound_exact'])
        assert exact_second==F(row['elementary_bound_exact']) and exact_first<=exact_second
        beta_tail=mp.betainc(m+mp.mpf('0.5'),mp.mpf('0.5'),0,mp.mpf('0.5'),regularized=True)
        printed=mp.mpf(row['tail_decimal_diagnostic'])
        assert abs(printed-beta_tail)/beta_tail<mp.mpf('4e-16')
        tails.append({'M':m,'alternative_exact_integral':str(delta),
                      'beta_integral_decimal':mp.nstr(beta_tail,35),'matches_author':True})
    return {'exact_bounds':bounds,'all_16_prior_moment_rows_match':True,'directional_tails':tails}


def bessel_comparison(author):
    intervals=[]
    for q in [1,4]:
        upper=sum((F((-q)**n,math.factorial(n)**2) for n in range(25)),F(0))
        lower=upper+F((-q)**25,math.factorial(25)**2)
        assert lower<upper and F(q,26**2)<1
        named=author['specified_nonmonotone_control'][f'J0_{2 if q==1 else 4}_interval']
        assert F(named[0])<lower<upper<F(named[1])
        intervals.append((lower,upper))
    (lo2,hi2),(lo4,hi4)=intervals
    assert 0<lo2<hi2 and lo4<hi4<0
    p1lower=(1-hi2**2)/2;p2upper=(1-hi4**2)/2
    assert p1lower>p2upper
    return {'method':'Different truncation: exact terms through n=24/25; intervals lie inside author n=20/21 brackets.',
            'J0_2_interval':[str(lo2),str(hi2)],'J0_4_interval':[str(lo4),str(hi4)],
            'strict_decrease_margin_lower':str(p1lower-p2upper),
            'strict_decrease_margin_decimal':float(p1lower-p2upper)}


def ring_comparison(author):
    rows=[]
    for case in author['cases']:
        k=case['K'];assert case['physical_dimension']==2**k
        assert case['occupation_fiber_dimension']==2
        counts=[]
        for comp in case['occupation_hopping_components']:
            n=comp['record_number'];h=k-n
            total=math.comb(k,h)
            # No birth contact iff the h holes form an independent set of C_K.
            # Root one of the h holes (for h>0) and count positive cyclic gaps;
            # equivalent closed count K/(K-h)*binomial(K-h,h).
            no_contact=F(k,k-h)*math.comb(k-h,h) if h<=k//2 else F(0)
            assert no_contact.denominator==1
            contact=total-int(no_contact)
            assert total==comp['occupation_patterns']
            assert contact==comp['birth_contact_patterns']
            counts.append({'N':n,'patterns':total,'birth_contacts':contact})
        for channel in case['channels']:
            assert channel['forward_births']==channel['reverse_orientation_births']==2**(k-3)
            assert channel['hopping_matrix_entries']==2**(k-1)
        full=sorted([sum(1<<i for i in range(0,k,2)),sum(1<<i for i in range(1,k,2))])
        assert full==case['full_basis_indices']
        assert F(case['unit_electric_monitoring_dual_eigenvalue'])==F(-k,2)
        chi=sp.symbols('chi')
        assert sp.expand(sp.sympify(case['terminal_coherence'])-chi**(k//2))==0
        assert sp.expand(sp.sympify(case['terminal_purity'])-(1+chi**k)/2)==0
        rows.append({'K':k,'independent_cycle_gap_counting':counts,'full_basis':full,
                     'channel_counts_checked_by_local_bit_freedom':True})
    prior=json.loads((OUT/'COUNT_RING_RESULTS.json').read_text())
    counter=prior['exact_controls']['broader_jump_completion_countercontrol']
    assert counter['record_count']==2 and counter['full_count']==4
    assert counter['full_exact_drift']=='zero'
    return {'cases':rows,'completion_scope_countercontrol_reused':counter,
            'countercontrol_source':identity(OUT/'COUNT_RING_RESULTS.json'),
            'scope':'The present comparison does not rerun the previously exact feedback-jump control or author ring suites.'}


def main():
    auth=authenticate()
    carrier=json.loads((BASE/'AUTONOMOUS_GAUGE_BIRTH_RAIL_RESULTS.json').read_text())
    ring=json.loads((BASE/'GAUGE_FORMATION_COUNT_COHERENCE_RESULTS.json').read_text())
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS for comparisons; one scope clarification remains in the frozen prose.',
            'authentication':auth,'carrier_comparisons':packet_comparisons(carrier),
            'independent_rational_nonmonotonicity_control':bessel_comparison(carrier),
            'ring_comparisons':ring_comparison(ring),'failed_attempts':[],
            'limits':'No author script imported/executed. Context-only literature/repository read receipts authenticated as artifacts, not independently verified underlying readings. Excluded clock/observability/frontier files unopened.'}
    (OUT/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
