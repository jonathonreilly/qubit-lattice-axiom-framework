"""Test C3 (exploratory, post-hoc redesign of Test C): translation-invariant single walker.
psi_x = e^{i k0 x}/sqrt(L) |up>, uniform P, uniform current, Bell rate lam = cos k0 to the right.
rho_0 = (1/L)(1 + eps cos(q x)).  Exact solution: Fourier mode damped by exp(-lam T (1 - cos q)).
Numerics: same generator code path as the other tests."""
import numpy as np, scipy.sparse as sp
from scipy.integrate import solve_ivp
from common import Ring, kl
L=160; x=np.arange(L); k0=0.0
ring=Ring(L)
psi0=(np.exp(1j*k0*x)[:,None]*np.array([1.0,0.0])[None,:]).astype(complex)/np.sqrt(L)
SZ=np.array([1.0,-1.0])
def wave(t):
    U=ring.U4(t); return np.einsum('aixj,xj->ai',U,psi0)
def gen(t):
    psi=wave(t); P=(np.abs(psi)**2).sum(1)
    T=np.real((np.roll(psi,-1,axis=0).conj()*SZ[None,:]*psi).sum(1))
    Pinv=1/P
    rp=np.maximum(T,0)*Pinv; rm=np.maximum(-np.roll(T,1),0)*Pinv
    idx=np.arange(L)
    rows=np.concatenate([(idx+1)%L,(idx-1)%L,idx]); cols=np.concatenate([idx,idx,idx])
    return P, sp.csc_matrix((np.concatenate([rp,rm,-(rp+rm)]),(rows,cols)),shape=(L,L))
T=30.0; eps=0.5
print('rate check', gen(0.0)[1][1,0], 'expected cos k0 =', np.cos(k0))
out=[]
for m in [1,2,4,8,16,32]:
    q=2*np.pi*m/L
    rho0=(1+eps*np.cos(q*x))/L
    sol=solve_ivp(lambda t,y: gen(t)[1]@y,(0,T),rho0,method='Radau',jac=lambda t,y:gen(t)[1],t_eval=[0,T],rtol=1e-11,atol=1e-15)
    P=gen(T)[0]
    D0=kl(rho0,P); DT=kl(sol.y[:,-1],P)
    pred=2*np.cos(k0)*T*(1-np.cos(q))
    out.append((m,-np.log(DT/D0),pred))
    print(f"m={m:2d} ell=L/(2pi m)={L/(2*np.pi*m):6.2f}  D0={D0:.4e} DT={DT:.4e}  -ln(DT/D0)={-np.log(DT/D0):.4f}  exact-mode prediction 2*lam*T*(1-cos q)={pred:.4f}")
ms=np.array([o[0] for o in out],float); nl=np.array([o[1] for o in out])
print('fitted exponent p (m=1..8):', np.polyfit(np.log(ms[:4]),np.log(nl[:4]),1)[0])
