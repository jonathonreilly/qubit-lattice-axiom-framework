from pathlib import Path
import json,hashlib,datetime,ast,difflib
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261014_214309');D=N/'transverse_field_memory_publication_draft';O=D/'proposal';W=N.parent/'correlation_worktree';P='.claude/science/physics-loops/toe-transverse-field-memory-20261015';R=N/'transverse_field_memory_publication_root_review';R.mkdir(exist_ok=False)
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def load(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),(str(p),r)
def dump(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
f=load(D/'FINAL_FREEZE.json');assert pin(D/'FINAL_FREEZE.json')['sha256']=='96e198bc616242f36fc59bb498c68d52cb4b2605fa3695f49eb4463720b43bee' and len(f['files'])==227
for r in f['files']:same(r['path'],r)
for r in load(D/'SOURCE_FRESHNESS.json')['identities']:same(r['original'],r)
bm=load(O/P/'BODY_MAP.json');note=O/bm['note'];b=note.read_bytes();assert pin(note)['sha256']=='259ffd4f4835fe9945772ac54981ed38f312b209fcd7f63ae01747b544974287'
def recover(r,record):
 if r['kind']=='blob':raw=(O/r['path']).read_bytes()
 elif r['kind']=='external_pinned':raw=(W/r['path']).read_bytes()
 else:
  p=O/r['container']
  if not p.exists():p=W/r['container']
  data=p.read_bytes();raw=data[r['start_byte_inclusive']:r['end_byte_exclusive']];assert data.count(raw)==1
 assert (len(raw),hashlib.sha256(raw).hexdigest())==(record['bytes'],record['sha256'])
for r in bm['bodies']:recover({'kind':'body_interval',**r},r)
sources=load(O/P/'SOURCE_MANIFEST.json')['sources']
for r in sources:recover(r['recovery'],r)
for r in load(O/P/'RECOVERY_SELECTION.json')['members']:
 if r['recovery'] is not None:
  recover(r['recovery'],r);assert any(all(q[k]==r[k] for k in ('bytes','sha256','recovery')) for q in sources)
parents=load(O/P/'DEPENDENCIES.json')['dependencies'];assert len(parents)==1;same(W/parents[0]['path'],parents[0])
for row in load(O/P/'INPUT_MANIFEST.json')['inputs']:same(O/row['path'],row)
reuse=[]
for r in load(D/'CHANGED_CODE_MAP.json')['files']:
 a=(D/'template_snapshot'/r['file']).read_text();b=(D/r['file']).read_text();assert hashlib.sha256(a.encode()).hexdigest()==r['old_sha256'] and hashlib.sha256(b.encode()).hexdigest()==r['new_sha256']
 diff=''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='finite_bank_publication_draft/'+r['file'],tofile='transverse_field_memory_publication_draft/'+r['file']));assert diff==(D/r['complete_diff']).read_text()
 if r['file'].endswith('.py'):
  old={v.name:v for v in ast.parse(a).body if isinstance(v,ast.FunctionDef)};new={v.name:v for v in ast.parse(b).body if isinstance(v,ast.FunctionDef)}
  for q in r['functions']:
   if q['status']=='same_AST':assert ast.dump(old[q['name']],include_attributes=False)==ast.dump(new[q['name']],include_attributes=False);reuse.append(r['file']+':'+q['name'])
for folder in ('build','inspection'):
 p=D/'metadata_runs'/folder;r=load(p/'EXECUTION.json');assert r['exit_code']==0
 for key in ('stdout','stderr'):same(r[key]['path'],r[key])
 same(p/'executed_source.py',r['child_source_at_launch']);assert (p/'stderr').stat().st_size==0
primary=O/'scripts/transverse_field_gibbs_memory_2026_10_15.py';tree=ast.parse(primary.read_text());values={v.targets[0].id:ast.literal_eval(v.value) for v in tree.body if isinstance(v,ast.Assign) and isinstance(v.targets[0],ast.Name) and v.targets[0].id in {'EXPECTED_BODIES','EXPECTED_PARENTS','EXPECTED_PARENT_REVIEW','AUDIT_INPUT_PATHS','MANIFEST_SHA256'}}
expected=(D/'primary_template.py').read_text()
for key in ('EXPECTED_BODIES','EXPECTED_PARENTS','EXPECTED_PARENT_REVIEW','AUDIT_INPUT_PATHS'):expected=expected.replace('__'+key+'__',repr(values[key]))
expected=expected.replace('__MANIFEST_SHA256__',values['MANIFEST_SHA256']).replace('__PARENT_PATH__',parents[0]['path']).replace('__PARENT_CLAIM_ID__',parents[0]['claim_id']);assert expected==primary.read_text()
decision={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'root_source_publication_review','disposition':'Accept source-only publication proposal for separately reviewed actual integration; no primary or publication result yet','proposal_freeze':pin(D/'FINAL_FREEZE.json'),'note':pin(note),'primary':pin(primary),'accepted_science':pin(N/'transverse_field_memory_root_review/ACCEPTANCE.md'),'read_coverage':'Complete current wrapper and nine packet texts, complete build/inspection/recorder/seal changed diffs including module-level logic, entire primary template, parent-reading and final-delivery records. Exact three scientific bodies reuse prior complete proof/comparison reading and actual root acceptance at unchanged hashes. All227members,114source records and recoverable selection rows checked mechanically;22named functions retain verified AST identity. No new independent mathematical or retained audit claim.','same_AST_functions':reuse,'changes_requiring_attention':'Integration must relocate RECOVERY_SELECTION alongside BODY_MAP and SOURCE_MANIFEST, enforce linkage in primary, pin real root read/base/receipt inputs and keep historical nulls. Current frozen unbound proposal is intentionally not executed.','scientific_programs_run':0,'editable_prompt_files_changed':[]}
dump(R/'ACCEPTANCE.json',decision);dump(R/'FINAL_FREEZE.json',{'utc':decision['utc'],'files':[pin(R/'ACCEPTANCE.json')]});print(json.dumps({'acceptance':pin(R/'ACCEPTANCE.json'),'freeze':pin(R/'FINAL_FREEZE.json'),'members':len(f['files']),'sources':len(sources),'same_AST':len(reuse)}))
