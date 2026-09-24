"""Authenticate this selected public projection, not a scientific verdict."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;REPO=HERE.parents[3];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((HERE/'PUBLICATION_UNIT_ACTUAL_ENERGY_TAIL.json').read_text())
assert m['base_pr']==8957 and m['base_commit']=='fb9edf315aed8192ea03873fe8e83882dbaf1502'
for key in ('artifacts','sources'):
 seen=set()
 for r in m[key]:
  assert r['path'] not in seen;seen.add(r['path']);p=HERE/r['path'];assert sha(p)==r['sha256'] and p.stat().st_size==r['bytes'],r['path']
omitted={r['path']:r for r in m['explicit_omissions']}
for r in m['seals']:
 p=HERE/r['path'];assert sha(p)==r['sha256'];s=json.loads(p.read_text())
 for a in s.get('artifacts',s.get('files',[])):
  q=p.parent/a['path'];name=str(q.relative_to(HERE))
  if name in omitted:assert not q.exists() and omitted[name]['sha256']==a['sha256']
  else:assert sha(q)==a['sha256'] and q.stat().st_size==a['bytes'],name
 for a in s.get('sources',[]):assert sha(REPO/a['path'])==a['sha256'],a['path']
f=json.loads((HERE/'fast_band_tail_rate_independent/FINAL_SEAL.json').read_text());assert not f['mathematical_corrections_required'] and f['new_scientific_numerical_executions']==0
print('Source closure verified: actual fixed-input lower bound; no audit verdict.')
