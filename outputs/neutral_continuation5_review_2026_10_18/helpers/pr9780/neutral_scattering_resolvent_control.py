import numpy as np,json
L=10;V=L*L;b=.18;M=8;z=-4*(1+b)+.2+.07j
idx=lambda x,y:(x%L)*L+y%L
H=np.zeros((V,V))
for x in range(L):
 for y in range(L):
  for dx,dy,v in [(1,0,-2),(-1,0,-2),(0,1,-2*b),(0,-1,-2*b)]:H[idx(x,y),idx(x+dx,y+dy)]+=v
G=np.linalg.inv(z*np.eye(V)-H);roots=np.zeros((V,2))
for d,(x,y) in enumerate([(1,0),(0,1)]):roots[idx(x,y),d]=roots[idx(-x,-y),d]=1/np.sqrt(2)
g=G[0,0];r=roots.T@G[:,0];cavity=roots.T@G@roots-np.outer(r,r)/g
sigma=0j
for _ in range(M):sigma=4/(z-sigma)
T=np.linalg.inv(np.eye(2)/sigma-cavity)
Hp=np.zeros((V-1+2*M,V-1+2*M));Hp[:V-1,:V-1]=H[1:,1:]
for a in range(2):
 start=V-1+a*M
 Hp[:V-1,start]=-2*roots[1:,a];Hp[start,:V-1]=Hp[:V-1,start]
 for j in range(M-1):Hp[start+j,start+j+1]=Hp[start+j+1,start+j]=-2
R=np.linalg.inv(z*np.eye(len(Hp))-Hp);errs=[]
ks=[(0,0),(1,0),(0,1)]
for ka in ks:
 for kb in ks:
  def wave(k):return np.array([np.exp(2j*np.pi*(k[0]*x+k[1]*y)/L)/np.sqrt(V) for x in range(L) for y in range(L)])
  pa,pb=wave(ka),wave(kb);ea=-4*np.cos(2*np.pi*ka[0]/L)-4*b*np.cos(2*np.pi*ka[1]/L);eb=-4*np.cos(2*np.pi*kb[0]/L)-4*b*np.cos(2*np.pi*kb[1]/L)
  direct=V*(z-ea)*(z-eb)*(pa[1:].conj()@R[:V-1,:V-1]@pb[1:]-(1/(z-ea) if ka==kb else 0))
  ha=np.sqrt(V)*(roots.T@pa-r*pa[0]/g);hb=np.sqrt(V)*(roots.T@pb-r*pb[0]/g)
  exact=-1/g+ha.T@T@hb
  errs.append(float(abs(direct-exact)))
assert max(errs)<1e-10,errs
print(json.dumps(dict(cases=len(errs),max_error=max(errs),scope='Finite coefficient graph resolvent identity; 100 host sites and two length8 rays, not physical-spin ED'),indent=2))
