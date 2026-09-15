import sympy as s
from fractions import Fraction as F
from itertools import product
import json,time,signal
signal.alarm(30);start=time.monotonic()
# Single syndrome qubit gives exact universal Clifford scalar-effect identity.
X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);I=s.eye(2);P=(I+X)/2;c=s.sqrt(3)/2;q=s.Rational(1,2);U=c*I+q*Z*X
assert U.H*U==I
for z in (-1,1):
 Q=(I+z*Z)/2;K=Q*U
 assert s.simplify(P*K.H*K*P-(1+z*s.sqrt(3)/2)*P/2)==s.zeros(2)
# Independent exact parity marginal via generating products, five unequal modes.
nu=[F(1,4),F(3,8),F(1,2),F(5,8),F(3,4)];prob=F(0);means=[F(0)]*5
for bits in product((0,1),repeat=5):
 if sum(bits)%2:continue
 w=F(1)
 for n,b in zip(nu,bits):w*=n if b else 1-n
 prob+=w
 for j,b in enumerate(bits):means[j]+=b*w
prod=lambda xs:__import__('functools').reduce(lambda a,b:a*b,xs,F(1))
r=prod([1-2*x for x in nu]);assert prob==(1+r)/2
for j,n in enumerate(nu):
 expected=n-2*n*(1-n)*prod([1-2*v for k,v in enumerate(nu) if k!=j])/(1+r)
 assert means[j]/prob==expected and abs(expected-n)<=F(1,31)
# Current patch normalization and weakest half-margin exactly, independent of Fourier fixtures.
assert F(1,16*54)*F(1,4)==F(1,3456)
assert F(2,8192)**2<F(3,6912**2)<F(2,6912)**2
# Upper-front union/Chernoff optimization: minimize exp(lambda T)(gamma/(gamma+lambda))^n.
l,T,g,n=s.symbols('l T g n',positive=True)
f=l*T+n*s.log(g/(g+l));critical=n/T-g
assert s.simplify(s.diff(f,l).subs(l,critical))==0
assert s.simplify(s.diff(f,l,2).subs(l,critical))==T*T/n
print(json.dumps({'status':'passed','checks':['exact syndrome pulse scalar effects','five-mode rational even-parity marginals','current normalization and old-margin rejection','optimized exponential waiting-time bound'],'seconds':time.monotonic()-start},indent=2))
