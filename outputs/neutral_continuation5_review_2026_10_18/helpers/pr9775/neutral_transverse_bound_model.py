import numpy as np,json
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

def matrix(L,a=1,b=0,c=1):
 # Half-plane representatives of r~-r. Physical unordered pairs have unit norm.
 reps=[(x,y) for y in range(L+1) for x in range(-L,L+1) if y>0 or x>0];idx={r:i for i,r in enumerate(reps)};states=[('host',r) for r in reps]
 for axis in ['x','y']:
  for ell in range(2,L+2):idx[(axis,ell)]=len(states);states.append((axis,ell))
 rr=[];cc=[];dd=[]
 for r,i in list(idx.items())[:len(reps)]:
  x,y=r
  for dx,dy,t in [(1,0,-2*a),(-1,0,-2*a),(0,1,-2*b),(0,-1,-2*b)]:
   s=(x+dx,y+dy)
   if s==(0,0):continue
   if s[1]<0 or s[1]==0 and s[0]<0:s=(-s[0],-s[1])
   if s in idx:rr.append(idx[s]);cc.append(i);dd.append(t)
 for axis,root,t in [('x',(1,0),-2*c),('y',(0,1),2*c)]:
  for ell in range(1,L+1):
   i=idx[root] if ell==1 else idx[(axis,ell)];j=idx[(axis,ell+1)];rr.extend([i,j]);cc.extend([j,i]);dd.extend([t,t])
 H=coo_matrix((dd,(rr,cc)),shape=(len(states),)*2).tocsr();assert np.max(abs((H-H.T).data),initial=0)<1e-12
 return H,states,idx
