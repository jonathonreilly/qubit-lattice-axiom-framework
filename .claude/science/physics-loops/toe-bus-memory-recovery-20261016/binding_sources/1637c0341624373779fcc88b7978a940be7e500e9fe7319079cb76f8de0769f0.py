"""Record completed source review with deterministic metadata checks only."""
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023');B=N/'bus_memory_recovery_publication_draft';P=B/'proposal';R=N/'root_bus_memory_recovery_publication_review';W=N.parent/'correlation_worktree'
K='.claude/science/physics-loops/toe-bus-memory-recovery-20261016';NOTE='docs/BUS_MEMORY_RECOVERY_BOUNDED_THEOREM_NOTE_2026-10-16.md';PRIMARY='scripts/bus_memory_recovery_2026_10_16.py'
def read(p):return json.loads(p.read_text())
def pin(p):
 p=Path(p);b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,row):assert all(pin(p)[k]==row[k] for k in ('bytes','sha256')),str(p)
def write(p,v):assert not p.exists();p.write_text(json.dumps(v,indent=2)+'\n')
assert pin(B/'FINAL_FREEZE.json')['sha256']=='5f680ad2dcd99182bd6e023e879963c8c23b6b22d8b737045c1ab50ad91c5e49'
members=read(B/'FINAL_FREEZE.json')['members'];assert len(members)==179
for row in members:same(B/row['path'],row)
assert {str(p.relative_to(B)) for p in B.rglob('*') if p.is_file()}=={r['path'] for r in members}|{'FINAL_FREEZE.json'}
archive=read(P/K/'ARCHIVE_INDEX.json');assert len(archive['sources'])==165 and archive['deduplicated_blobs']==118
for row in archive['sources']:same(row['original'],row);same(P/row['recovery'],row)
mapping=read(P/K/'BODY_MAP.json');note=(P/NOTE).read_bytes();assert len(mapping['bodies'])==5
assert note[:mapping['wrapper']['bytes']]==(B/'wrapper.md').read_bytes()
for row in mapping['bodies']:
 body=note[row['start_byte']:row['end_byte_exclusive']];assert body==Path(row['original']).read_bytes() and note.count(body)==1
 assert hashlib.sha256(body).hexdigest()==row['sha256'] and len(body)==row['bytes']
source=(P/PRIMARY).read_text();tree=ast.parse(source)
inputs=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='DECLARED_INPUTS' for t in n.targets))
assert len(inputs)==125
assert source==(B/'primary_template.py').read_text().replace('@@DECLARED_INPUTS@@',repr(inputs))
for name,row in inputs.items():same(P/name,row)
assert {str(p.relative_to(P)) for p in P.rglob('*') if p.is_file()}==set(inputs)|{PRIMARY}
manifest=read(P/K/'SOURCE_MANIFEST.json');count=0
for frozen in manifest['freezes']:
 value=read(Path(frozen['original']));rows=value[frozen['row_key']] if frozen['row_key'] else [value]
 assert len(rows)==frozen['member_count']
 for row in rows:
  p=Path(row['path']);p=p if p.is_absolute() else Path(frozen['base'])/p;same(p,row);count+=1
assert len(manifest['freezes'])==8 and count==113
parents=read(P/K/'PARENT_BINDING.json');assert len(parents['direct_canonical_parents'])==2
for row in parents['direct_canonical_parents']:same(W/row['path'],row)
reuse=read(B/'PROTOCOL_REUSE_MAP.json')
same(B/'record_metadata.py',reuse['source_recorder'])
same(B/'primary_template.py',reuse['current_primary_template'])
def functions(p):
 s=p.read_text().replace('@@DECLARED_INPUTS@@','{}');return {n.name:ast.get_source_segment(s,n) for n in ast.parse(s).body if isinstance(n,ast.FunctionDef)}
a=functions(Path(reuse['source_primary_template']['path']));b=functions(B/'primary_template.py')
for row in reuse['unchanged_functions']:assert a[row['name']]==b[row['name']]
runs=[]
for label,code in [('build_01',0),('integrity_01',0),('controls_01',0),('default_refusal_01',2),('inspection_01',0)]:
 d=B/'metadata_runs'/label;e=read(d/'EXECUTION.json');launch=read(d/'LAUNCH.json')
 assert all(e[k]==v for k,v in launch.items()) and e['exit_code']==code and not e['timed_out']
 assert e['cwd']==str(B) and e['argv'][2]==str(d/'source_at_launch.py')
 for key in ['source_original','source_at_launch','recorder_at_launch','stdout','stderr']:same(e[key]['path'],e[key])
 assert (d/'stderr').read_bytes()==b''
 runs.append(dict(label=label,receipt=pin(d/'EXECUTION.json'),exit_code=code))
assert len(read(B/'metadata_runs/controls_01/stdout')['scoped_in_memory_provenance_corruptions_rejected'])==6
state=read(P/K/'PUBLICATION_STATE.json')
assert state['actual_canonical_binding'] is None and state['actual_root_wrapper_code_approval'] is None and state['git_base'] is None
review=dict(utc=datetime.now(timezone.utc).isoformat(),status='source-only wrapper/code accepted for separately reviewed canonical integration; not retained audit',
 review=pin(R/'REVIEW.md'),source_freeze=pin(B/'FINAL_FREEZE.json'),source_note=pin(P/NOTE),primary=pin(P/PRIMARY),
 controlling_acceptance=pin(N/'bus_memory_recovery_root_review/QUALIFIED_ACCEPTANCE.json'),immutable_bodies=5,
 body_pins=mapping['bodies'],parent_binding=parents,selected_sources=165,selected_archive_blobs=118,immediate_freezes=8,frozen_member_rows=113,
 historical_process_records=9,historical_scientific_runs=3,new_metadata_runs=runs,provenance_negative_controls=6,
 current_main_revision='2cf2a218d582458d4d8807cd6196ab72b6a4bff1',instruction_revision='56c5c0ab64f532c5784e895b2f9aa6894fa334e0',
 scope='Two distinct conditional driven memory recovery schedules; exact source/read/receipt scope in REVIEW.md. Mathematical parents bus and preparation only; Git base still unbound.',
 cluster_cap_judgment='OPEN for this coherent reviewed recovery milestone, conditional on actual canonical conformance; no audit verdict applied.',
 scientific_reexecutions=0,actual_canonical_acceptance=None,retained_audit=False,editable_prompt_files_changed=[])
write(R/'REVIEW.json',review)
write(R/'FREEZE.json',dict(utc=datetime.now(timezone.utc).isoformat(),files=[pin(R/f) for f in ['REVIEW.md','REVIEW.json']],scientific_executions=0))
print(json.dumps(dict(review=pin(R/'REVIEW.json'),freeze=pin(R/'FREEZE.json'),verified_source_paths=165,immutable_bodies=5,scientific_executions=0),indent=2))
