from pathlib import Path
import json,hashlib,datetime,sys,platform
import numpy,scipy,sympy
D=Path(__file__).resolve().parent

def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r):assert row(Path(r['path']))==r,r['path']
sources=json.loads((D/'SOURCE_IDENTITIES.json').read_text())['sources']
for r in sources:verify(r)
(D/'RUNTIME.json').write_text(json.dumps({'python_executable':sys.executable,'python_version':sys.version,'platform':platform.platform(),'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__},indent=2)+'\n')
artifacts=[row(p) for p in sorted(D.iterdir()) if p.is_file() and p.name!='PRE_COMPARISON_SEAL.json']
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Independent reconstruction frozen before new author-source access; ready for bounded comparison, no formal audit or publication status.','sources':sources,'artifacts':artifacts,'prior_exposure':'Previously checked L=3 source and report are explicitly bound. No fourth-campaign author spectrum source, script, result, checkpoint or registry was read.','proved_scope':'Complete general-L unit-rotor H2 diagonalization, formation-output spectral measures, L=4 flat/dispersive weights and preparation limits, integer-winding components; only an initial subsequent-birth operator control.','failures_preserved':'One symbolic generator-assumption mismatch, original source and actual failed command streams/receipt retained; no scientific coefficient changed.','next_step':'Stop and await explicit authorization and exact author source identities for comparison.'}
assert not (D/'PRE_COMPARISON_SEAL.json').exists()
(D/'PRE_COMPARISON_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
for r in sources+artifacts:verify(r)
print(json.dumps({'report':row(D/'REPORT.md'),'pre_comparison_seal':row(D/'PRE_COMPARISON_SEAL.json'),'source_bindings':len(sources),'artifact_bindings':len(artifacts)},indent=2))
