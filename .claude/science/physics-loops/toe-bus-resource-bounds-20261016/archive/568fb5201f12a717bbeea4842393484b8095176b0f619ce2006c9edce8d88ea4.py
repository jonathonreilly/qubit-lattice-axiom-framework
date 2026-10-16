from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
O=Path(__file__).resolve().parent;N=O.parent;R=N/'reachable_bus_corrector_exposed_check';P=N/'reachable_bus_corrector_root_proposal'
def pin(p):
 p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(p):return json.loads(Path(p).read_text())
def same(p,row):
 q=pin(p);assert all(q[k]==row[k] for k in ('bytes','sha256')),str(p)
assert pin(R/'FREEZE.json')['sha256']=='de219af2c75464ce0bfb009ff7d45a85d90b7385c828e1036a35885556ed531e'
freeze=read(R/'FREEZE.json')
for row in freeze['files']:same(R/row['path'],row)
assert {str(p.relative_to(R)) for p in R.rglob('*') if p.is_file()}=={row['path'] for row in freeze['files']}|{'FREEZE.json'}
sources=read(R/'SOURCE_MANIFEST.json')['sources']
for row in sources:same(row['path'],row);same(R/row['captured'],row)
assert pin(P/'PROPOSED_LEMMAS.md')['sha256']==freeze['source_proposal_sha256']
receipts=[]
for label in ['source_envelope','exact_gram']:
 d=R/'runs'/label;e=read(d/'EXECUTION.json');l=read(d/'LAUNCH.json')
 assert e['exit_code']==0 and not e['timed_out'] and e['start_utc']<=e['end_utc'] and e['elapsed_seconds']>0
 for k,v in l.items():assert e[k]==v
 for k in ['source_at_launch','source_capture','launcher_at_launch','launcher_capture','source_inputs','stdout','stderr']:same(e[k]['path'],e[k])
 assert e['source_at_launch']['sha256']==e['source_capture']['sha256'] and e['launcher_at_launch']['sha256']==e['launcher_capture']['sha256']
 assert e['argv'][1]=='-B' and e['argv'][2]==e['source_capture']['path'] and e['argv'][3]==str(R) and e['cwd']==str(R)
 assert Path(e['stderr']['path']).read_bytes()==b''
 receipts.append(pin(d/'EXECUTION.json'))
scope=read(R/'SOURCE_COVERAGE.json');source=(R/'sources/02_STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md').read_bytes()
for row in scope['parent_read_intervals']:
 b=source[row['start_byte_inclusive']:row['end_byte_exclusive']];assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
assert pin(R/'REVIEW.md')['sha256']=='63570fc9f63958d4d59742a24864046e1a6e28dc73a6ccccfc0c1a81d30f4031'
value={'utc':datetime.now(timezone.utc).isoformat(),'kind':'qualified_mathematical_source_acceptance','status':'Accepted with explicit restricted source inverse and full residual norms; unpublished, no retained audit.','proposal':pin(P/'PROPOSED_LEMMAS.md'),'proposal_freeze':pin(P/'FREEZE.json'),'review':pin(R/'REVIEW.md'),'review_freeze':pin(R/'FREEZE.json'),'qualifications':pin(O/'FINAL_QUALIFICATIONS.md'),'actual_scientific_receipts':receipts,'frozen_members_verified':len(freeze['files']),'source_captures_verified':len(sources),'root_read_complete_changed_argument_and_executables':True,'root_scientific_executions':0,'historical_replays':0,'polynomial_total_runtime_established':False,'retained_audit':False,'canonical_mutations':False,'editable_prompt_files_changed':[]}
(O/'QUALIFIED_ACCEPTANCE.json').write_text(json.dumps(value,indent=2)+'\n')
members=[pin(O/n) for n in ['FINAL_QUALIFICATIONS.md','record_acceptance.py','QUALIFIED_ACCEPTANCE.json']]
(O/'FREEZE.json').write_text(json.dumps({'utc':value['utc'],'members':members,'scope':'Qualified source acceptance only; actual enclosing execution captured separately.'},indent=2)+'\n')
print(json.dumps({'acceptance':pin(O/'QUALIFIED_ACCEPTANCE.json'),'freeze':pin(O/'FREEZE.json'),'scientific_programs_run':0}))
