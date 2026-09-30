import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import collections,itertools,json,math,time,resource,signal,hashlib
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(30,31));signal.alarm(60)
out=Path(__file__).resolve().parent;t0=time.monotonic();c0=time.process_time()
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not(rt/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
# Explicit reuse of root's earlier independent charge/field word geometry only.
old=out.parent/'independent-fast-small-sector-check/check_words.py';ns={'__file__':str(old)}
exec(compile(old.read_text().split('t=time.process_time();')[0],str(old),'exec'),ns)
signal.alarm(60)
steps,add,near,charge,state,step,physical=[ns[k] for k in ('steps','add','near','charge','state','step','physical')]
zero=(0,0,0);ex=(1,0,0);ey=(0,1,0);ez=(0,0,1)
d2={add(a,b) for a in steps for b in steps}-{zero}
def weight(e,sg,S):
 if S is None:return 1.
 if abs(e)>S or abs(e+sg)>S:return 0.
 return math.sqrt(1-e*(e+sg)/(S*(S+1)))
def elementary(st,a,b,kind,S,sg=0):
 nxt=step(st,a,b,kind,sg)
 if nxt is None:return None,0.
 q,e=map(dict,st);inc=-charge(q,a) if kind=='out' else charge(q,b) if kind=='in' else sg
 return nxt,weight(e.get((a,b),0),inc,S)
def op(v,centers,kind,S):
 res=collections.defaultdict(float)
 for st,amp in v.items():
  for a in centers:
   for b in near(a):
    nxt,w=elementary(st,a,b,kind,S)
    if nxt is not None and w:res[nxt]+=amp*w
 return {st:x for st,x in res.items() if abs(x)>1e-13}
def plus(v,w,c=1):
 for st,x in w.items():v[st]+=c*x
 return v
def gate(q,a):return all(charge(q,add(a,d)) for d in d2)
def diagonal(st,S):
 if S is None:return 0.
 q,e=map(dict,st);result=0.
 for (a,b),v in e.items():
  if charge(q,a) and not charge(q,b) and gate(q,a):result+=1-weight(v,-charge(q,a),S)**2
 return result
def full(st,S):
 q,e=map(dict,st);h=next(x for x,v in q.items() if sum(x)%2==0 and v==0)
 centers={h}|{add(h,d) for d in d2}|{a for a,b in e}|{(40,0,0),(42,0,0)}
 v={st:1.};r=collections.defaultdict(float)
 plus(r,op(op(v,centers,'in',S),centers,'out',S));plus(r,op(op(v,centers,'out',S),centers,'in',S),-1)
 for a in centers:
  if gate(q,a):plus(r,op(op(v,[a],'out',S),[a],'in',S))
 r[st]+=diagonal(st,S)
 return {st:x for st,x in r.items() if abs(x)>1e-11}
def local(st,S):
 q=dict(st[0]);h=next(x for x,v in q.items() if sum(x)%2==0 and v==0);v={st:1.};r=collections.defaultdict(float)
 plus(r,op(op(v,[h],'in',S),[h],'out',S))
 for a in [add(h,d) for d in d2]:
  plus(r,op(op(v,[a],'out',S),[a],'in',S),-1)
  plus(r,op(op(v,[h],'in',S),[a],'out',S))
  plus(r,op(op(v,[a],'out',S),[h],'in',S),-1)
 r[st]+=diagonal(st,S)
 return {st:x for st,x in r.items() if abs(x)>1e-11}
def flux(st,c,v):
 q,e=map(dict,st)
 path=[c,add(c,ex),add(add(c,ex),ey),add(c,ey),c]
 for x,y in zip(path,path[1:]):
  a,b=(x,y) if sum(x)%2==0 else (y,x)
  e[a,b]=e.get((a,b),0)+(v if x==a else -v)
 return state(q,e)
single=step(((),()),zero,ex,'out')
c=(1,1,0);d=(1,0,1);extra=(2,0,1);dense=((),())
for aa,bb,kind,sg in [(c,ex,'out',0),(c,ey,'birth',1),(d,ez,'out',0),(d,extra,'birth',1),(zero,(0,-1,0),'out',0),(zero,(-1,0,0),'birth',1),(zero,(0,0,-1),'out',0)]:dense=step(dense,aa,bb,kind,sg)
rows=[];gauss=0;maxdiff=0.;nonzero_delta=0
for S in (1,2,5):
 for k,base in [(1,single),(7,dense)]:
  for f in sorted({0,1,S}):
   st=flux(base,(20,0,0),f);qnorm=1+sum(abs(v) for _,v in st[1]);assert all(abs(v)<=S for _,v in st[1]);gauss+=physical({st:1})
   hs=full(st,S);hl=local(st,S);err=max(abs(hs.get(x,0)-hl.get(x,0)) for x in set(hs)|set(hl));assert err<1e-10;maxdiff=max(maxdiff,err)
   gauss+=physical(hs)
   hr=full(st,None);diff=math.sqrt(sum(abs(hs.get(x,0)-hr.get(x,0))**2 for x in set(hs)|set(hr)))
   assert diff<=10000*qnorm*qnorm/(S*(S+1))
   ds=diagonal(st,S);assert -1e-12<=ds<=2*qnorm*qnorm/(S*(S+1));nonzero_delta+=ds>0
   hole=next(x for x,v in st[0] if sum(x)%2==0 and v==0);loss=0.;jdiff=0.;resolved={};coherent={}
   for b in near(hole):
    for sg in (-1,1):
     nxt,w=elementary(st,hole,b,'birth',S,sg)
     if nxt is None:continue
     loss+=w*w;jdiff+=(w-1)**2;resolved[(b,sg,nxt)]=w;coherent[(b,nxt)]=w;gauss+=physical({nxt:1})
   assert abs(sum(x*x for x in resolved.values())-sum(x*x for x in coherent.values()))<1e-12
   assert math.sqrt(jdiff)<=8*qnorm*qnorm/(S*(S+1))
   rows.append({'S':S,'k':k,'remote_flux':f,'actual_full_outputs':len(hs),'rotor_outputs':len(hr),'Delta_S':ds,'G_S':loss,'Q':qnorm,'H_difference_norm':diff})
# Exact rational boundary tests: the amplitude inequality reduces to (1-x)^2<=1-x.
from fractions import Fraction as F
link_checks=0
for S in range(1,13):
 C=S*(S+1)
 for e in range(-S-3,S+4):
  for sg in (-1,1):
   x=F(e*(e+sg),C)
   if abs(e)<=S and abs(e+sg)<=S:
    assert 0<=x<=1 and (1-x)**2<=1-x
   else:assert x>=1
   assert x<=F(2*(1+abs(e))**2,C)
   link_checks+=1
result={'scope':'actual sparse spin/full-compensation and original-mark finite controls, not all-time theorem proof','rows':rows,'Gauss_words':gauss,'max_full_vs_local_error':maxdiff,'nonzero_retained_Delta_cases':nonzero_delta,'exact_integer_spin_boundary_inequalities':link_checks,'own_reused_geometry_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
assert result['cpu_seconds']<30 and result['rss_bytes']<150*1024**2
