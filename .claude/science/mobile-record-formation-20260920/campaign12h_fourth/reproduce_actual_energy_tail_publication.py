"""Repeat the local control without resealing or modifying frozen evidence."""
from pathlib import Path
import datetime,hashlib,json,math,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
subprocess.run([sys.executable,str(HERE/'verify_actual_energy_tail_publication.py')],check=True)
tmp=Path(tempfile.mkdtemp(prefix='actual-energy-tail-portable-'));copy=tmp/'independent';source=HERE/'fast_band_tail_rate_independent';shutil.copytree(source,copy,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
out=tmp/'CONTROL.stdout';err=tmp/'CONTROL.stderr';start=time.monotonic()
with out.open('wb') as o,err.open('wb') as e:r=subprocess.run([sys.executable,'local_rate_control.py'],cwd=copy,stdout=o,stderr=e)
assert r.returncode==0,r.returncode
actual=json.loads((copy/'LOCAL_RATE_RESULTS.json').read_text());expected=json.loads((source/'LOCAL_RATE_RESULTS.json').read_text())
def compare(a,b,path=''):
 if isinstance(b,dict):
  assert set(a)==set(b),path
  for k in b:compare(a[k],b[k],path+'/'+k)
 elif isinstance(b,list):
  assert len(a)==len(b),path
  for i,(x,y) in enumerate(zip(a,b)):compare(x,y,path+'/'+str(i))
 elif isinstance(b,float):assert math.isfinite(a) and math.isclose(a,b,rel_tol=1e-10,abs_tol=2e-11),(path,a,b)
 else:assert a==b,(path,a,b)
compare(actual,expected)
# Repeat the physical Gauss constraints and complete supplied flat comparison.
A=(0,3,5,6);B=(1,2,4,7);edges=[(a,b) for a in A for b in B if a^b in (1,2,4)]
for row in actual['actual_first_marks']:
 for word in row['physical_R']:
  div=[0]*8
  for (a,b),e in zip(edges,word['E']):div[a]+=e;div[b]-=e
  assert div==[q-int(i in A) for i,q in enumerate(word['q'])]
prior=json.loads((source/'sources/fast_band_tail_author/EXACT_TAIL_RESULTS.json').read_text());index={tuple(q):i for i,q in enumerate(actual['charge_order'])};flat={}
for row in prior['bright_dark_Laurent_entries']:
 key=(tuple(prior['bright_words'][row['bright_row']]),tuple(prior['dark_words'][row['dark_column']]));flat[key]=flat.get(key,0)+row['coefficient']
count=0
for q in prior['bright_words']:
 for p in prior['dark_words']:
  key=(tuple(q),tuple(p));assert actual['G_zero'][index[key[0]]][index[key[1]]]==flat.get(key,0);count+=1
assert count==1728
saved=tmp/'CONTROL.RESULT.json';shutil.copy2(copy/'LOCAL_RATE_RESULTS.json',saved)
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':sha(source/'local_rate_control.py'),'exit_code':r.returncode,'wall_seconds':time.monotonic()-start,'stdout':str(out),'stderr':str(err),'result_path':str(saved),'result_sha256':sha(saved),'all_scientific_JSON_compared':True,'comparison':'Discrete fields exact; floating rel1e-10/abs2e-11. No field excluded. Original assertions unchanged.','flat_entries_checked':count,'physical_Gauss_checks':True,'limits':'Numerical samples illustrate the local structure, not the analytic decay exponent. Replay is not new independent evidence.'}
p=tmp/'PORTABLE_RUN_RECEIPT.json';p.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'passed':True,'receipt':str(p)}))
