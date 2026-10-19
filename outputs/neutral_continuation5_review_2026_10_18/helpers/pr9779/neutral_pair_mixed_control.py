import numpy as np,itertools,json
rng=np.random.default_rng(2026101801);errs=[]
for n in range(4,13):
 for rep in range(3):
  f=np.zeros((n,n),complex);x=np.zeros_like(f)
  for i,j in itertools.combinations(range(n),2):
   f[i,j]=rng.normal()+1j*rng.normal();f[j,i]=f[i,j];x[i,j]=rng.normal()+1j*rng.normal();x[j,i]=x[i,j]
  f/=np.sqrt(np.sum(abs(f)**2)/2);x/=np.sqrt(np.sum(abs(x)**2)/2);Phi=f/np.sqrt(2);Xi=x/np.sqrt(2);rho=Phi@Phi.conj().T;a=np.trace(Phi.conj().T@Xi)
  direct=0j
  for i,j,k,l in itertools.combinations(range(n),4):
   b2=2*(f[i,j]*f[k,l]+f[i,k]*f[j,l]+f[i,l]*f[j,k])
   fb=x[i,j]*f[k,l]+f[i,j]*x[k,l]+x[i,k]*f[j,l]+f[i,k]*x[j,l]+x[i,l]*f[j,k]+f[i,l]*x[j,k]
   direct+=b2.conjugate()*fb
  formula=2*a+4*np.trace(Phi.conj().T@Phi@Phi.conj().T@Xi)-16*np.sum(np.diag(rho)*np.diag(Xi@Phi.conj().T))+2*np.sum(abs(f)**2*f.conj()*x)
  errs.append(abs(direct-formula));assert errs[-1]<1e-12
print(json.dumps(dict(cases=len(errs),max_error=max(errs)),indent=2))
