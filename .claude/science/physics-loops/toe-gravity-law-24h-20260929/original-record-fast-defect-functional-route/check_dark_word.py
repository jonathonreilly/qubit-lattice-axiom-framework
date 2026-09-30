#!/usr/bin/env python3
"""Literal actual compensated H2 on two physical cubic words; no prior imports."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import itertools,json,hashlib,resource,signal,time,os
resource.setrlimit(resource.RLIMIT_CPU,(30,31));signal.alarm(90)
t0=time.monotonic();c0=time.process_time();runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
 assert not (runtime/'STOP_REQUESTED.json').exists()
 assert time.monotonic()-t0<90
 assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=150*1024**2
assert all(os.environ.get(k)=='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'))
guard();L=6
xyz=list(itertools.product(range(L),repeat=3));idx={x:i for i,x in enumerate(xyz)}
A=[i for i,x in enumerate(xyz) if sum(x)%2==0];B=[i for i,x in enumerate(xyz) if sum(x)%2]
steps=[tuple(s*int(k==j) for k in range(3)) for j in range(3) for s in (-1,1)]
shift=lambda x,d:tuple((a+b)%L for a,b in zip(x,d))
edges=[(a,idx[shift(xyz[a],d)]) for a in A for d in steps]
star={a:[j for j,(c,b) in enumerate(edges) if c==a] for a in A}
nearA={a:{c for c,b in edges if any(b==edges[j][1] for j in star[a]) and c!=a} for a in A}
assert all(len(v)==18 for v in nearA.values())
omega=(tuple(int(i in set(A)) for i in range(len(xyz))),tuple(0 for _ in edges))
matching=[j for j,(a,b) in enumerate(edges) if xyz[b]==shift(xyz[a],(1,0,0))]
assert len(matching)==len(A) and len({edges[j][1] for j in matching})==len(B)
dark=(tuple(int(i in set(B)) for i in range(len(xyz))),tuple(-int(j in matching) for j in range(len(edges))))
gauss_checks=0

def gauss(w):
 global gauss_checks
 q,E=w;div=[0]*len(xyz)
 for j,(a,b) in enumerate(edges):div[a]+=E[j];div[b]-=E[j]
 assert all(div[i]==q[i]-int(i in set(A)) for i in range(len(xyz)))
 gauss_checks+=1

def move(w,j,inward,S):
 q,E=w;a,b=edges[j]
 src,dst=(b,a) if inward else (a,b)
 if not q[src] or q[dst]:return None
 charge=q[src];step=charge if inward else -charge;z=E[j]
 squared=1-Fraction(z*(z+step),S*(S+1))
 if abs(z+step)>S:assert squared==0;return None
 if not squared:return None
 # The proof specializes to E=0,-1 and their exact returning paths.
 assert squared==1,('nonunit fixture path',z,step,squared)
 qq=list(q);ee=list(E);qq[dst]=charge;qq[src]=0;ee[j]+=step
 out=(tuple(qq),tuple(ee));gauss(out);return out

def F(w,inward,S,center=None):
 out=defaultdict(int)
 for j in (range(len(edges)) if center is None else star[center]):
  z=move(w,j,inward,S)
  if z is not None:out[z]+=1
 return dict(out)

def compose(v,inward,S,center=None):
 out=defaultdict(int)
 for w,c in v.items():
  for z,d in F(w,inward,S,center).items():out[z]+=c*d
 return {w:c for w,c in out.items() if c}

def C(w,S):
 q,E=w;out=defaultdict(Fraction)
 for a in A:
  if not all(q[c] for c in nearA[a]):continue
  for z,c in compose(F(w,False,S,a),True,S,a).items():out[z]+=c
  dspin=drot=Fraction(0)
  for j in star[a]:
   c,b=edges[j]
   if q[a] and not q[b]:
    drot+=1;dspin+=1-Fraction(E[j]*(E[j]-q[a]),S*(S+1))
  out[w]+=drot-dspin
 return {w:c for w,c in out.items() if c}

gauss(omega);gauss(dark)
# A concrete legal source word, with no inference about its actual probability.
w=omega
for j in matching:w=move(w,j,False,1)
assert w==dark
results=[]
for S in (1,2,7):
 for name,w in [('Omega',omega),('dense_dark',dark)]:
  fw=F(w,False,S);bw=F(w,True,S)
  ffstar=compose(bw,False,S);fstarf=compose(fw,True,S);comp=C(w,S)
  h=defaultdict(Fraction)
  for v,sgn in [(comp,1),(ffstar,1),(fstarf,-1)]:
   for z,c in v.items():h[z]+=sgn*c
  h={z:c for z,c in h.items() if c}
  assert not any(q==0 and w[0][b]==0 for a,b in edges for q in (w[0][a],))
  if name=='Omega':assert not h
  else:assert h=={w:6*len(A)}
  results.append({'spin':S,'word':name,'F_words':len(fw),'F_adjoint_words':len(bw),'compensation_words':len(comp),'H2_words':len(h),'H2_eigenvalue':str(h.get(w,0)),'bare_original_mark_action':'zero for every resolved sign and coherent edge, by exact input occupancy'})
  guard()
result={'scope':'Literal exact action on specified physical words, not actual bare-Omega time probabilities, a microscopic stationary state, or an estimate of the normal-form remainder.','L':L,'A_sites':len(A),'B_sites':len(B),'edges':len(edges),'perfect_matching_hops':len(matching),'gauss_output_checks':gauss_checks,'cases':results,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_name('DARK_WORD_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
