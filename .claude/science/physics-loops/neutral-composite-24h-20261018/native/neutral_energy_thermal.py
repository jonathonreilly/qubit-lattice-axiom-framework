"""Small open native Hamiltonian check of source high-temperature Taylor coefficient."""
import numpy as np,json
from scipy.linalg import eigh

def run():
 states=np.arange(64);H=np.zeros((64,64));Jx=.7;Jz=1.3
 for x in range(2):
  for z in range(2):
   i=3*x+z;j=i+1;H[np.diag_indices(64)]+=-Jz*(1-2*((states>>i ^ states>>j)&1))
 for z in range(3):H[states^((1<<z)|(1<<(z+3))),states]+=-Jx
 C=np.diag(sum(1-2*((states>>(3*x) ^ states>>(3*x+2))&1) for x in range(2)))
 E,U=eigh(H);c=np.diag(U.T@C@U);rows=[];v0=3*Jx**2+4*Jz**2
 for beta in [.02,.01,.005]:
  w=np.exp(-beta*E);w/=sum(w);cm=w@c;em=w@E;cov=w@(c*E)-cm*em;var=w@(E*E)-em**2
  rows.append(dict(beta=beta,C_mean=cm,mean_over_beta2=cm/beta**2,covariance=cov,coupling_over_beta=cov/var/beta,predicted_mean_coefficient=2*Jz**2,predicted_coupling_coefficient=-4*Jz**2/v0))
 assert abs(rows[-1]['mean_over_beta2']-2*Jz**2)<.001
 assert abs(rows[-1]['coupling_over_beta']+4*Jz**2/v0)<.001
 return dict(status='PASS',rows=rows,scope='Six physical sites, open2x1x3, finite Gibbs Taylor control; no thermodynamic remainder or state derivation')
if __name__=='__main__':
 r=run();print(json.dumps(r,indent=2));open(__file__.replace('.py','.json'),'w').write(json.dumps(r,indent=2)+'\n')
