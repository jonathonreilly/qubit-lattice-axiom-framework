import numpy as np,json,time
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

def run(nx,ny,L):
 A=nx*ny;edges=[(x+nx*y,x+dx+nx*(y+dy),axis) for y in range(ny) for x in range(nx) for dx,dy,axis in [(1,0,'x'),(0,1,'y')] if x+dx<nx and y+dy<ny]
 def moves(h):
  for a,b,axis in edges:
   for z in set([h[a],h[a]+1])&set([h[b],h[b]+1]):
    v=list(h);sa=1 if z>h[a] else -1;sb=1 if z>h[b] else -1;v[a]+=sa;v[b]+=sb;m=min(v);v=tuple(x-m for x in v)
    if max(v)<=L:yield v,-1 if axis=='x' else sa*sb
 states=[(0,)*A];idx={states[0]:0}
 for h in states:
  for v,a in moves(h):
   if v not in idx:idx[v]=len(states);states.append(v)
  if len(states)>1000000:raise RuntimeError('guard1M')
 rr=[];cc=[];dd=[]
 for h,i in idx.items():
  for v,a in moves(h):rr.append(idx[v]);cc.append(i);dd.append(a)
 H=coo_matrix((dd,(rr,cc)),shape=(len(states),len(states))).tocsr().astype(float);assert np.max(abs((H-H.T).data),initial=0)==0

 return H,states
