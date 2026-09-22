import json,time,signal
from fractions import Fraction as F
signal.alarm(30);t=time.monotonic();checks=[]
# Independent finite-difference identity: degree-eight dimension formula is fixed by nine values.
for R in range(12):
 n=R+2; closed=F(n*n*(n+1)**2*(n-1)*(n+2)*(3*n*n+3*n+2),2880)
 direct=sum(F((p+1)**2*(q+1)**2*(p+q+2)**2,4) for p in range(R+1) for q in range(R+1-p))
 assert closed==direct
 checks.append('dimension_R'+str(R))
# Distinct full-rank two-dimensional Q block verifies actual Schur congruence, not selected matrix element.
import sympy as s
K=s.diag(0,2,11,17);W=s.Matrix([[1,0,1,2],[0,1,2,-1],[1,1,0,1],[0,1,1,0]])
V=W.T*W;H=K+V;A=H[:2,:2];B=H[:2,2:];D=H[2:,2:]
for z in [s.Rational(-1),s.Rational(1,2),s.Rational(3),s.Rational(7)]:
 Q=D-z*s.eye(2);T=s.eye(4);T[2:,:2]=-Q.inv()*B.T
 assert T.T*(H-z*s.eye(4))*T==s.diag(A-z*s.eye(2)-B*Q.inv()*B.T,Q)
 checks.append('rank2Q_congruence_'+str(z))
# Quadratic endpoint equality for a generic exact scalar Schur envelope; no eigensolver.
for g,mu,b in [(11,3,2),(17,5,3),(19,0,0),(31,7,4)]:
 ell=(g+mu-s.sqrt((g-mu)**2+4*b*b))/2
 assert s.simplify((mu-ell)*(g-ell)-b*b)==0
 assert bool(ell<=mu)
 checks.append('endpoint_'+str((g,mu,b)))
print(json.dumps({'status':'PASS','checks':checks,'count':len(checks),'elapsed':time.monotonic()-t,'scope':'Independent exact dimension identity and rank-two excluded-block Schur congruence/endpoint controls; no primary imported or whole-cube diagonalization.'},indent=2))
