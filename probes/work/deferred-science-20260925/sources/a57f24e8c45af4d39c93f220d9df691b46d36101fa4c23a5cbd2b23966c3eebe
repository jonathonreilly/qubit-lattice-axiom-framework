"""One additional procedural source, never executed or imported."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
HERE=Path(__file__).resolve().parent
EXT=HERE.parent.parent
origin=EXT/'birth-charge-transport-publication/docs/audit/scripts/write_citation_graph_manifest.py'
st=origin.stat();raw=origin.read_bytes()
target=HERE/'sources/mechanical_graph_manifest_writer.py'
with target.open('xb') as f:f.write(raw)
pin=dict(origin=str(origin),snapshot=str(target.relative_to(HERE)),sha256=sha256(raw).hexdigest(),
         bytes=len(raw),mode=st.st_mode,dev=st.st_dev,ino=st.st_ino,
         mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns,nlink=st.st_nlink,
         role='Read-only mechanical dependency-hash convention; source never imported/executed')
result=dict(at_utc=datetime.now(timezone.utc).isoformat(),sources=[pin])
with (HERE/'MECHANICAL_SOURCE_PINS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
