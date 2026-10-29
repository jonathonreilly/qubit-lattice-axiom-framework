"""Execute linked author-source prefixes and genuine omission/order mutants."""
import hashlib,json,os,re,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path('.claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks');rows=[];resources=[]
THREADS=['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']
def sha(b):return hashlib.sha256(b).hexdigest()
def guard(where,pid=None):
 r=subprocess.run(['/usr/bin/memory_pressure','-Q'],capture_output=True,text=True,timeout=5);m=re.search(r'System-wide memory free percentage:\s*(\d+)%',r.stdout);assert r.returncode==0 and m
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if pid:
  ps=subprocess.run(['/bin/ps','-o','rss=','-p',str(pid)],capture_output=True,text=True,timeout=5)
  if ps.returncode==0 and ps.stdout.strip():rss=max(rss,int(ps.stdout.strip())*1024)
 d={'where':where,'rss':rss,'completed_child_maxrss':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,'free':int(m.group(1)),'load':list(os.getloadavg()),'nice':os.getpriority(os.PRIO_PROCESS,0),'threads':{k:os.environ.get(k) for k in THREADS}};resources.append(d)
 assert d['rss']<2e9 and d['completed_child_maxrss']<2e9 and d['free']>=50 and max(d['load'])<20 and d['nice']>=10 and set(d['threads'].values())=={'1'}
def one(text,old,new):
 assert text.count(old)==1,(old,text.count(old));return text.replace(old,new)
actual=(ROOT/'covariant_source_activity_actual.py').read_text();atoms=(ROOT/'covariant_source_activity_atoms.py').read_text()
assert sha(actual.encode())=='964917975efedcf2898bc1dd532bcf2849f74794b011156c4664425784dacb85'
assert sha(atoms.encode())=='943b97af7d8b08392631daf4d96ba322832e2aa43c5ea0eebb745efbd8b734ac'
prefix=actual[:actual.index('\nJomitvac=')]
independent='''
# Independent review assertion: direct normalized Haar moment, not phase(z).
review_den=mp.quad(lambda th:mp.sin(th)**2*mp.exp(t*mp.cos(th)),[0,mp.pi])
review_num=mp.quad(lambda th:mp.sin(th)**2*mp.cos(th)*mp.exp(t*mp.cos(th)),[0,mp.pi])
review_expected=u*(5+qmp)+t*frac-t*(review_num/review_den)*frac*(1-frac)+mp.mpf(2)/3
review_actual=mp.diff(lambda a:phase(a),0,2)
review_error=abs(review_actual-review_expected)/max(1,abs(review_expected))
print(json.dumps({'author_prefix_checks':checks,'review_expected_hessian':str(review_expected),'review_actual_hessian':str(review_actual),'review_error':str(review_error)}))
assert review_error<mp.mpf('1e-30'),'actual_density_zero_hessian'
'''
base=prefix+independent
cases=[('actual_baseline',base,None,'exact prefix through fixed-reference factorization plus independent Haar-moment Hessian'),
 ('actual_no_normalizer',one(base,'+mp.log(z0(t*radius(a)))',''),'actual_density_zero_hessian','delete field-dependent normalizer from actual phase'),
 ('actual_no_haar',one(base,'-logj(a)',''),'actual_density_zero_hessian','delete Haar Jacobian from actual phase'),
 ('actual_no_source_vacuum',one(base,'Jfixed=haar_axis*c0*mp.exp(-base-M)*Zg','Jfixed=haar_axis*c0*mp.exp(-base)*Zg'),'exact_fixed_reference_full_factors','delete source vacuum in Jfixed'),
 ('atoms_baseline',atoms,None,'exact full author checker'),
 ('atoms_wrong_sign',one(atoms,'R=-(K@P);R[inds,:]=0','R=(K@P);R[inds,:]=0'),'actual_parametrix_identity','change residual sign'),
 ('atoms_wrong_order',one(atoms,"ck('actual_inverse_order',np.linalg.norm(P@np.linalg.inv(ident-R)-G,np.inf)<1e-12)","ck('actual_inverse_order',np.linalg.norm(np.linalg.inv(ident-R)@P-G,np.inf)<1e-12)"),'actual_inverse_order','change computed inverse multiplication order')]
for name,code,expected,change in cases:
 guard(name+' preflight');path=ROOT/('review_covariant_source_activity_probe_'+name+'.py');path.write_text(code)
 before=sha(path.read_bytes());started=time.monotonic();proc=subprocess.Popen([sys.executable,'-B',str(path)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
 try:
  while True:
   try:out,err=proc.communicate(timeout=.5);break
   except subprocess.TimeoutExpired:
    assert time.monotonic()-started<60,name+' timeout';guard(name+' running',proc.pid)
 except BaseException:
  proc.kill();out,err=proc.communicate();(ROOT/('review_covariant_source_activity_probe_'+name+'.stdout.txt')).write_text(out);(ROOT/('review_covariant_source_activity_probe_'+name+'.stderr.txt')).write_text(err);raise
 elapsed=time.monotonic()-started;guard(name+' completed');assert elapsed<60
 op=ROOT/('review_covariant_source_activity_probe_'+name+'.stdout.txt');ep=ROOT/('review_covariant_source_activity_probe_'+name+'.stderr.txt');op.write_text(out);ep.write_text(err)
 after=sha(path.read_bytes());assert before==after
 good=(proc.returncode==0 and not err) if expected is None else (proc.returncode==1 and err.rstrip().endswith('AssertionError: '+expected) and 'Traceback' in err)
 row={'case':name,'change':change,'copy':str(path),'copy_sha256':before,'executed_sha256_unchanged':before==after,'stdout_sha256':sha(op.read_bytes()),'stderr_sha256':sha(ep.read_bytes()),'returncode':proc.returncode,'expected_assertion':expected,'matched_expected_outcome':good,'elapsed':elapsed};rows.append(row)
 if not good:
  (ROOT/'review_covariant_source_activity_probes_01.json').write_text(json.dumps({'cases':rows,'resources':resources},indent=2)+'\n')
  raise AssertionError('unexpected probe outcome '+name)
report={'stage':'post-exposure actual source substitutions; not a full actual-checker replay','author_actual_sha256':sha(actual.encode()),'author_atoms_sha256':sha(atoms.encode()),'prefix_sha256':sha(prefix.encode()),'prefix_lines':len(prefix.splitlines()),'independent_assertion_sha256':sha(independent.encode()),'cases':rows,'resources':resources}
(ROOT/'review_covariant_source_activity_probes_01.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'cases':len(rows),'all_expected':all(r['matched_expected_outcome'] for r in rows),'max_child_seconds':max(r['elapsed'] for r in rows)}))
