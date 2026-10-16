import sympy as s,json
from pathlib import Path
K=s.Matrix([[4,-1,0],[-1,5,-1],[0,-1,6]]);O=s.diag(1,s.eye(2));O[1:,1:]=s.Matrix([[s.Rational(3,5),s.Rational(-4,5)],[s.Rational(4,5),s.Rational(3,5)]])
P=O*K*O.T;expected=s.Matrix([[4,-s.Rational(3,5),-s.Rational(4,5)],[-s.Rational(3,5),s.Rational(33,5),-s.Rational(1,5)],[-s.Rational(4,5),-s.Rational(1,5),s.Rational(22,5)]])
assert P==expected
w=s.symbols('w');assert s.simplify((w*s.eye(3)+K).inv()[0,0]-(w*s.eye(3)+P).inv()[0,0])==0
H,J=s.symbols('H J');ts=s.symbols('t1:4');ds=[t*H/(1+t*J) for t in ts]
def residual(t,d):
 a,b,c=t;x,y,z=d
 return b*(c-a)*x*z-c*(b-a)*x*y+a*(b-c)*y*z
assert s.factor(residual(ts,ds))==0
# Fully correlated complex measurement shifts with a shared baseline error.
theta=[s.Rational(1,3),s.Rational(2,3),s.Rational(4,3)]
A=K+(1+s.I)**2*s.eye(3);r=A.inv();b=s.Matrix([1,0,0]);c=s.Matrix([0,0,1]);direction=s.Matrix([1,-1,0])
delta=[s.simplify((c.T*(r-(A+t*direction*direction.T).inv())*b)[0]) for t in theta]
assert s.simplify(residual(theta,delta))==0
err=(1+2*s.I)/100;d=[x+err for x in delta];epsilon=abs(complex(err));dn=[complex(x) for x in d];coeff=[abs(float(theta[1]*(theta[2]-theta[0]))),abs(float(theta[2]*(theta[1]-theta[0]))),abs(float(theta[0]*(theta[1]-theta[2])))]
pairs=[(0,2),(0,1),(1,2)];bound=sum(cf*(epsilon*abs(dn[j])+epsilon*abs(dn[i])+epsilon**2) for cf,(i,j) in zip(coeff,pairs));observed=abs(complex(residual(theta,d)))
assert observed<=bound
result={'transformed_stiffness':str(P),'row_sums':[str(sum(P[i,j] for j in range(3))) for i in range(3)],'boundary_resolvent_identity':True,'three_point_identity':True,'complex_correlated_error':{'residual':observed,'certificate':bound}}
Path(__file__).with_name('independent_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
