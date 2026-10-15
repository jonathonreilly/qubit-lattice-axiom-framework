from pathlib import Path
import json,hashlib,datetime,ast,difflib,gzip
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261014_214309');D=N/'single_port_program_and_controller_publication_draft';O=D/'proposal';W=N.parent/'correlation_worktree';P='.claude/science/physics-loops/toe-single-port-program-and-controller-20261015';R=N/'single_port_program_and_controller_publication_root_review';R.mkdir(exist_ok=False)
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def load(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),(str(p),r)
def dump(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
f=load(D/'FINAL_FREEZE.json');assert pin(D/'FINAL_FREEZE.json')['sha256']=='c2c576011f10bf011139756ee0ab96e5dedf609a4f354242d9c653198ca7b3c2' and len(f['files'])==178
for r in f['files']:same(D/r['path'],r)
for r in load(D/'SOURCE_FRESHNESS.json')['identities']:same(r['original'],r)
bm=load(O/P/'BODY_MAP.json');note=O/bm['note'];assert pin(note)['sha256']=='74968df4ceed3276e67dddb3f72acc013a15c415f0e87c58370a52ec8149c81f'
def recover(r,record):
 if r['kind']=='blob':raw=(O/r['path']).read_bytes()
 elif r['kind']=='external_pinned':raw=(W/r['path']).read_bytes()
 else:
  p=O/r['container']
  if not p.exists():p=W/r['container']
  data=p.read_bytes()
  if r['kind']=='external_gzip_interval':assert (len(data),hashlib.sha256(data).hexdigest())==(r['stored_bytes'],r['stored_sha256']);data=gzip.decompress(data)
  raw=data[r['start_byte_inclusive']:r['end_byte_exclusive']];assert data.count(raw)==1
 assert (len(raw),hashlib.sha256(raw).hexdigest())==(record['bytes'],record['sha256'])
for r in bm['bodies']:recover({'kind':'body_interval',**r},r)
sources=load(O/P/'SOURCE_MANIFEST.json')['sources']
for r in sources:recover(r['recovery'],r)
for r in load(O/P/'RECOVERY_SELECTION.json')['members']:
 if r['recovery'] is not None:
  recover(r['recovery'],r);assert any(all(q[k]==r[k] for k in ('bytes','sha256','recovery')) for q in sources)
parents=load(O/P/'DEPENDENCIES.json')['dependencies'];assert len(parents)==1;same(W/parents[0]['path'],parents[0])
for r in parents[0]['accepted_body_intervals']:recover({'kind':'external_body_interval',**r},r)
for r in parents[0]['review_evidence']:recover({'kind':'external_gzip_interval',**r},r)
for row in load(O/P/'INPUT_MANIFEST.json')['inputs']:same(O/row['path'],row)
reuse=load(D/'REUSE_MAP.json');exact=[]
for r in reuse['references']:same(r['path'],r);same(D/r['recovery'],r)
for r in reuse['functions']:
 for part,folder in (('current',D),('reference',D/'reference_scripts')):
  q=r[part]
  if q is None:continue
  lines=(folder/r['script']).read_text().splitlines(True);raw=''.join(lines[q['line_start']-1:q['line_end']]).encode();assert (len(raw),hashlib.sha256(raw).hexdigest())==(q['bytes'],q['sha256'])
 if r['byte_exact_reuse']:assert r['current']['sha256']==r['reference']['sha256'];exact.append(r['script']+':'+r['function'])
assert (D/'record_metadata.py').read_bytes()==(D/'reference_scripts/record_metadata.py').read_bytes()
diff=''
for r in reuse['references']:
 p=Path(r['path']);diff+=''.join(difflib.unified_diff((D/r['recovery']).read_text().splitlines(True),(D/p.name).read_text().splitlines(True),fromfile='reference/'+p.name,tofile='current/'+p.name))
assert diff==(D/'CHANGED_CODE.patch').read_text()
for row in load(D/'PAYLOAD_CHANGE_INDEX.json')['current_files']:same(D/row['path'],row)
receipts=[]
for folder,expected in (('build',0),('inspection',1),('inspection_final',0)):
 p=D/'metadata_runs'/folder;r=load(p/'EXECUTION.json');assert r['exit_code']==expected and r['scientific_execution'] is False
 for key in ('stdout','stderr','child_source_at_launch','recorder'):same(r[key]['path'],r[key])
 same(p/'executed_source.py',r['child_source_at_launch']);receipts.append(pin(p/'EXECUTION.json'))
primary=O/'scripts/single_port_program_and_autonomous_controller_2026_10_15.py';tree=ast.parse(primary.read_text());keys={'EXPECTED_BODIES','EXPECTED_PARENT_BODIES','AUDIT_INPUT_PATHS','MANIFEST_SHA256'};values={v.targets[0].id:ast.literal_eval(v.value) for v in tree.body if isinstance(v,ast.Assign) and isinstance(v.targets[0],ast.Name) and v.targets[0].id in keys};expected=(D/'primary_template.py').read_text()
for key in keys:expected=expected.replace('__'+key+'__',values[key] if key=='MANIFEST_SHA256' else repr(values[key]))
assert expected.rstrip()+'\n'==primary.read_text()
accept={'external_compiler':pin(N/'single_port_program_root_review/ACCEPTANCE.md'),'autonomous_controller':pin(N/'single_port_autonomous_root_review/ACCEPTANCE.md')}
decision={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'root_source_publication_review','root_read_complete':True,'decision':'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.','source_draft_freeze':pin(D/'FINAL_FREEZE.json'),'note':pin(note),'primary':pin(primary),'body_pins':bm['bodies'],'parents':parents,'existing_source_acceptances':accept,'read_coverage':'Entire current wrapper, nine packet texts, entire builder/inspector/seal helpers and primary template. Metadata recorder byte-exact reuse verified; every mapped reused function byte interval verified. Four immutable scientific bodies and canonical unary proof/review reuse prior complete source reading at unchanged identities and two actual source acceptances. Generated payload index/source/recovery/manifest and complete code diff reconstructed; no claim of linear rereading of duplicated full payload patch.','reviewed_qualifications':['Correct double-commutator Lie induction and nonempty computable-input domain; some weak rational coupling, not every coupling.','Actual-time aging, complete retained outputs and phase/scalar prices; pure-memory resource premise at actual aged time.','Endpoint-or-variation work price and whole-generator positivity versus positive old local blocks.','Bare vacuum, full reduced inverse/two-excitation corrector, actual nonscalar port counterterm, complex source sign and nominal one-head restriction.','Prepared pure clock and vacuum, unbounded finite resources, no native supply/detector/common cap/reuse.'],'exact_function_reuse':exact,'actual_metadata_receipts':receipts,'preserved_metadata_failure':'First inspection rejected extra template trailing newline. Frozen draft preserves failed receipt/source and final successful inspection. No science failure or repeated scientific execution.','integration_obligations':'Choose and actually observe reviewed base; bind real source-review execution and proposal; relocate every interval including RECOVERY_SELECTION with semantic primary linkage; keep historical nulls. Run bounded source/cache/mutations/focused/graph checks, preserve old graph and sole unary parent edge, then regular PR/attachment.','scientific_programs_run':0,'primary_runs':0,'historical_programs_replayed':0,'editable_prompt_files_changed':[]}
dump(R/'ACCEPTANCE.json',decision);dump(R/'FINAL_FREEZE.json',{'utc':decision['utc'],'files':[pin(R/'ACCEPTANCE.json')]});print(json.dumps({'review':pin(R/'ACCEPTANCE.json'),'freeze':pin(R/'FINAL_FREEZE.json'),'members':len(f['files']),'sources':len(sources),'exact_functions':len(exact)}))
