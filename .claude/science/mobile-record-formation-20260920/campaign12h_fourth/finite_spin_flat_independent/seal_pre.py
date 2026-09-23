import hashlib,json,sys,platform,datetime
from pathlib import Path
import numpy,scipy,sympy
here=Path(__file__).resolve().parent
sources=json.loads((here/'SOURCE_IDENTITIES.json').read_text())
for entry in sources['sources']:
    p=Path(entry['path'])
    assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],str(p)
runtime={'python':sys.version,'platform':platform.platform(),'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__}
(here/'RUNTIME.json').write_text(json.dumps(runtime,indent=2)+'\n')
items=[]
for p in sorted(here.iterdir()):
    if not p.is_file() or p.name=='PRE_COMPARISON_SEAL.json':continue
    b=p.read_bytes();items.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
seal={'stage':'PRE_COMPARISON','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'task':'Selective independent reconstruction of the prepared physical flat-sector joint-spin limit on the eight-site ring.','source_access':'Only the explicitly permitted fast-target and checked ring-spectrum sources in SOURCE_IDENTITIES.json were read. Candidate finite_spin_post_birth_author, second_event_author, fourth-campaign checkpoint, registries and other new result summaries remain unopened.','exposure':'Sent parent concise compact-frame, operator and crossing-corrector progress during reconstruction. Parent reported its candidate proof had already been written when those messages arrived, before its author freeze; candidate source itself was not read.','disposition':'Prepared-sector conditional limit reconstructed with an explicit gapless core-corrector proof, exact finite combinatorial identities, finite-spin controls and full scope qualifications. Not a source review verdict or formal audit.','open_boundaries':['Candidate-source comparison not yet performed.','Entire unselected first-mark output ordinary-time limit not established.','Microscopic random-event flat-selection restart not established.'],'preserved_failure':'Original subtractive norm-difference diagnostics and execution artifacts are retained; stable vector-residual diagnostics replace them in the final numeric controls. Electric leakage counterexample retained.','sources':sources,'artifacts':items,'excluded_artifacts':'Python bytecode cache; no scientific evidence is omitted.','scope':'Only the assigned independent directory was written. No Git mutation, audit application, publication, external messaging or onward delegation.'}
p=here/'PRE_COMPARISON_SEAL.json';p.write_text(json.dumps(seal,indent=2)+'\n')
print(json.dumps({'seal':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bound_artifact_count':len(items),'bound_source_count':len(sources['sources'])},indent=2))
