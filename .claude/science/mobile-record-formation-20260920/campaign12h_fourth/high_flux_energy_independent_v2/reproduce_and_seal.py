from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time
OUT=Path(__file__).resolve().parent
PYTHON='/opt/homebrew/opt/python@3.13/bin/python3.13'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
runs=[]
for script,log in [('independent_exact_control.py','exact_control.log'),('direct_matrix_action_control.py','direct_action_control.log')]:
    begin=datetime.datetime.now(datetime.timezone.utc).isoformat();started=time.time()
    with (OUT/log).open('wb') as out:
        r=subprocess.run([PYTHON,str(OUT/script)],cwd=OUT,stdout=out,stderr=subprocess.STDOUT)
    row={'command':[PYTHON,str(OUT/script)],'cwd':str(OUT),'started_utc':begin,
         'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'elapsed_seconds':time.time()-started,'exit_code':r.returncode,'script_sha256':digest(OUT/script),
         'full_log':log,'log_sha256':digest(OUT/log)}
    runs.append(row)
    if r.returncode:raise RuntimeError(row)
bindings=json.loads((OUT/'SOURCE_BINDINGS.json').read_text())
for row in bindings['sources']:
    if 'path' in row:assert digest(Path(row['path']))==row['sha256'],row
    assert digest(OUT/row['snapshot'])==row['sha256'],row
receipt={'stage':'PRE before any comparison with withheld author or prior independent attempt',
         'python':sys.version,'runs':runs,'current_sources_match_bound_snapshots':True,
         'science_status':'conditional exact reconstruction; no audit or retained verdict',
         'failure_history':['INITIAL_EXECUTION_FAILURE.log: first tool-mediated file creation did not produce script; execution reported missing file.'],
         'external_actions':[],'git_mutations':[]}
(OUT/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
files=[]
for p in sorted(OUT.rglob('*')):
    if p.is_file() and p.name not in ('PRE_SEAL.json','PRE_SEAL.sha256'):
        files.append({'path':str(p.relative_to(OUT)),'bytes':p.stat().st_size,'sha256':digest(p)})
seal={'stage':'PRE','sealed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'source_comparison_performed':False,'head':bindings['head'],'files':files}
sp=OUT/'PRE_SEAL.json';sp.write_text(json.dumps(seal,indent=2)+'\n')
sha=digest(sp);(OUT/'PRE_SEAL.sha256').write_text(sha+'  PRE_SEAL.json\n')
print(json.dumps({'PRE_seal_sha256':sha,'bound_files':len(files),'all_runs_exit_zero':True,'sources_revalidated':True},indent=2))
