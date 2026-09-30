#!/usr/bin/env python3
"""Disclosed author reuse; exact rational compact trial, not full T0 evaluation."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import resource,time,json,hashlib,signal
from pathlib import Path
from collections import defaultdict
from itertools import combinations
resource.setrlimit(resource.RLIMIT_CPU,(90,91))
signal.alarm(180)
t0,c0=time.monotonic(),time.process_time()
out=Path(__file__).resolve().parent;pack=out.parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert not(runtime/'STOP_REQUESTED.json').exists()
 assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
 assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=256*1024**2
 guard.calls+=1
guard.calls=0;guard()
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import splu
source=pack/'native-scattering-route/check_matching.py'
ns={};exec(compile(source.read_text().split('# All abstract graphs')[0],str(source),'exec'),ns)
add,sub,canonical,perfect,action12,disp=[ns[k] for k in ('add','sub','canonical','perfect','action12','disp')]
mon=list(combinations(range(5),2))+[(i,i) for i in range(5)];mon.sort();mi={p:i for i,p in enumerate(mon)}
z5=(0,)*5
u=[(1,0,0,0,0),(0,1,0,0,0),(-1,-1,0,0,0)]
def weight(a,b):
 d=sub(b,a);ix=[i for i in range(3) if d[i]]
 if len(ix)==1 and abs(d[ix[0]])==2:return u[ix[0]]
 if len(ix)==2 and all(abs(d[i])==1 for i in ix):
  v=[0]*5;v[2+[(0,1),(0,2),(1,2)].index(tuple(ix))]=-d[ix[0]]*d[ix[1]];return tuple(v)
 return z5
def phi(S):
 a,b,c,d=S;p=[0]*15
 for aa,bb,cc,dd in [(a,b,c,d),(a,c,b,d),(a,d,b,c)]:
  for i,x in enumerate(weight(aa,bb)):
   if x:
    for j,y in enumerate(weight(cc,dd)):
     if y:p[mi[tuple(sorted((i,j)))]]+=x*y
 return p
shapes={((0,0,0),)}
for n in range(2,5):
 shapes={canonical(S+(add(x,d),)) for S in shapes for x in S for d in disp if add(x,d) not in S};guard()
core=sorted(S for S in shapes if perfect(S));assert len(core)==1487
index={S:i for i,S in enumerate(core)}
rows=[];cols=[];vals=[];F=np.zeros((len(core),15),dtype=np.int64)
for i,S in enumerate(core):
 row=defaultdict(int)
 for z,(a,b) in action12(S).items():row[canonical(z)]+=a+b
 for z,c in row.items():
  if not c:continue
  if z in index:rows.append(i);cols.append(index[z]);vals.append(c)
  F[i]+=c*np.array(phi(z),dtype=np.int64)
 if i%50==0:guard()
A=coo_matrix((np.array(vals,dtype=np.int64),(rows,cols)),shape=(len(core),len(core))).tocsr()
assert (A-A.T).nnz==0
# A and F both contain 12 times their physical values.
X=splu(A.astype(float).tocsc()).solve(-F.astype(float));guard()
scale=2**16;Xi=np.rint(scale*X).astype(np.int64)
maxx=int(abs(Xi).max());rownorm=int(np.asarray(abs(A).sum(axis=1)).max())
assert rownorm*maxx<2**63 and len(core)*rownorm*maxx**2<2**63
AX=A@Xi
raw=json.loads((pack/'native-interaction-route/quartic.json').read_text())
B=np.array(raw['energy_mu_matrix_numerator'],dtype=np.int64)+np.array(raw['energy_tau_matrix_numerator'],dtype=np.int64)
# Conservative intermediate-overflow controls before all integer dot products.
assert len(core)*maxx*int(abs(F).max())*scale<2**61
assert int(abs(B).max())*scale**2<2**61
Qnum=B*scale**2+Xi.T@AX+scale*(F.T@Xi+Xi.T@F)
assert np.array_equal(Qnum,Qnum.T)
den=12*scale**2
from fractions import Fraction
# Exact coherent directions in raw polynomial coordinates, with s=1.
pE=np.zeros(15,dtype=np.int64);pE[mi[(0,0)]]=1;pE[mi[(0,1)]]=-1;pE[mi[(1,1)]]=1
E=Fraction(int(pE@Qnum@pE),2*den)
T=Fraction(int(Qnum[mi[(2,2)],mi[(2,2)]]),2*den)
# Real normalized Sym^2 frame. Floats below are diagnostics, not interval proofs.
L=np.zeros((5,5));L[0,0]=1/np.sqrt(2);L[0,1]=1/np.sqrt(6);L[1,0]=-1/np.sqrt(2);L[1,1]=1/np.sqrt(6)
for k in range(2,5):L[k,k]=1/np.sqrt(2)
P=np.zeros((15,15))
for a,(i,j) in enumerate(mon):
 for b,(k,l) in enumerate(mon):P[a,b]=L[i,k]*L[j,k] if k==l else (L[i,k]*L[j,l]+L[i,l]*L[j,k])/np.sqrt(2)
Ttrial=2*P.T@(Qnum/den)@P;Tbare=2*P.T@(B/12)@P
np.savez_compressed(out/'CORE_TRIAL.npz',rows=rows,cols=cols,vals=vals,F12=F,X_numerator=Xi,scale=scale,core=np.array(core,dtype=np.int16))
result={'scope':'Exact rational compact-trial upper matrix for full infinite-lattice threshold form; floating eigenvalues diagnostic only. Not the exact threshold matrix or EOS.',
'benchmark':{'mu':1,'tau':1},'core_dimension':len(core),'matrix_nnz':A.nnz,'monomial_order':mon,'trial_denominator':scale,'upper_pulse_matrix_denominator':den,'upper_pulse_matrix_numerator':[[str(int(a)) for a in row] for row in Qnum],
'exact_normalized_coherent_threshold_upper':{'E1':str(E),'T12':str(T)},
'diagnostic_bare_eigenvalues':np.linalg.eigvalsh(Tbare).tolist(),'diagnostic_compact_trial_eigenvalues':np.linalg.eigvalsh(Ttrial).tolist(),
'diagnostic_max_solve_residual_12H':float(np.max(abs(A@X+F))),
'diagnostic_integer_trial_residual_12H':float(np.max(abs(AX/scale+F))),
'overflow_bound_N_rowL1_maxX_squared':len(core)*rownorm*maxx**2,
'reused_action_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'bare_quartic_sha256':hashlib.sha256((pack/'native-interaction-route/quartic.json').read_bytes()).hexdigest(),
'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'deadline_stop_checks':guard.calls}
guard();(out/'CORE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if 'matrix_numerator' not in k},indent=2))
