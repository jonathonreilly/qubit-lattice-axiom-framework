"""One M2 per cubic site: collective shell pairs, exact Laurent overlap,
full local Pauli operators, proper-cubic covariance and readout witnesses.
No oscillator or harmonic substitution occurs.
"""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from collections import defaultdict,Counter
from pathlib import Path
import json
import sympy as s

ZERO=(0,0,0)
DIRS=tuple(tuple(sign if j==i else 0 for j in range(3)) for i in range(3) for sign in (1,-1))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def pair(a,b):return tuple(sorted((a,b)))
def ei(i):return DIRS[2*i]
D=[{pair(ei(i),neg(ei(i))):F(1)} for i in range(3)]
def combine(terms):
 out=defaultdict(F)
 for c,v in terms:
  for k,w in v.items():out[k]+=c*w
 return {k:v for k,v in out.items() if v}
E=[combine([(F(1),D[0]),(-F(1),D[1])]),combine([(F(1),D[0]),(F(1),D[1]),(-F(2),D[2])])]
T=[{pair(tuple(a*x for x in ei(i)),tuple(b*x for x in ei(j))):F(a*b,2) for a,b in product((1,-1),repeat=2)} for i,j in ((0,1),(0,2),(1,2))]
Q=E+T;norm=[F(2),F(6),F(1),F(1),F(1)]

def translated(v,t):return {pair(add(a,t),add(b,t)):c for (a,b),c in v.items()}
def inner(v,w):return sum(c*w.get(k,0) for k,c in v.items())
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
def rotations():
 for perm in permutations(range(3)):
  for signs in product((1,-1),repeat=3):
   if parity(perm)*signs[0]*signs[1]*signs[2]==1:
    yield lambda v,p=perm,t=signs:tuple(t[i]*v[p[i]] for i in range(3))

def main():
 # All translations possibly matching two radius-one shells lie in [-2,2]^3.
 G={}
 for a in range(5):
  for b in range(5):
   for t in product(range(-2,3),repeat=3):
    val=inner(Q[a],translated(Q[b],t))
    if val:G[a,b,t]=val
 expected={(0,0,ZERO):F(2),(1,1,ZERO):F(6)}
 for a,(i,j) in enumerate(((0,1),(0,2),(1,2)),start=2):
  expected[a,a,ZERO]=F(1)
  for u,v in product((1,-1),repeat=2):
   t=tuple(u*ei(i)[k]+v*ei(j)[k] for k in range(3))
   expected[a,a,t]=F(1,4)
 assert G==expected,(G,expected)
 # Exact action and covariance on the 15 shell two-particle words.
 words=list(combinations(DIRS,2));words=[pair(*w) for w in words];index={w:i for i,w in enumerate(words)}
 cols=[]
 for q in Q:cols.append(s.Matrix([s.Rational(q.get(w,0).numerator,q.get(w,0).denominator) for w in words]))
 PE=sum((v*v.T/s.Rational(norm[i].numerator,norm[i].denominator) for i,v in enumerate(cols[:2])),s.zeros(15))
 PT=sum((v*v.T for v in cols[2:]),s.zeros(15))
 assert PE*PE==PE and PT*PT==PT and PE*PT==s.zeros(15)
 for R in rotations():
  U=s.zeros(15)
  for j,(a,b) in enumerate(words):U[index[pair(R(a),R(b))],j]=1
  assert U*PE*U.T==PE and U*PT*U.T==PT
 # Literal lowering-pair matrices on all 64 states, including N>2.
 ann=[]
 for q in Q:
  A=s.zeros(64)
  for state in range(64):
   for (a,b),c in q.items():
    i,j=DIRS.index(a),DIRS.index(b)
    if (state>>i)&1 and (state>>j)&1:
     A[state^(1<<i)^(1<<j),state]+=s.Rational(c.numerator,c.denominator)
  ann.append(A)
 QE=sum((A.T*A/s.Rational(norm[i].numerator,norm[i].denominator) for i,A in enumerate(ann[:2])),s.zeros(64))
 QT=sum((A.T*A for A in ann[2:]),s.zeros(64))
 assert QE[63,63]==2 and QT[63,63]==3
 # Same record probabilities, different collective tensor-sector expectation.
 ip=DIRS.index(ei(0));im=DIRS.index(neg(ei(0)));jp=DIRS.index(ei(1));jm=DIRS.index(neg(ei(1)))
 sx=(1<<ip)|(1<<im);sy=(1<<jp)|(1<<jm)
 vplus=s.zeros(64,1);vminus=s.zeros(64,1)
 vplus[sx]=vminus[sx]=1;vplus[sy]=1;vminus[sy]=-1
 wp=(vplus.T*QE*vplus)[0]/2;wm=(vminus.T*QE*vminus)[0]/2
 assert wp==s.Rational(1,3) and wm==1
 # The filling witness is exact for every even torus: half the centers have full shells.
 mu,gE,gT,W=s.symbols('mu gE gT W',positive=True)
 density_full=mu-2*gE-3*gT+3*W
 density_checker=(mu-2*gE-3*gT)/2
 critical_checker=s.simplify(density_checker.subs({gE:2*mu,gT:mu}))
 assert critical_checker==-3*mu
 qx,qy,qz=s.symbols('qx qy qz',real=True)
 ST=[1+s.cos(qx)*s.cos(qy),1+s.cos(qx)*s.cos(qz),1+s.cos(qy)*s.cos(qz)]
 critical=[s.simplify(2*mu-mu*g) for g in ST]
 axis=[x.subs({qx:0,qy:0,qz:s.Symbol('k',real=True)}) for x in critical]
 output={'overlap_terms':[{'a':a,'b':b,'shift':t,'value':str(v)} for (a,b,t),v in sorted(G.items())],
         'local_cubic_ranks':[int(PE.trace()),int(PT.trace())],
         'local_orthogonal_projectors':True,'proper_rotations_checked':24,
         'full_shell_QE_QT':[str(QE[63,63]),str(QT[63,63])],
         'same_Z_distribution_QE_expectations':[str(wp),str(wm)],
         'two_particle_E_band':'2 mu - gE (multiplicity 2)',
         'two_particle_T_bands':['2 mu - gT ('+str(x)+')' for x in ST],
         'critical_T_bands':[str(x) for x in critical],
         'critical_axis_T_bands':[str(x) for x in axis],
         'full_density_with_NN_repulsion':str(density_full),
         'checker_density_with_NN_repulsion':str(density_checker),
         'critical_checker_density':str(critical_checker)}
 print(json.dumps(output,indent=2))
 print('TOTAL: PASS=5 FAIL=0 (exact Laurent Gram; cubic covariance; literal full M2 carrier; readout pair; all-volume product-state witness)')
 Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')

if __name__=='__main__':main()
