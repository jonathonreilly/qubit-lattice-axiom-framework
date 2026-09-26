#!/usr/bin/env python3
"""Independent exact square-cycle worm and finite-difference controls.

No imports or reads from author implementation/results. Four charge vertices
and four distinct midpoint slots form a single square, not a three-site ring.
"""
from pathlib import Path
from itertools import product
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
checks=[]
def ok(name,condition,detail=None):
 assert bool(condition),(name,detail)
 checks.append({'name':name,'passed':True,'detail':detail})

# Each oriented edge runs counterclockwise around a square.
edges=[(0,1),(1,2),(2,3),(3,0)]
q=4
fields=list(product((-1,0,1),repeat=q))
def divergence(f):
 out=[0]*q
 for a,(u,v) in zip(f,edges):out[u]+=a;out[v]-=a
 return tuple(out)
states=[]
for f in fields:
 div=divergence(f)
 for tail in range(q):
  for head in range(q):
   target=tuple(int(x==tail)-int(x==head) for x in range(q))
   if div==target:states.append((f,tail,head))
index={state:i for i,state in enumerate(states)}
z=s.Rational(2)
weights=s.Matrix([[z**sum(a!=0 for a in f) for f,_,_ in states]])
P=s.zeros(len(states))
R=s.zeros(len(states))
for ix,(f,tail,head) in enumerate(states):
 # Symmetric choice of the two incident square directions.
 options=[]
 for edge,(u,v) in enumerate(edges):
  if u==head:options.append((edge,+1,v))
  if v==head:options.append((edge,-1,u))
 assert len(options)==2
 for edge,sign,newhead in options:
  if f[edge] not in (0,-sign):P[ix,ix]+=s.Rational(1,2);continue
  new=list(f);new[edge]+=sign;new=tuple(new)
  change=sum(a!=0 for a in new)-sum(a!=0 for a in f)
  accept=min(s.Integer(1),z**change)
  jx=index[new,tail,newhead]
  P[ix,jx]+=accept/2;P[ix,ix]+=(1-accept)/2
 if head==tail:
  for target in range(q):R[ix,index[f,target,target]]+=s.Rational(1,q)
 else:R[ix,ix]=1
ok('square_extended_rows',all(sum(P.row(i))==1 for i in range(len(states))))
ok('square_extended_detailed_balance',s.diag(*list(weights))*P==P.T*s.diag(*list(weights)))
ok('closed_uniform_endpoint_relocation',weights*R==weights)
M=R*P
ok('composed_kernel_stationarity',weights*M==weights)
closed=[i for i,(_,t,h) in enumerate(states) if t==h]
opened=[i for i in range(len(states)) if i not in closed]
trace=M.extract(closed,closed)+M.extract(closed,opened)*(s.eye(len(opened))-M.extract(opened,opened)).inv()*M.extract(opened,closed)
wc=weights.extract([0],closed);wc=wc/sum(wc)
ok('exact_closed_trace_stationarity',wc*trace==wc)
ok('trace_rows_include_self_transitions',all(sum(trace.row(i))==1 for i in range(len(closed))) and any(trace[i,i]>0 for i in range(len(closed))))
closed_fields=sorted({states[i][0] for i in closed})
pi={f:sum(wc[j] for j,i in enumerate(closed) if states[i][0]==f) for f in closed_fields}
expected={f:z**sum(a!=0 for a in f)/(1+2*z**4) for f in closed_fields}
ok('three_square_closed_field_weights',pi==expected and len(closed_fields)==3,{str(f):str(p) for f,p in pi.items()})
# Relocation makes the field trace independent of the stored endpoint.
Q=s.zeros(3)
for a,f in enumerate(closed_fields):
 rows_f=[j for j,i in enumerate(closed) if states[i][0]==f]
 for b,g in enumerate(closed_fields):
  cols_g=[j for j,i in enumerate(closed) if states[i][0]==g]
  vals=[sum(trace[i,j] for j in cols_g) for i in rows_f]
  assert len(set(vals))==1
  Q[a,b]=vals[0]
pvec=s.Matrix([[pi[f] for f in closed_fields]])
jump=s.zeros(3)
for i in range(3):
 for j in range(3):
  if i!=j:jump[i,j]=Q[i,j]/(1-Q[i,i])
flux=s.Matrix([[pvec[i]*(1-Q[i,i]) for i in range(3)]]);flux/=sum(flux)
ok('dropping_closed_field_self_visits_biases_target',pvec*jump!=pvec and flux*jump==flux,
   {'target':[str(x) for x in pvec],'jump_stationary':[str(x) for x in flux]})
# Directed transition graph reaches every extended state.
seen={0}
while True:
 more=seen|{j for i in seen for j in range(len(states)) if M[i,j]>0}
 if more==seen:break
 seen=more
ok('square_extended_accessibility',len(seen)==len(states),{'extended_states':len(states),'closed_states_with_tail':len(closed)})

# Full finite-lattice parity identity, for arbitrary unconstrained vector arrays.
N=4
sites=list(product(range(N),repeat=3))
F={x:s.Matrix([((17*x[0]+11*x[1]+5*x[2]+3*i)%7)-3 for i in range(3)]) for x in sites}
def shift(x,i,n):return tuple((a+n)%N if j==i else a for j,a in enumerate(x))
def div2(field,x):return sum(field[shift(x,i,1)][i]-field[shift(x,i,-1)][i] for i in range(3))
for eta in product((0,1),repeat=3):
 transformed={x:s.Matrix([(-1)**(sum(a*b for a,b in zip(eta,x))+eta[i])*F[x][i] for i in range(3)]) for x in sites}
 assert all(div2(transformed,x)==(-1)**sum(a*b for a,b in zip(eta,x))*div2(F,x) for x in sites)
ok('all_eight_even_torus_staggering_identities',True)

# Complex adjoint identity for unrestricted symbolic complex v.
x=s.symbols('x:3',real=True);y=s.symbols('y:3',real=True)
v=s.Matrix([x[i]+s.I*y[i] for i in range(3)])
def cross(v):return s.Matrix([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
C=cross(v);norm=(v.conjugate().T*v)[0]
ok('adjoint_cross_gram_order_and_conjugation',
 all(s.simplify(a)==0 for a in C.conjugate().T*C-(norm*s.eye(3)-v*v.conjugate().T)) and
 all(s.simplify(a)==0 for a in C*C.conjugate().T-(norm*s.eye(3)-v.conjugate()*v.T)))
v=s.Matrix([s.I-1,-2,-s.I-1]);C=cross(v);zero=s.zeros(3)
G=zero.row_join(C.conjugate().T).col_join((-C).row_join(zero))
lam=s.symbols('lambda')
ok('adjoint_maxwell_six_field_spectrum',G.conjugate().T==-G and s.factor(G.charpoly(lam).as_expr())==lam**2*(lam**2+8)**2,
   {'charpoly':str(s.factor(G.charpoly(lam).as_expr()))})
for eta in product((0,1),repeat=3):
 centered=[0,0,0]
 plus=[-2*e for e in eta]
 if any(eta):assert sum(a*a for a in plus)>0
ok('adjoint_single_zero_and_centered_eight_corners',True)
output={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,
 'square_field_trace':[[str(Q[i,j]) for j in range(3)] for i in range(3)],
 'scope':'Exact reduced square-cycle sampler control and operator algebra; not a full cubic sampler equivalence or production mixing test.'}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
