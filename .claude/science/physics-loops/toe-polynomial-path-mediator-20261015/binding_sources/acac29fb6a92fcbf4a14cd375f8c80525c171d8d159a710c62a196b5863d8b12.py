from pathlib import Path
import ast,datetime,difflib,hashlib,json
N=Path(__file__).resolve().parents[1];D=N/'polynomial_path_mediator_publication_draft';S=D/'proposal';W=N.parent/'correlation_worktree';O=N/'polynomial_path_mediator_publication_root_review'
P='.claude/science/physics-loops/toe-polynomial-path-mediator-20261015';NOTE='docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md';H='scripts/polynomial_path_mediator_2026_10_15.py'
def read(p):return json.loads(Path(p).read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def rawsame(b,r):assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
def same(p,r):rawsame(Path(p).read_bytes(),r)
def resolve(base,p):return Path(p) if Path(p).is_absolute() else base/p
def recover(r):
 loc=r['recovery']
 if loc['kind']=='blob':b=(S/loc['path']).read_bytes()
 elif loc['kind']=='external_pinned':b=(W/loc['path']).read_bytes()
 else:
  p=S/loc['container']
  if not p.exists():p=W/loc['container']
  b=p.read_bytes()[loc['start_byte_inclusive']:loc['end_byte_exclusive']]
 rawsame(b,r);return b
freeze=read(D/'FINAL_FREEZE.json');assert pin(D/'FINAL_FREEZE.json')['sha256']=='922961127462c9856df7728d73e1c9eb885424d6675bb722eb3a99210fcdfb56' and len(freeze['files'])==162
for r in freeze['files']:same(resolve(D,r['path']),r)
assert {str(p) for p in D.rglob('*') if p.is_file()}=={str(resolve(D,r['path'])) for r in freeze['files']}|{str(D/'FINAL_FREEZE.json')}
assert freeze['scientific_programs_run_this_draft']==0 and freeze['historical_root_scientific_fixtures']==1
note=(S/NOTE).read_bytes();bodies=read(S/P/'BODY_MAP.json')['bodies'];assert len(bodies)==3 and note.startswith((D/'wrapper.md').read_bytes())
for r in bodies:
 raw=note[r['start_byte_inclusive']:r['end_byte_exclusive']];rawsame(raw,r);assert note.count(raw)==1
sources=read(S/P/'SOURCE_MANIFEST.json')['sources'];assert len(sources)==87
for r in sources:recover(r)
selection=read(S/P/'RECOVERY_SELECTION.json')
for r in selection['members']:
 if r['recovery'] is not None:
  assert any(r['bytes']==q['bytes'] and r['sha256']==q['sha256'] and r['recovery']==q['recovery'] for q in sources);recover(r)
objects=read(S/P/'ARCHIVE_INDEX.json')['objects'];assert len(objects)==63
assert {r['sha256'] for r in objects}=={r['sha256'] for r in sources if r['recovery']['kind']=='blob'}
for r in objects:same(S/r['path'],r)
parents=read(S/P/'DEPENDENCIES.json')['dependencies'];assert len(parents)==1 and parents[0]['claim_id']=='basis_state_waveform_clock_bounded_theorem_note_2026-10-15'
for r in parents:
 same(W/r['path'],r);assert len(r['accepted_body_intervals'])==3
 for b in r['accepted_body_intervals']:rawsame((W/b['container']).read_bytes()[b['start_byte_inclusive']:b['end_byte_exclusive']],b)
parent_binding=read(S/P/'PARENT_REVIEW_BINDING.json');assert parent_binding['gzip_reviews']==[]
for r in parent_binding['records']:recover(r)
assert parent_binding['publication']==read(N/'publication_integration/basis_state_clock/PUBLICATION.json')
manifest=read(S/P/'INPUT_MANIFEST.json')
for r in manifest['inputs']:same(S/r['path'],r)
primary=(S/H).read_text();names={'AUDIT_INPUT_PATHS','MANIFEST_SHA256','EXPECTED_BODIES','EXPECTED_PARENTS','EXPECTED_PARENT_BODIES','EXPECTED_PARENT_REVIEW','EXPECTED_GIT_BASE','EXPECTED_BASE_PR','EXPECTED_BASE_BRANCH','EXPECTED_ACCEPTANCES'}
literal={n.targets[0].id:ast.literal_eval(n.value) for n in ast.parse(primary).body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in names}
assert literal['EXPECTED_GIT_BASE'] is literal['EXPECTED_BASE_PR'] is literal['EXPECTED_BASE_BRANCH'] is None
expected_paths={r['path'] for r in manifest['inputs']}|{P+'/INPUT_MANIFEST.json',P+'/ACTUAL_BINDING.json'}|{r['path'] for r in parents}
assert set(literal['AUDIT_INPUT_PATHS'])==expected_paths and len(literal['AUDIT_INPUT_PATHS'])==len(expected_paths)==86
expected=(D/'primary_template.py').read_text()
for k in ['MANIFEST_SHA256','AUDIT_INPUT_PATHS','EXPECTED_BODIES','EXPECTED_PARENTS','EXPECTED_PARENT_BODIES','EXPECTED_PARENT_REVIEW']:expected=expected.replace('__'+k+'__',literal[k] if k=='MANIFEST_SHA256' else repr(literal[k]))
assert expected.rstrip()+'\n'==primary and literal['MANIFEST_SHA256']==pin(S/P/'INPUT_MANIFEST.json')['sha256'] and literal['EXPECTED_PARENT_REVIEW']==parent_binding
reuse=read(D/'REUSE_MAP.json');exact=0
for r in reuse['functions']:
 if r['byte_exact_reuse']:
  for label,folder in [('current',D),('reference',D/'reference_scripts')]:
   p=folder/r['script'];t=p.read_text();node=next(n for n in ast.parse(t).body if isinstance(n,ast.FunctionDef) and n.name==r['function']);rawsame(''.join(t.splitlines(keepends=True)[node.lineno-1:node.end_lineno]).encode(),r[label])
  exact+=1
assert exact==27
code_diff=''
for r in reuse['references']:
 p=Path(r['path']);same(p,r);same(D/r['captured'],r)
 code_diff+=''.join(difflib.unified_diff(p.read_text().splitlines(keepends=True),(D/p.name).read_text().splitlines(keepends=True),fromfile='reference/'+p.name,tofile='current/'+p.name))
assert code_diff==(D/'CHANGED_CODE.patch').read_text()
receipts=[]
for label in ['build','inspection']:
 p=D/'metadata_runs'/label/'EXECUTION.json';r=read(p);assert r['exit_code']==0 and not r['scientific_execution'] and not r['timed_out']
 for k in ['child_source_at_launch','recorder','stdout','stderr']:same(r[k]['path'],r[k])
 launch=read(p.parent/'LAUNCH.json');assert len(launch['inputs'])==13
 same(launch['script']['path'],launch['script']);same(launch['source_at_launch']['path'],launch['source_at_launch'])
 for row in launch['inputs']:
  same(row['original']['path'],row['original']);same(row['captured']['path'],row['captured']);assert row['original']['sha256']==row['captured']['sha256']
 assert Path(r['stderr']['path']).read_bytes()==b'';receipts.append(pin(p))
for r in read(D/'SOURCE_FRESHNESS.json')['identities']:same(r['original'],r)
fs=next(ast.literal_eval(x.value) for x in ast.parse((D/'build_proposal.py').read_text()).body if isinstance(x,ast.Assign) and isinstance(x.targets[0],ast.Name) and x.targets[0].id=='FREEZES');checked_freezes=[]
for relative,digest in fs:
 p=N/relative;assert pin(p)['sha256']==digest;x=read(p);members=x.get('files',x.get('members'))
 for r in members:same(resolve(p.parent,r['path']),r)
 checked_freezes.append(dict(freeze=pin(p),members=len(members)))
hist=read(S/P/'HISTORICAL_SCIENCE.json');assert hist['historical_scientific_programs']==1 and not hist['executed_this_draft'] and not hist['comparison_checker_inspected_fixture']
for k in ['results','interpretation','freeze','execution','source','recorder','stdout','stderr']:recover(hist[k])
r=read(N/'runs/polynomial_matrix_fixture_2008/EXECUTION.json');assert r['exit_code']==0
for k,h in [('child_source_at_launch','source'),('recorder','recorder'),('stdout','stdout'),('stderr','stderr')]:rawsame(recover(hist[h]),r[k])
assert json.loads(recover(hist['results']))['scientific_programs_run']==1
state=read(S/P/'PUBLICATION_STATE.json')
for k in ['canonical_binding','git_base','primary_execution','cache_execution','mutation_execution','graph_execution','publication_action','retained_audit']:assert state[k] is None
initial=read(D/'INITIAL_BINDING.json')
for k in ['canonical_parent','parent_publication','parent_review','actual_git_base','actual_binding','actual_primary_run','publication','root_publication_review']:assert initial[k] is None
assert not O.exists();O.mkdir()
review={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'root_source_publication_review','root_read_complete':True,'source_draft_freeze':pin(D/'FINAL_FREEZE.json'),'note':pin(S/NOTE),'primary':pin(S/H),'body_pins':bodies,'parents':parents,'parent_review_binding':parent_binding,'existing_source_acceptances':{'polynomial_path_mediator':pin(N/'polynomial_path_mediator_root_review/ACCEPTANCE.md')},'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.','full_current_files_read':[pin(D/'wrapper.md'),pin(D/'primary_template.py'),pin(D/'record_metadata.py')]+[pin(p) for p in sorted((D/'packet_text').glob('*'))],'changed_code_complete_read':[pin(D/x) for x in ['build_proposal.py','inspect_proposal.py','seal_packet.py','CHANGED_CODE.patch']],'code_reuse':pin(D/'REUSE_MAP.json'),'exact_helper_functions':exact,'metadata_receipts':receipts,'selected_source_freezes':checked_freezes,'read_scope':'Complete current wrapper10sections,9packet texts,primary and recorder; all changed module logic/functions across builder/inspector/seal read with27byte-exact prior helper functions reused. Two truncated aggregate reads were repaired with bounded complete current passages. Three immutable scientific bodies and necessary parent arguments reuse prior full reading at exact pins.162members87sources63blobs and all semantic recovery links, actual receipts and source captures verified. No primary or science execution.','qualification_scope':['Separate mu=m^-3/q=1/m and mu=m^-2/q=sqrt(G) generators and all ledgers.','Minimal clock-size ceiling and bounded sufficient Delta required for accuracy powers; explicit root majorants attributed to exposed comparison.','Complete auxiliary inverse and two-excitation noncommuting corrector, both bare endpoint costs, actual counterterms/scalars and full reference/controller outputs.','Real inverse calibration differs from general full-generator faults; exact unconditional marginal and actual release aging retained.','One historical finite root doubleprecision fixture is exposed sanity evidence; current packaging/review science0/replay0.','Native source, release/calibration/isolation hardware, total compiler complexity, physical identifications, common caps, permanent stop and reuse remain open.'],'scientific_programs_run_this_review':0,'historical_root_scientific_fixtures':1,'primary_runs':0,'historical_programs_replayed':0,'editable_prompt_files_changed':[]}
(O/'ACCEPTANCE.json').write_text(json.dumps(review,indent=2)+'\n');(O/'FINAL_FREEZE.json').write_text(json.dumps({'utc':review['utc'],'files':[pin(O/'ACCEPTANCE.json')],'scope':'Actual root source-publication review, no integration or audit'},indent=2)+'\n');print(json.dumps({'review':pin(O/'ACCEPTANCE.json'),'freeze':pin(O/'FINAL_FREEZE.json'),'members':162,'sources':87,'exact_functions':exact}))
