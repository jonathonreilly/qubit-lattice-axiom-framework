"""Build one source-only combined packet; never execute historical science."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
D=Path(sys.argv[1]).resolve();N=D.parent
P=D/'proposal';PK='.claude/science/physics-loops/toe-positive-onsite-endpoint-chart-recurrence-20261016'
NOTE='docs/POSITIVE_ONSITE_ENDPOINT_CHART_RECURRENCE_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/positive_onsite_endpoint_chart_recurrence_2026_10_16.py'
ROOTS={
 'endpoint_chart_root_proposal':('FREEZE.json','f0ad2c52437a6ac63e55a8c8d13d2bb7636c76049430653c83c3f55f253f3ccd','complete'),
 'endpoint_chart_certificate_candidate':('FREEZE.json','485d29b8c62083a9d3754a1245ef65889f46cf343f6e76557bfadfe8fe6c37cf','complete'),
 'endpoint_chart_exposed_check':('FINAL_FREEZE.json','dab6af16cf9977a9b20d3438a7db2da68a5ef632bd883c5b0c7b9bd77fceb991','review_selection'),
 'endpoint_chart_root_review':('FREEZE.json','d2c3cce2cde80aad2b105ead8a12671bdc8682d90fdc774fe0737e6390aae223','complete'),
 'endpoint_recurrence_candidate':('FREEZE.json','33f7d3b47e70451af22e3d8058b92b948833ecee4e25f30f746be794d24e1e9c','complete'),
 'endpoint_recurrence_exposed_check':('FINAL_FREEZE.json','453b32503e06a569a361414984b96e808e34b267dec077b209d926fe7ed84204','review_selection'),
 'endpoint_recurrence_root_review':('FREEZE.json','7e4268b5f1a848dda65213917045427fc56b68732a71d1a18c6fb99118b63065','complete'),
}
ROOT_RUNS=['endpoint_chart_selection','endpoint_chart_acceptance','endpoint_recurrence_acceptance']
ACCEPTANCES={
 'endpoint_chart_root_review/ACCEPTANCE.json':'112ecd184bf4e0fbb76814c73bffe0fa911b35ba808825e09bb574c790f6faf7',
 'endpoint_recurrence_root_review/ACCEPTANCE.json':'36e72537f8d2546bc15c9baf69dd526fb22d854bafc36d07a020a7225c73465e',
}
BODIES=[
 ('chart_original_derivation','endpoint_chart_certificate_candidate/DERIVATION.md'),
 ('chart_pre_enclosure_reconstruction','endpoint_chart_exposed_check/PRE_ENCLOSURE_ANALYSIS.md'),
 ('chart_exposed_review','endpoint_chart_exposed_check/REVIEW.md'),
 ('chart_complete_code_review','endpoint_chart_exposed_check/CODE_REVIEW.md'),
 ('chart_controlling_root_qualifications','endpoint_chart_root_review/FINAL_QUALIFICATIONS.md'),
 ('recurrence_original_derivation','endpoint_recurrence_candidate/DERIVATION.md'),
 ('recurrence_exposed_review','endpoint_recurrence_exposed_check/REVIEW.md'),
 ('recurrence_complete_analytic_code_review','endpoint_recurrence_exposed_check/ANALYTIC_CODE_REVIEW.md'),
 ('recurrence_controlling_root_qualifications','endpoint_recurrence_root_review/FINAL_QUALIFICATIONS.md'),
]
sha=lambda b:hashlib.sha256(b).hexdigest()
def put(rel,b):
 p=P/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def js(rel,x):put(rel,(json.dumps(x,indent=2)+'\n').encode())
def ident(b):return {'bytes':len(b),'sha256':sha(b)}
def read(p):return json.loads(p.read_text())
sources={};objects={};freeze_rows=[]
def add(path,alias=None,role='historical_source'):
 path=path.resolve();b=path.read_bytes();alias=alias or str(path.relative_to(N));h=sha(b)
 r={'source':alias,'original_path':str(path),'role':role,**ident(b),'recovery_path':PK+'/archive/sha256/'+h}
 if alias in sources:assert sources[alias]['sha256']==h
 else:sources[alias]=r
 objects[h]={'path':r['recovery_path'],**ident(b)}
 if not (P/r['recovery_path']).exists():put(r['recovery_path'],b)
 return b
assert not P.exists(),'Refuse overwrite of an existing proposal'
for folder,(filename,pin,mode) in ROOTS.items():
 f=N/folder/filename;raw=add(f,role='source_freeze');assert sha(raw)==pin
 rows=read(f)['members'];selected=[]
 assert len({r['path'] for r in rows})==len(rows)
 for row in rows:
  rel=row['path'];path=N/folder/rel;path.resolve().relative_to(N)
  b=path.read_bytes();assert ident(b)=={'bytes':row['bytes'],'sha256':row['sha256']},str(path)
  keep=mode=='complete' or '/' not in rel or rel.startswith(('scoped_runs/','metadata_runs/'))
  if keep:add(path);selected.append(rel)
 for terminal in ['runs/final_freeze','metadata_runs/final_seal']:
  for p in sorted((N/folder/terminal).glob('*')):
   if p.is_file():add(p,role='original_terminal_freeze_evidence')
 freeze_rows.append({'folder':folder,'alias':folder+'/'+filename,'sha256':pin,'members':len(rows),
  'complete_members':mode=='complete','selected_members':selected,'all_original_members_verified_at_build':True})
for name in ROOT_RUNS:
 for p in sorted((N/'runs'/name).iterdir()):
  if p.is_file():add(p,role='actual_root_metadata_or_heuristic_evidence')

# Preserve original paths named by every selected receipt. No result is rerun.
contracts=[];processed=set()
while True:
 pending=[alias for alias in sources if alias.endswith('/EXECUTION.json') and alias not in processed]
 if not pending:break
 for alias in pending:
  processed.add(alias);r=read(Path(sources[alias]['original_path']))
  if 'child_source_at_launch' in r:
   schema='root_original_and_capture';original,capture,recorder='child_source_at_launch','source_capture','recorder';index=1
  else:
   schema='captured_source_execution';original='original_source' if 'original_source' in r else 'source_original'
   capture,recorder='source_at_launch','recorder_at_launch';index=2 if r['argv'][1]=='-B' else 1
  for key in [original,capture,recorder,'stdout','stderr']:
   b=add(Path(r[key]['path']),role='actual_launch_source_or_complete_stream')
   assert ident(b)=={'bytes':r[key]['bytes'],'sha256':r[key]['sha256']}
  assert r['exit_code']==0
  contract={'alias':alias,'schema':schema,'original_key':original,'executed_argv_index':index,
   'exit_code':r['exit_code'],'argv':r['argv'],'source_sha256':r[original]['sha256'],
   'original_alias':str(Path(r[original]['path']).relative_to(N)),
   'capture_alias':str(Path(r[capture]['path']).relative_to(N)),
   'stdout_sha256':r['stdout']['sha256'],'stderr_sha256':r['stderr']['sha256']}
  for key in ['wall_timeout_seconds','timeout_seconds']:
   if key in r:contract[key]=r[key]
  contracts.append(contract)
for alias,h in ACCEPTANCES.items():assert sha((N/alias).read_bytes())==h
note=(D/'packet_text/WRAPPER.md').read_bytes();wrapper_len=len(note);maps=[]
for name,alias in BODIES:
 raw=(N/alias).read_bytes();assert alias in sources
 note+=('\n\n<!-- Unchanged complete source: '+name+' -->\n\n').encode();start=len(note);note+=raw
 maps.append({'name':name,'source':alias,'container':NOTE,'start_byte_inclusive':start,'end_byte_exclusive':len(note),**ident(raw)})
trailer_start=len(note)
note+=b'\n\nPublication scope remains conditional support under the premises and verification limits above; retained status requires the independent audit path.\n'
put(NOTE,note)
js(PK+'/BODY_MAP.json',{'new_wrapper_bytes':[0,wrapper_len],'trailing_wrapper_bytes':[trailer_start,len(note)],'bodies':maps})
js(PK+'/SOURCE_MANIFEST.json',{'schema':'endpoint_chart_recurrence_source_archive_v1','sources':list(sources.values()),
 'archive_rule':'Complete candidate source closures plus bounded review/acceptance selections; no recursive prior publication archives.'})
js(PK+'/ARCHIVE_INDEX.json',{'objects':list(objects.values()),'recursive_prior_publication_archives':False})
js(PK+'/FROZEN_SOURCE_CLOSURE.json',{'roots':freeze_rows})
js(PK+'/EXECUTION_CONTRACTS.json',{'receipts':contracts,'new_scientific_executions':0})
js(PK+'/PARENT_BINDING.json',{'canonical_binding_complete':False,'direct_mathematical_parents':[],
 'internal_argument_dependency':'The recurrence-based universal-duration consequence uses the chart qualified within this combined packet.',
 'git_ancestry_is_not_mathematical_dependency':True})
state={k:None for k in ['source_wrapper_review','source_publication_binding','canonical_integration','current_base_observation','canonical_review','primary_execution','publication_action','retained_audit']}
state.update(scientific_programs_run_this_draft=0,scientific_replays=0)
js(PK+'/PUBLICATION_STATE.json',state)
js(PK+'/ACTUAL_BINDING.json',{'kind':'unbound_source_only_proposal','source_review':None,'base_observation':None,'canonical_review':None,'canonical_parent_binding':None,'publication':None})
for name in ['PR_BODY.md','BINDING_CONTRACT.md','CLAIM_STATUS_CERTIFICATE.md','EVIDENCE_SCOPE.md']:put(PK+'/'+name,(D/'packet_text'/name).read_bytes())
js(PK+'/EXPOSURE.json',{'source_exposed':True,'same_selected_model':True,'blind_independence':False,
 'second_ODE_implementation':False,'new_scientific_executions':0,'historical_scientific_replays':0,
 'historical_author_enclosure_commands':2,'historical_separate_saved_evidence_checks':2,
 'historical_chart_selector_is_heuristic_only':True,'retained_audit':False})
inputs=[]
for p in sorted(P.rglob('*')):
 if p.is_file():inputs.append({'path':str(p.relative_to(P)),**ident(p.read_bytes())})
js(PK+'/INPUT_MANIFEST.json',{'schema':'endpoint_chart_recurrence_publication_inputs_v1','inputs':inputs})
msha=sha((P/PK/'INPUT_MANIFEST.json').read_bytes())
replacements={'__MANIFEST_SHA256__':msha,'__AUDIT_INPUT_PATHS__':repr([r['path'] for r in inputs]+[PK+'/INPUT_MANIFEST.json']),
 '__EXPECTED_BODIES__':repr({r['name']:r['sha256'] for r in maps}),
 '__EXPECTED_FREEZES__':repr({r['alias']:r['sha256'] for r in freeze_rows}),
 '__EXPECTED_ACCEPTANCES__':repr(ACCEPTANCES)}
generated=(D/'primary_template.py').read_text()
for key,value in replacements.items():generated=generated.replace(key,value)
put(SCRIPT,generated.encode())
result={'utc':datetime.now(timezone.utc).isoformat(),'note':NOTE,'note_sha256':sha(note),'primary_sha256':sha(generated.encode()),
 'unchanged_bodies':len(maps),'source_aliases':len(sources),'unique_archive_objects':len(objects),
 'source_receipts':len(contracts),'input_manifest_sha256':msha,'science_executions':0,'canonical_execution':None}
(D/'BUILD_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
