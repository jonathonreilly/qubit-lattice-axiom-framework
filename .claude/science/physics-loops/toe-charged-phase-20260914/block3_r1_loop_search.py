import numpy as np,random,time,json
from pathlib import Path
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]],complex);sz=np.diag([1,-1]);I=np.eye(4)
g=[np.kron(sx,s) for s in [sx,sy,sz]]+[np.kron(sy,np.eye(2))]
P={s*(i+1):(I-s*g[i])/2 for i in range(4) for s in [-1,1]}
rng=random.Random(914031);start=time.monotonic();count=0;valid=0
for n in [8,10,12,14,16,20,24,32]:
 for trial in range(40000):
  d=4 if trial%2 else 3
  axes=[rng.randrange(1,d+1) for _ in range(n//2)]
  word=axes+[-a for a in axes];rng.shuffle(word);x=[0]*d;seen={tuple(x)};ok=True
  for i,a in enumerate(word):
   x[abs(a)-1]+=1 if a>0 else -1
   if tuple(x) in seen and i!=n-1:ok=False;break
   seen.add(tuple(x))
  count+=1
  if not ok:continue
  valid+=1;T=I.copy()
  for a in word:T=T@P[a]
  tr=np.trace(T)
  if tr.real>0 and abs(tr.imag)<1e-14:
   out={'d':d,'length':n,'word':word,'trace':tr.real,'trials':count,'valid':valid,'seconds':time.monotonic()-start}
   Path('/tmp/toe-r1-loop-witness.json').write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True);raise SystemExit
 print({'length_finished':n,'trials':count,'valid':valid,'seconds':time.monotonic()-start},flush=True)
print('NO WITNESS IN THIS FINITE SEARCH',flush=True)
