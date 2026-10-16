from pathlib import Path
import ast,datetime,difflib,hashlib,json,sys
N=Path(__file__).resolve().parents[1];D=N/'accuracy_scaled_compiler_publication_draft';S=D/'proposal';W=N.parent/'correlation_worktree';R=N/'accuracy_scaled_compiler_publication_root_review'
P='.claude/science/physics-loops/toe-accuracy-scaled-compiler-20261015';NOTE='docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md';H='scripts/accuracy_scaled_compiler_2026_10_15.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def rawsame(b,r):assert(len(b),hashlib.sha256(b).hexdigest())==(r['bytes'],r['sha256'])
def write(p,v):assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
f=read(D/'FINAL_FREEZE.json');assert pin(D/'FINAL_FREEZE.json')['sha256']==sys.argv[1]
for r in f['files']:same(D/r['path'],r)
assert {str(p.resolve()) for p in D.rglob('*') if p.is_file()}=={str((D/r['path']).resolve()) for r in f['files']}|{str(D/'FINAL_FREEZE.json')}
note=(S/NOTE).read_bytes();bodies=read(S/P/'BODY_MAP.json')['bodies'];assert len(bodies)==3 and note.startswith((D/'wrapper.md').read_bytes())
assert {r['sha256'] for r in bodies}=={'6cae05fe6569b630041095b2cd44ad53a2cfedebdd0de30cd411975729f0186b','899a28b936f5d8213ca2fbf28da6dc0bf0bc59534a64b97d8f2116db53ff9dc5','c9c098724bd13d87ce129f291ff7f75d7862651a85c17034a161de3ff0e124a8'}
for r in bodies:
 b=note[r['start_byte_inclusive']:r['end_byte_exclusive']];rawsame(b,r);assert note.count(b)==1
sources=read(S/P/'SOURCE_MANIFEST.json')['sources'];assert len(sources)==75
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
  body=next(b for b in bodies if b['name']==loc['body_name']);assert all(loc[k]==body[k] for k in ('container','start_byte_inclusive','end_byte_exclusive'))
for m in read(S/P/'RECOVERY_SELECTION.json')['members']:
 if m.get('recovery') is not None:assert any(m['sha256']==r['sha256'] and m['bytes']==r['bytes'] and m['recovery']==r['recovery'] for r in sources)
objects=read(S/P/'ARCHIVE_INDEX.json')['objects'];assert len(objects)==53 and {o['sha256'] for o in objects}=={s['sha256'] for s in sources if s['recovery']['kind']=='blob'}
for o in objects:same(S/o['path'],o)
parents=read(S/P/'DEPENDENCIES.json')['dependencies'];assert len(parents)==1 and parents[0]['sha256']=='db922c9b3f67a603961f5a621a67eea7fa4894b793befbcdd3b7b034011e540a'
for r in parents:
 same(W/r['path'],r)
 for b in r['accepted_body_intervals']:rawsame((W/b['container']).read_bytes()[b['start_byte_inclusive']:b['end_byte_exclusive']],b)
assert parents[0]['required_mathematical_body_names']==['independent_author','comparison']
manifest=read(S/P/'INPUT_MANIFEST.json');[same(S/r['path'],r) for r in manifest['inputs']]
primary=(S/H).read_text();a=ast.parse(primary);names={'AUDIT_INPUT_PATHS','MANIFEST_SHA256','EXPECTED_BODIES','EXPECTED_PARENT_BODIES','EXPECTED_PARENT_REVIEW','EXPECTED_PARENTS','EXPECTED_ACCEPTANCES','EXPECTED_GIT_BASE','EXPECTED_BASE_PR','EXPECTED_BASE_BRANCH'}
literal={n.targets[0].id:ast.literal_eval(n.value) for n in a.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in names}
assert literal['EXPECTED_GIT_BASE'] is literal['EXPECTED_BASE_PR'] is literal['EXPECTED_BASE_BRANCH'] is None
assert set(literal['AUDIT_INPUT_PATHS'])=={r['path'] for r in manifest['inputs']}|{P+'/INPUT_MANIFEST.json',P+'/ACTUAL_BINDING.json'}|{r['path'] for r in parents}
expected=(D/'primary_template.py').read_text()
for key in ('MANIFEST_SHA256','AUDIT_INPUT_PATHS','EXPECTED_BODIES','EXPECTED_PARENT_BODIES','EXPECTED_PARENT_REVIEW','EXPECTED_PARENTS','EXPECTED_ACCEPTANCES'):expected=expected.replace('__'+key+'__',literal[key] if key=='MANIFEST_SHA256' else repr(literal[key]))
assert primary==expected.rstrip()+'\n' and literal['MANIFEST_SHA256']==pin(S/P/'INPUT_MANIFEST.json')['sha256']
reuse=read(D/'REUSE_MAP.json');exact=0
for r in reuse['functions']:
 if r.get('byte_exact_reuse',False):
  for label,folder in [('current',D),('reference',D/'reference_scripts')]:
   p=folder/r['script'];text=p.read_text();node=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==r['function']);rawsame(''.join(text.splitlines(True)[node.lineno-1:node.end_lineno]).encode(),r[label])
  exact+=1
code=''.join(''.join(difflib.unified_diff((D/'reference_scripts'/x).read_text().splitlines(True),(D/x).read_text().splitlines(True),fromfile='reference/'+x,tofile='current/'+x)) for x in reuse['module_level_scripts_in_full_diff']);assert code==(D/'CHANGED_CODE.patch').read_text()
assert ''.join(difflib.unified_diff((D/'PREBUILD_CHANGED_CODE.patch').read_text().splitlines(True),code.splitlines(True),fromfile='root_read/PREBUILD_CHANGED_CODE.patch',tofile='final/CHANGED_CODE.patch'))==(D/'POST_ROOT_READ_CODE.diff').read_text()
receipts=[]
for p in sorted((D/'metadata_runs').glob('*/EXECUTION.json')):
 r=read(p);assert r['exit_code']==0 and r['scientific_execution'] is False
 for k in ('stdout','stderr','child_source_at_launch','recorder','launch'):same(r[k]['path'],r[k])
 for row in read(r['launch']['path'])['inputs']:same(row['captured']['path'],row['captured']);assert row['captured']['sha256']==row['original']['sha256']
 assert Path(r['stderr']['path']).read_bytes()==b'';receipts.append(pin(p))
assert len(receipts)==2
for row in read(D/'SOURCE_FRESHNESS.json')['identities']:same(row['original'],row)
state=read(S/P/'PUBLICATION_STATE.json');assert state['scientific_programs_run_this_draft']==state['historical_root_scientific_fixtures']==state['historical_programs_replayed']==0
for key in ('canonical_binding','git_base','primary_execution','cache_execution','mutation_execution','graph_execution','publication_action','retained_audit'):assert state[key] is None
parent_review=read(S/P/'PARENT_REVIEW_BINDING.json');assert parent_review==literal['EXPECTED_PARENT_REVIEW']
review=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),kind='root_source_publication_review',root_read_complete=True,source_draft_freeze=pin(D/'FINAL_FREEZE.json'),note=pin(S/NOTE),primary=pin(S/H),body_pins=bodies,parents=parents,parent_review_binding=parent_review,existing_source_acceptances={'accuracy_scaled_compiler':pin(N/'accuracy_scaled_compiler_root_review/ACCEPTANCE.md')},decision='Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.',full_current_files_read=[pin(D/'wrapper.md')]+[pin(p) for p in sorted((D/'packet_text').glob('*'))],changed_code_complete_read=[pin(D/x) for x in reuse['module_level_scripts_in_full_diff']],read_scope='Complete wrapper read in two bounded outputs; nine packet texts fully read. Complete changed helper modules read in three contiguous outputs and reconstructed against five exact reviewed references. Final parent-binding paragraph, two post-preview helper changes, complete source editor adapt_sources.py and metadata provenance separately inspected. Three proof/readout/assessment bodies reuse accepted exact full reading. Complete source/recovery/freeze/receipt identities checked. No new independent science or retained verdict.',metadata_receipts=receipts,exact_helper_functions=exact,qualification_scope=['Fixed supplied computable consistent polynomial certificate; selected coupling, not every coupling.','Degree D versus separately attributed coefficient-index k0; D+1 nodes remain in both cases.','Only protected finite-grid parent recipe and its comparison imported; no substitution of alternative root timing/norm constants.','Actual exp(-isH)Wexp(-iTH) aging, physical scalar, all outputs, single integrated defect budget, positivity and endpoint-work/moment limits remain.','Enormous fixed-data sufficient powers; no oracle runtime, efficient dimension scaling, native realization, permanent halt or reuse theorem.'],scientific_programs_run_this_review=0,primary_runs=0,historical_programs_replayed=0,historical_root_scientific_fixtures=0,editable_prompt_files_changed=[])
write(R/'ACCEPTANCE.json',review);write(R/'FINAL_FREEZE.json',dict(utc=review['utc'],files=[pin(R/'ACCEPTANCE.json')],scope='Actual root publication-source review only'))
print(json.dumps(dict(review=pin(R/'ACCEPTANCE.json'),freeze=pin(R/'FINAL_FREEZE.json'),members=len(f['files']),sources=len(sources),exact_functions=exact)))
