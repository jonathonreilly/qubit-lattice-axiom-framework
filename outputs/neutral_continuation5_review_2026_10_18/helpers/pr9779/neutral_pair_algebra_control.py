import numpy as np,itertools
rng=np.random.default_rng(327)
for N in [4,5,6,8]:
 f=np.zeros((N,N),complex)
 for i in range(N):
  for j in range(i+1,N):f[i,j]=f[j,i]=rng.normal()+1j*rng.normal()
 f/=np.sqrt(np.sum(np.abs(f)**2)/2)
 Phi=f/np.sqrt(2);rho=Phi@Phi.conj().T
 exact=0
 for i,j,k,l in itertools.combinations(range(N),4):
  exact+=abs(2*(f[i,j]*f[k,l]+f[i,k]*f[j,l]+f[i,l]*f[j,k]))**2
 formula=2+4*np.trace(rho@rho).real-16*np.sum(np.diag(rho).real**2)+4*sum(abs(f[i,j])**4 for i in range(N) for j in range(i+1,N))
 print(N,exact,formula,abs(exact-formula));assert abs(exact-formula)<1e-12
