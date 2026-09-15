import pathlib,json,itertools,time,math
import sympy as s
from fractions import Fraction as F
r=pathlib.Path(__file__).parent;p=r/'original-8059/.claude/science/physics-loops/native-l6-sixth-prefix-gap-certificate-20260908/live_inputs';start=time.monotonic()
a=json.loads((p/'ADJACENT_CENSUS.json').read_text());targets=json.loads((p/'TARGETS.json').read_text())['cases'];by={int(x['mask']):x for x in targets}
V=list(itertools.product(range(6),repeat=3));vi={v:i for i,v in enumerate(V)};black=[i for i,v in enumerate(V) if sum(v)%2==0];white=[i for i,v in enumerate(V) if sum(v)%2];bi={x:i for i,x in enumerate(black)};wi={x:i for i,x in enumerate(white)};B=s.zeros(108);edges=[]
for v in V:
 for axis in range(3):
  w=list(v);w[axis]=(w[axis]+1)%6;i,j=sorted((vi[v],vi[tuple(w)]));edges.append([i,j]);z=-(-1)**sum(v[:axis])
  if i in bi:B[bi[i],wi[j]]=z
  else:B[bi[j],wi[i]]=-z
assert edges==a['edges'];A=B*B.T;I=s.eye(108);pol=I
for lam in (3,6,9,12):pol=pol*(A-lam*I)
assert pol==s.zeros(108)
mults=s.Matrix([[x**k for x in (3,6,9,12)] for k in range(4)]).inv()*s.Matrix([s.trace(A**k) for k in range(4)]);assert list(mults)==[32,48,24,4]
first=min(int(x['mask']) for x in targets if x['singleton'] is None);external=min(int(x['mask']) for row in a['rows'] if row['bridge']==3 for x in row['prefixes'] if x['bridge_count']%2 and by[int(x['mask'])]['singleton'] is None)
rows=[]
for mask in [first,external]:
 D=B.copy()
 for e,(i,j) in enumerate(edges):
  if mask>>e&1:
   if i in bi:D[bi[i],wi[j]]*=-1
   else:D[bi[j],wi[i]]*=-1
 M=D*D.T+s.Rational(25,4)*I;inv=M.inv(method='DM');assert M*inv==I;tr=s.trace(inv)
 canon=F(72)+40*F(math.isqrt(3*10**60),10**30)+48*F(math.isqrt(6*10**60),10**30)
 upper=F(1323,10)+F(5,2)*(108-F(25,4)*F(int(tr.p),int(tr.q)));gap=canon-upper;assert gap==F(by[mask]['gap_lower']) and gap>F(1,3)
 rows.append({'mask':str(mask),'gap':str(gap),'direct108_inverse_residual':True})
result={'status':'PASS','baseline_exact_spectrum':list(map(int,mults)),'two_direct_full_inverses':rows,'seconds':time.monotonic()-start,'canonical_helpers_imported':False};(r/'control_gap.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
