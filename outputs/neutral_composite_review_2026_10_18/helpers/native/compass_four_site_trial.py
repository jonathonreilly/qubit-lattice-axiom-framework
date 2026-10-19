"""Physical 16-dimensional block-state check, no projected dynamics."""
import numpy as np,json
from fractions import Fraction as F
from pathlib import Path
I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]);axes=[X,Y,Z]
s=8/33;t=1/4;th=np.arcsin(s)/2;eta=np.arcsin(t)/2
v=np.array([np.cos(th),np.sin(th)])
# logical tA,tB are independent; parity rA,rB has +YY correlation t.
r=np.array([[np.cos(eta),0],[0,-np.sin(eta)]])
psi=np.zeros(16)
for a in range(2):
 for b in range(2):
  for p in range(2):
   for q in range(2):
    bits=[a,a^p,b,b^q];idx=sum(bit<<(3-i) for i,bit in enumerate(bits))
    psi[idx]=v[a]*v[b]*r[p,q]
assert abs(np.linalg.norm(psi)-1)<1e-14
ops={}
for i in range(4):
 for a in range(3):
  op=np.array([[1.]])
  for j in range(4):op=np.kron(op,axes[a] if i==j else I)
  ops[i,a]=op
means={(i,a):np.vdot(psi,op@psi).real for (i,a),op in ops.items()}
def corr(i,j,a):return np.vdot(psi,ops[i,a]@ops[j,a]@psi).real
# Periodically tile 2x2x1 blocks; internal bonds evaluated jointly,
# boundary bonds factor across distinct blocks. z always joins blocks.
sum_bonds=corr(0,1,0)+corr(2,3,0)+means[1,0]*means[0,0]+means[3,0]*means[2,0]
sum_bonds+=corr(0,2,1)+corr(1,3,1)+means[2,1]*means[0,1]+means[3,1]*means[1,1]
sum_bonds+=sum(means[i,2]**2 for i in range(4))
value=-sum_bonds/4;target=-F(1153,1056)
assert abs(value-float(target))<1e-13
out=dict(energy_per_site_over_J=value,exact_formula=str(target),s=str(F(8,33)),t=str(F(1,4)),one_site_Z=[means[i,2] for i in range(4)],norm=float(np.linalg.norm(psi)),scope='Variational upper bound from four-physical-site pure block product, no ground-state or scalar claim')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
