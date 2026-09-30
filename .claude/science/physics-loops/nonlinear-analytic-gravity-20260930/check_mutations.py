"""Managed, serial source-mutation controls; never edits the primary."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys,time,resource
ROOT=Path.cwd()
PACK=ROOT/'.claude/science/physics-loops/nonlinear-analytic-gravity-20260930'
OUT=PACK/'mutations';OUT.mkdir(exist_ok=True)
SOURCE=ROOT/'scripts/nonlinear_canonical_gravity_analytic_approximation_2026_09_30.py'
base=SOURCE.read_text();base_sha=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
assert base_sha=='89f9815e9d66cbae91aa38dd6609eacb9f81145dc76ac8d521d18bbc24ea23bf'
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
DEADLINE=json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
# Each alteration corrupts the computed law, variation, normalization or operator.
# The acceptance assertions and their expected values remain untouched.
cases=[
 ('quartic_inverse','for r in range(1,5):','for r in range(1,3):',['--family','exact','--case','axial'],'exact_axial'),
 ('common_scalar_gradient','+3*sq*sum(iv[i][j]*phi.D(i)*phi.D(j)', '+2*sq*sum(iv[i][j]*phi.D(i)*phi.D(j)',['--family','exact','--case','axial'],'exact_axial'),
 ('structure_shift','sum(6*iv[i][j]*(N*M.D(j)-M*N.D(j))','sum(5*iv[i][j]*(N*M.D(j)-M*N.D(j))',['--family','exact','--case','axial'],'exact_axial'),
 ('circular_modes','def wrap(k): return tuple((v+J)%n-J for v in k)','def wrap(k): return tuple(k)',['--family','exact','--case','alias'],'exact_alias'),
 ('metric_r_adjoint','grad = grad_no_r-r_adj','grad = grad_no_r',['--family','variation'],'full_3d_variation'),
 ('scalar_metric_stress','base[1]-=metric_derivative','base[1]-=0*metric_derivative',['--family','scalar'],'coupled_scalar'),
 ('conformal_H_normalization','H2=.1**2*c/12','H2=.1**2*c/6',['--family','scalar'],'coupled_scalar'),
 ('centered_derivative','D[i,(i+1)%n]+=1/(2*eps);D[i,(i-1)%n]-=1/(2*eps)','D[i,(i+1)%n]+=1/(4*eps);D[i,(i-1)%n]-=1/(4*eps)',['--family','scalar'],'coupled_scalar'),
]
if len(sys.argv)>1:
 wanted=set(sys.argv[1:]);cases=[c for c in cases if c[0] in wanted]
 assert len(cases)==len(wanted),wanted
env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
records=[];start=time.monotonic();ru0=resource.getrusage(resource.RUSAGE_CHILDREN)
for name,before,after,args,intended in cases:
 assert time.time()<DEADLINE,'original campaign deadline reached'
 assert not (RUNTIME/'STOP_REQUESTED.json').exists(),'campaign stop requested'
 assert base.count(before)==1,(name,base.count(before))
 path=OUT/(name+'.py');path.write_text(base.replace(before,after))
 t=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN)
 try:
  run=subprocess.run([sys.executable,str(path),*args],capture_output=True,text=True,env=env,timeout=60,cwd=ROOT)
  status='completed';code=run.returncode;stdout=run.stdout;stderr=run.stderr
 except subprocess.TimeoutExpired as exc:
  status='timeout';code=None;stdout=exc.stdout or '';stderr=exc.stderr or ''
  if isinstance(stdout,bytes):stdout=stdout.decode(errors='replace')
  if isinstance(stderr,bytes):stderr=stderr.decode(errors='replace')
 r1=resource.getrusage(resource.RUSAGE_CHILDREN)
 (OUT/(name+'.stdout')).write_text(stdout);(OUT/(name+'.stderr')).write_text(stderr)
 detected=(status=='completed' and code==1 and 'FAIL '+intended+': AssertionError' in stdout)
 record={'name':name,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'before':before,'after':after,'args':args,'intended_family':intended,'status':status,'exit_code':code,'wall_seconds':time.monotonic()-t,'cpu_seconds':r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime,'cumulative_child_peak_rss_bytes':r1.ru_maxrss,'detected_by_assertion':detected}
 records.append(record)
 (OUT/'RESULTS.json').write_text(json.dumps({'base_sha256':base_sha,'records':records,'scope':'Actual scratch-source changes; primary and its expected assertions unchanged. No timeout counts as detection.'},indent=2)+'\n')
 print(name,status,code,'detected',detected,'wall',round(record['wall_seconds'],3),flush=True)
 if not detected:break
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==base_sha,'primary source changed'
ruf=resource.getrusage(resource.RUSAGE_CHILDREN)
summary={'base_sha256':base_sha,'records':records,'wall_seconds':time.monotonic()-start,'cpu_seconds':ruf.ru_utime+ruf.ru_stime-ru0.ru_utime-ru0.ru_stime,'child_peak_rss_bytes':ruf.ru_maxrss,'all_detected':len(records)==len(cases) and all(r['detected_by_assertion'] for r in records),'scope':'Author mutation controls, not independent review. Mathematical claims rely on written proof and separate formal review.'}
(OUT/'RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='records'},indent=2),flush=True)
raise SystemExit(0 if summary['all_detected'] else 1)
