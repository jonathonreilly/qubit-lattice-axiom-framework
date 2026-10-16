from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,subprocess
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');W=N.parent/'correlation_worktree';I=N/'publication_integration/bus_joint_energy';D=N/'bus_joint_energy_integration_corrected';S=N/'bus_joint_energy_publication_draft/proposal';R=N/'root_bus_joint_energy_integration_review'
Q='.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016';NOTE='docs/BUS_JOINT_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md';HELPER='scripts/bus_joint_energy_moments_2026_10_16.py';BASE='68c531309ac6dae96289aab964213b8c5f55969b'
def pin(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(p.read_text())
def same(p,row):
 a=pin(p);assert (a['bytes'],a['sha256'])==(row['bytes'],row['sha256']),str(p)
prepared=read(I/'PREPARED.json')
for rel,row in prepared['canonical_files'].items():same(W/rel,row)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip()==BASE
assert subprocess.check_output(['git','branch','--show-current'],cwd=W,text=True).strip()=='physics-loop/toe-bus-joint-energy-moments-20261016'
raw=(S/NOTE).read_text()
for old,new in read(D/'WRAPPER_REPLACEMENTS.json').items():assert raw.count(old)==1;raw=raw.replace(old,new)
assert raw==(W/NOTE).read_text()
bodies=read(W/Q/'BODY_MAP.json')['bodies'];old_bodies=read(S/Q/'BODY_MAP.json')['bodies'];data=(W/NOTE).read_bytes()
for old,b in zip(old_bodies,bodies):
 assert all(old[k]==b[k] for k in ['name','source','bytes','sha256','container'])
 source=(N/b['source']).read_bytes();assert data[b['start_byte_inclusive']:b['end_byte_exclusive']]==source and data.count(source)==1
parent=read(W/Q/'PARENT_BINDING.json');assert parent==read(S/Q/'PARENT_BINDING.json')
for row in parent['canonical_parents']:same(W/row['path'],row)
manifest=read(W/Q/'INPUT_MANIFEST.json')
for row in manifest['inputs']:same(W/row['path'],row)
def pieces(path):
 text=path.read_text();tree=ast.parse(text)
 return {n.name:ast.get_source_segment(text,n) for n in tree.body if isinstance(n,ast.FunctionDef)},{n.targets[0].id:ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id not in ['REPO']}
f1,a1=pieces(D/'proposed_primary_unbound.py');f2,a2=pieces(W/HELPER);assert f1==f2
changed={k for k in a1 if a1[k]!=a2[k]}
assert changed=={'EXPECTED_GIT_BASE','EXPECTED_ROOT_REVIEW_SHA','EXPECTED_ROOT_REVIEW_COMMAND','AUDIT_INPUT_PATHS','MANIFEST_SHA256'}
assert set(a2['AUDIT_INPUT_PATHS'])=={r['path'] for r in manifest['inputs']}|{Q+'/INPUT_MANIFEST.json'}
assert a2['EXPECTED_GIT_BASE']==BASE and a2['EXPECTED_ROOT_REVIEW_SHA']=='0b71a5ba5117ffce4792ede1dc1c36f20f61b35025a62377254d05807b61c923'
assert a2['MANIFEST_SHA256']==pin(W/Q/'INPUT_MANIFEST.json')['sha256']
source_manifest=read(W/Q/'SOURCE_MANIFEST.json')
for row in source_manifest['sources']:same(W/row['recovery_path'],row);same(Path(row['original']),row)
assert (W/Q/'PUBLICATION_STATE.json').read_bytes()==(S/Q/'PUBLICATION_STATE.json').read_bytes()
actual=read(W/Q/'ACTUAL_BINDING.json');assert not actual['root_read_complete'] and actual['canonical_review_evidence'] is None
assert actual['git_base']==BASE and actual['parent_binding']==parent and actual['raw_bodies']==bodies and actual['source_body_pins']==old_bodies
def verify_portable(value):
 if isinstance(value,dict):
  if {'path','bytes','sha256'}<=set(value) and not Path(value['path']).is_absolute():same(W/value['path'],value)
  else:
   for child in value.values():verify_portable(child)
 elif isinstance(value,list):
  for child in value:verify_portable(child)
for name in ['ACTUAL_BINDING.json','CANONICAL_BINDING.json','ACTUAL_REFRESH_PROVENANCE.json','ROOT_ACCEPTANCE_EXECUTION.json']:verify_portable(read(W/Q/name))
for label in ['prepare_parent_base','prepare_local_base','prepare_duplicates']:
 receipt=read(I/'runs'/label/'EXECUTION.json');assert receipt['exit_code']==0
 for k in ['stdout','stderr','recorder']:same(Path(receipt[k]['path']),receipt[k])
assert read(I/'runs/prepare_parent_base/stdout')['headRefOid']==BASE
assert (I/'runs/prepare_local_base/stdout').read_text().strip()==BASE
assert read(I/'runs/prepare_duplicates/stdout')==[]
result={'kind':'root_canonical_source_review','utc':datetime.now(timezone.utc).isoformat(),'root_read_complete':True,'git_base':BASE,'bound_note_sha256':pin(W/NOTE)['sha256'],'canonical_body_pins':bodies,'parent_binding':parent,'source_draft_freeze_sha256':'d0997db66b3b7465a8a02a233a6d0b8c56cb48af6571a3659fa49852cb28700f','source_draft_review_sha256':'0b71a5ba5117ffce4792ede1dc1c36f20f61b35025a62377254d05807b61c923','prebinding_primary':pin(W/HELPER),'integration_common':pin(D/'bus_joint_energy_common.py'),'reviewed_canonicalization_diff':pin(I/'CANONICALIZATION.diff'),'read_scope':'Complete scientific wrapper changes, current primary/common implementation changes and canonical binding data read. Exact unchanged body/parent/archive bytes reused from complete earlier reviews; copied receipts and literal declared input inventories verified against actual source records. No fresh scientific rereview inferred from hashes.','changed_primary_assignments':sorted(changed),'verified_prepared_files':len(prepared['canonical_files']),'decision':'Canonical source and binding accepted for actual metadata primary/cache and scoped integration. Final binding mutations and staged content require verification.','scientific_programs_run':0,'retained_audit':False,'editable_prompt_files_changed':[]}
path=R/'CANONICAL_REVIEW.json';assert not path.exists();path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'review':pin(path),'canonical_files':len(prepared['canonical_files']),'science_replays':0},indent=2))
