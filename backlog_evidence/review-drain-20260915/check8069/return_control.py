from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,signal,time
signal.alarm(30);t=time.monotonic();p=Path(__file__).parent/'original/outputs/native_certified_local_green_scalars_2026_09_09_inputs';rows=json.loads((p/'return_RESULT.json').read_text())['rows'];c=[];count=0
for n in range(max(r['terms'] for r in rows)):
 term=comb(2*n,n)**2;total=term
 for j in range(n):
  a=term*(n-j)**4;b=(j+1)**2*(2*n-2*j)*(2*n-2*j-1);assert a%b==0;term=a//b;total+=term;count+=1
 c.append(total)
for row in rows:
 s=F(row['s']);q=s*s+6;m=row['terms'];r=36/q**2;a=d=F(0)
 for n in reversed(range(m)):a=(a+c[n])/q**2;d=(d+(2*n+1)*c[n])/q**2
 a*=q;d*=2*s
 ta=r**m/q/(1-r);td=2*s*r**m/q**2*((2*m+1)-(2*m-1)*r)/(1-r)**2
 assert list(map(F,row['A']))==[a,a+ta];assert list(map(F,row['Aprime']))==[-d-td,-d];count+=2
print(json.dumps({'pass':True,'checks':count,'seconds':time.monotonic()-t,'rows':len(rows),'max_coefficients':len(c),'scope':'All six saved exact return intervals reconstructed with distinct coefficient recurrence and reverse Horner; no author evaluator or new parameter.'}))
