"""Read-only released-source correspondence; never imports or executes author code."""
from pathlib import Path
import ast,hashlib,itertools,json,math,subprocess
ROOT=Path(__file__).resolve().parent
A=ROOT/'post_sources/author'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def verify(name,condition,**data):
    assert condition,(name,data)
    row=dict(name=name,verified=True,**data);checks.append(row)
    print(json.dumps(row,sort_keys=True))
pre=json.loads((ROOT/'PRE_SEAL.json').read_text())
verify('PRE_seal_identity',sha(ROOT/'PRE_SEAL.json')=='3acf0388bdfdcad3ee4d5b829eeff1d0a65509c36d732b8ad9b449c415793196')
for m in pre['members']:
    p=ROOT/m['path'];assert p.stat().st_size==m['bytes'] and sha(p)==m['sha256'],m['path']
verify('all_PRE_members_preserved',len(pre['members'])==29,member_count=29)
pins=json.loads((ROOT/'POST_SOURCE_PINS.json').read_text())
for row in pins['sources']:
    dest=ROOT/row['frozen_path'];origin=Path(row['origin'])
    verify('released_copy_'+dest.name,sha(origin)==sha(dest)==row['sha256'] and dest.stat().st_size==row['bytes'])
seal=json.loads((A/'AUTHOR_CONTROL_SEAL.json').read_text())
verify('author_seal_seven_members',len(seal['files'])==7 and all(sha(A/name)==digest for name,digest in seal['files'].items()))
refs=json.loads((ROOT/'POST_REFERENCE_PINS.json').read_text())
verify('primary_reference_bindings',len(refs['sources'])==2 and all(sha(ROOT/x['frozen_path'])==x['sha256'] and (ROOT/x['frozen_path']).stat().st_size==x['bytes'] for x in refs['sources']),pdf_pages=refs['pdf_pages'])
authorpins=json.loads((A/'SOURCE_PINS.json').read_text())
repo=ROOT.parent/'campaign-working'
for src in authorpins['sources']:
    origin=Path(src['path'])
    if 'git_revision' in src:
        relative=str(origin.relative_to(repo))
        b=subprocess.check_output(['git','show',src['git_revision']+':'+relative],cwd=repo)
        verify('author_git_pin_'+origin.name,hashlib.sha256(b).hexdigest()==src['sha256'],commit=src['git_revision'])
    elif 'url' in src:
        verify('author_primary_pdf_pin',src['sha256']==sha(ROOT/'post_sources/reference/barthel_kliesch_1111.4210v2.pdf'))
    else:
        verify('author_prior_pin_'+origin.parent.name+'_'+origin.name,sha(origin)==src['sha256'])
result=json.loads((A/'LOCAL_BACKGROUND_CONTROL_RESULTS.json').read_text())
execution=json.loads((A/'CONTROL_EXECUTION.json').read_text())
verify('complete_stdout_equals_result',(A/'CONTROL.stdout.txt').read_bytes()==(A/'LOCAL_BACKGROUND_CONTROL_RESULTS.json').read_bytes())
verify('empty_stderr_and_zero_exit',(A/'CONTROL.stderr.txt').stat().st_size==0 and execution['exit_code']==0)
verify('author_script_fingerprints',sha(A/'local_background_controls.py')==result['script_sha256']==execution['script_sha256'])
verify('author_command_binding',Path(execution['command'][1]).name=='local_background_controls.py' and sha(Path(execution['command'][1]))==execution['script_sha256'])
ast.parse((A/'local_background_controls.py').read_text())
verify('author_source_parses_without_execution',True)
rotor=result['diagonal_rotor']
verify('four_rotor_rows',rotor['first_shift_energy_difference']=='2*x - 2*y + 1' and [r['cutoff'] for r in rotor['rows']]==[1,2,4,8])
for row in rotor['rows']:
    L=row['cutoff'];expected=2*abs(math.sin(.173))
    verify('rotor_record_arithmetic_'+str(L),row['valid_far_shift_columns']==4*L*L*(2*L+1)
           and row['far_commutator_norm']==0 and abs(row['near_commutator_norm']-expected)<1e-13
           and row['near_exact_norm']==expected,expected_columns=4*L*L*(2*L+1),expected_near_norm=expected)
rows=result['chain_rows']
expected=set(itertools.product([3,4,5,6],[0.,3.,30.],[.2,.7]))
verify('all_24_declared_chain_rows',len(rows)==24 and {(r['sites'],r['K'],r['time']) for r in rows}==expected)
for r in rows:
    assert r['delta']==.4 and r['kappa']==.07
    q=abs(r['summed_disturbance_integral_20']-r['summed_disturbance_integral_32'])
    assert r['quadrature_difference']==q
    assert abs(r['global_trivial_bound']-2*r['kappa']*(r['sites']-1)*r['time'])<1e-15
    assert r['local_observable_full_vs_hamiltonian_norm']<=r['summed_disturbance_integral_32']+max(1e-10,3*q)
    assert r['local_observable_full_vs_hamiltonian_norm']<=r['global_trivial_bound']+1e-10
verify('all_recorded_chain_arithmetic',True,max_quadrature_difference=max(r['quadrature_difference'] for r in rows),
       min_unadjusted_integral_margin=min(r['summed_disturbance_integral_32']-r['local_observable_full_vs_hamiltonian_norm'] for r in rows),
       max_local_observable_error=max(r['local_observable_full_vs_hamiltonian_norm'] for r in rows))
verify('declared_author_summary',result['all_assertions_passed'] and execution['elapsed_wall_seconds']==3.9454514579847455
       and max(r['quadrature_difference'] for r in rows)<1.44e-8,
       wall_seconds=execution['elapsed_wall_seconds'],internal_seconds=result['elapsed_seconds'],numpy=result['numpy'],scipy=result['scipy'])
note=(A/'LOCAL_RECORD_BACKGROUND_STABILITY_ROOT.md').read_text()
verify('frozen_editorial_typo_retained','chain length,+electric coefficient' in note)
verify('no_count_variance_or_lag_rate_import','not the quantitative first-pair bin estimate' in note and 'count variance' in note)
out=dict(scope='Exact source and recorded-number correspondence; author dynamics and quadrature not independently executed.',
         check_count=len(checks),checks=checks,script_sha256=sha(Path(__file__)))
(ROOT/'POST_CHECK_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print('TOTAL',len(checks),'POST correspondence checks verified')
