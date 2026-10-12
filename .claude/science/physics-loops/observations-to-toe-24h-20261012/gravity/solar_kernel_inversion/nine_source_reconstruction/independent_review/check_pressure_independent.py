#!/usr/bin/env python3
"""Exact RHS sensitivity and fixed-cap perturbation checks; no fitting."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from fractions import Fraction as F
import datetime as dt
import hashlib
import json
from pathlib import Path
import mpmath as mp
import numpy as np

HERE=Path(__file__).resolve().parent
mp.mp.dps=70
def read(path): return json.loads(path.read_text())
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def rat(value): return F(*map(int,value))
def ratio(value): return [str(value.numerator),str(value.denominator)]
def m(value):
    v=value if isinstance(value,F) else F(float(value))
    return mp.mpf(v.numerator)/v.denominator

def main():
    rows=read(HERE/'snapshot_manifest_v1.json')['files']+read(HERE/'certificate_snapshot_manifest_v1.json')['files']
    en={x['key']:x for x in rows}
    def p(key): return HERE/en[key]['snapshot']
    def doc(key): return read(p(key))
    pressure=doc('pressure_receipt');replay=doc('replay_receipt');results=[]
    assert pressure['source_sha256']==en['pressure_source']['sha256']
    assert pressure['source_data_sha256']==en['source_data']['sha256']
    assert pressure['target_data_sha256']==en['target_data']['sha256']
    assert replay['source_sha256']==en['replay_source']['sha256']
    assert replay['candidates_sha256']==en['CANDIDATES']['sha256']
    assert len(replay['cases'])==6
    for row in replay['cases']:
        assert row['matrix_sha256']==en[row['name']+'_matrix']['sha256']
        assert row['first']['status']==row['second']['status']==0
        assert row['weights_and_t_bitwise_match_original']
    with np.load(p('source_data')) as raw,np.load(p('target_data')) as target:
        for given in pressure['results']:
            family=given['family'];key=family+'_galaxies_only'
            c=doc(key+'_certificate');matrix=doc(key+'_matrix')
            assert given['certificate_sha256']==en[key+'_certificate']['sha256']
            y=list(map(rat,c['y_rational']));b=list(map(lambda v:F(float.fromhex(v)),matrix['b_hex']))
            L=rat(c['lower_bound_rational']);delta=rat(c['weight_deficit_rational'])
            assert given['lower_bound_rational']==c['lower_bound_rational']
            terms=[];shifts=[F(0)]*len(b)
            for i,(label,yi) in enumerate(zip(matrix['row_labels'],y)):
                if not yi or 'source' not in label: continue
                name=label['source'];bin=label['scored_bin'];mask=raw[name+'_score_mask']
                R=raw[name+'_R'][mask];V=target[name+'_v'][mask];A=V**2/R
                assert label['R_kpc']==float(R[bin])
                denominator=F(float(R[bin]))*F(float(A[bin]))
                sign=1 if label['kind']=='upper_velocity_rectangle' else -1
                assert label['kind'] in ['upper_velocity_rectangle','lower_velocity_rectangle']
                coeff=sign*yi/denominator
                actual=next(t for t in given['terms'] if all(t[k]==label[k] for k in ['source','kind','scored_bin']))
                assert coeff==rat(actual['coefficient_rational'])
                assert float(coeff)==actual['coefficient_approximate']
                assert float(V[bin])==actual['velocity_km_s']
                # An arbitrary exact positive or negative squared-speed shift.
                pressure_fixture=F((-1)**i*(i+1),7)
                shifts[i]=sign*pressure_fixture/denominator
                terms.append({**label,'coefficient':float(coeff),'coefficient_rational':ratio(coeff),
                              'fixture_p':ratio(pressure_fixture),'fixture_contribution':coeff*pressure_fixture})
            assert len(terms)==len(given['terms'])
            shifted=sum(yi*(bi+di) for yi,bi,di in zip(y,b,shifts))-100*delta
            affine=L+sum(t['fixture_contribution'] for t in terms)
            assert shifted==affine
            relieving=[t for t in terms if t['source']=='UGC07577']
            assert all(rat(t['coefficient_rational'])<0 for t in relieving)
            magnitude=-sum(rat(t['coefficient_rational']) for t in relieving)
            threshold=L/magnitude
            assert threshold==rat(given['necessary_max_pressure_km2_s2_rational'])
            assert float(threshold)==given['necessary_max_pressure_km2_s2_approximate']
            assert L-magnitude*threshold==0 and L-magnitude*threshold/2==L/2
            assert float(threshold/64)==given['illustrative_slope_if_sigma_8_km_s']
            entry={'family':family,'exact_affine_rhs_identity':True,
                   'necessary_pmax_rational':ratio(threshold),'necessary_pmax_approximate':float(threshold),
                   'units':'(km/s)^2','illustrative_minus_log_density_slope':float(threshold/64),
                   'threshold_saturates_this_certificate_only':True,'support':[]}
            for t in terms:
                t['fixture_contribution']=ratio(t['fixture_contribution']);entry['support'].append(t)
            if family=='D':
                velocity=F(float(target['UGC07577_v'][raw['UGC07577_score_mask']][2]))
                speed=mp.sqrt(m(velocity**2+threshold))
                assert abs(float(speed)-given['central_speed_illustration_km_s'])<1e-13
                assert abs(float(speed-m(velocity))-given['central_speed_increase_illustration_km_s'])<1e-13
                entry['illustrative_circular_speed_km_s']=float(speed)
            results.append(entry)
    # Show why the perturbation claim must preserve the explicit weight cap.
    # Original: -w-t<=-300, w<=100, y=(-1,-1), L=200.
    # Perturbed: -1.1w-t<=-300, .9w<=100; t column unchanged.
    eps=F(1,10);claim=F(200)-100*eps*2
    free_cap_w=F(100)/(1-eps);free_cap_t=300-(1+eps)*free_cap_w
    assert free_cap_t<claim and free_cap_w>100
    assert -(1+eps)*free_cap_w-free_cap_t==-300 and (1-eps)*free_cap_w==100
    # With w<=100 independently retained, the claimed lower bound is valid.
    fixed_cap_t=F(300)-(1+eps)*100
    assert fixed_cap_t>=claim
    out={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':sha(Path(__file__)),
      'pressure_checks':results,'replay_identity_and_record_checks':True,
      'replay_limit':'Reviewed source assertions and saved statuses; did not run an LP replay. Original second-stage status was not recorded.',
      'fixed_cap_perturbation_counterexample':{'epsilon':str(eps),'eta':'0','y':['-1','-1'],
        'original_L':'200','claimed_if_cap_not_preserved':str(claim),
        'relaxed_cap_feasible_w':str(free_cap_w),'relaxed_cap_feasible_t':str(free_cap_t),
        'fixed_cap_actual_min_t':str(fixed_cap_t),'interpretation':'The corollary is valid when nonnegativity and cap100 remain fixed.'},
      'no_author_imports':True,'no_fit_or_field_solve':True}
    dest=HERE/'independent_pressure_and_replay_checks_v1.json';assert not dest.exists()
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'results':[{k:v for k,v in x.items() if k!='support'} for x in results],
                      'fixed_cap_counterexample':out['fixed_cap_perturbation_counterexample']},indent=2))
if __name__=='__main__': main()
