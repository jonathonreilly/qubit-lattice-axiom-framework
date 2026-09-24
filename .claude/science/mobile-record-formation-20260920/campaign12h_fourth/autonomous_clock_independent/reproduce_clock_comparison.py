#!/usr/bin/env python3
"""Reproduce comparisons; author execution is separate consistency evidence.
All runtime copies, temporary model imports and logs remain inside this packet.
"""
from pathlib import Path
import datetime,difflib,hashlib,json,os,platform,shutil,subprocess,sys,time
import numpy,scipy,sympy,mpmath
HERE=Path(__file__).resolve().parent;SNAP=HERE/'comparison_sources';RUNTIME=HERE/'comparison_runtime/author'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def precheck():
 assert sha(HERE/'PRE_SEAL.json')=='d015c9245087ce39c102c61d859171c58ccd5b4a2ea4d25ea2b9bc37a61493ad'
 pre=json.loads((HERE/'PRE_SEAL.json').read_text())
 for row in pre['files']:
  p=HERE/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],row['path']
 return len(pre['files'])
before=precheck();bindings=json.loads((HERE/'COMPARISON_SOURCE_BINDINGS.json').read_text())
for row in bindings['sources']:assert sha(HERE/row['snapshot_path'])==row['sha256']
runs=[];copies=[]
def run(name,script):
 out=HERE/(name+'.stdout');err=HERE/(name+'.stderr');start=time.monotonic()
 tmp=HERE/'comparison_runtime/tmp';tmp.mkdir(parents=True,exist_ok=True)
 with out.open('wb') as stdout,err.open('wb') as stderr:
  code=subprocess.run([sys.executable,str(script)],cwd=HERE,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','TMPDIR':str(tmp)},stdout=stdout,stderr=stderr).returncode
 record={'name':name,'script':str(script.relative_to(HERE)),'script_sha256':sha(script),'exit_code':code,'wall_seconds':time.monotonic()-start,'stdout':out.name,'stdout_sha256':sha(out),'stderr':err.name,'stderr_sha256':sha(err)}
 runs.append(record);assert code==0,record;assert not err.read_bytes(),record
for name in ('traveling_packet_identity_control','traveling_program_and_star_control'):run(name,HERE/(name+'.py'))
for alias in ('autonomous_clock_author/clock_control.py','autonomous_clock_author/original_star_clock_control.py','microscopic_birth_energy_author/exact_star_energy.py'):
 src=SNAP/alias;dest=RUNTIME/alias;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
 assert sha(src)==sha(dest);copies.append({'snapshot':str(src.relative_to(HERE)),'runtime':str(dest.relative_to(HERE)),'sha256':sha(src)})
for name,script,result,original_log in [('author_clock_replay','clock_control.py','CLOCK_CONTROL_RESULTS.json','CLOCK_CONTROL.stdout'),('author_original_star_replay','original_star_clock_control.py','ORIGINAL_STAR_CLOCK_RESULTS.json','ORIGINAL_STAR_CLOCK.stdout')]:
 run(name,RUNTIME/'autonomous_clock_author'/script)
 assert (RUNTIME/'autonomous_clock_author'/result).read_bytes()==(SNAP/'autonomous_clock_author'/result).read_bytes(),result
 assert (HERE/(name+'.stdout')).read_bytes()==(SNAP/'autonomous_clock_author'/original_log).read_bytes(),original_log
# Authenticate the historical reporting correction without rerunning an
# obsolete helper or silently treating a floated zero as an exact error bound.
author=SNAP/'autonomous_clock_author'
old=(author/'initial_underflow_reporting/clock_control.py').read_text();new=(author/'clock_control.py').read_text()
(HERE/'author_underflow_reporting_fix.diff').write_text(''.join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),fromfile='frozen_initial_underflow_source',tofile='frozen_author_source')))
def changes(a,b,path=''):
 if isinstance(a,dict):
  assert set(a)==set(b)
  return [r for key in a for r in changes(a[key],b[key],path+'/'+key)]
 if isinstance(a,list):
  assert len(a)==len(b)
  return [r for i,(x,y) in enumerate(zip(a,b)) for r in changes(x,y,path+'/'+str(i))]
 return [] if a==b else [{'path':path,'old':a,'new':b}]
report={}
for name in ('CLOCK_CONTROL_RESULTS.json','ORIGINAL_STAR_CLOCK_RESULTS.json'):
 dif=changes(json.loads((author/'initial_underflow_reporting'/name).read_text()),json.loads((author/name).read_text()))
 for r in dif:
  assert ('proved_boundary_trace_bound' in r['path'] or '/error_terms/finite_boundary' in r['path']) and r['old']==0 and r['new']>0
 report[name]=dif
(HERE/'REPORTING_CORRECTION_CHECK.json').write_text(json.dumps({'scope':'Only displayed finite-boundary tail fields changed; all other recorded scientific outputs are byte-value equal after JSON parsing.','changes':report},indent=2)+'\n')
after=precheck()
receipt={'stage':'post-PRE source comparison','completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PRE_seal_sha256':sha(HERE/'PRE_SEAL.json'),'PRE_files_authenticated_before':before,'PRE_files_authenticated_after':after,'PRE_bytes_unchanged':True,'comparison_source_bindings_sha256':sha(HERE/'COMPARISON_SOURCE_BINDINGS.json'),'python':platform.python_version(),'libraries':{'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__,'mpmath':mpmath.__version__},'runs':runs,'author_runtime_copies':copies,'author_replay_result_and_stdout_byte_identical':True,'independence':'First two controls are independently written new calculations. Last two runs are frozen author consistency replay only. No author builder is imported by independent controls.','temporary_path_policy':'TMPDIR and every source/runtime/output path remain under this packet; operational source paths are relative aliases resolved by hashes.','unresolved_execution_failures':[]}
(HERE/'COMPARISON_EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'PRE_files_unchanged':after,'bound_comparison_sources':len(bindings['sources']),'executions':[{k:r[k] for k in ('name','exit_code')} for r in runs],'author_replay_byte_identical':True,'independent_star_max_difference':json.loads((HERE/'TRAVELING_PROGRAM_AND_STAR_RESULTS.json').read_text())['original_star_comparison']['max_author_field_difference']},indent=2))
