"""New finite-support supersolution search; all failures retained, not conclusions."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib,json,time
import numpy as np
from scipy.optimize import linprog
from primitive_kernel import column,relative_type
HERE=Path(__file__).resolve().parent
start=time.perf_counter();O=(0,0,0)
single={k[0]:v for k,v in column((O,)).items()};T=2*sum(single.values())
def types(R):return sorted({tuple(sorted(map(abs,r))) for r in product(range(R+1),repeat=3) if 0<sum(r)<=R and sum(r)%2==0})
near={r:column((O,r)) for r in types(4)}
all_runs=[]
for R in [4,6,8,10]:
 support=types(R);constraints=types(R+4);index={s:i for i,s in enumerate(support)}
 A=[];deficits=[];records=[]
 for r in constraints:
  if sum(r)<=4:
   col=near[r];row_sum=sum(col.values());response=[0]*len(support)
   for points,v in col.items():
    typ=relative_type(*points)
    if typ in index:response[index[typ]]+=v
  else:
   row_sum=T;response=[0]*len(support)
   for shift,v in single.items():
    q=tuple(a+b for a,b in zip(r,shift));typ=tuple(sorted(map(abs,q)))
    if typ in index:response[index[typ]]+=2*v
  if r in index:response[index[r]]-=T
  if not any(response) and row_sum==T:continue
  records.append({'separation':r,'deficit':row_sum-T,'response':response})
  A.append(response+[1]);deficits.append(T-row_sum)
 solution=linprog([0.]*len(support)+[-1.],A_ub=np.array(A,dtype=float),b_ub=np.array(deficits,dtype=float),bounds=[(-.9,.9)]*len(support)+[(None,None)],method='highs')
 run={'radius':R,'support_types':support,'constraints':records,'success':bool(solution.success),'message':solution.message}
 if solution.success:
  rational=[Fraction(float(x)).limit_denominator(100000) for x in solution.x[:-1]]
  residuals=[Fraction(row['deficit'])+sum(c*a for c,a in zip(rational,row['response'])) for row in records]
  run.update(floating_margin=float(solution.x[-1]),rational_corrections=[str(x) for x in rational],exact_residuals=[str(x) for x in residuals],exact_positive_h=min(1+x for x in rational)>0,exact_max_residual=str(max(residuals)),exact_feasible=max(residuals)<=0)
 all_runs.append(run)
 if solution.success and run['exact_feasible']:break
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256((HERE/'primitive_kernel.py').read_bytes()).hexdigest(),'runs':all_runs,'separated_threshold':T,'elapsed_seconds':time.perf_counter()-start,'scope':__doc__}
with (HERE/'SUPERSOLUTION_EXPLORATION.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({**result,'runs':[{k:v for k,v in r.items() if k not in ['constraints','exact_residuals']} for r in all_runs]},indent=2))
