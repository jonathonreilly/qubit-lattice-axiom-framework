"""Portable science replay in disposable copy; frozen evidence unchanged."""
from pathlib import Path
import json,hashlib,datetime,math,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(HERE/'verify_rotor_fast_tail_publication.py')],check=True)
tmp=Path(tempfile.mkdtemp(prefix='rotor-fast-tail-portable-'));copy=tmp/'campaign12h_fourth'
shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
jobs=[('fast_band_tail_author','exact_tail_control.py','EXACT_TAIL_RESULTS.json'),('fast_band_tail_independent','exact_fiber_control.py','EXACT_FIBER_RESULTS_01.json'),('fast_band_tail_independent','post_certificate_compare.py','POST_CERTIFICATE_RESULTS_02.json')]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def compare(a,b,path=''):
 if isinstance(b,dict):
  assert set(a)==set(b),path
  for k in b:
   if not path and k=='created_utc':continue
   compare(a[k],b[k],path+'/'+k)
 elif isinstance(b,list):
  assert len(a)==len(b),path
  for i,(x,y) in enumerate(zip(a,b)):compare(x,y,path+'/'+str(i))
 elif isinstance(b,float):assert math.isfinite(a) and abs(a-b)<2e-12,(path,a,b)
 else:assert a==b,(path,a,b)
rows=[]
for i,(folder,script,result) in enumerate(jobs,1):
 wd=copy/folder;(wd/result).unlink();out=tmp/f'run_{i}.stdout';err=tmp/f'run_{i}.stderr';start=time.monotonic()
 with out.open('wb') as o,err.open('wb') as e:r=subprocess.run([sys.executable,script],cwd=wd,stdout=o,stderr=e)
 row={'script':folder+'/'+script,'source_sha256':sha(HERE/folder/script),'exit_code':r.returncode,'wall_seconds':time.monotonic()-start,'stdout':str(out),'stderr':str(err)};rows.append(row)
 assert r.returncode==0,row
 compare(json.loads((wd/result).read_text()),json.loads((HERE/folder/result).read_text()))
 saved=tmp/f'run_{i}.RESULT.json';shutil.copy2(wd/result,saved);row['result_path']=str(saved);row['result_sha256']=sha(saved)
 row['comparison']='All scientific JSON, exact discrete fields and floating tolerance2e-12; only creation time excluded. Original assertions unchanged.'
 shutil.copy2(HERE/folder/result,wd/result)
 print(json.dumps({'completed':i,'script':script,'passed':True}),flush=True)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'temporary_copy':str(copy),'runs':rows,'all_three_scientific_replays_passed':True,'limits':'Replays are consistency checks, not new independent evidence; historical failed attempts remain failed.'}
p=tmp/'PORTABLE_RUN_RECEIPT.json';p.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'receipt':str(p),'all_passed':True}))
