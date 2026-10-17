import json
from pathlib import Path
import sympy as s
z=s.symbols('z')
d=(z+z*z)/2
v=1-1/((1+z)*(1+2*z))
A=(1+z)**2*s.diff(d,z)**2
nodes=[s.Rational(i,4) for i in range(1,5)]
M=s.Matrix([[A.subs(z,i),(-2*A*v).subs(z,i),-1,(d*d).subs(z,i)] for i in nodes])
b=s.Matrix([(-A*v*v).subs(z,i) for i in nodes])
assert M.det()==s.Rational(33,4096)
assert M.inv()*b==s.Matrix([1,1,s.Rational(1,4),0])
# Flat constant H=1, D=d=z,L=1. Rank3 but unique physical solution.
d=z; v=z/(1+z); A=(1+z)**2
N=s.Matrix([[A.subs(z,i),(-2*A*v).subs(z,i),-1,(d*d).subs(z,i)] for i in nodes])
c=s.Matrix([(-A*v*v).subs(z,i) for i in nodes])
assert N.rank()==3
h0,c0,k=s.symbols('h0 c0 k')
pol=s.Poly(s.expand(A*h0*h0-2*z*(1+z)*h0-c0+k*z*z+z*z),z)
sol=s.solve(pol.all_coeffs(),[h0,c0,k],dict=True)
assert sol==[{c0:0,h0:0,k:-1},{c0:1,h0:1,k:0}]
res={'root_fixture_determinant':str(M.det()),'root_fixture_theta':[str(x) for x in M.inv()*b],'constant_H_rank':N.rank(),'constant_H_lift_nullspace':[[str(x) for x in n] for n in N.nullspace()],'constant_H_nonlinear_solutions':[{str(k):str(v) for k,v in x.items()} for x in sol],'physical_unique':'H0=1,L^-2=1,k=0; H0=0 solution excluded by L^-2>0','all_assertions_pass':True}
Path('followup_result.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
