from pathlib import Path
import hashlib, json, subprocess, urllib.request
from datetime import datetime, timezone
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent
REPO=BASE/'campaign-working'
COMMIT='0e6ad8285096ed668816f18caaa6fbbfbd9c50e8'
OUT=ROOT/'sources'
OUT.mkdir(exist_ok=True)
rows=[]
def sha(b): return hashlib.sha256(b).hexdigest()
def keep(name,b,**meta):
    p=OUT/name
    if p.exists(): assert p.read_bytes()==b, name
    else: p.write_bytes(b)
    row=dict(frozen_path=str(p.relative_to(ROOT)),bytes=len(b),sha256=sha(b),**meta)
    rows.append(row)
    print(json.dumps(row,sort_keys=True))

spec=[
('local_compensation.md','docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md','c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b'),
('local_pair_form.md','docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md','7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a'),
('electric_magnetic.md','docs/ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION_BOUNDED_THEOREM_NOTE_2026-09-24.md','eb5e31ae7e76f80383c454bf3e01ec98df2f503e93f04159b1cc11545d9996b4'),
('agent_pointer.md','AGENTS.md','9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6'),
('workflow.md','docs/ai_methodology/SCIENCE_WORKFLOW.md','d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4'),
]
for name,path,expected in spec:
    b=subprocess.check_output(['git','show',f'{COMMIT}:{path}'],cwd=REPO)
    assert sha(b)==expected,(path,sha(b),expected)
    role='conditional supplied mathematical premise; no audit status imported' if name not in ('agent_pointer.md','workflow.md') else 'previously read unchanged procedure'
    keep(name,b,repository=str(REPO),commit=COMMIT,path=path,expected_sha256=expected,role=role)
current=(REPO/'docs/ai_methodology/SCIENCE_WORKFLOW.md').read_bytes()
assert sha(current)==spec[-1][2],('current workflow changed',sha(current))

prior=BASE/'record-photon-readout-independent'
for name,expected in [
('PRE.md','7e5140e5155943d99541efc2e8de7cc25f9cee9ba4d4330b9906def5c3adf76d'),
('PRE_SEAL.json','65ef5734192d3ca88511a992fad2b1788582ad8acf632c2b2d33e866d121cff6'),
('POST.md','dc217d7ff74cb074998f2f4e92cd02b79e1bdb207c2f4ebfc0e6fd8e8ee96d1c'),
('POST_SEAL.json','f6cc670e09877d631658d8d150f986fecfcd5925b0ecfb7394bdcd17aee7513e'),
]:
    b=(prior/name).read_bytes(); assert sha(b)==expected,(name,sha(b))
    keep('readout_'+name,b,path=str(prior/name),expected_sha256=expected,role='own unchanged previously sealed reconstruction, explicitly reusable')
    if name.endswith('_SEAL.json'):
        seal=json.loads(b)
        print('prior seal structure',name,list(seal))

url='https://arxiv.org/pdf/1810.02428v1'
p=OUT/'NSY_1810.02428v1.pdf'
b=p.read_bytes() if p.exists() else urllib.request.urlopen(url,timeout=60).read()
assert b.startswith(b'%PDF')
keep(p.name,b,url=url,role='primary mathematical reference, bounded strongly continuous time-dependent interactions; only necessary Sections 2.2, 2.3.1 and 3.1 imported')
reader=PdfReader(p)
selected=list(range(6,12))+list(range(15,23))
text='\n\n'.join(f'=== PDF page {i+1}, index {i} ===\n'+(reader.pages[i].extract_text() or '') for i in selected)
keep('NSY_required_sections.txt',text.encode(),derived_from=p.name,pdf_page_indices=selected,role='complete selected pages for mathematical-premise reading, not entire paper')
pins=dict(phase='blind PRE',created_utc=datetime.now(timezone.utc).isoformat(),sources=rows,current_workflow_sha256=sha(current),forbidden_sources_opened=False)
(ROOT/'SOURCE_PINS.json').write_text(json.dumps(pins,indent=2)+'\n')
print('all expected source hashes and current workflow identity matched; source pin count',len(rows))
