import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
R=4;N=R*R
edges=[];plaq=[]
for x in range(R):
 for y in range(R):
  i=x*R+y;edges.extend([(i,((x+1)%R)*R+y,0),(i,x*R+(y+1)%R,1)])
  plaq.append(sum(1<<(((x+a)%R)*R+(y+b)%R) for a,b in [(0,0),(1,0),(0,1),(1,1)]))
def flat(s):return all((s&m).bit_count()%2==0 for m in plaq)
flatstates=[s for s in range(1<<N) if flat(s)]
assert len(flatstates)==1<<(2*R-1)
for s in flatstates:
 for i,j,_ in edges:assert not flat(s^(1<<i)^(1<<j))
rng=np.random.default_rng(1834);samples=flatstates[:8]+[int(x) for x in rng.integers(0,1<<N,size=32)]
rows=[]
for s in samples:
 H=np.zeros((N,N))
 for i,j,y in edges:
  sign=1 if not y else (-1 if ((s>>i)^(s>>j))&1 else 1)
  H[i,j]-=sign;H[j,i]-=sign
 ev=np.linalg.eigvalsh(H);assert ev[0]>=-4-1e-12
 assert (abs(ev[0]+4)<1e-10)==flat(s)
 if flat(s):
  v=np.array([(-1 if (s>>y)&1 else 1)/R for x in range(R) for y in range(R)])
  assert np.linalg.norm(H@v+4*v)<1e-12
 rows.append(dict(background=s,flat=flat(s),ground=float(ev[0])))
print(json.dumps(dict(flat_background_count=len(flatstates),flat_edge_flips_checked=len(flatstates)*len(edges),spectral_checks=rows,scope='Exact flat-flux classification control; not full higher-order heavy ground')))
