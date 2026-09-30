"""One priced, standard-library exact job: original source words and supports.
No imports from other campaign runners; no rotor matrix truncation.
"""
from collections import Counter
from itertools import product
from fractions import Fraction
from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent
start=time.monotonic()
dirs=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def norm(a):return sum(abs(x) for x in a)
def ball(r,even=False):
 return {p for p in product(range(-r,r+1),repeat=3) if norm(p)<=r and (not even or sum(p)%2==0)}
disps={plus(a,b) for a in dirs for b in dirs if norm(plus(a,b))==2}
assert len(disps)==18
X=ball(4,True)
pairs={tuple(sorted((a,plus(a,d)))) for a in X for d in disps}
assert len(X)==85 and len(pairs)==1038
support_checks=[]
for r in (2,4,6):
 inner=ball(r,True)
 kept={tuple(sorted((a,plus(a,d)))) for a in inner for d in disps}
 S={a for p in kept for a in p}
 S|={plus(a,d) for a in list(S) for d in dirs}
 seed={(0,0,0),*dirs};S|=seed
 Splus=S|{plus(a,d) for a in S for d in dirs}
 assert max(map(norm,S))<=r+3 and max(map(norm,Splus))<=r+4
 candidates=ball(r+5,True)
 boundary=set()
 for a in candidates:
  for d in disps:
   c=plus(a,d);p=tuple(sorted((a,c)))
   if p in kept:continue
   supp={a,c}|{plus(x,e) for x in (a,c) for e in dirs}
   if supp&Splus:boundary.add(p)
 assert all(not ({a,c}|{plus(x,e) for x in (a,c) for e in dirs})&seed for a,c in boundary)
 upper=90*(4*(r+5)**2+2)
 assert len(boundary)<=upper
 support_checks.append({'r':r,'kept_pairs':len(kept),'gate_site_support':len(Splus),'actual_boundary_pairs':len(boundary),'boundary_pair_upper':upper})

# Literal original F and j on two complete cubic degree-six stars.
acenters=((0,0,0),(1,1,0))
bverts=sorted({plus(a,d) for a in acenters for d in dirs})
adj=tuple(tuple(i for i,b in enumerate(bverts) if norm(tuple(x-y for x,y in zip(a,b)))==1) for a in acenters)
edges=tuple((a,b) for a in range(2) for b in adj[a]);ei={e:i for i,e in enumerate(edges)}
shared=set(adj[0])&set(adj[1]);assert len(shared)==2
b=next(i for i,v in enumerate(bverts) if v==(1,0,0))
d=next(i for i,v in enumerate(bverts) if v==(0,1,0))

def hop(st,a,reverse=False):
 aq,bq,ee=st
 if not reverse:
  if not aq[a]:return
  for dest in adj[a]:
   if bq[dest]:continue
   aa=list(aq);bb=list(bq);en=list(ee);q=aa[a]
   aa[a]=0;bb[dest]=q;en[ei[a,dest]]-=q
   yield tuple(aa),tuple(bb),tuple(en)
 else:
  if aq[a]:return
  for dest in adj[a]:
   if not bq[dest]:continue
   aa=list(aq);bb=list(bq);en=list(ee);q=bb[dest]
   aa[a]=q;bb[dest]=0;en[ei[a,dest]]+=q
   yield tuple(aa),tuple(bb),tuple(en)

def apply_hop(vec,a,reverse=False):
 out=Counter()
 for st,v in vec.items():
  for dest in hop(st,a,reverse):out[dest]+=v
 return +out if all(v>=0 for v in out.values()) else {k:v for k,v in out.items() if v}
def pair(vec):
 out=vec
 for a,rev in ((0,False),(1,False),(1,True),(0,True)):out=apply_hop(out,a,rev)
 return {k:-2*v for k,v in out.items() if v}
def birth(vec,sigma):
 out=Counter()
 for st,v in vec.items():
  for aq,bq,ee in hop(st,0):
   if bq[b]:continue
   aa=list(aq);bb=list(bq);en=list(ee)
   aa[0]=sigma;bb[b]=-sigma;en[ei[0,b]]+=sigma
   out[(tuple(aa),tuple(bb),tuple(en))]+=v
 return {k:v for k,v in out.items() if v}
def subtract(u,v):
 return {k:u.get(k,0)-v.get(k,0) for k in u.keys()|v.keys() if u.get(k,0)!=v.get(k,0)}
def diag(st):
 aq,bq,ee=st
 return sum(ee[i]*(ee[i]-aq[a]) for i,(a,b) in enumerate(edges) if bq[b]==0)
def circulation(n):
 e=[0]*len(edges)
 for a,j,sgn in ((0,b,1),(1,b,-1),(1,d,1),(0,d,-1)):e[ei[a,j]]=sgn*n
 return ((1,1),(0,)*len(bverts),tuple(e))
base=circulation(0)
# Exact vacuum coefficient, including the two nontrivial plaquette translates.
vac=pair({base:1});assert vac[base]==-68 and sorted(vac.values())==[-68,-2,-2]
comm_rows=[]
comm_vectors=[]
for sigma in (-1,1):
 u=subtract(pair(birth({base:1},sigma)),birth(pair({base:1}),sigma))
 assert u
 comm_vectors.append(u)
 comm_rows.append({'sigma':sigma,'nonzero_words':len(u),'norm_squared':sum(v*v for v in u.values())})
coherent={k:sum(u.get(k,0) for u in comm_vectors) for k in comm_vectors[0].keys()|comm_vectors[1].keys()}
coherent={k:v for k,v in coherent.items() if v}
coherent_norm2=sum(v*v for v in coherent.values())
assert coherent_norm2>0
comm_rows.append({'instrument':'original unnormalized coherent sign sum','nonzero_words':len(coherent),'norm_squared':coherent_norm2,'cross_term_vs_resolved_sum':coherent_norm2-sum(row['norm_squared'] for row in comm_rows)})
# Unbounded electric commutator along actual physical circulation words.
# D on the full cubic embedding has the same values: all omitted link fields zero.
electric=[]
for n in (1,2,3,10):
 st=circulation(n);assert diag(st)==4*n*n
 av=pair({st:1});comm={s:(diag(s)-diag(st))*v for s,v in av.items() if diag(s)!=diag(st)}
 # Two shifted circulations with energy differences +/-8n+4, coefficient -2.
 assert sum(v*v for v in comm.values())==512*n*n+128
 electric.append({'circulation':n,'electric_pair_commutator_norm_squared':sum(v*v for v in comm.values())})

# Exact algebraic free-battery phase-flow discriminator in a declared 2x2
# finite fixture, independent of the source-word check above.
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def add(A,B):return tuple(tuple(A[i][j]+B[i][j] for j in range(2)) for i in range(2))
def scale(a,A):return tuple(tuple(a*A[i][j] for j in range(2)) for i in range(2))
def transpose(A):return tuple(zip(*A))
Z=((1,0),(0,-1));B=((1,0),(1,0));rho=((1,0),(0,0));G=mm(transpose(B),B)
def C(X):return add(mm(Z,X),scale(-1,mm(X,Z)))
def D(X):return add(mm(mm(B,X),transpose(B)),scale(Fraction(-1,2),add(mm(G,X),mm(X,G))))
cd=add(C(D(rho)),scale(-1,D(C(rho))))
assert cd!=((0,0),(0,0))
# Product e^(t A)e^(t D) and e^(t(A+D)) differ at t² by [A,D]/2;
# A=-i C. Strip their common -i to keep exact rational arithmetic.
flow_witness=[[str(x/2) for x in row] for row in cd]

# A transparent finite-volume sufficient resource certificate, symbolic only.
# eta target, collision count, and local battery spectra are not simulated.
N=24**3//2;K=delta=kappa=T=1;field_cut=100;epsilon=Fraction(1,100)
v=2592*N;Qmax=1+6*N*field_cut;hbar=2*K*Qmax*Qmax+2*v
g=80*kappa*N;c=7*g*g+4*hbar*g
n=(4*c*epsilon.denominator+epsilon.numerator-1)//epsilon.numerator
m=N*n;Mb=90*(4*9**2+2);boundary_norm=288*delta*Mb
# m eta<=eps/4 and m boundary_norm eta<=eps/4 in chosen energy unit.
eta_den=4*m*(boundary_norm+1)*epsilon.denominator
# 4 pi < 13, so LB+1 >=13/eta is sufficient.
LB=13*eta_den
assert Fraction(13*m,LB+1)<=epsilon/4
assert Fraction(13*m*boundary_norm,LB+1)<=epsilon/4
assert Fraction(c,n)<=epsilon/4
result={'source_overlap_counts':{'even_radius4_centers':len(X),'pairs_meeting_radius4_centers':len(pairs),'pair_overlap_upper':2076,'J_over_delta':288,'q_over_delta':2*288*2076},
 'support_checks':support_checks,'actual_source_pair_birth_boundary_commutator':comm_rows,
 'actual_unbounded_electric_pair_controls':electric,
 'free_battery_phase_flow_t_squared_difference_over_minus_i':flow_witness,
 'finite_cut_example_only_not_rotor_accuracy_claim':{'N':N,'per_link_cutoff':field_cut,'hbar':hbar,'g':g,'collision_bins':n,'fresh_batteries_and_mark_flags':m,'boundary_pair_upper':Mb,'boundary_energy_norm_upper':boundary_norm,'ladder_width':LB,'process_error_bound':'<=1/200 from sweep+fresh-battery errors','mean_free_energy_ledger_defect':'<=1/400 before finite-pulse errors','caveat':'No claim cutoff100 approximates the unbounded law; choose it from the accepted rotor bridge for that task.'},
 'runtime_seconds':time.monotonic()-start,
 'scope':'Exact source word/support controls, rational resource inequalities, and a separately labelled finite phase-flow fixture. Analytic proofs carry continuum times, Fourier tails, process composition and arbitrary rotor values.'}
(OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));print('PASS 6 groups; FAIL 0')
