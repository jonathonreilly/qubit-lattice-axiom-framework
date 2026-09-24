"""Authenticate a public projection with explicit private provenance omissions."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((HERE/'PUBLICATION_UNIT_AUTONOMOUS_CLOCK.json').read_text())
assert m['base_pr']==8929 and m['base_commit']=='413c01cc40fd085380125c8e1ec66a61f503eee3'
for key in ('artifacts','sources'):
 seen=set()
 for r in m[key]:
  assert r['path'] not in seen;seen.add(r['path']);p=HERE/r['path']
  assert p.stat().st_size==r['bytes'] and sha(p)==r['sha256'],r['path']
omitted={r['path']:r for r in m['explicit_omissions']};assert len(omitted)==4
assert sum('/instructions/' in x for x in omitted)==3
for seal in m['seals']:
 p=HERE/seal['path'];assert sha(p)==seal['sha256'];s=json.loads(p.read_text())
 for r in s.get('files',s.get('artifacts',[])):
  q=p.parent/r['path'];name=str(q.relative_to(HERE))
  if name in omitted:
   assert not q.exists() and r['sha256']==omitted[name]['sha256'] and r['bytes']==omitted[name]['bytes']
  else:assert q.stat().st_size==r['bytes'] and sha(q)==r['sha256'],name
 for name,pin in s.get('sources_sha256',{}).items():assert sha(HERE/name)==pin,name
f=json.loads((HERE/'autonomous_clock_independent/FINAL_SEAL.json').read_text())
assert not f['required_mathematical_corrections'] and not f['scientific_discrepancies']
print('per_element: original marks enter the finite conserving collision program.')
print('per_site: the numeric matter example is the complete four-site one-birth star.')
print('per_mode: finite clock propagation and microscopic energy bands; no photon claim.')
print('per_block: conserving battery blocks and positive programmed Hamiltonian, both counterphases.')
print('lattice_wide: fixed finite graph/horizon only; no locality or volume theorem.')
print('Selected source/seal closure verified; four explicit historical omissions. No audit verdict.')
