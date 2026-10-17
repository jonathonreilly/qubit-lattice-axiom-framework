"""Bounded metadata launcher; never execute either historical scientific program."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess,sys,time
D=Path(__file__).resolve().parent;N=D.parent
mode=sys.argv[1];assert mode in {'prepare','build','inspection','seal'}
source=D/({'prepare':'prepare_sources.py','build':'build_packet.py','inspection':'inspect_packet.py','seal':'seal_packet.py'}[mode])
label=sys.argv[2] if len(sys.argv)>2 else mode
assert label.replace('_','').isalnum() and '/' not in label
assert not (D/'FINAL_FREEZE.json').exists(),'Frozen packet is immutable'
run=D/'metadata_runs'/label;run.mkdir(parents=True,exist_ok=False)
sha=lambda b:hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
capture=run/'executed_source.py';capture.write_bytes(source.read_bytes())
recorder=run/'recorder_at_launch.py';recorder.write_bytes(Path(__file__).read_bytes())
outputs={'BUILD_RESULT.json','VERIFICATION.json','SEAL_RESULT.json','CODE_REUSE_MAP.json','CODE_FULL_DIFF.patch'}
input_paths={p for p in D.rglob('*') if p.is_file() and 'metadata_runs' not in p.relative_to(D).parts and p.name not in outputs}
if mode=='prepare':
 b=N/'weak_mediator_qualified_publication_draft'
 input_paths.add(b/'FINAL_FREEZE.json')
 for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py','MACHINERY_SOURCE_PINS.json']:
  input_paths.add(b/name)
 for folder in ['metadata_runs/build','metadata_runs/inspection','metadata_runs/seal','methodology']:
  input_paths.update(p for p in (b/folder).rglob('*') if p.is_file())
if mode=='build':
 tree=ast.parse(source.read_text())
 literals={t.id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) for t in n.targets if isinstance(t,ast.Name) and t.id in {'ROOTS','EXTRA_DIRS','EXTRA_FILES'}}
 for folder,(filename,expected,key) in literals['ROOTS'].items():
  f=N/folder/filename;input_paths.add(f);v=json.loads(f.read_text());assert sha(f.read_bytes())==expected
  for row in v[key]:input_paths.add(N/folder/row['path'])
 for folder in literals['EXTRA_DIRS']:input_paths.update(p for p in (N/folder).rglob('*') if p.is_file())
 for path in literals['EXTRA_FILES']:input_paths.add(N/path)
inputs=[pin(p) for p in sorted(input_paths)]
(run/'INPUT_IDENTITIES_AT_LAUNCH.json').write_text(json.dumps(inputs,indent=2)+'\n')
argv=[sys.executable,'-B',str(capture),str(D)]
r={'kind':'publication_packaging_metadata_only','argv':argv,'cwd':str(D),'started_utc':datetime.now(timezone.utc).isoformat(),'timeout_seconds':60,'python_version':sys.version,'child_source_at_launch':pin(capture),'original_source_at_launch':pin(source),'source_capture':pin(capture),'recorder_at_launch':pin(recorder),'input_identities_at_launch':pin(run/'INPUT_IDENTITIES_AT_LAUNCH.json'),'scientific_programs_run':0}
(run/'LAUNCH.json').write_text(json.dumps(r,indent=2)+'\n');t=time.monotonic()
with (run/'stdout').open('wb') as out,(run/'stderr').open('wb') as err:
 try:
  p=subprocess.run(argv,cwd=D,stdin=subprocess.DEVNULL,stdout=out,stderr=err,timeout=60);r.update(exit_code=p.returncode,timed_out=False)
 except subprocess.TimeoutExpired:r.update(exit_code=124,timed_out=True)
r.update(finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t,stdout=pin(run/'stdout'),stderr=pin(run/'stderr'),inputs_unchanged_after_run=all(pin(Path(x['path']))==x for x in inputs))
(run/'EXECUTION.json').write_text(json.dumps(r,indent=2)+'\n')
if mode=='seal' and r['exit_code']==0:
 assert r['inputs_unchanged_after_run'] is True and r['timed_out'] is False
 members=[]
 for p in sorted(D.rglob('*')):
  if p.is_file():
   v=pin(p);v['path']=str(p.relative_to(D));members.append(v)
 frozen={'kind':'source_only_qualified_product_source_mediator_publication_draft','frozen_utc':datetime.now(timezone.utc).isoformat(),'scientific_programs_run_this_draft':0,'historical_scientific_replays':0,'actual_science_acceptances':{'original':'9505e42b907fdb9031f42b02b4609965ef7980af536e9197c4864aba124119f5','pauli_addendum':'c79e410fcae41d3a061cf28bc2ffd45d06093a04dbe88e8961523f292a979cfa'},'source_wrapper_review':None,'source_publication_binding':None,'canonical_integration':None,'current_base':None,'canonical_review':None,'staged_review':None,'primary_execution':None,'publication':None,'retained_audit':None,'members':members}
 (D/'FINAL_FREEZE.json').write_text(json.dumps(frozen,indent=2)+'\n')
 r={'completed_metadata_execution':pin(run/'EXECUTION.json'),'freeze':pin(D/'FINAL_FREEZE.json'),'members':len(members),'exit_code':r['exit_code']}
print(json.dumps(r,indent=2));sys.exit(r['exit_code'])
