from fractions import Fraction as F
from math import comb
import time,json
from pathlib import Path
start=time.monotonic();checks=[]
def ck(v,n):
 if not v:raise AssertionError(n)
 checks.append(n)
# Laurent constant terms from repeated multiplication by 6-sum(z_j+z_j^-1), independent of multinomial moment formula.
p={(0,0,0):1};mm=[1]
for k in range(1,5):
 out={}
 for site,c in p.items():
  out[site]=out.get(site,0)+6*c
  for axis in range(3):
   for step in (-1,1):
    s=list(site);s[axis]+=step;s=tuple(s);out[s]=out.get(s,0)-c
 p=out;mm.append(p[(0,0,0)])
ck(mm==[1,6,42,324,2682],'Laurent constant-term normalization through degree4')
ck(F(3,2)**2-F(17,16)**2-F(15,16)**2==F(31,128)>0,'whole ellipse strict right cone')
ck([F(16,3)*8*m for m in (F(17,60),F(1),F(6))]==[F(544,45),F(128,3),F(256)],'three Gauss polynomial-approximation radii')
# Positive discrete measure, distinct from original single atoms; all rational identities and low bounds.
atoms=[(F(1,10),F(2,7)),(F(7,3),F(3,7)),(F(11),F(2,7))]
for q in (0,1,2):
 for t in (F(7),F(13)):
  exact=sum(w*x**q/(x+t*t) for x,w in atoms)
  partial=sum((-1)**n*sum(w*x**(n+q) for x,w in atoms)/t**(2*n+2) for n in range(4))
  rem=sum(w*x**(4+q)/(t**8*(x+t*t)) for x,w in atoms)
  ck(exact==partial+rem and rem>0,'positive mixed-measure remainder q%d t%s'%(q,t))
ck(F(1,12)+F(1,54)+2<3,'derivative envelope using pi>3')
ck(F(13000*2**20,2**192)*2<F(1,10**45),'outward two-endpoint roundoff allowance')
# Negative non-dyadic arithmetic enclosure independently uses integer quotient/remainder.
S=2**192
for x in (F(-31,17),F(7,23)):
 q,rem=divmod(x.numerator*S,x.denominator);ck(F(q,S)<=x<=F(q+(rem!=0),S),'directed rounding '+str(x))
r=dict(pass_count=len(checks),controls=checks,elapsed_seconds=time.monotonic()-start,scope='Tiny synthetic measure and degree<=4 Laurent controls; no catalog, M0..M41 production, primary or saved-node replay.');Path(__file__).with_name('independent-controls-result.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
