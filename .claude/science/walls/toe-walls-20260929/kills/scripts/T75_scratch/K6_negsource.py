"""F1 exterior with a source term: phi'' = -c phi/x^2 (c=1/4 from negative amplitude energy density). phi=x^s, s(s-1)=-c.
Check lattice version: phi_{x+1}+phi_{x-1}-2phi_x = -c phi_x/x^2 has solution ~ x^{1/2} at large x; exponent of w=phi^2."""
import numpy as np
c=0.25
N=4000
# integrate recursion from x=200 with phi=x^0.5 seed, using second-order recursion, check p=2*dlnphi/dlnx
x=np.arange(0,N+1.)
phi=np.zeros(N+1); phi[100]=100**.5; phi[101]=101**.5
for k in range(101,N):
    phi[k+1]=2*phi[k]-phi[k-1]-c*phi[k]/k**2
for n in (200,500,1000,3000):
    print(n, "p(w=phi^2)=", (2*(np.log(phi[n+1])-np.log(phi[n-1]))/(np.log(n+1)-np.log(n-1))))
# sign: energy density e_x = phi_x (K phi)_x with K = -c*12/gamma/x^2-ish <0 : negative. positive c (K>0) gives s>=1
for c2 in (0.5,2):
    import math
    s=(1+math.sqrt(1+4*c2))/2; print("positive K, c=",c2,"phi ~ x^s, w exponent",2*s)
