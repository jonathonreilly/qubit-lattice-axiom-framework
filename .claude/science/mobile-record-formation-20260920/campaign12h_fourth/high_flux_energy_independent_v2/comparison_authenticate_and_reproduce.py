#!/opt/homebrew/opt/python@3.13/bin/python3.13
import datetime,hashlib,json,os,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
PY='/opt/homebrew/opt/python@3.13/bin/python3.13'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pre=HERE/'PRE_SEAL.json'
assert sha(pre)=='3bf5577d8caf04c9f446f46dca570d43565ab4e58f775984ce479233ac9089a4'
for r in json.loads(pre.read_text())['files']:assert sha(HERE/r['path'])==r['sha256'],r['path']
expected={'high_flux_energy_author/AUTHOR_SEAL.json':'92272978616462937a76398eb2a1a1af03c08de92c59abc73f5de3ed84496d8f',
'high_flux_energy_extension_author/AUTHOR_SEAL.json':'2163902fc70b3077356c0097e61746f617ede94a5283ccb961270d48d4b091ea',
'high_flux_energy_author/HIGH_FLUX_ACTUAL_BIRTH_ENERGY_SPREAD.md':'a355623459a0bea115b0874ab03a1f691f55a71fa67785b4f04f68513a3ad472',
'high_flux_energy_extension_author/ROTOR_DRIFT_AND_FINITE_SPIN_HIGH_FLUX.md':'de24a51431ba27f10d178286da2c95cc69081b06a9058d225d4840e3225388c0'}
for p,h in expected.items():assert sha(BASE/p)==h,p
bound={}
for sealpath in list(expected)[:2]:
 seal=json.loads((BASE/sealpath).read_text())
 for label in ('science_sources_and_artifacts_sha256','artifacts_sha256','sources_sha256'):
  for p,h in seal.get(label,{}).items():
   assert sha(BASE/p)==h,p
   bound[p]=h
 bound[sealpath]=sha(BASE/sealpath)
# Snapshot only the comparison units and their actually used transitive builder.
# Other older seal-listed contexts are hash authenticated, not claimed reviewed.
snapshot=HERE/'comparison_sources';snapshot.mkdir(exist_ok=True)
read_full=[]
for p,h in bound.items():
 if p.startswith(('high_flux_energy_author/','high_flux_energy_extension_author/')) or p=='local_compensation_independent/model.py':
  dest=snapshot/p;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes((BASE/p).read_bytes())
  if p.endswith(('.md','.py')):read_full.append(p)
runs=[]
for directory,script,result in [
('high_flux_energy_author','cube_high_flux_birth.py','CUBE_HIGH_FLUX_RESULTS.json'),
('high_flux_energy_author','all_mark_high_flux_check.py','ALL_MARK_HIGH_FLUX_RESULTS.json'),
('high_flux_energy_author','cross_check_existing_independent_paths.py','CROSS_CHECK_RESULTS.json'),
('high_flux_energy_extension_author','full_rotor_energy_control.py','FULL_ROTOR_ENERGY_RESULTS.json'),
('high_flux_energy_extension_author','symbolic_spin_energy_balance.py','SYMBOLIC_SPIN_ENERGY_BALANCE_RESULTS.json'),
('high_flux_energy_extension_author','finite_spin_path_comparison.py','FINITE_SPIN_PATH_COMPARISON_RESULTS.json')]:
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 out=HERE/('COMPARISON_REPRODUCED_'+result)
 err=HERE/('COMPARISON_'+script+'.stderr')
 env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
 with out.open('wb') as so,err.open('wb') as se:
  r=subprocess.run([PY,str(BASE/directory/script)],cwd=HERE,env=env,stdout=so,stderr=se)
 assert r.returncode==0,(script,r.returncode)
 original=BASE/directory/result
 assert json.loads(out.read_text())==json.loads(original.read_text()),script
 runs.append({'script':directory+'/'+script,'script_sha256':sha(BASE/directory/script),'command':[PY,str(BASE/directory/script)],
   'started_utc':start,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
   'exit_code':r.returncode,'output':out.name,'stderr':err.name,'matches_sealed_JSON_semantically':True,
   'matches_sealed_bytes':out.read_bytes()==original.read_bytes()})
# No protected source or PRE byte may change through imports/reproduction.
for r in json.loads(pre.read_text())['files']:assert sha(HERE/r['path'])==r['sha256'],r['path']
for p,h in bound.items():assert sha(BASE/p)==h,p
report={'compared_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'PRE_seal_sha256':sha(pre),'all_PRE_bound_bytes_unchanged':True,'all_author_seal_bindings_authenticated':bound,
'full_scientific_note_and_script_reads':read_full,
'authority_boundary':'Conditional source comparison and calculation only, no landing or audit verdict',
'other_seal_bound_historical_context_not_mathematically_reviewed':[p for p in bound if p not in read_full and not p.startswith(('high_flux_energy_author/','high_flux_energy_extension_author/'))],
'runs':runs,'external_actions':[],'git_mutations':[]}
(HERE/'COMPARISON_RECEIPT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'PRE_unchanged':True,'authenticated_author_binding_count':len(bound),
  'scientific_scripts_reproduced':len(runs),'all_semantic_outputs_match':True,'bytewise_match_count':sum(r['matches_sealed_bytes'] for r in runs)},indent=2))
