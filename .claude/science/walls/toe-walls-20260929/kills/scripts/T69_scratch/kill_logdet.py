"""(1) The wall's own W = log|det D| with D = H_w = phi H phi: its u-dependence is exactly linear (zero Hessian).
   (2) Free-sea double-occupancy fraction (one record per site test).
   (3) family-3 spread on the attack's own registered mu values {0,0.25,0.4}."""
import numpy as np, sys
from kill_checks import build_H, coords
import scipy.sparse as sp
L=4; H=build_H(L); N=L**3; C=coords(L)
rng=np.random.default_rng(1)
def logdet(u):
    phi=np.exp(np.repeat(u,2)/2); Hw=(sp.diags(phi)@H@sp.diags(phi)).toarray()
    sgn,ld=np.linalg.slogdet(Hw); return ld
u0=np.zeros(N); base=logdet(u0)
for trial in range(3):
    u=0.3*rng.standard_normal(N)
    pred=base+np.sum(2*u)/1.0   # log|det(phi H phi)| = log|det H| + 2 sum_x tr log phi_x = log|det H| + sum_x 2*u_x*(1/2)*2 comps
    print('logdet(u)-logdet(0) =',logdet(u)-base,' vs sum_x 2 u_x =',2*u.sum(),' diff',logdet(u)-base-2*u.sum())
# second difference in eps for a cosine
q=2*np.pi*np.array([1,0,0])/L
f=lambda e: logdet(e*np.cos(C@q))
e=0.05; print('second difference of log-det along cos mode (should be 0):',(f(e)+f(-e)-2*f(0))/e**2)
# (2) double occupancy in the free sea: P_- projector local block
Hd=H.toarray(); w,v=np.linalg.eigh(Hd); Pm=v[:,w<0]@v[:,w<0].conj().T
occ=[]; dbl=[]
for x in range(N):
    B=Pm[2*x:2*x+2,2*x:2*x+2]           # <c_a^dag c_b>
    n_up,n_dn=B[0,0].real,B[1,1].real; off=B[0,1]
    dbl.append(n_up*n_dn-abs(off)**2); occ.append(n_up+n_dn)
print('free sea L=4: mean occupation per site',np.mean(occ),' P(double occ.) mean',np.mean(dbl),' P(empty)=',np.mean([ (1-B)  for B in [0]]) if False else '')
# P(empty) = det(1-B), P(single)=...
emp=[]
for x in range(N):
    B=Pm[2*x:2*x+2,2*x:2*x+2]; emp.append(np.linalg.det(np.eye(2)-B).real)
print('P(empty) mean',np.mean(emp),' => P(single)=',1-np.mean(emp)-np.mean(dbl))
