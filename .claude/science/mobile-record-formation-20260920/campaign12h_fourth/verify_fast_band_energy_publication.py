"""Selected public source/seal authentication, not a science or audit verdict."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;repo=HERE.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((HERE/'PUBLICATION_UNIT_FAST_BAND_ENERGY.json').read_text())
assert m['base_pr']==8946 and m['base_commit']=='bb4462598a2a9e9d9d2fddb229ea5152cc8b4d28'
for key in ('artifacts','sources'):
 seen=set()
 for r in m[key]:
  assert r['path'] not in seen;seen.add(r['path']);p=HERE/r['path']
  assert p.stat().st_size==r['bytes'] and sha(p)==r['sha256'],r['path']
omitted={r['path']:r for r in m['explicit_omissions']}
for seal in m['seals']:
 p=HERE/seal['path'];assert sha(p)==seal['sha256'];s=json.loads(p.read_text())
 for r in s['artifacts']:
  q=p.parent/r['path'];name=str(q.relative_to(HERE))
  if name in omitted:assert not q.exists() and r['sha256']==omitted[name]['sha256']
  else:assert q.stat().st_size==r['bytes'] and sha(q)==r['sha256'],name
 for name,pin in s.get('sources_sha256',{}).items():assert sha(HERE/name)==pin,name
f=json.loads((HERE/'fast_band_energy_independent/FINAL_SEAL.json').read_text())
assert not f['scientific_source_corrections_required']
assert f['historical_author_pair_precision_comparison_failed']
assert f['primary_science_controls_passed_at_unchanged_thresholds']
print('per_element: both original formation instruments and actual second mark.')
print('per_site: complete cube charge/Gauss sectors; six-ring capacity not transferred.')
print('per_mode: rare microscopic high band and positive finite-tau energy.')
print('per_block: uniform spectral similarity and integrated jump intensity.')
print('lattice_wide: fixed cube, compact fast time; no laboratory-time or bath theorem.')
print('Source/seal closure verified, including retained historical precision failure.')
