"""Independent saved arithmetic control; no author modules/oracles invoked."""
import json,gzip,hashlib,signal,time
from pathlib import Path
from fractions import Fraction as Q
from math import factorial,comb
signal.alarm(30); start=time.monotonic(); checks=0
p=Path(__file__).parent/'original/outputs/native_certified_local_green_scalars_2026_09_09_inputs'
def ck(x):
 global checks
 assert x; checks+=1
class I:
 def __init__(self,x,y=None):
  self.l=Q(x);self.h=Q(x if y is None else y)
 def rounded(self):
  q=2**192
  return I((self.l*q).__floor__()/Q(q),(self.h*q).__ceil__()/Q(q))
 def __add__(a,b):
  b=asI(b);return I(a.l+b.l,a.h+b.h).rounded()
 def __neg__(a):return I(-a.h,-a.l)
 def __sub__(a,b):return a+-asI(b)
 def __mul__(a,b):
  b=asI(b);z=[x*y for x in (a.l,a.h) for y in (b.l,b.h)];return I(min(z),max(z)).rounded()
 def recip(a):
  ck(not a.l<=0<=a.h);return I(1/a.h,1/a.l).rounded()
 def ser(a):return [str(a.l),str(a.h)]
def asI(x):return x if isinstance(x,I) else I(x)
def interval(row,key):return I(*row[key])
data=gzip.decompress((p/'B_ORACLES.json.gz').read_bytes());oracle=json.loads(data)
ck(hashlib.sha256(data).hexdigest()==json.loads((p/'B_ORACLES_INDEX.json').read_text())['decompressed_sha256'])
ck(len(oracle)==746)
for row in oracle.values():
 for k,w in zip(('A','Aprime'),row['widths']):
  x=interval(row,k);ck(x.h-x.l==Q(w));ck(0<=Q(w)<=Q(1,10**30))
 ck(row['terms']==160)
rule=[(I(*x),I(*w)) for x,w in json.loads((p/'B_GAUSS.json').read_text())['rule']]
# Independent exact polynomial Legendre recurrence validates complete simple root brackets.
def leg(n,x):
 a,b=Q(1),x
 for j in range(2,n+1):a,b=b,((2*j-1)*x*b-(j-1)*a)/j
 return b
for i,(x,w) in enumerate(rule):
 ck(leg(12,x.l)*leg(12,x.h)<0);ck(w.l>0)
 if i:ck(rule[i-1][0].h<x.l)
# Positive weights/nodes enclose all moments through exactness degree23.
for n in range(24):
 total=I(0)
 for x,w in rule:
  powx=I(1)
  for _ in range(n):powx=powx*x
  total=total+w*powx
 v=Q(0) if n%2 else Q(2,n+1);ck(total.l<=v<=total.h)
result=json.loads((p/'B_RESULT.json').read_text()); sums={s:[I(0),I(0)] for s in (1,2)};index=2
for j,stored in zip(range(-28,3),result['panels']):
 panel={s:[I(0),I(0)] for s in (1,2)};a=Q(2)**j
 for x,w in rule:
  lo=a*(x.l+3)/2;hi=a*(x.h+3)/2
  rl=oracle[f'{index:04d}.json'];rh=oracle[f'{index+1:04d}.json'];index+=2
  ck(Q(rl['s'])==lo and Q(rh['s'])==hi)
  t=I(lo,hi);t2=t*t;at=I(rh['A'][0],rl['A'][1]);weight=w*I(a/2)
  for s in (1,2):
   r=oracle[f'{s-1:04d}.json'];A=interval(r,'A');D=interval(r,'Aprime');den=t2-I(s*s);num=t2*at-A*I(s*s)
   g=num*den.recip();h=((A*I(2*s)+D*I(s*s))*den-num*I(2*s))*(den*den).recip()
   for k,v in enumerate((g,h)):panel[s][k]=panel[s][k]+weight*v
 for s in (1,2):
  for k in (0,1):
   sums[s][k]=sums[s][k]+panel[s][k]
   ck(panel[s][k].ser()==stored['panel'][str(s)][k]);ck(sums[s][k].ser()==stored['cumulative'][str(s)][k])
ck(index==746)
def moment(n):
 return sum(Q(factorial(n)*comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b),factorial(a)*factorial(b)*factorial(n-a-b)) for a in range(n+1) for b in range(n-a+1))
def atan(x,n):
 v=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0));return (v,v+x**(2*n+1)/Q(2*n+1))
a,b=atan(Q(1,5),32),atan(Q(1,239),10);pi=(16*a[0]-4*b[1],16*a[1]-4*b[0]);factor=I(2/pi[1],2/pi[0]);radius=Q(1000,27)*Q(4,25)**12
for s,row in zip((1,2),result['rows']):
 r=oracle[f'{s-1:04d}.json'];A=interval(r,'A');D=interval(r,'Aprime');c=I(1)-A*I(s*s);e=A*I(2*s)+D*I(s*s);tails=[I(0),I(0)]
 for n in range(16):
  weight=I(Q((-1)**n,(2*n+1)*8**(2*n+1)));tails=[tails[0]+c*weight,tails[1]+e*weight]
  c,e=I(moment(n+1))-c*I(s*s),c*I(2*s)-e*I(s*s)
 rem=Q(12**16,33*8**33);tails=[tails[0]+I(0,rem),tails[1]+I(0,rem/Q(2*s))]
 for k,key in enumerate(('B','Bprime')):
  low=Q(1,2**28)*(Q(1,s*s) if k==0 else Q(2,s**3));v=(sums[s][k]+tails[k]+I(-radius,radius+low))*factor
  if k:v=-v
  ck(v.ser()==row[key])
# Distinct combinatorial recurrence, exact saved return reconstruction at all six prescribed cases.
R=json.loads((p/'return_RESULT.json').read_text());print('return row keys',R['rows'][0].keys())
print(json.dumps({'pass':True,'predicates':checks,'seconds':time.monotonic()-start,'scope':'All saved B panels/cumulatives/final bounds exactly reconstructed;746 source-bound oracle rows reused, no oracle/integral invoked;Gauss root/moment controls independent.'}))
