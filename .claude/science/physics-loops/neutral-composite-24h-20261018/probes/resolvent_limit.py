"""Unrestricted neutral filter in HS and thermal norms; exposed development inputs."""
from pathlib import Path
import json,itertools,numpy as np
from scipy.special import expit
P=Path(__file__).resolve().parent;R=P.parents[4];d=json.loads((R/'data/collective_corner_response/candidate.json').read_text());s=np.array(d['shifts']);b=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);m=np.array(d['mass_matrix']['real'])+1j*np.array(d['mass_matrix']['imag']);rows=[]
for N in [12,24,36]:
 k=2*np.pi*(np.array(list(itertools.product(range(N),repeat=3)))+.5)/N;q=np.ones(3)*np.pi
 e,u=np.linalg.eigh(np.einsum('ks,sab->kab',np.exp(1j*k@s.T),b));eq,uq=np.linalg.eigh(np.einsum('ks,sab->kab',np.exp(1j*(k+q)@s.T),b));delta=eq[:,:,None]-e[:,None,:];B=uq.conj().transpose(0,2,1)@m@u
 f=expit((-2.28284271247462-e)/.03);fq=expit((-2.28284271247462-eq)/.03)
 for metric in ['HS','thermal']:
  w=abs(B)**2
  if metric=='thermal':w*=f[:,None,:]*(1-fq[:,:,None])
  w/=w.sum()
  for eta in [.1,.01,.001,.0001,.00001]:
   F=eta/((delta-.2)**2+eta);z=np.sum(w*F**2);a=np.sum(w*F);v=w*F**2/z;mean=np.sum(v*delta);std=np.sqrt(np.sum(v*(delta-mean)**2));res=np.sqrt(np.sum(v*(delta-.2)**2))
   rows.append(dict(N=N,metric=metric,eta=eta,overlap_squared=float(a*a/z),mean=float(mean),std=float(std),target_residual=float(res)))
 print(N,rows[-1],flush=True)
(P/'resolvent_limit.json').write_text(json.dumps({'scope':'Infinite spatial-support spectral filter on finite periodic grids; fixed chosen center .2 and supplied state. Not an independent particle or derived scalar interaction','rows':rows},indent=2)+'\n')
