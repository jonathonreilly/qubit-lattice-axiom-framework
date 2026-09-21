#!/usr/bin/env python3
"""Exact finite-word certificate and full-ring Gibbs/current controls."""
from pathlib import Path
from itertools import product
import hashlib,json
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix

HERE=Path(__file__).resolve().parent;checks=[]
def check(name,condition,detail=None):
 assert bool(condition),(name,detail)
 checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
z,k=s.symbols('z kappa',positive=True)
rates={(0,0):k,(1,1):k,(0,1):2*k*z/(1+z),(1,0):2*k/(1+z)}
h={(0,0,0):0,(0,0,1):0,(0,1,0):-k,(0,1,1):-2*k/(1+z),
   (1,0,0):0,(1,0,1):k*(z-1)/(1+z),(1,1,0):-2*k/(1+z),(1,1,1):-2*k/(1+z)}
for a,b,c,d in product(range(2),repeat=4):
 residual=int(b==0 and c==1)*rates[a,d]*z**(a-d)-int(b==1 and c==0)*rates[a,d]
 assert s.factor(residual-h[a,b,c]+h[b,c,d])==0,(a,b,c,d)
check('sixteen_word_exact_stationarity_coboundary',True)

def ring(N,q,classes,J,chemical):
 states=np.array(list(product(range(q),repeat=N)));index={tuple(v):i for i,v in enumerate(states)};size=len(states)
 sig=classes[states];H=-J*np.sum(sig*np.roll(sig,-1,axis=1),axis=1)
 logp=-H+chemical[states].sum(axis=1);pi=np.exp(logp-logp.max());pi/=pi.sum()
 rate=np.array([[1,2*np.exp(J)/(1+np.exp(J))],[2/(1+np.exp(J)),1]])
 rows=[];cols=[];vals=[];current=np.zeros(size)
 for x in range(N):
  y=(x+1)%N;source=np.flatnonzero((sig[:,x]==1)&(sig[:,y]==0))
  dststates=states[source].copy();dststates[:,[x,y]]=dststates[:,[y,x]]
  dst=np.array([index[tuple(v)] for v in dststates]);r=rate[sig[source,(x-1)%N],sig[source,(x+2)%N]]
  rows.extend([dst,source]);cols.extend([source,source]);vals.extend([r,-r]);current[source]+=r/N
  # Within-class symmetric exchanges preserve fine-label Gibbs weights.
  source=np.flatnonzero((sig[:,x]==sig[:,y])&(states[:,x]!=states[:,y]))
  dststates=states[source].copy();dststates[:,[x,y]]=dststates[:,[y,x]]
  dst=np.array([index[tuple(v)] for v in dststates]);r=np.full(len(source),.7)
  rows.extend([dst,source]);cols.extend([source,source]);vals.extend([r,-r])
 L=coo_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(size,size)).tocsr()
 residual=float(max(abs(L@pi)));j=float(pi@current)
 assert residual<2e-16 and j>0,(N,q,residual,j)
 for label in range(q):assert max(abs(L.T@np.sum(states==label,axis=1)))<2e-14
 rho=float(pi@sig[:,0]);cov=float(pi@(sig[:,0]*sig[:,1])-rho*rho)
 return dict(N=N,labels=q,states=size,J=J,current=j,density=rho,adjacent_covariance=cov,stationarity_residual=residual)

binary=[]
for N in (4,5,7,10):
 for J in (-.9,0,np.log(2)):
  result=ring(N,2,np.array([0,1]),J,np.array([0,.31]));binary.append(result)
  if J==0:assert abs(result['current']-result['density']*(1-result['density']))<2e-15
  else:assert abs(result['adjacent_covariance'])>1e-3
check('whole_binary_rings_correlated_Gibbs_and_nonzero_current',True,binary)
fine=[ring(5,4,np.array([0,0,1,1]),J,np.array([-.2,.1,.35,-.07])) for J in (-.9,np.log(2))]
check('four_fine_labels_full_generator_invariance',True,fine)

comparisons=[]
for J in (-.9,0,np.log(2)):
 mu=.31;T=np.array([[np.exp(J*a*b+mu*(a+b)/2) for b in range(2)] for a in range(2)])
 eig,vectors=np.linalg.eigh(T);Lambda=eig[-1];v=vectors[:,-1]
 if v[0]<0:v=-v
 assert np.min(v)>0
 P=T*v[None,:]/(Lambda*v[:,None]);stationary=v*v;rho=stationary[1];u=eig[0]/Lambda
 assert max(abs(P.sum(axis=1)-1))<1e-15 and max(abs(stationary@P-stationary))<1e-15
 four=np.array([[[[v[a]*T[a,b]*T[b,c]*T[c,d]*v[d]/Lambda**3 for d in range(2)] for c in range(2)] for b in range(2)] for a in range(2)])
 assert abs(four.sum()-1)<1e-15
 rate=np.array([[1,2*np.exp(J)/(1+np.exp(J))],[2/(1+np.exp(J)),1]])
 current=sum(four[a,1,0,d]*rate[a,d] for a,d in product(range(2),repeat=2))
 for distance in (0,1,2,5,11):
  covariance=rho*np.linalg.matrix_power(P,distance)[1,1]-rho*rho
  assert abs(covariance-rho*(1-rho)*u**distance)<1e-15
 assert current>0
 finite=next(x for x in binary if x['N']==10 and x['J']==J)
 T7=np.linalg.matrix_power(T,7);Z10=np.trace(np.linalg.matrix_power(T,10))
 finite_transfer=sum(T[a,1]*T[1,0]*T[0,d]*T7[d,a]*rate[a,d]/Z10 for a,d in product(range(2),repeat=2))
 assert abs(finite_transfer-finite['current'])<2e-15
 comparisons.append(dict(J=J,current=float(current),density=float(rho),correlation_eigenvalue=float(u),N10_current_error=abs(current-finite['current'])))
check('positive_transfer_matrix_current_and_correlation',True,comparisons)

# Fine-label orbit averaging does not magically transfer scalar correlations
# into the zero-mean vector observables.
axis=[np.array(v,float) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
cube=[np.array(v,float) for v in product((-1,1),repeat=3)]
assert np.all(sum(axis)==0) and np.all(sum(cube)==0)
for left,right in product([axis,cube],repeat=2):
 assert np.all(sum(np.outer(a,b) for a in left for b in right)==0)
check('scalar_orbit_correlations_do_not_create_raw_vector_covariance',True)

(HERE/'GIBBS_TRANSPORT_1D_RESULTS.json').write_text(json.dumps(dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,scope='Reconstruction of established one-dimensional KLS/Gibbs transport; exact finite-word proof and finite generator controls, not a 3D wave or continuum theorem.'),indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
