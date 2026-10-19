import numpy as np,json
rng=np.random.default_rng(182525);R=17;C=5
s=rng.choice([-1.,1.],size=(C,R,R))
psi=rng.normal(size=(C,R,R))+1j*rng.normal(size=(C,R,R));psi/=np.linalg.norm(psi)
ux=np.ones_like(s);uy=s*np.roll(s,-1,axis=2)
P=s*np.roll(s,-1,axis=1)*np.roll(s,-1,axis=2)*np.roll(np.roll(s,-1,axis=1),-1,axis=2)
B=(1-P)/2
prob=abs(psi)**2
delta=float(np.sum(abs(psi-ux*np.roll(psi,-1,axis=1))**2)+np.sum(abs(psi-uy*np.roll(psi,-1,axis=2))**2))
S0=float(np.sum(B*prob));rows=[]
for dx in range(-3,4):
 for dy in range(-3,4):
  Bd=np.roll(np.roll(B,-dx,axis=1),-dy,axis=2);Sd=float(np.sum(Bd*prob));r=abs(dx)+abs(dy)
  bound=2*S0+2*r*r*delta
  assert Sd<=bound+1e-12
  # Explicit path transport: x then y, with unitary signs at each step.
  current=psi.copy()
  for _ in range(abs(dy)):
   current=uy*np.roll(current,-1,axis=2) if dy>0 else np.roll(uy,1,axis=2)*np.roll(current,1,axis=2)
  for _ in range(abs(dx)):
   current=np.roll(current,-1 if dx>0 else 1,axis=1)
  transport=float(np.sum(abs(psi-current)**2))
  assert transport<=r*r*delta+1e-11
  assert Sd<=2*S0+2*transport+1e-11
  rows.append(dict(dx=dx,dy=dy,Sd=Sd,transport=transport,bound=bound))
q=np.zeros_like(B);union_sum=np.zeros_like(B)
for dx in range(-2,3):
 for dy in range(-2,3):
  Bd=np.roll(np.roll(B,-dx,axis=1),-dy,axis=2);q=np.maximum(q,Bd);union_sum+=Bd
assert np.all(q<=union_sum)
print(json.dumps(dict(status='pass',background_components=C,R=R,delta=delta,S0=S0,displacements=rows,joint_failure=float(np.sum(prob*q)),union_bound=float(np.sum(prob*union_sum)),scope='Algebra controls for background-valued states; no empirical data or asymptotic constant certification')))
