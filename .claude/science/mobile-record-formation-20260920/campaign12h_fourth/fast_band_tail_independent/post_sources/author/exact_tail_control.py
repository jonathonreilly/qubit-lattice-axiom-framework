"""Exact physical-cycle and Laurent-path certificate for the rotor cube tail.

Self-contained integer/SymPy construction; no other campaign code is imported.
The phase witness has z_01=-1 and all remaining edge phases equal to one.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json,sympy as s

A=(0,3,5,6);B=(1,2,4,7)
edges=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
tree=(1,2,3,4,6,9,11);chords=(0,5,7,8,10)
zero=(0,)*5
words=[]
for occupied in combinations(range(8),6):
 for minus in occupied:
  words.append(tuple((-1 if i==minus else 1) if i in occupied else 0 for i in range(8)))
grade=lambda q:sum(q[a]==0 for a in A)
low=[q for q in words if grade(q)==0]
middle=[q for q in words if grade(q)==1]
upper=[q for q in words if grade(q)==2]
dark=[q for q in middle if not any(q[a]==q[b]==0 for a,b in edges)]
bright=[q for q in middle if q not in dark]
assert [len(low),len(middle),len(upper),len(dark),len(bright)]==[36,96,36,24,72]

def step(q,inward=False):
 result=[]
 for ei,(a,b) in enumerate(edges):
  legal=q[a]==0 and q[b]!=0 if inward else q[a]!=0 and q[b]==0
  if not legal:continue
  charge=q[b] if inward else q[a]
  qq=list(q);qq[a],qq[b]=(charge,0) if inward else (0,charge)
  shift=[0]*5
  if ei in chords:shift[chords.index(ei)]=(charge if inward else -charge)
  result.append((tuple(qq),tuple(shift)))
 return result

def commutator_column(q):
 result=defaultdict(int)
 for first_inward,sign in [(True,1),(False,-1)]:
  for q1,e1 in step(q,first_inward):
   for q2,e2 in step(q1,not first_inward):
    assert grade(q2)==1
    result[(q2,tuple(x+y for x,y in zip(e1,e2)))]+=sign
 return {k:v for k,v in result.items() if v}

columns=[commutator_column(q) for q in dark]
assert all(q not in dark for col in columns for q,e in col)
Q=s.zeros(72,24);Qflat=s.zeros(72,24)
polynomials=[]
for j,col in enumerate(columns):
 for (q,e),value in col.items():
  i=bright.index(q);Q[i,j]+=value*(-1 if e[0]%2 else 1);Qflat[i,j]+=value
  polynomials.append({'bright_row':i,'dark_column':j,'cycle_exponent':e,'coefficient':value})
# The parity form keeps every Laurent evaluation in exact integer arithmetic.
assert all(v.is_Integer for v in Q)
gram=Q.T*Q;det=gram.det(method='domain-ge')
assert det>0
pivot_rows=list(Q.T.rref()[1]);assert len(pivot_rows)==24
minor=Q.extract(pivot_rows,range(24));minor_det=minor.det(method='domain-ge')
assert minor_det!=0
flat_rank=Qflat.rank();assert flat_rank==23
assert Qflat*s.ones(24,1)==s.zeros(72,1)

# Explicit integer tree/cycle coordinates for the physical Gauss subspace.
inc=s.zeros(8,12)
for i,(a,b) in enumerate(edges):inc[a,i]=1;inc[b,i]=-1
T=inc.extract(range(7),tree);assert abs(T.det())==1
cycles=s.zeros(12,5)
for j,ei in enumerate(chords):
 cycles[ei,j]=1
 v=-T.inv()*inc.extract(range(7),[ei])
 for k,ti in enumerate(tree):cycles[ti,j]=v[k]
assert inc*cycles==s.zeros(8,5)
assert all(v.is_Integer for v in cycles)
background=s.Matrix([int(i in A) for i in range(8)])
references={}
for q in words:
 rhs=s.Matrix(q)-background;v=T.inv()*rhs[:7,0];E=s.zeros(12,1)
 for k,ti in enumerate(tree):E[ti]=v[k]
 assert inc*E==rhs and all(v.is_Integer for v in E)
 references[q]=E
for q in words:
 for inward in [False,True]:
  for ei,(a,b) in enumerate(edges):
   legal=q[a]==0 and q[b]!=0 if inward else q[a]!=0 and q[b]==0
   if not legal:continue
   charge=q[b] if inward else q[a];qq=list(q);qq[a],qq[b]=(charge,0) if inward else (0,charge);qq=tuple(qq)
   de=s.zeros(12,1);de[ei]=charge if inward else -charge
   winding=s.Matrix([de[c] for c in chords])
   assert references[q]+de==references[qq]+cycles*winding

def physical_F(v,center=None):
 out=defaultdict(int)
 for (q,E),amp in v.items():
  for ei,(a,b) in enumerate(edges):
   if center is not None and a!=center:continue
   if not q[a] or q[b]:continue
   qq=list(q);ee=list(E);qq[a],qq[b]=0,q[a];ee[ei]-=q[a]
   out[(tuple(qq),tuple(ee))]+=amp
 return dict(out)
def birth(v,sign):
 out=defaultdict(int)
 for (q,E),amp in v.items():
  if q[0] or q[1]:continue
  for sigma in ([sign] if sign else [-1,1]):
   qq=list(q);ee=list(E);qq[0],qq[1]=sigma,-sigma;ee[0]+=sigma
   out[(tuple(qq),tuple(ee))]+=amp
 return dict(out)
omega={(tuple(int(i in A) for i in range(8)),(0,)*12):1}
actual=[]
for sign in [1,-1,0]:
 bv=birth(physical_F(omega),sign);rv={x:-v for x,v in physical_F(bv,0).items()}
 b=sum(v*v for v in bv.values());r=sum(v*v for v in rv.values())
 assert (b,r)=={1:(2,4),-1:(2,2),0:(4,6)}[sign]
 # Physical winding Fourier evaluation at flat phase; all R words are dark.
 v=s.zeros(24,1)
 for (q,E),amp in rv.items():assert q in dark;v[dark.index(q)]+=amp
 residual=(sum(v))**2/s.Integer(24*b)
 assert residual==({1:s.Rational(1,12),-1:s.Rational(1,12),0:s.Rational(1,6)}[sign])
 actual.append({'mark':sign,'b':b,'r':r,'flat_fiber_surviving_normalized_weight':str(residual),'physical_R':[{'q':q,'E':E,'coefficient':amp} for (q,E),amp in sorted(rv.items())]})

result={'all_assertions_passed':True,'edge_order':edges,'tree_edge_indices':tree,'chord_edge_indices':chords,'integer_cycle_matrix':[[int(v) for v in cycles.row(i)] for i in range(12)],'charge_words':words,'W_dimensions':[36,96,36],'dark_words':dark,'bright_words':bright,'dark_dark_Laurent_block_exactly_zero':True,'bright_dark_Laurent_entries':polynomials,'phase_witness':'z_01=-1; all other edge phases=1','Q_witness':[[int(v) for v in Q.row(i)] for i in range(72)],'Gram_witness':[[int(v) for v in gram.row(i)] for i in range(24)],'Gram_determinant':str(det),'full_rank_minor_rows':pivot_rows,'full_rank_minor_determinant':str(minor_det),'flat_phase_exact_rank':flat_rank,'flat_phase_uniform_dark_kernel_dimension':1,'actual_first_mark_flat_fiber_weights':actual,'scope':'Exact finite Laurent and physical Gauss-coordinate certificates. Almost-everywhere stability and strong decay follow from the separate analytic proof; a single Fourier fiber is not a normalizable physical state.'}
out=Path(__file__).parent/'EXACT_TAIL_RESULTS.json';out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['all_assertions_passed','W_dimensions','dark_dark_Laurent_block_exactly_zero','Gram_determinant','full_rank_minor_rows','full_rank_minor_determinant','flat_phase_exact_rank']},indent=2))
