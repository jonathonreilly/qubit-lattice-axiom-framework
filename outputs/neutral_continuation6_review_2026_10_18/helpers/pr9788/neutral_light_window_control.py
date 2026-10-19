from math import comb
import numpy as np,json
from itertools import product

def edge_masks(R):
 return [(x,y,a,(1<<(x*R+y))^(1<<(((x+1)%R)*R+y)) if a==0 else (1<<(x*R+y))^(1<<(x*R+(y+1)%R))) for x in range(R) for y in range(R) for a in range(2)]
def plaquettes(s,R):
 return [(x,y) for x in range(R) for y in range(R) if sum((s>>(((x+dx)%R)*R+(y+dy)%R))&1 for dx,dy in product([0,1],repeat=2))%2]
rows=[]
for R in [6,8]:
 edges=edge_masks(R);refs=[]
 choices=range(1<<(2*R-1)) if R==6 else np.random.default_rng(1819).choice(1<<(2*R-1),256,replace=False)
 for label in choices:
  label=int(label);s=sum(((((label>>x)&1)^((label>>(R+y-1))&1 if y else 0)))<<(x*R+y) for x in range(R) for y in range(R))
  assert not plaquettes(s,R);refs.append(s)
 outputs={}
 for j,s in enumerate(refs):
  for x,y,a,m in edges:
   out=s^m
   assert out not in outputs
   outputs[out]=(j,a)
   # Background parity is all positive, so checking mask suffices for all refs.
 for x,y,a,m in edges:assert len(plaquettes(m,R))==4
 rows.append(dict(R=R,ground_references=len(refs),orthogonal_edge_outputs=len(outputs)))
# Exact Fourier coefficient obtained from explicit bad plaquettes versus formula.
R=14;L=6;V=R*R*L;A=6*(L-1)*(L-2)/(2*L-3);err=0.
corner_cache={m:plaquettes(m,R) for x,y,a,m in edge_masks(R)}
for nx,ny in product(range(R),repeat=2):
 q=np.array([2*np.pi*nx/R,2*np.pi*ny/R])
 for x,y,a,m in edge_masks(R):
  center=np.array([x,y],float);center[a]+=.5
  corners=corner_cache[m]
  direct_static=.25*np.cos(q[0]/2)*np.cos(q[1]/2)*sum(np.exp(-1j*q@np.array([px+.5,py+.5])) for px,py in corners)
  expected=np.exp(-1j*q@center)*np.cos(q[a]/2)*np.cos(q[a])*np.cos(q[1-a]/2)**2
  err=max(err,abs(direct_static-expected))
assert err<1e-13
# Derived bright two-cluster matrix checks mixing subtraction only, not full H.
bright=[]
for L in [6,8]:
 R=2*L+2;V=R*R*L;A=6*(L-1)*(L-2)/(2*L-3)
 for lam in [.4,.3,.2]:
  gam=lam**L*comb(2*L-2,L-1)/8**(L-1);delta=L*lam**4/16;k=-gam*np.sqrt(2*R*R)
  a=3/np.sqrt(V);b=A/(2*np.sqrt(V))
  H=np.array([[0.,k],[k,delta]]);C=np.array([[0.,b*k],[b*k,a*delta]])
  ev,u=np.linalg.eigh(H);actual=abs(u[:,1]@C@u[:,0])**2;pred=((b-a)*k)**2
  bright.append(dict(L=L,lam=lam,weight_ratio=actual/pred,gap_over_delta=(ev[1]-ev[0])/delta))
 assert abs(bright[-1]['weight_ratio']-1)<abs(bright[-3]['weight_ratio']-1)
print(json.dumps(dict(edge_gram=rows,max_fourier_error=err,bright_mixing=bright,scope='Exact discrete geometry/Fourier controls and derived two-cluster algebra; no full microscopic eigenvalue calculation'),indent=2))
