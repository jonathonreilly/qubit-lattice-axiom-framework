import importlib.util
from pathlib import Path
from collections import Counter,deque
from fractions import Fraction
import numpy as np
import sympy as sp
p=Path('/Users/jonreilly/Documents/Codex/toe-charged-phase-20260914/.claude/science/physics-loops/toe-charged-phase-20260914/block9_ice_transport_check.py')
spec=importlib.util.spec_from_file_location('ice',p);ice=importlib.util.module_from_spec(spec);spec.loader.exec_module(ice)
roots,faces,start=ice.geometry(2);volume=8
endpoints=[]
for i in range(3):
 for r in roots:
  q=list(r);q[i]=(q[i]+1)%2;endpoints.append((roots.index(r),roots.index(tuple(q))))
remaining=[6]*8;degrees=[0]*8;states=[]
def grow(j,state):
 if j==24:
  assert degrees==[3]*8;states.append(state);return
 u,v=endpoints[j];remaining[u]-=1;remaining[v]-=1
 for bit in (0,1):
  degrees[u]+=bit;degrees[v]+=bit
  if all(degrees[k]<=3<=degrees[k]+remaining[k] for k in (u,v)):grow(j+1,state|(bit<<j))
  degrees[u]-=bit;degrees[v]-=bit
 remaining[u]+=1;remaining[v]+=1
grow(0,0);assert len(states)==9600
unseen=set(states);data=[]
while unseen:
 start=min(unseen);unseen.remove(start);queue=deque([start]);members=[start];pot={start:0};periods=[];active=0;moves=0
 while queue:
  state=queue.popleft()
  for r,ij,ids,mask in faces:
   bits=[(state>>q)&1 for q in ids]
   if bits[0]!=bits[2] or bits[1]!=bits[3] or bits[0]==bits[1]:continue
   dest=state^mask;phase=(-1)**sum(r)*(2*bits[0]-1)*int(ij==(0,1));moves+=1;active+=phase!=0
   if dest not in pot:pot[dest]=pot[state]-phase;queue.append(dest);members.append(dest);unseen.remove(dest)
   else:periods.append(pot[state]-phase-pot[dest])
 nonzero=sorted(set(periods)-{0});assert all(z%4==0 for z in nonzero)
 data.append((len(members),moves//2,active//2,bool(nonzero),tuple(nonzero)))
print('components',len(data), 'summary',Counter((n,m,a,positive) for n,m,a,positive,periods in data))
print('active but exact source', [d for d in data if d[2] and not d[3]])
# Exact Krylov minimal polynomial for the zero-flux mobile source drift.
_,_,ss,edges=ice.ice_component();N=len(ss);B,L,b,a=ice.graph_data(edges,N);b=list(map(int,b));vectors=[b]
def lap(v):
 out=[0]*N
 for x,y,_,_ in edges:
  z=v[x]-v[y];out[x]+=z;out[y]-=z
 return out
for rank in range(1,15):
 vectors.append(lap(vectors[-1]));M=sp.Matrix.hstack(*[sp.Matrix(v) for v in vectors])
 null=M.nullspace()
 if null:
  relation=null[0];assert relation[-1]!=0;relation=relation/relation[-1]
  print('Krylov degree',rank,'relation',list(relation),flush=True)
  phi=-sum((relation[j]*sp.Matrix(vectors[j-1]) for j in range(1,rank+1)),sp.zeros(N,1))/relation[0]
  assert sp.Matrix(lap(list(phi)))==sp.Matrix(b)
  chi=sp.Rational(2,N*8)*(sum(int(z)**2 for z in a)-(sp.Matrix(b).T*phi)[0])
  print('Exact Krylov curvature',chi,'corrector values',Counter(map(str,phi)),flush=True)
  break
