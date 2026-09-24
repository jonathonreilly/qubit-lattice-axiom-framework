#!/usr/bin/env python3

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/residue_polynomial_check.py', 'scripts/core_derivation.py')
from collections import defaultdict
from fractions import Fraction
import importlib.util,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('core',HERE/'core_derivation.py');core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
radius=80;nodes=core.walk_nodes(radius);inv={v:k for k,v in nodes.items()}
def dentry(n,m):
 row=defaultdict(Fraction)
 for target,_h2,d,_data in core.two_hop_paths(nodes[n]):
  row[inv[target]]+=d
 return row[m]
def poly(vals):
 y0,y1,y2=vals
 A=(y2-2*y1+y0)/2
 B=y1-y0-A
 C=y0
 return [A,B,C]
rows=[]
for r in range(15):
 row={}
 for kind,offset in [('diag',0),('right',1)]:
  vals=[dentry(r+15*k,r+15*k+offset) for k in range(4)]
  coeff=poly(vals[:3]);pred=sum(coeff[j]*9 for j in range(0))
  predicted=coeff[0]*9+coeff[1]*3+coeff[2]
  assert predicted==vals[3],(r,kind,vals,coeff,predicted)
  # k=-1 is also represented in the generated route.
  minus=dentry(r-15,r-15+offset)
  predminus=coeff[0]-coeff[1]+coeff[2]
  assert predminus==minus,(r,kind,minus,coeff,predminus)
  row[kind]={'quadratic_k2_k_const':[str(v) for v in coeff], 'samples_k0_to3':[str(v) for v in vals], 'sample_k_minus1':str(minus)}
 rows.append({'n_mod_15':r,**row})
# Convert the Jacobi matrix to a weighted path Laplacian by the unitary
# gauge (-1)^n.  The residual potential is diagonal minus adjacent weights.
def evalpoly(coeff,k): return coeff[0]*k*k+coeff[1]*k+coeff[2]
rem_rows=[]
for r,row in enumerate(rows):
 diag=[Fraction(x) for x in row['diag']['quadratic_k2_k_const']]
 right=[Fraction(x) for x in row['right']['quadratic_k2_k_const']]
 if r>0:
  left=[Fraction(x) for x in rows[r-1]['right']['quadratic_k2_k_const']]
 else:
  prev=[Fraction(x) for x in rows[14]['right']['quadratic_k2_k_const']]
  # w_(15k-1) is row 14 at cycle index k-1.
  left=[prev[0],-2*prev[0]+prev[1],prev[0]-prev[1]+prev[2]]
 vals=[]
 for k in (-1,0,1,2,3):
  vals.append(evalpoly(diag,k)-evalpoly(right,k)-evalpoly(left,k))
 coeff=poly(vals[1:4])
 assert coeff[0]==0,(r,vals,coeff)
 predicted=evalpoly(coeff,-1);assert predicted==vals[0]
 predicted=evalpoly(coeff,3);assert predicted==vals[4]
 rem_rows.append({'n_mod_15':r,'remainder_alpha_k_plus_beta':[str(coeff[1]),str(coeff[2])], 'samples_k_minus1_to3':[str(x) for x in vals]})
alpha_sum=sum(Fraction(row['remainder_alpha_k_plus_beta'][0]) for row in rem_rows)
beta_sum=sum(Fraction(row['remainder_alpha_k_plus_beta'][1]) for row in rem_rows)
assert alpha_sum==0 and beta_sum==3
for row in rows:
 A,B,C=[Fraction(x) for x in row['right']['quadratic_k2_k_const']]
 # Convexity reduces global integer nonnegativity to the integers nearest
 # the vertex; check a certified bracket and the claimed |k|>=3 bound.
 vertex=-B/(2*A); base=vertex.numerator//vertex.denominator
 assert min(A*k*k+B*k+C for k in (base-1,base,base+1,base+2))>=0
 assert all(A*k*k+B*k+C>=k*k for k in (-3,3))
 assert A==9 and abs(B)<=21
 # For f(k)=w(k)-k^2, the discrete outward differences are positive
 # beyond |k|>=3, so the exact checks at both endpoints prove the tails.
 assert 2*(A-1)*3+(A-1)+B>0
 assert 2*(A-1)*3-(A-1)-B>0
out={'status':'exact rational path-coefficient identity checked across cycle windings','coordinate':'n increases by one vacancy hop; 15 steps shift every E by +3','basis':'D[n,n] and D[n,n+1], each quadratic in k where n=r+15k','rows':rows,'weighted_laplacian_remainder':rem_rows,'cell_sums':{'alpha_sum':str(alpha_sum),'beta_sum':str(beta_sum)},'weights_nonnegative_all_integer_k':True,'weights_at_least_k_squared_for_abs_k_ge_3':True}
(HERE/'D_RESIDUE_POLYNOMIALS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
