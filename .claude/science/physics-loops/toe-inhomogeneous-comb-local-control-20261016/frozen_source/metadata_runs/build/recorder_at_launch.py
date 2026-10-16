"""Bounded metadata launcher, adapted from the preserved joint-energy recorder."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess,sys,time
D=Path(__file__).resolve().parent;N=D.parent;W=N.parent/'correlation_worktree'
mode=sys.argv[1];assert mode in {'build','inspection'}
source=D/({'build':'build_packet.py','inspection':'inspect_packet.py'}[mode])
run=D/'metadata_runs'/mode;run.mkdir(parents=True,exist_ok=False)
sha=lambda b:hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
capture=run/'executed_source.py';capture.write_bytes(source.read_bytes())
recorder=run/'recorder_at_launch.py';recorder.write_bytes(Path(__file__).read_bytes())
input_paths={p for p in D.rglob('*') if p.is_file() and 'metadata_runs' not in p.relative_to(D).parts and p.name not in {'BUILD_RESULT.json','VERIFICATION.json','REUSE_AND_READ_MAP.json'}}
if mode=='build':
 tree=ast.parse(source.read_text());roots=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='ROOTS' for t in n.targets))
 for folder in roots:
  f=N/folder/'FREEZE.json';input_paths.add(f);v=json.loads(f.read_text())
  for row in v.get('members',v.get('files',[])):
   p=Path(row['path']);input_paths.add(p if p.is_absolute() else N/folder/p)
 for run_name in ['unequal_fixed_word_acceptance','uniform_word_acceptance']:
  input_paths.update(p for p in (N/'runs'/run_name).iterdir() if p.is_file())
 input_paths.add(N/'review_run.py')
 for name in ['primary_template.py','record_metadata.py']:input_paths.add(N/'bus_joint_energy_publication_draft'/name)
 for rel in ['docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md','docs/ai_methodology/skills/ai-physics-lane-builder/SKILL.md','docs/ai_methodology/skills/workhorse/SKILL.md','docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md','docs/WRITING_VOICE_GUIDE_2026-04-25.md']:input_paths.add(W/rel)
inputs=[pin(p) for p in sorted(input_paths)]
(run/'INPUT_IDENTITIES_AT_LAUNCH.json').write_text(json.dumps(inputs,indent=2)+'\n')
argv=[sys.executable,'-B',str(capture),str(D)]
r={'kind':'publication_packaging_metadata_only','argv':argv,'cwd':str(D),'started_utc':datetime.now(timezone.utc).isoformat(),'timeout_seconds':60,'child_source_at_launch':pin(capture),'original_source_at_launch':pin(source),'recorder_at_launch':pin(recorder),'input_identities_at_launch':pin(run/'INPUT_IDENTITIES_AT_LAUNCH.json'),'scientific_programs_run':0}
(run/'LAUNCH.json').write_text(json.dumps(r,indent=2)+'\n');t=time.monotonic()
with (run/'stdout').open('wb') as out,(run/'stderr').open('wb') as err:
 try:
  p=subprocess.run(argv,cwd=D,stdin=subprocess.DEVNULL,stdout=out,stderr=err,timeout=60);r.update(exit_code=p.returncode,timed_out=False)
 except subprocess.TimeoutExpired:r.update(exit_code=124,timed_out=True)
r.update(finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-t,stdout=pin(run/'stdout'),stderr=pin(run/'stderr'),inputs_unchanged_after_run=all(pin(Path(x['path']))==x for x in inputs))
(run/'EXECUTION.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2));sys.exit(r['exit_code'])
