from collections import Counter
import numpy as np,json
from scipy.linalg import eigh

def build(R):
 assert R>=8 and R%2==0
 shapes=[(a,b) for a in range(1,R//2+1) for b in range(1,R//2+1) if a*b%2==0];lookup={s:i for i,s in enumerate(shapes)}
 sizes=np.array([(R if a<R//2 else R//2)*(R if b<R//2 else R//2) for a,b in shapes])
 H=np.diag([-8/7 if a==1 or b==1 else 0 for a,b in shapes]).astype(float)
 for i,(a,b) in enumerate(shapes):
  f={(0,0),(a,0),(0,b),(a,b)};cand=set()
  for x,y in f:
   for u in [x-1,x+1]:
    for v in [y,y+1]:cand.add(('x',u%R,v%R))
   for u in [x,x+1]:
    for v in [y-1,y+1]:cand.add(('y',u%R,v%R))
  counts=Counter()
  for axis,u,v in cand:
   if axis=='x':g={((u+d)%R,(v+e)%R) for d in [-1,1] for e in [-1,0]}
   else:g={((u+d)%R,(v+e)%R) for d in [-1,0] for e in [-1,1]}
   out=f^g
   if len(out)!=4:continue
   xs=sorted({x for x,y in out});ys=sorted({y for x,y in out});assert len(xs)==len(ys)==2
   da=xs[1]-xs[0];db=ys[1]-ys[0];s=(min(da,R-da),min(db,R-db));assert s in lookup
   counts[lookup[s]]+=1
  for j,k in counts.items():H[j,i]-=k/2*np.sqrt(sizes[i]/sizes[j])
 assert np.max(abs(H-H.T))<1e-12
 source=np.zeros(len(shapes));source[lookup[2,1]]=source[lookup[1,2]]=1
 reached=set(np.flatnonzero(source));todo=list(reached)
 while todo:
  i=todo.pop()
  for j in np.flatnonzero(H[:,i]):
   if j not in reached:reached.add(j);todo.append(j)
 ii=sorted(reached);return H[np.ix_(ii,ii)],source[ii],[shapes[i] for i in ii]
if __name__=='__main__':
 rows=[]
 for R in [8,10,12,16,20,24,32,48,64,80,120]:
  H,q,s=build(R);e,v=eigh(H);rows.append(dict(R=R,dim=len(s),upper=e[-1],next=e[-2],weight=float((q@v[:,-1])**2),min=e[0]))
 print(json.dumps(rows,indent=2))
