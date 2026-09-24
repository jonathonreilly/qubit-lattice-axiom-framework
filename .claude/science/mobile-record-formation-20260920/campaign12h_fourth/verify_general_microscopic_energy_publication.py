"""Authenticate the public projection; this is not a science or audit verdict."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
repo=HERE.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((HERE/'PUBLICATION_UNIT_GENERAL_MICROSCOPIC_ENERGY.json').read_text())
assert m['base_pr']==8936 and m['base_commit']=='69462972e8ef9585bdd8d85969e31c7b0b3638c3'
for key in ('artifacts','sources'):
 seen=set()
 for r in m[key]:
  assert r['path'] not in seen;seen.add(r['path']);p=HERE/r['path']
  assert p.stat().st_size==r['bytes'] and sha(p)==r['sha256'],r['path']
omitted={r['path']:r for r in m['explicit_omissions']}
assert len(omitted)==5 and all('/instructions/' in x for x in omitted)
for seal in m['seals']:
 p=HERE/seal['path'];assert sha(p)==seal['sha256'];s=json.loads(p.read_text())
 for r in s['artifacts']:
  q=p.parent/r['path'];name=str(q.relative_to(HERE))
  if name in omitted:assert not q.exists() and r['sha256']==omitted[name]['sha256'] and r['bytes']==omitted[name]['bytes']
  else:assert q.stat().st_size==r['bytes'] and sha(q)==r['sha256'],name
 for r in s.get('sources',[]):assert sha(repo/r['path'])==r['sha256'],r['path']
f=json.loads((HERE/'general_microscopic_birth_energy_independent/FINAL_COMPARISON_SEAL.json').read_text())
assert not f['corrections_required_to_released_claims']
print('per_element: original resolved/coherent marks and whole-P local leakage identity.')
print('per_site: physical charge/link words, blocked marks and distinct graph capacities.')
print('per_mode: full microscopic band moments, not a bounded slow observable.')
print('per_block: complete721-state model and309-column initial-power operator.')
print('lattice_wide: fixed finite graph only; no volume or physical selection theorem.')
print('Selected source/seal closure verified; five historical instruction omissions.')
