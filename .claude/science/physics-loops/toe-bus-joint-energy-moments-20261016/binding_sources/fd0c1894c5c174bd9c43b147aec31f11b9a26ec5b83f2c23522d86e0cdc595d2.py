from pathlib import Path
from datetime import datetime,timezone
import ast,copy,hashlib,json,subprocess
O=Path(__file__).resolve().parent;N=O.parent;P=N/'bus_joint_energy_graph_recovery_proposal';W=N.parent/'correlation_worktree';I=N/'publication_integration/bus_joint_energy';R=I/'graph_recovery_01'
Q='.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016';NOTE='docs/BUS_JOINT_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md';HELPER='scripts/bus_joint_energy_moments_2026_10_16.py'
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(Path(p).read_text())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ('bytes','sha256')),str(p)
records={r['path']:r for r in read(P/'SOURCE_MANIFEST.json')['sources']}
def before(name):
 row=records[str(W/name)];same(P/row['captured_path'],row);return (P/row['captured_path']).read_bytes()
prepared=read(R/'PREPARED.json')
for name,row in prepared['canonical_files'].items():same(W/name,row)
old=before(NOTE);new=(W/NOTE).read_bytes();append=b'\n\nDirect mathematical parent: [Strongly regular bus bounded theorem](STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md).\n'
assert new==old+append and pin(W/NOTE)['sha256']=='c55b35da1d25c03d66f5d6a7750ab1b7e2def371a821d5d77426640f2bb2ca49'
for name in ['BODY_MAP.json','PARENT_BINDING.json']:assert (W/Q/name).read_bytes()==before(Q+'/'+name)
for row in read(W/Q/'BODY_MAP.json')['bodies']:
 b=new[row['start_byte_inclusive']:row['end_byte_exclusive']];assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
a=json.loads(before(Q+'/ACTUAL_BINDING.json'));a['prior_canonical_review_evidence']=copy.deepcopy(a['canonical_review_evidence']);a.update(canonical_review_evidence=None,root_read_complete=False,note_sha256=pin(W/NOTE)['sha256'],canonical_execution_not_yet_performed=True);assert a==read(W/Q/'ACTUAL_BINDING.json')
c=json.loads(before(Q+'/CANONICAL_BINDING.json'));c['prior_canonical_review']=copy.deepcopy(c['canonical_review']);c.update(canonical_review=None,root_read_complete=False,bound_note_sha256=pin(W/NOTE)['sha256']);assert c==read(W/Q/'CANONICAL_BINDING.json')
m=json.loads(before(Q+'/INPUT_MANIFEST.json'))
for row in m['inputs']:
 current=pin(W/row['path']);row.update({k:current[k] for k in ['bytes','sha256']})
assert m==read(W/Q/'INPUT_MANIFEST.json')
old_tree=ast.parse(before(HELPER));new_tree=ast.parse((W/HELPER).read_bytes())
for t in [old_tree,new_tree]:
 for a in t.body:
  if isinstance(a,ast.Assign) and any(isinstance(k,ast.Name) and k.id=='MANIFEST_SHA256' for k in a.targets):a.value=ast.Constant(value='verified_manifest_hash')
assert ast.dump(old_tree)==ast.dump(new_tree)
for name,row in read(I/'BOUND_CANONICAL.json')['canonical_files'].items():
 if name not in [NOTE,HELPER,Q+'/ACTUAL_BINDING.json',Q+'/CANONICAL_BINDING.json',Q+'/INPUT_MANIFEST.json']:same(W/name,row)
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip();assert head=='68c531309ac6dae96289aab964213b8c5f55969b'
assert read(R/'actions/repair/EXECUTION.json')['exit_code']==0
v=read(N/'root_bus_joint_energy_integration_review/CANONICAL_REVIEW.json')
v.update(utc=datetime.now(timezone.utc).isoformat(),bound_note_sha256=pin(W/NOTE)['sha256'],prebinding_primary=pin(W/HELPER),integration_common=pin(P/'recovery_common.py'),reviewed_canonicalization_diff=pin(R/'CANONICALIZATION.diff'),read_scope='New127-byte parent citation read; both mathematical bodies and all other note bytes exactly unchanged. Complete recovery implementation reviewed separately. Canonical binding changes checked against exact intended null-current/preserve-prior transforms; every manifest pin checked, primary AST unchanged except manifest digest. Earlier complete scientific reads reused at identical premises/scope.',changed_primary_assignments=['MANIFEST_SHA256'],verified_prepared_files=len(prepared['canonical_files']),prior_canonical_review=pin(N/'root_bus_joint_energy_integration_review/CANONICAL_REVIEW.json'),implementation_review=pin(O/'REVIEW.json'),decision='Amended canonical note and pending bindings accepted for actual new canonical-review binding and scoped recovery checks. Failed original graph remains preserved; final staged review and publication are separate.')
f=O/'CANONICAL_REVIEW.json';assert not f.exists();f.write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'review':pin(f),'scientific_programs_run':0}))
