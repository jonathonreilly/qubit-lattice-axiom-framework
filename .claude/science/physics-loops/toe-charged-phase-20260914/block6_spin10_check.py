import numpy as np
from functools import reduce
from itertools import combinations
I=np.eye(2,dtype=complex);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]).astype(complex)
def kron(xs):return reduce(np.kron,xs)
gamma=[kron([I]*k+[s]+[Z]*(4-k)) for k in range(5) for s in (X,Y)]
P=np.where(np.diag(kron([Z]*5)).real>0)[0]
gen=[(.5j*gamma[a]@gamma[b])[np.ix_(P,P)] for a,b in combinations(range(10),2)]
C=kron([Y,X,Y,X,Y]);M=[(C@g)[np.ix_(P,P)] for g in gamma]
assert all(np.max(abs(m-m.T))<1e-14 for m in M)
cas=sum(t@t for t in gen);assert np.max(abs(cas-45/4*np.eye(16)))<1e-14
C2=2*np.kron(cas,np.eye(16))+2*sum(np.kron(t,t) for t in gen)
print('tensor Casimir',np.unique(np.round(np.linalg.eigvalsh(C2),8),return_counts=True))
sym=[];anti=[]
for i in range(16):
 v=np.zeros(256);v[16*i+i]=1;sym.append(v)
 for j in range(i+1,16):
  v=np.zeros(256);v[16*i+j]=1/np.sqrt(2);v[16*j+i]=1/np.sqrt(2);sym.append(v)
  v=v.copy();v[16*j+i]*=-1;anti.append(v)
for label,vs in [('symmetric',sym),('antisymmetric',anti)]:
 V=np.array(vs).T;print(label,np.unique(np.round(np.linalg.eigvalsh(V.T@C2@V),8),return_counts=True))
coef={}
for a,c in combinations(range(16),2):
 for b,d in combinations(range(16),2):
  v=sum(m[a,b]*m[c,d]-m[a,d]*m[c,b] for m in M)
  if abs(v)>1e-12:coef[(a,c,b,d)]=v
print('quartic nonzero coefficients',len(coef),'first',list(coef.items())[:8])
intertwiner_error=0.
for (a,b),t in zip(combinations(range(10),2),gen):
 for c in range(10):
  expected=1j*((M[b] if c==a else np.zeros((16,16)))-(M[a] if c==b else np.zeros((16,16))))
  err=t.T@M[c]+M[c]@t-expected
  assert np.array_equal(err,np.zeros((16,16)))
  intertwiner_error=max(intertwiner_error,float(np.max(abs(err))))
I256=np.eye(256);poly=(C2-9*I256)@(C2-21*I256)@(C2-25*I256)
assert np.array_equal(poly,np.zeros((256,256)))
multiplicities={}
for value in (9,21,25):
 other=[a for a in (9,21,25) if a!=value];p=(C2-other[0]*I256)@(C2-other[1]*I256)
 multiplicities[value]=int(round(np.trace(p).real/((value-other[0])*(value-other[1]))))
assert multiplicities=={9:10,21:120,25:126}
g=np.diag([1.,-1.]+[0.]*14);extra=np.kron(g,np.eye(16))+np.kron(np.eye(16),g)
assert np.linalg.norm(C2@extra-extra@C2)>1
omega={a:-2*c for a,c in coef.items()};bound=2*sum(abs(c) for c in omega.values())
assert omega[(0,1,14,15)]!=0
print('exact intertwiner identities',intertwiner_error,'exact Casimir multiplicities',multiplicities,'quartic norm bound',bound)
from collections import defaultdict
omega_create={(a,c,16+b,16+d):np.conj(v) for (a,c,b,d),v in omega.items()}
for t in gen:
 action=defaultdict(complex)
 for ids,value in omega_create.items():
  for slot,src in enumerate(ids):
   block,alpha=divmod(src,16)
   for beta in np.nonzero(t[:,alpha])[0]:
    changed=list(ids);changed[slot]=16*block+int(beta)
    if len(set(changed))<4:continue
    inv=sum(changed[a]>changed[b] for a in range(4) for b in range(a+1,4))
    action[tuple(sorted(changed))]+=value*t[beta,alpha]*(-1)**inv
 assert all(v==0 for v in action.values())
print('exact exterior fourth-power Spin(10) invariance verified for all 45 generators')
