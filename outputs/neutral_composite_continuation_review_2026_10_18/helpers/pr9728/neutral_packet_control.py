"""Declared leading crossover packet checks; not higher-order native dynamics."""
from pathlib import Path
import json,numpy as np
from scipy.linalg import eigh
rows=[]
for lam in [.1,.03,.01,.003]:
 M=int(np.ceil(lam**-1.5));j=np.arange(1,M+1);f=np.sqrt(2/(M+1))*np.sin(np.pi*j/(M+1))
 moment=float(2*np.dot(f,f)-2*np.dot(f[:-1],f[1:]));exact=4*np.sin(np.pi/(2*(M+1)))**2
 assert abs(moment-exact)<2e-15
 eta=lam**.125
 rows.append(dict(lam=lam,M=M,eta=eta,moment=moment,exact_moment=float(exact),tail_bound=float(exact/(4*np.sin(lam*eta/2)**2)),correlation_error_power_factor=float(M*lam**4),relative_error_power_factor=float(M*lam**2)))
modes=[]
for k in [0,.001,.003,.01,.03,.1]:
 n=180;A=np.diag(np.full(n,-.5));A[0,0]=.5
 for d,v in [(1,k),(2,.25)]:A+=np.diag(np.full(n-d,v),d)+np.diag(np.full(n-d,v),-d)
 H=np.zeros((n+1,n+1));H[:n,:n]=A;H[n,n]=-2;H[n,1]=H[1,n]=-np.sqrt(2)
 e,u=eigh(H,subset_by_index=[n-1,n]);res=float(u[0,-1]**2)
 if k==0:assert abs(e[-1]-9/16)<1e-13 and abs(res-15/16)<1e-13
 modes.append(dict(kappa=k,energy=float(e[-1]),residue=res,source_coefficient=4*res,other_upper=float(e[-2])))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(packet=rows,modes=modes,scope='Leading crossover and envelope controls only; constants of native remainder not numerically estimated'),indent=2)+'\n')
print(json.dumps(dict(packet=rows,modes=modes)))
