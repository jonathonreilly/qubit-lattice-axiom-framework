#!/usr/bin/env python3
"""Exact path sums and reduced column-model spectra; not 96-physical-qubit diagonalization."""
from pathlib import Path
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=[".claude/science/physics-loops/neutral-composite-24h-20261018/native/HIERARCHICAL_ROW_TUNNELING_PROOF.md"]
import numpy as np,json
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
from math import comb
from fractions import Fraction
# Exact cycle-path sum, excluding endpoints with zero denominator.
def paths(n):
 f={0:Fraction(1)}
 for size in range(n):
  for mask,val in list(f.items()):
   if mask.bit_count()!=size:continue
   for j in range(n):
    if mask>>j&1:continue
    q=mask|1<<j
    runs=sum(((q>>k)&1) and not((q>>((k-1)%n))&1) for k in range(n))
    f[q]=f.get(q,Fraction(0))+val/(runs or 1)
 return f[(1<<n)-1]
for n in range(2,15):assert paths(n)==comb(2*n-2,n-1)
M=4;D=1<<9
reps=[sum(((s>>((x-1)*3+y-1))&1)<<(x*4+y) for x in range(1,4) for y in range(1,4)) for s in range(D)]
def canonical(q):
 a=[(q>>(x*4))&1 for x in range(4)];b=[((q>>y)&1)^a[0] for y in range(4)]
 s=sum((((q>>(x*4+y))&1)^a[x]^b[y])<<((x-1)*3+y-1) for x in range(1,4) for y in range(1,4))
 return s,a,b
edges=[(x*4+y,((x+1)%4)*4+y) for x in range(4) for y in range(4)]+[(x*4+y,x*4+(y+1)%4) for x in range(4) for y in range(4)]
diag=np.array([-sum((-1)**sum((q>>i)&1 for i in [x*4+y,((x+1)%4)*4+y,x*4+(y+1)%4,((x+1)%4)*4+(y+1)%4]) for x in range(4) for y in range(4)) for q in reps])
results=[]
for t in [.1,.05,.02,.01,.005]:
 ev=[];vec=[];res=[]
 for character in [0,1]:
  rr=list(range(D));cc=list(range(D));vv=list(diag.astype(float))
  for col,q in enumerate(reps):
   for i,j in edges:
    row,a,b=canonical(q^(1<<i)^(1<<j));rr.append(row);cc.append(col);vv.append(-t*(-1)**(character*a[0]))
  H=coo_matrix((vv,(rr,cc)),shape=(D,D)).tocsr();assert (H-H.T).nnz==0
  e,v=eigsh(H,k=1,which='SA',tol=1e-13,v0=np.ones(D));ev.append(float(e[0]));vec.append(v[:,0]);res.append(float(np.linalg.norm(H@v[:,0]-e[0]*v[:,0])))
 results.append(dict(t=t,gap=ev[1]-ev[0],gap_over_2t2=(ev[1]-ev[0])/(2*t*t),Z00_weight=float(np.dot(vec[0],vec[1])**2),residual=max(res)))
output=dict(status='bounded-support',path_sum_n=list(range(2,15)),column_model_spectra=results,scope='Exact finite path sums and 16-column coefficient-model spectra only; native hierarchy is an analytic proof, not native96-qubit diagonalization')
p=Path(__file__).resolve().parents[1]/'outputs/native_row_tunneling/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(output,indent=2)+'\n');print(json.dumps(output))
