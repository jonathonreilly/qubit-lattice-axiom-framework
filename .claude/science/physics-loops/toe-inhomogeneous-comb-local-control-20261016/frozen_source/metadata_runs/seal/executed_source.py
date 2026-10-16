"""Seal already inspected source artifacts and actual metadata receipts only."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys
D=Path(__file__).resolve().parent;P=D/'proposal';PK='.claude/science/physics-loops/toe-inhomogeneous-comb-local-control-20261016'
run=D/'metadata_runs/seal';run.mkdir(parents=True,exist_ok=False)
def utc():return datetime.now(timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':sha(b)}
def dump(p,v):p.write_text(json.dumps(v,indent=2)+'\n')
start=utc();cap=run/'executed_source.py';cap.write_bytes(Path(__file__).read_bytes())
launch={'kind':'source_packet_byte_seal_only','argv':list(sys.orig_argv),'cwd':str(D),'started_utc':start,'source_at_launch':pin(cap),'scientific_programs_run':0}
dump(run/'LAUNCH.json',launch)
source_rows=json.loads((P/PK/'SOURCE_MANIFEST.json').read_text())['sources']
authority=[]
for row in source_rows:
 if not row['source'].startswith('authority/'):continue
 rel=row['source'][len('authority/'):];d=run/('authority_'+str(len(authority)));d.mkdir()
 argv=['git','show','dd16171663343dbdeb21adea70ab5e08b3a3a8df:'+rel];t=utc()
 r=subprocess.run(argv,cwd=D.parent.parent/'correlation_worktree',capture_output=True,timeout=30)
 (d/'stdout').write_bytes(r.stdout);(d/'stderr').write_bytes(r.stderr)
 receipt={'kind':'read-only pinned-methodology-source comparison','argv':argv,'cwd':str(D.parent.parent/'correlation_worktree'),'started_utc':t,'finished_utc':utc(),'exit_code':r.returncode,'stdout':pin(d/'stdout'),'stderr':pin(d/'stderr')}
 dump(d/'EXECUTION.json',receipt)
 assert r.returncode==0 and r.stderr==b'' and sha(r.stdout)==row['sha256']
 authority.append({'source':row['source'],'sha256':row['sha256'],'exact_main_object_match':True})
for mode in ['build','inspection','inspection_02']:
 d=D/'metadata_runs'/mode;r=json.loads((d/'EXECUTION.json').read_text());l=json.loads((d/'LAUNCH.json').read_text())
 assert all(r[k]==v for k,v in l.items())
 assert r['exit_code']==0 and r['timed_out'] is False and r['scientific_programs_run']==0 and r['inputs_unchanged_after_run'] is True
 for key in ['child_source_at_launch','recorder_at_launch','input_identities_at_launch','stdout','stderr']:
  assert pin(Path(r[key]['path']))==r[key],(mode,key)
 assert (d/'stderr').read_bytes()==b''
manifest=json.loads((P/PK/'INPUT_MANIFEST.json').read_text())
for row in manifest['inputs']:
 b=(P/row['path']).read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
maps=json.loads((P/PK/'BODY_MAP.json').read_text())['bodies']
template=(D/'primary_template.py').read_text();generated=template.replace('__MANIFEST_SHA256__',sha((P/PK/'INPUT_MANIFEST.json').read_bytes())).replace('__AUDIT_INPUT_PATHS__',repr([r['path'] for r in manifest['inputs']]+[PK+'/INPUT_MANIFEST.json'])).replace('__EXPECTED_BODIES__',repr({r['name']:r['sha256'] for r in maps}))
assert (P/'scripts/inhomogeneous_comb_local_control_2026_10_16.py').read_bytes()==generated.encode()
v=json.loads((D/'VERIFICATION.json').read_text());assert v['mathematics_tested_by_this_execution'] is False and all(x['rejected'] for x in v['scoped_metadata_mutants'])
assert v==json.loads((D/'metadata_runs/inspection_02/stdout').read_text())
assert (D/'SEAL_STDOUT.txt').read_bytes()==b'' and (D/'SEAL_STDERR.txt').read_bytes()==b''
receipt={**launch,'exit_code':0,'finished_utc':utc(),'stdout':pin(D/'SEAL_STDOUT.txt'),'stderr':pin(D/'SEAL_STDERR.txt'),'source_unchanged_after':Path(__file__).read_bytes()==cap.read_bytes()}
dump(run/'EXECUTION.json',receipt)
dump(D/'SEAL_VERIFICATION.json',{'utc':utc(),'proposal_input_files_verified':len(manifest['inputs']),'unchanged_bodies':len(maps),'metadata_run_receipts_verified':['build','inspection','inspection_02'],'pinned_methodology_source_comparisons':authority,'current_generated_primary_matches_template':True,'scientific_programs_run':0,'retained_audit':False})
members=[]
for p in sorted(D.rglob('*')):
 if p.is_file() and p.name!='FREEZE.json':
  b=p.read_bytes();members.append({'path':str(p.relative_to(D)),'bytes':len(b),'sha256':sha(b)})
dump(D/'FREEZE.json',{'kind':'source_only_qualified_comb_uniform_word_publication_draft','frozen_utc':utc(),'scientific_programs_run_this_draft':0,'historical_scientific_replays':0,'canonical_integration':None,'current_base':None,'primary_execution':None,'publication':None,'root_source_wrapper_review':None,'retained_audit':None,'members':members})
