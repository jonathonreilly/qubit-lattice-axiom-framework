import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import collections,itertools,json,time,resource,signal,hashlib
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,26));signal.alarm(60)
t0=time.monotonic();c0=time.process_time();out=Path(__file__).resolve().parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929');assert not(rt/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
old=out.parent/'independent-fast-small-sector-check/check_words.py';ns={'__file__':str(old)}
exec(compile(old.read_text().split('t=time.process_time();')[0],str(old),'exec'),ns);signal.alarm(60)
steps,add,near,charge,state,step,op,physical=[ns[k] for k in ('steps','add','near','charge','state','step','op','physical')]
o=(0,0,0);ex=(1,0,0);d2={add(a,b) for a in steps for b in steps}-{o}
def plus(dst,src,sg=1):
 for st,v in src.items():dst[st]+=sg*v
 return dst
def info(st):
 q=dict(st[0]);holes={x for x,v in q.items() if sum(x)%2==0 and not v};B={x for x,v in q.items() if sum(x)%2 and v};h=max(holes);G=2*sum(not charge(q,b) for h0 in holes for b in near(h0));phi=sum(max(-5,min(5,h[0]-b[0])) for b in B)
 return holes,B,h,G,phi
def base(holes,B):
 B=sorted(B);q={h:0 for h in holes};minus=(len(B)-len(holes))//2;assert len(B)-len(holes)==2*minus
 for i,b in enumerate(B):q[b]=-1 if i<minus else 1
 e=collections.Counter();diff={x:v-(1 if sum(x)%2==0 else 0) for x,v in q.items()}
 assert sum(diff.values())==0
 for x,sg in diff.items():
  at=x
  for j in range(3):
   while at[j]:
    y=list(at);y[j]-=1 if at[j]>0 else -1;y=tuple(y);a,b=(at,y) if sum(at)%2==0 else (y,at);e[a,b]+=sg if a==at else -sg;at=y
 st=state(q,e);physical({st:1});return st
def H(st):
 holes,B,h,g,p=info(st);nearholes={add(x,d) for x in holes for d in d2}-holes;r=collections.Counter();v={st:1}
 for x in holes:plus(r,op(op(v,x,'in'),x,'out'))
 for x in nearholes:plus(r,op(op(v,x,'out'),x,'in'),-1)
 for x in holes:
  for a in {add(x,d) for d in d2}-holes:
   plus(r,op(op(v,x,'in'),a,'out'));plus(r,op(op(v,a,'out'),x,'in'),-1)
 return {st:x for st,x in r.items() if x}
def full(st):
 holes,B,h,g,p=info(st);centers=holes|{add(x,d) for x in holes for d in d2}|{(40,0,0),(42,0,0)}
 def F(v,kind):
  r=collections.Counter()
  for a in centers:plus(r,op(v,a,kind))
  return {s:x for s,x in r.items() if x}
 r=collections.Counter();v={st:1};plus(r,F(F(v,'in'),'out'));plus(r,F(F(v,'out'),'in'),-1)
 for a in centers:
  if all(add(a,d) not in holes for d in d2):plus(r,op(op(v,a,'out'),a,'in'))
 return {st:x for st,x in r.items() if x}
fixtures=[{o,(0,2,0)},{o,(0,2,0),(-2,0,0)},{o,(0,2,0),(0,0,2),(-2,0,0)}]
rows=[];gauss=0;marks=0;full_entries=0
for holes in fixtures:
 B={b for h in holes for b in near(h)}|{(17,0,0),(19,0,0)}
 if (len(B)-len(holes))%2:B.add((21,0,0))
 st=base(holes,B);hb=H(st);ff=full(st);assert hb==ff;full_entries+=len(hb);gauss+=physical(ff)
 hi,bs,h,g,ph=info(st);assert g==0;b=add(h,ex);c=add(b,ex);target=step(step(st,h,b,'in'),c,b,'out');assert target is not None
 hs1,B1,h1,g1,ph1=info(target);assert h1==c and sum(x[0]==c[0] for x in hs1)==1
 assert step(step(target,c,b,'in'),h,b,'out')==st
 reverse=H(target);assert reverse[st]==1;gauss+=physical(reverse)
 classes=collections.Counter();deltas=[]
 for other,coef in reverse.items():
  hh,bb,hhmax,gg,pp=info(other)
  if gg or other==st:continue
  assert pp-ph>=6
  if hh==hs1:classes['same_hole_set']+=1;assert pp-ph>=10
  elif c in hh:classes['selected_output_hole_retained']+=1;assert pp-ph>=12
  else:classes['selected_output_hole_replaced']+=1
  deltas.append(pp-ph)
 for bright in [s for s in reverse if info(s)[3]][:8]:
  hh,bb,hm,gg,pp=info(bright)
  for a in hh:
   for b0 in near(a):
    for sg in (-1,1):
     nxt=step(bright,a,b0,'birth',sg)
     if nxt is None:continue
     qn=dict(nxt[0]);newholes={x for x,v in qn.items() if sum(x)%2==0 and not v};newB={x for x,v in qn.items() if sum(x)%2 and v}
     assert len(newholes)==len(hh)-1 and len(newB)==len(bb)+1
     gauss+=physical({nxt:1});marks+=1
 rows.append({'m':len(holes),'k':len(B),'full_action_entries':len(ff),'reverse_entries':len(reverse),'other_dark_rows':len(deltas),'minimum_height_increment':min(deltas) if deltas else None,'reverse_classes':dict(classes)})
r={'scope':'independent actual rotor cancellation/reverse-row/cascade-grade controls; no sampled semigroup theorem','cases':rows,'full_action_coefficients':full_entries,'Gauss_words':gauss,'original_birth_grade_checks':marks,'reused_own_elementary_word_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(out/'RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r));assert r['rss_bytes']<120*1024**2
