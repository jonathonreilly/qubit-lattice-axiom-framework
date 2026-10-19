"""Outgoing native K1+lambda K2 fast host, before native rank-one contact."""
import numpy as np,json
from scipy.integrate import quad_vec
from math import comb

def mu(m):return comb(m,m//2)/2**m if m%2==0 else 0.
def host(z,lam):
 z=complex(z);B0=4-2*lam;C0=z+4+lam;c0=-2*C0/(B0+np.sqrt(B0*B0-4*lam*C0));k0=np.arccos(c0)
 def integrand(u,openchannel):
  k=k0*(1-u*u) if openchannel else k0+(np.pi-k0)*u*u
  jac=2*k0*u if openchannel else 2*(np.pi-k0)*u
  x=np.cos(k);B=4-2*lam*x;C=z+4*x+lam*x*x;disc=np.sqrt(B*B-4*lam*C)
  r=-2*C/(B+disc);R=-B/lam-r
  I0=-1j/np.sqrt(1-r*r) if openchannel else -1/np.sqrt(r*r-1)
  moments=[]
  for m in range(5):
   Ir=r**m*I0+sum(r**j*mu(m-1-j) for j in range(m))
   IR=-sum(mu(m+j)/R**(j+1) for j in range(20))
   moments.append((Ir-IR)/disc) # lam*(r-R)=disc
  a,b,c,d,e=moments
  return jac*np.array([x*x*a-2*x*b+c,2*(x**3*a-x*x*b-x*c+d),4*(x**4*a-2*x*x*c+e)])/np.pi
 v=quad_vec(lambda u:integrand(u,True),0,1,epsabs=2e-10,epsrel=2e-10)[0]+quad_vec(lambda u:integrand(u,False),0,1,epsabs=2e-10,epsrel=2e-10)[0]
 return np.array([[v[0],v[1]],[v[1],v[2]]])
if __name__=='__main__':
 rows=[]
 # Physical upper-half-plane control by direct periodic quadrature (outgoing continuation agrees there).
 n=1600;c=np.cos(2*np.pi*(np.arange(n)+.5)/n);x=c[:,None];y=c[None,:];d=x-y;d2=2*(x*x-y*y)
 for lam in [.02,.1,.2]:
  z=-6*lam+.15j;den=z+4*(x+y)+lam*d*d
  direct=np.array([[np.mean(d*d/den),np.mean(d*d2/den)],[np.mean(d*d2/den),np.mean(d2*d2/den)]])
  value=host(z,lam);error=np.max(abs(direct-value));assert error<1e-8,(lam,error,direct,value)
  rows.append(dict(kind='direct_upper',lam=lam,error=float(error)))
 for lam in [.2,.1,.05,.025,.0125,.00625,.003125]:
  z=-6*lam-1j*.06*lam**3;G=host(z,lam);contact=G+lam*np.outer(G[:,0],G[0,:])/(1-lam*G[0,0]);row=dict(kind='outgoing',lam=lam,z=[z.real,z.imag],G=[[[v.real,v.imag] for v in r] for r in G],contact=[[[v.real,v.imag] for v in r] for r in contact]);rows.append(row);print(row,flush=True)
 open('/private/tmp/neutral_corrected_fast_host.json','w').write(json.dumps(rows,indent=2)+'\n')
