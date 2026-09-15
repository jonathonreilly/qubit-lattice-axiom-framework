import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import numpy as np,itertools,json,math
from scipy.linalg import expm
from pathlib import Path
checks=[];rows=[]
def ck(n,v):assert v,n;checks.append(n)
for m in [2,3,4,5]:
 edges=[(i,i+1) for i in range(m-1)]+[(i,m+i) for i in range(m)]+[(0,2*m)]
 counts={}
 for bits in itertools.product([0,1],repeat=2*m):
  occ=[0]*(2*m+1)
  for (a,b),bit in zip(edges,bits):occ[a]^=bit;occ[b]^=bit
  key=tuple(occ[m:2*m]),tuple(occ[:m]);counts[key]=counts.get(key,0)+1
  ck(f'parity m{m} '+str(bits),sum(occ)%2==0)
 ck(f'all ready/matter bijections m{m}',len(counts)==2**(2*m) and set(counts.values())=={1})
for m,coupling_sets in [(2,[(1.,)])]:
 M=2*m+1;basis=[b for b in range(2**M) if b.bit_count()%2==0];index={b:i for i,b in enumerate(basis)};dim=len(basis);I=np.eye(dim)
 occ=np.array([[(b>>j)&1 for j in range(M)] for b in basis]);ns=[np.diag(occ[:,j]) for j in range(M)]
 def hop(a,b):
  A=np.zeros((dim,dim),complex)
  for j,v in enumerate(basis):
   for to,fr in [(a,b),(b,a)]:
    if (v>>fr)&1 and not (v>>to)&1:
     mid=v^(1<<fr);sgn=(-1)**((v&((1<<fr)-1)).bit_count()+(mid&((1<<to)-1)).bit_count());A[index[mid^(1<<to)],j]+=sgn
  return A
 ts=[hop(i,i+1) for i in range(m-1)];leaf=[hop(i,m+i) for i in range(m)]
 for couplings in coupling_sets:
  h=np.zeros((m,m))
  for j,c in enumerate(couplings):h[j,j+1]=h[j+1,j]=c
  eps,O=np.linalg.eigh(h)
  if np.linalg.det(O)<0:O[:,0]*=-1
  V=np.zeros((dim,dim))
  for j,b in enumerate(basis):
   cols=[i for i in range(m) if (b>>i)&1]
   for i,a in enumerate(basis):
    if a>>m!=b>>m:continue
    rr=[k for k in range(m) if (a>>k)&1]
    if len(rr)==len(cols):V[i,j]=np.linalg.det(O[np.ix_(rr,cols)]) if rr else 1
  H=sum((c*t for c,t in zip(couplings,ts)),np.zeros((dim,dim)))
  ck('exterior diagonalization'+str(couplings),np.linalg.norm(V@sum((e*n for e,n in zip(eps,ns)),np.zeros((dim,dim)))@V.T-H)<1e-12)
  ready=(eps<0).astype(int);ix=np.flatnonzero(np.all(occ[:,m:2*m]==ready,axis=1));Q=I[:,ix];ck('ready rank'+str(couplings),len(ix)==2**m)
  for beta in [2*math.log(5/3)]:
   branch={'':V.T@Q}
   for j,e in enumerate(eps):
    r=np.exp(-beta*abs(e)/2);U=expm(-1j*math.acos(r)*leaf[j]);new={}
    for key,K in branch.items():
     for bit in [0,1]:new[key+str(bit)]=(ns[m+j] if bit else I-ns[m+j])@U@K
    branch=new
   branch={k:V@K for k,K in branch.items()};key=''.join(map(str,ready));K=branch[key];pref=np.exp(-beta*np.sum(abs(eps[eps<0]))/2);target=pref*expm(-beta*H/2)@Q
   tag=str((m,couplings,beta));err=np.linalg.norm(K-target);ck('Kraus'+tag,err<1e-12);ck('complete'+tag,np.linalg.norm(sum(A.conj().T@A for A in branch.values())-np.eye(2**m))<1e-12)
   prob=np.trace(K.conj().T@K).real/(2**m);ck('probability'+tag,abs(prob-np.prod((1+np.exp(-beta*abs(eps)))/2))<1e-12)
   ck('dimer success rational',abs(prob-289/625)<1e-12);ck('dimer failure weights',np.allclose(sorted(np.trace(v.conj().T@v).real/4 for k,v in branch.items() if k!=key),sorted([136/625,64/625,136/625]),atol=1e-12))
   rows.append(dict(m=m,couplings=couplings,beta=beta,kraus_residual=err,success=prob,outcomes=len(branch)))
# Encoded sector independent 4x4 logical matrix with energies 0,+/-1,2.
import sympy as s
r=s.Rational(3,5);weights=[r*r,1,r**4,r**6];Z=sum(weights)
ck('encoded probability',Z/4==s.Rational(6001,15625));ck('encoded energy',(-1+r**4+2*r**6)/Z==-s.Rational(6071,12002));ck('encoded hopping',(-1+r**4)/Z==-s.Rational(200,353))
for a,b in itertools.product([0,1],repeat=2):
 c=1-((a+b)%2);ck('encoded quadratic'+str((a,b)),a*b==s.Rational(a+b+c-1,2))
Path('/private/tmp/review-drain-20260915/check8036/dimer_independent.json').write_text(json.dumps(dict(checks=len(checks),rows=rows,route='Independent CAR bit signs,exterior minors,direct matrix exponential; no author QR or native Pauli construction imported'),indent=2));print('TOTAL: PASS='+str(len(checks))+' FAIL=0')
