"""Independently written flat pair-add/return paths and candidate supersolutions.

The optional one-occupied-B object is algebraic only, not a Gauss sector.
Convention: Q=-H4=2 times the overlapping-star Gram sum, parent Part I.
No imported program, artifact, matrix, fitted spectrum or root40 result.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations,product
from functools import lru_cache
from pathlib import Path
import hashlib,json,time
import numpy as np
from scipy.optimize import linprog

HERE=Path(__file__).resolve().parent
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
unit=tuple(tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in [-1,1])
@lru_cache(None)
def near(v):return tuple(plus(v,e) for e in unit)
@lru_cache(None)
def touching(x):
 pairs=set()
 for a in near(x):
  for b in near(a):
   for c in near(b):
    if c!=a:pairs.add(tuple(sorted((a,c))))
 return frozenset(pairs)
@lru_cache(None)
def outward_kernel(pair):
 a,c=pair
 return Counter(tuple(sorted((u,v))) for u in near(a) for v in near(c) if u!=v)

def gram_delta(occupied):
 """Apply 2 S* S directly on finite sets; subtract only affected vacuum rows."""
 occupied=tuple(sorted(occupied)); occ=set(occupied)
 relevant=set().union(*(touching(x) for x in occupied))
 column=Counter();vacuum=0;primitive=0
 for pair in sorted(relevant):
  kernel=outward_kernel(pair)
  vacuum+=2*sum(k*k for k in kernel.values())
  for addition,out_weight in kernel.items():
   if occ.intersection(addition):continue
   middle=occ.union(addition)
   for removal in combinations(sorted(middle),2):
    return_weight=kernel.get(removal,0)
    if return_weight:
     final=tuple(sorted(middle.difference(removal)))
     column[final]+=2*out_weight*return_weight;primitive+=1
 column[occupied]-=vacuum
 return {key:value for key,value in sorted(column.items()) if value},len(relevant),primitive

def typ(points):
 r=minus(points[1],points[0]);s=tuple(sorted(map(abs,r)))
 return 0 if s==(0,0,2) else 1 if s==(0,1,1) else None

def serialize(col):return [[list(map(list,key)),value] for key,value in col.items()]

start=time.perf_counter();origin=(0,0,0)
one,one_active,one_primitives=gram_delta((origin,))
single={key[0]:value for key,value in one.items()}
threshold=2*sum(single.values())
shells=[r for r in product(range(-6,7),repeat=3) if 0<sum(map(abs,r))<=6 and sum(r)%2==0]
# Cubic symmetry is used only to reduce the linear feasibility exploration;
# all oriented rows will later be retained if a certificate is found.
reps=sorted(set(tuple(sorted(map(abs,r))) for r in shells))
rows=[];bounds=[];coeffs=[]
for r in reps:
 col,nactive,nprimitive=gram_delta((origin,r));base=sum(col.values())-threshold
 response=[sum(value for key,value in col.items() if typ(key)==k)-threshold*int(typ((origin,r))==k) for k in [0,1]]
 rows.append({'displacement':r,'row_sum':sum(col.values()),'threshold_deficit':base,'h_responses':response,'active_pairs':nactive,'primitive_returns':nprimitive,'complete_delta_column':serialize(col)})
 coeffs.append(response);bounds.append(-base)
solution=linprog([0.,0.],A_ub=np.array(coeffs,dtype=float),b_ub=np.array(bounds,dtype=float),bounds=[(-.95,2),(-.95,2)],method='highs')
candidate=None
if solution.success:
 candidate=[str(Fraction(float(x)).limit_denominator(1000000)) for x in solution.x]
 values=[Fraction(x) for x in candidate]
 exact=[Fraction(row['threshold_deficit'])+sum(v*b for v,b in zip(values,row['h_responses'])) for row in rows]
 exact_feasible=max(exact)<=0 and min(1+x for x in values)>0
else:exact=[];exact_feasible=False
result={'scope':__doc__,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'single_algebraic_column':[[list(k),v] for k,v in single.items()],'single_row_sum':sum(single.values()),'single_active_pairs':one_active,'single_primitive_returns':one_primitives,'candidate_separated_upper_edge':threshold,
 'near_six_shell_representatives':rows,'linear_feasibility':{'success':bool(solution.success),'message':solution.message,'floating_x':solution.x.tolist() if solution.success else None,'rational_candidate':candidate,'exact_feasible':exact_feasible,'exact_residuals':[str(x) for x in exact]},
 'limits':'Exploration only. Finite support, all-volume extension and spectral interpretation require explicit proof. No root program used.','elapsed_seconds':time.perf_counter()-start}
with (HERE/'THRESHOLD_EXPLORATION.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
summary={k:v for k,v in result.items() if k!='near_six_shell_representatives'}
summary['representatives']=[{k:v for k,v in row.items() if k!='complete_delta_column'} for row in rows]
print(json.dumps(summary,indent=2))
