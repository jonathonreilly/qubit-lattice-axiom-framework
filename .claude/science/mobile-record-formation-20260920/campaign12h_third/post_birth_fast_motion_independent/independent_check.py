from pathlib import Path
import hashlib,json,math,itertools
import numpy as np
from scipy.linalg import eigh,expm
from scipy.special import jv,j0
D=Path(__file__).resolve().parent
bg=(1,0,1,0,1,0); qstar=(1,-1,1,0,1,1); estar=(1,0,0,0,0,1); initial=(qstar,estar)
def valid(s):
 q,E=s;return all(E[i]-E[(i-1)%6]+bg[i]==q[i] for i in range(6))
def moves(s,S=None):
 q,E=s;out=[]
 for x in range(6):
  if q[x]==0:continue
  c=q[x]
  for step in (-1,1):
   y=(x+step)%6
   if q[y]!=0:continue
   e=x if step==1 else y
   shift=-c*step
   F=list(E);F[e]+=shift
   if S is not None and abs(F[e])>S:continue
   a=1. if S is None else math.sqrt(1-E[e]*(E[e]+shift)/(S*(S+1)))
   r=list(q);r[x]=0;r[y]=c;t=(tuple(r),tuple(F));assert valid(t)
   out.append((t,-a))
 return out
def h2next(s):
 out={}
 for z,a in moves(s):
  for w,b in moves(z):out[w]=out.get(w,0)-a*b
 assert out[s]==-2
 del out[s]
 assert len(out)==2 and all(v==-1 for v in out.values())
 return out
assert valid(initial)
# Derive the actual unnormalized B=-jT action from the initial ice vector.
vac=(bg,(0,)*6); formed=[]
for z,a in moves(vac):
 q,E=z
 if q[0]==q[1]==0:
  r=list(q);r[0]=1;r[1]=-1;F=list(E);F[0]+=1
  w=(tuple(r),tuple(F));assert valid(w);formed.append((w,-a))
assert formed==[(initial,1.)]
# Walk the unwrapped physical configuration graph, never a Fourier-fiber matrix.
route=[initial];prev=None;now=initial
for k in range(1,61):
 candidates=list(h2next(now))
 if prev is None:nxt=next(s for s in candidates if s[0][5]==0)
 else:nxt=next(s for s in candidates if s!=prev)
 route.append(nxt);prev,now=now,nxt
assert len(set(route))==61
assert all(s[0].index(0)==(3+2*k)%6 for k,s in enumerate(route))
assert len(set(s[0] for s in route[:15]))==15
assert route[15][0]==qstar
flux_delta=tuple(a-b for a,b in zip(route[15][1],estar))
assert flux_delta in [(3,)*6,(-3,)*6]
assert all(route[k+15][0]==route[k][0] for k in range(46))
assert all(tuple(a-b for a,b in zip(route[k+15][1],route[k][1]))==flux_delta for k in range(46))
# Every possible P word occurs; three flux components follow from holonomy +/-3.
words=[]
for hole in range(6):
 for minus in range(6):
  if hole==minus:continue
  q=[1]*6;q[hole]=0;q[minus]=-1;words.append(tuple(q))
assert set(s[0] for s in route[:15])=={q for q in words if q.index(0)%2==1}
# Finite-spin complete physical sector, independently from charge words plus E0.
finite=[]
for S in (1,2,4):
 states=[]
 for q in words:
  for e0 in range(-S,S+1):
   E=[e0]
   for i in range(1,6):E.append(E[-1]+q[i]-bg[i])
   s=(q,tuple(E))
   if max(map(abs,E))<=S:assert valid(s);states.append(s)
 ix={s:i for i,s in enumerate(states)};n=len(states)
 T=np.zeros((n,n));W=np.array([sum(1 for a in (0,2,4) if s[0][a]==0) for s in states])
 assert set(W)=={0,1}
 for i,s in enumerate(states):
  for z,a in moves(s,S):T[ix[z],i]+=a
 assert np.max(abs(T-T.T))==0
 pp=np.where(W==0)[0];qq=np.where(W==1)[0];A=T[np.ix_(qq,pp)]
 assert np.max(abs(T[np.ix_(pp,pp)]))==0 and np.max(abs(T[np.ix_(qq,qq)]))==0
 M=A.T@A;target_initial=np.zeros(len(pp));target_initial[list(pp).index(ix[initial])]=1
 full_initial=np.zeros(n);full_initial[ix[initial]]=1
 ev,V=eigh(M);peak=0.;rows=[]
 for eps in (.2,.1,.05):
  h=np.diag(W/eps**2)+T/eps;w,v=eigh(h)
  for u in (.5,1.,2.):
   exact=v@(np.exp(-1j*u*w)*(v.T@full_initial));low=V@(np.exp(1j*u*ev)*(V.T@target_initial));embedded=np.zeros(n,complex);embedded[pp]=low
   err=float(np.linalg.norm(exact-embedded));bound=4*eps+16*u*eps**2
   assert err<=bound+1e-12
   rows.append({'epsilon':eps,'u':u,'vector_error':err,'bound':bound})
 finite.append({'S':S,'dimension':n,'P_dimension':len(pp),'T_norm':float(np.linalg.norm(T,2)),'rows':rows})
# Independent finite path expm and infinite Bessel/roots filter at bounded times.
L=60;npath=np.arange(-L,L+1);H=-2*np.eye(2*L+1)-np.diag(np.ones(2*L),1)-np.diag(np.ones(2*L),-1)
w,v=eigh(H);seed=np.zeros(2*L+1);seed[L]=1
prob=[]
for u in (0.,.2,.5,1.,2.,3.):
 psi=v@(np.exp(-1j*u*w)*(v.T@seed));p=float(np.sum(abs(psi[npath%3==0])**2));b=float(np.sum(jv(npath[npath%3==0],2*u)**2));formula=float((1+2*j0(2*math.sqrt(3)*u))/3)
 assert abs(p-formula)<2e-13 and abs(b-formula)<2e-13
 prob.append({'u':u,'finite_path_return':p,'Bessel_sum':b,'formula':formula})
r={'actual_birth_output':{'q':qstar,'E':estar,'amplitude':1},'graph':{'distinct_P_words':15,'winding_increment':flux_delta,'first_16_physical_states':route[:16],'all_61_distinct':True},'finite_spin_full_sector_controls':finite,'probability_controls':prob,'scope':'Source-informed independently assembled legal-hop graph and finite matrices; no author builder, no macroscopic-time claim.'}
(D/'INDEPENDENT_RESULTS.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
