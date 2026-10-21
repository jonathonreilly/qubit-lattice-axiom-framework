import numpy as np
from scipy.integrate import quad
from scipy.special import ai_zeros
import json

def gd(E):
 # Upper-half-plane boundary value integrated analytically in y.
 cuts=[0,np.pi]
 for s in [-4,4]:
  c=(s-E)/4
  if -1<c<1:cuts.append(float(np.arccos(c)))
 cuts=sorted(cuts)
 def f(x):
  c=np.cos(x); z=complex(E+4*c,0.)
  den=np.sqrt(z-4)*np.sqrt(z+4)
  return (2*c+E/4)**2/den
 re=im=0.
 for a,b in zip(cuts[:-1],cuts[1:]):
  re+=quad(lambda x:f(x).real,a,b,epsabs=1e-11,limit=300)[0]
  im+=quad(lambda x:f(x).imag,a,b,epsabs=1e-11,limit=300)[0]
 return complex(re,im)/np.pi-E/16
G=gd(-4);sig=4*G;a=sig/(2+sig);b=1-a
rows=[]
for lam in [.2,.1,.05,.025]:
 f=lam**3/16;L=(2/f)**(1/3)
 rows.append(dict(lam=lam,length=L,spacing_scale=lam*2**(1/3)*f**(2/3),width=-2*lam*f*a.imag))
out=dict(G=[G.real,G.imag],self_energy=[sig.real,sig.imag],scattering_length=[a.real,a.imag],endpoint_length=[b.real,b.imag],rows=rows,scope='Host-plus-string coefficient model only; not native resonance proof')
print(json.dumps(out,indent=2));open('/private/tmp/neutral_bulk_resonance.json','w').write(json.dumps(out,indent=2))
from scipy.sparse import diags
from scipy.sparse.linalg import eigs
z1=abs(ai_zeros(1)[0][0]);checks=[]
for lam in [.3,.2,.1,.05,.025]:
 f=lam**3/16; L=(2/f)**(1/3);N=int(14*L)
 diagonal=f*(np.arange(N)+2).astype(complex);diagonal[0]+=sig
 H=diags([-2*np.ones(N-1),diagonal,-2*np.ones(N-1)],[-1,0,1],format='csc')
 pred=-4+2**(1/3)*f**(2/3)*z1+f*(1+a)
 es,vs=eigs(H,k=1,sigma=pred,tol=1e-12);e=es[0];u=vs[:,0]
 residue=8*lam**2*G**2*u[0]**2/(u@u)
 residue_asym=G**2*b**2/4*lam**5
 row=dict(lam=lam,N=N,energy=[e.real,e.imag],prediction=[pred.real,pred.imag],width_over_lambda4=-2*lam*e.imag/lam**4,complex_readout_residue_over_lambda5=[residue.real/lam**5,residue.imag/lam**5],asymptotic_residue_over_lambda5=[residue_asym.real/lam**5,residue_asym.imag/lam**5],residual=float(np.linalg.norm(H@u-e*u)))
 checks.append(row)
out['frozen_boundary_controls']=checks
out['edge_product']=float((2/np.pi-.5)*(4-2*np.sqrt(3)))
print(json.dumps(checks,indent=2));open('/private/tmp/neutral_bulk_resonance.json','w').write(json.dumps(out,indent=2)+'\n')
