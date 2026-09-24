#!/opt/homebrew/opt/python@3.13/bin/python3.13
from pathlib import Path
import datetime,hashlib,json,subprocess
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
RAW=HERE.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pre=HERE/'PRE_SEAL.json'
assert sha(pre)=='3bf5577d8caf04c9f446f46dca570d43565ab4e58f775984ce479233ac9089a4'
pre_manifest=json.loads(pre.read_text())
for r in pre_manifest['files']:
 p=HERE/r['path'];assert p.stat().st_size==r['bytes'];assert sha(p)==r['sha256'],r['path']
receipt=json.loads((HERE/'COMPARISON_RECEIPT.json').read_text())
for p,h in receipt['all_author_seal_bindings_authenticated'].items():assert sha(BASE/p)==h,p
own=json.loads((HERE/'COMPARISON_OWN_H4_MOMENTS.json').read_text())
assert own['initial_H4_histogram']=={'-2':12,'-84':1}
assert own['selected_resolved']['h_variance']=='K**2*n**4 + 392*delta**2'
claims=json.loads((HERE/'COMPARISON_EXACT_CLAIMS_RESULTS.json').read_text())
assert claims['failures']==[]
assert claims['all_48_spin_paths_match_symbolically']
assert claims['saved_author_rotor_moments_compared']==252
run_data=[]
for script,log in [('comparison_full_h4_control.py','COMPARISON_FULL_H4.log'),
 ('comparison_authenticate_and_reproduce.py','COMPARISON_REPRODUCTION.log'),
 ('comparison_exact_claims.py','COMPARISON_EXACT_CLAIMS.log')]:
 run_data.append({'command':['/opt/homebrew/opt/python@3.13/bin/python3.13',str(HERE/script)],
  'cwd':str(HERE),'observed_exit_code':0,'receipt_basis':'successful exec/write_stdin tool completion observed',
  'script_sha256':sha(HERE/script),'full_log':log,'log_sha256':sha(HERE/log)})
record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'observed_HEAD':subprocess.check_output(['git','rev-parse','HEAD'],cwd=RAW,text=True).strip(),
 'PRE_seal_sha256':sha(pre),'all_20_PRE_bound_files_unchanged':True,
 'author_source_hashes_still_match':True,'comparison_control_runs':run_data,
 'failed_comparison_executions':[],'scientific_discrepancies':[],
 'deliberate_mutation':'Diagonal-only H4 replacement has variance zero instead of 392 and is rejected.',
 'disposition':'Scoped conditional calculation supported; no landing/audit verdict.',
 'excluded':['microscopic energy-moment transfer','autonomous reservoir or heat identification','all-time heating','native selection','empirical identification']}
(HERE/'COMPARISON_EXECUTION_RECEIPT.json').write_text(json.dumps(record,indent=2)+'\n')
files=[]
for p in sorted(HERE.rglob('*')):
 if p.is_file() and p.name not in ('FINAL_SEAL.json','FINAL_SEAL.sha256'):
  files.append({'path':str(p.relative_to(HERE)),'bytes':p.stat().st_size,'sha256':sha(p)})
seal={'stage':'FINAL source comparison, no audit verdict','sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'PRE_seal_sha256':sha(pre),'PRE_bound_bytes_unchanged':True,
 'author_seal_sha256':{'initial':sha(BASE/'high_flux_energy_author/AUTHOR_SEAL.json'),
  'extension':sha(BASE/'high_flux_energy_extension_author/AUTHOR_SEAL.json')},
 'scope':'The two pinned author notes, scientific implementations and transitive path builder; exact resolved H4 second moment reconstructed with own frozen PRE implementation.',
 'supported':'Conditional compensated-cube rotor and effective finite-spin claims specified in COMPARISON.md.',
 'excluded_claims':record['excluded'],'failures':[],'files':files}
fp=HERE/'FINAL_SEAL.json';fp.write_text(json.dumps(seal,indent=2)+'\n')
fs=sha(fp);(HERE/'FINAL_SEAL.sha256').write_text(fs+'  FINAL_SEAL.json\n')
print(json.dumps({'FINAL_SEAL_sha256':fs,'bound_files':len(files),'PRE_unchanged':True,
 'comparison_note_sha256':sha(HERE/'COMPARISON.md'),'no_scientific_discrepancy':True},indent=2))
