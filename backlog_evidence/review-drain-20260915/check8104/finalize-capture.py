from pathlib import Path
import json,hashlib,subprocess,math
r=Path('/private/tmp/review-drain-20260915');repo=r/'author-slot-one';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rec=json.load(open(r/'8104-unit-v1-preexecution.json'));report=json.load(open(r/'review-8104-preexecution.json'));primary=rec['notes'][0]['primary_runner'];ep=r/('8104-execution-'+Path(primary).stem+'.json');ex=json.load(open(ep));res=ex['result'];assert res['status']=='ok' and res['exit_code']==0 and res['stderr']=='' and res['elapsed_sec']<90;assert ex['preexecution_record_sha256']==sha(r/'8104-unit-v1-preexecution.json');cache=Path(ex['cache_path']);assert sha(cache)==ex['cache_sha256'];cp=cache.relative_to(repo).as_posix();tree=subprocess.check_output(['git','-C',str(repo),'write-tree'],text=True).strip()
for x in rec['source']['paths']:
 if x['path']!=cp:assert sha(repo/x['path'])==x['sha256']
 x['sha256']=sha(repo/x['path'])
for cat in rec['inputs'].values():
 for x in cat:assert sha(repo/x['path'])==x['sha256']
assert not subprocess.check_output(['git','-C',str(repo),'diff','--name-only'],text=True).strip()
old=json.load(open(r/'check8104/original-8104/.claude/science/physics-loops/flat-holonomy-spectral-floor-20260913/CANONICAL_EXECUTION.json'))['stdout'];new=res['stdout'];assert 'TOTAL: PASS=640 FAIL=0' in new
parse=lambda text:{line.split(' ',1)[0]:json.loads(line.split(' ',1)[1]) for line in text.splitlines() if line.startswith(('EXACT_TWIST ','RING '))}
a,b=parse(old),parse(new);assert a['EXACT_TWIST']==b['EXACT_TWIST'];diffs=[]
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
for data in [a['RING'],b['RING']]:
 for row in data:assert row['levels'][0]>=-2*math.sqrt(2)-1e-10
 row=data[-1];assert abs(row['levels'][0]+2*math.sqrt(2))<.005 and row['levels'][3]-row['levels'][0]<.026 and row['loop_real']<-.98 and abs(row['correction_over_g']-2**(-5/4))<.004 and abs(row['gap_over_g']-2**(-1/4))<.001
comparison=dict(floating_differences=diffs,max_difference=max((x['absolute_difference'] for x in diffs),default=0),unchanged_original_criteria='Both original and current ring outputs satisfy original positive-electric lower bound, .005 minimum accuracy, .026 level accumulation, -.98 loop concentration and .004/.001 formal coefficient challenges. Exact rational twist intervals unchanged. All640 assertions executed; no tolerance/source change.',nonfloat_and_exact_certificate_equal=True)
co=r/'8104-output-comparison.json';assert not co.exists();co.write_text(json.dumps(comparison,indent=2)+'\n');print(json.dumps(comparison,indent=2))
# Further final report emission follows after cold inspection of listed changes.
