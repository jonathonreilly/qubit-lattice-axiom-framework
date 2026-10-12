#!/usr/bin/env python3
"""Independent far-field identities, plateau arithmetic and tiny fixtures."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import sys
sys.dont_write_bytecode=True
import contextlib
import datetime
import hashlib
import io
import json
import math
from pathlib import Path
import resource
import time
import types
import mpmath as mp
import numpy as np
import sympy as sp

RUNTIME=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=RUNTIME/'gravity/response_inverse/independent_far_field_review'
MANIFEST=json.loads((OUT/'snapshot_manifest_v1.json').read_text())
SOURCES={Path(r['original']).name:r for r in MANIFEST['sources']}
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()


def guard():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RUNTIME/p).exists() for p in ['STOP_REQUESTED.json','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'])
    for row in MANIFEST['sources']+MANIFEST['receipts']:
        assert sha(row['original'])==sha(row['snapshot'])==row['sha256']


def subject(name):
    row=SOURCES[name+'.py'];module=types.ModuleType(name)
    module.__file__=row['original'];sys.modules[name]=module
    exec(compile(Path(row['snapshot']).read_text(),row['original'],'exec'),module.__dict__)
    return module


def write(path,data):
    assert not path.exists(),path
    path.write_text(json.dumps(data,indent=2)+'\n')


def independent_interval(weights,knots,E):
    # Find boundaries from all active derivative intervals, rather than merge
    # neighboring zero cells using the author's search-and-while algorithm.
    active=[(lo,hi) for w,lo,hi in zip(weights,knots[:-1],knots[1:]) if w!=0]
    assert all(not lo<E<hi for lo,hi in active)
    low=max([0.]+[hi for lo,hi in active if hi<=E])
    high=min([math.inf]+[lo for lo,hi in active if lo>=E])
    assert low<E<high
    return low,high


def independent_N(acceleration,weights,knots):
    A=mp.mpf(acceleration);result=mp.mpf(1)
    for weight,lo,hi in zip(weights,knots[:-1],knots[1:]):
        lo,hi=mp.mpf(str(lo)),mp.mpf(str(hi))
        basis=1 if A<=lo else 0 if A>=hi else mp.log(hi/A)/mp.log(hi/lo)
        result+=mp.mpf(str(weight))*basis
    return result


def symbolic_controls():
    r,a,ne,E=sp.symbols('r a N_e E',positive=True)
    c,K,b,d,epsilon=sp.symbols('c K b d epsilon',real=True)
    p2=(3*c*c-1)/2
    potential=-a*ne/r*(1+K*(1-c*c)/2)
    lap=lambda f:sp.diff(r*r*sp.diff(f,r),r)/(r*r)+sp.diff((1-c*c)*sp.diff(f,c),c)/(r*r)
    assert sp.simplify(lap(potential)+2*a*ne*K*p2/r**3)==0
    normalized_flux=sp.integrate(r*r*sp.diff(potential,r),(c,-1,1))/2
    assert sp.simplify(normalized_flux-a*ne*(1+K/3))==0
    assert sp.simplify(lap(p2/r**3))==0
    assert sp.integrate(r*r*sp.diff(p2/r**3,r),(c,-1,1))==0
    magnitude=sp.series(sp.sqrt(1+2*epsilon*c+epsilon**2),epsilon,0,3).removeO()
    response=ne+b*E*(magnitude-1)+d*E**2*(magnitude-1)**2/2
    response=sp.series(response,epsilon,0,3).removeO()
    flux=sp.expand(sp.integrate(response*(c+epsilon),(c,-1,1))/(2*epsilon))
    assert sp.simplify(flux.subs(epsilon,0)-ne-b*E/3)==0
    assert sp.diff(flux,epsilon).subs(epsilon,0)==0
    # U dot Hess(Phi_N) dot U uses Hess=a/r^3*(I-3 n n^T).
    norm2=E**2+2*E*epsilon*c+epsilon**2
    leading=sp.limit((b/E)*(norm2-3*(epsilon+E*c)**2),epsilon,0)
    assert sp.simplify(leading-b*E*(1-3*c*c))==0
    return {'poisson_identity':str(sp.simplify(lap(potential))),
            'flux_over_4pi':str(sp.simplify(normalized_flux)),
            'surface_expansion_limit':str(sp.simplify(flux.subs(epsilon,0))),
            'homogeneous_quadrupole_laplacian_and_flux_zero':True}


def nonplateau_flux_controls():
    # A synthetic smooth response; this exercises nonzero K independently.
    E=mp.mpf(1);ne=mp.mpf('1.6');b=mp.mpf('-.3');d=mp.mpf('.2')
    N=lambda A:ne+b*(A-E)+d*(A-E)**2/2
    expected=ne+E*b/3
    fluxes=[]
    for epsilon in ['.1','.01','.001']:
        q=mp.mpf(epsilon)
        value=mp.quad(lambda c:N(E*mp.sqrt(1+2*q*c+q*q))*(1+c/q),[-1,0,1])/2
        fluxes.append({'internal_to_external_ratio':float(q),'flux_coefficient':float(value),
                       'expected_limit':float(expected),'absolute_error':float(abs(value-expected))})
    assert fluxes[-1]['absolute_error']<4e-8
    assert all(fluxes[i+1]['absolute_error']<fluxes[i]['absolute_error']/90 for i in range(2))
    a=.7;angles=np.linspace(-1,1,301);errors=[]
    for r in [8.,16.,32.,64.]:
        s=a/r**2;m=np.sqrt(1+s*s+2*s*angles)
        exact=(-.3+.2*(m-1))/m*a/r**3*(m*m-3*(s+angles)**2)
        expected_source=a*(-.3)/r**3*(1-3*angles**2)
        err=float(np.max(np.abs(exact-expected_source)))
        errors.append({'r':r,'absolute_error':err,'r5_scaled_error':err*r**5})
    assert max(x['r5_scaled_error'] for x in errors)<2
    assert all(errors[i+1]['absolute_error']<errors[i]['absolute_error']/25 for i in range(3))
    return {'surface_flux':fluxes,'source_remainder':errors}


def original_arithmetic():
    fits=json.loads((OUT/'snapshot_shared_response_fits_v1.json').read_text())
    margin=json.loads((OUT/'snapshot_margin_candidate_v1.json').read_text())
    actual=json.loads((OUT/'snapshot_FAR_FIELD_PREDICTION_v1.json').read_text())
    original=next(c['best_sampled'] for c in fits['cases'] if c['family']=='D' and c['constraints']=='galaxies_external_solar')
    assert actual['source_sha256']==SOURCES['direct_far_field_check.py']['sha256']
    assert actual['note_sha256']==SOURCES['DIRECT_FAR_FIELD_PREDICTION.md']['sha256']
    assert actual['fits_sha256']==sha(OUT/'snapshot_shared_response_fits_v1.json')
    assert actual['margin_sha256']==sha(OUT/'snapshot_margin_candidate_v1.json')
    knots=[10**(-13+j/4) for j in range(21)]
    GM=mp.mpf('1.32712440018e20');au=mp.mpf(149597870700)
    results=[]
    for (label,candidate),reported in zip([('original_D_joint',original),('interior_D_joint',margin)],actual['rows']):
        w=candidate['weights'];E=float(candidate['external_newtonian_SI'])
        assert len(w)==20 and min(w)>=0
        low,high=independent_interval(w,knots,E)
        assert np.allclose(reported['constant_interval_SI'],[low,high],rtol=3e-16,atol=0)
        e=mp.mpf(str(E));delta=min(e-mp.mpf(str(low)),mp.mpf(str(high))-e)
        ne=independent_N(e,w,knots);speed=mp.sqrt(ne);rstar=mp.sqrt(GM/delta)
        assert abs(ne-mp.mpf(str(reported['N_E'])))<mp.mpf('5e-16')
        assert abs(speed-mp.mpf(str(reported['asymptotic_circular_speed_scale_ratio'])))<mp.mpf('5e-16')
        assert abs(rstar/au-mp.mpf(str(reported['solar_mass_support_bound_AU'])))<mp.mpf('5e-12')
        assert reported['K_E']==0
        checks=[]
        for factor in ['1.000001','1.001','2','10','100']:
            f=mp.mpf(factor);r=rstar*f;s=GM/r**2
            assert e-s>mp.mpf(str(low)) and e+s<mp.mpf(str(high))
            # Independent adaptive high-precision quadrature, not the author's
            # Legendre nodes or its ramp function. Pair opposite hemispheres.
            def integrand(c):
                plus=mp.sqrt(e*e+s*s+2*e*s*c)
                minus=mp.sqrt(e*e+s*s-2*e*s*c)
                return (independent_N(plus,w,knots)*(1+e*c/s)+independent_N(minus,w,knots)*(1-e*c/s))/2
            flux=mp.quad(integrand,[0,1])
            assert abs(flux-ne)<mp.mpf('1e-55')
            checks.append({'factor':float(f),'flux':float(flux),'absolute_error':str(abs(flux-ne))})
        inner_s=delta/mp.mpf('.99')**2
        inner_response=independent_N(e-inner_s,w,knots)
        assert inner_response>ne
        results.append({'candidate':label,'interval':[low,high],'N_E':float(ne),'K_E':0,
                        'speed_scale':float(speed),'support_bound_AU':float(rstar/au),
                        'delta_SI':float(delta),'independent_flux_checks':checks,
                        'opposite_axis_response_at_0_99_support_bound':float(inner_response)})
    return results


def extraction_fixtures(checker,fit):
    saved=fit.operator.OUT;root=OUT/'fixtures';root.mkdir(exist_ok=False)
    configurations=[('middle',{5:.2,13:.4},9),('low_tail',{8:.4},3),
                    ('high_tail',{4:.2},12),('all_zero',{},9),
                    ('one_cell',{8:.2,10:.4},9),('tiny_nonzero_neighbor',{8:1e-300,12:.4},9),
                    ('nonconstant',{9:.2},9)]
    results=[]
    try:
        for name,active,cell in configurations:
            directory=root/name;directory.mkdir();fit.operator.OUT=directory
            w=np.zeros(20)
            for j,value in active.items():w[j]=value
            knots=fit.operator.KNOTS
            E=float(np.sqrt(knots[cell]*knots[cell+1]))
            candidate={'weights':w.tolist(),'external_newtonian_SI':E}
            write(directory/'shared_response_fits_v1.json',{'cases':[{'family':'D',
                  'constraints':'galaxies_external_solar','best_sampled':candidate}]})
            write(directory/'margin_candidate_v1.json',candidate)
            try:
                with contextlib.redirect_stdout(io.StringIO()) as capture:checker.main()
            except AssertionError:
                assert name=='nonconstant'
                assert not (directory/'FAR_FIELD_PREDICTION_v1.json').exists()
                results.append({'fixture':name,'nonconstant_rejected':True});continue
            (directory/'stdout.txt').write_text(capture.getvalue())
            assert name!='nonconstant'
            result=json.loads((directory/'FAR_FIELD_PREDICTION_v1.json').read_text())
            expected=independent_interval(w,knots,E)
            for row in result['rows']:
                assert row['constant_interval_SI']==list(expected)
                assert abs(row['N_E']-float(independent_N(E,w,knots)))<1e-14
            results.append({'fixture':name,'interval':list(expected),'N_E':result['rows'][0]['N_E']})
    finally:fit.operator.OUT=saved
    return results


def main():
    guard();start=time.monotonic();mp.mp.dps=65
    checks={'symbolic':symbolic_controls(),'nonplateau':nonplateau_flux_controls(),
            'actual_response_arithmetic':original_arithmetic()}
    op=subject('direct_galaxy_response_operator');subject('direct_response_basis')
    fit=subject('direct_shared_response_fit');checker=subject('direct_far_field_check')
    op.field.RingField=lambda *a,**k:(_ for _ in ()).throw(AssertionError('Actual fields forbidden'))
    saved_load=np.load;np.load=lambda *a,**k:(_ for _ in ()).throw(AssertionError('No data arrays may be read'))
    try:checks['plateau_extraction']=extraction_fixtures(checker,fit)
    finally:np.load=saved_load
    guard()
    result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,
            'source_sha256':sha(__file__),'snapshot_manifest_sha256':sha(OUT/'snapshot_manifest_v1.json'),
            'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'mp_decimal_digits':mp.mp.dps,'actual_target_arrays_read':False,
            'actual_galaxy_field_computations':0,'actual_refits':0,'checks':checks}
    write(OUT/'independent_checks_v1.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))


if __name__=='__main__':main()
