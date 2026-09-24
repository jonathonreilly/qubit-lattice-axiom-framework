"""Verify the selected cube energy unit without rerunning or rewriting seals."""
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent
manifest=json.loads((HERE/'PUBLICATION_UNIT_HIGH_FLUX_ENERGY.json').read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert manifest['base_commit']=='4f5f210ecc33a8eba817fcfb153c9f43f81b96a6'
assert manifest['base_pr']==8870
assert manifest['claim_status']=='provisional review proposal; no audit verdict'
assert manifest['independent_check']=='completed blind PRE and source comparison'
for group in ('artifacts','sources'):
 seen=set()
 for row in manifest[group]:
  assert row['path'] not in seen;seen.add(row['path']);p=HERE/row['path']
  assert p.stat().st_size==row['bytes'],row['path']
  assert sha(p)==row['sha256'],row['path']
for name in ('high_flux_energy_author','high_flux_energy_extension_author'):
 seal=json.loads((HERE/name/'AUTHOR_SEAL.json').read_text())
 for key in ('science_sources_and_artifacts_sha256','artifacts_sha256','sources_sha256'):
  for path,h in seal.get(key,{}).items():assert sha(HERE/path)==h,path
ind=HERE/'high_flux_energy_independent_v2'
assert sha(ind/'PRE_SEAL.json')=='3bf5577d8caf04c9f446f46dca570d43565ab4e58f775984ce479233ac9089a4'
assert sha(ind/'FINAL_SEAL.json')=='6c9baf295340a4f93129a7967aa49651b14cadf29470bc22da1ab8658ffd332f'
excluded={row['path']:row for row in manifest['historical_procedure_snapshots_omitted']}
assert set(excluded)=={'sources/planning_agents.md','sources/repository_agent_pointer.md','sources/science_workflow.md'}
for name in ('PRE_SEAL.json','FINAL_SEAL.json'):
 for row in json.loads((ind/name).read_text())['files']:
  path=row['path']
  if path in excluded:
   assert row==excluded[path],path
   continue
  p=HERE/path.removeprefix('comparison_sources/') if path.startswith('comparison_sources/') else ind/path
  assert p.stat().st_size==row['bytes'],path
  assert sha(p)==row['sha256'],path
# The selected 47-word image is authenticated twice and compared independently.
check=json.loads((ind/'COMPARISON_H4_CERTIFICATE_RESULT.json').read_text())
assert check['every_input_and_H4_image_word_matches']
assert check['matched_image_words']==47 and check['actual_H4_variance']=='392'
assert check['symbolic_selected_covariance']=='0'
assert check['symbolic_selected_h_variance']=='K**2*n**4 + 392*delta**2'
print('per_element: exact primitive ladder paths and all 47 selected H4 image coefficients were independently reconstructed.')
print('per_site: the eight specified cube charges and their physical Gauss constraints were checked in the bound controls.')
print('per_mode: the specified face-flux family and marked output were checked; the full spectral-mode family was not enumerated.')
print('per_block: relevant number and hole grades retain the complete effective H4 action, including off-input-support amplitudes.')
print('lattice_wide: the complete finite cube mark sum was checked; arbitrary volume and all-time energy behavior were not executed.')
print('Source and seal closure verified. Provisional conditional review proposal; no audit verdict or no-go packet PASS.')
