"""Repeat scientific controls in a disposable copy; retain all frozen evidence."""
from pathlib import Path
import datetime,hashlib,json,math,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
subprocess.run([sys.executable,str(HERE/'verify_general_microscopic_energy_publication.py')],check=True)
tmp=Path(tempfile.mkdtemp(prefix='general-microscopic-portable-'));copy=tmp/'campaign12h_fourth'
shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
A='general_microscopic_birth_energy_author';I='general_microscopic_birth_energy_independent'
jobs=[(A,'local_leakage_control.py','LOCAL_LEAKAGE_RESULTS.json',None),(A,'complete_two_center_control.py','COMPLETE_TWO_CENTER_RESULTS.json',None),(I,'path_control.py','PATH_RESULTS_01.json','PATH_RESULTS_PORTABLE.json'),(I,'matrix_control_run01.py','MATRIX_RESULTS_01.json','MATRIX_RESULTS_PORTABLE.json'),(I,'ring_higher_order.py','RING_HIGHER_RESULTS_01.json','RING_HIGHER_RESULTS_PORTABLE.json'),(I,'frozen_cube_control.py','FROZEN_CUBE_RESULTS_01.json','FROZEN_CUBE_RESULTS_PORTABLE.json'),(I,'cube_subleading_control.py','CUBE_SUBLEADING_RESULTS_01.json','CUBE_SUBLEADING_RESULTS_PORTABLE.json'),(I,'post_path_compare.py','POST_PATH_COMPARISON_RESULTS.json',None),(I,'post_complete_k24.py','POST_COMPLETE_K24_RESULTS_01.json',None),(I,'post_scope_witness.py','POST_SCOPE_WITNESS.json',None)]
def compare(actual,expected,path=''):
 if isinstance(expected,dict):
  assert set(actual)==set(expected),path
  for k in expected:
   if path=='' and k=='created_utc':continue
   compare(actual[k],expected[k],path+'/'+k)
 elif isinstance(expected,list):
  assert len(actual)==len(expected),path
  for i,(a,b) in enumerate(zip(actual,expected)):compare(a,b,path+'/'+str(i))
 elif isinstance(expected,(int,float)) and not isinstance(expected,bool):
  assert math.isfinite(actual) and math.isclose(actual,expected,rel_tol=2e-8,abs_tol=2e-10),(path,actual,expected)
 else:assert actual==expected,(path,actual,expected)
rows=[]
for i,(folder,script,result,newresult) in enumerate(jobs,1):
 wd=copy/folder;out=tmp/f'run_{i}.stdout';err=tmp/f'run_{i}.stderr'
 actualpath=wd/(newresult or result)
 if actualpath.exists():actualpath.unlink()
 cmd=[sys.executable,script]+(['--attempt','PORTABLE'] if newresult else [])
 start=time.monotonic()
 with out.open('wb') as stdout,err.open('wb') as stderr:r=subprocess.run(cmd,cwd=wd,stdout=stdout,stderr=stderr)
 row={'script':folder+'/'+script,'source_sha256':sha(HERE/folder/script),'exit_code':r.returncode,'wall_seconds':time.monotonic()-start,'stdout':str(out),'stderr':str(err)};rows.append(row)
 assert r.returncode==0,row
 actual=json.loads(actualpath.read_text());expected=json.loads((HERE/folder/result).read_text());compare(actual,expected)
 row['comparison']='All scientific JSON fields compared; only top-level creation time excluded. Numeric roundoff: rel2e-8, abs2e-10; strings, booleans, keys and sizes exact.'
 row['result_sha256']=sha(actualpath)
 if script=='matrix_control_run01.py':shutil.copy2(actualpath,wd/result)
 print(json.dumps({'completed':i,'script':script,'passed':True}),flush=True)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'temporary_copy':str(copy),'runs':rows,'all_ten_scientific_replays_passed':True,'limits':'Replays test consistency, not new independence; procedural sealing wrappers are not rerun with omitted instruction snapshots.'}
(tmp/'PORTABLE_RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receipt':str(tmp/'PORTABLE_RUN_RECEIPT.json'),'runs':len(rows),'all_passed':True}))
