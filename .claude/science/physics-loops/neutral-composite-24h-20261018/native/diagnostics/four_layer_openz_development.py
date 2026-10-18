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
  out[i]=-16*val
 return out
@njit
def apply(v,diag,reps,sizes,ids,flips):
 out=diag*v
 for i in range(len(v)):
  for f in flips:
   j=ids[reps[i]^f];out[i]-=18*np.sqrt(sizes[i]/sizes[j])*v[j]
 return out

def geometry(R):
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
   if x+1<R:edges.append(masks[x*R+y]^masks[(x+1)*R+y])
   if y+1<R:edges.append(masks[x*R+y]^masks[x*R+y+1])
 flips=[]
 for x in range(R-1):
  for y in range(R-1):flips.append(sum(1<<(a*(R-1)+b) for a,b in [(x,y),(x+1,y),(x,y+1),(x+1,y+1)] if a<R-1 and b<R-1))
 return rot,ref,np.array(edges,np.int64),np.array(flips,np.int64)

def run(R):
 start=time.time();rot,ref,edges,flips=geometry(R);ids,reps,sizes=makeorbits((R-1)**2,rot,ref);diag=diagonal(reps,edges);dim=len(reps)
 print(dict(R=R,dimension=dim,full=len(ids),build_seconds=time.time()-start),flush=True)
 H=lambda v:apply(v,diag,reps,sizes,ids,flips)
 rng=np.random.default_rng(1820);x=rng.normal(size=dim);y=rng.normal(size=dim)
 sym=abs(x@H(y)-H(x)@y)/(np.linalg.norm(x)*np.linalg.norm(y));assert sym<1e-10
 calls=0
 def mv(v):
  nonlocal calls
  calls+=1
  if time.time()-start>1800:raise TimeoutError('owned four-layer solve1800s cap; no scientific conclusion')
  return H(v)
 op=LinearOperator((dim,dim),matvec=mv,dtype=float);v0=np.sqrt(sizes.astype(float));v0/=np.linalg.norm(v0)
 ev,u=eigsh(op,k=min(5,dim-2),which='SA',tol=2e-11,ncv=min(18,dim),v0=v0,maxiter=1000)
 order=np.argsort(ev);ev=ev[order];u=u[:,order];g=u[:,0];g*=np.sign(g.sum());E=-diag/16;q=-(8/3)*(E-float(g@(E*g)))*g
 res=[float(np.linalg.norm(H(u[:,i])-ev[i]*u[:,i])) for i in range(len(ev))]
 out=dict(R=R,dimension=dim,full_dimension=len(ids),ground=float(ev[0]),ground_residual=res[0],source_norm2=float(q@q),symmetry_error=sym,peaks=[dict(gap=float(ev[i]-ev[0]),weight=float((u[:,i]@q)**2),residual=res[i]) for i in range(1,len(ev))],elapsed=time.time()-start,calls=calls,scope='Open-z fourlayer D4-invariant native coefficient model, not full microscopic spectrum; no thermodynamic conclusion')
 P=Path('/tmp/neutral_four_layer_openz');P.mkdir(exist_ok=True);(P/f'R{R}.json').write_text(json.dumps(out,indent=2)+'\n');np.savez(P/f'R{R}.npz',ev=ev,u=u,reps=reps,sizes=sizes,diag=diag,flips=flips)
 print(json.dumps(out),flush=True)
if __name__=='__main__':
 for R in map(int,sys.argv[1:] or [4,5]):run(R)
