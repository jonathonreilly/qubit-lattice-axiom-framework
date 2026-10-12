#!/usr/bin/env python3
"""Independent synthetic margin/readout/cone checks; no empirical fitting."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import sys
sys.dont_write_bytecode = True
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
import numpy as np
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = RUNTIME/'gravity/response_inverse/independent_margin_review'
MANIFEST = json.loads((OUT/'snapshot_manifest_v1.json').read_text())
SOURCES = {Path(r['original']).name:r for r in MANIFEST['sources']}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def guard():
    assert time.time() < json.loads((RUNTIME/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RUNTIME/p).exists() for p in ['STOP_REQUESTED.json','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'])
    for row in MANIFEST['sources'] + MANIFEST['receipts']:
        assert sha(row['original']) == sha(row['snapshot']) == row['sha256']


def subject(name):
    row = SOURCES[name+'.py']
    module = types.ModuleType(name)
    module.__file__ = row['original']
    sys.modules[name] = module
    exec(compile(Path(row['snapshot']).read_text(),row['original'],'exec'),module.__dict__)
    return module


def write_json(path, value):
    assert not path.exists(), path
    path.write_text(json.dumps(value, indent=2)+'\n')


def run_main(module, args, log):
    old = sys.argv
    try:
        sys.argv = [module.__file__, *map(str,args)]
        with contextlib.redirect_stdout(io.StringIO()) as capture:
            module.main()
        log.write_text(capture.getvalue())
    finally:
        sys.argv = old


def fixture(name, E=2.32e-10):
    directory = OUT/'fixtures'/name
    directory.mkdir(parents=True, exist_ok=False)
    parent = directory/'shared_response_fits_v1.json'
    write_json(parent, {'synthetic':True, 'name':name})
    freeze = {'protocol_sha256':SOURCES['FOLLOWUP_MARGIN_PROTOCOL.md']['sha256'],
              'parent_fits_sha256':sha(parent),'fixed_external_newtonian_SI':E}
    write_json(directory/'FOLLOWUP_MARGIN_FREEZE.json',freeze)
    return directory, freeze


def fresh_rows():
    rows = []
    for i, A in enumerate(([4.,9.],[1.],[16.,25.,36.])):
        A = np.array(A)
        rows.append({'name':f'synthetic_{i}', 'R':np.arange(1,len(A)+1,dtype=float),
                     'A':A,'low':.81*A,'high':1.21*A,'g_N':A.copy(),
                     'K':np.zeros((len(A),20)), 'operator_receipt_sha256':f'synthetic-receipt-{i}'})
    return rows


def margin_lp_checks(margin, fit):
    saved_out, saved_training = fit.operator.OUT, fit.training_rows
    saved_solver, real_constraint = margin.linprog, fit.constraints
    saved_scan = fit.external_scan
    results = []
    try:
        fit.external_scan = lambda *a,**k: (_ for _ in ()).throw(AssertionError('E must not be scanned'))
        for label, low, high, baseline, coeff, expected in [
                ('positive_margin',.81,1.21,.7,1.,(.2,.31)),
                ('zero_error',1.,1.,1.,1.,(0.,0.)),
                ('infeasible',1.,1.,2.,0.,None)]:
            directory, freeze = fixture('lp_'+label)
            fit.operator.OUT = directory
            K = np.zeros((1,20)); K[0,0] = coeff
            rows = [{'name':'analytic_row','A':np.ones(1),'low':np.array([low]),
                     'high':np.array([high]),'g_N':np.array([baseline]),'K':K,
                     'R':np.ones(1),'operator_receipt_sha256':'synthetic-operator'}]
            fit.training_rows = lambda:rows
            calls = []
            def capture(c,**kw):
                calls.append({'c':c.copy(),'M':kw['A_ub'].copy(),'b':kw['b_ub'].copy(),'bounds':kw['bounds']})
                return saved_solver(c,**kw)
            margin.linprog = capture
            output = directory/'candidate.json'
            run_main(margin,['--output',output],directory/'stdout.txt')
            result = json.loads(output.read_text())
            assert result['external_newtonian_SI'] == freeze['fixed_external_newtonian_SI']
            assert result['numerical_candidate_validation_required'] is True
            assert np.array_equal(calls[0]['c'],np.r_[np.zeros(20),-1.])
            original,b,q = real_constraint(rows,True,freeze['fixed_external_newtonian_SI'],True)
            M = calls[0]['M']; E = freeze['fixed_external_newtonian_SI']
            assert np.array_equal(M[:,:20],original[:,:20])
            assert np.array_equal(calls[0]['b'],b)
            assert np.array_equal(M[2:-3,-1],np.zeros(21))
            trial = np.r_[np.linspace(0,.015,20),.037]
            force = baseline + float((K@trial[:20])[0])
            ge = E*(1+sum(float(w)*max(0.,min(1.,math.log(float(hi)/E)/math.log(float(hi/lo))))
                    for w,lo,hi in zip(trial[:20],fit.operator.KNOTS[:-1],fit.operator.KNOTS[1:])))
            physical = np.array([force + trial[-1]-high, low+trial[-1]-force,
                (ge + trial[-1]*(fit.EXTERNAL[1]-fit.EXTERNAL[0])/2-fit.EXTERNAL[1])/E,
                (fit.EXTERNAL[0]+trial[-1]*(fit.EXTERNAL[1]-fit.EXTERNAL[0])/2-ge)/E,
                float(q@trial[:20])/fit.QMAX+trial[-1]-1])
            residual = M@trial-calls[0]['b']
            assert np.max(np.abs(residual[[0,1,-3,-2,-1]]-physical)) < 6e-15
            if expected is None:
                assert result['status']==2 and len(calls)==1 and 'weights' not in result
            else:
                assert result['status']==0 and len(calls)==2
                z,w = expected
                assert abs(result['primary_max_z']-z)<1e-10
                assert abs(result['secondary_z']-max(0.,z-1e-8))<1e-10
                assert abs(result['weights'][0]-max(0.,w-1e-8))<1e-10
                assert max(abs(x) for x in result['weights'][1:])<1e-10
                assert np.array_equal(calls[1]['c'],np.r_[np.ones(20),0.])
                assert np.array_equal(calls[1]['M'][-1],np.r_[np.zeros(20),-1.])
                assert abs(calls[1]['b'][-1]+z-1e-8)<1e-10
            results.append({'fixture':label,'status':result['status'],
                            'primary_z':result.get('primary_max_z'),
                            'secondary_z':result.get('secondary_z'),
                            'independent_physical_residual_error':float(np.max(np.abs(residual[[0,1,-3,-2,-1]]-physical)))})
    finally:
        fit.operator.OUT,fit.training_rows = saved_out,saved_training
        margin.linprog,fit.external_scan = saved_solver,saved_scan
    return results


def readout_checks(readout, fit):
    directory,_ = fixture('readout')
    rows = fresh_rows()
    base = [[1.41,.71],[1.215],[1.05,1.05,1.05]]
    refined = [[1.435,.81],[1.225],[.77,.77,.77]]
    boundary = [[1.,1.31],[1.205],[1.09,1.09,1.09]]
    matrix = [[.81,1.21],[1.],[1.,1.,1.]]
    methods = ['base_direct_force','refined_direct_force','extended_boundary_force','matrix_force']
    factors = dict(zip(methods,[base,refined,boundary,matrix]))
    labels = ['D_regular','D_negative','D_tiny']
    candidate = {'status':0,'primary_minimum_t':0.,'fitted_t':1e-8,
                 'predicted_external_physical_SI':2.32e-10,'Q2_s_minus2':1e-28}
    fits = {'protocol_sha256':fit.operator.PROTOCOL_HASH,'cases':[
        {'family':'D','constraints':x,'best_sampled':candidate} for x in ['regular','negative','tiny']] + [
        {'family':'D','constraints':'missing','best_sampled':None},
        {'family':'D','constraints':'failed','best_sampled':{'status':2}}]}
    fits_path = directory/'fits.json'; write_json(fits_path,fits)
    groups = []
    expected = {}
    for i,row in enumerate(rows):
        all_fields = {}
        for label in labels:
            fields = {'passed': label != 'D_negative'}
            for method in methods:
                force = row['A']*np.array(factors[method][i]) if label=='D_regular' else row['A'].copy()
                if label=='D_negative' and i==0 and method=='base_direct_force': force[0] = -1.
                if label=='D_tiny' and i==0 and method=='base_direct_force': force[0] = row['high'][0]+1e-12*row['A'][0]
                fields[method] = force.tolist()
                needed = [max(0.,(float(F)-float(H))/float(A),(float(L)-float(F))/float(A))
                          for F,H,L,A in zip(force,row['high'],row['low'],row['A'])]
                score = None if min(force)<=0 else math.sqrt(sum((math.log10(float(F)/float(A))/2)**2
                          for F,A in zip(force,row['A']))/len(force))
                expected[(label,i,method)] = (needed,score)
            all_fields[label] = fields
        groups.append({'name':row['name'],'R_kpc':row['R'].tolist(),'candidate_results':all_fields})
    validation = {'fits_sha256':sha(fits_path),'rows':groups,
                  'candidate_passes':{l:l!='D_negative' for l in labels}}
    validation_path = directory/'validation.json'; write_json(validation_path,validation)
    saved = fit.training_rows; fit.training_rows = lambda:rows
    try:
        output = directory/'results.json'
        run_main(readout,['--fits',fits_path,'--validation',validation_path,'--output',output],directory/'stdout.txt')
    finally:
        fit.training_rows = saved
    result = json.loads(output.read_text()); summaries=[]
    for case in result['cases'][:3]:
        label = case['label']
        for method in methods:
            expt = max(max(expected[label,i,method][0]) for i in range(3))
            assert abs(case['required_t_by_force_method'][method]-expt)<1e-15
            sq = [expected[label,i,method][1] for i in range(3)]
            aggregate = None if None in sq else math.sqrt(sum(s*s for s in sq)/3)
            actual = case['equal_galaxy_rms_log10_velocity'][method]
            assert actual is aggregate if aggregate is None else abs(actual-aggregate)<2e-15
            for i,row in enumerate(case['per_galaxy']):
                assert np.max(np.abs(np.array(row['scores'][method]['required_t_by_row'])-expected[label,i,method][0]))<1e-15
        assert case['largest_direct_required_t']==max(case['required_t_by_force_method'][x] for x in methods[:3])
        summaries.append({k:v for k,v in case.items() if k not in ['per_galaxy']})
    assert abs(result['cases'][0]['largest_direct_required_t']-.225)<1e-15
    assert result['cases'][2]['largest_direct_required_t']>0
    assert all(not c['candidate_available'] for c in result['cases'][3:])
    return summaries


def validator_checks(validate, old_validator, fit):
    saved = (fit.operator.OUT,fit.training_rows,fit.operator.galaxy_geometry,
             fit.operator.LinearProjection,old_validator.boundary_extension,fit.constraints)
    cases = ['clean','tight_rectangles','numerical_failure','negative_force',
             'external_failure','solar_failure','missing_cache','weight_mutation']
    results = []
    try:
        for case in cases:
            directory,freeze = fixture('validate_'+case,3e-10 if case=='external_failure' else 2.32e-10)
            rows = fresh_rows()
            if case=='tight_rectangles':
                for row in rows: row['low'],row['high']=(1-.0005)**2*row['A'],(1+.0005)**2*row['A']
            weights = np.zeros(20); weights[0]=.2
            candidate = {'status':0,'protocol_sha256':freeze['protocol_sha256'],
                         'source_sha256':SOURCES['direct_margin_candidate.py']['sha256'],
                         'parent_fits_sha256':freeze['parent_fits_sha256'],
                         'external_newtonian_SI':freeze['fixed_external_newtonian_SI'],
                         'weights':weights.tolist(),
                         'operator_receipts':{r['name']:r['operator_receipt_sha256'] for r in rows}}
            candidate_path = directory/'candidate.json'; write_json(candidate_path,candidate)
            for row in rows:
                for tag in ['base','refined','boundary_extension']:
                    if case=='missing_cache' and row is rows[0] and tag=='boundary_extension': continue
                    (directory/f"newtonian_field_{row['name']}_{tag}.npz").write_bytes(b'ONLY SYNTHETIC CACHE')
                    write_json(directory/f"newtonian_field_{row['name']}_{tag}.json",{'synthetic':True})
            fit.operator.OUT=directory; fit.training_rows=lambda:rows
            calls=[]; seen_weights=[]
            def geometry(name,tag='base',refine=False):
                calls.append([name,tag,refine]); return {'name':name,'tag':tag},{'synthetic':True},None
            def boundary(name,data,receipt):
                return {'name':name,'tag':'boundary_extension'}
            class Projection:
                def __init__(self,data): self.data=data
                def combined(self,w):
                    seen_weights.append(w.tobytes())
                    if case=='weight_mutation': w[0]+=.0001
                    row=next(r for r in rows if r['name']==self.data['name'])
                    multiplier={'base':1.002,'refined':1.004,'boundary_extension':1.003}[self.data['tag']]
                    if case=='numerical_failure': multiplier=1.01
                    force=multiplier*row['A']
                    if case=='negative_force': force[0]=-1.
                    return force
            fit.operator.galaxy_geometry=geometry; fit.operator.LinearProjection=Projection
            old_validator.boundary_extension=boundary
            real_constraints=saved[-1]
            def constraints(*a,**k):
                M,b,q=real_constraints(*a,**k)
                if case=='solar_failure': q=q.copy();q[0]=2*fit.QMAX/.2
                return M,b,q
            fit.constraints=constraints
            output=directory/'validation.json'
            rejected=False
            try:
                run_main(validate,['--candidate',candidate_path,'--output',output],directory/'stdout.txt')
            except AssertionError:
                rejected=True
            if case in ['missing_cache','weight_mutation']:
                assert rejected and not output.exists()
                if case=='missing_cache': assert calls==[]
                results.append({'fixture':case,'assertion_rejected':True,'geometry_calls':len(calls)})
                continue
            assert not rejected
            result=json.loads(output.read_text())
            assert result['passed'] is (case=='clean')
            assert len(calls)==6 and len(seen_weights)==9 and all(w==weights.tobytes() for w in seen_weights)
            if case=='tight_rectangles':
                assert result['numerical_pass'] and not result['direct_original_galaxy_rectangles_pass']
            if case=='numerical_failure':
                assert not result['numerical_pass'] and result['direct_original_galaxy_rectangles_pass']
            if case=='external_failure': assert not result['external_rectangle_pass']
            if case=='solar_failure': assert not result['solar_rectangle_pass']
            results.append({'fixture':case,'passed':result['passed'],
                            'numerical_pass':result['numerical_pass'],
                            'direct_rectangles_pass':result['direct_original_galaxy_rectangles_pass'],
                            'external_pass':result['external_rectangle_pass'],
                            'solar_pass':result['solar_rectangle_pass'],
                            'unchanged_weight_calls':len(seen_weights)})
    finally:
        (fit.operator.OUT,fit.training_rows,fit.operator.galaxy_geometry,
         fit.operator.LinearProjection,old_validator.boundary_extension,fit.constraints)=saved
    return results


def scalar_symbol_checks():
    # Entirely independent one-ramp function and inversion, no author helper.
    low,high,c=.2,2.,.5
    weight=c*math.log(high/low)
    def N(A):
        return 1+weight*max(0.,min(1.,math.log(high/A)/math.log(high/low)))
    def A_of_g(g):
        if g<=low*N(low): return g/N(low)
        if g>=high: return g
        return brentq(lambda A:A*N(A)-g,low,high,xtol=2e-14)
    eta=np.diag([-1.,1.,1.,1.])
    def current(p):
        g=math.sqrt(float(p@eta@p))
        return (eta@p)/N(A_of_g(g))
    checks=[]
    for A in [.05,.35,1.,1.8,3.]:
        g=A*N(A); mu=1/N(A)
        D=N(A)-c if low<A<high else N(A)
        mup=c/(A*N(A)**2*D) if low<A<high else 0.
        for direction in [np.array([1.,0.,0.]),np.array([1.,2.,3.])/math.sqrt(14)]:
            p=np.r_[0.,g*direction]; raised=eta@p
            expected=mu*eta+(mup/g)*np.outer(raised,raised)
            h=1e-5*g
            measured=np.column_stack([(current(p+h*np.eye(4)[j])-current(p-h*np.eye(4)[j]))/(2*h) for j in range(4)])
            error=float(np.max(np.abs(measured-expected)))
            assert error<4e-9
            assert abs(g*mu-A)<2e-15
            spatial=expected[1:,1:]
            assert abs(float(direction@spatial@direction)-1/D)<2e-15
            speed2=float(direction@spatial@direction)/(-expected[0,0])
            assert abs(speed2-N(A)/D)<2e-15
            assert abs(float(np.linalg.det(expected))+mu**3/D)<3e-15
            checks.append({'A':A,'rotated':bool(direction[1]!=0),'finite_difference_error':error,
                           'mu':mu,'D':D,'radial_speed_squared':speed2})
    grid=np.geomspace(low*(1+1e-8),high*(1-1e-8),101)
    speed=np.array([N(a)/(N(a)-c) for a in grid])
    assert np.all(np.diff(speed)>0) and 0<2-speed[-1]<3e-8
    return {'checks':checks,'upper_knot_one_sided_supremum':2.,
            'near_upper_value':float(speed[-1]),'interpretation':'Static spacelike symbol only; no transfer of QUMOND fits.'}


def main():
    guard();start=time.monotonic()
    operator=subject('direct_galaxy_response_operator')
    solar=subject('direct_response_basis')
    fit=subject('direct_shared_response_fit')
    old_validator=subject('direct_validate_inverse_fields')
    margin=subject('direct_margin_candidate')
    validate=subject('direct_validate_margin')
    readout=subject('direct_inverse_results')
    # A hard trap also catches any accidental attempt at a real source solve.
    operator.field.RingField=lambda *a,**k: (_ for _ in ()).throw(AssertionError('No field solves permitted'))
    checks={'margin_lp':margin_lp_checks(margin,fit),
            'actual_field_readout':readout_checks(readout,fit),
            'margin_validator':validator_checks(validate,old_validator,fit),
            'single_scalar_symbol':scalar_symbol_checks()}
    guard()
    result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,
            'scope':'Synthetic/source checks only; no real galaxy fields or empirical fits.',
            'source_sha256':sha(__file__),'snapshot_manifest_sha256':sha(OUT/'snapshot_manifest_v1.json'),
            'elapsed_seconds':time.monotonic()-start,
            'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            'checks':checks}
    write_json(OUT/'synthetic_checks_v1.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))


if __name__=='__main__':main()
