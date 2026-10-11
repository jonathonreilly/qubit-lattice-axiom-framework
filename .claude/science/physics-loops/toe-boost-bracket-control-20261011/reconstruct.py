"""Verify exact preservation and the explicit publication edits."""
from pathlib import Path
import gzip, hashlib, json
P=Path(__file__).resolve().parent
W=P.parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
d=json.loads((P/'PUBLICATION_EDITS.json').read_text())
parts=[d['prefix']]
for row in d['parts']:
 b=gzip.decompress((P/row['preserved_source']).read_bytes())
 assert sha(b)==row['source_sha256']
 t=b.decode()
 for e in row['edits']:
  assert t.count(e['before'])==1
  t=t.replace(e['before'],e['after'])
 parts.extend([t,row['separator']])
b=''.join(parts).encode()
assert sha(b)==d['publication_sha256']
assert (W/d['publication_path']).read_bytes()==b
print('PASS: complete argument source preservation and explicit publication edits')
