import numpy as np
from common import sets
def masses_from(r,delta,a=1.0):
    k=np.arange(3); s=a*(1+2*np.sqrt(r)*np.cos(delta+2*np.pi*k/3)); return np.sort(s**2)
ms=sets['PDG2024']; m=np.array([ms['e'][0],ms['mu'][0],ms['tau'][0]])
print('data ratios: mu/e = %.5f  tau/e = %.3f'%(m[1]/m[0],m[2]/m[0]))
print('%-4s %-5s | r=p  delta=2p/(9 a_d) | mu/e (pred)   tau/e (pred)  | verdict'%('p','a_d'))
for p in (1.0,0.5):
    for ad in (0.5,1.0,2.0):
        r=p; d=2*p/(9*ad)
        if p==1.0:
            # r=1 : Q=1 -> smallest mass is 0 or negative sqrt; show as-is
            pass
        mm=masses_from(r,d)
        e,mu,ta=mm
        ok = (abs(mu/e/(m[1]/m[0])-1)<1e-4) and (abs(ta/e/(m[2]/m[0])-1)<2e-4)
        print('%-4.1f %-5.1f | r=%.2f delta=%.5f  | %-12.5g %-13.4g | %s'%(p,ad,r,d,mu/e if e>0 else float('nan'),ta/e if e>0 else float('nan'),'MATCH' if ok else 'no'))
# scale-free variant: Phi=Tr(A^-1 P_d)/Tr(A^-1) = 2 a_s/(a_d+2 a_s), r=(a_s/a_d)/2  => Phi = 4r/(1+4r)
print('\nscale-free normalised response: 3 delta = 4r/(1+4r)')
from common import dial
for nm,mm in {'lepton (PDG2024)':list(m),'down (M_Z)':[2.69e-3,0.0535,2.86],'up (M_Z)':[1.24e-3,0.624,171.7]}.items():
    q,r,d=dial(mm); print(' %-18s r=%.5f  delta_obs=%.5f  delta_pred=%.5f'%(nm,r,d,4*r/(1+4*r)/3))
