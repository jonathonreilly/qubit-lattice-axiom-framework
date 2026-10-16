from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
checks=[]
for r in [F(k,24) for k in range(24)]:
  for ps in product([F(0),F(1,4),F(1,2),F(3,4),F(1)],repeat=4):
    a=r;b=1-r;total=0
    for p in ps:
      z0=int(a+p>=1);z1=int(b+1-p>1)
      assert z0+z1==1
      a+=p-z0;b+=1-p-z1;total+=z0
      assert 0<=a<1 and 0<b<=1 and a+b==1
    assert total==int(r+sum(ps)) and abs(total-sum(ps))<1
checks.append({'name':'counter sequences and ties','cases':24*5**4})
for r in [F(k,100) for k in range(100)]:
  a=r;bits=[]
  for _ in range(100):
    z=int(a+F(1,2)>=1);bits.append(z);a+=F(1,2)-z
  assert all(x!=y for x,y in zip(bits,bits[1:])) and sum(bits)==50
checks.append({'name':'all sampled residues alternate','cases':100,'scope':'general proof in derivation'})
# Direct enumeration of first retention over up to 120 underlying events;
# compare the series result with rigorous residual probability.
loss=[]
for a,b in product([F(1,5),F(1,2),F(1)],repeat=2):
  D=a+b-a*b;pred=[[a*(1-b)/D,b/D],[a/D,b*(1-a)/D]]
  for previous in (0,1):
    survival=F(1);prob=[F(0),F(0)]
    for k in range(1,121):
      port=(previous+k)%2; eta=[a,b][port]
      prob[port]+=survival*eta;survival*=1-eta
    assert all(0<=pred[previous][j]-prob[j]<=survival for j in (0,1))
  pi0=a/(a+b);eigen=1-pred[0][1]-pred[1][0]
  covariance=pi0*pred[0][0]-pi0*pi0
  assert covariance/(pi0*(1-pi0))==eigen==-a*b/D
  loss.append({'eta0':str(a),'eta1':str(b),'eigen':str(eigen)})
checks.append({'name':'direct retention sequence','parameters':loss})
Path(__file__).with_name('independent_results.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks))
