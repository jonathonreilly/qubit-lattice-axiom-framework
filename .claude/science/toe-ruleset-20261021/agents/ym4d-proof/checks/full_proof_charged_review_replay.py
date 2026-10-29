"""Coordinator reproduction of four frozen charged-jet reviewer invocations.

This is reproduction, not independent mathematical review. Only the declared
elapsed_seconds field in the two stationary-chain runs is excluded from exact
parsed JSON comparison. All mathematical outputs and original evidence remain.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, shutil, subprocess, sys, tempfile, time

L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof'); C=L/'checks'
def sha(data): return hashlib.sha256(data).hexdigest()
def save(path, data):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(data,indent=2)+'\n')
receipt=C/'review_charged_jet_receipt.json'
expected='ad4226851b1b1d7b29e87f19c42c18a021fd8dd7afbfb5a85eeff5007120962d'
assert sha(receipt.read_bytes())==expected
d=json.loads(receipt.read_bytes())
records=d['owned_artifacts']+[{'path':str(receipt),'sha256':expected}]
inputs=[d['source'],*d['supporting_proof_bindings']]
for row in records+inputs: assert sha(Path(row['path']).read_bytes())==row['sha256'],row['path']
save(C/'full_proof_charged_review_bindings.json',{
    'created_utc':datetime.now(timezone.utc).isoformat(), 'artifacts':records,
    'source_and_supporting_proof_inputs':inputs,
    'scope':'Frozen scoped reviewer packet and its explicitly identified load-bearing source files; historical shared-register hashes remain in their original receipts.'})
work=Path(tempfile.mkdtemp(prefix='ym-charged-review-replay-'))
env=os.environ.copy();env.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
jobs=[('n1','review_charged_jet_independent.py',['--depth','1'],'review_charged_jet_n1_02_out.json',True),
      ('n2','review_charged_jet_independent.py',['--depth','2'],'review_charged_jet_n2_01_out.json',True),
      ('su3','review_charged_jet_su3.py',[],'review_charged_jet_su3_01_out.json',False),
      ('gauge','review_charged_jet_gauge.py',[],'review_charged_jet_gauge_01_out.json',False)]
runs=[]
for label,script,args,reference,timing in jobs:
    dest=work/label;dest.mkdir();names={script,'review_charged_jet_independent.py'}
    copied={}
    for name in names:
        shutil.copy2(C/name,dest/name);copied[name]=sha((dest/name).read_bytes())
        assert copied[name]==sha((C/name).read_bytes())
    command=['nice','-n','10',sys.executable,'-B',script,*args]
    started=time.monotonic();p=subprocess.run(command,cwd=dest,env=env,capture_output=True)
    out=C/('full_proof_charged_review_'+label+'_out.json');err=C/('full_proof_charged_review_'+label+'_err.txt')
    assert not out.exists() and not err.exists();out.write_bytes(p.stdout);err.write_bytes(p.stderr)
    actual=json.loads(p.stdout);old=json.loads((C/reference).read_bytes())
    if timing:actual.pop('elapsed_seconds');old.pop('elapsed_seconds')
    r={'label':label,'command':command,'temporary_directory':str(dest),'copied_scripts':copied,
       'environment_overrides':{'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1'},
       'exit_code':p.returncode,'wall_seconds':time.monotonic()-started,
       'excluded_top_level_fields':['elapsed_seconds'] if timing else [],
       'exact_non_time_json_match':actual==old,'passed':actual['passed'],'total':actual['total'],
       'stdout':{'path':str(out),'sha256':sha(p.stdout)},
       'stderr':{'path':str(err),'sha256':sha(p.stderr),'bytes':len(p.stderr)},
       'reference':{'path':str(C/reference),'sha256':sha((C/reference).read_bytes())}}
    save(C/('full_proof_charged_review_'+label+'_replay.json'),r);runs.append(r)
    print(json.dumps({k:r[k] for k in ['label','exit_code','exact_non_time_json_match','passed','total']}),flush=True)
for row in records+inputs: assert sha(Path(row['path']).read_bytes())==row['sha256'],row['path']
ok=all(r['exit_code']==0 and r['exact_non_time_json_match'] and not r['stderr']['bytes'] for r in runs)
save(C/'full_proof_charged_review_replay_summary.json',{
    'created_utc':datetime.now(timezone.utc).isoformat(),'all_ok':ok,'runs':runs,
    'frozen_review_artifact_records':len(records),'source_and_proof_inputs':len(inputs),
    'scope':'Four coordinator reproductions of separately reviewed finite controls. CJ18 and full continuum targets remain OPEN.'})
assert ok
