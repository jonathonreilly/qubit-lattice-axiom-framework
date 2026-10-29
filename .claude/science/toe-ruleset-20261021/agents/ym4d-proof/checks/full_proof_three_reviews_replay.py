"""Coordinator reproduction and byte binding of three separately reviewed units.
No reviewer/author artifacts are modified. Time fields are excluded only from
output identity, never from preserved raw evidence. This is not another review.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess, sys, tempfile, time
R=Path.cwd()
L=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof')
C=L/'checks'
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(path,data):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(data,indent=2)+'\n')
pins={
 'review_source_history_receipt.json':'6b1e1ff3e62051063182e7d92e0c1b9c6e1dc3fe598ab15f7703a6fec55868f9',
 'review_massgap_block_receipt.json':'b772b4e9497c9108d592eb6a80b95e7cb64d8ecef8782db385dc62b32b944ce4',
 'review_residual_full_colour_receipt.json':'e30df91f8682af55d857295b928e04f9bfa75c77f352ad51f88c2b3521e24d1d'}
receipts={}
for name,h in pins.items():
    b=(C/name).read_bytes();assert sha(b)==h,name
    receipts[name]=json.loads(b)
sr=receipts['review_source_history_receipt.json']
mr=receipts['review_massgap_block_receipt.json']
rr=receipts['review_residual_full_colour_receipt.json']
mm=json.loads(Path(mr['manifest']['path']).read_text())
si=json.loads(Path(sr['input_manifest']['path']).read_text())
rm=json.loads(Path(rr['source_manifest']['path']).read_text())
artifacts=sr['artifacts_excluding_receipt_itself']+mm['artifacts']+rr['commit_ready_artifacts']
artifacts += [{'path':str(C/n),'sha256':h} for n,h in pins.items()]
artifacts += [mr['manifest']]
# Manifest itself is already an artifact for the other two reviewers.
input_records=si['author_bound_records_verified']+si['consumed_science_inputs']+si['current_main_methodology']+si['installed_skills']+mm['source_inputs']+rm['frozen_files_verified']+rm['science_read_coverage']+rm['methodology_reads']+rm['installed_skill_reads']
verified=[]
for rec in artifacts+input_records:
    p=Path(rec['path']);rev=rec.get('revision')
    if rev and re.fullmatch('[0-9a-f]{40}',rev):
        rel=p.relative_to(R) if p.is_absolute() else p
        b=subprocess.check_output(['git','show',rev+':'+str(rel)])
        via='git:'+rev
    else:
        b=p.read_bytes();via='working-files-before-integration-summary-edits'
    actual=sha(b);assert actual==rec['sha256'],(str(p),via,actual,rec['sha256'])
    if 'bytes' in rec: assert len(b)==rec['bytes'],str(p)
    verified.append({'path':str(p),'sha256':actual,'bytes':len(b),'via':via})
unique={}
for rec in artifacts:
    p=Path(rec['path']);p=p.relative_to(R) if p.is_absolute() else p
    assert p.suffix.lower()!='.pdf',p
    unique[str(p)]={'path':str(p),'sha256':rec['sha256']}
excluded=rr['local_only_inputs']+mm['research_caches_not_publication_attachments']
for rec in excluded:
    p=Path(rec.get('path',rec.get('local_only_path')))
    assert str(p) not in unique
    if p.is_file(): assert sha(p.read_bytes())==rec['sha256']
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
dump(C/'full_proof_three_reviews_bindings.json',{
 'created_utc':datetime.now(timezone.utc).isoformat(),'head_before_integration':head,
 'receipt_pins':pins,'verified_records':verified,'verified_record_count':len(verified),
 'commit_ready_artifacts':list(unique.values()),'commit_ready_artifact_count':len(unique),
 'local_only_research_inputs_excluded':excluded,
 'scope':'Byte identity and replay only. Original independent review scope and limitations remain binding.'})
jobs=[]
for e in sr['executions']:
    jobs.append(('source_history_'+e['name'],Path(e['script']['path']),Path(e['stdout']['path'])))
jobs += [('massgap_block',C/'review_massgap_block_independent.py',C/'review_massgap_block_attempt03.stdout.json'),('massgap_literature',C/'review_massgap_block_literature_exact.py',C/'review_massgap_block_literature_results.json')]
for i,e in enumerate(rr['independent_executions'],1):
    jobs.append(('residual_full_colour_'+str(i).zfill(2),Path(e['implementation']['path']),Path(e['stdout']['path'])))
def normalize(v,ignored,path=''):
    if isinstance(v,dict):
        out={}
        for k,x in v.items():
            loc=path+'/'+k
            if k in {'elapsed_seconds','runtime_seconds'}: ignored.add(loc)
            else: out[k]=normalize(x,ignored,loc)
        return out
    if isinstance(v,list):return [normalize(x,ignored,path+'/'+str(i)) for i,x in enumerate(v)]
    return v
def run(job):
    label,script,reference=job
    before=script.read_bytes();expected=reference.read_bytes()
    temp=Path(tempfile.mkdtemp(prefix='ym-three-review-replay-'))
    copy=temp/script.name;copy.write_bytes(before)
    start=datetime.now(timezone.utc).isoformat();t=time.monotonic()
    proc=subprocess.run([sys.executable,str(copy)],cwd=R,capture_output=True)
    end=datetime.now(timezone.utc).isoformat()
    stem=C/('full_proof_'+label+'_review_replay')
    out=Path(str(stem)+'_out.json');err=Path(str(stem)+'_err.txt')
    assert not out.exists() and not err.exists()
    out.write_bytes(proc.stdout);err.write_bytes(proc.stderr)
    ignored=set();match=False;parse_error=None
    try:match=normalize(json.loads(proc.stdout),ignored)==normalize(json.loads(expected),ignored)
    except Exception as exc:parse_error=repr(exc)
    record={'label':label,'script':str(script),'script_sha256':sha(before),
      'reference':str(reference),'reference_sha256':sha(expected),
      'command':[sys.executable,str(copy)],'cwd':str(R),'started_utc':start,'finished_utc':end,
      'elapsed_seconds':time.monotonic()-t,'exit_code':proc.returncode,
      'stdout':{'path':str(out),'sha256':sha(proc.stdout)},'stderr':{'path':str(err),'sha256':sha(proc.stderr),'bytes':len(proc.stderr)},
      'ignored_comparison_fields':sorted(ignored),'all_other_output_fields_identical':match,'parse_error':parse_error,
      'original_script_unchanged':script.read_bytes()==before,'reference_unchanged':reference.read_bytes()==expected,
      'scope':'Coordinator reproduction of independent reviewer evidence; not a new independent review.'}
    dump(Path(str(stem)+'.json'),record)
    print(json.dumps({k:record[k] for k in ['label','exit_code','all_other_output_fields_identical','parse_error']}),flush=True)
    return record
records=[]
with ThreadPoolExecutor(max_workers=4) as pool:
    for f in as_completed([pool.submit(run,j) for j in jobs]):records.append(f.result())
for rec in unique.values(): assert sha(Path(rec['path']).read_bytes())==rec['sha256'],rec['path']
ok=all(r['exit_code']==0 and r['stderr']['bytes']==0 and r['all_other_output_fields_identical'] and r['original_script_unchanged'] and r['reference_unchanged'] for r in records)
dump(C/'full_proof_three_reviews_replay_summary.json',{'created_utc':datetime.now(timezone.utc).isoformat(),'all_ok':ok,'runs':sorted(records,key=lambda x:x['label']),'all_frozen_review_artifacts_unchanged':True,'scientific_scope':'Reproduced finite diagnostic evidence. No full existence or continuum gap claim.'})
print(json.dumps({'all_ok':ok,'runs':len(records),'artifacts':len(unique),'input_and_artifact_bindings':len(verified)}),flush=True)
assert ok
