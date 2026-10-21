"""Direct 9-qubit Gibbs response control on an explicitly open graph.
Checks response expansion and sign, not bulk numerical coefficients.
"""
from pathlib import Path
import json,numpy as np
from compass_scalar import operator
P=Path(__file__).resolve().parent
sites=[(0,0,0),(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(2,0,0),(1,1,0)];ix={s:i for i,s in enumerate(sites)};b=[]
for x,i in ix.items():
 for a in range(3):
  y=list(x);y[a]+=1
  if tuple(y) in ix:b.append((i,ix[tuple(y)],a,1.))
H=operator((9,),b).toarray();ct=[];et=[]
for a in range(3):
 l=[0,0,0];r=l.copy();l[a]=-1;r[a]=1
 ct.append((ix[tuple(l)],ix[tuple(r)],a,1.));et.extend([(0,ix[tuple(l)],a,.5),(0,ix[tuple(r)],a,.5)])
C=operator((9,),ct).toarray();E=operator((9,),et).toarray()
assert np.linalg.norm(C-(2*E@E-3*np.eye(512)))<1e-11
v,U=np.linalg.eigh(H);C=U.conj().T@C@U;E=U.conj().T@E@U;delta=v[:,None]-v[None,:]
rows=[]
for t in [.02,.1,.3]:
 A=np.exp(1j*delta*t)*C;Adot=1j*delta*A
 Fprime=float(np.sum(v*np.diag(Adot@E+E@Adot)).real/(2*512))
 for beta in [.02,.01,.005,.0025]:
  p=np.exp(-beta*(v-v.min()));p/=p.sum();chi=float((1j*np.sum(p*np.diag(A@E-E@A))).real)
  row=dict(t=t,beta=beta,chi=chi,chi_over_beta_squared=chi/beta**2,Fprime=Fprime,absolute_error=abs(chi/beta**2-Fprime));rows.append(row);print(row,flush=True)
 for j in range(1,4):
  assert rows[-4+j]['absolute_error'] < .3*rows[-5+j]['absolute_error']+1e-10
 # Uniform energy source is an exact stationary-response null.
 assert abs(1j*np.sum(p*np.diag(A@np.diag(v)-np.diag(v)@A)))<1e-12
(P/'thermal_dense_control.json').write_text(json.dumps(dict(scope='9qubit open graph control, not bulk coefficients or empirical data',sites=sites,bonds=b,rows=rows),indent=2)+'\n')
