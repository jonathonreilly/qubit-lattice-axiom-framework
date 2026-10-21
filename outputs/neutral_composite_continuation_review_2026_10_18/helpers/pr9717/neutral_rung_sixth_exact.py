"""Exact Q(sqrt(2),i) sixth-order matrix element in the existing four-rung model."""
from pathlib import Path
from neutral_rung_model import h,Ds
P=Path(__file__).resolve().parent
import sympy as s
hh=s.Matrix(h.astype(int));dd=[s.Matrix(d.astype(int)) for d in Ds];cols=[];es=[]
for e,m,vs in sorted(hh.eigenvects(),key=lambda v:float(v[0])):
 vv=s.GramSchmidt(vs,orthonormal=False)
 cols+=vv;es +=[e]*len(vv)
S=s.Matrix.hstack(*cols);Si=S.inv();de=[s.simplify(Si*d*S) for d in dd];gram=S.T*S
t1=s.sqrt(2)*(Si*dd[0]*dd[1]*S)[:2,:2];t2=s.sqrt(2)*(Si*dd[0]*dd[2]*S)[:2,:2];t3=s.simplify(-s.I*t1*t2)
print('e',es,'gram',list(gram.diagonal()),'t3',t3,'eig',t3.eigenvects(),flush=True)
import itertools,time,json
F=s.QQ.algebraic_field(s.sqrt(2),s.I);zero=F.zero;one=F.one
v=-sum((s.kronecker_product(d,d) for d in de),s.zeros(64))
cols=[[(a,F.from_sympy(s.expand(v[a,b]))) for a in range(64) if v[a,b]!=0] for b in range(64)]
L=4;digits=list(itertools.product(range(8),repeat=L)); powers=[8**(L-1-i) for i in range(L)]
labels=[-1,-1,0,0,0,0,1,1]
resolvents=[zero]+[F.from_sympy(-1/(2*s.sqrt(2)*j)) for j in range(1,9)]
rr=[resolvents[4+sum(labels[i] for i in bits)] for bits in digits]
assert hh*S==S*s.diag(*es)
assert gram==s.diag(8,4,2,2,2,2,8,4)
assert s.simplify(t3*t3)==s.eye(2)
uv=t3.eigenvects()[1][2][0];dv=t3.eigenvects()[0][2][0]
localdown=[F.from_sympy(dv[i]) for i in range(2)];localbra=[F.from_sympy(s.conjugate(uv[i])*gram[i,i]) for i in range(2)]
lowids=[sum(b*p for b,p in zip(bits,powers)) for bits in itertools.product(range(2),repeat=4)]
def mul(vs):
 a=one
 for b in vs:a*=b
 return a
start={idx:mul(localdown[b] for b in digits[idx]) for idx in lowids};bra={idx:mul(localbra[b] for b in digits[idx]) for idx in lowids}
def apply(x):
 out={}
 for idx,c in x.items():
  bits=digits[idx]
  for j in range(3):
   old=8*bits[j]+bits[j+1]
   for new,coeff in cols[old]:
    target=idx+(new//8-bits[j])*powers[j]+(new%8-bits[j+1])*powers[j+1]
    out[target]=out.get(target,zero)+coeff*c
 return {i:c for i,c in out.items() if c}
a=[start];bs={};clock=time.monotonic()
for n in range(1,7):
 out=apply(a[-1]);proj={i:out.get(i,zero) for i in lowids};diag=proj[lowids[-1]]/start[lowids[-1]]
 off=sum((bra[i]*proj[i] for i in lowids),zero)/F.from_sympy(s.Integer(8)**4)
 print('order',n,'bra up/down',F.to_sympy(off),'seconds',time.monotonic()-clock,flush=True)
 if n<6:
  assert all(proj[i]==diag*start[i] for i in lowids)
  bs[n]=diag
  for j in range(1,n):
   if not bs[j]:continue
   for i,c in a[n-j].items():out[i]=out.get(i,zero)-c*bs[j]
  a.append({i:rr[i]*c for i,c in out.items() if c and rr[i]})
 else:
  assert s.simplify(F.to_sympy(off)+63/(128*s.sqrt(2)))==0
  (P/'neutral_rung_sixth_exact.json').open('w').write(json.dumps(dict(coefficient=str(F.to_sympy(off)),seconds=time.monotonic()-clock,field=str(F),lower_coefficients={str(n):str(F.to_sympy(x)) for n,x in bs.items()},scope='Exact specified finite-band off-diagonal coefficient; canonical equivalence and charge obstruction proved in note.'),indent=2))
