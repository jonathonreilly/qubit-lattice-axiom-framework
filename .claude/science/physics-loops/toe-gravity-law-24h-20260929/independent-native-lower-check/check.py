#!/usr/bin/env python3
"""Independent literal hard-core, scalar-pin and filtered-form controls."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import itertools,collections,time,json,math,resource,signal,hashlib
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
signal.alarm(90);resource.setrlimit(resource.RLIMIT_CPU,(30,31))
start=time.monotonic();cpu=time.process_time();rng=np.random.default_rng(13092026)
E=[(1,0,0),(0,1,0),(0,0,1)];O=(0,0,0)
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
neg=lambda x:tuple(-a for a in x)
scale=lambda s,x:tuple(s*a for a in x)
D={scale(s*2,x) for x in E for s in (-1,1)}|{add(scale(s,E[i]),scale(t,E[j])) for i,j in itertools.combinations(range(3),2) for s,t in itertools.product((-1,1),repeat=2)}
DP=[scale(2,x) for x in E]+[add(E[i],scale(r,E[j])) for i,j in itertools.combinations(range(3),2) for r in (1,-1)]
words=[[(E[0],neg(E[0]),1),(E[1],neg(E[1]),-1)],[(E[0],neg(E[0]),1),(E[1],neg(E[1]),1),(E[2],neg(E[2]),-2)]]
words += [[(scale(s,E[i]),scale(t,E[j]),s*t) for s,t in itertools.product((-1,1),repeat=2)] for i,j in itertools.combinations(range(3),2)]
weights=[F(1,2),F(1,6),F(1,4),F(1,4),F(1,4)]
def grad(v):
 return 6*sum(x*x for x in v.values())-2*sum(a*v.get(add(x,e),F(0)) for x,a in v.items() for e in E)
def energy(psi):
 n=len(next(iter(psi)));norm=sum(z*z for z in psi.values());v3=F(0);diag=F(0);qr=collections.defaultdict(lambda:collections.defaultdict(F))
 for S,z in psi.items():
  for x in S:
   m=sum(add(x,d) in S for d in D);v3+=z*z*F(m*(m-1),2);diag+=z*z*F((m-1)*(m-2),2)
  centers={add(x,scale(s,e)) for x in S for e in E for s in (-1,1)}
  for x in centers:
   for a,wa in enumerate(words):
    for u,v,c in wa:
     pair=frozenset((add(x,u),add(x,v)))
     if pair<=S:qr[a,S-pair][x]+=c*z
 q=[F(0)]*5;w=F(0)
 for (a,eta),field in qr.items():q[a]+=weights[a]*sum(z*z for z in field.values());w+=weights[a]*grad(field)
 return n*norm-2*sum(q[:2])-sum(q[2:])+v3+w,diag
cases=[]
for n in (3,4,6):
 sites=list(itertools.product(range(-1,3),repeat=3));psi={frozenset(sites[i] for i in rng.choice(len(sites),size=n,replace=False)):F(int(rng.integers(-4,5)) or 1,7) for _ in range(18)}
 fibers=collections.defaultdict(dict)
 for S,z in psi.items():
  for x in S:
   for d in DP:
    y=add(x,d)
    if y in S:
     pair=frozenset((x,y));fibers[S-pair][pair]=z
 h,diag=energy(psi);tk=sum(energy(f)[0] for f in fibers.values());assert h==diag+tk
 eg=F(0)
 for eta,f in fibers.items():
  fields=collections.defaultdict(dict)
  for pair,z in f.items():
   x,y=tuple(pair);d=add(y,neg(x))
   if d not in DP:x,y=y,x;d=neg(d)
   fields[DP.index(d)][x]=z
  eg+=sum(grad(v) for v in fields.values())
  assert all(x not in eta for f0 in fields.values() for x in f0)
 assert h>=diag+eg/12
 cases.append({'N':n,'input_words':len(psi),'residual_fibers':len(fibers),'energy':str(h),'D':str(diag),'bare_gradient':str(eg),'identity_defect':'0'})
# Actual zero-mode frame and all symmetric incoming directions.
U=np.zeros((9,5));U[:3,0]=np.array([1,-1,0])/np.sqrt(2);U[:3,1]=np.array([1,1,-2])/np.sqrt(6)
for j in range(3):U[3+2*j:5+2*j,2+j]=np.array([-1,1])/np.sqrt(2)
assert np.max(abs(U.T@U-np.eye(5)))<1e-14
normerrors=[]
for i in range(5):
 for j in range(i,5):
  Z=np.zeros((5,5));Z[i,j]=1 if i==j else 1/np.sqrt(2)
  if i!=j:Z[j,i]=1/np.sqrt(2)
  literal=np.zeros((9,9))
  for d,e in itertools.product(range(9),repeat=2):
   literal[d,e]=sum(Z[a,b]*(U[d,a]*U[e,b]+U[e,a]*U[d,b]) for a,b in itertools.product(range(5),repeat=2))/np.sqrt(2)
  assert np.max(abs(literal-np.sqrt(2)*U@Z@U.T))<1e-14
  normerrors.append(abs(np.sum(literal*literal)-2))
assert max(normerrors)<1e-13
# Independent scalar hard-core one-pin capacity on finite Dirichlet boxes.
caps=[]
for radius in (1,2,3,4,6):
 points=list(itertools.product(range(-radius,radius+1),repeat=3));index={x:i for i,x in enumerate(points)};L=lil_matrix((len(points),len(points)))
 for x,i in index.items():
  L[i,i]=6
  for e in E:
   for s in (-1,1):
    y=add(x,scale(s,e))
    if y in index:L[i,index[y]]=-1
 L=L.tocsr();rhs=np.zeros(len(points));rhs[index[O]]=1;green=spsolve(L,rhs);g=green[index[O]];u=-green/g
 en=u@(L@u);assert abs(u[index[O]]+1)<1e-14 and abs(en-1/g)<1e-11
 assert g<=np.sqrt(3)*np.pi/8
 caps.append({'radius':radius,'points':len(points),'G00':g,'capacity':en})
# Forward-edge coordinate matrix derived directly from actual Q words.
length=5;modes=np.array(list(itertools.product(range(length),repeat=3)));ks=2*np.pi*np.where(modes<=length//2,modes,modes-length)/length;V=length**3
K=[];G=[];chi=[];banddef=0
for k in ks:
 ell=2*sum(1-np.cos(k));Q=np.zeros((5,9),complex);Q[0,:3]=np.exp(-1j*k)*np.array([1,-1,0])/np.sqrt(2);Q[1,:3]=np.exp(-1j*k)*np.array([1,1,-2])/np.sqrt(6)
 for j,(i,l) in enumerate(itertools.combinations(range(3),2)):
  for t,r in enumerate((1,-1)):Q[j+2,3+2*j+t]=-r*(np.exp(-1j*k[i])+np.exp(-1j*r*k[l]))/2
 mat=2*np.eye(9)-2*Q[:2].conj().T@Q[:2]-Q[2:].conj().T@Q[2:]+ell*Q.conj().T@Q
 ev,vec=np.linalg.eigh(mat);assert min(ev)>=ell/12-1e-13
 c=0 if np.linalg.norm(k)<1e-8 else (0.4 if np.linalg.norm(k)<2.1 else 1.)
 inv=(vec*np.where(ev>1e-10,1/np.maximum(ev,1e-10),0))@vec.conj().T
 K.append(mat);G.append(c*inv);chi.append(c)
K=np.array(K);G=np.array(G);chi=np.array(chi)
f=rng.normal(size=(length,length,length,9))+1j*rng.normal(size=(length,length,length,9));f[0,0,0]=0
fh=np.fft.fftn(f,axes=(0,1,2),norm='ortho').reshape(V,9);ph=(1-chi[:,None])*fh
r=np.sum(ph,axis=0)/np.sqrt(V);M=np.sum(G,axis=0)/V;coeff=np.linalg.solve(M,r)
q=-np.einsum('kij,j->ki',G,coeff)/np.sqrt(V)
assert np.max(abs(np.sum(q,axis=0)/np.sqrt(V)+r))<1e-12
used=np.einsum('ki,kij,kj,k->',fh.conj(),K,fh,chi).real
cap=np.vdot(r,coeff).real
positive=chi>0
completion=np.sum([np.vdot(q[j],K[j]@q[j]).real/chi[j] for j in np.flatnonzero(positive)])
wrong=np.vdot(r,np.linalg.solve(np.sum(G*chi[:,None,None],axis=0)/V,r)).real
assert abs(completion-cap)<1e-11 and used>=cap and abs(wrong-cap)>1e-4
result={'scope':'Independent finite controls; no thermodynamic or EOS theorem inferred','all_N_literal':cases,'symmetric_channels':len(normerrors),'incoming_norm_max_error':max(normerrors),'scalar_one_pin':caps,'smooth_split_control':{'L':length,'transition_modes':int(sum((chi>0)&(chi<1))),'used_energy':used,'capacity':cap,'completion':completion,'wrong_chi_squared_capacity':wrong},'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
