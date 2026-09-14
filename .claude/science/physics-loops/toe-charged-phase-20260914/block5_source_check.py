from pathlib import Path
import json,itertools
import numpy as np
from block5_tensor_check import incidence,pairs

def fields_from_source(rho,L):
 rh=np.fft.fftn(rho.reshape((L,)*3));freq=2*np.pi*np.fft.fftfreq(L)
 rf=np.zeros((L,L,L,6),dtype=complex);hf=np.zeros_like(rf);green=0.
 for ind in itertools.product(range(L),repeat=3):
  k=np.array([freq[i] for i in ind]);qh=2*np.sin(k/2);q2=qh@qh
  if q2<1e-20:continue
  P=np.eye(3)-np.outer(qh,qh)/q2
  for a,(i,j) in enumerate(pairs):
   offset=np.zeros(3)
   if i!=j:offset[i]=offset[j]=.5
   phase=np.exp(1j*k@offset)
   rf[ind+(a,)]=rh[ind]*P[i,j]*phase/2
   hf[ind+(a,)]=-rh[ind]*P[i,j]*phase/(2*q2)
  green+=abs(rh[ind])**2/q2
 R=np.fft.ifftn(rf,axes=(0,1,2));h=np.fft.ifftn(hf,axes=(0,1,2))
 assert np.max(abs(R.imag))<1e-13 and np.max(abs(h.imag))<1e-13
 return R.real.reshape(-1),h.real.reshape(-1),green/L**3

rows=[]
for L in [3,5]:
 G,S,T,sites=incidence(L);n=len(sites);w=np.tile([1.,1.,1.,2.,2.,2.],n)
 rho=np.zeros(n);rho[0]=1;rho[1]=-1
 R,h,green=fields_from_source(rho,L)
 assert np.max(abs(G@R))<1e-13 and np.max(abs(T@R-rho))<1e-13
 # q's off-diagonal components are doubled, unlike the physical tensor h.
 assert np.max(abs(S@(w*h)-rho))<1e-13
 assert np.max(abs(R.reshape(n,6).mean(axis=0)))<1e-13
 A=np.vstack([G,T]);b=np.r_[np.zeros(3*n),rho];wi=1/w
 v=wi*(A.T@np.linalg.lstsq((A*wi)@A.T,b,rcond=1e-12)[0])
 assert np.max(abs(v-R))<2e-13
 El=np.dot(w*R,R)/2;En=np.dot(w*h,R)/2
 assert abs(El-np.dot(rho,rho)/4)<1e-13
 assert abs(En+green/4)<1e-13
 # Noncompact constraint invariance: the scalar direction is null in the
 # constrained kinetic form, but not before vector reduction.
 rows.append({'L':L,'Fourier_vs_real_variational_field_error':float(np.max(abs(v-R))),'actual_metric_scalar_constraint_error':float(np.max(abs(S@(w*h)-rho))),'L_static_energy_over_g':float(El),'N_static_energy_over_g':float(En),'independent_inverse_Laplacian_value':float(-green/4)})
Path(__file__).with_name('BLOCK5_SOURCE_CHECK.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows,indent=2))
