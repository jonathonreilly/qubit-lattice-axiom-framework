from fractions import Fraction as F
from math import comb, factorial
from collections import defaultdict
from pathlib import Path
import json,time,hashlib,signal
signal.alarm(60)
t=time.monotonic(); checks=[]
def ck(name,b):
 checks.append({'name':name,'pass':bool(b)})
 if not b:raise AssertionError(name)
# Dynamic spatial walk, independent of the closed form.
d={(0,0,0):1}; cs=[1]
for step in range(1,13):
 e=defaultdict(int)
 for p,v in d.items():
  for axis in range(3):
   for sign in [-1,1]:
    q=list(p);q[axis]+=sign;e[tuple(q)]+=v
 d=e
 if step%2==0:cs.append(d[(0,0,0)])
 else:ck('odd-return-'+str(step),d.get((0,0,0),0)==0)
# All 1001 return terms computed by integer ratio updates inside each row;
# no import of primary, no repeated binomial implementation or stored partial sums.
num=0;terms=[];central=1
for n in range(1001):
 if n:central=central*2*(2*n-1)//n
 term=central;total=term
 for a in range(n):
  m=n-a
  top=term*m*m*m
  bottom=(a+1)*(a+1)*2*(2*m-1)
  ck_div=(top%bottom==0)
  if not ck_div:raise AssertionError(('noninteger',n,a))
  term=top//bottom;total+=term
 count=central*total;terms.append(count)
 num=36*num+count
 if n<=6:ck('walk-count-'+str(n),count==cs[n])
 if n<=30:
  direct=sum(factorial(2*n)//(factorial(a)*factorial(b)*factorial(n-a-b))**2 for a in range(n+1) for b in range(n-a+1))
  ck('multinomial-'+str(n),count==direct)
S=F(num,36**1000);T2=F(225,14)*F(197,225)**1001;X=F(38,25)-S-T2;T1sq=F(36,11)**3/F(108000)
ck('S-lower',S>F(3,2));ck('upper-positive',X>0);ck('upper-square',X*X>T1sq)
ck('decimal',S.numerator*10**6//S.denominator==1501637);ck('denominator-digits',len(str(S.denominator))==1553)
ck('T2',T2<F(1,10**50));ck('T1',T1sq<F(181,10000)**2)
# Paired series identity and geometric residual, including negative phi.
for p in [F(-9,10),F(-1,2),F(0),F(1,2),F(9,10)]:
 partial=sum((1+p)*p**(2*m) for m in range(11))
 ck('paired-'+str(p),F(1)/(1-p)-partial==p**22/(1-p))
ck('exp-majorant',1-F(2,15)+F(2,225)==F(197,225))
result={'passed':len(checks),'failed':0,'elapsed_sec':time.monotonic()-t,'cap_seconds':60,'checks':checks,'S1000_numerator':str(S.numerator),'S1000_denominator':str(S.denominator),'margin_squared_positive':str(X*X-T1sq),'implementation':'independent spatial walk + integer row-ratio closed-count accumulation; no primary import/execution; exact rational tail comparison'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print({k:result[k] for k in ['passed','failed','elapsed_sec']})
