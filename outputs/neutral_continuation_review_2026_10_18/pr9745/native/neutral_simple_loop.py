from fractions import Fraction as F
from math import factorial
import itertools,json

def coeff(colors):
 n=len(colors);masks=[(1<<j)|(1<<((j+1)%n)) for j in range(n)];states=[0]*(1<<n);dp=[F(0)]*(1<<n);dp[0]=F(1)
 for s in range(1,1<<n):
  l=s&-s;states[s]=states[s^l]^masks[l.bit_length()-1]
 for s in range((1<<n)-1):
  for j,t in enumerate(colors):
   if s>>j&1:continue
   ss=s|(1<<j);amp=(-1)**((states[s]&masks[j]).bit_count()) if t else -1
   val=dp[s]*amp
   if ss!=(1<<n)-1:val/=-states[ss].bit_count()
   dp[ss]+=val
 return dp[-1]
def closed(n,c):
 # c even; beta((c+1)/2,n-(c+1)/2)/pi using half-integer factorials.
 a=c//2;b=n-c//2-1
 beta=F(factorial(2*a)*factorial(2*b),4**(a+b)*factorial(a)*factorial(b)*factorial(n-1))
 return -(-1)**(c//2)*2**(n-1)*beta
if __name__=='__main__':
 rows=[]
 for n in [4,6,8]:
  checked=0;values={}
  for colors in itertools.product([0,1],repeat=n):
   c=sum(colors[j]!=colors[(j+1)%n] for j in range(n));got=coeff(colors);want=closed(n,c);assert got==want,(colors,got,want)
   checked+=1;values[c]=str(got)
  rows.append(dict(n=n,checked=checked,values=values));print(rows[-1],flush=True)
 open('/private/tmp/neutral_simple_loop.json','w').write(json.dumps(rows,indent=2)+'\n')
