"""Coordinator reproduction: two reviewed bridges and one covariance author.
Exact JSON comparison, excluding only the two declared covariance timings.
These are reproductions of already executed diagnostics, not new reviews.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, sys, tempfile, time

L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof'); C=L/'checks'
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,indent=2)+'\n')
pins={
 'review_crossover_import_receipt.json':('ad4df40b8d9df19a531c901c80b2ff8a561e24edf8299b696efb860917e25aab','artifacts'),
 'review_euclidean_rotation_freeze.json':('3107a2b1990f804bd60f00037107625f2b1d9f92b0f0027bc2870cee6e95341c','owned_artifacts'),
 'soft_fluctuation_receipt.json':('fb712adf789f689e078789d07b74237236eed7dc8db942d8763bad9c2c4a4bd1','files'),
}
records=[]
for name,(expected,key) in pins.items():
    raw=(C/name).read_bytes(); assert sha(raw)==expected,name
    rows=json.loads(raw)[key]+[{'path':str(C/name),'sha256':expected}]
    for row in rows:
        path=row['path']; revision=None
        if path==str(L/'SOFT_FLUCTUATION_COVARIANCE_ASTRA.md'):
            revision='86400dbc2ad09b0cf9c6bd9453a8e788a20f46cd'
            b=subprocess.check_output(['git','show',revision+':'+path])
        else:b=Path(path).read_bytes()
        assert sha(b)==row['sha256'],path
        records.append({'path':path,'sha256':sha(b),'revision':revision})
sources={
 'CROSSOVER_LITERATURE_BRIDGE_ASTRA.md':'c0f118a5228fffd8c2841d0a254328d722c4083629427ffd176a8fc4747b835a',
 'EUCLIDEAN_ROTATION_IMPORT_ASTRA.md':'513e44546c5147caa44479c616937994f46aab09764a9808a87f3edddb05e294',
 'SOFT_FLUCTUATION_COVARIANCE_ASTRA.md':'327d033b22281f5f727c018ccb9b1d23d8f7d131bd3633602d6655a9b3de2403',
}
for name,h in sources.items(): assert sha((L/name).read_bytes())==h,name
dump(C/'full_proof_bridge_reviews_bindings.json',{'created_utc':datetime.now(timezone.utc).isoformat(),'artifacts':records,'corrected_live_sources':sources,'scope':'Frozen review packets and covariance author packet; exact original covariance source retained at its recorded revision.'})
jobs=[
 ('crossover_independent','review_crossover_import_independent_02.py',[],'review_crossover_import_independent_02.stdout.json',False),
 ('crossover_mark','review_crossover_import_mark_admission.py',[],'review_crossover_import_mark_admission_01.stdout.json',False),
 ('rotation_independent','review_euclidean_rotation_independent.py',[],'review_euclidean_rotation_attempt01.stdout.json',False),
 ('rotation_matrix','review_euclidean_rotation_matrix_mutations_attempt02.py',[],'review_euclidean_rotation_matrix_mutations_attempt02.stdout.json',False),
 ('rotation_controls','review_euclidean_rotation_additional_controls.py',[],'review_euclidean_rotation_additional_controls.stdout.json',False),
 ('covariance_author','soft_fluctuation_check.py',['--mode','all'],'soft_fluctuation_all_02.json',True),
 ('tree_group_author','soft_fluctuation_tree_group.py',[],'soft_fluctuation_tree_group_02.json',True),
]
work=Path(tempfile.mkdtemp(prefix='ym-bridge-root-replay-'))
def run(job):
    label,script,args,reference,timing=job;dest=work/label;dest.mkdir()
    names=[script]+(['euclidean_rotation_import_exact.py'] if label in ['rotation_matrix','rotation_controls'] else [])
    copied={}
    for name in names:
        shutil.copy2(C/name,dest/name);copied[name]=sha((dest/name).read_bytes())
        assert copied[name]==sha((C/name).read_bytes())
    start=time.time();p=subprocess.run([sys.executable,script,*args],cwd=dest,capture_output=True)
    out=C/('full_proof_bridge_'+label+'_out.json');err=C/('full_proof_bridge_'+label+'_err.txt')
    assert not out.exists() and not err.exists();out.write_bytes(p.stdout);err.write_bytes(p.stderr)
    rb=(C/reference).read_bytes();r={'label':label,'command':[sys.executable,script,*args],'copies':copied,'temporary_directory':str(dest),'exit_code':p.returncode,'wall_seconds':time.time()-start,'stdout':str(out),'stderr':str(err),'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr),'reference':str(C/reference),'reference_sha256':sha(rb),'excluded_top_level_field':'elapsed_seconds' if timing else None}
    try:
        actual,expected=json.loads(p.stdout),json.loads(rb)
        if timing:actual.pop('elapsed_seconds');expected.pop('elapsed_seconds')
        r['exact_non_time_json_match']=actual==expected
        r['differing_top_level_keys']=sorted(k for k in actual.keys()|expected.keys() if actual.get(k)!=expected.get(k))
    except Exception as e:r.update(comparison_error=repr(e),exact_non_time_json_match=False)
    r['source_and_reference_unchanged']=all(sha((C/n).read_bytes())==h for n,h in copied.items()) and sha((C/reference).read_bytes())==sha(rb)
    dump(C/('full_proof_bridge_'+label+'_replay.json'),r)
    print(json.dumps({k:r[k] for k in ['label','exit_code','exact_non_time_json_match','wall_seconds']}),flush=True)
    return r
runs=[]
with ThreadPoolExecutor(max_workers=3) as pool:
    for future in as_completed([pool.submit(run,j) for j in jobs]):runs.append(future.result())
for row in records:
    raw=subprocess.check_output(['git','show',row['revision']+':'+row['path']]) if row['revision'] else Path(row['path']).read_bytes()
    assert sha(raw)==row['sha256'],row['path']
for n,h in sources.items():assert sha((L/n).read_bytes())==h,n
ok=all(r['exit_code']==0 and r['stderr_sha256']==sha(b'') and r['exact_non_time_json_match'] and r['source_and_reference_unchanged'] for r in runs)
dump(C/'full_proof_bridge_reviews_replay_summary.json',{'created_utc':datetime.now(timezone.utc).isoformat(),'all_ok':ok,'runs':sorted(runs,key=lambda r:r['label']),'frozen_artifact_records':len(records),'scope':'Five reviewed-bridge diagnostic reproductions and two covariance-author reproductions. This adds no independent proof review or continuum theorem.'})
print(json.dumps({'all_ok':ok,'runs':len(runs),'artifact_records':len(records)}),flush=True)
assert ok
