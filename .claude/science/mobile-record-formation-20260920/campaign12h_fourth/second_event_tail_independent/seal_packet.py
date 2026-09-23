from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
D=Path(__file__).resolve().parent
def row(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r):assert row(Path(r['path']))==r,r['path']
binding=json.loads((D/'SOURCE_BINDINGS.json').read_text())
for r in binding['source_rows']:verify(r)
receipts=[]
for prefix,result in [('tail_run','TAIL_RESULTS.json'),('provenance_run','SOURCE_BINDINGS.json')]:
 r=json.loads((D/(prefix+'_RECEIPT.json')).read_text())
 assert r['exit_code']==0
 for key in ('runner','stdout','stderr'):verify(r[key])
 assert not (D/(prefix+'.stderr')).read_bytes()
 assert (D/(prefix+'.stdout')).read_bytes()==(D/result).read_bytes()
 receipts.append(row(D/(prefix+'_RECEIPT.json')))
files=sorted(p for p in D.iterdir() if p.is_file() and p.name!='PRE_COMPARISON_SEAL.json')
assert len(files)==13,[p.name for p in files]
out={'created_utc':datetime.now(timezone.utc).isoformat(),
 'status':'Independent long-time/moment reconstruction frozen before new author access; no formal audit or publication status.',
 'read_boundary':binding['read_boundary'],
 'known_unopened_author_seal_sha256':binding['known_unopened_author_seal_sha256'],
 'sources':binding['source_rows'],'artifacts':[row(p) for p in files],
 'actual_receipts':receipts,'failed_attempts':[],
 'findings':['For a=eta-4 delta !=0 and a single circulation, S(t)~t^(-3/2)/(32|a|sqrt(2 pi kappa)).',
             'Mean=3/(8 kappa); positive moments exist exactly below order 3/2 for that input.',
             'At a=0 the law is Exp(4 kappa); general field densities obey the stated weighted inverse-frequency integrability criterion.',
             'Normalizable packets can have finite second moments, and coherent preparation can cancel one leading angular tail.',
             'Fast-limit moment passage is qualified separately from uniform survival convergence.'],
 'limits':['The supplied effective unit-rotor ring only; no finite-spin, microscopic conditioned-history or large-volume assertion.',
           'Finite quadratures corroborate analytic identities and tail proofs; no numerical grid is substituted for those proofs.',
           'Prior ring-spectrum and second-event author comparison were already known; the new tail author packet remains unopened.']}
target=D/'PRE_COMPARISON_SEAL.json';assert not target.exists()
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'report':row(D/'REPORT.md'),'PRE':row(target),'sources':len(out['sources']),'artifacts':len(out['artifacts'])},indent=2))
