"""Static source/evidence recheck and freeze; does not execute science."""
from pathlib import Path
import datetime, hashlib, json, subprocess
D=Path(__file__).resolve().parent
W=D.parent.parent/'correlation_worktree'
def sha(data): return hashlib.sha256(data).hexdigest()
def row(p):
    data=p.read_bytes()
    return {'path':str(p.relative_to(D)),'sha256':sha(data),'bytes':len(data)}
def write(name,data):
    (D/name).write_text(json.dumps(data,indent=2)+'\n')
for p in D.rglob('*.py'): compile(p.read_text(),str(p),'exec')
manifest=json.loads((D/'SOURCE_MANIFEST.json').read_text())
sources=[]
for item in manifest['sources']:
    data=(D/item['snapshot']).read_bytes()
    assert sha(data)==item['sha256'] and len(data)==item['bytes']
    if 'commit' in item:
        original=subprocess.check_output(['git','show',item['commit']+':'+item['repository_path']],cwd=W)
        authority=item['commit']+':'+item['repository_path']
    else:
        original=Path(item['original_path']).read_bytes(); authority=item['original_path']
    assert original==data
    sources.append({'snapshot':item['snapshot'],'authority':authority,'sha256':sha(data),'equal':True})
pre=json.loads((D/'attempt_01/PRELAUNCH.json').read_text())
receipt=json.loads((D/'attempt_01/RECEIPT.json').read_text())
out=json.loads((D/'attempt_01/stdout.json').read_text())
assert sha((D/'attempt_01/PRELAUNCH.json').read_bytes())==receipt['prelaunch_sha256']
for item in pre['bindings']:
    data=Path(item['path']).read_bytes()
    assert sha(data)==item['sha256'] and len(data)==item['bytes']
assert receipt['exit_code']==0 and not receipt['timed_out']
assert all(x['hash_and_bytes_equal'] and x['generation_equal'] for x in receipt['postchecks'])
assert len(out['checks'])==103
assert (D/'check_family.py').read_bytes()==(D/'attempt_01/check_family.py').read_bytes()
for key in ['stdout','stderr']:
    p=Path(receipt[key]['path']); assert sha(p.read_bytes())==receipt[key]['sha256']
assert (D/'attempt_01/stderr.txt').read_bytes()==b''
write('SOURCE_RECHECK.json',{'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_pairs':sources,'prelaunch_bindings_rechecked':len(pre['bindings']),'all_equal':True,'source_authority':'Repository inputs matched their pinned Git objects, regardless of the current moving worktree; later moment inputs matched frozen originals. No fetch or Git mutation.'})
write('RUN_SUMMARY.json',{
    'status':'Frozen unreviewed author candidate; independent analytical review and root qualification are next',
    'candidate':row(D/'CANDIDATE.md'),'resource_plan':row(D/'RESOURCE_PLAN.json'),
    'source_manifest':row(D/'SOURCE_MANIFEST.json'),
    'executed_script':row(D/'attempt_01/check_family.py'),
    'prelaunch':row(D/'attempt_01/PRELAUNCH.json'),'receipt':row(D/'attempt_01/RECEIPT.json'),
    'stdout':row(D/'attempt_01/stdout.json'),'stderr':row(D/'attempt_01/stderr.txt'),
    'scientific_attempts':1,'scientific_failures':0,'exact_assertions_recorded':len(out['checks']),
    'caps':receipt['actual_caps'],'wall_seconds':receipt['wall_seconds'],
    'user_cpu_seconds':receipt['child_user_cpu_seconds'],'system_cpu_seconds':receipt['child_system_cpu_seconds'],
    'matrix_dimension':0,'source_snapshots':len(sources),'prelaunch_bindings':len(pre['bindings']),
    'proposed_scope':out['parameters'],'proposed_budgets':out['budgets'],
    'new_load_bearing_step':'Arctan identity and analytic reference-mass lower bound; full kappa-family majorants and actual profile premises re-established.',
    'failed_route':'Naive old variance substitution produces mass ceiling 32/25 at kappa=1e-8 and cannot normalize the new envelope; preserved.',
    'independence':'Author computation with substantial prior source exposure and same model; no independent acceptance inferred.',
    'canonical_execution':False,'publication_or_audit':False,'editable_prompt_changes':[],
    'writes':'This packet only; no worktree, Git, shared checkpoint, source, axiom or audit changes.'})
files=[row(p) for p in sorted(D.rglob('*')) if p.is_file() and p.name not in ['FILE_MANIFEST.json','FREEZE.json']]
write('FILE_MANIFEST.json',{'files':files,'count':len(files),'scope':'All packet files except this manifest and the freeze record'})
freeze={'frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status':'Author candidate only; independent review pending',
    'candidate':row(D/'CANDIDATE.md'),'file_manifest':row(D/'FILE_MANIFEST.json'),
    'source_manifest':row(D/'SOURCE_MANIFEST.json'),'scientific_result':row(D/'attempt_01/stdout.json'),
    'execution_receipt':row(D/'attempt_01/RECEIPT.json'),'run_summary':row(D/'RUN_SUMMARY.json'),
    'member_count_excluding_manifest_and_freeze':len(files),
    'next_decision':'Separate analytical review of mass lower bound, directional normalization, full seed overlap, kappa-majorant transfer and actual-profile/finite-clock interfaces. No permission to infer joint-box, native, practical, retained or arbitrary-accuracy status.'}
write('FREEZE.json',freeze)
for item in files:
    assert row(D/item['path'])==item
print(json.dumps({'candidate':row(D/'CANDIDATE.md'),'freeze':row(D/'FREEZE.json'),'manifest':row(D/'FILE_MANIFEST.json'),'members':len(files),'all_static_bindings_verified':True},indent=2))
