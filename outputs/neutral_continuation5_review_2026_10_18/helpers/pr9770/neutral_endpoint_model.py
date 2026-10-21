import numpy as np,json
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
# four columns square, canonical heights minimum0; total endpoint COM momentum0.
edges=[(0,1,'x'),(2,3,'x'),(0,2,'y'),(1,3,'y')]
def moves(h):
 for a,b,axis in edges:
  for z in set([h[a],h[a]+1])&set([h[b],h[b]+1]):
   v=list(h);sa=1 if z>h[a] else -1;sb=1 if z>h[b] else -1;v[a]+=sa;v[b]+=sb;m=min(v);v=tuple(x-m for x in v)
   amp=-1 if axis=='x' else sa*sb
   yield v,amp

def matrix(L,k):
 states=[(0,0,0,0)];idx={states[0]:0}
 for h in states:
  for v,a in moves(h):
   if max(v)<=L and v not in idx:idx[v]=len(states);states.append(v)
 rr=[];cc=[];dd=[]
 for h,i in idx.items():
  for a,b,axis in edges:
   for z in set([h[a],h[a]+1])&set([h[b],h[b]+1]):
    v=list(h);sa=1 if z>h[a] else -1;sb=1 if z>h[b] else -1;v[a]+=sa;v[b]+=sb;m=min(v);v=tuple(x-m for x in v)
    if v in idx:rr.append(idx[v]);cc.append(i);dd.append((-1 if axis=='x' else sa*sb)*np.exp(-1j*k*(sa+sb)/4))
 H=coo_matrix((dd,(rr,cc)),shape=(len(states),len(states))).tocsr();return H,states
