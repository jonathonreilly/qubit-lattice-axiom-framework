import math,json,itertools
import mpmath as mp
mp.mp.dps=60
import numpy as np
from scipy.integrate import quad
# Independent probability and trace constants; direct 2x2 closed transition law.
z=math.exp(-2); heat=np.array([[(1+z)/2,(1-z)/2],[(1-z)/2,(1+z)/2]])
k=heat.copy();k[0,0]-=math.exp(-1)
v=np.linalg.eigvalsh(k);assert v[0]<0
# Cosine-well scaled coordinate integral avoids the program's f_a definitions.
m2=quad(lambda t:t*t*(1+math.cos(math.pi*t))/2,-1,1)[0]
norm=quad(lambda t:(1+math.cos(math.pi*t))/2,-1,1)[0]
assert abs(norm-1)<1e-14 and abs(m2-(1/3-2/math.pi**2))<1e-14
alpha=math.pi/3;c=2*math.sin(alpha/4)**2;T=alpha/(16*math.sqrt(2*c));C=3*math.pi**2/16+12*m2
rows=[]
for g in [.01,.004]:
 q=min(1,mp.exp(-T*c/g**2)+16*mp.exp(-alpha**2/(512*g**2*T)))
 eps=min(1,math.exp(C*T)*q**.25)
 qe=min(1,4*mp.exp(-alpha**2/(8*g**2*T)))
 epse=min(1,math.exp(C*T)*qe**.25)
 pj=min(1,6*max(eps,epse)**(1/24));pe=min(1,6*eps**(1/6))
 rows.append(dict(g=g,eps_exc=float(eps),magnetic_cluster=float(64*pe),current_cluster=float(196*pj)))
assert rows[0]['magnetic_cluster']<.39954 and rows[1]['current_cluster']<.02002
# Boundary of an elementary cube is assembled geometrically by ordered face deletion;
# build incidence matrices B1,B2,B3,B4 on the SINGLE four-cube, no torus or source coboundary.
cells={d:[] for d in range(5)}
for state in itertools.product((0,1,2),repeat=4):cells[state.count(2)].append(state)
B={}
for d in range(1,5):
 mat=np.zeros((len(cells[d-1]),len(cells[d])),dtype=int);idx={x:i for i,x in enumerate(cells[d-1])}
 for j,x in enumerate(cells[d]):
  varying=[i for i,a in enumerate(x) if a==2]
  for rank,axis in enumerate(varying):
   for end,sgn in [(0,-1),(1,1)]:
    y=list(x);y[axis]=end;mat[idx[tuple(y)],j]=sgn*(-1)**rank
 B[d]=mat
for d in (2,3,4):assert not np.any(B[d-1]@B[d])
rng=np.random.default_rng(165);a=rng.integers(-6,6,len(cells[1]));raw=B[2].T@a;flux=(raw+6)%12-6;sheet=(raw-flux)//12;charge=B[3].T@flux
assert np.all(charge%12==0) and np.array_equal(charge//12,-B[3].T@sheet)
assert not np.any(B[4].T@(charge//12))
# Limit x->0 via numerical Gaussian expectation instead of Fourier moment expression.
x=.007;fourth=quad(lambda w:abs(complex(math.cos(math.sqrt(x)*w),math.sin(math.sqrt(x)*w))-1)**4*math.exp(-w*w/2)/math.sqrt(2*math.pi),-10,10)[0]
assert fourth<12*x*x
print(json.dumps(dict(two_state_eigenvalues=v.tolist(),trial_second_moment=m2,T=T,C0=C,bounds=rows,cube_cells={d:len(v) for d,v in cells.items()},nonzero_cube_currents=int(np.count_nonzero(charge)),Gaussian_chord_fourth=fourth,Gaussian_chord_ratio=fourth/x**2),indent=2))
