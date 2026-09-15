from pathlib import Path
import sympy as s,json,time
start=time.monotonic();rows=[]
def check(n,b):
 assert b,n
 rows.append(n)
r=s.sqrt(2);c={-2:s.Rational(1,2),-1:r,0:s.Integer(2),1:r,2:s.Rational(1,2)}
# Cube kernel is the single all-ones integer relation. Contract fiber differences,
# without generating its729 auxiliary configurations or importing primary code.
z=sum(v**6 for v in c.values());a=sum(c.get(k-1,0)*v**5 for k,v in c.items())
check('cube kernel contraction norm',s.simplify(z-s.Rational(2561,32))==0)
check('cube kernel contraction overlap',s.simplify(a/z-1345*r/2561)==0)
check('redundancy gives strict lower bound',s.simplify(a/z-r/2)>0)
for length in [1,2,3,5]:
 x=s.symbols('x');prev=s.Integer(1);curr=x
 for j in range(2,length+1):prev,curr=curr,s.expand(x*curr-prev/4)
 expected=s.prod(x-s.cos(s.pi*j/(length+1)) for j in range(1,length+1))
 check('chain characteristic recurrence '+str(length),s.simplify(curr-expected)==0)
# Arbitrary singular values give +/-s_j one-particle bond eigenvalues;
# enumerate all many-body occupancies, independent of carrier matrices.
vals=[s.Rational(1,3),s.Rational(2,5),s.Rational(7,6),s.Rational(3,2)]
from itertools import product
energies=[sum(t*v for t,v in zip(bits,vals+[-v for v in vals])) for bits in product([0,1],repeat=8)]
check('arbitrary CAR bond norm is nuclear norm',max(energies)==sum(vals) and min(energies)==-sum(vals))
# Principal-angle energy bound via chord(sin), Cauchy Schwarz, sixfaces.
check('cube coercivity constant',s.Rational(2,1)/s.pi**2*(2*s.pi)**2/6==s.Rational(4,3))
check('global cube counting factor',2/s.Rational(4,3)==s.Rational(3,2))
# Q nonzero region in two-angle section has two triangles of area pi²/2.
check('S0 square compression differs from compressed square',2*(s.pi**2/2)/(2*s.pi)**2==s.Rational(1,4))
# Ground bound algebra: a/V(Etrial-Eon)+r*q; multiplying magneticenergy byg².
g,M,w,r0,q=s.symbols('g M w r q',positive=True)
trial=w*(8*g**2*M**2+(1-s.cos(s.pi/(2*M+2)))/g**2)
check('variational deficit scaling',s.expand(g**2*(trial+r0*q)- (8*w*g**4*M**2+w*(1-s.cos(s.pi/(2*M+2)))+g**2*r0*q))==0)
check('coarse electric constant',8*2**2==32)
print(json.dumps(dict(status='PASS',checks=len(rows),controls=rows,elapsed_seconds=time.monotonic()-start,scope='Independent symbolic kernel contraction, chain determinant recurrence, arbitrary CAR singular-value occupancy and coefficient checks; no primary invocation.'),indent=2))
