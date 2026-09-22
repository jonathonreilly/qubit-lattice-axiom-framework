"""Independent exact controls of sector-preserving dressing and resolvent bookkeeping.
No original runner imported; does not prove the imported infinite-dimensional bound.
"""
import json, time, hashlib
from pathlib import Path
from fractions import Fraction as F
start=time.monotonic(); checks=[]
def ck(name,value):
 assert value,name
 checks.append(name)
def mm(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,t):return [[t*x for x in a] for a in A]
n=8; I=[[int(i==j) for j in range(n)] for i in range(n)]
# two physical binary sites and a ghost; neutral creation raises BOTH physical
# sites, without changing a ghost excitation outside its support.
C=[[0]*n for _ in range(n)]
for g in range(2): C[6+g][g]=F(2,7)
P=[[int(i==j and i%2==0) for j in range(n)] for i in range(n)]
# opposite charges on two physical excitations, diagonal symmetry parameter2
G=[[F(2)**(((i>>2)&1)-((i>>1)&1)) if i==j else 0 for j in range(n)] for i in range(n)]
S=add(I,C); T=add(I,scale(C,-1))
ck('nilpotent_creation',mm(C,C)==[[0]*n for _ in range(n)])
ck('bounded_polynomial_inverse',mm(S,T)==I and mm(T,S)==I)
ck('ghost_projection_intertwines',mm(S,P)==mm(P,S))
ck('neutral_creation_equivariant',mm(S,G)==mm(G,S))
for L in (1,2,7):
 eta=F(1,5)
 for z in (-2,0,F(3,4)*L):
  ratios=[F(s)/(s-z) for s in range(L,L+13)]
  bound=1 if z<0 else F(L)/(L-z)
  ck(f'resolvent_sup_L{L}_z{z}',max(ratios)<=bound and eta*bound<1)
ck('nine_component_amplification_sharp',sum([F(1)]*9)**2==9*sum(x*x for x in [F(1)]*9))
# Completeness identity for traceless SU(N) generators normalized tr(TaTb)=2delta:
# sum_a Ta_ij Ta_kl=2(delta_il delta_jk-delta_ij delta_kl/N).
N=3
casimir=[[sum(2*(int(i==j)-F(int(i==k and k==j),N)) for k in range(N)) for j in range(N)] for i in range(N)]
ck('SU3_completeness_Casimir',casimir==[[F(16,3) if i==j else 0 for j in range(N)] for i in range(N)])
# Framework generators divide conventional Gell-Mann generators by sqrt(2).
ck('framework_energy_per_link',F(3,2)*(casimir[0][0]/2)==4)
out={'checks':checks,'passed':len(checks),'elapsed_seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Finite exact algebra only; imported coordinate theorem and domain/sector proof separately read analytically.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
