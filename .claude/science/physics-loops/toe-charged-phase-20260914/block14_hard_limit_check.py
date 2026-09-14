import itertools
import numpy as np

sites=list(itertools.product(range(2),repeat=3));si={p:i for i,p in enumerate(sites)}
edges=[(p,i) for p in sites for i in range(3) if p[i]==0];ei={e:i for i,e in enumerate(edges)}
faces=[(p,i,j) for p in sites for i,j in ((0,1),(0,2),(1,2)) if p[i]==p[j]==0];fi={f:i for i,f in enumerate(faces)}
def advance(p,i):
 q=list(p);q[i]+=1;return tuple(q)
G=np.zeros((12,8),int);F=np.zeros((6,12),int)
for r,(p,i) in enumerate(edges):G[r,si[advance(p,i)]]=1;G[r,si[p]]=-1
for r,(p,i,j) in enumerate(faces):
 for e,s in (((p,i),1),((advance(p,i),j),1),((advance(p,j),i),-1),((p,j),-1)):F[r,ei[e]]+=s
D=np.zeros(6,int);p=(0,0,0)
for f,s in (((advance(p,0),1,2),1),((p,1,2),-1),((advance(p,1),0,2),-1),((p,0,2),1),((advance(p,2),0,1),1),((p,0,1),-1)):D[fi[f]]+=s
assert np.max(abs(F@G))==0 and np.max(abs(D@F))==0
allb=np.array(list(itertools.product((-1,0,1),repeat=6)));charges=allb@D
physical=allb[charges%3==0];pi={tuple(b):i for i,b in enumerate(physical)};q=physical@D
assert len(physical)==243
zero=np.flatnonzero(q==0);assert len(zero)==141
Z=np.zeros((243,243));finite=np.zeros_like(Z);mu=2.3;t=.7
for i,b in enumerate(physical):
 for l in range(12):
  for sig in (-1,1):
   raw=b+sig*F[:,l];bp=(raw+1)%3-1;j=pi[tuple(bp)];m=(bp-raw)//3
   finite[j,i]+=t*np.exp(-mu*sum(m*m))
   if np.all(m==0):Z[j,i]+=t
assert np.max(abs(Z-Z.T))==0 and np.max(abs(finite-finite.T))<1e-12
assert np.max(abs((q[:,None]-q[None,:])*Z))==0
assert np.max(abs((q[:,None]-q[None,:])*finite))>1e-3
assert np.max(np.sum(abs(finite-Z),axis=1))<=24*t*np.exp(-mu)+1e-12
plus=np.array([[0,0,0],[1,0,0],[0,1,0]]);minus=plus.T;eye=np.eye(3)
tensor=np.zeros((729,729))
for l in range(12):
 for sig in (-1,1):
  term=np.array([[1.]])
  for r in range(6):
   c=sig*F[r,l];term=np.kron(term,plus if c==1 else minus if c==-1 else eye)
  tensor+=t*term
zero_all=np.flatnonzero(charges==0)
assert np.max(abs(tensor[np.ix_(zero_all,zero_all)]-Z[np.ix_(zero,zero)]))<1e-12
assert np.max(abs(1-np.cos(2*np.pi*allb/3)-1.5*allb**2))<1e-12
print('One cube: 243 physical mod3 flux states, 141 integer-neutral states; exact tensor-shift mapping, finite-penalty charge changes, rate bound and diagonal potential checked. No phase or stability proof.')
# Independent two-state variational comparison against the complete physical matrix.
K=.8;lam=.6;E=len(edges)
H=2*t*E*np.eye(243)-Z+np.diag(1.5*K*np.sum(physical**2,axis=1)+lam*(q/3)**2)
i=pi[(0,)*6];j=pi[tuple(F[:,0])];r=np.count_nonzero(F[:,0])
trial=H[np.ix_([i,j],[i,j])];upper=np.linalg.eigvalsh(trial)[0]
expected=2*t*E+.75*K*r-np.sqrt((.75*K*r)**2+t*t)
assert upper<=expected+1e-12 and upper<2*t*E
frozen=np.flatnonzero(np.sum(abs(Z),axis=1)==0)
assert len(frozen)>0 and np.min(np.diag(H)[frozen])>=2*t*E
assert np.linalg.eigvalsh(H)[0]<=upper+1e-12
print('Two-state neutral variational energy lies strictly below every frozen basis energy; frozen states counted:',len(frozen),'. This does not establish phase or thermodynamic sector selection.')
