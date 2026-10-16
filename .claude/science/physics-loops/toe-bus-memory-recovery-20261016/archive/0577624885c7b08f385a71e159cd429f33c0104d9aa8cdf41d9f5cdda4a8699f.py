"""Record root's analytical decision after complete source/check reads; no science execution."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
N=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
O=N/'bus_memory_recovery_root_review'
def read(p):return json.loads(p.read_text())
def pin(p):
 b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def same(p,r):assert all(pin(p)[k]==r[k] for k in ['bytes','sha256']),str(p)
def write(p,d):assert not p.exists();p.write_text(json.dumps(d,indent=2)+'\n')
expected={'bus_memory_recovery_root_proposal':'3235995b2bc6f90bcffe34355413181087288ff4540662c928b97341aa008ef0',
 'bus_memory_recovery_exposed_check':'a6e440713aaf7219621a58d8d2b0620b10ad14bdf1b9376aa27c9e8810588e3a',
 'bus_memory_recovery_candidate':'e30a9cf7396ad1e32ff10405006e1a34d361f529c8144a9989830b4a728d1415',
 'bus_memory_recovery_author_exposed_check':'ba58b86684d5fae32b3a31a893e86502a9cccd51e70c1dcf472a8c7ddd148ea4'}
verified=[]
for name,h in expected.items():
 P=N/name;f=P/'FREEZE.json';assert pin(f)['sha256']==h
 d=read(f);rows=d.get('files',d.get('members'))
 for row in rows:
  p=Path(row['path']);same(p if p.is_absolute() else P/p,row)
 verified.append(dict(freeze=pin(f),members=len(rows)))
for name in ['bus_memory_recovery_exposed_check','bus_memory_recovery_author_exposed_check']:
 P=N/name
 for row in read(P/'SOURCE_IDENTITIES.json')['sources']:
  same(Path(row['source']),row)
  if 'capture' in row:same(P/row['capture'],row)
for row in read(N/'bus_memory_recovery_candidate/SOURCE_MANIFEST.json')['sources']:same(Path(row['path']),row)
P=N/'bus_memory_recovery_author_exposed_check';e=read(P/'metadata_capture/EXECUTION.json')
assert e['exit_code']==0 and e['scientific_execution'] is False and e['source_unchanged_after_run'] is True
for key in ['stdout','stderr']:same(P/e[key]['path'],e[key])
assert (P/e['source_at_launch']).read_bytes()==(P/'capture_sources.py').read_bytes()
assert pin(P/e['source_at_launch'])['sha256']==e['source_sha256']
assert pin(P/'run_metadata_capture.py')['sha256']==e['launcher_sha256']
accept=dict(utc=datetime.now(timezone.utc).isoformat(),status='qualified source acceptance of two distinct conditional driven endpoint recovery constructions',
 controlling_qualifications=pin(O/'FINAL_QUALIFICATIONS.md'),
 primary_author_derivation=pin(N/'bus_memory_recovery_candidate/DERIVATION.md'),
 primary_exposed_check=pin(N/'bus_memory_recovery_author_exposed_check/REVIEW.md'),
 alternative_root_pre_result=pin(N/'bus_memory_recovery_root_proposal/PRE_RESULT_SKETCH.md'),
 alternative_exposed_check=pin(N/'bus_memory_recovery_exposed_check/REVIEW.md'),source_freezes_verified=verified,
 mathematical_parents=[pin(N/'bus_preparation_root_review/QUALIFIED_ACCEPTANCE.json'),pin(N/'bus_bounded_slew_preparation_root_review/QUALIFIED_ACCEPTANCE.json'),pin(N.parent/'correlation_worktree/docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md')],
 actual_metadata_receipt=pin(P/'metadata_capture/EXECUTION.json'),scientific_executions=0,historical_scientific_replays=0,
 root_complete_reads=True,load_bearing_checks=['Full stored A_C inversion after SWAP, including unknown entangled C.','Opposite-axis source rotation phase pi*n_S/2 in author schedule; different scalar in full-inverse route.','Full old-H ordering and actual scalar reserves.','Weak full-space absolute-area errors including the zero-signed-area return ramp.','Local nominal caps, global action/work and observable-norm moment allowances.','Finite repeated-use trace telescope with readiness counted once and all idle/control intervals retained.'],
 independence='Root pre-result route precedes separate author route; checker is source-exposed and knew root route before checking author. Same model and shared qualified parents, not blind/different-model replication or retained audit.',
 additional_physical_premise='Explicit u in[0,2] complement access and headroom; native control, microscopic driver outputs and measured energy remain unsupplied.',
 failed_shortcuts_preserved=['Ignoring stored U_E phase.','Dropping old-port error on a zero-signed-area ramp.','Using preparation rather than runtime output phase.','Transplanting scalar phases between the two different schedules.'],
 publication=None,retained_audit=False,editable_prompt_files_changed=[])
write(O/'QUALIFIED_ACCEPTANCE.json',accept)
write(O/'FREEZE.json',dict(utc=datetime.now(timezone.utc).isoformat(),status='qualified source decision, not retained audit',files=[pin(O/f) for f in ['FINAL_QUALIFICATIONS.md','QUALIFIED_ACCEPTANCE.json','record_acceptance.py']]))
print(json.dumps({'acceptance':pin(O/'QUALIFIED_ACCEPTANCE.json'),'freeze':pin(O/'FREEZE.json')},indent=2))
