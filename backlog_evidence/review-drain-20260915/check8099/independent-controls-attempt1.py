import sympy as s,json,time
from pathlib import Path
start=time.monotonic(); checks=[]
def ck(n,x):
 assert x,n
 checks.append(n)
X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1);I=s.eye(2);K=s.kronecker_product
# Exact four-band characteristic polynomial directly, independently of primary H^2 reduction.
a,b,c,d,u,v,w,E=s.symbols('a b c d u v w E',real=True)
H=K(I,w*Y+a*X+c*Z)+K(Z,b*X+d*Z)+K(X,u*X+v*Z)
S=w*w+a*a+b*b+c*c+d*d+u*u+v*v
U=(a*b+c*d)**2+(a*u+c*v)**2+(b*v-d*u)**2
ck('full_characteristic_polynomial',s.expand(H.charpoly(E).as_expr()-((E*E-S)**2-4*U))==0)
# Rational unit-circle substitution proves full complex determinant, no trig simplifier or source import.
t,z=s.symbols('t z',real=True); cb=s.Rational(3,5);sb=s.Rational(4,5);L=s.symbols('L',real=True)
Q=(L-t*cb-s.I*t*sb)*I+(-z*sb+s.I*z*cb)*Z+(v+s.I*u)*X
expr=s.expand(Q.det()-(L*L-2*L*t*(cb+s.I*sb)+(cb+s.I*sb)**2-(v+s.I*u)**2))
ck('qdet_unit_circle',s.rem(expr,s.Poly(z*z+t*t-1,z).as_expr(),z)==0)
# A rank-one Q root with exact rational node and mixing: derive projected dispersion via characteristic quadratic order.
# Aligned b with cos=3/5,sin=4/5, mu=3/5,R=4/5; xcos=12/25, zcos=9/10 (zeta=7/10).
R=s.Rational(4,5);mu=s.Rational(3,5);cx=s.Rational(12,25);sx=s.sqrt(1-cx*cx);cz=s.Rational(9,10);sz=s.sqrt(1-cz*cz)
qx=2*sx*R*(cb+s.I*sb);qz=2*(R-cx*cb-s.I*cx*sb)*sz;Delta2=4*(sb*sb+mu*mu*cb*cb)
ck('aligned_spectator',s.simplify(Delta2-4*sx*sx)==0)
ck('aligned_cross_zero',s.simplify(s.re(s.conjugate(qx)*qz))==0)
ck('aligned_xspeed',s.simplify(s.conjugate(qx)*qx/Delta2-R*R)==0)
ck('aligned_zspeed',s.simplify(s.conjugate(qz)*qz/Delta2-R*R*sb*sb*sz*sz/(sx*sx))==0)
ck('chirality_orientation',s.simplify(-s.im(s.conjugate(qx)*qz)/Delta2-4*sx*R*R*sb*sz/Delta2)==0)
# Fixed-momentum antiunitary and ordinary time reversal act differently.
J=K(I,Y);T=K(X,I)
ck('spectral_antisymmetry',s.simplify(J*s.conjugate(H)*J+H)==s.zeros(4))
ck('time_reversal_symbol',s.simplify(T*s.conjugate(H)*T-H.subs({b:-b,d:-d,w:-w},simultaneous=True))==s.zeros(4))
# Constant commutant of independent Fourier coefficients has exact complex nullity one.
coeff=[K(I,Y),K(I,Z),K(Z,cb*X-sb*Z),K(X,sb*X+cb*Z)]
B=[K(p,q) for p in [I,X,Y,Z] for q in [I,X,Y,Z]]
M=s.Matrix.hstack(*[s.Matrix.vstack(*[(C*A-A*C).reshape(16,1) for C in coeff]) for A in B])
ck('mixed_commutant_scalar',16-M.rank()==1)
ck('spinless_TRIM_rank',sum(s.conjugate(p)==-p for p in [X,Y,Z])==1)
print(json.dumps(dict(status='ok',count=len(checks),checks=checks,elapsed_seconds=time.monotonic()-start,primary_imported=False),indent=2))
