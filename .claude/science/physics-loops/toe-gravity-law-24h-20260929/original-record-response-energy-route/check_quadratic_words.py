#!/usr/bin/env python3
"""Literal finite-word Gauss/gradient corroboration, no exact-D or full-carrier solver."""
import datetime, hashlib, json, os, resource, time
from fractions import Fraction as F
from pathlib import Path
BASE=Path(__file__).resolve().parent
RUN=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
t0=time.monotonic(); c0=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    assert os.environ.get(name)=='1', (name,os.environ.get(name))
deadline=json.loads((RUN/'DEADLINE.json').read_text())['deadline_epoch']
def guard():
    assert not (RUN/'STOP_REQUESTED.json').exists(), 'STOP_REQUESTED'
    assert time.time()<deadline, 'campaign deadline'
    assert time.monotonic()-t0<30, 'wall ceiling'
    assert time.process_time()-c0<5, 'CPU ceiling'
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<60*1024**2, 'RSS ceiling'
guard()
L=16; origin=(0,0,0)
def v(x): return tuple(t%L for t in x)
def add(a,b): return v(tuple(x+y for x,y in zip(a,b)))
basis=[(1,0,0),(0,1,0),(0,0,1)]
star=[v(tuple(s*x for x in e)) for e in basis for s in (1,-1)]
q={}
for x in range(L):
 for y in range(L):
  for z in range(L):
   if (x+y+z)%2==0:q[x,y,z]=1
q.pop(origin)
for e in basis:q[v(e)]=1;q[v(tuple(-x for x in e))]=-1
q[3,0,0]=1
E={}
def edgeadd(E,a,axis,val):
 key=(v(a),axis);E[key]=E.get(key,0)+val
 if E[key]==0:E.pop(key)
for axis,e in enumerate(basis):
 edgeadd(E,origin,axis,-1);edgeadd(E,tuple(-x for x in e),axis,-1)
for x in range(3):edgeadd(E,(x,0,0),0,-1)
words={'psi':(q.copy(),E.copy())}
phiE=E.copy()
edgeadd(phiE,(0,3,0),0,1);edgeadd(phiE,(1,3,0),1,1)
edgeadd(phiE,(0,4,0),0,-1);edgeadd(phiE,(0,3,0),1,-1)
words['phi']=(q.copy(),phiE)
chiq=q.copy();chiq.pop((1,0,0));chiq[5,0,0]=1
chiE=E.copy()
for x in range(1,5):edgeadd(chiE,(x,0,0),0,-1)
words['chi']=(chiq,chiE)
def gauss(q,E):
 div={}
 for (a,axis),field in E.items():
  b=add(a,basis[axis]);div[a]=div.get(a,0)+field;div[b]=div.get(b,0)-field
 bad=[]
 for x in range(L):
  for y in range(L):
   for z in range(L):
    a=(x,y,z);want=q.get(a,0)-int((x+y+z)%2==0)
    if div.get(a,0)!=want:bad.append((a,div.get(a,0),want))
 assert not bad,bad
 return L**3
rows=0;facts={}
for name,(qw,ew) in words.items():
 guard();rows+=gauss(qw,ew)
 nB=sum(sum(a)%2 for a in qw);holes=L**3//2-sum(sum(a)%2==0 for a in qw)
 assert nB==7 and holes==1 and sum(qw.values())==L**3//2
 bright=[b for b in star if b not in qw]
 assert bright==([] if name!='chi' else [(1,0,0)])
 assert max(map(abs,ew.values()))==2
 facts[name]={'N_B':nB,'W':holes,'Ntot':len(qw),'total_charge':sum(qw.values()),'bare_bright_B_neighbors':bright,'max_abs_field':2,'field_edges':len(ew)}
assert words['psi']!=words['phi'] and words['psi']!=words['chi'] and words['phi']!=words['chi']
# Both original signs; squared normalized spin amplitudes, no rotor substitution.
S=4;C=S*(S+1);birth=[]
for sign in (1,-1):
 qw=chiq.copy();ew=chiE.copy();qin=(0,0,0);qb=(1,0,0)
 assert qin not in qw and qb not in qw
 Ei=ew[(qin,0)];weight=F(C-Ei*(Ei+sign),C)
 qw[qin]=sign;qw[qb]=-sign;edgeadd(ew,qin,0,sign)
 assert max(map(abs,ew.values()))<=S
 rows+=gauss(qw,ew)
 birth.append({'sign':sign,'input_E':Ei,'output_E':Ei+sign,'squared_weight':str(weight)})
assert [x['squared_weight'] for x in birth]==['9/10','7/10']
A=[[0,1,0],[1,0,1],[0,1,0]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
A2=mm(A,A);A4=mm(A2,A2)
assert A2==[[1,0,1],[0,2,0],[1,0,1]]
assert A4==[[2*x for x in row] for row in A2] # O=A/sqrt2 has O² a projection.
# j psi=j phi=0; j chi is nonzero. No exact-J runner is claimed.
assert A[2][0]==0 and F(A2[2][0],2)==F(1,2)
control={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Five exact finite physical words; bare gradients only. Exact-D asymptotics and absence of a uniform chain constant are analytic, not numerically tested. Input is not asserted to be the actual Omega ensemble.','L':L,'S':S,'words':facts,'births':birth,'gauss_rows_checked':rows,'O_squared_matrix':[[str(F(x,2)) for x in row] for row in A2],'bare_gradient_O_on_psi_squared':0,'bare_gradient_O_squared_on_psi_squared_resolved_plus':str(F(9,40)),'bare_gradient_O_squared_on_psi_squared_original_coherent':str(F(2,5)),'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'threads':{name:os.environ[name] for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS')}}
guard();(BASE/'QUADRATIC_WORD_RESULTS.json').write_text(json.dumps(control,indent=2)+'\n');print(json.dumps(control,indent=2))
