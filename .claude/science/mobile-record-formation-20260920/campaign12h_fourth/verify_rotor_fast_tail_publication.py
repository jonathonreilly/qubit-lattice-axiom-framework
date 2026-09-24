"""Publication source closure only; no science or audit verdict."""
from pathlib import Path
import json,hashlib
HERE=Path(__file__).resolve().parent;REPO=HERE.parents[3]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((HERE/'PUBLICATION_UNIT_ROTOR_FAST_TAIL.json').read_text())
assert m['base_pr']==8953 and m['base_commit']=='733bfa16316ca7f98d413d27cf4678a0accbbb31'
for key in ('artifacts','sources'):
 seen=set()
 for row in m[key]:
  assert row['path'] not in seen;seen.add(row['path']);p=HERE/row['path']
  assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],row['path']
omitted={r['path']:r for r in m['explicit_omissions']}
for row in m['seals']:
 p=HERE/row['path'];assert sha(p)==row['sha256'];s=json.loads(p.read_text())
 for r in s['artifacts']:
  q=p.parent/r['path'];name=str(q.relative_to(HERE))
  if name in omitted:assert not q.exists() and r['sha256']==omitted[name]['sha256']
  else:assert sha(q)==r['sha256'] and q.stat().st_size==r['bytes'],name
 for r in s.get('sources',[]):assert sha(REPO/r['path'])==r['sha256'],r['path']
for r in json.loads((HERE/'fast_band_tail_independent/POST_SOURCE_BINDINGS.json').read_text())['bindings']:
 p=HERE/'fast_band_tail_independent'/r['snapshot'];assert sha(p)==r['sha256']
f=json.loads((HERE/'fast_band_tail_independent/FINAL_SEAL.json').read_text())
assert not f['scientific_source_corrections_required'] and f['dependency_historical_numeric_comparison_still_failed']
print('per_element: unchanged original physical formation marks.')
print('per_site: complete fixed cube physical charge sector.')
print('per_mode: almost-everywhere damping; exceptional flat fiber retained.')
print('per_block: exact Laurent and Gauss-cycle certificates.')
print('lattice_wide: normalizable rotor states; sequential time limit only.')
print('Public source/seal closure verified; no audit status assigned.')
