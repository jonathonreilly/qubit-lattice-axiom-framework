"""Five science replays in a disposable copy; immutable evidence is retained."""
from pathlib import Path
import datetime,hashlib,json,math,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n in ['verify_general_microscopic_energy_publication.py','verify_fast_band_energy_publication.py']:
 subprocess.run([sys.executable,str(HERE/n)],check=True)
tmp=Path(tempfile.mkdtemp(prefix='fast-band-portable-'));copy=tmp/'campaign12h_fourth'
shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
A='fast_band_energy_author';I='fast_band_energy_independent'
jobs=[(A,'exact_fast_band_paths.py','EXACT_FAST_BAND_PATHS_RESULTS.json'),(A,'complete_spin_one_cube_control.py','COMPLETE_SPIN_ONE_CUBE_RESULTS.json'),(I,'cube_control.py','CONTROL_RESULTS.json'),(I,'count_control.py','COUNT_CONTROL_RESULTS.json'),(I,'post_compare.py','POST_CONTROL_RESULTS.json')]
def compare(actual,expected,path=''):
 if isinstance(expected,dict):
  assert set(actual)==set(expected),path
  for k in expected:
   if path=='' and k in ('created_utc','wall_seconds','elapsed_seconds'):continue
   compare(actual[k],expected[k],path+'/'+k)
 elif isinstance(expected,list):
  assert len(actual)==len(expected),path
  for i,(a,b) in enumerate(zip(actual,expected)):compare(a,b,path+'/'+str(i))
 elif isinstance(expected,(int,float)) and not isinstance(expected,bool):
  assert math.isfinite(actual) and abs(actual-expected)<5e-8,(path,actual,expected)
 else:assert actual==expected,(path,actual,expected)
rows=[]
for i,(folder,script,result) in enumerate(jobs,1):
 wd=copy/folder;out=tmp/f'run_{i}.stdout';err=tmp/f'run_{i}.stderr';start=time.monotonic()
 with out.open('wb') as stdout,err.open('wb') as stderr:r=subprocess.run([sys.executable,script],cwd=wd,stdout=stdout,stderr=stderr)
 row={'script':folder+'/'+script,'source_sha256':sha(HERE/folder/script),'exit_code':r.returncode,'wall_seconds':time.monotonic()-start,'stdout':str(out),'stderr':str(err)};rows.append(row)
 assert r.returncode==0,row
 actual=json.loads((wd/result).read_text());expected=json.loads((HERE/folder/result).read_text());compare(actual,expected)
 generated=tmp/f'run_{i}.RESULT.json';shutil.copy2(wd/result,generated)
 row['result_path']=str(generated);row['result_sha256']=sha(generated)
 row['comparison']='All scientific JSON fields; absolute floating tolerance5e-8; only top-level creation/runtime metadata excluded. Primary runner assertions unchanged.'
 # Later source-hash-bound controls must consume their original frozen inputs.
 shutil.copy2(HERE/folder/result,wd/result)
 print(json.dumps({'completed':i,'script':script,'passed':True}),flush=True)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'temporary_copy':str(copy),'runs':rows,'all_five_primary_scientific_replays_passed':True,'historical_author_pair_precision_failure_remains_false_in_evidence':True,'limits':'Historical provenance flags in replayed JSON describe the original derivation. Replays are not new independent evidence or new blind PREs.'}
(tmp/'PORTABLE_RUN_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receipt':str(tmp/'PORTABLE_RUN_RECEIPT.json'),'runs':len(rows),'all_primary_passed':True}))
