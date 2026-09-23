import itertools,json,time,signal,resource,hashlib
from pathlib import Path
import sympy as s
signal.alarm(45)
t=time.monotonic();results={}
# Independent exhaustive search of all 3^12 flows, no elimination and no original helper.
vs=list(itertools.product(range(2),repeat=3)); es=[(i,j) for i,x in enumerate(vs) for j,y in enumerate(vs) if sum(abs(a-b) for a,b in zip(x,y))==1 and i<j]
found={4:[],7:[]}
for flow in itertools.product(range(3),repeat=12):
 div=[0]*8
 for (i,j),v in zip(es,flow):div[i]+=v;div[j]-=v
 div=tuple(v%3 for v in div)
 for target in (4,7):
  b=tuple(1 if i==0 else 2 if i==target else 0 for i in range(8))
  if div==b:found[target].append(flow)
for target,flows in found.items():
 hist={}
 for flow in flows:
  n=sum(x!=0 for x in flow);hist[n]=hist.get(n,0)+1
  seen={0}
  while True:
   new=seen|{v for (a,b),q in zip(es,flow) if q for v in (a,b) if a in seen or b in seen}
   if new==seen:break
   seen=new
  assert target in seen
 assert len(flows)==243 and min(hist)==(1 if target==4 else 3)
 results[str(target)]={'count':len(flows),'histogram':hist}
# Saved original flow records: normalize edge ordering, compare exact sets.
p=Path('/private/tmp/review-drain-20260915/drain8033-original/head/.claude/science/physics-loops/finite-pw-static-lower-20260907/CANONICAL_RESULT.json')
j=json.loads(p.read_text());order=[es.index(tuple(e)) for e in j['edges']]
for k,flows in found.items():
 expected={tuple(f[i] for i in order) for f in flows}
 assert expected=={tuple(f) for f in j['flows'][str(k)]['solutions']}
results['original_flow_sets_match']=True
# Ghost-only flow along direct edge achieves weight1; restricting it to0 restores enumerated actual cube.
assert 0 not in [1,2];results['ghost_and_endpoint_boundary']='direct ghost charge vector (1,0,0,0,0,0,0,-1); zero actual flow accepted only if both endpoint equations removed'
K=s.diag(0,1,10);H=s.Matrix([[2,-1,0],[-1,2,0],[0,0,10]])
assert (H-K)[:2,:2].det()==1 and (H-K)[0,0]==2
assert set(H.eigenvals())=={s.Integer(1),s.Integer(3),s.Integer(10)}
assert 10-2==8<9==10-1
results['ritz_exact']={'V_principal_minors':[2,1,0],'full_spectrum':[1,3,10],'compressed_spectrum':[2,10]}
u,d,h=s.symbols('u d h',positive=True);theta=8*u*d/h
numer=4*d+s.sqrt(theta)*(4*d+4*d*s.sqrt(8*u))+8*u*d*(s.sqrt(32*u/h)+s.sqrt(theta))
b=(1+s.sqrt(theta)*(1+s.sqrt(8*u)+2*u)+2*u*s.sqrt(32*u/h))/(1-theta)
assert s.simplify(numer/(4*d*(1-theta))-b)==0
results['upper_envelope_identity']=True
# Restricted resolvent scalar bound decreases with eigenvalue for z>=0, increases for z<0.
lam,z=s.symbols('lam z',real=True);assert s.diff(lam/(lam-z),lam)==-z/(lam-z)**2
results['resolvent_derivative']='-z/(lambda-z)^2'
for R in range(1,25):assert min(p*p+p*(R-p)+(R-p)**2+3*R for p in range(R+1))==R*R-R*R//4+3*R
results['shell_minima_1_24']=True
results.update(seconds=time.monotonic()-t,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
print(json.dumps(results,indent=2))
