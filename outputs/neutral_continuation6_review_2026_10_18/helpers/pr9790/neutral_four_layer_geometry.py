from pathlib import Path
import numpy as np,json,time,sys
from numba import njit
from scipy.sparse.linalg import LinearOperator,eigsh
@njit
def linmap(x,cols):
 y=0;i=0
 while x:
  if x&1:y^=cols[i]
  x>>=1;i+=1
 return y
@njit
def makeorbits(n,rot,ref):
 dim=1<<n;ids=np.full(dim,-1,np.int32);reps=np.empty(dim//8+dim//2,np.int64);sizes=np.empty(len(reps),np.int8);count=0
 for x in range(dim):
  if ids[x]>=0:continue
  vals=np.empty(8,np.int64);v=x
  for j in range(4):vals[j]=v;v=linmap(v,rot)
  v=linmap(x,ref)
  for j in range(4):vals[4+j]=v;v=linmap(v,rot)
  size=0
  for j in range(8):
   if ids[vals[j]]<0:ids[vals[j]]=count;size+=1
  reps[count]=x;sizes[count]=size;count+=1
 return ids,reps[:count].copy(),sizes[:count].copy()
@njit
def par(x):
 x^=x>>32;x^=x>>16;x^=x>>8;x^=x>>4
 return (0x6996>>(x&15))&1
@njit
def diagonal(reps,edges):
 out=np.empty(len(reps))
 for i in range(len(reps)):
  val=0
  for e in edges:val+=1-2*par(reps[i]&e)
  out[i]=-5*val
 return out
@njit
def apply(v,diag,reps,sizes,ids,flips):
 out=diag*v
 for i in range(len(v)):
  for f in flips:
   j=ids[reps[i]^f];out[i]-=4*np.sqrt(sizes[i]/sizes[j])*v[j]
 return out

def geometry(R,periodic=False):
 n=(R-1)**2
 def expand(x):
  s=0
  for a in range(R-1):
   for b in range(R-1):
    if (x>>(a*(R-1)+b))&1:
     for i,j in [(a,b),(a,R-1),(R-1,b),(R-1,R-1)]:s^=1<<(i*R+j)
  return s
 def transform(x,kind):
  s=expand(x);out=0
  for i in range(R):
   for j in range(R):
    if(s>>(i*R+j))&1:
     a,b=(j,R-1-i) if kind=='rot' else(i,R-1-j)
     if a<R-1 and b<R-1:out^=1<<(a*(R-1)+b)
  return out
 rot=np.array([transform(1<<k,'rot') for k in range(n)],np.int64);ref=np.array([transform(1<<k,'ref') for k in range(n)],np.int64)
 masks=[]
 for x in range(R):
  for y in range(R):masks.append(sum(1<<(a*(R-1)+b) for a in range(R-1) for b in range(R-1) if (x==a or x==R-1)and(y==b or y==R-1)))
 edges=[]
 for x in range(R):
  for y in range(R):
   if x+1<R or periodic:edges.append(masks[x*R+y]^masks[((x+1)%R)*R+y])
   if y+1<R or periodic:edges.append(masks[x*R+y]^masks[x*R+(y+1)%R])
 flips=[]
 for x in range(R if periodic else R-1):
  for y in range(R if periodic else R-1):flips.append(sum(1<<(a*(R-1)+b) for a,b in [(x,y),((x+1)%R,y),(x,(y+1)%R),((x+1)%R,(y+1)%R)] if a<R-1 and b<R-1))
 return rot,ref,np.array(edges,np.int64),np.array(flips,np.int64)
