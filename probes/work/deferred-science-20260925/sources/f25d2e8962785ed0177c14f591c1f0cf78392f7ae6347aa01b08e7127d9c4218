from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent/'campaign-working'
COMMIT='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8'
OUT=ROOT/'sources';OUT.mkdir(exist_ok=True)
def sha(b):return hashlib.sha256(b).hexdigest()
sources=[]
def keep(name,b,**meta):
    p=OUT/name
    if p.exists():assert p.read_bytes()==b
    else:p.write_bytes(b)
    row=dict(frozen_path=str(p.relative_to(ROOT)),bytes=len(b),sha256=sha(b),**meta)
    sources.append(row);print(json.dumps(row,sort_keys=True))
spec=[
('local_compensation.md','docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b'),
('local_pair_form.md','docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a'),
('electric_magnetic.md','docs/ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION_BOUNDED_THEOREM_NOTE_2026-09-24.md','eb5e31ae7e76f80383c454bf3e01ec98df2f503e93f04159b1cc11545d9996b4'),
('weak_field_packets.md','docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf'),
('workflow.md','docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
('agent_pointer.md','AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6')]
for name,path,expected in spec:
    b=subprocess.check_output(['git','show',COMMIT+':'+path],cwd=REPO)
    assert sha(b)==expected,(path,sha(b),expected)
    keep(name,b,repository=str(REPO),commit=COMMIT,path=path,expected_sha256=expected,
         role='conditional supplied mathematical premise' if name not in ('workflow.md','agent_pointer.md') else 'previously read unchanged procedure')
current=sha((REPO/'docs/ai_methodology/SCIENCE_WORKFLOW.md').read_bytes())
assert current==spec[-2][2]
prior=ROOT.parent/'record-photon-readout-independent'
for name,expected in [
('PRE.md','7e5140e5155943d99541efc2e8de7cc25f9cee9ba4d4330b9906def5c3adf76d'),
('POST.md','dc217d7ff74cb074998f2f4e92cd02b79e1bdb207c2f4ebfc0e6fd8e8ee96d1c'),
('PRE_SEAL.json','65ef5734192d3ca88511a992fad2b1788582ad8acf632c2b2d33e866d121cff6'),
('POST_SEAL.json','f6cc670e09877d631658d8d150f986fecfcd5925b0ecfb7394bdcd17aee7513e')]:
    b=(prior/name).read_bytes();assert sha(b)==expected
    keep('readout_'+name,b,path=str(prior/name),expected_sha256=expected,role='own unchanged prior reconstruction, explicitly authorized reuse')
result=dict(phase='blind independent PRE',created_utc=datetime.now(timezone.utc).isoformat(),sources=sources,
            current_workflow_sha256=current,author_or_forbidden_packets_read=False)
(ROOT/'SOURCE_PINS.json').write_text(json.dumps(result,indent=2)+'\n')
print('all',len(sources),'source identities and current workflow verified')
