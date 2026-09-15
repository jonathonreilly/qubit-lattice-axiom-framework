from pathlib import Path
import json,hashlib,subprocess,math
r=Path('/private/tmp/review-drain-20260915');repo=r/'review-slot-one';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rec=json.load(open(r/'8103-unit-v1-timeout-preexecution.json'));report=json.load(open(r/'review-8103-timeout-preexecution.json'));primary=rec['notes'][0]['primary_runner'];ep=r/('8103-execution-'+Path(primary).stem+'.json');ex=json.load(open(ep));res=ex['result'];assert res['status']=='ok' and res['exit_code']==0 and res['stderr']=='' and res['elapsed_sec']<90;assert ex['preexecution_record_sha256']==sha(r/'8103-unit-v1-timeout-preexecution.json');cache=Path(ex['cache_path']);assert sha(cache)==ex['cache_sha256'];cp=cache.relative_to(repo).as_posix();tree=subprocess.check_output(['git','-C',str(repo),'write-tree'],text=True).strip()
for x in rec['source']['paths']:
 if x['path']!=cp:assert sha(repo/x['path'])==x['sha256']
 x['sha256']=sha(repo/x['path'])
for cat in rec['inputs'].values():
 for x in cat:assert sha(repo/x['path'])==x['sha256']
assert not subprocess.check_output(['git','-C',str(repo),'diff','--name-only'],text=True).strip()
old=json.load(open(r/'check8103/original-8103/.claude/science/physics-loops/gauss-reduced-weak-coupling-spectrum-20260913/CANONICAL_EXECUTION.json'))['stdout'];new=res['stdout'];assert 'TOTAL: PASS=600 FAIL=0' in new
parse=lambda text:{line.split(' ',1)[0]:json.loads(line.split(' ',1)[1]) for line in text.splitlines() if line.startswith(('GEOMETRY ','SPECTRAL '))}
a,b=parse(old),parse(new);assert a['GEOMETRY']==b['GEOMETRY'];diffs=[]
def compare(a,b,p=''):
 if isinstance(a,dict):
  assert a.keys()==b.keys()
  for k in a:compare(a[k],b[k],p+'/'+k)
 elif isinstance(a,list):
  assert len(a)==len(b)
  for i,(x,y) in enumerate(zip(a,b)):compare(x,y,p+'/'+str(i))
 elif isinstance(a,float):
  assert math.isfinite(a) and math.isfinite(b)
  if a!=b:diffs.append(dict(path=p,original=a,current=b,absolute_difference=abs(a-b)))
 else:assert a==b
compare(a,b)
for data in [a['SPECTRAL'],b['SPECTRAL']]:
 for ss in [1.,2.,3.]:
  rows=[x for x in data['fixed_boundary'] if x['s']==ss];errors=[abs(x['charged']-x['charged_target']) for x in rows];assert errors[2]<errors[1]<errors[0] and errors[-1]<.008
 full=data['full_space'];assert full[-1]['error']<.005 and full[-1]['error']<full[0]['error'];d=data['doubled_flux_copies'][-1];assert all(abs(x-2)<=.002+.002*2 for x in d[:2]) and d[1]-d[0]<1e-7
comparison=dict(floating_differences=diffs,max_difference=max((x['absolute_difference'] for x in diffs),default=0),unchanged_original_criteria='Both original and current printed fixed-boundary convergence, .008 accuracy, .005 full-space accuracy and doubled-cluster .002 allclose/1e-7 splitting satisfy original source criteria; all600 assertions executed. No tolerance/source change.',nonfloat_and_geometry_exact=True)
co=r/'8103-timeout-output-comparison.json';assert not co.exists();co.write_text(json.dumps(comparison,indent=2)+'\n');print(json.dumps(comparison,indent=2))
# Further final report emission follows after cold inspection of listed changes.
