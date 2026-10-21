AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from math import comb
import json,time

def run(L):
 # columns 0=(0,0),1=(1,0),2=(0,1),3=(1,1)
 idx=lambda c,z:c*L+z%L
 ops=[]
 for z in range(1,L):ops.append(((1<<idx(0,z))|(1<<idx(1,z)),0,-1))
 for a,b,axis in [(0,2,'y'),(2,3,'x'),(3,1,'y')]:
  f=(1<<idx(a,0))|(1<<idx(b,0));ops.append((f,f if axis=='y' else 0,1 if axis=='y' else -1))
 n=len(ops);size=1<<n;masks=[0]*size;dp=[F(0)]*size;dp[0]=F(1);dprime=[F(0)]*size
 for s in range(1,size):
  bit=s&-s;j=bit.bit_length()-1;masks[s]=masks[s^bit]^ops[j][0]
  val=F(0);der=F(0)
  for j,(flip,phase,coef) in enumerate(ops):
   if s>>j&1:
    prev=s^(1<<j);sign=coef*(-1)**((masks[prev]&phase).bit_count());val+=dp[prev]*sign;der+=dprime[prev]*sign
  if s!=size-1:
   mask=masks[s];N=sum(((mask>>idx(c,z))^(mask>>idx(c,z+1)))&1 for c in range(4) for z in range(L))
   assert N>0
   val/=(-2*N);D2=sum(((mask>>idx(c,z))^(mask>>idx(c,z+2)))&1 for c in range(4) for z in range(L));der=der/(-2*N)+val*F(D2,N)
  dp[s]=val;dprime[s]=der
 g=F(comb(2*L-2,L-1),8**(L-1));a=dp[-1]
 return dict(L=L,per_layer=str(a),all_layers=str(L*a),ratio_to_gamma=str(L*a/g),gamma=str(g),marked_ratio=str(dprime[-1]/a),words=__import__('math').factorial(n))
start=time.monotonic();rows=[run(L) for L in [4,6,8,10,12]];print(json.dumps(dict(rows=rows,seconds=time.monotonic()-start),indent=2))
