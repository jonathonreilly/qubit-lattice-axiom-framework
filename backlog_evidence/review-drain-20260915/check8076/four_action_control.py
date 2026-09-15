from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).parent;idx=json.loads((R/'8074-recovered-object-inventory.json').read_text());S=2**192;out=[];bind={}
def product(a,b):
 v=[x*y for x in a for y in b];return min(v)//S,(max(v)+S-1)//S
for o in range(5):
 p=f'native-sparse-pivot-action-run-4284/ORBIT_{o}/RESULT.json';x=next(x for x in idx if x['original_relative_path']==p);bind[p]=x['sha256'];d=json.loads((R/'forensic'/x['sha256']).read_text())
 for r in d['results']:
  T,G=r['T'],r['G'];n=len(T);L=[]
  for i in range(n):
   row=[]
   for j in range(n):
    terms=[product(T[i][k],T[k][j]) for k in range(n)];row.append([G[i][j][0]+sum(x[0] for x in terms),G[i][j][1]+sum(x[1] for x in terms)])
   L.append(row)
  for i in range(n):
   assert L[i][i][1]>=0;L[i][i][0]=max(0,L[i][i][0])
   for j in range(i+1,n):
    a=[max(L[i][j][0],L[j][i][0]),min(L[i][j][1],L[j][i][1])];assert a[0]<=a[1];L[i][j]=L[j][i]=a
  assert L==r['L'];lower=max(F(L[i][i][0],S) for i in range(n));upper=F(max(sum(max(abs(a),abs(b)) for a,b in row) for row in L),S)
  assert lower>F(3,10) and upper==F(r['delta_squared_upper_numerator'],r['denominator']) and lower<=upper
  out.append({'orbit':o,'impurity':r['impurity_bare_index'],'lower':str(lower),'upper':str(upper)})
(R/'four-action-control.json').write_text(json.dumps({'status':'PASS','results':out,'bindings':bind,'scope':'Independent exact interval G+T² reconstruction from original saved contractions; actual physical input/first contractions separate source obligations.'},indent=2)+'\n');print('PASS all ten four-pair action lower bounds')
