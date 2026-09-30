#!/usr/bin/env python3
"""Independent rational Neumann form and literal qubit removal controls."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import itertools,json,time,resource,signal
from fractions import Fraction as F
from pathlib import Path
signal.alarm(30)
import sympy as sp
import numpy as np
P=Path(__file__).resolve().parent;t=time.process_time();n=3;pts=list(itertools.product(range(n),repeat=3));ix={x:i for i,x in enumerate(pts)};nn=len(pts);L=sp.zeros(nn)
for x in pts:
 for k in range(3):
  y=list(x);y[k]+=1;y=tuple(y)
  if y in ix:
   i,j=ix[x],ix[y];L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
J=sp.ones(nn)/nn;G=(L+J).inv()-J
assert L*G==sp.eye(nn)-J and G*sp.ones(nn,1)==sp.zeros(nn,1)
rows=[]
for pins in [[(1,1,1)],[(0,0,0),(2,2,2)],[(0,1,1),(2,1,1),(1,2,2)]]:
 ids=[ix[x] for x in pins];m=len(ids);C=G.extract(ids,ids);one=sp.ones(m,1);u=G[:,ids]*C.inv()*one;f=sp.ones(nn,1)-u;assert all(f[i]==0 for i in ids) and sum(f)==nn
 E=(f.T*L*f)[0];norm=(f.T*f)[0];cap=(one.T*C.inv()*one)[0];assert E==cap
 B=max(sum(abs(C[i,j]) for j in range(m)) for i in range(m));assert E>=sp.Rational(m)*norm/(nn*(B+sp.Rational(m,4*n)))
 assert (u.T*u)[0]<=sp.Rational(n*n,4)*E
 rows.append({'pins':pins,'exact_capacity':str(E),'norm_squared':str(norm),'row_bound':str(B)})
# Independent construction: exact graph inverse vs FFT on the doubled periodic graph.
period=2*n;wave=np.fft.fftfreq(period)*2*np.pi;ell=sum(4*np.sin(k/2)**2 for k in np.meshgrid(wave,wave,wave,indexing='ij'));inv=np.zeros_like(ell);inv[ell>0]=1/ell[ell>0];GT=np.fft.ifftn(inv).real
maxerr=0;wrong=0
for x in pts:
 for y in pts:
  val=0
  for signs in itertools.product((1,-1),repeat=3):
   image=tuple(yi if sg==1 else -yi-1 for yi,sg in zip(y,signs));r=tuple((a-b)%period for a,b in zip(x,image));val+=GT[r]
  actual=float(G[ix[x],ix[y]]);maxerr=max(maxerr,abs(val-actual));wrong=max(wrong,abs(val/8-actual))
assert maxerr<2e-15 and wrong>0.05
# All physical graph edges are literal coordinate pairs, no selected matching.
def distance(x,y):return max(abs(a-b) for a,b in zip(x,y))
def graph_edge(x,y):
 v=sorted(abs(a-b) for a,b in zip(x,y));return v in [[0,0,2],[0,1,1]]
def edges(S):return [(x,y) for x,y in itertools.combinations(sorted(S),2) if graph_edge(x,y)]
def good(S,R=10):return [(x,y) for x,y in edges(S) if all(min(distance(z,x),distance(z,y))>R for z in S-{x,y})]
def interior(x):return all(5<=v<95 for v in x)
def selected(S):return [(x,y) for x,y in good(S) if interior(x) and interior(y)]
configs=[]
base=set()
for x in [20,45,70]:base.update({(x,20,20),(x+2,20,20)})
configs.append(base)
configs.append(base|{(45,50,50),(45,51,51),(46,50,51)})
configs.append(base|{(1,70,70),(3,70,70)})
counts=[]
for S in configs:
 g=len(selected(S));lhs=sum(len(selected(S-{x,y})) for x,y in edges(S) if interior(x) and interior(y));rhs=g*(g-1);assert lhs>=rhs
 counts.append({'particles':len(S),'selected_dimers':g,'literal_removal_count':lhs,'g_times_gminusone':rhs})
assert counts[0]['literal_removal_count']==6 and F(counts[0]['literal_removal_count'],2)<counts[0]['g_times_gminusone']
# Exact four-removal normalization and its failing lower-template sign.
lift=[]
from math import comb
for N in [5,6,8,12,30]:
 c1=F(comb(N-1,3),comb(N-2,2));c2=F(comb(N-2,2),comb(N-2,2));c3=F(N-3,comb(N-2,2));assert c1==F(N-1,3) and c2==1 and c3==F(2,N-2)
 # With V3=0 (separated dimers for even N), difference is negative.
 diff=N*(1-c1);assert diff==-F(N*(N-4),3)<0;lift.append({'N':N,'one_body':str(c1),'three_body':str(c3),'difference_at_V3_zero_over_mu':str(diff)})
r={'scope':'exact finite Neumann inverse/pins and literal extraction counts; no all-volume proof from samples','rational_pin_forms':rows,'reflection_entries_checked':nn*nn,'reflection_max_error':maxerr,'wrong_divide_eight_max_error':wrong,'physical_removal_counts':counts,'four_removal_coefficients':lift,'cpu_seconds':time.process_time()-t,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(P/'RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
