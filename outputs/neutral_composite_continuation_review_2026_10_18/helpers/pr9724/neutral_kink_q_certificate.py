"""Finite native derivation of local relative-chain coefficients at fixed momentum."""
from pathlib import Path
import numpy as np,json
from neutral_kink_core import band,h
rows=[]
for L in [12,16]:
 H1,H2,H3,states,_=band(L,third=True);lookup={x:i for i,x in enumerate(states)};powers=[8**j for j in range(L)]
 for mode in range(3*L//8+1): # fixed away from the collapsed q=pi bright bandwidth
  q=2*np.pi*mode/L;u=np.cos(q);c=np.cos(q/2);t=2*c;source=np.zeros(len(states),complex)
  for a in range(8):
   vac=sum(a*p for p in powers)
   for j,power in enumerate(powers):
    for new in np.flatnonzero(h[:,a]):
     r=lookup.get(vac+(int(new)-a)*power)
     if r is not None:source[r]+=h[new,a]*np.exp(1j*q*j)/np.sqrt(8*L)
  cur=source/np.linalg.norm(source);Q=[]
  for i in range(L//2-(mode%2)):
   Q.append(cur);v=H1@cur
   for _ in range(2):
    for old in Q:v-=old*np.vdot(old,v)
   b=np.linalg.norm(v)
   if b<1e-10:break
   cur=v/b
  Q=np.array(Q).T;assert np.linalg.norm(H1@Q-Q@(Q.conj().T@(H1@Q)))<1e-8
  R=H2@Q-Q@(Q.conj().T@(H2@Q));vv,sv,_=np.linalg.svd(R,full_matrices=False)
  assert sum(sv>1e-9)==1,(L,mode,Q.shape,sv.tolist())
  extra=vv[:,0];coupling=np.vdot(Q[:,1],H2@extra);extra*= -np.conjugate(coupling)/abs(coupling)
  W=np.column_stack([Q,extra]);A=W.conj().T@(H1@W);B=W.conj().T@(H2@W);C=W.conj().T@(H3@W)
  # Compare local entries only, before finite-chain folded terminal.
  checks=[A[0,1]-t,A[1,2]-t,B[0,0]-(1-u)/4,B[1,1]+.5,B[0,2]+u/4,B[1,-1]+np.sqrt(2),B[-1,-1]+2,C[0,1]-t*(-39+6*u)/64,C[1,2]+5*t/16,C[0,3]-t*(2*u-1)/32,C[0,-1]+np.sqrt(2)*c,C[2,-1]-c/np.sqrt(2)]
  err=float(max(abs(x) for x in checks));closure=float(np.linalg.norm(H3@W-W@C));assert err<1e-10 and closure<1e-10,(L,mode,err,closure)
  rows.append(dict(L=L,mode=mode,q=q,local_coefficient_error=err,third_order_closure=closure))
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2));print('finite local coefficients',len(rows),'maxerror',max(x['local_coefficient_error'] for x in rows))
