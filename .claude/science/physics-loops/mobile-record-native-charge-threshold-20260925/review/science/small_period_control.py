"""Small periods tested separately; no bulk threshold silently applied to them."""
from collections import Counter
from fractions import Fraction as F
from itertools import product,combinations
from pathlib import Path
import hashlib,json,math
import numpy as np
from primitive_kernel import column,neighbors,relative_type,add_kernel
HERE=Path(__file__).resolve().parent;O=(0,0,0);out=[]
for L in [2,4]:
 sites=list(product(range(L),repeat=3));B=[x for x in sites if sum(x)%2==0];A=[x for x in sites if sum(x)%2==1]
 pairs={tuple(sorted((a,c))) for b in B for a,c in combinations(neighbors(b,L),2)}
 q0=2*sum(sum(v*v for v in add_kernel(p,L).values()) for p in pairs)
 one=column((O,),L);single=sum(one.values())
 weights=Counter(relative_type(O,r,L) for r in B if r!=O);types=sorted(weights);ix={x:i for i,x in enumerate(types)};rows=[]
 for r in types:
  agg=Counter()
  for final,v in column((O,r),L).items():agg[ix[relative_type(*final,L)]]+=v
  rows.append(dict(agg))
 matrix=np.array([[rows[i].get(j,0)*math.sqrt(weights[types[i]]/weights[types[j]]) for j in range(len(types))] for i in range(len(types))])
 assert np.max(abs(matrix-matrix.T))<1e-10
 vals,vecs=np.linalg.eigh(matrix);v=vecs[:,-1]/np.sqrt([weights[t] for t in types])
 if sum(v)<0:v=-v
 integers=[round(float(x/max(v))*10**12) for x in v];assert min(integers)>0
 ratios=[F(sum(a*integers[j] for j,a in row.items()),integers[i]) for i,row in enumerate(rows)]
 out.append({'L':L,'degree':len(neighbors(O,L)),'n':len(B),'q0':q0,'single_algebraic_row_sum':single,'twice_single_row_sum':2*single,'single_complete_column':[[list(map(list,k)),v] for k,v in one.items()],'types':types,'relative_class_weights':[weights[t] for t in types],'matrix_rows':[[[j,v] for j,v in sorted(row.items()) if v] for row in rows],'positive_integer_vector':integers,'exact_pair_increment_interval':[str(min(ratios)),str(max(ratios))],'floating_pair_increment':float(vals[-1]),'interpretation':'No separated boxes of arbitrarily increasing size exist at this fixed tiny period. Twice the one-occupied-B algebraic row sum is recorded only as a finite algebraic comparison.'})
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256((HERE/'primitive_kernel.py').read_bytes()).hexdigest(),'rows':out}
with (HERE/'SMALL_PERIOD_RESULTS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
