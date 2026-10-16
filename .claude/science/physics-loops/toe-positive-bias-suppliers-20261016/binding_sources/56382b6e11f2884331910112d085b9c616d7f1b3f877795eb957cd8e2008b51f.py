from pathlib import Path
import ast,datetime,hashlib,json,subprocess
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');P=N/'positive_bias_integration_proposal';D=N/'publication_integration/positive_bias_suppliers';W=N.parent/'correlation_worktree';R=N/'root_positive_bias_integration_review';C=D/'canonical_source';S=N/'positive_bias_publication_draft/proposal'
PK='.claude/science/physics-loops/toe-positive-bias-suppliers-20261016';NOTE='docs/POSITIVE_BIAS_SUPPLIERS_BOUNDED_THEOREM_NOTE_2026-10-16.md';HELPER='scripts/positive_bias_suppliers_2026_10_16.py'
def read(p):return json.loads(Path(p).read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=sha(b))
def same(p,r):
 a=pin(p);assert a['bytes']==r['bytes'] and a['sha256']==r['sha256'],p
def parse(p):
 s=Path(p).read_text();ls=s.splitlines();f={n.name:'\n'.join(ls[n.lineno-1:n.end_lineno]) for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)};v={}
 for n in ast.parse(s).body:
  if isinstance(n,ast.Assign):
   for t in n.targets:
    if isinstance(t,ast.Name):
     try:v[t.id]=ast.literal_eval(n.value)
     except (ValueError,TypeError):pass
 return f,v
prep=read(D/'PREPARED.json');same(D/'CANONICALIZATION.diff',prep['diff'])
changed=[];added=[];unchanged=[]
for rel,row in prep['canonical_files'].items():
 same(W/rel,row);same(C/rel,row)
 if (S/rel).exists():(unchanged if (S/rel).read_bytes()==(W/rel).read_bytes() else changed).append(rel)
 else:added.append(rel)
assert len(unchanged)==150 and len(changed)==5 and len(added)==27
assert set(changed)=={PK+'/BODY_MAP.json',PK+'/INPUT_MANIFEST.json',PK+'/SOURCE_MANIFEST.json',NOTE,HELPER}
for proposal,canonical in [('PROPOSED_NOTE.md',NOTE),('PROPOSED_BODY_MAP.json',PK+'/BODY_MAP.json'),('PROPOSED_SOURCE_MANIFEST.json',PK+'/SOURCE_MANIFEST.json'),('PROPOSED_HISTORICAL_RECEIPT_INDEX.json',PK+'/HISTORICAL_RECEIPT_INDEX.json')]:assert (P/proposal).read_bytes()==(W/canonical).read_bytes()
f,a=parse(P/'proposed_primary_unbound.py');g,b=parse(W/HELPER);assert f==g
delta={k for k in b if a.get(k)!=b[k]}
assert delta=={'EXPECTED_GIT_BASE','MANIFEST_SHA256','AUDIT_INPUT_PATHS','EXPECTED_BASE_PR','EXPECTED_BASE_BRANCH','EXPECTED_BASE_PARENT_BRANCH'}
assert b['EXPECTED_GIT_BASE']=='e2c214f59ad8201a10ef1b7f245cd67973aeb088'
assert b['EXPECTED_BASE_PR']==9633 and b['EXPECTED_BASE_BRANCH']=='physics-loop/toe-bus-joint-energy-moments-20261016' and b['EXPECTED_BASE_PARENT_BRANCH']=='physics-loop/toe-strongly-regular-bus-20261015'
manifest=read(W/PK/'INPUT_MANIFEST.json');assert b['MANIFEST_SHA256']==pin(W/PK/'INPUT_MANIFEST.json')['sha256']
for row in manifest['inputs']:same(W/row['path'],row)
expected={r['path'] for r in manifest['inputs']}|{PK+'/INPUT_MANIFEST.json'}
assert set(b['AUDIT_INPUT_PATHS'])==expected and len(b['AUDIT_INPUT_PATHS'])==len(expected)
binding=read(W/PK/'ACTUAL_BINDING.json');canonical=read(W/PK/'CANONICAL_BINDING.json');bodies=read(W/PK/'BODY_MAP.json')['bodies'];parent=read(W/PK/'PARENT_BINDING.json');note=(W/NOTE).read_bytes()
assert binding['root_read_complete'] is False and canonical['root_read_complete'] is False
assert binding['raw_bodies']==bodies and binding['parent_binding']==parent
assert binding['source_body_pins']==read(S/PK/'BODY_MAP.json')['bodies']
assert binding['note_sha256']==canonical['bound_note_sha256']==sha(note)
assert binding['canonical_review_evidence'] is None and binding['new_scientific_execution'] is False and binding['retained_audit'] is False
for row in bodies:
 data=note[row['start_byte_inclusive']:row['end_byte_exclusive']];assert len(data)==row['bytes'] and sha(data)==row['sha256']
for row in parent['direct_mathematical_parents']:same(W/row['path'],row)
def walk(value):
 if isinstance(value,dict):
  if {'path','bytes','sha256'}<=value.keys():
   path=Path(value['path']);same(path if path.is_absolute() else W/path,value)
  for item in value.values():walk(item)
 elif isinstance(value,list):
  for item in value:walk(item)
walk(binding);walk(read(W/PK/'ACTUAL_REFRESH_PROVENANCE.json'))
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W).decode().strip()==b['EXPECTED_GIT_BASE']
assert subprocess.check_output(['git','branch','--show-current'],cwd=W).decode().strip()=='physics-loop/toe-positive-bias-suppliers-20261016'
out=R/'CANONICAL_REVIEW.json';assert not out.exists()
record=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),root_read_complete=True,bound_note_sha256=sha(note),canonical_body_pins=bodies,parent_binding=parent,source_draft_freeze_sha256='8b8c172a101b5cf35a4f542b55d7c5c3249da99dd78a896078805518dfe12d53',source_draft_review_sha256='599f13b41038fb53b326e766ad772305dfc4f0501721d52a51534ca86bc3ac42',git_base=b['EXPECTED_GIT_BASE'],prebinding_primary=pin(W/HELPER),integration_common=pin(P/'positive_bias_common.py'),prepared=pin(D/'PREPARED.json'),diff=pin(D/'CANONICALIZATION.diff'),
 review_method='Full changed prose and runtime functions already read at pinned proposal identities; canonical note/maps equal reviewed previews. Complete canonical diff partition verified by exact bytes, all data tables/metadata fields checked structurally, all primary functions unchanged and only six reviewed literals bound. Large repeated source inventories are checked exhaustively by deterministic comparisons, not claimed newly read scientific arguments.',
 unchanged_canonical_files=len(unchanged),changed_canonical_files=changed,added_canonical_files=added,primary_changed_literals=sorted(delta),
 scientific_programs_run=0,canonical_primary_runs=0,retained_audit=False,editable_prompt_files_changed=[])
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(dict(review=pin(out))))
