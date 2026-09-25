"""Read-only supplement verifier: no local source imports or writes."""
from collections import Counter
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;sha=lambda b:hashlib.sha256(b).hexdigest()
receipt=json.loads((HERE/'small_period.execution.json').read_text())
assert sha(Path(receipt['command'][1]).read_bytes())==receipt['source_sha256']
for stream in ['stdout','stderr']:
 b=(HERE/f'small_period.{stream}.txt').read_bytes();assert sha(b)==receipt[f'{stream}_sha256'] and len(b)==receipt[f'{stream}_bytes']
assert receipt['exit_code']==0 and receipt['stderr_bytes']==0
data=json.loads((HERE/'SMALL_PERIOD_RESULTS.json').read_text())
assert data['source_sha256']==receipt['source_sha256']
assert data['helper_sha256']==sha((HERE/'primitive_kernel.py').read_bytes())
steps=[tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in [-1,1]]
result=[]
for table in data['rows']:
 L=table['L'];vertices=list(product(range(L),repeat=3));B=[v for v in vertices if sum(v)%2==0]
 near=lambda x:{tuple((a+b)%L for a,b in zip(x,s)) for s in steps}
 pairs={tuple(sorted(pair)) for b in B for pair in combinations(near(b),2)}
 degree=len(near((0,0,0)));q0=0
 for a,c in pairs:
  r=len(near(a)&near(c));assert r>0;q0+=2*(degree*degree+r*r-2*r)
 assert q0==table['q0'] and degree==table['degree']
 assert sum(v for k,v in table['single_complete_column'])==table['single_algebraic_row_sum']
 rows=[dict(r) for r in table['matrix_rows']];w=table['relative_class_weights'];vec=table['positive_integer_vector'];ratios=[]
 shift=1-min(row.get(i,0) for i,row in enumerate(rows))
 for i,row in enumerate(rows):
  for j,value in row.items():
   assert value+(shift if i==j else 0)>=0 and w[i]*value==w[j]*rows[j].get(i,0)
  ratios.append(F(sum(value*vec[j] for j,value in row.items()),vec[i]))
 assert min(vec)>0
 assert [str(min(ratios)),str(max(ratios))]==table['exact_pair_increment_interval']
 assert max(ratios)<table['twice_single_row_sum']==2*table['single_algebraic_row_sum']
 result.append({'L':L,'q0':q0,'single_row':table['single_algebraic_row_sum'],'exact_pair_interval':table['exact_pair_increment_interval']})
print(json.dumps({'rows':result,'all_checks_completed':True,'source_imports_or_writes':False},indent=2))
