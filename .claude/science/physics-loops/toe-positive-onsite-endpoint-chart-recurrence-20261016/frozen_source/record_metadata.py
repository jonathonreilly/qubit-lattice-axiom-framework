"""Bounded metadata launcher with actual captures; never run historical science."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess,sys,time
D=Path(__file__).resolve().parent;N=D.parent;W=N.parent/'correlation_worktree'
mode=sys.argv[1];assert mode in {'build','inspection','seal'}
source=D/({'build':'build_packet.py','inspection':'inspect_packet.py','seal':'seal_packet.py'}[mode])
label=sys.argv[2] if len(sys.argv)>2 else mode
assert label.replace('_','').isalnum() and '/' not in label
assert not (D/'FINAL_FREEZE.json').exists(),'Frozen packet is immutable'
run=D/'metadata_runs'/label;run.mkdir(parents=True,exist_ok=False)
sha=lambda b:hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
capture=run/'executed_source.py';capture.write_bytes(source.read_bytes())
recorder=run/'recorder_at_launch.py';recorder.write_bytes(Path(__file__).read_bytes())
outputs={'BUILD_RESULT.json','VERIFICATION.json','SEAL_RESULT.json'}
input_paths={p for p in D.rglob('*') if p.is_file() and 'metadata_runs' not in p.relative_to(D).parts and p.name not in outputs}
if mode=='build':
 tree=ast.parse(source.read_text())
 literals={t.id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) for t in n.targets if isinstance(t,ast.Name) and t.id in {'ROOTS','ROOT_RUNS'}}
 for folder,(filename,expected,selection) in literals['ROOTS'].items():
  f=N/folder/filename;input_paths.add(f);v=json.loads(f.read_text())
  assert sha(f.read_bytes())==expected
  for row in v['members']:
   p=Path(row['path']);input_paths.add(p if p.is_absolute() else N/folder/p)
  for terminal in ['runs/final_freeze','metadata_runs/final_seal']:
   input_paths.update(p for p in (N/folder/terminal).glob('*') if p.is_file())
 for name in literals['ROOT_RUNS']:
  input_paths.update(p for p in (N/'runs'/name).iterdir() if p.is_file())
 for p in list(input_paths):
  if p.name=='EXECUTION.json':
   r=json.loads(p.read_text())
   for key in ['original_source','source_original','source_at_launch','child_source_at_launch','source_capture','recorder_at_launch','recorder','stdout','stderr']:
    if key in r:input_paths.add(Path(r[key]['path']))
inputs=[pin(p) for p in sorted(input_paths)]
(run/'INPUT_IDENTITIES_AT_LAUNCH.json').write_text(json.dumps(inputs,indent=2)+'\n')
argv=[sys.executable,'-B',str(capture),str(D)]
r={'kind':'publication_packaging_metadata_only','argv':argv,'cwd':str(D),'started_utc':datetime.now(timezone.utc).isoformat(),'timeout_seconds':60,'child_source_at_launch':pin(capture),'original_source_at_launch':pin(source),'source_capture':pin(capture),'recorder_at_launch':pin(recorder),'input_identities_at_launch':pin(run/'INPUT_IDENTITIES_AT_LAUNCH.json'),'scientific_programs_run':0}
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
 frozen={'kind':'source_only_qualified_endpoint_chart_recurrence_publication_draft','frozen_utc':datetime.now(timezone.utc).isoformat(),'scientific_programs_run_this_draft':0,'historical_scientific_replays':0,'source_wrapper_review':None,'source_publication_binding':None,'canonical_integration':None,'current_base':None,'canonical_review':None,'primary_execution':None,'publication':None,'retained_audit':None,'members':members}
 (D/'FINAL_FREEZE.json').write_text(json.dumps(frozen,indent=2)+'\n')
 r={'completed_metadata_execution':pin(run/'EXECUTION.json'),'freeze':pin(D/'FINAL_FREEZE.json'),'members':len(members),'exit_code':r['exit_code']}
print(json.dumps(r,indent=2));sys.exit(r['exit_code'])
