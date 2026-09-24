"""Second author cube construction via explicit integer Gauss coordinates."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/cube_certificate_check.py',)
from pathlib import Path
from itertools import combinations
import hashlib,json,time
import sympy as sp
D=Path(__file__).resolve().parent
old=json.loads((D/'CUBE_POINT_SPECTRUM_RESULTS.json').read_text())
edges=[(u,v) for u in range(8) for v in range(u+1,8)
       if (u^v) in (1,2,4)]
tree=[(0,1),(0,2),(0,4),(1,3),(1,5),(2,6),(3,7)]
chords=[e for e in edges if e not in tree]
assert edges==[tuple(e) for e in old['edges']]
inc=sp.zeros(8,12)
for j,(u,v) in enumerate(edges):inc[u,j]=1;inc[v,j]=-1
ti=[edges.index(e) for e in tree];ci=[edges.index(e) for e in chords]
Bt=inc.extract(range(1,8),ti);Bc=inc.extract(range(1,8),ci)
assert abs(Bt.det())==1
inverse=Bt.inv();background=sp.Matrix([int(u in (0,3,5,6)) for u in range(8)])
words=[]
for holes in combinations(range(8),2):
 for minus in range(8):
  if minus not in holes:
   words.append(tuple(0 if u in holes else -1 if u==minus else 1 for u in range(8)))
words=sorted(words)
pw=[q for q in words if all(q[u] for u in (0,3,5,6))]
qw=[q for q in words if sum(q[u]==0 for u in (0,3,5,6))==1]
assert pw==[tuple(q) for q in old['P_words']]
assert qw==[tuple(q) for q in old['W1_words']]
qi={q:i for i,q in enumerate(qw)}
def field(q,f):
 E=sp.zeros(12,1);c=sp.Matrix(f)
 b=(sp.Matrix(q)-background).extract(range(1,8),[0])
 t=inverse*(b-Bc*c)
 for j,value in zip(ti,t):E[j]=value
 for j,value in zip(ci,c):E[j]=value
 assert inc*E==sp.Matrix(q)-background and all(x.is_Integer for x in E)
 return E
transitions=[];gauss_count=0
for col,q in enumerate(pw):
 for e,(u,v) in enumerate(edges):
  for source,dest,direction in [(u,v,-1),(v,u,1)]:
   if q[source]==0 or q[dest]!=0:continue
   q2=list(q);charge=q2[source];q2[dest]=charge;q2[source]=0;q2=tuple(q2)
   delta=sp.zeros(12,1);delta[e]=direction*charge
   df=tuple(int(delta[j]) for j in ci)
   assert q2 in qi
   for f in [(0,)*5]+[tuple(int(k==j) for k in range(5)) for j in range(5)]:
    f2=tuple(a+b for a,b in zip(f,df))
    assert field(q2,f2)-field(q,f)==delta;gauss_count+=1
   transitions.append((qi[q2],col,df))
assert len(transitions)==216
x=sp.symbols('x');rows=[];gcd=None
for saved in old['exact_rows'][:3]:
 turns=saved['quarter_turns'];A=sp.zeros(96,36)
 for row,col,df in transitions:A[row,col]-=sp.I**(sum(a*b for a,b in zip(turns,df))%4)
 H=(-A.conjugate().T*A).applyfunc(sp.expand)
 assert H==H.conjugate().T and all(H[j,j]==-6 for j in range(36))
 p=sp.Poly(H.charpoly(x).as_expr(),x,domain=sp.QQ)
 assert [str(c) for c in p.all_coeffs()]==saved['characteristic_coefficients']
 gcd=p if gcd is None else sp.gcd(gcd,p).monic()
 rows.append({'quarter_turns':turns,'gcd':str(sp.factor(gcd.as_expr())),
              'p_minus2':str(p.eval(-2)),'p_minus5':str(p.eval(-5)),
              'p_minus6':str(p.eval(-6)),
              'H_trace':str(sp.trace(H)),'H2_trace':str(sp.trace(H*H)),
              'determinant_nonzero_surviving_roots':all(p.eval(v)!=0 for v in [-2,-5,-6])})
assert gcd==sp.Poly(1,x,domain=sp.QQ)
assert rows[-1]['determinant_nonzero_surviving_roots']
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'input_sha256':hashlib.sha256((D/'CUBE_POINT_SPECTRUM_RESULTS.json').read_bytes()).hexdigest(),
 'tree_incidence_determinant':str(Bt.det()),'physical_hop_gauss_checks':gauss_count,
 'legal_P_to_Q_hops':len(transitions),'rows':rows,
 'scope':'Second author implementation; exact finite certificate plus separate analytic proof. Not independent scientific review.'}
p=D/'CUBE_CERTIFICATE_CONTROLS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
