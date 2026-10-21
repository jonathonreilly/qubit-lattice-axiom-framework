import numpy as np,json
L=8;V=L*L;M=7;idx=lambda x,y:(x%L)*L+y%L
roots=np.zeros((V,2))
for d,(x,y) in enumerate([(1,0),(0,1)]):roots[idx(x,y),d]=roots[idx(-x,-y),d]=1/np.sqrt(2)
rows=[]
for b in [.1,.18,.23]:
 H=np.zeros((V,V))
 for x in range(L):
  for y in range(L):
   for dx,dy,v in [(1,0,-2),(-1,0,-2),(0,1,-2*b),(0,-1,-2*b)]:H[idx(x,y),idx(x+dx,y+dy)]+=v
 Hp=np.zeros((V-1+2*M,V-1+2*M));Hp[:V-1,:V-1]=H[1:,1:]
 for a,hop in enumerate([-2,2]):
  start=V-1+a*M;Hp[:V-1,start]=hop*roots[1:,a];Hp[start,:V-1]=Hp[:V-1,start]
  for j in range(M-1):Hp[start+j,start+j+1]=Hp[start+j+1,start+j]=hop
 f=np.array([-1,b]);source=np.zeros(len(Hp));source[:V-1]=roots[1:]@f
 for shift in [-.2,.3]:
  z=-4*(1+b)+shift+.13j;Gfree=np.linalg.inv(z*np.eye(V)-H);g=Gfree[0,0];r=roots.T@Gfree[:,0];G=roots.T@Gfree@roots-np.outer(r,r)/g
  sig=0j
  for _ in range(M):sig=4/(z-sig)
  direct=source@np.linalg.solve(z*np.eye(len(Hp))-Hp,source);T=np.linalg.inv(np.eye(2)/sig-G);formula=f@(T/sig**2-np.eye(2)/sig)@f
  rows.append(dict(b=b,shift=shift,error=float(abs(direct-formula))))
assert max(r['error'] for r in rows)<1e-10
print(json.dumps(dict(cases=rows,scope='Finite coefficient graph with physical ray signs, not many-qubit ED'),indent=2))
