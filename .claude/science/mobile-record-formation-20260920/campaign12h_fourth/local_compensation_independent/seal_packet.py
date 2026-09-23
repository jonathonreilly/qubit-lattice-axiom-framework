#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,datetime
base=Path(__file__).resolve().parent
out=base/'PRE_COMPARISON_SEAL.json';assert not out.exists()
def bind(p):
 b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
sources=json.loads((base/'SOURCE_BINDINGS.json').read_text())['sources']
for row in sources:
 assert bind(Path(row['path']))=={k:row[k] for k in ['path','bytes','sha256']}
artifacts=[bind(p) for p in sorted(base.iterdir()) if p.is_file() and p!=out]
seal={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'type':'Independent reconstruction PRE comparison seal','read_boundary':'Only the neutral supplied construction, prior checked parent/general theorem, narrow general-target correction, and own earlier cube sources. No specific local-compensation author note/builder/seal or excluded packet accessed.','scientific_status':'Conditional fixed-graph statewise full-density convergence established; no publication/audit verdict. Ready for separately authorized author-source comparison.','sources':sources,'artifacts':artifacts,'failures':'No failed scientific runs. Countercontrols and exact read/rerun limits are retained in REPORT.md and full outputs.'}
out.write_text(json.dumps(seal,indent=2)+'\n')
for row in sources+artifacts:
 assert bind(Path(row['path']))=={k:row[k] for k in ['path','bytes','sha256']}
print(json.dumps({'report':bind(base/'REPORT.md'),'pre_seal':bind(out),'verified_sources':len(sources),'verified_artifacts':len(artifacts)},indent=2))
