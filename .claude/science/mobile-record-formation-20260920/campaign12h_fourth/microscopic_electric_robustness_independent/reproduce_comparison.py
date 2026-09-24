#!/usr/bin/env python3
"""Replay frozen author and PRE controls only inside new comparison directories.
Root builders are executed only in separate child processes. The independent
comparison control reads their result data, never imports their implementation.
"""
from pathlib import Path
import hashlib,json,os,platform,shutil,subprocess,sys,time,datetime
HERE=Path(__file__).resolve().parent
PYTHON=Path(sys.executable).resolve()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_pre():
 assert sha(HERE/'PRE_SEAL.json')=='92f534204e822fbbc38f4cfbd8a5f6d1d33f09b727d7bead68fd22dfb4734faa'
 data=json.loads((HERE/'PRE_SEAL.json').read_text())
 for row in data['files']:
  p=HERE/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],row['path']
 return len(data['files'])
def copy(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst);assert sha(src)==sha(dst)
 return {'snapshot_path':src.relative_to(HERE).as_posix(),'runtime_path':dst.relative_to(HERE).as_posix(),'sha256':sha(src)}
def run(name,path,expected_code):
 stdout=HERE/(name+'.stdout');stderr=HERE/(name+'.stderr');start=time.monotonic()
 with stdout.open('wb') as out,stderr.open('wb') as err:
  r=subprocess.run([str(PYTHON),str(path)],cwd=HERE,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},stdout=out,stderr=err)
 row={'name':name,'script_relative_path':path.relative_to(HERE).as_posix(),'script_sha256':sha(path),'python':platform.python_version(),'exit_code':r.returncode,'expected_exit_code':expected_code,'wall_seconds':time.monotonic()-start,'stdout_path':stdout.name,'stdout_sha256':sha(stdout),'stderr_path':stderr.name,'stderr_sha256':sha(stderr)}
 assert r.returncode==expected_code,row
 return row
before=verify_pre()
manifest=json.loads((HERE/'COMPARISON_SOURCE_BINDINGS.json').read_text())
for row in manifest['sources']:assert sha(HERE/row['snapshot_path'])==row['sha256']
SNAP=HERE/'comparison_sources/campaign12h_fourth';RUNTIME=HERE/'comparison_runtime'
operations=[];executions=[]
operations.append(copy(HERE/'star_local_matrix_control.py',RUNTIME/'independent/star_local_matrix_control.py'))
executions.append(run('comparison_independent_replay',RUNTIME/'independent/star_local_matrix_control.py',0))
assert (RUNTIME/'independent/EXACT_STAR_MATRIX_RESULTS.json').read_bytes()==(HERE/'EXACT_STAR_MATRIX_RESULTS.json').read_bytes()
for case,filename,rc in [('author_success','exact_electric_star_energy.py',0),('author_preserved_failure','FAILED_exact_electric_star_energy.py',1)]:
 dest=RUNTIME/case
 operations.append(copy(SNAP/'microscopic_birth_energy_author/exact_star_energy.py',dest/'microscopic_birth_energy_author/exact_star_energy.py'))
 operations.append(copy(SNAP/'microscopic_electric_robustness_author'/filename,dest/'microscopic_electric_robustness_author'/filename))
 executions.append(run('comparison_'+case,dest/'microscopic_electric_robustness_author'/filename,rc))
 if rc==0:
  assert (dest/'microscopic_electric_robustness_author/EXACT_ELECTRIC_STAR_ENERGY_RESULTS.json').read_bytes()==(SNAP/'microscopic_electric_robustness_author/EXACT_ELECTRIC_STAR_ENERGY_RESULTS.json').read_bytes()
  assert (HERE/'comparison_author_success.stdout').read_bytes()==(SNAP/'microscopic_electric_robustness_author/EXACT_ELECTRIC_STAR_ENERGY.log').read_bytes()
  assert (HERE/'comparison_author_success.stderr').read_bytes()==b''
 else:
  assert b'AssertionError' in (HERE/'comparison_author_preserved_failure.stderr').read_bytes()
  assert (HERE/'comparison_author_preserved_failure.stdout').read_bytes()==(SNAP/'microscopic_electric_robustness_author/FAILED_EXACT_ELECTRIC_STAR_ENERGY.log').read_bytes()
executions.append(run('comparison_independent_check',HERE/'compare_frozen_sources.py',0))
after=verify_pre()
receipt={'stage':'post-PRE source comparison only','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_seal_sha256':sha(HERE/'PRE_SEAL.json'),'PRE_files_authenticated_before':before,'PRE_files_authenticated_after':after,'PRE_bytes_unchanged':True,'source_bindings_sha256':sha(HERE/'COMPARISON_SOURCE_BINDINGS.json'),'runtime_policy':'All runtime copies and generated outputs are beneath this packet. Root scientific builders execute in separate child processes and are never imported by the independent calculation. Relative names plus exact hashes permit relocation.','copies':operations,'executions':executions,'reproduction_results':{'own_PRE_result_byte_identical':True,'author_result_byte_identical':True,'author_stdout_byte_identical':True,'preserved_author_failure_reproduced':True},'unresolved_execution_failures':[]}
(HERE/'COMPARISON_EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'PRE_files_unchanged':after,'executions':[{k:r[k] for k in ('name','exit_code','expected_exit_code')} for r in executions],'independent_comparison':json.loads((HERE/'COMPARISON_RESULTS.json').read_text())['summary']},indent=2))
