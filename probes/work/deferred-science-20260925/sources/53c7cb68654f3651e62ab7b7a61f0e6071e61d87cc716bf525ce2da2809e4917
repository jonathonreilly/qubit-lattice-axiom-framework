"""Released-source binding and decimal checks of stored root34 tables.

No author module is imported or executed. No matrix exponential or eigensystem
is recomputed. Author-reported direct numerical residuals remain author evidence.
"""
from pathlib import Path
from decimal import Decimal, getcontext
from datetime import datetime, timezone
import ast
import hashlib
import json
import subprocess

getcontext().prec = 100
HERE = Path(__file__).resolve().parent
FROZEN = HERE/'post_frozen_author'
D = Decimal


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def relative(left, right):
    return abs(left-right)/max(D(1),abs(left),abs(right))


def main():
    pre_path = HERE/'PRE_SEAL.json'
    assert sha(pre_path) == '75bdc5d36dad74adf96285cefb0896539466f4e14c179cecc30f9afe5dbbf4ca'
    pre = load(pre_path)
    for row in pre['members']:
        p=HERE/row['path']
        assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
    assert len(pre['members'])==25
    pins=load(HERE/'POST_SOURCE_PINS.json')
    for row in pins['sources']:
        origin,frozen=Path(row['origin']),HERE/row['frozen']
        assert sha(origin)==sha(frozen)==row['sha256']
        assert origin.stat().st_size==frozen.stat().st_size==row['bytes']
    assert len(pins['sources'])==10
    author=load(FROZEN/'AUTHOR_SEAL.json')
    assert sha(FROZEN/'AUTHOR_SEAL.json')=='e59ad86d86b40ac23bf8bf9e3ed656865587041760fde772fe3b664a785f4e68'
    for name,row in author['files'].items():
        assert sha(FROZEN/name)==row['sha256'] and (FROZEN/name).stat().st_size==row['bytes']
    assert len(author['files'])==8
    parent_checks=[]
    for row in load(FROZEN/'SOURCE_PINS.json')['sources']:
        original=Path(row['path']);repo=HERE.parent/'campaign-working'
        relative_path=original.relative_to(repo)
        blob=subprocess.run(['git','show',row['revision']+':'+str(relative_path)],cwd=repo,
                            capture_output=True,check=True).stdout
        assert hashlib.sha256(blob).hexdigest()==row['sha256']==sha(original)==sha(HERE/'sources'/relative_path)
        parent_checks.append({'path':str(relative_path),'revision':row['revision'],
                              'sha256':row['sha256'],'bytes':len(blob)})
    code=FROZEN/'finite_window_energy_controls.py'
    tree=ast.parse(code.read_text())
    functions=[n.name for n in ast.walk(tree) if isinstance(n,ast.FunctionDef)]
    assert functions==['string','complex_pair','spectrum','main']
    data=load(FROZEN/'FINITE_WINDOW_ENERGY_RESULTS.json')
    execution=load(FROZEN/'EXECUTION.json')
    assert (FROZEN/'CONTROL.stdout').read_bytes()==(FROZEN/'FINITE_WINDOW_ENERGY_RESULTS.json').read_bytes()
    assert data['source_sha256']==execution['code_sha256']==sha(code)
    assert execution['stdout_sha256']==sha(FROZEN/'CONTROL.stdout')
    assert execution['stderr_sha256']==sha(FROZEN/'CONTROL.stderr')
    assert execution['stdout_bytes']==(FROZEN/'CONTROL.stdout').stat().st_size
    assert execution['stderr_bytes']==0 and (FROZEN/'CONTROL.stderr').stat().st_size==0
    assert execution['exit_code']==0 and data['precision_digits']==80
    assert data['original_lattice_simulation'] is False
    specs=data['spectrum_rows'];counts=data['first_event_rows'];responses=data['response_rows']
    assert len(specs)==10 and len(counts)==15 and len(responses)==25
    eps=sorted({r['epsilon'] for r in specs},key=D)
    assert len(eps)==5
    assert {(r['epsilon'],r['number_sector']) for r in specs}=={(e,n) for e in eps for n in (0,2)}
    maxima={k:D(0) for k in ('spectral_trace','spectral_product','mean','variance','weight_scale',
                             'event_difference','event_target','characteristic_difference','characteristic_bound',
                             'soft_response','interior_probability')}
    by_epsilon={}
    for row in specs:
        a,c,e=map(D,(row['a'],row['c'],row['epsilon']))
        low,high,w=map(D,(row['low_energy'],row['high_energy'],row['high_weight']))
        assert 0<low<high and 0<w<1
        z=1+(a*a+c)*e*e
        targets={
            'spectral_trace':(low+high,z/e**4),
            'spectral_product':(low*high,c*a*a/e**4),
            'mean':((1-w)*low+w*high,D(row['mean'])),
            'variance':((1-w)*(low-D(row['mean']))**2+w*(high-D(row['mean']))**2,D(row['variance'])),
            'weight_scale':(w/(a*a*e*e),D(row['high_weight_over_a_squared_epsilon_squared']))}
        assert relative(D(row['mean']),a*a/e**2)<D('1e-54')
        assert relative(D(row['variance']),a*a/e**6)<D('1e-54')
        assert relative(D(row['limiting_energy']),c*a*a)<D('1e-54')
        for key,(x,y) in targets.items():
            residual=relative(x,y);maxima[key]=max(maxima[key],residual)
            assert residual<D('1e-54'),(key,row)
        for field in ('direct_eigenvalue_error','mean_formula_error'):
            assert D(row[field])<D('1e-65')
        for field in ('direct_weight_error','variance_formula_relative_error'):
            assert D(row[field])<D('1e-70')
        if row['number_sector']==2:
            assert low<D('2.4')<high
            by_epsilon[row['epsilon']]=(low,high,w)
    assert {(r['epsilon'],r['window']) for r in counts}=={(e,b) for e in eps for b in ('0.15','0.6','1.3')}
    for row in counts:
        actual,target,difference=map(D,(row['actual_first_event_probability'],row['effective_probability'],row['difference']))
        assert 0<actual<1 and 0<target<1
        err=relative(actual-target,difference);maxima['event_difference']=max(maxima['event_difference'],err)
        assert err<D('1e-54')
        exact_target=1-(-D('0.7')*D(row['window'])).exp()
        err=relative(target,exact_target);maxima['event_target']=max(maxima['event_target'],err)
        assert err<D('1e-54')
    char_rows=[r for r in responses if 'time_parameter' in r]
    soft_rows=[r for r in responses if 'soft_response' in r]
    assert len(char_rows)==20 and len(soft_rows)==5
    assert all(sum(r['epsilon']==e for r in char_rows)==4 for e in eps)
    for row in char_rows:
        low,high,w=by_epsilon[row['epsilon']]
        x,y=map(D,row['characteristic']);tx,ty=map(D,row['target_characteristic'])
        error=((x-tx)**2+(y-ty)**2).sqrt()
        err=relative(error,D(row['convergence_error']));maxima['characteristic_difference']=max(maxima['characteristic_difference'],err)
        assert err<D('1e-54')
        bound=2*w+abs(D(row['time_parameter']))*abs(low-D('2.4'))
        err=relative(bound,D(row['proved_error_bound']));maxima['characteristic_bound']=max(maxima['characteristic_bound'],err)
        assert err<D('1e-54') and error<=bound+D('1e-54')
        assert D(row['direct_exponential_error'])<D('1e-65')
    for row in soft_rows:
        low,high,w=by_epsilon[row['epsilon']]
        soft=(1-w)/(1+(low-D('2.4'))**2)+w/(1+(high-D('2.4'))**2)
        err=relative(soft,D(row['soft_response']));maxima['soft_response']=max(maxima['soft_response'],err)
        assert err<D('1e-54')
        assert D(row['sharp_half_line_at_limit_probability'])==w
        assert D(row['sharp_half_line_target_atom_probability'])==1
        interior=(1-w if abs(low-D('2.4'))<D('0.1') else D(0))+(w if abs(high-D('2.4'))<D('0.1') else D(0))
        err=relative(interior,D(row['fixed_point_one_half_width_interval_probability']))
        maxima['interior_probability']=max(maxima['interior_probability'],err)
        assert err<D('1e-54')
    reported={field:max((D(r[field]) for r in specs)) for field in
              ('direct_eigenvalue_error','direct_weight_error','mean_formula_error','variance_formula_relative_error')}
    reported['direct_exponential_error']=max(D(r['direct_exponential_error']) for r in char_rows)
    return {'checked_utc':datetime.now(timezone.utc).isoformat(),'checker_sha256':sha(Path(__file__)),
        'scope':__doc__,'PRE_seal_sha256':sha(pre_path),'PRE_members_unchanged':25,
        'released_source_origins_verified':10,'author_members_verified':8,
        'parent_bindings':parent_checks,'author_AST_functions':functions,
        'author_execution':execution,'author_internal_elapsed_seconds':data['elapsed_seconds'],
        'row_counts':{'spectrum':10,'first_event':15,'characteristic':20,'soft_and_interval':5},
        'printed_digit_tolerance_relative':'1e-54; author output prints 60 significant digits from 80-digit calculations',
        'own_stored_arithmetic_maxima':{k:str(v) for k,v in maxima.items()},
        'maxima_of_reported_author_direct_residuals_not_recomputed':{k:str(v) for k,v in reported.items()},
        'exact_original_root_note_sha256':sha(FROZEN/'FINITE_WINDOW_MICROSCOPIC_ENERGY_MEASURES_ROOT.md'),
        'separate_magnetic_correction_sha256':sha(FROZEN/'FINITE_WINDOW_ENERGY_MAGNETIC_SUM_CORRECTION.md'),
        'generic_model_not_original_lattice':True,'independent_numerical_replication':False,
        'author_programs_imported_or_executed':[],'other_active_packets_opened':[],
        'failures':[]}


if __name__=='__main__':
    print(json.dumps(main(),indent=2,allow_nan=False))
