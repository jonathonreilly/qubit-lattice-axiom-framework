"""Seal a reviewed source-only packet using a captured metadata-only validation child."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,time
D=Path(sys.argv[-1]).resolve();P=D/'proposal'
PK='.claude/science/physics-loops/toe-interacting-preparation-control-work-20261016'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=sha(b))
def dump(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
def same(p,r):
 v=pin(p);assert v['bytes']==r['bytes'] and v['sha256']==r['sha256'],str(p)
def validate():
 manifest=json.loads((P/PK/'INPUT_MANIFEST.json').read_text())
 for row in manifest['inputs']:same(P/row['path'],row)
 sources=json.loads((P/PK/'SOURCE_MANIFEST.json').read_text())['sources']
 for row in sources:
  same(Path(row['original_path']),row);same(P/row['recovery_path'],row)
 maps=json.loads((P/PK/'BODY_MAP.json').read_text());note=P/'docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md';raw=note.read_bytes()
 assert raw[:maps['new_wrapper_bytes'][1]]==(D/'packet_text/WRAPPER.md').read_bytes()
 for row in maps['bodies']:
  body=raw[row['start_byte_inclusive']:row['end_byte_exclusive']]
  assert body==(D.parent/row['source']).read_bytes() and sha(body)==row['sha256']
 for mode in ['build','inspection']:
  folder=D/'metadata_runs'/mode;r=json.loads((folder/'EXECUTION.json').read_text());launch=json.loads((folder/'LAUNCH.json').read_text())
  assert all(r[k]==v for k,v in launch.items()) and r['exit_code']==0 and not r['timed_out']
  assert r['inputs_unchanged_after_run'] is True and r['scientific_programs_run']==0
  for k in ['child_source_at_launch','recorder_at_launch','input_identities_at_launch','stdout','stderr']:same(Path(r[k]['path']),r[k])
  same(Path(r['original_source_at_launch']['path']),r['original_source_at_launch'])
  assert (folder/'stderr').read_bytes()==b''
 template=(D/'primary_template.py').read_text()
 generated=template.replace('__MANIFEST_SHA256__',sha((P/PK/'INPUT_MANIFEST.json').read_bytes())).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in manifest['inputs']]+[PK+'/INPUT_MANIFEST.json'])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in maps['bodies']}))
 primary=P/'scripts/interacting_preparation_control_work_2026_10_16.py';assert primary.read_bytes()==generated.encode()
 result=json.loads((D/'VERIFICATION.json').read_text());assert result==json.loads((D/'metadata_runs/inspection/stdout').read_text())
 assert result['mathematics_tested_by_this_execution'] is False and len(result['scoped_metadata_mutants'])==7 and all(x['rejected'] for x in result['scoped_metadata_mutants'])
 reuse=json.loads((D/'REUSE_AND_READ_MAP.json').read_text())
 for row in reuse['exact_function_comparison']:
  assert sha((D/row['name']).read_bytes())==row['new_sha256'] and sha(Path(row['template']).read_bytes())==row['template_sha256']
 out=dict(utc=utc(),kind='final_source_metadata_validation_only',input_files=len(manifest['inputs']),source_aliases=len(sources),unchanged_bodies=len(maps['bodies']),metadata_receipts_verified=['build','inspection'],scoped_refusals=7,current_original_sources_match=True,generated_primary_matches_template=True,scientific_executions=0,source_wrapper_review=None,canonical_integration=None)
 dump(D/'SEAL_VERIFICATION.json',out);print(json.dumps(out,indent=2))
if '--validate' in sys.argv:
 validate();raise SystemExit(0)
assert not (D/'FREEZE.json').exists(),'Refuse re-sealing an existing freeze'
run=D/'metadata_runs/seal';run.mkdir(parents=True,exist_ok=False)
cap=run/'source_and_launcher_at_launch.py';cap.write_bytes(Path(__file__).read_bytes())
argv=[sys.executable,'-B',str(cap),'--validate',str(D)]
launch=dict(kind='source_packet_metadata_seal',launcher_orig_argv=list(sys.orig_argv),argv=argv,cwd=str(D),started_utc=utc(),timeout_seconds=60,source_and_launcher_at_launch=pin(cap),scientific_programs_run=0)
dump(run/'LAUNCH.json',launch);start=time.monotonic()
with (run/'stdout').open('wb') as out,(run/'stderr').open('wb') as err:
 try:
  child=subprocess.run(argv,cwd=D,stdout=out,stderr=err,stdin=subprocess.DEVNULL,timeout=60);code=child.returncode;timeout=False
 except subprocess.TimeoutExpired:code=124;timeout=True
receipt={**launch,'finished_utc':utc(),'exit_code':code,'timed_out':timeout,'elapsed_seconds':time.monotonic()-start,'stdout':pin(run/'stdout'),'stderr':pin(run/'stderr'),'source_unchanged_after':Path(__file__).read_bytes()==cap.read_bytes()}
dump(run/'EXECUTION.json',receipt)
assert code==0 and not timeout and receipt['source_unchanged_after'],receipt
members=[dict(path=str(p.relative_to(D)),bytes=p.stat().st_size,sha256=sha(p.read_bytes())) for p in sorted(D.rglob('*')) if p.is_file() and p!=D/'FREEZE.json']
freeze=dict(kind='source_only_interacting_preparation_control_work_publication_draft',frozen_utc=utc(),member_count=len(members),scientific_programs_run=0,scientific_replays=0,source_wrapper_review=None,source_publication=None,current_base=None,canonical_integration=None,canonical_review=None,primary_execution=None,publication=None,retained_audit=None,editable_prompt_files_changed=[],members=members)
dump(D/'FREEZE.json',freeze)
print(json.dumps(dict(freeze=pin(D/'FREEZE.json'),members=len(members),metadata_exit_code=code,scientific_executions=0),indent=2))
