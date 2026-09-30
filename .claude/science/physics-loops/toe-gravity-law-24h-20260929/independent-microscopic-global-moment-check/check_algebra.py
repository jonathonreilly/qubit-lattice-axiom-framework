#!/usr/bin/env python3
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import resource,signal,time,json,hashlib
from pathlib import Path
from itertools import combinations
resource.setrlimit(resource.RLIMIT_CPU,(10,11));signal.alarm(60)
t0,c0=time.monotonic(),time.process_time();p=Path(__file__).resolve().parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not(rt/'STOP_REQUESTED.json').exists();assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
import sympy as s
states=[(w,b) for w in range(3) for b in range(3)];idx={x:i for i,x in enumerate(states)}
W=s.diag(*(w for w,b in states));Kd=s.diag(*(w+b for w,b in states));N=s.diag(*(b-w for w,b in states))
j=s.zeros(9);F=s.zeros(9)
for col,(w,b) in enumerate(states):
 if w>0 and b<2:j[idx[w-1,b+1],col]=w+b+1
 if w<2 and b<2:F[idx[w+1,b+1],col]=w+2*b+1
comm=lambda a,b:a*b-b*a
assert comm(N,F)==s.zeros(9);assert comm(Kd,j)==s.zeros(9)
S1=F.T-F;j1=comm(S1,j);X=j.T*j1-j1.T*j
assert X.T==-X
IW=s.zeros(9)
for a in range(9):
 for b in range(9):
  if X[a,b]:
   assert abs(W[a,a]-W[b,b])==1
   IW[a,b]=X[a,b]/(W[a,a]-W[b,b])
assert IW.T==IW
Sl=s.I*IW/2;Hcorr=comm(Sl,W);rows=[]
for q in (2,3,5):
 f=s.diag(*(q**(w+b) for w,b in states))
 cross=j.T*f*j1+j1.T*f*j-(j.T*j1+j1.T*j)*f/2-f*(j.T*j1+j1.T*j)/2
 assert cross==comm(f,X)/2
 hc=s.I*comm(Hcorr,f)
 assert hc+cross==s.zeros(9)
 assert cross-hc==2*cross
 rows.append({'tilt_q':q,'uncancelled_entries':sum(x!=0 for x in cross),'corrected_zero':True,'wrong_sign_doubles':True})
# A has a degenerate zero-count block; all arithmetic is rational.
A=[0,0,1,2];Q=s.diag(*(2**a for a in A));Qp=s.diag(*(4**a for a in A));G=s.Matrix([[0,1,-1,0],[-1,0,1,1],[1,-1,0,1],[0,-1,-1,0]])
gnorm=3;M=s.Integer(4);gap=s.Rational(1,2);constant=(M-1)+8*M**2/gap
minorcount=0
for den in (256,512,1024):
 t=s.Rational(1,den);I=s.eye(4);U=(I-t*G)*(I+t*G).inv();assert U.T*U==I
 eta_upper=2*t*gnorm;assert eta_upper<=gap/(4*M)
 D=(1+constant*eta_upper**2)*Qp-U.T*Q*U
 for k in range(1,5):
  for inds in combinations(range(4),k):assert D.extract(inds,inds).det()>0;minorcount+=1
result={'grade_model':'abstract9-state algebra, not a physical Gauss graph','pole_controls':rows,'small_gate_principal_minors':minorcount,'small_gate_constant':str(constant),'zero_count_degeneracy':2,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['peak_rss_bytes']<120000000
(p/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
