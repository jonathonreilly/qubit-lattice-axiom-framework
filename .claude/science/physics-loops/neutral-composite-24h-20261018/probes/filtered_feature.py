"""Construct large neutral filtered features and measure source-overlap tradeoff."""
from pathlib import Path
import numpy as np,json,itertools
from scipy.special import expit
R=Path(__file__).resolve().parents[5];d=json.loads((R/'data/collective_corner_response/candidate.json').read_text());sh=np.array(d['shifts']);bl=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);M=np.array(d['mass_matrix']['real'])+1j*np.array(d['mass_matrix']['imag']);mu=d['chemical_potential_development_value']
def bands(k):return np.linalg.eigh(np.einsum('ks,sij->kij',np.exp(1j*k@sh.T),bl))
rows=[]
for N in [12,24,36]:
 k=2*np.pi/N*(np.array(list(itertools.product(range(N),repeat=3)))+.5);e,U=bands(k);eo,Uo=bands(k+np.pi);V=Uo.conj().transpose(0,2,1)@M@U
 de=(eo[:,:,None]-e[:,None,:]).ravel();f=expit((mu-e)/.03);fo=expit((mu-eo)/.03)
 w=(f[:,None,:]*(1-fo[:,:,None])*abs(V)**2/len(k)).ravel();total=w.sum();w=w/total
 for center in [.2,.3]:
  for tau in [4,8,16,32,64,128,256]:
   F=np.exp(-.5*(tau*(de-center))**2);z=np.dot(w,F*F);overlap=np.dot(w,F)**2/z
   p=w*F*F/z;mean=np.dot(p,de);width=np.sqrt(np.dot(p,(de-mean)**2));row={'N':N,'T':.03,'center':center,'tau':tau,'filtered_norm_squared':float(z),'normalized_source_overlap_squared':float(overlap),'frequency_mean':float(mean),'frequency_std':float(width),'tau_times_overlap_squared':float(tau*overlap),'tau_times_std':float(tau*width)};rows.append(row)
   print(N,center,tau,round(overlap,6),round(tau*overlap,5),round(tau*width,5),flush=True)
Path(__file__).with_name('filtered_feature.json').write_text(json.dumps({'scope':'Full positive structure-factor measure, supplied finite-T ensemble. Gaussian time filtering is constructed preparation, not new dynamics or physical scalar. Coupling metric is normalized overlap with original source, not gravitational coupling.','rows':rows},indent=2)+'\n')
