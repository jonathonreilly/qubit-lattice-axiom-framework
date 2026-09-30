import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import collections,itertools,json,resource,signal,time,hashlib
from pathlib import Path
from fractions import Fraction as Q
resource.setrlimit(resource.RLIMIT_CPU,(20,21));signal.alarm(60)
t0,c0=time.monotonic(),time.process_time();out=Path(__file__).resolve().parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929');assert not(rt/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
# Reuse only root's earlier independent elementary-word code, declared input.
old=out.parent/'independent-fast-small-sector-check/check_words.py';ns={'__file__':str(old)}
exec(compile(old.read_text().split('t=time.process_time();')[0],str(old),'exec'),ns)
steps,add,near,charge,state,step,op,physical=[ns[k] for k in ('steps','add','near','charge','state','step','op','physical')]
origin=(0,0,0);ex=(1,0,0);c=(2,0,0)
D2={add(x,y) for x in steps for y in steps if add(x,y)!=origin}
def base(S):
 S=sorted(S);q={origin:0};e=collections.Counter()
 for i,b in enumerate(S):
  sg=-1 if i<(len(S)-1)//2 else 1;q[b]=sg;at=b
  for axis in range(3):
   while at[axis]:
    nxt=list(at);nxt[axis]-=1 if at[axis]>0 else -1;nxt=tuple(nxt)
    a,z=(at,nxt) if sum(at)%2==0 else (nxt,at)
    e[a,z]+=sg if at==a else -sg;at=nxt
 st=state(q,e);physical({st:1});return st
def plus(dst,src,sg=1):
 for k,v in src.items():dst[k]+=sg*v
def H(st):
 q=dict(st[0]);h=next(x for x,v in q.items() if sum(x)%2==0 and not v);v={st:1};r=collections.Counter()
 plus(r,op(op(v,h,'in'),h,'out'))
 for d in D2:
  a=add(h,d)
  plus(r,op(op(v,a,'out'),a,'in'),-1)
  plus(r,op(op(v,h,'in'),a,'out'))
  plus(r,op(op(v,a,'out'),h,'in'),-1)
 return {s:v for s,v in r.items() if v}
def info(st):
 q=dict(st[0]);h=next(x for x,v in q.items() if sum(x)%2==0 and not v);S={x for x,v in q.items() if sum(x)%2 and v}
 G=2*sum(not charge(q,b) for b in near(h));ph=sum(max(-5,min(5,h[0]-b[0])) for b in S);return h,S,G,ph
masks=[set(near(origin))|{(11,0,0)},set(near(origin))|set(near(c))|{(11,0,0),(13,0,0)}, {x for x in itertools.product(range(-3,4),repeat=3) if sum(abs(v) for v in x) in (1,3)}|{(11,0,0)}]
rows=[]
for mask in masks:
 st=base(mask);target=step(step(st,origin,ex,'in'),c,ex,'out');hr=H(target);assert hr[st]==1
 physical(hr);h,S,g,ph=info(st);assert g==0
 diffs=[];same=0;holes=0
 for r,coef in hr.items():
  h1,S1,g1,ph1=info(r)
  if r==st or g1:continue
  assert ph1-ph>=6
  if h1==c:assert ph1-ph>=10;same+=1
  else:assert S1==S;holes+=1
  diffs.append(ph1-ph)
 rows.append({'k':len(mask),'reverse_words':len(hr),'other_dark_rows':len(diffs),'same_hole_dark_rows':same,'other_hole_dark_rows':holes,'minimum_height_increase':min(diffs) if diffs else None})
# Independent full vacancy-fiber operator on L8, derived from Dicke bijection.
L=8;wrap=lambda x:tuple(v%L for v in x)
nb=lambda x:[wrap(add(x,d)) for d in steps]
canon=lambda ah,bv:(tuple(sorted(ah)),tuple(sorted(bv)))
def F(v,adj=False,center=None):
 r=collections.Counter()
 for (ah,bv),amp in v.items():
  if not adj:
   for b in bv:
    for a in nb(b):
     if a not in ah and (center is None or a==center):r[canon(set(ah)|{a},set(bv)-{b})]+=amp
  else:
   for a in ah:
    if center is not None and a!=center:continue
    for b in nb(a):
     if b not in bv:r[canon(set(ah)-{a},set(bv)|{b})]+=amp
 return {s:v for s,v in r.items() if v}
psi={};b0=(1,0,0)
for h in itertools.product(range(L),repeat=3):
 if sum(h)%2==0 and (h[1]+h[2])%8==4:
  assert h[0]%2==0
  psi[canon([h],[b0])]=(-1)**(h[0]//2+h[2])
assert len(psi)==32 and all(b0 not in nb(ah[0]) for ah,bv in psi)
assert not F(psi,True)
Ct=collections.Counter()
for st,amp in psi.items():
 h=st[0][0]
 for a in nb(b0):
  if a==h or h in {z for b in nb(a) for z in nb(b) if z!=a}:continue
  plus(Ct,F(F({st:amp},center=a),True,center=a))
Ct={s:v for s,v in Ct.items() if v};FF=F(F(psi),True);assert Ct==FF
# Piecewise periodic height; exact fractions and a different small grid.
periodic=0
for L in (28,32,44,52,80):
 sigma=Q(10,L-10)
 def chi(x):
  y=(x+5)%L-5
  return Q(y) if y<=5 else Q(5)-sigma*(y-5)
 for k in range(7,L//4+1,2):
  assert sigma*(k-6)<=Q(5,2)
  assert Q(7,2)*(20*k//7+1)>10*k
  for d in range(1,5):
   assert sum(chi(s+d)-chi(s) for s in (-1,1,0,0,0,0))==6*d
   for x in range(L):assert chi(x+d)-chi(x)>=-sigma*d;periodic+=1
  assert 10-2*sigma*(k-6)>=5
result={'literal_rotor_reverse_rows':rows,'Gauss_states_checked':sum(x['reverse_words'] for x in rows)+3,'periodic_L8_hole_amplitudes':len(psi),'full_C_and_FstarF_matching_coefficients':len(Ct),'Fstar_psi_zero':True,'periodic_height_point_checks':periodic,'scope':'Finite controls plus analytic proof check; not microscopic output convergence.','cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'own_reused_word_code_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['peak_rss_bytes']<120000000
(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
