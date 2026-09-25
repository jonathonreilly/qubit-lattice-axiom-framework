"""Freeze four permitted scientific parents and unchanged procedure identities."""
from pathlib import Path
import datetime,hashlib,json,subprocess
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
REPO=BASE/'native-ground-publication'
REV='d3dfdff92b6eb9e422da3691d13af4c249b7c4e9'
sha=lambda b:hashlib.sha256(b).hexdigest()
items=[
('NATIVE_GROUND_ENERGY_AND_ORIGINAL_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-25.md','d709a13f913f0f16cce7f4fe4ae47ebfc90dc8d90b1fcd0cf0c952337bedcf7b'),
('LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a'),
('LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b'),
('FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md','2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516')]
(HERE/'sources').mkdir()
rows=[]
for name,expected in items:
 p=REPO/'docs'/name;body=p.read_bytes();git=subprocess.check_output(['git','show',f'{REV}:docs/{name}'],cwd=REPO)
 assert body==git and sha(body)==expected
 dest=HERE/'sources'/name
 with dest.open('xb') as f:f.write(body)
 rows.append({'origin':str(p),'frozen_path':str(dest.relative_to(HERE)),'revision':REV,'sha256':expected,'bytes':len(body),'exact_git_object':True,'role':'Supplied conditional parent, unchanged complete prior reading reused; no runtime/author/review source imported for new control.'})
for rel,expected in [('AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),('docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4')]:
 p=REPO/rel;body=p.read_bytes();assert sha(body)==expected
 dest=HERE/'sources'/p.name
 with dest.open('xb') as f:f.write(body)
 rows.append({'origin':str(p),'frozen_path':str(dest.relative_to(HERE)),'sha256':expected,'bytes':len(body),'role':'Unchanged applicable procedure, earlier complete reading reused.'})
ref=subprocess.check_output(['git','rev-parse','origin/ai/execution'],cwd=REPO,text=True).strip()
body=subprocess.check_output(['git','show',ref+':AGENTS.md'],cwd=REPO)
assert ref=='eb1f1ca8338848cf2046582e13aef372d8540937' and sha(body)=='b72ba953ee650b464b7987c71de3415de590be5aa42451240525a2b2585312e7'
dest=HERE/'sources/AGENTS_execution.md'
with dest.open('xb') as f:f.write(body)
rows.append({'origin':'git:origin/ai/execution:AGENTS.md','repository':str(REPO),'revision':ref,'frozen_path':str(dest.relative_to(HERE)),'sha256':sha(body),'bytes':len(body),'role':'Unchanged instruction ref, earlier complete reading reused; no fetch or repository mutation.'})
packet={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'phase':'Blind bounded PRE check40','sources':rows,'historical_exposure':'Earlier root33/35/36 source and separate PRE/POST checks were read in earlier authorized tasks. New task imports only four exact public parent notes; no earlier runtime or review packet is used to compute the new control.','forbidden_candidate_read':False,'new_author_controls_imported_or_executed':False,'delegation':False}
with (HERE/'SOURCE_PINS.json').open('x') as f:json.dump(packet,f,indent=2);f.write('\n')
print(json.dumps(packet,indent=2))
