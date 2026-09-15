from pathlib import Path
from fractions import Fraction as F
import json,hashlib
R=Path(__file__).parent; items=json.loads((R/'8076-recovered-object-inventory.json').read_text());S=2**256
results=[];bindings={}
for orbit in range(5):
 rows=[x for x in items if f'native-coordinate-free-run-prospective/ORBIT_{orbit}/' in x['original']]
 def get(suffix,imp=None):
  choices=[]
  for x in rows:
   if x['original'].endswith(suffix):
    d=json.loads((R/'forensic'/x['sha256']).read_text())
    if imp is None or d.get('impurity')==imp: choices.append((x,d))
  assert choices
  x,d=choices[0];bindings[x['original']]=x['sha256'];return d.get('data',d) if isinstance(d,dict) else d
 H=get('_H_raw.json')
 for i in range(len(H)):
  for j in range(i+1,len(H)):
   z=[max(H[i][j][0],H[j][i][0]),min(H[i][j][1],H[j][i][1])];assert z[0]<=z[1];H[i][j]=H[j][i]=z
 for imp in (399,400):
  N=get('_N_raw.json',imp);res=get('_result.json',imp);iv=get('_inverse_residual.json',imp)
  n=len(N)
  for i in range(n):
   for j in range(i+1,n):
    z=[max(N[i][j][0],N[j][i][0]),min(N[i][j][1],N[j][i][1])];assert z[0]<=z[1];N[i][j]=N[j][i]=z
  c=[[F(a+b,2*S) for a,b in row] for row in N]
  z=max(sum(F(b-a,2*S) for a,b in row) for row in N)
  e=F(max(max(sum(max(abs(a-(S if i==j else 0)),abs(b-(S if i==j else 0))) for j,(a,b) in enumerate(row)) for i,row in enumerate(H)),max(sum(max(abs(H[i][j][0]-(S if i==j else 0)),abs(H[i][j][1]-(S if i==j else 0))) for i in range(n)) for j in range(n))),S)
  assert e==F(res['e']) and 0<=e<1
  eps=F(iv['r'])/(1-e);q=z+F(iv['A_norm'])**2*eps
  upper=max(c[i][i]+sum(abs(c[i][j]) for j in range(n) if i!=j) for i in range(n))+q;upper/=1-e
  lower=max([F(0)]+[max(F(0),c[i][i]-q)/F(H[i][i][1],S) for i in range(n)])
  for k,v in [('delta_squared_upper',upper),('delta_squared_lower',lower),('matrix_radius',z),('combined_radius',q),('inverse_error',eps)]:assert F(res[k])==v,k
  assert lower>F(53,100) and lower<=upper
  results.append({'orbit':orbit,'impurity':imp,'lower':str(lower),'upper':str(upper)})
(R/'schur-control.json').write_text(json.dumps({'scope':'Independent exact scalar reconstruction from saved H and N interval matrices; original contractions and physical inputs remain separate source obligations. No historical worker executed.','results':results,'bindings':bindings},indent=2)+'\n')
print('PASS',len(results),'exact saved-stage Schur lower/upper/error reconstructions')
