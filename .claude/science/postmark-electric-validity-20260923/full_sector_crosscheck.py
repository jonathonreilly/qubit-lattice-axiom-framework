#!/usr/bin/env python3
"""Independent dense finite-spin sector assembly to cross-check H2 and H4."""
from itertools import permutations
import importlib.util, json, math
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('probe', HERE/'fixed_time_probe.py')
p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
bg=(1,0,1,0,1,0); qstar=(1,-1,1,0,1,1); estar=(1,0,0,0,0,1)
qs=sorted(set(permutations((0,-1,1,1,1,1))))
rows=[]
for S in (2,3,4,6):
 C=S*(S+1); states=[]
 for q in qs:
  for e0 in range(-S,S+1):
   E=[e0]
   for j in range(1,6): E.append(E[-1]+q[j]-bg[j])
   if max(abs(x) for x in E)<=S:
    st=(q,tuple(E))
    assert all(E[j]-E[(j-1)%6]+bg[j]==q[j] for j in range(6))
    states.append(st)
 ix={st:i for i,st in enumerate(states)}; T=np.zeros((len(states),len(states)))
 for col,(q,E) in enumerate(states):
  for x,c in enumerate(q):
   if c==0:continue
   for step in (-1,1):
    y=(x+step)%6
    if q[y]!=0:continue
    edge=x if step==1 else y; a=-c*step; F=list(E);F[edge]+=a
    if max(abs(z) for z in F)>S:continue
    amp=-math.sqrt(max(0,1-E[edge]*(E[edge]+a)/C))
    qq=list(q);qq[x],qq[y]=0,c; dest=(tuple(qq),tuple(F))
    T[ix[dest],col]+=amp
 assert np.max(abs(T-T.T))<1e-14
 W=np.array([sum(q[a]==0 for a in (0,2,4)) for q,E in states])
 P=np.where(W==0)[0];Q1=np.where(W==1)[0];Q2=np.where(W==2)[0]
 A=T[np.ix_(Q1,P)];M=A.T@A;Z=T[np.ix_(Q2,Q1)]@A
 H2=-M;H4=M@M-0.5*Z.T@Z
 radius=200; nodes,inv=p.path_basis(radius)
 ns=[n for n,st in nodes.items() if max(abs(e) for e in st[1])<=S]
 pnodes=[nodes[n] for n in ns]
 ids=[ix[st] for st in pnodes]
 local2=p.h2_rows({n:nodes[n] for n in ns},inv,S)
 local4=p.h4_rows({n:nodes[n] for n in ns},inv,S)
 local2mat=p.sparse_from_rows(local2,ns).toarray().real
 local4mat=p.sparse_from_rows(local4,ns).toarray().real
 err2=float(np.max(abs(H2[np.ix_([np.where(P==i)[0][0] for i in ids], [np.where(P==i)[0][0] for i in ids])]-local2mat)))
 err4=float(np.max(abs(H4[np.ix_([np.where(P==i)[0][0] for i in ids], [np.where(P==i)[0][0] for i in ids])]-local4mat)))
 # Measure couplings from this rotor path component to all other P states.
 pindex={state:k for k,state in enumerate([states[i] for i in P])}
 comp=[pindex[st] for st in pnodes]
 outside=[k for k in range(len(P)) if k not in set(comp)]
 leak2=float(np.max(abs(H2[np.ix_(comp,outside)]))) if outside else 0.0
 leak4=float(np.max(abs(H4[np.ix_(comp,outside)]))) if outside else 0.0
 rows.append({'S':S,'full_sector_dimension':len(states),'P_dimension':len(P),'component_dimension':len(comp),'H2_submatrix_max_error':err2,'H4_submatrix_max_error':err4,'H2_cross_component_max':leak2,'H4_cross_component_max':leak4,'H2_norm':float(np.linalg.norm(H2,2)),'H4_norm':float(np.linalg.norm(H4,2))})
out={'status':'independent finite-sector dense matrix check','construction':'full physical (q,E) basis and dense T block products; separately compared to local path assembly','results':rows}
(HERE/'FULL_SECTOR_CROSSCHECK.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
