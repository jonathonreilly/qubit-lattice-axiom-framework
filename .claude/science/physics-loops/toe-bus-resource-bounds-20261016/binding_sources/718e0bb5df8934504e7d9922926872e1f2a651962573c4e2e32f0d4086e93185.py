"""Record an actual root source review after deterministic identity checks."""
from pathlib import Path
from datetime import datetime, timezone
import ast, hashlib, json
N=Path(__file__).resolve().parents[1]
B=N/'bus_resource_publication_draft'; P=B/'proposal'
K=P/'.claude/science/physics-loops/toe-bus-resource-bounds-20261016'
O=N/'root_bus_resource_publication_review'
def read(p): return json.loads(Path(p).read_text())
def pin(p):
    p=Path(p); b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(p,r):
    x=pin(p); assert x['sha256']==r['sha256'] and x['bytes']==r['bytes'], str(p)
def write(p,obj):
    with Path(p).open('x') as f: f.write(json.dumps(obj,indent=2)+'\n')
freeze=read(B/'FINAL_FREEZE.json')
assert pin(B/'FINAL_FREEZE.json')['sha256']=='aca82160f36a6ea453871e9b732c0517c149112fc6147fd018d82b088f28b1db'
for row in freeze['members']: check(B/row['path'],row)
assert {str(p.relative_to(B)) for p in B.rglob('*') if p.is_file()}=={r['path'] for r in freeze['members']}|{'FINAL_FREEZE.json'}
archive=read(K/'ARCHIVE_INDEX.json')['sources']
for row in archive:
    check(row['original'],row); check(P/row['recovery'],row)
mapping=read(K/'BODY_MAP.json'); note=(P/mapping['note']).read_bytes()
assert note[:mapping['wrapper']['bytes']]==(B/'wrapper.md').read_bytes()
for row in mapping['bodies']:
    assert note[row['start_byte']:row['end_byte_exclusive']]==Path(row['original']).read_bytes()
    check(row['original'],row)
assert len(mapping['bodies'])==8
primary=P/'scripts/bus_resource_bounds_2026_10_16.py'; src=primary.read_text()
tree=ast.parse(src)
inputs=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='DECLARED_INPUTS' for t in n.targets))
assert src==(B/'primary_template.py').read_text().replace('@@DECLARED_INPUTS@@',repr(inputs))
for name,row in inputs.items(): check(P/name,row)
assert {str(p.relative_to(P)) for p in P.rglob('*') if p.is_file()}==set(inputs)|{str(primary.relative_to(P))}
manifest=read(K/'SOURCE_MANIFEST.json')
for frozen in manifest['freezes']:
    obj=read(frozen['original']); rows=obj[frozen['row_key']] if frozen['row_key'] else [obj]
    assert len(rows)==frozen['member_count']
    paths=[]
    for row in rows:
        p=Path(row['path']);p=p if p.is_absolute() else Path(frozen['base'])/p
        check(p,row); paths.append(str(p))
    assert paths==frozen['members']
parents=read(K/'PARENT_BINDING.json')['direct_canonical_parents']
for row in parents:
    check(N.parent/'correlation_worktree'/row['path'],row)
    assert (']('+Path(row['path']).name+')').encode() in note
assert len(parents)==4
expected={'build_01':1,'recovery_01':0,'build_02':0,'integrity_01':0,'parent_binding_01':0,'integrity_02':0,'controls_01':0,'default_refusal_01':2,'inspection_01':0,'final_check_01':0}
receipts=[]
for label,code in expected.items():
    folder=B/'metadata_runs'/label;e=read(folder/'EXECUTION.json');launch=read(folder/'LAUNCH.json')
    assert all(e[k]==v for k,v in launch.items())
    assert e['exit_code']==code and not e['timed_out']
    for key in ['source_at_launch','recorder_at_launch','stdout','stderr']:check(e[key]['path'],e[key])
    assert e['source_at_launch']['sha256']==e['source_original']['sha256']
    assert e['argv'][2]==str(folder/'source_at_launch.py') and e['cwd']==str(B)
    if label=='build_01': assert 'StopIteration' in (folder/'stderr').read_text()
    else: assert (folder/'stderr').read_bytes()==b''
    receipts.append(dict(label=label,receipt=pin(folder/'EXECUTION.json'),actual_exit=code))
old=(B/'build_packet.py').read_text()
corrected=old.replace("key=next(k for k in ['members','files'] if k in obj)","key=next((k for k in ['members','files'] if k in obj),None)").replace('rows=obj[key];members=[]','rows=obj[key] if key else [obj];members=[]')
assert corrected==(B/'build_packet_v2.py').read_text()
assert sum(p.is_file() for p in (B/'failed_build_01').rglob('*'))==23
assert len(read(B/'metadata_runs/controls_01/stdout')['scoped_in_memory_provenance_corruptions_rejected'])==6
assert read(B/'metadata_runs/default_refusal_01/stdout')['status']=='canonical-certification-refused'
result=dict(reviewed_utc=datetime.now(timezone.utc).isoformat(),status='source-only wrapper/code accepted for separately reviewed canonical integration; not retained audit',review=pin(O/'REVIEW.md'),source_freeze=pin(B/'FINAL_FREEZE.json'),source_note=pin(P/mapping['note']),source_primary=pin(primary),wrapper=pin(B/'wrapper.md'),frozen_members=len(freeze['members']),selected_live_sources=len(archive),immutable_bodies=8,declared_inputs=len(inputs),acceptance_reference_edges=len(manifest['acceptance_reference_edges']),metadata_receipts=receipts,scientific_reexecutions=0,cluster_cap='OPEN conditional on canonical conformance',actual_canonical_acceptance=None,actual_new_publication=None,retained_audit=False,editable_prompt_files_changed=[])
write(O/'REVIEW.json',result)
write(O/'FREEZE.json',dict(utc=result['reviewed_utc'],members=[pin(O/'REVIEW.md'),pin(O/'REVIEW.json'),pin(Path(__file__))],scope='Root source review and identity recording, not a new scientific execution.'))
print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),verified_source_paths=len(archive),immutable_bodies=8,scientific_executions=0),indent=2))
