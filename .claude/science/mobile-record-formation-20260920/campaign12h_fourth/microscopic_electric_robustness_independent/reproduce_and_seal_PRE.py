from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys,time
HERE=Path(__file__).resolve().parent
PY='/opt/homebrew/opt/python@3.13/bin/python3.13'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sources=json.loads((HERE/'SOURCE_BINDINGS.json').read_text())
for row in sources['sources']:
 if 'path' in row:assert sha(Path(row['path']))==row['sha256'],row['path']
 assert sha(HERE/row['snapshot'])==row['sha256'],row['snapshot']
runs=[]
for script,log in [('star_local_matrix_control.py','exact_star_matrix.log'),('star_finite_time_control.py','finite_time_control.log')]:
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();t0=time.time()
 env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
 with (HERE/log).open('wb') as out:
  r=subprocess.run([PY,str(HERE/script)],cwd=HERE,env=env,stdout=out,stderr=subprocess.STDOUT)
 runs.append({'command':[PY,str(HERE/script)],'cwd':str(HERE),'start_utc':start,
  'finish_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':time.time()-t0,
  'exit_code':r.returncode,'script_sha256':sha(HERE/script),'full_log':log,'log_sha256':sha(HERE/log)})
 if r.returncode:raise RuntimeError(runs[-1])
for row in sources['sources']:
 if 'path' in row:assert sha(Path(row['path']))==row['sha256'],row['path']
receipt={'stage':'PRE; withheld author packet not read','python':sys.version,'runs':runs,
 'sources_revalidated':True,'failed_executions':[],'failed_physics_assertions':[],
 'sensitivity_controls':['dephasing the common leaf superposition changes injected mean',
  'lambda>0 initial state has a nonzero H-eigenstate residual and energy loss term',
  'P-compressed output Hamiltonian misses positive epsilon^-6 variance'],
 'numeric_role':'Full Lindblad consistency and asymptotic corroboration; analytic limit proof is separate',
 'git_mutations':[],'external_actions':[],'writes_outside_owned_directory':[]}
(HERE/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
files=[]
for p in sorted(HERE.rglob('*')):
 if p.is_file() and p.name not in ('PRE_SEAL.json','PRE_SEAL.sha256'):
  files.append({'path':str(p.relative_to(HERE)),'bytes':p.stat().st_size,'sha256':sha(p)})
seal={'stage':'PRE independent reconstruction','sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'author_comparison_performed':False,'source_bindings_sha256':sha(HERE/'SOURCE_BINDINGS.json'),
 'scope':'Supplied electric family on the complete physical three-leaf star; common partially W=1 initial state; original actual formation instruments',
 'open':'Author source comparison and any autonomous realization; no audit or landing verdict',
 'files':files}
p=HERE/'PRE_SEAL.json';p.write_text(json.dumps(seal,indent=2)+'\n')
h=sha(p);(HERE/'PRE_SEAL.sha256').write_text(h+'  PRE_SEAL.json\n')
print(json.dumps({'PRE_seal_sha256':h,'bound_files':len(files),'all_runs_completed':True,
 'sources_revalidated':True,'note_sha256':sha(HERE/'PRE_RECONSTRUCTION.md')},indent=2))
