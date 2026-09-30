import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import ast,collections,itertools,json,math,resource,signal,time,hashlib
from pathlib import Path
from fractions import Fraction
out=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not(runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(10,11));signal.alarm(20)
t0=time.monotonic();c0=time.process_time()
sources={};steps=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b));near=lambda a:[add(a,d) for d in steps]
zero=(0,0,0);ex=(1,0,0);ey=(0,1,0);ez=(0,0,1)
d2={add(a,b) for a in steps for b in steps}-{zero}
raw=(out/'check.py').read_bytes();tree=ast.parse(raw)
names={'load_defs','hole','dist','occupied','V','delta_exact'}
nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
assert {n.name for n in nodes}==names
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(out/'check.py'),'exec'),globals())
load_defs(out.parent/'independent-fast-small-sector-check/check_words.py',['charge','state','step','physical'])
load_defs(out.parent/'finite-spin-fast-response-route/check_spin.py',['gate','flux'])
base=((),());c=(1,1,0);d=(1,0,1);extra=(2,0,1)
for aa,bb,kind,sg in [(c,ex,'out',0),(c,ey,'birth',1),(d,ez,'out',0),
 (d,extra,'birth',1),(zero,(0,-1,0),'out',0),(zero,(-1,0,0),'birth',1),
 (zero,(0,0,-1),'out',0)]:base=step(base,aa,bb,kind,sg)
rows=[];gauss=0
for S in (1,2,5):
 for v in sorted({1,S}):
  for remote in (0,S):
   st=flux(flux(base,(2,0,0),v),(30,0,0),remote);target=V(st)
   assert target is not None and all(abs(e)<=S for z in (st,target) for _,e in z[1])
   gauss+=physical({st:1,target:1})
   actual=delta_exact(target,S)-delta_exact(st,S)
   expected=Fraction(2*v*v,S*(S+1))
   assert actual==expected and actual>0
   h=hole(st);c1=hole(target)
   centers={h,c1}|{add(h,z) for z in d2}|{add(c1,z) for z in d2}
   assert delta_exact(target,S,centers)-delta_exact(st,S,centers)==actual
   rows.append({'S':S,'local_flux':v,'remote_flux':remote,'exact_nonzero_difference':str(actual)})
result={'scope':'exact nonzero local compensation commutator; no dynamical simulation',
 'rows':rows,'Gauss_words':gauss,'primary_definition_sha256':hashlib.sha256(raw).hexdigest(),
 'reused_sources':sources,'cpu_seconds':time.process_time()-c0,
 'wall_seconds':time.monotonic()-t0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['cpu_seconds']<10 and result['rss_bytes']<80*1024**2
(out/'FOLLOWUP_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result));print('TOTAL: PASS=1 FAIL=0')
