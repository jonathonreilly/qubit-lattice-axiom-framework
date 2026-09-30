"""Independent exact sphere integration and trace-elimination algebra; no candidate imports."""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import sympy as s, itertools, math, json
n=s.Matrix(s.symbols('n0:3'));v=s.symbols('v0:18');M=s.zeros(3)
for b,(i,j) in enumerate([(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]):M[i,j]=M[j,i]=sum(v[3*b+k]*n[k] for k in range(3))
def df(k):return math.prod(range(k,0,-2)) if k>0 else 1
def average(p):
 return s.expand(sum(c*s.Rational(math.prod(df(k-1) for k in powers),df(sum(powers)+1)) for powers,c in s.Poly(s.expand(p),*n).terms() if all(k%2==0 for k in powers)))
z=M*n;f=n.dot(z);h1=2*(z.dot(z)-f*f);tt=s.trace(M*M)-2*z.dot(z)+f*f-(s.trace(M)-f)**2/2
form=average(h1-tt/4);Q=s.hessian(form,v)/2;R=Q.copy();L=s.eye(18);D=[]
for k in range(18):
 d=R[k,k];assert d>=0
 if d==0:assert all(R[i,k]==0 for i in range(k,18));D.append(d);continue
 D.append(d)
 for i in range(k+1,18):L[i,k]=R[i,k]/d
 for i in range(k+1,18):
  for j in range(k+1,18):R[i,j]-=L[i,k]*d*L[j,k]
assert L*s.diag(*D)*L.T==Q and Q.rank()==sum(int(bool(d>0)) for d in D)
# A fixed nonzero trace column, arbitrary symbolic first moments: separate rational block calculation.
a=s.Matrix([1,2,3]);b=s.Matrix(3,2,s.symbols('b0:6'));q=s.symbols('q');AA=a.dot(a);P=s.eye(3)-a*a.T/AA
W=s.Matrix.hstack(a,q*b);V=W.T*W;Schur=V[1:,1:]-V[1:,0:1]*V[0:1,1:]/V[0,0]
assert s.simplify(Schur-q*q*b.T*P*b)==s.zeros(2) and P*P==P and P.T==P
# General trace-leading family a+q c: the leading q^2 Schur coefficient is the same constant projection.
c=s.Matrix(s.symbols('c0:3'));W=s.Matrix.hstack(a+q*c,q*b);V=W.T*W;S=V[1:,1:]-V[1:,0:1]*V[0:1,1:]/V[0,0]
assert all(s.simplify(s.limit(S[i,j]/q**2,q,0)-(b.T*P*b)[i,j])==0 for i in range(2) for j in range(2))
r={'verdict':'PASS','all_first_moments':18,'angular_bound':'<H1> >= <TT>/4','rational_LDL_pivots':[str(d) for d in D],'rank':Q.rank(),'trace_elimination':'q^2 B^* (I-aa^*/||a||^2) B + O(q^3); constant family projection preserves first-moment polynomial and quarter bound','scope':'Requires a finite positive Gram sum of local move amplitudes and a single gapped trace channel. Positivity of an arbitrary analytic quadratic form alone is not asserted to imply this representation.'}
print(json.dumps(r)); assert r['verdict']=='PASS'
