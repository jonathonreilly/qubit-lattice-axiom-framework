from fractions import Fraction as F
import json
rows=[]
for L in range(2,16):
 n=L-1;full=(1<<n)-1;v=[F(0)]*(1<<n);v[0]=F(1)
 for S in range(1,full):
  c=(S & ~(S<<1)).bit_count();a=(S&1)+((S>>(n-1))&1)
  total=F(0);bits=S
  while bits:
   b=bits&-bits;bits-=b;total+=v[S^b]
  v[S]=total/(4*(2*c-a))
 A=sum(v[full^(1<<i)] for i in range(n))
 rows.append(dict(L=L,amplitude=str(A),scaled=str(A*2**(L-2))))
print(json.dumps(rows,indent=2))
