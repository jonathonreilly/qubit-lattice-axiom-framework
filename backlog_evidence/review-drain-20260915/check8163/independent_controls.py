"""Small independent mathematical controls; never imports or executes PR programs."""
import numpy as np
from scipy.integrate import quad
import json, hashlib
from pathlib import Path
rng=np.random.default_rng(8163)
rows=[]
for rank in [1,2,3]:
 for nt in [1,2,4]:
  Xs=[]; As=[]; Ds=[]; full=np.zeros((2*rank*nt,2*rank*nt),complex)
  for t in range(nt):
   def pos():
    z=rng.normal(size=(rank,rank))+1j*rng.normal(size=(rank,rank))
    return np.eye(rank)+.07*z.conj().T@z
   A,D=pos(),pos();B=.11*(rng.normal(size=(rank,rank))+1j*rng.normal(size=(rank,rank)))
   di=np.linalg.inv(D);X=np.block([[A+B@di@B.conj().T,B@di],[di@B.conj().T,di]])
   assert np.min(np.linalg.eigvalsh(X))>0
   u=slice(2*rank*t,2*rank*t+rank);v=slice(2*rank*t+rank,2*rank*(t+1))
   full[u,u]=A;full[u,v]=B;full[v,u]=-B.conj().T;full[v,v]=D
   if t+1<nt:full[u,slice(2*rank*(t+1),2*rank*(t+1)+rank)]=-np.eye(rank)
   if t:full[v,slice(2*rank*(t-1)+rank,2*rank*t)]=-np.eye(rank)
   Xs.append(X);As.append(A);Ds.append(D)
  product=np.eye(2*rank,dtype=complex);chron=product.copy()
  for x in Xs:product=x@product;chron=np.linalg.solve(x,chron)
  direct=np.linalg.det(full)
  forward=np.prod([np.linalg.det(x) for x in Ds])*np.linalg.det(product[:rank,:rank])
  complement=np.prod([np.linalg.det(x) for x in As])*np.linalg.det(np.linalg.inv(product)[rank:,rank:])
  chrono=np.prod([np.linalg.det(x) for x in As])*np.linalg.det(chron[rank:,rank:])
  errs=[abs(direct-forward),abs(direct-complement),abs(abs(direct)-abs(chrono))]
  assert max(errs)<1e-10
  rows.append({'rank':rank,'slices':nt,'errors':errs})
rect=[]
for mu in [2.,6.,17.]:
 F=.7;k=.3
 integral=2*k*k*quad(lambda t: np.exp(-2*mu*t)*(np.cos(F*t)-1),0,np.inf,epsabs=1e-13)[0]
 formula=-k*k*F*F/(mu*(4*mu*mu+F*F))
 assert abs(integral-formula)<1e-13
 rect.append({'mu':mu,'quadrature':integral,'formula':formula,'error':abs(integral-formula)})
# The geometric weighted run sum is delta/(1+mu*delta-exp(b*delta));
# compare its denominator with delta*(mu-b*exp(b/mu)).
weighted=[]
for mu,k in [(7.,1.),(20.,.5),(2.,.1)]:
 b=(mu-6*k)/4;mb=mu-b*np.exp(b/mu)
 assert mb>6*k
 for delta in [1/mu,.03/mu,1e-5/mu]:
  den=mu*delta-np.expm1(b*delta)
  assert den>=delta*mb*(1-1e-12)
  weighted.append({'mu':mu,'delta':delta,'denominator_ratio':den/(delta*mb)})
out={'scope':'Nine small abstract block Schur/complementary determinants, independent Laplace quadrature, and weighted-run denominator controls; not primary evidence or a general proof.','block_identities':rows,'rectangle':rect,'weighted_runs':weighted,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(out,indent=2))
