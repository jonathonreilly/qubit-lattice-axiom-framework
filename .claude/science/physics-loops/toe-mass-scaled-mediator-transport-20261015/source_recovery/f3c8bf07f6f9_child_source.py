#!/usr/bin/env python3
"""Final source/copy freshness check only; no scientific verification."""
from pathlib import Path
import hashlib,json,datetime
ROOT=Path(__file__).resolve().parent
def ident(p):
    b=p.read_bytes(); return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
verified=[]
for row in manifest['sources']:
    p=Path(row['path']); got=ident(p)
    assert got['bytes']==row['bytes'] and got['sha256']==row['sha256'],str(p)
    if row['recovery_copy']:
        assert (ROOT/row['recovery_copy']).read_bytes()==p.read_bytes(),row['recovery_copy']
    verified.append(got)
result={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Exact source identities and recovery copies only; no scientific run.','sources':verified,'source_count':len(verified),'recovery_copy_count':sum(r['recovery_copy'] is not None for r in manifest['sources']),'report':ident(ROOT/'REPORT.md'),'coverage':ident(ROOT/'READ_COVERAGE.md')}
(ROOT/'FINAL_SOURCE_RECHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='sources'},indent=2))
