#!/usr/bin/env python3
"""One-time local evidence manifest writer; not a read-only verifier."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

base=Path(__file__).resolve().parent
assert not (base/'EVIDENCE_PINS.json').exists()
sources=json.loads((base/'SOURCE_PINS_INITIAL.json').read_text())
for row in sources['sources']:
    assert hashlib.sha256(Path(row['origin']).read_bytes()).hexdigest()==row['sha256']
    assert hashlib.sha256((base/row['snapshot']).read_bytes()).hexdigest()==row['sha256']
sources['pre_seal_reverified_utc']=datetime.now(timezone.utc).isoformat()
(base/'SOURCE_PINS.json').write_text(json.dumps(sources,indent=2,sort_keys=True)+'\n')
rows=[]
for path in sorted(base.rglob('*')):
    if path.is_file():
        raw=path.read_bytes()
        rows.append(dict(path=str(path.relative_to(base)),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
manifest=dict(created_utc=datetime.now(timezone.utc).isoformat(),
              scope='PRE42 evidence fixed before read-only verification; manifest excludes itself and later verifier logs/seal',
              members=rows)
(base/'EVIDENCE_PINS.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
print(json.dumps(dict(evidence_members=len(rows),source_origins=len(sources['sources'])),indent=2))
