from pathlib import Path
import json
import numpy as np
import quimb.tensor as qtn
from scipy.linalg import eigh
from native_mpo import build,X,expectation
def main():
 qtn.set_contract_strategy('greedy')
 H=build((2,2,2));dense=H.to_dense();g=np.random.default_rng(191001).normal(size=256);g/=np.linalg.norm(g)
 m=qtn.MatrixProductState.from_dense(g,dims=[2]*8);vs=[m]
 for sites in [[1,2],[1,2,5,6]]:
  v=m.copy()
  for i in sites:v.gate_(X,i,contract=True)
  vs.append(v)
 V=np.column_stack([v.to_dense().reshape(-1) for v in vs]);n=len(vs)
 GG=np.array([[float(np.real(a.H@b)) for b in vs] for a in vs]);HH=np.array([[expectation(a,H,b) for b in vs] for a in vs]);QQ=np.array([[float(np.real(qtn.expec_TN_1D(a.H,H,H,b))) for b in vs] for a in vs])
 e=HH[0,0];C=np.vstack((-GG[0,1:],np.eye(n-1)));G=C.T@GG@C;K=C.T@(HH-e*GG)@C;Q=C.T@(QQ-2*e*HH+e*e*GG)@C
 B=V@C;HB=(dense-e*np.eye(256))@B
 errors=[float(np.max(abs(G-B.T@B))),float(np.max(abs(K-B.T@HB))),float(np.max(abs(Q-HB.T@HB)))]
 ev,c=eigh(K,G);Y=B@c;rr=np.linalg.norm((dense-e*np.eye(256))@Y-Y*ev,axis=0);rr2=np.sqrt(np.maximum(0,np.diag(c.T@Q@c)-ev**2));errors.append(float(max(abs(rr-rr2))))
 assert max(errors)<1e-10
 out=dict(max_error=max(errors),reference_residual=float(np.linalg.norm(dense@g-e*g)),scope='Dense versus tensor centered moments and full residuals with deliberately nonstationary reference')
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)

if __name__=="__main__":main()
