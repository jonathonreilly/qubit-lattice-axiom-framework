"""Independent supplier controls. No author checker is imported or executed.

The sole reused mathematical data are the separately checked rotor Laurent
coefficients.  Finite battery matrices below are a different exact fixture;
the unbounded-rotor extension is proved in REPORT.md, not by a cutoff model.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from collections import Counter
import json,hashlib,math
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def simplify(M):return M.applyfunc(s.simplify)
def zero(M):return all(s.simplify(x)==0 for x in M)

# Independently identify the physical circulation and read its frozen coefficient.
z=((( -2,0,0),(-2,-1,0),-1),((-2,0,0),(-1,0,0),1),
   ((-1,-1,0),(-2,-1,0),1),((-1,-1,0),(-1,0,0),-1))
div=Counter()
for a,b,c in z:div[a]+=c;div[b]-=c
assert all(c==0 for c in div.values())
coeff=json.loads((ROOT/'independent-birth-energy-check/coefficients.json').read_text())
cov={}
for mark,terms in coeff.items():
 found=[Fraction(c) for w,c in terms if tuple((tuple(a),tuple(b),v) for a,b,v in w)==z]
 assert found==[Fraction(2,5)],(mark,found)
 cov[mark]={'matrix_element_over_delta':str(found[0]),'state_expectation_difference_over_delta':str(2*found[0])}

# Incidence Schur bound, retaining both charges, on the entire six-neighbour
# local hard-core matter carrier. Rotor shifts are permutations of field words.
degrees={}
for o in range(6):
 rows=Counter();cols=[]
 for bs in product((0,-1,1),repeat=6):
  if sum(v!=0 for v in bs)!=o:continue
  for charge in (-1,1):
   count=0
   for j,v in enumerate(bs):
    if v:continue
    out=list(bs);out[j]=charge
    rows[tuple(out)]+=1;count+=1
   cols.append(count)
 assert set(cols)=={6-o} and set(rows.values())=={o+1}
 degrees[o]={'column_degree':6-o,'row_degree':o+1,'norm_squared_bound':(6-o)*(o+1)}
assert max(d['norm_squared_bound'] for d in degrees.values())==12

# Count affected pair terms geometrically without reading author helper code.
near=[v for v in product(range(-2,3),repeat=3) if sum(abs(x) for x in v)==2]
assert len(near)==18
centers={(0,0,0),*near}
affected=set()
for a in centers:
 for d in near:
  b=tuple(a[i]+d[i] for i in range(3))
  affected.add(tuple(sorted((a,b))))
assert len(affected)==264
local_magnetic_bound=len(affected)*(2*12**2+72)
assert local_magnetic_bound==95040

# Different cap fixture: Hin=(0,2), Hout=(0,4), nontrivial Hadamard W.
# The input and output each have a positive battery with levels 0,...,4.
# Both lower and upper losses occur on the supplied packet below.
B=5
Hin=s.diag(0,2);Hout=s.diag(0,4)
W=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
C=s.zeros(2*B)
for j,ein in enumerate((0,2)):
 for n in range(B):
  for i,eout in enumerate((0,4)):
   m=n+ein-eout
   if 0<=m<B:C[i*B+m,j*B+n]=W[i,j]
Kin=s.diag(*(list(range(B))+list(range(2,2+B))))
Kout=s.diag(*(list(range(B))+list(range(4,4+B))))
assert zero(Kout*C-C*Kin)

# The square-root polynomial is exact for the fixture spectrum {0,1/2,1}.
# Independently assert the spectral polynomial before using its root.
def defect(A):
 I=s.eye(A.rows)
 assert zero(A*(A-I/2)*(A-I))
 R=simplify(I+(2*s.sqrt(2)-3)*A+(2-2*s.sqrt(2))*A*A)
 assert zero(R*R-(I-A))
 return R
R=defect(C.H*C);D=defect(C*C.H)
U=R.row_join(-C.H).col_join(C.row_join(D))
K=s.diag(Kin,Kout)
assert zero(U.H*U-s.eye(4*B)) and zero(U*U.H-s.eye(4*B))
assert zero(K*U-U*K)

phi=s.Matrix([1,s.I])/s.sqrt(2)
beta=s.Matrix([0,s.Rational(1,2),1/s.sqrt(2),s.Rational(1,2),0])
psi=s.kronecker_product(phi,beta)
accepted=simplify(C*psi);refused=simplify(R*psi)
p=s.simplify((refused.H*refused)[0])
assert s.simplify((accepted.H*accepted)[0]+p)==1

# Explicit uncapped energy-line output, including both sides of the real cap.
chi={}
for j,ein in enumerate((0,2)):
 for n in range(B):
  for i,eout in enumerate((0,4)):
   key=(i,n+ein-eout)
   chi[key]=s.simplify(chi.get(key,0)+W[i,j]*phi[j]*beta[n])
chi={k:v for k,v in chi.items() if v!=0}
low=s.simplify(sum(s.conjugate(v)*v for (i,e),v in chi.items() if e<0))
high=s.simplify(sum(s.conjugate(v)*v for (i,e),v in chi.items() if e>=B))
assert low>0 and high>0 and s.simplify(low+high-p)==0
assert all((0,4)[i]+e>=1 for (i,e),v in chi.items())
assert all((0,4)[i]>1 for (i,e),v in chi.items() if e<0)
assert all((0,4)[i]+e>4 for (i,e),v in chi.items() if e>4)

Hs_in=s.kronecker_product(Hin,s.eye(B))
Hs_out=s.kronecker_product(Hout,s.eye(B))
Eb=s.kronecker_product(s.eye(2),s.diag(*range(B)))
initial_system=s.simplify((psi.H*Hs_in*psi)[0])
initial_battery=s.simplify((psi.H*Eb*psi)[0])
final_system=s.simplify((accepted.H*Hs_out*accepted)[0]+(refused.H*Hs_in*refused)[0])
final_battery=s.simplify((accepted.H*Eb*accepted)[0]+(refused.H*Eb*refused)[0])
assert s.simplify(initial_system+initial_battery-final_system-final_battery)==0
refusal_energy=s.simplify((refused.H*Hs_in*refused)[0])
J=s.sqrt(2);bottom=1;width=2
refusal_bound=bottom*p+(J+width)*s.sqrt(p)
assert float(refusal_energy)<=float(refusal_bound)

# Non-recurrence time t=pi/3. Correct pre-program phase is exp(+i K t).
phases=(1,(1+s.I*s.sqrt(3))/2,(-1+s.I*s.sqrt(3))/2,-1,
        (-1-s.I*s.sqrt(3))/2,(1-s.I*s.sqrt(3))/2)
free=s.diag(*(phases[-int(K[i,i])%6] for i in range(K.rows)))
program=simplify(free.H*U)
assert zero(free*program-U)
wrong_program=simplify(free*U)
assert not zero(free*wrong_program-U)
wrong_relative=simplify(free*wrong_program*U.H)
assert s.simplify(wrong_relative[0,0]-wrong_relative[1,1])!=0
Q=s.zeros(K.rows).row_join(program.H).col_join(program.row_join(s.zeros(K.rows)))
Kclock=s.diag(K,K)
assert zero(Q.H-Q) and zero(Q*Q-s.eye(2*K.rows)) and zero(Q*Kclock-Kclock*Q)
# g*t=pi/2 gives evolution -i*exp(-i*pi/2)*free*program=-U.
arrival=simplify(-free*program)
assert zero(arrival+U)

# The uncapped lift with BOTH system and battery freely evolved obeys the
# output total-energy phase, so sharp-reference behavior differs from W phi_s.
free_in=s.diag(1,phases[-2%6]);free_out=s.diag(1,phases[-4%6])
desired=simplify(W*free_in*phi)
free_reference=simplify(free_out*W*phi)
assert not zero(desired*desired.H-free_reference*free_reference.H)

N=24**3//2
Crot=95040+48*N+2*math.sqrt(48*N)+2
Jrot=math.sqrt((1974*N)**2+48*N)
results={'covariance':cov,'incidence_degrees':degrees,'affected_pair_count':len(affected),
 'magnetic_commutator_bound':local_magnetic_bound,
 'cap_fixture':{'input_dimension':2*B,'output_dimension':2*B,'Julia_dimension':4*B,
  'battery_cap':B-1,'lower_loss':str(low),'upper_loss':str(high),'refusal':str(p),
  'initial_system':str(initial_system),'initial_battery':str(initial_battery),
  'final_system':str(final_system),'final_battery':str(final_battery),
  'refusal_system_energy':str(refusal_energy),'refusal_energy_bound':str(refusal_bound),
  'two_sided_unitarity':True,'strong_energy_block_relation':True},
 'clock':{'time':'pi/3','coupling':'3/2','dimension':2*K.rows,
          'correct_sign_arrival':'-U','wrong_phase_sign_detected':True,
          'free_reference_changes_target_state':True},
 'rotor_L24_unit_coupling':{'N':N,'C':Crot,'J':Jrot},
 'scope':'Exact finite controls plus analytic report; no rotor cutoff, author program or original coefficient regeneration.'}
(HERE/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
print('TOTAL: PASS=7 FAIL=0 (covariance data; incidence norm; geometry; Julia; cap/refusal; nonrecurrence clock; free-reference distinction)')
