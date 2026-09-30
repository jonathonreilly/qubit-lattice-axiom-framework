import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,signal,resource,math
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
resource.setrlimit(resource.RLIMIT_CPU,(15,16));signal.alarm(60)
t0,c0=time.monotonic(),time.process_time();out=Path(__file__).resolve().parent;pack=out.parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not(rt/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
import numpy as np
ns={};src=pack/'native-scattering-route/check_matching.py';exec(compile(src.read_text().split('# All abstract graphs')[0],str(src),'exec'),ns)
sub,disp,matching_edges,degrees=[ns[k] for k in ('sub','disp','matching_edges','degrees')]
types=[('axis',i) for i in range(3)]+[('plane',i,j,sg) for i in range(3) for j in range(i+1,3) for sg in (-1,1)]
def identify(pair):
 a,b=sorted(pair);d=sub(b,a);ix=[i for i in range(3) if d[i]]
 if len(ix)==1 and abs(d[ix[0]])==2:return ix[0],tuple((x+y)//2 for x,y in zip(a,b))
 assert len(ix)==2 and all(abs(d[i])==1 for i in ix)
 i,j=ix
 if d[i]<0:a,b=b,a;d=sub(b,a)
 return types.index(('plane',i,j,d[j])),a
r=np.load(out/'RESIDUAL.npz');den=int(r['denominator']);mon=[tuple(x) for x in json.loads((out/'CORE_RESULTS.json').read_text())['monomial_order']]
vecs=[]
for name in ['E1','T12']:
 v=np.zeros(15,dtype=np.int64)
 if name=='E1':
  for p,c in [((0,0),1),((0,1),-1),((1,1),1)]:v[mon.index(p)]=c
 else:v[mon.index((2,2))]=1
 vecs.append((name,v))
results={};Gsave={}
for name,v in vecs:
 g={};qnorm=Fraction();pcount=qcount=lift_checks=0
 for SS,rr in zip(r['shapes'],r['numerator']):
  val=int(rr@v)
  if not val:continue
  S=tuple(map(tuple,SS.tolist()));pm=[(a,b) for a,b in matching_edges(S) if sub(a[1],a[0]) in disp and sub(b[1],b[0]) in disp]
  if not pm:
   D=sum((d-1)*(d-2)//2 for d in degrees(S));assert D>=1;qnorm+=Fraction(val*val,D);qcount+=1;continue
  pcount+=1;m=2*len(pm);keys=[]
  for a,b in pm:
   for removed,residual in [(a,b),(b,a)]:
    alpha,y=identify(residual);beta,x=identify(removed);key=(alpha,beta,sub(x,y));assert key not in g
    g[key]=Fraction(val,m);keys.append(key)
  assert len(set(keys))==m and sum(g[k] for k in keys)==val;lift_checks+=1
 l1=defaultdict(Fraction)
 for (alpha,beta,position),value in g.items():l1[alpha,beta]+=abs(value)
 coarse=sum(x*x for x in l1.values())
 # Physical normalized incoming adds factor1/2 to quadratic raw residual cost.
 qphysical=qnorm/(2*den**2);lphysical=coarse/(2*den**2)
 results[name]={'perfect_rows':pcount,'nonmatching_rows':qcount,'lift_coordinates':len(g),'exact_lift_checks':lift_checks,'exact_q_cost':str(qphysical),'exact_sum_channel_l1_squared':str(lphysical),'coarse_dual_cost_upper_expression':str(qphysical)+' + (3*sqrt(3)*pi/4)*('+str(lphysical)+')','coarse_dual_cost_float_display':float(qphysical)+3*math.sqrt(3)*math.pi/4*float(lphysical)}
 Gsave[name]={'keys':[[a,b,list(pos)] for a,b,pos in g],'numerators':[str(x.numerator) for x in g.values()],'denominators':[x.denominator for x in g.values()],'raw_common_denominator':den,'physical_quadratic_factor':'1/2'}
(out/'DUAL_LIFT.json').write_text(json.dumps(Gsave,separators=(',',':'))+'\n')
results['cpu_seconds']=time.process_time()-c0;results['wall_seconds']=time.monotonic()-t0;results['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert results['peak_rss_bytes']<120000000
(out/'DUAL_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
