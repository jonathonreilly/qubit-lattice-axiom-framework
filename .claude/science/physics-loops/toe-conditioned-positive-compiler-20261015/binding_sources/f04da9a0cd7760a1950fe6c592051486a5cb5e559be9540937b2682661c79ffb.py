from pathlib import Path
import ast,datetime,hashlib,json
N=Path(__file__).resolve().parents[1];D=N/'conditioned_positive_compiler_publication_draft';S=D/'proposal';W=N.parent/'correlation_worktree';R=N/'conditioned_positive_compiler_publication_root_review'
P='.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015';NOTE='docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md';H='scripts/conditioned_positive_time_compiler_2026_10_15.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def rawsame(b,r):assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
def write(p,v):assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
f=read(D/'FINAL_FREEZE.json');assert pin(D/'FINAL_FREEZE.json')['sha256']=='137a053a187876c9540c9a2f3efcc60d03af6cb2b5da28398c86b86d8981e3fa' and len(f['files'])==247
for r in f['files']:same(r['path'],r)
assert {str(p) for p in D.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{str(D/'FINAL_FREEZE.json')}
note=(S/NOTE).read_bytes();bodies=read(S/P/'BODY_MAP.json')['bodies'];assert len(bodies)==3 and note.startswith((D/'wrapper.md').read_bytes())
for r in bodies:
 b=note[r['start_byte_inclusive']:r['end_byte_exclusive']];rawsame(b,r);assert note.count(b)==1
sources=read(S/P/'SOURCE_MANIFEST.json')['sources'];assert len(sources)==84
for r in sources:
 loc=r['recovery']
 if loc['kind']=='blob':b=(S/loc['path']).read_bytes()
 elif loc['kind']=='external_pinned':b=(W/loc['path']).read_bytes()
 else:
  p=S/loc['container']
  if not p.exists():p=W/loc['container']
  b=p.read_bytes()[loc['start_byte_inclusive']:loc['end_byte_exclusive']]
 rawsame(b,r)
 if loc['kind']=='body_interval':
  body=next(b for b in bodies if b['name']==loc['body_name'])
  assert all(loc[k]==body[k] for k in ('container','start_byte_inclusive','end_byte_exclusive')) and all(r[k]==body[k] for k in ('bytes','sha256'))
for m in read(S/P/'RECOVERY_SELECTION.json')['members']:
 loc=m.get('recovery')
 if loc is not None:assert any(m['sha256']==r['sha256'] and m['bytes']==r['bytes'] and loc==r['recovery'] for r in sources)
objects=read(S/P/'ARCHIVE_INDEX.json')['objects'];assert len(objects)==63
assert {o['sha256'] for o in objects}=={s['sha256'] for s in sources if s['recovery']['kind']=='blob'}
for o in objects:same(S/o['path'],o)
parents=read(S/P/'DEPENDENCIES.json')['dependencies'];assert len(parents)==1
for r in parents:
 same(W/r['path'],r)
 for b in r['accepted_body_intervals']+r['review_evidence']:rawsame((W/b['container']).read_bytes()[b['start_byte_inclusive']:b['end_byte_exclusive']],b)
assert parents[0]['required_mathematical_body_names']==['compiler_author']
manifest=read(S/P/'INPUT_MANIFEST.json');[same(S/r['path'],r) for r in manifest['inputs']]
primary=(S/H).read_text();a=ast.parse(primary);names={'AUDIT_INPUT_PATHS','MANIFEST_SHA256','EXPECTED_BODIES','EXPECTED_PARENT_BODIES','EXPECTED_PARENT_REVIEWS','EXPECTED_PARENTS','EXPECTED_ACCEPTANCES','EXPECTED_GIT_BASE','EXPECTED_BASE_PR','EXPECTED_BASE_BRANCH'}
literal={n.targets[0].id:ast.literal_eval(n.value) for n in a.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in names}
assert literal['EXPECTED_GIT_BASE'] is literal['EXPECTED_BASE_PR'] is literal['EXPECTED_BASE_BRANCH'] is None
assert set(literal['AUDIT_INPUT_PATHS'])=={r['path'] for r in manifest['inputs']}|{P+'/INPUT_MANIFEST.json',P+'/ACTUAL_BINDING.json'}|{r['path'] for r in parents}
expected=(D/'primary_template.py').read_text()
for key in ('MANIFEST_SHA256','AUDIT_INPUT_PATHS','EXPECTED_BODIES','EXPECTED_PARENT_BODIES','EXPECTED_PARENT_REVIEWS','EXPECTED_PARENTS','EXPECTED_ACCEPTANCES'):
 expected=expected.replace('__'+key+'__',literal[key] if key=='MANIFEST_SHA256' else repr(literal[key]))
assert primary==expected.rstrip()+'\n' and literal['MANIFEST_SHA256']==pin(S/P/'INPUT_MANIFEST.json')['sha256']
reuse=read(D/'REUSE_MAP.json');exact=0
for r in reuse['functions']:
 if r.get('byte_exact_reuse',False):
  for label,folder in [('current',D),('reference',D/'reference_scripts')]:
   p=folder/r['script'];text=p.read_text();n=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==r['function']);b=''.join(text.splitlines(keepends=True)[n.lineno-1:n.end_lineno]).encode();rawsame(b,r[label])
  exact+=1
receipts=[]
for label in ('prepare','build','build_final','inspection_final','inspection_final_current'):
 p=D/'metadata_runs'/label/'EXECUTION.json';r=read(p);assert r['exit_code']==0 and r['scientific_execution'] is False
 for k in ('stdout','stderr','child_source_at_launch','recorder','launch'):same(r[k]['path'],r[k])
 for row in read(r['launch']['path'])['inputs']:
  same(row['captured']['path'],row['captured']);assert row['captured']['sha256']==row['original']['sha256']
 assert Path(r['stderr']['path']).read_bytes()==b'';receipts.append(pin(p))
for row in read(D/'SOURCE_FRESHNESS.json')['identities']:same(row['original'],row)
freezes=[]
for relative,digest in read(D/'SELECTED_FREEZES.json'):
 p=N/relative;assert pin(p)['sha256']==digest;seal=read(p);rows=seal['files'] if 'files' in seal else seal['members']
 for row in rows:same(p.parent/row['path'],row)
 freezes.append({'freeze':pin(p),'members':len(rows)})
state=read(S/P/'PUBLICATION_STATE.json');assert state['autonomous_clock_imported'] is False
for key in ('canonical_binding','git_base','primary_execution','cache_execution','mutation_execution','graph_execution','publication_action','retained_audit'):assert state[key] is None
for row in read(D/'PARENT_METADATA_ORIGINS.json')['sources']:
 for key in ('original','copy'):same(row[key]['path'],row[key])
review={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'root_source_publication_review','root_read_complete':True,'source_draft_freeze':pin(D/'FINAL_FREEZE.json'),'note':pin(S/NOTE),'primary':pin(S/H),'body_pins':bodies,'parents':parents,'existing_source_acceptances':{'conditioned_compiler':pin(N/'conditioned_positive_compiler_root_review/ACCEPTANCE.md')},'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.','current_files_reviewed_with_exact_reuse':[pin(D/x) for x in ('wrapper.md','build_proposal.py','primary_template.py','inspect_proposal.py','seal_packet.py','prepare_sources.py','record_metadata.py')]+[pin(p) for p in sorted((D/'packet_text').glob('*'))],'read_scope':'Complete current wrapper and nine packet texts read. Complete changed builder, inspector, seal, recorder, preparation and primary logic read; repeated unchanged functions reused at verified exact identities. Aggregate truncated changed-code display repaired by complete affected inspector/recorder/seal and builder-final ranges. Three mathematical bodies and compiler parent proof/review reuse exact prior complete reading. Full freeze/source/body/recovery/receipt integrity verified; no new scientific calculation or independent verdict.','prior_root_metadata_failure':{'receipt':pin(N/'runs/conditioned_publication_review_2114/EXECUTION.json'),'reason':'Root verifier assumed files key for every nested freeze; protected/comparison freezes use members. No source decision was written. Corrected reader preserves both schemas.'},'metadata_receipts':receipts,'selected_source_freezes':freezes,'exact_helper_functions':exact,'qualification_scope':['Root supplied-log and protected finite-grid recipes remain distinct; actual quantitative augmented certificate and fixed finite plant supplied.','Product targets compose augmented pairs before reconstructing total aging; window target exp(-isH) W exp(-iTH) with full scalar phase.','Operator-norm root recurrence test and larger Frobenius protected test are not interchangeable; rational root durations versus computable protected durations remain distinct.','Full pulse/time/action/calibration/slew/work/moment costs and all outputs retained. Fixed-certificate bounds are not uniform as coupling/conditioning changes, nor polynomial in qubit count or oracle runtime.','Accuracy-scaled coupling, autonomous implementation, native suppliers, common caps, permanent stopping, pure-memory restoration and physical identification excluded.'],'scientific_programs_run':0,'primary_runs':0,'historical_programs_replayed':0,'editable_prompt_files_changed':[]}
write(R/'ACCEPTANCE.json',review);write(R/'FINAL_FREEZE.json',{'utc':review['utc'],'files':[pin(R/'ACCEPTANCE.json')],'scope':'Actual root publication-source review only'})
print(json.dumps({'review':pin(R/'ACCEPTANCE.json'),'freeze':pin(R/'FINAL_FREEZE.json'),'members':247,'sources':84,'exact_functions':exact}))
