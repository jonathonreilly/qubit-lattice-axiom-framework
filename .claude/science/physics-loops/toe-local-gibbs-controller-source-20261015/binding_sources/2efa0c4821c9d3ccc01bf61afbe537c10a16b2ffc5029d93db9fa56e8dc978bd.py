from pathlib import Path
import ast,datetime,gzip,hashlib,json
N=Path(__file__).resolve().parents[1];D=N/'local_gibbs_controller_publication_draft';S=D/'proposal';W=N.parent/'correlation_worktree';R=N/'local_gibbs_controller_publication_root_review'
P='.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015';NOTE='docs/LOCAL_GIBBS_CONTROLLER_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md';H='scripts/local_gibbs_controller_source_2026_10_15.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
def rawsame(b,r):assert len(b)==r['bytes'] and hashlib.sha256(b).hexdigest()==r['sha256']
def write(p,v):assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
f=read(D/'FINAL_FREEZE.json');assert pin(D/'FINAL_FREEZE.json')['sha256']=='c1a78b657c4d41c2b18bd1e9d90a6705cd4446abc170874dffb23e104723da28' and len(f['files'])==138
for r in f['files']:same(D/r['path'],r)
assert {str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()}=={r['path'] for r in f['files']}|{'FINAL_FREEZE.json'}
note=(S/NOTE).read_bytes();bodies=read(S/P/'BODY_MAP.json')['bodies'];assert len(bodies)==3 and note.startswith((D/'wrapper.md').read_bytes())
for r in bodies:
 b=note[r['start_byte_inclusive']:r['end_byte_exclusive']];rawsame(b,r);assert note.count(b)==1
sources=read(S/P/'SOURCE_MANIFEST.json')['sources'];assert len(sources)==73
for r in sources:
 loc=r['recovery']
 if loc['kind']=='blob':b=(S/loc['path']).read_bytes()
 elif loc['kind']=='external_pinned':b=(W/loc['path']).read_bytes()
 else:
  p=S/loc['container']
  if not p.exists():p=W/loc['container']
  b=p.read_bytes()[loc['start_byte_inclusive']:loc['end_byte_exclusive']]
 rawsame(b,r)
for m in read(S/P/'RECOVERY_SELECTION.json')['members']:
 loc=m.get('recovery')
 if loc is not None:assert any(m['sha256']==r['sha256'] and m['bytes']==r['bytes'] and loc==r['recovery'] for r in sources)
parents=read(S/P/'DEPENDENCIES.json')['dependencies'];assert len(parents)==1
for r in parents:
 same(W/r['path'],r)
 for b in r['accepted_body_intervals']:rawsame((W/b['container']).read_bytes()[b['start_byte_inclusive']:b['end_byte_exclusive']],b)
pr=read(S/P/'PARENT_REVIEW_BINDING.json');same(S/pr['compressed']['path'],pr['compressed']);same(S/pr['decompressed']['path'],pr['decompressed'])
assert gzip.decompress((S/pr['compressed']['path']).read_bytes())==(S/pr['decompressed']['path']).read_bytes()
manifest=read(S/P/'INPUT_MANIFEST.json');[same(S/r['path'],r) for r in manifest['inputs']]
primary=(S/H).read_text();a=ast.parse(primary);names={'AUDIT_INPUT_PATHS','MANIFEST_SHA256','EXPECTED_BODIES','EXPECTED_PARENT_BODIES','EXPECTED_GIT_BASE','EXPECTED_BASE_PR','EXPECTED_BASE_BRANCH'}
literal={n.targets[0].id:ast.literal_eval(n.value) for n in a.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in names}
assert literal['EXPECTED_GIT_BASE'] is literal['EXPECTED_BASE_PR'] is literal['EXPECTED_BASE_BRANCH'] is None
assert set(literal['AUDIT_INPUT_PATHS'])=={r['path'] for r in manifest['inputs']}|{P+'/INPUT_MANIFEST.json',P+'/ACTUAL_BINDING.json'}|{r['path'] for r in parents}
expected=(D/'primary_template.py').read_text().replace('__MANIFEST_SHA256__',pin(S/P/'INPUT_MANIFEST.json')['sha256']).replace('__AUDIT_INPUT_PATHS__',repr(literal['AUDIT_INPUT_PATHS'])).replace('__EXPECTED_BODIES__',repr(literal['EXPECTED_BODIES'])).replace('__EXPECTED_PARENT_BODIES__',repr(literal['EXPECTED_PARENT_BODIES'])).rstrip()+'\n'
assert primary==expected
reuse=read(D/'REUSE_MAP.json');exact=0
for r in reuse['functions']:
 if r['byte_exact_reuse']:
  for label,folder in [('current',D),('reference',D/'reference_scripts')]:
   p=folder/r['script'];text=p.read_text();n=next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==r['function']);b=''.join(text.splitlines(keepends=True)[n.lineno-1:n.end_lineno]).encode();rawsame(b,r[label])
  exact+=1
assert pin(D/'record_metadata.py')['sha256']=='96c5ebbdcbe83ec482e8e5d3f10e42b9d738557dcb6c04c42e089e0d8fc686ed'
receipts=[]
for label in ('build','inspection'):
 p=D/'metadata_runs'/label/'EXECUTION.json';r=read(p);assert r['exit_code']==0 and r['scientific_execution'] is False
 for k in ('stdout','stderr','child_source_at_launch','recorder'):same(r[k]['path'],r[k])
 assert Path(r['stderr']['path']).read_bytes()==b'';receipts.append(pin(p))
for row in read(D/'SOURCE_FRESHNESS.json')['identities']:same(row['original'],row)
review={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'root_source_publication_review','root_read_complete':True,'source_draft_freeze':pin(D/'FINAL_FREEZE.json'),'note':pin(S/NOTE),'primary':pin(S/H),'body_pins':bodies,'parents':parents,'parent_review_binding':pr,'existing_source_acceptances':{'local_gibbs_controller':pin(N/'local_gibbs_controller_root_review/ACCEPTANCE.md')},'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.','full_current_files_read':[pin(D/x) for x in ('wrapper.md','build_proposal.py','primary_template.py','inspect_proposal.py','seal_packet.py')]+[pin(p) for p in sorted((S/P).glob('*.md'))],'read_scope':'Complete current wrapper, nine packet texts, primary template, builder/inspector/seal code read. Original three bodies and canonical parent proof/review reused at exact previously complete read identities. Recorder byte-exact reuse; generated primary rendered exactly. All138members73sources and recovery links verified. Source-only interpretation; no new independent scientific vote.','metadata_receipts':receipts,'exact_helper_functions':exact,'qualification_scope':['Normalized versus unnormalized physical edges and distinct M^4/M^8 certificates; full-sector spectrum/gap and complex phases.','Exact norm/scalar versus block/Pauli/positive-channel costs; actual extra C_gamma identity reserve.','Full Gibbs marginal and exact unconditioned retained output; sharp g and separate continuity/actual-gap calibrations.','Fixed geometry and design-only power-of-two choice, actual source-local and plant-coupling distinction, paid clock compensation and old aging.','No cooling time, native source, efficient general synthesis, complete runtime handoff, common cap, detector/energy identification, reuse or retained audit.'],'scientific_programs_run':0,'primary_runs':0,'historical_programs_replayed':0,'editable_prompt_files_changed':[]}
write(R/'ACCEPTANCE.json',review);write(R/'FINAL_FREEZE.json',{'utc':review['utc'],'files':[pin(R/'ACCEPTANCE.json')],'scope':'Actual root publication-source review only'})
print(json.dumps({'review':pin(R/'ACCEPTANCE.json'),'freeze':pin(R/'FINAL_FREEZE.json'),'members':138,'sources':73,'exact_functions':exact}))
