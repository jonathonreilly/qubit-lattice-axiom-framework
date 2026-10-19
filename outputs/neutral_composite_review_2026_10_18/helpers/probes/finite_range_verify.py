"""Independent momentum-space verification and thermal response of saved features."""
from pathlib import Path
import json,itertools,numpy as np
from scipy.special import expit
P=Path(__file__).resolve().parent;R=P.parents[3]
d=json.loads((R/'data/collective_corner_response/candidate.json').read_text())
s=np.array(d['shifts']);b=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);m=np.array(d['mass_matrix']['real'])+1j*np.array(d['mass_matrix']['imag'])
z=np.load(P/'finite_range_modes.npz');prior=json.loads((P/'finite_range_mode.json').read_text());q=np.ones(3)*np.pi
print(d.keys(),flush=True)
mu=-2.28284271247462;rows=[]
for N in [8,16,24]:
 k=2*np.pi*(np.array(list(itertools.product(range(N),repeat=3)))+.5)/N
 h=np.einsum('ks,sab->kab',np.exp(1j*k@s.T),b);hq=np.einsum('ks,sab->kab',np.exp(1j*(k+q)@s.T),b)
 e,u=np.linalg.eigh(h);eq,uq=np.linalg.eigh(hq);delta=eq[:,:,None]-e[:,None,:]
 f=expit((mu-e)/.03);fq=expit((mu-eq)/.03);w=f[:,None,:]*(1-fq[:,:,None])
 source=uq.conj().transpose(0,2,1)@m@u;sn=np.sum(w*abs(source)**2)
 for old in prior['rows']:
  r=old['range_L1'];eta=old['eta'];c=z[f'r{r}_eta{eta}'];coords=z[f'coords{r}']
  M=np.einsum('kr,rab->kab',np.exp(1j*k@coords.T),c)
  LM=hq@M-M@h;norm=np.sum(abs(M)**2)/len(k);res=np.sqrt(np.sum(abs(LM-.2*M)**2)/len(k))
  # N>2*(r+1) integrates all relevant Laurent products exactly.
  if N>2*(r+1):
   assert abs(norm-1)<1e-10
   assert abs(res-old['normalized_HS_residual'])<1e-10
  v=uq.conj().transpose(0,2,1)@M@u;ww=w*abs(v)**2;vn=ww.sum();mean=np.sum(ww*delta)/vn;std=np.sqrt(np.sum(ww*(delta-mean)**2)/vn)
  overlap=abs(np.sum(w*source.conj()*v))**2/(sn*vn)
  residual2=std**2+(mean-.2)**2
  source_measure=w*abs(source)**2/sn
  bounds=[(residual2+t)*np.sum(source_measure/((delta-.2)**2+t)) for t in [1e-5,1e-4,.001,.01,.1,1.]]
  bound=min(1.,min(bounds));assert overlap<=bound+1e-10
  rows.append(dict(N=N,radius=r,eta=eta,HS_norm=float(norm),HS_residual=float(res),thermal_mean=float(mean),thermal_std=float(std),thermal_source_overlap_squared=float(overlap),thermal_target_residual=float(np.sqrt(residual2)),source_overlap_bound=float(bound)))
 print(N,rows[-1],flush=True)
(P/'finite_range_verify.json').write_text(json.dumps(dict(scope='Momentum-space independent check; supplied grand-canonical state mu, T=.03; full signed transition frequencies, positive structure weights; thermal overlap is not canonical coupling',mu=mu,T=.03,rows=rows),indent=2)+'\n')
