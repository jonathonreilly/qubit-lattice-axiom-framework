import numpy as np,json
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import splu
from math import pi,log
S=[(0,0),(1,0),(0,1),(1,1),(0,-1),(1,-1)]
V=np.zeros((6,6))
for i,j in [(0,2),(0,4),(1,3),(1,5)]:V[i,j]=V[j,i]=2
r=(4-pi)/(4-2*pi)
def run(R):
 pts=[(x,y) for x in range(-R+1,R+1) for y in range(-R+1,R)];ix={p:i for i,p in enumerate(pts)};n=len(pts);A=lil_matrix((n,n));b=np.zeros(n)
 for (x,y),i in ix.items():
  A[i,i]=4
  for q in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
   if q in ix:A[i,ix[q]]=-1
   else:b[i]+=1
 ids=[ix[p] for p in S];rhs=np.zeros((n,6));rhs[ids,np.arange(6)]=1
 G=splu(A.tocsc()).solve(rhs)[ids,:];u=np.linalg.solve(np.eye(6)+G@V,np.ones(6));g=G[0,0]
 B=A.copy()
 for i in range(6):
  for j in range(6):
   if V[i,j]:B[ids[i],ids[j]]+=V[i,j]
 full=splu(B.tocsc()).solve(b)
 pred=2*r/(8*g*(1+r)-1-4*r/pi)
 return dict(R=R,g=g,source=float(u[0]+u[1]),outer=float(u[2]),ratio=float(u[0]/u[2]),predicted_source=pred,source_times_log=float((u[0]+u[1])*log(R)),full_schur_error=float(np.max(abs(full[ids]-u))),residual=float(np.linalg.norm(B@full-b)))
print(json.dumps(dict(rows=[run(R) for R in [8,16,32,64,128]],ratio_limit=r,scaled_source_limit=pi*r/(2*(1+r))),indent=2))
