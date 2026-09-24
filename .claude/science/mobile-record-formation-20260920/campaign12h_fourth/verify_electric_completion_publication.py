"""Verify corrected electric-family publication source closure."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
manifest=json.loads((HERE/'PUBLICATION_UNIT_ELECTRIC_COMPLETION.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert manifest['base_pr']==8891
assert manifest['base_commit']=='432edb3bfdb12f8471955b4de344826cee45ed4f'
assert manifest['claim_status']=='provisional review proposal; no audit verdict'
for group in ('artifacts','sources'):
 seen=set()
 for row in manifest[group]:
  assert row['path'] not in seen;seen.add(row['path']);p=HERE/row['path']
  assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
author=HERE/'field_energy_completion_author';ind=HERE/'field_energy_completion_independent'
assert sha(author/'AUTHOR_SEAL.json')=='96a39d1872cfa54b9699475d0d800dc3cf05cf3208a3404bb599048964a4c7dc'
aseal=json.loads((author/'AUTHOR_SEAL.json').read_text())
for group in ('artifacts_sha256','sources_sha256'):
 for path,h in aseal[group].items():assert sha(HERE/path)==h,path
assert sha(ind/'PRE_SEAL.json')=='3c06c43ca8e216532709f929f6241d6b5c7f1c9d05a1152ad578a297fc5b6aa9'
assert sha(ind/'FINAL_SEAL.json')=='32dc1da84668012da48f37b450770a32bdc648f23b713ea10384f384d667d1da'
for name,key in [('PRE_SEAL.json','artifacts'),('FINAL_SEAL.json','files')]:
 for path,r in json.loads((ind/name).read_text())[key].items():
  assert sha(ind/path)==(r if isinstance(r,str) else r['sha256']),path
corr=ind/'CORRECTION_REVIEW_SEAL.json'
assert sha(corr)=='7603e1cd727ce5bffec7eedb4323f2ad619df58a2a23a1eb5db5033a1ce8eae4'
cs=json.loads(corr.read_text())
for group in ('source','review'):
 r=cs[group];p=ind/r['path'];assert p.stat().st_size==r['bytes'] and sha(p)==r['sha256']
for name,h in cs['prior_seals_sha256'].items():assert sha(ind/name)==h
checks=json.loads((ind/'COMPARISON_EXACT_MATCHES.json').read_text())
assert checks['six_cycle_Gauss_compatible_full_occupancy_words']==0
assert checks['H4_certificate_words_matched']==47
assert checks['own_total_lambda_cases']==54
print('per_element: the finite-spin local diagonal and primitive paths were checked; full H4 covariance was independently reconstructed.')
print('per_site: specified mixed-graph and cube charge words obey Gauss; six-cycle full occupation is explicitly rejected by parity.')
print('per_mode: the specified terminal Wilson coherence is distinguished; a complete mode or photon spectrum was not executed.')
print('per_block: the P-supported common target and existing terminal sectors are covered, with finite-window conditioning kept explicit.')
print('lattice_wide: a fixed finite-graph theorem is supplied; growing-volume dynamics, mixing and physical parameter selection were not executed.')
print('Corrected source and seal closure verified. No audit verdict or no-go packet PASS.')
