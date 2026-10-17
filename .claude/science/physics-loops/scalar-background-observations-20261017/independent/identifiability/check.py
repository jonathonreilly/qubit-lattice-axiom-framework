"""Independent exact kinematic identifiability check; no action or observations."""
import json
from pathlib import Path
import sympy as s
z=s.symbols('z',real=True)
# Construct the geometry first, independently of the lifted matrix.
D=z+z**2
H=1/s.diff(D,z)
H0=H.subs(z,0)
v=H0-H/(1+z)
a=1/(1+z)
assert s.simplify((H*s.diff(D,z))**2-1)==0
assert v.subs(z,0)==0
assert all(H.subs(z,i)>0 for i in range(5))
# Metric exists locally by dt/dz = -1/((1+z)H); no stress tensor assumed.
dtdz=-1/((1+z)*H)
assert s.simplify(s.diff(a,z)/dtdz/a-H)==0
A=(1+z)**2*s.diff(D,z)**2
row=s.Matrix([[A,-2*A*v,-1,D**2]])
nodes=[1,2,3,4]
M=s.Matrix.vstack(*[row.subs(z,i) for i in nodes])
b=s.Matrix([-A.subs(z,i)*v.subs(z,i)**2 for i in nodes])
theta=M.inv()*b
assert M.det()==23712
assert theta==s.Matrix([1,1,1,0])
assert theta[0]==theta[1]**2
assert s.simplify(A*(theta[1]-v)**2-theta[2]+theta[3]*D**2)==0
# Unknown-clock scale degeneracy, using v_obs = gain * v_true.
g,h0,l,k,d,dp,vobs,zz=s.symbols('g h0 l k d dp vobs zz',nonzero=True)
raw=(1+zz)**2*dp**2*(h0-vobs/g)**2-l**-2+k*d**2
lam=s.symbols('lam',positive=True)
scaled=raw.subs({h0:lam*h0,l:l/lam,k:lam**2*k,g:g/lam}, simultaneous=True)
assert s.simplify(scaled-lam**2*raw)==0
# Constant distance record gain absorbed by L; H0 and k unchanged.
beta=s.symbols('beta',positive=True)
rescale=raw.subs({d:beta*d,dp:beta*dp,l:l/beta},simultaneous=True)
assert s.simplify(rescale-beta**2*raw)==0
result={'scope':'conditional FLRW kinematics; synthetic exact fixture', 'D':str(D),'H':str(H),'v':str(v),'dt_dz':str(dtdz),'nodes':nodes,'matrix':[[str(x) for x in M.row(i)] for i in range(4)],'rhs':[str(x) for x in b],'determinant':str(M.det()),'theta':[str(x) for x in theta],'all_assertions_pass':True}
Path('result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
